# Sổ lỗi tự ghi — sd-vlncn-sct-vn

Lỗi Bạn chỉ ra trong phiên, Claude ghi ngay theo CLAUDE.md mục "Tự ghi lỗi" (Bạn chốt 17/10/2026). Đọc tệp này trước khi
soạn văn bản thuộc lĩnh vực của plugin. Định dạng mỗi mục và cách kiểm: `scripts/check_anti_error_format.py` ở gốc kho.
Lỗi kiểm được bằng máy thì kèm quy tắc trong `qa_rules.py` (vbhc-vn) hoặc `check_facts.py` và ghi mã ở dòng "Máy kiểm".
Yêu cầu riêng cho MỘT văn bản không ghi ở đây mà ghi vào `trang-thai/<hồ sơ>.md` mục "Yêu cầu riêng một lần".

### L001 — 13/11/2026 — Cấp sai mã số doanh nghiệp tại Điều 1 Giấy phép sử dụng VLNCN

- Lỗi: Điều 1 Giấy phép cấp lại ghi mã số doanh nghiệp và cơ quan cấp chép từ giấy phép đã cấp năm trước (mã sai sẵn từ đó), trong khi ngày đăng ký thay đổi và số điện thoại lại cập nhật theo bản đăng ký kinh doanh mới — sửa một phần của câu nên phần sai ở lại. Doanh nghiệp phát hiện và báo lại sau khi nhận giấy phép.
- Cách đúng: đọc một lượt từ bản đăng ký kinh doanh gốc trong hồ sơ và viết lại CẢ cụm nhận dạng (tên, loại hình, mã số, cơ quan cấp, ngày đăng ký lần đầu, lần thay đổi gần nhất, trụ sở, điện thoại). Không lấy mã số từ giấy phép cũ, Giấy đề nghị, Báo cáo sử dụng VLNCN hay Phương án nổ mìn — các tài liệu đó thường chép lại giấy phép cũ nên cùng sai một nguồn. Bản đăng ký cấp từ 2025 do Phòng Doanh nghiệp và Đăng ký kinh doanh - Sở Tài chính cấp, không còn Sở Kế hoạch và Đầu tư. Hồ sơ cấp lại, cấp điều chỉnh tuy không bắt buộc nộp bản này vẫn phải có bản gốc để đối chiếu.
- Ví dụ: giấy phép ghi mã mở đầu bằng dải của tỉnh này nhưng câu lại ghi cơ quan đăng ký của tỉnh khác cấp — mâu thuẫn thấy được ngay trên mặt văn bản.
- Máy kiểm: `scripts/kiem_tra_dkdn.py` (so mã số trong dự thảo với bản gốc, kiểm đầu mã theo tỉnh, cảnh báo "Sở Kế hoạch và Đầu tư" với bản cấp từ 2025); anti-error 38.

