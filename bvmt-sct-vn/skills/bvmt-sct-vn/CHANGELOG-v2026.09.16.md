# CHANGELOG bvmt-sct-vn v1.5.2 — 16/9/2026

## Rút gọn description trong plugin.json về dưới 500 ký tự

- `.claude-plugin/plugin.json`: description **599 → 492 ký tự**. Bỏ phần diễn giải mốc thời hạn (Sở NN&MT dự thảo Kế hoạch UBND tỉnh trước 05/10/2026, đề xuất phần ngành trước 30/9/2026) và ngày của CV 2449-CV/ĐU — các mốc này vẫn giữ nguyên, đầy đủ trong `SKILL.md` và reference; description chỉ còn giữ tên văn bản để kích hoạt skill.
- Lý do: trình upload plugin của Claude từ chối gói có description > 500 ký tự; `scripts/check_descriptions.py` và CI `validate-plugins.yml` đang báo đỏ vì mục này. Phát hiện khi chạy bộ kiểm tra bắt buộc trước khi push đợt kccn-sct-vn 1.36.0 / dacn-sct-vn 1.6.0.
- `plugin.json` → **1.5.2**. Không đổi nội dung nghiệp vụ.
