# Nhật ký thay đổi plugin hc-sct-vn

## 1.2.0 — 2026.07.24 — Cập nhật khung xử phạt theo NĐ 275/2026/NĐ-CP

NĐ 275/2026/NĐ-CP ngày 08/7/2026 (hiệu lực 25/8/2026) thay thế NĐ 71/2019 + Điều 1 NĐ 17/2022 — nhóm hóa chất Đ7–52 viết lại theo Luật 69/2025 (Đ25 CSDL/báo cáo thay Đ29 cũ, mức tăng ~3 lần: không báo cáo năm 30–40 tr/tổ chức; Đ34 huấn luyện ATHC thay Đ11 cũ). Sửa: SKILL.md (khung xử phạt), ref 07, ref 10, ref 11 mục 4a (chế tài răn đe 2 thời kỳ), ref 15, ref 16 bài học 1. Chi tiết chế tài + thẩm quyền + chuyển tiếp: plugin dùng chung mới **`xp-hc-vlncn-sct-vn`** (toàn văn NĐ 275/2026 trong van-ban-goc).

## 1.1.0 — 2026.07.24 — Bổ sung vụ Cục Hóa chất xử phạt DN trên địa bàn (QĐ 26/QĐ-XPVPHC)

Nguồn: QĐ số 26/QĐ-XPVPHC ngày 08/7/2026 của Cục trưởng Cục Hóa chất (Phùng Mạnh Ngọc) xử phạt Công ty TNHH Thương mại Hải Đăng (phường Lào Cai) 16 triệu đồng — Sở nhận số đến 14708 ngày 20/7/2026, "để biết và phối hợp quản lý trên địa bàn". Metadata xác minh bằng OCR + soi ảnh (số "26", ngày "08" viết tay trên bản scan).

- **ref 16 (mục 5 mới):** hồ sơ vụ việc đầy đủ — 2 hành vi + căn cứ + mức phạt (hồ sơ huấn luyện 4tr theo điểm a khoản 3 Điều 11 NĐ 71/2019; không nộp báo cáo năm 2025 qua chemicaldata.gov.vn 12tr theo Điều 29 NĐ 71/2019 sửa khoản 15 Điều 1 NĐ 17/2022); 5 bài học nghiệp vụ; mục "VIỆC CHỜ XÁC MINH" đổi thành mục 6.
- **ref 10:** quy trình xử lý khi Cục kiểm tra/xử phạt trực tiếp không qua Sở (cập nhật theo dõi, tránh trùng lặp kiểm tra theo NĐ 217/2025, tổng hợp báo cáo năm); chốt NĐ 71/2019 + 17/2022 vẫn là khung xử phạt hiện hành đến 7/2026, chưa có NĐ xử phạt mới theo Luật 69/2025; bổ sung QĐ 464/QĐ-BCT 16/3/2026 (chức năng Cục Hóa chất) làm căn cứ thẩm quyền.
- **ref 11 (mục 4a mới):** chế tài răn đe cho CV đôn đốc DN báo cáo năm (mức phạt + tiền lệ thực tế, không nêu tên DN trong văn bản gửi rộng rãi; báo cáo nộp qua hệ thống, không nhận bản giấy).
- **ref 07:** điểm kiểm tra 3 cấu phần bắt buộc của hồ sơ huấn luyện (nội dung; người huấn luyện; kết quả kiểm tra) — thiếu một cấu phần đã cấu thành vi phạm.
- **ref 15 + SKILL.md:** cập nhật mục lục; thư mục mới `vi-du-thuc-te/xu-phat/` kèm bản scan QĐ gốc.


## 1.0.1 — 2026.07.05 — Rà soát chéo toàn diện sau khởi tạo

Đối chiếu từng số liệu với văn bản gốc (Điều 9, 13, 14, 20, 21, 22 NĐ 26; Điều 29-35, 40 NĐ 25; Điều 3-4 TT 01; Điều 48 Luật) — toàn bộ thời hạn, ngưỡng, thành phần hồ sơ xác nhận khớp. Chỉnh sửa:
- **Chính xác pháp lý:** ref 09 — khoản 4 Điều 21 NĐ 26 chỉ miễn GCN/GP **SẢN XUẤT** cho san chiết, pha chế nội bộ (không đương nhiên miễn kinh doanh); ref 06 — bổ sung phí thẩm định KH (khoản 7 Điều 34 NĐ 25).
- **Liên kết plugin/skill (mới):** `xd-sct-vn` — Thông báo kết quả kiểm tra nghiệm thu (điểm c hồ sơ Điều 9, Điều 20 NĐ 26) là thủ tục KTCTNT, dẫn tại SKILL mục I/VII, ref 03, 05, 10; `kcn-ccn-vn` — cơ sở hóa chất trong KCN/CCN, QĐ phê duyệt KH gửi BQL khu (ref 06); `pccc-sct-vn`, `bvmt-sct-vn`, `hnh-sct-vn` — mục phối hợp liên lĩnh vực khi kiểm tra hiện trường (ref 10 mục 6) và ranh giới KH sự cố hóa chất ≠ kế hoạch sự cố chất thải ≠ hồ sơ PCCC (ref 06 mục 11); ánh xạ hóa chất ↔ loại HHNH (loại 8/2/5) + TT 26/2026 đưa loại 5, 8 về tỉnh (ref 13 mục G).
- **Tổ chức nội bộ:** ref 01 mục 5 — phân tầng duyệt: CN Loan → **TP Nguyễn Hữu Long** (hóa chất không thuộc phân công trực tiếp PTP Trang; Trang chỉ kiêm khi cán bộ phụ trách vắng) → PGĐ Thuân, khớp `sct-laocai-org-vn`.
- Rà 100% đường dẫn file trích dẫn trong SKILL + 16 references: 0 lỗi tên file.

## 1.0.0 — 2026.07.05 — Khởi tạo plugin quản lý nhà nước về hóa chất

Plugin lớn phục vụ toàn bộ công tác QLNN về hóa chất của Phòng Quản lý Công nghiệp,
Sở Công Thương tỉnh Lào Cai, xây dựng trên **khung pháp lý mới có hiệu lực từ
01/01/2026** (thay thế hoàn toàn Luật Hóa chất 06/2007 và các Nghị định 113/2017,
82/2022, Thông tư 32/2017, 17/2022).

### Khung pháp lý cốt lõi (đã đối chiếu văn bản gốc)
- Luật Hóa chất số 69/2025/QH15 (14/6/2025, hiệu lực 01/01/2026).
- Nghị định 24/2026/NĐ-CP (17/01/2026) — 04 danh mục hóa chất (Phụ lục I-IV).
- Nghị định 25/2026/NĐ-CP (17/01/2026) — phát triển CN hóa chất, an toàn - an ninh,
  huấn luyện an toàn, Kế hoạch/Biện pháp phòng ngừa ứng phó sự cố hóa chất.
- Nghị định 26/2026/NĐ-CP (17/01/2026) — quản lý hoạt động hóa chất, cấp phép,
  khai báo, thu hồi.
- Thông tư 01/2026/TT-BCT + 02/2026/TT-BCT (17/01/2026) — biểu mẫu, phân cấp TTHC.

### Nội dung ban hành
- SKILL.md: bản đồ 6 nghiệp vụ; chuỗi thẩm quyền UBND cấp tỉnh / Cục Hóa chất;
  bảng phân cấp TTHC theo Điều 3-4 TT 01/2026; nguyên tắc nghiệp vụ bất biến.
- 16 reference files: thẩm quyền - phân cấp; điều kiện SX/KD; hồ sơ - trình tự GCN;
  hóa chất kiểm soát đặc biệt; dịch vụ tồn trữ; Kế hoạch/Biện pháp phòng ngừa sự cố;
  huấn luyện an toàn; khai báo - XNK; thu hồi - miễn trừ; kiểm tra chuyên ngành;
  báo cáo - thống kê; danh mục hóa chất; FAQ doanh nghiệp; bộ mẫu văn bản;
  mục lục văn bản gốc; thực tiễn tại Sở.
- Bộ mẫu (mau-ho-so): văn bản đề nghị (Mẫu 10a, 10b, 11a) và mẫu GCN kết quả
  (Mẫu 10c) dựng theo Phụ lục X, XI Thông tư 01/2026.
- Ví dụ thực tế (vi-du-thuc-te): CV từ chối cấp GCN (axit HNO3), QĐ thành lập
  Đoàn kiểm tra hóa chất 2026, Báo cáo kết quả kiểm tra 04 đơn vị, CV cử người
  thẩm định KH sự cố, các báo cáo - bản trình đã ban hành.
- Văn bản gốc (van-ban-goc): Luật 69/2025, NĐ 24/25/26/2026, TT 01+02/2026,
  NĐ 146/2025, NĐ 34/2024, NĐ 71/2019 (xử phạt), QCVN 05A:2020/BCT SĐ1:2024,
  TCVN 5507:2002, CV Cục Hóa chất.

### Việc chờ xác minh (KHÔNG tự điền)
- **Quyết định ủy quyền của UBND tỉnh Lào Cai cho Giám đốc Sở Công Thương** ký các
  Giấy chứng nhận/Giấy phép hóa chất thuộc thẩm quyền UBND cấp tỉnh (GCN đủ điều kiện
  SX/KD hóa chất có điều kiện; GCN dịch vụ tồn trữ; GP hóa chất kiểm soát đặc biệt
  nhóm 2; phê duyệt KH phòng ngừa sự cố): đến 05/7/2026 **chưa xác minh đã ban hành**.
  → Trước khi kết luận người ký (Chủ tịch UBND tỉnh hay Giám đốc Sở theo ủy quyền),
  PHẢI hỏi Bạn. Thực tiễn CV từ chối 4/2026 còn ghi "Sở không đủ cơ sở tham mưu UBND
  tỉnh cấp" → tại thời điểm đó Sở tham mưu, UBND tỉnh ký.
- Quyết định công bố TTHC hóa chất mới nhất (thời hạn giải quyết, phí thẩm định).
