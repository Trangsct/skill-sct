#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""nap_vbpl_data360x.py — Nạp đề xuất văn bản pháp luật CÔNG KHAI từ Data360X vào
registry/trang-thai.csv, rồi sinh lại data/vbpl.json của plugin vbhc-vn.

Đầu vào: file CSV do `vlncn-laocai/scripts/de-xuat-vbpl.py` sinh (cột ma, so_ky_hieu,
ngay_ban_hanh, co_quan, trich_yeu, nguon). Chỉ chứa văn bản của cơ quan ban hành công khai
(Chính phủ, Bộ, UBND tỉnh) — không có văn bản nội bộ của Sở.

Quy tắc nạp:
  - Mã đã có trong trang-thai.csv → KHÔNG ghi đè (dòng người duy trì đã đối chiếu bản gốc).
    Riêng dòng cũ chưa có ngay_ban_hanh thì điền bổ sung từ Data360X và ghi chú nguồn.
  - Mã chưa có → thêm dòng mới với ngay_ban_hanh; hieu_luc ĐỂ TRỐNG (Data360X không có,
    không đoán); ghi_chu ghi "nguồn Data360X <url>; chưa kiểm ngày hiệu lực".
  - Sau khi nạp: chạy scripts/build_vbpl.py để sinh lại vbpl.json.

Cách chạy (gốc kho skill-sct):
    python3 scripts/nap_vbpl_data360x.py ../vlncn-laocai/theo-doi/de-xuat-vbpl.csv
    python3 scripts/nap_vbpl_data360x.py <csv> --xem     # chỉ liệt kê, không ghi
"""
import csv, subprocess, sys
from pathlib import Path

GOC = Path(__file__).resolve().parent.parent
TT = GOC / "registry" / "trang-thai.csv"


def main():
    if len(sys.argv) < 2:
        print(__doc__); return 2
    src = Path(sys.argv[1]); xem = "--xem" in sys.argv
    if not src.exists():
        print(f"LỖI: không có {src}", file=sys.stderr); return 2
    with TT.open(encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh); cot = rd.fieldnames; cu = list(rd)
    co = {r["ma"]: r for r in cu}
    them, bo_sung = [], []
    for r in csv.DictReader(src.open(encoding="utf-8", newline="")):
        ma, ngay = r["ma"].strip(), r["ngay_ban_hanh"].strip()
        if not ma or not ngay:
            continue
        ghi = f"nguồn Data360X {r.get('nguon','')}; chưa kiểm ngày hiệu lực; {r.get('trich_yeu','')[:90]}"
        if ma in co:
            d = co[ma]
            if not (d.get("ngay_ban_hanh") or "").strip():
                d["ngay_ban_hanh"] = ngay
                d["ghi_chu"] = ((d.get("ghi_chu") or "").rstrip("; ") + f"; ngày ban hành theo Data360X {r.get('nguon','')}").strip("; ")
                bo_sung.append(ma)
            continue
        dong = {c: "" for c in cot}
        dong.update({"ma": ma, "ngay_ban_hanh": ngay, "ghi_chu": ghi})
        cu.append(dong); co[ma] = dong; them.append(ma)
    print(f"Thêm mới {len(them)}, bổ sung ngày ban hành {len(bo_sung)}, tổng {len(cu)} dòng")
    for m in them[:10]: print("  +", m)
    for m in bo_sung: print("  ~", m)
    if xem:
        return 0
    with TT.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cot); w.writeheader(); w.writerows(cu)
    r = subprocess.run([sys.executable, str(GOC / "scripts" / "build_vbpl.py")], capture_output=True, text=True)
    print(r.stdout.strip() or r.stderr.strip())
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
