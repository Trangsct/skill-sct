# Reference 17 — Tính giá trị sản xuất, tăng trưởng kinh tế tỉnh từ số liệu rà soát SXKD quý IV/2026 và dữ liệu nền 2025

**Nạp ngày 03/11/2026** từ 05 tệp Bạn gửi. Ba nhóm dữ liệu, đều đã ĐƯA VÀO PLUGIN dạng máy đọc (kho công khai → đã ẩn danh hộ kinh doanh, họ tên cá nhân, số điện thoại; bản gốc không chép vào kho):

| Nhóm | Nguồn | Dữ liệu trong plugin |
|---|---|---|
| **A. Rà soát SXKD, đầu tư, xây dựng quý IV và cả năm 2026** | Báo cáo của **Sở Tài chính** gửi UBND tỉnh *Kết quả tổng hợp rà soát tình hình sản xuất, kinh doanh, đầu tư, xây dựng phục vụ đánh giá tăng trưởng quý IV và cả năm 2026 (cập nhật đến ngày 26/10/2026)* — **bản chưa có số, ngày** ("Số: /BC-STC", "ngày … tháng 10 năm 2026"), Giám đốc Đỗ Đức Minh; kèm Excel 03 phụ lục. Thực hiện Văn bản **10210/UBND-TH ngày 07/10/2026** của UBND tỉnh | `du-lieu/sxkd-tang-truong/2026-10-26-stc-quy-iv.json` (940 đơn vị SXKD, 595 công trình, 46 trọng điểm + bảng tổng hợp) |
| **B. Dữ liệu nền vùng Yên Bái cũ (31/5/2025)** | Bộ "YB cung cấp thông tin 31.5.2025" — Sở Công Thương Yên Bái (trước sáp nhập) cung cấp cho Sở Công Thương Lào Cai: 16 biểu công nghiệp, thủy điện, khoáng sản, KCN, CCN, thương mại | `du-lieu/nen-2025/yen-bai-31-05-2025/*.md` (17 tệp) |
| **C. Dữ liệu nền vùng Lào Cai cũ (6/2025)** | "Danh sách phụ biểu các lĩnh vực ngành" của Sở Công Thương Lào Cai (tên tệp mang mốc 03–04/6/2025): KCN, CCN, khai thác chế biến khoáng sản, thủy điện, hạ tầng thương mại | `du-lieu/nen-2025/lao-cai-phu-bieu-06-2025/*.md` (5 tệp) |

> ⚠️ **GATE viện dẫn nhóm A:** báo cáo Sở Tài chính là **bản chưa có số/ngày**. Chỉ viết "theo số liệu tổng hợp của Sở Tài chính (cập nhật đến 26/10/2026)", **không** viết "Báo cáo số … /BC-STC". Khi có bản ký thì Bạn gửi để ghi số, ngày vào đây. Nhóm B, C cũng là phụ biểu không số — ghi "số liệu Sở Công Thương Yên Bái (cũ) cung cấp 31/5/2025", "phụ biểu Sở Công Thương Lào Cai (cũ) 6/2025".

---

## I. NHÓM A — SỐ LIỆU SỞ TÀI CHÍNH TỔNG HỢP (chốt 26/10/2026) — số ĐỘNG

Đã máy cộng lại từ Excel, **khớp lời văn báo cáo** (lệnh `tinh_tang_truong.py tong-hop` tự kiểm).

### 1. Tiếp nhận, phạm vi

- 99/99 xã, phường báo cáo (95 có danh sách; 04 không có đối tượng: Liên Sơn, Lâm Thượng, A Mú Sung, Phong Dụ Thượng) + Ban QLDA ĐTXD công trình giao thông tỉnh báo cáo trực tiếp 31 dự án.
- **Ngưỡng CV 10210** (cột "Đối chiếu ngưỡng"): Công nghiệp — QIV ≥ 5 tỷ hoặc tăng thêm ≥ 2 tỷ; Nông-lâm-thủy sản — QIV ≥ 1 tỷ; công trình — TMĐT ≥ 5 tỷ và QIV ≥ 2 tỷ, hoặc giải ngân QIV ≥ 5 tỷ. Đơn vị dưới ngưỡng xã vẫn đưa vào được gắn "[Bổ sung đặc thù]".
- Đơn vị tính thống nhất **tỷ đồng**; Sở Tài chính đã loại trùng giữa các xã.

### 2. Bảng tổng hợp (tỷ đồng)

| Khu vực | Số đơn vị | DN | HTX | Hộ KD | Khác | 9 tháng | Ước QIV | Ước cả năm | Tỷ trọng QIV |
|---|---|---|---|---|---|---|---|---|---|
| Công nghiệp - khai khoáng - năng lượng | 202 (+02 công trình) | 166 | 27 | 9 | — | 19.035,37 | **7.358,80** (đơn vị 7.345,92 + công trình 12,88) | 27.400,33 | 33,1% |
| Xây dựng | 91 (+593 công trình) | 82 | 1 | 2 | 6 tổ đội | 4.190,28 | **4.833,24** (công trình 3.179,57 + đơn vị 1.653,67) | 5.835,37 (đơn vị) | 21,7% |
| Nông, lâm nghiệp, thủy sản | 46 | 19 | 25 | 2 | — | 758,84 | **244,04** | 1.021,87 | 1,1% |
| Thương mại, dịch vụ | 601 | 411 | 16 | 172 | 2 ĐVSN | 27.469,99 | **9.817,07** | 37.622,21 | 44,1% |
| **Cộng** | **940 đơn vị + 595 công trình** | 678 | 69 | 185 | 8 | 51.454,48 | **22.253,14** (SXKD 19.060,69 + công trình 3.192,45) | 71.879,79 (SXKD) | 100% |

- Phụ lục 02 (595 công trình): TMĐT 24.070,44; thực hiện đến 30/9: 7.272,46; QIV 3.192,45 (T10 713,19 · T11 1.013,30 · T12 1.404,83); lũy kế năm 8.763,86; nghiệm thu/thanh toán 6.688,08. Đầu tư công 580 công trình (QIV 2.525,58), ngoài ngân sách - FDI 14 (665,37), nhà ở dân cư 1 (1,50).
- **10 DN lớn nhất** đạt 5.700,72 tỷ QIV = 29,9% khu vực SXKD: Luyện đồng Lào Cai - VIMICO **1.826**; mỏ tuyển đồng Sin Quyền **930**; Đồng Tả Phời - Vinacomin **638,58**; Apatit Việt Nam **614,19** (4 đơn vị đầu = 4.008,77 tỷ).
- **Tăng thêm QIV so cùng kỳ có căn cứ: 300,04 tỷ** từ 86 đơn vị (công nghiệp 197,32 tỷ — riêng Nậm Trung Hồ +127,03 do nhà máy thủy điện Nậm Trung Hồ 1 mới).
- Vướng mắc: 145 đơn vị/công trình (50 SXKD, 63 công trình, 32/46 trọng điểm). Nhóm: GPMB, đất đai 53 lượt (38 công trình; Ban QLDA giao thông 23/31 dự án); chi phí, vật liệu, vận chuyển 37; thủ tục, cơ chế, giấy phép 31; sản xuất đình trệ 19; thời tiết, thủy văn 15 (thủy điện thiếu nước); thị trường 12; vốn 11. Ngành Công Thương liên quan trực tiếp: **thủy điện không đủ nước phát theo công suất thiết kế** (Văn Chấn QIV giảm 6,57 tỷ do mưa thấp); **mỏ đá không được cấp phép sử dụng VLNCN 01/7/2025 – 30/9/2026** (Công ty TNHH Đại Đồng Tiến, xã Văn Chấn — xem `sd-vlncn-sct-vn`); mỏ đá khai thác hết công suất (DNTN Thành Hương - Nghĩa Lộ, QIV giảm 19,23 tỷ).
- Kiến nghị của Sở Tài chính: xã cập nhật **trước ngày 15 hằng tháng**; **Sở Công Thương** cùng các sở, hai Ban quản lý phối hợp rà soát, đối chiếu, hoàn thiện số liệu, hạn chế sai lệch, trùng lặp; Thống kê tỉnh tổng hợp, đánh giá tăng trưởng QIV theo ngành.

### 3. ⚠️ Điều PHẢI biết trước khi dùng số nhóm A cho công nghiệp

1. **Không phải GTSXCN.** Cột số là doanh thu hoặc giá trị sản xuất **giá hiện hành** do xã ghi (có xã lấy doanh thu kê khai thuế ÷ 3 cho từng tháng). GTSXCN chính thức của Thống kê tỉnh tính theo phương pháp khác và có bản giá so sánh 2010 (reference `04` mục II).
2. **Độ phủ chỉ khoảng 1/3.** 202 đơn vị công nghiệp cộng 9 tháng 19.035,37 tỷ ≈ **33,6%** GTSXCN 9 tháng của tỉnh (56.678 tỷ, reference `12`). Lý do: danh sách do **xã, phường** lập → **vắng 20/37 DN công nghiệp** UBND tỉnh giao Sở theo dõi (CV 10349, reference `15`), gồm gần hết khối hóa chất - phân bón - luyện kim trong KCN Tằng Loỏng (Đức Giang, DAP số 2, các nhà máy phốt pho, Supe lân Apromaco, LatViTa, Đông Nam Á), gang thép Việt Trung, xi măng Yên Bình, xi măng và khoáng sản Yên Bái, gỗ Thiên An, Cao Tiệp, Lâm Phong, thủy điện Thác Bà, Xuân Thiện, Vietraximex, Mường Hum. Lệnh `do-phu` in danh sách vắng mặt mới nhất.
   → Khi Sở Công Thương "phối hợp rà soát, hoàn thiện số liệu" (kiến nghị 3 của Sở Tài chính): đề nghị bổ sung các DN vắng mặt, lấy số từ báo cáo DN / Ban QL Khu kinh tế (`du-lieu/gtsxcn-kcn-kkt-2027.json`) / Ban QL các KCN — không để Thống kê dùng tổng 7.358,80 tỷ làm GTSXCN quý IV.
3. **Ngành xếp lại.** Một số đơn vị chế biến chè, nấm xã ghi nông nghiệp đã được Sở Tài chính xếp công nghiệp (ghi_chu). Plugin máy xếp tiếp ngành cấp 1 theo sản phẩm (B 24 đơn vị · C 114 · D 41 · E 7 · chưa xếp được 16 vì thiếu sản phẩm) — **cần Thống kê xác nhận** trước khi trích theo ngành.
4. **Dữ liệu bất thường đã thấy:** Apatit Tam Đỉnh hai dòng (Quặng tuyển 9 tháng 0, QIV 188,03; Quặng loại I, II 9 tháng 27,47, QIV 125,19) — QIV gấp nhiều lần 9 tháng, phải hỏi DN; Thủy điện Văn Chấn ghi ở xã Văn Chấn nhưng nhà máy ở xã Sơn Lương (nguy cơ trùng); Thủy điện Yên Hà (Phụ lục 03) không có ở Phụ lục 01, số 151,29 không ghi ĐVT; Công ty Gia Phát (sửa chữa máy móc, 199 tỷ QIV) xếp công nghiệp C 33.

### 4. Cơ cấu công nghiệp trong danh sách (máy tính, QIV, tỷ đồng)

| Nhóm sản phẩm | Số đv | QIV | Cả năm |
|---|---|---|---|
| Đồng, kim loại màu | 8 | 3.478,31 | 13.067,62 |
| Apatit, phân bón, hóa chất | 10 | 1.167,50 | 3.665,74 |
| Thủy điện, điện | 40 | 1.009,46 | 3.727,27 |
| Đá, cát, sỏi, VLXD | 29 | 395,23 | 1.535,98 |
| Gỗ, lâm sản | 38 | 353,90 | 1.180,20 |
| Quế, hồi, tinh dầu, dược liệu | 17 | 264,53 | 1.140,76 |
| Các nhóm còn lại | 60 | 676,99 | 3.082,76 |

Chạy lại bất cứ lúc nào: `python3 scripts/tinh_tang_truong.py cong-nghiep --top 15` (lọc `--nganh C`, `--xa "Bát Xát"`, `--tim "thủy điện"`).

---

## II. PHƯƠNG PHÁP TÍNH — GIÁ TRỊ SẢN XUẤT VÀ TĂNG TRƯỞNG (công cụ `scripts/tinh_tang_truong.py`)

> Mọi kết quả của công cụ là **[ƯỚC] của Phòng** — số chính thức do Thống kê tỉnh công bố (reference `04`). Tham số không có nguồn (chỉ số giá, hệ số VA/GO, tỷ trọng) thì **không tự giả định**: công cụ đòi nhập.

### 1. Ước GTSXCN cả năm từ 9 tháng (lệnh `uoc-nam`)

```
9 tháng cùng kỳ  = LK9 / (1 + g9)
QIV/2026 ước     = --q4 nhập  |  LK9 × (QIV/9 tháng của mẫu đơn vị công nghiệp Sở Tài chính = 0,3695 kỳ 26/10)
QIV/2025         = --q4-cung-ky  |  --nam-truoc − 9 tháng cùng kỳ  |  (thiếu số thật) giả định tăng cùng nhịp 9 tháng
Cả năm 2026      = LK9 + QIV/2026 ;  tốc độ = Cả năm 2026 / (9T cùng kỳ + QIV/2025) − 1
QIV cần đạt để cả năm tăng M% = (1 + M) × Cả năm 2025 − LK9
```
Ví dụ (đầu vào reference `12`: 56.678 tỷ, +9,9%; mục tiêu 13%; chưa có số QIV/2025 nên giả định cùng nhịp): QIV phải đạt **≈ 23.134 tỷ**, cao hơn mức ước từ tỷ lệ mẫu ≈ 2.190 tỷ. Có số cả năm 2025 của Thống kê thì nhập `--nam-truoc` để ra số chính xác hơn. Mẫu 37 đơn vị công nghiệp có cột tăng thêm cho QIV +29,75% — **không dùng làm tốc độ chung** (lệch về dự án mới).

### 2. Đóng góp vào tăng trưởng GRDP (lệnh `dong-gop`)

```
Điểm % đóng góp của khu vực i = Tỷ trọng VA khu vực i kỳ gốc (giá so sánh) × Tốc độ tăng VA khu vực i / 100
Tăng trưởng GRDP ≈ Σ điểm % đóng góp (kể cả thuế sản phẩm trừ trợ cấp)
Tốc độ khu vực CN-XD cần đạt = (Mục tiêu GRDP − Σ đóng góp các khu vực khác) / Tỷ trọng CN-XD × 100
```
Tỷ trọng phải là **cơ cấu kỳ gốc giá so sánh** của Thống kê; reference `12` chỉ có cơ cấu **giá hiện hành 9 tháng** (37,58% / 14,57% / 40,57% / 7,28% theo BC 998) — dùng tạm để ước nhanh thì ghi rõ. Kiểm chứng: BC 998 ghi CN-XD +10,67% đóng góp 3,60 điểm % → tỷ trọng gốc ngầm định ≈ 33,7%, khác 37,58% → minh họa vì sao không lấy cơ cấu giá hiện hành làm quyền số.

### 3. Quy đổi (lệnh `quy-doi`)

- Giá hiện hành → giá so sánh: chia chỉ số giá sản xuất công nghiệp (Thống kê).
- Giá trị sản xuất (GO) → giá trị tăng thêm (VA): nhân hệ số VA/GO của ngành (Thống kê; khác nhau rất xa giữa thủy điện, khai khoáng, luyện kim, chế biến gỗ). VA là đầu vào chỉ tiêu 4, 5 NQ 169 (reference `02`, `04` mục V).
- Từ ngày dự án mới vận hành: cộng GTSX năm ổn định × số tháng hoạt động/12 (quy tắc reference `16`).

### 4. Quy trình tháng (ghép lịch reference `05`, `15`)

| Mốc | Việc |
|---|---|
| Trước 10 | Thông tin tóm tắt DN biến động → Thống kê tỉnh, Sở Tài chính (CV 10349, ref `15`) |
| **Trước 15** | Xã gửi Sở Tài chính bản rà soát SXKD cập nhật (kiến nghị 1 của Sở Tài chính) |
| Sau khi Sở Tài chính tổng hợp | Bạn gửi Excel → `python3 scripts/nap_sxkd_stc.py <tệp.xlsx> --ky YYYY-MM-DD --ra du-lieu/sxkd-tang-truong/<ky>-stc-<ten>.json` → `tinh_tang_truong.py tong-hop`, `do-phu`, `uoc-nam` |
| Trước 20 | Báo cáo chỉ tiêu NQ 169 gửi Sở Tài chính (ref `05`) — phần IIP, GTSXCN dùng số Thống kê; phần giải thích dùng danh sách đơn vị |

---

## III. NHÓM B — DỮ LIỆU NỀN VÙNG YÊN BÁI CŨ (31/5/2025) — số tĩnh, làm gốc so sánh

### 1. Chuỗi chỉ tiêu công nghiệp - thương mại 2020–2025 (`tinh_tang_truong.py nen-2025`)

| Chỉ tiêu | MT NQ 2025 | 2020 | 2021 | 2022 | 2023 | 2024 | 6T 2025 | Ước 2025 |
|---|---|---|---|---|---|---|---|---|
| GTSXCN giá SS 2010 (tỷ đồng) | 20.000 | 13.000 | 14.210 | 15.540 | 16.920 | 18.480 | 10.050 | **21.300** |
| IIP tăng (%) | 9 | 8,12 | 9,12 | 9,23 | 7 ⚠️ | 9,23 | 10,5 | 9,25 ⚠️ |
| Bán lẻ + DV tiêu dùng (tỷ đồng) | 30.000 | — | 21.176 | 23.815,3 | 25.850 | 30.105,7 | 16.895,5 | 34.500 |
| Xuất khẩu (triệu USD) | 500 | — | 226,3 | 297,3 | 350 | 425,5 | 250,2 | 520 |

⚠️ Hai biểu cùng bộ ghi khác: IIP 2023 là 7% (phụ lục 01) và 6,62% (phụ lục 1 các chỉ số); IIP ước 2025 là 9,25% và 9,5%. GTSXCN 2020→ước 2025 tăng bình quân **10,38%/năm** (máy tính). Cơ cấu nội ngành ước 2025: khai khoáng 5,6% · CBCT 80,12% · điện 13,68% · nước, rác 0,6%. Kịch bản 2025 của Yên Bái cũ: phương án 8,2% → GTSXCN 20.000 tỷ; phương án 10,5% → 21.300 tỷ.

### 2. Mục lục tệp (`du-lieu/nen-2025/yen-bai-31-05-2025/`)

| Tệp | Nội dung chính |
|---|---|
| `phu-luc-01-tong-hop-ket-qua-thuc-hien-5-nam-2021-2025-…md` | Bảng trên + KCN (đến 31/12/2023), CCN 15 cụm 773,78 ha lấp đầy 34,13% |
| `phu-luc-02-cac-dn-sxcn-tren-dia-ban-den-30-5-2025-…md` | **Năng lực sản xuất theo sản phẩm** (công suất, sản lượng 2020, dự kiến 2025, tình hình): giấy đế - vàng mã - bột giấy; may (24.900 nghìn sp); tinh dầu quế (1.165 tấn); điện (708,8 MW; thủy điện đã phát 366,7 MW); tinh bột sắn (66.000 tấn); nước máy, dược; xi măng (1,26 triệu tấn công suất), gạch, sứ; chè (1.241 tấn búp tươi/ngày) — dùng làm gốc khi ước GTSX năm ổn định |
| `khu-cong-nghiep.md` | 03 KCN đến 30/5/2025: **Phía Nam** 400 ha, 66 dự án, 11.056 tỷ, lấp đầy 86,57% · **Minh Quân** 107,887 ha, 16 dự án, 2.219 tỷ, 91,16% · **Âu Lâu** 118,35 ha, 11 dự án, 1.842 tỷ, 81,23% · Trấn Yên 254,59 ha (Viglacera, GPMB); nhóm dự án: 43 đang sản xuất, 14 đang xây dựng, 24 hoàn thiện thủ tục, 12 chưa triển khai; **18 dự án FDI** 2.805,48 tỷ (116,25 triệu USD), doanh thu, XNK, lao động, nộp NSNN từng dự án; danh sách chi tiết dự án 3 KCN |
| `cum-cong-nghiep.md` | Dự án sản xuất trong từng CCN; tổng hợp CCN ước đến 31/12/2025 (Âu Lâu 96,66%, Đầm Hồng 100%, Bắc Văn Yên 96,65%…); quy hoạch CCN 2021–2030 |
| `tong-hop-du-an-cap-moi-nam-2024-…md`, `…-2025-…md` | Dự án được cấp mới QĐ chủ trương / GCN ĐKĐT 2024 và quý I/2025, chia theo ngành (CBCT nông lâm, khai khoáng, VLXD, điện, công nghiệp khác) |
| `phu-luc-03-thuy-dien-dien-luoi.md` | Phụ lục chỉ số Nghị quyết (bảng trên, lấp đầy KCN/CCN, điện nông thôn 98,36% hộ); **33 thủy điện đã phát điện 599,5 MW, 05 đang thi công 67 MW**; thủy điện phát điện 2021–2025; lưới điện 110–500 kV |
| `cac-du-an-thuy-dien-co-trong-qhd-viii-dieu-chinh-…md` | QHĐ VIII điều chỉnh: 41 dự án vận hành 2021–2030 (501,1 MW), 2031–2035 (209 MW), thủy điện lớn (190 MW) |
| `danh-sach-cac-mo-khoang-san-tren-dia-ban-tinh.md` | Giấy phép thăm dò (bảng 73 dòng) và khai thác (bảng 146 dòng, kể cả dòng tiêu đề) — đơn vị, mỏ, loại khoáng sản, số GP, ngày cấp, hết hạn, công suất, hiện trạng, tồn tại |
| Thương mại: `bieu-nam-tinh-hinh-dau-tu-cho-…`, `bieu-mau-sieu-thi-tttm`, `danh-sach-130-ch-xang-dau-2025`, `ds-thuong-nhan-mua-ban-khi-…`, `danh-sach-cua-hang-ban-le-lpg-…-tom-tat` (510 cửa hàng, chỉ số đếm), `danh-sach-cua-hang-tong-hop-…`, `danh-sach-dn-ban-buon-ruou-thuoc-la-…`, `danh-sach-theo-doi-cap-phep-ban-hang-da-cap-…` | Hạ tầng thương mại (chợ, TTTM, siêu thị, xăng dầu, LPG, rượu - thuốc lá, đa cấp) — đầu vào chỉ tiêu 6 bán lẻ; nghiệp vụ thuộc Phòng QLTM |

## IV. NHÓM C — DỮ LIỆU NỀN VÙNG LÀO CAI CŨ (6/2025)

| Tệp (`du-lieu/nen-2025/lao-cai-phu-bieu-06-2025/`) | Nội dung chính |
|---|---|
| `phu-luc-cac-khu-cong-nghiep-tren-dia-ban-tinh-lao-cai.md` | Dự án từng KCN: **Bắc Duyên Hải** 63 dự án đang SXKD (TMĐT ≈ 974,26 tỷ) · **Đông Phố Mới** 38 dự án (≈ 830,29 tỷ) · **Tằng Loỏng** 25 dự án đã sản xuất (≈ 18.210,16 tỷ; ước doanh thu 22.119,9 tỷ theo biểu quy hoạch) — tên DN, dự án, văn bản pháp lý, diện tích, lô, TMĐT |
| `quy-hoach-va-phu-luc-cac-cum-cong-nghiep-…md` | Quy hoạch KCN (3 KCN thành lập + 4 KCN mới đến 2030: Cốc Mỳ - Trịnh Tường 800 ha, Bản Qua 107, Võ Lao 200, Cam Cọn 100) và CCN (6 cụm thành lập + 13 cụm quy hoạch); cơ sở trong CCN Đông Phố Mới, Sơn Mãn, Bắc Duyên Hải, Phố Ràng, Khánh Yên Thượng (cơ sở cá nhân đã ẩn danh) |
| `phu-luc-3-khai-thac-che-bien-khoang-san-g-sua.md` | Phụ biểu 3 — dự án khai thác chế biến khoáng sản theo DN: apatit (Apatit Việt Nam, Tam Đỉnh, Vạn Thắng, Đức Giang, Hóa chất Lào Cai, Vật tư nông sản), đồng (TKV, Tả Phời), sắt, secpentin, graphit, nước khoáng nóng — diện tích, GP, công suất, hoạt động, vướng mắc, kế hoạch |
| `phu-luc-cap-nhat-qh-mr-thuy-dien-26-05-2025.md` | **130 dự án thủy điện trong quy hoạch, 1.577,55 MW** (36 dự án mở rộng): đã hoàn thành 1.169,35 MW · đã khởi công 82,8 MW · có chủ trương 90,8 MW · đang khảo sát 234,6 MW; thống kê nhà máy thủy điện nhỏ (năm vận hành, lưu vực, mực nước, công suất, sản lượng thiết kế) |
| `danh-sach-ha-tang-thuong-mai-tinh-lao-cai-sua.md` | 71 chợ (theo hạng, địa bàn), 17 chợ biên giới - KKT cửa khẩu, siêu thị, TTTM, 91 cửa hàng xăng dầu, đại lý, thương nhân đầu mối, LPG, 5 trung tâm logistics, kho > 1.000 m², bán buôn rượu, đa cấp |

⚠️ Biểu Lào Cai cũ có lỗi nhập: tỷ lệ lấp đầy KCN Bắc Duyên Hải ghi "0.72"; diện tích Tằng Loỏng ghi "1.1"; doanh thu ghi lẫn dấu phẩy/chấm. Đối chiếu `kccn-sct-vn` và reference `08`, `12` (12 KCN 3.306,18 ha toàn tỉnh mới) trước khi dùng.

---

## V. QUY TẮC KHI DÙNG REFERENCE NÀY

1. Nhóm A là **số ước, số động** — dùng cho kỳ quý IV/2026; kỳ sau nạp tệp mới bằng `nap_sxkd_stc.py`, không sửa tay JSON.
2. **Không cộng** nhóm A với `gtsxcn-kcn-kkt-2027.json`, `danh-muc-du-an.json`, `du-an-hoan-thanh-2026.json` khi chưa khử trùng theo tên DN/mã số thuế.
3. Nhóm B, C là **ảnh chụp tháng 5–6/2025, trước sáp nhập** — địa danh huyện cũ, số liệu cũ; chỉ dùng làm gốc so sánh, năng lực sản xuất, danh mục; số hiện hành tra plugin chuyên ngành (`kccn-sct-vn`, `qlks-sct-vn`, `quy-hoach-ct-vn`).
4. Văn bản gửi đi chỉ nêu tên công ty và số giấy phép nhà nước cấp; không nêu doanh thu từng DN khi văn bản công khai (thông tin kinh doanh của DN).
