# 20 — Sổ theo dõi cơ sở hoạt động hóa chất, GCN/GP đã cấp trên địa bàn (dựng 06/11/2026)

Nguồn: 3 tệp Bạn gửi 06/11/2026 (bản quét GP, GCN, hồ sơ kiểm tra — OCR), sổ văn bản đi/đến, hồ sơ kiểm tra 2026.
**Bản đầy đủ, luôn mới nằm trên web nội bộ** (`vlncn-laocai.vercel.app`, menu **Hóa chất**: Cơ sở · GP, GCN · Hồ sơ đang xử lý ·
KH, BP sự cố · Huấn luyện · Kiểm tra, xử phạt · Báo cáo của DN · Thống kê · Văn bản) và trong **máy chủ tra cứu MCP**
(`tra_doanh_nghiep`, `tra_van_ban_den_di` — plugin `tra-cuu-sct-vn`). Tệp máy đọc kèm plugin: `data/so-theo-doi-hoa-chat.csv`
(mỗi dòng một cơ sở: hoạt động, hóa chất, GCN/GP, hồ sơ, KH/BP, kiểm tra, xử phạt, báo cáo 2025). Bạn chốt 06/11/2026: sổ này kèm **mã số doanh
nghiệp và địa chỉ cơ sở** (thông tin đăng ký doanh nghiệp là công khai); vẫn KHÔNG ghi số điện thoại, người đại diện, số CCCD —
các chi tiết đó tra trên web nội bộ hoặc bản gốc.

## 1. GATE trước khi trả lời về một doanh nghiệp hóa chất

1. Gọi `tra_doanh_nghiep` (MCP) hoặc mở `data/so-theo-doi-hoa-chat.csv` → biết DN đã có GCN/GP nào, hồ sơ nào đang xử lý, đã kiểm tra, đã báo cáo chưa.
2. Cần toàn văn giấy phép: `tra_van_ban_den_di "47/GCN-SCT"` hoặc plugin `van-ban-sct-vn` `tim.py --xem` (bản chữ OCR của 39 tệp nằm trong sổ văn bản, năm 2018–2026).
3. Chỉ khi cả hai nơi không có mới nói "chưa có trong sổ theo dõi" và hỏi Bạn.

## 2. GCN đủ điều kiện cấp trước 01/01/2026 — còn dùng đến hết 31/12/2027 (khoản 3 Điều 48 Luật 69/2025)

| Doanh nghiệp (cơ sở) | GCN | Phạm vi (theo GCN) |
|---|---|---|
| Hóa chất Đức Giang Lào Cai | 47/GCN-SCT 27/6/2025 (SX và KD); trước đó 02/GCN-SCT 19/12/2019; 07/GCN-SCT 25/4/2023 (chỉ có tên tệp) | Phốt pho vàng 9.800 t/năm (lô B12, B13); 2019: axit sunfuric 400.000 t, axit photphoric trích ly 100.000 t, axit photphoric thực phẩm 20.000 t, natri metasilicat |
| CP Phốt pho Việt Nam | 01/GCN-SCT 13/02/2023 (SX+KD); 1623/GCN-SCT 17/9/2021 (KD) | Phốt pho vàng; KD axit photphoric tại Nhà máy hóa chất Đồng Nai |
| CP Quốc tế Lavita | 02/GCN-SCT 21/02/2023; 10/GCN-SCT 09/5/2024; 45/GCN-SCT 13/6/2025 | Phốt pho đỏ; axit photphoric 6.600 t/năm; KD phốt pho vàng |
| Chi nhánh Luyện đồng Lào Cai - Vimico | 03/GCN-SCT 14/12/2018 (nhà máy số 1); 25/GCN-SCT 27/12/2022 (nhà máy Bản Qua) | Axit sunfuric |
| CP Đông Nam Á Lào Cai | 04/GCN-SCT 23/3/2023 | Phốt pho vàng |
| CP Phốt pho Apatit Việt Nam | 08/GCN-SCT 25/4/2023 | Phốt pho vàng 20.000 t/năm |
| CP Phốt pho vàng Lào Cai | 19/GCN-SCT 17/7/2024 | Phốt pho vàng |
| TNHH Phốt pho vàng Việt Nam | 27/GCN-SCT 07/11/2024 | Phốt pho vàng 19.800 t/năm |
| CP Victory | 21/GCN-SCT 26/3/2025 (KD) | Phốt pho vàng; kho tại nhà máy 10.000 t/năm |
| CP DAP số 2 - Vinachem | 538/GCN-SCT 16/4/2021 | Axit sunfuric, axit photphoric, axit flosilisic (quy mô bản quét mờ) |
| TNHH Khoáng sản và Luyện kim Việt Trung | 878/GCN-SCT 04/6/2021 | Khí oxy — Nhà máy Gang thép |
| TNHH MTV Khí công nghiệp Lào Cai | 02/GCN-SCT 18/6/2020 (KD; báo cáo kiểm tra ghi 17/6/2020) | Oxy, argon — Khu TTCN Bắc Duyên Hải |
| CP XNK Light Logistics | 03/GCN-SCT 20/8/2020 (KD) | Argon 1.000 t/năm (kho tại Bắc Duyên Hải) — xác minh còn hoạt động |
| TNHH Thương mại và Vận tải 69 | 1702/GCN-SCT 14/11/2018 (KD) | Axit sunfuric, kho thuê của DAP số 2 (hợp đồng đến 30/9/2023) |
| TNHH Vật tư và Thiết bị Gia Phát | 26/GCN-SCT 26/8/2022 (KD) | Lưu huỳnh 60.000 t, axit sunfuric 25.000 t/năm; kho thuê DAP số 2 |
| DNTN Nhung Thắng LPG | 2888/GCN-SCT 14/12/2021 (Sở CT Yên Bái cũ) | Bảng hóa chất chưa đọc được từ bản quét |
| DNTN Việt Phong | 48/GCN-SCT 02/10/2019 (Sở CT Yên Bái cũ) | Bảng hóa chất chưa đọc được từ bản quét |

Bài học: **mọi GCN cũ hết hiệu lực 31/12/2027** — khi DN thay đổi ĐKDN mà không cấp lại GCN là vi phạm (vụ Khí công nghiệp Lào Cai, mục 4); từ nay hướng dẫn DN lập hồ sơ GCN mới theo Điều 9 NĐ 26/2026 trước hạn.

## 3. GP cấp theo khung 2026 (đến 06/11/2026)

- **GP nhập khẩu hóa chất cần kiểm soát đặc biệt nhóm 1 — UBND tỉnh cấp, 06 tháng, theo từng hóa đơn** (PCT Nguyễn Thành Sinh ký): 3384/GP-UBND 18/9/2026 Trần Bình - Yên Bái (methanol 4.960 kg + adhesive resin 2.700 kg); 3385/GP-UBND 18/9/2026 Dafu Stone (88.000 kg UPR chứa 30% styrene); 3387/GP-UBND 18/9/2026 Đá trắng Bảo Lai (66.000 kg UPR, styrene 25–45%; thân GP in "18/8" — lỗi); 3509/GP-UBND 28/9/2026 Polyfill Yên Bái (maleic anhydride 20.000 kg); 3510/GP-UBND 28/9/2026 Đạt Phương (methanol 7.200 kg + adhesive resin 3.420 kg). Hồ sơ lần tiếp của Dafu (44.000 kg) và Bảo Lai (110.000 kg) trình 04/11/2026 (TTr 7271, 7270/TTr-SCT).
- **GP Cục Hóa chất cấp cho DN trên địa bàn**: 1844/GP-HC ngày 23/9/2026 — TNHH MTV Triều Dương, SX và KD hóa chất cần kiểm soát đặc biệt (SX benzaldehyde 210.000 kg/năm; KD benzaldehyde, methanol 2.000.000, toluene 2.500.000, axit sulfuric 5.400.000, axit hydrochloric 470.000 kg/năm; cơ sở tại CCN Phố Ràng, xã Bảo Yên), hiệu lực đến 23/9/2031 (số, ngày viết tay trên bản quét). Sở đã cử đại diện đoàn thẩm định (3574/SCT-CN 18/6/2026) → khi Cục cấp phép, Sở nhận bản sao để theo dõi, kiểm tra.
- **GP tỉnh khác gửi về**: Sở Công Thương Thái Nguyên cấp 598 và 599/GP-SCT ngày 16/9/2026 cho CP 198 Thành Công nhập khẩu axit sulfuric 60% (72.000 kg và 48.000 kg) bán cho 5 cơ sở, trong đó có **CP Lâm Nông sản Thực phẩm Yên Bái (phường Yên Bái)** → cơ sở sử dụng trên địa bàn, Sở theo dõi mua bán hóa chất kiểm soát đặc biệt nhóm 2.
- Từ chối / trả hồ sơ GCN: CP TM-VT và tư vấn kỹ thuật (HNO3) — 1709/SCT-CN 01/4/2026; Hóa chất Quang Huy (lưu huỳnh, kho thuê Bắc Ninh) — 7149/SCT-CN 30/10/2026 yêu cầu hoàn thiện (mục 5c ref 16).

## 4. Kiểm tra chuyên ngành hóa chất 2026 (QĐ 2872/QĐ-SCT 21/5/2026; KH 2922/KH-ĐKT; TB 2948/TB-ĐKT; BC 3508/ĐKT-SCT 16/6/2026)

| Đơn vị | Ngày | Kết quả |
|---|---|---|
| TNHH MTV Khí công nghiệp Lào Cai (KD oxy) | 28/5/2026 | 3 tồn tại: thay đổi ĐKDN 4 lần không cấp lại GCN (k4 Đ16 NĐ 71/2019); chưa huấn luyện nhóm 1, 2 (02 người) (điểm a k2 Đ11 NĐ 71/2019); chưa có Biện pháp sự cố trong vận chuyển từ 01/01/2026 (điểm c k1 Đ38 Luật — chưa có chế tài). **BB VPHC 01.KCN/BB-VPHC 29/5/2026 → QĐ XPHC 3364/QĐ-XPHC 10/6/2026**; CV 3907/SCT-CN 01/7/2026 |
| TNHH MTV Supe lân Apromaco Lào Cai (sử dụng) | 01/6/2026 | Chấp hành tốt: Biện pháp xác nhận 530/SCT-KT 17/4/2015, diễn tập hằng năm; huấn luyện qua tư vấn (QĐ 190225-2/QĐML-HLATHC 19/2/2025, 240225-1/QĐCNKQ-HLATHC); kiểm định đến 25/11/2026; vận chuyển H2SO4 thuê đơn vị có GP; báo cáo CSDL 04/02/2026. TB 3929/SCT-CN 02/7/2026 |
| CP LNS Thực phẩm Yên Bái — NM giấy Nguyễn Phúc (sử dụng) | 04/6/2026 | Tốt; tồn tại: chưa bố trí người chuyên môn ATHC trung cấp hóa (k2 Đ27 NĐ 25/2026). CV 3927/SCT-CN |
| TNHH Hapaco Yên Sơn — XN giấy Âu Lâu (sử dụng) | 08/6/2026 | Tốt. CV 3928/SCT-CN |

Kế hoạch kiểm tra 2026 (QĐ 1402/QĐ-SCT 21/3/2026) ghi 5 đơn vị hóa chất (thêm CP Phốt pho Apatit Việt Nam) nhưng QĐ 2872 chỉ 4.
Đợt 12/2025 (QĐ 2827/QĐ-SCT; BC 3470/ĐKT-SCT 31/12/2025) kiểm tra công tác phòng ngừa, ứng phó sự cố: Phốt pho vàng Việt Nam (TB 3462), LaVita (3464), Luyện đồng (3466), Đông Nam Á (3467); dừng kiểm tra Đức Giang (3294/SCT-CN).
Cục Hóa chất kiểm tra, xử phạt trực tiếp: TNHH Thương mại Hải Đăng — 26/QĐ-XPVPHC 08/7/2026, 16 triệu đồng (ref 16 mục 5).

## 5. Báo cáo năm 2025 trên CSDL hóa chất quốc gia (CV 3169/SCT-CN 19/12/2025; đôn đốc lần 2 CV 1735/SCT-CN 02/4/2026)

- Đã báo cáo (25): Đức Giang LC, Phốt pho vàng LC, Victory, Khí công nghiệp LC, Luyện đồng Vimico, DAP 2, Apromaco, Mỏ tuyển đồng Sin Quyền, Phốt pho VN, Lavita, BQL DA ĐTXD Trấn Yên, Yên Phú, Cấp nước Nghĩa Lộ, Xi măng và Khoáng sản YB, Lâm Nông sản TP YB, An Bình Văn Yên, Cấp nước và XD YB, Hapaco Yên Sơn, Nhung Thắng LPG, Đá trắng Bảo Lai, Tân Phú, An Phúc, Việt Phong, Nước sạch và MT Lục Yên, YBB.
- Chưa báo cáo, đề nghị lần 2 (12): Đông Nam Á LC, Phốt pho vàng VN, Phốt pho Apatit VN, Khoáng sản và Luyện kim Việt Trung, SX và XNK Bao bì, TM Thành Công, Vật tư và Thiết bị Gia Phát, Cấp nước Lào Cai, Apatit Việt Nam, Đồng Tả Phời, Thịnh Đạt, Kim Thành. Chế tài từ 25/8/2026: 30–40 triệu đồng với tổ chức (điểm a k3 Đ25 NĐ 275/2026).

## 6. Kế hoạch, Biện pháp sự cố đang theo dõi

- Kế hoạch do Cục Hóa chất thẩm định (điểm a): Đức Giang LC — nhà máy axit thực phẩm, axit điện tử, muối phốt phát (Hội đồng QĐ 333/QĐ-HC 27/10/2026, họp 29/10/2026, Sở cử CV Loan theo 7007/SCT-CN); DAP số 2 — Kế hoạch điều chỉnh, NH3 5.700 t (Phiếu 03c 08/9/2026).
- Biện pháp DN ban hành: Khí công nghiệp LC (01/QĐ 05/01/2019, diễn tập 12/6/2025; đang thay thiết bị chứa, phải cập nhật); Apromaco (xác nhận 530/SCT-KT 17/4/2015 — cần rà ngưỡng Phụ lục IV NĐ 24, nếu vượt phải lập Kế hoạch trước 31/12/2026); Thành Công (xác nhận 01/XN-SCT 29/01/2016; Biện pháp 2026 chưa làm rõ thay đổi — 5944/SCT-CN 23/9/2026); Trạm XLNT KCN Tằng Loỏng giai đoạn IIg (12/QĐ-TTDV 05/02/2026); LNS, Hapaco (có, số chưa ghi).
- Chủ trương xây dựng Kế hoạch phòng ngừa, ứng phó sự cố hóa chất cấp tỉnh: 6608/SCT-CN 14/10/2026; Tổ soạn thảo Kế hoạch quốc gia: QĐ 2584/QĐ-BCT 08/10/2026, Sở cử người 5197, 6571/SCT-CN.

## 7. Chỗ còn phải đối chiếu bản gốc (đã đánh dấu trên web)

GP 3387 (ngày in trên thân giấy); GP 3385 (ngày hóa đơn in 01/7/2027); GP 1844/GP-HC (số, ngày, hạn viết tay); GCN 07/GCN-SCT 2023 Đức Giang (tệp trùng GCN 47/2025); bảng hóa chất các GCN quét mờ; mức phạt QĐ 3364/QĐ-XPHC; đơn vị ban hành QĐ 12/QĐ-TTDV; ký hiệu LĐV (kế hoạch huấn luyện 739, 781/KH-LĐV) suy là Luyện đồng Vimico.
