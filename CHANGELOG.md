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

