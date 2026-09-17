# Reference 04 — Kịch bản mẫu (từng bước, câu trả lời mẫu)

## 1. "Soạn báo cáo kết quả họp chấm điểm CCN Xuân Ái"

1. Tra kho: `python3 scripts/tim_trong_kho.py "Xuân Ái" --tu 01/09/2026` → thấy GM 5615/GM-HĐ, QĐ 3226/QĐ-UBND
   (mục lục), 5928/SXD-PTĐT, 8782/SNNMT-QLĐĐ, 561/PG-VBNB2026 (có `.md`).
2. Thiếu bản gốc QĐ 3226 và Biên bản họp (nếu đã phát hành) → sai bot:
   `tim = "3226/QĐ-UBND; biên bản họp Hội đồng Xuân Ái; kết quả lựa chọn chủ đầu tư Xuân Ái"`, `ngay = 30`,
   `ten = xuan-ai-cham-diem`.
3. Chờ ~5 phút, đọc `theo-doi/yeu-cau/xuan-ai-cham-diem/README.md`. Không thấy biên bản → ghi rõ trong báo cáo
   gửi người dùng: "Data360X chưa có Biên bản/Thông báo kết quả tính đến <ngày giờ quét>".
4. Soạn theo `vbhc-vn`, dẫn số/ngày lấy ở đầu các tệp `.md`.

Câu trả lời mẫu: *"Tôi đã lấy từ Data360X 4 văn bản (5928, 8782, 561 ngày 10/9; GM 5615). QĐ 3226/QĐ-UBND ngày
09/9 chỉ có mục lục, bản gốc chưa tải được — nếu Bạn có bản giấy thì chụp gửi tôi. Dự thảo báo cáo dưới đây…"*

## 2. "Tuần này có văn bản gì về hóa chất không?"

1. `python3 scripts/tim_trong_kho.py --linh-vuc hc-sct-vn --tu <hôm nay − 7>`.
2. Bản tin mới nhất cũ hơn 4 ngày → gọi `quet-tren-may.yml` (`ngay = 10`), chờ, chạy lại bước 1.
3. Trả lời theo dạng bảng `số | ngày | đi/đến | trích yếu | có bản gốc?`; nói rõ mốc quét.

## 3. Bot trả về `.pdf` (bản scan)

```python
import pymupdf
d = pymupdf.open("theo-doi/yeu-cau/<ten>/<số>.pdf")
for i, p in enumerate(d): p.get_pixmap(dpi=150).save(f"trang-{i+1}.png")
```
Đọc từng ảnh bằng công cụ xem ảnh; số/ngày chép từ ảnh (ghi rõ "đọc từ ảnh trang 1"). Không dùng kết quả
OCR của mô hình khác để ghi số/ngày mà không soi lại ảnh.

## 4. Cập nhật plugin đầu phiên (theo CLAUDE.md của skill-sct)

1. Đọc `theo-doi/bao-cao/<ngày mới nhất>.md`. Cũ hơn 4 ngày → gọi quét (động tác 3).
2. Với từng mục lĩnh vực: mở tệp `.md`, đối chiếu plugin; có quy định/số liệu mới → sửa reference, nâng
   version, CHANGELOG, `sync_marketplace.py --bump`, `check_descriptions.py`, PR + merge.
3. Chạy `python3 scripts/nap_vbpl_data360x.py ../vlncn-laocai/theo-doi/de-xuat-vbpl.csv` để nạp VBPL công khai.
4. Không có gì mới → một dòng: "Đã rà bản tin <ngày>, không có văn bản làm đổi plugin nào."

## 5. Soát dự thảo có viện dẫn

1. Thả `.docx` vào `du-thao/` (kho vlncn-laocai) → workflow *Soat du thao* sinh `trich-dan.json`.
2. Gọi `tim-van-ban.yml` với `ho_so` = tên thư mục → `du-thao/<ho_so>/kem-theo/`.
3. Văn bản viện dẫn không thấy (cũ hơn khoảng quét) → động tác 2 với `ngay = 180`, hoặc xin người dùng.
