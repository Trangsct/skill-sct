---
name: ho-so-sct-vn
description: "TRẠNG THÁI HỒ SƠ đang làm của Sở Công Thương Lào Cai — đọc TRƯỚC khi soạn bất kỳ văn bản nào gắn với một hồ sơ cụ thể. Kích hoạt: tên cụm công nghiệp (Phú Thịnh 1, Thống Nhất 1, Mông Sơn, Châu Quế…), 'ủy quyền Giám đốc Sở', 'Bài toán lớn số 2', 'BT2', 'Làng Cang 2', 'Kế hoạch 130', 'hồ sơ đang ở bước nào', 'đã có văn bản gì', 'việc còn dở', 'nhật ký phiên'. Mỗi hồ sơ một tệp trang-thai/slug.md: văn bản đã phát hành (số, ngày, cơ quan, tệp gốc), bước đã xong, bước tiếp theo, vướng mắc, quyết định của Bạn trong các phiên, yêu cầu riêng một lần, nhật ký phiên. Script: tim_ho_so.py (chọn tệp từ câu yêu cầu theo bí danh), trang_thai_ho_so.py (bảng tổng hợp), ghi_nhat_ky.py (ghi nhật ký cuối phiên; trong gói claude.ai dùng --tam rồi đưa Bạn dán). Bản chép từ trang-thai/ gốc kho skill-sct, máy đồng bộ, không sửa tay."
---

# ho-so-sct-vn — trạng thái hồ sơ dùng chung xuyên phiên

> **Lấy toàn văn văn bản quy phạm pháp luật từ thuvienphapluat.vn — TỰ ĐỘNG, không chờ Bạn nhắc (Bạn chốt 27/11/2026; quy trình đã chạy được 26/11/2026; áp dụng mọi plugin):** cần toàn văn một luật, nghị định, thông tư, quyết định… mà MCP `sct-tra-cuu` (`tra_phap_luat`, `tra_van_ban`, `tra_reference`) và `scripts/tim_van_ban.py` đều không có (thường là văn bản ngoài lĩnh vực công thương, vd Nghị định 335/2025/NĐ-CP về đánh giá công chức) thì tự lấy qua trình duyệt trên máy Bạn, không hỏi lại: (1) WebSearch chỉ dùng để tìm đường dẫn trang văn bản trên thuvienphapluat.vn (bản tóm tắt của báo không thay được toàn văn); WebFetch bị chặn ở thuvienphapluat.vn, luatnguyen, congbao.chinhphu.vn — không thử lại, không vòng qua bằng curl; (2) nạp công cụ Claude in Chrome trong MỘT lần ToolSearch (`list_connected_browsers`, `select_browser`, `tabs_context_mcp`, `tabs_create_mcp`, `navigate`, `get_page_text`, `javascript_tool`, `computer`, `tabs_close_mcp`); máy có 2 Chrome kết nối thì `select_browser` trước, Bạn không chỉ định thì chọn Browser 1; Chrome không kết nối thì làm y các bước bằng trình duyệt tích hợp của ứng dụng Claude; (3) mở tab mới (`tabs_context_mcp` createIfEmpty) → `navigate` tới trang văn bản → `get_page_text`; (4) `get_page_text` cắt ở 50.000 ký tự nên thường mất Phụ lục, mẫu biểu ở cuối — đây là giới hạn công cụ, KHÔNG phải trang chặn, không vội kết luận phải đăng nhập; lấy phần còn thiếu bằng `javascript_tool`: đọc `document.body.innerText`, cắt từ mốc (vd `lastIndexOf('PHỤ LỤC II')`), chuẩn hóa bớt xuống dòng và chuỗi dấu chấm, gán vào biến `window.__vb` rồi trả từng khúc khoảng 1.000–1.600 ký tự, ghép đủ đến hết văn bản; (5) trang đòi đăng nhập: tài khoản cơ quan đã lưu sẵn trong Chrome, chỉ bấm nút Đăng nhập, KHÔNG BAO GIỜ gõ mật khẩu; tài khoản dùng chung tối đa 5 người — hiện cảnh báo "có 1 người khác bị Đăng xuất" thì bấm Đồng ý luôn, không hỏi Bạn (quy tắc cơ quan: nhiều người đăng nhập thì ưu tiên người đăng nhập sau, người đang làm; người đăng nhập trước thường lấy văn bản xong để treo — Bạn chốt 27/11/2026); (6) lấy xong đóng tab (`tabs_close_mcp`); (7) đối chiếu số, ngày, cơ quan ban hành, trích yếu trên trang với văn bản cần tìm (số trùng khác năm là văn bản khác: 303/2025 ≠ 303/2026); (8) lưu vào kho để lần sau không phải lấy lại: tệp `.txt` toàn văn đặt tên `YYYY.MM.DD-SỐ.KÝ.HIỆU-Tên-trích-yếu-ngắn.txt`, dòng đầu ghi "Nguồn: thuvienphapluat.vn, lấy ngày dd/mm/yyyy", vào `van-ban-goc/` của plugin chủ theo lĩnh vực (ngoài mọi lĩnh vực → `vbhc-vn`), chạy `scripts/build_so_cai_van_ban_goc.py`, push, mở PR và merge; phiên không có quyền ghi kho thì vẫn giao tệp và hướng dẫn Bạn nạp qua Hộp thư `_inbox/`; (9) Bạn cần file thì dựng Word: Times New Roman 13, lề trên, dưới 2 cm, trái 3 cm, phải 2 cm; Chương, Mục, tiêu đề in đậm căn giữa; "Điều n." in đậm; soi bản PDF kiểm tra trang trắng rồi mới giao. Chỉ khi cả Chrome lẫn trình duyệt tích hợp không kết nối được, hoặc trang không có văn bản, mới báo Bạn tải bổ sung.

Bạn chốt 17/10/2026 (bản giao việc mục 5, 6): mỗi hồ sơ đang làm một tệp `trang-thai/slug.md` theo `trang-thai/MAU.md`,
để phiên sau biết ngay hồ sơ ở bước nào, Bạn đã quyết gì, còn dở việc gì — không phải kể lại từ đầu. Plugin này là
**bản chép** của `trang-thai/` và `scripts/` ở gốc kho `Trangsct/skill-sct` (máy sinh bởi `scripts/build_ho_so_plugin.py`,
CI kiểm khớp) để phiên trên claude.ai đọc được; nguồn chuẩn vẫn ở gốc kho.

## GATE "Đọc trạng thái hồ sơ" — chạy trước mọi việc soạn thảo gắn một hồ sơ

1. Bạn nhắc đến một hồ sơ (tên cụm, tên dự án, "BT2", "ủy quyền"…) → chạy ngay:
   `python3 <thư mục skill>/scripts/tim_ho_so.py "<câu yêu cầu của Bạn>"` → mở tệp nó chỉ ra, **dùng ngay nội dung**:
   văn bản đã phát hành (số, ngày, tệp gốc), bước hiện tại, quyết định Bạn đã chốt, yêu cầu riêng một lần.
2. **Không tóm tắt lại hồ sơ cho Bạn** (Bạn đã biết hồ sơ của mình). Chỉ nêu MỘT dòng khi tệp mâu thuẫn với yêu cầu
   (tệp ghi bước đã xong mà Bạn yêu cầu làm lại; tệp ghi Bạn đã quyết khác).
3. Tệp mới hơn tài liệu plugin lĩnh vực: dữ liệu plugin cũ quá 7 ngày thì lấy bậc theo mục "Bước đã xong", "Nhật ký
   phiên" của tệp; chỉ hỏi Bạn khi tệp cũng không rõ.
4. Không có tệp khớp (`tim_ho_so.py` trả mã 1): làm theo yêu cầu, cuối phiên ghi nhật ký tạm (mục dưới) kèm `--tao-moi`.

Tổng hợp mọi hồ sơ: `python3 <thư mục skill>/scripts/trang_thai_ho_so.py [--plugin kccn-sct-vn]`.
Hồ sơ CCN/KCN: `kccn-sct-vn/scripts/trang_thai_cum.py` vẫn dùng như cũ để tra bậc thủ tục trong tài liệu plugin.

## Kết thúc phiên — nhật ký (không chờ Bạn nhắc)

Khi Bạn nói xong, cảm ơn, chuyển việc khác, hoặc khi giao văn bản cuối của phiên:

- Trong gói claude.ai, thư mục skill **chỉ đọc** → chạy với `--tam` ở thư mục làm việc:
  `python3 <thư mục skill>/scripts/ghi_nhat_ky.py "<slug/bí danh>" --viec "…" --van-ban "<tên tệp> (bản N)"
  --quyet-dinh "…" --viec-do "…" --cau-hoi "…" --xong "…" --tiep-theo "…" --tam`
  → sinh `nhat-ky-tam.json`; đưa Bạn tệp này (hoặc dán nội dung JSON) kèm câu: "Dán vào kho: tại gốc skill-sct chạy
  `python3 scripts/ghi_nhat_ky.py --nap-tam nhat-ky-tam.json` rồi commit". Hồ sơ chưa có tệp: thêm
  `--tao-moi "<Tên hồ sơ>" --bi-danh "a; b" --plugin <plugin>`.
- Trong phiên Claude Code có kho: chạy không `--tam`, script sửa thẳng `trang-thai/` gốc kho và tự đồng bộ bản chép.
- "Đã ghi nhật ký" là một vế trong câu báo cuối khi giao file, không báo riêng.
- Kho công khai: chỉ tên công ty và số giấy phép nhà nước cấp; KHÔNG số điện thoại, tài khoản, người đại diện, sức
  khỏe, đời tư — script từ chối ghi (mã 3) khi gặp.

## Tệp trong gói

| Tệp | Nội dung |
|---|---|
| `trang-thai/MAU.md` | Mẫu 7 mục; `trang-thai/README.md` cách dùng |
| `trang-thai/ccn-*.md` | 4 cụm công nghiệp đang làm (Phú Thịnh 1, Thống Nhất 1, Mông Sơn, Châu Quế) |
| `trang-thai/uy-quyen-gd-sct.md` | 5 QĐ ủy quyền đã ban hành, dự thảo QĐ ủy quyền chung, việc còn mở |
| `trang-thai/bai-toan-lon-so-2.md` | Kế hoạch Bài toán lớn số 2 |
| `trang-thai/tan-thu-da-thai-lang-cang-2.md`, `kh-130-cong-nghiep-vat-lieu.md` | chưa có dữ kiện trong kho — Bạn gửi văn bản là điền |
| `scripts/tim_ho_so.py`, `trang_thai_ho_so.py`, `ghi_nhat_ky.py`, `check_trang_thai.py`, `trang_thai_lib.py` | như trên |
