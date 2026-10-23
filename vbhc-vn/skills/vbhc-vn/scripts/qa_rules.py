#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""qa_rules.py — Bộ quy tắc soạn thảo VBHC được kiểm BẰNG MÁY (vbhc-vn 2.31.0).

Mỗi quy tắc là một hàm `rule_Rnn(doc, ctx)` trả về danh sách `Finding`.
Docstring của mỗi hàm ghi: mã quy tắc, nội dung quy tắc, nguồn, mức FAIL/WARN.

Nguyên tắc (Bạn chốt 16/9/2026):
  - Mẫu thật trong examples/ là CHUẨN: quy tắc nào làm mẫu thật FAIL thì quy tắc sai,
    sửa quy tắc, không sửa mẫu.
  - Không có lỗi im lặng: file bất thường phải báo rõ (mã LOI-DOC), không bỏ qua.
  - Quy tắc máy không kiểm được (nội dung pháp lý, suy diễn nhiệm vụ, giọng văn tổng thể)
    KHÔNG ép thành regex — xem loại N trong tests/rule-inventory.md.

Cách chạy:
    python3 scripts/qa_rules.py file.docx              # chạy toàn bộ
    python3 scripts/qa_rules.py file.docx --only R03   # chạy một quy tắc
    python3 scripts/qa_rules.py file.docx --final      # nâng WARN nhóm hoàn thiện thành FAIL
    python3 scripts/qa_rules.py file.docx --json       # xuất JSON cho máy đọc

Exit code: 0 = không có FAIL, 1 = có FAIL, 2 = lỗi sử dụng/đọc file.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
import zipfile
from dataclasses import dataclass, asdict
from pathlib import Path

try:
    from docx import Document
    from docx.oxml.ns import qn
except ImportError:  # pragma: no cover
    print("LỖI: thiếu python-docx. Cài: pip install python-docx", file=sys.stderr)
    raise

SCRIPT_DIR = Path(__file__).resolve().parent
PLUGIN_DIR = SCRIPT_DIR.parent
DATA_DIR = PLUGIN_DIR / "data"

FAIL = "FAIL"
WARN = "WARN"

# Các mã thuộc "nhóm hoàn thiện": WARN khi soạn dở, FAIL khi Bạn yêu cầu bản xuất bản.
NHOM_HOAN_THIEN = {"R03", "R19", "R20", "R21"}

MAX_EXCERPT = 80


@dataclass
class Finding:
    code: str
    level: str
    loc: str
    excerpt: str
    hint: str

    def line(self) -> str:
        return f"[{self.level} {self.code}] {self.loc}: {self.excerpt}\n      → {self.hint}"


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s or "")


def cut(s: str, n: int = MAX_EXCERPT) -> str:
    s = re.sub(r"\s+", " ", nfc(s)).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


# ────────────────────────── Ngữ cảnh văn bản ──────────────────────────

class Ctx:
    """Ngữ cảnh một file .docx: đoạn văn phẳng hóa, XML thô, loại văn bản đoán được."""

    def __init__(self, path: Path, final: bool = False):
        self.path = Path(path)
        self.final = final
        self.errors: list[str] = []
        with zipfile.ZipFile(self.path) as z:
            names = set(z.namelist())
            self.xml = z.read("word/document.xml").decode("utf-8", "replace")
            self.comments_xml = (
                z.read("word/comments.xml").decode("utf-8", "replace")
                if "word/comments.xml" in names else ""
            )

    def build(self, doc) -> None:
        """Phẳng hóa mọi paragraph (thân + ô bảng) theo thứ tự đọc, kèm định vị."""
        self.items: list[tuple[str, object]] = []
        for i, p in enumerate(doc.paragraphs):
            self.items.append((f"đoạn {i}", p))
        for ti, t in enumerate(doc.tables):
            for ri, row in enumerate(t.rows):
                for ci, cell in enumerate(row.cells):
                    for pi, p in enumerate(cell.paragraphs):
                        self.items.append((f"bảng {ti} ô [{ri},{ci}] đoạn {pi}", p))
        self.texts = [(loc, nfc(p.text)) for loc, p in self.items]
        self.full_text = "\n".join(t for _, t in self.texts)
        self.loai = self._doan_loai()

    # loại văn bản đoán từ tên file + 20 đoạn đầu (chỉ dùng để miễn trừ, không để kết luận)
    def _doan_loai(self) -> str:
        dau = nfc(" ".join(t for _, t in self.texts[:25])).upper()
        ten = nfc(self.path.stem).lower()
        bang = [
            ("phieu-trinh", "PHIẾU TRÌNH", "phieu-trinh"),
            ("bien-ban", "BIÊN BẢN", "bien-ban"),
            ("to-trinh", "TỜ TRÌNH", "to-trinh"),
            ("bao-cao", "BÁO CÁO", "bao-cao"),
            ("ke-hoach", "KẾ HOẠCH", "ke-hoach"),
            ("quyet-dinh", "QUYẾT ĐỊNH", "quyet-dinh"),
            ("giay-phep", "GIẤY PHÉP", "giay-phep"),
            ("giay-chung-nhan", "GIẤY CHỨNG NHẬN", "giay-chung-nhan"),
            ("giay-moi", "GIẤY MỜI", "giay-moi"),
            ("thong-bao", "THÔNG BÁO", "thong-bao"),
            ("phu-bieu", "PHỤ BIỂU", "phu-bieu"),
        ]
        for khoa_ten, khoa_dau, ma in bang:
            if khoa_ten in ten or khoa_dau in dau:
                return ma
        return "cong-van"


# ────────────────────────── Tiện ích XML / run ──────────────────────────

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def runs_of(p):
    return list(p.runs)


def is_italic(run) -> bool:
    return bool(run.italic) or bool(run.font.italic)


def is_bold(run) -> bool:
    """Đậm THẬT khi hiển thị: đặt trên run, hoặc run để trống (None) thì kế thừa kiểu ký tự /
    kiểu đoạn (vd Heading 1) theo chuỗi base_style. Run ghi rõ không đậm (<w:b w:val="0"/>)
    thì là không đậm. Vụ 22/9/2026: dòng 'KT. GIÁM ĐỐC' đậm qua kiểu Heading 1 bị R11 bắt nhầm."""
    if run.bold is not None:
        return bool(run.bold)
    st = getattr(run, "style", None)
    while st is not None and getattr(st, "name", "") not in ("Default Paragraph Font",):
        if st.font.bold is not None:
            return bool(st.font.bold)
        st = st.base_style
    par = getattr(run, "_parent", None)
    st = getattr(par, "style", None)
    while st is not None:
        if st.font.bold is not None:
            return bool(st.font.bold)
        st = st.base_style
    return False


def text_runs(p):
    """Các run CÓ CHỮ (bỏ run rỗng/chỉ khoảng trắng — chúng không mang định dạng nhìn thấy)."""
    return [r for r in p.runs if nfc(r.text).strip()]


def _tt(el) -> str:
    return nfc("".join(el.itertext()))


# ────────────────────────── Dữ liệu ngoài code ──────────────────────────

def _doc_list(ten_file: str) -> list[str]:
    """Đọc danh sách chuỗi từ data/<ten_file>; mỗi dòng 1 mục, '#' là ghi chú."""
    f = DATA_DIR / ten_file
    if not f.exists():
        return []
    out = []
    for ln in f.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if ln and not ln.startswith("#"):
            out.append(nfc(ln))
    return out


def _doc_vbpl() -> dict:
    """Kho dữ kiện văn bản pháp luật, khóa theo mã registry (vd 'NĐ 32/2024').

    File data/vbpl.json SINH TỰ ĐỘNG từ registry/trang-thai.csv bởi scripts/build_vbpl.py —
    không sửa tay. Thiếu file thì trả rỗng và R05 im lặng bỏ qua (không đoán).
    """
    f = DATA_DIR / "vbpl.json"
    if not f.exists():
        return {}
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ValueError(f"data/vbpl.json hỏng cấu trúc JSON: {e}") from e
    return {nfc(k): v for k, v in (data.get("van_ban") or {}).items()}


# Hậu tố số hiệu → loại văn bản, để quy một trích dẫn về mã của registry/trang-thai.csv.
# Định nghĩa đặt TRONG plugin để plugin chạy được cả khi cài độc lập, không có kho skill-sct;
# scripts/build_vbpl.py ở gốc kho nhập lại hàm này, không định nghĩa bản thứ hai.
HAU_TO_LOAI = [
    (re.compile(r"/QH\d+$|/UBTVQH\d+$"), "Luật"),
    (re.compile(r"/NĐ-CP$"), "NĐ"),
    (re.compile(r"/NQ-"), "NQ"),
    (re.compile(r"/TT-"), "TT"),
    (re.compile(r"/QĐ-"), "QĐ"),
    (re.compile(r"/QCVN"), "QCVN"),
    (re.compile(r"/VBHN-"), "VBHN"),
    (re.compile(r"-KL/"), "KL"),
]


def ma_tu_so_hieu(so: str) -> str | None:
    """Quy số hiệu trong văn bản về mã registry: '32/2024/NĐ-CP' → 'NĐ 32/2024'.

    Không nhận dạng được loại thì trả None — phía gọi phải BỎ QUA, không được đoán.
    """
    s_ = nfc(so).upper()
    loai = next((l for rx, l in HAU_TO_LOAI if rx.search(s_)), None)
    if loai is None:
        return None
    phan = so.split("/")
    if loai == "Luật":
        goc = "/".join(phan[:2])
    elif loai in ("NĐ", "TT") and len(phan) >= 3 and re.fullmatch(r"\d{2,4}", phan[1]):
        goc = "/".join(phan[:2])
    else:
        goc = so
    return f"{loai} {goc}"


def _ma_registry(so: str) -> str | None:
    return ma_tu_so_hieu(so)


# ────────────────────────── Các quy tắc ──────────────────────────

SO_VB = re.compile(
    # số hiệu có thể có phần thập phân (NQ 66.25/2026/NQ-CP) hoặc chữ cái (12a/2026/QĐ-UBND)
    r"số\s+(\d{1,5}(?:\.\d{1,3})?[a-zA-Z]?/\d{2,4}/[A-ZĐ][A-ZĐ0-9\-]{1,13}"
    r"|\d{1,5}(?:\.\d{1,3})?[a-zA-Z]?/[A-ZĐ][A-ZĐa-z0-9\-]{1,14})",
    re.IGNORECASE,
)
NGAY = re.compile(r"ngày\s+\d{1,2}\s*(?:tháng\s*\d{1,2}\s*năm\s*\d{4}|/\d{1,2}/\d{4})|\d{1,2}/\d{1,2}/\d{4}")


CAN_CU = re.compile(r"^\s*(Căn\s+cứ|Thực\s+hiện|Triển\s+khai|Theo\s+đề\s+nghị|Xét\s+đề\s+nghị)\b",
                    re.IGNORECASE)
HET_MO_DAU = re.compile(r"^\s*([IVX]+\.|\d+\.\s|PHẦN\b|Điều\s+\d)")


# Luật, Bộ luật, Nghị quyết Quốc hội dẫn theo số/năm, KHÔNG kèm ngày — thể thức chuẩn
# (mẫu thật to-trinh-vbqppl-tien-chat-thuoc-no.docx: "Luật … số 42/2024/QH15").
LUAT_QH = re.compile(r"/(QH\d+|UBTVQH\d+)$")


def _vung_can_cu(ctx) -> set[str]:
    """Các đoạn thuộc VÙNG CĂN CỨ: mở đầu "Căn cứ/Thực hiện…" hoặc đoạn mở đầu công văn,
    tính đến đề mục đầu tiên (I., 1., Điều 1). Ngoài vùng này là thân văn bản."""
    vung: set[str] = set()
    for loc, t in ctx.texts:
        if not loc.startswith("đoạn"):
            continue
        s_ = t.strip()
        if not s_:
            continue
        if HET_MO_DAU.match(s_):
            break
        vung.add(loc)
    for loc, t in ctx.texts:
        if CAN_CU.match(t.strip()):
            vung.add(loc)
    return vung


def rule_R01(doc, ctx) -> list[Finding]:
    """R01 — Dẫn văn bản lần đầu phải đầy đủ.

    Quy tắc: lần XUẤT HIỆN ĐẦU TIÊN của mỗi số hiệu văn bản (vd "số 32/2024/NĐ-CP")
    phải nằm trong đoạn có NGÀY BAN HÀNH; các lần sau mới được viết gọn.
    Nguồn: Quy tắc Giám đốc chốt 13/9/2026; Nhóm A (phong-tranh-sai-lam.md).
    Mức: FAIL trong VÙNG CĂN CỨ (đoạn mở đầu, dòng "Căn cứ…/Thực hiện…") — đây là chỗ
    viện dẫn có giá trị pháp lý; WARN ở thân văn bản.

    Miễn trừ: Luật, Bộ luật, Nghị quyết Quốc hội (số hiệu kết thúc /QHnn, /UBTVQHnn) —
    thể thức chuẩn dẫn theo số/năm, không kèm ngày ban hành.

    Hiệu chỉnh 16/9/2026: bản FAIL-toàn-văn bắt 32 lỗi trên 26 mẫu thật đã ban hành
    (báo cáo tháng liệt kê nhiệm vụ viết gọn "Chỉ thị số 20/CT-BCT về tăng cường…").
    Theo nguyên tắc "mẫu thật là chuẩn", quy tắc thu hẹp về vùng căn cứ.
    """
    vung = _vung_can_cu(ctx)
    out: list[Finding] = []
    da_gap: set[str] = set()
    for loc, t in ctx.texts:
        if not t.strip():
            continue
        co_ngay = bool(NGAY.search(t))
        bao_trong_doan: set[str] = set()
        for m in SO_VB.finditer(t):
            so = m.group(1)
            khoa = so.upper()
            if khoa in da_gap:
                continue
            da_gap.add(khoa)
            if co_ngay or khoa in bao_trong_doan or LUAT_QH.search(khoa):
                continue
            bao_trong_doan.add(khoa)
            muc = FAIL if loc in vung else WARN
            out.append(Finding(
                "R01", muc, loc, cut(t),
                f"Lần đầu dẫn '{so}' phải đủ: số, ngày ban hành, cơ quan ban hành, "
                f"trích yếu, và '(sau đây viết tắt là …)' nếu còn dẫn lại.",
            ))
    return out


CHEM = re.compile(
    r"(?<![A-Za-z0-9])("
    r"P2O5|H2SO4|H3PO4|H2O2|HNO3|NH3|NH4|CO2|SO2|SO3|NO2|N2O|CH4|H2O|H2S|"
    r"CaCO3|CaO|Al2O3|Fe2O3|Fe3O4|SiO2|AlF3|NaOH|KOH|Na2CO3|NaCl|CaSO4|MgO|CuSO4|ZnO|TiO2"
    r")(?![A-Za-z0-9])"
)


def rule_R02(doc, ctx) -> list[Finding]:
    """R02 — Công thức hóa học phải có chỉ số dưới THẬT.

    Quy tắc: P₂O₅, H₂SO₄, CO₂… viết chữ số bằng run `vertAlign=subscript`,
    không để nguyên chuỗi phẳng "P2O5". Nguồn: Quy tắc bất biến 25 (Bạn chốt 13/9/2026).
    Mức: FAIL.

    Cách kiểm: ghép text các run KHÔNG subscript của từng paragraph — công thức viết đúng
    (chữ số nằm ở run subscript) sẽ không còn nguyên chuỗi, nên không bị bắt.
    """
    out: list[Finding] = []
    for loc, p in ctx.items:
        phang = "".join(
            r.text for r in p.runs
            if (r.font.subscript is not True)
        )
        for m in CHEM.finditer(nfc(phang)):
            out.append(Finding(
                "R02", FAIL, loc, cut(p.text),
                f"'{m.group(1)}' đang là chữ phẳng — tách run và đặt "
                f"font.subscript=True cho chữ số (không dùng ký tự Unicode ₂₅).",
            ))
    return out


TRONG = [
    (re.compile(r"…{2,}"), "dấu … lặp"),
    (re.compile(r"\.{4,}"), "dấu . lặp"),
    (re.compile(r"\[\s*\]"), "ngoặc vuông rỗng"),
    (re.compile(r"…\s*/\s*…"), "…/…"),
    (re.compile(r"\(\s*nêu\s+số\s+liệu\s*\)", re.IGNORECASE), "(nêu số liệu)"),
    (re.compile(r"\(\s*bổ\s+sung\s+sau\s*\)", re.IGNORECASE), "(bổ sung sau)"),
    (re.compile(r"\bXX+\b"), "XX giữ chỗ"),
]
# Dòng ngày ban hành và dòng "Số: …" ĐƯỢC PHÉP để trống — Nhóm G và Quy tắc 27(c).
MIEN_TRU_TRONG = re.compile(
    r"^\s*(Số\s*:|.{0,25},\s*ngày\b)|ngày\s+…*\s*tháng|ngày\s{2,}tháng", re.IGNORECASE
)
TIM = "7030A0"


def rule_R03(doc, ctx) -> list[Finding]:
    """R03 — Bản hoàn thiện không còn chỗ trống.

    Quy tắc: bản Bạn yêu cầu "hoàn thiện để xuất bản" không được còn "……", "....",
    "[ ]", "…/…", "(nêu số liệu)" và CHỮ MÀU TÍM 7030A0 (cơ chế đánh dấu nội dung
    chưa hoàn thiện — phải liệt kê đủ vị trí). Ngoại lệ: dòng "Số: …" và dòng
    địa danh/ngày tháng góc phải được để trống cho văn thư điền khi ký.
    Nguồn: Quy tắc bất biến 27(c) (Bạn chốt 16/9/2026); Nhóm G.
    Mức: WARN — thành FAIL khi chạy --final.
    """
    muc = FAIL if ctx.final else WARN
    out: list[Finding] = []
    for loc, t in ctx.texts:
        if not t.strip() or MIEN_TRU_TRONG.search(t):
            continue
        for rx, ten in TRONG:
            if rx.search(t):
                out.append(Finding(
                    "R03", muc, loc, cut(t),
                    f"Còn chỗ trống ({ten}) — bản xuất bản phải viết thành câu hoàn chỉnh "
                    f"hoặc nêu định tính, không để dấu giữ chỗ.",
                ))
                break
    # chữ tím: liệt kê ĐỦ vị trí, không gộp
    for loc, p in ctx.items:
        for r in p.runs:
            col = r.font.color
            rgb = getattr(col, "rgb", None) if col is not None else None
            if rgb is not None and str(rgb).upper() == TIM:
                out.append(Finding(
                    "R03", muc, loc, cut(r.text or p.text),
                    "Chữ tím 7030A0 = nội dung Bạn đánh dấu chưa hoàn thiện — "
                    "phải chốt nội dung và trả về màu đen trước khi trình ký.",
                ))
    return out


def _o_ke_ben(doc, loc: str):
    """Trả về các paragraph của ô liền phải trong cùng hàng (cho bố cục Kính gửi dạng bảng)."""
    m = re.match(r"bảng (\d+) ô \[(\d+),(\d+)\]", loc)
    if not m:
        return []
    ti, ri, ci = (int(x) for x in m.groups())
    try:
        row = doc.tables[ti].rows[ri]
    except IndexError:
        return []
    out = []
    for cell in list(row.cells)[ci + 1:]:
        out.extend(cell.paragraphs)
    return out


def _lui(p) -> tuple:
    pf = p.paragraph_format
    return (
        round(pf.left_indent.cm, 2) if pf.left_indent is not None else None,
        round(pf.first_line_indent.cm, 2) if pf.first_line_indent is not None else None,
    )


def _lui_hieu_dung(p) -> float:
    """Mép trái NHÌN THẤY của một dòng = thụt lề + khoảng trắng dẫn đầu (ước 0,20 cm/ký tự
    ở cỡ 13-14pt). Mẫu thật cong-van-ubnd-tinh-chi-dao.docx căn khối Kính gửi bằng dấu
    cách chứ không bằng indent, nên chỉ so indent là bắt nhầm."""
    pf = p.paragraph_format
    left = pf.left_indent.cm if pf.left_indent is not None else 0.0
    dem = len(nfc(p.text)) - len(nfc(p.text).lstrip(" \t"))
    return round(left + dem * 0.20, 2)


def rule_R04(doc, ctx) -> list[Finding]:
    """R04 — Khối Kính gửi nhiều cơ quan.

    Quy tắc: khi "Kính gửi:" đứng RIÊNG một dòng, các dòng cơ quan phía dưới phải
    THẲNG CỘT với nhau (cùng thụt lề); dòng "Kính gửi:" không in đậm.
    Nguồn: Nhóm G; Quy tắc bất biến 27(a) (Bạn chốt 16/9/2026).
    Mức: FAIL cho phần in đậm; WARN cho phần thẳng cột.

    Miễn trừ: Phiếu trình giải quyết công việc (mẫu thật in đậm "Kính gửi:" có chủ đích).
    Hiệu chỉnh 16/9/2026: mẫu thật cong-van-ubnd-tinh-chi-dao.docx căn khối Kính gửi bằng
    khoảng trắng dẫn đầu (16-17 dấu cách) chứ không bằng indent — so indent cứng làm mẫu
    thật FAIL, nên phần thẳng cột hạ xuống WARN với dung sai 0,35 cm.
    """
    out: list[Finding] = []
    for idx, (loc, p) in enumerate(ctx.items):
        t = nfc(p.text).strip()
        if not re.match(r"^Kính\s+gửi\s*:", t):
            continue
        if ctx.loai != "phieu-trinh" and all(is_bold(r) for r in text_runs(p)) and text_runs(p):
            out.append(Finding(
                "R04", FAIL, loc, cut(t),
                "Dòng 'Kính gửi:' không in đậm (NĐ 30/2020 — chỉ tên loại và trích yếu đậm).",
            ))
        if re.match(r"^Kính\s+gửi\s*:\s*\S", t):
            continue  # gửi 1 nơi, viết cùng dòng — không thuộc phạm vi quy tắc này
        # "Kính gửi:" đứng riêng → gom các dòng cơ quan
        ds = _o_ke_ben(doc, loc)
        if not ds:
            ds = [q for _, q in ctx.items[idx + 1: idx + 12]]
        cq = []
        for q in ds:
            tq = nfc(q.text).strip()
            if not tq:
                if cq:
                    break
                continue
            if not re.match(r"^[-–•]?\s*[A-ZĐÀ-Ỹ]", tq) or len(tq) > 160:
                break
            cq.append(q)
            if tq.endswith("."):
                break
        if len(cq) < 2:
            continue
        for q in cq:
            tr = text_runs(q)
            if tr and all(is_bold(r) for r in tr):
                out.append(Finding(
                    "R04", FAIL, loc, cut(q.text),
                    "Dòng tên cơ quan trong khối Kính gửi không in đậm.",
                ))
        muc_lui = {_lui_hieu_dung(q) for q in cq}
        if len(muc_lui) > 1 and (max(muc_lui) - min(muc_lui)) > 0.35:
            out.append(Finding(
                "R04", WARN, loc, cut(" / ".join(nfc(q.text).strip() for q in cq[:3])),
                f"{len(cq)} dòng cơ quan dưới 'Kính gửi:' lệch cột "
                f"({min(muc_lui):.2f}–{max(muc_lui):.2f} cm) — đặt cùng left/hanging indent.",
            ))
    return out


def rule_R05(doc, ctx) -> list[Finding]:
    """R05 — Không viện dẫn văn bản chưa có hiệu lực tại ngày ký.

    Quy tắc: đọc ngày ở dòng địa danh/ngày tháng; với mỗi văn bản được viện dẫn,
    nếu tra được ngày hiệu lực trong data/vbpl.json mà ngày hiệu lực SAU ngày ký
    thì FAIL. KHÔNG có dữ liệu thì bỏ qua, không báo (không đoán).
    Kho sinh từ registry/trang-thai.csv — lớp trạng thái người duy trì ghi sau khi đối chiếu
    bản gốc; bổ sung văn bản thì sửa CSV đó rồi chạy `python3 scripts/build_vbpl.py`.
    Nguồn: Nhóm A, Nhóm D (vụ NQ 66.25/2026 ngày 11/9/2026).
    Mức: FAIL.
    """
    kho = _doc_vbpl()
    if not kho:
        return []
    ngay_ky = None
    for _, t in ctx.texts[:40]:
        m = re.search(r",\s*ngày\s+(\d{1,2})\s*tháng\s*(\d{1,2})\s*năm\s*(\d{4})", t)
        if m:
            d, mo, y = (int(x) for x in m.groups())
            ngay_ky = (y, mo, d)
            break
    if ngay_ky is None:
        return []
    out: list[Finding] = []
    da_bao: set[str] = set()
    for loc, t in ctx.texts:
        for m in SO_VB.finditer(t):
            so = m.group(1)
            ma = _ma_registry(so)
            if ma is None or ma in da_bao:
                continue
            ghi = kho.get(nfc(ma))
            if not ghi or not ghi.get("ngay_hieu_luc"):
                continue
            try:
                y, mo, d = (int(x) for x in ghi["ngay_hieu_luc"].split("-"))
            except (ValueError, AttributeError):
                raise ValueError(
                    f"data/vbpl.json: '{ma}' có ngay_hieu_luc sai định dạng YYYY-MM-DD"
                )
            if (y, mo, d) > ngay_ky:
                da_bao.add(ma)
                out.append(Finding(
                    "R05", FAIL, loc, cut(t),
                    f"'{so}' ({ma}) hiệu lực {ghi['ngay_hieu_luc']}, SAU ngày ký văn bản "
                    f"({ngay_ky[2]:02d}/{ngay_ky[1]:02d}/{ngay_ky[0]}) — bỏ khỏi văn bản trình ký.",
                ))
    return out


DN = re.compile(
    r"(Công\s?ty|Doanh\s+nghiệp|Hợp\s+tác\s+xã|HTX|Hộ\s+kinh\s+doanh|Chi\s+nhánh|Tập\s+đoàn|Tổng\s+công\s?ty)",
    re.IGNORECASE,
)


def _khoi_noi_nhan(ctx) -> list[tuple[str, str]]:
    khoi: list[tuple[str, str]] = []
    bat = False
    for loc, t in ctx.texts:
        s = t.strip()
        if re.match(r"^Nơi\s+nhận\s*:", s):
            bat = True
            continue
        if not bat:
            continue
        if not s:
            if khoi:
                break
            continue
        khoi.append((loc, s))
        if re.match(r"^-?\s*Lưu\s*:", s):
            break
    return khoi


def rule_R06(doc, ctx) -> list[Finding]:
    """R06 — Thứ tự Nơi nhận khi văn bản gửi doanh nghiệp.

    Quy tắc: doanh nghiệp/tổ chức được cấp phép KHÔNG đứng dòng đầu của Nơi nhận
    (xếp gần cuối, ngay trên dòng Lưu); dòng cuối cùng của khối là dòng "Lưu:".
    Nguồn: Nhóm G, Bạn chốt 07/9/2026 (áp dụng vĩnh viễn cho Giấy phép, Quyết định,
    Công văn cấp cho/gửi doanh nghiệp).
    Mức: FAIL.
    """
    khoi = _khoi_noi_nhan(ctx)
    if not khoi:
        return []
    out: list[Finding] = []
    loc0, dong0 = khoi[0]
    if DN.search(dong0) and not re.match(r"^-?\s*Như\s+trên", dong0, re.IGNORECASE):
        out.append(Finding(
            "R06", FAIL, loc0, cut(dong0),
            "Doanh nghiệp không được đứng dòng đầu Nơi nhận — thứ tự chuẩn: UBND tỉnh (b/c); "
            "cơ quan phối hợp; Ban Giám đốc Sở (trừ văn bản thủ tục hành chính — R22); doanh nghiệp; Lưu.",
        ))
    loc_c, dong_c = khoi[-1]
    if not re.match(r"^-?\s*Lưu\s*:", dong_c):
        out.append(Finding(
            "R06", FAIL, loc_c, cut(dong_c),
            "Dòng cuối khối Nơi nhận phải là dòng 'Lưu: …'.",
        ))
    return out


KY_HIEU_HOP_LE = re.compile(
    r"^-?\s*Lưu\s*:\s*[A-ZĐ0-9]", re.IGNORECASE
)


def rule_R07(doc, ctx) -> list[Finding]:
    """R07 — Dòng Lưu đúng dạng.

    Quy tắc: dòng Lưu chỉ ghi ký hiệu đơn vị lưu, KHÔNG ghi tên chuyên viên soạn thảo,
    kết thúc bằng dấu chấm — "Lưu: VT, CN."; công văn nội bộ Phòng "Lưu: CN."; phòng QLCN
    dùng ký hiệu **CN**, không "QLCN".
    Nguồn: Nhóm G; Bạn chốt 01/10/2026 bỏ tên chuyên viên ở cuối văn bản (thay quy ước cũ
    "CN (Tên)").
    Mức: FAIL cho phần cấu trúc; WARN khi còn tên trong ngoặc — vì mẫu thật đã ban hành
    trước 01/10/2026 vẫn có "CN(Trung)", không được bắt mẫu thật FAIL. build_vb.py và
    TemplateDoc.save() tự bỏ tên (fill_template.chuan_hoa_dong_luu) nên bản dựng mới luôn sạch.
    """
    out: list[Finding] = []
    for loc, t in ctx.texts:
        s = t.strip()
        if not re.match(r"^-?\s*Lưu\s*:", s):
            continue
        if not KY_HIEU_HOP_LE.match(s):
            out.append(Finding(
                "R07", FAIL, loc, cut(s),
                "Sau 'Lưu:' phải là ký hiệu đơn vị lưu (VT, CN, KT, TH…).",
            ))
            continue
        if not s.rstrip().endswith("."):
            out.append(Finding(
                "R07", FAIL, loc, cut(s),
                "Dòng Lưu kết thúc bằng dấu chấm.",
            ))
        if re.search(r"\bQLCN\s*[(,.]", s):
            out.append(Finding(
                "R07", FAIL, loc, cut(s),
                "Trong dòng Lưu dùng ký hiệu 'CN', không dùng 'QLCN'.",
            ))
        if re.search(r"\b(?:Q?LCN|CN)\s?\([^)]*\)", s):
            out.append(Finding(
                "R07", WARN, loc, cut(s),
                "Từ 01/10/2026 không ghi tên chuyên viên ở dòng Lưu — ghi 'Lưu: VT, CN.' "
                "(nội bộ Phòng: 'Lưu: CN.').",
            ))
    return out


def rule_R08(doc, ctx) -> list[Finding]:
    """R08 — Từ suy đoán trong văn bản trình ký.

    Quy tắc: cấm "dự kiến" (ngoài tiến độ kế hoạch), "gần như", "có vẻ", "có lẽ",
    "khả năng cao", "theo tôi"… Nguồn: Nhóm C.
    Mức: WARN (giữ đúng mức của check_document.py, tránh báo trùng hai đường).

    TÁI DÙNG: gọi thẳng `check_document.find_speculative` — không viết lại danh sách.
    """
    try:
        sys.path.insert(0, str(SCRIPT_DIR))
        from check_document import find_speculative  # type: ignore
    except ImportError as e:
        raise RuntimeError(f"R08 không nạp được check_document.py: {e}") from e
    out: list[Finding] = []
    for so_dong, tu, dong in find_speculative(ctx.full_text):
        out.append(Finding(
            "R08", WARN, f"dòng {so_dong}", cut(dong),
            f"Từ suy đoán '{tu}' — thay bằng cấu trúc "
            f"'Căn cứ [số liệu/quy định], [nhận định]; đề nghị … xem xét, quyết định.'",
        ))
    return out


def rule_R09(doc, ctx) -> list[Finding]:
    """R09 — Thuật ngữ sai theo danh sách cấm.

    Quy tắc: các cụm từ Bạn đã chốt là sai (vd "cụm tiểu thủ công nghiệp" khi đi cùng
    Sơn Mãn / Đông Phố Mới) không được xuất hiện. Danh sách để ở
    data/thuat-ngu-cam.txt — bổ sung KHÔNG phải sửa code.
    Định dạng mỗi dòng: `cụm cấm | cụm thay thế | điều kiện kèm (tùy chọn)`.
    Cụm nào còn tồn tại trong mẫu thật đã ban hành thì để ở data/thuat-ngu-canh-bao.txt
    (mức WARN) cho tới khi Bạn chốt sửa mẫu — không bắt mẫu thật FAIL.
    Nguồn: Nhóm K5; reference/phong-tranh-sai-lam.md.
    Mức: FAIL (thuat-ngu-cam.txt) / WARN (thuat-ngu-canh-bao.txt).
    """
    out: list[Finding] = []
    nguon = ([(FAIL, x) for x in _doc_list("thuat-ngu-cam.txt")]
             + [(WARN, x) for x in _doc_list("thuat-ngu-canh-bao.txt")])
    for muc, dong in nguon:
        phan = [x.strip() for x in dong.split("|")]
        cam = phan[0]
        thay = phan[1] if len(phan) > 1 and phan[1] else "(xem reference)"
        kem = phan[2] if len(phan) > 2 and phan[2] else ""
        if not cam:
            continue
        rx = re.compile(re.escape(cam), re.IGNORECASE)
        for loc, t in ctx.texts:
            if not rx.search(t):
                continue
            if kem and not re.search(re.escape(kem), ctx.full_text, re.IGNORECASE):
                continue
            out.append(Finding(
                "R09", muc, loc, cut(t),
                f"'{cam}' là thuật ngữ sai — viết '{thay}'.",
            ))
    return out


def rule_R10(doc, ctx) -> list[Finding]:
    """R10 — Giọng giải thích lọt vào thân văn bản (Nhóm J).

    Quy tắc: mỗi câu trong thân VBHC phải nêu quy định, nêu yêu cầu hoặc nêu sự việc.
    Câu đánh giá mức độ, so sánh dễ - khó, dẫn dắt tâm lý hoặc giải thích "vì sao tôi
    viết như vậy" thuộc phần trao đổi với Bạn, không thuộc văn bản.
    Danh sách cụm lấy ĐÚNG từ Nhóm J trong reference (data/giong-giai-thich.txt) —
    không tự thêm.
    Nguồn: Nhóm J (Bạn chốt 31/8/2026, vụ công văn hướng dẫn kho VLNCN).
    Mức: WARN (máy dễ bắt nhầm ngữ cảnh hợp lệ J5).
    """
    out: list[Finding] = []
    for cum in _doc_list("giong-giai-thich.txt"):
        rx = re.compile(re.escape(cum), re.IGNORECASE)
        for loc, t in ctx.texts:
            if rx.search(t):
                out.append(Finding(
                    "R10", WARN, loc, cut(t),
                    f"Cụm '{cum}' thuộc giọng giải thích (Nhóm J) — viết lại thành câu "
                    f"nêu quy định/yêu cầu/sự việc, hoặc bỏ hẳn.",
                ))
    return out


DIA_DANH = re.compile(r"^[A-ZĐÀ-Ỹ][^,]{1,24},\s*ngày\b")


def rule_R11(doc, ctx) -> list[Finding]:
    """R11 — Dòng địa danh/ngày tháng in nghiêng; khối chức danh - người ký.

    Quy tắc: dòng "Lào Cai, ngày … tháng … năm …" IN NGHIÊNG; dòng chức danh
    (KT. GIÁM ĐỐC / PHÓ GIÁM ĐỐC / TRƯỞNG PHÒNG…) VIẾT HOA, IN ĐẬM, CĂN GIỮA.
    Nguồn: Quy tắc thể thức đã chốt (NĐ 30/2020 Phụ lục I); Nhóm H2.
    Mức: FAIL.

    Phạm vi hẹp có chủ đích: chỉ xét dòng địa danh trong 30 đoạn đầu (khối header) —
    trong thân biên bản có câu "…, ngày…" là văn xuôi bình thường, không phải thể thức.
    KHÔNG kiểm "không đậm" vì mẫu thật bao-cao-ket-qua-thang-atvsld.docx để đậm+nghiêng.
    """
    out: list[Finding] = []
    for loc, p in ctx.items[:30]:
        t = nfc(p.text).strip()
        if not DIA_DANH.match(t) or "tháng" not in t:
            continue
        tr = text_runs(p)
        if tr and not any(is_italic(r) for r in tr):
            out.append(Finding(
                "R11", FAIL, loc, cut(t),
                "Dòng địa danh, ngày tháng năm phải in nghiêng (13pt, <w:i/> trên run).",
            ))
        break
    for loc, p in ctx.items:
        t = nfc(p.text).strip()
        if not re.match(r"^(KT\.|TM\.|TL\.|Q\.)?\s*"
                        r"(GIÁM ĐỐC|PHÓ GIÁM ĐỐC|CHỦ TỊCH|PHÓ CHỦ TỊCH|TRƯỞNG PHÒNG|"
                        r"PHÓ TRƯỞNG PHÒNG|CHÁNH VĂN PHÒNG|KT\. CHÁNH VĂN PHÒNG|"
                        r"PHÓ CHÁNH VĂN PHÒNG|NGƯỜI BÁO CÁO)\s*$", t):
            continue
        tr = text_runs(p)
        if tr and not all(is_bold(r) for r in tr):
            out.append(Finding(
                "R11", FAIL, loc, cut(t),
                "Dòng chức danh người ký phải in đậm, viết hoa, căn giữa.",
            ))
    return out


LE_CHUAN = {"top": 2.0, "bottom": 2.0, "left": 3.0, "right": 2.0}
SAI_SO_LE = 0.05


def rule_R12(doc, ctx) -> list[Finding]:
    """R12 — Lề trang A4.

    Quy tắc của Sở: trên 2 cm, dưới 2 cm, trái 3 cm, phải 2 cm (NĐ 30/2020 Phụ lục I
    cho phép trên/dưới 20-25 mm, trái 30-35 mm, phải 15-20 mm).
    Mức: FAIL khi lề KHÔNG được đặt hoặc phi lý (<0,5 cm hoặc >5 cm — dấu hiệu file hỏng);
    WARN khi lệch chuẩn 2/2/3/2 quá 0,05 cm.

    Hiệu chỉnh 16/9/2026: 4/26 mẫu thật đã ban hành lệch chuẩn có chủ đích
    (giay-chung-nhan-attp-winmart 2,54 cm theo phôi GCN; ke-hoach-thuc-hien-de-an-08
    lề trên 1,50 cm; cong-van-noi-bo-phong lề dưới 1,75 cm; cong-van-vp-ubnd-truyen-dat
    lề dưới 0,75 cm). Mẫu thật là chuẩn, nên mức
    FAIL chỉ giữ cho trường hợp thiếu lề hoặc trị số phi lý.
    """
    out: list[Finding] = []
    for si, s_ in enumerate(doc.sections):
        thuc = {
            "top": s_.top_margin, "bottom": s_.bottom_margin,
            "left": s_.left_margin, "right": s_.right_margin,
        }
        for ten, chuan in LE_CHUAN.items():
            v = thuc[ten]
            if v is None:
                out.append(Finding(
                    "R12", FAIL, f"section {si}", f"lề {ten} không được đặt",
                    f"Đặt lề {ten} = {chuan} cm.",
                ))
                continue
            if v.cm < 0.5 or v.cm > 5.0:
                out.append(Finding(
                    "R12", FAIL, f"section {si}", f"lề {ten} = {v.cm:.2f} cm",
                    f"Trị số phi lý — lề {ten} phải là {chuan} cm.",
                ))
            elif abs(v.cm - chuan) > SAI_SO_LE:
                out.append(Finding(
                    "R12", WARN, f"section {si}", f"lề {ten} = {v.cm:.2f} cm",
                    f"Lệch chuẩn của Sở ({chuan} cm) — giữ nguyên nếu là phôi có sẵn "
                    f"(GCN, giấy phép), sửa nếu là văn bản soạn mới.",
                ))
    return out


def rule_R13(doc, ctx) -> list[Finding]:
    """R13 — Lùi đầu dòng đồng đều trong thân văn bản.

    Quy tắc: mọi đoạn thân, kể cả đề mục và gạch đầu dòng, lùi ĐỒNG ĐỀU
    (Bạn bác bản "lùi tiến không đều"). Máy kiểm bằng cách lấy trị firstLine
    phổ biến nhất của file rồi báo các đoạn lệch — KHÔNG áp một con số cứng,
    vì mẫu thật dùng cả 1,00 cm và 1,25 cm tùy văn bản.
    Nguồn: Quy tắc bất biến 27(b) (Bạn chốt 16/9/2026).
    Mức: WARN.
    """
    vals: dict[float, int] = {}
    than: list[tuple[str, object, float]] = []
    for loc, p in ctx.items:
        if not loc.startswith("đoạn"):
            continue  # ô bảng có quy ước căn lề riêng — Quy tắc 24
        t = nfc(p.text).strip()
        if len(t) < 30:
            continue
        # bỏ khối thể thức: tên loại, trích yếu, Kính gửi (căn giữa có chủ đích)
        if p.alignment is not None and int(p.alignment) == 1:
            continue
        if re.match(r"^(Kính\s+gửi|Nơi\s+nhận|-?\s*Lưu\s*:)", t):
            continue
        fi = p.paragraph_format.first_line_indent
        v = round(fi.cm, 2) if fi is not None else 0.0
        vals[v] = vals.get(v, 0) + 1
        than.append((loc, p, v))
    if len(than) < 5 or not vals:
        return []
    pho_bien = max(vals.items(), key=lambda kv: kv[1])[0]
    if vals[pho_bien] < 0.6 * len(than):
        return []  # file không có chuẩn rõ ràng — không đoán
    out: list[Finding] = []
    for loc, p, v in than:
        if abs(v - pho_bien) > 0.05:
            out.append(Finding(
                "R13", WARN, loc, cut(p.text),
                f"Lùi đầu dòng {v:.2f} cm trong khi phần lớn văn bản lùi {pho_bien:.2f} cm "
                f"— đặt lại cho đồng đều.",
            ))
    return out


VET_SUA = [
    (re.compile(r"bản\s+điều\s+chỉnh", re.IGNORECASE), "bản điều chỉnh"),
    (re.compile(r"sửa\s+lần\s*\d", re.IGNORECASE), "sửa lần N"),
    (re.compile(r"\bbản\s+sửa\s*(lần)?\s*\d", re.IGNORECASE), "bản sửa lần N"),
    (re.compile(r"\(đã\s+sửa\)", re.IGNORECASE), "(đã sửa)"),
    (re.compile(r"\bbản\s+nháp\b", re.IGNORECASE), "bản nháp"),
    (re.compile(r"\bv\d\s*\.docx", re.IGNORECASE), "tên file cũ vN.docx"),
]


def rule_R14(doc, ctx) -> list[Finding]:
    """R14 — Không để lại dấu vết lần chỉnh sửa trước.

    Quy tắc: trong thân văn bản không còn "bản điều chỉnh", "sửa lần N", "(đã sửa)",
    "bản nháp", tên file cũ; trong document.xml không còn comment (w:commentReference)
    hay tracked change (w:ins / w:del) sót lại.
    Nguồn: Nhóm F, Nhóm K7 (xóa màu đỏ cả ở rPr của paragraph mark).
    Mức: FAIL.
    """
    out: list[Finding] = []
    for loc, t in ctx.texts:
        for rx, ten in VET_SUA:
            if rx.search(t):
                out.append(Finding(
                    "R14", FAIL, loc, cut(t),
                    f"Còn dấu vết lần sửa trước ('{ten}') — xóa khỏi bản trình ký.",
                ))
                break
    n_cmt = ctx.xml.count("<w:commentReference")
    if n_cmt:
        out.append(Finding(
            "R14", FAIL, "document.xml", f"{n_cmt} comment còn trong file",
            "Xóa hết comment trước khi trình ký (Word: Review → Delete All Comments).",
        ))
    n_ins = len(re.findall(r"<w:(ins|del)\b", ctx.xml))
    if n_ins:
        out.append(Finding(
            "R14", FAIL, "document.xml", f"{n_ins} tracked change còn trong file",
            "Chấp nhận/từ chối hết tracked change (Word: Review → Accept All).",
        ))
    return out


QD = re.compile(r"Quyết\s+định\s+số\s+(\d{1,5}[a-zA-Z]?/\S+)", re.IGNORECASE)
VB_TRINH = re.compile(r"(Tờ\s+trình|Báo\s+cáo)\s+số\s+\d", re.IGNORECASE)


def rule_R15(doc, ctx) -> list[Finding]:
    """R15 — Dẫn Quyết định thì không nhắc các văn bản trình hình thành Quyết định đó.

    Quy tắc: khi văn bản đã dẫn một Quyết định, không nhắc lại Tờ trình/Báo cáo đã
    dùng để trình ban hành chính Quyết định ấy trong CÙNG một đoạn — Quyết định đã
    là kết quả cuối cùng.
    Nguồn: Nhóm K6 ("đúng không đồng nghĩa với cần ghi").
    Mức: WARN — máy dễ đoán sai quan hệ giữa hai văn bản.
    """
    out: list[Finding] = []
    for loc, t in ctx.texts:
        if QD.search(t) and VB_TRINH.search(t):
            out.append(Finding(
                "R15", WARN, loc, cut(t),
                "Đoạn dẫn cả Quyết định lẫn Tờ trình/Báo cáo trình ban hành Quyết định đó "
                "— kiểm lại, thường chỉ cần dẫn Quyết định.",
            ))
    return out


# ────────────────────────── Bảng đăng ký ──────────────────────────

def _con_lai_trong_bang(doc, loc: str) -> str:
    """Chữ ở mọi ô KHÁC của bảng chứa 'Kính gửi' (khi nơi nhận bị đặt xuống hàng dưới)."""
    m = re.match(r"bảng (\d+) ô \[(\d+),(\d+)\]", loc)
    if not m:
        return ""
    ti, ri, ci = (int(x) for x in m.groups())
    try:
        bang = doc.tables[ti]
    except IndexError:
        return ""
    ra = []
    for r_i, row in enumerate(bang.rows):
        for c_i, cell in enumerate(row.cells):
            if (r_i, c_i) == (ri, ci):
                continue
            t = nfc(cell.text).strip()
            if t and not re.match(r"^Kính\s+gửi", t):
                ra.append(t)
    return "\n".join(ra)


def _khoi_kinh_gui(doc, ctx) -> tuple[str, str, list[str]] | None:
    """Trả (vị trí, phần chữ NẰM CÙNG dòng/ô với 'Kính gửi', danh sách nơi nhận của cả khối).

    Mẫu thật của Sở có ba cách trình bày khối này, cùng phải nhận ra được:
      - một paragraph 'Kính gửi: <một cơ quan>.'                      (một nơi nhận)
      - bảng 2 ô: ô trái 'Kính gửi:', ô phải danh sách '- A;' '- B.'   (nhiều nơi nhận)
      - một ô/paragraph 'Kính gửi:' rồi danh sách ngay dưới trong cùng ô, hoặc ở các
        paragraph tiếp theo (mẫu của UBND tỉnh, cong-van-xin-y-kien-cac-co-quan…).
    """
    for i, (loc, t) in enumerate(ctx.texts):
        s0 = nfc(t).strip()
        if not re.match(r"^Kính\s+gửi", s0):
            continue
        cung_cho = re.sub(r"^Kính\s+gửi\s*:?\s*", "", s0).strip()
        muc = [x.strip().strip(";.").strip()
               for x in re.split(r"[;\n]", cung_cho) if x.strip().strip(";.-").strip()]
        if not muc:
            # danh sách nằm ở ô kế bên (bảng) hoặc các đoạn tiếp theo
            nguon = "\n".join(nfc(x.text) for x in _o_ke_ben(doc, loc))
            if not nguon.strip():
                nguon = _con_lai_trong_bang(doc, loc)
            if not nguon.strip():
                gom = []
                for _, t2 in ctx.texts[i + 1:i + 8]:
                    s2 = nfc(t2).strip()
                    if not s2:
                        if gom:
                            break
                        continue
                    if not s2.startswith("-"):
                        break
                    gom.append(s2)
                nguon = "\n".join(gom)
            muc = [x.strip().strip(";.").strip()
                   for x in re.split(r"[;\n]", nguon) if x.strip().strip(";.-").strip()]
        return loc, cung_cho, muc
    return None


def rule_R16(doc, ctx) -> list[Finding]:
    """R16 — Khối Kính gửi: gửi MỘT cơ quan thì phải nằm trên cùng một dòng.

    Quy tắc: gửi một cơ quan → 'Kính gửi: <tên cơ quan>.' trên CÙNG MỘT DÒNG; gửi nhiều cơ quan
    → 'Kính gửi:' tách lên trên, danh sách '- A;' … '- Z.' xuống dưới. Khối Kính gửi phải có nơi
    nhận, không được để trống.
    Nguồn: Nhóm G, Bạn chốt 18/9/2026 (bản xuất ra ngày 18/9/2026 để 'Kính gửi:' một dòng, tên
    cơ quan một dòng dù chỉ gửi Công an tỉnh).
    Mức: FAIL.
    """
    kg = _khoi_kinh_gui(doc, ctx)
    if kg is None:
        return []
    loc, cung_cho, muc = kg
    if not muc:
        return [Finding("R16", FAIL, loc, "Kính gửi:",
                        "Khối Kính gửi chưa có nơi nhận — ghi tên cơ quan nhận văn bản.")]
    # Dấu hiệu chắc chắn sai: 'Kính gửi:' đứng một mình, dưới/bên nó là ĐÚNG MỘT nơi nhận viết
    # trơn (không có gạch đầu dòng) — tức một cơ quan mà vẫn tách hai dòng. Mọi mẫu thật trình bày
    # dạng danh sách đều mở đầu bằng '- ', nên điều kiện này không bắt nhầm mẫu thật.
    if not cung_cho and len(muc) == 1 and not muc[0].lstrip().startswith("-"):
        return [Finding(
            "R16", FAIL, loc, cut(f"Kính gửi: / {muc[0]}"),
            "Chỉ gửi một cơ quan thì 'Kính gửi: " + cut(muc[0], 40) + ".' phải nằm trên CÙNG MỘT "
            "dòng (xóa bảng/đoạn tách dòng); tách dòng chỉ dùng khi gửi nhiều cơ quan.")]
    return []


THU_TU_LA = re.compile(r"(?<![\w])(Một|Hai|Ba|Bốn|Năm|Sáu|Bảy|Tám|Chín|Mười)\s+là\s*,", re.IGNORECASE)
DANH_SO_KEP = re.compile(r"\(\s*\d{1,2}\s*\)\s*(Một|Hai|Ba|Bốn|Năm|Sáu|Bảy|Tám|Chín|Mười)\s+là\b", re.IGNORECASE)


def rule_R17(doc, ctx) -> list[Finding]:
    """R17 — Liệt kê "Một là, Hai là…": không đánh số kép, mỗi ý một đoạn.

    Quy tắc: khi liệt kê bằng "Một là, …", "Hai là, …" thì KHÔNG thêm số trong ngoặc
    "(1) Một là", "(2) Hai là" (đánh số hai lần); mỗi ý viết thành một đoạn riêng, ý giữa kết
    thúc bằng dấu chấm phẩy, ý cuối bằng dấu chấm — không dồn cả dãy ý vào một đoạn.
    Nguồn: rà soát Báo cáo tháng 9/2026 thực hiện NQ 34-NQ/TU (mục Khó khăn, vướng mắc viết
    "(1) Một là… (2) Hai là… (4) Bốn là…" trong cùng một đoạn), Bạn chốt 22/9/2026
    "thống nhất kiểu đánh số".
    Mức: WARN.
    """
    out: list[Finding] = []
    for loc, t in ctx.texts:
        if not loc.startswith("đoạn"):
            continue
        if DANH_SO_KEP.search(t):
            out.append(Finding("R17", WARN, loc, cut(t),
                               "Đánh số kép '(n) Một là' — bỏ '(n)', chỉ giữ 'Một là, …'."))
        elif len(THU_TU_LA.findall(t)) >= 2:
            out.append(Finding("R17", WARN, loc, cut(t),
                               "Nhiều ý 'Một là/Hai là…' dồn trong một đoạn — tách mỗi ý thành một đoạn."))
    return out


LA_MA = re.compile(r"^\s*(I|II|III|IV|V|VI|VII|VIII|IX|X)\.\s")


def _mo_dau_tab(p) -> bool:
    for r in p._p.findall(qn("w:r")):
        con = [c for c in r if c.tag not in (qn("w:rPr"), qn("w:lastRenderedPageBreak"))]
        if con:
            return con[0].tag == qn("w:tab")
    return False


def rule_R18(doc, ctx) -> list[Finding]:
    """R18 — Đề mục La Mã (I, II, III…) trong cùng văn bản phải lùi đầu dòng thống nhất.

    Quy tắc: các đề mục cùng cấp I, II, III, IV… phải cùng một cách lùi đầu dòng; không để đề
    mục này gõ ký tự tab ở đầu còn đề mục kia dùng thụt dòng đầu của đoạn (lệch 1,27 cm và 1 cm).
    Chỉ bắt khi văn bản LẪN hai cách — nhiều mẫu thật dùng tab đầu đoạn một cách nhất quán nên
    tab tự nó không phải lỗi (tests/rule-inventory.md mục D: quy tắc phải PASS mẫu thật).
    Nguồn: Quy tắc thể thức "lùi đầu dòng đồng nhất 1cm" (SKILL.md mục Thể thức); rà soát Báo cáo
    tháng 9/2026 thực hiện NQ 34-NQ/TU (đề mục I, II, IV mở đầu bằng tab, đề mục III không),
    Bạn chốt 22/9/2026 "thống nhất kiểu đánh số và thể thức".
    Mức: WARN.
    """
    muc = [(loc, p) for loc, p in ctx.items
           if loc.startswith("đoạn") and LA_MA.match(nfc(p.text))]
    co_tab = [(loc, p) for loc, p in muc if _mo_dau_tab(p)]
    if not co_tab or len(co_tab) == len(muc):
        return []
    return [Finding("R18", WARN, loc, cut(p.text),
                    "Đề mục La Mã mở đầu bằng tab trong khi đề mục cùng cấp khác không dùng tab — "
                    "xóa tab, đặt thụt dòng đầu 1 cm như các đề mục còn lại.")
            for loc, p in co_tab]


# ─────────────── R19–R22: chuẩn xuất bản (Bạn chốt 13/10/2026) ───────────────
# Vụ 13/10/2026: 3 công văn hoàn thiện hồ sơ vận chuyển HHNH (Toàn Phát TQ, An Bình, Tân Phúc
# Hưng) trình trên hệ thống quản lý văn bản mới, PGĐ ký số báo lỗi. Rà lại: kiểu Normal và số
# trang còn phông .VnTime (TCVN3) kế thừa từ mẫu cũ; dòng Nơi nhận cỡ 12; khối ký dính sát thân
# văn bản (đoạn đệm 1–7 pt); văn bản thủ tục hành chính vẫn gửi "Ban Giám đốc Sở".
# Sửa tự động: scripts/chuan_hoa_xuat_ban.py (fill_template.save() và build_vb.py đã gọi sẵn).

PHONG_CHUAN = "Times New Roman"
PHONG_KY_HIEU_OK = re.compile(r"^(Symbol|Wingdings.*|Webdings)$")
PHAN_PHONG = re.compile(r"word/(document|styles|header\d*|footer\d*|footnotes|endnotes)\.xml$")


def rule_R19(doc, ctx) -> list[Finding]:
    """R19 — Toàn bộ file chỉ dùng phông Times New Roman.

    Quy tắc: trước khi xuất file phải quét TOÀN BỘ phông — thân, kiểu (Normal, Header, Footer…),
    docDefaults, đầu/chân trang (số trang), chú thích, phông giao diện (theme). Không còn .VnTime,
    .VnTimeH (TCVN3), Arial, Calibri, Cambria, Segoe UI, Courier… Phông ký hiệu Symbol, Wingdings
    được giữ. Sửa: python3 scripts/chuan_hoa_xuat_ban.py <file> --chi-phong.
    Nguồn: Bạn chốt 13/10/2026 "nguyên tắc trước khi xuất file phải quét toàn bộ đúng phông chữ".
    Mức: WARN (mẫu thật cũ còn phông lạ trong kiểu chữ ẩn) — thành FAIL khi chạy --final.
    """
    muc = FAIL if ctx.final else WARN
    la: dict[str, set[str]] = {}
    with zipfile.ZipFile(ctx.path) as z:
        for n in z.namelist():
            if PHAN_PHONG.match(n):
                x = z.read(n).decode("utf-8", "replace")
                for attrs in re.findall(r"<w:rFonts\b([^>]*)/>", x):
                    for _, v in re.findall(r'w:(ascii|hAnsi|eastAsia|cs)="([^"]+)"', attrs):
                        if v != PHONG_CHUAN and not PHONG_KY_HIEU_OK.match(v):
                            la.setdefault(v, set()).add(n.split("/")[-1])
            elif n == "word/theme/theme1.xml":
                x = z.read(n).decode("utf-8", "replace")
                for v in re.findall(r'<a:latin typeface="([^"]*)"', x):
                    if v and v != PHONG_CHUAN:
                        la.setdefault(v, set()).add("theme1.xml")
    return [Finding("R19", muc, ", ".join(sorted(noi)), f"phông '{ten}'",
                    "Đổi toàn bộ về Times New Roman (kể cả kiểu chữ, số trang, theme): "
                    "python3 scripts/chuan_hoa_xuat_ban.py <file> --chi-phong")
            for ten, noi in sorted(la.items())]


def _co_chu(run, p, doc) -> float | None:
    """Cỡ chữ hiển thị (pt) của run: run → kiểu ký tự → kiểu đoạn → docDefaults."""
    if run is not None and run.font.size is not None:
        return run.font.size.pt
    st = p.style
    while st is not None:
        if st.font.size is not None:
            return st.font.size.pt
        st = st.base_style
    try:
        sz = doc.styles.element.find(qn("w:docDefaults")).find(qn("w:rPrDefault")) \
            .find(qn("w:rPr")).find(qn("w:sz"))
        return int(sz.get(qn("w:val"))) / 2
    except AttributeError:
        return None


def _co_dau_doan(p, doc) -> float | None:
    ppr = p._p.pPr
    if ppr is not None:
        rpr = ppr.find(qn("w:rPr"))
        if rpr is not None and rpr.find(qn("w:sz")) is not None:
            return int(rpr.find(qn("w:sz")).get(qn("w:val"))) / 2
    return _co_chu(None, p, doc)


def _o_noi_nhan(doc):
    for t in doc.tables:
        for row in t.rows:
            for c in row.cells:
                if any(re.match(r"^\s*Nơi\s+nhận", nfc(p.text)) for p in c.paragraphs):
                    return t, c
    return None, None


def rule_R20(doc, ctx) -> list[Finding]:
    """R20 — Cỡ chữ khối Nơi nhận: các dòng "- …" cỡ 11.

    Quy tắc: "Nơi nhận:" cỡ 12 (đậm, nghiêng); tên cơ quan, đơn vị nhận ("- Như trên;",
    "- Sở …;", "- Lưu: VT, CN.") cỡ 11 — để 12 là sai (NĐ 30/2020 Phụ lục I ô số 9b).
    Nguồn: Bạn chốt 13/10/2026 "các cơ quan ở nơi nhận chữ 11, mà bạn lại để 12 là sai".
    Mức: WARN (nhiều mẫu thật cũ để 12) — thành FAIL khi chạy --final.
    """
    muc = FAIL if ctx.final else WARN
    _, o = _o_noi_nhan(doc)
    if o is None:
        return []
    out: list[Finding] = []
    for i, p in enumerate(o.paragraphs):
        tx = nfc(p.text).strip()
        if not tx.startswith("-"):
            continue
        co = {_co_chu(r, p, doc) for r in text_runs(p)}
        sai = sorted(c for c in co if c is not None and abs(c - 11) > 0.01)
        if sai:
            out.append(Finding("R20", muc, f"ô Nơi nhận đoạn {i}", cut(tx),
                               f"Dòng Nơi nhận đang cỡ {', '.join(f'{c:g}' for c in sai)} — phải cỡ 11 "
                               f"(sửa: scripts/chuan_hoa_xuat_ban.py)."))
    return out


def rule_R21(doc, ctx) -> list[Finding]:
    """R21 — Khối Nơi nhận - ký cách khối nội dung đúng MỘT dòng (cỡ 14).

    Quy tắc: giữa đoạn cuối của thân văn bản và bảng Nơi nhận - chữ ký có đúng một đoạn trống,
    cao bằng một dòng chữ thường (cỡ ≥ 12, không đặt giãn dòng cố định dưới 12 pt). Đoạn "đệm"
    1–7 pt của mẫu cũ nhìn như dính sát — không tính là một dòng.
    Nguồn: Quy tắc 22 / H13 (09/9/2026, 18/9/2026); Bạn nhắc lại 13/10/2026 "khối nơi nhận và
    ký phải cách khối nội dung văn bản 1 dòng".
    Mức: WARN (13 mẫu thật cũ có 0, 2 dòng hoặc đoạn đệm nhỏ) — thành FAIL khi chạy --final.
    """
    muc = FAIL if ctx.final else WARN
    t, _ = _o_noi_nhan(doc)
    if t is None:
        return []
    body = doc.element.body
    tbl = t._tbl
    if tbl.getparent() is not body:
        return []
    kids = list(body)
    i = kids.index(tbl) - 1
    trong = []
    while i >= 0 and kids[i].tag == qn("w:p") and not _tt(kids[i]).strip():
        trong.append(kids[i])
        i -= 1
    loc = "trước bảng Nơi nhận - ký"
    if not trong:
        return [Finding("R21", muc, loc, "(không có dòng trống)",
                        "Thêm đúng một dòng trống cỡ 14 giữa thân văn bản và khối Nơi nhận - ký.")]
    if len(trong) > 1:
        return [Finding("R21", muc, loc, f"({len(trong)} đoạn trống)",
                        "Chỉ giữ đúng một dòng trống cỡ 14 trước khối Nơi nhận - ký.")]
    from docx.text.paragraph import Paragraph
    p = Paragraph(trong[0], doc._body)
    co = _co_dau_doan(p, doc)
    sp = trong[0].find(".//" + qn("w:spacing"))
    co_dinh = (sp is not None and sp.get(qn("w:lineRule")) == "exact"
               and int(sp.get(qn("w:line"), "240")) < 240)
    if (co is not None and co < 12) or co_dinh:
        return [Finding("R21", muc, loc, f"(đoạn trống cỡ {co:g} pt)" if co else "(giãn dòng cố định nhỏ)",
                        "Dòng trống trước khối ký quá thấp, nhìn như dính sát — đặt cỡ 14, giãn dòng đơn "
                        "(sửa: scripts/chuan_hoa_xuat_ban.py).")]
    return []


TTHC_TRICH_YEU = re.compile(
    r"hồ\s+sơ\s+đề\s+nghị\s+cấp|bổ\s+sung\s+hồ\s+sơ|hoàn\s+thiện\s+hồ\s+sơ|trả\s+(lại\s+)?hồ\s+sơ|"
    r"từ\s+chối\s+cấp|không\s+cấp\s+Giấy|chấm\s+dứt\s+(việc\s+)?thẩm\s+định|"
    r"cấp(\s+lại|\s+điều\s+chỉnh)?\s+Giấy\s+(phép|chứng\s+nhận)", re.IGNORECASE)


def _la_tthc(ctx) -> bool:
    if ctx.loai in ("giay-phep", "giay-chung-nhan"):
        return True
    vv = [t for _, t in ctx.texts[:40] if t.strip().startswith("V/v")]
    if vv and TTHC_TRICH_YEU.search(vv[0]):
        return True
    if "motcua-tthc" in ctx.full_text:
        return True
    return any(re.match(r"^-?\s*Lưu\s*:.*\bBP1C\b", t.strip()) for _, t in ctx.texts)


def rule_R22(doc, ctx) -> list[Finding]:
    """R22 — Văn bản giải quyết thủ tục hành chính không gửi "Ban Giám đốc Sở".

    Quy tắc: công văn hoàn thiện, bổ sung, trả hồ sơ; giấy phép, giấy chứng nhận; văn bản từ chối,
    chấm dứt thẩm định… thuộc thủ tục hành chính chỉ gửi trực tiếp các đơn vị theo đúng quy định
    (tổ chức, cá nhân nộp hồ sơ; cơ quan mà văn bản quy phạm buộc phải gửi). Nhận diện: V/v có
    "hồ sơ đề nghị cấp", "bổ sung/hoàn thiện/trả hồ sơ", "cấp Giấy phép/Giấy chứng nhận"…; văn bản
    là Giấy phép/Giấy chứng nhận; có địa chỉ motcua-tthc; dòng Lưu có BP1C.
    Nguồn: Bạn chốt 13/10/2026 "thủ tục hành chính từ nay không gửi Ban Giám đốc Sở nữa, chỉ gửi
    trực tiếp các đơn vị theo đúng quy định".
    Mức: FAIL.
    """
    if not _la_tthc(ctx):
        return []
    return [Finding("R22", FAIL, loc, cut(dong),
                    "Văn bản thủ tục hành chính không gửi Ban Giám đốc Sở — xóa dòng này "
                    "(scripts/chuan_hoa_xuat_ban.py --tthc).")
            for loc, dong in _khoi_noi_nhan(ctx)
            if re.search(r"Ban\s+(Giám\s+đốc|GĐ)\s+Sở|\bBGĐ\s+Sở", dong)]



# ── R23: số hiệu văn bản quy phạm phải có nguồn (GATE 0, Bạn chốt 17/10/2026) ──

# Số hiệu văn bản quy phạm pháp luật luôn có năm ở giữa: 32/2024/NĐ-CP, 66.25/2026/NQ-CP, 42/2024/QH15,
# 01/2026/QĐ-UBND. Văn bản hành chính (3725/QĐ-UBND, 6020/SCT-CN) không có năm nên không thuộc R23.
# Chỉ các ký hiệu của văn bản quy phạm (Luật Ban hành VBQPPL); số/năm/ký hiệu của doanh nghiệp (38/2026/AP-DA) không tính.
SO_QPPL = re.compile(
    r"(?<![\d./])(\d{1,4}(?:\.\d{1,3})?[a-z]?)/(\d{4})/"
    r"(NĐ-CP|NQ-CP|QĐ-TTg|NQ-HĐND|QĐ-UBND|TTLT-[A-ZĐ\-]{2,20}|TT-[A-ZĐ]{2,10}|NQ-UBTVQH\d{2}|"
    r"PL-UBTVQH\d{2}|UBTVQH\d{2}|QH\d{2}|L-CTN)(?![\w/-])")
TEP_CAN_CU_PHIEN = ("can-cu-phien.txt", "ke-hoach-soan.txt")
_KHO_SO_HIEU: set[str] | None = None


def khoa_so_hieu(so: str) -> str:
    """'32/2024/NĐ-CP' và '32/2024/ND-CP' về cùng một khóa so sánh."""
    return nfc(so).upper().replace("Đ", "D").replace(" ", "")


def _so_hieu_trong_kho() -> set[str]:
    """Số hiệu của mọi tệp gốc trong kho: sổ cái DANH-MUC-VAN-BAN-GOC.csv ở gốc kho skill-sct (khi chạy trong
    kho) và van-ban-goc/00-DANH-MUC-CHUNG.md của plugin (có cả trong gói claude.ai). Hai tệp do
    scripts/build_so_cai_van_ban_goc.py sinh — cùng nguồn với scripts/tim_van_ban.py lớp 1."""
    global _KHO_SO_HIEU
    if _KHO_SO_HIEU is not None:
        return _KHO_SO_HIEU
    kho: set[str] = set()
    md = PLUGIN_DIR / "van-ban-goc" / "00-DANH-MUC-CHUNG.md"
    if md.exists():
        for ln in md.read_text(encoding="utf-8").splitlines():
            if ln.startswith("| ") and not ln.startswith("| Số hiệu"):
                kho.add(khoa_so_hieu(ln.split("|")[1].strip()))
    for goc in PLUGIN_DIR.parents:
        csv_ = goc / "DANH-MUC-VAN-BAN-GOC.csv"
        if csv_.exists():
            for ln in csv_.read_text(encoding="utf-8").splitlines()[1:]:
                kho.add(khoa_so_hieu(ln.split(",", 1)[0]))
            break
    kho.discard("")
    kho.discard("—")
    _KHO_SO_HIEU = kho
    return kho


def _can_cu_phien(ctx) -> set[str]:
    """Căn cứ Bạn cung cấp trong phiên: tệp can-cu-phien.txt (mỗi dòng một số hiệu) và các dòng căn cứ có nguồn
    trong ke-hoach-soan.txt (GATE 0), đặt cạnh file .docx hoặc ở thư mục làm việc; biến môi trường
    VBHC_CAN_CU_PHIEN (ngăn bằng dấu phẩy, chấm phẩy). Dòng ghi "chưa có nguồn" không được tính."""
    import os
    ra: set[str] = set()
    thu_muc = {ctx.path.resolve().parent, Path.cwd()}
    for d in thu_muc:
        for ten in TEP_CAN_CU_PHIEN:
            f = d / ten
            if not f.exists():
                continue
            for ln in f.read_text(encoding="utf-8").splitlines():
                if "chưa có nguồn" in nfc(ln).lower():
                    continue
                ra |= {khoa_so_hieu(m.group(0)) for m in SO_QPPL.finditer(nfc(ln))}
    for x in re.split(r"[,;]", os.environ.get("VBHC_CAN_CU_PHIEN", "")):
        if x.strip():
            ra.add(khoa_so_hieu(x.strip()))
    return ra


def rule_R23(doc, ctx) -> list[Finding]:
    """R23 — Số hiệu văn bản quy phạm pháp luật viện dẫn phải có nguồn.

    Quy tắc: mọi số hiệu văn bản quy phạm (dạng số/năm/ký hiệu: 32/2024/NĐ-CP, 42/2024/QH15, 01/2026/QĐ-UBND)
    xuất hiện trong file phải khớp một tệp gốc trong kho (sổ cái văn bản gốc — như tim_van_ban.py lớp 1) hoặc
    danh sách căn cứ Bạn cung cấp trong phiên (can-cu-phien.txt, ke-hoach-soan.txt, VBHC_CAN_CU_PHIEN).
    Không khớp thì in số hiệu để Bạn kiểm tra — KHÔNG kết luận là bịa (kho chưa đủ thì chỉ là chưa đối chiếu được).
    Nguồn: GATE 0 — Kế hoạch soạn thảo, điểm c (Bạn chốt 17/10/2026, bản giao việc mục 1.4); Nhóm A.
    Mức: WARN. Mỗi số hiệu báo một lần.
    """
    kho = _so_hieu_trong_kho() | _can_cu_phien(ctx)
    out: list[Finding] = []
    da_bao: set[str] = set()
    for loc, t in ctx.texts:
        for m in SO_QPPL.finditer(t):
            k = khoa_so_hieu(m.group(0))
            if k in kho or k in da_bao:
                continue
            da_bao.add(k)
            out.append(Finding(
                "R23", WARN, loc, cut(t),
                f"Số hiệu '{m.group(0)}' chưa khớp tệp gốc nào trong kho hay căn cứ Bạn gửi trong phiên — "
                f"chạy tim_van_ban.py \"{m.group(0)}\" đối chiếu; không có nguồn thì bỏ khỏi văn bản hoặc bôi tím.",
            ))
    return out


UBND_DAY_DU = re.compile(r"(?:Ủy|Uỷ) ban nhân dân")


def _bang_phu_luc(doc, ti: int) -> bool:
    """Bảng ≥ 3 cột, không phải bảng header (Quốc hiệu/Số:) hay bảng Nơi nhận - ký → coi là bảng phụ lục/danh mục."""
    try:
        tb = doc.tables[ti]
    except IndexError:
        return False
    if len(tb.columns) < 3:
        return False
    dau = nfc(" ".join(c.text for r in tb.rows[:2] for c in r.cells))
    if re.search(r"CỘNG HÒA|CỘNG HOÀ|Độc lập|Nơi nhận", dau):
        return False
    return True


def rule_R24(doc, ctx) -> list[Finding]:
    """R24 — "Ủy ban nhân dân" ở khối Nơi nhận và trong ô bảng phụ lục, danh mục phải viết tắt "UBND".

    Quy tắc (phạm vi đã thu hẹp khi chuyển từ PR 116, 18/10/2026): chỉ bắt ở (1) các dòng của khối
    "Nơi nhận:" và (2) ô của bảng phụ lục, danh mục (bảng ≥ 3 cột, không phải bảng header hay bảng ký).
    Ở đó viết "UBND tỉnh (b/c)", "UBND các xã, phường"…; chữ đầy đủ chỉ ở tên cơ quan ban hành đầu trang
    và khối ký "TM. ỦY BAN NHÂN DÂN" (viết hoa, không bị bắt). THÂN văn bản (kể cả Kính gửi, căn cứ) KHÔNG
    thuộc phạm vi R24: checklist rà soát độc lập dòng 12 và ra_soat_doc_lap.py mục [5] (Bạn chốt
    17/10/2026) yêu cầu thân viết đầy đủ "Ủy ban nhân dân" — hai quy tắc giữ đúng phạm vi của mình;
    riêng phần căn cứ còn chờ Bạn chốt (xem Nhóm P9).
    Nguồn: Bạn chốt 04/10/2026 khi rà Kế hoạch Bài toán lớn số 2 (PR 116, R19 của nhánh); Nhóm G, Nhóm P9
    trong reference/phong-tranh-sai-lam.md.
    Mức: WARN — mẫu thật ban hành trước 04/10/2026 có thể còn viết đủ chữ; văn bản soạn mới phải sửa hết
    trước khi trình ký.
    """
    out: list[Finding] = []
    da: set[str] = set()
    for loc, dong in _khoi_noi_nhan(ctx):
        if UBND_DAY_DU.search(dong):
            da.add(loc)
            out.append(Finding(
                "R24", WARN, loc, cut(dong),
                "Nơi nhận viết tắt 'UBND' (UBND tỉnh (b/c), UBND các xã, phường) — chữ đầy đủ chỉ ở "
                "đầu trang và khối ký.",
            ))
    for loc, t in ctx.texts:
        m = re.match(r"bảng (\d+) ô", loc)
        if not m or loc in da or not UBND_DAY_DU.search(t):
            continue
        if not _bang_phu_luc(doc, int(m.group(1))):
            continue
        out.append(Finding(
            "R24", WARN, loc, cut(t),
            "Trong bảng phụ lục, danh mục viết tắt 'UBND' (UBND tỉnh, UBND xã, phường) — viết đủ chữ "
            "chỉ ở thân văn bản.",
        ))
        if len(out) >= 8:
            break
    return out


CQNN = re.compile(
    r"(UBND|Ủy ban|Uỷ ban|HĐND|Tỉnh ủy|Tỉnh uỷ|\bSở\b|Chi cục|\bCục\b|\bBộ\b|Ban Quản lý|BQL|Công an|Thuế|"
    r"Thống kê|Hải quan|Trung tâm|Viện\b|Trường\b)",
    re.IGNORECASE,
)
DONG_NOI_BO = re.compile(
    r"^-?\s*(Lưu\s*:|Như\s+trên|Như\s+kính\s+gửi|CVP|PCVP|Chánh\s+VP|Phó\s+CVP|Văn\s+phòng|VP\b|"
    r"Ban\s+Giám\s+đốc|Giám\s+đốc|GĐ|PGĐ|Lãnh\s+đạo|Các\s+phòng|Phòng\b)",
    re.IGNORECASE,
)


def rule_R25(doc, ctx) -> list[Finding]:
    """R25 — Nơi nhận xếp theo vị thế cơ quan nhà nước; doanh nghiệp đứng riêng dòng, sau cùng.

    Quy tắc: thứ tự khối Nơi nhận đi từ cấp trên (Tỉnh ủy, HĐND, UBND tỉnh, BCĐ — để b/c) →
    sở, ban, ngành tỉnh → cơ quan ngành dọc (Công an, Thuế, Thống kê, Hải quan) → UBND xã,
    phường → doanh nghiệp (dòng riêng) → Văn phòng (CVP, PCVP) → Lưu. Doanh nghiệp KHÔNG
    chung dòng với cơ quan nhà nước (vụ "Chi cục Hải quan khu vực VII; Công ty Điện lực Lào
    Cai" bị Bạn bác 04/10/2026).
    Nguồn: Bạn chốt 04/10/2026 (PR 116, R20 của nhánh — đổi mã R25 khi chuyển lên bản 2.34.0 vì R20 ở
    main đã là "Nơi nhận cỡ 11"); Nhóm G, Nhóm P9. Bổ sung cho R06 (R06 chỉ bắt dòng đầu) và R22.
    Mức: FAIL khi doanh nghiệp chung dòng với cơ quan nhà nước; WARN khi sau dòng doanh nghiệp
    còn dòng cơ quan nhà nước (trừ Văn phòng, Ban Giám đốc, Lưu).
    """
    khoi = _khoi_noi_nhan(ctx)
    if not khoi:
        return []
    out: list[Finding] = []
    da_co_dn = False
    for loc, dong in khoi:
        la_dn = bool(DN.search(dong))
        la_cq = bool(CQNN.search(dong)) and not DONG_NOI_BO.match(dong)
        if la_dn and la_cq:
            out.append(Finding(
                "R25", FAIL, loc, cut(dong),
                "Doanh nghiệp không chung dòng với cơ quan nhà nước — tách thành dòng riêng, "
                "xếp sau các cơ quan nhà nước, trước dòng Văn phòng và Lưu.",
            ))
            continue
        if la_dn:
            da_co_dn = True
            continue
        if da_co_dn and la_cq:
            out.append(Finding(
                "R25", WARN, loc, cut(dong),
                "Cơ quan nhà nước đứng sau dòng doanh nghiệp — sắp lại Nơi nhận theo vị thế: "
                "cấp trên (b/c), sở ngành, ngành dọc, UBND xã phường, rồi mới đến doanh nghiệp.",
            ))
    return out


def rule_R26(doc, ctx) -> list[Finding]:
    """R26 — Khối Nơi nhận - chữ ký: hai ô căn TRÊN (vAlign top), dòng "Nơi nhận:" ngang dòng chức vụ.

    Quy tắc: bảng khối ký không áp căn giữa chiều dọc như bảng nội dung. Ô ký thường cao hơn ô Nơi nhận
    (chức vụ + khoảng trống ký + họ tên), nếu ô Nơi nhận đặt vAlign center/bottom thì dòng "Nơi nhận:"
    tụt xuống thấp hơn dòng "KT. CHỦ TỊCH"/"GIÁM ĐỐC" — Bạn chỉ ra 23/10/2026 ("sao cái ô nơi nhận thấp
    hơn dòng KT. Chủ tịch"). Cách đúng: mọi ô của bảng ký vAlign top (hoặc bỏ vAlign); nhu cầu ô ký rộng
    rãi giải quyết bằng dòng trống trong ô ký, không bằng căn giữa dọc.
    Nguồn: Bạn chốt 23/10/2026; Nhóm G (reference/phong-tranh-sai-lam.md), sổ lỗi L011.
    Mức: WARN — mẫu thật cũ có thể còn vAlign center ở ô Nơi nhận; --tu-sua của kiem_tra_truoc_khi_giao.py
    tự đặt top.
    """
    t, o = _o_noi_nhan(doc)
    if t is None:
        return []
    out: list[Finding] = []
    for row in t.rows:
        for c in row.cells:
            if not c.text.strip():
                continue
            pr = c._tc.tcPr
            va = pr.find(qn("w:vAlign")) if pr is not None else None
            if va is not None and va.get(qn("w:val")) in ("center", "bottom"):
                out.append(Finding(
                    "R26", WARN, "bảng Nơi nhận - ký", cut(c.text.strip().splitlines()[0] if c.text.strip() else ""),
                    "Ô khối ký đặt căn giữa/dưới theo chiều dọc → dòng 'Nơi nhận:' lệch dòng chức vụ; đặt vAlign top "
                    "cho mọi ô của bảng ký (kiem_tra_truoc_khi_giao.py --tu-sua tự sửa).",
                ))
                break
        if out:
            break
    return out


RULES = [
    ("R01", rule_R01),
    ("R02", rule_R02),
    ("R03", rule_R03),
    ("R04", rule_R04),
    ("R05", rule_R05),
    ("R06", rule_R06),
    ("R07", rule_R07),
    ("R08", rule_R08),
    ("R09", rule_R09),
    ("R10", rule_R10),
    ("R11", rule_R11),
    ("R12", rule_R12),
    ("R13", rule_R13),
    ("R14", rule_R14),
    ("R15", rule_R15),
    ("R16", rule_R16),
    ("R17", rule_R17),
    ("R18", rule_R18),
    ("R19", rule_R19),
    ("R20", rule_R20),
    ("R21", rule_R21),
    ("R22", rule_R22),
    ("R23", rule_R23),
    ("R24", rule_R24),
    ("R25", rule_R25),
    ("R26", rule_R26),
]

MA_HOP_LE = {ma for ma, _ in RULES}


def chay(path: Path, only: list[str] | None = None, final: bool = False) -> list[Finding]:
    """Chạy toàn bộ (hoặc một phần) quy tắc trên một file .docx.

    Lỗi khi đọc file hoặc khi một hàm kiểm gặp dữ liệu bất thường được trả về dưới mã
    LOI-DOC / LOI-<mã> ở mức FAIL — không bao giờ nuốt lỗi im lặng.
    """
    path = Path(path)
    try:
        ctx = Ctx(path, final=final)
        doc = Document(str(path))
        ctx.build(doc)
    except Exception as e:
        return [Finding("LOI-DOC", FAIL, str(path.name), cut(str(e)),
                        "Không đọc được file .docx — kiểm tra file có hợp lệ không.")]
    out: list[Finding] = []
    for ma, fn in RULES:
        if only and ma not in only:
            continue
        try:
            out.extend(fn(doc, ctx))
        except Exception as e:
            out.append(Finding(
                f"LOI-{ma}", FAIL, str(path.name), cut(f"{type(e).__name__}: {e}"),
                f"Hàm kiểm {ma} gặp dữ liệu bất thường — sửa hàm kiểm hoặc báo lại, "
                f"KHÔNG bỏ qua file này.",
            ))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Kiểm quy tắc soạn thảo VBHC bằng máy (vbhc-vn).",
        formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument("docx", nargs="+", help="một hoặc nhiều file .docx")
    ap.add_argument("--only", action="append", default=[],
                    help="chỉ chạy các mã này, vd --only R03 --only R11")
    ap.add_argument("--final", action="store_true",
                    help="bản hoàn thiện để xuất bản: nâng WARN nhóm hoàn thiện thành FAIL")
    ap.add_argument("--json", action="store_true", help="xuất JSON cho máy đọc")
    a = ap.parse_args()

    only = []
    for m in a.only:
        for x in re.split(r"[,\s]+", m):
            x = x.strip().upper()
            if not x:
                continue
            if x not in MA_HOP_LE:
                print(f"LỖI: không có quy tắc '{x}'. Mã hợp lệ: {', '.join(sorted(MA_HOP_LE))}",
                      file=sys.stderr)
                return 2
            only.append(x)

    tong: dict[str, list[Finding]] = {}
    for f in a.docx:
        p = Path(f)
        if not p.exists():
            print(f"LỖI: không tìm thấy {p}", file=sys.stderr)
            return 2
        tong[str(p)] = chay(p, only or None, a.final)

    if a.json:
        print(json.dumps(
            {k: [asdict(x) for x in v] for k, v in tong.items()},
            ensure_ascii=False, indent=2))
    else:
        for f, ds in tong.items():
            n_fail = sum(1 for x in ds if x.level == FAIL)
            n_warn = len(ds) - n_fail
            print("=" * 62)
            print(f"QA QUY TẮC — {Path(f).name}" + ("   [--final]" if a.final else ""))
            print("=" * 62)
            for x in sorted(ds, key=lambda x: (x.level != FAIL, x.code)):
                print("  " + x.line())
            ket = "PASS" if n_fail == 0 else f"FAIL ({n_fail} lỗi)"
            print(f"\nKẾT QUẢ: {ket}  |  WARN: {n_warn}  |  "
                  f"quy tắc chạy: {len(only) if only else len(RULES)}")
    return 1 if any(x.level == FAIL for ds in tong.values() for x in ds) else 0


if __name__ == "__main__":
    sys.exit(main())
