---
name: attp-sct-vn
description: "Chuyên gia QLNN về AN TOÀN THỰC PHẨM và CÔNG NGHIỆP TIÊU DÙNG - THỰC PHẨM, Sở Công Thương tỉnh Lào Cai. 6 nghiệp vụ: (1) thẩm định, cấp/cấp lại/thu hồi Giấy chứng nhận cơ sở đủ điều kiện ATTP thuộc trách nhiệm Bộ Công Thương (đã phân cấp về UBND cấp tỉnh - khoản 5 Điều 37 NĐ 146/2025); (2) tự công bố sản phẩm, xác định cơ sở không thuộc diện cấp GCN (Điều 12 NĐ 15/2018); (3) thuốc lá: Giấy phép chế biến nguyên liệu, phân phối, bán buôn sản phẩm thuốc lá; (4) rượu: SX công nghiệp, phân phối, bán buôn; (5) hậu kiểm, kiểm tra chuyên ngành, truy xuất nguồn gốc, thu hồi sản phẩm; (6) báo cáo, thống kê. CẢNH BÁO: NĐ 46/2026 đang TẠM NGƯNG theo NQ 15/2026, áp dụng lại NĐ 15/2018 - đọc reference 08 trước khi trích căn cứ. Từ khóa: ATTP, GCNATTP-SCTLC, tự công bố, NĐ 15/2018, NĐ 46/2026, NQ 15/2026, TT 43/2018/TT-BCT, thuốc lá, NĐ 67/2013, rượu, NĐ 105/2017, sữa chế biến, dầu thực vật, bánh kẹo, bia, nước giải khát, hậu kiểm, ngộ độc thực phẩm, CN(Nam)."
---

# attp-sct-vn - An toàn thực phẩm và công nghiệp tiêu dùng - thực phẩm (Sở Công Thương Lào Cai)

## I. KHI NÀO DÙNG SKILL NÀY

Kích hoạt skill khi xử lý bất kỳ việc nào sau đây:

- Thẩm định hồ sơ, tham mưu cấp mới, cấp lại, thu hồi **Giấy chứng nhận cơ sở đủ điều kiện an toàn thực phẩm** đối với cơ sở sản xuất, kinh doanh thực phẩm thuộc trách nhiệm quản lý của Bộ Công Thương trên địa bàn tỉnh.
- Xác định **một cơ sở/sản phẩm thuộc ngành nào quản lý**: Công Thương, Y tế hay Nông nghiệp và Môi trường; xác định cơ sở **không thuộc diện cấp** Giấy chứng nhận.
- Tiếp nhận, rà soát hồ sơ **tự công bố sản phẩm**; hướng dẫn doanh nghiệp về ghi nhãn, chỉ tiêu kiểm nghiệm, hồ sơ công bố.
- Cấp phép, hướng dẫn lĩnh vực **thuốc lá**: Giấy phép chế biến nguyên liệu thuốc lá; Giấy phép phân phối, bán buôn sản phẩm thuốc lá; chấp thuận nhập khẩu nguyên liệu, máy móc thiết bị chuyên ngành thuốc lá.
- Cấp phép, hướng dẫn lĩnh vực **rượu**: Giấy phép sản xuất rượu công nghiệp, Giấy phép phân phối, bán buôn rượu.
- **Hậu kiểm, kiểm tra chuyên ngành** ATTP; truy xuất nguồn gốc; thu hồi, xử lý sản phẩm không bảo đảm an toàn; phối hợp xử lý sự cố, ngộ độc thực phẩm.
- Soạn công văn hướng dẫn doanh nghiệp, tờ trình, quyết định, kế hoạch, báo cáo định kỳ/chuyên đề trong lĩnh vực ATTP và công nghiệp tiêu dùng - thực phẩm (Tháng hành động vì ATTP, Tết Trung thu, Tết Nguyên đán).
- Trả lời câu hỏi của doanh nghiệp, hộ kinh doanh về điều kiện, hồ sơ, thời hạn, phí, lệ phí.

**Xử phạt vi phạm hành chính về ATTP (NĐ 115/2018/NĐ-CP và văn bản sửa đổi) KHÔNG xử lý trong plugin này.** Plugin chỉ thực hiện thu hồi Giấy chứng nhận (biện pháp của cơ quan cấp) và kiến nghị, chuyển hồ sơ khi phát hiện vi phạm qua kiểm tra.

### Liên kết hệ sinh thái plugin/skill

| Tình huống chạm ranh giới | Plugin/skill gọi kèm | Nội dung liên quan |
|---|---|---|
| Soạn văn bản kết quả (CV, GCN, TTr, QĐ, KH, BC) | `vbhc-vn` | Thể thức NĐ 30/2020, Chế độ A/B, tên file chuẩn, QA render |
| Nhận PDF văn bản đến, hồ sơ DN | `vbhc-pdf-reader-vn` | Đọc đúng số/ngày/người ký từ file gốc (GATE PDF) |
| Xác định người ký, dòng Lưu CN(tên), phòng chủ trì | `sct-laocai-org-vn` | ATTP/CN tiêu dùng - thực phẩm: CN(Nam); PGĐ phụ trách ATTP: Nguyễn Đình Chiến |
| Cơ sở chế biến thực phẩm dùng hóa chất, phụ gia thuộc quản lý hóa chất | `hc-sct-vn` | GCN đủ điều kiện SX/KD hóa chất, khai báo hóa chất |
| Cơ sở nằm trong KCN, CCN | `kccn-sct-vn` | Vị trí, đầu mối quản lý hạ tầng |
| Điều kiện PCCC của cơ sở chế biến thực phẩm, kho hàng | `pccc-sct-vn` | Phụ lục phân loại cơ sở, thẩm duyệt, kiểm tra |
| Nhà xưởng, công trình của cơ sở | `xd-sct-vn` | Thẩm định thiết kế, KTCTNT công trình công nghiệp |
| Bài phát biểu của lãnh đạo Sở tại hội nghị ATTP | `bpb-sct-vn` | Kết cấu, giọng văn nói, định dạng riêng |

## II. CẢNH BÁO HIỆU LỰC BẮT BUỘC ĐỌC TRƯỚC (tình trạng đặc biệt năm 2026)

Lĩnh vực ATTP đang ở trạng thái pháp lý **hai lớp**, rất dễ trích sai căn cứ:

1. **Nghị định số 46/2026/NĐ-CP** ngày 26/01/2026 quy định chi tiết thi hành Luật An toàn thực phẩm (thay thế NĐ 15/2018) đã **BỊ TẠM NGƯNG HIỆU LỰC**.
2. Việc tạm ngưng thực hiện theo **Nghị quyết số 09/2026/NQ-CP** ngày 04/02/2026, sau đó được thay thế bởi **Nghị quyết số 15/2026/NQ-CP** ngày 06/4/2026 (hiệu lực từ ngày ký). NQ 15/2026 tạm ngưng hiệu lực áp dụng NĐ 46/2026 và Nghị quyết số 66.13/2026/NQ-CP ngày 27/01/2026 **cho đến khi Luật An toàn thực phẩm (sửa đổi) và Nghị định hướng dẫn có hiệu lực thi hành**.
3. Trong thời gian tạm ngưng, **Nghị định số 15/2018/NĐ-CP** ngày 02/02/2018 và các văn bản hướng dẫn **tiếp tục có hiệu lực**. Hồ sơ đã nộp trước ngày NQ 15/2026 có hiệu lực tiếp tục giải quyết theo NĐ 15/2018.
4. Luật ATTP (sửa đổi) tính đến thời điểm cập nhật skill **vẫn đang trong quá trình soạn thảo**, chưa trình Quốc hội thông qua.

**Quy tắc áp dụng khi soạn văn bản:** căn cứ pháp lý dẫn **Luật An toàn thực phẩm số 55/2010/QH12** và **Nghị định số 15/2018/NĐ-CP**; **KHÔNG dẫn NĐ 46/2026** trừ khi Bạn xác nhận đã có văn bản mới chấm dứt tạm ngưng. Trước khi phát hành văn bản chính thức, kiểm tra lại tình trạng hiệu lực (chi tiết và mốc thời gian tại reference 08).

## III. KHUNG PHÁP LÝ

### 1. Nền tảng an toàn thực phẩm
- **Luật An toàn thực phẩm số 55/2010/QH12** ngày 17/6/2010.
- **Nghị định số 15/2018/NĐ-CP** ngày 02/02/2018 quy định chi tiết thi hành một số điều của Luật An toàn thực phẩm - **văn bản nghiệp vụ cốt lõi đang áp dụng** (tự công bố, đăng ký bản công bố, cấp GCN cơ sở đủ điều kiện, các trường hợp không thuộc diện cấp GCN tại Điều 12, phân công trách nhiệm quản lý tại Điều 36-39 và các Phụ lục).
- **Nghị định số 46/2026/NĐ-CP** ngày 26/01/2026 - **đang tạm ngưng hiệu lực** (xem mục II).
- **Nghị quyết số 15/2026/NQ-CP** ngày 06/4/2026 (thay thế NQ 09/2026/NQ-CP ngày 04/02/2026).
- **Thông tư số 43/2018/TT-BCT** ngày 15/11/2018 (hiệu lực 01/01/2019) quy định về quản lý an toàn thực phẩm thuộc trách nhiệm của Bộ Công Thương - quy định hồ sơ, trình tự, thủ tục cấp Giấy chứng nhận cơ sở đủ điều kiện ATTP; chỉ định cơ sở kiểm nghiệm; thu hồi sản phẩm.
- **Nghị định số 115/2018/NĐ-CP** về xử phạt VPHC về ATTP (dùng để nhận diện hành vi, không xử lý trình tự xử phạt trong plugin này).

### 2. Phân cấp, phân quyền
- **Nghị định số 146/2025/NĐ-CP** ngày 12/6/2025 (hiệu lực 01/7/2025), Chương XIV - Điều 37 phân cấp lĩnh vực ATTP. Đáng chú ý **khoản 5 Điều 37**: nhiệm vụ, quyền hạn của Bộ Công Thương về **cấp Giấy chứng nhận cơ sở đủ điều kiện an toàn thực phẩm thuộc trách nhiệm quản lý của Bộ Công Thương** quy định tại khoản 6 Điều 39 NĐ 15/2018 **do Ủy ban nhân dân cấp tỉnh thực hiện**; trình tự, thủ tục theo Phụ lục XI. Các khoản khác: kiểm tra nhà nước đối với thực phẩm xuất khẩu và truy xuất nguồn gốc sản phẩm không bảo đảm an toàn do **Chủ tịch UBND cấp tỉnh** thực hiện; chỉ định cơ sở kiểm nghiệm phục vụ QLNN, chỉ định cơ quan kiểm tra nhà nước về ATTP nhập khẩu do **UBND cấp tỉnh** thực hiện.
- **Nghị định số 139/2025/NĐ-CP** ngày 12/6/2025 về phân định thẩm quyền của chính quyền địa phương 02 cấp trong lĩnh vực QLNN của Bộ Công Thương (xác định việc gì thuộc cấp xã).
- **Nghị quyết số 19/2026/NQ-CP** về cắt giảm, phân cấp, đơn giản hóa TTHC, điều kiện kinh doanh thuộc phạm vi quản lý của Bộ Công Thương.
- **Nghị quyết số 66.18/2026/NQ-CP** ngày 18/5/2026 (hiệu lực 01/7/2026 đến hết 28/02/2027).
- **Quyết định số 28/2025/QĐ-UBND ngày 10/11/2025** của UBND tỉnh Lào Cai về phân cấp quản lý nhà nước về ATTP trên địa bàn tỉnh (hiệu lực **20/11/2025**), thay thế QĐ 08/2021/QĐ-UBND của tỉnh Yên Bái và QĐ 45/2024/QĐ-UBND của tỉnh Lào Cai - **văn bản gối đầu để phân định thẩm quyền tại địa phương** (reference 01).
- **Quyết định số 904/QĐ-UBND ngày 26/8/2025** ủy quyền Giám đốc Sở Công Thương thành lập Đoàn thẩm định cấp GCN ATTP - **thời hạn đến hết 31/12/2025**, phải kiểm tra văn bản thay thế (reference 02).
- **Quyết định số 217/QĐ-UBND ngày 27/01/2026** kiện toàn Ban Chỉ đạo An toàn thực phẩm tỉnh.
- **Thông tư số 38/2025/TT-BCT ngày 19/6/2025**, khoản 2 Điều 16 sửa khoản 2 Điều 6 TT 43/2018/TT-BCT: thẩm quyền cấp GCN do UBND cấp tỉnh thực hiện.
- **NĐ 17/2020/NĐ-CP** (Mẫu 03a Biên bản thẩm định, Mẫu 05C Giấy chứng nhận), **NĐ 77/2016/NĐ-CP**, **NĐ 155/2018/NĐ-CP**.
- QCVN mới 2026: **TT 09/2026/TT-BCT** (sữa dạng lỏng), **TT 10/2026/TT-BCT** (dầu thực vật tinh chế), **TT 39/2026/TT-BCT** (đồ uống có cồn) - chưa đối chiếu toàn văn.

### 3. Thuốc lá (chi tiết tại reference 06)
- **Nghị định số 67/2013/NĐ-CP** ngày 27/6/2013, sửa đổi bởi NĐ 106/2017/NĐ-CP, NĐ 08/2018/NĐ-CP, NĐ 17/2020/NĐ-CP.
- **Nghị định số 146/2025/NĐ-CP**, Điều 18-19: phân cấp hàng loạt nhiệm vụ về UBND cấp tỉnh, trong đó **khoản 5 Điều 18** phân cấp cấp, cấp lại, cấp sửa đổi, bổ sung, thu hồi **Giấy phép chế biến nguyên liệu thuốc lá** (khoản 1 Điều 14, Điều 43 NĐ 67/2013) từ Bộ Công Thương **về UBND cấp tỉnh**.
- **Nghị quyết số 19/2026/NQ-CP** (Phụ lục II phần B): cắt giảm điều kiện; bãi bỏ điều kiện cấp Giấy phép mua bán nguyên liệu thuốc lá, GCN đủ điều kiện đầu tư trồng cây thuốc lá.

### 4. Rượu, bia, nước giải khát (chi tiết tại reference 07)
- **Nghị định số 105/2017/NĐ-CP** ngày 14/9/2017 về kinh doanh rượu, sửa đổi bởi NĐ 17/2020/NĐ-CP.
- **Nghị định số 146/2025/NĐ-CP**, Điều 20: phân cấp về UBND cấp tỉnh việc cấp Giấy phép sản xuất rượu công nghiệp quy mô từ 03 triệu lít/năm trở lên và Giấy phép phân phối rượu.

## IV. NGUYÊN TẮC BẤT BIẾN KHI DÙNG SKILL

1. **Không bịa số, ngày văn bản.** Mọi số/ngày trong skill này đã được đối chiếu nguồn; nội dung nào chưa xác minh đều ghi rõ "chưa xác minh - hỏi Bạn".
2. **GATE PDF:** trước khi viện dẫn số, ngày, người ký của văn bản đến, đọc từ file gốc trên đĩa, không lấy từ context hiển thị.
3. **GATE HIỆU LỰC ATTP:** mỗi lần trích căn cứ ATTP, kiểm tra mục II; mặc định dùng NĐ 15/2018, không dùng NĐ 46/2026.
3a. **GATE ỦY QUYỀN ĐOÀN THẨM ĐỊNH:** QĐ 904/QĐ-UBND ngày 26/8/2025 ủy quyền Giám đốc Sở lập Đoàn thẩm định chỉ có thời hạn **đến hết 31/12/2025**. Trước khi soạn Quyết định thành lập Đoàn thẩm định hoặc viện dẫn căn cứ ủy quyền, **hỏi Bạn** về Quyết định ủy quyền năm 2026 (reference 02 mục 1).
4. **Không tra hiện trạng cơ sở trong skill** (số lượng cơ sở đã cấp GCN, danh sách doanh nghiệp) - dữ liệu tĩnh dễ lỗi thời; hỏi Bạn hoặc chờ số liệu cập nhật.
5. **Ký hiệu văn bản:** dùng SCT-CN và dòng Lưu VT, CN(Nam) cho lĩnh vực ATTP/CN tiêu dùng - thực phẩm; GCN ATTP dùng ký hiệu GCNATTP-SCTLC. Không tự đổi sang ký hiệu phòng khác.
6. **Người ký:** GCN, quyết định, báo cáo quan trọng - Giám đốc Sở Hoàng Chí Hiền; KT.GĐ - PGĐ Nguyễn Đình Chiến (phụ trách ATTP).
7. **Biên bản thẩm định/kiểm tra dạng bảng có ô đánh giá (Đạt/Không đạt, checkbox):** giữ nguyên như mẫu, **không tự điền X**, chỉ thay thông tin cơ sở.

## V. BẢN ĐỒ REFERENCES

| File | Nội dung |
|---|---|
| `references/01-pham-vi-phan-cong.md` | QĐ 28/2025/QĐ-UBND: 6 nguyên tắc phân cấp, nhiệm vụ Sở Công Thương (Điều 6), ranh giới với cấp xã (Điều 7), Sở Y tế, Sở NN&MT; QCVN sản phẩm mới |
| `references/02-gcn-du-dieu-kien-attp.md` | Điều kiện, hồ sơ, trình tự, thời hạn, thẩm quyền cấp/cấp lại/thu hồi GCN theo TT 43/2018 |
| `references/03-tu-cong-bo-san-pham.md` | Tự công bố, đăng ký bản công bố, ghi nhãn, kiểm nghiệm |
| `references/04-khong-thuoc-dien-cap-gcn.md` | Điều 12 NĐ 15/2018 - các trường hợp miễn và nghĩa vụ thay thế |
| `references/05-hau-kiem-kiem-tra.md` | Hậu kiểm, kiểm tra chuyên ngành, truy xuất nguồn gốc, thu hồi sản phẩm, sự cố ATTP |
| `references/06-thuoc-la.md` | Toàn bộ mảng thuốc lá: 03 TTHC nguyên liệu thuốc lá, thẩm quyền sau phân cấp, điều kiện sau cắt giảm |
| `references/07-ruou-bia-nuoc-giai-khat.md` | Cấp phép rượu, phân cấp theo NĐ 146/2025 |
| `references/08-canh-bao-hieu-luc-2026.md` | Diễn biến NĐ 46/2026 - NQ 09/2026 - NQ 15/2026 - Luật ATTP (sửa đổi); cách trích căn cứ an toàn |
| `mau-ho-so/` | 05 tài liệu hướng dẫn và mẫu thật của Sở (xem README trong thư mục) |
| `vi-du-thuc-te/` | Vụ Siêu thị An Lạc (GCN ATTP 9/2025) và vụ Kim Ngọc (thuốc lá 2025) |
| `van-ban-goc/` | QĐ 28/2025, QĐ 904, NQ 15/2026, TT 43/2018, TT 57/2018, TT 43/2023 |

## VI. VIỆC CÒN THIẾU (cần Bạn cung cấp để hoàn thiện v1.2)

Xếp theo mức độ cấp thiết:

1. **Quyết định ủy quyền lập Đoàn thẩm định năm 2026** thay QĐ 904/QĐ-UBND (hết hạn 31/12/2025) - đang chặn việc soạn Quyết định thành lập Đoàn thẩm định.
2. **Phụ lục I, II, III của QĐ 28/2025/QĐ-UBND** (danh mục sản phẩm từng ngành) - bản PDF hiện có không kèm phụ lục; đây là phần tra cứu hằng ngày.
3. **Quyết định công bố TTHC** lĩnh vực ATTP, rượu, thuốc lá đang áp dụng - để chốt thời hạn giải quyết, phí, lệ phí.
4. **Bộ biểu mẫu sạch**: Đơn Mẫu 01a, Bản thuyết minh Mẫu 02a (TT 43/2018); Biên bản thẩm định Mẫu 03a, Giấy chứng nhận Mẫu 05C (NĐ 17/2020); Bản tự công bố Mẫu 01 (NĐ 15/2018); mẫu bản cam kết.
5. **01 bộ hồ sơ cấp GCN ATTP hoàn chỉnh, bản sạch** (Tờ trình + Biên bản thẩm định + Giấy chứng nhận đã ký) để làm mẫu chuẩn Chế độ B.
6. Kế hoạch, báo cáo ATTP gần nhất của Sở (Tháng hành động vì ATTP, Tết Trung thu, Tết Nguyên đán) để lấy bố cục và giọng văn.
7. Bản đọc được của **TT 57/2018/TT-BCT** và **TT 43/2023/TT-BCT** (hai file PDF hiện là bản scan, không trích được text) để lấy biểu mẫu thuốc lá.
