# CHANGELOG — plugin vbhc-vn

## v2.4.0 — 24/7/2026 (Quy tắc 20: cấm chiều cao dòng cố định `<w:trHeight>` trong bảng nội dung)

### Vấn đề thật
Biên bản thẩm định hồ sơ cấp Giấy phép vận chuyển HHNH loại 2 (Công ty CP thương mại vận tải và tư vấn kỹ thuật, 24/7/2026): trang 4 kết thúc bằng đề mục `- Lái xe:` rồi bỏ trắng gần nửa trang, bảng danh sách lái xe nhảy nguyên khối sang trang 5. Soi XML: `</w:p><w:tbl>` liền nhau, KHÔNG có paragraph trống — thủ phạm là `<w:trHeight>` gán cứng cho từng dòng (tiêu đề 1623 twip, mỗi dòng dữ liệu 2002 twip) cộng `<w:cantSplit/>`, làm cụm "dòng tiêu đề + dòng dữ liệu đầu" cao ~7 cm, vượt phần giấy còn lại nên Word đẩy cả bảng sang trang mới.

### Khắc phục đã áp dụng và chuẩn hóa thành quy tắc
- Gỡ sạch `<w:trHeight>` trong bảng → dòng tự co theo nội dung.
- Siết giãn dòng trong ô bảng từ 360 exact (18pt, chuẩn thân văn bản) về **300 exact (15pt) cho chữ 13pt**, 320 cho chữ 14pt.
- Kết quả: cụm "tiêu đề + dòng 1" từ 6,96 cm còn 5,89 cm; bảng bám ngay dưới đề mục, hết khoảng trắng; giữ nguyên `<w:cantSplit/>` để không xẻ đôi dòng qua trang.

### SKILL.md
- **Quy tắc 20 mới** (nhóm anti-error): cấm `<w:trHeight>` ở Chế độ A; Chế độ B phải gỡ sạch khi sửa mẫu thật/file doanh nghiệp. Hai ngoại lệ: bảng header (bảng 1) giữ nguyên theo mẫu thật; chừa chỗ ký/điền tay thì dùng paragraph trống trong ô. Kèm mốc an toàn ≤ 6 cm cho cụm "tiêu đề + dòng 1" và đoạn code gỡ nhanh theo chỉ số bảng.
- Frontmatter: bổ sung "chiều cao dòng bảng" vào danh mục tiêu chí QA.

### Script
- `scripts/check_document.py`: thêm **nhóm [F]** — hàm `find_fixed_row_heights()` quét bảng cấp ngoài cùng, đếm `<w:trHeight>` theo từng bảng; bảng 1 (header) chỉ báo INFO, bảng 2 trở đi báo LỖI và đưa vào `has_critical` (fail `--strict`). In luôn hướng khắc phục.

### Reference
- `reference/phong-tranh-sai-lam.md`: thêm 1 dòng checklist trước khi trình ký, 2 dòng "bắt lỗi ngay khi đang hình thành" ([F-trHeight]), cập nhật mô tả phạm vi dò của `check_document.py`.

## v2.1.0 — 06/7/2026 (QA MỘT PHÁT — cắt thời gian hoàn thành 1 văn bản)

### Vấn đề
Quy trình Bước 4 cũ tốn thời gian: render PDF 2 lần (soi ảnh + qa_pdf_check tự render lại, mỗi lần soffice nguội 15-25s), 6-8 lượt tool rời rạc (inspect → build → validate → render → view 2-4 ảnh trang → qa_pdf_check → check_document), lặp render/view sau từng lỗi nhỏ.

### Script mới
- `scripts/qa_all.py` — **QA MỘT PHÁT, đường QA chính**: một lệnh gộp (1) kiểm XML: Line header + 13pt Số/Ngày (tái dùng hàm qa_pdf_check), `<w:br/>` header (Quy tắc 10), body căn giữa/thiếu firstLine 1cm/thụt treo (WARN — bài học Chế độ B); (2) check_document.py (hiệu lực VBQPPL, từ suy đoán, số đáng ngờ); (3) render PDF **đúng 1 lần** với profile soffice ấm (`-env:UserInstallation`) dùng lại cho widow word + khối ký gãy trang; (4) xuất **ảnh ghép mọi trang trong 1 file** `qa_sheet.png` → chỉ cần 1 lượt `view`. Đo thực tế: 3.0s lần nguội, 1.3-1.7s lần ấm (trước đây ≥ 30-50s cho chuỗi render đôi). Test PASS trên demo công văn + test âm tính FAIL đúng với `<w:br/>` cố ý trong header.

### Sửa script
- `qa_pdf_check.py`: thêm `--pdf <path>` — dùng PDF render sẵn, không render lại (hết cảnh render đôi khi chạy kèm soi ảnh).

### SKILL.md
- Bước 2: bỏ lượt inspect template khi `reference/templates-chi-tiet.md` đã có chỉ số.
- Bước 4 viết lại: một lệnh `build && qa_all`; view 1 ảnh ghép; sửa lỗi theo báo cáo text, gom hết mới render lại.
- Mục mới "Quy tắc tốc độ": văn bản thường xong trong 3-4 lượt tool; chất lượng vẫn là chốt chặn (không giao file chưa PASS).
- Chế độ B: assertion CENTER/firstLine/shape/br-header chuyển sang qa_all.py phủ; chỉ tự viết assertion phần nội dung vụ việc.
- Description frontmatter cập nhật "QA MỘT PHÁT qa_all.py".

## v2.0.2 — 06/7/2026 (gỡ phụ thuộc đường dẫn skill lẻ + phân vai với sentinel)

### Sửa lỗi
- `reference/vbhc-pdf-reader-vn-goc.md` (4 chỗ) và `reference/anti-error-sct-vn-goc.md` (1 chỗ): đường dẫn hardcode `/mnt/skills/user/vbhc-pdf-reader-vn/scripts/extract_metadata.py` → đường dẫn plugin `"/mnt/skills/plugins/vbhc-vn:vbhc-vn/scripts/extract_metadata.py"` (kèm ghi chú fallback khi có skill lẻ). Trước đây các lệnh này chỉ chạy được chừng nào skill lẻ vbhc-pdf-reader-vn còn cài — gỡ skill lẻ là thành đường dẫn chết.

### Phân vai với skill lẻ vbhc-pdf-reader-vn (nâng lên v2.0 cùng ngày)
- Skill lẻ giữ vai trò **SENTINEL**: description trigger mạnh + quy tắc cứng + script, thu gọn 250 → 70 dòng; toàn bộ chi tiết nghiệp vụ ủy quyền cho `reference/doc-pdf-metadata.md` của plugin này. Hai bên cùng trỏ một quy trình, không còn trùng ~250 dòng khi cả hai kích hoạt.
- **Quy ước đồng bộ**: `scripts/extract_metadata.py` tồn tại ở 2 nơi (plugin + skill lẻ) và phải GIỐNG TỪNG BYTE; mọi lần sửa script phải cập nhật đồng thời cả hai và ghi CHANGELOG. Đã kiểm chứng 06/7/2026: `diff` = 0.

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
