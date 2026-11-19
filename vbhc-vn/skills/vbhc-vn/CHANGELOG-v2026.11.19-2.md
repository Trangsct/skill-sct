# vbhc-vn 2.43.0 — 19/11/2026 — Cấm lề đoạn âm ở trích yếu (R30, L018)

- **Nguồn:** công văn 19/11/2026, trích yếu nới bằng lề đoạn âm; Phó Giám đốc chuyển PDF bằng Word thì chữ bị che hai bên (Bạn chỉ ra).
- **scripts/noi_o_trich_yeu.py (mới):** nới ô "V/v" bằng lưới bảng, cân hai bên, bỏ lề âm; `--check` báo lề âm trong bảng đầu trang.
- **scripts/qa_rules.py — R30 (mới, FAIL):** bảng đầu trang có lề đoạn âm. File lỗi `tests/fail/r30-trich-yeu-le-am.docx`.
- Sổ lỗi L018; L015 bỏ cách "lề trái đoạn âm" (lịch sử); SKILL.md Nhóm G, bảng lệnh; "R01–R29" → "R01–R30". `plugin.json` → 2.43.0.
