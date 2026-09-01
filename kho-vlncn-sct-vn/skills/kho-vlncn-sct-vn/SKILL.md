---
name: kho-vlncn-sct-vn
description: "KHO VẬT LIỆU NỔ CÔNG NGHIỆP (VLNCN), Sở Công Thương Lào Cai. Kích hoạt: kho VLNCN, kho tạm, kho cố định, gửi kho, nghiệm thu công trình kho, KTCTNT, kiểm định, phương án nổ mìn (PANM), kho tiền chất thuốc nổ, QCVN 01:2019/BCT. ⭐ PHÂN LUỒNG 4 trường hợp (ref 11) chạy TRƯỚC mọi việc: (A) kho cố định xây mới - có KTCTNT; (B) kho tạm phục vụ thi công - MIỄN GPXD, MIỄN thông báo khởi công, CĐT tự thẩm định thiết kế, MIỄN KTCTNT từ 01/7/2026 (loại trừ k1 Đ25 NĐ 207/2026; chuyển tiếp k3 Đ53 - dừng kiểm tra); (C) kho hiện hữu - kiểm định hiện trạng + quy trình bảo trì (Đ8, Đ34, Đ36 NĐ 207/2026); (D) thuê kho, thuê dịch vụ nổ mìn. Cấp công trình theo TT 34/2026: không có kho cấp III/IV. Nghiệm thu PCCC do CĐT tự tổ chức theo NQ 66.18/2026. Nghiệp vụ khác: hướng dẫn doanh nghiệp, kế hoạch - biên bản - thông báo KTCTNT, gửi kho, PANM, giấy phép sử dụng VLNCN, kiểm tra, báo cáo. Kèm mẫu văn bản, ví dụ thực tế, văn bản gốc."
---

# kho-vlncn-sct-vn — Quản lý nhà nước về kho vật liệu nổ công nghiệp (Sở Công Thương Lào Cai)

## I. KHI NÀO DÙNG SKILL NÀY

Kích hoạt khi xử lý bất kỳ việc nào sau:

- Hướng dẫn doanh nghiệp các bước **chuẩn bị → hồ sơ → điều kiện → thiết kế → thi công → nghiệm thu → đưa vào sử dụng** kho VLNCN (kho mới hoặc kho tạm phục vụ thi công) → reference `03`.
- ⭐ **Chưa biết hồ sơ đi đường nào** (kho mỏ / kho tạm thi công / kho cũ / không xây kho) → chạy PHÂN LUỒNG 3 câu hỏi tại reference `11` TRƯỚC mọi việc khác. Chọn sai luồng là làm thừa hoặc thiếu thủ tục.
- Xây dựng **Kế hoạch kiểm tra công tác nghiệm thu** (KTCTNT), **Biên bản kiểm tra**, **Thông báo kết quả/chấp thuận nghiệm thu** hoàn thành công trình kho VLNCN → reference `04` + mẫu 01, 02, 08.
- Kho **hiện hữu xây từ lâu** (hồ sơ cũ, quy chuẩn cũ) cần tiếp tục sử dụng: hướng dẫn **kiểm định chất lượng**, xác nhận đề cương kiểm định, xác nhận đáp ứng QCVN → reference `05` + mẫu 03, 04, 05.
- Thẩm định, tham mưu **phê duyệt Phương án nổ mìn (PANM) tại khu vực có công trình cần bảo vệ**, dự thảo QĐ của UBND tỉnh → **chủ trì tại `sd-vlncn-sct-vn` (reference 03 + mẫu 07–11, tiền lệ mới nhất)**; reference `07` + mẫu 06, 07, 09 tại đây dùng khi gắn trực tiếp hồ sơ kho.
- Tra cứu **yêu cầu kỹ thuật** kho VLNCN theo QCVN 01:2019/BCT: phân loại kho, sức chứa tối đa, kết cấu, tường rào, ụ bảo vệ, chống sét, PCCC, khoảng cách an toàn → reference `02`.
- **Thẩm định hồ sơ** doanh nghiệp nộp: checklist đầu mục, lỗi thường gặp, cây quyết định → reference `08`.
- Trả lời câu hỏi doanh nghiệp về thủ tục, điều kiện kho → reference `09`.
- Quản lý vận hành kho: lý lịch kho, xuất nhập, bảo vệ, camera, báo cáo định kỳ/đột xuất → reference `10`.
- Xác định **thẩm quyền, ranh giới trách nhiệm** giữa Sở Công Thương – Công an (PCCC, ANTT) – Sở Xây dựng – UBND tỉnh – UBND xã → mục IV dưới đây + reference `06`.

**KHÔNG thuộc plugin này:** cấp Giấy phép vận chuyển VLNCN (**Trưởng phòng PC06 Công an cấp tỉnh** — điểm đ k2 Đ4 TT 75/2024/TT-BCA; khối BQP dùng Mệnh lệnh vận chuyển; plugin `hnh-sct-vn` chỉ xử lý HHNH loại 1 TRỪ VLNCN); xử phạt VPHC (→ plugin `xp-hc-vlncn-sct-vn` theo NĐ 275/2026); huấn luyện KTAT VLNCN chỉ nêu ở mức liên quan hồ sơ (→ `hl-vlncn-sct-vn`). **PANM và Giấy phép sử dụng VLNCN: plugin `sd-vlncn-sct-vn` CHỦ TRÌ** (quy trình thẩm định, mẫu Tờ trình - QĐ đầy đủ, tiền lệ mới nhất) — reference `07` và mẫu 06, 07, 09 tại đây chỉ dùng khi vụ việc gắn trực tiếp hồ sơ kho.

Khi soạn văn bản kết quả: kết hợp skill `vbhc-vn` (thể thức, mẫu), `sct-laocai-org-vn` (người ký, Lưu CN), `vbhc-pdf-reader-vn`/GATE (đọc PDF đến). Khi liên quan PCCC sâu: skill `pccc-sct-vn`.

## II. KHUNG PHÁP LÝ (đã đối chiếu văn bản gốc trong `van-ban-goc/`, cập nhật 7/2026)

Toàn bộ số/ngày đã xác minh. TUYỆT ĐỐI không tự thay số khác. Chi tiết từng văn bản: reference `01`.

**Nhóm 1 — VLNCN chuyên ngành:**
1. **Luật số 42/2024/QH15** ngày 29/6/2024 (hiệu lực 01/01/2025) — Quản lý, sử dụng vũ khí, vật liệu nổ và công cụ hỗ trợ. Điều 38 (điều kiện sử dụng — điểm c: có kho đạt QCVN hoặc hợp đồng thuê kho), Điều 39 (hồ sơ cấp GP sử dụng — điểm đ: văn bản nghiệm thu PCCC đối với kho), Điều 41 (vận chuyển), Điều 42 (trách nhiệm tổ chức).
2. **Luật số 118/2025/QH15** ngày 10/12/2025 (**hiệu lực 01/7/2026**) — sửa đổi, bổ sung 10 luật liên quan an ninh, trật tự. Hai nội dung tác động trực tiếp đến nghiệp vụ kho:
   - **k6 Đ9** sửa **điểm đ khoản 1 Điều 39** Luật 42/2024 thành: *"Bản sao văn bản nghiệm thu về phòng cháy và chữa cháy hoặc văn bản chấp thuận kết quả nghiệm thu về phòng cháy và chữa cháy đối với **kho cố định** chứa vật liệu nổ công nghiệp và điều kiện bảo đảm an toàn theo tiêu chuẩn, quy chuẩn kỹ thuật"* (nguồn: trích nguyên văn tại footnote CV 2826/SCT-CN ngày 19/5/2026 của Sở).
   - ⭐ **k7 điểm a Đ9** sửa **điểm b khoản 2 Điều 40**: tổ chức, DN hoạt động **dịch vụ nổ mìn** phải có kho bảo quản **hoặc GỬI KHO bảo quản** đạt tiêu chuẩn; *"Việc gửi kho phải có **thỏa thuận bằng văn bản** và **thông báo đến Ủy ban nhân dân cấp tỉnh để theo dõi, quản lý**"* → khi thẩm định hồ sơ có phương án gửi kho, kiểm tra đủ 02 điều kiện này; Sở mở sổ theo dõi thông báo gửi kho. Việc gửi kho **không làm giảm** yêu cầu kỹ thuật của kho nhận gửi (QCVN 01:2019/BCT + Điều 15 NĐ 181/2024).
   - **k7 điểm c Đ9** bổ sung **điểm d khoản 4 Điều 40**: DN đã có GP kinh doanh VLNCN thì hồ sơ GP dịch vụ nổ mìn **không bao gồm** giấy tờ tại điểm đ k1 Đ39.
   - 📗 Bản tra cứu hợp nhất: **VBHN số 78/VBHN-VPQH ngày 26/3/2026** trong `van-ban-goc/` — chỉ tra nội dung, **không** dùng làm căn cứ ban hành.
3. **Nghị định số 181/2024/NĐ-CP** ngày 31/12/2024 — quy định chi tiết Luật 42/2024 về VLNCN, tiền chất thuốc nổ. **Điều 15** (quản lý, bảo quản VLNCN — nghĩa vụ của tổ chức sử dụng kho), Điều 16 (kho tiền chất), Điều 4–9 (trình độ chuyên môn, huấn luyện KTAT), Điều 17 (thu hồi giấy phép).
4. **Thông tư số 23/2024/TT-BCT** ngày 07/11/2024 (hiệu lực 01/01/2025) — Điều 4 (thẩm quyền cấp phép), Điều 5 + Phụ lục (mẫu giấy đề nghị/giấy phép), Điều 14 (đánh giá nguy cơ rủi ro), Điều 15 (phương án, hộ chiếu nổ mìn), Điều 16 (kế hoạch ứng cứu khẩn cấp), Điều 17 (báo cáo định kỳ/đột xuất), Điều 19 (trách nhiệm cấp tỉnh — **khoản 5: chức năng cơ quan chuyên môn về xây dựng và PCCC đối với công trình kho VLNCN**).
5. **Thông tư số 38/2025/TT-BCT** ngày 19/6/2025 (hiệu lực 01/7/2025) — Điều 1 sửa TT 23/2024: **thẩm quyền cấp GP sử dụng VLNCN chuyển về UBND cấp tỉnh** (khoản 4 Điều 4 mới), trừ tổ chức có GP khoáng sản do Bộ NN&MT cấp (→ Cục KTAT&MTCN) và Bộ Quốc phòng. Điều 19 đổi thành "Trách nhiệm của UBND cấp tỉnh".
6. **Nghị định số 146/2025/NĐ-CP** ngày 12/6/2025 — phân quyền, phân cấp lĩnh vực công nghiệp và thương mại; Chương về VLNCN: Điều 22–24 (phân quyền/phân cấp: huấn luyện + cấp GCN KTAT VLNCN của Bộ Công Thương → UBND cấp tỉnh).
7a. **QCVN 04:2020/BCT** ban hành kèm **Thông tư số 47/2020/TT-BCT** ngày 21/12/2020 — chất lượng **tiền chất thuốc nổ** dùng để sản xuất VLNCN: chỉ tiêu chất lượng, phương pháp thử, ghi nhãn, hợp quy. **Mục 2.2: bảo quản TCTN thực hiện theo QCVN 01:2019/BCT** (không có bộ yêu cầu kho riêng). Dùng khi kho có bảo quản TCTN hoặc khi kiểm tra nguồn gốc, chất lượng lô TCTN nhập kho.
7. **QCVN 01:2019/BCT** ban hành kèm **Thông tư số 32/2019/TT-BCT** ngày 21/11/2019 (hiệu lực 01/7/2020) — **văn bản kỹ thuật cốt lõi** về kho: Điều 5 (yêu cầu chung: khoảng cách an toàn, thiết bị điện, chống sét, PCCC, môi trường), Điều 21 (kho VLNCN: phân loại, sức chứa, bảo quản chung), Điều 22 (bảo quản tại nơi nổ mìn), Điều 23 (kho tiền chất); Phụ lục 1 (nhóm tương thích), Phụ lục 7 (tính khoảng cách an toàn), Phụ lục 8 (thủ tục xuất nhập kho), Phụ lục 9 (lý lịch kho), **Phụ lục 10 (quy định xây dựng kho, sắp xếp VLNCN)**, Phụ lục 11 (chống sét), Phụ lục 13 (chế độ bảo vệ), Phụ lục 16 (PCCC). Đến 7/2026 chưa có bản sửa đổi thay thế — các văn bản Sở ban hành 5–6/2026 vẫn viện dẫn trực tiếp QCVN 01:2019/BCT.

**Nhóm 2 — Xây dựng (SCT là cơ quan chuyên môn về xây dựng đối với kho VLNCN). ⭐ CẬP NHẬT 29/8/2026 — hai khung theo mốc 01/7/2026, LIÊN KẾT plugin `xd-sct-vn`:**

⭐ **GATE trước khi chọn căn cứ nhóm này**: xác định 3 mốc (khởi công / quyết định đầu tư-phê duyệt thiết kế / thời điểm thực hiện thủ tục KTCTNT) rồi tra bảng quyết định tại **plugin `xd-sct-vn` reference `11-chuyen-tiep-2026.md`**. Một hồ sơ kho có thể dùng HAI khung (vd kho Đồng Tiến 8/2026: khởi công trước 01/7/2026 → miễn GPXD theo Đ89 Luật 2014; thủ tục KTCTNT sau 01/7/2026 → NĐ 207/2026) — khi đó phải có 01 câu lập luận chuyển tiếp trong văn bản. Văn bản gốc cả hai khung nằm ở `xd-sct-vn/van-ban-goc/`.

**Khung HIỆN HÀNH (thủ tục thực hiện từ 01/7/2026):**
8. **Luật Xây dựng số 135/2025/QH15** (hiệu lực 01/7/2026) — điểm a khoản 2 Điều 43 (miễn GPXD công trình tạm), khoản 3 Điều 43 (miễn GPXD vẫn gửi thông báo khởi công), **Điều 72 (công trình tạm** — hết thời hạn phải tháo dỡ, hoàn trả mặt bằng), khoản 4 Điều 57 (KTCTNT), khoản 5 Điều 26 + khoản 3 Điều 29 (thẩm tra thiết kế bắt buộc với công trình AT-LICĐ).
9. **NĐ 207/2026/NĐ-CP ngày 15/6/2026** — **Điều 25-27 (KTCTNT: đối tượng, thẩm quyền CQCM cấp tỉnh, trình tự — CĐT gửi Báo cáo hoàn thành theo Phụ lục VI)**; Điều 28 (hồ sơ hoàn thành); Phụ lục V (mẫu thông báo khởi công). Điều khoản chuyển tiếp: Điều 53.
   ⭐ **Khoản 1 Điều 25 LOẠI TRỪ công trình thuộc điểm a k1 Đ69, các Điều 70, 71 và 72 Luật 135/2025 khỏi nghĩa vụ KTCTNT — Điều 72 là CÔNG TRÌNH TẠM.** Phần loại trừ đứng TRƯỚC cụm "bao gồm" nên chi phối cả 3 điểm a, b, c. Kho tạm vẫn thuộc Phụ lục IV NĐ 217/2026 (mã II.6, cấp II trở lên) nhưng được miễn KTCTNT — phải viết lập luận hai tầng này thành văn. **Khoản 3 Điều 53**: công trình khởi công trước 01/7/2026 thuộc diện KTCTNT theo NĐ 06/2021 nhưng không thuộc diện theo NĐ 207/2026 thì **không tiếp tục thực hiện việc kiểm tra**. Chi tiết + nguyên văn: reference `11`.
   ⚠ Đối chiếu khung cũ: **khoản 1 Điều 24 NĐ 06/2021 KHÔNG có loại trừ công trình tạm** (3 nhóm: dự án quan trọng quốc gia/quy mô lớn; vốn đầu tư công; công trình AT-LICĐ) → các vụ Nậm Cang 1A, Móng Sến 1, Ngòi Nhù 1A KTCTNT theo khung cũ là ĐÚNG, không phải làm thừa.
10. **NĐ 217/2026/NĐ-CP ngày 19/6/2026** — thiết kế, thẩm định (Đ41-43); Phụ lục IV (danh mục công trình AT-LICĐ); chuyển tiếp Điều 76. **TT 34/2026/TT-BXD** — cấp công trình (dự án quyết định đầu tư từ 01/7/2026). **Mã số 1.2.6.8 Phụ lục I (nhóm 1.2.6 Công trình hóa chất): kho hầm lò/kho ngầm = cấp I mọi quy mô; kho cố định nổi và nửa ngầm >10 tấn = cấp I, ≤10 tấn = cấp II; kho lưu động = cấp II mọi quy mô. KHÔNG có kho VLNCN cấp III/IV** → mọi kho đều thuộc ngưỡng "cấp II trở lên" của Phụ lục IV NĐ 217/2026; không tồn tại lập luận "kho nhỏ nên được miễn". **TT 39/2026/TT-BXD** — mã định danh, CSDL quốc gia HĐXD (ghi mã thật hoặc "chưa được cấp", không ghi lấp lửng).
11. **QĐ 11/2026/QĐ-UBND ngày 29/01/2026** của UBND tỉnh Lào Cai — Đ16 (tiếp nhận thông báo khởi công), Đ17 (KTCTNT + kiểm tra PCCC hằng năm). Bản dấu đỏ trong `xd-sct-vn/van-ban-goc/`.

**Khung CŨ (chỉ dùng theo chuyển tiếp — hồ sơ tiếp nhận / công trình khởi công / dự án quyết định đầu tư TRƯỚC 01/7/2026):**
12. **Luật Xây dựng 50/2014** (sđ Luật 62/2020) — điểm c khoản 2 Điều 89 (miễn GPXD), Điều 131 (công trình tạm). **NĐ 06/2021/NĐ-CP** — Điều 23 (KTCTNT); sđ bởi NĐ 35/2023, NĐ 175/2024 (năng lực, CCHN), NĐ 144/2025, NĐ 67/2026. **TT 06/2021/TT-BXD** (sđ **TT 02/2025/TT-BXD**) — phân cấp công trình (kho VLNCN ≤10 tấn: cấp II — tiền lệ CV 2826/SCT-CN). **TT 10/2021/TT-BXD** Điều 5 — kiểm định xây dựng. Toàn văn khung cũ: `xd-sct-vn/van-ban-goc/` (các file hậu tố `-CU`).

**Nhóm 3 — PCCC, ANTT:**
13. **Luật PCCC&CNCH số 55/2024/QH15** ngày 29/11/2024 (hiệu lực 01/7/2025) — điểm a khoản 5 Điều 18 (nghiệm thu về PCCC).
14. **Nghị định 105/2025/NĐ-CP** ngày 15/5/2025 — Điều 6 (thẩm định thiết kế PCCC: 5 nội dung điểm a–đ); Phụ lục I điểm 20, Phụ lục II STT 26, Phụ lục III mục 9 điểm c: **kho cố định chứa VLNCN thuộc diện thẩm định thiết kế PCCC, không phụ thuộc quy mô**; Phụ lục VII STT 24 (bảo hiểm cháy nổ bắt buộc). Phân định: cơ quan chuyên môn về xây dựng (SCT với kho VLNCN) thẩm định 5 nội dung a–đ; cơ quan Công an thẩm định/nghiệm thu các nội dung thuộc thẩm quyền Công an. Chi tiết dùng skill `pccc-sct-vn`.
15. Điều kiện **an ninh, trật tự**: kho VLNCN là ngành nghề đầu tư kinh doanh có điều kiện về ANTT — doanh nghiệp phải có **Giấy chứng nhận đủ điều kiện về ANTT do cơ quan Công an cấp** (đầu mục bắt buộc trong hồ sơ cấp GP sử dụng VLNCN).

**Nhóm 4 — Xử phạt (chỉ tham chiếu, xử lý ở plugin `xp-hc-vlncn-sct-vn`):** **NĐ 275/2026/NĐ-CP ngày 08/7/2026** (hiệu lực 25/8/2026, thay NĐ 71/2019 + Điều 1 NĐ 17/2022) — nhóm bảo quản kho: **Điều 57** (kho không đạt yêu cầu xây dựng-ANTT-PCCC-chống sét: 50–70 tr cá nhân + đình chỉ bảo quản 6–12 tháng; bảo quản vượt quy mô thiết kế: 30–50 tr; để mất VLNCN tại kho: 80–100 tr + tước GP 6–12 tháng; tổ chức ×2). Hành vi kết thúc trước 25/8/2026 → Đ53 NĐ 71/2019 (sđ NĐ 17/2022, bản gốc trong `van-ban-goc/`).

**Văn bản địa phương (Lào Cai):**
- **QĐ 05/2025/QĐ-UBND ngày 01/7/2025** — chức năng, nhiệm vụ Sở Công Thương (căn cứ chuẩn trong mọi văn bản).
- ⭐ **QĐ 2272/QĐ-UBND ngày 29/6/2026** (hiệu lực 01/7/2026) — **Sở Công Thương là cơ quan tiếp nhận hồ sơ** cấp, cấp lại, cấp điều chỉnh **GCN đủ điều kiện sản xuất tiền chất thuốc nổ** trên địa bàn tỉnh; SCT chủ trì thẩm định, Công an tỉnh phối hợp ANTT + PCCC (liên quan trực tiếp khi hồ sơ có hạng mục **kho TCTN** — Đ16 NĐ 181/2024, QCVN 04:2020/BCT). Bản ký: `sd-vlncn-sct-vn/van-ban-goc/2026.06.29-2272.QD.UBND-...pdf`.
- **QĐ 1883/QĐ-UBND ngày 06/11/2025** — UBND tỉnh **ủy quyền Giám đốc Sở Công Thương** thực hiện nhiệm vụ **huấn luyện, kiểm tra, cấp, cấp lại Giấy chứng nhận huấn luyện KTAT VLNCN** (TTHC 2.000229, 2.000210), thời hạn đến hết **28/02/2027** — nội dung chi tiết tại `hl-vlncn-sct-vn/references/01-phap-ly.md` mục C. ⚠ Đây **KHÔNG** phải quyết định ủy quyền cấp Giấy phép sử dụng VLNCN (GP sử dụng vẫn do **Chủ tịch UBND tỉnh** ký, ký hiệu `/GP-UBND`, SCT thẩm định trình). Đã có **bản ký thật** tại `hl-vlncn-sct-vn/van-ban-goc/2025.11.06-1883.QD.UBND-...ban-ky.pdf` — viện dẫn thẳng, không cần xác minh lại.
- ⚠ **NĐ 149/2024/NĐ-CP** ngày 15/11/2024 quy định chi tiết Luật 42/2024 phần **vũ khí, vật liệu nổ QUÂN DỤNG, công cụ hỗ trợ** — **KHÔNG điều chỉnh VLNCN**; không đưa vào căn cứ của văn bản về kho VLNCN.
- **TT 75/2024/TT-BCA** ngày 15/11/2024 — **Giấy phép vận chuyển VLNCN, TCTN do Trưởng phòng PC06 Công an cấp tỉnh cấp** (điểm đ k2 Đ4); nếu nơi có kho tiếp nhận không cấp GP vận chuyển thì **PC06 nơi có kho xác nhận vào Giấy đăng ký tiếp nhận VLNCN, TCTN**; quá cảnh/XNK → Cục trưởng C06 (điểm i k1). Toàn văn tại `sd-vlncn-sct-vn/van-ban-goc/`.
- ➡️ Bản đồ đầy đủ thẩm quyền, nhiệm vụ UBND cấp tỉnh & Sở Công Thương về VLNCN, TCTN: `sd-vlncn-sct-vn/references/10-tham-quyen-ubnd-tinh-va-sct.md`.

## III. NGUYÊN TẮC CỐT LÕI — "MỘT KHO, BỐN TRỤ PHÁP LÝ"

Kho VLNCN phải đồng thời thỏa mãn 4 trụ, thiếu 1 trụ là chưa đủ điều kiện đưa vào sử dụng:

| Trụ | Nội dung | Cơ quan | Kết quả đầu ra |
|---|---|---|---|
| 1. Xây dựng | Thiết kế, thi công, nghiệm thu công trình đúng pháp luật xây dựng | **Sở Công Thương** (cơ quan chuyên môn về xây dựng đối với kho VLNCN — khoản 5 Điều 19 TT 23/2024) | Văn bản chấp thuận kết quả nghiệm thu (TB-SCT) |
| 2. PCCC | Thẩm định thiết kế PCCC, nghiệm thu PCCC | Công an tỉnh (phần thẩm quyền CA) + SCT (5 nội dung a–đ Điều 6 NĐ 105/2025) | Văn bản chấp thuận kết quả nghiệm thu PCCC |
| 3. ANTT | Đủ điều kiện an ninh trật tự | Công an tỉnh | GCN đủ điều kiện về ANTT |
| 4. Kỹ thuật an toàn VLNCN | Đáp ứng QCVN 01:2019/BCT (vị trí, khoảng cách, sức chứa, kết cấu, chống sét, tiếp địa...) | Sở Công Thương thẩm định khi cấp GP sử dụng VLNCN | Giấy phép sử dụng VLNCN (UBND tỉnh/ủy quyền) |

Kho chỉ là **điều kiện thành phần** của Giấy phép sử dụng VLNCN — hoàn thành kho chưa đồng nghĩa được chứa VLNCN; phải có GP sử dụng VLNCN (hoặc hợp đồng thuê kho của đơn vị có phép).

## IV. THẨM QUYỀN — PHÂN ĐỊNH NHANH

- **Cấp GP sử dụng VLNCN:** UBND cấp tỉnh (TT 38/2025, nay Đ4 TT 23/2024 bản TT 26/2026), trừ: tổ chức có GP khoáng sản do Bộ NN&MT cấp → Cục KTAT&MTCN; tổ chức thuộc Bộ Quốc phòng. Tại Lào Cai: đến 19/8/2026 Chủ tịch UBND tỉnh ký `/GP-UBND`; **từ 20/8/2026 GĐ SCT ký theo ủy quyền QĐ 2867/QĐ-UBND ngày 17/8/2026** (đến hết 28/02/2027; QĐ 1883 chỉ ủy quyền GCN huấn luyện — ref 01 mục IV).
- **Kiểm tra công tác nghiệm thu công trình kho VLNCN:** Sở Công Thương (Phòng QLCN chủ trì).
- **PANM tại khu vực có công trình cần bảo vệ:** cơ quan cấp GP sử dụng VLNCN phê duyệt + văn bản đồng ý của UBND cấp tỉnh (điểm d khoản 2 Điều 38 Luật 42/2024). Thực tiễn Lào Cai: SCT thẩm định → Tờ trình → **Chủ tịch UBND tỉnh ký QĐ phê duyệt** (mẫu 06, 07).
- **Huấn luyện, cấp GCN KTAT VLNCN:** UBND cấp tỉnh (NĐ 146/2025 phân cấp từ Bộ Công Thương).
- **Nghiệm thu PCCC, GCN ANTT:** Công an tỉnh.
- **Vận chuyển VLNCN:** giấy phép do cơ quan Công an/Quốc phòng cấp theo Luật 42/2024 — KHÔNG thuộc SCT (khác HHNH các loại khác).

## V. NGƯỜI KÝ, NGƯỜI SOẠN (thực tiễn đã ban hành, khớp `sct-laocai-org-vn`)

- Lĩnh vực VLNCN thuộc **PGĐ Hoàng Văn Thuân** phụ trách → văn bản thường ký **KT. GIÁM ĐỐC / PHÓ GIÁM ĐỐC Hoàng Văn Thuân**. Tờ trình UBND tỉnh quan trọng: GĐ Hoàng Chí Hiền (cân nhắc theo vụ việc).
- **Lưu VT, CN(tên):**
  - Văn bản về **công trình xây dựng kho** (KH kiểm tra, TB kết quả nghiệm thu, xác nhận đề cương kiểm định, CV hướng dẫn/xác nhận QCVN): **CN(Dũng)** — Ngô Ngọc Dũng (thẩm định dự án/công trình công nghiệp).
  - Văn bản về **giấy phép sử dụng VLNCN, PANM**: từ **10/7/2026** dùng **CN(Khôi)** — Trần Đăng Khôi (chuyên viên VLNCN theo Thông báo phân công nội bộ Phòng QLCN 10/7/2026, xem skill `sct-laocai-org-vn`); văn bản trước 6/7/2026 dùng CN(Linh) — Vũ Việt Linh (đúng lịch sử).
- Đoàn kiểm tra thực tế thường gồm: PGĐ Hoàng Văn Thuân (chủ trì), Phó TP QLCN Đỗ Mạnh Cường, CV VLNCN (từ 10/7/2026: Trần Đăng Khôi; trước đó: Vũ Việt Linh), CV Ngô Ngọc Dũng.
- Ký hiệu: công văn `/SCT-CN`; thông báo `/TB-SCT`; tờ trình `/TTr-SCT`; QĐ UBND `/QĐ-UBND`.

## VI. PHÂN LUỒNG 4 TRƯỜNG HỢP RỒI MỚI ĐẾN QUY TRÌNH (chi tiết reference `11`, quy trình Luồng A tại reference `03`)

**BƯỚC 0 — luôn chạy trước:** 3 câu hỏi phân luồng.

```
1. DN có bắt buộc phải TỰ XÂY kho không?
   ├─ Không   → LUỒNG D  thuê kho / thuê dịch vụ nổ mìn (điểm c k1 Đ38 Luật 42/2024)
   └─ Có      → câu 2
2. Kho đã xây, đã dùng từ trước, hồ sơ QLCL không còn đầy đủ?
   ├─ Đúng    → LUỒNG C  kiểm định hiện trạng + quy trình bảo trì (Đ34, Đ36, Đ8 NĐ 207/2026)
   └─ Xây mới → câu 3
3. Kho dùng LÂU DÀI (mỏ, cơ sở SX) hay chỉ phục vụ THI CÔNG công trình chính?
   ├─ Lâu dài → LUỒNG A  đầy đủ, CÓ KTCTNT của SCT
   └─ Thi công→ LUỒNG B  công trình tạm: MIỄN GPXD (điểm a k2 Đ43), MIỄN thông báo khởi công
                         (k3 Đ43), CĐT TỰ thẩm định-phê duyệt thiết kế (k2 Đ72),
                         MIỄN KTCTNT (loại trừ k1 Đ25 NĐ 207/2026)
```

**Quy trình LUỒNG A (kho cố định xây mới — chi tiết reference `03`):**

```
GĐ1 CHUẨN BỊ      → loại kho, vị trí, sức chứa; khoảng cách an toàn (PL7 QCVN); pháp lý dự án
                    gốc (QĐ CTĐT/GP khoáng sản); đất đai; ĐTM/GPMT
GĐ2 THIẾT KẾ      → tư vấn đủ năng lực; thiết kế theo QCVN 01:2019/BCT; thẩm tra; thẩm định
                    thiết kế PCCC; xác định loại - cấp công trình (TT 34/2026)
GĐ3 THI CÔNG      → thông báo khởi công; nhà thầu + TVGS đủ điều kiện; hồ sơ QLCL lập ĐỒNG THỜI
                    với thi công (không lập bù); chống sét - tiếp địa, đủ phiếu đo TỪNG hệ
GĐ4 HOÀN THÀNH    → nghiệm thu nội bộ; nghiệm thu PCCC do CĐT tự tổ chức (NQ 66.18/2026);
                    hồ sơ hoàn công; Báo cáo hoàn thành theo Phụ lục VI NĐ 207/2026; GCN ANTT
GĐ5 SCT KIỂM TRA  → KH kiểm tra → kiểm tra hiện trường + hồ sơ → Biên bản → TB chấp thuận
                    (12 ngày làm việc với công trình cấp II — điểm b k4 Đ27 NĐ 207/2026)
GĐ6 CẤP PHÉP      → hồ sơ GP sử dụng VLNCN (Đ39 Luật 42/2024 + Luật 118/2025); PANM → vận hành
```

**LUỒNG B, C, D:** trình tự và danh mục hồ sơ riêng tại reference `11` mục IV, V, VI.

## VII. ANTI-ERROR RIÊNG CHO LĨNH VỰC NÀY (đúc kết từ bản phản biện hồ sơ Ngòi Nhù 1A — reference 08)

1. **Nhất quán tư cách công trình:** chọn MỘT hướng — "công trình xây dựng tạm" (Điều 72 Luật 135/2025 từ 01/7/2026, trước đó Điều 131 Luật XD 2014: miễn GPXD, CĐT tự thẩm định, phê duyệt thiết kế) HOẶC "công trình thuộc diện thẩm định tại CQCM về xây dựng" — và giữ nhất quán trong toàn bộ hồ sơ, biên bản, thông báo. Không viết "được SCT thẩm định thiết kế" nếu Sở không thẩm định. Tư cách công trình tạm quyết định luôn việc CÓ hay KHÔNG phải KTCTNT (ref 11 mục II).
2. **Trình tự nghiệm thu:** công trình thuộc diện kiểm tra công tác nghiệm thu CHỈ được đưa vào sử dụng sau khi có văn bản chấp thuận (khoản 2 Điều 29 NĐ 207/2026; khung cũ: Điều 23 NĐ 06/2021). Biên bản nghiệm thu của chủ đầu tư không được ghi "bàn giao đưa vào sử dụng từ ngày nghiệm thu".
3. **Đủ 2 đầu mục Công an:** văn bản chấp thuận kết quả nghiệm thu PCCC + GCN đủ điều kiện ANTT (biên bản kiểm tra định kỳ PC03 KHÔNG thay thế văn bản nghiệm thu PCCC).
4. **Không copy sót nội dung vụ khác:** rà tên chủ đầu tư, ngày biên bản, tên xã tại mọi phụ lục.
5. **Năng lực cá nhân phải có minh chứng:** chỉ huy trưởng, TVGS phải có chứng chỉ hành nghề + quyết định giao nhiệm vụ (NĐ 175/2024); giấy ủy quyền ký văn bản phải còn hiệu lực, rõ phạm vi.
6. **Không tự điền số/ngày văn bản chưa ban hành**; số liệu sức chứa, khoảng cách phải khớp thiết kế được duyệt; GATE khi đọc PDF đến.
7. Sau sáp nhập 01/7/2025: địa danh dùng **xã + tỉnh Lào Cai** (không còn cấp huyện); ghi chú vị trí cũ nếu cần như tiền lệ TB Móng Sến 1.
8. **Đủ phiếu đo điện trở cho TỪNG hệ tiếp đất** (đúc kết vụ Đồng Tiến 8/2026): hệ thu sét (≤10Ω) VÀ hệ chống tĩnh điện (theo thiết kế, thường ≤4Ω) là hai phép đo riêng — thiếu một phiếu là chưa đủ căn cứ kết luận hạng mục đạt; không chấp nhận câu "báo cáo hoàn thành nêu yêu cầu" thay cho kết quả đo.
9. **Kế hoạch kiểm tra phát hành TRƯỚC ngày kiểm tra** (tối thiểu 2-3 ngày làm việc) để CĐT chuẩn bị — không ban hành kế hoạch và kiểm tra cùng ngày.
10. **CĐT tự thẩm định thiết kế + tự thi công + tự giám sát ("3 trong 1")**: soi kỹ nhất minh chứng năng lực THEO ĐÚNG KHUNG THỜI ĐIỂM: hoạt động trước 01/7/2026 → chứng chỉ năng lực tổ chức theo NĐ 175/2024 (nếu có) + CCHN cá nhân; từ 01/7/2026 → NĐ 212/2026 đã BÃI BỎ chứng chỉ năng lực tổ chức (tự công khai csdlhdxd.gov.vn, Đ41), CCHN cá nhân chỉ còn 4 lĩnh vực (giám sát vẫn cần, chỉ huy trưởng xét kinh nghiệm), KHÔNG yêu cầu nộp giấy tờ đã có trên CSDL (k4 Đ22) — chi tiết `xd-sct-vn` ref 11 mục 5; cùng với tính độc lập của bộ phận giám sát; kiểm tra file hồ sơ số bằng md5/dung lượng — vụ Đồng Tiến: file "chứng chỉ năng lực doanh nghiệp" nộp nhầm, trùng byte với hồ sơ năng lực của đơn vị tư vấn khác. Biểu thông số kèm TB phải có mục **khoảng cách an toàn theo Phụ lục 7 QCVN 01:2019/BCT** đối chiếu thực tế ↔ tối thiểu theo sức chứa.
11a. **Kho phục vụ MỎ khác kho tạm thi công** (đúc kết vụ Toàn Kim Sơn - Háng Chua Xay 7/2026): KHÔNG phải công trình tạm → căn cứ miễn GPXD phải chỉ rõ điểm, khoản áp dụng; PHẢI chốt phân loại kho cố định/lưu động ngay từ đầu vì quyết định đầu mục nghiệm thu PCCC (điểm đ k1 Đ39 Luật 42/2024 sđ Luật 118/2025 chỉ áp kho CỐ ĐỊNH); kim thu sét KHÔNG được đặt trên mái kho (khoản 1.3 PL11 QCVN — hệ thu sét bố trí riêng biệt theo 2.2); kho vỏ thép bắt buộc hệ chống cảm ứng tĩnh điện ≤5Ω (khoản 2.4 PL11); thời hạn ra TB: 12 ngày làm việc với công trình cấp II kể từ nhận báo cáo hoàn thành (điểm b khoản 4 Điều 27 NĐ 207/2026); biên bản kiểm tra KHÔNG sửa sau khi ký — điều chỉnh bằng phụ lục/biên bản bổ sung có chữ ký các bên; biên bản nghiệm thu của CĐT không đồng nghĩa được đưa vào sử dụng trước khi có TB chấp thuận. Case: `vi-du-thuc-te/toan-kim-son-kho-mo-hang-chua-say-2026/`.
12. ⭐ **KIỂM TRA DIỆN KTCTNT TRƯỚC KHI RA KẾ HOẠCH KIỂM TRA** (đúc kết 31/8/2026, đọc bản gốc NĐ 207/2026): công trình tạm (Điều 72 Luật 135/2025) **KHÔNG thuộc diện KTCTNT** từ 01/7/2026 do phần loại trừ tại khoản 1 Điều 25 NĐ 207/2026; kho tạm khởi công trước 01/7/2026 mà chưa kiểm tra xong thì **DỪNG, không kiểm tra tiếp** (khoản 3 Điều 53). Không suy diễn từ tiền lệ Nậm Cang 1A / Móng Sến 1 / Đồng Tiến sang hồ sơ mới. Khi ban hành văn bản phải viết lập luận HAI TẦNG: kho tạm CÓ thuộc Phụ lục IV NĐ 217/2026 (điểm b k1 Đ25) nhưng bị loại trừ ngay tại phần mở đầu khoản 1. Chi tiết: reference `11`.
13. **Không hợp thức hóa hồ sơ giai đoạn đã qua**: khi kho đã xây xong mà thiếu nhật ký thi công, biên bản nghiệm thu công việc, kết quả thí nghiệm — KHÔNG hướng dẫn DN lập bổ sung hoặc lập lùi ngày, cũng không tự soạn hộ dưới danh nghĩa đơn vị thiết kế/giám sát. Đường đúng là Luồng C (kiểm định hiện trạng). Đây vừa bảo vệ DN vừa bảo vệ người ký văn bản của Sở.
11. **Hồ sơ vắt qua mốc 01/7/2026**: chạy GATE chuyển tiếp tại **plugin `xd-sct-vn` reference `11-chuyen-tiep-2026.md`** trước khi viết căn cứ; nếu dùng hai khung cho hai mốc (miễn GPXD lúc khởi công theo luật cũ; thủ tục KTCTNT theo NĐ 207/2026) thì phải có 01 câu lập luận trong văn bản. Case chuẩn: `vi-du-thuc-te/dong-tien-kho-tam-KTCTNT-2026/`.

14. ⭐ **KHÔNG yêu cầu "nhật ký giám sát"** (kỹ sư phản hồi 31/8/2026, đã đối chiếu bản gốc). Tra toàn văn NĐ 06/2021 và NĐ 207/2026: chỉ có **"nhật ký thi công xây dựng công trình"** do **nhà thầu thi công** lập (khoản 13 Điều 13 NĐ 06/2021 = khoản 13 Điều 15 NĐ 207/2026, mẫu tại Phụ lục IIa). "Nhật ký giám sát" là tài liệu của thế hệ quy định cũ, **không còn trong cả hai nghị định**. Tài liệu đúng của tư vấn giám sát là **"báo cáo về công tác giám sát thi công xây dựng công trình"** — khoản 3 Điều 20 NĐ 207/2026: báo cáo định kỳ hoặc theo giai đoạn thi công (Phụ lục IVa) và báo cáo khi tổ chức nghiệm thu giai đoạn, nghiệm thu hoàn thành gói thầu, hạng mục, công trình (Phụ lục IVb). Nhà thầu thiết kế lập **báo cáo đánh giá việc thực hiện giám sát tác giả** (Điều 21). → Rà mọi công văn, biên bản, checklist trước khi phát hành: yêu cầu DN nộp tài liệu không có trong quy định là **đặt thêm điều kiện trái pháp luật**, và bị DN phản bác đúng.

## VIII. CẤU TRÚC PLUGIN

```
references/
  01-khung-phap-ly.md              Chi tiết từng văn bản, điều khoản then chốt, quan hệ sửa đổi
  02-yeu-cau-ky-thuat-qcvn.md      Phân loại kho, sức chứa, kết cấu, PL10, chống sét, PCCC, khoảng cách
  03-quy-trinh-xay-kho-moi.md      6 giai đoạn hướng dẫn doanh nghiệp, đầu mục hồ sơ từng bước
  04-kiem-tra-cong-tac-nghiem-thu.md  Nghiệp vụ KTCTNT của Sở: trình tự, nội dung, văn bản đầu ra
  05-kho-hien-huu-kiem-dinh.md     Lộ trình kho cũ (tiền lệ Mông Sơn): kiểm định, đề cương, xác nhận
  06-pccc-antt-phan-dinh.md        PCCC (NĐ 105/2025), ANTT, ranh giới SCT - Công an - SXD
  07-panm-giay-phep-su-dung.md     PANM khu vực có công trình cần bảo vệ; hồ sơ GP sử dụng VLNCN
  08-checklist-tham-dinh-loi-thuong-gap.md  Checklist đầu mục + 12 lỗi từ phản biện thực tế
  09-hoi-dap-doanh-nghiep.md       FAQ trả lời doanh nghiệp
  10-van-hanh-bao-cao.md           Lý lịch kho, xuất nhập, bảo vệ, báo cáo định kỳ/đột xuất, kiểm tra
  11-phan-luong-4-truong-hop.md    ⭐ PHÂN LUỒNG 4 trường hợp; cấp công trình TT 34/2026; loại trừ
                                   công trình tạm khỏi KTCTNT (k1 Đ25, k3 Đ53 NĐ 207/2026);
                                   căn cứ kiểm định theo NĐ 207/2026; NQ 66.18/2026 về PCCC
mau-van-ban/                       9 mẫu sẵn dùng (điền chỗ trống là ban hành được)
vi-du-thuc-te/                     Văn bản Sở đã ban hành 4 vụ việc thật + bản phản biện hồ sơ
  dong-tien-kho-tam-KTCTNT-2026/   Case CHUẨN kho tạm theo khung mới (KH 4826, BB 11/8, TB 5088/TB-SCT)
                                   + README-BAI-HOC: 8 điểm làm đúng, 6 điểm rút kinh nghiệm
  toan-kim-son-kho-mo-hang-chua-say-2026/  Case kho phục vụ MỎ chì kẽm (KH 4168, TB 4566/TB-SCT)
                                   + README: 9 vấn đề (kim thu sét trên mái, phân loại kho - PCCC,
                                   quá hạn Đ27, biên bản bị sửa sau ký) + bảng so sánh 2 case
van-ban-goc/                       TT 32/2019 (QCVN 01:2019/BCT), Luật 42/2024, NĐ 181/2024,
                                   TT 23/2024, TT 38/2025, NĐ 146/2025, NĐ 71/2019, NĐ 17/2022, NĐ 149/2024
```

## IX. QUY TẮC LÀM VIỆC

1. Trả lời/soạn thảo bằng tiếng Việt, văn phong hành chính.
2. Trước khi viện dẫn văn bản đến (PDF): chạy GATE trích số/ngày/người ký từ file.
3. Không dùng dữ liệu hiện trạng (tên doanh nghiệp đang làm hồ sơ, tiến độ) từ skill làm dữ liệu thời sự — hỏi Bạn số liệu mới nhất.
4. Mọi mẫu văn bản khi xuất docx: theo thể thức NĐ 30/2020 qua skill `vbhc-vn`; render kiểm tra trước khi giao.
5. Khi số văn bản địa phương chưa chắc chắn (QĐ ủy quyền, QĐ quản lý xây dựng của tỉnh): để trống + hỏi Bạn, không đoán.
