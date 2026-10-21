# CHANGELOG — data360x-sct-vn v1.3.0 (21/10/2026)

Nguồn: Bạn báo 21/10/2026 — từ 10/10/2026 văn bản đi, đến chuyển sang nền tảng EGOV (`egov1.laocai.gov.vn`).

- `SKILL.md`: khối cảnh báo đầu tệp — kho `theo-doi/` dừng ở lượt quét Data360X 10/10/2026; văn bản sau mốc đó nằm trên
  EGOV, chưa có trong kho; không kết luận "không có", xin Bạn gửi tệp trực tiếp. Quy tắc 4 thêm câu trả lời chuẩn.
- `references/03-bot-va-may-co-quan.md` mục 7 (mới): nguồn EGOV, Claude không vào được egov1 từ máy chủ nước ngoài; bước 1 công
  cụ soi `egov_soi.py` + `soi-egov.bat` (ccn-laocai PR #113), nơi để kết quả `vlncn-laocai/theo-doi/egov/soi/`; bước 2 bot EGOV
  giữ nguyên đầu ra cũ.
- `scripts/check_facts.py`: rule `data360x-sau-10-10-2026-la-egov` (WARN).
- `plugin.json` 1.2.0 → 1.3.0.
