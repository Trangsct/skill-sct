# CHANGELOG — vbhc-vn v2.36.0 (19/10/2026)

Gộp hai lượt ghi plugin của phiên claude.ai 17–19/10/2026 (đánh số 2.35.0 và 2.36.0 trên nền `204fc21`) vào `main` sau vbhc-vn 2.35.0 (NĐ 30/2020, NĐ 74/2026). Viện dẫn kccn-sct-vn đánh lại: ref 48 → ref 49, ref 49 → ref 50.

## Phần 1 — Nhóm Q (18/10/2026)

Nguồn: phiên 17–18/10/2026 dựng bộ báo cáo của UBND tỉnh gửi Thường trực Tỉnh ủy theo Chương trình 130-CTr/TU (kccn-sct-vn ref 49).

- **Nhóm Q (mới)** `reference/phong-tranh-sai-lam.md`: báo cáo của UBND tỉnh gửi Tỉnh ủy do Sở dự thảo — Q1 giọng chủ thể UBND tỉnh; Q2 hướng giải quyết là cam kết "UBND tỉnh chỉ đạo"; Q3 phần kiến nghị chỉ gồm việc của cấp ủy cơ sở, Đảng đoàn HĐND tỉnh, chủ trương lớn, Trung ương (cấm "Đảng ủy UBND tỉnh chỉ đạo Sở…"); Q4 không lặp kiến nghị bằng mục III; Q5 đánh giá chung 3 điểm; Q6 thể thức; Q7 rà bài phát biểu của Chủ tịch, Bí thư (cộng lại số tổng, đủ ký hiệu, động từ đúng chủ thể, bài Bí thư không mạnh hơn Chủ tịch, soi câu bất lợi cho Sở, góp ý bôi tím trong file của Văn phòng); Q8 CCN thành lập ghi QĐ không ghi nghị quyết.
- `reference/so-loi-tu-ghi.md`: L004 (thành lập theo Nghị quyết), L005 (kiến nghị kiểu Sở kiến nghị tỉnh), L006 (mục III lặp kiến nghị) — kèm đề xuất R26, R27 cho `qa_rules.py` (chưa cài, làm ở đợt sau).
- `SKILL.md`: bảng nhóm A–P thêm dòng Q; tiêu đề "17 nhóm A–Q".

## Phần 2 — Nhóm R (19/10/2026)

Nguồn: phiên 18–19/10/2026 dựng tài liệu của Giám đốc Sở đón đoàn Thường trực Tỉnh ủy (khung 14 nhãn/dự án) và báo cáo tổng hợp 48 trang của Sở làm việc với Thường trực Tỉnh ủy (kccn-sct-vn ref 50, mẫu 10).

- **Nhóm R (mới)** `reference/phong-tranh-sai-lam.md`: tài liệu dài, báo cáo tổng hợp, tài liệu nội bộ — R1 giữ khung và nhãn của lãnh đạo; R2 không ghi "số liệu đến ngày"; R3 mốc khởi công theo BQL KKT; R4 ước số ghi "(ước của Sở)"; R5 lùi đầu dòng 1 cm thống nhất; R6 đường kẻ tiêu đề tính theo bề rộng ô; R7 khối ký không tách trang; R8 phụ lục cùng file; R9 mục có phụ lục vẫn viết tóm tắt; R10 chữ tím + phiếu đề nghị phòng, diff file phòng bạn trả lại; R11 chỉ số hóa học, đơn vị tiền; R12 tên trạm, một con số cho một chỉ tiêu. Checklist thêm dòng [R].
- `reference/so-loi-tu-ghi.md`: L007 (kẻ tiêu đề sai độ rộng), L008 (khối ký tách trang), L009 (lùi đầu dòng lẫn ba kiểu), L010 (mốc chốt số liệu thừa) — đề xuất R28, R29 cho `qa_rules.py` (chưa cài).
- `SKILL.md`: bảng nhóm thêm dòng R; tiêu đề "18 nhóm A–R". `plugin.json` → 2.36.0, description "A-R".
