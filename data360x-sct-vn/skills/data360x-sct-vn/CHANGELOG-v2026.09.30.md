# data360x-sct-vn 1.1.0 — 30/9/2026

- Reference 05 mới: **TAY và hàng đợi `yeu-cau/`** — tiến trình TAY (`ccn-laocai/tay/tay.py`) trên laptop/máy
  bàn tự kéo việc từ `vlncn-laocai/yeu-cau/*.json` mỗi 10 phút thay cho GitHub runner; định dạng tệp yêu cầu,
  ba cách ghi (MCP `create_or_update_file`, workflow `yeu-cau.yml`, script), cách chờ và đọc kết quả, nhịp tim
  `trang-thai/tay.json`. Bối cảnh: bot ngừng 11 ngày (18–29/9), runner lên laptop hỏng 3 lần, lượt online bị
  cổng từ chối; Bạn chốt 30/9/2026 xây lại theo `ccn-laocai/bot/KE-HOACH-XAY-LAI.md`.
- `scripts/goi_bot.py`: thêm `--qua-tay` (ghi vào hàng đợi rồi chờ `trang_thai` xong/loi); `trang-thai` in thêm
  nhịp tim TAY.
- SKILL.md: mục I và quy tắc 7 nói rõ hai đường (TAY ưu tiên, runner cũ tạm giữ); description nhắc hàng đợi TAY.
