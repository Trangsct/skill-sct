# Reference 07 — Kịch bản tăng trưởng, cảnh báo sớm và giải trình

## I. CĂN CỨ

- Điểm a khoản 2 mục III Công văn triển khai: cơ quan chủ trì chỉ tiêu **chủ động xây dựng và cập nhật phương án, kịch bản thực hiện phù hợp với kịch bản tăng trưởng của tỉnh**.
- Điểm b khoản 1 mục III: **Sở Tài chính** chủ trì xây dựng, cập nhật **kịch bản tăng trưởng của tỉnh** theo tháng, quý, cả năm → kịch bản ngành Công Thương phải **khớp và bổ trợ**, không được xây độc lập lệch pha.
- Mục 4 mục I: kịp thời nhận diện chỉ tiêu **có nguy cơ không hoàn thành**.

---

## II. BA KỊCH BẢN CHUẨN

Mỗi chỉ tiêu chủ trì dựng 3 kịch bản cho phần còn lại của năm:

| Kịch bản | Giả định | Dùng để |
|---|---|---|
| **Cao** | Các dự án động lực vận hành đúng tiến độ cam kết; thị trường thuận lợi; không phát sinh sự cố | Xác định dư địa vượt mục tiêu |
| **Cơ sở** | Tiến độ dự án theo xu hướng thực tế 3 kỳ gần nhất; thị trường ổn định | **Là kịch bản báo cáo chính thức** |
| **Thấp** | Có ít nhất một dự án lớn chậm/dừng; thị trường bất lợi | Xác định rủi ro, chuẩn bị phương án khắc phục |

Mỗi kịch bản phải nêu **3 giả định định lượng** cụ thể, không mô tả định tính chung chung.

---

## III. PHƯƠNG PHÁP DỰNG KỊCH BẢN CHO CHỈ TIÊU SẢN LƯỢNG

**Bước 1 — Xác định phần đã thực hiện.**
```
Luỹ kế đến kỳ báo cáo (LK)
Tỷ lệ hoàn thành hiện tại = LK / Kế hoạch năm × 100%
```

**Bước 2 — Xác định tiến độ chuẩn.**
```
Tiến độ chuẩn tại tháng n = n / 12 × 100%
Độ lệch = Tỷ lệ hoàn thành − Tiến độ chuẩn
```

**Bước 3 — Ngoại suy phần còn lại.**
```
Bình quân tháng thực tế = LK / n
Ước cả năm (kịch bản cơ sở) = LK + Bình quân tháng × (12 − n)
Ước cả năm (kịch bản cao)   = LK + Bình quân 3 tháng gần nhất × (12 − n) × 1,05
Ước cả năm (kịch bản thấp)  = LK + Bình quân 3 tháng gần nhất × (12 − n) × 0,90
```

**Bước 4 — Điều chỉnh theo dự án động lực.** Cộng thêm sản lượng dự kiến của dự án mới vận hành trong năm; trừ đi sản lượng của dự án đã dừng. Đây là bước **bắt buộc** — ngoại suy thuần tuý không phản ánh được dự án mới.

**Bước 5 — Tính tốc độ tăng.**
```
Tốc độ tăng (%) = (Ước cả năm / Thực hiện năm trước − 1) × 100
```
So với **Mục tiêu 2026** tại reference `02` → kết luận đạt / không đạt.

⚠️ **Lưu ý về tính mùa vụ.** Ngoại suy tuyến tính sai nặng với hai nhóm:
- **Điện phát**: phụ thuộc thuỷ văn, mùa mưa (tháng 6-10) sản lượng cao gấp nhiều lần mùa khô. Phải ngoại suy theo **cùng kỳ năm trước**, không theo bình quân tháng.
- **Nông sản chế biến** (chè, tinh bột sắn, gỗ): theo vụ thu hoạch.

Với hai nhóm này dùng công thức:
```
Ước cả năm = Thực hiện cùng kỳ năm trước cả năm × (LK năm nay / LK cùng kỳ năm trước)
```

---

## IV. NGƯỠNG CẢNH BÁO

Áp dụng cho mọi chỉ tiêu và mọi sản phẩm chủ yếu:

| Mức | Điều kiện | Hành động bắt buộc |
|---|---|---|
| 🟢 **An toàn** | Độ lệch ≥ −3 điểm % so tiến độ chuẩn | Theo dõi bình thường |
| 🟡 **Cần chú ý** | Độ lệch từ −3 đến −8 điểm % | Nêu tên trong báo cáo kỳ; xác định nguyên nhân |
| 🟠 **Nguy cơ** | Độ lệch từ −8 đến −15 điểm % | Phân tích nguyên nhân + đề xuất giải pháp cụ thể trong báo cáo |
| 🔴 **Báo động** | Độ lệch < −15 điểm %, hoặc dự báo cả năm không đạt mục tiêu | **Báo cáo đột xuất UBND tỉnh qua Sở Tài chính**; người đứng đầu trực tiếp chỉ đạo (mục III.6) |

Script `phan_tich_thang.py` tự động gắn nhãn 4 mức này.

---

## V. MẪU GIẢI TRÌNH CHỈ TIÊU CÓ NGUY CƠ KHÔNG HOÀN THÀNH

Cấu trúc 5 phần, dùng cho từng chỉ tiêu:

```
1. Chỉ tiêu và mức độ hụt
   - Mục tiêu năm 2026: ...
   - Thực hiện đến ngày ...: ... (đạt ...% mục tiêu, chậm ... điểm % so tiến độ)
   - Dự báo cả năm (kịch bản cơ sở): ...

2. Nguyên nhân
   a) Nguyên nhân khách quan: (thị trường, thuỷ văn, giá nguyên liệu, chính sách...)
   b) Nguyên nhân chủ quan: (tiến độ dự án, năng lực doanh nghiệp, phối hợp...)
   → Mỗi nguyên nhân phải quy được về dự án/doanh nghiệp cụ thể và lượng hoá được mức ảnh hưởng

3. Giải pháp thuộc thẩm quyền Sở Công Thương đã và đang triển khai

4. Nội dung vượt thẩm quyền, đề nghị UBND tỉnh chỉ đạo
   - Đề nghị ai làm gì, hoàn thành trước ngày nào

5. Cam kết mức phấn đấu
```

**Nguyên tắc viết:** không đổ toàn bộ cho nguyên nhân khách quan. Phải có ít nhất một nguyên nhân chủ quan kèm giải pháp khắc phục — đây là yêu cầu của mục III.6 về trách nhiệm người đứng đầu.

---

## VI. LIÊN KẾT KỊCH BẢN NGÀNH VỚI KỊCH BẢN TỈNH

Trước khi gửi kịch bản ngành:
1. Đối chiếu giả định tăng trưởng khu vực công nghiệp và xây dựng (chỉ tiêu 1.2) với kịch bản của Sở Tài chính.
2. Nếu kịch bản ngành cho kết quả **thấp hơn** kịch bản tỉnh → phải nêu rõ và giải trình chênh lệch, không im lặng.
3. Nếu **cao hơn** → nêu rõ điều kiện cần để đạt (dự án nào phải vận hành đúng hạn).
4. Ghi rõ ngày chốt số liệu đầu vào của kịch bản.
