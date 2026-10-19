# Sổ lỗi tự ghi — vbhc-vn

Lỗi Bạn chỉ ra trong phiên, Claude ghi ngay theo CLAUDE.md mục "Tự ghi lỗi" (Bạn chốt 17/10/2026). Đọc tệp này trước khi
soạn văn bản thuộc lĩnh vực của plugin. Định dạng mỗi mục và cách kiểm: `scripts/check_anti_error_format.py` ở gốc kho.
Lỗi kiểm được bằng máy thì kèm quy tắc trong `qa_rules.py` (vbhc-vn) hoặc `check_facts.py` và ghi mã ở dòng "Máy kiểm".
Yêu cầu riêng cho MỘT văn bản không ghi ở đây mà ghi vào `trang-thai/<hồ sơ>.md` mục "Yêu cầu riêng một lần".

### L001 — 17/10/2026 — Khoảng cách sau "Kính gửi" và ô ký tên
- Lỗi: thân văn bản bắt đầu ngay sát dưới khối "Kính gửi" (không có dòng trống); ô ký tên hẹp, thấp hơn hẳn khối Nơi nhận nên lãnh đạo không đủ chỗ ký.
- Cách đúng: sau dòng "Kính gửi" (cả khối nhiều nơi nhận) cách đúng 1 dòng trống rồi mới vào thân văn bản; ô ký tên rộng rãi, chiều cao tương ứng các dòng của khối Nơi nhận (≥ 3 dòng trống giữa chức danh và tên người ký — H13).
- Ví dụ: "Kính gửi: Ủy ban nhân dân tỉnh Lào Cai" → (1 dòng trống) → "Thực hiện …".
- Máy kiểm: `ra_soat_doc_lap.py` mục [3]; tự sửa dòng trống sau Kính gửi: `kiem_tra_truoc_khi_giao.py --tu-sua`; checklist_ra_soat.txt dòng 4, 5.

### L002 — 18/10/2026 — Doanh nghiệp chung dòng với cơ quan nhà nước ở Nơi nhận
- Lỗi: Nơi nhận ghép doanh nghiệp vào cùng dòng với cơ quan nhà nước ("Chi cục Hải quan khu vực VII; Công ty Điện lực Lào Cai") và xếp doanh nghiệp xen giữa các cơ quan. Bạn bác ngày 04/10/2026 khi rà Kế hoạch Bài toán lớn số 2 (PR 116); ghi sổ khi chuyển lên bản 2.34.0.
- Cách đúng: Nơi nhận xếp theo vị thế: cấp trên (b/c) → sở, ban, ngành → cơ quan ngành dọc → UBND xã, phường → doanh nghiệp đứng RIÊNG dòng, sau cùng → Văn phòng → Lưu.
- Ví dụ: "- UBND các xã, phường có cụm công nghiệp;" → "- Công ty Điện lực Lào Cai;" → "- CVP, PCVP UBND tỉnh;" → "- Lưu: VT, KT."
- Máy kiểm: R25 (FAIL khi chung dòng; WARN khi cơ quan nhà nước đứng sau doanh nghiệp); R06, R22.

### L003 — 18/10/2026 — "Ủy ban nhân dân" viết đủ chữ ở Nơi nhận và bảng phụ lục
- Lỗi: dòng Nơi nhận và ô bảng phụ lục của Kế hoạch viết "Ủy ban nhân dân tỉnh" thay vì "UBND tỉnh" (Bạn chốt 04/10/2026, PR 116). Thân văn bản vẫn viết đầy đủ theo checklist rà soát dòng 12 (17/10/2026); phần căn cứ chờ Bạn chốt phạm vi.
- Cách đúng: Nơi nhận "- UBND tỉnh (b/c);", "- UBND các xã, phường …;"; ô bảng phụ lục "UBND xã …"; đầu trang và khối ký "TM. ỦY BAN NHÂN DÂN" giữ đủ chữ.
- Ví dụ: "- Ủy ban nhân dân tỉnh (để b/c);" → "- UBND tỉnh (để b/c);".
- Máy kiểm: R24 (WARN).

### L004 — 17/10/2026 — CCN đã thành lập ghi "thành lập theo Nghị quyết"
- Lỗi: đánh giá chung báo cáo UBND tỉnh viết "Cụm công nghiệp Mông Sơn được thành lập năm 2026 theo Nghị quyết số 34-NQ/TU".
- Cách đúng: cụm đã có Quyết định thành lập thì chỉ ghi "thành lập tại Quyết định số 3426/QĐ-UBND ngày 23/9/2026"; nghị quyết chỉ là định hướng, không phải văn bản thành lập.
- Ví dụ: "Cụm công nghiệp Mông Sơn đã được thành lập tại Quyết định số 3426/QĐ-UBND ngày 23/9/2026".
- Máy kiểm: `qa_rules.py --forbid "thành lập theo Nghị quyết"` (đề xuất R26); Nhóm Q8.

### L005 — 17/10/2026 — Báo cáo của UBND tỉnh viết kiến nghị kiểu Sở kiến nghị tỉnh
- Lỗi: điểm "Kiến nghị Thường trực Tỉnh ủy chỉ đạo" ghi "Đảng ủy Ủy ban nhân dân tỉnh chỉ đạo Sở Tài chính bố trí vốn…", tức UBND tỉnh kiến nghị Tỉnh ủy chỉ đạo chính mình làm việc thuộc thẩm quyền mình.
- Cách đúng: việc thuộc thẩm quyền UBND tỉnh đưa lên "Hướng giải quyết: Ủy ban nhân dân tỉnh chỉ đạo: …"; phần kiến nghị chỉ còn Đảng ủy xã, phường; Đảng đoàn HĐND tỉnh; chủ trương lớn; ý kiến với Trung ương (Nhóm Q2, Q3).
- Ví dụ: "d) Kiến nghị Thường trực Tỉnh ủy chỉ đạo: Đảng ủy xã Gia Phú tập trung lãnh đạo giải phóng mặt bằng…; Đảng đoàn Hội đồng nhân dân tỉnh thống nhất chủ trương bố trí vốn khu tái định cư Phú Xuân khi Ủy ban nhân dân tỉnh trình."
- Máy kiểm: `qa_rules.py --forbid "Đảng ủy Ủy ban nhân dân tỉnh chỉ đạo" ` trong đoạn bắt đầu "d) Kiến nghị" (đề xuất R27); `ra_soat_doc_lap.py` mục giọng chủ thể.

### L006 — 17/10/2026 — Lặp kiến nghị bằng mục III riêng
- Lỗi: báo cáo có điểm d) kiến nghị ở từng dự án nhưng vẫn thêm "III. ĐỀ XUẤT, KIẾN NGHỊ THƯỜNG TRỰC TỈNH ỦY CHỈ ĐẠO" gom lại.
- Cách đúng: bỏ mục III; đánh giá chung kết bằng cam kết của UBND tỉnh; sửa đồng bộ công văn trình và phiếu trình mô tả bố cục.
- Ví dụ: phiếu trình ghi "kiến nghị Thường trực Tỉnh ủy chỉ đạo được nêu ngay tại từng dự án, không lập mục đề xuất, kiến nghị riêng".
- Máy kiểm: thủ công (GATE 0b dàn ý); Nhóm Q4.

### L007 — 19/10/2026 — Đường kẻ dưới tên cơ quan, tiêu ngữ kẻ sai độ rộng
- Lỗi: kẻ viền dưới ngay trong đoạn chữ, lề trái/phải tính theo số twips cố định không gắn với bề rộng ô; LibreOffice nhìn tạm được nhưng Word kẻ tràn rộng hơn chữ "Độc lập – Tự do – Hạnh phúc", kẻ dưới "SỞ CÔNG THƯƠNG" lệch.
- Cách đúng: đoạn trống riêng có viền dưới, cỡ chữ 1 pt, lề hai bên = (bề rộng ô − chiều dài kẻ)/2; ô trái 6 cm kẻ ~2,3 cm, ô phải 10 cm kẻ ~5,6 cm (Nhóm R6).
- Ví dụ: `build_bctl.py` hàm `ke(cell, after_par, cell_tw, line_tw)` (kccn-sct-vn ví dụ 2026-10-19).
- Máy kiểm: thủ công — chụp trang 1 ở 110 dpi, so chiều dài kẻ với chữ; đề xuất R28 cho `qa_rules.py` (kiểm `w:ind` của đoạn có `w:pBdr` trong ô tiêu đề).

### L008 — 19/10/2026 — Khối ký tách sang trang sau (lặp lại lỗi cũ ở báo cáo 48 trang)
- Lỗi: bảng ký rơi sang trang mới, trang trước kết bằng câu kết và dòng trống.
- Cách đúng: đoạn kết và dòng trống keep_with_next; hàng bảng ký cantSplit; mọi dòng trong ô Nơi nhận keep_with_next (Nhóm R7); kiểm ảnh hai trang cuối trước khi giao.
- Ví dụ: báo cáo tổng hợp Sở 19/10/2026 trang 28–29 sau sửa liền nhau.
- Máy kiểm: `qa_pdf_check.py` (trang cuối chỉ có khối ký → FAIL); kiểm thêm trang kế cuối kết bằng câu "./." mà không có bảng ký.

### L009 — 19/10/2026 — Lùi đầu dòng lẫn ba kiểu trong một tài liệu
- Lỗi: ghép nội dung từ ba lần dựng (docx-js, python-docx, chèn đoạn) nên 137 đoạn thụt lề trái 0,5 cm, 89 đoạn không lùi, 57 đoạn lùi 1 cm.
- Cách đúng: trước khi xuất, quét mọi đoạn không căn giữa: left_indent 0, first_line_indent 1 cm, căn đều (Nhóm R5).
- Ví dụ: tài liệu 7 dự án bản đầy đủ 19/10/2026 sau khi chuẩn hóa 291 đoạn.
- Máy kiểm: đề xuất R29 cho `qa_rules.py` (đếm kiểu thụt đầu dòng của đoạn thân; >1 kiểu → WARN).

### L010 — 18/10/2026 — Ghi mốc chốt số liệu thừa trong tài liệu chuẩn bị
- Lỗi: tiêu đề phụ "(Số liệu đến ngày 17/10/2026…)", nhãn "Về GPMB (đến 16/10/2026)", "sản lượng đến 15/10/2026" trong tài liệu nội bộ chuẩn bị đón đoàn.
- Cách đúng: bỏ mốc chốt, viết "đến nay"; chỉ giữ ngày của văn bản viện dẫn và mốc tiến độ (Nhóm R2). Bạn: "giai đoạn chuẩn bị báo cáo này không cần quá tính toán một vài ngày".
- Ví dụ: "Về GPMB:" ; "sản lượng đến nay khoảng 286.000 tấn".
- Máy kiểm: grep "số liệu đến ngày", "(đến \d\d/\d\d/20" trong tài liệu nội bộ → WARN (đề xuất gộp vào R29).

