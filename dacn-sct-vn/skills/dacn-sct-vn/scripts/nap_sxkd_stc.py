#!/usr/bin/env python3
"""Nạp Phụ lục tổng hợp rà soát SXKD, đầu tư, xây dựng của Sở Tài chính vào plugin dacn-sct-vn.

Nguồn: tệp Excel "Phụ lục tổng hợp tình hình SXKD năm 2026" kèm Báo cáo của Sở Tài chính gửi UBND tỉnh
(rà soát theo Văn bản 10210/UBND-TH ngày 07/10/2026). Ba sheet:
  - Phụ lục 01: doanh nghiệp, HTX, hộ SXKD (9 tháng, T10-T12, QIV, cả năm, tăng thêm QIV so cùng kỳ)
  - Phụ lục 02: công trình, dự án xây dựng và đầu tư QIV
  - Phụ lục 03: doanh nghiệp, dự án trọng điểm cần theo dõi, tháo gỡ

Kho skill-sct CÔNG KHAI → script tự ẩn danh:
  - Hộ kinh doanh cá thể, tổ đội thi công: bỏ tên chủ hộ, mã số thuế/mã định danh, địa điểm chi tiết;
    chỉ giữ xã/phường, lĩnh vực, sản phẩm, số liệu.
  - Mọi ô chữ: xóa số điện thoại, email, cụm "ông/bà + họ tên".

Dùng:
  python3 scripts/nap_sxkd_stc.py <tệp.xlsx> --ky "2026-10-26" --ra du-lieu/sxkd-tang-truong/2026-10-26-stc-quy-iv.json
Không có --ra thì chỉ in tóm tắt (để soát trước khi ghi).
"""
import argparse
import datetime as dt
import json
import re
import sys
import unicodedata

try:
    import openpyxl
except ImportError:  # pragma: no cover
    sys.exit("Thiếu openpyxl: pip install openpyxl")

RE_PHONE = re.compile(r"(?<!\d)(?:\+?84|0)(?:[\s.\-]?\d){8,10}(?!\d)")
RE_CCCD = re.compile(r"(?<!\d)\d{12}(?!\d)")
RE_EMAIL = re.compile(r"[\w.+\-]+@[\w\-]+(?:\.[\w\-]+)+")
RE_ONGBA = re.compile(r"\b(?:[Ôô]ng|[Bb]à|[Aa]nh|[Cc]hị)\s*:?\s+(?:[A-ZĐÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ][\wÀ-ỹ]*)(?:\s+[A-ZĐÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ][\wÀ-ỹ]*){1,3}")
RE_THAN = re.compile(r"\b(?:vợ|chồng|con|cháu)(?:\s+là)?\s+(?:[A-ZĐÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ][\wÀ-ỹ]*)(?:\s+[A-ZĐÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ][\wÀ-ỹ]*){1,3}")
RE_DS_HO = re.compile(r"(hộ[^:;+]{0,90}:)\s*([^;+]+)")
TEN_RIENG = r"[A-ZĐÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ][\wÀ-ỹ]*(?:\s+[A-ZĐÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ][\wÀ-ỹ]*){0,3}"
RE_CHI_TEN = re.compile(rf"^\s*{TEN_RIENG}(?:\s*(?:,|và)\s*{TEN_RIENG})*\s*(?:-.*)?$")
CA_NHAN = ("Hộ kinh doanh cá thể", "Tổ đội thi công")


def _an_ds_ho(m):
    """'03 hộ ...: Thào A, Thào B' → '03 hộ ...: [ẩn danh]' khi phần sau dấu hai chấm chỉ là danh sách tên."""
    sau = m.group(2)
    if RE_CHI_TEN.match(sau):
        duoi = sau[sau.index(" -"):] if " -" in sau else ""
        return f"{m.group(1)} [ẩn danh]{duoi} "
    return m.group(0)


def nfc(s):
    return unicodedata.normalize("NFC", s) if isinstance(s, str) else s


def sach_mst(s):
    """Mã số thuế: giữ nguyên (10 số hoặc 10 số + '-xxx'); 12 số là mã định danh cá nhân → bỏ."""
    if s is None:
        return None
    s = re.sub(r"\s+", "", nfc(str(s)))
    return None if re.fullmatch(r"\d{12}", s) else (s or None)


def sach(s):
    """Chuẩn hóa ô chữ và xóa thông tin cá nhân."""
    if s is None:
        return None
    if isinstance(s, (int, float)):
        return s
    if isinstance(s, (dt.datetime, dt.date)):
        return s.strftime("%d/%m/%Y")
    s = nfc(str(s)).strip()
    s = RE_EMAIL.sub("[đã xóa email]", s)
    s = RE_CCCD.sub("[đã xóa mã định danh 12 số]", s)
    s = RE_PHONE.sub("[đã xóa số điện thoại]", s)
    s = RE_ONGBA.sub("[ẩn danh]", s)
    s = RE_THAN.sub("[ẩn danh]", s)
    s = RE_DS_HO.sub(_an_ds_ho, s)
    s = re.sub(r"\s+", " ", s)
    return s or None


def so(v):
    """Ô số → float; ô chữ kiểu '8.350,7' hoặc '40.680' giữ nguyên dạng chữ ở trường _goc."""
    if v is None or v == "":
        return None
    if isinstance(v, (int, float)):
        return round(float(v), 4)
    return None


def slug(s):
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(c for c in s if unicodedata.category(c) != "Mn").replace("đ", "d").replace("Đ", "D")
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def tim_dong_tieu_de(ws, chu):
    for i, r in enumerate(ws.iter_rows(min_row=1, max_row=10, values_only=True), start=1):
        if r and r[0] == "STT" and any(chu in str(c or "") for c in r):
            return i
    raise SystemExit(f"Không thấy dòng tiêu đề chứa '{chu}' trong sheet {ws.title}")


def doc_pl01(ws):
    h = tim_dong_tieu_de(ws, "Tên DN/HTX")
    ds, dem_an = [], {}
    for r in ws.iter_rows(min_row=h + 2, values_only=True):
        if not r or not isinstance(r[0], (int, float)):
            continue
        loai = sach(r[6])
        xa = sach(r[1])
        ban_ghi = {
            "stt": int(r[0]),
            "xa": xa,
            "ten": sach(r[2]),
            "mst": sach_mst(r[3]),
            "dia_diem": sach(r[4]),
            "khu_vuc": sach(r[5]),
            "loai_hinh": loai,
            "san_pham": sach(r[7]),
            "dvt": sach(r[8]),
            "kq_9_thang": so(r[9]),
            "uoc_t10": so(r[10]),
            "uoc_t11": so(r[11]),
            "uoc_t12": so(r[12]),
            "uoc_qiv": so(r[13]),
            "uoc_ca_nam": so(r[14]),
            "tang_them_qiv": so(r[15]),
            "kho_khan": sach(r[16]),
            "minh_chung": sach(r[17]),
            "doi_chieu_nguong": sach(r[18]),
            "ghi_chu": sach(r[19]),
            "tinh_vao_tong_hop": sach(r[20]),
        }
        if loai in CA_NHAN:
            goc = nfc(str(r[2] or "")).strip()
            for t in ("ghi_chu", "kho_khan", "minh_chung", "san_pham"):
                if goc and ban_ghi[t]:
                    ban_ghi[t] = ban_ghi[t].replace(goc, "[ẩn danh]")
                if ban_ghi[t]:
                    ban_ghi[t] = re.sub(rf"'{TEN_RIENG}'", "'[ẩn danh]'", ban_ghi[t])
            k = slug(xa)
            dem_an[k] = dem_an.get(k, 0) + 1
            ban_ghi["ten"] = f"{loai} (ẩn danh) {k}-{dem_an[k]:02d}"
            ban_ghi["mst"] = None
            ban_ghi["dia_diem"] = None
            ban_ghi["_an_danh"] = True
        ds.append(ban_ghi)
    return ds


def doc_pl02(ws):
    h = tim_dong_tieu_de(ws, "Tên công trình")
    ds = []
    for r in ws.iter_rows(min_row=h + 2, values_only=True):
        if not r or not isinstance(r[0], (int, float)):
            continue
        b = {
            "stt": int(r[0]), "xa": sach(r[1]), "ten": sach(r[2]), "chu_dau_tu": sach(r[3]),
            "nha_thau": sach(r[4]), "phan_loai": sach(r[5]), "tong_muc_dau_tu": so(r[6]),
            "th_den_30_9": so(r[7]), "t10": so(r[8]), "t11": so(r[9]), "t12": so(r[10]),
            "tong_qiv": so(r[11]), "luy_ke_ca_nam": so(r[12]), "nghiem_thu_thanh_toan": so(r[13]),
            "tien_do": sach(r[14]), "minh_chung": sach(r[15]), "vuong_mac": sach(r[16]),
            "dvt": sach(r[17]), "linh_vuc": sach(r[18]), "doi_chieu_nguong": sach(r[19]),
            "ghi_chu": sach(r[20]), "tinh_vao_tong_hop": sach(r[21]) if len(r) > 21 else None,
        }
        if b["phan_loai"] == "Nhà ở-dân cư":
            b["chu_dau_tu"] = "Cá nhân, hộ gia đình (ẩn danh)"
        ds.append(b)
    return ds


def doc_pl03(ws):
    h = tim_dong_tieu_de(ws, "Doanh nghiệp/Dự án")
    ds = []
    for r in ws.iter_rows(min_row=h + 1, values_only=True):
        if not r or not isinstance(r[0], (int, float)):
            continue
        ds.append({
            "stt": int(r[0]), "xa": sach(r[1]), "ten": sach(r[2]), "khu_vuc": sach(r[3]),
            "kha_nang_tao_them_qiv_ty": so(r[4]), "muc_tieu_qiv": sach(r[5]), "vuong_mac": sach(r[6]),
            "co_quan_xu_ly": sach(r[7]), "thoi_han": sach(r[8]), "ket_qua_kien_nghi": sach(r[9]),
            "nguyen_van": sach(r[10]),
        })
    return ds


def cong(ds, truong, loc=lambda b: True):
    return round(sum((b.get(truong) or 0) for b in ds if loc(b)), 2)


def tong_hop(pl01, pl02):
    kv = {}
    for b in pl01:
        k = b["khu_vuc"] or "(trống)"
        x = kv.setdefault(k, {"so_don_vi": 0, "theo_loai_hinh": {}, "kq_9_thang": 0, "uoc_qiv": 0, "uoc_ca_nam": 0,
                              "tang_them_qiv": 0, "so_don_vi_co_tang_them": 0})
        x["so_don_vi"] += 1
        lh = x["theo_loai_hinh"].setdefault(b["loai_hinh"] or "(trống)", {"so": 0, "uoc_qiv": 0})
        lh["so"] += 1
        lh["uoc_qiv"] = round(lh["uoc_qiv"] + (b["uoc_qiv"] or 0), 2)
        for t in ("kq_9_thang", "uoc_qiv", "uoc_ca_nam", "tang_them_qiv"):
            x[t] = round(x[t] + (b[t] or 0), 2)
        if b["tang_them_qiv"] not in (None, 0):
            x["so_don_vi_co_tang_them"] += 1
    xd = {}
    for b in pl02:
        k = b["linh_vuc"] or "(trống)"
        x = xd.setdefault(k, {"so_cong_trinh": 0, "tong_qiv": 0, "luy_ke_ca_nam": 0, "tong_muc_dau_tu": 0})
        x["so_cong_trinh"] += 1
        for t in ("tong_qiv", "luy_ke_ca_nam", "tong_muc_dau_tu"):
            x[t] = round(x[t] + (b[t] or 0), 2)
    return {
        "phu_luc_01": {"so_don_vi": len(pl01), "kq_9_thang": cong(pl01, "kq_9_thang"), "uoc_qiv": cong(pl01, "uoc_qiv"),
                       "uoc_ca_nam": cong(pl01, "uoc_ca_nam"), "tang_them_qiv": cong(pl01, "tang_them_qiv"),
                       "theo_khu_vuc": kv},
        "phu_luc_02": {"so_cong_trinh": len(pl02), "tong_qiv": cong(pl02, "tong_qiv"),
                       "luy_ke_ca_nam": cong(pl02, "luy_ke_ca_nam"), "tong_muc_dau_tu": cong(pl02, "tong_muc_dau_tu"),
                       "theo_phan_loai": {p: {"so": sum(1 for b in pl02 if b["phan_loai"] == p),
                                              "tong_qiv": cong(pl02, "tong_qiv", lambda b, p=p: b["phan_loai"] == p)}
                                          for p in sorted({b["phan_loai"] or "(trống)" for b in pl02})},
                       "theo_linh_vuc": xd},
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("xlsx")
    ap.add_argument("--ky", required=True, help="Ngày chốt số liệu của Sở Tài chính, dạng YYYY-MM-DD")
    ap.add_argument("--van-ban", default="Báo cáo của Sở Tài chính gửi UBND tỉnh (bản chưa có số), kết quả tổng hợp rà soát tình hình SXKD, đầu tư, xây dựng phục vụ đánh giá tăng trưởng quý IV và cả năm 2026")
    ap.add_argument("--ra", help="Tệp JSON ghi ra")
    a = ap.parse_args()

    wb = openpyxl.load_workbook(a.xlsx, data_only=True, read_only=True)
    ten = {nfc(ws.title).strip(): ws for ws in wb.worksheets}
    pl01 = doc_pl01(ten["Phụ lục 01"])
    pl02 = doc_pl02(ten["Phụ lục 02"])
    pl03 = doc_pl03(ten["Phụ lục 03"]) if "Phụ lục 03" in ten else []
    th = tong_hop(pl01, pl02)
    out = {
        "_nguon": {
            "tai_lieu": a.van_ban,
            "can_cu": "Văn bản 10210/UBND-TH ngày 07/10/2026 của UBND tỉnh về rà soát, tổng hợp tình hình SXKD, đầu tư, xây dựng phục vụ đánh giá tăng trưởng quý IV và cả năm 2026",
            "ky_chot_so_lieu": a.ky,
            "don_vi": "tỷ đồng (Sở Tài chính đã quy đổi thống nhất)",
            "tep_goc": a.xlsx.split("/")[-1],
            "nap_ngay": dt.date.today().isoformat(),
        },
        "_canh_bao": [
            "Số ƯỚC do xã, phường, chủ đầu tư báo cáo, Sở Tài chính tổng hợp — số ĐỘNG; Sở Tài chính đề nghị xã cập nhật trước ngày 15 hằng tháng → nạp kỳ mới bằng chính script này, không sửa tay.",
            "Giá trị của đơn vị SXKD là DOANH THU hoặc GIÁ TRỊ SẢN XUẤT theo giá hiện hành, xã báo cáo lẫn lộn; KHÔNG phải GTSXCN giá so sánh 2010 của Thống kê. Muốn tính tăng trưởng phải quy đổi (scripts/tinh_tang_truong.py, reference 17).",
            "Phạm vi là các đơn vị đạt ngưỡng CV 10210 (Công nghiệp: QIV ≥ 5 tỷ hoặc tăng thêm ≥ 2 tỷ) cộng một số đơn vị dưới ngưỡng xã bổ sung — KHÔNG phải toàn bộ doanh nghiệp công nghiệp của tỉnh.",
            "Cột 'Tăng thêm QIV so cùng kỳ' chỉ có ở 86 đơn vị; đơn vị trống KHÔNG có nghĩa là tăng thêm bằng 0.",
            "Hộ kinh doanh cá thể, tổ đội thi công đã ẩn danh (kho công khai). Tên doanh nghiệp, HTX, mã số thuế giữ nguyên như bản gốc.",
            "Một số đơn vị được xếp lại lĩnh vực (chế biến chè, nấm...) — đọc trường ghi_chu. Thủy điện Văn Chấn ghi ở xã Văn Chấn nhưng nhà máy ở xã Sơn Lương — có thể trùng.",
        ],
        "tong_hop": th,
        "phu_luc_01_don_vi_sxkd": pl01,
        "phu_luc_02_cong_trinh_du_an": pl02,
        "phu_luc_03_trong_diem": pl03,
    }
    p1 = th["phu_luc_01"]
    print(f"PL01: {p1['so_don_vi']} đơn vị; 9T {p1['kq_9_thang']:,.2f}; QIV {p1['uoc_qiv']:,.2f}; cả năm {p1['uoc_ca_nam']:,.2f}; tăng thêm {p1['tang_them_qiv']:,.2f} tỷ")
    for k, v in p1["theo_khu_vuc"].items():
        print(f"   {k}: {v['so_don_vi']} đơn vị, QIV {v['uoc_qiv']:,.2f}, cả năm {v['uoc_ca_nam']:,.2f}")
    p2 = th["phu_luc_02"]
    print(f"PL02: {p2['so_cong_trinh']} công trình; QIV {p2['tong_qiv']:,.2f}; lũy kế năm {p2['luy_ke_ca_nam']:,.2f} tỷ")
    print(f"PL03: {len(pl03)} dòng trọng điểm; ẩn danh {sum(1 for b in pl01 if b.get('_an_danh'))} hộ/tổ đội")
    if a.ra:
        with open(a.ra, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=1)
            f.write("\n")
        print("Đã ghi", a.ra)


if __name__ == "__main__":
    main()
