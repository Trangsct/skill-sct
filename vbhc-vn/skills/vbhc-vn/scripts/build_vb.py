#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_vb.py — Trình biên dịch NỘI DUNG DẠNG THẺ sang .docx trên mẫu thật (Chế độ B).

Vì sao có script này: phần dễ sai nhất khi soạn là sửa XML tay từng run — mất đường Line,
mất nghiêng dòng ngày, quên chỉ số dưới công thức hóa học, lùi đầu dòng không đều. Với script
này chỉ cần viết NỘI DUNG dạng text có thẻ; script dựng .docx trên mẫu thật và tự chuẩn hóa
thể thức, nên các lỗi đó không còn chỗ phát sinh. Sửa lần hai chỉ là sửa text rồi build lại.

Mở rộng cơ chế thẻ của build_bao_cao_phong.py ra ĐỦ 7 LOẠI: công văn, tờ trình, báo cáo,
kế hoạch, quyết định, giấy phép, công văn nội bộ Phòng.

NGUYÊN TẮC GIỮ NGUYÊN (Nhóm F, Quy tắc bất biến 1, 2, 11):
  - Chỉ thay các paragraph THÂN VĂN BẢN ở cấp tài liệu.
  - KHÔNG đụng bảng header, bảng chữ ký, đường Line, dòng Số, dòng địa danh/ngày.
  - Muốn sửa trích yếu, người ký, Nơi nhận thì sửa trên file xuất ra hoặc dùng fill_template.py.

CÁCH DÙNG
    python3 scripts/build_vb.py noi-dung.txt ra.docx --loai cong-van
    python3 scripts/build_vb.py noi-dung.txt ra.docx --mau examples/sct/<file>.docx
    ... --than-tu 6            # ép vị trí paragraph thân đầu tiên nếu tự dò sai
    ... --khong-qa             # bỏ bước chạy qa_rules sau khi dựng

FILE NỘI DUNG — mỗi dòng một đoạn, thẻ ở đầu dòng:
    [H]  đề mục ĐẬM đứng      (I. / II. / 1. / 2.)
    [I]  đề mục NGHIÊNG       (a) / b) / c) — nhãn và tiêu đề ngắn, theo Quy tắc bất biến 9)
    [K]  dòng "Kính gửi: …"   (căn giữa, không đậm — Nhóm G, R04)
    [P]  đoạn thường          (mặc định khi không ghi thẻ)
    ##   dòng chú thích, bỏ qua

TỰ CHUẨN HÓA (không phải nhớ, không sửa tay được nữa):
  - Công thức hóa học P2O5, H2SO4, CO2… → chữ số thành chỉ số DƯỚI thật (Quy tắc 25, R02).
  - Đơn vị m2, m3, km2 → chữ số thành chỉ số TRÊN thật (Quy tắc bất biến 8).
  - Mọi đoạn thân lùi đầu dòng ĐỒNG ĐỀU theo trị phổ biến của chính mẫu (Quy tắc 27(b), R13).
  - Đoạn thường căn đều hai bên; đề mục giữ căn lề của mẫu.
  - Cấm ngắt dòng cứng: gặp "\\n" trong một dòng nội dung là dừng và báo lỗi (Quy tắc 10).
  - Cấm markdown: gặp ** hoặc * đầu dòng là dừng và báo lỗi (quy ước văn phong).

Dựng xong script tự chạy qa_rules.py trên file kết quả và in báo cáo. Vẫn phải chạy tiếp
`qa_all.py` để soi ảnh render trước khi giao.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

try:
    from docx import Document
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.shared import Cm
except ImportError:  # pragma: no cover
    print("LỖI: thiếu python-docx. Cài: pip install python-docx", file=sys.stderr)
    raise

SCRIPT_DIR = Path(__file__).resolve().parent
PLUGIN_DIR = SCRIPT_DIR.parent
EX = PLUGIN_DIR / "examples"

# Mẫu thật mặc định cho từng loại (Chế độ B — ưu tiên mẫu đã ban hành hơn template trắng).
MAU_MAC_DINH = {
    "cong-van": EX / "sct" / "cong-van-de-nghi-bo-sung-ho-so.docx",
    "cong-van-noi-bo": EX / "sct" / "cong-van-noi-bo-phong-tham-gia-y-kien-kcn.docx",
    "to-trinh": EX / "sct" / "to-trinh-vbqppl-tien-chat-thuoc-no.docx",
    "bao-cao": EX / "sct" / "bao-cao-tinh-hinh-trien-khai-ccn.docx",
    "bao-cao-phong": EX / "sct" / "bao-cao-thang-phong-qlcn.docx",
    "ke-hoach": EX / "sct" / "ke-hoach-thuc-hien-de-an-08.docx",
    "giay-phep": EX / "sct" / "giay-phep-van-chuyen-hhnh.docx",
    "bien-ban": EX / "sct" / "bien-ban-lam-viec-lien-nganh-ccn.docx",
}

CHEM = re.compile(
    r"(?<![A-Za-zÀ-ỹ0-9])("
    r"P2O5|H2SO4|H3PO4|H2O2|HNO3|NH3|NH4|CO2|SO2|SO3|NO2|N2O|CH4|H2O|H2S|"
    r"CaCO3|CaO|Al2O3|Fe2O3|Fe3O4|SiO2|AlF3|NaOH|KOH|Na2CO3|NaCl|CaSO4|MgO|CuSO4|ZnO|TiO2"
    r")(?![A-Za-zÀ-ỹ0-9])")
MU = re.compile(r"(?<![A-Za-zÀ-ỹ0-9])((?:k?m|c?m|dm|ha)\s?)([23])(?![\dA-Za-zÀ-ỹ])")


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s or "")


# ────────────────────────── Đọc file nội dung ──────────────────────────

THE = {"[H]": "h", "[I]": "i", "[K]": "k", "[P]": "p"}


def doc_noi_dung(p: Path) -> list[tuple[str, str]]:
    ra: list[tuple[str, str]] = []
    for so, dong in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        dong = dong.rstrip()
        if not dong.strip() or dong.lstrip().startswith("##"):
            continue
        kieu = "p"
        for the, k in THE.items():
            if dong.startswith(the):
                kieu, dong = k, dong[len(the):].strip()
                break
        if "**" in dong or dong.lstrip().startswith("* "):
            raise SystemExit(
                f"LỖI dòng {so}: dùng markdown trong nội dung VBHC.\n  {dong[:70]}\n"
                f"  → Đậm/nghiêng thể hiện bằng thẻ [H]/[I], không bằng ** hay *.")
        if "\\n" in dong or "\r" in dong:
            raise SystemExit(
                f"LỖI dòng {so}: có ngắt dòng cứng (Quy tắc bất biến 10).\n  {dong[:70]}\n"
                f"  → Muốn xuống dòng thì tách thành một dòng nội dung riêng.")
        ra.append((nfc(dong), kieu))
    if not ra:
        raise SystemExit(f"LỖI: {p} không có dòng nội dung nào.")
    return ra


# ────────────────────────── Dựng đoạn ──────────────────────────

def _chia_chi_so(text: str) -> list[tuple[str, str | None]]:
    """Cắt chuỗi thành các mẩu (text, kiểu) với kiểu ∈ {None, 'sub', 'sup'}.

    Công thức hóa học → chữ số 'sub'; đơn vị m2/m3 → chữ số 'sup'.
    """
    moc: list[tuple[int, int, str]] = []
    for m in CHEM.finditer(text):
        for c in re.finditer(r"\d+", m.group(1)):
            moc.append((m.start(1) + c.start(), m.start(1) + c.end(), "sub"))
    for m in MU.finditer(text):
        moc.append((m.start(2), m.end(2), "sup"))
    if not moc:
        return [(text, None)]
    moc.sort()
    ra: list[tuple[str, str | None]] = []
    cur = 0
    for a, b, k in moc:
        if a < cur:
            continue
        if a > cur:
            ra.append((text[cur:a], None))
        ra.append((text[a:b], k))
        cur = b
    if cur < len(text):
        ra.append((text[cur:], None))
    return ra


def viet(p, text: str, dam: bool, nghieng: bool) -> None:
    """Ghi text vào paragraph, giữ định dạng run mẫu, tự tách run chỉ số trên/dưới."""
    co_chu = [r for r in p.runs if r.text.strip()]
    goc = co_chu[0] if co_chu else (p.runs[0] if p.runs else p.add_run(""))
    # So sánh theo PHẦN TỬ XML, không theo object: python-docx tạo object Run bọc MỚI mỗi lần
    # đọc p.runs, nên `r is not goc` luôn đúng và sẽ xóa nhầm cả run gốc (lỗi đã mắc 16/9/2026:
    # mẩu chữ đầu mỗi đoạn biến mất khi đoạn có công thức hóa học).
    for r in list(p.runs):
        if r._element is not goc._element:
            r._element.getparent().remove(r._element)
    manh = _chia_chi_so(text)
    goc.text = manh[0][0]
    goc.bold = True if dam else None
    goc.italic = True if nghieng else None
    if manh[0][1] == "sub":
        goc.font.subscript = True
    elif manh[0][1] == "sup":
        goc.font.superscript = True
    truoc = goc
    for phan, kieu in manh[1:]:
        moi = p.add_run(phan)
        moi.font.name = goc.font.name
        moi.font.size = goc.font.size
        moi.bold = True if dam else None
        moi.italic = True if nghieng else None
        if kieu == "sub":
            moi.font.subscript = True
        elif kieu == "sup":
            moi.font.superscript = True
        truoc = moi
    return truoc


def lui_pho_bien(doc) -> float | None:
    """Trị firstLine phổ biến nhất trong thân mẫu — để lùi đầu dòng đồng đều (R13)."""
    dem: dict[float, int] = {}
    for p in doc.paragraphs:
        if len(nfc(p.text).strip()) < 30:
            continue
        if p.alignment is not None and int(p.alignment) == 1:
            continue
        fi = p.paragraph_format.first_line_indent
        v = round(fi.cm, 2) if fi is not None else 0.0
        dem[v] = dem.get(v, 0) + 1
    if not dem:
        return None
    return max(dem.items(), key=lambda kv: kv[1])[0]


def do_than(doc, co_kinh_gui: bool) -> tuple[int, int]:
    """Khoảng paragraph THÂN ở cấp tài liệu.

    Bắt đầu sau khối tên loại / trích yếu / Kính gửi của mẫu. Nếu file nội dung CÓ dòng [K]
    thì bắt đầu NGAY TẠI dòng Kính gửi của mẫu để thay nó, tránh ra hai dòng Kính gửi.
    """
    ps = doc.paragraphs
    dau, i_kg = 0, None
    for i, p in enumerate(ps[:14]):
        t = nfc(p.text).strip()
        if re.match(r"^Kính\s+gửi", t):
            i_kg = i
            dau = i + 1
        elif p.alignment is not None and int(p.alignment) == 1 and t:
            dau = max(dau, i + 1)
    if co_kinh_gui and i_kg is not None:
        dau = i_kg
    cuoi = max((i for i, p in enumerate(ps) if nfc(p.text).strip()), default=dau)
    return dau, cuoi


# ────────────────── Khối "Kính gửi" và khoảng cách giữa các khối (Bạn chốt 18/9/2026) ──────────────────
# Bạn chốt 18/9/2026: gửi MỘT cơ quan thì "Kính gửi:" và tên cơ quan phải nằm TRÊN CÙNG MỘT DÒNG;
# gửi NHIỀU cơ quan thì "Kính gửi:" tách lên trên, danh sách xuống dưới. Khối Kính gửi cách khối trên
# (trích yếu) và khối dưới (thân) đúng một dòng trống; khối ký cách thân đúng một dòng trống.
# Mẫu thật của Sở có hai kiểu khối Kính gửi: paragraph căn giữa (một nơi nhận) và bảng 2 ô (nhiều
# nơi nhận) — script phải dựng đúng kiểu theo SỐ nơi nhận trong dòng [K], không theo kiểu của mẫu.

def _phan_tu_than(doc) -> list[tuple[str, object]]:
    """Các phần tử ở cấp tài liệu theo thứ tự đọc: ('p', Paragraph) hoặc ('t', Table)."""
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    ra: list[tuple[str, object]] = []
    for ch in doc.element.body.iterchildren():
        if ch.tag.endswith("}p"):
            ra.append(("p", Paragraph(ch, doc)))
        elif ch.tag.endswith("}tbl"):
            ra.append(("t", Table(ch, doc)))
    return ra


def _trong(x) -> bool:
    return x[0] == "p" and not nfc(x[1].text).strip()


def bang_kinh_gui(doc):
    """Bảng 2 ô dùng làm khối Kính gửi trong mẫu (ô đầu bắt đầu bằng 'Kính gửi')."""
    for t in doc.tables:
        for r in t.rows:
            for c in r.cells:
                if re.match(r"^Kính\s+gửi", nfc(c.text).strip()):
                    return t
    return None


def p_kinh_gui(doc):
    for p in doc.paragraphs[:14]:
        if re.match(r"^Kính\s+gửi", nfc(p.text).strip()):
            return p
    return None


def tach_noi_nhan(dong: str) -> list[str]:
    """'Kính gửi: A; B.' → ['A', 'B'] (bỏ chữ 'Kính gửi', dấu ; . - ở hai đầu)."""
    s = re.sub(r"^\s*Kính\s+gửi\s*:?\s*", "", nfc(dong)).strip()
    return [x.strip().strip(";.").strip() for x in s.split(";") if x.strip().strip(";.-").strip()]


def _p_moi_tu_khuon(khuon, text: str, cang_giua: bool):
    """Nhân bản paragraph khuôn (giữ font mẫu) rồi ghi text; trả Paragraph mới CHƯA gắn vào thân."""
    from copy import deepcopy
    from docx.text.paragraph import Paragraph
    el = deepcopy(khuon._p)
    p = Paragraph(el, khuon._parent)
    if text:
        viet(p, text, dam=False, nghieng=False)
    else:
        for r in list(p.runs):
            r._element.getparent().remove(r._element)
    p.paragraph_format.first_line_indent = None
    if cang_giua:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    return p


def dat_kinh_gui(doc, dong: str, khuon) -> None:
    """Dựng khối Kính gửi đúng thể thức theo SỐ nơi nhận (xem ghi chú đầu mục)."""
    muc = tach_noi_nhan(dong)
    bang, p_kg = bang_kinh_gui(doc), p_kinh_gui(doc)
    if len(muc) <= 1:
        ten = (muc[0] if muc else "").rstrip(".")
        text = f"Kính gửi: {ten}." if ten else "Kính gửi:"
        if bang is not None:
            # Thay cả bảng bằng MỘT dòng căn giữa, giữ đúng một dòng trống ở trên và ở dưới.
            tbl = bang._tbl
            truoc_trong = tbl.getprevious() is not None and tbl.getprevious().tag.endswith("}p") \
                and not nfc(tbl.getprevious().xpath("string(.)")).strip()
            sau_trong = tbl.getnext() is not None and tbl.getnext().tag.endswith("}p") \
                and not nfc(tbl.getnext().xpath("string(.)")).strip()
            p_moi = _p_moi_tu_khuon(khuon, text, cang_giua=True)
            tbl.addprevious(p_moi._p)
            if not truoc_trong:
                p_moi._p.addprevious(_p_moi_tu_khuon(khuon, "", cang_giua=False)._p)
            if not sau_trong:
                p_moi._p.addnext(_p_moi_tu_khuon(khuon, "", cang_giua=False)._p)
            tbl.getparent().remove(tbl)
        elif p_kg is not None:
            viet(p_kg, text, dam=False, nghieng=False)
            p_kg.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_kg.paragraph_format.first_line_indent = None
        return
    # Nhiều nơi nhận: "Kính gửi:" ở trên, danh sách '- A;' … '- Z.' ở dưới.
    ds = [f"- {m};" for m in muc[:-1]] + [f"- {muc[-1].rstrip('.')}."]
    if bang is not None:
        o_trai, o_phai = None, None
        for r in bang.rows:
            for c in r.cells:
                if re.match(r"^Kính\s+gửi", nfc(c.text).strip()):
                    o_trai = c
                elif o_trai is not None and o_phai is None and c is not o_trai:
                    o_phai = c
        if o_phai is None:      # bảng một ô: ghi cả khối vào ô đó
            o_phai = o_trai
        ps = o_phai.paragraphs
        khuon_o = ps[0]
        for extra in ps[1:]:
            extra._p.getparent().remove(extra._p)
        viet(khuon_o, ds[0], dam=False, nghieng=False)
        truoc = khuon_o
        for dong_ds in ds[1:]:
            p_moi = _p_moi_tu_khuon(khuon_o, dong_ds, cang_giua=False)
            p_moi.alignment = khuon_o.alignment
            truoc._p.addnext(p_moi._p)
            truoc = p_moi
        if o_trai is not o_phai:
            viet(o_trai.paragraphs[0], "Kính gửi:", dam=False, nghieng=False)
        return
    if p_kg is not None:
        viet(p_kg, "Kính gửi:", dam=False, nghieng=False)
        truoc = p_kg
        for dong_ds in ds:
            p_moi = _p_moi_tu_khuon(khuon, dong_ds, cang_giua=False)
            truoc._p.addnext(p_moi._p)
            truoc = p_moi


def cach_mot_dong_truoc_khoi_ky(doc, khuon) -> None:
    """Khối ký (bảng có 'Nơi nhận' / chức danh người ký) cách thân ĐÚNG MỘT dòng trống.

    Bạn chốt 18/9/2026. Mẫu thật đã ban hành có bản 0, bản 2 dòng trống nên qa_all chỉ WARN,
    nhưng bản script dựng ra thì luôn đúng một dòng.
    """
    pt = _phan_tu_than(doc)
    for i, (k, el) in enumerate(pt):
        if k != "t":
            continue
        chu = nfc(" ".join(c.text for r in el.rows for c in r.cells))
        if "Nơi nhận" not in chu and "GIÁM ĐỐC" not in chu.upper():
            continue
        j, trong = i - 1, []
        while j >= 0 and _trong(pt[j]):
            trong.append(pt[j][1])
            j -= 1
        if not trong:
            el._tbl.addprevious(_p_moi_tu_khuon(khuon, "", cang_giua=False)._p)
        else:
            for p_thua in trong[1:]:          # giữ lại đúng một dòng trống
                p_thua._p.getparent().remove(p_thua._p)
        return


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Biên dịch nội dung dạng thẻ sang .docx trên mẫu thật.",
        formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument("noi_dung", help="file .txt nội dung có thẻ")
    ap.add_argument("ra", help="file .docx kết quả")
    ap.add_argument("--loai", choices=sorted(MAU_MAC_DINH), help="loại văn bản (chọn mẫu mặc định)")
    ap.add_argument("--mau", help="đường dẫn mẫu thật .docx (ưu tiên hơn --loai)")
    ap.add_argument("--than-tu", type=int, help="ép vị trí paragraph thân đầu tiên")
    ap.add_argument("--khong-qa", action="store_true", help="không chạy qa_rules sau khi dựng")
    a = ap.parse_args()

    if a.mau:
        mau = Path(a.mau)
    elif a.loai:
        mau = MAU_MAC_DINH[a.loai]
    else:
        print("LỖI: phải cho biết --loai hoặc --mau.", file=sys.stderr)
        return 2
    if not mau.exists():
        print(f"LỖI: không có mẫu {mau}", file=sys.stderr)
        return 2

    rows = doc_noi_dung(Path(a.noi_dung))
    doc = Document(str(mau))
    # Dòng [K] KHÔNG đi vào thân: khối Kính gửi có thể là paragraph hay bảng, dựng riêng ở cuối
    # để giữ đúng thể thức và các dòng trống ngăn cách (Bạn chốt 18/9/2026).
    dong_kg = next((t for t, k in rows if k == "k"), None)
    rows = [(t, k) for t, k in rows if k != "k"]
    if not rows:
        print("LỖI: nội dung chỉ có dòng [K], không có đoạn thân nào.", file=sys.stderr)
        return 2
    dau, cuoi = do_than(doc, co_kinh_gui=False)
    # Dòng trống ngăn giữa khối Kính gửi và thân là một phần thể thức — không ghi thân lên nó.
    ps_dd = doc.paragraphs
    while dau < cuoi and not nfc(ps_dd[dau].text).strip():
        dau += 1
    if a.than_tu is not None:
        dau = a.than_tu
    co_cho = cuoi - dau + 1
    if co_cho < 1:
        print(f"LỖI: không dò được thân văn bản trong {mau.name} "
              f"(dau={dau}, cuoi={cuoi}) — dùng --than-tu để chỉ định.", file=sys.stderr)
        return 2

    ps = doc.paragraphs
    mau_than = ps[dau]
    lui = lui_pho_bien(doc)

    # Đủ chỗ thì dùng lại paragraph có sẵn; thiếu thì nhân bản paragraph thân làm khuôn.
    from copy import deepcopy
    from docx.text.paragraph import Paragraph
    dich: list = []
    for i in range(len(rows)):
        if dau + i <= cuoi:
            dich.append(ps[dau + i])
        else:
            el = deepcopy(mau_than._p)
            dich[-1]._p.addnext(el)
            dich.append(Paragraph(el, mau_than._parent))
    # Thừa paragraph cũ thì xóa sạch, không để tồn dư vụ việc cũ (Nhóm G, H10).
    for i in range(dau + len(rows), cuoi + 1):
        ps[i]._p.getparent().remove(ps[i]._p)

    for (text, kieu), p in zip(rows, dich):
        viet(p, text, dam=(kieu == "h"), nghieng=(kieu == "i"))
        if kieu == "k":
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.first_line_indent = None
        else:
            if kieu == "p":
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            if lui is not None:
                p.paragraph_format.first_line_indent = Cm(lui)

    if dong_kg:
        dat_kinh_gui(doc, dong_kg, khuon=dich[0])
    cach_mot_dong_truoc_khoi_ky(doc, khuon=dich[0])

    ra = Path(a.ra)
    ra.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(ra))
    print(f"Đã dựng {ra}  ({len(rows)} đoạn thân, mẫu: {mau.name}, "
          f"lùi đầu dòng {lui if lui is not None else '—'} cm)")

    if a.khong_qa:
        return 0
    sys.path.insert(0, str(SCRIPT_DIR))
    from qa_rules import chay, FAIL  # noqa: E402
    ds = chay(ra)
    n_fail = sum(1 for x in ds if x.level == FAIL)
    print(f"\n── qa_rules: {n_fail} FAIL, {len(ds) - n_fail} WARN ──")
    for x in sorted(ds, key=lambda x: x.level != FAIL)[:15]:
        print("  " + x.line())
    print("\n→ Còn phải chạy `qa_all.py` để soi ảnh render trước khi giao.")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
