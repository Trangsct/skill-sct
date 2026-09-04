---
name: hnh-sct-vn
description: "VẬN CHUYỂN HÀNG HÓA NGUY HIỂM (HHNH), Sở Công Thương Lào Cai. Kích hoạt: giấy phép vận chuyển HHNH, GP-SCT, thẩm định hồ sơ, loại 1 (trừ VLNCN, tiền chất thuốc nổ) 2 3 4 5 8 9, xăng dầu, axit, NH3, LPG, người áp tải, NĐ 161/2024. 4 nghiệp vụ: (1) thẩm định, tham mưu cấp/điều chỉnh/cấp lại/thu hồi Giấy phép - cả 7 loại do Giám đốc Sở ký theo ủy quyền QĐ 1696 (sửa đổi tại QĐ 2848/QĐ-UBND ngày 14/8/2026), mã TTHC 1.013340/50/51 và 1.014967/68/69; (2) hướng dẫn doanh nghiệp thủ tục, hồ sơ, điều kiện phương tiện, người lái xe, người áp tải, tập huấn, bao bì, biểu trưng; (3) kiểm tra chuyên ngành (NĐ 217/2025); (4) báo cáo. Kèm văn bản gốc, biểu mẫu, checklist, ví dụ thực tế: Giấy phép đã cấp, biên bản thẩm định, bộ hồ sơ doanh nghiệp mẫu chuẩn nhóm loại 8 (axit ăn mòn, công-ten-nơ bồn ISO tank). Chuyên sâu xuyên biên giới Việt - Trung, cửa khẩu Kim Thành. Từ khóa thêm: NĐ 105/2025, TT 26/2026, Điều 51 Luật 36/2024, QĐ 1213/QĐ-BCT, Phụ lục I."
---

# hnh-sct-vn - Plugin lớn HHNH: cấp phép, thẩm định, trả lời DN, kiểm tra, báo cáo (Sở Công Thương Lào Cai)

## I. KHI NÀO DÙNG SKILL NÀY

Kích hoạt skill khi xử lý bất kỳ việc nào sau đây:

- Thẩm định hồ sơ và tham mưu cấp mới, cấp điều chỉnh, cấp lại, thu hồi Giấy phép vận chuyển hàng hóa nguy hiểm (sau đây gọi tắt là Giấy phép) loại 1 (trừ vật liệu nổ công nghiệp, tiền chất thuốc nổ), loại 2, loại 3, loại 4, loại 5, loại 8, loại 9. (Cập nhật: từ 29/5/2026 loại 5 và loại 8 cũng do UBND cấp tỉnh cấp - xem mục III.)
- Trả lời, giải đáp, hướng dẫn cho doanh nghiệp, hợp tác xã, hộ kinh doanh trên địa bàn tỉnh về thủ tục, hồ sơ, điều kiện.
- Soạn công văn hướng dẫn, thông báo bổ sung hồ sơ, tờ trình, quyết định, báo cáo liên quan đến lĩnh vực vận chuyển hàng hóa nguy hiểm.
- Xác định thẩm quyền cấp phép, phân định ranh giới với cơ quan khác (Bộ Công an, Bộ Quốc phòng, Cục Hóa chất - Bộ Công Thương, cơ quan năng lượng nguyên tử).
- Xử lý các trường hợp đặc thù: doanh nghiệp hoặc phương tiện nước ngoài; vận chuyển xuyên biên giới Việt - Trung qua cửa khẩu Lào Cai; vận chuyển qua hầm, phà; vận chuyển bằng đường sắt, đường thủy nội địa; trường hợp miễn cấp phép theo ngưỡng khối lượng.
- Tư vấn về tập huấn an toàn hàng hóa nguy hiểm, người áp tải, bao bì, nhãn, biểu trưng nguy hiểm.
- **Thẩm định hồ sơ:** áp dụng cây quyết định, checklist và Phiếu thẩm định (reference 11).
- **Kiểm tra chuyên ngành:** xây dựng kế hoạch, tổ chức cuộc kiểm tra việc chấp hành pháp luật vận chuyển HHNH, lập biên bản kiểm tra, kết luận (reference 12 - theo NĐ 217/2025, KHÔNG còn "thanh tra chuyên ngành").
- **Báo cáo cấp trên, thống kê:** báo cáo định kỳ, đột xuất (sự cố), chuyên đề; bộ chỉ tiêu thống kê (reference 13).
- **Tra cứu văn bản gốc:** mở bộ văn bản gốc kèm theo trong `van-ban-goc/` theo mục lục (reference 15).

**Xử phạt vi phạm hành chính (lập biên bản VPHC, ra quyết định XPVPHC) KHÔNG xử lý trong plugin này** mà thuộc **plugin xử phạt riêng `xp-sct-vn`** (dùng chung cả Sở). Plugin HHNH chỉ thực hiện **thu hồi Giấy phép** (biện pháp của cơ quan cấp phép - reference 06) và **chuyển hồ sơ/kiến nghị** khi phát hiện vi phạm khi kiểm tra (reference 12).

### Liên kết hệ sinh thái plugin/skill (gọi đúng plugin khi việc chạm ranh giới)

| Tình huống chạm ranh giới | Plugin/skill gọi kèm | Nội dung liên quan |
|---|---|---|
| Soạn văn bản kết quả (CV, GP, TTr, QĐ, BC) | `vbhc-vn` | Thể thức NĐ 30/2020, template Chế độ A/B, tên file chuẩn |
| Nhận PDF văn bản đến (hồ sơ DN, văn bản chỉ đạo) | `vbhc-pdf-reader-vn` | Đọc đúng số/ngày/người ký từ file gốc |
| Xác định người ký, dòng Lưu CN(tên), phòng chủ trì | `sct-laocai-org-vn` | Phân công BGĐ, chuyên viên QLCN |
| DN vận chuyển hóa chất loại 5, 8, khí độc 2.3 (NH3, clo, axit): kiểm tra nghĩa vụ hóa chất song song | `hc-sct-vn` | GCN đủ điều kiện SX/KD hóa chất; Kế hoạch phòng ngừa, ứng phó sự cố hóa chất; khai báo hóa chất nhập khẩu; huấn luyện an toàn hóa chất (Luật 69/2025, NĐ 24-26/2026). Phương án ứng cứu "sự cố hóa chất" điểm d khoản 1 Điều 15 NĐ 161 đối chiếu chéo với KH phòng ngừa sự cố hóa chất của DN; SDS/MSDS dùng chung để phân loại |
| VLNCN, tiền chất thuốc nổ (loại 1 đã trừ) | `sd-vlncn-sct-vn`, `kho-vlncn-sct-vn`, `hl-vlncn-sct-vn` | GP sử dụng VLNCN, PANM, kho, huấn luyện KTAT - pháp luật chuyên ngành riêng; XNK VLNCN thuộc tỉnh từ 01/7/2026 (Điều 27 TT 26/2026) |
| Điều kiện PCCC vận chuyển, Điều 44 NĐ 105/2025, cửa hàng xăng dầu/kho LPG của DN | `pccc-sct-vn` | Nội dung chi tiết Điều 44; PCCC 8 lĩnh vực ngành Công Thương |
| Điểm đến/kho hàng trong KCN, CCN (Tằng Loỏng...) | `kcn-ccn-vn` | Vị trí xã, hiện trạng, đầu mối BQL |
| Lập biên bản VPHC, ra QĐ xử phạt | `xp-sct-vn` (plugin riêng) | Toàn bộ trình tự xử phạt |
| Công trình xây dựng liên quan (kho, trạm chiết nạp của DN vận chuyển) | `xd-sct-vn` | Thẩm định thiết kế, KTCTNT công trình công nghiệp |

## II. KHUNG PHÁP LÝ — danh mục rút gọn (toàn văn diễn giải từng văn bản: `references/18-khung-phap-ly-tong-hop.md`)

Toàn bộ số/ngày dưới đây đã xác minh từ văn bản gốc. TUYỆT ĐỐI không thay đổi, không tự điền số/ngày khác. Khi cần dẫn điều khoản, mốc hiệu lực, nội dung chuyển tiếp: mở ref 18 (và ref 01, 09).

- **1.** Luật Trật tự, an toàn giao thông đường bộ số 36/2024/QH15 ngày 27/6/2024 (hiệu lực 01/01/2025)
- **1a.** Luật Đường bộ số 35/2024/QH15 ngày 27/6/2024
- **2.** Nghị định số 161/2024/NĐ-CP ngày 18/12/2024 (hiệu lực 01/01/2025)
- **3.** Nghị định số 34/2024/NĐ-CP ngày 31/3/2024 (hiệu lực 15/5/2024)
- **4.** Luật Phòng cháy, chữa cháy và cứu nạn, cứu hộ số 55/2024/QH15 ngày 29/11/2024 (hiệu lực 01/7/2025)
- **5.** Nghị định số 105/2025/NĐ-CP ngày 15/5/2025 (hiệu lực 01/7/2025)
- **6.** Nghị định số 146/2025/NĐ-CP ngày 12/6/2025
- **7.** Nghị định số 139/2025/NĐ-CP ngày 12/6/2025
- **8.** Thông tư số 38/2025/TT-BCT ngày 19/6/2025 (hiệu lực 01/7/2025)
- **9.** Thông tư số 26/2026/TT-BCT ngày 20/5/2026 (hiệu lực **29/5/2026**, do Thứ trưởng Phan Thị Thắng ký)
- **10.** Thông tư số 15/2026/TT-BCT ngày 25/3/2026 (hiệu lực 10/4/2026)
- **11.** Nghị quyết số 19/2026/NQ-CP
- **12.** Nghị quyết số 66.18/2026/NQ-CP ngày 18/5/2026
- **13.** Văn bản số 2265/BCT-ATMT ngày 02/4/2026
- **13a.** Quyết định số 1213/QĐ-BCT ngày 22/5/2026
- **14.** Văn bản của Chủ tịch UBND tỉnh Lào Cai
- **15.** Quyết định số 1696/QĐ-UBND ngày 15/5/2026 của UBND tỉnh Lào Cai
- **15a.** QUYẾT ĐỊNH SỐ 2848/QĐ-UBND NGÀY 14/8/2026 CỦA UBND TỈNH LÀO CAI
- **16.** Nghị định thư giữa Chính phủ Việt Nam và Chính phủ Trung Quốc
- **17.** Nghị định số 158/2024/NĐ-CP
- **18.** Luật Thanh tra số 84/2025/QH15 ngày 25/6/2025 (hiệu lực 01/7/2025)
- **19.** Nghị định số 217/2025/NĐ-CP ngày 05/8/2025

## III. CHUỖI THẨM QUYỀN - HIỂU ĐÚNG ĐỂ KHÔNG NHẦM (cốt lõi nhất)

Đây là nội dung dễ sai nhất và là lý do skill này tồn tại. Nếu chỉ đọc Điều 14 Nghị định 161/2024/NĐ-CP sẽ kết luận SAI rằng Bộ Công an cấp loại 1, 2, 3, 4, 9. Thực tế thẩm quyền đã dịch chuyển qua một chuỗi văn bản:

**Bộ Công an (theo Điều 14 NĐ 161/2024 gốc) → Bộ Công Thương (NĐ 105/2025 bãi bỏ khoản 1 Điều 14, Điều 19 và sửa khoản 3 Điều 14 NĐ 161; Điều 44 NĐ 105/2025) → phân cấp cho UBND cấp tỉnh (Điều 8 TT 38/2025, sửa bởi Điều 3 TT 15/2026, nay là Điều 25 TT 26/2026 - bản hiện hành) → UBND tỉnh Lào Cai ủy quyền cho Giám đốc Sở Công Thương.**

Lưu ý cập nhật (tháng 8/2026): bản sửa Điều 8 TT 38/2025 hiện hành là bản tại **Điều 25 Thông tư 26/2026/TT-BCT** (hiệu lực 29/5/2026), thay cho hiệu lực bản sửa tại Điều 3 TT 15/2026. **Thay đổi quan trọng từ 29/5/2026:** ngoài loại 1 (trừ VLNCN/tiền chất thuốc nổ), 2, 3, 4, 9 (phân cấp theo khoản 2 Điều 8), TT 26/2026 còn giao **loại 5 và loại 8 cho UBND cấp tỉnh** (khoản 1 Điều 8). Tức UBND cấp tỉnh nay cấp Giấy phép cho **loại 1 trừ VLNCN/tiền chất thuốc nổ, 2, 3, 4, 5, 8, 9**. Cục Hóa chất - Bộ Công Thương KHÔNG còn là cơ quan cấp loại 5, 8. Tại Lào Cai: loại 1,2,3,4,9 đã ủy quyền Giám đốc Sở theo QĐ 1696; **loại 5,8 được ủy quyền bổ sung cho Giám đốc Sở bằng QĐ 2848/QĐ-UBND ngày 14/8/2026 sửa đổi, bổ sung QĐ 1696 (mục II.15a) - từ 14/8/2026 Giám đốc Sở ký cả 7 loại.**

Phân định thẩm quyền cấp Giấy phép hiện hành theo loại hàng:

| Loại hàng hóa nguy hiểm | Cơ quan cấp Giấy phép hiện hành |
|---|---|
| Loại 1 (trừ vật liệu nổ công nghiệp, tiền chất thuốc nổ), loại 2, loại 3, loại 4, loại 9 | UBND cấp tỉnh (Lào Cai: ủy quyền Giám đốc Sở Công Thương) cho tổ chức, cá nhân đặt trụ sở chính hoặc chi nhánh trên địa bàn tỉnh - khoản 2 Điều 8 TT 38/2025 (sửa bởi Điều 25 TT 26/2026) |
| Loại 5, loại 8 | **UBND cấp tỉnh** - khoản 1 Điều 8 TT 38/2025 (sửa bởi Điều 25 TT 26/2026), hiệu lực 29/5/2026; khoản 1 KHÔNG kèm điều kiện trụ sở/chi nhánh. Lào Cai: **từ 14/8/2026 Giám đốc Sở ký theo ủy quyền bổ sung tại QĐ 2848/QĐ-UBND (mục II.15a)**, mã TTHC 1.013340/1.013350/1.013351. Giai đoạn 29/5-13/8/2026: Sở thẩm định, trình UBND tỉnh ký; trước 29/5/2026 do Cục Hóa chất cấp |
| Vật liệu nổ công nghiệp, tiền chất thuốc nổ (thuộc loại 1) | Theo pháp luật chuyên ngành về vật liệu nổ công nghiệp (skill `pccc-sct-vn` mục VLNCN) - KHÔNG thuộc thủ tục này |
| Loại 6 (chất độc, chất gây nhiễm bệnh) | Theo phân công tại NĐ 161 (Bộ Y tế, Bộ Nông nghiệp và Môi trường tùy nhóm) |
| Loại 7 (chất phóng xạ) | Theo pháp luật về năng lượng nguyên tử |
| Hóa chất bảo vệ thực vật | UBND cấp tỉnh (theo khoản 4 Điều 14 NĐ 161 - đầu mối Sở Nông nghiệp và Môi trường, không thuộc Sở Công Thương) |
| Tổ chức, doanh nghiệp thuộc Bộ Quốc phòng | Bộ Quốc phòng |

**Nguyên tắc bất biến về thẩm quyền:**
- Phạm vi Sở Công Thương Lào Cai xử lý gồm loại 1 (trừ VLNCN, tiền chất thuốc nổ), 2, 3, 4, 5, 8, 9 - loại 1,2,3,4,9 Sở ký theo ủy quyền QĐ 1696; loại 5, 8 Sở ký theo ủy quyền bổ sung tại QĐ 2848/QĐ-UBND từ 14/8/2026. Câu hỏi về loại 6, loại 7, hóa chất BVTV, VLNCN/tiền chất thuốc nổ phải chuyển đúng đầu mối, không tự nhận.
- Điều kiện địa bàn: tổ chức, cá nhân phải đặt **trụ sở chính HOẶC chi nhánh** trên địa bàn tỉnh Lào Cai.
- Giấy phép **có hiệu lực trên toàn quốc** (không bị giới hạn trong tỉnh), thời hạn theo đề nghị của người vận tải nhưng **tối đa 24 tháng và không quá niên hạn sử dụng phương tiện**.

**Ai ký Giấy phép - theo QĐ 1696/QĐ-UBND ngày 15/5/2026, được sửa đổi, bổ sung tại QĐ 2848/QĐ-UBND ngày 14/8/2026:**
- **Loại 1 (trừ VLNCN/tiền chất thuốc nổ), 2, 3, 4, 9 → mô hình ủy quyền:** lãnh đạo Sở ký trực tiếp Giấy phép, dùng hình thức văn bản và con dấu của Sở Công Thương (theo QĐ 1696). Thực tế các Giấy phép đã phát hành do **KT. GIÁM ĐỐC - PHÓ GIÁM ĐỐC Hoàng Văn Thuân** ký (PGĐ phụ trách HHNH, theo phân công nội bộ) - xem thể thức chuẩn tại reference 16 mục 2 và bản gốc tại vi-du-thuc-te/giay-phep-da-cap/.
- **Loại 5, 8 → từ 14/8/2026 cùng mô hình ủy quyền:** Giám đốc Sở ký theo ủy quyền như loại 1,2,3,4,9 - con dấu Sở; căn cứ trong Giấy phép dẫn "Quyết định số 1696/QĐ-UBND ngày 15/5/2026... (được sửa đổi, bổ sung tại Quyết định số 2848/QĐ-UBND ngày 14/8/2026...)" và **khoản 1** Điều 8 TT 38/2025 (sửa bởi Điều 25 TT 26/2026). Hồ sơ tiếp nhận trong giai đoạn 29/5-13/8/2026: Sở thẩm định, trình UBND tỉnh ký.

Mã TTHC đã công bố (theo Phụ lục QĐ 2848/QĐ-UBND, nguồn QĐ 1213/QĐ-BCT ngày 22/5/2026): loại 1 (trừ VLNCN/TCTN), 2, 3, 4, 9: cấp mới 1.014967; cấp điều chỉnh 1.014968; cấp lại 1.014969. **Loại 5, 8: cấp mới 1.013340; cấp điều chỉnh 1.013350; cấp lại 1.013351.**

## IV. CÁC REFERENCE FILES (đọc khi cần đào sâu)

Đọc file tương ứng trong thư mục `references/` khi xử lý chi tiết:

- `01-chuoi-tham-quyen.md` - Chi tiết chuỗi thẩm quyền, căn cứ từng văn bản, ai ký, mã TTHC, xử lý câu hỏi "ai cấp loại này".
- `02-thanh-phan-ho-so.md` - Thành phần hồ sơ cấp mới, cấp điều chỉnh, cấp lại; các mẫu Phụ lục; checklist thẩm định hồ sơ.
- `03-trinh-tu-thu-tuc.md` - Trình tự, thời hạn giải quyết (05/03/02 ngày làm việc), các bước nội bộ, cách nộp hồ sơ, xử lý hồ sơ thiếu.
- `04-dieu-kien-tuan-thu.md` - Điều kiện phương tiện, người lái xe/người áp tải, tập huấn an toàn, bao bì - thùng chứa, nhãn, biểu trưng nguy hiểm.
- `05-trach-nhiem-cac-ben.md` - Trách nhiệm người thuê vận tải, người vận tải, người lái xe, người áp tải (Điều 28-30 NĐ 161); nghĩa vụ song song theo Luật Đường bộ 35/2024 (giấy vận tải, đóng gói - ký/mã hiệu, cử người áp tải); hồ sơ vận chuyển; chế độ báo cáo, lưu giữ.
- `06-thu-hoi-mien-cap.md` - Các trường hợp thu hồi Giấy phép và hệ quả (30/60 ngày); các trường hợp miễn cấp Giấy phép theo ngưỡng khối lượng; từ chối cấp phép.
- `07-truong-hop-dac-thu.md` - Doanh nghiệp/phương tiện nước ngoài; vận chuyển xuyên biên giới Việt - Trung qua Lào Cai; qua hầm/phà; đường sắt, đường thủy; chuyển tiếp giấy phép cũ.
- `08-faq-doanh-nghiep.md` - Bộ câu hỏi - trả lời mẫu để giải đáp doanh nghiệp; ngôn ngữ hướng dẫn chuẩn.
- `09-cap-nhat-phap-ly-2026.md` - **Cập nhật pháp lý mới nhất (NĐ 105/2025, TT 38/2025, TT 15/2026, TT 26/2026):** nội dung Điều 44 khoản 4 NĐ 105, Điều 25 + Điều 26 TT 26/2026, thẩm quyền hiện hành (loại 5,8 chuyển về UBND cấp tỉnh), người áp tải theo khối lượng. ĐỌC FILE NÀY trước khi kết luận thẩm quyền/áp tải.
- `10-danh-muc-phu-luc-1.md` - **Cấu trúc Danh mục Phụ lục I NĐ 161 (đã đối chiếu bản gốc):** Danh mục chỉ có 6 cột, KHÔNG có cột ngưỡng khối lượng (cột cuối là số hiệu nguy hiểm). Kèm bảng tra nhanh số UN/loại/số hiệu nguy hiểm các mặt hàng thường gặp ở Lào Cai (trích đúng Phụ lục I).
- `11-tham-dinh-quy-trinh.md` - **Quy trình thẩm định:** cây quyết định 6 bước, checklist thẩm định chi tiết từng tài liệu, mẫu Phiếu thẩm định nội bộ, 8 lỗi thẩm định thường gặp. ĐỌC khi thẩm định hồ sơ.
- `12-kiem-tra-chuyen-nganh.md` - **Kiểm tra chuyên ngành (NĐ 217/2025):** điểm cốt lõi "kiểm tra" thay "thanh tra"; phạm vi/đối tượng/hình thức; trình tự cuộc kiểm tra; checklist nội dung kiểm tra HHNH; mẫu Biên bản kiểm tra. ĐỌC khi tổ chức kiểm tra.
- `13-bao-cao-thong-ke.md` - **Báo cáo cấp trên:** các loại báo cáo và đầu mối; bộ chỉ tiêu thống kê chuẩn; khung báo cáo định kỳ/đột xuất. ĐỌC khi lập báo cáo.
- `14-bo-mau-van-ban.md` - **Bộ mẫu văn bản kết quả:** thông báo bổ sung, từ chối, tờ trình cấp phép, thông báo CSGT, quyết định thu hồi, trả lời doanh nghiệp, quyết định/kế hoạch kiểm tra, biên bản kiểm tra, chuyển hồ sơ, báo cáo; kèm bảng tra "việc→mẫu→reference". (Biên bản VPHC/QĐ XPVPHC thuộc plugin xử phạt riêng.)
- `15-muc-luc-van-ban-goc.md` - **Mục lục tra cứu bộ văn bản gốc** kèm trong `van-ban-goc/` và `vi-du-thuc-te/`: bảng ánh xạ từng file → nội dung → reference dùng. ĐỌC khi cần mở nguyên văn một văn bản.
- `16-thuc-tien-cap-phep-sct.md` - **Thực tiễn cấp phép tại Sở (đúc kết hồ sơ đã xử lý 2026):** bảng tiền lệ nội bộ (An Khang, Thái Thịnh, Bắc Cường, Apatit, Sợi Phương Nam, HNL...); thể thức Giấy phép thực tế (số /GP - SCT, người ký, nơi nhận, Lưu VT, BP1C, CN); quy trình 6 bước sau ủy quyền; các quyết định nghiệp vụ đã chốt (thời hạn GP khống chế theo kiểm định, GPKDVT, lỗi phân loại điển hình). mục 10 - bộ hồ sơ mẫu loại 5 và mẫu riêng Chi nhánh số 1 Sợi Phương Nam (lỗi lặp lại của đơn vị, trọng tải xe biển Trung Quốc, chữa cháy chất oxy hóa, quy tắc bôi đỏ bản giao doanh nghiệp). ĐỌC TRƯỚC KHI SOẠN bất kỳ văn bản kết quả nào.
- `17-xuyen-bien-gioi-viet-trung.md` - **Hồ sơ có yếu tố nước ngoài/xuyên biên giới Việt - Trung (chuyên sâu):** cây quyết định thẩm quyền (khoản 1 vs khoản 2 Điều 8 - loại 5,8 không có điều kiện địa bàn); giấy phép loại D của Sở Xây dựng; checklist riêng cho xe biển Trung Quốc; tiền lệ 4 vụ việc. ĐỌC khi hồ sơ có xe biển nước ngoài, pháp nhân nước ngoài hoặc tuyến qua cửa khẩu.
- `18-khung-phap-ly-tong-hop.md` - **Khung pháp lý HHNH tổng hợp 19 văn bản** (toàn văn diễn giải, mốc hiệu lực, chuyển tiếp; tách từ SKILL.md mục II 02/9/2026).
- `19-nguyen-tac-nghiep-vu-bat-bien.md` - ⭐ **21 nguyên tắc nghiệp vụ bất biến** (toàn văn; BẮT BUỘC đọc trước khi thẩm định/soạn — tách từ SKILL.md mục VII 02/9/2026).
- `20-csdl-gp-hhnh-da-cap.md` - **Ảnh chụp tự động CSDL trang vlncn-laocai** (máy sinh, không sửa tay, đồng bộ 18h40 hằng ngày): bảng mọi GP vận chuyển HHNH Sở đã phát hành có trên trang (số, ngày, hạn, loại, tổ chức, mã số DN, hàng hóa - số UN, số phương tiện, liên kết PDF ký số), thống kê theo loại/tháng, cách trang hỗ trợ nghiệp vụ. ĐỌC khi cần tra "GP số mấy, cấp ngày nào, còn hạn không, tổ chức nào đã có GP".
- `mau-ho-so/` - Bộ biểu mẫu dựng trực tiếp từ hồ sơ thực tế (giữ nguyên cấu trúc, nội dung đã chuyển thành placeholder): Mẫu 1 Giấy đề nghị (Phụ lục IV), Mẫu 2 Bảng kê phương tiện, Mẫu 3 Bảng kê người lái xe + người áp tải, Mẫu 4 Phương án tổ chức vận chuyển (Phụ lục V), Mẫu 5 Giấy phép vận chuyển HHNH của Sở Công Thương, Mẫu 6 Biên bản thẩm định hồ sơ cấp Giấy phép (văn bản NỘI BỘ của Sở, bản chuẩn văn phong 24/7/2026 - xe biển Việt Nam, thẩm định tại trụ sở doanh nghiệp; khi dùng cho vụ mới thay toàn bộ thông tin doanh nghiệp/phương tiện/nhân sự theo hồ sơ thực tế và cập nhật tên thành viên Đoàn theo phân công hiện hành), kèm `00-huong-dan-lap-ho-so.md`.

## IV-a. VÍ DỤ THỰC TẾ KÈM THEO (`vi-du-thuc-te/`) - cập nhật 8/2026

Ba nhóm ví dụ thực tế, ưu tiên dùng làm bản gốc khi soạn văn bản (Chế độ B):
- `giay-phep-da-cap/` - hồ sơ Sở đã phát hành, LÀ MẪU CHUẨN CỦA SỞ (luôn dựng văn bản mới từ các file này):
  - `GP-ThaiThinh-xangdau-loai3-072026.docx`, `GP-SoiPhuongNam-NH3-loai2-xuyenbiengioi-072026.docx` - 2 Giấy phép (Thái Thịnh loại 3; Sợi Phương Nam NH3 loại 2 xuyên biên giới, 16 xe biển Trung Quốc). MẪU GIẤY PHÉP CHUẨN - luôn dựng GP mới từ đây.
  - `Bien-ban-tham-dinh-SCT-ThaiThinh-xangdau-loai3.docx` - **MẪU BIÊN BẢN THẨM ĐỊNH CHUẨN CỦA SỞ** (dùng cho loại 1, 2, 3, 4, 9). Khi soạn Biên bản thẩm định BẮT BUỘC dựng từ file này (Chế độ B, giữ nguyên thể thức). Cấu trúc chi tiết mẫu Sở: xem reference 16 mục 3.
- `cuc-hoa-chat/` - bộ hồ sơ nghiệp vụ của Cục Hóa chất (checklist thẩm định chi tiết, Phiếu trình, Biên bản thẩm định loại 5-8, GP mẫu loại 8, CV bổ sung hồ sơ xuyên biên giới) - **CHỈ dùng tham chiếu cho loại 5, 8** (Sở trình UBND tỉnh ký) và hồ sơ Việt - Trung. **KHÔNG dùng Biên bản thẩm định của Cục Hóa chất làm mẫu cho loại 1,2,3,4,9** - loại này dùng mẫu Biên bản của Sở ở `giay-phep-da-cap/`.
- `tien-anh-lpg-xangdau-072026/` - **02 Giấy phép cấp cùng đợt cho 01 doanh nghiệp** (Công ty TNHH MTV thương mại Tiến Anh): LPG loại 2 đi ở **dạng chai chứa** trên xe tải có mui, và xăng + dầu diesel loại 3 trên tổ hợp đầu kéo - sơ mi rơ moóc xi téc. ĐỌC khi hàng KHÔNG đi bằng xi téc/bồn (cột "Khối lượng vận chuyển") hoặc khi một đơn vị nộp nhiều bộ hồ sơ cùng lúc. Kèm README tóm tắt bài học; chi tiết reference 16 mục 8.
- `ha-tan-axit-loai8-082026/` - **BỘ HỒ SƠ DOANH NGHIỆP MẪU CHUẨN CHO LOẠI 8** (Công ty TNHH thương mại du lịch và vận tải Hà Tân, 8/2026): 04 tệp Giấy đề nghị - Bảng kê người lái xe và người áp tải - Bảng kê phương tiện - Phương án, cho 09 chất ăn mòn (HCl, NaOH, hypoclorit, H2SO4, 03 phân mức HNO3, HNO3 khói đỏ, N.O.S.), hàng đi trong **công-ten-nơ bồn (ISO tank)** trên tổ hợp đầu kéo - sơ mi rơ moóc chở container. DÙNG LÀM BẢN GỐC khi hướng dẫn doanh nghiệp lập hồ sơ loại 8 và khi rà soát, chỉnh sửa hồ sơ doanh nghiệp nộp. Kèm README nêu 06 điểm phải yêu cầu bổ sung và chuẩn thể thức của bộ; chi tiết reference 16 mục 9.
- `soi-phuong-nam-canxi-hypoclorit-loai5-092026/` - **BỘ HỒ SƠ MẪU CHUẨN CHO LOẠI 5 và MẪU RIÊNG CỦA CHI NHÁNH SỐ 1 SỢI PHƯƠNG NAM** (03/9/2026, đơn vị nộp hồ sơ thường xuyên - vụ thứ ba trong năm sau Argon và NH3): 04 tệp doanh nghiệp (Giấy đề nghị - Bảng kê phương tiện - Bảng kê người lái xe và người áp tải - Phương án) cho canxi hypoclorit khô UN 1748 và ngậm nước UN 2880 (loại 5, nhóm 5.1, số hiệu nguy hiểm 50), hàng đóng thùng nhựa 50 lít xếp trong **công-ten-nơ 40 feet** trên tổ hợp xe **biển Trung Quốc** thuê theo hợp đồng, tuyến trong phạm vi 500 m khu vực cửa khẩu Kim Thành; kèm **công văn hoàn thiện, bổ sung hồ sơ** của Sở. DÙNG LÀM BẢN GỐC khi đơn vị này nộp hồ sơ đợt sau và khi lập hồ sơ loại 5. Kèm README nêu 09 lỗi đã sửa và các lỗi lặp lại của đơn vị; chi tiết reference 16 mục 10.
- `rut-tra-ho-so/` - mẫu CV dừng xử lý/trả hồ sơ và mẫu doanh nghiệp đề nghị rút hồ sơ.

## V. VĂN BẢN GỐC KÈM THEO (`van-ban-goc/`)

Plugin kèm sẵn bộ văn bản gốc để khi làm việc **không phải gửi lại tài liệu**. Tra theo mục lục tại reference 15. Cấu trúc 7 nhóm: `01-luat` (Điều 51 Luật 36/2024; toàn văn Luật Đường bộ 35/2024 bản text); `02-nghi-dinh` (NĐ 161/2024 bản text, 105/2025, 158/2024, Nghị định thư Việt-Trung, NQ 19/2026, NQ 66.18/2026); `03-thong-tu` (TT 26/2026, 15/2026, 37/2020, 37-BGTVT, 23/2024, 16/2018); `04-uy-quyen-quy-trinh` (QĐ 1696 ủy quyền, QĐ 2848/QĐ-UBND ngày 14/8/2026 sửa đổi bổ sung QĐ 1696, Quy trình nội bộ TTHC, Hướng dẫn thủ tục của Sở, CV 2265/BCT, Hiệp định Việt-Trung); `05-phu-luc-bieu-mau` (Phụ lục I-VIII, Điều 6, Điều 15); `06-kiem-tra` (NĐ 217/2025, Luật Thanh tra 84/2025); `07-tham-khao` (UN numbers, ĐLVN kiểm định xi téc, ví dụ cấp phép Cty TQ).

Nguyên tắc: ưu tiên đọc bản **text (.doc/.docx)** để trích nhanh; các bản scan rất nặng (NĐ 161 ~87 MB, Luật TTGT ~64 MB) đã lược bỏ, thay bằng bản text - cần bản có dấu thì tra Cơ sở dữ liệu quốc gia về VBPL. Khi có văn bản mới, bổ sung vào đúng thư mục và cập nhật reference 15.

## VI. BẢN ĐỒ 4 NGHIỆP VỤ - GẶP VIỆC GÌ ĐỌC GÌ

Tra nhanh: nhận yêu cầu → xác định nghiệp vụ → đọc reference tương ứng → soạn kết quả theo `vbhc-vn`.

| Nghiệp vụ | Gặp tình huống | Đọc reference | Mẫu kết quả |
|---|---|---|---|
| **1. Thẩm định hồ sơ** | Có hồ sơ cấp mới/điều chỉnh/cấp lại cần xử lý | 11 (quy trình + checklist mở rộng), 16 (thực tiễn Sở), 02 (hồ sơ), 03 (trình tự), 04 (điều kiện), 10 (Phụ lục I); có yếu tố nước ngoài → 17 | Phiếu thẩm định; mẫu 1, 2, 3, 4 (ref 14); ví dụ thực tế (vi-du-thuc-te/) |
| **2. Trả lời doanh nghiệp** | DN hỏi thủ tục, điều kiện, thẩm quyền, miễn cấp phép | 08 (FAQ), 01 (thẩm quyền), 06 (miễn cấp), 07 (đặc thù), 17 (Việt - Trung) | Mẫu 7 (reference 14) |
| **3. Kiểm tra chuyên ngành** | Lập kế hoạch/tổ chức kiểm tra; phát hiện vi phạm | 12 (kiểm tra), 04 (điều kiện), 05 (trách nhiệm) | Mẫu 8, 9, 10 (reference 14) |
| **4. Báo cáo cấp trên** | Báo cáo định kỳ/đột xuất/chuyên đề; thống kê | 13 (báo cáo) | Mẫu 11 (reference 14) |
| *(Thu hồi Giấy phép)* | Vi phạm thuộc Điều 17 NĐ 161 | 06 (thu hồi) | Mẫu 6 (reference 14) |
| *(Xử phạt VPHC)* | Cần lập biên bản VPHC, ra QĐ xử phạt | → **plugin xử phạt riêng `xp-sct-vn`** | (plugin riêng) |

**Ba câu hỏi gác cổng cho mọi nghiệp vụ** (trả lời trước khi làm):
1. **Đúng thẩm quyền không?** Loại hàng thuộc 1 (trừ VLNCN/tiền chất thuốc nổ), 2, 3, 4, 5, 8, 9 và đối tượng đặt trụ sở/chi nhánh tại Lào Cai (điều kiện địa bàn chỉ áp cho nhóm 1,2,3,4,9)? Người ký đúng (cả 7 loại → lãnh đạo Sở ký theo ủy quyền QĐ 1696 + QĐ 2848; thực tế KT.GĐ - PGĐ Hoàng Văn Thuân ký; riêng hồ sơ loại 5,8 tiếp nhận trước 14/8/2026 → trình UBND tỉnh)? (mục III, reference 16)
2. **Đúng văn bản hiện hành không?** Đã áp chuỗi thẩm quyền mới (loại 5, 8 về tỉnh từ 29/5/2026; ủy quyền cho Giám đốc Sở từ 14/8/2026 tại QĐ 2848 - mục II.15a); mã TTHC đúng nhóm (loại 5,8 dùng 1.013340/50/51, KHÔNG dùng 1.01496x); với kiểm tra dùng NĐ 217/2025 ("kiểm tra" không phải "thanh tra")?
3. **Có số/ngày nào đang bịa không?** Kế hoạch/quyết định kiểm tra, số văn bản nội bộ - đã xác minh chưa? Căn cứ ủy quyền dẫn đúng "QĐ 1696/QĐ-UBND ngày 15/5/2026 (được sửa đổi, bổ sung tại QĐ 2848/QĐ-UBND ngày 14/8/2026)"? (mục VII dưới đây, điểm 10)

## VII. NGUYÊN TẮC NGHIỆP VỤ BẤT BIẾN — ⭐ BẮT BUỘC đọc `references/19-nguyen-tac-nghiep-vu-bat-bien.md` trước khi thẩm định / soạn văn bản

Toàn văn 21 nguyên tắc ở ref 19; SKILL.md chỉ giữ mục lục để định vị, KHÔNG được coi là đủ.

- **1** — Số lượng hồ sơ: 01 bộ
- **2** — Hình thức nộp
- **3** — Thời hạn giải quyết
- **4** — Hồ sơ thiếu/sai
- **5** — Từ chối cấp phép phải trả lời bằng văn bản nêu rõ lý do
- **6** — Sau khi cấp
- **7** — CẤM cấp phép
- **8** — Không tự thêm điều kiện
- **9** — Người áp tải
- **10** — TUYỆT ĐỐI không bịa số/ngày văn bản pháp luật
- **11** — Thời hạn Giấy phép - phân biệt căn cứ luật và biện pháp nghiệp vụ
- **12** — Biên bản thẩm định dùng MẪU MỚI từ 20/7/2026
- **13** — Tổ hợp bồn chở khí biển Trung Quốc: kiểm định BỒN tách riêng kiểm định XE
- **14** — Cột trọng tải trong bảng phương tiện của GP - khi số liệu không sạch thì ghi chung
- **15** — VĂN PHONG CÔNG VĂN GỬI DOANH NGHIỆP - 02 quy tắc bất biến
- **16** — Đối chiếu MÔI CHẤT của bồn với hàng đề nghị cấp phép
- **17** — Xe biển Việt Nam
- **18** — Cột "Khối lượng vận chuyển" của Danh mục kèm Giấy phép - chọn cách ghi theo DẠNG CHỨA HÀNG, không copy máy …
- **19** — Doanh nghiệp nộp NHIỀU bộ hồ sơ cùng đợt: soát chéo để hai Giấy phép không lệch nhau
- **20** — BIỂN KIỂM SOÁT ghi KHÔNG kèm hậu tố trên đăng ký xe
- **21** — Rà soát bộ hồ sơ doanh nghiệp nộp: soát chéo cả 04 tệp, không đọc từng tệp rời

## VIII. BỐI CẢNH LÀO CAI

- Đối tượng điển hình trên địa bàn: vận chuyển oxy lỏng, nitơ lỏng, khí công nghiệp (loại 2); xăng, dầu, nhiên liệu lỏng dễ cháy (loại 3); LPG/LNG/CNG (loại 2); một số hóa chất công nghiệp.
- Lào Cai là tỉnh biên giới với Trung Quốc (cửa khẩu quốc tế Lào Cai, Kim Thành) - cần lưu ý quy định vận chuyển xuyên biên giới (Nghị định thư Việt - Trung) khi doanh nghiệp có hoạt động qua cửa khẩu.
- Vật liệu nổ công nghiệp và tiền chất thuốc nổ (phục vụ khai thác apatit, đá, khoáng sản) là lĩnh vực riêng do Phó Giám đốc Hoàng Văn Thuân phụ trách, theo pháp luật chuyên ngành VLNCN - KHÔNG thuộc thủ tục cấp phép vận chuyển HHNH loại 1, 2, 3, 4, 9 này (loại 1 đã trừ VLNCN, tiền chất thuốc nổ).
