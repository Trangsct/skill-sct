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

### Mã người soạn ở dòng "Lưu" và người ký
- Dòng lưu: `Lưu: VT, CN(<Mã>).` với mã viết tắt người soạn của Phòng QLCN (đã gặp: Long, Trang, Khôi, LTH…). Hỏi/ướm theo người thụ lý hồ sơ; nếu không rõ để `Lưu: VT, CN.`.
- **Người ký**: theo Quy tắc 6 — chọn PGĐ theo **lĩnh vực** (KCN/CCN/ATTP → Nguyễn Đình Chiến; HHNH/hóa chất/VLNCN/khoáng sản/môi trường/PCCC/KHCN/ATVSLĐ/năng lượng/thương mại → Hoàng Văn Thuân; xem bảng trong `sct-laocai-org-vn`). Khi không chắc, nêu rõ để người dùng chọn thay vì mặc định cứng.
