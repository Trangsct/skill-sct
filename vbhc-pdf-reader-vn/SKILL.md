---
name: vbhc-pdf-reader-vn
description: "SENTINEL — PHẢI CHẠY NGAY mỗi khi nhận PDF có vẻ là văn bản nhà nước VN, không chờ phát hiện thiếu thông tin. Trích chính xác metadata (số văn bản, ngày, cơ quan, người ký, trích yếu, nơi nhận) từ PDF VBHC/QPPL Việt Nam. Vấn đề: PDF VBHC layout 2 cột với text-box độc lập cho số/ngày, khi nạp vào context các vùng này thường trống hoặc nối sai. Triggers: tên file chứa CV, QĐ, TTr, BC, KH, NQ, NĐ, TT, BYT, BNN, BCT, SYT, UBND, HĐND, SCT; cụm 'PDF', 'công văn đến', 'văn bản đến', 'file đính kèm', 'đọc giúp', 'tham gia ý kiến', 'soạn công văn triển khai', 'triển khai văn bản', 'báo cáo theo chỉ đạo'; context có 'Số: /UBND-...', 'ngày tháng năm 20...' bị trống. Từ khoá: công văn, quyết định, tờ trình, kế hoạch, báo cáo, nghị quyết, nghị định, thông tư, UBND, HĐND, Bộ, Sở, KT., TM., TUQ., TL., người ký, trích yếu, nơi nhận."
---

# vbhc-pdf-reader-vn v2.0 — Lính gác đọc PDF văn bản hành chính Việt Nam

> Vai trò từ v2.0: skill này là **SENTINEL (lính gác)** — nhiệm vụ duy nhất là bảo đảm
> quy tắc "chạy script trước, soạn thảo sau" được thi hành ngay ở lượt đầu tiên nhận PDF.
> Toàn bộ chi tiết nghiệp vụ (pattern số văn bản, chức vụ ký, ví dụ vụ thật, quy trình OCR
> đầy đủ) đã hợp nhất vào plugin **vbhc-vn** — đọc
> `reference/doc-pdf-metadata.md` của plugin khi cần tra sâu. KHÔNG lặp lại ở đây để
> tiết kiệm ngữ cảnh.

## ⚠️ QUY TẮC CỨNG — KHÔNG NGOẠI LỆ

Trong lượt hiện tại, nếu nhận được file PDF có dấu hiệu là văn bản nhà nước Việt Nam
(tên file, dòng đầu context, hoặc bối cảnh hội thoại gợi ý), **DỪNG mọi thao tác khác**
và chạy ngay:

```bash
python3 /mnt/skills/user/vbhc-pdf-reader-vn/scripts/extract_metadata.py "<đường dẫn file>"
# Nếu skill này không có trên disk (chỉ cài plugin), dùng bản giống hệt trong plugin:
# python3 "/mnt/skills/plugins/vbhc-vn:vbhc-vn/scripts/extract_metadata.py" "<đường dẫn file>"
```

KHÔNG được:
- Tin số văn bản/ngày tháng đọc từ context window khi nguồn là PDF.
- Bỏ qua vì "context đã có vẻ đủ thông tin".
- Soạn văn bản trả lời/triển khai trước khi xác minh số/ngày bằng script.

Bỏ qua quy tắc này đã gây **3 vụ dẫn chiếu sai** trong công việc thực tế:

| Vụ | Số văn bản đúng | Context hiển thị |
|---|---|---|
| CV UBND tỉnh về ĐVHD | 3861/UBND-NC, 15/5/2026 | "Số: /UBND-NC", ngày trống |
| CV UBND tỉnh về Đề án ATTP | 3954/UBND-VX, 17/5/2026 | "Số: /UBND-VX", ngày trống |
| CV Sở Y tế | 2861/SYT-NVY, 19/6/2026 | "Số: /SYT-NVY" trống |

Chi phí chạy: ~2 giây. Chi phí bỏ qua: sửa tay từng chỗ, hoặc văn bản trình ký sai số/ngày.

## Cờ kích hoạt (bất kỳ cờ nào)

1. **Tên file** chứa: CV/cong_van, QĐ/QD/quyet_dinh, TTr/to_trinh, BC/bao_cao, KH/ke_hoach, NQ, NĐ/ND, TT/thong_tu, UBND, HĐND, BCT, BYT, BNN, SYT, SCT, STC, SNN, SXD.
2. **Dòng đầu context** có: "ỦY BAN NHÂN DÂN", "BỘ ...", "SỞ ...", "HỘI ĐỒNG NHÂN DÂN", "CHÍNH PHỦ", "THỦ TƯỚNG", "QUỐC HỘI".
3. **Context** hiện trường số/ngày trống: `Số:    /UBND-...`, `ngày      tháng      năm`.
4. **Người dùng nhắc**: "PDF", "công văn đến", "văn bản đến", "file đính kèm", "đọc giúp", "tham gia ý kiến", "soạn công văn triển khai", "báo cáo theo chỉ đạo".
5. **Hội thoại có mục đích** soạn văn bản tham mưu/triển khai/trả lời dựa trên văn bản nguồn cấp trên.

## Quy trình rút gọn

1. **Chạy script** (lệnh trên) → JSON 11 trường: `co_quan_ban_hanh`, `so_van_ban`, `dia_danh_ngay`, `ngay_iso`, `loai_van_ban`, `trich_yeu`, `kinh_gui`, `nguoi_ky`, `chuc_vu_ky`, `noi_nhan`, `phuong_phap`.
2. **Nếu phần lớn trường null** → PDF scan ảnh: `ocrmypdf --language vie+eng --force-ocr in.pdf /tmp/ocr.pdf` rồi chạy lại script (script cũng tự fallback OCR khi pdftotext trả về <100 ký tự).
3. **Debug**: thêm cờ `--raw` để in text gốc theo layout.
4. **Chạy LẠI** khi: cần dẫn chiếu chính xác; soạn văn bản trả lời/triển khai; context đã trôi nhiều lượt; người dùng nhắc lại PDF từ lượt trước.

Quy ước riêng của Bạn: nếu không đọc được người ký, KHÔNG cần OCR lại — chỉ cần số văn bản + ngày là đủ.

## Liên kết

- **Plugin vbhc-vn** (`/mnt/skills/plugins/vbhc-vn:vbhc-vn/`):
  - `reference/doc-pdf-metadata.md` — quy trình đầy đủ, pattern số văn bản, bảng chức vụ ký (KT./TM./TUQ./TL.), danh mục KHÔNG LÀM.
  - Mục "Phòng tránh 8 nhóm sai lầm tham mưu", Nhóm E — tuyến phòng vệ thứ hai khi skill này không tự kích hoạt.
  - Khi soạn công văn trả lời/triển khai: dùng kết quả trích xuất để điền chính xác "Thực hiện Văn bản số ... ngày ... của ...".
- Script `scripts/extract_metadata.py` ở đây và trong plugin là **một bản duy nhất** — khi sửa phải cập nhật ĐỒNG THỜI cả hai nơi (ghi vào CHANGELOG plugin).

## CHANGELOG skill này

- **v2.0 (06/7/2026)**: thu gọn thành sentinel (~1/3 độ dài cũ) sau khi nội dung đầy đủ đã hợp nhất vào plugin vbhc-vn v2.0.x; bổ sung vụ sai thứ 3 (2861/SYT-NVY); bỏ tham chiếu chết tới skill anti-error-sct-vn (đã hợp nhất vào vbhc-vn); thêm lệnh fallback sang script trong plugin; script giữ nguyên (đã kiểm chứng 5 file thật, giống từng byte với bản trong plugin).
- **v1.0 (18/5/2026)**: bản đầu, test 5 file thực tế.
