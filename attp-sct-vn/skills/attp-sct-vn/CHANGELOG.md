# CHANGELOG - attp-sct-vn

## v1.3.0 - 29/7/2026
ĐÍNH CHÍNH KẾT LUẬN SAI của v1.2.0 về hộ kinh doanh, dựa trên 02 công văn hướng dẫn của Bộ Công Thương.

- **Nạp bản gốc CV 3109/BCT-KHCN ngày 20/4/2018 và CV 8520/BCT-KHCN ngày 30/12/2021** vào `van-ban-goc/`.
- **ĐẢO KẾT LUẬN**: v1.2.0 kết luận hộ có địa điểm cố định mà sản xuất, chế biến thực phẩm thì phải cấp Giấy chứng nhận, bất kể quy mô. **SAI**. Kết luận đúng: **mọi hộ kinh doanh thực phẩm ngành Công Thương đều không thuộc diện cấp Giấy chứng nhận, chỉ gửi bản cam kết đến UBND cấp xã, kể cả khi có hoạt động sản xuất, chế biến.**
- Chuỗi căn cứ 3 bước: (1) **khoản 10 Điều 3 NĐ 15/2018** - cơ sở kinh doanh thực phẩm nhỏ lẻ được định nghĩa theo **hình thức đăng ký** (đã đăng ký hộ kinh doanh), không theo công suất hay doanh thu; (2) **điểm d khoản 1 Điều 12** - kinh doanh thực phẩm nhỏ lẻ không thuộc diện cấp GCN; (3) **mục 1 CV 3109/BCT-KHCN** - dẫn khoản 16 Điều 4 Luật Doanh nghiệp, sản xuất thực phẩm nhỏ lẻ là một công đoạn trong hoạt động kinh doanh thực phẩm nhỏ lẻ.
- **Nghĩa vụ thay thế** (CV 8520/BCT-KHCN): đáp ứng khoản 1 Điều 22 Luật ATTP và gửi bản cam kết theo khoản 2 Điều 10 NĐ 17/2020/NĐ-CP; tại Lào Cai nộp tại UBND cấp xã theo khoản 8 Điều 7 QĐ 28/2025.
- **GỠ GATE của v1.2.0** về việc ai ký GCN cho hộ kinh doanh ngành Công Thương. Không phải lỗ hổng văn bản: QĐ 28/2025 Điều 6 và Điều 7 khoản 7 chỉ ghi "Quản lý" vì hộ kinh doanh không bao giờ cần GCN.
- **Bổ sung từ CV 3109**: TT 57/2015/TT-BCT không còn hiệu lực; Điều 40-43 Mục 7 Chương VI NĐ 77/2016 đã bị bãi bỏ bởi khoản 14 Điều 18 NĐ 08/2018 - điều kiện với cơ sở nhỏ lẻ chỉ còn khoản 1 Điều 22 Luật ATTP. Mục 3: cơ sở khoản 9 Điều 36 thuộc diện phải cấp GCN thì đơn vị QLNN ngành Công Thương thẩm định, cấp. Mục 4: cơ sở sản xuất rượu thủ công nhằm mục đích kinh doanh đăng ký hộ kinh doanh là cơ sở nhỏ lẻ. Mục 5: siêu thị vừa sản xuất vừa kinh doanh chỉ cấp 01 GCN.
- **GATE mới thay thế**: khi kết luận một cơ sở phải cấp GCN, bắt buộc rà đủ 3 nguồn theo thứ tự - định nghĩa Điều 3 NĐ 15/2018, danh mục Điều 12, công văn hướng dẫn của Bộ Công Thương. Thiếu nguồn nào thì dừng.
- reference 09 viết lại toàn bộ (141 dòng): kết luận chốt đặt ở mục 0; mục 1 ghi lại lỗi đã mắc để không lặp; 3 trường hợp ngoại lệ (doanh nghiệp và hợp tác xã, phần dịch vụ ăn uống, sản phẩm ngành khác); Điều 36 khoản 8-9-10; 5 việc xã phải làm; mục 10 cảnh báo câu không được viết trong công văn hướng dẫn.
- reference 04 đính chính đoạn kết luận, dẫn sang reference 09.
- Ghi nhận: các nghị quyết cắt giảm TTHC 2026 (NQ 19/2026, NQ 66.16/2026, NQ 66.18/2026) điều chỉnh thành phần hồ sơ cấp GCN nên không ảnh hưởng tuyến xã.

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
