#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""trang_thai_lib.py — hàm dùng chung cho tệp trạng thái hồ sơ trong trang-thai/ (Bạn chốt 17/10/2026).

Không chạy trực tiếp. Được nhập bởi:
  scripts/tim_ho_so.py         — chọn tệp trạng thái từ câu yêu cầu của Bạn
  scripts/trang_thai_ho_so.py  — liệt kê mọi hồ sơ: tên, ngày cập nhật cuối, bước tiếp theo
  scripts/ghi_nhat_ky.py       — ghi nhật ký cuối phiên, cập nhật các mục của tệp
  scripts/check_trang_thai.py  — CI: tệp đủ mục của mẫu, dòng nhật ký cuối có ngày, không lộ thông tin riêng

Bố cục một tệp (xem trang-thai/MAU.md):
  # <Tên hồ sơ>
  Bí danh: a; b; c
  Plugin liên quan: kccn-sct-vn, vbhc-vn
  ## Văn bản đã phát hành          (bảng Markdown)
  ## Bước đã xong                   (danh sách đánh số, mỗi dòng có ngày)
  ## Bước tiếp theo
  ## Vướng mắc, câu hỏi còn mở
  ## Quyết định của Bạn
  ## Yêu cầu riêng một lần
  ## Nhật ký phiên                  (mỗi phiên một mục "### dd/mm/yyyy", hoặc "### Tóm tắt đến ngày dd/mm/yyyy")
"""
from __future__ import annotations

import re
import unicodedata
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
THU_MUC = REPO / "trang-thai"
BO_QUA = {"MAU.md", "README.md"}

MUC = [
    "Văn bản đã phát hành",
    "Bước đã xong",
    "Bước tiếp theo",
    "Vướng mắc, câu hỏi còn mở",
    "Quyết định của Bạn",
    "Yêu cầu riêng một lần",
    "Nhật ký phiên",
]
NGAY = re.compile(r"\b(\d{1,2})/(\d{1,2})/(\d{4})\b")
DE_NHAT_KY = re.compile(r"^###\s+(?:Tóm tắt đến ngày\s+)?(\d{1,2}/\d{1,2}/\d{4})\b")
TRONG = "chưa có thông tin trong kho"

# Kho skill-sct CÔNG KHAI (mục 6.2 bản giao việc 17/10/2026): không ghi số điện thoại, tài khoản,
# người đại diện, thông tin đăng ký của doanh nghiệp, sức khỏe, đời tư. Chỉ tên công ty và số giấy phép.
CAM = [
    (re.compile(r"(?<![\d/.])(?:\+?84|0)(?:[\s.\-]?\d){8,10}(?![\d/])"), "số điện thoại"),
    (re.compile(r"số\s+tài\s+khoản|tài\s+khoản\s+ngân\s+hàng|\bSTK\b", re.I), "tài khoản ngân hàng"),
    (re.compile(r"người\s+đại\s+diện\s+theo\s+pháp\s+luật|căn\s+cước|\bCCCD\b|\bCMND\b", re.I),
     "người đại diện / giấy tờ tùy thân"),
    (re.compile(r"mã\s+số\s+thuế|giấy\s+chứng\s+nhận\s+đăng\s+ký\s+(?:doanh\s+nghiệp|kinh\s+doanh)", re.I),
     "thông tin đăng ký doanh nghiệp"),
    (re.compile(r"nằm\s+viện|ốm\s+đau|bệnh\s+án|nghỉ\s+ốm|thai\s+sản|ly\s+hôn|hoàn\s+cảnh\s+gia\s+đình", re.I),
     "sức khỏe, đời tư"),
]


def nfc(s: str) -> str:
    return unicodedata.normalize("NFC", s or "")


def bo_dau(s: str) -> str:
    s = unicodedata.normalize("NFD", nfc(s))
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.replace("đ", "d").replace("Đ", "D").lower()


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", bo_dau(s)).strip("-")


def hom_nay() -> str:
    d = date.today()
    return f"{d.day:02d}/{d.month:02d}/{d.year}"


def ngay_khoa(s: str) -> tuple[int, int, int]:
    m = NGAY.search(s or "")
    if not m:
        return (0, 0, 0)
    d, mo, y = (int(x) for x in m.groups())
    return (y, mo, d)


def cac_tep() -> list[Path]:
    if not THU_MUC.is_dir():
        return []
    return sorted(p for p in THU_MUC.glob("*.md") if p.name not in BO_QUA)


def kiem_rieng_tu(text: str) -> list[str]:
    """Các loại thông tin riêng tư lọt vào nội dung (để từ chối ghi / báo đỏ trên CI)."""
    ra = []
    for rx, ten in CAM:
        m = rx.search(nfc(text))
        if m:
            ra.append(f"{ten}: '{m.group(0)}'")
    return ra


class HoSo:
    """Một tệp trạng thái, tách thành phần đầu (trước mục ## đầu tiên) và các mục ## theo thứ tự."""

    def __init__(self, path: Path):
        self.path = Path(path)
        self.dau: list[str] = []
        self.muc: dict[str, list[str]] = {}
        self.thu_tu: list[str] = []
        hien = None
        for ln in nfc(self.path.read_text(encoding="utf-8")).splitlines():
            if ln.startswith("## "):
                hien = ln[3:].strip()
                self.thu_tu.append(hien)
                self.muc[hien] = []
            elif hien is None:
                self.dau.append(ln)
            else:
                self.muc[hien].append(ln)

    # ── thuộc tính đọc ─────────────────────────────────────────
    @property
    def ten(self) -> str:
        for ln in self.dau:
            if ln.startswith("# "):
                return ln[2:].strip()
        return self.path.stem

    def _truong(self, khoa: str) -> str:
        for ln in self.dau:
            if ln.lower().startswith(khoa.lower() + ":"):
                return ln.split(":", 1)[1].strip()
        return ""

    @property
    def bi_danh(self) -> list[str]:
        return [x.strip() for x in re.split(r"[;,]", self._truong("Bí danh")) if x.strip()]

    @property
    def plugins(self) -> list[str]:
        return [x.strip() for x in re.split(r"[;,\s]+", self._truong("Plugin liên quan")) if x.strip()]

    def dong(self, muc: str) -> list[str]:
        return [ln for ln in self.muc.get(muc, []) if ln.strip()]

    def muc_nhat_ky(self) -> list[tuple[str, list[str]]]:
        """[(dòng tiêu đề ###, các dòng nội dung)] theo thứ tự trong tệp."""
        ra: list[tuple[str, list[str]]] = []
        for ln in self.muc.get("Nhật ký phiên", []):
            if ln.startswith("### "):
                ra.append((ln, []))
            elif ra:
                ra[-1][1].append(ln)
        return ra

    @property
    def ngay_cap_nhat(self) -> str:
        cac = [DE_NHAT_KY.match(h) for h, _ in self.muc_nhat_ky()]
        ngay = [m.group(1) for m in cac if m]
        return max(ngay, key=ngay_khoa) if ngay else ""

    @property
    def buoc_tiep_theo(self) -> str:
        for ln in self.dong("Bước tiếp theo"):
            return re.sub(r"^\s*(?:[-*]|\d+\.)\s*", "", ln).strip()
        return ""

    # ── ghi ────────────────────────────────────────────────────
    def dat(self, muc: str, dong: list[str]) -> None:
        if muc not in self.muc:
            self.thu_tu.append(muc)
        self.muc[muc] = [""] + dong + [""]

    def them(self, muc: str, dong: list[str]) -> None:
        cu = [ln for ln in self.muc.get(muc, []) if ln.strip()]
        cu = [ln for ln in cu if TRONG not in ln]  # bỏ dòng giữ chỗ khi đã có nội dung thật
        self.dat(muc, cu + dong)

    def van_ban(self) -> str:
        ra = list(self.dau)
        while ra and not ra[-1].strip():
            ra.pop()
        for m in self.thu_tu:
            ra += ["", f"## {m}"]
            noi = list(self.muc[m])
            while noi and not noi[0].strip():
                noi.pop(0)
            while noi and not noi[-1].strip():
                noi.pop()
            ra += [""] + noi if noi else []
        return "\n".join(ra).rstrip() + "\n"

    def luu(self) -> None:
        self.path.write_text(self.van_ban(), encoding="utf-8")
