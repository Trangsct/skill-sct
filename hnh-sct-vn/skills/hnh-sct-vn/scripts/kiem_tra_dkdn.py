#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra dữ kiện đăng ký doanh nghiệp trong dự thảo Giấy phép sử dụng VLNCN.

Chạy TRƯỚC khi xuất file (anti-error 38 — vụ GP 5890/GP-SCT cấp sai mã số doanh nghiệp):

    python3 scripts/kiem_tra_dkdn.py "du-thao-GP.docx" --dkdn "6.2 Dang ky kinh doanh.pdf"
    python3 scripts/kiem_tra_dkdn.py "du-thao-GP.docx" --ma-so 0123456789

Kiểm 3 việc:
  1. Lấy mã số doanh nghiệp ghi trong dự thảo (Điều 1).
  2. So với mã số đọc từ bản gốc Giấy chứng nhận đăng ký doanh nghiệp (--dkdn: PDF/ảnh,
     tự OCR bằng tesseract nếu bản scan không có lớp chữ) hoặc với --ma-so do người dùng nhập.
  3. Đối chiếu hai chữ số đầu của mã số với tỉnh của cơ quan cấp ghi ngay trong câu, và cảnh báo
     khi câu còn ghi "Sở Kế hoạch và Đầu tư" cho bản đăng ký cấp từ năm 2025 trở đi.

Mã trả về: 0 = đạt, 1 = có cảnh báo cần xử lý, 2 = lỗi đầu vào.
"""
import argparse
import os
import re
import subprocess
import sys
import tempfile

# Đầu mã số doanh nghiệp theo tỉnh nơi đăng ký — các dải đã gặp trong hồ sơ của Sở.
# Bổ sung dần khi gặp tỉnh mới; chỉ dùng để CẢNH BÁO, không dùng để kết luận.
DAU_MA_THEO_TINH = {
    "5000": ["tuyên quang", "tuyen quang"],
    "5200": ["yên bái", "yen bai"],
    "5300": ["lào cai", "lao cai"],
    "0100": ["hà nội", "ha noi"],
    "0101": ["hà nội", "ha noi"],
    "0102": ["hà nội", "ha noi"],
    "0103": ["hà nội", "ha noi"],
    "0104": ["hà nội", "ha noi"],
    "0105": ["hà nội", "ha noi"],
    "0106": ["hà nội", "ha noi"],
    "0107": ["hà nội", "ha noi"],
    "0108": ["hà nội", "ha noi"],
    "0109": ["hà nội", "ha noi"],
    "0110": ["hà nội", "ha noi"],
}

CAU_DKDN = re.compile(
    r"Giấy chứng nhận đăng ký doanh nghiệp[^.;]{0,400}", re.IGNORECASE)
MA_SO = re.compile(r"\b(\d{10})(?:-\d{3})?\b")


def chu_tu_docx(duong_dan):
    try:
        from docx import Document
    except ImportError:
        sys.exit("Thiếu python-docx: pip install python-docx --break-system-packages")
    d = Document(duong_dan)
    phan = [p.text for p in d.paragraphs]
    for bang in d.tables:
        for hang in bang.rows:
            for o in hang.cells:
                phan.append(o.text)
    return "\n".join(phan)


def chu_tu_pdf(duong_dan):
    try:
        ra = subprocess.run(["pdftotext", "-layout", duong_dan, "-"],
                            capture_output=True, text=True, timeout=120)
        chu = ra.stdout or ""
    except (OSError, subprocess.SubprocessError):
        chu = ""
    if len(chu.strip()) >= 40:
        return chu
    # bản scan → OCR từng trang
    with tempfile.TemporaryDirectory() as tmp:
        try:
            subprocess.run(["pdftoppm", "-r", "300", "-png", duong_dan,
                            os.path.join(tmp, "t")], check=True, timeout=300)
        except (OSError, subprocess.SubprocessError):
            return chu
        gom = []
        for ten in sorted(os.listdir(tmp)):
            try:
                ra = subprocess.run(["tesseract", os.path.join(tmp, ten), "stdout", "-l", "vie"],
                                    capture_output=True, text=True, timeout=300)
                gom.append(ra.stdout or "")
            except (OSError, subprocess.SubprocessError):
                return chu + "\n[khong-ocr-duoc]"
        return chu + "\n".join(gom)


def doc_chu(duong_dan):
    duoi = os.path.splitext(duong_dan)[1].lower()
    if duoi == ".docx":
        return chu_tu_docx(duong_dan)
    if duoi == ".pdf":
        return chu_tu_pdf(duong_dan)
    sys.exit("Chỉ nhận .docx (dự thảo) và .pdf (bản đăng ký doanh nghiệp): %s" % duong_dan)


def main():
    ap = argparse.ArgumentParser(description="Kiểm tra mã số doanh nghiệp trong dự thảo Giấy phép")
    ap.add_argument("du_thao", help="Dự thảo Giấy phép (.docx) hoặc văn bản đã ban hành (.pdf)")
    ap.add_argument("--dkdn", help="Bản Giấy chứng nhận đăng ký doanh nghiệp trong hồ sơ (.pdf)")
    ap.add_argument("--ma-so", help="Mã số doanh nghiệp đúng, nhập tay khi không có tệp")
    tham_so = ap.parse_args()

    chu = doc_chu(tham_so.du_thao)
    cau = CAU_DKDN.search(chu)
    if not cau:
        print("[LỖI] Không tìm thấy cụm 'Giấy chứng nhận đăng ký doanh nghiệp' trong dự thảo.")
        return 2
    cau = " ".join(cau.group(0).split())
    ma_du_thao = MA_SO.search(cau)
    if not ma_du_thao:
        print("[LỖI] Cụm nhận dạng không có mã số 10 chữ số:\n  %s" % cau)
        return 2
    ma_du_thao = ma_du_thao.group(1)
    print("Dự thảo ghi: %s" % cau)
    print("Mã số trong dự thảo: %s" % ma_du_thao)

    canh_bao = []

    # (1) so với bản gốc
    ma_goc = None
    if tham_so.dkdn:
        chu_goc = doc_chu(tham_so.dkdn)
        m = re.search(r"[Mm]ã số doanh nghiệp[^0-9]{0,20}(\d{10})", chu_goc)
        if not m:
            ds = MA_SO.findall(chu_goc)
            m = ds[0] if ds else None
            ma_goc = m
        else:
            ma_goc = m.group(1)
        if ma_goc is None:
            canh_bao.append("Không đọc được mã số từ bản đăng ký doanh nghiệp "
                            "(bản scan chưa OCR được) — PHẢI đối chiếu bằng mắt trước khi trình.")
        else:
            print("Mã số trên bản đăng ký doanh nghiệp: %s" % ma_goc)
    elif tham_so.ma_so:
        ma_goc = re.sub(r"\D", "", tham_so.ma_so)
    else:
        canh_bao.append("Chưa có nguồn đối chiếu (--dkdn hoặc --ma-so): không kết luận được mã số đúng hay sai.")

    if ma_goc and ma_goc != ma_du_thao:
        canh_bao.append("MÃ SỐ LỆCH: dự thảo %s — bản gốc %s. Sửa cả cụm nhận dạng theo bản gốc."
                        % (ma_du_thao, ma_goc))

    # (2) đầu mã số so với tỉnh của cơ quan cấp ghi trong câu
    cau_thuong = cau.lower()
    dau = ma_du_thao[:4]
    tinh_cua_dau = DAU_MA_THEO_TINH.get(dau)
    if tinh_cua_dau and not any(tinh in cau_thuong for tinh in tinh_cua_dau):
        canh_bao.append("Đầu mã %s thuộc dải %s nhưng câu không ghi tỉnh đó — mở bản gốc kiểm lại."
                        % (dau, "/".join(tinh_cua_dau[:1])))

    # (3) cơ quan cấp
    if "kế hoạch và đầu tư" in cau_thuong:
        nam = re.findall(r"ngày\s+\d{1,2}/\d{1,2}/(\d{4})", cau)
        nam_cuoi = max((int(n) for n in nam), default=0)
        if nam_cuoi >= 2025:
            canh_bao.append("Câu ghi 'Sở Kế hoạch và Đầu tư' nhưng bản đăng ký ghi ngày năm %d — "
                            "bản cấp từ 2025 do Phòng Doanh nghiệp và Đăng ký kinh doanh - Sở Tài chính cấp."
                            % nam_cuoi)

    if canh_bao:
        print("\nKẾT QUẢ: CÓ CẢNH BÁO")
        for c in canh_bao:
            print("  [!] %s" % c)
        return 1
    print("\nKẾT QUẢ: ĐẠT")
    return 0


if __name__ == "__main__":
    sys.exit(main())
