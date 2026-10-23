# CHANGELOG — vbhc-vn v2.37.0 (23/10/2026)

- **R26 (WARN) mới:** bảng Nơi nhận - chữ ký không được đặt ô căn giữa/dưới theo chiều dọc; dòng "Nơi nhận:" phải ngang dòng chức vụ người ký (Bạn chỉ ra 23/10/2026 ở dự thảo Công văn UBND tỉnh và Tờ trình hồ sơ hóa chất). File lỗi `tests/fail/r26-khoi-ky-can-giua-doc.docx`.
- `kiem_tra_truoc_khi_giao.py --tu-sua`: thêm `sua_khoi_ky` (đặt vAlign top cho mọi ô bảng ký); sửa lỗi `sua_bang` so sánh bảng bằng `is` nên không nhận ra bảng ký và áp căn giữa dọc nhầm lên khối ký — nay so sánh `_tbl`.
- Sổ lỗi tự ghi L011; `tests/rule-inventory.md` thêm R26; SKILL.md Nhóm G và các chỗ "R01–R25" → "R01–R26".
- `plugin.json` 2.36.2 → 2.37.0.
