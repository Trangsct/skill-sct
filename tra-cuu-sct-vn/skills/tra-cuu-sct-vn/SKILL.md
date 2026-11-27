---
name: tra-cuu-sct-vn
description: "MÁY CHỦ TRA CỨU MCP của bộ plugin Sở Công Thương Lào Cai (16 công cụ chỉ đọc, đọc thẳng kho GitHub, luôn mới). Kích hoạt khi cần: tra văn bản gốc, toàn văn, hiệu lực pháp luật; trạng thái hồ sơ một cụm công nghiệp; danh mục khu, cụm công nghiệp; tìm từ khóa trong tài liệu tham khảo; soạn bất kỳ văn bản nào của Sở (gói bối cảnh, người ký, kiểm tra dữ kiện); thẩm định hồ sơ (checklist, đối chiếu); lập báo cáo (số liệu); thống kê; 'việc hôm nay', 'việc chờ xử lý'. Gọi công cụ máy chủ TRƯỚC; máy chủ không kết nối thì dùng script, tài liệu plugin như cũ; không bao giờ coi kết quả rỗng là 'không có văn bản' khi chưa tra bằng cả hai cách."
---

# tra-cuu-sct-vn — gắn máy chủ tra cứu MCP vào bộ plugin

> **Lấy toàn văn văn bản quy phạm pháp luật từ thuvienphapluat.vn — TỰ ĐỘNG, không chờ Bạn nhắc (Bạn chốt 27/11/2026; quy trình đã chạy được 26/11/2026; áp dụng mọi plugin):** cần toàn văn một luật, nghị định, thông tư, quyết định… mà MCP `sct-tra-cuu` (`tra_phap_luat`, `tra_van_ban`, `tra_reference`) và `scripts/tim_van_ban.py` đều không có (thường là văn bản ngoài lĩnh vực công thương, vd Nghị định 335/2025/NĐ-CP về đánh giá công chức) thì tự lấy qua trình duyệt trên máy Bạn, không hỏi lại: (1) WebSearch chỉ dùng để tìm đường dẫn trang văn bản trên thuvienphapluat.vn (bản tóm tắt của báo không thay được toàn văn); WebFetch bị chặn ở thuvienphapluat.vn, luatnguyen, congbao.chinhphu.vn — không thử lại, không vòng qua bằng curl; (2) nạp công cụ Claude in Chrome trong MỘT lần ToolSearch (`list_connected_browsers`, `select_browser`, `tabs_context_mcp`, `tabs_create_mcp`, `navigate`, `get_page_text`, `javascript_tool`, `computer`, `tabs_close_mcp`); máy có 2 Chrome kết nối thì `select_browser` trước, Bạn không chỉ định thì chọn Browser 1; Chrome không kết nối thì làm y các bước bằng trình duyệt tích hợp của ứng dụng Claude; (3) mở tab mới (`tabs_context_mcp` createIfEmpty) → `navigate` tới trang văn bản → `get_page_text`; (4) `get_page_text` cắt ở 50.000 ký tự nên thường mất Phụ lục, mẫu biểu ở cuối — đây là giới hạn công cụ, KHÔNG phải trang chặn, không vội kết luận phải đăng nhập; lấy phần còn thiếu bằng `javascript_tool`: đọc `document.body.innerText`, cắt từ mốc (vd `lastIndexOf('PHỤ LỤC II')`), chuẩn hóa bớt xuống dòng và chuỗi dấu chấm, gán vào biến `window.__vb` rồi trả từng khúc khoảng 1.000–1.600 ký tự, ghép đủ đến hết văn bản; (5) trang đòi đăng nhập: tài khoản cơ quan đã lưu sẵn trong Chrome, chỉ bấm nút Đăng nhập, KHÔNG BAO GIỜ gõ mật khẩu; tài khoản dùng chung tối đa 5 người — hiện cảnh báo "có 1 người khác bị Đăng xuất" thì bấm Đồng ý luôn, không hỏi Bạn (quy tắc cơ quan: nhiều người đăng nhập thì ưu tiên người đăng nhập sau, người đang làm; người đăng nhập trước thường lấy văn bản xong để treo — Bạn chốt 27/11/2026); (6) lấy xong đóng tab (`tabs_close_mcp`); (7) đối chiếu số, ngày, cơ quan ban hành, trích yếu trên trang với văn bản cần tìm (số trùng khác năm là văn bản khác: 303/2025 ≠ 303/2026); (8) lưu vào kho để lần sau không phải lấy lại: tệp `.txt` toàn văn đặt tên `YYYY.MM.DD-SỐ.KÝ.HIỆU-Tên-trích-yếu-ngắn.txt`, dòng đầu ghi "Nguồn: thuvienphapluat.vn, lấy ngày dd/mm/yyyy", vào `van-ban-goc/` của plugin chủ theo lĩnh vực (ngoài mọi lĩnh vực → `vbhc-vn`), chạy `scripts/build_so_cai_van_ban_goc.py`, push, mở PR và merge; phiên không có quyền ghi kho thì vẫn giao tệp và hướng dẫn Bạn nạp qua Hộp thư `_inbox/`; (9) Bạn cần file thì dựng Word: Times New Roman 13, lề trên, dưới 2 cm, trái 3 cm, phải 2 cm; Chương, Mục, tiêu đề in đậm căn giữa; "Điều n." in đậm; soi bản PDF kiểm tra trang trắng rồi mới giao. Chỉ khi cả Chrome lẫn trình duyệt tích hợp không kết nối được, hoặc trang không có văn bản, mới báo Bạn tải bổ sung.

Máy chủ `sct-tra-cuu` (kho mã `sct-mcp`, chạy trên Vercel) đọc thẳng dữ liệu của bộ plugin và sổ theo dõi văn bản trên GitHub,
nên mọi nơi dùng Claude (Claude Code, Claude desktop, Antigravity) tra được cùng một nguồn, luôn mới, không phải mở từng tệp.
Plugin lĩnh vực vẫn là nơi hướng dẫn cách làm (thể thức, giọng văn, mẫu, GATE); máy chủ chỉ tra dữ liệu.

## Nguyên tắc

1. Cần tra văn bản, toàn văn, trạng thái hồ sơ một cụm, danh mục khu cụm, từ khóa trong tài liệu tham khảo → **gọi công cụ của
   máy chủ này trước** (`tra_van_ban`, `doc_van_ban`, `trang_thai_cum`, `danh_muc_kcn_ccn`, `tra_reference`, `tra_phap_luat`).
2. Máy chủ không kết nối được (không thấy công cụ `sct-tra-cuu` trong `/mcp`, hoặc lỗi mạng) → dùng script và tài liệu trong
   plugin như cũ: `scripts/tim_van_ban.py`, `van-ban-goc/00-DANH-MUC-CHUNG.md`, `kccn-sct-vn/scripts/trang_thai_cum.py`,
   `scripts/tim_ho_so.py`, references 12, 13 của kccn-sct-vn.
3. **Không bao giờ coi kết quả rỗng là "không có văn bản"** khi chưa tra bằng cả hai cách (máy chủ và script/tài liệu plugin).
   Chỉ khi cả hai không thấy mới được nói "chưa có bản gốc trong kho" và hướng dẫn nạp qua Hộp thư `_inbox/`.
4. Mọi kết quả máy chủ đều ghi nguồn (tệp, dòng); mục "không có dữ liệu" nghĩa là kho chưa ghi → bôi tím hoặc hỏi Bạn,
   tuyệt đối không bịa số, ngày, tên. Dữ liệu có ở nhiều nguồn thì máy chủ lấy nguồn mới nhất và ghi ngày nguồn.

## Quy trình bắt buộc khi SOẠN VĂN BẢN

1. Gọi `goi_boi_canh_soan_thao(doi_tuong, loai_van_ban, linh_vuc)` → nhận diện, trạng thái hồ sơ, văn bản liên quan, quy tắc
   riêng, văn bản bị cấm ở bậc hiện tại, mẫu gần nhất. Văn bản định soạn nằm trong mục "bị cấm" → không soạn, báo lại Bạn.
2. Gọi `nguoi_ky_va_luong_trinh(linh_vuc, loai_van_ban, ngay_ky)` → người ký, khối ký, ký hiệu, dòng Lưu, kiểm duyệt.
3. Viết văn bản theo GATE 0, 0b của `vbhc-vn` (kế hoạch soạn, dàn ý) và quy tắc plugin lĩnh vực.
4. Viết xong gọi `kiem_tra_du_kien(noi_dung)` với toàn bộ phần căn cứ và các đoạn có số, ngày, tên → sửa mọi "SAI LỆCH",
   bôi tím mọi "không tìm thấy".
5. Rồi mới dựng file Word bằng `vbhc-vn` và chạy `kiem_tra_truoc_khi_giao.py`.

## Quy trình khi THẨM ĐỊNH HỒ SƠ

Gọi `checklist_tham_dinh(loai_ho_so, ngay_nop)` rồi `doi_chieu_ho_so(loai_ho_so, noi_dung_ho_so)` (nội dung Claude đã đọc từ
PDF) TRƯỚC khi viết biên bản, phiếu nhận xét hay công văn hoàn thiện hồ sơ. Kết quả "đạt" chỉ nghĩa là hồ sơ có nhắc đến;
điều kiện định lượng, hiệu lực phải tự đọc hồ sơ kết luận; máy chủ không kết luận cấp hay không cấp.

## Quy trình khi LẬP BÁO CÁO, THỐNG KÊ, THEO DÕI VIỆC

- Lập báo cáo định kỳ, đột xuất → `so_lieu_bao_cao(linh_vuc, ky, mau)`; mỗi số dùng phải kèm nguồn và ngày chốt như máy chủ trả;
  số đánh "ước" ghi rõ "ước"; chỗ "chưa có" thì ghi "chưa có", không ước thay, không nội suy giữa hai kỳ.
- Đếm văn bản đi đến theo kỳ, sản lượng công việc, số giấy phép theo tháng, số cụm theo nhóm → `thong_ke(doi_tuong, …)`.
- Bạn hỏi "việc hôm nay", "việc chờ xử lý", "việc của Phòng" → `viec_cho_xu_ly(pham_vi, trang_thai)`; việc có liên quan
  một cụm thì máy chủ gợi ý loại văn bản cần soạn theo bậc thủ tục.
- Tra văn bản đến, đi, doanh nghiệp → `tra_van_ban_den_di`, `tra_doanh_nghiep` (từ 06/11/2026 `tra_doanh_nghiep` trả thêm `so_theo_doi_plugin`: dòng sổ theo dõi cơ sở hoạt động hóa chất của plugin hc-sct-vn — GCN/GP đã cấp, hồ sơ, Kế hoạch/Biện pháp, kiểm tra, báo cáo; sổ văn bản có bản chữ OCR 39 GCN/GP hóa chất 2018–2026; từ 07/11/2026 (máy chủ 1.0.2) trả thêm `so_theo_doi_hoa_chat`, mã số DN, địa chỉ cơ sở đọc từ sổ theo dõi hóa chất do web nội bộ tự xuất — kho riêng, cần quyền). Máy chủ trả "chưa được cấp quyền kho văn bản"
  thì dùng plugin `van-ban-sct-vn` trong phiên, không báo lỗi.

## Danh sách công cụ

| Nhóm | Công cụ |
|---|---|
| Tra cứu | `tra_van_ban`, `doc_van_ban`, `trang_thai_cum`, `danh_muc_kcn_ccn`, `tra_reference` |
| Soạn thảo | `goi_boi_canh_soan_thao`, `nguoi_ky_va_luong_trinh`, `tra_van_ban_den_di`, `tra_doanh_nghiep`, `kiem_tra_du_kien` |
| Thẩm định, báo cáo, thống kê, việc | `checklist_tham_dinh`, `doi_chieu_ho_so`, `so_lieu_bao_cao`, `thong_ke`, `viec_cho_xu_ly`, `tra_phap_luat` |

Cách khai báo `SCT_MCP_URL`, `SCT_MCP_TOKEN` trên máy và kiểm tra bằng `/mcp`: `README.md` của plugin này. Hai tệp dữ liệu máy
chủ đọc là `kccn-sct-vn/skills/kccn-sct-vn/data/danh-muc-kcn-ccn-qd525.csv` và
`sct-laocai-org-vn/skills/sct-laocai-org-vn/data/phan-cong-ky.json` — khi sửa reference 12, 13 hoặc phân công ký thì sửa hai tệp này cùng đợt.

## Sổ theo dõi hóa chất đi đường tự động (Bạn chốt 07/11/2026)

`tra_doanh_nghiep "<tên DN>"` là đường chính để biết một doanh nghiệp hóa chất đã có GCN/GP, hồ sơ, KH/BP, kiểm tra, báo cáo gì:
khối `so_theo_doi_hoa_chat` (kèm mã số DN, địa chỉ cơ sở) đọc từ `data/so-theo-doi-hoa-chat.csv` của plugin riêng `van-ban-sct-vn`,
tệp này do workflow `plugin-van-ban.yml` của kho riêng tự xuất từ CSDL web nội bộ sau mỗi lần nạp — không ai chép tay. Nghi dữ liệu
cũ: xem lượt Actions mới nhất của kho riêng xanh chưa, rồi gọi lại. Sơ đồ đầy đủ và việc Claude được/không được làm: plugin
`hc-sct-vn` reference 21.
