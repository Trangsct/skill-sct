#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""thong_ke_so_loi.py — đếm lỗi Bạn chỉ ra theo tuần, lấy từ sổ lỗi tự ghi của mọi plugin (đề xuất 8, 18/10/2026).

    python3 scripts/thong_ke_so_loi.py              # bảng theo tuần ISO, theo plugin
    python3 scripts/thong_ke_so_loi.py --tu 17/10/2026

Dùng sau vài tuần để xem bản nâng cấp 17/10/2026 (GATE 0, 0b, rà soát độc lập) có giảm số lỗi phải sửa thật không.
Nguồn: các mục "### Lnnn — dd/mm/yyyy — …" trong references/so-loi-tu-ghi.md (vbhc-vn: reference/).
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path(__file__).resolve().parent.parent
DE = re.compile(r"^###\s+L(\d{3})\s+—\s+(\d{2})/(\d{2})/(\d{4})\s+—\s+(.*)$")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tu", help="chỉ tính từ ngày dd/mm/yyyy")
    a = ap.parse_args()
    tu = None
    if a.tu:
        d, m, y = (int(x) for x in a.tu.split("/"))
        tu = date(y, m, d)
    bang: dict[tuple[int, int], dict[str, int]] = defaultdict(lambda: defaultdict(int))
    tong = 0
    for p in sorted(REPO.glob("*/skills/*/reference*/so-loi-tu-ghi.md")):
        plugin = p.parents[2].name
        for ln in p.read_text(encoding="utf-8").splitlines():
            m = DE.match(ln)
            if not m:
                continue
            ng = date(int(m.group(4)), int(m.group(3)), int(m.group(2)))
            if tu and ng < tu:
                continue
            y, w, _ = ng.isocalendar()
            bang[(y, w)][plugin] += 1
            tong += 1
    if not bang:
        print("Chưa có mục lỗi nào trong sổ lỗi tự ghi.")
        return 0
    for (y, w) in sorted(bang):
        chi_tiet = ", ".join(f"{k} {v}" for k, v in sorted(bang[(y, w)].items()))
        print(f"Tuần {w:02d}/{y}: {sum(bang[(y, w)].values()):3d} lỗi  ({chi_tiet})")
    print(f"\nTổng {tong} lỗi Bạn chỉ ra đã được ghi vào plugin.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
