#!/usr/bin/env python3
"""
fix_quoc_hieu.py — Chuẩn hóa Quốc hiệu / Tiêu ngữ trong file .docx theo quy ước cố định của Bạn:

  - "CỘNG HOÀ XÃ HỘI CHỦ NGHĨA VIỆT NAM"  →  "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM"
  - "Độc lập - Tự do - Hạnh phúc" (gạch nối "-")  →  "Độc lập – Tự do – Hạnh phúc" (en dash "–")

Chỉ sửa TEXT trong từng node <w:t>, KHÔNG động vào run/paragraph/shape → giữ nguyên Line
shape, định dạng, relationships. Sửa in-place (ghi đè file) hoặc --out để ghi file mới.

Dùng:
    python3 scripts/fix_quoc_hieu.py <file.docx> [--out <file2.docx>] [--check]

    --check : chỉ báo có/không vi phạm, exit 1 nếu có, không sửa.

Khi nào chạy: Chế độ B (sửa mẫu thật trong examples/ hoặc file người dùng tải lên) — mẫu thật
nhiều file còn "HOÀ"/gạch nối; chạy ngay sau khi build, trước qa_all.py.
"""
import re
import sys
import unicodedata
import zipfile
from pathlib import Path

RULES = [
    (re.compile(r"CỘNG\s+HOÀ"), "CỘNG HÒA"),
    (re.compile(r"Độc\s+lập\s*-\s*Tự\s+do\s*-\s*Hạnh\s+phúc"), "Độc lập – Tự do – Hạnh phúc"),
]
T_NODE = re.compile(r"(<w:t(?:\s[^>]*)?>)(.*?)(</w:t>)", re.S)


def scan_text(xml: str):
    """Trả về danh sách vi phạm tìm thấy trong text đã ghép (NFC)."""
    plain = unicodedata.normalize("NFC", re.sub(r"<[^>]+>", "", xml))
    found = []
    for rx, _ in RULES:
        if rx.search(plain):
            found.append(rx.pattern)
    return found


def fix_xml(xml: str):
    """Sửa từng <w:t>; đếm số thay thế. Text được chuẩn NFC trước khi so khớp."""
    n = 0

    def _sub(m):
        nonlocal n
        inner = unicodedata.normalize("NFC", m.group(2))
        new = inner
        for rx, rep in RULES:
            new, k = rx.subn(rep, new)
            n += k
        return m.group(1) + new + m.group(3)

    return T_NODE.sub(_sub, xml), n


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    src = Path(args[0])
    out = Path(args[args.index("--out") + 1]) if "--out" in args else src
    check_only = "--check" in args
    if not src.exists() or src.suffix.lower() != ".docx":
        print(f"LỖI: cần file .docx tồn tại: {src}")
        sys.exit(2)

    with zipfile.ZipFile(src) as z:
        parts = {i.filename: z.read(i.filename) for i in z.infolist()}
        infos = z.infolist()

    targets = [k for k in parts if k.startswith("word/") and k.endswith(".xml")
               and (k == "word/document.xml" or "header" in k or "footer" in k)]
    total = 0
    viol = []
    for k in targets:
        xml = parts[k].decode("utf-8")
        v = scan_text(xml)
        if v:
            viol.append((k, v))
        if not check_only:
            new_xml, n = fix_xml(xml)
            if n:
                parts[k] = new_xml.encode("utf-8")
                total += n

    if check_only:
        if viol:
            for k, v in viol:
                print(f"[VI PHẠM] {k}: {', '.join(v)}")
            sys.exit(1)
        print("OK: Quốc hiệu/Tiêu ngữ đúng quy ước (CỘNG HÒA, en dash).")
        sys.exit(0)

    if total == 0:
        print("Không có gì cần sửa.")
        if out != src:
            out.write_bytes(src.read_bytes())
        return
    # Ghi lại zip giữ nguyên thứ tự và compression của từng entry
    tmp = out.with_suffix(".docx.tmp")
    with zipfile.ZipFile(tmp, "w") as zo:
        for i in infos:
            zo.writestr(i, parts[i.filename], compress_type=i.compress_type)
    tmp.replace(out)
    # Kiểm lại sau sửa: nếu Quốc hiệu bị tách qua nhiều run thì regex trên từng <w:t> không bắt được
    with zipfile.ZipFile(out) as z:
        left = [k for k in targets if scan_text(z.read(k).decode("utf-8"))]
    print(f"Đã sửa {total} chỗ → {out}")
    if left:
        print("⚠ CÒN SÓT (Quốc hiệu/Tiêu ngữ bị tách qua nhiều run, cần sửa tay bằng str_replace "
              "trong document.xml): " + ", ".join(left))
        sys.exit(1)


if __name__ == "__main__":
    main()
