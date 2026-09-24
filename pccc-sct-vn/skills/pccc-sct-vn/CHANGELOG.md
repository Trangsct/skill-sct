# CHANGELOG — pccc-sct-vn

## [1.3.0] - 24/9/2026 — mẫu công văn triển khai NĐ 347; sửa mức phạt tổ chức; QĐ 11/2026 đã phân công kiểm tra định kỳ
- **mau-van-ban/01 MỚI** — nội dung công văn Sở hướng dẫn chủ đầu tư, cơ sở ngành Công Thương thực hiện NĐ 347/2026 + CV 6501/CAT-PCCC (đã dựng .docx trên mẫu thật vbhc-vn, QA PASS).
- **Sửa sai 1.2.0:** mức 30–50 triệu tại k3 Đ18 NĐ 106 là mức **cá nhân**; tổ chức gấp 02 lần = 60–100 triệu (k1 Đ4 NĐ 106), kèm đình chỉ 03–06 tháng (điểm a k6 Đ18, không bị NĐ 347 sửa) — ref 04, ref 16 (bảng B.7 thêm cột), SKILL.md.
- **Sửa nhận định sai:** SKILL.md IX.2 ghi "UBND tỉnh chưa phân cấp kiểm tra định kỳ, quá hạn 8 tháng" — thực tế Điều 17 khoản 1 QĐ 11/2026/QĐ-UBND ngày 29/01/2026 đã giao CQCM về xây dựng cấp tỉnh tổ chức kiểm tra PCCC hằng năm theo điểm b k2 Đ13 NĐ 105. Sửa SKILL.md mục VI, IX.2; ref 05 mục 4.3; ref 16 mục D.

## [1.2.0] - 24/9/2026 — NĐ 347/2026/NĐ-CP: chủ đầu tư tự nghiệm thu PCCC; CV 6501/CAT-PCCC
- Nguồn: NĐ 347/2026/NĐ-CP ngày 08/9/2026 (hiệu lực 15/9/2026) — toàn văn Bạn gửi 24/9/2026, lưu `van-ban-goc/ND-347-2026-ND-CP-08-9-2026-sua-doi-ND-105-2025.pdf` + `.docx`; CV 6501/CAT-PCCC ngày 23/9/2026 của Công an tỉnh (bản gốc chỉ lưu ở kho riêng tư `vlncn-laocai/theo-doi/2026/`).
- **ref 16 MỚI** — bảng điều khoản NĐ 105 bị bãi bỏ/sửa (k5 Đ6, Đ10, Mẫu PC15-PC17, k5 Đ46; điểm b, đ k7 Đ41); điểm đ k1 Đ12 mới (CĐT tự nghiệm thu, khai báo CSDL PCCC); k1 Đ6 (thẩm định PCCC chỉ trong BCNCKT; Điều 74 NĐ 217/2026 bị bãi bỏ); k2 Đ13, k3 và k8 Đ14 (Công an kiểm tra nhóm 2 PL II 02 năm/lần; kế hoạch trước 15/12, báo trước 03 ngày làm việc, biên bản PC03; kiểm tra chung thì Công an chủ trì); Phụ lục III mới (hạng D, E ≥ 30.000 m³/10.000 m²; DT sàn tính theo nhà lớn nhất); xử phạt k3, k4 Đ18 NĐ 106; chuyển tiếp Đ40; CV 6501 và việc Sở cần làm; bẫy trích yếu "66.18/2026/NĐ-CP".
- ref 04 viết lại theo cơ chế mới (quy trình 6 bước chuyển thành lịch sử); ref 05 thêm trình tự k3, k8 Đ14 (giải quyết vướng mắc CV 314/SCT-CN); sửa ref 01, 02, 03, 07, 08, 10, 11, 13; SKILL.md: khối "CẬP NHẬT 15/9/2026", khung pháp lý, Nhiệm vụ 1-3, nguyên tắc bất biến 12 mới.
- check_facts: rule `pccc-nghiem-thu-nd347`.

## [1.1.5] - 02/9/2026 — nơi nộp TTHC duy nhất motcua-tthc.moit.gov.vn
- Nơi nộp hồ sơ TTHC: DUY NHẤT Cổng dịch vụ công một cửa Bộ Công Thương https://motcua-tthc.moit.gov.vn/ (đăng nhập VNeID) — Bạn chốt lại 02/9/2026. Bỏ mọi cách ghi "kênh phụ"/"hoặc qua" Trung tâm Phục vụ hành chính công, bưu chính, trực tiếp, "Cổng DVCQG", "Hệ thống TTGQ TTHC tỉnh" trong hướng dẫn DN; trích luật thì ghi rõ là trích luật.

## [1.1.4] - 02/9/2026 — thêm GATE PDF đầu SKILL.md
- Plugin chưa có cổng đọc PDF văn bản đến bằng extract_metadata.py; bổ sung 1 đoạn ngay dưới tiêu đề (bài học vụ QĐ 5116/QĐ-SCT).

Nhật ký thay đổi của plugin (PCCC ngành Công Thương). Lịch sử trước 02/9/2026 xem CHANGELOG.md ở gốc repo (tìm theo tên plugin) và `git log -- pccc-sct-vn/`.

## [1.1.3] - 02/9/2026 — khởi tạo CHANGELOG trong thư mục skill
- Rà soát tổng thể 02/9/2026: plugin đúng cấu trúc, description trong ngưỡng, không phát hiện dữ kiện lỗi thời cần sửa. Phiên bản giữ nguyên 1.1.3.
- Từ nay mỗi lần nâng cấp ghi mục mới lên đầu file này (theo CLAUDE.md của repo).
