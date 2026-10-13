# CHANGELOG — dacn-sct-vn v1.9.0 (12/10/2026)

Nguồn: hai PDF Bạn gửi trong phiên 12/10/2026 — Công văn 10349/UBND-KT và Giấy chứng nhận đăng ký đầu tư điều chỉnh lần 5 dự án Nhà máy bao bì thùng phuy (KCN Tằng Loỏng). Cả hai lưu vào `van-ban-goc/` kèm bản `.txt`.

## 1. Reference 15 (mới) — CV 10349/UBND-KT ngày 09/10/2026, Chủ tịch UBND tỉnh Nguyễn Tuấn Anh ký

- Chế độ **theo dõi, nắm bắt tình hình SXKD doanh nghiệp** mới, song song với báo cáo chỉ tiêu NQ 169: Sở Công Thương **chủ trì 37 DN công nghiệp + 41 DN thương mại** (Phụ lục); theo dõi sản lượng, công suất, nguyên liệu, điện năng, đơn hàng, thị trường, XNK; nhận diện DN giảm sản lượng, dừng, dưới công suất.
- Mốc: **trước ngày 10 hằng tháng** gửi thông tin tóm tắt → **Thống kê tỉnh + Sở Tài chính**; Thống kê tỉnh tổng hợp trước ngày 12; vấn đề cấp bách báo cáo ngay.
- Yêu cầu chung: không phát sinh TTHC, ưu tiên CSDL sẵn có, chỉ gặp DN khi thật cần. Ranh giới 4 sở khác. Danh sách đầy đủ 78 DN của Sở kèm gợi ý theo dõi; DN trùng giữa các sở; nhận xét để đề xuất bổ sung danh sách.
- ⚠️ Ký hiệu: bản ký ghi **UBND-KT**, trang Phụ lục in UBND-TH — dùng UBND-KT.
- Tệp: `van-ban-goc/2026.10.09-10349.UBND.KT-Tang-cuong-theo-doi-nam-bat-SXKD-doanh-nghiep.pdf` (bản quét 4,6 MB, export-ignore) + `.txt` toàn văn (máy phiên không có tesseract — Claude đọc ảnh 200 dpi và gõ lại; số 10349 và ngày 09 là trường điền điện tử trong lớp chữ PDF, khớp ảnh).

## 2. Reference 08 mục 3 — dự án thứ cấp KCN Tằng Loỏng: GCN ĐKĐT điều chỉnh lần 5 Nhà máy bao bì thùng phuy

- **GCN ĐKĐT mã số 8280788124, chứng nhận điều chỉnh lần thứ 05 ngày 09/10/2026**, Trưởng ban BQL Khu kinh tế Vương Trinh Quốc ký, nơi nhận có Sở Công Thương. Nhà đầu tư: Công ty TNHH sản xuất và xuất nhập khẩu Bao Bì (GCN ĐKDN 5300233269). Căn cứ **Văn bản 10320/UBND-KT ngày 09/10/2026** của UBND tỉnh chấp thuận chủ trương điều chỉnh; BC thẩm định 51/QHXD ngày 09/10/2026.
- Nội dung: 300.000 thùng phuy/năm; đất 16.444 m² tại một phần Lô CN3 KCN Tằng Loỏng; tổng vốn 16,133 tỷ đồng (tự có 11,483; vay 4,65); thời hạn 50 năm từ 01/3/2006; **bổ sung ~600 m² nhà xưởng**: chuẩn bị Quý III–IV/2026, thi công Quý I–II/2027, vận hành Quý III/2027; 50–80 lao động, doanh thu 90 tỷ/năm, nộp NSNN ~3 tỷ/năm.
- Khép vụ việc kccn-sct-vn ref 26 (Sở góp ý điều chỉnh dự án tại 4639/SCT-KH ngày 03/8/2026).
- Tệp: `van-ban-goc/2026.10.09-8280788124.GCNDKDT-Dieu-chinh-lan-5-Bao-Bi-thung-phuy-KCN-Tang-Loong.pdf` + `.txt` (pdftotext).

## 3. `du-lieu/danh-muc-du-an.json` — bản ghi **CBCT-082** (97 bản ghi)

- Dự án thứ cấp đầu tiên của KCN do **Ban Quản lý Khu kinh tế tỉnh** quản lý được ghi vào sổ (mở rộng `_pham_vi`). Trạng thái **MR** (đang hoạt động, mở rộng nhà xưởng) — tính vào cả sản lượng và vốn đầu tư theo quy tắc reference 03. Quy mô ghi đủ từ GCN; sản lượng thực hiện để trống (số động).
- Dự án **không có trong danh sách 37 DN công nghiệp** của CV 10349 — ghi ở `ghi_chu` để cân nhắc khi đề xuất bổ sung.

## 4. Khác

- `references/05-che-do-bao-cao.md`: thêm mục 0 phân biệt hai chế độ (trước ngày 10 — DN; trước ngày 20 — chỉ tiêu) và dòng lịch tháng.
- `SKILL.md`: nghiệp vụ 13 (theo dõi SXKD DN theo CV 10349), 14 (khuyến công, ref 14 — bổ sung dòng còn thiếu trong danh sách), bảng reference thêm 15, bảng `du-lieu` 97 bản ghi, bảng phạm vi dữ liệu; description.
- `plugin.json` → 1.9.0; keyword `cv-10349-2026`, `theo-doi-sxkd-doanh-nghiep`, `bao-bi-thung-phuy`.
