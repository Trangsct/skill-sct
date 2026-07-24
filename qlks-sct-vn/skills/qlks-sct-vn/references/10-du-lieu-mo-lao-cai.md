# 10 — Dữ liệu mỏ trên địa bàn tỉnh Lào Cai (ảnh chụp dữ liệu)

⚠️ NGUYÊN TẮC SỬ DỤNG: đây là ẢNH CHỤP DỮ LIỆU tại thời điểm lập bảng của cơ quan quản lý, dùng để TRA CỨU NỀN (định vị mỏ, GP, đơn vị) khi soạn thảo. Giấy phép có thể đã gia hạn/thu hồi/cấp đổi, hiện trạng đã thay đổi. TUYỆT ĐỐI không đưa số liệu vào văn bản chính thức khi chưa được Bạn xác nhận. Con số tổng hợp dưới đây tính từ dữ liệu gốc, kèm mốc thời gian.

**SỐ LIỆU CHÍNH THỨC ưu tiên trích dẫn** (nguồn: Báo cáo của UBND tỉnh về công tác QLNN về địa chất, khoáng sản năm 2025 — reference 13): đến 31/12/2025, toàn tỉnh có **178 GP khai thác còn hiệu lực** (Bộ NNMT cấp 70; Chủ tịch UBND tỉnh cấp 108) và **02 GP thăm dò còn hiệu lực** (đều là đá VLXDTT, tỉnh cấp). CSV dưới đây 208 dòng vì gồm cả GP đã hết hạn — khi cần con số "còn hiệu lực" dùng 178, khi cần tra chi tiết từng mỏ dùng CSV.

## I. BA FILE DỮ LIỆU (thư mục `du-lieu/`)

### 1. `ds-gp-khai-thac-31-10-2025.csv` — Danh sách GP khai thác toàn tỉnh, chốt 31/10/2025 (bảng theo dõi cập nhật đến 17/11/2025)

- Tổng: **208 giấy phép khai thác** (mỗi dòng 1 GP; một đơn vị có thể nhiều GP).
- Theo vùng: 137 GP vùng Yên Bái cũ; 71 GP vùng Lào Cai cũ.
- Theo cơ quan cấp: **137 GP tỉnh cấp; 70 GP Bộ cấp** (1 dòng thiếu dữ liệu).
- Theo loại khoáng sản (nhiều nhất): đá làm VLXDTT 50; cát sỏi 37; đá vôi trắng 35; quặng sắt 29; apatit 12; chì - kẽm 7; quặng đồng 5; felspat 4; đất làm gạch 4; vàng 3; grafit 3; sét 3; than 2; thạch anh 2; đất hiếm 1; nước khoáng nóng 1; serpentin 1...
- Hiện trạng (cột Hien_trang, thời điểm chốt): Đang KT ~78; Chưa KT ~28; Dừng KT (các dạng) ~20; nhiều GP ghi "Hết hạn" tại cột Ghi chú (28 GP).
- Cột: TT, Tên đơn vị, Tên mỏ - xã, Huyện (tên cũ trước sáp nhập — khi đưa vào văn bản phải quy đổi về xã mới + "tỉnh Lào Cai"), Loại KS, Số GP, Ngày cấp, Ngày hết hạn, Diện tích (ha), Cơ quan cấp, Ghi chú, Công suất (m3/tấn/năm), Hiện trạng, Thời gian XDCB, Mức sâu, Trữ lượng khai thác, Trữ lượng được phép.

### 2. `ds-gp-tham-do-yen-bai-6-2025.csv` — GP thăm dò vùng Yên Bái cũ, bảng 6/2025

- **43 GP thăm dò** (23 Bộ cấp, 20 tỉnh cấp) — tại thời điểm thống kê **toàn bộ ghi "Hết hạn"**.
- Loại: đá vôi trắng 13; cát sỏi 8; đá VLXDTT 8; đá ốp lát - mỹ nghệ 3; đất làm gạch 3; thạch anh 2; kaolin 2; mangan, chì - kẽm, grafit... 1.
- Dùng khi: rà quá khứ thăm dò của một khu vực; trả lời "khu này đã ai thăm dò chưa"; đối chiếu quyền ưu tiên cấp phép khai thác sau thăm dò (K2a Đ73 Luật, bổ sung bởi Luật 147/2025).

### 3. `theo-doi-phap-ly-mo-khai-thac-4-2026.csv` — Bảng theo dõi hồ sơ pháp lý 209 mỏ, cập nhật ~28/4/2026

Cột theo dõi (dấu "a" = đã có/đã thực hiện tại thời điểm cập nhật):
- `Nop_TKM` nộp thiết kế mỏ: 105/209
- `TB_GDDH_mo` thông báo GĐĐH mỏ: 104/209
- `Ban_giao_moc` bàn giao mốc: 113/209
- `Tram_can` lắp trạm cân: 25/209 · `Camera`: 11/209
- `Ky_quy_PHMT`: 70/209 · `QD_thue_dat`: 86/209 · `GP_VLN` giấy phép sử dụng VLNCN: 29/209
(Ô trống = chưa có hoặc chưa cập nhật — không suy diễn "vi phạm" từ ô trống; chỉ dùng để LẬP DANH SÁCH RÀ SOÁT, kết luận phải qua kiểm tra thực tế.)

## I-b. GIẤY PHÉP MỚI GHI NHẬN SAU MỐC CHỐT CSV (cập nhật thủ công, đã đối chiếu văn bản gốc)

| Mỏ / khoáng sản | Đơn vị | Giấy phép | Ghi chú với SCT |
|---|---|---|---|
| **Mỏ Quý Xa** — quặng sắt, xã Văn Bàn, tỉnh Lào Cai (**nhóm I**) | **Công ty cổ phần Khai thác và Chế biến kim loại Thủ Đô**, trụ sở KCN Tằng Loỏng, xã Tằng Loỏng, tỉnh Lào Cai | **GP 199/GP-BNNMT ngày 14/7/2026** của Bộ Nông nghiệp và Môi trường | Nguồn: CV 6795/SNNMT-KS ngày 17/7/2026 (đồng gửi SCT). Nhóm I → SCT thẩm định thiết kế mỏ, theo dõi KH quản lý rủi ro, huấn luyện KTAT, VLNCN, và **là nơi nhận báo cáo định kỳ**. Mở hồ sơ theo dõi theo reference 07 mục VI. Trụ sở khác địa chỉ mỏ → doanh nghiệp phải lưu 01 bộ bản sao sổ sách tại văn phòng mỏ (reference 14 mục V) |
| **Khu vực Bến Đền, xã Gia Phú và xã Bảo Thắng, tỉnh Lào Cai** — **tổng oxit đất hiếm (TR2O3), không bao gồm oxit xeri (CeO2)** (**nhóm I** — đất hiếm là khoáng sản chiến lược, quan trọng) | **Công ty Cổ phần Công nghiệp Khánh An**, địa chỉ Số 31, phố Tân Xuân 3, phường Đông Ngạc, thành phố Hà Nội | **GP 197/GP-BNNMT ngày 13/7/2026** của Bộ trưởng Bộ Nông nghiệp và Môi trường | Nguồn: CV 6987/SNNMT-KS ngày 23/7/2026 (đồng gửi SCT). Mỏ đất hiếm **thứ 2** trên bảng theo dõi toàn tỉnh (CSV 31/10/2025 mới ghi 1 GP đất hiếm). Nhóm I → SCT thẩm định thiết kế mỏ, theo dõi KH quản lý rủi ro, huấn luyện KTAT, VLNCN, nhận báo cáo định kỳ. Mỏ nằm trên địa bàn **2 xã** (Gia Phú, Bảo Thắng — vùng Lào Cai cũ); doanh nghiệp trụ sở Hà Nội → phải lưu 01 bộ bản sao sổ sách tại văn phòng mỏ (reference 14 mục V). Giấy phép cấp theo thành phần có ích kèm loại trừ CeO2 — trích dẫn phải chép nguyên cụm |

⚠️ Bảng này chỉ ghi giấy phép đã đối chiếu được văn bản gốc. Trước khi đưa vào văn bản chính thức vẫn phải xác nhận với Bạn về hiện trạng (đã XDCB chưa, đã thuê đất chưa...).

## II. CÁCH DÙNG TRONG NGHIỆP VỤ

1. **Chuẩn bị kiểm tra một mỏ:** lọc theo tên đơn vị/tên mỏ → lấy Số GP, ngày, diện tích, công suất, cột theo dõi pháp lý → in kèm checklist.
2. **Lập danh sách rà soát theo Chỉ thị 11:** lọc mỏ thiếu Nop_TKM (thiết kế mỏ) → danh sách đề xuất kiểm tra/tham mưu đình chỉ (sau khi xác minh lại với Bạn).
3. **Đối chiếu VLNCN:** mỏ có GP_VLN = "a" ↔ danh sách GP VLNCN của SCT; mỏ nổ mìn nhưng không có dấu → rà soát.
4. **Trả lời nhanh "mỏ X của ai, GP số mấy":** tra CSV, trả lời kèm chú thích "theo bảng theo dõi đến [mốc thời gian], đề nghị đối chiếu hồ sơ gốc".
5. **Thống kê báo cáo:** chỉ dùng làm số nền; số chính thức lấy từ SNNMT/Bạn cung cấp tại thời điểm báo cáo.

## III. LƯU Ý ĐỊA GIỚI

Cột Huyện ghi tên đơn vị hành chính CŨ (Lục Yên, Văn Yên, Trấn Yên, Yên Bình, Văn Chấn, Trạm Tấu, Mù Cang Chải, TP Yên Bái; Bát Xát, Văn Bàn, Bảo Thắng, Bảo Yên, Si Ma Cai...). Từ 01/7/2025 không còn cấp huyện — văn bản hành chính ghi "xã/phường ..., tỉnh Lào Cai". Tên xã có thể đã đổi sau sắp xếp: xác minh tên xã mới trước khi đưa vào văn bản.
