#!/usr/bin/env python3
"""Đánh số trang cho file Word từ 2 trang trở lên (Bạn chốt 17/11/2026).

Theo Nghị định 30/2020/NĐ-CP: số trang bằng chữ số Ả Rập, cỡ 13, kiểu chữ đứng, canh giữa
trong phần lề trên, không hiển thị số ở trang thứ nhất.

Dùng: python3 them_so_trang.py <file.docx> [file2.docx ...]
  - Đếm trang bằng LibreOffice (soffice); file chỉ 1 trang thì bỏ qua.
  - File đã có trường PAGE ở đầu hoặc chân trang thì không thêm lần nữa.
  --check : chỉ kiểm, trả mã 1 nếu có file từ 2 trang trở lên chưa có số trang.
"""
import copy
import re
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt


def so_trang(path):
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", tmp, str(path)],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
        pdf = Path(tmp) / (Path(path).stem + ".pdf")
        if not pdf.exists():
            return None
        out = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
        m = re.search(r"Pages:\s+(\d+)", out)
        return int(m.group(1)) if m else None


def da_co_so_trang(path):
    with zipfile.ZipFile(path) as z:
        for n in z.namelist():
            if re.match(r"word/(header|footer)\d*\.xml", n):
                x = z.read(n).decode("utf8", "ignore")
                if re.search(r"instrText[^>]*>\s*PAGE\b", x) or 'w:instr=" PAGE' in x or "w:instr=\"PAGE" in x:
                    return True
    return False


def them(path):
    d = Document(path)
    for s in d.sections:
        s.different_first_page_header_footer = True
        s.header.is_linked_to_previous = False
        h = s.header
        p = h.paragraphs[0] if h.paragraphs else h.add_paragraph()
        for r in list(p.runs):
            r._r.getparent().remove(r._r)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        for kind, text in (("begin", None), (None, " PAGE "), ("separate", None), (None, "2"), ("end", None)):
            r = p.add_run()
            r.font.name = "Times New Roman"
            r.font.size = Pt(13)
            r._r.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), "Times New Roman")
            if kind:
                fc = OxmlElement("w:fldChar")
                fc.set(qn("w:fldCharType"), kind)
                r._r.append(fc)
            elif text == " PAGE ":
                it = OxmlElement("w:instrText")
                it.set(qn("xml:space"), "preserve")
                it.text = text
                r._r.append(it)
            else:
                r.text = text
        if s.header_distance is None or s.header_distance > s.top_margin:
            s.header_distance = Pt(20)
    d.save(path)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check = "--check" in sys.argv
    if not args:
        print(__doc__)
        return 2
    thieu = 0
    for f in args:
        n = so_trang(f)
        if n is None:
            print(f"? {f}: không đếm được số trang")
            continue
        if n < 2:
            print(f"- {f}: {n} trang, không cần số trang")
            continue
        if da_co_so_trang(f):
            print(f"ok {f}: {n} trang, đã có số trang")
            continue
        if check:
            print(f"THIẾU {f}: {n} trang, chưa có số trang")
            thieu += 1
        else:
            them(f)
            print(f"+ {f}: {n} trang, đã thêm số trang (lề trên, canh giữa, ẩn trang 1)")
    return 1 if thieu else 0


if __name__ == "__main__":
    sys.exit(main())
