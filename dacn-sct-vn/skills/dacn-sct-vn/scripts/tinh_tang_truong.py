#!/usr/bin/env python3
"""Tính giá trị sản xuất công nghiệp và tăng trưởng kinh tế tỉnh từ số liệu rà soát SXKD (dacn-sct-vn, reference 17).

Nguồn dữ liệu mặc định: tệp mới nhất trong du-lieu/sxkd-tang-truong/*-stc-*.json (nạp bằng nap_sxkd_stc.py).

Lệnh:
  tong-hop                 Tổng hợp Phụ lục 01, 02 theo khu vực, loại hình; đối chiếu số trong lời văn báo cáo Sở Tài chính
  cong-nghiep [--top N] [--nganh B|C|D|E] [--xa "..."] [--tim "..."]
                           Đơn vị công nghiệp: xếp ngành cấp 1 (B khai khoáng, C CBCT, D điện, E nước - rác), nhóm sản phẩm,
                           9 tháng, QIV, cả năm, tăng thêm; tỷ trọng top N
  do-phu [--lk9 56678]     Độ phủ của danh sách so với GTSXCN 9 tháng của tỉnh; doanh nghiệp Sở theo dõi (CV 10349) VẮNG mặt
  uoc-nam --lk9 X --tang9 G [--q4 Y | --ty-le-q4 R] [--q4-cung-ky Z | --nam-truoc N] [--muc-tieu M] [--ke-hoach K]
                           Ước GTSXCN cả năm và tốc độ tăng; mức quý IV cần đạt để đạt mục tiêu năm
  dong-gop --ty-trong "CN-XD=35.37,NLTS=..,DV=..,THUE=.." --tang "CN-XD=10.67,..."
                           Điểm % đóng góp của từng khu vực vào tăng trưởng GRDP; --muc-tieu-grdp G → tốc độ khu vực CN-XD cần đạt
  quy-doi --gia-tri X [--chi-so-gia P] [--he-so-va H]
                           Giá hiện hành → giá so sánh (chia chỉ số giá); GTSX → giá trị tăng thêm (nhân hệ số VA/GO)
  nen-2025                 Chuỗi GTSXCN, IIP, bán lẻ, xuất khẩu vùng Yên Bái cũ 2020-2025 (số gốc 31/5/2025)

Nguyên tắc (SKILL.md mục VIII): mọi kết quả là ƯỚC CỦA PHÒNG, phải ghi nhãn [ƯỚC] và nguồn đầu vào; số chính thức do
Thống kê tỉnh công bố. Không đưa tham số (chỉ số giá, hệ số VA/GO, tỷ trọng) khi chưa có nguồn — script không tự bịa.
"""
import argparse
import glob
import json
import os
import re
import sys

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DL = os.path.join(GOC, "du-lieu", "sxkd-tang-truong")

# Số trong lời văn Báo cáo Sở Tài chính (cập nhật 26/10/2026) — dùng để tự kiểm khi nạp đúng tệp kỳ đó
LOI_VAN_STC_2026_10_26 = {
    "tong_qiv": 22253.14, "sxkd_qiv": 19060.69, "xd_qiv": 3192.45,
    "cong_nghiep_qiv": 7358.80, "cong_nghiep_dn": 7182.22, "cong_nghiep_htx": 156.57, "cong_nghiep_hkd": 7.13,
    "cong_nghiep_cong_trinh": 12.88, "tang_them": 300.04, "so_don_vi": 940, "so_cong_trinh": 595,
}

NGANH = [  # (mã, tên, mẫu) — thứ tự quan trọng: D, E trước; C trước B
    ("D", "Sản xuất, phân phối điện", r"thủy điện|thuỷ điện|điện năng|điện thương phẩm|phát điện|sản xuất điện|\bđiện\b|năng lượng tái tạo|hơi nước"),
    ("E", "Cấp nước, xử lý rác thải, nước thải", r"cấp nước|nước sạch|rác|môi trường công nghiệp|chất thải|thoát nước"),
    ("C", "Chế biến, chế tạo", r"luyện|tinh luyện|chế biến (chè|quế|gỗ|lâm|đá hoa|nông)|sản xuất (gỗ|ván|tinh bột|thuốc|phân|mỹ phẩm|tôn|bê tông|vật liệu|sản phẩm|kim loại|viên)|"
     r"gỗ|ván|đũa|viên nén|chè|quế|hồi|tinh dầu|may|dệt|sợi|tơ tằm|vàng mã|giấy|linh kiện|đồ chơi|cơ khí|tráng phủ|in ấn|\bin\b|"
     r"phân bón|phân lân|hóa chất|hoá chất|phốt pho|apatit tuyển|xi măng|gạch|bê tông|thép|tôn|kẹo|thực phẩm|măng|miến|nấm|"
     r"đá hoa trắng|chế biến đá|dược|sửa chữa máy|kỹ thuật công nghiệp|plywood|lâm sản|vật liệu xây dựng"),
    ("B", "Khai khoáng", r"khai thác|khai khoáng|khoáng sản|quặng|mỏ|apatit|đá|cát|sỏi|than|thạch anh|đồng tả phời|sin quyền"),
]
NHOM_SP = [  # nhóm sản phẩm chủ yếu để đọc nhanh (không phải phân ngành chính thức)
    ("Đồng, kim loại màu", r"đồng|kim loại quý|kim loại màu|vimico|tả phời"),
    ("Apatit, phân bón, hóa chất", r"apatit|phân|hóa chất|hoá chất|phốt pho|supe"),
    ("Sắt, thép", r"sắt|thép|tôn"),
    ("Thủy điện, điện", r"thủy điện|thuỷ điện|điện"),
    ("Đá, cát, sỏi, VLXD", r"đá|cát|sỏi|gạch|bê tông|xi măng|vật liệu xây dựng|vlxd"),
    ("Gỗ, lâm sản", r"gỗ|ván|đũa|viên nén|lâm sản|plywood|tre"),
    ("Quế, hồi, tinh dầu, dược liệu", r"quế|hồi|tinh dầu|dược"),
    ("Chè", r"chè|trà"),
    ("May, dệt, tơ tằm", r"may|dệt|sợi|tơ"),
    ("Thực phẩm khác", r"kẹo|thực phẩm|măng|miến|tinh bột|sắn|nấm"),
    ("Cơ khí, sửa chữa, in", r"cơ khí|sửa chữa|tráng phủ|in ấn|\bin\b|kỹ thuật"),
    ("Nước, rác", r"nước|rác|môi trường"),
]

# 37 DN công nghiệp UBND tỉnh giao Sở theo dõi (CV 10349/UBND-KT, reference 15) — mẫu nhận diện tên
DN_CV10349 = [
    ("Luyện tuyển đồng Sin Quyền", r"sin quyền"), ("Khoáng sản 3 - VIMICO", r"khoáng sản 3"), ("Khai khoáng Minh Đức", r"khai khoáng minh đức"),
    ("Khai thác và CB kim loại Thủ đô", r"kim loại thủ đô"), ("Đồng Tả Phời", r"tả phời"), ("Apatit Việt Nam", r"apatit việt nam"),
    ("Phân lân nung chảy Lào Cai", r"phân lân nung chảy"), ("Apatit Tam Đỉnh", r"tam đỉnh"), ("Đầu tư Vạn Thắng (công nghiệp)", r"vạn thắng"),
    ("Hóa chất Đức Giang", r"đức giang"), ("Phốt pho Việt Nam", r"phốt pho việt nam"), ("Phốt pho Apatit Việt Nam", r"phốt pho apatit"),
    ("Phốt pho vàng Lào Cai", r"phốt pho vàng"), ("Đông Nam Á Lào Cai", r"đông nam á lào cai"), ("LatViTa", r"latvita"),
    ("Supe lân Apromaco Lào Cai", r"apromaco|su pe lân"), ("DAP số 2 Vinachem", r"dap số 2|dap-vinachem"), ("Xi măng và KS Yên Bái", r"xi măng và khoáng sản yên bái"),
    ("Xi măng Yên Bình", r"xi măng yên bình"), ("Khoáng sản CN Yên Bái", r"ks cn yên bái|khoáng sản công nghiệp yên bái"),
    ("Tủ bếp Cao Tiệp", r"cao tiệp"), ("Ngành gỗ Thiên An", r"thiên an"), ("SX và ĐT Lâm Phong", r"lâm phong"),
    ("Khoáng sản và Luyện kim Việt Trung", r"việt trung"), ("Luyện đồng Lào Cai - VIMICO", r"luyện đồng"), ("ĐTXD và PT Trường Thành", r"đầu tư xây dựng và phát triển trường thành"),
    ("Thủy điện Văn Chấn", r"thuỷ điện văn chấn|thủy điện văn chấn"), ("Thủy điện Thác Bà", r"thủy điện thác bà|thuỷ điện thác bà"), ("Xuân Thiện Yên Bái", r"xuân thiện"),
    ("Sông Đà 9", r"sông đà 9"), ("XD và TM 299 tại Lào Cai", r"299|xây dựng và thương mại 2"), ("Công nghiệp Việt Long", r"việt long"),
    ("ĐT và PT Điện Miền Bắc 2", r"miền bắc 2"), ("Điện Vietraximex", r"vietraximex"), ("Năng lượng Bắc Hà", r"năng lượng bắc hà"),
    ("Thủy điện Bắc Hà", r"thủy điện bắc hà|thuỷ điện bắc hà"), ("Thủy điện Mường Hum", r"mường hum"),
]

NEN_YEN_BAI_2025 = {  # "Phụ lục 01 Tổng hợp kết quả 5 năm 2021-2025" và "Phụ lục 1 các chỉ số" (bộ YB 31/5/2025) — số gốc
    "nguon": "Bộ 'YB cung cấp thông tin 31.5.2025' (Sở Công Thương Yên Bái trước sáp nhập): phụ lục 01 tổng hợp kết quả 2021-2025; phụ lục 1 các chỉ số (kèm dự thảo báo cáo Tỉnh ủy 2025)",
    "gtsxcn_gia_ss_2010_ty": {"2020": 13000, "2021": 14210, "2022": 15540, "2023": 16920, "2024": 18480, "uoc_2025": 21300, "6t_2025": 10050},
    "iip_tang_pct": {"2020": 8.12, "2021": 9.12, "2022": 9.23, "2023": "7 (phụ lục 01) / 6,62 (phụ lục 1)", "2024": 9.23, "uoc_2025": "9,25 (phụ lục 01) / 9,5 (phụ lục 1)", "6t_2025": 10.5},
    "ban_le_ty": {"2021": 21176, "2022": 23815.3, "2023": 25850, "2024": 30105.7, "6t_2025": 16895.5, "uoc_2025": 34500},
    "xuat_khau_trieu_usd": {"2021": 226.3, "2022": 297.3, "2023": 350, "2024": 425.5, "6t_2025": 250.2, "uoc_2025": 520},
    "co_cau_noi_nganh_pct": {"khai_khoang": {"2020": 7.15, "2024": 5.98, "uoc_2025": 5.6}, "che_bien_che_tao": {"2020": 79.45, "2024": 80.5, "uoc_2025": 80.12},
                             "dien": {"2020": 12.8, "2024": 13.23, "uoc_2025": 13.68}, "nuoc_rac": {"2020": 0.6, "2024": 0.64, "uoc_2025": 0.6}},
    "muc_tieu_nq_2025": {"gtsxcn_ty": 20000, "iip_pct": 9, "ban_le_ty": 30000, "xuat_khau_trieu_usd": 500},
}


def tep_moi_nhat(tep=None):
    if tep:
        return tep
    ds = sorted(glob.glob(os.path.join(DL, "*-stc-*.json")))
    if not ds:
        sys.exit("Chưa có tệp du-lieu/sxkd-tang-truong/*-stc-*.json — chạy nap_sxkd_stc.py trước")
    return ds[-1]


def nap(tep=None):
    p = tep_moi_nhat(tep)
    with open(p, encoding="utf-8") as f:
        return json.load(f), p


def xep_nganh(b):
    s = f"{b.get('san_pham') or ''} {b.get('ten') or ''}".lower()
    for ma, ten, mau in NGANH:
        if re.search(mau, s):
            return ma
    return "?"


def nhom_sp(b):
    s = f"{b.get('san_pham') or ''} {b.get('ten') or ''}".lower()
    for ten, mau in NHOM_SP:
        if re.search(mau, s):
            return ten
    return "Khác / chưa ghi sản phẩm"


def la_cn(b):
    return (b.get("khu_vuc") or "").startswith("Công nghiệp")


def f(x, nd=2):
    return "—" if x is None else f"{x:,.{nd}f}".replace(",", "_").replace(".", ",").replace("_", ".")


def cong(ds, k):
    return round(sum(b.get(k) or 0 for b in ds), 2)


def lenh_tong_hop(a):
    d, p = nap(a.tep)
    th = d["tong_hop"]
    print(f"Nguồn: {os.path.basename(p)} — {d['_nguon']['tai_lieu'][:110]}… (chốt {d['_nguon']['ky_chot_so_lieu']})\n")
    p1, p2 = th["phu_luc_01"], th["phu_luc_02"]
    print(f"Phụ lục 01 — {p1['so_don_vi']} đơn vị SXKD: 9 tháng {f(p1['kq_9_thang'])}; QIV {f(p1['uoc_qiv'])}; cả năm {f(p1['uoc_ca_nam'])}; tăng thêm QIV {f(p1['tang_them_qiv'])} tỷ đồng")
    print(f"{'Khu vực':42} {'Số':>4} {'9 tháng':>11} {'QIV':>10} {'Cả năm':>11} {'Tỷ trọng QIV':>13}")
    for k, v in sorted(p1["theo_khu_vuc"].items(), key=lambda x: -x[1]["uoc_qiv"]):
        print(f"{k[:42]:42} {v['so_don_vi']:>4} {f(v['kq_9_thang']):>11} {f(v['uoc_qiv']):>10} {f(v['uoc_ca_nam']):>11} {v['uoc_qiv']/p1['uoc_qiv']*100:>12.1f}%")
        for lh, x in v["theo_loai_hinh"].items():
            print(f"    {lh[:38]:38} {x['so']:>4} {'':>11} {f(x['uoc_qiv']):>10}")
    print(f"\nPhụ lục 02 — {p2['so_cong_trinh']} công trình: QIV {f(p2['tong_qiv'])}; lũy kế năm {f(p2['luy_ke_ca_nam'])}; TMĐT {f(p2['tong_muc_dau_tu'])} tỷ đồng")
    for k, v in p2["theo_phan_loai"].items():
        print(f"    {k:30} {v['so']:>4} công trình, QIV {f(v['tong_qiv'])}")
    for k, v in p2["theo_linh_vuc"].items():
        print(f"    lĩnh vực {k:30} {v['so_cong_trinh']:>4}, QIV {f(v['tong_qiv'])}")
    tong = p1["uoc_qiv"] + p2["tong_qiv"]
    cn = p1["theo_khu_vuc"].get("Công nghiệp - Khai khoáng - Năng lượng", {}).get("uoc_qiv", 0) + p2["theo_linh_vuc"].get("Công nghiệp - Khai khoáng - Năng lượng", {}).get("tong_qiv", 0)
    print(f"\nTổng QIV (SXKD + công trình): {f(tong)} tỷ đồng; khu vực công nghiệp (đơn vị + công trình): {f(cn)} tỷ đồng ({cn/tong*100:.1f}%)")
    if d["_nguon"]["ky_chot_so_lieu"] == "2026-10-26":
        lv = LOI_VAN_STC_2026_10_26
        ok = abs(tong - lv["tong_qiv"]) < 0.05 and abs(cn - lv["cong_nghiep_qiv"]) < 0.05 and p1["so_don_vi"] == lv["so_don_vi"]
        print(("✅ Khớp" if ok else "⚠️ LỆCH") + f" lời văn báo cáo Sở Tài chính: tổng {f(lv['tong_qiv'])}, công nghiệp {f(lv['cong_nghiep_qiv'])}, {lv['so_don_vi']} đơn vị, {lv['so_cong_trinh']} công trình")


def lenh_cong_nghiep(a):
    d, _ = nap(a.tep)
    ds = [dict(b, nganh=xep_nganh(b), nhom=nhom_sp(b)) for b in d["phu_luc_01_don_vi_sxkd"] if la_cn(b)]
    if a.nganh:
        ds = [b for b in ds if b["nganh"] == a.nganh.upper()]
    if a.xa:
        ds = [b for b in ds if a.xa.lower() in (b["xa"] or "").lower()]
    if a.tim:
        ds = [b for b in ds if a.tim.lower() in f"{b['ten']} {b['san_pham'] or ''}".lower()]
    tq = cong(ds, "uoc_qiv") or 1
    print(f"{len(ds)} đơn vị công nghiệp; 9 tháng {f(cong(ds, 'kq_9_thang'))}; QIV {f(cong(ds, 'uoc_qiv'))}; cả năm {f(cong(ds, 'uoc_ca_nam'))}; tăng thêm {f(cong(ds, 'tang_them_qiv'))} tỷ đồng [số xã báo cáo]\n")
    print("Theo ngành cấp 1 (máy xếp theo sản phẩm — cần Thống kê xác nhận):")
    for ma, ten, _ in NGANH + [("?", "Chưa xếp được (thiếu sản phẩm)", "")]:
        g = [b for b in ds if b["nganh"] == ma]
        if g:
            print(f"  {ma} {ten:38} {len(g):>4} đv  9T {f(cong(g, 'kq_9_thang')):>10}  QIV {f(cong(g, 'uoc_qiv')):>9} ({cong(g, 'uoc_qiv')/tq*100:4.1f}%)  năm {f(cong(g, 'uoc_ca_nam')):>10}")
    print("\nTheo nhóm sản phẩm:")
    nhom = {}
    for b in ds:
        nhom.setdefault(b["nhom"], []).append(b)
    for k, g in sorted(nhom.items(), key=lambda x: -cong(x[1], "uoc_qiv")):
        print(f"  {k:34} {len(g):>4} đv  QIV {f(cong(g, 'uoc_qiv')):>9}  năm {f(cong(g, 'uoc_ca_nam')):>10}")
    top = sorted(ds, key=lambda b: -(b["uoc_qiv"] or 0))[: a.top]
    print(f"\nTop {a.top} theo QIV (chiếm {cong(top, 'uoc_qiv')/tq*100:.1f}% QIV công nghiệp của danh sách):")
    for b in top:
        print(f"  {b['stt']:>4} {b['ten'][:52]:52} {b['nganh']} {(b['xa'] or '')[:18]:18} 9T {f(b['kq_9_thang']):>9} QIV {f(b['uoc_qiv']):>8} năm {f(b['uoc_ca_nam']):>9} +{f(b['tang_them_qiv'])}")


def lenh_do_phu(a):
    d, _ = nap(a.tep)
    ds = [b for b in d["phu_luc_01_don_vi_sxkd"] if la_cn(b)]
    lk9 = cong(ds, "kq_9_thang")
    print(f"Danh sách Sở Tài chính: {len(ds)} đơn vị công nghiệp, 9 tháng {f(lk9)} tỷ đồng (doanh thu/giá trị sản xuất giá hiện hành, xã báo cáo)")
    if a.lk9:
        print(f"GTSXCN 9 tháng của tỉnh nhập vào: {f(a.lk9)} tỷ đồng → danh sách phủ khoảng {lk9/a.lk9*100:.1f}% (chỉ để biết độ phủ; hai số khác phương pháp, KHÔNG thay nhau)")
    ten = " ¦ ".join((b["ten"] or "").lower() for b in d["phu_luc_01_don_vi_sxkd"])
    co, vang = [], []
    for nhan, mau in DN_CV10349:
        (co if re.search(mau, ten) else vang).append(nhan)
    print(f"\nDoanh nghiệp công nghiệp Sở theo dõi theo CV 10349/UBND-KT (37): có trong danh sách {len(co)}, VẮNG {len(vang)}")
    print("  VẮNG: " + "; ".join(vang))
    print("\n→ Muốn ước GTSXCN toàn ngành: lấy số 9 tháng của Thống kê tỉnh làm gốc (uoc-nam), dùng danh sách này để ước QIV; "
          "bổ sung số QIV của các DN vắng mặt từ báo cáo DN / Ban QL Khu kinh tế (du-lieu/gtsxcn-kcn-kkt-2027.json) / Ban QL các KCN.")


def lenh_uoc_nam(a):
    d, _ = nap(a.tep)
    ds = [b for b in d["phu_luc_01_don_vi_sxkd"] if la_cn(b) and b["kq_9_thang"] and b["uoc_qiv"] is not None]
    r_mau = cong(ds, "uoc_qiv") / cong(ds, "kq_9_thang")
    co_tt = [b for b in ds if b["tang_them_qiv"] is not None]
    q4_mau, tt_mau = cong(co_tt, "uoc_qiv"), cong(co_tt, "tang_them_qiv")
    g_q4_mau = tt_mau / (q4_mau - tt_mau) if q4_mau - tt_mau else None
    lk9, g9 = a.lk9, a.tang9 / 100
    lk9_ck = lk9 / (1 + g9)
    if a.q4 is not None:
        q4, nguon_q4 = a.q4, "nhập trực tiếp"
    else:
        r = a.ty_le_q4 if a.ty_le_q4 is not None else r_mau
        q4, nguon_q4 = lk9 * r, f"tỷ lệ QIV/9 tháng = {r:.4f}" + (" (mẫu đơn vị công nghiệp Sở Tài chính)" if a.ty_le_q4 is None else "")
    if a.q4_cung_ky is not None:
        q4_ck, nguon_ck = a.q4_cung_ky, "nhập trực tiếp"
    elif a.nam_truoc is not None:
        q4_ck, nguon_ck = a.nam_truoc - lk9_ck, f"cả năm 2025 {f(a.nam_truoc)} − 9 tháng 2025"
    else:
        q4_ck, nguon_ck = q4 / (1 + g9), "GIẢ ĐỊNH QIV/2025 tăng cùng nhịp 9 tháng — thiếu số thật, nhập --q4-cung-ky hoặc --nam-truoc"
        if g_q4_mau is not None:
            print(f"  (tham khảo: {len(co_tt)} đơn vị có cột tăng thêm cho QIV tăng {g_q4_mau*100:.2f}% so cùng kỳ — mẫu nhỏ, lệch về dự án mới, KHÔNG dùng làm tốc độ chung)")
    nam, nam_ck = lk9 + q4, lk9_ck + q4_ck
    g = nam / nam_ck - 1
    print("[ƯỚC CỦA PHÒNG — không phải số Thống kê công bố]")
    print(f"  9 tháng: {f(lk9)} tỷ (+{a.tang9:.2f}%) → cùng kỳ 2025 ≈ {f(lk9_ck)} tỷ")
    print(f"  QIV/2026 ước: {f(q4)} tỷ ({nguon_q4})")
    print(f"  QIV/2025: {f(q4_ck)} tỷ ({nguon_ck})")
    print(f"  Cả năm 2026 ước: {f(nam)} tỷ; cả năm 2025 ≈ {f(nam_ck)} tỷ → tăng {g*100:.2f}%")
    if a.muc_tieu is not None:
        can = (1 + a.muc_tieu / 100) * nam_ck - lk9
        print(f"  Để cả năm tăng {a.muc_tieu}%: QIV phải đạt {f(can)} tỷ (tăng {(can/q4_ck-1)*100:.2f}% so QIV/2025; "
              f"{'thiếu' if can > q4 else 'dư'} {f(abs(can - q4))} tỷ so mức ước)")
    if a.ke_hoach:
        print(f"  So kế hoạch năm {f(a.ke_hoach)} tỷ: đạt {nam/a.ke_hoach*100:.1f}%")
    print("  Lưu ý: GTSX giá hiện hành tăng ≠ IIP tăng; muốn ra tốc độ thực phải chia chỉ số giá (lệnh quy-doi) hoặc dùng IIP của Thống kê.")


def doc_cap(s):
    out = {}
    for x in (s or "").split(","):
        if "=" in x:
            k, v = x.split("=", 1)
            out[k.strip()] = float(v.replace(" ", ""))
    return out


def lenh_dong_gop(a):
    w, g = doc_cap(a.ty_trong), doc_cap(a.tang)
    tw = sum(w.values())
    if abs(tw - 100) > 0.6:
        print(f"⚠️ Tổng tỷ trọng = {tw:.2f}% (không bằng 100) — kiểm lại đầu vào")
    tong = 0
    print("Điểm % đóng góp = tỷ trọng kỳ gốc (giá so sánh) × tốc độ tăng khu vực / 100")
    for k, v in w.items():
        dg = v * g.get(k, 0) / 100
        tong += dg
        print(f"  {k:8} tỷ trọng {v:6.2f}%  tăng {g.get(k, 0):6.2f}%  → đóng góp {dg:5.2f} điểm %")
    print(f"  GRDP tăng ≈ {tong:.2f}% [ƯỚC — Thống kê tỉnh tính chính thức]")
    if a.muc_tieu_grdp is not None and a.khu_vuc in w:
        khac = sum(w[k] * g.get(k, 0) / 100 for k in w if k != a.khu_vuc)
        can = (a.muc_tieu_grdp - khac) / w[a.khu_vuc] * 100
        print(f"  Để GRDP tăng {a.muc_tieu_grdp}%: khu vực {a.khu_vuc} phải tăng {can:.2f}% (các khu vực khác giữ như nhập)")


def lenh_quy_doi(a):
    x = a.gia_tri
    if a.chi_so_gia:
        print(f"Giá so sánh = {f(x)} / ({a.chi_so_gia}/100) = {f(x / (a.chi_so_gia / 100))} tỷ đồng")
    if a.he_so_va:
        print(f"Giá trị tăng thêm = {f(x)} × {a.he_so_va} = {f(x * a.he_so_va)} tỷ đồng")
    if not (a.chi_so_gia or a.he_so_va):
        print("Cần --chi-so-gia (chỉ số giá sản xuất công nghiệp, %, Thống kê) hoặc --he-so-va (tỷ lệ VA/GO ngành, Thống kê). Script không tự giả định.")


def lenh_nen_2025(a):
    n = NEN_YEN_BAI_2025
    print("Vùng YÊN BÁI CŨ — " + n["nguon"])
    for k, nhan in (("gtsxcn_gia_ss_2010_ty", "GTSXCN giá SS 2010 (tỷ)"), ("iip_tang_pct", "IIP tăng (%)"), ("ban_le_ty", "Bán lẻ + DV tiêu dùng (tỷ)"), ("xuat_khau_trieu_usd", "Xuất khẩu (triệu USD)")):
        print(f"  {nhan:28} " + "; ".join(f"{y}: {v}" for y, v in n[k].items()))
    s = n["gtsxcn_gia_ss_2010_ty"]
    cagr = (s["uoc_2025"] / s["2020"]) ** (1 / 5) - 1
    print(f"  → GTSXCN 2020→ước 2025 tăng bình quân {cagr*100:.2f}%/năm (giá SS 2010); mục tiêu NQ 2025: {n['muc_tieu_nq_2025']}")
    print("  Cơ cấu nội ngành (%): " + "; ".join(f"{k} {v}" for k, v in n["co_cau_noi_nganh_pct"].items()))
    print("  Vùng LÀO CAI CŨ 2025: xem du-lieu/nen-2025/lao-cai-phu-bieu-06-2025/ (KCN, CCN, thủy điện, khoáng sản, hạ tầng thương mại).")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tep", help="Tệp JSON SXKD (mặc định: mới nhất)")
    sp = ap.add_subparsers(dest="lenh", required=True)
    sp.add_parser("tong-hop")
    x = sp.add_parser("cong-nghiep")
    x.add_argument("--top", type=int, default=15)
    x.add_argument("--nganh")
    x.add_argument("--xa")
    x.add_argument("--tim")
    x = sp.add_parser("do-phu")
    x.add_argument("--lk9", type=float)
    x = sp.add_parser("uoc-nam")
    x.add_argument("--lk9", type=float, required=True, help="GTSXCN 9 tháng của tỉnh (tỷ đồng)")
    x.add_argument("--tang9", type=float, required=True, help="Tốc độ tăng 9 tháng so cùng kỳ (%%)")
    x.add_argument("--q4", type=float)
    x.add_argument("--ty-le-q4", type=float)
    x.add_argument("--q4-cung-ky", type=float, help="GTSXCN quý IV/2025 (tỷ đồng, cùng loại giá)")
    x.add_argument("--nam-truoc", type=float, help="GTSXCN cả năm 2025 (tỷ đồng, cùng loại giá)")
    x.add_argument("--muc-tieu", type=float, help="Tốc độ tăng cả năm cần đạt (%%)")
    x.add_argument("--ke-hoach", type=float, help="Kế hoạch GTSXCN năm (tỷ đồng)")
    x = sp.add_parser("dong-gop")
    x.add_argument("--ty-trong", required=True)
    x.add_argument("--tang", required=True)
    x.add_argument("--muc-tieu-grdp", type=float)
    x.add_argument("--khu-vuc", default="CN-XD")
    x = sp.add_parser("quy-doi")
    x.add_argument("--gia-tri", type=float, required=True)
    x.add_argument("--chi-so-gia", type=float)
    x.add_argument("--he-so-va", type=float)
    sp.add_parser("nen-2025")
    a = ap.parse_args()
    {"tong-hop": lenh_tong_hop, "cong-nghiep": lenh_cong_nghiep, "do-phu": lenh_do_phu, "uoc-nam": lenh_uoc_nam,
     "dong-gop": lenh_dong_gop, "quy-doi": lenh_quy_doi, "nen-2025": lenh_nen_2025}[a.lenh](a)


if __name__ == "__main__":
    main()
