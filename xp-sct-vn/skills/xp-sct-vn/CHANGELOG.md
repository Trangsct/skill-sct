# CHANGELOG — xp-sct-vn

## 1.5.0 — 05/9/2026
NQ 66.25/2026/NQ-CP (04/9/2026, hiệu lực 15/9/2026): thẩm quyền xử phạt khoáng sản NĐ 36/2020 (21 điều) và k3 Đ6 NĐ 189/2025 chuyển sang ngành Công Thương — ref 06 mục A GATE mới; xem CHANGELOG-v2026.09.05.md.

## 1.4.2 — 02/9/2026
- Ref 07 mục ATVSLĐ trỏ sang plugin mới `atvsld-sct-vn`.

## 1.4.1 — 02/9/2026
- Rút description plugin.json về ≤500 ký tự (1.4.0 để 561, vi phạm giới hạn CI).

## 1.4.0 — 02/9/2026
## Việc 4: nạp Luật 88/2025, NĐ 118/2021 + Phụ lục biểu mẫu vào trục chung
- **Bản gốc mới (`van-ban-goc/chung/`)**: Luật 88/2025/QH15 (docx + scan có dấu 18 trang), NĐ 118/2021/NĐ-CP bản gốc (chưa hợp nhất NĐ 68/2025, 190/2025), Phụ lục biểu mẫu NĐ 118 (42 mẫu MQĐ, 30 mẫu MBB).
- **Reference 10 mới** — đối chiếu nguyên văn theo điều, khoản: thời hiệu Đ6 (danh mục 02 năm gồm khoáng sản, môi trường, đất đai, xây dựng, kinh doanh hàng hóa/hàng giả; điểm c mới kéo dài 01 năm khi tố tụng chuyển đến); trần Đ24 (điểm đ 100 tr: thương mại, quản lý vật liệu nổ, điện lực; điểm i 500 tr: xây dựng, đất đai; k3 ATTP/CLSPHH theo luật riêng); **Đ37a điểm c: Giám đốc Sở là chức danh xử phạt theo Luật; Đ53 k2: chức danh tiếp nhận nhiệm vụ thực hiện thẩm quyền** (căn cứ luật cho chuyển đổi Chánh TT Sở → GĐ Sở, bổ sung vào ref 08 và ref 09 K.1); Đ54 giao cấp phó (MQĐ34); Đ56 không lập BB (500 nghìn/1 tr); Đ58 k1/k3b/k5 + Đ12 NĐ 118 (02/05/03 ngày làm việc); Đ59 người lập BB được xác minh; Đ60 hội đồng định giá ≤05 ngày làm việc; Đ62/63 "05 ngày làm việc"; **Đ70 gửi QĐ 03 ngày làm việc, thêm điện tử + niêm yết**; Đ71; Đ87 cưỡng chế + giao cấp phó (MQĐ35); Đ125 k4 tạm giữ cùng lúc lập BB VPHC không cần biên bản tạm giữ, 24 giờ báo cáo; Đ126; bãi bỏ Đ38–49, 51; Điều 2, 3 chuyển tiếp; danh mục biểu mẫu Sở hay dùng.
- **Ref 00 sửa 3 điểm ghi theo luật cũ**: gửi QĐ xử phạt 02 → **03 ngày làm việc** (Đ70 mới); chuyển biên bản "24 giờ" → **"kịp thời"** (k5 Đ58 mới); GATE Điều 66 → Điều 66 không bị sửa, giữ 07/10 ngày làm việc và 01/02 tháng. Dòng lập BB VPHC ghi đủ 02/05/03 ngày làm việc theo k2 Đ12 NĐ 118.
- **Ref 09 K.1**: bổ sung trần theo Đ24 mới (thương mại, VLNCN, điện lực 100 tr → GĐ Sở 80/160 tr; VLNCN đối chiếu thêm Đ63 NĐ 275/2026).
- **Mẫu 13 mới**: QĐ giao nhiệm vụ lập biên bản VPHC theo lĩnh vực (khuôn QĐ 5116), biến thể môi trường Đ45–46 NĐ 45/2022 và xăng dầu – khí; mỗi lĩnh vực một quyết định.
- INDEX, SKILL.md (định tuyến + cây thư mục), README mẫu cập nhật. Còn thiếu: NĐ 68/2025, NĐ 190/2025 (hợp nhất NĐ 118), VBHN 63/VBHN-VPQH.

## [1.3.3] - 02/9/2026 — sửa theo scripts/check_facts.py (CI dữ kiện lỗi thời)
- Sửa các vi phạm do scripts/check_facts.py quét: nơi nộp hồ sơ → motcua-tthc.moit.gov.vn; tiêu ngữ en dash trong mẫu; trỏ xp-hc-vlncn-sct-vn → xp-sct-vn; CN(M.Cường) trong mẫu → CN(Khôi), trong ví dụ lịch sử chú thích "lịch sử"; ký hiệu /GP-SCT bỏ chữ "dự kiến". Không đổi nghiệp vụ.

## 1.3.2 — 02/9/2026
- Sửa lỗi đọc số văn bản: QĐ 5116/QĐ-SCT ngày 20/8/2026 là **bản ký số đầy đủ** (2 trường /Sig), không phải "bản dự thảo chưa điền số" như ghi tại 1.3.1 — lỗi do không chạy `extract_metadata.py` mà tin lớp text trong context. Đổi tên file bản gốc `_ban-ky-so.pdf`, bỏ ảnh chụp Data360X (không còn cần làm chứng cứ số/ngày), sửa ref 09 K.2, INDEX.
- SKILL.md thêm **mục 0 GATE PDF** ngay trên mục định tuyến: chạy script trước mọi việc; context trống số/ngày = PDF ký số, cấm kết luận "dự thảo".

## 1.3.1 — 02/9/2026
Bạn chốt hai điểm treo từ v1.2.0 (ghi tại `references/09` mục K mới):
1. **Chuyển đổi chức danh "Chánh Thanh tra Sở Công Thương" → Giám đốc Sở** theo k2 Đ21 NĐ 189/2025; thẩm quyền theo k2 Đ6 NĐ 189 (nguyên văn đã đối chiếu: phạt đến 80% mức tối đa lĩnh vực tại Điều 24 Luật; tước GP/đình chỉ; tịch thu; khắc phục k1 Đ28 Luật). Mức: khoáng sản 800 tr CN / 1,6 tỷ TC (trần 1 tỷ theo k1 Đ4 NĐ 36); môi trường Đ45–46: 800 tr / 1,6 tỷ; xăng dầu – khí 80/160 tr. Áp dụng cho k2 Đ65 NĐ 36, k4 Đ64 NĐ 45, k2 Đ62 NĐ 99, k2 Đ87 NĐ 98, k2 Đ29 NĐ 115. Ref 08 mục D.6 gỡ điều kiện "phải có ý kiến Sở Tư pháp trước".
2. **Tư cách người lập biên bản VPHC khoáng sản: QĐ 5116/QĐ-SCT ngày 20/8/2026** (GĐ Hoàng Chí Hiền ký; PTP phụ trách khoáng sản + CV QLCN; hành vi thuộc thẩm quyền GĐ Sở; k1 Đ58 Luật, k1 Đ12 NĐ 118). Bản gốc ký số lưu `van-ban-goc/khoang-san/` (số/ngày đọc bằng extract_metadata.py — ban đầu ghi nhầm là "bản dự thảo" do không chạy script, sửa tại 1.3.2). Bảng I ref 09: NĐ 36 "chưa chắc" → CÓ. Hành vi ngoài Đ65 (Đ37, 40, 41, 47, 49) QĐ 5116 không trao quyền → chỉ biên bản kiểm tra, chuyển SNNMT.

Cập nhật: ref 09 (mục K, D, bảng I), 08 (D.6), 06, 90 (dòng 11), checklist 08, INDEX, SKILL.md quy tắc XỬ/CHUYỂN. Lưu ý rà khi trích dẫn QĐ 5116: căn cứ chưa ghi NĐ 04/2022; cụm "NĐ 190/2025 ngày 01/7/2025 sửa NĐ 68/2025 ngày 13/8/2025" có ngày ngược — kiểm tra lại số/ngày.

## 1.3.0 — 02/9/2026
Bạn cung cấp lại 3 bản gốc (phiên 01/9 bị tạm dừng khi đang đọc): **NĐ 04/2022/NĐ-CP** (06/01/2022, sửa NĐ 36/2020 — 36 khoản) → `van-ban-goc/khoang-san/`; **NĐ 17/2022/NĐ-CP** (31/01/2022, sửa NĐ 71/2019, 134/2013, 98/2020 — 52 khoản, 99/2020 — 20 khoản) → `van-ban-goc/chung/`; NĐ 24/2025 (đã có). Hết tình trạng "bản gốc chưa hợp nhất" ở 3 nhánh B, C, D của ref 09.

Nội dung đối chiếu nguyên văn đưa vào `references/09` (tiểu mục "Sửa đổi bởi …" dưới từng bảng B, C, D):
1. **NĐ 99/2020 (xăng dầu, khí) sau NĐ 17/2022**: Đ55 lập biên bản KHÔNG sửa; **k2 Đ62 nêu đích danh "Chánh Thanh tra Sở Công Thương" 50/100 tr, tước GP, đình chỉ**; **k7 Đ63 mới: thanh tra chuyên ngành Công Thương xử mọi hành vi của Nghị định theo Đ62**; Đ56 (xã 5/10; huyện 100/200 Chương II, 50/100 khác), Đ61 QLTT viết lại; bãi bỏ điểm a k3 Đ39 và điểm a k5 Đ40 (không dẫn nữa); Đ4a/4b mới (vi phạm nhiều lần, số lợi bất hợp pháp); điểm g k3 Đ4 buộc nộp lại GP bị tẩy xóa.
2. **NĐ 98/2020 (thương mại) sau NĐ 17/2022 + NĐ 24/2025**: k2 Đ80 danh sách người lập biên bản = công chức cơ quan Đ81–87a (thêm UB Cạnh tranh QG) — QLCN vẫn không có; Đ82 QLTT (Đội trưởng 25 tr; Chi cục trưởng 50 tr, tước GP); Đ87 Chánh TT sở 50 tr; Đ87a, k6a Đ88; NĐ 24/2025 chỉ sửa tiếp phần biện pháp khắc phục Đ78, 81–88.
3. **NĐ 36/2020 (khoáng sản) sau NĐ 04/2022**: **Đ65 mới thêm Điều 48** (cát sỏi không GP) vào phạm vi thanh tra công thương, k2 giữ 50 tr + tước GP/đình chỉ 01–24 tháng; **Đ5b: thời hiệu khoáng sản 02 năm** + danh mục hành vi đã kết thúc (gồm k3 Đ38, điểm b k1 Đ39); k1 Đ5 mức cá nhân, tổ chức ×2, hộ KD như cá nhân; **Đ38 k3 mở rộng** (vượt 10% chiều cao tầng/góc dốc sườn tầng; đổ thải sai vị trí thiết kế; khung thời gian; thiết bị) với mức mới điểm b 20–30, d 50–70 tr, k4 d 100–200 tr; Đ36 k4/4a chậm báo cáo 30–50 / 50–60 tr; Đ37 thêm tiêu chí độ sâu/độ cao; Đ40 ngoại lệ trạm cân; Đ41 bãi bỏ k1, mức mới; Đ48 mới; Đ64 huyện 100 tr; k1 Đ69 dẫn Đ58 Luật (k2 không sửa); Đ39, Đ55–62 không sửa.

Cập nhật: ref 09 (intro, B, C, D, bảng I), ref 90 (dòng 11, 15, 16, checklist bản gốc), ref 06, ref 07, INDEX, SKILL.md mục II.8 và cây thư mục. Kết luận nghiệp vụ không đảo chiều so với v1.2.0; căn cứ chắc hơn ở 2 điểm: Chánh TT Sở CT được nêu đích danh trong NĐ 99 (k2 Đ62 bản NĐ 17/2022) và phạm vi Đ65 NĐ 36 gồm Đ48.

## 1.2.0 — 01/9/2026
Bạn cung cấp 11 bản gốc: NĐ 133/2026, 99/2020, 98/2020, 24/2025, 36/2020, 45/2022, 123/2024, 281/2026, 16/2022, 122/2021, 288/2026 → `van-ban-goc/{dien-luc,xang-dau-khi,thuong-mai,khoang-san,moi-truong,dat-dai,xay-dung,dau-tu}/`. Reference mới **09-doi-chieu-ban-goc-cac-nhanh.md** chép nguyên văn thời hiệu, mức, hành vi, thẩm quyền lập biên bản/xử phạt từng nghị định + bảng "Sở lập BB được không / xử được không".

Sửa nhận định sai trước đây:
1. **Đầu tư: thời hiệu 01 năm** (k1 Đ5 NĐ 122/2021), không phải 02 năm. NĐ 288/2026 chỉ sửa phần đăng ký doanh nghiệp (Đ43, 44, 46, 48, 52, 65). k4 Đ79: công chức cơ quan được giao kiểm tra đầu tư lập được biên bản.
2. **Khoáng sản: ngành Công Thương CÓ thẩm quyền xử phạt** — Điều 65 NĐ 36/2020 (Đ36, 38 thiết kế mỏ, 39 GĐĐH mỏ, Mục 2 Chương III Đ55–62 KTAT khai thác; Chánh TT Sở CT 50 tr, đình chỉ khai thác → GĐ Sở qua k2 Đ21 NĐ 189). Ranh giới Đ37, công suất Đ41, trạm cân Đ40 vẫn chuyển SNNMT.
3. **Môi trường: Sở CT chỉ xử Đ45 (KNK), Đ46 (ô-dôn)** — Đ64, Đ68 NĐ 45/2022; k3 Đ15 hạ tầng CCN chép nguyên văn.
4. **Điện lực NĐ 133/2026**: Đ25 GĐ Sở CT 80/160 tr đích danh; k2 Đ23 công chức Sở lập BB; thời hiệu 01 năm (phát điện, XNK, mua bán 02 năm); không có tước GP.
5. **Xăng dầu, khí NĐ 99/2020**: mức ghi là mức TỔ CHỨC (Đ5); k2 Đ55 công chức Sở lập BB; k2 Đ62 Chánh TT sở 50/100 tr → GĐ Sở; QLTT Đ61.
6. **Thương mại NĐ 98/2020 + 24/2025**: công chức QLCN không lập BB (Đ80); QLTT Đ82.
7. **Đất đai NĐ 281/2026 (hiệu lực 31/8/2026)**: xã 250 tr, GĐ Sở NN&MT 400 tr; Sở CT không lập BB (k2b Đ32).
8. **Xây dựng NĐ 16/2022**: mức tổ chức; k7c Đ16 không GPXD 120–140 tr; k8 sai thiết kế thẩm định 80–100 tr; k4 Đ72 công chức được phân công kiểm tra hoạt động xây dựng lập được BB.

Cập nhật: ref 03, 06, 07, 08 (mục D.6), 90; checklist 05, 08; INDEX; SKILL.md. Ba bản gốc chưa hợp nhất (NĐ 99, 98, 36) — cần NĐ 17/2022, NĐ 04/2022.

## 1.1.1 — 01/9/2026
- **NĐ 124/2021/NĐ-CP** (Bạn cung cấp) → `van-ban-goc/attp/`. Đối chiếu 22 khoản Điều 1 sửa NĐ 115/2018 vào ref 07 và checklist 07: k2 Đ3 mở rộng danh mục mức tổ chức (thêm k6 Đ9, điểm a k3 Đ20, k1 Đ21; cá nhân giảm một nửa; tới 7 lần giá trị thực phẩm với k1 Đ4, k1 Đ22, k6 Đ26); **Đ18 k1, k2 thêm "GCN đã hết hiệu lực"**; Đ9: k3đ người trực tiếp / k5d chủ cơ sở **không có giấy xác nhận tập huấn kiến thức ATTP** (5–7 / 10–15 tr), k7a bệnh truyền nhiễm, k7b nước không đạt; Đ20 k1b Hệ thống dữ liệu ATTP, k2e phiếu kiểm nghiệm hết hạn; Đ21 k1 30–40 tr (mức TC); Đ29 k3 Trưởng đoàn thanh tra chuyên ngành cấp sở (Sở CT) cùng mức Chánh Thanh tra Sở; Đ34 QLTT; hiệu lực 01/01/2022, chuyển tiếp có lợi (k2 Đ4).

## 1.1.0 — 01/9/2026
Bạn cung cấp 5 bản gốc: NĐ 189/2025, NĐ 311/2026, NĐ 168/2024, NĐ 283/2026, NĐ 115/2018 → `van-ban-goc/{chung,giao-thong,lao-dong,attp}/`. Đối chiếu nguyên văn, sửa 4 chỗ plugin ghi sai trước đây:

1. **Chủ tịch UBND cấp xã = 50% mức tối đa** (k1 Đ5 NĐ 189), không phải 10%; Giám đốc sở 80% (k2 Đ6); Chi cục trưởng thuộc Sở 50%; Đội trưởng QLTT 30%, Chi cục trưởng QLTT 50% (Đ12). **Điều 21 NĐ 189**: mức của NĐ 189 thay số tiền trong nghị định chuyên ngành ban hành trước (hệ quả: xã PCCC 25 tr thay 5 tr; xã ATTP 50 tr thay 5 tr); chức danh mất ("Chánh Thanh tra Sở") → chức danh tiếp nhận (Giám đốc Sở).
2. **NĐ 311/2026**: Trưởng đoàn kiểm tra của tổ chức thuộc bộ giảm 80% → 50% (k4 Đ1); **không có Trưởng đoàn kiểm tra cấp Sở** ở cả NĐ 189 lẫn 311.
3. **NĐ 283/2026 hiệu lực 10/9/2026** (k1 Đ66) — đến hết 09/9/2026 vẫn NĐ 12/2022; chuyển tiếp Đ67. Sở Công Thương **không có thẩm quyền lập biên bản** (Đ54 chỉ Sở Nội vụ, xã, Bộ Nội vụ, BHXH, Công an, thanh tra). Bảng hành vi Đ32, 35 (không kiểm định theo số thiết bị 20–75 tr), 36 (không huấn luyện theo số người 5–50 tr); thẩm quyền xã 37,5 / tỉnh 75 / GĐ Sở Nội vụ 60 tr.
4. **NĐ 168/2024**: Đ23 lái xe (k5 12–14 tr không GP); **Đ26 đơn vị kinh doanh vận tải** (điểm d k2 không áp tải 2–4 tr TC; điểm d k4 lái xe/áp tải không tập huấn 6–8 tr TC); **Đ46: Sở không được lập biên bản**.
5. **NĐ 115/2018** (bản 2018, chưa hợp nhất NĐ 124/2021): **k2 Đ27 công chức ngành Công Thương được lập biên bản**; Đ29 "Chánh thanh tra Sở Công Thương" 50/100 tr → áp k2 Đ21 NĐ 189 = Giám đốc Sở 80/160 tr (ghi rõ là cách áp dụng, khuyến nghị hỏi Sở Tư pháp trước QĐ đầu); Đ18 k2 không GCN 30–40 tr (mức tổ chức ghi sẵn); Đ20, 21, 9 nguyên văn.

Mới: `references/08-tham-quyen-chuc-danh-nd189-nd311.md` (bảng chức danh, Điều 4, Điều 21, cách áp dụng cho Sở, câu viện dẫn theo ngày ký). Sửa: ref 00, 02, 04, 07 (bảng G đầy đủ), 90; checklist 04, 07; INDEX; SKILL.md.

## 1.0.2 — 01/9/2026
- **NĐ 106/2025/NĐ-CP** (Bạn cung cấp bản gốc docx) → `van-ban-goc/pccc/`. Đối chiếu toàn văn: mức tối đa cá nhân 50 tr (Đ4); thời hiệu 01 năm, mốc riêng cho Đ18 (từ ngày bàn giao / ngày chấm dứt hoạt động — k4 Đ5); chuyển tiếp Đ40.
- **Phát hiện then chốt — khoản 2 Điều 29**: công chức **cơ quan chuyên môn về xây dựng** đang thi hành công vụ có thẩm quyền **lập biên bản VPHC** về PCCC → Đoàn kiểm tra của Sở lập BB VPHC Mẫu 01 rồi chuyển 24h; Giám đốc Sở không có tên tại Đ30–36 nên không ra QĐ (Chủ tịch UBND xã 5 tr, tỉnh 50 tr; Chánh Thanh tra tỉnh 35 tr; Công an Đ31). Sửa từ "kiến nghị" thành "lập BB VPHC → chuyển" tại ref 04, 03, 05, 02, checklist 06, SKILL.md.
- `references/04` mục B viết lại: bảng 30 hành vi thuộc phạm vi Sở phát hiện (Đ14, 15, 16, 18, 23, 24, 25) với mức tổ chức, bổ sung, khắc phục; quy tắc chọn 1 cấu thành khi trùng VLNCN (a k5 Đ57 NĐ 275) – PCCC (a k4/k6 Đ25 NĐ 106).
- `checklists/06`: điền điểm-khoản-điều thay ⚠️; thêm mục D hồ sơ pháp lý PCCC (Đ18) và câu kết luận mẫu có viện dẫn k2 Đ29.
- `references/90`: dòng PCCC → ✅; INDEX bổ sung.

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
