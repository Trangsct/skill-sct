# Hai chế độ làm việc, quy trình Chế độ A và API TemplateDoc

Tách khỏi `SKILL.md` ngày 16/9/2026 (bản 2.23.0). Nội dung giữ nguyên.

Đọc file này khi: bắt đầu một văn bản mới và cần chọn chế độ, hoặc cần cú pháp cụ thể của
`TemplateDoc` / quy trình unpack-sửa-pack.

Từ bản 2.23.0 có thêm đường thứ ba, thường nhanh hơn cả hai: viết nội dung dạng thẻ rồi để
`scripts/build_vb.py` dựng trên mẫu thật (xem README plugin).

## Quy tắc tốc độ (v2.1.0) — hoàn thành 1 văn bản trong ÍT LƯỢT TOOL NHẤT

Mục tiêu: văn bản thường (công văn, tờ trình ≤ 3 trang) xong trong **3-4 lượt tool**: (1) viết script build, (2) một lệnh bash `build && qa_all`, (3) view 1 ảnh ghép, (4) copy outputs + present_files. Cụ thể:
1. **Không chạy inspect template** khi `reference/templates-chi-tiet.md` đã có chỉ số (Bước 2).
2. **Nối build + QA trong MỘT lệnh bash**: `python3 build.py && python3 scripts/qa_all.py output/<file>.docx --forbid "<chuỗi vụ cũ>" ... --require "<chuỗi vụ mới>" ...`. Không tách validate/render/qa thành các lượt riêng. Với Chế độ B trên mẫu thật, `--forbid`/`--require` là BẮT BUỘC (Quy tắc bất biến 17).
3. **Render PDF đúng 1 lần mỗi vòng** — `qa_all.py` tự lo; không tự gọi soffice/pdftoppm rời nữa.
4. **View đúng 1 ảnh ghép** `qa_sheet.png`; chỉ mở ảnh trang lẻ khi có nghi vấn cụ thể.
5. **Sửa lỗi theo báo cáo text, gom hết rồi mới render lại** — không lặp render/view sau từng lỗi nhỏ.
6. **Đọc reference đúng file cần** (bảng ở mục "Tài liệu tham chiếu"), không đọc dàn trải; nội dung SKILL.md này đã đủ cho văn bản thường.
7. Chỉ vòng lặp thêm khi qa_all FAIL hoặc người dùng yêu cầu sửa — chất lượng vẫn là chốt chặn: **không giao file chưa PASS**.

## Hai chế độ làm việc

> **QUY TẮC ƯU TIÊN (theo yêu cầu của Bạn): luôn ưu tiên sửa trên MẪU THẬT thay vì soạn từ template trắng.**
> Khi cần soạn một văn bản, TRƯỚC TIÊN kiểm tra `examples/` xem có mẫu thật phù hợp với loại văn bản đó không:
> - **Có mẫu phù hợp** → dùng **Chế độ B**: copy mẫu thật ra chỗ làm việc, thay nội dung, giữ 100% định dạng đã được kiểm chứng. Đây là cách Bạn muốn ưu tiên.
> - **Không có mẫu phù hợp** → mới dùng **Chế độ A** (template trắng trong `templates/`).
> - Nếu Bạn tải lên một file .docx cụ thể để sửa → luôn dùng Chế độ B trên chính file đó.
> Bảng "Mẫu thật ↔ loại văn bản" ở mục "Thư viện mẫu thật đã ban hành (`examples/`)" giúp tra nhanh mẫu nào dùng cho việc gì.

### Chế độ A — Tạo mới từ template (`templates/` + `TemplateDoc`)
Theo "Quy trình bắt buộc (5 bước)" bên dưới. Dùng khi soạn một văn bản mới **chưa có mẫu thật phù hợp trong `examples/`** và Bạn không tải lên file gốc.

### Chế độ B — Sửa file người dùng tải lên hoặc mẫu thật trong `examples/` (unpack → sửa XML → pack)
Dùng khi rà soát/chỉnh sửa file .docx có sẵn, **hoặc khi soạn mới mà có mẫu thật phù hợp trong `examples/`** (ưu tiên). **Tuyệt đối không dựng lại từ template** (sẽ mất định dạng gốc). Workflow đã kiểm chứng nhiều lần:

```bash
# 1. Đọc nội dung để nắm cấu trúc (text + bảng)
cd /mnt/user-data/uploads && ls -la
extract-text "TÊN_FILE.docx"          # với .doc: convert trước bằng soffice.py --convert-to docx

# 2. Giải nén để sửa trực tiếp XML
cp "/mnt/user-data/uploads/TÊN_FILE.docx" /home/claude/work/src.docx
python /mnt/skills/public/docx/scripts/office/unpack.py /home/claude/work/src.docx /home/claude/work/unpacked/

# 3. Sửa /home/claude/work/unpacked/word/document.xml bằng str_replace (kèm context <w:rPr> để trúng đúng run)
#    grep -n "chuỗi cần tìm" để định vị; sửa số liệu / câu chữ / đánh số mục…

# 4. Đóng gói lại — BẮT BUỘC dùng --original để giữ relationships, media, content-types
python /mnt/skills/public/docx/scripts/office/pack.py /home/claude/work/unpacked/ /home/claude/work/out.docx --original /home/claude/work/src.docx
```

**Bài học XML Chế độ B (11 điểm — vụ thật đã trả giá): đọc `reference/cong-cu-ky-thuat.md` mục "Bài học XML Chế độ B" TRƯỚC khi sửa XML** (sed thay nhầm khối ký, run tách bởi lastRenderedPageBreak, đổi đậm→nghiêng cả run, chèn ô trống + paraId, không truy cập paragraphs[n] sau khi chèn/xóa, clone body từ đoạn justify, merge_runs trước str_replace, assertion sau build).

**Thay nội dung trong run giữ định dạng (python-docx)**: gán `runs[0].text = chuỗi_mới` rồi xóa các run sau (`r.text = ''`) — giữ được đậm/nghiêng/font của run đầu.

## Quy trình bắt buộc cho Chế độ A (5 bước)

### Bước 1: Chọn template

| Loại văn bản | File template |
|---|---|
| Công văn | `templates/01-cong-van.docx` |
| Tờ trình | `templates/02-to-trinh.docx` |
| Báo cáo | `templates/03-bao-cao.docx` |
| Kế hoạch | `templates/04-ke-hoach.docx` |
| Quyết định cá biệt | `templates/05-quyet-dinh.docx` |
| Giấy phép | `templates/06-giay-phep.docx` |
| Giấy chứng nhận ATTP | `templates/07-giay-chung-nhan-attp.docx` |
| Công văn nội bộ Phòng (tham gia ý kiến) | `templates/08-cong-van-noi-bo-phong.docx` |
| Biên bản (làm việc, kiểm tra) | `templates/09-bien-ban.docx` |

### Bước 2: Lấy cấu trúc paragraph của template — KHÔNG chạy inspect nếu đã có sẵn

Chỉ số paragraph/table của cả 9 template đã ghi sẵn trong **`reference/templates-chi-tiet.md`** — đọc file đó và dùng luôn chỉ số, **bỏ qua lượt chạy inspect** (tiết kiệm 1 lượt tool). Chỉ chạy inspect khi nghi template đã bị sửa hoặc reference chưa khớp:

```bash
python3 scripts/fill_template.py templates/01-cong-van.docx   # chỉ khi cần đối chiếu
```

Lệnh trên in ra:
- Danh sách paragraph (P0, P1, P2,...) với text rút gọn
- Danh sách table (Table 0 = header, Table 1 = footer chữ ký)

### Bước 3: Viết script Python để sửa nội dung

Dùng `TemplateDoc` từ `scripts/fill_template.py`:

```python
from fill_template import TemplateDoc
doc = TemplateDoc('templates/01-cong-van.docx')

# Sửa header (Table 0)
doc.replace_in_cell(0, 0, 0, 'Số:       /SCT-CN', 'Số: 458/SCT-CN')
doc.replace_in_cell(0, 0, 0, 'V/v ……………….', 'V/v báo cáo tiến độ ...')
doc.replace_in_cell(0, 0, 1, 'ngày      tháng      năm 2026',
                    'ngày 15 tháng 5 năm 2026')

# Sửa Kính gửi (P2 trong công văn)
doc.replace_in_paragraph(2, '…………..', 'Ủy ban nhân dân tỉnh Lào Cai')

# Thay nội dung body (P4 đến P15)
doc.replace_body_paragraphs(start_idx=4, end_idx=16, new_paragraphs=[
    {'text': 'Đoạn mở đầu...'},
    {'text': '1. Mục thứ nhất', 'bold': True},
    {'text': '- Nội dung...'},
    # ...
])

# Sửa Lưu VT
doc.replace_in_cell(1, 0, 0, 'Lưu: VT, CN.', 'Lưu: VT, CN(Tên).')

# Lưu
doc.save('output/cong-van-moi.docx')
```

### Bước 4: Chạy script build + QA MỘT PHÁT (`qa_all.py`) — trong CÙNG MỘT lệnh bash

Trước khi xuất, **rà soát căn chỉnh đều đẹp và đồng bộ danh mục đánh số thứ tự các mục** (xem Quy tắc 8): hệ thống đề mục nhất quán, đánh số liên tục không nhảy bậc, đúng cấp (I, II, III → 1, 2, 3 → a, b, c hoặc 1.1, 1.2).

**Gộp build và QA vào MỘT lệnh bash duy nhất** (tiết kiệm 3-4 lượt tool so với chạy rời):

```bash
python3 scripts/<ten-script>.py && python3 scripts/qa_all.py output/<file>.docx
```

`qa_all.py` là **đường QA chính từ v2.1.0** — một lệnh, render PDF **đúng 1 lần** (profile soffice ấm, ~1-3s), làm trọn:
1. **Kiểm XML**: đủ Line header, 13pt dòng Số/Ngày (Quy tắc 11-12), `<w:br/>` trong header = 0 (Quy tắc 10), body căn giữa/thiếu firstLine 1cm (WARN — bài học Chế độ B).
2. **check_document.py**: VBQPPL hết hiệu lực (Nhóm D), từ suy đoán (Nhóm C), số văn bản đáng ngờ (Nhóm A).
3. **Kiểm trên PDF render**: widow word (Quy tắc 13), khối chữ ký gãy trang (Quy tắc 14).
4. **Xuất ẢNH GHÉP** `/home/claude/work/qa/qa_sheet.png` — mọi trang trong 1 ảnh.

**QA trực quan**: `view` **MỘT ảnh ghép `qa_sheet.png` là đủ** để soi tổng thể (header/số ký hiệu trang đầu, khối chữ ký trang cuối, ngắt trang, tràn lề). Chỉ mở ảnh trang riêng `qa-N.jpg` khi ảnh ghép phát hiện nghi vấn ở trang N, hoặc văn bản > 6 trang cần soi kỹ biểu/tiêu đề bảng lặp. Đây là file QA tạm — KHÔNG xuất PDF cho người dùng.

**Vòng sửa lỗi**: khi FAIL, sửa theo **báo cáo TEXT** trước (đủ căn cứ định vị lỗi), chạy lại `qa_all.py` MỘT lần sau khi đã sửa hết — KHÔNG render/soi ảnh sau từng lỗi nhỏ. Khi tool view ảnh không truyền được nội dung, báo cáo text của `qa_all.py` là đủ căn cứ kết luận. KHÔNG giao file chưa qua `qa_all.py` PASS (hoặc PASS kèm WARN đã được cân nhắc).

`qa_pdf_check.py` vẫn dùng được độc lập khi chỉ cần kiểm 4 mục thể thức; đã có PDF render sẵn thì thêm `--pdf <path>` để khỏi render lại. `validate.py` của skill docx public chỉ cần chạy khi qa_all báo nghi hỏng cấu trúc file.

### Bước 5: Đặt tên file chuẩn & trả file qua present_files

Đặt file vào `/mnt/user-data/outputs/` với **tên file chuẩn** `YYYY.MM.DD. [Tên văn bản].docx` (xem Quy tắc 7) rồi gọi `present_files`. KHÔNG tạo PDF kèm.

## API thư viện `TemplateDoc`

| Method | Mô tả |
|---|---|
| `replace_in_paragraph(idx, pattern, replacement)` | Thay text khớp pattern trong paragraph thứ idx |
| `set_paragraph_text(idx, new_text)` | Đặt toàn bộ text paragraph idx (giữ format run đầu) |
| `replace_in_cell(table_idx, row, col, pattern, replacement)` | Thay text trong ô bảng |
| `replace_in_cell_paragraph(t, r, c, p_idx, pattern, replacement)` | Thay trong 1 paragraph cụ thể của ô bảng |
| `set_cell_paragraph_text(t, r, c, p_idx, new_text)` | Đặt text 1 paragraph trong ô bảng |
| `replace_keeping_first_run(p_idx, new_after, separator=': ')` | Cho paragraph "Điều X:..." — giữ "Điều X" bold, thay phần sau |
| `replace_body_paragraphs(start, end, new_paragraphs)` | Thay nguyên 1 đoạn nhiều paragraph (giữ format paragraph mẫu) |
| `replace_all(pattern, replacement)` | Find & replace trong toàn doc |
| `inspect()` | In cấu trúc paragraph & table để debug |
| `save(path)` | Lưu file |
