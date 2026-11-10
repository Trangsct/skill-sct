# CHANGELOG — vbhc-vn v2.39.0 (10/11/2026)

- `scripts/qa_rules.py`: quy tắc **R27 (FAIL)** — phiếu trình "Kính gửi … Giám đốc Sở" có đủ 4 người ký: chuyên viên → Phó Trưởng phòng → Trưởng phòng → Phó Giám đốc phụ trách (bảng ký Phòng ba ô, mục ý kiến Phó Giám đốc); Giám đốc ký thẳng văn bản được trình nên phiếu trình không có mục, ô ký Giám đốc (có thì FAIL). Bạn chốt 10/11/2026.
- `tests/fail/r27-phieu-trinh-giam-doc-thieu-luong.docx` + `.expect` (sinh bằng `tests/tao_file_loi.py` từ mẫu phiếu trình thật); hồi quy xanh.
- `reference/so-loi-tu-ghi.md`: L015; `tests/rule-inventory.md`: dòng R27; SKILL.md R01–R27.
- `plugin.json` 2.38.1 → 2.39.0.
