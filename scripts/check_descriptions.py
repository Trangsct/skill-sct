#!/usr/bin/env python3
"""Kiểm tra giới hạn độ dài description trước khi đóng gói plugin.

Trình upload plugin của Claude từ chối gói nếu vượt giới hạn:
  - description trong .claude-plugin/plugin.json : tối đa 500 ký tự
  - description trong frontmatter SKILL.md       : tối đa 1024 ký tự

    python3 scripts/check_descriptions.py
"""

import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
MAX_PLUGIN_JSON = 500
MAX_SKILL_MD = 1024


def read_json_description(path):
    """Đọc description mà không cần thư viện ngoài."""
    import json

    return json.loads(path.read_text(encoding="utf-8")).get("description", "")


def read_skill_description(path):
    """Trích description trong frontmatter, hỗ trợ cả chuỗi trích dẫn và block scalar."""
    text = path.read_text(encoding="utf-8")
    front = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not front:
        return None
    body = front.group(1)

    try:
        import yaml  # có thì dùng, chuẩn nhất
        value = yaml.safe_load(body).get("description")
        return value if isinstance(value, str) else None
    except ImportError:
        pass

    quoted = re.search(r'^description:\s*"(.*?)"\s*$', body, re.S | re.M)
    if quoted:
        return quoted.group(1)

    block = re.search(r"^description:\s*[>|][-+]?\s*\n((?:[ \t]+.*\n?)+)", body, re.M)
    if block:
        lines = [line.strip() for line in block.group(1).splitlines() if line.strip()]
        return " ".join(lines)

    plain = re.search(r"^description:\s*(\S.*?)\s*$", body, re.M)
    return plain.group(1) if plain else None


def main():
    problems = []
    for manifest in sorted(REPO.glob("*/.claude-plugin/plugin.json")):
        name = manifest.parents[1].name
        length = len(read_json_description(manifest))
        status = "ok  "
        if length > MAX_PLUGIN_JSON:
            status = "VƯỢT"
            problems.append(f"{name}: plugin.json description {length} > {MAX_PLUGIN_JSON}")

        skill = REPO / name / "skills" / name / "SKILL.md"
        skill_len = -1
        if skill.exists():
            description = read_skill_description(skill)
            if description is None:
                problems.append(f"{name}: không đọc được description trong SKILL.md")
            else:
                skill_len = len(description)
                if skill_len > MAX_SKILL_MD:
                    status = "VƯỢT"
                    problems.append(f"{name}: SKILL.md description {skill_len} > {MAX_SKILL_MD}")

        print(f"{status} {name:24} plugin.json={length:4}  SKILL.md={skill_len:5}")

    if problems:
        print("\nKhông đạt:")
        for line in problems:
            print(f"  - {line}")
        return 1

    print("\nTất cả description nằm trong giới hạn.")
    return 0


def _run_check_facts() -> int:
    """CI (validate-plugins.yml) chỉ gọi check_descriptions.py; token PAT không có quyền sửa
    workflow nên check_facts.py được gọi từ đây để vẫn chặn dữ kiện lỗi thời trên CI."""
    import subprocess
    here = pathlib.Path(__file__).resolve().parent
    print("\n=== scripts/check_facts.py (dữ kiện lỗi thời / quy ước cũ) ===")
    return subprocess.run([sys.executable, str(here / "check_facts.py")]).returncode


def _run_check_registry() -> None:
    """Sổ đăng ký văn bản pháp luật: chỉ cảnh báo dẫn văn bản đã bị thay thế (không chặn CI)."""
    import subprocess
    here = pathlib.Path(__file__).resolve().parent
    print("\n=== scripts/build_registry.py --check (văn bản đã bị thay thế còn được dẫn) ===")
    subprocess.run([sys.executable, str(here / "build_registry.py"), "--check"])


if __name__ == "__main__":
    rc = main()
    rc_facts = _run_check_facts()
    _run_check_registry()
    sys.exit(rc or rc_facts)
