# 00 — MỤC LỤC FILE NGUỒN GỐC

Thư mục `sources/` chứa **toàn văn các văn bản gốc** (trích xuất text từ PDF/DOCX) để tra cứu chính xác, đầy đủ. Khi cần số liệu/danh mục/tọa độ để đưa vào văn bản, **mở đúng file dưới đây và tra trực tiếp** thay vì chỉ dựa vào các reference tóm tắt.

## Danh sách file nguồn

| File | Văn bản gốc | Tình trạng pháp lý | Dùng để tra |
|---|---|---|---|
| `qd866-dieuchinh-2026-thuyetminh.txt` | Thuyết minh Điều chỉnh Quy hoạch khoáng sản nhóm I 2021-2030 (Cục ĐC&KS - Bộ NN&MT, 3/2026); PDF gốc 219 trang | **DỰ THẢO — chưa ký** | Quan điểm, mục tiêu, định hướng thăm dò/khai thác/chế biến từng khoáng sản; phần Lào Cai (đồng, sắt, đất hiếm, graphit, vàng) |
| `qd866-dieuchinh-2026-phuluc.txt` | Phụ lục Điều chỉnh QH khoáng sản nhóm I (3/2026); PDF gốc 449 trang. Gồm Phụ lục I (trữ lượng), II (thăm dò), III (khai thác), IV (chế biến), VI (tọa độ khép góc) + tổng hợp ý kiến góp ý các tỉnh | **DỰ THẢO — chưa ký** | Danh mục mỏ + trữ lượng + công suất + **tọa độ khép góc** từng mỏ; ý kiến góp ý của các địa phương |
| `qd768-quyhoach-dien-viii-toanvan.txt` | QĐ 768/QĐ-TTg 15/4/2025 — Điều chỉnh Quy hoạch điện VIII (toàn văn quyết định) | **ĐÃ KÝ** (PTT Bùi Thanh Sơn) | Quan điểm, mục tiêu, cơ cấu nguồn điện quốc gia, định hướng lưới; danh mục TBA/ĐZ 500-220kV miền Bắc (trong bảng) |
| `qht-laocai-2026-baocao-thuyetminh.txt` | Báo cáo (thuyết minh) Điều chỉnh Quy hoạch tỉnh Lào Cai 2021-2030 (UBND tỉnh, bản thao tác 07/6/2026); DOCX gốc | Bản thao tác — KHÔNG phải QĐ 525 đã ký | **Toàn bộ 04 ngành tích hợp**: hiện trạng + phương án điện (Bảng 4-15, 32-43), khoáng sản (mục 1.4.2, 4.6, 6), KCN (5.2), CCN; kèm các bảng |
| `qht-laocai-2026-phuluc.txt` | Phụ lục Báo cáo Điều chỉnh QHT Lào Cai (07/6/2026); 54 bảng | Bản thao tác | Chỉ tiêu KT-XH, dân số, GRDP, sử dụng đất, danh mục dự án ưu tiên... |

## Văn bản gốc KHÁC (chưa có text — tham chiếu qua reference)

- **QĐ 2581/QĐ-TTg 24/11/2025** (Tả Phời) — PDF scan ảnh; nội dung đã trích vào ref 07 mục A.
- **QĐ 525/QĐ-UBND 25/02/2026** (Quy hoạch tỉnh Lào Cai) + phụ lục — PDF scan; bản thao tác thuyết minh tương ứng đã có text tại `qht-laocai-2026-*.txt`; danh mục KCN/CCN trong skill `kcn-ccn-vn` ref 17.

## Cách tra (quan trọng)

1. Tra theo **TÊN MỎ + TÊN XÃ** hoặc **tên dự án điện**, KHÔNG tra theo số phụ lục (chỉ số phụ lục giữa các khoáng sản không nhất quán — ví dụ VI.7 là thiếc, VI.10 là đồng).
   ```bash
   grep -n -i "sin quyền\|tả phời" sources/qd866-dieuchinh-2026-phuluc.txt
   grep -n -i "trạm chuyển đổi.*lào cai\|back-to-back" sources/qd768-quyhoach-dien-viii-toanvan.txt
   ```
2. Đọc khối xung quanh dòng tìm được (`sed -n 'A,Bp' <file>`).
3. **Phân biệt pháp lý:** số liệu từ file dự thảo (qd866-dieuchinh-2026-*) chỉ để tham khảo/góp ý; khi viện dẫn chính thức phải dựa vào văn bản ĐÃ KÝ (QĐ 866 18/7/2023, QĐ 2581, QĐ 768, QĐ 525).
4. File nguồn là text trích từ PDF: có thể sai sót OCR, header lặp giữa trang — đối chiếu bản gốc khi cần độ chính xác tuyệt đối.

## Thêm file nguồn mới

Khi có văn bản gốc mới (PDF/DOCX), trích text và đặt vào `sources/` với tiền tố ngày + tên ngắn, thêm dòng mô tả vào bảng trên. Văn bản đã ký để riêng, dự thảo ghi rõ "DỰ THẢO".
