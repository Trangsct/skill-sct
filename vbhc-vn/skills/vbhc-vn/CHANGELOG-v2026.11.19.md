# vbhc-vn 2.42.0 — 19/11/2026 — Khung khối Kính gửi nhiều nơi nhận (R29, L017)

- **Nguồn:** công văn đề nghị ba cơ quan báo cáo tình hình thi hành pháp luật về chất lượng sản phẩm, hàng hóa (19/11/2026); Bạn chỉ ra khối Kính gửi lệch, sai quy tắc, rồi gửi lại bản sửa tay làm chuẩn ("khối ô Kính gửi cần tạo khung thế này").
- **Quy ước mới (Quy tắc 27(a), sổ lỗi L017):** Kính gửi từ hai cơ quan trở lên dựng khung bảng 2 cột không viền rộng hết phần thân; hàng 1 ô trái "Kính gửi:" căn phải; từ hàng 2 ô phải mỗi cơ quan một hàng; cơ quan đầu thấp hơn "Kính gửi:" một dòng. Cách tab + lề treo trước ngày này là lịch sử.
- **scripts/build_vb.py:** hàm `khung_kinh_gui()`; dòng `[K]` nhiều nơi nhận trên mẫu chỉ có đoạn "Kính gửi" (mẫu công văn mặc định) nay tự dựng khung thay vì xếp đoạn rời.
- **scripts/qa_rules.py — R29 (mới, WARN):** văn bản ký hiệu của Sở, Kính gửi nhiều nơi nhận mà không ở khung 2 cột, hoặc cơ quan đầu cùng dòng "Kính gửi:". File lỗi `tests/fail/r29-kinh-gui-nhieu-noi-cung-dong.docx`; baseline thêm 1 WARN đúng trên mẫu cũ `cong-van-xin-y-kien-cac-co-quan-phuong-an-ccn-von-nsnn.docx` (xếp đoạn rời).
- SKILL.md Nhóm G, checklist rà soát dòng 11, `tests/rule-inventory.md`; "R01–R27" → "R01–R29". `plugin.json` → 2.42.0.
