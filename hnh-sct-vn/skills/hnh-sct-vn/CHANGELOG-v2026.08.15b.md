# hnh-sct-vn v1.8.0 - 15/8/2026 - Bộ hồ sơ doanh nghiệp mẫu chuẩn NHÓM LOẠI 8 + quy tắc biển kiểm soát

Nguồn: bộ hồ sơ Công ty TNHH thương mại du lịch và vận tải Hà Tân (mã số 5300821912) đề nghị cấp Giấy phép vận chuyển 09 chất ăn mòn loại 8; Sở rà soát, chỉnh sửa và Bạn duyệt ngày 15/8/2026.

## Thêm mới

- `vi-du-thuc-te/ha-tan-axit-loai8-082026/` - **bộ hồ sơ doanh nghiệp mẫu đầu tiên của nhóm loại 8**: 04 tệp docx (Giấy đề nghị, Bảng kê người lái xe và người áp tải, Bảng kê phương tiện, Phương án tổ chức vận chuyển) + README.
  - 09 chất loại 8, tổng 28.100 tấn/năm; đáng chú ý UN 2031 có 03 phân mức nồng độ cho 03 số hiệu nguy hiểm khác nhau (885 / 85 / 80) và UN 2032 khói đỏ (856).
  - Hàng đi trong **công-ten-nơ bồn (ISO tank)** trên tổ hợp đầu kéo 24H-018.08 và sơ mi rơ moóc tải chở container 24RM-004.80 - dạng chứa hàng khác hẳn nhóm loại 2, 3 vốn dùng xi téc gắn cố định.
  - Thời hạn đề nghị 24 tháng; chuẩn thể thức A4, lề 2/2/3/2, bảng đúng 16 cm vùng in.

## Nguyên tắc nghiệp vụ mới (SKILL.md mục VII)

- **Nguyên tắc 20 - biển kiểm soát KHÔNG kèm hậu tố** (V), (T) in trên Chứng nhận đăng ký xe. Mọi hồ sơ, biên bản, phiếu trình, công văn, Giấy phép chỉ ghi phần biển số. Thay thế hướng dẫn cũ "ghi đủ hậu tố" tại reference 11.
- **Nguyên tắc 21 - soát chéo cả 04 tệp của bộ hồ sơ doanh nghiệp**, 07 điểm: thời hạn đề nghị; dạng chứa hàng; hạng GPLX; phạm vi loại hàng; địa danh theo đơn vị hành chính hiện hành; số/ngày để trống thống nhất; danh mục thành phần hồ sơ khớp thứ tự đánh số của bộ.

## Sửa các reference

- `references/11-tham-dinh-quy-trinh.md`: sửa dòng hậu tố biển trong bảng đối chiếu mở rộng cho khớp nguyên tắc 20; thêm **lỗi thẩm định 17, 18, 19** (chép hậu tố biển; không kiểm dạng chứa hàng với ISO tank; đọc từng tệp rời không soát chéo); thêm lưu ý hai hệ hạng GPLX cũ và mới tồn tại song song, không tự quy đổi.
- `references/16-thuc-tien-cap-phep-sct.md`: thêm **mục 9** - đặc thù nhóm loại 8 (ISO tank; Điều 11 NĐ 161 không áp dụng vì loại 8 không phải chất dễ cháy, nổ; mã TTHC 1.013340; mốc 14/8/2026 để chọn mô hình trình ký), 06 điểm doanh nghiệp hay thiếu, chuẩn thể thức khi Sở chỉnh giúp hồ sơ, hạng GPLX hai hệ song song.

## Sửa lỗi tồn

- **Description SKILL.md vượt ngưỡng 1024 ký tự** (1130 ký tự, phát sinh từ v1.7.0 khi bổ sung QĐ 2848) → rút gọn còn 1014 ký tự, giữ đủ từ khóa kích hoạt và bổ sung từ khóa nhóm loại 8.

## Phiên bản

`plugin.json`: 1.7.0 → **1.8.0**; description plugin bổ sung cụm bộ hồ sơ mẫu nhóm loại 8.
