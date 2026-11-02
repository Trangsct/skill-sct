# Sổ lỗi tự ghi — hnh-sct-vn

Lỗi Bạn chỉ ra trong phiên, Claude ghi ngay theo CLAUDE.md mục "Tự ghi lỗi" (Bạn chốt 17/10/2026). Đọc tệp này trước khi
soạn văn bản thuộc lĩnh vực của plugin. Định dạng mỗi mục và cách kiểm: `scripts/check_anti_error_format.py` ở gốc kho.
Lỗi kiểm được bằng máy thì kèm quy tắc trong `qa_rules.py` (vbhc-vn) hoặc `check_facts.py` và ghi mã ở dòng "Máy kiểm".
Yêu cầu riêng cho MỘT văn bản không ghi ở đây mà ghi vào `trang-thai/<hồ sơ>.md` mục "Yêu cầu riêng một lần".

### L001 — 02/11/2026 — Kết luận Sở không có thẩm quyền với tiền chất thuốc nổ loại 5.1
- Lỗi: thẩm định hồ sơ vận chuyển amoni nitrat và 05 muối clorat, perclorat, nitrat (loại 5.1), kết luận hàng là tiền chất thuốc nổ nên ngoài thủ tục HHNH, dự thảo công văn từ chối. Nguyên nhân: plugin ghi "trừ VLNCN, tiền chất thuốc nổ" như loại trừ chung. Bạn chỉ ra hai Giấy phép amoni nitrat Bộ, Cục đã cấp trước đó.
- Cách đúng: phần "trừ vật liệu nổ công nghiệp, tiền chất thuốc nổ" chỉ áp trong loại 1. Tiền chất loại 5.1 thụ lý như loại 5 (khoản 1 Điều 8), cấp Giấy phép HHNH kèm câu "không thay thế giấy phép vận chuyển, giấy phép nhập khẩu tiền chất thuốc nổ"; giấy phép của Công an cấp song song. Nguyên tắc 30.
- Ví dụ: tiền lệ 516/GP-BCT (6/2025), 112/GP-HC (11/2025), 5869/GP-SCT ngày 21/9/2026.
- Máy kiểm: check_facts `hnh-tien-chat-loai-5-van-cap-phep`
