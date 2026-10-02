# CHANGELOG — vbhc-vn v2.28.0 (01/10/2026)

Bạn chốt 01/10/2026: từ nay không ghi tên chuyên viên ở cuối văn bản — dòng Lưu chỉ ghi `Lưu: VT, CN.` (công văn nội bộ Phòng `Lưu: CN.`).

- Quy tắc bất biến 6/18, Nhóm G, phong-tranh-sai-lam, the-thuc-van-phong, templates-chi-tiet, cong-thuc-thuc-chien, quy-trinh-hai-che-do, thu-vien-mau-that, README: dòng Lưu ghi `Lưu: VT, CN.` (nội bộ Phòng `Lưu: CN.`), bỏ quy ước "CN (Tên)".
- `scripts/fill_template.py`: hàm mới `chuan_hoa_dong_luu()`; `TemplateDoc.save()` và `build_vb.py` gọi hàm này nên văn bản dựng từ mẫu thật cũ (còn "CN(Trung)", "CN (Khôi)") tự bỏ tên.
- `qa_rules.py` R07: bỏ WARN "thiếu khoảng trắng trước ngoặc", thay bằng WARN "còn tên chuyên viên ở dòng Lưu"; baseline WARN chốt lại (5 mẫu thật cũ có tên); thêm ca thử `tests/fail/r07b-dong-luu-con-ten-chuyen-vien`.
- Template trắng 02, 03, 04, 05, 06, 08: dòng Lưu về `Lưu: VT, CN.` / `Lưu: CN.`; demo_cong_van, demo_quyet_dinh bỏ bước điền tên.
- 26 mẫu thật trong `examples/` giữ nguyên (văn bản đã ban hành).
- `plugin.json` → 2.28.0.
