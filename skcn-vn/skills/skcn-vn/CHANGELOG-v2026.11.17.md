# skcn-vn 1.3.0 — 17/11/2026 — Phần Quản lý thuốc

Bạn yêu cầu nâng skill "giỏi hơn các đối thủ" (các app nhắc uống thuốc) sau đợt tự dùng Doxycyclin tái phát.

- `SKILL.md`: thêm mục **Quản lý thuốc** gồm 8 phần: (1) nhận diện thuốc từ ảnh hộp, vỉ, đơn, tra tờ hướng dẫn đúng sản phẩm, không đoán hoạt chất từ tên biệt dược; (2) liều theo nhãn, đổi ra số viên và giờ, đã uống rồi mới hỏi thì đối chiếu trước, quên liều, thuốc cho con; (3) rà an toàn bắt buộc trước thuốc mới: trùng hoạt chất trong tủ, tương tác TPCN, va chạm nền bệnh, lịch sử kháng sinh thất bại, kèm bảng va chạm đặc thù (doxycyclin, fluoroquinolon, corticoid, NSAID, paracetamol, thuốc ho codein, rượu bia); (4) khối theo dõi đợt điều trị, mốc đánh giá ngày 3, không ngừng sớm; (5) đặt nhắc uống thuốc thật trên điện thoại bằng công cụ `mcp__claude-device__`; (6) ghi tuân thủ; (7) tủ thuốc gia đình; (8) cách trả lời về thuốc (không markdown, câu đầu trả lời thẳng).
- `SKILL.md` mục Hồ sơ nền: thêm trào ngược (Pantoloc), đờm xanh đặc mãn tính không dùng làm tiêu chí nhiễm khuẩn, thói quen tự điều trị tại nhà.
- `SKILL.md` mục Ranh giới: thay câu "Không tư vấn liều thuốc kê đơn" bằng quy tắc cụ thể — chỉ báo liều in trên tờ hướng dẫn có nguồn; không tự đặt liều khác nhãn, không chọn hộ mức liều, số ngày đợt kháng sinh; không khuyên tự bắt đầu kháng sinh.
- `SKILL.md` description: thêm từ khóa kích hoạt về thuốc.
- `references/lich-su-chi-so.md`: thêm mục **Đợt điều trị** với 3 khối (amoxicillin + clavulanic 10/2026, Doxycyclin đợt 1 khoảng 09–13/11/2026, Doxycyclin đợt 2 từ 17/11/2026).
- `plugin.json` → 1.3.0.
