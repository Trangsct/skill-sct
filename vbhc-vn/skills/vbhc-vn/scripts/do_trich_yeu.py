#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""do_trich_yeu.py — Đo khối trích yếu "V/v" của công văn trên bản dựng PDF (Bạn chốt 10/11/2026).

Quy ước trình bày trích yếu công văn (sổ lỗi L015, quy tắc R27):
  1. Một đoạn liền, tự xuống dòng (R27 kiểm trong .docx); tối đa 3-4 dòng.
  2. Tâm khối trích yếu trùng tâm khối tên cơ quan ở trên (vd "UBND TỈNH LÀO CAI / SỞ CÔNG THƯƠNG").
  3. Dòng dài nhất rộng hơn khối tên cơ quan mỗi bên khoảng 0,5-1 cm (trích yếu ngắn hơn thì thôi).
  4. Mép phải không chạm đường thẳng đứng của chữ "CỘNG" (Quốc hiệu) — cách tối thiểu khoảng 0,2 cm.
  5. Dòng cuối không rớt riêng một chữ.

Cách chỉnh khi chưa đạt: nới ô trích yếu (thêm một cột lưới hẹp bên phải cho ô V/v gộp vào), đặt lề trái âm
và lề phải dương cho đoạn trích yếu để dịch tâm; KHÔNG xuống dòng tay, không dùng khoảng trắng không ngắt.
Thông số đã dùng cho mẫu công văn của Sở có lưới 3119 + 236 + 5820 twip: thêm cột 283 twip (0,5 cm), lề trái
đoạn -18,2 pt, lề phải +8 pt → 3 dòng, lệch tâm 0 pt, rộng hơn khối tên cơ quan 0,95 cm mỗi bên, cách "CỘNG"
0,4 cm. Lưới khác thì chỉnh rồi đo lại bằng script này.

Chạy:  python3 scripts/do_trich_yeu.py <file>.docx|.pdf        (mã thoát 1 khi có mục KHÔNG ĐẠT)
Cần: libreoffice (soffice) để dựng PDF từ .docx, poppler-utils (pdftotext).
"""
from __future__ import annotations

import collections
import re
import subprocess
import sys
import tempfile
from pathlib import Path

PT_CM = 28.3465


def dung_pdf(p: Path, tam: Path) -> Path:
    if p.suffix.lower() == ".pdf":
        return p
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(tam), str(p)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
    return tam / (p.stem + ".pdf")


def doc_tu(pdf: Path):
    xml = subprocess.run(["pdftotext", "-bbox", "-l", "1", str(pdf), "-"], check=True,
                         capture_output=True, text=True).stdout
    return [(float(a), float(b), float(c), w) for a, b, c, w in re.findall(
        r'xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="[\d.]+">([^<]*)<', xml)]


def do(p: Path) -> int:
    with tempfile.TemporaryDirectory() as t:
        tu = doc_tu(dung_pdf(p, Path(t)))
    cong = [w for w in tu if w[3] == "CỘNG"]
    vv = [w for w in tu if w[3].startswith("V/v")]
    if not cong or not vv:
        print("Không thấy chữ 'CỘNG' hoặc dòng 'V/v' ở trang 1 — không phải công văn có trích yếu ở bảng đầu trang.")
        return 0
    x_cong, y_cong = cong[0][0], cong[0][1]
    y_vv = vv[0][1]
    dong = collections.defaultdict(list)
    for w in tu:
        dong[round(w[1])].append(w)
    ys = sorted(dong)
    # khối tên cơ quan: các dòng từ dòng Quốc hiệu tới trước dòng "Số:", phần nằm bên trái chữ CỘNG
    co_quan = []
    for y in ys:
        if y < round(y_cong) - 2 or y >= round(y_vv):
            continue
        trai = [w for w in dong[y] if w[2] < x_cong]
        if not trai or trai[0][3].startswith("Số"):
            continue
        co_quan.append((min(w[0] for w in trai), max(w[2] for w in trai)))
    # khối trích yếu: từ dòng V/v, các dòng liền nhau (cách dưới 1,6 lần bước dòng), dừng ở "Kính"
    ty, truoc, buoc = [], None, None
    for y in ys:
        if y < round(y_vv):
            continue
        ws = dong[y]
        if ws[0][3].startswith("Kính"):
            break
        if truoc is not None:
            if buoc is None:
                buoc = y - truoc
            if y - truoc > 1.6 * buoc:
                break
        # dòng trích yếu có thể cùng hàng với "…, ngày … tháng … năm" ở cột phải: chỉ lấy cụm chữ liền nhau từ trái,
        # dừng ở khoảng hở lớn hơn 25 pt
        ws = sorted(ws)
        cum = [ws[0]]
        for w in ws[1:]:
            if w[0] - cum[-1][2] > 25:
                break
            cum.append(w)
        ty.append((cum[0][0], cum[-1][2], len(cum)))
        truoc = y
    if not co_quan or not ty:
        print("Không tách được khối tên cơ quan hoặc khối trích yếu.")
        return 0
    cq_t, cq_p = min(a for a, _ in co_quan), max(b for _, b in co_quan)
    ty_t, ty_p = min(a for a, _, _ in ty), max(b for _, b, _ in ty)
    tam_cq = (cq_t + cq_p) / 2
    # tâm trích yếu lấy theo dòng dài nhất (đoạn căn giữa nên mọi dòng cùng tâm)
    dai = max(ty, key=lambda d: d[1] - d[0])
    tam_ty = (dai[0] + dai[1]) / 2
    lech = tam_ty - tam_cq
    hon_trai, hon_phai = (cq_t - ty_t) / PT_CM, (ty_p - cq_p) / PT_CM
    cach_cong = (x_cong - ty_p) / PT_CM
    loi = 0

    def muc(ok, ten, gia_tri):
        nonlocal loi
        loi += 0 if ok else 1
        print(f"  [{'ĐẠT' if ok else 'KHÔNG ĐẠT'}] {ten}: {gia_tri}")

    print(f"ĐO TRÍCH YẾU — {p.name}")
    muc(len(ty) <= 4, "Số dòng (tối đa 3-4)", len(ty))
    if len(ty) == 1:
        # trích yếu một dòng ở mẫu căn đều hai bên (công văn nội bộ phòng) nằm sát trái — không tính lỗi
        print(f"  [thông tin] Trích yếu một dòng, lệch tâm {lech:+.1f} pt (không xét)")
    else:
        muc(abs(lech) <= 3, "Lệch tâm so với khối tên cơ quan (≤ 3 pt)", f"{lech:+.1f} pt")
    muc(cach_cong >= 0.2, "Mép phải cách đường thẳng đứng chữ 'CỘNG' (≥ 0,2 cm)", f"{cach_cong:.2f} cm")
    muc(not (len(ty) > 1 and ty[-1][2] == 1), "Dòng cuối không rớt riêng một chữ", f"{ty[-1][2]} chữ")
    print(f"  [thông tin] Rộng hơn khối tên cơ quan: trái {hon_trai:.2f} cm, phải {hon_phai:.2f} cm "
          f"(mong muốn 0,5-1 cm mỗi bên khi trích yếu đủ dài)")
    return 1 if loi else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(do(Path(sys.argv[1])))
