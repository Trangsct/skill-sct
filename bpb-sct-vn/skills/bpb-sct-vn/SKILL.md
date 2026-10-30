---
name: bpb-sct-vn
description: "BÀI PHÁT BIỂU, THAM LUẬN, DIỄN VĂN cho Giám đốc/lãnh đạo Sở Công Thương Lào Cai. Kích hoạt: 'bài phát biểu', 'tham luận', 'diễn văn', 'phát biểu khai mạc/bế mạc/chỉ đạo/chào mừng', 'BPB', 'kính thưa hội nghị'; hội nghị BCH Đảng bộ tỉnh, Tỉnh ủy, HĐND, UBND tỉnh; giao ban - giao kế hoạch, tổng kết, triển khai nghị quyết; diễn văn kỷ niệm; phỏng vấn, bài viết ký tên Giám đốc Sở. Kết cấu chuẩn đã duyệt: kính thưa phân tầng - mở đầu gắn nghị quyết - các nhóm nhiệm vụ - tín hiệu cơ hội - cam kết - cảm ơn; giọng văn nói chính trị; ngân hàng câu từ; quy tắc bản duyệt (điền đủ số liệu thật, bỏ chuỗi xin ý kiến, cấp Sở không kiến nghị Ban Thường vụ); định dạng docx riêng Times New Roman 15pt. Mẫu 28/10/2026 BCH Đảng bộ tỉnh về KCN, CCN: việc lớn đã làm trước, nêu vấn đề rồi giao việc, giọng ngang cấp, mốc theo ngày đọc (R8–R22). Mẫu 30/10/2026 đối ngoại PGĐ sang Ngọc Khê, Vân Nam: chiều chuyến đi, 2 trang, Hội chợ Việt – Trung (R23–R29); luôn kèm tin nhắn Zalo gửi lãnh đạo (R30). Liên kết vbhc-vn, sct-laocai-org-vn."
---

# Soạn Bài phát biểu Giám đốc Sở Công Thương Lào Cai

> **Tra văn bản gốc (Bạn chốt 09/10/2026, áp dụng mọi plugin):** đọc `van-ban-goc/00-DANH-MUC-CHUNG.md` và chạy `python3 scripts/tim_van_ban.py "<số hiệu hoặc cụm từ>"` TRƯỚC khi kết luận văn bản nào chưa có trong kho. Văn bản đã có trong danh mục thì phải mở toàn văn `.txt` cùng tên đặt cạnh bản gốc để trích; cấm trả lời "không có tài liệu", "chưa có trong gói", "không mở được toàn văn", "tra mạng khi cần nguyên văn". Khi Bạn gửi văn bản quy phạm pháp luật trong phiên: (a) đọc số, ngày, cơ quan, người ký bằng script (GATE), không đọc bằng mắt; (b) đặt tên `YYYY.MM.DD-SỐ.KÝ.HIỆU-Tên-trích-yếu-ngắn`, giữ nguyên định dạng gốc; (c) lưu vào `van-ban-goc/` của plugin chủ theo lĩnh vực, không nhân bản sang plugin khác; (d) sinh `.txt` bằng `scripts/trich_chu_van_ban_goc.py`; (e) chạy `scripts/build_so_cai_van_ban_goc.py` ở gốc kho để cập nhật danh mục; (f) cập nhật reference tóm tắt + CHANGELOG; (g) push, mở PR. Phiên không có quyền ghi kho thì nói ngay ở câu đầu và hướng dẫn Bạn dùng Hộp thư nạp kho `_inbox/` trên GitHub (`_inbox/README.md`, 6 bước), không được chỉ tóm tắt rồi bỏ qua tệp.

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
- Nội dung **trả lời phỏng vấn báo chí** hoặc **bài viết** ký tên Giám đốc Sở.
  ⚠️ Phỏng vấn báo chí là **thể loại riêng, KHÔNG áp khung bài phát biểu hội nghị**:
  bắt buộc đọc `references/tra-loi-phong-van-bao-chi.md` (11 quy tắc đúc kết từ bản
  duyệt của PGĐ Hoàng Văn Thuân 11/8/2026) và mở 2 mẫu duyệt
  `kho-bai-mau/phong-van-ttxvn-2026-08-11-*.docx` trước khi soạn. Luôn giao **sản
  phẩm kép**: bản đầy đủ + bản tóm tắt cầm tay.

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

**Bước 5 — Luôn giao kèm tin nhắn Zalo gửi lãnh đạo (R30, Bạn chốt 30/10/2026).** Mỗi lần giao file
bài phát biểu, tham luận, phỏng vấn (bản đầu hay bản sửa), cuối câu trả lời có đoạn "Tin nhắn gửi
anh …:" để Bạn chép sang Zalo: gõ thẳng, không markdown, không gạch đầu dòng tự động, tối đa một màn
hình điện thoại; "Dạ, em gửi anh…" khi nhắn riêng lãnh đạo; nêu đã sửa gì theo đúng ý lãnh đạo, độ dài,
chỗ số ước/bôi tím, một câu hỏi nếu còn thiếu dữ kiện; gửi hai file một lúc thì nói rõ file nào là bản
nào. Tin thật: `references/bpb-doi-ngoai-lam-viec-dia-phuong-trung-quoc-30-10-2026.md` mục E.

---

## 2A. Dàn ý trước khi viết (GATE 0b)

GATE 0 (kế hoạch soạn, ghi `ke-hoach-soan.txt`, không gửi duyệt) và GATE 0b (dàn ý) của `vbhc-vn` áp dụng cho plugin này (Bạn chốt 17/10/2026): lập dàn ý theo dàn ý mặc định dưới đây hoặc mẫu gần nhất trong kho, viết thân ngay, không gửi dàn ý xin duyệt trừ khi Bạn yêu cầu; khi giao file báo một dòng "Dàn ý theo mẫu …". Bảng đủ các loại: `vbhc-vn` `reference/dan-y-mac-dinh.md`.

Dàn ý mặc định của bài phát biểu: mở đầu (kính thưa phân tầng, 1–2 đoạn gắn nghị quyết) → bối cảnh, kết quả → hạn chế →
nhiệm vụ, giải pháp (các nhóm, mở bằng "Kính thưa Hội nghị!") → tín hiệu, cơ hội (tùy chọn) → kết thúc (cam kết, mong
phối hợp, cảm ơn) — chi tiết từng phần ở mục 3 dưới đây. Bài tóm tắt 03 trang khi Giám đốc dự họp UBND tỉnh: biến thể
ở mục 7.

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
| **BCH Đảng bộ tỉnh / Tỉnh ủy** | Kính thưa: Đồng chí Bí thư Tỉnh ủy, / Các đồng chí Thường trực Tỉnh ủy, Ủy viên Ban Thường vụ Tỉnh ủy, / Thưa toàn thể các đồng chí Ủy viên Ban Chấp hành Đảng bộ tỉnh! — **Bản Giám đốc sửa tay 28/10/2026** (hội nghị có đại diện Ban Đảng Trung ương dự): Kính thưa: Đồng chí Bí thư Tỉnh ủy, / Kính thưa các đồng chí Thường trực Tỉnh ủy, Ủy viên Ban Thường vụ Tỉnh ủy, Ủy viên Ban Chấp hành Đảng bộ tỉnh, / Kính thưa các đồng chí đại diện các Ban Đảng Trung ương, / Thưa toàn thể các đồng chí! |
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
- [ ] **Đã soạn kèm tin nhắn Zalo gửi lãnh đạo** (Bước 5, R30).

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
- **Đề mục & cụm dẫn đầu:** in đậm. **`Kính thưa Hội nghị!`** in đậm + nghiêng,
  **thụt dòng đầu 1.27 cm như thân bài** (thẻ `[BREAK]` của script đã thụt từ 06/10/2026;
  trước đó dòng này sát lề trái — lỗi bắt được khi dựng bài 06/10/2026).
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

**Trưởng phòng báo cáo tại giao ban Sở** (Bạn chốt 06/9/2026): mẫu `kho-bai-mau/bpb-giao-ban-thang-9-2026-truong-phong-qlcn.docx` — kính thưa 3 dòng (Giám đốc chủ trì, các Phó Giám đốc, toàn thể đồng chí dự họp), xưng "Thay mặt Phòng Quản lý Công nghiệp", kết quả lồng ghép lũy kế + tháng gần nhất trong từng lĩnh vực, đề xuất đúng cấp (PGĐ phụ trách/Giám đốc), không nhắc vận chuyển HHNH. Quy ước chi tiết: `vbhc-vn/reference/bao-cao-dinh-ky-phong-qlcn.md` mục 3.

**Giám đốc dự cuộc họp của UBND tỉnh do Chủ tịch chủ trì về một lĩnh vực Sở chủ trì** (Bạn chốt 06/10/2026, vụ họp CCN theo Giấy mời 565/GM-UBND): soạn **bài phát biểu tóm tắt 03 trang** đi kèm Báo cáo đầy đủ đã gửi Văn phòng UBND tỉnh — mẫu `kho-bai-mau/bpb-hop-ccn-ubnd-tinh-2026-10-06-tom-tat.docx`. Kính thưa 04 dòng (Chủ tịch; PCT Thường trực; PCT phụ trách; lãnh đạo sở, ngành, đơn vị, UBND xã, phường dự họp); mở đầu một câu nêu đã gửi Báo cáo đầy đủ + báo trước 04 nội dung; 04 đề mục `1. Về … / 2. Về … / 3. Về nguyên nhân … / 4. Những việc đề nghị UBND tỉnh chỉ đạo` bám đúng thứ tự Báo cáo; mục 4 dùng "Một là … Năm là", mỗi ý một việc + cơ quan + mốc; nguyên nhân nêu đủ 03 nhóm, có câu "UBND tỉnh đã nhiều lần chỉ đạo tại …" và "Sở … nhận trách nhiệm …"; kết bằng cam kết đôn đốc + "Xin trân trọng cảm ơn các đồng chí!". **Số liệu chép đúng Báo cáo cùng kỳ** (plugin `kccn-sct-vn` ref 44), không thêm số mới; tên 03 cụm Phú Thịnh viết đủ.

**Giám đốc phát biểu tại Hội nghị Ban Chấp hành Đảng bộ tỉnh về vướng mắc các dự án khu, cụm công nghiệp trọng điểm** (Bạn chốt 28/10/2026, 8 vòng Giám đốc duyệt qua Zalo): mẫu **`kho-bai-mau/bpb-bch-dang-bo-tinh-2026-10-28-khu-cum-cong-nghiep-gd-duyet.docx`** (bản Giám đốc duyệt 20h29, 5 trang) — đọc `references/bpb-bch-dang-bo-tinh-khu-cum-cong-nghiep-28-10-2026.md` (kết cấu, chuỗi 15 ý kiến Giám đốc, bản Giám đốc sửa tay, bản Giám đốc sửa cuối trên Zalo, quy tắc R8–R22). Tóm tắt: sau đoạn số liệu tăng trưởng là đoạn **việc lớn Tỉnh ủy, UBND tỉnh đã triển khai** (chỉ thị, ban chỉ đạo, kiểm tra thực địa, kết luận, hội nghị — số, ngày, tên người đứng đầu, một câu đánh giá đúng mức về chỉ thị mới) rồi mới vào vướng mắc; phần I, II **chỉ nêu hiện trạng và vướng mắc** (Giám đốc chốt "nêu vấn đề và giao việc luôn", không để khối "giải quyết ngay / cần chỉ đạo" lặp với phần III); phần III mở bằng câu **đề nghị Hội nghị phát động chiến dịch GPMB đến 31/12/2026**, 8 mục phân công viết **giọng ngang cấp** ("đề nghị Sở…", việc Chủ tịch đã giao thì dẫn "đã được Chủ tịch UBND tỉnh giao"), mục cuối "Về phần mình, Sở Công Thương nhận trách nhiệm…"; kết một đoạn, không lặp phần cam kết; **mốc thời gian soát theo ngày đọc** (bỏ mốc trong tháng soạn); "khoảng 5 trang" là tối đa 5 trang; tên, số lãnh đạo nhắn qua Zalo phải đối chiếu bản gốc (Chỉ thị "34" → 42-CT/TU; "tổ công tác" → Ban Chỉ đạo); **mỗi việc phải có chủ thể** (Giám đốc đánh "Ai?" vào câu không có cơ quan chủ trì); bỏ câu "Thay mặt…" mở đầu, vào thẳng số liệu khi Giám đốc đã sửa tay như vậy; **an ninh, trật tự viết mềm**, không nêu đích danh khu, có "(nếu có)" (R18); Giám đốc sửa trên Zalo dán toàn văn cũng là bản duyệt — diff, chỉ sửa lỗi gõ và điền chỗ đánh dấu (R19); làm tròn số khi đọc, chức danh thay tên riêng lãnh đạo cấp trên, trích chỉ đạo của Chủ tịch nguyên văn trong ngoặc kép, dẫn quyết định nhiều dự án phải nêu tên từng dự án (R20); bản lãnh đạo sửa vẫn đối chiếu plugin (R21); **kết bài bằng một khẩu hiệu hành động hai vế có vần, riêng một đoạn đậm nghiêng căn giữa** — "Mặt bằng sạch đến đâu, dự án về đến đó; công nghiệp vươn xa, Lào Cai bứt phá!" (R22). Số liệu, mốc, bộ máy: plugin `kccn-sct-vn` ref 54.

**Lãnh đạo Sở đi làm việc với địa phương nước ngoài (đối ngoại, giới thiệu Lào Cai và mời hợp tác)** (Bạn chốt 30/10/2026, PGĐ Hoàng Văn Thuân sang thành phố Ngọc Khê, Vân Nam): mẫu `kho-bai-mau/bpb-doi-ngoai-thanh-pho-ngoc-khe-2026-10-30-pgd-thuan.docx` (2 trang) — đọc `references/bpb-doi-ngoai-lam-viec-dia-phuong-trung-quoc-30-10-2026.md` (R23–R30). Tóm tắt: **xác định trước chiều chuyến đi** — sang thăm hay đón đoàn (bản đầu viết nhầm thành đón đoàn, phải viết lại; R23); mặc định 2 trang, câu ngắn, số làm tròn, không đọc số hiệu văn bản vì qua phiên dịch (R24); kết cấu 6 khối: câu hình ảnh gắn kết hai địa phương → bốn câu dẫn đậm "Lào Cai là cửa ngõ / tỉnh công nghiệp / thị trường và điểm đến / giàu nguyên liệu xanh" → thế mạnh của bạn + câu bắc cầu → năm hướng hợp tác "Một là… Năm là" (thương mại và hội chợ, logistics, chế biến sâu khoáng sản, nông lâm sản, du lịch) → cam kết đầu mối + mời sang thăm Lào Cai → kết (R25); "số liệu mới nhất đến hết tháng …" thì ước tháng chưa có số, bôi tím số ước (R26); không mời hợp tác đất hiếm, không nêu tên doanh nghiệp (R27, `dacn-sct-vn` ref 13); Hội chợ Kinh tế Thương mại và Du lịch Biên giới Việt – Trung (Hà Khẩu, 8–13/11/2026) đặt ở hướng hợp tác thứ nhất kèm lời mời tham gia, soát theo ngày đọc (R29).

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
- `references/bpb-bch-dang-bo-tinh-khu-cum-cong-nghiep-28-10-2026.md` — **bài phát biểu tại Hội nghị BCH Đảng bộ tỉnh về vướng mắc KCN, CCN (28/10/2026)**: chuỗi 15 ý kiến Giám đốc, kết cấu bản duyệt 5 trang, quy tắc R8–R22 (giọng ngang cấp ở phần phân công, việc lớn trước vướng mắc sau, mốc theo ngày đọc, độ dài là mệnh lệnh và thứ tự cắt, dễ đọc trên bục, đối chiếu tên số lãnh đạo nhắn Zalo, không chép chữ sai của báo, giữ chỗ Giám đốc đã sửa tay, mỗi việc phải có chủ thể, nêu vấn đề và giao việc luôn, an ninh trật tự viết mềm, bản Giám đốc sửa trên Zalo là bản duyệt, dẫn quyết định nhiều dự án nêu tên từng dự án), bản Giám đốc sửa tay và sửa cuối trên Zalo, cách dựng file python-docx.
- `references/bpb-doi-ngoai-lam-viec-dia-phuong-trung-quoc-30-10-2026.md` — **bài phát biểu đối ngoại khi lãnh đạo Sở sang làm việc với địa phương nước ngoài** (PGĐ Thuân – thành phố Ngọc Khê, 30/10/2026): chuỗi 6 ý kiến, R23 chiều chuyến đi, R24 hai trang qua phiên dịch, R25 kết cấu 6 khối, R26 ước số tháng gần nhất bôi tím, R27 nội dung đối ngoại, R28 thông tin địa phương bạn, R29 sự kiện có ngày, **R30 luôn giao kèm tin nhắn Zalo gửi lãnh đạo** (áp dụng mọi bài), số cửa khẩu, Hội chợ Việt – Trung 2026, ba tin nhắn thật.
- `references/tra-loi-phong-van-bao-chi.md` — **11 quy tắc riêng cho TRẢ LỜI PHỎNG
  VẤN BÁO CHÍ** (đúc kết từ bản duyệt PGĐ Hoàng Văn Thuân 11/8/2026, vụ TTXVN): mở
  bài bằng số vĩ mô tầng bậc, khung "điểm nghẽn → năng lực sản xuất mới", giải pháp
  theo chuỗi sản phẩm có tên mỏ/nhà máy, nguyên tắc 3 tầng thẩm quyền, không đọc số
  hiệu văn bản, không xác nhận tiền đề tiêu cực của câu hỏi, giọng điềm đạm, sản
  phẩm kép kèm bản tóm tắt. **BẮT BUỘC đọc trước khi soạn bài phỏng vấn.**
- `kho-bai-mau/` — **22 bài mẫu gốc** do Sở cung cấp (kèm `00-MUC-LUC.md` tra nhanh
  theo dịp; tên file đã chuẩn hoá không dấu). Ưu tiên **mở đúng mẫu gần nhất** với
  dịp đang soạn để bám thể thức/giọng (Chế độ B — sửa mẫu thật). File
  `bpb-bch-ktck-gd-duyet.docx` là bản GĐ đã duyệt — chuẩn cao nhất để đối chiếu;
  `phong-van-ttxvn-2026-08-11-ban-duyet-pgd-thuan.docx` (+ bản tóm tắt cùng ngày) là
  chuẩn cao nhất cho thể loại trả lời phỏng vấn báo chí.
- `scripts/build_bpb.py` — sinh file .docx đúng định dạng bài phát biểu.
