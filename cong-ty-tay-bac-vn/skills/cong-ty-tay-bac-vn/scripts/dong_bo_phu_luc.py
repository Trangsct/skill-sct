"""Đồng bộ Phụ lục 1, 2 của tài liệu dùng chung với đề kiểm tra chung (không chia theo vị trí)."""
import sys, os, copy, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx import Document
from docx.oxml.ns import qn
from docx.shared import Emu

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'mau', 'nguon', '2026.10.29. Tài liệu tập huấn an toàn hàng hóa nguy hiểm dùng chung cho người lái xe, người áp tải.docx')
OUT = sys.argv[1]
d = Document(SRC)
ps = d.paragraphs


def set_text(p, text):
    runs = p.runs
    runs[0].text = text
    for r in runs[1:]:
        r._r.getparent().remove(r._r)


def find(prefix, start=0):
    for i in range(start, len(ps)):
        if ps[i].text.strip().startswith(prefix):
            return i
    raise KeyError(prefix)


# Mục kiểm tra trong phần tổ chức tập huấn
i = find('- Kiểm tra trắc nghiệm 20 câu')
t = ps[i].text
a = t.index('Phần A gồm')
b = t.index('(Phụ lục 1)')
set_text(ps[i], t[:a] + 'đề dùng chung cho người lái xe và người áp tải, Phần A gồm 12 câu chung, Phần B gồm 08 câu theo loại, nhóm hàng được tập huấn ' + t[b:])

# Phụ lục 1
pl1 = find('PHỤ LỤC 1')
i = find('Thời gian làm bài: 60 phút', pl1)
t = ps[i].text
a = t.index('Đề gồm 20')
b = t.index('Mỗi câu có một')
set_text(ps[i], t[:a] + 'Đề gồm 20 câu hỏi trắc nghiệm, dùng chung cho người lái xe và người áp tải: Phần A (câu 1 đến câu 12) '
         'câu hỏi chung; Phần B (câu 13 đến câu 20) bộ câu hỏi của loại, nhóm hàng được tập huấn. ' + t[b:])

pb = find('PHẦN B. CÂU HỎI THEO VỊ TRÍ', pl1)
pc = find('PHẦN C. CÂU HỎI THEO LOẠI', pl1)
b1 = find('Bộ B1', pl1)
b2 = find('Bộ B2', pl1)


def qset(start, end):
    out = []
    for p in ps[start:end]:
        t = p.text.strip()
        if t.startswith('Câu '):
            out.append({'q': t.split('. ', 1)[1], 'o': []})
        elif len(t) > 2 and t[1] == '.' and t[0] in 'ABCD':
            out[-1]['o'].append(t[3:])
    return out


B1 = qset(b1 + 1, b2)
B2 = qset(b2 + 1, pc)
COMMON = [
    (B2[0]['q'], [B2[0]['o'][1], B2[0]['o'][0], B2[0]['o'][2], B2[0]['o'][3]]),
    (B2[3]['q'].replace('người áp tải phải bảo đảm', 'người lái xe, người áp tải phải bảo đảm'),
     [B2[3]['o'][0], B2[3]['o'][2], B2[3]['o'][3], B2[3]['o'][1]]),
    (B1[2]['q'], B1[2]['o']),
    (B1[3]['q'].replace('người lái xe phải:', 'người lái xe, người áp tải phải:'), B1[3]['o']),
]
assert COMMON[0][1][0].startswith('Người thuê vận tải') and COMMON[1][1][3].startswith('Không xếp chung')
assert COMMON[2][1][1].startswith('Làm sạch') and COMMON[3][1][2].startswith('Theo sự hướng dẫn')

q_tpl = ps[find('Câu 1.', pl1)]._p
o_tpl = ps[find('Câu 1.', pl1) + 1]._p
anchor = ps[pb - 1]._p          # phương án D của câu 8
for n, (q, opts) in enumerate(COMMON, 9):
    e = copy.deepcopy(q_tpl)
    anchor.addnext(e); anchor = e
    from docx.text.paragraph import Paragraph
    set_text(Paragraph(e, ps[0]._parent), 'Câu %d. %s' % (n, q))
    for L, o in zip('ABCD', opts):
        e = copy.deepcopy(o_tpl)
        anchor.addnext(e); anchor = e
        set_text(Paragraph(e, ps[0]._parent), '%s. %s' % (L, o))
# xóa PHẦN B cũ (tiêu đề + Bộ B1 + Bộ B2)
for p in ps[pb:pc]:
    p._p.getparent().remove(p._p)
set_text(ps[pc], 'PHẦN B. CÂU HỎI THEO LOẠI, NHÓM HÀNG')

# Phụ lục 2
body = d.element.body
els = list(body)
def para_el(text, after):
    for k in range(after, len(els)):
        if els[k].tag == qn('w:p') and els[k].xpath('string(.)').strip() == text:
            return k
    raise KeyError(text)
k2 = [k for k, e in enumerate(els) if e.tag == qn('w:p') and e.xpath('string(.)').strip() == 'PHỤ LỤC 2'][0]
kA = para_el('Phần A', k2)
kB = para_el('Phần B', kA)
kC = para_el('Phần C', kB)
tA = els[kA + 1]
assert tA.tag == qn('w:tbl')
# thêm 4 cột câu 9 - 12 vào bảng Phần A
grid = tA.find(qn('w:tblGrid'))
cols = grid.findall(qn('w:gridCol'))
total = sum(int(c.get(qn('w:w'))) for c in cols)
for _ in range(4):
    grid.append(copy.deepcopy(cols[-1]))
cols = grid.findall(qn('w:gridCol'))
first = int(total * 0.16)
other = int((total - first) / 12)
cols[0].set(qn('w:w'), str(first))
for c in cols[1:]:
    c.set(qn('w:w'), str(other))
ANS_COMMON = ['A', 'D', 'B', 'C']
for r, tr in enumerate(tA.findall(qn('w:tr'))):
    tcs = tr.findall(qn('w:tc'))
    for j, val in enumerate([str(x) for x in range(9, 13)] if r == 0 else ANS_COMMON):
        tc = copy.deepcopy(tcs[-1])
        ts = tc.findall('.//' + qn('w:t'))
        ts[0].text = val
        for t in ts[1:]:
            t.text = ''
        tcs[-1].addnext(tc) if j == 0 else last.addnext(tc)
        last = tc
    for tc in tr.findall(qn('w:tc')):
        w = tc.find(qn('w:tcPr') + '/' + qn('w:tcW'))
        if w is not None:
            w.set(qn('w:w'), str(first if tc is tr.findall(qn('w:tc'))[0] else other))
            w.set(qn('w:type'), 'dxa')
# xóa Phần B cũ và bảng của nó (kèm đoạn trống sau bảng), đổi Phần C thành Phần B
for e in els[kB:kC]:
    body.remove(e)
for t in els[kC].findall('.//' + qn('w:t')):
    if t.text and 'Phần C' in t.text:
        t.text = t.text.replace('Phần C', 'Phần B')

# bỏ mã bộ câu hỏi C1...C11
for p in d.paragraphs:
    if re.match(r'Bộ C\d+\. ', p.text):
        for r in p.runs:
            r.text = re.sub(r'Bộ C\d+\. ', 'Bộ câu hỏi: ', r.text)
for t in d.tables[-2:]:
    for row in t.rows:
        c = row.cells[0]
        for p in c.paragraphs:
            for r in p.runs:
                r.text = re.sub(r'^C\d+\. ', '', r.text).replace('Bộ câu hỏi', 'Loại, nhóm hàng') if r.text else r.text
path = os.path.join(OUT, '2026.11.01. Tài liệu tập huấn an toàn hàng hóa nguy hiểm dùng chung cho người lái xe, người áp tải.docx')
d.save(path)
print('saved', path)
