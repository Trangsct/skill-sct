#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_sigsplit.py — kiểm hàm check_sig_split (qa_pdf_check.py) không cần LibreOffice (sửa 17/10/2026).

Dùng khối ký thật của examples/sct/cong-van-de-nghi-bo-sung-ho-so.docx và các trang PDF giả lập:
  1. Khối ký trọn một trang, trang sau là Phụ lục → KHÔNG báo (cách cũ báo nhầm mọi văn bản có phụ lục).
  2. "KT. GIÁM ĐỐC" ở trang 1, "PHÓ GIÁM ĐỐC" + tên người ký sang trang 2 → PHẢI báo (cách cũ bỏ sót).
  3. File không có khối ký nhận dạng được → chỉ nhắc soát tay ("không tìm thấy…"), không đoán theo trang.

Chạy tại thư mục plugin:  python3 tests/test_sigsplit.py   (run_regression.py gọi kèm, mục 7)
"""
from __future__ import annotations

import sys
from pathlib import Path

PLUGIN = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PLUGIN / "scripts"))

from qa_pdf_check import _o_ky_docx, check_sig_split  # noqa: E402

MAU = PLUGIN / "examples" / "sct" / "cong-van-de-nghi-bo-sung-ho-so.docx"
KHONG_KY = PLUGIN / "examples" / "sct" / "phu-bieu-danh-gia-nhiem-vu-giao-ban-qlcn.docx"


def main() -> int:
    loi = []
    dong = _o_ky_docx(MAU)
    if not dong or len(dong) < 2:
        print(f"test_sigsplit: ĐỎ — không đọc được khối ký của mẫu: {dong}")
        return 1
    dau, ten = dong[0], dong[-1]
    than = "Sở Công Thương đề nghị Công ty hoàn thiện hồ sơ./."
    tron = [f"{than}\nNơi nhận:   {dau}\n- Như trên;\n" + "\n".join(dong[1:]), "Phụ lục\nDANH MỤC HỒ SƠ\n1 ..."]
    if check_sig_split(tron, MAU):
        loi.append("1. báo nhầm gãy khối ký khi trang sau là phụ lục")
    gay = [f"{than}\nNơi nhận:   {dau}\n- Như trên;", "\n".join(dong[1:]) + "\n- Lưu: VT, CN."]
    if not check_sig_split(gay, MAU):
        loi.append(f"2. bỏ sót khối ký gãy trang ('{dau}' trang 1, '{ten}' trang 2)")
    r = check_sig_split(["BẢNG ĐÁNH GIÁ", "trang 2"], KHONG_KY)
    if len(r) != 1 or not r[0].startswith("không tìm thấy"):
        loi.append(f"3. file không có khối ký phải chỉ nhắc soát tay: {r}")
    if loi:
        print("test_sigsplit: ĐỎ")
        for x in loi:
            print("  • " + x)
        return 1
    print("test_sigsplit: xanh — không báo nhầm phụ lục, bắt được khối ký gãy trang.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
