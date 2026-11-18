# CHANGELOG — kccn-sct-vn v1.67.1 (18/11/2026)

Nguồn: phiên tổng hợp ý kiến các cơ quan theo Công văn 7485/SCT-CN, hoàn thiện Tờ trình phê duyệt Đề án di dời CCN Đầm Hồng.

- ref 45 mục B: thêm 5 điểm soát Đề án di dời (căn cứ đã bị thay — Luật Đầu tư 143/2025/QH15, Luật Xây dựng 135/2025/QH15, QĐ 49/2026/QĐ-UBND
  bãi bỏ QĐ 15/2024/QĐ-UBND tỉnh Yên Bái; phạm vi giao việc Sở Tài chính; công nghệ lạc hậu; ranh giới phần cụm từng phường; cơ quan được
  hỏi ý kiến phải có trong phân công) và cách lập Phụ lục tổng hợp ý kiến kèm Tờ trình.
- `plugin.json` 1.67.0 → 1.67.1.

# CHANGELOG — kccn-sct-vn v1.67.2 (18/11/2026, lần 2)

- ref 45 mục B: căn cứ bảo vệ doanh nghiệp thứ cấp khi di dời cụm — điểm m khoản 3 Điều 124 Luật Đất đai + Điều 44a NĐ 102/2024 (bổ sung bởi
  NĐ 49/2026); phạm vi khoản 6 Điều 202 (chỉ thuê lại của chủ đầu tư hạ tầng); thẩm quyền hỗ trợ khác (UBND tỉnh quy định, UBND cấp xã quyết
  định theo khoản 12 Điều 3 NQ 254/2025/QH15, khoản 1 Điều 10 NĐ 151/2025); thông báo thu hồi đất 120 ngày (NQ 254); phân định trách nhiệm có
  lợi cho Sở.
- `plugin.json` 1.67.1 → 1.67.2.

## 1.67.3 (18/11/2026, lần 3) — thẩm quyền, điều kiện thu hồi đất khi di dời cụm

- Ref 45 mục 16–19: không dẫn Điều 5, 9, 10 NĐ 151/2025 (hết hiệu lực từ 31/01/2026 theo điểm đ khoản 3 Điều 16 NĐ 49/2026); thẩm quyền
  thu hồi đất theo Điều 83 Luật Đất đai, khoản 1 Điều 14 NĐ 49/2026, Điều 3 QĐ 40/2026/QĐ-UBND (tổ chức theo Điều 81, 82 → UBND tỉnh);
  thu hồi theo Điều 79 cần dự án cụ thể và điều kiện Điều 80; quản lý hiện trạng dựa thủ tục có thật (khoản 4 Điều 76); giảm tiền thuê
  lại đất cho doanh nghiệp nhỏ và vừa (khoản 1 Điều 32 NĐ 32 sửa tại NĐ 303). Sửa mục 11 (hai vế điểm đ khoản 3 Điều 124), mục 13.
- `scripts/check_facts.py`: rule `nd151-dieu-5-9-10-het-hieu-luc` (FAIL).
