# CHANGELOG — sd-vlncn-sct-vn v2026.9.3.2 (03/9/2026)

## [2026.9.3.2] - 03/9/2026 — vụ Thịnh Đạt: PANM hầm lò chuẩn rà đủ Phụ lục VII + Giấy đề nghị Mẫu số 04; anti-error 25–30
- **2 khung docx chuẩn mới** trong `vi-du-thuc-te/` (kèm 2 script python-docx dựng lại): `PANM-Thinh-Dat-mo-chi-kem-Trong-Pa-Sang-Tu-Le-ham-lo-ban-chuan-3.9.2026.docx` (20 trang, thay khung Kim Thành 21/8 làm khuôn hầm lò) và `Giay-de-nghi-Mau-04-cap-GP-su-dung-VLNCN-Thinh-Dat-ban-chuan-3.9.2026.docx`.
- **Mẫu 24 mới** — Giấy đề nghị theo **Mẫu số 04 Phụ lục III TT 23/2024** (sửa nhầm lẫn "Mẫu số 03" — Mẫu 03 là XNK; Mẫu 04 không bị TT 26/2026 sửa): 11 mục đúng thứ tự, địa danh – ngày ở đầu văn bản, danh mục "không đưa vào đơn", điểm kiểm tra của Sở.
- **Mẫu 22**: chỉ khung hầm lò chuẩn mới + checklist Phụ lục VII 5 phần để rà trước khi xuất PANM.
- **Ref 11 thêm anti-error 25–30**: (25) Mẫu 04; (26) 9 nội dung Phụ lục VII khung Kim Thành thiếu — đáng kể nhất là **đường kính lỗ khoan** (thiết kế chỉ có dt) — và **khối ký PHÊ DUYỆT trái – NGƯỜI LẬP phải**; (27) **thời gian nổ mìn hầm lò không ấn định khung giờ cấm**, neo vào chế độ làm việc thiết kế, GP bỏ dòng giờ nổ mìn (chốt PTP Trang 03/9); (28) GATE 3 nguồn số VLNCN năm khi thuyết minh nhiều phiên bản (Thịnh Đạt: 88.000 QĐ 09 ↔ 40.848 Bảng 8.12 ↔ 71.640 PANM cũ) + kiểm tra nội bộ bảng mới (Bảng 8.12 lệch ~8 lần so Bảng 5.1/8.10); (29) sức chứa kho theo văn bản nghiệm thu PCCC (3.000 kg năm 2011), không theo BC hoàn thành DN (5.000 kg); (30) chủng loại + phương pháp nổ theo Bảng 8.10 thiết kế (AĐ1, kíp điện vi sai; lò dốc 74° cấm dây cháy chậm), Qđ max 50,4 kg trùng GP 32 cũ làm đối chứng.
- **Ref 07 mục M** — toàn bộ dữ liệu vụ Thịnh Đạt đã soi ảnh (pháp nhân, ANTT, chuỗi lineage thiết kế QĐ 09/QĐ-Cty 24/6/2026, nhân sự 7 người + số GCN, thông số thiết kế dùng cho PANM, 4 bộ số VLNCN mâu thuẫn, việc còn lại khi DN nộp lại).
- SKILL.md: mục I thêm 2 dòng routing (khung hầm lò mới; mẫu 24); mục VI mục lục 25–30; cây thư mục.
- Kỹ thuật: .rar mở bằng `unar` khi `rarfile` không có backend; bảng python-docx cần `tblLayout fixed` + `tblGrid`; bảng 8 cột để section landscape riêng.
- plugin.json 2026.9.3.1 → **2026.9.3.2**.

