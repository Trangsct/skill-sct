# CHANGELOG — plugin vbhc-vn

## [2.13.0] - 06/9/2026 — Nhóm K: văn bản chỉ đạo của UBND tỉnh do Sở dự thảo — giao việc cho cơ quan khác

### Thêm
- **reference/phong-tranh-sai-lam.md — Nhóm K MỚI** (K1–K7). Nguồn: dự thảo Công văn UBND tỉnh tăng cường quản lý VLNCN (bản 03/9/2026) bị Lãnh đạo Sở đọc nửa đầu và bôi đỏ 5 đoạn (1đ, 2a, 2b, 2c, 2d): *dùng từ vượt khỏi phong cách hành chính* + *trích dẫn điều khoản chưa chính xác*; rà tiếp nửa sau phát hiện mục 3 (Bộ CHQS tỉnh) sai thẩm quyền.
  - K1 không cài điều kiện tiên quyết vào thủ tục của cơ quan khác ("chỉ cấp GP vận chuyển sau khi…" ↔ Điều 41 Luật 42/2024 chốt cứng 03 ngày làm việc) → cơ chế phối hợp, đối chiếu.
  - K2 mỗi việc giao cơ quan X phải có điều khoản thẩm quyền của chính X (Bộ CHQS tỉnh không cấp Mệnh lệnh vận chuyển — Đ6 TT 98/2024/TT-BQP; Công an chỉ thẩm định 2 nội dung PCCC — Đ9 NĐ 105/2025; kiểm tra nghiệm thu PCCC dừng từ 01/7/2026 — NQ 66.18/2026); bảng 3 cột trước khi viết mục "Giao".
  - K3 bỏ tính từ đánh giá sau động từ thủ tục; K4 không ngoặc đơn giải thích trong câu giao việc; K5 thuật ngữ theo luật; K6 gọi tắt Luật một lần, điều khoản bị sửa ghi kèm văn bản sửa, không lặp ngày ở lần dẫn sau; K7 quy trình khi Lãnh đạo bôi đỏ một phần (sửa toàn văn, xóa đỏ ở paragraph mark, báo cáo 2 danh sách).
  - Lệnh QA nhanh `qa_all.py --forbid` cho các cụm đã bị bôi đỏ; checklist thêm ô [K]; mục "Khi tự phát hiện sắp mắc lỗi" thêm 3 dòng K2–K4.
- Khung đã sửa theo ý kiến Lãnh đạo lưu tại `sd-vlncn-sct-vn/vi-du-thuc-te/Du-thao-CV-UBND-tinh-chi-dao-tang-cuong-quan-ly-VLNCN-ban-sua-6.9.2026.docx` (mẫu 23 plugin đó, phiên bản 2026.9.6.1).

### Sửa
- SKILL.md: "10 nhóm A–J" → **"11 nhóm A–K"** tại 3 vị trí; tóm tắt Nhóm K trong mục "Luôn áp dụng" và danh sách nhóm; plugin.json description đồng bộ.

## [2.11.0] - 31/8/2026 — Nhóm J: giọng giải thích lọt vào thân văn bản

### Thêm
- **reference/phong-tranh-sai-lam.md — Nhóm J MỚI**. Bạn phát hiện lỗi tái phát qua câu *"Doanh nghiệp lưu ý điểm này để không nhầm rằng kho nhỏ thì được miễn thủ tục"* trong công văn hướng dẫn kho VLNCN. Cơ chế phát sinh: vừa soạn văn bản vừa viết phần giải thích cho người dùng trong cùng một mạch nên register bị rò. `check_document.py` không bắt được vì không sai thể thức, không sai căn cứ — phải tự soi thủ công.
  - **Tiêu chí một câu**: mỗi câu trong thân VBHC phải nêu quy định, nêu yêu cầu hoặc nêu sự việc.
  - **J1**: bảng 10 mẫu câu đã mắc thật kèm cách viết lại ("Đây là luồng đầy đủ nhất", "cần nắm rõ", "không đồng nghĩa với", "đáng kể", "công cụ pháp lý đúng là", "Điểm cần đặc biệt lưu ý"...).
  - **J2**: đề mục không dùng dạng hỏi đáp; chuyển "Câu hỏi 1: … ?" thành "1. Xác định … hay không".
  - **J3**: cấm từ định lượng cảm tính không kèm số.
  - **J4**: cấm câu meta về chính văn bản.
  - **J5**: ranh giới ngoại lệ — nêu bối cảnh, nguyên nhân khách quan ở đoạn mở đầu công văn vẫn hợp lệ.
  - Cách QA: `qa_all.py --forbid` cho các cụm hay tái phát, rồi đọc lại một lượt riêng chỉ soi register.

### Sửa
- Tiêu đề file: 8 nhóm → **10 nhóm A–J**; SKILL.md đổi "9 nhóm A–I" thành "10 nhóm A–J" tại 3 vị trí và bổ sung tóm tắt Nhóm J vào mục "Luôn áp dụng".

