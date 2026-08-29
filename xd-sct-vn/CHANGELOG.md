# CHANGELOG — plugin xd-sct-vn

## [1.4.0] - 29/8/2026
- Nạp văn bản gốc Bạn cung cấp vào `van-ban-goc/` (đã GATE nội dung, đối chiếu khớp các trích dẫn trong SKILL + ref 11):
  - `ND-212-2026-dieu-kien-nang-luc-HDXD-CSDL-quoc-gia.docx` — NĐ 212/2026/NĐ-CP ngày 17/6/2026, ký PTT Phạm Gia Túc; xác minh nguyên văn k4 Đ22, Đ28, Đ38, Đ41, Đ55.
  - `NQ-66.18-2026-NQ-CP-phan-quyen-cat-giam-TTHC-DKKD.docx` — NQ 66.18/2026/NQ-CP ngày 18/5/2026 (bản đầy đủ 4720 đoạn kèm phụ lục); hiệu lực 01/7/2026-28/02/2027 trừ ngoại lệ k2, k4 Đ7.
  - Loại: bản 66_18 định dạng .doc là bản TIẾNG ANH rút gọn (56 đoạn, không phụ lục) — không nạp.
- Ghi chú mới từ toàn văn NQ 66.18: Phụ lục I.2 (Công Thương) phần VLNCN - tiền chất chỉ sửa thủ tục thẩm quyền Bộ (XNK), KHÔNG ảnh hưởng thủ tục cấp tỉnh — các plugin sd-vlncn, kho-vlncn không phải điều chỉnh quy trình.

## [1.3.0] - 29/8/2026
- Bổ sung khối CẮT GIẢM ĐIỀU KIỆN NĂNG LỰC 01/7/2026 (xác minh web): NĐ 212/2026/NĐ-CP (bãi bỏ chứng chỉ năng lực tổ chức, tự công khai csdlhdxd.gov.vn Đ41; CCHN còn 4 lĩnh vực Đ28; chỉ huy trưởng xét kinh nghiệm Đ38; cấm đòi giấy tờ đã có trên CSDL k4 Đ22; chuyển tiếp Đ55) + NQ 66.18/2026/NQ-CP (01/7/2026-28/02/2027). Ref 11 thêm mục 5: bảng chuyển tiếp năng lực theo mốc hoạt động + nguyên tắc có lợi khi xử phạt + câu mẫu yêu cầu DN (tiền lệ Đồng Tiến).

## [1.2.1] - 29/8/2026
- Reference `11-chuyen-tiep-2026.md`: bổ sung bài học số 3 — vụ kho VLNCN tạm Đồng Tiến, case CHUẨN "hai mốc, hai khung" trong một hồ sơ (miễn GPXD theo Đ89 Luật 2014 tại thời điểm khởi công; KTCTNT theo NĐ 207/2026 tại thời điểm thủ tục); liên kết chéo plugin `kho-vlncn-sct-vn` v1.8.0.

## [1.2.0] - 29/8/2026
Bổ sung nhóm chuyển tiếp + case study thực tế. Nguồn: bộ VBQPPL Bạn cung cấp 29/8/2026 và hồ sơ thẩm định BCNCKT 110kV Âu Lâu (Phòng QLNL).
- **Thêm reference `11-chuyen-tiep-2026.md`** — GATE CHUYỂN TIẾP quanh mốc 01/7/2026: bảng quyết định khung áp dụng (khoản 1-4 Đ53 NĐ 207/2026; khoản 1, 2, 5 Đ76 NĐ 217/2026; khoản 1 Đ53 về cấp công trình theo thời điểm quyết định đầu tư); 3 mốc thời gian độc lập của một dự án; câu mẫu lập luận chuyển tiếp đưa vào văn bản.
- **Thêm văn bản gốc khung CŨ** phục vụ hồ sơ chuyển tiếp: NĐ 06/2021 (QLCL), NĐ 175/2024 (QLHĐXD), TT 06/2021/TT-BXD + TT 02/2025/TT-BXD (phân cấp công trình). Đã loại bản .doc trùng của TT 06/2021.
- **Thêm thông tư khung mới**: TT 36/2026/TT-BXD (chi phí ĐTXD), TT 39/2026/TT-BXD (CSDL quốc gia về hoạt động xây dựng).
- **Thêm case study `vi-du-thuc-te/au-lau-110kv-tham-dinh-BCNCKT/`**: 14 file hồ sơ thật + README-BAI-HOC.md — ghi nhận điểm làm đúng (thẩm quyền, phạm vi thẩm định a-b-c khoản 4 Đ27, lấy ý kiến đủ đối tượng) và 8 nhóm lỗi cần tránh: bỏ qua khoản 2 Đ76 NĐ 217 (lỗi nền tảng); quá thời hạn không gia hạn; dẫn nhầm cặp NĐ 207↔217; đánh giá theo quy hoạch tỉnh cũ thay vì QĐ 525/QĐ-UBND; nhận xét PCCC copy khung dân dụng; khẳng định vượt căn cứ hồ sơ; thành phần trùng-thiếu; số liệu mâu thuẫn nội bộ (kể cả phép tính phí tự mâu thuẫn).
- **SKILL.md**: nâng cấp anti-error 1 (chuyển tiếp thành văn, trỏ ref 11); thêm anti-error 9-12 (cặp 207↔217; nghĩa vụ thẩm tra thiết kế công trình AT-LICĐ — bài học vụ phân lân nung chảy 8/2026; thời hạn cứng Đ37 + quy hoạch QĐ 525; chỉ khẳng định điều có tài liệu đối chiếu). Cập nhật cấu trúc plugin, mục lục văn bản gốc.
- Không đưa vào: bản .doc trùng TT 06/2021; dự thảo QĐ phân cấp QLĐTXD 13/01/2025 (đã có bản ban hành QĐ 11/2026); NĐ 25/2026 + NĐ 26/2026 hóa chất (đã có trong plugin hc-sct-vn); TT 34/2026 và bản scan QĐ 11/2026 (trùng file đã có, xác nhận md5).

## [1.1.1] - 14/7/2026
- Đồng bộ Thông báo phân công nội bộ Phòng QLCN 10/7/2026: kiểm duyệt nội bộ thẩm định/KTCTNT = **PTP Nguyễn Hồng Vân**; phối hợp kho VLNCN chuyển CN(Linh) → **CN(Khôi)**.

## v1.1.0 (04/7/2026)
Bổ sung văn bản gốc và nội dung cấp công trình để plugin tự đủ, không phải tải thêm khi làm việc.
- **Thêm TT 34/2026/TT-BXD ngày 25/6/2026** (cấp công trình xây dựng, thay TT 06/2021) — bản docx gốc trong van-ban-goc/.
- **Thêm reference 10-cap-cong-trinh.md**: nguyên tắc xác định cấp (Phụ lục I/II/III); bảng tra chuyên sâu công trình ngành CT (luyện kim 1.2.2, khoáng sản 1.2.3, xăng dầu/LPG 1.2.4, hóa chất/VLNCN 1.2.6, apatit 1.2.6.7); chuyển tiếp Điều 5.
- **Thêm NĐ 217/2026 bản PDF gốc** (nén còn đọc rõ) bên cạnh bản OCR text — có bản dấu đỏ để in/đối chiếu.
- Cập nhật SKILL.md (mục II thêm TT 34; mục III trỏ ref 10; mục VIII thêm ref 10), reference 02 (ví dụ cấp công trình theo TT 34), mục lục văn bản gốc.


## v1.0.0 (04/7/2026)
Phiên bản đầu tiên. Plugin chuyên gia QLNN về xây dựng (cấp bộ + tỉnh + xã), Sở Công Thương tỉnh Lào Cai, chuyên sâu công trình ngành Công Thương.

**Nội dung:**
- SKILL.md: nguyên tắc "SCT là cơ quan chuyên môn về xây dựng đối với công trình công nghiệp" (3 câu hỏi); phân định thẩm quyền 3 cấp; quy trình 6 giai đoạn; người ký/người soạn (PGĐ Hoàng Văn Thuân, Lưu CN(Dũng)); 8 nhóm anti-error.
- 9 references: khung pháp lý; thẩm quyền 3 cấp; thẩm định + khởi công; KTCTNT; giấy phép xây dựng; công trình tạm; sự cố - bảo trì - an toàn; chuyên sâu công trình ngành Công Thương; hỏi đáp DN.
- Bộ mẫu KTCTNT công trình công nghiệp (kế hoạch kiểm tra, biên bản, thông báo chấp thuận nghiệm thu).
- 12 văn bản gốc (GATE metadata): Luật XD 135/2025, NĐ 207/2026, NĐ 217/2026 (OCR), NĐ 140/2025, NĐ 144/2025, QĐ 11/2026/QĐ-UBND Lào Cai (PDF + OCR), NĐ 14/2026, NQ 24/2026, NQ 18/2026, NĐ 35/2023, NĐ 178/2025, NĐ 243/2025.

**Liên kết:** kho-vlncn-sct-vn, sd-vlncn-sct-vn, hl-vlncn-sct-vn, kcn-ccn-vn, pccc-sct-vn, quy-hoach-ct-vn, vbhc-vn, sct-laocai-org-vn.

**Điểm cần xác minh (ghi trong ref 05, 09):** Điều 14 khoản 1c QĐ 11/2026 (OCR) ghi UBND xã cấp GPXD "công trình cấp II, cấp IV" — khác Điều 53 NĐ 217/2026 (xã cấp III, IV). Cần đối chiếu bản QĐ 11/2026 chính thức khi gặp công trình cấp II/III của tổ chức.

**Cần bổ sung (ghi trong 00-MUC-LUC):** TT 34/2026/TT-BXD (cấp công trình), Phụ lục IX NĐ 207/2026, Phụ lục IV NĐ 217/2026, NĐ 06/2021 + 175/2024 (chuyển tiếp).
