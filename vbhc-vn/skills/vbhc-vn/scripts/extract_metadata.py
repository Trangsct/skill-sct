#!/usr/bin/env python3
"""
Trích xuất metadata văn bản hành chính / QPPL Việt Nam từ file PDF.

Output: JSON gồm các trường:
  - co_quan_ban_hanh:   Cơ quan ban hành (UBND TỈNH LÀO CAI, BỘ CÔNG THƯƠNG...)
  - so_van_ban:         Số văn bản (vd. 3861/UBND-NC, 187/2025/NĐ-CP)
  - dia_danh_ngay:      Địa danh + ngày ban hành (Lào Cai, ngày 15 tháng 5 năm 2026)
  - ngay_iso:           Ngày dạng ISO YYYY-MM-DD (nếu parse được)
  - loai_van_ban:       Loại văn bản (CÔNG VĂN, QUYẾT ĐỊNH, TỜ TRÌNH, BÁO CÁO, KẾ HOẠCH, NGHỊ QUYẾT)
  - trich_yeu:          Trích yếu (V/v ... | Ban hành ... | Về việc ...)
  - kinh_gui:           Danh sách "Kính gửi" (nếu là công văn)
  - nguoi_ky:           Người ký
  - chuc_vu_ky:         Chức vụ người ký (kèm KT./TM./TUQ. nếu có)
  - noi_nhan:           Danh sách nơi nhận
  - phuong_phap:        text-extraction | ocr (cách trích xuất)

Cách dùng:
  python extract_metadata.py /path/to/file.pdf
  python extract_metadata.py /path/to/file.pdf --raw   # in kèm raw text
"""

import json
import re
import subprocess
import sys
from pathlib import Path

# Các từ khoá báo hiệu "đã sang trang/khu vực khác" — DỪNG gom right_column
STOP_MARKERS = (
    "CỘNG HÒA",
    "CỘNG HOÀ",
    "Độc lập",
    "ỦY BAN NHÂN DÂN",
    "UỶ BAN NHÂN DÂN",
    "QUY ĐỊNH",
    "QUYẾT ĐỊNH",
    "Chương ",
    "Điều ",
    "Phụ lục",
    "PHỤ LỤC",
)


def run_pdftotext(pdf_path: str, layout: bool = True) -> str:
    """Trích text từ PDF. Trả về '' nếu PDF là ảnh quét (không có text layer)."""
    cmd = ["pdftotext"]
    if layout:
        cmd.append("-layout")
    cmd += [pdf_path, "-"]
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, timeout=60)
        return out.decode("utf-8", errors="replace")
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return ""


def run_ocr(pdf_path: str) -> str:
    """OCR fallback khi PDF không có text layer."""
    try:
        out_pdf = "/tmp/_ocr_temp.pdf"
        subprocess.check_call(
            ["ocrmypdf", "--language", "vie+eng", "--force-ocr",
             "--quiet", pdf_path, out_pdf],
            stderr=subprocess.DEVNULL, timeout=180,
        )
        return run_pdftotext(out_pdf, layout=True)
    except FileNotFoundError:
        return ""
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return ""


def extract_text(pdf_path: str) -> tuple[str, str]:
    """Trả về (text, phuong_phap)."""
    txt = run_pdftotext(pdf_path, layout=True)
    if len(txt.strip()) > 100:
        return txt, "text-extraction"
    ocr_txt = run_ocr(pdf_path)
    if len(ocr_txt.strip()) > 100:
        return ocr_txt, "ocr"
    return txt, "text-extraction"


def _normalize_space(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


# ============================================================
# Các hàm trích xuất từng trường
# ============================================================

def _is_right_only_line(line: str) -> bool:
    """
    Dòng chỉ có 1 cụm text ở cột phải (nhiều khoảng trắng đầu, không có khoảng
    trắng dài giữa các cụm). Ví dụ:
        "                                                  CHỦ TỊCH"
        "                                                  Hoàng Chí Hiền"
    """
    if not line:
        return False
    stripped = line.lstrip()
    if not stripped:
        return False
    leading = len(line) - len(stripped)
    # Có khoảng trắng dài (>=3) giữa 2 cụm → là layout 2 cột bình thường
    if re.search(r"\S\s{3,}\S", line):
        return False
    # Không có 2 cụm; nếu thụt đầu >= 30 → là cột phải
    return leading >= 30


def _left_column(line: str) -> str:
    """Trả về phần trái của dòng có layout 2 cột. Empty nếu là dòng right-only."""
    if _is_right_only_line(line):
        return ""
    s = line
    for marker in ("CỘNG HÒA", "CỘNG HOÀ", "Độc lập", ", ngày", " ngày "):
        idx = s.find(marker)
        if idx > 0:
            s = s[:idx]
    m = re.search(r"\S(\s{3,})\S", s)
    if m:
        s = s[:m.start() + 1]
    return s.rstrip()


def _right_column(line: str) -> str:
    """Trả về phần phải của dòng có layout 2 cột (hoặc cả dòng nếu là right-only)."""
    if _is_right_only_line(line):
        return line.strip()
    s = line
    m = re.search(r"\S(\s{3,})\S", s)
    if m:
        return s[m.end() - 1:].lstrip()
    return ""


def _is_stop_line(s: str) -> bool:
    """
    Một dòng được coi là STOP (đã sang khu vực khác: trang sau, phụ lục, mục mới)
    khi nó BẮT ĐẦU bằng một marker, KHÔNG có prefix:
      - '-', '+', '•' (item Nơi nhận như "- Như Điều 3;")
      - 'TM.', 'KT.', 'TUQ.' (chức vụ ký như "TM. ỦY BAN NHÂN DÂN")
    """
    if not s:
        return False
    stripped = s.strip()
    if not stripped:
        return False
    if stripped.startswith(("-", "+", "•")):
        return False
    if stripped.startswith(("TM.", "KT.", "TUQ.")):
        return False
    for marker in STOP_MARKERS:
        if stripped.startswith(marker):
            return True
    return False


def _is_likely_name(s: str) -> bool:
    """2-5 từ Title Case (chữ cái đầu hoa, các chữ còn lại thường)."""
    tokens = s.split()
    if not (2 <= len(tokens) <= 5):
        return False
    for t in tokens:
        if not t or not t[0].isalpha():
            return False
        if not t[0].isupper() or t.isupper():
            return False
    return True


def extract_co_quan_ban_hanh(text: str) -> str | None:
    """
    Cơ quan ban hành là dòng VIẾT HOA ở đầu văn bản, thường gồm 1-3 dòng:
      ỦY BAN NHÂN DÂN
      TỈNH LÀO CAI
    Hoặc với văn bản của Sở:
      UBND TỈNH LÀO CAI
      SỞ CÔNG THƯƠNG
    """
    lines = text.splitlines()[:25]
    collected = []
    for ln in lines:
        left = _left_column(ln).strip()
        if not left:
            if collected:
                break
            continue
        if re.search(r"\bSố\s*:?\s*\d", left) or re.search(r"ngày\s+\d", left, re.I):
            break
        letters = [c for c in left if c.isalpha()]
        if not letters:
            continue
        upper_ratio = sum(1 for c in letters if c.isupper()) / len(letters)
        if upper_ratio < 0.8:
            if collected:
                break
            continue
        collected.append(left)
        if len(collected) >= 3:
            break
    if not collected:
        return None
    if len(collected) >= 2:
        return _normalize_space(" - ".join(collected))
    return _normalize_space(collected[0])


def extract_so_van_ban(text: str) -> str | None:
    """
    Tìm số ký hiệu văn bản. Hỗ trợ:
      - Số: 3861/UBND-NC
      - Số: 187/2025/NĐ-CP
      - Số: 2984/BNNMT-LNKL
      - Số 37/ĐK-HT
      - Số: 59    /QĐ-SCT     (có khoảng trắng thừa quanh dấu /)
    """
    head = "\n".join(text.splitlines()[:30])
    pat = re.compile(
        r"Số\s*:?\s*"
        r"(?P<so>\d+)"
        r"(?:\s*/\s*(?P<nam>\d{4}))?"
        r"\s*/\s*"
        r"(?P<kh>[A-Za-zĐđÀ-ỹ\-\.]+(?:-[A-Za-zĐđÀ-ỹ\-\.]+)*)",
        re.UNICODE,
    )
    m = pat.search(head)
    if not m:
        return None
    so, nam, kh = m.group("so"), m.group("nam"), m.group("kh")
    if nam:
        return f"{so}/{nam}/{kh}"
    return f"{so}/{kh}"


def extract_dia_danh_ngay(text: str) -> tuple[str | None, str | None]:
    """
    Tìm 'Lào Cai, ngày 15 tháng 5 năm 2026'.

    Hỗ trợ 3 dạng:
    1. Trọn 1 dòng (chuẩn).
    2. Bị tách 2 dòng do typo/scan:
        "Lào Cai, ngày 01 tháng 07"
        "                                6 năm 2025"
    3. Nằm ở cột phải khi cột trái có "Số: ...".

    Validate: địa danh phải có ít nhất 1 chữ thường (để tránh dính "SCT", "QĐ"...).
    """
    head_lines = text.splitlines()[:30]
    pat_full = re.compile(
        r"(?P<diadanh>[A-ZĐÀ-Ỹ][A-Za-zĐđÀ-ỹ\s\.]{1,40}?)\s*,\s*"
        r"ngày\s+(?P<d>\d{1,2})\s+tháng\s+(?P<m>\d{1,2})\s+năm\s+(?P<y>\d{4})",
        re.UNICODE,
    )

    def _strip_so_van_ban(s: str) -> str:
        """Bỏ phần Quốc hiệu, 'Số: X/YYY-ZZZ' để tránh nhiễu vào địa danh."""
        s = re.sub(
            r"Số\s*:?\s*\d+\s*(?:/\s*\d{4})?\s*/\s*[A-Za-zĐđÀ-ỹ\-\.]+",
            "",
            s,
        )
        s = re.sub(
            r"CỘNG\s+HO[ÀA]\s+X[ÃA]\s+HỘI\s+CHỦ\s+NGHĨA\s+VIỆT\s+NAM",
            "",
            s,
            flags=re.IGNORECASE,
        )
        s = re.sub(
            r"Độc\s+lập\s*[-–]\s*Tự\s+do\s*[-–]\s*Hạnh\s+phúc",
            "",
            s,
            flags=re.IGNORECASE,
        )
        return s

    def _ok_diadanh(d: str) -> bool:
        """Địa danh hợp lệ: có chữ thường (tránh dính 'SCT', 'QĐ'...)."""
        return bool(re.search(r"[a-zà-ỹ]", d))

    # B1: thử match trọn 1 dòng
    for ln in head_lines:
        right = _right_column(ln)
        target = _strip_so_van_ban(right if right else ln)
        m = pat_full.search(target)
        if m and _ok_diadanh(m.group("diadanh")):
            d, mo, y = int(m.group("d")), int(m.group("m")), int(m.group("y"))
            diadanh = m.group("diadanh").strip()
            full = f"{diadanh}, ngày {d:02d} tháng {mo} năm {y}"
            return full, f"{y:04d}-{mo:02d}-{d:02d}"

    # B2: gộp dòng để xử lý ngày bị tách
    pat_split = re.compile(
        r"(?P<diadanh>[A-ZĐÀ-Ỹ][A-Za-zĐđÀ-ỹ\s\.]{1,40}?)\s*,\s*"
        r"ngày\s+(?P<d>\d{1,2})\s+tháng\s+(?P<m>\d{1,2})\b"
        r"[^\n]*?\s+năm\s+(?P<y>\d{4})",
        re.UNICODE | re.DOTALL,
    )
    for i in range(len(head_lines) - 1):
        right_i = _right_column(head_lines[i])
        if right_i:
            chunk = right_i
            for j in range(1, 4):
                if i + j < len(head_lines):
                    chunk += " " + head_lines[i + j].strip()
            chunk = _strip_so_van_ban(chunk)
            m = pat_split.search(chunk)
            if m and _ok_diadanh(m.group("diadanh")):
                d, mo, y = int(m.group("d")), int(m.group("m")), int(m.group("y"))
                full = f"{m.group('diadanh').strip()}, ngày {d:02d} tháng {mo} năm {y}"
                return full, f"{y:04d}-{mo:02d}-{d:02d}"
        chunk = head_lines[i]
        for j in range(1, 4):
            if i + j < len(head_lines):
                chunk += " " + head_lines[i + j]
        chunk = _strip_so_van_ban(chunk)
        m = pat_split.search(chunk)
        if m and _ok_diadanh(m.group("diadanh")):
            d, mo, y = int(m.group("d")), int(m.group("m")), int(m.group("y"))
            full = f"{m.group('diadanh').strip()}, ngày {d:02d} tháng {mo} năm {y}"
            return full, f"{y:04d}-{mo:02d}-{d:02d}"
    return None, None


def extract_loai_van_ban(text: str) -> str | None:
    """
    Loại văn bản: dòng VIẾT HOA toàn bộ nằm dưới phần header (Số/ngày).
    """
    keywords = ["QUYẾT ĐỊNH", "TỜ TRÌNH", "BÁO CÁO", "KẾ HOẠCH",
                "NGHỊ QUYẾT", "CHỈ THỊ", "THÔNG BÁO", "CÔNG VĂN"]
    for ln in text.splitlines()[:30]:
        s = ln.strip()
        for kw in keywords:
            if s == kw or (s.startswith(kw) and len(s) <= len(kw) + 5):
                return kw
    if re.search(r"\bV\s*[/.]\s*v\b", text[:2000]):
        return "CÔNG VĂN"
    return None


def extract_trich_yeu(text: str) -> str | None:
    """
    Trích yếu của văn bản. 2 dạng:
    1. CÔNG VĂN: bắt đầu bằng "V/v ..."
    2. QĐ, TTr, BC, KH, NQ: nằm DƯỚI tên loại văn bản (VIẾT HOA).
    """
    lines = text.splitlines()[:50]

    # Dạng 1: V/v
    start_idx = None
    for i, ln in enumerate(lines):
        if re.match(r"\s*V\s*[/.]\s*v\b", ln):
            start_idx = i
            break
    if start_idx is not None:
        collected = []
        for ln in lines[start_idx:start_idx + 8]:
            s = ln.strip()
            if not s:
                if collected:
                    break
                continue
            if re.match(r"Kính\s+gửi", s, re.I) or ("ngày" in s and "tháng" in s and "năm" in s):
                break
            collected.append(s)
        out = _normalize_space(" ".join(collected))
        out = re.sub(r"^V\s*[/.]\s*v\b\s*", "", out)
        if out:
            return out

    # Dạng 2: dưới tên loại văn bản
    type_keywords = ["QUYẾT ĐỊNH", "TỜ TRÌNH", "BÁO CÁO", "KẾ HOẠCH",
                     "NGHỊ QUYẾT", "CHỈ THỊ", "THÔNG BÁO"]
    type_idx = None
    for i, ln in enumerate(lines):
        s = ln.strip()
        if s in type_keywords:
            type_idx = i
            break
    if type_idx is None:
        return None
    collected = []
    for ln in lines[type_idx + 1:type_idx + 8]:
        s = ln.strip()
        if not s:
            if collected:
                break
            continue
        if s.startswith(("Căn cứ", "Thực hiện ", "Theo đề nghị")):
            break
        # Dừng nếu là dòng VIẾT HOA dài (như "GIÁM ĐỐC SỞ CÔNG THƯƠNG TỈNH LÀO CAI")
        letters = [c for c in s if c.isalpha()]
        if letters and sum(1 for c in letters if c.isupper()) / len(letters) > 0.9 and len(s) > 15:
            break
        collected.append(s)
    out = _normalize_space(" ".join(collected))
    return out or None


def extract_kinh_gui(text: str) -> list[str]:
    """Liệt kê các đơn vị kính gửi."""
    lines = text.splitlines()
    start = None
    for i, ln in enumerate(lines):
        if re.match(r"\s*Kính\s+gửi", ln, re.I):
            start = i
            break
    if start is None:
        return []
    items = []
    for ln in lines[start:start + 30]:
        s = ln.strip().lstrip("•").strip()
        m = re.match(r"^[-+•]\s*(.+?)\s*[;,.]?\s*$", s)
        if m:
            items.append(m.group(1).strip())
        elif items and (not s or re.match(r"^[A-ZĐÀ-Ỹ][a-zà-ỹ]", s)):
            break
    return items


def extract_nguoi_ky(text: str) -> tuple[str | None, str | None]:
    """
    Người ký + chức vụ ở cuối văn bản, cấu trúc layout 2 cột.
    Quy tắc: DỪNG gom khi gặp Quốc hiệu/UBND/Chương/Điều/Phụ lục.
    """
    lines = text.splitlines()
    start = None
    end_luu = None
    for i, ln in enumerate(lines):
        if start is None and re.match(r"\s*Nơi\s+nhận", ln, re.I):
            start = i
        if start is not None and re.search(r"-\s*Lưu\s*:", ln):
            end_luu = i
            break
    if start is None:
        return None, None

    upper_bound = min(end_luu + 8, len(lines)) if end_luu is not None else min(start + 30, len(lines))
    pool = []
    for ln in lines[start:upper_bound]:
        right = _right_column(ln).strip()
        if right:
            if _is_stop_line(right):
                break
            pool.append(right)

    if end_luu is not None:
        for ln in lines[end_luu + 1:end_luu + 12]:
            s = ln.strip()
            if not s:
                continue
            if _is_stop_line(s):
                break
            left = _left_column(ln).strip()
            right = _right_column(ln).strip()
            if not left and right:
                pool.append(right)
            elif left and not right:
                if (s.isupper() and len(s) < 60) or _is_likely_name(s):
                    pool.append(s)

    if not pool:
        return None, None

    sign_keywords = ("KT.", "TM.", "TUQ.", "CHỦ TỊCH", "GIÁM ĐỐC",
                     "BỘ TRƯỞNG", "THỦ TƯỚNG", "CHỦ NHIỆM", "TRƯỞNG BAN",
                     "PHÓ CHỦ TỊCH", "PHÓ GIÁM ĐỐC", "VIỆN TRƯỞNG", "CỤC TRƯỞNG")
    idx_sign = None
    for i, ln in enumerate(pool):
        if any(kw in ln for kw in sign_keywords):
            idx_sign = i
            break
    if idx_sign is None:
        return None, None

    chuc_vu_parts = [pool[idx_sign].strip()]
    j = idx_sign + 1
    while j < min(idx_sign + 4, len(pool)):
        s = pool[j].strip()
        if not s:
            j += 1
            continue
        if _is_stop_line(s):
            break
        letters = [c for c in s if c.isalpha()]
        if not letters:
            break
        upper_ratio = sum(1 for c in letters if c.isupper()) / len(letters)
        if upper_ratio >= 0.7 and not s.startswith(("-", "+", "•")):
            chuc_vu_parts.append(s)
            j += 1
        else:
            break
    chuc_vu = _normalize_space(" - ".join(chuc_vu_parts))

    name = None
    for k in range(j, min(j + 10, len(pool))):
        s = pool[k].strip()
        if not s or s.startswith(("-", "+", "•")):
            continue
        if _is_stop_line(s):
            break
        if "Nơi nhận" in s or "Lưu" in s:
            continue
        if _is_likely_name(s):
            name = s
            break
    return name, chuc_vu


def extract_noi_nhan(text: str) -> list[str]:
    """
    Liệt kê 'Nơi nhận' ở cuối văn bản — chỉ lấy cột trái.
    KHÔNG break khi gặp dòng trống cột trái (vì cột phải có chức vụ chen giữa).
    Chỉ break khi gặp "Lưu:" (item cuối) hoặc stop marker.
    """
    lines = text.splitlines()
    start = None
    for i, ln in enumerate(lines):
        if re.match(r"\s*Nơi\s+nhận", ln, re.I):
            start = i
            break
    if start is None:
        return []
    items = []
    seen_luu = False
    for ln in lines[start + 1:start + 40]:
        if _is_stop_line(ln):
            break
        if seen_luu:
            break
        left = _left_column(ln)
        s = left.strip()
        if not s:
            continue
        m = re.match(r"^[-+•]\s*(.+?)\s*[;,.]?\s*$", s)
        if m:
            item = m.group(1).strip()
            items.append(item)
            if re.match(r"Lưu\s*:", item, re.I):
                seen_luu = True
        else:
            if any(kw in s for kw in ("KT.", "TM.", "CHỦ TỊCH", "GIÁM ĐỐC", "BỘ TRƯỞNG")):
                break
    return items


# ============================================================
# Main
# ============================================================

def extract_all(pdf_path: str) -> dict:
    text, method = extract_text(pdf_path)
    dia_danh_ngay, ngay_iso = extract_dia_danh_ngay(text)
    nguoi_ky, chuc_vu = extract_nguoi_ky(text)
    return {
        "file": str(Path(pdf_path).name),
        "phuong_phap": method,
        "co_quan_ban_hanh": extract_co_quan_ban_hanh(text),
        "so_van_ban": extract_so_van_ban(text),
        "dia_danh_ngay": dia_danh_ngay,
        "ngay_iso": ngay_iso,
        "loai_van_ban": extract_loai_van_ban(text),
        "trich_yeu": extract_trich_yeu(text),
        "kinh_gui": extract_kinh_gui(text),
        "nguoi_ky": nguoi_ky,
        "chuc_vu_ky": chuc_vu,
        "noi_nhan": extract_noi_nhan(text),
    }


def main():
    if len(sys.argv) < 2:
        print("Cách dùng: python extract_metadata.py <file.pdf> [--raw]", file=sys.stderr)
        sys.exit(1)
    pdf_path = sys.argv[1]
    show_raw = "--raw" in sys.argv
    if not Path(pdf_path).exists():
        print(f"Không tìm thấy file: {pdf_path}", file=sys.stderr)
        sys.exit(1)
    result = extract_all(pdf_path)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if show_raw:
        print("\n" + "=" * 60 + "\nRAW TEXT (pdftotext -layout)\n" + "=" * 60)
        text, _ = extract_text(pdf_path)
        print(text)


if __name__ == "__main__":
    main()
