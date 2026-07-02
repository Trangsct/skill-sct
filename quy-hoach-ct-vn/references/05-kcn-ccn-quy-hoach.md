# 05 — Quy hoạch KCN và CCN tỉnh Lào Cai (lớp quy hoạch)

Reference này chỉ xử lý **lớp quy hoạch** của KCN/CCN: danh mục, vị trí xã, diện tích, quy mô theo Quy hoạch tỉnh (QĐ 525). Mọi nội dung **thành lập, mở rộng, điều chỉnh, chấm điểm chủ đầu tư hạ tầng, điều kiện khởi công, hiện trạng lấp đầy** → dùng skill **`kcn-ccn-vn`** (đầy đủ hơn, cập nhật hơn).

## 1. Nguồn dữ liệu quy hoạch KCN/CCN

| Văn bản | Nội dung | Skill chứa chi tiết |
|---|---|---|
| QĐ 525/QĐ-UBND 25/02/2026, **Phụ lục II** | Danh mục **KCN** quy hoạch (vị trí xã, diện tích, điều chỉnh) | `kcn-ccn-vn` ref 17 |
| QĐ 525/QĐ-UBND 25/02/2026, **Phụ lục III** | Danh mục **CCN** quy hoạch (vị trí xã, diện tích, điều chỉnh tiến độ) | `kcn-ccn-vn` ref 17 |
| QĐ 1382/QĐ-UBND 23/4/2026 | Danh mục dự án thu hút đầu tư (13 KCN + 35 CCN) | `kcn-ccn-vn` ref 16 |
| Báo cáo Sở Công Thương 18/6/2026 | Hiện trạng triển khai (23 CCN, 07 do DN làm CĐT...) | `kcn-ccn-vn` ref 15 |

## 2. Khung quy hoạch tổng thể (theo QĐ 525 — số liệu để đối chiếu)

- **KCN:** đến 2030 quy hoạch **20 KCN (~5.797 ha)**; tầm nhìn 2050: 22 KCN (~8.078 ha). Hiện trạng: 07 KCN đã thành lập.
- **CCN:** **54 CCN/~2.928 ha theo QĐ 525** (Phụ lục III: nhóm I 20 + II 14 + IV bổ sung 17 + V điều chỉnh tiến độ 03). Báo cáo 18/6/2026 nêu **56 CCN/3.052,81 ha** (= 54 + 02 cụm Gia Hội và Phong Hải đưa từ sau 2030 lên). Tầm nhìn 2050: 62 CCN (~3.779 ha).

> Khi viện dẫn **quy hoạch (QĐ 525)** dùng 54 CCN/2.928 ha; khi báo cáo **tình hình triển khai mới nhất** dùng 56 CCN/3.052,81 ha. Diễn đạt CCN đúng: "23 CCN đã phê duyệt QHCT, trong đó 13 đã có QĐ thành lập" — KHÔNG viết "23 CCN đã thành lập".

## 3. Địa danh dễ nhầm (đồng bộ với `kcn-ccn-vn`)

- KCN **Phú Xuân** (300 ha) và **Phú Xuân 1** (200 ha): đều tại **xã Gia Phú** (KHÔNG ghi "Xuân Hòa").
- CCN **Yên Hợp** (12 ha), **Yên Hợp 1** (63 ha), **Yên Hợp 2** (75 ha): đều tại **xã Xuân Ái**; là các dự án độc lập, KHÔNG dùng "giai đoạn I/II".
- CCN **Tân Nguyên** và **Mông Sơn**: tại **xã Bảo Ái**.
- CCN **Thống Nhất** (35 ha) và **Thống Nhất 1** (75 ha): đều tại **xã Gia Phú**.
- CCN **Phú Thịnh 5, Phú Thịnh 6**: tại **Phường Văn Phú** (theo Phụ lục III QĐ 525).

## 4. Liên hệ quy hoạch điện - khoáng sản với KCN/CCN

Khi rà soát quy hoạch tích hợp, lưu ý các điểm giao thoa giữa 04 ngành:
- KCN/CCN cần **phương án cấp điện** đồng bộ (đấu nối từ TBA 110kV gần nhất — xem ref 03). Một số TBA 110kV trong danh mục (ref 03) phục vụ trực tiếp KCN/CCN.
- Một số CCN gắn với **chế biến khoáng sản** (ví dụ khu vực Tằng Loỏng — apatit, hóa chất, luyện kim): khi quy hoạch phải đồng bộ với quy hoạch khoáng sản (ref 04) và yêu cầu môi trường.
- Nguồn **VLXDTT** (ref 04) phục vụ thi công hạ tầng KCN/CCN — cân đối cung cầu khi lập tiến độ.

→ Để làm bất kỳ việc gì sâu hơn về KCN/CCN (thẩm định hồ sơ, chấm điểm, điều kiện khởi công, mô hình 02 cấp, FDI làm CĐT, quy chế CCN QĐ 16/2026), chuyển sang **`kcn-ccn-vn`**.
