#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""trich_chu_van_ban_goc.py — sinh bản trích chữ toàn văn (.txt) cho văn bản quy phạm pháp luật
chỉ có PDF trong van-ban-goc/ của các plugin.

Vì sao: tệp ≥ 3 MB bị export-ignore, không đi vào gói claude.ai; PDF quét không có lớp chữ.
Không có bản trích chữ thì Claude trên claude.ai không nắm được nội dung văn bản (vụ 08/10/2026).
Bản .txt nhỏ, luôn nằm trong gói, là thứ Claude đọc; PDF/Word gốc chỉ để đối chiếu trên GitHub.

Cách làm cho từng PDF có tên dạng văn bản quy phạm (ND-, TT-, Luat-, NQ-, QD-…) mà cùng thư mục
KHÔNG có .docx/.doc cùng tên gốc và chưa có .txt/.md cùng tên:
  - có lớp chữ (pdftotext ≥ 200 ký tự/trang trung bình) → pdftotext -layout;
  - không có lớp chữ (bản quét) → pdftoppm 200 dpi + tesseract -l vie, ghi rõ "[OCR]" ở đầu tệp.

Dùng:  python3 scripts/trich_chu_van_ban_goc.py [--check] [--chi <đường dẫn PDF>]
  --check: chỉ liệt kê PDF còn thiếu bản trích chữ, không sinh (thoát mã 1 nếu còn thiếu).
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
QPPL = re.compile(r"^(ND|TT|TTLT|Luat|LUAT|PL|NQ|QD)[-_ ]?(\d+)[-_ ](\d{4})", re.I)


def can_trich(f: Path) -> bool:
    if f.suffix.lower() != ".pdf" or not QPPL.match(f.name):
        return False
    anh_em = {p.suffix.lower() for p in f.parent.iterdir() if p.stem == f.stem}
    return not ({".docx", ".doc", ".txt", ".md"} & anh_em)


def so_trang(f: Path) -> int:
    out = subprocess.run(["pdfinfo", str(f)], capture_output=True, text=True).stdout
    m = re.search(r"Pages:\s+(\d+)", out)
    return int(m.group(1)) if m else 0


def ocr_trang(args):
    f, i = args
    with tempfile.TemporaryDirectory() as d:
        subprocess.run(["pdftoppm", "-r", "200", "-f", str(i), "-l", str(i), "-png", str(f), f"{d}/p"],
                       check=True, capture_output=True)
        png = next(Path(d).glob("p*.png"))
        r = subprocess.run(["tesseract", str(png), "-", "-l", "vie"], capture_output=True, text=True)
    return i, r.stdout


def trich(f: Path) -> Path:
    n = so_trang(f)
    text = subprocess.run(["pdftotext", "-layout", str(f), "-"], capture_output=True, text=True).stdout
    out = f.with_suffix(".txt")
    if n and len(text.strip()) / n >= 200:
        out.write_text(f"[Bản trích chữ tự động bằng pdftotext từ {f.name} — {n} trang. "
                       f"Đối chiếu bản gốc trên GitHub khi trích nguyên văn.]\n\n" + text, encoding="utf-8")
        return out
    with ThreadPoolExecutor(max_workers=4) as ex:
        pages = dict(ex.map(ocr_trang, [(f, i) for i in range(1, n + 1)]))
    body = "\n".join(f"\n===== Trang {i} =====\n{pages[i]}" for i in range(1, n + 1))
    out.write_text(f"[OCR] [Bản trích chữ tự động bằng tesseract tiếng Việt từ bản quét {f.name} — {n} trang. "
                   f"Có thể sai số, ngày, dấu; số/ngày phải đối chiếu bản gốc trên GitHub trước khi trích dẫn.]\n"
                   + body, encoding="utf-8")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--chi", help="chỉ xử lý một PDF")
    a = ap.parse_args()
    if a.chi:
        print(trich(Path(a.chi)))
        return 0
    thieu = [f for vbg in sorted(REPO.glob("*/skills/*/van-ban-goc")) for f in sorted(vbg.rglob("*.pdf")) if can_trich(f)]
    print(f"PDF văn bản quy phạm chưa có bản trích chữ: {len(thieu)}")
    for f in thieu:
        print(f"  - {f.relative_to(REPO)} ({so_trang(f)} trang)")
    if a.check:
        return 1 if thieu else 0
    for f in thieu:
        print(f"→ {trich(f).relative_to(REPO)}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
