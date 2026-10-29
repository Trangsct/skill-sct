# CHANGELOG - skcn-vn

## 1.3.0 — 30/10/2026 — Bác sĩ riêng tại nhà

- Thêm `references/bac-si-rieng-tai-nha.md`: tủ thuốc kèm hoạt chất, 10 quy tắc an toàn cứng, chăm sóc theo tình huống, dấu hiệu phải đi viện, nguồn thuốc app Long Châu, nhật ký các đợt ốm.
- `SKILL.md`: kích hoạt và mục "Bác sĩ riêng tại nhà". `plugin.json` → 1.3.0. Chi tiết: `CHANGELOG-v2026.10.30.md`.

## 1.2.0 — 17/10/2026 — Sửa tim_van_ban.py không tìm được số hiệu có chữ Đ

- `scripts/tim_van_ban.py` (bản chép từ gốc kho, đồng bộ bằng `build_so_cai_van_ban_goc.py`): sửa lỗi biểu thức tìm — chữ "đ" bị thay hai lần thành `[đ[dđ]]` nên MỌI số hiệu có chữ Đ (NĐ-CP, QĐ-UBND, QĐ-TTg) không bao giờ khớp và script kết luận sai "chưa có trong kho" (phát hiện 17/10/2026 khi kiểm thử GATE 0). Sau khi sửa: "181/2024/NĐ-CP" khớp 3 mục danh mục.
- `plugin.json` → 1.2.0. Chi tiết: `CHANGELOG-v2026.10.17.md`.

## [1.1.1] - 09/10/2026 — Sổ cái văn bản gốc dùng chung, bản .txt toàn văn, tim_van_ban.py, quy tắc "không được nói không có"

- `SKILL.md`: thêm khối **Tra văn bản gốc** ngay dưới tiêu đề — đọc `van-ban-goc/00-DANH-MUC-CHUNG.md`, chạy `scripts/tim_van_ban.py` trước khi kết luận văn bản chưa có; văn bản đã có thì mở bản `.txt`; cấm trả lời "chưa có trong gói", "không mở được toàn văn", "tra mạng khi cần nguyên văn"; 7 bước (a)–(g) khi Bạn gửi văn bản quy phạm; không có quyền ghi thì hướng dẫn Hộp thư `_inbox/`.
- `van-ban-goc/00-DANH-MUC-CHUNG.md` (máy sinh bởi `scripts/build_so_cai_van_ban_goc.py` ở gốc kho, giống nhau ở mọi plugin): danh mục toàn bộ văn bản gốc của 24 plugin (số hiệu, ngày, tên, plugin chủ, đường dẫn, có .txt), danh sách trùng số hiệu nhiều plugin, tệp đặt tên chưa chuẩn.
- `scripts/tim_van_ban.py` (bản chép từ gốc kho): tìm theo số hiệu/cụm từ trong danh mục, toàn văn .txt/.md mọi plugin và reference; chạy được trong gói claude.ai.
- `van-ban-goc/`: mọi tệp gốc .pdf/.doc/.docx/.xlsx có bản trích chữ `.txt` cùng tên đặt cạnh (hiện 0 tệp .txt), sinh bằng `scripts/trich_chu_van_ban_goc.py` (NFC; bản quét OCR đánh dấu `[OCR]`, số/ngày phải đối chiếu bản gốc).
- `plugin.json` → 1.1.1.

Chi tiết: `CHANGELOG-v2026.10.09.md`.

## [1.1.0] - 06/9/2026 — đưa vào repo; kế hoạch tập luyện tại nhà, chỉ số 05–06/9
- Xem `CHANGELOG-v2026.09.06.md`.

## [1.0.0] - 31/8/2026
- Bản đầu: hồ sơ nền, ngưỡng tham chiếu, lịch sử chỉ số, cảnh báo đỏ, đánh giá TPCN, chuẩn bị đi khám, sổ theo dõi CSV.
