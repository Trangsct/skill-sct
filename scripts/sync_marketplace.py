#!/usr/bin/env python3
"""Đồng bộ .claude-plugin/marketplace.json từ 18 file plugin.json.

Claude Code phân giải version của plugin theo thứ tự: plugin.json -> entry trong
marketplace.json -> commit SHA. Đặt version ở cả hai chỗ mà để lệch nhau thì bản
plugin.json sẽ che version trong marketplace.json, còn catalog hiển thị cho người
dùng (tên, mô tả, version) thì vẫn là bản cũ. Script này giữ hai file luôn khớp.

    python3 scripts/sync_marketplace.py           # ghi lại marketplace.json
    python3 scripts/sync_marketplace.py --check    # kiểm tra; lỗi cấu trúc mới exit 1
    python3 scripts/sync_marketplace.py --bump     # ghi lại + tự nâng metadata.version
    python3 scripts/sync_marketplace.py --bump --baseline before.json
                                                  # so thêm với catalog của commit trước

Chế độ --bump dùng cho CI trên nhánh main: mỗi khi có plugin đổi version hoặc đổi
mô tả, metadata.version của marketplace được nâng một bậc patch để claude.ai nhận
ra catalog đã thay đổi mà không phải sửa tay.

--baseline vá kẽ hở "PR đã sync sẵn": nếu marketplace.json trong PR đã khớp hết
với plugin.json (không còn lệch) thì bump kiểu cũ sẽ bị bỏ qua, dù catalog thực
tế vừa thay đổi so với main cũ. Truyền vào marketplace.json của commit trước đó
(git show <before>:.claude-plugin/marketplace.json) để bot nhận ra "catalog đổi
mà metadata.version chưa nâng" và vẫn tự nâng.
"""

import argparse
import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"

# Các khoá chỉ có ý nghĩa trong marketplace entry, luôn giữ nguyên từ bản cũ.
MARKETPLACE_ONLY = ("source", "category", "tags", "strict", "relevance", "defaultEnabled")
# Các khoá lấy từ plugin.json làm nguồn chuẩn.
FROM_PLUGIN = ("description", "version")


def load_plugins():
    """Trả về {tên plugin: nội dung plugin.json} cho mọi plugin trong repo."""
    out = {}
    for manifest in sorted(REPO.glob("*/.claude-plugin/plugin.json")):
        data = json.loads(manifest.read_text(encoding="utf-8"))
        out[data["name"]] = data
    return out


def build(marketplace, plugins):
    """Dựng lại mảng plugins, giữ nguyên thứ tự và các khoá riêng của marketplace."""
    entries = []
    for entry in marketplace["plugins"]:
        name = entry["name"]
        if name not in plugins:
            sys.exit(f"marketplace.json khai báo '{name}' nhưng repo không có thư mục plugin")
        manifest = plugins[name]
        new = {"name": name}
        for key in MARKETPLACE_ONLY:
            if key in entry:
                new[key] = entry[key]
        for key in FROM_PLUGIN:
            if key in manifest:
                new[key] = manifest[key]
        entries.append(new)

    listed = {e["name"] for e in entries}
    for name in sorted(set(plugins) - listed):
        sys.exit(f"plugin '{name}' có trong repo nhưng thiếu entry trong marketplace.json")

    result = dict(marketplace)
    result["plugins"] = entries
    return result


def bump_patch(version):
    """Nâng một bậc patch: 4.5.3 -> 4.5.4. Không parse được thì thêm '.1'."""
    parts = version.split(".")
    if len(parts) == 3 and all(p.isdigit() for p in parts):
        parts[2] = str(int(parts[2]) + 1)
        return ".".join(parts)
    return version + ".1"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="chỉ kiểm tra, không ghi file")
    ap.add_argument("--bump", action="store_true", help="ghi file và tự nâng metadata.version")
    ap.add_argument(
        "--baseline",
        help="marketplace.json của commit trước; catalog đổi so với bản này mà "
        "metadata.version chưa nâng thì --bump vẫn nâng, kể cả khi hết lệch",
    )
    args = ap.parse_args()

    marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    updated = build(marketplace, load_plugins())

    drift = [
        (old["name"], old.get("version"), new.get("version"))
        for old, new in zip(marketplace["plugins"], updated["plugins"])
        if old != new
    ]

    stale_meta = False
    if args.baseline:
        baseline = json.loads(pathlib.Path(args.baseline).read_text(encoding="utf-8"))
        old_meta = baseline.get("metadata", {}).get("version")
        new_meta = updated.get("metadata", {}).get("version")
        stale_meta = updated["plugins"] != baseline.get("plugins") and new_meta == old_meta
        if stale_meta:
            print(f"catalog đã đổi so với commit trước nhưng metadata.version vẫn {new_meta}")

    if not drift and not stale_meta:
        print(f"marketplace.json đã khớp {len(updated['plugins'])} plugin.json")
        return 0

    for name, old_version, new_version in drift:
        change = f"{old_version} -> {new_version}" if old_version != new_version else "mô tả"
        print(f"lệch: {name} ({change})")

    if args.check:
        print(
            "\nKhông cần sync tay: bot trên main sẽ tự đồng bộ marketplace.json "
            "và nâng metadata.version sau khi merge."
        )
        return 0

    if args.bump:
        meta = updated.setdefault("metadata", {})
        meta["version"] = bump_patch(meta.get("version", "0.0.0"))
        print(f"\nmetadata.version -> {meta['version']}")

    MARKETPLACE.write_text(
        json.dumps(updated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    if drift:
        tail = "" if args.bump else " Nhớ nâng metadata.version trước khi push."
        print(f"Đã đồng bộ {len(drift)} entry.{tail}")
    else:
        print("Entry đã khớp sẵn, chỉ nâng metadata.version.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
