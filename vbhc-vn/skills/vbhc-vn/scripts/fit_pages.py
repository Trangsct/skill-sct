#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fit_pages.py — Can trang van ban dai (hop dong, phu luc hop dong) bang gian dong Exactly.

Quy tac 28 cua skill vbhc-vn:
  - Chi dung cho HOP DONG, PHU LUC HOP DONG va van ban dai nhieu trang.
    VBHC theo ND 30/2020 va bao cao dinh ky cua Phong van gian dong don, KHONG Exactly.
  - Muc gian dong hop le: 17-21 pt (340-420 twips), w:lineRule="exact".
    Duoi 17 pt dau tieng Viet (o, e, a co dau chong) bi cat khi in.
  - Gan keepNext + keepLines cho de muc "Dieu N."; gan keepNext cho cac doan cuoi
    truoc bang chu ky de khoi ky khong tro troi mot trang.

Cach dung:
  # Do thu moi muc, in so trang de chon
  python3 fit_pages.py sweep hop-dong.docx
  python3 fit_pages.py sweep hop-dong.docx --pts 17,17.5,18,19,20,21

  # Ap dung muc da chon va xuat file
  python3 fit_pages.py apply hop-dong.docx 18 -o hop-dong-can-trang.docx

Sau khi chot muc, PHAI cap nhat lai cau "Hop dong gom ... trang" theo so trang
PDF thuc te (doi gian dong ma quen sua so trang la loi).
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

PT_MIN, PT_MAX = 17.0, 21.0
DEFAULT_PTS = [17, 17.5, 18, 19, 20, 21]
SOFFICE = "/mnt/skills/public/docx/scripts/office/soffice.py"


def unpack(docx, dest):
    with zipfile.ZipFile(docx) as z:
        z.extractall(dest)


def pack(src, docx):
    if os.path.exists(docx):
        os.remove(docx)
    base = os.path.abspath(docx)
    subprocess.run(["zip", "-Xqr", base, "."], cwd=src, check=True)


def set_exact_spacing(xml, pt):
    """Doi moi gian dong dang auto sang exact theo so twips tuong ung."""
    tw = int(round(pt * 20))
    return re.sub(r'w:line="\d+" w:lineRule="(?:auto|exact|atLeast)"',
                  'w:line="%d" w:lineRule="exact"' % tw, xml)


def _insert_in_ppr(xml, p_start, props):
    """Chen props vao dau <w:pPr> cua doan bat dau tai p_start (tao pPr neu chua co)."""
    e = xml.find(">", p_start) + 1
    if xml[e:e + 8] == "<w:pPr>":
        return xml[:e + 8] + props + xml[e + 8:]
    if xml[e:e + 6] == "<w:pPr":
        k = xml.find(">", e) + 1
        return xml[:k] + props + xml[k:]
    return xml[:e] + "<w:pPr>" + props + "</w:pPr>" + xml[e:]


def keep_headings(xml, pattern=r"Điều \d+\."):
    """De muc 'Dieu N.' khong bi bo roi cuoi trang."""
    rx = re.compile(r"<w:p(?: [^>]*)?>(?:(?!</w:p>).)*?<w:t(?: [^>]*)?>" + pattern, re.S)
    for m in reversed(list(rx.finditer(xml))):
        xml = _insert_in_ppr(xml, m.start(), "<w:keepNext/><w:keepLines/>")
    return xml.replace("<w:keepNext/><w:keepLines/><w:keepNext/>", "<w:keepNext/><w:keepLines/>")


def keep_before_signature(xml, n=3):
    """n doan cuoi truoc bang chu ky di kem khoi ky."""
    tbl = xml.rfind("<w:tbl>")
    if tbl < 0:
        return xml
    head, tail = xml[:tbl], xml[tbl:]
    starts = [m.start() for m in re.finditer(r"<w:p(?: [^>]*)?>", head)]
    for s in reversed(starts[-n:]):
        head = _insert_in_ppr(head, s, "<w:keepNext/>")
    return head + tail


def build(src_docx, pt, out_docx, keep=True):
    tmp = tempfile.mkdtemp()
    try:
        unpack(src_docx, tmp)
        p = os.path.join(tmp, "word", "document.xml")
        xml = open(p, encoding="utf-8").read()
        xml = set_exact_spacing(xml, pt)
        if keep:
            xml = keep_headings(xml)
            xml = keep_before_signature(xml)
        open(p, "w", encoding="utf-8").write(xml)
        pack(tmp, out_docx)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return out_docx


def page_count(docx):
    out = os.path.dirname(os.path.abspath(docx)) or "."
    subprocess.run([sys.executable, SOFFICE, "--headless", "--convert-to", "pdf", docx],
                   cwd=out, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pdf = os.path.splitext(docx)[0] + ".pdf"
    if not os.path.exists(pdf):
        return None, None
    info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    m = re.search(r"^Pages:\s+(\d+)", info, re.M)
    return (int(m.group(1)) if m else None), pdf


def cmd_sweep(args):
    pts = [float(x) for x in args.pts.split(",")]
    work = tempfile.mkdtemp()
    print("muc pt | so trang   (chon muc nho trang nhat ma trang cuoi van du noi dung)")
    for pt in pts:
        if not (PT_MIN <= pt <= PT_MAX):
            print("%6s | bo qua: ngoai khoang 17-21 pt" % pt)
            continue
        out = os.path.join(work, "thu_%s.docx" % str(pt).replace(".", "_"))
        build(args.docx, pt, out, keep=not args.no_keep)
        n, _ = page_count(out)
        print("%6s | %s" % (pt, n if n else "khong render duoc"))
    print("\nAnh render trang cuoi cua muc da chon phai co dieu khoan hieu luc + khoi ky cung trang.")


def cmd_apply(args):
    pt = float(args.pt)
    if not (PT_MIN <= pt <= PT_MAX):
        sys.exit("Muc gian dong phai trong khoang 17-21 pt (Quy tac 28).")
    out = args.out or (os.path.splitext(args.docx)[0] + "-can-trang.docx")
    build(args.docx, pt, out, keep=not args.no_keep)
    n, _ = page_count(out)
    print("Da xuat: %s (gian dong Exactly %s pt, %s trang)" % (out, pt, n))
    print("Nho sua lai cau \"Hop dong gom ... trang\" cho khop %s trang." % n)


def main():
    ap = argparse.ArgumentParser(description="Can trang bang gian dong Exactly 17-21 pt")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("sweep", help="do thu cac muc gian dong, in so trang")
    s.add_argument("docx")
    s.add_argument("--pts", default=",".join(str(x) for x in DEFAULT_PTS))
    s.add_argument("--no-keep", action="store_true", help="khong gan keepNext/keepLines")
    s.set_defaults(func=cmd_sweep)

    a = sub.add_parser("apply", help="ap dung mot muc gian dong va xuat file")
    a.add_argument("docx")
    a.add_argument("pt")
    a.add_argument("-o", "--out")
    a.add_argument("--no-keep", action="store_true")
    a.set_defaults(func=cmd_apply)

    args = ap.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
