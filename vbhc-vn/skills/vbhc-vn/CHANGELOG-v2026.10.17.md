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
- `tests/baseline-warn.json` cập nhật CÓ CHỦ ĐÍCH: 11 mẫu thật thêm WARN R23 (tổng 36) — mẫu thật dẫn văn bản quy phạm
  chưa có tệp gốc trong kho (ví dụ NĐ 303/2026/NĐ-CP, NĐ 74/2026/NĐ-CP). Đây là thông tin đúng (kho chưa đủ bản gốc),
  không phải bắt nhầm; số WARN tự giảm khi nạp thêm bản gốc. Không mẫu thật nào FAIL.
- `tests/rule-inventory.md`: thêm R23.

## Mục 4 — Tự ghi lỗi

- `reference/so-loi-tu-ghi.md` (mới): sổ lỗi có cấu trúc L001 — ngày — tiêu đề; Lỗi; Cách đúng; Ví dụ; Máy kiểm. Bảng
  reference và mục QA của `SKILL.md`, `HUONG_DAN_CAP_NHAT.md` dẫn quy trình. Nhóm A–O văn xuôi giữ nguyên.

- `plugin.json` → 2.31.0.
