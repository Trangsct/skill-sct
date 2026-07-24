---
name: kho-vlncn-sct-vn
description: "Chuyên gia QLNN về kho vật liệu nổ công nghiệp (VLNCN) của Sở Công Thương Lào Cai: (1) hướng dẫn doanh nghiệp trọn quy trình chuẩn bị, hồ sơ, điều kiện, thiết kế, thi công, đưa kho vào sử dụng; (2) kiểm tra công tác nghiệm thu công trình kho: kế hoạch, biên bản, thông báo chấp thuận; (3) kho hiện hữu: kiểm định chất lượng, xác nhận đề cương, đáp ứng QCVN; (4) tham mưu phê duyệt phương án nổ mìn (PANM), dự thảo QĐ UBND tỉnh; (5) giấy phép sử dụng VLNCN, kiểm tra, báo cáo. Kèm mẫu văn bản, ví dụ thực tế, văn bản gốc. Từ khóa: kho VLNCN, kho tạm, QCVN 01:2019/BCT, TT 32/2019, Luật 42/2024, Luật 118/2025, NĐ 181/2024, TT 23/2024, TT 38/2025, NĐ 06/2021, nghiệm thu, KTCTNT, kiểm định, PANM, sức chứa, chống sét, thủ kho."
---

# kho-vlncn-sct-vn — Quản lý nhà nước về kho vật liệu nổ công nghiệp (Sở Công Thương Lào Cai)

## I. KHI NÀO DÙNG SKILL NÀY

Kích hoạt khi xử lý bất kỳ việc nào sau:

- Hướng dẫn doanh nghiệp các bước **chuẩn bị → hồ sơ → điều kiện → thiết kế → thi công → nghiệm thu → đưa vào sử dụng** kho VLNCN (kho mới hoặc kho tạm phục vụ thi công) → reference `03`.
- Xây dựng **Kế hoạch kiểm tra công tác nghiệm thu** (KTCTNT), **Biên bản kiểm tra**, **Thông báo kết quả/chấp thuận nghiệm thu** hoàn thành công trình kho VLNCN → reference `04` + mẫu 01, 02, 08.
- Kho **hiện hữu xây từ lâu** (hồ sơ cũ, quy chuẩn cũ) cần tiếp tục sử dụng: hướng dẫn **kiểm định chất lượng**, xác nhận đề cương kiểm định, xác nhận đáp ứng QCVN → reference `05` + mẫu 03, 04, 05.
- Thẩm định, tham mưu **phê duyệt Phương án nổ mìn (PANM) tại khu vực có công trình cần bảo vệ**, dự thảo QĐ của UBND tỉnh → **chủ trì tại `sd-vlncn-sct-vn` (reference 03 + mẫu 07–11, tiền lệ mới nhất)**; reference `07` + mẫu 06, 07, 09 tại đây dùng khi gắn trực tiếp hồ sơ kho.
- Tra cứu **yêu cầu kỹ thuật** kho VLNCN theo QCVN 01:2019/BCT: phân loại kho, sức chứa tối đa, kết cấu, tường rào, ụ bảo vệ, chống sét, PCCC, khoảng cách an toàn → reference `02`.
- **Thẩm định hồ sơ** doanh nghiệp nộp: checklist đầu mục, lỗi thường gặp, cây quyết định → reference `08`.
- Trả lời câu hỏi doanh nghiệp về thủ tục, điều kiện kho → reference `09`.
- Quản lý vận hành kho: lý lịch kho, xuất nhập, bảo vệ, camera, báo cáo định kỳ/đột xuất → reference `10`.
- Xác định **thẩm quyền, ranh giới trách nhiệm** giữa Sở Công Thương – Công an (PCCC, ANTT) – Sở Xây dựng – UBND tỉnh – UBND xã → mục IV dưới đây + reference `06`.

**KHÔNG thuộc plugin này:** cấp Giấy phép vận chuyển VLNCN (Bộ Công an/Bộ Quốc phòng — plugin `hnh-sct-vn` chỉ xử lý HHNH loại 1 TRỪ VLNCN); xử phạt VPHC (→ plugin `xp-hc-vlncn-sct-vn` theo NĐ 275/2026); huấn luyện KTAT VLNCN chỉ nêu ở mức liên quan hồ sơ (→ `hl-vlncn-sct-vn`). **PANM và Giấy phép sử dụng VLNCN: plugin `sd-vlncn-sct-vn` CHỦ TRÌ** (quy trình thẩm định, mẫu Tờ trình - QĐ đầy đủ, tiền lệ mới nhất) — reference `07` và mẫu 06, 07, 09 tại đây chỉ dùng khi vụ việc gắn trực tiếp hồ sơ kho.

Khi soạn văn bản kết quả: kết hợp skill `vbhc-vn` (thể thức, mẫu), `sct-laocai-org-vn` (người ký, Lưu CN), `vbhc-pdf-reader-vn`/GATE (đọc PDF đến). Khi liên quan PCCC sâu: skill `pccc-sct-vn`.

## II. KHUNG PHÁP LÝ (đã đối chiếu văn bản gốc trong `van-ban-goc/`, cập nhật 7/2026)

Toàn bộ số/ngày đã xác minh. TUYỆT ĐỐI không tự thay số khác. Chi tiết từng văn bản: reference `01`.

**Nhóm 1 — VLNCN chuyên ngành:**
1. **Luật số 42/2024/QH15** ngày 29/6/2024 (hiệu lực 01/01/2025) — Quản lý, sử dụng vũ khí, vật liệu nổ và công cụ hỗ trợ. Điều 38 (điều kiện sử dụng — điểm c: có kho đạt QCVN hoặc hợp đồng thuê kho), Điều 39 (hồ sơ cấp GP sử dụng — điểm đ: văn bản nghiệm thu PCCC đối với kho), Điều 41 (vận chuyển), Điều 42 (trách nhiệm tổ chức).
2. **Luật số 118/2025/QH15** ngày 10/12/2025 — sửa đổi, bổ sung nhiều luật; **khoản 6 Điều 9 sửa điểm đ khoản 1 Điều 39 Luật 42/2024** thành: *"Bản sao văn bản nghiệm thu về phòng cháy và chữa cháy hoặc văn bản chấp thuận kết quả nghiệm thu về phòng cháy và chữa cháy đối với kho cố định chứa vật liệu nổ công nghiệp và điều kiện bảo đảm an toàn theo tiêu chuẩn, quy chuẩn kỹ thuật"* (nguồn: trích dẫn nguyên văn tại footnote CV 2826/SCT-CN ngày 19/5/2026 của Sở).
3. **Nghị định số 181/2024/NĐ-CP** ngày 31/12/2024 — quy định chi tiết Luật 42/2024 về VLNCN, tiền chất thuốc nổ. **Điều 15** (quản lý, bảo quản VLNCN — nghĩa vụ của tổ chức sử dụng kho), Điều 16 (kho tiền chất), Điều 4–9 (trình độ chuyên môn, huấn luyện KTAT), Điều 17 (thu hồi giấy phép).
4. **Thông tư số 23/2024/TT-BCT** ngày 07/11/2024 (hiệu lực 01/01/2025) — Điều 4 (thẩm quyền cấp phép), Điều 5 + Phụ lục (mẫu giấy đề nghị/giấy phép), Điều 14 (đánh giá nguy cơ rủi ro), Điều 15 (phương án, hộ chiếu nổ mìn), Điều 16 (kế hoạch ứng cứu khẩn cấp), Điều 17 (báo cáo định kỳ/đột xuất), Điều 19 (trách nhiệm cấp tỉnh — **khoản 5: chức năng cơ quan chuyên môn về xây dựng và PCCC đối với công trình kho VLNCN**).
5. **Thông tư số 38/2025/TT-BCT** ngày 19/6/2025 (hiệu lực 01/7/2025) — Điều 1 sửa TT 23/2024: **thẩm quyền cấp GP sử dụng VLNCN chuyển về UBND cấp tỉnh** (khoản 4 Điều 4 mới), trừ tổ chức có GP khoáng sản do Bộ NN&MT cấp (→ Cục KTAT&MTCN) và Bộ Quốc phòng. Điều 19 đổi thành "Trách nhiệm của UBND cấp tỉnh".
6. **Nghị định số 146/2025/NĐ-CP** ngày 12/6/2025 — phân quyền, phân cấp lĩnh vực công nghiệp và thương mại; Chương về VLNCN: Điều 22–24 (phân quyền/phân cấp: huấn luyện + cấp GCN KTAT VLNCN của Bộ Công Thương → UBND cấp tỉnh).
7. **QCVN 01:2019/BCT** ban hành kèm **Thông tư số 32/2019/TT-BCT** ngày 21/11/2019 (hiệu lực 01/7/2020) — **văn bản kỹ thuật cốt lõi** về kho: Điều 5 (yêu cầu chung: khoảng cách an toàn, thiết bị điện, chống sét, PCCC, môi trường), Điều 21 (kho VLNCN: phân loại, sức chứa, bảo quản chung), Điều 22 (bảo quản tại nơi nổ mìn), Điều 23 (kho tiền chất); Phụ lục 1 (nhóm tương thích), Phụ lục 7 (tính khoảng cách an toàn), Phụ lục 8 (thủ tục xuất nhập kho), Phụ lục 9 (lý lịch kho), **Phụ lục 10 (quy định xây dựng kho, sắp xếp VLNCN)**, Phụ lục 11 (chống sét), Phụ lục 13 (chế độ bảo vệ), Phụ lục 16 (PCCC). Đến 7/2026 chưa có bản sửa đổi thay thế — các văn bản Sở ban hành 5–6/2026 vẫn viện dẫn trực tiếp QCVN 01:2019/BCT.

**Nhóm 2 — Xây dựng (SCT là cơ quan chuyên môn về xây dựng đối với kho VLNCN):**
8. **Luật Xây dựng 50/2014/QH13**, sửa đổi bởi **Luật 62/2020/QH14** — điểm c khoản 2 Điều 89 (công trình miễn GPXD), khoản 30 Điều 1 Luật 62/2020, **Điều 131 (công trình tạm)**: công trình tạm ảnh hưởng lớn đến an toàn, lợi ích cộng đồng phải được thẩm tra điều kiện an toàn và gửi cơ quan chuyên môn về xây dựng địa phương theo dõi, kiểm tra TRƯỚC khi thi công.
9. **Nghị định 06/2021/NĐ-CP** ngày 26/01/2021 (quản lý chất lượng, thi công, bảo trì) — **Điều 23 (kiểm tra công tác nghiệm thu — điều kiện đưa công trình vào sử dụng, thời hạn thông báo trước nghiệm thu tối thiểu 10 ngày với công trình dưới cấp I)**; khoản 13 Điều 2 (định nghĩa bảo trì); điểm g khoản 2 Điều 5 (kiểm định phục vụ bảo trì); điểm đ khoản 5 Điều 33 (kiểm định khi có yêu cầu của CQNN). Được sửa đổi bởi: **NĐ 35/2023/NĐ-CP** (20/6/2023), **NĐ 175/2024/NĐ-CP** (30/12/2024 — điều kiện năng lực hoạt động xây dựng, chứng chỉ hành nghề), **NĐ 144/2025/NĐ-CP** (12/6/2025 — phân quyền, phân cấp QLNN Bộ Xây dựng), **NĐ 67/2026/NĐ-CP** (04/3/2026).
10. **Thông tư 10/2021/TT-BXD** ngày 25/8/2021 — Điều 5: trình tự, nội dung **kiểm định xây dựng**.
11. **Thông tư 06/2021/TT-BXD** ngày 30/6/2021 — phân cấp công trình (kho VLNCN cố định nổi/nửa ngầm sức chứa ≤10 tấn: công trình công nghiệp **cấp II** — theo cách vận dụng tại CV 2826/SCT-CN).
12. Quy định về quản lý hoạt động xây dựng trên địa bàn tỉnh Lào Cai do UBND tỉnh ban hành (viện dẫn chung; khi cần số cụ thể phải hỏi Bạn).

**Nhóm 3 — PCCC, ANTT:**
13. **Luật PCCC&CNCH số 55/2024/QH15** ngày 29/11/2024 (hiệu lực 01/7/2025) — điểm a khoản 5 Điều 18 (nghiệm thu về PCCC).
14. **Nghị định 105/2025/NĐ-CP** ngày 15/5/2025 — Điều 6 (thẩm định thiết kế PCCC: 5 nội dung điểm a–đ); Phụ lục I điểm 20, Phụ lục II STT 26, Phụ lục III mục 9 điểm c: **kho cố định chứa VLNCN thuộc diện thẩm định thiết kế PCCC, không phụ thuộc quy mô**; Phụ lục VII STT 24 (bảo hiểm cháy nổ bắt buộc). Phân định: cơ quan chuyên môn về xây dựng (SCT với kho VLNCN) thẩm định 5 nội dung a–đ; cơ quan Công an thẩm định/nghiệm thu các nội dung thuộc thẩm quyền Công an. Chi tiết dùng skill `pccc-sct-vn`.
15. Điều kiện **an ninh, trật tự**: kho VLNCN là ngành nghề đầu tư kinh doanh có điều kiện về ANTT — doanh nghiệp phải có **Giấy chứng nhận đủ điều kiện về ANTT do cơ quan Công an cấp** (đầu mục bắt buộc trong hồ sơ cấp GP sử dụng VLNCN).

**Nhóm 4 — Xử phạt (chỉ tham chiếu, xử lý ở plugin `xp-hc-vlncn-sct-vn`):** **NĐ 275/2026/NĐ-CP ngày 08/7/2026** (hiệu lực 25/8/2026, thay NĐ 71/2019 + Điều 1 NĐ 17/2022) — nhóm bảo quản kho: **Điều 57** (kho không đạt yêu cầu xây dựng-ANTT-PCCC-chống sét: 50–70 tr cá nhân + đình chỉ bảo quản 6–12 tháng; bảo quản vượt quy mô thiết kế: 30–50 tr; để mất VLNCN tại kho: 80–100 tr + tước GP 6–12 tháng; tổ chức ×2). Hành vi kết thúc trước 25/8/2026 → Đ53 NĐ 71/2019 (sđ NĐ 17/2022, bản gốc trong `van-ban-goc/`).

**Văn bản địa phương (Lào Cai):**
- **QĐ 05/2025/QĐ-UBND ngày 01/7/2025** — chức năng, nhiệm vụ Sở Công Thương (căn cứ chuẩn trong mọi văn bản).
- **QĐ 1883/QĐ-UBND ngày 06/11/2025** — ủy quyền cấp Giấy phép sử dụng VLNCN trên địa bàn tỉnh (ghi nhận từ hồ sơ trước đây; TRƯỚC KHI VIỆN DẪN phải xác minh lại số/ngày/phạm vi ủy quyền với Bạn — không tự điền).
- NĐ 149/2024/NĐ-CP ngày 15/11/2024 (quy định chi tiết Luật 42/2024 phần Bộ Công an quản lý — tham chiếu khi phân định).

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

- **Cấp GP sử dụng VLNCN:** UBND cấp tỉnh (TT 38/2025), trừ: tổ chức có GP khoáng sản do Bộ NN&MT cấp → Cục KTAT&MTCN; tổ chức thuộc Bộ Quốc phòng. Tại Lào Cai có QĐ ủy quyền (xác minh QĐ 1883 trước khi dẫn).
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

## VI. QUY TRÌNH TỔNG THỂ CHO DOANH NGHIỆP (tóm tắt — chi tiết reference 03)

```
GĐ1 CHUẨN BỊ      → xác định loại kho, vị trí, sức chứa; kiểm tra khoảng cách an toàn (PL7 QCVN);
                    pháp lý dự án gốc (QĐ chủ trương đầu tư/GP khoáng sản); đất đai; ĐTM/GPMT
GĐ2 THIẾT KẾ      → thuê tư vấn đủ năng lực (NĐ 175/2024); thiết kế theo QCVN 01:2019/BCT;
                    thẩm tra thiết kế; thẩm định thiết kế PCCC; xác định tư cách công trình
                    (công trình tạm Đ131 hay công trình thuộc diện thẩm định tại CQCM)
GĐ3 THI CÔNG      → thông báo khởi công; nhà thầu + TVGS đủ điều kiện; nhật ký, quản lý chất lượng;
                    thi công chống sét - tiếp địa; gửi thiết kế cho SCT theo dõi (công trình tạm)
GĐ4 HOÀN THÀNH    → đo điện trở tiếp địa; nghiệm thu nội bộ; hồ sơ hoàn công; báo cáo hoàn thành
                    gửi SCT TRƯỚC ≥10 ngày; nghiệm thu PCCC (Công an); GCN ANTT
GĐ5 NHÀ NƯỚC KIỂM TRA → SCT ban hành KH kiểm tra → kiểm tra hiện trường + hồ sơ → Biên bản
                    → TB chấp thuận kết quả nghiệm thu (CHỈ SAU ĐÓ mới được đưa vào sử dụng)
GĐ6 CẤP PHÉP      → hồ sơ GP sử dụng VLNCN (Điều 39 Luật 42/2024 + Luật 118/2025); PANM
                    (phê duyệt nếu khu vực có công trình cần bảo vệ) → vận hành, báo cáo định kỳ
```

## VII. ANTI-ERROR RIÊNG CHO LĨNH VỰC NÀY (đúc kết từ bản phản biện hồ sơ Ngòi Nhù 1A — reference 08)

1. **Nhất quán tư cách công trình:** chọn MỘT hướng — "công trình tạm" (Điều 131 Luật XD, miễn GPXD, chủ đầu tư tự thẩm định + gửi SCT theo dõi trước thi công) HOẶC "công trình cấp II thuộc diện thẩm định tại CQCM về xây dựng" — và giữ nhất quán trong toàn bộ hồ sơ, biên bản, thông báo. Không viết "được SCT thẩm định thiết kế" nếu Sở không thẩm định.
2. **Trình tự nghiệm thu:** công trình thuộc diện kiểm tra công tác nghiệm thu CHỈ được đưa vào sử dụng sau khi có văn bản chấp thuận (Điều 23 NĐ 06/2021). Biên bản nghiệm thu của chủ đầu tư không được ghi "bàn giao đưa vào sử dụng từ ngày nghiệm thu".
3. **Đủ 2 đầu mục Công an:** văn bản chấp thuận kết quả nghiệm thu PCCC + GCN đủ điều kiện ANTT (biên bản kiểm tra định kỳ PC03 KHÔNG thay thế văn bản nghiệm thu PCCC).
4. **Không copy sót nội dung vụ khác:** rà tên chủ đầu tư, ngày biên bản, tên xã tại mọi phụ lục.
5. **Năng lực cá nhân phải có minh chứng:** chỉ huy trưởng, TVGS phải có chứng chỉ hành nghề + quyết định giao nhiệm vụ (NĐ 175/2024); giấy ủy quyền ký văn bản phải còn hiệu lực, rõ phạm vi.
6. **Không tự điền số/ngày văn bản chưa ban hành**; số liệu sức chứa, khoảng cách phải khớp thiết kế được duyệt; GATE khi đọc PDF đến.
7. Sau sáp nhập 01/7/2025: địa danh dùng **xã + tỉnh Lào Cai** (không còn cấp huyện); ghi chú vị trí cũ nếu cần như tiền lệ TB Móng Sến 1.

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
mau-van-ban/                       9 mẫu sẵn dùng (điền chỗ trống là ban hành được)
vi-du-thuc-te/                     Văn bản Sở đã ban hành 4 vụ việc thật + bản phản biện hồ sơ
van-ban-goc/                       TT 32/2019 (QCVN 01:2019/BCT), Luật 42/2024, NĐ 181/2024,
                                   TT 23/2024, TT 38/2025, NĐ 146/2025, NĐ 71/2019, NĐ 17/2022, NĐ 149/2024
```

## IX. QUY TẮC LÀM VIỆC

1. Trả lời/soạn thảo bằng tiếng Việt, văn phong hành chính.
2. Trước khi viện dẫn văn bản đến (PDF): chạy GATE trích số/ngày/người ký từ file.
3. Không dùng dữ liệu hiện trạng (tên doanh nghiệp đang làm hồ sơ, tiến độ) từ skill làm dữ liệu thời sự — hỏi Bạn số liệu mới nhất.
4. Mọi mẫu văn bản khi xuất docx: theo thể thức NĐ 30/2020 qua skill `vbhc-vn`; render kiểm tra trước khi giao.
5. Khi số văn bản địa phương chưa chắc chắn (QĐ ủy quyền, QĐ quản lý xây dựng của tỉnh): để trống + hỏi Bạn, không đoán.
