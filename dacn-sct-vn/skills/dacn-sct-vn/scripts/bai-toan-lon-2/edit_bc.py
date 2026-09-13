# -*- coding: utf-8 -*-
"""Báo cáo v10 (theo chỉ đạo Giám đốc 13/9): ngắn gọn, thuyết phục; ban hành chậm nhất 15/10/2026; làm đồng thời.
Sửa trực tiếp trên file gốc bc_src.docx (giữ định dạng), thay toàn bộ thân từ đoạn mở đầu đến câu kết."""
import copy
from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
from docx.table import _Row

SRC = "/home/claude/work/bc_src.docx"
OUT = "/home/claude/work/output/bc_bt2.docx"
d = Document(SRC)
P = d.paragraphs


def set_text(p, text, italic_all=None):
    assert p.runs, p.text
    assert p._p.find('.//' + qn('w:pict')) is None and p._p.find('.//' + qn('w:drawing')) is None
    p.runs[0].text = text
    for r in p.runs[1:]:
        r._element.getparent().remove(r._element)
    if italic_all is not None:
        p.runs[0].italic = italic_all


T_H1, T_H2, T_BODY, T_SUB = [copy.deepcopy(P[i]._p) for i in (8, 9, 10, 12)]
FIRST, LAST = 7, 29
anchor = P[30]
for i in range(FIRST, LAST + 1):
    P[i]._p.getparent().remove(P[i]._p)


def add(kind, text):
    tpl = {"H1": T_H1, "H2": T_H2, "T": T_BODY, "S": T_SUB}[kind]
    el = copy.deepcopy(tpl)
    anchor._p.addprevious(el)
    set_text(Paragraph(el, anchor._parent), text)


BODY = [
    ("T", "Thực hiện Thông báo số 78/TB-UBND ngày 28/5/2026, Công văn số 7698/UBND-NC ngày 29/7/2026 và Công văn số 8652/UBND-NC ngày 24/8/2026 của UBND tỉnh, Sở Công Thương được giao chủ trì xây dựng dự thảo Kế hoạch của UBND tỉnh thực hiện Bài toán lớn số 2 “Phát triển công nghiệp khai thác và tinh chế nguyên liệu phục vụ phát triển công nghệ chiến lược” giai đoạn 2026 - 2030, thời hạn gửi UBND tỉnh trước ngày 15/9/2026. Sở Công Thương báo cáo và đề xuất như sau:"),

    ("H1", "I. TÌNH HÌNH TRIỂN KHAI"),
    ("T", "1. Sở đã thành lập Tổ công tác xây dựng Bài toán lớn số 2 do Giám đốc Sở chỉ đạo; đã nghiên cứu đề bài, rà soát Danh mục công nghệ chiến lược và Danh mục sản phẩm công nghệ chiến lược tại Quyết định số 21/2026/QĐ-TTg; thu thập tài liệu pháp lý, quy hoạch, giấy phép, hiện trạng khai thác, chế biến của các chuỗi nguyên liệu; tham khảo ý kiến một số chuyên gia đầu ngành về khai thác, chế biến khoáng sản; tìm hiểu đầu ra của các sản phẩm công nghiệp hiện có của tỉnh."),
    ("T", "2. Đã xây dựng dự thảo Kế hoạch gồm thân Kế hoạch 07 mục và 02 phụ lục (Phụ lục I phân công nhiệm vụ; Phụ lục II Danh mục dự án thu hút đầu tư); đã xin ý kiến các phòng, đơn vị và Tổ công tác của Sở, tiếp thu, hoàn thiện. Dự thảo đã cập nhật các định hướng, quy định mới nhất của Trung ương: Kết luận số 83-KL/TW ngày 08/8/2026 của Bộ Chính trị về phát triển công nghiệp vật liệu Việt Nam; Luật Công nghệ cao năm 2025; Quyết định số 1493/QĐ-TTg ngày 06/8/2026; Nghị quyết số 66.25/2026/NQ-CP ngày 04/9/2026; Nghị định số 351/2026/NĐ-CP ngày 11/9/2026 và Thông tư số 50/2026/TT-BCT ngày 13/9/2026 (từ ngày 15/9/2026 chức năng quản lý nhà nước về địa chất, khoáng sản, khu công nghiệp thuộc ngành Công Thương từ Trung ương đến địa phương)."),

    ("H1", "II. HIỆN TRẠNG VÀ VẤN ĐỀ ĐẶT RA"),
    ("H2", "1. Vị trí của tỉnh trong chuỗi công nghệ chiến lược"),
    ("T", "Đối chiếu với Danh mục sản phẩm công nghệ chiến lược tại Quyết định số 21/2026/QĐ-TTg, Lào Cai tham gia chủ yếu ở khâu cung cấp nguyên liệu, vật liệu và hóa chất đầu vào: trực tiếp là sản phẩm số 25 (hệ thống khai thác, chế biến sâu và sản phẩm chế biến sâu từ khoáng sản, đất hiếm); gián tiếp là nguyên liệu cho các sản phẩm số 17 (vật liệu tiên tiến), 18 (pin, ắc quy, tích trữ năng lượng), 20 (thiết bị điện, máy điện), 23 (chip chuyên dụng). Kết luận số 83-KL/TW xác định công nghiệp vật liệu là đầu vào, điều kiện tiên quyết của các sản phẩm công nghệ chiến lược; yêu cầu quản lý khoáng sản chiến lược theo chuỗi giá trị, hạn chế tối đa xuất khẩu thô, làm chủ công nghệ chế biến sâu. Quy hoạch khoáng sản quốc gia và Quy hoạch tỉnh xác định apatit, đồng, sắt, đất hiếm, graphit là nhóm khoáng sản phải gắn khai thác với chế biến sâu tại tỉnh."),
    ("H2", "2. Hiện trạng 05 loại khoáng sản"),
    ("S", "a) Apatit: 12 giấy phép khai thác; 03 nhà máy tuyển 1,37 triệu tấn tinh quặng/năm và 02 nhà máy tuyển mới năm 2026 (450.000 tấn/năm); tổ hợp hóa chất Tằng Loỏng gồm 05 nhà máy phốt pho vàng, DAP số 2, axit, supe lân, lân nung chảy. Sản phẩm: tinh quặng, phốt pho vàng, phân bón, axit; phốt pho vàng chủ yếu bán ở dạng nguyên liệu trung gian và xuất khẩu. Điểm nghẽn: nguồn quặng bị khóa do chậm giải phóng mặt bằng các khai trường 24, 25, 19b, Cam Đường 2, khai trường 19, năm 2026 các nhà máy tuyển chỉ huy động khoảng 19% công suất; bãi thải gyps, xỉ chưa được xử lý căn cơ. Dư địa: axit phốt phoric cấp điện tử (dự án 60.000 tấn/năm, đăng ký hoàn thành quý IV/2026), hóa chất phốt pho tinh khiết cao, muối phốt phát cho pin; tái chế gyps, xỉ."),
    ("S", "b) Đồng: các mỏ Sin Quyền, Tả Phời, Vi Kẽm; các nhà máy tuyển 125.000 tấn tinh quặng/năm; Nhà máy luyện đồng 30.000 tấn đồng catot/năm, là tổ hợp tuyển - luyện đồng hoàn chỉnh duy nhất cả nước. Sản phẩm: tinh quặng, đồng tấm, axit sunfuric; đồng tấm bán cho cơ sở kéo dây, đúc ngoài tỉnh. Dư địa: dây, cáp điện, đồng kỹ thuật cho thiết bị điện; thu hồi vàng, bạc, đất hiếm từ quặng đuôi."),
    ("S", "c) Sắt: 13 giấy phép khai thác, khoảng 1,75 triệu tấn quặng/năm; mỏ Quý Xa 5 triệu tấn/năm (Giấy phép số 199/GP-BNNMT ngày 14/7/2026); Nhà máy gang thép Lào Cai tái khởi động quý II/2025, cán thép 500.000 tấn/năm. Dư địa: ổn định nguồn quặng Quý Xa cho luyện kim tại tỉnh; khu liên hợp gang thép Võ Lao theo Kế hoạch số 283/KH-UBND và Chiến lược ngành thép (Quyết định số 261/QĐ-TTg)."),
    ("S", "d) Đất hiếm, graphit và khoáng sản khác: chưa có sản phẩm. Đất hiếm: mỏ Yên Phú tạm dừng; Bến Đền được cấp Giấy phép số 197/GP-BNNMT ngày 13/7/2026, chưa khai thác; chưa có cơ sở thủy luyện, chiết tách tại tỉnh. Graphit: các dự án Nậm Thi, Bảo Hà, Làng Khoai - Làng Mạ - Bông 2 chưa vận hành; mỏ Yên Thái hết hạn giấy phép. Tiến độ phụ thuộc nhà đầu tư và thẩm quyền của Trung ương; giai đoạn 2026 - 2030 xác định nhiệm vụ khôi phục, đưa vào khai thác, chuẩn bị điều kiện; chế biến sâu thuộc tầm nhìn đến năm 2050."),
    ("H2", "3. Vấn đề đặt ra để Kế hoạch khả thi"),
    ("T", "Đây là bài toán lớn, phạm vi vượt khỏi thẩm quyền và nguồn lực của một địa phương. Một số định hướng của Trung ương đã rõ (Kết luận số 83-KL/TW, Quyết định số 21/2026/QĐ-TTg, Quyết định số 1493/QĐ-TTg, Nghị quyết số 66.25/2026/NQ-CP); một số nội dung chưa được cụ thể hóa: chưa có tiêu chuẩn kỹ thuật, yêu cầu chất lượng nguyên liệu cho từng sản phẩm công nghệ chiến lược; chưa có quy hoạch, cơ chế cho cơ sở chế biến sâu đất hiếm, graphit tại tỉnh; Chiến lược quốc gia phát triển công nghiệp vật liệu đang được xây dựng. Công nghệ tinh chế, chế biến sâu thay đổi hằng ngày, phần lớn thuộc diện bí mật công nghệ của doanh nghiệp nước ngoài, khó tiếp cận; nguồn dữ liệu, thông tin về công nghệ, thị trường, cân bằng vật chất từ quặng đến sản phẩm tinh chế còn ít và chưa chuẩn hóa; các tập đoàn, tổng công ty chủ chuỗi đang trong quá trình xây dựng định hướng, chiến lược sau khi có Kết luận số 83-KL/TW. Sản phẩm công nghiệp hiện có của tỉnh (tinh quặng apatit, phốt pho vàng, đồng tấm, phôi thép) chủ yếu bán ở dạng nguyên liệu trung gian ra ngoài tỉnh hoặc xuất khẩu; về lâu dài chưa có kế hoạch chế biến sâu trong nước gắn với nguồn nguyên liệu của tỉnh. Các doanh nghiệp tham gia khai thác, chế biến khoáng sản trên địa bàn hầu hết là doanh nghiệp ngoài nhà nước, chủ yếu tính toán hiệu quả lợi nhuận trước mắt, chưa chú trọng lợi ích lâu dài của nguồn tài nguyên; trong khi định hướng chiến lược cấp quốc gia về khoáng sản chiến lược chưa đầy đủ, dẫn đến nguy cơ chảy máu, lãng phí tài nguyên. Kinh nghiệm các nước phát triển (nhóm G7) là kiểm soát chặt, hạn chế xuất khẩu khoáng sản chiến lược, chủ yếu nhập khẩu nguyên liệu để chế biến sâu và dự trữ trong nước."),
    ("T", "Do đó, để Kế hoạch bảo đảm khả thi, gắn với thực tiễn và phù hợp với xu thế phát triển công nghệ của thế giới, Sở cần thu thập số liệu từ doanh nghiệp chủ chuỗi, khảo sát thực địa, làm việc trực tiếp với Bộ Công Thương, Bộ Khoa học và Công nghệ và các tập đoàn để thống nhất định hướng sản phẩm, quy hoạch, cơ chế trước khi trình ban hành; các công việc này được tiến hành đồng thời, không chờ đợi."),

    ("H1", "III. NỘI DUNG CHÍNH CỦA DỰ THẢO KẾ HOẠCH"),
    ("T", "1. Tên gọi: Kế hoạch phát triển công nghiệp khai thác và tinh chế nguyên liệu phục vụ phát triển công nghệ chiến lược trên địa bàn tỉnh Lào Cai giai đoạn 2026 - 2030, tầm nhìn đến năm 2050 (cụ thể hóa Bài toán lớn số 2). Phạm vi: 05 loại khoáng sản apatit, đồng, sắt, đất hiếm, graphit và khoáng sản khác đi kèm; tập trung trước hết vào apatit, đồng, sắt là ba chuỗi đang có sản xuất, sản phẩm và thị trường tiêu thụ."),
    ("T", "2. Mục tiêu: nâng cấp giá trị các chuỗi apatit, đồng, sắt từ sản phẩm trung gian lên tinh chế, chế biến sâu; khôi phục khai thác, chuẩn bị điều kiện chế biến sâu đất hiếm, graphit; hình thành Danh mục 16 dự án thu hút đầu tư công nghiệp khai thác và tinh chế nguyên liệu (danh mục mở) để bổ sung Danh mục dự án thu hút đầu tư của tỉnh tại Quyết định số 1382/QĐ-UBND; tỷ lệ huy động công suất tuyển apatit 50% năm 2027, 80% năm 2030; nhà máy axit phốt phoric cấp điện tử vận hành thương mại; 02 - 03 dự án tinh chế, chế biến sâu quy mô lớn được quyết định đầu tư; 100% doanh nghiệp khoáng sản chiến lược kết nối dữ liệu sản lượng."),
    ("T", "3. Nhiệm vụ: 08 nhiệm vụ tương ứng 07 nhóm sản phẩm dự kiến tại Thông báo số 78/TB-UBND, gồm kiểm kê, cân đối nguồn nguyên liệu và cơ chế chuyển hóa lợi thế tài nguyên; Danh mục dự án và xúc tiến đầu tư có mục tiêu; khơi thông nguồn nguyên liệu, tháo gỡ điểm nghẽn; phát triển ba chuỗi apatit, đồng, sắt lên sản phẩm tinh chế, hạ nguồn; lớp dữ liệu và giám sát sản lượng; nghiên cứu, chuyển giao công nghệ, kinh tế tuần hoàn; nhân lực, truyền thông, theo dõi, đánh giá (chi tiết tại Phụ lục I của dự thảo)."),
    ("T", "4. Nguồn lực và tổ chức thực hiện: ngân sách nhà nước dự kiến 30.000 triệu đồng giai đoạn 2026 - 2030 từ chi sự nghiệp và chi thường xuyên; hạ tầng vùng nguyên liệu sử dụng kế hoạch đầu tư công trung hạn tại Quyết định số 2390/QĐ-UBND, không phát sinh nhu cầu vốn mới; vốn dự án do doanh nghiệp bảo đảm. Tổ công tác liên ngành do Phó Chủ tịch UBND tỉnh làm Tổ trưởng, Sở Công Thương là cơ quan thường trực; sơ kết năm 2028, tổng kết năm 2030."),

    ("H1", "IV. KIẾN NGHỊ, ĐỀ XUẤT"),
    ("T", "Để Kế hoạch vừa là định hướng của tỉnh để tổ chức thực hiện, vừa là nội dung tham mưu với Trung ương về định hướng chiến lược quốc gia phát triển công nghiệp vật liệu, bảo đảm thống nhất, đồng bộ và phù hợp với Nghị quyết số 57-NQ/TW, Sở Công Thương kính đề nghị UBND tỉnh:"),
    ("T", "1. Cho phép Sở Công Thương tiếp tục hoàn thiện dự thảo Kế hoạch theo tiến độ tại Phụ lục kèm theo (thu thập số liệu, khảo sát thực địa, làm việc với bộ, tập đoàn và xin ý kiến sở, ngành, doanh nghiệp tiến hành đồng thời), trình UBND tỉnh ban hành chậm nhất ngày 15/10/2026."),
    ("T", "2. Thống nhất tên gọi, kết cấu, phạm vi, khung 08 nhiệm vụ và mức kinh phí của dự thảo nêu tại mục III để Sở làm cơ sở hoàn thiện; giao các sở, ngành, doanh nghiệp chủ chuỗi cung cấp số liệu, hồ sơ theo đề nghị của Sở Công Thương."),
    ("T", "3. Cho phép Sở, trong quá trình hoàn thiện, đưa vào Kế hoạch nội dung tham mưu UBND tỉnh kiến nghị Trung ương về quản lý khoáng sản chiến lược theo chuỗi giá trị: cấm hoặc hạn chế xuất khẩu khoáng sản thô, sản phẩm sơ chế; áp thuế xuất khẩu cao đối với nguyên liệu trung gian; ưu đãi cho dự án chế biến sâu trong nước."),
    ("T", "Sở Công Thương kính báo cáo UBND tỉnh xem xét, cho ý kiến chỉ đạo./."),
]
for k, t in BODY:
    add(k, t)

set_text(P[30], "(Gửi kèm: dự thảo Kế hoạch và 02 phụ lục)", italic_all=True)

cell = d.tables[1].cell(0, 0)
for p in cell.paragraphs:
    if "Lưu: VT" in p.text:
        set_text(p, "- Lưu: VT, CN(Khôi).")

# ---------------- Phụ lục tiến độ
t = d.tables[2]
ROWS = [
    ["I. ĐÃ THỰC HIỆN (đến 14/9/2026)"],
    ["1", "Thành lập Tổ công tác; nghiên cứu đề bài, thu thập tài liệu, tham khảo chuyên gia; dựng dự thảo Kế hoạch; xin ý kiến nội bộ Sở; báo cáo UBND tỉnh", "Dự thảo Kế hoạch; Báo cáo UBND tỉnh", "Sở Công Thương", "8/2026 - 14/9/2026"],
    ["II. SỐ LIỆU, KHẢO SÁT, LÀM VIỆC VỚI TRUNG ƯƠNG (15 - 30/9/2026, tiến hành đồng thời)"],
    ["2", "Đề nghị doanh nghiệp chủ chuỗi và các cơ quan cung cấp số liệu theo biểu mẫu; tiếp nhận hồ sơ, dữ liệu địa chất, khoáng sản theo NQ 66.25/2026/NQ-CP", "Hồ sơ số liệu; dữ liệu bàn giao", "Sở Công Thương; Sở NN&MT; doanh nghiệp", "Gửi 16/9; nhận trước 25/9"],
    ["3", "Xin ý kiến bằng văn bản các sở, ngành, UBND cấp xã liên quan, doanh nghiệp chủ chuỗi", "Văn bản góp ý; Bảng tiếp thu, giải trình", "Sở Công Thương", "Gửi 16/9; hạn 26/9"],
    ["4", "Khảo sát thực địa KCN Tằng Loỏng, các khai trường apatit, mỏ Sin Quyền, mỏ Quý Xa, các dự án đất hiếm, graphit", "Báo cáo khảo sát; số liệu xác nhận tại hiện trường", "Tổ công tác", "18 - 26/9"],
    ["5", "Làm việc với Bộ Công Thương, Bộ KH&CN và các tập đoàn, tổng công ty chủ chuỗi (Hóa chất Việt Nam, Đức Giang, Khoáng sản - TKV, Việt Trung)", "Biên bản làm việc; ý kiến về định hướng sản phẩm, quy hoạch, cơ chế", "Lãnh đạo Sở; Tổ công tác", "22 - 30/9"],
    ["III. HOÀN THIỆN, XIN Ý KIẾN, TRÌNH VÀ BAN HÀNH (01/10 - 15/10/2026)"],
    ["6", "Lập bảng cân đối nguồn - công suất chế biến ba chuỗi; hoàn thiện dự thảo Kế hoạch và 02 phụ lục theo số liệu, ý kiến góp ý và ý kiến của bộ, tập đoàn", "Dự thảo Kế hoạch hoàn thiện", "Sở Công Thương", "01 - 05/10"],
    ["7", "Hội nghị lấy ý kiến các sở, ngành, doanh nghiệp chủ chuỗi; Lãnh đạo UBND tỉnh chủ trì", "Biên bản hội nghị; kết luận của Lãnh đạo UBND tỉnh", "UBND tỉnh chủ trì; Sở Công Thương chuẩn bị", "06 - 07/10"],
    ["8", "Tiếp thu ý kiến hội nghị; Lãnh đạo Sở thông qua; trình UBND tỉnh; phối hợp Văn phòng UBND tỉnh thẩm tra, hoàn thiện; UBND tỉnh ban hành Kế hoạch", "Báo cáo trình UBND tỉnh; Kế hoạch của UBND tỉnh", "Giám đốc Sở; Văn phòng UBND tỉnh", "08 - 15/10; ban hành chậm nhất 15/10/2026"],
]


def uniq_cells(row):
    out, prev = [], None
    for c in row.cells:
        if c._tc is prev:
            continue
        prev = c._tc
        out.append(c)
    return out


body_rows = t.rows[1:]
group_src = copy.deepcopy([r._tr for r in body_rows if len(uniq_cells(r)) == 1][0])
item_src = copy.deepcopy([r._tr for r in body_rows if len(uniq_cells(r)) == 5][0])
tbl = t._tbl
for r in body_rows:
    tbl.remove(r._tr)
for row in ROWS:
    tr = copy.deepcopy(group_src if len(row) == 1 else item_src)
    tbl.append(tr)
    nr = _Row(tr, t)
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    _w = [1.0, 9.5, 4.0, 3.5, 3.0]   # bề rộng cột (cm) ước lượng, để tính ngưỡng 1 dòng
    for ci, (c, txt) in enumerate(zip(uniq_cells(nr), row)):
        ps = c.paragraphs
        set_text(ps[0], txt)
        for extra in ps[1:]:
            extra._p.getparent().remove(extra._p)
        # Quy tắc vbhc-vn: cột TT và ô 1 dòng căn giữa; ô nhiều chữ căn đều; không căn trái
        if len(row) == 1:
            ps[0].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif ci in (0, 4) or len(txt) <= _w[ci] * 4.5:
            ps[0].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        else:
            ps[0].paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

# xóa đoạn trống cuối sau bảng phụ lục (gây trang trắng)
_last = d.paragraphs[-1]
if _last.text.strip() == "" and _last._p.find(".//" + qn("w:sectPr")) is None:
    _last._p.getparent().remove(_last._p)
d.save(OUT)
print("OK", OUT)
