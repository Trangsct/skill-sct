import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vb import *
from vb import _set_widths, _no_borders, _valign
from docx.shared import Cm, Pt
from docx.enum.text import WD_TAB_ALIGNMENT
import qbank
from tai_lieu_bo_sung_loai1 import C12

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
DATE = '2026.11.01'
ORG = {'Doanh nghiệp tư nhân Vận tải A': ['DOANH NGHIỆP TƯ NHÂN', 'VẬN TẢI A'], 'Công ty TNHH Vận tải B': ['CÔNG TY TNHH', 'VẬN TẢI B']}
TB_UP = ['CÔNG TY TNHH NĂNG LƯỢNG', 'VÀ ĐIỆN LỰC TÂY BẮC']
HT = 'Doanh nghiệp tư nhân Vận tải A'
TP = 'Công ty TNHH Vận tải B'
G = {
    '1': 'Loại 1: Chất nổ và vật phẩm dễ nổ (tín hiệu báo nguy tàu biển)',
    '2.1': 'Loại 2, nhóm 2.1: Khí dễ cháy',
    '3': 'Loại 3: Chất lỏng dễ cháy và chất nổ lỏng khử nhạy',
    '2.3': 'Loại 2, nhóm 2.3: Khí độc hại',
    '5.1': 'Loại 5, nhóm 5.1: Chất ôxi hóa',
    '8': 'Loại 8: Chất ăn mòn',
}
UNITS = [  # (đơn vị, loại nhóm, học viên mẫu) - chỉ dùng đếm số bản in
    (HT, ['2.1', '3'], [('Học viên %d' % i, '', 'Lái xe', ['2.1', '3']) for i in range(4)]),
    (TP, ['1', '5.1', '2.3', '8'], [('Học viên %d' % i, '', 'Lái xe', ['1', '5.1', '2.3', '8']) for i in range(9)]),
]
SETS, ANS = qbank.load()
qbank.C_KEY['1'] = 'C12'
SETS['C12'] = [{'n': i, 'q': q, 'o': o} for i, (q, o, a) in enumerate(C12, 13)]
ANS['C12'] = [a for _, _, a in C12]
SZ = 13


def ma_de(g, vt):
    return '%s-%s' % (g, 'LX' if vt == 'Lái xe' else 'AT')


def save(d, name):
    path = os.path.join(OUT, '%s. %s.docx' % (DATE, name))
    d.save(path)
    print('saved', path)


def title(d, lines):
    P(d, '', size=8, before=0)
    p = None
    for k, ln in enumerate(lines):
        p = P(d, ln, bold=True, align='center', before=12 if k == 0 else 0, keep=True)
    add_line(p, 110, (9072 / 20 - 110) / 2, 22)
    P(d, '', size=10, before=0)


def info_line(d, left, right=None):
    p = P(d, left + ('\t' + right if right else ''), size=SZ, align='left', indent=False, before=3)
    p.paragraph_format.tab_stops.add_tab_stop(Cm(9.5), WD_TAB_ALIGNMENT.LEFT)
    return p


def score_box(d):
    t = TABLE(d, [3024, 3024, 3024], [['Điểm bằng số', 'Điểm bằng chữ', 'Số câu trả lời đúng'], ['', '', '']],
              ['center'] * 3, size=SZ)
    tr = t.rows[1]
    tr.height = Cm(1.5)
    from docx.enum.table import WD_ROW_HEIGHT_RULE
    tr.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
    return t


def questions(d, head, items):
    P(d, head, size=SZ, bold=True, align='left', indent=False, before=6, keep=True)
    for x in items:
        P(d, '⟪Câu %d.⟫ %s' % (x['n'], x['q']), size=SZ, before=2, keep=True)
        opts = ['%s. %s' % (L, o) for L, o in zip('ABCD', x['o'])]
        m = max(len(o) for o in opts)
        per = 4 if m <= 15 else (2 if m <= 35 else 1)
        lines = ['\t'.join(opts[i:i + per]) for i in range(0, 4, per)]
        for k, ln in enumerate(lines):
            p = P(d, ln, size=SZ, align='left', indent=False, before=0, keep=(k < len(lines) - 1))
            p.paragraph_format.left_indent = Cm(1)
            for j in range(1, per):
                p.paragraph_format.tab_stops.add_tab_stop(Cm(1 + 15.0 / per * j - 1), WD_TAB_ALIGNMENT.LEFT)



SO_BAN = {}
for unit, gs, people in UNITS:
    for g in gs:
        SO_BAN[g] = SO_BAN.get(g, 0) + sum(1 for x in people if g in x[3])
ORDER = ['1', '2.1', '2.3', '3', '5.1', '8']


# Câu 9 - 12 dùng chung cho người lái xe và người áp tải
B2, B1 = SETS['B2'], SETS['B1']
COMMON = [
    {'n': 9, 'q': B2[0]['q'], 'o': [B2[0]['o'][1], B2[0]['o'][0], B2[0]['o'][2], B2[0]['o'][3]]},
    {'n': 10, 'q': B2[3]['q'].replace('người áp tải phải bảo đảm', 'người lái xe, người áp tải phải bảo đảm'),
     'o': [B2[3]['o'][0], B2[3]['o'][2], B2[3]['o'][3], B2[3]['o'][1]]},
    {'n': 11, 'q': B1[2]['q'], 'o': B1[2]['o']},
    {'n': 12, 'q': B1[3]['q'].replace('người lái xe phải:', 'người lái xe, người áp tải phải:'), 'o': B1[3]['o']},
]
ANS_COMMON = ['A', 'D', 'B', 'C']
assert COMMON[0]['o'][0].startswith('Người thuê vận tải') and COMMON[1]['o'][3].startswith('Không xếp chung')
assert COMMON[2]['o'][1].startswith('Làm sạch') and COMMON[3]['o'][2].startswith('Theo sự hướng dẫn')
for x, o in zip(COMMON, ['A', 'D', 'B', 'C']):
    print(x['n'], x['q'], '->', o, x['o'][' ABCD'.index(o) - 1])


def blank_paper(g):
    d = new_doc()
    title(d, ['BÀI KIỂM TRA KẾT THÚC KHÓA TẬP HUẤN', 'AN TOÀN HÀNG HÓA NGUY HIỂM'])
    info_line(d, 'Loại, nhóm hàng kiểm tra: ⟪%s⟫' % G[g])
    info_line(d, 'Họ và tên: ……………………………………', 'Ngày sinh: ……/……/………')
    info_line(d, 'Đơn vị: …………………………………………………………………………')
    info_line(d, 'Vị trí làm việc: ………………………………', 'Ngày kiểm tra: ……/……/2026')
    P(d, '', size=6, before=0)
    score_box(d)
    P(d, '«Thời gian làm bài 60 phút. Học viên khoanh tròn chữ cái trước phương án đúng. Mỗi câu chỉ có một phương án đúng, '
         'mỗi câu đúng được 0,5 điểm; bài kiểm tra đạt yêu cầu khi đạt từ 5,0 điểm trở lên. Học viên không sử dụng tài liệu khi làm bài.»',
      size=SZ, before=8)
    questions(d, 'PHẦN A. CÂU HỎI CHUNG', SETS['A'] + COMMON)
    questions(d, 'PHẦN B. CÂU HỎI VỀ %s' % ('LOẠI 1 (TÍN HIỆU BÁO NGUY TÀU BIỂN)' if g == '1' else G[g].upper()), SETS[qbank.C_KEY[g]])
    nm = {'1': 'Loại 1 Tín hiệu báo nguy tàu biển', '2.1': 'Nhóm 2.1 Khí dễ cháy', '2.3': 'Nhóm 2.3 Khí độc hại',
          '3': 'Loại 3 Chất lỏng dễ cháy', '5.1': 'Nhóm 5.1 Chất ôxi hóa', '8': 'Loại 8 Chất ăn mòn'}[g]
    save(d, 'Mẫu bài kiểm tra - %s' % nm)
    return nm


for g in ORDER:
    print(g, SO_BAN[g], blank_paper(g))

# Đáp án
d = new_doc()
header_block(d, ['CÔNG TY TNHH NĂNG LƯỢNG', 'VÀ ĐIỆN LỰC TÂY BẮC'], None, None)
title(d, ['ĐÁP ÁN BÀI KIỂM TRA KẾT THÚC KHÓA TẬP HUẤN', 'AN TOÀN HÀNG HÓA NGUY HIỂM'])
P(d, '«(Dùng cho người chấm, không phát cho học viên)»', align='center', before=0, after=6)
P(d, '1. Phần A, câu hỏi chung (tất cả các mẫu)', bold=True, align='left', indent=False, before=6, keep=True)
TABLE(d, [1500] + [631] * 12, [['Câu'] + [str(i) for i in range(1, 13)], ['Đáp án'] + ANS['A'] + ANS_COMMON],
      ['center'] * 13, size=13)
P(d, '2. Phần B, câu hỏi theo loại, nhóm hàng', bold=True, align='left', indent=False, before=12, keep=True)
GS = {'1': 'Loại 1: Tín hiệu báo nguy tàu biển', '2.1': 'Nhóm 2.1: Khí dễ cháy', '3': 'Loại 3: Chất lỏng dễ cháy',
      '2.3': 'Nhóm 2.3: Khí độc hại', '5.1': 'Nhóm 5.1: Chất ôxi hóa', '8': 'Loại 8: Chất ăn mòn'}
rows = [['Loại, nhóm hàng'] + [str(i) for i in range(13, 21)]]
for g in ORDER:
    rows.append([GS[g]] + ANS[qbank.C_KEY[g]])
TABLE(d, [4272] + [600] * 8, rows, ['left'] + ['center'] * 8, size=13)
P(d, 'Cách tính điểm: mỗi câu đúng được 0,5 điểm, tổng điểm tối đa 10 điểm; bài kiểm tra đạt yêu cầu khi đạt từ 5,0 điểm '
     'trở lên. Mỗi loại, nhóm hàng chấm và ghi kết quả riêng. Học viên không đạt được kiểm tra lại; sau 02 lần kiểm tra không '
     'đạt thì phải tập huấn lại theo điểm c khoản 1 Điều 8 Nghị định số 161/2024/NĐ-CP.', size=13, before=10)
save(d, 'Đáp án bài kiểm tra kết thúc khóa tập huấn an toàn hàng hóa nguy hiểm')
