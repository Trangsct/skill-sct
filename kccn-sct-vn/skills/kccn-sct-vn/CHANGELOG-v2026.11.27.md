# kccn-sct-vn 1.71.1 — 27/11/2026 — Tự động lấy toàn văn văn bản QPPL từ thuvienphapluat.vn

- SKILL.md: thêm khối quy trình lấy toàn văn qua Claude in Chrome (Bạn chốt 27/11/2026, chạy được 26/11/2026): thứ tự tra kho → trình duyệt; giới hạn 50.000 ký tự của get_page_text và cách lấy phần Phụ lục bằng javascript_tool; tài khoản cơ quan chỉ bấm Đăng nhập, hỏi Bạn trước khi đẩy người khác ra; lưu bản .txt vào van-ban-goc/; dựng Word khi Bạn cần.
- `plugin.json` → 1.71.1.

# kccn-sct-vn 1.71.2 — 27/11/2026 (lần 2) — Tài khoản thuvienphapluat: luôn bấm Đồng ý

- SKILL.md khối lấy toàn văn: hiện cảnh báo "có 1 người khác bị Đăng xuất" thì bấm Đồng ý luôn, không hỏi Bạn (quy tắc cơ quan, ưu tiên người đăng nhập sau). Quy ước "hỏi Bạn trước" sáng 27/11/2026 là lịch sử.
- `plugin.json` → 1.71.2.

# kccn-sct-vn 1.71.3 — 27/11/2026 (lần 3) — Tờ trình Đảng ủy UBND tỉnh xin chủ trương thành lập CCN; Quy chế 19-QC/TU

- Ref 60 (mới): khuôn bộ Tờ trình của Đảng ủy UBND tỉnh (-TTr/ĐU) xin chủ trương Thường trực, Ban Thường vụ Tỉnh ủy thành lập CCN và Phiếu trình của Văn phòng UBND tỉnh; căn cứ Quy chế 19-QC/TU ngày 15/10/2026, 05-QC/ĐU ngày 12/01/2026; số liệu theo Báo cáo thẩm định thay thế; điều kiện theo khoản 3 Điều 1 NĐ 303/2026; không đưa ý kiến khác nhau.
- Sổ lỗi L004 (dẫn Quy chế cũ 02-QC/TU, 01-QC/TU); ref 33 ghi Quy chế 02-QC/TU là lịch sử.
- check_facts: rule `quy-che-lam-viec-tinh-uy-02-qc-tu-da-thay`, `quy-che-19-qc-tu-sai-nam`.
- trang-thai: ccn-tan-hop (7984/BC-SCT, 8011/TTr-SCT, 1932/VPUBND-KT); tạo thanh-lap-cum-cong-nghiep-ban-phiet-1.
- `plugin.json` → 1.71.3.
