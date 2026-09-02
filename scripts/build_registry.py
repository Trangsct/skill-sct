#!/usr/bin/env python3
"""Sổ đăng ký văn bản pháp luật dùng chung — quét trích dẫn trong 20 plugin.

    python3 scripts/build_registry.py          # dựng lại registry/van-ban-phap-luat.csv + README.md
    python3 scripts/build_registry.py --check  # chỉ báo: văn bản có trạng thái "hết hiệu lực/bị thay thế"
                                               # mà plugin vẫn dẫn không kèm văn bản thay thế (WARN, exit 0)

Hai lớp dữ liệu:
1. TỰ ĐỘNG (không sửa tay): mã văn bản, loại, số plugin dùng, số lần, có bản gốc trong van-ban-goc/ không.
2. NGƯỜI DUY TRÌ (`registry/trang-thai.csv`): ngày ban hành, hiệu lực, bị sửa đổi bởi, bị thay thế bởi,
   dự thảo thay thế, ghi chú. Chỉ ghi khi đã đối chiếu bản gốc; để trống nếu chưa chắc.

Quy ước mã (khớp cả cách viết tắt lẫn đầy đủ): `Luật 118/2025` · `NĐ 275/2026` · `TT 26/2026/TT-BCT` ·
`QĐ 2867/QĐ-UBND` · `QĐ 42/2026/QĐ-TTg` · `NQ 169/NQ-CP` · `VBHN 78/VBHN-VPQH` · `QCVN 01:2019/BCT` · `KL 48/KL-TT`.
"""
import csv
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
REG = REPO / "registry"
EXCLUDE_PARTS = ("van-ban-goc", "vi-du-thuc-te", "examples", "templates", "node_modules")

# (loại, regex) — nhóm 1 = số, nhóm 2 = năm (nếu có), nhóm 3 = ký hiệu (nếu có)
PATTERNS = [
    ("Luật", re.compile(r"\bLuật(?:\s+số)?\s+(\d{1,3})/(\d{4})(?:/QH\d{2})?", re.I)),
    ("NĐ", re.compile(r"\b(?:NĐ|Nghị định)(?:\s+số)?\s+(\d{1,3})/(\d{4})(?:/NĐ-CP)?", re.I)),
    ("TT", re.compile(r"\b(?:TT|Thông tư)(?:\s+số)?\s+(\d{1,3})/(\d{4})(?:/TT-([A-ZĐ&]{2,8}))?", re.I)),
    ("QĐ", re.compile(r"\b(?:QĐ|Quyết định)(?:\s+số)?\s+(\d{1,5})(?:/(\d{4}))?/QĐ-([A-ZĐ]{2,8})", re.I)),
    ("NQ", re.compile(r"\b(?:NQ|Nghị quyết)(?:\s+số)?\s+(\d{1,3}(?:\.\d{1,2})?)(?:/(\d{4}))?/NQ-([A-ZĐ]{2,8})", re.I)),
    ("VBHN", re.compile(r"\b(\d{1,3})/VBHN-([A-ZĐ]{2,8})", re.I)),
    ("QCVN", re.compile(r"\bQCVN\s+(\d{2}[A-Z]?):(\d{4})/([A-Z]{2,8})", re.I)),
    ("KL", re.compile(r"\b(?:KL|Kết luận)(?:\s+thanh tra)?(?:\s+số)?\s+(\d{1,4})/KL-([A-ZĐ]{2,8})", re.I)),
]


def make_key(kind, m):
    g = m.groups()
    if kind in ("Luật", "NĐ"):
        return f"{kind} {int(g[0])}/{g[1]}"
    if kind == "TT":
        return f"TT {int(g[0])}/{g[1]}"  # ký hiệu cơ quan (TT-BCT…) không đưa vào mã để không tách đôi
    if kind in ("QĐ", "NQ"):
        so, nam, kh = g
        so = so if "." in so else str(int(so))
        mid = f"/{nam}" if nam else ""
        return f"{kind} {so}{mid}/{kind}-{kh.upper()}"
    if kind == "VBHN":
        return f"VBHN {int(g[0])}/VBHN-{g[1].upper()}"
    if kind == "QCVN":
        return f"QCVN {g[0].upper()}:{g[1]}/{g[2].upper()}"
    if kind == "KL":
        return f"KL {int(g[0])}/KL-{g[1].upper()}"
    return m.group(0)


def iter_plugin_files():
    for pj in sorted(REPO.glob("*/.claude-plugin/plugin.json")):
        plugin = pj.parent.parent.name
        d = REPO / plugin / "skills" / plugin
        if not d.exists():
            continue
        for f in sorted(d.rglob("*.md")):
            rel = f.relative_to(d).as_posix()
            if rel.startswith("CHANGELOG") or any(p in rel.split("/") for p in EXCLUDE_PARTS):
                continue
            yield plugin, f


def originals_index():
    """Tập các chuỗi 'số-năm' xuất hiện trong tên file van-ban-goc để đoán có bản gốc."""
    names = []
    for pj in REPO.glob("*/.claude-plugin/plugin.json"):
        plugin = pj.parent.parent.name
        for f in (REPO / plugin / "skills" / plugin).rglob("van-ban-goc/**/*"):
            if f.is_file() and f.suffix.lower() in (".pdf", ".docx", ".doc", ".txt"):
                names.append((plugin, f.name))
    return names


def has_original(key, names):
    """Đoán có bản gốc: tên file chứa số hiệu (token riêng) VÀ năm (nếu mã có năm) hoặc loại văn bản."""
    kind = key.split(" ")[0]
    m = re.search(r"(\d+(?:\.\d+)?)(?:[/:](\d{4}))?", key.split(" ", 1)[1])
    if not m:
        return ""
    so, nam = m.group(1), m.group(2)
    tag = {"NĐ": "ND", "QĐ": "QD", "TT": "TT", "NQ": "NQ", "Luật": "Luat", "VBHN": "VBHN", "QCVN": "QCVN", "KL": "KL"}.get(kind, "")
    hits = set()
    for p, n in names:
        if not re.search(rf"(?<![\d.]){re.escape(so)}(?![\d])", n):
            continue
        if nam and not re.search(rf"(?<!\d){nam}(?!\d)", n):
            continue
        if not nam and tag and tag.lower() not in n.lower():
            continue
        hits.add(p)
    return ";".join(sorted(hits))


def scan():
    cites = defaultdict(lambda: defaultdict(int))  # key -> plugin -> count
    kinds = {}
    for plugin, f in iter_plugin_files():
        try:
            text = f.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            text = f.read_text(encoding="utf-8", errors="ignore")
        text = unicodedata.normalize("NFC", text)
        for kind, rx in PATTERNS:
            for m in rx.finditer(text):
                key = make_key(kind, m)
                cites[key][plugin] += 1
                kinds[key] = kind
    return cites, kinds


def load_status():
    p = REG / "trang-thai.csv"
    if not p.exists():
        return {}
    with p.open(encoding="utf-8", newline="") as fh:
        return {r["ma"].strip(): r for r in csv.DictReader(fh) if r.get("ma", "").strip()}


def sort_key(k):
    kind = k.split(" ")[0]
    order = {"Luật": 0, "VBHN": 1, "NĐ": 2, "TT": 3, "QĐ": 4, "NQ": 5, "QCVN": 6, "KL": 7}
    m = re.search(r"(\d{4})", k)
    return (order.get(kind, 9), -(int(m.group(1)) if m else 0), k)


def build():
    REG.mkdir(exist_ok=True)
    cites, kinds = scan()
    status = load_status()
    names = originals_index()
    rows = []
    for key in sorted(cites, key=sort_key):
        pl = cites[key]
        st = status.get(key, {})
        rows.append({
            "ma": key, "loai": kinds[key],
            "so_plugin": len(pl), "so_lan": sum(pl.values()),
            "plugins": ";".join(sorted(pl)),
            "ban_goc_tai": has_original(key, names),
            "ngay_ban_hanh": st.get("ngay_ban_hanh", ""), "hieu_luc": st.get("hieu_luc", ""),
            "bi_sua_doi_boi": st.get("bi_sua_doi_boi", ""), "bi_thay_the_boi": st.get("bi_thay_the_boi", ""),
            "du_thao_thay_the": st.get("du_thao_thay_the", ""), "ghi_chu": st.get("ghi_chu", ""),
        })
    out = REG / "van-ban-phap-luat.csv"
    with out.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    # README tóm tắt
    top = sorted(rows, key=lambda r: -r["so_plugin"])[:25]
    stale = [r for r in rows if r["bi_thay_the_boi"] or r["du_thao_thay_the"]]
    unknown_status_multi = [r for r in rows if r["so_plugin"] >= 3 and not any(r[c] for c in ("hieu_luc", "bi_sua_doi_boi", "bi_thay_the_boi", "ghi_chu"))]
    lines = ["# Sổ đăng ký văn bản pháp luật dùng chung (tự sinh — không sửa tay file này)", "",
             f"- Tổng số văn bản được trích dẫn trong 20 plugin: **{len(rows)}** (Luật {sum(1 for r in rows if r['loai']=='Luật')}, NĐ {sum(1 for r in rows if r['loai']=='NĐ')}, TT {sum(1 for r in rows if r['loai']=='TT')}, QĐ {sum(1 for r in rows if r['loai']=='QĐ')}, NQ {sum(1 for r in rows if r['loai']=='NQ')}, khác {sum(1 for r in rows if r['loai'] not in ('Luật','NĐ','TT','QĐ','NQ'))}).",
             f"- Có trạng thái do người duy trì ghi (`trang-thai.csv`): **{sum(1 for r in rows if r['ma'] in load_status())}**.",
             "- Dựng lại: `python3 scripts/build_registry.py`; kiểm dẫn chiếu văn bản đã bị thay thế: `--check`.", "",
             "## Văn bản dùng ở nhiều plugin nhất (khi thay đổi phải rà tất cả plugin trong cột)", "",
             "| Mã | Số plugin | Plugins | Hiệu lực | Bị sửa đổi bởi | Bị thay thế bởi / dự thảo |", "|---|---|---|---|---|---|"]
    for r in top:
        lines.append(f"| {r['ma']} | {r['so_plugin']} | {r['plugins'].replace(';', ', ')} | {r['hieu_luc']} | {r['bi_sua_doi_boi']} | {r['bi_thay_the_boi'] or r['du_thao_thay_the']} |")
    lines += ["", "## Văn bản đã bị thay thế hoặc đang có dự thảo thay thế — theo dõi", "",
              "| Mã | Plugins đang dẫn | Bị thay thế bởi | Dự thảo thay thế | Ghi chú |", "|---|---|---|---|---|"]
    for r in stale:
        lines.append(f"| {r['ma']} | {r['plugins'].replace(';', ', ')} | {r['bi_thay_the_boi']} | {r['du_thao_thay_the']} | {r['ghi_chu']} |")
    lines += ["", "## Dùng ở ≥3 plugin nhưng chưa có trạng thái — cần rà bản gốc rồi ghi vào `trang-thai.csv`", ""]
    lines += [f"- {r['ma']} ({r['so_plugin']} plugin: {r['plugins'].replace(';', ', ')})" for r in unknown_status_multi] or ["- (không có)"]
    (REG / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"registry: {len(rows)} văn bản, {len(stale)} có thay thế/dự thảo, {len(unknown_status_multi)} cần rà → {out}")
    return rows


def check():
    status = load_status()
    cites, _ = scan()
    warns = 0
    for key, st in status.items():
        rep = st.get("bi_thay_the_boi", "").strip()
        if not rep or key not in cites:
            continue
        # tìm dòng dẫn key mà không nhắc văn bản thay thế
        rep_num = re.search(r"(\d+/\d{4})", rep)
        rep_num = rep_num.group(1) if rep_num else rep
        for plugin, f in iter_plugin_files():
            if plugin not in cites[key]:
                continue
            for n, line in enumerate(f.read_text(encoding="utf-8", errors="ignore").split("\n"), 1):
                line_n = unicodedata.normalize("NFC", line)
                kind, rest = key.split(" ", 1)
                num = rest.split("/")[0]
                if re.search(rf"\b{num}/{rest.split('/')[1][:4]}", line_n) and rep_num not in line_n \
                        and not re.search(r"(thay thế|hết hiệu lực|lịch sử|cũ\b|trước |đã bị|bãi bỏ)", line_n, re.I):
                    print(f"[WARN thay-the] {plugin}/{f.relative_to(REPO / plugin / 'skills' / plugin)}:{n}: dẫn {key} không kèm {rep}")
                    warns += 1
    print(f"check_registry: {warns} WARN (không chặn CI)")
    return 0


if __name__ == "__main__":
    sys.exit(check() if "--check" in sys.argv else (build() and 0))
