# Báo cáo định kỳ của Phòng QLCN, phụ biểu giao ban và bài phát biểu Trưởng phòng — quy ước chốt 06/9/2026

Nguồn: bộ sản phẩm Bạn duyệt ngày 06/9/2026 (Báo cáo 9 tháng, Báo cáo tháng 9, Phụ biểu tháng 9 phần Phòng QLCN, Bài phát biểu giao ban tháng 9). Mẫu thật lưu tại `examples/sct/` (3 file) và `bpb-sct-vn/kho-bai-mau/` (2 file). Script dựng: `scripts/build_bao_cao_phong.py`.

## 1. Báo cáo định kỳ của Phòng (tháng, 6 tháng, 9 tháng, năm)

**Thể loại:** báo cáo nội bộ Phòng gửi Phòng KH-TH tổng hợp — KHÔNG cấp số, KHÔNG ký hiệu; header trái "SỞ CÔNG THƯƠNG LÀO CAI / PHÒNG QL CÔNG NGHIỆP"; người ký **TRƯỞNG PHÒNG Nguyễn Hữu Long**; Nơi nhận cố định: `- Phòng KH-TH; - GĐ, PGĐ Thuân, PGĐ Chiến; - Lưu: CN Nhung.` (CN Nhung = chuyên viên tổng hợp báo cáo, KHÔNG đổi). Dòng ngày: "Lào Cai, ngày      tháng M năm YYYY" — để trống ngày, tháng = tháng ký (báo cáo tháng 8 ký tháng 9).

**Tiêu đề:** `BÁO CÁO` / `Tình hình thực hiện công tác tháng M năm YYYY,` / `Kế hoạch công tác tháng M+1 năm YYYY`. Bản 6 tháng/9 tháng: `Tình hình thực hiện công tác 9 tháng đầu năm 2026,` / `nhiệm vụ trọng tâm 3 tháng cuối năm 2026`.

**Kết cấu báo cáo tháng (mẫu `bao-cao-thang-phong-qlcn.docx`):**
- I. NHIỆM VỤ HOÀN THÀNH — đoạn mở đầu cố định ("Thực hiện nhiệm vụ được phân công, trong tháng M năm YYYY (đến thời điểm báo cáo), Phòng Quản lý Công nghiệp đã bám sát chỉ đạo của Tỉnh ủy, UBND tỉnh, Ban Giám đốc Sở… Kết quả cụ thể như sau:"), rồi 9 mục theo lĩnh vực: 1. Khoáng sản (a) QLNN, b) SXKD của doanh nghiệp); 2. VLNCN, tiền chất thuốc nổ và vận chuyển HHNH; 3. Hóa chất; 4. Khu công nghiệp, cụm công nghiệp; 5. Phát triển công nghiệp, công nghiệp hỗ trợ và khuyến công; 6. ATTP; chất lượng sản phẩm; 7. Bảo vệ môi trường; 8. PCTT, PCCN, CNCH và an toàn; 9. Lĩnh vực khác.
- II. KHÓ KHĂN, VƯỚNG MẮC — 2–3 đoạn văn xuôi (khoáng sản; hồ sơ CCN; khối lượng công việc).
- III. KẾ HOẠCH CÔNG TÁC THÁNG M+1 — danh sách 1., 2., … (13–17 việc), việc cuối luôn "Thực hiện các nhiệm vụ thường xuyên của Phòng và các nhiệm vụ đột xuất khác do Lãnh đạo Sở giao."

**Kết cấu báo cáo 9 tháng (mẫu `bao-cao-9-thang-phong-qlcn.docx`):** I. Nhiệm vụ hoàn thành (10 mục — thêm mục 10 "Kết quả tham mưu ban hành văn bản, giải quyết TTHC" với số liệu đếm từ sổ văn bản đi) → II. Khó khăn, vướng mắc (theo lĩnh vực, đánh số 1–7) → III. Một số giải pháp chủ yếu (theo lĩnh vực; mục CCN dùng "Một là/Hai là/Ba là/Bốn là") → IV. Nhiệm vụ trọng tâm 3 tháng cuối năm (18 việc).

**Nguồn số liệu bắt buộc và cách đếm (Bạn chốt):**
- Sổ văn bản đi Data360X (xuất .xlsx): lọc cột "Đơn vị soạn thảo" = "Phòng Công nghiệp"; đếm theo phần ký hiệu sau số (`/SCT-CN`, `/QĐ-SCT`, `/BC-SCT`, `/TTr-SCT`, `/2026/GCNATTP-SCTLC`, `/GP-SCT`, `/GM-SCT`, `/KH-SCT`, `/TB-SCT`); bỏ dòng trống. Giấy phép GP-SCT tách VLNCN (trích yếu có "nổ"/"VLNCN") và HHNH (trích yếu có "vận chuyển"/"HHNH"). Ghi trong báo cáo dạng: "1.383 văn bản, gồm: 898 công văn, 188 quyết định, 71 báo cáo, 69 tờ trình, 41 GCN ATTP, 35 giấy phép (25 GP vận chuyển HHNH, 08 GP sử dụng VLNCN, 02 giấy phép khác)…".
- Bảng giấy phép sử dụng VLNCN (`gp_su_dung_vlncn_*.xlsx`, 2 sheet còn hiệu lực/hết hiệu lực): số cấp trong kỳ = đếm theo ngày cấp; tách GP-UBND (trước ủy quyền) và GP-SCT (từ 20/8/2026 theo QĐ 2867/QĐ-UBND ngày 17/8/2026); số còn hiệu lực = số dòng sheet 1.
- Số liệu Bạn cung cấp trong chat (vd hóa chất "lũy kế 8 tháng…") giữ NGUYÊN mốc kỳ Bạn ghi, không tự cộng thêm tháng sau; việc phát sinh tháng sau ghi thành câu riêng ("Trong tháng 9 đã trình…").
- Hiện trạng mỏ (12/45 chưa sản xuất, 11/45 tạm dừng, 22 đang hoạt động) lấy từ báo cáo tháng gần nhất, không lấy từ skill.

**Thể thức (đã chốt sau 3 vòng sửa):** xem docstring `scripts/build_bao_cao_phong.py`. Điểm quan trọng: KHÔNG dùng giãn dòng "Exactly" trong thân — Word tính khác LibreOffice, tạo khoảng trống nửa trang cuối trang (vụ 06/9/2026 trang 15 Báo cáo 9 tháng) và lệch số trang; dùng giãn dòng đơn + after 3pt + widowControl. Header 13pt (Quốc hiệu và tên cơ quan chủ quản 12pt) để mỗi dòng gọn 1 dòng; Line VML `from="0,23pt"` cho paragraph 19pt.

## 2. Phụ biểu theo dõi, đánh giá kết quả nhiệm vụ giao ban (phần Phòng QLCN)

Mẫu `examples/sct/phu-bieu-danh-gia-nhiem-vu-giao-ban-qlcn.docx` (khổ ngang, bảng 7 cột: Lãnh đạo phụ trách | Phòng/Đơn vị | Công việc cụ thể được giao | Hoàn thành | Đang triển khai | Chưa thực hiện | Ghi chú). Phòng QLCN có 2 khối: "5. Ông Hoàng Văn Thuân (PGĐ 3)" và "6. Ông Nguyễn Đình Chiến (PGĐ 4)", cột 1–2 gộp dọc (vMerge) theo khối.

Quy ước:
- Cột "Công việc cụ thể được giao" chép NGUYÊN VĂN nhiệm vụ từ báo cáo giao ban kỳ trước của Sở (mục "Nhiệm vụ, giải pháp trong thời gian tới") + nhiệm vụ Lãnh đạo Sở/Trưởng phòng giao thêm (tin nhắn Zalo) — mỗi nhiệm vụ 1 dòng.
- Đánh dấu "X" đúng 1 trong 3 cột; căn giữa ngang + dọc.
- Ghi chú phải dẫn số, ngày văn bản kết quả (Tờ trình, Quyết định, Văn bản, Báo cáo) từ sổ văn bản đi; nhiệm vụ nhiều đầu việc thì tách "Đã… / Đối với…". Không viết chú thích biên tập ("đề nghị bổ sung số…") vào ô — ghi ngoài chat.
- Phông chữ trong bảng thống nhất Times New Roman 12pt, tiêu đề 13pt; KHÔNG highlight/nền màu (file gốc của Phòng có nền vàng đánh dấu — phải gỡ `w:highlight`); dòng tiêu đề bảng `tblHeader` lặp mọi trang; gỡ `trHeight` cố định ở dòng nội dung; lề ô 80 dxa.
- Chỉ dựng phần Phòng QLCN; không bịa kết quả của phòng khác — Bạn dán vào biểu tổng hợp của Phòng KH-TH.

## 3. Bài phát biểu Trưởng phòng tại giao ban Sở (xem `bpb-sct-vn`)

Mẫu `bpb-sct-vn/kho-bai-mau/bpb-giao-ban-thang-9-2026-truong-phong-qlcn.docx` (bản Bạn sửa tay 06/9/2026): tiêu đề `BÀI PHÁT BIỂU` / `tại cuộc họp giao ban tháng M năm YYYY của Sở Công Thương`; kính thưa 3 dòng (Giám đốc chủ trì, các PGĐ, toàn thể đồng chí dự họp); mở đầu "Thay mặt Phòng Quản lý Công nghiệp, tôi xin báo cáo … ba nội dung"; **kết quả lồng ghép theo TỪNG LĨNH VỰC**: mỗi ý "Thứ …, về …:" nêu lũy kế 9 tháng trước rồi nối kết quả tháng gần nhất của chính lĩnh vực đó (Bạn chốt cách lồng ghép này thay vì tách 2 phần); nhiệm vụ tháng sau "Một là/Hai là/Ba là"; khó khăn - đề xuất "Thứ nhất/Thứ hai" (đề xuất đúng cấp: với PGĐ phụ trách, Giám đốc); kết cam kết "rõ người, rõ việc, rõ thời hạn" + cảm ơn. Bạn yêu cầu: bài phát biểu KHÔNG nhắc vận chuyển hàng hóa nguy hiểm; không đưa nội dung Nghị quyết 66.25/2026/NQ-CP vào bài giao ban; nhiệm vụ đã do PTP khác hoàn thành (vd 3 kế hoạch CNHT, CN sinh học, KL 83-KL/TW do PTP Đỗ Mạnh Cường) phải chuyển sang phần kết quả, không để ở phần nhiệm vụ.
