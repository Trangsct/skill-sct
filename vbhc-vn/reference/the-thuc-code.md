# Mã chuẩn thể thức — chỉ dùng khi DỰNG MỚI TỪ ĐẦU

Ưu tiên luôn là dùng `templates/` hoặc `examples/` (giữ định dạng sẵn). File này chỉ dùng cho
trường hợp **không có mẫu phù hợp** và buộc phải sinh `.docx` bằng code. Hai thứ dưới đây là 2 lỗi
đã lặp lại nhiều lần (lùi đầu dòng không đồng nhất; đường gạch chân vẽ sai cách), nên chép sẵn để
khỏi mò lại. Dựng xong **luôn render ra ảnh kiểm tra từng trang** rồi mới xuất.

## 1. Một hàm định dạng đoạn DUY NHẤT — lùi 1cm đồng nhất

Lý do: nếu mỗi loại đề mục (I/II, 1/2, a/b, "một là") lại set thụt lề riêng thì văn bản bị "cái
vào cái ra". Dùng đúng một hàm cho MỌI đoạn (đề mục lẫn nội dung), mặc định `firstLine = 1cm`,
không bao giờ đặt `firstLine = 0` cho đề mục. Số thứ tự (1., 2., a., b.) viết liền vào đầu chuỗi
văn bản, KHÔNG dùng numbering treo (hanging) của Word.

### python-docx
```python
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING

def P(doc, text, *, bold=False, italic=False, center=False, left=False, size=14):
    """Hàm định dạng đoạn DUY NHẤT cho mọi đoạn trong VBHC."""
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.first_line_indent = Cm(1)              # lùi đầu dòng đồng nhất 1cm
    pf.space_before = Pt(6); pf.space_after = Pt(6)
    pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
    if center:
        pf.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif left:                                # dòng "Ông/Bà:..." để trái cho gọn
        pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
    else:
        pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r = p.add_run(text)
    r.font.name = "Times New Roman"; r.font.size = Pt(size)
    r.font.color.rgb = RGBColor(0, 0, 0)
    r.bold = bold; r.italic = italic
    return p
# Dòng thành phần dùng left=True: P(doc, "Ông/Bà: ...\t- ...;", left=True)
```

### docx-js (Node) — tương đương
```javascript
const FONT="Times New Roman", SZ=28; // half-points => 14pt
function P(text,{bold=false,italic=false,center=false,left=false}={}) {
  return new Paragraph({
    alignment: center?AlignmentType.CENTER:(left?AlignmentType.LEFT:AlignmentType.JUSTIFIED),
    spacing:{before:120,after:120,line:240,lineRule:"auto"}, // single
    indent:{firstLine:567},                                   // 567 twips = 1cm
    children:[new TextRun({text,font:FONT,size:SZ,bold,italics:italic,color:"000000"})],
  });
}
```

## 2. Đường gạch chân ngang = ĐỐI TƯỢNG LINE (không underscore, không border đoạn)

Lý do: ký tự underscore và border đoạn không phải đối tượng vẽ — không chỉnh được độ dài/căn giữa,
dễ lệch khi sửa nội dung, và không đúng cách Văn thư trình bày. Phải là một Line shape (Insert >
Shapes > Line) — mở trong Word chọn/di chuyển được.

Đã kiểm chứng: **VML `<v:line>` nổi, căn giữa theo lề** hiển thị đúng cả ở LibreOffice và Word.
(Inline DrawingML `cy=0` KHÔNG hiển thị trong LibreOffice — tránh.)

### Quy trình: docx-js đặt placeholder → unpack → thay bằng VML → pack
Trong lúc dựng, ở vị trí cần đường kẻ chèn một đoạn placeholder căn giữa: `P("@@HEADER_RULE@@",{center:true})`.
Sau khi xuất .docx, chạy đoạn Python sau để thay placeholder bằng đường Line:

```python
import re, subprocess, os, shutil
SK="/mnt/skills/public/docx/scripts/office"
def inject_line(docx_path):
    work="/tmp/_inj_"+os.path.basename(docx_path).replace(".docx","")
    if os.path.exists(work): shutil.rmtree(work)
    subprocess.run(["python",f"{SK}/unpack.py",docx_path,work],check=True)
    xmlp=f"{work}/word/document.xml"; s=open(xmlp,encoding="utf-8").read()
    vml=('<w:r><w:rPr><w:noProof/></w:rPr><w:pict>'
         '<v:line xmlns:v="urn:schemas-microsoft-com:vml" '
         'xmlns:o="urn:schemas-microsoft-com:office:office" id="HeaderRule" '
         'o:spid="_x0000_s1026" '
         'style="position:absolute;z-index:251658240;mso-position-horizontal:center;'
         'mso-position-horizontal-relative:margin;mso-position-vertical-relative:line" '
         'from="0,7pt" to="144pt,7pt" o:gfxdata="" strokecolor="black" '
         'strokeweight=".75pt"/></w:pict></w:r>')
    s,n=re.subn(r'<w:r>(?:(?!</w:r>).)*?@@HEADER_RULE@@.*?</w:r>', vml, s, flags=re.S)
    assert n>=1, "khong thay placeholder @@HEADER_RULE@@"
    open(xmlp,"w",encoding="utf-8").write(s)
    subprocess.run(["python",f"{SK}/pack.py",work,docx_path,"--original",docx_path],check=True)
```

Tham số: `from/to` = chiều ngang đường kẻ (144pt ≈ 5,08cm ≈ 1/2 ô); `strokeweight` độ đậm;
`mso-position-horizontal:center` + `...relative:margin` để căn giữa theo lề. Mỗi đường một `id`
riêng nếu có nhiều đường trong cùng file.

## 3. Render kiểm tra bắt buộc trước khi xuất
```bash
python /mnt/skills/public/docx/scripts/office/soffice.py --headless --convert-to pdf out.docx --outdir /tmp
pdftoppm -jpeg -r 110 /tmp/out.pdf /tmp/qa
# rồi view các ảnh qa-*.jpg: kiểm tra đường kẻ hiển thị, lùi đầu dòng đồng nhất, không tràn lề
```
Lưu ý: LibreOffice (trình render preview) có thể hiển thị shape lệch nhẹ so với Word — nếu cần
chắc chắn tuyệt đối, mở lại bằng Word để xác nhận đường Line.
