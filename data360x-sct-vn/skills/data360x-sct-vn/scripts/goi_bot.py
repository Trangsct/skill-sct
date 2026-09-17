#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""goi_bot.py — Ra lệnh cho bot Data360X trên máy cơ quan qua GitHub Actions, chờ và in kết quả.

    python3 goi_bot.py lay --tim "5511/SCT-CN; 3226/QĐ-UBND; tiêu chí lựa chọn chủ đầu tư" --ngay 60 --ten xuan-ai
    python3 goi_bot.py quet --ngay 30
    python3 goi_bot.py tim --ho-so "2026.09.03. To trinh ... CCN Phu Thinh 6"
    python3 goi_bot.py giu-phien
    python3 goi_bot.py trang-thai                 # nhịp tim máy + run gần nhất của từng workflow
    thêm --khong-cho để chỉ gửi lệnh, không chờ

Cần token GitHub có quyền Actions: write + Contents: read trên kho Trangsct/vlncn-laocai, đặt ở
GITHUB_TOKEN / GH_TOKEN / BOT_GITHUB_TOKEN. Trong phiên Claude Code có MCP GitHub thì gọi thẳng
actions_run_trigger, không cần script này (xem reference 02).
"""
import argparse
import base64
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

REPO = "Trangsct/vlncn-laocai"
WF = {"lay": "lay-van-ban.yml", "quet": "quet-tren-may.yml", "tim": "tim-van-ban.yml", "giu-phien": "giu-phien.yml"}
CHO_TOI_DA_PHUT = 40


def token():
    tk = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or os.environ.get("BOT_GITHUB_TOKEN")
    if not tk:
        sys.exit("Thiếu GITHUB_TOKEN / GH_TOKEN / BOT_GITHUB_TOKEN (quyền Actions: write trên kho vlncn-laocai).")
    return tk


def gh(method, duong, body=None):
    req = urllib.request.Request(f"https://api.github.com/{duong}", method=method,
                                 data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": "Bearer " + token(), "Accept": "application/vnd.github+json",
                                          "X-GitHub-Api-Version": "2022-11-28", "User-Agent": "data360x-sct-vn",
                                          "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            chu = r.read()
            return json.loads(chu) if chu else {}
    except urllib.error.HTTPError as e:
        sys.exit(f"GitHub {e.code} khi {method} {duong}: {e.read()[:300].decode(errors='replace')}")


def run_moi_nhat(wf):
    d = gh("GET", f"repos/{REPO}/actions/workflows/{wf}/runs?per_page=1")
    r = (d.get("workflow_runs") or [None])[0]
    return r


def cho(wf, sau_luc):
    """Chờ run tạo sau mốc sau_luc kết thúc. Kiểm tra sau 3 phút rồi mỗi 2 phút (không dồn dập)."""
    time.sleep(20)
    het = time.time() + CHO_TOI_DA_PHUT * 60
    lan = 0
    while time.time() < het:
        r = run_moi_nhat(wf)
        if r and r["created_at"] >= sau_luc:
            print(f"  run #{r['run_number']} {r['status']}" + (f" / {r['conclusion']}" if r.get("conclusion") else "")
                  + f"  {r['html_url']}")
            if r["status"] == "completed":
                return r
            if r["status"] == "queued" and lan >= 5:
                print("  Vẫn xếp hàng sau 10 phút: máy cơ quan có thể đang tắt hoặc chưa đăng nhập Windows.")
        time.sleep(180 if lan == 0 else 120)
        lan += 1
    print("Quá thời gian chờ; xem tiếp trên trang Actions.")
    return None


def doc_tep(duong):
    d = gh("GET", f"repos/{REPO}/contents/{duong}?ref=main")
    return base64.b64decode(d["content"]).decode("utf-8") if d.get("content") else ""


def log_loi(run_id):
    jobs = gh("GET", f"repos/{REPO}/actions/runs/{run_id}/jobs").get("jobs") or []
    for j in jobs:
        if j.get("conclusion") == "failure":
            print(f"  Bước lỗi: " + ", ".join(s["name"] for s in j.get("steps", []) if s.get("conclusion") == "failure"))
            print(f"  Log: {j['html_url']}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("viec", choices=list(WF) + ["trang-thai"])
    ap.add_argument("--tim", help="(lay) số ký hiệu / từ khóa, cách nhau bằng ;")
    ap.add_argument("--ngay", help="(lay/quet) số ngày quét")
    ap.add_argument("--ten", default="", help="(lay) tên thư mục kết quả")
    ap.add_argument("--ho-so", help="(tim) tên thư mục trong du-thao/")
    ap.add_argument("--khong-cho", action="store_true")
    a = ap.parse_args()

    if a.viec == "trang-thai":
        try:
            nt = json.loads(doc_tep("trang-thai/bot-chay.json"))
            print(f"Nhịp tim: lần cuối {nt.get('lan_cuoi')} trên máy {nt.get('may')}, quét {nt.get('quet')}, đẩy {nt.get('day')}"
                  + (f", lỗi: {nt.get('loi')}" if nt.get("loi") else ""))
        except SystemExit:
            print("Chưa có nhịp tim.")
        for k, wf in WF.items():
            r = run_moi_nhat(wf)
            print(f"{k:10} {wf:22} " + (f"#{r['run_number']} {r['status']}/{r.get('conclusion')} lúc {r['created_at']}" if r else "chưa chạy lần nào"))
        return 0

    inputs = {}
    if a.viec == "lay":
        if not a.tim:
            sys.exit("lay cần --tim")
        inputs = {"tim": a.tim, "ngay": a.ngay or "60", "ten": a.ten}
    elif a.viec == "quet":
        inputs = {"ngay": a.ngay or "30"}
    elif a.viec == "tim":
        if not a.ho_so:
            sys.exit("tim cần --ho-so")
        inputs = {"ho_so": a.ho_so}

    wf = WF[a.viec]
    truoc = run_moi_nhat(wf)
    if truoc and truoc["status"] in ("queued", "in_progress"):
        print(f"Lệnh trước của {wf} còn đang {truoc['status']} (#{truoc['run_number']}); lệnh mới sẽ xếp hàng sau nó.")
    sau_luc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    gh("POST", f"repos/{REPO}/actions/workflows/{wf}/dispatches", {"ref": "main", "inputs": inputs})
    print(f"Đã gửi lệnh {wf} {json.dumps(inputs, ensure_ascii=False)}")
    if a.khong_cho:
        return 0
    r = cho(wf, sau_luc)
    if not r:
        return 1
    if r["conclusion"] != "success":
        log_loi(r["id"])
        return 1
    if a.viec == "lay":
        ds = gh("GET", f"repos/{REPO}/contents/theo-doi/yeu-cau?ref=main")
        thu_muc = sorted((x["name"] for x in ds if x["type"] == "dir"))
        ten = a.ten if a.ten in thu_muc else (thu_muc[-1] if thu_muc else "")
        if ten:
            print(f"\n=== theo-doi/yeu-cau/{ten}/README.md ===\n" + doc_tep(f"theo-doi/yeu-cau/{ten}/README.md"))
    elif a.viec == "quet":
        ds = gh("GET", f"repos/{REPO}/contents/theo-doi/bao-cao?ref=main")
        ten = sorted(x["name"] for x in ds if x["name"].endswith(".md"))
        if ten:
            print(f"\n=== theo-doi/bao-cao/{ten[-1]} (40 dòng đầu) ===\n" + "\n".join(doc_tep(f"theo-doi/bao-cao/{ten[-1]}").splitlines()[:40]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
