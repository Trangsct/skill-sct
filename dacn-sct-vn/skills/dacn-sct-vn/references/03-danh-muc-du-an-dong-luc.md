# Reference 03 — Khung quản lý danh mục dự án động lực tăng trưởng

> **Nguyên tắc gốc:** plugin này lưu **khung phân loại và phương pháp**, KHÔNG lưu dữ liệu hiện trạng dự án (số liệu động, dễ lỗi thời). Dữ liệu thật nạp vào `du-lieu/danh-muc-du-an.json` và do Bạn cập nhật.

---

## I. PHẠM VI "DỰ ÁN CÔNG NGHIỆP" CẦN THEO DÕI

Toàn bộ dự án có tác động tới ít nhất một chỉ tiêu Sở Công Thương chủ trì, gồm 07 nhóm:

| Mã nhóm | Nhóm dự án | Chỉ tiêu tác động chính | Plugin chuyên ngành |
|---|---|---|---|
| **HT-KCN** | Hạ tầng khu công nghiệp | 3, 4, 29, 32 | `kccn-sct-vn` |
| **HT-CCN** | Hạ tầng cụm công nghiệp | 3, 4, 29, 32 | `kccn-sct-vn` |
| **KS** | Khai thác, chế biến khoáng sản | 3, 7c | `qlks-sct-vn`, `tkm-sct-vn` |
| **LK-HC** | Luyện kim, hoá chất, phân bón | 3, 4, 7b, 8, 32 | `hc-sct-vn`, `qlks-sct-vn` |
| **CBCT** | Chế biến, chế tạo khác (gỗ, giấy, dệt may, thực phẩm, VLXD, cơ khí) | 3, 4, 5, 7a, 7b | — |
| **NL** | Nguồn điện, lưới điện, năng lượng | 3, 15, 32 | `quy-hoach-ct-vn` |
| **TM** | Hạ tầng thương mại, logistics, cửa khẩu | 6, 7, 8 | — |

---

## II. PHÂN LOẠI THEO TRẠNG THÁI VÒNG ĐỜI

Mỗi dự án có đúng **một** trạng thái tại mỗi kỳ báo cáo:

| Mã | Trạng thái | Đặc điểm | Ảnh hưởng tới tăng trưởng |
|---|---|---|---|
| `TN` | Tiềm năng — trong danh mục thu hút đầu tư, chưa có nhà đầu tư | QĐ 1382/QĐ-UBND | Không tính vào kỳ báo cáo |
| `DX` | Đã có nhà đầu tư đề xuất, đang thẩm định | Có hồ sơ tại Sở/BQL | Không tính; theo dõi tiến độ thủ tục |
| `CT` | Đã có chủ trương đầu tư / quyết định thành lập | Đủ pháp lý khởi động | Đóng góp vào **vốn đầu tư** (chỉ tiêu 11) |
| `GPMB` | Đang giải phóng mặt bằng | Nút thắt phổ biến nhất | Đóng góp vốn đầu tư |
| `XD` | Đang xây dựng | Có khối lượng hoàn thành | Đóng góp vốn đầu tư, chỉ tiêu 1.2 (xây dựng) |
| `HĐ` | Đang hoạt động sản xuất, kinh doanh | **Có sản lượng, doanh thu** | Đóng góp IIP, GTSX, kim ngạch, điện thương phẩm |
| `MR` | Đang mở rộng, nâng công suất | Vừa có sản lượng vừa có vốn | Đóng góp cả hai |
| `TĐ` | Tạm dừng / dừng hoạt động / không triển khai | **Kéo tụt chỉ tiêu** | Phải nêu trong mục điểm nghẽn |

**Quy tắc bắt buộc:** trong báo cáo, chỉ dự án trạng thái `HĐ` và `MR` mới được tính vào chỉ tiêu sản lượng/IIP. Không cộng dồn dự án `XD` vào sản lượng.

---

## III. TIÊU CHÍ XẾP HẠNG "DỰ ÁN ĐỘNG LỰC"

Chấm 100 điểm, dùng để xếp thứ tự ưu tiên theo dõi và đôn đốc. Dự án ≥ 60 điểm đưa vào danh mục trọng điểm báo cáo UBND tỉnh.

| Tiêu chí | Điểm tối đa | Cách chấm |
|---|---|---|
| **1. Quy mô đóng góp giá trị sản xuất** (tỷ đồng/năm khi vận hành ổn định) | 30 | ≥1.000 tỷ: 30 đ · 500-1.000: 22 đ · 200-500: 15 đ · 50-200: 8 đ · <50: 3 đ |
| **2. Số chỉ tiêu NQ 169 tác động trực tiếp** | 15 | ≥4 chỉ tiêu: 15 đ · 3: 11 đ · 2: 7 đ · 1: 4 đ |
| **3. Tính sẵn sàng phát sinh kết quả trong năm báo cáo** | 20 | Đã hoạt động: 20 đ · Vận hành trong năm: 16 đ · Đang XD, vận hành năm sau: 10 đ · Chưa khởi công: 4 đ |
| **4. Thuộc ngành chế biến, chế tạo** (chỉ tiêu 4, 5 khó nhất) | 10 | Chế biến chế tạo: 10 đ · Khai khoáng/điện: 6 đ · Khác: 3 đ |
| **5. Đóng góp xuất khẩu / thay thế nhập khẩu** | 10 | Xuất khẩu chính: 10 đ · Có xuất khẩu: 6 đ · Không: 0 đ |
| **6. Sử dụng lao động địa phương** (người) | 5 | ≥500: 5 đ · 200-500: 3 đ · <200: 1 đ |
| **7. Mức độ rủi ro tiến độ** (điểm nghẽn đang tồn tại) | 10 | Không vướng: 10 đ · 1 nhóm vướng: 6 đ · 2-3 nhóm: 3 đ · ≥4 nhóm hoặc đã dừng: 0 đ |

> Thang điểm này là **công cụ nội bộ tham mưu**, không phải thang chấm điểm pháp lý. Không nhầm với thang 100 điểm lựa chọn chủ đầu tư hạ tầng CCN tại Điều 13 NĐ 32/2024 (thuộc `kccn-sct-vn`).

---

## IV. TRƯỜNG DỮ LIỆU BẮT BUỘC CỦA MỘT DỰ ÁN

Xem lược đồ máy đọc tại `du-lieu/schema-du-an.json`. Tóm tắt:

| Nhóm trường | Trường |
|---|---|
| **Định danh** | mã dự án, tên đầy đủ, chủ đầu tư, mã số thuế |
| **Vị trí** | xã/phường, KCN/CCN (nếu có), toạ độ |
| **Phân loại** | nhóm (HT-KCN…TM), trạng thái (TN…TĐ), ngành cấp 2 |
| **Pháp lý** | số/ngày quyết định chủ trương đầu tư hoặc GCN đăng ký đầu tư, cơ quan cấp |
| **Quy mô** | tổng mức đầu tư (tỷ đồng), diện tích (ha), công suất thiết kế + đơn vị |
| **Tiến độ** | tiến độ cam kết, tiến độ thực tế, % hoàn thành, ngày dự kiến vận hành |
| **Đóng góp** | chỉ tiêu NQ 169 tác động, sản lượng kỳ, doanh thu kỳ, kim ngạch XK kỳ, lao động |
| **Điểm nghẽn** | danh sách mã nhóm điểm nghẽn (xem reference `06`), mô tả, cơ quan giải quyết, hạn xử lý |
| **Nguồn** | tên file/kỳ báo cáo đã lấy số liệu, ngày cập nhật |

**Trường `nguon` là bắt buộc.** Bản ghi thiếu `nguon` không được đưa vào báo cáo phát hành.

---

## V. QUY TẮC GẮN DỰ ÁN ↔ CHỈ TIÊU

| Loại dự án | Chỉ tiêu được phép quy kết |
|---|---|
| Nhà máy chế biến, chế tạo đang hoạt động | 3 (IIP), 4, 5; nếu xuất khẩu → 7, 7b |
| Mỏ, nhà máy tuyển khoáng sản | 3; nếu xuất khẩu → 7, 7c |
| Nhà máy luyện kim, hoá chất | 3, 4; nhập nguyên liệu → 8; xuất sản phẩm → 7, 7b |
| Nhà máy thuỷ điện / nguồn điện | 3 (ngành sản xuất, phân phối điện); **không** tự động quy vào chỉ tiêu 15 |
| Lưới điện, trạm biến áp | 15 (gián tiếp, qua năng lực cấp điện) |
| Hạ tầng KCN/CCN | 11 (vốn đầu tư); sau khi có dự án thứ cấp hoạt động → 3, 4; XLNT → 29 |
| Trung tâm thương mại, chợ, siêu thị, logistics | 6; nếu gắn cửa khẩu → 7, 8 |
| Dự án cải tạo, thay thiết bị tiết kiệm năng lượng | 32 |

⚠️ **Sai lầm thường gặp cần tránh:**
- Quy sản lượng **điện phát** vào chỉ tiêu 15 (điện thương phẩm). Hai đại lượng khác nhau — xem reference `04` mục III.
- Cộng vốn đầu tư đăng ký vào chỉ tiêu 11 (vốn đầu tư **thực hiện**).
- Tính dự án đã dừng hoạt động vào sản lượng vì còn tên trong danh mục.

---

## VI. NGUỒN HÌNH THÀNH DANH MỤC

1. **QĐ 1382/QĐ-UBND ngày 23/4/2026** — Danh mục dự án thu hút đầu tư 2026-2030 (431 danh mục, 5 phụ lục; Phụ lục 01 có 13 KCN + 35 CCN) → nguồn dự án trạng thái `TN`.
2. **QĐ 525/QĐ-UBND ngày 25/02/2026** — Quy hoạch tỉnh (Phụ lục II, III: khoáng sản, điện) → đối chiếu tính hợp quy hoạch (`quy-hoach-ct-vn`).
3. **Báo cáo của Ban Quản lý các Khu công nghiệp tỉnh** và **Ban Quản lý Khu kinh tế tỉnh** → dự án thứ cấp trong KCN.
4. **File theo dõi sản xuất công nghiệp hằng tháng của Phòng QLCN** → dự án đang hoạt động có sản lượng (42 nhóm sản phẩm chủ yếu).
5. **Báo cáo của UBND cấp xã** → dự án ngoài KCN/CCN trên địa bàn.
6. **Hồ sơ cấp phép chuyên ngành của Sở** (VLNCN, hoá chất, HHNH, khoáng sản) → xác nhận dự án còn hoạt động thực tế.

Định kỳ **rà soát chéo 6 nguồn này mỗi quý** để tránh sót và trùng.
