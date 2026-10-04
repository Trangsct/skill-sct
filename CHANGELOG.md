## kccn-sct-vn 1.47.0 — 04/10/2026: danh mục thu hút đầu tư các CCN, các KCN và tin báo cáo Lãnh đạo, số chốt hết 01/10/2026

- Reference 43 mới: phân nhóm, số cộng danh mục CCN (09 cụm doanh nghiệp làm chủ đầu tư 634,95 ha, 5.158,58 tỷ; 05 cụm đã nộp hồ sơ, có Bản Phiệt 1; 22 cụm kêu gọi sau khi bỏ CCN Thống Nhất 35 ha); 14 KCN (Cam Đường chưa khởi công; quy hoạch phân khu Đông An chưa phê duyệt); 10 lỗi đã bắt trong file nguồn; 05 điểm vênh còn mở; mẫu tin báo cáo Lãnh đạo.
- Bạn chốt 04/10/2026: chưa rõ thì bỏ khỏi bản trình; tên 02 file danh mục cùng một kiểu (ref 31 mục 13). Rà thông tin cũ ở ref 32, 34, 36, 41, 42.
- check_facts: `kcn-cam-duong-chua-khoi-cong`, `ccn-mong-son-tmdt-496-651` (FAIL).

## 01/10/2026 — Dòng Lưu không ghi tên chuyên viên (20 plugin)

- Bạn chốt 01/10/2026: từ nay không ghi tên chuyên viên ở cuối văn bản — dòng Lưu chỉ ghi `Lưu: VT, CN.` (công văn nội bộ Phòng `Lưu: CN.`), thay quy ước cũ "Lưu: VT, CN(tên)".
- vbhc-vn 2.28.0: `fill_template.chuan_hoa_dong_luu()` tự bỏ tên khi dựng từ mẫu thật cũ (`build_vb.py`, `TemplateDoc.save()`); R07 WARN khi còn tên; template trắng 02–06, 08 sửa dòng Lưu; mẫu thật `examples/` giữ nguyên.
- sct-laocai-org-vn 2.5.0: bảng chuyên viên ↔ lĩnh vực chỉ còn để phân việc, không đưa tên vào văn bản.
- Mọi plugin nghiệp vụ: mẫu văn bản, hướng dẫn về `Lưu: VT, CN.`; chỗ nêu chuyên viên tham mưu đổi "CN(Tên)" thành "CV Tên". Ví dụ thực tế, văn bản gốc, CHANGELOG cũ giữ nguyên (lịch sử).
- `scripts/check_facts.py`: rule mới `luu-khong-ghi-ten-chuyen-vien` (FAIL), bỏ rule `cn-m-cuong-vlncn`.
- Phiên bản: attp-sct-vn 1.5.2, atvsld-sct-vn 1.0.1, bvmt-sct-vn 1.6.1, dacn-sct-vn 1.6.2, data360x-sct-vn 1.1.1, hc-sct-vn 1.3.1, hl-vlncn-sct-vn 1.4.4, hnh-sct-vn 1.11.1, kccn-sct-vn 1.46.1, kho-vlncn-sct-vn 1.12.1, pccc-sct-vn 1.3.1, qlks-sct-vn 2.1.1, quy-hoach-ct-vn 1.4.1, sct-laocai-org-vn 2.5.0, sd-vlncn-sct-vn 2026.10.1.1, tkm-sct-vn 1.4.1, vbhc-vn 2.28.0, xd-sct-vn 1.6.1, xp-hc-vlncn-sct-vn 1.6.2, xp-sct-vn 1.6.1.

## kccn-sct-vn 1.46.0 — 01/10/2026: 38 nhóm ngành, nghề thu hút đầu tư KCN Phú Xuân, Phú Xuân 1 (VB 9813/UBND-XD ngày 27/9/2026); chi tiết QĐ 3480 tuyến 4E

- Ref 15 mục IV-ter mới: bảng 38 nhóm ngành (mã ngành QĐ 36/2025/QĐ-TTg, STT Phụ lục II NĐ 48/2026/NĐ-CP), điều kiện BVMT, lưu ý khi góp ý dự án thứ cấp.
- Ref 23: mặt cắt, cơ cấu tổng mức đầu tư 130 tỷ của tuyến QL4E – CCN Thống Nhất 1 theo bản gốc QĐ 3480.

## kccn-sct-vn 1.45.1 — 01/10/2026: Bạn chốt lấy số liệu theo báo cáo của xã, chủ đầu tư (mới hơn)

- Ref 42 mục C đã chốt: Yên Thế lấp đầy 59,5%, 05 DN; Hưng Khánh 32,75%; Bắc Văn Yên theo danh sách xã; Y Can khởi công dự kiến 11/2026; lấp đầy bình quân 23 cụm tính lại 30,49%. Ref 31 mục 12 mới; ref 41 đánh dấu số cũ là lịch sử.
- check_facts: `ccn-yen-the-lap-day-59-5`, `ccn-hung-khanh-lap-day-32-75` (FAIL); `ccn-y-can-khoi-cong-11-2026` lên FAIL.

## kccn-sct-vn 1.45.0 — 01/10/2026: báo cáo của UBND cấp xã và chủ đầu tư hạ tầng theo CV 6059/SCT-CN ngày 28/9/2026

- Reference 42 mới: 07 báo cáo (Bắc Duyên Hải; phường Văn Phú — Phú Thịnh 1, 2, 3; xã Lục Yên — Yên Thế; xã Đông Cuông — Bắc Văn Yên, Đông An, An Bình; xã Hưng Khánh; Công ty 888 — Phú Thịnh 2; Công ty Tây Bắc — Y Can): số liệu GPMB, doanh nghiệp, hạ tầng, kiến nghị; bảng 12 điểm vênh chờ chốt.
- Ref 41 trỏ sang ref 42; check_facts thêm `ccn-phu-thinh-2-chua-co-qd-thue-dat` (FAIL), `ccn-y-can-khoi-cong-11-2026` (WARN).
- Kèm theo: sinh lại `vbhc-vn/.../data/vbpl.json` từ `registry/trang-thai.csv` (bước nạp VBPL đầu phiên; không có dòng mới).

## bvmt-sct-vn 1.6.0 — 01/10/2026: Quy chế dữ liệu tài nguyên và môi trường tỉnh Lào Cai (QĐ 3556/QĐ-UBND ngày 30/9/2026)

- Reference 12 mới: phần việc của Sở Công Thương theo Quy chế kèm QĐ 3556/QĐ-UBND — giao nộp dữ liệu (≤ 30 ngày sau nghiệm thu nhiệm vụ; 01 năm; 03–04 tháng hồ sơ XDCB), biên bản BM.01 TT 03/2022, metadata, Mẫu 01 và báo cáo Mẫu 05 NĐ 73/2017 trước 15/12 hằng năm; bảng dữ liệu TNMT đang ở Sở; điểm vênh về khoáng sản với NQ 66.25/2026/NQ-CP; lịch việc đề xuất.
- Bản gốc + bản trích chữ tại `bvmt-sct-vn/.../van-ban-goc/tinh/`; ref 01, 02, SKILL.md, INDEX cập nhật.
- QĐ 44/2021/QĐ-UBND (Lào Cai) và QĐ 23/2011/QĐ-UBND (Yên Bái) bị bãi bỏ từ 30/9/2026: rule check_facts `qd-44-2021-ubnd-du-lieu-tnmt-bai-bo`, ghi vào `registry/trang-thai.csv`.
- Kèm theo: nạp 4 văn bản pháp luật mới từ `vlncn-laocai/theo-doi/de-xuat-vbpl.csv` (QĐ 2405/QĐ-BCT, QĐ 3430, 3433, 3443/QĐ-UBND) vào `registry/trang-thai.csv`, sinh lại `vbhc-vn/.../data/vbpl.json`.

## sd-vlncn-sct-vn 2026.9.30.1 — 30/9/2026: PANM bản đầy đủ có bìa, đường kẻ quốc hiệu; kíp theo thiết kế đã thẩm định (Kim Thành)

- Anti-error 37 (references/11): PANM giao doanh nghiệp phải đầy đủ, dài theo Phụ lục VII TT 23/2024; bìa viền kép, đường kẻ Straight Connector dưới tên DN và tiêu ngữ (gạch ngang dài), đánh số trang từ trang nội dung; kíp tính theo chỉ tiêu thiết kế đã thẩm định, không tự dựng tỷ lệ kíp/kg; bỏ câu đối chiếu thừa dễ làm DN bị bắt lỗi; viện dẫn thiết kế bằng văn bản thẩm định của Sở.
- mau-van-ban/22: thêm mục "Trình bày bắt buộc khi xuất PANM cho doanh nghiệp"; references/07 mục K: sửa chuỗi thiết kế 2021 (Sơn Thái, 88/BCTT-AH, VB 897/SCT-KTATMT ngày 18/5/2021), thêm giai đoạn 2.
- Ví dụ thực tế: script dựng PANM Kim Thành và bản .docx đầy đủ 42 trang (57.115 kíp/năm, 40.480 kg thuốc nổ/năm).
- scripts/check_facts.py: rule `kim-thanh-tham-tra-2021-88-bctt`.

## data360x-sct-vn 1.1.0 — 30/9/2026: hàng đợi TAY thay runner

- Reference 05 mới: tiến trình TAY (`ccn-laocai/tay/tay.py`) trên laptop/máy bàn tự kéo việc từ `vlncn-laocai/yeu-cau/*.json` mỗi 10 phút; định dạng tệp yêu cầu, 3 cách ghi, chờ/đọc kết quả, nhịp tim `trang-thai/tay.json`. `goi_bot.py --qua-tay`. SKILL.md: ưu tiên TAY, bốn workflow runner chỉ còn dự phòng.
- Bối cảnh: bot ngừng 11 ngày (18–29/9), runner lên laptop hỏng 3 lần, lượt online bị cổng từ chối; Bạn chốt 30/9/2026 xây lại bộ công cụ (`ccn-laocai/bot/KE-HOACH-XAY-LAI.md`).

## 29/9/2026 — marketplace: sửa lỗi claude.ai ngừng đồng bộ từ 11/9 (archive kho vượt trần 512 MB)

- Nguyên nhân: claude.ai tải archive zip của kho khi đồng bộ, trần 512 MB (docs Cowork → Limits). Archive nén: 503,6 MB ở commit 10/9 (đồng bộ được), 512,8 MB ở commit 11/9 (bvmt 1.5.0 thêm 5 PDF), 520,1 MB ngày 28/9 → "Sync failed", mọi plugin trên claude.ai đứng ở bản 10/9 trong khi kho và CI vẫn bình thường.
- Sửa: `scripts/export_ignore.py` (mới) sinh `.gitattributes` đánh `export-ignore` cho 55 tệp ≥ 3 MB → archive còn 207 MB; tệp vẫn nằm trong kho cho git clone / Claude Code. `check_descriptions.py` gọi thêm `export_ignore.py --check` (CI đỏ nếu `.gitattributes` lệch hoặc archive dự tính > 400 MB, plugin > 150 MB).
- CLAUDE.md, README: ghi cơ chế đồng bộ của claude.ai (tự chạy khi push/merge vào main, nút Re-sync) và quy tắc kèm bản trích chữ cho văn bản gốc nặng.
- Không đổi nội dung hay version plugin nào.

## data360x-sct-vn 1.0.6 — 28/9/2026: sửa lỗi "Sync failed" trên claude.ai

- Description SKILL.md của data360x-sct-vn có `danh-muc-<năm>.json` — ký tự `<` `>` làm claude.ai từ chối đồng bộ marketplace; đổi thành `danh-muc-NĂM.json`.
- `scripts/check_descriptions.py`: chặn ký tự `<` `>` trong description plugin.json và mọi SKILL.md.

## kccn-sct-vn 1.44.0 — 28/9/2026

- Kỳ cập nhật 28/9/2026 (ref 41): Mông Sơn, Yên Hợp 2 đã thành lập (QĐ 3426, 3427 ngày 23/9/2026); tuyến Quốc lộ 4E phê duyệt dự án QĐ 3480 ngày 27/9/2026; bản gốc QĐ 2071 (IC18 260 tỷ, gỡ cờ đỏ địa danh); lấp đầy CCN 29,02%; 08 quy ước bộ tài liệu họp Chủ tịch UBND tỉnh; rà lại ref 12, 22, 23, 30, 31, 39; 02 rule check_facts mới; 04 ví dụ thực tế.

## 25/9/2026 — kho-vlncn-sct-vn 1.12.0: ref 03 theo khung 01/7/2026; mẫu 10 hướng dẫn trình tự 3 đối tượng kho

- ref 03: thẩm định BCNCKT tại Sở, thiết kế triển khai do chủ đầu tư thẩm định (Đ41 NĐ 217), năng lực NĐ 212/2026, báo cáo hoàn thành k4 Đ27 NĐ 207; bỏ NĐ 175/2024 và Điều 23 NĐ 06/2021 khỏi hướng dẫn hiện hành.
- mẫu 10 mới: công văn hướng dẫn trình tự kho cố định xây mới, kho tạm (kể cả container), kho hiện hữu.

## 24/9/2026 (đợt 3) — sd-vlncn-sct-vn 2026.9.24.2: sửa nơi nộp hồ sơ GĐ6

- ref 04 GĐ6: nơi nộp hồ sơ GP sử dụng VLNCN là https://motcua-tthc.moit.gov.vn/ (bỏ Trung tâm PVHCC / Cổng DVC / bưu chính).

## 24/9/2026 (đợt 2) — NĐ 347/2026 lan sang 6 plugin + mẫu công văn triển khai; sửa mức phạt tổ chức

- **pccc-sct-vn 1.3.0:** mẫu 01 — công văn Sở hướng dẫn chủ đầu tư thực hiện NĐ 347/2026 + CV 6501/CAT-PCCC; sửa mức phạt k3 Đ18 NĐ 106 (tổ chức 60–100 triệu, đình chỉ 3–6 tháng); sửa nhận định "UBND tỉnh chưa phân cấp kiểm tra định kỳ" — Điều 17 khoản 1 QĐ 11/2026/QĐ-UBND đã giao.
- **xp-sct-vn 1.6.0:** k3, k4 Điều 18 NĐ 106 theo NĐ 347; Sở còn 3 việc về PCCC; checklist 01, 05, 06.
- **sd-vlncn-sct-vn 2026.9.24.1:** hồ sơ PCCC kho cố định trong hồ sơ GP sử dụng = biên bản nghiệm thu của chủ đầu tư.
- **kho-vlncn-sct-vn 1.11.1, dacn-sct-vn 1.6.1, kccn-sct-vn 1.43.1:** mức phạt tổ chức; bỏ "Công an tỉnh nghiệm thu PCCC".
- **check_facts.py:** rule `pccc-nghiem-thu-nd347` quét thêm xp, sd-vlncn, dacn, kccn, hc, tkm, attp.

## 24/9/2026 — pccc-sct-vn 1.2.0 + kho-vlncn-sct-vn 1.11.0 + xd-sct-vn 1.6.0: NĐ 347/2026/NĐ-CP và CV 6501/CAT-PCCC (chủ đầu tư tự nghiệm thu PCCC)

- Nguồn: NĐ 347/2026/NĐ-CP ngày 08/9/2026 (hiệu lực 15/9/2026) sửa NĐ 105/2025, NĐ 106/2025; CV 6501/CAT-PCCC ngày 23/9/2026 của Công an tỉnh Lào Cai phối hợp triển khai NQ 66.18/2026/NQ-CP.
- **pccc-sct-vn 1.2.0:** ref 16 mới; bãi bỏ k5 Đ6, Đ10 NĐ 105 → không còn kiểm tra nghiệm thu PCCC của Sở lẫn Công an, CĐT tự nghiệm thu; thẩm định PCCC chỉ trong BCNCKT; trình tự kiểm tra định kỳ mới (trước 15/12, 03 ngày làm việc, PC03, Công an chủ trì khi phối hợp); Phụ lục III mới; ref 04 viết lại, ref 05 và 9 ref khác sửa.
- **kho-vlncn-sct-vn 1.11.0:** đầu mục PCCC của kho = biên bản nghiệm thu PCCC của CĐT; mẫu 01, 02, 08 và checklist bỏ yêu cầu văn bản chấp thuận của Công an.
- **xd-sct-vn 1.6.0:** PCCC trong KTCTNT; Điều 74 NĐ 217/2026 bị Điều 39 NĐ 347 bãi bỏ; anti-error 15.
- **check_facts.py:** rule `pccc-nghiem-thu-nd347` (chỉ quét 3 plugin trên).

## 22/9/2026 — kccn-sct-vn 1.43.0 + vbhc-vn 2.27.0: rà soát Báo cáo NQ 34-NQ/TU tháng 9/2026

- **kccn-sct-vn 1.43.0:** ref 40 (mới) — 06 báo cáo đầu vào kỳ tháng 9/2026; số chốt bảng GPMB (03 KCN 626,24 ha; tổng GPMB 597,74 ha; mặt bằng sạch 361,47 ha = 72,29%; Trấn Yên, Cam Đường theo báo cáo chủ đầu tư); 8 điểm vênh giữa báo cáo các Ban và cách viết đã chốt (Y Can/Đông An trước 30/9; Âu Lâu, Minh Quân đã duyệt QHPK; KCN Thống Nhất đã có QHPK 1/2000; Châu Quế TTr 196/TTr-UBND).
- **vbhc-vn 2.27.0:** R17 (WARN) đánh số kép "(1) Một là"/nhiều ý dồn một đoạn; R18 (WARN) đề mục La Mã lẫn tab với thụt dòng đầu; `is_bold` tính đậm kế thừa kiểu đoạn (R11 hết bắt nhầm "KT. GIÁM ĐỐC" kiểu Heading 1); 2 file lỗi nhân tạo mới trong tests/fail.
- **check_facts.py:** rule `kcn-3-khu-626-24-ha`.

## 22/9/2026 — sd-vlncn-sct-vn 2026.9.22.2: kinh nghiệm kiểm tra chuyên đề VLNCN của Cục ATMT (CV 1994/ATMT-ATKV ngày 17/9/2026)

- Nguồn: CV 1994/ATMT-ATKV ngày 17/9/2026 của Cục Kỹ thuật an toàn và Môi trường công nghiệp (Bộ Công Thương), Cục trưởng Phạm Tuấn Anh ký, gửi Công ty Công nghiệp hóa chất mỏ Tây Bắc — nơi nhận có SCT tỉnh Lào Cai.
- ref 05 thêm mục G: chuỗi mốc kiểm tra chuyên đề cấp Bộ đặt cạnh chuỗi 6 bước của Sở (QĐ 338/QĐ-BCT 25/02/2026 → QĐ 154/QĐ-ATMT 07/8/2026 → kiểm tra 10–11/9 → báo cáo 15/9 → CV 17/9); mẫu văn bản kết luận khi đơn vị không có vi phạm; 04 yêu cầu sau kiểm tra, nhấn yêu cầu doanh nghiệp tự kiểm tra theo tầng có thời hạn khắc phục và phúc tra.
- ⚠️ Bẫy viện dẫn: CV 1994 dẫn "Điều 45 Luật Quản lý, sử dụng vũ khí, vật liệu nổ và công cụ hỗ trợ" nhưng Điều 45 hiện hành là thủ tục cấp GP kinh doanh tiền chất thuốc nổ; điều đúng nội dung là Điều 42 (trách nhiệm của tổ chức, doanh nghiệp trong quản lý, sử dụng VLNCN; lưu trữ sổ sách, chứng từ 10 năm).
- Bổ sung một dòng hỏi về hồ sơ tự kiểm tra nội bộ vào checklist kiểm tra hiện trường.

