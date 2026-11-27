# qlks-sct-vn 2.11.1 — 27/11/2026 — Tự động lấy toàn văn văn bản QPPL từ thuvienphapluat.vn

- SKILL.md: thêm khối quy trình lấy toàn văn qua Claude in Chrome (Bạn chốt 27/11/2026, chạy được 26/11/2026): thứ tự tra kho → trình duyệt; giới hạn 50.000 ký tự của get_page_text và cách lấy phần Phụ lục bằng javascript_tool; tài khoản cơ quan chỉ bấm Đăng nhập, hỏi Bạn trước khi đẩy người khác ra; lưu bản .txt vào van-ban-goc/; dựng Word khi Bạn cần.
- `plugin.json` → 2.11.1.

# qlks-sct-vn 2.11.2 — 27/11/2026 (lần 2) — Tài khoản thuvienphapluat: luôn bấm Đồng ý

- SKILL.md khối lấy toàn văn: hiện cảnh báo "có 1 người khác bị Đăng xuất" thì bấm Đồng ý luôn, không hỏi Bạn (quy tắc cơ quan, ưu tiên người đăng nhập sau). Quy ước "hỏi Bạn trước" sáng 27/11/2026 là lịch sử.
- `plugin.json` → 2.11.2.

# qlks-sct-vn 2.12.0 — 27/11/2026 (lần 3) — Văn bản pháp luật mới lấy toàn văn từ thuvienphapluat.vn

- NĐ 402/2026/NĐ-CP ngày 06/11/2026 sửa NĐ 114/2018 (hiệu lực 20/12/2026): toàn văn vào van-ban-goc; ref 17 bổ sung (bỏ nghĩa vụ Sở báo cáo vận hành hồ chứa thủy điện k5 Đ13; Sở được lấy ý kiến phương án cắm mốc chỉ giới đập thủy điện); ghi chú mẫu 07.
- `plugin.json` → 2.12.0.

# qlks-sct-vn 2.12.1 — 27/11/2026 (lần 4) — Văn bản dài lấy qua Google Docs

- SKILL.md khối lấy toàn văn: thêm bước (8b) chuyển văn bản dài từ thuvienphapluat qua clipboard → Google Docs trong thư mục Drive → tải về dạng chữ (đã chạy được 27/11/2026).
- `plugin.json` → 2.12.1.
