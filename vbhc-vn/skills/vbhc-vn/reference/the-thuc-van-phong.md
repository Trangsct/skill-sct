# Thể thức, văn phong và rà soát — quy ước cố định của Bạn

Tách khỏi `SKILL.md` ngày 16/9/2026 (bản 2.23.0). Nội dung giữ nguyên.

Đọc file này khi: băn khoăn quy cách một thành phần thể thức, chọn ký hiệu văn bản, đặt tên
file, hoặc khi soạn một loại văn bản có quy ước riêng (công văn nội bộ Phòng, giấy mời, QĐ
cá biệt, GCN ATTP, biên bản). Căn cứ gốc đầy đủ ở `reference/nd30-phu-luc-1-the-thuc.md`.

## Thể thức, văn phong và rà soát (quy ước cố định của Bạn — hợp nhất từ bộ nhớ)

Áp dụng cho MỌI văn bản soạn/sửa trong skill này.

### Thể thức trình bày (VBHC thường — theo NĐ 30/2020)
Căn cứ gốc đầy đủ nằm ở `reference/nd30-phu-luc-1-the-thuc.md` (thể thức từng thành phần), `nd30-phu-luc-2-viet-hoa.md` (viết hoa), `nd30-phu-luc-3-viet-tat-mau.md` (viết tắt tên loại VB) — tra khi có điểm chưa chắc, KHÔNG suy đoán quy cách. Các dòng dưới là quy ước đã chốt áp dụng hằng ngày:
- **Font** Times New Roman, **cỡ 14**. **Lề A4**: trên/dưới 20mm, trái 30mm, phải 20mm. Line spacing single; before/after 6pt; **first line indent 1cm**; **căn đều (justify)**. TẤT CẢ đoạn nội dung và đề mục lùi đầu dòng **đồng nhất**, **không thụt treo**. Khi dựng bằng code: dùng **một hàm định dạng đoạn duy nhất**, KHÔNG đặt riêng firstLine=0 cho đề mục; số thứ tự viết liền đầu dòng (không dùng numbering treo). *(Kiểm tự động: **R12** lề, **R13** lùi đầu dòng — `scripts/qa_rules.py`.)*
- Bố cục đủ: Quốc hiệu/Tiêu ngữ, tên cơ quan, số ký hiệu, địa danh-ngày, trích yếu, nội dung, nơi nhận, chữ ký.
- **Header bắt buộc vẽ đường kẻ ngang bằng ĐỐI TƯỢNG LINE (Insert > Shapes > Line)** ở CẢ HAI bên: dưới tên cơ quan ban hành (vd "SỞ CÔNG THƯƠNG", "PHÒNG QUẢN LÝ CÔNG NGHIỆP") và dưới "Độc lập – Tự do – Hạnh phúc"; căn giữa, dài ~1/2 ô (3-5cm), là đường kẻ thật chọn/di chuyển được. Không dùng ký tự gạch chân (underscore) cũng không dùng paragraph border — *vì sao:* underscore và border không phải đối tượng vẽ, không căn giữa/chỉnh độ dài được và dễ lệch khi sửa nội dung. Khi dựng .docx bằng code: tạo đường kẻ dưới dạng line drawing object (VML `<v:line>` nổi, căn giữa theo lề: `mso-position-horizontal:center;mso-position-horizontal-relative:margin`, hoặc DrawingML) — mã sẵn ở `reference/the-thuc-code.md`; render ra ảnh kiểm tra đường kẻ hiển thị đúng trước khi xuất.
- **Quốc hiệu "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM" (HÒA, không "HOÀ"); tiêu ngữ dùng EN DASH "–"**. File người dùng tải lên: chạy `python3 scripts/fix_quoc_hieu.py <file.docx>` ngay sau build. **Dòng "Kính gửi:" KHÔNG in đậm.** *(Kiểm tự động: tag `QUOCHIEU` + **R09**; **R04** cho khối Kính gửi.)*
- **Không dùng màu nền/shading** cho bất kỳ ô/dòng/bảng nào — bảng nền trắng, chỉ viền đen mảnh. *Vì sao:* VBHC chuẩn dùng nền trắng; shading dễ lệch màu, khó đọc khi in/photocopy.
- Cột Quốc hiệu được phép rộng vượt tỷ lệ chuẩn để Quốc hiệu nằm gọn trên 1 dòng. Đoạn bị lẻ 1 chữ ở dòng cuối: co khoảng cách chữ (character spacing/condensed) để tránh.
- **KHÔNG bao giờ chèn ngắt dòng cứng `\n`/`<w:br/>` trong một paragraph** (xem Quy tắc bất biến 10) — V/v, tên cơ quan, ngày tháng để chuỗi liền, Word tự wrap.
- **Số mũ đơn vị đo (m³, m², cm²) BẮT BUỘC là superscript thật** — không để "m3/m2" số thường (lỗi lặp nhiều lần, PTP Trang nhắc 29/7/2026). Khi sửa bằng code: tách chữ số mũ thành run riêng kế thừa nguyên rPr + `<w:vertAlign w:val="superscript"/>`; rà toàn văn (cả bảng) bằng regex `m[23](?!\d)` trước khi xuất; kiểm nhanh trên bản render — tesseract đọc thành "m°"/"m?" là dấu hiệu superscript đã ăn.

### VBQPPL (QĐ UBND, NQ HĐND) — KHÔNG dùng NĐ 30/2020
Theo **NĐ 78/2025 + NĐ 187/2025**. Lề trên/dưới/phải 15-20mm, trái 30-35mm. Quốc hiệu/Tiêu ngữ/Tên CQ 12-14 đậm; số ký hiệu CÓ năm (.../2026/QĐ-UBND); CĂN CỨ cỡ 14 nghiêng; nội dung 13-14 lùi 1-1.27cm; Điều đậm; Nơi nhận 12 nghiêng đậm. QĐ UBND QPPL trực tiếp theo **Mẫu 19** (NĐ 78/2025 PL III): có dòng "Ủy ban nhân dân tỉnh ban hành Quyết định..." nghiêng, sau căn cứ, trước "QUYẾT ĐỊNH:".

### Văn phong & viết tắt
- Phong cách hành chính: KHÔNG ký tự đặc biệt, emoji, dấu sao (*); không dùng `*` để in đậm/gạch đầu dòng.
- Trong nội dung chính (trừ tiêu đề và dòng "Kính gửi"): **viết tắt ngay từ lần đầu**: Ủy ban nhân dân→UBND; Hội đồng nhân dân→HĐND; Mặt trận Tổ quốc→MTTQ; trách nhiệm hữu hạn→TNHH (kể cả trong tên DN: "Công ty TNHH..."). "Quốc hội" giữ nguyên.
- Đơn vị diện tích: luôn **"ha"**, KHÔNG "héc-ta"/"hecta" — kể cả nội dung cho truyền hình/đại chúng.
- Địa danh cũ của Yên Bái (Âu Lâu, Trấn Yên, Văn Chấn, Nghĩa Lộ, Mù Cang Chải, Trạm Tấu, Lục Yên, Văn Yên, Yên Bình...) nay thuộc **tỉnh Lào Cai** (từ 1/7/2025) — ghi "tỉnh Lào Cai".

### Ký hiệu, người soạn, tên file, định dạng xuất
- **Ký hiệu**: Công văn `SCT-CN`; Tờ trình `TTr-SCT`; Báo cáo `BC-SCT`; Kế hoạch `KH-SCT`; QĐ cá biệt `QĐ-SCT`; Giấy phép `GP-SCT`; GCN ATTP `.../{năm}/GCNATTP-SCTLC`. Dòng lưu: `Lưu: VT, CN (Tên).` *(Kiểm tự động: **R07**; thứ tự Nơi nhận khi gửi doanh nghiệp: **R06**.)* Văn bản do Bạn (PGĐ Chiến, phụ trách QLCN) yêu cầu **luôn dùng `SCT-CN` + `Lưu: VT, CN(tên)`**, kể cả khi nội dung thuộc lĩnh vực phòng khác — KHÔNG đổi sang ký hiệu phòng khác.
- **Tên file**: `năm.tháng.ngày. Trích yếu` tiếng Việt CÓ DẤU (vd `2026.06.19. Báo cáo tổng kết...`). Ngày = ngày ban hành/dự kiến ký, không rút gọn tùy tiện ("v2", "final").
- **CHỈ tạo file Word (.docx), KHÔNG kèm PDF**.

### Rà soát/review — các lỗi KHÔNG được báo (đã thống nhất)
- KHÔNG báo lỗi **thiếu số ký hiệu** ("Số: .../...") đối với file Word (số do văn thư cấp sau).
- KHÔNG báo lỗi **"thiếu chữ NAM"** trong Quốc hiệu và KHÔNG tự thêm "NAM" — nếu công cụ trích xuất hiển thị Quốc hiệu kết thúc ở "...VIỆT", đó là lỗi hiển thị phía Claude (NAM nằm ở run/dòng khác), không phải văn bản thiếu chữ.
- Khi trích metadata PDF: nếu không đọc được người ký, KHÔNG cần OCR lại — chỉ cần số văn bản + ngày là đủ.

### Sửa file SAU khi QA — hai bẫy đã trả giá (vụ Thành Hương 29-30/7/2026)
- **Gán `run.text = ...` (python-docx) xóa TOÀN BỘ nội dung run, kể cả shape `v:line`/`w:pict` nằm trong run** — điền "tháng 7" vào ô ngày đã làm mất đường kẻ dưới "Độc lập – Tự do – Hạnh phúc" của dự thảo GP dù QA trước đó PASS. Trước khi gán text vào đoạn thuộc bảng header (ô ngày, ô quốc hiệu, ô tên cơ quan): grep `<w:pict`/`v:line` trong đoạn; nếu có, chỉ sửa phần tử `w:t` trong XML hoặc trích nguyên khối run chứa pict từ mẫu gốc chèn trả lại.
- **Mọi chỉnh sửa sau lần QA PASS — dù chỉ một ô ngày — phải chạy lại `qa_all.py` và render soi lại**; khoảng hở "sửa nhẹ khỏi QA" chính là nơi lỗi lọt ra bản giao cho người dùng.
- Khi nghi ngờ thể thức mà không soi được ảnh: **đối chiếu pixel với bản ký thật** — render cả hai cùng 120 dpi, dò các đoạn kẻ ngang (ngưỡng xám < 175, đoạn liên tục ≥ 30 px, liệt kê MỌI đoạn mỗi hàng chứ không chỉ đoạn dài nhất) rồi so tọa độ; đo đậm/thường bằng tỉ lệ mực hai vùng TRÊN CÙNG MỘT DÒNG (nhãn vs nội dung), không so giữa các dòng khác cấu trúc.

### Một số loại có quy ước riêng (tóm tắt; chi tiết ở mục template/examples)
- **Công văn nội bộ Phòng - tham gia ý kiến (phong cách chốt 21/8/2026, thay kiểu cũ của mẫu KCN Phú Xuân)**: người ký **TRƯỞNG PHÒNG Nguyễn Hữu Long**; thân gồm đề mục đậm `1.` (hiện trạng/bối cảnh hoặc phạm vi) và `2.` (ý kiến), **KHÔNG có đề mục "3. Kết luận"** — kết luận là đoạn thường cuối; ý kiến trong mục 2 trình bày **gạch đầu dòng nhãn nghiêng `- Về ...:`** (không dùng a) b) c)). Hồ sơ trải nhiều lĩnh vực → mục 1 đổi thành "Về phạm vi tham gia ý kiến": chỉ rõ nội dung nào thuộc cơ quan/phòng nào và ghi thành văn "không tham gia ý kiến đối với các nội dung thuộc trách nhiệm của cơ quan, đơn vị khác". **Bộ 4 lớp bảo vệ pháp lý** khi phải chấp thuận phương án bất lợi cho lĩnh vực Phòng quản lý: ghi nhận quan điểm nhất quán của Phòng tại các cuộc họp trước đó; quy nguồn lý do thay đổi cho ý kiến các đơn vị liên quan; quy trách nhiệm tính chính xác của hồ sơ, số liệu cho chủ đầu tư/đơn vị tư vấn/đơn vị đăng ký; chốt "phương án tối ưu tại thời điểm hiện nay" kèm điều kiện theo dõi tiếp. Hai mẫu thật: `cong-van-noi-bo-phong-tham-gia-y-kien-tuyen-110kv-qua-ccn.docx` và `...-thu-hoi-cat-long-ho.docx` (chi tiết ở `reference/thu-vien-mau-that.md`).
- **Giấy mời họp `SCT-GM`**: văn bản độc lập, không tham chiếu cuộc họp trước, các thành phần bình đẳng, không ghi "mời thêm"; kết cấu 4 mục (Thành phần; Thời gian; Địa điểm; Nội dung).
- **QĐ cá biệt SCT**: "QUYẾT ĐỊNH" + "Về việc..."; "GIÁM ĐỐC SỞ CÔNG THƯƠNG" in hoa đậm căn giữa; căn cứ in nghiêng; cuối căn cứ "Theo đề nghị của Trưởng phòng Quản lý công nghiệp,"; "QUYẾT ĐỊNH:" đậm; Điều 1, 2, 3 đậm.
- **GCN ATTP**: KHÔNG có số góc trái; Quốc hiệu căn giữa toàn trang; số cấp `.../{năm}/GCNATTP-SCTLC` đặt dưới bảng; hiệu lực 3 năm; kèm phụ lục danh mục.
- **Biên bản (làm việc, kiểm tra)**: mở đầu Quốc hiệu căn giữa, **KHÔNG cấp số**; đường gạch chân ngang dưới Quốc hiệu vẽ bằng ĐỐI TƯỢNG LINE (shape) căn giữa — không dùng character underline, không dùng paragraph border. Có **template trắng `templates/09-bien-ban.docx`** (Chế độ A) và 2 mẫu thật `bien-ban-lam-viec-lien-nganh-ccn.docx`, `bien-ban-kiem-tra-thuc-te-hhnh.docx` trong `examples/sct/` (Chế độ B — ưu tiên khi có vụ việc tương tự).
