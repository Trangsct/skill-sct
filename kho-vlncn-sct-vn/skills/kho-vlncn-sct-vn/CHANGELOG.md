# CHANGELOG — kho-vlncn-sct-vn

## v1.4 — 04/7/2026
- Rút gọn description trong SKILL.md xuống 724 ký tự / 898 byte (giới hạn validator claude.ai: 1024). Toàn văn mô tả dài chuyển vào mục I SKILL.md, không mất nội dung kích hoạt.
- Bổ sung script tự kiểm tra mô phỏng validator (tên kebab-case, description ≤1024 ký tự và byte, đường dẫn 100% ASCII, frontmatter hợp lệ) — chạy trước mọi lần đóng gói sau này.

## v1.3 — 04/7/2026
- Đóng gói theo chuẩn plugin Claude chính thức: `.claude-plugin/plugin.json` ở gốc zip + skill đặt tại `skills/kho-vlncn-sct-vn/` (tham chiếu docs code.claude.com/docs/en/plugins). Khắc phục dứt điểm lỗi validation khi upload plugin.

## v1.2 — 04/7/2026
- Đóng gói lại zip: SKILL.md và các thư mục nằm NGAY GỐC zip (không bọc trong thư mục con) — khắc phục lỗi "Zip must contain a .claude-plugin/plugin.json file or a top-level SKILL.md".

## v1.1 — 04/7/2026
- Đổi toàn bộ tên file trong vi-du-thuc-te/ và van-ban-goc/ sang không dấu, ASCII an toàn (khắc phục lỗi "Zip file contains path with invalid characters" khi upload plugin lên claude.ai); cập nhật 2 file mục lục tương ứng. Nội dung không thay đổi.

## v1.0 — 04/7/2026
- Khởi tạo plugin từ: (i) bộ hồ sơ 4 vụ việc thực tế 2026 (Nậm Cang 1A, Móng Sến 1, Mông Sơn, Ngòi Nhù 1A); (ii) TT 32/2019/TT-BCT (QCVN 01:2019/BCT) toàn văn; (iii) bộ VBQPPL VLNCN 2024–2025; (iv) bản phản biện pháp lý hồ sơ Ngòi Nhù 1A.
- 10 references; 9 mẫu văn bản (gộp trong 5 file); 21 file ví dụ thực tế; 10 văn bản gốc.
- Việc cần cập nhật tiếp: xác minh QĐ 1883/QĐ-UBND (ủy quyền cấp GP sử dụng VLNCN); bổ sung toàn văn Luật 118/2025; bổ sung QĐ công bố TTHC lĩnh vực VLNCN hiện hành; theo dõi QCVN thay thế QCVN 01:2019/BCT (nếu ban hành).
