# vbhc-vn v2.0.0 (plugin) — Bộ template + quy trình thực chiến, Sở Công Thương Lào Cai

> **v2.0.0 (05/7/2026)**: chuyển chuẩn PLUGIN (.claude-plugin/plugin.json); thêm 4 Quy tắc bất biến 11-14 (an toàn shape Line, 13pt dòng Số/Ngày, chống widow word, khối ký không gãy trang); Nhóm anti-error H; script mới `scripts/qa_pdf_check.py`; sửa false positive check_document; bổ sung 10 VBQPPL hết hiệu lực mới; chuẩn hóa Quốc hiệu/tiêu ngữ + chèn Line template 07. Chi tiết: CHANGELOG.md.

**Cập nhật quan trọng**: phiên bản này KHÔNG sinh văn bản từ đầu bằng code (cách cũ không tái tạo được khung, gạch chân, layout chữ ký). Skill hoạt động theo **2 chế độ**: (A) tạo mới từ 08 mẫu trắng (Sở + nội bộ phòng) bằng `TemplateDoc`; (B) **sửa file .docx người dùng tải lên** bằng workflow unpack→sửa XML→pack, giữ NGUYÊN 100% định dạng gốc. Chế độ B (rà soát/chỉnh sửa file có sẵn) là loại việc thường gặp nhất.

## Cấu trúc thư mục

```
vbhc-vn/
├── SKILL.md                              ← Hướng dẫn cho Claude
├── README.md                             ← File này
├── requirements.txt
├── scripts/
│   ├── fill_template.py                  ← Thư viện helper Python
│   ├── demo_cong_van.py
│   ├── demo_to_trinh.py
│   └── demo_quyet_dinh.py
├── templates/                            ← MẪU TRẮNG (Chế độ A - TemplateDoc)
│   ├── 01-cong-van.docx
│   ├── 02-to-trinh.docx
│   ├── 03-bao-cao.docx
│   ├── 04-ke-hoach.docx
│   ├── 05-quyet-dinh.docx
│   ├── 06-giay-phep.docx
│   ├── 07-giay-chung-nhan-attp.docx
│   └── 08-cong-van-noi-bo-phong.docx     ← công văn nội bộ phòng (Trưởng phòng ký)
└── examples/                             ← MẪU THẬT đã ban hành (Chế độ B - mở, sửa, giữ định dạng)
    ├── sct/                              ← văn bản do Sở Công Thương ban hành
    │   ├── cong-van-de-nghi-bo-sung-ho-so.docx
    │   ├── cong-van-moi-hop-sct.docx
    │   ├── to-trinh-vbqppl-tien-chat-thuoc-no.docx
    │   ├── ke-hoach-thuc-hien-de-an-08.docx
    │   ├── bao-cao-ket-qua-thang-atvsld.docx
    │   ├── bao-cao-tinh-hinh-trien-khai-ccn.docx
    │   ├── giay-phep-van-chuyen-hhnh.docx
    │   └── giay-chung-nhan-attp-winmart.docx
    └── ubnd/                             ← văn bản cấp UBND tỉnh / VP UBND
        ├── giay-moi-hop-ubnd.docx
        ├── cong-van-ubnd-tinh-chi-dao.docx
        ├── cong-van-vp-ubnd-truyen-dat.docx
        ├── thong-bao-ket-luan-ubnd.docx
        ├── phieu-trinh-giai-quyet-cong-viec.docx
        └── bao-cao-vp-ubnd.docx
```

## Nguyên lý hoạt động

1. Bạn upload các file mẫu .docx mà Bạn dùng hàng ngày → đặt vào `templates/`.
2. Khi cần soạn văn bản mới, Claude:
   - Mở file mẫu tương ứng bằng `python-docx`
   - Dùng helper `TemplateDoc` để sửa text trong các paragraph cụ thể
   - Lưu thành file mới
3. **Khung header, gạch chân, bảng chữ ký, font Times New Roman 14, lề, spacing** — tất cả giữ NGUYÊN từ file gốc.

## Cài đặt local (tùy chọn)

```bash
cd vbhc-vn
pip install python-docx
python3 scripts/demo_cong_van.py    # Tạo output/cong-van-an-thinh.docx
```

---

## CÁCH B — Memory edits (đã hoàn thành ✓)

Memory đã có 18 quy tắc về quy ước văn bản hành chính của Bạn. Mỗi cuộc trò chuyện mới Claude tự nhớ.

## CÁCH C — Project knowledge (KHUYẾN NGHỊ làm trước)

### Bước 1: Tạo Project trong Claude.ai
- Mở Claude.ai → **Projects** → **Create project** → tên: `Sở Công Thương - Văn bản hành chính`.

### Bước 2: Tải file vào Project knowledge
Tải lên 11 file:
- 7 file mẫu trong `templates/` (.docx)
- `scripts/fill_template.py`
- 3 file demo trong `scripts/`

### Bước 3: Project instructions

Vào **Custom instructions**, dán đoạn sau:

```
Đây là project soạn văn bản hành chính cho Sở Công Thương tỉnh Lào Cai.

QUY TẮC TỐI THƯỢNG: KHÔNG BAO GIỜ sinh văn bản từ đầu bằng code.
LUÔN làm theo quy trình sau:

1. Đọc fill_template.py để hiểu API thư viện.
2. Đọc 1 file demo phù hợp (demo_cong_van.py / demo_to_trinh.py / demo_quyet_dinh.py).
3. Mở file mẫu tương ứng trong templates/ bằng python-docx.
4. Dùng các method của TemplateDoc (replace_in_cell, set_paragraph_text, 
   replace_keeping_first_run, replace_body_paragraphs) để sửa nội dung.
5. Lưu file mới, validate, present_files.

Bảng tra cứu nhanh:
- Công văn → templates/01-cong-van.docx
- Tờ trình → templates/02-to-trinh.docx
- Báo cáo → templates/03-bao-cao.docx
- Kế hoạch → templates/04-ke-hoach.docx
- Quyết định cá biệt → templates/05-quyet-dinh.docx
- Giấy phép → templates/06-giay-phep.docx
- GCN ATTP → templates/07-giay-chung-nhan-attp.docx

KHÔNG tạo PDF. KHÔNG động vào cấu trúc table. KHÔNG xóa paragraph trong cells.

Người ký mặc định:
- QĐ, GP, GCN ATTP, BC, CV: KT.GĐ-PGĐ Nguyễn Đình Chiến
- TTr quan trọng: GIÁM ĐỐC Hoàng Chí Hiền
- "Lưu: VT, CN(Tên người soạn)" - hỏi tôi tên người soạn nếu không biết.
```

### Bước 4: Yêu cầu Claude

```
Tạo Quyết định thành lập Đoàn thẩm định cấp Giấy chứng nhận ATTP 
cho Công ty TNHH ABC tại Lô A12, KCN Đông Phố Mới, người soạn là Trang.
```

Claude sẽ mở `templates/05-quyet-dinh.docx`, sửa Số ký hiệu, tiêu đề, thông tin cụ thể của ABC, danh sách đoàn, người soạn → trả file `.docx` với layout y hệt mẫu.

---

## CÁCH A — Custom Skill (làm sau)

Đóng gói cả thư mục thành ZIP, upload tại Claude.ai → Settings → Capabilities → Skills.

---

## Cập nhật mẫu khi có thay đổi

Khi mẫu chuẩn của Sở thay đổi (vd: đổi nhân sự ký, đổi format header), chỉ cần:
1. Soạn lại file mẫu chuẩn trong Word.
2. Đặt đè vào `templates/` với cùng tên file.
3. Reupload Project knowledge / Custom Skill.

Không cần sửa code Python.

## Changelog

### v4 (19/6/2026) — Quy trình thực chiến + nâng cấp từ rà soát 10 ngày
- ✓ Thêm **Chế độ B**: sửa file .docx người dùng tải lên (unpack→sửa `word/document.xml`→pack `--original`), kèm các bài học XML (sed nhầm chữ ký, ngắt trang `lastRenderedPageBreak`, reorder `<w:tr>`, điền ô trống, paraId < 0x80000000).
- ✓ Thêm **QA trực quan bắt buộc** ở Bước 4: render PDF→JPG→`view` để bắt lỗi tràn lề/lệch cột/chữ ký rớt trang (validate sạch chưa đủ).
- ✓ Thêm **công thức căn bảng/biểu "vuông vắn, đều đẹp"** (A4 ngang, 9071 DXA, vAlign center, TT căn giữa, nội dung justify, header lặp mỗi trang, dòng Tổng cộng).
- ✓ Thêm **checklist đồng bộ chéo** Báo cáo ↔ Phụ lục ↔ văn bản VP UBND (số tổng, đánh số, tham chiếu chéo, không vá nửa vời).
- ✓ Thêm mục **toàn vẹn số liệu & metadata** (không bịa số/ngày, để trống chờ phát hành, xác minh PDF qua `vbhc-pdf-reader-vn`; tránh "dự kiến" trong bản trình ký).
- ✓ Quy tắc **7** (tên file `YYYY.MM.DD. [Tên VB].docx`), **8** (căn chỉnh & đồng bộ đánh số), **9** (in nghiêng đầu mục a), b), c)…).
- ✓ Làm rõ Quy tắc 5: được render PDF nội bộ để QA, chỉ KHÔNG giao PDF cho người dùng.
- ✓ Mở rộng `description` để skill bắt cả việc "rà soát/sửa/căn chỉnh/đồng bộ".

### v3 (29/4/2026) — Template-based approach
- ✓ Bỏ hoàn toàn việc sinh văn bản từ code (Node.js).
- ✓ Dùng 7 file mẫu thật của Bạn làm template.
- ✓ Helper Python `fill_template.py` để sửa text giữ nguyên format.
- ✓ 3 demo cụ thể: Công văn, Tờ trình, Quyết định cá biệt.

### v2 (29/4/2026)
- Sinh văn bản bằng Node.js — KHÔNG đúng layout, đã loại bỏ.

### v1
- Bộ template đầu tiên — đã loại bỏ.
