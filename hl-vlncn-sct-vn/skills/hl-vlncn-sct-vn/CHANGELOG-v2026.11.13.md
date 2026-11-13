# CHANGELOG hl-vlncn-sct-vn v1.7.0 — 13/11/2026

## Nguồn

Vụ ngày 13/11/2026: Giấy phép sử dụng vật liệu nổ công nghiệp ghi sai mã số doanh nghiệp tại Điều 1 do chép cụm nhận dạng
từ giấy phép đã cấp năm trước và chỉ cập nhật một phần của câu; doanh nghiệp phát hiện sau khi nhận giấy phép. Bạn yêu cầu
ghi quy tắc này vào mọi plugin có việc cấp giấy phép, giấy chứng nhận.

## Thay đổi

- SKILL.md: thêm khối **GATE cấp Giấy phép, Giấy chứng nhận — đúng thông tin, đúng mẫu**, áp dụng khi dựng Giấy chứng nhận huấn luyện kỹ thuật an toàn VLNCN, tiền chất thuốc nổ:
  (1) dữ kiện nhận dạng tổ chức đọc từ bản gốc đăng ký kinh doanh, viết lại cả cụm, cấm chép từ bản cũ và từ hồ sơ doanh nghiệp,
  cơ quan cấp từ 2025 là Sở Tài chính, kiểm nhanh đầu mã số theo tỉnh; (2) dựng đúng mẫu tại văn bản quy phạm, không tự sáng tạo;
  (3) đã ban hành mà sai thì xử lý theo khoản 3 Điều 18 Nghị định số 30/2020/NĐ-CP, không dùng thủ tục cấp lại hay cấp điều chỉnh
  để sửa lỗi của cơ quan.
- `scripts/kiem_tra_dkdn.py`: script kiểm mã số doanh nghiệp trong dự thảo với bản gốc đăng ký kinh doanh (OCR bản scan),
  kiểm đầu mã theo tỉnh và cảnh báo cơ quan cấp lỗi thời.
