# vbhc-vn 2.40.1 — 16/11/2026

- R02 (công thức hóa học phải có chỉ số dưới thật) không còn bắt nhầm công thức KHÔNG có chữ số (KOH, NaOH, CaO, NaCl, MgO, ZnO) — viết phẳng là đúng. Vụ thật: bảng hóa chất của biên bản kiểm tra phòng ngừa, ứng phó sự cố hóa chất báo FAIL ở dòng KOH, NaOH. Thêm `tests/test_r02.py` (mục 8 của `run_regression.py`): 3 trường hợp — không chữ số không báo, H2SO4/P2O5 phẳng phải báo, H₂SO₄ có run subscript không báo.

# vbhc-vn 2.40.0 — 16/11/2026

- Nơi nhận có "Ban Giám đốc Sở", dòng Lưu ghi lại tên chuyên viên soạn thảo `CN(Tên)` (trừ Giấy phép, Giấy chứng nhận thủ tục hành chính). Máy kiểm: R07 đảo (WARN khi thiếu tên), R22 thu hẹp còn GP/GCN, R28 mới (WARN khi thiếu Ban Giám đốc Sở). `build_vb.py --nguoi-soan`, `TemplateDoc.save(ra, nguoi_soan=)` điền tên; `chuan_hoa_dong_luu` không còn xóa tên; `kiem_tra_truoc_khi_giao.py` báo dòng Lưu thiếu tên. File lỗi mẫu r07b, r22, r28; baseline WARN chốt lại (13 cảnh báo R07 trên mẫu thật biến mất vì mẫu thật vốn ghi tên). Quy tắc mới: Bạn bảo "hoàn thiện" → gửi thư cho chuyên viên phụ trách.
- Nguồn: Bạn chốt 16/11/2026 "bổ sung nơi nhận - Ban Giám đốc Sở và có ghi tên chuyên viên soạn thảo phía dưới như quy ước trước đây (trừ Giấy phép, giấy chứng nhận của thủ tục hành chính)". Quy ước 01/10/2026 (bỏ tên) và 13/10/2026 (thủ tục hành chính không gửi Ban Giám đốc Sở) là lịch sử.
