# Hướng dẫn cài đặt / cập nhật plugin vbhc-vn

## Cài mới (khuyến nghị: xóa bản cũ, cài bản mới hoàn toàn)

1. Trong Claude.ai: Settings → Capabilities (hoặc mục quản lý Skills/Plugins) → gỡ skill/plugin `vbhc-vn` cũ (cả bản user skill lẫn bản plugin nếu có 2 bản — tránh trùng trigger).
2. Tải lên file `vbhc-vn-vX.Y.Z.zip` (bản mới nhất trong repo `Trangsct/skill-sct`).
3. Kiểm tra sau cài: hỏi Claude "kiểm tra plugin vbhc-vn" — Claude phải đọc được `SKILL.md` tại `/mnt/skills/plugins/vbhc-vn:vbhc-vn/SKILL.md`.

## Cấu trúc gói (chuẩn plugin từ 04/7/2026)

```
vbhc-vn-vX.Y.Z.zip
├── .claude-plugin/plugin.json     ← manifest (bắt buộc, ở gốc zip)
└── skills/vbhc-vn/
    ├── SKILL.md                   ← description ≤ 1024 bytes UTF-8
    ├── templates/  (09 mẫu trắng)
    ├── examples/   (17 mẫu thật: 11 sct + 6 ubnd)
    ├── reference/  (thể thức NĐ 30, 8 nhóm anti-error, công cụ kỹ thuật...)
    └── scripts/    (fill_template, extract_metadata, check_document, qa_pdf_check)
```

## Quy trình bắt buộc sau mỗi lần build/chỉnh/nâng cấp

1. Chạy validator đóng gói (kiểm description bytes, ASCII paths, cấu trúc zip) TRƯỚC khi xuất.
2. Cập nhật `CHANGELOG.md` (bắt buộc, không cần nhắc).
3. Push GitHub repo `Trangsct/skill-sct` — nếu phiên Claude.ai không có credentials thì tải zip về và push thủ công (hoặc dùng Claude Code có GitHub App).

## Ghi chú đường dẫn

Skill cài dạng **plugin** nằm tại `/mnt/skills/plugins/vbhc-vn:vbhc-vn/`; cài dạng **user skill** nằm tại `/mnt/skills/user/vbhc-vn/`. Các script trong tài liệu viết theo đường dẫn plugin — nếu dùng bản user skill thì thay tiền tố tương ứng.
