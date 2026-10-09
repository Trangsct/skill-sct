# CHANGELOG — sd-vlncn-sct-vn v2026.10.9.1 (09/10/2026)

Sổ cái văn bản gốc dùng chung, bản .txt toàn văn, công cụ tìm và quy tắc "không được nói không có" (Bạn chốt 09/10/2026, áp dụng mọi plugin — bản giao việc sau vụ QCVN 01:2019/BCT).

- `SKILL.md`: thêm khối **Tra văn bản gốc** ngay dưới tiêu đề — đọc `van-ban-goc/00-DANH-MUC-CHUNG.md`, chạy `scripts/tim_van_ban.py` trước khi kết luận văn bản chưa có; văn bản đã có thì mở bản `.txt`; cấm trả lời "chưa có trong gói", "không mở được toàn văn", "tra mạng khi cần nguyên văn"; 7 bước (a)–(g) khi Bạn gửi văn bản quy phạm; không có quyền ghi thì hướng dẫn Hộp thư `_inbox/`.
- `van-ban-goc/00-DANH-MUC-CHUNG.md` (máy sinh bởi `scripts/build_so_cai_van_ban_goc.py` ở gốc kho, giống nhau ở mọi plugin): danh mục toàn bộ văn bản gốc của 24 plugin (số hiệu, ngày, tên, plugin chủ, đường dẫn, có .txt), danh sách trùng số hiệu nhiều plugin, tệp đặt tên chưa chuẩn.
- `scripts/tim_van_ban.py` (bản chép từ gốc kho): tìm theo số hiệu/cụm từ trong danh mục, toàn văn .txt/.md mọi plugin và reference; chạy được trong gói claude.ai.
- `van-ban-goc/`: mọi tệp gốc .pdf/.doc/.docx/.xlsx có bản trích chữ `.txt` cùng tên đặt cạnh (hiện 2 tệp .txt), sinh bằng `scripts/trich_chu_van_ban_goc.py` (NFC; bản quét OCR đánh dấu `[OCR]`, số/ngày phải đối chiếu bản gốc).
- INDEX văn bản gốc: bỏ câu "Chưa có trong gói (tra mạng/hỏi Bạn khi cần nguyên văn)" về QCVN 01:2019/BCT và TT 26/2026/TT-BCT, thay bằng đường dẫn toàn văn (.doc/.docx + .txt) tại kho-vlncn-sct-vn và qlks-sct-vn.
- `plugin.json` → 2026.10.9.1.
