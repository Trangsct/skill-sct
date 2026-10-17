#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""test_ra_soat.py — kiểm GATE cuối (Bạn chốt 17/10/2026, bản giao việc mục 3).

  1. ra_soat_doc_lap.py đo đúng: bỏ dòng trống sau "Kính gửi" của mẫu thật công văn → mục [3] báo 0 dòng (⚠).
  2. kiem_tra_truoc_khi_giao.py --tu-sua sửa lại đúng 1 dòng, Nơi nhận cỡ 11, dòng Lưu bỏ tên chuyên viên, và
     không làm phát sinh FAIL mới so với mẫu thật.
  3. Một lệnh kiem_tra_truoc_khi_giao.py chạy xong dưới 30 giây.

Chạy tại thư mục plugin:  python3 tests/test_ra_soat.py   (run_regression.py gọi kèm, mục 6)
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import time
from pathlib import Path

PLUGIN = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PLUGIN / "scripts"))

from docx import Document  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402

import ra_soat_doc_lap  # noqa: E402
from qa_rules import FAIL, _tt, chay  # noqa: E402

NGUON = PLUGIN / "examples" / "sct" / "cong-van-de-nghi-bo-sung-ho-so.docx"


def muc(ds, ten):
    return [x for x in ds if x["muc"] == ten]


def main() -> int:
    tam = PLUGIN / "tests" / "_ket-qua" / "ra-soat"
    if tam.exists():
        shutil.rmtree(tam)
    tam.mkdir(parents=True)
    f = tam / "cong-van-ra-soat.docx"
    shutil.copy(NGUON, f)
    d = Document(str(f))
    kids = list(d.element.body)
    i = next(k for k, el in enumerate(kids) if el.tag == qn("w:p") and _tt(el).strip().startswith("Kính gửi"))
    j = i + 1
    while _tt(kids[j]).strip().startswith(("-", "+")):
        j += 1
    if _tt(kids[j]).strip():
        raise SystemExit("test_ra_soat: mẫu đổi bố cục — sau khối Kính gửi không còn dòng trống")
    d.element.body.remove(kids[j])
    d.save(str(f))
    loi = []

    x = muc(ra_soat_doc_lap.do(f, render=False), "3. Sau Kính gửi")
    if not x or not x[0]["canh_bao"] or not x[0]["noi_dung"].startswith("0 "):
        loi.append(f"1. ra_soat_doc_lap.py không báo thiếu dòng trống sau Kính gửi: {x}")

    fail_goc = {(y.code) for y in chay(NGUON) if y.level == FAIL}
    t0 = time.time()
    subprocess.run([sys.executable, str(PLUGIN / "scripts" / "kiem_tra_truoc_khi_giao.py"), str(f), "--tu-sua"],
                   capture_output=True, text=True, timeout=120)
    giay = time.time() - t0
    ds = ra_soat_doc_lap.do(f, render=False)
    x = muc(ds, "3. Sau Kính gửi")
    if not x or x[0]["canh_bao"]:
        loi.append(f"2. --tu-sua không khôi phục đúng 1 dòng trống sau Kính gửi: {x}")
    if any(y["canh_bao"] for y in muc(ds, "2. Nơi nhận")):
        loi.append("2. --tu-sua chưa đưa dòng Nơi nhận về cỡ 11")
    moi = [y for y in chay(f) if y.level == FAIL and y.code not in fail_goc]
    if moi:
        loi.append("2. --tu-sua làm phát sinh FAIL mới: " + ", ".join(y.code for y in moi))
    if any(y.code == "R07" for y in chay(f)):
        loi.append("2. --tu-sua chưa bỏ tên chuyên viên ở dòng Lưu (R07)")
    if giay >= 30:
        loi.append(f"3. kiem_tra_truoc_khi_giao.py mất {giay:.1f}s ≥ 30s")

    if loi:
        print("test_ra_soat: ĐỎ")
        for y in loi:
            print("  • " + y)
        return 1
    print(f"test_ra_soat: xanh — đo đúng, tự sửa đúng, một lệnh {giay:.1f}s.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
