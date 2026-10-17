#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tim_ho_so.py — chọn tệp trạng thái hồ sơ trong trang-thai/ từ câu yêu cầu của Bạn (Bạn chốt 17/10/2026).

    python3 scripts/tim_ho_so.py "soạn công văn đôn đốc cụm Phú Thịnh 1"
    python3 scripts/tim_ho_so.py "Làng Cang 2" --json

So câu yêu cầu (bỏ dấu, không phân biệt hoa thường) với tên hồ sơ, dòng "Bí danh:" và tên tệp của từng tệp
trong trang-thai/. Điểm = độ dài cụm khớp dài nhất, nên "Phú Thịnh 1" thắng "Phú Thịnh" khi cả hai có mặt;
"Thống Nhất 1" không khớp nhầm "Thống Nhất 10" (biên chữ số).

Thoát mã 0 và in đường dẫn tệp khớp nhất (kèm các tệp khớp kém hơn nếu có); mã 1 khi không tệp nào khớp —
khi đó tạo tệp mới bằng `ghi_nhat_ky.py --tao-moi`, không hỏi Bạn.
"""
from __future__ import annotations

import argparse
import json
import re
import sys

from trang_thai_lib import HoSo, REPO, bo_dau, cac_tep


def _rx(cum: str) -> re.Pattern:
    toks = [re.escape(t) for t in re.split(r"[^a-z0-9]+", bo_dau(cum)) if t]
    return re.compile(r"(?<![a-z0-9])" + r"[^a-z0-9]+".join(toks) + r"(?![a-z0-9])")


def cham(cau: str) -> list[tuple[int, HoSo, str]]:
    q = bo_dau(cau)
    ra = []
    for p in cac_tep():
        hs = HoSo(p)
        cum = [hs.ten, p.stem.replace("-", " "), *hs.bi_danh]
        tot, khop = 0, ""
        for c in cum:
            if len(bo_dau(c).strip()) < 3:
                continue
            if _rx(c).search(q) and len(c) > tot:
                tot, khop = len(c), c
        if tot:
            ra.append((tot, hs, khop))
    ra.sort(key=lambda x: -x[0])
    return ra


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cau", help="câu yêu cầu của Bạn hoặc tên/bí danh hồ sơ")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    ds = cham(a.cau)
    if a.json:
        print(json.dumps([{"tep": str(h.path.relative_to(REPO)), "ten": h.ten, "khop": k, "diem": d}
                          for d, h, k in ds], ensure_ascii=False, indent=2))
        return 0 if ds else 1
    if not ds:
        print("Không có tệp trạng thái nào khớp. Tạo mới: python3 scripts/ghi_nhat_ky.py --tao-moi \"<Tên hồ sơ>\" "
              "--bi-danh \"…\" --plugin <plugin>")
        return 1
    for i, (d, h, k) in enumerate(ds):
        dau = "→" if i == 0 else " "
        print(f"{dau} {h.path}  ({h.ten}; khớp \"{k}\")")
    return 0


if __name__ == "__main__":
    sys.exit(main())
