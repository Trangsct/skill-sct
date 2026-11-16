#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_r02.py — R02 (công thức hóa học phải có chỉ số dưới thật), sửa 16/11/2026.

Vụ thật: bảng hóa chất của biên bản kiểm tra phòng ngừa, ứng phó sự cố hóa chất có dòng KOH, NaOH
viết đúng (không có chữ số) mà R02 báo FAIL. Kiểm:
  1. KOH, NaOH, CaO, NaCl viết phẳng → KHÔNG báo.
  2. H2SO4, P2O5 viết phẳng → PHẢI báo.
  3. H₂SO₄ viết bằng run subscript thật → KHÔNG báo.

Chạy tại thư mục plugin:  python3 tests/test_r02.py   (run_regression.py gọi kèm, mục 8)
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

from docx import Document

PLUGIN = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PLUGIN / "scripts"))

import qa_rules  # noqa: E402


def _r02(doc_path: Path) -> list:
    return [f for f in qa_rules.chay(doc_path, only=["R02"]) if f.code == "R02"]


def main() -> int:
    loi = []
    with tempfile.TemporaryDirectory() as td:
        d = Document()
        d.add_paragraph("Hóa chất sử dụng: KOH, NaOH, CaO, NaCl.")
        p1 = Path(td) / "khong-chu-so.docx"; d.save(p1)

        d = Document()
        d.add_paragraph("Axit H2SO4 và P2O5 viết phẳng.")
        p2 = Path(td) / "phang.docx"; d.save(p2)

        d = Document()
        p = d.add_paragraph("Axit H")
        for txt, sub in (("2", True), ("SO", False), ("4", True), (" viết đúng.", False)):
            r = p.add_run(txt); r.font.subscript = sub or None
        p3 = Path(td) / "dung.docx"; d.save(p3)

        if _r02(p1):
            loi.append("1. bắt nhầm công thức không có chữ số (KOH, NaOH, CaO, NaCl)")
        if len(_r02(p2)) < 2:
            loi.append("2. bỏ sót H2SO4/P2O5 viết phẳng")
        if _r02(p3):
            loi.append("3. bắt nhầm H₂SO₄ đã có run subscript")
    if loi:
        print("test_r02: ĐỎ — " + "; ".join(loi))
        return 1
    print("test_r02: XANH — 3/3 trường hợp đúng")
    return 0


if __name__ == "__main__":
    sys.exit(main())
