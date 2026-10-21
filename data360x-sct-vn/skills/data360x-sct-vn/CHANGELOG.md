# CHANGELOG data360x-sct-vn

## 1.3.0 — 21/10/2026 — Từ 10/10/2026 nguồn văn bản là EGOV

- `SKILL.md` khối cảnh báo EGOV; quy tắc 4 thêm câu trả lời cho văn bản sau 10/10/2026; ref 03 mục 7 (công cụ soi EGOV, lộ trình
  bot EGOV). Chi tiết: `CHANGELOG-v2026.10.21.md`.

## 1.2.0 — 17/10/2026 — Sửa tim_van_ban.py không tìm được số hiệu có chữ Đ

- `scripts/tim_van_ban.py` (bản chép từ gốc kho, đồng bộ bằng `build_so_cai_van_ban_goc.py`): sửa lỗi biểu thức tìm — chữ "đ" bị thay hai lần thành `[đ[dđ]]` nên MỌI số hiệu có chữ Đ (NĐ-CP, QĐ-UBND, QĐ-TTg) không bao giờ khớp và script kết luận sai "chưa có trong kho" (phát hiện 17/10/2026 khi kiểm thử GATE 0). Sau khi sửa: "181/2024/NĐ-CP" khớp 3 mục danh mục.
- `plugin.json` → 1.2.0. Chi tiết: `CHANGELOG-v2026.10.17.md`.

