# CHANGELOG — plugin dat-dai-sct-vn

## [1.2.1] - 09/10/2026 — Sổ cái văn bản gốc dùng chung, bản .txt toàn văn, tim_van_ban.py, quy tắc "không được nói không có"

- `SKILL.md`: thêm khối **Tra văn bản gốc** ngay dưới tiêu đề — đọc `van-ban-goc/00-DANH-MUC-CHUNG.md`, chạy `scripts/tim_van_ban.py` trước khi kết luận văn bản chưa có; văn bản đã có thì mở bản `.txt`; cấm trả lời "chưa có trong gói", "không mở được toàn văn", "tra mạng khi cần nguyên văn"; 7 bước (a)–(g) khi Bạn gửi văn bản quy phạm; không có quyền ghi thì hướng dẫn Hộp thư `_inbox/`.
- `van-ban-goc/00-DANH-MUC-CHUNG.md` (máy sinh bởi `scripts/build_so_cai_van_ban_goc.py` ở gốc kho, giống nhau ở mọi plugin): danh mục toàn bộ văn bản gốc của 24 plugin (số hiệu, ngày, tên, plugin chủ, đường dẫn, có .txt), danh sách trùng số hiệu nhiều plugin, tệp đặt tên chưa chuẩn.
- `scripts/tim_van_ban.py` (bản chép từ gốc kho): tìm theo số hiệu/cụm từ trong danh mục, toàn văn .txt/.md mọi plugin và reference; chạy được trong gói claude.ai.
- `van-ban-goc/`: mọi tệp gốc .pdf/.doc/.docx/.xlsx có bản trích chữ `.txt` cùng tên đặt cạnh (hiện 1 tệp .txt), sinh bằng `scripts/trich_chu_van_ban_goc.py` (NFC; bản quét OCR đánh dấu `[OCR]`, số/ngày phải đối chiếu bản gốc).
- `plugin.json` → 1.2.1.

Chi tiết: `CHANGELOG-v2026.10.09.md`.

## [1.2.0] - 02/10/2026 — Nạp thêm 9 văn bản (QĐ 40, 43, 47/2026, QĐ 18, 20/2025 của tỉnh; Luật 43/2024, Luật 146/2025; NĐ 101/2024, NĐ 226/2025); hoàn tất đối chiếu
- Reference 13 (mới): QĐ 40/2026/QĐ-UBND — 16 khoản phân cấp cho Chủ tịch UBND cấp xã (thu hồi đất, phê duyệt phương án, cưỡng chế, cho thuê đất trả tiền hằng năm cho tổ chức trừ dự án từ 2 xã trở lên); QĐ 47/2026/QĐ-UBND — trình tự khi thỏa thuận trên 75%, thu hồi trước khi phê duyệt phương án, giao đất, cho thuê đất không quá 15 ngày làm việc.
- Reference 12: thêm QĐ 18/2025 (mức thưởng bàn giao sớm 3%, hỗ trợ ổn định sản xuất kinh doanh 30% một năm thu nhập sau thuế, trách nhiệm các ngành), QĐ 20/2025 (cây trồng, vật nuôi), QĐ 43/2026 (chỉ áp dụng sản phẩm dùng ngân sách nhà nước).
- Reference 11: thẩm quyền Chủ tịch UBND cấp xã đã khớp bản gốc QĐ 40/2026; xác định các mốc 02, 03, 05 ngày làm việc và 30 ngày làm việc là hướng dẫn riêng của Sổ tay (QĐ 47/2026 không đặt các mốc này); hiệu lực Luật Đất đai 01/8/2024 theo Luật 43/2024; NĐ 101/2024 khớp.
- Sửa reference 01, 02, 03, 04, 06, 09 và SKILL.md (quy tắc hành văn 7, 8).
- `registry/trang-thai.csv`: thêm 9 văn bản; sửa dòng Luật 31/2024.
- Còn thiếu: Bộ đơn giá bồi thường nhà, công trình; Bộ đơn giá cây trồng, vật nuôi; văn bản hợp nhất Luật Đất đai.

## [1.1.0] - 02/10/2026 — Nạp bản gốc 14 văn bản; đối chiếu Sổ tay với bản gốc; văn bản của tỉnh về giá đất, bồi thường nhà xưởng, tách thửa
- `van-ban-goc/trung-uong/` (11 tệp): Luật Đất đai 31/2024/QH15; NQ 254/2025/QH15; NĐ 71, 88, 102/2024; NĐ 151/2025; NĐ 49, 50/2026; NQ 66.3/2025, NQ 66.11/2026; Văn bản 1153/BNNMT-QLĐĐ. `van-ban-goc/tinh/` (3 tệp): NQ 19/2025/NQ-HĐND, QĐ 21/2025/QĐ-UBND, QĐ 49/2026/QĐ-UBND.
- Reference 11 (mới): bảng điều khoản đã khớp; 07 điểm Sổ tay dẫn chưa đúng hoặc chưa đủ (Điều 5 và mẫu 45-48 NĐ 151/2025 hết hiệu lực từ 31/01/2026; Điều 39 NĐ 102/2024 không áp dụng cho thu hồi đất thực hiện dự án; thẩm định 30 ngày chứ không phải 30 ngày làm việc; điểm c k1 Đ80 chỉ cho dự án thuộc thẩm quyền Quốc hội, Thủ tướng; thông báo ban hành lại không tính lại 60, 120 ngày); 11 quy định Sổ tay chưa nêu; bảng ngày ban hành, hiệu lực; văn bản còn thiếu.
- Reference 12 (mới): Bảng giá đất Lào Cai (giá đất nông nghiệp, Phụ lục IV giá đất KCN, CCN), bồi thường nhà, công trình, di chuyển máy móc, diện tích tối thiểu tách thửa.
- Sửa reference 01 đến 10 và SKILL.md theo kết quả đối chiếu; reference 10 thêm điểm 15 đến 18; SKILL.md thêm quy tắc hành văn 6, 7.
- `registry/trang-thai.csv`: ghi ngày ban hành, hiệu lực 12 văn bản đã đối chiếu.
- Còn thiếu: QĐ 40/2026/QĐ-UBND, quy định trình tự thủ tục của tỉnh, QĐ 18/2025/QĐ-UBND, QĐ 43/2026/QĐ-UBND (Lào Cai), NĐ 101/2024, NĐ 226/2025, Luật 43/2024.

## [1.0.0] - 02/10/2026 — Lập plugin từ Sổ tay bồi thường, hỗ trợ, tái định cư của Sở Nông nghiệp và Môi trường tỉnh Lào Cai
- SKILL.md: phạm vi (đọc báo cáo GPMB, viết đúng chủ thể, trả lời chủ đầu tư), mức độ tin cậy của nguồn, bảng mốc thời hạn rút gọn, 5 quy tắc hành văn.
- 10 reference: nguồn và văn bản viện dẫn; thẩm quyền cấp xã, Hội đồng bồi thường, chủ đầu tư; quy trình 12 bước; bảng mốc thời hạn; kiểm đếm bắt buộc và cưỡng chế; thưởng bàn giao sớm, khiếu nại, hồ sơ địa chính; 10 tình huống phát sinh; danh mục 39 biểu mẫu kèm bảng quy đổi số mẫu; áp dụng cho Sở Công Thương; 14 điểm chưa thống nhất trong Sổ tay.
- Checklist đọc báo cáo GPMB của xã, chủ đầu tư.
- `van-ban-goc/`: bản gốc PDF (chỉ trên GitHub) và bản trích chữ bằng máy.
- Chưa làm: đối chiếu bản gốc các luật, nghị định, quyết định Sổ tay viện dẫn.
