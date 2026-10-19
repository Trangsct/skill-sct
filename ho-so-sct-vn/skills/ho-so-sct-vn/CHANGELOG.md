# CHANGELOG — ho-so-sct-vn v1.0.1 (19/10/2026)

- Bản chép `trang-thai/` sinh lại: thêm hồ sơ `ccn-xuan-ai.md` (CCN Xuân Ái — QĐ 3865/QĐ-UBND ngày 17/10/2026, bậc 10) và các thay
  đổi tệp trạng thái từ 18/10/2026 (bai-toan-lon-so-2, ccn-thong-nhat-1) chưa nâng bản. `plugin.json` 1.0.0 → 1.0.1.

# CHANGELOG — ho-so-sct-vn v1.0.0 (18/10/2026)

- Plugin mới (đề xuất 2 sau bản giao việc 17/10/2026): bản chép `trang-thai/` và 5 script trạng thái hồ sơ của gốc kho
  để phiên trên claude.ai đọc được GATE "Đọc trạng thái hồ sơ" và ghi nhật ký tạm (`--tam`). Máy sinh bởi
  `scripts/build_ho_so_plugin.py` (ghi_nhat_ky.py tự gọi; CI kiểm khớp qua check_descriptions.py) — không sửa tay bản chép.
