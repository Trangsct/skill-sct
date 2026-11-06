---
name: tra-cuu-sct-vn
description: "MÁY CHỦ TRA CỨU MCP của bộ plugin Sở Công Thương Lào Cai (16 công cụ chỉ đọc, đọc thẳng kho GitHub, luôn mới). Kích hoạt khi cần: tra văn bản gốc, toàn văn, hiệu lực pháp luật; trạng thái hồ sơ một cụm công nghiệp; danh mục khu, cụm công nghiệp; tìm từ khóa trong tài liệu tham khảo; soạn bất kỳ văn bản nào của Sở (gói bối cảnh, người ký, kiểm tra dữ kiện); thẩm định hồ sơ (checklist, đối chiếu); lập báo cáo (số liệu); thống kê; 'việc hôm nay', 'việc chờ xử lý'. Gọi công cụ máy chủ TRƯỚC; máy chủ không kết nối thì dùng script, tài liệu plugin như cũ; không bao giờ coi kết quả rỗng là 'không có văn bản' khi chưa tra bằng cả hai cách."
---

# tra-cuu-sct-vn — gắn máy chủ tra cứu MCP vào bộ plugin

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
- Tra văn bản đến, đi, doanh nghiệp → `tra_van_ban_den_di`, `tra_doanh_nghiep` (từ 06/11/2026 `tra_doanh_nghiep` trả thêm `so_theo_doi_plugin`: dòng sổ theo dõi cơ sở hoạt động hóa chất của plugin hc-sct-vn — GCN/GP đã cấp, hồ sơ, Kế hoạch/Biện pháp, kiểm tra, báo cáo; sổ văn bản có bản chữ OCR 39 GCN/GP hóa chất 2018–2026). Máy chủ trả "chưa được cấp quyền kho văn bản"
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
