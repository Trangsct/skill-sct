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
- **CCN sau năm 2030:** 74 CCN/~3.849,31 ha theo Bảng 25 Báo cáo tổng hợp (xem mục 5 — danh sách đầy đủ, gồm Phong Hải, Gia Hội).
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

## 5. Danh mục CCN thời kỳ sau năm 2030 và cơ chế "đầu tư sớm hơn" (cập nhật 29/10/2026)

Nguồn: Báo cáo tổng hợp Quy hoạch tỉnh (bản hoàn thiện 09/10/2026 theo QĐ 525), mục 5.3 và **Bảng 25** (trang 296-299);
Phụ lục III QĐ 525 (bản ký, trang 33-36 tệp PDF). Toàn văn: `van-ban-goc/2026.02.25-525.QD.UBND-Bao-cao-tong-hop-*.txt`
(dòng 13286-13520) và `van-ban-goc/2026.02.25-525.QD.UBND-Phe-duyet-dieu-chinh-*.txt` (OCR).

- **Phụ lục III QĐ 525 chỉ liệt kê 54 CCN đến năm 2030 (2.927,81 ha)**, chia mục I (giữ nguyên 20), II (điều chỉnh tăng,
  giảm 14), III (rút 13 — không tính vào 54), IV (bổ sung 17), V (đưa từ sau 2030 lên: Phú Thịnh 5, Phú Thịnh 6, Châu Quế
  Thượng), VI (Púng Luông đưa sang sau 2030). **Ghi chú cuối Phụ lục III:** "Trường hợp huy động được nguồn lực đầu tư phục
  vụ phát triển kinh tế - xã hội thì báo cáo cấp có thẩm quyền xem xét chấp thuận cho đầu tư sớm hơn đối với một số cụm
  công nghiệp dự kiến đầu tư sau 2030."
- **Thời kỳ sau năm 2030: 74 CCN, khoảng 3.849,31 ha** (Bảng 25 mục B, chỉ có trong Báo cáo tổng hợp, không có bảng riêng
  trong Phụ lục III). Gồm:
  - B.I — 18 CCN giữ theo QĐ 1086/QĐ-TTg, QĐ 316/QĐ-TTg (716 ha): Nậm Búng (xã Gia Hội, 63); Púng Luông (10); Cam Đường 3
    (phường Cam Đường, 38; QH cũ là CCN Cam Đường); Thái Niên (xã Bảo Thắng, 75); **Phong Hải (xã Phong Hải, 75)**; Phú Nhuận
    (xã Tằng Loỏng, 75); Phong Niên (xã Xuân Quang, 75); Khánh Yên Trung (22); Liêm Phú (23,5); Tân Thượng (xã Bảo Hà, 20);
    Minh Lương (20,1); Dương Quỳ (20); Chiềng Ken (28); Nậm Tha (xã Chiềng Ken, 20,4); Trịnh Tường (20); Bảo Nhai (35);
    Quang Kim 2 (xã Bát Xát, 60, tăng 25); Bản Vược (xã Bát Xát, 36, tăng 6).
  - B.II — 12 CCN đã có trong QH 1086, 316 đề xuất rút: Thẩm Dương, Cam Cọn, Khánh Yên Hạ, Dần Thàng, Khánh Yên Thượng (xã Văn
    Bàn), Lùng Vai, Mường Khương, Bản Xèo, Lùng Phình, Cán Cấu, Sín Chéng, Thanh Kim.
  - B.III — 02 CCN bổ sung mới sau 2030 (125 ha): Mường Lai (xã Mường Lai, 75); **Gia Hội (xã Gia Hội, 50)**.
- Ghi chú Bảng 25 nêu đích danh các cụm "dự kiến đầu tư sau năm 2030, như: Nậm Búng, Cam Đường 3, Thái Niên, Phong Hải, Phong
  Niên, Quang Kim 2, Mường Lai,…" có thể báo cáo cấp có thẩm quyền chấp thuận đầu tư sớm hơn khi huy động được nguồn lực.

**Áp dụng khi phân loại đề xuất phát sinh (Văn bản 10199/UBND-TH ngày 07/10/2026 của UBND tỉnh, mục 2.2):** đề xuất đưa
Phong Hải (75 ha) và Gia Hội (50 ha) lên giai đoạn 2026-2030 là nhóm "đã được định hướng nhưng đề nghị thay đổi tiến độ" —
làm tăng số lượng, diện tích CCN đến 2030 nên phải điều chỉnh Quy hoạch tỉnh (trình tự Luật Quy hoạch 2025; Điều 6, 7
NĐ 32/2024/NĐ-CP). Đề xuất Yên Hợp tăng 07 ha vượt mức 05 ha được quyết ngay tại QĐ mở rộng (khoản 4 Điều 10 NĐ 32/2024,
sửa đổi tại khoản 5 Điều 1 NĐ 303/2026/NĐ-CP) — xem `kccn-sct-vn` ref 55.
