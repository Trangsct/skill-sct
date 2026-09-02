---
name: xp-sct-vn
description: "XỬ PHẠT VPHC và KIỂM TRA CHUYÊN NGÀNH đa lĩnh vực, Sở Công Thương Lào Cai. Kích hoạt: xử phạt, mức phạt, thời hiệu, biên bản VPHC, QĐ-XPHC, tước giấy phép, đình chỉ, chuyển hồ sơ, kiến nghị xử lý, thẩm quyền Giám đốc Sở, Trưởng đoàn kiểm tra, QĐ kiểm tra Mẫu 03, kế hoạch kiểm tra, biên bản kiểm tra, báo cáo kết quả, kiểm tra sau kết luận thanh tra, báo cáo thực hiện KLTT. Trục: Luật XLVPHC (sđ 2020, 2025), NĐ 118/2021, NĐ 189/2025 + NĐ 311/2026, NĐ 217/2025, TT 56/2025. Nhánh: hóa chất + VLNCN (NĐ 275/2026, NĐ 71/2019 — Sở XỬ); kho VLNCN, thiết kế kho; vận chuyển HHNH (NĐ 168/2024 giao thông, NĐ 106/2025 PCCC); CCN (NĐ 122/2021 + 288/2026 đầu tư, NĐ 16/2022 xây dựng, NĐ 123/2024 + 281/2026 đất đai, NĐ 45/2022 môi trường); PCCC ngành CT; khoáng sản NĐ 36/2020; ATTP NĐ 115/2018; ATVSLĐ NĐ 283/2026; điện lực NĐ 133/2026; xăng dầu NĐ 99/2020; QLTT NĐ 98/2020. Kèm 12 mẫu văn bản, 8 checklist kiểm tra, hồ sơ mẫu thật (Khí công nghiệp, HCM Tây Bắc, KL 45, KL 48)."
---

# xp-sct-vn — Xử phạt VPHC và kiểm tra chuyên ngành đa lĩnh vực (Sở Công Thương Lào Cai)

Plugin **trục – nhánh**: trục là thủ tục chung theo Luật XLVPHC + quy trình kiểm tra NĐ 217/2025 – TT 56/2025 (dùng cho mọi lĩnh vực); mỗi nhánh trả lời *hành vi – điều khoản – mức – ai phạt – Sở XỬ hay CHUYỂN*. Kế thừa toàn bộ plugin `xp-hc-vlncn-sct-vn` (giữ nguyên trong `references/01-vlncn-hoachat/`); plugin cũ vẫn dùng song song cho đến khi Bạn quyết định gỡ.

## I. ĐỊNH TUYẾN — đọc file nào

| Câu hỏi / việc | Đọc |
|---|---|
| Thời hiệu, thời hạn lập biên bản – giải trình – ra QĐ – nộp phạt, tình tiết tăng nặng/giảm nhẹ, mức trung bình khung, giao quyền, nhiều hành vi nhiều ngành, hình sự, hồ sơ | `references/00-phan-chung-luat-xlvphc.md` |
| Hóa chất, VLNCN, tiền chất: hành vi – mức – thẩm quyền – chuyển tiếp 25/8/2026 – đối chiếu NĐ 71/2019 – phân định NĐ 282/2025 | `references/01-vlncn-hoachat/01…06` |
| **Quy trình kiểm tra chuyên ngành** (Mẫu 03–08 TT 56), kiểm tra sau kết luận thanh tra, thể thức chuẩn của Sở, 7 quyết định biên tập kế hoạch | `references/01-vlncn-hoachat/07-quy-trinh-kiem-tra-chuyen-nganh-tt56.md` — **áp dụng cho mọi lĩnh vực** |
| Vận chuyển HHNH: nghị định nào (giao thông, hóa chất, PCCC, hàng hóa), Sở phạt được phần nào, thu hồi GP | `references/02-hhnh-van-chuyen.md` |
| CCN: chủ đầu tư hạ tầng / thứ cấp vi phạm đầu tư, xây dựng, đất đai, môi trường, PCCC → chuyển ai; 3 công cụ mạnh hơn phạt | `references/03-ccn-dau-tu-xay-dung-dat-dai.md` |
| PCCC cơ sở SXCN: 4 việc của Sở, điểm g–h Đ13 NĐ 105, chế tài NĐ 106/2025 | `references/04-pccc-nganh-cong-thuong.md` |
| Kho VLNCN, thiết kế kho: đứng trước tồn tại X → điểm-khoản-điều nào, bẫy tố tụng | `references/05-kho-vlncn-thiet-ke-hanh-vi.md` |
| Khoáng sản, môi trường: nhận diện – chuyển hồ sơ; cách viết công văn chuyển; tiền lệ KL 45, KL 48 | `references/06-khoang-san-moi-truong-chuyen-ho-so.md` |
| ATTP, ATVSLĐ, điện lực, xăng dầu – LPG, thương mại/QLTT | `references/07-attp-atvsld-dien-xangdau.md` |
| **Đối chiếu bản gốc 8 nhánh** (điện lực, xăng dầu – khí, thương mại, khoáng sản, môi trường, đất đai, xây dựng, đầu tư): thời hiệu, mức, hành vi, ai lập biên bản, ai phạt; bảng "Sở lập BB được không / xử được không" | `references/09-doi-chieu-ban-goc-cac-nhanh.md` |
| **Ai phạt đến bao nhiêu** theo chức danh (NĐ 189/2025 + 311/2026 bản gốc): xã 50%, GĐ sở 80%, QLTT 30/50%; Điều 21 chuyển tiếp; Trưởng đoàn kiểm tra của Sở không có thẩm quyền | `references/08-tham-quyen-chuc-danh-nd189-nd311.md` |
| Tra nhanh 18 lĩnh vực → nghị định → thời hiệu → ai phạt → XỬ/CHUYỂN; việc còn nợ | `references/90-ma-tran-linh-vuc-nghi-dinh-tham-quyen.md` |
| Soạn văn bản: QĐ kiểm tra, KH, TB, BB công bố, BB kiểm tra, BB VPHC, QĐ-XPHC, BC kết quả, CV chuyển hồ sơ, TTr UBND tỉnh, QĐ tạm dừng/đình chỉ, BC thực hiện KLTT | `mau-van-ban/00-README-quy-uoc.md` → mẫu 01–12 |
| Khung kiểm tra theo lĩnh vực (nội dung – căn cứ – hành vi – XỬ/CHUYỂN) | `checklists/00-README.md` → 01–08 |
| Bản gốc nghị định, thông tư | `van-ban-goc/INDEX.md` |
| Hồ sơ mẫu thật | `vi-du-thuc-te/` (Khí công nghiệp — đã ký; HCM Tây Bắc — sau KL 48; KL 45 Viglacera) |

## II. VĂN BẢN LÕI

1. **Luật XLVPHC** 15/2012 (sđ Luật 67/2020, **Luật 88/2025** — hiệu lực 01/7/2025; VBHN 63/VBHN-VPQH 2025). Viện dẫn: *"Luật Xử lý vi phạm hành chính (sửa đổi, bổ sung năm 2020 và năm 2025)"*.
2. **NĐ 118/2021** (sđ NĐ 68/2025, NĐ 190/2025) — mẫu biên bản số 01, mẫu quyết định số 02, xử phạt điện tử.
3. **NĐ 189/2025** (bản gốc `van-ban-goc/chung/`): Chủ tịch xã 50%, **GĐ sở 80%**, tỉnh 100%; Điều 21 chuyển tiếp thay mức cũ; **sửa bởi NĐ 311/2026 ngày 06/8/2026 — hiệu lực 26/9/2026** (Chánh Thanh tra tỉnh cùng nhóm GĐ sở; không dẫn NĐ 311 trong QĐ ký trước 26/9/2026) — `references/08`.
4. **NĐ 217/2025 + TT 56/2025/TT-BCT** — kiểm tra chuyên ngành; **TT 56 chỉ có 01 mẫu biên bản (Mẫu 05)**.
5. **NĐ 275/2026** (hóa chất + VLNCN, hiệu lực 25/8/2026; NĐ 71/2019 cho hành vi kết thúc trước mốc) — bản gốc trong `van-ban-goc/`; GĐ Sở đích danh Đ63.
6. **NĐ 106/2025** (PCCC, hiệu lực 01/7/2025) — bản gốc `van-ban-goc/pccc/`, bảng hành vi ref 04 mục B.
7. **Đã có bản gốc, đối chiếu xong**: NĐ 168/2024 (giao thông — Sở không lập BB, Đ46); NĐ 283/2026 (lao động — **hiệu lực 10/9/2026**, trước đó NĐ 12/2022; Sở không lập BB, Đ54); NĐ 115/2018 + NĐ 124/2021 (ATTP — công chức Sở lập BB k2 Đ27; "Chánh TT Sở CT" 50 tr → GĐ Sở 80 tr theo k2 Đ21 NĐ 189).
8. **Đã có bản gốc, đối chiếu xong (ref 09)**: NĐ 133/2026 (điện — GĐ Sở 80/160 tr, Đ25); NĐ 99/2020 (xăng dầu, khí — mức tổ chức, Sở lập BB k2 Đ55); NĐ 98/2020 + 24/2025 (QLTT); **NĐ 36/2020 (khoáng sản — Đ65: thanh tra CT xử Đ36, 38, 39, 55–62)**; **NĐ 45/2022 (môi trường — Đ68: Sở CT chỉ Đ45, 46)**; NĐ 123/2024 + 281/2026 (đất đai — xã 250 tr; Sở không lập BB); NĐ 16/2022 (xây dựng — k4 Đ72 lập BB); NĐ 122/2021 + 288/2026 (**đầu tư thời hiệu 01 năm**; k4 Đ79 lập BB). **Văn bản sửa đổi đã đối chiếu (v1.3.0)**: NĐ 17/2022 (NĐ 98, 99: Đ56/61/62/63, Đ80/82/87 viết lại — Chánh TT Sở CT đích danh k2 Đ62 NĐ 99), NĐ 04/2022 (NĐ 36: Đ65 thêm Đ48; Đ5b thời hiệu 02 năm; Đ38 k3 mở rộng). Không còn nhánh "chưa hợp nhất". NĐ 16/2022 (dự thảo thay); NĐ 123/2024 + 281/2026; NĐ 45/2022 (dự thảo thay); NĐ 36/2020 + 04/2022 (dự thảo thay); NĐ 115/2018 + 124/2021; NĐ 283/2026; NĐ 133/2026; NĐ 99/2020 + 17/2022; NĐ 98/2020 + 24/2025; NĐ 282/2025.
9. **QĐ 05/2025/QĐ-UBND** (chức năng Sở); **QĐ 1094/QĐ-SCT 09/3/2026** (giao quyền xử phạt PGĐ).

## III. QUY TẮC CHỐT (không suy đoán lại)

- **Thời hiệu**: hóa chất, VLNCN, HHNH, PCCC, lao động, ATTP, điện = **01 năm**; đất đai, xây dựng, môi trường, khoáng sản, hàng hóa, đầu tư = **02 năm** (Điều 6 Luật sđ 88/2025). Lĩnh vực theo **nghị định điều chỉnh hành vi**. Hành vi "không thực hiện nghĩa vụ" đang tồn tại = đang thực hiện → tính từ ngày phát hiện. Hết thời hiệu → điểm c khoản 1 Điều 65: không lập BB VPHC, không ra QĐ.
- **XỬ / CHUYỂN** — 3 câu hỏi (`references/90`): (1) hành vi thuộc nghị định nào; (2) nghị định/NĐ 189+311 có trao thẩm quyền cho GĐ Sở hoặc QLTT không; (3) mức tổ chức và hình thức bổ sung có vượt trần GĐ Sở không. Sở tự phạt: hóa chất, VLNCN (kho, sử dụng, huấn luyện), hóa chất trong vận chuyển, điện lực (Đ25 NĐ 133), ATTP ngành CT (qua Đ21 NĐ 189), xăng dầu – khí và hàng hóa qua QLTT, **khoáng sản phần thiết kế mỏ – GĐĐH mỏ – KTAT khai thác (Đ36, 38, 39, 48, 55–62 NĐ 36/2020 qua Đ65; lập BB theo QĐ 5116/QĐ-SCT 20/8/2026)**, môi trường chỉ Đ45–46 NĐ 45/2022. **Chức danh "Chánh Thanh tra Sở CT" trong nghị định cũ → Giám đốc Sở, phạt đến 80% trần lĩnh vực (k2 Đ6 + k2 Đ21 NĐ 189 — Bạn chốt 02/9/2026, ref 09 mục K).** Sở **không** ra QĐ phạt: giao thông, PCCC, ANTT, đầu tư, xây dựng, đất đai, môi trường, khoáng sản, lao động → chuyển bằng `mau-van-ban/09`, luôn yêu cầu "thông báo kết quả về Sở". **Riêng PCCC**: công chức Sở (CQCM về xây dựng) **được lập BB VPHC** theo k2 Đ29 NĐ 106/2025 → lập rồi chuyển Chủ tịch UBND tỉnh/Công an trong 24h.
- **Thể thức**: bám hồ sơ đã ban hành trong `vi-du-thuc-te/` trước mọi suy luận từ mẫu trong thông tư; khối ký Đoàn "TM. ĐOÀN KIỂM TRA / TRƯỞNG ĐOÀN"; BB VPHC 01 người lập, đủ 10 mục; QĐ-XPHC đủ 12 dòng căn cứ gồm Điều 57, 68, 70, 78, 85 Luật và QĐ 1094; mức = trung bình khung tổ chức; "10 ngày làm việc" cho thời hạn kiểm tra theo cách Sở đã thống nhất.
- **Kiểm tra sau kết luận thanh tra** (KL 48, KL 45): KLTT không thay biên bản VPHC; lập đoàn kiểm tra riêng đối tượng bên thứ ba; không "kiểm tra lại" nội dung đã kết luận; dẫn chiếu đúng mục/trang KLTT; thời hiệu chạy song song. Sở nằm trong bảng trách nhiệm KLTT → báo cáo theo Điều 54 Luật Thanh tra 2025 bằng `mau-van-ban/12`.
- **Chuyển tiếp 25/8/2026** (hóa chất, VLNCN): hành vi kết thúc trước → NĐ 71/2019; đang diễn ra/sau → NĐ 275/2026 (k1 Đ74); khiếu nại QĐ cũ → quy định thời điểm ban hành.
- **GATE bản gốc**: chỉ ghi điểm-khoản-điều vào biên bản/QĐ khi đã đối chiếu bản gốc trong `van-ban-goc/` hoặc vbpl.vn; chưa có → mô tả hành vi + "xử lý theo quy định pháp luật về xử phạt VPHC trong lĩnh vực …". Không bịa số/ngày văn bản; không tự điền số QĐ chưa ban hành.

## IV. QUY TRÌNH CHUẨN MỘT VỤ VIỆC (mọi lĩnh vực)

```
Phát hiện (kế hoạch / đột xuất / chỉ đạo / KLTT)
→ QĐ kiểm tra (Mẫu 01)  → KH kiểm tra (02, người ra QĐ duyệt) → TB Điều 7 trong 3 ngày LV (03)
→ Công bố (04) → Kiểm tra theo checklist lĩnh vực → BB kiểm tra Mẫu 05 (05) + Phụ lục hồ sơ
   + mục 4.5 xác định hành vi – thời hiệu – thẩm quyền
→ Rẽ nhánh từng hành vi:
   a) còn thời hiệu, thuộc Sở → BB VPHC (06) trong 2 ngày LV → giải trình 2/5 ngày LV
      → QĐ-XPHC (07) trong 7 ngày LV (GĐ hoặc PGĐ theo QĐ 1094) → giao QĐ 2 ngày LV → nộp 10 ngày
   b) vượt thẩm quyền → BB VPHC + TTr Chủ tịch UBND tỉnh (10) trong 10 ngày LV
   c) thuộc cơ quan khác → CV chuyển hồ sơ (09) trong 24 giờ (nếu đã lập BB) / ngay sau kiểm tra
   d) hết thời hiệu → ghi nhận, không BB VPHC; khắc phục hậu quả nếu cần (k2 Đ65)
   e) dấu hiệu tội phạm → chuyển cơ quan điều tra trước (Đ62)
→ BC kết quả Mẫu 06 (08) ≤ 10 ngày LV → văn bản nhận xét của người ra QĐ ≤ 15 ngày
→ Theo dõi thi hành, khắc phục; cưỡng chế; [BC thực hiện KLTT (12)]; lưu HSKT
```
Thời hạn chi tiết: `references/00` mục C. Trùng thanh tra/kiểm toán → tạm dừng/đình chỉ (Mẫu 11).

## V. LIÊN KẾT PLUGIN

- Nghĩa vụ gốc, điều kiện, cấp phép, kỹ thuật: `sd-vlncn-sct-vn`, `kho-vlncn-sct-vn`, `hl-vlncn-sct-vn`, `hc-sct-vn`, `hnh-sct-vn`, `kccn-sct-vn`, `xd-sct-vn`, `pccc-sct-vn`, `qlks-sct-vn`, `tkm-sct-vn`, `bvmt-sct-vn`, `attp-sct-vn`. Plugin này chỉ lo chế tài + quy trình kiểm tra dẫn tới chế tài.
- Soạn/render docx: `vbhc-vn`; người ký, dòng Lưu, phân công phòng: `sct-laocai-org-vn`; đọc PDF văn bản đến/KLTT: `vbhc-pdf-reader-vn`.
- Các plugin `hnh-sct-vn` (đang trỏ `xlvphc-sct-vn`), `qlks-sct-vn/08`, `bvmt-sct-vn/06`, `pccc-sct-vn` cần sửa trỏ về `xp-sct-vn` ở phiên sau.

## VI. CẤU TRÚC

```
xp-sct-vn/skills/xp-sct-vn/
├── SKILL.md
├── CHANGELOG.md, CHANGELOG-v2026.09.01.md
├── references/
│   ├── 00-phan-chung-luat-xlvphc.md
│   ├── 01-vlncn-hoachat/ (01–07 kế thừa xp-hc-vlncn-sct-vn v1.6.0; 07 = quy trình kiểm tra dùng chung)
│   ├── 02-hhnh-van-chuyen.md · 03-ccn-dau-tu-xay-dung-dat-dai.md · 04-pccc-nganh-cong-thuong.md
│   ├── 05-kho-vlncn-thiet-ke-hanh-vi.md · 06-khoang-san-moi-truong-chuyen-ho-so.md
│   ├── 07-attp-atvsld-dien-xangdau.md · 08-tham-quyen-chuc-danh-nd189-nd311.md · 09-doi-chieu-ban-goc-cac-nhanh.md · 90-ma-tran-linh-vuc-nghi-dinh-tham-quyen.md
├── mau-van-ban/ 00-README + 01–12
├── checklists/ 00-README + 01–08
├── vi-du-thuc-te/ (Khí công nghiệp mẫu thật 7 file; HCM Tây Bắc 10 file; KL 45 Viglacera; KH PGĐ duyệt)
└── van-ban-goc/ (NĐ 275/2026, NĐ 282/2025, TT 56/2025, VBHN 78/2026; chung/ 189+311; pccc/ 106; giao-thong/ 168; lao-dong/ 283; attp/ 115+124; dien-luc/ 133; xang-dau-khi/ 99; thuong-mai/ 98+24; khoang-san/ 36+04/2022; chung/ +17/2022; moi-truong/ 45; dat-dai/ 123+281; xay-dung/ 16; dau-tu/ 122+288 + INDEX)
```
