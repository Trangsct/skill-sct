# CHANGELOG — dacn-sct-vn v1.10.0 (17/10/2026)

Nguồn: bản giao việc nâng cấp hệ plugin 17/10/2026, mục 2 và mục 5.

- SKILL.md: mục dàn ý văn bản dài theo GATE 0b của vbhc-vn 2.31.0 (Bạn chốt 17/10/2026) — lập dàn ý theo dàn ý mặc định hoặc mẫu gần nhất trong kho, ghi `ke-hoach-soan.txt`, viết thân ngay, không gửi dàn ý xin duyệt trừ khi Bạn yêu cầu; giao file báo một dòng "Dàn ý theo mẫu …".
- Mục II-b (mới): dàn ý mặc định kế hoạch cấp tỉnh (I–VII theo mẫu KH 427/KH-UBND, lấy từ `scripts/bai-toan-lon-2/noi_dung_bt2.py`), báo cáo chuyên đề, đề án (Dự thảo Đề án 13).
- Tệp trạng thái hồ sơ `trang-thai/bai-toan-lon-so-2.md`, `trang-thai/kh-130-cong-nghiep-vat-lieu.md` ở gốc kho (Kế hoạch 130 chưa có văn bản trong kho).
- `plugin.json` → 1.10.0.
- `scripts/tim_van_ban.py` (bản chép): sửa lỗi không tìm được số hiệu có chữ Đ (NĐ-CP, QĐ-UBND) — biểu thức `[đ[dđ]]` làm script kết luận sai "chưa có trong kho" (phát hiện 17/10/2026 khi kiểm thử C3).
