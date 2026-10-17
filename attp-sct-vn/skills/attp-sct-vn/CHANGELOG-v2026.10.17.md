# CHANGELOG — attp-sct-vn v1.7.0 (17/10/2026)

Nguồn: bản giao việc nâng cấp hệ plugin 17/10/2026 (kiểm thử tổng thể C3).

- `scripts/tim_van_ban.py` (bản chép từ gốc kho, đồng bộ bằng `build_so_cai_van_ban_goc.py`): sửa lỗi biểu thức tìm — chữ "đ" bị thay hai lần thành `[đ[dđ]]` nên MỌI số hiệu có chữ Đ (NĐ-CP, QĐ-UBND, QĐ-TTg) không bao giờ khớp và script kết luận sai "chưa có trong kho" (phát hiện 17/10/2026 khi kiểm thử GATE 0). Sau khi sửa: "181/2024/NĐ-CP" khớp 3 mục danh mục.
- `plugin.json` 1.6.1 → 1.7.0.
