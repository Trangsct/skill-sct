# Nhật ký thay đổi bộ skill

## 2026-07-05 (đợt 2) — Đưa 6 plugin lên repo + chuẩn hóa kiểu lưu "gói trong thư mục"
- **Chuẩn hóa cấu trúc repo**: mỗi plugin nay lưu dạng `<tên>/.claude-plugin/plugin.json` + `<tên>/skills/<tên>/...` (zip lại từng thư mục là ra file upload được ngay, không phải bọc thủ công — tránh lỗi validation upload). Chuyển `vbhc-vn` và `hnh-sct-vn` từ kiểu phẳng cũ sang kiểu gói.
- **Thêm mới**: hc-sct-vn v1.0.1, xd-sct-vn v1.1.0, hl-vlncn-sct-vn v1.0.0, sd-vlncn-sct-vn v2026.7.4.2, kho-vlncn-sct-vn v1.4.0.
- **Cập nhật**: hnh-sct-vn → v1.1.0 (thẩm quyền loại 5+8 theo TT 26/2026); vbhc-vn giữ v2.0.1.
- Nắn lại 2 gói bị bọc lệch (hc-sct-vn, sd-vlncn-sct-vn) về đúng chuẩn; dọn __pycache__/.DS_Store.

## 2026-07-05 — vbhc-vn: nâng cấp v2.0.0 → v2.0.1 (chuẩn plugin + vá SZ13 tận gốc)
- **v2.0.0**: chuyển chuẩn plugin; 4 quy tắc bất biến mới (11: cấm gán run.text vào run neo shape Line; 12: dòng Số/Ngày 13pt tường minh, ngày in nghiêng; 13: cấm widow word; 14: khối ký không gãy trang); nâng 7 → 8 nhóm anti-error; thêm `scripts/qa_pdf_check.py` (QA tự động 4 kiểm tra); sửa CỘNG HOÀ→CỘNG HÒA + en dash tiêu ngữ 4 template; chèn Line thiếu vào template 07; check_document bổ sung 10 VBQPPL hết hiệu lực; đổi tên 2 file reference bỏ dấu cách; thêm CHANGELOG riêng của plugin.
- **v2.0.1**: `fill_template.py` gán text vào run chủ đạo (text dài nhất) giữ 13pt tường minh khi điền template; vá 7/9 template gốc thiếu `w:sz=26` ở dòng Số/Ngày (01,02,03,04,05,07,08); `qa_pdf_check.py` guard đầu vào .docx báo lỗi thân thiện khi truyền nhầm PDF; rút gọn demo công văn cho khối ký trọn trang 1. Kiểm chứng: 3 demo → 3/3 QA PASS, render soi ảnh đạt thể thức.

## 2026.07.02 — Khởi tạo kho + đợt cập nhật từ rà soát tuần 30/6–2/7
- **vbhc-vn**: nâng 5 → 7 nhóm sai lầm (thêm Nhóm F — không rebuild file người dùng tải lên; Nhóm G — thể thức chi tiết từ chỉnh sửa tay); thêm `reference/cong-cu-ky-thuat.md` (RAR/OCR/docx/QA); rút gọn description dưới 1024 ký tự.
- **kcn-ccn-vn**: thêm `references/18-hien-trang-cap-nhat.md` (file hiện trạng động có dấu thời gian + bảng mốc hạn); quy tắc 7 mới về sử dụng hiện trạng; nguyên tắc xử lý song song CCN chưa có QĐ thành lập (7b); ĐVSNCL làm chủ đầu tư hạ tầng (7c).
- **hnh-sct-vn**: cảnh báo PGĐ ký KT. GĐ theo ủy quyền đích danh QĐ 1696 + yêu cầu Điều 14 Luật 72/2025 (ref 01); tiền lệ Phương Nam xe biển Trung Quốc / giấy phép loại D NĐ 158/2024 (ref 07); checklist rà dự thảo Giấy phép mục 7b (ref 03).

## 2026-07-04 — vbhc-vn
- Bổ sung VĂN BẢN GỐC 3 Phụ lục Nghị định 30/2020/NĐ-CP vào `reference/`:
  - `nd30-phu-luc-1-the-thuc.md`: Phụ lục I — thể thức, kỹ thuật trình bày VBHC và bản sao (cỡ chữ, kiểu chữ, sơ đồ ô, bảng mẫu chữ Mục V).
  - `nd30-phu-luc-2-viet-hoa.md`: Phụ lục II — quy tắc viết hoa trong VBHC.
  - `nd30-phu-luc-3-viet-tat-mau.md`: Phụ lục III — bảng chữ viết tắt tên loại văn bản + mô tả mẫu trình bày.
- SKILL.md: thêm chỉ dẫn tra 3 file trên (khi nào đọc file nào), rút gọn description ≤1024 ký tự, bổ sung trigger về thể thức/viết hoa/viết tắt theo NĐ 30/2020.
- Không đưa Phụ lục IV–VI (quản lý văn bản, lập hồ sơ, tài liệu điện tử) — ngoài phạm vi soạn thảo.
