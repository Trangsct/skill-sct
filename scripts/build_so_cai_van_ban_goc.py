#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_so_cai_van_ban_goc.py — Sổ cái văn bản gốc DÙNG CHUNG cho mọi plugin (Bạn chốt 09/10/2026).

Vì sao: 24 plugin có 18 thư mục van-ban-goc/ với hàng trăm tệp, nhưng không có danh mục chung; mỗi
phiên chỉ tìm trong plugin đang mở rồi kết luận "chưa có" (vụ QCVN 01:2019/BCT ngày 09/10/2026 — tệp
nằm ở kho-vlncn-sct-vn, phiên mở sd-vlncn-sct-vn không thấy). Gói plugin đồng bộ về claude.ai KHÔNG
gồm CLAUDE.md và scripts/ ở gốc kho, nên danh mục và công cụ tìm phải nằm BÊN TRONG từng plugin.

Script này (chạy tại gốc kho, KHÔNG sửa tay sản phẩm của nó):
  1. Quét */skills/*/van-ban-goc/ (mọi tệp gốc .pdf .doc .docx .xlsx; bản .txt/.md độc lập) và
     */skills/*/vi-du-thuc-te/ (chỉ văn bản có số hiệu dạng văn bản quy phạm / chỉ đạo; bỏ ảnh, dự thảo).
  2. Đọc số hiệu, ngày ban hành, tên từ tên tệp theo quy ước  YYYY.MM.DD-SỐ.KÝ.HIỆU-Tên  (ví dụ
     2026.08.17-2867.QD.UBND-Uy-quyen-GD-SCT-linh-vuc-VLNCN). Tên chưa chuẩn thì đọc "Số:" và "ngày …
     tháng … năm …" trong 3.000 ký tự đầu của bản .txt (chỉ nhận khi đứng trước "Căn cứ"), thiếu thì đoán
     từ tên tệp, và ghi cờ "tên chưa chuẩn" ở cột ghi_chu.
  3. Ghi  DANH-MUC-VAN-BAN-GOC.csv  ở gốc kho (sắp theo ngày ban hành giảm dần), cột:
     so_hieu, ngay_ban_hanh, ten, plugin_chu, duong_dan, dinh_dang, co_txt, kich_thuoc_kb, ngay_nap, ghi_chu.
  4. Ghi  van-ban-goc/00-DANH-MUC-CHUNG.md  (bản rút gọn cho người và cho Claude) vào TỪNG plugin —
     nội dung giống nhau — và chép  scripts/tim_van_ban.py  vào  skills/<plugin>/scripts/  của từng plugin.
  5. Phát hiện cùng một số hiệu nằm ở nhiều plugin (nguyên tắc một nguồn: mỗi văn bản chỉ một plugin chủ)
     — đợt đầu chỉ cảnh báo và liệt kê ở cuối 00-DANH-MUC-CHUNG.md, chưa xóa; Bạn quyết plugin chủ.

Dùng:
  python3 scripts/build_so_cai_van_ban_goc.py            # dựng lại toàn bộ
  python3 scripts/build_so_cai_van_ban_goc.py --check    # CI: sản phẩm lệch với kho, hoặc còn câu "chưa có trong
                                                         # gói"/"tra mạng khi cần nguyên văn" trong tài liệu plugin -> exit 1
"""
from __future__ import annotations

import argparse
import csv
import io
import os
import re
import subprocess
import sys
import unicodedata
from collections import defaultdict
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CSV_PATH = REPO / "DANH-MUC-VAN-BAN-GOC.csv"
MD_NAME = "00-DANH-MUC-CHUNG.md"
TIM_SCRIPT = REPO / "scripts" / "tim_van_ban.py"
COLS = ["so_hieu", "ngay_ban_hanh", "ten", "plugin_chu", "duong_dan", "dinh_dang", "co_txt",
        "kich_thuoc_kb", "ngay_nap", "ghi_chu"]

DUOI_GOC = (".pdf", ".doc", ".docx", ".xlsx")
DUOI_CHU = (".txt", ".md")
UU_TIEN = {".docx": 0, ".doc": 1, ".pdf": 2, ".xlsx": 3, ".txt": 4, ".md": 5}
BO_QUA_TEN = {"INDEX.md", "00-MUC-LUC.md", "README.md", "README-BAI-HOC.md", MD_NAME, "line_runs.txt"}
HAU_TO_TRICH = ("-TEXT", "-OCR", "_ban-trich-chu", " (bản text trích được)", "-text")

# Câu đầu tệp danh mục — Bạn chốt nguyên văn 09/10/2026
CAU_DAU = ("Danh mục toàn bộ văn bản gốc trong mọi plugin của kho skill-sct. Trước khi kết luận văn bản nào "
           "chưa có, phải tra tệp này và chạy scripts/tim_van_ban.py")

# Cụm bị cấm trong tài liệu plugin khi văn bản đã có trong danh mục (mục 3.3 bản giao việc 09/10/2026)
CUM_CAM = re.compile(r"(chưa có trong gói|không có trong gói|tra mạng[^\n]{0,40}nguyên văn|"
                     r"hỏi Bạn khi cần nguyên văn|không mở được toàn văn|không có tài liệu tham chiếu)", re.I)
DONG_CHO_PHEP = re.compile(r"(cấm|CẤM|lịch sử|check_facts|build_so_cai|không được nói|không được trả lời|vụ 09/10/2026)")

LOAI_VB = {"nd": "NĐ", "tt": "TT", "ttlt": "TTLT", "luat": "Luật", "nq": "NQ", "qd": "QĐ", "cv": "CV", "kh": "KH",
           "tb": "TB", "ct": "CT", "ctr": "CTr", "kl": "KL", "bc": "BC", "bb": "BB", "gcn": "GCN", "gp": "GP",
           "qcvn": "QCVN", "tcvn": "TCVN", "dlvn": "ĐLVN", "vbhn": "VBHN", "pl": "PL", "hd": "HD", "cthd": "CTHĐ",
           "gxn": "GXN", "bdk": "BĐK", "sl": "SL", "ttr": "TTr"}
MA_KY_HIEU = {"QD": "QĐ", "ND": "NĐ", "HDND": "HĐND", "NDCP": "NĐ-CP", "QDUBND": "QĐ-UBND", "DU": "ĐU",
              "DCKS": "ĐCKS", "QLDD": "QLĐĐ", "BDKH": "BĐKH", "DKT": "ĐKT", "DDT": "ĐĐT", "ATD": "ATĐ"}
DANG = {"TW", "TU", "ĐU", "DU"}
CHUAN = re.compile(r"^(\d{4})\.(\d{2})\.(\d{2})[-_. ]+([0-9][0-9A-Za-zĐđ.]*)[-_ ]+(.+)$")
NGAY_TRONG_TEN = re.compile(r"(?<!\d)(\d{1,2})[-_.](\d{1,2})[-_.](\d{4})(?!\d)")
NGAY_ISO_TRONG_TEN = re.compile(r"(?<!\d)(\d{4})-(\d{2})-(\d{2})(?!\d)")
NGAY_ISO_CHAM = re.compile(r"(?<!\d)(\d{4})\.(\d{2})\.(\d{2})(?!\d)")
MA_CODE = re.compile(r"^[A-ZĐ]{1,7}[a-z]{0,2}\d{0,2}$")
VI_DU_HOP_LE = re.compile(r"^(?:\d{4}[.\-]\d{2}[.\-]\d{2}[. _-]*)?(ND|TT|Luat|NQ|QD|CV|KH|TB|CT|CTr|KL|GXN|BDK|QCVN|VBHN)[-_ ]\d", re.I)
VI_DU_LOAI = re.compile(r"(du-thao|Du-thao|Dự thảo|du_thao|mau|Mau-|MAU|-chinh-sua|ban-chot|ban-trinh|khung-)", re.I)


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


# ----------------------------------------------------------------------------- đọc tên tệp
def _ky_hieu_tu_codes(codes: list[str]) -> list[str]:
    out = []
    for c in codes:
        c2 = MA_KY_HIEU.get(c.upper(), c)
        out.extend(c2.split("-"))
    return out


def tu_ten_chuan(stem: str):
    """Tên theo quy ước YYYY.MM.DD-SỐ.KÝ.HIỆU-Tên → (so_hieu, ngay dd/mm/yyyy, ten) hoặc None."""
    m = CHUAN.match(stem)
    if not m:
        return None
    y, mo, d, token, ten = m.groups()
    parts = [p for p in token.split(".") if p]
    nums = [p for p in parts if re.fullmatch(r"\d+", p)]
    codes = [p for p in parts if not re.fullmatch(r"\d+", p)]
    if not nums:
        return None
    if len(nums) >= 2 and re.fullmatch(r"(19|20)\d{2}", nums[-1]):
        so = (".".join(nums[:-1]) if len(nums) > 2 else nums[0]) + "/" + nums[-1]
    else:
        so = ".".join(nums)
    kh = "-".join(_ky_hieu_tu_codes(codes))
    so_hieu = f"{so}/{kh}" if kh else so
    ten = re.sub(r"[-_]+", " ", ten).strip()
    return so_hieu, f"{d}/{mo}/{y}", ten


ORG = {"CP", "TTg", "BCT", "BCA", "BQP", "BXD", "BTC", "BNNMT", "BTNMT", "BNN", "BKHCN", "BYT", "BGTVT", "BLĐTBXH", "BNV",
       "UBND", "HĐND", "VPCP", "VPUBND", "VPQH", "SCT", "SNNMT", "SXD", "STC", "SYT", "TU", "TW", "ĐU", "BQL", "BQLCKCN", "HĐTV",
       "VNX", "VSDC", "TTCP", "ATMT", "ATKV", "ATĐ", "ĐCKS", "PCKS", "KS", "KT", "XD", "NC", "TH", "NLN", "CST", "CCMT", "QLĐĐ",
       "QLCS", "QHQT", "NN", "BĐKH", "TCCB", "KHCN", "VP", "CN", "ĐKT", "ĐĐT", "VS", "DK", "PLNC", "XPVPHC", "QLHC", "HC",
       "SY", "TT", "CucHoaChat", "DTT72", "SD1", "CWC"}
ORG_KHONG = {"CWC", "CucHoaChat"}   # có trong tên nhưng không phải ký hiệu cơ quan
ORG -= ORG_KHONG
LUAT_TRONG_TEN = re.compile(r"(?<![\d.])(\d{1,4}(?:\.\d{1,2})?)[-_ ](\d{4})[-_ ](QH\d{2}|N[DĐ]-?CP|TT-[A-ZĐ]{2,7}|Q[DĐ]-[A-ZĐ]{2,7}|NQ-[A-ZĐ]{2,7})")


def _la_code(tok: str, loai: str, da_co: list[str]) -> bool:
    if tok in da_co:
        return False
    if tok.upper() in MA_KY_HIEU:
        return True
    if re.fullmatch(r"QH\d{2}", tok):
        return True
    if tok in ORG or tok == loai or (loai == "QĐ" and tok == "QD") or (loai == "NĐ" and tok == "ND") or (loai == "CTr" and tok == "CTr"):
        return True
    return False


def tu_ten_long(stem: str):
    """Tên chưa chuẩn (ND-181-2024, QD-2867-QD-UBND, CV-7103-UBND-TH-10-7-2026…) → (so_hieu|'', ngay|'', ten)."""
    s = stem
    ngay = ""
    for rx, thu_tu in ((NGAY_TRONG_TEN, "dmy"), (NGAY_ISO_TRONG_TEN, "ymd"), (NGAY_ISO_CHAM, "ymd")):
        m = rx.search(s)
        if m:
            a, b, c = m.groups()
            d, mo, y = (a, b, c) if thu_tu == "dmy" else (c, b, a)
            if 1 <= int(d) <= 31 and 1 <= int(mo) <= 12:
                ngay = f"{int(d):02d}/{int(mo):02d}/{y}"
                s = s[:m.start()] + " " + s[m.end():]
                break
    tokens = [t for t in re.split(r"[-_ ]+", s) if t]
    ten_mac_dinh = re.sub(r"[-_]+", " ", stem).strip()
    if not tokens:
        return "", ngay, ten_mac_dinh
    loai = LOAI_VB.get(tokens[0].lower())
    if not loai:
        m = LUAT_TRONG_TEN.search(s)
        if m:
            num, year, kh = m.groups()
            kh = kh.replace("ND", "NĐ").replace("QD", "QĐ")
            kh = "NĐ-CP" if kh in ("NĐ-CP", "NĐCP") else kh
            return f"{num}/{year}/{kh}", ngay, ten_mac_dinh
        if re.fullmatch(r"\d{1,5}", tokens[0]) and len(tokens) > 1 and re.fullmatch(r"[A-ZĐ]{2,7}", tokens[1]):
            codes = [t for t in tokens[1:3] if re.fullmatch(r"[A-ZĐ]{2,7}", t)]
            return f"{tokens[0]}/{'-'.join(codes)}", ngay, " ".join(tokens[1 + len(codes):])
        return "", ngay, ten_mac_dinh
    i = 1
    num = ""
    if i < len(tokens) and re.fullmatch(r"\d+[A-Z]?(\.\d+)?", tokens[i]):
        num = tokens[i]
        i += 1
        # NQ-66-18-2026 → 66.18/2026
        if i + 1 < len(tokens) and re.fullmatch(r"\d{1,2}", tokens[i]) and re.fullmatch(r"(19|20)\d{2}", tokens[i + 1]):
            num = f"{num}.{tokens[i]}"
            i += 1
    year = ""
    if i < len(tokens) and re.fullmatch(r"(19|20)\d{2}", tokens[i]):
        year = tokens[i]
        i += 1
    codes: list[str] = []
    while i < len(tokens) and len(codes) < 3 and _la_code(tokens[i], loai, codes):
        codes.append(tokens[i])
        i += 1
    ten = " ".join(tokens[i:]).strip()
    if not num:
        m = LUAT_TRONG_TEN.search(s)
        if m:
            n2, y2, kh = m.groups()
            kh = "NĐ-CP" if kh.upper().replace("-", "") == "NDCP" else kh.replace("QD", "QĐ")
            return f"{n2}/{y2}/{kh}", ngay, ten_mac_dinh
        return "", ngay, ten_mac_dinh
    kh = _ky_hieu_tu_codes(codes)
    if loai in ("QCVN", "TCVN", "ĐLVN"):
        so_hieu = f"{loai} {num}:{year}" + (f"/{'-'.join(kh)}" if kh else "")
    elif kh and re.fullmatch(r"QH\d{2}", kh[-1]):
        so_hieu = f"{num}/{year}/{kh[-1]}" if year else f"{num}/{kh[-1]}"
    elif loai == "Luật":
        so_hieu = f"Luật {num}/{year}" if year else f"Luật {num}"
    elif kh and kh[-1] in DANG:
        so_hieu = f"{num}-{loai}/{kh[-1]}"
    elif kh:
        kyhieu = "-".join(kh) if (kh[0] == loai or loai == "CV") else f"{loai}-" + "-".join(kh)
        so_hieu = f"{num}/{year}/{kyhieu}" if year else f"{num}/{kyhieu}"
    elif loai == "NĐ":
        so_hieu = f"{num}/{year}/NĐ-CP" if year else f"NĐ {num}"
    elif loai == "NQ" and year:
        so_hieu = f"{num}/{year}/NQ-CP"
    elif year:
        so_hieu = f"{loai} {num}/{year}"
    else:
        so_hieu = f"{loai} {num}"
    return so_hieu, ngay, ten


SO_TRONG_TEXT = re.compile(r"(?:^|\s)Số:\s*([0-9][0-9A-Za-zĐđ.]*/[0-9A-Za-zĐđ./\-]*[A-Za-zĐđ0-9])", re.I)
NGAY_TRONG_TEXT = re.compile(r"ngày\s+(\d{1,2})\s+tháng\s+(\d{1,2})\s+năm\s+(\d{4})", re.I)


def tu_text(txt: Path):
    """Đọc 'Số:' và 'ngày … tháng … năm …' ở phần đầu bản .txt, chỉ nhận khi đứng trước 'Căn cứ'."""
    try:
        head = nfc(txt.read_text(encoding="utf-8", errors="replace")[:3500])
    except OSError:
        return "", ""
    if head.startswith("["):
        head = head.split("\n", 1)[1] if "\n" in head else head
    head = head[:3000]
    cc = head.find("Căn cứ")
    vung = head[:cc] if cc > 0 else head[:1500]
    so, ngay = "", ""
    m = SO_TRONG_TEXT.search(vung)
    if m:
        so = m.group(1).strip().rstrip(".,;")
    m = NGAY_TRONG_TEXT.search(vung)
    if m:
        d, mo, y = m.groups()
        if 1 <= int(d) <= 31 and 1 <= int(mo) <= 12:
            ngay = f"{int(d):02d}/{int(mo):02d}/{y}"
    return so, ngay


# ----------------------------------------------------------------------------- quét kho
def plugins() -> list[str]:
    return sorted(p.parent.parent.name for p in REPO.glob("*/.claude-plugin/plugin.json"))


def ngay_nap_map() -> dict[str, str]:
    """Ngày tệp được thêm vào kho lần đầu (git log --diff-filter=A); kho nông thì thiếu, lấy từ CSV cũ."""
    out: dict[str, str] = {}
    try:
        r = subprocess.run(["git", "-C", str(REPO), "log", "--diff-filter=A", "--format=%x00%as", "--name-only", "-z"],
                           capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return out
    cur = ""
    for tok in r.stdout.decode("utf-8", "replace").split("\0"):
        tok = tok.strip("\n")
        if not tok:
            continue
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", tok):
            cur = tok
        else:
            for p in tok.split("\n"):
                if p:
                    out[p] = cur  # log mới -> cũ, giá trị cuối là lần thêm sớm nhất
    return out


def csv_cu() -> dict[str, dict]:
    if not CSV_PATH.exists():
        return {}
    with CSV_PATH.open(encoding="utf-8", newline="") as f:
        return {r["duong_dan"]: r for r in csv.DictReader(f)}


def la_ban_trich(f: Path, goc_stems: set[str]) -> bool:
    """txt/md là bản trích của một tệp gốc cùng thư mục (cùng tên, hoặc tên bỏ hậu tố -TEXT/-OCR là tiền tố của tệp gốc)."""
    stem = f.stem
    if stem in goc_stems:
        return True
    for ht in HAU_TO_TRICH:
        if stem.endswith(ht):
            core = stem[: -len(ht)]
            if any(g == core or g.startswith(core) for g in goc_stems):
                return True
    return False


def quet() -> tuple[list[dict], list[str]]:
    rows, canh_bao = [], []
    nap = ngay_nap_map()
    cu = csv_cu()
    hom_nay = date.today().isoformat()
    for plugin in plugins():
        skill = REPO / plugin / "skills" / plugin
        for nguon in ("van-ban-goc", "vi-du-thuc-te"):
            root = skill / nguon
            if not root.is_dir():
                continue
            theo_thu_muc: dict[Path, list[Path]] = defaultdict(list)
            for f in sorted(root.rglob("*")):
                if f.is_file() and f.name not in BO_QUA_TEN and not f.name.startswith("."):
                    theo_thu_muc[f.parent].append(f)
            for d, files in theo_thu_muc.items():
                goc = [f for f in files if f.suffix.lower() in DUOI_GOC]
                goc_stems = {f.stem for f in goc}
                chu = [f for f in files if f.suffix.lower() in DUOI_CHU and not la_ban_trich(f, goc_stems)]
                nhom: dict[str, list[Path]] = defaultdict(list)
                for f in goc + chu:
                    if nguon == "vi-du-thuc-te" and not (VI_DU_HOP_LE.match(f.name) and not VI_DU_LOAI.search(f.name)):
                        continue
                    nhom[f.stem].append(f)
                for stem, fs in nhom.items():
                    fs.sort(key=lambda p: UU_TIEN[p.suffix.lower()])
                    chinh = fs[0]
                    txt = chinh.with_suffix(".txt")
                    co_txt = txt.exists() or chinh.suffix.lower() in DUOI_CHU
                    rel = chinh.relative_to(REPO).as_posix()
                    ghi_chu = []
                    chuan = tu_ten_chuan(stem)
                    if chuan:
                        so_hieu, ngay, ten = chuan
                    else:
                        so_l, ngay_l, ten = tu_ten_long(stem)
                        so_t, ngay_t = tu_text(txt if txt.exists() else chinh) if co_txt else ("", "")
                        so_hieu = so_t or so_l
                        ngay = ngay_l or ngay_t   # ngày ghi trong tên tệp tin cậy hơn dòng đầu bản trích
                        ghi_chu.append("tên chưa chuẩn")
                        if not so_hieu:
                            ghi_chu.append("không đọc được số hiệu")
                    if nguon == "vi-du-thuc-te":
                        ghi_chu.append("vi-du-thuc-te")
                    if txt.exists():
                        try:
                            if txt.read_text(encoding="utf-8", errors="replace")[:6].startswith("[OCR]"):
                                ghi_chu.append("ocr")
                        except OSError:
                            pass
                    kb = sum(os.stat(f).st_size for f in fs) // 1024
                    if any(os.stat(f).st_size >= 3 * 1024 * 1024 for f in fs):
                        ghi_chu.append("bản gốc ≥ 3 MB chỉ có trên GitHub")
                    rows.append({
                        "so_hieu": nfc(so_hieu), "ngay_ban_hanh": ngay, "ten": nfc(ten), "plugin_chu": plugin,
                        "duong_dan": rel, "dinh_dang": "+".join(p.suffix.lower().lstrip(".") for p in fs),
                        "co_txt": "co" if co_txt else "khong", "kich_thuoc_kb": str(kb),
                        "ngay_nap": cu.get(rel, {}).get("ngay_nap") or nap.get(rel) or hom_nay,
                        "ghi_chu": "; ".join(ghi_chu),
                    })

    def key_sap(r):
        m = re.fullmatch(r"(\d{2})/(\d{2})/(\d{4})", r["ngay_ban_hanh"] or "")
        if m:
            return (0, -int(m.group(3) + m.group(2) + m.group(1)), r["plugin_chu"], r["duong_dan"])
        return (1, 0, r["plugin_chu"], r["duong_dan"])  # không rõ ngày xếp cuối

    rows.sort(key=key_sap)
    # Trùng số hiệu ở nhiều plugin
    theo_so: dict[str, set[str]] = defaultdict(set)
    for r in rows:
        if r["so_hieu"] and "vi-du-thuc-te" not in r["ghi_chu"]:
            theo_so[chuan_hoa_so(r["so_hieu"])].add(r["plugin_chu"])
    for so, ps in sorted(theo_so.items()):
        if len(ps) > 1:
            vd = next(r for r in rows if chuan_hoa_so(r["so_hieu"]) == so)
            canh_bao.append(f"{vd['so_hieu']} — {', '.join(sorted(ps))}")
    return rows, canh_bao


def chuan_hoa_so(s: str) -> str:
    s = nfc(s).upper().replace("Đ", "D").replace(" ", "")
    return s


# ----------------------------------------------------------------------------- sản phẩm
def csv_text(rows: list[dict]) -> str:
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=COLS, lineterminator="\n")
    w.writeheader()
    for r in rows:
        w.writerow(r)
    return buf.getvalue()


def md_text(rows: list[dict], canh_bao: list[str]) -> str:
    goc = [r for r in rows if "vi-du-thuc-te" not in r["ghi_chu"]]
    vd = [r for r in rows if "vi-du-thuc-te" in r["ghi_chu"]]
    co_txt = sum(1 for r in goc if r["co_txt"] == "co")
    L = [f"# Danh mục chung văn bản gốc — toàn bộ kho skill-sct",
         "",
         f"**{CAU_DAU}** (ví dụ `python3 scripts/tim_van_ban.py \"QCVN 01:2019\"`).",
         "",
         "- Tệp này do `scripts/build_so_cai_van_ban_goc.py` sinh ra, giống nhau ở mọi plugin — **không sửa tay**; "
         "sửa thì chạy lại script tại gốc kho.",
         "- Đường dẫn ghi theo gốc kho `<plugin>/skills/<plugin>/van-ban-goc/…`. Trên claude.ai gói plugin nằm tại "
         "`/mnt/skills/plugins/<plugin>:<plugin>/van-ban-goc/…` (thay phần `<plugin>/skills/<plugin>/`).",
         "- Mỗi tệp gốc có bản trích chữ **cùng tên, đuôi `.txt`** đặt cạnh (cột *.txt*). Bản gốc ≥ 3 MB bị "
         "export-ignore, không vào gói claude.ai — khi đó **mở bản `.txt`**, không được trả lời \"không mở được toàn văn\".",
         "- Văn bản đã có ở đây thì **phải mở toàn văn để trích**; chỉ khi tra danh mục và chạy `tim_van_ban.py` "
         "đều không thấy mới được nói \"chưa có bản gốc trong kho\" và hướng dẫn Bạn nạp qua Hộp thư `_inbox/` trên GitHub.",
         "",
         f"Thống kê: {len(goc)} văn bản gốc ({co_txt} có bản .txt) ở {len({r['plugin_chu'] for r in goc})} plugin; "
         f"{len(vd)} văn bản có số hiệu trong `vi-du-thuc-te/`. Sắp theo ngày ban hành giảm dần; không rõ ngày xếp cuối.",
         "",
         "## Văn bản gốc (van-ban-goc/)",
         "",
         "| Số hiệu | Ngày | Tên | Plugin chủ | Đường dẫn | .txt |",
         "|---|---|---|---|---|---|"]
    for r in goc:
        L.append(f"| {r['so_hieu'] or '—'} | {r['ngay_ban_hanh'] or '—'} | {_md(r['ten'])} | {r['plugin_chu']} | "
                 f"`{_md(r['duong_dan'])}` | {'có' if r['co_txt'] == 'co' else 'KHÔNG'}"
                 f"{' (OCR)' if 'ocr' in r['ghi_chu'] else ''} |")
    L += ["", "## Văn bản có số hiệu trong vi-du-thuc-te/ (văn bản đi, đến đã dùng làm ví dụ)", "",
          "| Số hiệu | Ngày | Tên | Plugin | Đường dẫn |", "|---|---|---|---|---|"]
    for r in vd:
        L.append(f"| {r['so_hieu'] or '—'} | {r['ngay_ban_hanh'] or '—'} | {_md(r['ten'])} | {r['plugin_chu']} | `{_md(r['duong_dan'])}` |")
    L += ["", "## Cùng số hiệu ở nhiều plugin (chờ Bạn chốt plugin chủ; chưa xóa)", ""]
    if canh_bao:
        L += [f"- {c}" for c in canh_bao]
    else:
        L.append("- (không có)")
    chua_chuan = [r for r in goc if "tên chưa chuẩn" in r["ghi_chu"]]
    L += ["", f"## Tệp đặt tên chưa theo quy ước YYYY.MM.DD-SỐ.KÝ.HIỆU-Tên: {len(chua_chuan)}", "",
          "Số hiệu, ngày của các tệp này đọc từ phần đầu bản .txt hoặc đoán từ tên tệp — đối chiếu bản gốc trước khi trích dẫn số/ngày.", ""]
    return "\n".join(L) + "\n"


def _md(s: str) -> str:
    return s.replace("|", "\\|")


def san_pham(rows, canh_bao) -> dict[Path, str]:
    out = {CSV_PATH: csv_text(rows)}
    md = md_text(rows, canh_bao)
    tim = TIM_SCRIPT.read_text(encoding="utf-8")
    for p in plugins():
        skill = REPO / p / "skills" / p
        out[skill / "van-ban-goc" / MD_NAME] = md
        out[skill / "scripts" / "tim_van_ban.py"] = tim
    return out


def kiem_cum_cam() -> list[str]:
    """Tài liệu plugin (.md) còn câu 'chưa có trong gói', 'tra mạng khi cần nguyên văn'… → liệt kê."""
    loi = []
    for p in plugins():
        skill = REPO / p / "skills" / p
        for f in sorted(skill.rglob("*.md")):
            if f.name.startswith("CHANGELOG") or f.name == MD_NAME:
                continue
            for n, line in enumerate(f.read_text(encoding="utf-8", errors="replace").split("\n"), 1):
                line = nfc(line)
                if CUM_CAM.search(line) and not DONG_CHO_PHEP.search(line):
                    loi.append(f"{f.relative_to(REPO)}:{n}: «{CUM_CAM.search(line).group(0)}»")
    return loi


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    rows, canh_bao = quet()
    sp = san_pham(rows, canh_bao)
    goc = [r for r in rows if "vi-du-thuc-te" not in r["ghi_chu"]]
    print(f"Văn bản gốc: {len(goc)} ({sum(1 for r in goc if r['co_txt'] == 'co')} có .txt); "
          f"vi-du-thuc-te có số hiệu: {len(rows) - len(goc)}; trùng số hiệu nhiều plugin: {len(canh_bao)}; "
          f"tên chưa chuẩn: {sum(1 for r in goc if 'tên chưa chuẩn' in r['ghi_chu'])}")
    for c in canh_bao:
        print(f"  TRÙNG: {c}")
    cam = kiem_cum_cam()
    if a.check:
        lech = [p for p, text in sp.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
        for p in lech:
            print(f"LỆCH: {p.relative_to(REPO)} — chạy python3 scripts/build_so_cai_van_ban_goc.py rồi commit")
        for c in cam:
            print(f"CỤM CẤM: {c}")
        if lech or cam:
            return 1
        print("Sổ cái văn bản gốc khớp với kho; không còn câu 'chưa có trong gói'.")
        return 0
    for p, text in sp.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        if not p.exists() or p.read_text(encoding="utf-8") != text:
            p.write_text(text, encoding="utf-8")
            print(f"→ {p.relative_to(REPO)}")
    for c in cam:
        print(f"CỤM CẤM (sửa tay): {c}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
