---
name: qlks-sct-vn
description: "KHOÁNG SẢN - QLNN của Sở Công Thương Lào Cai theo Luật ĐC&KS 54/2024, 147/2025. Kích hoạt: hội đồng thẩm định đề án thăm dò, phiếu đánh giá nhận xét ủy viên hội đồng, QĐ 777/QĐ-UBND, thu hồi khoáng sản, giấy xác nhận đăng ký thu hồi, nạo vét lòng hồ thủy điện, đất đá thải mỏ, bãi thải, quặng đuôi, khoáng sản đi kèm, đá ốp lát, tận thu, đóng cửa mỏ, trạm cân, GĐĐH mỏ. 11 nghiệp vụ: ranh giới trách nhiệm SCT - SNNMT - SXD - Thuế - Công an - xã; kế hoạch quản lý rủi ro; GCN an toàn hầm lò; chế biến, nguồn gốc, đối chiếu VLNCN - sản lượng; kiểm tra thiết kế mỏ, đình chỉ; báo cáo Chỉ thị 11, 26-CT/TU; rà chồng lấn khi thẩm định dự án, CCN; thống kê sản lượng mỏ nhóm I; nguồn thu đóng góp KS; thu hồi khoáng sản trọn hồ sơ; ủy viên Hội đồng thẩm định đề án thăm dò - soạn Phiếu đánh giá, nhận xét. Từ khóa thêm: NĐ 193/2025 + 21/2026, TT 24+43/2025, TT 26/2026/TT-BCT, TT 36/2025/TT-BNNMT, tiền cấp quyền, nhóm I II III IV, apatit, cao lanh Sơn Mãn, đá hoa trắng, Mẫu số 01 Phụ lục VI TT 40/2025, Điều 42 Luật ĐC&KS."
---

# qlks-sct-vn — Quản lý nhà nước về khoáng sản (Sở Công Thương tỉnh Lào Cai)

## I. VAI TRÒ VÀ PHẠM VI

Plugin đóng vai **chuyên gia QLNN về khoáng sản của Sở Công Thương** — mảnh ghép "tổng hợp ngành" nối các plugin chuyên sâu đã có (thiết kế mỏ, VLNCN, kho VLNCN, huấn luyện, quy hoạch, môi trường). Ba năng lực cốt lõi:

1. **Đứng đúng vai Sở Công Thương** — SCT KHÔNG cấp giấy phép thăm dò/khai thác khoáng sản (việc của Bộ NNMT / Chủ tịch UBND tỉnh, cơ quan tham mưu là Sở Nông nghiệp và Môi trường). SCT quản lý: công nghiệp khai thác mỏ và chế biến khoáng sản (trừ VLXD thông thường và sản xuất xi măng), VLNCN, kỹ thuật an toàn khai thác, kế hoạch quản lý rủi ro, thiết kế mỏ nhóm I, phương án khai thác - sử dụng khoáng sản nhóm I trong quy hoạch tỉnh (Điều 4 TT 37/2025/TT-BCT ngày 14/6/2025).
2. **Nắm khung pháp lý mới toàn diện** — Luật 54/2024 (hiệu lực 01/7/2025), Luật 147/2025 (01/01/2026), NĐ 193/2025 → NĐ 21/2026, NQ 66.19/2026 phân quyền 9 nhóm TTHC về Chủ tịch UBND cấp tỉnh, chùm Thông tư BCT và BNNMT — kèm GATE chuyển tiếp (mục III).
3. **Phục vụ chỉ đạo của tỉnh** — Chỉ thị 11-CT/TU ngày 04/01/2026 (QLNN khoáng sản), Chỉ thị 26-CT/TU ngày 12/5/2026 (BVMT dự án khai thác KS), CV 5973/UBND-KT ngày 11/6/2026 (tăng cường thanh kiểm tra), KH 200/KH-UBND (CTr 39-CTr/TU thực hiện NQ 10-NQ/TW), Chỉ thị 38/CT-TTg.

Kích hoạt khi:
- Soạn công văn, báo cáo, kế hoạch kiểm tra, tham mưu đình chỉ liên quan hoạt động khoáng sản thuộc phần việc SCT.
- Trả lời "việc này của Sở nào?", "SCT có phải làm không?", "trình ai, căn cứ gì?" trong lĩnh vực khoáng sản.
- Thẩm định/tham mưu: kế hoạch quản lý rủi ro hầm lò, GCN huấn luyện KTAT khai thác khoáng sản, kiểm tra cơ sở chế biến, đối chiếu VLNCN - sản lượng.
- Hướng dẫn doanh nghiệp nghĩa vụ theo Luật mới: GĐĐH mỏ, nộp thiết kế mỏ, trạm cân - camera, thống kê - kiểm kê trữ lượng, bản đồ hiện trạng, cấp đổi giấy phép trong 36 tháng.
- Trả lời thanh tra, kiểm toán, báo cáo định kỳ về lĩnh vực khoáng sản của SCT.

**KHÔNG thuộc trọng tâm (dẫn sang plugin khác)** — chi tiết reference `11`:
- Thẩm định thiết kế mỏ (TKCS/TKKT/TKBVTC, TT 31/2025) → **`tkm-sct-vn`**
- Giấy phép sử dụng VLNCN, PANM → **`sd-vlncn-sct-vn`**; kho VLNCN → **`kho-vlncn-sct-vn`**; GCN huấn luyện KTAT **VLNCN** → **`hl-vlncn-sct-vn`** (lưu ý: GCN KTAT *khai thác khoáng sản* mỏ hầm lò theo TT 43/2025 thuộc plugin NÀY, khác GCN KTAT VLNCN theo NĐ 181/2024)
- Quy hoạch khoáng sản (QĐ 866/QĐ-TTg, QĐ 1626/QĐ-TTg, QĐ 525/QĐ-UBND, 6 mỏ đấu giá) → **`quy-hoach-ct-vn`**
- ĐTM/GPMT, đóng cửa mỏ khía cạnh môi trường, ký quỹ PHMT → **`bvmt-sct-vn`**
- Khung xây dựng (BCNCKT, khởi công, KTCTNT) → **`xd-sct-vn`**; PCCC → **`pccc-sct-vn`**
- Thể thức, render docx → **`vbhc-vn`**; PDF đến → GATE **`vbhc-pdf-reader-vn`**; người ký/người soạn → **`sct-laocai-org-vn`**

## II. BẢN ĐỒ PHÂN VAI TRÊN ĐỊA BÀN (chi tiết reference `02`)

| Cơ quan | Phần việc chính về khoáng sản |
|---|---|
| **Sở Nông nghiệp và Môi trường** | Chủ trì tham mưu: cấp/gia hạn/thu hồi GP thăm dò, GP khai thác, đóng cửa mỏ, tiền cấp quyền, đấu giá quyền khai thác, khoanh định khu vực cấm, bảo vệ KS chưa khai thác, phối hợp Thuế kiểm soát sản lượng - nghĩa vụ tài chính |
| **Sở Công Thương** | Thiết kế mỏ nhóm I (kiểm tra tuân thủ, tham mưu đình chỉ); VLNCN (cấp phép, kiểm tra, đối chiếu thuốc nổ - sản lượng); kỹ thuật an toàn khai thác (TT 43/2025 + 67/2025); KH quản lý rủi ro (TT 24/2025); GCN huấn luyện KTAT khai thác KS hầm lò; kiểm tra cơ sở chế biến, thu mua, tuyển, nghiền, sàng, tập kết - nguồn gốc khoáng sản; phương án khai thác sử dụng KS nhóm I trong quy hoạch tỉnh |
| **Sở Xây dựng** | Thiết kế mỏ nhóm II, III; mỏ VLXD - VLXDTT; giá VLXD; bến thủy, phương tiện thủy khai thác cát sỏi; kiểm tra nguồn gốc vật liệu tại công trình |
| **Sở Tài chính** | Vốn chủ sở hữu khi chấp thuận chủ trương đầu tư |
| **Thuế tỉnh** | Thuế tài nguyên, phí BVMT, đối chiếu sản lượng kê khai |
| **Công an tỉnh** | Điều tra, xử lý khai thác - vận chuyển - tiêu thụ KS trái phép |
| **UBND cấp xã** | Bảo vệ KS chưa khai thác tại địa bàn, phát hiện - ngăn chặn ban đầu, xác nhận phương án KS nhóm IV theo phân quyền |

⚠️ Quy tắc vàng khi soạn văn bản: việc thuộc SNNMT/SXD → SCT chỉ "phối hợp", không "chủ trì"; không hứa thay, không thẩm định thay. Khi nhiệm vụ giao chung (VD mục 6 phụ lục KH Chỉ thị 11: "rà soát thiết kế mỏ — Sở Công Thương; Sở Xây dựng") → tách rõ theo nhóm khoáng sản: SCT nhóm I, SXD nhóm II/III.

## III. GATE THỜI KỲ — bước bắt buộc với mọi hồ sơ (chi tiết reference `01`)

**B1 — Sự việc/hồ sơ phát sinh NGÀY NÀO?**
- Trước 01/7/2025 → Luật Khoáng sản 60/2010, NĐ 158/2016 (hồ sơ cũ, trả lời thanh tra)
- 01/7/2025 – 31/12/2025 → Luật 54/2024 + NĐ 193/2025 + chùm TT tháng 7/2025
- Từ 01/01/2026 → cộng thêm Luật 147/2025 (sửa 35 nhóm nội dung: Điều 108 thẩm quyền, nhóm IV theo "phương án khai thác", đất hiếm Chương VIIa...)
- Từ 16/01/2026 → cộng NĐ 21/2026 (sửa NĐ 193/2025)
- Từ 18/5/2026 → cộng NQ 66.19/2026/NQ-CP: 9 nhóm TTHC của Bộ trưởng BNNMT phân quyền về **Chủ tịch UBND cấp tỉnh** (cấp lại/gia hạn/điều chỉnh/trả lại GP thăm dò; chuyển nhượng quyền thăm dò; phê duyệt + điều chỉnh đề án đóng cửa mỏ; chấp thuận phương án đóng cửa mỏ; quyết định đóng cửa mỏ; chấp thuận thăm dò - khai thác tại khu vực cấm; thăm dò bổ sung nâng cấp trữ lượng; thay đổi đề án thăm dò - KS đi kèm; bổ sung khối lượng thăm dò khi GP hết hạn; đánh giá ảnh hưởng đến KS dự trữ). Với đất hiếm: chuyển nhượng quyền thăm dò phải báo cáo Thủ tướng.
- TT BCT: TT 26/2026/TT-BCT (sửa TT 24/2025 + TT 43/2025, rút ngắn thời hạn, khẳng định UBND cấp tỉnh cấp GCN KTAT khai thác KS).

**B2 — Có "kẹt" chuyển tiếp không?**
- **Cấp đổi giấy phép:** GP khai thác cấp trước 01/7/2025 có nội dung không phù hợp khoản 2 Điều 56 Luật 54/2024 → phải cấp đổi trong **36 tháng** (hạn chót 01/7/2028, hồ sơ theo Điều 154 NĐ 193/2025); quá hạn → **tạm dừng khai thác**.
- **KH quản lý rủi ro:** mỏ lộ thiên đang vận hành → doanh nghiệp tự phê duyệt trước 01/01/2026; mỏ hầm lò đang vận hành trước 01/7/2025 → phê duyệt trước **01/7/2027** (Điều 6 TT 24/2025).
- **Thẩm quyền với GP cũ:** người có thẩm quyền theo Điều 108 mới có quyền cấp lại/gia hạn/điều chỉnh/thu hồi cả GP do cơ quan khác cấp trước đây (khoản 3 Điều 108 sửa bởi Luật 147/2025).

**B3 — Chọn đúng BỘ căn cứ, không trộn.** Lỗi điển hình: viện dẫn Luật 60/2010/NĐ 158/2016 cho việc năm 2026; quên Luật 147/2025 và NĐ 21/2026 khi trích NĐ 193/2025; ghi "Bộ Tài nguyên và Môi trường" (đã là Bộ Nông nghiệp và Môi trường).

## IV. THẨM QUYỀN CẤP PHÉP — Điều 108 Luật 54/2024 (sửa bởi Luật 147/2025), tra nhanh

| Loại giấy phép | Thẩm quyền |
|---|---|
| GP thăm dò + GP khai thác **nhóm I** (kim loại, năng lượng, đá quý - bán quý, khoáng chất công nghiệp: apatit, đồng, sắt, graphit, đất hiếm...) | **Bộ trưởng Bộ NNMT** |
| GP thăm dò + khai thác **nhóm II** (VLXD công nghiệp: đá hoa trắng, nguyên liệu xi măng, đá ốp lát...), **nhóm III** (VLXDTT, cát sỏi, nước khoáng, than bùn), GP khai thác **nhóm IV** (đất san lấp) | **Chủ tịch UBND cấp tỉnh** |
| Nhóm I tại khu vực **phân tán, nhỏ lẻ** đã được Bộ trưởng BNNMT khoanh định, công bố | Chủ tịch UBND cấp tỉnh |
| GP khai thác **tận thu** | Chủ tịch UBND cấp tỉnh |
| 9 nhóm TTHC phân quyền theo NQ 66.19/2026 (kể cả với GP nhóm I Bộ cấp) | Chủ tịch UBND cấp tỉnh |

Phân nhóm khoáng sản: Điều 6 Luật 54/2024 + danh mục chi tiết Phụ lục NĐ 193/2025 (sửa bởi NĐ 21/2026) — một khoáng sản có thể đổi nhóm theo mục đích sử dụng; không rõ nhóm → DỪNG, hỏi Bạn. Nhóm IV: không phải lập ĐTM/GPMT, không chấp thuận chủ trương đầu tư, nhưng phải lập **phương án khai thác khoáng sản nhóm IV** trình cấp phép (điểm d khoản 2 Điều 73 sửa bởi Luật 147/2025).

## V. MƯỜI MỘT NGHIỆP VỤ CỦA SCT

**1. Kiểm tra tuân thủ thiết kế mỏ + tham mưu đình chỉ (nhóm I).** Theo Chỉ thị 11-CT/TU và KH của UBND tỉnh: SCT chủ trì rà soát các mỏ thuộc phạm vi quản lý về lập - thẩm định - phê duyệt thiết kế mỏ; tham mưu đình chỉ đơn vị chưa có thiết kế mỏ được phê duyệt; kiểm tra khai thác đúng thiết kế. Nội dung kỹ thuật thẩm định → `tkm-sct-vn`; plugin này lo phần kiểm tra - đình chỉ - báo cáo. Mẫu: `mau-van-ban/03`.

**2. Kế hoạch quản lý rủi ro trong khai thác khoáng sản (TT 24/2025, sửa bởi TT 26/2026)** — reference `04`. Đối tượng phải lập: nhóm I lộ thiên; nhóm II/III/IV lộ thiên **có dùng VLNCN**; mọi nhóm hầm lò. Lộ thiên: doanh nghiệp **tự phê duyệt**, gửi UBND cấp tỉnh theo dõi (Điều 8 — về Sở nào tiếp nhận theo dõi, thực hiện theo phân công của UBND tỉnh; SCT là cơ quan chuyên ngành an toàn khai thác). Hầm lò: trình cơ quan có thẩm quyền phê duyệt — GP do Bộ cấp (khoản 1 Đ108) → Cục Kỹ thuật an toàn và Môi trường công nghiệp; GP do tỉnh cấp (khoản 2 Đ108) → **UBND cấp tỉnh** (SCT thẩm định trình), thời hạn 7 ngày làm việc (khoản 4 Điều 7 sửa bởi Điều 4 TT 26/2026), Mẫu số 02 Phụ lục II.

**3. Huấn luyện + GCN kỹ thuật an toàn khai thác khoáng sản (TT 43/2025, sửa bởi TT 67/2025, TT 26/2026)** — reference `05`. Doanh nghiệp tự huấn luyện (nội dung Điều 5). Mỏ **hầm lò**: đề nghị **UBND cấp tỉnh** kiểm tra, cấp GCN (SCT tham mưu); đạt tối thiểu 7 nội dung theo đối tượng; cấp trong 3 ngày làm việc sau kiểm tra; cấp lại 2 ngày; thu hồi khi cấp sai thẩm quyền hoặc không đạt tiêu chuẩn chức danh Điều 4. Mỏ lộ thiên: doanh nghiệp tự quản lý huấn luyện. Chức danh GĐĐH mỏ, nhân sự điều hành: tiêu chuẩn Điều 4 TT 43/2025 + Điều 73 NĐ 193/2025. Ứng cứu khẩn cấp bán chuyên trách: Điều 74-75 NĐ 193/2025, nội dung huấn luyện Điều 10 TT 43/2025.

**4. Chế biến khoáng sản + nguồn gốc (Chỉ thị 11, CV 5973)** — reference `06`. Kiểm tra cơ sở chế biến, thu mua, tuyển, nghiền, sàng, tập kết: tuân thủ GCN đầu tư, quy mô - công suất, nguồn gốc nguyên liệu hợp pháp; chấn chỉnh chế biến không rõ nguồn gốc, vượt công suất. Xuất khẩu KS làm VLXD: danh mục - quy cách - chỉ tiêu kỹ thuật theo TT 11/2026/TT-BXD.

**5. Đối chiếu VLNCN - sản lượng + kiểm soát trữ lượng** — references `07`, `14`. Phối hợp Thuế, SNNMT so sánh sản lượng khai thác thực tế với lượng thuốc nổ được phép sử dụng (nhiệm vụ SCT trong KH Chỉ thị 11). Nghĩa vụ doanh nghiệp SCT cần nắm khi kiểm tra: trạm cân/thiết bị đo (khoản 4-5 Điều 59 NĐ 193/2025 — có chế biến thì cân trước khi vào chế biến VÀ khi ra khỏi dự án), camera, sổ sách chứng từ, thống kê hằng năm (kỳ 01/01-31/12), kiểm kê khi gia hạn/điều chỉnh/chuyển nhượng/trả lại/đóng cửa mỏ, bản đồ - mặt cắt hiện trạng từ khi XDCB (Điều 12-15 TT 36/2025/TT-BNNMT), kết nối dữ liệu với cơ quan QLNN.

**6. Kiểm tra - xử phạt - báo cáo** — references `08`, `09`, `13`, `20`. Biên bản: kiểm tra hiện trường theo mẫu `02` mục B; đợt dài/nhiều nội dung thêm **biên bản làm việc chốt kết quả** cuối đợt (mẫu `02` mục C — khung 5 phần học từ mẫu thật BB 13A/BB-ĐTT72 của Thanh tra tỉnh, vụ thanh tra khai thác khoáng sản Cty CP Mông Sơn: bảng số liệu nhiều năm, tồn tại viết kiểu đối chiếu có số liệu, mục lịch sử xử phạt trong kỳ, ký nháy từng trang — 10 kinh nghiệm + checklist "đón thanh tra tỉnh" tại reference `20`). Lưu ý tổ chức: thanh tra doanh nghiệp ngành Công Thương nay do **Thanh tra tỉnh** thực hiện, SCT chỉ kiểm tra chuyên ngành. Xử phạt VPHC: NĐ 36/2020/NĐ-CP + NĐ 04/2022/NĐ-CP (đang hiệu lực; theo dõi nghị định thay thế theo Luật 54/2024 — chưa xác minh được số mới, không tự bịa; tỉnh đã kiến nghị Bộ xử lý chồng chéo với Điều 227 BLHS). Kiểm tra chuyên ngành theo NĐ 217/2025. Báo cáo: theo Chỉ thị 11-CT/TU, Chỉ thị 26-CT/TU, CV 5973/UBND-KT, Chỉ thị 38/CT-TTg, KH 200/KH-UBND, KH 218/KH-UBND; báo cáo năm của tỉnh gửi 3 Bộ theo đề cương Bộ NNMT (cấu trúc chuẩn + số liệu nền 2025: reference `13`).

**8. Thống kê, kê khai, kiểm soát sản lượng và báo cáo định kỳ** — reference `14` (nguồn: CV 5141/SNNMT-KS ngày 29/12/2025). Hai chiều: (i) SCT **nhận** báo cáo định kỳ của mỏ **nhóm I** (cả GP Bộ cấp và tỉnh cấp) và nước nóng - nước khoáng thiên nhiên tỉnh cấp — hạn nộp trước **15/02** hằng năm, Mẫu 05 Phụ lục IV TT 36/2025 (nhóm II/III/IV đi luồng Sở Xây dựng); (ii) SCT **dùng** bộ sổ sách - chứng từ này khi kiểm tra mỏ và đối chiếu VLNCN: vị trí cân - đo (có chế biến → 02 điểm), loại thiết bị (cân là mặc định; đo đạc chỉ với nước khoáng - nước nóng, đá ốp lát, cát sỏi lòng sông - lòng hồ - biển, KS ghi công suất theo thể tích), sổ khối lượng ghi hàng ngày, sổ hàm lượng hàng tháng, **ngưỡng chênh lệch 10%** buộc giải trình, bản đồ - mặt cắt hiện trạng 01 năm 01 lần chốt 31/12, lưu bản sao tại văn phòng mỏ khi trụ sở khác địa chỉ dự án.

**7. Khoáng sản trong thẩm định dự án, thành lập CCN** — reference `12`, mẫu `06`. Hai chiều: (i) SCT tổng hợp thẩm định CCN (khớp kccn-sct-vn) → đọc, xử lý ý kiến khoáng sản của SNNMT (rà 4 lớp: QĐ 866/QĐ-TTg, QĐ 1626/QĐ-TTg, QĐ 525/QĐ-UBND, khu dự trữ QĐ 1277/QĐ-TTg + GP còn hiệu lực; có chồng lấn → yêu cầu chủ đầu tư điều chỉnh ranh giới); (ii) SCT được hỏi ý kiến dự án khác → trả lời phần khoáng sản nhóm I + khoảng cách an toàn nổ mìn thuộc chức năng, phần rà tổng thể chỉ dẫn về SNNMT.

**9. Nguồn thu đóng góp từ tổ chức, cá nhân khai thác khoáng sản trong đầu tư công** — reference `15` (nguồn: **QĐ 2390/QĐ-UBND ngày 09/7/2026** về kế hoạch đầu tư công trung hạn 2026-2030, Biểu số 04). Tổng nguồn cả giai đoạn **1.594.379 triệu đồng**; đã phân bổ **257.448** cho 03 dự án (đường T2 và đường T12, T19 trong KCN Tằng Loỏng — 70.000; đường dọc sông Hồng Bản Vược – Y Tý — 187.448); **còn 1.336.931 chưa phân bổ**. Dùng khi: trả lời nguồn thu này được chi vào đâu, đề xuất bố trí vốn hạ tầng nơi có hoạt động khoáng sản, soạn báo cáo về nghĩa vụ đóng góp và hiệu quả sử dụng. Gọi đúng tên nguồn, không lẫn với thuế tài nguyên / tiền cấp quyền khai thác.

**10. THU HỒI KHOÁNG SẢN — hoàn thiện trọn bộ hồ sơ** — references `16` (trục chung), `17` (nạo vét lòng hồ thuỷ điện thu hồi cát sỏi), `18` (đất đá thải mỏ, quặng đuôi, KS đi kèm), `19` (toàn văn 7 mẫu Phụ lục III); mẫu `07`, `08`; checklist `checklist-ho-so-thu-hoi-khoang-san.md`; 10 văn bản thật tại `vi-du-thuc-te/`.

Ba câu phải trả lời trước mọi việc: (i) đây là **thu hồi** (giấy xác nhận đăng ký) chứ không phải **khai thác/khai thác tận thu** (giấy phép); (ii) thuộc điểm nào của khoản 1 Điều 75 → quyết định luồng **Điều 97** (trong dự án đầu tư khai thác KS) hay **Điều 98** (nạo vét, xây dựng công trình, đất ở, đóng cửa mỏ) NĐ 193/2025; (iii) khoáng sản thu hồi **dùng cho chính dự án** (không phải đăng ký, chỉ cập nhật báo cáo định kỳ) hay **cung cấp cho dự án khác** (phải đăng ký). Thẩm quyền cấp giấy xác nhận: **Chủ tịch UBND cấp tỉnh** (SNNMT tham mưu), riêng đất ở - đất nông nghiệp là **Chủ tịch UBND cấp xã**. Từ 01/01/2026 (khoản 23 Điều 1 Luật 147/2025): chỉ còn **một** trường hợp miễn đăng ký (dùng cho chính dự án — điểm a khoản 4 Điều 75), và **nhà thầu thi công** được cấp giấy xác nhận nếu chủ đầu tư, nhà đầu tư không có nhu cầu thu hồi và có văn bản chấp thuận.

Vai SCT — bốn đầu việc, không đùn hết sang SNNMT: (a) **hướng dẫn chủ đập thuỷ điện** phần dự án/kế hoạch nạo vét (Điều 42, khoản 1 Điều 49 NĐ 62/2025; Điều 14 NĐ 67/2018 sửa bởi NĐ 40/2023 — chủ sở hữu công trình quyết định chủ trương đầu tư, **không phải xin giấy phép trong phạm vi bảo vệ đập**; theo CV 216/ATMT-ATĐ ngày 30/01/2026); (b) **trả lời khi SNNMT xin ý kiến** về thiết kế mỏ, sự phù hợp khu vực xin thu hồi so với thiết kế, việc chấp hành quy định khi khai thác; (c) **chấp thuận bằng văn bản** với tư cách cơ quan thẩm định TKCS khi khu vực thi công chồng lấn diện tích đã công nhận kết quả thăm dò (điểm b khoản 3 Điều 97); (d) hướng dẫn **chế biến, xuất khẩu** sản phẩm sau thu hồi.

Bẫy lớn nhất: pháp luật ĐC&KS **không** quy định việc lập, thẩm định, phê duyệt dự án/kế hoạch nạo vét lòng hồ (CV 2419/ĐCKS-PCKS ngày 19/9/2025) → không hứa thẩm định, không đẩy sang SNNMT; chỉ đúng vai hướng dẫn chủ đập theo pháp luật điện lực - an toàn đập.

**11. Ủy viên Hội đồng thẩm định Đề án thăm dò khoáng sản tỉnh — soạn Phiếu đánh giá, nhận xét** — reference `21`, mẫu `09`. Hội đồng thành lập theo **QĐ 777/QĐ-UBND ngày 12/8/2025**; ủy viên của SCT là **PGĐ Hoàng Văn Thuân**. SNNMT gửi văn bản xin ý kiến kèm hồ sơ, đề án; SCT trả lời bằng Phiếu trong **12 ngày làm việc** (điểm b khoản 3 Điều 42 NĐ 193/2025 sửa bởi NĐ 21/2026). SCT KHÔNG thẩm định nội dung địa chất (việc của ủy viên phản biện) và KHÔNG kết luận về hành lang công trình thủy lợi (việc của Phòng QLXDCT-TL&PCTT thuộc SNNMT).

Bốn trục nội dung bắt buộc của Phiếu SCT: (i) **rà tọa độ - diện tích - quy hoạch** (đối chiếu từng điểm khép góc với Phụ lục QĐ trúng đấu giá, tự tính lại diện tích, chồng ranh giới lên QĐ 1626/QĐ-TTg hoặc Phụ lục QĐ 525/QĐ-UBND); (ii) **phương án phát triển khu, cụm công nghiệp** + định hướng địa điểm chế biến sâu; (iii) **quy hoạch và hiện trạng công trình thủy điện, lưới điện** (tra `quy-hoach-ct-vn` reference `03`, viện dẫn Luật Điện lực 2024 + NĐ 62/2025/NĐ-CP); (iv) **vật liệu nổ công nghiệp trong giai đoạn thăm dò** — bắt buộc với đề án mỏ đá phải mở đường công vụ, làm nền khoan (Luật 42/2024 sửa bởi Luật 118/2025, NĐ 181/2024, QCVN 01:2019/BCT). Kèm trục bổ trợ kiểm soát rủi ro "khai thác lậu dưới vỏ bọc thăm dò" (moong khai thác thử, thi công ban đêm trên sông).

Bốn vụ đã thẩm định làm chuẩn đối chiếu: cát sỏi Ngòi Thia (xã Xuân Ái); cát sỏi sông Chảy Bản Mủng - Bản Chuân (xã Xuân Hòa); cát sỏi suối Nhù thôn Ngầu 3 (xã Võ Lao); đá hoa trắng Làng Lạnh III (xã Lục Yên) — bảng tra tại reference `21` mục IV.

## VI. DỮ LIỆU MỎ TRÊN ĐỊA BÀN (reference `10` + thư mục `du-lieu/`)

Ảnh chụp dữ liệu tại thời điểm lập (KHÔNG dùng làm hiện trạng thời sự — luôn hỏi Bạn trước khi đưa số liệu vào văn bản):
- `ds-gp-khai-thac-31-10-2025.csv`: 208 giấy phép khai thác toàn tỉnh (137 vùng Yên Bái cũ + 71 vùng Lào Cai cũ; 137 tỉnh cấp + 70 Bộ cấp; nhiều nhất: đá VLXDTT 50, cát sỏi 37, đá vôi trắng 35, quặng sắt 29, apatit 12).
- `ds-gp-tham-do-yen-bai-6-2025.csv`: 43 GP thăm dò vùng Yên Bái cũ (toàn bộ đã hết hạn tại thời điểm thống kê).
- `theo-doi-phap-ly-mo-khai-thac-4-2026.csv`: bảng theo dõi 209 mỏ với các cột hồ sơ pháp lý (nộp thiết kế mỏ, TB GĐĐH mỏ, bàn giao mốc, trạm cân, camera, ký quỹ, thuê đất, GP VLNCN) — cập nhật đến 28/4/2026, dấu "a" = đã có.

## VII. NGƯỜI KÝ, NGƯỜI SOẠN, KÝ HIỆU (khớp `sct-laocai-org-vn`)

- PGĐ phụ trách khoáng sản: **Hoàng Văn Thuân** ký KT. GIÁM ĐỐC các văn bản chuyên ngành; Tờ trình UBND tỉnh, báo cáo quan trọng: GĐ **Hoàng Chí Hiền**.
- PTP kiểm duyệt lĩnh vực khoáng sản, hóa chất: **Nguyễn Hồng Vân**.
- Chuyên viên (dòng Lưu): **CN(Dũng)** — thẩm định công trình/khoáng sản, kiểm tra mỏ; **CN(Nhung)** — khoáng sản chế biến - luyện kim; **CN(Khôi)** — khi gắn VLNCN/GCN huấn luyện VLNCN. Ví dụ: `Lưu: VT, CN(Dũng).`
- Ký hiệu: công văn `/SCT-CN`; báo cáo `/BC-SCT`; kế hoạch `/KH-SCT`; tờ trình `/TTr-SCT`.
- Soạn docx qua `vbhc-vn`; PDF đến chạy GATE `vbhc-pdf-reader-vn` (extract_metadata.py) trước khi trích số/ngày.

## VIII. QUY TRÌNH CHUẨN XỬ LÝ MỘT VIỆC KHOÁNG SẢN

```
B0 GATE PDF        → trích đúng số/ngày/người ký văn bản đến (vbhc-pdf-reader-vn)
B1 GATE VAI        → mục II: việc của SCT? chủ trì hay phối hợp? Không của SCT → nêu đúng
                     cơ quan có thẩm quyền, soạn văn bản chuyển/phúc đáp đúng vai
B2 GATE THỜI KỲ    → mục III: chọn bộ căn cứ theo ngày phát sinh
B3 GATE NHÓM KS    → mục IV: nhóm I/II/III/IV quyết định thẩm quyền và plugin liên kết
B4 NGHIỆP VỤ       → mục V: chọn nghiệp vụ 1-10, mở reference tương ứng
                     Việc thu hồi khoáng sản → thêm GATE LUỒNG: Điều 97 hay Điều 98?
                     dùng cho chính dự án hay bán ra ngoài? (reference 16 mục III)
                     Xin ý kiến đề án thăm dò (HĐ 777) → nghiệp vụ 11, reference 21:
                     phủ đủ 4 trục (tọa độ-quy hoạch · KCN/CCN · thủy điện-lưới điện · VLNCN)
B5 SOẠN VĂN BẢN    → mẫu tại mau-van-ban/ + thể thức vbhc-vn; người ký mục VII
B6 QA              → render soi ảnh từng trang; đối chiếu checklist; số liệu mỏ chưa
                     xác minh → để trống + hỏi Bạn
```

## IX. NGUYÊN TẮC BẤT BIẾN

1. **Không bịa số/ngày văn bản.** Văn bản chưa xác minh (kể cả nghị định xử phạt mới, quyết định phân công nội bộ tỉnh) → để trống, ghi chú đề nghị Bạn cung cấp.
2. **Không dùng dữ liệu `du-lieu/` làm hiện trạng thời sự** — chỉ dùng làm nền tra cứu; số liệu đưa vào văn bản chính thức phải được Bạn xác nhận.
3. **Không lấn vai SNNMT/SXD** — mọi câu chữ về cấp phép thăm dò/khai thác/đóng cửa mỏ đều ở thế "phối hợp/tham gia ý kiến".
4. **Câu ranh giới trách nhiệm** trong biên bản, báo cáo kiểm tra: doanh nghiệp chịu trách nhiệm về tính chính xác của hồ sơ, số liệu cung cấp; kết quả kiểm tra không thay thế nghĩa vụ chấp hành pháp luật của doanh nghiệp.
5. **Mọi nội dung xuất ra không dùng ký hiệu markdown**; file docx TNR 14pt, tên file `YYYY.MM.DD. Tên đầy đủ có dấu.docx`.

## X. CÂY THƯ MỤC

```
references/   01 khung pháp lý + GATE · 02 phân vai · 03 phân nhóm + thẩm quyền
              04 KH quản lý rủi ro · 05 KTAT + huấn luyện · 06 chế biến
              07 nghĩa vụ DN + kiểm soát trữ lượng · 08 kiểm tra xử phạt
              09 chỉ đạo của tỉnh · 10 dữ liệu mỏ · 11 liên kết plugin
              12 khoáng sản trong thẩm định dự án/CCN · 13 báo cáo năm + số liệu 2025
              14 thống kê - kê khai - kiểm soát sản lượng + báo cáo định kỳ (CV 5141)
              15 nguồn thu đóng góp KS trong đầu tư công (QĐ 2390/2026)
              16 THU HỒI KHOÁNG SẢN — trục chung: 5 trường hợp Điều 75, thẩm quyền,
                 hai luồng hồ sơ Điều 97/98, trình tự - thời hạn, nghĩa vụ Điều 76,
                 bộ mẫu Phụ lục III TT 36/2025, 7 bẫy
              17 nạo vét lòng hồ thuỷ điện kết hợp thu hồi cát, sỏi (CV 216/ATMT-ATĐ,
                 CV 2419/ĐCKS-PCKS, NĐ 62/2025, NĐ 67/2018 sửa bởi NĐ 40/2023)
              18 thu hồi đất đá thải mỏ, quặng đuôi, KS đi kèm trong mỏ đang hoạt động
                 (Điều 97 NĐ 193, khoản 9 Điều 4 Luật 147/2025, tiền cấp quyền)
              19 TOÀN VĂN Phụ lục III TT 36/2025 (sửa bởi TT 04/2026): 7 mẫu hồ sơ
                 thu hồi 01 · 02 · 03 · 03a · 04 · 05 · 06 + 05 bản vẽ bắt buộc
              20 biên bản thanh tra/kiểm tra — kinh nghiệm từ mẫu thật BB 13A/BB-ĐTT72
                 (Thanh tra tỉnh, vụ Mông Sơn) + checklist đón thanh tra tỉnh
              21 HỘI ĐỒNG THẨM ĐỊNH ĐỀ ÁN THĂM DÒ (QĐ 777/QĐ-UBND) — vai ủy viên SCT:
                 phân vai Hội đồng, 4 trục nội dung Phiếu, 6 lỗi kỹ thuật lặp lại,
                 4 vụ thực tế, kỹ thuật xử lý hồ sơ đến (giải nén, OCR, tính diện tích)
mau-van-ban/  01 CV hướng dẫn - đôn đốc DN · 02 KH + biên bản kiểm tra + BB làm việc chốt kết quả
              03 BC kết quả kiểm tra + tham mưu đình chỉ
              04 tham mưu phê duyệt KH rủi ro hầm lò + GCN KTAT
              05 báo cáo định kỳ + CV phối hợp liên ngành
              06 ý kiến khoáng sản trong thẩm định dự án + xử lý chồng lấn
              07 bộ mẫu thu hồi cát sỏi lòng hồ thuỷ điện (CV hướng dẫn chủ đập,
                 bản đăng ký mẫu 02, CV trả hồ sơ - chỉ dẫn đúng cơ quan)
              08 bộ mẫu thu hồi đất đá thải mỏ (VB đề nghị mẫu 01, báo cáo mẫu 04,
                 yêu cầu bản đồ hiện trạng, VB SCT tham gia ý kiến, CV hướng dẫn DN)
              09 Phiếu đánh giá, nhận xét của ủy viên Hội đồng thẩm định Đề án thăm dò
                 (khung biểu mẫu + khung nội dung I.1/I.2/I.3 + câu chữ mẫu đã dùng)
checklists/   kiểm tra mỏ · hồ sơ pháp lý mỏ · hồ sơ thu hồi khoáng sản
vi-du-thuc-te/ 10 văn bản thật về thu hồi KS — xem 00-MUC-LUC.md
du-lieu/      3 file CSV ảnh chụp dữ liệu giấy phép, theo dõi pháp lý
van-ban-goc/  22 văn bản nguồn đã đối chiếu (gồm CV 5141, CV 6795 của SNNMT và
              BB 13A/BB-ĐTT72 của Thanh tra tỉnh — bản scan, phải render ảnh để đọc)
```
