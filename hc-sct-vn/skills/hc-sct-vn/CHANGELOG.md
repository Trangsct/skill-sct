# CHANGELOG — hc-sct-vn

## 1.6.1 — 18/10/2026 — Căn cứ chức năng Sở: QĐ 3628/QĐ-UBND ngày 02/10/2026 thay QĐ 05/2025/QĐ-UBND (chuyển từ PR 112/115)

- Thay dẫn QĐ 05/2025/QĐ-UBND → **QĐ 3628/QĐ-UBND ngày 02/10/2026** (Quy định CNNV, quyền hạn, cơ cấu tổ chức Sở Công Thương — 06 phòng, có Phòng Quản lý khoáng sản; không có khu công nghiệp) trong mẫu văn bản, reference: `references/10-kiem-tra-chuyen-nganh.md`; `references/14-bo-mau-van-ban.md`. Dòng nói về văn bản đã ký trước 02/10/2026 giữ nguyên dẫn cũ, ghi "lịch sử". Nguồn: `sct-laocai-org-vn` ref 04; bản gốc + `.txt`: `sct-laocai-org-vn/skills/sct-laocai-org-vn/van-ban-goc/2026.10.02-QD-3628-QD-UBND.pdf`. Máy kiểm: rule `qd-05-2025-da-thay-bang-qd-3628` trong `scripts/check_facts.py`.
- `plugin.json` 1.6.0 → 1.6.1.

## 1.6.0 — 17/10/2026 — Sửa tim_van_ban.py không tìm được số hiệu có chữ Đ

- `scripts/tim_van_ban.py` (bản chép từ gốc kho, đồng bộ bằng `build_so_cai_van_ban_goc.py`): sửa lỗi biểu thức tìm — chữ "đ" bị thay hai lần thành `[đ[dđ]]` nên MỌI số hiệu có chữ Đ (NĐ-CP, QĐ-UBND, QĐ-TTg) không bao giờ khớp và script kết luận sai "chưa có trong kho" (phát hiện 17/10/2026 khi kiểm thử GATE 0). Sau khi sửa: "181/2024/NĐ-CP" khớp 3 mục danh mục.
- `plugin.json` → 1.6.0. Chi tiết: `CHANGELOG-v2026.10.17.md`.

## [1.5.0] - 12/10/2026 — Lớp cắt giảm, phân cấp NQ 19/2026/NQ-CP + TT 26/2026/TT-BCT (ref 18); Chiến lược QĐ 726/QĐ-TTg (ref 19); 13 biểu mẫu mới

- **ref 18 (mới):** thẩm quyền mới từ 29/5/2026 (GP XNK kiểm soát đặc biệt nhóm 1, GP nhập khẩu hóa chất cấm, GCN dịch vụ tồn trữ mọi cơ sở → UBND cấp tỉnh); điều kiện kinh doanh viết lại; hồ sơ GCN/GP **bỏ Thông báo nghiệm thu và Phiếu ATHC**; thời hạn 14/10/05/03 ngày; Hội đồng KH tách luồng; miễn trừ ≤ 1 %; bảng 13 mẫu TT 26; checklist mới. Sửa ref 01–06, 09, 13–16 theo.
- **ref 19 (mới):** Chiến lược phát triển ngành CN hóa chất đến 2030, tầm nhìn 2040 (QĐ 726/QĐ-TTg 16/6/2022 + CV 3698/BCT-HC 30/6/2022).
- `van-ban-goc/`: TT 26/2026 bản ký số (thân văn bản) + .txt; `07-chien-luoc/` QĐ 726 + .txt. NQ 19/2026 dùng bản ở `hnh-sct-vn` (không nhân bản).
- `mau-ho-so/TT-26-2026/`: 13 mẫu Phần III TT 26 tách từ bản Word; xóa mẫu cũ TT 01/TT 02.
- SKILL.md mục I–VI, description; `plugin.json` → 1.5.0.

Chi tiết: `CHANGELOG-v2026.10.12.md`.

## [1.3.3] - 09/10/2026 — Sổ cái văn bản gốc dùng chung, bản .txt toàn văn, tim_van_ban.py, quy tắc "không được nói không có"

- `SKILL.md`: thêm khối **Tra văn bản gốc** ngay dưới tiêu đề — đọc `van-ban-goc/00-DANH-MUC-CHUNG.md`, chạy `scripts/tim_van_ban.py` trước khi kết luận văn bản chưa có; văn bản đã có thì mở bản `.txt`; cấm trả lời "chưa có trong gói", "không mở được toàn văn", "tra mạng khi cần nguyên văn"; 7 bước (a)–(g) khi Bạn gửi văn bản quy phạm; không có quyền ghi thì hướng dẫn Hộp thư `_inbox/`.
- `van-ban-goc/00-DANH-MUC-CHUNG.md` (máy sinh bởi `scripts/build_so_cai_van_ban_goc.py` ở gốc kho, giống nhau ở mọi plugin): danh mục toàn bộ văn bản gốc của 24 plugin (số hiệu, ngày, tên, plugin chủ, đường dẫn, có .txt), danh sách trùng số hiệu nhiều plugin, tệp đặt tên chưa chuẩn.
- `scripts/tim_van_ban.py` (bản chép từ gốc kho): tìm theo số hiệu/cụm từ trong danh mục, toàn văn .txt/.md mọi plugin và reference; chạy được trong gói claude.ai.
- `van-ban-goc/`: mọi tệp gốc .pdf/.doc/.docx/.xlsx có bản trích chữ `.txt` cùng tên đặt cạnh (hiện 0 tệp .txt), sinh bằng `scripts/trich_chu_van_ban_goc.py` (NFC; bản quét OCR đánh dấu `[OCR]`, số/ngày phải đối chiếu bản gốc).
- `plugin.json` → 1.3.3.

Chi tiết: `CHANGELOG-v2026.10.09.md`.

## [1.3.0] - 08/9/2026 — Sở là thành viên Hội đồng thẩm định KH của Cục Hóa chất; Phiếu Mẫu 03c; vụ DAP số 2
- **ref 17 (mới)** `17-thanh-vien-hoi-dong-tham-dinh-kh-cuc-hoa-chat.md`: phân biệt vai trò Sở (cơ quan thẩm định với điểm b / thành viên Hội đồng của Cục với điểm a); cách điền Phiếu Mẫu 03c (không tự đánh X ô lựa chọn, ngày để trống, chức vụ chuyên môn); checklist 8 điểm thẩm định nội dung KH theo Phụ lục II TT 02/2026 (KH điều chỉnh phải khớp Bảng 1.2 → 2.1 → 2.2 → mục 4.3 + diễn tập; bộ ngưỡng AEGL 60 phút; axit không bay hơi phải tính lượng tràn); điều kiện an toàn trạm xuất NH3 lỏng và trạm xuất axit (110% dung tích xe bồn, 17 m, vật liệu, không phun nước vào H2SO4 đặc); quan hệ KH điều chỉnh với thủ tục đầu tư - xây dựng - PCCC - môi trường; bán H2SO4 ra ngoài → GP kinh doanh hóa chất kiểm soát đặc biệt nhóm 2 (tỉnh) + phiếu kiểm soát mua bán; dữ kiện vụ DAP số 2 đã xác minh.
- **vi-du-thuc-te/ke-hoach-su-co/**: `Mau-03c-goc.docx`; `2026.09.08. Phieu-nhan-xet-Mau-03c-KH-su-co-DAP-so-2.docx` (bản hoàn thiện cho CV Loan, 10 nhóm yêu cầu); `build_phieu_03c.py` + `line_runs.txt` (script dựng Phiếu 03c trên mẫu gốc: A4 lề 2-2-3-2, header 13pt 2 đường Line shape, thân 14pt lùi 1 cm, subscript công thức, m2/m3 số mũ, nén chữ tránh chữ lẻ); `VB-de-nghi-1648-DAP2-KTh-tham-dinh-KH.pdf`.
- SKILL.md (mục I, IV, V), ref 06 (mục 3, 12), ref 15 (mục lục), ref 16 (mục 5a) trỏ sang ref 17; description plugin/SKILL thêm từ khóa Mẫu 03c, trạm xuất NH3, DAP số 2.

## [1.2.3] - 02/9/2026 — nơi nộp TTHC duy nhất motcua-tthc.moit.gov.vn
- Nơi nộp hồ sơ TTHC: DUY NHẤT Cổng dịch vụ công một cửa Bộ Công Thương https://motcua-tthc.moit.gov.vn/ (đăng nhập VNeID) — Bạn chốt lại 02/9/2026. Bỏ mọi cách ghi "kênh phụ"/"hoặc qua" Trung tâm Phục vụ hành chính công, bưu chính, trực tiếp, "Cổng DVCQG", "Hệ thống TTGQ TTHC tỉnh" trong hướng dẫn DN; trích luật thì ghi rõ là trích luật.

## [1.2.2] - 02/9/2026 — sửa theo scripts/check_facts.py (CI dữ kiện lỗi thời)
- Sửa các vi phạm do script quét: nơi nộp hồ sơ → motcua-tthc.moit.gov.vn; tiêu ngữ en dash trong mẫu; trỏ xp-hc-vlncn-sct-vn → xp-sct-vn; CN(M.Cường) trong mẫu → CN(Khôi), trong ví dụ lịch sử chú thích "lịch sử"; ký hiệu /GP-SCT bỏ chữ "dự kiến". Không đổi nghiệp vụ.

Nhật ký thay đổi của plugin (Quản lý nhà nước về hóa chất). Lịch sử trước 02/9/2026 xem CHANGELOG.md ở gốc repo (tìm theo tên plugin) và `git log -- hc-sct-vn/`.

## [1.2.1] - 02/9/2026 — khởi tạo CHANGELOG trong thư mục skill
- Rà soát tổng thể 02/9/2026: plugin đúng cấu trúc, description trong ngưỡng, không phát hiện dữ kiện lỗi thời cần sửa. Phiên bản giữ nguyên 1.2.1.
- Từ nay mỗi lần nâng cấp ghi mục mới lên đầu file này (theo CLAUDE.md của repo).
