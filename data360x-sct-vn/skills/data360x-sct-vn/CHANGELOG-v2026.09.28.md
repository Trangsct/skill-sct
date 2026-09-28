# data360x-sct-vn 1.0.6 — 28/9/2026

- Sửa lỗi khiến claude.ai báo **"Sync failed"** cho cả marketplace `skill-sct`: description trong frontmatter SKILL.md chứa ký tự `<` `>` (`danh-muc-<năm>.json`), trình đồng bộ skill của claude.ai không nhận. Đổi thành `danh-muc-NĂM.json`; thân SKILL.md không đổi.
- `scripts/check_descriptions.py` thêm bước chặn ký tự `<` `>` trong description của plugin.json và của mọi SKILL.md (CI validate-plugins.yml đỏ nếu tái phạm).
