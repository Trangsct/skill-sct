## 1.8.0 — 28/10/2026 — Bản Giám đốc duyệt bài phát biểu BCH Đảng bộ tỉnh (sửa cuối trên Zalo); quy tắc R18–R20

- kho-bai-mau thêm `bpb-bch-dang-bo-tinh-2026-10-28-khu-cum-cong-nghiep-gd-duyet.docx` (bản Giám đốc chốt 20h29, 5 trang) — mẫu chuẩn mới; reference ghi từng chỗ Giám đốc sửa cuối (làm tròn số, chức danh thay tên riêng, trích chỉ đạo của Chủ tịch nguyên văn, tách gạch đầu dòng, cắt đề nghị vượt cấp); R18 an ninh trật tự viết mềm "(nếu có)", R19 bản Zalo dán toàn văn là bản duyệt, R20 nêu tên từng dự án khi dẫn quyết định nhiều dự án.
- `plugin.json` → 1.8.0. Chi tiết: `CHANGELOG-v2026.10.28-2.md`.

## 1.7.0 — 28/10/2026 — Mẫu bài phát biểu tại Hội nghị BCH Đảng bộ tỉnh về vướng mắc KCN, CCN trọng điểm (5 trang); quy tắc R8–R17

- kho-bai-mau thêm bản cuối 28/10/2026, bản Giám đốc sửa tay và bản đầu 27/10/2026; reference mới `bpb-bch-dang-bo-tinh-khu-cum-cong-nghiep-28-10-2026.md` (việc lớn đã làm trước, phân công giọng ngang cấp, phát động chiến dịch GPMB, mốc theo ngày đọc, độ dài tối đa, đối chiếu tên số lãnh đạo nhắn Zalo); SKILL.md mục 7, 8.
- `plugin.json` → 1.7.0. Chi tiết: `CHANGELOG-v2026.10.28.md`.

## 1.6.0 — 17/10/2026 — Dàn ý trước khi viết (GATE 0b)

- SKILL.md: mục dàn ý văn bản dài theo GATE 0b của vbhc-vn 2.31.0 (Bạn chốt 17/10/2026) — lập dàn ý theo dàn ý mặc định hoặc mẫu gần nhất trong kho, ghi `ke-hoach-soan.txt`, viết thân ngay, không gửi dàn ý xin duyệt trừ khi Bạn yêu cầu; giao file báo một dòng "Dàn ý theo mẫu …". Mục 2A: dàn ý mặc định bài phát biểu (mở đầu, bối cảnh, kết quả, hạn chế, nhiệm vụ, kết thúc) dẫn mục 3.
- `plugin.json` → 1.6.0. Chi tiết: `CHANGELOG-v2026.10.17.md`.

## 1.5.1 — 09/10/2026 — Sổ cái văn bản gốc dùng chung, bản .txt toàn văn, tim_van_ban.py, quy tắc "không được nói không có"

- `SKILL.md`: thêm khối **Tra văn bản gốc** ngay dưới tiêu đề — đọc `van-ban-goc/00-DANH-MUC-CHUNG.md`, chạy `scripts/tim_van_ban.py` trước khi kết luận văn bản chưa có; văn bản đã có thì mở bản `.txt`; cấm trả lời "chưa có trong gói", "không mở được toàn văn", "tra mạng khi cần nguyên văn"; 7 bước (a)–(g) khi Bạn gửi văn bản quy phạm; không có quyền ghi thì hướng dẫn Hộp thư `_inbox/`.
- `van-ban-goc/00-DANH-MUC-CHUNG.md` (máy sinh bởi `scripts/build_so_cai_van_ban_goc.py` ở gốc kho, giống nhau ở mọi plugin): danh mục toàn bộ văn bản gốc của 24 plugin (số hiệu, ngày, tên, plugin chủ, đường dẫn, có .txt), danh sách trùng số hiệu nhiều plugin, tệp đặt tên chưa chuẩn.
- `scripts/tim_van_ban.py` (bản chép từ gốc kho): tìm theo số hiệu/cụm từ trong danh mục, toàn văn .txt/.md mọi plugin và reference; chạy được trong gói claude.ai.
- `van-ban-goc/`: mọi tệp gốc .pdf/.doc/.docx/.xlsx có bản trích chữ `.txt` cùng tên đặt cạnh (hiện 0 tệp .txt), sinh bằng `scripts/trich_chu_van_ban_goc.py` (NFC; bản quét OCR đánh dấu `[OCR]`, số/ngày phải đối chiếu bản gốc).
- `plugin.json` → 1.5.1.

Chi tiết: `CHANGELOG-v2026.10.09.md`.

## 1.5.0 — 06/10/2026 — Mẫu bài phát biểu tóm tắt tại cuộc họp UBND tỉnh về CCN; thẻ [BREAK] thụt dòng đầu

- kho-bai-mau thêm `bpb-hop-ccn-ubnd-tinh-2026-10-06-tom-tat.docx` (bản cuối Giám đốc đọc tại cuộc họp 06/10/2026 theo Giấy mời 565/GM-UBND; 03 trang, 04 phần bám Báo cáo của Sở); mục lục + SKILL.md mục 7 bổ sung dạng "phát biểu tóm tắt đi kèm Báo cáo đầy đủ".
- `scripts/build_bpb.py`: thẻ `[BREAK]` ("Kính thưa Hội nghị!") thêm `first_line_indent` 1.27 cm cho khớp thân bài (trước đó sát lề trái); SKILL.md mục 6 ghi rõ.
- Số liệu CCN trong bài phải chép đúng Báo cáo cùng kỳ — plugin kccn-sct-vn ref 44.

## 1.4.0 — 06/9/2026 — Mẫu bài phát biểu Trưởng phòng tại giao ban Sở

- kho-bai-mau thêm `bpb-giao-ban-thang-9-2026-truong-phong-qlcn.docx` (bản Bạn sửa tay, lồng ghép 9 tháng + tháng 9 theo từng lĩnh vực) và `bpb-tong-hop-9-thang-2026-truong-phong-qlcn.docx`; mục lục + SKILL.md mục 7 bổ sung dạng Trưởng phòng báo cáo giao ban.

# CHANGELOG — bpb-sct-vn

Nhật ký thay đổi của plugin (Bài phát biểu, tham luận, diễn văn cho lãnh đạo Sở). Lịch sử trước 02/9/2026 xem CHANGELOG.md ở gốc repo (tìm theo tên plugin) và `git log -- bpb-sct-vn/`.

## [1.3.2] - 02/9/2026 — khởi tạo CHANGELOG trong thư mục skill
- Rà soát tổng thể 02/9/2026: plugin đúng cấu trúc, description trong ngưỡng, không phát hiện dữ kiện lỗi thời cần sửa. Phiên bản giữ nguyên 1.3.2.
- Từ nay mỗi lần nâng cấp ghi mục mới lên đầu file này (theo CLAUDE.md của repo).
