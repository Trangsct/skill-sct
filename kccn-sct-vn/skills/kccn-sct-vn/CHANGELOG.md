# CHANGELOG — kccn-sct-vn

## v1.3.0 — 2026-07-06 (cập nhật 03 KCN được chấp thuận chủ trương đầu tư)

### Thêm mới
- `references/15-kcn-chap-thuan-ctdt-2026.md`: chi tiết 03 QĐ chấp thuận CTĐT đồng thời chấp thuận NĐT — KCN Bản Qua (QĐ 2170/QĐ-UBND 23/6/2026 của UBND tỉnh, 76,39 ha, NĐT Công ty CP ĐT phát triển công nghiệp Lào Cai, GCN ĐKĐT mã 4275604886 ngày 30/6/2026); KCN Phú Xuân (QĐ 2336/QĐ-UBND 02/7/2026 của Chủ tịch UBND tỉnh, 300 ha) và KCN Phú Xuân 1 (QĐ 2338/QĐ-UBND 02/7/2026, 200 ha) — cùng NĐT Công ty CP công nghiệp Linh Linh, xã Gia Phú. Nâng tổng số KCN đã thành lập/có QĐ CTĐT lên 10. Kèm 5 lưu ý nghiệp vụ (thẩm quyền ban hành khác nhau, chênh lệch 76,39/107 ha Bản Qua, không gộp Phú Xuân + Phú Xuân 1).
- `van-ban-goc/`: bổ sung 4 file gốc đã ký: QD-2170, QD-2336, QD-2338, GCN-DKDT-KCN-Ban-Qua.

### Cập nhật
- `references/12`: tách bảng "KCN mới được chấp thuận CTĐT (03)" khỏi nhóm "chưa thành lập"; tổng 10 KCN đến 7/2026.
- `references/14`: chú thích trạng thái CTĐT mới cho 3 dòng Bản Qua, Phú Xuân, Phú Xuân 1 trong bảng 13 KCN thu hút đầu tư.
- `SKILL.md`: mục lục + trigger 8 thêm reference 15.

## v1.2.0 — 2026-07-06 (merge dữ liệu tra cứu từ skill cũ kcn-ccn-vn)

### Thêm mới
- `references/13-qd525-quy-hoach-tinh.md`: TOÀN VĂN Phụ lục II (20 KCN) + Phụ lục III (54 CCN, đủ 6 nhóm: giữ nguyên / điều chỉnh / rút / bổ sung / tiến độ / sau 2030) của QĐ 525/QĐ-UBND ngày 25/02/2026; căn cứ ban hành, mục tiêu KT-XH; đối soát số liệu 54 CCN (QĐ 525) vs 56 CCN (Báo cáo 18/6/2026) vs 52 CCN (bản docx dự thảo thiếu Châu Quế + Châu Quế Thượng); tầm nhìn 2050. Chuyển từ reference 17 của skill kcn-ccn-vn.
- `references/14-qd1382-danh-muc-thu-hut.md`: QĐ 1382/QĐ-UBND ngày 23/4/2026 — 431 danh mục thu hút đầu tư; chi tiết 13 KCN (40.044 tỷ) + 35 CCN (22.854 tỷ) kèm TMĐT, nhà đầu tư, phân 3 nhóm tiến độ; suất vốn QĐ 425/QĐ-BXD ngày 30/3/2026. Chuyển từ reference 16 của skill kcn-ccn-vn, bổ sung cảnh báo dữ liệu động (cột nhà đầu tư/tiến độ).

### Sửa lỗi nghiêm trọng (vị trí xã sai trong reference 12 cũ)
Reference 12 v1.1.0 suy tên xã từ tên KCN, SAI so với Phụ lục II QĐ 525 (bản PDF đã ký, khớp QĐ 1382):
- KCN Bản Qua: ~~Xã Bản Qua~~ → **Xã Bát Xát**
- KCN Y Can: ~~Xã Y Can~~ → **Xã Lương Thịnh, xã Quy Mông**
- KCN Đông An: ~~Xã Đông An~~ → **Xã Đông Cuông**
- KCN Thịnh Hưng: ~~Xã Thịnh Hưng~~ → **Xã Yên Bình, phường Văn Phú**
- KCN Lục Yên: ~~Xã Tân Lĩnh~~ → **Xã Lục Yên, xã Tân Lĩnh**
- KCN Cốc Mỳ - Trịnh Tường: ~~Xã Cốc Mỳ, Trịnh Tường~~ → **Xã Trịnh Tường**
- Bổ sung KCN Việt Hồng 2 (200 ha, xã Việt Hồng) bị thiếu trong bảng.
- CCN Y Can: chốt **Xã Quy Mông** (khác vị trí KCN Y Can); CCN Đông An: **Xã Đông Cuông**; CCN Bảo Hưng 2: **Phường Âu Lâu** (75→50 ha); CCN Đầm Hồng: các phường Yên Bái, Văn Phú (rút khỏi QH).

### Cập nhật
- `references/12`: chuyển thành bảng tra NHANH, trỏ sang reference 13 (toàn văn QĐ 525) và 14 (QĐ 1382); thêm quy tắc "KHÔNG suy tên xã từ tên KCN"; thêm phân biệt CCN Y Can vs KCN Y Can; cập nhật website congnghieplaocai.vn.
- `SKILL.md`: mục lục thêm reference 13, 14; trigger 8 mở rộng tra cứu quy hoạch + thu hút đầu tư; nguyên tắc bất biến 4 và 6 cập nhật; description thêm từ khóa "QĐ 525 quy hoạch tỉnh, QĐ 1382 danh mục thu hút đầu tư".

### Không merge (chủ đích)
- Reference 15, 18 (hiện trạng lấp đầy/tiến độ theo Báo cáo 18/6/2026) và các bảng lấp đầy trong reference 12 skill cũ: giữ nguyên tắc plugin "hiện trạng là số liệu tĩnh — HỎI Bạn", tránh dùng số liệu lỗi thời khi soạn văn bản.
- Reference 11 (NQ 34/KH 134), 13 (suất vốn chi tiết), 14 (NQ 26) skill cũ: cân nhắc merge đợt sau nếu cần.

## v1.1.0 — 2026-07-05
- Sửa lỗi nghiêm trọng quy trình Điều 10 NĐ 32/2024; bổ sung bài học thực tế KCN Phú Xuân, CCN Tân Nguyên, Minh Quân, Y Can.

## v1.0.0 — 2026-07
- Phát hành lần đầu: 12 references, 3 checklists, 7 bộ mẫu văn bản, văn bản gốc, ví dụ thực tế.
