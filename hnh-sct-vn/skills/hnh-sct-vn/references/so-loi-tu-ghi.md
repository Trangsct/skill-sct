# Sổ lỗi tự ghi — hnh-sct-vn

Lỗi Bạn chỉ ra trong phiên, Claude ghi ngay theo CLAUDE.md mục "Tự ghi lỗi" (Bạn chốt 17/10/2026). Đọc tệp này trước khi
soạn văn bản thuộc lĩnh vực của plugin. Định dạng mỗi mục và cách kiểm: `scripts/check_anti_error_format.py` ở gốc kho.
Lỗi kiểm được bằng máy thì kèm quy tắc trong `qa_rules.py` (vbhc-vn) hoặc `check_facts.py` và ghi mã ở dòng "Máy kiểm".
Yêu cầu riêng cho MỘT văn bản không ghi ở đây mà ghi vào `trang-thai/<hồ sơ>.md` mục "Yêu cầu riêng một lần".

### L001 — 02/11/2026 — Công văn hoàn thiện hồ sơ viết dài, phân tích chi tiết từng điểm
- Lỗi: công văn hoàn thiện hồ sơ cấp Giấy phép vận chuyển dầu diesel (loại 3) dài 3,5 trang; mỗi điểm trích nguyên văn hồ sơ doanh nghiệp, giải thích quy định thành đoạn, liệt kê chi tiết kỹ thuật (số khoang xi téc, số chuyến, danh mục nghĩa vụ khi vận chuyển) rồi mới đề nghị. Bạn yêu cầu nâng cấp "theo giọng văn UBND tỉnh, tổng quan hơn, không quá chi tiết".
- Cách đúng: giọng văn chỉ đạo, khoảng 2 trang; mỗi ý là một yêu cầu trực tiếp mở bằng động từ kèm điều khoản; hiện trạng hồ sơ nêu gọn trong ngoặc cuối ý; phân tích chi tiết để ở Biên bản thẩm định, Phiếu trình (nguyên tắc 29, mẫu `mau-ho-so/Mau 9`).
- Ví dụ: "- Xác định cụ thể điểm nhận hàng, điểm giao hàng, lộ trình theo các tuyến đường đi qua và thời gian vận chuyển; bảo đảm hành trình không đi qua công trình hầm có chiều dài từ 100 m trở lên, không qua phà theo Điều 11 Nghị định số 161/2024/NĐ-CP (Phương án hiện chỉ liệt kê tên các xã, phường)."
- Máy kiểm: không (loại N, giọng văn tổng thể); tên nơi nộp kiểm bằng rule `hnh-ten-he-thong-nop-ho-so` của `check_facts.py`.
