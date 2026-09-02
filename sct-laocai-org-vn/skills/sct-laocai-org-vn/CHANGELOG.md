# CHANGELOG — sct-laocai-org-vn

## [2.1.1] - 02/9/2026 — nơi nộp TTHC duy nhất motcua-tthc.moit.gov.vn
- Nơi nộp hồ sơ TTHC: DUY NHẤT Cổng dịch vụ công một cửa Bộ Công Thương https://motcua-tthc.moit.gov.vn/ (đăng nhập VNeID) — Bạn chốt lại 02/9/2026. Bỏ mọi cách ghi "kênh phụ"/"hoặc qua" Trung tâm Phục vụ hành chính công, bưu chính, trực tiếp, "Cổng DVCQG", "Hệ thống TTGQ TTHC tỉnh" trong hướng dẫn DN; trích luật thì ghi rõ là trích luật.

## [2.1.0] - 02/9/2026 — tinh gọn SKILL.md (42,2k → 37k ký tự)
- Chức năng, nhiệm vụ chi tiết 6 phòng theo QĐ 59/QĐ-SCT (nguyên văn) tách sang `references/01-chuc-nang-nhiem-vu-cac-phong-qd59.md` (kèm chế độ báo cáo nội bộ Phòng QLCN); SKILL.md giữ tóm tắt 1 dòng/phòng để định tuyến.
- Giữ nguyên trong SKILL.md phần dùng hằng ngày: cơ cấu nội bộ Phòng QLCN, chuyên viên ↔ lĩnh vực, phân tầng duyệt, routing trình Lãnh đạo Sở, người soạn/người ký, bảng routing nhanh, quy tắc soạn văn bản phân công, sai lầm thường gặp.
- Mục CHANGELOG cũ trong SKILL.md chuyển sang file này (phần "Lịch sử trước 02/9/2026").
- plugin.json 2.0.4 → **2.1.0**.

Nhật ký thay đổi của plugin (Cơ cấu tổ chức, phân công Sở Công Thương). Lịch sử trước 02/9/2026 xem CHANGELOG.md ở gốc repo (tìm theo tên plugin) và `git log -- sct-laocai-org-vn/`.

## [2.0.4] - 02/9/2026 — khởi tạo CHANGELOG trong thư mục skill
- Rà soát tổng thể 02/9/2026: plugin đúng cấu trúc, description trong ngưỡng, không phát hiện dữ kiện lỗi thời cần sửa. Phiên bản giữ nguyên 2.0.4.
- Từ nay mỗi lần nâng cấp ghi mục mới lên đầu file này (theo CLAUDE.md của repo).

## Lịch sử trước 02/9/2026 (chuyển từ mục CHANGELOG cũ trong SKILL.md)
- **v2.0.1 (15/7/2026)**: chốt 2 điểm mở theo xác nhận của Bạn — **KCN → CN(Trung)**; **HHNH toàn bộ (cấp GP vận chuyển + an toàn/tập huấn) → CN(Linh)** từ 15/7/2026; giai đoạn 6/7–14/7/2026 hồ sơ HHNH giữ CN(Khôi) đúng lịch sử; đồng bộ bảng routing, dòng Lưu, liên kết hnh-sct-vn, mục sai lầm.
- **v2.0 (14/7/2026)**: viết lại toàn bộ mục "Cơ cấu nội bộ Phòng QLCN" theo **Thông báo phân công ngày 10/7/2026** (TP Nguyễn Hữu Long ký, không số, hiệu lực 10/7/2026): 1 TP + **3 PTP** (Nguyễn Hồng Vân, Trần Trọng Trang, Đỗ Mạnh Cường) + 10 chuyên viên; VLNCN + CCN + KHCN-ĐMST CN → TP trực tiếp chỉ đạo; VLNCN chuyển CN(Linh) → **CN(Khôi)**; ATTP chuyển CN(Dương) → **CN(Nam)** (chuyên viên mới Lã Doãn Nam); Dương → chất lượng SPHH + SXTD bền vững; Linh → an toàn ngành/HHNH (an toàn)/kiểm định/PCCC/thăm dò - đóng cửa mỏ; thêm phân tầng duyệt theo PTP, chế độ báo cáo nội bộ (10h thứ Sáu/ngày 25/15-01/đoàn kiểm tra 01-03 ngày), 2 điểm mở (KCN, thụ lý cấp GP HHNH) phải hỏi Bạn; quy ước CN(V.Cường)/CN(M.Cường) tránh trùng tên; bảng liên kết hệ sinh thái plugin kèm nguyên tắc single source of truth; 4 mục sai lầm mới.
- **v1.x (đến 02/2026)**: bản theo phân công nội bộ cũ (1 PTP Trần Trọng Trang) + Dự thảo Lần 4 phân công BGĐ.
