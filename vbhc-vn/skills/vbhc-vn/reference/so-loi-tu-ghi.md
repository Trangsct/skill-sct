# Sổ lỗi tự ghi — vbhc-vn

Lỗi Bạn chỉ ra trong phiên, Claude ghi ngay theo CLAUDE.md mục "Tự ghi lỗi" (Bạn chốt 17/10/2026). Đọc tệp này trước khi
soạn văn bản thuộc lĩnh vực của plugin. Định dạng mỗi mục và cách kiểm: `scripts/check_anti_error_format.py` ở gốc kho.
Lỗi kiểm được bằng máy thì kèm quy tắc trong `qa_rules.py` (vbhc-vn) hoặc `check_facts.py` và ghi mã ở dòng "Máy kiểm".
Yêu cầu riêng cho MỘT văn bản không ghi ở đây mà ghi vào `trang-thai/<hồ sơ>.md` mục "Yêu cầu riêng một lần".

### L001 — 17/10/2026 — Khoảng cách sau "Kính gửi" và ô ký tên
- Lỗi: thân văn bản bắt đầu ngay sát dưới khối "Kính gửi" (không có dòng trống); ô ký tên hẹp, thấp hơn hẳn khối Nơi nhận nên lãnh đạo không đủ chỗ ký.
- Cách đúng: sau dòng "Kính gửi" (cả khối nhiều nơi nhận) cách đúng 1 dòng trống rồi mới vào thân văn bản; ô ký tên rộng rãi, chiều cao tương ứng các dòng của khối Nơi nhận (≥ 3 dòng trống giữa chức danh và tên người ký — H13).
- Ví dụ: "Kính gửi: Ủy ban nhân dân tỉnh Lào Cai" → (1 dòng trống) → "Thực hiện …".
- Máy kiểm: `ra_soat_doc_lap.py` mục [3]; tự sửa dòng trống sau Kính gửi: `kiem_tra_truoc_khi_giao.py --tu-sua`; checklist_ra_soat.txt dòng 4, 5.
