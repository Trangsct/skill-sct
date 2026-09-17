# data360x-sct-vn 1.0.2 — 17/9/2026 (c)

- Quy tắc 8: từ khóa NGẮN (số trơn, tên riêng: `Xuân Ái`, `PH Group`) — Bạn chốt 17/9/2026; bot cũng tự rút gọn.
- Quy tắc 9: một hồ sơ có nhiều tệp — bot tải đủ đính kèm (.docx có bản chữ .md); đọc cả đính kèm khi góp ý dự thảo. Kịch bản 5 mới (9500/UBND-XD). Ref 01 thêm đường dẫn đính kèm.

# data360x-sct-vn 1.0.1 — 17/9/2026 (b)

- Bot tìm bằng **ô tìm kiếm** của Data360X thay vì lật từng trang (Bạn chốt 17/9/2026); `ngay` của workflow lấy văn bản chỉ còn là đường lui. Cập nhật SKILL.md, ref 01, ref 03.
- Máy cơ quan không có bash: workflow chuyển sang PowerShell, yêu cầu đi qua tệp UTF-8 (`--lay @tệp`).

# data360x-sct-vn 1.0.0 — 17/9/2026

Plugin mới. Bạn chốt 17/9/2026: *"Data360X giống như cánh tay, chuột và bàn phím của Claude"* — khi làm việc,
Claude biết kết hợp kho văn bản đã gom và biết giao bot vào Data360X tải đúng tài liệu đang cần.

- `SKILL.md`: bức tranh 30 giây; 7 quy tắc (tra kho trước, gộp một lệnh, số/ngày lấy ở đầu tệp, không bịa,
  công khai – riêng tư, không đổi lịch, máy phải bật); 4 động tác (tra kho, sai bot lấy, quét mới, tìm viện
  dẫn); bảng "khi nào tự dùng"; liên kết plugin khác.
- `references/01-kho-theo-doi.md`: cây thư mục `theo-doi/`, từng trường của bản ghi danh mục, bản tin, bảng
  lĩnh vực ↔ plugin, tiêu chí bot tải PDF, giới hạn.
- `references/02-workflows.md`: 5 workflow (4 nút bấm + đề xuất VBPL), inputs, cách gọi bằng MCP / gh /
  script / trang web, cách chờ, bảng đọc log lỗi, mã thoát của bot.
- `references/03-bot-va-may-co-quan.md`: chế độ dòng lệnh, ràng buộc (không đăng nhập hộ, không captcha),
  runner, phiên đăng nhập và giữ phiên hằng ngày, thứ tự kiểm tra khi bot hỏng.
- `references/04-kich-ban-mau.md`: 5 kịch bản có thật với lệnh từng bước và câu trả lời mẫu.
- `scripts/tim_trong_kho.py`: tra danh mục theo từ khóa / số / lĩnh vực / ngày / nguồn; `--ban-tin`; `--doc`;
  đọc từ bản clone hoặc GitHub API.
- `scripts/goi_bot.py`: gửi lệnh workflow, chờ (3 phút rồi mỗi 2 phút, tối đa 40 phút), in README kết quả
  hoặc bản tin; `trang-thai` xem nhịp tim máy.

Kèm theo ở kho khác (cùng ngày): bot `--lay` (ccn-laocai), workflow `lay-van-ban.yml` và `giu-phien.yml`
(vlncn-laocai).
