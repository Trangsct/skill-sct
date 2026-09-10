#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import shutil, os
from copy import deepcopy
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt
from docx.text.paragraph import Paragraph

SRC = '/mnt/skills/plugins/vbhc-vn:vbhc-vn/examples/sct/cong-van-xin-y-kien-cac-co-quan-phuong-an-ccn-von-nsnn.docx'
OUT = '/home/claude/work/output/cv_xin_y_kien_bt2.docx'
os.makedirs(os.path.dirname(OUT), exist_ok=True)
d = Document(SRC)


def set_text(p, text):
    """Giữ định dạng run đầu, xóa các run sau."""
    runs = [r for r in p.runs]
    if not runs:
        p.add_run(text); return
    runs[0].text = text
    for r in runs[1:]:
        r._element.getparent().remove(r._element)


def clone_after(p, text):
    new = deepcopy(p._p); p._p.addnext(new)
    np_ = Paragraph(new, p._parent); set_text(np_, text); return np_


# ---------- header: ngày tháng 9; V/v
c_date = d.tables[0].rows[2].cells[1]
for r in c_date.paragraphs[0].runs:
    if r.text == '7':
        r.text = '9'
for row in d.tables[0].rows:
  for cell in row.cells:
    for p in cell.paragraphs:
      if p.text.startswith('V/v'):
        set_text(p, 'V/v tham gia ý kiến dự thảo Kế hoạch thực hiện Bài toán lớn số 2 giai đoạn 2026 - 2030')

P = d.paragraphs
# ---------- Kính gửi (3 dòng, xóa 2 dòng thừa)
recipients = [
    '- Các Sở: Khoa học và Công nghệ, Tài chính, Nông nghiệp và Môi trường, Xây dựng, Nội vụ; Công an tỉnh; Ban Quản lý Khu kinh tế tỉnh; Ban Quản lý các khu công nghiệp tỉnh;',
    '- Các viện nghiên cứu, trường đại học và doanh nghiệp (có danh sách kèm theo).',
]
for i, t in zip(range(2, 4), recipients):
    set_text(P[i], t)
for i in (6, 5, 4):
    P[i]._element.getparent().remove(P[i]._element)
P = d.paragraphs  # body: P5..P10
body = {
 5: 'Thực hiện Công văn số 8652/UBND-NC ngày 24/8/2026 của UBND tỉnh về việc triển khai thực hiện 08 bài toán lớn, Sở Công Thương được giao chủ trì xây dựng dự thảo Kế hoạch của UBND tỉnh thực hiện Bài toán lớn số 2 “Phát triển công nghiệp khai thác và tinh chế nguyên liệu phục vụ phát triển công nghệ chiến lược” giai đoạn 2026 - 2030 và đến nay đã hoàn thành bước đầu dự thảo.',
 6: 'Kế hoạch có tính chất khoa học chuyên sâu về công nghệ tuyển, thủy luyện, tinh chế khoáng sản và liên quan đến nhiều ngành, lĩnh vực, doanh nghiệp; để dự thảo sát thực tiễn, bảo đảm cơ sở khoa học và tính khả thi trước khi trình UBND tỉnh, Sở Công Thương trân trọng đề nghị quý cơ quan, đơn vị dành thời gian nghiên cứu, cho ý kiến, nhất là các nhiệm vụ dự kiến giao chủ trì, phối hợp, mục tiêu, chỉ tiêu và kinh phí; kính mong các nhà khoa học, các thầy, cô ở các viện nghiên cứu, trường đại học góp ý về định hướng công nghệ, tính khả thi của các nhiệm vụ khoa học công nghệ; kính mong quý doanh nghiệp góp ý về mục tiêu, dự án động lực và các nhiệm vụ, dự án có thể cùng tham gia.',
 7: 'Do thời hạn UBND tỉnh giao là trước ngày 15/9/2026, Sở Công Thương kính mong nhận được văn bản góp ý của quý cơ quan, đơn vị trước ngày 13/9/2026 (qua Phòng Quản lý công nghiệp) để kịp tổng hợp, hoàn thiện.',
 8: '__DEL__',
 9: 'Sở Công Thương trân trọng cảm ơn và rất mong nhận được sự quan tâm, phối hợp của quý cơ quan, đơn vị (gửi kèm dự thảo Kế hoạch, các Phụ lục và danh sách gửi)./.',
}
for i, t in body.items():
    set_text(P[i], t)
for p in list(d.paragraphs):
    if p.text == '__DEL__':
        p._element.getparent().remove(p._element)
for p in list(d.paragraphs):
    if p.text.strip().startswith('Sở Công Thương đề nghị các cơ quan, đơn vị quan tâm, phối hợp thực hiện'):
        p._element.getparent().remove(p._element)
P = d.paragraphs
# giữ đúng 1 dòng trống giữa thân văn bản và bảng ký/nơi nhận (NĐ 30)
blank_before_sig = [p for p in P[9:] if not p.text.strip()]
for p in blank_before_sig[1:]:
    p._element.getparent().remove(p._element)
if not blank_before_sig:
    from copy import deepcopy as _dc
    last = [p for p in d.paragraphs if p.text.strip()][-1]
    e = _dc(last._p); last._p.addnext(e)
    for r in e.findall('.//{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r'): e.remove(r)

for p in d.paragraphs:
    if p.text.startswith('(Gửi kèm'):
        for r in p.runs: r.italic = True
    else:
        for r in p.runs: r.italic = False

# dòng trống sau Kính gửi: giãn dòng đơn (mẫu gốc 19pt) để tiết kiệm chỗ cho khối ký
for _p in d.paragraphs[:6]:
    if not _p.text.strip() and _p.paragraph_format.line_spacing:
        _p.paragraph_format.line_spacing = 1.0; _p.paragraph_format.space_after = Pt(0)
# thân: giãn đoạn 6→4pt (Quy tắc 14) để khối ký nằm trọn trang 1
for _p in d.paragraphs[5:9]:
    _p.paragraph_format.space_after = Pt(4)
# ---------- footer
for _c in d.tables[1].rows[0].cells:
    for _p in _c.paragraphs:
        _p.paragraph_format.line_spacing = 1.0; _p.paragraph_format.space_after = Pt(0); _p.paragraph_format.space_before = Pt(0)
c_nn = d.tables[1].rows[0].cells[0]
for p in c_nn.paragraphs:
    if 'UBND tỉnh' in p.text:
        set_text(p, '- UBND tỉnh (báo cáo);')
    if 'Lưu' in p.text:
        set_text(p, '- Lưu: VT, CN(Khôi).')
c_ky = d.tables[1].rows[0].cells[1]
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
_trPr = d.tables[1].rows[0]._tr.get_or_add_trPr(); _trPr.append(OxmlElement('w:cantSplit'))
for _p in [p for p in d.paragraphs if p.text.strip()][-2:]:
    _p.paragraph_format.keep_with_next = True
# Quy tắc 22 (Bạn chốt 09/9/2026): ô ký 4 paragraph trống (Bạn chốt 3-4 dòng ký) — không bớt để ép trang
blanks = [p for p in c_ky.paragraphs if not p.text.strip()]
for p in blanks[3:]:
    p._element.getparent().remove(p._element)
for p in c_ky.paragraphs:
    if 'Nguyễn Đình Chiến' in p.text:
        set_text(p, ' Hoàng Văn Thuân')

from docx.shared import Pt
for p in d.paragraphs:
    if p.text.startswith('Kính gửi'):
        p.paragraph_format.space_before = Pt(2)
body_el = d.element.body
# xóa các đoạn trống sau bảng ký (trừ sectPr)
tbl = d.tables[1]._tbl
for el in list(body_el):
    if el.tag.endswith('}p') and body_el.index(el) > body_el.index(tbl):
        if not ''.join(el.itertext()).strip():
            body_el.remove(el)
# ---------- Danh sách kèm theo (trang riêng, sau khối ký)
from docx.enum.text import WD_BREAK
from docx.shared import Pt as _Pt
def _P(t, bold=False, center=False, italic=False, size=14, after=6, first=True):
    p = d.add_paragraph(); r = p.add_run(t); r.bold = bold; r.italic = italic; r.font.size = _Pt(size); r.font.name = 'Times New Roman'
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if center else WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_after = _Pt(after); p.paragraph_format.space_before = _Pt(0)
    p.paragraph_format.first_line_indent = Cm(1) if (first and not center) else None
    return p
_t = _P('DANH SÁCH', bold=True, center=True, after=0); _t.paragraph_format.page_break_before = True
_P('các viện nghiên cứu, trường đại học, doanh nghiệp được đề nghị tham gia ý kiến dự thảo Kế hoạch thực hiện Bài toán lớn số 2', bold=True, center=True, after=0)
_P('(Kèm theo Công văn số          /SCT-CN ngày        /9/2026 của Sở Công Thương)', italic=True, center=True, size=13, after=10)
_P('I. Các viện nghiên cứu, trường đại học', bold=True)
for t in ['1. Viện Khoa học vật liệu - Viện Hàn lâm Khoa học và Công nghệ Việt Nam;', '2. Viện Khoa học và Công nghệ Mỏ - Luyện kim (Bộ Công Thương);', '3. Viện Hóa học công nghiệp Việt Nam (Tập đoàn Hóa chất Việt Nam);', '4. Trường Đại học Mỏ - Địa chất;', '5. Trường Đại học Bách khoa Hà Nội.']:
    _P(t)
_P('II. Các doanh nghiệp khai thác, chế biến khoáng sản, hóa chất trên địa bàn tỉnh', bold=True)
for t in ['1. Công ty TNHH một thành viên Apatit Việt Nam;', '2. Chi nhánh Mỏ tuyển đồng Sin Quyền, Lào Cai - VIMICO;', '3. Chi nhánh Luyện đồng Lào Cai - VIMICO;', '4. Công ty cổ phần Đồng Tả Phời - VINACOMIN;', '5. Công ty TNHH một thành viên Đức Giang Lào Cai;', '6. Công ty cổ phần DAP số 2 - Vinachem;', '7. Công ty cổ phần Phốt pho vàng Lào Cai;', '8. Công ty TNHH Phốt pho Việt Nam;', '9. Công ty cổ phần Phốt pho Apatit Việt Nam;', '10. Công ty cổ phần Công nghiệp Khánh An (mỏ đất hiếm Bến Đền);', '11. Công ty TNHH Tập đoàn Graphite Việt Nam (mỏ graphit Yên Thái);', '12. Chủ đầu tư các dự án khai thác, tuyển graphit Nậm Thi, Bảo Hà.']:
    _P(t)
d.save(OUT)
print('OK', OUT)
