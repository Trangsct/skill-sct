#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""chuan_hoa_xuat_ban.py — Chuẩn hóa file .docx TRƯỚC KHI XUẤT (vbhc-vn 2.30.0).

Bạn chốt 13/10/2026 (vụ 3 công văn hoàn thiện hồ sơ vận chuyển HHNH Toàn Phát TQ, An Bình,
Tân Phúc Hưng — trình trên hệ thống quản lý văn bản mới của Sở, PGĐ ký số báo lỗi):

  1. PHÔNG: quét TOÀN BỘ file, mọi khai báo phông phải là Times New Roman — kể cả phần không
     nhìn thấy: kiểu Normal, Header/Footer (số trang), dấu cuối đoạn, docDefaults, phông giao
     diện (theme), bảng phông. Mẫu thật kế thừa từ file cũ của Yên Bái còn ".VnTime" (TCVN3)
     ở kiểu Normal và số trang; hệ thống chuyển Word → PDF để ký số có thể lỗi vì thiếu phông.
  2. NƠI NHẬN: dòng "Nơi nhận:" cỡ 12 (đậm, nghiêng); các dòng "- …" bên dưới cỡ 11
     (NĐ 30/2020). Không để 12.
  3. KHỐI NƠI NHẬN - KÝ cách khối nội dung ĐÚNG MỘT DÒNG trống cỡ 14 — không phải đoạn
     "đệm" 1–7 pt như nhiều mẫu thật cũ (nhìn như dính sát).
  4. --tthc: văn bản giải quyết thủ tục hành chính KHÔNG gửi "Ban Giám đốc Sở", chỉ gửi
     đúng các đơn vị theo quy định.

Cách chạy:
    python3 scripts/chuan_hoa_xuat_ban.py vao.docx                  # sửa tại chỗ
    python3 scripts/chuan_hoa_xuat_ban.py vao.docx -o ra.docx
    python3 scripts/chuan_hoa_xuat_ban.py vao.docx --tthc           # thêm bước 4
    python3 scripts/chuan_hoa_xuat_ban.py vao.docx --chi-phong      # chỉ bước 1

fill_template.TemplateDoc.save() và build_vb.py gọi hàm chuan_hoa_file() sau khi lưu, nên
mọi văn bản dựng từ mẫu đều sạch. File người dùng gửi (Chế độ B) phải chạy lệnh này trước
khi giao, rồi chạy qa_all.py --final (R19–R22 bắt lại nếu còn sót).
"""
from __future__ import annotations

import argparse
import collections
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

PHONG = "Times New Roman"
FULL = (f'<w:rFonts w:ascii="{PHONG}" w:hAnsi="{PHONG}" '
        f'w:eastAsia="{PHONG}" w:cs="{PHONG}"/>')
# Phông ký hiệu (ô vuông, dấu tích…) giữ nguyên — đổi sang Times New Roman sẽ mất ký tự.
PHONG_KY_HIEU = re.compile(r'w:(?:ascii|hAnsi)="(?:Symbol|Wingdings[^"]*|Webdings)"')

PHAN_CHU = re.compile(r"word/(document|styles|header\d*|footer\d*|footnotes|endnotes|numbering)\.xml$")
RFONTS = re.compile(r"<w:rFonts\b[^>]*/>")


def _txt(s: str) -> str:
    return "".join(re.findall(r"<w:t(?:\s[^>]*)?>([^<]*)", s))


def _thay_rfonts(m: re.Match) -> str:
    return m.group(0) if PHONG_KY_HIEU.search(m.group(0)) else FULL


def chuan_hoa_phong_xml(x: str, la_than: bool) -> str:
    """Mọi w:rFonts → Times New Roman đủ 4 thuộc tính; thân văn bản: run/đoạn thiếu rFonts thì thêm."""
    x = RFONTS.sub(_thay_rfonts, x)
    if not la_than:
        return x

    def rpr(m: re.Match) -> str:
        body = m.group(2)
        if "<w:rFonts" in body:
            return m.group(0)
        if body.startswith("<w:rStyle"):
            i = body.index("/>") + 2
            body = body[:i] + FULL + body[i:]
        else:
            body = FULL + body
        return m.group(1) + body + "</w:rPr>"

    x = re.sub(r"(<w:rPr>)(.*?)</w:rPr>", rpr, x, flags=re.S)
    x = x.replace("<w:rPr/>", f"<w:rPr>{FULL}</w:rPr>")
    x = re.sub(r"(<w:r(?:\s[^>]*)?>)(?!<w:rPr)", lambda m: m.group(1) + f"<w:rPr>{FULL}</w:rPr>", x)

    def ppr(m: re.Match) -> str:
        s = m.group(0)
        if "<w:rPr>" in s:
            return s
        # rPr của dấu cuối đoạn đứng trước sectPr/pPrChange nếu có
        for moc in ("<w:sectPr", "<w:pPrChange"):
            if moc in s:
                return s.replace(moc, f"<w:rPr>{FULL}</w:rPr>" + moc, 1)
        return s.replace("</w:pPr>", f"<w:rPr>{FULL}</w:rPr></w:pPr>")

    return re.sub(r"<w:pPr>.*?</w:pPr>", ppr, x, flags=re.S)


def chuan_hoa_theme(x: str) -> str:
    return re.sub(r'(<a:latin) typeface="[^"]*"', rf'\1 typeface="{PHONG}"', x)


def chuan_hoa_font_table(x: str) -> str:
    return re.sub(r'<w:font w:name="(?!Times New Roman"|Symbol"|Wingdings)[^"]*".*?</w:font>', "", x, flags=re.S)


# ───────────────────────── khối Nơi nhận - ký ─────────────────────────

def _bang_ky(x: str) -> tuple[int, int] | None:
    """Vị trí (đầu, cuối) của bảng Nơi nhận - ký: bảng cấp thân đầu tiên có chữ 'Nơi nhận'."""
    for m in re.finditer(r"<w:tbl>.*?</w:tbl>", x, flags=re.S):
        if re.search(r"Nơi\s*nhận", _txt(m.group(0))):
            # bảng lồng: lấy trọn bảng ngoài cùng chứa vị trí này
            return m.start(), m.end()
    return None


def chuan_hoa_noi_nhan(x: str, tthc: bool) -> tuple[str, int, int]:
    vt = _bang_ky(x)
    if vt is None:
        return x, 0, 0
    a, b = vt
    t = x[a:b]
    paras = list(re.finditer(r"<w:p[ >].*?</w:p>", t, flags=re.S))
    da_bo = da_sua = 0
    out = t
    trong_khoi = False
    ds = []
    for m in paras:
        s = _txt(m.group(0)).strip()
        if re.match(r"^Nơi\s*nhận", s):
            trong_khoi = True
            continue
        if trong_khoi and s.startswith("-"):
            ds.append(m)
            if re.match(r"^-?\s*Lưu\s*:", s.lstrip("- ")) or s.lstrip("- ").startswith("Lưu"):
                trong_khoi = False
    for m in reversed(ds):
        s = m.group(0)
        tx = _txt(s).strip()
        if tthc and re.match(r"^-\s*Ban\s+(Giám\s+đốc|GĐ)\s+Sở", tx):
            out = out[:m.start()] + out[m.end():]
            da_bo += 1
            continue
        s2 = re.sub(r'<w:sz w:val="\d+"/>', '<w:sz w:val="22"/>', s)
        s2 = re.sub(r'<w:szCs w:val="\d+"/>', '<w:szCs w:val="22"/>', s2)
        # run/dấu đoạn không có sz thì thêm (cỡ kế thừa kiểu Normal thường là 14)
        s2 = re.sub(r"<w:rPr>(?:(?!</w:rPr>).)*?</w:rPr>",
                    lambda r: r.group(0) if "<w:sz " in r.group(0)
                    else r.group(0).replace("</w:rPr>", '<w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr>'),
                    s2, flags=re.S)
        s2 = s2.replace('<w:vertAlign w:val="subscript"/>', "").replace('<w:vertAlign w:val="superscript"/>', "")
        if s2 != s:
            da_sua += 1
        out = out[:m.start()] + s2 + out[m.end():]
    return x[:a] + out + x[b:], da_bo, da_sua


DONG_TRONG = ('<w:p><w:pPr><w:keepNext/><w:spacing w:before="0" w:after="0" w:line="240" '
              'w:lineRule="auto"/><w:jc w:val="both"/><w:rPr>' + FULL +
              '<w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr></w:pPr></w:p>')


def mot_dong_truoc_khoi_ky(x: str) -> tuple[str, int]:
    """Giữa đoạn có chữ cuối cùng và bảng Nơi nhận - ký: đúng một dòng trống cỡ 14."""
    vt = _bang_ky(x)
    if vt is None:
        return x, 0
    a, _ = vt
    head = x[:a]
    ps = list(re.finditer(r"<w:p[ >].*?</w:p>", head, flags=re.S))
    # chỉ xét đoạn cấp thân (không nằm trong bảng trước đó)
    k = len(ps) - 1
    while k >= 0 and not _txt(ps[k].group(0)).strip() and "<w:drawing" not in ps[k].group(0) \
            and "<w:pict" not in ps[k].group(0) and "<w:sectPr" not in ps[k].group(0):
        k -= 1
    if k < 0:
        return x, 0
    cuoi = ps[k]
    # đoạn trống nằm trong ô bảng (bảng kết thúc ngay trước) thì không đụng
    giua = head[cuoi.end():]
    if "<w:tbl>" in giua or "</w:tbl>" in giua:
        return x, 0
    so_bo = len(ps) - 1 - k
    # khoảng sau của đoạn cuối không lớn hơn mức thường gặp của các đoạn thân
    than = [m.group(0) for m in ps if "<w:ind w:firstLine" in m.group(0) and _txt(m.group(0)).strip()]
    afters = collections.Counter(
        (re.search(r'w:after="(\d+)"', s.split("</w:pPr>")[0]) or [None, "0"])[1] for s in than)
    lp = cuoi.group(0)
    if afters:
        mode = int(afters.most_common(1)[0][0])
        m_af = re.search(r'w:after="(\d+)"', lp.split("</w:pPr>")[0])
        if m_af and int(m_af.group(1)) > mode:
            lp = lp.replace(m_af.group(0), f'w:after="{mode}"', 1)
    return head[:cuoi.start()] + lp + DONG_TRONG + x[a:], so_bo


def chuan_hoa_file(vao: str | Path, ra: str | Path | None = None, tthc: bool = False,
                   chi_phong: bool = False) -> dict:
    vao = Path(vao)
    ra = Path(ra) if ra else vao
    bao_cao = {"phan_sua_phong": 0, "bo_ban_giam_doc": 0, "dong_noi_nhan_11": 0, "doan_trong_thay": 0}
    with zipfile.ZipFile(vao) as z:
        muc = [(i, z.read(i.filename)) for i in z.infolist()]
    moi = []
    for info, data in muc:
        ten = info.filename
        if PHAN_CHU.match(ten) or ten == "word/theme/theme1.xml" or ten == "word/fontTable.xml":
            x = data.decode("utf-8")
            cu = x
            if ten == "word/theme/theme1.xml":
                x = chuan_hoa_theme(x)
            elif ten == "word/fontTable.xml":
                x = chuan_hoa_font_table(x)
            else:
                x = chuan_hoa_phong_xml(x, la_than=not ten.endswith(("styles.xml", "numbering.xml")))
            if x != cu:
                bao_cao["phan_sua_phong"] += 1
            if ten == "word/document.xml" and not chi_phong:
                x, bo, sua = chuan_hoa_noi_nhan(x, tthc)
                x, n = mot_dong_truoc_khoi_ky(x)
                bao_cao.update(bo_ban_giam_doc=bo, dong_noi_nhan_11=sua, doan_trong_thay=n)
            data = x.encode("utf-8")
        moi.append((info, data))
    with tempfile.NamedTemporaryFile(suffix=".docx", delete=False) as tmp:
        tam = Path(tmp.name)
    with zipfile.ZipFile(tam, "w", zipfile.ZIP_DEFLATED) as z:
        for info, data in moi:
            z.writestr(info, data)
    shutil.move(str(tam), str(ra))
    return bao_cao


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docx")
    ap.add_argument("-o", "--ra", help="file kết quả (mặc định: sửa tại chỗ)")
    ap.add_argument("--tthc", action="store_true",
                    help="văn bản giải quyết thủ tục hành chính: bỏ dòng 'Ban Giám đốc Sở' ở Nơi nhận")
    ap.add_argument("--chi-phong", action="store_true", help="chỉ chuẩn hóa phông chữ")
    a = ap.parse_args()
    if not Path(a.docx).exists():
        print(f"LỖI: không thấy {a.docx}", file=sys.stderr)
        return 2
    bc = chuan_hoa_file(a.docx, a.ra, tthc=a.tthc, chi_phong=a.chi_phong)
    print(f"Đã chuẩn hóa {a.ra or a.docx}: phông (số phần XML sửa) {bc['phan_sua_phong']}; "
          f"dòng Nơi nhận về cỡ 11: {bc['dong_noi_nhan_11']}; bỏ 'Ban Giám đốc Sở': {bc['bo_ban_giam_doc']}; "
          f"đoạn trống cũ trước khối ký thay bằng 1 dòng cỡ 14: {bc['doan_trong_thay']}")
    print("→ Chạy tiếp: python3 scripts/qa_all.py <file> --final")
    return 0


if __name__ == "__main__":
    sys.exit(main())
