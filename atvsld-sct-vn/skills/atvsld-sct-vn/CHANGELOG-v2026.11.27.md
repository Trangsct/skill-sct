# atvsld-sct-vn 1.2.2 — 27/11/2026 — Tự động lấy toàn văn văn bản QPPL từ thuvienphapluat.vn

- SKILL.md: thêm khối quy trình lấy toàn văn qua Claude in Chrome (Bạn chốt 27/11/2026, chạy được 26/11/2026): thứ tự tra kho → trình duyệt; giới hạn 50.000 ký tự của get_page_text và cách lấy phần Phụ lục bằng javascript_tool; tài khoản cơ quan chỉ bấm Đăng nhập, hỏi Bạn trước khi đẩy người khác ra; lưu bản .txt vào van-ban-goc/; dựng Word khi Bạn cần.
- `plugin.json` → 1.2.2.

# atvsld-sct-vn 1.2.3 — 27/11/2026 (lần 2) — Tài khoản thuvienphapluat: luôn bấm Đồng ý

- SKILL.md khối lấy toàn văn: hiện cảnh báo "có 1 người khác bị Đăng xuất" thì bấm Đồng ý luôn, không hỏi Bạn (quy tắc cơ quan, ưu tiên người đăng nhập sau). Quy ước "hỏi Bạn trước" sáng 27/11/2026 là lịch sử.
- `plugin.json` → 1.2.3.

# atvsld-sct-vn 1.3.0 — 27/11/2026 (lần 3) — Văn bản pháp luật mới lấy toàn văn từ thuvienphapluat.vn

- NĐ 418/2026/NĐ-CP ngày 20/11/2026 sửa NĐ 143/2024 (hiệu lực 05/01/2027): toàn văn vào van-ban-goc; ref 03 bổ sung UBND cấp xã báo tai nạn chết người trong 24 giờ.
- `plugin.json` → 1.3.0.

# atvsld-sct-vn 1.3.1 — 27/11/2026 (lần 4) — Văn bản dài lấy qua Google Docs

- SKILL.md khối lấy toàn văn: thêm bước (8b) chuyển văn bản dài từ thuvienphapluat qua clipboard → Google Docs trong thư mục Drive → tải về dạng chữ (đã chạy được 27/11/2026).
- `plugin.json` → 1.3.1.
