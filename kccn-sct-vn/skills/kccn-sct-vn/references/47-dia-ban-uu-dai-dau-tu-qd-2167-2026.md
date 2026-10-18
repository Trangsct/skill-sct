# 47. Địa bàn ưu đãi đầu tư cấp xã tỉnh Lào Cai — QĐ 2167/QĐ-UBND ngày 23/6/2026 (thay QĐ 1894/QĐ-UBND ngày 07/11/2025); QĐ 2752/QĐ-UBND ngày 31/12/2025 (thôn, xã vùng DTTS và miền núi 2026-2030)

Soạn 08/10/2026 (PR 127, nhánh `kccn-1.50.0-dia-ban-uu-dai-qd-2167`), chuyển lên bản 1.52.0 ngày 18/10/2026. Nguồn: bản gốc Bạn gửi 08/10/2026; số, ngày, người ký đọc bằng `extract_metadata.py` (QĐ 1894, QĐ 2167 — PDF ký số) và OCR + soi ảnh (QĐ 2752 là bản scan). Dùng khi: trả lời doanh nghiệp về ưu đãi theo địa bàn (thuế TNDN, tiền thuê đất); viết phần địa bàn trong báo cáo đầu tư, báo cáo thẩm định CCN; tra một xã, phường có phải địa bàn khó khăn, đặc biệt khó khăn không.

Quan hệ với ref `46` (kỳ cập nhật 10/10/2026): ref 46 mục D đã ghi **CV 6468/SCT-CN ngày 09/10/2026** — văn bản Sở đã phát hành trả lời vụ miễn tiền thuê đất CCN Thống Nhất 1 (ba ý ngành nghề – địa bàn – thẩm quyền). Ref 47 này là **lớp văn bản gốc và danh mục tra cứu** đứng sau câu trả lời đó: chuỗi hiệu lực (mục B), danh mục 95 xã, phường nguyên văn (mục C), bảng đối chiếu nơi đặt từng KCN, CCN (mục D), QĐ 2752 (mục E) và phần hồ sơ vụ việc không có ở ref 46 (mục F). Khi soạn văn bản mới: lấy khuôn ba ý ở ref 46 mục D, lấy số liệu địa bàn ở đây.

## A. Văn bản gốc trong `van-ban-goc/`

| Tệp | Nội dung | Ghi chú |
|---|---|---|
| `QD-2167-QD-UBND-23-6-2026-cong-bo-dia-ban-uu-dai-dau-tu-cap-xa.pdf` + `.txt` | Quyết định (02 trang); bản `.txt` gồm cả Quyết định và Phụ lục | PDF ký số; pdftotext, khớp bản gốc |
| `QD-2167-QD-UBND-23-6-2026-Phu-luc-danh-muc-dia-ban.pdf` + `.txt` | Phụ lục danh mục 87 + 08 xã, phường | PDF ký số |
| `QD-1894-QD-UBND-07-11-2025-cong-bo-dia-ban-uu-dai-dau-tu.pdf` + `.txt` | Quyết định cũ (01 trang, không kèm Phụ lục) | PDF ≥ 3 MB — export-ignore, chỉ có trên GitHub; claude.ai đọc bản `.txt` |
| `QD-2752-QD-UBND-31-12-2025-thon-xa-vung-DTTS-MN-2026-2030.pdf` + `.txt` | Bản scan 63 trang (đã nén lại 120 dpi); `.txt` là OCR toàn bộ 63 trang | PDF ≥ 3 MB — chỉ có trên GitHub. OCR có thể sai ô "x" và số La Mã khu vực — soi ảnh trước khi viện dẫn |
| `QD-2752-QD-UBND-31-12-2025-Phu-luc-II-xa-khu-vuc-I-II-III.pdf` + `.txt` | Phụ lục II (06 trang, bản rõ hơn) + OCR | |

Bản `.txt` đặt **cùng tên** tệp PDF theo quy tắc sổ cái văn bản gốc (09/10/2026); tên `-TEXT.txt`/`-OCR.txt` của PR 127 không dùng nữa.

Không lưu: tệp Excel "Phụ biểu - ưu đãi đầu tư" Bạn gửi cùng ngày 08/10/2026 (bảng làm việc khi dự thảo QĐ 2167, ô số Quyết định còn trống) — không phải văn bản ban hành.

## B. Chuỗi văn bản và hiệu lực

| Văn bản | Người ký | Căn cứ chính | Nội dung | Hiệu lực |
|---|---|---|---|---|
| QĐ 1894/QĐ-UBND ngày 07/11/2025 của UBND tỉnh Lào Cai về việc công bố địa bàn ưu đãi đầu tư trên địa bàn tỉnh Lào Cai | KT. Chủ tịch — PCT Nguyễn Thế Phước | Luật Đầu tư 2020; NĐ 31/2021/NĐ-CP, NĐ 239/2025/NĐ-CP; NQ 1673/NQ-UBTVQH15; TTr 226/TTr-STC ngày 08/10/2025 | 61 xã, phường đặc biệt khó khăn; 34 xã, phường khó khăn | **Đã bị thay thế** từ 23/6/2026 (lịch sử) |
| QĐ 2167/QĐ-UBND ngày 23/6/2026 của UBND tỉnh Lào Cai về việc công bố địa bàn ưu đãi đầu tư cấp xã trên địa bàn tỉnh Lào Cai | KT. Chủ tịch — PCT Phan Trung Bá | Luật Tổ chức chính quyền địa phương 16/6/2025; Luật Đầu tư ngày 11/12/2025; NQ 76/2025/UBTVQH15; NQ 1673/NQ-UBTVQH15; **NĐ 96/2026/NĐ-CP ngày 31/3/2026** (quy định chi tiết Luật Đầu tư); **QĐ 2752/QĐ-UBND ngày 31/12/2025**; TTr 365/TTr-STC ngày 07/5/2026 | **87 xã, phường đặc biệt khó khăn; 08 xã, phường khó khăn** (Điều 1); UBND cấp xã công khai, hỗ trợ nhà đầu tư (Điều 2) | Từ ngày ký 23/6/2026; **thay thế QĐ 1894** (Điều 3) |
| QĐ 2752/QĐ-UBND ngày 31/12/2025 của UBND tỉnh Lào Cai phê duyệt danh sách thôn, xã vùng đồng bào dân tộc thiểu số và miền núi giai đoạn 2026 - 2030 trên địa bàn tỉnh Lào Cai | Chủ tịch Nguyễn Tuấn Anh | NĐ 272/2025/NĐ-CP ngày 16/10/2025 về phân định vùng đồng bào DTTS và miền núi giai đoạn 2026-2030; Thông báo 186-TB/TU ngày 30/12/2025; Kết luận 90-KL/TU ngày 31/12/2025; TTr 69/TTr-HĐTĐ ngày 28/12/2025 | 2.438 thôn vùng DTTS và miền núi (1.033 thôn đặc biệt khó khăn); 95 xã: 12 xã khu vực I, 36 xã khu vực II, 47 xã khu vực III | Từ ngày ký |

Quy tắc viện dẫn: từ 23/6/2026 chỉ dẫn QĐ 2167/QĐ-UBND; gặp văn bản (của doanh nghiệp, xã) còn dẫn QĐ 1894/QĐ-UBND thì ghi rõ "đã được thay thế bởi Quyết định số 2167/QĐ-UBND ngày 23/6/2026". **QĐ 2167 căn cứ NĐ 96/2026/NĐ-CP, không căn cứ NĐ 31/2021/NĐ-CP (sđ NĐ 239/2025) như QĐ 1894** — phần Căn cứ đọc từ bản `.txt` của QĐ 2167; tài liệu ưu đãi 21/7/2026 (ref 16) trước đây ghi nhầm căn cứ. Máy kiểm: rule `qd-1894-dia-ban-uu-dai-thay-boi-qd-2167` trong `scripts/check_facts.py` gốc kho.

## C. Danh mục theo Phụ lục QĐ 2167/QĐ-UBND (nguyên văn thứ tự)

I. Địa bàn có điều kiện kinh tế - xã hội **đặc biệt khó khăn** (87): 1 Phường Cầu Thia; 2 Phường Sa Pa; 3 Xã A Mú Sung; 4 Xã Bắc Hà; 5 Xã Bản Hồ; 6 Xã Bản Lầu; 7 Xã Bản Liền; 8 Xã Bản Xèo; 9 Xã Bảo Ái; 10 Xã Bảo Hà; 11 Xã Bảo Nhai; 12 Xã Bảo Thắng; 13 Xã Bảo Yên; 14 Xã Bát Xát; 15 Xã Cảm Nhân; 16 Xã Cao Sơn; 17 Xã Cát Thịnh; 18 Xã Chấn Thịnh; 19 Xã Châu Quế; 20 Xã Chế Tạo; 21 Xã Chiềng Ken; 22 Xã Cốc Lầu; 23 Xã Cốc San; 24 Xã Dền Sáng; 25 Xã Đông Cuông; 26 Xã Dương Quỳ; 27 Xã Gia Hội; **28 Xã Gia Phú**; 29 Xã Hạnh Phúc; 30 Xã Hợp Thành; 31 Xã Hưng Khánh; 32 Xã Khánh Hòa; 33 Xã Khánh Yên; 34 Xã Khao Mang; 35 Xã Lâm Giang; 36 Xã Lâm Thượng; 37 Xã Lao Chải; 38 Xã Liên Sơn; 39 Xã Lục Yên; 40 Xã Lùng Phình; 41 Xã Lương Thịnh; 42 Xã Mậu A; 43 Xã Minh Lương; 44 Xã Mỏ Vàng; 45 Xã Mù Cang Chải; 46 Xã Mường Bo; 47 Xã Mường Hum; 48 Xã Mường Khương; 49 Xã Mường Lai; 50 Xã Nậm Chày; 51 Xã Nậm Có; 52 Xã Nậm Xé; 53 Xã Nghĩa Đô; 54 Xã Nghĩa Tâm; 55 Xã Ngũ Chỉ Sơn; 56 Xã Pha Long; 57 Xã Phình Hồ; 58 Xã Phong Dụ Hạ; 59 Xã Phong Dụ Thượng; 60 Xã Phong Hải; 61 Xã Phúc Khánh; 62 Xã Phúc Lợi; 63 Xã Púng Luông; 64 Xã Si Ma Cai; 65 Xã Sín Chéng; 66 Xã Sơn Lương; 67 Xã Tả Củ Tỷ; 68 Xã Tả Phìn; 69 Xã Tả Van; 70 Xã Tà Xi Láng; 71 Xã Tân Hợp; 72 Xã Tân Lĩnh; 73 Xã Tằng Loỏng; 74 Xã Thác Bà; 75 Xã Thượng Bằng La; 76 Xã Thượng Hà; 77 Xã Trạm Tấu; 78 Xã Trịnh Tường; 79 Xã Tú Lệ; 80 Xã Văn Bàn; 81 Xã Văn Chấn; 82 Xã Việt Hồng; 83 Xã Võ Lao; 84 Xã Xuân Hòa; 85 Xã Xuân Quang; 86 Xã Y Tý; 87 Xã Yên Thành.

II. Địa bàn có điều kiện kinh tế - xã hội **khó khăn** (08): 1 Phường Cam Đường; 2 Phường Lào Cai; 3 Phường Nghĩa Lộ; 4 Phường Trung Tâm; 5 Xã Quy Mông; 6 Xã Trấn Yên; 7 Xã Xuân Ái; 8 Xã Yên Bình.

Không có tên trong hai danh mục (95/99 xã, phường có tên): **phường Văn Phú, phường Yên Bái, phường Nam Cường, phường Âu Lâu**. Khi nói về dự án ở 04 phường này, không viết "địa bàn khó khăn/đặc biệt khó khăn theo QĐ 2167"; ưu đãi theo địa bàn của dự án trong CCN dựa vào khoản 1 Điều 25 NĐ 32/2024/NĐ-CP (CCN là địa bàn có điều kiện KT-XH khó khăn) — cơ quan thuế, cơ quan đất đai xác định mức cụ thể.

## D. Nơi đặt KCN, CCN đối chiếu với QĐ 2167 (máy đối chiếu từ bảng ref `12`, 08/10/2026)

| KCN/CCN | Vị trí (ref 12) | Địa bàn theo QĐ 2167 |
|---|---|---|
| KCN Đông Phố Mới, KCN Bắc Duyên Hải; CCN Bắc Duyên Hải, CCN Đông Phố Mới | Phường Lào Cai | Khó khăn |
| KCN Tằng Loỏng | Xã Tằng Loỏng | Đặc biệt khó khăn |
| KCN Phía Nam | Phường Văn Phú | Không có tên |
| KCN Âu Lâu | Phường Âu Lâu, xã Quy Mông | Âu Lâu không có tên; Quy Mông khó khăn |
| KCN Trấn Yên, KCN Minh Quân; CCN Minh Quân, CCN Âu Lâu, CCN Bảo Hưng 2 | Phường Âu Lâu | Không có tên |
| KCN Bản Qua, KCN Bát Xát | Xã Bát Xát | Đặc biệt khó khăn |
| KCN Phú Xuân, KCN Phú Xuân 1, KCN Thống Nhất; CCN Thống Nhất 1, CCN Thống Nhất | Xã Gia Phú | Đặc biệt khó khăn |
| KCN Võ Lao | Xã Võ Lao, xã Tằng Loỏng | Đặc biệt khó khăn (cả hai xã) |
| KCN Cam Đường | Phường Cam Đường | Khó khăn |
| KCN Y Can | Xã Lương Thịnh, xã Quy Mông | Lương Thịnh đặc biệt khó khăn; Quy Mông khó khăn |
| CCN Y Can | Xã Quy Mông | Khó khăn |
| KCN Đông An; CCN Đông An | Xã Đông Cuông | Đặc biệt khó khăn |
| KCN Thịnh Hưng | Xã Yên Bình, phường Văn Phú | Yên Bình khó khăn; Văn Phú không có tên |
| KCN Lục Yên | Xã Lục Yên, xã Tân Lĩnh | Đặc biệt khó khăn (cả hai xã) |
| KCN Cốc Mỳ - Trịnh Tường | Xã Trịnh Tường | Đặc biệt khó khăn |
| KCN Việt Hồng 1, KCN Việt Hồng 2 | Xã Việt Hồng | Đặc biệt khó khăn |
| CCN Phú Thịnh 1, CCN Phú Thịnh 2, CCN Phú Thịnh 3, CCN Phú Thịnh 4 | Xã Yên Bình, phường Văn Phú | Yên Bình khó khăn; Văn Phú không có tên |
| CCN Phú Thịnh 5, CCN Phú Thịnh 6 | Phường Văn Phú | Không có tên |
| CCN Yên Hợp, CCN Yên Hợp 1, CCN Yên Hợp 2 | Xã Xuân Ái | Khó khăn |
| CCN Tân Nguyên, CCN Mông Sơn | Xã Bảo Ái | Đặc biệt khó khăn |
| CCN Đầm Hồng | Các phường Yên Bái, Văn Phú | Không có tên |
| CCN Châu Quế | Xã Châu Quế | Đặc biệt khó khăn |

Cụm nằm trên hai xã, phường khác nhóm: ưu đãi theo địa bàn xác định theo vị trí thửa đất của dự án — đề nghị cơ quan thuế, cơ quan đất đai xác định, không tự kết luận. Cụm chưa có trong bảng (CCN Tân Hợp — xã Tân Hợp, STT 71 Mục I; CCN Bản Phiệt 1 — phường Lào Cai, Mục II…): tra mục C theo xã, phường ở ref `12`/ref `44`.

## E. QĐ 2752/QĐ-UBND — dòng đã soi ảnh

- Xã Gia Phú (STT 34 Phụ lục II): vùng đồng bào DTTS **Đạt**; miền núi **Không đạt**; xã vùng đồng bào DTTS và miền núi **Đạt**; **khu vực II**; 42 thôn, 02 thôn đặc biệt khó khăn (ảnh trang 3 tệp Phụ lục II).
- Bốn phường Văn Phú, Yên Bái, Nam Cường, Âu Lâu (STT 1–4 Phụ lục II): "Không đạt" ở cả ba cột — trùng với việc 04 phường này không có tên trong QĐ 2167.
- Các dòng khác: tra bản `.txt` (OCR), soi ảnh trang tương ứng trong PDF trước khi viện dẫn.
- Lưu ý ranh giới: QĐ 2752 phân định **vùng DTTS và miền núi** (NĐ 272/2025) — là căn cứ để UBND tỉnh lập danh mục địa bàn ưu đãi đầu tư, **không phải** chính danh mục ưu đãi; khi viện dẫn địa bàn ưu đãi đầu tư chỉ dẫn QĐ 2167.

## F. Hồ sơ vụ việc 08/10/2026 — Văn bản 232/CV-LCIDI-HT (CCN Thống Nhất 1) — phần bổ sung cho ref 46 mục D

Văn bản Sở đã phát hành, ba ý trả lời và thể thức: **ref 46 mục D (CV 6468/SCT-CN ngày 09/10/2026)** — không chép lại ở đây. Dưới đây là những dữ kiện ref 46 không có:

**Văn bản hỏi:** số 232/CV-LCIDI-HT ngày 08/10/2026 của Công ty CP Đầu tư Phát triển Công nghiệp Lào Cai (Tổng Giám đốc Phạm Quốc Việt ký; bản scan, đọc trên ảnh) gửi UBND tỉnh, Sở Tài chính, Sở NN&MT, Sở Công Thương, "Cục Thuế tỉnh", UBND xã Gia Phú; hỏi dự án hạ tầng CCN Thống Nhất 1 có thuộc diện **miễn tiền thuê đất toàn bộ thời gian thuê** (ngành nghề đặc biệt ưu đãi + địa bàn đặc biệt khó khăn) không. Bản gốc là văn bản đến của Sở — không đưa vào kho.

**Lỗi trong văn bản của Công ty (không chép lại khi trả lời, không đưa vào văn bản của Sở):**
- dẫn "điều 139" NĐ 103/2024/NĐ-CP (đúng là Điều 39);
- NĐ 32/2024/NĐ-CP ghi ngày 13/3/2024 (đúng 15/3/2024);
- dẫn QĐ 1894/QĐ-UBND đã bị thay thế (đúng: QĐ 2167/QĐ-UBND);
- viết "Cục Thuế tỉnh" (tên dùng trong văn bản của Sở: Thuế tỉnh Lào Cai);
- dẫn "Quyết định số 636/QĐ-UBND ngày 23/4/2026" cho thuê đất giai đoạn 1. ⚠️ Cùng ngày 23/4/2026 UBND tỉnh ban hành QĐ 1382/QĐ-UBND, nên số 636 khó thuộc dãy số Quyết định của UBND tỉnh năm 2026 — có thể là quyết định của cấp khác hoặc công ty ghi nhầm số/ngày. BC 214/BC-LCIDI 29/9/2026 (ref 44) và tệp trạng thái `trang-thai/ccn-thong-nhat-1.md` đang ghi theo công ty; **chưa có bản gốc, không viện dẫn số này trong văn bản của Sở** cho đến khi Bạn đối chiếu (ghi ở mục "Vướng mắc, câu hỏi còn mở" của tệp trạng thái).

**Nguyên tắc rút ra (Nhóm A vbhc-vn — không ghép hai dữ kiện thành kết luận thay cơ quan có thẩm quyền):** Sở chỉ nêu thông tin đã ban hành thuộc lĩnh vực mình (ngành, nghề theo Điều 25 NĐ 32/2024; địa bàn theo QĐ 2167 — xã Gia Phú STT 28 Mục I); **không kết luận "được miễn toàn bộ thời gian thuê"**; đề nghị Công ty liên hệ Sở NN&MT, Thuế tỉnh Lào Cai; khi lập hồ sơ dẫn QĐ 2167. Nơi nhận văn bản trả lời đã dùng: Như trên; UBND tỉnh (báo cáo); Các Sở: Tài chính, NN&MT; Thuế tỉnh Lào Cai; UBND xã Gia Phú; Ban Giám đốc Sở; Lưu: VT, CN.

**Chưa đối chiếu bản gốc (nguồn thứ cấp, 08/10/2026):** khoản 3 Điều 39 NĐ 103/2024/NĐ-CP có mức miễn toàn bộ thời gian thuê cho dự án thuộc Danh mục ngành, nghề đặc biệt ưu đãi đầu tư đầu tư tại địa bàn đặc biệt khó khăn (chưa chốt ký hiệu điểm); theo khoản 3 Điều 157 Luật Đất đai 2024, người được miễn tiền thuê đất không phải làm thủ tục đề nghị miễn; NĐ 50/2026/NĐ-CP ngày 31/01/2026 (quy định chi tiết NQ 254/2025/QH15 về tiền sử dụng đất, tiền thuê đất) có quy định trình tự miễn, giảm. Có bản gốc thì lưu `van-ban-goc/` (hoặc plugin `dat-dai-sct-vn`) và sửa mục này.
