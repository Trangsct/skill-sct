# CHANGELOG — kccn-sct-vn v1.64.0 (05/11/2026)

Nguồn: bản giao việc xây máy chủ MCP tra cứu (plugin `tra-cuu-sct-vn`).

- `data/danh-muc-kcn-ccn-qd525.csv` (mới): danh mục máy đọc 20 KCN (5.797 ha) + 54 CCN (2.927,81 ha) theo QĐ 525/QĐ-UBND 25/02/2026, trích từ references 12, 13; kèm 11 CCN rút khỏi quy hoạch (nhóm III), Púng Luông (nhóm VI), KCN Đông Phố Mới (ngoài Phụ lục II) để tra tên; cột ghi chú ghi địa danh dễ nhầm và mốc đã có Quyết định thành lập sau QĐ 525 (Mông Sơn, Yên Hợp 2, Xuân Ái). Tổng diện tích đã kiểm khớp.
- `SKILL.md`: mục 0c — khi máy chủ tra cứu đang kết nối, ưu tiên `tra_van_ban`, `trang_thai_cum`, `danh_muc_kcn_ccn` thay cho script; bảng reference thêm dòng CSV. Hướng dẫn script cũ giữ nguyên.
- `plugin.json` 1.63.0 → 1.64.0.
