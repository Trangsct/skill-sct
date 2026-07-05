# Đọc PDF văn bản đến — trích metadata chính xác (hợp nhất từ vbhc-pdf-reader-vn)

> ### CẢNH BÁO CỨNG — làm trước mọi việc khác
> Khi nhận file PDF có dấu hiệu là văn bản nhà nước Việt Nam (tên file, dòng đầu context, hoặc bối cảnh hội thoại), **DỪNG mọi thao tác khác** và chạy ngay:
>
> ```bash
> python3 "/mnt/skills/plugins/vbhc-vn:vbhc-vn/scripts/extract_metadata.py" "<đường dẫn file>" # nếu cài dạng user skill thì thay bằng /mnt/skills/user/vbhc-vn/scripts/
> ```
>
> Quy tắc cứng, không ngoại lệ. KHÔNG tin số/ngày đọc từ context window; KHÔNG bỏ qua vì "context có vẻ đủ"; KHÔNG soạn văn bản trả lời/triển khai trước khi xác minh số/ngày bằng script. Việc bỏ qua đã gây ≥2 vụ dẫn chiếu sai (CV 3861/UBND-NC; CV 3954/UBND-VX) và **trong phiên gần đây cũng lặp lại** (context hiển thị "Số: /SYT-NVY" trống, file thật là 2861/SYT-NVY ngày 19/6/2026). Chi phí chạy: ~2 giây.

### Vì sao cần
VBHC Việt Nam (NĐ 30/2020, NĐ 78/2025, NĐ 187/2025) có **layout 2 cột** ở đầu (cơ quan | Quốc hiệu; Số/ngày là text-box độc lập) và 2 cột ở cuối (Nơi nhận | chức vụ-người ký). Khi PDF nạp tự động vào context, các text-box số/ngày/người ký thường bị **bỏ trống** hoặc **nối sai thứ tự**. Đây là lỗi pipeline phía Claude, không phải lỗi file gốc → bắt buộc đọc lại từ file gốc trên disk bằng script.

### Cờ kích hoạt (bất kỳ cờ nào)
1. Tên file chứa: CV/cong_van, QĐ/QD/quyet_dinh, TTr/to_trinh, BC/bao_cao, KH/ke_hoach, NQ, NĐ/ND, TT/thong_tu, UBND, BCT, BYT, BNN, SCT, STC, SNN, SXD, HĐND.
2. Dòng đầu file có: "ỦY BAN NHÂN DÂN", "BỘ ...", "SỞ ...", "HỘI ĐỒNG NHÂN DÂN", "CHÍNH PHỦ", "THỦ TƯỚNG", "QUỐC HỘI".
3. Context hiện: `Số: /UBND-...`, `Số: /BYT-...`, `ngày tháng năm`, hoặc bất kỳ trường số/ngày trống.
4. Người dùng nhắc: "PDF", "công văn đến", "văn bản đến", "file đính kèm", "đọc giúp", "tham gia ý kiến", "soạn công văn triển khai", "báo cáo theo chỉ đạo".
5. Hội thoại có mục đích soạn văn bản tham mưu/triển khai/trả lời dựa trên văn bản nguồn cấp trên.

### Quy trình 3 bước
**Bước 1 — Trích xuất**: chạy script trên. Output JSON 11 trường: `co_quan_ban_hanh`, `so_van_ban` (vd `3954/UBND-VX`, `05/2025/QĐ-UBND`, `59/QĐ-SCT`), `dia_danh_ngay`, `ngay_iso`, `loai_van_ban`, `trich_yeu`, `kinh_gui`, `nguoi_ky`, `chuc_vu_ky` (kèm KT./TM./TUQ./TL.), `noi_nhan`, `phuong_phap`.

**Bước 2 — OCR (nếu output phần lớn null)**: file có thể là scan ảnh thuần.
```bash
ocrmypdf --language vie+eng --force-ocr <input>.pdf /tmp/ocr_output.pdf
python3 "/mnt/skills/plugins/vbhc-vn:vbhc-vn/scripts/extract_metadata.py" /tmp/ocr_output.pdf # nếu cài dạng user skill thì thay bằng /mnt/skills/user/vbhc-vn/scripts/
```
Script đã tự fallback OCR khi `pdftotext` trả về <100 ký tự.

**Bước 3 — Debug**: thêm cờ `--raw` để in toàn bộ text gốc (`pdftotext -layout`) kiểm tra layout từng dòng.

### Chức vụ ký (đọc đúng thẩm quyền)
`KT.` = ký thay (Phó ký thay Trưởng); `TM.` = thay mặt tập thể; `TUQ.` = thừa uỷ quyền; `TL.` = thừa lệnh (thường kết hợp KT.); không tiền tố = người đứng đầu ký trực tiếp.

### KHÔNG LÀM
- Không chạy script khi nhận PDF VBHC (sai lầm chính — phải chạy NGAY).
- Bỏ qua vì "context đủ thông tin" — context không đáng tin với layout 2 cột.
- Dùng `pdftotext` thiếu cờ `-layout` (nối text-box sai thứ tự); dùng `cat`/`pypdf extract_text()` cho văn bản 2 cột; bỏ qua OCR khi pdftotext trả về rỗng.
- Soạn văn bản với số nguồn để trống "yêu cầu xác minh sau" khi file gốc đã có số trên disk.

### Khi nào chạy LẠI script
Khi cần dẫn chiếu chính xác số/ngày; soạn công văn trả lời/triển khai; tổng hợp danh mục VB đến/đi; context đã trôi nhiều lượt; người dùng nhắc lại PDF đã gửi từ lượt trước.
