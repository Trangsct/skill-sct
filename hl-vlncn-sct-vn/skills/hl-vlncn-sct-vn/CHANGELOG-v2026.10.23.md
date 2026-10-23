# CHANGELOG — hl-vlncn-sct-vn 1.5.3 (23/10/2026)

- `references/so-loi-tu-ghi.md` MỚI (tạo bằng `check_anti_error_format.py --tao`), L001: GCN 31/GCN-SCT ngày 27/01/2026 in số định danh 11 chữ số (rơi số 0 đầu do cột Excel dạng số); cách đúng: đủ 12 chữ số, cột dạng văn bản, soát độ dài trước khi in. Phát hiện khi rà thông báo bổ sung thủ kho (sd-vlncn-sct-vn ref 14, anti-error 38).
- SKILL.md: cấu trúc thêm dòng sổ lỗi.
- Máy kiểm: rule `so-dinh-danh-du-12-chu-so` (WARN) trong `scripts/check_facts.py`.
- `plugin.json` 1.5.2 → 1.5.3. Chi tiết: `CHANGELOG-v2026.10.23.md`.
