#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tim_van_ban.py — tìm văn bản gốc trong TOÀN BỘ các plugin trước khi kết luận "chưa có" (Bạn chốt 09/10/2026).

    python3 scripts/tim_van_ban.py "QCVN 01:2019"
    python3 scripts/tim_van_ban.py "303/2026"
    python3 scripts/tim_van_ban.py "khoảng cách an toàn do đất, đá văng" --tat-ca

Tham số là số hiệu hoặc cụm từ. Chuẩn hóa NFC cả truy vấn lẫn dữ liệu, không phân biệt hoa thường,
coi các dấu ngăn (khoảng trắng / : . - _ ,) là tương đương và đ ~ d, nên "QCVN 01:2019", "QCVN-01-2019",
"qcvn 01 2019" tìm được như nhau. Ba lớp tìm, in theo thứ tự:
  1. DANH MỤC — DANH-MUC-VAN-BAN-GOC.csv ở gốc kho (hoặc van-ban-goc/00-DANH-MUC-CHUNG.md của plugin khi
     phiên chỉ có gói plugin): khớp số hiệu, tên hoặc đường dẫn.
  2. TOÀN VĂN — mọi bản .txt/.md trong van-ban-goc/ và vi-du-thuc-te/ của MỌI plugin: in tệp, plugin,
     số dòng và đoạn trích 300 ký tự quanh chỗ khớp (mặc định tối đa 3 chỗ/tệp; --tat-ca để in hết).
  3. NHẮC ĐẾN — SKILL.md, references/, mau-van-ban/ (chỉ là tóm tắt, không phải bản gốc).

Chạy được ở cả hai bố cục: gốc kho skill-sct (<plugin>/skills/<plugin>/van-ban-goc) và gói plugin trên
claude.ai (/mnt/skills/plugins/<plugin>:<plugin>/van-ban-goc). Bản chép trong scripts/ của từng plugin do
build_so_cai_van_ban_goc.py đồng bộ từ scripts/tim_van_ban.py ở gốc kho — không sửa bản chép.

Thoát mã 0 khi thấy ở lớp 1 hoặc 2; mã 1 khi chỉ có lớp 3 hoặc không thấy. CHỈ khi mã 1 mới được nói
"chưa có bản gốc trong kho" và hướng dẫn Bạn nạp qua Hộp thư _inbox/ trên GitHub.
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
import unicodedata
from pathlib import Path

CSV_NAME = "DANH-MUC-VAN-BAN-GOC.csv"
MD_NAME = "00-DANH-MUC-CHUNG.md"
SEP = r"[\s/:.\-_,;]*"
NGAN = 150  # ký tự mỗi bên quanh chỗ khớp → đoạn trích ~300 ký tự


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s)


def regex_tu_truy_van(q: str) -> re.Pattern:
    q = nfc(q).casefold()
    parts = [p for p in re.split(r"[\s/:.\-_,;]+", q) if p]
    toks = []
    for p in parts:
        t = re.escape(p).replace("đ", "[đd]").replace("d", "[dđ]")
        toks.append(t)
    # biên: "303/2026" không khớp "1303/2026" hay "30-3-2026"; "Bảng 1" không khớp "Bảng 10"
    return re.compile(r"(?<![0-9a-zđA-ZĐ])" + SEP.join(toks) + r"(?![0-9])", re.I)


# ----------------------------------------------------------------------------- bố cục
def tim_goc(script: Path) -> tuple[Path | None, Path, Path | None]:
    """Trả về (gốc kho có CSV hoặc None, gốc chứa các plugin, thư mục skill chứa script khi ở trong gói)."""
    skill_dir = None
    for base in (script.parent, Path.cwd()):
        for d in [base, *base.parents]:
            if (d / CSV_NAME).exists():
                return d, d, None
    # Không có CSV ở gốc: đang ở trong gói plugin (…/<plugin>/scripts/tim_van_ban.py hoặc …/<plugin>/skills/<plugin>/scripts/)
    if script.parent.name == "scripts":
        skill_dir = script.parent.parent
    base = skill_dir if skill_dir else Path.cwd()
    # gốc chứa các plugin: thư mục cha mà dưới nó có nhiều thư mục mang van-ban-goc/
    for d in [base, *base.parents]:
        if any(d.glob("*/van-ban-goc")) or any(d.glob("*/skills/*/van-ban-goc")):
            return None, d, skill_dir
    return None, base, skill_dir


def thu_muc_du_lieu(root: Path, ten: str) -> list[Path]:
    out = list(root.glob(f"*/skills/*/{ten}")) + list(root.glob(f"*/{ten}"))
    seen, uniq = set(), []
    for d in out:
        r = d.resolve()
        if r not in seen and r.is_dir():
            seen.add(r)
            uniq.append(d)
    return sorted(uniq)


def ten_plugin(p: Path, root: Path) -> str:
    try:
        rel = p.resolve().relative_to(root.resolve())
    except ValueError:
        return p.parts[0] if p.parts else "?"
    first = rel.parts[0]
    return first.split(":")[0]


# ----------------------------------------------------------------------------- lớp 1: danh mục
def doc_danh_muc(repo: Path | None, skill_dir: Path | None, root: Path) -> list[dict]:
    if repo and (repo / CSV_NAME).exists():
        with (repo / CSV_NAME).open(encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f))
    ung_vien = []
    if skill_dir:
        ung_vien.append(skill_dir / "van-ban-goc" / MD_NAME)
    ung_vien += [d / MD_NAME for d in thu_muc_du_lieu(root, "van-ban-goc")]
    for md in ung_vien:
        if md.exists():
            rows = []
            for line in md.read_text(encoding="utf-8", errors="replace").split("\n"):
                if not line.startswith("| ") or line.startswith("| Số hiệu") or line.startswith("|---"):
                    continue
                cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
                if len(cells) >= 5:
                    rows.append({"so_hieu": cells[0], "ngay_ban_hanh": cells[1], "ten": cells[2].replace("\\|", "|"),
                                 "plugin_chu": cells[3], "duong_dan": cells[4].strip("`").replace("\\|", "|"),
                                 "co_txt": cells[5] if len(cells) > 5 else ""})
            return rows
    return []


def tim_danh_muc(q: str, rows: list[dict]) -> list[dict]:
    rx = regex_tu_truy_van(q)
    out = []
    for r in rows:
        chuoi = " ".join((r.get("so_hieu", ""), r.get("ten", ""), r.get("duong_dan", "")))
        if rx.search(nfc(chuoi).casefold()):
            out.append(r)
    return out


# ----------------------------------------------------------------------------- lớp 2, 3: toàn văn
def tim_trong_tep(f: Path, rx: re.Pattern, toi_da: int) -> list[tuple[int, str]]:
    try:
        text = nfc(f.read_text(encoding="utf-8", errors="replace"))
    except OSError:
        return []
    low = text.casefold()
    hits = []
    for m in rx.finditer(low):
        a, b = max(0, m.start() - NGAN), min(len(text), m.end() + NGAN)
        dong = low.count("\n", 0, m.start()) + 1
        trich = text[a:b].replace("\n", " ")
        trich = re.sub(r"\s{2,}", " ", trich).strip()
        hits.append((dong, trich))
        if toi_da and len(hits) >= toi_da:
            break
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description="Tìm văn bản gốc trong mọi plugin")
    ap.add_argument("truy_van", help="số hiệu hoặc cụm từ")
    ap.add_argument("--tat-ca", action="store_true", help="in mọi chỗ khớp trong từng tệp (mặc định 3)")
    ap.add_argument("--khong-nhac-den", action="store_true", help="bỏ lớp 3 (reference, SKILL.md)")
    ap.add_argument("--trong", help="cụm từ thứ hai: chỉ tìm trong toàn văn các văn bản đã khớp ở lớp 1 (ví dụ --trong \"Bảng 1\")")
    a = ap.parse_args()
    q = a.truy_van.strip()
    if not q:
        print("Thiếu truy vấn.")
        return 2
    script = Path(__file__).resolve()
    repo, root, skill_dir = tim_goc(script)
    rx = regex_tu_truy_van(q)
    toi_da = 0 if a.tat_ca else 3

    print(f"Truy vấn: {q}")
    print(f"Phạm vi: {root}" + (" (gốc kho)" if repo else " (gói plugin)"))

    rows = doc_danh_muc(repo, skill_dir, root)
    dm = tim_danh_muc(q, rows)
    print(f"\n[1] DANH MỤC ({len(rows)} mục): {len(dm)} khớp")
    for r in dm:
        print(f"  - {r.get('so_hieu') or '—'} | {r.get('ngay_ban_hanh') or '—'} | {r.get('ten')}")
        print(f"      plugin {r.get('plugin_chu')} | {r.get('duong_dan')} | .txt: {r.get('co_txt')}")

    tep_goc = []
    for ten in ("van-ban-goc", "vi-du-thuc-te"):
        for d in thu_muc_du_lieu(root, ten):
            tep_goc += [f for f in d.rglob("*") if f.suffix.lower() in (".txt", ".md") and f.name != MD_NAME]
    # .txt/.md của các mục khớp danh mục xếp lên đầu
    uu_tien = set()
    for r in dm:
        rel = r.get("duong_dan", "")
        for f in tep_goc:
            try:
                frel = f.relative_to(root).as_posix()
            except ValueError:
                continue
            if frel.rsplit(".", 1)[0] == rel.rsplit(".", 1)[0] or frel.rsplit(".", 1)[0] == rel.replace("/skills/", "/", 1).rsplit(".", 1)[0]:
                uu_tien.add(f)
    if a.trong:
        rx2 = regex_tu_truy_van(a.trong)
        print(f"\n[1b] CỤM \"{a.trong}\" trong toàn văn {len(uu_tien)} văn bản khớp danh mục:")
        for f in sorted(uu_tien):
            for dong, trich in tim_trong_tep(f, rx2, toi_da):
                print(f"  - {f.relative_to(root)} dòng {dong}: …{trich}…")
    so_tep = 0
    print(f"\n[2] TOÀN VĂN ({len(tep_goc)} tệp .txt/.md trong van-ban-goc, vi-du-thuc-te; tệp của mục khớp danh mục in trước):")
    for f in sorted(uu_tien) + sorted(set(tep_goc) - uu_tien):
        hits = tim_trong_tep(f, rx, toi_da)
        if not hits:
            continue
        so_tep += 1
        print(f"  - {ten_plugin(f, root)} | {f.relative_to(root)}")
        for dong, trich in hits:
            print(f"      dòng {dong}: …{trich}…")
    if so_tep == 0:
        print("  (không thấy)")

    so_nhac = 0
    if not a.khong_nhac_den:
        tep_ref = []
        for ten in ("references", "mau-van-ban", "checklists"):
            for d in thu_muc_du_lieu(root, ten):
                tep_ref += [f for f in d.rglob("*.md")]
        tep_ref += list(root.glob("*/skills/*/SKILL.md")) + list(root.glob("*/SKILL.md"))
        print(f"\n[3] NHẮC ĐẾN trong SKILL.md / references / mẫu (tóm tắt, KHÔNG phải bản gốc):")
        for f in sorted(set(tep_ref)):
            hits = tim_trong_tep(f, rx, 1)
            if not hits:
                continue
            so_nhac += 1
            print(f"  - {ten_plugin(f, root)} | {f.relative_to(root)} | dòng {hits[0][0]}: …{hits[0][1][:200]}…")
        if so_nhac == 0:
            print("  (không thấy)")

    if dm or so_tep:
        print(f"\nKẾT LUẬN: CÓ trong kho — mở bản .txt/.md ở trên để trích nguyên văn (bản gốc ≥ 3 MB chỉ có trên GitHub).")
        return 0
    print("\nKẾT LUẬN: KHÔNG thấy trong danh mục lẫn toàn văn" +
          (f"; {so_nhac} tài liệu có nhắc đến (tóm tắt)." if so_nhac else ".") +
          "\nChỉ lúc này mới được nói \"chưa có bản gốc trong kho\"; hướng dẫn Bạn nạp qua Hộp thư _inbox/ trên GitHub "
          "(github.com/Trangsct/skill-sct → _inbox → Add file → Upload files).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
