# vbhc-vn 2.39.0 — 10/11/2026

Trích yếu công văn: một đoạn liền, tự xuống dòng, tối đa 3-4 dòng, cân với khối tên cơ quan (Bạn chốt 10/11/2026).

- **R27 mới** trong `scripts/qa_rules.py`: ô "V/v" của bảng đầu trang tách thành nhiều đoạn hoặc có khoảng trắng không
  ngắt (U+00A0) để ép dòng → FAIL; trích yếu dài quá 140 ký tự → WARN. File lỗi
  `tests/fail/r27-trich-yeu-tach-nhieu-doan.docx` (sinh bằng `tests/tao_file_loi.py`); 26 mẫu thật không phát sinh FAIL, WARN.
- **`scripts/do_trich_yeu.py` mới**: dựng PDF rồi đo khối trích yếu — số dòng (tối đa 4), lệch tâm so với khối tên cơ quan
  (≤ 3 pt), mép phải cách đường thẳng đứng của chữ "CỘNG" (≥ 0,2 cm), dòng cuối không rớt riêng một chữ; in thêm độ rộng
  hơn khối tên cơ quan mỗi bên (mong muốn 0,5-1 cm). Mã thoát 1 khi có mục không đạt.
- `reference/so-loi-tu-ghi.md`: L015 (quy ước, cách chỉnh bằng bề rộng ô và lề đoạn, thông số đã dùng cho lưới 3119 + 236 +
  5820 twip). `tests/rule-inventory.md` thêm R27; SKILL.md Nhóm G và các chỗ "R01–R26" → "R01–R27".
- `plugin.json` 2.38.1 → 2.39.0.

# vbhc-vn 2.39.1 — 10/11/2026

- `scripts/do_trich_yeu.py`: dòng trích yếu cùng hàng với dòng địa danh, ngày tháng ở cột phải (mẫu công văn nội bộ phòng)
  chỉ lấy cụm chữ bên trái; trích yếu một dòng không xét lệch tâm (mẫu nội bộ phòng căn đều hai bên theo mẫu thật).
- Đã đo 9 template: 7 template không có dòng V/v; `01-cong-van.docx` và `08-cong-van-noi-bo-phong.docx` thử với trích yếu
  dài 96 và 109 ký tự đều 3-4 dòng, lệch tâm 0 pt, cách chữ "CỘNG" 0,53-0,62 cm, rộng hơn khối tên cơ quan 0,66-1,02 cm mỗi
  bên — đạt quy ước L015, giữ nguyên template.
- Quét R27 trên 323 tệp .docx của kho (trừ văn bản gốc, file lỗi thử): 7 tệp ví dụ thực tế vướng — 6 tệp của Sở đã gộp/bỏ
  khoảng trắng không ngắt (sd-vlncn-sct-vn 1 tệp, tkm-sct-vn 5 tệp); 1 tệp là công văn của Sở Nông nghiệp và Môi trường
  trong qlks-sct-vn, văn bản của cơ quan khác nên giữ nguyên.
- `plugin.json` 2.39.0 → 2.39.1.
