## [2.25.0] - 18/9/2026 — R16 khối Kính gửi + build_vb.py dựng đúng khoảng cách khối

- **Nguồn:** vụ thật 18/9/2026 — bản công văn góp ý dự thảo QCVN 03:2026/BCA xuất ra cho Bạn bị lỗi trình bày: chỉ gửi một cơ quan (Công an tỉnh) nhưng "Kính gửi:" và tên cơ quan nằm hai dòng lệch nhau (giữ lại bảng 2 ô của mẫu gửi nhiều cơ quan), lại không cách một dòng với khối trích yếu phía trên và khối thân phía dưới; khối ký cũng không cách thân đúng một dòng. Bạn chỉ ra trực tiếp trên bản Word.
- **qa_rules.py — R16 (mới, FAIL)**: khối Kính gửi — gửi MỘT cơ quan thì "Kính gửi: <tên>." trên cùng một dòng; gửi nhiều cơ quan mới tách "Kính gửi:" lên trên, danh sách "- A;" … "- Z." xuống dưới; không để khối trống không có nơi nhận. Nhận được cả ba cách trình bày của mẫu thật (paragraph căn giữa, bảng 2 ô, danh sách trong cùng ô). Điều kiện bắt lỗi dựa vào dấu gạch đầu dòng nên 26/26 mẫu thật sạch.
- **build_vb.py**: dòng `[K]` không đi vào thân nữa mà dựng khối Kính gửi riêng theo SỐ nơi nhận — một nơi nhận thì xóa bảng của mẫu, thay bằng một dòng căn giữa, giữ đúng một dòng trống trên/dưới; nhiều nơi nhận thì điền danh sách vào ô phải của bảng. Thêm chuẩn hóa khối ký cách thân đúng một dòng trống. Thân văn bản không ghi lên dòng trống ngăn cách nữa.
- **normalize_body.py**: giữ 1 đoạn trống dưới trích yếu + **1** đoạn trống trước khối ký (trước đây 2).
- **tests/fail/r16-kinh-gui-tach-dong-mot-noi-nhan.docx** (file lỗi THẬT, không phải nhân tạo) + `.expect`; `run_regression.py` xanh: 26 mẫu thật 0 FAIL, 17 file lỗi bắt đúng mã.

