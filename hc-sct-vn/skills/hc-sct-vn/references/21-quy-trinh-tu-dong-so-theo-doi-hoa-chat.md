# 21 — Quy trình TỰ ĐỘNG của sổ theo dõi hóa chất: từ giấy phép Bạn gửi đến câu trả lời của Claude (Bạn chốt 07/11/2026)

Nguyên tắc Bạn chốt 07/11/2026: **"mọi thứ phải tự động, tôi sẽ không làm tay"**. Mọi bước dưới đây do máy làm; Claude trong
phiên chỉ làm đúng hai việc có dấu ★. Không có bước nào Bạn phải chép tệp, sửa CSV hay nâng phiên bản bằng tay.

## 1. Dây chuyền (một chiều, một nguồn sự thật)

```
Bạn gửi GP/GCN/hồ sơ (PDF quét, Word, rar)
   │
   ▼ ★ Claude đọc (OCR tesseract vie / pdftotext), nạp vào CSDL web bằng script nap_*.py (chạy lại được, không bịa)
CSDL web nội bộ  instance/vlncn.db  (kho riêng vlncn-laocai) — NGUỒN SỰ THẬT DUY NHẤT
   │  menu Hóa chất: Cơ sở · GP, GCN · Hồ sơ · KH, BP sự cố · Huấn luyện · Kiểm tra, xử phạt · Báo cáo DN · Thống kê · Văn bản
   │
   ▼ push main  →  workflow plugin-van-ban.yml (GitHub Actions, tự chạy)
   ├─ scripts/xuat_so_hoa_chat.py      → theo-doi/so-theo-doi-hoa-chat.csv  (đủ mã số DN, địa chỉ cơ sở)
   ├─ scripts/build_plugin_van_ban.py  → plugins/van-ban-sct-vn/.../data/so-theo-doi-hoa-chat.csv + nâng phiên bản plugin
   └─ git add plugins/… marketplace.json theo-doi/so-theo-doi-hoa-chat.csv → commit → push main
   │
   ├─▶ claude.ai tự đồng bộ marketplace vlncn-laocai-noi-bo → plugin van-ban-sct-vn trong mọi phiên chat có sổ mới
   │
   └─▶ máy chủ MCP sct-mcp (Vercel) đọc thẳng tệp đó trên GitHub mỗi lần gọi (không cache):
        tra_doanh_nghiep "<tên DN>"  →  so_theo_doi_hoa_chat (mã số DN, địa chỉ, hoạt động, hóa chất, GCN/GP,
                                        hồ sơ, KH/BP, kiểm tra, xử phạt, báo cáo), van_ban_so_theo_doi (toàn văn GP)
   │
   ▼ ★ Claude trả lời Bạn — GATE số 0 (ref 20): gọi tra_doanh_nghiep TRƯỚC, dẫn nguồn "sổ theo dõi hóa chất (web nội bộ)"
```

Kho công khai `skill-sct` (plugin này) chỉ giữ **bản rút gọn** `data/so-theo-doi-hoa-chat.csv` (tên công ty, số giấy phép;
không mã số DN, địa chỉ) làm lối vào khi MCP không kết nối. Bản rút gọn KHÔNG được chép tay từ bản đầy đủ; khi cần làm mới
thì chạy `xuat_csv()` của kho riêng với tham số rút gọn — việc này hiếm, vì MCP mới là đường chính.

## 2. Hai việc Claude làm trong phiên (★)

| Khi | Claude làm | Không làm |
|---|---|---|
| Bạn gửi GP/GCN/biên bản/hồ sơ hóa chất mới | Đọc bằng script (số, ngày, cơ quan từ chính tệp — PDF ký số phải `extract_metadata.py`); viết/bổ sung script `scripts/nap_hoa_chat_<ngày>.py` ở kho riêng, chạy, kiểm tra trang web 200, commit `instance/vlncn.db` + bản gốc sang `vlncn-laocai-files/uploads/hoa-chat/`, mở PR và merge ngay (quy tắc kho riêng). Chỗ chưa đọc được ghi `verify_note "[CẦN ĐỐI CHIẾU]"`. | Không sửa tay CSV ở bất kỳ kho nào; không chép dữ liệu mã số/địa chỉ sang kho công khai; không nâng phiên bản plugin riêng bằng tay (workflow tự nâng). |
| Bạn hỏi về một DN hóa chất | Gọi `tra_doanh_nghiep` trước (ref 20 GATE 0); cần toàn văn thì `tra_van_ban_den_di "<số GP>"`; MCP không kết nối thì mở `data/so-theo-doi-hoa-chat.csv` + plugin `van-ban-sct-vn` `tim.py`. | Không nói "chưa có trong sổ" khi chưa tra cả hai đường. |

Khi nạp đợt mới mà xuất hiện **loại dữ liệu chưa có cột** (ví dụ ngày diễn tập, số người huấn luyện): thêm cột ở `models.py`,
một dòng trong `MODULES[...]['fields']` của `hoa_chat.py`, và cột tương ứng trong `xuat_csv()`; workflow sẽ tự đưa cột mới ra
plugin và MCP ở lượt kế tiếp. Nâng `tra_doanh_nghiep` chỉ khi muốn MCP hiểu nghĩa cột mới.

## 3. Kiểm tra dây chuyền đang sống (khi nghi ngờ dữ liệu cũ)

1. Kho riêng → Actions → *Dung plugin van-ban-sct-vn*: lượt mới nhất phải xanh và có commit "Plugin van-ban-sct-vn: dung lai tu
   du lieu moi HH:MM_dd/mm/yyyy" ngay sau commit dữ liệu.
2. Gọi `tra_doanh_nghiep` với một DN vừa nạp: phải có khối `so_theo_doi_hoa_chat` và nguồn "sổ theo dõi hóa chất (web nội bộ)".
3. Trong phiên chat claude.ai: plugin `van-ban-sct-vn` phiên bản dạng `1.YYYYMMDD.HHMM` phải mới hơn giờ nạp.

Lỗi đã gặp và đã sửa: lượt 641 (07/11/2026 08:16) đỏ vì bước lưu chỉ `git add plugins/…`, tệp CSV vừa xuất ở `theo-doi/` còn
unstaged nên `git pull --rebase` từ chối. Sửa: thêm tệp đó vào `git add` (PR #163 kho riêng); từ đó lượt 642 xanh. Nếu lại đỏ với
"cannot pull with rebase: You have unstaged changes" thì có tệp mới sinh ngoài danh sách `git add` — bổ sung vào danh sách,
không xóa bước xuất.

## 4. Ranh giới công khai — riêng tư (không đổi)

- Kho riêng `vlncn-laocai` (CSDL, sổ đủ cột, plugin van-ban-sct-vn) và MCP có khóa: mã số DN, địa chỉ cơ sở (thông tin đăng ký
  doanh nghiệp là công khai — Bạn chốt 06/11/2026). **Không bao giờ**: số điện thoại, người đại diện, CCCD, tài khoản, ở mọi bản.
- Kho công khai `skill-sct`: tên công ty, số giấy phép nhà nước cấp, tóm tắt nghiệp vụ (ref 20); `check_trang_thai.py` và
  `check_facts.py` chặn khi lộ mẫu cấm.
