#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tra_toa_do_quy_hoach.py - tra ranh giới 123 khu vực quy hoạch khoáng sản nhóm I tỉnh Lào Cai
(số hóa từ 09 sơ đồ quy hoạch: bản vẽ 3.3, 3.4, 4.6, 8.4, 8.5, 9.3, 11.2, 11.3, 12).

    python3 scripts/tra_toa_do_quy_hoach.py --ten "Làng Cáng"        # tọa độ các khu vực có tên chứa cụm từ
    python3 scripts/tra_toa_do_quy_hoach.py --diem 2475900 405200     # điểm VN-2000 (KTT 105, múi 6) nằm trong khu vực nào
    python3 scripts/tra_toa_do_quy_hoach.py --diem 22.4 104.1 --wgs84 # điểm WGS84 (vĩ độ, kinh độ)
    python3 scripts/tra_toa_do_quy_hoach.py --ban-ve 12               # danh sách khu vực của một bản vẽ
    python3 scripts/tra_toa_do_quy_hoach.py --tong-hop                # số khu vực, số điểm theo bản vẽ, loại khu vực

Dữ liệu: du-lieu/toa-do-ranh-gioi-quy-hoach-khoang-san-nhom-I-lao-cai.csv (cùng plugin).
Tọa độ chỉ để tham khảo; tọa độ pháp lý theo Phụ lục VI tương ứng. Khu vực có cột
doi_chieu_phu_luc_VI_du_thao = "không khớp" phải đối chiếu Phụ lục VI trước khi dùng.
Không cần thư viện ngoài.
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
import unicodedata
from collections import OrderedDict
from pathlib import Path

CSV_NAME = "toa-do-ranh-gioi-quy-hoach-khoang-san-nhom-I-lao-cai.csv"


def tim_csv() -> Path:
    here = Path(__file__).resolve().parent
    for p in (here.parent / "du-lieu" / CSV_NAME, here / CSV_NAME):
        if p.exists():
            return p
    sys.exit(f"Không thấy {CSV_NAME} trong du-lieu/")


def chuan(s: str) -> str:
    s = unicodedata.normalize("NFC", s).lower().replace("đ", "d")
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
    return " ".join(s.split())


def doc() -> "OrderedDict[tuple, dict]":
    kv: "OrderedDict[tuple, dict]" = OrderedDict()
    with open(tim_csv(), encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            key = (r["ban_ve"], r["ten_khu_vuc"])
            k = kv.setdefault(key, dict(r, diem_goc=[]))
            k["diem_goc"].append((r["diem"], float(r["x_vn2000"]), float(r["y_vn2000"]),
                                  float(r["vi_do_wgs84"]), float(r["kinh_do_wgs84"])))
    return kv


def trong_da_giac(x: float, y: float, poly: list) -> bool:
    ins = False
    n = len(poly)
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
            ins = not ins
    return ins


def kc_den_canh(x, y, poly):
    best = math.inf
    n = len(poly)
    for i in range(n):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % n]
        dx, dy = x2 - x1, y2 - y1
        t = 0 if dx == dy == 0 else max(0, min(1, ((x - x1) * dx + (y - y1) * dy) / (dx * dx + dy * dy)))
        best = min(best, math.hypot(x - (x1 + t * dx), y - (y1 + t * dy)))
    return best


def in_khu(k, toa_do=True):
    print(f"{k['ban_ve']} | {k['loai_khu_vuc']} | {k['ten_khu_vuc']}"
          f" | khoảng {k['dien_tich_so_do_ha']} ha | {k['phu_luc_toa_do']}"
          f" | đối chiếu Phụ lục VI dự thảo: {k['doi_chieu_phu_luc_VI_du_thao']}"
          + (" | tên cần đối chiếu" if k["ghi_chu_ten"] else ""))
    if toa_do:
        for d, x, y, la, lo in k["diem_goc"]:
            print(f"   {d:>3}  X={x:,.0f}  Y={y:,.0f}  vĩ độ={la:.6f}  kinh độ={lo:.6f}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ten")
    ap.add_argument("--diem", nargs=2, type=float, metavar=("X_hoac_VIDO", "Y_hoac_KINHDO"))
    ap.add_argument("--wgs84", action="store_true", help="--diem là vĩ độ, kinh độ WGS84")
    ap.add_argument("--ban-ve")
    ap.add_argument("--tong-hop", action="store_true")
    ap.add_argument("--ban-kinh", type=float, default=500, help="m, liệt kê khu vực gần điểm (mặc định 500)")
    a = ap.parse_args()
    kv = doc()

    if a.ten:
        q = chuan(a.ten)
        hit = [k for k in kv.values() if q in chuan(k["ten_khu_vuc"])]
        for k in hit:
            in_khu(k)
        print(f"-- {len(hit)} khu vực")
    elif a.diem:
        p, q = a.diem
        idx = (3, 4) if a.wgs84 else (1, 2)
        trong, gan = [], []
        for k in kv.values():
            poly = [(d[idx[0]], d[idx[1]]) for d in k["diem_goc"]]
            if trong_da_giac(p, q, poly):
                trong.append(k)
            elif not a.wgs84:
                m = kc_den_canh(p, q, poly)
                if m <= a.ban_kinh:
                    gan.append((m, k))
        print("NẰM TRONG:" if trong else "Không nằm trong khu vực nào.")
        for k in trong:
            in_khu(k, toa_do=False)
        if gan:
            print(f"GẦN (≤ {a.ban_kinh:.0f} m):")
            for m, k in sorted(gan, key=lambda t: t[0]):
                print(f"   cách {m:,.0f} m: ", end="")
                in_khu(k, toa_do=False)
    elif a.ban_ve:
        for k in kv.values():
            if k["ban_ve"].replace("Bản vẽ ", "") == a.ban_ve.replace("Bản vẽ ", ""):
                in_khu(k, toa_do=False)
    else:
        th: "OrderedDict[tuple, list]" = OrderedDict()
        for k in kv.values():
            v = th.setdefault((k["ban_ve"], k["loai_khu_vuc"]), [0, 0])
            v[0] += 1
            v[1] += len(k["diem_goc"])
        for (b, l), (n, m) in th.items():
            print(f"{b} | {l} | {n} khu vực | {m} điểm")
        print(f"Cộng: {len(kv)} khu vực, {sum(len(k['diem_goc']) for k in kv.values())} điểm")


if __name__ == "__main__":
    main()
