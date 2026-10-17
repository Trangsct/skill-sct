#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""trang_thai_ho_so.py — bảng tổng hợp mọi hồ sơ trong trang-thai/ (Bạn chốt 17/10/2026).

    python3 scripts/trang_thai_ho_so.py
    python3 scripts/trang_thai_ho_so.py --plugin kccn-sct-vn
    python3 scripts/trang_thai_ho_so.py --json

In tên hồ sơ, ngày cập nhật cuối (ngày của mục nhật ký mới nhất) và bước tiếp theo, sắp theo ngày cập nhật
giảm dần. Mở rộng từ kccn-sct-vn/scripts/trang_thai_cum.py (script đó vẫn dùng như cũ để tra bậc thủ tục của
một cụm trong tài liệu plugin; khi có tệp trạng thái trùng tên cụm, nó in thêm đường dẫn tệp).
"""
from __future__ import annotations

import argparse
import json
import sys

from trang_thai_lib import HoSo, REPO, cac_tep, ngay_khoa


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plugin", help="chỉ hồ sơ có plugin này trong dòng 'Plugin liên quan'")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    ds = [HoSo(p) for p in cac_tep()]
    if a.plugin:
        ds = [h for h in ds if a.plugin in h.plugins]
    ds.sort(key=lambda h: ngay_khoa(h.ngay_cap_nhat), reverse=True)
    if a.json:
        print(json.dumps([{"tep": str(h.path.relative_to(REPO)), "ten": h.ten, "plugin": h.plugins,
                           "cap_nhat": h.ngay_cap_nhat, "buoc_tiep_theo": h.buoc_tiep_theo} for h in ds],
                         ensure_ascii=False, indent=2))
        return 0
    if not ds:
        print("Chưa có hồ sơ nào" + (f" của {a.plugin}" if a.plugin else "") + " trong trang-thai/.")
        return 0
    for h in ds:
        print(f"{h.ngay_cap_nhat or '—':10}  {h.ten}")
        print(f"{'':10}  tệp: {h.path.relative_to(REPO)}  |  plugin: {', '.join(h.plugins) or '—'}")
        print(f"{'':10}  bước tiếp theo: {h.buoc_tiep_theo or '—'}")
    print(f"\nTổng: {len(ds)} hồ sơ.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
