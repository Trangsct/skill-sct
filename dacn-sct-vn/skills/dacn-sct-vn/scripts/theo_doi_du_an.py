#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
theo_doi_du_an.py — Quản lý sổ danh mục dự án công nghiệp động lực tăng trưởng
(Phòng Quản lý Công nghiệp, Sở Công Thương tỉnh Lào Cai).

Phục vụ Nghị quyết 169/NQ-CP: theo dõi dự án, gắn dự án với chỉ tiêu, chấm điểm
ưu tiên, lọc dự án có điểm nghẽn, xuất bảng đưa vào báo cáo.

CÁCH DÙNG
  python3 theo_doi_du_an.py kiem-tra              # kiểm tra tính hợp lệ của sổ
  python3 theo_doi_du_an.py danh-sach             # in toàn bộ
  python3 theo_doi_du_an.py danh-sach --nhom CBCT --trang-thai HD
  python3 theo_doi_du_an.py chi-tieu 3            # dự án tác động tới chỉ tiêu 3
  python3 theo_doi_du_an.py diem-nghen            # dự án đang vướng, xếp theo mức độ
  python3 theo_doi_du_an.py trong-diem            # dự án >= 60 điểm ưu tiên
  python3 theo_doi_du_an.py bang-bao-cao          # bảng dán vào báo cáo (không markdown)
  python3 theo_doi_du_an.py cham-diem CBCT-001    # gợi ý chấm điểm ưu tiên

Tham số chung: --file <đường dẫn danh-muc-du-an.json>

NGUYÊN TẮC BẤT BIẾN
  - Script KHÔNG tự sinh dữ liệu, KHÔNG suy đoán giá trị thiếu.
  - Bản ghi thiếu trường 'nguon' bị đánh dấu KHONG-DU-DIEU-KIEN-BAO-CAO.
"""

import argparse
import json
import os
import sys
from datetime import date

MAC_DINH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "du-lieu", "danh-muc-du-an.json"
)

TEN_NHOM = {
    "HT-KCN": "Hạ tầng khu công nghiệp",
    "HT-CCN": "Hạ tầng cụm công nghiệp",
    "KS": "Khai thác, chế biến khoáng sản",
    "LK-HC": "Luyện kim, hoá chất, phân bón",
    "CBCT": "Chế biến, chế tạo khác",
    "NL": "Nguồn điện, lưới điện, năng lượng",
    "TM": "Hạ tầng thương mại, logistics, cửa khẩu",
}

TEN_TRANG_THAI = {
    "TN": "Tiềm năng",
    "DX": "Đã đề xuất, đang thẩm định",
    "CT": "Đã có chủ trương đầu tư",
    "GPMB": "Đang giải phóng mặt bằng",
    "XD": "Đang xây dựng",
    "HD": "Đang hoạt động",
    "MR": "Đang mở rộng, nâng công suất",
    "TD": "Tạm dừng, dừng hoạt động",
}

TEN_DIEM_NGHEN = {
    "QH": "Quy hoạch",
    "CTDT": "Chủ trương đầu tư, thẩm định",
    "GPMB": "Giải phóng mặt bằng",
    "DD": "Đất đai",
    "XD": "Xây dựng",
    "MT-PCCC": "Môi trường, phòng cháy chữa cháy",
    "TC": "Nghĩa vụ tài chính, vốn, thị trường",
}

# Trạng thái được phép tính vào chỉ tiêu sản lượng (reference 03 mục II)
TRANG_THAI_CO_SAN_LUONG = {"HD", "MR"}


def nap(duong_dan):
    if not os.path.exists(duong_dan):
        sys.exit(f"Không tìm thấy file sổ: {duong_dan}")
    with open(duong_dan, encoding="utf-8") as f:
        return json.load(f)


def kiem_tra(so):
    ds = so.get("du_an", [])
    loi, canh_bao = [], []
    ma_da_dung = set()

    if not ds:
        print("Sổ đang RỖNG. Nạp dữ liệu thật trước khi dùng cho báo cáo.")
        return

    for i, d in enumerate(ds, 1):
        nhan = d.get("ma") or f"[dòng {i}]"
        for truong in ("ma", "ten", "nhom", "trang_thai"):
            if not d.get(truong):
                loi.append(f"{nhan}: thiếu trường bắt buộc '{truong}'")
        if d.get("ma") in ma_da_dung:
            loi.append(f"{nhan}: mã dự án bị trùng")
        ma_da_dung.add(d.get("ma"))

        if d.get("nhom") and d["nhom"] not in TEN_NHOM:
            loi.append(f"{nhan}: nhóm '{d['nhom']}' không hợp lệ")
        if d.get("trang_thai") and d["trang_thai"] not in TEN_TRANG_THAI:
            loi.append(f"{nhan}: trạng thái '{d['trang_thai']}' không hợp lệ")

        nguon = d.get("nguon") or {}
        if not nguon.get("tai_lieu") or not nguon.get("ngay_cap_nhat"):
            loi.append(f"{nhan}: KHONG-DU-DIEU-KIEN-BAO-CAO — thiếu 'nguon.tai_lieu' hoặc 'nguon.ngay_cap_nhat'")

        dg = d.get("dong_gop") or {}
        sl = dg.get("san_luong_ky")
        if sl not in (None, 0) and d.get("trang_thai") not in TRANG_THAI_CO_SAN_LUONG:
            loi.append(
                f"{nhan}: có sản lượng nhưng trạng thái là '{d.get('trang_thai')}' "
                f"— chỉ trạng thái HD/MR mới được tính sản lượng (reference 03 mục II)"
            )
        if d.get("trang_thai") in TRANG_THAI_CO_SAN_LUONG and not dg.get("chi_tieu_tac_dong"):
            canh_bao.append(("Dự án đang hoạt động nhưng chưa gắn chỉ tiêu NQ 169 nào", nhan))

        for dn in d.get("diem_nghen") or []:
            if dn.get("ma_nhom") not in TEN_DIEM_NGHEN:
                loi.append(f"{nhan}: mã nhóm điểm nghẽn '{dn.get('ma_nhom')}' không hợp lệ")
            if not dn.get("tac_dong_chi_tieu"):
                canh_bao.append((
                    "Điểm nghẽn chưa nêu tác động tới chỉ tiêu tăng trưởng "
                    "(báo cáo NQ 169 bắt buộc có — reference 06)",
                    f"{nhan} / {dn.get('ma_nhom')}"))

    print(f"\nKIỂM TRA SỔ DANH MỤC — {len(ds)} bản ghi")
    print(f"Kỳ số liệu: {so.get('_ky_so_lieu') or '[chưa ghi]'}"
          f" | Cập nhật: {so.get('_ngay_cap_nhat') or '[chưa ghi]'}")
    print("=" * 80)

    canh_bao_goc = so.get("_canh_bao_du_lieu_goc") or []
    if canh_bao_goc:
        print(f"\nCẢNH BÁO VỀ DỮ LIỆU GỐC ({len(canh_bao_goc)}) — đọc trước khi dùng:")
        for x in canh_bao_goc:
            print("  ⚠ " + x)

    if loi:
        print(f"\nLỖI ({len(loi)}) — phải sửa:")
        for x in loi[:20]:
            print("  ✗ " + x)
        if len(loi) > 20:
            print(f"  ... và {len(loi)-20} lỗi nữa")

    if canh_bao:
        nhom = {}
        for loai, chi_tiet in canh_bao:
            nhom.setdefault(loai, []).append(chi_tiet)
        print(f"\nCẢNH BÁO ({len(canh_bao)} lượt, {len(nhom)} loại):")
        for loai, ds_ct in sorted(nhom.items(), key=lambda x: -len(x[1])):
            print(f"\n  ! [{len(ds_ct)} lượt] {loai}")
            print(f"    Ví dụ: {', '.join(ds_ct[:5])}"
                  + (f" ... (+{len(ds_ct)-5})" if len(ds_ct) > 5 else ""))

    if not loi and not canh_bao and not canh_bao_goc:
        print("\nKhông phát hiện lỗi.")
    print()


def loc(ds, nhom=None, trang_thai=None, chi_tieu=None, co_diem_nghen=False):
    kq = ds
    if nhom:
        kq = [d for d in kq if d.get("nhom") == nhom]
    if trang_thai:
        kq = [d for d in kq if d.get("trang_thai") == trang_thai]
    if chi_tieu:
        kq = [d for d in kq if chi_tieu in ((d.get("dong_gop") or {}).get("chi_tieu_tac_dong") or [])]
    if co_diem_nghen:
        kq = [d for d in kq if d.get("diem_nghen")]
    return kq


def in_danh_sach(ds, tieu_de):
    print()
    print("=" * 110)
    print(tieu_de)
    print("=" * 110)
    if not ds:
        print("(không có bản ghi phù hợp)")
        print()
        return
    print(f"{'Mã':<12}{'Tên dự án':<46}{'Nhóm':<9}{'Trạng thái':<10}{'Điểm':>6}{'Vướng':>7}")
    print("-" * 110)
    for d in sorted(ds, key=lambda x: -(x.get("diem_uu_tien") or 0)):
        diem = d.get("diem_uu_tien")
        print(
            f"{(d.get('ma') or ''):<12}"
            f"{(d.get('ten') or '')[:45]:<46}"
            f"{(d.get('nhom') or ''):<9}"
            f"{(d.get('trang_thai') or ''):<10}"
            f"{(f'{diem:.0f}' if diem is not None else '—'):>6}"
            f"{len(d.get('diem_nghen') or []):>7}"
        )
    print("-" * 110)
    print(f"Tổng: {len(ds)} dự án")
    print()


def in_diem_nghen(ds):
    co_vuong = [d for d in ds if d.get("diem_nghen")]
    print()
    print("=" * 110)
    print("DỰ ÁN CÓ ĐIỂM NGHẼN — xếp theo số nhóm vướng")
    print("=" * 110)
    if not co_vuong:
        print("(không có)")
        print()
        return
    for d in sorted(co_vuong, key=lambda x: -len(x.get("diem_nghen") or [])):
        print(f"\n[{d.get('ma')}] {d.get('ten')}")
        print(f"    Nhóm: {TEN_NHOM.get(d.get('nhom'), '?')} | "
              f"Trạng thái: {TEN_TRANG_THAI.get(d.get('trang_thai'), '?')}")
        for dn in d["diem_nghen"]:
            print(f"    • {TEN_DIEM_NGHEN.get(dn.get('ma_nhom'), dn.get('ma_nhom'))}: "
                  f"{dn.get('mo_ta') or '[chưa mô tả]'}")
            print(f"      Cơ quan giải quyết: {dn.get('co_quan_giai_quyet') or '[chưa xác định]'} | "
                  f"Hạn: {dn.get('han_xu_ly') or '[chưa có]'}")
            print(f"      Tác động chỉ tiêu: {dn.get('tac_dong_chi_tieu') or '[CHƯA NÊU — bắt buộc phải có]'}")
    print()
    print(f"Tổng: {len(co_vuong)} dự án đang vướng")
    print()


def bang_bao_cao(ds):
    """In bảng dạng văn bản thuần, không ký hiệu markdown, để dán vào báo cáo."""
    print()
    print("BIỂU: DANH MỤC DỰ ÁN CÔNG NGHIỆP ĐỘNG LỰC TĂNG TRƯỞNG")
    print(f"(Số liệu cập nhật đến ngày {date.today().strftime('%d/%m/%Y')} "
          f"— kiểm tra lại trước khi phát hành)")
    print()
    tieu_de = ("TT", "Tên dự án", "Chủ đầu tư", "Địa điểm", "TMĐT (tỷ đ)", "Trạng thái", "Chỉ tiêu tác động")
    print(" | ".join(tieu_de))
    for i, d in enumerate(sorted(ds, key=lambda x: -(x.get("diem_uu_tien") or 0)), 1):
        vt = d.get("vi_tri") or {}
        qm = d.get("quy_mo") or {}
        dg = d.get("dong_gop") or {}
        dia_diem = vt.get("kcn_ccn") or vt.get("xa_phuong") or ""
        tmdt = qm.get("tong_muc_dau_tu_ty_dong")
        print(" | ".join([
            str(i),
            d.get("ten") or "",
            d.get("chu_dau_tu") or "",
            dia_diem,
            (f"{tmdt:,.2f}".replace(",", " ") if tmdt is not None else ""),
            TEN_TRANG_THAI.get(d.get("trang_thai"), ""),
            ", ".join(dg.get("chi_tieu_tac_dong") or []),
        ]))
    print()


def cham_diem(d):
    """In hướng dẫn chấm điểm ưu tiên theo reference 03 mục III."""
    print()
    print(f"CHẤM ĐIỂM ƯU TIÊN — [{d.get('ma')}] {d.get('ten')}")
    print("=" * 80)
    qm = d.get("quy_mo") or {}
    dg = d.get("dong_gop") or {}
    goi_y = []

    dt = dg.get("doanh_thu_ky_ty_dong")
    if dt is not None:
        moc = [(1000, 30), (500, 22), (200, 15), (50, 8), (0, 3)]
        diem = next(d_ for m, d_ in moc if dt >= m)
        goi_y.append(("1. Quy mô đóng góp GTSX", f"{dt:,.0f} tỷ đ/kỳ", diem, 30))
    else:
        goi_y.append(("1. Quy mô đóng góp GTSX", "[thiếu doanh thu]", None, 30))

    ct = dg.get("chi_tieu_tac_dong") or []
    n = len(ct)
    diem2 = 15 if n >= 4 else 11 if n == 3 else 7 if n == 2 else 4 if n == 1 else 0
    goi_y.append(("2. Số chỉ tiêu tác động", f"{n} chỉ tiêu: {', '.join(ct) or '—'}", diem2, 15))

    tt = d.get("trang_thai")
    diem3 = {"HD": 20, "MR": 20, "XD": 10}.get(tt, 4)
    goi_y.append(("3. Tính sẵn sàng", TEN_TRANG_THAI.get(tt, "?"), diem3, 20))

    diem4 = 10 if d.get("nhom") in ("CBCT", "LK-HC") else 6 if d.get("nhom") in ("KS", "NL") else 3
    goi_y.append(("4. Thuộc chế biến, chế tạo", TEN_NHOM.get(d.get("nhom"), "?"), diem4, 10))

    xk = dg.get("kim_ngach_xk_ky_trieu_usd")
    diem5 = 10 if (xk or 0) > 0 else 0
    goi_y.append(("5. Đóng góp xuất khẩu", f"{xk or 0} triệu USD", diem5, 10))

    ld = qm.get("lao_dong_nguoi")
    diem6 = None if ld is None else (5 if ld >= 500 else 3 if ld >= 200 else 1)
    goi_y.append(("6. Lao động", f"{ld if ld is not None else '[thiếu]'} người", diem6, 5))

    nv = len(d.get("diem_nghen") or [])
    diem7 = 0 if tt == "TD" else (10 if nv == 0 else 6 if nv == 1 else 3 if nv <= 3 else 0)
    goi_y.append(("7. Rủi ro tiến độ", f"{nv} nhóm vướng", diem7, 10))

    tong = 0
    thieu = False
    for ten, gia_tri, diem, toi_da in goi_y:
        hien = f"{diem}/{toi_da}" if diem is not None else f"—/{toi_da}"
        print(f"  {ten:<32} {gia_tri:<34} {hien:>8}")
        if diem is None:
            thieu = True
        else:
            tong += diem
    print("-" * 80)
    if thieu:
        print(f"  TỔNG (chưa đủ dữ liệu): {tong}/100 — bổ sung trường thiếu rồi chấm lại")
    else:
        print(f"  TỔNG: {tong}/100 — {'ĐƯA VÀO DANH MỤC TRỌNG ĐIỂM' if tong >= 60 else 'theo dõi thường'}")
    print("\n  Ghi chú: đây là gợi ý máy tính theo reference 03 mục III. Người tham mưu quyết định số cuối.")
    print()


def main():
    p = argparse.ArgumentParser(description="Quản lý danh mục dự án động lực tăng trưởng.")
    p.add_argument("lenh", choices=[
        "kiem-tra", "danh-sach", "chi-tieu", "diem-nghen", "trong-diem", "bang-bao-cao", "cham-diem"
    ])
    p.add_argument("doi_so", nargs="?", help="Mã chỉ tiêu (lệnh chi-tieu) hoặc mã dự án (lệnh cham-diem)")
    p.add_argument("--file", default=MAC_DINH)
    p.add_argument("--nhom", choices=list(TEN_NHOM))
    p.add_argument("--trang-thai", dest="trang_thai", choices=list(TEN_TRANG_THAI))
    a = p.parse_args()

    so = nap(a.file)
    ds = so.get("du_an", [])

    if a.lenh == "kiem-tra":
        kiem_tra(so)
    elif a.lenh == "danh-sach":
        kq = loc(ds, a.nhom, a.trang_thai)
        in_danh_sach(kq, "DANH MỤC DỰ ÁN CÔNG NGHIỆP")
    elif a.lenh == "chi-tieu":
        if not a.doi_so:
            sys.exit("Thiếu mã chỉ tiêu. Ví dụ: theo_doi_du_an.py chi-tieu 3")
        kq = loc(ds, chi_tieu=a.doi_so)
        in_danh_sach(kq, f"DỰ ÁN TÁC ĐỘNG TỚI CHỈ TIÊU {a.doi_so}")
    elif a.lenh == "diem-nghen":
        in_diem_nghen(ds)
    elif a.lenh == "trong-diem":
        kq = [d for d in ds if (d.get("diem_uu_tien") or 0) >= 60]
        in_danh_sach(kq, "DANH MỤC DỰ ÁN TRỌNG ĐIỂM (từ 60 điểm)")
    elif a.lenh == "bang-bao-cao":
        bang_bao_cao(loc(ds, a.nhom, a.trang_thai))
    elif a.lenh == "cham-diem":
        if not a.doi_so:
            sys.exit("Thiếu mã dự án. Ví dụ: theo_doi_du_an.py cham-diem CBCT-001")
        d = next((x for x in ds if x.get("ma") == a.doi_so), None)
        if not d:
            sys.exit(f"Không tìm thấy dự án có mã '{a.doi_so}'")
        cham_diem(d)


if __name__ == "__main__":
    main()
