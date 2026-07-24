---
name: hc-sct-vn
description: "Chuyên gia quản lý nhà nước về HÓA CHẤT của Sở Công Thương tỉnh Lào Cai theo khung pháp lý mới 2026 (Luật Hóa chất 69/2025, Nghị định 24/25/26/2026, Thông tư 01+02/2026). 6 nghiệp vụ: (1) thẩm định, tham mưu cấp/cấp lại/điều chỉnh/thu hồi Giấy chứng nhận đủ điều kiện sản xuất, kinh doanh hóa chất có điều kiện; GCN dịch vụ tồn trữ; Giấy phép hóa chất cần kiểm soát đặc biệt nhóm 2 (thẩm quyền UBND cấp tỉnh); (2) thẩm định, phê duyệt Kế hoạch phòng ngừa, ứng phó sự cố hóa chất; (3) hướng dẫn doanh nghiệp hồ sơ, điều kiện, khai báo hóa chất nhập khẩu, huấn luyện an toàn; (4) kiểm tra chuyên ngành (NĐ 217/2025); (5) báo cáo cấp trên; (6) soạn công văn, tờ trình, quyết định, báo cáo. Kèm văn bản gốc, biểu mẫu, ví dụ thực tế của Sở. Từ khóa: hóa chất, Luật 69/2025, NĐ 24/25/26/2026, TT 01/2026, GCN đủ điều kiện, hóa chất có điều kiện, kiểm soát đặc biệt nhóm 1-2, dịch vụ tồn trữ, KH phòng ngừa sự cố, huấn luyện an toàn hóa chất, khai báo hóa chất, QCVN 05A, axit HNO3, NH3, tiền chất, CN(Loan), PGĐ Thuân."
---

# hc-sct-vn — Plugin lớn HÓA CHẤT: cấp phép, thẩm định KH sự cố, hướng dẫn DN, kiểm tra, báo cáo (Sở Công Thương Lào Cai)

## I. KHI NÀO DÙNG SKILL NÀY

Kích hoạt khi xử lý bất kỳ việc nào về **quản lý nhà nước lĩnh vực hóa chất** trên địa bàn tỉnh Lào Cai:

- Thẩm định hồ sơ và tham mưu cấp mới/cấp lại/cấp điều chỉnh/thu hồi **Giấy chứng nhận đủ điều kiện sản xuất, kinh doanh hóa chất có điều kiện** (thẩm quyền UBND cấp tỉnh).
- Thẩm định hồ sơ **Giấy chứng nhận đủ điều kiện hoạt động dịch vụ tồn trữ hóa chất** (thẩm quyền UBND cấp tỉnh với cơ sở thuộc đối tượng Biện pháp/KH do tỉnh thẩm định — hiệu lực 01/7/2026).
- Thẩm định hồ sơ **Giấy phép sản xuất, kinh doanh hóa chất cần kiểm soát đặc biệt nhóm 2** và **Giấy phép xuất khẩu, nhập khẩu hóa chất cần kiểm soát đặc biệt nhóm 2** (phân cấp cho UBND cấp tỉnh tại Điều 3, 4 Thông tư 01/2026).
- **Thẩm định, phê duyệt Kế hoạch phòng ngừa, ứng phó sự cố hóa chất** trong lĩnh vực dân sự đối với đối tượng thuộc **điểm b khoản 2 Điều 33 NĐ 25/2026** (UBND cấp tỉnh chủ trì); lập Hội đồng thẩm định; kiểm tra thực tế; ra Quyết định phê duyệt.
- Hướng dẫn doanh nghiệp, hợp tác xã, hộ kinh doanh về thủ tục, hồ sơ, điều kiện; về **khai báo hóa chất nhập khẩu** (Cổng một cửa quốc gia); **huấn luyện an toàn chuyên ngành hóa chất**; **Biện pháp phòng ngừa, ứng phó sự cố hóa chất** (DN tự ban hành); phân loại - ghi nhãn - phiếu an toàn hóa chất.
- **Kiểm tra chuyên ngành** việc chấp hành pháp luật về hóa chất (NĐ 217/2025, TT 56/2025); lập Đoàn kiểm tra; biên bản; kết luận.
- **Báo cáo cấp trên** (UBND tỉnh, Bộ Công Thương/Cục Hóa chất): định kỳ, đột xuất (sự cố), chuyên đề; đôn đốc DN báo cáo; cung cấp thông tin cho cơ quan phối hợp (Công an, Quân sự).
- Xây dựng, cập nhật **Kế hoạch phòng ngừa, ứng phó sự cố hóa chất cấp tỉnh** (Điều 37 NĐ 25); tổ chức diễn tập cấp tỉnh.
- Soạn công văn, tờ trình, quyết định, báo cáo, bài phát biểu, thông báo trong lĩnh vực hóa chất.
- Tra cứu **danh mục hóa chất** (cơ bản/có điều kiện/kiểm soát đặc biệt/phải xây dựng KH) tại Nghị định 24/2026.

**Xử phạt vi phạm hành chính (lập biên bản VPHC, ra QĐ xử phạt)** trong lĩnh vực hóa chất **KHÔNG xử lý trong plugin này** mà thuộc plugin xử phạt riêng của Sở. Plugin hóa chất chỉ thực hiện **thu hồi Giấy chứng nhận/Giấy phép** (biện pháp của cơ quan cấp phép — reference 09) và **chuyển hồ sơ/kiến nghị** khi phát hiện vi phạm qua kiểm tra (reference 10). Khung xử phạt gốc (NĐ 71/2019 sửa bởi NĐ 17/2022) kèm tại `van-ban-goc/05-xu-phat-kiem-tra/` để tra khi cần dẫn chiếu.

**Vật liệu nổ công nghiệp, tiền chất thuốc nổ** là lĩnh vực RIÊNG (các plugin `kho-vlncn-sct-vn`, `sd-vlncn-sct-vn`, `hl-vlncn-sct-vn`), KHÔNG thuộc plugin hóa chất — dù cùng do PGĐ Hoàng Văn Thuân phụ trách. **Vận chuyển hàng hóa nguy hiểm** (kể cả vận chuyển hóa chất: loại 8 ăn mòn, loại 2 khí, loại 5 oxy hóa...) thuộc plugin `hnh-sct-vn`. **Bảo vệ môi trường/ĐTM/GPMT dự án hóa chất** thuộc plugin `bvmt-sct-vn`. **Thông báo kết quả kiểm tra công tác nghiệm thu** công trình nhà xưởng/kho (thành phần hồ sơ bắt buộc tại Điều 9, Điều 20 NĐ 26) là thủ tục KTCTNT theo pháp luật xây dựng → plugin `xd-sct-vn`; DN chưa có Thông báo nghiệm thu → hướng dẫn theo plugin đó. **Cơ sở hóa chất đặt trong KCN/CCN** → phối hợp BQL khu, tra plugin `kcn-ccn-vn`. **PCCC kho hóa chất** → plugin `pccc-sct-vn`.

Khi soạn văn bản kết quả, kết hợp `vbhc-vn` (thể thức, mẫu 08/09) và `anti-error` (chống bịa số/ngày). Nhận PDF văn bản đến → chạy `vbhc-pdf-reader-vn`. Xác định người ký/người soạn/PGĐ phụ trách → tra `sct-laocai-org-vn`.

## II. KHUNG PHÁP LÝ MỚI 2026 (đã đối chiếu văn bản gốc)

**ĐIỂM MẤU CHỐT: từ 01/01/2026 toàn bộ khung pháp luật hóa chất đã ĐỔI MỚI.** Luật Hóa chất 06/2007, Nghị định 113/2017, 82/2022, Thông tư 32/2017, 17/2022 đã **HẾT HIỆU LỰC**. Khi thẩm định hồ sơ, nếu doanh nghiệp còn viện dẫn các văn bản cũ này → **hồ sơ không đạt** (đây là lỗi điển hình đã gặp trong thực tế — xem reference 16, vụ HNO3). Số/ngày dưới đây đã xác minh từ văn bản gốc, TUYỆT ĐỐI không tự đổi.

1. **Luật Hóa chất số 69/2025/QH15** ngày 14/6/2025, **hiệu lực 01/01/2026** (riêng Giấy chứng nhận dịch vụ tồn trữ tại khoản 5 Điều 14 hiệu lực 01/7/2026). Nền tảng: phân loại hóa chất thành **hóa chất có điều kiện / hóa chất cần kiểm soát đặc biệt / hóa chất cấm** (Điều 9); thẩm quyền cấp GCN đủ điều kiện SX/KD hóa chất có điều kiện thuộc **UBND cấp tỉnh** (Điều 10, 11); GP hóa chất cần kiểm soát đặc biệt và hóa chất cấm thuộc **Bộ, cơ quan ngang Bộ** (Điều 10, 11, 12); KH/Biện pháp phòng ngừa sự cố (Điều 37, 38); huấn luyện an toàn (Điều 36); khai báo hóa chất NK (Điều 12). Bản gốc: `van-ban-goc/01-luat/`.
2. **Nghị định số 24/2026/NĐ-CP** ngày 17/01/2026 — **các danh mục hóa chất** (Phụ lục I: hóa chất cơ bản CN trọng điểm; Phụ lục II: SX-KD có điều kiện; Phụ lục III: cần kiểm soát đặc biệt nhóm 1-2; Phụ lục IV: phải xây dựng KH phòng ngừa - Bảng A chất + ngưỡng, Bảng B hỗn hợp theo GHS). Bản gốc: `van-ban-goc/02-nghi-dinh/`.
3. **Nghị định số 25/2026/NĐ-CP** ngày 17/01/2026 — phát triển CN hóa chất; **an toàn, an ninh hóa chất**; tư vấn chuyên ngành; **huấn luyện an toàn chuyên ngành hóa chất** (Điều 29-32); **Kế hoạch phòng ngừa, ứng phó sự cố hóa chất** (Điều 33-34, thẩm quyền UBND cấp tỉnh tại điểm d khoản 6 Điều 34); **Biện pháp phòng ngừa** (Điều 35); KH cấp tỉnh (Điều 37); khoảng cách an toàn (Điều 28, 35). Bản gốc: `van-ban-goc/02-nghi-dinh/`.
4. **Nghị định số 26/2026/NĐ-CP** ngày 17/01/2026 — **quản lý hoạt động hóa chất**: điều kiện SX/KD (Điều 4-8); **hồ sơ, trình tự cấp GCN đủ điều kiện SX/KD hóa chất có điều kiện** (Điều 9, thẩm quyền UBND cấp tỉnh); hóa chất cần kiểm soát đặc biệt (Điều 11-15); hóa chất cấm (Điều 16-18); **dịch vụ tồn trữ** (Điều 19-20); **miễn trừ - thu hồi** (Điều 21-22); đăng ký hóa chất mới (Điều 23-25); **khai báo hóa chất NK** (Điều 6). Đây là **văn bản nghiệp vụ cốt lõi** của Sở. Bản gốc: `van-ban-goc/02-nghi-dinh/`.
5. **Thông tư số 01/2026/TT-BCT** ngày 17/01/2026 — hướng dẫn Luật + NĐ 26; **PHÂN CẤP TTHC** (Điều 3-4: UBND cấp tỉnh cấp GP hóa chất kiểm soát đặc biệt nhóm 2, GP XNK nhóm 2); mẫu phiếu an toàn hóa chất; **toàn bộ biểu mẫu** (Phụ lục I-XIX; Phụ lục X là biểu mẫu GCN đủ điều kiện SX-KD có điều kiện; Phụ lục XI là dịch vụ tồn trữ). Bản gốc: `van-ban-goc/03-thong-tu/`.
6. **Thông tư số 02/2026/TT-BCT** ngày 17/01/2026 — biện pháp thi hành NĐ 25 (biểu mẫu KH/Biện pháp phòng ngừa, diễn tập, huấn luyện, tư vấn). Bản gốc: `van-ban-goc/03-thong-tu/`.
7. **Nghị định số 146/2025/NĐ-CP** ngày 12/6/2025 về phân quyền, phân cấp lĩnh vực công nghiệp và thương mại. **Lưu ý: các Điều 6, 7, 8, 9 (phần hóa chất) của NĐ 146/2025 đã bị NĐ 26/2026 BÃI BỎ** (khoản 4 Điều 31 NĐ 26) → phần hóa chất áp dụng NĐ 26/2026, không dẫn NĐ 146 cho hóa chất.
8. **Nghị định số 34/2024/NĐ-CP** ngày 27/3/2024 về thực hiện Công ước cấm vũ khí hóa học (CWC) — nhiều Điều đã bị NĐ 26/2026 bãi bỏ; phần hóa chất Bảng CWC nay quản theo NĐ 24 + NĐ 26. Bản gốc: `van-ban-goc/02-nghi-dinh/`.
9. **QCVN 05A:2020/BCT** (Thông tư 48/2020/TT-BCT) **sửa đổi 1:2024** (Thông tư 19/2024/TT-BCT ngày 10/10/2024) — quy chuẩn an toàn trong SX, KD, sử dụng, bảo quản, vận chuyển hóa chất nguy hiểm. **Là căn cứ kỹ thuật cốt lõi khi kiểm tra thực tế/thẩm định điều kiện** (phân khu, không để lẫn chất oxy hóa với chất ăn mòn, thiết bị rửa mắt - tắm khẩn cấp trong 17m, v.v.). Bản gốc: `van-ban-goc/04-qcvn-tcvn/`.
10. **TCVN 5507:2002** — hóa chất nguy hiểm, quy phạm an toàn. Bản gốc: `van-ban-goc/04-qcvn-tcvn/`.

**Khung kiểm tra chuyên ngành:** Luật Thanh tra 84/2025 (sở không còn thanh tra chuyên ngành); **NĐ 217/2025/NĐ-CP** ngày 05/8/2025 (kiểm tra chuyên ngành — văn bản trình tự cốt lõi); **TT 56/2025/TT-BCT** ngày 28/11/2025 (quy trình kiểm tra chuyên ngành Công Thương). Xem reference 10, bản gốc `van-ban-goc/05-xu-phat-kiem-tra/`.

**Khung xử phạt (→ plugin xử phạt riêng):** NĐ 71/2019 sửa bởi NĐ 17/2022 (hóa chất, VLNCN); NĐ 189/2025 (thẩm quyền xử phạt). Bản gốc kèm để dẫn chiếu, không tự lập biên bản VPHC ở plugin này.

## III. CHUỖI THẨM QUYỀN — CỐT LÕI NHẤT (phân định UBND cấp tỉnh / Cục Hóa chất)

Đây là nội dung dễ sai nhất. Khung mới **phân loại hóa chất theo 3 nhóm** và **phân quyền theo nhóm**:

| Việc | Cơ quan có thẩm quyền | Căn cứ |
|---|---|---|
| **GCN đủ điều kiện SẢN XUẤT hóa chất có điều kiện** | **UBND cấp tỉnh** (nơi đặt trụ sở chính hoặc nơi đặt cơ sở SX-KD) | Điều 10 Luật 69/2025; Điều 9 NĐ 26 |
| **GCN đủ điều kiện KINH DOANH hóa chất có điều kiện** | **UBND cấp tỉnh** | Điều 11 Luật 69/2025; Điều 9 NĐ 26 |
| **GCN đủ điều kiện SX và KD hóa chất có điều kiện** | **UBND cấp tỉnh** | Điều 9 NĐ 26 |
| **GCN đủ điều kiện hoạt động dịch vụ tồn trữ hóa chất** (cơ sở thuộc đối tượng Biện pháp/KH do tỉnh thẩm định) | **UBND cấp tỉnh** (hiệu lực 01/7/2026) | Điều 14 Luật; Điều 20 NĐ 26 |
| GCN dịch vụ tồn trữ (cơ sở thuộc đối tượng KH do Bộ thẩm định) | **Bộ Công Thương (Cục Hóa chất)** | Điều 20.2 NĐ 26; Điều 3.2.d TT 01 |
| **GP sản xuất/kinh doanh/SX&KD hóa chất cần kiểm soát đặc biệt NHÓM 2** (tổ chức không có nhóm 1) | **UBND cấp tỉnh** (nơi đặt trụ sở chính) | Điều 3.1.a, Điều 4 TT 01/2026 |
| **GP xuất khẩu, nhập khẩu hóa chất cần kiểm soát đặc biệt NHÓM 2** | **UBND cấp tỉnh** | Điều 3.1.b TT 01/2026 |
| GP hóa chất cần kiểm soát đặc biệt NHÓM 1 (và đồng thời nhóm 1+2) | **Cục Hóa chất** | Điều 3.2.b, c TT 01 |
| GP sản xuất/nhập khẩu hóa chất cấm (công nghiệp) | **Cục Hóa chất / liên Bộ** | Điều 17, 18 NĐ 26; Điều 3.2.a TT 01 |
| Đăng ký hóa chất mới; tiếp nhận khai báo hóa chất NK | **Cục Hóa chất** (Cổng một cửa quốc gia) | Điều 6, 23 NĐ 26; Điều 3.2.đ, e TT 01 |
| **Thẩm định, phê duyệt KH phòng ngừa sự cố** (điểm b khoản 2 Điều 33 — tổng tỉ lệ ≥ 1, không có chất Bảng A/hỗn hợp Bảng B riêng lẻ vượt ngưỡng) | **UBND cấp tỉnh** nơi đặt dự án/cơ sở | Điều 34.6.d NĐ 25 |
| Thẩm định, phê duyệt KH phòng ngừa sự cố (điểm a khoản 2 Điều 33 — có ≥1 chất Bảng A/hỗn hợp Bảng B vượt ngưỡng riêng lẻ) | **Bộ Công Thương (Cục Hóa chất)** | Điều 34.6.c NĐ 25 |
| Biện pháp phòng ngừa sự cố (dưới ngưỡng KH) | **DN tự xây dựng, tự ban hành** (không thẩm định) | Điều 35 NĐ 25 |
| Huấn luyện an toàn hóa chất | **DN tự tổ chức + tự ra QĐ công nhận** (không cấp phép; Sở kiểm tra hồ sơ) | Điều 29-32 NĐ 25 |

**Nguyên tắc bất biến về thẩm quyền:**
- Phạm vi Sở Công Thương Lào Cai tham mưu gồm: GCN đủ điều kiện SX/KD hóa chất có điều kiện; GCN dịch vụ tồn trữ (đối tượng tỉnh); GP hóa chất kiểm soát đặc biệt **nhóm 2** + GP XNK nhóm 2; thẩm định/phê duyệt KH phòng ngừa (điểm b); kiểm tra; báo cáo. **Nhóm 1, hóa chất cấm, đăng ký hóa chất mới, khai báo NK → chuyển đúng đầu mối Cục Hóa chất, không tự nhận.**
- **Ai ký:** thẩm quyền pháp lý là **UBND cấp tỉnh**. Việc ký thực tế phụ thuộc **Quyết định ủy quyền của UBND tỉnh Lào Cai cho Giám đốc Sở Công Thương** — ĐẾN 05/7/2026 CHƯA XÁC MINH đã ban hành. **Phải hỏi Bạn trước khi kết luận người ký.** Nếu chưa ủy quyền: Sở thẩm định, **trình Chủ tịch UBND tỉnh ký** (thực tiễn CV từ chối 4/2026 ghi "Sở không đủ cơ sở tham mưu UBND tỉnh cấp"). Nếu đã ủy quyền: Giám đốc Sở ký (KT.GĐ - PGĐ Hoàng Văn Thuân theo phân công nội bộ khi cấp phép/thẩm định thường lệ).
- **Người soạn - dòng Lưu:** hóa chất → chuyên viên **Nguyễn Thị Loan** → `Lưu: VT, CN(Loan)`. PGĐ phụ trách: **Hoàng Văn Thuân**. Tờ trình/chủ trương → trình trực tiếp **GĐ Hoàng Chí Hiền**. Tra `sct-laocai-org-vn` để chốt.

## IV. CÁC REFERENCE FILES (đọc khi đào sâu)

- `01-tham-quyen-phan-cap.md` — Chi tiết chuỗi thẩm quyền, phân cấp TTHC (Điều 3-4 TT 01), phân định UBND cấp tỉnh/Cục Hóa chất theo nhóm, ai ký, mã TTHC, xử lý câu hỏi "ai cấp việc này".
- `02-dieu-kien-sx-kd-co-dieu-kien.md` — Điều kiện chung an toàn (Điều 4-5 NĐ 26); điều kiện SX/KD hóa chất có điều kiện (Điều 7-8 NĐ 26); trình độ người phụ trách an toàn (ĐH/trung cấp hóa học); yêu cầu nhà xưởng, kho, phân khu.
- `03-ho-so-trinh-tu-gcn-co-dieu-kien.md` — Thành phần hồ sơ cấp/cấp lại/điều chỉnh GCN đủ điều kiện SX/KD hóa chất có điều kiện (Điều 9 NĐ 26); trình tự - thời hạn (12/03/05 ngày làm việc); checklist thẩm định; xử lý hồ sơ khác địa phương.
- `04-hoa-chat-kiem-soat-dac-biet.md` — Nhóm 1 vs nhóm 2; điều kiện, hồ sơ, trình tự GP SX/KD (Điều 11-13 NĐ 26); GP XNK (Điều 14); phân cấp nhóm 2 về tỉnh; phiếu kiểm soát mua bán; công bố mục đích sử dụng.
- `05-dich-vu-ton-tru.md` — Điều kiện (Điều 19 NĐ 26); hồ sơ, trình tự, phân định Bộ/tỉnh (Điều 20); hiệu lực 01/7/2026; quan hệ với điều kiện thuê kho của cơ sở KD.
- `06-ke-hoach-phong-ngua-su-co.md` — Đối tượng KH vs Biện pháp (Điều 33, 35 NĐ 25); công thức tổng tỉ lệ; **trình tự thẩm định KH của UBND cấp tỉnh** (Hội đồng 7-9 người, 15/05/20/10 ngày); QĐ phê duyệt; diễn tập; điều chỉnh KH.
- `07-huan-luyen-an-toan.md` — Đối tượng 3 nhóm (Điều 29 NĐ 25); nội dung, người huấn luyện, thời lượng (8 giờ chu kỳ đầu), kiểm tra, hồ sơ, QĐ công nhận (Điều 30-32); DN tự tổ chức; Sở kiểm tra hồ sơ.
- `08-khai-bao-xnk.md` — Khai báo hóa chất NK qua Cổng một cửa (Điều 6 NĐ 26); miễn trừ khai báo (dưới 10kg, kiểm soát đặc biệt/cấm đã có GP...); XNK hóa chất có điều kiện (Điều 10); thủ tục hải quan.
- `09-thu-hoi-mien-tru.md` — Các trường hợp thu hồi (Điều 19 Luật; Điều 22 NĐ 26); trình tự thu hồi (10 ngày làm việc); miễn cấp GCN/GP (Điều 18 Luật; Điều 21 NĐ 26 — ngưỡng nồng độ 0,1%/1%/5%, sản phẩm miễn trừ).
- `10-kiem-tra-chuyen-nganh.md` — Kiểm tra chuyên ngành hóa chất (NĐ 217/2025, TT 56/2025); lập Đoàn; checklist nội dung kiểm tra (đối chiếu QCVN 05A); biên bản; kết luận; chuyển kiến nghị xử phạt.
- `11-bao-cao-thong-ke.md` — Các loại báo cáo (định kỳ, đột xuất sự cố, chuyên đề); đôn đốc DN; cung cấp thông tin phối hợp (Công an, Quân sự); bộ chỉ tiêu thống kê; báo cáo triển khai chiến lược ngành.
- `12-danh-muc-hoa-chat.md` — Cấu trúc 4 danh mục NĐ 24/2026 (Phụ lục I-IV); cách phân loại một hóa chất (có điều kiện/kiểm soát đặc biệt/cấm/cơ bản); ngưỡng hỗn hợp; hóa chất Bảng CWC; tiền chất công nghiệp; tra nhanh các chất thường gặp ở Lào Cai.
- `13-faq-doanh-nghiep.md` — Bộ câu hỏi - trả lời mẫu để giải đáp doanh nghiệp; ngôn ngữ hướng dẫn chuẩn; các vướng mắc điển hình (khai báo dưới 10kg, chuyển tiếp giấy phép cũ, phân loại hỗn hợp, N2O khí cười).
- `14-bo-mau-van-ban.md` — Bộ mẫu văn bản kết quả của Sở: CV hướng dẫn/từ chối/bổ sung hồ sơ; tờ trình; QĐ (cấp phép, phê duyệt KH, thành lập đoàn kiểm tra/Hội đồng thẩm định); báo cáo; bảng tra "việc → mẫu → reference".
- `15-muc-luc-van-ban-goc.md` — Mục lục tra cứu văn bản gốc (`van-ban-goc/`) và ví dụ thực tế (`vi-du-thuc-te/`): ánh xạ file → nội dung → reference.
- `16-thuc-tien-sct.md` — **Thực tiễn tại Sở (đúc kết hồ sơ đã xử lý 2026):** vụ HNO3 (8 lỗi từ chối cấp GCN); QĐ kiểm tra 04 đơn vị; thể thức văn bản thực tế; các quyết định nghiệp vụ đã chốt; vụ Cục Hóa chất xử phạt DN trên địa bàn (QĐ 26/QĐ-XPVPHC 7/2026 — mức phạt thực tế 4tr hồ sơ huấn luyện + 12tr không báo cáo chemicaldata.gov.vn; NĐ 71/2019 vẫn là khung xử phạt hiện hành); việc chờ xác minh. **ĐỌC TRƯỚC KHI SOẠN bất kỳ văn bản kết quả nào.**
- `mau-ho-so/` — Biểu mẫu DN nộp (Mẫu 10a, 10b, 11a; đề nghị thẩm định KH) + mẫu GCN kết quả (10c); kèm `00-huong-dan-lap-ho-so.md`.

## V. BẢN ĐỒ 6 NGHIỆP VỤ — GẶP VIỆC GÌ ĐỌC GÌ

| Nghiệp vụ | Tình huống | Đọc reference | Mẫu kết quả |
|---|---|---|---|
| **1. Thẩm định cấp phép** | Hồ sơ GCN SX/KD có điều kiện; GCN tồn trữ; GP kiểm soát đặc biệt nhóm 2 | 01, 02, 03 (hoặc 04/05), 16, 12 | Mẫu 10c, GP (ref 14); ví dụ tại vi-du-thuc-te/ |
| **2. Thẩm định KH sự cố** | Hồ sơ KH phòng ngừa (đối tượng điểm b) | 06, 12 | QĐ thành lập Hội đồng, QĐ phê duyệt (ref 14) |
| **3. Hướng dẫn DN** | DN hỏi thủ tục, điều kiện, khai báo, huấn luyện, Biện pháp | 13, 01, 07, 08, 09 | CV hướng dẫn (ref 14) |
| **4. Kiểm tra chuyên ngành** | Lập kế hoạch/tổ chức kiểm tra; phát hiện vi phạm | 10, 02, 16 | QĐ Đoàn, thông báo, biên bản, BC kết quả (ref 14) |
| **5. Báo cáo cấp trên** | Định kỳ/đột xuất/chuyên đề; đôn đốc; cung cấp thông tin | 11 | BC, CV đôn đốc, bản trình (ref 14) |
| **6. Soạn văn bản** | Mọi công văn/tờ trình/QĐ/báo cáo | 14, 16 + `vbhc-vn` | theo bảng ref 14 |
| *(Thu hồi GCN/GP)* | Vi phạm thuộc Điều 19 Luật | 09 | QĐ thu hồi (ref 14) |
| *(Xử phạt VPHC)* | Lập biên bản, ra QĐ xử phạt | → **plugin xử phạt riêng** | (plugin riêng) |

**Bốn câu hỏi gác cổng cho mọi nghiệp vụ:**
1. **Đúng khung pháp lý mới không?** Đã dùng Luật 69/2025 + NĐ 24/25/26/2026 + TT 01/02-2026? DN còn viện dẫn Luật 06/2007, NĐ 113/2017, 82/2022 → lỗi (mục II, ref 16).
2. **Đúng phân loại hóa chất không?** Chất thuộc nhóm nào (có điều kiện / kiểm soát đặc biệt nhóm 1-2 / cấm / cơ bản)? Tra danh mục NĐ 24 (ref 12) trước khi kết luận thủ tục và thẩm quyền.
3. **Đúng thẩm quyền + người ký không?** Việc thuộc UBND cấp tỉnh hay Cục Hóa chất (mục III)? Người ký phụ thuộc QĐ ủy quyền — **đã xác minh chưa** (ref 01, 16)?
4. **Có số/ngày nào đang bịa không?** QĐ ủy quyền, QĐ công bố TTHC, số văn bản nội bộ — xác minh trước, không tự điền.

## VI. NGUYÊN TẮC NGHIỆP VỤ BẤT BIẾN

1. **Số lượng hồ sơ: 01 bộ** cho mọi thủ tục cấp phép (riêng KH phòng ngừa: 01 bộ đề nghị + **09 bản KH**, sau chỉnh sửa nộp 01 bản điện tử + 07 bản in).
2. **Hình thức nộp:** trực tiếp, qua bưu chính, hoặc trực tuyến qua Hệ thống dịch vụ công. Đầu mối tiếp nhận: **Trung tâm Phục vụ Hành chính công tỉnh**; phòng thụ lý: **Phòng Quản lý Công nghiệp**.
3. **Thời hạn giải quyết** (kể từ ngày nhận đủ hồ sơ hợp lệ): GCN đủ điều kiện SX/KD có điều kiện (cơ sở cùng địa phương trụ sở): **12 ngày làm việc** (gồm kiểm tra thực tế); khác địa phương: 03 + 09 + 03 ngày. Cấp lại: **05 ngày làm việc**. Cấp điều chỉnh: như cấp mới. Dịch vụ tồn trữ: **12 ngày làm việc** (tương tự). Thẩm định KH: 15 ngày thẩm định + 05 ngày thông báo + 20 ngày kiểm tra thực tế + 10 ngày phê duyệt (Điều 34 NĐ 25). Đối chiếu Quyết định công bố TTHC mới nhất khi áp dụng cụ thể.
4. **Hồ sơ thiếu/sai:** trong **03 ngày làm việc** thông báo bằng văn bản để bổ sung (thời gian bổ sung không tính vào thời hạn giải quyết).
5. **Từ chối cấp phải trả lời bằng văn bản nêu rõ lý do** (hoặc qua hệ thống dịch vụ công). Mẫu chuẩn: CV từ chối tại vi-du-thuc-te/gcn-tu-choi/.
6. **Kiểm tra thực tế là bắt buộc** trước khi cấp GCN đủ điều kiện SX/KD hóa chất có điều kiện (Điều 9 NĐ 26) và dịch vụ tồn trữ (Điều 20) — lập Biên bản kiểm tra điều kiện thực tế, đối chiếu **QCVN 05A:2020/BCT SĐ1:2024**.
7. **Sau khi cấp:** gửi bản sao GCN/GP đến **Bộ Công Thương (Cục Hóa chất)** và UBND cấp tỉnh nơi đặt trụ sở chính/cơ sở SX-KD để phối hợp quản lý; cập nhật lên Cơ sở dữ liệu chuyên ngành hóa chất (GP kiểm soát đặc biệt: 07 ngày làm việc).
8. **Không tự thêm điều kiện/giấy tờ** ngoài thành phần hồ sơ quy định. Luật quy định gì làm đúng vậy.
9. **Chuyển tiếp (Điều 48 Luật 69/2025):** GP/GCN cấp trước 01/01/2026 tiếp tục dùng đến hết thời hạn; GCN đủ điều kiện SX/KD cũ dùng đến hết **31/12/2027**; hóa chất mới vào Danh mục kiểm soát đặc biệt phải đáp ứng trước **31/12/2026**; BP đã ban hành nhưng thuộc đối tượng KH phải xây KH trình thẩm định trước **31/12/2026** (Điều 40 NĐ 25).
10. **TUYỆT ĐỐI không bịa số/ngày văn bản.** QĐ ủy quyền UBND tỉnh cho GĐ Sở (chưa xác minh), QĐ công bố TTHC, số văn bản nội bộ — xác minh trước khi đưa vào văn bản.

## VII. BỐI CẢNH LÀO CAI

- Đối tượng điển hình: kho hóa chất công nghiệp (axit HNO3, H2SO4, HCl, NaOH, các muối nitrat/clorat); khí công nghiệp (oxy, nitơ, NH3 amoniac); hóa chất phục vụ tuyển khoáng (apatit, đồng), luyện kim, xử lý nước; dịch vụ kho vận - tồn trữ hóa chất và tiền chất thuốc nổ khu vực cửa khẩu/KCN.
- Lào Cai là tỉnh biên giới, có nhiều DN NK hóa chất qua cửa khẩu → lưu ý khai báo hóa chất NK, phối hợp Hải quan; hóa chất kiểm soát đặc biệt/tiền chất công nghiệp gắn với kiểm soát ma túy (QĐ 917/QĐ-UBND về quy chế phối hợp).
- **Ranh giới tránh nhầm:** tiền chất thuốc nổ, VLNCN → plugin VLNCN (dù cùng PGĐ Thuân); vận chuyển hóa chất/HHNH → plugin `hnh-sct-vn`; ĐTM/GPMT dự án hóa chất → plugin `bvmt-sct-vn`; PCCC kho hóa chất → plugin `pccc-sct-vn`; nghiệm thu công trình kho/nhà xưởng (KTCTNT) → plugin `xd-sct-vn`; cơ sở hóa chất trong KCN/CCN → plugin `kcn-ccn-vn`. Nhiều cơ sở tại Lào Cai lưu chứa ĐỒNG THỜI hóa chất và tiền chất thuốc nổ trong một kho → phải kiểm tra phân khu, KH sự cố cho tình huống lưu chứa đồng thời (bài học vụ HNO3, ref 16).
