# CHANGELOG — kccn-sct-vn v1.64.0 (05/11/2026)

Nguồn: bản giao việc xây máy chủ MCP tra cứu (plugin `tra-cuu-sct-vn`).

- `data/danh-muc-kcn-ccn-qd525.csv` (mới): danh mục máy đọc 20 KCN (5.797 ha) + 54 CCN (2.927,81 ha) theo QĐ 525/QĐ-UBND 25/02/2026, trích từ references 12, 13; kèm 11 CCN rút khỏi quy hoạch (nhóm III), Púng Luông (nhóm VI), KCN Đông Phố Mới (ngoài Phụ lục II) để tra tên; cột ghi chú ghi địa danh dễ nhầm và mốc đã có Quyết định thành lập sau QĐ 525 (Mông Sơn, Yên Hợp 2, Xuân Ái). Tổng diện tích đã kiểm khớp.
- `SKILL.md`: mục 0c — khi máy chủ tra cứu đang kết nối, ưu tiên `tra_van_ban`, `trang_thai_cum`, `danh_muc_kcn_ccn` thay cho script; bảng reference thêm dòng CSV. Hướng dẫn script cũ giữ nguyên.
- `plugin.json` 1.63.0 → 1.64.0.

---

# CHANGELOG — kccn-sct-vn v1.65.0 (05/11/2026)

Nguồn: bản tin egov1 05/11/2026 và rà soát 45 việc mục Phụ trách (lượt nâng cấp plugin tự động buổi tối).

- **Văn bản quy phạm mới — Thông tư 69/2026/TT-BCT ngày 30/10/2026** (hiệu lực 18/12/2026) sửa đổi TT 14/2024/TT-BCT:
  - lưu bản gốc `van-ban-goc/2026.10.30-69.2026.TT-BCT-Sua-doi-TT-14-2024-bao-cao-CSDL-mau-van-ban-CCN.pdf` (bản quét 45 trang, ≥ 3 MB, chỉ trên GitHub) và bản chữ OCR `.txt` cùng tên (đạt kiểm tra chất lượng); số, ngày đọc trên trang 1 bản gốc (chữ ký số Bộ Công Thương 30/10/2026);
  - `references/55-...` mới: bảng đối chiếu Điều 1–4 TT 69/2026 ↔ Điều 1, khoản 3 Điều 3, khoản 1 Điều 4, Phụ lục I, II TT 14/2024; chuỗi báo cáo 06 biểu (Sở nộp Biểu 05, 06 về Cục Công nghiệp trước 30/6 và 31/12; xã Biểu 03, 04; xã đầu mối cho CCN liên xã); Phụ lục II Mẫu 01–04; áp dụng cho kỳ báo cáo cả năm 2026; 3 anti-error;
  - ref 01 (khung pháp lý) thêm dòng TT 69/2026; ref 09 ghi chú quy định cũ là lịch sử từ 18/12/2026.
- `references/54-...` **mục I**: QĐ 4154/QĐ-UBND ngày 04/11/2026 thành lập Hội đồng, Tổ giúp việc đánh giá lựa chọn chủ đầu tư CCN công nghệ cao Phú Thịnh 6 (bãi bỏ QĐ 3273/QĐ-UBND 11/9/2026): thành phần, nhiệm vụ; VB 7297/SCT-CN 04/11/2026.
- `SKILL.md`: dòng ref 55 mới, dòng ref 54 thêm mục I.
- `registry/trang-thai.csv`: TT 14/2024 (bị sửa đổi bởi TT 69/2026), TT 69/2026 (ban hành 30/10/2026, hiệu lực 18/12/2026).
- `plugin.json` 1.64.0 → 1.65.0.
