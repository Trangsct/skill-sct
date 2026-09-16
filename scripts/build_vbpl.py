#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_vbpl.py — Sinh kho dữ kiện văn bản pháp luật cho plugin vbhc-vn.

Nguồn DUY NHẤT: registry/trang-thai.csv — lớp trạng thái do người duy trì ghi sau khi đã
đối chiếu bản gốc (ngày ban hành, hiệu lực, bị sửa đổi/thay thế bởi). Không lập kho thứ hai
để hai nguồn khỏi lệch nhau.

Đầu ra: vbhc-vn/skills/vbhc-vn/data/vbpl.json — dùng cho:
  - quy tắc R05 trong scripts/qa_rules.py (không viện dẫn văn bản chưa có hiệu lực tại ngày ký);
  - scripts/cite_check.py (đối chiếu mọi số hiệu văn bản trong bản thảo với kho).

Cách chạy (tại gốc kho skill-sct):
    python3 scripts/build_vbpl.py            # sinh lại vbpl.json
    python3 scripts/build_vbpl.py --check    # chỉ kiểm đã khớp chưa, không ghi

Exit code: 0 = ok, 1 = lệch (khi --check), 2 = lỗi dữ liệu nguồn.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

GOC = Path(__file__).resolve().parent.parent
NGUON = GOC / "registry" / "trang-thai.csv"
DICH = GOC / "vbhc-vn" / "skills" / "vbhc-vn" / "data" / "vbpl.json"

# Quy số hiệu → mã registry: TÁI DÙNG hàm trong plugin, không định nghĩa bản thứ hai.
sys.path.insert(0, str(GOC / "vbhc-vn" / "skills" / "vbhc-vn" / "scripts"))
from qa_rules import ma_tu_so_hieu  # noqa: E402  (dùng bởi scripts/cite_check.py và R05)

__all__ = ["ma_tu_so_hieu", "doc_ngay", "dung_kho"]


def doc_ngay(s: str) -> str | None:
    """'01/7/2026' → '2026-07-01'. Rỗng hoặc không đọc được → None (KHÔNG đoán).

    Nhận hai biến thể có trong registry:
      - khoảng hiệu lực '20/8/2026 → 28/02/2027' → lấy ngày BẮT ĐẦU;
      - ghi chú kèm '29/5/2026 (một phần)'       → lấy ngày, bỏ ghi chú.
    Mọi dạng khác trả None và được script báo ra, không đoán bừa.
    """
    s = (s or "").strip()
    if not s:
        return None
    s = re.split(r"→|->", s)[0].strip()
    s = re.sub(r"\s*\(.*$", "", s).strip()
    m = re.fullmatch(r"(\d{1,2})/(\d{1,2})/(\d{4})", s)
    if not m:
        return None
    d, mo, y = (int(x) for x in m.groups())
    if not (1 <= mo <= 12 and 1 <= d <= 31):
        return None
    return f"{y:04d}-{mo:02d}-{d:02d}"


def dung_kho() -> dict:
    if not NGUON.exists():
        print(f"LỖI: không có {NGUON}", file=sys.stderr)
        sys.exit(2)
    van_ban: dict[str, dict] = {}
    bo_qua: list[str] = []
    with NGUON.open(encoding="utf-8", newline="") as fh:
        for dong in csv.DictReader(fh):
            ma = (dong.get("ma") or "").strip()
            if not ma:
                continue
            hl = doc_ngay(dong.get("hieu_luc", ""))
            bh = doc_ngay(dong.get("ngay_ban_hanh", ""))
            if hl is None and (dong.get("hieu_luc") or "").strip():
                bo_qua.append(f"{ma}: hieu_luc {dong['hieu_luc']!r} không đọc được")
            ghi = {
                "ngay_ban_hanh": bh,
                "ngay_hieu_luc": hl,
                "bi_sua_doi_boi": (dong.get("bi_sua_doi_boi") or "").strip() or None,
                "bi_thay_the_boi": (dong.get("bi_thay_the_boi") or "").strip() or None,
                "ghi_chu": (dong.get("ghi_chu") or "").strip() or None,
            }
            van_ban[ma] = {k: v for k, v in ghi.items() if v is not None}
    return {
        "_doc": ("Kho dữ kiện văn bản pháp luật có kiểm chứng. SINH TỰ ĐỘNG bởi "
                 "scripts/build_vbpl.py từ registry/trang-thai.csv — KHÔNG SỬA TAY file này. "
                 "Muốn thêm/sửa một văn bản: sửa registry/trang-thai.csv rồi chạy lại script."),
        "_nguon": "registry/trang-thai.csv",
        "_quy_uoc": {
            "khoa": ("Mã như trong registry, vd 'NĐ 32/2024', 'Luật 42/2024', "
                     "'QĐ 2867/QĐ-UBND'. Hàm ma_tu_so_hieu() trong scripts/build_vbpl.py quy "
                     "một số hiệu trong văn bản về mã này."),
            "ngay": "YYYY-MM-DD; thiếu trường nghĩa là CHƯA kiểm chứng — R05 bỏ qua, không báo.",
        },
        "_canh_bao": ("Không ghi số, ngày từ trí nhớ (Nhóm A). registry/trang-thai.csv chỉ được "
                      "ghi khi đã mở bản gốc đối chiếu."),
        "van_ban": dict(sorted(van_ban.items())),
        "_bo_qua": bo_qua,
    }


def main() -> int:
    kho = dung_kho()
    if kho["_bo_qua"]:
        print("CẢNH BÁO — dòng nguồn không đọc được ngày, đã bỏ trống (không đoán):")
        for x in kho["_bo_qua"]:
            print("  • " + x)
    moi = json.dumps(kho, ensure_ascii=False, indent=2) + "\n"
    co_hl = sum(1 for v in kho["van_ban"].values() if v.get("ngay_hieu_luc"))
    if "--check" in sys.argv:
        cu = DICH.read_text(encoding="utf-8") if DICH.exists() else ""
        if cu != moi:
            print("LỆCH: data/vbpl.json chưa khớp registry/trang-thai.csv — "
                  "chạy `python3 scripts/build_vbpl.py` rồi commit cùng.", file=sys.stderr)
            return 1
        print(f"vbpl.json đã khớp — {len(kho['van_ban'])} văn bản, {co_hl} có ngày hiệu lực")
        return 0
    DICH.write_text(moi, encoding="utf-8")
    print(f"Đã ghi {DICH.relative_to(GOC)} — {len(kho['van_ban'])} văn bản, "
          f"{co_hl} có ngày hiệu lực")
    return 0


if __name__ == "__main__":
    sys.exit(main())
