> [LƯU TRỮ] Đây là BẢN GỐC của skill anti-error-sct-vn trước khi hợp nhất vào vbhc-vn (ngày 20/6/2026). Nội dung đã được tích hợp vào mục "Phòng tránh 5 nhóm sai lầm tham mưu" của vbhc-vn. Script kiểm tra nay ở <thư mục skill vbhc-vn>/scripts/check_document.py. File này chỉ để tra cứu lịch sử.

---
name: anti-error-sct-vn
description: "Quy trình bắt buộc phòng tránh 5 nhóm sai lầm trong tham mưu, soạn thảo VBHC cho Lãnh đạo Sở Công Thương và văn bản trình UBND tỉnh. Kích hoạt khi: tham mưu pháp lý; soạn công văn, tờ trình, báo cáo, quyết định, kế hoạch dựa trên văn bản chỉ đạo cấp trên; thẩm định hồ sơ; rà soát, góp ý dự thảo; viết bài phát biểu, tham luận của Lãnh đạo; tham gia ý kiến dự thảo VBQPPL; nhận PDF VBHC cần dẫn chiếu chính xác số/ngày. 5 nhóm sai lầm: (A) bịa số văn bản pháp luật; (B) tự suy diễn nhiệm vụ ngoài văn bản chỉ đạo cấp trên; (C) dùng từ suy đoán ('dự kiến', 'gần như', 'có thể') trong văn bản trình ký; (D) dùng VBPL đã hết hiệu lực; (E) tin context window đối với số/ngày từ PDF có header 2 cột. Từ khoá: tham mưu, soạn công văn, tờ trình, báo cáo, quyết định, kế hoạch, thẩm định, rà soát, góp ý dự thảo, bài phát biểu, viện dẫn pháp luật, căn cứ pháp lý, triển khai chỉ đạo, file PDF, công văn đến, văn bản đến."
---

# anti-error-sct-vn — Phòng tránh sai lầm tham mưu hành chính

## Tại sao skill này tồn tại

Skill này không phải lý thuyết — nó được rút ra từ những sai lầm **đã thực sự xảy ra** trong công việc của Bạn (Giám đốc Sở Công Thương tỉnh Lào Cai) với Claude. Mỗi quy tắc bên dưới đều có ít nhất một vụ việc làm minh chứng. Mục tiêu là không lặp lại.

Trong thẩm định, tham mưu, soạn văn bản hành chính cấp Sở/Tỉnh: **một sai sót pháp lý hoặc tự suy diễn ngoài thẩm quyền có thể dẫn đến quyết định hành chính sai, gây hậu quả cho cơ quan và doanh nghiệp**. Vì vậy quy trình bên dưới là bắt buộc, không phải tuỳ chọn.

## Khi nào dùng

- Tham mưu cho Lãnh đạo Sở Công Thương nội dung triển khai văn bản chỉ đạo cấp trên (UBND tỉnh, Bộ, Tỉnh uỷ).
- Soạn công văn, tờ trình, báo cáo, quyết định, kế hoạch, bài phát biểu, tham luận.
- Thẩm định hồ sơ (CCN, ATTP, VLNCN, hoá chất, rượu, xăng dầu, khoáng sản, đầu tư...).
- Rà soát, góp ý dự thảo văn bản trong hoặc ngoài Sở.
- Tham gia ý kiến vào dự thảo Nghị quyết HĐND, Quyết định QPPL UBND.
- **Nhận PDF văn bản hành chính** cần dẫn chiếu chính xác số/ngày (kết hợp với skill `vbhc-pdf-reader-vn`).

## 5 nhóm sai lầm và quy trình phòng tránh

### Nhóm A — Bịa/sai nội dung pháp lý

**Sai lầm đã xảy ra:**

- Bịa "Quyết định 1099/QĐ-UBND" trong bài phát biểu Chủ tịch UBND tỉnh (báo chí chỉ đưa tin có QĐ phê duyệt 431 danh mục dự án, không nêu số) — đã được Bạn phát hiện và ghi vào memory rule.
- Trích dẫn sai Điều 5 NĐ 105/2017/NĐ-CP (thực ra là Điều 8) và tự thêm điều kiện "trung cấp/đại học chuyên ngành hóa thực phẩm, kỹ thuật thực phẩm, sinh học" — điều luật không có nội dung này.
- Suy diễn quy định "chứng minh số dư tiền mặt/tiền gửi bắt buộc theo điểm b Khoản 1 Điều 5 NĐ 96/2024" — điều khoản đó chỉ quy định tỷ lệ vay/VCSH, không quy định gì về sao kê tiền gửi.
- Tính sai mức VCSH tối thiểu cho CCN ≥ 20 ha (đúng là 15%, đã khẳng định nhầm Cương Lĩnh sai khi họ viện dẫn đúng).

**Quy trình bắt buộc trước khi viện dẫn pháp luật:**

1. **Không bao giờ điền số/ngày văn bản từ trí nhớ.** Phải có nguồn cụ thể (file Bạn cung cấp, kết quả tra cứu chính thống thuvienphapluat.vn / vbpl.vn / cơ sở dữ liệu quốc gia về VBPL).
2. **Khi nguồn không có số/ngày**: viết chung "Quyết định của UBND tỉnh ban hành tháng X năm Y" — KHÔNG tự điền số. Ghi rõ trong phụ lục/cuối báo cáo: "đề nghị Bạn xác minh số/ngày trước khi sử dụng".
3. **Khi viện dẫn điều/khoản**: phải tra cứu văn bản gốc trước khi viết. Không được mô tả nội dung điều khoản từ trí nhớ. Nếu chưa tra được, ghi rõ "[cần xác minh điều/khoản cụ thể]".
4. **Khi tính toán theo công thức trong luật** (tỷ lệ VCSH, dư nợ vay, suất đầu tư...): viết rõ công thức, đối chiếu cả 2 chiều (ví dụ tỷ lệ vay tối đa và tỷ lệ VCSH tối thiểu phải khớp).
5. **Tuyệt đối không tự thêm điều kiện** "phù hợp chuyên ngành", "trung cấp trở lên", "có chứng chỉ X" nếu luật không nói. Luật quy định gì thì viết đúng vậy, không "diễn giải" thành điều kiện cứng hơn.

### Nhóm B — Tự suy diễn thêm nhiệm vụ ngoài văn bản chỉ đạo

**Sai lầm đã xảy ra:**

- Vụ Công văn 3861/UBND-NC ngày 15/5/2026 về bảo vệ ĐVHD: tự đề xuất "ban hành Quyết định của Sở Công Thương về việc cử thành viên tham gia Ban Chỉ đạo, Tổ công tác liên ngành" — văn bản UBND không yêu cầu việc này (mục 5 giao Sở NN&MT chủ trì; BCĐ tỉnh do Chủ tịch UBND tỉnh ban hành QĐ thành lập, Sở không có thẩm quyền tự ban hành QĐ cử thành viên).
- Ban đầu kết luận sai "Sở Công Thương không có thẩm quyền thẩm định dự án LTT" — thực ra SCT cấp tỉnh là Cơ quan chuyên môn về xây dựng đối với công trình công nghiệp hoá chất.

**Quy trình bắt buộc khi tham mưu triển khai văn bản chỉ đạo cấp trên:**

1. **Đọc kỹ phần "yêu cầu/giao nhiệm vụ" của văn bản nguồn**, gạch chân từng câu giao việc cụ thể. Phân loại:
   - Nhiệm vụ giao đích danh cho cơ quan mình.
   - Nhiệm vụ giao cho cơ quan khác (chỉ phối hợp, không chủ động).
   - Nhiệm vụ chung cho nhiều cơ quan.
2. **Quy tắc 1-1-1**: Mỗi nhiệm vụ Claude đề xuất Sở thực hiện phải truy ngược được về:
   - 1 câu trong văn bản chỉ đạo cấp trên, HOẶC
   - 1 điều khoản pháp luật quy định trách nhiệm của Sở, HOẶC
   - 1 chức năng đã ghi trong Quyết định quy định chức năng, nhiệm vụ, quyền hạn của Sở.
   Không có 1 trong 3 căn cứ này → KHÔNG đề xuất.
3. **Kiểm tra thẩm quyền ban hành văn bản:**
   - Ban Chỉ đạo, Tổ công tác cấp tỉnh: do Chủ tịch UBND tỉnh ban hành QĐ thành lập. Sở chỉ **đề xuất nhân sự bằng công văn**, không ban hành QĐ cử thành viên.
   - QĐ điều động, bổ nhiệm cán bộ thuộc Sở: Giám đốc Sở có thẩm quyền với cấp Trưởng/Phó phòng và tương đương, công chức không giữ chức vụ.
   - VBQPPL: thuộc thẩm quyền HĐND, UBND cấp tỉnh — Sở chỉ tham mưu, không tự ban hành.
4. **Khi không chắc văn bản có yêu cầu hay không**: dừng, hỏi lại Bạn thay vì tự thêm. Câu hỏi mẫu: *"Trong văn bản này, tôi không thấy nội dung yêu cầu X — Bạn có nhận được chỉ đạo bổ sung qua kênh khác không?"*

### Nhóm C — Dùng từ suy đoán trong văn bản hành chính

**Sai lầm đã xảy ra:**

- Vụ biên bản CCN Bản Phụng: dùng "lưu lượng nước thải dự kiến gần như chắc chắn sẽ thuộc ngưỡng phải quan trắc tự động" — Bạn nhắc: trong văn bản hành chính "không bao giờ 'dự kiến' và 'gần như'".

**Quy tắc:**

Văn bản hành chính chỉ có 3 trạng thái nội dung:
- **Khẳng định**: phải dẫn được căn cứ (điều, khoản, mục cụ thể).
- **Yêu cầu/đề nghị**: nêu rõ căn cứ pháp lý.
- **Bảo lưu/chưa kết luận**: ghi rõ "đề nghị Bạn xác minh", "cần làm rõ thêm", "thuộc thẩm quyền của cơ quan X" — KHÔNG dùng từ suy đoán.

**Danh sách từ/cụm từ CẤM trong văn bản hành chính trình ký Lãnh đạo:**

- "dự kiến" (trừ khi nói về tiến độ tương lai trong kế hoạch)
- "gần như", "gần như chắc chắn", "có vẻ", "có lẽ"
- "có thể" (khi dùng để suy đoán; được dùng khi nêu lựa chọn cho cơ quan có thẩm quyền)
- "khả năng cao", "nhiều khả năng"
- "ước tính", "khoảng" (trừ khi có cơ sở tính toán cụ thể)
- "đa số", "phần lớn" (không có số liệu)
- "theo tôi", "tôi nghĩ", "tôi cho rằng"

Khi cần nêu đánh giá mang tính dự báo, dùng cấu trúc: *"Căn cứ [số liệu/quy định cụ thể], [nhận định]; đề nghị cơ quan có thẩm quyền xem xét, quyết định."*

### Nhóm D — Dùng văn bản pháp luật đã hết hiệu lực

**Sai lầm đã xảy ra:**

- Phải Bạn nhắc mới biết Luật Đầu tư số 143/2025/QH15 (hiệu lực 01/3/2026) đã thay thế Luật Đầu tư 2020.
- Đã dẫn Nghị định 68/2017/NĐ-CP và NĐ 66/2020/NĐ-CP cho CCN trong khi đã có NĐ 32/2024/NĐ-CP thay thế.
- Đã dẫn Thông tư 28/2020/TT-BCT đã bị bãi bỏ bởi Thông tư 14/2024/TT-BCT.
- Đã dẫn Luật Hóa chất 2007 trong khi Luật Hóa chất 69/2025/QH15 hiệu lực 01/01/2026.

**Quy trình bắt buộc:**

1. **Bất kỳ Luật/Nghị định/Thông tư nào ban hành trước năm 2024**: phải tra cứu trạng thái hiệu lực trước khi viện dẫn. Dùng từ khoá: "[tên VB] còn hiệu lực không", "[tên VB] thay thế".
2. **Danh sách VB đã thay thế phổ biến trong lĩnh vực ngành Công Thương** (cập nhật định kỳ):

| VB cũ (KHÔNG dùng) | VB mới hiện hành |
|---|---|
| Luật Đầu tư 61/2020/QH14 | Luật Đầu tư 143/2025/QH15 (HL 01/3/2026) |
| Luật Hóa chất 2007 | Luật Hóa chất 69/2025/QH15 (HL 01/01/2026) |
| Luật ATTP 2010 (đang sửa) | đang sửa đổi, cần kiểm tra cập nhật |
| NĐ 68/2017/NĐ-CP + NĐ 66/2020/NĐ-CP (CCN) | NĐ 32/2024/NĐ-CP |
| TT 28/2020/TT-BCT (CCN) | TT 14/2024/TT-BCT |
| Luật QLBVCT số 14/2017 (VLNCN) | Luật 42/2024/QH15 |
| QĐ 1369/2020/QĐ-TTg (BMNN CT) | QĐ 476/QĐ-TTg ngày 25/3/2026 |

3. **Khi viện dẫn văn bản còn hiệu lực nhưng đã được sửa đổi/bổ sung**: bắt buộc ghi đầy đủ. Ví dụ: *"Nghị định số 31/2021/NĐ-CP (được sửa đổi, bổ sung bởi Nghị định số 239/2025/NĐ-CP)"*.

4. **Đặc biệt với các lĩnh vực thường xuyên thay đổi văn bản**: hóa chất, đầu tư, đất đai, môi trường, xây dựng, đấu thầu — luôn search trước khi viết.

### Nhóm E — Tin context window đối với PDF có header 2 cột

**Sai lầm đã xảy ra:**

- **Vụ 1 — CV 3861/UBND-NC ngày 15/5/2026** (UBND tỉnh Lào Cai, về bảo vệ ĐVHD): context window của Claude nạp PDF với "Số: /UBND-NC" và "ngày tháng 5 năm 2026" (trống). Claude tin theo context, soạn văn bản triển khai với các trường bỏ trống yêu cầu Bạn điền sau, trong khi file scan đã có đầy đủ số/ngày.
- **Vụ 2 — CV 3954/UBND-VX ngày 17/5/2026** (UBND tỉnh Lào Cai, về tham gia ý kiến Đề án ATTP của Bộ Y tế): mặc dù đã có sẵn skill `vbhc-pdf-reader-vn` được xây dựng từ vụ 1, Claude vẫn lặp lại sai lầm — không tự chạy skill, soạn công văn với chỗ trống "Văn bản số ....../UBND-VX ngày .../5/2026". Bạn phải nhắc "Cách nào để khắc phục việc bạn không đọc được số văn bản từ file pdf?" thì Claude mới chạy skill và lấy được số/ngày chính xác. Vụ này nghiêm trọng hơn vụ 1 vì đã có biện pháp phòng vệ nhưng Claude bỏ qua.

**Nguyên nhân kỹ thuật:**

Văn bản hành chính VN có layout 2 cột ở phần đầu — text-box độc lập cho số văn bản và ngày tháng. Đường ống xử lý PDF nạp tự động vào context window thường:

- Bỏ trống các text-box độc lập (số, ngày, người ký).
- Nối các dòng theo thứ tự từ trên xuống mà bỏ mất thông tin cột phải.
- Trả về "Số: /UBND-..." hoặc "ngày tháng ... năm 20..." khi text-box trống ở phía Claude nhìn thấy.

Đây **KHÔNG phải lỗi của file gốc** — file scan đã có đầy đủ thông tin. Đây là lỗi pipeline phía Claude.

**Quy trình bắt buộc:**

1. **Mọi khi nhận PDF có dấu hiệu là VBHC Việt Nam** (tên file chứa CV/QĐ/TTr/BC/KH/NQ/NĐ/TT/UBND/BYT/BCT/BNN/SCT/STC/SNN/SXD..., hoặc dòng đầu context có "ỦY BAN NHÂN DÂN", "BỘ ...", "SỞ ...", "HỘI ĐỒNG NHÂN DÂN", "CHÍNH PHỦ"): **DỪNG mọi thao tác khác**, chạy ngay:

   ```bash
   python3 /mnt/skills/user/vbhc-pdf-reader-vn/scripts/extract_metadata.py "<đường dẫn>"
   ```

2. **Quy tắc tuyệt đối**: KHÔNG bao giờ tin số văn bản/ngày tháng đọc từ context window khi nguồn là PDF. Luôn xác minh bằng skill `vbhc-pdf-reader-vn`.

3. **Khi context window đã có đủ số/ngày**: vẫn nên chạy skill để đối chiếu — chi phí ~2 giây, lợi ích là không phải sửa lại văn bản trình ký.

4. **Khi không có file gốc trên disk** (chỉ có ảnh chụp hoặc dán text): ghi rõ "đề nghị Bạn xác minh số/ngày trước khi ký" và liệt kê các trường nghi ngờ.

5. **Liên kết với Nhóm A**: nếu skill không chạy được (file scan không OCR được), áp dụng Nhóm A — không bịa, ghi chú cần xác minh.

**Tự kiểm tra**: nếu Claude đang viết "Văn bản số .../UBND-..." hoặc "ngày .../5/2026" với dấu chấm lửng/khoảng trống trong văn bản trình ký mà nguồn là PDF Bạn đã gửi, đó là dấu hiệu Claude đã bỏ qua skill `vbhc-pdf-reader-vn`. **Dừng lại, chạy skill, điền chính xác — không soạn tiếp.**

**Đặc biệt nguy hiểm**: việc bỏ qua skill này đã xảy ra 2 lần và lần thứ 2 vẫn xảy ra dù đã có biện pháp phòng vệ. Đây là sai lầm có xu hướng tự lặp lại — Claude phải đặc biệt cảnh giác.

## Quy trình tổng hợp trước khi trình tham mưu

Trước khi giao văn bản cho Bạn, Claude tự thực hiện checklist sau:

```
☐ Mọi số/ngày văn bản đều có nguồn cụ thể (không bịa)                              [Nhóm A]
☐ Mọi điều khoản pháp luật đã được tra cứu, không trích từ trí nhớ                 [Nhóm A]
☐ Mọi nhiệm vụ đề xuất truy ngược được về văn bản chỉ đạo, pháp luật, chức năng Sở [Nhóm B]
☐ Không có từ suy đoán ("dự kiến", "gần như", "có thể") trong phần khẳng định       [Nhóm C]
☐ Mọi VBQPPL viện dẫn đã kiểm tra còn hiệu lực                                     [Nhóm D]
☐ Nếu nguồn là PDF VBHC, đã chạy vbhc-pdf-reader-vn xác minh số/ngày từ file gốc   [Nhóm E]
☐ Đã ghi rõ phần nào "cần Bạn xác minh trước khi ký"
```

Nếu có 1 ô không tick được → BÁO CÁO LẠI VỚI BẠN, không tự giải quyết bằng cách bịa hoặc suy đoán.

## Script kiểm tra tự động

Sau khi soạn xong file .docx, chạy:

```bash
python /mnt/skills/user/anti-error-sct-vn/scripts/check_document.py <file.docx>
```

Script này dò các pattern rủi ro: từ suy đoán, số văn bản đáng nghi (số quá lớn/quá nhỏ), văn bản đã hết hiệu lực được liệt kê trong danh mục đen, ô số/ngày văn bản bị để trống (Nhóm E), và in cảnh báo trước khi trình ký.

## Khi Claude phát hiện chính mình sắp mắc lỗi

Nếu trong quá trình soạn thảo, Claude nhận ra:
- *"Tôi đang đoán số văn bản này"* → dừng, viết chung và ghi chú xác minh. [Nhóm A]
- *"Điều khoản này tôi không nhớ rõ"* → dừng, tra cứu, hoặc ghi "[cần xác minh]". [Nhóm A]
- *"Tôi đang đề xuất nhiệm vụ này nhưng văn bản chỉ đạo không nói rõ"* → dừng, hỏi Bạn. [Nhóm B]
- *"Tôi muốn dùng từ 'gần như'"* → đổi sang cấu trúc dẫn chứng cụ thể hoặc bảo lưu. [Nhóm C]
- *"Văn bản này ban hành trước 2024, tôi nhớ là vẫn còn hiệu lực"* → tra cứu trước khi dùng. [Nhóm D]
- ***"Tôi đang điền '...' hoặc khoảng trống cho số/ngày văn bản nguồn là PDF Bạn gửi"*** → **dừng ngay**, chạy `vbhc-pdf-reader-vn` để trích đúng từ file gốc. **Không bao giờ tin context window đối với layout 2 cột.** [Nhóm E]

Đây là lúc skill này có giá trị nhất — không phải để sửa lỗi sau khi đã sai, mà để bắt được sai lầm **ngay khi đang hình thành**.

## Liên kết với các skill khác

- **vbhc-pdf-reader-vn**: skill chuyên trích xuất metadata từ PDF VBHC — là tuyến phòng vệ thứ nhất chống Nhóm E. Skill anti-error này là tuyến phòng vệ thứ hai (checklist tổng hợp).
- **vbhc-vn**: khi soạn văn bản đầu ra, dùng kết quả Nhóm A (số/ngày đã xác minh) và Nhóm E (số/ngày từ skill PDF reader) để điền chính xác.
- **sct-laocai-org-vn**: tra cứu phòng chủ trì khi áp dụng Nhóm B (kiểm tra thẩm quyền).
- **kcn-ccn-vn / pccc-sct-vn**: áp dụng Nhóm D với danh mục VB đã thay thế trong từng lĩnh vực.
