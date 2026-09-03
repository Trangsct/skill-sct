# CHANGELOG — dacn-sct-vn

## v1.4.0 — 03/9/2026 (nạp danh mục dự án SXCN dự kiến hoàn thành, vận hành năm 2026)

**Nguồn:** File `1. Các DA SXCN dự kiến hoàn thành năm 2026.docx` do Bạn cung cấp ngày 03/9/2026 (3 trang, 1.311 từ), tiêu đề bản gốc "CÁC DỰ ÁN SXCN DỰ KIẾN HOÀN THÀNH ĐI VOÀ SẢN XUẤT NĂM 2026", ghi kỳ "(Tháng 9/2026)".

> ⚠️ **Tài liệu KHÔNG có số, ngày, cơ quan ban hành, người ký** — là bản tổng hợp/dự thảo phục vụ điều hành, không phải văn bản đã phát hành. GATE viện dẫn đã ghi ở đầu reference `10` và trường `_gate_vien_dan` của file JSON.

### Thêm mới
- `references/10-du-an-hoan-thanh-2026.md` — danh mục đầy đủ theo 05 nhóm a-đ của bản gốc:
  - **Nhóm a) 08 dự án chế biến** kèm công suất, chủ đầu tư, địa điểm, mốc, đóng góp dự kiến và bảng *việc phải làm ↔ cơ quan chịu trách nhiệm*. Sở Công Thương trực tiếp chủ trì 02/08 đầu việc (cấp phép hóa chất Triều Dương, Đức Giang).
  - **Nhóm b) khoáng sản**: mỏ sắt Quý Xa (5 triệu tấn/năm, 284 tỷ đồng — Sở Công Thương chủ trì, chạm 03 plugin `tkm-sct-vn`, `qlks-sct-vn`, `sd-vlncn-sct-vn`); khai trường apatit 24, 25, 19b; mỏ đồng Sin Quyền, Vi Kẽm, Tả Phời; các mỏ và nhà máy tuyển sắt đang tạm dừng.
  - **Nhóm c) 09 KCN** tách đúng hai Ban theo nguyên tắc bất biến số 6: 05 KCN đã có CTĐT (Bản Qua, Phú Xuân, Phú Xuân 1, Võ Lao, Cam Đường — Ban Quản lý Khu kinh tế tỉnh) và 04 KCN đang lập quy hoạch phân khu (Việt Hồng 1, Việt Hồng 2, Y Can, Đông An — Ban Quản lý các Khu công nghiệp tỉnh).
  - **Nhóm d) 14 lượt CCN** chia 05 nhóm đầu việc; Sở Công Thương chủ trì 04/05 nhóm — mảng nặng nhất của Sở trong tài liệu.
  - **Nhóm đ) năng lượng**: 04 công trình lưới điện, 04 thủy điện (Nậm Khoá 1-2, Hồ Bốn 2, Si Ma Cai, Lán Bò — 27 tỷ đồng), dự án cấp điện nông thôn do Sở Công Thương làm chủ đầu tư.
  - **Bảng gắn dự án ↔ chỉ tiêu NQ 169** (do plugin lập theo reference `03` mục V) và mục *giá trị sử dụng* của tài liệu.
- `du-lieu/du-an-hoan-thanh-2026.json` — bản máy đọc, mỗi mục đã gắn mã nhóm (ref `03`) và chỉ tiêu tác động. **Tách riêng khỏi `danh-muc-du-an.json`** vì khác nguồn và khác cấu trúc.

### Tổng hợp số
| Nhóm | Đóng góp dự kiến cộng dồn được |
|---|---|
| a) 07/08 dự án chế biến (loại trừ Quế Hồi Việt Nam) | 344,6 tỷ đồng |
| b) Mỏ sắt Quý Xa | 284 tỷ đồng |
| đ) 04 thủy điện | 27 tỷ đồng |
| **Tổng** | **655,6 tỷ đồng** |

Bản gốc **không có dòng tổng cộng** — con số 655,6 tỷ là do plugin cộng dồn, đã ghi rõ phạm vi tại reference và JSON.

### 11 cảnh báo bản gốc đã ghi nhận (KHÔNG tự sửa)
1. Không có số, ngày, cơ quan ban hành, người ký → cấm viện dẫn dạng "theo Văn bản số ... ngày ...".
2. Lỗi chính tả tiêu đề "ĐI VOÀ SẢN XUẤT" → đúng là "ĐI VÀO".
3. ⚠️ **Đóng góp của Nhà máy quế hữu cơ Bảo Thắng ghi 4.343 tỷ đồng** — lớn hơn tổng 09 dự án còn lại 6,6 lần, không phù hợp quy mô (dây chuyền sấy, tháp chưng cất); nhiều khả năng là 4,343 tỷ. **Đã loại khỏi mọi số tổng, chờ Bạn xác nhận.**
4. Lỗi bố cục: tiêu đề "b) Nhóm dự án khai thác, chế biến khoáng sản" dính vào cuối gạch đầu dòng dự án axit điện tử Đức Giang.
5. ⚠️ **04 mốc đã quá hạn tại thời điểm lập**: tài liệu ghi kỳ tháng 9/2026 nhưng để mốc tháng 8/2026 cho tuyển apatit Tam Đỉnh, mỏ sắt Quý Xa, khởi công KCN Cam Đường; mốc đầu tháng 9/2026 cho quế hữu cơ Bảo Thắng.
6. **Dồn 07 đầu việc vào mốc quý III/2026** (hết 30/9) — rủi ro trượt tiến độ tập trung rất cao trong tháng 9; cần rà từng đầu việc trước ngày 20/9 để kịp kỳ báo cáo.
7. Diện tích CCN Yên Hợp 2 ghi 75 ha — đối chiếu hồ sơ thẩm định tại `kccn-sct-vn`; không nhầm với CCN Yên Hợp (12 ha, QĐ 2201/2024) và CCN Yên Hợp 1 (63 ha) cùng tại xã Xuân Ái.
8. Công suất Nhà máy xử lý chất thải Việt Sơn 720.000 tấn/năm rất lớn — đối chiếu quyết định phê duyệt ĐTM trước khi trích.
9. Không ghi đóng góp bằng tiền ≠ đóng góp bằng 0 — để trống, không điền số 0.
10. Địa điểm Nhà máy quế hữu cơ Bảo Thắng không ghi xã/phường — không suy đoán từ tên "Bảo Thắng".
11. Hai số văn bản dẫn chiếu trong nhóm năng lượng (**1599/UBND-KT ngày 06/3/2026**, **2182/QĐ-UBND ngày 23/6/2026**) lấy nguyên văn bản gốc, **chưa đối chiếu bản scan có dấu** — phải chạy GATE trước khi viện dẫn.

### Phát hiện nghiệp vụ đáng chú ý
- **Ba nguồn cùng chỉ về một nút thắt**: rủi ro nguồn cung quặng apatit tại reference `08` (hai đầu mối apatit đăng ký sản lượng 2027 bằng 0), phân bón giảm sâu tại reference `09` (NPK −72,65%, MAP −57,41%) và nhóm khai trường 24, 25, 19b tại reference `10` → **GPMB và thuê đất khai trường apatit** là điểm nghẽn số 1 của chỉ tiêu 3 và 4.
- Tài liệu này chính là **danh mục giải pháp bù đắp** cho khoảng hụt 3,88 điểm % của chỉ tiêu 3 (IIP 6 tháng 9,12% / mục tiêu 13% — reference `09`).
- Mỗi dòng đã có sẵn *ai làm gì, hạn nào* → dùng trực tiếp cho `mau-van-ban/02` (công văn đôn đốc) mà không phải dựng lại.

### Cập nhật
- `SKILL.md`: thêm nghiệp vụ (10); thêm reference `10` và file JSON mới vào hai bảng tra; **bảng phạm vi dữ liệu từ 02 lên 03 nguồn**, ghi rõ reference `10` chỉ có mốc và đóng góp dự kiến, không có hồ sơ dự án đầy đủ; GATE Bước 1 bổ sung quy tắc dùng reference `10`; description làm lại còn 1.000 ký tự.
- `.claude-plugin/plugin.json`: version → **1.4.0**; bổ sung keywords `du-an-hoan-thanh-2026`, `quy-xa`, `thuy-dien`, `tram-bien-ap`.

### Lưu ý vận hành
Toàn bộ mốc và số đóng góp là **DỰ KIẾN tại thời điểm tháng 9/2026**. Trước mỗi kỳ báo cáo phải xác nhận với chủ đầu tư và cơ quan chủ trì xem dự án **đã vận hành thực tế chưa**; dự án chưa vận hành thì đưa vào mục điểm nghẽn, không tính vào chỉ tiêu sản lượng và IIP.

## [1.3.2] - 02/9/2026 — sửa theo scripts/check_facts.py (CI dữ kiện lỗi thời)
- Sửa các vi phạm do script quét: nơi nộp hồ sơ → motcua-tthc.moit.gov.vn; tiêu ngữ en dash trong mẫu; trỏ xp-hc-vlncn-sct-vn → xp-sct-vn; CN(M.Cường) trong mẫu → CN(Khôi), trong ví dụ lịch sử chú thích "lịch sử"; ký hiệu /GP-SCT bỏ chữ "dự kiến". Không đổi nghiệp vụ.

## v1.3.0 — 2026-07-27 (nạp mốc số liệu KTXH 6 tháng đầu năm 2026 của Thống kê tỉnh)

**Nguồn:** Báo cáo số **615/BC-TKT ngày 30/6/2026** của Thống kê tỉnh Lào Cai (Cục Thống kê) — Tình hình kinh tế - xã hội tháng 6 và quý II năm 2026 (67 trang). Số/ngày đối chiếu bản scan có dấu trên vOffice (số đến 13116, ban hành 30/6/2026); file .docx bản soạn thảo để trống ô số và ngày.

### Thêm mới
- `references/09-so-lieu-ktxh-6-thang-2026.md` — mốc so sánh 6 tháng đầu năm 2026, thay mốc Quý I:
  - GRDP 61.264,53 tỷ đồng, +9,01% (CN-XD +11,93%, riêng công nghiệp +12,16% đóng góp 3,13 điểm %; cơ cấu CN-XD lên 36,16%).
  - **Bảng đối chiếu đủ 9 chỉ tiêu SCT chủ trì**: IIP 9,12%/mục tiêu 13% (cảnh báo ĐỎ, không cải thiện so Quý I); bán lẻ +13,14%/12,9% (VƯỢT); điện thương phẩm +10,56%/12,10% (VÀNG, cải thiện mạnh, riêng tháng 6 +29,13%); XK +62%/93,5% và NK +57%/108,3% (ĐỎ, mới đạt ~30-35% kế hoạch giá trị); chỉ tiêu 4, 5, 32 chưa có số trong BC 615.
  - IIP chi tiết 4 ngành cấp 1 kèm đóng góp điểm % (điện +19,29% đóng góp 4,53 — động lực số 1); ngành cấp 2 tăng/giảm; bảng phân biệt 3 con số "chế biến, chế tạo" (VA 7,46% ≠ IIP 6,36% ≠ IIP tháng 6 13,69%).
  - Sản phẩm chủ yếu 6 tháng và tháng 6 (tăng: chì, kẽm, đá vôi, thép bán thành phẩm +2,7 lần, Supe +53,61%...; giảm: NPK −72,65%, MAP −57,41%, lân nung chảy, quặng sắt, vàng) — nhóm phân bón - hóa chất kéo lùi CBCT, khớp rủi ro apatit tại reference 08.
  - Tiêu thụ CBCT 6 tháng chỉ +0,47% trong khi sản xuất +6,36% → tồn kho +13,4%; lao động công nghiệp +7,88%.
  - XNK qua cửa khẩu 1.870 triệu USD (+35%, đạt 30,4% KH); Kim Thành ~400 xe/ngày; C/O 6 tháng ~420 nghìn tấn.
  - Vốn đầu tư toàn xã hội 26.861,38 tỷ (29,85% KH năm); giải ngân đầu tư công 32,68%; 13.335 doanh nghiệp (sát mục tiêu 13,4 nghìn).
  - Danh sách dự án công nghiệp - năng lượng ngoài Nhà nước đang triển khai (DCP-MCP-SSP Yên Bái, pin mặt trời Create Capital, 05 thủy điện, chưng cất dầu FO Hải Yến...) — đầu vào cập nhật sổ `danh-muc-du-an.json`.
  - **06 mâu thuẫn/lưu ý số liệu của bản gốc** ghi nhận, không tự sửa: đóng góp CN-XD 3,82 ≠ 3,83; câu "20 ngành... 16/21 ngành"; lỗi đánh máy "năm 2025"; đơn vị doanh thu bưu chính bất hợp lý (triệu đồng) — cấm trích dẫn khi chưa xác minh; 3 con số CBCT khác bản chất; phương pháp XNK của BC 615 khác kỳ gốc chỉ tiêu 7, 8 NQ 169 — phải chốt với Thống kê tỉnh và Hải quan.

### Cập nhật
- `references/02-chi-tieu-nq169-sct.md`: thêm ghi chú mốc mới nhất 6 tháng → trỏ reference `09`; cột Quý I giữ lại để thấy diễn biến.
- `SKILL.md`: thêm nghiệp vụ (9) tra số liệu KTXH chính thức của Thống kê tỉnh; thêm reference `09` vào bảng tra; GATE Bước 1 bổ sung quy tắc dùng reference `09` (ảnh chụp có kỳ chốt — chỉ làm mốc so sánh, không dùng làm số kỳ mới hơn); description làm lại còn 986 ký tự.
- `.claude-plugin/plugin.json`: version 1.2.0 → **1.3.0**; bổ sung keywords `grdp`, `thong-ke-tinh`, `bao-cao-ktxh`, `san-pham-chu-yeu`.

### Lưu ý vận hành
Toàn bộ số trong reference `09` là số **ước tính** của Thống kê tỉnh tại kỳ 6 tháng — trích dẫn phải kèm nguồn "Báo cáo 615/BC-TKT ngày 30/6/2026". Sang kỳ báo cáo mới (tháng 7, quý III) phải nạp số kỳ mới, không dùng lại bảng này làm số hiện hành.

## v1.2.0 — 2026-07-26 (nạp mảng KCN và Khu kinh tế cửa khẩu vùng Lào Cai cũ)

**Nguồn:** Kế hoạch số **72/KH-BQL ngày 08/7/2026** của Ban Quản lý Khu kinh tế tỉnh Lào Cai về Phát triển kinh tế - xã hội năm 2027 (Trưởng ban Vương Trinh Quốc ký số 08/7/2026 14:01:38), kèm biểu **Dự tính giá trị SXCN năm 2027**. Ban hành theo Văn bản 6607/UBND-TH ngày 27/6/2026 của UBND tỉnh. Nơi nhận có Sở Công Thương. Metadata đã trích từ PDF gốc bằng `extract_metadata.py` (GATE PDF).

### Thêm mới
- `references/08-kcn-kkt-bql-khu-kinh-te.md` — kết quả 2026 và kế hoạch 2027 của Ban Quản lý Khu kinh tế tỉnh: sản xuất công nghiệp, xuất nhập khẩu, xuất nhập cảnh, thu ngân sách và phí hạ tầng cửa khẩu, quy hoạch và thu hút đầu tư, tồn tại hạn chế, 05 định hướng nhiệm vụ 2027, mốc tiến độ Bản Vược và Cửa khẩu thông minh.
- `du-lieu/gtsxcn-kcn-kkt-2027.json` — biểu dự tính GTSXCN 2027 số hóa đầy đủ: **04 khu vực, 37 cơ sở, 85 dòng sản phẩm**, mỗi dòng có công suất thiết kế, tỷ lệ % công suất hoạt động, sản lượng đăng ký, GTSXCN (triệu đồng), doanh thu (đồng).

| Khu vực | GTSXCN 2027 (triệu đồng) | Cơ sở |
|---|---|---|
| KCN Tằng Loỏng | 24.869.912 | 17 |
| KCN Bắc Duyên Hải | 411.406 | 8 |
| KCN Đông Phố Mới | 161.022 | 9 |
| Khu kinh tế cửa khẩu | 859.008 | 3 |
| **Tổng cộng** | **26.301.347** | **37** |

Đối chiếu: cộng dồn 37 cơ sở = 26.301.348, dòng "Tổng cộng" của bản gốc ghi 26.301.347 — **lệch 1 triệu đồng do làm tròn trong Excel gốc**; doanh thu khớp tuyệt đối 38.097.407.344.052 đồng. Khi trích dẫn dùng đúng con số dòng Tổng cộng của bản gốc.

### 05 mâu thuẫn số liệu đã ghi vào reference 08 mục IV (KHÔNG tự sửa số của Ban)
1. **Mục tiêu 2027 (26.000 tỷ) thấp hơn ước thực hiện 2026 (28.000 tỷ) khoảng 7,1%** — Ban so với *kế hoạch* 2026 (25.000 tỷ) để ra "104%". Phải làm rõ trước khi tổng hợp vào chỉ tiêu IIP >12% và chỉ tiêu 3, 4 của NQ 169.
2. % tăng kim ngạch không khớp số tuyệt đối: xuất khẩu 1,65 → 2,2 tỷ USD thực tế +33,3% (văn bản ghi +23%); nhập khẩu 1,3 → 2 tỷ USD thực tế +53,8% (văn bản ghi +50%).
3. KCN Đông Phố Mới năm 2027 dừng hoạt động để phục vụ dự án đường sắt Lào Cai - Hà Nội - Hải Phòng (NQ 187/2025/QH15 ngày 19/02/2025) nhưng biểu vẫn đăng ký 161.022 triệu đồng.
4. Bản gốc đánh số trùng: Phần I mục II có hai mục cùng số "2" — trích dẫn theo tên mục, không theo số mục.
5. GTSXCN trong biểu là **giá hiện hành suy từ doanh thu**, không phải giá so sánh 2010 → không dùng trực tiếp tính IIP (reference `04`).

### 08 cảnh báo sử dụng ghi trong `_canh_bao_su_dung` của file JSON
Số 2027 là **đăng ký của doanh nghiệp**, không phải chỉ tiêu giao; cột "KH đăng ký" trộn nhiều đơn vị đo nên không cộng dồn; mục 7 và 8 của KCN Tằng Loỏng nằm trong ô gộp Excel (đọc theo layout: 7 = Phốt pho Apatit P7, 8 = quốc tế Lavita) nên cần xác nhận lại với Ban trước khi đưa vào văn bản chính thức; các ô trống giữ nguyên, không suy đoán; tỷ lệ 202% của Đông Phố Mới là cộng dồn đơn vị đo khác nhau, không trích dẫn.

### Phát hiện nghiệp vụ đáng chú ý
- **04 cơ sở đầu bảng chiếm 71,3% GTSXCN đăng ký** (Đức Giang P4 5.361.106 · VTM 5.068.226 · Luyện đồng Vimico 4.629.899 · DAP số 2 3.686.109) — trùng khớp nhận định "04 nhóm chủ lực" của Ban, là 04 điểm theo dõi ưu tiên khi cảnh báo hụt chỉ tiêu.
- **Cả hai đầu mối quặng apatit đăng ký sản lượng bằng 0** (Nhà máy Tuyển quặng Apatit 900.000 tấn CSTK; Đức Giang KT25 loại 1 và loại 3), cùng H3PO4 trích ly của Đức Giang P4 và supe lân của Apromaco — khớp với rủi ro "nguồn cung quặng apatit chưa ổn định" mà Ban nêu.
- **05 dây chuyền mới vận hành 2027** đã liệt kê để dựng kịch bản tăng trưởng (reference `07`) và bổ sung danh mục dự án động lực (reference `03`).

### Cập nhật
- `SKILL.md`: thêm nghiệp vụ (7) tổng hợp số liệu KCN, KKT cửa khẩu; thêm reference `08` và file dữ liệu mới vào bảng tra; **thay ghi chú phạm vi sổ bằng bảng hai địa bàn - hai Ban**; thêm nguyên tắc bất biến số 6 "phân biệt hai Ban, không gộp nhầm"; bổ sung từ khóa kích hoạt (GTSXCN, Tằng Loỏng, Bắc Duyên Hải, Đông Phố Mới, Khu kinh tế cửa khẩu, Bản Vược) — description 1.014 ký tự, dưới ngưỡng 1.024.
- `.claude-plugin/plugin.json`: version 1.1.2 → **1.2.0**; bổ sung keywords `kcn-tang-loong`, `khu-kinh-te-cua-khau`, `gtsxcn`.

### Lưu ý vận hành
Số 2026 trong reference `08` là **ước thực hiện tại thời điểm 08/7/2026**, số 2027 là **đăng ký của doanh nghiệp**. Cả hai đều là số động — đến kỳ báo cáo sau phải cập nhật lại từ báo cáo mới nhất của Ban Quản lý Khu kinh tế tỉnh, không dùng lại như số chính thức cả năm.

## v1.1.0 — 2026-07-23 (nạp dữ liệu thật 95 dự án trong 03 KCN)

### Thêm mới
- `du-lieu/danh-muc-du-an.json`: từ sổ rỗng → **95 dự án thứ cấp** trong 03 KCN do Ban Quản lý các Khu công nghiệp tỉnh Lào Cai quản lý. Nguồn: Phụ lục 01 và 02 kèm Báo cáo của Tổ rà soát (bản 12/5/2026) và Báo cáo đánh giá hiện trạng, tình hình triển khai các dự án đầu tư trong các KCN (số liệu chốt đến 16/4/2026).

| Chiều | Kết quả |
|---|---|
| Theo KCN | phía Nam 66 · Minh Quân 17 · Âu Lâu 12 (khớp tuyệt đối với Báo cáo) |
| Theo trạng thái | HD (đã sản xuất, kinh doanh) 46 · XD (đang đầu tư xây dựng) 13 · CT (chưa triển khai xây dựng) 36 |
| Theo nhóm | CBCT 80 · LK-HC 13 · NL 2 (phân loại tự động theo từ khoá, cần rà soát) |
| Tổng vốn đăng ký | 15.501,318 tỷ đồng (cộng dồn từng mục) |
| Điểm nghẽn | 63/95 dự án đang vướng, 238 lượt: xây dựng 96 · môi trường và PCCC 45 · chủ trương đầu tư 44 · nghĩa vụ tài chính 34 · đất đai 19 |
| Mức độ vướng | 1 dự án vướng 8 nhóm · 7 dự án vướng 7 nhóm · 6 dự án vướng 6 nhóm · 32 dự án không vướng |

### 05 cảnh báo về dữ liệu gốc (ghi trong trường `_canh_bao_du_lieu_goc`, script in ra đầu tiên khi chạy `kiem-tra`)
1. **09 dự án nhóm A đã dừng hoạt động nhưng phụ lục không chỉ rõ là dự án nào** (KCN phía Nam 06, Minh Quân 03). Sổ tạm để cả 46 ở trạng thái HD — phải xác định và chuyển sang TD trước khi tính chỉ tiêu sản lượng.
2. **Chênh lệch tổng vốn 98 tỷ đồng**: cộng dồn 95 mục = 15.501,318 tỷ, dòng "Tổng cộng" của phụ lục ghi 15.403,318 tỷ. Nguyên nhân: tiểu tổng "KCN phía Nam" nhóm B thiếu đúng 98 tỷ của mục 47 (Công ty TNHH Super Star). Sổ lấy theo cộng dồn từng mục.
3. **Chênh lệch cột nghĩa vụ tài chính 3 lượt**: cộng dồn 34, dòng tổng ghi 31; lệch ở nhóm B (STT 48, 50, 51, 58 có đánh dấu nhưng tiểu tổng ghi 01, và Phụ lục 01 để trống cột này). Sổ giữ nguyên đánh dấu từng mục, không tự sửa. **07 cột điểm nghẽn còn lại khớp tuyệt đối** giữa cộng dồn và dòng tổng.
4. Trường `xa_phuong` để trống — phụ lục không ghi địa giới hành chính mới sau 01/7/2025, không suy đoán.
5. Trường `nhom`, `nganh_cap_2` phân loại tự động theo từ khoá — cần rà soát thủ công, đặc biệt nhóm chế biến bột đá CaCO3 (ranh giới CBCT ↔ KS ảnh hưởng trực tiếp chỉ tiêu 4).

### Cập nhật
- `scripts/theo_doi_du_an.py` — lệnh `kiem-tra` viết lại: in kỳ số liệu và ngày cập nhật ở đầu; in khối cảnh báo về dữ liệu gốc trước tiên; **gom cảnh báo theo LOẠI kèm số lượt và ví dụ** thay vì liệt kê từng dòng (238 dòng → 1 khối), giới hạn 20 dòng lỗi.
- `SKILL.md` mục VI: mô tả nội dung sổ và **ghi rõ phạm vi còn thiếu** (KCN do Ban Quản lý Khu kinh tế tỉnh quản lý, CCN, dự án ngoài khu/cụm, khoáng sản, thuỷ điện, hạ tầng KCN/CCN).
- `.claude-plugin/plugin.json`: version 1.1.0.

### Lưu ý vận hành
Sổ là **số liệu động**, chỉ đúng tại kỳ ghi ở `_ky_so_lieu`. Trước mỗi kỳ báo cáo phải cập nhật lại từ báo cáo mới nhất của Ban Quản lý các Khu công nghiệp tỉnh và Ban Quản lý Khu kinh tế tỉnh. Trường `_canh_bao_han_dung` trong file nhắc lại điều này.

## v1.0.1 — 2026-07-23 (xác nhận 03 điểm treo, gỡ toàn bộ GATE)

Bạn đã đối chiếu bản gốc có dấu và xác nhận ngày 23/7/2026. Ba nội dung treo ở v1.0.0 nay đã chốt:

1. **Số Công văn triển khai của UBND tỉnh Lào Cai: 7323/UBND-TH ngày 17/7/2026** (Chủ tịch Nguyễn Tuấn Anh ký). Con số 7325 trên trang Phụ lục của bản scan là lệch dấu đóng số — không dùng.
2. **Ba dòng phân nhóm hàng xuất khẩu (7a nông-lâm-thuỷ sản 87,5%; 7b công nghiệp chế biến, chế tạo 7,14%; 7c nhiên liệu, khoáng sản 18,18%) CÓ trên bản ký** và được sử dụng chính thức. Việc 7a, 7b mờ/mất và 7c bị đánh số nhầm thành TT 10 là lỗi in ấn của bản scan, không phải nội dung văn bản. Khi lập bảng trong báo cáo, đánh số lại theo trật tự 7a, 7b, 7c dưới chỉ tiêu 7.
3. **Chỉ tiêu 29 (tỷ lệ KCN đang hoạt động có hệ thống xử lý nước thải tập trung đạt chuẩn), mục tiêu năm 2026: 42%.** Con số 41,7% trong bản dự thảo Excel là số cũ — không dùng.

### Cập nhật
- `SKILL.md` mục III.5: thay khối cảnh báo GATE bằng ghi nhận đã xác nhận; bổ sung người ký.
- `references/01-khung-phap-ly-tang-truong.md`: thay GATE số văn bản bằng xác nhận, ghi rõ người ký.
- `references/02-chi-tieu-nq169-sct.md`: gỡ 02 cảnh báo (7a/7b/7c và chỉ tiêu 29); bổ sung hướng dẫn đánh số lại 7a, 7b, 7c khi lập bảng báo cáo.
- `mau-van-ban/01`: điền số 7323/UBND-TH vào đoạn mở đầu; sửa lưu ý số 1 thành căn cứ viện dẫn chuẩn.
- `mau-van-ban/02`: điền số 7323/UBND-TH vào phần căn cứ.
- `mau-van-ban/03`: ghi đầy đủ số, ngày Công văn ở phần căn cứ.
- `.claude-plugin/plugin.json`: version 1.0.1.

**Kết quả:** plugin không còn nội dung treo; toàn bộ căn cứ pháp lý đã đủ điều kiện viện dẫn trực tiếp vào văn bản phát hành.

## v1.0.0 — 2026-07-23 (phát hành lần đầu)

### Bối cảnh
Plugin được xây dựng để đáp ứng yêu cầu tại Nghị quyết số 169/NQ-CP ngày 27/6/2026 của Chính phủ về mục tiêu tăng trưởng của các địa phương năm 2026 và giai đoạn 2026-2030, và Công văn triển khai của UBND tỉnh Lào Cai ngày 17/7/2026 (kèm Phụ lục phân công 32 chỉ tiêu). Sở Công Thương được giao **chủ trì theo dõi, tổng hợp, đánh giá và báo cáo 09 chỉ tiêu**, phối hợp 06 chỉ tiêu.

### Thêm mới
- `SKILL.md`: 07 trigger nghiệp vụ; quy trình chuẩn 5 bước với GATE số liệu động/tĩnh; bảng phân vai với 10 plugin trong hệ sinh thái; bảng tra nhanh 09 chỉ tiêu chủ trì; 06 nguyên tắc bất biến.
- `references/01-khung-phap-ly-tang-truong.md`: chuỗi văn bản KL 18-KL/TW → NQ 25/2026/QH16 → NQ 109/NQ-CP → NQ 169/NQ-CP → Công văn UBND tỉnh; mục đích yêu cầu; nhiệm vụ chung; trách nhiệm cơ quan chủ trì (điểm a-d), cơ quan phối hợp (điểm a-d), người đứng đầu; bảng đầu mối cấp tỉnh.
- `references/02-chi-tieu-nq169-sct.md`: **bảng đầy đủ 32 chỉ tiêu**, tách 3 nhóm chủ trì / phối hợp / tham khảo; kết quả Quý I/2026 làm mốc; ghi nhận 2 sai lệch giữa bản dự thảo Excel và bản ký (mất 2 dòng phân nhóm hàng xuất khẩu; chỉ tiêu 29 lệch 41,7 và 42); 5 quy tắc sử dụng bảng.
- `references/03-danh-muc-du-an-dong-luc.md`: 07 nhóm dự án (HT-KCN, HT-CCN, KS, LK-HC, CBCT, NL, TM); 08 trạng thái vòng đời; thang chấm điểm ưu tiên 100 điểm với 7 tiêu chí; trường dữ liệu bắt buộc; quy tắc gắn dự án ↔ chỉ tiêu và 3 sai lầm thường gặp; 6 nguồn hình thành danh mục.
- `references/04-phuong-phap-tinh-va-nguon-so-lieu.md`: cách tính IIP, giá trị sản xuất giá so sánh 2010 và giá thực tế, điện thương phẩm (phân biệt với điện phát), kim ngạch xuất nhập khẩu, chế biến chế tạo, tổng mức bán lẻ, tiết kiệm năng lượng; bảng nguồn số liệu theo từng chỉ tiêu; quy trình 5 bước xử lý chênh lệch số liệu với Thống kê tỉnh.
- `references/05-che-do-bao-cao.md`: hạn trước ngày 20 của kỳ báo cáo, đầu mối Sở Tài chính, cơ chế lồng ghép NQ 01/NQ-CP; 5 nội dung bắt buộc; khung báo cáo 7 mục; 6 quy tắc số liệu; lịch công tác gợi ý trong tháng; 3 trường hợp báo cáo đột xuất.
- `references/06-diem-nghen-va-thao-go.md`: 07 nhóm điểm nghẽn (QH, CTDT, GPMB, DD, XD, MT-PCCC, TC) chưng cất từ thực tiễn rà soát dự án trong các KCN; biểu hiện và hướng xử lý từng nhóm; quy tắc 04 yếu tố bắt buộc khi đưa điểm nghẽn vào báo cáo.
- `references/07-kich-ban-tang-truong.md`: 3 kịch bản chuẩn; phương pháp ngoại suy 5 bước; xử lý riêng nhóm chịu tính mùa vụ (điện phát, nông sản chế biến); 4 ngưỡng cảnh báo; mẫu giải trình chỉ tiêu có nguy cơ không hoàn thành; quy tắc liên kết kịch bản ngành với kịch bản tỉnh.
- `scripts/phan_tich_thang.py`: đọc file Excel theo dõi sản xuất công nghiệp hằng tháng (sheet T1-T12), tính tỷ lệ hoàn thành kế hoạch năm, độ lệch so tiến độ chuẩn, tăng giảm so cùng kỳ và so tháng trước, ước thực hiện cả năm; tự gắn nhãn 4 mức cảnh báo; xuất CSV; không suy đoán số thiếu, đánh dấu THIEU-SO-LIEU.
- `scripts/theo_doi_du_an.py`: 7 lệnh quản lý sổ danh mục dự án (kiem-tra, danh-sach, chi-tieu, diem-nghen, trong-diem, bang-bao-cao, cham-diem); tự kiểm tra tính hợp lệ, phát hiện bản ghi thiếu nguồn và bản ghi tính sản lượng sai trạng thái; chấm điểm ưu tiên tự động theo thang 100.
- `du-lieu/schema-du-an.json`: lược đồ JSON Schema đầy đủ cho một bản ghi dự án.
- `du-lieu/danh-muc-du-an.json`: sổ dữ liệu khởi tạo rỗng — plugin không tự sinh dữ liệu.
- `mau-van-ban/01-bao-cao-dinh-ky-nq169.md`: khung báo cáo định kỳ 7 mục kèm bảng 9 chỉ tiêu chủ trì có sẵn mục tiêu.
- `mau-van-ban/02-cong-van-don-doc-du-an.md`: công văn đôn đốc chủ đầu tư và UBND cấp xã.
- `mau-van-ban/03-bao-cao-giai-trinh-chi-tieu.md`: báo cáo giải trình chỉ tiêu có nguy cơ không hoàn thành.
- `checklists/checklist-so-lieu-ky-bao-cao.md`: 12 mục kiểm tra số liệu trước khi trình ký.
- `checklists/checklist-ra-soat-diem-nghen.md`: rà soát dự án chậm tiến độ theo 07 nhóm điểm nghẽn.

### Lưu ý còn treo
- **Số Công văn triển khai của UBND tỉnh**: bản scan đóng dấu số tự động, OCR không xác minh được; trang 1 hiển thị 7323, Phụ lục hiển thị 7325. Đã đánh dấu GATE tại `SKILL.md` mục III.5 và `references/01`. **Cần xác nhận trên bản gốc trước khi viện dẫn trong văn bản phát hành.**
- **Hai dòng phân nhóm hàng xuất khẩu** (nông lâm thuỷ sản, công nghiệp chế biến chế tạo) chỉ có trong bản dự thảo Excel, không hiển thị trên bản ký. Cần đối chiếu bản gốc có dấu.
