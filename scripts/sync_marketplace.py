#!/usr/bin/env python3
"""Đồng bộ mô tả trong .claude-plugin/marketplace.json từ 18 file plugin.json.

Repo này KHÔNG đặt `version` trong plugin.json lẫn marketplace.json. Với
marketplace git dùng đường dẫn tương đối, bỏ `version` thì Claude Code coi mỗi
commit là một bản mới — không phải nâng số thủ công, không lệch được.

Còn lại mỗi `description` là phải khớp, vì đó là dòng chữ hiển thị trong danh
mục plugin. Script này lo phần đó.

    python3 scripts/sync_marketplace.py           # ghi lại marketplace.json
    python3 scripts/sync_marketplace.py --check    # chỉ kiểm tra, lệch thì exit 1
"""

import argparse
import collections
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"


def load_plugins():
    """Trả về {tên plugin: nội dung plugin.json} cho mọi plugin trong repo."""
    out = {}
    for manifest in sorted(REPO.glob("*/.claude-plugin/plugin.json")):
        data = json.loads(manifest.read_text(encoding="utf-8"))
        if "version" in data:
            sys.exit(
                f"{manifest.relative_to(REPO)} còn khoá 'version' — bỏ đi, "
                "nếu không plugin sẽ bị ghim và người dùng không nhận được bản mới"
            )
        out[data["name"]] = data
    return out


def build(marketplace, plugins):
    """Cập nhật description của từng entry, giữ nguyên thứ tự và các khoá khác."""
    entries = []
    for entry in marketplace["plugins"]:
        name = entry["name"]
        if name not in plugins:
            sys.exit(f"marketplace.json khai báo '{name}' nhưng repo không có thư mục plugin")
        if "version" in entry:
            sys.exit(f"entry '{name}' còn khoá 'version' — bỏ đi để mỗi commit là một bản mới")
        new = collections.OrderedDict(entry)
        new["description"] = plugins[name]["description"]
        entries.append(new)

    listed = {e["name"] for e in entries}
    for name in sorted(set(plugins) - listed):
        sys.exit(f"plugin '{name}' có trong repo nhưng thiếu entry trong marketplace.json")

    result = collections.OrderedDict(marketplace)
    result["plugins"] = entries
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="chỉ kiểm tra, không ghi file")
    args = ap.parse_args()

    marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"), object_pairs_hook=collections.OrderedDict)
    updated = build(marketplace, load_plugins())

    drift = [
        old["name"]
        for old, new in zip(marketplace["plugins"], updated["plugins"])
        if old != new
    ]

    if not drift:
        print(f"marketplace.json đã khớp {len(updated['plugins'])} plugin.json")
        return 0

    for name in drift:
        print(f"mô tả lệch: {name}")

    if args.check:
        print("\nChạy `python3 scripts/sync_marketplace.py` rồi commit lại marketplace.json.")
        return 1

    MARKETPLACE.write_text(
        json.dumps(updated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"\nĐã đồng bộ mô tả của {len(drift)} entry.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
