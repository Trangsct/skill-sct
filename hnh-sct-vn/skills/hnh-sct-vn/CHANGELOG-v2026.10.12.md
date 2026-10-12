# CHANGELOG — hnh-sct-vn v1.11.5 (12/10/2026)

Sửa tên nơi nộp hồ sơ thủ tục hành chính (Bạn chốt 12/10/2026, đối chiếu giao diện https://motcua-tthc.moit.gov.vn/): tên đúng là **"Hệ thống thông tin giải quyết thủ tục hành chính Bộ Công Thương"**, không phải "Cổng dịch vụ công một cửa Bộ Công Thương". Địa chỉ và quy ước nơi nộp duy nhất giữ nguyên.

- Thay tên gọi tại: `references/08-faq-doanh-nghiep.md`; `references/14-bo-mau-van-ban.md`; `references/16-thuc-tien-cap-phep-sct.md`; `references/19-nguyen-tac-nghiep-vu-bat-bien.md` (nguyên tắc 2 ghi thêm tên gọi đúng); `mau-ho-so/00-huong-dan-lap-ho-so.md`.
- `scripts/check_facts.py` ở gốc kho: rule mới `ten-he-thong-tthc-bct` (FAIL khi còn ghi "Cổng dịch vụ công một cửa"); rule `noi-nop-dvcqg` thu hẹp, chỉ chặn hệ thống giải quyết thủ tục hành chính **của tỉnh**.
- CHANGELOG cũ giữ nguyên làm lịch sử.
- `plugin.json` → 1.11.5.
