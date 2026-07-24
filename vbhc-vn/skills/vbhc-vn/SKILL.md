---
name: vbhc-vn
description: "Soạn thảo, rà soát văn bản hành chính (.docx) Sở Công Thương Lào Cai: công văn, tờ trình, báo cáo, kế hoạch, quyết định, giấy phép (kể cả HHNH), GCN ATTP, công văn nội bộ phòng; văn bản cấp UBND tỉnh/VP do Sở dự thảo (giấy mời, chỉ đạo, thông báo kết luận, phiếu trình). Dùng cho tham mưu, thẩm định, góp ý, bài phát biểu, VBQPPL; nhận PDF văn bản đến thì chạy scripts/extract_metadata.py đọc đúng số/ngày/người ký. Gồm: Chế độ A (template trắng), Chế độ B (sửa file gốc); 9 nhóm anti-error; QA một phát qa_all.py (render 1 lần + ảnh ghép: widow, khối ký, Line header, 13pt Số/Ngày, chiều cao dòng bảng); 3 Phụ lục NĐ 30/2020 (thể thức, viết hoa, viết tắt). Trigger: soạn/rà soát/sửa/tham mưu/thẩm định/góp ý/triển khai; ký hiệu SCT-CN, TTr-SCT, BC-SCT, KH-SCT, QĐ-SCT, GP-SCT, GCNATTP-SCTLC; tên file PDF chứa CV/QĐ/TTr/BC/KH/NQ/NĐ/TT/UBND/SCT/HĐND."
---

# vbhc-vn — Soạn văn bản hành chính từ mẫu thật của Sở Công Thương Lào Cai

Nguyên tắc lõi: **giữ nguyên 100% định dạng gốc** (header, gạch chân, bảng chữ ký, font), chỉ thay nội dung — không sinh văn bản từ đầu bằng code khi đã có mẫu/file gốc. *Vì sao:* dựng lại bằng code thường không tái tạo đúng khung, đường gạch chân, layout chữ ký → dễ sai thể thức và mất thời gian; mẫu thật đã được kiểm chứng.

Skill có **2 chế độ làm việc** (xem mục "Hai chế độ làm việc" bên dưới để chọn đúng):
- **Chế độ A — Tạo mới từ template**: dùng 09 mẫu trắng trong `templates/` + `TemplateDoc`. Áp dụng khi soạn một văn bản mới (công văn, tờ trình, quyết định, biên bản…).
- **Chế độ B — Sửa file người dùng tải lên**: dùng workflow `unpack → sửa `word/document.xml` → pack`. Áp dụng khi rà soát/chỉnh sửa file .docx có sẵn (báo cáo, phụ lục, biểu, kịch bản điều hành, bài phát biểu, kết luận…). **Đây là loại việc thường gặp nhất** và phải giữ nguyên định dạng file gốc, KHÔNG dựng lại bằng template.

**Thư viện mẫu sẵn có trong skill**: `templates/` = mẫu TRẮNG (Chế độ A, điền bằng `TemplateDoc`, đánh số 01-09); `examples/` = văn bản THẬT đã ban hành (Chế độ B - mở mẫu, copy ra chỗ làm việc, thay nội dung, giữ định dạng), gồm `examples/sct/` và `examples/ubnd/`. Xem mục "Thư viện mẫu thật đã ban hành (`examples/`)".

## Tài liệu tham chiếu (`reference/`) — đọc khi cần
SKILL.md chỉ giữ phần lõi; chi tiết nằm ở các file dưới (đọc đúng file khi cần, để tiết kiệm ngữ cảnh):
- `reference/templates-chi-tiet.md` — cấu trúc paragraph/table từng template 01–09 (Chế độ A).
- `reference/thu-vien-mau-that.md` — 17 mẫu thật `examples/`, bảng mẫu↔loại VB, người ký, cấu trúc mẫu UBND/VP (Chế độ B).
- `reference/phong-tranh-sai-lam.md` — chi tiết 9 nhóm sai lầm + checklist + vụ thật (Nhóm I: văn phong công văn gửi doanh nghiệp).
- `scripts/qa_all.py` — **QA MỘT PHÁT (đường QA chính từ v2.1.0)**: một lệnh gộp kiểm XML (Line header, 13pt Số/Ngày, br trong header, body căn giữa/firstLine) + check_document + render PDF đúng 1 lần (widow word, khối ký gãy trang) + xuất ẢNH GHÉP mọi trang trong 1 ảnh để `view` 1 lượt. Chạy ở Bước 4, nối liền lệnh build.
- `scripts/qa_pdf_check.py` — QA 4 mục thể thức chạy lẻ khi cần; có `--pdf <path>` dùng PDF render sẵn khỏi render lại.
- `reference/cong-cu-ky-thuat.md` — công thức kỹ thuật ĐÃ KIỂM CHỨNG (giải nén RAR/RAR5 tên tiếng Việt, OCR PDF scan/chữ ký số, sửa docx đa run, QA render) — đọc TRƯỚC khi xử lý file nén/PDF scan/sửa XML, không mò lại từ đầu.
- `reference/doc-pdf-metadata.md` — chi tiết quy trình đọc PDF công văn đến (cờ kích hoạt, OCR, 11 trường).
- `reference/cong-thuc-thuc-chien.md` — căn bảng/biểu khổ ngang, đồng bộ chéo nhiều file.
- `reference/the-thuc-code.md` — **mã chuẩn khi DỰNG MỚI TỪ ĐẦU**: hàm định dạng đoạn 1cm duy nhất + XML đường Line (VML). Đọc khi không có mẫu và phải sinh .docx bằng code.
- `reference/nd-79-2025-tom-tat.md` (+ file gốc `79_2025_ND-CP.docx`) — kiểm tra, rà soát, xử lý VBQPPL hết hiệu lực (gắn Nhóm D).
- `reference/nd30-phu-luc-1-the-thuc.md` — **VĂN BẢN GỐC Phụ lục I NĐ 30/2020**: thể thức, kỹ thuật trình bày (cỡ chữ, kiểu chữ, vị trí ô 1-14, khoảng cách từng thành phần; sơ đồ bố trí; bảng mẫu chữ Mục V; bản sao văn bản). Đọc khi: (a) băn khoăn quy cách một thành phần thể thức mà SKILL.md/the-thuc-code.md chưa nêu; (b) người dùng hỏi căn cứ pháp lý của một quy tắc trình bày; (c) đối chiếu khi render soi ảnh phát hiện nghi vấn thể thức.
- `reference/nd30-phu-luc-2-viet-hoa.md` — **VĂN BẢN GỐC Phụ lục II NĐ 30/2020**: quy tắc viết hoa (tên người, địa lý, cơ quan tổ chức, chức danh, ngày lễ, viện dẫn phần/chương/mục/điều/khoản/điểm). Đọc khi soạn thảo gặp trường hợp viết hoa không chắc chắn — KHÔNG đoán.
- `reference/nd30-phu-luc-3-viet-tat-mau.md` — **VĂN BẢN GỐC Phụ lục III NĐ 30/2020**: bảng chữ viết tắt tên loại văn bản (NQ, QĐ, CT, QC, TB, HD, KH, PA, ĐA, BC, BB, TTr, HĐ, CĐ, GM, GGT, GNP, PC...) + mô tả mẫu trình bày và ghi chú chân trang. Đọc khi cần ký hiệu chuẩn cho loại văn bản chưa có trong templates/, hoặc kiểm tra ký hiệu văn bản đến/đi.

## Khi nào dùng

Khi người dùng yêu cầu tạo/soạn **hoặc rà soát/sửa/chỉnh** các văn bản:
- Công văn (CV), Tờ trình (TTr), Báo cáo (BC), Kế hoạch (KH)
- Quyết định cá biệt (QĐ-SCT), Giấy phép (GP), Giấy chứng nhận ATTP
- Phụ lục, biểu tổng hợp (khổ ngang), kịch bản điều hành, bài phát biểu, kết luận hội nghị, phiếu nhận xét/thẩm định hồ sơ
- Công văn nội bộ giữa các phòng (vd Phòng QLCN tham gia ý kiến gửi Phòng Kế hoạch - Tổng hợp), do Trưởng phòng ký
- **Văn bản cấp UBND tỉnh / Văn phòng UBND tỉnh** mà Sở dự thảo: giấy mời họp, công văn chỉ đạo/đề nghị, thông báo kết luận, phiếu trình, báo cáo của VP UBND (xem mục riêng phía dưới)
- Giấy phép vận chuyển hàng hóa nguy hiểm (GP-SCT), giấy mời dự họp cấp Sở (SCT-CN), tờ trình ban hành VBQPPL - có mẫu thật trong `examples/sct/`

Hoặc nhắc tới các ký hiệu: `SCT-CN`, `TTr-SCT`, `BC-SCT`, `KH-SCT`, `QĐ-SCT`, `GP-SCT`, `GCNATTP-SCTLC`.

**Luôn áp dụng mục "Phòng tránh 9 nhóm sai lầm tham mưu"** (đã hợp nhất từ `anti-error-sct-vn`) ở cuối skill này: tránh bịa số văn bản, suy diễn nhiệm vụ, dùng từ suy đoán trong bản trình ký, dùng VBPL hết hiệu lực, tin context window với PDF; và **Nhóm I - văn phong công văn gửi doanh nghiệp**: không nêu mốc hiệu lực giấy tờ mà DN chưa vi phạm, không viết "đề nghị liên hệ Phòng ... để được hướng dẫn". Xem mục "Đọc PDF văn bản đến" (đã hợp nhất từ vbhc-pdf-reader-vn — xác minh số/ngày từ PDF công văn đến). Đối chiếu nội dung chuyên môn với `kcn-ccn-vn`/`hnh-sct-vn`.

## Thể thức, văn phong và rà soát (quy ước cố định của Bạn — hợp nhất từ bộ nhớ)

Áp dụng cho MỌI văn bản soạn/sửa trong skill này.

### Thể thức trình bày (VBHC thường — theo NĐ 30/2020)
Căn cứ gốc đầy đủ nằm ở `reference/nd30-phu-luc-1-the-thuc.md` (thể thức từng thành phần), `nd30-phu-luc-2-viet-hoa.md` (viết hoa), `nd30-phu-luc-3-viet-tat-mau.md` (viết tắt tên loại VB) — tra khi có điểm chưa chắc, KHÔNG suy đoán quy cách. Các dòng dưới là quy ước đã chốt áp dụng hằng ngày:
- **Font** Times New Roman, **cỡ chữ 14** cho nội dung. **Lề A4**: trên/dưới 20mm, trái 30mm, phải 20mm. **Line spacing** single; **before/after** 6pt; **first line indent 1cm**; **căn đều (justify)**. TẤT CẢ đoạn nội dung và đề mục (I, II; 1, 2; a, b; "một là", "hai là"...) lùi đầu dòng **đồng nhất 1cm** — không "cái vào cái ra", **không thụt treo (hanging indent)**. Khi dựng bằng code: dùng **một hàm định dạng đoạn duy nhất** (mặc định firstLine=1cm), KHÔNG tự đặt firstLine=0 cho đề mục; số thứ tự (1., 2., a., b.) viết liền vào đầu dòng văn bản (không dùng numbering treo); dòng thành phần "Ông/Bà:..." để **căn trái** cho gọn; render ra ảnh kiểm tra từng trang trước khi xuất.
- Bố cục đủ: Quốc hiệu/Tiêu ngữ, tên cơ quan, số ký hiệu, địa danh-ngày, trích yếu, nội dung, nơi nhận, chữ ký.
- **Header bắt buộc vẽ đường kẻ ngang bằng ĐỐI TƯỢNG LINE (Insert > Shapes > Line)** ở CẢ HAI bên: dưới tên cơ quan ban hành (vd "SỞ CÔNG THƯƠNG", "PHÒNG QUẢN LÝ CÔNG NGHIỆP") và dưới "Độc lập - Tự do - Hạnh phúc"; căn giữa, dài ~1/2 ô (3-5cm), là đường kẻ thật chọn/di chuyển được. Không dùng ký tự gạch chân (underscore) cũng không dùng paragraph border — *vì sao:* underscore và border không phải đối tượng vẽ, không căn giữa/chỉnh độ dài được và dễ lệch khi sửa nội dung. Khi dựng .docx bằng code: tạo đường kẻ dưới dạng line drawing object (VML `<v:line>` nổi, căn giữa theo lề: `mso-position-horizontal:center;mso-position-horizontal-relative:margin`, hoặc DrawingML) — mã sẵn ở `reference/the-thuc-code.md`; render ra ảnh kiểm tra đường kẻ hiển thị đúng trước khi xuất.
- **Không dùng màu nền/shading** cho bất kỳ ô/dòng/bảng nào — bảng nền trắng, chỉ viền đen mảnh. *Vì sao:* VBHC chuẩn dùng nền trắng; shading dễ lệch màu, khó đọc khi in/photocopy.
- Cột Quốc hiệu được phép rộng vượt tỷ lệ chuẩn để Quốc hiệu nằm gọn trên 1 dòng. Đoạn bị lẻ 1 chữ ở dòng cuối: co khoảng cách chữ (character spacing/condensed) để tránh.
- **KHÔNG bao giờ chèn ngắt dòng cứng `\n`/`<w:br/>` trong một paragraph** (xem Quy tắc bất biến 10) — V/v, tên cơ quan, ngày tháng để chuỗi liền, Word tự wrap.

### VBQPPL (QĐ UBND, NQ HĐND) — KHÔNG dùng NĐ 30/2020
Theo **NĐ 78/2025 + NĐ 187/2025**. Lề trên/dưới/phải 15-20mm, trái 30-35mm. Quốc hiệu/Tiêu ngữ/Tên CQ 12-14 đậm; số ký hiệu CÓ năm (.../2026/QĐ-UBND); CĂN CỨ cỡ 14 nghiêng; nội dung 13-14 lùi 1-1.27cm; Điều đậm; Nơi nhận 12 nghiêng đậm. QĐ UBND QPPL trực tiếp theo **Mẫu 19** (NĐ 78/2025 PL III): có dòng "Ủy ban nhân dân tỉnh ban hành Quyết định..." nghiêng, sau căn cứ, trước "QUYẾT ĐỊNH:".

### Văn phong & viết tắt
- Phong cách hành chính: KHÔNG ký tự đặc biệt, emoji, dấu sao (*); không dùng `*` để in đậm/gạch đầu dòng.
- Trong nội dung chính (trừ tiêu đề và dòng "Kính gửi"): **viết tắt ngay từ lần đầu**: Ủy ban nhân dân→UBND; Hội đồng nhân dân→HĐND; Mặt trận Tổ quốc→MTTQ; trách nhiệm hữu hạn→TNHH (kể cả trong tên DN: "Công ty TNHH..."). "Quốc hội" giữ nguyên.
- Đơn vị diện tích: luôn **"ha"**, KHÔNG "héc-ta"/"hecta" — kể cả nội dung cho truyền hình/đại chúng.
- Địa danh cũ của Yên Bái (Âu Lâu, Trấn Yên, Văn Chấn, Nghĩa Lộ, Mù Cang Chải, Trạm Tấu, Lục Yên, Văn Yên, Yên Bình...) nay thuộc **tỉnh Lào Cai** (từ 1/7/2025) — ghi "tỉnh Lào Cai".

### Ký hiệu, người soạn, tên file, định dạng xuất
- **Ký hiệu**: Công văn `SCT-CN`; Tờ trình `TTr-SCT`; Báo cáo `BC-SCT`; Kế hoạch `KH-SCT`; QĐ cá biệt `QĐ-SCT`; Giấy phép `GP-SCT`; GCN ATTP `.../{năm}/GCNATTP-SCTLC`. Dòng lưu: `Lưu: VT, CN(Tên)`. Văn bản do Bạn (PGĐ Chiến, phụ trách QLCN) yêu cầu **luôn dùng `SCT-CN` + `Lưu: VT, CN(tên)`**, kể cả khi nội dung thuộc lĩnh vực phòng khác — KHÔNG đổi sang ký hiệu phòng khác.
- **Tên file**: `năm.tháng.ngày. Trích yếu` tiếng Việt CÓ DẤU (vd `2026.06.19. Báo cáo tổng kết...`). Ngày = ngày ban hành/dự kiến ký, không rút gọn tùy tiện ("v2", "final").
- **CHỈ tạo file Word (.docx), KHÔNG kèm PDF**.

### Rà soát/review — các lỗi KHÔNG được báo (đã thống nhất)
- KHÔNG báo lỗi **thiếu số ký hiệu** ("Số: .../...") đối với file Word (số do văn thư cấp sau).
- KHÔNG báo lỗi **"thiếu chữ NAM"** trong Quốc hiệu và KHÔNG tự thêm "NAM" — nếu công cụ trích xuất hiển thị Quốc hiệu kết thúc ở "...VIỆT", đó là lỗi hiển thị phía Claude (NAM nằm ở run/dòng khác), không phải văn bản thiếu chữ.
- Khi trích metadata PDF: nếu không đọc được người ký, KHÔNG cần OCR lại — chỉ cần số văn bản + ngày là đủ.

### Một số loại có quy ước riêng (tóm tắt; chi tiết ở mục template/examples)
- **Giấy mời họp `SCT-GM`**: văn bản độc lập, không tham chiếu cuộc họp trước, các thành phần bình đẳng, không ghi "mời thêm"; kết cấu 4 mục (Thành phần; Thời gian; Địa điểm; Nội dung).
- **QĐ cá biệt SCT**: "QUYẾT ĐỊNH" + "Về việc..."; "GIÁM ĐỐC SỞ CÔNG THƯƠNG" in hoa đậm căn giữa; căn cứ in nghiêng; cuối căn cứ "Theo đề nghị của Trưởng phòng Quản lý công nghiệp,"; "QUYẾT ĐỊNH:" đậm; Điều 1, 2, 3 đậm.
- **GCN ATTP**: KHÔNG có số góc trái; Quốc hiệu căn giữa toàn trang; số cấp `.../{năm}/GCNATTP-SCTLC` đặt dưới bảng; hiệu lực 3 năm; kèm phụ lục danh mục.
- **Biên bản (làm việc, kiểm tra)**: mở đầu Quốc hiệu căn giữa, **KHÔNG cấp số**; đường gạch chân ngang dưới Quốc hiệu vẽ bằng ĐỐI TƯỢNG LINE (shape) căn giữa — không dùng character underline, không dùng paragraph border. Có **template trắng `templates/09-bien-ban.docx`** (Chế độ A) và 2 mẫu thật `bien-ban-lam-viec-lien-nganh-ccn.docx`, `bien-ban-kiem-tra-thuc-te-hhnh.docx` trong `examples/sct/` (Chế độ B — ưu tiên khi có vụ việc tương tự).

## Quy tắc tốc độ (v2.1.0) — hoàn thành 1 văn bản trong ÍT LƯỢT TOOL NHẤT

Mục tiêu: văn bản thường (công văn, tờ trình ≤ 3 trang) xong trong **3-4 lượt tool**: (1) viết script build, (2) một lệnh bash `build && qa_all`, (3) view 1 ảnh ghép, (4) copy outputs + present_files. Cụ thể:
1. **Không chạy inspect template** khi `reference/templates-chi-tiet.md` đã có chỉ số (Bước 2).
2. **Nối build + QA trong MỘT lệnh bash**: `python3 build.py && python3 scripts/qa_all.py output/<file>.docx --forbid "<chuỗi vụ cũ>" ... --require "<chuỗi vụ mới>" ...`. Không tách validate/render/qa thành các lượt riêng. Với Chế độ B trên mẫu thật, `--forbid`/`--require` là BẮT BUỘC (Quy tắc bất biến 17).
3. **Render PDF đúng 1 lần mỗi vòng** — `qa_all.py` tự lo; không tự gọi soffice/pdftoppm rời nữa.
4. **View đúng 1 ảnh ghép** `qa_sheet.png`; chỉ mở ảnh trang lẻ khi có nghi vấn cụ thể.
5. **Sửa lỗi theo báo cáo text, gom hết rồi mới render lại** — không lặp render/view sau từng lỗi nhỏ.
6. **Đọc reference đúng file cần** (bảng ở mục "Tài liệu tham chiếu"), không đọc dàn trải; nội dung SKILL.md này đã đủ cho văn bản thường.
7. Chỉ vòng lặp thêm khi qa_all FAIL hoặc người dùng yêu cầu sửa — chất lượng vẫn là chốt chặn: **không giao file chưa PASS**.

## Hai chế độ làm việc

> **QUY TẮC ƯU TIÊN (theo yêu cầu của Bạn): luôn ưu tiên sửa trên MẪU THẬT thay vì soạn từ template trắng.**
> Khi cần soạn một văn bản, TRƯỚC TIÊN kiểm tra `examples/` xem có mẫu thật phù hợp với loại văn bản đó không:
> - **Có mẫu phù hợp** → dùng **Chế độ B**: copy mẫu thật ra chỗ làm việc, thay nội dung, giữ 100% định dạng đã được kiểm chứng. Đây là cách Bạn muốn ưu tiên.
> - **Không có mẫu phù hợp** → mới dùng **Chế độ A** (template trắng trong `templates/`).
> - Nếu Bạn tải lên một file .docx cụ thể để sửa → luôn dùng Chế độ B trên chính file đó.
> Bảng "Mẫu thật ↔ loại văn bản" ở mục "Thư viện mẫu thật đã ban hành (`examples/`)" giúp tra nhanh mẫu nào dùng cho việc gì.

### Chế độ A — Tạo mới từ template (`templates/` + `TemplateDoc`)
Theo "Quy trình bắt buộc (5 bước)" bên dưới. Dùng khi soạn một văn bản mới **chưa có mẫu thật phù hợp trong `examples/`** và Bạn không tải lên file gốc.

### Chế độ B — Sửa file người dùng tải lên hoặc mẫu thật trong `examples/` (unpack → sửa XML → pack)
Dùng khi rà soát/chỉnh sửa file .docx có sẵn, **hoặc khi soạn mới mà có mẫu thật phù hợp trong `examples/`** (ưu tiên). **Tuyệt đối không dựng lại từ template** (sẽ mất định dạng gốc). Workflow đã kiểm chứng nhiều lần:

```bash
# 1. Đọc nội dung để nắm cấu trúc (text + bảng)
cd /mnt/user-data/uploads && ls -la
extract-text "TÊN_FILE.docx"          # với .doc: convert trước bằng soffice.py --convert-to docx

# 2. Giải nén để sửa trực tiếp XML
cp "/mnt/user-data/uploads/TÊN_FILE.docx" /home/claude/work/src.docx
python /mnt/skills/public/docx/scripts/office/unpack.py /home/claude/work/src.docx /home/claude/work/unpacked/

# 3. Sửa /home/claude/work/unpacked/word/document.xml bằng str_replace (kèm context <w:rPr> để trúng đúng run)
#    grep -n "chuỗi cần tìm" để định vị; sửa số liệu / câu chữ / đánh số mục…

# 4. Đóng gói lại — BẮT BUỘC dùng --original để giữ relationships, media, content-types
python /mnt/skills/public/docx/scripts/office/pack.py /home/claude/work/unpacked/ /home/claude/work/out.docx --original /home/claude/work/src.docx
```

**Bài học XML đã rút ra (áp dụng để khỏi vấp lại):**
- Khi một chuỗi (vd tên người, "Lào Cai") xuất hiện ở **cả bảng dữ liệu lẫn khối chữ ký**, `sed -i` sẽ thay nhầm tất cả → dùng `str_replace` kèm context `<w:rPr>` (cỡ chữ `<w:sz w:val="..."/>`, có/không `<w:b/>`) để trúng đúng vị trí.
- Văn bản bị tách run bởi `<w:lastRenderedPageBreak/>` → phải `str_replace` cả cụm bắc qua thẻ ngắt, không tách 2 lần.
- Đổi run **đậm → nghiêng**: thay cả khối `<w:r>...</w:r>` gồm `<w:rPr>` (đổi `<w:b/>` thành `<w:i/>`), không chỉ đổi text.
- **Sắp xếp lại thứ tự dòng trong bảng** (gộp/đổi nhóm): thao tác ở cấp XML qua `tbl._tbl` / `tbl.tr_lst`, gỡ rồi nối lại `<w:tr>` theo thứ tự mong muốn — API `python-docx` chuẩn không hỗ trợ reorder.
- **Điền ô trống**: tìm `<w:p ...>` không chứa `<w:r`/`<w:t>`, chèn `<w:r>` ngay sau `</w:pPr>`. `paraId` tự sinh phải < `0x80000000` (vd dùng tiền tố `0A...`, tránh `AA...`).
- File `.doc` (cũ): convert sang `.docx` bằng `soffice.py --headless --convert-to docx` trước khi `extract-text`.
- **KHÔNG truy cập `d.paragraphs[n]` theo chỉ số sau khi đã chèn/xóa cấu trúc** (vụ thật CV kho VLNCN 04/7/2026: 4 lỗi cùng gốc — body căn giữa, sót nội dung vụ cũ, thiếu dòng Kính gửi, sai tháng): danh sách paragraph tự tính lại nên chỉ số trôi. Bắt TRƯỚC mọi tham chiếu cần dùng: `paras0 = list(d.paragraphs)` rồi thao tác qua `._p` đã lưu.
- **Clone paragraph để sinh body phải clone từ đoạn body chuẩn** (justify, firstLine ≥ 1cm) — clone từ đoạn căn giữa (Kính gửi, tiêu đề) sẽ thừa hưởng sai `pPr` cho toàn bộ nội dung.
- **Thay text header tách nhiều run**: lấy đủ chuỗi `''.join(r.text for r in p.runs)`, sửa, ghi vào `runs[0].text`, xóa text run sau — NHƯNG trước đó PHẢI kiểm tra run có shape không (Quy tắc 11); run chứa shape thì đi đường `w:t`.
- **Assertion tự động sau build** (bắt buộc với Chế độ B trên mẫu thật): không còn tên/địa danh vụ việc cũ; đủ các dòng Kính gửi; ngày tháng đúng; mọi đoạn body không CENTER; firstLine ≥ 1cm (≥ 360000 EMU); còn đủ số shape Line như gốc. Từ v2.1.0: phần CENTER/firstLine/shape Line/br-header đã nằm sẵn trong `scripts/qa_all.py` — chạy `qa_all.py` ngay sau build là phủ được; chỉ cần tự viết assertion riêng cho phần NỘI DUNG vụ việc (tên/địa danh cũ, dòng Kính gửi, ngày tháng).
- **Sửa XML trực tiếp trên file có run vụn**: chạy `merge_runs.py` (skill docx public) gộp `<w:t>` trước rồi mới str_replace; khớp whitespace trong `<w:t>` chính xác từng dấu cách.

**Thay nội dung trong run giữ định dạng (python-docx)**: gán `runs[0].text = chuỗi_mới` rồi xóa các run sau (`r.text = ''`) — giữ được đậm/nghiêng/font của run đầu.

## Quy trình bắt buộc cho Chế độ A (5 bước)

### Bước 1: Chọn template

| Loại văn bản | File template |
|---|---|
| Công văn | `templates/01-cong-van.docx` |
| Tờ trình | `templates/02-to-trinh.docx` |
| Báo cáo | `templates/03-bao-cao.docx` |
| Kế hoạch | `templates/04-ke-hoach.docx` |
| Quyết định cá biệt | `templates/05-quyet-dinh.docx` |
| Giấy phép | `templates/06-giay-phep.docx` |
| Giấy chứng nhận ATTP | `templates/07-giay-chung-nhan-attp.docx` |
| Công văn nội bộ Phòng (tham gia ý kiến) | `templates/08-cong-van-noi-bo-phong.docx` |
| Biên bản (làm việc, kiểm tra) | `templates/09-bien-ban.docx` |

### Bước 2: Lấy cấu trúc paragraph của template — KHÔNG chạy inspect nếu đã có sẵn

Chỉ số paragraph/table của cả 9 template đã ghi sẵn trong **`reference/templates-chi-tiet.md`** — đọc file đó và dùng luôn chỉ số, **bỏ qua lượt chạy inspect** (tiết kiệm 1 lượt tool). Chỉ chạy inspect khi nghi template đã bị sửa hoặc reference chưa khớp:

```bash
python3 scripts/fill_template.py templates/01-cong-van.docx   # chỉ khi cần đối chiếu
```

Lệnh trên in ra:
- Danh sách paragraph (P0, P1, P2,...) với text rút gọn
- Danh sách table (Table 0 = header, Table 1 = footer chữ ký)

### Bước 3: Viết script Python để sửa nội dung

Dùng `TemplateDoc` từ `scripts/fill_template.py`:

```python
from fill_template import TemplateDoc
doc = TemplateDoc('templates/01-cong-van.docx')

# Sửa header (Table 0)
doc.replace_in_cell(0, 0, 0, 'Số:       /SCT-CN', 'Số: 458/SCT-CN')
doc.replace_in_cell(0, 0, 0, 'V/v ……………….', 'V/v báo cáo tiến độ ...')
doc.replace_in_cell(0, 0, 1, 'ngày      tháng      năm 2026',
                    'ngày 15 tháng 5 năm 2026')

# Sửa Kính gửi (P2 trong công văn)
doc.replace_in_paragraph(2, '…………..', 'Ủy ban nhân dân tỉnh Lào Cai')

# Thay nội dung body (P4 đến P15)
doc.replace_body_paragraphs(start_idx=4, end_idx=16, new_paragraphs=[
    {'text': 'Đoạn mở đầu...'},
    {'text': '1. Mục thứ nhất', 'bold': True},
    {'text': '- Nội dung...'},
    # ...
])

# Sửa Lưu VT
doc.replace_in_cell(1, 0, 0, 'Lưu: VT, CN.', 'Lưu: VT, CN(Tên).')

# Lưu
doc.save('output/cong-van-moi.docx')
```

### Bước 4: Chạy script build + QA MỘT PHÁT (`qa_all.py`) — trong CÙNG MỘT lệnh bash

Trước khi xuất, **rà soát căn chỉnh đều đẹp và đồng bộ danh mục đánh số thứ tự các mục** (xem Quy tắc 8): hệ thống đề mục nhất quán, đánh số liên tục không nhảy bậc, đúng cấp (I, II, III → 1, 2, 3 → a, b, c hoặc 1.1, 1.2).

**Gộp build và QA vào MỘT lệnh bash duy nhất** (tiết kiệm 3-4 lượt tool so với chạy rời):

```bash
python3 scripts/<ten-script>.py && python3 scripts/qa_all.py output/<file>.docx
```

`qa_all.py` là **đường QA chính từ v2.1.0** — một lệnh, render PDF **đúng 1 lần** (profile soffice ấm, ~1-3s), làm trọn:
1. **Kiểm XML**: đủ Line header, 13pt dòng Số/Ngày (Quy tắc 11-12), `<w:br/>` trong header = 0 (Quy tắc 10), body căn giữa/thiếu firstLine 1cm (WARN — bài học Chế độ B).
2. **check_document.py**: VBQPPL hết hiệu lực (Nhóm D), từ suy đoán (Nhóm C), số văn bản đáng ngờ (Nhóm A).
3. **Kiểm trên PDF render**: widow word (Quy tắc 13), khối chữ ký gãy trang (Quy tắc 14).
4. **Xuất ẢNH GHÉP** `/home/claude/work/qa/qa_sheet.png` — mọi trang trong 1 ảnh.

**QA trực quan**: `view` **MỘT ảnh ghép `qa_sheet.png` là đủ** để soi tổng thể (header/số ký hiệu trang đầu, khối chữ ký trang cuối, ngắt trang, tràn lề). Chỉ mở ảnh trang riêng `qa-N.jpg` khi ảnh ghép phát hiện nghi vấn ở trang N, hoặc văn bản > 6 trang cần soi kỹ biểu/tiêu đề bảng lặp. Đây là file QA tạm — KHÔNG xuất PDF cho người dùng.

**Vòng sửa lỗi**: khi FAIL, sửa theo **báo cáo TEXT** trước (đủ căn cứ định vị lỗi), chạy lại `qa_all.py` MỘT lần sau khi đã sửa hết — KHÔNG render/soi ảnh sau từng lỗi nhỏ. Khi tool view ảnh không truyền được nội dung, báo cáo text của `qa_all.py` là đủ căn cứ kết luận. KHÔNG giao file chưa qua `qa_all.py` PASS (hoặc PASS kèm WARN đã được cân nhắc).

`qa_pdf_check.py` vẫn dùng được độc lập khi chỉ cần kiểm 4 mục thể thức; đã có PDF render sẵn thì thêm `--pdf <path>` để khỏi render lại. `validate.py` của skill docx public chỉ cần chạy khi qa_all báo nghi hỏng cấu trúc file.

### Bước 5: Đặt tên file chuẩn & trả file qua present_files

Đặt file vào `/mnt/user-data/outputs/` với **tên file chuẩn** `YYYY.MM.DD. [Tên văn bản].docx` (xem Quy tắc 7) rồi gọi `present_files`. KHÔNG tạo PDF kèm.

## API thư viện `TemplateDoc`

| Method | Mô tả |
|---|---|
| `replace_in_paragraph(idx, pattern, replacement)` | Thay text khớp pattern trong paragraph thứ idx |
| `set_paragraph_text(idx, new_text)` | Đặt toàn bộ text paragraph idx (giữ format run đầu) |
| `replace_in_cell(table_idx, row, col, pattern, replacement)` | Thay text trong ô bảng |
| `replace_in_cell_paragraph(t, r, c, p_idx, pattern, replacement)` | Thay trong 1 paragraph cụ thể của ô bảng |
| `set_cell_paragraph_text(t, r, c, p_idx, new_text)` | Đặt text 1 paragraph trong ô bảng |
| `replace_keeping_first_run(p_idx, new_after, separator=': ')` | Cho paragraph "Điều X:..." — giữ "Điều X" bold, thay phần sau |
| `replace_body_paragraphs(start, end, new_paragraphs)` | Thay nguyên 1 đoạn nhiều paragraph (giữ format paragraph mẫu) |
| `replace_all(pattern, replacement)` | Find & replace trong toàn doc |
| `inspect()` | In cấu trúc paragraph & table để debug |
| `save(path)` | Lưu file |

## Cấu trúc cụ thể từng template
Chi tiết cấu trúc paragraph/table của từng template (chỉ số P/Table để điền đúng) — đọc khi soạn bằng Chế độ A: **`reference/templates-chi-tiet.md`**.

## Thư viện mẫu thật đã ban hành (`examples/`)
17 mẫu thật (`examples/sct/` 11 + `examples/ubnd/` 6) để soạn bằng Chế độ B: bảng "mẫu thật ↔ loại văn bản", người ký/ký hiệu, cấu trúc từng mẫu UBND/VP, lưu ý số liệu — đọc khi chọn mẫu hoặc soạn văn bản cấp UBND/VP: **`reference/thu-vien-mau-that.md`**.
Cốt lõi: ưu tiên mẫu thật trong `examples/` hơn template trắng (Chế độ B); KHÔNG dùng `TemplateDoc` cho file `examples/` (đã điền sẵn, không theo chỉ số paragraph); KHÔNG bê nguyên nội dung vụ việc cũ sang văn bản mới — chỉ kế thừa khung, thể thức, văn phong.

## Công thức & checklist thực chiến
Công thức căn bảng/biểu khổ ngang "vuông vắn" (A4 ngang 9071 DXA, lặp dòng tiêu đề, nền trắng), đồng bộ chéo Báo cáo↔Phụ lục↔VP UBND, toàn vẹn số liệu/metadata, mã người soạn dòng "Lưu" — đọc khi dựng biểu hoặc đồng bộ nhiều file: **`reference/cong-thuc-thuc-chien.md`**.

## Phòng tránh 9 nhóm sai lầm tham mưu (luôn áp dụng)
Áp dụng cho mọi việc soạn/rà soát/góp ý/tham mưu (không chỉ tạo .docx). Tóm tắt dưới đây; checklist đầy đủ + `scripts/check_document.py` + các vụ thật ở **`reference/phong-tranh-sai-lam.md`**.
- **A — Pháp lý:** không điền số/ngày văn bản hay nội dung điều/khoản từ trí nhớ; phải có nguồn hoặc tra cứu, chưa rõ thì ghi "[cần xác minh]". *Vì sai một số văn bản trong tờ trình/phát biểu của Lãnh đạo gây hậu quả nặng.*
- **B — Nhiệm vụ:** mỗi nhiệm vụ đề xuất Sở làm phải truy ngược về 1 câu chỉ đạo / 1 điều khoản / 1 chức năng của Sở (quy tắc 1-1-1); không suy diễn ngoài văn bản chỉ đạo.
- **C — Từ ngữ:** bản trình ký không dùng từ suy đoán ("dự kiến/gần như/có thể/khoảng" khi không có cơ sở); chỉ ở 3 trạng thái: khẳng định (có căn cứ), đề nghị (nêu căn cứ), bảo lưu.
- **D — Hiệu lực:** mọi VBQPPL viện dẫn phải còn hiệu lực; tra trạng thái với VB ban hành trước 2024; đối chiếu danh mục hết hiệu lực theo **NĐ 79/2025** (xem `reference/nd-79-2025-tom-tat.md`). Bảng VB đã thay thế ở file reference.
- **E — PDF:** nguồn là PDF VBHC thì chạy `scripts/extract_metadata.py` đọc số/ngày từ file gốc, không tin context (layout 2 cột); header/tiêu đề không được lọt `<w:br/>`.
- **F — Không rebuild:** người dùng tải .docx lên để sửa tiếp (kể cả file do Claude tạo trước đó) → **sửa trực tiếp file đó**, không chạy lại script build/template cũ; giữa các vòng người dùng thường đã sửa tay trong Word. Chưa diff toàn văn thì mặc định coi là ĐÃ có sửa tay. *Vụ thật: Báo cáo PCCC 01/7/2026 mất 4 chỉnh sửa tay do rebuild.*
- **G — Thể thức từ chỉnh sửa tay:** dòng ngày điền sẵn tháng/năm, để trống ngày; `Lưu: VT, CN (Tên)` có khoảng trắng trước ngoặc; đậm deadline dùng `<w:b/>` chỉ đúng cụm ngày; nghiêng ghi chú "(có văn bản kèm theo)"; Kính gửi ↔ Nơi nhận "Như trên" nhất quán; gửi xã/phường liên quan trực tiếp thì liệt kê rõ xã đó trong đơn vị phối hợp; header cơ quan chủ quản ghi đầy đủ. Chi tiết: `reference/phong-tranh-sai-lam.md` Nhóm G.
- **H — Toàn vẹn thể thức khi thao tác XML/run (4 lỗi thật 05/7/2026):** không gán `run.text` cho run neo shape Line (hàng Số/Ngày header) — sửa qua `w:t`; dòng Số/Ngày 13pt tường minh + ngày nghiêng; không để widow word (1 chữ rơi dòng); khối chữ ký không gãy giữa 2 trang (cantSplit + co giãn văn bản). QA bằng soi ảnh render VÀ `scripts/qa_pdf_check.py`. Chi tiết: `reference/phong-tranh-sai-lam.md` Nhóm H, Quy tắc bất biến 11-14.
- **I — Văn phong CV gửi doanh nghiệp:** không nêu mốc hiệu lực giấy tờ mà DN chưa vi phạm (chỉ nêu nghĩa vụ chung; mốc cụ thể để ở biên bản/phiếu trình nội bộ); không viết "đề nghị liên hệ Phòng ... để được hướng dẫn" — kết thúc ngay tại đoạn đề nghị nộp lại hồ sơ, đầu mối duy nhất là Trung tâm Phục vụ hành chính công tỉnh. *(Bạn chốt 24/7/2026.)*

## Đọc PDF văn bản đến — trích metadata chính xác

> ### CẢNH BÁO CỨNG — làm trước mọi việc khác
> Nhận file PDF có dấu hiệu là văn bản nhà nước VN (tên file CV/QĐ/TTr/BC/KH/NQ/NĐ/TT/UBND/SCT…; dòng đầu "ỦY BAN NHÂN DÂN/BỘ/SỞ/HĐND/CHÍNH PHỦ"; hoặc bối cảnh "công văn đến") → **DỪNG mọi thao tác khác** và chạy ngay:
> ```bash
> python3 "/mnt/skills/plugins/vbhc-vn:vbhc-vn/scripts/extract_metadata.py" "<đường dẫn file>" # nếu cài dạng user skill thì thay bằng /mnt/skills/user/vbhc-vn/scripts/
> ```
> *Vì sao:* PDF VBHC có layout 2 cột; số/ngày/người ký là text-box độc lập, khi nạp vào context thường bị bỏ trống hoặc nối sai thứ tự → **context KHÔNG đáng tin**. Ô "Số: /…" hay "ngày … tháng …" trống là **tín hiệu phải đọc đĩa**, không phải kết luận "nháp chưa cấp số" (hai thứ hiển thị y hệt nhau). Bỏ qua đã gây ≥2 vụ dẫn chiếu sai (CV 3861/UBND-NC; CV 3954/UBND-VX). Chi phí ~2 giây.

Cờ kích hoạt, OCR fallback (`ocrmypdf`), 11 trường output JSON, chức vụ ký (KT./TM./TUQ./TL.), khi nào chạy lại — chi tiết: **`reference/doc-pdf-metadata.md`**.

## Quy tắc bất biến

1. **KHÔNG bao giờ sinh văn bản từ đầu bằng code khi đã có mẫu/file gốc** — Chế độ A: mở mẫu trong `templates/`; Chế độ B: sửa trực tiếp file người dùng tải lên (unpack→XML→pack), giữ nguyên định dạng gốc.
2. **KHÔNG động vào structure tables** (header table, footer signature table) — chỉ thay text trong cells.
3. **KHÔNG xóa/thêm paragraph trong giữa table cells** — chỉ thay text.
4. **Khi thay text trong paragraph có "Điều X" bold**: dùng `replace_keeping_first_run` (không dùng `set_paragraph_text`).
5. **KHÔNG giao PDF cho người dùng** — sản phẩm cuối chỉ là .docx. (Được phép render PDF/JPG **nội bộ** để QA trực quan ở Bước 4, nhưng không `present_files` file PDF đó.)
6. **Người ký mặc định**:
   - **Chọn PGĐ ký theo LĨNH VỰC** (phân công cắt ngang phòng — xem bảng đầy đủ trong `sct-laocai-org-vn` mục "Phân công lĩnh vực giữa các Phó Giám đốc"):
     - **PGĐ Nguyễn Đình Chiến** ký: **KCN, CCN, ATTP** (vd QĐ/GCN ATTP, CV/BC về cụm công nghiệp).
     - **PGĐ Hoàng Văn Thuân** ký: **HHNH (vận chuyển hàng nguy hiểm), hóa chất, VLNCN, tiền chất thuốc nổ, khoáng sản, môi trường, PCCC, khoa học (KHCN), ATVSLĐ, năng lượng, thương mại** (vd GP vận chuyển HHNH, văn bản hóa chất/VLNCN, PCCC).
     - Lĩnh vực QLCN chưa nêu tên: mặc định PGĐ Nguyễn Đình Chiến (phụ trách phòng) hoặc hỏi lại.
   - TTr UBND tỉnh, KH quan trọng, QĐ/BC quan trọng → **GIÁM ĐỐC Hoàng Chí Hiền**.
   - Khi PGĐ phụ trách vắng, PGĐ còn lại ký thay (nêu rõ để người dùng xác nhận, không mặc định cứng).
   - **Ngoại lệ - Công văn nội bộ Phòng (template 08)**: do **Trưởng phòng** ký (mặc định Trưởng phòng QLCN Nguyễn Hữu Long), không phải Lãnh đạo Sở; header không có số ký hiệu, dòng lưu chỉ `Lưu: CN (...)`.
   - **Văn bản cấp UBND tỉnh / VP UBND (examples/ubnd)**: người ký là Lãnh đạo UBND tỉnh hoặc Văn phòng UBND tỉnh (KT. CHỦ TỊCH - PHÓ CHỦ TỊCH; TL. CHỦ TỊCH - KT. CHÁNH VĂN PHÒNG - PHÓ CHÁNH VĂN PHÒNG; CHÁNH VĂN PHÒNG; TM. ỦY BAN NHÂN DÂN TỈNH - CHỦ TỊCH). Xem mục "Văn bản cấp UBND tỉnh và Văn phòng UBND tỉnh".
7. **Tên file chuẩn**: đặt theo định dạng `YYYY.MM.DD. [Tên văn bản].docx` — tiền tố ngày (năm.tháng.ngày), một dấu chấm và khoảng trắng, rồi tên văn bản đầy đủ bằng tiếng Việt **có dấu**.
   - Ví dụ: `2026.06.19. Báo cáo tổng kết triển khai cụm công nghiệp.docx`
   - Ví dụ: `2026.05.15. Công văn báo cáo tiến độ thẩm định CCN An Thịnh.docx`
   - Ngày trong tên file = ngày ban hành ghi trên văn bản (không phải ngày tạo file). Nếu chưa rõ ngày ban hành thì dùng ngày dự kiến ký.
8. **Căn chỉnh đều đẹp, đồng bộ đánh số trước khi xuất file**: văn bản cần được căn chỉnh đều đẹp và đồng bộ danh mục đánh số thứ tự các mục trước khi xuất file. Hệ thống đề mục phải đánh số liên tục, không nhảy bậc, đúng cấp (I, II, III → 1, 2, 3 → a, b, c hoặc 1.1, 1.2); canh lề, thụt đầu dòng và khoảng cách đoạn nhất quán. Thực hiện rà soát này ở Bước 4, trước khi `save`.
9. **In nghiêng các đầu mục chữ cái a), b), c)…**: ở cấp đề mục thấp nhất dùng chữ cái thường (a), b), c), d)…), phần **nhãn chữ cái cùng tiêu đề ngắn của mục** in **nghiêng đứng (italic), không đậm** — để phân biệt với cấp trên (I, II, III và 1, 2, 3 in **đậm đứng**, không nghiêng). Áp dụng đồng bộ cho mọi mục a), b), c)… cùng cấp trong toàn văn bản (đúng kiểu đã chỉnh ở báo cáo CCN). Lưu ý: chỉ in nghiêng nhãn + tiêu đề đầu mục; phần nội dung diễn giải phía sau vẫn để đứng bình thường.
10. **TUYỆT ĐỐI KHÔNG chèn ngắt dòng cứng (`\n`/`<w:br/>`) vào trong một paragraph — đặc biệt ở header/tiêu đề** (lỗi tái diễn, đã được khóa ở tầng code):
   - **Triệu chứng**: dòng V/v, tên cơ quan, "Lào Cai, ngày... tháng... năm", tiêu đề bị ngắt giữa cụm từ thành các dòng ngắn xấu (vd `V/v ... Kế / hoạch phát / triển y dược cổ / truyền ...`).
   - **Nguyên nhân**: truyền chuỗi có `\n` vào trường header/tiêu đề (vd `'V/v ...Kế hoạch phát\ntriển...'`). `python-docx` tự chuyển `\n` trong `run.text` thành `<w:br/>` → ngắt dòng cứng sai chỗ.
   - **Quy tắc**: trong VBHC, một paragraph KHÔNG bao giờ chứa ngắt dòng cứng. Mọi việc "xuống dòng" phải tách thành **paragraph riêng** (mỗi dict `{text:...}` trong `replace_body_paragraphs`, hoặc nhiều paragraph trong ô bảng). Trường V/v, ngày tháng, tên cơ quan luôn truyền **một chuỗi liền**, để Word **tự wrap** theo bề rộng cột — không tự ngắt thủ công.
   - **Tầng phòng vệ tự động**: hàm `_norm_inline()` trong `scripts/fill_template.py` đã tự chuẩn hóa mọi `\n`/`\r` thành 01 dấu cách ở mọi lần ghi text (`_set_paragraph_text`, `_replace_text_in_paragraph`), nhưng **vẫn giữ nguyên các chuỗi nhiều dấu cách căn chỉnh có chủ đích** (vd `Số:        /SCT-CN`, `ngày      tháng 6 năm 2026`). Dù vậy, vẫn phải tuân thủ quy tắc trên khi soạn — không ỷ lại guard.
   - **QA bắt buộc**: ở Bước 4, kiểm tra số `<w:br/>` trong các ô header phải bằng 0 (xem script `check_document.py` — đã dò lỗi này). Nhìn ảnh render trang 1: V/v phải wrap mềm theo cột, không gãy giữa cụm từ.
11. **TUYỆT ĐỐI không gán `run.text` cho run trong hàng Số/Ngày của header** (lỗi thật 05/7/2026 — làm mất đường Line dưới Tiêu ngữ): hai đường Line của header thường được NEO (anchor) trong run0 của paragraph "Số: .../..." và "Lào Cai, ngày...". Setter `run.text = ...` của python-docx **xóa toàn bộ phần tử con của `<w:r>`, kể cả `mc:AlternateContent` chứa shape Line và mất luôn định dạng nghiêng/cỡ chữ**. Quy tắc thao tác an toàn:
   - Trước khi sửa bất kỳ run nào trong header, kiểm tra run có chứa shape không: `list(run._r.iter(qn('w:drawing'))) + list(run._r.iter(qn('w:pict')))` — chú ý dùng `iter()` (shape bọc trong `mc:AlternateContent`, `findall` trực tiếp KHÔNG thấy).
   - Sửa text của paragraph có shape: chỉ sửa qua node `w:t` (`for t in p._p.iter(qn('w:t')): ...`), không gán `run.text`, không xóa run. Lưu ý text có thể tách run (vd "tháng" và "6" là 2 `w:t` riêng) — tìm node theo ngữ cảnh node liền trước.
   - Nếu paragraph đã lỡ hỏng: deep copy nguyên `<w:p>` từ file gốc/mẫu thật thay thế, rồi mới sửa `w:t`.
   - QA: trước khi xuất, đếm shape trong file (`document.xml` phải còn đủ số `<w:pict`/`<w:drawing` như file gốc; công văn SCT chuẩn = 2 Line header).
12. **Dòng "Số: .../..." và dòng "Địa danh, ngày ... tháng ... năm ..." cỡ 13pt tường minh, dòng ngày in nghiêng**: đặt `w:sz`/`w:szCs` = 26 trực tiếp trên run (không dựa vào kế thừa style Normal 14pt); dòng ngày giữ `<w:i/>`. Khi copy mẫu thật mà mẫu chưa đặt tường minh thì bổ sung.
13. **Không để 1 chữ đơn độc rơi xuống dòng (widow word)** — trong ô V/v của header lẫn mọi đoạn nội dung: co chữ bằng character spacing condensed (`w:spacing` trong `rPr`, giá trị âm, thường -4 đến -8 twentieths of a point) để chữ lẻ lên dòng trên, hoặc nới cho 2-3 chữ cùng xuống. QA tự động sau render: quét PDF bằng `pdftotext -layout` tìm dòng chỉ có 1 từ đứng cuối đoạn (xem `scripts/qa_pdf_check.py`).
14. **Khối chữ ký không được gãy giữa 2 trang** (chức danh một trang, tên người ký trang sau): (a) đặt `<w:cantSplit/>` trong `trPr` của hàng bảng chữ ký để hàng không bị tách; (b) nếu cantSplit đẩy cả khối sang trang mới để lại trang trước hụt, thì **co giãn toàn văn bản** cho khối ký về nằm trọn trang trước: giảm space before/after các đoạn body 6pt → 4pt (hoặc 3pt), có thể bớt 1-2 paragraph trống trong khối ký (giữ tối thiểu 4 dòng trống cho chữ ký tay); (c) QA phân trang bằng `pdftotext`: tên người ký phải cùng trang với "KT. GIÁM ĐỐC"/"TM. ..." (xem `scripts/qa_pdf_check.py`).

15. **Unicode NFC/NFD — so khớp text file docx PHẢI chuẩn hóa NFC hai phía** (vụ thật 09/7/2026 — CV Yên Hợp gửi Sở Tài chính): nhiều file mẫu thật lưu tiếng Việt dạng **NFD** (dấu tách rời: `ị` = `i` + `U+0323`) trong khi chuỗi Claude gõ là NFC → `pattern in text` trượt. `fill_template.py` đã NFC-normalize sẵn ở tầng `_replace_text_in_paragraph`; khi tự viết code so khớp/assert ngoài TemplateDoc (grep nội dung, kiểm tra forbidden strings...), LUÔN `unicodedata.normalize('NFC', ...)` cả hai phía.
16. **Mọi lệnh replace là BẮT BUỘC KHỚP, thất bại phải nổ to** (cùng vụ 09/7/2026: `replace_in_cell` trượt im lặng → trích yếu V/v vụ nổ mìn cũ lọt ra bản trình ký dù QA thể thức PASS): `replace_in_cell`/`replace_in_paragraph` từ v2.2.0 mặc định `required=True` — pattern không khớp là raise `ValueError` kèm text thật để sửa pattern ngay. Chỉ truyền `required=False` khi pattern là tùy chọn CÓ CHỦ ĐÍCH. KHÔNG bọc try/except để nuốt lỗi này.
17. **QA nội dung bằng `--forbid`/`--require` là BẮT BUỘC với Chế độ B trên mẫu thật** (chốt chặn thứ hai, độc lập với assertion trong build script): 
   ```bash
   python3 scripts/qa_all.py output/<file>.docx \
     --forbid "<trích yếu vụ cũ>" "<tên DN cũ>" "CN(<tên người soạn cũ>)" "<người ký cũ nếu khác>" \
     --require "<số CV đến>" "<ngày CV đến>" "CN(<tên người soạn mới>)" "<người ký mới>"
   ```
   Danh sách forbid tối thiểu = các chuỗi đặc trưng của vụ việc trong mẫu gốc (đọc mẫu trước khi build là có ngay); require tối thiểu = số/ngày văn bản đến, `CN(tên)`, tên người ký. Thể thức PASS ≠ nội dung đúng — hai tầng kiểm khác nhau.
18. **Người soạn thảo trong dòng Lưu = CHUYÊN VIÊN phụ trách lĩnh vực, KHÔNG mặc định CN(Trang)** (cùng vụ 09/7/2026): tra bảng "Chuyên viên ↔ lĩnh vực tham mưu" trong `sct-laocai-org-vn` (vd CCN/KCN → **Lê Quang Trung** → `CN(Trung)`; HHNH → theo bảng; ATTP → theo bảng). `CN(Trang)` CHỈ dùng khi Bạn (PTP) nói rõ tự soạn. Không rõ lĩnh vực của ai → hỏi, không đoán.
19. **Văn bản đến là PDF (kể cả đã thấy nội dung trong context) → PHẢI chạy `extract_metadata.py` TRƯỚC khi dẫn chiếu số/ngày** (cùng vụ 09/7/2026: context hiển thị "Số: /UBND-KT" trống, đĩa có đủ **857/UBND-KT ngày 08/7/2026**): ô số/ngày trống trong context là tín hiệu ĐỌC ĐĨA, không phải bằng chứng "văn bản chưa cấp số". Nếu script cũng không đọc được số → để trống và NÓI RÕ với Bạn, không tự điền "số .../...".
20. **TUYỆT ĐỐI KHÔNG đặt chiều cao dòng cố định `<w:trHeight>` cho bảng nội dung — để dòng tự co theo nội dung** (vụ thật 24/7/2026 — Biên bản thẩm định HHNH Công ty CP thương mại vận tải và tư vấn kỹ thuật, bảng "Lái xe" bị đẩy nguyên khối sang trang sau, trang trước bỏ trắng nửa trang):
   - **Triệu chứng**: giữa một đề mục (vd `- Lái xe:`) và bảng ngay dưới nó xuất hiện khoảng trắng lớn; bảng nhảy sang trang sau. Nhìn trong Word tưởng là "thừa dòng trống", nhưng soi XML thấy `</w:p><w:tbl>` liền nhau — KHÔNG có paragraph trống nào.
   - **Nguyên nhân**: mỗi `<w:tr>` bị gán `<w:trHeight w:val="..."/>` (chiều cao tối thiểu cố định) — thường do bê nguyên bảng từ file doanh nghiệp gửi, hoặc do Word ghi lại khi ai đó kéo tay chiều cao dòng. Cộng thêm `<w:cantSplit/>` (không cho tách dòng qua trang), cụm "dòng tiêu đề + dòng dữ liệu đầu tiên" cao hơn phần giấy còn lại → Word đẩy CẢ bảng sang trang mới. Chiều cao cố định còn làm dòng phình thêm dù nội dung ngắn.
   - **Quy tắc**: Chế độ A (dựng mới) KHÔNG BAO GIỜ ghi `<w:trHeight>`. Chế độ B (sửa mẫu thật / file doanh nghiệp) phải **gỡ sạch `<w:trHeight>` trong mọi bảng nội dung**. **Hai ngoại lệ duy nhất**: (a) **bảng header** (bảng số 1: tên cơ quan ↔ Quốc hiệu) — giữ nguyên như mẫu thật đã kiểm chứng, không đụng; (b) cần chừa chỗ ký tay/điền tay → dùng **paragraph trống trong ô**, KHÔNG dùng `trHeight`.
   - **Gỡ rồi vẫn hụt** (nội dung ô thật sự cao): siết giãn dòng TRONG Ô BẢNG về giãn đơn — `<w:spacing w:after="0" w:line="300" w:lineRule="exact"/>` cho chữ 13pt (`w:sz` 26), `320` cho chữ 14pt — thay cho 360 của phần thân văn bản. Mốc an toàn: cụm "dòng tiêu đề + dòng dữ liệu đầu" **≤ 6 cm** thì luôn bám được vào cuối trang trước. Giữ nguyên `<w:cantSplit/>`; KHÔNG gỡ cantSplit để "cho nó tự tách" — dòng bị xẻ đôi qua trang còn xấu hơn khoảng trắng.
   - **Lệnh gỡ nhanh (Chế độ B, đúng 1 bảng theo chỉ số, 0-based)**:
     ```python
     import re
     p = 'unpacked/word/document.xml'; idx = 3          # bảng thứ 4
     x = open(p, encoding='utf-8').read()
     s = [m.start() for m in re.finditer(r'<w:tbl>', x)][idx]
     e = [m.end()   for m in re.finditer(r'</w:tbl>', x)][idx]
     seg = re.sub(r'<w:trHeight[^/]*/>', '', x[s:e])                       # gỡ chiều cao cố định
     seg = seg.replace('w:line="360"', 'w:line="300"')                     # (nếu cần) siết giãn dòng trong ô
     open(p, 'w', encoding='utf-8').write(x[:s] + seg + x[e:])
     ```
   - **QA bắt buộc**: `check_document.py` nhóm **[F]** đếm `<w:trHeight>` theo từng bảng — bảng số 2 trở đi phải bằng 0. Sau render, soi ảnh ghép: không trang nào được kết thúc bằng một đề mục rồi bỏ trắng quá 3 dòng.

## Demo có sẵn

Trong `scripts/`:
- `demo_cong_van.py` — Tạo công văn báo cáo tiến độ thẩm định CCN An Thịnh
- `demo_to_trinh.py` — Tạo Tờ trình phê duyệt Quy hoạch CCN Y Can
- `demo_quyet_dinh.py` — Tạo QĐ thành lập Đoàn thẩm định ATTP cho Cty Hùng Sơn

Đọc các demo này khi cần ví dụ cụ thể về cách sửa từng loại văn bản.
