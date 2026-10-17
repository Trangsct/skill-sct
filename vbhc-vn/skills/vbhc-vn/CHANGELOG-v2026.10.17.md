# CHANGELOG — vbhc-vn v2.31.0 (17/10/2026)

Nguồn: bản giao việc nâng cấp hệ plugin 17/10/2026 (mục 1 GATE 0, mục 2 GATE 0b, mục 3 GATE cuối, mục 4 tự ghi lỗi).
Nguyên tắc tốc độ của bản giao việc: kế hoạch, dàn ý, rà soát chạy ngầm, chỉ báo kết quả gọn; tối đa một lần hỏi mỗi phiên.

## Mục 1 — GATE 0 Kế hoạch soạn thảo

- `SKILL.md`: mục mới "GATE 0 — Kế hoạch soạn thảo" đặt trước mọi GATE (a–f: loại văn bản, người ký, ký hiệu; nơi nhận;
  căn cứ kèm nguồn — không nguồn thì không đưa vào; số liệu kèm nguồn; điểm thiếu; tự tìm trong kho trước, không thấy thì
  bôi tím, chỉ hỏi khi chỗ thiếu quyết định toàn bộ nội dung). Kế hoạch ghi `ke-hoach-soan.txt`, không gửi Bạn duyệt;
  văn bản dưới một trang đủ dữ kiện thì bỏ qua tệp kế hoạch. Mẫu `templates/ke-hoach-soan-mau.txt` (gõ thẳng, không markdown).
- `qa_rules.py` **R23 (WARN)**: số hiệu văn bản quy phạm dạng số/năm/ký hiệu phải khớp tệp gốc trong kho (sổ cái
  `00-DANH-MUC-CHUNG.md` / `DANH-MUC-VAN-BAN-GOC.csv` — cùng nguồn với `tim_van_ban.py` lớp 1) hoặc căn cứ Bạn gửi trong
  phiên (`can-cu-phien.txt`, dòng có nguồn trong `ke-hoach-soan.txt`, biến `VBHC_CAN_CU_PHIEN`). Chạy trong `qa_all.py` mục 1b.
- `tests/test_gate0.py` (mới; `run_regression.py` gọi ở mục 5) + `tests/fail/r23-so-hieu-qppl-chua-co-nguon.docx`
  (câu chèn lấy nguyên từ mẫu thật phiếu trình UBND, không bịa số hiệu).
- `tests/baseline-warn.json` cập nhật CÓ CHỦ ĐÍCH: 10 mẫu thật thêm WARN R23 (tổng 33) — mẫu thật dẫn văn bản quy phạm
  chưa có tệp gốc trong kho (ví dụ NĐ 303/2026/NĐ-CP, NĐ 74/2026/NĐ-CP). Đây là thông tin đúng (kho chưa đủ bản gốc),
  không phải bắt nhầm; số WARN tự giảm khi nạp thêm bản gốc. Không mẫu thật nào FAIL.
- `tests/rule-inventory.md`: thêm R23.

## Mục 2 — GATE 0b Dàn ý

- `SKILL.md`: mục "GATE 0b — Dàn ý" (văn bản từ 3 trang hoặc báo cáo, kế hoạch, đề án, phương án nổ mìn, đánh giá rủi ro,
  ứng cứu khẩn cấp, bài phát biểu, tờ trình kèm dự thảo): lập dàn ý theo dàn ý mặc định hoặc mẫu gần nhất, ghi
  `ke-hoach-soan.txt`, viết thân ngay; chỉ gửi dàn ý khi Bạn yêu cầu hoặc loại chưa có mẫu; giao file báo một dòng.
- `reference/dan-y-mac-dinh.md` (mới): 14 loại văn bản, mọi dàn ý lấy nguyên từ mẫu thật, mẫu văn bản, văn bản gốc trong kho
  (Phụ lục VI, VII, IX TT 23/2024/TT-BCT; bpb-sct-vn mục 3; kccn mẫu 02, 04, ref 44; Kế hoạch BT2 v11; Đề án 13).
- Dẫn chiếu chéo: bpb-sct-vn 1.6.0, kccn-sct-vn 1.51.0, dacn-sct-vn 1.10.0, sd-vlncn-sct-vn 2026.10.17.1.

## Mục 3 — GATE cuối Rà soát độc lập

- `SKILL.md`: mục "GATE cuối — Rà soát độc lập": sau khi dựng xong, hai việc chạy SONG SONG — Claude chạy một lệnh
  `kiem_tra_truoc_khi_giao.py --tu-sua`, tác tử phụ chưa tham gia soạn (chạy nền) đối chiếu checklist bằng số đo của
  script, không sửa file; lỗi hình thức Claude tự sửa bằng script, lỗi nội dung nêu gọn kèm hướng xử lý; tối đa 2 vòng;
  không có công cụ tác tử phụ thì ghi "rà soát không độc lập". Bảng QA thêm hai dòng.
- `scripts/checklist_ra_soat.txt` (mới, gõ thẳng): 30 điểm — 11 hình thức (máy sửa được), 19 nội dung; mỗi điểm dẫn số đo
  [n] của script hoặc "mắt", kèm nguồn (Quy tắc, Nhóm A–O, R-mã, Bạn chốt 17/10/2026).
- `scripts/ra_soat_doc_lap.py` (mới): 16 số đo — phông từng run (kể cả kiểu, theme); cỡ chữ Nơi nhận; dòng trống sau Kính
  gửi, trước khối ký, ô ký so với Nơi nhận; trang gần trống (dùng lại PDF của qa_all.py); "UBND" trong thân; quy ước số 0
  ngày tháng; nền, căn dọc ô bảng; dấu vết chỉnh sửa; dòng Số; Ban Quản lý Khu kinh tế ↔ Ban Quản lý các KCN; tên cụm gộp
  số; Nơi nhận văn bản thủ tục hành chính; giao việc cho Phòng QLCN; chữ tím; "Kính thưa" giữa bài; R23.
- `scripts/kiem_tra_truoc_khi_giao.py` (mới): một lệnh gộp `qa_all.py` + `cite_check.py` + `ra_soat_doc_lap.py` (dùng lại
  PDF, không render lần hai); `--tu-sua` (chuan_hoa_xuat_ban.py, một dòng trống sau Kính gửi, bảng nền trắng căn giữa
  dọc, dòng Lưu bỏ tên chuyên viên), tối đa 2 vòng. **Thời gian đo: 1,5 giây** trên công văn mẫu 2 trang
  (`examples/sct/cong-van-de-nghi-bo-sung-ho-so.docx`), mục tiêu < 30 giây.
- `reference/so-loi-tu-ghi.md` L001 (17/10/2026): sau "Kính gửi" cách 1 dòng; ô ký cao tương ứng khối Nơi nhận. Bảng
  Nhóm G trong SKILL.md thêm vế này.
- `tests/test_ra_soat.py` (mới; `run_regression.py` mục 6): đo đúng, tự sửa đúng, không sinh FAIL mới, dưới 30 giây.

## Mục 4 — Tự ghi lỗi

- `reference/so-loi-tu-ghi.md` (mới): sổ lỗi có cấu trúc L001 — ngày — tiêu đề; Lỗi; Cách đúng; Ví dụ; Máy kiểm. Bảng
  reference và mục QA của `SKILL.md`, `HUONG_DAN_CAP_NHAT.md` dẫn quy trình. Nhóm A–O văn xuôi giữ nguyên.

- `plugin.json` → 2.31.0.
