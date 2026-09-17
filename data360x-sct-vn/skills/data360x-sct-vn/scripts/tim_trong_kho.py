#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tim_trong_kho.py — Tra kho văn bản đi/đến đã gom từ Data360X (theo-doi/ của kho riêng tư vlncn-laocai).

Tra KHO TRƯỚC, sai bot SAU (quy tắc 1 của skill data360x-sct-vn).

    python3 tim_trong_kho.py "tiêu chí lựa chọn chủ đầu tư"           # từ khóa trong trích yếu, không phân biệt dấu
    python3 tim_trong_kho.py 5511/SCT-CN 3226/QĐ-UBND                 # số ký hiệu (khớp đúng, bỏ khoảng trắng và dấu chấm)
    python3 tim_trong_kho.py "Xuân Ái" --linh-vuc kccn-sct-vn --tu 01/09/2026 --den 30/09/2026
    python3 tim_trong_kho.py --nguon den --linh-vuc hc-sct-vn --tu 7   # 7 = 7 ngày gần nhất
    python3 tim_trong_kho.py --ban-tin                                  # in bản tin mới nhất
    python3 tim_trong_kho.py --doc 5563/SCT-CN                          # in chữ của văn bản (nếu đã có tệp .md)

Nguồn dữ liệu (thử theo thứ tự):
  1. Thư mục clone kho vlncn-laocai: biến môi trường VLNCN_DIR, hoặc ../vlncn-laocai, ../../vlncn-laocai,
     ~/vlncn-laocai, /home/user/vlncn-laocai.
  2. GitHub API (kho riêng tư) với GITHUB_TOKEN / GH_TOKEN / BOT_GITHUB_TOKEN.
Không có cả hai → in hướng dẫn, thoát mã 2.
"""
import argparse
import base64
import json
import os
import re
import sys
import unicodedata
import urllib.request
from datetime import date, datetime, timedelta
from pathlib import Path

REPO = "Trangsct/vlncn-laocai"
THU_MUC = "theo-doi"


def bo_dau(s):
    s = unicodedata.normalize("NFD", str(s or ""))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", s.replace("đ", "d").replace("Đ", "D")).strip().lower()


def chuan_so(s):
    return re.sub(r"[\s.]", "", s or "").upper()


def parse_ngay(s):
    m = re.search(r"(\d{1,2})/(\d{1,2})/(\d{4})", s or "")
    return date(int(m.group(3)), int(m.group(2)), int(m.group(1))) if m else None


def moc(s):
    """'7' -> hôm nay - 7 ngày; '01/09/2026' -> ngày."""
    if not s:
        return None
    if s.isdigit():
        return date.today() - timedelta(days=int(s))
    n = parse_ngay(s)
    if not n:
        sys.exit(f"Không hiểu mốc ngày: {s} (dùng dd/mm/yyyy hoặc số ngày)")
    return n


# ---------------------------------------------------------------- nguồn dữ liệu
def tim_clone():
    ung = [os.environ.get("VLNCN_DIR", "")] + [str(Path(p).expanduser()) for p in
           ("../vlncn-laocai", "../../vlncn-laocai", "../../../vlncn-laocai", "~/vlncn-laocai", "/home/user/vlncn-laocai")]
    for u in ung:
        if u and (Path(u) / THU_MUC).is_dir():
            return Path(u)
    return None


def token():
    return os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or os.environ.get("BOT_GITHUB_TOKEN") or ""


def doc_tep(duong, goc=None):
    """Đọc một tệp trong kho: từ clone nếu có, không thì qua API. Trả text hoặc None."""
    if goc:
        p = goc / duong
        return p.read_text(encoding="utf-8") if p.exists() else None
    tk = token()
    if not tk:
        return None
    req = urllib.request.Request(f"https://api.github.com/repos/{REPO}/contents/{duong}?ref=main",
                                 headers={"Authorization": "Bearer " + tk, "Accept": "application/vnd.github+json",
                                          "User-Agent": "data360x-sct-vn"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.loads(r.read())
        if isinstance(d, dict) and d.get("content"):
            return base64.b64decode(d["content"]).decode("utf-8")
        if isinstance(d, dict) and d.get("download_url"):
            with urllib.request.urlopen(urllib.request.Request(d["download_url"], headers={"Authorization": "Bearer " + tk}), timeout=60) as r2:
                return r2.read().decode("utf-8")
    except Exception as e:
        print(f"Không đọc được {duong} qua API: {e}", file=sys.stderr)
    return None


def liet_ke(duong, goc=None):
    if goc:
        p = goc / duong
        return sorted(x.name for x in p.iterdir()) if p.is_dir() else []
    tk = token()
    if not tk:
        return []
    req = urllib.request.Request(f"https://api.github.com/repos/{REPO}/contents/{duong}?ref=main",
                                 headers={"Authorization": "Bearer " + tk, "Accept": "application/vnd.github+json",
                                          "User-Agent": "data360x-sct-vn"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return sorted(x["name"] for x in json.loads(r.read()))
    except Exception:
        return []


def nap_danh_muc(goc, cac_nam):
    ds = []
    for nam in cac_nam:
        chu = doc_tep(f"{THU_MUC}/danh-muc-{nam}.json", goc)
        if chu:
            try:
                ds.extend(json.loads(chu))
            except json.JSONDecodeError:
                print(f"danh-muc-{nam}.json hỏng", file=sys.stderr)
    return ds


# ---------------------------------------------------------------- chính
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tim", nargs="*", help="từ khóa (không dấu cũng được) hoặc số ký hiệu (có dấu /)")
    ap.add_argument("--linh-vuc", help="mã plugin, ví dụ kccn-sct-vn (nhiều mã cách nhau bằng dấu phẩy)")
    ap.add_argument("--nguon", choices=["den", "di"], help="chỉ văn bản đến / đi")
    ap.add_argument("--tu", help="từ ngày dd/mm/yyyy, hoặc N = N ngày gần nhất")
    ap.add_argument("--den", help="đến ngày dd/mm/yyyy")
    ap.add_argument("--co-tep", action="store_true", help="chỉ văn bản đã có chữ/bản gốc trong kho")
    ap.add_argument("--nam", default=str(date.today().year), help="năm danh mục (nhiều năm: 2025,2026)")
    ap.add_argument("--ban-tin", action="store_true", help="in bản tin mới nhất rồi thoát")
    ap.add_argument("--doc", metavar="SO_KY_HIEU", help="in nội dung tệp .md của văn bản")
    ap.add_argument("--json", action="store_true", help="in kết quả dạng JSON")
    ap.add_argument("--gioi-han", type=int, default=60)
    a = ap.parse_args()

    goc = tim_clone()
    if not goc and not token():
        print("Không thấy bản clone vlncn-laocai (đặt VLNCN_DIR) và không có GITHUB_TOKEN. "
              "Trong phiên có MCP GitHub: dùng get_file_contents với Trangsct/vlncn-laocai, "
              f"đường dẫn {THU_MUC}/danh-muc-{a.nam}.json", file=sys.stderr)
        return 2
    if goc:
        print(f"(kho: {goc})", file=sys.stderr)

    if a.ban_tin:
        ten = liet_ke(f"{THU_MUC}/bao-cao", goc)
        ten = [t for t in ten if t.endswith(".md")]
        if not ten:
            print("Chưa có bản tin nào."); return 1
        print(doc_tep(f"{THU_MUC}/bao-cao/{ten[-1]}", goc) or "")
        return 0

    ds = nap_danh_muc(goc, [n.strip() for n in a.nam.split(",")])
    if not ds:
        print("Danh mục trống hoặc không đọc được.", file=sys.stderr); return 1

    if a.doc:
        so = chuan_so(a.doc)
        for r in ds:
            if chuan_so(r.get("so_ky_hieu")) == so:
                if r.get("tep", "").endswith(".md"):
                    print(doc_tep(r["tep"], goc) or "(không đọc được tệp)")
                elif r.get("tep"):
                    print(f"Bản scan, không có chữ: {r['tep']} — dựng ảnh trang bằng pymupdf để đọc.")
                else:
                    print(f"Chỉ có mục lục, chưa có bản gốc. URL: {r.get('url_chi_tiet')}\n"
                          f"→ sai bot: workflow lay-van-ban.yml, tim=\"{r.get('so_ky_hieu')}\"")
                return 0
        print(f"Không có {a.doc} trong danh mục."); return 1

    so_can = {chuan_so(t) for t in a.tim if "/" in t}
    # Mỗi từ khóa là một cụm; khớp khi MỌI chữ trong cụm đều có trong trích yếu (không cần liền nhau):
    # "tiêu chí lựa chọn" vẫn bắt được "tiêu chí đánh giá lựa chọn chủ đầu tư".
    tu_khoa = [bo_dau(t).split() for t in a.tim if "/" not in t]
    lv = {x.strip() for x in a.linh_vuc.split(",")} if a.linh_vuc else set()
    tu, den = moc(a.tu), moc(a.den)

    kq = []
    for r in ds:
        n = parse_ngay(r.get("ngay_ban_hanh"))
        if tu and (not n or n < tu):
            continue
        if den and (not n or n > den):
            continue
        if a.nguon and r.get("nguon") != a.nguon:
            continue
        if lv and not (lv & set(r.get("linh_vuc") or [])):
            continue
        if a.co_tep and not r.get("tep"):
            continue
        ty = " " + bo_dau(r.get("trich_yeu")) + " "
        if so_can and chuan_so(r.get("so_ky_hieu")) not in so_can:
            if not tu_khoa or not any(all(f" {c}" in ty or c in ty for c in cum) for cum in tu_khoa):
                continue
        elif tu_khoa and not so_can and not any(all(c in ty for c in cum) for cum in tu_khoa):
            continue
        kq.append(r)
    kq.sort(key=lambda r: parse_ngay(r.get("ngay_ban_hanh")) or date.min, reverse=True)

    if a.json:
        print(json.dumps(kq[:a.gioi_han], ensure_ascii=False, indent=1)); return 0
    print(f"{len(kq)} văn bản khớp" + (f" (in {a.gioi_han} mới nhất)" if len(kq) > a.gioi_han else "") + ":")
    for r in kq[:a.gioi_han]:
        tep = r.get("tep") or "-"
        print(f"{r.get('so_ky_hieu') or '(không số)':22} | {r.get('ngay_ban_hanh', ''):10} | {r.get('nguon', ''):3} | "
              f"{','.join(r.get('linh_vuc') or []) or '-':28} | {(r.get('trich_yeu') or '')[:90]} | {tep}")
    if kq and not any(r.get("tep") for r in kq[:a.gioi_han]):
        print("\nKhông văn bản nào có bản gốc trong kho → sai bot: workflow lay-van-ban.yml với các số ký hiệu trên.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
