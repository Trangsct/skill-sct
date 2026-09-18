#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""normalize_body.py — chuan hoa than van ban .docx do co quan khac gui den (Che do B).

Xu ly 4 loi lap lai khi nhan file cua UBND cap xa / doanh nghiep:
  1. numPr  — dinh dang danh sach tu dong cua Word: Word tu chen them dau "-"
              truoc chu da go -> hien thi "- -"; xoa numPr, giu ky tu go that.
  2. w:ind  — moi nhom doan mot muc thut le (left=720, left=0, chi firstLine...)
              -> xoa het, dat left=0, right=0, firstLine=1cm dong nhat.
  3. w:tab  — tab thua o dau doan (lui dau dong chong len firstLine).
  4. doan trong thua nam giua than van ban -> xoa, chi giu 1 doan trong dau
     (duoi trich yeu) va 1 doan trong cuoi (truoc khoi Noi nhan - chu ky).

KHONG dung run.text = ... nen khong lam mat shape v:line trong header.
Khong dong vao bang (bang giu nguyen dinh dang goc).

Dung:
    python3 normalize_body.py file.docx                 # sua tai cho, ghi de
    python3 normalize_body.py file.docx -o out.docx     # ghi ra file khac
    python3 normalize_body.py file.docx --check         # chi bao cao, khong sua
    python3 normalize_body.py file.docx --indent 720    # lui dau dong 1,27cm

Sau khi chay: luon chay scripts/qa_all.py va soi anh render truoc khi giao.
"""
import argparse
import sys

from docx import Document
from docx.oxml.ns import qn
from docx.shared import Twips

TITLE_HINTS = ('THÔNG BÁO', 'CÔNG VĂN', 'BÁO CÁO', 'TỜ TRÌNH', 'KẾ HOẠCH',
               'QUYẾT ĐỊNH', 'BIÊN BẢN', 'GIẤY MỜI', 'PHỤ LỤC')


def is_title(p):
    t = p.text.strip()
    if not t:
        return False
    if t in TITLE_HINTS:
        return True
    pf = p.paragraph_format
    return pf.alignment is not None and int(pf.alignment) == 1   # CENTER


def normalize(path, out=None, indent=567, check=False):
    doc = Document(path)
    stat = {'numPr': 0, 'ind': 0, 'tab': 0, 'empty': 0}

    for p in doc.paragraphs:
        if not p.text.strip() or is_title(p):
            continue
        pPr = p._p.get_or_add_pPr()
        for e in pPr.findall(qn('w:numPr')):
            stat['numPr'] += 1
            if not check:
                pPr.remove(e)
        for e in pPr.findall(qn('w:ind')):
            a = {k.split('}')[1]: v for k, v in e.attrib.items()}
            if a.get('firstLine') != str(indent) or a.get('left') not in (None, '0'):
                stat['ind'] += 1
            if not check:
                pPr.remove(e)
        for r in p.runs:
            for t in r._r.findall(qn('w:tab')):
                stat['tab'] += 1
                if not check:
                    r._r.remove(t)
        if not check:
            pf = p.paragraph_format
            pf.left_indent = Twips(0)
            pf.right_indent = Twips(0)
            pf.first_line_indent = Twips(indent)

    empties = [q for q in doc.paragraphs if not q.text.strip()]
    # Giu 1 doan trong duoi trich yeu + 1 doan trong truoc khoi ky (Ban chot 18/9/2026:
    # khoi ky cach than dung MOT dong trong).
    thua = empties[1:-1] if len(empties) > 2 else []
    stat['empty'] = len(thua)
    if not check:
        for q in thua:
            q._p.getparent().remove(q._p)

    print('numPr (bullet tu dong) : %d' % stat['numPr'])
    print('w:ind  (thut le lech)  : %d' % stat['ind'])
    print('w:tab  (tab dau doan)  : %d' % stat['tab'])
    print('doan trong thua        : %d' % stat['empty'])

    if check:
        print('--check: khong ghi file.')
        return 1 if any(stat.values()) else 0

    doc.save(out or path)
    print('Da ghi: %s' % (out or path))
    return 0


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('docx')
    ap.add_argument('-o', '--out')
    ap.add_argument('--indent', type=int, default=567,
                    help='lui dau dong, twips (567 = 1cm, 720 = 1,27cm)')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    sys.exit(normalize(a.docx, a.out, a.indent, a.check))
