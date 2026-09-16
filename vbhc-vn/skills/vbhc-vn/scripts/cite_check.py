#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cite_check.py — Đối chiếu MỌI số hiệu văn bản trong bản thảo với kho dữ kiện có kiểm chứng.

Vì sao có script này: lỗi nghiêm trọng nhất khi tham mưu là bịa số, bịa ngày, gán sai đối tượng
(Nhóm A trong reference/phong-tranh-sai-lam.md). Lỗi đó không chữa được bằng lời dặn, chỉ chữa
được bằng nguồn đối chiếu. Script quét mọi cụm "số …/…" trong file .docx, so với
data/vbpl.json (sinh từ registry/trang-thai.csv — lớp trạng thái người duy trì ghi sau khi mở
bản gốc), rồi chia làm ba nhóm:

  [KHỚP]     có trong kho, ngày tháng trong văn bản trùng kho → yên tâm.
  [LỆCH]     có trong kho nhưng ngày ban hành ghi trong văn bản KHÁC kho → phải sửa một bên.
  [CHƯA CÓ]  không có trong kho → Bạn xác nhận từ bản gốc rồi bổ sung vào
             registry/trang-thai.csv, hoặc sửa lại số hiệu nếu viết sai.

Script KHÔNG tự kết luận một số hiệu là bịa — kho chưa đầy đủ thì "chưa có trong kho" chỉ nghĩa
là chưa đối chiếu được. Không bao giờ tự sửa số hiệu trong file.

Cách chạy:
    python3 scripts/cite_check.py file.docx
    python3 scripts/cite_check.py file.docx --to-tim   # chép ra bản _cantra.docx, bôi TÍM
                                                       # các số hiệu chưa có trong kho
    python3 scripts/cite_check.py file.docx --json

Chữ tím 7030A0 là cơ chế đánh dấu nội dung chưa hoàn thiện đã quy ước với Bạn (Quy tắc bất
biến 27(c)); quy tắc R03 sẽ chặn không cho file còn chữ tím đi vào bản xuất bản.

Exit code: 0 = không có mục LỆCH, 1 = có LỆCH, 2 = lỗi sử dụng/đọc file.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import OrderedDict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from qa_rules import (  # noqa: E402
    Ctx, SO_VB, ma_tu_so_hieu, nfc, cut, _doc_vbpl,
)

try:
    from docx import Document
    from docx.shared import RGBColor
except ImportError:  # pragma: no cover
    print("LỖI: thiếu python-docx. Cài: pip install python-docx", file=sys.stderr)
    raise

TIM = RGBColor(0x70, 0x30, 0xA0)
NGAY_KE = re.compile(
    r"ngày\s+(\d{1,2})\s*(?:tháng\s*(\d{1,2})\s*năm\s*(\d{4})|/\s*(\d{1,2})\s*/\s*(\d{4}))")


def ngay_sau(text: str, tu: int) -> str | None:
    """Ngày ban hành ghi NGAY SAU một số hiệu, vd '… số 32/2024/NĐ-CP ngày 15/3/2024 …'."""
    m = NGAY_KE.search(text, tu, tu + 60)
    if not m:
        return None
    d = int(m.group(1))
    mo = int(m.group(2) or m.group(4))
    y = int(m.group(3) or m.group(5))
    return f"{y:04d}-{mo:02d}-{d:02d}"


def quet(path: Path) -> list[dict]:
    ctx = Ctx(path)
    doc = Document(str(path))
    ctx.build(doc)
    kho = _doc_vbpl()
    ra: OrderedDict[str, dict] = OrderedDict()
    for loc, t in ctx.texts:
        for m in SO_VB.finditer(t):
            so = m.group(1)
            ma = ma_tu_so_hieu(so)
            khoa = ma or so
            if khoa in ra:
                continue
            ghi = kho.get(nfc(ma)) if ma else None
            trong_vb = ngay_sau(t, m.end())
            if ghi is None:
                trang_thai = "CHƯA CÓ"
                ghi_chu = ("Chưa đối chiếu được — mở bản gốc xác nhận rồi bổ sung vào "
                           "registry/trang-thai.csv, hoặc sửa số hiệu nếu viết sai.")
            elif trong_vb and ghi.get("ngay_ban_hanh") and trong_vb != ghi["ngay_ban_hanh"]:
                trang_thai = "LỆCH"
                ghi_chu = (f"Văn bản ghi ngày ban hành {trong_vb}, kho ghi "
                           f"{ghi['ngay_ban_hanh']} — phải sửa một bên.")
            else:
                trang_thai = "KHỚP"
                phan = []
                if ghi.get("ngay_ban_hanh"):
                    phan.append(f"ban hành {ghi['ngay_ban_hanh']}")
                if ghi.get("ngay_hieu_luc"):
                    phan.append(f"hiệu lực {ghi['ngay_hieu_luc']}")
                if ghi.get("bi_thay_the_boi"):
                    phan.append(f"ĐÃ BỊ THAY THẾ bởi {ghi['bi_thay_the_boi']}")
                if ghi.get("bi_sua_doi_boi"):
                    phan.append(f"đã sửa đổi bởi {ghi['bi_sua_doi_boi']}")
                ghi_chu = "; ".join(phan) or "có trong kho, chưa ghi ngày"
            ra[khoa] = {"so_hieu": so, "ma": ma, "trang_thai": trang_thai,
                        "vi_tri": loc, "trich": cut(t, 70), "ghi_chu": ghi_chu}
    return list(ra.values())


def to_tim(path: Path, can_tra: set[str]) -> Path:
    """Chép file ra bản _cantra.docx và bôi TÍM các số hiệu chưa đối chiếu được."""
    doc = Document(str(path))

    def xu_ly(p):
        for r in p.runs:
            t = nfc(r.text)
            if any(s in t for s in can_tra):
                r.font.color.rgb = TIM

    for p in doc.paragraphs:
        xu_ly(p)
    for tb in doc.tables:
        for row in tb.rows:
            for c in row.cells:
                for p in c.paragraphs:
                    xu_ly(p)
    ra = path.with_name(path.stem + "_cantra.docx")
    doc.save(str(ra))
    return ra


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Đối chiếu số hiệu văn bản trong bản thảo với kho dữ kiện có kiểm chứng.",
        formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument("docx")
    ap.add_argument("--to-tim", action="store_true",
                    help="xuất thêm bản _cantra.docx bôi tím các số hiệu chưa có trong kho")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    p = Path(a.docx)
    if not p.exists():
        print(f"LỖI: không tìm thấy {p}", file=sys.stderr)
        return 2
    try:
        ds = quet(p)
    except Exception as e:
        print(f"LỖI đọc {p.name}: {type(e).__name__}: {e}", file=sys.stderr)
        return 2

    if a.json:
        print(json.dumps(ds, ensure_ascii=False, indent=2))
    else:
        print("=" * 66)
        print(f"ĐỐI CHIẾU SỐ HIỆU VĂN BẢN — {p.name}")
        print("=" * 66)
        if not ds:
            print("  Không tìm thấy số hiệu văn bản nào trong bản thảo.")
        for x in sorted(ds, key=lambda x: {"LỆCH": 0, "CHƯA CÓ": 1, "KHỚP": 2}[x["trang_thai"]]):
            print(f"  [{x['trang_thai']:8s}] {x['so_hieu']}")
            print(f"             {x['vi_tri']}: {x['trich']}")
            print(f"             → {x['ghi_chu']}")
        n = {k: sum(1 for x in ds if x["trang_thai"] == k)
             for k in ("KHỚP", "LỆCH", "CHƯA CÓ")}
        print(f"\nTỔNG: {len(ds)} số hiệu — khớp {n['KHỚP']}, lệch {n['LỆCH']}, "
              f"chưa có trong kho {n['CHƯA CÓ']}")

    if a.to_tim:
        can = {x["so_hieu"] for x in ds if x["trang_thai"] != "KHỚP"}
        if can:
            print(f"Đã bôi tím {len(can)} số hiệu → {to_tim(p, can)}")
        else:
            print("Không có số hiệu nào cần tra — không xuất bản bôi tím.")
    return 1 if any(x["trang_thai"] == "LỆCH" for x in ds) else 0


if __name__ == "__main__":
    sys.exit(main())
