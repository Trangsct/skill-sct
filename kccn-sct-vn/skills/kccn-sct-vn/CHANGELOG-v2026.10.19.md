# CHANGELOG — kccn-sct-vn v1.54.0 (19/10/2026)

- **Bản gốc QĐ 3865/QĐ-UBND ngày 17/10/2026** (UBND tỉnh thành lập CCN Xuân Ái, xã Xuân Ái, tỉnh Lào Cai — Bạn gửi 19/10/2026;
  số, ngày, người ký đọc bằng `extract_metadata.py`): lưu `van-ban-goc/2026.10.17-3865.QD.UBND-Thanh-lap-CCN-Xuan-Ai.pdf`
  (1,2 MB, vào gói claude.ai) + bản trích chữ `.txt` cùng tên (pdftotext, đạt kiểm tra). Quyết định cá biệt, không có bản Word.
- **references/48 (mới)**: thông tin văn bản, căn cứ (KL 408-KL/TU 12/10/2026, TTr 5723/TTr-SCT 14/9/2026; căn cứ NĐ 32/2024 theo
  chuyển tiếp k2 Đ35 NĐ 303/2026); 10 khoản Điều 1 (75 ha, thôn Quyết Hùng, 17 ngành nghề, CĐT Công ty CP LAMSEN Industrial Lào Cai,
  TMĐT 815,596 tỷ — vốn CSH 18,39%, tiến độ 39 tháng từ ngày QĐ ≈ 17/01/2030, thời hạn 50 năm); Điều 3 trách nhiệm (ký quỹ, XLNT
  trước khi nhận dự án thứ cấp, bãi bỏ theo k2 Đ12 NĐ 32/2024; Sở đầu mối; xã Xuân Ái chủ trì GPMB); **bảng tọa độ 18 mốc VN-2000
  đọc từ ảnh phụ lục + WGS84**, diện tích tính lại 75,00 ha; hệ quả: 26 CCN đã thành lập, 10 cụm doanh nghiệp làm CĐT, 04 cụm thành
  lập năm 2026; việc tiếp theo.
- Ref 12 (dòng Xuân Ái, địa danh dễ nhầm), ref 31 mục 14 (sổ chốt), ref 39 bậc 10 (mẫu QĐ 3865); ref 30, 41, 43, 44: 10 dòng
  "đã trình / chờ Quyết định thành lập" của Xuân Ái ghi kèm "lịch sử — QĐ 3865, ref 48". SKILL.md: dòng ref 48, địa danh dễ nhầm.
- `scripts/check_facts.py`: rule `ccn-xuan-ai-da-thanh-lap-qd-3865` (FAIL); tách lại 2 rule `qd-05-2025-da-thay-bang-qd-3628`,
  `ubnd-viet-tat-noi-nhan-trong-mau` bị dồn chung một dict với rule `qd-1894-…` (thiếu dấu đóng, chỉ rule cuối có hiệu lực) —
  bật lại vẫn 0 FAIL.
- Hồ sơ `trang-thai/ccn-xuan-ai.md` (mới, GATE "Đọc trạng thái hồ sơ").
- `plugin.json` 1.53.0 → 1.54.0.
