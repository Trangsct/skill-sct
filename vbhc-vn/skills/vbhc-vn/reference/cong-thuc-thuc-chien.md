# Công thức & checklist thực chiến (rút từ việc thật)

### Căn chỉnh bảng/biểu "vuông vắn, đều đẹp"
Khi người dùng yêu cầu căn bảng đều đẹp, hoặc dựng biểu tổng hợp khổ ngang (biểu thu hút đầu tư, biểu CCN…), áp tham số chuẩn:
- **Khổ A4 ngang** cho biểu nhiều cột; lề trên/dưới/phải 20mm, trái 30mm. Bề rộng nội dung A4 (lề 30/20) = **9071 DXA** — tổng `columnWidths` phải bằng 9071 để không tràn lề.
- **Căn ô**: tất cả ô căn giữa theo chiều dọc (vertical center); cột **TT** căn giữa ngang; các cột nội dung **căn đều hai biên (justify)**; **tên cụm/đối tượng in đậm**.
- **Nền trắng, không shading**; viền đen mảnh; **dòng tiêu đề bảng lặp lại ở mỗi trang** (thuộc tính `tblHeader` cho hàng đầu) khi bảng tràn nhiều trang.
- Có **dòng "Tổng cộng"** cộng đúng các cột số khi là biểu tổng hợp.
- Căn ô đều bằng lxml/python-docx: duyệt mọi `<w:tc>`, set `vAlign=center`; set alignment paragraph theo cột. (Reorder dòng: thao tác `<w:tr>` ở cấp XML như mục Chế độ B.)

### Đồng bộ chéo Báo cáo ↔ Phụ lục ↔ văn bản VP UBND
Việc CCN thường gồm 1 báo cáo + nhiều phụ lục + đôi khi bản của VP UBND tỉnh. Khi sửa, rà đồng bộ **toàn bộ**, không chỉ một phần:
- **Số liệu tổng** (tổng diện tích, số cụm, TMĐT, tỷ lệ lấp đầy, số dự án) phải khớp tuyệt đối giữa Mục tổng hợp của báo cáo và dòng "Tổng cộng" của phụ lục.
- **Đánh số mục/nhóm và tham chiếu chéo**: khi thêm/bớt/đổi nhóm trong phụ lục, cập nhật lại số La Mã, STT, và mọi câu "xem mục … Phụ lục …" trong thân báo cáo.
- **Khi căn chỉnh theo bản VP UBND**: đồng bộ cả phần nội dung (khó khăn, kiến nghị, đề xuất), không chỉ Mục I và bảng — người dùng đã nhiều lần nhắc "đồng bộ toàn diện, không vá nửa vời".
- Nếu **tổng nêu trong văn bản ≠ tổng cộng từng dòng** (vd 228 ha vs 263 ha): KHÔNG tự ý chỉnh một bên cho khớp — liệt kê từng dòng, nêu rõ chênh lệch để người dùng quyết.

### Toàn vẹn số liệu & metadata (bắt buộc, gắn với mục "Phòng tránh 7 nhóm sai lầm")
- **Không bịa số/ngày văn bản, không bịa số liệu.** Thiếu thì để `-` hoặc để trống chờ phát hành, KHÔNG điền số phỏng đoán.
- **Số ký hiệu văn bản đi và ngày ký**: mặc định để trống cho văn thư cấp; nêu rõ trong phần báo lại.
- **Xác minh số/ngày từ PDF công văn đến** bằng `scripts/extract_metadata.py` (mục "Đọc PDF văn bản đến") trước khi trích dẫn (vùng số/ngày hay bị trống trong context do PDF layout 2 cột) — đã nhiều lần phát hiện số thật khác hẳn (vd 833/BQL-QHXD, 3501/SCT-CN, 2861/SYT-NVY).
- Tránh dùng "dự kiến", "gần như", "có thể" trong bản trình ký (trừ khi là **tên gọi văn bản** hoặc thuật ngữ chuẩn như "tổng mức đầu tư dự kiến" ở bước chủ trương).

### Dòng "Lưu" và người ký
- Dòng lưu: `Lưu: VT, CN.` — không ghi tên/mã người soạn (Bạn chốt 01/10/2026).
- **Người ký**: theo Quy tắc 6 — chọn PGĐ theo **lĩnh vực** (KCN/CCN/ATTP → Nguyễn Đình Chiến; HHNH/hóa chất/VLNCN/khoáng sản/môi trường/PCCC/KHCN/ATVSLĐ/năng lượng/thương mại → Hoàng Văn Thuân; xem bảng trong `sct-laocai-org-vn`). Khi không chắc, nêu rõ để người dùng chọn thay vì mặc định cứng.

### Phụ lục bảng của kế hoạch, danh mục dự án (rút từ Kế hoạch Bài toán lớn số 2, 04/10/2026)
- **Tiêu đề phụ lục là một đoạn**: "PHỤ LỤC II" / "DANH MỤC … CÔNG NGHỆ CHIẾN LƯỢC GIAI ĐOẠN 2026 - 2030" / "(Kèm theo Kế hoạch số …/KH-UBND ngày … của UBND tỉnh Lào Cai)". Không tách "GIAI ĐOẠN 2026 - 2030" thành đoạn riêng — Bạn yêu cầu ghép nối với dòng trên.
- **Cột tên cơ quan phải đủ rộng** (≥ 3,5 cm ở khổ ngang 10pt) để "Sở Công Thương; BQL Khu kinh tế tỉnh" không bị giãn chữ thành "Sở Công / Thương; BQL / Khu kinh tế" khi căn đều. Cân lại các cột trong cùng tổng `tblGrid`; không đổi khổ giấy.
- **Không cắt một dòng bảng sang hai trang**: đặt `w:cantSplit` cho mọi `w:tr` của bảng danh mục; dòng tiêu đề giữ `tblHeader`. Sau đó render kiểm tra phần Ghi chú dưới bảng không bị đẩy sang trang riêng — nếu bị thì rút gọn câu chữ vài ô dài nhất (trạng thái, địa điểm), không thu nhỏ chữ.
- **Viết tắt trong bảng, viết đủ trong thân**: Phụ lục dùng KCN, CCN, XLNT, Sở NN&MT, Sở KH&CN, BQL; thân văn bản viết đủ tên sở, ban. Riêng "UBND" viết tắt ở cả hai (R19).

### Khối ký phải nằm cùng trang với phần kết — cách xử lý khi LibreOffice đẩy sang trang mới
- `keep_with_next` ở đề mục tạo CHUỖI (đề mục → "a) Điểm nghẽn" → đoạn thân có widow control): một chuỗi không vừa chỗ trống cuối trang sẽ kéo cả nhóm sang trang sau, để lại trang chỉ đầy 84–88%; dồn tích vài trang như vậy thì phần kết + khối ký rơi sang trang riêng. Dấu hiệu: bảng "fill% từng trang" có nhiều trang dưới 90% trước trang ký.
- Cách sửa theo thứ tự: (1) đặt `keep_with_next` cho đoạn "Trên đây là…" để phần kết luôn đi cùng bảng ký; (2) bỏ đoạn trống thừa ngay trước bảng ký (giữ đúng 1 — SIGSPACE); (3) gộp dòng Nơi nhận cùng cấp (ví dụ "Công an tỉnh; Thuế tỉnh; Thống kê tỉnh") nhưng không gộp doanh nghiệp với cơ quan nhà nước (R20); (4) lược câu trùng lặp ở các mục cuối (tổ chức thực hiện, chế độ báo cáo) — việc đã nêu ở nội dung nhiệm vụ thì không nhắc lại ở phần giao việc; (5) chỉ khi vẫn thiếu mới cắt ý. Không giảm số dòng trống trong ô ký xuống dưới 4, không đổi cỡ chữ, không đổi lề.
- Đo bằng script: với mỗi trang lấy `max(bottom)` của chữ so với chiều cao trang (pdfplumber); trang ký phải ≤ 92% và trang trước nó không được dưới ~85% nếu còn trang ký lẻ.
