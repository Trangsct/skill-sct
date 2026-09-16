# Văn bản thể thức Đảng và bộ văn bản cá nhân đảng viên sau giám sát (Bạn chốt 16/9/2026)

Nguồn: bộ 4 văn bản cho Trưởng phòng QLCN sau khi Đoàn giám sát BTV Đảng ủy UBND tỉnh (QĐ 580-QĐ/ĐU ngày 07/8/2026) thông qua dự thảo Báo cáo kết quả giám sát 04 đảng viên. Bạn duyệt qua 4 lượt sửa; các quy ước dưới đây là bản chốt. Script dựng chuẩn: `scripts/build_vb_dang.js` (docx-js, không có nội dung cá nhân — đổi tên, chi bộ, nội dung khi dùng).

## 1. Thể thức văn bản của Đảng (khác NĐ 30/2020)

- KHÔNG có Quốc hiệu, tiêu ngữ. Góc phải: **ĐẢNG CỘNG SẢN VIỆT NAM** in hoa đậm 13pt, dưới là **một đường gạch ngang đúng bằng và cân với dòng chữ** (paragraph border top, indent trái/phải cân — trong script: `left:880,right:1020` trên ô rộng 5000 dxa, đã soi ảnh khớp; sai lệch vài chục dxa đã nhìn thấy lệch). Dưới đường kẻ: `Lào Cai, ngày … tháng … năm 2026` in nghiêng 13pt.
- Góc trái: cơ quan cấp trên (`ĐẢNG BỘ SỞ CÔNG THƯƠNG TỈNH LÀO CAI`, thường 13pt), dưới là đơn vị ban hành in đậm (`CHI BỘ SỐ 2`), dưới nữa là dấu `*`. Văn bản cá nhân đảng viên KHÔNG có dòng Số.
- Tên loại văn bản (BÁO CÁO, KẾ HOẠCH) in hoa đậm; trích yếu ngay dưới in đậm, **viết hoa chữ cái đầu** ("Kết quả khắc phục…", không "kết quả khắc phục…"). Trích yếu dài quá 1 dòng → **tự chia dòng thủ công cho cân số chữ** (dòng 1 nội dung chính, dòng 2 "của Ban Thường vụ Đảng ủy UBND tỉnh"); dòng căn cứ in nghiêng dưới trích yếu cũng chia cân, **không để dòng lẻ 1-2 chữ** kiểu "UBND tỉnh)".
- Khối ký cá nhân: `NGƯỜI BÁO CÁO` đậm căn giữa, 3 dòng trống, họ tên đậm; bên trái `Nơi nhận:` (đậm nghiêng 12pt) + các dòng 11pt: Như trên; Đảng ủy Sở Công thương; Chi ủy Chi bộ số …; Lưu: cá nhân. Hàng ký `cantSplit`, đoạn "Trên đây là…" `keepNext` để khối ký không rơi một mình sang trang mới.
- Thân văn bản vẫn theo quy ước chung: Times New Roman 14, căn đều, giãn dòng 1,3-1,5, **mọi đoạn thân (kể cả đề mục I, II; mục 1, 2; gạch đầu dòng) lùi đầu dòng đồng đều 1,27 cm** — Bạn bác bản có đoạn lùi, đoạn sát lề ("lệch lạc, xô lệch, lùi tiến dòng không đồng đều"). Chỉ tiêu đề, khối Kính gửi, Nơi nhận, khối ký không lùi.

## 2. Khối Kính gửi (chốt 16/9/2026)

- "Kính gửi:" và tên các cơ quan **thẳng cột** bằng tab + hanging indent (đây là ngoại lệ có chủ đích của quy tắc "không thụt treo" — chỉ áp dụng cho khối Kính gửi): đoạn 1 `indent:{left:off,hanging:1560}` + tab stop `off`, text `Kính gửi:\t- Cơ quan 1;`; các đoạn sau `indent:{left:off}`.
- **Cả khối đặt cân giữa trang**, không sát lề trái. Bề rộng thân 9300 dxa: dòng gửi ngắn (≈ 4 000 dxa) → `off = 3760`; dòng dài hơn thì giảm `off` (2 500-3 200) sao cho mỗi cơ quan **đúng 1 dòng, không gãy thành 3 dòng**. Chia lại nội dung dòng nếu cần thay vì để gãy.
- Kính gửi 1 nơi ở VBHC thường vẫn theo Nhóm G (1 dòng căn giữa); quy ước này dành cho ≥ 2 nơi và cho văn bản thể thức Đảng.

## 3. Bản xuất bản không để chỗ trống

- **Cấm để "……", "…/…/2026", "(nêu số liệu)"** trong file giao xuất bản. Văn bản cá nhân được lược căn cứ: viết thẳng "Thực hiện Thông báo kết luận giám sát của Ban Thường vụ Đảng ủy UBND tỉnh đối với 04 đảng viên…" khi Thông báo chưa có số; kết quả chưa có số liệu thì viết định tính thành câu hoàn chỉnh ("đã duy trì kiểm điểm tiến độ hằng tuần…", "không có văn bản bị trả lại do áp dụng sai quy định").
- Chỉ dòng `ngày      tháng      năm 2026` ở góc phải được để trống (khoảng trắng, không dấu chấm) cho văn bản ký sau.
- Bôi tím (7030A0) chỉ dùng ở bản làm việc; bản Bạn yêu cầu "hoàn thiện để xuất bản" phải hết tím.

## 4. Bộ 4 văn bản sau giám sát đảng viên — kết cấu đã duyệt

| Văn bản | Thời điểm | Kết cấu |
|---|---|---|
| Ý kiến phát biểu tại hội nghị thông qua dự thảo BC giám sát | Tại hội nghị | Kính thưa (3 dòng); 1. Về dự thảo Báo cáo (nhất trí, đánh giá sát, đúng, không đề nghị sửa); 2. Nghiêm túc tiếp thu từng hạn chế, nhận nguyên nhân chủ quan là chính; 3. Kế hoạch khắc phục (3.1 theo hạn chế 1, 3.2 theo hạn chế 2, 3.3 thời gian và trách nhiệm); 4. Kiến nghị, cam kết; Xin trân trọng cảm ơn |
| Báo cáo giải trình, tiếp thu dự thảo BC giám sát | Gửi Đoàn ngay sau hội nghị | Kính gửi Đoàn giám sát; I. Chấp hành QĐ, kế hoạch giám sát; II. Ý kiến đối với dự thảo: 1. ưu điểm (mục B.I.x), 2. hạn chế + nguyên nhân (B.II.x), 3. nhận xét kiến nghị (C); III. Phương hướng khắc phục |
| Kế hoạch khắc phục hạn chế, khuyết điểm | Sau Thông báo kết luận | Căn cứ QĐ giám sát + BC kết quả giám sát + Thông báo kết luận (không dẫn số nếu chưa có); I. Mục đích, yêu cầu; II. Bảng 5 cột: TT / Hạn chế / Giải pháp / Thời gian / Kết quả, sản phẩm để đánh giá (bảng 12pt, dòng tiêu đề lặp lại); III. Tổ chức thực hiện (báo cáo chi bộ, Đảng ủy Sở; báo cáo kết quả đúng hạn Thông báo; đưa vào kiểm điểm cuối năm) |
| Báo cáo kết quả khắc phục | Đến hạn tại Thông báo / kiểm điểm cuối năm | Kính gửi BTV Đảng ủy UBND tỉnh, Đảng ủy Sở; I. Hạn chế được kết luận; II. Kết quả khắc phục theo từng hạn chế (định tính, câu hoàn chỉnh); III. Tự đánh giá và phương hướng |

Nguyên tắc nội dung: lấy nguyên văn hạn chế, khuyết điểm và mục số trong dự thảo Báo cáo của Đoàn; xác định "nguyên nhân chủ quan là chính, không đổ lỗi hoàn cảnh"; mỗi hạn chế có giải pháp đo được (sổ kiểm điểm tiến độ hằng tuần, danh mục VBQPPL theo lĩnh vực, biên bản sinh hoạt chuyên môn hằng tháng). Chi bộ sinh hoạt của đảng viên đọc từ chú thích dự thảo Báo cáo (Long: Chi bộ số 2 từ 3/2026), không đoán. Mỗi văn bản gọn 2 trang A4 — thiếu chỗ thì co giãn dòng 1,3 hoặc rút thân, không co khối ký.
