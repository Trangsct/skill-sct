#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os
SK = '/mnt/skills/plugins/vbhc-vn:vbhc-vn'
sys.path.insert(0, SK + '/scripts')
from fill_template import TemplateDoc

doc = TemplateDoc(SK + '/templates/02-to-trinh.docx')
doc.replace_in_cell(0, 0, 1, 'ngày       tháng       năm 2026', 'ngày       tháng 9 năm 2026')
doc.set_paragraph_text(4, 'Về việc ban hành Kế hoạch thực hiện Bài toán lớn số 2')
doc.set_paragraph_text(5, '“Phát triển công nghiệp khai thác và tinh chế nguyên liệu')
from copy import deepcopy
from docx.text.paragraph import Paragraph
p5 = doc.doc.paragraphs[5]
x1 = deepcopy(p5._p); p5._p.addnext(x1)
doc._set_paragraph_text(Paragraph(x1, p5._parent), 'phục vụ phát triển công nghệ chiến lược”')
x2 = deepcopy(p5._p); x1.addnext(x2)
doc._set_paragraph_text(Paragraph(x2, p5._parent), 'trên địa bàn tỉnh Lào Cai giai đoạn 2026 - 2030')

B = []
def T(t, **k): B.append(dict(text=t, **k))

T('Thực hiện Thông báo số 78/TB-UBND ngày 28/5/2026 của UBND tỉnh về việc công bố Danh mục bài toán lớn về khoa học, công nghệ, đổi mới sáng tạo và chuyển đổi số phục vụ phát triển kinh tế - xã hội tỉnh Lào Cai giai đoạn 2026 - 2030; Công văn số 7698/UBND-NC ngày 29/7/2026 và Công văn số 8652/UBND-NC ngày 24/8/2026 của UBND tỉnh về việc triển khai thực hiện 08 bài toán lớn, trong đó giao Sở Công Thương chủ trì xây dựng dự thảo Kế hoạch thực hiện Bài toán lớn số 2, hoàn thành gửi UBND tỉnh trước ngày 15/9/2026.')
T('Sở Công Thương đã xây dựng dự thảo Kế hoạch của UBND tỉnh thực hiện Bài toán lớn số 2 “Phát triển công nghiệp khai thác và tinh chế nguyên liệu phục vụ phát triển công nghệ chiến lược” trên địa bàn tỉnh Lào Cai giai đoạn 2026 - 2030 (sau đây gọi là dự thảo Kế hoạch) và kính trình UBND tỉnh xem xét, ban hành với các nội dung chủ yếu sau:')
T('I. QUÁ TRÌNH XÂY DỰNG DỰ THẢO KẾ HOẠCH', bold=True)
T('1. Cách tiếp cận', bold=True)
T('Dự thảo Kế hoạch được xây dựng theo đúng yêu cầu tại Công văn số 7698/UBND-NC và Công văn số 8652/UBND-NC của UBND tỉnh: bắt đầu bằng việc “ra đề bài” (bối cảnh, hiện trạng, điểm nghẽn và bốn câu hỏi Bài toán phải trả lời); mỗi nhiệm vụ xác định đủ chín nội dung theo tinh thần sáu rõ; lộ trình được lập theo từng quý; không xây dựng cơ sở dữ liệu, phần mềm, hạ tầng trùng lặp với các nhiệm vụ đã và đang triển khai; không bố trí kinh phí thuê tư vấn, việc mời chuyên gia thực hiện theo nguyên tắc phối hợp chuyên môn.')
T('Nội dung chuyên môn bám sát Danh mục công nghệ chiến lược và Danh mục sản phẩm công nghệ chiến lược ban hành kèm theo Quyết định số 21/2026/QĐ-TTg ngày 30/4/2026 của Thủ tướng Chính phủ (thay thế Quyết định số 1131/QĐ-TTg, có hiệu lực từ ngày 01/7/2026), trọng tâm là sản phẩm số 25 “Hệ thống khai thác, chế biến sâu và sản phẩm chế biến sâu từ khoáng sản, dầu khí và đất hiếm” và các sản phẩm số 17, 18, 20, 23; Chương trình khoa học, công nghệ và đổi mới sáng tạo quốc gia đặc biệt về công nghệ chiến lược (Quyết định số 1493/QĐ-TTg ngày 06/8/2026); Quy hoạch tỉnh; Quy hoạch khoáng sản quốc gia; Nghị quyết số 169/NQ-CP; Chương trình hành động số 39-CTr/TU, Chỉ thị số 11-CT/TU, Chỉ thị số 26-CT/TU và các kế hoạch của UBND tỉnh về khoáng sản.')
T('Dự thảo đã cập nhật Nghị quyết số 66.25/2026/NQ-CP ngày 04/9/2026 của Chính phủ về xử lý khó khăn, vướng mắc liên quan đến chức năng, nhiệm vụ, quyền hạn quản lý nhà nước về khu công nghiệp, địa chất, khoáng sản (có hiệu lực từ ngày 15/9/2026), theo đó nhiệm vụ tham mưu quản lý nhà nước về địa chất, khoáng sản của Sở Nông nghiệp và Môi trường, Sở Xây dựng do Sở Công Thương thực hiện; việc phân công cơ quan chủ trì các nhiệm vụ trong dự thảo được xây dựng theo nguyên tắc giao cho cơ quan có chức năng quản lý nhà nước trực tiếp và có điều khoản chuyển tiếp phù hợp với hiệu lực tạm thời của Nghị quyết.')
T('2. Lấy ý kiến và tiếp thu, hoàn thiện', bold=True)
T('Sở Công Thương đã gửi dự thảo Kế hoạch lấy ý kiến các cơ quan: Sở Khoa học và Công nghệ, Sở Tài chính, Sở Nông nghiệp và Môi trường, Sở Xây dựng, Công an tỉnh, Ban Quản lý Khu kinh tế tỉnh, Ban Quản lý các khu công nghiệp tỉnh và các cơ quan liên quan tại Công văn số          /SCT-CN ngày        /9/2026. Trên cơ sở ý kiến tham gia, Sở Công Thương đã tổng hợp, tiếp thu, giải trình và hoàn thiện dự thảo (Bảng tổng hợp tiếp thu, giải trình ý kiến kèm theo Tờ trình này).')
T('II. BỐ CỤC VÀ NỘI DUNG CƠ BẢN CỦA DỰ THẢO KẾ HOẠCH', bold=True)
T('1. Bố cục', bold=True)
T('Dự thảo Kế hoạch gồm 11 mục (bối cảnh, hiện trạng và yêu cầu đặt ra; mục đích, yêu cầu; quan điểm, nguyên tắc; mục tiêu, chỉ tiêu và sản phẩm đầu ra; phạm vi, quy mô, đối tượng; nhiệm vụ và giải pháp; phương thức thực hiện; nguồn lực tài chính; lộ trình; tổ chức thực hiện; chế độ báo cáo, kiểm tra, sơ kết, tổng kết) và 03 phụ lục: Phụ lục I. Danh mục 16 nhiệm vụ theo sáu rõ; Phụ lục II. Định hướng phát triển các chuỗi giá trị nguyên liệu chiến lược và dự án động lực; Phụ lục III. Lộ trình và kết quả theo từng quý, năm.')
T('2. Nội dung cơ bản', bold=True)
T('a) Đề bài của Bài toán: bám các chiến lược, quy hoạch đã được phê duyệt (Nghị quyết số 10-NQ/TW, Quy hoạch khoáng sản quốc gia, Quy hoạch tỉnh, Quyết định số 21/2026/QĐ-TTg, Chỉ thị số 11-CT/TU, Chỉ thị số 26-CT/TU, Đề án số 13), đánh giá hiện trạng từng chuỗi giá trị đất hiếm, graphit, apatit - hóa chất phốt pho, đồng, sắt - thép và khoáng sản đi kèm theo giấy phép, công suất, tiến độ thực tế (mỏ đất hiếm Bến Đền, Yên Phú; các mỏ graphit Nậm Thi, Bảo Hà, Yên Thái; các khai trường apatit và tổ hợp hóa chất Tằng Loỏng); bảy điểm nghẽn và bảy câu hỏi Bài toán phải trả lời về nguyên liệu, công nghệ, dự án đầu tư, dữ liệu - giám sát, cơ chế chính sách, nhân lực và môi trường (bố trí tập trung các cơ sở chế biến sâu để xử lý môi trường tập trung).')
T('b) Mục tiêu, chỉ tiêu: đến hết năm 2027 mỏ đất hiếm Bến Đền đi vào khai thác, dự án Yên Phú hoạt động trở lại, hoàn thành kiến nghị bổ sung quy hoạch chế biến đất hiếm; các dự án tuyển graphit Nậm Thi, Bảo Hà khởi công, vận hành; khôi phục các khai trường apatit, tỷ lệ huy động công suất tuyển đạt 50%; Atlas số vận hành; đến năm 2030 dự án thủy luyện đất hiếm và dự án tinh chế graphit được chấp thuận chủ trương đầu tư, khởi công, phấn đấu vận hành giai đoạn đầu; các nhà máy tuyển graphit đạt tổng công suất từ 55.000 tấn/năm; tỷ lệ huy động công suất tuyển apatit đạt 80%; ít nhất 01 dự án hóa chất phốt pho tinh khiết cao mới; ít nhất 08 nhiệm vụ khoa học và công nghệ, 04 quy trình công nghệ được chuyển giao; 03 mô hình kinh tế tuần hoàn; 1.500 lượt người được đào tạo; góp phần thực hiện các chỉ tiêu tại Nghị quyết số 169/NQ-CP. Bảy sản phẩm đầu ra bám sát Thông báo số 78/TB-UBND.')
T('c) Nhiệm vụ: 16 nhiệm vụ trong 06 nhóm: (1) dữ liệu, bản đồ số và giám sát chuỗi giá trị (03 nhiệm vụ); (2) nghiên cứu, làm chủ và chuyển giao công nghệ tinh chế với ba cụm nhiệm vụ khoa học và công nghệ (03 nhiệm vụ); (3) phát triển các chuỗi giá trị đất hiếm, graphit, apatit - hóa chất phốt pho (03 nhiệm vụ); (4) phát triển chuỗi đồng, sắt - thép và khoáng sản đi kèm (01 nhiệm vụ); (5) kinh tế tuần hoàn, khu công nghiệp sinh thái, năng lượng (01 nhiệm vụ); (6) đầu tư, hạ tầng, cơ chế, chính sách, nhân lực, truyền thông (05 nhiệm vụ).')
T('d) Phương thức thực hiện: nhiệm vụ nghiên cứu, mô hình điểm thực hiện theo hình thức đặt hàng nhiệm vụ khoa học và công nghệ cấp tỉnh có doanh nghiệp đồng hành; Atlas số và kết nối dữ liệu giám sát thực hiện dưới dạng hạng mục mở rộng của hệ thống thông tin, dữ liệu về hoạt động khoáng sản (Đề án số 13 của Tỉnh ủy, Kế hoạch số 133/KH-UBND) theo hình thức thuê dịch vụ công nghệ thông tin, dùng chung hạ tầng Trung tâm dữ liệu của tỉnh và kết nối với Bài toán lớn số 8; dự án tinh chế, chế biến sâu do doanh nghiệp đầu tư; hạ tầng khu, cụm công nghiệp theo kế hoạch đầu tư công trung hạn, vốn chủ đầu tư hạ tầng và ngành điện; các nhiệm vụ kiểm kê, xúc tiến, đào tạo, truyền thông là nhiệm vụ thường xuyên theo định mức chi hiện hành.')
T('đ) Kinh phí: tổng nhu cầu từ ngân sách nhà nước dự kiến 365.000 triệu đồng cho giai đoạn 2026 - 2030, gồm: kinh phí sự nghiệp và chi thường xuyên 65.000 triệu đồng (năm 2026: 1.000; năm 2027: 14.000; năm 2028: 19.000; năm 2029: 17.000; năm 2030: 14.000 triệu đồng), trong đó ba cụm nhiệm vụ khoa học và công nghệ 22.000 triệu đồng, Atlas số và kết nối giám sát 7.000 triệu đồng, mô hình mỏ số và phòng phân tích đất hiếm, graphit 11.000 triệu đồng, kinh tế tuần hoàn 5.000 triệu đồng, xúc tiến đầu tư, hội nghị, hội thảo, khảo sát 8.000 triệu đồng, nhân lực 7.000 triệu đồng, kiểm kê dữ liệu 1.500 triệu đồng, cơ chế chính sách 1.500 triệu đồng, truyền thông, sơ kết, tổng kết 2.000 triệu đồng; và vốn đầu tư công 300.000 triệu đồng cho hạ tầng vùng nguyên liệu, khu chế biến (đường kết nối và hạ tầng khu chế biến đất hiếm vùng Xuân Ái; đường vận chuyển và hạ tầng cụm công nghiệp vùng graphit Bảo Hà - Bảo Thắng; đường vận chuyển quặng apatit; hạ tầng xử lý nước thải, khu lưu giữ, xử lý gyps, xỉ tại Khu công nghiệp Tằng Loỏng) từ nguồn thu đóng góp của tổ chức, cá nhân khai thác khoáng sản trong kế hoạch đầu tư công trung hạn 2026 - 2030 theo Quyết định số 2390/QĐ-UBND (tổng nguồn 1.594.379 triệu đồng, chưa phân bổ 1.336.931 triệu đồng), phân kỳ năm 2027: 56.000; năm 2028: 91.000; năm 2029: 83.000; năm 2030: 70.000 triệu đồng. Vốn đầu tư dự án, thiết bị giám sát tại hiện trường và hạ tầng khu, cụm công nghiệp do doanh nghiệp, chủ đầu tư hạ tầng bảo đảm, không tính vào kinh phí Kế hoạch.')
T('e) Tổ chức thực hiện: Tổ công tác liên ngành do Phó Chủ tịch UBND tỉnh làm Tổ trưởng, Sở Công Thương là cơ quan thường trực; Nhóm chuyên gia tư vấn không phát sinh chi phí; thủ trưởng cơ quan chủ trì nhiệm vụ chịu trách nhiệm trước UBND tỉnh; báo cáo hằng quý, sơ kết năm 2028, tổng kết năm 2030; điều khoản chuyển tiếp về phân công theo Nghị quyết số 66.25/2026/NQ-CP.')
T('III. KIẾN NGHỊ, ĐỀ XUẤT', bold=True)
T('1. Đề nghị UBND tỉnh xem xét, ban hành Kế hoạch thực hiện Bài toán lớn số 2 theo dự thảo kèm theo Tờ trình này.')
T('2. Để bảo đảm điều kiện thực hiện Bài toán, đề nghị UBND tỉnh: (i) giao Sở Tài chính cân đối, bố trí kinh phí sự nghiệp năm 2026 (1.000 triệu đồng), tổng hợp nhu cầu các năm 2027 - 2030 theo phân kỳ và tham mưu dành 300.000 triệu đồng từ nguồn thu đóng góp khai thác khoáng sản chưa phân bổ trong kế hoạch đầu tư công trung hạn cho danh mục công trình hạ tầng vùng nguyên liệu, khu chế biến; giao Sở Khoa học và Công nghệ đưa các nhiệm vụ khoa học và công nghệ của Bài toán vào danh mục đặt hàng năm 2027; (ii) chỉ đạo việc phân công, chuyển giao chức năng, nhiệm vụ quản lý nhà nước về địa chất, khoáng sản và khu công nghiệp giữa các cơ quan chuyên môn theo khoản 5 Điều 7 Nghị quyết số 66.25/2026/NQ-CP, trong đó chuyển giao nguyên trạng cho Sở Công Thương hồ sơ, dữ liệu, hệ thống thông tin, đề án, dự toán và biên chế, nhân sự đang thực hiện các nhiệm vụ này để bảo đảm tính liên tục và năng lực chủ trì Bài toán; (iii) cho phép Sở Công Thương cập nhật phân công tại Kế hoạch sau khi UBND tỉnh ban hành quyết định chuyển giao mà không phải trình lại toàn bộ Kế hoạch.')
T('Sở Công Thương kính trình UBND tỉnh xem xét, quyết định (hồ sơ kèm theo: dự thảo Kế hoạch, 03 phụ lục và Bảng tổng hợp tiếp thu, giải trình ý kiến)./.')
B.append(dict(text=''))  # 1 dòng trống trước khối ký (Quy tắc 22)
doc.replace_body_paragraphs(11, 34, B)

doc.replace_in_cell(1, 0, 0, '- Sở Tư pháp;', '- Sở KH&CN, Sở Tài chính;')
# Quy tắc 22: tên lãnh đạo ngang dòng Lưu — Nơi nhận 5 dòng + tiêu đề = 6; ô ký: GIÁM ĐỐC + 3 trống + tên (dòng ký 13pt cao hơn dòng nơi nhận 11pt)
_c = doc.doc.tables[1].rows[0].cells[1]
_bl = [p for p in _c.paragraphs if not p.text.strip()]
for _p in _bl[3:]:
    _p._element.getparent().remove(_p._element)

doc.replace_in_cell(1, 0, 0, 'Lưu VT; CN(Trung).', 'Lưu: VT, CN(Trang).')
out = '/home/claude/work/output/ttr_bt2.docx'
os.makedirs(os.path.dirname(out), exist_ok=True)
doc.save(out)
print('OK', out)
