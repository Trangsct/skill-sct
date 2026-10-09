# CHANGELOG — atvsld-sct-vn

## [1.0.2] - 09/10/2026 — Sổ cái văn bản gốc dùng chung, bản .txt toàn văn, tim_van_ban.py, quy tắc "không được nói không có"

- `SKILL.md`: thêm khối **Tra văn bản gốc** ngay dưới tiêu đề — đọc `van-ban-goc/00-DANH-MUC-CHUNG.md`, chạy `scripts/tim_van_ban.py` trước khi kết luận văn bản chưa có; văn bản đã có thì mở bản `.txt`; cấm trả lời "chưa có trong gói", "không mở được toàn văn", "tra mạng khi cần nguyên văn"; 7 bước (a)–(g) khi Bạn gửi văn bản quy phạm; không có quyền ghi thì hướng dẫn Hộp thư `_inbox/`.
- `van-ban-goc/00-DANH-MUC-CHUNG.md` (máy sinh bởi `scripts/build_so_cai_van_ban_goc.py` ở gốc kho, giống nhau ở mọi plugin): danh mục toàn bộ văn bản gốc của 24 plugin (số hiệu, ngày, tên, plugin chủ, đường dẫn, có .txt), danh sách trùng số hiệu nhiều plugin, tệp đặt tên chưa chuẩn.
- `scripts/tim_van_ban.py` (bản chép từ gốc kho): tìm theo số hiệu/cụm từ trong danh mục, toàn văn .txt/.md mọi plugin và reference; chạy được trong gói claude.ai.
- `van-ban-goc/`: mọi tệp gốc .pdf/.doc/.docx/.xlsx có bản trích chữ `.txt` cùng tên đặt cạnh (hiện 2 tệp .txt), sinh bằng `scripts/trich_chu_van_ban_goc.py` (NFC; bản quét OCR đánh dấu `[OCR]`, số/ngày phải đối chiếu bản gốc).
- `plugin.json` → 1.0.2.

Chi tiết: `CHANGELOG-v2026.10.09.md`.

## [1.0.0] - 02/9/2026 — khởi tạo
- Plugin ATVSLĐ phần ngành Công Thương, dựng từ 2 bản gốc Bạn cung cấp: Luật 84/2015/QH13 và NĐ 283/2026/NĐ-CP (hiệu lực 10/9/2026, thay NĐ 12/2022).
- Kết luận nền (nguyên văn): điểm d k1 Đ33 Luật giao Bộ Công Thương QLNN máy, thiết bị, vật tư, chất nghiêm ngặt nhóm áp lực/nâng đặc thù CN/hóa chất/VLNCN/mỏ/dầu khí; NĐ 283/2026 không trao thẩm quyền lập biên bản hay xử phạt cho Sở Công Thương (Đ54, 55–63) → Sở CHUYỂN Sở Nội vụ; hành vi KTAT mỏ, VLNCN, hóa chất Sở XỬ theo NĐ 36/2020, 275/2026.
- 6 references: 01 khung pháp lý + ranh giới (nguyên văn Đ14, 28–36, 82–89 Luật; Đ54, 55, 61, 63 NĐ 283); 02 máy thiết bị nhóm Công Thương (nêu mâu thuẫn k2 Đ30 Luật ↔ k1 Đ35 NĐ 283 về nơi khai báo); 03 TNLĐ, sự cố; 04 xử phạt (nguyên văn Đ3, 7, 31–38, 66, 67; bảng XỬ/CHUYỂN); 05 huấn luyện; 06 báo cáo, Tháng hành động, Hội đồng.
- GATE rõ ràng: NĐ 39/2016, NĐ 44/2016, TT 36/2019, TT 06/2020, TT 09/2017/TT-BCT chưa có bản gốc — không dẫn điều khoản/mã thiết bị.
- Người ký PGĐ Hoàng Văn Thuân; chuyên viên CN(Linh); PTP Trang (theo sct-laocai-org-vn).
