---
name: bpb-sct-vn
description: >-
  Chuyên gia soạn BÀI PHÁT BIỂU / THAM LUẬN cho Giám đốc Sở Công Thương tỉnh Lào
  Cai theo phong cách đã duyệt. Dùng khi soạn/biên tập: phát biểu tham luận tại hội
  nghị BCH Đảng bộ tỉnh, Tỉnh ủy, HĐND, UBND tỉnh; hội nghị giao ban - giao kế
  hoạch, tổng kết, triển khai nghị quyết; phát biểu khai mạc/bế mạc/chỉ đạo/chào
  mừng; diễn văn kỷ niệm; hoặc nội dung phỏng vấn, bài viết ký tên Giám đốc Sở.
  Skill nắm kết cấu chuẩn (kính thưa phân tầng → mở đầu gắn nghị quyết → các nhóm
  nhiệm vụ → tín hiệu cơ hội → cam kết → cảm ơn), giọng văn nói chính trị - trang
  trọng, ngân hàng câu từ, quy tắc "bản duyệt" (điền đủ số liệu thật, bỏ chuỗi xin
  ý kiến, cấp Sở không kiến nghị Ban Thường vụ) và định dạng docx riêng (Times New
  Roman 15pt). Trigger: "bài phát biểu", "phát biểu tham luận", "tham luận", "diễn
  văn", "phát biểu khai mạc/bế mạc/chỉ đạo", "phát biểu cho Giám đốc/lãnh đạo Sở",
  "BPB", "kính thưa hội nghị", hội nghị giao ban/giao KH/BCH/triển khai nghị quyết.
  Liên kết vbhc-vn (render/QA docx) và sct-laocai-org-vn.
---

# Soạn Bài phát biểu Giám đốc Sở Công Thương Lào Cai

Skill này giúp soạn **bài phát biểu / tham luận** cho lãnh đạo Sở Công Thương tỉnh
Lào Cai (chủ yếu là Giám đốc Sở) đúng phong cách đã được duyệt. Đây là văn **nói**
để đọc trước hội nghị — khác hẳn văn bản hành chính (VBHC): không có Quốc hiệu, số
ký hiệu, nơi nhận; câu chữ có nhịp điệu, giàu số liệu, mang màu sắc chính trị và
quyết tâm hành động.

> Phân biệt với plugin **vbhc-vn**: vbhc-vn lo *thể thức VBHC* (công văn, tờ trình,
> báo cáo…). Skill này lo *nội dung + văn phong + kết cấu bài phát biểu*, chỉ mượn
> vbhc-vn ở khâu render/QA file docx cuối cùng (xem mục 6).

---

## 1. Khi nào dùng skill này

Kích hoạt khi người dùng yêu cầu soạn/biên tập bất kỳ dạng nào sau đây:

- Phát biểu **tham luận** tại hội nghị (BCH Đảng bộ tỉnh, Tỉnh ủy, HĐND, UBND tỉnh…).
- Phát biểu tại **hội nghị giao ban, giao kế hoạch, tổng kết, triển khai nghị quyết**.
- Phát biểu **khai mạc / bế mạc / chỉ đạo / chào mừng**, diễn văn **kỷ niệm**.
- Nội dung **trả lời phỏng vấn** hoặc **bài viết** ký tên Giám đốc Sở (cùng giọng văn).

Nếu người dùng đưa PDF/văn bản đến (nghị quyết, kế hoạch, giấy mời) làm căn cứ cho
bài phát biểu → chạy `vbhc-pdf-reader-vn` / `extract_metadata.py` để lấy đúng số,
ngày, tên văn bản trước khi trích dẫn. **Tuyệt đối không bịa số/ngày văn bản.**

---

## 2. Quy trình soạn (4 bước)

**Bước 1 — Xác định "5 thông số" của bài.** Hỏi (hoặc suy ra từ ngữ cảnh) trước khi
viết. Nếu thiếu thông số then chốt thì hỏi gọn 1 câu, đừng hỏi tràn lan:
1. **Hội nghị nào, ai chủ trì, thành phần dự?** → quyết định lời kính thưa (mục 4).
2. **Chủ đề / nhiệm vụ trọng tâm** cần trình bày.
3. **Thời lượng** mong muốn → quyết định độ dài (mục 3, "Hai biến thể").
4. **Số liệu, dự án, văn bản căn cứ** người dùng cung cấp; nếu chưa cung cấp, lấy
   nền từ kho số liệu KT-XH mới nhất trong `references/` (hiện là
   `so-lieu-ktxh-thang-7-2026.md`) — số người dùng đưa luôn thắng số trong kho.
5. **Ai đọc** — Giám đốc Sở hay Phó Giám đốc (đổi cách xưng "thay mặt…").

**Bước 2 — Dựng khung theo kết cấu chuẩn** (mục 3). Điền các mảng nội dung vào khung.

**Bước 3 — Viết theo giọng đã duyệt** (mục 5 + ngân hàng câu từ `references/ngan-hang-cau-tu.md`).
Kiểm lại bằng **checklist bản duyệt** (mục 5B) — đây là bước quan trọng nhất, phân
biệt bản nháp non và bản GĐ duyệt.

**Bước 4 — Xuất file .docx** đúng định dạng bài phát biểu (mục 6), render soi ảnh
từng trang bằng QA của vbhc-vn trước khi giao. Đặt tên file
`YYYY.MM.DD. [Tên đầy đủ có dấu].docx`.

---

## 3. Kết cấu chuẩn của bài phát biểu

Mọi bài phát biểu tham luận đều đi theo "cung" 6 nhịp sau (đọc kỹ ví dụ có chú giải
trong `references/cau-truc-va-vi-du.md`):

1. **TIÊU ĐỀ** — căn giữa, in đậm, 15pt. Mẫu: `BÀI PHÁT BIỂU THAM LUẬN` (dòng 1) +
   chủ đề (dòng 2-3). Nếu là hội nghị BCH có thể thêm dòng `Chủ đề: …`.

2. **LỜI KÍNH THƯA** — phân tầng theo cấp hội nghị (mục 4). Dòng đầu "Kính thưa:"
   in đậm; các dòng đối tượng in nghiêng, thụt lề trái 1.27cm.

3. **MỞ ĐẦU (1–2 đoạn)** — công thức:
   - Câu chào - dẫn nhập: *"Hôm nay, tại Hội nghị quan trọng này, thay mặt Sở Công
     Thương, tôi xin phép được trình bày tham luận về: …"*
   - Đặt bối cảnh & tầm vóc: gắn với **Nghị quyết Đại hội Đảng bộ tỉnh**, mục tiêu
     **GRDP > 10%**, XNK **6,1 tỷ USD**, định vị Lào Cai "cực tăng trưởng, trung tâm
     kết nối giao thương chiến lược".
   - Nêu **số nhóm nhiệm vụ/giải pháp** sẽ trình bày: *"…xin đề xuất 06 nhóm nhiệm
     vụ trọng tâm như sau:"*
   - Chèn `Kính thưa Hội nghị!` (in đậm + nghiêng) làm dấu ngắt sang thân bài.

4. **THÂN BÀI — các nhóm nhiệm vụ/giải pháp.** Đây là phần dài nhất. Quy tắc:
   - Đánh số nhẹ kiểu **văn nói**: `1.`, `2.`, `3.` hoặc `I - NHÓM THỨ NHẤT:` /
     `II - NHÓM THỨ HAI:` hoặc `* Nhóm 1:`. **Không** dùng cấu trúc pháp lý kiểu
     Điều/Khoản/Điểm hay a) b) c) lồng nhiều tầng.
   - Trong mỗi nhóm dùng: gạch đầu dòng `-`, ký hiệu `*`, `+`, và `(i)(ii)(iii)` cho
     giải pháp; hoặc `Một là,` `Hai là,` `Ba là,` cho ý song song. **In đậm cụm dẫn
     đầu** mỗi ý ("Một là,", "Về nguyên liệu sản xuất:", tên đề mục).
   - Mỗi luận điểm phải có **số liệu / tên dự án / văn bản dẫn chiếu cụ thể** — không
     nói chung chung (xem checklist mục 5B).
   - Đề nghị/kiến nghị đặt ngay dưới nhóm liên quan: *"Đề nghị UBND tỉnh…"*, *"Đề
     nghị các xã, phường…"*, hoặc mục cố định *"* Đề xuất, kiến nghị (nếu có):"*.

5. **TÍN HIỆU – CƠ HỘI (1 đoạn, tuỳ chọn nhưng nên có ở bài giao KH/tổng kết).**
   Mở bằng `Kính thưa Hội nghị!` rồi liệt kê thời cơ: quy hoạch tỉnh, kế hoạch đầu
   tư công, hạ tầng giao thông - cửa khẩu, **giá sản phẩm chủ lực đang tốt** (vàng,
   đồng, quặng sắt, phốt pho vàng, DAP — nêu con số so sánh), sự vào cuộc của cả hệ
   thống chính trị. Có thể chốt bằng thành ngữ: *"Thiên thời, địa lợi, nhân hòa đã
   hội tụ đủ."*

6. **KẾT BÀI.** Gồm 3 lớp:
   - **Cam kết:** *"Chúng tôi cam kết sẽ nỗ lực hết mình, với tinh thần 'Kỷ cương,
     hành động, trách nhiệm, sáng tạo, hiệu quả'…"*
   - **Mong quan tâm/phối hợp** (đúng cấp — xem quy tắc R4 mục 5A).
   - **Cảm ơn:** *"Xin trân trọng cảm ơn!"* (có thể thêm lời chúc nếu dịp lễ, Tết).

**Hai biến thể độ dài:**
- **Bản đầy đủ (tham luận):** trình bày kỹ nhiều nhóm nhiệm vụ, số liệu dày — dùng
  cho hội nghị lớn, phát biểu chính. Có thể 3–5 trang.
- **Bản rút gọn (phát biểu ~3–4 phút / ~2 trang):** giữ nguyên cung 6 nhịp nhưng mỗi
  nhóm chỉ 2–4 ý cô đọng — dùng cho phát biểu tại chỗ, hội nghị nhiều đại biểu. Khi
  người dùng nói "ngắn gọn", "phát biểu tại chỗ", "vài phút" → chọn biến thể này.

---

## 4. Ma trận LỜI KÍNH THƯA theo cấp hội nghị

Chọn đúng bộ kính thưa (chi tiết + mẫu đầy đủ trong `references/cau-truc-va-vi-du.md`):

| Loại hội nghị | Lời kính thưa |
|---|---|
| **BCH Đảng bộ tỉnh / Tỉnh ủy** | Kính thưa: Đồng chí Bí thư Tỉnh ủy, / Các đồng chí Thường trực Tỉnh ủy, Ủy viên Ban Thường vụ Tỉnh ủy, / Thưa toàn thể các đồng chí Ủy viên Ban Chấp hành Đảng bộ tỉnh! |
| **Hội nghị do Chủ tịch UBND tỉnh chủ trì** | Kính thưa đồng chí Chủ tịch UBND tỉnh chủ trì hội nghị / Kính thưa các đồng chí lãnh đạo tỉnh, / Thưa toàn thể Hội nghị! |
| **Hội nghị chung (giao KH, triển khai NQ, tổng kết)** | Kính thưa các đồng chí lãnh đạo tỉnh, / Kính thưa các vị đại biểu khách quý, / Thưa toàn thể Hội nghị! |
| **Lễ kỷ niệm / có khách TW, quốc tế** | Bổ sung dòng khách mời cấp cao lên trên; giữ "Thưa toàn thể…" ở cuối. |

Nguyên tắc: xếp đối tượng **từ cao xuống thấp**; dòng cuối luôn là "Thưa toàn thể
Hội nghị!" (hoặc "…các đồng chí!"). Xưng danh chức vụ đúng, không viết tắt tên cơ quan.

---

## 5. Giọng văn & nguyên tắc vàng

### 5A. Nguyên tắc bắt buộc (rút ra từ các bản GĐ đã duyệt)

- **R1 — Văn nói, không phải VBHC.** Câu ngắn, dứt khoát, có nhịp. Dùng "Một là/Hai
  là/Ba là", "Thứ nhất/Thứ hai/Thứ ba", "Trước hết". **In đậm cụm dẫn đầu** mỗi ý.
- **R2 — Cụ thể, không hàn lâm.** Mọi khẳng định phải neo vào **số liệu / tên dự án
  / tên xã, phường / văn bản (số + ngày)**. Đây là yêu cầu nhất quán của Giám đốc:
  "nêu cụ thể, không hàn lâm". Tránh câu khẩu hiệu rỗng không kèm dữ liệu.
- **R3 — Quyết định đã ban hành thì chỉ nêu quyết định**, không thuật lại cả chuỗi
  xin ý kiến/trình duyệt dẫn tới nó (đó là chi tiết của bản nháp, cắt khi hoàn thiện).
- **R4 — Đúng cấp khi đề nghị.** Cấp Sở **không "kiến nghị"** Ban Thường vụ / Thường
  trực Tỉnh ủy trong bài. Với Tỉnh ủy dùng: *"rất mong nhận được sự quan tâm lãnh
  đạo, chỉ đạo…"*. "Đề xuất/kiến nghị" chỉ dành cho UBND tỉnh, sở ngành, địa phương
  cấp dưới.
- **R5 — Nhất quán viết tắt & đơn vị.** GRDP, IIP, XNK, GPMB, KCN, CCN, NSNN, TĐC,
  TTHC, TMĐT, CK (cùng kỳ); tỷ USD, tỷ đồng, ha, MW, tấn, %. Lần đầu nên mở ngoặc
  chú thích viết tắt lạ.
- **R6 — Địa danh Lào Cai mới.** Sau hợp nhất 01/7/2025, mọi địa danh (kể cả Yên Bái
  cũ) đều ghi thuộc **tỉnh Lào Cai**; không còn cấp huyện, dùng xã/phường.
- **R7 — Không bịa.** Số liệu, tên/số/ngày văn bản chưa xác minh thì để trống có dấu
  hiệu `……` và nhắc người dùng bổ sung, **không** điền số giả.

### 5B. Checklist "bản duyệt" (chạy trước khi giao)

So sánh bản nháp non ↔ bản GĐ duyệt cho thấy bản duyệt luôn:
- [ ] **Đã điền hết placeholder** `……`, `?`, `(hỏi…)`, `(cụ thể ntn?)` — hoặc gắn cờ
      rõ ràng để người dùng bổ sung, không để lọt câu hỏi biên tập vào bản trình.
- [ ] **Mỗi nhóm nhiệm vụ có ít nhất 1 số liệu/mốc tiến độ cụ thể** (theo quý/năm,
      công suất MW, giá trị tỷ đồng, tên dự án…).
- [ ] **Trình tự thủ tục (nếu có) viết dạng mũi tên** `A => B => C` cho dễ theo dõi.
- [ ] **Đã cắt chuỗi trình/xin ý kiến rườm rà** với các quyết định đã ban hành (R3).
- [ ] **Đề nghị đúng cấp** (R4), không "kiến nghị" cấp uỷ.
- [ ] **Lời kính thưa khớp đúng thành phần hội nghị** (mục 4).
- [ ] **Kết bài đủ 3 lớp** (cam kết → mong phối hợp → cảm ơn).
- [ ] Đọc thử thành tiếng: câu có trôi, có nhịp không? Bỏ câu quá dài/lủng củng.

---

## 6. Định dạng file .docx (riêng cho bài phát biểu)

Bài phát biểu **KHÔNG** dùng thể thức VBHC (không Quốc hiệu/số/nơi nhận). Thông số:

- **Font:** Times New Roman, **15pt** toàn bài (to hơn VBHC 14pt để đọc trên bục).
- **Lề:** trên 1.5 cm · dưới 1.25 cm · trái 3.0 cm · phải 1.25 cm · khổ A4.
- **Tiêu đề:** căn giữa (CENTER), **in đậm**.
- **Lời kính thưa:** dòng "Kính thưa:" in đậm; các dòng đối tượng **in nghiêng**,
  thụt lề trái 1.27 cm.
- **Thân bài:** căn đều (JUSTIFY), thụt dòng đầu 1.27 cm, giãn dòng đơn (1.0),
  cách đoạn before/after 6pt.
- **Đề mục & cụm dẫn đầu:** in đậm. **`Kính thưa Hội nghị!`** in đậm + nghiêng.
  Các ý phụ `(1)(2)(3)` có thể in nghiêng.
- Tên file: `YYYY.MM.DD. [Tên đầy đủ có dấu].docx`.

Có 2 cách tạo file:
1. **Dùng script kèm skill:** `scripts/build_bpb.py` sinh khung .docx đúng định dạng
   trên từ một file nội dung; đọc `scripts/build_bpb.py` để biết cách gọi. Nhanh, ổn
   định cho đúng font 15pt/lề/đậm-nghiêng.
2. **Nhờ vbhc-vn render** nếu cần QA soi ảnh từng trang: soạn nội dung theo khung
   rồi chuyển sang bước QA `qa_all.py` của vbhc-vn (render 1 lần + ảnh ghép) để soát
   widow, khối chữ, in đậm/nghiêng trước khi giao.

Luôn **render soi ảnh từng trang** trước khi trình.

---

## 7. Người đọc & người ký (tra khi cần)

Mặc định bài phát biểu do **Giám đốc Sở Hoàng Chí Hiền** trình bày ("thay mặt Sở
Công Thương / thay mặt ngành Công Thương, tôi…"). Nếu Phó Giám đốc đọc, đổi cách
xưng cho phù hợp lĩnh vực phụ trách. Tra phân công lãnh đạo Sở ở skill
`sct-laocai-org-vn` khi không chắc ai phát biểu về lĩnh vực nào.

---

## 8. Tài liệu tham khảo trong skill

- `references/cau-truc-va-vi-du.md` — kết cấu chi tiết + **1 bài mẫu đầy đủ có chú
  giải** + các bộ lời kính thưa. Đọc khi cần bám sát mẫu thật.
- `references/ngan-hang-cau-tu.md` — **ngân hàng câu mở đầu, chuyển ý, đề nghị, tín
  hiệu-cơ hội, cam kết, kết bài, khẩu hiệu & từ vựng đặc trưng**. Đọc khi cần "chất
  giọng" đúng.
- `references/so-lieu-ktxh-thang-7-2026.md` — **kho số liệu KT-XH tháng 7 và 7
  tháng đầu năm 2026** (nguồn: BC 229-BC/TU ngày 27/7/2026 của Tỉnh ủy): GTSXCN,
  bán lẻ, XNK, thu NSNN, giải ngân, FDI, du lịch, khởi công CCN Phú Thịnh 3, Thông
  báo 381/TB-VPCP, nhiệm vụ tháng 8 (tiết kiệm 10% điện, bảo đảm nguyên liệu sản
  xuất). Mở khi soạn bài phát biểu trong tháng 8–9/2026 mà người dùng chưa đưa số
  liệu; số liệu người dùng cung cấp luôn được ưu tiên.
- `kho-bai-mau/` — **12 bài mẫu gốc** do Sở cung cấp (kèm `00-MUC-LUC.md` tra nhanh
  theo dịp; tên file đã chuẩn hoá không dấu). Ưu tiên **mở đúng mẫu gần nhất** với
  dịp đang soạn để bám thể thức/giọng (Chế độ B — sửa mẫu thật). File
  `bpb-bch-ktck-gd-duyet.docx` là bản GĐ đã duyệt — chuẩn cao nhất để đối chiếu.
- `scripts/build_bpb.py` — sinh file .docx đúng định dạng bài phát biểu.
