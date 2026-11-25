# 15 — Ranh giới số hóa 09 sơ đồ quy hoạch khoáng sản nhóm I tỉnh Lào Cai (123 khu vực, 1.129 điểm góc)

> **Nguồn:** file KMZ Bạn gửi ngày 25/11/2026 — `du-lieu/00_TongHop_RanhGioi_QuyHoach_LaoCai.kmz` (file gốc, mở được bằng Google Earth). Ranh giới số hóa từ 09 sơ đồ quy hoạch thăm dò, khai thác khoáng sản nhóm I: bản vẽ 3.3, 3.4 (chì kẽm), 4.6 (sắt), 8.4 (đồng - molipden), 8.5 (đồng), 9.3 (vàng), 11.2, 11.3 (đất hiếm), 12 (apatit). File không ghi số quyết định; số Phụ lục VI khớp **dự thảo điều chỉnh QĐ 866 (3/2026, chưa ký)** — `sources/qd866-dieuchinh-2026-phuluc.txt` (xem kết quả đối chiếu mục C).
>
> ⚠️ **Tính pháp lý:** tọa độ chỉ để tham khảo, định vị, rà chồng lấn. Đưa tọa độ vào văn bản chính thức: lấy theo Phụ lục VI của văn bản **đã ký** (QĐ 866/QĐ-TTg ngày 18/7/2023; riêng Tả Phời theo QĐ 2581/QĐ-TTg ngày 24/11/2025 — ref 07 mục A.2), không lấy từ bảng này.

## A. Các tệp

| Tệp | Nội dung |
|---|---|
| `du-lieu/00_TongHop_RanhGioi_QuyHoach_LaoCai.kmz` | **File gốc** (1 `doc.kml`): thư mục theo bản vẽ → loại khu vực → khu vực (đa giác + nhãn); bảng tọa độ trong phần mô tả từng khu vực |
| `du-lieu/toa-do-ranh-gioi-quy-hoach-khoang-san-nhom-I-lao-cai.csv` | 1.129 dòng (mỗi dòng 1 điểm góc): bản vẽ, sơ đồ, Phụ lục VI, loại khu vực, STT, tên, ghi chú tên, diện tích trên sơ đồ, điểm, X, Y (VN-2000), vĩ độ, kinh độ (WGS84), kết quả đối chiếu Phụ lục VI dự thảo |
| `du-lieu/2026.11.25. Bảng tọa độ ranh giới các khu vực quy hoạch khoáng sản nhóm I tỉnh Lào Cai.docx` | Bảng tọa độ xuất Word (36 trang): Phần I tổng hợp; Phần II 09 bảng chi tiết theo bản vẽ |
| `scripts/tra_toa_do_quy_hoach.py` | Tra theo tên (`--ten`), theo điểm (`--diem X Y` hoặc `--wgs84`: nằm trong khu vực nào, khu vực nào trong bán kính 500 m), theo bản vẽ (`--ban-ve 12`), tổng hợp (`--tong-hop`); không cần thư viện ngoài |

## B. Hệ tọa độ và kết quả kiểm tra

- **VN-2000, múi chiếu 6°, kinh tuyến trục 105°, k = 0,9996** (cùng hệ với Phụ lục VI QĐ 866) + WGS84 độ thập phân.
- ⚠️ **Không so trực tiếp với tọa độ giấy phép khai thác, đề án thăm dò của tỉnh** — các hồ sơ này thường dùng VN-2000 **kinh tuyến trục 104°45', múi 3°**; phải chuyển hệ trước khi so (chênh lệch hàng trăm mét đến hàng km).
- Tọa độ VN-2000 và WGS84 trong file khớp nhau (lệch tối đa 1,4 m, do làm tròn); đa giác trên bản đồ khớp bảng tọa độ; diện tích tính lại từ tọa độ khớp diện tích ghi trong file.
- **Chồng lấn:** nhiều khu vực chồng lấn nhau trên sơ đồ (khu vực đã cấp phép khai thác nằm trong khu vực thăm dò): Sinh Quyền (cu) với Sin Quyền (Cu) phần mở rộng ~296 ha; Tả Phời (Cu) với các khu không ghi tên gần Tả Phời (Cu) ~25–322 ha; Làng Mỵ với 08 khu đã cấp phép khai thác (bản vẽ 4.6); Đồng Vi Kẽm Cốc Mỳ (Cu) với "Khu vực đã cấp phép khai thác" ~149 ha; Làng Phúng 1, Tam Đỉnh 1, 2 với Tam Đỉnh - Làng Phúng; KT10 - Cam Đường 1 với khu gần Đông Bắc KT 10 ~50 ha... → **không cộng gộp diện tích** các khu vực.
- **Tên chưa chắc chắn:** (1) loại khu vực bản vẽ 3.3 — sơ đồ gốc không có chú giải (màu xanh lam, ghi "Khu vực quy hoạch thăm dò"); (2) 03 tên file ghi "lấy theo nhãn gần nhất, cần đối chiếu": Làng Thảo (1) (bản vẽ 4.6), Tam Đỉnh - Làng Phúng (1), (2) (bản vẽ 12). Các khu "Không ghi tên trên sơ đồ (gần …)" là tên tạm theo nhãn lân cận.

## C. Đối chiếu với Phụ lục VI dự thảo điều chỉnh QĐ 866 (3/2026)

So từng điểm góc với tọa độ trong `sources/qd866-dieuchinh-2026-phuluc.txt` (khoảng cách tới điểm gần nhất, lấy trung vị theo khu vực):

- **113/123 khu vực khớp** (trung vị dưới 10 m; đối chiếu cả hai cách ghi số "2495034" và "2.495.034" trong phụ lục) → phần lớn tọa độ trong file trùng tọa độ Phụ lục VI dự thảo.
- **10 khu vực lệch (9 "không khớp", 1 "lệch nhỏ"), phải đối chiếu Phụ lục VI trước khi dùng** (cột `doi_chieu_phu_luc_VI_du_thao`):
  - Đất hiếm (bản vẽ 11.2): **Mỏ Mường Hum** — cùng 4 điểm, cùng diện tích ~2.985 ha nhưng lệch ~3,4 km so với Phụ lục VI.14; **Mỏ Bến Đền (1), (2), (3)** — file chia 3 khối (212,5 + 202,2 + 285,7 ha), Phụ lục VI.14 là 1 khối 12 điểm, 2.160 ha.
  - Đồng (bản vẽ 8.4): **Sinh Quyền (cu)** — lệch ~0,6 km.
  - Apatit (bản vẽ 12): **KT 9/37** (~0,8 km), **KT 7 KT 5 (khu 2) (2)** (~0,1 km), **KT 28** (~0,1 km), **KT 17** (~0,1 km); **KT 7 KT 5 (khu 2) (1)** lệch nhỏ (~17 m).
- Ví dụ khớp đã kiểm tra tay: KT 26 (Phụ lục VI.16, mục "Các dự án cấp mới", 10,5 ha, 8 điểm) và KT 27 (33,6 ha) trùng điểm góc tới vài mét.

## D. Cách dùng

```bash
python3 scripts/tra_toa_do_quy_hoach.py --diem 2476700 396900      # một điểm (VN-2000 KTT 105, múi 6) có nằm trong khu vực quy hoạch nào không
python3 scripts/tra_toa_do_quy_hoach.py --ten "Làng Cáng"           # tọa độ khu vực
python3 scripts/tra_toa_do_quy_hoach.py --tong-hop
```

Dùng khi: rà một dự án, CCN, KCN, điểm mỏ nhóm III–IV có chồng lấn khu vực quy hoạch khoáng sản nhóm I không (kết hợp `kccn-sct-vn`, `qlks-sct-vn` ref 12); định vị nhanh một mỏ trên Google Earth; chuẩn bị ý kiến khi Bộ lấy ý kiến điều chỉnh quy hoạch khoáng sản. Điểm nằm sát ranh (dưới ~100 m) hoặc khu vực "không khớp" → mở Phụ lục VI để kết luận.

## E. Tổng hợp theo bản vẽ

| Bản vẽ | Khoáng sản | Phụ lục VI | Số khu vực | Số điểm |
|---|---|---|---|---|
| 3.3 | Chì kẽm, khu vực Lào Cai 1 | VI.3 | 2 | 16 |
| 3.4 | Chì kẽm, khu vực Lào Cai 2 | VI.3 | 4 | 26 |
| 4.6 | Sắt, khu vực Lào Cai 2 | VI.4 | 36 | 323 |
| 8.4 | Đồng - molipden, khu vực Lào Cai 1 | VI.10, VI.12 | 15 | 105 |
| 8.5 | Đồng, khu vực Lào Cai 2 | VI.10 | 3 | 30 |
| 9.3 | Vàng | VI.13 | 7 | 47 |
| 11.2 | Đất hiếm, khu vực Lào Cai 1 | VI.14 | 4 | 33 |
| 11.3 | Đất hiếm, khu vực Lào Cai 2 | VI.14 | 3 | 34 |
| 12 | Apatit | VI.16 | 49 | 515 |
| | **Cộng** | | **123** | **1.129** |

## F. Danh mục khu vực (tọa độ từng điểm: CSV hoặc script)

### Bản vẽ 3.3 - Sơ đồ quy hoạch thăm dò, khai thác quặng chì kẽm khu vực Lào Cai 1 (tỷ lệ 1:100.000) — Phụ lục VI.3

| STT | Loại khu vực | Tên khu vực | Số điểm | Diện tích trên sơ đồ (ha) | Đối chiếu PL VI dự thảo |
|---|---|---|---|---|---|
| 1 | Khu vực quy hoạch thăm dò (sơ đồ không có chú giải; màu xanh lam) | Bản Mế | 8 | 17,9 | khớp |
| 2 | Khu vực quy hoạch thăm dò (sơ đồ không có chú giải; màu xanh lam) | Gia Khâu A | 8 | 154,5 | khớp |

### Bản vẽ 3.4 - Sơ đồ quy hoạch thăm dò, khai thác quặng chì kẽm khu vực Lào Cai 2 (tỷ lệ 1:100.000) — Phụ lục VI.3

| STT | Loại khu vực | Tên khu vực | Số điểm | Diện tích trên sơ đồ (ha) | Đối chiếu PL VI dự thảo |
|---|---|---|---|---|---|
| 1 | Khu vực đã thăm dò | Làng Rẩy-Núi Ngàng | 9 | 137,6 | khớp |
| 2 | Khu vực thăm dò cấp mới | Bản Lìm | 4 | 479,7 | khớp |
| 3 | Khu vực thăm dò cấp mới | Cây Luồng | 8 | 53,8 | khớp |
| 4 | Khu vực thăm dò cấp mới | Xà Hồ | 5 | 2,5 | khớp |

### Bản vẽ 4.6 - Sơ đồ quy hoạch thăm dò, khai thác quặng sắt khu vực Lào Cai 2 (tỷ lệ 1:100.000) — Phụ lục VI.4

| STT | Loại khu vực | Tên khu vực | Số điểm | Diện tích trên sơ đồ (ha) | Đối chiếu PL VI dự thảo |
|---|---|---|---|---|---|
| 1 | Khu vực đã cấp phép khai thác | Bắc Núi 300 (1) | 4 | 3,2 | khớp |
| 2 | Khu vực đã cấp phép khai thác | Bắc Núi 300 (2) | 4 | 1,9 | khớp |
| 3 | Khu vực đã cấp phép khai thác | Bắc Núi 300 (3) | 5 | 4,4 | khớp |
| 4 | Khu vực đã cấp phép khai thác | Bắc Núi 300 (4) | 9 | 18,9 | khớp |
| 5 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Bản Phào) (1) | 8 | 5,8 | khớp |
| 6 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Bản Phào) (2) | 7 | 3,8 | khớp |
| 7 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Làng Mỵ 2) (1) | 11 | 4,6 | khớp |
| 8 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Làng Mỵ 2) (2) | 15 | 11,4 | khớp |
| 9 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Làng Mỵ 2) (3) | 5 | 2,0 | khớp |
| 10 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Làng Mỵ 2) (4) | 5 | 0,8 | khớp |
| 11 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Làng Mỵ 2) (5) | 5 | 1,7 | khớp |
| 12 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Làng Mỵ) (1) | 7 | 7,9 | khớp |
| 13 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Làng Mỵ) (2) | 8 | 8,0 | khớp |
| 14 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Làng Mỵ) (3) | 14 | 20,2 | khớp |
| 15 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Làng Mỵ) (4) | 14 | 20,9 | khớp |
| 16 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Làng Mỵ) (5) | 9 | 21,8 | khớp |
| 17 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Làng Mỵ) (6) | 16 | 14,1 | khớp |
| 18 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Làng Mỵ) (7) | 12 | 4,3 | khớp |
| 19 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Làng Thảo) (1) | 5 | 9,6 | khớp |
| 20 | Khu vực đã cấp phép khai thác | Làng Mỵ 2 | 7 | 3,3 | khớp |
| 21 | Khu vực đã cấp phép khai thác | Làng Thảo (2) | 5 | 11,6 | khớp |
| 22 | Khu vực đã cấp phép khai thác | Núi 300 | 27 | 113,0 | khớp |
| 23 | Khu vực đã thăm dò | Làng Mỵ | 16 | 1599,2 | khớp |
| 24 | Khu vực đã thăm dò cấp mới | Bản Lan - Kiến Ba | 4 | 783,6 | khớp |
| 25 | Khu vực đã thăm dò cấp mới | Bản Phào | 5 | 113,5 | khớp |
| 26 | Khu vực đã thăm dò cấp mới | Gia Chẽ | 5 | 834,2 | khớp |
| 27 | Khu vực đã thăm dò cấp mới | Không ghi tên trên sơ đồ (gần Làng Thảo) (2) | 9 | 43,5 | khớp |
| 28 | Khu vực đã thăm dò cấp mới | Không ghi tên trên sơ đồ (gần Núi 300) | 10 | 29,9 | khớp |
| 29 | Khu vực đã thăm dò cấp mới | Làng Thảo (1) ⚠️ tên cần đối chiếu | 11 | 36,4 | khớp |
| 30 | Khu vực đã thăm dò cấp mới | Núi Vi | 21 | 185,7 | khớp |
| 31 | Khu vực đã thăm dò cấp mới | Suối Dầm - Suối Yong | 5 | 100,4 | khớp |
| 32 | Khu vực đã thăm dò cấp mới | Sùng Đô | 5 | 699,3 | khớp |
| 33 | Khu vực đã thăm dò cấp mới | Tân An - Bản Phào | 6 | 2126,0 | khớp |
| 34 | Khu vực đã thăm dò cấp mới | Xuân Giang | 7 | 172,9 | khớp |
| 35 | Khu vực đã thăm dò cấp mới | Xóm Bằng | 9 | 217,4 | khớp |
| 36 | Khu vực đã thăm dò cấp mới | Đông Nam Bản Phào | 8 | 98,6 | khớp |

### Bản vẽ 8.4 - Sơ đồ quy hoạch thăm dò, khai thác quặng đồng - molipden khu vực Lào Cai 1 (tỷ lệ 1:50.000) — Phụ lục VI.10, VI.12

| STT | Loại khu vực | Tên khu vực | Số điểm | Diện tích trên sơ đồ (ha) | Đối chiếu PL VI dự thảo |
|---|---|---|---|---|---|
| 1 | Khu vực khai thác - đã cấp | Khu vực đã cấp phép khai thác | 6 | 155,0 | khớp |
| 2 | Khu vực khai thác - đã cấp | Không ghi tên trên sơ đồ | 4 | 25,1 | khớp |
| 3 | Khu vực khai thác - đã cấp | Không ghi tên trên sơ đồ (gần Tả Phời (Cu)) (2) | 5 | 37,0 | khớp |
| 4 | Khu vực khai thác - đã cấp | Không ghi tên trên sơ đồ (gần Tả Phời (Cu)) (3) | 5 | 25,0 | khớp |
| 5 | Khu vực khai thác - đã cấp | Không ghi tên trên sơ đồ (gần Tả Phời (Cu)) (4) | 16 | 161,3 | khớp |
| 6 | Khu vực khai thác - đã cấp | Sinh Quyền (cu) | 9 | 296,3 | không khớp |
| 7 | Khu vực thăm dò, khai thác - đã cấp | Không ghi tên trên sơ đồ (gần Tả Phời (Cu)) (1) | 12 | 322,5 | khớp |
| 8 | Khu vực thăm dò, khai thác - đã cấp | Kin Tchang Hồ (Mo) | 4 | 46,3 | khớp |
| 9 | Khu vực thăm dò, khai thác - đã cấp | Lùng Thàng (Cu) | 4 | 1655,2 | khớp |
| 10 | Khu vực thăm dò, khai thác - đã cấp | Sin Quyền (Cu) phần mở rộng | 5 | 585,9 | khớp |
| 11 | Khu vực thăm dò, khai thác - đã cấp | Suối Thầu và Phìn Ngàn Chải (Cu) | 4 | 96,1 | khớp |
| 12 | Khu vực thăm dò, khai thác - đã cấp | Trịnh Tường (Cu) | 5 | 462,6 | khớp |
| 13 | Khu vực thăm dò, khai thác - đã cấp | Tả Phời (Cu) | 7 | 667,5 | khớp |
| 14 | Khu vực thăm dò, khai thác - đã cấp | Đông Nam Sin Quyền (Cu) | 4 | 385,9 | khớp |
| 15 | Khu vực thăm dò, khai thác - đã cấp | Đồng Vi Kẽm Cốc Mỳ (Cu) | 15 | 293,3 | khớp |

### Bản vẽ 8.5 - Sơ đồ quy hoạch thăm dò, khai thác quặng đồng khu vực Lào Cai 2 (tỷ lệ 1:50.000) — Phụ lục VI.10

| STT | Loại khu vực | Tên khu vực | Số điểm | Diện tích trên sơ đồ (ha) | Đối chiếu PL VI dự thảo |
|---|---|---|---|---|---|
| 1 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Khe Cam (Cu)) | 14 | 14,1 | khớp |
| 2 | Khu vực đã cấp phép khai thác | Làng Phát (Cu) | 8 | 14,4 | khớp |
| 3 | Khu vực thăm dò mới | Khe Cam (Cu) | 8 | 49,8 | khớp |

### Bản vẽ 9.3 - Sơ đồ quy hoạch thăm dò, khai thác quặng vàng tỉnh Lào Cai (tỷ lệ 1:100.000) — Phụ lục VI.13

| STT | Loại khu vực | Tên khu vực | Số điểm | Diện tích trên sơ đồ (ha) | Đối chiếu PL VI dự thảo |
|---|---|---|---|---|---|
| 1 | Khu vực đã cấp phép khai thác | Sa Phìn | 7 | 83,8 | khớp |
| 2 | Khu vực đã thăm dò | Không ghi tên trên sơ đồ (gần Tả Phời) (1) | 8 | 50,5 | khớp |
| 3 | Khu vực đã thăm dò | Không ghi tên trên sơ đồ (gần Tả Phời) (2) | 8 | 25,3 | khớp |
| 4 | Khu vực đã thăm dò | Tả Phời | 5 | 28,7 | khớp |
| 5 | Khu vực đã thăm dò cấp mới | Minh Lương | 10 | 111,6 | khớp |
| 6 | Khu vực đã thăm dò cấp mới | Ngoại vi mỏ Sa Phìn (1) | 5 | 47,9 | khớp |
| 7 | Khu vực đã thăm dò cấp mới | Ngoại vi mỏ Sa Phìn (2) | 4 | 82,9 | khớp |

### Bản vẽ 11.2 - Sơ đồ quy hoạch thăm dò, khai thác quặng đất hiếm khu vực Lào Cai 1 (tỷ lệ 1:50.000) — Phụ lục VI.14

| STT | Loại khu vực | Tên khu vực | Số điểm | Diện tích trên sơ đồ (ha) | Đối chiếu PL VI dự thảo |
|---|---|---|---|---|---|
| 1 | Khu vực đã thăm dò | Mỏ Bến Đền (1) | 13 | 212,5 | không khớp |
| 2 | Khu vực đã thăm dò | Mỏ Bến Đền (2) | 9 | 202,2 | không khớp |
| 3 | Khu vực đã thăm dò | Mỏ Bến Đền (3) | 7 | 285,7 | không khớp |
| 4 | Khu vực đã thăm dò cấp mới | Mỏ Mường Hum | 4 | 2984,1 | không khớp |

### Bản vẽ 11.3 - Sơ đồ quy hoạch thăm dò, khai thác quặng đất hiếm khu vực Lào Cai 2 (tỷ lệ 1:50.000) — Phụ lục VI.14

| STT | Loại khu vực | Tên khu vực | Số điểm | Diện tích trên sơ đồ (ha) | Đối chiếu PL VI dự thảo |
|---|---|---|---|---|---|
| 1 | Khu vực đã cấp phép khai thác | Mỏ Yên Phú | 11 | 6,2 | khớp |
| 2 | Khu vực đã thăm dò cấp mới | Làng Phát | 12 | 796,3 | khớp |
| 3 | Khu vực đã thăm dò cấp mới | Tân An | 11 | 773,5 | khớp |

### Bản vẽ 12 - Sơ đồ quy hoạch thăm dò, khai thác quặng apatit tỉnh Lào Cai (tỷ lệ 1:100.000) — Phụ lục VI.16

| STT | Loại khu vực | Tên khu vực | Số điểm | Diện tích trên sơ đồ (ha) | Đối chiếu PL VI dự thảo |
|---|---|---|---|---|---|
| 1 | Khu vực đã cấp phép khai thác | KT 13 | 4 | 61,8 | khớp |
| 2 | Khu vực đã cấp phép khai thác | KT 18 | 7 | 2,8 | khớp |
| 3 | Khu vực đã cấp phép khai thác | KT 19 | 10 | 49,7 | khớp |
| 4 | Khu vực đã cấp phép khai thác | KT 19B | 7 | 24,6 | khớp |
| 5 | Khu vực đã cấp phép khai thác | KT 32 | 6 | 12,8 | khớp |
| 6 | Khu vực đã cấp phép khai thác | KT Cam đường 2 | 23 | 24,1 | khớp |
| 7 | Khu vực đã cấp phép khai thác | KT Mỏ Cóc1 | 10 | 77,8 | khớp |
| 8 | Khu vực đã cấp phép khai thác | KT10 - Cam Đường 1 | 10 | 49,9 | khớp |
| 9 | Khu vực đã cấp phép khai thác | Khai trường 20-22 Vườn Cam | 7 | 76,6 | khớp |
| 10 | Khu vực đã cấp phép khai thác | Khai trường 38 Phú Nhuận | 10 | 9,9 | khớp |
| 11 | Khu vực đã cấp phép khai thác | Khai trường 39 Khu Văn Sơn | 21 | 24,1 | khớp |
| 12 | Khu vực đã cấp phép khai thác | Khu 40 Khu Võ Lao | 17 | 11,3 | khớp |
| 13 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần KT 19B) (1) | 3 | 4,4 | khớp |
| 14 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần KT 19B) (2) | 4 | 3,8 | khớp |
| 15 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần KT 19B) (3) | 5 | 2,1 | khớp |
| 16 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Khu vực Quang Kim-Bát Xá) | 32 | 29,0 | khớp |
| 17 | Khu vực đã cấp phép khai thác | Không ghi tên trên sơ đồ (gần Đông Bắc KT 10) | 10 | 74,8 | khớp |
| 18 | Khu vực đã cấp phép khai thác | Làng Cáng 2 | 7 | 36,7 | khớp |
| 19 | Khu vực đã cấp phép khai thác | Làng Phúng 1 | 25 | 91,9 | khớp |
| 20 | Khu vực đã cấp phép khai thác | Làng Phúng 2 | 6 | 4,0 | khớp |
| 21 | Khu vực đã cấp phép khai thác | Làng Phúng 3 | 8 | 3,9 | khớp |
| 22 | Khu vực đã cấp phép khai thác | Ngòi Đum -Đông Hồ | 51 | 80,6 | khớp |
| 23 | Khu vực đã cấp phép khai thác | Quang Kim Khu 1 | 17 | 19,6 | khớp |
| 24 | Khu vực đã cấp phép khai thác | Quang Kim Khu 2 | 9 | 14,2 | khớp |
| 25 | Khu vực đã cấp phép khai thác | Tam Đỉnh 1 | 9 | 21,0 | khớp |
| 26 | Khu vực đã cấp phép khai thác | Tam Đỉnh 2 | 9 | 15,3 | khớp |
| 27 | Khu vực đã thăm dò | KT 27 | 9 | 33,5 | khớp |
| 28 | Khu vực đã thăm dò | KT 28 | 6 | 38,0 | không khớp |
| 29 | Khu vực đã thăm dò | KT 29 | 5 | 5,6 | khớp |
| 30 | Khu vực đã thăm dò cấp mới | KT 11-12-31 | 10 | 91,6 | khớp |
| 31 | Khu vực đã thăm dò cấp mới | KT 17 | 9 | 262,3 | không khớp |
| 32 | Khu vực đã thăm dò cấp mới | KT 26 | 8 | 10,2 | khớp |
| 33 | Khu vực đã thăm dò cấp mới | KT 30 | 7 | 31,4 | khớp |
| 34 | Khu vực đã thăm dò cấp mới | KT 5 (khu 1) | 12 | 32,8 | khớp |
| 35 | Khu vực đã thăm dò cấp mới | KT 7 KT 5 (khu 2) (1) | 10 | 14,2 | lệch nhỏ |
| 36 | Khu vực đã thăm dò cấp mới | KT 7 KT 5 (khu 2) (2) | 5 | 10,1 | không khớp |
| 37 | Khu vực đã thăm dò cấp mới | KT 9/37 | 10 | 25,8 | không khớp |
| 38 | Khu vực đã thăm dò cấp mới | KT Làng Cáng 1 | 10 | 54,1 | khớp |
| 39 | Khu vực đã thăm dò cấp mới | KT Làng Cóc | 10 | 79,9 | khớp |
| 40 | Khu vực đã thăm dò cấp mới | Khai trường 23 | 8 | 22,1 | khớp |
| 41 | Khu vực đã thăm dò cấp mới | Khu vực Quang Kim-Bát Xá | 4 | 97,2 | khớp |
| 42 | Khu vực đã thăm dò cấp mới | Không ghi tên trên sơ đồ (gần Khai trường 38 Phú Nhuận) | 4 | 60,1 | khớp |
| 43 | Khu vực đã thăm dò cấp mới | Không ghi tên trên sơ đồ (gần Khu 40 Khu Võ Lao) (1) | 4 | 26,9 | khớp |
| 44 | Khu vực đã thăm dò cấp mới | Không ghi tên trên sơ đồ (gần Khu 40 Khu Võ Lao) (2) | 6 | 167,6 | khớp |
| 45 | Khu vực đã thăm dò cấp mới | Ngòi Bo - Ngòi Chát | 7 | 268,4 | khớp |
| 46 | Khu vực đã thăm dò cấp mới | Phía Nam Khai trường 25 | 4 | 11,8 | khớp |
| 47 | Khu vực đã thăm dò cấp mới | Tam Đỉnh - Làng Phúng (1) ⚠️ tên cần đối chiếu | 10 | 161,4 | khớp |
| 48 | Khu vực đã thăm dò cấp mới | Tam Đỉnh - Làng Phúng (2) ⚠️ tên cần đối chiếu | 23 | 155,9 | khớp |
| 49 | Khu vực đã thăm dò cấp mới | Đông Bắc KT 10 | 7 | 32,3 | khớp |
