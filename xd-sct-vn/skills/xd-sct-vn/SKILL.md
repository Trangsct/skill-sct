---
name: xd-sct-vn
description: "XÂY DỰNG - QLNN cấp bộ + tỉnh + xã, Sở Công Thương Lào Cai, chuyên sâu công trình ngành Công Thương. Kích hoạt: cơ quan chuyên môn về xây dựng, thẩm định BCNCKT/BCKTKT/thiết kế, giấy phép xây dựng (cấp hoặc miễn), KTCTNT, điều kiện khởi công, sự cố công trình, công trình tạm, cấp công trình. Dùng khi: xác định SCT có phải cơ quan chuyên môn về xây dựng không; kiểm tra công tác nghiệm thu; bảo trì, đánh giá an toàn; phân định thẩm quyền tỉnh - xã - BQL KKT/KCN; loại, cấp công trình. Khung pháp lý hiệu lực 01/7/2026 (chi tiết mục II). Liên kết plugin kho-vlncn-sct-vn, sd-vlncn-sct-vn, hl-vlncn-sct-vn, kcn-ccn-vn, pccc-sct-vn, vbhc-vn, sct-laocai-org-vn. Từ khóa thêm: Luật Xây dựng 135/2025, NĐ 207/2026, NĐ 217/2026, NĐ 140/2025, NĐ 144/2025, QĐ 11/2026, công trình công nghiệp."
---

# xd-sct-vn — Quản lý nhà nước về xây dựng, chuyên sâu ngành Công Thương (Sở Công Thương Lào Cai)

## I. KHI NÀO DÙNG SKILL NÀY

Plugin đóng ba vai đồng thời — **chuyên gia cấp bộ** (nắm khung Luật/NĐ/TT của Bộ Xây dựng), **cấp tỉnh** (vận dụng phân quyền cho UBND tỉnh, Sở, BQL), **cấp xã** (mô hình chính quyền 2 cấp sau 01/7/2025) — nhưng **luôn ưu tiên chuyên sâu công trình ngành Công Thương** (kho VLNCN, nhà máy/kho hóa chất, công trình khai thác - chế biến khoáng sản, nhà máy điện - lưới điện, hạ tầng KCN/CCN, cửa hàng xăng dầu/LPG, công trình công nghiệp chế biến chế tạo).

Kích hoạt khi xử lý bất kỳ việc nào sau:

- Xác định **Sở Công Thương có phải "cơ quan chuyên môn về xây dựng"** đối với một công trình cụ thể không, và với nghiệp vụ nào (thẩm định thiết kế / kiểm tra nghiệm thu / sự cố) → mục III + reference `02`.
- **Thẩm định** Báo cáo nghiên cứu khả thi (BCNCKT), Báo cáo kinh tế - kỹ thuật (BCKTKT), thiết kế xây dựng triển khai sau thiết kế cơ sở của **dự án đầu tư xây dựng công trình công nghiệp** → reference `03`.
- **Kiểm tra công tác nghiệm thu (KTCTNT)** công trình chuyên ngành công nghiệp: kế hoạch, biên bản, thông báo chấp thuận → reference `04` + mẫu 01, 02, 03. ⭐ **Bước bắt buộc trước khi ra kế hoạch kiểm tra: đọc reference `04` mục I.0 — nhóm LOẠI TRỪ khỏi KTCTNT (công trình bí mật nhà nước, khẩn cấp - cấp bách, đầu tư công đặc biệt và CÔNG TRÌNH TẠM) theo khoản 1 Điều 25 NĐ 207/2026, kèm chuyển tiếp khoản 3 Điều 53.**
- **Điều kiện khởi công**, thông báo khởi công, quản lý chất lượng thi công theo NĐ 207/2026 → reference `03` mục D.
- **Giấy phép xây dựng**: trường hợp phải xin / được miễn; thẩm quyền cấp (tỉnh, xã, BQL KKT/KCN); công trình công nghiệp → reference `05`.
- **Công trình tạm** (kho VLNCN tạm, lán trại thi công) theo Điều 72 Luật 135/2025 → reference `06`.
- **Sự cố công trình**, đánh giá an toàn, bảo trì, dừng khai thác sử dụng → reference `07`.
- **Phân định thẩm quyền 3 cấp** (bộ ↔ tỉnh ↔ xã) sau NĐ 140/2025, NĐ 144/2025, QĐ 11/2026/QĐ-UBND Lào Cai; loại và cấp công trình → reference `02` + `08`.
- Trả lời doanh nghiệp, tham mưu công văn, tờ trình, báo cáo về xây dựng công trình công nghiệp → reference `09` + mẫu.

**KHÔNG thuộc trọng tâm plugin này (chỉ nêu ranh giới, dẫn sang nơi khác):**
- Kho VLNCN chi tiết (quy trình, QCVN 01:2019/BCT, nghiệm thu kho) → plugin **`kho-vlncn-sct-vn`** (plugin này chỉ nêu phần khung xây dựng chung áp cho kho).
- Giấy phép sử dụng VLNCN, PANM → **`sd-vlncn-sct-vn`**; huấn luyện KTAT → **`hl-vlncn-sct-vn`**.
- Hạ tầng KCN/CCN (thành lập, chủ đầu tư, lấp đầy) → **`kcn-ccn-vn`**; PCCC công trình → **`pccc-sct-vn`**; quy hoạch điện/khoáng sản/KCN/CCN → **`quy-hoach-ct-vn`**.
- Công trình điện lực (lưới điện, nhà máy điện) → thẩm định thuộc **Phòng QLNL** (không phải QLCN) — xem `sct-laocai-org-vn`.
- Thể thức văn bản, soạn thảo docx → **`vbhc-vn`**; đọc PDF đến → GATE/`vbhc-pdf-reader-vn`.

## II. KHUNG PHÁP LÝ (đã đối chiếu văn bản gốc trong `van-ban-goc/`, GATE 7/2026)

Toàn bộ số/ngày dưới đây đã trích xuất từ chính văn bản gốc. TUYỆT ĐỐI không tự thay số khác. Chi tiết từng văn bản: reference `01`.

**Trục xương sống — hiệu lực đồng loạt 01/7/2026:**
1. **Luật Xây dựng số 135/2025/QH15** — Quốc hội khóa XV, Kỳ họp thứ 10 thông qua **ngày 10/12/2025**; **hiệu lực 01/7/2026** (một số nội dung: khoản 2-3 Điều 43, Điều 71, khoản 3-4-5 Điều 95 hiệu lực từ 01/01/2026 — Điều 94). Thay Luật Xây dựng 50/2014 (và các luật sửa đổi). 95 điều, 8 chương. Điều then chốt cho SCT: Đ6 (loại, cấp công trình), Đ26-27 (thẩm định BCNCKT — CQCM về xây dựng), Đ29 (thẩm định, phê duyệt thiết kế), Đ43-46 (giấy phép xây dựng), Đ48 (điều kiện khởi công), Đ57 (nghiệm thu, KTCTNT), Đ72 (công trình tạm), Đ91-92 (nội dung, trách nhiệm QLNN về xây dựng).
2. **Nghị định 207/2026/NĐ-CP ngày 15/6/2026** — quy định chi tiết Luật Xây dựng về **quản lý chất lượng, thi công xây dựng và bảo trì công trình**; **hiệu lực 01/7/2026**, **thay NĐ 06/2021/NĐ-CP** (và các NĐ sửa đổi 35/2023, 175/2024 phần QLCL). Điều then chốt: Đ24 (nghiệm thu hoàn thành), **Đ25-26-27 (kiểm tra công tác nghiệm thu, thẩm quyền, trình tự)**, Đ34-41 (bảo trì, đánh giá an toàn), Đ45-49 (sự cố công trình), Đ52 (hiệu lực), Đ53 (chuyển tiếp). Bãi bỏ Điều 8 NĐ 140/2025 và Điều 13 NĐ 144/2025.
3. **Nghị định 217/2026/NĐ-CP ngày 19/6/2026** — quy định chi tiết Luật Xây dựng về **quản lý hoạt động xây dựng**; **hiệu lực 01/7/2026**, thay NĐ 175/2024/NĐ-CP. Điều then chốt: Đ5 (phân loại dự án), Đ16-25 (thiết kế), Đ31-38 (thẩm định BCNCKT của CQCM), Đ41-43 (thẩm định thiết kế sau khi dự án được duyệt), Đ49-62 (giấy phép xây dựng: điều kiện, thẩm quyền, hồ sơ, trình tự).
3b. **Thông tư 34/2026/TT-BXD ngày 25/6/2026** — quy định chi tiết về **cấp công trình xây dựng** (điểm a khoản 2 Điều 6 Luật 135/2025); **hiệu lực 01/7/2026, thay TT 06/2021/TT-BXD**; bãi bỏ Điều 10 TT 09/2025/TT-BXD. Xác định cấp theo Phụ lục I (mức độ quan trọng/công suất), Phụ lục II (quy mô kết cấu), lấy cấp cao nhất; Phụ lục III ví dụ. Cấp công trình là căn cứ nền cho thẩm quyền thẩm định, cấp GPXD, đối tượng KTCTNT. Chi tiết + bảng tra ngành CT: reference `10`.

**Phân quyền, phân cấp — mô hình chính quyền 02 cấp:**
4. **Nghị định 140/2025/NĐ-CP ngày 12/6/2025** — **phân định thẩm quyền của chính quyền địa phương 02 cấp** trong lĩnh vực QLNN của Bộ Xây dựng; hiệu lực 01/7/2025, **hết hiệu lực 01/3/2027** (Điều 30). Cốt lõi: nhiệm vụ trước đây của UBND cấp huyện / cơ quan chuyên môn cấp huyện → **UBND cấp xã / cơ quan được giao quản lý xây dựng thuộc UBND cấp xã** (Đ4 GPXD, Đ5 công trình tạm, Đ7 quản lý hoạt động XD, Đ8 QLCL). **Lưu ý: Điều 8 đã bị NĐ 207/2026 bãi bỏ.**
5. **Nghị định 144/2025/NĐ-CP ngày 12/6/2025** — **phân quyền, phân cấp** trong lĩnh vực QLNN của Bộ Xây dựng; hiệu lực 01/7/2025, hết hiệu lực 01/3/2027 (Điều 45). Đ11 (thẩm định BCNCKT, thiết kế), Đ13 (QLCL — **đã bị NĐ 207/2026 bãi bỏ**). Đọc kèm để xác định thẩm quyền cấp tỉnh vs trung ương.

**Văn bản địa phương (Lào Cai) — cụ thể hóa cho tỉnh:**
6. **Quyết định 11/2026/QĐ-UBND ngày 29/01/2026 của UBND tỉnh Lào Cai** — Quy định một số nội dung về **quản lý đầu tư và xây dựng trên địa bàn tỉnh**. Đây là văn bản **áp dụng trực tiếp** cho mọi hồ sơ tại Lào Cai. Điều then chốt: Đ3 (chấp thuận vị trí, hướng tuyến, tổng mặt bằng), **Đ7 (thẩm quyền thẩm định BCNCKT/BCKTKT — liệt kê rõ Sở Công Thương là CQCM về xây dựng cấp tỉnh)**, Đ14 (thẩm quyền cấp GPXD), Đ16 (tiếp nhận thông báo khởi công), **Đ17 (KTCTNT + kiểm tra PCCC hằng năm)**, Đ18 (sự cố), Đ19-20 (trật tự xây dựng), Đ24 (chuyển tiếp). Bãi bỏ Điều 4 QĐ 58/2025/QĐ-UBND.

**Nhóm cắt giảm TTHC (tham chiếu khi thủ tục thay đổi):**
7. **NĐ 14/2026/NĐ-CP ngày 13/01/2026** — cắt giảm, đơn giản hóa TTHC liên quan SXKD (một phần lĩnh vực xây dựng); hiệu lực 15/01/2026 (một số điều 01/7/2026).
8. **NQ 24/2026/NQ-CP** (hiệu lực 29/4/2026 đến trước 01/3/2027) và **NQ 18/2026/NQ-CP** (hiệu lực 01/7/2026 đến hết 28/02/2027) — cắt giảm, phân cấp, đơn giản hóa TTHC, điều kiện kinh doanh (gồm lĩnh vực xây dựng). Dùng khi rà soát TTHC còn hiệu lực.

**Văn bản nền còn hiệu lực một phần / chuyển tiếp (đối chiếu khi hồ sơ cũ):**
9. **NĐ 06/2021, NĐ 35/2023, NĐ 175/2024** — **đã bị thay bởi NĐ 207/2026 và NĐ 217/2026 từ 01/7/2026**, nhưng vẫn áp dụng cho hồ sơ đã tiếp nhận / công trình khởi công trước 01/7/2026 theo điều khoản chuyển tiếp (Đ53 NĐ 207/2026, Đ95 Luật 135/2025). NĐ 175/2024 vẫn được QĐ 11/2026 viện dẫn cho nhiều thủ tục cấp tỉnh — kiểm tra kỹ điều khoản chuyển tiếp trước khi dẫn.
10. **NĐ 243/2025/NĐ-CP** (PPP), **NĐ 178/2025/NĐ-CP** (quy hoạch đô thị và nông thôn), **QĐ 409/QĐ-BXD 11/4/2025** (suất vốn đầu tư 2024) — tham chiếu chuyên đề khi gặp dự án PPP, quy hoạch, hoặc cần suất vốn.


### ⭐ CẮT GIẢM ĐIỀU KIỆN NĂNG LỰC TỪ 01/7/2026 (xác minh web 29/8/2026 — GATE trước khi yêu cầu doanh nghiệp nộp giấy tờ năng lực)
- **NĐ 212/2026/NĐ-CP ngày 17/6/2026** (hiệu lực 01/7/2026; ký PTT Phạm Gia Túc; 📗 toàn văn: `van-ban-goc/ND-212-2026-dieu-kien-nang-luc-HDXD-CSDL-quoc-gia.docx`, GATE 29/8/2026) — điều kiện năng lực HĐXD + Hệ thống thông tin, CSDL quốc gia về HĐXD (csdlhdxd.gov.vn):
  - **BÃI BỎ chứng chỉ năng lực của TỔ CHỨC** → tổ chức TỰ CÔNG KHAI thông tin năng lực trên csdlhdxd.gov.vn, người đại diện pháp luật chịu trách nhiệm toàn diện (Điều 41).
  - CCHN cá nhân chỉ còn **4 lĩnh vực**: khảo sát; lập quy hoạch đô thị - nông thôn; thiết kế; **giám sát thi công** (Điều 28). KHÔNG cấp CCHN Quản lý dự án, Định giá xây dựng (Điều 55).
  - **Chỉ huy trưởng, giám đốc QLDA: xét theo trình độ + kinh nghiệm (Điều 38), KHÔNG cần chứng chỉ.**
  - CCHN đã cấp theo Luật 2014: dùng đến hết hạn (khoản 5 Điều 55).
  - ⚠️ **Khoản 4 Điều 22: cơ quan QLNN KHÔNG được yêu cầu tổ chức, cá nhân cung cấp giấy tờ, thông tin đã có trên CSDL quốc gia về HĐXD.** Mã định danh dự án/công trình/năng lực: Điều 8, 14, 19.
- **NQ 66.18/2026/NQ-CP ngày 18/5/2026** (hiệu lực 01/7/2026 đến hết 28/02/2027, TRỪ ngoại lệ tại khoản 2, khoản 4 Điều 7 — đối chiếu toàn văn khi dùng; 📗 `van-ban-goc/NQ-66.18-2026-NQ-CP-phan-quyen-cat-giam-TTHC-DKKD.docx`, GATE 29/8/2026) — phân quyền, cắt giảm ĐKKD 11 ngành (có Xây dựng - PL I.8, Công Thương - PL I.2, Công an, Quốc phòng): không thực hiện điều kiện CCHN với chủ trì xác định - thẩm tra - quản lý chi phí (k1 Đ88 Luật 135); không thực hiện điều kiện năng lực với chủ trì kiểm định (k2 Đ88 + Đ87 NĐ 175/2024); cá nhân đủ điều kiện QLDA thì đủ điều kiện chỉ huy trưởng.
- **HỆ QUẢ NGHIỆP VỤ**: (1) không soạn văn bản yêu cầu DN nộp "chứng chỉ năng lực tổ chức" như điều kiện hiện hành — chỉ được yêu cầu minh chứng năng lực TẠI THỜI ĐIỂM thực hiện hoạt động nếu hoạt động đó diễn ra TRƯỚC 01/7/2026 (khung NĐ 175/2024), kèm nguyên tắc áp dụng quy định có lợi khi xem xét xử phạt; (2) hoạt động từ 01/7/2026: kiểm tra việc tự công khai trên csdlhdxd.gov.vn + CCHN cá nhân 4 lĩnh vực; (3) tra cứu trên hệ thống thay vì đòi nộp lại giấy tờ. Tiền lệ áp dụng: báo cáo vụ Đồng Tiến 29/8/2026. Ghi chú thêm từ toàn văn NQ 66.18: Phụ lục I.2 (Bộ Công Thương) phần VLNCN - tiền chất thuốc nổ chỉ điều chỉnh thủ tục thẩm quyền BỘ (XNK VLNCN 05 ngày - GP 06 tháng; kinh doanh/XNK tiền chất 03 ngày), KHÔNG thay đổi các thủ tục thẩm quyền cấp tỉnh (GP sử dụng VLNCN, kho, PANM); chuyển tiếp NĐ 212: khoản 1 Điều 55 xử lý kết quả thủ tục ban hành 01/01-30/6/2026 chưa cập nhật CSDL.

## III. NGUYÊN TẮC CỐT LÕI — "SỞ CÔNG THƯƠNG LÀ CQCM VỀ XÂY DỰNG ĐỐI VỚI CÔNG TRÌNH CÔNG NGHIỆP"

Đây là trục xác định mọi việc. Ba câu hỏi theo thứ tự:

**Câu 1 — Công trình này có phải "công trình công nghiệp" thuộc ngành Công Thương không?**
Có → SCT có thể là CQCM về xây dựng. Gồm: kho VLNCN, nhà máy - kho hóa chất, công trình khai thác - chế biến khoáng sản (trừ VLXD thông thường, xi măng), hạ tầng kỹ thuật CCN, cơ khí - luyện kim - điện tử, công nghiệp chế biến chế tạo, xăng dầu - LPG.
**Ngoại lệ trong nội bộ Sở:** công trình **điện lực** (nhà máy điện, lưới điện, TBA) → Phòng **QLNL** thẩm định, KHÔNG phải QLCN (xem `sct-laocai-org-vn`, `quy-hoach-ct-vn`).

**Câu 2 — Nghiệp vụ gì?** Ba nghiệp vụ CQCM về xây dựng mà SCT thực hiện:
| Nghiệp vụ | Căn cứ | Chuyên viên QLCN |
|---|---|---|
| Thẩm định BCNCKT/BCKTKT, thiết kế XD sau TK cơ sở của dự án ĐTXD công trình công nghiệp | Đ26-27, 29 Luật 135/2025; Đ31-43 NĐ 217/2026; **Đ7 QĐ 11/2026** | **Ngô Ngọc Dũng — CN(Dũng)** |
| Kiểm tra công tác nghiệm thu (KTCTNT) công trình chuyên ngành công nghiệp | Đ57 Luật 135/2025; **Đ25-27 NĐ 207/2026**; **Đ17 QĐ 11/2026** | CN(Dũng) (kho VLNCN: đồng thời CN(Khôi) từ 10/7/2026; trước đó CN(Linh)) |
| Giám định nguyên nhân, giải quyết sự cố công trình công nghiệp | Đ55 Luật 135/2025; Đ45-49 NĐ 207/2026; Đ18 QĐ 11/2026 | CN(Dũng) |

**Câu 3 — Cấp nào?** (bộ / tỉnh / xã) → mục IV.

## IV. PHÂN ĐỊNH THẨM QUYỀN 3 CẤP (sau NĐ 140/2025, 144/2025, QĐ 11/2026)

**Cấp trung ương (bộ):** Bộ Xây dựng thống nhất QLNN về xây dựng (Đ92 Luật 135/2025); CQCM về xây dựng thuộc bộ quản lý công trình chuyên ngành thẩm định/KTCTNT công trình cấp đặc biệt, nhóm A/dự án quan trọng quốc gia, công trình trên địa bàn ≥2 tỉnh (theo NĐ 217/2026, 207/2026).

**Cấp tỉnh (Lào Cai) — Đ7, Đ14, Đ17 QĐ 11/2026:**
- **CQCM về xây dựng cấp tỉnh = Sở Xây dựng, Sở Nông nghiệp và Môi trường, Sở Công Thương, BQL các KCN, BQL Khu kinh tế** — chủ trì thẩm định BCNCKT/BCKTKT dự án vốn đầu tư công và vốn nhà nước ngoài đầu tư công do Chủ tịch UBND tỉnh quyết định đầu tư (Đ7 khoản 1). SCT chủ trì phần **công trình công nghiệp**.
- **KTCTNT (Đ17 khoản 1):** CQCM về xây dựng cấp tỉnh kiểm tra công trình chuyên ngành trên địa bàn tỉnh (trừ công trình do cấp xã quyết định đầu tư chỉ lập BCKTKT); đồng thời tổ chức **kiểm tra PCCC hằng năm** theo điểm b khoản 2 Điều 13 NĐ 105/2025.
- **GPXD (Đ14):** Sở Xây dựng cấp GPXD công trình cấp đặc biệt/I/II (trừ nhà ở riêng lẻ và công trình trong KCN/KKT); **BQL KKT, BQL các KCN** cấp GPXD công trình trong KCN/KCX/khu công nghệ cao/KKT được giao (trừ nhà ở riêng lẻ).

**Cấp xã (sau 01/7/2025, không còn cấp huyện) — NĐ 140/2025 + Đ14 QĐ 11/2026:**
- Nhiệm vụ QLNN về xây dựng trước đây của UBND cấp huyện / CQCM cấp huyện → **UBND cấp xã / cơ quan được giao quản lý xây dựng thuộc UBND cấp xã** (Đ4, Đ7 NĐ 140/2025).
- **GPXD (Đ14 khoản 1c QĐ 11/2026):** UBND cấp xã cấp GPXD công trình cấp III, cấp IV và nhà ở riêng lẻ trên địa bàn (trừ công trình trong KCN/KKT). Công trình nằm trên ≥2 xã: một xã chủ trì cấp, thống nhất bằng văn bản với các xã còn lại (Đ14 khoản 1d).
- **KTCTNT (Đ17 khoản 2):** cơ quan quản lý xây dựng thuộc UBND cấp xã kiểm tra nghiệm thu công trình thuộc dự án chỉ lập BCKTKT do Chủ tịch UBND cấp xã quyết định đầu tư.
- **Công trình tạm (Đ5 NĐ 140/2025):** UBND cấp xã chấp thuận địa điểm, quy mô, thời gian tồn tại công trình tạm (khoản 2 Điều 131 Luật XD cũ / Đ72 Luật 135/2025); trình tự theo quy định của UBND tỉnh.
- **Trật tự xây dựng (Đ19-20 QĐ 11/2026):** UBND cấp xã quản lý trật tự XD trên địa bàn (trừ trong KCN/KKT do BQL quản lý).

## V. NGƯỜI KÝ, NGƯỜI SOẠN (khớp `sct-laocai-org-vn`)

- Lĩnh vực **thẩm định công trình công nghiệp** thuộc **PGĐ Hoàng Văn Thuân** phụ trách (tham gia quản lý dự án CN) → văn bản thường ký **KT. GIÁM ĐỐC / PHÓ GIÁM ĐỐC Hoàng Văn Thuân**. Tờ trình UBND tỉnh quan trọng: GĐ Hoàng Chí Hiền (cân nhắc theo vụ việc).
- PTP QLCN phụ trách "tham gia quản lý các dự án công nghiệp": **Trần Trọng Trang**.
- **Lưu VT, CN(tên):** văn bản về thẩm định BCNCKT/BCKTKT/thiết kế, KTCTNT, sự cố công trình công nghiệp → **CN(Dũng)** — Ngô Ngọc Dũng; kiểm duyệt nội bộ từ 10/7/2026: **PTP Nguyễn Hồng Vân** (thẩm định + KTCTNT thuộc phân công PTP Vân — xem skill `sct-laocai-org-vn`). Riêng công trình **kho VLNCN**, khi nghiệp vụ đan xen VLNCN thì phối hợp **CN(Khôi)** — Trần Đăng Khôi (từ 10/7/2026; trước đó CN(Linh) — Vũ Việt Linh) (xem plugin `kho-vlncn-sct-vn`, `sd-vlncn-sct-vn`).
- Ký hiệu: công văn `/SCT-CN`; thông báo `/TB-SCT`; tờ trình `/TTr-SCT`; báo cáo `/BC-SCT`; QĐ UBND `/QĐ-UBND`.

## VI. QUY TRÌNH TỔNG THỂ (công trình công nghiệp — SCT là CQCM về xây dựng)

```
GĐ1 CHUẨN BỊ DỰ ÁN → chủ trương đầu tư; lập BCNCKT/BCKTKT (Đ23-25 Luật 135; Đ27-30 NĐ 217)
GĐ2 THẨM ĐỊNH      → SCT thẩm định BCNCKT/BCKTKT + thiết kế (Đ26-27,29 Luật 135; Đ31-43 NĐ 217;
                     Đ7 QĐ 11/2026) → thông báo kết quả thẩm định
GĐ3 GIẤY PHÉP XD   → xin GPXD (nếu không thuộc diện miễn Đ43 Luật 135) HOẶC thông báo khởi công
                     kèm hồ sơ (công trình đã thẩm định BCNCKT → miễn GPXD, điểm e khoản 2 Đ43)
GĐ4 KHỞI CÔNG      → đủ điều kiện khởi công (Đ48 Luật 135); thông báo khởi công (Đ16 QĐ 11/2026);
                     quản lý chất lượng thi công (NĐ 207/2026)
GĐ5 NGHIỆM THU     → chủ đầu tư nghiệm thu (Đ57 Luật 135; Đ24 NĐ 207) → SCT KTCTNT với công trình
                     thuộc diện (Đ25-27 NĐ 207; Đ17 QĐ 11/2026) → thông báo chấp thuận kết quả
                     nghiệm thu (điều kiện đưa vào sử dụng)
GĐ6 KHAI THÁC      → bàn giao; bảo hành (Đ64 Luật 135); bảo trì, đánh giá an toàn (Đ34-41 NĐ 207);
                     xử lý sự cố nếu có (Đ45-49 NĐ 207); dừng khai thác khi cần (Đ67 Luật 135)
```

## VII. ANTI-ERROR RIÊNG LĨNH VỰC NÀY

1. **Luôn kiểm tra mốc 01/7/2026 và điều khoản chuyển tiếp — ĐỌC reference `11-chuyen-tiep-2026.md` TRƯỚC KHI CHỌN CĂN CỨ.** Công trình khởi công / hồ sơ tiếp nhận trước 01/7/2026 áp dụng NĐ 06/2021 + 175/2024 (Đ53 NĐ 207/2026; khoản 2 Đ76 NĐ 217/2026; Đ95 Luật 135/2025); từ 01/7/2026 áp NĐ 207/2026 + 217/2026. Ba mốc độc lập của một dự án (tiếp nhận hồ sơ / quyết định đầu tư / khởi công) có thể rơi vào các khung khác nhau — lập luận chuyển tiếp phải THÀNH VĂN trong phiếu trình và văn bản ban hành, không trộn căn cứ. Bản gốc khung cũ (NĐ 06/2021, NĐ 175/2024, TT 06/2021 + TT 02/2025) đã có trong `van-ban-goc/`. *(Bài học vụ Âu Lâu 8/2026: thẩm định BCNCKT theo khung mới cho hồ sơ tiếp nhận 18/3/2026 mà không lập luận khoản 2 Đ76.)*
2. **Không nhầm "phân định thẩm quyền 2 cấp" (NĐ 140/2025) đã bị bãi bỏ một phần:** Điều 8 NĐ 140/2025 và Điều 13 NĐ 144/2025 **đã bị NĐ 207/2026 bãi bỏ** — phần QLCL nay theo NĐ 207/2026. Kiểm tra trước khi viện dẫn.
3. **Công trình điện KHÔNG thuộc QLCN** — chuyển Phòng QLNL. Chỉ giữ ở QLCN: công nghiệp chế biến chế tạo, khoáng sản, hóa chất, VLNCN, CCN.
4. **Cấp huyện không còn** (sau 01/7/2025): mọi thẩm quyền cấp huyện cũ đã chuyển UBND cấp xã. Không viết "UBND huyện", "Phòng Kinh tế - Hạ tầng huyện". Địa danh: **xã + tỉnh Lào Cai**.
5. **Miễn GPXD ≠ miễn mọi thủ tục:** công trình miễn GPXD (Đ43 khoản 2 Luật 135, gồm công trình đã thẩm định BCNCKT, công trình tạm, cấp IV nhỏ...) vẫn phải **gửi thông báo khởi công kèm hồ sơ** (Đ43 khoản 3).
6. **KTCTNT là điều kiện đưa vào sử dụng:** công trình thuộc diện KTCTNT chỉ được khai thác sau khi có văn bản chấp thuận kết quả nghiệm thu (Đ57 Luật 135; Đ25 NĐ 207). Biên bản nghiệm thu của chủ đầu tư không thay thế.
7. **Phân biệt "thẩm định thiết kế" và "kiểm tra nghiệm thu":** hai nghiệp vụ khác nhau, ở hai giai đoạn khác nhau; công trình có thể miễn thẩm định nhưng vẫn thuộc diện KTCTNT và ngược lại. Không gộp.
8. **GATE mọi PDF đến; không tự điền số/ngày văn bản chưa ban hành;** render kiểm tra trước khi giao (qua `vbhc-vn`).
9. **Không dẫn nhầm cặp nghị định "sinh đôi" 207 ↔ 217:** NĐ 207/2026 = chất lượng - thi công - bảo trì - nghiệm thu; NĐ 217/2026 = dự án - thiết kế - thẩm định - GPXD. Cùng số điều nhưng nội dung khác hẳn (vd Đ26 NĐ 207 = thẩm quyền KTCTNT, Đ26 NĐ 217 = quy hoạch làm căn cứ lập BCNCKT). Trước trình ký: rà mọi cụm "Điều … Nghị định 2x7/2026" và đối chiếu TÊN ĐIỀU trong văn bản gốc. *(Lỗi thật vụ Âu Lâu.)*
10. **Thẩm tra thiết kế là nghĩa vụ hay bị bỏ sót:** công trình ảnh hưởng lớn AT-LICĐ (Phụ lục IV NĐ 217) bắt buộc THẨM TRA thiết kế làm cơ sở cho CĐT thẩm định (điểm a khoản 5 Đ26 + khoản 3 Đ29 Luật 135; khoản 4 Đ41 NĐ 217), kèm thẩm tra nội dung PCCC nếu thuộc diện thẩm định PCCC (điểm b khoản 5 Đ26). Công văn hướng dẫn DN về thiết kế sau TKCS phải nhắc CẢ thẩm tra, không chỉ "thẩm định, phê duyệt". *(Bài học vụ phân lân nung chảy 8/2026.)*
11. **Thời hạn thẩm định là thời hạn cứng (Đ37 NĐ 217):** nhóm C cấp II = 12 ngày làm việc từ khi hồ sơ hợp lệ; cần thêm → văn bản gia hạn NGAY, nêu lý do, chỉ 01 lần; ý kiến nội bộ liên phòng xin từ đầu, không dồn sát ngày ban hành. Sau 25/02/2026, đánh giá phù hợp quy hoạch tại Lào Cai đối chiếu **QĐ 525/QĐ-UBND** (điều chỉnh quy hoạch tỉnh hợp nhất), quy hoạch tỉnh Yên Bái cũ chỉ nêu ở phần quá trình pháp lý. *(Vụ Âu Lâu: 5 tháng không gia hạn; đánh giá theo quy hoạch cũ.)*
12. **Chỉ khẳng định điều có tài liệu đối chiếu; nội dung đánh giá theo đặc thù công trình:** không xác nhận "phù hợp" cho hạng mục không tồn tại (vd thang máy chữa cháy, gian lánh nạn ở TBA ngoài trời); không kết luận về năng lực/CCHN khi thành phần hồ sơ không có; văn bản trùng số/ngày/trích yếu trong danh mục → kiểm bản gốc, loại một; mọi con số xuất hiện ≥2 lần và mọi phép tính in trong văn bản (kể cả phí thẩm định nội suy TT 28/2023) phải tự khớp khi đối chiếu chéo thông báo ↔ phiếu trình ↔ hồ sơ. Chi tiết 8 nhóm lỗi: `vi-du-thuc-te/au-lau-110kv-tham-dinh-BCNCKT/README-BAI-HOC.md`.

13. ⭐ **Kiểm tra NHÓM LOẠI TRỪ trước khi kết luận công trình thuộc diện KTCTNT** (bổ sung 31/8/2026): khoản 1 Điều 25 NĐ 207/2026 loại trừ công trình thuộc điểm a khoản 1 Điều 69, các Điều 70, 71 và **72** (công trình xây dựng tạm) Luật 135/2025 — phần loại trừ đứng TRƯỚC cụm "bao gồm" nên chi phối cả ba điểm a, b, c. Một công trình tạm vẫn nằm trong Phụ lục IV NĐ 217/2026 mà vẫn được miễn KTCTNT; phải viết lập luận hai tầng thành văn. Khoản 1 Điều 24 **NĐ 06/2021 không có nhóm loại trừ này** và còn có tiêu chí "vốn đầu tư công" đã bị bỏ → hồ sơ vắt qua mốc phải áp khoản 3 Điều 53: khởi công trước 01/7/2026, thuộc diện theo NĐ 06/2021 nhưng không thuộc diện theo NĐ 207/2026 thì **DỪNG, không kiểm tra tiếp**. Chi tiết: reference `04` mục I.0, reference `06` mục V, reference `11` bảng quyết định.

14. **Gọi đúng tên tài liệu quản lý chất lượng:** không có "nhật ký giám sát" trong NĐ 06/2021 lẫn NĐ 207/2026. Nhà thầu thi công lập **nhật ký thi công xây dựng công trình** (k13 Đ15, Phụ lục IIa); tư vấn giám sát lập **báo cáo về công tác giám sát thi công xây dựng công trình** (k3 Đ20, Phụ lục IVa định kỳ/theo giai đoạn và IVb khi nghiệm thu); nhà thầu thiết kế lập **báo cáo đánh giá việc thực hiện giám sát tác giả** (Đ21). Yêu cầu tài liệu không có trong quy định là đặt thêm điều kiện trái pháp luật. Chi tiết: reference `04` mục I.0b.

## VIII. CẤU TRÚC PLUGIN

```
references/
  01-khung-phap-ly.md            Chi tiết từng văn bản, điều khoản, quan hệ thay thế - chuyển tiếp
  02-tham-quyen-3-cap.md         Bảng phân định bộ/tỉnh/xã; loại - cấp công trình; CQCM xây dựng
  03-tham-dinh-khoi-cong.md      Thẩm định BCNCKT/BCKTKT/thiết kế + điều kiện khởi công + QLCL thi công
  04-kiem-tra-nghiem-thu.md      KTCTNT: đối tượng, thẩm quyền, trình tự, văn bản đầu ra (NĐ 207, QĐ 11)
  05-giay-phep-xay-dung.md       GPXD: phải xin/miễn, thẩm quyền tỉnh-xã-BQL, hồ sơ, trình tự
  06-cong-trinh-tam.md           Công trình tạm Đ72 Luật 135; liên kết kho VLNCN tạm
  07-su-co-bao-tri-an-toan.md    Sự cố, giám định, bảo trì, đánh giá an toàn, dừng khai thác
  08-cong-trinh-cong-thuong.md   CHUYÊN SÂU: từng loại công trình ngành CT, ai thẩm định, cấp mấy
  09-hoi-dap-doanh-nghiep.md     FAQ trả lời DN + tham chiếu văn bản
  10-cap-cong-trinh.md           Cấp công trình theo TT 34/2026; bảng tra chuyên sâu công trình ngành CT
  11-chuyen-tiep-2026.md         GATE CHUYỂN TIẾP quanh mốc 01/7/2026: bảng quyết định khung áp dụng
                                 (Đ53 NĐ 207, Đ76 NĐ 217), 3 mốc thời gian, câu mẫu lập luận
mau-van-ban/                     Mẫu KH kiểm tra, TB nghiệm thu, CV thẩm định, phiếu trình
van-ban-goc/                     Luật 135/2025, NĐ 207/2026, NĐ 217/2026, NĐ 140/2025, NĐ 144/2025,
                                 QĐ 11/2026 (Lào Cai); nhóm CHUYỂN TIẾP: NĐ 06/2021, NĐ 175/2024,
                                 TT 06/2021 + TT 02/2025; TT 36/2026 (chi phí), TT 39/2026 (CSDL)
vi-du-thuc-te/
  au-lau-110kv-tham-dinh-BCNCKT/ Case study thẩm định BCNCKT ĐZ+TBA 110kV Âu Lâu (Phòng QLNL, 8/2026):
                                 14 file hồ sơ + README-BAI-HOC.md (8 nhóm lỗi cần tránh + điểm làm đúng).
                                 CHỈ THAM KHẢO QUY TRÌNH — không clone văn bản làm mẫu.
```

## IX. QUY TẮC LÀM VIỆC

1. Trả lời/soạn thảo bằng tiếng Việt, văn phong hành chính.
2. Trước khi viện dẫn văn bản đến (PDF): chạy GATE trích số/ngày/người ký từ file.
3. Luôn xác định **mốc thời gian hiệu lực** (trước/sau 01/7/2026) trước khi chọn căn cứ pháp lý.
4. Không dùng dữ liệu hiện trạng (tên DN đang làm hồ sơ, tiến độ) từ skill làm dữ liệu thời sự — hỏi Bạn số liệu mới nhất.
5. Mọi mẫu văn bản khi xuất docx: theo thể thức NĐ 30/2020 qua skill `vbhc-vn`; render kiểm tra trước khi giao.
6. Khi số văn bản địa phương chưa chắc chắn: để trống + hỏi Bạn, không đoán.
7. Với công trình cụ thể, luôn chạy 3 câu hỏi mục III trước khi tư vấn thẩm quyền.
