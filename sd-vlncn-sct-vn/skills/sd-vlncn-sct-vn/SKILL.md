---
name: sd-vlncn-sct-vn
description: "Chuyên gia QLNN về GIẤY PHÉP SỬ DỤNG vật liệu nổ công nghiệp (VLNCN) và PHƯƠNG ÁN NỔ MÌN (PANM) của Sở Công Thương Lào Cai. 5 nghiệp vụ: (1) thẩm định, tham mưu cấp/cấp lại/điều chỉnh/thu hồi Giấy phép sử dụng VLNCN (Chủ tịch UBND tỉnh ký GP-UBND, SCT thẩm định trình); (2) thẩm định PANM tại khu vực có công trình cần bảo vệ, lập hồ sơ trình UBND tỉnh: Phiếu trình, Tờ trình, dự thảo QĐ, biên bản kiểm tra hiện trường, lấy ý kiến Sở Xây dựng; (3) hướng dẫn doanh nghiệp: điều kiện, hồ sơ, chỉ huy nổ mìn, huấn luyện KTAT, hộ chiếu nổ mìn; (4) kiểm tra, xử phạt VPHC (NĐ 71/2019 + 17/2022); (5) báo cáo định kỳ/đột xuất. Kèm mẫu sẵn dùng + ví dụ thực tế + văn bản gốc. Từ khóa: giấy phép sử dụng VLNCN, GP-UBND, phương án nổ mìn, PANM, hộ chiếu nổ mìn, nổ mìn khu dân cư, khoảng cách an toàn, đá văng, chấn động, QCVN 01:2019/BCT, Luật 42/2024, NĐ 181/2024, TT 23/2024, TT 38/2025, NĐ 146/2025, dịch vụ nổ mìn, tiêu hủy VLNCN, mỏ đá, thủy điện, gói thầu."
---

# sd-vlncn-sct-vn — Giấy phép sử dụng VLNCN & Phương án nổ mìn (Sở Công Thương Lào Cai)

## I. KHI NÀO DÙNG SKILL NÀY

Kích hoạt khi xử lý bất kỳ việc nào sau:

- **Cấp / cấp lại / cấp điều chỉnh / thu hồi Giấy phép sử dụng VLNCN**: thẩm định hồ sơ doanh nghiệp, checklist, Phiếu trình, Tờ trình UBND tỉnh, dự thảo Giấy phép (GP-UBND), dự thảo QĐ điều chỉnh → reference `02` + mẫu 01–06.
- **Phương án nổ mìn (PANM)**: xác định có phải trình UBND tỉnh phê duyệt không (cây quyết định); thẩm định nội dung theo Phụ lục VII TT 23/2024 và QCVN 01:2019/BCT; kiểm tra hiện trường; lấy ý kiến Sở Xây dựng; Tờ trình + dự thảo QĐ phê duyệt PANM (kèm/không kèm chấp thuận sử dụng VLNCN tại khu vực có công trình cần bảo vệ) → reference `03` + mẫu 07–11.
- **Hướng dẫn doanh nghiệp** từng bước: điều kiện Điều 38 Luật 42/2024, hồ sơ Điều 39, trình độ chỉ huy nổ mìn/thợ mìn, huấn luyện KTAT, hộ chiếu nổ mìn, đánh giá rủi ro, kế hoạch ứng cứu khẩn cấp, thông báo sử dụng VLNCN, dịch vụ nổ mìn → reference `04`.
- **CV hướng dẫn hoàn thiện hồ sơ, CV đôn đốc, VB trả lời/giải quyết đề nghị, VB tuyên truyền** → mẫu 12–14 + ví dụ thực tế.
- **Kiểm tra, giám sát, xử phạt VPHC** trong sử dụng VLNCN: kế hoạch kiểm tra, nội dung kiểm tra, biên bản, tra cứu hành vi – mức phạt NĐ 71/2019 (sđ NĐ 17/2022), hình thức bổ sung tước GP/đình chỉ, thẩm quyền xử phạt → reference `05`.
- **Báo cáo** định kỳ/đột xuất về VLNCN: của doanh nghiệp gửi Sở; của UBND tỉnh (SCT dự thảo) gửi Bộ Công Thương/Cục KTAT&MTCN → reference `06` + mẫu 15.
- Tra cứu **ví dụ thực tế đã ban hành** (giấy phép, QĐ PANM, tờ trình, báo cáo… của Lào Cai 2025–2026) → reference `07` + thư mục `vi-du-thuc-te/`.

**Ranh giới với plugin khác:** kho VLNCN (thiết kế, nghiệm thu, kiểm định kho) → plugin `kho-vlncn-sct-vn`; vận chuyển VLNCN → Công an/Quốc phòng cấp phép, KHÔNG thuộc SCT (plugin `hnh-sct-vn` chỉ xử lý HHNH trừ VLNCN); PCCC chuyên sâu → `pccc-sct-vn`. Khi soạn văn bản: kết hợp `vbhc-vn` (thể thức), `sct-laocai-org-vn` (người ký, Lưu CN), GATE/`vbhc-pdf-reader-vn` khi đọc PDF đến.

## II. KHUNG PHÁP LÝ (đã đối chiếu văn bản gốc, cập nhật 7/2026 — chi tiết: reference `01`)

TUYỆT ĐỐI không tự thay số/ngày khác. Toàn bộ đã xác minh từ văn bản gốc trong hồ sơ Sở.

1. **Luật số 42/2024/QH15** ngày 29/6/2024 (hiệu lực 01/01/2025) — Quản lý, sử dụng vũ khí, vật liệu nổ và công cụ hỗ trợ. Cốt lõi: **Điều 38** (điều kiện + quy định sử dụng VLNCN; điểm d khoản 2: PANM tại khu dân cư/công trình cần bảo vệ phải được cơ quan cấp GP phê duyệt + đồng ý bằng văn bản của UBND cấp tỉnh); **Điều 39** (hồ sơ, thủ tục cấp/cấp lại/điều chỉnh GP sử dụng; thời hạn GP); Điều 40 (dịch vụ nổ mìn); Điều 42 (trách nhiệm tổ chức); khoản 5 Điều 9 + Điều 10 (các trường hợp thu hồi).
2. **Luật số 118/2025/QH15** ngày 10/12/2025 — khoản 6 Điều 9 sửa điểm đ khoản 1 Điều 39 Luật 42/2024: "Bản sao văn bản nghiệm thu về PCCC **hoặc văn bản chấp thuận kết quả nghiệm thu về PCCC đối với kho cố định** chứa VLNCN và điều kiện bảo đảm an toàn theo tiêu chuẩn, quy chuẩn kỹ thuật".
3. **Nghị định số 181/2024/NĐ-CP** ngày 31/12/2024 — quy định chi tiết về VLNCN, tiền chất thuốc nổ: **Điều 4** (trình độ chuyên môn người quản lý, chỉ huy nổ mìn, thợ mìn), Điều 5–9 (huấn luyện, cấp GCN KTAT), Điều 15 (quản lý, bảo quản), **Điều 17** (thủ tục thu hồi giấy phép — Mẫu số 05 Phụ lục).
4. **Thông tư số 23/2024/TT-BCT** ngày 07/11/2024 (hiệu lực 01/01/2025) — Điều 3 + Phụ lục I (Danh mục VLNCN được phép sử dụng), **Điều 4** (thẩm quyền), Điều 5 + **Phụ lục III** (mẫu giấy đề nghị, mẫu giấy phép), Điều 14 (đánh giá nguy cơ rủi ro — PL VI), **Điều 15 + Phụ lục VII** (nội dung PANM), **Phụ lục VIII** (hộ chiếu nổ mìn), Điều 16 (KH ứng cứu khẩn cấp — PL IX), **Điều 17** (báo cáo định kỳ/đột xuất — PL X), Điều 19 (trách nhiệm cấp tỉnh).
5. **Thông tư số 38/2025/TT-BCT** ngày 19/6/2025 (hiệu lực 01/7/2025) — Điều 1 sửa TT 23/2024: **thẩm quyền cấp/cấp lại/cấp điều chỉnh GP sử dụng VLNCN chuyển về UBND CẤP TỈNH** (khoản 4 Điều 4 mới); Cục KTAT&MTCN chỉ còn cấp cho tổ chức nghiên cứu/thử nghiệm VLNCN hoặc có GP khoáng sản do **Bộ Nông nghiệp và Môi trường** cấp (trừ Bộ Quốc phòng); Điều 19 đổi thành "Trách nhiệm của UBND cấp tỉnh"; báo cáo đột xuất gửi **Công an xã** + UBND cấp tỉnh.
6. **Nghị định số 146/2025/NĐ-CP** ngày 12/6/2025 — phân quyền, phân cấp: Điều 22–23 (phân quyền TTg, Bộ trưởng BCT — văn bản đề nghị cấp GP dịch vụ nổ mìn toàn quốc/thềm lục địa do UBND cấp tỉnh ban hành); **khoản 1 Điều 24**: huấn luyện, kiểm tra, cấp/cấp lại GCN huấn luyện KTAT VLNCN (k1 Đ6, Đ9, điểm b k1 Đ18 NĐ 181) từ Bộ Công Thương → **UBND cấp tỉnh**.
7. **Nghị định số 139/2025/NĐ-CP** ngày 12/6/2025 — phân định thẩm quyền chính quyền 02 cấp lĩnh vực QLNN của Bộ Công Thương (căn cứ trong QĐ ủy quyền của tỉnh).
8. **QCVN 01:2019/BCT** (kèm TT 32/2019/TT-BCT ngày 21/11/2019) — quy chuẩn an toàn cốt lõi: **Phụ lục 7** (công thức khoảng cách an toàn: chấn động Rc, sóng không khí rs, đá văng Rđv — Bảng 7.8; nổ lộ thiên với người ≥300 m/200 m, thiết bị-công trình ≥200 m/150 m tùy quy mô); Điều 22 (bảo quản tại nơi nổ mìn); quy định giờ nổ, tín hiệu, canh gác.
9. **Xử phạt: Nghị định số 71/2019/NĐ-CP** ngày 30/8/2019 (hiệu lực 15/10/2019), sửa đổi bởi **Nghị định số 17/2022/NĐ-CP** ngày 31/01/2022 — Điều 49–57 (VLNCN); **Điều 56** (vi phạm sử dụng VLNCN, dịch vụ nổ mìn — mức phạt 3–100 triệu đ/cá nhân, tổ chức ×2, tước GP 6–24 tháng); Điều 58–60 (thẩm quyền). Lưu ý: NĐ 17/2022 KHÔNG sửa Điều 56; Bộ Công Thương đang xây dựng Nghị định thay thế NĐ 71/2019 (theo QĐ 1688/QĐ-TTg ngày 06/8/2025) — **trước khi viện dẫn phải kiểm tra Nghị định mới đã ban hành chưa**.
10. **Văn bản địa phương Lào Cai:** QĐ 05/2025/QĐ-UBND ngày 01/7/2025 (chức năng SCT); QĐ ủy quyền của UBND tỉnh cho GĐ SCT thực hiện **huấn luyện, kiểm tra, cấp/cấp lại GCN huấn luyện KTAT VLNCN** (TTHC mã 2.000229, 2.000210), thời hạn đến 28/02/2027 — số/ngày QĐ phải xác minh với Bạn trước khi viện dẫn (dự thảo trình tại TTr 2205/TTr-SCT ngày 28/10/2025; kho-vlncn ghi nhận QĐ 1883/QĐ-UBND ngày 06/11/2025).

## III. THẨM QUYỀN — PHÂN ĐỊNH NHANH (từ 01/7/2025)

| Việc | Cơ quan | Ghi chú |
|---|---|---|
| Cấp/cấp lại/điều chỉnh **GP sử dụng VLNCN** trên địa bàn | **Chủ tịch UBND tỉnh** ký (KT. PCT Nguyễn Thành Sinh), ký hiệu `/GP-UBND`, SCT thẩm định + Tờ trình | Trừ 2 ngoại lệ dưới |
| GP sử dụng cho tổ chức nghiên cứu/thử nghiệm VLNCN; tổ chức có GP khoáng sản do **Bộ NN&MT** cấp | Cục Kỹ thuật an toàn và Môi trường công nghiệp (Bộ Công Thương) | điểm c k2 Đ4 TT 23 (sđ TT 38/2025) |
| Tổ chức thuộc **Bộ Quốc phòng** | Bộ Quốc phòng (Tổng cục CNQP) | |
| **Thu hồi** GP sử dụng VLNCN | Cơ quan đã cấp (= Chủ tịch UBND tỉnh; SCT tham mưu) | Đ17 NĐ 181/2024 |
| **Phê duyệt PANM** tại khu dân cư/công trình cần bảo vệ + chấp thuận sử dụng | **Chủ tịch UBND tỉnh** ký QĐ (SCT thẩm định, Tờ trình) | điểm d k2 Đ38 Luật 42/2024 |
| PANM thông thường (ngoài khu vực trên) | **Lãnh đạo doanh nghiệp tự ký duyệt** — KHÔNG trình UBND tỉnh | điểm d k1 Đ39 Luật 42/2024 |
| GP **dịch vụ nổ mìn** tại địa phương (1 tỉnh) | Cục KTAT&MTCN cấp; **UBND cấp tỉnh ban hành văn bản đề nghị** | k1 Đ23 NĐ 146/2025 |
| Huấn luyện + GCN huấn luyện KTAT VLNCN | UBND cấp tỉnh, đã **ủy quyền GĐ Sở Công Thương** | mã TTHC 2.000229/2.000210 |
| GP **vận chuyển** VLNCN | Cơ quan Công an (Đ41 Luật 42/2024) | KHÔNG thuộc SCT |
| Kiểm tra, xử phạt sử dụng VLNCN trên địa bàn | SCT chủ trì (Đ19 TT 23); Chủ tịch UBND các cấp, Thanh tra, Công an theo NĐ 71/2019 | |

## IV. NGƯỜI KÝ, NGƯỜI SOẠN (khớp `sct-laocai-org-vn` + thực tiễn đã ban hành)

- Lĩnh vực VLNCN thuộc **PGĐ Hoàng Văn Thuân** phụ trách → công văn, báo cáo UBND tỉnh của Sở thường ký **KT. GIÁM ĐỐC / PHÓ GIÁM ĐỐC Hoàng Văn Thuân**. Tờ trình UBND tỉnh: cân nhắc GĐ Hoàng Chí Hiền với vụ việc lớn.
- **Lưu: VT, CN(Linh)** — Vũ Việt Linh là chuyên viên tham mưu GP sử dụng VLNCN + PANM (đã xác minh từ Phiếu trình thực tế). Một số văn bản đôn đốc chung dùng CN(M.Cường) — Đỗ Mạnh Cương, Phó TP QLCN; mặc định dùng CN(Linh), hỏi Bạn nếu khác.
- Văn bản UBND tỉnh (GP, QĐ PANM, QĐ điều chỉnh): **CHỦ TỊCH ỦY BAN NHÂN DÂN TỈNH LÀO CAI** là chủ thể ban hành, ký **KT. CHỦ TỊCH / PHÓ CHỦ TỊCH Nguyễn Thành Sinh**; nơi nhận có "CVP, PCVP UBND tỉnh (Bích)", "Lưu: VT, TTPVHCC, KT.".
- Ký hiệu: giấy phép và QĐ điều chỉnh GP dùng `/GP-UBND`; QĐ phê duyệt PANM `/QĐ-UBND`; tờ trình `/TTr-SCT`; công văn `/SCT-CN`.

## V. HAI QUY TRÌNH LÕI (tóm tắt — chi tiết reference 02, 03)

**A. Cấp GP sử dụng VLNCN (5 ngày làm việc kể từ khi đủ hồ sơ — k6 Đ39):**
```
DN nộp hồ sơ (TTPVHCC tỉnh / Cổng DVC / bưu chính)
→ SCT (Phòng QLCN – CN Linh) kiểm tra tính đầy đủ, hợp lệ
→ Thẩm định hồ sơ theo checklist Đ38+Đ39 (ref 02) + kiểm tra điều kiện thực tế khi cần
   (chưa đạt → CV /SCT-CN hướng dẫn hoàn thiện, nêu ĐÍCH DANH từng tồn tại — mẫu 12)
→ Phiếu trình lãnh đạo Sở (mẫu 06) → Tờ trình /TTr-SCT + dự thảo Giấy phép (mẫu 03, 01)
→ Chủ tịch UBND tỉnh ký GP-UBND (KT. PCT Nguyễn Thành Sinh)
→ Trả kết quả; cập nhật CSDL VLNCN; theo dõi thông báo sử dụng, báo cáo định kỳ
```
Thời hạn GP (k7 Đ39): theo GP thăm dò ≤ **04 năm**; theo GP khai thác ≤ **05 năm**; theo thời hạn công trình ≤ **02 năm**. Thực tiễn Lào Cai: mỏ khai thác ghi "có giá trị 05 năm kể từ ngày ký"; công trình ghi theo tiến độ.

**B. Phê duyệt PANM tại khu vực có công trình cần bảo vệ:**
```
Hồ sơ DN đến (thường qua Phiếu chuyển VPUBND) → GATE đọc PDF
→ Bước 1. XÁC ĐỊNH có thuộc diện phê duyệt không (cây quyết định ref 03):
   trong bán kính ảnh hưởng có khu dân cư/cơ sở KCB/di tích/công trình QP-AN/công trình quan trọng?
   – KHÔNG (khoảng cách ≥ QCVN, có che chắn tự nhiên) → VB báo cáo UBND tỉnh khẳng định
     không thuộc diện, DN tự phê duyệt theo điểm d k1 Đ39 (tiền lệ Yên Thành — mẫu 14)
   – CÓ → tiếp bước 2
→ Bước 2. Rà hồ sơ: PANM đủ nội dung PL VII TT 23, chỉ huy nổ mìn ký + lãnh đạo DN phê duyệt nội bộ,
   pháp lý dự án gốc, hợp đồng thi công (chưa đạt → CV hoàn thiện — tiền lệ Vạn Thắng)
→ Bước 3. Kiểm tra hiện trường (SCT + UBND xã + DN) → Biên bản (mẫu 09): đo khoảng cách thực tế,
   đếm hộ dân/công trình trong bán kính, địa hình che chắn, hướng nổ
→ Bước 4. Thẩm định kỹ thuật theo QCVN 01:2019/BCT: kiểm tra Rc, rs, Rđv (PL 7), quy mô Qmax,
   biện pháp che chắn (lưới B40 + bao cát), canh gác, giờ nổ; liên quan quốc lộ/tỉnh lộ
   → CV lấy ý kiến Sở Xây dựng về phương án tổ chức giao thông (mẫu 08)
→ Bước 5. Phiếu trình → Tờ trình /TTr-SCT (mẫu 07) + dự thảo QĐ (mẫu 10/11)
→ Chủ tịch UBND tỉnh ký QĐ phê duyệt PANM (gộp nội dung "đồng ý bằng văn bản của UBND cấp tỉnh")
→ Giao SCT + PC06 Công an tỉnh + UBND xã giám sát thực hiện
```

## VI. ANTI-ERROR RIÊNG LĨNH VỰC NÀY (đúc kết từ hồ sơ thật 2025–2026)

1. **Đúng thẩm quyền, đúng thể thức chủ thể:** Giấy phép/QĐ PANM là văn bản của **Chủ tịch UBND tỉnh** (không phải "TM. ỦY BAN NHÂN DÂN" — dùng "KT. CHỦ TỊCH / PHÓ CHỦ TỊCH"); tiêu đề căn cứ mở đầu là "CHỦ TỊCH ỦY BAN NHÂN DÂN TỈNH LÀO CAI". Riêng QĐ ủy quyền là của UBND tỉnh (TM. ỦY BAN NHÂN DÂN).
2. **Không nhầm 2 chế độ PANM:** chỉ trình UBND tỉnh khi thuộc điểm d k2 Đ38; ngoài diện đó nếu DN vẫn trình → Sở làm VB báo cáo UBND tỉnh khẳng định không thuộc diện + hướng dẫn DN tự phê duyệt (KHÔNG im lặng trả hồ sơ).
3. **PANM phải được phê duyệt nội bộ trước:** người lập (chỉ huy nổ mìn) ký ghi rõ họ tên + lãnh đạo DN ký duyệt — thiếu là trả hồ sơ (tiền lệ Vạn Thắng).
4. **Số liệu 3 khớp:** tổng khối lượng VLNCN trong Giấy phép = trong PANM = trong thiết kế/Phụ lục hợp đồng; Qmax một đợt nổ trong GP phải khớp tính toán an toàn của PANM. Khối lượng đá còn lại phải trừ phần đã thi công.
5. **Khoảng cách an toàn:** luôn kiểm tra đủ 3 giá trị Rc (chấn động), rs (sóng không khí), Rđv (đá văng — tra Bảng 7.8 PL 7 QCVN); giá trị lớn nhất phải ≤ khoảng cách thực tế đến công trình gần nhất; nêu rõ trang/mục QCVN đã tra.
6. **Điều kiện tiên quyết trước khi cấp GP:** thiết kế mỏ/công trình được lập-thẩm định-phê duyệt đúng trình tự pháp luật xây dựng tại thời điểm lập (vướng → làm rõ dứt điểm với Sở Xây dựng bằng câu hỏi ĐÓNG, yêu cầu khẳng định rõ, có thời hạn — tiền lệ Đồng Khê); kho đạt 4 trụ (xem `kho-vlncn-sct-vn`) hoặc hợp đồng/ý định giao kết thuê kho, thuê vận chuyển.
7. **GCN ANTT + nghiệm thu PCCC kho** là đầu mục cứng của hồ sơ; biên bản kiểm tra định kỳ của Công an KHÔNG thay thế văn bản nghiệm thu PCCC.
8. **Không tự điền số/ngày** văn bản chưa ban hành; số GP, số TTr để trống "Số:      /GP-UBND". GATE bắt buộc khi đọc PDF đến. Sau 01/7/2025 địa danh ghi **xã + tỉnh Lào Cai** (có thể mở ngoặc "(nay là xã…, tỉnh Lào Cai)" với địa danh cũ trong hồ sơ gốc).
9. **Nghị định thay thế NĐ 71/2019 đang dự thảo** — trước khi tham mưu xử phạt, kiểm tra văn bản mới nhất; nếu chưa có thì viện dẫn "NĐ 71/2019/NĐ-CP được sửa đổi, bổ sung bởi NĐ 17/2022/NĐ-CP".
10. **Render-and-verify** mọi file .docx đầu ra trước khi bàn giao (quy tắc chung của Bạn).

## VII. CẤU TRÚC PLUGIN

```
sd-vlncn-sct-vn/
├── SKILL.md                          ← file này
├── CHANGELOG.md
├── references/
│   ├── 01-phap-ly.md                 ← khung pháp lý chi tiết, trích điều khoản gốc
│   ├── 02-quy-trinh-cap-gp.md        ← cấp/cấp lại/điều chỉnh/thu hồi GP: điều kiện, hồ sơ,
│   │                                    trình tự, checklist thẩm định, lỗi thường gặp
│   ├── 03-panm.md                    ← PANM: cây quyết định, nội dung PL VII, công thức QCVN,
│   │                                    quy trình thẩm định-trình phê duyệt, hộ chiếu nổ mìn
│   ├── 04-huong-dan-dn.md            ← hướng dẫn doanh nghiệp A→Z + FAQ
│   ├── 05-kiem-tra-xu-phat.md        ← kiểm tra, giám sát; bảng hành vi-mức phạt NĐ 71/2019;
│   │                                    thẩm quyền; quy trình xử phạt của Sở
│   ├── 06-bao-cao.md                 ← chế độ báo cáo định kỳ/đột xuất các cấp
│   └── 07-vi-du-thuc-te.md           ← index ví dụ + bài học kinh nghiệm từng vụ việc
├── mau-van-ban/                      ← 19 mẫu sẵn dùng (điền 【...】), soạn docx bằng vbhc-vn
│   ├── 01-giay-phep-su-dung-vlncn-mo-khoang-san.md
│   ├── 02-giay-phep-su-dung-vlncn-cong-trinh.md
│   ├── 03-to-trinh-cap-gp.md
│   ├── 04-qd-dieu-chinh-gp.md
│   ├── 05-qd-thu-hoi-gp.md
│   ├── 06-phieu-trinh-tham-dinh.md
│   ├── 07-to-trinh-phe-duyet-panm.md
│   ├── 08-cv-lay-y-kien-so-xay-dung.md
│   ├── 09-bien-ban-kiem-tra-hien-truong.md
│   ├── 10-qd-phe-duyet-panm.md
│   ├── 11-qd-phe-duyet-panm-kem-chap-thuan.md
│   ├── 12-cv-huong-dan-hoan-thien-ho-so.md
│   ├── 13-cv-don-doc-thuc-hien-quy-dinh.md
│   ├── 14-vb-bao-cao-ubnd-khong-thuoc-dien-phe-duyet.md
│   ├── 15-bao-cao-dinh-ky-nam-vlncn.md
│   ├── 16-qd-kiem-tra-chuyen-nganh.md
│   ├── 17-ke-hoach-kiem-tra-cua-doan.md
│   ├── 18-bao-cao-ket-qua-kiem-tra.md
│   └── 19-thong-bao-ket-qua-sau-kiem-tra.md
├── vi-du-thuc-te/                    ← văn bản thật đã ban hành (docx + PDF ký thật: Phiếu trình,
│                                       biên bản hiện trường, PANM đầy đủ của DN, CV SXD/SCT)
└── van-ban-goc/                      ← văn bản pháp luật ĐẦY ĐỦ (Luật 42, NĐ 181, TT 23, TT 38,
                                        NĐ 146, NĐ 71, NĐ 17) — xem van-ban-goc/INDEX.md
```

**Nguyên tắc dùng mẫu:** ưu tiên lấy văn bản thật trong `vi-du-thuc-te/` cùng loại làm khung (Chế độ B của vbhc-vn — sửa file gốc), mẫu trong `mau-van-ban/` dùng khi cần khởi tạo nhanh hoặc đối chiếu đầu mục. Dữ liệu hiện trạng (số đơn vị, số kho, sản lượng…) KHÔNG lấy từ skill — hỏi Bạn số liệu mới nhất.
