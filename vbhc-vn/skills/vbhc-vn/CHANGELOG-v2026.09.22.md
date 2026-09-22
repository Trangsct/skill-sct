## [2.27.0] - 22/9/2026 — R17 đánh số "Một là", R18 đề mục La Mã lệch tab; R11 tính đậm kế thừa kiểu

- **Nguồn:** rà soát dự thảo Báo cáo tháng 9/2026 thực hiện NQ 34-NQ/TU của Sở (PGĐ Nguyễn Đình Chiến ký, CN(Trung)) ngày 22/9/2026. Bạn chốt "thống nhất kiểu đánh số và thể thức".
- **qa_rules.py — R17 (mới, WARN):** liệt kê "Một là, Hai là…" không kèm số trong ngoặc "(1) Một là"; mỗi ý một đoạn riêng, ý giữa kết thúc dấu chấm phẩy, ý cuối dấu chấm. Bản gốc báo cáo dồn "(1) Một là… (4) Bốn là…" vào một đoạn.
- **qa_rules.py — R18 (mới, WARN):** các đề mục La Mã I, II, III… trong cùng văn bản phải cùng một cách lùi đầu dòng; chỉ bắt khi LẪN tab với thụt dòng đầu (bản gốc: I, II, IV mở đầu bằng tab, III thụt 1 cm). Bản đầu bắt mọi đoạn mở đầu bằng tab thì 4 mẫu thật dính (biên bản liên ngành CCN, tờ trình tiền chất, CV UBND chỉ đạo, giấy mời UBND) → thu hẹp theo nguyên tắc "mẫu thật là chuẩn".
- **qa_rules.py — `is_bold` sửa:** run để trống thuộc tính đậm thì kế thừa kiểu ký tự/kiểu đoạn theo chuỗi base_style. Vụ 22/9/2026: dòng "KT. GIÁM ĐỐC" đậm qua kiểu Heading 1 bị R11 báo FAIL nhầm.
- **tests/fail:** thêm `r17-danh-so-kep-mot-la.docx`, `r18-de-muc-la-ma-lech-tab.docx` (nhân tạo từ `examples/sct/bao-cao-thang-phong-qlcn.docx`, sinh bằng `tests/tao_file_loi.py`); 26 mẫu thật không phát sinh R17/R18.
- **reference/cong-cu-ky-thuat.md:** ghi bẫy helper thay chữ trải nhiều run: không dùng `id(p._p)` để đánh dấu đoạn đã duyệt (lxml tạo proxy mới, id bị tái sử dụng → bỏ sót đoạn trong ô bảng); duyệt `body.iter(w:p)` bọc `Paragraph`.
- Ghi chú hồi quy: 4 dòng "BẮT THỪA SIGSPLIT" khi chạy ngoài CI đã có từ trước bản này (do môi trường render), không phát sinh từ thay đổi.
- `plugin.json` → 2.27.0.
