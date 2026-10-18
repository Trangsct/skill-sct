# CHANGELOG — vbhc-vn v2.34.0 (18/10/2026) — chuyển từ PR 116

Chuyển nội dung PR 116 (nhánh `vbhc-2.29.0-nhom-p-r19-r20`, Bạn chốt 04/10/2026 qua 6 vòng sửa Kế hoạch của UBND tỉnh về
công nghiệp khai thác và tinh chế nguyên liệu phục vụ công nghệ chiến lược — Bài toán lớn số 2 — sau CV 9958/UBND-NC ngày
30/9/2026 trả về "chưa đạt") lên bản hiện tại. Mã quy tắc của nhánh (R19, R20) đổi thành **R24, R25** vì main đã dùng
R19 (phông), R20 (Nơi nhận cỡ 11), R21–R23.

- **R25** (mã cũ R20 của nhánh): Nơi nhận xếp theo vị thế cơ quan nhà nước (cấp trên b/c → sở ngành → ngành dọc → UBND
  xã, phường → doanh nghiệp → Văn phòng → Lưu); doanh nghiệp chung dòng với cơ quan nhà nước → FAIL (vụ "Chi cục Hải quan
  khu vực VII; Công ty Điện lực Lào Cai"); cơ quan nhà nước đứng sau doanh nghiệp → WARN. Ca thử
  `tests/fail/r25-doanh-nghiep-chung-dong-co-quan`. Bổ sung cho R06, R22. Baseline WARN cập nhật có chủ đích: mẫu thật
  `examples/ubnd/thong-bao-ket-luan-ubnd.docx` (VP UBND tỉnh) có 1 WARN R25 (Công ty Điện lực Lào Cai đứng trước Ban QLDA,
  UBND xã) — mẫu thật là chuẩn nên chỉ WARN, không FAIL.
- **R24** (mã cũ R19 của nhánh) — **phạm vi đã thu hẹp**: nhánh viết "Ủy ban nhân dân" → "UBND" ở căn cứ, thân, nơi nhận,
  phụ lục; nhưng main 17/10/2026 (checklist rà soát độc lập dòng 12, `ra_soat_doc_lap.py` mục [5]) chốt thân văn bản viết
  ĐẦY ĐỦ. Hai quy tắc giữ ở phạm vi của mình: R24 chỉ bắt (WARN) ở **khối Nơi nhận** và **ô bảng phụ lục, danh mục** (bảng
  ≥ 3 cột, không phải bảng header hay bảng ký); thân, Kính gửi không thuộc R24; **phần căn cứ chưa xác định được phạm vi —
  chờ Bạn chốt** (ghi ở Nhóm P9, checklist dòng 12). 0 WARN mới trên 26 mẫu thật. Ca thử
  `tests/fail/r24-uy-ban-nhan-dan-viet-du-chu-noi-nhan` (dựng lại từ mẫu thật giấy phép HHNH, không dùng file lỗi của
  nhánh vì phạm vi đã đổi).
- **Nhóm P** mới trong `reference/phong-tranh-sai-lam.md` (16 nhóm A–P): kế hoạch UBND tỉnh triển khai đề án, bài toán lớn —
  P1 bám đề bài không nhắc tên văn bản cấp tỉnh cũ trong thân, căn cứ rút gọn 4 nhóm; P2 bỏ câu ghi chú làm việc; P3 chỉ
  tiêu phụ thuộc doanh nghiệp, Trung ương ghi phấn đấu đồng bộ; P4 việc ngoài thẩm quyền tỉnh là "đề xuất", tiêu chí là
  "định hướng"; P5 không đặt điều kiện tự chặn mục tiêu; P6 mục đích, yêu cầu, quan điểm theo mẫu kế hoạch đã duyệt; P7 thứ
  tự bám đề bài; P8 giao đúng Ban Quản lý theo địa bàn, mở nguồn sự nghiệp kinh tế; P9 bản trình ký duy nhất (kèm ghi chú
  phạm vi "UBND"). Dòng [P] vào checklist trước khi trình.
- `reference/cong-thuc-thuc-chien.md`: hai mục mới — phụ lục bảng của kế hoạch (tiêu đề một đoạn, cột cơ quan ≥ 3,5 cm,
  `cantSplit`, viết tắt trong bảng) và khối ký cùng trang với phần kết (chuỗi `keep_with_next`, 5 bước xử lý, đo fill%
  bằng pdfplumber).
- SKILL.md: bảng A–P (16 nhóm), dòng G ghép "Nơi nhận theo vị thế, doanh nghiệp riêng dòng sau cùng" và phạm vi "UBND";
  dòng P; định tuyến Kế hoạch trỏ Nhóm P; R01–R25. `scripts/checklist_ra_soat.txt` dòng 12 ghi rõ phạm vi.
  `tests/rule-inventory.md` thêm R24, R25, dòng loại N cho P1–P8. `tests/tao_file_loi.py` thêm 2 ca (27 file lỗi).
  `reference/so-loi-tu-ghi.md` L002, L003.
- Kèm theo ở gốc kho: `scripts/check_facts.py` rule WARN `ubnd-viet-tat-noi-nhan-trong-mau` — chỉ quét dòng Nơi nhận
  "- Ủy ban nhân dân tỉnh … (b/c)" trong mẫu .md (phạm vi rõ); không quét thân. dacn-sct-vn 1.11.0 (ref 11 bản trình ký
  04/10/2026), `trang-thai/bai-toan-lon-so-2.md`.
- KHÔNG chuyển: `registry/` và `marketplace.json` của nhánh (sinh lại bằng script theo quy trình chung).
- `plugin.json` → 2.34.0.
