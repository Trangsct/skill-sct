# 12 - CSDL VLNCN trực tuyến của Sở (vlncn-laocai.vercel.app) - ảnh chụp tự động

> **File do máy sinh tự động** từ cơ sở dữ liệu trang https://vlncn-laocai.vercel.app (lệnh `scripts/dong_bo_tri_thuc.py` trong repo vlncn-laocai), cập nhật ngày 03/09/2026. **KHÔNG sửa tay file này** - sửa dữ liệu trên trang web rồi chạy đồng bộ (hoặc chờ lượt tự động 18h40). Số liệu là **hiện trạng CSDL của trang**: giấy phép chưa nhập lên trang thì chưa có ở đây, nên đây là bảng tra nhanh, KHÔNG phải danh mục pháp lý đầy đủ; khi trích dẫn chính thức phải mở bản PDF ký số theo liên kết trong bảng. Dữ liệu hiện trạng khác (khối lượng đã sử dụng, số kho) vẫn HỎI Bạn, không lấy từ file này.

## A. Trang web và dây chuyền dữ liệu (để biết tra ở đâu)

- Trang: https://vlncn-laocai.vercel.app (mã nguồn repo `Trangsct/vlncn-laocai`; file PDF ký số lưu repo công khai `Trangsct/vlncn-laocai-files/uploads/<số>_<ký hiệu>.pdf`).
- Các mục: Doanh nghiệp, Nhân sự, Công trình, **GP sử dụng VLNCN**, Dịch vụ nổ mìn, GP tiền chất thuốc nổ, GCN huấn luyện, **GP vận chuyển HHNH** (lĩnh vực riêng, plugin hnh-sct-vn), Báo cáo của DN (Mẫu 02), **Báo cáo định kỳ** (xem số liệu và xuất Word đúng Mẫu 03 Phụ lục X TT 23/2024 theo bản báo cáo thật của tỉnh, kỳ 6 tháng / 1 / 2 / 3 / 5 / 10 năm; mục trang chưa quản lý để 【…】), **Cập nhật dữ liệu ngay**.
- Dây chuyền tự động 18h hằng ngày: bot trên máy Bạn đọc Văn bản đi/đến trên Data360X (csdlvb.laocai.gov.vn) -> tải PDF vào hộp thư đến -> GitHub Actions dùng Gemini đọc 2 lượt 2 model, so khớp số liệu -> ghi CSDL (trường bắt buộc chắc thì tự cập nhật, chưa chắc thì mở PR chờ duyệt) -> 18h40 đồng bộ file này sang plugin.
- Bấm mọi tiêu đề cột trên trang để sắp xếp (ví dụ theo ngày hết hạn).

## B. Giấy phép sử dụng VLNCN còn hiệu lực (30 giấy phép, tính đến 03/09/2026)

| Số GP | Ngày cấp | Hết hạn | Tổ chức (mã số DN) | Công trình / địa điểm | Chủng loại, khối lượng | PDF |
|---|---|---|---|---|---|---|
| 5315/GP-SCT | 28/08/2026 | 15/03/2029 | Công ty trách nhiệm hữu hạn Khoáng sản Bản Cầm (5300692181) | Mỏ đá làm vật liệu xây dựng thông thường thôn Bản Cầm, xã Phong Hải, tỉnh Lào Cai | Thuốc nổ các loại (thuốc nổ Amonit AD1; thuốc nổ ANFO; thuốc nổ nhũ tương dùng cho lộ thiên): 62500 kg/năm; kíp nổ các l… | [5315_GP-SCT.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/5315_GP-SCT.pdf) |
| 5347/GP-SCT | 28/08/2026 | 28/08/2031 | Công ty cổ phần Mông Sơn (5200278146) | mỏ đá hoa trắng khu vực Mông Sơn | Thuốc nổ các loại (thuốc nổ Amonit AD1; thuốc nổ Anfo): 38950 kg/năm; kíp nổ các loại (kíp nổ điện vi sai; kíp nổ điện s… | [5347_GP-SCT.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/5347_GP-SCT.pdf) |
| 5323/GP-SCT | 28/08/2026 | 31/12/2026 | Công ty CP Xây dựng giao thông Yên Bái (5200193037) | Gói thầu số 14: Thi công xây dựng công trình Đường kết nối Mường La (Sơn La), Than Uyên, Tân Uyên (Lai Châu), … | Thuốc nổ các loại (thuốc nổ nhũ tương dùng cho lộ thiên; thuốc nổ Amonit AD1; thuốc nổ ANFO): 57266 kg; kíp nổ các loại … | [5323_GP-SCT.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/5323_GP-SCT.pdf) |
| 5236/GP-SCT | 24/08/2026 | 31/03/2027 | Công ty cổ phần Đầu tư xây dựng và dịch vụ thương mại Trường Phát (6200118578) | Dự án Thủy điện Yên Hà |  | [5236_GP-SCT.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/5236_GP-SCT.pdf) |
| 5234/GP-SCT | 24/08/2026 | 24/08/2031 | Công ty cổ phần Miền Tây (5200278918) | Mỏ đá vôi làm vật liệu xây dựng thông thường khu vực phường Trung Tâm, tỉnh Lào Cai | Thuốc nổ các loại (thuốc nổ Amonit AD1; thuốc nổ Anfo): 21400 kg/năm; Kíp nổ điện các loại (kíp nổ điện vi sai; kíp nổ đ… | [5234_GP-SCT.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/5234_GP-SCT.pdf) |
| 5235/GP-SCT | 24/08/2026 | 31/03/2027 | Công ty TNHH MTV Thương mại tổng hợp Thành Nam (5300738100) | dự án Thủy điện Yên Hà | Thuốc nổ các loại (Anfo, Amonit AD1, nhũ tương lộ thiên, nhũ tương chuyên dụng trong hầm lò, công trình ngầm không có kh… | [5235_GP-SCT.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/5235_GP-SCT.pdf) |
| 2743/GP-UBND | 07/08/2026 | 31/12/2026 | Công ty CP Đầu tư và Phát triển An Việt (2900837203) | Thi công Gói thầu số 13: đường nối Quốc lộ 32 với cao tốc Nội Bài - Lào Cai (IC14), phân đoạn nổ mìn Km1+443,8… | Thuốc nổ 53.657 kg; Kíp nổ điện 22.085 cái; Dây nổ chịu nước 35.678 m | [2743_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/2743_GP-UBND.pdf) |
| 2628/GP-UBND | 30/07/2026 | 31/12/2026 | Công ty CP Xây dựng giao thông Yên Bái (5200193037) | Thi công Gói thầu số 13: đường nối Quốc lộ 32 với cao tốc Nội Bài - Lào Cai (IC14), phân đoạn Km0 - Km1+443,80… | Thuốc nổ 72.215 kg; Kíp nổ 48.336 cái; Dây nổ chịu nước 81.623 m | [2628_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/2628_GP-UBND.pdf) |
| 2507/GP-UBND | 21/07/2026 | 05/07/2031 | Công ty Cổ phần Khai thác vật liệu xây dựng Miền Bắc (5300319526) | Mỏ đá làm VLXD thông thường thôn Toòng Già | Thuốc nổ các loại (amonit AD1, Anfo, nhũ tương lộ thiên) 63.000 kg/năm; Kíp nổ (điện vi sai, điện số 8) 11.090 cái/năm; … | [2507_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/2507_GP-UBND.pdf) |
| 2270/GP-UBND | 29/06/2026 | 31/10/2027 | Công ty TNHH MTV Xây dựng và Thương mại Đại Thành Sơn (5300721724) | Thi công Gói thầu XL-01B: khoan đào, gia cố các tuyến hầm dẫn nước thủy điện Hỏm Dưới | Thuốc nổ 32.549 kg; Kíp nổ 29.472 cái; Dây nổ chịu nước 17.036 m | [2270_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/2270_GP-UBND.pdf) |
| 2059/GP-UBND | 13/06/2026 | 31/12/2026 | Công ty CP Tư vấn Xây dựng và Thương mại Tiến Đạt (5200324353) | Thi công Gói thầu 31: đường kết nối Mường La - IC15, phân đoạn nổ mìn cọc 39C (Km57+260,63) - cọc 91+5,73m (Km… | Thuốc nổ 9.787 kg; Kíp nổ 5.120 cái; Dây nổ chịu nước 8.028 m | [2059_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/2059_GP-UBND.pdf) |
| 2008/GP-UBND | 08/06/2026 | 31/12/2027 | Công ty CP Đầu tư phát triển Đô thị và Khu công nghiệp (0101172083) | Thi công thủy điện Ngòi Nhù 1A (đập đầu mối vai phải, đường ống áp lực, hầm dẫn nước, tháp điều áp) | Thuốc nổ 50.375 kg; Kíp nổ 40.464 cái; Dây nổ chịu nước 31.074 m | [2008_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/2008_GP-UBND.pdf) |
| 1802/GP-UBND | 23/05/2026 | 28/02/2027 | Công ty CP Xây dựng giao thông Yên Bái (5200193037) | Thi công Gói thầu 31: đường kết nối Mường La - IC15, phân đoạn nổ mìn Km58+790,49 - Km60+000 | Thuốc nổ 24.059 kg; Kíp nổ 11.327 cái; Dây nổ chịu nước 20.102 m | [1802_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/1802_GP-UBND.pdf) |
| 1219/GP-UBND | 09/04/2026 | 31/12/2027 | Công ty CP Đầu tư Xây dựng Hạ tầng Cơ sở (0101151252) | Thi công thủy điện Nậm Cang 1A (hố móng nhà máy, đập, đường VH1, VH2, hầm dẫn nước chính, hầm chuyển nước) | Thuốc nổ 142.850 kg; Kíp nổ 115.900 cái; Dây nổ chịu nước 38.500 m | [1219_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/1219_GP-UBND.pdf) |
| 1161/GP-UBND | 02/04/2026 | 02/04/2027 | Công ty TNHH Anh Nguyên (5300145291) | Khai thác mỏ đá làm VLXD thông thường tại thôn Hoàng Thu Phố A, xã Si Ma Cai, tỉnh Lào Cai | Thuốc nổ 22.800 kg; Kíp nổ 8.978 cái; Dây nổ 6.914 m | [1161_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/1161_GP-UBND.pdf) |
| 829/GP-UBND | 27/03/2026 | 27/03/2027 | Công ty TNHH MTV Duy Hiếu (5200332830) | Khai thác mỏ đá làm VLXD thông thường tại Bản Mỏ Đá, xã Xuân Hòa, tỉnh Lào Cai | Thuốc nổ 8.400 kg; Kíp nổ 8.938 cái; Dây nổ 4.442 m | [829_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/829_GP-UBND.pdf) |
| 507/GP-UBND | 25/02/2026 | 25/02/2027 | Công ty CP Xây dựng giao thông Yên Bái (5200193037) | Thi công Gói thầu số 13: đoạn Km0 - Km2+571 và khu TĐC 1, nối QL32 với cao tốc Nội Bài - Lào Cai | Thuốc nổ 92.075 kg; Kíp nổ 57.546 cái; Dây nổ 81.623 m | [507_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/507_GP-UBND.pdf) |
| 471/GP-UBND | 13/02/2026 | 13/02/2027 | Công ty TNHH MTV Xây dựng và Đầu tư Cộng Lực (2700189308) | Thi công các hạng mục thuộc Dự án thủy điện Nậm Khóa 1-2, xã Nậm Xé, huyện Văn Bàn, tỉnh Lào Cai | Thuốc nổ 6.579 kg; Kíp nổ 54.251 cái; Dây nổ 26.730 m | [471_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/471_GP-UBND.pdf) |
| 362/GP-UBND | 06/02/2026 | 06/02/2027 | Công ty TNHH Hiệp Phú (5000197820) | Thi công Gói thầu số 15: đường kết nối Mường La (Sơn La) - IC15 Nội Bài - Lào Cai | Thuốc nổ 64.205 kg; Kíp nổ 34.183 cái; Dây nổ 29.550 m | [362_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/362_GP-UBND.pdf) |
| 371/GP-UBND | 06/02/2026 | 06/02/2027 | Công ty TNHH MTV Duy Cương (5000458060) | Thi công Gói thầu XL-01A: các tuyến hầm và khoan phá đá, Dự án thủy điện Hỏm Dưới, xã Nậm Chày, tỉnh Lào Cai | Thuốc nổ 78.866 kg; Kíp nổ 68.984 cái; Dây nổ chịu nước 40.747 m | [371_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/371_GP-UBND.pdf) |
| 247/GP-UBND | 29/01/2026 | 29/01/2027 | Công ty CP Xây dựng giao thông Yên Bái (5200193037) | Thi công Gói thầu số 14: đường kết nối Mường La (Sơn La), Than Uyên, Tân Uyên (Lai Châu), Mù Cang Chải (Yên Bá… | Thuốc nổ 69.972 kg; Kíp nổ 36.622 cái; Dây nổ 57.391 m | [247_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/247_GP-UBND.pdf) |
| 169/GP-UBND | 23/01/2026 | 23/01/2027 | Công ty TNHH Anh Nam Xuân Thủy (2600958743) | Thi công Gói thầu số 05: xử lý các vị trí tiềm ẩn tai nạn giao thông trên QL4D (Km183+00) | Thuốc nổ 11.607 kg; Kíp nổ 4.151 cái; Dây nổ 5.844 m | [169_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/169_GP-UBND.pdf) |
| 2294/GP-UBND | 09/12/2025 | 31/03/2027 | Công ty TNHH MTV Sông Đà 10.1 (5900320001) | Thi công hầm cao tốc Nội Bài - Lào Cai (hầm trái) Km186+221 - Km186+751 | Thuốc nổ 106.537 kg; Kíp nổ 109.187 cái; Dây nổ 106.000 m | [2294_GP-UBND.docx](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/2294_GP-UBND.docx) |
| 2241/GP-UBND | 05/12/2025 | 05/12/2026 | Công ty TNHH Hiệp Phú (5000197820) | Thi công Gói thầu SFD-XL01: đoạn tuyến Khánh Hòa - Văn Yên (Km6+663,9 - Km10+981,63) | Thuốc nổ 12.301 kg; Kíp nổ 6.593 cái; Dây nổ chịu nước 5.663 m | [2241_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/2241_GP-UBND.pdf) |
| 2076/GP-UBND | 26/11/2025 | 10/12/2026 | Công ty TNHH Linh Huy Hoàng (0500455580) | Thi công Gói thầu số 31: đường kết nối Mường La - Than Uyên - IC15 (Km54+342 - Km57+260) | Thuốc nổ 17.454 kg; Kíp nổ 9.136 cái; Dây nổ 14.315 m | [2076_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/2076_GP-UBND.pdf) |
| 2044/GP-UBND | 24/11/2025 | 24/11/2028 | Công ty CP Xây dựng Thương mại và Phát triển Hầm mỏ Võ Nghệ (2902038301) | Thi công hầm dẫn nước bổ sung thủy điện Bắc Nà, xã Bản Liền, huyện Bắc Hà, tỉnh Lào Cai | Thuốc nổ 40.530 kg; Kíp nổ 35.486 cái; Dây nổ 12.056 m | [2044_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/2044_GP-UBND.pdf) |
| 1855/QĐ-UBND | 03/11/2025 | 03/11/2026 | Công ty cổ phần Khoáng sản Yên Bái VPG (5200190029) | Khai thác mỏ felspat thôn Hồng Quân, xã Thác Bà, tỉnh Lào Cai | Thuốc nổ 6.837 kg/năm; Kíp nổ 19.200 cái/năm | [1855_QĐ-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/1855_QĐ-UBND.pdf) |
| 1822/GP-UBND | 31/10/2025 | 31/12/2028 | Công ty TNHH Xây lắp công trình Hồng Toàn (5300204892) | Khai thác đá làm VLXD thông thường tại mỏ đá thôn Bản Cầm, xã Phong Hải, tỉnh Lào Cai | Thuốc nổ 61.500 kg/năm; Kíp nổ 13.150 cái/năm; Dây nổ chịu nước 12.017 m/năm | [1822_GP-UBND.docx](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/1822_GP-UBND.docx) |
| 1369/GP-UBND | 07/10/2025 | 07/10/2026 | Công ty TNHH HTQ Yên Bái (5200854939) | Khai thác đá làm VLXD thông thường tại khu vực Gốc Sấu, thôn Đoàn Kết, xã Tân Hợp, tỉnh Lào Cai | Thuốc nổ 6.150 kg/năm; Kíp nổ 2.015 cái/năm; Dây nổ chịu nước 2.743 m/năm | [1369_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/1369_GP-UBND.pdf) |
| 1285/GP-UBND | 30/09/2025 | 30/09/2026 | Công ty TNHH thương mại và xây dựng hạ tầng Bắc Hà (0107829819) | Thi công Gói thầu 11: Xây dựng hệ thống cấp nước sạch các xã trên địa bàn huyện Si Ma Cai | Thuốc nổ 4.039 kg; Kíp nổ 5.392 cái; Dây nổ 1.426 m | [1285_GP-UBND.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/1285_GP-UBND.pdf) |

## C. Giấy phép sử dụng VLNCN đã hết hiệu lực trong CSDL (25 giấy phép, chỉ để tra lịch sử)

| Số GP | Ngày cấp | Hết hạn | Tổ chức | Công trình |
|---|---|---|---|---|
| 1363/GP-UBND | 22/04/2026 | 30/06/2026 | Công ty CP Đầu tư và Phát triển An Việt | Thi công Gói thầu số 13: đường nối QL32 với cao tốc Nội Bài - Lào Cai (IC14), phân đoạn nổ… |
| 821/GP-UBND | 27/03/2026 | 31/05/2026 | Công ty CP Tập đoàn Long Biên | Thi công Gói thầu XL-01: Km2+00 - Km3+127 và Km3+417 - Km4+340, tuyến nối Lai Châu (QL279) |
| 914/GP-UBND | 26/08/2025 | 26/08/2026 | Công ty TNHH MTV Duy Cương | Thi công hầm dẫn nước và giếng điều áp thuộc Dự án mở rộng nâng công suất thủy điện Suối C… |
| 882/GP-UBND | 22/08/2025 | 31/12/2025 | Công ty CP Đầu tư và Phát triển Elementa VN | Thi công Gói thầu XL-01: đoạn Km0 - Km18+500, tuyến nối Lai Châu (Km4+974 - Km6+000) |
| 782/QĐ-UBND | 13/08/2025 | 13/08/2026 | Công ty Cổ phần đầu tư Tân Hoàng Long | Khai thác đá làm VLXD thông thường tại mỏ đá Bản Cầm, xã Phong Hải, tỉnh Lào Cai |
| 12/GP-SCT | 16/06/2025 | 16/06/2026 | Công ty TNHH MTV Xây dựng và Đầu tư Cộng Lực | Thi công tuyến năng lượng thuộc Dự án thủy điện Nậm Khóa 1-2, xã Nậm Xé, huyện Văn Bàn |
| 10/GP-SCT | 11/06/2025 | 20/03/2026 | Công ty CP Xây dựng Thương mại và Phát triển Hầm mỏ Võ Nghệ | Thi công đào, gia cố đường hầm dẫn nước dự án thủy điện Bắc Nà |
| 20/GP-SCT | 21/08/2024 | 21/08/2025 | Công ty TNHH Xây lắp công trình Hồng Toàn | TTHCCấp lại Giấy phép sử dụng VLNCN tại mỏ đá Bản Cầm - Cty KS Bản Cầm |
| 04/GP-SCT | 07/03/2024 | 07/03/2025 | Công ty TNHH Anh Nguyên | TTHCCấp Giấy phép sd VLNCN mỏ đá thôn Tả Hồ, xã Tà Chải, huyện Bắc Hà -Cty Anh Nguyên |
| 27/GP-SCT | 14/09/2022 | 14/09/2023 | Công ty TNHH Đại Trí | TTHCCấp lại Giấy phép sử dụng VLNCN cho Công ty Đại Trí thi công công trình đường liên xã … |
| 25/GP-SCT | 22/08/2022 | 22/08/2023 | HTX Hoàng Vũ | TTHCCấp Giấy phép sử dụng VLNCN cho Hợp tác xã Hoàng Vũ thi công công trình đường sắp xếp … |
| 23/GP-SCT | 15/08/2022 | 15/08/2023 | Công ty Cổ phần đầu tư Tân Hoàng Long | Cấp Giấy phép sử dụng VLNCN cho Công ty CP ĐT Tân Hoàng Long |
| 21/GP-SCT | 29/07/2022 | 29/07/2023 | Công ty TNHH MTV Định Nghĩa | Cấp Giấy phép sử dụng VLNCN cho Công ty TNHH MTV Định Nghĩa tại Gói thầu số 15: Thi công x… |
| 19/GP-SCT | 21/07/2022 | 21/07/2023 | HTX Hoàng Vũ | TTHCGiấy phép sử dụng VLNCN HTX Hoàng Vũ công trình đường liên huyện từ xã Lùng Sui, huyện… |
| 18/GP-SCT | 21/06/2022 | 21/06/2023 | Công ty TNHH Đại Trí | TTHCCấp lại giấy phép sử dụng VLNCN cho Công ty Đại Trí |
| 17/GP-SCT | 15/06/2022 | 15/06/2023 | Công ty TNHH 995 | TTHCCấp Giấy phép nổ mìn đường liên thôn xã Tung Chung Phố, huyện Mường Khương - Cty 995 |
| 38/GP-SCT | 09/09/2021 | 09/09/2022 | Công ty TNHH VLXD Sơn Thạch | GIẤY PHÉP SỬ DỤNG VẬT LIỆU NỔ CÔNG NGHIỆP (C.TY HUY Hoàng) |
| 22/GP-SCT | 28/05/2021 | 28/05/2022 | Công ty TNHH VLXD Sơn Thạch | Giấy phép sử dụng VLNCN Hưng Phát nổ mỏ đá Mã Tuyển, TT Mường Khương |
| 11/GP-SCT | 01/03/2021 | 01/03/2022 | Công ty CP Đầu tư phát triển Đô thị và Khu công nghiệp | Giấy phép sử dụng VLNCN tại thủy điện Pờ Hồ của Cty phát triển đô thị và KCN |
| 07/GP-SCT | 27/01/2021 | 27/01/2022 | Công ty TNHH Anh Nguyên | Giấy phép sử dụng VLNCN ( Cty Anh Nguyên nổ tại thôn Phố Thầu, thị trấn Si Ma Cai) |
| 09/GP-SCT | 27/01/2021 | 27/01/2022 | Công ty TNHH MTV Định Nghĩa | Giấy phép sử dụng VLNCN cấp cho Cty Định Nghĩa nổ tại thủy điện Nậm Cang A1 |
| 05/GP-SCT | 22/01/2021 | 22/01/2022 | Công ty TNHH Đại Trí | Giấy phép sử dụng VLNCN Cty Đại trí nổ tại khu tái định cư sân bay Cam Cọn |
| 06/GP-SCT | 22/01/2021 | 22/01/2022 | Công ty TNHH Linh Anh | Cấp giấy phép sử dụng VLNCN Cty Linh Anh nổ tại tt Mường Khương |
| 03/GP-SCT | 15/01/2021 | 15/01/2022 | Công ty TNHH Anh Nguyên | Giấy phép sử dụng VLNCN (công ty Anh Nguyên) |
| 01/GP-SCT | 12/01/2021 | 12/01/2022 | Công ty TNHH Xây lắp công trình Hồng Toàn | Giấy phép sử dụng VLNCN Cty Hồng Toàn mỏ đá Bản Cầm |

## D. Thống kê nhanh

| Năm cấp | Số GP sử dụng VLNCN | Trong đó ký hiệu /GP-SCT |
|---|---|---|
| 2026 | 24 | 6 |
| 2025 | 13 | 2 |
| 2024 | 2 | 2 |
| 2022 | 7 | 7 |
| 2021 | 9 | 9 |

- Tổ chức có GP sử dụng VLNCN còn hiệu lực: **25**.
- Giấy phép kinh doanh tiền chất thuốc nổ trong CSDL: **14** (còn hiệu lực 14).
- Thông báo dịch vụ nổ mìn trong CSDL: **16**, đang hoạt động 16, của 5 đơn vị.

## E. Giấy phép kinh doanh tiền chất thuốc nổ

| Số GP | Ngày cấp | Hết hạn | Tổ chức | PDF |
|---|---|---|---|---|
| 03/KDTCTN/GP-HC (2026) | 23/01/2026 | 23/01/2031 | Tổng công ty Kinh tế Kỹ thuật Công nghiệp Quốc phòng | [03_KDTCTN_GP-HC_2026.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/tctn/03_KDTCTN_GP-HC_2026.pdf) |
| 01/KDTCTN/GP-HC (2026) | 21/01/2026 | 23/01/2031 | Công ty TNHH SHA Group | [01_KDTCTN_GP-HC_2026.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/tctn/01_KDTCTN_GP-HC_2026.pdf) |
| 02/KDTCTN/GP-HC (2026) | 21/01/2026 | 23/01/2031 | Công ty CP Sản xuất và Thương mại Hóa chất An Phú | [02_KDTCTN_GP-HC_2026.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/tctn/02_KDTCTN_GP-HC_2026.pdf) |
| 12/KDTCTN/GP-HC | 12/12/2025 | 12/12/2030 | Công ty TNHH thương mại và xây dựng hạ tầng Bắc Hà | [12_KDTCTN_GP-HC.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/tctn/12_KDTCTN_GP-HC.pdf) |
| 13/KDTCTN/GP-HC | 12/12/2025 | 12/12/2030 | Công ty CP AHH | [13_KDTCTN_GP-HC.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/tctn/13_KDTCTN_GP-HC.pdf) |
| 09/KDTCTN/GP-HC | 23/10/2025 | 23/10/2030 | Công ty TNHH MTV Hưng Hiên | [09_KDTCTN_GP-HC.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/tctn/09_KDTCTN_GP-HC.pdf) |
| 10/KDTCTN/GP-HC | 23/10/2025 | 23/10/2030 | Công ty CP Tập đoàn Long Biên | [10_KDTCTN_GP-HC.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/tctn/10_KDTCTN_GP-HC.pdf) |
| 08/KDTCTN/GP-HC | 14/10/2025 | 14/10/2030 | Công ty CP Đầu tư và Phát triển Elementa VN | [08_KDTCTN_GP-HC.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/tctn/08_KDTCTN_GP-HC.pdf) |
| 04/KDTCTN/GP-HC | 01/10/2025 | 01/10/2030 | Công ty TNHH SHA Group | [04_KDTCTN_GP-HC.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/tctn/04_KDTCTN_GP-HC.pdf) |
| 05/KDTCTN/GP-HC | 01/10/2025 | 01/10/2030 | Công ty TNHH Minh Long Việt Nam | [05_KDTCTN_GP-HC.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/tctn/05_KDTCTN_GP-HC.pdf) |
| 06/KDTCTN/GP-HC | 01/10/2025 | 01/10/2030 | Công ty CP Sản xuất và Thương mại Hóa chất An Phú | [06_KDTCTN_GP-HC.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/tctn/06_KDTCTN_GP-HC.pdf) |
| 07/KDTCTN/GP-HC | 01/10/2025 | 01/10/2030 | Công ty CP Vật tư Phú Thọ | [07_KDTCTN_GP-HC.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/tctn/07_KDTCTN_GP-HC.pdf) |
| 02/KDTCTN/GP-HC | 14/07/2025 | 14/07/2030 | Công ty CP Sản xuất và Thương mại Hóa chất An Phú | [02_KDTCTN_GP-HC.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/tctn/02_KDTCTN_GP-HC.pdf) |
| 03/KDTCTN/GP-HC | 14/07/2025 | 14/07/2030 | Công ty CP Vật tư Phú Thọ | [03_KDTCTN_GP-HC.pdf](https://raw.githubusercontent.com/Trangsct/vlncn-laocai-files/main/uploads/tctn/03_KDTCTN_GP-HC.pdf) |

## F. Dịch vụ nổ mìn (thông báo Sở đã tiếp nhận)

| Số VB | Ngày | Đơn vị dịch vụ nổ mìn | GP dịch vụ nổ mìn | Công trình | Trạng thái |
|---|---|---|---|---|---|
| 230/PC-VPUBND | 13/03/2026 | Công ty Công nghiệp Hóa chất Mỏ Tây Bắc |  | Thi công nổ mìn tại Nhà máy xử lý chất thải công nghiệp và nguy hại, KCN Tằng Loỏng, huyện… | đang hoạt động |
| 153/PC-VPUBND | 10/02/2026 | Tổng công ty Kinh tế Kỹ thuật Công nghiệp quốc phòng (Bộ Quốc phòng) |  | Thi công phá đá Gói thầu XL-03: Xây dựng đoạn Km40+000 - Km63+446, đường kết nối giao thôn… | đang hoạt động |
| 152/PC-VPUBND | 10/02/2026 | Tổng công ty Kinh tế Kỹ thuật Công nghiệp quốc phòng (Bộ Quốc phòng) |  | Thi công nổ mìn mỏ apatit Tam Đỉnh - Làng Phúng, tỉnh Lào Cai | đang hoạt động |
| 55/PC-VPUBND | 12/01/2026 | Công ty Công nghiệp Hóa chất Mỏ Tây Bắc |  | Hoạt động dịch vụ nổ mìn tại các khai trường trên địa bàn tỉnh Lào Cai (Quý I/2026) | đang hoạt động |
| 31/PC-KT | 07/01/2026 | Tổng công ty Xây dựng Trường Sơn (Bộ Quốc phòng) |  | Thi công nổ mìn khai trường đường cao tốc Mù Cang Chải - IC15 Nội Bài - Lào Cai | đang hoạt động |
| 6/VPUBND-KT | 05/01/2026 | Công ty Công nghiệp Hóa chất Mỏ Tây Bắc |  | Khai thác mỏ apatit Làng Cáng 2 và khai trường 32, xã Hợp Thành, TP Lào Cai | đang hoạt động |
| 16/PC-KT | 05/01/2026 | Tổng công ty Kinh tế Kỹ thuật Công nghiệp quốc phòng (Bộ Quốc phòng) |  | Thi công nổ mìn đoạn tuyến Khánh Hòa - Văn Yên, từ Km15+523,45 đến Km22+300 | đang hoạt động |
| 547/PC-VP | 27/12/2025 | Công ty Công nghiệp Hóa chất Mỏ Tây Bắc |  | Thi công nổ mìn tại mỏ đồng Sin Quyền, huyện Bát Xát, tỉnh Lào Cai | đang hoạt động |
| 546/PC-VP | 27/12/2025 | Công ty Công nghiệp Hóa chất Mỏ Tây Bắc |  | Thi công nổ mìn tại mỏ đồng Tả Phời, huyện Bát Xát, tỉnh Lào Cai | đang hoạt động |
| 549/PC-VP | 27/12/2025 | Công ty Công nghiệp Hóa chất Mỏ Tây Bắc |  | Thi công nổ mìn khai trường mỏ apatit trên địa bàn tỉnh Lào Cai | đang hoạt động |
| 550/PC-VP | 27/12/2025 | Công ty Công nghiệp Hóa chất Mỏ Tây Bắc |  | Thi công nổ mìn khai trường mỏ trên địa bàn tỉnh Lào Cai | đang hoạt động |
| 534/PC-VPUBND | 19/12/2025 | Công ty Công nghiệp Hóa chất Mỏ Tây Bắc |  | Thi công nổ mìn tại mỏ sắt Kíp Tước, huyện Bát Xát, tỉnh Lào Cai | đang hoạt động |
| 423/PC-VPUBND | 18/11/2025 | Công ty Công nghiệp Hóa chất Mỏ Tây Bắc |  | Khai thác đá hoa trắng tại mỏ thôn Trung Sơn, xã Bảo Ái, huyện Yên Bình, tỉnh Lào Cai | đang hoạt động |
| 387/PC-VPUBND | 06/11/2025 | Công ty Công nghiệp Hóa chất Mỏ Tây Bắc |  | Khai thác đá làm VLXD thông thường tại mỏ Đồng Bông, xã Xuân Ái, huyện Văn Yên, tỉnh Lào C… | đang hoạt động |
| 349/PC-VPUBND | 29/10/2025 | Công ty Cổ phần Xi măng và Khoáng sản Yên Bái |  | Khai thác đá vôi tại mỏ Mông Sơn, xã Bảo Ái, huyện Yên Bình, tỉnh Lào Cai | đang hoạt động |
| 29/TB-TH | 25/08/2025 | Doanh nghiệp tư nhân Thành Hương (Nghĩa Lộ, Yên Bái) |  | Hoạt động dịch vụ nổ mìn trên địa bàn tỉnh Lào Cai | đang hoạt động |
