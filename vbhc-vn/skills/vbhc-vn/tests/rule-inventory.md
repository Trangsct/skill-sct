# Kiểm kê quy tắc soạn thảo của plugin vbhc-vn

Lập ngày 16/9/2026 theo Bản giao việc "Nâng cấp plugin vbhc-vn: chuyển quy tắc soạn thảo
sang kiểm tra bằng máy và dựng bộ kiểm thử hồi quy" (Bước 1).

Nguồn kiểm kê: `SKILL.md` (27 quy tắc bất biến + mục thể thức), `reference/phong-tranh-sai-lam.md`
(12 nhóm A–L), `reference/nd30-phu-luc-1-the-thuc.md`, `CHANGELOG.md`, docstring các script.

## Cách đọc bảng

- **Loại M** = máy kiểm được, đã hoặc sẽ có hàm kiểm.
- **Loại N** = máy KHÔNG kiểm được (nội dung pháp lý, suy diễn nhiệm vụ, giọng văn tổng thể).
  Các dòng loại N giữ nguyên văn xuôi trong SKILL.md và reference — không ép thành regex.
- **Hàm kiểm**: `qa_rules.py` = bộ quy tắc mới đợt này; các tên khác là hàm đã có từ trước,
  đợt này chỉ GẮN MÃ, không viết lại.
- **Mức**: FAIL chặn trình ký; WARN nhắc để người soạn cân nhắc.

## A. Quy tắc loại M — đã có hàm kiểm (đợt này)

| Mã | Nội dung quy tắc | Nguồn | Hàm kiểm | Mức |
|---|---|---|---|---|
| R01 | Lần đầu dẫn một số hiệu văn bản phải đủ số, ngày ban hành, cơ quan, trích yếu; lần sau mới viết gọn | Giám đốc chốt 13/9/2026; Nhóm A | `qa_rules.rule_R01` | FAIL ở vùng căn cứ / WARN ở thân |
| R02 | Công thức hóa học phải có chỉ số dưới thật (run `subscript`), không viết phẳng P2O5 | Quy tắc bất biến 25 (13/9/2026) | `qa_rules.rule_R02` | FAIL |
| R03 | Bản hoàn thiện không còn "……", "....", "[ ]", "…/…", "(nêu số liệu)", chữ tím 7030A0 | Quy tắc bất biến 27(c) (16/9/2026) | `qa_rules.rule_R03` | WARN → FAIL khi `--final` |
| R04 | Khối Kính gửi nhiều cơ quan: không in đậm, các dòng cơ quan thẳng cột | Nhóm G; Quy tắc 27(a) | `qa_rules.rule_R04` | FAIL (đậm) / WARN (thẳng cột) |
| R05 | Không viện dẫn văn bản chưa có hiệu lực tại ngày ký | Nhóm A, D (vụ NQ 66.25 ngày 11/9/2026) | `qa_rules.rule_R05` + `data/vbpl.json` (62 văn bản, 37 có ngày hiệu lực) | FAIL |
| R06 | Nơi nhận gửi doanh nghiệp: doanh nghiệp không ở dòng đầu; dòng cuối là Lưu | Nhóm G, Bạn chốt 07/9/2026 | `qa_rules.rule_R06` | FAIL |
| R07 | Dòng Lưu: ký hiệu đơn vị hợp lệ, kết thúc dấu chấm, dùng "CN" không "QLCN" | Nhóm G | `qa_rules.rule_R07` | FAIL / WARN (khoảng trắng trước ngoặc) |
| R08 | Cấm từ suy đoán trong văn bản trình ký | Nhóm C | `qa_rules.rule_R08` → `check_document.find_speculative` | WARN |
| R09 | Thuật ngữ sai theo danh sách cấm | Nhóm K5 | `qa_rules.rule_R09` + `data/thuat-ngu-cam.txt` | FAIL |
| R10 | Giọng giải thích lọt vào thân văn bản | Nhóm J (31/8/2026), Nhóm L | `qa_rules.rule_R10` + `data/giong-giai-thich.txt` | WARN |
| R11 | Dòng địa danh/ngày in nghiêng; dòng chức danh người ký viết hoa, in đậm, căn giữa | NĐ 30/2020 PL I; Nhóm H2 | `qa_rules.rule_R11` | FAIL |
| R12 | Lề trang A4 trên 2, dưới 2, trái 3, phải 2 cm | NĐ 30/2020 PL I | `qa_rules.rule_R12` | FAIL (thiếu/phi lý) / WARN (lệch chuẩn) |
| R13 | Đoạn thân lùi đầu dòng đồng đều | Quy tắc 27(b) (16/9/2026) | `qa_rules.rule_R13` | WARN |
| R14 | Không để lại dấu vết lần sửa trước; không còn comment, tracked change | Nhóm F, K7 | `qa_rules.rule_R14` | FAIL |
| R15 | Dẫn Quyết định thì không nhắc văn bản trình hình thành Quyết định đó | Nhóm K6 | `qa_rules.rule_R15` | WARN |
| R16 | Khối Kính gửi: một cơ quan thì cùng một dòng, nhiều cơ quan mới tách dòng; không để trống nơi nhận | Nhóm G, Bạn chốt 18/9/2026 | `qa_rules.rule_R16` | FAIL |

## B. Quy tắc loại M — ĐÃ CÓ hàm kiểm từ trước, đợt này chỉ gắn mã

Không viết lại (nguyên tắc IV.1 của bản giao việc). Các hàm này vẫn chạy ở mục 1, 2, 3
của `qa_all.py`, giữ nguyên tag cũ.

| Mã | Nội dung quy tắc | Nguồn | Hàm kiểm (tag trong qa_all) | Mức |
|---|---|---|---|---|
| H1 | Không mất đường Line trong header (đếm shape = mẫu gốc) | Nhóm H1, H5; Quy tắc bất biến 11 | `qa_pdf_check.check_line_shapes` (LINES) | FAIL |
| H2 | Dòng "Số:" và "Địa danh, ngày…" 13pt tường minh | Nhóm H2; Quy tắc bất biến 12 | `qa_pdf_check.check_so_ngay_13pt` (SZ13) | FAIL |
| H3 | Không widow word (1 chữ lẻ rơi dòng) | Nhóm H3; Quy tắc bất biến 13 | `qa_pdf_check.check_widow` (WIDOW) | FAIL |
| H4 | Khối chữ ký không gãy giữa 2 trang | Nhóm H4; Quy tắc bất biến 14 | `qa_pdf_check.check_sig_split` (SIGSPLIT) | FAIL |
| H12 | Không đặt `trHeight` cố định cho bảng nội dung | Nhóm H12; Quy tắc bất biến 20 | `check_document.find_fixed_row_heights` (mục [F]) | FAIL |
| H13 | Khối ký: 1 đoạn trống trước bảng ký, đủ đoạn trống trong ô ký | Quy tắc bất biến 22 (09/9/2026) | `qa_all.check_sig_block` (SIGSPACE) | FAIL |
| QT10 | Không ngắt dòng cứng `<w:br/>` trong ô header | Quy tắc bất biến 10 | `qa_all.check_header_br` (HDR-BR) | FAIL |
| QH | Quốc hiệu "CỘNG HÒA", tiêu ngữ dùng en dash | Nhóm G | `qa_all.check_quoc_hieu_tieu_ngu` (QUOCHIEU) | FAIL |
| KG | Dòng Kính gửi không in đậm (bản kiểm cũ) | Nhóm G | `qa_all.check_kinh_gui_bold` (KINHGUI) | WARN |
| ND | Văn bản pháp luật đã hết hiệu lực | Nhóm D | `check_document.find_expired_laws` | FAIL |
| CT | Nội dung bắt buộc có / bắt buộc không có | Quy tắc bất biến 17 | `qa_all.check_content_lists` (`--forbid`/`--require`) | FAIL |

## C. Quy tắc loại N — máy KHÔNG kiểm được, giữ nguyên văn xuôi

Các quy tắc dưới đây đòi hỏi đọc hiểu pháp lý hoặc phán đoán ngữ cảnh. Ép thành regex sẽ
vừa bắt nhầm mẫu thật vừa bỏ lọt lỗi thật, nên **giữ nguyên trong SKILL.md và reference**.

| Nhóm | Vì sao máy không kiểm được |
|---|---|
| A — bịa/sai nội dung pháp lý | Phải mở bản gốc mới biết điều khoản dẫn có đúng không. Máy chỉ kiểm được phần hình thức (R01) và phần hiệu lực khi đã có kho dữ kiện (R05). |
| B — tự suy diễn nhiệm vụ ngoài văn bản chỉ đạo | Quy tắc 1-1-1 đòi truy ngược mỗi nhiệm vụ về câu chỉ đạo, điều khoản hoặc chức năng của Sở. |
| E — tin context window với PDF 2 cột | Là quy tắc QUY TRÌNH (phải chạy `extract_metadata.py` trước), không phải thuộc tính của file .docx xuất ra. |
| F — rebuild file thay vì sửa file tải lên | Quy tắc quy trình; chỉ phát hiện được khi so sánh với bản người dùng tải lên. |
| I — văn phong công văn gửi doanh nghiệp | "Chỉ nêu cái chưa đủ, không nêu cái đang đúng" đòi hiểu hồ sơ. Phần cấm câu cố định đã chuyển vào R10. |
| J5 — ranh giới ngoại lệ của Nhóm J | Phân biệt "nêu bối cảnh khách quan" (được) với "dẫn dắt cảm xúc" (cấm) là việc đọc hiểu. R10 chỉ bắt được danh sách cụm cố định, nên để mức WARN. |
| K1, K2, K8 — giao việc cho cơ quan khác | Đòi tra thẩm quyền pháp định của từng ngành và cân nhịp văn bản theo chủ thể. |
| L1 — cho ý kiến phải có chính kiến | Máy đếm được số lần "nhất trí" (đã đưa vào `--forbid` của Nhóm L) nhưng không đánh giá được chính kiến có đúng không. |
| Quy tắc bất biến 6 — chọn người ký theo lĩnh vực | Phụ thuộc bảng phân công của Sở và nội dung vụ việc. |
| Quy tắc bất biến 18 — người soạn trong dòng Lưu | Máy kiểm được ĐỊNH DẠNG (R07) nhưng không biết chuyên viên nào phụ trách vụ việc. |

## D. Những chỗ quy tắc văn xuôi LỆCH với mẫu thật — cần Bạn chốt

Khi đưa quy tắc vào máy, ba quy tắc dưới đây bắt chính mẫu thật đã ban hành. Theo nguyên
tắc "mẫu thật là chuẩn", tôi đã hạ mức hoặc thu hẹp phạm vi và ghi lại ở đây để Bạn quyết.

1. **Header cơ quan chủ quản viết tắt.** Nhóm G ghi "ghi đầy đủ ỦY BAN NHÂN DÂN TỈNH LÀO CAI,
   không viết tắt UBND TỈNH LÀO CAI". Nhưng ô header chuẩn của Sở trong **22/26 mẫu thật** in
   "UBND TỈNH LÀO CAI / SỞ CÔNG THƯƠNG". Đã GỠ khỏi máy kiểm. Đề nghị Bạn chốt: quy tắc này chỉ
   áp cho thân văn bản, hay ô header cũng phải sửa?
2. **Dòng Lưu viết liền "CN(Trung)".** Nhóm G ghi Bạn đã sửa tay thành "CN (Khôi)" có khoảng
   trắng, nhưng **9/26 mẫu thật** vẫn viết liền. Đã để mức WARN. Đề nghị Bạn chốt: bắt buộc có
   khoảng trắng (nâng lên FAIL) hay chấp nhận cả hai?
3. **Lề trang.** 4/26 mẫu thật lệch chuẩn 2/2/3/2 có chủ đích (GCN ATTP dùng phôi 2,54 cm;
   Kế hoạch đề án 08 lề trên 1,50 cm; công văn nội bộ Phòng lề dưới 1,75 cm; công văn VP UBND
   lề dưới 0,75 cm). Đã hạ FAIL xuống WARN, chỉ giữ FAIL khi lề thiếu hoặc phi lý (<0,5 cm).
   Đề nghị Bạn chốt: có chuẩn hóa lại các mẫu này không?

**Cập nhật 17/9/2026 — Bạn yêu cầu tự động hóa tối đa, nên cả 4 mục đã được xử lý theo nguyên
tắc "mẫu thật là chuẩn" thay vì chờ chốt tay:**

- Mục 1 (header viết tắt): quy tắc Nhóm G "ghi đầy đủ ỦY BAN NHÂN DÂN TỈNH LÀO CAI" xếp vào
  **lịch sử** — ô header chuẩn của Sở in "UBND TỈNH LÀO CAI" ở 22/26 mẫu thật và thân văn bản
  vốn phải viết tắt UBND từ lần đầu. Không đưa vào máy kiểm. Bạn muốn khôi phục thì nói.
- Mục 2 (`CN(Trung)` viết liền): giữ WARN — máy nhắc, không chặn.
- Mục 3 (lề trang): giữ WARN, FAIL chỉ khi phi lý.
- Mục 4 (`qa_all.py` đỏ 24/26): **ĐÃ HIỆU CHỈNH 4 hàm kiểm cũ theo mẫu thật** — chi tiết ngay dưới.
  Kết quả: **26/26 mẫu thật PASS `qa_all.py`**, tiêu chí VII.1 đạt.

4. **`qa_all.py` đang FAIL 24/26 mẫu thật — nợ kỹ thuật CÓ SẴN TỪ TRƯỚC đợt 2.23.0.**
   Đo ngày 16/9/2026: chỉ `cong-van-noi-bo-phong-tham-gia-y-kien-thu-hoi-cat-long-ho.docx`
   và `phieu-trinh-giai-quyet-cong-viec.docx` PASS. Phân bố tag:
   SIGSPACE 13 file, SZ13 12 file, LINES 5 file, HDR-BR 1 file.
   Bộ quy tắc mới (mục 1b, R01–R15) đóng góp **0 FAIL** — đây là các hàm kiểm cũ chặt hơn
   mẫu thật. Riêng SZ13 đã được ghi nhận từ trước là dương tính giả trong Nhóm K10
   ("File Bạn lưu lại từ Word mất `sz` tường minh → qa_all báo SZ13 là do Word ghi lại,
   không sửa file cuối của Bạn").
   Đợt này KHÔNG sửa các hàm cũ (nguyên tắc IV.1 của bản giao việc: tái dùng, không viết lại),
   chỉ chốt hiện trạng vào `tests/baseline-qa-all.json` để nâng cấp sau không làm tệ thêm.
   Đề nghị Bạn chốt cho đợt sau: hiệu chỉnh SIGSPACE, SZ13, LINES theo mẫu thật (giống cách
   đã làm với R01, R04, R12 đợt này), hay chuẩn hóa lại 24 mẫu thật?
   ~~Đây cũng là lý do tiêu chí VII.1 chưa đạt.~~ **Đã xử lý 17/9/2026** — hiệu chỉnh theo đúng
   cách đã làm với R01/R04/R12, có file lỗi chứng minh vẫn bắt được lỗi thật:

   | Tag | Trước | Sau hiệu chỉnh | File lỗi chứng minh |
   |---|---|---|---|
   | SZ13 | FAIL khi sz ≠ 26 | FAIL khi sz đặt tường minh ra cỡ lạ (≠ 26/27/28) hoặc dòng ngày mất nghiêng; trống/27/28 → WARN (Word ghi lại làm mất sz — K10) | `sz13-dong-so-sai-co-chu.docx` (sz=20) |
   | SIGSPACE | 3 điều kiện đều FAIL | (2) ô ký ≥3 dòng trống giữ FAIL; (1) đúng 1 dòng trống trước bảng ký và (3) Nơi nhận ≤45 ký tự → WARN (13 mẫu thật có 0–2 dòng trống, Nơi nhận dài tới 78 ký tự) | `sigspace-o-ky-thieu-dong-trong.docx` |
   | LINES | FAIL khi < 2 `w:pict` | đếm cả `w:drawing`; tuyệt đối → WARN; FAIL khi `--goc <mẫu gốc>` và số shape GIẢM (đúng ý H1 "đếm shape file xuất == gốc") | `lines-mat-duong-ke-header.docx` |
   | HDR-BR | xét bảng 0 vô điều kiện | chỉ xét khi bảng 0 thật sự là header (có Quốc hiệu/Số:); phụ biểu bảng 0 là bảng số liệu | `hdrbr-ngat-dong-cung-trong-header.docx` |

## Đ. Công cụ đi kèm bộ quy tắc (bổ sung 16/9/2026)

| Công cụ | Việc | Nguồn dữ liệu |
|---|---|---|
| `scripts/qa_rules.py` | 16 quy tắc R01–R16, chạy lẻ hoặc qua `qa_all.py` mục 1b | `data/*.txt`, `data/vbpl.json` |
| `scripts/cite_check.py` | Đối chiếu mọi số hiệu trong bản thảo: KHỚP / LỆCH / CHƯA CÓ | `data/vbpl.json` |
| `scripts/build_vbpl.py` (gốc kho) | Sinh `data/vbpl.json` — **không sửa tay file JSON** | `registry/trang-thai.csv` |
| `scripts/build_vb.py` | Dựng .docx từ nội dung dạng thẻ cho 8 loại; tự làm chỉ số dưới/trên và lùi đầu dòng | mẫu thật trong `examples/` |
| `tests/tao_file_loi.py` | Sinh lại toàn bộ `tests/fail/` một cách tái lập được | mẫu thật trong `examples/` |
| `tests/run_regression.py` | Hồi quy 4 mục: mẫu thật sạch · 16 file lỗi bị bắt (kể cả tag cũ SZ13/SIGSPACE/LINES/HDR-BR) · `qa_all` PASS 26/26 · biên dịch 8 loại | — |
| `scripts/nap_vbpl_data360x.py` (gốc kho) + `vlncn-laocai/scripts/de-xuat-vbpl.py` | Nạp văn bản pháp luật CÔNG KHAI từ danh mục Data360X vào registry (số, ngày ban hành; hiệu lực để trống) | `theo-doi/danh-muc-<năm>.json` |

Muốn bổ sung một văn bản pháp luật vào kho đối chiếu: sửa `registry/trang-thai.csv` (chỉ ghi khi
đã mở bản gốc), rồi chạy `python3 scripts/build_vbpl.py` tại gốc kho và commit cùng.

## E. Quy trình từ nay khi phát hiện lỗi mới

Không thêm văn xuôi vào SKILL.md nữa. Bốn bước (chi tiết trong `HUONG_DAN_CAP_NHAT.md`):

1. Lưu file lỗi vào `tests/fail/` kèm file `.expect` cùng tên.
2. Viết hàm kiểm `rule_Rnn` trong `scripts/qa_rules.py`, đăng ký vào bảng `RULES`.
3. Chạy `python3 tests/run_regression.py` — phải xanh (mẫu thật vẫn sạch, file lỗi bị bắt).
4. Tăng version trong `.claude-plugin/plugin.json`, ghi CHANGELOG.
