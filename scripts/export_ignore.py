#!/usr/bin/env python3
"""Giữ archive của kho dưới trần 512 MB của claude.ai bằng thuộc tính export-ignore.

claude.ai đồng bộ marketplace từ GitHub bằng cách tải ARCHIVE (zip) của kho, với giới hạn
mặc định (docs Cowork, mục Limits): archive kho tối đa 512 MB, mỗi gói plugin tối đa 200 MB,
5.000 tệp. Vụ 11/9/2026: archive nén của kho lên 512,8 MB (10/9 mới 503,6 MB) -> claude.ai
báo "Sync failed", mọi plugin trên claude.ai đứng ở bản 10/9 dù kho vẫn cập nhật đều.

GitHub tôn trọng thuộc tính `export-ignore` trong .gitattributes khi tạo archive (zipball),
nên tệp nặng (PDF quét, hồ sơ ví dụ) VẪN nằm trong kho cho git clone / Claude Code, nhưng
KHÔNG đi vào gói claude.ai. Script này sinh .gitattributes từ danh sách tệp nặng:

    python3 scripts/export_ignore.py            # ghi lại .gitattributes
    python3 scripts/export_ignore.py --check    # chỉ kiểm, lệch hoặc quá trần thì exit 1 (CI)

Quy tắc: mọi tệp git đang theo dõi có kích thước >= NGUONG_TEP được đánh export-ignore.
Tệp nhỏ hơn (văn bản .md/.txt, mẫu .docx, PDF ngắn) vẫn vào gói. Sau khi thêm tệp mới vào
kho: chạy script rồi commit .gitattributes cùng đợt. check_descriptions.py gọi --check nên CI
đỏ nếu quên.
"""

import argparse
import os
import pathlib
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
GITATTRIBUTES = REPO / ".gitattributes"

MB = 1024 * 1024
NGUONG_TEP = 3 * MB          # tệp từ mức này không vào gói claude.ai
TRAN_ARCHIVE = 512 * MB      # giới hạn của claude.ai (nén); kiểm bằng tổng chưa nén nên chặt hơn
TRAN_CANH_BAO = 400 * MB     # vượt mức này thì CI đỏ để còn dư địa trước khi chạm 512
TRAN_PLUGIN = 150 * MB       # gói plugin claude.ai tối đa 200 MB, giữ dư địa

HEADER = [
    "# TỰ SINH bởi scripts/export_ignore.py - KHÔNG sửa tay, chạy lại script rồi commit.",
    "#",
    "# claude.ai đồng bộ marketplace bằng archive (zip) của kho, trần 512 MB; mỗi plugin 200 MB.",
    f"# Tệp từ {NGUONG_TEP // MB} MB trở lên được đánh export-ignore: vẫn nằm trong kho (git clone,",
    "# Claude Code) nhưng không vào gói claude.ai. Vụ 11/9/2026: archive 512,8 MB -> \"Sync failed\".",
    "#",
]


def tracked_files():
    """Danh sách (đường dẫn, kích thước) của mọi tệp git đang theo dõi, theo bytes UTF-8."""
    out = subprocess.run(
        ["git", "-C", str(REPO), "ls-files", "-z"], capture_output=True, check=True
    ).stdout
    files = []
    for raw in out.split(b"\0"):
        if not raw:
            continue
        path = raw.decode("utf-8")
        full = REPO / path
        if not full.is_file():      # tệp đã xóa khỏi working tree nhưng chưa commit
            continue
        files.append((path, os.stat(full).st_size))
    return files


def quote_pattern(path):
    """Viết đường dẫn thành pattern .gitattributes: thoát ký tự glob, rồi bọc C-style nếu cần."""
    escaped = "".join("\\" + c if c in "*?[]\\" else c for c in path)
    need_quote = any(ch.isspace() or ord(ch) > 126 or ch in '"#!' for ch in escaped)
    if not need_quote:
        return escaped
    return '"' + escaped.replace("\\", "\\\\").replace('"', '\\"') + '"'


def build(files):
    big = sorted(p for p, s in files if s >= NGUONG_TEP)
    lines = list(HEADER) + [f"{quote_pattern(p)} export-ignore" for p in big]
    return "\n".join(lines) + "\n", big


def check_attr(paths):
    """Hỏi git xem từng đường dẫn có export-ignore thật hay không (theo .gitattributes hiện có)."""
    if not paths:
        return {}
    out = subprocess.run(
        ["git", "-C", str(REPO), "check-attr", "-z", "--stdin", "export-ignore"],
        input="\0".join(paths).encode("utf-8") + b"\0",
        capture_output=True,
        check=True,
    ).stdout.split(b"\0")
    result = {}
    for i in range(0, len(out) - 2, 3):
        result[out[i].decode("utf-8")] = out[i + 2] == b"set"
    return result


def report(files, ignored):
    """In tổng dung lượng còn đi vào gói claude.ai, theo từng plugin; trả về danh sách lỗi."""
    errors = []
    total = 0
    per_plugin = {}
    for path, size in files:
        if ignored.get(path):
            continue
        total += size
        top = path.split("/", 1)[0]
        if (REPO / top / ".claude-plugin" / "plugin.json").exists():
            per_plugin[top] = per_plugin.get(top, 0) + size
    print(f"Archive claude.ai (ước tính chưa nén, sau export-ignore): {total / MB:.1f} MB "
          f"/ trần {TRAN_ARCHIVE // MB} MB (CI đỏ từ {TRAN_CANH_BAO // MB} MB)")
    for name, size in sorted(per_plugin.items(), key=lambda kv: -kv[1])[:5]:
        print(f"  {name:24} {size / MB:6.1f} MB")
    if total > TRAN_CANH_BAO:
        errors.append(
            f"archive dự tính {total / MB:.1f} MB vượt mức cảnh báo {TRAN_CANH_BAO // MB} MB: "
            f"hạ NGUONG_TEP trong scripts/export_ignore.py hoặc chuyển tệp nặng ra kho khác"
        )
    for name, size in per_plugin.items():
        if size > TRAN_PLUGIN:
            errors.append(f"plugin {name} còn {size / MB:.1f} MB đi vào gói claude.ai (> {TRAN_PLUGIN // MB} MB)")
    return errors


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true", help="chỉ kiểm tra, không ghi file")
    args = ap.parse_args()

    files = tracked_files()
    content, big = build(files)
    current = GITATTRIBUTES.read_text(encoding="utf-8") if GITATTRIBUTES.exists() else ""

    if args.check:
        errors = []
        if current != content:
            errors.append(".gitattributes lệch với danh sách tệp nặng hiện có - chạy "
                          "`python3 scripts/export_ignore.py` rồi commit")
        ignored = check_attr([p for p, _ in files])
        missing = [p for p in big if not ignored.get(p)]
        if missing:
            errors.append(f"{len(missing)} tệp >= {NGUONG_TEP // MB} MB chưa được export-ignore, ví dụ: {missing[0]}")
        errors += report(files, ignored)
        if errors:
            print("\nKhông đạt:")
            for e in errors:
                print(f"  - {e}")
            return 1
        print(f"export-ignore: {len(big)} tệp nặng đã được loại khỏi archive claude.ai, .gitattributes khớp.")
        return 0

    GITATTRIBUTES.write_text(content, encoding="utf-8")
    ignored = check_attr([p for p, _ in files])
    bad = [p for p in big if not ignored.get(p)]
    if bad:
        print(f"LỖI: git không nhận pattern cho {len(bad)} tệp, ví dụ: {bad[0]}")
        return 1
    print(f"Đã ghi .gitattributes: {len(big)} tệp >= {NGUONG_TEP // MB} MB được export-ignore.")
    return 1 if report(files, ignored) else 0


if __name__ == "__main__":
    sys.exit(main())
