# CHANGELOG — data360x-sct-vn v1.4.0 (29/10/2026)

Nguồn: Bạn yêu cầu 29/10/2026 "nâng cấp dự án data 360, hiện nay tôi đã chuyển sang trang web quản lý tài liệu mới" (ảnh
chụp danh sách Văn bản đến egov1), "tự động hóa công việc", "tự động cập nhật các thông tin mới nhất vào các plugin".

- Bot EGOV đã có (ccn-laocai PR #114): `bot-data360x.py` đọc egov1 làm cổng mặc định; Văn bản có Độ mật khác "Thường" bị bỏ.
- `SKILL.md`: khối cảnh báo EGOV viết lại — bản tin hằng ngày thứ Hai–Sáu (đọc mọi bản tin từ lần nâng cấp trước), việc chờ xử
  lý ở `theo-doi/viec-cho-xu-ly/<ngày>/` (thay vOffice), văn bản sau 10/10/2026 thì sai bot lấy qua egov1 trước khi xin Bạn gửi.
- `references/03-bot-va-may-co-quan.md` mục 7: bước 2 xong; lịch TAY 0.2.0; khảo sát cổng `theo-doi/egov/soi/<ngày-giờ>-bot/`.
- `references/05-tay-hang-doi.md`: thêm loại yêu cầu `viec`, `khao-sat` (workflow `yeu-cau.yml` chưa có hai lựa chọn này —
  ghi thẳng tệp JSON vào `yeu-cau/`).
- `plugin.json` 1.3.0 → 1.4.0.
