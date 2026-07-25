# CHANGELOG
## v1.9.0 — 25/7/2026: ref 19 qua GATE tài liệu gốc, phát hiện 3 nội dung gán sai cho NQ 34

Bạn cung cấp bản gốc NQ 34-NQ/TU và Kế hoạch 134/KH-UBND. Đã GATE cả hai và **viết lại toàn bộ ref 19**.

### Định danh đã kiểm chứng

| | NQ 34-NQ/TU | KH 134/KH-UBND |
|---|---|---|
| Cơ quan | Ban Thường vụ Tỉnh ủy Lào Cai | UBND tỉnh Lào Cai |
| Số, ngày | 34-NQ/TU, 27/12/2025 | 134/KH-UBND, 26/3/2026 |
| Người ký | T/M BAN THƯỜNG VỤ — PHÓ BÍ THƯ THƯỜNG TRỰC — **Hoàng Giang** | TM. UBND — KT. CHỦ TỊCH — PHÓ CHỦ TỊCH — **Nguyễn Thế Phước** |

### 🔴 LỖI NẶNG NHẤT: 3 nội dung bản cũ GÁN SAI cho NQ 34

Bản chưng cất cũ ghi NQ 34 có các mục tiêu "đến năm 2030 cơ cấu Công nghiệp - Xây dựng chiếm **45,3% GRDP**", "tăng trưởng GRDP bình quân **từ 11%/năm** trở lên", "đưa Lào Cai trở thành **tỉnh phát triển khá** trong vùng Trung du và Miền núi phía Bắc".

Rà toàn văn 5 trang NQ 34: các cụm **"45,3", "11%", "GRDP", "phát triển khá", "Trung du" KHÔNG xuất hiện ở bất kỳ trang nào**. NQ 34 chỉ nói "tăng trưởng kinh tế trên 10% năm 2026". Ba nội dung trên nhiều khả năng thuộc **Đề án 08** (được NQ 34 dẫn chiếu) hoặc NQ Đại hội Đảng bộ tỉnh. **Đã loại khỏi ref 19** kèm cảnh báo tuyệt đối không viện dẫn cùng NQ 34.

### 🔴 BẪY ĐỌC FILE: số và ngày KH 134 bị nuốt khi render

Khi nạp PDF Kế hoạch vào context, dòng số/ngày hiển thị **trống** ("Số: /KH-UBND ... ngày tháng 3 năm 2026"). Đọc từ đĩa bằng `pdftotext -layout` và `extract_metadata.py` cho ra đầy đủ **"Số: 134/KH-UBND — Lào Cai, ngày 26 tháng 3 năm 2026"**. Đúng kịch bản mà `vbhc-pdf-reader-vn` sinh ra để chặn. Tên file ghi "trình ký ngày 24/3/2026" là ngày trình ký, KHÔNG phải ngày ban hành. Đã ghi cảnh báo vào ref 19 mục I và mục sai lầm.

### 🔴 CỜ ĐỎ trong chính bản gốc KH 134

KH ban hành 26/3/2026 nhưng viện dẫn *"Quyết định số 1955/QĐ-UBND **ngày 19/6/2026**; hiện đang triển khai"* — sau ngày ban hành 3 tháng. Nghi lỗi đánh máy (có thể là 19/6/2025). Ref 19 ghi cờ đỏ: không viện dẫn QĐ 1955 kèm ngày này cho tới khi tra được bản gốc.

### Bổ sung nội dung bản cũ thiếu

- **07 mục tiêu 2026 của NQ 34 đầy đủ** — bản cũ thiếu hẳn chỉ tiêu (1) *06 KCN + 20 CCN đang hoạt động* và (6) *tỷ lệ lấp đầy KCN trên 70%, CCN 60-70%*; nay có đủ, kèm tên 02 KCN (Bản Qua, Võ Lao) và 05 CCN (Bảo Minh, Bảo Hưng 2, An Thịnh, Bản Phung, Yên Hợp giai đoạn II).
- **Vốn đầu tư KH 134:** khái toán **7.080 tỷ đồng** = NSNN 1.280 tỷ + doanh nghiệp 5.800 tỷ, kèm chi tiết 285 tỷ hạ tầng KCN (Tằng Loỏng 70, phía Nam 70, Minh Quân 68, Âu Lâu 77 — QĐ 1902/QĐ-UBND 16/6/2025 và QĐ 2339/QĐ-UBND 12/12/2025), 447 tỷ CCN (VB 1289/UBND-TH 23/02/2026), 3 dự án đường kết nối.
- **10 đầu mối tổ chức thực hiện**, trong đó **Sở Công Thương là CƠ QUAN THƯỜNG TRỰC**.
- **Hai mốc báo cáo khác nhau:** trước ngày **20** hằng tháng các sở gửi SCT (KH 134); trước ngày **25** hằng tháng UBND tỉnh báo cáo BTV Tỉnh ủy qua VP Tỉnh ủy (NQ 34).
- Di dời CCN Đầm Hồng (UBND phường Yên Bái chủ trì, phê duyệt phương án trong 2026); danh sách CCN mở rộng; Tằng Loỏng gắn di dời trên 400 hộ dân.

### Lưu ý nghiệp vụ mới ghi vào ref 19

- **"Yên Hợp giai đoạn II"** trong NQ 34 không khớp hồ sơ thực tế (Yên Hợp, Yên Hợp 1, Yên Hợp 2 là dự án độc lập) — trích nguyên văn thì giữ, soạn nghiệp vụ thì dùng đúng tên theo hồ sơ.
- **CCN Bản Phung** có tên trong NQ 34 nhưng nhà đầu tư đã rút hồ sơ 7/2026 — loại khỏi bảng theo dõi tiến độ.
- Bản gốc NQ 34 đánh mục **I → III → IV, không có mục II**; trích theo số mục phải giữ đúng.
- Bản gốc KH 134 lặp tên **"Yên Thế" 02 lần** trong danh sách CCN mở rộng — giữ nguyên khi trích.

### Văn bản gốc bổ sung

`NQ-34-NQ-TU-27-12-2025.pdf` (nén 3,9 MB → 0,96 MB), `KH-134-KH-UBND-26-3-2026.pdf`, `KH-134-KH-UBND-26-3-2026-TEXT.txt` (bản text layout để tra nhanh).

`plugin.json` v1.8.0 → **v1.9.0**.

## v1.8.0 — 25/7/2026: Merge 03 reference tồn đọng từ skill cũ, có kiểm chứng bản gốc

Hoàn tất việc "cân nhắc merge đợt sau" đã ghi từ v1.0. Ba reference cuối của skill `kcn-ccn-vn` nay đã vào plugin, **đối chiếu bản gốc trước khi merge chứ không bê nguyên**.

### references/21 — NQ 26-NQ/TU (MỚI, đã qua GATE tài liệu gốc)

Đối chiếu bản scan 62 trang bằng OCR tiếng Việt 200 dpi + soi ảnh 300 dpi từng vùng số liệu.

- **Xác nhận định danh:** Số 26-NQ/TU, Tỉnh ủy Lào Cai, ngày 05/12/2025, người ký T/M TỈNH ỦY — BÍ THƯ Trịnh Việt Hùng (trang 13).
- 🔴 **SỬA LỖI OCR CỦA BẢN CŨ:** mục tiêu tổng quát ghi "tăng trưởng từ **107%** trở lên" — bản gốc là **"từ 10% trở lên"**. Bản cũ tự mâu thuẫn với chính chỉ tiêu (2) "GRDP đạt trên 10%".
- Xác nhận 28/28 chỉ tiêu khớp bản gốc, gồm chỉ tiêu (14) "72,4 tuổi / 66,5 năm" (OCR máy đọc nhầm thành %, bản cũ đúng).
- Xác nhận đoạn KCN/CCN mục 3.1 nguyên văn, trong đó **"Quy hoạch điện VIII điều chỉnh"** (OCR đọc nhầm VII).
- **BỔ SUNG phần bản cũ đã bỏ hoàn toàn:** phụ lục biểu phân công — trích được "Thành lập mới 03 khu công nghiệp: KCN Y Can, KCN Đông An, **KCN Bản Qua**, tháng 12/2026" (khớp văn bản gốc KCN Bản Qua đã có trong plugin) và dòng đầu tư hạ tầng KCN/CCN hạn 12/2026. Cột cơ quan chủ trì/phối hợp/lãnh đạo phụ trách KHÔNG chưng cất (bảng ngang, rủi ro gán sai trách nhiệm) — ghi rõ phải mở PDF gốc trang 18, 24-25.
- Cảnh báo CCN Bản Phung: NQ 26 nêu tên nhưng nhà đầu tư đã rút hồ sơ 7/2026 — giữ khi trích nguyên văn, loại khỏi bảng theo dõi tiến độ.

### references/20 — Suất vốn đầu tư QĐ 425/QĐ-BXD (MỚI, đã qua GATE tài liệu gốc)

Đọc trực tiếp file gốc QĐ 425/QĐ-BXD ngày 30/3/2026 (công bố suất vốn **năm 2025**).

- Xác nhận 4 con số của bản cũ ĐỀU ĐÚNG: KCN <100ha 9.716; 100-300ha 8.948; >300ha 8.241; CCN 5-75ha 7.611 (triệu đồng/ha). Bổ sung mã hiệu 13300.01-08, cột chi phí xây dựng/thiết bị, và 4 dòng khu đô thị.
- 🔴 **SỬA LỖI THỰC CHẤT 1:** bản cũ **gộp phạm vi KCN và CCN làm một**. QĐ 425 quy định khác nhau — với KCN "trạm xử lý" nằm trong chi phí xây dựng; với CCN thì không, chỉ có "trạm bơm chuyển bậc" và thiết bị chuyển nước thải *về* trạm xử lý. Bản cũ còn tự thêm "khu điều hành", "chi phí dự phòng" cho CCN.
- 🔴 **SỬA LỖI THỰC CHẤT 2:** bản cũ liệt kê "chi phí bồi thường, GPMB, tái định cư" là khoản **QĐ 425 không tính vào suất vốn**. Nguyên văn QĐ 425 chỉ có **đúng 03 khoản** và KHÔNG có GPMB — viện dẫn như bản cũ là gán sai văn bản.
- **BỔ SUNG điều kiện pháp lý bản cũ thiếu hẳn:** Bảng 51 chỉ dùng **khi UBND cấp tỉnh chưa công bố suất vốn riêng**, theo **NĐ 49/2026/NĐ-CP ngày 31/01/2026**. Phải kiểm tra tỉnh đã công bố chưa trước khi áp. Thêm lưu ý suất vốn là bình quân cả nước, áp theo địa giới **trước hợp nhất** (quan trọng với Lào Cai + Yên Bái).

### references/19 — Nội dung NQ 34-NQ/TU + KH 134/KH-UBND (MỚI, CHƯA qua GATE)

- Tách vai rõ với ref 17: ref 19 = **nội dung tĩnh**, ref 17 = **tiến độ động**. Đã loại bỏ toàn bộ "Kết quả Quý I/2026" của bản cũ (số liệu đã lỗi thời).
- ⚠️ **Bản gốc NQ 34 và KH 134 chưa có trong `van-ban-goc/`** — reference ghi banner cảnh báo ngay đầu file: số liệu chi tiết chưa đối chiếu bản gốc, phải kiểm trước khi trình ký. Khi có bản gốc, bổ sung và cập nhật lại.

### Phát hiện chéo: mâu thuẫn chỉ tiêu XLNT

Chỉ tiêu tỷ lệ KCN có hệ thống xử lý nước thải tập trung: **KH 134 đặt 100%**, **NQ 26 đặt 41,7%**. Hai văn bản khác phạm vi, không được trộn. Đã ghi cảnh báo chéo ở cả ref 19, ref 21 và dẫn tới ref 17 mục VII.

### Văn bản gốc bổ sung (`van-ban-goc/`)

- `NQ-26-NQ-TU-05-12-2025.pdf` — bản scan 62 trang, đã nén từ 44 MB xuống 8,7 MB (ảnh xám, cạnh dài 1400 px), kiểm chứng lại sau nén vẫn đọc sạch số/ngày/người ký.
- `NQ-26-NQ-TU-05-12-2025-OCR.txt` — bản OCR toàn văn theo trang để tra nhanh, kèm cảnh báo không dùng để viện dẫn số liệu.
- `QD-425-QD-BXD-30-3-2026-suat-von-dau-tu.docx`.

### Khác

- SKILL.md: bảng reference 18 → **21 mục**; frontmatter description thêm từ khoá suất vốn đầu tư, QĐ 425, NQ 34, KH 134, NQ 26 (1015/1024 ký tự).
- `plugin.json` v1.7.0 → **v1.8.0**, description 488/500 ký tự.
 — kccn-sct-vn

## v1.7.0 — 2026-07-23 (Nghị định 178/2026/NĐ-CP — tài sản kết cấu hạ tầng CCN)

### Thêm mới
- `references/18-nd178-2026-tai-san-kcht-ccn.md`: chưng cất toàn văn NĐ 178/2026/NĐ-CP ngày 20/5/2026 (hiệu lực 06/7/2026, 4 chương 49 điều) — nghị định khung ĐẦU TIÊN về quản lý, sử dụng, khai thác tài sản kết cấu hạ tầng CCN/KCN do Nhà nước đầu tư. Nội dung: phạm vi và 5 nhóm loại trừ (khoản 2 Đ.1 — DN vốn nhà nước, CPH, NQ 198/2025, hạ tầng có NĐ riêng); hai chế độ quản lý song song (khoản 3 Đ.1 — chế độ NĐ 186/2025 vs chế độ NĐ 178, thủ tục chuyển khoản 6 Đ.10); SCT = cơ quan quản lý chuyên ngành hạ tầng cấp tỉnh với CCN (điểm b khoản 2 Đ.2) chủ trì hồ sơ giao + có ý kiến trước khi Chủ tịch UBND tỉnh quyết định (điểm a khoản 5 Đ.47); trình tự giao Đ.10 (phân loại 5 nhóm, hồ sơ Mẫu 01B, quyết định 12 ngày làm việc, biên bản Mẫu 01); nguyên tắc Đ.7 (QP-AN, đất đai theo Luật Đất đai không theo NĐ 178, bảo hiểm); 4 phương thức khai thác (Đ.16-22); 9 hình thức xử lý (Đ.23-31); kê khai 30 ngày, báo cáo trước 28/02 - 15/3, CSDL (Đ.33-34); mốc 06/01/2027 (BCT công bố danh mục chi tiết TSKCHT CCN) và 06/7/2028 (hạn hoàn thành giao tài sản hiện có); chuyển tiếp Đ.48; lộ trình khuyến nghị 6 bước cho Phòng QLCN quý III/2026.
- `van-ban-goc/ND-178-2026-tai-san-ket-cau-ha-tang.docx`: toàn văn Nghị định 178/2026/NĐ-CP.

### Cập nhật
- `references/01-khung-phap-ly.md`: mở rộng dòng NĐ 178/2026 tại bảng D (vai trò SCT, 2 mốc thời hạn, trỏ reference 18 + văn bản gốc).
- `SKILL.md`: description bổ sung từ khóa "NĐ 178/2026 tài sản hạ tầng"; mục I thêm trigger 9 (tài sản kết cấu hạ tầng CCN); mục III thêm điểm 7 khung pháp lý; mục IV thêm dòng reference 18.
- `plugin.json`: version 1.7.0; description bổ sung NĐ 178/2026.

## v1.6.0 — 2026-07-22 (tiến độ NQ 34-NQ/TU đến 20/7/2026 + hồ sơ KCN Cam Đường)

### Thêm mới
- `references/17-tien-do-nq34-thang7-2026.md`: chưng cất 2 báo cáo tháng 7/2026 (BC Sở Công Thương gửi UBND tỉnh, số liệu chốt đến 20/7/2026, PGĐ Nguyễn Đình Chiến ký; BC Ban Quản lý Khu kinh tế gửi Sở, Trưởng ban Vương Trinh Quốc ký). Nội dung: GPMB **500,30 ha = 80,24%** KH năm 623,49 ha; mặt bằng sạch **280,33 ha = 56,06%** mục tiêu 500 ha; bảng 15 khu/cụm trọng điểm (Trấn Yên 142 ha; Khu Bản Qua 85,60 ha; Kim Thành - Bản Vược 19,50 ha; Thống Nhất 1 GPMB xong 74,97 ha + 5 ha sạch; Phú Thịnh 2: 62/75 + 3 ha; Phú Thịnh 3: 43/75 + 5 ha…); trạng thái thủ tục 10 CCN mới (Yên Hợp 2 — TTr 4213/TTr-SCT 15/7; Tân Nguyên — TTr 4290 16/7; Châu Quế — TTr 4299 17/7; Báo Đáp, Bắc Văn Yên, Đông An, Bản Phiệt 1, Phú Thịnh 6, Phú Thịnh 4, An Thịnh); tiến độ 04 KCN sau CTĐT + 02 BCĐ (PCT Nguyễn Thành Sinh, PCT Phan Trung Bá); di dời KCN Đông Phố Mới (2 dự án hạ tầng, kiểm đếm 38/39 tổ chức, TB thu hồi đất 84 hộ); Tằng Loỏng (Đề án sinh thái — VB 3413/UBND-KT 04/5, TTr 33/TTr-BQL 16/6; GPMT 493/GPMT-BNNMT; di dân ~1.300 tỷ; GTSXCN 6 tháng 14.426 tỷ = 58% KH, +20%); XLNT KCN đạt chuẩn 33,33%; 4 dự án trọng tâm (Lao Kay hoạt động từ 10/7/2026); khó khăn - kiến nghị; 5 lưu ý nghiệp vụ (phân biệt GPMB ≠ mặt bằng sạch, 2 mẫu số 80,24%/56,06%).

### Cập nhật
- `references/15`: tiêu đề cập nhật đến 22/7/2026; thêm mục V-bis — tiến độ sau chấp thuận CTĐT của 4 KCN (VB hướng dẫn 879/964/965/1052/BQL-QHXD; hợp đồng Đại Hồng Phát, ACUD, đo đạc Miền Bắc; GPMB ~100 ha Cù Hà + Phẻo) và hồ sơ **KCN Cam Đường** (196,3 ha; QH phân khu QĐ 96/QĐ-BQL 18/6/2026; NĐT đề xuất Công ty CP đầu tư Lê Premium; thẩm định BC 204 + 221/BC-BQL; ý kiến Bộ Công an CV 12783/ANKT-ANTCĐT 21/7/2026; ĐANG TRÌNH — chưa viện dẫn như KCN đã chấp thuận; mục tiêu khởi công 8/2026).
- `SKILL.md`: mục lục + trigger 8 thêm reference 17.
- Website congnghieplaocai.vn đồng bộ cùng ngày (tin 22/7/2026 + cập nhật 16 đơn vị trong ccn-data.json/unit-details.json + chatbot context, SW v66).

## v1.5.0 — 2026-07-21 (chính sách ưu đãi đầu tư trong CCN)

### Thêm mới
- `references/16-uu-dai-dau-tu-ccn.md`: chính sách ưu đãi đầu tư trong CCN theo Tài liệu Sở 21/7/2026 (thuế TNDN, tiền thuê đất, hỗ trợ hạ tầng ≤30%, danh mục xã ĐBKK/KK theo QĐ 2167/QĐ-UBND). (Ghi bổ sung hồi cứu — bản phát hành 1.5.0 thiếu entry CHANGELOG.)

## v1.4.0 — 2026-07-20 (KCN Võ Lao được chấp thuận chủ trương đầu tư)

### Thêm mới
- `references/15`: bổ sung mục V — KCN Võ Lao được chấp thuận CTĐT đồng thời chấp thuận NĐT tại **QĐ 2463/QĐ-UBND ngày 16/7/2026 của UBND tỉnh** (TM. UBND, Chủ tịch Nguyễn Tuấn Anh ký): 482,6 ha (quy hoạch GĐ1 500 ha), địa điểm **xã Võ Lao VÀ xã Tằng Loỏng**, NĐT Công ty CP đầu tư hạ tầng Châu Giang (Tổng Giám đốc Bùi Trung Hiếu), tổng vốn 5.171,344 tỷ đồng, 70 năm, 2 giai đoạn (GĐ1 200 ha hoàn thành QIII/2029; GĐ2 282,6 ha sau 2030, hoàn thành QIV/2032); căn cứ KL 301-KL/TU 03/7/2026, VB 12258/ANKT-ANTCĐT 14/7/2026 Bộ Công an, BC thẩm định 17/BC-BQL 23/01/2026 + BC bổ sung 217/BC-BQL 09/7/2026. Thêm lưu ý 6 (2 xã), lưu ý 7 (hoàn thành vượt mục tiêu 02 KCN của NQ 34-NQ/TU: 04 KCN được chấp thuận trong năm 2026).
- `van-ban-goc/QD-2463-2026-CTDT-KCN-Vo-Lao.pdf`: bản gốc đã cấp số, ký ban hành.

### Cập nhật
- Tổng số KCN đã thành lập/có QĐ chấp thuận CTĐT: 10 → **11 KCN** (07 hiện hữu + Bản Qua + Phú Xuân + Phú Xuân 1 + Võ Lao) — đồng bộ references 12, 15 và SKILL.md.
- `references/12`: chuyển Võ Lao từ bảng "chưa thành lập" sang bảng "KCN mới được chấp thuận CTĐT (04)"; ghi kép 500 ha QH / 482,6 ha chấp thuận.
- `references/14`: chú thích trạng thái CTĐT mới cho dòng Võ Lao (bảng 13 KCN thu hút đầu tư).
- `references/15`: lưu ý 1 về thẩm quyền — QĐ 2463 do UBND tỉnh ban hành (cùng nhóm QĐ 2170), khác QĐ 2336/2338 do Chủ tịch UBND tỉnh.


## v1.3.1 — 2026-07-09 (loại 02 CCN khỏi danh mục theo dõi)

### Cập nhật
- `references/13-qd525-quy-hoach-tinh.md` (mục III.1): loại vĩnh viễn **CCN Bảo Hưng** (Phường Âu Lâu, 75 ha — đã bãi bỏ QĐ thành lập tại QĐ 2100/QĐ-UBND ngày 24/10/2024) và **CCN Võ Lao** (Xã Võ Lao, 14 ha) khỏi danh mục theo dõi; mục III.1 còn 04 CCN đã thành lập (Đầm Hồng, Tây Cầu Mậu A, Đông Phố Mới, Sơn Mãn). Giữ chú thích đối chiếu: nguyên văn QĐ 525 mục III liệt kê 06 CCN đã thành lập. KHÔNG nhầm với CCN Bảo Hưng 2 (Phường Âu Lâu, 50 ha — vẫn trong quy hoạch) và KCN Võ Lao (giai đoạn 1, 500 ha — vẫn trong quy hoạch).
- Đồng bộ với file theo dõi tọa độ `Toa_do_KCN_CCN_Lao_Cai_sapxep.xlsx` (danh mục còn 22 KCN + 60 CCN).


## v1.3.0 — 2026-07-06 (cập nhật 03 KCN được chấp thuận chủ trương đầu tư)

### Thêm mới
- `references/15-kcn-chap-thuan-ctdt-2026.md`: chi tiết 03 QĐ chấp thuận CTĐT đồng thời chấp thuận NĐT — KCN Bản Qua (QĐ 2170/QĐ-UBND 23/6/2026 của UBND tỉnh, 76,39 ha, NĐT Công ty CP ĐT phát triển công nghiệp Lào Cai, GCN ĐKĐT mã 4275604886 ngày 30/6/2026); KCN Phú Xuân (QĐ 2336/QĐ-UBND 02/7/2026 của Chủ tịch UBND tỉnh, 300 ha) và KCN Phú Xuân 1 (QĐ 2338/QĐ-UBND 02/7/2026, 200 ha) — cùng NĐT Công ty CP công nghiệp Linh Linh, xã Gia Phú. Nâng tổng số KCN đã thành lập/có QĐ CTĐT lên 10. Kèm 5 lưu ý nghiệp vụ (thẩm quyền ban hành khác nhau, chênh lệch 76,39/107 ha Bản Qua, không gộp Phú Xuân + Phú Xuân 1).
- `van-ban-goc/`: bổ sung 4 file gốc đã ký: QD-2170, QD-2336, QD-2338, GCN-DKDT-KCN-Ban-Qua.

### Cập nhật
- `references/12`: tách bảng "KCN mới được chấp thuận CTĐT (03)" khỏi nhóm "chưa thành lập"; tổng 10 KCN đến 7/2026.
- `references/14`: chú thích trạng thái CTĐT mới cho 3 dòng Bản Qua, Phú Xuân, Phú Xuân 1 trong bảng 13 KCN thu hút đầu tư.
- `SKILL.md`: mục lục + trigger 8 thêm reference 15.

## v1.2.0 — 2026-07-06 (merge dữ liệu tra cứu từ skill cũ kcn-ccn-vn)

### Thêm mới
- `references/13-qd525-quy-hoach-tinh.md`: TOÀN VĂN Phụ lục II (20 KCN) + Phụ lục III (54 CCN, đủ 6 nhóm: giữ nguyên / điều chỉnh / rút / bổ sung / tiến độ / sau 2030) của QĐ 525/QĐ-UBND ngày 25/02/2026; căn cứ ban hành, mục tiêu KT-XH; đối soát số liệu 54 CCN (QĐ 525) vs 56 CCN (Báo cáo 18/6/2026) vs 52 CCN (bản docx dự thảo thiếu Châu Quế + Châu Quế Thượng); tầm nhìn 2050. Chuyển từ reference 17 của skill kcn-ccn-vn.
- `references/14-qd1382-danh-muc-thu-hut.md`: QĐ 1382/QĐ-UBND ngày 23/4/2026 — 431 danh mục thu hút đầu tư; chi tiết 13 KCN (40.044 tỷ) + 35 CCN (22.854 tỷ) kèm TMĐT, nhà đầu tư, phân 3 nhóm tiến độ; suất vốn QĐ 425/QĐ-BXD ngày 30/3/2026. Chuyển từ reference 16 của skill kcn-ccn-vn, bổ sung cảnh báo dữ liệu động (cột nhà đầu tư/tiến độ).

### Sửa lỗi nghiêm trọng (vị trí xã sai trong reference 12 cũ)
Reference 12 v1.1.0 suy tên xã từ tên KCN, SAI so với Phụ lục II QĐ 525 (bản PDF đã ký, khớp QĐ 1382):
- KCN Bản Qua: ~~Xã Bản Qua~~ → **Xã Bát Xát**
- KCN Y Can: ~~Xã Y Can~~ → **Xã Lương Thịnh, xã Quy Mông**
- KCN Đông An: ~~Xã Đông An~~ → **Xã Đông Cuông**
- KCN Thịnh Hưng: ~~Xã Thịnh Hưng~~ → **Xã Yên Bình, phường Văn Phú**
- KCN Lục Yên: ~~Xã Tân Lĩnh~~ → **Xã Lục Yên, xã Tân Lĩnh**
- KCN Cốc Mỳ - Trịnh Tường: ~~Xã Cốc Mỳ, Trịnh Tường~~ → **Xã Trịnh Tường**
- Bổ sung KCN Việt Hồng 2 (200 ha, xã Việt Hồng) bị thiếu trong bảng.
- CCN Y Can: chốt **Xã Quy Mông** (khác vị trí KCN Y Can); CCN Đông An: **Xã Đông Cuông**; CCN Bảo Hưng 2: **Phường Âu Lâu** (75→50 ha); CCN Đầm Hồng: các phường Yên Bái, Văn Phú (rút khỏi QH).

### Cập nhật
- `references/12`: chuyển thành bảng tra NHANH, trỏ sang reference 13 (toàn văn QĐ 525) và 14 (QĐ 1382); thêm quy tắc "KHÔNG suy tên xã từ tên KCN"; thêm phân biệt CCN Y Can vs KCN Y Can; cập nhật website congnghieplaocai.vn.
- `SKILL.md`: mục lục thêm reference 13, 14; trigger 8 mở rộng tra cứu quy hoạch + thu hút đầu tư; nguyên tắc bất biến 4 và 6 cập nhật; description thêm từ khóa "QĐ 525 quy hoạch tỉnh, QĐ 1382 danh mục thu hút đầu tư".

### Không merge (chủ đích)
- Reference 15, 18 (hiện trạng lấp đầy/tiến độ theo Báo cáo 18/6/2026) và các bảng lấp đầy trong reference 12 skill cũ: giữ nguyên tắc plugin "hiện trạng là số liệu tĩnh — HỎI Bạn", tránh dùng số liệu lỗi thời khi soạn văn bản.
- Reference 11 (NQ 34/KH 134), 13 (suất vốn chi tiết), 14 (NQ 26) skill cũ: cân nhắc merge đợt sau nếu cần.
  **[Cập nhật 25/7/2026]** Thư mục `kcn-ccn-vn/` đã được XOÁ khỏi nhánh main (xem CHANGELOG gốc repo). Ba reference tồn đọng nêu trên vẫn nằm nguyên trong lịch sử git, lấy lại bằng:
  ```bash
  git show 07dd33e:kcn-ccn-vn/references/11-nq34-kh134.md        > /tmp/11-nq34-kh134.md
  git show 07dd33e:kcn-ccn-vn/references/13-suat-von-dau-tu.md   > /tmp/13-suat-von-dau-tu.md
  git show 07dd33e:kcn-ccn-vn/references/14-nq26-nhiem-vu-2026.md > /tmp/14-nq26.md
  git show 07dd33e --stat        # xem toàn bộ 23 file bản cũ
  ```
  ⚠️ Khi merge lại phải RÀ SỐ LIỆU TRƯỚC: bảng suất vốn ref 13 cũ lập theo **QĐ 409/QĐ-BXD (2025)**, đã có **QĐ 425/QĐ-BXD ngày 30/3/2026** thay thế (xem ref 07 mục suất vốn). Ref 14 (NQ 26) là bản OCR, mọi số liệu chỉ tiêu phải đối chiếu bản gốc.

## v1.1.0 — 2026-07-05
- Sửa lỗi nghiêm trọng quy trình Điều 10 NĐ 32/2024; bổ sung bài học thực tế KCN Phú Xuân, CCN Tân Nguyên, Minh Quân, Y Can.

## v1.0.0 — 2026-07
- Phát hành lần đầu: 12 references, 3 checklists, 7 bộ mẫu văn bản, văn bản gốc, ví dụ thực tế.
