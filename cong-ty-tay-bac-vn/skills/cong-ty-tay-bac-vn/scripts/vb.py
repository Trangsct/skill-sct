"""Thư viện dựng văn bản hành chính (thể thức NĐ 30/2020) cho hồ sơ lớp tập huấn."""
import re, copy
import docx
from docx.shared import Pt, Cm, Mm, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import parse_xml, OxmlElement

PURPLE = '7030A0'
W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
_line_id = [100]


def new_doc(landscape=False, page=None, margins=(20, 20, 30, 20)):
    d = docx.Document()
    st = d.styles['Normal']
    st.font.name = 'Times New Roman'
    st.font.size = Pt(14)
    rpr = st.element.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    for a in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'):
        rf.set(qn(a), 'Times New Roman')
    pf = st.paragraph_format
    pf.space_before = Pt(0); pf.space_after = Pt(0); pf.line_spacing = 1.0
    s = d.sections[0]
    if page:
        s.page_width, s.page_height = Mm(page[0]), Mm(page[1])
    else:
        s.page_width, s.page_height = Mm(210), Mm(297)
        if landscape:
            s.orientation = WD_ORIENT.LANDSCAPE
            s.page_width, s.page_height = Mm(297), Mm(210)
    s.top_margin, s.bottom_margin, s.left_margin, s.right_margin = [Mm(x) for x in margins]
    s.header_distance = Mm(10); s.footer_distance = Mm(10)
    # xóa đoạn trống mặc định
    for p in list(d.element.body.findall(qn('w:p'))):
        d.element.body.remove(p)
    return d


def add_section(d, landscape):
    s = d.add_section(WD_SECTION.NEW_PAGE)
    if landscape:
        s.orientation = WD_ORIENT.LANDSCAPE
        s.page_width, s.page_height = Mm(297), Mm(210)
        s.top_margin, s.bottom_margin, s.left_margin, s.right_margin = Mm(20), Mm(20), Mm(20), Mm(20)
    else:
        s.orientation = WD_ORIENT.PORTRAIT
        s.page_width, s.page_height = Mm(210), Mm(297)
        s.top_margin, s.bottom_margin, s.left_margin, s.right_margin = Mm(20), Mm(20), Mm(30), Mm(20)
    return s


def _runs(p, text, size, bold, italic):
    if '«' in text:
        for seg in re.split(r'(«[^»]*»)', text):
            if seg.startswith('«'):
                _runs(p, seg[1:-1], size, bold, True)
            elif seg:
                _runs(p, seg, size, bold, italic)
        return p
    for part in re.split(r'(⟦[^⟧]*⟧|⟪[^⟫]*⟫)', text):
        if not part:
            continue
        b, i, col, t = bold, italic, None, part
        if part.startswith('⟦'):
            col, t = PURPLE, part[1:-1]
        elif part.startswith('⟪'):
            b, t = True, part[1:-1]
        r = p.add_run(t)
        r.font.name = 'Times New Roman'
        r._element.get_or_add_rPr().find(qn('w:rFonts')).set(qn('w:eastAsia'), 'Times New Roman')
        r.font.size = Pt(size); r.bold = b; r.italic = i
        if col:
            r.font.color.rgb = docx.shared.RGBColor.from_string(col)
    return p


def P(container, text='', *, size=14, bold=False, italic=False, align='both', indent=True,
      before=6, after=0, keep=False, line=1.0, page_break=False):
    p = container.add_paragraph()
    pf = p.paragraph_format
    pf.alignment = {'both': WD_ALIGN_PARAGRAPH.JUSTIFY, 'center': WD_ALIGN_PARAGRAPH.CENTER,
                    'left': WD_ALIGN_PARAGRAPH.LEFT, 'right': WD_ALIGN_PARAGRAPH.RIGHT}[align]
    pf.first_line_indent = Cm(1) if indent and align == 'both' else Cm(0)
    pf.space_before = Pt(before); pf.space_after = Pt(after)
    pf.line_spacing = line
    pf.widow_control = True
    if keep:
        pf.keep_with_next = True
    if page_break:
        pf.page_break_before = True
    _runs(p, text, size, bold, italic)
    return p


def add_line(p, width_pt, x_pt, y_pt):
    """Đường kẻ ngang (VML line) neo vào đoạn p, tọa độ tính theo vùng chữ của cột/ô."""
    _line_id[0] += 1
    xml = ('<w:r %s><w:rPr><w:noProof/></w:rPr><w:pict>'
           '<v:line xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" '
           'id="Line%d" o:spid="_x0000_s%d" '
           'style="position:absolute;z-index:%d;mso-position-horizontal:absolute;mso-position-horizontal-relative:text;'
           'mso-position-vertical:absolute;mso-position-vertical-relative:text" '
           'from="%.2fpt,%.2fpt" to="%.2fpt,%.2fpt" strokecolor="black" strokeweight=".75pt"/></w:pict></w:r>') % (
        W, _line_id[0], 1025 + _line_id[0], 251659264 + _line_id[0], x_pt, y_pt, x_pt + width_pt, y_pt)
    p._p.append(parse_xml(xml))


def _no_borders(tbl):
    tblPr = tbl._tbl.tblPr
    b = parse_xml('<w:tblBorders %s>%s</w:tblBorders>' % (W, ''.join(
        '<w:%s w:val="nil"/>' % k for k in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV'])))
    tblPr.append(b)


def _set_widths(tbl, widths):
    tbl.autofit = False
    tblPr = tbl._tbl.tblPr
    tw = tblPr.find(qn('w:tblW'))
    if tw is None:
        tw = OxmlElement('w:tblW'); tblPr.append(tw)
    tw.set(qn('w:w'), str(sum(widths))); tw.set(qn('w:type'), 'dxa')
    lay = OxmlElement('w:tblLayout'); lay.set(qn('w:type'), 'fixed'); tblPr.append(lay)
    grid = tbl._tbl.tblGrid
    for gc, w in zip(grid.findall(qn('w:gridCol')), widths):
        gc.set(qn('w:w'), str(w))
    for row in tbl.rows:
        for c, w in zip(row.cells, widths):
            c.width = Emu(w * 635)


def cell_text(cell, text, *, size=13, bold=False, italic=False, align='center', before=2, after=2, first=True):
    p = cell.paragraphs[0] if first and not cell.paragraphs[0].text and len(cell.paragraphs) == 1 else cell.add_paragraph()
    pf = p.paragraph_format
    pf.alignment = {'both': WD_ALIGN_PARAGRAPH.JUSTIFY, 'center': WD_ALIGN_PARAGRAPH.CENTER,
                    'left': WD_ALIGN_PARAGRAPH.LEFT, 'right': WD_ALIGN_PARAGRAPH.RIGHT}[align]
    pf.first_line_indent = Cm(0); pf.space_before = Pt(before); pf.space_after = Pt(after); pf.line_spacing = 1.0
    _runs(p, text, size, bold, italic)
    return p


def _valign(cell, v='center'):
    tcPr = cell._tc.get_or_add_tcPr()
    va = tcPr.find(qn('w:vAlign'))
    if va is None:
        va = OxmlElement('w:vAlign'); tcPr.append(va)
    va.set(qn('w:val'), v)


def TABLE(container, widths, rows, aligns, *, size=13, header=True, merge_rows=(), bold_rows=()):
    """Bảng nội dung: viền đơn, nền trắng, mọi ô căn giữa dọc, dòng tiêu đề lặp lại."""
    t = container.add_table(rows=len(rows), cols=len(widths))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.style = None
    tblPr = t._tbl.tblPr
    tblPr.append(parse_xml('<w:tblBorders %s>%s</w:tblBorders>' % (W, ''.join(
        '<w:%s w:val="single" w:sz="4" w:space="0" w:color="000000"/>' % k
        for k in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']))))
    _set_widths(t, widths)
    for ri, r in enumerate(rows):
        row = t.rows[ri]
        trPr = row._tr.get_or_add_trPr()
        trPr.append(parse_xml('<w:cantSplit %s/>' % W))
        if header and ri == 0:
            trPr.append(parse_xml('<w:tblHeader %s/>' % W))
        if ri in merge_rows:
            c = row.cells[0].merge(row.cells[-1])
            pm = cell_text(c, r[0], size=size, bold=True, align='left')
            pm.paragraph_format.keep_with_next = True
            _valign(c)
            continue
        for ci, txt in enumerate(r):
            c = row.cells[ci]
            hdr = header and ri == 0
            for k, line in enumerate(txt.split('\n')):
                cell_text(c, line, size=size, bold=hdr or ri in bold_rows,
                          align='center' if hdr else aligns[ci], first=(k == 0))
            _valign(c)
    return t


def header_block(d, org_lines, so, ngay, *, left_w=4100, right_w=5300, org_size=12, qh=True):
    """Bảng tiêu đề: tên đơn vị + số | quốc hiệu, tiêu ngữ + địa danh ngày."""
    t = d.add_table(rows=1, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _no_borders(t); _set_widths(t, [left_w, right_w])
    L, R = t.rows[0].cells
    for k, ln in enumerate(org_lines):
        p = cell_text(L, ln, size=org_size, bold=True, before=0, after=0, first=(k == 0))
    lw = 60 if len(org_lines[-1]) > 12 else 50
    add_line(p, lw, ((left_w - 216) / 20 - lw) / 2, org_size + 6)
    cell_text(L, '', size=8, before=0, after=0, first=False)
    if so:
        cell_text(L, so, size=13, before=4, after=0, first=False)
    if qh:
        cell_text(R, 'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM', size=12, bold=True, before=0, after=0)
        p = cell_text(R, 'Độc lập – Tự do – Hạnh phúc', size=14, bold=True, before=0, after=0, first=False)
        add_line(p, 171, ((right_w - 216) / 20 - 171) / 2, 18)
        cell_text(R, '', size=8, before=0, after=0, first=False)
        if ngay:
            cell_text(R, ngay, size=14, italic=True, before=4, after=0, first=False)
    for c in (L, R):
        _valign(c, 'top')
    return t


def quoc_hieu_center(d):
    P(d, 'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM', size=13, bold=True, align='center', before=0)
    p = P(d, 'Độc lập – Tự do – Hạnh phúc', size=14, bold=True, align='center', before=0)
    add_line(p, 170, (9072 / 20 - 170) / 2, 18)
    P(d, '', size=8, before=0)


def sign_block(d, noi_nhan, chuc_vu_lines, ten, *, left_w=4300, right_w=4772, blank=4):
    """Khối Nơi nhận - chữ ký: cách thân 1 dòng, căn trên, dòng Nơi nhận ngang chức vụ."""
    P(d, '', size=14, before=0)
    t = d.add_table(rows=1, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _no_borders(t); _set_widths(t, [left_w, right_w])
    tr = t.rows[0]._tr.get_or_add_trPr(); tr.append(parse_xml('<w:cantSplit %s/>' % W))
    L, R = t.rows[0].cells
    if noi_nhan:
        cell_text(L, 'Nơi nhận:', size=12, bold=True, italic=True, align='left', before=0, after=0)
        for k, n in enumerate(noi_nhan):
            cell_text(L, n, size=11, align='left', before=0, after=0, first=False)
    for k, c in enumerate(chuc_vu_lines):
        cell_text(R, c, size=14, bold=True, before=0, after=0, first=(k == 0))
    for _ in range(blank):
        cell_text(R, '', size=14, before=0, after=0, first=False)
    cell_text(R, ten, size=14, bold=True, before=0, after=0, first=False)
    for c in (L, R):
        _valign(c, 'top')
    # giữ khối ký liền
    for p in d.element.body.iter(qn('w:p')):
        pass
    return t


def two_sign(d, left, right, *, blank=4, names=('', '')):
    """Khối ký hai bên (hợp đồng): mỗi bên là list dòng in đậm, rồi chỗ ký, rồi tên."""
    P(d, '', size=14, before=0)
    t = d.add_table(rows=1, cols=2)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    _no_borders(t); _set_widths(t, [4536, 4536])
    tr = t.rows[0]._tr.get_or_add_trPr(); tr.append(parse_xml('<w:cantSplit %s/>' % W))
    for cell, lines, name in zip(t.rows[0].cells, (left, right), names):
        for k, ln in enumerate(lines):
            cell_text(cell, ln, size=14, bold=not ln.startswith('('), italic=ln.startswith('('),
                      before=0, after=0, first=(k == 0))
        for _ in range(blank):
            cell_text(cell, '', size=14, before=0, after=0, first=False)
        if name:
            cell_text(cell, name, size=14, bold=True, before=0, after=0, first=False)
        _valign(cell, 'top')
    return t


def keep_table_with_prev(p):
    p.paragraph_format.keep_with_next = True
