# CHANGELOG — tra-cuu-sct-vn v1.0.1 (06/11/2026)

- Máy chủ sct-mcp 1.0.1: `tra_doanh_nghiep` đọc thêm sổ theo dõi dạng bảng kèm plugin (`<plugin>/skills/<plugin>/data/*.csv`) — trước hết là `hc-sct-vn/data/so-theo-doi-hoa-chat.csv` (52 cơ sở hoạt động hóa chất) — trả trường `so_theo_doi_plugin`; sổ văn bản (kho riêng) nay có bản chữ OCR 39 GCN/GP, hồ sơ kiểm tra hóa chất 2018–2026 nên `tra_van_ban_den_di "47/GCN-SCT"` tra được.
- `plugin.json` 1.0.0 → 1.0.1.

# CHANGELOG — tra-cuu-sct-vn v1.0.2 (07/11/2026)

- Máy chủ 1.0.2: `tra_doanh_nghiep` trả `so_theo_doi_hoa_chat`, mã số DN, địa chỉ từ sổ theo dõi hóa chất trong kho riêng (web nội bộ tự xuất mỗi lần dựng plugin).
