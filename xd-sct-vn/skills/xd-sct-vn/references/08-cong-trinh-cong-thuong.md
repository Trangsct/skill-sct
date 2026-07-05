# 08. CHUYÊN SÂU — công trình xây dựng ngành Công Thương

Đây là phần cốt lõi phân biệt plugin này với QLNN xây dựng chung. Với mỗi loại công trình: SCT có vai trò gì, chuyên viên nào, cấp công trình thường gặp, plugin liên kết.

## Bảng tổng hợp công trình ngành Công Thương do SCT làm CQCM về xây dựng

| Loại công trình | Vai trò SCT (CQCM về XD) | Chuyên viên QLCN | Plugin liên kết | Ghi chú cấp/đặc thù |
|---|---|---|---|---|
| **Kho VLNCN** (cố định, tạm) | Thẩm định thiết kế (nếu thuộc diện), KTCTNT, xác nhận đáp ứng QCVN | CN(Dũng) chủ trì công trình + CN(Linh) VLNCN | **kho-vlncn-sct-vn** (chi tiết QCVN 01:2019/BCT, quy trình) | Kho ≤10 tấn thường cấp II; kho tạm áp Đ72 (ref 06) |
| **Nhà máy, kho hóa chất** | Thẩm định BCNCKT/thiết kế, KTCTNT | CN(Dũng) + phối hợp CN(Loan) hóa chất | (hóa chất: `sct-laocai-org-vn`) | Đối chiếu an toàn hóa chất, khoảng cách; PCCC → `pccc-sct-vn` |
| **Công trình khai thác - chế biến khoáng sản** (trừ VLXD thông thường, xi măng) | Thẩm định BCNCTKT/BCNCKT/BCKTKT + các bước thiết kế sau TK cơ sở; KTCTNT; kiểm tra ATKT | CN(Dũng) thẩm định + CN(Nhung) khoáng sản | `quy-hoach-ct-vn` (quy hoạch khoáng sản) | Loại trừ rõ VLXD thông thường + xi măng (→ Sở Xây dựng) |
| **Hạ tầng kỹ thuật CCN** | Thẩm định (phần thuộc thẩm quyền), phối hợp quản lý | CN(Dũng) + CN(Trung) KCN/CCN | **kcn-ccn-vn** | CCN ngoài KCN/KKT; hạ tầng dùng chung |
| **Cơ khí, luyện kim, điện tử, công nghiệp hỗ trợ** | Thẩm định BCNCKT/BCKTKT, thiết kế, KTCTNT | CN(Dũng) + CN(Cường) | — | Công trình công nghiệp chế tạo |
| **Công nghiệp chế biến, thực phẩm, tiêu dùng** | Thẩm định, KTCTNT | CN(Dũng) + CN(T.Dương) | — | ATTP → nghiệp vụ khác, không phải xây dựng |
| **Cửa hàng xăng dầu, cửa hàng gas, kho LPG** | Thẩm định (phần công trình công nghiệp), KTCTNT | CN(Dũng) | `pccc-sct-vn` (PCCC cửa hàng xăng dầu/gas) | Đối chiếu QCVN xăng dầu; PCCC bắt buộc |

## Nguyên tắc "3 câu hỏi" áp cho công trình cụ thể (nhắc lại từ SKILL mục III)

1. **Công trình công nghiệp thuộc ngành CT?** → nếu điện lực thì chuyển QLNL; nếu VLXD/xi măng thì chuyển Sở Xây dựng; nếu trong KCN/KKT thì chuyển BQL.
2. **Nghiệp vụ gì?** thẩm định thiết kế / KTCTNT / sự cố — mỗi cái căn cứ khác nhau (ref 03, 04, 07).
3. **Cấp nào?** dự án do UBND tỉnh quyết định đầu tư → SCT cấp tỉnh; do UBND xã quyết định đầu tư chỉ lập BCKTKT → cấp xã.

## Điểm nghiệp vụ đặc thù ngành CT

### A. Kho VLNCN — giao thoa 3 plugin
- **Xây dựng công trình kho** (thiết kế, thi công, nghiệm thu): plugin `kho-vlncn-sct-vn` là chính; plugin xây dựng này cung cấp khung chung (điều kiện khởi công, KTCTNT, công trình tạm).
- **GP sử dụng VLNCN, PANM**: plugin `sd-vlncn-sct-vn`.
- **Huấn luyện KTAT**: plugin `hl-vlncn-sct-vn`.
- Khi một hồ sơ kho VLNCN cần cả khung xây dựng lẫn QCVN chuyên ngành → dùng đồng thời plugin này + `kho-vlncn-sct-vn`.

### B. Công trình khoáng sản — hai lớp pháp luật
Vừa chịu pháp luật xây dựng (Luật 135/2025, NĐ 207/2026, NĐ 217/2026) vừa pháp luật khoáng sản. SCT thẩm định "các bước thiết kế xây dựng triển khai sau thiết kế cơ sở của dự án khai thác - chế biến khoáng sản" (`sct-laocai-org-vn`). Đối chiếu giấy phép khai thác khoáng sản (Bộ NN&MT hoặc UBND tỉnh cấp) trước khi thẩm định phần xây dựng.

### C. Ranh giới với PCCC
Theo Điều 93 khoản 2 Luật 135/2025 (sửa Điều 17 Luật PCCC 55/2024): **CQCM về xây dựng thẩm định các nội dung a,b,c,d,đ khoản 1 Điều 16** đối với dự án phải thẩm định thiết kế về PCCC. Phần thẩm quyền Công an vẫn do Công an thực hiện. Chi tiết phân định PCCC → plugin `pccc-sct-vn`. SCT (với công trình công nghiệp ngành CT) là CQCM về xây dựng trong quan hệ này.

### D. Kiểm tra PCCC hằng năm gắn với KTCTNT
Điều 17 khoản 1 QĐ 11/2026: CQCM về xây dựng cấp tỉnh, khi kiểm tra công trình chuyên ngành, **đồng thời tổ chức kiểm tra công tác PCCC hằng năm** theo điểm b khoản 2 Điều 13 NĐ 105/2025. Đây là điểm mới cần lưu ý khi lập kế hoạch kiểm tra công trình công nghiệp — gộp nội dung PCCC.
