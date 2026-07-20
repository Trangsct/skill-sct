# Nâng cấp hnh-sct-vn v1.2.0 - 06/7/2026

## Bổ sung MẪU BIÊN BẢN THẨM ĐỊNH CHUẨN CỦA SỞ (loại 1, 2, 3, 4, 9)

Trước v1.2.0, khi soạn Biên bản thẩm định hồ sơ HHNH, skill chỉ có mẫu Biên bản của **Cục Hóa chất** (bản Đức Giang loại 5, 8) tại `vi-du-thuc-te/cuc-hoa-chat/`. Mẫu này khác thể thức, thành phần và cấu trúc bảng so với biên bản thực tế của **Sở Công Thương Lào Cai**, dẫn đến rủi ro dựng biên bản loại 1,2,3,4,9 sai mẫu (sai thành phần: ghi Trưởng phòng thay vì Phó Trưởng phòng chủ trì; sai bảng thành phần hồ sơ: thêm cột "Đạt/Không đạt" không có trong mẫu Sở; sai khối chữ ứng).

### 1. Thêm file mẫu
- **`vi-du-thuc-te/giay-phep-da-cap/Bien-ban-tham-dinh-SCT-ThaiThinh-xangdau-loai3.docx`** - Biên bản thẩm định THẬT của Sở (hồ sơ Công ty TNHH Thái Thịnh, loại 3 xăng dầu, lập 01/7/2026). Đây là **MẪU CHUẨN** để dựng mọi Biên bản thẩm định loại 1, 2, 3, 4, 9 theo Chế độ B (sửa trên file gốc, giữ nguyên định dạng).

### 2. Đặc điểm mẫu Biên bản của Sở (ghi vào reference 16 mục 3)
- Cơ quan: `UBND TỈNH LÀO CAI / SỞ CÔNG THƯƠNG`; tên: "BIÊN BẢN THẨM ĐỊNH HỒ SƠ / Phục vụ cấp Giấy phép vận chuyển hàng hóa nguy hiểm loại [x] / của [DN]".
- 04 căn cứ: NĐ 161/2024; Điều 44 NĐ 105/2025; khoản 2 Điều 8 TT 38/2025 (sửa bởi Điều 25 TT 26/2026); QĐ 1696/QĐ-UBND.
- I. THÀNH PHẦN: **Phó Trưởng phòng Trần Trọng Trang - Chủ trì** + **Chuyên viên Trần Đăng Khôi - Thành viên** (KHÔNG phải Trưởng phòng Long).
- II. NỘI DUNG VÀ KẾT QUẢ THẨM ĐỊNH: 1. Thông tin đơn vị; 2. Kết quả thẩm định a) Thành phần hồ sơ (bảng **STT | Tài liệu**, chỉ 2 cột, kèm số hiệu từng văn bản), b) phương tiện (bảng + đoạn đánh giá, lưu ý mốc kiểm định hết hạn trước thời hạn GP), c) nhân sự (lái xe bảng + người áp tải đoạn văn), d) danh mục hàng (đối chiếu Phụ lục I), đ) phương án (cam kết Điều 11); 3. Nhận xét, kiến nghị của Phòng QLCN.
- Chữ ký (bảng 1x3): NGƯỜI THẨM ĐỊNH (Khôi) | (trống) | PHÓ TRƯỞNG PHÒNG (Trang); đặt `cantSplit` để khối ký không gãy trang.

### 3. Cập nhật tài liệu
- **SKILL.md mục IV-a:** tách rõ nhóm `giay-phep-da-cap/` (mẫu chuẩn của Sở: Giấy phép + Biên bản thẩm định); ghi rõ Biên bản của Cục Hóa chất ở `cuc-hoa-chat/` **CHỈ dùng tham chiếu cho loại 5, 8**.
- **Reference 16 mục 3:** thay toàn bộ mô tả "Biên bản thẩm định hồ sơ" bằng cấu trúc thực tế của mẫu Sở + trỏ đến file; cập nhật dòng Hải Yến và dòng Thái Thịnh trong bảng tiền lệ (mục 1).
- **Reference 11 Bước 6:** lập Biên bản thẩm định theo mẫu chuẩn của Sở (Phiếu thẩm định mục 3 chỉ là bản rút gọn nội bộ).
- **Reference 15 (mục lục):** thêm dòng cho file Biên bản mẫu Sở; làm rõ mẫu Đức Giang chỉ cho loại 5, 8.

### 4. Lưu ý nghiệp vụ rút ra từ mẫu Thái Thịnh (áp dụng khi thẩm định loại 3 xăng dầu)
- Đoạn đánh giá phương tiện nêu cả GCN kiểm định ATKT&BVMT và GCN kiểm định phương tiện đo của xi téc; khống chế/lưu ý theo mốc kiểm định hết hạn sớm nhất so với thời hạn GP đề nghị (24 tháng).
- Người áp tải: nếu DN viện dẫn Điều 8 TT 37/2020 để không bố trí, ghi rõ căn cứ này dựa trên Danh mục cũ (NĐ 42/2020) đã thay thế; Phụ lục I NĐ 161 không còn cột ngưỡng khối lượng → nêu để Lãnh đạo Phòng/Sở quyết định yêu cầu bổ sung áp tải hay chấp thuận không áp tải.
- Phương án phải thể hiện cam kết Điều 11 (không qua hầm ≥100 m/phà); nếu thiếu thì đưa vào mục cần hoàn thiện.
