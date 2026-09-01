# CHANGELOG — xp-sct-vn

## 1.0.1 — 01/9/2026
- **NĐ 311/2026/NĐ-CP xác minh từ chinhphu.vn**: ban hành 06/8/2026, **hiệu lực 26/9/2026**, PTTg Lê Tiến Châu ký; sửa Điều 6 NĐ 189/2025 (đổi tên Chi cục trưởng; thêm Chánh Thanh tra tỉnh vào nhóm Giám đốc Sở — 80% mức tối đa; các Cục trưởng; k4 Trưởng đoàn kiểm tra của tổ chức thuộc bộ), Điều 7 (Thanh tra viên, Trưởng đoàn thanh tra Thanh tra tỉnh), Công an, THADS, Điều 11 hải quan – thuế. Nhóm Giám đốc Sở không đổi.
- `references/00`: dòng NĐ 189/311 viết lại theo xác minh; quy tắc nền GĐ Sở = 80% mức tối đa lĩnh vực; cảnh báo không dẫn NĐ 311 trong QĐ ký trước 26/9/2026.
- `references/07` mục G: bổ sung quy tắc 80%/100%; ghi rõ Trưởng đoàn kiểm tra cấp Sở chưa được trao thẩm quyền theo tin công bố.
- `references/90`, `van-ban-goc/INDEX.md`, `mau-van-ban/07`, SKILL.md: đồng bộ mốc 26/9/2026; link PDF ký số (dạng ảnh, tải thủ công).
- Đã sửa `hnh-sct-vn` v1.8.3 trỏ về `xp-sct-vn` (6 file) thay tên plugin không tồn tại `xlvphc-sct-vn`.

## 1.0.0 — 01/9/2026

Khởi tạo plugin xử phạt VPHC đa lĩnh vực theo mô hình trục – nhánh, kế thừa toàn bộ `xp-hc-vlncn-sct-vn` v1.6.0 (giữ nguyên 7 references trong `references/01-vlncn-hoachat/`, văn bản gốc, hồ sơ mẫu thật).

## Mới
- `references/00-phan-chung-luat-xlvphc.md`: trục chung — văn bản nền (Luật 88/2025, NĐ 118 sđ 68+190/2025, NĐ 189/2025 sđ **NĐ 311/2026**, NĐ 61/2026), bảng thời hiệu theo lĩnh vực, bảng thời hạn thủ tục (BB 2 ngày LV, chuyển 24h, giải trình 2/5 ngày, ra QĐ 7 ngày LV/10/1 tháng/2 tháng, giao 2 ngày, nộp 10 ngày + 0,05%/ngày), nguyên tắc mức phạt, ranh giới hình sự, kiểm soát chất lượng BB VPHC và QĐ-XPHC, giao quyền, điện tử, hồ sơ.
- `references/02` HHNH: bản đồ 6 nghị định (NĐ 168/2024 Đ23 k5; NĐ 275/2026 hóa chất — Sở XỬ; NĐ 106/2025; Đ58 VLNCN; NĐ 98/2020; đường sắt NĐ 81/2026), 2 nút thay xử phạt (thu hồi GP Đ17 NĐ 161; k4 Đ52), ranh giới hiện trường.
- `references/03` CCN: NĐ 32/303 không có chế tài; bản đồ đầu tư (NĐ 122/2021 sđ **288/2026**), xây dựng (NĐ 16/2022 — dự thảo thay), đất đai (NĐ 123/2024 sđ **281/2026**), môi trường (NĐ 45/2022 — dự thảo thay), PCCC; 3 công cụ mạnh hơn phạt; bảng "vi phạm nào — chuyển ai"; bài học KL 45.
- `references/04` PCCC: 4 việc của Sở, chế tài NĐ 106/2025 (GATE), 2 hình thức kiểm tra định kỳ, bảng cơ sở PL II.
- `references/05` Kho VLNCN: bảng tồn tại → điểm-khoản-điều Đ57/53/54/61 NĐ 275/2026 (thiết kế – xây dựng – vận hành), hành vi phải chuyển, 4 bẫy tố tụng, câu viện dẫn mẫu.
- `references/06` Khoáng sản – môi trường: NĐ 36/2020 (dự thảo mới 3/2026), NĐ 45/2022; bảng định tuyến; 5 thành phần công văn chuyển hồ sơ; tiền lệ KL 45 (VB 863/TT-P4), KL 48 (VB 7962/UBND-NC).
- `references/07` ATTP (NĐ 115/2018), ATVSLĐ (**NĐ 283/2026** thay NĐ 12/2022), điện lực (**NĐ 133/2026**), xăng dầu – khí (NĐ 99/2020), thương mại (NĐ 98/2020 sđ 24/2025); bảng thẩm quyền chờ NĐ 311/2026.
- `references/90`: ma trận 18 lĩnh vực → nghị định → thời hiệu → ai phạt → XỬ/CHUYỂN → trạng thái xác minh; 3 câu hỏi quyết định; danh sách việc nợ.
- `mau-van-ban/` 12 mẫu + README quy ước (QĐ kiểm tra Mẫu 03; KH Mẫu 04 + đề cương báo cáo DN; TB Điều 7; BB công bố; BB kiểm tra Mẫu 05 + phụ lục + mục xác định hành vi – thời hiệu; BB VPHC Mẫu 01 đủ 10 mục; QĐ-XPHC 12 dòng căn cứ; BC kết quả Mẫu 06; CV chuyển hồ sơ; TTr Chủ tịch UBND tỉnh; QĐ tạm dừng/đình chỉ Mẫu 07–08; BC thực hiện KLTT theo Điều 54 Luật Thanh tra 2025).
- `checklists/` 8 khung kiểm tra 5 cột (nội dung – căn cứ – xem – hành vi – XỬ/CHUYỂN): kho VLNCN; sử dụng VLNCN – hộ chiếu; hóa chất; HHNH; CCN (CĐT hạ tầng + thứ cấp); PCCC điểm g, h; ATTP; mỏ khoáng sản phần Sở.
- `vi-du-thuc-te/`: thêm KL 45/KL-TT Viglacera (05/7/2026); BB kiểm tra Mẫu 05 Khí công nghiệp đã ký; KH 2922/KH-ĐKT; BB kiểm tra HCM Tây Bắc đã ký; BC 3094 của doanh nghiệp; VB 7962/UBND-NC.

## Nguyên tắc xác minh
Số hiệu nghị định các nhánh mới đã tra cứu đến 9/2026; **số điều/khoản của nghị định chưa có bản gốc đều đánh dấu GATE** — không viện dẫn vào biên bản/QĐ khi chưa đối chiếu. Việc nợ: tải ~14 bản gốc, lập bảng hành vi từng nhánh, điền bảng thẩm quyền theo NĐ 311/2026, sửa các plugin anh em trỏ về `xp-sct-vn`.
