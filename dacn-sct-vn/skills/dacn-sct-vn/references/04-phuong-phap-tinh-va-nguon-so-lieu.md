# Reference 04 — Phương pháp tính và nguồn số liệu

> Điểm c khoản 2 mục III Công văn triển khai: cơ quan chủ trì chỉ tiêu phải **phối hợp Thống kê tỉnh thống nhất khái niệm, phạm vi, phương pháp tính, nguồn số liệu, kỳ báo cáo và thời điểm xác định**. Nội dung dưới đây là cách hiểu nghiệp vụ để làm việc với Thống kê tỉnh, **không thay thế hướng dẫn chính thức của cơ quan thống kê**.

---

## I. CHỈ TIÊU 3 — CHỈ SỐ SẢN XUẤT CÔNG NGHIỆP (IIP)

**Bản chất:** chỉ số so sánh khối lượng sản phẩm công nghiệp kỳ báo cáo với kỳ gốc, tính theo **hiện vật quy đổi**, không theo giá trị.

**Cơ quan công bố:** Thống kê tỉnh. Sở Công Thương **chủ trì theo dõi, báo cáo** nhưng **không tự công bố IIP**.

**Vai trò của Sở Công Thương:**
- Theo dõi sản lượng 42 nhóm sản phẩm chủ yếu (file theo dõi hằng tháng) làm cơ sở giải thích biến động IIP.
- Xác định sản phẩm nào kéo IIP lên/xuống.
- Đối chiếu với số Thống kê tỉnh; chênh lệch thì rà soát, giải trình, thống nhất **trước khi** báo cáo UBND tỉnh.

**Bốn ngành cấp 1 cấu thành IIP:**
| Ngành | Ghi trong file theo dõi |
|---|---|
| Khai khoáng | "CN Khai thác" |
| Chế biến, chế tạo | "CN Chế biến" |
| Sản xuất và phân phối điện, khí đốt, nước nóng | "CN Điện nước" (phần điện) |
| Cung cấp nước, quản lý và xử lý rác thải, nước thải | "CN Điện nước" (phần nước) |

⚠️ File theo dõi của Phòng gộp điện và nước thành một dòng "CN Điện nước". Khi cần tách theo chuẩn thống kê phải bóc riêng dòng "Điện phát" và "Nước máy".

---

## II. GIÁ TRỊ SẢN XUẤT CÔNG NGHIỆP (GTSX)

Hai loại giá cùng tồn tại trong file theo dõi, **không được lẫn**:

| Loại | Dùng để | Ghi chú |
|---|---|---|
| **Giá thực tế** (giá hiện hành) | Báo cáo quy mô, doanh thu, so kế hoạch năm | Chịu ảnh hưởng biến động giá |
| **Giá so sánh 2010** | Tính **tốc độ tăng trưởng**, so cùng kỳ | Loại trừ yếu tố giá — đây mới là số dùng cho chỉ tiêu tăng trưởng |

**Công thức trong file theo dõi:**
```
GTSX giá thực tế (sản phẩm i) = Sản lượng(i) × Đơn giá thực tế(i)
GTSX giá 2010    (sản phẩm i) = Sản lượng(i) × Đơn giá cố định 2010(i)
```
Đơn giá cố định 2010 nằm ở cột riêng trong sheet tháng và **không thay đổi giữa các tháng**. Nếu phát hiện đơn giá 2010 bị sửa giữa các sheet → lỗi dữ liệu, phải báo lại.

**Kiểm tra nhanh tính nhất quán:** tổng GTSX = CN Khai thác + CN Chế biến + CN Điện nước. Lệch quá 0,5% → có sản phẩm bị bỏ sót hoặc tính hai lần.

---

## III. CHỈ TIÊU 15 — ĐIỆN THƯƠNG PHẨM (dễ nhầm nhất)

| Đại lượng | Định nghĩa | Nguồn | Thuộc chỉ tiêu |
|---|---|---|---|
| **Điện phát** (sản lượng điện sản xuất) | Điện năng do các nhà máy trên địa bàn phát lên lưới | Chủ đầu tư nhà máy báo cáo Sở; file theo dõi thuỷ điện theo từng nhà máy | **Chỉ tiêu 3** (IIP ngành sản xuất điện) |
| **Điện thương phẩm** | Điện năng **bán đến hộ tiêu thụ cuối cùng** trên địa bàn | **Công ty Điện lực Lào Cai** | **Chỉ tiêu 15** |

**Không được** lấy tổng sản lượng thuỷ điện để báo cáo chỉ tiêu 15. Lào Cai là tỉnh **phát điện lớn hơn tiêu thụ**, hai con số lệch nhau rất xa và lệch cả về xu hướng (điện phát phụ thuộc thuỷ văn theo mùa; điện thương phẩm phụ thuộc phụ tải công nghiệp và dân sinh).

**Kỳ tính:** tăng trưởng điện thương phẩm bình quân — so sản lượng thương phẩm luỹ kế kỳ báo cáo với cùng kỳ năm trước.

**Đặc thù cần lưu ý khi phân tích:** phụ tải công nghiệp của tỉnh tập trung ở một số hộ tiêu thụ rất lớn (luyện đồng, phốt pho vàng, hoá chất, luyện kim, xi măng). Một nhà máy lớn dừng bảo dưỡng hoặc giảm công suất có thể làm hụt chỉ tiêu 15 của cả tỉnh → khi thấy điện thương phẩm giảm bất thường, kiểm tra ngay tình hình vận hành nhóm hộ tiêu thụ lớn trước khi kết luận.

---

## IV. CHỈ TIÊU 7, 8 — KIM NGẠCH XUẤT, NHẬP KHẨU

**Nguồn chính thức:** Chi cục Hải quan khu vực VII. Ban Quản lý Khu kinh tế tỉnh phối hợp (hoạt động qua cửa khẩu). Thống kê tỉnh đối chiếu.

**Phân nhóm hàng xuất khẩu** theo Phụ lục: nông-lâm-thuỷ sản / công nghiệp chế biến, chế tạo / nhiên liệu, khoáng sản.

**Lưu ý phương pháp:**
- Phân biệt **kim ngạch trên địa bàn** (doanh nghiệp đăng ký tại tỉnh) và **kim ngạch qua cửa khẩu** (bao gồm hàng của doanh nghiệp tỉnh khác). Chỉ tiêu 7, 8 dùng khái niệm nào phải thống nhất bằng văn bản với Thống kê tỉnh và Hải quan ngay từ kỳ đầu tiên.
- Mục tiêu 2026 rất cao (XK 93,5%, NK 108,3%) → biến động một vài lô hàng lớn ảnh hưởng mạnh. Báo cáo phải nêu cơ cấu, không chỉ nêu tổng.

---

## V. CHỈ TIÊU 4, 5 — CHẾ BIẾN, CHẾ TẠO

| Chỉ tiêu | Công thức bản chất | Cơ quan tính |
|---|---|---|
| 4 — Tỷ trọng CBCT trong GRDP | VA ngành chế biến, chế tạo ÷ GRDP × 100 | Thống kê tỉnh tính; Sở Công Thương chủ trì báo cáo |
| 5 — Giá trị tăng thêm CBCT bình quân đầu người | VA ngành chế biến, chế tạo ÷ dân số trung bình, quy đổi USD | nt |

Sở Công Thương **không tự tính VA**. Vai trò: theo dõi năng lực sản xuất của các nhà máy chế biến chế tạo, giải thích biến động, đề xuất giải pháp tăng quy mô ngành.

**Tỷ giá quy đổi USD** phải thống nhất với Thống kê tỉnh (thường dùng tỷ giá bình quân năm do cơ quan có thẩm quyền công bố) — ghi rõ tỷ giá đã dùng trong báo cáo.

---

## VI. CHỈ TIÊU 6 — TỔNG MỨC BÁN LẺ

Tổng mức bán lẻ hàng hoá **và** doanh thu dịch vụ tiêu dùng. Nguồn: điều tra của Thống kê tỉnh; Sở Công Thương theo dõi qua hệ thống chợ, siêu thị, trung tâm thương mại, cửa hàng xăng dầu, thương mại điện tử. Phối hợp Sở Văn hoá, Thể thao và Du lịch phần doanh thu dịch vụ lưu trú, ăn uống, lữ hành.

---

## VII. CHỈ TIÊU 32 — TIẾT KIỆM NĂNG LƯỢNG

Tỷ lệ = (Số doanh nghiệp công nghiệp áp dụng giải pháp sử dụng năng lượng tiết kiệm, hiệu quả ÷ Tổng số doanh nghiệp công nghiệp) × 100.

**Việc cần làm để có tử số:** xác định danh sách cơ sở sử dụng năng lượng trọng điểm; theo dõi việc thực hiện kiểm toán năng lượng, mô hình quản lý năng lượng, thay thế thiết bị hiệu suất cao. Phối hợp Ban Quản lý các KCN và Ban Quản lý Khu kinh tế tỉnh với các doanh nghiệp trong KCN.

**Việc cần làm để có mẫu số:** thống nhất với Thống kê tỉnh phạm vi "doanh nghiệp công nghiệp" (theo ngành cấp 1 B, C, D, E) và thời điểm chốt danh sách.

---

## VIII. BẢNG NGUỒN SỐ LIỆU THEO CHỈ TIÊU

| Chỉ tiêu | Nguồn số liệu chính | Nguồn đối chiếu | Tần suất |
|---|---|---|---|
| 3 (IIP) | Thống kê tỉnh | File theo dõi 42 sản phẩm của Phòng QLCN | Tháng |
| 4, 5 (CBCT) | Thống kê tỉnh | Báo cáo doanh nghiệp chế biến chế tạo | Quý/Năm |
| 6 (bán lẻ) | Thống kê tỉnh | Báo cáo hệ thống phân phối | Tháng |
| 7, 7a-c, 8 (XNK) | Chi cục Hải quan khu vực VII | BQL Khu kinh tế tỉnh; Thống kê tỉnh | Tháng |
| 15 (điện thương phẩm) | Công ty Điện lực Lào Cai | Thống kê tỉnh | Tháng |
| 32 (TKNL) | Sở Công Thương tự tổng hợp | BQL các KCN; BQL Khu kinh tế tỉnh | 6 tháng/Năm |
| 11 (vốn ĐTTXH) | Thống kê tỉnh | Báo cáo tiến độ dự án | Quý |
| 29, 30, 31 (môi trường) | Sở Nông nghiệp và Môi trường | Sở Công Thương cung cấp danh sách cơ sở | 6 tháng |

---

## IX. QUY TRÌNH XỬ LÝ CHÊNH LỆCH SỐ LIỆU

1. **Phát hiện** chênh lệch giữa số chuyên ngành của Sở và số Thống kê tỉnh.
2. **Xác định nguyên nhân** theo 5 khả năng: (a) khác phạm vi (trên địa bàn / qua cửa khẩu / theo đăng ký); (b) khác thời điểm chốt số; (c) khác giá (thực tế / so sánh 2010); (d) sót hoặc trùng đơn vị báo cáo; (e) lỗi nhập liệu.
3. **Lập biên bản/công văn đối chiếu** với Thống kê tỉnh, nêu rõ số của mỗi bên và nguyên nhân.
4. **Thống nhất số dùng chính thức** — Thống kê tỉnh chủ trì về chuyên môn thống kê.
5. **Chỉ sau khi thống nhất** mới đưa vào báo cáo UBND tỉnh. Nếu chưa kịp thống nhất, báo cáo phải ghi rõ hai số và tình trạng đang rà soát, **không tự chọn số có lợi**.
