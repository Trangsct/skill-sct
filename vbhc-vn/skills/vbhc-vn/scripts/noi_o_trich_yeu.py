#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""noi_o_trich_yeu.py — Nới bề rộng ô trích yếu "V/v …" của công văn mà KHÔNG dùng lề đoạn âm.

Vì sao: lề đoạn âm (w:ind left/right < 0) trong ô bảng làm chữ tràn ra ngoài ô. LibreOffice vẫn vẽ đủ, nhưng
Word khi xuất PDF (và hệ thống ký số) CẮT phần chữ nằm ngoài ô → trích yếu mất chữ hai bên (Bạn chỉ ra
19/11/2026, sổ lỗi L018, R30). Cách đúng: nới chính Ô bằng lưới bảng, cân hai bên để tâm trích yếu vẫn trùng
tâm khối tên cơ quan:

    lưới cũ   [A][C]            →  lưới mới  [L][A][M][C-M]      (L = M = --them twip; bảng dịch trái L)
    hàng trên [A][C]            →  [L+A, đoạn lùi trái +L][M+C]   (chữ đứng nguyên chỗ cũ)
    hàng V/v  [A][C]            →  [L+A+M][C-M]                   (ô rộng thêm 2 × them, lề đoạn 0)

CÁCH DÙNG
    python3 scripts/noi_o_trich_yeu.py <file>.docx              # nới mỗi bên 340 twip (0,6 cm)
    python3 scripts/noi_o_trich_yeu.py <file>.docx --them 280
    python3 scripts/noi_o_trich_yeu.py <file>.docx --check      # chỉ báo có lề âm trong bảng đầu trang hay không
Sau khi chạy: `python3 scripts/do_trich_yeu.py <file>.docx` để đo lại số dòng, cân tâm, khoảng cách chữ "CỘNG".
"""
from __future__ import annotations

import argparse
import sys
import unicodedata

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


def _nfc(s):
    return unicodedata.normalize("NFC", s or "")


def le_am(tbl) -> list:
    """Các w:ind có lề trái/phải âm trong một bảng."""
    ra = []
    for ind in tbl.iter(qn("w:ind")):
        for a in ("w:left", "w:right", "w:start", "w:end"):
            v = ind.get(qn(a))
            if v and v.lstrip().startswith("-"):
                ra.append((ind, a))
    return ra


def _hang_vv(tbl):
    for tr in tbl.findall(qn("w:tr")):
        tcs = tr.findall(qn("w:tc"))
        if tcs and _nfc("".join(tcs[0].itertext())).strip().lower().startswith("v/v"):
            return tr
    return None


def _dat_o(tc, rong: int, span: int) -> None:
    tcPr = tc.find(qn("w:tcPr"))
    if tcPr is None:
        tcPr = OxmlElement("w:tcPr"); tc.insert(0, tcPr)
    tcW = tcPr.find(qn("w:tcW"))
    if tcW is None:
        tcW = OxmlElement("w:tcW"); tcPr.insert(0, tcW)
    tcW.set(qn("w:w"), str(rong)); tcW.set(qn("w:type"), "dxa")
    gs = tcPr.find(qn("w:gridSpan"))
    if span > 1:
        if gs is None:
            gs = OxmlElement("w:gridSpan"); tcW.addnext(gs)
        gs.set(qn("w:val"), str(span))
    elif gs is not None:
        tcPr.remove(gs)


def noi(doc, them: int = 340) -> bool:
    """Nới ô V/v của bảng đầu trang mỗi bên `them` twip. Trả False khi bảng không đúng dạng 2 cột."""
    if not doc.tables:
        return False
    tbl = doc.tables[0]._tbl
    grid = tbl.find(qn("w:tblGrid"))
    cols = grid.findall(qn("w:gridCol"))
    tr_vv = _hang_vv(tbl)
    if len(cols) != 2 or tr_vv is None:
        return False
    a, c = (int(x.get(qn("w:w"))) for x in cols)
    if any(len(tr.findall(qn("w:tc"))) != 2 for tr in tbl.findall(qn("w:tr"))):
        return False
    # lưới mới [L][A][M][C-M]
    for x in cols:
        grid.remove(x)
    for w in (them, a, them, c - them):
        g = OxmlElement("w:gridCol"); g.set(qn("w:w"), str(w)); grid.append(g)
    tblPr = tbl.tblPr
    tw = tblPr.find(qn("w:tblW"))
    if tw is not None and tw.get(qn("w:type")) == "dxa":
        tw.set(qn("w:w"), str(a + c + them))
    ind = tblPr.find(qn("w:tblInd"))
    if ind is None:
        ind = OxmlElement("w:tblInd"); ind.set(qn("w:type"), "dxa"); ind.set(qn("w:w"), "0")
        (tw if tw is not None else tblPr[0]).addnext(ind)
    ind.set(qn("w:w"), str(int(ind.get(qn("w:w")) or 0) - them))
    for tr in tbl.findall(qn("w:tr")):
        t1, t2 = tr.findall(qn("w:tc"))
        if tr is tr_vv:
            _dat_o(t1, them + a + them, 3)
            _dat_o(t2, c - them, 1)
            for p in t1.findall(qn("w:p")):          # bỏ lề âm/dương cũ của trích yếu
                pPr = p.find(qn("w:pPr"))
                old = pPr.find(qn("w:ind")) if pPr is not None else None
                if old is not None:
                    pPr.remove(old)
        else:
            _dat_o(t1, them + a, 2)
            _dat_o(t2, c, 2)
            for p in t1.findall(qn("w:p")):          # giữ chữ đứng nguyên chỗ: lùi trái đúng bằng cột L
                pPr = p.find(qn("w:pPr"))
                if pPr is None:
                    pPr = OxmlElement("w:pPr"); p.insert(0, pPr)
                pi = pPr.find(qn("w:ind"))
                if pi is None:
                    pi = OxmlElement("w:ind")
                    jc = pPr.find(qn("w:jc"))
                    (jc.addprevious(pi) if jc is not None else pPr.append(pi))
                pi.set(qn("w:left"), str(int(pi.get(qn("w:left")) or 0) + them))
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file")
    ap.add_argument("--them", type=int, default=340, help="twip nới mỗi bên (mặc định 340 = 0,6 cm)")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    doc = Document(a.file)
    if not doc.tables:
        print("Không có bảng đầu trang."); return 0
    am = le_am(doc.tables[0]._tbl)
    if a.check:
        print(f"{'CÓ' if am else 'không có'} lề đoạn âm trong bảng đầu trang ({len(am)} chỗ)")
        return 1 if am else 0
    if not noi(doc, a.them):
        print("LỖI: bảng đầu trang không đúng dạng 2 cột có ô V/v — sửa tay.", file=sys.stderr); return 2
    doc.save(a.file)
    print(f"Đã nới ô trích yếu mỗi bên {a.them} twip bằng lưới bảng, bỏ lề đoạn âm.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
