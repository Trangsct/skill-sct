# CHANGELOG — plugin kho-vlncn-sct-vn

## [1.12.0] - 25/9/2026 — ref 03 theo khung 01/7/2026; mẫu 10 hướng dẫn trình tự 3 đối tượng kho
- **ref 03 (quy trình kho mới) bỏ khung cũ:** "Hướng A/B" theo Điều 131 Luật XD 2014 và "Sở thẩm định thiết kế triển khai sau TKCS" chuyển thành lịch sử; nay Sở thẩm định **BCNCKT** (k1 Đ27 Luật 135; Đ32 NĐ 217) lồng ghép PCCC, thiết kế triển khai do **chủ đầu tư thẩm định** trên cơ sở thẩm tra (k3 Đ29 Luật 135; k1, k4 Đ41, Đ42 NĐ 217); năng lực theo NĐ 212/2026 (Đ41 tự công khai, k1 Đ28 CCHN 4 lĩnh vực, k2 Đ38 chỉ huy trưởng không cần CCHN, k4 Đ22); bỏ NĐ 175/2024, "chứng chỉ năng lực", "hợp đồng lao động"; báo cáo hoàn thành theo PL VI và k4 Đ27 NĐ 207 thay "báo trước 10 ngày" của Điều 23 NĐ 06/2021.
- **mẫu 10 MỚI:** công văn hướng dẫn trình tự từng bước cho kho cố định xây mới (8 bước), kho tạm (7 bước, kể cả container lưu động — điểm 2.1, 2.7 PL10 QCVN) và kho hiện hữu (7 bước theo Điều 4 TT 32/2026), mỗi bước dẫn điều khoản.

## [1.11.1] - 24/9/2026 — mức phạt tổ chức k3 Đ18 NĐ 106
- ref 06: đưa kho vào sử dụng khi chưa tự nghiệm thu PCCC — tổ chức 60–100 triệu (cá nhân 30–50), đình chỉ 03–06 tháng (bản 1.11.0 chỉ ghi mức cá nhân).

## [1.11.0] - 24/9/2026 — nghiệm thu PCCC kho theo NĐ 347/2026 (bỏ văn bản chấp thuận của Công an)
- Căn cứ: NĐ 347/2026/NĐ-CP ngày 08/9/2026 (hiệu lực 15/9/2026) bãi bỏ k5 Đ6, Đ10 NĐ 105/2025 và Mẫu PC15-PC17; CV 6501/CAT-PCCC ngày 23/9/2026 của Công an tỉnh.
- Đầu mục PCCC của kho đổi thành **biên bản nghiệm thu PCCC do CĐT tổ chức** (hợp với điểm đ k1 Đ39 Luật 42/2024 sđ Luật 118/2025 "văn bản nghiệm thu… hoặc văn bản chấp thuận…"); văn bản chấp thuận đã cấp trước 15/9/2026 vẫn dùng; thêm khai báo CSDL PCCC và thông báo Công an tỉnh thời gian đưa kho vào hoạt động.
- Sửa SKILL.md (bảng 4 trụ, GĐ4, anti-error 3), ref 03, 04, 06, 08, 09, 10, 11; mẫu 01 (mục b chỉ còn đối chiếu hồ sơ PCCC), mẫu 02 (căn cứ + yêu cầu CĐT), mẫu 08.

## [1.10.4] - 09/9/2026 — bổ sung vụ Phú Hà (kho hiện hữu mỏ đá Bản Cầm) + khung TT 32/2026
- Thêm `vi-du-thuc-te/phu-ha-kho-hien-huu-ban-cam-2026/SCT-CN_YK_De_cuong_kiem_dinh_Kho_VLNCN_Phu_Ha_Ban_Cam_9.2026.docx` — CV tham gia ý kiến Đề cương kiểm định, phúc đáp VB 0709/2026/CV-PH ngày 07/9/2026 của Công ty cổ phần Phú Hà (nối tiếp CV 5400/SCT-CN ngày 04/9/2026).
- **Mẫu này thay cho mẫu 04 vụ Mông Sơn** khi làm kho hiện hữu từ 01/7/2026: căn cứ chuyển sang Điều 4 Thông tư số 32/2026/TT-BXD ngày 22/6/2026 (hướng dẫn khoản 6 Điều 8 NĐ 207/2026; bãi bỏ các Điều 2-9 và 19 TT 10/2021/TT-BXD). Khoản 5 Điều 4 là căn cứ để SCT cho ý kiến về đề cương và là căn cứ yêu cầu tổ chức kiểm định phải độc lập với chủ đầu tư, chủ sở hữu và các nhà thầu.
- Ghi nhận lập luận năng lực: không có CCHN mang tên "kiểm định xây dựng" (khoản 1, khoản 2 Điều 88 Luật Xây dựng 135/2025; khoản 1 Điều 28 NĐ 212/2026 chỉ 4 lĩnh vực cấp CCHN).
- Cấp công trình kho: mục 1.2.6.8 điểm b Bảng 1.2 Phụ lục I TT 34/2026/TT-BXD — kho cố định nổi và nửa ngầm sức chứa ≤10 tấn là cấp II (>10 tấn: cấp I).
- Cập nhật `vi-du-thuc-te/00-MUC-LUC.md` (thêm VỤ 5). plugin.json 1.10.3 → **1.10.4**.

## [1.10.1] - 31/8/2026 — BỎ "nhật ký giám sát" khỏi mọi danh mục hồ sơ

Kỹ sư phản biện: *"nhật ký giám sát bỏ không yêu cầu từ Nghị định 06 rồi, giờ Nghị định 207 cũng không yêu cầu"*. Đã tra toàn văn cả hai nghị định — **phản biện đúng hoàn toàn**.

- Cả NĐ 06/2021 và NĐ 207/2026 chỉ có **"nhật ký thi công xây dựng công trình"** do **nhà thầu thi công** lập (khoản 13 Điều 13 NĐ 06/2021 = khoản 13 Điều 15 NĐ 207/2026; mẫu Phụ lục IIa). Không có bất kỳ chỗ nào nhắc "nhật ký giám sát".
- Tài liệu đúng của tư vấn giám sát: **báo cáo về công tác giám sát thi công xây dựng công trình** — khoản 3 Điều 20 NĐ 207/2026, gồm (a) báo cáo định kỳ hoặc theo giai đoạn thi công (Phụ lục IVa) và (b) báo cáo khi tổ chức nghiệm thu giai đoạn, nghiệm thu hoàn thành gói thầu, hạng mục, công trình (Phụ lục IVb). Nhà thầu thiết kế lập báo cáo đánh giá việc thực hiện giám sát tác giả (Điều 21).
- Sửa: ref 03 mục quản lý chất lượng, ref 04 mục IV.3, ref 08 checklist, mẫu 08-09 biên bản kiểm tra.
- SKILL.md **anti-error 14 MỚI**: yêu cầu DN nộp tài liệu không có trong quy định là đặt thêm điều kiện trái pháp luật; rà mọi công văn, biên bản, checklist trước khi phát hành.

## [1.10.0] - 31/8/2026 — PHÂN LUỒNG 4 trường hợp; công trình tạm được MIỄN KTCTNT

### Thêm
- **references/11-phan-luong-4-truong-hop.md** — reference mới, GHI ĐÈ mọi phát biểu trái ngược tại ref 03, 04, 06, 08, 09 về diện KTCTNT của kho tạm. Nội dung: cấp công trình kho theo TT 34/2026 mã 1.2.6.8 (không có kho cấp III/IV); kho luôn thuộc Phụ lục IV NĐ 217/2026 mã II.6; phát hiện loại trừ công trình tạm tại khoản 1 Điều 25 NĐ 207/2026 kèm lập luận hai tầng; đối chiếu khoản 1 Điều 24 NĐ 06/2021 (không có loại trừ); chuyển tiếp khoản 3 Điều 53; sơ đồ phân luồng 3 câu hỏi; bảng đối chiếu 4 luồng; căn cứ kiểm định theo NĐ 207/2026; Luồng D thuê kho - gửi kho; 6 điểm không đổi ở cả 4 luồng.
- SKILL.md anti-error **12** (kiểm tra diện KTCTNT trước khi ra kế hoạch kiểm tra) và **13** (không hợp thức hóa hồ sơ giai đoạn đã qua, không soạn hộ hồ sơ dưới danh nghĩa đơn vị thiết kế/giám sát).

### Sửa
- SKILL.md mục VI: thay sơ đồ 6 giai đoạn đơn tuyến bằng **BƯỚC 0 phân luồng** + quy trình Luồng A.
- SKILL.md Nhóm 2 (Xây dựng): bổ sung loại trừ khoản 1 Điều 25 + chuyển tiếp khoản 3 Điều 53 vào mục 9; bổ sung bảng cấp công trình kho vào mục TT 34/2026; anti-error 1 (Đ131 → Đ72), anti-error 2 (Đ23 NĐ 06/2021 → khoản 2 Đ29 NĐ 207/2026).
- ref 03: nêu rõ chỉ áp dụng LUỒNG A; kho phục vụ thi công chuyển LUỒNG B.
- ref 04: cảnh báo diện áp dụng ở đầu file; mục I căn cứ tách 2 khung.
- ref 05: cảnh báo căn cứ kiểm định đã đổi từ 01/7/2026, trỏ ref 11 mục V.
- ref 08: checklist thêm mục "đã chạy phân luồng chưa".
- ref 09: viết lại câu 2 (kho tạm miễn 4 nội dung) và câu 3 (4 điều kiện phụ thuộc luồng).
- **vi-du-thuc-te/dong-tien-kho-tam-KTCTNT-2026/README-BAI-HOC.md**: cảnh báo case rơi vào khoản 3 Điều 53, không dùng làm tiền lệ về diện kiểm tra; giữ giá trị làm mẫu kỹ thuật soạn thảo.

### Cần xác minh
- TT 10/2021/TT-BXD còn hiệu lực hay đã có TT thay thế theo khoản 6 Điều 8 NĐ 207/2026.
- Rà soát hồ sơ kho tạm đang thụ lý để áp khoản 3 Điều 53 (dừng KTCTNT).

## [1.9.0] - 29/8/2026
Case study thứ hai theo khung NĐ 207/2026: kho VLNCN phục vụ MỎ chì kẽm Háng Chua Xay (Cty CP Toàn Kim Sơn, TB 4566/TB-SCT ngày 30/7/2026) — cặp đối chiếu với kho tạm Đồng Tiến.
- 6 điểm làm đúng (giám sát thuê ngoài độc lập; KH trước kiểm tra; địa danh chuyển đổi chuẩn; điều khoản mã định danh NĐ 212) và 9 vấn đề rút kinh nghiệm, nặng nhất: 03 kim thu sét đặt TRÊN MÁI kho trái khoản 1.3 PL11 QCVN 01:2019/BCT; không có hệ chống cảm ứng tĩnh điện ≤5Ω (khoản 2.4 PL11); quá thời hạn 12 ngày làm việc (điểm b khoản 4 Điều 27 NĐ 207/2026); biên bản kiểm tra bị sửa 13 ngày sau khi lập; phân loại kho cố định/lưu động chưa chốt (quyết định đầu mục nghiệm thu PCCC).
- SKILL.md: anti-error 11a cho kho phục vụ mỏ; bảng so sánh kho tạm ↔ kho mỏ trong README case.

## [1.8.1] - 29/8/2026
- Đính chính anti-error 10 + README case Đồng Tiến theo NĐ 212/2026/NĐ-CP: KHÔNG còn yêu cầu "chứng chỉ năng lực tổ chức" như điều kiện hiện hành; minh chứng năng lực soi theo hai mốc 01/7/2026, trỏ xd-sct-vn ref 11 mục 5.

## [1.8.0] - 29/8/2026
Liên kết plugin `xd-sct-vn` + case chuẩn kho tạm Đồng Tiến. Nguồn: bộ hồ sơ KTCTNT kho VLNCN tạm Đồng Tiến (gói thầu SFD-XL03 Khánh Hòa - Văn Yên) Bạn cung cấp 29/8/2026.
- **SKILL.md Nhóm 2 (Xây dựng) viết lại theo 2 khung**: khung HIỆN HÀNH từ 01/7/2026 (Luật 135/2025 Đ43-Đ72-Đ57, NĐ 207/2026 Đ25-27, NĐ 217/2026, TT 34 + 39/2026, QĐ 11/2026) và khung CŨ chỉ dùng theo chuyển tiếp (Luật 50/2014, NĐ 06/2021, TT 06/2021 + TT 02/2025); GATE 3 mốc trỏ sang **plugin `xd-sct-vn` reference `11-chuyen-tiep-2026.md`**; toàn văn 2 khung nằm ở `xd-sct-vn/van-ban-goc/` — không nhân đôi kho văn bản.
- **Thêm case study `vi-du-thuc-te/dong-tien-kho-tam-KTCTNT-2026/`** (14 file + README-BAI-HOC): 8 điểm làm đúng dùng làm chuẩn (nhất quán tư cách công trình tạm; ràng buộc tháo dỡ; giới hạn phạm vi kiểm tra; biểu thông số chi tiết; điều khoản "đóng băng" khi thay đổi; xử lý 2 mốc 2 khung; tốc độ 10 ngày) và 6 điểm rút kinh nghiệm (thiếu 01 câu lập luận chuyển tiếp; THIẾU phiếu đo điện trở hệ chống tĩnh điện ≤4Ω; file năng lực của chính CĐT nộp nhầm — trùng md5 với hồ sơ AYB; kế hoạch và kiểm tra cùng ngày; biểu thiếu mục khoảng cách an toàn PL7 QCVN; mã định danh ghi lấp lửng).
- **Anti-error 8-11 mới**: đủ phiếu đo cho từng hệ tiếp đất; kế hoạch kiểm tra trước ngày kiểm tra 2-3 ngày làm việc; soi năng lực CĐT "3 trong 1" (tự thẩm định + tự thi công + tự giám sát) kèm kiểm md5 hồ sơ số; GATE chuyển tiếp khi hồ sơ vắt mốc 01/7/2026.
- Loại khỏi bộ lưu: hồ sơ năng lực PCCC Tràng An 168 (101 MB, vượt giới hạn GitHub) và bản trùng md5 của file năng lực.

