#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""run_regression.py — Bộ kiểm thử hồi quy LỚP 1 của plugin vbhc-vn.

Hoàn toàn tất định, KHÔNG gọi mô hình, chạy được trên GitHub Actions.
Nâng cấp plugin làm hỏng thứ đang đúng thì lệnh này đỏ.

Kiểm hai chiều:
  1. MẪU THẬT PHẢI SẠCH — mọi file trong examples/ không được có FAIL nào.
     Số WARN của từng file được chốt trong tests/baseline-warn.json; phát sinh WARN mới
     cũng là đỏ (quy tắc mới bắt nhầm mẫu thật), trừ khi cập nhật baseline có chủ đích.
  3. (tùy chọn --voi-qa-all) qa_all.py trên mẫu thật không được SINH THÊM tag FAIL nào so
     với tests/baseline-qa-all.json. Baseline này ghi nhận nợ kỹ thuật có sẵn từ trước đợt
     2.23.0 (SZ13, SIGSPACE, LINES, HDR-BR trên 24/26 mẫu) — xem mục D.4 rule-inventory.md.

  2. FILE LỖI PHẢI BỊ BẮT — mỗi file trong tests/fail/ phải bắt ĐÚNG và ĐỦ các mã ghi
     trong file .expect cùng tên, và KHÔNG được sinh thêm mã FAIL nào ngoài danh sách
     cho phép (= mã kỳ vọng + các mã vốn có của chính mẫu thật gốc ghi ở dòng "nguon:").

Cách chạy:
    python3 tests/run_regression.py              # chạy đủ
    python3 tests/run_regression.py --cap-nhat-baseline   # chốt lại baseline WARN
    python3 tests/run_regression.py -v           # in chi tiết từng phát hiện

Exit code: 0 = xanh, 1 = có kỳ vọng sai.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

PLUGIN = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PLUGIN / "scripts"))

from qa_rules import chay, FAIL, WARN  # noqa: E402

TESTS = PLUGIN / "tests"
BASELINE = TESTS / "baseline-warn.json"
BASELINE_QA = TESTS / "baseline-qa-all.json"
TAG_FAIL = re.compile(r"^\[FAIL ([A-Z0-9\-]+)\]")


def tags_qa_all(f: Path) -> list[str]:
    """Các tag FAIL mà qa_all.py báo trên một file (cần LibreOffice để render PDF)."""
    r = subprocess.run(
        [sys.executable, str(PLUGIN / "scripts" / "qa_all.py"), str(f), "--no-image"],
        capture_output=True, text=True, timeout=300)
    return sorted({m.group(1) for m in (TAG_FAIL.match(ln) for ln in r.stdout.splitlines()) if m})


def ma_muc(ds) -> set[str]:
    return {f"{x.code} {x.level}" for x in ds}


def doc_expect(p: Path) -> tuple[str | None, set[str]]:
    nguon, ma = None, set()
    for ln in p.read_text(encoding="utf-8").splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("#"):
            continue
        if ln.startswith("nguon:"):
            nguon = ln.split(":", 1)[1].strip()
            continue
        ma.add(ln)
    return nguon, ma


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cap-nhat-baseline", action="store_true",
                    help="ghi lại tests/baseline-warn.json theo kết quả hiện tại")
    ap.add_argument("--voi-qa-all", action="store_true",
                    help="chạy thêm qa_all.py trên mẫu thật (cần LibreOffice, chậm hơn)")
    ap.add_argument("-v", "--chi-tiet", action="store_true")
    a = ap.parse_args()

    loi: list[str] = []
    cache: dict[str, list] = {}

    def ket_qua(p: Path):
        k = str(p)
        if k not in cache:
            cache[k] = chay(p)
        return cache[k]

    # ── 1. Mẫu thật phải sạch ────────────────────────────────────────
    mau = sorted((PLUGIN / "examples").rglob("*.docx"))
    if not mau:
        print("LỖI: không tìm thấy mẫu thật nào trong examples/", file=sys.stderr)
        return 1
    baseline = json.loads(BASELINE.read_text(encoding="utf-8")) if BASELINE.exists() else {}
    moi_baseline: dict[str, dict[str, int]] = {}
    print(f"── 1. Mẫu thật ({len(mau)} file) — không được có FAIL ──")
    for f in mau:
        ten = f.relative_to(PLUGIN).as_posix()
        ds = ket_qua(f)
        fails = [x for x in ds if x.level == FAIL]
        warns = Counter(x.code for x in ds if x.level == WARN)
        moi_baseline[ten] = dict(sorted(warns.items()))
        if fails:
            loi.append(f"MẪU THẬT FAIL — {ten}")
            for x in fails:
                loi.append(f"      {x.line()}")
        cu = baseline.get(ten)
        if cu is not None and not a.cap_nhat_baseline:
            for ma in set(warns) | set(cu):
                if warns.get(ma, 0) > cu.get(ma, 0):
                    loi.append(
                        f"WARN MỚI trên mẫu thật — {ten}: {ma} {cu.get(ma, 0)} → {warns[ma]}"
                        " (quy tắc mới đang bắt nhầm mẫu thật; sửa quy tắc, không sửa mẫu)")
        if a.chi_tiet:
            print(f"   {ten}: {len(fails)} FAIL, {sum(warns.values())} WARN")
    if not a.chi_tiet:
        print(f"   xong — {sum(1 for f in mau if not [x for x in ket_qua(f) if x.level == FAIL])}"
              f"/{len(mau)} file sạch FAIL")

    # ── 2. File lỗi phải bị bắt ──────────────────────────────────────
    fails_dir = sorted((TESTS / "fail").glob("*.docx"))
    print(f"\n── 2. File lỗi ({len(fails_dir)} file) — phải bắt đúng mã trong .expect ──")
    for f in fails_dir:
        exp_f = f.with_suffix(".expect")
        if not exp_f.exists():
            loi.append(f"THIẾU .expect cho {f.name}")
            continue
        nguon, ky_vong = doc_expect(exp_f)
        if not ky_vong:
            loi.append(f".expect rỗng: {exp_f.name}")
            continue
        thuc = ma_muc(ket_qua(f))
        thieu = ky_vong - thuc
        if thieu:
            loi.append(f"KHÔNG BẮT ĐƯỢC — {f.name}: thiếu {sorted(thieu)}; thực tế {sorted(thuc)}")
        cho_phep = set(ky_vong)
        if nguon:
            pn = PLUGIN / nguon
            if not pn.exists():
                loi.append(f"nguon không tồn tại trong {exp_f.name}: {nguon}")
            else:
                cho_phep |= ma_muc(ket_qua(pn))
        thua = {m for m in thuc if m.endswith(FAIL)} - cho_phep
        if thua:
            loi.append(f"BẮT THỪA — {f.name}: FAIL ngoài danh sách cho phép {sorted(thua)}")
        print(f"   {f.name}: {'ok' if not (thieu or thua) else 'SAI'}"
              f"  (kỳ vọng {sorted(ky_vong)})")

    # ── 3. qa_all.py trên mẫu thật (tùy chọn) ────────────────────────
    if a.voi_qa_all:
        print(f"\n── 3. qa_all.py trên mẫu thật ({len(mau)} file) ──")
        cu_qa = json.loads(BASELINE_QA.read_text(encoding="utf-8")) if BASELINE_QA.exists() else {}
        moi_qa: dict[str, list[str]] = {}
        for f in mau:
            ten = f.relative_to(PLUGIN).as_posix()
            try:
                tags = tags_qa_all(f)
            except subprocess.TimeoutExpired:
                loi.append(f"qa_all.py quá 300s trên {ten}")
                continue
            moi_qa[ten] = tags
            them = set(tags) - set(cu_qa.get(ten, []))
            if cu_qa and them and not a.cap_nhat_baseline:
                loi.append(f"qa_all.py SINH LỖI MỚI — {ten}: {sorted(them)}")
            if a.chi_tiet:
                print(f"   {ten}: {tags or 'PASS'}")
        if not a.chi_tiet:
            sach = sum(1 for v in moi_qa.values() if not v)
            print(f"   xong — {sach}/{len(moi_qa)} file PASS qa_all.py "
                  f"(phần còn lại là NỢ KỸ THUẬT có sẵn: SZ13, SIGSPACE, LINES, HDR-BR "
                  f"— xem mục D.4 tests/rule-inventory.md)")
        if a.cap_nhat_baseline:
            BASELINE_QA.write_text(json.dumps(moi_qa, ensure_ascii=False, indent=2) + "\n",
                                   encoding="utf-8")
            print(f"   Đã ghi lại {BASELINE_QA.relative_to(PLUGIN)}")

    if a.cap_nhat_baseline:
        BASELINE.write_text(json.dumps(moi_baseline, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8")
        print(f"\nĐã ghi lại {BASELINE.relative_to(PLUGIN)}")

    print("\n" + "=" * 62)
    if loi:
        print(f"HỒI QUY ĐỎ — {len(loi)} vấn đề:")
        for x in loi:
            print("  • " + x)
        return 1
    print("HỒI QUY XANH — mẫu thật sạch FAIL, mọi file lỗi bị bắt đúng mã.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
