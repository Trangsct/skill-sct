#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_ban_word_vbqppl.py — rà văn bản quy phạm pháp luật chưa có bản Word trong van-ban-goc/.

Quy tắc Bạn chốt 08/10/2026 (CLAUDE.md, mục Quy tắc nghiệp vụ chung): văn bản quy phạm pháp luật
Bạn gửi phải lưu bản Word (.docx) vào van-ban-goc/ của plugin đúng lĩnh vực.

Script chỉ BÁO CÁO (luôn thoát mã 0), in hai danh sách:
  1. File PDF trong van-ban-goc/ có tên dạng văn bản quy phạm (ND-, TT-, Luat-, NQ-…-CP/QH, QD-…-TTg)
     mà cùng thư mục không có .docx/.doc cùng tên gốc.
  2. Reference ghi "Bạn cung cấp" kèm "PDF"/"Word" nhưng cả plugin không có file nào mang số-năm đó.

Dùng:  python3 scripts/check_ban_word_vbqppl.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
QPPL = re.compile(r"^(ND|TT|TTLT|Luat|LUAT|PL|NQ|QD)[-_ ]?(\d+)[-_ ](\d{4})", re.I)
NGUON = re.compile(r"(NĐ|Nghị định|Thông tư|TT|Luật)\s*(?:số\s*)?(\d+)/(\d{4})[^\n]{0,200}Bạn (?:cung cấp|gửi)", re.I)


def main() -> int:
    thieu_word, thieu_file = [], []
    for vbg in sorted(REPO.glob("*/skills/*/van-ban-goc")):
        files = [f for f in vbg.rglob("*") if f.is_file()]
        stems_word = {f.stem.lower() for f in files if f.suffix.lower() in (".docx", ".doc")}
        for f in files:
            if f.suffix.lower() == ".pdf" and QPPL.match(f.name) and f.stem.lower() not in stems_word:
                thieu_word.append(f.relative_to(REPO))
    for plugin in sorted(p for p in REPO.iterdir() if (p / ".claude-plugin").is_dir()):
        ten_file = " ".join(f.name for f in plugin.rglob("van-ban-goc/**/*") if f.is_file())
        for ref in plugin.rglob("references/*.md"):
            for m in NGUON.finditer(ref.read_text(encoding="utf-8", errors="ignore")[:3000]):
                so, nam = m.group(2), m.group(3)
                if not re.search(rf"(?<!\d){so}[-_ ]{nam}", ten_file):
                    thieu_file.append(f"{ref.relative_to(REPO)}: {m.group(1)} {so}/{nam}")
    print(f"1. PDF văn bản quy phạm chưa có bản Word cùng tên: {len(thieu_word)}")
    for f in thieu_word:
        print(f"   - {f}")
    print(f"2. Reference ghi nguồn 'Bạn cung cấp/gửi' nhưng plugin không có file gốc: {len(thieu_file)}")
    for s in sorted(set(thieu_file)):
        print(f"   - {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
