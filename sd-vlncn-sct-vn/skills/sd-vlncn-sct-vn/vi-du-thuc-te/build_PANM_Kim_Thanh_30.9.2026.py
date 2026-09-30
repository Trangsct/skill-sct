# -*- coding: utf-8 -*-
"""
Dung lai Phuong an no min Cty CP Kim Thanh - mo chi - kem Cao Pha (Tu Le), ham lo, ban day du 30/9/2026
(anti-error 37 sd-vlncn-sct-vn). Chay: python3 build_PANM_Kim_Thanh_30.9.2026.py [thu_muc_anh] [file_ra.docx]
- thu_muc_anh: chua s-06.jpg, s-19.jpg, s-20.jpg, s-21.jpg (anh ban ve trich Tap 2 thiet ke); thieu anh thi bo qua hinh.
- Chu tim 7030A0 = noi dung chua hoan thien.
"""
import sys, os
IMG_DIR = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'anh-PANM-Kim-Thanh')
OUT = sys.argv[2] if len(sys.argv) > 2 else 'PANM-Kim-Thanh-ban-day-du.docx'
# -*- coding: utf-8 -*-
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH as AL
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

RED = RGBColor(0x70, 0x30, 0xA0)
IND = Cm(1.0)

doc = Document()

# ---- page setup ----
s = doc.sections[0]
s.page_width, s.page_height = Cm(21.0), Cm(29.7)
s.left_margin, s.right_margin = Cm(3.0), Cm(2.0)
s.top_margin, s.bottom_margin = Cm(2.0), Cm(2.0)

st = doc.styles['Normal']
st.font.name = 'Times New Roman'
st.font.size = Pt(14)
st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
pf = st.paragraph_format
pf.space_after = Pt(0)
pf.space_before = Pt(0)
pf.line_spacing = 1.3
pf.alignment = AL.JUSTIFY


def para(text='', bold=False, italic=False, align=AL.JUSTIFY, indent=IND,
         size=14, red=False, space_before=0, space_after=0, keep=False):
    p = doc.add_paragraph()
    p.paragraph_format.alignment = align
    p.paragraph_format.first_line_indent = indent
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    if keep:
        p.paragraph_format.keep_with_next = True
    if text:
        add_run(p, text, bold, italic, size, red)
    return p


def add_run(p, text, bold=False, italic=False, size=14, red=False):
    r = p.add_run(text)
    r.bold = bold
    r.italic = italic
    r.font.name = 'Times New Roman'
    r.font.size = Pt(size)
    r._element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    if red:
        r.font.color.rgb = RED
    return r


def set_fixed(tbl, widths):
    tblPr = tbl._tbl.tblPr
    lay = OxmlElement('w:tblLayout')
    lay.set(qn('w:type'), 'fixed')
    tblPr.append(lay)
    grid = tbl._tbl.find(qn('w:tblGrid'))
    if grid is not None:
        tbl._tbl.remove(grid)
    grid = OxmlElement('w:tblGrid')
    for w in widths:
        gc = OxmlElement('w:gridCol')
        gc.set(qn('w:w'), str(int(w.twips)))
        grid.append(gc)
    tbl._tbl.insert(1, grid)


def set_borders(tbl):
    tblPr = tbl._tbl.tblPr
    borders = OxmlElement('w:tblBorders')
    for edge in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        el = OxmlElement('w:' + edge)
        el.set(qn('w:val'), 'single')
        el.set(qn('w:sz'), '6')
        el.set(qn('w:space'), '0')
        el.set(qn('w:color'), '000000')
        borders.append(el)
    tblPr.append(borders)


def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement('w:tblHeader')
    el.set(qn('w:val'), 'true')
    trPr.append(el)


def table(rows, widths=None, size=12, header=True, aligns=None):
    n = len(rows[0])
    tbl = doc.add_table(rows=len(rows), cols=n)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    set_borders(tbl)
    if widths:
        set_fixed(tbl, widths)
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = tbl.cell(i, j)
            cell.text = ''
            p = cell.paragraphs[0]
            p.paragraph_format.first_line_indent = Cm(0)
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.line_spacing = 1.0
            if i == 0 and header:
                p.paragraph_format.alignment = AL.CENTER
            elif aligns:
                p.paragraph_format.alignment = aligns[j]
            else:
                p.paragraph_format.alignment = AL.CENTER
            red = isinstance(val, tuple)
            txt = val[0] if red else val
            add_run(p, str(txt), bold=(i == 0 and header), size=size, red=red)
            if widths:
                cell.width = widths[j]
    if header:
        repeat_header(tbl.rows[0])
    if widths:
        for r in tbl.rows:
            for j, c in enumerate(r.cells):
                c.width = widths[j]
    return tbl



def new_section(landscape=False):
    sec = doc.add_section(WD_SECTION.NEW_PAGE)
    if landscape:
        sec.orientation = WD_ORIENT.LANDSCAPE
        sec.page_width, sec.page_height = Cm(29.7), Cm(21.0)
        sec.left_margin, sec.right_margin = Cm(2.0), Cm(2.0)
        sec.top_margin, sec.bottom_margin = Cm(2.0), Cm(2.0)
    else:
        sec.orientation = WD_ORIENT.PORTRAIT
        sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
        sec.left_margin, sec.right_margin = Cm(3.0), Cm(2.0)
        sec.top_margin, sec.bottom_margin = Cm(2.0), Cm(2.0)
    return sec


def caption(text):
    para(text, bold=True, align=AL.CENTER, indent=Cm(0), size=13,
         space_before=6, space_after=4, keep=True)


def spacer(pt=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(pt)
    p.paragraph_format.line_spacing = 1.0
    return p


from docx.shared import Cm as _Cm

L = AL.LEFT
C = AL.CENTER
_tbl_no = [0]


def T():
    _tbl_no[0] += 1
    return _tbl_no[0]


def mixed(parts, indent=IND, space_before=0, space_after=0, keep=False, align=AL.JUSTIFY):
    p = para('', indent=indent, space_before=space_before, space_after=space_after,
             keep=keep, align=align)
    for t, pu in parts:
        add_run(p, t, red=pu)
    return p


def h1(t):
    para(t, bold=True, space_before=6, space_after=3, keep=True)


def h2(t):
    para(t, bold=True, space_before=3, space_after=2, keep=True)


def h3(t):
    para(t, italic=True, bold=True, space_before=2, space_after=1, keep=True)


def paras(lst):
    for t in lst:
        if isinstance(t, list):
            mixed(t)
        else:
            para(t)


def nosplit(tbl, keep_all=False):
    for r in tbl.rows:
        r._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
    if keep_all:
        for r in tbl.rows[:-1]:
            for c in r.cells:
                for p in c.paragraphs:
                    p.paragraph_format.keep_with_next = True


def cap(text):
    caption('Bảng %d. %s' % (T(), text))
    return _tbl_no[0]


def src(text):
    para(text, italic=True, size=13, space_after=2)


# ================= HEADER =================
from docx.enum.text import WD_BREAK


def bottom_line(p, left_cm, right_cm, space=1, sz=6):
    """Duong ke ngang duoi dong chu: vien duoi doan, gioi han bang lui trai/phai."""
    pf = p.paragraph_format
    pf.left_indent = Cm(left_cm)
    pf.right_indent = Cm(right_cm)
    pPr = p._p.get_or_add_pPr()
    bdr = OxmlElement('w:pBdr')
    b = OxmlElement('w:bottom')
    b.set(qn('w:val'), 'single')
    b.set(qn('w:sz'), str(sz))
    b.set(qn('w:space'), str(space))
    b.set(qn('w:color'), '000000')
    bdr.append(b)
    pPr.append(bdr)


def line_para(cell_or_doc, left_cm, right_cm):
    q = cell_or_doc.add_paragraph()
    q.paragraph_format.first_line_indent = Cm(0)
    q.paragraph_format.space_before = Pt(0)
    q.paragraph_format.space_after = Pt(0)
    q.paragraph_format.line_spacing = Pt(2)
    r = q.add_run('')
    r.font.size = Pt(2)
    bottom_line(q, left_cm, right_cm, space=0)
    return q



_line_id = [100]


def hline(p, x_cm, y_cm, w_cm):
    """Duong ke ngang ve bang Straight Connector (nhu mau that), neo vao doan p."""
    from lxml import etree
    _line_id[0] += 1
    E = 360000
    x, y, w = int(x_cm * E), int(y_cm * E), int(w_cm * E)
    xml = (
        '<w:r xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
        'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
        'xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">'
        '<w:drawing><wp:anchor distT="0" distB="0" distL="114300" distR="114300" simplePos="0" '
        'relativeHeight="%d" behindDoc="0" locked="0" layoutInCell="1" allowOverlap="1">'
        '<wp:simplePos x="0" y="0"/>'
        '<wp:positionH relativeFrom="column"><wp:posOffset>%d</wp:posOffset></wp:positionH>'
        '<wp:positionV relativeFrom="paragraph"><wp:posOffset>%d</wp:posOffset></wp:positionV>'
        '<wp:extent cx="%d" cy="0"/><wp:effectExtent l="0" t="0" r="0" b="0"/><wp:wrapNone/>'
        '<wp:docPr id="%d" name="Straight Connector %d"/><wp:cNvGraphicFramePr/>'
        '<a:graphic><a:graphicData uri="http://schemas.microsoft.com/office/word/2010/wordprocessingShape">'
        '<wps:wsp><wps:cNvCnPr/><wps:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="%d" cy="0"/></a:xfrm>'
        '<a:prstGeom prst="line"><a:avLst/></a:prstGeom>'
        '<a:ln w="9525"><a:solidFill><a:srgbClr val="000000"/></a:solidFill></a:ln></wps:spPr>'
        '<wps:bodyPr/></wps:wsp></a:graphicData></a:graphic></wp:anchor></w:drawing></w:r>'
    ) % (251660000 + _line_id[0], x, y, w, _line_id[0], _line_id[0], w)
    p._p.append(etree.fromstring(xml))


def cover_page():
    pc = para('CÔNG TY CỔ PHẦN KIM THÀNH', bold=True, align=C, indent=Cm(0), size=15, space_before=6)
    hline(pc, 6.5, 0.98, 3.0)
    for _ in range(4):
        spacer(14)
    para('PHƯƠNG ÁN NỔ MÌN', bold=True, align=C, indent=Cm(0), size=28, space_after=8)
    p = para('', align=C, indent=Cm(0), size=14, space_after=6)
    add_run(p, 'Số: ', size=14)
    add_run(p, '01/PANM-KT', size=14, red=True)
    spacer(14)
    for t in ['KHAI THÁC QUẶNG CHÌ - KẼM BẰNG PHƯƠNG PHÁP HẦM LÒ',
              'TẠI MỎ CHÌ - KẼM KHU VỰC XÃ CAO PHẠ,',
              'HUYỆN MÙ CANG CHẢI, TỈNH YÊN BÁI',
              '(NAY LÀ XÃ TÚ LỆ, TỈNH LÀO CAI)']:
        para(t, bold=True, align=C, indent=Cm(0), size=14, space_after=0)
    spacer(8)
    para('(Giấy phép khai thác khoáng sản số 680/GP-UBND ngày 07/4/2020', italic=True, align=C, indent=Cm(0), size=13)
    para('của Ủy ban nhân dân tỉnh Yên Bái)', italic=True, align=C, indent=Cm(0), size=13)
    for _ in range(4):
        spacer(14)
    para('ĐƠN VỊ LẬP PHƯƠNG ÁN: CÔNG TY CỔ PHẦN KIM THÀNH', bold=True, align=C, indent=Cm(0), size=13, space_after=2)
    para('Trụ sở: Tổ 6, phường Nghĩa Lộ, tỉnh Lào Cai', align=C, indent=Cm(0), size=13, space_after=2)
    para('Địa điểm nổ mìn: mỏ chì - kẽm khu vực xã Tú Lệ, tỉnh Lào Cai', align=C, indent=Cm(0), size=13)
    for _ in range(3):
        spacer(14)
    para('Lào Cai, năm 2026', bold=True, align=C, indent=Cm(0), size=14)


cover_page()
_cover_sec = doc.sections[0]
_main = new_section(False)
# vien trang doi cho bia
pg = OxmlElement('w:pgBorders')
pg.set(qn('w:offsetFrom'), 'text')
for edge in ('top', 'left', 'bottom', 'right'):
    e = OxmlElement('w:' + edge)
    e.set(qn('w:val'), 'double')
    e.set(qn('w:sz'), '12')
    e.set(qn('w:space'), '12')
    e.set(qn('w:color'), '000000')
    pg.append(e)
sp_ = doc.sections[0]._sectPr
# chen pgBorders sau pgMar theo thu tu schema
pgMar = sp_.find(qn('w:pgMar'))
pgMar.addnext(pg)
# so trang: giua, dau trang, tu trang noi dung (bia khong danh so)
_main.header.is_linked_to_previous = False
hp = _main.header.paragraphs[0]
hp.paragraph_format.alignment = C
hp.paragraph_format.first_line_indent = Cm(0)
_r = hp.add_run()
for tag, txt in (('begin', None), (None, 'PAGE'), ('end', None)):
    if tag:
        fc = OxmlElement('w:fldChar'); fc.set(qn('w:fldCharType'), tag); _r._r.append(fc)
    else:
        it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = txt; _r._r.append(it)
_r.font.size = Pt(13); _r.font.name = 'Times New Roman'
pgn = OxmlElement('w:pgNumType'); pgn.set(qn('w:start'), '1')
_main._sectPr.append(pgn)
_tp = OxmlElement('w:titlePg'); _main._sectPr.append(_tp)
# bia: header rieng, trong
doc.sections[0].header.is_linked_to_previous = False

h = doc.add_table(rows=1, cols=2)
h.alignment = WD_TABLE_ALIGNMENT.CENTER
c1, c2 = h.cell(0, 0), h.cell(0, 1)
set_fixed(h, [Cm(5.5), Cm(10.5)])
c1.width, c2.width = Cm(5.5), Cm(10.5)
p = c1.paragraphs[0]
p.paragraph_format.alignment = C
p.paragraph_format.first_line_indent = Cm(0)
p.paragraph_format.line_spacing = 1.1
add_run(p, 'CÔNG TY CỔ PHẦN KIM THÀNH', bold=True, size=13)
hline(p, 1.62, 1.14, 1.9)
p = c2.paragraphs[0]
p.paragraph_format.alignment = C
p.paragraph_format.first_line_indent = Cm(0)
p.paragraph_format.line_spacing = 1.1
add_run(p, 'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM', bold=True, size=13)
p2 = c2.add_paragraph()
p2.paragraph_format.alignment = C
p2.paragraph_format.first_line_indent = Cm(0)
p2.paragraph_format.line_spacing = 1.1
add_run(p2, 'Độc lập – Tự do – Hạnh phúc', bold=True, size=13)
hline(p2, 2.16, 0.62, 5.8)

spacer(10)
para('PHƯƠNG ÁN NỔ MÌN', bold=True, align=C, indent=Cm(0), size=16, space_after=4)
para('Khai thác quặng chì - kẽm bằng phương pháp hầm lò tại mỏ chì - kẽm khu vực '
     'xã Cao Phạ, huyện Mù Cang Chải, tỉnh Yên Bái (nay là xã Tú Lệ, tỉnh Lào Cai)',
     bold=True, align=C, indent=Cm(0), size=13, space_after=10)

# ================= I =================
h1('I. CĂN CỨ LẬP PHƯƠNG ÁN')
h2('1. Căn cứ pháp lý, tiêu chuẩn, quy chuẩn và thiết kế')
h3('a) Văn bản quy phạm pháp luật, quy chuẩn kỹ thuật')
paras([
    '- Luật Quản lý, sử dụng vũ khí, vật liệu nổ và công cụ hỗ trợ số 42/2024/QH15 ngày 29/6/2024, được sửa đổi, bổ sung tại Luật số 118/2025/QH15 ngày 10/12/2025;',
    '- Luật Địa chất và khoáng sản số 54/2024/QH15 ngày 29/11/2024;',
    '- Nghị định số 181/2024/NĐ-CP ngày 31/12/2024 của Chính phủ quy định chi tiết một số điều của Luật Quản lý, sử dụng vũ khí, vật liệu nổ và công cụ hỗ trợ về vật liệu nổ công nghiệp và tiền chất thuốc nổ;',
    '- Thông tư số 23/2024/TT-BCT ngày 07/11/2024 của Bộ trưởng Bộ Công Thương quy định về quản lý, sử dụng vật liệu nổ công nghiệp, tiền chất thuốc nổ thuộc thẩm quyền quản lý của Bộ Công Thương, được sửa đổi, bổ sung tại Thông tư số 38/2025/TT-BCT ngày 19/6/2025 và Thông tư số 26/2026/TT-BCT ngày 20/5/2026;',
    '- QCVN 01:2019/BCT - Quy chuẩn kỹ thuật quốc gia về an toàn trong sản xuất, thử nghiệm, nghiệm thu, bảo quản, vận chuyển, sử dụng, tiêu hủy vật liệu nổ công nghiệp và bảo quản tiền chất thuốc nổ (ban hành kèm theo Thông tư số 32/2019/TT-BCT ngày 21/11/2019);',
    '- QCVN 04:2017/BCT - Quy chuẩn kỹ thuật quốc gia về an toàn trong khai thác quặng hầm lò (ban hành kèm theo Thông tư số 31/2017/TT-BCT ngày 28/12/2017);',
    '- QCVN 05:2012/BCT - Quy chuẩn kỹ thuật quốc gia về thuốc nổ nhũ tương dùng cho mỏ hầm lò, công trình ngầm không có khí và bụi nổ và các quy chuẩn kỹ thuật quốc gia tương ứng với chủng loại vật liệu nổ công nghiệp được lựa chọn sử dụng.',
])
h3('b) Hồ sơ pháp lý của dự án')
paras([
    '- Quyết định số 1717/QĐ-UBND ngày 06/9/2019 của Ủy ban nhân dân tỉnh Yên Bái phê duyệt trữ lượng quặng chì - kẽm khu vực xã Cao Phạ;',
    '- Quyết định số 292/QĐ-UBND ngày 21/02/2020 của Ủy ban nhân dân tỉnh Yên Bái chấp thuận chủ trương đầu tư Dự án đầu tư khai thác quặng chì - kẽm mỏ chì - kẽm khu vực xã Cao Phạ, huyện Mù Cang Chải, tỉnh Yên Bái;',
    '- Giấy phép khai thác khoáng sản số 680/GP-UBND ngày 07/4/2020 của Ủy ban nhân dân tỉnh Yên Bái cấp cho Công ty Cổ phần Kim Thành được khai thác quặng chì - kẽm bằng phương pháp hầm lò tại khu vực xã Cao Phạ, huyện Mù Cang Chải, tỉnh Yên Bái (nay là xã Tú Lệ, tỉnh Lào Cai), thời hạn đến hết ngày 07/10/2028;',
    '- Quyết định số 1345/QĐ-UBND ngày 02/7/2020 của Ủy ban nhân dân tỉnh Yên Bái về việc gia hạn sử dụng đất cho Công ty Cổ phần Kim Thành; Hợp đồng thuê đất số 67/2020/HĐTĐ ngày 21/8/2020;',
    '- Giấy phép sử dụng vật liệu nổ công nghiệp số 5248/GP-SCT ngày 25/8/2026 của Sở Công Thương tỉnh Lào Cai cấp cho Công ty Cổ phần Kim Thành.',
])
h3('c) Hồ sơ thiết kế mỏ')
paras([
    '- Thiết kế bản vẽ thi công công trình khai thác quặng chì - kẽm khu vực xã Cao Phạ (thiết kế gốc), được Sở Công Thương tỉnh Yên Bái thông báo kết quả thẩm định tại Văn bản số 738/SCT-KTATMT ngày 07/5/2020, Giám đốc Công ty phê duyệt tại Quyết định số 10.5/QĐ-KT ngày 10/5/2020;',
    '- Thiết kế bản vẽ thi công điều chỉnh do Công ty TNHH tư vấn và đầu tư Sơn Thái lập năm 2021, được Sở Công Thương tỉnh Yên Bái thông báo kết quả thẩm định tại Văn bản số 897/SCT-KTATMT ngày 18/5/2021 (sau đây gọi tắt là Thiết kế điều chỉnh lần thứ nhất);',
    [('- Thiết kế bản vẽ thi công điều chỉnh Dự án đầu tư khai thác quặng chì - kẽm mỏ chì - kẽm khu vực xã Cao Phạ, huyện Mù Cang Chải, tỉnh Yên Bái (nay là xã Tú Lệ, tỉnh Lào Cai), gồm Tập 1 - Thuyết minh và Tập 2 - Bản vẽ, do Công ty TNHH MTV Tư vấn Đầu tư Xây dựng Công nghiệp Mỏ Luyện kim lập tháng 5/2026; được Công ty Cổ phần Tư vấn Khoáng sản và Tài nguyên Môi trường thẩm tra ngày 19/5/2026; Công ty thẩm định tại Văn bản số 25.5/2026/TB-KT ngày 25/5/2026 và Giám đốc Công ty phê duyệt tại Quyết định số 26.5/QĐ-KT ', False), ('ngày 26/5/2026', True), (' (sau đây gọi tắt là Thiết kế được duyệt).', False)],
])
h3('d) Hồ sơ kho vật liệu nổ công nghiệp và nhân sự')
paras([
    '- Giấy chứng nhận thẩm duyệt thiết kế về phòng cháy và chữa cháy số 28/TD-PCCC ngày 24/01/2024 và Văn bản số 31/NT-PCCC ngày 29/3/2024 chấp thuận kết quả nghiệm thu về phòng cháy và chữa cháy của Phòng Cảnh sát PCCC và CNCH, Công an tỉnh Yên Bái; Thông báo số 945/TB-SCT ngày 25/4/2024 của Sở Công Thương tỉnh Yên Bái về kết quả kiểm tra công tác nghiệm thu hoàn thành công trình kho chứa vật liệu nổ công nghiệp;',
    '- Giấy chứng nhận đủ điều kiện về an ninh, trật tự số 19/GCN-CĐ5 ngày 10/6/2024;',
    '- Quyết định số 11/QĐ-BN ngày 01/5/2025 và Quyết định số 01/QĐ-BN ngày 03/6/2024 của Giám đốc Công ty về việc bổ nhiệm chỉ huy nổ mìn tại mỏ chì - kẽm xã Cao Phạ; Danh sách cán bộ, công nhân liên quan đến vật liệu nổ công nghiệp mỏ chì xã Tú Lệ, tỉnh Lào Cai tháng 8 năm 2026 của Công ty.',
])

h2('2. Trữ lượng, quy mô, công suất, chế độ làm việc và năng suất khai thác')
paras([
    '- Diện tích khu vực khai thác: 3,526 ha; phương pháp khai thác: hầm lò; biên giới dưới sâu của mỏ giới hạn tại mức +1635 m.',
    '- Trữ lượng: tổng trữ lượng cấp 122 của toàn mỏ là 70.864 tấn quặng (Quyết định số 1717/QĐ-UBND); trữ lượng được phép đưa vào thiết kế khai thác là 67.304 tấn, trữ lượng khai thác là 57.209 tấn (Giấy phép khai thác khoáng sản số 680/GP-UBND); trữ lượng đã khai thác đến ngày 31/12/2025 là 35.354,67 tấn; trữ lượng khai thác còn lại là 21.854,33 tấn (mục 2.1.4 Thiết kế được duyệt).',
    '- Công suất khai thác: 7.150 tấn quặng nguyên khai/năm (mục 3.2.1 Thiết kế được duyệt).',
    '- Chế độ làm việc: 300 ngày/năm; 25 ngày/tháng; 01 ca/ngày đêm (Bảng 3.1 Thiết kế được duyệt); thời gian hoàn thành 01 chu kỳ đào lò là 07 giờ (bản vẽ hộ chiếu thi công).',
    '- Hệ số tổn thất quặng thực tế của mỏ 15%; hệ số làm việc không đều trong năm k’ = 0,715 (Bảng 8.3 Thiết kế được duyệt).',
])
para('Năng suất khai thác và tiến độ đào lò theo ngày, tháng, quý, năm được tổng hợp như sau:', keep=True)
cap('Năng suất khai thác, tiến độ đào lò theo thời gian')
t = table([
    ['TT', 'Chỉ tiêu', 'Đơn vị', 'Ngày đêm', 'Tháng', 'Quý', 'Năm'],
    ['1', 'Sản lượng quặng nổ mìn lò chợ', 'tấn', '41,66', '-', '-', '-'],
    ['2', 'Sản lượng quặng khai thác', 'tấn', '33,33', '833,24', '1.787,5', '7.150'],
    ['3', 'Tiến độ đào lò có chống (tiết diện đào 5,20 m²)', 'm', '0,80', '20', '60', '240'],
    ['4', 'Tiến độ đào lò không chống, lò chân tầng', 'm', '1,00', '25', '75', '300'],
], widths=[Cm(0.9), Cm(6.1), Cm(1.4), Cm(1.8), Cm(1.8), Cm(1.9), Cm(2.1)], size=12,
    aligns=[C, L, C, C, C, C, C])
nosplit(t, True)
src('Nguồn: Bảng 8.3 Thiết kế được duyệt và Bảng chỉ tiêu kinh tế - kỹ thuật cơ bản của đường lò trên các bản vẽ hộ chiếu thi công (KT-DADC-CTN-06.1, 06.2, 06.3). Sản lượng quý bằng sản lượng năm chia đều cho 04 quý; tiến độ quý, năm tính theo 25 ngày/tháng và 300 ngày/năm.')
para('Trình tự khai thác theo Bảng 5.2 Thiết kế được duyệt như sau:', keep=True)
cap('Lịch khai thác lò chợ')
t = table([
    ['TT', 'Tên lò chợ', 'Trữ lượng khai thác (tấn)', 'Công suất (tấn/năm)', 'Thời gian khai thác (năm)', 'Năm thực hiện'],
    ['1', 'Lò chợ cột 03', '1.582', '7.150', '0,2', '2026'],
    ['2', 'Lò chợ cột 04', '11.864', '7.150', '1,7', '2026 - 2027'],
    ['3', 'Lò chợ cột 05', '8.408', '7.150', '1,2', '2027 - 2028'],
    ['', 'Tổng cộng', '21.854', '', '3,1', ''],
], widths=[Cm(0.9), Cm(3.6), Cm(3.0), Cm(2.6), Cm(2.8), Cm(3.1)], size=12,
    aligns=[C, L, C, C, C, C])
nosplit(t, True)
src('Nguồn: Bảng 5.2 Thiết kế được duyệt. Phần trữ lượng chưa khai thác hết sau ngày 07/10/2028 chỉ được tiếp tục khai thác và sử dụng vật liệu nổ công nghiệp khi được gia hạn Giấy phép khai thác khoáng sản và Giấy phép sử dụng vật liệu nổ công nghiệp theo quy định.')

h2('3. Phương pháp mở vỉa, hệ thống khai thác, công nghệ khai thác, thiết bị và nhân công')
h3('a) Mở vỉa và hiện trạng các đường lò')
para('Mỏ được mở vỉa bằng các đường lò bằng (lò xuyên vỉa, lò dọc vỉa) kết hợp lò thượng; không có giếng mỏ, sân ga, hầm trạm. Mỏ chia thành 03 mức khai thác: mức thứ nhất từ +1690 m đến +1715 m, khai thông bằng lò xuyên vỉa từ mặt bằng cửa lò số 1 (+1690 m); mức thứ hai từ +1660 m đến +1690 m, khai thông bằng lò xuyên vỉa từ mặt bằng cửa lò số 4 (+1656 m); mức thứ ba từ +1635 m đến +1660 m, khai thông bằng lò xuyên vỉa từ mặt bằng cửa lò số 3 (+1633 m). Các mức được liên kết bằng lò thượng thông gió - vận tải +1633 m ÷ +1715 m; lò dọc vỉa +1715 m của mức khai thác trước được sử dụng làm lò thông gió. Các đường lò đào với tiết diện hình thang, diện tích đào 5,2 m², diện tích sử dụng 3,8 m², chống gỗ, bước chống 0,8 m/vì (mục 4.2 Thiết kế được duyệt).')
para('Mỏ đã hoàn thành công tác xây dựng cơ bản và đi vào hoạt động từ năm 2020. Khối lượng các đường lò khai thông đã đầu tư xây dựng như sau:', keep=True)
cap('Khối lượng các đường lò khai thông đã đầu tư xây dựng')
t = table([
    ['TT', 'Tên đường lò', 'Vật liệu chống', 'Sđ (m²)', 'Ssd (m²)', 'Chiều dài (m)'],
    ['1', 'Lò trong đá', '', '', '', '543,5'],
    ['-', 'Lò xuyên vỉa mức +1633', 'Gỗ', '5,2', '3,8', '258,7'],
    ['-', 'Lò xuyên vỉa mức +1656', 'Gỗ', '5,2', '3,8', '132,1'],
    ['-', 'Lò xuyên vỉa mức +1690', 'Gỗ', '5,2', '3,8', '152,7'],
    ['2', 'Lò trong quặng', '', '', '', '323,0'],
    ['-', 'Lò dọc vỉa mức +1715', 'Gỗ', '5,2', '3,8', '66,0'],
    ['-', 'Thượng thông gió - vận tải mức +1633 ÷ +1715', 'Gỗ', '4,2', '3,24', '90,0'],
    ['-', 'Lò dọc vỉa mức +1690', 'Gỗ', '5,2', '3,8', '65,0'],
    ['-', 'Lò dọc vỉa mức +1660', 'Gỗ', '5,2', '3,8', '55,0'],
    ['-', 'Lò dọc vỉa mức +1635', 'Gỗ', '5,2', '3,8', '47,0'],
    ['', 'Tổng cộng', '', '', '', '866,5'],
], widths=[Cm(0.9), Cm(7.1), Cm(2.0), Cm(1.8), Cm(1.8), Cm(2.4)], size=12,
    aligns=[C, L, C, C, C, C])
nosplit(t, True)
src('Nguồn: Bảng 1.4 Thiết kế được duyệt.')
h3('b) Hệ thống khai thác và công nghệ khai thác')
paras([
    'Hệ thống khai thác áp dụng là hệ thống khai thác buồng lưu quặng cho các khối, thân quặng có góc dốc lớn hơn 50 độ; tầng được chia thành phân tầng cao 30 m theo hướng dốc, theo phương chia thành các khối khai thác rộng 30 m đến 40 m; trên mỗi mức, ruộng mỏ được chia thành các cột có chiều dài theo phương từ 20 m đến 50 m bằng các lò thượng cột (mục 3.1.2 và mục 8.1.1 Thiết kế được duyệt).',
    'Công tác chuẩn bị gồm: đào lò xuyên vỉa, dọc vỉa vận chuyển mức dưới; lò thượng cuối khối nối thông giữa các lò dọc vỉa và mặt đất để thông gió; thượng đầu khối tiến trước gương khai thác; lò chân tầng đào dọc vỉa, chênh cao 3 m đến 5 m so với lò dọc vỉa vận chuyển; các phễu tháo quặng từ lò dọc vỉa lên lò chân tầng, bố trí cách nhau 4 m đến 8 m; các lò cúp từ thượng vào buồng khai thác để thông gió.',
    'Công tác khấu quặng: trong mỗi luồng khấu, khai thác bằng khoan nổ mìn từng đợt trong các lỗ khoan nhỏ theo các lớp dày 1,5 m đến 2,5 m, trên từng đoạn lò chợ dài 5,0 m, lỗ khoan được khoan lên theo hướng khấu. Sau mỗi chu kỳ khấu, tháo sơ bộ 30% đến 40% lượng quặng đã nở rời để tạo không gian làm việc tại gương; việc tháo và điều tiết quặng thực hiện bằng cửa chắn và cũi lợn tại các lò tháo quặng.',
    'Công tác chống giữ: đá và quặng có độ kiên cố lớn nên gương lò chợ không chống; trường hợp gương, vách, trụ có biểu hiện kém ổn định thì chống giữ tạm bằng cột gỗ đường kính 14 cm đến 16 cm, văng, xà gỗ đường kính 12 cm đến 14 cm.',
    'Công tác vận tải: quặng tháo qua các phễu xuống goòng trên lò dọc vỉa, đẩy hoặc kéo bằng tàu điện ra bãi chứa tại mặt bằng cửa lò; mặt bằng tập kết quặng tại mức +1656 m. Quặng quá cỡ được đập vụn lần hai bằng búa chèn; Phương án này không áp dụng nổ mìn ốp để phá quặng, đá quá cỡ.',
])
h3('c) Thiết bị phục vụ công tác khoan nổ mìn')
cap('Thiết bị chủ yếu phục vụ công tác khoan nổ mìn')
t = table([
    ['TT', 'Tên thiết bị', 'Đặc tính kỹ thuật chính', 'Số lượng', 'Nguồn'],
    ['1', 'Búa khoan khí nén YT-24', 'Khoan gương đào lò', '02 chiếc', 'Bảng 8.9'],
    ['2', 'Máy khoan khí nén YT-28', 'Đường kính khoan 34 - 45 mm; áp lực 0,47 - 0,63 MPa; nặng 26 kg', 'Theo nhu cầu lò chợ', 'Mục 8.1'],
    ['3', 'Máy nén khí LGY-5/8GT', 'Công suất 5 m³/phút', '01 chiếc', 'Bảng 8.9'],
    ['4', 'Quạt gió cục bộ YBT-52-2', 'Lưu lượng 145 - 225 m³/phút; hạ áp 100 - 240 mmH₂O; 11 kW', '02 chiếc', 'Bảng 8.9'],
    ['5', 'Máy nổ mìn BKM-1/100', 'Khởi nổ kíp điện, mắc nối tiếp đến 100 kíp', '02 chiếc', 'Bảng 8.9'],
    ['6', 'Máy nổ mìn MEB (tương đương)', 'Điện trở mạch kíp cho phép 1.220 Ω; điện áp đầu ra 3.000 V', 'Dự phòng', 'Mục 8.1'],
    ['7', 'Búa chèn G10', 'Sửa gương, phá đá quá cỡ; năng lượng tác động 43 J', 'Theo nhu cầu', 'Mục 8.1'],
    ['8', 'Xe goòng 0,8 m³', 'Cỡ đường 600 mm', '10 chiếc', 'Bảng 1.5'],
], widths=[Cm(0.9), Cm(4.3), Cm(6.3), Cm(2.3), Cm(2.2)], size=12, aligns=[C, L, L, C, C])
nosplit(t)
src('Nguồn: Bảng 1.5, mục 8.1 và Bảng 8.9 Thiết kế được duyệt; được thay thế bằng thiết bị có đặc tính kỹ thuật tương đương.')
h3('d) Nhân công')
para('Lò chợ bố trí 10 người/ngày đêm làm việc trực tiếp tại buồng khai thác và buồng thu hồi (Bảng 8.3 và Bảng 8.4 Thiết kế được duyệt); mỗi gương đào lò bố trí 04 người/ca (bản vẽ hộ chiếu thi công). Nhân sự trực tiếp thực hiện công tác vật liệu nổ công nghiệp gồm 12 người, nêu tại mục V.3 Phương án này.')

h2('4. Các từ, cụm từ viết tắt')
paras([
    '- VLNCN: vật liệu nổ công nghiệp;',
    '- QCVN: quy chuẩn kỹ thuật quốc gia;',
    '- Thiết kế được duyệt: Thiết kế bản vẽ thi công điều chỉnh lập tháng 5/2026 nêu tại điểm c mục I.1 Phương án này;',
    '- Thiết kế điều chỉnh lần thứ nhất: Thiết kế bản vẽ thi công điều chỉnh lập năm 2021 nêu tại điểm c mục I.1 Phương án này;',
    '- Bản vẽ hộ chiếu thi công: các bản vẽ số KT-DADC-CTN-06.1 (lò dọc vỉa, xuyên vỉa có chống), KT-DADC-CTN-06.2 (lò dọc vỉa, xuyên vỉa không chống), KT-DADC-CTN-06.3 (lò chân tầng không chống) thuộc Tập 2 Thiết kế được duyệt;',
    '- Sđ, Ssd: diện tích tiết diện đào, diện tích tiết diện sử dụng của đường lò;',
    '- Công ty: Công ty Cổ phần Kim Thành.',
])

# ================= II =================
h1('II. ĐẶC ĐIỂM KHU VỰC NỔ MÌN')
h2('1. Vị trí, giới hạn tọa độ và cao độ khu vực nổ mìn')
para('Toàn bộ khu vực nổ mìn nằm trọn trong ranh giới khu vực khai thác đã được cấp phép tại Giấy phép khai thác khoáng sản số 680/GP-UBND ngày 07/4/2020, diện tích 3,526 ha, thuộc xã Tú Lệ, tỉnh Lào Cai (trước đây là bản Kháo Nhà, xã Cao Phạ, huyện Mù Cang Chải, tỉnh Yên Bái). Tọa độ các điểm khép góc và vị trí các cửa lò như sau:', keep=True)
cap('Tọa độ ranh giới khu vực khai thác (VN 2000, KTT 104°45’, múi chiếu 3°)')
t = table([
    ['Tên điểm', 'X (m)', 'Y (m)', 'Tên điểm', 'X (m)', 'Y (m)'],
    ['1', '2.413.383', '442.754', '6', '2.413.241', '443.197'],
    ['2', '2.413.310', '442.885', 'VI', '2.413.224', '443.125'],
    ['3', '2.413.307', '443.121', 'VII', '2.413.234', '443.124'],
    ['4', '2.413.327', '443.176', '7', '2.413.201', '443.029'],
    ['5', '2.413.260', '443.222', '8', '2.413.320', '442.736'],
], widths=[Cm(2.0), Cm(3.1), Cm(2.9), Cm(2.0), Cm(3.1), Cm(2.9)], size=12)
nosplit(t, True)
src('Nguồn: Bảng 2.1 Thiết kế được duyệt và bản vẽ KT-DADC-KT-01. Diện tích: 3,526 ha.')
cap('Tọa độ, cao độ các cửa lò')
t = table([
    ['TT', 'Tên cửa lò', 'X (m)', 'Y (m)', 'Cao độ mặt bằng', 'Mức khai thác phục vụ'],
    ['1', 'Cửa lò số 1', '2.413.265', '443.032', '+1690 m', '+1690 ÷ +1715 m'],
    ['2', 'Cửa lò số 4', '2.413.300', '443.138', '+1656 m', '+1660 ÷ +1690 m'],
    ['3', 'Cửa lò số 3', '2.413.330', '443.184', '+1633 m', '+1635 ÷ +1660 m'],
], widths=[Cm(0.9), Cm(2.8), Cm(2.8), Cm(2.4), Cm(3.0), Cm(4.1)], size=12)
nosplit(t, True)
src('Nguồn: bản vẽ KT-DADC-KT-01 (Ranh giới khai trường và vị trí cửa lò) và mục 4.1, 4.2 Thiết kế được duyệt. Mặt bằng cửa lò số 3 có diện tích 0,18 ha.')
mixed([('Bản đồ địa hình khu vực nổ mìn thể hiện ranh giới khu vực khai thác, ranh giới khu phụ trợ, vị trí các cửa lò, hệ thống đường lò và đường giao thông được đính kèm tại Phụ lục 2 Phương án này (trích bản vẽ KT-DADC-KT-01 của Thiết kế được duyệt). ', False),
       ('Công ty bổ sung trên bản đồ vòng bán kính 1.000 m tính từ các cửa lò và vị trí các công trình nêu tại Bảng 7 Phương án này.', True)])

h2('2. Đặc điểm địa hình, khí hậu và điều kiện hạ tầng')
paras([
    'Địa hình khu vực có dạng dải kéo dài theo phương Tây Bắc - Đông Nam, thuộc vùng núi cao và trung bình, độ cao từ 1.400 m đến 2.200 m, sườn dốc 60 - 75 độ; khu mỏ nằm ở độ cao khoảng 1.600 m. Khí hậu mang đặc tính miền núi Tây Bắc, chia thành hai mùa; mùa mưa từ tháng 4 đến tháng 10, lượng mưa 1.500 - 2.200 mm/năm, có nguy cơ lũ quét, trượt lở đất.',
    'Giao thông: mỏ cách Ngã Ba Kim (Quốc lộ 32) khoảng 17 km về phía Tây Nam; từ Quốc lộ 32 vào mỏ theo tuyến đường liên thôn bê tông dài 5 km, rộng 6 m và tuyến đường đá cấp phối dài 12 km, rộng 5 m; đoạn vào mỏ đi chung tuyến đường qua diện tích khai trường của Công ty TNHH khai thác khoáng sản Nam Hồng Hà (mục 1.6.3 Thiết kế được duyệt).',
    'Cấp điện: nguồn điện cấp cho mỏ lấy từ trạm biến áp 1.000 kVA đặt tại khu vực kho VLNCN của Công ty TNHH khai thác khoáng sản Nam Hồng Hà. Cấp nước: dẫn từ khe suối phía Tây Nam khai trường về các téc chứa trên mặt bằng bằng ống cao su Ø50 mm và Ø25 mm.',
    'Thông tin liên lạc: trên mặt đất sử dụng điện thoại di động (khu vực có sóng của các nhà mạng); trong lò, do các đường lò có chiều dài nhỏ, thông tin liên lạc thực hiện bằng đèn hiệu và lời nói trực tiếp (mục 1.6.3 Thiết kế được duyệt). Công ty quy định tín hiệu bằng đèn và còi theo mục IV.9 Phương án này.',
])

h2('3. Dân cư, nhà ở, công trình trong phạm vi bán kính 1.000 m (kể cả công trình ngầm)')
para('Dân cư trong vùng thưa thớt, chủ yếu là đồng bào dân tộc thiểu số, sống tập trung thành các điểm dân cư nhỏ ven đường, thung lũng và sườn đồi, cách xa khu vực mỏ. Khu vực mỏ có một suối chảy theo hướng Tây sang Đông dài khoảng 700 m, rộng 3 m đến 6 m; các cửa lò nằm cao hơn địa hình xung quanh nên nước mặt không ảnh hưởng đến hoạt động khai thác.')
para('Các nhà ở, công trình trong phạm vi bán kính 1.000 m tính từ các cửa lò và từ hình chiếu bằng của các gương nổ mìn như sau:', keep=True)
cap('Thống kê nhà ở, công trình trong phạm vi bán kính 1.000 m')
t = table([
    ['TT', 'Nhà ở, công trình', 'Chủ sở hữu', 'Khoảng cách đến vị trí nổ mìn gần nhất (m)', 'Ghi chú'],
    ['1', 'Nhà ở, khu dân cư', '-', ('Không có trong bán kính 1.000 m', 'x'), 'Đo đạc xác nhận'],
    ['2', 'Cơ sở khám bệnh, chữa bệnh; trường học; di tích lịch sử - văn hóa; khu bảo tồn thiên nhiên; công trình quốc phòng, an ninh; công trình quan trọng khác của quốc gia', '-', ('Không có', 'x'), 'Đo đạc xác nhận'],
    ['3', 'Khai trường, tuyến đường vận chuyển đi chung', 'Công ty TNHH khai thác khoáng sản Nam Hồng Hà', ('……', 'x'), 'Công trình sản xuất của tổ chức khác'],
    ['4', 'Kho VLNCN và trạm biến áp 1.000 kVA', 'Công ty TNHH khai thác khoáng sản Nam Hồng Hà', ('……', 'x'), 'Công trình sản xuất của tổ chức khác'],
    ['5', 'Công trình ngầm của tổ chức khác', '-', ('……', 'x'), 'Đo đạc xác nhận'],
    ['6', 'Nhà máy tuyển (cách khai trường khoảng 500 m về phía Đông Nam)', 'Công ty', '≈ 500', 'Công trình của Công ty'],
    ['7', 'Kho VLNCN, trạm máy nén khí, trạm quạt gió, bể lắng, kho chất thải nguy hại, mặt bằng các cửa lò', 'Công ty', ('……', 'x'), 'Công trình của Công ty'],
], widths=[Cm(0.9), Cm(6.0), Cm(3.4), Cm(3.1), Cm(2.6)], size=12, aligns=[C, L, L, C, L])
nosplit(t)
mixed([('Khoảng cách tại Bảng 7 được xác định bằng đo đạc thực tế tại hiện trường và thể hiện trên bản đồ tại Phụ lục 2 Phương án này.', True)])
para('Các công trình sản xuất của Công ty TNHH khai thác khoáng sản Nam Hồng Hà không thuộc các đối tượng khu dân cư, cơ sở khám bệnh, chữa bệnh, di tích, công trình quốc phòng, an ninh hoặc công trình quan trọng khác của quốc gia; Công ty thông báo cho Công ty TNHH khai thác khoáng sản Nam Hồng Hà về địa điểm, thời gian nổ mìn và quy ước tín hiệu, phối hợp canh gác trên tuyến đường đi chung theo mục IV.10 Phương án này.')
para('Theo mục 2.4.2 Chỉ dẫn kỹ thuật của Thiết kế được duyệt, khoảng cách an toàn đối với khu dân cư khi nổ mìn là lớn hơn 500 m.')

h2('4. Đặc điểm địa chất, tính chất cơ lý đất đá, điều kiện địa chất thủy văn và phân loại mỏ về khí, bụi nổ')
h3('a) Địa tầng và thân quặng')
para('Diện tích mỏ chỉ có mặt các đá thuộc hệ tầng Trạm Tấu, chủ yếu là đá phun trào ryolit màu xám, xám trắng, kiến trúc porphyr nền felsit, giàu thạch anh, felspat; chưa phát hiện biểu hiện hoạt động magma xâm nhập, kiến tạo. Trong diện tích mỏ tồn tại 01 thân quặng chì - kẽm (TQ.2) dạng mạch kéo dài theo phương Tây Bắc - Đông Nam, cắm về phía Tây Nam, thế nằm 240∠55 - 60°; chiều dài khoảng 110 m; chiều dày thật từ 1,48 m đến 5,80 m, trung bình 3,93 m; hệ số biến thiên chiều dày 72,21%. Khoáng vật quặng chủ yếu là pyrit, sphalerit, galenit, pyrotin; hàm lượng Pb + Zn trung bình 8,52% (mục 2.1.2 Thiết kế được duyệt).')
h3('b) Tính chất cơ lý của đá và quặng')
cap('Chỉ tiêu cơ lý đá ryolit vây quanh thân quặng')
t = table([
    ['Số hiệu mẫu', 'Khối lượng riêng (g/cm³)', 'Khối lượng thể tích tự nhiên (g/cm³)', 'σn khô gió (kG/cm²)', 'σn bão hòa (kG/cm²)', 'σk khô gió (kG/cm²)', 'Góc ma sát trong', 'Lực dính kết (kG/cm²)', 'f'],
    ['CL.04', '2,73', '2,71', '801', '755', '65', '37°26’', '132', '7,8'],
    ['CL.05', '2,66', '2,64', '1.035', '995', '70', '39°22’', '172', '9,3'],
    ['CL.06', '2,67', '2,66', '911', '864', '73', '38°40’', '152', '8,6'],
], widths=[Cm(1.8), Cm(1.8), Cm(2.0), Cm(1.7), Cm(1.7), Cm(1.7), Cm(1.8), Cm(1.8), Cm(1.1)], size=11)
nosplit(t, True)
src('Nguồn: Bảng 2.3 Thiết kế được duyệt (03 mẫu đá tầng ryolit bị thạch anh hóa).')
paras([
    '- Quặng (Bảng 2.6 Thiết kế được duyệt): độ ẩm tự nhiên 0,15%; độ hút nước 0,37%; khối lượng riêng 2,73 g/cm³; độ lỗ rỗng 0,73%; khối lượng thể tích tự nhiên 2,71 g/cm³, bão hòa 2,72 g/cm³; trọng lượng thể tích quặng dùng trong tính toán khai thác 3,26 tấn/m³ (Bảng 8.3 Thiết kế được duyệt).',
    '- Theo kết quả kiểm toán kết cấu chống (mục 8.2 Thiết kế được duyệt), các đường lò đi qua đá, quặng có cường độ kháng nén σn = 278 ÷ 532 kG/cm², cường độ kháng kéo σk = 13 ÷ 49 kG/cm²; hệ số ổn định nóc và hông các đường lò lớn hơn 4, thuộc loại vững chắc, trừ các đoạn cửa lò đào qua vùng đất đá phong hóa và khu vực ngã ba phải chống giữ.',
    '- Hệ số kiên cố của đá, quặng: f = 6 ÷ 10; hệ số kiên cố tính toán dùng cho khoan nổ mìn f = 8 (Bảng 8.10 Thiết kế được duyệt). Toàn bộ tính toán tại mục III Phương án này sử dụng f = 8.',
])
h3('c) Điều kiện địa chất thủy văn, địa chất công trình')
paras([
    '- Tầng chứa nước khe nứt trong hệ tầng Trạm Tấu là tầng nghèo nước; nguồn lộ xuất hiện ở các đới khe nứt với lưu lượng từ 0,001 l/s đến 0,1 l/s, dạng thấm rỉ; nước trong suốt, độ pH 6,60 - 6,82; kết quả quan trắc lỗ khoan không gặp túi nước và các hiện tượng bất thường về nước dưới đất.',
    '- Tầng đất phủ phân bố trên mặt đá gốc, chiều sâu từ 0,7 m đến 2,0 m, gồm sét, cát, sạn lẫn cục tảng và mùn thực vật, mềm rời dễ sập lở; đá ryolit bị phong hóa nhẹ ở phần trên, có thể tới độ sâu 2 - 3 m.',
    '- Các hiện tượng địa chất tự nhiên cần lưu ý khi nổ mìn: phong hóa (sâu 0,7 m đến 2 m), xâm thực bóc mòn, trượt lở ven suối và sườn dốc. Tại lò số 3 đã từng xảy ra hiện tượng sập nóc lò do áp lực đá vách lớn, vì chống yếu; các vị trí này đã được gia cố, chống bổ sung. Khi nổ mìn tại khu vực gần cửa lò đào qua đất đá phong hóa và các vị trí đã từng sập nóc, chỉ huy nổ mìn phải giảm lượng thuốc nạp các lỗ biên và kiểm tra vì chống trước, sau mỗi đợt nổ.',
])
h3('d) Phân loại mỏ về khí và bụi nổ')
para('Căn cứ Điều 52 QCVN 04:2017/BCT, kết quả phân tích mẫu hóa nhóm quặng và kết quả đo nồng độ H₂S trong đường lò: mỏ chì - kẽm khu vực xã Cao Phạ thuộc loại mỏ KHÔNG nguy hiểm về khí và bụi nổ (nồng độ lưu huỳnh nhỏ hơn 12% và nồng độ H₂S nhỏ hơn 6,6 ppm), được phép làm việc theo chế độ mỏ công tác bình thường (mục 10.1 Thiết kế được duyệt).')

h2('5. Hướng, trình tự nổ mìn, thay đổi điều kiện địa chất theo chu kỳ khai thác và ảnh hưởng đến công trình xung quanh')
paras([
    'Toàn bộ công tác nổ mìn của mỏ được thực hiện trong hầm lò, không có nổ mìn lộ thiên. Do đó không phát sinh đá văng ra ngoài phạm vi đường lò và không phát sinh sóng đập không khí lan truyền trên mặt đất. Yếu tố ảnh hưởng cần kiểm soát là chấn động do nổ mìn đối với các công trình trên mặt đất, độ ổn định của đường lò, vì chống và khí độc sau nổ mìn; các nội dung này được tính toán, quy định tại mục III.8 và mục IV Phương án này.',
    'Hướng nổ mìn: gương đào lò tiến theo hướng tim lò do bộ phận trắc địa xác định; gương lò chợ khấu theo hướng dốc từ dưới lên, trên từng đoạn dài 5,0 m, trong mỗi mức các cột khai thác tiến hành lần lượt từ trong ra phía lò xuyên vỉa.',
    'Trình tự khai thác theo Bảng 2 Phương án này: năm 2026 khai thác phần quặng còn lại của lò chợ cột số 03 và lò chợ cột số 04; năm 2027 khai thác phần quặng còn lại của lò chợ cột số 04 và lò chợ cột số 05; năm 2028 khai thác phần quặng còn lại của lò chợ cột số 05. Khi chuyển sang cột khai thác mới, chiều dày thân quặng (thay đổi từ 1,48 m đến 5,80 m) và góc dốc (55° đến 60°) có thể thay đổi; chỉ huy nổ mìn phải xem xét thực tế gương lò để điều chỉnh số hàng, số lỗ khoan và lượng thuốc nạp trong hộ chiếu nổ mìn, bảo đảm không vượt quá quy mô một đợt nổ và khối lượng thuốc nổ tức thời quy định tại mục III.6 Phương án này.',
])

# ================= III =================
h1('III. TÍNH TOÁN, LỰA CHỌN CÁC THÔNG SỐ KHOAN NỔ MÌN')
para('Các thông số khoan nổ mìn tại Phương án này được lấy thống nhất với mục 8.1, mục 8.2.4, Bảng 8.2, Bảng 8.3, Bảng 8.10 và các bản vẽ hộ chiếu thi công của Thiết kế được duyệt.')

h2('1. Lựa chọn đường kính lỗ khoan, chiều dài bước đào, chiều sâu lỗ khoan')
paras([
    '- Đường kính lỗ khoan: sử dụng thỏi thuốc đường kính dt = 32 mm, chọn đường kính lỗ khoan d = dt + 4 mm = 36 mm, phù hợp với choòng khoan đường kính 34 - 45 mm của búa khoan YT-24, YT-28 và bảo đảm nạp thỏi thuốc không bị kẹt.',
    '- Chiều cao tầng, đường cản chân tầng: không áp dụng do toàn bộ công tác nổ mìn thực hiện trong hầm lò; thay vào đó lựa chọn chiều dài một bước đào (tiến độ một chu kỳ khoan nổ): 0,80 m đối với lò có chống tiết diện đào 5,20 m²; 1,00 m đối với lò không chống, lò chân tầng, lò thượng có góc dốc lớn hơn 45° và phễu tháo quặng; 1,0 m đối với gương lò chợ.',
    '- Chiều sâu lỗ khoan: lỗ biên, lỗ phá 1,2 m; lỗ tạo rạch 1,4 m (sâu hơn các lỗ khác 0,2 m để tạo mặt tự do); chiều sâu lỗ mìn trung bình 1,27 m; hệ số sử dụng lỗ mìn 0,67 đối với lò có chống và 0,84 đối với lò không chống.',
])

h2('2. Lựa chọn chỉ tiêu thuốc nổ tính toán')
paras([
    'Chỉ tiêu thuốc nổ đơn vị đào lò được xác định theo công thức q = q₁ × f꜀ × v × e × d꜀ (kg/m³), trong đó q₁ = 0,1 × f là chỉ tiêu thuốc nổ tiêu chuẩn; f꜀ là hệ số cấu trúc đất đá; v là hệ số nén ép phụ thuộc diện tích gương; e là hệ số khả năng công nổ của thuốc nổ; d꜀ là hệ số ảnh hưởng của đường kính thỏi thuốc. Với f = 8, thỏi thuốc đường kính 32 mm, kết quả chỉ tiêu thuốc nổ đơn vị q = 3,20 kg/m³ cho các loại đường lò (Bảng 8.10 Thiết kế được duyệt).',
    'Chỉ tiêu thuốc nổ đơn vị khai thác lò chợ q = 0,1 × f × f꜀ × v × e × k_d = 0,1 × 8 × 2,1 × 6,5/(19,65)^0,5 × 380/280 × 0,95 = 3,2 kg/m³ (mục 8.1 Thiết kế được duyệt).',
])

h2('3. Thông số khoan nổ mìn đào lò chuẩn bị')
para('Tổng số lỗ khoan trên gương N = N_b + N_rf (lỗ biên, nền và lỗ phá, tạo rạch); lượng thuốc nổ cho một chu kỳ đào lò được chọn theo số thỏi thuốc nạp cho từng nhóm lỗ. Kết quả tính toán, lựa chọn cho từng loại đường lò như sau:', keep=True)
cap('Thông số cơ bản của hộ chiếu khoan nổ mìn đào chống lò')
W2 = [Cm(0.9), Cm(4.5), Cm(1.2), Cm(1.9), Cm(1.9), Cm(1.9), Cm(1.9), Cm(1.9)]
rows2 = [
    ['TT', 'Tên thông số', 'Đơn vị', 'Lò xuyên vỉa, dọc vỉa vận tải và thông gió', 'Lò thượng (α ≤ 45°)', 'Lò thượng (α > 45°)', 'Lò dọc vỉa phân tầng', 'Phễu tháo quặng'],
    ['1', 'Hình dạng tiết diện lò', '-', 'Hình thang', 'Hình thang', 'Chữ nhật', 'Hình thang', 'Chữ nhật'],
    ['2', 'Diện tích đào của lò', 'm²', '5,20', '4,20', '4,20', '3,60', '4,00'],
    ['3', 'Diện tích sử dụng', 'm²', '3,80', '3,24', '3,24', '2,60', '4,00'],
    ['4', 'Chiều rộng đường lò', 'm', '2,31', '2,01', '1,70', '1,85', '2,50'],
    ['5', 'Hệ số kiên cố của đá, quặng (f)', '-', '8', '8', '8', '8', '8'],
    ['6', 'Thuốc nổ sử dụng', '-', 'AĐ1', 'AĐ1', 'AĐ1', 'AĐ1', 'AĐ1'],
    ['7', 'Đường kính thỏi thuốc (dt)', 'mm', '32', '32', '32', '32', '32'],
    ['8', 'Đường kính lỗ khoan (d = dt + 4 mm)', 'mm', '36', '36', '36', '36', '36'],
    ['9', 'Khả năng sinh công của thuốc nổ (Pe)', 'cm³', '280', '315', '315', '340', '323'],
    ['10', 'Mật độ thuốc nổ', 'kg/m³', '1.100', '1.250', '1.250', '1.250', '1.250'],
    ['11', 'Chỉ tiêu thuốc nổ đơn vị (q)', 'kg/m³', '3,20', '3,20', '3,20', '3,20', '3,20'],
    ['12', 'Tiến độ một chu kỳ khoan nổ (Lo)', 'm', '0,80', '0,80', '1,00', '0,80', '1,00'],
    ['13', 'Tổng số lỗ khoan trên gương (N), trong đó:', 'lỗ', '26', '17', '17', '16', '19'],
    ['14', '- Số lỗ khoan biên, nền (Nb)', 'lỗ', '13', '12', '12', '11', '12'],
    ['15', '- Số lỗ khoan phá (Nf)', 'lỗ', '9', '4', '4', '4', '4'],
    ['16', '- Số lỗ khoan tạo rạch (Nr)', 'lỗ', '4', '1', '1', '1', '3'],
    ['17', 'Chiều sâu lỗ khoan biên, lỗ phá', 'm', '1,2', '1,2', '1,2', '1,2', '1,2'],
    ['18', 'Chiều sâu lỗ khoan tạo rạch', 'm', '1,4', '1,4', '1,4', '1,4', '1,4'],
    ['19', 'Khoảng cách giữa các lỗ mìn tạo biên (rb)', 'm', '0,5', '0,5', '0,5', '0,5', '0,5'],
    ['20', 'Số thỏi thuốc lỗ biên / phá / rạch', 'thỏi', '2 / 2,5 / 3', '2,5 / 3 / 3,5', '2,5 / 3 / 3,5', '2,5 / 2,75 / 3,25', '2,5 / 2,75 / 3,5'],
    ['21', 'Chiều dài bua lỗ biên / phá / rạch', 'm', '0,700 / 0,575 / 0,650', '0,575 / 0,450 / 0,525', '0,575 / 0,450 / 0,525', '0,575 / 0,5125 / 0,5875', '0,575 / 0,5125 / 0,525'],
    ['22', 'Lượng thuốc nổ một chu kỳ đào lò (Q)', 'kg', '12,10', '9,10', '9,10', '8,35', '10,30'],
    ['23', 'Số kíp nổ một chu kỳ (mỗi lỗ 01 kíp)', 'cái', '26', '17', '17', '16', '19'],
    ['24', 'Lượng thuốc nổ cho 01 m lò', 'kg/m', '15,13', '11,38', '9,10', '10,44', '10,30'],
    ['25', 'Số kíp nổ cho 01 m lò', 'cái/m', '33', '21', '18', '20', '20'],
]
t = table(rows2, widths=W2, size=11, aligns=[C, L, C, C, C, C, C, C])
nosplit(t)
src('Nguồn: Bảng 8.10 Thiết kế được duyệt. Khối lượng một thỏi thuốc 0,2 kg; chiều dài một thỏi 0,25 m.')
para('Lý lịch lỗ mìn chi tiết theo các bản vẽ hộ chiếu thi công của Thiết kế được duyệt (Phụ lục 3, Phụ lục 4, Phụ lục 5 Phương án này) như sau:', keep=True)
cap('Lý lịch lỗ mìn theo bản vẽ hộ chiếu thi công đào lò')
t = table([
    ['Gương lò', 'Nhóm lỗ', 'Số hiệu lỗ', 'Số lỗ', 'Chiều dài lỗ (m)', 'Góc nghiêng (độ)', 'Thuốc/lỗ (kg)', 'Thuốc nhóm (kg)', 'Kíp nhóm (cái)'],
    ['Lò dọc vỉa, xuyên vỉa có chống, Sđ = 5,20 m², Lo = 0,80 m (KT-DADC-CTN-06.1)', 'Tạo rạch', '1 - 4', '4', '1,4', '90', '0,6', '2,4', '4'],
    ['', 'Phá', '5 - 13', '9', '1,2', '90', '0,5', '4,5', '9'],
    ['', 'Biên, nền', '14 - 26', '13', '1,2', '78 - 80', '0,4', '5,2', '13'],
    ['', 'Cộng', '', '26', '32,0', '', '', '12,1', '26'],
    ['Lò dọc vỉa, xuyên vỉa không chống, Sđ = 3,60 m², Lo = 1,00 m (KT-DADC-CTN-06.2)', 'Tạo rạch', '1 - 3', '3', '1,4', '90', '0,8', '2,4', '3'],
    ['', 'Phá', '4 - 11', '8', '1,2', '90', '0,6', '4,8', '8'],
    ['', 'Biên, nền', '12 - 26', '15', '1,2', '85', '0,6', '9,0', '15'],
    ['', 'Cộng', '', '26', '31,8', '', '', '16,2', '26'],
    ['Lò chân tầng không chống, Sđ = 4,00 m², Lo = 1,00 m (KT-DADC-CTN-06.3)', 'Tạo rạch', '1 - 4', '4', '1,4', '90', '0,8', '3,2', '4'],
    ['', 'Phá', '5 - 8', '4', '1,2', '90', '0,6', '2,4', '4'],
    ['', 'Biên, nền', '9 - 23', '15', '1,2', '84', '0,5', '7,5', '15'],
    ['', 'Cộng', '', '23', '28,4', '', '', '13,1', '23'],
], widths=[Cm(4.2), Cm(1.6), Cm(1.4), Cm(1.0), Cm(1.4), Cm(1.6), Cm(1.5), Cm(1.6), Cm(1.5)], size=11,
    aligns=[L, L, C, C, C, C, C, C, C])
for r0 in (1, 5, 9):
    a = t.cell(r0, 0).merge(t.cell(r0 + 3, 0))
    txt = a.text.strip()
    for p in a.paragraphs[1:]:
        p._p.getparent().remove(p._p)
    a.paragraphs[0].runs[0].text = txt
    for rr in a.paragraphs[0].runs[1:]:
        rr._r.getparent().remove(rr._r)
    a.paragraphs[0].paragraph_format.alignment = L
nosplit(t)
src('Nguồn: Bảng lý lịch lỗ mìn trên các bản vẽ KT-DADC-CTN-06.1, 06.2, 06.3 Thiết kế được duyệt. Thuốc nổ AĐ1 thỏi Ø32 × 200 g × 250 mm; kíp nổ điện vi sai.')
paras([
    'Quy cách khoan: lỗ khoan tạo rạch khoan vuông góc với mặt gương, sâu hơn các lỗ khác 0,2 m để tạo mặt tự do đầu tiên; lỗ khoan phá khoan vuông góc với mặt gương; lỗ khoan biên khoan cách đường biên thiết kế 10 cm, nghiêng 78 - 85 độ ra phía ngoài đường biên để bảo đảm tiết diện lò sau khi nổ. Khoảng cách giữa các lỗ mìn tạo biên rb = 0,4 - 0,5 m. Khoan lần lượt các lỗ biên trước, lỗ nền, tiếp đến lỗ phá và lỗ tạo rạch; khoan xong lấy sạch phoi, đánh dấu miệng lỗ bằng que tre hoặc gỗ.',
    'Cấu trúc cột thuốc: nạp liên tục các thỏi thuốc đường kính 32 mm, chiều dài 0,25 m, khối lượng 0,2 kg/thỏi, tính từ đáy lỗ khoan; mìn mồi (thỏi thuốc có kíp) đặt tại thỏi thuốc trong cùng, kíp nổ lắp ngược hướng ra miệng lỗ; phần lỗ khoan còn lại nạp bua bằng hỗn hợp sét và cát, nạp chặt. Chiều dài cột thuốc bằng số thỏi nhân với 0,25 m; chiều dài bua không nhỏ hơn trị số tại Bảng 9 Phương án này và không nhỏ hơn 1/3 chiều dài lỗ mìn (mục 2.2.2 Chỉ dẫn kỹ thuật của Thiết kế được duyệt).',
    'Kiểm tra điều kiện bua: lỗ biên lò có chống dài 1,2 m nạp 2 thỏi (0,5 m) còn 0,7 m bua (58%); lỗ tạo rạch dài 1,4 m nạp 3 thỏi (0,75 m) còn 0,65 m bua (46%); lỗ biên lò không chống nạp 3 thỏi (0,75 m) còn 0,45 m bua (38%); các trường hợp đều lớn hơn 1/3 chiều dài lỗ mìn.',
])

h2('4. Thông số khoan nổ mìn khai thác lò chợ')
para('Chi phí thuốc nổ một chu kỳ tính toán Q = L꜀ × m × r × q = 30 × 3,93 × 1,0 × 3,2 = 377,3 kg; số lỗ khoan một chu kỳ N = (30/0,4 - 1) × 8 = 592 lỗ (mục 8.1 Thiết kế được duyệt). Thông số lựa chọn như sau:', keep=True)
cap('Thông số cơ bản của hộ chiếu khoan nổ mìn khai thác lò chợ')
rows3 = [
    ['TT', 'Tên thông số', 'Đơn vị', 'Giá trị'],
    ['1', 'Chiều dày trung bình thân quặng (m)', 'm', '3,93'],
    ['2', 'Góc dốc trung bình thân quặng', 'độ', '56'],
    ['3', 'Chiều dài lò chợ (Lc)', 'm', '30'],
    ['4', 'Chiều rộng một đợt nổ mìn', 'm', '5,0'],
    ['5', 'Tiến độ khấu gương một chu kỳ (r)', 'm', '1,0'],
    ['6', 'Diện tích gương nổ một đợt (5,0 × 3,93)', 'm²', '19,65'],
    ['7', 'Chỉ tiêu thuốc nổ đơn vị (q)', 'kg/m³', '3,2'],
    ['8', 'Đường kính thỏi thuốc / đường kính lỗ khoan', 'mm', '32 / 36'],
    ['9', 'Số hàng lỗ khoan trên gương', 'hàng', '8'],
    ['10', 'Khoảng cách giữa các hàng lỗ khoan', 'm', '0,5'],
    ['11', 'Khoảng cách giữa các lỗ khoan trong một hàng', 'm', '0,4'],
    ['12', 'Số lỗ khoan trong một hàng', 'lỗ', '74'],
    ['13', 'Tổng số lỗ khoan một chu kỳ khấu (8 × 74)', 'lỗ', '592'],
    ['14', 'Lượng thuốc nạp lỗ hàng 1 và hàng 8', 'kg/lỗ', '0,5'],
    ['15', 'Lượng thuốc nạp lỗ hàng 2 đến hàng 7', 'kg/lỗ', '0,7'],
    ['16', 'Lượng thuốc nổ một chu kỳ khấu (2 × 74 × 0,5 + 6 × 74 × 0,7)', 'kg', '384,8'],
    ['17', 'Số kíp nổ một chu kỳ khấu (mỗi lỗ 01 kíp)', 'cái', '592'],
    ['18', 'Số đợt nổ trong một chu kỳ khấu (30 m : 5 m)', 'đợt', '6'],
    ['19', 'Quy mô một đợt nổ (384,8 : 6)', 'kg', '64,1'],
    ['20', 'Số kíp nổ một đợt (592 : 6)', 'cái', '99'],
    ['21', 'Sản lượng quặng nổ mìn một chu kỳ khấu', 'tấn', '59,52'],
]
t = table(rows3, widths=[Cm(1.0), Cm(10.0), Cm(2.0), Cm(3.0)], size=12, aligns=[C, L, C, C])
nosplit(t)
src('Nguồn: mục 8.1, Bảng 8.2 và Bảng 8.3 Thiết kế được duyệt.')
para('Cấu trúc cột thuốc lò chợ: lỗ hàng 1 và hàng 8 nạp 2,5 thỏi (0,5 kg), lỗ hàng 2 đến hàng 7 nạp 3,5 thỏi (0,7 kg), nạp liên tục từ đáy lỗ, mìn mồi đặt tại thỏi trong cùng, kíp nổ lắp ngược; bua nạp chặt, chiều dài không nhỏ hơn 0,5 m (mục 8.1 Thiết kế được duyệt); chiều sâu lỗ khoan được ghi trong hộ chiếu nổ mìn bảo đảm điều kiện chiều dài bua này. Thứ tự nạp tiến hành từ vách sang trụ (lỗ hàng sát vách trước, lỗ hàng trụ sau).')

h2('5. Phương pháp nổ mìn, chủng loại vật liệu nổ công nghiệp, phương tiện khởi nổ và mạng nổ')
paras([
    '- Phương pháp nổ mìn: nổ mìn trong các lỗ khoan nhỏ, điều khiển nổ vi sai, khởi nổ bằng máy nổ mìn chuyên dụng cho hầm lò. Không áp dụng nổ mìn buồng, nổ mìn lỗ khoan lớn, nổ mìn ốp và nổ mìn đốt bằng dây cháy chậm.',
    '- Thuốc nổ: thuốc nổ Amonit AĐ1 và thuốc nổ nhũ tương dùng cho mỏ hầm lò (mục 8.2.1 Thiết kế được duyệt), thuộc Danh mục vật liệu nổ công nghiệp được phép sản xuất, kinh doanh, sử dụng tại Việt Nam ban hành kèm theo Phụ lục I Thông tư số 23/2024/TT-BCT, dùng cho mỏ hầm lò, công trình ngầm không có khí và bụi nổ. Thông số dùng trong tính toán là khả năng sinh công 280 ÷ 380 cm³, mật độ 1.100 ÷ 1.250 kg/m³, thỏi thuốc đường kính 32 mm, khối lượng 0,2 kg, chiều dài 0,25 m; khi lựa chọn loại thuốc nổ có thông số khác, Công ty tính lại chỉ tiêu thuốc nổ đơn vị và lượng thuốc nạp cho từng lỗ mìn, thể hiện trong hộ chiếu nổ mìn của đợt nổ tương ứng.',
    '- Kíp nổ: kíp nổ điện vi sai (bản vẽ hộ chiếu thi công) và kíp nổ vi sai phi điện (mục 2.2.2 Chỉ dẫn kỹ thuật của Thiết kế được duyệt), thuộc Danh mục nêu trên, dùng cho mỏ hầm lò, công trình ngầm không có khí và bụi nổ. Các quy định về đo điện trở, cường độ dòng điện gây nổ và đấu nối mạng nổ tại Phương án này áp dụng khi sử dụng kíp nổ điện; trường hợp sử dụng kíp nổ vi sai phi điện, Công ty thực hiện đấu nối theo hướng dẫn của nhà sản xuất và thể hiện sơ đồ mạng nổ trong hộ chiếu nổ mìn.',
    '- Phương tiện khởi nổ: máy nổ mìn BKM-1/100 (02 chiếc) hoặc máy nổ mìn chuyên dụng cho hầm lò có đặc tính kỹ thuật tương đương, được kiểm định theo quy định. Máy đo điện trở kíp và mạng nổ được kiểm định 01 lần/06 tháng.',
    '- Mạng nổ điện: các kíp trong một đợt nổ đấu nối tiếp theo sơ đồ đấu kíp tại bản vẽ hộ chiếu thi công; ở lò chợ, đấu nối theo trình tự từ đoạn nổ mìn trên xuống đoạn dưới, sau đó đấu nối tiếp hai đoạn với nhau. Số kíp của một đợt nổ lớn nhất là 99 kíp (gương lò chợ), không vượt quá khả năng khởi nổ 100 kíp mắc nối tiếp của máy nổ mìn BKM-1/100. Điện trở mạng nổ đo thực tế trước khi khởi nổ không được sai khác quá 10% so với trị số tính toán và không vượt quá điện trở mạch cho phép của máy nổ mìn sử dụng.',
])
para('- Công ty KHÔNG sử dụng dây cháy chậm và phương pháp nổ mìn đốt tại mỏ. Lý do: thân quặng có góc dốc trung bình 56 độ, các lò thượng của mỏ có góc dốc lớn hơn 45 độ, thuộc trường hợp không được nổ mìn bằng dây cháy chậm ở lò đứng, lò nghiêng có độ dốc trên 30 độ theo quy định tại QCVN 01:2019/BCT; đồng bộ thiết bị nổ mìn tại Bảng 8.9 Thiết kế được duyệt chỉ trang bị máy nổ mìn điện.', bold=True)
para('Trường hợp kết quả đo, phân tích khí mỏ xác định mỏ chuyển sang loại nguy hiểm về khí hoặc bụi nổ theo QCVN 04:2017/BCT thì phải chuyển sang sử dụng thuốc nổ an toàn và kíp nổ an toàn dùng cho hầm lò có khí và bụi nổ, đồng thời điều chỉnh Phương án này trước khi tiếp tục thực hiện.', italic=True)

h2('6. Quy mô một đợt nổ và khối lượng thuốc nổ tức thời lớn nhất')
para('Toàn bộ các đợt nổ được điều khiển vi sai, chia tối thiểu 05 cấp vi sai, mỗi cấp bố trí không quá 20 lỗ khoan. Đối với gương đào lò, bản vẽ hộ chiếu thi công sử dụng kíp vi sai số 1 (tạo rạch), số 3 (phá), số 5 (biên, nền); khi lập hộ chiếu nổ mìn, chỉ huy nổ mìn tách các nhóm lỗ để bảo đảm tối thiểu 05 cấp vi sai theo thứ tự: tạo rạch; phá; biên hông; biên nóc; nền. Quy mô một đợt nổ và khối lượng thuốc nổ tức thời lớn nhất của từng loại gương như sau:', keep=True)
cap('Quy mô một đợt nổ và khối lượng thuốc nổ tức thời lớn nhất')
t = table([
    ['TT', 'Loại gương nổ', 'Thuốc nổ một đợt (kg)', 'Kíp nổ một đợt (cái)', 'Số cấp vi sai tối thiểu', 'Thuốc nổ tức thời lớn nhất (kg)'],
    ['1', 'Gương lò chợ (một đoạn 5 m)', '64,1', '99', '05', '14,0 (20 lỗ × 0,7 kg)'],
    ['2', 'Lò dọc vỉa, xuyên vỉa có chống', '12,10', '26', '05', '≤ 5,2'],
    ['3', 'Lò dọc vỉa, xuyên vỉa không chống', '16,2', '26', '05', '≤ 9,0'],
    ['4', 'Lò chân tầng không chống', '13,1', '23', '05', '≤ 7,5'],
    ['5', 'Lò thượng, lò dọc vỉa phân tầng, phễu tháo quặng', '≤ 10,30', '≤ 19', '05', '≤ 6,0'],
], widths=[Cm(0.9), Cm(5.4), Cm(2.3), Cm(2.3), Cm(2.3), Cm(2.8)], size=12, aligns=[C, L, C, C, C, C])
nosplit(t, True)
paras([
    '- Quy mô một đợt nổ lớn nhất đối với gương lò chợ là 64,1 kg; đối với gương đào lò là 16,2 kg (lò dọc vỉa, xuyên vỉa không chống). Các trị số này không vượt quá quy mô một đợt nổ lớn nhất 64,1 kg (gương lò chợ) và 20,3 kg (gương đào lò) quy định tại Giấy phép sử dụng vật liệu nổ công nghiệp số 5248/GP-SCT.',
    '- Khối lượng thuốc nổ tức thời lớn nhất của mỏ là 14,0 kg (gương lò chợ); số cấp vi sai, số lỗ và khối lượng thuốc nổ của từng cấp được thể hiện cụ thể trong hộ chiếu nổ mìn của từng đợt nổ.',
    '- Quy mô một đợt nổ lớn nhất của mỏ Q = 64,1 kg được sử dụng để tính toán khoảng cách an toàn tại mục III.8 Phương án này.',
])

h2('7. Khối lượng vật liệu nổ công nghiệp sử dụng')
para('Khối lượng VLNCN được xác định trên cơ sở các chỉ tiêu tại Bảng 8.3 Thiết kế được duyệt và các chỉ tiêu đào lò chuẩn bị của Thiết kế điều chỉnh lần thứ nhất; do mỏ đã hoàn thành công tác xây dựng cơ bản (Bảng 3 Phương án này), không tính khối lượng VLNCN cho thi công đào các đường lò khai thông, mở vỉa và chuẩn bị thời điểm ban đầu. Mỗi lỗ mìn sử dụng 01 kíp nổ. Cụ thể:')
paras([
    'a) Chi phí thuốc nổ khai thác lò chợ cho 1.000 tấn quặng: C1 = 1.430 kg/1.000 tấn (Bảng 8.3 Thiết kế được duyệt).',
    'b) Chi phí kíp nổ khai thác lò chợ cho 1.000 tấn quặng: C3 = 2.200 cái/1.000 tấn (Bảng 8.3 Thiết kế được duyệt).',
    'c) Chi phí thuốc nổ đào lò chuẩn bị cho 1.000 tấn quặng: C2 = 20,3 × 69 = 1.401 kg/1.000 tấn (69 m lò chuẩn bị cho 1.000 tấn quặng và 20,3 kg thuốc nổ cho 01 m lò tiết diện đào 5,20 m² theo Thiết kế điều chỉnh lần thứ nhất).',
    'd) Chi phí kíp nổ đào lò chuẩn bị cho 1.000 tấn quặng: C4 = 26 × 69 = 1.794 cái/1.000 tấn (26 kíp nổ cho 01 m lò chuẩn bị theo Thiết kế điều chỉnh lần thứ nhất).',
    'đ) Tổng chi phí thuốc nổ cho 1.000 tấn quặng, có tính hệ số sử dụng hiệu quả của thuốc nổ trong lỗ khoan k = 0,5 (Thiết kế điều chỉnh lần thứ nhất):',
])
para('C = (C1 + C2) : k = (1.430 + 1.401) : 0,5 = 5.662 kg/1.000 tấn.', align=C, indent=Cm(0))
para('e) Tổng chi phí kíp nổ cho 1.000 tấn quặng: do mỗi lỗ mìn sử dụng 01 kíp nổ, số lỗ mìn tăng theo cùng tỷ lệ với lượng thuốc nổ nên áp dụng cùng hệ số k = 0,5:')
para('C’ = (C3 + C4) : k = (2.200 + 1.794) : 0,5 = 7.988 cái/1.000 tấn.', align=C, indent=Cm(0))
para('g) Với công suất khai thác 7.150 tấn/năm: khối lượng thuốc nổ 5.662 × 7,15 = 40.483 kg, làm tròn xuống 40.480 kg/năm; số lượng kíp nổ 7.988 × 7,15 = 57.114,2 cái, làm tròn 57.115 cái/năm. Phân bổ theo công đoạn như sau:', keep=True)
cap('Phân bổ khối lượng vật liệu nổ công nghiệp theo công đoạn trong 01 năm')
t = table([
    ['TT', 'Công đoạn', 'Thuốc nổ (kg/1.000 tấn)', 'Kíp nổ (cái/1.000 tấn)', 'Thuốc nổ (kg/năm)', 'Kíp nổ (cái/năm)'],
    ['1', 'Khai thác lò chợ', '1.430 : 0,5 = 2.860', '2.200 : 0,5 = 4.400', '20.449', '31.460'],
    ['2', 'Đào lò chuẩn bị', '1.401 : 0,5 = 2.802', '1.794 : 0,5 = 3.588', '20.034', '25.654'],
    ['', 'Cộng', '5.662', '7.988', '40.483 (làm tròn 40.480)', '57.114 (làm tròn 57.115)'],
], widths=[Cm(0.9), Cm(3.4), Cm(3.1), Cm(3.1), Cm(3.0), Cm(2.5)], size=12, aligns=[C, L, C, C, C, C])
nosplit(t, True)
para('Khối lượng VLNCN sử dụng lớn nhất theo tháng, quý, năm:', keep=True, space_before=3)
cap('Khối lượng vật liệu nổ công nghiệp sử dụng lớn nhất')
t = table([
    ['TT', 'Chủng loại vật liệu nổ công nghiệp', 'Đơn vị', 'Hằng năm', 'Hằng quý', 'Hằng tháng'],
    ['1', 'Thuốc nổ các loại (thuốc nổ Amonit AĐ1; thuốc nổ nhũ tương dùng cho mỏ hầm lò)', 'kg', '40.480', '10.120', '3.373'],
    ['2', 'Kíp nổ các loại (kíp nổ điện vi sai; kíp nổ vi sai phi điện)', 'cái', '57.115', '14.278', '4.759'],
    ['3', 'Dây nổ, dây cháy chậm', 'm', '0', '0', '0'],
], widths=[Cm(1.0), Cm(7.0), Cm(1.6), Cm(2.2), Cm(2.1), Cm(2.1)], size=12, aligns=[C, L, C, C, C, C])
nosplit(t, True)
src('Ghi chú: khối lượng hằng quý, hằng tháng chia đều từ khối lượng hằng năm và làm tròn xuống; khối lượng thực tế từng tháng theo tiến độ đào lò, khai thác nhưng không vượt khối lượng hằng năm.')
para('Kho VLNCN của Công ty có sức chứa tối đa 4.900 kg thuốc nổ và phụ kiện nổ tương ứng. Nhu cầu thuốc nổ lớn nhất trong một tháng là 3.373 kg, không vượt quá sức chứa cho phép của kho; số lượng VLNCN mỗi lần nhập kho và khối lượng tồn chứa tại mọi thời điểm không vượt quá sức chứa cho phép của kho.')
para('Tổng khối lượng VLNCN sử dụng đến hết thời hạn Giấy phép khai thác khoáng sản (ngày 07/10/2028):', keep=True)
cap('Khối lượng VLNCN sử dụng theo từng năm đến hết ngày 07/10/2028')
t = table([
    ['TT', 'Năm', 'Thuốc nổ các loại (kg)', 'Kíp nổ các loại (cái)', 'Dây nổ, dây cháy chậm (m)'],
    ['1', '2026', '13.493', '19.038', '0'],
    ['2', '2027', '40.480', '57.115', '0'],
    ['3', 'Đến hết ngày 07/10/2028', '30.360', '42.836', '0'],
    ['', 'Tổng cộng', '84.333', '118.989', '0'],
], widths=[Cm(1.0), Cm(5.4), Cm(3.3), Cm(3.3), Cm(3.0)], size=12)
nosplit(t, True)
src('Ghi chú: năm 2026 tính cho 04 tháng; từ ngày 01/01/2028 đến ngày 07/10/2028 tính cho 09 tháng.')

h2('8. Tính toán khoảng cách an toàn')
para('a) Khoảng cách an toàn về chấn động đối với công trình trên mặt đất', keep=True)
para('Áp dụng công thức tại Phụ lục 7 QCVN 01:2019/BCT: R꜀ = K꜀ × α × ∛Q (m); trong đó K꜀ là hệ số phụ thuộc tính chất nền đất của công trình cần bảo vệ, α là hệ số phụ thuộc chỉ số tác động nổ, Q là khối lượng thuốc nổ của một đợt nổ (kg). Lấy K꜀ × α = 7 (công trình nhà cấp IV, nền đất):')
paras([
    '- Gương lò chợ, Q = 64,1 kg: ∛Q = 4,0; R꜀ = 7 × 4,0 = 28,0 m.',
    '- Gương đào lò lớn nhất, Q = 16,2 kg: ∛Q = 2,53; R꜀ = 7 × 2,53 = 17,7 m.',
])
para('b) Khoảng cách an toàn về tác động của sóng đập không khí', keep=True)
para('Công tác nổ mìn được thực hiện hoàn toàn trong hầm lò kín, sóng đập không khí không lan truyền ra ngoài trời nên không áp dụng đối với công trình trên mặt đất. Trong hầm lò, người phải rút về vị trí an toàn theo quy định tại điểm d mục này và mục IV.5 Phương án này.')
para('c) Khoảng cách an toàn do đá văng', keep=True)
para('Không phát sinh đá văng ra ngoài phạm vi đường lò do toàn bộ đợt nổ được thực hiện trong hầm lò. Tại khu vực cửa lò, trong thời gian nổ mìn phải cấm người và phương tiện trong bán kính 50 m tính từ cửa lò của mức đang nổ mìn.')
para('d) Khoảng cách an toàn đối với người trong hầm lò', keep=True)
para('Theo mục 2.4.2 Chỉ dẫn kỹ thuật của Thiết kế được duyệt, khoảng cách an toàn đối với người trong hầm lò khi nổ mìn là tối thiểu 150 m đối với đường lò thẳng và tối thiểu 100 m đối với đường lò cong. Các trị số này lớn hơn khoảng cách tối thiểu 50 m quy định tại QCVN 01:2019/BCT đối với nổ mìn ở lò chợ, do đó Phương án lấy theo trị số của Thiết kế được duyệt. Trường hợp chiều dài đường lò từ gương nổ đến cửa lò nhỏ hơn các trị số trên, người phải rút ra ngoài cửa lò và đứng ngoài bán kính 50 m tính từ cửa lò.')
para('đ) Khoảng cách an toàn đối với thiết bị', keep=True)
para('Trước mỗi đợt nổ, toàn bộ búa khoan, đường ống khí nén mềm, goòng, cáp điện di động và dụng cụ tại gương phải được tháo và di chuyển ra ngoài phạm vi tối thiểu 50 m tính từ gương nổ hoặc đưa về vị trí có vì chống bảo vệ. Quạt gió cục bộ và đường ống gió được giữ nguyên để phục vụ thông gió sau nổ mìn. Cắt điện khu vực gương nổ trước giờ khởi nổ theo quy định tại mục IV.6 Phương án này.')
para('e) Tổng hợp và kết luận', keep=True)
cap('Tổng hợp khoảng cách an toàn khi nổ mìn')
t = table([
    ['TT', 'Loại khoảng cách an toàn', 'Trị số tính toán, quy định', 'Trị số áp dụng'],
    ['1', 'Chấn động đối với công trình trên mặt đất', 'R꜀ = 28,0 m (lò chợ); 17,7 m (đào lò)', '≥ 28,0 m'],
    ['2', 'Sóng đập không khí đối với công trình trên mặt đất', 'Không phát sinh (nổ trong hầm lò)', 'Không áp dụng'],
    ['3', 'Đá văng tại cửa lò (người, phương tiện)', '50 m tính từ cửa lò', '50 m'],
    ['4', 'Người trong hầm lò', 'QCVN 01:2019/BCT: 50 m; Thiết kế: 150 m lò thẳng, 100 m lò cong', '150 m / 100 m'],
    ['5', 'Thiết bị tại gương', 'Ngoài phạm vi 50 m hoặc nơi có vì chống bảo vệ', '50 m'],
    ['6', 'Khu dân cư', 'Chỉ dẫn kỹ thuật của Thiết kế: > 500 m', '> 500 m'],
], widths=[Cm(0.9), Cm(5.6), Cm(6.2), Cm(3.3)], size=12, aligns=[C, L, L, C])
nosplit(t)
para('Theo mục II.3 Phương án này, trong bán kính 1.000 m tính từ các cửa lò và từ hình chiếu bằng của các gương nổ mìn không có nhà ở, khu dân cư, cơ sở khám bệnh, chữa bệnh, di tích lịch sử - văn hóa, khu bảo tồn thiên nhiên, công trình quốc phòng, an ninh hoặc công trình quan trọng khác của quốc gia. Do đó khu vực nổ mìn của mỏ bảo đảm khoảng cách an toàn và không thuộc trường hợp quy định tại điểm d khoản 2 Điều 38 Luật Quản lý, sử dụng vũ khí, vật liệu nổ và công cụ hỗ trợ; Phương án này do Giám đốc Công ty phê duyệt theo quy định tại khoản 1 Điều 15 Thông tư số 23/2024/TT-BCT.', space_before=3)

h2('9. Thời gian nổ mìn')
paras([
    '- Buổi sáng: từ 7 giờ 00 đến 11 giờ 00.',
    '- Buổi chiều: từ 13 giờ 00 đến 18 giờ 00.',
    '- Không thực hiện khoan, nổ mìn từ 20 giờ 00 đến 6 giờ 00 sáng hôm sau.',
    '- Trong các khung giờ trên, nổ mìn được thực hiện theo chu kỳ sản xuất của từng gương, ngay sau khi kết thúc công tác khoan, nạp mìn, đấu nối mạng nổ, rút toàn bộ người ra vị trí an toàn và đặt đủ trạm gác theo mục IV.10 Phương án này. Thời điểm nổ mìn cụ thể của từng đợt do chỉ huy nổ mìn quyết định và được ghi trong hộ chiếu nổ mìn.',
    '- Không thực hiện nổ mìn khi hệ thống thông gió, chiếu sáng, thông tin liên lạc của mỏ không bảo đảm hoặc khi có mưa lớn, giông sét (mục IV.13 Phương án này).',
])
para('Trước khi nổ mìn lần đầu, Công ty thông báo bằng văn bản đến Ủy ban nhân dân xã Tú Lệ, Công an xã Tú Lệ và Công ty TNHH khai thác khoáng sản Nam Hồng Hà về địa điểm, thời gian hoạt động nổ mìn và quy ước tín hiệu cảnh báo.')

h2('10. Cung ứng, bảo quản và vận chuyển vật liệu nổ công nghiệp')
paras([
    '- Công ty mua VLNCN của tổ chức có Giấy phép kinh doanh VLNCN theo hợp đồng; đơn vị cung ứng vận chuyển và bàn giao tại kho VLNCN của Công ty tại xã Tú Lệ, tỉnh Lào Cai (trước đây là bản Kháo Nhà, xã Cao Phạ, huyện Mù Cang Chải, tỉnh Yên Bái), có biên bản bàn giao kèm theo.',
    '- Kho VLNCN của Công ty là kho nổi, cố định, cấp II, xây dựng trên diện tích đất khoảng 458 m², diện tích xây dựng 26,25 m², chia thành 02 ngăn (ngăn chứa thuốc nổ 12,24 m², ngăn chứa phụ kiện nổ 8,69 m²), sức chứa tối đa 4.900 kg thuốc nổ và phụ kiện nổ tương ứng; bệ để VLNCN xây cao hơn mặt nền kho 30 cm; cửa kho 02 lớp có khóa chống cắt; hàng rào bảo vệ khung thép lưới B40 cao 2,0 m, trên cùng 04 lượt dây thép gai cao trên 0,5 m; bể nước chữa cháy 10 m³, máy bơm chữa cháy, bể cát, bình chữa cháy; cột thu lôi chống sét cao 12,0 m, điện trở nối đất nhỏ hơn 10 Ω; camera quan sát cửa kho, hệ thống chiếu sáng và chòi canh gác trên đường vào kho (Thông báo số 945/TB-SCT). Kho được canh gác 24/24 giờ.',
    '- Việc xuất, nhập kho thực hiện theo QCVN 01:2019/BCT, có sổ sách theo dõi, kiểm đếm hằng ngày. VLNCN sử dụng không hết trong ca phải nhập lại kho ngay trong ngày, có xác nhận của chỉ huy nổ mìn và thủ kho.',
    '- Việc vận chuyển VLNCN từ kho đến nơi sử dụng trong hầm lò được thực hiện theo quy định tại mục IV.1 Phương án này và QCVN 01:2019/BCT. Trường hợp vận chuyển VLNCN trên đường bộ ngoài phạm vi mỏ, Công ty thực hiện theo Giấy phép vận chuyển VLNCN do cơ quan Công an có thẩm quyền cấp.',
])

# ================= IV =================
h1('IV. BIỆN PHÁP BẢO ĐẢM AN TOÀN KHI NỔ MÌN')
h2('1. An toàn khi bốc dỡ, bảo quản tạm và vận chuyển vật liệu nổ công nghiệp')
paras([
    '- Khu vực bốc dỡ phải có biển báo xác định giới hạn ngăn cách; người không có nhiệm vụ không được vào khu vực đã ngăn cách; có lực lượng bảo vệ theo quy định. Không bốc dỡ VLNCN khi có giông sét.',
    '- Vận chuyển từ kho đến nơi sử dụng trong hầm lò bằng ô tô, xe goòng chạy trên đường ray hoặc mang xách thủ công. Không vận chuyển thuốc nổ và phụ kiện nổ trong cùng một chuyến; không xếp các hòm, túi đựng VLNCN cao hơn thành toa xe goòng; không để goòng có VLNCN tự trôi theo độ dốc; không chở người, vật liệu khác cùng chuyến với VLNCN.',
    '- Vận chuyển VLNCN theo lò thượng, qua lò nối vào buồng khai thác được thực hiện thủ công, thuốc nổ và kíp nổ đựng trong hòm, túi riêng; người mang kíp nổ đi trước hoặc sau người mang thuốc nổ với khoảng cách không nhỏ hơn 10 m.',
    '- Thợ mìn, người phục vụ phải mang theo đèn ắc quy phòng nổ hoạt động tốt khi vận chuyển VLNCN trong hầm lò.',
    '- Khi bảo quản tạm tại nơi làm việc, VLNCN phải để trong hòm, thùng chứa theo Phụ lục 10 QCVN 01:2019/BCT, đặt tại vị trí cao không bị ngập nước, cách gương lò lớn hơn 30 m, dưới sự quản lý trực tiếp của thợ mìn hoặc người bảo vệ; kíp nổ để cách ly với thuốc nổ; số lượng không vượt quá nhu cầu 01 ca.',
])
h2('2. An toàn khi khoan lỗ mìn')
paras([
    '- Trước khi khoan phải thông gió, đo khí tại gương; kiểm tra tình trạng nóc lò, hông lò, củng cố vì chống của ca trước, cạy hết đá om, đá treo để tạo không gian làm việc an toàn; kiểm tra hệ thống khí nén, nước, cần khoan và các van an toàn.',
    '- Quản đốc hoặc cán bộ trực ca trực tiếp xem xét toàn bộ gương lò, đánh dấu vị trí lỗ khoan theo hộ chiếu bằng sơn hoặc vôi. Mỗi máy khoan bố trí hai người; khoan lần lượt các lỗ biên trước, lỗ nền, tiếp đến lỗ phá và lỗ tạo rạch; khi khoan bắt đầu bằng choòng ngắn, sau đó mới dùng choòng dài; khử bụi bằng nước trong quá trình khoan.',
    '- Nghiêm cấm khoan tiếp hoặc khoan mới vào lỗ mìn đã nạp thuốc, lỗ mìn câm hoặc đáy lỗ mìn cũ còn sót; không khoan khô; không khoan khi gương chưa được củng cố.',
    '- Khi bắt mép mở lò tuyệt đối không được nổ mìn mà phải cuốc thủ công để tạo gương; sau khi dựng xong các vì bắt mép, các vì tiếp theo mới được nổ mìn nhẹ theo chỉ đạo của trưởng ca, cán bộ trực ca hoặc phó quản đốc (mục 2.2.2 Chỉ dẫn kỹ thuật của Thiết kế được duyệt).',
    '- Khi các đường lò còn cách điểm bục từ 7 m đến 10 m, phải khoan thăm dò trước gương bằng choòng khoan dài từ 2,5 m đến 3,0 m để đề phòng sự cố bục nước, bục bùn.',
])
h2('3. An toàn khi nạp mìn')
paras([
    '- Trước khi nạp mìn phải kiểm tra lại nồng độ khí tại gương; chỉ được nạp mìn khi nồng độ khí trong giới hạn cho phép theo QCVN 04:2017/BCT (khí CH₄ không lớn hơn 1%) và không có hiện tượng xì khí; nếu không bảo đảm phải thông gió cho tới khi đạt yêu cầu.',
    '- Kiểm tra lại số lượng VLNCN, phương tiện nổ, bua, dụng cụ nạp theo hộ chiếu; bố trí người gác mìn tại tất cả các đường lò dẫn vào vị trí nổ mìn theo hộ chiếu; phát tín hiệu bắt đầu nạp mìn; di chuyển máy khoan và thiết bị ra xa khu vực nổ mìn.',
    '- Công tác nạp do 02 người thực hiện: một người nạp, một người chuẩn bị bua; thứ tự nạp như thứ tự khoan. Thổi sạch phoi khoan trong lỗ trước khi nạp; thỏi thuốc có kíp được chuẩn bị ngay tại gương; các thỏi thuốc và bua được nạp bằng gậy gỗ, không dùng dụng cụ kim loại; không đập, ép mạnh thỏi thuốc có kíp.',
    '- Bua làm bằng đất sét trộn cát theo tỷ lệ sét/cát = 1/3, nạp chặt, chiều dài không nhỏ hơn trị số ghi tại Bảng 9, Bảng 11 Phương án này và không nhỏ hơn 1/3 chiều dài lỗ mìn. Nạp xong mỗi lỗ, thợ mìn phải nối chập hai đầu dây kíp với nhau cho đến khi đấu vào mạng nổ.',
    '- Không nạp và nổ mìn trong gương lò có khoảng chưa chống lớn hơn quy định trong thiết kế chống lò hoặc khi vì chống ở gương đã bị hư hỏng.',
])
h2('4. An toàn khi đấu nối mạng nổ và khởi nổ')
paras([
    '- Chỉ được đấu nối mạng nổ sau khi đã nạp và lấp bua xong toàn bộ các phát mìn của một đợt nổ; trước khi đấu kíp điện chỉ có thợ mìn ở lại gương, những người còn lại phải ra khỏi gương.',
    '- Đấu nối theo sơ đồ đấu kíp trong hộ chiếu; ở lò chợ đấu từ đoạn nổ mìn trên xuống đoạn dưới, sau đó đấu nối tiếp hai đoạn với nhau. Sau khi đấu xong, thợ mìn kiểm tra lại toàn bộ bãi mìn: cách đấu nối, đối chiếu với hộ chiếu nổ mìn, kiểm tra các mối nối.',
    '- Đo điện trở mạng nổ bằng thiết bị đo chuyên dụng: nếu điện trở đo được bằng hoặc sai số không quá 10% so với kết quả tính toán thì mạng nổ đạt yêu cầu; sau khi đo phải tháo dây chính khỏi máy đo và đấu chập lại. Nếu không đạt phải kiểm tra lại cách đấu nối (mục 2.2.2 Chỉ dẫn kỹ thuật của Thiết kế được duyệt).',
    '- Sau khi hoàn tất các công việc trên mới đấu dây chính với mạng nổ và di chuyển về vị trí an toàn chuẩn bị khởi nổ. Trước khi khởi nổ phải kiểm tra lại nồng độ khí tại gương; chỉ phát tín hiệu nổ khi đã nhận được báo cáo mọi người đã rút hết và các trạm gác đã vào vị trí.',
    '- Sau khi nổ, tháo dây dẫn chính khỏi máy nổ mìn, đấu chập lại; thông gió tích cực tối thiểu 30 phút, đo khí bảo đảm an toàn mới thu hồi dây chính và kiểm tra bãi mìn.',
])
h2('5. An toàn khi nổ mìn trong hầm lò')
paras([
    'a) Trước khi bắt đầu nạp mìn, theo hiệu lệnh của thợ mìn, tất cả mọi người trong khu vực gương lò phải rút ra vị trí an toàn; vị trí an toàn phải được thông gió bình thường, tránh được đất đá văng và được chống đỡ chắc chắn.',
    'b) Khoảng cách an toàn đối với người khi nổ mìn trong hầm lò là tối thiểu 150 m đối với đường lò thẳng và tối thiểu 100 m đối với đường lò cong (mục III.8.d Phương án này); người phải ở khu vực ngược chiều đi của khí độc.',
    'c) Đối với các lò thượng, lò nghiêng có độ dốc lớn hơn 30 độ, chỉ được nổ mìn bằng kíp nổ vi sai; việc khởi nổ tiến hành từ nơi an toàn ngoài đường lò dốc. Nghiêm cấm nổ mìn bằng dây cháy chậm tại các đường lò này.',
    'd) Kể từ khi 02 gương lò còn cách nhau 20 m, không được nổ mìn đồng thời từ 02 gương đối diện; trước khi nạp mìn, người không có nhiệm vụ phải rút ra khỏi cả 02 gương. Khi 02 gương còn cách nhau 7,0 m, chỉ được tiến hành công tác ở một gương và phải khoan lỗ khoan thăm dò sâu hơn lỗ khoan từ 1,0 m trở lên.',
    'đ) Khi nổ mìn ở gương của một trong hai đường lò đào song song cách nhau không lớn hơn 20 m, tất cả mọi người phải rút ra khỏi cả 02 gương đến vị trí an toàn; chỉ được khởi nổ sau khi đã nhận được thông báo mọi người đã rút hết và đã đặt trạm gác bảo vệ.',
    'e) Không được nổ mìn khi trong khoảng 20 m kể từ vị trí nổ mìn đi ra ngoài còn đất đá chưa xúc hết, toa xe, đồ vật chiếm trên một phần ba tiết diện ngang của lò.',
    'g) Nổ mìn tại lò chợ: trong buồng khai thác phải duy trì lượng quặng lưu đủ làm sàn công tác; người rút ra theo lò nối về thượng cột và lò dọc vỉa phía gió sạch; cửa chắn, cũi lợn tại các lò tháo quặng phải được kiểm tra trước khi nổ.',
])
h2('6. An toàn khi nổ mìn điện')
paras([
    '- Không được bảo quản, vận chuyển kíp điện gần các nguồn thu, phát sóng điện từ tần số radio với khoảng cách nhỏ hơn khoảng cách quy định tại Phụ lục 6 QCVN 01:2019/BCT; cấm sử dụng thiết bị thu, phát sóng điện từ tần số radio cầm tay trong phạm vi bán kính 50 m khu vực nổ mìn bằng kíp điện.',
    '- Cắt điện toàn bộ thiết bị điện, cáp điện di động trong khu vực gương nổ trước khi đấu nối mạng nổ; chỉ đóng điện trở lại sau khi đã kiểm tra bãi mìn.',
    '- Toàn bộ kíp điện trong một mạng nổ phải cùng loại và cùng một nhà sản xuất; phải đo điện trở từng kíp trước khi sử dụng; sau khi đo, hai đầu dây phải được đấu chập lại cho đến khi đấu vào mạng nổ. Dụng cụ đo có dòng điện phát vào mạch đo không vượt quá 50 mA.',
    '- Mạng điện nổ mìn luôn phải có hai dây dẫn; cấm sử dụng nước, đất, đường ống kim loại, đường ray, dây cáp để làm một trong hai dây dẫn. Đầu dây nối mạng phải được cạo sạch, mối nối chặt và quấn băng cách điện. Cấm đấu mạng điện nổ mìn theo hướng đi từ nguồn điện đến các phát mìn.',
    '- Chìa khóa máy nổ mìn do chỉ huy nổ mìn giữ trong suốt thời gian từ khi chuẩn bị nạp đến khi khởi nổ; cấm giao chìa khóa cho người khác.',
    '- Cường độ dòng điện gây nổ phóng vào mỗi kíp không nhỏ hơn 1,0 A; không nhỏ hơn 1,3 A khi số kíp nổ đồng thời đến 300 chiếc và không nhỏ hơn 2,5 A khi khởi nổ bằng dòng điện xoay chiều. Số kíp mắc nối tiếp trong một đợt nổ không vượt quá khả năng khởi nổ của máy nổ mìn sử dụng.',
    '- Khi quay chìa khóa máy nổ mìn đến vị trí khởi nổ mà phát mìn không nổ, người khởi nổ phải tháo hai đầu dây dẫn chính ra khỏi nguồn điện, đấu chập lại và chỉ được vào kiểm tra bãi mìn sau ít nhất 05 phút.',
    '- Chỉ những thợ mìn đã qua đào tạo, huấn luyện và có ít nhất 01 năm kinh nghiệm làm việc với phương pháp nổ mìn điện mới được đấu, lắp mạng điện nổ mìn.',
])
h2('7. Thông gió và kiểm soát khí mỏ')
paras([
    '- Thông gió chung của mỏ theo phương pháp thông gió đẩy, trạm quạt chính đặt tại rãnh gió ở mặt bằng cửa lò vận tải; gió sạch theo lò xuyên vỉa, dọc vỉa vận tải vào khu đào lò và khai thác, gió bẩn theo lò dọc vỉa thông gió ra ngoài. Lưu lượng gió yêu cầu cho lò chợ 426 m³/phút (7,1 m³/s); cho mỗi gương lò chuẩn bị 159,6 m³/phút (2,66 m³/s); cho toàn mỏ 644,2 m³/phút (10,7 m³/s) (mục 10.1 Thiết kế được duyệt).',
    '- Gương đào lò độc đạo được thông gió bằng quạt cục bộ YBT-52-2 lưu lượng không nhỏ hơn 1,93 m³/s, hạ áp không nhỏ hơn 150 mmH₂O; quạt đặt phía đón luồng gió sạch, cách cửa lò hoặc đường lò cần thông gió tối thiểu 10 m; ống gió vải đường kính 600 mm, miệng ống cách gương không quá 8 m.',
    '- Lượng không khí sạch đưa vào mỗi gương lò có nổ mìn phải bảo đảm để sau khi thông gió không quá 30 phút, hàm lượng khí độc quy đổi sang cacbon oxit không lớn hơn 60 ppm và không vượt quá giới hạn cho phép theo QCVN 04:2017/BCT.',
    '- Sau khi nổ mìn phải thông gió tích cực bằng quạt cục bộ tối thiểu 30 phút; chỉ được đưa người vào làm việc sau khi đã đo kiểm tra hàm lượng ôxy, cacbonic, cacbon oxit bảo đảm quy định.',
    '- Bố trí cán bộ đo khí kiểm tra đầu ca và trong ca bằng máy đo khí, ghi kết quả vào sổ theo dõi; không bố trí người vào làm việc tại những vị trí chưa được kiểm tra đo khí. Các cửa gió, tường chắn gió tại những nơi ngừng khai thác phải được duy trì kín khít để không làm giảm lưu lượng gió đến gương nổ.',
])
h2('8. Biện pháp che chắn bảo vệ chống đá văng')
para('Toàn bộ công tác nổ mìn được thực hiện trong hầm lò, đá văng bị giới hạn trong phạm vi đường lò nên không áp dụng biện pháp che chắn miệng lỗ mìn bằng lưới thép và bao cát như đối với nổ mìn lộ thiên. Biện pháp bảo vệ tương ứng là: rút toàn bộ người về vị trí an toàn có vì chống chắc chắn theo mục IV.5 Phương án này; di chuyển thiết bị ra ngoài phạm vi 50 m theo mục III.8.đ; cấm người và phương tiện trong bán kính 50 m tính từ cửa lò của mức đang nổ mìn; đóng kín cửa gió, cửa chắn tại các ngã ba, ngã tư đường lò dẫn vào khu vực nổ mìn.')
h2('9. Tín hiệu cảnh báo an toàn và giờ nổ mìn')
paras([
    '- Quy ước 03 hiệu lệnh bằng còi: hiệu lệnh bắt đầu nạp mìn (01 hồi còi dài); hiệu lệnh khởi nổ (02 hồi còi ngắn); hiệu lệnh báo yên (03 hồi còi ngắn). Trong lò, hiệu lệnh được truyền bằng còi kết hợp đèn hiệu và lời nói trực tiếp giữa chỉ huy nổ mìn và các trạm gác.',
    '- Hiệu lệnh được phổ biến cho toàn bộ người lao động, ghi trong hộ chiếu nổ mìn và niêm yết tại các mặt bằng cửa lò, cổng kho VLNCN.',
    '- Giờ nổ mìn theo mục III.9 Phương án này.',
])
h2('10. Canh gác mìn')
paras([
    '- Bố trí trạm gác tại toàn bộ các ngã ba, ngã tư đường lò dẫn vào khu vực nổ mìn và tại cửa lò của mức đang nổ mìn. Mỗi trạm bố trí ít nhất 01 người, có băng gác, đèn và biển báo “Cấm vào”. Vị trí, số lượng trạm gác và người gác của từng đợt nổ được ghi cụ thể trong hộ chiếu nổ mìn (mục VII, VIII Mẫu hộ chiếu tại Phụ lục 1 Phương án này).',
    '- Trong thời gian nổ mìn, cấm người và phương tiện trong bán kính 50 m tính từ cửa lò của mức đang nổ mìn; khi cửa lò nằm gần tuyến đường đi chung với Công ty TNHH khai thác khoáng sản Nam Hồng Hà, bố trí người gác tạm dừng người, phương tiện trên tuyến đường.',
    '- Người gác chỉ được rời trạm gác khi có lệnh của chỉ huy nổ mìn sau khi đã kiểm tra bãi mìn bảo đảm an toàn.',
])
h2('11. Kiểm tra sau khi nổ mìn và xử lý mìn câm')
paras([
    '- Sau khi nổ mìn và thông gió theo mục IV.7, cán bộ trực ca cùng thợ mìn vào kiểm tra chất lượng nổ mìn và tình trạng gương lò, vì chống; cạy hết đá om, đá treo trước khi cho người vào làm việc.',
    '- Thợ mìn phải đếm số phát mìn đã nổ. Trường hợp không đếm được hoặc có phát mìn không nổ, chỉ được trở lại khu vực bãi mìn sau 15 phút kể từ khi phát mìn cuối cùng nổ và sau khi đã thông gió hết khói mìn.',
    '- Khi phát hiện mìn câm, thợ mìn phải báo ngay cho chỉ huy nổ mìn; cắm biển cảnh báo, giữ nguyên trạm gác. Nếu mìn điện bị câm, nếu tìm được hai đầu dây điện trong phát mìn thì phải lập tức đấu chập mạch lại.',
    '- Xử lý mìn câm theo chỉ đạo trực tiếp của chỉ huy nổ mìn: khoan một lỗ khoan song song cách lỗ mìn câm không nhỏ hơn 30 cm, bằng chiều sâu và đúng hướng với lỗ mìn câm, nạp thuốc và nổ để phá; để xác định hướng lỗ khoan phụ, cho phép moi lấy vật liệu nút lỗ mìn câm (bua) một khoảng 20 cm kể từ miệng lỗ. Tuyệt đối không được khoan trực tiếp vào lỗ mìn câm, không được dùng dụng cụ kim loại moi lấy thuốc nổ.',
    '- Sau khi nổ phát mìn để thủ tiêu mìn câm, thợ mìn phải kiểm tra kỹ đống đá để thu gom tất cả vật liệu nổ của phát mìn câm bị tung ra; chỉ cho người vào làm việc sau khi đã xử lý xong và được chỉ huy nổ mìn xác nhận an toàn.',
    '- Mọi trường hợp mìn câm phải được ghi vào hộ chiếu nổ mìn và sổ theo dõi; báo cáo Sở Công Thương theo quy định.',
])
h2('12. Củng cố gương, xúc bốc sau nổ mìn')
paras([
    '- Người thợ chính vào gương cạy om, người thợ phụ chuẩn bị vật liệu chống lò; cạy om từ ngoài vào trong, từ nền lò lên nóc lò bằng choòng và cuốc; khi vị trí làm việc đã bảo đảm an toàn mới tải bớt quặng, đá và dựng vì chống.',
    '- Khi xúc bốc không được quay lưng vào gương mà phải quay mặt vào gương để quan sát; cấm tổ chức xúc bốc tại gương lò khi đá om treo chưa được cạy sạch; tại lò thượng, dọc theo máng trượt cứ cách 15 m phải có cược giữ quặng.',
    '- Trong quá trình xúc bốc, nếu phát hiện VLNCN còn sót phải dừng ngay công việc, báo chỉ huy nổ mìn để thu gom, xử lý.',
])
h2('13. Xử lý, ứng phó khi gặp sự cố về thời tiết, cản trở khác trong các khâu khoan, nạp, nổ')
paras([
    '- Không thực hiện bốc dỡ, vận chuyển VLNCN trên mặt đất và nổ mìn khi có mưa lớn, giông sét; khi đang nạp mìn mà có giông sét, phải dừng nạp, rút người ra vị trí an toàn và cử người gác khu vực đã nạp.',
    '- Không nổ mìn khi hệ thống thông gió, chiếu sáng, thông tin liên lạc của mỏ không bảo đảm; khi mất điện quạt cục bộ phải dừng nạp mìn và rút người ra khỏi gương.',
    '- Khi khoan gặp lỗ mìn cũ, khe nứt lớn, hang hốc, nước chảy mạnh hoặc đất đá thay đổi so với hộ chiếu, phải dừng khoan, báo chỉ huy nổ mìn để điều chỉnh hộ chiếu trước khi tiếp tục.',
    '- Khi nạp mìn mà lỗ khoan bị tắc, sập vách lỗ không nạp đủ thuốc thì không được dùng lực ép thỏi thuốc; lỗ đó được đánh dấu, ghi vào hộ chiếu và xử lý theo chỉ đạo của chỉ huy nổ mìn.',
])
h2('14. Ứng cứu khẩn cấp')
para('Công ty lập Bản đánh giá nguy cơ rủi ro về an toàn theo Điều 14 và Phụ lục VI Thông tư số 23/2024/TT-BCT, rà soát hằng năm; xây dựng, phê duyệt Kế hoạch ứng cứu khẩn cấp theo Điều 16 và Phụ lục IX Thông tư số 23/2024/TT-BCT, tổ chức luyện tập, diễn tập hằng năm. Các tình huống khẩn cấp chủ yếu và biện pháp xử lý ban đầu như sau:', keep=True)
cap('Tình huống khẩn cấp và biện pháp xử lý ban đầu')
t = table([
    ['TT', 'Tình huống', 'Biện pháp xử lý ban đầu', 'Báo cáo'],
    ['1', 'Mất cắp, thất thoát VLNCN; xâm nhập trái phép kho', 'Phong tỏa hiện trường, kiểm đếm, tăng cường bảo vệ, phối hợp Công an truy tìm', 'Công an xã Tú Lệ, Công an tỉnh, Sở Công Thương trong 24 giờ'],
    ['2', 'Cháy tại kho VLNCN hoặc nơi bảo quản tạm', 'Báo động, sơ tán người ra ngoài vùng nguy hiểm, dùng phương tiện chữa cháy tại chỗ khi đám cháy chưa lan đến VLNCN, gọi lực lượng cứu hỏa 114', 'Công an, Sở Công Thương trong 24 giờ'],
    ['3', 'Nổ sớm, nổ không kiểm soát, người bị thương', 'Dừng mọi công việc, sơ cứu, đưa nạn nhân ra ngoài, gọi cấp cứu 115, giữ nguyên hiện trường', 'Công an, Sở Công Thương trong 24 giờ'],
    ['4', 'Mìn câm không xử lý được trong ca', 'Giữ trạm gác, cắm biển cấm, bàn giao bằng văn bản cho ca sau, chỉ huy nổ mìn trực tiếp xử lý', 'Ghi hộ chiếu, sổ theo dõi'],
    ['5', 'Sập lò, bục nước sau nổ mìn', 'Rút người theo đường thoát hiểm, kiểm đếm quân số, tổ chức cứu hộ theo phương án của mỏ', 'Cơ quan có thẩm quyền theo quy định'],
    ['6', 'Ngộ độc khí sau nổ mìn', 'Đưa nạn nhân ra nơi thoáng khí, sơ cứu, tăng cường thông gió, đo khí trước khi vào lại', 'Cơ quan có thẩm quyền theo quy định'],
], widths=[Cm(0.9), Cm(4.0), Cm(7.2), Cm(3.9)], size=12, aligns=[C, L, L, L])
pass
para('Thông tin liên lạc khi xảy ra sự cố: trên mặt đất bằng điện thoại di động; trong lò bằng đèn hiệu, còi và lời nói trực tiếp. Danh bạ liên lạc của Giám đốc, người quản lý VLNCN, chỉ huy nổ mìn, Công an xã Tú Lệ, Ủy ban nhân dân xã Tú Lệ, Sở Công Thương được niêm yết tại kho VLNCN và các mặt bằng cửa lò.', space_before=3)
h2('15. Tăng cường an ninh, an toàn')
paras([
    '- Duy trì canh gác kho VLNCN 24/24 giờ, camera quan sát cửa kho, hệ thống chiếu sáng hàng rào; kiểm đếm VLNCN xuất, nhập, tồn hằng ngày; đối chiếu số lượng VLNCN đã sử dụng với hộ chiếu nổ mìn.',
    '- Người không có nhiệm vụ không được vào khu vực kho, nơi bảo quản tạm và khu vực nạp, nổ mìn; cấm mang lửa, vật dụng phát lửa vào kho và nơi có VLNCN.',
    '- VLNCN thừa, kém phẩm chất được nhập lại kho, lập biên bản và xử lý theo quy định; không tự tiêu hủy khi chưa bảo đảm điều kiện theo QCVN 01:2019/BCT.',
])

# ================= V =================
h1('V. TỔ CHỨC THỰC HIỆN')
h2('1. Trình tự thực hiện và thủ tục kiểm soát các bước')
para('Mỗi đợt nổ mìn phải lập hộ chiếu nổ mìn theo Mẫu số 02 Phụ lục VIII Thông tư số 23/2024/TT-BCT (khung áp dụng tại mỏ nêu tại Phụ lục 1 Phương án này) trên cơ sở Phương án này; nghiêm cấm thực hiện nổ mìn khi chưa có hộ chiếu nổ mìn được duyệt. Trình tự và thủ tục kiểm soát các bước như sau:', keep=True)
cap('Trình tự thực hiện và kiểm soát các bước của một đợt nổ mìn')
t = table([
    ['Bước', 'Nội dung công việc', 'Người thực hiện', 'Người kiểm tra, xác nhận', 'Hồ sơ ghi chép'],
    ['1', 'Lập hộ chiếu nổ mìn cho gương nổ', 'Chỉ huy nổ mìn', 'Người quản lý VLNCN duyệt', 'Hộ chiếu nổ mìn'],
    ['2', 'Lĩnh VLNCN tại kho theo hộ chiếu', 'Thợ mìn', 'Thủ kho, chỉ huy nổ mìn', 'Phiếu xuất kho, sổ kho'],
    ['3', 'Kiểm tra gương, đo khí, củng cố', 'Cán bộ trực ca, thợ lò', 'Chỉ huy nổ mìn', 'Sổ đo khí, sổ giao ca'],
    ['4', 'Đánh dấu, khoan lỗ mìn', 'Tổ khoan', 'Cán bộ trực ca', 'Mục V hộ chiếu'],
    ['5', 'Đặt trạm gác, phát tín hiệu nạp mìn', 'Người gác mìn', 'Chỉ huy nổ mìn', 'Mục VII hộ chiếu'],
    ['6', 'Nạp mìn, lấp bua', 'Thợ mìn (02 người/nhóm)', 'Chỉ huy nổ mìn', 'Mục V hộ chiếu'],
    ['7', 'Đấu nối, đo điện trở mạng nổ', 'Thợ mìn', 'Chỉ huy nổ mìn', 'Mục III hộ chiếu'],
    ['8', 'Rút người, phát tín hiệu, khởi nổ', 'Chỉ huy nổ mìn', 'Chỉ huy nổ mìn', 'Mục VI hộ chiếu'],
    ['9', 'Thông gió, đo khí, kiểm tra bãi mìn, xử lý mìn câm', 'Thợ mìn, cán bộ trực ca', 'Chỉ huy nổ mìn', 'Mục XI hộ chiếu, sổ theo dõi'],
    ['10', 'Phát tín hiệu báo yên, thu hồi trạm gác', 'Chỉ huy nổ mìn', 'Chỉ huy nổ mìn', 'Mục VI hộ chiếu'],
    ['11', 'Nhập lại kho VLNCN thừa', 'Thợ mìn', 'Thủ kho, chỉ huy nổ mìn', 'Mục IX hộ chiếu, sổ kho'],
], widths=[Cm(1.2), Cm(5.0), Cm(3.3), Cm(3.3), Cm(3.2)], size=12, aligns=[C, L, L, L, L])
nosplit(t)
h2('2. Trách nhiệm của từng cá nhân, từng nhóm')
paras([
    '- Người quản lý về VLNCN: tổ chức thực hiện, kiểm tra, giám sát toàn bộ công tác quản lý, bảo quản, vận chuyển và sử dụng VLNCN; duyệt hộ chiếu nổ mìn; trình Giám đốc Công ty phê duyệt, điều chỉnh Phương án này; chịu trách nhiệm về chế độ báo cáo.',
    '- Chỉ huy nổ mìn: lập hộ chiếu nổ mìn; phân công người khoan, nạp, gác mìn; trực tiếp chỉ huy các khâu nạp, đấu nối mạng nổ, khởi nổ, kiểm tra sau nổ mìn và xử lý mìn câm; giữ chìa khóa máy nổ mìn; xác nhận VLNCN thừa trả về kho.',
    '- Nhóm khoan (02 người/máy khoan): khoan đúng vị trí, chiều sâu, góc nghiêng theo hộ chiếu; báo ngay khi phát hiện lỗ mìn cũ, mìn câm, điều kiện địa chất bất thường.',
    '- Nhóm nạp mìn (thợ mìn, 02 người/nhóm): nạp đúng lượng thuốc, cấu trúc cột thuốc, chiều dài bua; đấu chập đầu dây kíp; đấu nối mạng theo sơ đồ.',
    '- Người gác mìn: có mặt tại trạm gác trước khi phát tín hiệu nạp mìn, không cho người, phương tiện vào khu vực nguy hiểm; chỉ rời trạm khi có lệnh của chỉ huy nổ mìn.',
    '- Nhóm xử lý sau nổ mìn (thợ mìn, cán bộ trực ca): đo khí, kiểm tra bãi mìn, xử lý mìn câm, cạy om, củng cố gương trước khi bàn giao cho nhóm xúc bốc.',
    '- Thủ kho: quản lý xuất, nhập, tồn kho; lập và lưu sổ sách theo QCVN 01:2019/BCT.',
    '- Chỉ những người có Giấy chứng nhận huấn luyện kỹ thuật an toàn VLNCN còn hiệu lực mới được tham gia các công việc liên quan đến VLNCN; người quản lý, chỉ huy nổ mìn, thợ mìn, thủ kho phải bảo đảm trình độ chuyên môn theo Điều 4 Nghị định số 181/2024/NĐ-CP.',
])
para('3. Nhân sự trực tiếp thực hiện Phương án này (theo Danh sách cán bộ, công nhân liên quan đến VLNCN tháng 8 năm 2026 của Công ty):', bold=True, keep=True)
cap('Danh sách nhân sự thực hiện Phương án')
t = table([
    ['TT', 'Họ và tên', 'Năm sinh', 'Chức danh', 'Trình độ chuyên môn', 'Số GCN huấn luyện KTAT'],
    ['1', 'Nguyễn Đình Khương', '1979', 'Người quản lý', 'Đại học Mỏ - Địa chất', '136/SCT-2025'],
    ['2', 'Nguyễn Hữu Trực', '1966', 'Chỉ huy nổ mìn', 'Cao đẳng mỏ địa chất', '135/SCT-2025'],
    ['3', 'Hoàng Văn Hưng', '1988', 'Chỉ huy nổ mìn', 'Cao đẳng công nghệ kỹ thuật hóa học', '137/SCT-2025'],
    ['4', 'Vũ Khắc Hòa', '1973', 'Thủ kho', 'Sơ cấp', '59/SCT-2024'],
    ['5', 'Lường Văn Hóa', '1989', 'Thợ mìn', 'Sơ cấp', '25/GCN-SCT'],
    ['6', 'Giàng A Hồng', '1994', 'Thợ mìn', 'Sơ cấp', '141/SCT-2025'],
    ['7', 'Lý A Tủa', '1993', 'Thợ mìn', 'Sơ cấp', '26/GCN-SCT'],
    ['8', 'Nguyễn Văn Hồng', '1979', 'Thợ mìn - Gác', 'Sơ cấp', '376/GCN-SCT'],
    ['9', 'Giàng A Phà', '1997', 'Thợ mìn - Gác', 'Sơ cấp', '142/SCT-2025'],
    ['10', 'Hoàng Anh Tuấn', '1997', 'Thợ mìn - Bảo vệ', 'Sơ cấp', '24/GCN-SCT'],
    ['11', 'Hờ A Tu', '1997', 'Thợ mìn - Bảo vệ', 'Sơ cấp', '375/GCN-SCT'],
    ['12', 'Giàng A Dì', '1992', 'Thợ mìn - Bảo vệ', 'Sơ cấp', '374/GCN-SCT'],
], widths=[Cm(0.9), Cm(3.8), Cm(1.6), Cm(3.0), Cm(4.0), Cm(2.7)], size=12, aligns=[C, L, C, L, L, C])
nosplit(t)
src('Chỉ huy nổ mìn Nguyễn Hữu Trực được bổ nhiệm tại Quyết định số 11/QĐ-BN ngày 01/5/2025; chỉ huy nổ mìn Hoàng Văn Hưng được bổ nhiệm tại Quyết định số 01/QĐ-BN ngày 03/6/2024.')
h2('4. Ghi chép, báo cáo')
paras([
    '- Mọi sự kiện bất thường trong đợt nổ mìn, kể cả khi chưa đến mức xảy ra sự cố (mìn câm, nổ không hết, đá văng bất thường, vì chống bị đánh đổ, khí độc vượt giới hạn, thời gian thông gió kéo dài) phải được ghi vào mục XI hộ chiếu nổ mìn và sổ theo dõi; các ghi chép về sự cố (nếu có) được lưu cùng hộ chiếu.',
    '- Báo cáo định kỳ tình hình sử dụng VLNCN gửi Sở Công Thương theo Mẫu số 02 Phụ lục X Thông tư số 23/2024/TT-BCT trước ngày 18 tháng 6 (báo cáo sáu tháng) và trước ngày 18 tháng 12 (báo cáo năm); thời gian chốt số liệu từ ngày 15 tháng 12 năm trước đến ngày 14 tháng 6 hoặc ngày 14 tháng 12 của kỳ báo cáo.',
    '- Báo cáo đột xuất theo Mẫu số 04 Phụ lục X Thông tư số 23/2024/TT-BCT: trong 24 giờ kể từ khi phát hiện xâm nhập trái phép khu vực tồn trữ, mất cắp, thất thoát hoặc tai nạn, sự cố VLNCN (gửi cơ quan Công an và Sở Công Thương); trong 48 giờ kể từ khi chấm dứt hoạt động VLNCN (gửi Sở Công Thương); theo yêu cầu của cơ quan có thẩm quyền.',
    '- Hộ chiếu nổ mìn, sổ xuất nhập kho, sổ đo khí, sổ theo dõi mìn câm được lưu giữ tại mỏ để phục vụ kiểm tra.',
])
h2('5. Giám sát ảnh hưởng của nổ mìn')
para('Công ty tổ chức giám sát ảnh hưởng của nổ mìn đến đường lò, vì chống và các công trình, nhà ở của tổ chức, cá nhân xung quanh; tiếp nhận, giải quyết phản ánh và bồi thường thiệt hại (nếu có) theo quy định của pháp luật.')
h2('6. Kỷ luật nội bộ')
para('Cá nhân, bộ phận vi phạm Phương án này, hộ chiếu nổ mìn hoặc các quy định về an toàn VLNCN bị đình chỉ ngay công việc liên quan đến VLNCN, xử lý kỷ luật theo nội quy lao động của Công ty; trường hợp gây hậu quả bị xử lý theo quy định của pháp luật.')
h2('7. Hiệu lực, sửa đổi, bổ sung Phương án')
paras([
    '- Phương án này có hiệu lực kể từ ngày được Giám đốc Công ty phê duyệt đến hết ngày 07/10/2028 (thời hạn của Giấy phép khai thác khoáng sản số 680/GP-UBND ngày 07/4/2020 của Ủy ban nhân dân tỉnh Yên Bái).',
    '- Khi có thay đổi về thiết kế, quy mô khai thác, chủng loại VLNCN, điều kiện an toàn hoặc kết quả đo đạc khoảng cách thực tế đến nhà ở, công trình xung quanh, Phương án phải được rà soát, sửa đổi, bổ sung và phê duyệt lại trước khi tiếp tục thực hiện; văn bản phê duyệt sửa đổi, bổ sung ghi rõ ngày sửa đổi, bổ sung.',
])
h2('8. Người lập, người duyệt Phương án')
para('Người lập Phương án: ông Nguyễn Hữu Trực, Chỉ huy nổ mìn của Công ty. Người phê duyệt Phương án: ông Trần Quang Vinh, Giám đốc Công ty Cổ phần Kim Thành. Phương án không thuộc trường hợp phải được cơ quan có thẩm quyền phê duyệt theo điểm d khoản 2 Điều 38 Luật Quản lý, sử dụng vũ khí, vật liệu nổ và công cụ hỗ trợ; lý do nêu tại mục III.8.e Phương án này.')
para('Trên đây là Phương án nổ mìn khai thác quặng chì - kẽm bằng phương pháp hầm lò tại mỏ chì - kẽm khu vực xã Tú Lệ, tỉnh Lào Cai của Công ty Cổ phần Kim Thành. Công ty cam kết tổ chức thực hiện đúng các nội dung của Phương án và các quy định của pháp luật về quản lý, sử dụng VLNCN./.', space_before=6, keep=True)

sp = para('', keep=True)
sg = doc.add_table(rows=1, cols=2)
sg.alignment = WD_TABLE_ALIGNMENT.CENTER
set_fixed(sg, [Cm(8.0), Cm(8.0)])
sg.rows[0]._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
for j, (l1, l2) in enumerate([
    ('PHÊ DUYỆT\nGIÁM ĐỐC CÔNG TY', 'Trần Quang Vinh'),
    ('NGƯỜI LẬP PHƯƠNG ÁN\nCHỈ HUY NỔ MÌN', 'Nguyễn Hữu Trực'),
]):
    cell = sg.cell(0, j)
    cell.width = Cm(8.0)
    p = cell.paragraphs[0]
    p.paragraph_format.alignment = C
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.keep_with_next = True
    add_run(p, l1, bold=True, size=13)
    for _ in range(2):
        q = cell.add_paragraph()
        q.paragraph_format.first_line_indent = Cm(0)
        q.paragraph_format.keep_with_next = True
        q.paragraph_format.line_spacing = 1.0
    q = cell.add_paragraph()
    q.paragraph_format.alignment = C
    q.paragraph_format.first_line_indent = Cm(0)
    add_run(q, l2, bold=True, size=13)

# ================= PHỤ LỤC 1: khung hộ chiếu =================
new_section(False)
para('PHỤ LỤC 1', bold=True, align=C, indent=Cm(0))
para('KHUNG HỘ CHIẾU NỔ MÌN HẦM LÒ ÁP DỤNG TẠI MỎ', bold=True, align=C, indent=Cm(0))
para('(Theo Mẫu số 02 Phụ lục VIII Thông tư số 23/2024/TT-BCT; kèm theo Phương án nổ mìn khai thác quặng chì - kẽm bằng phương pháp hầm lò tại mỏ chì - kẽm khu vực xã Tú Lệ)', italic=True, align=C, indent=Cm(0), size=13, space_after=6)
paras([
    'Đơn vị: Công ty Cổ phần Kim Thành. Công trường, phân xưởng: ……',
    'HỘ CHIẾU NỔ MÌN HẦM LÒ số: ……/……/20……, theo Phương án nổ mìn được Giám đốc Công ty phê duyệt ngày …… tháng …… năm ……',
    'I. Vị trí nổ: gương (lò chợ cột …… / lò dọc vỉa, xuyên vỉa, thượng, chân tầng mức ……), cửa lò số ……, mức ……',
    'II. Đất đá loại: ryolit bị thạch anh hóa / quặng chì - kẽm; hệ số kiên cố f = ……; tình trạng nứt nẻ, nước: ……',
    'III. Sơ đồ phân bố lỗ khoan của gương nổ, nạp thuốc và đấu nối: theo bản vẽ hộ chiếu thi công tương ứng (Phụ lục 3, Phụ lục 4, Phụ lục 5) hoặc sơ đồ lò chợ 8 hàng lỗ; ghi rõ số cấp vi sai (tối thiểu 05 cấp), điện trở mạng nổ tính toán và đo thực tế.',
    'IV. Vật liệu nổ sử dụng trong ca: thuốc nổ …… kg; kíp nổ điện vi sai …… cái (theo từng số vi sai); kíp nổ vi sai phi điện …… cái.',
])
para('V. Bảng lý lịch lỗ mìn:', keep=True)
t = table([
    ['Nhóm lỗ', 'Số lỗ', 'Chiều sâu lỗ (m)', 'Góc nghiêng (độ)', 'Thuốc/lỗ (kg)', 'Kíp/lỗ (cái)', 'Tổng thuốc (kg)', 'Tổng kíp (cái)', 'Số vi sai'],
    ['Tạo rạch', '', '', '', '', '1', '', '', ''],
    ['Phá', '', '', '', '', '1', '', '', ''],
    ['Biên hông', '', '', '', '', '1', '', '', ''],
    ['Biên nóc', '', '', '', '', '1', '', '', ''],
    ['Nền', '', '', '', '', '1', '', '', ''],
    ['Cộng', '', '', '', '', '', '', '', ''],
], widths=[Cm(2.2), Cm(1.4), Cm(1.8), Cm(1.8), Cm(1.8), Cm(1.6), Cm(1.8), Cm(1.8), Cm(1.8)], size=11)
nosplit(t, True)
paras([
    'VI. Quy định hiệu lệnh nổ mìn: bắt đầu nạp mìn - 01 hồi còi dài; khởi nổ - 02 hồi còi ngắn; báo yên - 03 hồi còi ngắn.',
])
para('VII. Phân công gác mìn:', keep=True)
t = table([
    ['STT', 'Họ và tên', 'Chức vụ', 'Tổ, đội', 'Trạm gác số', 'Ký nhận'],
    ['1', '', '', '', '', ''],
    ['2', '', '', '', '', ''],
    ['3', '', '', '', '', ''],
], widths=[Cm(1.2), Cm(4.4), Cm(2.6), Cm(2.4), Cm(2.4), Cm(3.0)], size=11)
nosplit(t, True)
paras([
    'VIII. Sơ đồ vị trí nổ mìn, trạm gác mìn, nơi tránh mìn (cách gương tối thiểu 150 m lò thẳng, 100 m lò cong), vị trí khởi nổ: ……',
    'IX. Vật liệu nổ thừa trả về kho: thuốc nổ …… kg; kíp nổ …… cái. Chỉ huy nổ mìn ký xác nhận: ……',
    'X. Biện pháp kỹ thuật an toàn: theo mục IV Phương án nổ mìn; kết quả đo khí trước khi nạp mìn, trước khi khởi nổ, sau khi nổ mìn: ……',
    'XI. Đánh giá kết quả nổ mìn: 1. Đánh giá công tác thực hiện hộ chiếu khoan: …… 2. Đánh giá kết quả nổ mìn (số phát nổ/số phát nạp, mìn câm, sự kiện bất thường): ……',
])
para('', keep=True)
sg2 = doc.add_table(rows=1, cols=3)
sg2.alignment = WD_TABLE_ALIGNMENT.CENTER
set_fixed(sg2, [Cm(5.3), Cm(5.3), Cm(5.4)])
for j, l1 in enumerate(['NGƯỜI LẬP HỘ CHIẾU\n(Ký và ghi rõ họ tên)', 'CHỈ HUY NỔ MÌN\n(Ký và ghi rõ họ tên)', 'NGƯỜI QUẢN LÝ DUYỆT\n(Ký và ghi rõ họ tên)']):
    cell = sg2.cell(0, j)
    p = cell.paragraphs[0]
    p.paragraph_format.alignment = C
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(6)
    add_run(p, l1, bold=True, size=12)

# ================= PHỤ LỤC 2-5: bản vẽ =================
from docx.shared import Cm as CM2
for no, img, ttl in [
    (2, os.path.join(IMG_DIR, 's-06.jpg'), 'BẢN ĐỒ RANH GIỚI KHAI TRƯỜNG VÀ VỊ TRÍ CỬA LÒ (trích bản vẽ KT-DADC-KT-01, Thiết kế được duyệt)'),
    (3, os.path.join(IMG_DIR, 's-19.jpg'), 'HỘ CHIẾU THI CÔNG LÒ DỌC VỈA, XUYÊN VỈA CÓ CHỐNG (trích bản vẽ KT-DADC-CTN-06.1, Thiết kế được duyệt)'),
    (4, os.path.join(IMG_DIR, 's-20.jpg'), 'HỘ CHIẾU THI CÔNG LÒ DỌC VỈA, XUYÊN VỈA KHÔNG CHỐNG (trích bản vẽ KT-DADC-CTN-06.2, Thiết kế được duyệt)'),
    (5, os.path.join(IMG_DIR, 's-21.jpg'), 'HỘ CHIẾU THI CÔNG LÒ CHÂN TẦNG KHÔNG CHỐNG (trích bản vẽ KT-DADC-CTN-06.3, Thiết kế được duyệt)'),
]:
    sec = new_section(True)
    sec.top_margin, sec.bottom_margin = CM2(1.8), CM2(1.0)
    sec.header_distance = CM2(0.8)
    sec.left_margin, sec.right_margin = CM2(1.5), CM2(1.5)
    p = para('PHỤ LỤC %d. %s' % (no, ttl), bold=True, align=C, indent=Cm(0), size=12, space_after=2, keep=True)
    pi = doc.add_paragraph()
    pi.paragraph_format.alignment = C
    pi.paragraph_format.first_line_indent = Cm(0)
    pi.paragraph_format.line_spacing = 1.0
    if os.path.exists(img):
        pi.add_run().add_picture(img, width=CM2(23.0))

for _sec in doc.sections[2:]:
    for _tag in ('w:pgNumType', 'w:titlePg'):
        for _el in _sec._sectPr.findall(qn(_tag)):
            _sec._sectPr.remove(_el)
out = OUT
doc.save(out)
print('saved', out)
