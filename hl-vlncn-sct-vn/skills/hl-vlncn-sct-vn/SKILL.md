---
name: hl-vlncn-sct-vn
description: "Chuyên gia QLNN về HUẤN LUYỆN, KIỂM TRA, CẤP GIẤY CHỨNG NHẬN huấn luyện kỹ thuật an toàn (GCN KTAT) vật liệu nổ công nghiệp (VLNCN) và tiền chất thuốc nổ (TCTN) của Sở Công Thương Lào Cai. 5 nghiệp vụ: (1) tiếp nhận, thẩm định hồ sơ đề nghị của doanh nghiệp (Mẫu 01, 02 NĐ 181/2024), phân biệt 2 chế độ: người quản lý (Sở huấn luyện + kiểm tra) và các đối tượng khác (DN tự huấn luyện, Sở kiểm tra); (2) soạn trọn chuỗi văn bản: Kế hoạch KH-SCT, Thông báo tổ chức, QĐ thành lập/kiện toàn Tổ kiểm tra, Báo cáo kết quả, QĐ công nhận kết quả + cấp GCN (GĐ Sở ký theo ủy quyền QĐ 1883/QĐ-UBND); (3) hướng dẫn DN điều kiện trình độ Đ4, hồ sơ, thời hạn, cấp lại; (4) kiểm tra, xử phạt; (5) báo cáo UBND tỉnh. Kèm mẫu + ví dụ thực tế + văn bản gốc. Từ khóa: GCN huấn luyện KTAT VLNCN, huấn luyện kiểm tra sát hạch, người quản lý VLNCN, chỉ huy nổ mìn, thợ nổ mìn, thủ kho, người phục vụ, TCTN, NĐ 181/2024 Điều 4-9, NĐ 146/2025 Điều 24, QĐ 1883/QĐ-UBND, TTHC 2.000229, 2.000210, 6/10 điểm, GCN 2 năm, Tổ kiểm tra."
---

# hl-vlncn-sct-vn — Huấn luyện, kiểm tra, cấp GCN KTAT VLNCN & TCTN (Sở Công Thương Lào Cai)

## I. KHI NÀO DÙNG SKILL NÀY

Kích hoạt khi xử lý bất kỳ việc nào sau:

- **Tiếp nhận hồ sơ đề nghị của doanh nghiệp** (Giấy đề nghị Mẫu 01 + danh sách Mẫu 02 NĐ 181/2024): kiểm tra tính đầy đủ, hợp lệ; đối chiếu điều kiện trình độ Điều 4 → reference `02`/`03` + checklist.
- **Soạn chuỗi văn bản tổ chức một kỳ huấn luyện/kiểm tra**: Kế hoạch (/KH-SCT), Thông báo tổ chức (/SCT-CN), Báo cáo kết quả của Tổ kiểm tra, Quyết định công nhận kết quả + cấp GCN (/QĐ-SCT), danh sách kèm theo, Giấy chứng nhận Mẫu 03 → mẫu 01–07 + ví dụ thực tế.
- **QĐ thành lập/kiện toàn/bổ sung Tổ kiểm tra, cấp GCN** → mẫu 08.
- **Trả lời, hướng dẫn doanh nghiệp**: điều kiện chuyên môn từng chức danh, hồ sơ, nơi nộp, thời hạn, cấp lại, huấn luyện định kỳ/lại, TCTN; văn bản trả hồ sơ không hợp lệ/không đủ điều kiện → reference `04` + mẫu 09, 10 (tiền lệ HTX Văn Thịnh, Cty Duy Hiếu).
- **Kiểm tra việc chấp hành pháp luật** về quản lý, bảo quản, sử dụng VLNCN (trong đó có kiểm tra GCN huấn luyện của người lao động): QĐ thành lập đoàn, KH kiểm tra, biên bản, báo cáo, thông báo kết quả sau kiểm tra; hành vi – mức phạt NĐ 71/2019 (Đ50: bố trí người chưa huấn luyện) → reference `06` + mẫu 11–12.
- **Báo cáo** UBND tỉnh định kỳ hằng năm/đột xuất về thực hiện nhiệm vụ ủy quyền (điểm đ khoản 2 Điều 3 QĐ 1883/QĐ-UBND) → reference `06` + mẫu 13.
- Tra cứu **ví dụ thực tế 2025–2026 của Lào Cai** → reference `07` + thư mục `vi-du-thuc-te/`.

**Ranh giới, liên kết với plugin khác:**
- Giấy phép SỬ DỤNG VLNCN + Phương án nổ mìn → `sd-vlncn-sct-vn` (điều kiện nhân sự Đ4 và GCN huấn luyện là đầu mục cứng của hồ sơ cấp GP sử dụng — hai plugin dùng chung Điều 4 NĐ 181).
- Kho VLNCN (thiết kế, nghiệm thu, kiểm định; huấn luyện thủ kho là điều kiện "4 trụ" của kho) → `kho-vlncn-sct-vn`.
- Vận chuyển VLNCN → Công an cấp phép, KHÔNG thuộc SCT (`hnh-sct-vn` chỉ xử lý HHNH trừ VLNCN, tiền chất thuốc nổ).
- Soạn văn bản: kết hợp `vbhc-vn` (thể thức), `sct-laocai-org-vn` (người ký, dòng Lưu), GATE/`vbhc-pdf-reader-vn` khi đọc PDF đến.

## II. KHUNG PHÁP LÝ (đã đối chiếu văn bản gốc, cập nhật 7/2026 — chi tiết: reference `01`)

TUYỆT ĐỐI không tự thay số/ngày khác. Đã xác minh từ văn bản gốc và hồ sơ Sở đã ban hành.

1. **Luật số 42/2024/QH15 ngày 29/6/2024** (hiệu lực 01/01/2025) — Quản lý, sử dụng vũ khí, vật liệu nổ và công cụ hỗ trợ. ⚠️ Một số Kế hoạch cũ của Sở ghi "ngày 26 tháng 8 năm 2024" — SAI, không lặp lại; QĐ công nhận đã dùng đúng "ngày 29/6/2024".
2. **Nghị định số 181/2024/NĐ-CP ngày 31/12/2024** (hiệu lực 01/01/2025) — văn bản LÕI của lĩnh vực:
   - **Điều 4**: trình độ chuyên môn (người quản lý, người phân tích thử nghiệm, chỉ huy nổ mìn, thợ nổ mìn);
   - **Điều 5**: 7 nhóm đối tượng phải huấn luyện KTAT VLNCN;
   - **Điều 6**: thẩm quyền cấp GCN = cơ quan cấp GP sử dụng/GCN đủ điều kiện sản xuất/GP kinh doanh/GP dịch vụ nổ mìn (trừ Bộ Quốc phòng);
   - **Điều 7**: nội dung huấn luyện theo từng đối tượng (8 khoản);
   - **Điều 8**: tổ chức huấn luyện — cơ quan có thẩm quyền huấn luyện NGƯỜI QUẢN LÝ; DN tự huấn luyện các đối tượng còn lại; tiêu chuẩn người huấn luyện (khoản 3); hình thức lần đầu (16 giờ; riêng người quản lý 12 giờ)/định kỳ 02 năm (½ thời gian)/huấn luyện lại (½ thời gian);
   - **Điều 9**: thủ tục — hồ sơ Mẫu 01+02+02 ảnh 3x4+bằng cấp; 05 ngày thông báo kế hoạch (02 ngày trả lời nếu hồ sơ chưa hợp lệ); 10 ngày tổ chức huấn luyện/kiểm tra; đạt từ **6/10 điểm**; 05 ngày cấp GCN Mẫu 03; **cấp lại 03 ngày** (mất, hư hỏng, thay đổi thông tin — hiệu lực như GCN cũ); nộp qua Cổng DVC quốc gia/Hệ thống TTHC tỉnh/bưu chính/trực tiếp; **GCN hiệu lực 02 năm, giá trị toàn quốc**;
   - **Điều 10–14**: TCTN — đối tượng là người quản lý kho TCTN (đã có GCN VLNCN thì MIỄN — k2 Đ10); DN tự huấn luyện 12 giờ; Sở kiểm tra, cấp GCN trong 03 ngày sau kiểm tra;
   - **Điều 17**: thủ tục thu hồi giấy phép, GIẤY CHỨNG NHẬN (Mẫu 04, 05);
   - **điểm b khoản 1 Điều 18** + khoản 4 Điều 18 (trách nhiệm UBND các cấp); **Điều 20** (chuyển tiếp: GCN cũ dùng đến hết hạn).
3. **Nghị định số 146/2025/NĐ-CP ngày 12/6/2025** — **khoản 1 Điều 24**: nhiệm vụ huấn luyện, kiểm tra, cấp, cấp lại GCN huấn luyện KTAT VLNCN của Bộ Công Thương (k1 Đ6, Đ9, điểm b k1 Đ18 NĐ 181) chuyển về **UBND cấp tỉnh**; trình tự tại Phụ lục VII.
4. **Nghị định số 139/2025/NĐ-CP ngày 12/6/2025** — phân định thẩm quyền 02 cấp lĩnh vực QLNN của Bộ Công Thương (căn cứ trong QĐ ủy quyền).
5. **Thông tư số 38/2025/TT-BCT ngày 19/6/2025** — sửa đổi phân cấp TTHC của Bộ Công Thương (căn cứ ban hành; nội dung huấn luyện không thay đổi so với NĐ 181).
6. **QĐ số 1883/QĐ-UBND ngày 06/11/2025** của UBND tỉnh Lào Cai — **ỦY QUYỀN GIÁM ĐỐC SỞ CÔNG THƯƠNG** thực hiện huấn luyện, kiểm tra, cấp, cấp lại GCN huấn luyện KTAT VLNCN (TTHC **2.000229** cấp, **2.000210** cấp lại); hiệu lực **đến hết ngày 28/02/2027**; GĐ không được ủy quyền tiếp; dùng hình thức văn bản, con dấu của Sở; báo cáo UBND tỉnh hằng năm/đột xuất. (Trình tại TTr 2205/TTr-SCT ngày 28/10/2025; PCT Nguyễn Thành Sinh ký TM. UBND, KT. CHỦ TỊCH.)
7. **QĐ số 05/2025/QĐ-UBND ngày 01/7/2025** — chức năng, nhiệm vụ SCT.
8. **Văn bản nội bộ Sở:** QĐ số **2797/QĐ-SCT ngày 28/11/2025** thành lập Tổ kiểm tra, cấp GCN huấn luyện KTAT VLNCN, TCTN; QĐ số **564/QĐ-SCT ngày 31/01/2026** bổ sung thành viên Tổ kiểm tra.
9. **Xử phạt:** NĐ 71/2019/NĐ-CP (sđ NĐ 17/2022) — **Điều 50**: bố trí người chưa được huấn luyện/kiểm tra không đạt/không đủ trình độ làm công việc liên quan VLNCN (chi tiết → `sd-vlncn-sct-vn` reference 05); kiểm tra Nghị định thay thế NĐ 71/2019 trước khi viện dẫn.
10. **TT 09/2026/TT-BQP ngày 22/01/2026** chỉ áp dụng khối Bộ Quốc phòng — KHÔNG ảnh hưởng thẩm quyền Sở.

## III. THẨM QUYỀN — PHÂN ĐỊNH NHANH (từ 06/11/2025)

| Việc | Cơ quan | Ghi chú |
|---|---|---|
| Huấn luyện + kiểm tra + cấp GCN cho **NGƯỜI QUẢN LÝ** | **GĐ Sở Công Thương** (ủy quyền QĐ 1883); Sở biên soạn tài liệu, tổ chức huấn luyện 12h rồi kiểm tra | k1 Đ7, điểm a k1 Đ8, k1 Đ9 NĐ 181 |
| Kiểm tra + cấp GCN cho **các đối tượng khác** (thủ kho, chỉ huy nổ mìn, thợ mìn, người phục vụ, người sản xuất, người phân tích thử nghiệm) | **GĐ Sở Công Thương**; DN TỰ huấn luyện (16h) trước, nộp kèm kế hoạch + tài liệu huấn luyện + bằng cấp người huấn luyện | k2 Đ8, k2 Đ9 NĐ 181 |
| Cấp lại GCN (mất, hỏng, đổi thông tin) | GĐ Sở Công Thương — 03 ngày làm việc | k3 Đ9; TTHC 2.000210 |
| Kiểm tra + cấp GCN KTAT **TCTN** (người quản lý kho TCTN) | Cơ quan chuyên môn thuộc UBND tỉnh = Sở Công Thương | Đ11, Đ14 NĐ 181; đã có GCN VLNCN → miễn (k2 Đ10) |
| Thu hồi GCN | Cơ quan đã cấp (GĐ SCT) | Đ17 NĐ 181, Mẫu 04–05 |
| Tổ chức, DN thuộc **Bộ Quốc phòng** | Cục Quản lý Công nghệ/cơ quan được BQP giao | k2 Đ6, k2 Đ11 NĐ 181; TT 09/2026/TT-BQP |
| Kiểm tra, xử phạt việc chấp hành (kể cả bố trí người chưa huấn luyện) | SCT chủ trì kiểm tra; xử phạt theo NĐ 71/2019 | Đ50 NĐ 71/2019 |

## IV. NGƯỜI KÝ, NGƯỜI SOẠN (khớp `sct-laocai-org-vn` + văn bản đã ban hành 2026)

- **QĐ công nhận kết quả + cấp GCN, QĐ thành lập Tổ/Đoàn**: **GIÁM ĐỐC Hoàng Chí Hiền ký trực tiếp** (nhiệm vụ ủy quyền đích danh cho Giám đốc — không dùng KT. thường xuyên). Khi GĐ vắng: PGĐ ký phải có **Giấy ủy quyền công tác đích danh** và đưa GUQ vào phần căn cứ (tiền lệ: GUQ 2180/GUQ-SCT ngày 21/4/2026 → PGĐ Trịnh Văn Thành ký QĐ công nhận cho Cty Hóa chất mỏ Tây Bắc).
- **Kế hoạch, Thông báo, Công văn trả lời DN**: ký **KT. GIÁM ĐỐC / PHÓ GIÁM ĐỐC Hoàng Văn Thuân** (PGĐ phụ trách VLNCN).
- **Báo cáo kết quả của Tổ kiểm tra**: Tổ trưởng ký, kính gửi Giám đốc Sở; tiêu đề cơ quan "SỞ CÔNG THƯƠNG / TỔ KIỂM TRA THEO KẾ HOẠCH [số]"; văn bản Đoàn kiểm tra chấp hành pháp luật dùng ký hiệu `/ĐKT-SCT`, `/KH-ĐKT`.
- **Dòng Lưu**: văn bản thực tế 2026 — QĐ công nhận kết quả dùng **CN(Linh)** (Vũ Việt Linh — chuyên viên VLNCN theo skill tổ chức); KH/TB/CV và văn bản đoàn kiểm tra dùng **CN(M.Cường)**. Mặc định theo người trực tiếp tham mưu hồ sơ; không rõ thì **hỏi Bạn** — tuyệt đối không điền tên lãnh đạo phòng.
- Ký hiệu: Kế hoạch `/KH-SCT`; Thông báo tổ chức bằng công văn `/SCT-CN` (một số kỳ dùng `/TB-SCT` cho thông báo kết quả); QĐ `/QĐ-SCT`; báo cáo Đoàn kiểm tra `/ĐKT-SCT`.

## V. HAI QUY TRÌNH LÕI + CHUỖI VĂN BẢN (chi tiết reference `02`, `03`)

**A. Người quản lý (Sở huấn luyện + kiểm tra + cấp GCN):**
```
DN nộp hồ sơ (Cổng DVC quốc gia / Hệ thống TTHC tỉnh / bưu chính / trực tiếp):
  Mẫu 01 + Mẫu 02 + 02 ảnh 3x4 + bản sao bằng đại học đúng ngành k1 Đ4
→ Sở kiểm tra hồ sơ: chưa hợp lệ → CV trả lời nêu rõ lý do trong 02 ngày (mẫu 09;
  tiền lệ Văn Thịnh: kỹ sư cơ khí KHÔNG thuộc k1 Đ4 → từ chối)
→ Trong 05 ngày làm việc: ban hành KẾ HOẠCH /KH-SCT (mẫu 02) — gộp nhiều DN một kỳ
  + THÔNG BÁO /SCT-CN gửi DN (mẫu 04): thời gian 1,5 ngày (12h huấn luyện + kiểm tra),
  địa điểm, đối tượng, nội dung dẫn ĐIỀU 7 NĐ 181
→ Trong 10 ngày kể từ thông báo: Tổ kiểm tra (QĐ 2797 + 564) tổ chức huấn luyện
  (tài liệu do Sở biên soạn) + kiểm tra viết/vấn đáp, chấm theo thang 10, đạt ≥ 6/10
→ Tổ trưởng lập BÁO CÁO kết quả (mẫu 06) → GĐ ký QĐ CÔNG NHẬN KẾT QUẢ /QĐ-SCT
  kèm danh sách (mẫu 05) → trong 05 ngày kể từ kết thúc kiểm tra: cấp GCN Mẫu 03
  (GĐ ký, dấu Sở, khổ 190x130 mm) → vào sổ theo dõi, lưu hồ sơ
```

**B. Các đối tượng khác — thủ kho, chỉ huy nổ mìn, thợ mìn, người phục vụ… (DN huấn luyện, Sở kiểm tra + cấp GCN):**
```
DN TỰ tổ chức huấn luyện (16h lần đầu; định kỳ/lại = 8h) bằng người huấn luyện đạt k3 Đ8
→ nộp hồ sơ: Mẫu 01 + Mẫu 02 + 02 ảnh 3x4 + KẾ HOẠCH huấn luyện + TÀI LIỆU huấn luyện
  chi tiết từng đối tượng + bằng cấp người huấn luyện (và bằng cấp k2, k3 Đ4 nếu có
  người quản lý DN kinh doanh / người phân tích thử nghiệm)
→ Sở: 05 ngày thông báo kế hoạch kiểm tra (KH /KH-SCT + TB /SCT-CN — nội dung dẫn ĐIỀU 9;
  DN đông người: chia đợt như Sin Quyền 2 đợt x 100 người; có thể kiểm tra tại trụ sở DN)
→ 10 ngày tổ chức kiểm tra → chấm ≥ 6/10 → BC Tổ kiểm tra → QĐ công nhận + cấp GCN (05 ngày)
→ Không đạt → DN huấn luyện lại (½ thời gian) và đăng ký kiểm tra lại;
  DN không cử người tham dự → CV thông báo không đủ điều kiện cấp (tiền lệ Duy Hiếu, mẫu 10)
```

**C. Cấp lại:** Mẫu 01 + Mẫu 02 + 02 ảnh — 03 ngày làm việc, hiệu lực theo GCN cũ.
**D. TCTN:** như B nhưng huấn luyện 12h, nội dung Đ12, cấp GCN trong 03 ngày sau kiểm tra (Đ14); đã có GCN VLNCN → miễn.

## VI. ANTI-ERROR RIÊNG LĨNH VỰC NÀY (đúc kết từ hồ sơ thật 2025–2026)

1. **Không nhầm 2 chế độ:** người quản lý → Sở huấn luyện (Thông báo dẫn **Điều 7** NĐ 181, thời gian **1,5 ngày**); đối tượng khác → Sở chỉ kiểm tra (Thông báo dẫn **Điều 9**, DN phải nộp kèm kế hoạch + tài liệu huấn luyện + bằng cấp người huấn luyện). Hồ sơ đối tượng khác thiếu 3 đầu mục này là chưa hợp lệ.
2. **Trình độ người quản lý phải đúng khoản 1 Điều 4** (12 ngành kỹ thuật: hóa chất; vũ khí; vật liệu nổ; chỉ huy kỹ thuật công binh; khai thác mỏ; kỹ thuật mỏ; địa chất; xây dựng công trình; giao thông; thủy lợi; địa vật lý; dầu khí). Ngành gần đúng vẫn từ chối — tiền lệ HTX Văn Thịnh (kỹ sư Công nghệ kỹ thuật cơ khí → không đủ điều kiện, CV 3155/SCT-CN nêu đích danh căn cứ, đề nghị bố trí nhân sự khác). Chỉ huy nổ mìn/thợ mìn kiểm tra thêm thâm niên (k4, k5 Đ4).
3. **QĐ công nhận + GCN do GIÁM ĐỐC ký trực tiếp** (chủ thể căn cứ mở đầu: "GIÁM ĐỐC SỞ CÔNG THƯƠNG TỈNH LÀO CAI"); GĐ vắng → PGĐ ký kèm Giấy ủy quyền công tác đưa vào căn cứ. KH/TB ký KT. GĐ — PGĐ Hoàng Văn Thuân.
4. **Bộ căn cứ chuẩn của QĐ công nhận** (theo QĐ 3728, 3770 đã ban hành): Luật 42/2024 (29/6/2024) → NĐ 181/2024 + NĐ 146/2025 → TT 23/2024 + TT 38/2025 → QĐ 05/2025/QĐ-UBND → QĐ 1883/QĐ-UBND → QĐ 2797/QĐ-SCT + QĐ 564/QĐ-SCT + Kế hoạch số …/KH-SCT của kỳ đó → "Theo đề nghị của Tổ trưởng Tổ kiểm tra…". Không bỏ sót Kế hoạch của kỳ.
5. **Luật 42/2024 ngày 29/6/2024** — không chép lại lỗi "26/8/2024" trong một số KH cũ.
6. **Thang điểm đạt ≥ 6/10;** không đạt → huấn luyện lại ½ thời gian rồi mới kiểm tra lại; GCN **02 năm, toàn quốc**; huấn luyện **định kỳ 02 năm/lần** — nhắc DN đăng ký trước khi GCN hết hạn; thợ nổ mìn/người sản xuất nghỉ việc ≥ 06 tháng hoặc đổi công nghệ → huấn luyện lại.
7. **Bám sát thời hạn 05–02–10–05 (cấp lại 03) ngày làm việc** của Đ9; quá hạn là vi phạm TTHC.
8. **Miễn TCTN** khi đã có GCN VLNCN còn hiệu lực (k2 Đ10) — không bắt DN làm 2 thủ tục.
9. **Ủy quyền hết hạn 28/02/2027** — tham mưu trình UBND tỉnh QĐ ủy quyền mới/gia hạn trước thời điểm này; không được ủy quyền tiếp cho cấp dưới.
10. **Phí, lệ phí:** TTHC 2.000229/2.000210 công bố hiện hành không quy định phí — xác minh lại khi có công bố mới trước khi trả lời DN.
11. **Không tự điền số/ngày** văn bản chưa ban hành ("Số:      /QĐ-SCT"); GATE bắt buộc khi đọc PDF đến; địa danh sau 01/7/2025 ghi xã/phường + tỉnh Lào Cai; render-and-verify mọi file .docx trước khi bàn giao.
12. **Kỳ kiểm tra đông người** (như Sin Quyền ~200): chia đợt trong Thông báo, ghi rõ số thứ tự từng chức danh theo danh sách DN đã đăng ký; có thể tổ chức tại trụ sở DN (tiền lệ Hóa chất mỏ Tây Bắc).

## VII. CẤU TRÚC PLUGIN

```
hl-vlncn-sct-vn/
├── SKILL.md                              ← file này
├── CHANGELOG.md
├── references/
│   ├── 01-phap-ly.md                     ← trích toàn văn Đ4–9, 10–14, 17, 18, 20 NĐ 181;
│   │                                        Đ24 NĐ 146/2025; nội dung QĐ 1883/QĐ-UBND
│   ├── 02-quy-trinh-nguoi-quan-ly.md     ← quy trình A + checklist thẩm định + tổ chức lớp
│   ├── 03-quy-trinh-doi-tuong-khac.md    ← quy trình B, C (cấp lại), D (TCTN) + checklist
│   ├── 04-huong-dan-dn.md                ← hướng dẫn doanh nghiệp A→Z + FAQ + bảng trình độ Đ4
│   ├── 05-noi-dung-huan-luyen-kiem-tra.md← nội dung Đ7 (8 khoản) & Đ12 theo từng đối tượng;
│   │                                        định hướng ra đề, chấm điểm
│   ├── 06-kiem-tra-bao-cao.md            ← kiểm tra chấp hành pháp luật (chuỗi QĐ 1050→KH 1105
│   │                                        →BC 1883/ĐKT→TB 1894); xử phạt Đ50; báo cáo UBND tỉnh
│   └── 07-vi-du-thuc-te.md               ← index ví dụ thật kèm metadata đã GATE
├── mau-van-ban/                          ← 14 mẫu sẵn dùng (xem 00-MUC-LUC.md)
├── vi-du-thuc-te/                        ← file .docx thật đã ban hành 2026 (nguồn RAR Bạn cấp)
└── van-ban-goc/                          ← NĐ 181/2024 toàn văn; QĐ ủy quyền + Phụ lục (dự thảo
                                             trình kèm TTr 2205 — bản ban hành: QĐ 1883/QĐ-UBND)
```
