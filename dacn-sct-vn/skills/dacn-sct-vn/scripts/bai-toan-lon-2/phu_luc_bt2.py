# -*- coding: utf-8 -*-
"""Phụ lục Kế hoạch v8 (14/9/2026): PL I bảng phân công nhiệm vụ 6 cột theo form Kế hoạch đã ban hành của UBND tỉnh
(gộp nhiệm vụ, lộ trình, kinh phí); PL II Danh mục dự án thu hút đầu tư (13 dự án)."""

SUB = "(Kèm theo Kế hoạch số:          /KH-UBND ngày        tháng        năm 2026 của Ủy ban nhân dân tỉnh Lào Cai)"

# ------------------------------------------------------------------ PHỤ LỤC I
H1 = ["Nội dung", "Phân công nhiệm vụ", "Tiến độ", "Phương pháp", "Nguồn lực", "Sản phẩm đầu ra"]
W1 = [6.6, 4.4, 3.2, 3.8, 2.6, 4.1]
TX = "Chi thường xuyên của cơ quan chủ trì (không tính riêng); vốn đầu tư của doanh nghiệp."

R1 = [
    ["1. Kiểm kê, cân đối nguồn nguyên liệu và xây dựng cơ chế chuyển hóa lợi thế tài nguyên thành giá trị gia tăng cao: rà soát từng mỏ, khai trường theo năm mức trạng thái; danh mục mỏ, khai trường bị vướng kèm nguyên nhân, trách nhiệm, phương án xử lý; bảng cân đối nguồn nguyên liệu - công suất chế biến từng chuỗi; bộ tiêu chí lựa chọn dự án khai thác gắn chế biến sâu; danh mục khu vực không đấu giá quyền khai thác đối với nguyên liệu cho nhà máy chế biến đang hoạt động; cơ chế ưu tiên cho tổ chức có cơ sở chế biến sâu; chính sách hỗ trợ theo NQ 193/2025/QH15; kiểm soát bán nguyên liệu trung gian, xuất khẩu thô; tham mưu UBND tỉnh kiến nghị Trung ương về cấm hoặc hạn chế xuất khẩu khoáng sản thô, sơ chế, thuế xuất khẩu nguyên liệu trung gian, ưu đãi chế biến sâu.\n(Sản phẩm 1 tại TB 78/TB-UBND)",
     "Chủ trì: Sở Công Thương.\nPhối hợp: Sở Tài chính, Sở NN&MT, Sở KH&CN, Sở Tư pháp, Thuế tỉnh, Thống kê tỉnh, UBND các xã, phường, doanh nghiệp.",
     "Khởi động quý IV/2026; báo cáo kiểm kê, bảng cân đối nguồn quý II/2027; bộ tiêu chí, danh mục khu vực không đấu giá, cơ chế ưu tiên quý IV/2027; cập nhật hằng quý đến 2030.",
     "Sở tự thực hiện bằng bộ máy hiện có: khảo sát, làm việc với doanh nghiệp, hội thảo, rà soát chính sách; Tổ công tác liên ngành xử lý điểm nghẽn.",
     "NSNN 1.500 triệu đồng (chi thường xuyên: khảo sát, hội thảo, rà soát chính sách).",
     "Báo cáo kiểm kê, phân loại trạng thái nguồn nguyên liệu; bảng cân đối nguồn - công suất chế biến ba chuỗi; danh mục điểm nghẽn; bộ tiêu chí, danh mục khu vực không đấu giá, cơ chế ưu tiên được ban hành; văn bản kiến nghị Trung ương."],
    ["2. Xây dựng Danh mục dự án thu hút đầu tư công nghiệp khai thác và tinh chế nguyên liệu và xúc tiến đầu tư có mục tiêu: cụ thể hóa Phụ lục II thành hồ sơ cơ hội đầu tư từng dự án (nguyên liệu, sản phẩm, địa điểm, quỹ đất, hạ tầng, quy hoạch, ưu đãi, đầu mối); trình UBND tỉnh phê duyệt, cập nhật hằng năm; hằng năm 01 hội nghị xúc tiến chuyên đề, 01 hội thảo khoa học, 01 đoàn công tác tiếp cận tập đoàn có công nghệ nguồn về hóa chất phốt pho, vật liệu pin, đồng kỹ thuật, luyện kim; kết nối doanh nghiệp chủ chuỗi với doanh nghiệp hạ nguồn trong nước; ấn phẩm xúc tiến đa ngôn ngữ.\n(Sản phẩm 2, 3 tại TB 78/TB-UBND)",
     "Chủ trì: Sở Công Thương.\nPhối hợp: Sở Tài chính, BQL Khu kinh tế tỉnh, BQL các KCN tỉnh, Sở NN&MT, Sở Xây dựng, Trung tâm XTĐT, TM&DL tỉnh, doanh nghiệp chủ chuỗi.",
     "Danh mục và hồ sơ cơ hội đầu tư trình phê duyệt quý II/2027; hội nghị xúc tiến lần thứ nhất năm 2027; xúc tiến hằng năm 2027 - 2030; cập nhật Danh mục hằng năm.",
     "Lập hồ sơ cơ hội đầu tư; xúc tiến đầu tư có địa chỉ; hội nghị, hội thảo, đoàn công tác theo định mức hiện hành; kết nối doanh nghiệp chủ chuỗi - hạ nguồn.",
     "NSNN 5.000 triệu đồng (chi thường xuyên: hội nghị, hội thảo, công tác, thông tin tuyên truyền).",
     "Danh mục và các hồ sơ cơ hội đầu tư được UBND tỉnh phê duyệt, bổ sung vào Danh mục dự án thu hút đầu tư của tỉnh; biên bản ghi nhớ, hợp đồng bao tiêu; 02 - 03 dự án tinh chế, chế biến sâu quy mô lớn được quyết định đầu tư trước 2030 (phấn đấu)."],
    ["3. Khơi thông nguồn nguyên liệu và tháo gỡ điểm nghẽn theo từng dự án: hoàn thành GPMB, thuê đất khai trường 24, 25 (xã Bát Xát), 19b (xã Cốc San), Cam Đường 2, khai trường 19 (phường Cam Đường); nâng huy động công suất 03 nhà máy tuyển Apatit Việt Nam và 02 nhà máy tuyển mới; phối hợp Bộ Công Thương cân đối quặng apatit toàn quốc; ổn định nguồn quặng đồng; đôn đốc mỏ Quý Xa vào khai thác; đôn đốc, hỗ trợ đưa các dự án đất hiếm Bến Đền, Yên Phú, graphit Nậm Thi, Bảo Hà vào khai thác; xử lý giấy phép hết hạn, dự án chậm tiến độ theo hướng gắn chế biến sâu; xử lý điểm nghẽn theo danh mục nhiệm vụ 1, báo cáo Tổ công tác hằng quý.\n(Sản phẩm 3 tại TB 78/TB-UBND - điều kiện về nguyên liệu)",
     "Chủ trì: Sở Công Thương (cân đối nguồn, cấp phép, theo dõi); Sở NN&MT và UBND các xã, phường (GPMB, thuê đất, môi trường).\nPhối hợp: Sở Tài chính, Công an tỉnh, BQL Khu kinh tế tỉnh, doanh nghiệp.",
     "Mặt bằng các khai trường apatit trọng điểm hoàn thành năm 2027; mỏ Quý Xa vào khai thác năm 2027; tỷ lệ huy động công suất tuyển apatit 50% năm 2027, 80% năm 2030; đất hiếm, graphit vào khai thác trước 2030; điểm nghẽn xử lý hằng quý.",
     "Nhiệm vụ thường xuyên; Nhà nước tháo gỡ mặt bằng, thủ tục; doanh nghiệp thực hiện dự án theo giấy phép; Tổ công tác họp hằng quý.",
     TX,
     "Mặt bằng các khai trường apatit trọng điểm; mỏ Quý Xa vận hành; các nhà máy tuyển, luyện đồng ổn định; mỏ đất hiếm Bến Đền và ít nhất 01 dự án graphit vào khai thác trước 2030 (phấn đấu); báo cáo xử lý điểm nghẽn hằng quý."],
    ["4. Phát triển chuỗi apatit - hóa chất phốt pho lên sản phẩm tinh chế, chế biến sâu: hỗ trợ nhà máy axit phốt phoric cấp điện tử 60.000 tấn/năm vận hành thương mại; xúc tiến các dự án sử dụng phốt pho vàng sản xuất hóa chất phốt pho tinh khiết cao, muối phốt phát cho pin lithium sắt phốt phát, phốt pho đỏ, hợp chất phốt pho chuyên dụng; không mở rộng công suất phốt pho vàng; dự án tuyển quặng loại II, IV, tận thu quặng đuôi; dự án tái chế gyps, xỉ; cân đối axit sunfuric giữa luyện đồng và hóa chất phốt pho; theo dõi cấp phép hóa chất, an toàn hóa chất.\n(Sản phẩm 3 tại TB 78/TB-UBND)",
     "Chủ trì: Sở Công Thương.\nPhối hợp: BQL Khu kinh tế tỉnh, Sở KH&CN, Sở NN&MT, Công an tỉnh, UBND xã Tằng Loỏng, Tập đoàn Hóa chất Đức Giang, Tập đoàn Hóa chất Việt Nam, Công ty TNHH MTV Apatit Việt Nam.",
     "Nhà máy axit điện tử hoàn thành đầu tư quý IV/2026, vận hành thương mại năm 2027; dự án hóa chất phốt pho tinh khiết cao được quyết định đầu tư năm 2029 (phấn đấu); dự án tái chế gyps, xỉ triển khai 2027 - 2030.",
     "Dự án đầu tư của doanh nghiệp; xúc tiến theo nhiệm vụ 2; nghiên cứu theo nhiệm vụ 7; Nhà nước bảo đảm hạ tầng ngoài hàng rào, thủ tục.",
     TX,
     "Nhà máy axit phốt phoric cấp điện tử vận hành; ít nhất 01 dự án sử dụng phốt pho vàng sản xuất hóa chất phốt pho tinh khiết cao được quyết định đầu tư trước 2030; dự án tái chế gyps, xỉ được triển khai; sản phẩm phốt pho chuyển dần từ bán nguyên liệu trung gian sang tinh chế tại tỉnh."],
    ["5. Phát triển chuỗi đồng và chuỗi sắt - thép lên sản phẩm hạ nguồn: xúc tiến dự án sử dụng đồng tấm sản xuất dây, cáp điện, thanh cái, đồng kỹ thuật; thu hồi vàng, bạc, đất hiếm, khoáng sản đi kèm từ quặng đuôi tuyển đồng; chuyển đổi thải khô; ổn định nguồn quặng Quý Xa cho luyện kim tại tỉnh; chuẩn bị điều kiện quy hoạch, hạ tầng, môi trường cho khu liên hợp gang thép Võ Lao theo KH 283/KH-UBND; thu hồi khoáng sản đi kèm từ đất đá thải; không lặp lại nội dung đã có tại KH 283/KH-UBND.\n(Sản phẩm 3 tại TB 78/TB-UBND)",
     "Chủ trì: Sở Công Thương.\nPhối hợp: BQL Khu kinh tế tỉnh, Sở NN&MT, Sở KH&CN, UBND các xã Bát Xát, Trịnh Tường, Hợp Thành, Văn Bàn, Tằng Loỏng, Tổng công ty Khoáng sản - TKV, Công ty Khoáng sản và Luyện kim Việt Trung, doanh nghiệp.",
     "Báo cáo điều kiện khu liên hợp gang thép Võ Lao năm 2027; mô hình thu hồi khoáng sản từ quặng đuôi tuyển đồng năm 2028; dự án sử dụng đồng tấm được quyết định đầu tư năm 2029 (phấn đấu).",
     "Dự án đầu tư của doanh nghiệp; xúc tiến theo nhiệm vụ 2; nghiên cứu theo nhiệm vụ 7; thực hiện theo KH 283/KH-UBND.",
     TX,
     "Ít nhất 01 dự án sử dụng đồng tấm được quyết định đầu tư trước 2030 (phấn đấu); ít nhất 01 mô hình thu hồi khoáng sản từ quặng đuôi tuyển đồng; báo cáo điều kiện cho khu liên hợp gang thép Võ Lao."],
    ["6. Lớp dữ liệu nguyên liệu chiến lược và giám sát sản lượng trực tuyến: tiếp nhận, vận hành liên tục hệ thống thông tin, dữ liệu về hoạt động khoáng sản (KH 133/KH-UBND) theo NQ 66.25/2026/NQ-CP; lớp dữ liệu chuyên đề: bản đồ số vùng nguyên liệu gắn cơ sở chế biến, dữ liệu sản phẩm, cân bằng vật chất; kết nối trạm cân, camera, đối soát sản lượng với dữ liệu thuế, hải quan, điện năng theo Luật Địa chất và khoáng sản, NĐ 193/2025/NĐ-CP; liên thông cơ sở dữ liệu quốc gia theo KL 83-KL/TW; tuân thủ kiến trúc Bài toán lớn số 8; không xây dựng hệ thống mới.\n(Sản phẩm 4 tại TB 78/TB-UBND)",
     "Chủ trì: Sở Công Thương.\nPhối hợp: Sở NN&MT (bàn giao), Sở KH&CN, Công an tỉnh, Thuế tỉnh, Chi cục Hải quan khu vực VII, Công ty Điện lực Lào Cai, Sở Tài chính, doanh nghiệp.",
     "Tiếp nhận hệ thống quý IV/2026; lớp dữ liệu nghiệm thu, vận hành quý IV/2027; 80% doanh nghiệp kết nối năm 2028, 100% năm 2029; duy trì đến 2030.",
     "Hạng mục mở rộng hệ thống hiện có; thuê dịch vụ công nghệ thông tin; thiết bị hiện trường do doanh nghiệp đầu tư.",
     "NSNN 4.000 triệu đồng (thuê dịch vụ CNTT, chi thường xuyên).",
     "Hệ thống được tiếp nhận, vận hành liên tục; lớp dữ liệu nguyên liệu chiến lược được nghiệm thu, vận hành; 100% doanh nghiệp khoáng sản chiến lược kết nối dữ liệu sản lượng; quy chế cập nhật, chia sẻ dữ liệu."],
    ["7. Nghiên cứu, chuyển giao công nghệ tinh chế và kinh tế tuần hoàn: đặt hàng nhiệm vụ KH&CN cấp tỉnh về tuyển quặng apatit loại II, IV, quặng nghèo, nâng thu hồi P2O5; hóa chất phốt pho tinh khiết cao từ phốt pho vàng; nâng hệ số thu hồi đồng, thu hồi vàng, bạc, đất hiếm từ quặng đuôi; tái chế gyps, xỉ phốt pho, xỉ luyện kim; mỗi nhiệm vụ có doanh nghiệp tiếp nhận, kinh phí đối ứng, sản phẩm mẫu; đề xuất nhiệm vụ đủ điều kiện tham gia Chương trình quốc gia theo QĐ 1493/QĐ-TTg; Đề án KCN sinh thái Tằng Loỏng; kiểm kê khí nhà kính, tiết kiệm năng lượng theo Chỉ thị 26-CT/TU; đề xuất nhiệm vụ về đất hiếm, graphit khi có nguồn nguyên liệu và đối tác cụ thể.\n(Sản phẩm 5, 6 tại TB 78/TB-UBND)",
     "Chủ trì: Sở KH&CN (nhiệm vụ KH&CN); Sở NN&MT (chất thải, quan trắc); BQL Khu kinh tế tỉnh (Đề án KCN sinh thái).\nPhối hợp: Sở Công Thương (đề xuất đầu bài, lựa chọn doanh nghiệp tiếp nhận), viện nghiên cứu, trường đại học, doanh nghiệp.",
     "Đặt hàng đợt 1 năm 2027, đợt 2 năm 2028; chuyển giao quy trình đầu tiên năm 2028; nghiệm thu đợt 2 năm 2029; Đề án KCN sinh thái trình phê duyệt năm 2028; mô hình kinh tế tuần hoàn thứ nhất 2028, thứ hai 2030.",
     "Đặt hàng nhiệm vụ KH&CN cấp tỉnh (tuyển chọn hoặc giao trực tiếp); kinh phí đối ứng của doanh nghiệp; đề xuất tham gia Chương trình quốc gia.",
     "NSNN 16.000 triệu đồng (sự nghiệp KH&CN); kinh phí đối ứng của doanh nghiệp.",
     "Ít nhất 06 nhiệm vụ KH&CN được triển khai; ít nhất 03 quy trình công nghệ được chuyển giao vào sản xuất; ít nhất 02 mô hình kinh tế tuần hoàn; Đề án KCN sinh thái Tằng Loỏng được phê duyệt, triển khai."],
    ["8. Nhân lực, truyền thông, theo dõi và đánh giá: kế hoạch đào tạo, bồi dưỡng về mỏ, tuyển khoáng, luyện kim, hóa chất, tự động hóa, quản lý khoáng sản sau chuyển giao chức năng; liên kết viện, trường, cơ sở giáo dục nghề nghiệp; truyền thông về định hướng chế biến sâu, hạn chế xuất khẩu thô và vùng dự án; bộ chỉ số theo dõi; kiểm tra hằng năm; sơ kết 2028, tổng kết 2030.\n(Sản phẩm 7 tại TB 78/TB-UBND)",
     "Chủ trì: Sở Công Thương.\nPhối hợp: Sở Nội vụ, Sở KH&CN, Sở GD&ĐT, Sở VH,TT&DL, Báo và Đài PT-TH tỉnh, cơ sở đào tạo, doanh nghiệp.",
     "Kế hoạch đào tạo và bộ chỉ số theo dõi quý II/2027; đào tạo, truyền thông, kiểm tra hằng năm; sơ kết năm 2028; tổng kết năm 2030.",
     "Nhiệm vụ thường xuyên theo định mức đào tạo, bồi dưỡng, thông tin tuyên truyền, hội nghị; liên kết cơ sở đào tạo; doanh nghiệp tự đào tạo.",
     "NSNN 3.500 triệu đồng (sự nghiệp đào tạo, chi thường xuyên); kinh phí đào tạo của doanh nghiệp.",
     "Kế hoạch đào tạo 2026 - 2030; ít nhất 800 lượt người được đào tạo, bồi dưỡng; sản phẩm truyền thông hằng năm; bộ chỉ số theo dõi; báo cáo kiểm tra, sơ kết, tổng kết."],
    ["Tổng kinh phí dự kiến từ ngân sách nhà nước giai đoạn 2026 - 2030: 30.000 triệu đồng (năm 2026: 500; năm 2027: 6.500; năm 2028: 9.000; năm 2029: 8.000; năm 2030: 6.000), gồm: nhiệm vụ 1: 1.500; nhiệm vụ 2: 5.000; nhiệm vụ 6: 4.000; nhiệm vụ 7: 16.000; nhiệm vụ 8: 3.500; các nhiệm vụ 3, 4, 5 thực hiện bằng chi thường xuyên của cơ quan chủ trì và vốn đầu tư của doanh nghiệp. Hạ tầng vùng nguyên liệu, khu chế biến sử dụng kế hoạch đầu tư công trung hạn đã được phê duyệt tại Quyết định số 2390/QĐ-UBND, không phát sinh nhu cầu vốn mới."],
]

PL1 = dict(
    title_lines=["PHỤ LỤC I: PHÂN CÔNG NHIỆM VỤ THỰC HIỆN KẾ HOẠCH PHÁT TRIỂN CÔNG NGHIỆP KHAI THÁC",
                 "VÀ TINH CHẾ NGUYÊN LIỆU PHỤC VỤ PHÁT TRIỂN CÔNG NGHỆ CHIẾN LƯỢC",
                 "GIAI ĐOẠN 2026 - 2030, TẦM NHÌN ĐẾN NĂM 2050"],
    sub=SUB, headers=H1, rows=R1, widths=W1, font=10.5, group_rows={8},
    note="Ghi chú: Kinh phí nêu tại Phụ lục là kinh phí dự kiến từ ngân sách nhà nước, được xác định cụ thể theo dự toán hằng năm và quyết định của cấp có thẩm quyền; vốn đầu tư các dự án khai thác, tuyển, luyện, tinh chế, chế biến sâu và thiết bị giám sát tại hiện trường do doanh nghiệp bảo đảm. Cơ quan chủ trì cụ thể hóa tiến độ theo tháng trong kế hoạch chi tiết, gửi Sở Công Thương tổng hợp; mốc phụ thuộc quyết định đầu tư của doanh nghiệp hoặc thẩm quyền của Trung ương là mốc phấn đấu.",
)

# ------------------------------------------------------------------ PHỤ LỤC II
H2 = ["TT", "Tên dự án", "Địa điểm dự kiến", "Nguyên liệu đầu vào (từ sản phẩm hiện có của tỉnh)",
      "Sản phẩm, quy mô định hướng", "Trạng thái; hình thức", "Cơ quan đầu mối; nhà đầu tư"]
W2 = [0.9, 4.5, 3.2, 3.6, 5.3, 3.6, 3.6]

R2 = [
    ["A. CHUỖI APATIT - HÓA CHẤT PHỐT PHO"],
    ["1", "Nhà máy sản xuất axit phốt phoric cấp điện tử", "KCN Tằng Loỏng", "Phốt pho vàng sản xuất tại tỉnh", "Axit phốt phoric cấp điện tử 60.000 tấn/năm phục vụ công nghiệp điện tử, bán dẫn", "Đang đầu tư; theo tiến độ đăng ký hoàn thành quý IV/2026", "Sở Công Thương; BQL Khu kinh tế tỉnh. Công ty TNHH MTV Đức Giang Lào Cai"],
    ["2", "Nhà máy hóa chất phốt pho tinh khiết cao và muối phốt phát cho pin", "KCN Tằng Loỏng", "Phốt pho vàng, axit phốt phoric sản xuất tại tỉnh", "Axit phốt phoric tinh khiết cao, muối phốt phát (lithium sắt phốt phát và tiền chất) cho pin, hóa chất điện tử; quy mô theo đề xuất của nhà đầu tư", "Kêu gọi đầu tư mới; dự án đầu tư của doanh nghiệp", "Sở Công Thương; BQL Khu kinh tế tỉnh. Nhà đầu tư trong nước, nước ngoài có công nghệ nguồn"],
    ["3", "Nhà máy phốt pho đỏ và hợp chất phốt pho chuyên dụng", "KCN Tằng Loỏng", "Phốt pho vàng sản xuất tại tỉnh", "Phốt pho đỏ, hợp chất phốt pho cho vật liệu chống cháy, phụ gia điện tử, hóa chất tinh khiết; quy mô theo đề xuất của nhà đầu tư", "Kêu gọi đầu tư mới", "Sở Công Thương; BQL Khu kinh tế tỉnh. Doanh nghiệp phốt pho vàng hiện có và đối tác"],
    ["4", "Dự án tuyển quặng apatit loại II, IV và tận thu quặng đuôi", "Vùng Cam Đường, Bát Xát, Tằng Loỏng", "Quặng apatit loại II, IV, quặng đuôi các nhà máy tuyển", "Tinh quặng apatit từ quặng nghèo, quặng đuôi; mở rộng nguồn nguyên liệu, giảm lãng phí tài nguyên", "Kêu gọi đầu tư mới, gắn nhiệm vụ KH&CN tuyển quặng nghèo", "Sở Công Thương. Công ty TNHH MTV Apatit Việt Nam và doanh nghiệp tuyển khoáng"],
    ["5", "Nhà máy tái chế gyps, xỉ phốt pho làm vật liệu xây dựng, phụ gia xi măng", "KCN Tằng Loỏng", "Gyps, xỉ phốt pho, xỉ lò phát sinh tại tổ hợp hóa chất", "Vật liệu xây dựng, phụ gia xi măng, thạch cao; xử lý căn cơ bãi thải theo Chỉ thị 26-CT/TU", "Kêu gọi đầu tư mới; kinh tế tuần hoàn", "Sở Công Thương; Sở NN&MT; Sở Xây dựng. Doanh nghiệp hóa chất, sản xuất vật liệu xây dựng"],
    ["6", "Dự án thu hồi flo và sản xuất hóa chất flo từ chế biến apatit", "KCN Tằng Loỏng", "Khí, dung dịch chứa flo phát sinh khi sản xuất DAP, supe lân, phốt pho vàng", "Axit flosilicic, nhôm florua, axit HF và hóa chất flo cho luyện nhôm, điện tử; tận thu flo trong quặng apatit", "Kêu gọi đầu tư mới; kinh tế tuần hoàn", "Sở Công Thương; BQL Khu kinh tế tỉnh. Doanh nghiệp hóa chất phốt pho hiện có và đối tác"],
    ["B. CHUỖI ĐỒNG"],
    ["7", "Nhà máy sản xuất dây, cáp điện, thanh cái và đồng kỹ thuật", "KCN Tằng Loỏng hoặc khu, cụm công nghiệp gắn chế biến sâu", "Đồng catot (đồng tấm) sản xuất tại tỉnh", "Dây, cáp điện, thanh cái, đồng kỹ thuật cho thiết bị điện, máy điện; quy mô theo đề xuất của nhà đầu tư", "Kêu gọi đầu tư mới", "Sở Công Thương; BQL Khu kinh tế tỉnh. Doanh nghiệp luyện đồng cùng các đối tác hạ nguồn"],
    ["8", "Dự án thu hồi vàng, bạc, đất hiếm, tinh quặng sắt (magnetit), lưu huỳnh và khoáng sản đi kèm từ quặng đồng, quặng đuôi tuyển đồng, xỉ luyện đồng; chuyển đổi thải khô", "Khu vực nhà máy tuyển Sin Quyền, Tả Phời; KCN Tằng Loỏng", "Quặng đồng, quặng đuôi tuyển đồng, xỉ luyện đồng", "Kim loại quý, đất hiếm, tinh quặng sắt, lưu huỳnh thu hồi; giảm hồ thải, tận thu tài nguyên", "Kêu gọi đầu tư mới, gắn nhiệm vụ KH&CN", "Sở Công Thương; Sở KH&CN. Tổng công ty Khoáng sản - TKV, doanh nghiệp tuyển đồng"],
    ["C. CHUỖI SẮT - THÉP"],
    ["9", "Khai thác mỏ sắt Quý Xa", "Xã Văn Bàn", "Quặng sắt Quý Xa", "Quặng sắt 5 triệu tấn/năm cung cấp cho luyện kim tại tỉnh và trong nước", "Đang triển khai (GP 199/GP-BNNMT ngày 14/7/2026)", "Sở Công Thương. Công ty Khoáng sản và Luyện kim Việt Trung"],
    ["10", "Khu liên hợp gang thép Võ Lao", "KCN Võ Lao", "Quặng sắt Quý Xa và các mỏ trên địa bàn", "Gang, phôi, thép theo KH 283/KH-UBND và Chiến lược ngành thép (QĐ 261/QĐ-TTg); quy mô theo quy hoạch và đề xuất của nhà đầu tư", "Kêu gọi đầu tư theo KH 283/KH-UBND (phấn đấu)", "Sở Công Thương; BQL Khu kinh tế tỉnh. Nhà đầu tư luyện kim"],
    ["11", "Dự án tuyển nâng cấp quặng sắt nghèo và thu hồi khoáng sản đi kèm từ đất đá thải, quặng đuôi các mỏ sắt", "Các mỏ sắt Quý Xa, Làng Lếch, Làng Vinh và mỏ sắt khác", "Quặng sắt nghèo, đất đá thải, quặng đuôi", "Tinh quặng sắt chất lượng cao cho luyện kim; khoáng sản đi kèm thu hồi; giảm bãi thải", "Kêu gọi đầu tư mới, gắn nhiệm vụ KH&CN", "Sở Công Thương; Sở NN&MT. Doanh nghiệp khai thác sắt và đối tác"],
    ["D. ĐẤT HIẾM, GRAPHIT VÀ KHOÁNG SẢN KHÁC: ĐẾN 2030 KHÔI PHỤC KHAI THÁC; CHẾ BIẾN SÂU THEO TẦM NHÌN ĐẾN NĂM 2050"],
    ["12", "Khai thác, chế biến đất hiếm Bến Đền", "Xã Gia Phú, xã Bảo Thắng", "Quặng đất hiếm Bến Đền", "Tinh quặng, sản phẩm chế biến đất hiếm theo giấy phép và quy hoạch; chế biến trong nước", "Đến 2030: khôi phục, đưa vào khai thác (GP 197/GP-BNNMT ngày 13/7/2026)", "Sở Công Thương. Công ty CP Công nghiệp Khánh An"],
    ["13", "Nhà máy thủy luyện, chiết tách đất hiếm gắn vùng nguyên liệu Yên Phú, Bến Đền", "Vùng Xuân Ái hoặc địa điểm theo quy hoạch", "Tinh quặng đất hiếm của tỉnh", "Tổng oxit đất hiếm, oxit riêng cho nam châm, linh kiện điện tử", "Tầm nhìn 2050; trong kỳ chuẩn bị điều kiện, kiến nghị quy hoạch khi có nhà đầu tư cụ thể", "Sở Công Thương; Sở KH&CN. Nhà đầu tư có công nghệ nguồn"],
    ["14", "Khai thác, tuyển graphit Nậm Thi, Bảo Hà", "Xã Bảo Thắng, xã Bảo Hà", "Quặng graphit", "Tinh quặng graphit phục vụ chế biến trong nước", "Đến 2030: đưa vào khai thác, tuyển; xử lý dự án chậm tiến độ gắn chế biến sâu", "Sở Công Thương. Chủ đầu tư các dự án đã cấp phép"],
    ["15", "Nhà máy tinh chế graphit độ sạch cao, vật liệu cực dương pin và vật liệu chịu lửa, điện cực", "Cụm công nghiệp vùng Bảo Hà - Bảo Thắng hoặc KCN", "Tinh quặng graphit của tỉnh", "Graphit độ sạch cao, vật liệu cực dương pin; điện cực, vật liệu chịu lửa cho luyện kim tại chỗ", "Tầm nhìn 2050; trong kỳ chuẩn bị điều kiện, kêu gọi khi có nguồn nguyên liệu", "Sở Công Thương; Sở KH&CN. Nhà đầu tư có công nghệ nguồn"],
    ["Đ. CÁC DỰ ÁN KHÁC"],
    ["16", "Dự án thu hồi, chế biến khoáng sản đi kèm, sản phẩm phụ và chất thải (quặng đuôi, xỉ, gyps, đất đá thải) hoặc chế biến sâu khác phù hợp định hướng của Kế hoạch do nhà đầu tư đề xuất", "Theo đề xuất của nhà đầu tư, phù hợp quy hoạch", "Khoáng sản, sản phẩm trung gian, chất thải của các chuỗi trên địa bàn", "Sản phẩm tinh chế, vật liệu, hóa chất phục vụ công nghệ chiến lược; theo đề xuất của nhà đầu tư", "Danh mục mở; bổ sung khi có đề xuất đủ điều kiện", "Sở Công Thương. Nhà đầu tư trong nước, nước ngoài"],
    ['Ghi chú: Danh mục là danh mục mở, mang tính định hướng kêu gọi đầu tư: mỗi loại khoáng sản có thể thu hồi, chế biến thành nhiều sản phẩm và khoáng sản đi kèm; nhà đầu tư được đề xuất dự án ngoài Danh mục phù hợp định hướng của Kế hoạch; Danh mục được cụ thể hóa thành hồ sơ cơ hội đầu tư (nhiệm vụ 2), trình UBND tỉnh phê duyệt để bổ sung, cập nhật Danh mục dự án thu hút đầu tư của tỉnh ban hành tại Quyết định số 1382/QĐ-UBND và cập nhật hằng năm; tổng mức đầu tư, công suất, công nghệ do nhà đầu tư đề xuất theo quy định của pháp luật về đầu tư; dự án đang đầu tư, đang hoàn thiện thủ tục được đưa vào để theo dõi, hỗ trợ; dự án không còn đáp ứng điều kiện thì đưa ra khỏi Danh mục.'],
]

PL2 = dict(
    title_lines=["PHỤ LỤC II: DANH MỤC DỰ ÁN THU HÚT ĐẦU TƯ CÔNG NGHIỆP KHAI THÁC",
                 "VÀ TINH CHẾ NGUYÊN LIỆU PHỤC VỤ PHÁT TRIỂN CÔNG NGHỆ CHIẾN LƯỢC",
                 "GIAI ĐOẠN 2026 - 2030, TẦM NHÌN ĐẾN NĂM 2050"],
    sub=SUB, headers=H2, rows=R2, widths=W2, font=9.5, group_rows={0, 7, 10, 14, 19, 21},
    note=None,
)
