# CHANGELOG — xd-sct-vn

Nhật ký thay đổi của plugin (Quản lý nhà nước về xây dựng ngành Công Thương). Lịch sử trước 02/9/2026 xem CHANGELOG.md ở gốc repo (tìm theo tên plugin) và `git log -- xd-sct-vn/`.

## [1.6.3] - 09/10/2026 — Sổ cái văn bản gốc dùng chung, bản .txt toàn văn, tim_van_ban.py, quy tắc "không được nói không có"

- `SKILL.md`: thêm khối **Tra văn bản gốc** ngay dưới tiêu đề — đọc `van-ban-goc/00-DANH-MUC-CHUNG.md`, chạy `scripts/tim_van_ban.py` trước khi kết luận văn bản chưa có; văn bản đã có thì mở bản `.txt`; cấm trả lời "chưa có trong gói", "không mở được toàn văn", "tra mạng khi cần nguyên văn"; 7 bước (a)–(g) khi Bạn gửi văn bản quy phạm; không có quyền ghi thì hướng dẫn Hộp thư `_inbox/`.
- `van-ban-goc/00-DANH-MUC-CHUNG.md` (máy sinh bởi `scripts/build_so_cai_van_ban_goc.py` ở gốc kho, giống nhau ở mọi plugin): danh mục toàn bộ văn bản gốc của 24 plugin (số hiệu, ngày, tên, plugin chủ, đường dẫn, có .txt), danh sách trùng số hiệu nhiều plugin, tệp đặt tên chưa chuẩn.
- `scripts/tim_van_ban.py` (bản chép từ gốc kho): tìm theo số hiệu/cụm từ trong danh mục, toàn văn .txt/.md mọi plugin và reference; chạy được trong gói claude.ai.
- `van-ban-goc/`: mọi tệp gốc .pdf/.doc/.docx/.xlsx có bản trích chữ `.txt` cùng tên đặt cạnh (hiện 4 tệp .txt), sinh bằng `scripts/trich_chu_van_ban_goc.py` (NFC; bản quét OCR đánh dấu `[OCR]`, số/ngày phải đối chiếu bản gốc).
- 00-MUC-LUC: mục "CHƯA có trong bộ" đổi thành "Chưa có bản gốc trong kho"; NĐ 212/2026 đã có nên bỏ khỏi danh sách thiếu.
- `plugin.json` → 1.6.3.

Chi tiết: `CHANGELOG-v2026.10.09.md`.

## [1.6.0] - 24/9/2026 — NĐ 347/2026/NĐ-CP: PCCC trong KTCTNT; Điều 74 NĐ 217/2026 bị bãi bỏ
- SKILL.md: mục NĐ 347/2026 (hiệu lực 15/9/2026) trong khối cắt giảm; anti-error **15** — KTCTNT không kèm kiểm tra nghiệm thu PCCC, không đòi văn bản chấp thuận của Công an, không dẫn Điều 74 NĐ 217/2026 (bãi bỏ bởi Điều 39 NĐ 347).
- ref 01 (ghi chú Điều 74 NĐ 217), ref 04 (PCCC trong KTCTNT; trình tự PCCC hằng năm k3 Đ14), ref 08 mục C, D.
- `van-ban-goc/ND-347-2026-ND-CP-08-9-2026-sua-doi-ND-105-2025.docx` + mục lục.

## [1.5.1] - 02/9/2026 — khởi tạo CHANGELOG trong thư mục skill
- Rà soát tổng thể 02/9/2026: plugin đúng cấu trúc, description trong ngưỡng, không phát hiện dữ kiện lỗi thời cần sửa. Phiên bản giữ nguyên 1.5.1.
- Từ nay mỗi lần nâng cấp ghi mục mới lên đầu file này (theo CLAUDE.md của repo).
