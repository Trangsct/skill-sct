#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""trich_hieu_luc.py — điền ngày ban hành, ngày hiệu lực còn trống trong registry/trang-thai.csv TỪ BẢN GỐC trong kho
(Bạn chốt 18/10/2026, đề xuất 7 sau bản giao việc 17/10/2026).

    python3 scripts/trich_hieu_luc.py            # in những dòng sẽ điền, không ghi
    python3 scripts/trich_hieu_luc.py --ghi      # ghi vào registry/trang-thai.csv rồi sinh lại data/vbpl.json

Với mỗi mã còn trống hieu_luc: tìm tệp gốc theo DANH-MUC-VAN-BAN-GOC.csv (số hiệu → mã registry qua ma_tu_so_hieu),
mở bản .txt toàn văn, đọc câu "có hiệu lực (thi hành) (kể) từ ngày dd tháng mm năm yyyy" hoặc "kể từ ngày ký";
ngày ban hành trống thì lấy cột ngày của danh mục. Chỉ ghi khi đọc được từ chính bản gốc; ghi_chu nối thêm
"hiệu lực máy trích từ <tệp>" để phân biệt với dòng Bạn đối chiếu tay. R05 (viện dẫn văn bản chưa có hiệu lực tại
ngày ký) chỉ chạy được khi cột này có giá trị.
"""
from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "vbhc-vn" / "skills" / "vbhc-vn" / "scripts"))
from qa_rules import ma_tu_so_hieu, nfc  # noqa: E402

CSV = REPO / "registry" / "trang-thai.csv"
DM = REPO / "DANH-MUC-VAN-BAN-GOC.csv"
HL = re.compile(r"có hiệu lực(?: thi hành)?(?: kể)? từ ngày\s+(\d{1,2})\s+tháng\s+(\d{1,2})\s+năm\s+(\d{4})", re.I)
HL_KY = re.compile(r"có hiệu lực(?: thi hành)?(?: kể)? từ ngày ký", re.I)


def tep_goc(so_hieu_map: dict, ma: str):
    for so, lst in so_hieu_map.items():
        if ma_tu_so_hieu(so) != ma:
            continue
        for duong_dan, ngay in lst:
            p = REPO / duong_dan
            t = p if p.suffix == ".txt" else p.with_suffix(".txt")
            if t.exists():
                return t, ngay
    return None, None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ghi", action="store_true")
    a = ap.parse_args()
    so_hieu_map: dict[str, list] = {}
    for r in csv.DictReader(DM.open(encoding="utf-8")):
        so_hieu_map.setdefault(r["so_hieu"], []).append((r["duong_dan"], r["ngay_ban_hanh"]))
    rows = list(csv.DictReader(CSV.open(encoding="utf-8")))
    cot = list(rows[0].keys())
    n = 0
    for r in rows:
        if r["hieu_luc"].strip():
            continue
        t, ngay_dm = tep_goc(so_hieu_map, r["ma"])
        if t is None:
            continue
        text = nfc(t.read_text(encoding="utf-8", errors="replace"))
        m = HL.search(text)
        hl = None
        if m:
            d, mo, y = (int(x) for x in m.groups())
            hl = f"{d:02d}/{mo}/{y}"
        elif HL_KY.search(text) and (r["ngay_ban_hanh"].strip() or ngay_dm):
            hl = r["ngay_ban_hanh"].strip() or ngay_dm
        if not hl:
            continue
        if not r["ngay_ban_hanh"].strip() and ngay_dm:
            r["ngay_ban_hanh"] = ngay_dm
        r["hieu_luc"] = hl
        r["ghi_chu"] = (r["ghi_chu"] + "; " if r["ghi_chu"].strip() else "") + f"hiệu lực máy trích từ {t.name}"
        n += 1
        print(f"{r['ma']:28} ban hành {r['ngay_ban_hanh']:11} hiệu lực {hl:11} ← {t.name[:60]}")
    print(f"\n{n} dòng điền được từ bản gốc.")
    if a.ghi and n:
        with CSV.open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cot)
            w.writeheader()
            w.writerows(rows)
        print(f"Đã ghi {CSV.relative_to(REPO)}")
        subprocess.run([sys.executable, str(REPO / "scripts" / "build_vbpl.py")], check=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
