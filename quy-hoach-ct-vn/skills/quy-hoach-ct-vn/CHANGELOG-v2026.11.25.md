# quy-hoach-ct-vn 1.9.1 — 25/11/2026 — bảng người ký theo QĐ 7750/QĐ-SCT

- SKILL.md mục VI: ý kiến quy hoạch khoáng sản — PGĐ Hoàng Văn Thuân (khai thác mỏ, chế biến) hoặc PGĐ Phạm Năng Chung (địa chất, khoáng sản còn lại; phụ trách Phòng Quản lý Khoáng sản); ý kiến về VLNCN — PGĐ Thuân từ 17/11/2026; quy hoạch điện — PGĐ Nguyễn Trường Giang. Căn cứ: QĐ 7750/QĐ-SCT ngày 17/11/2026 (thay QĐ 6320/QĐ-SCT).
- `plugin.json` 1.9.0 → 1.9.1.

# quy-hoach-ct-vn 1.10.0 — 25/11/2026 — Ranh giới số hóa 09 sơ đồ quy hoạch khoáng sản nhóm I Lào Cai (ref 15)

- Lưu file KMZ Bạn gửi 25/11/2026 (`du-lieu/00_TongHop_RanhGioi_QuyHoach_LaoCai.kmz`, file gốc) cùng bảng tọa độ CSV 123 khu vực, 1.129 điểm góc (VN-2000 KTT 105° múi 6° + WGS84) và bảng Word xuất từ file.
- Reference 15 mới: tệp, hệ tọa độ, kết quả kiểm tra (VN-2000 khớp WGS84, diện tích khớp), các khu chồng lấn, kết quả đối chiếu Phụ lục VI dự thảo điều chỉnh QĐ 866 (113/123 khớp; 10 khu vực lệch: Mường Hum, Bến Đền (1)–(3), Sinh Quyền (cu), KT 9/37, KT 28, KT 17, KT 7 KT 5 (khu 2) (1), (2)), danh mục khu vực theo bản vẽ.
- Script `scripts/tra_toa_do_quy_hoach.py`: tra theo tên, theo điểm (nằm trong khu vực nào, khu vực trong bán kính 500 m), theo bản vẽ, tổng hợp.
- Ref 08: dòng dẫn sang ref 15. SKILL.md: dòng ref 15 trong bảng mục III, thư mục `du-lieu/` ở mục IV.
- `plugin.json` 1.9.1 → 1.10.0.
