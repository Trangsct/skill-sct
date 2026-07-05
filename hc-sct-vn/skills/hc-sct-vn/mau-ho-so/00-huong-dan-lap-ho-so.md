# Hướng dẫn sử dụng bộ mẫu hồ sơ hóa chất

Bộ mẫu dựng theo **Phụ lục X, XI Thông tư 01/2026/TT-BCT** và **Điều 34 Nghị định
25/2026/NĐ-CP**. Placeholder dạng `…(số)…` giữ nguyên đánh số theo văn bản gốc để
tra cứu ghi chú. Khi soạn cho một hồ sơ cụ thể, thay placeholder bằng dữ liệu thực,
render kiểm tra rồi mới giao (nguyên tắc pre-delivery của Bạn).

## Danh mục mẫu

| File | Dùng cho | Người/đơn vị lập | Căn cứ |
|---|---|---|---|
| `Mau-10a-Van-ban-de-nghi-cap-GCN-SXKD-co-dieu-kien.docx` | DN đề nghị cấp GCN đủ điều kiện SX/KD hóa chất có điều kiện | Doanh nghiệp | Mẫu 10a PL X TT 01/2026 |
| `Mau-10b-Van-ban-de-nghi-cap-lai-dieu-chinh-GCN.docx` | DN đề nghị cấp lại/điều chỉnh GCN | Doanh nghiệp | Mẫu 10b PL X TT 01/2026 |
| `Mau-10c-Giay-chung-nhan-du-dieu-kien-SXKD.docx` | **Kết quả** — GCN do cơ quan có thẩm quyền cấp | Sở tham mưu, cơ quan có thẩm quyền ký | Mẫu 10c PL X TT 01/2026 |
| `Mau-11a-Van-ban-de-nghi-GCN-dich-vu-ton-tru.docx` | DN đề nghị cấp GCN dịch vụ tồn trữ hóa chất | Doanh nghiệp | Mẫu 11a PL XI TT 01/2026 |
| `Mau-Van-ban-de-nghi-tham-dinh-KH-phong-ngua-su-co.docx` | DN đề nghị thẩm định Kế hoạch phòng ngừa, ứng phó sự cố hóa chất | Doanh nghiệp | Điều 34 NĐ 25/2026 |

## Lưu ý quan trọng khi dùng Mẫu 10c (GCN kết quả)

- **Người ký (placeholder (6))** phụ thuộc **Quyết định ủy quyền của UBND tỉnh Lào Cai**:
  thẩm quyền cấp theo luật là **UBND cấp tỉnh** (Điều 9, 10, 11 Luật 69/2025; Điều 9
  NĐ 26/2026). Nếu UBND tỉnh đã ủy quyền cho **Giám đốc Sở Công Thương** thì GĐ Sở ký,
  dùng con dấu và thể thức của Sở; nếu chưa ủy quyền thì **Sở thẩm định, trình Chủ tịch
  UBND tỉnh ký**. **Đến 05/7/2026 chưa xác minh QĐ ủy quyền — phải hỏi Bạn trước khi
  chốt người ký** (xem CHANGELOG mục "Việc chờ xác minh").
- Dòng Lưu: `Lưu: VT, CN(Loan)` (Nguyễn Thị Loan — chuyên viên tham mưu hóa chất).
- Sau khi cấp phải gửi bản sao đến **Bộ Công Thương (Cục Hóa chất)** và UBND cấp tỉnh
  nơi đặt trụ sở chính/cơ sở SX-KD để phối hợp quản lý (điểm đ khoản 5 Điều 9 NĐ 26).

## Các mẫu khác trong hệ thống

- **Mẫu GCN dịch vụ tồn trữ (11c), mẫu GP hóa chất kiểm soát đặc biệt (PL VI), mẫu GP
  XNK (PL VII), mẫu đăng ký hóa chất mới (PL XII)**: khi cần, trích từ bản gốc
  `van-ban-goc/03-thong-tu/TT-01-2026-BCT-huong-dan-ND26-bieu-mau.docx` (mở đúng Phụ lục).
- **Mẫu Quyết định phê duyệt Kế hoạch phòng ngừa sự cố (PL II NĐ 25), mẫu văn bản đề
  nghị thẩm định, biên bản họp Hội đồng, phiếu đánh giá**: trích từ
  `van-ban-goc/02-nghi-dinh/ND-25-2026-...docx` và Thông tư 02/2026/TT-BCT.

Khi soạn văn bản kết quả của Sở (công văn, tờ trình, quyết định, báo cáo), kết hợp
skill `vbhc-vn` (thể thức, mẫu 08/09) và `anti-error` (chống bịa số/ngày). Nhận PDF
văn bản đến → chạy `vbhc-pdf-reader-vn`.
