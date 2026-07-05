# Công cụ kỹ thuật đã kiểm chứng thực chiến (đọc TRƯỚC khi mò lệnh)

Tổng hợp các cách làm ĐÃ CHẠY ĐƯỢC trong môi trường Claude với hồ sơ SCT Lào Cai (rút từ các phiên 6-7/2026). Gặp đúng tình huống → dùng ngay công thức, không thử lại từ đầu.

## 1. Giải nén lưu trữ (RAR/ZIP tên file tiếng Việt)

| Tình huống | Cách đã chạy được |
|---|---|
| RAR thường | Copy file về thư mục làm việc (KHÔNG thao tác trực tiếp trên `/mnt/user-data/uploads` khi tên có dấu), rồi: `export LANG=C.UTF-8 LC_ALL=C.UTF-8 && unrar x -y file.rar`. Xem trước nội dung: `unrar lb file.rar` |
| `unrar`/`7z` không có sẵn | Python: `pip install rarfile --break-system-packages` → `import rarfile; rarfile.RarFile(path).extractall('.')` — xử lý tốt tên tiếng Việt |
| RAR5 (unrar và rarfile đều bó tay) | `apt-get install -y libarchive-tools` (không cần sudo) → `bsdtar -xf file.rar` |
| ZIP mà bsdtar lỗi encoding tên tiếng Việt | Python `zipfile` chuẩn |
| Tên file giải nén bị vỡ dấu | Đổi tên hàng loạt sang ASCII tuần tự (01.pdf, 02.pdf...) rồi xử lý; debug tên file bằng `os.walk` + `repr()` |

## 2. Đọc PDF scan tiếng Việt (OCR)

Chuỗi chẩn đoán: `pdftotext -layout` ra trống/toàn form-feed → PDF ảnh (scan), làm theo bảng:

| Tình huống | Cách đã chạy được |
|---|---|
| Cài OCR tiếng Việt | `apt-get install -y tesseract-ocr-vie`. Nếu offline: tải `vie.traineddata` từ github.com/tesseract-ocr/tessdata_fast, đặt `TESSDATA_PREFIX` = thư mục chứa file đó (KHÔNG phải tessdata hệ thống) |
| OCR từng trang | `pdftoppm -jpeg -r 120 file.pdf pg` → `tesseract pg-1.jpg out -l vie --psm 6` |
| OCR cả file, giữ layout | `ocrmypdf --language vie+eng --force-ocr in.pdf out.pdf` → `pdftotext out.pdf` |
| PDF có chữ ký số chặn ocrmypdf | Bỏ OCR, render ảnh đọc trực tiếp bằng mắt (vision): `pdftoppm -jpeg -r 130-150` rồi `view` từng ảnh — số văn bản/ngày/người ký đọc được tin cậy ở 130-150 DPI |
| File scan nhiều trang (50-90+) | OCR song song batch 8 trang (background jobs + `wait`) |
| Đọc metadata VBHC (số/ngày/người ký) | LUÔN chạy `scripts/extract_metadata.py` trước (GATE PDF — xem Nhóm E); OCR chỉ là fallback khi script trả null |

## 3. Sửa .docx giữ nguyên định dạng (Chế độ B)

- **Unpack/pack**: dùng `/mnt/skills/public/docx/scripts/office/unpack.py` và `pack.py --original goc.docx` (KHÔNG phải đường dẫn trong vbhc-vn/scripts).
- **Thay text an toàn nhất**: `str_replace` trên nội dung `<w:t>` trong `word/document.xml`, kèm đủ ngữ cảnh XML xung quanh để chuỗi là duy nhất; định vị bằng `grep -n`. KHÔNG dựng lại cả paragraph (vỡ `<w:rPr>`).
- **Chuỗi bị Word tách nhiều run** (tên công ty, quốc hiệu...): gộp toàn bộ run trong paragraph → thay trên chuỗi gộp → dồn kết quả về run đầu. Khi giữ định dạng: chọn run đầu tiên CÓ `w:rPr` làm run giữ lại (run[0] có thể không có font).
- **Ô bảng nhiều run gây chữ lặp**: gộp hết run trong cell rồi ghi đè, không chỉ sửa run đầu.
- **Nhân bản dòng bảng**: `deepcopy(row._tr)` → `row._tr.addnext(new)`.
- **Chèn đoạn đúng vị trí**: `anchor._p.addprevious()/addnext()`; xóa đoạn: lấy slice danh sách paragraphs TRƯỚC rồi mới `p._p.getparent().remove(p._p)` (xóa trong lúc lặp gây trôi index); trước mỗi lần xóa `assert` text mục tiêu tồn tại đúng 1 lần.
- **Duyệt đúng thứ tự đoạn + bảng xen kẽ**: `doc.element.body.iterchildren()` kiểm tag `'}p'` / `'}tbl'` (d.paragraphs bỏ qua bảng).
- **Khối ký bị cắt sang 2 trang**: thêm `OxmlElement('w:cantSplit')` vào `trPr` dòng bảng ký.
- **Word đòi "repair" khi mở**: kiểm `numbering.xml` — trong `w:lvl`, `w:numFmt` phải đứng TRƯỚC `w:pStyle`; sửa thứ tự rồi repack.

## 4. QA trước khi giao file (bắt buộc)

1. `soffice --headless --convert-to pdf file.docx`
2. `pdftoppm -jpeg -r 130 file.pdf qa` → `view` TỪNG trang ảnh.
3. `pdftotext -layout` đối chiếu nội dung/căn cột.
4. Render ảnh đôi khi không ổn định ở vòng lặp sau của cùng phiên → fallback kiểm tra bằng code: grep text trích xuất, kiểm alignment/bold/indent/số `<w:br/>`.
5. Soát chéo thể thức theo checklist Nhóm G (`phong-tranh-sai-lam.md`): Kính gửi ↔ Nơi nhận, tiêu ngữ en dash, "./.", dòng Lưu, dòng ngày.
6. Với .xlsx: recalc bằng LibreOffice headless, xác nhận 0 lỗi công thức trước khi giao.

## 5. Sửa header an toàn shape + đồng bộ thể thức (bổ sung 05/7/2026, từ vụ 4 lỗi công văn HHNH)

```python
from docx.oxml.ns import qn
import copy

# (a) Kiểm tra run có shape (Line) không — BẮT BUỘC trước khi gán run.text
def run_has_shape(run):
    return bool(list(run._r.iter(qn('w:drawing'))) + list(run._r.iter(qn('w:pict'))))

# (b) Sửa text trong paragraph CÓ shape: chỉ qua w:t, xác định node theo ngữ cảnh
# ví dụ đổi số tháng '6' -> '7' khi text tách run (' tháng' | '6'):
ts = list(p._p.iter(qn('w:t')))
for i, t in enumerate(ts):
    if t.text and t.text.strip() == 'tháng':
        for t2 in ts[i+1:]:
            if t2.text and t2.text.strip() == '6':
                t2.text = t2.text.replace('6', '7'); break
        break

# (c) Khôi phục paragraph hỏng: deep copy nguyên <w:p> từ file gốc
new_p = copy.deepcopy(src_para._p)
old_para._p.addprevious(new_p); old_para._p.getparent().remove(old_para._p)

# (d) 13pt tường minh cho dòng Số/Ngày
for r in p.runs:
    rpr = r._element.get_or_add_rPr()
    for tag in ('w:sz','w:szCs'):
        e = rpr.find(qn(tag))
        if e is None: e = rpr.makeelement(qn(tag), {}); rpr.append(e)
        e.set(qn('w:val'), '26')

# (e) Co chữ chống widow word (condensed -0.2pt/ký tự)
sp = rpr.find(qn('w:spacing'))
if sp is None: sp = rpr.makeelement(qn('w:spacing'), {}); rpr.append(sp)
sp.set(qn('w:val'), '-4')

# (f) Khối ký không tách trang
tr = table.rows[0]._tr
trPr = tr.find(qn('w:trPr')) or tr.makeelement(qn('w:trPr'), {})
if trPr.getparent() is None: tr.insert(0, trPr)
if trPr.find(qn('w:cantSplit')) is None:
    trPr.append(trPr.makeelement(qn('w:cantSplit'), {}))
# rồi co giãn: space before/after body 6pt -> 4pt nếu khối ký bị đẩy nguyên sang trang mới
```

QA khép vòng: `python3 scripts/qa_pdf_check.py <file.docx>` — kiểm widow word, khối ký cùng trang, đủ 2 Line header, cỡ 13pt dòng Số/Ngày. Khi tool view ảnh không hoạt động, script này + `pdftotext -layout` là đường QA chính.
