#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_gate0.py — kiểm quy tắc R23 của GATE 0 (Bạn chốt 17/10/2026, bản giao việc mục 1.5).

Dựng một .docx từ mẫu thật tờ trình (examples/sct/to-trinh-vbqppl-tien-chat-thuoc-no.docx), chèn vào thân một câu
viện dẫn hai số hiệu văn bản quy phạm CHƯA có tệp gốc trong kho — câu lấy NGUYÊN từ mẫu thật
examples/ubnd/phieu-trinh-giai-quyet-cong-viec.docx, không bịa số hiệu — rồi kiểm:
  1. R23 cảnh báo (WARN) đủ hai số hiệu đó; không cảnh báo số hiệu đã có trong kho (181/2024/NĐ-CP).
  2. Có can-cu-phien.txt liệt kê 74/2026/NĐ-CP cạnh file → không còn cảnh báo số đó, vẫn cảnh báo số kia.
  3. ke-hoach-soan.txt ghi số hiệu kèm "chưa có nguồn" → KHÔNG được tính là có nguồn.
  4. R23 không bao giờ ở mức FAIL.

Chạy tại thư mục plugin:  python3 tests/test_gate0.py   (run_regression.py gọi kèm, mục 5)
Thoát mã 0 = đạt.
"""
from __future__ import annotations

import shutil
import sys
from copy import deepcopy
from pathlib import Path

PLUGIN = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PLUGIN / "scripts"))

from docx import Document  # noqa: E402
from docx.text.paragraph import Paragraph  # noqa: E402

from qa_rules import FAIL, chay  # noqa: E402

NGUON = PLUGIN / "examples" / "sct" / "to-trinh-vbqppl-tien-chat-thuoc-no.docx"
# Nguyên văn từ examples/ubnd/phieu-trinh-giai-quyet-cong-viec.docx (đoạn "Các ý kiến tham gia tập trung vào: …").
CAU = ("Các ý kiến tham gia tập trung vào: cập nhật căn cứ pháp lý theo Nghị định số 74/2026/NĐ-CP "
       "(thay thế Nghị định số 08/2025/NĐ-CP).")
# 18/10/2026: NĐ 74/2026/NĐ-CP đã có bản gốc trong kho → chỉ còn 08/2025/NĐ-CP chưa có nguồn
CHUA_CO = ["08/2025/NĐ-CP"]
DA_CO = ["181/2024/NĐ-CP", "74/2026/NĐ-CP"]


def dung_file(dich: Path) -> Path:
    """Bản sao tờ trình, chèn CAU thành một đoạn mới ngay sau đoạn 20 (thân văn bản, ngoài vùng căn cứ)."""
    dich.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(NGUON, dich)
    d = Document(str(dich))
    neo = d.paragraphs[20]
    if not neo.text.startswith("Sở Công Thương đã tổng hợp"):
        raise SystemExit("test_gate0: mẫu tờ trình đổi bố cục — đoạn 20 không còn là đoạn tiếp thu ý kiến")
    moi = deepcopy(neo._p)
    neo._p.addnext(moi)
    p = Paragraph(moi, neo._parent)
    giu = [r for r in p.runs if r.text.strip()][0]
    for r in p.runs:
        if r._element is not giu._element:
            r.text = ""
    giu.text = CAU
    d.save(str(dich))
    return dich


def r23(p: Path) -> list[str]:
    ds = chay(p, only=["R23"])
    if any(x.level == FAIL for x in ds):
        raise AssertionError("R23 phải là WARN, không được FAIL")
    return [x.hint for x in ds]


def main() -> int:
    tam = PLUGIN / "tests" / "_ket-qua" / "gate0"
    if tam.exists():
        shutil.rmtree(tam)
    loi = []

    f = dung_file(tam / "a" / "to-trinh-gate0.docx")
    goi_y = r23(f)
    for so in CHUA_CO:
        if not any(so in g for g in goi_y):
            loi.append(f"1. R23 không cảnh báo số hiệu chưa có trong kho: {so}")
    for so in DA_CO:
        if any(so in g for g in goi_y):
            loi.append(f"1. R23 cảnh báo nhầm {so} (đã có tệp gốc trong kho)")

    f2 = dung_file(tam / "b" / "to-trinh-gate0.docx")
    (f2.parent / "can-cu-phien.txt").write_text("08/2025/NĐ-CP\n", encoding="utf-8")
    goi_y = r23(f2)
    if any("08/2025/NĐ-CP" in g for g in goi_y):
        loi.append("2. can-cu-phien.txt có 08/2025/NĐ-CP mà R23 vẫn cảnh báo")
    if goi_y:
        loi.append(f"2. còn cảnh báo ngoài dự kiến: {goi_y}")

    f3 = dung_file(tam / "c" / "to-trinh-gate0.docx")
    (f3.parent / "ke-hoach-soan.txt").write_text(
        "c) Căn cứ:\n- Nghị định số 08/2025/NĐ-CP — chưa có nguồn - cần người dùng cung cấp\n", encoding="utf-8")
    if not any("08/2025/NĐ-CP" in g for g in r23(f3)):
        loi.append("3. Căn cứ ghi 'chưa có nguồn' trong ke-hoach-soan.txt bị tính là có nguồn")

    if loi:
        print("test_gate0: ĐỎ")
        for x in loi:
            print("  • " + x)
        return 1
    print("test_gate0: xanh — R23 cảnh báo đúng số hiệu chưa có nguồn, nhận danh sách căn cứ của phiên.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
