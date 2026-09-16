#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cham_case.py — Chấm một sản phẩm .docx theo tieu-chi.txt của một case lớp 2.

Cú pháp tieu-chi.txt (mỗi dòng một tiêu chí, '#' là ghi chú):
    require: <chuỗi bắt buộc xuất hiện>
    forbid:  <chuỗi cấm xuất hiện>
    rule-pass: <danh sách mã quy tắc qa_rules.py phải không có FAIL>
    trang:   <khoảng số trang chấp nhận được, vd 1-2>
    ghi-chu: <ghi chú cho người duyệt — KHÔNG chấm bằng máy>

So khớp chuỗi luôn chuẩn hóa NFC hai phía (Quy tắc bất biến 15) và không phân biệt
hoa thường. Exit code: 0 = ĐẠT, 1 = KHÔNG ĐẠT, 2 = lỗi sử dụng.
"""
import re
import subprocess
import sys
import unicodedata
import zipfile
from pathlib import Path

PLUGIN = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PLUGIN / "scripts"))
from qa_rules import chay, FAIL  # noqa: E402


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s or "").lower()


def toan_van(p: Path) -> str:
    with zipfile.ZipFile(p) as z:
        x = z.read("word/document.xml").decode("utf-8", "replace")
    x = re.sub(r"</w:p>", "\n", x)
    return nfc(re.sub(r"<[^>]+>", "", x))


def so_trang(p: Path) -> int | None:
    """Số trang thật — render bằng LibreOffice rồi đếm trang PDF."""
    out = PLUGIN / "tests" / "_ket-qua" / "_render"
    out.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf",
                        "--outdir", str(out), str(p)],
                       capture_output=True, timeout=180, check=True)
        pdf = out / (p.stem + ".pdf")
        r = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True)
        m = re.search(r"^Pages:\s*(\d+)", r.stdout, re.M)
        return int(m.group(1)) if m else None
    except (subprocess.SubprocessError, OSError):
        return None


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    docx, tc = Path(sys.argv[1]), Path(sys.argv[2])
    if not docx.exists() or not tc.exists():
        print(f"LỖI: thiếu {docx if not docx.exists() else tc}", file=sys.stderr)
        return 2

    van = toan_van(docx)
    hong: list[str] = []
    ma_can: set[str] = set()
    khoang_trang = None

    for ln in tc.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        khoa, _, gt = ln.partition(":")
        khoa, gt = khoa.strip().lower(), gt.strip()
        if khoa == "require":
            if nfc(gt) not in van:
                hong.append(f"THIẾU chuỗi bắt buộc: {gt!r}")
        elif khoa == "forbid":
            if nfc(gt) in van:
                hong.append(f"CÒN chuỗi cấm: {gt!r}")
        elif khoa == "rule-pass":
            ma_can |= set(gt.split())
        elif khoa == "trang":
            m = re.match(r"(\d+)\s*-\s*(\d+)$", gt)
            if m:
                khoang_trang = (int(m.group(1)), int(m.group(2)))
        elif khoa == "ghi-chu":
            pass
        else:
            hong.append(f"tieu-chi.txt có khóa lạ: {khoa!r} — sửa file tiêu chí")

    if ma_can:
        fails = [x for x in chay(docx) if x.level == FAIL and x.code in ma_can]
        for x in fails:
            hong.append(f"quy tắc {x.code} FAIL — {x.loc}: {x.excerpt}")

    if khoang_trang:
        n = so_trang(docx)
        if n is None:
            print("   (không render được để đếm trang — bỏ qua tiêu chí trang)")
        elif not (khoang_trang[0] <= n <= khoang_trang[1]):
            hong.append(f"số trang {n}, ngoài khoảng {khoang_trang[0]}-{khoang_trang[1]}")

    if hong:
        print("   KHÔNG ĐẠT:")
        for h in hong:
            print("      • " + h)
        return 1
    print("   ĐẠT")
    return 0


if __name__ == "__main__":
    sys.exit(main())
