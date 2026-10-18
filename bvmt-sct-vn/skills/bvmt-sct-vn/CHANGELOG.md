# CHANGELOG bvmt-sct-vn

## 1.7.1 — 18/10/2026 — Căn cứ chức năng Sở: QĐ 3628/QĐ-UBND ngày 02/10/2026 thay QĐ 05/2025/QĐ-UBND (chuyển từ PR 112/115)

- Thay dẫn QĐ 05/2025/QĐ-UBND → **QĐ 3628/QĐ-UBND ngày 02/10/2026** (Quy định CNNV, quyền hạn, cơ cấu tổ chức Sở Công Thương — 06 phòng, có Phòng Quản lý khoáng sản; không có khu công nghiệp) trong mẫu văn bản, reference: `references/11-kl75-ctr31-ctr104-tu-trien-khai-sct.md`. Dòng nói về văn bản đã ký trước 02/10/2026 giữ nguyên dẫn cũ, ghi "lịch sử". Nguồn: `sct-laocai-org-vn` ref 04; bản gốc + `.txt`: `sct-laocai-org-vn/skills/sct-laocai-org-vn/van-ban-goc/2026.10.02-QD-3628-QD-UBND.pdf`. Máy kiểm: rule `qd-05-2025-da-thay-bang-qd-3628` trong `scripts/check_facts.py`.
- `plugin.json` 1.7.0 → 1.7.1.

## 1.7.0 — 17/10/2026 — Sửa tim_van_ban.py không tìm được số hiệu có chữ Đ

- `scripts/tim_van_ban.py` (bản chép từ gốc kho, đồng bộ bằng `build_so_cai_van_ban_goc.py`): sửa lỗi biểu thức tìm — chữ "đ" bị thay hai lần thành `[đ[dđ]]` nên MỌI số hiệu có chữ Đ (NĐ-CP, QĐ-UBND, QĐ-TTg) không bao giờ khớp và script kết luận sai "chưa có trong kho" (phát hiện 17/10/2026 khi kiểm thử GATE 0). Sau khi sửa: "181/2024/NĐ-CP" khớp 3 mục danh mục.
- `plugin.json` → 1.7.0. Chi tiết: `CHANGELOG-v2026.10.17.md`.

