# -*- coding: utf-8 -*-
"""Dựng Phiếu nhận xét, đánh giá (Mẫu 03c) — bản hoàn thiện."""
import os
import copy
import re
import os
import shutil
import subprocess
import zipfile
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph

import sys
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'Mau-03c-goc.docx')
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'out.docx')
LINE_RUNS = open(os.path.join(HERE, 'line_runs.txt'), encoding='utf-8').read().split('\n=====\n')

doc = Document(SRC)
for s in doc.sections:
    s.page_width, s.page_height = Cm(21.0), Cm(29.7)
    s.top_margin, s.bottom_margin = Cm(2), Cm(2)
    s.left_margin, s.right_margin = Cm(3), Cm(2)

FONT = 'Times New Roman'


def style_run(r, size=14, bold=None, italic=None):
    r.font.name = FONT
    r.font.size = Pt(size)
    rPr = r._r.get_or_add_rPr()
    rf = rPr.find(qn('w:rFonts'))
    if rf is None:
        rf = rPr.makeelement(qn('w:rFonts'), {})
        rPr.insert(0, rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
        rf.set(qn(a), FONT)
    if bold is not None:
        r.bold = bold
    if italic is not None:
        r.italic = italic


def set_par(par, text, size=14, bold=False, italic=False, align='justify',
            first=1.0, before=6, after=0):
    for r in list(par.runs):
        r._r.getparent().remove(r._r)
    r = par.add_run(text)
    style_run(r, size, bold, italic)
    f = par.paragraph_format
    f.alignment = {'justify': WD_ALIGN_PARAGRAPH.JUSTIFY, 'center': WD_ALIGN_PARAGRAPH.CENTER,
                   'right': WD_ALIGN_PARAGRAPH.RIGHT, 'left': WD_ALIGN_PARAGRAPH.LEFT}[align]
    f.first_line_indent = Cm(first)
    f.left_indent = Cm(0)
    f.space_before = Pt(before)
    f.space_after = Pt(after)
    f.line_spacing = 1.0
    return par


def add_par_after(par, text, **kw):
    new_p = copy.deepcopy(par._p)
    par._p.addnext(new_p)
    np = Paragraph(new_p, par._parent)
    return set_par(np, text, **kw)


def cell_rebuild(cell, lines):
    """lines: list of (text, size, bold, italic, before) ; text '@@LINE1@@' → placeholder."""
    ps = cell.paragraphs
    base = ps[0]
    for p in ps[1:]:
        p._p.getparent().remove(p._p)
    cur = None
    for i, (text, size, bold, italic, before) in enumerate(lines):
        if i == 0:
            cur = set_par(base, text, size=size, bold=bold, italic=italic, align='center',
                          first=0, before=before, after=0)
        else:
            cur = add_par_after(cur, text, size=size, bold=bold, italic=italic, align='center',
                                first=0, before=before, after=0)


# ------------------------------------------------------------------ dòng "Mẫu 03c"
paras = doc.paragraphs
paras[0]._p.getparent().remove(paras[0]._p)          # bỏ dòng mô tả mẫu
set_par(doc.paragraphs[0], 'Mẫu 03c', size=14, bold=True, align='right', first=0, before=0, after=6)

# ------------------------------------------------------------------ header (bảng 0)
t0 = doc.tables[0]
t0.alignment = WD_TABLE_ALIGNMENT.CENTER
for row in t0.rows:
    row.cells[0].width = Cm(5.9)
    row.cells[1].width = Cm(10.1)
t0.columns[0].width = Cm(5.9)
t0.columns[1].width = Cm(10.1)
cell_rebuild(t0.cell(0, 0), [('BỘ CÔNG THƯƠNG', 13, False, False, 0),
                              ('HỘI ĐỒNG THẨM ĐỊNH', 13, True, False, 0),
                              ('@@LINE1@@', 13, False, False, 0)])
cell_rebuild(t0.cell(0, 1), [('CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM', 13, True, False, 0),
                              ('Độc lập – Tự do – Hạnh phúc', 14, True, False, 0),
                              ('@@LINE2@@', 13, False, False, 0)])
cell_rebuild(t0.cell(1, 0), [('', 13, False, False, 0)])
cell_rebuild(t0.cell(1, 1), [('Hà Nội, ngày      tháng      năm 2026', 14, False, True, 6)])

# --------------------------------------------------------------- các dòng thông tin
TEN_KH = ('Kế hoạch phòng ngừa, ứng phó sự cố hóa chất của Nhà máy sản xuất '
          'phân bón Điamôn phốt phát (DAP) số 2 thuộc Công ty Cổ phần DAP số 2 - Vinachem')
for p in doc.paragraphs:
    t = p.text.replace('\xa0', ' ').strip()
    if t == 'PHIẾU NHẬN XÉT, ĐÁNH GIÁ':
        set_par(p, t, bold=True, align='center', first=0, before=12)
    elif t.startswith('Kế hoạch phòng ngừa, ứng phó sự cố hóa chất của'):
        set_par(p, TEN_KH, bold=True, align='center', first=0, before=6, after=6)
    elif t.startswith('1. Thông tin kế hoạch'):
        set_par(p, '1. Thông tin kế hoạch:', bold=True)
    elif t.startswith('- Tên kế hoạch'):
        set_par(p, '- Tên kế hoạch: ' + TEN_KH + '.')
    elif t.startswith('- Cơ sở hoạt động hóa chất'):
        set_par(p, '- Cơ sở hoạt động hóa chất: Nhà máy sản xuất phân bón Điamôn phốt phát (DAP) '
                   'số 2, công suất 330.000 tấn DAP/năm, 420.000 tấn axit sunfuric 98,5%/năm và '
                   '162.000 tấn axit photphoric (quy đổi 100% P2O5)/năm.')
    elif t.startswith('- Địa điểm thực hiện'):
        set_par(p, '- Địa điểm thực hiện: Khu công nghiệp Tằng Loỏng, xã Tằng Loỏng, tỉnh Lào Cai')
    elif t.startswith('- Tổ chức quản lý'):
        set_par(p, '- Tổ chức quản lý: Công ty Cổ phần DAP số 2 - Vinachem; địa chỉ trụ sở chính: '
                   'thôn Trung Tâm, xã Tằng Loỏng, tỉnh Lào Cai; Giấy chứng nhận đăng ký doanh nghiệp '
                   'mã số 5300265969, đăng ký thay đổi lần thứ 13 ngày 03/8/2026.')
    elif t.startswith('2. Thông tin người nhận xét'):
        set_par(p, '2. Thông tin người nhận xét:', bold=True)
    elif t.startswith('Họ tên'):
        set_par(p, '- Họ tên: Nguyễn Thị Loan.')
    elif t.startswith('Chức vụ'):
        set_par(p, '- Chức vụ: Chuyên viên Phòng Quản lý công nghiệp.')
    elif t.startswith('Cơ quan'):
        set_par(p, '- Cơ quan: Sở Công Thương tỉnh Lào Cai.')
    elif t.startswith('3. Kết quả đánh giá'):
        for r in list(p.runs):
            r._r.getparent().remove(r._r)
        r1 = p.add_run('3. Kết quả đánh giá ')
        style_run(r1, 14, True, False)
        r2 = p.add_run('(thành viên Hội đồng ký vào ô đã lựa chọn):')
        style_run(r2, 14, False, True)
        f = p.paragraph_format
        f.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        f.first_line_indent = Cm(1)
        f.space_before, f.space_after = Pt(6), Pt(0)
    elif t.startswith('4. Ý kiến nhận xét'):
        set_par(p, '4. Ý kiến nhận xét:', bold=True)
    elif t.startswith('4.1'):
        set_par(p, '4.1. Các nội dung đạt yêu cầu:', bold=True)
    elif t.startswith('4.2'):
        set_par(p, '4.2. Các nội dung cần chỉnh sửa, bổ sung:', bold=True)

# ---------------------------------------------------------- bảng ô lựa chọn (bảng 1)
t1 = doc.tables[1]
t1.alignment = WD_TABLE_ALIGNMENT.CENTER
grid = t1._tbl.find(qn('w:tblGrid'))
if grid is not None:
    for gc, w in zip(grid.findall(qn('w:gridCol')), (13.3, 1.4, 1.3)):
        gc.set(qn('w:w'), str(int(w * 567)))
tblPr = t1._tbl.tblPr
tw = tblPr.find(qn('w:tblW'))
if tw is not None:
    tw.set(qn('w:w'), str(int(16 * 567))); tw.set(qn('w:type'), 'dxa')
for row in t1.rows:
    row.cells[0].width = Cm(13.3)
    row.cells[1].width = Cm(1.4)
    row.cells[2].width = Cm(1.3)
    for c in row.cells:
        for p in c.paragraphs:
            for r in p.runs:
                style_run(r, 14)
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(6)
            if 'chỉnh sửa' in p.text:
                for r in p.runs:
                    rPr = r._r.get_or_add_rPr()
                    sp = rPr.makeelement(qn('w:spacing'), {qn('w:val'): '-10'})
                    rPr.append(sp)

# ----------------------------------------------------------------- nội dung 4.1
DAT = [
    ('a) Về hồ sơ và thẩm quyền thẩm định', True),
    ('- Hồ sơ đề nghị thẩm định đủ thành phần theo khoản 1 Điều 34 Nghị định số 25/2026/NĐ-CP ngày '
     '17/01/2026 của Chính phủ quy định chi tiết và biện pháp để tổ chức, hướng dẫn thi hành một số điều '
     'của Luật Hóa chất về phát triển ngành công nghiệp hóa chất và an toàn, an ninh hóa chất (sau đây '
     'gọi là Nghị định số 25/2026/NĐ-CP), gồm Văn bản đề nghị thẩm định số 1648/DAP2-KTh của Công ty '
     'Cổ phần DAP số 2 - Vinachem lập theo Mẫu 03a Phụ lục III Thông tư số 02/2026/TT-BCT ngày '
     '17/01/2026 của Bộ trưởng Bộ Công Thương quy định một số biện pháp thi hành Luật Hóa chất (sau '
     'đây gọi là Thông tư số 02/2026/TT-BCT) và 09 bản Kế hoạch.', False),
    ('- Xác định đúng đối tượng và thẩm quyền: khối lượng tồn trữ lớn nhất tại một thời điểm của '
     'amoniac khan là 5.700 tấn, lớn hơn ngưỡng 50.000 kg quy định tại số thứ tự 7 Bảng A Phụ lục IV '
     'Nghị định số 24/2026/NĐ-CP ngày 17/01/2026 của Chính phủ quy định các danh mục hóa chất thuộc '
     'phạm vi điều chỉnh của Luật Hóa chất (sau đây gọi là Nghị định số 24/2026/NĐ-CP), thuộc điểm a '
     'khoản 2 Điều 33 Nghị định số 25/2026/NĐ-CP; thẩm quyền thẩm định, phê duyệt thuộc Bộ Công Thương '
     'theo điểm c khoản 6 Điều 34 Nghị định số 25/2026/NĐ-CP và khoản 3 Điều 4 Thông tư số '
     '02/2026/TT-BCT.', False),
    ('- Căn cứ lập Kế hoạch điều chỉnh phù hợp với điểm a khoản 3 Điều 36 Nghị định số 25/2026/NĐ-CP '
     'do cơ sở đầu tư bổ sung hệ thống đường ống và các trạm xuất NH3, H3PO4, H2SO4, H2SiF6; Kế hoạch '
     'điều chỉnh được thẩm định, phê duyệt như lần đầu theo khoản 4 Điều 36 cùng Nghị định.', False),
    ('b) Về bố cục và căn cứ pháp lý', True),
    ('- Bố cục Kế hoạch bám theo hướng dẫn tại mục B Phụ lục II Thông tư số 02/2026/TT-BCT, gồm phần '
     'Mở đầu và 04 chương; có mục lục, danh mục bảng, danh mục hình.', False),
    ('- Căn cứ pháp lý về hóa chất đã cập nhật theo khung pháp luật hiện hành: Luật Hóa chất số '
     '69/2025/QH15; các Nghị định số 24/2026/NĐ-CP, 25/2026/NĐ-CP, 26/2026/NĐ-CP ngày 17/01/2026 của '
     'Chính phủ; các Thông tư số 01/2026/TT-BCT, 02/2026/TT-BCT ngày 17/01/2026 của Bộ trưởng Bộ Công '
     'Thương; QCVN 05A:2020/BCT và Sửa đổi 1:2024 QCVN 05A:2020/BCT.', False),
    ('c) Về nội dung chuyên môn', True),
    ('- Chương 1 mô tả đầy đủ quy mô đầu tư, diện tích, các hạng mục công trình (đã cập nhật các khu '
     'vực xuất, nhập hóa chất), công nghệ sản xuất của 04 xưởng, quy trình xuất, nhập từng loại hóa '
     'chất, bản kê khai hóa chất, yêu cầu kỹ thuật về bao gói, bảo quản, vận chuyển, điều kiện tự '
     'nhiên và danh sách các công trình công nghiệp trong phạm vi 1.000 m bao quanh nhà máy.', False),
    ('- Chương 2 có mô phỏng bằng phần mềm ALOHA và MARPLOT cho các kịch bản đối với amoniac gồm rò '
     'rỉ bồn chứa qua lỗ đường kính 1,5 cm, vỡ đường ống lỗ 6 cm, nổ bồn chứa và rò rỉ tại khu vực '
     'xuất, nhập xe bồn; có phân cấp sự cố 03 cấp, kế hoạch sơ tán người và tài sản, sơ đồ tổ chức '
     'điều hành ứng phó, danh mục trang thiết bị, hệ thống báo động, thông tin liên lạc và kế hoạch '
     'phối hợp với lực lượng bên ngoài.', False),
    ('- Chương 3 xây dựng 09 kịch bản diễn tập; Chương 4 có giải pháp kỹ thuật khắc phục hậu quả, phục '
     'hồi môi trường và phương án bồi thường thiệt hại.', False),
    ('- Tài liệu kèm theo có Giấy phép môi trường số 454/GPMT-BNNMT ngày 24/10/2025 của Bộ Nông '
     'nghiệp và Môi trường; hồ sơ thẩm duyệt thiết kế, nghiệm thu về phòng cháy, chữa cháy các năm '
     '2015, 2019, 2024; Phương án phòng cháy, chữa cháy và cứu nạn, cứu hộ năm 2026; quyết định kiện '
     'toàn Ban chỉ đạo, đội ứng phó sự cố hóa chất; hợp đồng xử lý nước thải, chất thải.', False),
]

# ----------------------------------------------------------------- nội dung 4.2
SUA = [
    ('4.2.1. Cập nhật đầy đủ các điểm nguy cơ mới vào Bảng 2.1', True),
    ('Bảng 2.1 Danh sách các điểm nguy cơ mới liệt kê thiết bị công nghệ của 03 xưởng và hệ thống '
     'đường ống chung, chưa đưa vào các hạng mục đầu tư bổ sung đã nêu tại Bảng 1.2 gồm bãi xuất NH3 '
     '(450 m2), khu vực xuất, nhập axit sunfuric (263 m2), khu vực xuất CPA và NH3 (425 m2), khu vực '
     'xuất WPA và H2SiF6 (272 m2) cùng các tuyến ống mới, đồng thời chưa nêu điều kiện công nghệ và số '
     'người lao động có mặt tại các vị trí này. Đề nghị bổ sung đầy đủ để thống nhất với Bảng 2.2 và '
     'thể hiện các điểm nguy cơ mới trên Hình 2.1.', False),
    ('4.2.2. Thống nhất số liệu phạm vi ảnh hưởng của sự cố', True),
    ('Số liệu tại Bảng 2.1, Bảng 2.2 chưa thống nhất với kết quả mô phỏng tại mục 2.2: cùng kịch bản rò '
     'rỉ amoniac tại kho chứa, bảng ghi vùng AEGL-3 là 121 m, AEGL-2 là 170 m, AEGL-1 là 277 m, trong '
     'khi mục 2.2.1.1 xác định lần lượt là 340 m, 960 m và 2.270 m; đối với tình huống nổ bồn, bảng ghi '
     'phạm vi nguy cơ tử vong 288 m còn mục 2.2.1.3 xác định 1.246 m, 1.609 m và 2.574 m. Các ngưỡng '
     'nồng độ AEGL của amoniac ghi trong bảng (5.000 ppm, 2.700 ppm, 1.100 ppm) không phù hợp với bộ '
     'giá trị AEGL thời gian phơi nhiễm 60 phút. Đề nghị rà soát, thống nhất số liệu trong toàn bộ Kế '
     'hoạch; thuyết minh rõ bộ ngưỡng, thời gian phơi nhiễm, thông số khí tượng (tốc độ gió, hướng gió, '
     'cấp ổn định khí quyển, nhiệt độ) và điều kiện nguồn phát thải (nhiệt độ, áp suất, pha lỏng hoặc '
     'khí) đã sử dụng khi chạy mô phỏng.', False),
    ('4.2.3. Bổ sung đánh giá, mô phỏng và giải pháp cho các trạm xuất hóa chất dạng lỏng', True),
    ('Sự cố tràn đổ, rò rỉ H2SO4, H3PO4, H2SiF6 và NaOH mới được đánh giá bằng khuyến cáo cách ly 50 m '
     'theo hướng gió, chưa tính toán lượng hóa chất tràn đổ lớn nhất, khả năng thu gom, thời gian ứng '
     'phó tại từng trạm xuất. Đề nghị bổ sung: dung tích và loại phương tiện chứa lớn nhất được phép '
     'nhận hàng tại mỗi trạm, số phương tiện đồng thời; dung tích hệ thống thu gom (đê bao, rãnh, hố '
     'thu) tại từng trạm xuất bảo đảm tối thiểu bằng 110% dung tích phương tiện chứa lớn nhất theo các '
     'điểm 9.1.1, 10.1.7 và 11.2 QCVN 05A:2020/BCT (Sửa đổi 1:2024); thiết bị rửa mắt và tắm khẩn cấp '
     'trong phạm vi tối đa 17 m tính từ khu vực tồn trữ theo điểm 5.9; vật liệu chế tạo và biện pháp '
     'chống ăn mòn cho bồn, đường ống, van, khớp nối theo từng loại axit (H2SO4 98% dùng thép cacbon, '
     'H3PO4 và H2SiF6 dùng thép không gỉ, nhựa hoặc thép lót cao su, không dùng vật liệu thủy tinh, gốm '
     'silicat cho H2SiF6); vật liệu trung hòa (vôi bột, soda) và vật liệu thấm hút bố trí tại chỗ; biển '
     'cảnh báo, hình đồ cảnh báo theo Phụ lục A QCVN 05A:2020/BCT (Sửa đổi 1:2024). Lưu ý nêu rõ trong '
     'phương án ứng phó việc không phun nước trực tiếp vào vũng axit sunfuric đặc để tránh phản ứng '
     'tỏa nhiệt, bắn tóe.', False),
    ('4.2.4. Bổ sung điều kiện an toàn đối với hệ thống đường ống, van và trạm xuất NH3', True),
    ('Kết quả mô phỏng cho thấy sự cố vỡ đường ống amoniac có vùng AEGL-3 tới 2,2 km và vùng AEGL-2 '
     'tới 6,1 km, trong khi mục 4.3 mới có biện pháp cho kho chứa NH3, chưa có mục riêng cho trạm xuất '
     'và tuyến ống mới. Đề nghị bổ sung, làm rõ: sơ đồ công nghệ và mặt bằng trạm xuất NH3 thể hiện vị '
     'trí bơm hoặc máy nén, đường xuất lỏng, đường hồi hơi cân bằng áp, van chặn khẩn cấp và điểm tập '
     'kết; van chặn khẩn cấp đóng nhanh tại đầu ống xuất và trên tuyến ống, kích hoạt được từ phòng '
     'điều khiển trung tâm và tại hiện trường; van an toàn xả áp cho các đoạn ống dẫn NH3 lỏng có thể '
     'bị cô lập giữa hai van; khớp nối chống bung hoặc ống mềm có van tự đóng khi phương tiện di chuyển '
     'bất ngờ; biện pháp chèn bánh, khóa liên động không cho phương tiện di chuyển trong quá trình '
     'nạp; thiết bị đo mức, cân hoặc lưu lượng kế và liên động ngắt quá đầy xe bồn; nối đất, chống '
     'tĩnh điện cho phương tiện và ống mềm; đầu dò khí NH3 tại khu vực xuất kèm ngưỡng cảnh báo và '
     'liên động dừng bơm, đóng van; giàn phun mưa dập hơi amoniac phủ kín khu vực xuất; thiết bị điện '
     'trong vùng nguy hiểm dùng loại phòng nổ; mặt nạ phòng độc, bình khí thở bố trí theo hướng ngược '
     'gió; quy trình xuất có phiếu kiểm tra trước, trong và sau khi bơm, có người giám sát thường trực; '
     'kế hoạch kiểm định kỹ thuật an toàn bồn, đường ống, van an toàn theo quy định về thiết bị có yêu '
     'cầu nghiêm ngặt về an toàn lao động và kế hoạch kiểm tra chiều dày, ăn mòn định kỳ đối với tuyến '
     'ống mới, vì các kịch bản sự cố trong Kế hoạch đều xuất phát từ nguyên nhân ăn mòn.', False),
    ('4.2.5. Bổ sung kịch bản diễn tập tại các trạm xuất', True),
    ('Chương 3 có 09 kịch bản diễn tập nhưng chưa có kịch bản tại trạm xuất NH3 (mới có Tình huống 9 '
     'rò rỉ trong quá trình nhập amoniac), trạm xuất H3PO4 và trạm xuất H2SiF6. Đề nghị bổ sung ít '
     'nhất 01 kịch bản diễn tập tại trạm xuất NH3 (rò rỉ tại khớp nối ống mềm hoặc đứt ống mềm khi '
     'phương tiện di chuyển), 01 kịch bản tại trạm xuất H2SiF6 và đưa vào kế hoạch diễn tập định kỳ '
     'hằng năm theo khoản 2 Điều 36 Nghị định số 25/2026/NĐ-CP; thực hiện chế độ báo cáo kết quả diễn '
     'tập theo Mẫu 04 Phụ lục IV Thông tư số 02/2026/TT-BCT.', False),
    ('4.2.6. Đánh giá ảnh hưởng ra ngoài hàng rào và cơ chế phối hợp', True),
    ('Nhà máy nằm trong Khu công nghiệp Tằng Loỏng, tiếp giáp Chi nhánh Luyện đồng Lào Cai, Nhà máy '
     'Tuyển Tằng Loỏng và nhiều cơ sở công nghiệp khác; khu vực xử lý Gyps giáp thôn Hà Hợp. Đề nghị bổ '
     'sung đánh giá nguy cơ sự cố dây chuyền sang các cơ sở lân cận theo từng hướng gió chính; cơ chế '
     'cảnh báo sớm ra ngoài hàng rào (còi, loa, tin nhắn); quy chế phối hợp bằng văn bản với các doanh '
     'nghiệp liền kề, Ban Quản lý Khu kinh tế tỉnh Lào Cai, UBND xã Tằng Loỏng và lực lượng Cảnh sát '
     'phòng cháy, chữa cháy và cứu nạn, cứu hộ; bổ sung Sở Công Thương, UBND xã Tằng Loỏng, Sở Nông '
     'nghiệp và Môi trường, đơn vị vận hành hạ tầng khu công nghiệp vào danh bạ liên lạc khẩn cấp tại '
     'mục 5.1.1.5.', False),
    ('4.2.7. Thống nhất số liệu khối lượng, đơn vị tính và đối chiếu ngưỡng', True),
    ('Bảng khối lượng tại phần Mở đầu liệt kê 06 hóa chất, Bảng 1.6 liệt kê 09 hóa chất; axit '
     'photphoric khi ghi 2.900 tấn, khi ghi 2.900 tấn quy đổi P2O5; axit sunfuric ghi 10.000 tấn nhưng '
     'theo Bảng 1.7 thì 02 bồn chứa có tổng dung tích 6.020 m3, với tỷ trọng 1,83 tương ứng khoảng '
     '11.000 tấn; các chất Na2SO4, Na2CO3, Na2SiF6 ghi số liệu nhưng thiếu đơn vị tính. Đề nghị thống '
     'nhất theo khối lượng tồn trữ lớn nhất thực tế tại một thời điểm, ghi khối lượng hóa chất thực '
     '(không quy đổi) và bổ sung bảng đối chiếu từng hóa chất với ngưỡng quy định tại Phụ lục IV Nghị '
     'định số 24/2026/NĐ-CP làm căn cứ xác định đối tượng theo khoản 2 Điều 33 Nghị định số '
     '25/2026/NĐ-CP.', False),
    ('4.2.8. Bổ sung các phần còn thiếu theo bố cục quy định', True),
    ('Kế hoạch chưa có phần Kiến nghị và cam kết của chủ đầu tư; chưa có Phụ lục các tài liệu kèm theo '
     'với các bản vẽ in màu khổ A3 gồm sơ đồ vị trí khu đất, sơ đồ tổng mặt bằng, sơ đồ mô tả các vị '
     'trí lưu trữ, bảo quản hóa chất và trạng thái bảo quản, sơ đồ thoát hiểm, sơ đồ mặt bằng bố trí '
     'thiết bị và dây chuyền công nghệ kèm khối lượng hóa chất nguy hiểm tại các thiết bị chính theo '
     'mục A và mục B Phụ lục II Thông tư số 02/2026/TT-BCT. Đề nghị bổ sung đầy đủ.', False),
    ('4.2.9. Rà soát thông tin pháp lý của cơ sở và các văn bản viện dẫn', True),
    ('Văn bản đề nghị thẩm định ghi Giấy chứng nhận đăng ký doanh nghiệp đăng ký thay đổi lần thứ 12 '
     'ngày 07/7/2025, trong khi tài liệu kèm theo là bản đăng ký thay đổi lần thứ 13 ngày 03/8/2026 do '
     'Phòng Doanh nghiệp, Sở Tài chính tỉnh Lào Cai cấp. Đề nghị chỉnh lý cho thống nhất; đồng thời rà '
     'soát ký hiệu, ngày ban hành và hiệu lực của các văn bản viện dẫn tại mục 3 phần Mở đầu, nhất là '
     'nhóm văn bản về bảo vệ môi trường và an toàn, vệ sinh lao động.', False),
    ('4.2.10. Hoàn thiện các thủ tục pháp lý đối với hạng mục đầu tư bổ sung', True),
    ('Đề nghị Công ty rà soát, hoàn thiện và bổ sung vào hồ sơ: hồ sơ điều chỉnh chủ trương đầu tư, '
     'Giấy chứng nhận đăng ký đầu tư đối với việc bổ sung hạng mục và sản phẩm nếu thuộc trường hợp '
     'phải điều chỉnh theo pháp luật về đầu tư; hồ sơ thẩm định thiết kế, giấy phép xây dựng hoặc miễn '
     'giấy phép, nghiệm thu công trình theo pháp luật về xây dựng; hồ sơ thẩm duyệt thiết kế và nghiệm '
     'thu về phòng cháy, chữa cháy cho các trạm xuất và tuyến ống mới; kết quả rà soát sự phù hợp của '
     'hạng mục bổ sung với Giấy phép môi trường số 454/GPMT-BNNMT.', False),
    ('Trường hợp Công ty bán các hóa chất nêu trên ra ngoài cơ sở: NH3, H3PO4, H2SiF6, NaOH, lưu huỳnh '
     'thuộc Phụ lục II Nghị định số 24/2026/NĐ-CP nên phải có Giấy chứng nhận đủ điều kiện kinh doanh '
     'hóa chất sản xuất, kinh doanh có điều kiện; H2SO4 thuộc nhóm 2 Phụ lục III Nghị định số '
     '24/2026/NĐ-CP nên phải có Giấy phép kinh doanh hóa chất cần kiểm soát đặc biệt do UBND cấp tỉnh '
     'cấp theo điểm a khoản 1 Điều 3 Thông tư số 01/2026/TT-BCT và phải lập phiếu kiểm soát mua, bán '
     'trong thời hạn 10 ngày kể từ ngày giao hàng theo khoản 1 Điều 8 Thông tư số 01/2026/TT-BCT; hoạt '
     'động vận chuyển phải có Giấy phép vận chuyển hàng hóa nguy hiểm theo Nghị định số 161/2024/NĐ-CP '
     'và Biện pháp phòng ngừa, ứng phó sự cố hóa chất trong vận chuyển theo khoản 3 Điều 35 Nghị định '
     'số 25/2026/NĐ-CP.', False),
    ('Các hạng mục thay đổi chỉ được đưa vào hoạt động sau khi Kế hoạch phòng ngừa, ứng phó sự cố hóa '
     'chất điều chỉnh được phê duyệt theo khoản 8 Điều 36 Nghị định số 25/2026/NĐ-CP; sau khi được phê '
     'duyệt, Công ty cập nhật Kế hoạch trên cơ sở dữ liệu quốc gia trong thời hạn 30 ngày theo điểm c '
     'khoản 5 Điều 34 Nghị định số 25/2026/NĐ-CP.', False),
]


def fill_block(anchor_text, items):
    ps = doc.paragraphs
    idx = next(i for i, p in enumerate(ps) if p.text.replace('\xa0', ' ').strip().startswith(anchor_text))
    dots = []
    j = idx + 1
    while j < len(ps) and ps[j].text.strip() and set(ps[j].text.strip()) <= {'…', '.', ' ', '\xa0'}:
        dots.append(ps[j])
        j += 1
    cur = dots[0]
    for text, bold in items:
        cur = add_par_after(cur, text, bold=bold)
    for d in dots:
        d._p.getparent().remove(d._p)


fill_block('4.1', DAT)
fill_block('4.2', SUA)

# ---------------------------------------------- nén chữ nhẹ để tránh chữ lẻ dòng cuối
def condense(par, val=-6):
    for r in par.runs:
        rPr = r._r.get_or_add_rPr()
        sp = rPr.find(qn('w:spacing'))
        if sp is None:
            sp = rPr.makeelement(qn('w:spacing'), {})
            rPr.append(sp)
        sp.set(qn('w:val'), str(val))


for p in doc.paragraphs:
    t = p.text.replace('\xa0', ' ').strip()
    if t.startswith('Kế hoạch phòng ngừa, ứng phó sự cố hóa chất của Nhà máy') or \
       t.startswith('- Địa điểm thực hiện'):
        condense(p, -10)
    elif t.startswith('- Tên kế hoạch'):
        condense(p, -14)

# ------------------------------------------------------------- xóa ghi chú mẫu
for p in list(doc.paragraphs):
    t = p.text.replace('\xa0', ' ').strip()
    if t.startswith('Ghi chú:') or re.match(r'^\(\d\)\s', t):
        p._p.getparent().remove(p._p)

# ----------------------------------------------------------- khối chữ ký (bảng 2)
t2 = doc.tables[2]
t2.alignment = WD_TABLE_ALIGNMENT.CENTER
c = t2.cell(0, 1)
cell_rebuild(c, [('Người nhận xét, đánh giá', 14, True, False, 0),
                 ('(Ký và ghi rõ họ tên)', 14, False, True, 0),
                 ('', 14, False, False, 0), ('', 14, False, False, 0), ('', 14, False, False, 0),
                 ('Nguyễn Thị Loan', 14, True, False, 0)])
for row in t2.rows:
    row.cells[0].width = Cm(8)
    row.cells[1].width = Cm(8)

# ---------------------------------------------- subscript công thức, superscript đơn vị
SUB = re.compile(r'(NH3|H2SO4|H3PO4|H2SiF6|Na2SO4|Na2CO3|Na2SiF6|P2O5)')
SUP = re.compile(r'(m[23])(?!\d)')
CHEM_SPLIT = re.compile(r'(NH3|H2SO4|H3PO4|H2SiF6|Na2SO4|Na2CO3|Na2SiF6|P2O5|m[23](?!\d))')


def _mk_run(tmpl_r, text, vert=None):
    nr = copy.deepcopy(tmpl_r)
    for t_el in nr.findall(qn('w:t')):
        nr.remove(t_el)
    rPr = nr.find(qn('w:rPr'))
    if rPr is None:
        rPr = nr.makeelement(qn('w:rPr'), {})
        nr.insert(0, rPr)
    for va in rPr.findall(qn('w:vertAlign')):
        rPr.remove(va)
    if vert:
        rPr.append(rPr.makeelement(qn('w:vertAlign'), {qn('w:val'): vert}))
    t = nr.makeelement(qn('w:t'), {})
    t.set(qn('xml:space'), 'preserve')
    t.text = text
    nr.append(t)
    return nr


def chem_format(par):
    for r in list(par.runs):
        txt = r.text
        if not CHEM_SPLIT.search(txt):
            continue
        parts = [p for p in CHEM_SPLIT.split(txt) if p]
        anchor = r._r
        for part in parts:
            if SUP.fullmatch(part):
                pieces = [(part[0], None), (part[1], 'superscript')]
            elif SUB.fullmatch(part):
                pieces = [(ch, 'subscript' if ch.isdigit() else None) for ch in part]
                # gộp ký tự liền nhau cùng kiểu
                merged = []
                for ch, v in pieces:
                    if merged and merged[-1][1] == v:
                        merged[-1] = (merged[-1][0] + ch, v)
                    else:
                        merged.append((ch, v))
                pieces = merged
            else:
                pieces = [(part, None)]
            for text, v in pieces:
                nr = _mk_run(r._r, text, v)
                anchor.addnext(nr)
                anchor = nr
        r._r.getparent().remove(r._r)


for p in doc.paragraphs:
    chem_format(p)
for t in doc.tables:
    for row in t.rows:
        for cc in row.cells:
            for p in cc.paragraphs:
                chem_format(p)

doc.save(OUT)

# ------------------------------------------ chèn Line shape thay placeholder
work = os.path.join(HERE, '_unz')
if os.path.exists(work):
    shutil.rmtree(work)
with zipfile.ZipFile(OUT) as z:
    z.extractall(work)
xmlp = f'{work}/word/document.xml'
s = open(xmlp, encoding='utf-8').read()


def adapt(run_xml, off_emu, cx_emu, pt_y):
    run_xml = re.sub(r'<wp:posOffset>\d+</wp:posOffset>(</wp:positionH>)',
                     f'<wp:posOffset>{off_emu}</wp:posOffset>\\1', run_xml, count=1)
    run_xml = re.sub(r'<wp:extent cx="\d+"', f'<wp:extent cx="{cx_emu}"', run_xml)
    run_xml = re.sub(r'<a:ext cx="\d+"', f'<a:ext cx="{cx_emu}"', run_xml)
    fr = off_emu / 12700
    to = (off_emu + cx_emu) / 12700
    run_xml = re.sub(r'from="[^"]+" to="[^"]+"',
                     f'from="{fr:.1f}pt,{pt_y}pt" to="{to:.1f}pt,{pt_y}pt"', run_xml)
    return run_xml


# ô trái: text width ≈ 5,6 − 0,38 = 5,22 cm ; đường 2,6 cm
L1 = adapt(LINE_RUNS[0], int((5.52 - 2.6) / 2 * 360000), int(2.6 * 360000), 1.6)
# ô phải: text width ≈ 10,4 − 0,38 = 10,02 cm ; đường 5,2 cm
L2 = adapt(LINE_RUNS[1], int((9.72 - 5.2) / 2 * 360000), int(5.2 * 360000), 2.35)
s, n1 = re.subn(r'<w:r>(?:(?!</w:r>).)*?@@LINE1@@.*?</w:r>', L1, s, flags=re.S)
s, n2 = re.subn(r'<w:r>(?:(?!</w:r>).)*?@@LINE2@@.*?</w:r>', L2, s, flags=re.S)
assert n1 == 1 and n2 == 1, (n1, n2)
# đảm bảo khai báo namespace cần thiết
root_tag = s[s.find('<w:document'):s.find('>', s.find('<w:document'))]
need = {'mc': 'http://schemas.openxmlformats.org/markup-compatibility/2006',
        'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
        'wps': 'http://schemas.microsoft.com/office/word/2010/wordprocessingShape',
        'wp14': 'http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing',
        'w14': 'http://schemas.microsoft.com/office/word/2010/wordml',
        'v': 'urn:schemas-microsoft-com:vml', 'o': 'urn:schemas-microsoft-com:office:office',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
add = ''.join(f' xmlns:{k}="{v}"' for k, v in need.items() if f'xmlns:{k}=' not in root_tag)
if add:
    s = s.replace(root_tag, root_tag + add, 1)
open(xmlp, 'w', encoding='utf-8').write(s)
os.remove(OUT)
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    for dp, _, fns in os.walk(work):
        for fn in fns:
            full = os.path.join(dp, fn)
            z.write(full, os.path.relpath(full, work))
print('saved', OUT)
