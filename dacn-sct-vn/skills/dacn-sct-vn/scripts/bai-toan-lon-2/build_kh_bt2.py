# -*- coding: utf-8 -*-
"""Dựng mới Dự thảo Kế hoạch UBND tỉnh thực hiện Bài toán lớn số 2 (từ đầu, python-docx + VML line)."""
import re, zipfile, shutil, os, copy
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

from noi_dung_bt2 import CAN_CU, THAN, NOI_NHAN, PL1, PL2, PL3

MODE = os.environ.get("MODE", "body")  # body | pl | all
OUT = "/home/claude/work/output/kh_bt2.docx" if MODE != "pl" else "/home/claude/work/output/kh_bt2_phuluc.docx"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

doc = Document()
# ---- Font mặc định
st = doc.styles["Normal"]
st.font.name = "Times New Roman"
st.font.size = Pt(14)
st.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
st.element.rPr.rFonts.set(qn("w:ascii"), "Times New Roman")
st.element.rPr.rFonts.set(qn("w:hAnsi"), "Times New Roman")
st.paragraph_format.space_before = Pt(0)
st.paragraph_format.space_after = Pt(0)

sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21), Cm(29.7)
sec.top_margin = sec.bottom_margin = Cm(2)
sec.left_margin = Cm(3); sec.right_margin = Cm(2)


def _run(p, text, bold=False, italic=False, size=14, sup=False):
    r = p.add_run(text)
    r.font.name = "Times New Roman"; r.font.size = Pt(size)
    r._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    r.font.color.rgb = RGBColor(0, 0, 0)
    r.bold = bold; r.italic = italic
    if sup:
        r.font.superscript = True
    return r


def add_runs(p, text, bold=False, italic=False, size=14):
    """Tách m2/m3 thành superscript thật; hỗ trợ **đậm** và __nghiêng__ nội dòng."""
    # tokens: **..**, __..__
    pos = 0
    for m in re.finditer(r"\*\*(.+?)\*\*|__(.+?)__", text):
        if m.start() > pos:
            _emit(p, text[pos:m.start()], bold, italic, size)
        if m.group(1) is not None:
            _emit(p, m.group(1), True, italic, size)
        else:
            _emit(p, m.group(2), bold, True, size)
        pos = m.end()
    if pos < len(text):
        _emit(p, text[pos:], bold, italic, size)


def _emit(p, text, bold, italic, size):
    parts = re.split(r"(m[23](?!\d))", text)
    for part in parts:
        if not part:
            continue
        if re.fullmatch(r"m[23]", part):
            _run(p, "m", bold, italic, size)
            _run(p, part[1], bold, italic, size, sup=True)
        else:
            _run(p, part, bold, italic, size)


def P(container, text, *, bold=False, italic=False, center=False, left=False,
      size=14, first=Cm(1), before=4, after=4, keep_next=False, indent_left=None):
    """Hàm định dạng đoạn DUY NHẤT — lùi đầu dòng 1cm đồng nhất."""
    p = container.add_paragraph()
    pf = p.paragraph_format
    pf.first_line_indent = first
    if indent_left is not None:
        pf.left_indent = indent_left
    pf.space_before = Pt(before); pf.space_after = Pt(after)
    pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
    if center:
        pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif left:
        pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
    else:
        pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf.keep_with_next = keep_next
    add_runs(p, text, bold=bold, italic=italic, size=size)
    return p


def set_cell_borders_none(table):
    tbl = table._tbl
    tblPr = tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "nil")
        borders.append(el)
    tblPr.append(borders)


def set_table_borders_single(table, sz="4"):
    tblPr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single"); el.set(qn("w:sz"), sz)
        el.set(qn("w:space"), "0"); el.set(qn("w:color"), "000000")
        borders.append(el)
    tblPr.append(borders)


def set_col_widths(table, widths_cm):
    table.autofit = False
    tblPr = table._tbl.tblPr
    layout = OxmlElement("w:tblLayout"); layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    for row in table.rows:
        for i, w in enumerate(widths_cm):
            row.cells[i].width = Cm(w)
    # tblGrid
    grid = table._tbl.tblGrid
    for i, gc in enumerate(grid.findall(qn("w:gridCol"))):
        gc.set(qn("w:w"), str(int(widths_cm[i] * 567)))


def cell_par(cell, text, *, bold=False, italic=False, center=False, size=14,
             first=0, before=0, after=0, clear=False):
    if clear:
        p = cell.paragraphs[0]
        for r in list(p.runs):
            r._element.getparent().remove(r._element)
    else:
        p = cell.add_paragraph()
    pf = p.paragraph_format
    pf.first_line_indent = first
    pf.space_before = Pt(before); pf.space_after = Pt(after)
    pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
    pf.alignment = WD_ALIGN_PARAGRAPH.CENTER if center else WD_ALIGN_PARAGRAPH.LEFT
    add_runs(p, text, bold=bold, italic=italic, size=size)
    return p


def mark_13pt(p):
    for r in p.runs:
        r.font.size = Pt(13)
        rPr = r._element.rPr
        sz = rPr.find(qn("w:sz"))
        if sz is None:
            sz = OxmlElement("w:sz"); rPr.append(sz)
        sz.set(qn("w:val"), "26")
        szcs = rPr.find(qn("w:szCs"))
        if szcs is None:
            szcs = OxmlElement("w:szCs"); rPr.append(szcs)
        szcs.set(qn("w:val"), "26")


# ============================================================ HEADER
if MODE == "pl":
    sec.orientation = WD_ORIENT.LANDSCAPE
    sec.page_width, sec.page_height = Cm(29.7), Cm(21)
    sec.top_margin = Cm(2); sec.bottom_margin = Cm(2); sec.left_margin = Cm(3); sec.right_margin = Cm(2)
hdr = doc.add_table(rows=1, cols=2) if MODE != "pl" else None
if MODE != "pl":
    hdr.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_cell_borders_none(hdr)
    set_col_widths(hdr, [6.0, 10.0])
    c0, c1 = hdr.rows[0].cells
    cell_par(c0, "ỦY BAN NHÂN DÂN", center=True, size=13, clear=True)
    cell_par(c0, "TỈNH LÀO CAI", bold=True, center=True, size=13)
    cell_par(c0, "@@LINE1@@", center=True, size=13)
    p_so = cell_par(c0, "Số:            /KH-UBND", center=True, size=13, before=4)
    mark_13pt(p_so)
    cell_par(c1, "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM", bold=True, center=True, size=13, clear=True)
    cell_par(c1, "Độc lập – Tự do – Hạnh phúc", bold=True, center=True, size=14)
    cell_par(c1, "@@LINE2@@", center=True, size=13)
    p_ngay = cell_par(c1, "Lào Cai, ngày         tháng 9 năm 2026", italic=True, center=True, size=13, before=4)
    mark_13pt(p_ngay)

    P(doc, "DỰ THẢO", bold=True, left=True, first=0, before=6, after=0, size=12)  # theo sửa của Bạn 09/9: căn trái
    P(doc, "KẾ HOẠCH", bold=True, center=True, first=0, before=6, after=0, keep_next=True)
    for i, tl in enumerate(["Thực hiện Bài toán lớn số 2 “Phát triển công nghiệp khai thác và tinh chế",
                            "nguyên liệu phục vụ phát triển công nghệ chiến lược”",
                            "trên địa bàn tỉnh Lào Cai giai đoạn 2026 - 2030"]):
        P(doc, tl, bold=True, center=True, first=0, before=0, after=(6 if i == 2 else 0), keep_next=True)
    P(doc, "", first=0, before=3, after=3)  # dòng trống sau tiêu đề (theo sửa của Bạn 09/9)

    # ============================================================ CĂN CỨ
    for c in CAN_CU:
        P(doc, c, before=3, after=3)

    # ============================================================ THÂN
    for item in THAN:
        kind, text = item[0], item[1]
        if kind == "H1":      # I. MỤC ĐÍCH ... đậm
            P(doc, text, bold=True, keep_next=True)
        elif kind == "H2":    # 1. ... đậm
            P(doc, text, bold=True, keep_next=True)
        elif kind == "H3":    # a) ... nghiêng
            P(doc, text, italic=True, keep_next=True)
        elif kind == "H3B":   # Nhiệm vụ N: đậm nghiêng
            P(doc, text, bold=True, italic=True, keep_next=True)
        elif kind == "NOTE":
            P(doc, text, italic=True)
        else:
            P(doc, text)

    # ============================================================ CHỮ KÝ
    # 2 đoạn cuối thân đi cùng khối ký (Word: keep with next) — tránh khối ký rơi một mình sang trang mới
    P(doc, "", first=0, before=0, after=0)  # đúng 1 dòng trống trước khối ký (Quy tắc 22 vbhc-vn)
    # Nhóm H7/H13: keepNext CHỈ cho đoạn kết + dòng trống (không chuỗi dài → trống nửa trang trong Word)
    for _p in doc.paragraphs[-2:]:
        _p.paragraph_format.keep_with_next = True
    sig = doc.add_table(rows=1, cols=2)
    sig.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_cell_borders_none(sig)
    set_col_widths(sig, [8.0, 8.0])
    s0, s1 = sig.rows[0].cells
    cell_par(s0, "Nơi nhận:", bold=True, italic=True, size=12, clear=True)
    for nn in NOI_NHAN:
        cell_par(s0, nn, size=11)
    cell_par(s1, "TM. ỦY BAN NHÂN DÂN", bold=True, center=True, size=13, clear=True)
    cell_par(s1, "KT. CHỦ TỊCH", bold=True, center=True, size=13)
    cell_par(s1, "PHÓ CHỦ TỊCH", bold=True, center=True, size=13)
    # số dòng trống = số dòng Nơi nhận (kể cả tiêu đề) - 3 dòng chức danh - 1 dòng tên; tối thiểu 3 (Quy tắc 22)
    for _ in range(7):  # 7 dòng trống theo bản Bạn sửa tay 09/9/2026
        cell_par(s1, "", center=True, size=13)
    cell_par(s1, "Giàng Quốc Hưng", bold=True, center=True, size=14)
    # khối ký không gãy trang
    trPr = sig.rows[0]._tr.get_or_add_trPr()
    cs = OxmlElement("w:cantSplit"); trPr.append(cs)
    for _c in (s0, s1):
        for _p in _c.paragraphs[:-1]:
            _p.paragraph_format.keep_with_next = True

# ============================================================ PHỤ LỤC (khổ ngang)
FIRST = [True]
def landscape_section():
    if MODE == "pl" and FIRST[0]:
        FIRST[0] = False
        return doc.sections[0]
    s = doc.add_section(WD_SECTION.NEW_PAGE)
    s.orientation = WD_ORIENT.LANDSCAPE
    s.page_width, s.page_height = Cm(29.7), Cm(21)
    s.top_margin = Cm(2); s.bottom_margin = Cm(2)
    s.left_margin = Cm(3); s.right_margin = Cm(2)
    return s


def make_table(headers, rows, widths, font=11, header_font=11, group_rows=None):
    """rows: list of list[str]; group_rows: set of row idx that are merged group titles."""
    group_rows = group_rows or set()
    t = doc.add_table(rows=1, cols=len(headers))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders_single(t)
    set_col_widths(t, widths)
    # header row repeat
    hr = t.rows[0]
    trPr = hr._tr.get_or_add_trPr()
    th = OxmlElement("w:tblHeader"); th.set(qn("w:val"), "true"); trPr.append(th)
    for i, h in enumerate(headers):
        cell_par(hr.cells[i], h, bold=True, center=True, size=header_font, clear=True, before=2, after=2)
    for ri, row in enumerate(rows):
        r = t.add_row()
        for i, w in enumerate(widths):
            r.cells[i].width = Cm(w)
        if ri in group_rows:
            merged = r.cells[0].merge(r.cells[-1])
            cell_par(merged, row[0], bold=True, size=font, clear=True, before=2, after=2)
            continue
        for i, val in enumerate(row):
            paras = val.split("\n") if val else [""]
            first = True
            for ptxt in paras:
                if first:
                    cell_par(r.cells[i], ptxt, size=font, clear=True, before=1, after=1,
                             center=(i == 0), bold=(i == 0 and ri not in group_rows and False))
                    first = False
                else:
                    cell_par(r.cells[i], ptxt, size=font, before=1, after=1, center=(i == 0))
    return t


def phu_luc(title_lines, sub, headers, rows, widths, font=10.5, group_rows=None, note=None):
    landscape_section()
    for i, tl in enumerate(title_lines):
        P(doc, tl, bold=True, center=True, first=0, before=(6 if i == 0 else 0), after=0)
    P(doc, sub, italic=True, center=True, first=0, before=0, after=8)
    make_table(headers, rows, widths, font=font, header_font=font, group_rows=group_rows)
    if note:
        P(doc, note, italic=True, first=0, before=6, after=0, size=11)


if MODE != "body":
    phu_luc(**PL1)
    phu_luc(**PL2)
    phu_luc(**PL3)

doc.save(OUT)

# ============================================================ VML LINE injection
def inject_lines(path):
    tmp = path + ".tmp"
    zin = zipfile.ZipFile(path)
    zout = zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED)
    for item in zin.infolist():
        data = zin.read(item.filename)
        if item.filename == "word/document.xml":
            s = data.decode("utf-8")
            for i, (tag, width) in enumerate([("@@LINE1@@", "58pt"), ("@@LINE2@@", "160pt")]):
                vml = ('<w:r><w:rPr><w:noProof/></w:rPr><w:pict>'
                       '<v:line xmlns:v="urn:schemas-microsoft-com:vml" '
                       'xmlns:o="urn:schemas-microsoft-com:office:office" id="HeaderRule%d" '
                       'o:spid="_x0000_s10%d" '
                       'style="position:absolute;z-index:25165824%d;mso-position-horizontal:center;'
                       'mso-position-horizontal-relative:margin;mso-position-vertical-relative:line" '
                       'from="0,3pt" to="%s,3pt" o:gfxdata="" strokecolor="black" '
                       'strokeweight=".75pt"/></w:pict></w:r>') % (i + 1, 26 + i, i, width)
                s, n = re.subn(r'<w:r>(?:(?!</w:r>).)*?' + re.escape(tag) + r'.*?</w:r>', vml, s, flags=re.S)
                assert n == 1, (tag, n)
            data = s.encode("utf-8")
        zout.writestr(item, data)
    zout.close(); zin.close()
    shutil.move(tmp, path)


if MODE != "pl":
    inject_lines(OUT)
print("OK", OUT)
