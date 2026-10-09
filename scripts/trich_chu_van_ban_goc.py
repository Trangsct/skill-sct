#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""trich_chu_van_ban_goc.py — bản trích chữ toàn văn (.txt) cho MỌI tệp gốc trong van-ban-goc/.

Vì sao (Bạn chốt 08/10/2026, mở rộng 09/10/2026): tệp ≥ 3 MB bị export-ignore nên không vào gói
claude.ai; PDF quét không có lớp chữ; .doc/.docx không grep được. Không có bản trích chữ thì Claude
trên claude.ai không nắm được nội dung (vụ QCVN 01:2019/BCT ngày 09/10/2026: tệp .doc 109 trang có
trong kho nhưng phiên trả lời "không mở được toàn văn"). Bản .txt nhỏ, luôn nằm trong gói, là thứ
Claude đọc; bản gốc chỉ để đối chiếu trên GitHub.

Quy tắc: mỗi tệp .pdf / .doc / .docx / .xlsx trong */skills/*/van-ban-goc/ phải có tệp .txt CÙNG TÊN
GỐC đặt cạnh (X.docx -> X.txt). Cùng tên gốc mà có nhiều định dạng (X.docx + X.pdf) thì một .txt là đủ,
lấy từ nguồn tốt nhất: docx > doc > pdf có lớp chữ > xlsx > pdf quét (OCR).

Cách trích:
  - .docx : bóc chữ từ word/document.xml (giữ ngắt đoạn; ô bảng ngăn bằng " | ").
  - .doc  : soffice --headless --convert-to docx vào thư mục tạm rồi bóc như .docx.
            KHÔNG dùng soffice --convert-to txt vì hỏng mã tiếng Việt (ra dấu "?").
  - .xlsx : openpyxl, mỗi sheet một khối, ô ngăn bằng " | ".
  - .pdf  : pdftotext -layout; dưới 200 ký tự/trang coi là bản quét -> pdftoppm 200 dpi + tesseract -l vie,
            đầu tệp ghi "[OCR]".
  Mọi bản trích chuẩn hóa Unicode NFC, ghi UTF-8.

Kiểm tra chất lượng (mục 2.2 bản giao việc 09/10/2026) — không đạt thì KHÔNG ghi tệp, báo lỗi:
  - tỷ lệ ký tự "?" trên tổng ký tự chữ dưới 0,5 %;
  - có ít nhất một trong các cụm: "CỘNG HÒA XÃ HỘI CHỦ NGHĨA", "Điều 1", "Căn cứ" (so không phân biệt
    hoa thường, chấp nhận "CỘNG HOÀ"; văn bản của Đảng: "ĐẢNG CỘNG SẢN VIỆT NAM"); phụ lục, biểu mẫu,
    danh mục, phiếu sao y, ghi chú nghiệp vụ không có ba cụm đó thì chấp nhận thêm "Phụ lục", "Mẫu số",
    "Kính gửi", "Danh mục", "Sao y", "Quy trình", "Nghị định số", "Thông tư số", "UN number", "Điều n" (CUM_PHU);
  - ít nhất 200 ký tự.

Dùng:
  python3 scripts/trich_chu_van_ban_goc.py            # sinh .txt cho mọi tệp còn thiếu
  python3 scripts/trich_chu_van_ban_goc.py --check    # chỉ liệt kê tệp thiếu .txt hoặc .txt không đạt (exit 1)
  python3 scripts/trich_chu_van_ban_goc.py --chi <tệp> [--ghi-de]   # xử lý một tệp
  python3 scripts/trich_chu_van_ban_goc.py --kiem <tệp.txt>         # chỉ chấm chất lượng một bản .txt

check_descriptions.py gọi --check nên CI đỏ khi còn tệp gốc thiếu bản trích chữ hoặc bản trích không đạt.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from xml.etree import ElementTree as ET

REPO = Path(__file__).resolve().parent.parent
DUOI_GOC = (".pdf", ".doc", ".docx", ".xlsx")
UU_TIEN = {".docx": 0, ".doc": 1, ".pdf": 2, ".xlsx": 3}
NGUONG_CHU_MOI_TRANG = 200          # dưới mức này coi PDF là bản quét
TY_LE_HOI_TOI_DA = 0.005            # 0,5 % ký tự "?" trên ký tự chữ
CUM_CHINH = ("cộng hòa xã hội chủ nghĩa", "cộng hoà xã hội chủ nghĩa", "điều 1", "căn cứ",
             "đảng cộng sản việt nam")   # văn bản của Đảng (NQ-TW, KL-TW, CTr-TU) không có Quốc hiệu, "Căn cứ"
# Phụ lục, biểu mẫu, danh mục, phiếu sao y, ghi chú nghiệp vụ, bảng tra (UN numbers): không có ba cụm trên
CUM_PHU = ("phụ lục", "mẫu số", "kính gửi", "danh mục", "sao y", "quy trình", "nghị định số", "thông tư số", "un number")
CUM_PHU_RX = re.compile(r"điều \d+")
DO_DAI_TOI_THIEU = 200

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


# ----------------------------------------------------------------------------- bóc chữ
def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


def _doan(p) -> str:
    out = []
    for el in p.iter():
        if el.tag == W + "t":
            out.append(el.text or "")
        elif el.tag == W + "tab":
            out.append("\t")
        elif el.tag in (W + "br", W + "cr"):
            out.append("\n")
    return "".join(out)


def _khoi(el, out: list):
    """Duyệt theo thứ tự tài liệu: đoạn -> dòng; bảng -> hàng ô ngăn ' | '."""
    for child in list(el):
        tag = child.tag
        if tag == W + "p":
            out.append(_doan(child))
        elif tag == W + "tbl":
            out.append("")
            for tr in child.findall(W + "tr"):   # chỉ hàng trực tiếp; bảng lồng xử lý khi đệ quy vào ô
                cells = []
                for tc in tr.findall(W + "tc"):
                    sub: list = []
                    _khoi(tc, sub)
                    cells.append(" ".join(s.strip() for s in sub if s.strip()))
                out.append(" | ".join(cells))
            out.append("")
        elif tag == W + "sectPr":
            continue
        else:
            _khoi(child, out)


def trich_docx(f: Path) -> str:
    with zipfile.ZipFile(f) as z:
        xml = z.read("word/document.xml")
    root = ET.fromstring(xml)
    body = root.find(W + "body")
    out: list = []
    _khoi(body if body is not None else root, out)
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return nfc(text)


def doc_sang_docx(f: Path, thu_muc_tam: Path) -> Path:
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        raise RuntimeError("không có soffice/libreoffice để chuyển .doc -> .docx")
    profile = thu_muc_tam / "lo-profile"
    subprocess.run([soffice, f"-env:UserInstallation=file://{profile}", "--headless", "--convert-to", "docx",
                    "--outdir", str(thu_muc_tam), str(f)], check=True, capture_output=True, timeout=600)
    out = thu_muc_tam / (f.stem + ".docx")
    if not out.exists():
        raise RuntimeError(f"soffice không tạo được {out.name}")
    return out


def trich_doc(f: Path) -> str:
    with tempfile.TemporaryDirectory() as d:
        return trich_docx(doc_sang_docx(f, Path(d)))


def trich_xlsx(f: Path) -> str:
    import openpyxl  # có sẵn trong môi trường; CI cài qua pip
    wb = openpyxl.load_workbook(f, read_only=True, data_only=True)
    out = []
    for ws in wb.worksheets:
        out.append(f"=== Sheet: {ws.title} ===")
        for row in ws.iter_rows(values_only=True):
            cells = ["" if v is None else str(v).strip() for v in row]
            if any(cells):
                out.append(" | ".join(cells).rstrip(" |"))
        out.append("")
    return nfc("\n".join(out))


def so_trang(f: Path) -> int:
    out = subprocess.run(["pdfinfo", str(f)], capture_output=True, text=True).stdout
    m = re.search(r"Pages:\s+(\d+)", out)
    return int(m.group(1)) if m else 0


def _ocr_trang(args):
    f, i = args
    with tempfile.TemporaryDirectory() as d:
        subprocess.run(["pdftoppm", "-r", "200", "-f", str(i), "-l", str(i), "-png", str(f), f"{d}/p"],
                       check=True, capture_output=True)
        png = next(Path(d).glob("p*.png"))
        # OMP_THREAD_LIMIT=1: tesseract tự mở nhiều luồng OpenMP; 4 tiến trình song song trên máy ít nhân sẽ tranh
        # chấp và chậm hàng trăm lần (đo 09/10/2026: 2 giây/trang đơn luồng, >7 phút/trang khi tranh chấp).
        r = subprocess.run(["tesseract", str(png), "-", "-l", "vie"], capture_output=True, text=True,
                           env={**os.environ, "OMP_THREAD_LIMIT": "1"})
    return i, r.stdout


def trich_pdf(f: Path) -> tuple[str, str]:
    """Trả về (text, cách) với cách = 'pdftotext' hoặc 'ocr'."""
    n = so_trang(f)
    text = subprocess.run(["pdftotext", "-layout", str(f), "-"], capture_output=True, text=True).stdout
    if n and len(text.strip()) / n >= NGUONG_CHU_MOI_TRANG:
        return nfc(text), "pdftotext"
    if not shutil.which("tesseract"):
        raise RuntimeError("PDF là bản quét nhưng máy không có tesseract (cần tesseract-ocr + tesseract-ocr-vie)")
    with ThreadPoolExecutor(max_workers=4) as ex:
        pages = dict(ex.map(_ocr_trang, [(f, i) for i in range(1, n + 1)]))
    body = "\n".join(f"\n===== Trang {i} =====\n{pages[i]}" for i in range(1, n + 1))
    return nfc(body), "ocr"


def trich_text(f: Path) -> tuple[str, str]:
    """Bóc chữ từ một tệp gốc. Trả về (text, cách)."""
    s = f.suffix.lower()
    if s == ".docx":
        return trich_docx(f), "docx"
    if s == ".doc":
        return trich_doc(f), "doc->docx"
    if s == ".xlsx":
        return trich_xlsx(f), "xlsx"
    if s == ".pdf":
        return trich_pdf(f)
    raise ValueError(f"không hỗ trợ định dạng {s}")


# ----------------------------------------------------------------------------- chất lượng
def kiem_tra_chat_luong(text: str) -> tuple[bool, str]:
    """Trả về (đạt, lý do). Bỏ dòng đầu (header '[Bản trích chữ ...]') khi chấm."""
    body = text.split("\n", 1)[1] if text.startswith("[") and "\n" in text else text
    body = nfc(body)
    chu = sum(1 for c in body if c.isalpha())
    if len(body.strip()) < DO_DAI_TOI_THIEU:
        return False, f"quá ngắn ({len(body.strip())} ký tự)"
    hoi = body.count("?")
    ty_le = hoi / chu if chu else 1.0
    if ty_le >= TY_LE_HOI_TOI_DA:
        return False, f"tỷ lệ '?' {ty_le:.2%} ≥ 0,5 % (hỏng mã tiếng Việt?)"
    low = body.casefold()
    if any(c in low for c in CUM_CHINH):
        return True, "đạt"
    if any(c in low for c in CUM_PHU) or CUM_PHU_RX.search(low):
        return True, "đạt (cụm phụ: phụ lục/mẫu/kính gửi/danh mục/sao y/quy trình/điều n)"
    return False, "không thấy cụm 'CỘNG HÒA XÃ HỘI CHỦ NGHĨA' / 'Điều 1' / 'Căn cứ'"


# ----------------------------------------------------------------------------- danh sách việc
def tep_goc(vbg: Path) -> list[Path]:
    return sorted(f for f in vbg.rglob("*") if f.is_file() and f.suffix.lower() in DUOI_GOC)


def nhom_theo_ten(files: list[Path]) -> dict[Path, list[Path]]:
    """Gom các tệp cùng thư mục + cùng tên gốc; khóa = đường dẫn .txt đích."""
    nhom: dict[Path, list[Path]] = {}
    for f in files:
        nhom.setdefault(f.with_suffix(".txt"), []).append(f)
    for k in nhom:
        nhom[k].sort(key=lambda p: UU_TIEN[p.suffix.lower()])
    return nhom


def header(f: Path, cach: str, text: str) -> str:
    if cach == "ocr":
        return (f"[OCR] [Bản trích chữ tự động bằng tesseract tiếng Việt từ bản quét {f.name} — {so_trang(f)} trang. "
                "Có thể sai số, ngày, dấu; số/ngày phải đối chiếu bản gốc trên GitHub trước khi trích dẫn.]\n")
    if cach == "pdftotext":
        return (f"[Bản trích chữ tự động bằng pdftotext từ {f.name} — {so_trang(f)} trang. "
                "Đối chiếu bản gốc trên GitHub khi trích nguyên văn.]\n")
    n_doan = sum(1 for l in text.split("\n") if l.strip())
    return (f"[Bản trích chữ tự động ({cach}) từ {f.name} — {n_doan} đoạn, chuẩn hóa Unicode NFC. "
            "Đối chiếu bản gốc trên GitHub khi trích nguyên văn.]\n")


def sinh_txt(nguon: list[Path], dich: Path, ghi_de: bool = False) -> tuple[Path | None, str]:
    """Thử lần lượt các nguồn theo ưu tiên; ghi .txt đầu tiên đạt chất lượng. Trả (đường dẫn hoặc None, thông báo)."""
    if dich.exists() and not ghi_de:
        return dich, "đã có"
    loi = []
    for f in nguon:
        try:
            text, cach = trich_text(f)
        except Exception as e:  # noqa: BLE001
            loi.append(f"{f.name}: {e}")
            continue
        ok, ly_do = kiem_tra_chat_luong(text)
        if not ok:
            loi.append(f"{f.name} ({cach}): {ly_do}")
            continue
        dich.write_text(header(f, cach, text) + "\n" + text.strip() + "\n", encoding="utf-8")
        return dich, f"{cach}; {ly_do}"
    return None, "; ".join(loi)


def quet() -> tuple[list[tuple[Path, list[Path]]], list[tuple[Path, str]]]:
    """Trả về (danh sách (txt đích, nguồn) còn thiếu, danh sách (txt, lý do) không đạt)."""
    thieu, khong_dat = [], []
    for vbg in sorted(REPO.glob("*/skills/*/van-ban-goc")):
        for dich, nguon in nhom_theo_ten(tep_goc(vbg)).items():
            if not dich.exists():
                thieu.append((dich, nguon))
                continue
            ok, ly_do = kiem_tra_chat_luong(dich.read_text(encoding="utf-8", errors="replace"))
            if not ok:
                khong_dat.append((dich, ly_do))
    return thieu, khong_dat


def main() -> int:
    ap = argparse.ArgumentParser(description="Bản trích chữ toàn văn cho tệp gốc trong van-ban-goc/")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--chi", help="chỉ xử lý một tệp gốc")
    ap.add_argument("--kiem", help="chỉ chấm chất lượng một bản .txt")
    ap.add_argument("--ghi-de", action="store_true", help="ghi đè .txt đã có (dùng với --chi)")
    a = ap.parse_args()

    if a.kiem:
        ok, ly_do = kiem_tra_chat_luong(Path(a.kiem).read_text(encoding="utf-8", errors="replace"))
        print(("ĐẠT: " if ok else "KHÔNG ĐẠT: ") + ly_do)
        return 0 if ok else 1

    if a.chi:
        f = Path(a.chi).resolve()
        out, tb = sinh_txt([f], f.with_suffix(".txt"), ghi_de=a.ghi_de)
        print(f"{'→ ' + str(out) if out else 'LỖI'}: {tb}")
        return 0 if out else 1

    thieu, khong_dat = quet()
    print(f"Tệp gốc chưa có bản trích chữ cùng tên: {len(thieu)}")
    for dich, nguon in thieu:
        print(f"  - {dich.relative_to(REPO)}  <- {', '.join(p.suffix for p in nguon)}")
    print(f"Bản trích chữ không đạt kiểm tra chất lượng: {len(khong_dat)}")
    for dich, ly_do in khong_dat:
        print(f"  - {dich.relative_to(REPO)}: {ly_do}")
    if a.check:
        return 1 if (thieu or khong_dat) else 0

    loi = []
    for dich, nguon in thieu:
        out, tb = sinh_txt(nguon, dich)
        if out:
            print(f"→ {out.relative_to(REPO)} ({tb})", flush=True)
        else:
            loi.append((dich, tb))
            print(f"LỖI {dich.relative_to(REPO)}: {tb}", flush=True)
    if loi:
        print(f"\nKhông sinh được {len(loi)} bản trích chữ — xem lý do ở trên.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
