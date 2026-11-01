"""Bộ hồ sơ lớp tập huấn HHNH: học chung nội dung chung từ 20/10/2026, nội dung riêng học riêng; Tây Bắc cấp GCN."""
import sys, os, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vb import *
from vb import _set_widths, _no_borders, _valign

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
DATE = '2026.11.01'
D = datetime.date


def fd(x):  # tháng 1, 2 có số 0; tháng 3 - 12 bỏ số 0
    return '%02d/%d/%d' % (x.day, x.month, x.year) if x.month > 2 else '%02d/%02d/%d' % (x.day, x.month, x.year)


def fdl(x):  # dòng địa danh
    return 'Lào Cai, ngày %02d tháng %s năm %d' % (x.day, ('%02d' % x.month) if x.month <= 2 else str(x.month), x.year)


def fdt(x):
    return 'ngày %02d tháng %s năm %d' % (x.day, ('%02d' % x.month) if x.month <= 2 else str(x.month), x.year)


TB = 'Công ty TNHH Năng lượng và Điện lực Tây Bắc'
TB_UP = ['CÔNG TY TNHH NĂNG LƯỢNG', 'VÀ ĐIỆN LỰC TÂY BẮC']
TB_ADDR = 'Số nhà 16, ngõ 119 đường Nguyễn Phúc, phường Yên Bái, tỉnh Lào Cai'
GV = '⟦Họ và tên người tập huấn⟧'
GV_SINH = '⟦…/…/…⟧'
GV_KN = '⟦Đơn vị, thời gian, công việc quản lý hóa chất (tối thiểu 05 năm)⟧'
GV_BANG = '⟦Bản sao Bằng tốt nghiệp đại học số hiệu …, ngày …, Trường …⟧'
TB_DT = '⟦…⟧'
GIOHOC = 'buổi tối, từ 19 giờ 00 đến 23 giờ 00'
HTHUC = 'học trực tuyến (online), ' + GIOHOC
ND161 = ('Nghị định số 161/2024/NĐ-CP ngày 18 tháng 12 năm 2024 của Chính phủ quy định Danh mục hàng hóa nguy hiểm, '
         'vận chuyển hàng hóa nguy hiểm và trình tự, thủ tục cấp giấy phép, cấp giấy chứng nhận hoàn thành chương trình '
         'tập huấn cho người lái xe hoặc người áp tải vận chuyển hàng hóa nguy hiểm trên đường bộ')

# Lịch: nội dung chung 12 giờ học chung 3 buổi; nội dung riêng 04 giờ (gồm kiểm tra) mỗi loại, nhóm 1 buổi
CHUNG = [D(2026, 10, 20), D(2026, 10, 21), D(2026, 10, 22)]
RIENG = {'2.1': D(2026, 10, 23), '3': D(2026, 10, 24), '2.3': D(2026, 10, 25), '5.1': D(2026, 10, 26),
         '8': D(2026, 10, 27), '1': D(2026, 10, 30)}
NGAY_HD = D(2026, 10, 16)      # hợp đồng người tập huấn, thỏa thuận phối hợp
NGAY_QD = D(2026, 10, 19)      # quyết định tổ chức tập huấn
NGAY_QD_L1 = D(2026, 10, 29)   # quyết định tổ chức tập huấn bổ sung loại 1
NGAY_CN = D(2026, 11, 2)       # quyết định công nhận, cấp Giấy chứng nhận
NGAY_HH = D(2028, 11, 2)       # hết hạn Giấy chứng nhận

G = {
    '1': 'Loại 1: Chất nổ và vật phẩm dễ nổ (tín hiệu báo nguy tàu biển)',
    '2.1': 'Loại 2, nhóm 2.1: Khí dễ cháy',
    '3': 'Loại 3: Chất lỏng dễ cháy và chất nổ lỏng khử nhạy',
    '2.3': 'Loại 2, nhóm 2.3: Khí độc hại',
    '5.1': 'Loại 5, nhóm 5.1: Chất ôxi hóa',
    '8': 'Loại 8: Chất ăn mòn',
}
VT = {'Lái xe': 'Người lái xe', 'Áp tải': 'Người áp tải'}
# ===== KHỐI DỮ LIỆU LỚP: thay bằng dữ liệu thật khi dựng hồ sơ (kho công khai - chỉ để dữ liệu mẫu) =====
# people = (họ tên, ngày tháng năm sinh đủ, số định danh 12 số, 'Lái xe' hoặc 'Áp tải', [loại, nhóm], [giới tính 'Nam'/'Nữ'])
HT = dict(
    ten='Doanh nghiệp tư nhân Vận tải A', goi='Doanh nghiệp', org=['DOANH NGHIỆP TƯ NHÂN', 'VẬN TẢI A'], ky='A',
    thu_truong='CHỦ DOANH NGHIỆP TƯ NHÂN VẬN TẢI A', chuc='CHỦ DOANH NGHIỆP', nguoi_ky='Nguyễn Văn A', dieu_le=None,
    qd_cua='Chủ Doanh nghiệp tư nhân Vận tải A',
    dai_dien='ông Nguyễn Văn A, Chủ doanh nghiệp',
    dia_chi='⟦Địa chỉ trụ sở⟧', mst='⟦…⟧', dt='⟦…⟧',
    groups=['2.1'], so_cn='01/QĐ',
    people=[('Học viên A1', '01/01/1980', '000000000001', 'Lái xe', ['2.1']),
            ('Học viên A2', '02/02/1985', '000000000002', 'Áp tải', ['2.1'])])
TP = dict(
    ten='Công ty TNHH Vận tải B', goi='Công ty', org=['CÔNG TY TNHH', 'VẬN TẢI B'], ky='B',
    thu_truong='GIÁM ĐỐC CÔNG TY TNHH VẬN TẢI B', chuc='GIÁM ĐỐC', nguoi_ky='Trần Thị B',
    dieu_le='Căn cứ Điều lệ Công ty TNHH Vận tải B;', qd_cua='Giám đốc Công ty TNHH Vận tải B',
    dai_dien='bà Trần Thị B, Giám đốc',
    dia_chi='⟦Địa chỉ trụ sở⟧', mst='⟦…⟧', dt='⟦…⟧', groups=['2.3', '5.1', '8', '1'], so_cn='02/QĐ',
    people=[('Học viên B1', '03/3/1981', '000000000003', 'Lái xe', ['5.1', '1']),
            ('Học viên B2', '04/4/2004', '000000000004', 'Áp tải', ['5.1', '1'], 'Nữ'),
            ('Học viên B3', '05/5/1994', '000000000005', 'Lái xe', ['2.3', '5.1', '8'])])
UNITS = [HT, TP]
for U in UNITS:
    U['modules'] = [(g, [p for p in U['people'] if g in p[4]]) for g in U['groups']]
    U['so_qd'] = '%02d.%d/QĐ' % (NGAY_QD.day, NGAY_QD.month)
    U['so_tt'] = '%02d.%d/2026/TTPH-%s' % (NGAY_HD.day, NGAY_HD.month, U['ky'])
    U['ket_thuc'] = max(RIENG[g] for g in U['groups'])
SO_QD_L1 = '%02d.%d/QĐ' % (NGAY_QD_L1.day, NGAY_QD_L1.month)
SO_HD = '%02d.%d/2026/HĐGV' % (NGAY_HD.day, NGAY_HD.month)


def gshort(gs):
    return ', '.join(('nhóm ' if '.' in g else 'loại ') + g for g in gs)


def gtext(gs):
    return '; '.join(G[g] for g in gs).replace('Loại', 'loại')


def lich(g):
    ds = CHUNG + [RIENG[g]]
    return 'các buổi tối ngày %s, %s, %s và %s' % tuple(fd(x) for x in ds)


def tu_den(gs):
    ds = CHUNG + [RIENG[g] for g in gs]
    return 'từ ngày %s đến ngày %s' % (fd(min(ds)), fd(max(ds)))


def save(d, name):
    d.save(os.path.join(OUT, '%s. %s.docx' % (DATE, name)))
    print('saved', name)


def title_block(d, lines, before=18):
    P(d, lines[0], bold=True, align='center', before=before, keep=True)
    p = None
    for t in lines[1:]:
        p = P(d, t, bold=True, align='center', before=0, keep=True)
    add_line(p, 110, (9072 / 20 - 110) / 2, 22)
    P(d, '', before=0)


def org_title(d, U, first, lines):
    p = P(d, U['ten'].upper(), size=13, bold=True, align='center', before=0, page_break=not first, keep=True)
    add_line(p, 80, (9072 / 20 - 80) / 2, 19)
    P(d, '', size=8, before=0)
    for t in lines:
        P(d, t, bold=True, align='center', before=6, keep=True)


THOI_LUONG = ('16 giờ cho mỗi loại, nhóm hàng, bao gồm thời gian kiểm tra; trong đó 12 giờ nội dung chung (Chuyên đề 1, 2, 3, 4) '
              'học chung với người lái xe, người áp tải của các loại, nhóm hàng khác, 04 giờ nội dung riêng của loại, nhóm hàng '
              '(Chuyên đề 5) và kiểm tra học riêng')

# ======================================================================
# 1. THỎA THUẬN PHỐI HỢP (Tây Bắc với từng doanh nghiệp)
# ======================================================================
for U in UNITS:
    d = new_doc()
    quoc_hieu_center(d)
    P(d, 'THỎA THUẬN PHỐI HỢP', bold=True, align='center', before=12, keep=True)
    P(d, 'Tổ chức tập huấn an toàn hàng hóa nguy hiểm', bold=True, align='center', before=0, keep=True)
    P(d, 'Số: %s' % U['so_tt'], align='center', before=0, after=6)
    for t in ['«Căn cứ Bộ luật Dân sự số 91/2015/QH13 ngày 24 tháng 11 năm 2015;»', '«Căn cứ %s;»' % ND161,
              '«Căn cứ nhu cầu tập huấn của hai bên,»']:
        P(d, t)
    P(d, 'Hôm nay, %s, tại trụ sở Công ty TNHH Năng lượng và Điện lực Tây Bắc, chúng tôi gồm:' % fdt(NGAY_HD))
    P(d, '⟪BÊN A: CÔNG TY TNHH NĂNG LƯỢNG VÀ ĐIỆN LỰC TÂY BẮC⟫')
    P(d, '- Đại diện: Ông Trần Trọng Đài; Chức vụ: Giám đốc. Mã số doanh nghiệp: 5200966576.', before=3)
    P(d, '- Địa chỉ: %s; Điện thoại: %s.' % (TB_ADDR, TB_DT), before=3)
    P(d, '⟪BÊN B: %s⟫' % U['ten'].upper())
    dd = U['dai_dien'].split(', ')
    P(d, '- Đại diện: %s; Chức vụ: %s. Mã số doanh nghiệp: %s.' % (dd[0][0].upper() + dd[0][1:], dd[1], U['mst']), before=3)
    P(d, '- Địa chỉ: %s; Điện thoại: %s.' % (U['dia_chi'], U['dt']), before=3)
    P(d, 'Hai bên thống nhất như sau:')
    P(d, '⟪Điều 1. Nội dung⟫', keep=True)
    P(d, 'Bên A tổ chức khóa tập huấn an toàn hàng hóa nguy hiểm theo hình thức %s; Bên B cử người lái xe, người áp tải tham gia '
         'theo quyết định cử của Bên B. Thời lượng 16 giờ cho mỗi loại, nhóm hàng, bao gồm thời gian kiểm tra.' % HTHUC)
    P(d, '⟪Điều 2. Trách nhiệm của Bên A⟫', keep=True)
    for t in ['1. Bố trí người tập huấn đủ điều kiện theo khoản 4 Điều 8 Nghị định số 161/2024/NĐ-CP; cung cấp tài liệu tập huấn; tổ chức kiểm tra.',
              '2. Ban hành quyết định công nhận kết quả kiểm tra và cấp Giấy chứng nhận hoàn thành chương trình tập huấn trong thời hạn '
              '07 ngày làm việc kể từ khi kết thúc tập huấn, kiểm tra.',
              '3. Bàn giao hồ sơ tập huấn cho Bên B.']:
        P(d, t)
    P(d, '⟪Điều 3. Trách nhiệm của Bên B⟫', keep=True)
    for t in ['1. Ban hành quyết định cử người tham gia tập huấn và phê duyệt tài liệu tập huấn.',
              '2. Lưu giữ hồ sơ tập huấn trong thời hạn 03 năm, xuất trình khi cơ quan quản lý nhà nước yêu cầu.']:
        P(d, t)
    P(d, '⟪Điều 4. Điều khoản chung⟫', keep=True)
    P(d, 'Bên A không thu kinh phí tập huấn của Bên B. Thỏa thuận có hiệu lực kể từ ngày ký; lập thành 02 bản, mỗi bên giữ 01 bản./.')
    two_sign(d, ['ĐẠI DIỆN BÊN A', 'GIÁM ĐỐC'], ['ĐẠI DIỆN BÊN B', U['chuc']], blank=3, names=('Trần Trọng Đài', U['nguoi_ky']))
    save(d, 'Thỏa thuận phối hợp tổ chức tập huấn - Công ty Tây Bắc và %s' % U['ten'])

# ======================================================================
# 2. HỒ SƠ CỦA TỪNG DOANH NGHIỆP
# ======================================================================
for U in UNITS:
    goi, ten, n = U['goi'], U['ten'], len(U['people'])
    nbai = sum(len(p) for _, p in U['modules'])
    TLC = 'Tài liệu tập huấn an toàn hàng hóa nguy hiểm dùng chung cho người lái xe, người áp tải'

    def qd_cu(so, ngay, gs, ps, title, tl, tg):
        d = new_doc()
        header_block(d, U['org'], 'Số: %s' % so, fdl(ngay))
        title_block(d, ['QUYẾT ĐỊNH'] + title)
        P(d, U['thu_truong'], bold=True, align='center', before=6, after=6)
        cc = ['«Căn cứ %s;»' % ND161]
        if U['dieu_le']:
            cc.append('«%s»' % U['dieu_le'])
        cc[-1] = cc[-1][:-2] + '.»'
        for t in cc:
            P(d, t)
        P(d, 'QUYẾT ĐỊNH:', bold=True, align='center', before=12, after=6, keep=True)
        combos = []
        for p in ps:
            c = [g for g in p[4] if g in gs]
            if c not in combos:
                combos.append(c)
        nd = '; '.join('%s: %02d người' % (gshort(c), sum(1 for p in ps if [g for g in p[4] if g in gs] == c)) for c in combos)
        P(d, '⟪Điều 1.⟫ Cử %02d người lái xe, người áp tải (có danh sách kèm theo) tham gia khóa tập huấn an toàn hàng hóa nguy hiểm do Công ty TNHH Năng lượng và Điện lực Tây Bắc tổ chức, cụ thể:' % len(ps))
        P(d, '1. Loại, nhóm hàng: %s.' % nd)
        P(d, '2. Thời gian: %s.' % tg)
        P(d, '3. Hình thức: %s.' % HTHUC)
        P(d, '⟪Điều 2.⟫ Phê duyệt %s làm tài liệu tập huấn của %s.' % (tl, goi))
        P(d, '⟪Điều 3.⟫ Quyết định này có hiệu lực kể từ ngày ký. Những người có tên tại Điều 1 chịu trách nhiệm thi hành Quyết định này./.')
        sign_block(d, ['- Như Điều 3;', '- Công ty Tây Bắc;', '- Lưu: VT.'], [U['chuc']], U['nguoi_ky'])
        P(d, 'DANH SÁCH NGƯỜI THAM GIA TẬP HUẤN', bold=True, align='center', before=0, page_break=True, keep=True)
        P(d, 'AN TOÀN HÀNG HÓA NGUY HIỂM', bold=True, align='center', before=0, keep=True)
        P(d, '«(Kèm theo Quyết định số %s ngày %s của %s)»' % (so, fd(ngay), U['qd_cua']), align='center', before=0, after=12, keep=True)
        rows = [['TT', 'Họ và tên', 'Ngày sinh', 'Vị trí làm việc', 'Loại, nhóm hàng']]
        for i, p in enumerate(ps, 1):
            rows.append([str(i), p[0], p[1], VT[p[3]], '; '.join(g for g in p[4] if g in gs)])
        TABLE(d, [600, 3100, 1700, 1872, 1800], rows, ['center', 'left', 'center', 'center', 'center'], size=13)
        return d

    def tg_rieng(gs):
        return ('16 giờ cho mỗi loại, nhóm hàng; nội dung chung (12 giờ) học chung các buổi tối ngày %s, %s, %s; '
                'nội dung riêng và kiểm tra (04 giờ): %s' % (fd(CHUNG[0]), fd(CHUNG[1]), fd(CHUNG[2]),
                '; '.join('%s ngày %s' % (('nhóm ' if '.' in g else 'loại ') + g, fd(RIENG[g])) for g in gs)))

    T1 = ['Về việc cử người lái xe, người áp tải tham gia', 'tập huấn an toàn hàng hóa nguy hiểm']
    if U is HT:
        d = qd_cu(U['so_qd'], NGAY_QD, U['groups'], U['people'], T1, TLC, tg_rieng(U['groups']))
        save(d, '%s - Quyết định cử người tham gia tập huấn' % ten)
    else:
        d = qd_cu(U['so_qd'], NGAY_QD, U['groups'], U['people'], T1,
                  TLC + ' và Tài liệu tập huấn bổ sung an toàn hàng hóa nguy hiểm loại 1 (tín hiệu báo nguy tàu biển)',
                  tg_rieng(U['groups']))
        save(d, '%s - Quyết định cử người tham gia tập huấn' % ten)

    # ---------- Hồ sơ lớp (khoản 7 Điều 8)
    def gl(g):
        return ('Nhóm ' if '.' in g else 'Loại ') + g
    d = new_doc()
    org_title(d, U, True, ['DANH SÁCH NGƯỜI THAM GIA TẬP HUẤN', 'AN TOÀN HÀNG HÓA NGUY HIỂM'])
    P(d, 'Thời gian tập huấn: buổi tối, từ 19 giờ 00 đến 23 giờ 00; nội dung chung các ngày %s, %s, %s; nội dung riêng và kiểm tra: %s.' % (
        fd(CHUNG[0]), fd(CHUNG[1]), fd(CHUNG[2]), '; '.join('%s ngày %s' % (gl(g).lower(), fd(RIENG[g])) for g in U['groups'])), before=6, after=6, keep=True)
    rows = [['TT', 'Họ và tên', 'Ngày, tháng, năm sinh', 'Chức danh', 'Vị trí làm việc', 'Loại, nhóm hàng', 'Chữ ký']]
    for i, p in enumerate(U['people'], 1):
        rows.append([str(i), p[0], p[1], p[3], VT[p[3]], '; '.join(p[4]), '\n'])
    TABLE(d, [620, 2230, 1450, 950, 1500, 1250, 1072], rows, ['center', 'left', 'center', 'center', 'center', 'center', 'center'], size=12)
    two_sign(d, [''], ['NGƯỜI TẬP HUẤN', '(Ký, ghi rõ họ tên)'], blank=3, names=('', GV))
    org_title(d, U, False, ['THÔNG TIN VỀ NGƯỜI TẬP HUẤN'])
    P(d, '', before=0)
    TABLE(d, [567, 3200, 5305], [
        ['TT', 'Nội dung', 'Thông tin'],
        ['1', 'Họ và tên', GV], ['2', 'Ngày, tháng, năm sinh', GV_SINH], ['3', 'Trình độ học vấn', 'Đại học'],
        ['4', 'Chuyên ngành được đào tạo', 'Hóa học'],
        ['5', 'Kinh nghiệm công tác', GV_KN],
        ['6', 'Tài liệu chứng minh kèm theo', GV_BANG],
    ], ['center', 'left', 'left'], size=13)
    two_sign(d, [''], ['NGƯỜI TẬP HUẤN', '(Ký, ghi rõ họ tên)'], blank=3, names=('', GV))
    org_title(d, U, False, ['KẾT QUẢ KIỂM TRA TẬP HUẤN', 'AN TOÀN HÀNG HÓA NGUY HIỂM'])
    P(d, 'Điểm kiểm tra theo từng loại, nhóm hàng (thang điểm 10, đạt yêu cầu từ 5,0 điểm trở lên):', before=6, after=6, keep=True)
    gs = U['groups']
    rows = [['TT', 'Họ và tên', 'Ngày, tháng, năm sinh'] + ['%s\n(%s)' % (gl(g), fd(RIENG[g])[:5]) for g in gs] + ['Kết quả']]
    for i, p in enumerate(U['people'], 1):
        rows.append([str(i), p[0], p[1]] + [('⟦…⟧' if g in p[4] else '-') for g in gs] + ['Đạt'])
    wg = int((9072 - 620 - 2180 - 1450 - 950) / len(gs))
    TABLE(d, [620, 2180, 1450] + [wg] * len(gs) + [9072 - 620 - 2180 - 1450 - wg * len(gs)], rows,
          ['center', 'left', 'center'] + ['center'] * (len(gs) + 1), size=12)
    two_sign(d, [''], ['NGƯỜI TẬP HUẤN', '(Ký, ghi rõ họ tên)'], blank=3, names=('', GV))
    # Biên bản bàn giao hồ sơ: bà Dương và doanh nghiệp
    add_section(d, landscape=False)
    header_block(d, U['org'], None, None)
    title_block(d, ['BIÊN BẢN', 'Bàn giao hồ sơ tập huấn an toàn hàng hóa nguy hiểm'], before=8)
    P(d, 'Hôm nay, %s, chúng tôi gồm:' % fdt(U['ket_thuc']))
    P(d, '⟪Bên giao:⟫ %s, người tập huấn.' % GV)
    P(d, '⟪Bên nhận:⟫ %s, đại diện là %s.' % (ten, U['dai_dien']))
    P(d, 'Khóa tập huấn %s (%s) đã kết thúc; %02d người tham gia, %02d/%02d bài kiểm tra đạt yêu cầu. Bên giao bàn giao cho Bên nhận hồ sơ tập huấn gồm:' % (
        tu_den(U['groups']), gshort(U['groups']), n, nbai, nbai), keep=True)
    TABLE(d, [567, 6237, 2268], [
        ['TT', 'Tài liệu', 'Số lượng'],
        ['1', 'Danh sách người tham gia tập huấn có chữ ký', '01 bản'],
        ['2', 'Thông tin về người tập huấn kèm tài liệu chứng minh', '01 bộ'],
        ['3', 'Đề kiểm tra, đáp án và bài kiểm tra đã chấm', '%02d bài' % nbai],
        ['4', 'Kết quả kiểm tra', '01 bản'],
    ], ['center', 'left', 'center'], size=13)
    P(d, 'Biên bản lập thành 02 bản, mỗi bên giữ 01 bản./.')
    two_sign(d, ['BÊN GIAO', 'NGƯỜI TẬP HUẤN'], ['BÊN NHẬN', U['chuc']], blank=3, names=(GV, U['nguoi_ky']))
    save(d, '%s - Hồ sơ lớp tập huấn' % ten)

    # ---------- Quyết định công nhận kết quả (Công ty Tây Bắc)
    d = new_doc()
    header_block(d, TB_UP, 'Số: %s' % U['so_cn'], fdl(NGAY_CN))
    title_block(d, ['QUYẾT ĐỊNH', 'Về việc công nhận kết quả kiểm tra và cấp Giấy chứng nhận hoàn thành', 'chương trình tập huấn an toàn hàng hóa nguy hiểm'])
    P(d, 'GIÁM ĐỐC CÔNG TY TNHH NĂNG LƯỢNG VÀ ĐIỆN LỰC TÂY BẮC', bold=True, align='center', before=6, after=6)
    cc = ['«Căn cứ %s;»' % ND161, '«Căn cứ Điều lệ Công ty TNHH Năng lượng và Điện lực Tây Bắc;»',
          '«Căn cứ Thỏa thuận phối hợp số %s ngày %s với %s;»' % (U['so_tt'], fd(NGAY_HD), ten)]
    cc.append('«Căn cứ Quyết định số %s ngày %s của %s về việc cử người tham gia tập huấn;»' % (U['so_qd'], fd(NGAY_QD), U['qd_cua']))
    cc.append('«Căn cứ kết quả kiểm tra của người tập huấn.»')
    for t in cc:
        P(d, t)
    P(d, 'QUYẾT ĐỊNH:', bold=True, align='center', before=12, after=6, keep=True)
    P(d, '⟪Điều 1.⟫ Công nhận kết quả kiểm tra đạt yêu cầu và cấp Giấy chứng nhận hoàn thành chương trình tập huấn an toàn hàng hóa nguy hiểm cho %02d người lái xe, người áp tải của %s (có danh sách kèm theo). Giấy chứng nhận có giá trị 02 năm kể từ ngày cấp.' % (n, ten))
    P(d, '⟪Điều 2.⟫ Quyết định này có hiệu lực kể từ ngày ký. %s và những người có tên tại Điều 1 chịu trách nhiệm thi hành Quyết định này./.' % ten)
    sign_block(d, ['- Như Điều 2;', '- Lưu: VT.'], ['GIÁM ĐỐC'], 'Trần Trọng Đài')
    add_section(d, landscape=True)
    P(d, 'DANH SÁCH NGƯỜI ĐƯỢC CÔNG NHẬN KẾT QUẢ VÀ CẤP GIẤY CHỨNG NHẬN', bold=True, align='center', before=0, keep=True)
    P(d, '«(Kèm theo Quyết định số %s ngày %s của Giám đốc Công ty TNHH Năng lượng và Điện lực Tây Bắc)»' % (U['so_cn'], fd(NGAY_CN)), align='center', before=0, after=12, keep=True)
    rows = [['TT', 'Họ và tên', 'Ngày sinh', 'Số định danh cá nhân', 'Vị trí làm việc', 'Loại, nhóm hàng', 'Số Giấy chứng nhận']]
    cn = U['so_cn'].split('/')[0]
    for i, p in enumerate(U['people'], 1):
        rows.append([str(i), p[0], p[1], p[2], VT[p[3]], '; '.join(p[4]), '%02d.%s/QĐ' % (i, cn)])
    TABLE(d, [700, 3400, 1800, 2300, 2000, 2100, 2270], rows,
          ['center', 'left', 'center', 'center', 'center', 'center', 'center'], size=13)
    save(d, 'Công ty Tây Bắc - Quyết định công nhận kết quả và cấp Giấy chứng nhận - %s' % ten)

    # ---------- Giấy chứng nhận (Phụ lục VI NĐ 161) - Công ty Tây Bắc ký
    d = new_doc(page=(190, 130), margins=(6, 6, 6, 6))
    FACE_W = [5046, 5046]

    def PB(d, brk=True):
        d.element.body.find(qn('w:sectPr')).addprevious(parse_xml('<w:p %s><w:pPr><w:spacing w:before="0" w:after="0" w:line="20" w:lineRule="exact"/><w:rPr><w:sz w:val="2"/></w:rPr></w:pPr>%s</w:p>' % (W, '<w:r><w:rPr><w:sz w:val="2"/></w:rPr><w:br w:type="page"/></w:r>' if brk else '')))

    def face(d):
        t = d.add_table(rows=1, cols=2)
        t.alignment = WD_TABLE_ALIGNMENT.CENTER
        t._tbl.tblPr.append(parse_xml('<w:tblBorders %s>%s</w:tblBorders>' % (W, ''.join(
            '<w:%s w:val="single" w:sz="8" w:space="0" w:color="000000"/>' % b for b in ['top', 'left', 'bottom', 'right', 'insideV']))))
        _set_widths(t, FACE_W)
        t.rows[0]._tr.get_or_add_trPr().append(parse_xml('<w:trHeight %s w:val="6300" w:hRule="exact"/>' % W))
        return t.rows[0].cells

    for k, p in enumerate(U['people'], 1):
        L, R = face(d)
        cell_text(L, '', size=12)
        cell_text(R, TB_UP[0], size=13, bold=True, before=0, after=0)
        cell_text(R, TB_UP[1], size=13, bold=True, before=0, after=40, first=False)
        cell_text(R, 'GIẤY CHỨNG NHẬN', size=18, bold=True, before=2, after=6, first=False)
        for ln in ['HOÀN THÀNH CHƯƠNG TRÌNH', 'TẬP HUẤN AN TOÀN', 'HÀNG HÓA NGUY HIỂM']:
            cell_text(R, ln, size=14, bold=True, before=2, after=2, first=False)
        _valign(R, 'center'); _valign(L, 'center')
        PB(d)
        L, R = face(d)
        cell_text(L, 'CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM', size=11, bold=True, before=4, after=0)
        q = cell_text(L, 'Độc lập – Tự do – Hạnh phúc', size=12, bold=True, before=0, after=0, first=False)
        add_line(q, 146, ((5046 - 216) / 20 - 146) / 2, 15)
        cell_text(L, 'GIẤY CHỨNG NHẬN HOÀN THÀNH CHƯƠNG TRÌNH TẬP HUẤN AN TOÀN HÀNG HÓA NGUY HIỂM', size=12, bold=True, before=8, after=4, first=False)
        inner = L.add_table(rows=1, cols=2)
        _no_borders(inner); _set_widths(inner, [1400, 3400])
        A, B = inner.rows[0].cells
        A._tc.get_or_add_tcPr().append(parse_xml('<w:tcBorders %s>%s</w:tcBorders>' % (W, ''.join(
            '<w:%s w:val="single" w:sz="4" w:space="0" w:color="000000"/>' % b for b in ['top', 'left', 'bottom', 'right']))))
        inner.rows[0]._tr.get_or_add_trPr().append(parse_xml('<w:trHeight %s w:val="1980" w:hRule="exact"/>' % W))
        cell_text(A, 'Ảnh 3x4', size=11, italic=True); _valign(A, 'center')
        for j, ln in enumerate(['Họ và tên: ⟪%s⟫' % p[0], 'Nam/Nữ: %s' % (p[5] if len(p) > 5 else 'Nam'), 'Ngày sinh: %s' % p[1],
                                'Số định danh cá nhân: %s' % p[2], 'Nghề nghiệp: %s' % VT[p[3]]]):
            cell_text(B, ln, size=11, align='left', before=1, after=1, first=(j == 0))
        _valign(B, 'center')
        cell_text(L, 'Đơn vị công tác: %s' % ten, size=11, align='left', before=4, after=0, first=False)
        cell_text(L, 'Số: %02d.%s/QĐ' % (k, cn), size=11, align='left', before=2, after=0, first=False)
        cell_text(L, 'Giấy chứng nhận này có giá trị 02 năm', size=11, italic=True, align='left', before=2, after=0, first=False)
        cell_text(L, 'Từ ngày %s đến ngày %s' % (fd(NGAY_CN), fd(NGAY_HH)), size=11, italic=True, align='left', before=0, after=0, first=False)
        _valign(L, 'top')
        cell_text(R, 'Đã hoàn thành lớp tập huấn an toàn hàng hóa nguy hiểm đối với: %s cho %s do Công ty TNHH Năng lượng và Điện lực Tây Bắc tổ chức %s và kiểm tra đã đạt yêu cầu.' % (
            gtext(p[4]), ('bà ' if len(p) > 5 and p[5] == 'Nữ' else 'ông ') + p[0], tu_den(p[4])), size=12, align='left', before=24, after=12)
        cell_text(R, fdl(NGAY_CN), size=12, italic=True, before=6, after=0, first=False)
        cell_text(R, 'ĐƠN VỊ TẬP HUẤN', size=12, bold=True, before=4, after=0, first=False)
        cell_text(R, '(Ký tên, đóng dấu)', size=11, italic=True, before=0, after=0, first=False)
        for _ in range(4):
            cell_text(R, '', size=12, before=0, after=0, first=False)
        cell_text(R, 'Trần Trọng Đài', size=12, bold=True, before=0, after=0, first=False)
        _valign(R, 'top')
        PB(d, brk=(k < n))
    save(d, 'Công ty Tây Bắc - Giấy chứng nhận hoàn thành chương trình tập huấn - %s - %02d học viên' % (ten, n))
