#!/usr/bin/env python3
"""Xuất mọi sheet của tệp Excel thành bảng Markdown đã ẩn danh — để đưa số liệu nguồn vào plugin (kho CÔNG KHAI).

Dùng cho các biểu Bạn gửi (phụ biểu ngành, danh sách KCN/CCN, thủy điện, mỏ, hạ tầng thương mại...).
  python3 scripts/xuat_bang_an_danh.py <tệp.xlsx> [<tệp2.xlsx> ...] --ra du-lieu/nen-2025/ --nguon "mô tả nguồn"
Tệp .xls cũ: đổi trước bằng `soffice --headless --convert-to xlsx`.

Quy tắc ẩn danh (Bạn chốt 17/10/2026 cho kho công khai: chỉ tên công ty và số giấy phép nhà nước cấp):
  1. Bỏ hẳn cột có tiêu đề: điện thoại, liên hệ, đại diện, email, giấy khám sức khỏe, tập huấn, số người, GĐ VP.
  2. Ô chữ: xóa số điện thoại, email, mã định danh 12 số, cụm "ông/bà/anh/chị + họ tên", "GĐ: họ tên", "HKD họ tên".
  3. Cột tên cơ sở/đơn vị/thương nhân: ô chỉ gồm họ tên người (không có Công ty, HTX, DNTN, Nhà máy...) → "[cá nhân - ẩn danh]";
     họ tên trong ngoặc sau tên công ty → bỏ.
  4. Bỏ dòng, cột trống; ô lỗi công thức (#REF!, #N/A) → để trống.
"""
import argparse
import datetime as dt
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nap_sxkd_stc import sach, slug, nfc  # noqa: E402

import openpyxl  # noqa: E402

COT_BO = re.compile(r"điện\s*thoại|liên\s*hệ|đại\s*đi?ện|giám\s*đốc|^\s*GĐ\b|e-?mail|sức\s*khỏe|\bK\s*SK\b|tập\s*huấn|số\s+người|GĐ\s*VP|NLH", re.I)
COT_TEN = re.compile(r"tên\s*(cơ sở|đơn vị|thương nhân|doanh nghiệp|cửa hàng|ĐKD|nhà đầu tư|chủ)|^đơn vị$|chủ\s*(sở hữu|đầu tư|cơ sở)|thương nhân quản lý", re.I)
TO_CHUC = re.compile(r"công\s*ty|cty|\bct\b|htx|hợp tác|dntn|doanh nghiệp|chi nhánh|nhà máy|xưởng|tổng|ban\b|ubnd|ủy ban|trung tâm|tập đoàn|"
                     r"liên danh|cửa hàng|\bch\b|chxd|petrolimex|đại lý|lâm trường|nông trường|trường|bệnh viện|điện lực|tnhh|cp\b|cổ phần|"
                     r"thủy điện|thuỷ điện|mỏ|kho|siêu thị|chợ|văn phòng|viện|cục|sở\b|quỹ|group|corp|ltd|jsc", re.I)
HO_TEN = re.compile(r"^[A-ZĐÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ][a-zà-ỹđ]*(?:\s+[A-ZĐÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ][a-zà-ỹđ]*){1,4}$")
RE_HKD = re.compile(r"\b(HKD|Hộ kinh doanh|Hộ KD|GĐ|Giám đốc|Chủ hộ|Chủ cơ sở)\s*:?\s+[A-ZĐÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ][\wÀ-ỹ]*(?:\s+[A-ZĐÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ][\wÀ-ỹ]*){1,3}")
HO = ("Nguyễn Trần Lê Phạm Hoàng Huỳnh Phan Vũ Võ Đặng Bùi Đỗ Hồ Ngô Dương Lý Đoàn Đinh Lương Tống Vương Trịnh Đào Mai "
      "Cao Lưu Hà Tạ Nông Lò Lục Ma Giàng Sùng Vàng Thào Hầu Lù Mua Chu Triệu Quách Tô Kiều Phùng Khổng La Lã Lại Đàm Hứa Từ "
      "Thái Nghiêm Âu Khúc Ninh Bạch Doãn Đồng Mạc Tăng Vi Lâm Phí Nhữ Cù Diệp Giáp Hán Lành Sầm Hoàng").split()
DEM = set(("Thị Văn Đức Ngọc Mạnh Quang Minh Hữu Xuân Công Tiến Trọng Kim Hồng Phương Thanh Thu Anh Tuấn Hải Việt Đình Bá Duy "
           "Quốc Như Bích Lan Mai Thúy Thuý Huy Trung Hoàng Gia Chí Khắc Doãn Tất Phúc Vĩnh Sỹ Sĩ Hùng Thế Danh Nhật Bảo Khánh "
           "Tùng Lệ Diệu Thùy Thuỳ Ánh Hương Ngân Seo Trí Thành Long Nam Sơn Hòa Hoà Tài Phú Cường Thái Đăng Diệp Kiều Hạnh "
           "Ngọc Thục Huyền Mỹ Quý Đại Hiền Trường Tú Lệ Tân Thiện Thủy Hữu Khả Hoài Ngô Đắc").split())


def la_ho_ten(s):
    """Ô chỉ là họ tên người Việt: họ phổ biến + tên đệm phổ biến (không phân biệt hoa thường), 3-4 chữ."""
    w = s.split()
    return (3 <= len(w) <= 4 and w[0] in HO and w[1].capitalize() in DEM
            and all(x[:1].isupper() for x in w[2:]) and not re.search(r"công\s*ty|cty|htx|tnhh", s, re.I))


NGOAC_TEN = re.compile(r"\(\s*(?:Nhận chuyển nhượng từ\s+(?:CS|cơ sở)\s+)?[A-ZĐÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ][a-zà-ỹđ]*(?:\s+[A-ZĐÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ][a-zà-ỹđ]*){1,3}\s*\)")


def o(v, la_cot_ten=False):
    if isinstance(v, str) and v.strip().startswith("#") and v.strip().rstrip("!").upper() in ("#REF", "#N/A", "#VALUE", "#DIV/0", "#NAME?"):
        return ""
    if isinstance(v, float):
        return f"{v:.4f}".rstrip("0").rstrip(".") if v != int(v) else str(int(v))
    s = sach(v)
    if s is None:
        return ""
    s = str(s)
    s = RE_HKD.sub(lambda m: m.group(1) + " [ẩn danh]", s)
    if la_cot_ten:
        s = NGOAC_TEN.sub("", s).strip()
        w = s.split()
        if 2 <= len(w) <= 4 and w[0] in HO and all(x[:1].isupper() for x in w) and not TO_CHUC.search(s):
            s = "[cá nhân - ẩn danh]"
    if la_ho_ten(s):
        s = "[cá nhân - ẩn danh]"
    # "CH gas X - Nguyễn Văn A", "Cửa hàng ... (Trần Thị B)"
    s = re.sub(r"(?:-|–|\()\s*((?:%s)\s+(?:%s)(?:\s+[A-ZĐÀÁẠẢÃÂẦẤẬẨẪĂẰẮẶẲẴÈÉẸẺẼÊỀẾỆỂỄÌÍỊỈĨÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠÙÚỤỦŨƯỪỨỰỬỮỲÝỴỶỸ][\wÀ-ỹ]*){1,2})\s*\)?" % ("|".join(HO), "|".join(DEM)),
               " - [ẩn danh]", s)
    return s.replace("|", "/").replace("\n", " ")


def xuat_sheet(ws):
    rows = [list(r) for r in ws.iter_rows(values_only=True)]
    rows = [r for r in rows if any(v not in (None, "") for v in r)]
    if not rows:
        return None
    w = max(len(r) for r in rows)
    rows = [r + [None] * (w - len(r)) for r in rows]
    # tiêu đề cột: gộp chữ 6 dòng đầu theo cột
    tieu_de = [" ".join(nfc(str(r[c])) for r in rows[:6] if isinstance(r[c], str)) for c in range(w)]
    bo = {c for c in range(w) if COT_BO.search(tieu_de[c] or "")}
    ten = {c for c in range(w) if COT_TEN.search(tieu_de[c] or "")}
    # cột chứa họ tên ở dòng dữ liệu nhưng tiêu đề mơ hồ: cột 1-2 có tiêu đề "Tên ..."
    out = [[o(r[c], c in ten) for c in range(w) if c not in bo] for r in rows]
    giu = [j for j in range(len(out[0])) if any(row[j] for row in out)]
    out = [[row[j] for j in giu] for row in out]
    out = [row for row in out if any(row)]
    ten_bo = [re.sub(r"[\d.\s]{6,}", " ", str(sach(tieu_de[c]) or ""))[:30].strip() for c in sorted(bo)]
    return out, sorted(bo), ten_bo


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("xlsx", nargs="+")
    ap.add_argument("--ra", required=True, help="Thư mục ghi tệp .md")
    ap.add_argument("--nguon", required=True, help="Mô tả nguồn ghi đầu mỗi tệp")
    ap.add_argument("--ten", help="Tên tệp ra (chỉ khi một tệp vào)")
    a = ap.parse_args()
    os.makedirs(a.ra, exist_ok=True)
    for f in a.xlsx:
        wb = openpyxl.load_workbook(f, data_only=True)
        goc = nfc(os.path.basename(f))
        ten = a.ten if (a.ten and len(a.xlsx) == 1) else slug(os.path.splitext(goc)[0])[:80] + ".md"
        dong = [f"# {os.path.splitext(goc)[0]}", "",
                f"> Nguồn: {a.nguon}. Tệp gốc: `{goc}`. Máy trích ngày {dt.date.today().strftime('%d/%m/%Y')} bằng "
                "`scripts/xuat_bang_an_danh.py` — đã bỏ cột điện thoại/liên hệ/đại diện và ẩn danh họ tên cá nhân (kho công khai). "
                "Bảng giữ nguyên số và chữ của bản gốc, kể cả lỗi; đọc reference 17 trước khi trích.", ""]
        tong = 0
        for ws in wb.worksheets:
            kq = xuat_sheet(ws)
            if not kq:
                continue
            bang, bo, ten_bo = kq
            tong += len(bang)
            dong += [f"## Sheet: {nfc(ws.title).strip()}  ({len(bang)} dòng)", ""]
            if bo:
                dong += [f"_Đã bỏ cột: {'; '.join(t or '?' for t in ten_bo)}_", ""]
            n = max(len(r) for r in bang)
            dong.append("| " + " | ".join(f"c{j+1}" for j in range(n)) + " |")
            dong.append("|" + "---|" * n)
            for r in bang:
                dong.append("| " + " | ".join(r + [""] * (n - len(r))) + " |")
            dong.append("")
        p = os.path.join(a.ra, ten)
        with open(p, "w", encoding="utf-8") as fo:
            fo.write(unicodedata.normalize("NFC", "\n".join(dong)))
        print(f"{p}: {tong} dòng, {os.path.getsize(p)//1024} KB")


if __name__ == "__main__":
    main()
