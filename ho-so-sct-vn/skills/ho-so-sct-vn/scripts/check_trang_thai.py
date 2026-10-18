#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_trang_thai.py — CI: kiểm tệp trạng thái hồ sơ trong trang-thai/ (Bạn chốt 17/10/2026, mục 5.5).

    python3 scripts/check_trang_thai.py

Mỗi tệp (trừ MAU.md, README.md) phải có: dòng tiêu đề "# …", dòng "Bí danh:", dòng "Plugin liên quan:" trỏ
plugin có thật trong kho, đủ 7 mục "##" của mẫu theo đúng thứ tự, ít nhất một mục nhật ký và mục nhật ký CUỐI
có ngày ("### dd/mm/yyyy" hoặc "### Tóm tắt đến ngày dd/mm/yyyy"); nhật ký không quá 10 mục (mục 6.3); không
chứa số điện thoại, tài khoản, người đại diện, thông tin đăng ký doanh nghiệp, sức khỏe, đời tư (mục 6.2 —
kho công khai). Gọi từ check_descriptions.py nên CI validate-plugins.yml đỏ khi vi phạm.

Thoát mã 0 = đạt, 1 = có lỗi.
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True  # nhập trang_thai_lib cạnh script: không sinh __pycache__ trong kho (CI chặn)

from trang_thai_lib import DE_NHAT_KY, MUC, REPO, THU_MUC, TRONG_GOI, HoSo, cac_tep, kiem_rieng_tu

TOI_DA_NHAT_KY = 10


def kiem(p) -> list[str]:
    hs = HoSo(p)
    loi = []
    if not any(ln.startswith("# ") for ln in hs.dau):
        loi.append("thiếu dòng tiêu đề '# Tên hồ sơ'")
    if not hs.bi_danh:
        loi.append("thiếu dòng 'Bí danh:' (tim_ho_so.py cần để tự chọn tệp)")
    if not hs.plugins:
        loi.append("thiếu dòng 'Plugin liên quan:'")
    for pl in hs.plugins:
        if not TRONG_GOI and not (REPO / pl / ".claude-plugin" / "plugin.json").exists():
            loi.append(f"plugin không có trong kho: {pl}")
    thieu = [m for m in MUC if m not in hs.muc]
    if thieu:
        loi.append("thiếu mục: " + "; ".join(thieu))
    else:
        thu_tu = [m for m in hs.thu_tu if m in MUC]
        if thu_tu != MUC:
            loi.append("các mục không đúng thứ tự của trang-thai/MAU.md")
    nk = hs.muc_nhat_ky()
    if not nk:
        loi.append("Nhật ký phiên chưa có mục nào ('### dd/mm/yyyy')")
    else:
        if not DE_NHAT_KY.match(nk[-1][0]):
            loi.append(f"mục nhật ký cuối không có ngày: '{nk[-1][0]}'")
        if len(nk) > TOI_DA_NHAT_KY:
            loi.append(f"nhật ký {len(nk)} mục > {TOI_DA_NHAT_KY} — chạy ghi_nhat_ky.py để tự gộp mục cũ")
    for x in kiem_rieng_tu(p.read_text(encoding="utf-8")):
        loi.append(f"lộ thông tin riêng ({x}) — kho công khai, xóa đi")
    return loi


def main() -> int:
    if not THU_MUC.is_dir():
        print("Chưa có thư mục trang-thai/ — bỏ qua.")
        return 0
    if not (THU_MUC / "MAU.md").exists():
        print("LỖI: thiếu trang-thai/MAU.md")
        return 1
    tong = 0
    for p in cac_tep():
        loi = kiem(p)
        tong += len(loi)
        print(f"{'ok  ' if not loi else 'LỖI '} {p.relative_to(REPO)}")
        for x in loi:
            print(f"      - {x}")
    print(f"\n{len(cac_tep())} tệp trạng thái, {tong} lỗi.")
    return 1 if tong else 0


if __name__ == "__main__":
    sys.exit(main())
