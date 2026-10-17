# trang-thai/ — trạng thái hồ sơ dùng chung xuyên phiên

Bạn chốt 17/10/2026. Mỗi hồ sơ đang làm một tệp `<slug>.md` theo `MAU.md`, để phiên Claude sau biết ngay
hồ sơ đang ở bước nào, Bạn đã quyết những gì, còn dở việc gì — không phải hỏi lại, không phải đọc lại cả lịch sử.

| Việc | Lệnh (chạy ở gốc kho) |
|---|---|
| Tìm tệp hồ sơ từ câu yêu cầu của Bạn | `python3 scripts/tim_ho_so.py "soạn công văn gửi xã về cụm Phú Thịnh 1"` |
| Liệt kê mọi hồ sơ, ngày cập nhật cuối, bước tiếp theo | `python3 scripts/trang_thai_ho_so.py [--plugin kccn-sct-vn]` |
| Tạo hồ sơ mới từ mẫu | `python3 scripts/ghi_nhat_ky.py --tao-moi "Tên hồ sơ" --bi-danh "a; b" --plugin kccn-sct-vn` |
| Ghi nhật ký cuối phiên | `python3 scripts/ghi_nhat_ky.py <slug hoặc bí danh> --viec "…" --van-ban "…" --xong "…" --tiep-theo "…"` |
| Kiểm cấu trúc (CI chạy qua `check_descriptions.py`) | `python3 scripts/check_trang_thai.py` |

Quy tắc dùng (chi tiết ở `CLAUDE.md` mục "Trạng thái hồ sơ" và "Kết thúc phiên"):

- Bạn nhắc đến một hồ sơ → chạy `tim_ho_so.py`, đọc tệp, dùng ngay; KHÔNG tóm tắt lại cho Bạn. Chỉ nêu một dòng
  khi tệp mâu thuẫn với yêu cầu (tệp ghi bước đã xong mà Bạn yêu cầu làm lại).
- Chưa có tệp → tạo mới từ mẫu ngay trong phiên, không hỏi.
- Kho công khai: chỉ tên công ty và số giấy phép nhà nước cấp; không số điện thoại, tài khoản, người đại diện,
  sức khỏe, đời tư. `ghi_nhat_ky.py` và `check_trang_thai.py` chặn các mẫu đó.
- Nhật ký quá 10 mục thì `ghi_nhat_ky.py` tự gộp các mục cũ thành "Tóm tắt đến ngày …".
- Thư mục này nằm ở gốc kho nên KHÔNG vào gói plugin trên claude.ai; phiên claude.ai không đọc được thì làm
  theo yêu cầu, cuối phiên đưa đoạn nhật ký để Bạn dán (hoặc tệp `.patch`).
