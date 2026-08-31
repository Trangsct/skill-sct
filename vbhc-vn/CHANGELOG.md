# CHANGELOG — plugin vbhc-vn

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

