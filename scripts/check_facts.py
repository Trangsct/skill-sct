#!/usr/bin/env python3
"""Quét dữ kiện lỗi thời / quy ước cũ còn sót trong toàn bộ plugin.

Mỗi khi Bạn chốt một quy ước mới hoặc một dữ kiện đổi (ủy quyền mới, đổi chuyên viên,
đổi nơi nộp hồ sơ...), thêm MỘT mục vào danh sách RULES bên dưới; CI (validate-plugins.yml)
sẽ đỏ ở bất kỳ plugin nào còn dùng cách cũ.

    python3 scripts/check_facts.py            # quét, in vi phạm, exit 1 nếu có FAIL
    python3 scripts/check_facts.py --warn     # in cả WARN (không làm CI đỏ)
    python3 scripts/check_facts.py --list     # liệt kê các quy tắc đang áp dụng

Phạm vi quét: mọi file .md trong <plugin>/skills/<plugin>/ (SKILL.md, references, mau-van-ban,
checklists, INDEX), TRỪ CHANGELOG*, van-ban-goc/*.md (văn bản gốc), vi-du-thuc-te/ (lịch sử thật)
và các dòng chứa từ khóa lịch sử/ngoại lệ (xem ALLOW_LINE).

Cách viết một rule:
  {
    "id": "gp-ubnd-2867",           # mã ngắn, duy nhất
    "pattern": r"...",              # regex (Python, IGNORECASE), so khớp trên từng dòng (NFC)
    "why": "...",                   # vì sao sai, và cách ghi đúng
    "since": "2026-08-20",          # mốc dữ kiện đổi
    "level": "FAIL" | "WARN",
    "only": ["sd-vlncn-sct-vn"],    # (tùy chọn) chỉ quét các plugin này
    "skip": ["vbhc-vn"],            # (tùy chọn) bỏ qua các plugin này
  }
"""
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Dòng có các cụm này được coi là đang nói về LỊCH SỬ / ngoại lệ có chủ ý → không báo
ALLOW_LINE = re.compile(
    r"(đến 19/8/2026|trước 20/8/2026|đến hết 19/8|trước đây|lịch sử|cũ\)|\(cũ\)|đã bãi bỏ|"
    r"không sửa lại|giữ nguyên lịch sử|không dùng|KHÔNG ghi|không ghi|cấm|CẤM|sai:|SAI|"
    r"→ đúng|-> đúng|thay vì|đã sửa|đã thay|từng ghi|trước 10/7/2026|đến 14/7/2026|"
    r"quy ước cố định|check_facts|kênh phụ|hoặc qua Trung tâm|ghi nhầm|nguồn ghi|cách gọi|NQ 34 \(12/2025\)|"
    r"không \"giai đoạn|vụ (QĐ )?5116)",
    re.I,
)

RULES = [
    {
        "id": "gp-ubnd-sau-2867",
        # "dự thảo Giấy phép (GP-UBND)", "ký GP-UBND", "trình Chủ tịch UBND tỉnh ký GP" — sau 20/8/2026 GP sử dụng VLNCN là /GP-SCT
        "pattern": r"(dự thảo giấy phép \(GP-UBND\)|Chủ tịch UBND tỉnh ký GP-UBND|GP sử dụng vẫn do Chủ tịch|ký hiệu dự kiến `/GP-SCT`)",
        "why": "Từ 20/8/2026 GP sử dụng VLNCN do Sở cấp theo QĐ 2867/QĐ-UBND, ký hiệu /GP-SCT, KT. GĐ – PGĐ Hoàng Văn Thuân ký (thu hồi GP, phê duyệt PANM vẫn UBND tỉnh).",
        "since": "2026-08-20",
        "level": "FAIL",
    },
    {
        "id": "noi-nop-pvhcc",
        "pattern": r"(đầu mối (tiếp nhận|nộp hồ sơ)[^.\n]{0,40}Trung tâm Phục vụ hành chính công|nộp (trực tiếp )?tại Trung tâm Phục vụ hành chính công|qua Trung tâm Phục vụ hành chính công tỉnh\) để được xem xét)",
        "why": "Nơi nộp TTHC ghi Cổng dịch vụ công một cửa Bộ Công Thương https://motcua-tthc.moit.gov.vn/ (quy ước 02/8/2026); Trung tâm PVHCC chỉ nêu là kênh phụ.",
        "since": "2026-08-02",
        "level": "FAIL",
    },
    {
        "id": "noi-nop-dvcqg",
        "pattern": r"nộp (hồ sơ )?(trên|qua|tại) Cổng Dịch vụ công [Qq]uốc gia",
        "why": "Không hướng dẫn DN nộp qua Cổng DVCQG; ghi https://motcua-tthc.moit.gov.vn/ (trích dẫn nguyên văn luật thì thêm chữ 'theo luật' hoặc để trong ngoặc kép).",
        "since": "2026-08-02",
        "level": "WARN",
    },
    {
        "id": "cong-hoa",
        "pattern": r"CỘNG HOÀ",
        "why": "Quốc hiệu viết 'CỘNG HÒA' (không 'HOÀ').",
        "since": "2026-06-01",
        "level": "FAIL",
    },
    {
        "id": "tieu-ngu-gach-noi",
        "pattern": r"Độc lập - Tự do - Hạnh phúc",
        "why": "Tiêu ngữ dùng en dash: 'Độc lập – Tự do – Hạnh phúc'.",
        "since": "2026-06-01",
        "level": "WARN",
    },
    {
        "id": "cn-m-cuong-vlncn",
        "pattern": r"CN\(M\.?\s?Cường\)",
        "why": "Từ 10/7/2026 chuyên viên VLNCN/PANM là CN(Khôi); Đỗ Mạnh Cường là PTP, không đứng dòng Lưu (văn bản cũ giữ nguyên lịch sử — thêm chữ 'lịch sử'/'trước 10/7/2026' vào dòng nếu là trích dẫn cũ).",
        "since": "2026-07-10",
        "level": "WARN",
    },
    {
        "id": "yen-hop-giai-doan",
        "pattern": r"Yên Hợp[^|\n]{0,25}giai đoạn (I|II|1|2)\b",
        "why": "CCN Yên Hợp (12 ha) và CCN Yên Hợp 1 (63 ha) là 2 dự án độc lập; không dùng 'giai đoạn I/II' (nếu chép nguyên văn nguồn phải chú thích).",
        "since": "2026-07-01",
        "level": "WARN",
    },
    {
        "id": "so-tnmt-hien-hanh",
        "pattern": r"(chuyển|gửi|hỏi|lấy ý kiến|phối hợp với) Sở (Tài nguyên và Môi trường|TN&MT)\b",
        "why": "Sở TN&MT đã hợp nhất thành Sở Nông nghiệp và Môi trường (SNNMT) từ 01/3/2025; nếu trích nguyên văn nghị định cũ thì giữ nhưng chú thích '(nay là SNNMT)'.",
        "since": "2025-03-01",
        "level": "WARN",
    },
    {
        "id": "xp-hc-vlncn-cu",
        "pattern": r"→ plugin `xp-hc-vlncn-sct-vn`|dùng plugin xp-hc-vlncn-sct-vn",
        "why": "xp-hc-vlncn-sct-vn đã được xp-sct-vn kế thừa (02/9/2026); trỏ sang xp-sct-vn.",
        "since": "2026-09-02",
        "level": "WARN",
        "skip": ["xp-hc-vlncn-sct-vn"],
    },
    {
        "id": "ban-du-thao-pdf",
        "pattern": r"bản dự thảo chưa điền số|chưa điền số/ngày|PDF là bản dự thảo",
        "why": "Không kết luận PDF là 'bản dự thảo/chưa điền số' khi chưa chạy extract_metadata.py (vụ QĐ 5116/QĐ-SCT 02/9/2026).",
        "since": "2026-09-02",
        "level": "FAIL",
    },
]

EXCLUDE_PARTS = ("van-ban-goc", "vi-du-thuc-te", "examples", "templates")
EXCLUDE_NAME = ("nd30-phu-luc",)  # bản chép nguyên văn VBQPPL — không sửa theo quy ước nội bộ


def iter_files():
    for pj in sorted(REPO.glob("*/.claude-plugin/plugin.json")):
        plugin = pj.parent.parent.name
        skill_dir = REPO / plugin / "skills" / plugin
        if not skill_dir.exists():
            continue
        for f in sorted(skill_dir.rglob("*.md")):
            rel = f.relative_to(skill_dir).as_posix()
            if rel.startswith("CHANGELOG") or any(p in rel.split("/") for p in EXCLUDE_PARTS) \
                    or any(x in f.name for x in EXCLUDE_NAME):
                continue
            yield plugin, f, rel


def main():
    args = sys.argv[1:]
    if "--list" in args:
        for r in RULES:
            print(f"[{r['level']}] {r['id']} (từ {r['since']}): {r['why']}")
        return 0
    show_warn = "--warn" in args
    compiled = [(r, re.compile(r["pattern"], re.I)) for r in RULES]
    fails, warns = [], []
    for plugin, f, rel in iter_files():
        try:
            lines = f.read_text(encoding="utf-8").split("\n")
        except UnicodeDecodeError:
            lines = f.read_text(encoding="utf-8", errors="ignore").split("\n")
        for n, raw in enumerate(lines, 1):
            line = unicodedata.normalize("NFC", raw)
            if ALLOW_LINE.search(line):
                continue
            for r, rx in compiled:
                if r.get("only") and plugin not in r["only"]:
                    continue
                if plugin in r.get("skip", []):
                    continue
                m = rx.search(line)
                if m:
                    item = (r["id"], f"{plugin}/{rel}:{n}", m.group(0)[:60], r["why"])
                    (fails if r["level"] == "FAIL" else warns).append(item)
    for lv, items in (("FAIL", fails), ("WARN", warns if show_warn else [])):
        for rid, loc, hit, why in items:
            print(f"[{lv} {rid}] {loc}: «{hit}»\n    → {why}")
    print(f"\ncheck_facts: {len(fails)} FAIL, {len(warns)} WARN "
          f"({'hiện' if show_warn else 'ẩn — dùng --warn để xem'})")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
