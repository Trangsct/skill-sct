# CHANGELOG — vbhc-vn v2.32.0 (17/10/2026, đợt 2)

Sửa các lỗi có từ trước, phát hiện khi kiểm thử tổng thể bản giao việc 17/10/2026 (Bạn yêu cầu "sửa luôn").

- **SIGSPLIT (khối ký gãy trang) — `qa_pdf_check.check_sig_split`**: viết lại theo khối ký thật trong file .docx (ô bảng
  chứa chức danh ký, hoặc đoạn chức danh viết hoa cuối văn bản): tìm trang có tên người ký và trang có dòng chức danh đầu
  khối; khác trang mới là gãy. Hai lỗi cũ: (1) báo nhầm mọi văn bản có phụ lục sau khối ký (4 file lỗi + mẫu thật
  cong-van-moi-hop-sct báo FAIL khi render); (2) bỏ sót khi "KT. GIÁM ĐỐC" ở trang 1 còn "PHÓ GIÁM ĐỐC" + tên sang trang 2.
  File không có khối ký nhận dạng được (phụ biểu, biên bản ký nhiều bên) → WARN "kiểm tra thủ công", không còn FAIL.
  `qa_all.py` truyền đường dẫn .docx vào hàm. Thử: `tests/test_sigsplit.py` (run_regression.py mục 7, không cần LibreOffice).
- **`cite_check.py`**: tra thêm sổ cái văn bản gốc (`00-DANH-MUC-CHUNG.md` / `DANH-MUC-VAN-BAN-GOC.csv`) — trước chỉ tra
  sổ đăng ký trạng thái nên TT 23/2024/TT-BCT, TT 32/2019/TT-BCT… có bản gốc trong kho vẫn bị báo "chưa có".
- **`build_vb.py`**: (1) thẻ `[[…]]` trong dòng nội dung → chữ TÍM 7030A0 (Quy tắc 27(c)) — trước phải tự tách run;
  (2) "Kính gửi" một nơi nhận không thêm dấu chấm cuối (Nhóm G; 6/8 mẫu thật không chấm); (3) dựng xong in nhắc
  trích yếu, dòng ngày, người ký, Nơi nhận vẫn là của mẫu — qa_rules PASS không có nghĩa các phần đó đã đúng.
- Hồi quy lớp 1 xanh hoàn toàn trên máy phiên (trước còn 4 dòng SIGSPLIT báo nhầm trên file lỗi có phụ lục).
- `plugin.json` → 2.32.0.
