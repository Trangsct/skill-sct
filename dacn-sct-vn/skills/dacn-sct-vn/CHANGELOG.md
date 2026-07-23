# CHANGELOG — dacn-sct-vn

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
