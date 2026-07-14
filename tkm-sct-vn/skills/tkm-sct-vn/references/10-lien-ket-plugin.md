# 10 — Bản đồ liên kết plugin: chuỗi công việc thiết kế mỏ trong hệ sinh thái skill-sct

Nguyên tắc: `tkm-sct-vn` là plugin CHUYÊN SÂU về thẩm định thiết kế mỏ; mọi nghiệp vụ giáp ranh chuyển sang plugin chuyên trách tương ứng, không tự làm thay. Khi một hồ sơ chạm nhiều domain: xử lý theo THỨ TỰ PHÁP LÝ của dự án (quy hoạch → dự án/thiết kế → môi trường/PCCC → xây dựng → VLNCN/hóa chất → vận hành), mỗi bước gọi đúng plugin.

## A. Vòng đời một dự án mỏ — plugin nào vào việc ở bước nào

| # | Bước | Plugin chủ lực | tkm-sct-vn làm gì |
|---|---|---|---|
| 1 | Kiểm tra mỏ có trong quy hoạch (QĐ 866/QĐ-TTg, Phụ lục QĐ 525/QĐ-UBND) | `quy-hoach-ct-vn` | Nhận kết quả làm mục "Sự phù hợp quy hoạch" khi thẩm định; không tự tra quy hoạch ngoài plugin đó |
| 2 | GATE PDF mọi văn bản đến (tờ trình, giấy phép, QĐ chủ trương) | `vbhc-pdf-reader-vn` | Bắt buộc chạy trước B0 |
| 3 | Thẩm định BCNCKT/TKCS (mỏ nhóm I); từ chối/chuyển nhóm II-III-IV | **tkm-sct-vn** | Nghiệp vụ lõi (SKILL.md III–V) |
| 4 | ĐTM/GPMT, đập thải quặng đuôi, cải tạo phục hồi, đóng cửa mỏ | `bvmt-sct-vn` | Chỉ kiểm tra "đã có ĐTM/GPMT chưa" trong thành phần hồ sơ (B3); nội dung môi trường → bvmt |
| 5 | PCCC công trình mỏ, kho, nhà máy tuyển (thẩm duyệt, nghiệm thu PCCC) | `pccc-sct-vn` | Ghi nhận văn bản thẩm duyệt PCCC trong hồ sơ; phân định thẩm quyền PCCC → pccc |
| 6 | Điều kiện khởi công, KTCTNT, sự cố công trình, cấp công trình, thẩm quyền CQCM xây dựng | `xd-sct-vn` | tkm dùng chung GATE 01/7/2026; câu hỏi thuần xây dựng (giấy phép XD, nghiệm thu) → xd |
| 7 | Giấy phép sử dụng VLNCN + Phương án nổ mìn (PANM) | `sd-vlncn-sct-vn` | Thiết kế khoan nổ mìn TRONG thiết kế mỏ do tkm thẩm định (Chương khoan nổ PL TT 31/2025); hồ sơ GIẤY PHÉP sử dụng VLNCN và PANM → sd-vlncn. Tiền lệ ranh giới: CV Sâu Chua 2019 — SCT "cho ý kiến thông số khoan nổ, sẽ thẩm định khi cấp phép VLNCN" |
| 8 | Kho VLNCN của mỏ: thiết kế, thi công, KTCTNT kho, kiểm định | `kho-vlncn-sct-vn` | Kho VLNCN là hạng mục có chế độ riêng (QCVN 01:2019/BCT) — tkm KHÔNG thẩm định kho theo phụ lục mỏ; chuyển kho-vlncn |
| 9 | Huấn luyện KTAT VLNCN (chỉ huy nổ mìn, thợ mìn, thủ kho) | `hl-vlncn-sct-vn` | Khi thông báo thẩm định yêu cầu "nhân sự đủ điều kiện" → dẫn sang thủ tục của hl-vlncn |
| 10 | Hóa chất tuyển khoáng (nhà máy tuyển dùng xantat, dầu thông, axit...): GCN đủ điều kiện, KH phòng ngừa sự cố | `hc-sct-vn` | Thẩm định thiết kế nhà máy tuyển: phần công nghệ - xây dựng do tkm; điều kiện hoạt động hóa chất → hc |
| 11 | Vận chuyển hàng hóa nguy hiểm (axit, amoniac... phục vụ tuyển) | `hnh-sct-vn` | Lưu ý: vận chuyển VLNCN/TCTN KHÔNG thuộc hnh (giấy phép vận chuyển VLNCN do cơ quan Công an cấp theo pháp luật VLNCN) — chỉ hóa chất nguy hiểm loại khác mới sang hnh |
| 12 | Nhà máy chế biến sâu đặt trong CCN/KCN (thủ tục đầu tư vào cụm, ưu đãi, khởi công trong CCN) | `kccn-sct-vn` | tkm chỉ thẩm định thiết kế phần khai thác mỏ; dự án trong CCN → điều kiện CCN theo kccn |
| 13 | Soạn - render mọi văn bản (.docx), QA thể thức | `vbhc-vn` | Mọi output văn bản của tkm đi qua vbhc Chế độ B, dùng file `vi-du-thuc-te/` làm template gốc |
| 14 | Ai ký, phòng nào chủ trì, dòng Lưu | `sct-laocai-org-vn` | tkm mặc định PGĐ Hoàng Văn Thuân + CN(Dũng); trường hợp lạ (liên phòng, trình GĐ) → tra org |
| 15 | Bài phát biểu, tham luận về khoáng sản/thiết kế mỏ cho Lãnh đạo Sở | `bpb-sct-vn` | tkm cấp chất liệu (số liệu BC 452, dòng thời gian pháp lý, tồn tại - kiến nghị); kết cấu và giọng văn → bpb |

## B. Bốn kịch bản liên plugin hay gặp (chuỗi gọi chuẩn)

**KB1 — "Thẩm định thiết kế mỏ đá/quặng trọn gói":**
`vbhc-pdf-reader` (đọc tờ trình + giấy phép + QĐ trữ lượng) → `tkm` GATE giai đoạn + thẩm quyền → `quy-hoach-ct` (đối chiếu quy hoạch) → `tkm` B3-B4 (checklist + 5 trục, trong đó trục hồ sơ có mục ĐTM/GPMT ↔ `bvmt`, PCCC ↔ `pccc`) → `tkm` B5 dự thảo thông báo → `vbhc` render + QA → `sct-laocai-org` xác nhận ký/Lưu.

**KB2 — "Mỏ mới xin đồng thời nhiều thủ tục" (doanh nghiệp hỏi tổng thể):**
Trả lời theo trình tự: thiết kế (`tkm`) → môi trường (`bvmt`) → xây dựng - khởi công (`xd`) → VLNCN (giấy phép sử dụng `sd-vlncn`; kho `kho-vlncn`; nhân sự `hl-vlncn`) → hóa chất nếu có tuyển (`hc`) → vận chuyển hóa chất (`hnh`). Mỗi mục nêu: căn cứ - thẩm quyền - đầu mối; KHÔNG gộp điều kiện của các domain vào một "danh mục chung" thiếu căn cứ.

**KB3 — "Hậu thanh tra BC 452 / đoàn kiểm tra mỏ":**
`tkm` reference `09` (checklist vi phạm điển hình: thứ tự khai thác, công suất, phạm vi, XDCB mỏ) + reference `08` (ứng xử thanh tra) → phần nổ mìn đối chiếu hộ chiếu - PANM (`sd-vlncn`) → kho (`kho-vlncn`) → môi trường - đóng cửa mỏ (`bvmt`) → biên bản/báo cáo kiểm tra (`vbhc`).

**KB4 — "Tham luận/báo cáo ngành về quản lý khoáng sản":**
Chất liệu: `tkm` reference `01` (dòng thời gian) + `09` (số liệu toàn quốc BC 452, ghi rõ nguồn, không gán cho Lào Cai) + `quy-hoach-ct` (danh mục quy hoạch tỉnh) → kết cấu và giọng (`bpb`) → render (`vbhc`).

## C. Quy tắc chống giẫm chân
1. Một câu hỏi thuộc trọn domain khác → chuyển hẳn plugin đó, tkm không trả lời "tạm".
2. Câu hỏi giáp ranh → tkm trả phần thiết kế mỏ + chỉ rõ "phần X theo thủ tục tại [plugin/lĩnh vực Y, chuyên viên Z]" (chuyên viên: Dũng — thiết kế/kho VLNCN; Khôi — VLNCN/TCTN/HHNH; Loan — hóa chất; Nhung — khoáng sản; M.Long — môi trường; Trung — KCN/CCN; theo `sct-laocai-org-vn`).
3. Dữ liệu hiện trạng (tỷ lệ lấp đầy, tiến độ mỏ, sản lượng) — không plugin nào được bịa; hỏi Bạn.
4. Văn bản pháp luật trùng nhau giữa plugin (NĐ 175/2024→217/2026, Luật 135/2025...): nếu hai plugin ghi khác nhau về số/ngày → DỪNG, báo Bạn đối chiếu bản gốc, không tự chọn.
