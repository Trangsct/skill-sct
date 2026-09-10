#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from docx import Document
from docx.shared import Pt

import os as _os
SRC = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'mau-cong-van-noi-bo-van-phong-so.docx')  # mẫu thật của Văn phòng Sở (Bạn gửi 10/9/2026)
OUT = '/home/claude/work/output/cv_noi_bo_bt2.docx'
d = Document(SRC)


def set_text(p, text):
    """Quy tắc 11: chỉ sửa run có chữ; run rỗng (neo shape Line) giữ nguyên."""
    txt = [r for r in p.runs if r.text]
    if not txt:
        p.add_run(text); return
    txt[0].text = text
    for r in txt[1:]:
        r.text = ''


for row in d.tables[0].rows:
    for cell in row.cells:
        for p in cell.paragraphs:
            if p.text.startswith('Số:'):
                set_text(p, 'Số:             /SCT-CN')
            elif p.text.startswith('V/v'):
                set_text(p, 'V/v xin ý kiến dự thảo Kế hoạch của UBND tỉnh thực hiện Bài toán lớn số 2')

P = d.paragraphs
set_text(P[1], 'Kính gửi:')
from copy import deepcopy
from docx.text.paragraph import Paragraph
from docx.shared import Cm
_e1 = deepcopy(P[1]._p); P[1]._p.addnext(_e1); _k1 = Paragraph(_e1, P[1]._parent); set_text(_k1, '- Ban Giám đốc Sở Công Thương;')
_e2 = deepcopy(_e1); _e1.addnext(_e2); _k2 = Paragraph(_e2, P[1]._parent); set_text(_k2, '- Các phòng chuyên môn, đơn vị thuộc Sở.')
from docx.enum.text import WD_ALIGN_PARAGRAPH
for _p in (_k1, _k2):
    _p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    _p.paragraph_format.left_indent = Cm(6.5)
    _p.paragraph_format.first_line_indent = None
    _p.paragraph_format.space_before = Pt(0); _p.paragraph_format.space_after = Pt(0)
P[1].paragraph_format.space_after = Pt(0)
_k2.paragraph_format.space_after = Pt(14)  # cách 1 dòng với thân văn bản
P = d.paragraphs

body = [
    'Thực hiện Công văn số 8652/UBND-NC ngày 24/8/2026 của UBND tỉnh, Sở Công Thương được giao chủ trì xây dựng dự thảo Kế hoạch của UBND tỉnh thực hiện Bài toán lớn số 2 “Phát triển công nghiệp khai thác và tinh chế nguyên liệu phục vụ phát triển công nghệ chiến lược” giai đoạn 2026 - 2030, gửi UBND tỉnh trước ngày 15/9/2026. Phòng Quản lý công nghiệp đã dựng dự thảo Kế hoạch (11 mục, 03 phụ lục).',
    'Phòng Quản lý công nghiệp kính đề nghị các đồng chí Lãnh đạo Sở cho ý kiến chỉ đạo về kết cấu, mục tiêu, phân công và tổng mức kinh phí; các phòng chuyên môn, đơn vị thuộc Sở quan tâm tham gia ý kiến theo lĩnh vực phụ trách (Phòng Kế hoạch - Tổng hợp: chỉ tiêu tăng trưởng, kinh phí, chế độ báo cáo; Phòng Quản lý thương mại: xuất khẩu, xúc tiến thương mại; Phòng Quản lý năng lượng: nguồn điện, tiết kiệm năng lượng; Văn phòng Sở: thể thức, hội nghị, đào tạo; Chi cục Quản lý thị trường: nguồn gốc khoáng sản, sản phẩm lưu thông).',
    'Ý kiến của các đồng chí và các phòng, đơn vị xin gửi về Phòng Quản lý công nghiệp trước ngày 13/9/2026 để Phòng kịp tổng hợp, hoàn thiện dự thảo và Tờ trình trình Giám đốc Sở (gửi kèm dự thảo Kế hoạch và Phụ lục I, II, III).',
    'Phòng Quản lý công nghiệp rất mong nhận được sự quan tâm, phối hợp của các đồng chí Lãnh đạo Sở và các phòng chuyên môn, đơn vị thuộc Sở./.',
]
targets = [p for p in P[5:] if p.text.strip()]
for i, t in enumerate(body):
    set_text(targets[i], t)
    for r in targets[i].runs:
        r.bold = False
for p in targets[len(body):]:
    p._element.getparent().remove(p._element)

for p in d.tables[1].rows[0].cells[0].paragraphs:
    if 'Lưu' in p.text:
        set_text(p, '- Lưu: VT, CN(Khôi).')
for p in d.tables[1].rows[0].cells[1].paragraphs:
    if 'Trịnh Văn Thành' in p.text:
        set_text(p, 'Hoàng Văn Thuân')
    elif p.text.startswith('KT.GIÁM'):
        set_text(p, 'KT. GIÁM ĐỐC')

# --- chuẩn hóa theo QA (mẫu VP có vài lệch thể thức): sz 13pt tường minh dòng Số/ngày; 1 dòng trống trước bảng ký; ô ký >= 3 dòng trống
from docx.shared import Pt
from copy import deepcopy
for row in d.tables[0].rows:
    for cell in row.cells:
        for p in cell.paragraphs:
            if p.text.startswith('Số:') or p.text.startswith('Lào Cai, ngày'):
                for r in p.runs:
                    r.font.size = Pt(13)
                    if p.text.startswith('Lào Cai'):
                        r.italic = True
body_el = d.element.body; kids = list(body_el); tbl = d.tables[1]._tbl; idx = kids.index(tbl)
blanks = []
j = idx - 1
while j >= 0 and kids[j].tag.endswith('}p') and not ''.join(kids[j].itertext()).strip():
    blanks.append(kids[j]); j -= 1
for e in blanks[1:]:
    body_el.remove(e)
c = d.tables[1].rows[0].cells[1]
bl = [p for p in c.paragraphs if not p.text.strip()]
while len(bl) < 3:
    e = deepcopy(bl[-1]._p); bl[-1]._p.addnext(e)
    from docx.text.paragraph import Paragraph
    bl.append(Paragraph(e, bl[-1]._parent))
# xóa đoạn trống sau bảng ký (gây trang trắng)
kids = list(body_el); idx = kids.index(tbl)
for e in kids[idx + 1:]:
    if e.tag.endswith('}p') and not ''.join(e.itertext()).strip():
        body_el.remove(e)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
d.save(OUT)
import subprocess, sys
subprocess.run([sys.executable, '/mnt/skills/plugins/vbhc-vn:vbhc-vn/scripts/fix_quoc_hieu.py', OUT], check=False)
print('OK', OUT)
