# CHANGELOG — quy-hoach-ct-vn

## [1.3.0] - 13/9/2026 — chuỗi chủ trương → chiến lược khoáng sản (NQ 10-NQ/TW, NQ 88/NQ-CP, QĐ 334) + toàn văn QĐ 2581

- `references/10-chu-truong-chien-luoc-khoang-san.md` MỚI: NQ 10-NQ/TW 10/02/2022, NQ 88/NQ-CP 22/7/2022 (18 nhiệm vụ),
  QĐ 334/QĐ-TTg 01/4/2023 (Chiến lược — định hướng từng loại khoáng sản, dự trữ KS quốc gia, phân công), QĐ 154/QĐ-TTg
  29/01/2022 (kéo dài kỳ QH VLXD, xi măng — lịch sử); 8 anti-error.
- `references/07` mục A viết lại từ **toàn văn QĐ 2581 đã ký**: chốt dấu thập phân công suất (967,434 và 8,473 ×10³ tấn/năm),
  bảng tọa độ đầy đủ 4 khu (30 điểm, tổng 248,3 ha, trong đó 200 ha đã cấp phép), cảnh báo QĐ 2581 cho 03 tỉnh,
  cảnh báo vênh tên xã trong bản gốc. `references/08` trỏ sang bản đã ký + sửa 1 byte UTF-8 hỏng. `references/04` thêm 4 dòng.
- `van-ban-goc/` MỚI (05 DOCX + mục lục); `sources/` thêm 05 file toàn văn + cập nhật mục lục.
- `SKILL.md` (description, trường hợp dùng 7, bảng QH quốc gia, bảng reference, nguyên tắc bất biến mới số 8), `README.md`.
- `plugin.json` → 1.3.0. Chi tiết: `CHANGELOG-v2026.09.13.md`.

## [1.2.0] - 05/9/2026 — NQ 66.25/2026/NQ-CP: quy hoạch khoáng sản về Bộ Công Thương

- `references/04` bảng khung pháp lý: thêm NQ 66.25/2026/NQ-CP (04/9/2026, hiệu lực 15/9/2026 – 28/02/2027) — chức năng quy hoạch địa chất, khoáng sản (NĐ 70/2026 PL I số 26–28) chuyển Bộ NN&MT → Bộ Công Thương; cấp Sở → Sở Công Thương; kiến nghị điều chỉnh QĐ 866/2581/1626 từ 15/9/2026 gửi Bộ Công Thương.
- `plugin.json` → 1.2.0.

## [1.1.2] - 02/9/2026 — thêm GATE PDF đầu SKILL.md
- Plugin chưa có cổng đọc PDF văn bản đến bằng extract_metadata.py; bổ sung 1 đoạn ngay dưới tiêu đề (bài học vụ QĐ 5116/QĐ-SCT).

## v1.1.0 — 26/7/2026: reference 09 — vốn đầu tư công cấp điện nông thôn 2026-2030

Bổ sung `references/09-von-dtc-cap-dien-2026-2030.md` từ **Quyết định số 2390/QĐ-UBND ngày 09/7/2026** của UBND tỉnh Lào Cai về kế hoạch đầu tư công trung hạn giai đoạn 2026-2030 nguồn vốn ngân sách địa phương (Chủ tịch Nguyễn Tuấn Anh ký; căn cứ NQ 25/NQ-HĐND ngày 29/6/2026; Tờ trình 536/TTr-STC ngày 19/6/2026).

### Phát hiện đáng ghi nhớ

Rà toàn bộ 05 biểu: **Sở Công Thương chỉ làm chủ đầu tư 07 dự án, tất cả là cấp điện nông thôn, tổng 130.447 triệu đồng**, 100% từ nguồn thu tiền sử dụng đất (không có XDCB tập trung). Đây là toàn bộ vốn đầu tư công trung hạn mà Sở trực tiếp làm chủ đầu tư — dùng ngay khi lãnh đạo hỏi, khi lập báo cáo giải ngân hoặc giải trình năng lực chủ đầu tư.

- Chuyển tiếp (biểu 02) — 49.345: cấp điện nông thôn từ lưới điện Quốc gia tỉnh Yên Bái 2014-2025 (45.000); khắc phục khẩn cấp điện nông thôn do thiên tai 2024 theo QĐ 1859/QĐ-UBND 03/11/2025 (3.900); cấp điện thôn Sín Chải theo QĐ 2226/QĐ-UBND 27/6/2025 (134); cấp điện thôn Lếch Mông theo QĐ 2206/QĐ-UBND 27/6/2025 (311).
- Khởi công mới (biểu 02.1) — 81.102, cả ba theo QĐ ngày 28/4/2026: xã Sơn Lương 37.500 (QĐ 1413); thôn Đề Chơ, xã Phình Hồ 6.102 (QĐ 1411); xã Khao Mang, Mù Cang Chải, Lao Chải 37.500 (QĐ 1412).

### Ba bẫy đã ghi cảnh báo trong ref 09

1. **03 dự án khởi công mới được xếp ở lĩnh vực "Nông nghiệp và phát triển nông thôn, phòng chống, khắc phục thiên tai"**, không phải lĩnh vực công nghiệp/năng lượng. Xếp sai lĩnh vực sẽ lệch số với Sở Tài chính.
2. **Tên dự án giữ địa danh cũ, địa điểm ghi xã mới**: "thôn Sín Chải, xã Trung Chải, thị xã Sa Pa" nhưng địa điểm là xã Tả Phìn; "xã Thanh Bình, thị xã Sa Pa" nhưng địa điểm là xã Bản Hồ.
3. **Bẫy đọc file**: bản .doc lưu hành nội bộ là dự thảo trình ký, ô số/ngày TRỐNG; chỉ bản PDF đã ký mới có số 2390 và ngày 09/7/2026. Phải GATE PDF trước khi viện dẫn.

Ranh giới sử dụng: reference 09 chỉ dùng cho **cấp điện nông thôn bằng ngân sách tỉnh**; nguồn điện, TBA, đường dây 110-500 kV vẫn tra reference 02, 03 (vốn do ngành điện/nhà đầu tư bố trí, không qua ngân sách tỉnh).

### Thay đổi SKILL.md

- Thêm dòng reference 09 vào bảng mục III.
- Bổ sung phạm vi "tra vốn đầu tư công cấp điện nông thôn của Sở Công Thương (QĐ 2390/QĐ-UBND 09/7/2026)" và từ khoá "cấp điện nông thôn" vào `description`; rút gọn các cụm dài để giữ description trong giới hạn 1024 ký tự (còn 1022).

Liên kết: phần KCN/CCN của cùng quyết định → plugin `kccn-sct-vn` reference 22; nguồn thu đóng góp khai thác khoáng sản → `qlks-sct-vn` reference 15. File PDF gốc lưu tại `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/QD-2390-2026-KH-dau-tu-cong-trung-han-2026-2030.pdf`.
