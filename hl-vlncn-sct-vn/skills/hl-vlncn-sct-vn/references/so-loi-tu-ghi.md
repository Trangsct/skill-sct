# Sổ lỗi tự ghi — hl-vlncn-sct-vn

Lỗi Bạn chỉ ra trong phiên, Claude ghi ngay theo CLAUDE.md mục "Tự ghi lỗi" (Bạn chốt 17/10/2026). Đọc tệp này trước khi
soạn văn bản thuộc lĩnh vực của plugin. Định dạng mỗi mục và cách kiểm: `scripts/check_anti_error_format.py` ở gốc kho.
Lỗi kiểm được bằng máy thì kèm quy tắc trong `qa_rules.py` (vbhc-vn) hoặc `check_facts.py` và ghi mã ở dòng "Máy kiểm".
Yêu cầu riêng cho MỘT văn bản không ghi ở đây mà ghi vào `trang-thai/<hồ sơ>.md` mục "Yêu cầu riêng một lần".

### L001 — 23/10/2026 — Số định danh trên Giấy chứng nhận thiếu số 0 ở đầu
- Lỗi: Giấy chứng nhận số 31/GCN-SCT ngày 27/01/2026 (theo QĐ 458/QĐ-SCT) in "Số định danh" 11 chữ số, rơi số 0 đầu (danh sách lập trên Excel để cột dạng số). Doanh nghiệp chép lại số sai này vào thông báo gửi Sở; CSDL trang vlncn-laocai cũng nhập theo bản sai. Phát hiện khi rà thông báo bổ sung thủ kho ngày 23/10/2026 (sd-vlncn-sct-vn ref 14, anti-error 38).
- Cách đúng: số định danh cá nhân luôn đủ 12 chữ số, giữ số 0 đầu; cột số định danh trong danh sách kèm Quyết định công nhận và trong tệp dựng GCN phải để dạng văn bản (Text), soát độ dài 12 trước khi in.
- Ví dụ: "Số định danh: 0xxxxxxxxxxx" (12 chữ số), không "xxxxxxxxxxx" (11 chữ số).
- Máy kiểm: check_facts rule `so-dinh-danh-du-12-chu-so` (WARN) cho tài liệu plugin; dữ liệu Excel phải soát tay khi dựng GCN.
