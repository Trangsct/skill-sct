# 11 — Bản đồ liên kết plugin (hệ sinh thái skill-sct)

qlks-sct-vn là plugin "tổng hợp ngành khoáng sản" — khi đi sâu vào nghiệp vụ chuyên biệt, chuyển sang plugin chuyên sâu và dùng đúng căn cứ của plugin đó.

| Tình huống | Plugin | Ghi chú giao diện |
|---|---|---|
| Thẩm định/từ chối/chấm dứt thẩm định TKCS, TKKT, TKBVTC; nội dung thiết kế mỏ theo TT 31/2025; thẩm quyền SCT/SXD theo nhóm KS; GATE 01/7/2026 (NĐ 217/2026) | **tkm-sct-vn** | qlks lo phần KIỂM TRA tuân thủ thiết kế + tham mưu đình chỉ; tkm lo phần THẨM ĐỊNH |
| GP sử dụng VLNCN, phương án nổ mìn, hộ chiếu nổ mìn, dịch vụ nổ mìn | **sd-vlncn-sct-vn** | qlks cung cấp ngữ cảnh mỏ (GP khai thác, công suất, thiết kế) khi thẩm định VLNCN; nguyên tắc "VLNCN phù hợp công suất khai thác" (Chỉ thị 11) |
| Kho VLNCN: thiết kế, nghiệm thu, kiểm định, QCVN 01:2019/BCT | **kho-vlncn-sct-vn** | |
| GCN huấn luyện KTAT **VLNCN, tiền chất thuốc nổ** (NĐ 181/2024, Sở huấn luyện + kiểm tra) | **hl-vlncn-sct-vn** | KHÁC GCN KTAT **khai thác khoáng sản** (TT 43/2025, UBND tỉnh cấp, chỉ hầm lò) — thuộc qlks (reference 05). Quy trình tổ chức kiểm tra có thể tái dùng mô hình Tổ kiểm tra của hl-vlncn |
| Quy hoạch: dự án/mỏ có trong quy hoạch không (QĐ 866/QĐ-TTg, QĐ 1626/QĐ-TTg, QĐ 525/QĐ-UBND 25/02/2026); tham gia ý kiến điều chỉnh quy hoạch; 6 mỏ đấu giá | **quy-hoach-ct-vn** | qlks lo "phương án khai thác, sử dụng KS nhóm I trong quy hoạch tỉnh" ở góc độ nhiệm vụ SCT; nội dung quy hoạch cụ thể tra quy-hoach-ct-vn |
| ĐTM/GPMT dự án mỏ, đóng cửa mỏ - cải tạo phục hồi (góc môi trường), ký quỹ, gyps Tằng Loỏng, Chỉ thị 26-CT/TU chi tiết, NQ 66.19 Mục VI-VII (ĐTM/GPMT) | **bvmt-sct-vn** | NQ 66.19 Phụ lục VIII (khoáng sản) thuộc qlks; các Phụ lục môi trường thuộc bvmt |
| BCNCKT, điều kiện khởi công, GPXD, KTCTNT, sự cố công trình mỏ | **xd-sct-vn** | |
| PCCC kho VLNCN, nhà máy tuyển, cơ sở chế biến | **pccc-sct-vn** | |
| Hóa chất trong tuyển - chế biến (axit, xút, thuốc tuyển) | **hc-sct-vn** | |
| Vận chuyển khoáng sản là HHNH (không phổ biến) hoặc vận chuyển VLNCN | **hnh-sct-vn** / sd-vlncn | |
| Soạn - render docx, thể thức NĐ 30/2020, QA | **vbhc-vn** | Chế độ B ưu tiên khi có văn bản mẫu |
| PDF văn bản đến | **vbhc-pdf-reader-vn** | GATE bắt buộc trước khi trích số/ngày |
| Ai ký, ai soạn, phòng nào chủ trì | **sct-laocai-org-vn** | Khoáng sản: PGĐ Thuân; PTP Nguyễn Hồng Vân; CN(Dũng)/CN(Nhung)/CN(Khôi) |
| Bài phát biểu lãnh đạo Sở về khoáng sản, công nghiệp khai khoáng | **bpb-sct-vn** | qlks cấp chất liệu nội dung, bpb cấp giọng văn - kết cấu |

## Quy tắc phối hợp khi một việc chạm nhiều plugin

1. Xác định "trục chính" của việc (VD: hồ sơ xin GP VLNCN cho mỏ đá → trục sd-vlncn; qlks bổ sung phần đối chiếu GP khai thác - công suất - thiết kế mỏ).
2. Căn cứ pháp lý lấy theo plugin trục chính; phần bổ trợ trích đúng phạm vi.
3. Không lặp nội dung giữa các plugin trong cùng một văn bản — mỗi căn cứ xuất hiện một lần.
4. Xung đột dữ liệu giữa plugin (số văn bản, ngày) → dừng, báo Bạn, không tự chọn.
