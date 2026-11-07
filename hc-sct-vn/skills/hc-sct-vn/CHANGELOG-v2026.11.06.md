# CHANGELOG — hc-sct-vn v1.9.0 (06/11/2026)

- **Reference 20 (mới) — Sổ theo dõi cơ sở hoạt động hóa chất, GCN/GP đã cấp:** 17 DN còn GCN đủ điều kiện cấp trước 01/01/2026 (dùng đến 31/12/2027, bảng số/ngày/phạm vi); 5 GP nhập khẩu nhóm 1 UBND tỉnh đã cấp (3384, 3385, 3387 ngày 18/9/2026; 3509, 3510 ngày 28/9/2026); GP Cục Hóa chất 1844/GP-HC 23/9/2026 cấp Triều Dương; GP Thái Nguyên 598, 599/GP-SCT gửi về (cơ sở LNS mua H2SO4); kết quả kiểm tra 04 đơn vị 2026 (Khí công nghiệp Lào Cai: BB VPHC, QĐ XPHC 3364/QĐ-XPHC 10/6/2026); đợt kiểm tra sự cố 12/2025; 25 DN đã / 12 DN chưa báo cáo 2025; KH/BP đang theo dõi; danh sách chỗ còn phải đối chiếu bản gốc.
- **`data/so-theo-doi-hoa-chat.csv`** (mới, máy đọc, 52 cơ sở; chỉ tên công ty và số giấy phép — không mã số DN, địa chỉ) xuất từ web nội bộ mục Hóa chất; MCP `tra_doanh_nghiep` đọc được.
- **SKILL.md:** câu hỏi gác cổng số 0 "DN này đã có gì trong sổ theo dõi?" trước 4 câu hỏi cũ; bảng reference thêm 20. **Ref 16** thêm mục 5d.
- Nguồn: 3 tệp Bạn gửi 06/11/2026 (bản quét, OCR; bản gốc ở kho riêng vlncn-laocai-files; bản chữ trong sổ văn bản plugin van-ban-sct-vn).
- `plugin.json` 1.8.1 → 1.9.0.

# CHANGELOG — hc-sct-vn v1.9.1 (07/11/2026)

- `data/so-theo-doi-hoa-chat.csv` thêm cột `ma_so_dn`, `dia_chi` (Bạn chốt 06/11/2026: thông tin đăng ký doanh nghiệp là công khai, đưa vào sổ; vẫn không có điện thoại, người đại diện). Ref 20 ghi rõ.
- `plugin.json` 1.9.0 → 1.9.1.

# CHANGELOG — hc-sct-vn v1.9.2 (07/11/2026)

- Ref 20: bản sổ đủ mã số DN, địa chỉ nay do web nội bộ tự xuất vào plugin riêng van-ban-sct-vn và MCP `tra_doanh_nghiep` 1.0.2 đọc thẳng (Bạn chốt 07/11/2026 "mọi thứ phải tự động"); kho công khai giữ bản rút gọn.

# CHANGELOG — hc-sct-vn v1.9.3 (07/11/2026)

- **Reference 21 (mới) — Quy trình tự động của sổ theo dõi hóa chất:** sơ đồ dây chuyền Bạn gửi GP/GCN → Claude nạp CSDL web → workflow `plugin-van-ban.yml` xuất sổ đủ mã số DN, địa chỉ vào plugin riêng `van-ban-sct-vn` → MCP `tra_doanh_nghiep` đọc thẳng; hai việc Claude làm trong phiên và việc cấm làm tay; cách kiểm tra dây chuyền; lỗi lượt 641 (CSV unstaged) đã sửa ở PR #163 kho riêng; ranh giới công khai – riêng tư.
- SKILL.md bảng reference thêm 21; `plugin.json` 1.9.2 → 1.9.3.
