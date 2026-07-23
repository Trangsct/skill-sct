---
name: hnh-sct-vn
description: "Chuyên gia vận chuyển hàng hóa nguy hiểm (HHNH) của Sở Công Thương tỉnh Lào Cai. 4 nghiệp vụ: (1) thẩm định hồ sơ, tham mưu cấp/điều chỉnh/cấp lại/thu hồi Giấy phép vận chuyển HHNH loại 1 (trừ VLNCN, tiền chất thuốc nổ), 2, 3, 4, 9 (Sở ký theo ủy quyền QĐ 1696) và loại 5, 8 (Sở thẩm định, trình UBND tỉnh ký); (2) trả lời, hướng dẫn doanh nghiệp về thủ tục, hồ sơ, điều kiện phương tiện, người lái xe, người áp tải, tập huấn, bao bì, biểu trưng; (3) kiểm tra chuyên ngành (NĐ 217/2025); (4) báo cáo cấp trên. Kèm văn bản gốc + ví dụ thực tế (Giấy phép Sở đã cấp, checklist, Phiếu trình, Biên bản thẩm định, mẫu rút/trả hồ sơ). Chuyên sâu xuyên biên giới Việt - Trung: xe biển Trung Quốc, chi nhánh, giấy phép loại D, cửa khẩu Kim Thành, Hà Khẩu. Từ khóa: HHNH, giấy phép vận chuyển, GP-SCT, thẩm định, thu hồi, NĐ 161/2024, NĐ 105/2025, TT 26/2026, Điều 51 Luật 36/2024, Luật Đường bộ 35/2024, giấy vận tải, QĐ 1696, người áp tải, tập huấn an toàn, Phụ lục I, loại 1 2 3 4 5 8 9, xăng dầu, NH3, oxy nitơ, LPG."
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

**Xử phạt vi phạm hành chính (lập biên bản VPHC, ra quyết định XPVPHC) KHÔNG xử lý trong plugin này** mà thuộc **plugin xử phạt riêng `xlvphc-sct-vn`** (dùng chung cả Sở). Plugin HHNH chỉ thực hiện **thu hồi Giấy phép** (biện pháp của cơ quan cấp phép - reference 06) và **chuyển hồ sơ/kiến nghị** khi phát hiện vi phạm khi kiểm tra (reference 12).

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
| Lập biên bản VPHC, ra QĐ xử phạt | `xlvphc-sct-vn` (plugin riêng) | Toàn bộ trình tự xử phạt |
| Công trình xây dựng liên quan (kho, trạm chiết nạp của DN vận chuyển) | `xd-sct-vn` | Thẩm định thiết kế, KTCTNT công trình công nghiệp |

## II. KHUNG PHÁP LÝ (cập nhật tháng 6/2026, đã đối chiếu văn bản gốc do Bạn cung cấp)

Toàn bộ số/ngày dưới đây đã được xác minh từ văn bản gốc trong bộ hồ sơ QPPL. TUYỆT ĐỐI không thay đổi, không tự điền số khác.

1. **Luật Trật tự, an toàn giao thông đường bộ số 36/2024/QH15** ngày 27/6/2024 (hiệu lực 01/01/2025). Điều 51 là nền tảng: định nghĩa hàng hóa nguy hiểm; yêu cầu phải có giấy phép vận chuyển; bố trí người áp tải khi cần thiết; dán biểu trưng nhận diện, lắp đèn, tín hiệu cảnh báo; tập huấn người lái xe/người áp tải; cơ quan cấp giấy phép phải gửi thông báo ngay đến cơ quan Cảnh sát giao thông.
1a. **Luật Đường bộ số 35/2024/QH15** ngày 27/6/2024 (hiệu lực 01/01/2025, cùng ngày với Luật 36/2024 - hai luật này tách ra từ Luật Giao thông đường bộ 2008). KHÔNG phải căn cứ cấp Giấy phép HHNH (căn cứ là Luật 36/2024), nhưng là khung hoạt động vận tải bao trùm, liên quan trực tiếp: **Điều 56** (phân biệt kinh doanh vận tải / vận tải nội bộ - xác định loại hình khi thẩm định, liên quan GPKD vận tải NĐ 158/2024); **Điều 61 khoản 1, 3** (giấy vận tải bắt buộc khi vận tải hàng hóa trên đường bộ; vận tải hàng hóa phải theo pháp luật TTATGTĐB và "quy định khác của pháp luật có liên quan" = khung HHNH); **Điều 62** (đơn vị vận tải cấp giấy vận tải cho lái xe, kiểm tra thông tin hàng hóa, hướng dẫn xếp dỡ an toàn); **Điều 63** (lái xe có quyền từ chối khi hàng cấm lưu thông/không có giấy vận tải); **Điều 64 khoản 2 điểm a, d** (người thuê vận tải: đóng gói đúng quy cách, ghi ký/mã hiệu; **cử người áp tải với hàng bắt buộc áp tải** - neo nghĩa vụ áp tải ở tầm luật); **Điều 60 khoản 2 điểm c + Điều 65 khoản 2** (cấm mang HHNH lên xe khách, xe thô sơ, xe mô tô, xe gắn máy - ranh giới loại phương tiện). Bản text tại `van-ban-goc/01-luat/`.
2. **Nghị định số 161/2024/NĐ-CP** ngày 18/12/2024 (hiệu lực 01/01/2025) quy định về Danh mục hàng hóa nguy hiểm, vận chuyển hàng hóa nguy hiểm và trình tự, thủ tục cấp giấy phép, cấp giấy chứng nhận hoàn thành chương trình tập huấn (đường bộ). **Đây là văn bản nghiệp vụ cốt lõi** (phân loại, điều kiện, hồ sơ, trình tự, thu hồi). Lưu ý: Điều 14 gốc của Nghị định này giao Bộ Công an cấp loại 1, 2, 3, 4, 9 - thẩm quyền này SAU ĐÓ đã thay đổi (xem mục III). NĐ 161 còn hiệu lực.
3. **Nghị định số 34/2024/NĐ-CP** ngày 31/3/2024 (hiệu lực 15/5/2024) về Danh mục hàng hóa nguy hiểm, vận chuyển hàng hóa nguy hiểm bằng phương tiện cơ giới đường bộ và đường thủy nội địa (thay thế NĐ 42/2020/NĐ-CP). NĐ 161/2024 **không thay thế toàn bộ** mà chỉ sửa đổi, bổ sung, bãi bỏ một số điều của NĐ 34/2024 (Điều 31 NĐ 161). Phần còn hiệu lực của NĐ 34/2024 áp dụng cho **vận chuyển hàng hóa nguy hiểm trên đường thủy nội địa**. (QĐ ủy quyền của UBND tỉnh Lào Cai dẫn cả NĐ 34/2024 và NĐ 161/2024 là đúng.)
4. **Luật Phòng cháy, chữa cháy và cứu nạn, cứu hộ số 55/2024/QH15** ngày 29/11/2024 (hiệu lực 01/7/2025).
5. **Nghị định số 105/2025/NĐ-CP** ngày 15/5/2025 (hiệu lực 01/7/2025) quy định chi tiết Luật PCCC&CNCH. **Đây là văn bản chuyển thẩm quyền:** NĐ 105/2025 đã **bãi bỏ khoản 1 Điều 14 và Điều 19, sửa đổi khoản 3 Điều 14** của NĐ 161/2024, theo đó **Bộ Công Thương** (thay vì Bộ Công an) tổ chức cấp Giấy phép loại 1, 2, 3, 4, 5, 8, 9 (trừ hóa chất bảo vệ thực vật và trường hợp Bộ Quốc phòng). Căn cứ phân cấp tiếp theo viện dẫn Điều 44 NĐ 105/2025 - LƯU Ý bản dẫn hiện hành theo Điều 25 TT 26/2026: khoản 2 Điều 8 (loại 1,2,3,4,9) dẫn **điểm b, điểm e khoản 4 Điều 44** (KHÔNG còn "khoản 6" như bản TT 15/2026); khoản 1 Điều 8 (loại 5,8) dẫn **điểm b, e, g khoản 4 Điều 44**. (Nội dung chi tiết Điều 44 tra trong skill `pccc-sct-vn`; phân tích tại reference 01 mục 2a.)
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
15. **Quyết định số 1696/QĐ-UBND ngày 15/5/2026 của UBND tỉnh Lào Cai** về việc ủy quyền cho Giám đốc Sở Công Thương thực hiện một số nhiệm vụ, quyền hạn của UBND tỉnh trong lĩnh vực **an toàn vệ sinh lao động và vận chuyển hàng hóa nguy hiểm** trên địa bàn tỉnh (đã ban hành chính thức - thay cho bản dự thảo trước đây). Căn cứ dẫn: Luật Tổ chức CQĐP 2025, NĐ 146/2025, NĐ 34/2024, NĐ 161/2024, NĐ 105/2025, NĐ 16/2026 (đường sắt), TT 38/2025, TT 15/2026, QĐ 555/QĐ-BCT. **LƯU Ý QUAN TRỌNG (đã trao đổi, xác nhận):** QĐ 1696 ban hành **trước** khi TT 26/2026 có hiệu lực (29/5/2026) và căn cứ dẫn TT 38/2025 + TT 15/2026, nên **chưa bao quát loại 5 và loại 8** mới được TT 26/2026 chuyển về UBND cấp tỉnh. Vì vậy hiện tại: **loại 1 (trừ VLNCN/tiền chất thuốc nổ), 2, 3, 4, 9 → Giám đốc Sở ký theo ủy quyền QĐ 1696; loại 5, 8 vẫn thuộc thẩm quyền UBND tỉnh (chưa ủy quyền)**. Sở đang chuẩn bị **đề nghị ủy quyền lại theo TT 26/2026** (đến 04/7/2026 CHƯA thấy QĐ ủy quyền mới - phải hỏi Bạn xác minh trước khi kết luận người ký loại 5, 8); khi có QĐ ủy quyền mới phải cập nhật số/ngày và phạm vi (bổ sung loại 5, 8) - không tự điền trước.
16. **Nghị định thư giữa Chính phủ Việt Nam và Chính phủ Trung Quốc** về thực hiện Hiệp định vận tải đường bộ Việt - Trung - áp dụng cho vận chuyển xuyên biên giới qua cửa khẩu Lào Cai (Điều 13: phương tiện vận tải hàng hóa nguy hiểm phải được cơ quan có thẩm quyền hai Bên cấp phép, gắn với giấy phép đặc biệt loại D).
17. **Nghị định số 158/2024/NĐ-CP** về hoạt động vận tải đường bộ (điều kiện kinh doanh vận tải - bối cảnh khi doanh nghiệp hỏi về giấy phép kinh doanh vận tải so với giấy phép vận chuyển HHNH). Bản gốc tại `van-ban-goc/02-nghi-dinh/`.

**Bổ sung khung pháp lý cho nghiệp vụ kiểm tra (cập nhật 2025-2026):**

18. **Luật Thanh tra số 84/2025/QH15** ngày 25/6/2025 (hiệu lực 01/7/2025). Sắp xếp hệ thống thanh tra 2 cấp; **các sở không còn tổ chức thanh tra**. Điều 61 quy định hoạt động **kiểm tra chuyên ngành** của các cơ quan quản lý nhà nước. Gắn với Kết luận số 134-KL/TW ngày 28/3/2025 của Bộ Chính trị, Ban Bí thư. Bản gốc tại `van-ban-goc/06-kiem-tra/`.
19. **Nghị định số 217/2025/NĐ-CP** ngày 05/8/2025 về hoạt động **kiểm tra chuyên ngành**. **Đây là văn bản trình tự, thủ tục cốt lõi cho hoạt động kiểm tra của Sở** (thay cho "thanh tra chuyên ngành" trước đây). Nguyên tắc quản lý rủi ro, không trùng lặp với thanh tra/kiểm toán. (Chi tiết tại reference 12; bản gốc tại `van-ban-goc/06-kiem-tra/`.)

**Khung pháp lý xử phạt VPHC → thuộc plugin riêng:** các văn bản về xử phạt vi phạm hành chính (Luật sửa đổi XLVPHC số 88/2025/QH15 - Điều 37a; NĐ 189/2025 về thẩm quyền xử phạt; NĐ 118/2021 đã được **NĐ 68/2025 và NĐ 190/2025** sửa đổi, bổ sung - nguồn biểu mẫu BBVPHC/QĐ XPVPHC; NĐ 168/2024 xử phạt giao thông đường bộ - thẩm quyền CSGT; NĐ 71/2019 sửa NĐ 17/2022 - hóa chất, VLNCN) **được xây dựng và áp dụng trong plugin xử phạt riêng `xlvphc-sct-vn`**, không lặp lại ở đây. Khi gặp việc xử phạt, gọi plugin đó.

## III. CHUỖI THẨM QUYỀN - HIỂU ĐÚNG ĐỂ KHÔNG NHẦM (cốt lõi nhất)

Đây là nội dung dễ sai nhất và là lý do skill này tồn tại. Nếu chỉ đọc Điều 14 Nghị định 161/2024/NĐ-CP sẽ kết luận SAI rằng Bộ Công an cấp loại 1, 2, 3, 4, 9. Thực tế thẩm quyền đã dịch chuyển qua một chuỗi văn bản:

**Bộ Công an (theo Điều 14 NĐ 161/2024 gốc) → Bộ Công Thương (NĐ 105/2025 bãi bỏ khoản 1 Điều 14, Điều 19 và sửa khoản 3 Điều 14 NĐ 161; Điều 44 NĐ 105/2025) → phân cấp cho UBND cấp tỉnh (Điều 8 TT 38/2025, sửa bởi Điều 3 TT 15/2026, nay là Điều 25 TT 26/2026 - bản hiện hành) → UBND tỉnh Lào Cai ủy quyền cho Giám đốc Sở Công Thương.**

Lưu ý cập nhật (tháng 6/2026): bản sửa Điều 8 TT 38/2025 hiện hành là bản tại **Điều 25 Thông tư 26/2026/TT-BCT** (hiệu lực 29/5/2026), thay cho hiệu lực bản sửa tại Điều 3 TT 15/2026. **Thay đổi quan trọng từ 29/5/2026:** ngoài loại 1 (trừ VLNCN/tiền chất thuốc nổ), 2, 3, 4, 9 (phân cấp theo khoản 2 Điều 8), TT 26/2026 còn giao **loại 5 và loại 8 cho UBND cấp tỉnh** (khoản 1 Điều 8). Tức UBND cấp tỉnh nay cấp Giấy phép cho **loại 1 trừ VLNCN/tiền chất thuốc nổ, 2, 3, 4, 5, 8, 9** (tại Lào Cai: loại 1,2,3,4,9 đã ủy quyền Giám đốc Sở theo QĐ 1696; loại 5,8 chưa ủy quyền - Sở thẩm định, trình UBND tỉnh ký). Cục Hóa chất - Bộ Công Thương KHÔNG còn là cơ quan cấp loại 5, 8.

Phân định thẩm quyền cấp Giấy phép hiện hành theo loại hàng:

| Loại hàng hóa nguy hiểm | Cơ quan cấp Giấy phép hiện hành |
|---|---|
| Loại 1 (trừ vật liệu nổ công nghiệp, tiền chất thuốc nổ), loại 2, loại 3, loại 4, loại 9 | UBND cấp tỉnh (Lào Cai: ủy quyền Giám đốc Sở Công Thương) cho tổ chức, cá nhân đặt trụ sở chính hoặc chi nhánh trên địa bàn tỉnh - khoản 2 Điều 8 TT 38/2025 (sửa bởi Điều 25 TT 26/2026) |
| Loại 5, loại 8 | **UBND cấp tỉnh** - khoản 1 Điều 8 TT 38/2025 (sửa bởi Điều 25 TT 26/2026), hiệu lực 29/5/2026; khoản 1 KHÔNG kèm điều kiện trụ sở/chi nhánh. Lào Cai: chưa ủy quyền (QĐ 1696 chỉ phủ 1,2,3,4,9) → Sở thẩm định, trình UBND tỉnh ký. Trước 29/5/2026 do Cục Hóa chất cấp |
| Vật liệu nổ công nghiệp, tiền chất thuốc nổ (thuộc loại 1) | Theo pháp luật chuyên ngành về vật liệu nổ công nghiệp (skill `pccc-sct-vn` mục VLNCN) - KHÔNG thuộc thủ tục này |
| Loại 6 (chất độc, chất gây nhiễm bệnh) | Theo phân công tại NĐ 161 (Bộ Y tế, Bộ Nông nghiệp và Môi trường tùy nhóm) |
| Loại 7 (chất phóng xạ) | Theo pháp luật về năng lượng nguyên tử |
| Hóa chất bảo vệ thực vật | UBND cấp tỉnh (theo khoản 4 Điều 14 NĐ 161 - đầu mối Sở Nông nghiệp và Môi trường, không thuộc Sở Công Thương) |
| Tổ chức, doanh nghiệp thuộc Bộ Quốc phòng | Bộ Quốc phòng |

**Nguyên tắc bất biến về thẩm quyền:**
- Phạm vi Sở Công Thương Lào Cai xử lý gồm loại 1 (trừ VLNCN, tiền chất thuốc nổ), 2, 3, 4, 5, 8, 9 - trong đó loại 1,2,3,4,9 Sở ký theo ủy quyền; loại 5, 8 Sở thẩm định, trình UBND tỉnh ký (đến khi có QĐ ủy quyền bổ sung). Câu hỏi về loại 6, loại 7, hóa chất BVTV, VLNCN/tiền chất thuốc nổ phải chuyển đúng đầu mối, không tự nhận.
- Điều kiện địa bàn: tổ chức, cá nhân phải đặt **trụ sở chính HOẶC chi nhánh** trên địa bàn tỉnh Lào Cai.
- Giấy phép **có hiệu lực trên toàn quốc** (không bị giới hạn trong tỉnh), thời hạn theo đề nghị của người vận tải nhưng **tối đa 24 tháng và không quá niên hạn sử dụng phương tiện**.

**Ai ký Giấy phép - đã có Quyết định ủy quyền (QĐ 1696/QĐ-UBND ngày 15/5/2026):**
- **Loại 1 (trừ VLNCN/tiền chất thuốc nổ), 2, 3, 4, 9 → mô hình ủy quyền:** lãnh đạo Sở ký trực tiếp Giấy phép, dùng hình thức văn bản và con dấu của Sở Công Thương (theo QĐ 1696). Thực tế các Giấy phép đã phát hành do **KT. GIÁM ĐỐC - PHÓ GIÁM ĐỐC Hoàng Văn Thuân** ký (PGĐ phụ trách HHNH, theo phân công nội bộ) - xem thể thức chuẩn tại reference 16 mục 2 và bản gốc tại vi-du-thuc-te/giay-phep-da-cap/.
- **Loại 5, 8 → hiện vẫn thuộc UBND tỉnh** (QĐ 1696 ban hành trước TT 26/2026 nên chưa ủy quyền 5, 8). Trong khi chờ ủy quyền lại theo TT 26/2026: Sở thẩm định, **trình UBND tỉnh** ký; hoặc tham mưu UBND tỉnh ban hành QĐ ủy quyền bổ sung. **Phải xác minh QĐ ủy quyền lại đã ban hành chưa trước khi xác định người ký cho loại 5, 8.**

Mã TTHC đã công bố: cấp mới 1.014967; cấp điều chỉnh 1.014968; cấp lại 1.014969.

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
- `16-thuc-tien-cap-phep-sct.md` - **Thực tiễn cấp phép tại Sở (đúc kết hồ sơ đã xử lý 2026):** bảng tiền lệ nội bộ (An Khang, Thái Thịnh, Bắc Cường, Apatit, Sợi Phương Nam, HNL...); thể thức Giấy phép thực tế (số /GP - SCT, người ký, nơi nhận, Lưu VT, BP1C, CN); quy trình 6 bước sau ủy quyền; các quyết định nghiệp vụ đã chốt (thời hạn GP khống chế theo kiểm định, GPKDVT, lỗi phân loại điển hình). ĐỌC TRƯỚC KHI SOẠN bất kỳ văn bản kết quả nào.
- `17-xuyen-bien-gioi-viet-trung.md` - **Hồ sơ có yếu tố nước ngoài/xuyên biên giới Việt - Trung (chuyên sâu):** cây quyết định thẩm quyền (khoản 1 vs khoản 2 Điều 8 - loại 5,8 không có điều kiện địa bàn); giấy phép loại D của Sở Xây dựng; checklist riêng cho xe biển Trung Quốc; tiền lệ 4 vụ việc. ĐỌC khi hồ sơ có xe biển nước ngoài, pháp nhân nước ngoài hoặc tuyến qua cửa khẩu.
- `mau-ho-so/` - Bộ biểu mẫu dựng trực tiếp từ hồ sơ thực tế (giữ nguyên cấu trúc, nội dung đã chuyển thành placeholder): Mẫu 1 Giấy đề nghị (Phụ lục IV), Mẫu 2 Bảng kê phương tiện, Mẫu 3 Bảng kê người lái xe + người áp tải, Mẫu 4 Phương án tổ chức vận chuyển (Phụ lục V), Mẫu 5 Giấy phép vận chuyển HHNH của Sở Công Thương, kèm `00-huong-dan-lap-ho-so.md`.

## IV-a. VÍ DỤ THỰC TẾ KÈM THEO (`vi-du-thuc-te/`) - MỚI 7/2026

Ba nhóm ví dụ thực tế, ưu tiên dùng làm bản gốc khi soạn văn bản (Chế độ B):
- `giay-phep-da-cap/` - hồ sơ Sở đã phát hành, LÀ MẪU CHUẨN CỦA SỞ (luôn dựng văn bản mới từ các file này):
  - `GP-ThaiThinh-xangdau-loai3-072026.docx`, `GP-SoiPhuongNam-NH3-loai2-xuyenbiengioi-072026.docx` - 2 Giấy phép (Thái Thịnh loại 3; Sợi Phương Nam NH3 loại 2 xuyên biên giới, 16 xe biển Trung Quốc). MẪU GIẤY PHÉP CHUẨN - luôn dựng GP mới từ đây.
  - `Bien-ban-tham-dinh-SCT-ThaiThinh-xangdau-loai3.docx` - **MẪU BIÊN BẢN THẨM ĐỊNH CHUẨN CỦA SỞ** (dùng cho loại 1, 2, 3, 4, 9). Khi soạn Biên bản thẩm định BẮT BUỘC dựng từ file này (Chế độ B, giữ nguyên thể thức). Cấu trúc chi tiết mẫu Sở: xem reference 16 mục 3.
- `cuc-hoa-chat/` - bộ hồ sơ nghiệp vụ của Cục Hóa chất (checklist thẩm định chi tiết, Phiếu trình, Biên bản thẩm định loại 5-8, GP mẫu loại 8, CV bổ sung hồ sơ xuyên biên giới) - **CHỈ dùng tham chiếu cho loại 5, 8** (Sở trình UBND tỉnh ký) và hồ sơ Việt - Trung. **KHÔNG dùng Biên bản thẩm định của Cục Hóa chất làm mẫu cho loại 1,2,3,4,9** - loại này dùng mẫu Biên bản của Sở ở `giay-phep-da-cap/`.
- `rut-tra-ho-so/` - mẫu CV dừng xử lý/trả hồ sơ và mẫu doanh nghiệp đề nghị rút hồ sơ.

## V. VĂN BẢN GỐC KÈM THEO (`van-ban-goc/`)

Plugin kèm sẵn bộ văn bản gốc để khi làm việc **không phải gửi lại tài liệu**. Tra theo mục lục tại reference 15. Cấu trúc 7 nhóm: `01-luat` (Điều 51 Luật 36/2024; toàn văn Luật Đường bộ 35/2024 bản text); `02-nghi-dinh` (NĐ 161/2024 bản text, 105/2025, 158/2024, Nghị định thư Việt-Trung, NQ 19/2026, NQ 66.18/2026); `03-thong-tu` (TT 26/2026, 15/2026, 37/2020, 37-BGTVT, 23/2024, 16/2018); `04-uy-quyen-quy-trinh` (QĐ 1696 ủy quyền, Quy trình nội bộ TTHC, Hướng dẫn thủ tục của Sở, CV 2265/BCT, Hiệp định Việt-Trung); `05-phu-luc-bieu-mau` (Phụ lục I-VIII, Điều 6, Điều 15); `06-kiem-tra` (NĐ 217/2025, Luật Thanh tra 84/2025); `07-tham-khao` (UN numbers, ĐLVN kiểm định xi téc, ví dụ cấp phép Cty TQ).

Nguyên tắc: ưu tiên đọc bản **text (.doc/.docx)** để trích nhanh; các bản scan rất nặng (NĐ 161 ~87 MB, Luật TTGT ~64 MB) đã lược bỏ, thay bằng bản text - cần bản có dấu thì tra Cơ sở dữ liệu quốc gia về VBPL. Khi có văn bản mới (đặc biệt **QĐ ủy quyền lại theo TT 26/2026**), bổ sung vào đúng thư mục và cập nhật reference 15.

## VI. BẢN ĐỒ 4 NGHIỆP VỤ - GẶP VIỆC GÌ ĐỌC GÌ

Tra nhanh: nhận yêu cầu → xác định nghiệp vụ → đọc reference tương ứng → soạn kết quả theo `vbhc-vn`.

| Nghiệp vụ | Gặp tình huống | Đọc reference | Mẫu kết quả |
|---|---|---|---|
| **1. Thẩm định hồ sơ** | Có hồ sơ cấp mới/điều chỉnh/cấp lại cần xử lý | 11 (quy trình + checklist mở rộng), 16 (thực tiễn Sở), 02 (hồ sơ), 03 (trình tự), 04 (điều kiện), 10 (Phụ lục I); có yếu tố nước ngoài → 17 | Phiếu thẩm định; mẫu 1, 2, 3, 4 (ref 14); ví dụ thực tế (vi-du-thuc-te/) |
| **2. Trả lời doanh nghiệp** | DN hỏi thủ tục, điều kiện, thẩm quyền, miễn cấp phép | 08 (FAQ), 01 (thẩm quyền), 06 (miễn cấp), 07 (đặc thù), 17 (Việt - Trung) | Mẫu 7 (reference 14) |
| **3. Kiểm tra chuyên ngành** | Lập kế hoạch/tổ chức kiểm tra; phát hiện vi phạm | 12 (kiểm tra), 04 (điều kiện), 05 (trách nhiệm) | Mẫu 8, 9, 10 (reference 14) |
| **4. Báo cáo cấp trên** | Báo cáo định kỳ/đột xuất/chuyên đề; thống kê | 13 (báo cáo) | Mẫu 11 (reference 14) |
| *(Thu hồi Giấy phép)* | Vi phạm thuộc Điều 17 NĐ 161 | 06 (thu hồi) | Mẫu 6 (reference 14) |
| *(Xử phạt VPHC)* | Cần lập biên bản VPHC, ra QĐ xử phạt | → **plugin xử phạt riêng `xlvphc-sct-vn`** | (plugin riêng) |

**Ba câu hỏi gác cổng cho mọi nghiệp vụ** (trả lời trước khi làm):
1. **Đúng thẩm quyền không?** Loại hàng thuộc 1 (trừ VLNCN/tiền chất thuốc nổ), 2, 3, 4, 5, 8, 9 và đối tượng đặt trụ sở/chi nhánh tại Lào Cai? Người ký đúng (loại 1,2,3,4,9 → lãnh đạo Sở theo ủy quyền QĐ 1696, thực tế KT.GĐ - PGĐ Hoàng Văn Thuân ký; loại 5,8 → trình UBND tỉnh ký)? (mục III, reference 16)
2. **Đúng văn bản hiện hành không?** Đã áp chuỗi thẩm quyền mới (loại 5, 8 về tỉnh từ 29/5/2026, chưa ủy quyền); với kiểm tra dùng NĐ 217/2025 ("kiểm tra" không phải "thanh tra")?
3. **Có số/ngày nào đang bịa không?** QĐ ủy quyền lại (TT 26/2026), kế hoạch/quyết định kiểm tra - đã xác minh chưa? (mục VII dưới đây, điểm 10)

## VII. NGUYÊN TẮC NGHIỆP VỤ BẤT BIẾN

1. **Số lượng hồ sơ: 01 bộ** cho mọi thủ tục (cấp mới, điều chỉnh, cấp lại).
2. **Hình thức nộp:** trực tiếp, qua dịch vụ bưu chính, hoặc trực tuyến qua Hệ thống thông tin giải quyết thủ tục hành chính. Đầu mối tiếp nhận: Trung tâm Phục vụ Hành chính công tỉnh; phòng chuyên môn thụ lý: **Phòng Quản lý Công nghiệp (QLCN)**.
3. **Thời hạn giải quyết** (kể từ ngày nhận đủ hồ sơ hợp lệ): cấp mới 05 ngày làm việc; cấp điều chỉnh 03 ngày làm việc; cấp lại (do mất, hỏng) 02 ngày làm việc. Riêng đường sắt: 03 ngày làm việc.
4. **Hồ sơ thiếu/sai:** nếu nộp trực tiếp thì hướng dẫn hoàn thiện ngay; nếu nộp qua bưu chính/trực tuyến thì trong 01 ngày làm việc phải thông báo bằng văn bản hoặc qua hệ thống để bổ sung. Mọi yêu cầu sửa đổi, bổ sung phải bằng văn bản.
5. **Từ chối cấp phép phải trả lời bằng văn bản nêu rõ lý do** (hoặc thông báo qua hệ thống dịch vụ công trực tuyến).
6. **Sau khi cấp:** phải thực hiện khoản 5 Điều 51 Luật 36/2024/QH15 (gửi thông báo ngay đến cơ quan Cảnh sát giao thông) và thông báo nội dung Giấy phép trên Cổng/trang thông tin điện tử của cơ quan.
7. **CẤM cấp phép** đối với hoạt động vận chuyển chất dễ cháy, nổ có hành trình đi qua công trình hầm có chiều dài từ 100 m trở lên, hoặc qua phà (theo Điều 11 NĐ 161). Cơ quan cấp phép phải từ chối.
8. **Không tự thêm điều kiện** không có trong văn bản (ví dụ: không yêu cầu giấy tờ ngoài thành phần hồ sơ quy định tại Điều 15 NĐ 161). Luật quy định gì làm đúng vậy.
9. **Người áp tải.** Danh mục Phụ lục I NĐ 161 KHÔNG có cột ngưỡng khối lượng (đã đối chiếu bản gốc; cột cuối là số hiệu nguy hiểm), nên phép thử "khối lượng > cột 7" của Điều 8 TT 37/2020/TT-BCT (dựa trên Danh mục khung cũ NĐ 42/2020) KHÔNG áp dụng cho khung NĐ 161. NĐ 105/2025 (khoản 4 Điều 23, Điều 26 NĐ 161) giao Bộ Công Thương quy định loại hàng bắt buộc áp tải. Trong khi chưa có danh mục cụ thể phân biệt, áp dụng theo hướng an toàn: yêu cầu người áp tải cho mọi chuyến HHNH phải cấp phép (loại 1 trừ VLNCN/tiền chất thuốc nổ, 2, 3, 4, 5, 8, 9); hồ sơ phải có danh sách người áp tải + chứng nhận tập huấn của người áp tải. Xem reference 04 (mục 3a) và 10.
10. **TUYỆT ĐỐI không bịa số/ngày văn bản pháp luật.** QĐ ủy quyền hiện hành là **QĐ 1696/QĐ-UBND ngày 15/5/2026** (chỉ phủ loại 1,2,3,4,9); **QĐ ủy quyền lại theo TT 26/2026 (bổ sung loại 5,8) chưa ban hành** - khi ban hành phải xác minh số/ngày trước khi đưa vào văn bản, không tự điền. Kế hoạch/quyết định kiểm tra và mọi số văn bản nội bộ khác cũng phải xác minh.
11. **Thời hạn Giấy phép - phân biệt căn cứ luật và biện pháp nghiệp vụ** (bài học 20/7/2026, vụ Toàn Phát TQ). Căn cứ luật: khoản 3 Điều 13 NĐ 161/2024 - thời hạn GP theo đề nghị của người vận tải nhưng tối đa không quá 24 tháng và **không quá NIÊN HẠN SỬ DỤNG của phương tiện**. Luật KHÔNG ràng buộc thời hạn GP với thời hạn kiểm định (đăng kiểm) - đó chỉ là điều kiện phương tiện phải duy trì trong suốt quá trình vận chuyển. Việc cấp GP thời hạn ngắn hơn theo mốc hạn kiểm định/GCN tập huấn là biện pháp nghiệp vụ của Sở, ghi lý do trong Phiếu trình/Biên bản thẩm định; trong văn bản gửi doanh nghiệp phải trích đúng câu luật, không viết "không vượt quá thời hạn kiểm định" như thể là quy định. Chi tiết: reference 11 (lỗi thẩm định số 9) và reference 16 mục 2. Mệnh đề "nhưng không vượt quá ngày [niên hạn]" CHỈ viết khi niên hạn rơi TRONG thời hạn GP tính từ ngày ký dự kiến; nếu thời hạn GP kết thúc trước niên hạn thì không viết (vụ Argon chốt 23/7/2026: ký 7/2026 + 24 tháng = 7/2028 < niên hạn 23/8/2028 → chỉ ghi "24 tháng kể từ ngày ký./.") - reference 16 mục 6.4.
12. **Biên bản thẩm định dùng MẪU MỚI từ 20/7/2026** (vụ Toàn Phát TQ): 4 căn cứ (NĐ 161; Điều 44 NĐ 105/2025; khoản 2 Điều 8 TT 38/2025 sửa bởi Điều 25 TT 26/2026; QĐ 1696); địa điểm làm việc TẠI TRỤ SỞ doanh nghiệp/chi nhánh kèm địa chỉ (không ghi "tại Sở Công Thương"); bảng phương tiện có cột NIÊN HẠN SỬ DỤNG; bảng ký 2 bên ĐẠI DIỆN CÔNG TY/CHI NHÁNH - TRƯỞNG ĐOÀN; câu nhận xét Phương án BỎ chữ "tối thiểu" (riêng bảng thành phần hồ sơ giữ nguyên văn NĐ); giờ/ngày để trống điền tay. Mẫu + ví dụ: vi-du-thuc-te/soi-phuong-nam-argon-nh3-072026/, chi tiết reference 16 mục 6.1.
13. **Tổ hợp bồn chở khí biển Trung Quốc: kiểm định BỒN tách riêng kiểm định XE** - phải đọc báo cáo kiểm định bồn (Viện kiểm định thiết bị đặc biệt cấp tỉnh TQ), mốc bồn thường sớm hơn mốc xe và DN hay kê thiếu; ghi cả 2 mốc vào biên bản, tách nghĩa vụ duy trì thành điều kiện riêng. Thông số hồ sơ đang mâu thuẫn (vd dung tích bồn) thì KHÔNG đưa vào biên bản/GP. Chi tiết reference 16 mục 6.2, reference 11 (lỗi 10-11).

14. **Cột trọng tải trong bảng phương tiện của GP - khi số liệu không sạch thì ghi chung** (thông lệ mới 23/7/2026, GP Argon 2 xe). Số liệu DN kê không khớp giấy tờ gốc (ví dụ đầu kéo: 25.000 kg là tổng trọng lượng bản thân, KHÔNG phải trọng tải chở hay khối lượng kéo theo - khối lượng kéo theo là 40.000 kg, trọng tải chở đầu kéo = 0) hoặc hồ sơ mâu thuẫn → tiêu đề cột rút gọn "Trọng tải được phép chở", từng dòng ghi "Theo giấy tờ của phương tiện", không bê số DN tự kê vào GP. Số liệu sạch, nhất quán → được ghi số cụ thể như tiền lệ GP NH3 16 xe. Chi tiết reference 16 mục 6.6.
## VIII. BỐI CẢNH LÀO CAI

- Đối tượng điển hình trên địa bàn: vận chuyển oxy lỏng, nitơ lỏng, khí công nghiệp (loại 2); xăng, dầu, nhiên liệu lỏng dễ cháy (loại 3); LPG/LNG/CNG (loại 2); một số hóa chất công nghiệp.
- Lào Cai là tỉnh biên giới với Trung Quốc (cửa khẩu quốc tế Lào Cai, Kim Thành) - cần lưu ý quy định vận chuyển xuyên biên giới (Nghị định thư Việt - Trung) khi doanh nghiệp có hoạt động qua cửa khẩu.
- Vật liệu nổ công nghiệp và tiền chất thuốc nổ (phục vụ khai thác apatit, đá, khoáng sản) là lĩnh vực riêng do Phó Giám đốc Hoàng Văn Thuân phụ trách, theo pháp luật chuyên ngành VLNCN - KHÔNG thuộc thủ tục cấp phép vận chuyển HHNH loại 1, 2, 3, 4, 9 này (loại 1 đã trừ VLNCN, tiền chất thuốc nổ).
