#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_anti_error_format.py — kiểm định dạng SỔ LỖI TỰ GHI của mọi plugin (Bạn chốt 17/10/2026, mục 4.3).

    python3 scripts/check_anti_error_format.py            # kiểm mọi sổ lỗi; CI gọi qua check_descriptions.py
    python3 scripts/check_anti_error_format.py --tao hc-sct-vn   # tạo sổ lỗi rỗng cho một plugin
    python3 scripts/check_anti_error_format.py --so-tiep vbhc-vn # in số thứ tự lỗi kế tiếp

Sổ lỗi tự ghi là nơi Claude ghi lỗi Bạn chỉ ra NGAY TRONG PHIÊN (CLAUDE.md mục "Tự ghi lỗi"): mỗi plugin một tệp
`skills/<plugin>/references/so-loi-tu-ghi.md` (vbhc-vn: `reference/so-loi-tu-ghi.md`). Mỗi lỗi một mục:

    ### L001 — 17/10/2026 — Tiêu đề ngắn
    - Lỗi: mô tả lỗi đã mắc (văn bản nào, sai chỗ nào — đã ẩn danh)
    - Cách đúng: cách viết / trình bày đúng
    - Ví dụ: ví dụ ngắn đã ẩn danh (không bắt buộc)
    - Máy kiểm: R23 (qa_rules.py) | check_facts `ma-rule` | không — loại N

Kiểm: số thứ tự L001, L002… liên tục không trùng; ngày dd/mm/yyyy hợp lệ; có dòng "- Lỗi:" và "- Cách đúng:" không
rỗng; không lộ số điện thoại, tài khoản, người đại diện (kho công khai). Các mục anti-error văn xuôi có từ trước
(vbhc-vn phong-tranh-sai-lam.md nhóm A–O, sd-vlncn ref 11, tkm ref 08…) giữ nguyên, không ép theo định dạng này.

Thoát mã 0 = đạt, 1 = có lỗi.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

from trang_thai_lib import kiem_rieng_tu, nfc

REPO = Path(__file__).resolve().parent.parent
TEN = "so-loi-tu-ghi.md"
DE = re.compile(r"^###\s+L(\d{3})\s+—\s+(\d{2})/(\d{2})/(\d{4})\s+—\s+(\S.*)$")
DAU_TEP = """# Sổ lỗi tự ghi — {plugin}

Lỗi Bạn chỉ ra trong phiên, Claude ghi ngay theo CLAUDE.md mục "Tự ghi lỗi" (Bạn chốt 17/10/2026). Đọc tệp này trước khi
soạn văn bản thuộc lĩnh vực của plugin. Định dạng mỗi mục và cách kiểm: `scripts/check_anti_error_format.py` ở gốc kho.
Lỗi kiểm được bằng máy thì kèm quy tắc trong `qa_rules.py` (vbhc-vn) hoặc `check_facts.py` và ghi mã ở dòng "Máy kiểm".
Yêu cầu riêng cho MỘT văn bản không ghi ở đây mà ghi vào `trang-thai/<hồ sơ>.md` mục "Yêu cầu riêng một lần".
"""


def cac_so() -> list[Path]:
    ra = []
    for d in sorted(REPO.glob("*/skills/*")):
        for sub in ("references", "reference"):
            p = d / sub / TEN
            if p.exists():
                ra.append(p)
    return ra


def duong_dan(plugin: str) -> Path:
    goc = REPO / plugin / "skills" / plugin
    if not goc.is_dir():
        raise SystemExit(f"Không có plugin {plugin}")
    sub = "reference" if (goc / "reference").is_dir() and not (goc / "references").is_dir() else "references"
    return goc / sub / TEN


def doc_muc(p: Path) -> list[tuple[str, list[str]]]:
    muc: list[tuple[str, list[str]]] = []
    for ln in nfc(p.read_text(encoding="utf-8")).splitlines():
        if ln.startswith("### "):
            muc.append((ln, []))
        elif muc:
            muc[-1][1].append(ln)
    return muc


def kiem(p: Path) -> list[str]:
    loi = []
    so_truoc = 0
    for de, noi in doc_muc(p):
        m = DE.match(de)
        if not m:
            loi.append(f"tiêu đề sai mẫu '### L001 — dd/mm/yyyy — Tiêu đề': {de}")
            continue
        so, d, mo, y = (int(x) for x in m.groups()[:4])
        if so != so_truoc + 1:
            loi.append(f"L{so:03d}: số thứ tự không liên tục (trước là L{so_truoc:03d})")
        so_truoc = so
        try:
            date(y, mo, d)
        except ValueError:
            loi.append(f"L{so:03d}: ngày không hợp lệ {d:02d}/{mo:02d}/{y}")
        for nhan in ("- Lỗi:", "- Cách đúng:"):
            dong = next((ln for ln in noi if ln.startswith(nhan)), None)
            if dong is None or not dong[len(nhan):].strip():
                loi.append(f"L{so:03d}: thiếu dòng '{nhan}' có nội dung")
    for x in kiem_rieng_tu(p.read_text(encoding="utf-8")):
        loi.append(f"lộ thông tin riêng ({x}) — kho công khai, ẩn danh lại")
    return loi


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tao", metavar="PLUGIN", help="tạo sổ lỗi rỗng cho plugin này")
    ap.add_argument("--so-tiep", metavar="PLUGIN", help="in số thứ tự lỗi kế tiếp của plugin này")
    a = ap.parse_args()
    if a.tao:
        p = duong_dan(a.tao)
        if p.exists():
            print(f"Đã có {p.relative_to(REPO)}")
            return 0
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(DAU_TEP.format(plugin=a.tao), encoding="utf-8")
        print(f"Đã tạo {p.relative_to(REPO)} — thêm dòng dẫn tệp này vào bảng reference của SKILL.md")
        return 0
    if a.so_tiep:
        p = duong_dan(a.so_tiep)
        n = 0
        if p.exists():
            n = max([int(m.group(1)) for m in (DE.match(h) for h, _ in doc_muc(p)) if m] or [0])
        print(f"L{n + 1:03d}")
        return 0
    tong = 0
    ds = cac_so()
    for p in ds:
        loi = kiem(p)
        tong += len(loi)
        print(f"{'ok  ' if not loi else 'LỖI '} {p.relative_to(REPO)} ({len(doc_muc(p))} mục)")
        for x in loi:
            print(f"      - {x}")
    print(f"\n{len(ds)} sổ lỗi tự ghi, {tong} lỗi định dạng.")
    return 1 if tong else 0


if __name__ == "__main__":
    sys.exit(main())
