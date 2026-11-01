import os
"""Đọc ngân hàng câu hỏi, đáp án từ Phụ lục 1, 2 của tài liệu tập huấn dùng chung."""
import re
from docx import Document

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'mau', 'nguon', '2026.10.29. Tài liệu tập huấn an toàn hàng hóa nguy hiểm dùng chung cho người lái xe, người áp tải.docx')

C_KEY = {'2.1': 'C1', '2.2': 'C2', '2.3': 'C3', '3': 'C4', '4.1': 'C5', '4.2': 'C6', '4.3': 'C7',
         '5.1': 'C8', '5.2': 'C9', '8': 'C10', '9': 'C11'}


def load():
    d = Document(SRC)
    ps = [p.text.strip() for p in d.paragraphs]
    st = ps.index('PHẦN A. CÂU HỎI CHUNG')
    en = ps.index('PHỤ LỤC 2')
    sets, cur, q = {}, None, None
    for t in ps[st:en]:
        if t == 'PHẦN A. CÂU HỎI CHUNG':
            cur = 'A'; sets[cur] = []; continue
        m = re.match(r'Bộ (B1|B2|C\d+)\. (.*)', t)
        if m:
            cur = m.group(1); sets[cur] = []; continue
        if t.startswith('PHẦN') or not t:
            continue
        m = re.match(r'Câu (\d+)\. (.*)', t)
        if m:
            q = {'n': int(m.group(1)), 'q': m.group(2), 'o': []}
            sets[cur].append(q); continue
        m = re.match(r'([ABCD])\. (.*)', t)
        if m:
            q['o'].append(m.group(2)); continue
        raise ValueError('Dòng lạ: ' + t)
    tabs = d.tables[-3:]
    ans = {'A': [c.text for c in tabs[0].rows[1].cells[1:]]}
    for t in tabs[1:]:
        for r in t.rows[1:]:
            k = r.cells[0].text.split('.')[0]
            ans[k] = [c.text for c in r.cells[1:]]
    for k, v in sets.items():
        assert all(len(x['o']) == 4 for x in v), k
        assert len(v) == len(ans[k]), k
    return sets, ans


if __name__ == '__main__':
    import sys
    sets, ans = load()
    print({k: len(v) for k, v in sets.items()})
    for k in sys.argv[1:]:
        print('==', k)
        for x, a in zip(sets[k], ans[k]):
            print('Câu %d. %s' % (x['n'], x['q']))
            for L, o in zip('ABCD', x['o']):
                print('   %s%s. %s' % ('*' if L == a else ' ', L, o))
