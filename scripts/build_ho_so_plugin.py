#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_ho_so_plugin.py — đồng bộ thư mục trang-thai/ và các script trạng thái hồ sơ vào plugin ho-so-sct-vn
(Bạn chốt 18/10/2026). Lý do: trang-thai/ và scripts/ ở gốc kho KHÔNG vào gói claude.ai; plugin ho-so-sct-vn mang
bản chép để phiên trên claude.ai đọc được trạng thái hồ sơ (GATE "Đọc trạng thái hồ sơ").

    python3 scripts/build_ho_so_plugin.py            # chép trang-thai/*.md + 5 script vào plugin
    python3 scripts/build_ho_so_plugin.py --check    # CI: bản chép phải khớp nguồn (chạy kèm check_descriptions.py)

NGUỒN CHUẨN là trang-thai/ và scripts/ ở gốc kho — không sửa bản chép trong plugin. Sau mỗi lần ghi nhật ký
(ghi_nhat_ky.py tự gọi script này) hay sửa script, chạy lại rồi commit cả hai nơi.
"""
from __future__ import annotations

import filecmp
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True
REPO = Path(__file__).resolve().parent.parent
NGUON_TT = REPO / "trang-thai"
NGUON_SC = REPO / "scripts"
PLUGIN = REPO / "ho-so-sct-vn" / "skills" / "ho-so-sct-vn"
SCRIPTS = ["trang_thai_lib.py", "tim_ho_so.py", "trang_thai_ho_so.py", "ghi_nhat_ky.py", "check_trang_thai.py"]


def cap() -> list[tuple[Path, Path]]:
    ra = [(p, PLUGIN / "trang-thai" / p.name) for p in sorted(NGUON_TT.glob("*.md"))]
    ra += [(NGUON_SC / s, PLUGIN / "scripts" / s) for s in SCRIPTS]
    return ra


def main() -> int:
    check = "--check" in sys.argv
    if not NGUON_TT.is_dir():
        print("Chưa có trang-thai/ — bỏ qua.")
        return 0
    loi = []
    for src, dst in cap():
        if check:
            if not dst.exists() or not filecmp.cmp(src, dst, shallow=False):
                loi.append(str(dst.relative_to(REPO)))
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
    if check:
        thua = [p for p in (PLUGIN / "trang-thai").glob("*.md") if not (NGUON_TT / p.name).exists()] \
            if (PLUGIN / "trang-thai").is_dir() else []
        loi += [f"{p.relative_to(REPO)} (thừa, nguồn đã xóa)" for p in thua]
        if loi:
            print("Bản chép trong ho-so-sct-vn LỆCH nguồn — chạy python3 scripts/build_ho_so_plugin.py:")
            for x in loi:
                print("  - " + x)
            return 1
        print(f"ho-so-sct-vn khớp nguồn ({len(cap())} tệp).")
        return 0
    for p in (PLUGIN / "trang-thai").glob("*.md"):
        if not (NGUON_TT / p.name).exists():
            p.unlink()
    print(f"Đã chép {len(cap())} tệp vào {PLUGIN.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
