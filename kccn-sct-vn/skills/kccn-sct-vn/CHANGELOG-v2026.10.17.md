# CHANGELOG — kccn-sct-vn v1.51.0 (17/10/2026)

Nguồn: bản giao việc nâng cấp hệ plugin 17/10/2026 (mục 2 — dàn ý; mục 5 — tệp trạng thái hồ sơ dùng chung).

- **Tệp trạng thái hồ sơ** (`trang-thai/` ở gốc kho skill-sct): khởi tạo `ccn-phu-thinh-1`, `ccn-thong-nhat-1`,
  `ccn-mong-son`, `ccn-chau-que` từ ref 13–46. `scripts/trang_thai_cum.py` giữ nguyên cách dùng, in thêm đường dẫn tệp
  trạng thái trùng tên cụm (tra dòng "Bí danh:") và — khi dòng mới nhất trong plugin quá 07 ngày — lấy bậc theo tệp đó thay
  vì hỏi lại Bạn. `SKILL.md` mục 0: thêm một gạch đầu dòng về tệp trạng thái.
- **Ref 26**: đính chính ngày QĐ 2736/QĐ-UBND thành lập Hội đồng lựa chọn chủ đầu tư CCN Mông Sơn là **06/8/2026** (bản
  gốc `van-ban-goc/QD-2736-2026-HD-lua-chon-CDT-CCN-Mong-Son.pdf`), trước ghi nhầm 07/8/2026.
- `plugin.json` → 1.51.0.
