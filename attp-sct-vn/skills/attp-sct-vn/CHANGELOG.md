# CHANGELOG - attp-sct-vn

## v1.2.0 - 29/7/2026
Đóng hai lỗ hổng GATE và mở tuyến nghiệp vụ cấp xã.

- **Nạp bản gốc Nghị định 15/2018/NĐ-CP** vào `van-ban-goc/` (bản .doc Bạn cung cấp + bản .txt trích được để grep). Trước đó reference 04 tự dặn "mở file gốc NĐ 15/2018 để đọc, không viết theo trí nhớ" nhưng file không tồn tại - GATE bị vô hiệu hóa. Nay đã đóng.
- **reference 04** bổ sung danh mục đầy đủ khoản 1 Điều 12 (điểm a đến k) và khoản 2, trích từ bản gốc; nhấn mạnh **không có mục "sản xuất thực phẩm nhỏ lẻ"** trong danh mục miễn.
- **reference 09 MỚI - hộ kinh doanh nhỏ lẻ và vai trò UBND cấp xã**: ranh giới quản lý theo loại đăng ký kinh doanh (QĐ 28/2025 Điều 6, Điều 7 khoản 7, 8, 9); phân loại 3 nhóm A (phải cấp GCN) - B (miễn, nộp cam kết tại xã) - C (dịch vụ ăn uống/hỗn hợp); điều kiện soi khi kiểm tra (Điều 19, 22 Luật ATTP); hồ sơ và thời hạn (Điều 34, 36, 37 Luật ATTP); quy trình 6 bước cho công chức xã; thẩm quyền xử phạt theo Điều 5 NĐ 189/2025; ví dụ nghiệp vụ hộ sản xuất bánh mỳ kèm 10 câu hỏi kiểm tra tại hiện trường.
- **GATE MỚI chưa gỡ**: QĐ 28/2025 chỉ ghi thẩm quyền "Cấp Giấy chứng nhận" tại Điều 4 khoản 4 (Sở Y tế) và Điều 7 khoản 2 (UBND cấp xã, mảng dịch vụ ăn uống); Điều 6 (Sở Công Thương) và Điều 7 khoản 7 (hộ kinh doanh ngành Công Thương) chỉ ghi "Quản lý". Chưa xác định được ai ký GCN cho hộ kinh doanh ngành Công Thương - cấm suy diễn, phải hỏi lại (reference 09 mục 2).
- **Đã đối chiếu bản gốc và chốt**: Phụ lục IV NĐ 15/2018 nhóm "Bánh, mứt, kẹo" gồm mục 2 "Bánh bít cốt, bánh mì nướng và các loại bánh nướng tương tự", mục 3 "Bánh bột nhào", mục 4 "Bánh mì giòn", mục 5 "Bánh gato", mục 11 "Các sản phẩm bánh mứt kẹo khác" - tức bánh mỳ thuộc ngành Công Thương.
- **Sửa lỗi validate**: `description` trong `plugin.json` từ 597 xuống 451 ký tự (giới hạn 500 - gói cũ sẽ bị trình upload từ chối). `description` trong SKILL.md giữ dưới 1024.
- SKILL.md: thêm dòng kích hoạt cho việc hướng dẫn, tập huấn công chức cấp xã; cập nhật bản đồ references và danh sách việc còn thiếu.


## v1.1.0 - 28/7/2026
Nạp bộ tài liệu thực tế của Sở (2 archive ATTP và Thuốc lá do Bạn cung cấp).

- **reference 01** viết mới hoàn toàn theo **QĐ 28/2025/QĐ-UBND ngày 10/11/2025** (hiệu lực 20/11/2025, thay QĐ 08/2021 Yên Bái và QĐ 45/2024 Lào Cai): 6 nguyên tắc phân cấp, nhiệm vụ Sở Công Thương (Điều 6), ranh giới doanh nghiệp cấp tỉnh - hộ kinh doanh thuộc cấp xã (Điều 7), Sở Y tế, Sở NN&MT, trách nhiệm báo cáo về Sở Y tế; QCVN mới TT 09, 10, 39/2026/TT-BCT.
- **reference 02** viết mới: chuỗi thẩm quyền 3 tầng (NĐ 146/2025 khoản 5 Điều 37 + Phụ lục XI → TT 38/2025 khoản 2 Điều 16 sửa TT 43/2018 → QĐ 904/QĐ-UBND ủy quyền lập Đoàn thẩm định); trình tự thực tế 6 bước; thành phần hồ sơ; 4 nhóm điều kiện thẩm định tại cơ sở; bài học Chế độ B.
- **GATE mới:** QĐ 904/QĐ-UBND chỉ ủy quyền **đến hết 31/12/2025** → cấm viện dẫn như đang còn hiệu lực, phải hỏi Bạn về QĐ thay thế năm 2026.
- **reference 03, 04, 05, 07** viết mới: tự công bố (quy trình nội bộ Sở, bảng ai tiếp nhận theo chủ thể), cơ sở không thuộc diện cấp GCN và nghĩa vụ bản cam kết, hậu kiểm - xử phạt - sự cố, rượu bia (chuỗi GCN ATTP → Giấy phép sản xuất rượu, chỉ tiêu kiểm nghiệm QCVN 6-3:2010/BYT).
- **reference 06** bổ sung mục 6: TT 57/2018 và TT 43/2023; mẫu Quyết định thành lập Đoàn thẩm định; 3 lỗi hợp đồng ủy thác theo CV 2534/SCT-CN ngày 17/11/2025; cảnh báo file mẫu đặt tên sai (nội dung là hồ sơ mua bán, không phải chế biến).
- Thêm 05 biểu mẫu, hướng dẫn thật vào `mau-ho-so/`; 02 bộ ví dụ thực tế (Siêu thị An Lạc, Kim Ngọc); 06 văn bản gốc vào `van-ban-goc/`.
- SKILL.md: bổ sung văn bản của tỉnh vào khung pháp lý, thêm GATE ủy quyền, cập nhật bản đồ references và danh sách 7 việc còn thiếu.

## v1.0.0 - 28/7/2026
Khởi tạo plugin An toàn thực phẩm và công nghiệp tiêu dùng - thực phẩm.

- SKILL.md: phạm vi kích hoạt, bảng liên kết hệ sinh thái plugin, khung pháp lý, nguyên tắc bất biến, bản đồ references.
- GATE HIỆU LỰC ATTP: NĐ 46/2026 tạm ngưng theo NQ 15/2026, tiếp tục áp dụng NĐ 15/2018 (reference 08).
- reference 06 (thuốc lá): đính chính thẩm quyền Giấy phép chế biến nguyên liệu thuốc lá đã phân cấp về UBND cấp tỉnh theo khoản 5 Điều 18 NĐ 146/2025; điều kiện cắt giảm còn 02 theo NQ 19/2026.
