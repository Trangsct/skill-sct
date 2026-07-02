---
name: hnh-sct-vn
description: "Chuyên gia pháp luật, nghiệp vụ quản lý nhà nước về vận chuyển hàng hóa nguy hiểm (HHNH) của Sở Công Thương tỉnh Lào Cai. Dùng khi: thẩm định hồ sơ, tham mưu cấp, cấp điều chỉnh, cấp lại, thu hồi Giấy phép vận chuyển HHNH loại 1 (trừ vật liệu nổ công nghiệp, tiền chất thuốc nổ), loại 2, 3, 4, 5, 8, 9; giải đáp doanh nghiệp về trình tự, thành phần hồ sơ, điều kiện phương tiện, người lái xe, người áp tải, tập huấn an toàn, bao bì, biểu trưng nguy hiểm; xác định thẩm quyền (UBND tỉnh phân cấp, Sở Công Thương được ủy quyền); trường hợp đặc thù (nước ngoài, xuyên biên giới Việt - Trung, qua hầm/phà, miễn cấp phép); thu hồi, báo cáo. Từ khóa: vận chuyển hàng nguy hiểm, HHNH, giấy phép vận chuyển, Nghị định 161/2024/NĐ-CP, Nghị định 105/2025/NĐ-CP, Thông tư 38/2025/TT-BCT, Thông tư 26/2026/TT-BCT, Thông tư 37/2020/TT-BCT, Điều 51 Luật 36/2024/QH15, phân cấp, ủy quyền, tập huấn an toàn, người áp tải, Danh mục Phụ lục I, oxy lỏng, xăng dầu, LPG, lưu huỳnh, miễn cấp phép, loại 1 2 3 4 5 8 9."
---

# hnh-sct-vn - Chuyên gia cấp phép vận chuyển hàng hóa nguy hiểm Sở Công Thương Lào Cai

## I. KHI NÀO DÙNG SKILL NÀY

Kích hoạt skill khi xử lý bất kỳ việc nào sau đây:

- Thẩm định hồ sơ và tham mưu cấp mới, cấp điều chỉnh, cấp lại, thu hồi Giấy phép vận chuyển hàng hóa nguy hiểm (sau đây gọi tắt là Giấy phép) loại 1 (trừ vật liệu nổ công nghiệp, tiền chất thuốc nổ), loại 2, loại 3, loại 4, loại 5, loại 8, loại 9. (Cập nhật: từ 29/5/2026 loại 5 và loại 8 cũng do UBND cấp tỉnh cấp - xem mục III.)
- Trả lời, giải đáp, hướng dẫn cho doanh nghiệp, hợp tác xã, hộ kinh doanh trên địa bàn tỉnh về thủ tục, hồ sơ, điều kiện.
- Soạn công văn hướng dẫn, thông báo bổ sung hồ sơ, tờ trình, quyết định, báo cáo liên quan đến lĩnh vực vận chuyển hàng hóa nguy hiểm.
- Xác định thẩm quyền cấp phép, phân định ranh giới với cơ quan khác (Bộ Công an, Bộ Quốc phòng, Cục Hóa chất - Bộ Công Thương, cơ quan năng lượng nguyên tử).
- Xử lý các trường hợp đặc thù: doanh nghiệp hoặc phương tiện nước ngoài; vận chuyển xuyên biên giới Việt - Trung qua cửa khẩu Lào Cai; vận chuyển qua hầm, phà; vận chuyển bằng đường sắt, đường thủy nội địa; trường hợp miễn cấp phép theo ngưỡng khối lượng.
- Tư vấn về tập huấn an toàn hàng hóa nguy hiểm, người áp tải, bao bì, nhãn, biểu trưng nguy hiểm.

Khi soạn văn bản hành chính kết quả, kết hợp với skill `vbhc-vn` (định dạng, mẫu) và `anti-error-sct-vn` (phòng tránh sai số/ngày văn bản). Khi nhận PDF văn bản đến, kết hợp `vbhc-pdf-reader-vn`.

## II. KHUNG PHÁP LÝ (cập nhật tháng 6/2026, đã đối chiếu văn bản gốc do Bạn cung cấp)

Toàn bộ số/ngày dưới đây đã được xác minh từ văn bản gốc trong bộ hồ sơ QPPL. TUYỆT ĐỐI không thay đổi, không tự điền số khác.

1. **Luật Trật tự, an toàn giao thông đường bộ số 36/2024/QH15** ngày 27/6/2024 (hiệu lực 01/01/2025). Điều 51 là nền tảng: định nghĩa hàng hóa nguy hiểm; yêu cầu phải có giấy phép vận chuyển; bố trí người áp tải khi cần thiết; dán biểu trưng nhận diện, lắp đèn, tín hiệu cảnh báo; tập huấn người lái xe/người áp tải; cơ quan cấp giấy phép phải gửi thông báo ngay đến cơ quan Cảnh sát giao thông.
2. **Nghị định số 161/2024/NĐ-CP** ngày 18/12/2024 (hiệu lực 01/01/2025) quy định về Danh mục hàng hóa nguy hiểm, vận chuyển hàng hóa nguy hiểm và trình tự, thủ tục cấp giấy phép, cấp giấy chứng nhận hoàn thành chương trình tập huấn (đường bộ). **Đây là văn bản nghiệp vụ cốt lõi** (phân loại, điều kiện, hồ sơ, trình tự, thu hồi). Lưu ý: Điều 14 gốc của Nghị định này giao Bộ Công an cấp loại 1, 2, 3, 4, 9 - thẩm quyền này SAU ĐÓ đã thay đổi (xem mục III). NĐ 161 còn hiệu lực.
3. **Nghị định số 34/2024/NĐ-CP** ngày 31/3/2024 (hiệu lực 15/5/2024) về Danh mục hàng hóa nguy hiểm, vận chuyển hàng hóa nguy hiểm bằng phương tiện cơ giới đường bộ và đường thủy nội địa (thay thế NĐ 42/2020/NĐ-CP). NĐ 161/2024 **không thay thế toàn bộ** mà chỉ sửa đổi, bổ sung, bãi bỏ một số điều của NĐ 34/2024 (Điều 31 NĐ 161). Phần còn hiệu lực của NĐ 34/2024 áp dụng cho **vận chuyển hàng hóa nguy hiểm trên đường thủy nội địa**. (QĐ ủy quyền của UBND tỉnh Lào Cai dẫn cả NĐ 34/2024 và NĐ 161/2024 là đúng.)
4. **Luật Phòng cháy, chữa cháy và cứu nạn, cứu hộ số 55/2024/QH15** ngày 29/11/2024 (hiệu lực 01/7/2025).
5. **Nghị định số 105/2025/NĐ-CP** ngày 15/5/2025 (hiệu lực 01/7/2025) quy định chi tiết Luật PCCC&CNCH. **Đây là văn bản chuyển thẩm quyền:** NĐ 105/2025 đã **bãi bỏ khoản 1 Điều 14 và Điều 19, sửa đổi khoản 3 Điều 14** của NĐ 161/2024, theo đó **Bộ Công Thương** (thay vì Bộ Công an) tổ chức cấp Giấy phép loại 1, 2, 3, 4, 5, 8, 9 (trừ hóa chất bảo vệ thực vật và trường hợp Bộ Quốc phòng). Căn cứ phân cấp tiếp theo viện dẫn **Điều 44 (điểm b, điểm e khoản 4 và khoản 6)**. (Nội dung chi tiết Điều 44 tra trong skill `pccc-sct-vn`.)
6. **Nghị định số 146/2025/NĐ-CP** ngày 12/6/2025 về phân quyền, phân cấp trong lĩnh vực công nghiệp và thương mại.
7. **Nghị định số 139/2025/NĐ-CP** ngày 12/6/2025 về phân định thẩm quyền của chính quyền địa phương 02 cấp trong lĩnh vực quản lý nhà nước của Bộ Công Thương.
8. **Thông tư số 38/2025/TT-BCT** ngày 19/6/2025 (hiệu lực 01/7/2025) về phân cấp thực hiện thủ tục hành chính của Bộ Công Thương. **Điều 8** là điều khoản phân cấp về vận chuyển hàng hóa nguy hiểm. Điều 8 này đã qua hai lần sửa: lần đầu bởi Điều 3 Thông tư 15/2026/TT-BCT (25/3/2026, hiệu lực 10/4/2026); **sau đó bởi Điều 25 Thông tư 26/2026/TT-BCT (xem mục 9) - bản sửa của TT 26/2026 là bản hiện hành.**
9. **Thông tư số 26/2026/TT-BCT** ngày 20/5/2026 (hiệu lực **29/5/2026**, do Thứ trưởng Phan Thị Thắng ký) - **VĂN BẢN MỚI NHẤT, bao quát 8 lĩnh vực gồm vận chuyển hàng hóa nguy hiểm.** **Điều 25 sửa đổi, bổ sung Điều 8 Thông tư 38/2025/TT-BCT** thành "Điều 8. Thẩm quyền giải quyết thủ tục hành chính về vận chuyển hàng hóa nguy hiểm", gồm 2 khoản (nội dung gốc đã xác minh từ văn bản):
   - **Khoản 1: UBND cấp tỉnh** tiếp nhận hồ sơ, thẩm định, cấp, cấp điều chỉnh, cấp lại, thu hồi Giấy phép vận chuyển HHNH **loại 5 và loại 8** (theo khoản 1 Điều 4 NĐ 161/2024; điểm b, e, g khoản 4 Điều 44 NĐ 105/2025). ĐÂY LÀ THAY ĐỔI QUAN TRỌNG: loại 5, 8 trước đây do Cục Hóa chất - Bộ Công Thương cấp, **nay chuyển về UBND cấp tỉnh**.
   - **Khoản 2: Bộ trưởng Bộ Công Thương phân cấp cho UBND cấp tỉnh** (nơi tổ chức, cá nhân đặt trụ sở chính hoặc chi nhánh) cấp, cấp điều chỉnh, cấp lại, thu hồi Giấy phép HHNH **loại 1 (trừ VLNCN, tiền chất thuốc nổ), loại 2, loại 3, loại 4, loại 9** (điểm b, điểm e khoản 4 Điều 44 NĐ 105/2025).
   - **Điều 26 TT 26/2026 bãi bỏ Điều 3 Thông tư 15/2026/TT-BCT** (bản sửa Điều 8 trước đây). Như vậy bản Điều 8 hiện hành là bản do Điều 25 TT 26/2026 quy định. TT 26/2026 cũng tuyên bố cắt giảm, rút ngắn thời hạn ở nhiều lĩnh vực - khi áp dụng thời hạn cụ thể cần đối chiếu Quyết định công bố TTHC mới nhất.
10. **Thông tư số 15/2026/TT-BCT** ngày 25/3/2026 (hiệu lực 10/4/2026) - vẫn còn hiệu lực ở các nội dung không bị TT 26/2026 bãi bỏ; riêng nội dung phân cấp vận chuyển HHNH đã được TT 26/2026 sửa đổi lại (xem mục 8, 9).
11. **Nghị quyết số 19/2026/NQ-CP** của Chính phủ về cắt giảm, phân cấp, đơn giản hóa thủ tục hành chính, điều kiện kinh doanh thuộc phạm vi quản lý của Bộ Công Thương (là căn cứ ban hành TT 26/2026; chính là file "19-nqcp" trong bộ hồ sơ).
12. **Nghị quyết số 66.18/2026/NQ-CP** ngày 18/5/2026 về phân quyền, cắt giảm, đơn giản hóa thủ tục hành chính, điều kiện kinh doanh (hiệu lực 01/7/2026 đến hết 28/02/2027) - khung phân quyền chung.
13. **Văn bản số 2265/BCT-ATMT** ngày 02/4/2026 của Bộ Công Thương (do Thứ trưởng Trương Thanh Hoài ký) đề nghị UBND các tỉnh triển khai thủ tục; dẫn chiếu **Quyết định số 555/QĐ-BCT** ngày 26/3/2026 công bố thủ tục hành chính. (Trước đó Quyết định số 1781/QĐ-BCT ngày 23/6/2025 là lần công bố đầu, hiệu lực 01/7/2025.)
14. **Văn bản của Chủ tịch UBND tỉnh Lào Cai** giao Sở Công Thương chủ trì triển khai (theo CV 2265/BCT-ATMT).
15. **Quyết định của UBND tỉnh Lào Cai về việc ủy quyền cho Giám đốc Sở Công Thương** thực hiện một số nhiệm vụ, quyền hạn của UBND tỉnh trong lĩnh vực an toàn vệ sinh lao động và vận chuyển hàng hóa nguy hiểm (dự thảo tháng 4/2026, theo Tờ trình số 1856/TTr-SCT ngày 08/4/2026; thời hạn ủy quyền đến hết 28/02/2027). **CẢNH BÁO 1:** số và ngày của Quyết định này còn để trống trong bản dự thảo - phải xác minh khi ban hành chính thức, không tự điền. **CẢNH BÁO 2:** bản dự thảo dẫn căn cứ "Khoản 2 Điều 3 TT 15/2026"; khi hoàn thiện sau ngày 29/5/2026 nên cập nhật căn cứ thành **Điều 8 TT 38/2025 được sửa đổi bởi Điều 25 TT 26/2026** cho đúng văn bản hiện hành.
16. **Nghị định thư giữa Chính phủ Việt Nam và Chính phủ Trung Quốc** về thực hiện Hiệp định vận tải đường bộ Việt - Trung - áp dụng cho vận chuyển xuyên biên giới qua cửa khẩu Lào Cai (Điều 13: phương tiện vận tải hàng hóa nguy hiểm phải được cơ quan có thẩm quyền hai Bên cấp phép, gắn với giấy phép đặc biệt loại D).

## III. CHUỖI THẨM QUYỀN - HIỂU ĐÚNG ĐỂ KHÔNG NHẦM (cốt lõi nhất)

Đây là nội dung dễ sai nhất và là lý do skill này tồn tại. Nếu chỉ đọc Điều 14 Nghị định 161/2024/NĐ-CP sẽ kết luận SAI rằng Bộ Công an cấp loại 1, 2, 3, 4, 9. Thực tế thẩm quyền đã dịch chuyển qua một chuỗi văn bản:

**Bộ Công an (theo Điều 14 NĐ 161/2024 gốc) → Bộ Công Thương (NĐ 105/2025 bãi bỏ khoản 1 Điều 14, Điều 19 và sửa khoản 3 Điều 14 NĐ 161; Điều 44 NĐ 105/2025) → phân cấp cho UBND cấp tỉnh (Điều 8 TT 38/2025, sửa bởi Điều 3 TT 15/2026, nay là Điều 25 TT 26/2026 - bản hiện hành) → UBND tỉnh Lào Cai ủy quyền cho Giám đốc Sở Công Thương.**

Lưu ý cập nhật (tháng 6/2026): bản sửa Điều 8 TT 38/2025 hiện hành là bản tại **Điều 25 Thông tư 26/2026/TT-BCT** (hiệu lực 29/5/2026), thay cho hiệu lực bản sửa tại Điều 3 TT 15/2026. **Thay đổi quan trọng từ 29/5/2026:** ngoài loại 1 (trừ VLNCN/tiền chất thuốc nổ), 2, 3, 4, 9 (phân cấp theo khoản 2 Điều 8), TT 26/2026 còn giao **loại 5 và loại 8 cho UBND cấp tỉnh** (khoản 1 Điều 8). Tức UBND cấp tỉnh (Lào Cai: ủy quyền Giám đốc Sở Công Thương) nay cấp Giấy phép cho **loại 1 trừ VLNCN/tiền chất thuốc nổ, 2, 3, 4, 5, 8, 9**. Cục Hóa chất - Bộ Công Thương KHÔNG còn là cơ quan cấp loại 5, 8.

Phân định thẩm quyền cấp Giấy phép hiện hành theo loại hàng:

| Loại hàng hóa nguy hiểm | Cơ quan cấp Giấy phép hiện hành |
|---|---|
| Loại 1 (trừ vật liệu nổ công nghiệp, tiền chất thuốc nổ), loại 2, loại 3, loại 4, loại 9 | UBND cấp tỉnh (Lào Cai: ủy quyền Giám đốc Sở Công Thương) cho tổ chức, cá nhân đặt trụ sở chính hoặc chi nhánh trên địa bàn tỉnh - khoản 2 Điều 8 TT 38/2025 (sửa bởi Điều 25 TT 26/2026) |
| Loại 5, loại 8 | **UBND cấp tỉnh** (Lào Cai: ủy quyền Giám đốc Sở Công Thương) - khoản 1 Điều 8 TT 38/2025 (sửa bởi Điều 25 TT 26/2026), hiệu lực 29/5/2026. Trước 29/5/2026 do Cục Hóa chất - Bộ Công Thương cấp |
| Vật liệu nổ công nghiệp, tiền chất thuốc nổ (thuộc loại 1) | Theo pháp luật chuyên ngành về vật liệu nổ công nghiệp (skill `pccc-sct-vn` mục VLNCN) - KHÔNG thuộc thủ tục này |
| Loại 6 (chất độc, chất gây nhiễm bệnh) | Theo phân công tại NĐ 161 (Bộ Y tế, Bộ Nông nghiệp và Môi trường tùy nhóm) |
| Loại 7 (chất phóng xạ) | Theo pháp luật về năng lượng nguyên tử |
| Hóa chất bảo vệ thực vật | UBND cấp tỉnh (theo khoản 4 Điều 14 NĐ 161 - đầu mối Sở Nông nghiệp và Môi trường, không thuộc Sở Công Thương) |
| Tổ chức, doanh nghiệp thuộc Bộ Quốc phòng | Bộ Quốc phòng |

**Nguyên tắc bất biến về thẩm quyền:**
- Thủ tục Sở Công Thương Lào Cai thực hiện CHỈ gồm loại 1 (trừ VLNCN, tiền chất thuốc nổ), 2, 3, 4, 9. Mọi câu hỏi về loại 5, 6, 7, 8, hóa chất BVTV, VLNCN phải chuyển đúng đầu mối, không tự nhận.
- Điều kiện địa bàn: tổ chức, cá nhân phải đặt **trụ sở chính HOẶC chi nhánh** trên địa bàn tỉnh Lào Cai.
- Giấy phép **có hiệu lực trên toàn quốc** (không bị giới hạn trong tỉnh), thời hạn theo đề nghị của người vận tải nhưng **tối đa 24 tháng và không quá niên hạn sử dụng phương tiện**.

**Ai ký Giấy phép - hai mô hình trong hồ sơ dự thảo (phải xác định rõ mô hình đang áp dụng trước khi soạn):**
- **Mô hình ủy quyền (Quyết định ủy quyền):** Giám đốc Sở Công Thương ký trực tiếp Giấy phép, sử dụng hình thức văn bản và con dấu của Sở Công Thương. Đây là mô hình theo Quyết định ủy quyền của UBND tỉnh.
- **Mô hình trình ký (Quy trình nội bộ TTHC):** Sở Công Thương thẩm định, trình UBND tỉnh; UBND tỉnh ký Giấy phép.

Hai mô hình này cùng tồn tại trong bộ dự thảo tháng 4/2026. **Khi tham mưu, phải hỏi/xác minh Quyết định ủy quyền đã được ban hành chưa.** Nếu đã ban hành Quyết định ủy quyền thì áp dụng mô hình ủy quyền (Giám đốc Sở ký). Mã TTHC đã công bố: cấp mới 1.014967; cấp điều chỉnh 1.0149681; cấp lại 1.014969.

## IV. CÁC REFERENCE FILES (đọc khi cần đào sâu)

Đọc file tương ứng trong thư mục `references/` khi xử lý chi tiết:

- `01-chuoi-tham-quyen.md` - Chi tiết chuỗi thẩm quyền, căn cứ từng văn bản, ai ký, mã TTHC, xử lý câu hỏi "ai cấp loại này".
- `02-thanh-phan-ho-so.md` - Thành phần hồ sơ cấp mới, cấp điều chỉnh, cấp lại; các mẫu Phụ lục; checklist thẩm định hồ sơ.
- `03-trinh-tu-thu-tuc.md` - Trình tự, thời hạn giải quyết (05/03/02 ngày làm việc), các bước nội bộ, cách nộp hồ sơ, xử lý hồ sơ thiếu.
- `04-dieu-kien-tuan-thu.md` - Điều kiện phương tiện, người lái xe/người áp tải, tập huấn an toàn, bao bì - thùng chứa, nhãn, biểu trưng nguy hiểm.
- `05-trach-nhiem-cac-ben.md` - Trách nhiệm người thuê vận tải, người vận tải, người lái xe, người áp tải; hồ sơ vận chuyển; chế độ báo cáo, lưu giữ.
- `06-thu-hoi-mien-cap.md` - Các trường hợp thu hồi Giấy phép và hệ quả (30/60 ngày); các trường hợp miễn cấp Giấy phép theo ngưỡng khối lượng; từ chối cấp phép.
- `07-truong-hop-dac-thu.md` - Doanh nghiệp/phương tiện nước ngoài; vận chuyển xuyên biên giới Việt - Trung qua Lào Cai; qua hầm/phà; đường sắt, đường thủy; chuyển tiếp giấy phép cũ.
- `08-faq-doanh-nghiep.md` - Bộ câu hỏi - trả lời mẫu để giải đáp doanh nghiệp; ngôn ngữ hướng dẫn chuẩn.
- `09-cap-nhat-phap-ly-2026.md` - **Cập nhật pháp lý mới nhất (NĐ 105/2025, TT 38/2025, TT 15/2026, TT 26/2026):** nội dung Điều 44 khoản 4 NĐ 105, Điều 25 + Điều 26 TT 26/2026, thẩm quyền hiện hành (loại 5,8 chuyển về UBND cấp tỉnh), người áp tải theo khối lượng. ĐỌC FILE NÀY trước khi kết luận thẩm quyền/áp tải.
- `10-danh-muc-phu-luc-1.md` - **Cấu trúc Danh mục Phụ lục I NĐ 161 (đã đối chiếu bản gốc):** Danh mục chỉ có 6 cột, KHÔNG có cột ngưỡng khối lượng (cột cuối là số hiệu nguy hiểm). Kèm bảng tra nhanh số UN/loại/số hiệu nguy hiểm các mặt hàng thường gặp ở Lào Cai (trích đúng Phụ lục I).
- `mau-ho-so/` - Bộ biểu mẫu dựng trực tiếp từ hồ sơ thực tế (giữ nguyên cấu trúc, nội dung đã chuyển thành placeholder): Mẫu 1 Giấy đề nghị (Phụ lục IV), Mẫu 2 Bảng kê phương tiện, Mẫu 3 Bảng kê người lái xe + người áp tải, Mẫu 4 Phương án tổ chức vận chuyển (Phụ lục V), Mẫu 5 Giấy phép vận chuyển HHNH của Sở Công Thương, kèm `00-huong-dan-lap-ho-so.md`.

## V. NGUYÊN TẮC NGHIỆP VỤ BẤT BIẾN

1. **Số lượng hồ sơ: 01 bộ** cho mọi thủ tục (cấp mới, điều chỉnh, cấp lại).
2. **Hình thức nộp:** trực tiếp, qua dịch vụ bưu chính, hoặc trực tuyến qua Hệ thống thông tin giải quyết thủ tục hành chính. Đầu mối tiếp nhận: Trung tâm Phục vụ Hành chính công tỉnh; phòng chuyên môn thụ lý: **Phòng Quản lý Công nghiệp (QLCN)**.
3. **Thời hạn giải quyết** (kể từ ngày nhận đủ hồ sơ hợp lệ): cấp mới 05 ngày làm việc; cấp điều chỉnh 03 ngày làm việc; cấp lại (do mất, hỏng) 02 ngày làm việc. Riêng đường sắt: 03 ngày làm việc.
4. **Hồ sơ thiếu/sai:** nếu nộp trực tiếp thì hướng dẫn hoàn thiện ngay; nếu nộp qua bưu chính/trực tuyến thì trong 01 ngày làm việc phải thông báo bằng văn bản hoặc qua hệ thống để bổ sung. Mọi yêu cầu sửa đổi, bổ sung phải bằng văn bản.
5. **Từ chối cấp phép phải trả lời bằng văn bản nêu rõ lý do** (hoặc thông báo qua hệ thống dịch vụ công trực tuyến).
6. **Sau khi cấp:** phải thực hiện khoản 5 Điều 51 Luật 36/2024/QH15 (gửi thông báo ngay đến cơ quan Cảnh sát giao thông) và thông báo nội dung Giấy phép trên Cổng/trang thông tin điện tử của cơ quan.
7. **CẤM cấp phép** đối với hoạt động vận chuyển chất dễ cháy, nổ có hành trình đi qua công trình hầm có chiều dài từ 100 m trở lên, hoặc qua phà (theo Điều 11 NĐ 161). Cơ quan cấp phép phải từ chối.
8. **Không tự thêm điều kiện** không có trong văn bản (ví dụ: không yêu cầu giấy tờ ngoài thành phần hồ sơ quy định tại Điều 15 NĐ 161). Luật quy định gì làm đúng vậy.
9. **Người áp tải.** Danh mục Phụ lục I NĐ 161 KHÔNG có cột ngưỡng khối lượng (đã đối chiếu bản gốc; cột cuối là số hiệu nguy hiểm), nên phép thử "khối lượng > cột 7" của Điều 8 TT 37/2020/TT-BCT (dựa trên Danh mục khung cũ NĐ 42/2020) KHÔNG áp dụng cho khung NĐ 161. NĐ 105/2025 (khoản 4 Điều 23, Điều 26 NĐ 161) giao Bộ Công Thương quy định loại hàng bắt buộc áp tải. Trong khi chưa có danh mục cụ thể phân biệt, áp dụng theo hướng an toàn: yêu cầu người áp tải cho mọi chuyến HHNH phải cấp phép (loại 1 trừ VLNCN/tiền chất thuốc nổ, 2, 3, 4, 5, 8, 9); hồ sơ phải có danh sách người áp tải + chứng nhận tập huấn của người áp tải. Xem reference 04 (mục 3a) và 10.
10. **TUYỆT ĐỐI không bịa số/ngày văn bản pháp luật.** Số/ngày Quyết định ủy quyền của UBND tỉnh và các văn bản nội bộ còn dự thảo phải xác minh trước khi đưa vào văn bản trình ký.

## VI. BỐI CẢNH LÀO CAI

- Đối tượng điển hình trên địa bàn: vận chuyển oxy lỏng, nitơ lỏng, khí công nghiệp (loại 2); xăng, dầu, nhiên liệu lỏng dễ cháy (loại 3); LPG/LNG/CNG (loại 2); một số hóa chất công nghiệp.
- Lào Cai là tỉnh biên giới với Trung Quốc (cửa khẩu quốc tế Lào Cai, Kim Thành) - cần lưu ý quy định vận chuyển xuyên biên giới (Nghị định thư Việt - Trung) khi doanh nghiệp có hoạt động qua cửa khẩu.
- Vật liệu nổ công nghiệp và tiền chất thuốc nổ (phục vụ khai thác apatit, đá, khoáng sản) là lĩnh vực riêng do Phó Giám đốc Hoàng Văn Thuân phụ trách, theo pháp luật chuyên ngành VLNCN - KHÔNG thuộc thủ tục cấp phép vận chuyển HHNH loại 1, 2, 3, 4, 9 này (loại 1 đã trừ VLNCN, tiền chất thuốc nổ).
