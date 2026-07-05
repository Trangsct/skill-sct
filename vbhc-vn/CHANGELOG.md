# CHANGELOG — plugin vbhc-vn

## v2.0.1 — 05/7/2026 (vá SZ13 tận gốc + guard đầu vào QA)

### Sửa lỗi
- `fill_template.py`: thêm `_dominant_run()` — khi thay text, gán vào run có text DÀI NHẤT (run mang định dạng chủ đạo) thay vì run[0]; các run khác xóa trắng nên thứ tự hiển thị không đổi. Sửa lỗi mất `w:sz=26` (13pt tường minh) ở dòng Số/Ngày sau khi điền template (vi phạm Quy tắc bất biến 12) khi run[0] rỗng/ngắn không mang sz. Áp dụng cho cả `_replace_text_in_paragraph` và `_set_paragraph_text`. Không đụng run neo shape (giữ Quy tắc bất biến 11).
- **7/9 template** thiếu 13pt tường minh ở dòng Số/Ngày ngay trong file gốc (01, 02, 03, 04, 05, 07, 08 — chỉ 06 và 09 đạt sẵn): đã quét toàn bộ, đặt `w:sz=26` cho mọi text-run của dòng Số/Ngày + `w:i` cho dòng ngày; đã render kiểm không hồi quy Line shape.
- `qa_pdf_check.py`: thêm guard đầu vào — tool nhận `.docx` (tự render PDF bên trong), truyền nhầm `.pdf`/file không tồn tại nay báo lỗi thân thiện kèm hướng dẫn thay vì crash `PackageNotFoundError`.
- `demo_cong_van.py`: rút gọn nội dung mẫu để khối ký về trọn trang 1 (Quy tắc bất biến 14) — cả 3 demo nay tự thân đạt `qa_pdf_check` PASS 3/3.

### Kiểm chứng
- End-to-end: 3 demo → 3/3 QA PASS; render ảnh soi công văn + quyết định đạt thể thức (2 Line header, 13pt + nghiêng dòng ngày, khối ký trọn trang).

## v2.0.0 — 05/7/2026 (nâng cấp toàn diện, chuyển chuẩn plugin, cài mới thay bản cũ)

### Quy tắc mới vĩnh viễn (từ vụ 4 lỗi công văn HHNH 05/7/2026)
- **Quy tắc bất biến 11**: cấm gán `run.text` cho run neo shape Line (hàng Số/Ngày header) — shape bọc trong `mc:AlternateContent`, gán text xóa mất Line + định dạng; sửa qua node `w:t`, hỏng thì deep copy `<w:p>` từ gốc; QA đếm shape.
- **Quy tắc bất biến 12**: dòng "Số:" và "Địa danh, ngày..." 13pt tường minh (`w:sz`=26), dòng ngày in nghiêng.
- **Quy tắc bất biến 13**: không để widow word (1 chữ rơi dòng) — co chữ condensed hoặc nới; QA quét pdftotext.
- **Quy tắc bất biến 14**: khối chữ ký không gãy giữa 2 trang — `cantSplit` + co giãn toàn văn bản (space 6→4pt) để khối ký về trọn trang trước.
- **Nhóm anti-error H mới** (nâng 7 nhóm → 8 nhóm): toàn vẹn thể thức khi thao tác XML/run; bài học "render LibreOffice đẹp chưa chắc Word đẹp — QA dữ liệu song song soi ảnh".

### Script mới
- `scripts/qa_pdf_check.py`: QA tự động 4 kiểm tra (widow word, khối ký gãy trang, đủ Line header, cỡ 13pt dòng Số/Ngày); là đường QA chính khi tool view ảnh lỗi. Đã test PASS/FAIL trên vụ thật.

### Tích hợp bài học các phiên 25/6 – 05/7/2026
- Bài học XML mới: cấm `d.paragraphs[n]` sau chèn/xóa (vụ CV kho VLNCN 04/7 — 4 lỗi cùng gốc trôi chỉ số); clone body từ đoạn body chuẩn; join-runs phải né run có shape; assertion tự động sau build Chế độ B; `merge_runs.py` trước sửa XML.
- Bước 4 QA: bổ sung đường QA thay thế (`pdftotext -layout` + kiểm XML) khi view ảnh không truyền được.

### Sửa lỗi phát hiện trong plugin
- `check_document.py`: (1) 2 pattern "số trống/ngày trống" gây false positive trái quy ước — hạ thành mục [INFO] không tính cảnh báo; (2) bổ sung 10 VBQPPL hết hiệu lực mới (Luật XD 50/2014→135/2025, NĐ 06/2021→207/2026, NĐ 175/2024→217/2026, TT 06/2021→TT 34/2026, NĐ 71/2018→181/2024, Điều 3 TT 15/2026 bãi bỏ bởi TT 26/2026, NĐ 113/2017 + 82/2022 + TT 32/2017 → khung Luật Hóa chất 69/2025, cảnh báo "thanh tra chuyên ngành"→"kiểm tra chuyên ngành").
- Template: sửa "CỘNG HOÀ"→"CỘNG HÒA" + hyphen→en dash tiêu ngữ ở 02-to-trinh, 03-bao-cao, 07-gcn-attp, 09-bien-ban; chèn Line shape dưới Tiêu ngữ vào 07 (trước đây thiếu hẳn, đã render kiểm vị trí).
- `thu-vien-mau-that.md`: cảnh báo 2 mẫu thật dùng `w:pBdr` thay Line (bao-cao-tinh-hinh-trien-khai-ccn, bao-cao-vp-ubnd) — giữ nguyên tư liệu nhưng khi dựng mới phải thay bằng Line; bảng số Line chuẩn theo loại văn bản.
- `HUONG_DAN_CAP_NHAT.md`: viết mới (file cũ hỏng encoding mojibake, không đọc được).
- Đổi tên 2 file reference có dấu cách/ngoặc → `anti-error-sct-vn-goc.md`, `vbhc-pdf-reader-vn-goc.md`.
- Sửa mọi đường dẫn tuyệt đối `/mnt/skills/user/vbhc-vn` → đường dẫn plugin `/mnt/skills/plugins/vbhc-vn:vbhc-vn/` (kèm ghi chú fallback user skill).
- Description SKILL.md: 1246 bytes (vượt giới hạn 1024) → viết lại còn 998 bytes.

### Đóng gói
- Lần đầu đóng gói theo chuẩn plugin (`.claude-plugin/plugin.json` + `skills/vbhc-vn/`); kèm validator tự kiểm trước khi xuất.

## v1.x — trước 05/7/2026
- Bản user skill hợp nhất từ vbhc-vn + anti-error-sct-vn + vbhc-pdf-reader-vn + 3 Phụ lục NĐ 30/2020; 9 template trắng + 17 mẫu thật; 7 nhóm anti-error.
