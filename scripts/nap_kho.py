#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""nap_kho.py — Hộp thư nạp kho: xử lý tệp Bạn kéo thả vào _inbox/ trên GitHub (Bạn chốt 09/10/2026).

Workflow .github/workflows/nap-kho.yml chạy script này mỗi khi có push vào _inbox/. Với mỗi tệp
.pdf/.doc/.docx/.xlsx trong _inbox/:
  1. Bóc chữ (scripts/trich_chu_van_ban_goc.py) và đọc số hiệu, ngày ban hành, cơ quan, trích yếu
     bằng script — không đọc bằng mắt; số, ngày không đọc được thì để trống và ghi rõ trong PR.
  2. Đoán plugin chủ theo bảng từ khóa TU_KHOA (tên tệp + 5.000 ký tự đầu). Không đoán được →
     vbhc-vn/skills/vbhc-vn/van-ban-goc/chua-phan-loai/ và ghi rõ trong PR.
  3. Đổi tên chuẩn  YYYY.MM.DD-SỐ.KÝ.HIỆU-Tên-trích-yếu-ngắn.<đuôi gốc>  (thiếu ngày hoặc số thì giữ tên gốc),
     chuyển vào van-ban-goc/ của plugin chủ, sinh .txt cùng tên, chạy build_so_cai_van_ban_goc.py và
     export_ignore.py, xóa tệp khỏi _inbox/.
  4. Ghi tiêu đề, mô tả PR (số, ngày, plugin chủ, kết quả kiểm tra .txt, cảnh báo dung lượng: tệp > 3 MB
     không vào gói claude.ai; kho > 480 MB) ra thư mục --ket-qua để workflow mở PR "Nạp kho: [số hiệu] [tên]".

Chạy tay để thử:  python3 scripts/nap_kho.py --ket-qua /tmp/nap  (không commit, không push).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

sys.dont_write_bytecode = True  # không sinh __pycache__ (CI đỏ nếu còn; workflow nap-kho dùng git add -A)
REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import trich_chu_van_ban_goc as trich  # noqa: E402
import build_so_cai_van_ban_goc as so_cai  # noqa: E402

INBOX = REPO / "_inbox"
CHUA_PHAN_LOAI = REPO / "vbhc-vn" / "skills" / "vbhc-vn" / "van-ban-goc" / "chua-phan-loai"
MB = 1024 * 1024
NGUONG_TEP = 3 * MB
TRAN_KHO = 480 * MB

# (plugin, [(từ khóa, trọng số)]) — xét theo thứ tự; cụm càng đặc thù trọng số càng cao
TU_KHOA = [
    ("kho-vlncn-sct-vn", [("kho vật liệu nổ", 6), ("kho vlncn", 6), ("qcvn 01:2019", 6), ("kho chứa vật liệu nổ", 5)]),
    ("hl-vlncn-sct-vn", [("huấn luyện kỹ thuật an toàn", 5), ("giấy chứng nhận huấn luyện", 5), ("chỉ huy nổ mìn", 2)]),
    ("sd-vlncn-sct-vn", [("vật liệu nổ công nghiệp", 3), ("vlncn", 3), ("nổ mìn", 3), ("tiền chất thuốc nổ", 3)]),
    ("hc-sct-vn", [("hóa chất", 3), ("hoá chất", 3)]),
    ("hnh-sct-vn", [("hàng hóa nguy hiểm", 5), ("hàng hoá nguy hiểm", 5)]),
    ("kccn-sct-vn", [("cụm công nghiệp", 4), ("khu công nghiệp", 3)]),
    ("qlks-sct-vn", [("khoáng sản", 3), ("địa chất", 2)]),
    ("tkm-sct-vn", [("thiết kế mỏ", 5), ("thiết kế cơ sở mỏ", 5)]),
    ("attp-sct-vn", [("an toàn thực phẩm", 4), ("thực phẩm", 2)]),
    ("bvmt-sct-vn", [("bảo vệ môi trường", 3), ("khí nhà kính", 5), ("các-bon", 4), ("môi trường", 1)]),
    ("pccc-sct-vn", [("phòng cháy", 4), ("chữa cháy", 4)]),
    ("dat-dai-sct-vn", [("đất đai", 3), ("thu hồi đất", 4), ("bồi thường, hỗ trợ, tái định cư", 5)]),
    ("xp-sct-vn", [("xử phạt vi phạm hành chính", 4), ("xử phạt", 2)]),
    ("xd-sct-vn", [("hoạt động xây dựng", 4), ("xây dựng", 1)]),
    ("atvsld-sct-vn", [("an toàn, vệ sinh lao động", 5), ("vệ sinh lao động", 4)]),
    ("quy-hoach-ct-vn", [("quy hoạch", 2)]),
    ("sct-laocai-org-vn", [("cơ cấu tổ chức", 3), ("chức năng, nhiệm vụ, quyền hạn", 3), ("sở công thương tỉnh lào cai", 1)]),
]
TIEU_DE = re.compile(r"^\s*(NGHỊ ĐỊNH|THÔNG TƯ|QUYẾT ĐỊNH|LUẬT|NGHỊ QUYẾT|CHỈ THỊ|KẾ HOẠCH|THÔNG BÁO|KẾT LUẬN|CÔNG VĂN|BÁO CÁO)\s*$", re.M)
CO_QUAN = re.compile(r"^\s*(CHÍNH PHỦ|QUỐC HỘI|THỦ TƯỚNG CHÍNH PHỦ|ỦY BAN THƯỜNG VỤ QUỐC HỘI|UỶ BAN THƯỜNG VỤ QUỐC HỘI|"
                     r"BỘ [A-ZĐÀ-Ỹ ,]+|ỦY BAN NHÂN DÂN[A-ZĐÀ-Ỹ ]+|UỶ BAN NHÂN DÂN[A-ZĐÀ-Ỹ ]+|HỘI ĐỒNG NHÂN DÂN[A-ZĐÀ-Ỹ ]+|"
                     r"SỞ [A-ZĐÀ-Ỹ ]+|TỈNH ỦY[A-ZĐÀ-Ỹ ]*|BAN CHẤP HÀNH TRUNG ƯƠNG|BỘ CHÍNH TRỊ)\s*$", re.M)
NGUOI_KY = re.compile(r"^\s*(KT\.|TM\.|TL\.|TUQ\.)?\s*(THỦ TƯỚNG|PHÓ THỦ TƯỚNG|BỘ TRƯỞNG|THỨ TRƯỞNG|CHỦ TỊCH|PHÓ CHỦ TỊCH|GIÁM ĐỐC|PHÓ GIÁM ĐỐC|CHỦ TỊCH QUỐC HỘI)\s*$\s*\n(?:.*\n){0,4}?\s*([A-ZĐÀ-Ỹ][a-zđà-ỹ]+(?: [A-ZĐÀ-Ỹ][a-zđà-ỹ]+){1,4})\s*$", re.M)


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


def khong_dau(s: str) -> str:
    s = nfc(s).replace("Đ", "D").replace("đ", "d")
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn")


def slug(s: str, toi_da: int = 80) -> str:
    """Tên trích yếu ngắn không dấu: 'SỬA ĐỔI, BỔ SUNG MỘT SỐ ĐIỀU' → 'Sua-doi-bo-sung-mot-so-dieu'."""
    s = re.sub(r"[^A-Za-z0-9]+", "-", khong_dau(s)).strip("-")
    if len(s) > toi_da:
        s = s[:toi_da].rsplit("-", 1)[0]
    s = s.lower()
    return s[:1].upper() + s[1:]


def doc_thong_tin(text: str) -> dict:
    """Số, ngày, cơ quan, trích yếu, người ký từ bản trích chữ (chỉ phần đầu/cuối)."""
    head = text[:4000]
    tmp = Path(tempfile.mkdtemp()) / "x.txt"
    tmp.write_text(text, encoding="utf-8")
    so, ngay = so_cai.tu_text(tmp)
    shutil.rmtree(tmp.parent, ignore_errors=True)
    co_quan = ""
    m = CO_QUAN.search(head)
    if m:
        co_quan = " ".join(m.group(1).split())
    trich_yeu = ""
    m = TIEU_DE.search(head)
    if m:
        sau = head[m.end():].strip().split("\n")
        dong = [d.strip() for d in sau[:3] if d.strip()]
        if dong:
            trich_yeu = " ".join(dong[:2])[:160]
    nguoi_ky = ""
    m = NGUOI_KY.search(text[-6000:])
    if m:
        nguoi_ky = m.group(3)
    return {"so_hieu": so, "ngay": ngay, "co_quan": co_quan, "trich_yeu": trich_yeu, "nguoi_ky": nguoi_ky}


def doan_plugin(ten_tep: str, text: str) -> tuple[str, list[str]]:
    low = nfc(ten_tep + "\n" + text[:5000]).casefold()
    tieu_de = nfc(text[:600]).casefold()
    diem = []
    for plugin, tks in TU_KHOA:
        d = 0
        for tk, w in tks:
            n = low.count(tk)
            if n:
                d += w * min(n, 5) + (w * 3 if tk in tieu_de else 0)
        diem.append((d, plugin))
    diem.sort(key=lambda x: -x[0])
    giai_trinh = [f"{p}: {d}" for d, p in diem[:4] if d]
    if not diem or diem[0][0] == 0:
        return "", giai_trinh
    return diem[0][1], giai_trinh


def ten_chuan(info: dict, goc: Path) -> str | None:
    if not info["ngay"] or not info["so_hieu"]:
        return None
    d, mo, y = info["ngay"].split("/")
    so = khong_dau(info["so_hieu"]).replace("/", ".").replace("-", ".")
    so = re.sub(r"[^A-Za-z0-9.]", "", so)
    ten = slug(info["trich_yeu"] or goc.stem, 70) or slug(goc.stem, 70)
    return f"{y}.{mo}.{d}-{so}-{ten}{goc.suffix.lower()}"


def kich_thuoc_kho() -> int:
    """Kích thước kho git (pack đã nén, như 'kho khoảng 459 MB' Bạn nêu 09/10/2026) — đo bằng git count-objects."""
    out = subprocess.run(["git", "-C", str(REPO), "count-objects", "-v"], capture_output=True, text=True, check=True).stdout
    kb = 0
    for line in out.split("\n"):
        if line.startswith(("size-pack:", "size:")):
            kb += int(line.split(":")[1])
    return kb * 1024


def xu_ly(f: Path) -> dict:
    kq = {"tep_goc": f.name, "kich_thuoc_mb": round(os.stat(f).st_size / MB, 2), "canh_bao": []}
    try:
        text, cach = trich.trich_text(f)
    except Exception as e:  # noqa: BLE001
        kq["loi"] = f"không bóc được chữ: {e}"
        return kq
    ok, ly_do = trich.kiem_tra_chat_luong(text)
    kq["kiem_tra_txt"] = f"{cach}; {'ĐẠT' if ok else 'KHÔNG ĐẠT'} — {ly_do}"
    info = doc_thong_tin(text)
    kq.update(info)
    plugin, giai_trinh = doan_plugin(f.name, text)
    kq["giai_trinh_plugin"] = giai_trinh
    if plugin:
        dich_dir = REPO / plugin / "skills" / plugin / "van-ban-goc"
        kq["plugin_chu"] = plugin
    else:
        dich_dir = CHUA_PHAN_LOAI
        kq["plugin_chu"] = "(chưa phân loại) vbhc-vn/van-ban-goc/chua-phan-loai"
        kq["canh_bao"].append("Không đoán được plugin chủ — Bạn chuyển tệp sang plugin đúng lĩnh vực rồi chạy lại build_so_cai_van_ban_goc.py.")
    dich_dir.mkdir(parents=True, exist_ok=True)
    ten_moi = ten_chuan(info, f)
    if not ten_moi:
        ten_moi = f.name
        kq["canh_bao"].append("Không đọc được đủ số hiệu/ngày bằng script — giữ nguyên tên tệp gốc; Bạn đổi tên theo quy ước "
                              "YYYY.MM.DD-SỐ.KÝ.HIỆU-Tên sau khi đối chiếu.")
    dich = dich_dir / ten_moi
    if dich.exists():
        kq["canh_bao"].append(f"Đã có tệp cùng tên {dich.relative_to(REPO)} — tệp mới được lưu với hậu tố _nap-lai.")
        dich = dich.with_name(dich.stem + "_nap-lai" + dich.suffix)
    shutil.move(str(f), str(dich))
    kq["duong_dan"] = dich.relative_to(REPO).as_posix()
    txt = dich.with_suffix(".txt")
    if ok:
        txt.write_text(trich.header(dich, cach, text) + "\n" + text.strip() + "\n", encoding="utf-8")
        kq["txt"] = txt.relative_to(REPO).as_posix()
    else:
        kq["canh_bao"].append("Bản trích chữ KHÔNG đạt kiểm tra chất lượng nên chưa ghi .txt — CI sẽ đỏ cho tới khi có bản .txt đạt "
                              "(nguồn Word tốt hơn, hoặc OCR lại).")
    if os.stat(dich).st_size >= NGUONG_TEP:
        kq["canh_bao"].append(f"Tệp {kq['kich_thuoc_mb']} MB ≥ 3 MB: bản gốc bị export-ignore, KHÔNG vào gói claude.ai; "
                              "toàn văn vẫn tra được qua bản .txt.")
    # trùng số hiệu với văn bản đã có ở plugin khác
    if info["so_hieu"]:
        rows, _ = so_cai.quet()
        key = so_cai.chuan_hoa_so(info["so_hieu"])
        khac = sorted({r["plugin_chu"] for r in rows if so_cai.chuan_hoa_so(r["so_hieu"]) == key and r["duong_dan"] != kq["duong_dan"]})
        if khac:
            kq["canh_bao"].append(f"Số hiệu {info['so_hieu']} đã có ở plugin: {', '.join(khac)} — nguyên tắc một nguồn, Bạn chọn plugin chủ.")
    return kq


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ket-qua", required=True, help="thư mục ghi title.txt, body.md, commit.txt, ket-qua.json")
    a = ap.parse_args()
    out = Path(a.ket_qua)
    out.mkdir(parents=True, exist_ok=True)
    teps = sorted(f for f in INBOX.iterdir() if f.is_file() and f.suffix.lower() in trich.DUOI_GOC) if INBOX.is_dir() else []
    gh_out = os.environ.get("GITHUB_OUTPUT")
    if not teps:
        print("_inbox/ không có tệp .pdf/.doc/.docx/.xlsx nào.")
        if gh_out:
            Path(gh_out).open("a", encoding="utf-8").write("co_tep=false\n")
        return 0
    kqs = [xu_ly(f) for f in teps]
    subprocess.run([sys.executable, str(REPO / "scripts" / "build_so_cai_van_ban_goc.py")], check=False)
    subprocess.run([sys.executable, str(REPO / "scripts" / "export_ignore.py")], check=False)
    tong = kich_thuoc_kho()
    canh_bao_kho = f"Kho git (pack) {tong / MB:.0f} MB VƯỢT 480 MB — sắp chạm trần 512 MB của claude.ai; rà export-ignore (scripts/export_ignore.py)." if tong > TRAN_KHO else ""

    dau = kqs[0]
    tieu_de = "Nạp kho: " + " ; ".join(f"{k.get('so_hieu') or k['tep_goc']} {(k.get('trich_yeu') or '')[:60]}".strip() for k in kqs)[:200]
    L = ["Tệp Bạn đưa vào `_inbox/` đã được xử lý tự động bởi `scripts/nap_kho.py` (workflow nap-kho.yml). "
         "Số, ngày, cơ quan đọc bằng script từ bản trích chữ; đối chiếu lại trước khi dùng.", ""]
    for k in kqs:
        L.append(f"## {k['tep_goc']} ({k['kich_thuoc_mb']} MB)")
        if "loi" in k:
            L += [f"- LỖI: {k['loi']} — tệp vẫn nằm trong `_inbox/`.", ""]
            continue
        L += [f"- Số hiệu: **{k.get('so_hieu') or '(không đọc được)'}** — ngày ban hành: **{k.get('ngay') or '(không đọc được)'}**",
              f"- Cơ quan: {k.get('co_quan') or '(không đọc được)'}; người ký: {k.get('nguoi_ky') or '(không đọc được)'}",
              f"- Trích yếu (máy đọc): {k.get('trich_yeu') or '(không đọc được)'}",
              f"- Plugin chủ: **{k['plugin_chu']}** (điểm từ khóa: {', '.join(k['giai_trinh_plugin']) or 'không có'})",
              f"- Đã chuyển tới: `{k['duong_dan']}`" + (f" + bản trích chữ `{k['txt']}`" if k.get('txt') else ""),
              f"- Kiểm tra bản .txt: {k['kiem_tra_txt']}"]
        for c in k["canh_bao"]:
            L.append(f"- ⚠️ {c}")
        L.append("")
    if canh_bao_kho:
        L.append(f"⚠️ {canh_bao_kho}")
    L += ["", "Việc còn lại sau khi merge: cập nhật reference tóm tắt của plugin chủ, CHANGELOG, nâng version (phiên Claude làm theo "
          "mục 4.1 CLAUDE.md). Danh mục chung `DANH-MUC-VAN-BAN-GOC.csv` và `00-DANH-MUC-CHUNG.md` đã dựng lại trong PR này."]
    (out / "title.txt").write_text(tieu_de + "\n", encoding="utf-8")
    (out / "body.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    (out / "commit.txt").write_text(tieu_de + "\n\n" + "\n".join(f"- {k['tep_goc']} -> {k.get('duong_dan', '(lỗi)')}" for k in kqs) + "\n",
                                     encoding="utf-8")
    (out / "ket-qua.json").write_text(json.dumps(kqs, ensure_ascii=False, indent=2), encoding="utf-8")
    print((out / "body.md").read_text(encoding="utf-8"))
    if gh_out:
        Path(gh_out).open("a", encoding="utf-8").write("co_tep=true\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
