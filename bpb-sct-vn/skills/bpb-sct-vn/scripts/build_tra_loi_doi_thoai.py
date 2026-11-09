import re,sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

FONT="Times New Roman"; SZ=14
TIM=RGBColor(0x70,0x30,0xA0)
d=Document()
s=d.sections[0]
s.page_width=Cm(21); s.page_height=Cm(29.7)
s.top_margin=Cm(2); s.bottom_margin=Cm(2); s.left_margin=Cm(3); s.right_margin=Cm(2)
st=d.styles['Normal']; st.font.name=FONT; st.font.size=Pt(SZ)
st.element.rPr.rFonts.set(qn('w:eastAsia'),FONT); st.element.rPr.rFonts.set(qn('w:cs'),FONT)

def runs(p,text,size=SZ,bold=False,italic=False):
    # cú pháp: **đậm**, __nghiêng__, {{tím}}
    for part in re.split(r'(\*\*.+?\*\*|__.+?__|\{\{.+?\}\})',text):
        if not part: continue
        b,i,c=bold,italic,None
        if part.startswith('**'):
            part=part[2:-2]; b=True
            if part.startswith('__') and part.endswith('__'): part=part[2:-2]; i=True
        elif part.startswith('__'): part=part[2:-2]; i=True
        elif part.startswith('{{'): part=part[2:-2]; c=TIM
        r=p.add_run(part); r.font.name=FONT; r.font.size=Pt(size); r.bold=b; r.italic=i
        r._element.rPr.rFonts.set(qn('w:eastAsia'),FONT); r._element.rPr.rFonts.set(qn('w:cs'),FONT)
        if c: r.font.color.rgb=c

def fmt(p,align=WD_ALIGN_PARAGRAPH.JUSTIFY,indent=True,before=0,after=6):
    f=p.paragraph_format
    f.alignment=align; f.space_before=Pt(before); f.space_after=Pt(after)
    f.line_spacing=1.15; f.first_line_indent=Cm(1.0) if indent else Cm(0)
    f.widow_control=True

def para(text,container=None,first=None,**k):
    c=container or d
    p=first if first is not None else c.add_paragraph()
    kk={x:k.pop(x) for x in ('bold','italic','size') if x in k}
    fmt(p,**k); runs(p,text,**kk); return p

def borders(t):
    tblPr=t._tbl.tblPr
    b=OxmlElement('w:tblBorders')
    for e in ('top','left','bottom','right','insideH','insideV'):
        x=OxmlElement('w:'+e); x.set(qn('w:val'),'single'); x.set(qn('w:sz'),'4'); x.set(qn('w:space'),'0'); x.set(qn('w:color'),'000000'); b.append(x)
    tblPr.append(b)

def table(rows,cols,widths):
    t=d.add_table(rows=rows,cols=cols); t.alignment=WD_TABLE_ALIGNMENT.CENTER; borders(t)
    t.autofit=False
    for r in t.rows:
        for i,c in enumerate(r.cells):
            c.width=Cm(widths[i]); c.vertical_alignment=WD_ALIGN_VERTICAL.CENTER
    return t

C=WD_ALIGN_PARAGRAPH.CENTER
para("**CÂU HỎI THEO CHƯƠNG TRÌNH CỦA UBND TỈNH**",align=C,indent=False,after=0)
para("**LƯỢT 2 – CÂU 8**",align=C,indent=False,after=8)

t=table(2,3,[6.4,4.8,4.8])
for i,x in enumerate(["LĨNH VỰC","NGƯỜI HỎI","DỰ KIẾN TRẢ LỜI"]):
    para("**%s**"%x,first=t.cell(0,i).paragraphs[0],align=C,indent=False,before=3,after=3)
for i,x in enumerate(["Các cơ chế chính sách hỗ trợ, vốn vay, Quỹ khởi nghiệp","**Đoàn xã Mường Khương**","**Sở Công Thương**"]):
    para(x,first=t.cell(1,i).paragraphs[0],align=C,indent=False,before=3,after=3)
para("",indent=False,after=0)

Q="Câu hỏi: “Kính thưa đồng chí Chủ tịch UBND tỉnh! Hiện nay, nhiều đoàn viên, thanh niên trên địa bàn xã Mường Khương đã mạnh dạn phát triển các sản phẩm đặc trưng, như: chè, quýt, tương ớt, chuối, lạc hoa... Tuy nhiên, phần lớn các mô hình còn có **__quy mô nhỏ; việc xây dựng và phát triển thương hiệu, nâng cao giá trị sản phẩm, mở rộng thị trường và kết nối tiêu thụ còn gặp nhiều khó khăn.__** Vậy trong thời gian tới, tỉnh có những cơ chế, chính sách và giải pháp cụ thể nào để hỗ trợ đoàn viên, thanh niên xây dựng thương hiệu, nâng cao chất lượng và giá trị các sản phẩm đặc trưng; đồng thời hỗ trợ kết nối, quảng bá và tiêu thụ sản phẩm thông qua các sàn thương mại điện tử, hệ thống siêu thị, các kênh phân phối và mở rộng thị trường trong và ngoài tỉnh, qua đó tạo điều kiện để thanh niên phát triển sản xuất, khởi nghiệp và nâng cao thu nhập?”"
Q=Q.replace("**__","\x01").replace("__**","\x02")
t=table(2,1,[16]); 
para("**CÂU HỎI**",first=t.cell(0,0).paragraphs[0],align=C,indent=False,before=3,after=3)
p=t.cell(1,0).paragraphs[0]; fmt(p,indent=False,before=3,after=3)
a,rest=Q.split("\x01"); b,c2=rest.split("\x02")
runs(p,a); runs(p,b,bold=True,italic=True); runs(p,c2)
para("",indent=False,after=0)

ANS=open(sys.argv[1],encoding='utf8').read().strip().split("\n")
t=table(2,1,[16])
para("**CÂU TRẢ LỜI**",first=t.cell(0,0).paragraphs[0],align=C,indent=False,before=3,after=3)
cell=t.cell(1,0); first=cell.paragraphs[0]
for i,line in enumerate([l for l in ANS if l.strip()]):
    line=line.strip()
    if line.startswith('[C]'):
        para('**__'+line[3:]+'__**',container=cell,first=None,align=C,indent=False,before=4,after=4)
    else:
        pp=para(line,container=cell,first=first if i==0 else None,indent=(i>0),before=2,after=4)
        if re.match(r'^\*\*\d\.',line): pp.paragraph_format.keep_with_next=True
# cho phép dòng bảng tách qua trang (mặc định), không lặp

para("",indent=False,after=0)
para("**MỘT SỐ NỘI DUNG DỰ KIẾN CHUẨN BỊ THÊM**",align=C,indent=False,before=6,after=6)
for line in open(sys.argv[2],encoding='utf8').read().strip().split("\n"):
    if line.strip(): para(line.strip())
d.save(sys.argv[3])
