---
name: vbhc-pdf-reader-vn
description: "Đọc và trích xuất chính xác metadata (số văn bản, ngày ban hành, cơ quan, người ký, trích yếu, nơi nhận) từ PDF văn bản hành chính, QPPL Việt Nam. PHẢI CHẠY NGAY mỗi khi nhận PDF có vẻ là văn bản nhà nước VN — không chờ phát hiện thiếu thông tin trong context. Vấn đề giải quyết: PDF VBHC có layout 2 cột (cơ quan | Quốc hiệu) với text-box độc lập cho số/ngày, khi nạp vào context Claude các vùng này thường bị bỏ trống hoặc nối sai thứ tự. Triggers: tên file chứa 'CV', 'QĐ', 'TTr', 'BC', 'KH', 'NQ', 'NĐ', 'TT', 'BYT', 'BNN', 'BCT', 'UBND', 'HĐND', 'SCT'; cụm 'PDF', 'file PDF', 'công văn đến', 'văn bản đến', 'file đính kèm', 'đọc giúp', 'tham gia ý kiến', 'soạn công văn triển khai', 'triển khai văn bản', 'báo cáo theo chỉ đạo'; context có 'Số: /UBND-...', 'ngày tháng ... năm 20...' bị trống. Từ khoá: công văn, quyết định, tờ trình, kế hoạch, báo cáo, nghị quyết, nghị định, thông tư, UBND, HĐND, Bộ Y tế, Bộ Công Thương, Sở, KT., TM., TUQ., TL., người ký, trích yếu, nơi nhận."
---

# vbhc-pdf-reader-vn — Đọc PDF văn bản hành chính Việt Nam

> ## ⚠️ CẢNH BÁO CỨNG — ĐỌC TRƯỚC KHI LÀM BẤT KỲ VIỆC GÌ KHÁC
>
> Trong lượt hiện tại, nếu Claude nhận được file PDF kèm theo lời nhắn của người dùng, và file đó có dấu hiệu là văn bản nhà nước Việt Nam (tên file, dòng đầu trong context, hoặc bối cảnh hội thoại gợi ý), thì **DỪNG mọi thao tác khác lại** và chạy ngay:
>
> ```bash
> python3 "/mnt/skills/plugins/vbhc-vn:vbhc-vn/scripts/extract_metadata.py"   # bản giống hệt; nếu có skill lẻ vbhc-pdf-reader-vn thì dùng /mnt/skills/user/vbhc-pdf-reader-vn/scripts/ "<đường dẫn file>"
> ```
>
> Đây là **quy tắc cứng, không có ngoại lệ**. KHÔNG được:
> - Tin số văn bản/ngày tháng đọc từ context window khi nguồn là PDF.
> - Bỏ qua bước này vì "context đã có vẻ đủ thông tin".
> - Soạn văn bản trả lời/triển khai trước khi xác minh số/ngày bằng skill.
>
> Việc bỏ qua quy tắc này **đã làm xảy ra ít nhất 2 vụ dẫn chiếu sai** trong công việc thực tế của Bạn:
>
> | Vụ | Số văn bản đúng | Hậu quả nếu tin context |
> |---|---|---|
> | CV UBND tỉnh về ĐVHD (14/5/2026) | 3861/UBND-NC ngày 15/5/2026 | Văn bản triển khai để trống số/ngày, Bạn phải sửa lại |
> | CV UBND tỉnh về Đề án ATTP (18/5/2026) | 3954/UBND-VX ngày 17/5/2026 | Công văn tham gia ý kiến để trống số/ngày, Bạn phải nhắc Claude chạy lại skill |
>
> Chi phí chạy skill: ~2 giây. Chi phí bỏ qua: Bạn phải đọc lại file gốc, gõ tay sửa từng chỗ, hoặc tệ hơn là văn bản trình ký sai số/ngày dẫn chiếu.

## QUY TẮC SỐ 1 — BẮT BUỘC

**Khi người dùng upload bất kỳ PDF nào trông giống văn bản hành chính/QPPL Việt Nam, Claude PHẢI chạy script trích xuất NGAY ở lượt phản hồi đầu tiên, không cần chờ phát hiện context window thiếu thông tin.**

```bash
python3 "/mnt/skills/plugins/vbhc-vn:vbhc-vn/scripts/extract_metadata.py"   # bản giống hệt; nếu có skill lẻ vbhc-pdf-reader-vn thì dùng /mnt/skills/user/vbhc-pdf-reader-vn/scripts/ "<đường dẫn file>"
```

**Cờ kích hoạt** (bất kỳ cờ nào):

1. **Tên file** có chứa: "cong_van", "công_văn", "QĐ", "QD", "quyet_dinh", "TTr", "to_trinh", "BC", "bao_cao", "KH", "ke_hoach", "NQ", "nghi_quyet", "NĐ", "ND", "TT", "thong_tu", "UBND", "BCT", "BYT", "BNN", "SCT", "STC", "SNN", "SXD", "HĐND".
2. **Dòng đầu file** (sau khi mở context) có: "ỦY BAN NHÂN DÂN", "BỘ ...", "SỞ ...", "HỘI ĐỒNG NHÂN DÂN", "CHÍNH PHỦ", "THỦ TƯỚNG", "QUỐC HỘI".
3. **Context window** hiện ra: `Số:    /UBND-...`, `Số:    /BYT-...`, `Số:    /BCT-...`, `Số:    /QĐ-...`, `ngày      tháng      năm`, hoặc bất kỳ trường số/ngày nào trống.
4. **Người dùng nhắc**: "PDF", "công văn đến", "văn bản đến", "file đính kèm", "tệp đính kèm", "đọc giúp", "tham gia ý kiến", "soạn công văn triển khai", "soạn thư trả lời", "báo cáo theo chỉ đạo", "triển khai văn bản".
5. **Hội thoại có mục đích** soạn văn bản tham mưu, triển khai, trả lời, báo cáo dựa trên một văn bản nguồn (cấp trên ban hành).

## Tại sao skill này tồn tại

Văn bản hành chính nhà nước Việt Nam (theo Nghị định 30/2020/NĐ-CP, Nghị định 78/2025/NĐ-CP, Nghị định 187/2025/NĐ-CP) có **layout 2 cột** ở phần đầu:

```
ỦY BAN NHÂN DÂN              CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
TỈNH LÀO CAI                 Độc lập - Tự do - Hạnh phúc

Số: 3954/UBND-VX             Lào Cai, ngày 17 tháng 5 năm 2026
V/v ...
```

Và **2 cột ở phần cuối**:

```
Nơi nhận:                    TL. CHỦ TỊCH
- Như trên;                  KT. CHÁNH VĂN PHÒNG
- ...                        PHÓ CHÁNH VĂN PHÒNG
- Lưu: VT.
                             Nguyễn Thanh Tú
```

Khi PDF được nạp tự động vào context window (qua API document upload), các text-box độc lập (số văn bản, ngày tháng, chức vụ – tên người ký) thường bị **bỏ trống** hoặc **nối sai thứ tự**. Đây là vấn đề kỹ thuật của đường ống xử lý PDF — không phải lỗi của file scan.

→ **Bắt buộc** đọc lại bằng skill này từ file gốc trên disk khi cần dẫn chiếu chính xác.

## Quy trình 3 bước

### Bước 1 — Chạy script trích xuất

```bash
python3 "/mnt/skills/plugins/vbhc-vn:vbhc-vn/scripts/extract_metadata.py"   # bản giống hệt; nếu có skill lẻ vbhc-pdf-reader-vn thì dùng /mnt/skills/user/vbhc-pdf-reader-vn/scripts/ /mnt/user-data/uploads/<file>.pdf
```

Output là JSON gồm 11 trường:

| Trường | Mô tả | Ví dụ |
|---|---|---|
| `co_quan_ban_hanh` | Cơ quan ban hành | `"ỦY BAN NHÂN DÂN - TỈNH LÀO CAI"` hoặc `"UBND TỈNH LÀO CAI - SỞ CÔNG THƯƠNG"` |
| `so_van_ban` | Số ký hiệu | `"3954/UBND-VX"`, `"05/2025/QĐ-UBND"`, `"59/QĐ-SCT"` |
| `dia_danh_ngay` | Địa danh + ngày dạng văn bản | `"Lào Cai, ngày 17 tháng 5 năm 2026"` |
| `ngay_iso` | Ngày dạng ISO | `"2026-05-17"` |
| `loai_van_ban` | Loại VB | `"CÔNG VĂN"`, `"QUYẾT ĐỊNH"`, `"TỜ TRÌNH"`, `"BÁO CÁO"`, `"KẾ HOẠCH"`, `"NGHỊ QUYẾT"` |
| `trich_yeu` | Trích yếu | `"tham gia ý kiến đối với..."` (công văn) hoặc `"Ban hành Quy định..."` (QĐ) |
| `kinh_gui` | Danh sách kính gửi (công văn) | `["Các sở: Y tế, Nội vụ, Công Thương", ...]` |
| `nguoi_ky` | Họ tên người ký | `"Nguyễn Thanh Tú"`, `"Đỗ Xuân Tuyên"`, `"Hoàng Chí Hiền"` |
| `chuc_vu_ky` | Chức vụ kèm KT./TM./TUQ./TL. | `"KT. CHỦ TỊCH - PHÓ CHỦ TỊCH"`, `"TM. ỦY BAN NHÂN DÂN - CHỦ TỊCH"`, `"GIÁM ĐỐC"`, `"TL. CHỦ TỊCH - KT. CHÁNH VĂN PHÒNG - PHÓ CHÁNH VĂN PHÒNG"` |
| `noi_nhan` | Danh sách nơi nhận | `["Như trên", "Lưu: VT", ...]` |
| `phuong_phap` | Cách trích | `"text-extraction"` hoặc `"ocr"` |

### Bước 2 (nếu output rỗng) — OCR cho PDF scan

Khi script trả về phần lớn trường là `null` và `phuong_phap == "text-extraction"`, nghĩa là pdftotext không đọc được — file có thể là scan thuần ảnh:

```bash
ocrmypdf --language vie+eng --force-ocr <input>.pdf /tmp/ocr_output.pdf
python3 "/mnt/skills/plugins/vbhc-vn:vbhc-vn/scripts/extract_metadata.py"   # bản giống hệt; nếu có skill lẻ vbhc-pdf-reader-vn thì dùng /mnt/skills/user/vbhc-pdf-reader-vn/scripts/ /tmp/ocr_output.pdf
```

Script đã tích hợp fallback OCR tự động khi `pdftotext` trả về <100 ký tự.

### Bước 3 — Cờ `--raw` khi debug

```bash
python3 .../extract_metadata.py file.pdf --raw
```

In kèm toàn bộ text gốc (sau `pdftotext -layout`) để kiểm tra layout từng dòng.

## Test cases đã verify

Skill được test với 5 file thực tế của Bạn (17-18/5/2026):

| File | Số VB | Ngày | Người ký | Chức vụ |
|---|---|---|---|---|
| CV UBND tỉnh về ĐVHD | `3861/UBND-NC` | 15/5/2026 | Giàng Quốc Hưng | KT. CHỦ TỊCH - PHÓ CHỦ TỊCH |
| CV UBND tỉnh về Đề án ATTP | `3954/UBND-VX` | 17/5/2026 | Nguyễn Thanh Tú | TL. CHỦ TỊCH - KT. CHÁNH VĂN PHÒNG - PHÓ CHÁNH VĂN PHÒNG |
| CV Bộ Y tế xin ý kiến Đề án ATTP | `3542/BYT-ATTP` | 16/5/2026 | Đỗ Xuân Tuyên | KT. BỘ TRƯỞNG - THỨ TRƯỞNG |
| QĐ về CNNV của SCT (UBND ban hành) | `05/2025/QĐ-UBND` | 01/7/2025 | Trần Huy Tuấn | TM. ỦY BAN NHÂN DÂN - CHỦ TỊCH |
| QĐ về CNNV phòng chuyên môn (SCT ban hành) | `59/QĐ-SCT` | 01/7/2025 | Hoàng Chí Hiền | GIÁM ĐỐC |

Tất cả các trường đều trích xuất đúng. Đặc biệt skill xử lý được các edge case:
- Số văn bản có khoảng trắng thừa quanh dấu `/` (`"Số: 59    /QĐ-SCT"`).
- Ngày bị tách 2 dòng do typo/scan (`"ngày 01 tháng 07"` + dòng dưới `"6 năm 2025"`).
- Chức vụ ký có nhiều dòng xen kẽ giữa danh sách Nơi nhận (`"TM. ỦY BAN NHÂN DÂN"` ở dòng đầu, `"CHỦ TỊCH"` ở dòng giữa nhiều dòng Nơi nhận).
- Chức vụ ký dạng "TL. ... KT. ... PHÓ ..." (3 cấp ký thừa lệnh + ký thay).
- Văn bản nhiều trang, không lan sang Quốc hiệu trang phụ lục.

## Các pattern Việt Nam thường gặp

### Số văn bản

| Pattern | Loại văn bản |
|---|---|
| `Số: 3954/UBND-VX` | Công văn UBND |
| `Số: 3542/BYT-ATTP` | Công văn Bộ Y tế, Cục ATTP |
| `Số: 2984/BNNMT-LNKL` | Công văn Bộ NN&MT, Cục LNKL |
| `Số: 37/ĐK-HT` | Điện khẩn |
| `Số: 187/2025/NĐ-CP` | Nghị định (QPPL có năm) |
| `Số: 05/2025/QĐ-UBND` | Quyết định QPPL UBND |
| `Số: 525/QĐ-UBND` | Quyết định cá biệt |
| `Số: 59/QĐ-SCT` | Quyết định của Sở Công Thương |
| `Số: 166/KH-UBND` | Kế hoạch |
| `Số: 01/KHPH-CSMT-GHPGVN-LNKL` | Kế hoạch phối hợp nhiều cơ quan |

### Ngày ban hành

Luôn theo dạng: `<địa danh>, ngày <d> tháng <m> năm <yyyy>`
- "Hà Nội, ngày 30 tháng 3 năm 2026"
- "Lào Cai, ngày 17 tháng 5 năm 2026"
- "TP. Hồ Chí Minh, ngày..." (lưu ý dấu chấm sau TP)

Lưu ý: ngày trong file scan có thể bị tách 2 dòng — skill đã xử lý tự động.

### Chức vụ ký

| Marker | Ý nghĩa |
|---|---|
| `KT. CHỦ TỊCH` / `KT. GIÁM ĐỐC` / `KT. BỘ TRƯỞNG` | Ký thay (Phó ký thay Trưởng) |
| `TM. ỦY BAN NHÂN DÂN` / `TM. HỘI ĐỒNG` | Thay mặt tập thể |
| `TUQ. CHỦ TỊCH` / `TUQ. GIÁM ĐỐC` | Thừa uỷ quyền |
| `TL. CHỦ TỊCH` / `TL. GIÁM ĐỐC` | Thừa lệnh (thường kết hợp với KT.) |
| (Không có tiền tố) | Người đứng đầu ký trực tiếp |

## Sai lầm thường gặp — KHÔNG LÀM

❌ **Không chạy skill khi nhận PDF VBHC** — đây là sai lầm chính. Phải chạy NGAY, không chờ phát hiện thiếu.

❌ **Bỏ qua skill vì context có vẻ đủ thông tin** — context window không đáng tin với layout 2 cột. Đây là sai lầm đã lặp lại 2 lần (CV 3861/UBND-NC và CV 3954/UBND-VX).

❌ Tin số văn bản đọc được từ context window khi thấy phần "Số:" để trống.

❌ Dùng `pdftotext` không có cờ `-layout` — sẽ nối các text-box sai thứ tự.

❌ Dùng `cat` trên PDF — in ra binary, vô nghĩa.

❌ Dùng pypdf `extract_text()` cho văn bản VN có 2 cột — cũng mất layout. (Pypdf ok cho văn bản 1 cột đơn giản, nhưng không an toàn cho văn bản hành chính VN.)

❌ Bỏ qua bước OCR khi `pdftotext` trả về `""` — đây là dấu hiệu PDF scan, cần OCR (script đã tự động fallback).

❌ Soạn văn bản trả lời/triển khai với số văn bản nguồn để trống "yêu cầu Bạn điền sau" khi file gốc đã có sẵn số trên disk.

## Khi nào cần CHẠY LẠI script

- Khi viết phản hồi cần dẫn chiếu chính xác số/ngày văn bản.
- Khi soạn công văn trả lời/triển khai văn bản cấp trên.
- Khi tổng hợp danh mục văn bản đến/đi.
- Khi rà soát, lưu trữ.
- Khi context window dài và đã trôi qua nhiều lượt — không tin vào trí nhớ ngắn hạn của hội thoại.
- Khi người dùng nhắc lại file PDF đã gửi từ lượt trước (vì context có thể đã trôi).

## Ví dụ minh hoạ (vụ thực tế đã xảy ra)

### Vụ 1: CV 3861/UBND-NC về bảo vệ ĐVHD (14/5/2026)

**Input**: PDF công văn UBND tỉnh Lào Cai về bảo vệ động vật hoang dã (file `14_5_2026-VB_CỦA_UBND_TỈNH_ve_dongvathoangda.pdf`).

**Context window của Claude (tự động trích)**: thiếu số (`"Số: /UBND-NC"`) và ngày (`"ngày tháng 5 năm 2026"`).

**Claude lần đầu (SAI)**: tin theo context, viết "Văn bản số …….…/UBND-NC ngày …../5/2026" và yêu cầu Bạn xác minh sau.

**Sau khi chạy skill (ĐÚNG)**:
```json
{
  "co_quan_ban_hanh": "ỦY BAN NHÂN DÂN - TỈNH LÀO CAI",
  "so_van_ban": "3861/UBND-NC",
  "dia_danh_ngay": "Lào Cai, ngày 15 tháng 5 năm 2026",
  "nguoi_ky": "Giàng Quốc Hưng",
  "chuc_vu_ky": "KT. CHỦ TỊCH - PHÓ CHỦ TỊCH"
}
```

### Vụ 2: CV 3954/UBND-VX về Đề án ATTP (18/5/2026)

**Input**: PDF công văn UBND tỉnh Lào Cai về tham gia ý kiến Đề án ATTP của Bộ Y tế (file `Cv_tham_gia_y_kien_du_thao_de_an.pdf`).

**Context window của Claude**: thiếu số (`"Số: /UBND-VX"`) và ngày (`"ngày tháng 5 năm 2026"`).

**Claude lần đầu (SAI)**: dù đã có sẵn skill `vbhc-pdf-reader-vn`, vẫn bỏ qua và soạn công văn với chỗ trống "Văn bản số ....../UBND-VX ngày .../5/2026", yêu cầu Bạn xác minh sau khi nhận CV chính thức.

**Bạn nhắc**: "Cách nào để khắc phục việc bạn không đọc được số văn bản từ file pdf tôi gửi?"

**Sau khi chạy skill (ĐÚNG)**:
```json
{
  "co_quan_ban_hanh": "ỦY BAN NHÂN DÂN - TỈNH LÀO CAI",
  "so_van_ban": "3954/UBND-VX",
  "dia_danh_ngay": "Lào Cai, ngày 17 tháng 5 năm 2026",
  "nguoi_ky": "Nguyễn Thanh Tú",
  "chuc_vu_ky": "TL. CHỦ TỊCH - KT. CHÁNH VĂN PHÒNG - PHÓ CHÁNH VĂN PHÒNG"
}
```

→ Đủ căn cứ dẫn chiếu chính xác ngay từ đầu:
> "Thực hiện Công văn số **3954/UBND-VX** ngày **17/5/2026** của UBND tỉnh Lào Cai..."

**Bài học**: Mỗi lần Bạn gửi PDF VBHC, Claude tốn ~2 giây chạy script để có dữ liệu chính xác — rẻ hơn rất nhiều so với việc Bạn phải đọc lại file gốc để sửa các chỗ Claude điền sai hoặc để trống. **Đây là sai lầm Claude đã lặp lại 2 lần** — quy tắc bắt buộc trên đầu skill này tồn tại để Claude không lặp lại lần thứ 3.

## Liên kết với các skill khác

- **vbhc-vn** (mục "Phòng tránh 5 nhóm sai lầm tham mưu" — đã hợp nhất nội dung anti-error): Nhóm E — Tin context window đối với PDF có header 2 cột. Đây là tuyến phòng vệ thứ hai khi skill này không được tự kích hoạt.
- **vbhc-vn**: khi soạn công văn trả lời/triển khai, dùng kết quả trích xuất của skill này để điền chính xác phần "Thực hiện Văn bản số ... ngày ... của ..." trong đoạn mở đầu.
