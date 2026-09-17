# 39. GATE TRẠNG THÁI HỒ SƠ — bắt buộc chạy trước khi soạn hoặc sửa văn bản gắn tên một CCN/KCN cụ thể

> Nguồn: vụ thật ngày 17/9/2026 (CCN Châu Quế). Người dùng phải trực tiếp nhận lỗi với Lãnh đạo Sở.
> Reference này là GATE, đứng trước mọi nghiệp vụ soạn thảo của plugin. Ref 32 trả lời câu hỏi
> "số liệu hiện trạng lấy ở đâu"; ref này trả lời câu hỏi khác: **"cụm này đang ở bước thủ tục nào,
> và văn bản sắp soạn có còn hợp lệ ở bước đó không"**.

---

## A. VỤ THẬT 17/9/2026 — CCN CHÂU QUẾ

- Người dùng gửi 02 file: Công văn **5348/SCT-CN ngày 28/8/2026** (mẫu, đề nghị Công an tỉnh cử cán bộ
  tham gia Hội đồng và Tổ giúp việc CCN Phú Thịnh 6 và CCN Xuân Ái) và một bản dự thảo cùng loại cho
  **CCN Châu Quế**, yêu cầu "sửa lại cho giống bản Xuân Ái".
- Claude sửa xong, giao file. Nội dung văn bản: đề nghị cử cán bộ **"để có cơ sở tham mưu UBND tỉnh
  thành lập Hội đồng và Tổ giúp việc"**.
- Thực tế: **CCN Châu Quế đã có Quyết định của UBND tỉnh thành lập Hội đồng đánh giá lựa chọn chủ đầu tư**.
  Bước mà văn bản đề nghị làm thì đã xong từ trước. Văn bản sai về bản chất, không phải sai câu chữ.
- Dấu hiệu đã nằm sẵn trong plugin mà Claude không tra: ref 17 ghi **Tờ trình 4299/SCT-TTr ngày 17/7/2026
  trình thành lập Hội đồng đánh giá lựa chọn CĐT CCN Châu Quế** — cách thời điểm soạn 02 tháng, trong khi
  Phú Thịnh 6 và Xuân Ái mới trình lập Hội đồng ngày 04/9/2026 (ref 30). Hai cụm **không cùng một bước**.
- Nguyên nhân gốc: lấy mẫu của cụm A áp cho cụm B mà không kiểm tra cụm B đang ở bước nào; coi hai file
  người dùng gửi là đủ dữ kiện, không tra trạng thái trong plugin, không hỏi người dùng.

**Bài học một câu: mẫu văn bản mượn được, trạng thái hồ sơ không mượn được.**

---

## B. GATE 4 BƯỚC (bắt buộc, chạy trước khi viết dòng đầu tiên)

**Bước 1 — Liệt kê tên cụm/khu.** Ghi ra mọi tên CCN/KCN xuất hiện trong yêu cầu, trong file đính kèm và
trong file mẫu. Phân biệt rõ đâu là **cụm đích** (văn bản sắp soạn nói về cụm nào) và đâu là **cụm mẫu**.

**Bước 2 — Tra trạng thái cụm đích:**

```bash
python3 <thư mục plugin kccn-sct-vn>/scripts/trang_thai_cum.py "Châu Quế"
```

Script quét toàn bộ `references/`, `vi-du-thuc-te/`, `checklists/`, in mọi dòng có tên cụm kèm số/ngày
văn bản, xếp theo bậc thủ tục ở mục C và kết luận **bậc cao nhất đã đạt**.

**Bước 3 — Đối chiếu bậc với loại văn bản sắp soạn:**

- Văn bản thuộc bậc **thấp hơn hoặc bằng** bậc đã đạt → **DỪNG**, không soạn. Xem bảng cấm ngược mục D,
  chọn đúng loại văn bản của bậc hiện tại rồi báo lại người dùng.
- Không tìm thấy dòng nào về cụm đích, hoặc dòng mới nhất cũ hơn kỳ cập nhật mới nhất (ref 32), hoặc
  không rõ Quyết định/kết quả của bậc kế tiếp đã có chưa → **DỪNG, hỏi người dùng** bằng câu ở mục E.
- Chỉ khi bậc của văn bản đúng **liền sau** bậc đã đạt mới được soạn.

**Bước 4 — Ghi giả định vào phần trao đổi (không đưa vào văn bản).** Một dòng: "Bản này soạn theo giả định
CCN X đang ở bậc N (căn cứ <số văn bản, ngày>); nếu đã có <văn bản bậc N+1> thì phải đổi hướng."
Người dùng đọc dòng đó là chặn được sai lầm ngay trước khi trình ký.

GATE này áp dụng cho **cả việc sửa file người dùng tải lên**. Người dùng đưa file không có nghĩa là trạng
thái trong file còn đúng: bản dự thảo có thể được soạn từ nhiều tuần trước, hoặc do bộ phận khác soạn.

---

## C. BẬC THANG THỦ TỤC — thành lập CCN và lựa chọn chủ đầu tư hạ tầng (thực tế Lào Cai)

Căn cứ Điều 10, 12, 13 NĐ 32/2024 (sửa đổi tại NĐ 303/2026 từ 15/9/2026), đối chiếu chuỗi văn bản thật của
Tân Nguyên, Mông Sơn, Yên Hợp 2 (ref 26, 27, 30).

| Bậc | Nội dung bước | Văn bản đặc trưng của bậc |
|---|---|---|
| 1 | Cụm nằm trong quy hoạch tỉnh và danh mục thu hút đầu tư | QĐ 525/QĐ-UBND; QĐ 1382/QĐ-UBND |
| 2 | UBND cấp xã thông báo công khai tiếp nhận hồ sơ | TB .../TB-UBND của xã, phường |
| 3 | Nhà đầu tư nộp Báo cáo đầu tư; xã lập hồ sơ, trình Sở | TTr .../TTr-UBND của xã |
| 4 | Sở lấy ý kiến sở, ngành về hồ sơ thành lập | CV .../SCT-CN xin ý kiến |
| 5 | Sở đề nghị các cơ quan **cử cán bộ**, rồi trình UBND tỉnh lập Hội đồng | CV .../SCT-CN cử cán bộ; TTr .../TTr-SCT |
| 6 | UBND tỉnh **thành lập Hội đồng + Tổ giúp việc** | QĐ .../QĐ-UBND (mẫu: QĐ 2736 Mông Sơn, QĐ 2549 Tân Nguyên) |
| 7 | Xin ý kiến thành viên Hội đồng, ban hành tiêu chí chấm điểm | CV .../SCT-CN; TTr .../TTr-SCT; **QĐ .../QĐ-HĐ** của Chủ tịch Hội đồng |
| 8 | Họp Hội đồng chấm điểm, báo cáo kết quả | GM .../GM-HĐ; biên bản, phiếu chấm; báo cáo kết quả |
| 9 | Sở thẩm định, trình UBND tỉnh quyết định thành lập cụm | BC .../BC-SCT + TTr .../TTr-SCT |
| 10 | UBND tỉnh ban hành **Quyết định thành lập CCN**, giao chủ đầu tư | QĐ .../QĐ-UBND |
| 11 | Sau thành lập: QHCT 1/500, đất đai, môi trường, khởi công | Chuỗi văn bản chuyên ngành, ref 08, 23 |

Cụm đang ở bậc nào thì chỉ soạn được văn bản của bậc đó hoặc bậc liền sau. Bậc 5 chính là bậc của vụ
Châu Quế; cụm đã ở bậc 6 nên văn bản bậc 5 không còn chỗ đứng.

---

## D. BẢNG CẤM NGƯỢC — đã có văn bản này thì không soạn văn bản kia

| Cụm đã có | CẤM soạn | Nếu vẫn cần xử lý thì soạn gì |
|---|---|---|
| QĐ thành lập Hội đồng, Tổ giúp việc (bậc 6) | Công văn đề nghị cử cán bộ "để có cơ sở tham mưu UBND tỉnh thành lập Hội đồng" | Công văn đề nghị cử lãnh đạo, cán bộ **thay thế** để trình UBND tỉnh **kiện toàn, sửa đổi** Quyết định đã ban hành — dẫn thẳng Quyết định đó, nêu lý do kiện toàn |
| QĐ tiêu chí chấm điểm của Chủ tịch Hội đồng (bậc 7) | Công văn xin ý kiến dự thảo tiêu chí | Tờ trình đề nghị ban hành Quyết định **thay thế** (mẫu Tân Nguyên: thay QĐ 2778/QĐ-HĐ, ref 27) |
| Báo cáo kết quả chấm điểm (bậc 8) | Văn bản đôn đốc nộp hồ sơ đăng ký làm chủ đầu tư | Báo cáo, tờ trình bậc 9 |
| QĐ thành lập CCN (bậc 10) | Tờ trình đề nghị thành lập cụm | Văn bản điều chỉnh, bổ sung Quyết định thành lập (ref 11) |
| Quyết định đã ban hành (mọi loại) | Nhắc lại tờ trình, báo cáo đã hình thành nên Quyết định đó | Dẫn thẳng Quyết định (quy ước người dùng chốt) |
| Hội đồng đã giải thể (vd Bản Phung, QĐ 3116/QĐ-UBND 27/8/2026) | Mọi văn bản coi Hội đồng còn hoạt động | Văn bản theo hướng kêu gọi đầu tư lại |

---

## E. CÂU HỎI CHUẨN KHI THIẾU DỮ KIỆN

Hỏi ngắn, hỏi đúng một việc, không hỏi vòng:

- "CCN X đã có Quyết định thành lập Hội đồng đánh giá lựa chọn chủ đầu tư chưa? Nếu có, cho tôi số và ngày."
- "Thành phần Hội đồng CCN X hiện đã là lãnh đạo (Phó Giám đốc) các sở, ngành theo chỉ đạo của
  đồng chí Phó Chủ tịch Thường trực UBND tỉnh chưa, hay còn là chuyên viên?"
- "Cụm X đã họp chấm điểm chưa? Có Báo cáo kết quả chưa?"

Không tự điền số, ngày của Quyết định đã ban hành. Không suy ra "chắc đã có" hoặc "chắc chưa có" từ mốc
thời gian.

---

## F. QUY TẮC MƯỢN MẪU TỪ CỤM KHÁC

1. Chỉ mượn **thể thức và văn phong**: bố cục, cách xưng hô, khối ký, nơi nhận, cách dẫn chỉ đạo.
2. Không mượn **tình huống**: câu mở đầu, lý do ban hành, mốc thời hạn, danh sách cơ quan nhận đều phải
   dựng lại theo hồ sơ của cụm đích.
3. Trước khi mượn, ghi ra hai bậc: cụm mẫu bậc mấy, cụm đích bậc mấy. Khác bậc → mẫu chỉ còn giá trị
   thể thức, phần thân phải viết mới.
4. Ngày tháng trên file mẫu không nói gì về cụm đích. Mẫu 28/8/2026 của Phú Thịnh 6 và Xuân Ái không
   chứng minh Châu Quế cùng tiến độ.
5. Mẫu do người dùng gửi vẫn phải qua GATE mục B. Người dùng gửi file là giao việc, không phải xác nhận
   trạng thái.

---

## G. LIÊN KẾT

- Ref 32 — nguồn số liệu hiện trạng, nhịp cập nhật 2 kỳ/tuần; GATE này dùng ref kỳ cập nhật mới nhất làm
  mốc đối chiếu độ mới.
- Ref 05 — trình tự, thời hạn thành lập CCN; ref 06, 27 — Hội đồng và tiêu chí chấm điểm; ref 11 — điều
  chỉnh, bãi bỏ Quyết định thành lập.
- Ref 17, 26, 30, 37 — chuỗi văn bản thật của từng cụm, là nguồn để script dò bậc.
- Plugin `vbhc-vn`, Nhóm M (trạng thái hồ sơ vụ việc) — bản rút gọn của GATE này cho mọi lĩnh vực, không
  riêng CCN/KCN.
