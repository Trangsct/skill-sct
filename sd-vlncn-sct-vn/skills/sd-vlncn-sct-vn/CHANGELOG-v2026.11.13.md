# CHANGELOG sd-vlncn-sct-vn v2026.11.13.1 — 13/11/2026

## Nguồn

Doanh nghiệp báo ngày 13/11/2026: Giấy phép số 5890/GP-SCT ngày 21/9/2026 (cấp lại cho Công ty TNHH MTV Duy Cương,
thủy điện Suối Chăn 2) ghi sai mã số doanh nghiệp và sai cơ quan cấp đăng ký kinh doanh tại Điều 1. Rà lại hồ sơ:
cụm nhận dạng được chép từ Giấy phép số 914/GP-UBND ngày 26/8/2025 (đã sai từ 2025), chỉ cập nhật một phần
(ngày đăng ký thay đổi, số điện thoại) theo bản đăng ký kinh doanh mới.

## Thay đổi

- **anti-error 38** (references/11): dữ kiện nhận dạng doanh nghiệp tại Điều 1 đọc từ bản gốc Giấy chứng nhận đăng ký
  doanh nghiệp và viết lại cả cụm; cấm chép từ giấy phép cũ, Giấy đề nghị, Báo cáo sử dụng VLNCN, Phương án nổ mìn
  (cùng sai một nguồn); áp dụng cả hồ sơ cấp lại, cấp điều chỉnh; cơ quan cấp từ 2025 là Phòng Doanh nghiệp và Đăng ký
  kinh doanh - Sở Tài chính; kiểm nhanh đầu mã số theo tỉnh; thêm gạch "Về tư cách pháp nhân" trong Phiếu trình.
- **references/02 mục G mới** — giấy phép đã ban hành có sai sót: chọn hình thức xử lý theo khoản 3 Điều 18
  NĐ 30/2020/NĐ-CP (sai nội dung → văn bản có hình thức tương đương thay thế; sai thể thức, kỹ thuật trình bày →
  công văn đính chính); không dùng thủ tục cấp lại (k2 Đ39) hay cấp điều chỉnh (k3 Đ39) để sửa lỗi của cơ quan.
- **references/07 mục P** — hồ sơ vụ việc: văn bản, chỗ sai, đường đi của lỗi, vì sao đối chiếu chéo không bắt được,
  các văn bản khác của cùng doanh nghiệp cần rà.
- **references/so-loi-tu-ghi.md** — lập sổ lỗi tự ghi của plugin, mục L001.
- **mau-van-ban/01, 02** — ghi chú cảnh báo tại Điều 1; **mau-van-ban/06** — thêm gạch "Về tư cách pháp nhân" vào mục 4.
- **scripts/kiem_tra_dkdn.py** mới: so mã số trong dự thảo .docx với bản Giấy chứng nhận đăng ký doanh nghiệp
  (OCR tiếng Việt khi là bản scan), kiểm đầu mã theo tỉnh của cơ quan cấp, cảnh báo cơ quan cấp lỗi thời.
- SKILL.md: thêm dòng mục lục anti-error 38 và dòng dẫn sổ lỗi tự ghi.

## Bổ sung cùng ngày (bản 2026.11.13.2)

- Bổ sung vào phần xử lý khi giấy phép, giấy chứng nhận đã ban hành mà sai: **hình thức xử lý theo đề nghị bằng văn bản của doanh nghiệp** (Bạn chốt 13/11/2026), Sở không tự chọn thay; chưa có đề nghị thì thông báo chỗ sai và hướng xử lý để doanh nghiệp đề nghị.
