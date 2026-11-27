---
name: sct-laocai-org-vn
description: "CƠ CẤU TỔ CHỨC, PHÂN CÔNG Sở Công Thương Lào Cai. Kích hoạt: ai ký, trình ai, PGĐ nào phụ trách, chuyên viên tham mưu, dòng Lưu VT CN, phòng nào chủ trì, phân công BGĐ; Hoàng Chí Hiền, Hoàng Văn Thuân, Nguyễn Đình Chiến, Phạm Năng Chung, Nguyễn Hữu Long, Trần Trọng Trang. Nội dung: QĐ 3628/QĐ-UBND 02/10/2026 (thay QĐ 05/2025): Sở có 06 phòng (thêm Phòng Quản lý khoáng sản) + Chi cục QLTT, KCN không thuộc Sở; TT 50/2026/TT-BCT, NĐ 351/2026 (ref 04); BGĐ GĐ + 6 PGĐ theo QĐ 7750/QĐ-SCT 17/11/2026 (thay QĐ 6320) - PGĐ Thuân ký hóa chất, VLNCN, xây dựng; PGĐ Chung phụ trách Phòng QLKS; CNNV Văn phòng + 5 phòng theo QĐ 6226/QĐ-SCT 02/10/2026 (thay QĐ 59, ref 01); Quy chế làm việc QĐ 6286/QĐ-SCT 05/10/2026; nội bộ Phòng QLCN 10/7/2026 (1 TP + 3 PTP + 10 CV, ai kiểm duyệt); soạn công văn phân công, QĐ cử công chức. Phòng QLKS từ 10/2026: TP Lưu Đức Cường, PTP Nguyễn Hồng Vân, ký hiệu SCT-KS (ref 03). Từ khóa: Đỗ Mạnh Cường, QLCN, QLTM, QLNL, KH-TH, QLKS, NQ 66.25/2026 (tiếp nhận địa chất, khoáng sản từ 15/9/2026)."
---

# sct-laocai-org-vn — Cơ cấu tổ chức Sở Công Thương tỉnh Lào Cai

> **Tra văn bản gốc (Bạn chốt 09/10/2026, áp dụng mọi plugin):** đọc `van-ban-goc/00-DANH-MUC-CHUNG.md` và chạy `python3 scripts/tim_van_ban.py "<số hiệu hoặc cụm từ>"` TRƯỚC khi kết luận văn bản nào chưa có trong kho. Văn bản đã có trong danh mục thì phải mở toàn văn `.txt` cùng tên đặt cạnh bản gốc để trích; cấm trả lời "không có tài liệu", "chưa có trong gói", "không mở được toàn văn", "tra mạng khi cần nguyên văn". Khi Bạn gửi văn bản quy phạm pháp luật trong phiên: (a) đọc số, ngày, cơ quan, người ký bằng script (GATE), không đọc bằng mắt; (b) đặt tên `YYYY.MM.DD-SỐ.KÝ.HIỆU-Tên-trích-yếu-ngắn`, giữ nguyên định dạng gốc; (c) lưu vào `van-ban-goc/` của plugin chủ theo lĩnh vực, không nhân bản sang plugin khác; (d) sinh `.txt` bằng `scripts/trich_chu_van_ban_goc.py`; (e) chạy `scripts/build_so_cai_van_ban_goc.py` ở gốc kho để cập nhật danh mục; (f) cập nhật reference tóm tắt + CHANGELOG; (g) push, mở PR. Phiên không có quyền ghi kho thì nói ngay ở câu đầu và hướng dẫn Bạn dùng Hộp thư nạp kho `_inbox/` trên GitHub (`_inbox/README.md`, 6 bước), không được chỉ tóm tắt rồi bỏ qua tệp.

> **Lấy toàn văn văn bản quy phạm pháp luật từ thuvienphapluat.vn — TỰ ĐỘNG, không chờ Bạn nhắc (Bạn chốt 27/11/2026; quy trình đã chạy được 26/11/2026; áp dụng mọi plugin):** cần toàn văn một luật, nghị định, thông tư, quyết định… mà MCP `sct-tra-cuu` (`tra_phap_luat`, `tra_van_ban`, `tra_reference`) và `scripts/tim_van_ban.py` đều không có (thường là văn bản ngoài lĩnh vực công thương, vd Nghị định 335/2025/NĐ-CP về đánh giá công chức) thì tự lấy qua trình duyệt trên máy Bạn, không hỏi lại: (1) WebSearch chỉ dùng để tìm đường dẫn trang văn bản trên thuvienphapluat.vn (bản tóm tắt của báo không thay được toàn văn); WebFetch bị chặn ở thuvienphapluat.vn, luatnguyen, congbao.chinhphu.vn — không thử lại, không vòng qua bằng curl; (2) nạp công cụ Claude in Chrome trong MỘT lần ToolSearch (`list_connected_browsers`, `select_browser`, `tabs_context_mcp`, `tabs_create_mcp`, `navigate`, `get_page_text`, `javascript_tool`, `computer`, `tabs_close_mcp`); máy có 2 Chrome kết nối thì `select_browser` trước, Bạn không chỉ định thì chọn Browser 1; Chrome không kết nối thì làm y các bước bằng trình duyệt tích hợp của ứng dụng Claude; (3) mở tab mới (`tabs_context_mcp` createIfEmpty) → `navigate` tới trang văn bản → `get_page_text`; (4) `get_page_text` cắt ở 50.000 ký tự nên thường mất Phụ lục, mẫu biểu ở cuối — đây là giới hạn công cụ, KHÔNG phải trang chặn, không vội kết luận phải đăng nhập; lấy phần còn thiếu bằng `javascript_tool`: đọc `document.body.innerText`, cắt từ mốc (vd `lastIndexOf('PHỤ LỤC II')`), chuẩn hóa bớt xuống dòng và chuỗi dấu chấm, gán vào biến `window.__vb` rồi trả từng khúc khoảng 1.000–1.600 ký tự, ghép đủ đến hết văn bản; (5) trang đòi đăng nhập: tài khoản cơ quan đã lưu sẵn trong Chrome, chỉ bấm nút Đăng nhập, KHÔNG BAO GIỜ gõ mật khẩu; tài khoản dùng chung tối đa 5 người — hiện cảnh báo "có 1 người khác bị Đăng xuất" thì bấm Đồng ý luôn, không hỏi Bạn (quy tắc cơ quan: nhiều người đăng nhập thì ưu tiên người đăng nhập sau, người đang làm; người đăng nhập trước thường lấy văn bản xong để treo — Bạn chốt 27/11/2026); (6) lấy xong đóng tab (`tabs_close_mcp`); (7) đối chiếu số, ngày, cơ quan ban hành, trích yếu trên trang với văn bản cần tìm (số trùng khác năm là văn bản khác: 303/2025 ≠ 303/2026); (8) lưu vào kho để lần sau không phải lấy lại: tệp `.txt` toàn văn đặt tên `YYYY.MM.DD-SỐ.KÝ.HIỆU-Tên-trích-yếu-ngắn.txt`, dòng đầu ghi "Nguồn: thuvienphapluat.vn, lấy ngày dd/mm/yyyy", vào `van-ban-goc/` của plugin chủ theo lĩnh vực (ngoài mọi lĩnh vực → `vbhc-vn`), chạy `scripts/build_so_cai_van_ban_goc.py`, push, mở PR và merge; phiên không có quyền ghi kho thì vẫn giao tệp và hướng dẫn Bạn nạp qua Hộp thư `_inbox/`; (8b) VĂN BẢN DÀI (Bạn chốt 27/11/2026, đã chạy được): `javascript_tool` chỉ trả khoảng 1.100 ký tự mỗi lần, `get_page_text` 50.000 ký tự, máy ảo đám mây bị thuvienphapluat, luatvietnam chặn, nút "Tải về" không ra tệp đọc được — nên chuyển qua Google Docs: (i) trong trang thuvienphapluat dùng `javascript_tool` `fetch` (credentials include) các trang văn bản cần lấy, lấy chữ phần tử `.content1` (đổi `br`, `p`, `tr` thành xuống dòng), nối nhiều văn bản vào một chuỗi có dòng phân cách `=====VANBAN <số hiệu> =====`, đặt vào một `textarea`, chọn hết rồi `computer` phím ctrl+c; (ii) tạo Google Docs bằng `mcp__Google_Drive__create_file` (mimeType document) trong thư mục Drive "Văn bản QPPL tải từ thuvienphapluat" (id 1fgC7yr2I49TH7Te6Mu8KL--V-p7R8fwJ), mở tài liệu trong Chrome, bấm vào thân rồi ctrl+shift+v; (iii) chờ khoảng 10 giây, `mcp__Google_Drive__download_file_content` exportMimeType text/plain — tệp tự lưu vào máy ảo, tách theo dòng phân cách; tài liệu giữ lại trong thư mục Drive cho Bạn; (9) Bạn cần file thì dựng Word: Times New Roman 13, lề trên, dưới 2 cm, trái 3 cm, phải 2 cm; Chương, Mục, tiêu đề in đậm căn giữa; "Điều n." in đậm; soi bản PDF kiểm tra trang trắng rồi mới giao. Chỉ khi cả Chrome lẫn trình duyệt tích hợp không kết nối được, hoặc trang không có văn bản, mới báo Bạn tải bổ sung.

## Bảng phân công ký dạng máy đọc — `data/phan-cong-ky.json` (từ 05/11/2026)

Trích từ các mục "Phân công nhiệm vụ trong Lãnh đạo Sở", "Bảng routing trình Lãnh đạo Sở", "Khối người ký" dưới đây thành JSON
(giai đoạn hiệu lực, lĩnh vực → phòng, chuyên viên, kiểm duyệt, người ký, khối ký, ký hiệu, dòng Lưu, người ký thay khi vắng).
Máy chủ tra cứu (plugin `tra-cuu-sct-vn`, công cụ `nguoi_ky_va_luong_trinh`) đọc tệp này. **Khi có quyết định phân công mới
hoặc sửa bảng ký trong SKILL.md thì sửa JSON cùng đợt**; không ghi số điện thoại, thông tin riêng vào tệp.

## Lãnh đạo tỉnh, lãnh đạo các Sở ngành, địa giới hành chính — `references/02-lanh-dao-tinh-so-nganh-dia-gioi.md`

Tra ở đây (không suy đoán) khi cần: tên Bí thư/Chủ tịch/các Phó Chủ tịch UBND tỉnh (nhiệm kỳ 2026-2031); Giám đốc các Sở ngành (5/2026); diện tích, dân số, 99 xã/phường của tỉnh Lào Cai mới (NQ 202/2025/QH15, từ 01/7/2025); quy tắc ghi địa danh Yên Bái cũ thành "tỉnh Lào Cai", 8 xã không sắp xếp; tỉnh, thành phố khác đã đổi cấp (mục 2a: Bắc Ninh thành phố trực thuộc Trung ương từ 20/9/2026, Quảng Ninh từ 01/9/2026 — ghi "Ủy ban nhân dân thành phố Bắc Ninh" trong văn bản gửi đi); địa chỉ, điện thoại Sở Công Thương (Số 165 Lý Thường Kiệt, phường Yên Bái; 02163.857.863 — không điền email). Chuyển từ bộ ghi nhớ cá nhân sang skill ngày 08/9/2026.

## Kỳ cập nhật 10/10/2026 — `references/03-ky-cap-nhat-10-10-2026-nhan-su-phong-khoang-san-so-van-ban.md`

Văn bản tổ chức, nhân sự tuần 29/9–09/10/2026 theo sổ văn bản Data360X (Đề án 6152/ĐA-SCT → QĐ 3620 và QĐ 3628/QĐ-UBND 02/10/2026; QĐ 3589/QĐ-UBND điều động PGĐ Phạm Năng Chung; QĐ 6231 bổ nhiệm PTP Phòng QLKS Nguyễn Hồng Vân; 10 QĐ điều động công chức 02/10; QĐ 6478 tiếp nhận Phùng Đức Minh; 6426/SCT-KH điều chỉnh phân công Đề án 08 — hạn 14/10); Phòng Quản lý Khoáng sản đã vận hành (ký hiệu `/SCT-KS`, TP Lưu Đức Cường); Trưởng phòng các phòng khác thấy trên luồng xử lý; số QĐ phân công BGĐ thời điểm đó là 6320/QĐ-SCT (6286 là Quy chế làm việc; nay đã thay bằng QĐ 7750/QĐ-SCT ngày 17/11/2026); việc còn phải làm khi bot mang bản gốc về.

## Khung tổ chức mới 9–10/2026 — `references/04-qd-3628-chuc-nang-co-cau-so-2026.md`

Tóm lược theo từng điều, đọc từ bản gốc trong `van-ban-goc/`: **NĐ 351/2026/NĐ-CP** 11/9/2026 (Bộ Công Thương — Điều 1; khoản 11–13 Điều 2: địa chất - khoáng sản, KCN - CCN, hóa chất - VLNCN); **TT 50/2026/TT-BCT** 13/9/2026 sửa TT 37/2025 (bảng đối chiếu khoản ↔ điều; điểm y khoản 2 Điều 4 "địa chất và khoáng sản"; Điều 3 chuyển tiếp ATTP); **QĐ 3628/QĐ-UBND** 02/10/2026 (Điều 1 chức năng — không có KCN; Điều 2 nhiệm vụ, khoản 12; Điều 3 cơ cấu 06 phòng + Chi cục QLTT; Điều 8); **QĐ 3589/QĐ-UBND** 30/9/2026 bổ nhiệm PGĐ Phạm Năng Chung; mục lịch sử về 03 dự thảo 04/10/2026 đã ban hành.

## Vị trí việc làm, phương án biên chế 2027–2031 (11/2026) — `references/05-ky-cap-nhat-17-11-2026-vi-tri-viec-lam-bien-che-2027-2031.md`

KL 107-KL/TW 17/10/2026, HD 07-HD/BTCTW 19/10/2026; Sở Nội vụ: QĐ 733/QĐ-SNV 30/10/2026 (Tổ thẩm định), CV 4581/SNV-TCBC 06/11 (hồ sơ), **CV 4673/SNV-TCBC 12/11/2026 (quy trình 5 bước)**, **CV 4714/SNV-TCBC 13/11/2026 (cơ quan có đơn vị trực thuộc)**; khóa Cổng kê khai từ 00h 11/11/2026; 09 biểu A1–D2; tài liệu kiểm chứng (số văn bản đi, đến, TTHC, hồ sơ quản lý); mốc biên chế hiện có 30/9/2026.

Mã vị trí việc làm (SCT.LĐQL.01–12, SCT.CMNV…), quỹ giờ 1.904, mức thời gian dùng chung, cách chạy bộ 09 biểu: mục 8 của reference 05. Lãnh đạo Chi cục Quản lý thị trường và phân công theo QĐ 149/QĐ-QLTT ngày 08/9/2025 (Chi cục trưởng Đỗ Du Bắc; các Phó Chi cục trưởng Trần Văn Chiến, Bùi Hồng Hưng, Nguyễn Quang Hiểu): mục D của reference 04.

## Kỳ cập nhật 24/11/2026 — `references/06-ky-cap-nhat-24-11-2026-tam-dung-tuyen-dung-sap-xep-bo-may-tiep-cong-dan.md`

**Tạm dừng tuyển dụng mới, điều chuyển công chức** đến khi xong phương án biên chế 2027–2031 (CV 191/BCĐCP 17/11, CV 13451/BNV-CCVC 20/11, **CV 12027/UBND-NC 22/11/2026**; khung CV 8578/UBND-NC 22/8/2026: điều động giữa các sở chỉ khi Chủ tịch UBND tỉnh chấp thuận). Sắp xếp bộ máy KL 433-KL/TU 05/11/2026; chuyển giao ATTP về Chi cục ATTP thuộc Sở Y tế (KL 114-KL/TW; KH 394/KH-SYT — sẽ sửa QĐ 3628, QĐ 6226). Tiếp công dân, đơn thư: **Văn phòng Sở chủ trì theo dõi hạn, tổng hợp số liệu** (CV 11857/UBND-TCD 18/11, CV 7864/SCT-VP 20/11/2026). Chỉ tiêu 2027 Tỉnh ủy giao Giám đốc Sở (NQ 116-NQ/TU): IIP 12%, 30 CCN, bán lẻ 110.000 tỷ đồng, XNK qua địa bàn 7.100 triệu USD, hộ dùng điện an toàn 96,89%.

## Phân công Ban Giám đốc mới từ 17/11/2026 — `references/07-qd-7750-phan-cong-ban-giam-doc-17-11-2026.md`

**QĐ 7750/QĐ-SCT ngày 17/11/2026** thay QĐ 6320/QĐ-SCT ngày 06/10/2026. Ba thay đổi làm đổi người ký: (1) **hóa chất, vật liệu nổ công nghiệp** chuyển từ PGĐ Chiến sang **PGĐ Hoàng Văn Thuân**; (2) **xây dựng chuyên ngành Công Thương** (thẩm định thiết kế, kiểm tra nghiệm thu công trình công nghiệp, trừ dự án năng lượng) ghi đích danh cho **PGĐ Thuân**; (3) **Phòng Quản lý Khoáng sản** chuyển từ PGĐ Thuân sang **PGĐ Phạm Năng Chung** phụ trách. PGĐ Chiến vẫn phụ trách Phòng QLCN (cụm công nghiệp, an toàn thực phẩm, khuyến công, cơ khí, PCTT). **Bạn chốt 25/11/2026: vận chuyển hàng hóa nguy hiểm, PCCC cũng chuyển sang PGĐ Thuân.** Reference 07: tóm tắt từng khoản, bảng đối chiếu QĐ 6320 ↔ QĐ 7750, các lĩnh vực QĐ không ghi đích danh (KCN, dầu khí, than; HHNH, PCCC Bạn đã chốt), xã, phường theo dõi (99/99), văn bản đã ký kiểm chứng.

## Căn cứ pháp lý gốc

- **NĐ số 351/2026/NĐ-CP ngày 11/9/2026** của Chính phủ quy định CNNV, quyền hạn và cơ cấu tổ chức của **Bộ Công Thương** (Phó Thủ tướng Phạm Gia Túc ký; thay **NĐ 40/2025/NĐ-CP — lịch sử**). Điều 1 bổ sung lĩnh vực **than, địa chất, khoáng sản, dầu khí, khu công nghiệp** vào Bộ; khoản 11 Điều 2 nhiệm vụ địa chất và khoáng sản; khoản 12 khuyến công, khu công nghiệp, cụm công nghiệp. Dùng để đối chiếu một lĩnh vực thuộc nhóm nào ở cấp Bộ. Bản gốc: `van-ban-goc/2026.09.11-ND-351-2026-ND-CP.pdf` (+ `.txt`).
- **TT số 37/2025/TT-BCT ngày 14/6/2025** hướng dẫn CNNV cơ quan chuyên môn về công thương cấp tỉnh, cấp xã, **được sửa đổi, bổ sung bởi TT số 50/2026/TT-BCT ngày 13/9/2026 (hiệu lực 15/9/2026)**: Sở Công Thương thêm lĩnh vực **điện, than, địa chất, khoáng sản, dầu khí**; điểm c khoản 2 Điều 4 "Về công nghiệp nặng, công nghiệp nhẹ"; điểm y khoản 2 Điều 4 "Về địa chất và khoáng sản"; Phòng Kinh tế cấp xã thêm khoản 20 Điều 6. **Không giao Sở Công Thương quản lý khu công nghiệp.** Điều 3 chuyển tiếp: Sở tiếp tục tham mưu QLNN về an toàn thực phẩm đến khi có quy định khác. Bản gốc: `van-ban-goc/2026.09.13-TT-50-2026-TT-BCT.pdf` (bản quét) + `.txt` (OCR).
- **QĐ số 3628/QĐ-UBND ngày 02/10/2026** của UBND tỉnh Lào Cai (Chủ tịch Nguyễn Tuấn Anh ký; hiệu lực từ ngày ký) ban hành Quy định CNNV, quyền hạn và cơ cấu tổ chức của SCT tỉnh Lào Cai — **căn cứ chuẩn trong mọi văn bản của Sở từ 02/10/2026**, dùng thay **QĐ số 05/2025/QĐ-UBND ngày 01/7/2025 (Chủ tịch Trần Huy Tuấn ký; thay QĐ 13/2025/QĐ-UBND Yên Bái cũ và QĐ 23/2025/QĐ-UBND Lào Cai cũ) — lịch sử**. QĐ 3628 không có điều khoản bãi bỏ QĐ 05/2025 (ref 04); văn bản ký trước 02/10/2026 dẫn QĐ 05/2025 là đúng lịch sử, không sửa lại. Căn cứ của QĐ 3628: QĐ 3620/QĐ-UBND ngày 02/10/2026 (phê duyệt Đề án sắp xếp), TTr 6205/TTr-SCT ngày 02/10/2026. Tóm tắt từng điều: `references/04`. Bản gốc: `van-ban-goc/2026.10.02-QD-3628-QD-UBND.pdf` (3,9 MB — chỉ có trên GitHub) + `.txt` (OCR, luôn có trong gói claude.ai).
- **QĐ số 6226/QĐ-SCT ngày 02/10/2026** của Giám đốc Sở (Hoàng Chí Hiền ký; hiệu lực từ ngày ký) ban hành Quy định chức năng, nhiệm vụ, quyền hạn của Văn phòng và các phòng chuyên môn — Văn phòng (Điều 3), KH-TH (Điều 4), QLCN (Điều 5), **Quản lý khoáng sản (Điều 6)**, QLNL (Điều 7), QLTM (Điều 8); **thay QĐ 59/QĐ-SCT ngày 01/7/2025 (lịch sử)**. Nội dung từng điều, khoản, mục: `references/01-chuc-nang-nhiem-vu-cac-phong-qd6226.md`. Văn bản nội bộ — không lưu bản gốc vào kho công khai.
- **QĐ số 6286/QĐ-SCT ngày 05/10/2026** của Giám đốc Sở ban hành Quy chế làm việc của Sở (số, ngày đọc từ phần căn cứ của QĐ 7750/QĐ-SCT và QĐ 6320/QĐ-SCT; chưa có bản gốc Quy chế). Quy chế trước đó: QĐ 04/QĐ-SCT ngày 01/7/2025 — lịch sử.
- **Phân công nhiệm vụ Ban Giám đốc Sở** — hiện hành: **QĐ 7750/QĐ-SCT ngày 17/11/2026** của Giám đốc Sở (Hoàng Chí Hiền ký; hiệu lực từ ngày ký; số, ngày, người ký đọc bằng script từ bản PDF ký số Bạn gửi 25/11/2026), thay **QĐ 6320/QĐ-SCT ngày 06/10/2026** (áp dụng 05/10–16/11/2026 — lịch sử; trước nữa là QĐ 766/QĐ-SCT ngày 12/02/2026 và QĐ 3488/QĐ-SCT ngày 31/12/2025). Nội dung phân công được Lãnh đạo Sở thống nhất tại cuộc họp ngày 16/11/2026. Văn bản nội bộ — không lưu bản gốc vào kho công khai; tóm tắt từng khoản và bảng đối chiếu với QĐ 6320: `references/07-qd-7750-phan-cong-ban-giam-doc-17-11-2026.md`.
- **QĐ số 3589/QĐ-UBND ngày 30/9/2026** của Chủ tịch UBND tỉnh (Nguyễn Tuấn Anh ký): điều động ông **Phạm Năng Chung**, Phó Giám đốc Sở Nông nghiệp và Môi trường, đến nhận công tác tại Sở Công Thương và **bổ nhiệm Phó Giám đốc Sở Công Thương, thời hạn 05 năm kể từ 01/10/2026** (văn bản nhân sự — không lưu bản gốc vào kho công khai; dữ kiện ở ref 04 mục A.4).
- **Thông báo phân công nhiệm vụ cho cán bộ, công chức Phòng QLCN ngày 10/7/2026** của Trưởng phòng Nguyễn Hữu Long (thông báo nội bộ, **không có số văn bản** — khi trích dẫn ghi "Thông báo ngày 10/7/2026 của Trưởng phòng QLCN", không bịa số), hiệu lực từ 10/7/2026, thay bản phân công cũ — nguồn của mục "Cơ cấu nội bộ Phòng QLCN" dưới đây.

## Cơ cấu tổ chức (theo QĐ 3628/QĐ-UBND ngày 02/10/2026, Điều 3)

**Lãnh đạo Sở** (khoản 1): Giám đốc + các Phó Giám đốc, số lượng PGĐ theo quy định của cấp có thẩm quyền; PGĐ không kiêm người đứng đầu đơn vị trực thuộc. Từ 01/10/2026: **01 GĐ + 06 PGĐ**.

**06 phòng chuyên môn, nghiệp vụ** (khoản 2 Điều 3 — thứ tự a–e như bản gốc; trước 02/10/2026 là 05 phòng theo QĐ 05/2025/QĐ-UBND, lịch sử):
1. Văn phòng Sở
2. Phòng Kế hoạch - Tổng hợp (KH-TH)
3. Phòng Quản lý công nghiệp (QLCN)
4. **Phòng Quản lý khoáng sản (QLKS) — phòng mới**, tiếp nhận mảng địa chất, khoáng sản (từ Sở NN&MT), khoáng sản làm VLXD (từ Sở Xây dựng) và mảng công nghiệp khai thác mỏ, chế biến khoáng sản tách từ Phòng QLCN
5. Phòng Quản lý năng lượng (QLNL)
6. Phòng Quản lý thương mại (QLTM)

**Phòng Quản lý Khoáng sản** vận hành từ 10/2026 (từ 17/11/2026 **PGĐ Phạm Năng Chung** phụ trách Phòng theo QĐ 7750/QĐ-SCT; 05/10–16/11/2026 PGĐ Thuân phụ trách theo QĐ 6320/QĐ-SCT — lịch sử; Đề án sắp xếp được phê duyệt tại **QĐ 3620/QĐ-UBND ngày 02/10/2026** — số/ngày đọc từ phần căn cứ của QĐ 3628, chưa có bản gốc Đề án). **Phòng đã vận hành từ đầu tháng 10/2026: Trưởng phòng Lưu Đức Cường; Phó Trưởng phòng Nguyễn Hồng Vân (điều động, bổ nhiệm tại QĐ 6231/QĐ-SCT ngày 02/10/2026); ký hiệu văn bản `/SCT-KS`; dòng `Lưu: VT, KS.`** — chi tiết và chuỗi 10 QĐ điều động công chức ngày 02/10/2026: reference `03`.

**01 tổ chức hành chính trực thuộc**: Chi cục Quản lý thị trường tỉnh (QLTT). Đây là tổ chức hành chính độc lập, KHÔNG phải phòng chuyên môn của Sở.

Bố trí Phó Trưởng phòng theo biên chế: <10 biên chế → 1 PTP; 10-14 → tối đa 2 PTP; ≥15 → tối đa 3 PTP.

## Phân công nhiệm vụ trong Lãnh đạo Sở (Ban Giám đốc) — QĐ 7750/QĐ-SCT ngày 17/11/2026

> Nguồn: **Quyết định số 7750/QĐ-SCT ngày 17/11/2026** của Giám đốc Sở (Hoàng Chí Hiền ký; số, ngày, người ký đọc bằng `extract_metadata.py` từ bản PDF ký số Bạn gửi 25/11/2026) về việc phân công nhiệm vụ đối với Giám đốc, Phó Giám đốc - Sở Công Thương tỉnh Lào Cai; **hiệu lực từ ngày ký, thay thế QĐ 6320/QĐ-SCT ngày 06/10/2026** (Điều 3). Căn cứ: NĐ 30/2020/NĐ-CP; QĐ 3628/QĐ-UBND ngày 02/10/2026; QĐ 6286/QĐ-SCT ngày 05/10/2026 ban hành Quy chế làm việc; ý kiến thống nhất của Lãnh đạo Sở tại cuộc họp ngày 16/11/2026; đề nghị của Chánh Văn phòng Sở. Nơi nhận: Thường trực Tỉnh ủy, UBND tỉnh; các sở, ngành; UBND các xã, phường. Kết cấu: Điều 1 nguyên tắc chung (7 khoản), Điều 2 phân công (7 khoản, GĐ và PGĐ1–PGĐ6), Điều 3 hiệu lực thi hành.
> Cơ cấu BGĐ không đổi: **01 Giám đốc + 06 Phó Giám đốc**. Bản trước (QĐ 6320, áp dụng 05/10–16/11/2026): PGĐ Chiến phụ trách hóa chất, VLNCN; PGĐ Thuân phụ trách Phòng Quản lý Khoáng sản — đã hết hiệu lực, chỉ dùng để đọc văn bản cũ (lịch sử). Chi tiết từng khoản và bảng đối chiếu: `references/07-qd-7750-phan-cong-ban-giam-doc-17-11-2026.md`.

### Nguyên tắc chung (Điều 1)
- Tập trung dân chủ, thảo luận tập thể, cá nhân phụ trách, chế độ thủ trưởng. GĐ chịu trách nhiệm trước Tỉnh ủy, UBND tỉnh, Chủ tịch UBND tỉnh, Bộ Công Thương.
- PGĐ giúp GĐ phụ trách, chỉ đạo một số lĩnh vực + một/một số phòng; được ủy quyền giải quyết việc thuộc lĩnh vực; chịu trách nhiệm trước GĐ và pháp luật; được ủy nhiệm điều hành khi GĐ vắng.
- Việc vượt phạm vi / mới phát sinh chưa có chủ trương cấp trên → PGĐ xin ý kiến GĐ hoặc đưa ra tập thể Lãnh đạo Sở.
- Một PGĐ vắng (nghỉ phép, đi nước ngoài) → PGĐ được phân công xử lý thay việc hằng ngày; cả hai cùng vắng → GĐ trực tiếp hoặc phân công PGĐ khác.
- Ngoài Điều 2, PGĐ làm việc khác theo phân công, ủy quyền của GĐ (khoản 7 Điều 1 — ở QĐ 6320 là Điều 3 riêng, lịch sử).

### Phân công cụ thể (Điều 2)

**① Giám đốc — Hoàng Chí Hiền (GĐ).** Lãnh đạo, quản lý toàn diện. Trực tiếp phụ trách (không đổi so với bản trước):
- Quy hoạch, kế hoạch, chương trình, đề án, dự án trọng tâm của ngành.
- Tổ chức bộ máy, quản lý cán bộ - công chức - người lao động.
- Tài chính, tài sản, **chủ tài khoản** của Sở.
- Đối ngoại, hội nhập KTQT, hợp tác quốc tế.
- KHCN-ĐMST-CĐS của cơ quan; dân chủ cơ sở; PCTN, tiêu cực, lãng phí; phối hợp với cơ quan, đoàn thể theo quy chế phối hợp.
- Chỉ đạo chung KNTC, tiếp công dân; **người phát ngôn**; thành viên UBND tỉnh; nhiệm vụ BCĐ, Tổ công tác của Tỉnh ủy, UBND tỉnh, Bộ Công Thương mà GĐ là thành viên; Chủ tịch HĐ TĐKT-KL của Sở.
- **Phụ trách trực tiếp: Văn phòng Sở, Phòng KH-TH, Chi cục QLTT.**

**② PGĐ1 — Trịnh Văn Thành.** Trực tiếp phụ trách (không đổi):
- Hành chính, quản trị; CCHC; thi đua khen thưởng; chế độ - chính sách cán bộ.
- **Được ủy quyền phụ trách Sở khi GĐ vắng mặt**; chủ tài khoản theo ủy quyền (phó chủ tài khoản chi thường xuyên Văn phòng Sở; ký hợp đồng dịch vụ, phê duyệt hồ sơ chi thường xuyên; việc đột xuất báo GĐ trước).
- Thương mại và lưu thông hàng hóa (trừ QLTT); dịch vụ TM (trừ logistics); quản lý cạnh tranh; bán hàng đa cấp; QLNN về giá trong phạm vi ngành; Hội Bảo vệ quyền lợi người tiêu dùng.
- **Phụ trách: Phòng Quản lý thương mại.**

**③ PGĐ2 — Nguyễn Trường Giang.** Trực tiếp phụ trách (không đổi):
- Điện; năng lượng mới; NLTT; sử dụng năng lượng TK&HQ; an toàn trong lĩnh vực điện lực.
- **Phụ trách: Phòng Quản lý năng lượng.**

**④ PGĐ3 — Hoàng Văn Thuân.** Trực tiếp phụ trách:
- **Hóa chất**; **luyện kim**; **vật liệu nổ công nghiệp**; **công nghiệp khai thác mỏ và chế biến khoáng sản**; **công nghiệp môi trường**; **vệ sinh an toàn lao động (trừ lĩnh vực Năng lượng)**.
- **Lĩnh vực xây dựng chuyên ngành Công Thương (trừ các dự án thuộc lĩnh vực Năng lượng)** theo quy định của pháp luật về xây dựng.
- QĐ 7750 **không ghi PGĐ Thuân phụ trách phòng nào** — các lĩnh vực trên nằm ở Phòng QLCN (PGĐ Chiến phụ trách phòng) và Phòng Quản lý Khoáng sản (PGĐ Chung phụ trách phòng).
- ⚠️ So với QĐ 6320 (lịch sử): **nhận lại hóa chất, VLNCN**; thêm đích danh xây dựng chuyên ngành; **không còn** phụ trách Phòng Quản lý Khoáng sản, không còn ghi "dầu khí; than" và nhóm việc "địa chất".

**⑤ PGĐ4 — Phạm Năng Chung.** Trực tiếp phụ trách:
- **Lĩnh vực địa chất, khoáng sản (trừ lĩnh vực PGĐ Hoàng Văn Thuân phụ trách).**
- **Chỉ đạo, phụ trách: Phòng Quản lý Khoáng sản** (mới — 05/10–16/11/2026 Phòng do PGĐ Thuân phụ trách, lịch sử).
- QĐ 7750 ghi gọn một dòng, không liệt kê từng việc như QĐ 6320 (thăm dò, trữ lượng, cấp phép, đóng cửa mỏ, tiền cấp quyền, đấu giá, dữ liệu, khoáng sản làm VLXD) — các việc này vẫn thuộc "địa chất, khoáng sản" của PGĐ Chung.

**⑥ PGĐ5 — Nguyễn Đình Chiến.** Trực tiếp phụ trách:
- CN tiêu dùng; CN thực phẩm; CN hỗ trợ; CN chế biến khác; tiểu thủ công nghiệp; sản xuất và tiêu dùng bền vững; khuyến công; **quản lý cụm công nghiệp**; tư vấn phát triển công nghiệp; **an toàn thực phẩm**; cơ khí; CN công nghệ cao (không bao gồm công nghiệp công nghệ số).
- Lĩnh vực quản lý thị trường; **phòng chống thiên tai - tìm kiếm cứu nạn**.
- **Phụ trách: Phòng Quản lý công nghiệp.**
- ⚠️ So với QĐ 6320 (lịch sử): **không còn hóa chất, vật liệu nổ công nghiệp**.

**⑦ PGĐ6 — Nguyễn Huy Tưởng.** Trực tiếp phụ trách (không đổi):
- Xuất khẩu, nhập khẩu; thương mại biên giới; TMĐT và kinh tế số; xúc tiến thương mại; dịch vụ logistics; phòng vệ thương mại; hiện diện TM và đầu tư KD của nhà cung cấp dịch vụ / nhà đầu tư nước ngoài tại VN.
- QĐ không ghi phòng phụ trách riêng — các lĩnh vực trên nằm trong Phòng QLTM (PGĐ Thành phụ trách phòng).

Mọi PGĐ: thành viên các BCĐ, hội đồng do tỉnh thành lập theo lĩnh vực.

### ⚠️ Lưu ý cốt lõi — thay đổi so với bản phân công trước (QĐ 6320, lịch sử)

- **Hóa chất, tiền chất công nghiệp; VLNCN (GP sử dụng `/GP-SCT`, kho, huấn luyện KTAT), tiền chất thuốc nổ** → **trình và ký KT.GĐ — PGĐ Hoàng Văn Thuân từ 17/11/2026** (QĐ 7750 ghi đích danh "hóa chất", "vật liệu nổ công nghiệp"). Giai đoạn 05/10–16/11/2026 do PGĐ Nguyễn Đình Chiến ký (QĐ 6320 — lịch sử); đến 04/10/2026 do PGĐ Thuân ký (QĐ 766 — lịch sử). Kiểm chứng trên sổ văn bản đi: 7827/SCT-CN ngày 19/11/2026 (hướng dẫn hồ sơ cấp lại GP sử dụng VLNCN) còn do PGĐ Chiến ký; từ 23/11/2026 PGĐ Thuân ký — 7937/GP-SCT (GP sử dụng VLNCN), 7910/KH-SCT (KH kiểm tra, cấp GCN huấn luyện KTAT VLNCN), 7908/SCT-CN (thủ tục đưa kho VLNCN vào sử dụng), đều ngày 23/11/2026.
- **Thẩm định BCNCKT, thiết kế; kiểm tra công tác nghiệm thu công trình công nghiệp** (kho VLNCN, kho hóa chất, nhà máy, công trình mỏ — trừ dự án năng lượng) → **PGĐ Thuân** (QĐ 7750 ghi đích danh "xây dựng chuyên ngành Công Thương"). Trước đó công trình không thuộc mỏ ghi "dự kiến PGĐ Chiến" (05/10–16/11/2026 — lịch sử). Dự án năng lượng → PGĐ Giang.
- **Phòng QLCN vẫn do PGĐ Nguyễn Đình Chiến phụ trách**: cụm công nghiệp, ATTP, khuyến công, cơ khí, CN hỗ trợ/tiêu dùng/thực phẩm/chế biến khác, TTCN, SXTD bền vững, PCTT-TKCN trình PGĐ Chiến.
- **Vận chuyển HHNH, PCCC ngành Công Thương → PGĐ Hoàng Văn Thuân — Bạn chốt 25/11/2026** (QĐ 7750 không ghi đích danh hai lĩnh vực này; Bạn chốt chuyển sang PGĐ Thuân cùng hóa chất, VLNCN). Giấy phép vận chuyển HHNH 07/10–16/11/2026 (6369/GP-SCT … 7680/GP-SCT) do PGĐ Chiến ký — lịch sử.
- **QĐ 7750 không ghi đích danh, Bạn chưa chốt**: an toàn ngành ngoài ATVSLĐ (xăng dầu, khí), KCN, chất lượng SPHH, KHCN-ĐMST lĩnh vực CN. Các việc này của Phòng QLCN **giữ "dự kiến PGĐ Chiến ký" theo Bạn chốt 06/10/2026** (Chiến phụ trách Phòng QLCN) — chờ Bạn xác nhận lại; khi lãnh đạo phân việc khác thì sửa bảng dưới.
- **Dầu khí, than**: QĐ 6320 ghi cho PGĐ Thuân (lịch sử); QĐ 7750 không ghi — hỏi Bạn khi phát sinh, không tự gán.
- **PGĐ Hoàng Văn Thuân** giữ: khai thác mỏ, chế biến khoáng sản, luyện kim, **công nghiệp môi trường**, **ATVSLĐ** (nay ghi rõ "trừ lĩnh vực Năng lượng" — an toàn điện thuộc PGĐ Giang); thẩm định thiết kế mỏ (thuộc khai thác mỏ và xây dựng chuyên ngành).
- **Phòng Quản lý Khoáng sản**: **PGĐ Phạm Năng Chung phụ trách phòng** và chỉ đạo địa chất, khoáng sản (cấp phép, tiền cấp quyền, đấu giá, đóng cửa mỏ, dữ liệu, KS làm VLXD); PGĐ Thuân chỉ đạo phần công nghiệp khai thác mỏ, chế biến khoáng sản. Ký hiệu `/SCT-KS`, dòng `Lưu: VT, KS.` (reference `03` mục C).
- **Phòng QLTM**: PGĐ Thành phụ trách phòng; PGĐ Tưởng chỉ đạo lĩnh vực XNK, TM biên giới, XTTM, TMĐT, logistics, phòng vệ TM.
- **Lĩnh vực của PGĐ Thuân nằm ở Phòng QLCN** (đối chiếu Điều 5 QĐ 6226/QĐ-SCT với khoản 4 Điều 2 QĐ 7750/QĐ-SCT): **hóa chất, tiền chất**; **VLNCN, tiền chất thuốc nổ**; **công nghiệp luyện kim** (mục 2.2 — phần cơ khí của mục này thuộc PGĐ Chiến); **bảo vệ môi trường và phát triển công nghiệp môi trường** (mục 2.10); **ATVSLĐ**: kiểm định kỹ thuật an toàn lao động, máy - thiết bị có yêu cầu nghiêm ngặt (điểm b, c mục 2.12); **thẩm định, kiểm tra nghiệm thu công trình công nghiệp**. Khai thác mỏ, chế biến khoáng sản và ATVSLĐ trong khai thác thuộc **Phòng Quản lý khoáng sản** (Điều 6). Các nhiệm vụ còn lại của Phòng QLCN do PGĐ Chiến (phụ trách Phòng) chỉ đạo.

### Cặp xử lý thay khi vắng (đi công tác nước ngoài / nghỉ phép) — không đổi so với bản trước

| Khi vắng | Người xử lý thay công việc hằng ngày |
|---|---|
| GĐ Hoàng Chí Hiền | PGĐ1 Trịnh Văn Thành (ủy quyền phụ trách Sở) |
| PGĐ1 Trịnh Văn Thành | PGĐ6 Nguyễn Huy Tưởng |
| PGĐ6 Nguyễn Huy Tưởng | PGĐ1 Trịnh Văn Thành |
| PGĐ2 Nguyễn Trường Giang | PGĐ5 Nguyễn Đình Chiến |
| PGĐ5 Nguyễn Đình Chiến | PGĐ2 Nguyễn Trường Giang |
| PGĐ3 Hoàng Văn Thuân | PGĐ4 Phạm Năng Chung |
| PGĐ4 Phạm Năng Chung | PGĐ3 Hoàng Văn Thuân |

→ Hệ quả với Phòng QLCN: khi **Thuân vắng**, việc hóa chất, VLNCN, thẩm định - nghiệm thu công trình, môi trường, ATVSLĐ trình **PGĐ Chung**; khi **Chiến vắng**, việc CCN, ATTP, khuyến công, PCTT trình **PGĐ Giang**.

### Xã/phường theo dõi (phụ trách hoạt động Công Thương) — 99/99 xã, phường

- **GĐ Hiền (9):** Phong Dụ Hạ, Phong Dụ Thượng, Châu Quế, Lâm Giang, Đông Cuông, Tân Hợp, Mậu A, Xuân Ái, Mỏ Vàng.
- **PGĐ1 Thành (10):** Nghĩa Lộ, Cầu Thia, Trung Tâm, Liên Sơn, Gia Hội, Thượng Bằng La, Chấn Thịnh, Nghĩa Tâm, Sơn Lương, Cát Thịnh.
- **PGĐ2 Giang (22):** Cam Đường, Lào Cai, Sa Pa, Cốc San, Hợp Thành, Mường Bo, Tả Van, Bản Hồ, Tả Phìn, Ngũ Chỉ Sơn, Mù Cang Chải, Khao Mang, Púng Luông, Chế Tạo, Nậm Có, Lao Chải, Tú Lệ, Trạm Tấu, Hạnh Phúc, Phình Hồ, Tà Xi Láng, Văn Chấn.
- **PGĐ3 Thuân (13):** Bảo Thắng, Phong Hải, Xuân Quang, Tằng Loỏng, **Gia Phú** (nơi có KCN Phú Xuân, Phú Xuân 1), Cốc Lầu, Bảo Nhai, Bản Liền, Bắc Hà, Tả Củ Tỷ, Lùng Phình, Si Ma Cai, Sín Chéng.
- **PGĐ4 Chung (20):** Bảo Yên, Nghĩa Đô, Thượng Hà, Xuân Hòa, Phúc Khánh, Bảo Hà, Văn Bàn, Võ Lao, Khánh Yên, Dương Quỳ, Chiềng Ken, Minh Lương, Nậm Chày, Nậm Xé, Lâm Thượng, Lục Yên, Tân Lĩnh, Khánh Hòa, Phúc Lợi, Mường Lai.
- **PGĐ5 Chiến (14):** Cảm Nhân, Yên Thành, Thác Bà, Yên Bình, Bảo Ái, Trấn Yên, Lương Thịnh, Hưng Khánh, Việt Hồng, Quy Mông, Văn Phú, Yên Bái, Nam Cường, Âu Lâu.
- **PGĐ6 Tưởng (11):** Bát Xát, Mường Hum, Dền Sáng, Y Tý, A Mú Sung, Trịnh Tường, Bản Xèo, Mường Khương, Pha Long, Bản Lầu, Cao Sơn.

> So với QĐ 6320 (lịch sử): (1) 13 xã Bảo Thắng … Sín Chéng trước đây chưa giao ai, nay giao **PGĐ Thuân**; (2) 08 xã Văn Bàn, Võ Lao, Khánh Yên, Dương Quỳ, Chiềng Ken, Minh Lương, Nậm Chày, Nậm Xé chuyển từ PGĐ Thuân sang **PGĐ Chung**; (3) 06 xã Bảo Yên, Nghĩa Đô, Thượng Hà, Xuân Hòa, Phúc Khánh, Bảo Hà trước ghi ở cả hai người, nay chỉ PGĐ Chung; (4) danh sách của GĐ, PGĐ Thành, Giang, Chiến, Tưởng không đổi. Xã Xuân Hòa là xã riêng, KHÔNG phải nơi đặt KCN Phú Xuân.

## Chức năng, nhiệm vụ Văn phòng và các phòng (QĐ 6226/QĐ-SCT ngày 02/10/2026) — chi tiết: `references/01-chuc-nang-nhiem-vu-cac-phong-qd6226.md`

Tóm tắt để định tuyến (viện dẫn "mục 2.x khoản 2 Điều y QĐ 6226/QĐ-SCT"; chi tiết từng điểm: mở ref 01):

- **1. Văn phòng Sở (Điều 3)** — tổ chức bộ máy - cán bộ; tài chính, tài sản cơ quan **và tài chính ngành**; pháp chế; CCHC, ISO, thường trực Một cửa; thi đua; bảo vệ chính trị nội bộ; dân vận; hành chính - văn thư - con dấu - chữ ký số, PCCC cơ quan, trang thông tin điện tử; thường trực kiểm tra chuyên ngành, tiếp công dân, KNTC, PCTN, trả lời cử tri; đôn đốc tiến độ; phân công thực hiện phân cấp, ủy quyền; hướng dẫn chức năng Phòng Kinh tế cấp xã; phòng thủ tỉnh; thường trực Hội đồng định giá tài sản trong tố tụng hình sự.
- **2. Phòng Kế hoạch - Tổng hợp (Điều 4)** — chiến lược, quy hoạch, kế hoạch ngành; thống kê, báo cáo ngành tuần/tháng/quý/năm; dự thảo QĐ, chỉ thị cá biệt của UBND tỉnh; chương trình công tác, thông báo kết luận họp Lãnh đạo Sở; quản lý đầu tư (ý kiến chủ trương đầu tư, GCN đầu tư ngành; thẩm định dự toán); CTMTQG; CNTT, quản trị mạng, KHCN-ĐMST-chuyển đổi số ngành; hướng dẫn nghiệp vụ cấp xã.
- **3. Phòng Quản lý công nghiệp (Điều 5)** — CN địa phương, thống kê SXCN (trừ năng lượng, khoáng sản); cơ khí, luyện kim; CN hỗ trợ; ATTP, CN tiêu dùng - thực phẩm - chế biến khác; khuyến công; **CCN (cơ quan đầu mối)**; TTCN; SX-TD bền vững; chất lượng SPHH; BVMT - CN môi trường; hóa chất, VLNCN; an toàn ngành (trừ năng lượng, khai thác chế biến khoáng sản) gồm HHNH, xăng dầu, khí, máy - thiết bị nghiêm ngặt, kiểm định KTAT lao động, tài liệu an toàn; thẩm định, KTCTNT công trình công nghiệp; tổng hợp nhiệm vụ KCN (nếu có); dầu khí (trừ thương mại); tiền chất; thường trực PCTT-TKCN, KHCN-ĐMST lĩnh vực CN, PCCC. **Cơ cấu nội bộ, chuyên viên ↔ lĩnh vực, người soạn/người ký: mục ngay dưới.**
- **4. Phòng Quản lý khoáng sản (Điều 6)** — than; địa chất, khoáng sản (cấp phép, đóng cửa mỏ, tiền cấp quyền, đấu giá, trữ lượng, khu vực cấm, dữ liệu); VLXD; công nghiệp khai thác mỏ và chế biến khoáng sản (thẩm định dự án, thiết kế; an toàn, ATVSLĐ trong khai thác, chế biến khoáng sản).
- **5. Phòng Quản lý năng lượng (Điều 7)** — điện, năng lượng mới, NLTT, TKNL (GP hoạt động điện lực, thẩm định công trình năng lượng, cơ quan chuyên môn về xây dựng công trình ngành Điện); an toàn đập, hồ chứa thủy điện; điện nông thôn.
- **6. Phòng Quản lý thương mại (Điều 8)** — thị trường trong nước (chợ, TTTM, siêu thị; **rượu, thuốc lá, xăng dầu, khí** - GCN đủ điều kiện kinh doanh); XNK; thương mại biên giới; TMĐT; XTTM; cạnh tranh; bán hàng đa cấp; phòng vệ TM; logistics; bảo vệ NTD; hội nhập KTQT, BCĐ Hội nhập quốc tế; phối hợp Chi cục QLTT.
- **Chi cục Quản lý thị trường** — tổ chức hành chính trực thuộc Sở (không phải phòng chuyên môn); CNNV do UBND tỉnh quyết định riêng.

### 3. Phòng Quản lý công nghiệp — cơ cấu nội bộ, người soạn, người ký (dùng hằng ngày)

#### Cơ cấu nội bộ Phòng QLCN (phân công đến từng công chức)

> Nguồn: **Thông báo phân công nhiệm vụ cho cán bộ, công chức Phòng QLCN** do Trưởng phòng
> **Nguyễn Hữu Long** ký ngày **10/7/2026** (thông báo nội bộ phòng, **không có số văn bản**),
> **hiệu lực kể từ ngày 10/7/2026** — thay thế bản phân công cũ. Căn cứ tại thời điểm ban hành (lịch sử): QĐ 59/QĐ-SCT và
> QĐ 04/QĐ-SCT cùng ngày 01/7/2025 (nay thay bằng QĐ 6226/QĐ-SCT và QĐ 7750/QĐ-SCT — lịch sử).

**Nguyên tắc làm việc (Phần A Thông báo):**
- **Trưởng phòng**: lãnh đạo, chỉ đạo, quản lý toàn diện; trực tiếp phân công nhiệm vụ cho PTP và chuyên viên; kiểm duyệt, cho ý kiến mọi dự thảo văn bản của phòng **trước khi trình Lãnh đạo Sở**.
- **Các Phó Trưởng phòng**: chịu trách nhiệm trước GĐ Sở, Trưởng phòng và pháp luật về lĩnh vực phụ trách; trực tiếp chỉ đạo, hướng dẫn chuyên viên; **kiểm duyệt dự thảo của chuyên viên thuộc lĩnh vực mình trước khi trình Trưởng phòng hoặc Lãnh đạo Sở**.
- **Chuyên viên**: chủ động xử lý việc được phân công; báo cáo, trao đổi kịp thời với PTP phụ trách trực tiếp. **Khi PTP phụ trách vắng mặt hoặc chuyên viên và PTP không thống nhất phương án** → chuyên viên **báo cáo trực tiếp Trưởng phòng** quyết định.

**Lãnh đạo phòng (1 TP + 3 PTP):**

| Lãnh đạo | Trực tiếp chỉ đạo, thực hiện |
|---|---|
| **Trưởng phòng — Nguyễn Hữu Long** | Phụ trách chung; chủ trì/phối hợp xây dựng chiến lược, quy hoạch, kế hoạch, đề án, VBQPPL của phòng. Trực tiếp chỉ đạo: **① Quản lý cụm công nghiệp; ② Vật liệu nổ công nghiệp; ③ KHCN - đổi mới sáng tạo trong lĩnh vực công nghiệp**. Thường trực BCĐ PCTT-TKCN ngành Công Thương Lào Cai. |
| **PTP — Nguyễn Hồng Vân** *(lịch sử đến 01/10/2026 — từ 02/10/2026 là Phó Trưởng phòng Quản lý Khoáng sản theo QĐ 6231/QĐ-SCT; người kiểm duyệt mới các mảng dưới đây tại Phòng QLCN: hỏi Bạn — reference `03` mục C)* | ① CN khai thác mỏ và chế biến **khoáng sản**; ② **Hóa chất**; tiền chất ma túy, tiền chất công nghiệp; Thường trực BCĐ phòng ngừa, ứng phó sự cố hóa chất tỉnh; ③ **Thẩm định BCNCKT, BCKTKT ĐTXD và các bước thiết kế sau TKCS, kiểm tra công tác nghiệm thu** các dự án; ④ **Thường trực, giải quyết công việc của Phòng khi Trưởng phòng đi vắng**. |
| **PTP — Trần Trọng Trang** | ① **ATTP**, CN tiêu dùng, CN thực phẩm và CN chế biến khác; **quản lý chất lượng sản phẩm hàng hóa**; **sản xuất và tiêu dùng bền vững**; ② **Bảo vệ môi trường** và phát triển CN môi trường; ③ **Quản lý an toàn** đối với ngành, lĩnh vực thuộc phạm vi quản lý (bao trùm an toàn HHNH, xăng dầu, khí, máy - thiết bị nghiêm ngặt, kiểm định KTAT); ④ **Phối hợp** chỉ đạo, thực hiện nhiệm vụ về quản lý **cụm công nghiệp**. |
| **PTP — Đỗ Mạnh Cường** | ① CN địa phương; ② CN cơ khí, CN điện tử; ③ CN hỗ trợ; ④ Khuyến công; ⑤ Tiểu thủ công nghiệp. |

⚠️ Thay đổi lớn so với bản phân công cũ: phòng nay có **3 PTP** (trước chỉ ghi nhận 1); **VLNCN và CCN do Trưởng phòng trực tiếp chỉ đạo** (không qua PTP, PTP Trang chỉ *phối hợp* CCN); PTP Trang **không còn trực tiếp** phụ trách HHNH/PCCC/KCN như bản cũ — các nội dung an toàn nằm trong nhóm "quản lý an toàn" ở trên; **khi TP vắng, PTP Vân thường trực** (không phải PTP Trang).

**Chuyên viên ↔ nhiệm vụ (Phần B Thông báo, mục V–XIV):**

| Chuyên viên | CHỦ TRÌ | PHỐI HỢP |
|---|---|---|
| **Lã Doãn Nam** | **ATTP**; CN tiêu dùng; CN thực phẩm và CN chế biến khác (trọn quy trình từ SX - chế biến - bảo quản - vận chuyển - KD; ATTP chợ/siêu thị/TTTM; chống thực phẩm giả) | Quản lý chất lượng SPHH |
| **Nguyễn Thị Thùy Dương** | (i) **Quản lý chất lượng SPHH** (chỉ định tổ chức ĐGSPH; đăng ký chứng nhận - thử nghiệm - giám định - kiểm định; tiếp nhận công bố hợp quy); (ii) **SX và tiêu dùng bền vững** | ATTP, CN tiêu dùng, CN thực phẩm, CN chế biến khác |
| **Lê Quang Trung** | (i) **Cụm công nghiệp** (đầu mối QLNN; thẩm định trình UBND tỉnh thành lập/mở rộng/điều chỉnh/bãi bỏ; Quy chế quản lý CCN; tham gia ý kiến dự án hạ tầng + dự án SXKD trong CCN; CSDL CCN); (ii) **CN địa phương** (thống kê sản lượng, giá trị SXCN, chỉ số SXCN; hướng dẫn Phòng Kinh tế cấp xã; DN, HTX, làng nghề) | PCCC ngành Công Thương |
| **Bùi Việt Cường** | (i) **Khuyến công**; (ii) CN **cơ khí**, CN **điện tử** (gồm luyện kim trong chính sách phát triển ngành cơ khí - luyện kim - điện tử); (iii) **CN hỗ trợ**; (iv) **Tiểu thủ công nghiệp** | CN địa phương; PCCC ngành Công Thương |
| **Nguyễn Thị Thúy Nhung** | (i) **Chế biến khoáng sản, luyện kim**; thẩm định, chấp thuận tài liệu an toàn; (ii) **Chủ trì tổng hợp báo cáo định kỳ, đột xuất của Phòng** | Sát hạch kiểm tra KTAT khai thác khoáng sản; PCTT-TKCN; phòng ngừa ứng phó sự cố hóa chất; an toàn hồ đập |
| **Vũ Việt Linh** | (i) **Quản lý an toàn ngành**: tuyên truyền - kiểm tra an toàn trong quản lý, sử dụng, bảo quản, KD và **vận chuyển HHNH**, xăng dầu, khí, máy - thiết bị nghiêm ngặt về KTAT; **tập huấn** người điều khiển phương tiện, người áp tải, xếp dỡ, thủ kho; **kiểm định KTAT lao động**, kiểm định thiết bị điện; chủ trì thẩm định chấp thuận tài liệu an toàn; thẩm định trình cấp **chứng chỉ kiểm định viên**; (ii) **PCCC** ngành Công Thương; (iii) Tham mưu ý kiến về **thăm dò, đóng cửa mỏ** | VLNCN; thẩm định BCNCKT/BCKTKT/thiết kế sau TKCS công trình CN; quản lý an toàn ngành |
| **Ngô Ngọc Dũng** | (i) Triển khai **Quy hoạch khoáng sản** thuộc lĩnh vực SCT; **an toàn hồ, đập** ngành Công Thương (trừ hồ đập thủy điện); **thường trực PCTT-TKCN** của ngành; (ii) Chủ trì/phối hợp **thẩm định BCNCKT, BCKTKT, thiết kế sau TKCS** công trình công nghiệp; (iii) QLNN và **kiểm tra công tác nghiệm thu (KTCTNT)** công trình chuyên ngành CN | PCCC ngành Công Thương |
| **Lê Minh Long** | (i) **BVMT và phát triển CN môi trường** (VBQPPL; Đề án CN môi trường; kinh tế tuần hoàn; ứng phó BĐKH ngành CT; thống kê môi trường; báo cáo hằng năm UBND tỉnh + Bộ Công Thương); (ii) Tổ chức **sát hạch kiểm tra KTAT về khai thác khoáng sản**; (iii) Nhiệm vụ BVMT ngành Công Thương | Thẩm định BCNCKT/BCKTKT/thiết kế sau TKCS công trình CN |
| **Nguyễn Thị Loan** | (i) **Hóa chất**; phòng ngừa ứng phó sự cố hóa chất; (ii) Quản lý **tiền chất ma túy, tiền chất công nghiệp** lĩnh vực công thương | Tổng hợp báo cáo định kỳ, đột xuất của Phòng |
| **Trần Đăng Khôi** | (i) **VLNCN** trọn gói: chiến lược - kế hoạch phát triển ngành VLNCN; tuyên truyền, kiểm tra, phối hợp thanh tra, đề xuất xử lý vi phạm; **thẩm định trình cấp/cấp lại/thu hồi GP sử dụng VLNCN**; **huấn luyện, kiểm tra, trình cấp GCN huấn luyện KTAT VLNCN**; nhiệm vụ theo Luật 42/2024 (Luật QLSD vũ khí, VLN, CCHT); **quản lý tiền chất thuốc nổ**; (ii) **KHCN - ĐMST trong lĩnh vực công nghiệp** | Cụm công nghiệp; PCCC ngành Công Thương |

**Phân tầng duyệt nội bộ phòng (theo lĩnh vực):**

| Lĩnh vực | Chuyên viên chủ trì | PTP kiểm duyệt | Ghi chú |
|---|---|---|---|
| CCN | Trung (+ Khôi phối hợp) | — **TP Long trực tiếp** (PTP Trang phối hợp chỉ đạo) | |
| VLNCN, tiền chất thuốc nổ | Khôi (+ Linh phối hợp) | — **TP Long trực tiếp** | |
| KHCN-ĐMST lĩnh vực CN | Khôi | — **TP Long trực tiếp** | |
| Khoáng sản (chế biến, luyện kim, tài liệu an toàn) | Nhung | **PTP Vân** | |
| Quy hoạch khoáng sản, an toàn hồ đập, PCTT | Dũng | **PTP Vân** (khoáng sản) | PCTT: TP Long là thường trực BCĐ |
| Hóa chất, tiền chất | Loan | **PTP Vân** | |
| Thẩm định BCNCKT/BCKTKT/thiết kế, KTCTNT | Dũng (+ Linh, M.Long phối hợp) | **PTP Vân** | |
| ATTP, CN tiêu dùng/thực phẩm/chế biến khác | Nam (+ Dương phối hợp) | **PTP Trang** | |
| Chất lượng SPHH, SXTD bền vững | Dương (+ Nam phối hợp) | **PTP Trang** | |
| BVMT, CN môi trường, sát hạch KTAT khai thác KS | M.Long | **PTP Trang** | |
| An toàn ngành, HHNH (toàn bộ), kiểm định KTAT, PCCC, thăm dò - đóng cửa mỏ | Linh | **PTP Trang** | |
| CN địa phương | Trung (+ Cường phối hợp) | **PTP Đ.M.Cường** | |
| Cơ khí - điện tử, CN hỗ trợ, khuyến công, TTCN | Cường (CV) | **PTP Đ.M.Cường** | |

✅ **Hai điểm Thông báo 10/7/2026 không nêu đích danh — Bạn đã chốt ngày 15/7/2026:**
1. **Khu công nghiệp**: CV **Lê Quang Trung** tiếp tục theo dõi KCN / tham gia ý kiến dự án trong KCN.
2. **HHNH (vận chuyển hàng hóa nguy hiểm)**: **toàn bộ về CV Vũ Việt Linh** — cả thụ lý hồ sơ cấp GP vận chuyển lẫn an toàn - kiểm tra - tập huấn. Riêng giai đoạn **6/7 – 14/7/2026** hồ sơ HHNH do CV Khôi thụ lý — văn bản giai đoạn này giữ `CV Khôi` đúng lịch sử, không sửa lại.

**Bảng routing trình Lãnh đạo Sở (phân công BGĐ QĐ 7750/QĐ-SCT ngày 17/11/2026 + phân công nội bộ 10/7/2026):**

| Lĩnh vực | CV chủ trì | Kiểm duyệt nội bộ | Trình lên |
|---|---|---|---|
| Hóa chất; tiền chất ma túy, tiền chất công nghiệp | Loan | PTP Vân → TP Long | **PGĐ Hoàng Văn Thuân** *(từ 17/11/2026, QĐ 7750; 05/10–16/11/2026 PGĐ Chiến — lịch sử)* |
| VLNCN (GP sử dụng `/GP-SCT`, PANM, kho, huấn luyện KTAT); tiền chất thuốc nổ | Khôi | TP Long | **PGĐ Hoàng Văn Thuân** *(từ 17/11/2026, QĐ 7750; 05/10–16/11/2026 PGĐ Chiến — lịch sử)* |
| PCTT-TKCN | Dũng (thường trực) | TP Long | **PGĐ Nguyễn Đình Chiến** |
| ATTP; CN tiêu dùng/thực phẩm/chế biến khác; rượu - bia (về ATTP/CN) | Nam | PTP Trang → TP Long | **PGĐ Nguyễn Đình Chiến** |
| Chất lượng SPHH; SXTD bền vững | Dương | PTP Trang → TP Long | **PGĐ Nguyễn Đình Chiến** |
| Cơ khí; CN điện tử; CN công nghệ cao; CN hỗ trợ; khuyến công; TTCN; CN địa phương | Cường (CV) / Trung (CN địa phương) | PTP Đ.M.Cường → TP Long | **PGĐ Nguyễn Đình Chiến** |
| CCN (thường lệ); KCN (thường lệ) | Trung | TP Long | **PGĐ Nguyễn Đình Chiến** |
| HHNH (gồm cấp GP vận chuyển); PCCC ngành CT | Linh | PTP Trang → TP Long | **PGĐ Hoàng Văn Thuân** *(Bạn chốt 25/11/2026; 05/10–24/11/2026 PGĐ Chiến — lịch sử)* |
| An toàn ngành khác (phần an toàn xăng dầu, khí) | Linh | PTP Trang → TP Long | **PGĐ Nguyễn Đình Chiến** *(dự kiến — Bạn chốt 06/10/2026; QĐ 7750 không ghi đích danh, chờ Bạn xác nhận lại)* |
| Thẩm định BCNCKT/BCKTKT/thiết kế, KTCTNT **công trình công nghiệp không thuộc mỏ** (kho VLNCN, kho hóa chất, nhà máy CN…; trừ dự án năng lượng) | Dũng / Khôi | PTP Vân → TP Long | **PGĐ Hoàng Văn Thuân** *(từ 17/11/2026 — QĐ 7750 ghi "xây dựng chuyên ngành Công Thương")* |
| KHCN-ĐMST lĩnh vực CN | Khôi | TP Long | **PGĐ Nguyễn Đình Chiến** *(dự kiến — QĐ 7750 không ghi đích danh)* |
| Than, CN khai thác mỏ, chế biến khoáng sản; thẩm định dự án, báo cáo, **thiết kế mỏ**; KTCTNT công trình mỏ; kiểm tra an toàn, ATVSLĐ trong khai thác (Điều 6 QĐ 6226 — **Phòng Quản lý khoáng sản**) | chuyên viên Phòng Quản lý Khoáng sản (Nhung, Dũng đã điều động 02/10/2026) | PTP Nguyễn Hồng Vân → TP Lưu Đức Cường | **PGĐ Hoàng Văn Thuân** *(QĐ 7750: "công nghiệp khai thác mỏ và chế biến khoáng sản", xây dựng chuyên ngành; than không ghi đích danh)* |
| Công nghiệp luyện kim (mục 2.2 Điều 5 QĐ 6226); dầu khí trừ thương mại (khoản 1 Điều 5) — **Phòng QLCN** | CV V.Cường (chính sách cơ khí - luyện kim) | PTP Đ.M.Cường → TP Long | **PGĐ Hoàng Văn Thuân** (luyện kim; phần cơ khí → PGĐ Chiến; dầu khí: QĐ 7750 không ghi đích danh — hỏi Bạn) |
| CN môi trường; BVMT ngành CT, ứng phó BĐKH, KNK (mục 2.10 Điều 5 QĐ 6226) | M.Long (đã có QĐ điều động 02/10/2026 — người tham mưu hiện tại: hỏi Bạn) | PTP Trang → TP Long | **PGĐ Hoàng Văn Thuân** *(QĐ 7750 ghi "công nghiệp môi trường"; mục 2.10 gộp BVMT và CN môi trường)* |
| ATVSLĐ; máy - thiết bị - vật tư có yêu cầu nghiêm ngặt về ATLĐ, kiểm định KTAT (điểm b, c mục 2.12 Điều 5 QĐ 6226) | Linh | PTP Trang → TP Long | **PGĐ Hoàng Văn Thuân** |
| Khoáng sản: thăm dò, trữ lượng, cấp phép (đầu mối tham mưu), đóng cửa mỏ, tiền cấp quyền, đấu giá, dữ liệu; KS làm VLXD | Phòng Quản lý Khoáng sản (Linh: thăm dò - đóng cửa mỏ đến khi bàn giao) | PTP Nguyễn Hồng Vân → TP Lưu Đức Cường (reference `03`) | **PGĐ Phạm Năng Chung** *(phụ trách Phòng Quản lý Khoáng sản từ 17/11/2026)* |
| **Tờ trình, kế hoạch, quy hoạch, chủ trương đầu tư** (mọi lĩnh vực, kể cả KCN/CCN) | (CV lĩnh vực) | PTP → TP Long | **GĐ Hoàng Chí Hiền** |

> ⚠️ **Quy tắc trình GĐ:** mọi **Tờ trình, kế hoạch, quy hoạch, chủ trương đầu tư** (kể cả về KCN/CCN) trình **trực tiếp Giám đốc Hoàng Chí Hiền** — kể cả khi nội dung thuộc lĩnh vực thường lệ của PGĐ. Việc thường lệ (cấp phép, thẩm định hồ sơ, công văn tham gia ý kiến, báo cáo chuyên đề) mới trình PGĐ phụ trách.
> Khi **Chiến vắng** → việc nhóm Chiến trình **PGĐ Giang**; khi **Thuân vắng** → **PGĐ Chung**; khi **Chung vắng** → **PGĐ Thuân**.
> Văn bản hóa chất, VLNCN ban hành **05/10–16/11/2026** do PGĐ Chiến ký (QĐ 6320) và văn bản **trước 05/10/2026** do PGĐ Thuân ký (hóa chất, VLNCN, HHNH, PCCC…) là lịch sử đúng thời điểm — không sửa lại.

#### Dòng Lưu, CHUYÊN VIÊN THAM MƯU và NGƯỜI KÝ (khối chữ ký)

**a) Dòng Lưu cuối Nơi nhận:** `Lưu: VT, CN(Tên).` — **VT** = Văn thư, **CN** = Phòng Quản lý công nghiệp, trong ngoặc là **tên chuyên viên soạn thảo** (Bạn chốt 16/11/2026, khôi phục quy ước trước 01/10/2026); công văn nội bộ Phòng ghi `Lưu: CN(Tên).`. Nơi nhận có dòng "- Ban Giám đốc Sở;". Ngoại lệ: Giấy phép, Giấy chứng nhận thủ tục hành chính ghi `Lưu: VT, BP1C, CN.`, không gửi Ban Giám đốc Sở. Văn bản ban hành 01/10–16/11/2026 ghi "Lưu: VT, CN." không tên là lịch sử, không sửa lại.

Bảng dưới cho biết **chuyên viên nào tham mưu lĩnh vực nào** — dùng để giao việc, hỏi thông tin, kiểm duyệt và **lấy tên ghi vào dòng Lưu**:

| Chuyên viên | Gọi tắt | Lĩnh vực mặc định (từ 10/7/2026) |
|---|---|---|
| Lã Doãn Nam | CV Nam | ATTP, CN tiêu dùng/thực phẩm/chế biến khác |
| Nguyễn Thị Thùy Dương | CV Dương | Chất lượng SPHH, SXTD bền vững |
| Lê Quang Trung | CV Trung | CCN, CN địa phương (KCN: mặc định, xác nhận) |
| Bùi Việt Cường | CV V.Cường (phân biệt PTP Đỗ Mạnh Cường) | Khuyến công, cơ khí - điện tử, CN hỗ trợ, TTCN |
| Nguyễn Thị Thúy Nhung | CV Nhung | Khoáng sản (chế biến, luyện kim), tổng hợp báo cáo Phòng |
| Vũ Việt Linh | CV Linh | An toàn ngành, **HHNH toàn bộ (cấp GP vận chuyển + an toàn/tập huấn — Bạn chốt 15/7/2026)**, kiểm định KTAT, PCCC, thăm dò - đóng cửa mỏ |
| Ngô Ngọc Dũng | CV Dũng | Thẩm định công trình CN, KTCTNT, quy hoạch khoáng sản, hồ đập, PCTT |
| Lê Minh Long | CV M.Long (phân biệt TP Nguyễn Hữu Long) | BVMT, CN môi trường, KNK/carbon |
| Nguyễn Thị Loan | CV Loan | Hóa chất, tiền chất |
| Trần Đăng Khôi | CV Khôi | VLNCN, tiền chất thuốc nổ, GCN huấn luyện KTAT, KHCN-ĐMST CN (HHNH chỉ trong giai đoạn 6/7–14/7/2026) |
| Trần Trọng Trang (PTP tự soạn) | PTP Trang | |

⚠️ **Hai cặp trùng tên** (chỉ để gọi trong trao đổi nội bộ, không ghi vào văn bản): (1) CV **Lê Minh Long** ↔ TP **Nguyễn Hữu Long** → gọi **CV M.Long**; (2) CV **Bùi Việt Cường** ↔ PTP **Đỗ Mạnh Cường** → gọi **CV V.Cường** / **PTP Đ.M.Cường**.

**b) Khối người ký — xác định theo LĨNH VỰC (không theo xã theo dõi), từ 17/11/2026 (QĐ 7750/QĐ-SCT, thay QĐ 6320/QĐ-SCT):**

| Loại việc | Khối ký | Người ký |
|---|---|---|
| CCN, ATTP, khuyến công, CN tiêu dùng/thực phẩm/hỗ trợ/công nghệ cao, cơ khí, CN địa phương, TTCN, SXTD bền vững; **PCTT-TKCN** — *báo cáo, công văn, thẩm định, cấp phép thường lệ* | KT. GIÁM ĐỐC<br>PHÓ GIÁM ĐỐC | **Nguyễn Đình Chiến** |
| **Hóa chất, tiền chất; VLNCN (GP sử dụng `/GP-SCT`, kho, huấn luyện), tiền chất thuốc nổ**; thẩm định thiết kế, KTCTNT công trình công nghiệp (kể cả kho VLNCN, kho hóa chất, công trình mỏ; trừ dự án năng lượng); khai thác mỏ, chế biến khoáng sản, luyện kim, thẩm định thiết kế mỏ; CN môi trường/BVMT; ATVSLĐ (trừ lĩnh vực năng lượng) | KT. GIÁM ĐỐC<br>PHÓ GIÁM ĐỐC | **Hoàng Văn Thuân** *(hóa chất, VLNCN, công trình không thuộc mỏ: từ 17/11/2026; 05/10–16/11/2026 PGĐ Chiến — lịch sử)* |
| **Vận chuyển HHNH; PCCC ngành CT** | KT. GIÁM ĐỐC<br>PHÓ GIÁM ĐỐC | **Hoàng Văn Thuân** *(Bạn chốt 25/11/2026; 05/10–24/11/2026 PGĐ Chiến — lịch sử)* |
| An toàn ngành (ngoài ATVSLĐ), KCN, chất lượng SP, KHCN-ĐMST CN | KT. GIÁM ĐỐC<br>PHÓ GIÁM ĐỐC | **Nguyễn Đình Chiến** *(dự kiến — Bạn chốt 06/10/2026; QĐ 7750 không ghi đích danh, chờ Bạn xác nhận lại)* |
| Địa chất, khoáng sản: thăm dò, trữ lượng, cấp phép, đóng cửa mỏ, tiền cấp quyền, đấu giá, dữ liệu; KS làm VLXD | KT. GIÁM ĐỐC<br>PHÓ GIÁM ĐỐC | **Phạm Năng Chung** |
| Điện, năng lượng, an toàn điện | KT. GIÁM ĐỐC<br>PHÓ GIÁM ĐỐC | **Nguyễn Trường Giang** |
| **Tờ trình, kế hoạch, quy hoạch, chủ trương đầu tư** (mọi lĩnh vực, kể cả KCN/CCN); báo cáo tổng kết/sơ kết toàn ngành; báo cáo theo chỉ đạo Tỉnh ủy/quan trọng | GIÁM ĐỐC | **Hoàng Chí Hiền** |

**Mẫu khối ký** (đặt nửa phải trang, in đậm, căn giữa khối):
- PGĐ ký thay GĐ: dòng 1 `KT. GIÁM ĐỐC` → dòng 2 `PHÓ GIÁM ĐỐC` → (chừa khoảng trống chữ ký) → họ tên PGĐ.
- GĐ ký trực tiếp: dòng 1 `GIÁM ĐỐC` → (chừa khoảng trống) → `Hoàng Chí Hiền`.

**c) Hai lưu ý xác định người ký:**
- ⚠️ **Báo cáo chuyên đề ≠ Tờ trình.** Báo cáo kết quả rà soát / đề xuất theo lĩnh vực (vd "Báo cáo kết quả rà soát, đề xuất mở rộng CCN Âu Lâu") → **PGĐ phụ trách** ký KT.GĐ (CCN → Chiến). Chỉ **Tờ trình đề nghị UBND tỉnh** thành lập/mở rộng CCN, chủ trương đầu tư, quy hoạch mới do **Giám đốc** ký.
- ⚠️ **Xã theo dõi KHÔNG quyết định người ký.** Người ký xác định theo **lĩnh vực chuyên môn**, không theo PGĐ "theo dõi hoạt động Công Thương" của xã nơi đối tượng tọa lạc. Vd: một kho VLNCN ở xã Văn Bàn (PGĐ Chung theo dõi xã) — văn bản về kho vẫn do **PGĐ Thuân** ký vì VLNCN thuộc lĩnh vực của Thuân (từ 17/11/2026).

### 4–6. Phòng Quản lý khoáng sản, Phòng Quản lý năng lượng, Phòng Quản lý thương mại, Chi cục QLTT

Nhiệm vụ chi tiết theo Điều 6, 7, 8 QĐ 6226/QĐ-SCT và ghi chú về Chi cục QLTT: `references/01-chuc-nang-nhiem-vu-cac-phong-qd6226.md`.

## Bảng routing nhanh — Việc nào, giao phòng nào

| Vấn đề | Phòng chủ trì | Phòng phối hợp |
|---|---|---|
| Cụm công nghiệp (thành lập, mở rộng, điều chỉnh, lựa chọn chủ đầu tư hạ tầng) | QLCN | KH-TH (đầu tư), QLNL (cấp điện), QLTM (nếu có TM), Văn phòng (tổng hợp) |
| Khu công nghiệp — **không thuộc chức năng Sở** (QĐ 3628/QĐ-UBND, TT 50/2026/TT-BCT); Sở chỉ tham gia ý kiến quy hoạch phân khu, dự án đầu tư trong KCN, KKT theo đề nghị của Ban Quản lý Khu kinh tế (ý kiến hồ sơ KCN đã thấy đi ký hiệu `/SCT-KS` — ref 03 mục C) | (BQL KKT chủ trì) | QLCN (CV Trung theo dõi), QLKS, QLNL, KH-TH |
| Địa chất, khoáng sản (cấp phép thăm dò, khai thác, tiền cấp quyền, đấu giá, đóng cửa mỏ, thiết kế mỏ, an toàn khai thác, chế biến khoáng sản, KS làm VLXD) | **Phòng QLKS** (từ 02/10/2026 theo QĐ 3628; TP Lưu Đức Cường, PTP Nguyễn Hồng Vân; ký hiệu `/SCT-KS`) | QLCN (VLNCN, an toàn ngành; hồ sơ đang dở trước bàn giao), QLNL (thủy điện), KH-TH |
| Thẩm định CT công nghiệp (cơ khí, luyện kim, hóa chất, chế biến) | QLCN | KH-TH (đầu tư) |
| Thẩm định thiết kế mỏ, dự án khai thác - chế biến khoáng sản | **Phòng QLKS** (trình PGĐ Thuân) | QLCN (VLNCN), KH-TH |
| Thẩm định CT năng lượng (thủy điện, điện mặt trời, lưới điện) | QLNL | KH-TH |
| Cấp GCN ATTP cơ sở SX-KD thực phẩm thuộc ngành CT | QLCN | Văn phòng (TTHC), KH-TH (báo cáo) |
| Cấp GP sử dụng/SX/KD vật liệu nổ công nghiệp | QLCN | Văn phòng (TTHC) |
| Cấp GP hoạt động điện lực | QLNL | Văn phòng (TTHC) |
| Cấp GCN đủ điều kiện kinh doanh xăng dầu, khí, rượu, thuốc lá | QLTM | Văn phòng (TTHC) |
| Khuyến công | QLCN | KH-TH (vốn), Trung tâm XTĐT-TM-HTDN |
| Xúc tiến thương mại | QLTM | KH-TH (vốn), Trung tâm XTĐT-TM-HTDN |
| Quản lý chợ, TTTM, siêu thị (về kinh doanh) | QLTM | QLCN (về ATTP) |
| Quản lý thị trường, xử lý hàng giả, gian lận TM | **Chi cục QLTT** | QLTM (phối hợp), QLCN (về ATTP) |
| Tham gia BCĐ liên ngành cấp tỉnh do Sở khác chủ trì | Văn phòng (cử cán bộ) | Phòng chuyên môn phù hợp |
| Quy hoạch tỉnh - quy hoạch ngành Công Thương | KH-TH | Tất cả phòng có liên quan |
| Báo cáo định kỳ ngành CT (tuần/tháng/quý/năm) | KH-TH | Tất cả phòng |
| Theo dõi, đôn đốc tiến độ chung của Sở | Văn phòng | KH-TH |
| Tham mưu QĐ-CT cá biệt UBND tỉnh về lĩnh vực CT | KH-TH | Phòng chuyên môn liên quan |
| Tham mưu VBQPPL của HĐND/UBND tỉnh | Văn phòng (pháp chế) | Phòng chuyên môn liên quan |
| Văn thư đến/đi, con dấu, chữ ký số | Văn phòng | - |
| CCHC, kiểm soát TTHC, một cửa | Văn phòng | Phòng chuyên môn (TTHC chuyên ngành) |
| KHCN-ĐMST-CĐS ngành Công Thương | KH-TH | QLCN (CN), QLNL (NL), QLTM (TM) |
| KHCN-ĐMST lĩnh vực công nghiệp | QLCN | KH-TH |
| Hội nhập KTQT, FTA | QLTM | KH-TH |
| BVMT, công nghiệp môi trường ngành CT | QLCN | - |
| Tiền chất ma túy lĩnh vực CT, tiền chất thuốc nổ | QLCN | - |
| An toàn đập hồ chứa thủy điện | QLNL | QLCN (PCTT-TKCN chung) |
| Phòng chống thiên tai, TKCN ngành CT | QLCN (thường trực) | QLNL (thủy điện) |
| Tiếp công dân, KNTC, PCTN | Văn phòng (thường trực) | Phòng chuyên môn nếu có vụ việc |
| Bảo vệ bí mật nhà nước | Văn phòng | Tất cả phòng |
| KH Công Thương trong các trạng thái QP | Văn phòng | KH-TH, QLNL (điện), QLCN (CN), QLTM (TM) |

## Quy tắc khi soạn văn bản nội bộ phân công

1. **Đầu mục Kính gửi**: "Trưởng các phòng chuyên môn, đơn vị thuộc Sở" (gọi chung); hoặc gọi đích danh khi văn bản chỉ giao 1-2 phòng.
2. **Cấu trúc phân công**: dùng a), b), c)... để gán phòng cụ thể. Mỗi phòng có 1 đoạn riêng, ghi rõ "(chủ trì)" hoặc "(phối hợp)" nếu có nhiều phòng cùng làm.
3. **Đối với Chi cục QLTT**: KHÔNG gộp với các phòng chuyên môn của Sở. Khi cần giao Chi cục QLTT, dùng mệnh đề "Chi cục Quản lý thị trường tỉnh chủ động..." và đặt mục riêng.
4. **Báo cáo - tổng hợp**:
   - Các phòng → Văn phòng Sở (đầu mối tổng hợp).
   - Văn phòng Sở → Sở chủ trì cấp tỉnh / UBND tỉnh / Bộ Công Thương.
   - Hạn báo cáo nội bộ thường trước hạn ngoài 2-3 ngày để Văn phòng tổng hợp.
5. **Người ký** (đối chiếu mục "Phân công Ban Giám đốc" — QĐ 7750/QĐ-SCT ngày 17/11/2026):
   - Văn bản chuyên môn thường lệ (cấp phép, thẩm định, công văn tham gia ý kiến, báo cáo chuyên đề): **KT.GĐ - PGĐ phụ trách lĩnh vực**:
     - ATTP, CN tiêu dùng/thực phẩm/hỗ trợ, cơ khí, khuyến công, CCN, PCTT (và dự kiến KCN, chất lượng SP, an toàn ngành khác — QĐ 7750 không ghi đích danh) → **Nguyễn Đình Chiến**.
     - **Hóa chất, VLNCN, tiền chất** (từ 17/11/2026), **HHNH, PCCC** (Bạn chốt 25/11/2026), thẩm định - KTCTNT công trình công nghiệp (trừ dự án năng lượng), khai thác, chế biến khoáng sản, luyện kim, thiết kế mỏ, CN môi trường/BVMT, ATVSLĐ → **Hoàng Văn Thuân**; địa chất, cấp phép, thăm dò, trữ lượng, đóng cửa mỏ, tiền cấp quyền, đấu giá khoáng sản, KS làm VLXD → **Phạm Năng Chung**.
     - Điện - năng lượng - thủy điện → **Nguyễn Trường Giang**; thương mại nội địa, BVQLNTD, cạnh tranh, đa cấp → **Trịnh Văn Thành**; XNK, TM biên giới, XTTM, TMĐT, logistics, phòng vệ TM → **Nguyễn Huy Tưởng**.
   - **Tờ trình, kế hoạch, quy hoạch, chủ trương đầu tư, văn bản giao nhiệm vụ trọng tâm**: **GIÁM ĐỐC** (Hoàng Chí Hiền) — kể cả nội dung KCN/CCN.
   - Khi PGĐ phụ trách vắng: việc của Chiến → KT.GĐ Nguyễn Trường Giang; việc của Thuân → Phạm Năng Chung (và ngược lại).
6. **Các phòng "thường trực"**:
   - Văn phòng: PCTN, tiếp công dân, KNTC, kiểm tra chuyên ngành tổng hợp, theo dõi tiến độ.
   - QLCN: PCTT-TKCN ngành Công Thương, an toàn PCCC chuyên ngành.
   - QLTM: BCĐ Hội nhập quốc tế của tỉnh.

## Sai lầm thường gặp — KHÔNG LÀM

- ❌ Giao cụm công nghiệp cho Phòng QLNL hoặc Phòng KH-TH — đúng là **Phòng QLCN** (mục 2.6 khoản 2 Điều 5 QĐ 6226/QĐ-SCT).
- ❌ Giao ATTP cho Phòng QLTM — đúng là **Phòng QLCN** (vì ATTP thuộc CN thực phẩm). QLTM chỉ quản lý chợ-TTTM-siêu thị về mặt kinh doanh, không quản lý ATTP của các cơ sở đó.
- ❌ Giao quản lý thị trường (chống hàng giả) cho Phòng QLTM — đúng là **Chi cục QLTT** chủ trì, QLTM chỉ phối hợp.
- ❌ Giao xăng dầu (cấp GCN đủ điều kiện KD) cho Phòng QLCN — đúng là **Phòng QLTM** (vì xăng dầu là hàng hóa KD có điều kiện trong thị trường trong nước). QLCN chỉ quản lý an toàn xăng dầu (bồn chứa, vận chuyển), không quản lý KD.
- ❌ Giao an toàn đập hồ chứa thủy điện cho Phòng QLCN — đúng là **Phòng QLNL** (mục 2.4 khoản 2 Điều 7 QĐ 6226/QĐ-SCT).
- ❌ Giao thẩm định công trình điện (lưới điện, NMĐ) cho Phòng QLCN — đúng là **Phòng QLNL** (điểm l mục 2.3 khoản 2 Điều 7 QĐ 6226/QĐ-SCT).
- ❌ Coi Chi cục QLTT là "phòng" của Sở — Chi cục là **tổ chức hành chính độc lập trực thuộc Sở**, có lãnh đạo - các phòng - các Đội QLTT riêng.
- ❌ Ghi "Phòng Thanh tra Sở", "Phòng Tổ chức cán bộ" trong văn bản — các phòng này **không còn tồn tại** sau hợp nhất; mọi nhiệm vụ chuyển về Văn phòng Sở.
- ❌ Trình **Tờ trình / kế hoạch / quy hoạch / chủ trương đầu tư** lên PGĐ ký KT.GĐ — các loại này phải trình **Giám đốc Hoàng Chí Hiền** (kể cả nội dung KCN/CCN).
- ❌ Dẫn **QĐ 05/2025/QĐ-UBND** làm căn cứ chức năng Sở trong văn bản ký từ 02/10/2026 — phải dẫn **QĐ 3628/QĐ-UBND ngày 02/10/2026**; văn bản ký trước ngày đó giữ nguyên lịch sử (máy kiểm: rule `qd-05-2025-da-thay-bang-qd-3628` của `check_facts.py`).
- ❌ Ghi Sở có **05 phòng** hoặc BGĐ **05 PGĐ** trong văn bản từ 02/10/2026 — Sở có **06 phòng** (thêm Phòng Quản lý khoáng sản, khoản 2 Điều 3 QĐ 3628), BGĐ **01 GĐ + 06 PGĐ** (thêm Phạm Năng Chung từ 01/10/2026, QĐ 3589/QĐ-UBND).
- ❌ Viết Sở Công Thương **quản lý nhà nước về khu công nghiệp** — **QĐ 3628/QĐ-UBND và TT 50/2026/TT-BCT không giao** Sở lĩnh vực KCN (Điều 1 Quy định chỉ có cụm công nghiệp). NQ 66.25/2026/NQ-CP chuyển KCN cấp Bộ về Bộ Công Thương (NĐ 351/2026 khoản 12 Điều 2) và để cấp tỉnh "theo QĐ phân công của UBND tỉnh" — UBND tỉnh đã phân công tại QĐ 3628 (văn bản mới hơn, 02/10/2026) mà không có KCN, nên mục NQ 66.25 dưới đây ghi theo QĐ 3628: KCN vẫn do Ban Quản lý Khu kinh tế quản lý, Sở chỉ tham gia ý kiến theo đề nghị của Ban.
- ❌ Từ 17/11/2026 trình hồ sơ **hóa chất, VLNCN (GP sử dụng, kho, huấn luyện), tiền chất, thẩm định - KTCTNT công trình công nghiệp** lên **PGĐ Nguyễn Đình Chiến** — QĐ 7750/QĐ-SCT giao các lĩnh vực này cho **PGĐ Hoàng Văn Thuân** (05/10–16/11/2026 PGĐ Chiến ký theo QĐ 6320 — lịch sử). PCTT, CCN, ATTP, khuyến công vẫn **PGĐ Chiến**; HHNH, PCCC cũng **PGĐ Thuân** (Bạn chốt 25/11/2026); địa chất, cấp phép, tiền cấp quyền, đấu giá, đóng cửa mỏ → **PGĐ Phạm Năng Chung**.
- ❌ Dẫn QĐ 6320/QĐ-SCT (06/10/2026), QĐ 766/QĐ-SCT (12/02/2026) hay "Dự thảo Lần 4" là phân công BGĐ hiện hành — các bản này là lịch sử; hiện hành là **QĐ 7750/QĐ-SCT ngày 17/11/2026** (GĐ + 6 PGĐ).
- ❌ Coi PGĐ Thuân phụ trách Phòng QLCN hoặc Phòng Quản lý Khoáng sản — từ 17/11/2026 **PGĐ Chiến phụ trách Phòng QLCN**, **PGĐ Chung phụ trách Phòng Quản lý Khoáng sản**; PGĐ Thuân, PGĐ Tưởng chỉ đạo theo lĩnh vực (QĐ 7750 không ghi phòng riêng). Lĩnh vực của PGĐ Thuân vẫn do chuyên viên Phòng QLCN và Phòng Quản lý Khoáng sản tham mưu.
- ❌ Ghi số văn bản cho Thông báo phân công nội bộ Phòng QLCN 10/7/2026 — thông báo này **không có số**; trích dẫn theo ngày + người ký (Trưởng phòng Nguyễn Hữu Long).
- ❌ Dùng bản phân công nội bộ cũ (1 PTP, VLNCN → CV Linh, ATTP → CV Dương) cho văn bản soạn **từ 10/7/2026 trở đi** — từ ngày này: 3 PTP (Vân, Trang, Đ.M.Cường); **VLNCN → CV Khôi**; **ATTP → CV Nam**; **chất lượng SPHH → CV Dương**; khi TP vắng **PTP Vân** thường trực (không phải PTP Trang).
- ❌ Trình dự thảo lĩnh vực khoáng sản/hóa chất/thẩm định công trình lên PTP Trang hoặc PTP Đ.M.Cường kiểm duyệt — các lĩnh vực này thuộc **PTP Nguyễn Hồng Vân**. CCN, VLNCN, KHCN-ĐMST CN do **Trưởng phòng trực tiếp** chỉ đạo, không qua PTP.
- ❌ Gán hồ sơ cấp GP vận chuyển HHNH cho CV Khôi từ 15/7/2026 trở đi — Bạn đã chốt: **HHNH toàn bộ → CV Linh**; Khôi chỉ còn VLNCN/tiền chất thuốc nổ/GCN huấn luyện KTAT/KHCN-ĐMST CN. Văn bản HHNH giai đoạn 6/7–14/7/2026 giữ CV Khôi đúng lịch sử. KCN → CV Trung (đã xác nhận).

## Tiếp nhận chức năng QLNN về địa chất, khoáng sản và khu công nghiệp từ 15/9/2026 (NQ 66.25/2026/NQ-CP)

**Căn cứ:** Nghị quyết 66.25/2026/NQ-CP ngày 04/9/2026 của Chính phủ (PTT Nguyễn Văn Thắng ký; hiệu lực 15/9/2026 – 28/02/2027 theo cơ chế NQ 206/2025/QH15). Toàn văn + ma trận trước/sau: `qlks-sct-vn` reference 23; phần KCN: `kccn-sct-vn` reference 29.

| Nội dung | Trước 15/9/2026 | Từ 15/9/2026 |
|---|---|---|
| Tham mưu UBND tỉnh QLNN về địa chất, khoáng sản (Điều 8 NĐ 150/2025; Điều 25 NĐ 193/2025): quy hoạch, cấp phép thăm dò/khai thác, tiền cấp quyền, đấu giá, bảo vệ KS chưa khai thác, kiểm soát sản lượng, đóng cửa mỏ, dữ liệu, xử phạt | Sở NN&MT (khoáng sản VLXD: Sở Xây dựng) | **Sở Công Thương** (Điều 3 k2 NQ) |
| QLNN về khu công nghiệp cấp Bộ; cơ quan chuyên môn cấp tỉnh về KCN | Bộ Tài chính; Sở Tài chính | **Bộ Công Thương** (NĐ 351/2026 Điều 1, khoản 12 Điều 2); cấp tỉnh: NQ 66.25 để "theo QĐ phân công của UBND tỉnh" (Điều 2; Điều 7 k5) — **TT 50/2026/TT-BCT (15/9/2026) và QĐ 3628/QĐ-UBND (02/10/2026) KHÔNG giao Sở Công Thương**; KCN vẫn do Ban Quản lý Khu kinh tế quản lý, Sở chỉ tham gia ý kiến (bản skill trước 18/10/2026 ghi "Sở Công Thương theo QĐ phân công" — lịch sử) |
| Đất đai, thuê đất, GPMB, ĐTM, GPMT, ký quỹ phục hồi môi trường mỏ | Sở NN&MT | **Vẫn Sở NN&MT** |
| Ban Quản lý Khu kinh tế tỉnh, Ban Quản lý các KCN tỉnh | Quản lý trực tiếp KCN, KKT | **Không đổi**; báo cáo thêm Bộ Công Thương |

**Ai phụ trách trong Sở (áp dụng cho việc mới, chờ Quyết định phân công của UBND tỉnh và điều chỉnh phân công nội bộ):**
- Lãnh đạo Sở (QĐ 7750/QĐ-SCT ngày 17/11/2026): **PGĐ Phạm Năng Chung** — địa chất, khoáng sản (thăm dò, trữ lượng, cấp phép, đóng cửa mỏ, tiền cấp quyền, đấu giá, dữ liệu, KS làm VLXD), phụ trách **Phòng Quản lý Khoáng sản**; **PGĐ Hoàng Văn Thuân** — công nghiệp khai thác mỏ, chế biến khoáng sản, thẩm định thiết kế mỏ; **PGĐ Nguyễn Đình Chiến** — CCN (KCN: dự kiến, QĐ 7750 không ghi đích danh); Giám đốc Hoàng Chí Hiền ký Tờ trình UBND tỉnh về phân công, chuyển giao và biên bản bàn giao. (05/10–16/11/2026 PGĐ Thuân phụ trách Phòng Quản lý Khoáng sản theo QĐ 6320 — lịch sử.)
- Phòng chủ trì: mảng khoáng sản tiếp nhận → **Phòng Quản lý Khoáng sản** (mới, QĐ 3628/QĐ-UBND ngày 02/10/2026); đến khi bàn giao xong, Phòng QLCN (PTP Nguyễn Hồng Vân; CV Dũng, CV Nhung) vẫn xử lý việc đang dở; KCN: CV Trung (Phòng QLCN). Khối lượng cấp phép, tiền cấp quyền, hội đồng thẩm định tăng mạnh → tham mưu tiếp nhận **biên chế, nhân sự, dự toán chuyển theo nguyên trạng** (Điều 7 k3, k5c NQ).
- Văn bản do Phòng QLCN soạn: `Lưu: VT, CN(Tên).`, ký hiệu SCT-CN. Văn bản do Phòng Quản lý Khoáng sản soạn: ký hiệu **`/SCT-KS`**, dòng **`Lưu: VT, KS.`** (quan sát 7 văn bản đi ngày 09/10/2026: 6416, 6417, 6419, 6420, 6452, 6473, 6481/SCT-KS — reference `03` mục C; kể cả việc KCN như ý kiến hồ sơ KCN Minh Quân mở rộng 6481/SCT-KS).

**GATE hành văn:** từ 02/10/2026 đã có QĐ 3628/QĐ-UBND — viết thẳng "Sở Công Thương là cơ quan chuyên môn tham mưu UBND tỉnh quản lý nhà nước về địa chất, khoáng sản" (dẫn QĐ 3628 + TT 50/2026 + NQ 66.25); **không viết Sở quản lý khu công nghiệp**; cụm cũ "cơ quan chuyên môn được UBND tỉnh giao QLNN về địa chất, khoáng sản (khu công nghiệp)" chỉ đúng cho văn bản ký 15/9–01/10/2026 (lịch sử); không viết "Sở Công Thương cấp giấy phép khai thác" (thẩm quyền cấp vẫn là Chủ tịch UBND tỉnh/Bộ Công Thương — Sở thẩm định, trình). Hồ sơ tiếp nhận từ SNNMT/SXD: chuyển nguyên trạng, không tính lại thời hạn, không yêu cầu nộp lại (Điều 4 NQ).

## Công cụ số và dây chuyền dữ liệu của Phòng Quản lý công nghiệp (từ 9/2026)

| Công cụ | Địa chỉ / kho mã | Dùng để | Người vận hành |
|---|---|---|---|
| **Cổng Khu, Cụm công nghiệp Lào Cai** | https://www.congnghieplaocai.vn (repo `Trangsct/ccn-laocai`, Netlify CMS + Vercel) | Bản đồ, danh mục, chi tiết 23 CCN đã thành lập + 35 CCN quy hoạch + 20 KCN; văn bản pháp luật; chatbot Gemini | PTP Trần Trọng Trang; số liệu CCN: CV Trung |
| **CSDL VLNCN và hàng hóa nguy hiểm** | https://vlncn-laocai.vercel.app (repo `Trangsct/vlncn-laocai`; PDF ký số tại `Trangsct/vlncn-laocai-files/uploads`) | GP sử dụng VLNCN, tiền chất thuốc nổ, GCN huấn luyện, dịch vụ nổ mìn, **GP vận chuyển HHNH** (lĩnh vực riêng, báo cáo riêng); xuất **Báo cáo định kỳ** đúng Mẫu 03 PL X TT 23/2024 và khung báo cáo HHNH; nút *Cập nhật dữ liệu ngay* | PTP Trang; VLNCN: CV Khôi; HHNH: CV Linh |
| **Dây chuyền tự động 18h** | bot `ccn-laocai/bot/` trên máy PTP Trang → Data360X (csdlvb.laocai.gov.vn, Văn bản đi/đến Phòng Công nghiệp) → GitHub Actions + Gemini (đọc PDF 2 lượt, so khớp số liệu, số/ngày lấy từ trường ký số) → CSDL web → 18h40 đồng bộ sang plugin | Giấy phép mới ký tự lên trang; trường bắt buộc chắc thì tự cập nhật, chưa chắc mở PR chờ duyệt; bấm đúp `cap-nhat-ngay.bat` để chạy sớm | PTP Trang (đăng nhập Data360X khi phiên hết hạn) |
| **Bộ plugin skill-sct** | repo `Trangsct/skill-sct` (21 plugin) | Tri thức nghiệp vụ; hai plugin `sd-vlncn-sct-vn` (ref 12) và `hnh-sct-vn` (ref 20) nhận ảnh chụp CSDL trang web tự động mỗi ngày | PTP Trang |

Nguyên tắc: **trang web là nguồn sự thật về giấy phép đã cấp** (số, ngày, hạn, PDF ký số); **plugin là nguồn sự thật về quy trình, thẩm quyền, mẫu văn bản**; số liệu hiện trạng khác (khối lượng đã dùng, kho, tiến độ CCN) hỏi Bạn. Không bịa số/ngày; mọi con số trong báo cáo xuất từ trang đều kèm nguồn.

## Liên kết với các skill/plugin khác (hệ sinh thái Trangsct/skill-sct)

Skill này là **nguồn chuẩn duy nhất (single source of truth)** về nhân sự - routing của Sở. Khi các plugin nghiệp vụ dưới đây ghi tên chuyên viên/dòng Lưu khác với mục "Cơ cấu nội bộ Phòng QLCN" ở trên, **lấy skill này (bản mới nhất) làm chuẩn** và báo Bạn để đồng bộ plugin.

| Plugin nghiệp vụ | Lĩnh vực | CV chủ trì (từ 10/7/2026) | PTP kiểm duyệt | PGĐ ký thường lệ |
|---|---|---|---|---|
| **kccn-sct-vn** | CCN/KCN | CV Trung | TP Long trực tiếp (PTP Trang phối hợp) | Chiến |
| **sd-vlncn-sct-vn**, **kho-vlncn-sct-vn**, **hl-vlncn-sct-vn** | GP sử dụng VLNCN, PANM, kho, huấn luyện KTAT, tiền chất thuốc nổ | **CV Khôi** (trước 6/7/2026 là CV Linh — văn bản cũ vẫn đúng lịch sử) | TP Long trực tiếp | **Thuân** (từ 17/11/2026, QĐ 7750; 05/10–16/11/2026 Chiến — lịch sử) |
| **hnh-sct-vn** | GP vận chuyển HHNH | **CV Linh** — toàn bộ HHNH từ 15/7/2026 (giai đoạn 6/7–14/7/2026: CV Khôi) | PTP Trang | **Thuân** (Bạn chốt 25/11/2026; 05/10–24/11/2026 Chiến — lịch sử) |
| **hc-sct-vn** | Hóa chất, tiền chất | CV Loan | **PTP Vân** | **Thuân** (từ 17/11/2026, QĐ 7750; 05/10–16/11/2026 Chiến — lịch sử) |
| **tkm-sct-vn**, **xd-sct-vn** | Thẩm định thiết kế mỏ, công trình CN, KTCTNT | CV Dũng | **PTP Vân** | **Thuân** (mỏ và công trình CN khác — QĐ 7750: xây dựng chuyên ngành Công Thương; dự án năng lượng: Giang) |
| **bvmt-sct-vn** | BVMT, CN môi trường, KNK | CV M.Long | PTP Trang | Thuân (CN môi trường — QĐ 7750) |
| **quy-hoach-ct-vn** | Quy hoạch khoáng sản/điện/KCN/CCN | CV Dũng (QH khoáng sản), CV Trung (KCN/CCN) | theo lĩnh vực | GĐ (tờ trình quy hoạch) |
| **pccc-sct-vn** | PCCC ngành Công Thương | CV Linh (Trung/Cường/Dũng/Khôi phối hợp) | PTP Trang | **Thuân** (Bạn chốt 25/11/2026; 05/10–24/11/2026 Chiến — lịch sử) |
| **atvsld-sct-vn** | ATVSLĐ, máy - thiết bị nghiêm ngặt | CV Linh | PTP Trang | Thuân |
| **qlks-sct-vn** | Khoáng sản (tiếp nhận NQ 66.25) | Phòng Quản lý Khoáng sản; CV Dũng, CV Nhung | PTP Vân (việc đang dở) | Chung (phụ trách Phòng QLKS; địa chất, cấp phép, tiền cấp quyền, đấu giá, đóng cửa mỏ) / Thuân (công nghiệp khai thác mỏ, chế biến khoáng sản) |
| **vbhc-vn** | Soạn/render .docx | — lấy routing + dòng Lưu từ skill này | — | — |
| **bpb-sct-vn** | Bài phát biểu GĐ Sở | — dùng danh sách lãnh đạo + số liệu từ skill này | — | GĐ |
| **vbhc-pdf-reader-vn** | Đọc metadata PDF đến | — chạy trước khi trích dẫn văn bản đến | — | — |

## Văn bản gốc (`van-ban-goc/`)

- `2026.09.11-ND-351-2026-ND-CP.pdf` + `.txt` — **NĐ 351/2026/NĐ-CP ngày 11/9/2026** CNNV, cơ cấu Bộ Công Thương (thay NĐ 40/2025 — lịch sử). Tóm tắt: ref 04 mục A.1.
- `2026.09.13-TT-50-2026-TT-BCT.pdf` (bản quét) + `.txt` (OCR) — **TT 50/2026/TT-BCT ngày 13/9/2026** sửa TT 37/2025/TT-BCT, hiệu lực 15/9/2026. Bảng đối chiếu khoản ↔ điều: ref 04 mục A.2.
- `2026.10.02-QD-3628-QD-UBND.pdf` (3,9 MB, chỉ có trên GitHub) + `.txt` (OCR, có trong gói claude.ai) — **QĐ 3628/QĐ-UBND ngày 02/10/2026** Quy định CNNV, quyền hạn, cơ cấu tổ chức Sở (06 phòng). Tóm tắt từng điều: ref 04 mục A.3. Cả ba do Bạn cung cấp 04/10/2026, chuyển từ PR 115 ngày 18/10/2026.
- `ND-303-2025-chuc-nang-nhiem-vu-co-cau-to-chuc-bo-co-quan-ngang-bo.docx` và `.pdf` — **Nghị định số 303/2025/NĐ-CP ngày 19/11/2025** của Chính phủ quy định chức năng, nhiệm vụ, quyền hạn và cơ cấu tổ chức của bộ, cơ quan ngang bộ (Phó Thủ tướng Phạm Thị Thanh Trà ký; hiệu lực 20/11/2025; thay Nghị định 123/2016/NĐ-CP). Bạn gửi ngày 08/10/2026. **Không nhầm với Nghị định số 303/2026/NĐ-CP ngày 01/8/2026** sửa đổi Nghị định 32/2024/NĐ-CP về cụm công nghiệp (plugin `kccn-sct-vn` reference 24).
