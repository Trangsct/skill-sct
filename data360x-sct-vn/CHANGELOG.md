# data360x-sct-vn 1.0.5 — 17/9/2026 (f)

- Bot tải được **đính kèm trên Data360X** (tab *File đính kèm*): bắt Authorization + khuôn URL tải tệp từ Chrome, danh sách tệp từ JSON `get-attachs-by-id`; 3/3 tệp hồ sơ 9425/UBND-NC (PR ccn-laocai #81–#84). Token bị che trong log.
- Quy tắc 9 bổ sung: PDF chính bot lưu có thể là đính kèm đầu tiên — đối chiếu số ký hiệu ở từng `.md` trước khi trích dẫn; `tai_duoc: false` → xem log, không đoán. Ref 03 thêm mục 6 (cách tải đính kèm, dòng log để soi).

# data360x-sct-vn 1.0.4 — 17/9/2026 (e)

- Quy tắc 12b: đọc **luồng xử lý** (tab *Thông tin gửi, nhận*) trước khi chọn loại văn bản — Phòng chủ trì → văn bản của Sở, phối hợp → công văn nội bộ Phòng gửi phòng chủ trì, nhận để biết → không soạn; người xử lý chính = người soạn (Bạn chốt 17/9/2026). Bot ghi sẵn `vai_tro_phong`, `nguoi_xu_ly_chinh`, `han_xu_ly`.

# data360x-sct-vn 1.0.3 — 17/9/2026 (d)

- Quy tắc 10: tài liệu sau mã QR — bot quét QR trong PDF, tải từ Google Drive / trang web; không tải được thì đưa URL cho người dùng, không đoán.
- Quy tắc 11: từ khóa rộng bị chặn trần 12 văn bản. Quy tắc 12: Chrome bị đóng giữa lượt — bot tự mở lại, README luôn có.

# data360x-sct-vn 1.0.2 — 17/9/2026 (c)

- Quy tắc 8: từ khóa NGẮN (số trơn, tên riêng: `Xuân Ái`, `PH Group`) — Bạn chốt 17/9/2026; bot cũng tự rút gọn.
- Quy tắc 9: một hồ sơ có nhiều tệp — bot tải đủ đính kèm (.docx có bản chữ .md); đọc cả đính kèm khi góp ý dự thảo. Kịch bản 5 mới (9500/UBND-XD). Ref 01 thêm đường dẫn đính kèm.

# data360x-sct-vn 1.0.1 — 17/9/2026 (b)

- Bot tìm bằng **ô tìm kiếm** của Data360X thay vì lật từng trang (Bạn chốt 17/9/2026); `ngay` của workflow lấy văn bản chỉ còn là đường lui. Cập nhật SKILL.md, ref 01, ref 03.
- Máy cơ quan không có bash: workflow chuyển sang PowerShell, yêu cầu đi qua tệp UTF-8 (`--lay @tệp`).

# data360x-sct-vn 1.0.0 — 17/9/2026

Plugin mới. Bạn chốt 17/9/2026: *"Data360X giống như cánh tay, chuột và bàn phím của Claude"* — khi làm việc,
Claude biết kết hợp kho văn bản đã gom và biết giao bot vào Data360X tải đúng tài liệu đang cần.

- `SKILL.md`: bức tranh 30 giây; 7 quy tắc (tra kho trước, gộp một lệnh, số/ngày lấy ở đầu tệp, không bịa,
  công khai – riêng tư, không đổi lịch, máy phải bật); 4 động tác (tra kho, sai bot lấy, quét mới, tìm viện
  dẫn); bảng "khi nào tự dùng"; liên kết plugin khác.
- `references/01-kho-theo-doi.md`: cây thư mục `theo-doi/`, từng trường của bản ghi danh mục, bản tin, bảng
  lĩnh vực ↔ plugin, tiêu chí bot tải PDF, giới hạn.
- `references/02-workflows.md`: 5 workflow (4 nút bấm + đề xuất VBPL), inputs, cách gọi bằng MCP / gh /
  script / trang web, cách chờ, bảng đọc log lỗi, mã thoát của bot.
- `references/03-bot-va-may-co-quan.md`: chế độ dòng lệnh, ràng buộc (không đăng nhập hộ, không captcha),
  runner, phiên đăng nhập và giữ phiên hằng ngày, thứ tự kiểm tra khi bot hỏng.
- `references/04-kich-ban-mau.md`: 5 kịch bản có thật với lệnh từng bước và câu trả lời mẫu.
- `scripts/tim_trong_kho.py`: tra danh mục theo từ khóa / số / lĩnh vực / ngày / nguồn; `--ban-tin`; `--doc`;
  đọc từ bản clone hoặc GitHub API.
- `scripts/goi_bot.py`: gửi lệnh workflow, chờ (3 phút rồi mỗi 2 phút, tối đa 40 phút), in README kết quả
  hoặc bản tin; `trang-thai` xem nhịp tim máy.

Kèm theo ở kho khác (cùng ngày): bot `--lay` (ccn-laocai), workflow `lay-van-ban.yml` và `giu-phien.yml`
(vlncn-laocai).
