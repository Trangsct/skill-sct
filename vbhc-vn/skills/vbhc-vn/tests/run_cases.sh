#!/usr/bin/env bash
# run_cases.sh — Bộ kiểm thử LỚP 2 của plugin vbhc-vn (CÓ gọi mô hình).
#
# Khác lớp 1 (tests/run_regression.py — tất định, chạy trên CI): lớp 2 giao đề bài thật
# cho Claude Code ở chế độ không tương tác, rồi chấm sản phẩm bằng qa_all.py và tieu-chi.txt.
# Vì có gọi mô hình nên KHÔNG chạy trên CI — chạy theo yêu cầu trong phiên làm việc.
#
# Cách chạy:
#   bash tests/run_cases.sh              # chạy toàn bộ case
#   bash tests/run_cases.sh 01 05        # chỉ chạy case có tiền tố 01 và 05
#   CLAUDE_BIN=claude bash tests/run_cases.sh    # đổi lệnh gọi Claude Code
#
# Kết quả: bảng ĐẠT/KHÔNG ĐẠT từng case + sản phẩm trong tests/_ket-qua/<case>/.

set -uo pipefail
PLUGIN="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CASES="$PLUGIN/tests/cases"
OUT="$PLUGIN/tests/_ket-qua"
CLAUDE_BIN="${CLAUDE_BIN:-claude}"

if ! command -v "$CLAUDE_BIN" >/dev/null 2>&1; then
  echo "LỖI: không tìm thấy lệnh '$CLAUDE_BIN'. Đặt CLAUDE_BIN trỏ tới Claude Code CLI." >&2
  exit 2
fi

mkdir -p "$OUT"
loc=("$@")
tong=0; dat=0

chon() {
  [ ${#loc[@]} -eq 0 ] && return 0
  for p in "${loc[@]}"; do [[ "$(basename "$1")" == "$p"* ]] && return 0; done
  return 1
}

for c in "$CASES"/*/; do
  chon "$c" || continue
  ten="$(basename "$c")"
  tong=$((tong+1))
  echo "═══ $ten ═══"
  thu_muc="$OUT/$ten"; rm -rf "$thu_muc"; mkdir -p "$thu_muc"

  de="$(cat "$c/de-bai.txt")"
  dau_vao=""
  if [ -d "$c/dau-vao" ] && [ -n "$(ls -A "$c/dau-vao" 2>/dev/null | grep -v '^\.gitkeep$')" ]; then
    dau_vao=$'\n\nTệp đầu vào kèm theo nằm trong thư mục: '"$c/dau-vao"
  fi

  "$CLAUDE_BIN" -p "Dùng plugin vbhc-vn. $de$dau_vao

Lưu sản phẩm .docx vào thư mục $thu_muc. Chỉ giao file .docx, không giao PDF." \
    >"$thu_muc/nhat-ky.txt" 2>&1

  san_pham="$(find "$thu_muc" -name '*.docx' -print -quit)"
  if [ -z "$san_pham" ]; then
    echo "   KHÔNG ĐẠT — không sinh ra file .docx (xem $thu_muc/nhat-ky.txt)"
    continue
  fi
  echo "   Sản phẩm: $(basename "$san_pham")"

  if python3 "$PLUGIN/tests/cham_case.py" "$san_pham" "$c/tieu-chi.txt"; then
    dat=$((dat+1))
  fi
done

echo
echo "══════════════════════════════════════════════════════════════"
echo "LỚP 2: $dat/$tong case ĐẠT"
[ "$dat" -eq "$tong" ]
