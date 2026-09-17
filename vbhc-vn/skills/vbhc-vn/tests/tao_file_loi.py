# -*- coding: utf-8 -*-
"""tao_file_loi.py — Sinh lại toàn bộ file lỗi trong tests/fail/ một cách TÁI LẬP ĐƯỢC.

Mỗi file lỗi là một bản sao mẫu thật trong examples/ được sửa CÓ CHỦ ĐÍCH đúng một chỗ, kèm
file .expect ghi mã quy tắc bắt buộc bị bắt và dòng nguon: trỏ về mẫu gốc.

Hai điều bắt buộc khi thêm file lỗi mới vào script này:
  1. KHÔNG bịa số hiệu, ngày tháng văn bản — lấy nguyên từ chính mẫu thật hoặc từ
     registry/trang-thai.csv.
  2. Chỉ phá ĐÚNG một thứ. Phá lẫn thứ khác thì bộ hồi quy báo "BẮT THỪA" — đó là
     chốt chặn, không phải phiền toái.

Chạy tại thư mục plugin:  python3 tests/tao_file_loi.py
Sau đó luôn chạy:         python3 tests/run_regression.py
"""
import shutil, re, sys
from pathlib import Path
from docx import Document
from docx.shared import RGBColor, Cm
from docx.oxml.ns import qn

EX = Path('examples'); OUT = Path('tests/fail')


def dat_text(p, moi):
    """Thay text của paragraph mà GIỮ NGUYÊN định dạng run đầu (nghiêng, đậm, cỡ chữ).

    Gán thẳng runs[0].text rồi xóa các run sau là cách nhanh nhất, nhưng nếu run đầu không
    mang định dạng của đoạn (vd run đầu chỉ là khoảng trắng) thì đoạn mất nghiêng/đậm — đã
    làm hỏng một file lỗi ngày 16/9/2026. Nên chọn run ĐẦU TIÊN CÓ CHỮ làm run giữ lại."""
    co_chu = [r for r in p.runs if r.text.strip()]
    giu = co_chu[0] if co_chu else p.runs[0]
    # So theo phần tử XML: p.runs trả object bọc MỚI mỗi lần gọi nên `is not` luôn đúng.
    for r in p.runs:
        if r._element is not giu._element:
            r.text = ''
    giu.text = moi
OUT.mkdir(parents=True, exist_ok=True)

NGUON = {}


def sao(src, ten):
    p = OUT / ten
    shutil.copy(EX / src, p)
    NGUON[ten] = 'examples/' + src
    return p


def ghi_expect(p, ma_bat_buoc, ghi_chu):
    (p.with_suffix('.expect')).write_text(
        "# File lỗi NHÂN TẠO — sinh bằng tests/tao_file_loi.py từ bản sao mẫu thật.\n"
        f"# {ghi_chu}\n"
        f"nguon: {NGUON[p.name]}\n"
        + "\n".join(ma_bat_buoc) + "\n", encoding='utf-8')

def dau_tien(doc, dk):
    for p in doc.paragraphs:
        if dk(p.text): return p
    for t in doc.tables:
        for r in t.rows:
            for c in r.cells:
                for p in c.paragraphs:
                    if dk(p.text): return p
    return None

# ── R01: dẫn văn bản trần ở dòng Căn cứ ──────────────────────────────
p = sao('sct/to-trinh-vbqppl-tien-chat-thuoc-no.docx', 'r01-dan-van-ban-tran.docx')
d = Document(str(p))
neo = d.paragraphs[12]
if not neo.text.strip().startswith('Căn cứ'): sys.exit('R01: đoạn 12 không phải dòng Căn cứ')
from copy import deepcopy
from docx.text.paragraph import Paragraph
moi_p = deepcopy(neo._p); neo._p.addnext(moi_p)
np = Paragraph(moi_p, neo._parent)
# Số hiệu 1936/SCT-CN lấy NGUYÊN từ chính mẫu thật (đoạn 18), chỉ bỏ ngày ban hành.
dat_text(np, 'Căn cứ Văn bản số 1936/SCT-CN của Sở Công Thương;')
d.save(str(p))
ghi_expect(p, ['R01 FAIL'],
           'Chèn một dòng Căn cứ dẫn văn bản TRẦN (không ngày ban hành, không cơ quan đầy đủ).')

# ── R02: công thức hóa học phẳng ─────────────────────────────────────
p = sao('sct/bao-cao-tinh-hinh-trien-khai-ccn.docx', 'r02-cong-thuc-hoa-hoc-phang.docx')
d = Document(str(p))
alt = dau_tien(d, lambda t: len(t.strip()) > 80)
dat_text(alt, 'Cơ sở sử dụng H2SO4 và P2O5 trong dây chuyền. ' + alt.text)
d.save(str(p))
ghi_expect(p, ['R02 FAIL'], 'Chèn câu có H2SO4, P2O5 viết phẳng (không có run subscript).')

# ── R03: còn chỗ trống + chữ tím ─────────────────────────────────────
p = sao('sct/cong-van-de-nghi-bo-sung-ho-so.docx', 'r03-con-cho-trong-va-chu-tim.docx')
d = Document(str(p))
alt = dau_tien(d, lambda t: len(t.strip()) > 80)
dat_text(alt, 'Số lượng hồ sơ còn thiếu: …… bộ (nêu số liệu). ' + alt.text)
r = alt.add_run(' Nội dung này sẽ rà lại sau.')
r.font.color.rgb = RGBColor(0x70, 0x30, 0xA0)
d.save(str(p))
ghi_expect(p, ['R03 WARN'], 'Chèn "……", "(nêu số liệu)" và một run màu tím 7030A0. --final nâng thành FAIL.')

# ── R04: Kính gửi in đậm ─────────────────────────────────────────────
p = sao('sct/cong-van-xin-y-kien-cac-co-quan-phuong-an-ccn-von-nsnn.docx', 'r04-kinh-gui-in-dam.docx')
d = Document(str(p))
alt = dau_tien(d, lambda t: t.strip().startswith('Kính gửi'))
for r in alt.runs: r.bold = True
d.save(str(p))
ghi_expect(p, ['R04 FAIL'], 'Bôi đậm dòng "Kính gửi:" (lỗi thật đã ghi nhận).')

# ── R06: doanh nghiệp đứng dòng đầu Nơi nhận ─────────────────────────
p = sao('sct/giay-phep-van-chuyen-hhnh.docx', 'r06-doanh-nghiep-dong-dau-noi-nhan.docx')
d = Document(str(p))
alt = dau_tien(d, lambda t: t.strip().startswith('Nơi nhận'))
if alt is None: sys.exit('R06: không tìm được Nơi nhận')
from copy import deepcopy
moi_p = deepcopy(alt._p)
alt._p.addnext(moi_p)
from docx.text.paragraph import Paragraph
np = Paragraph(moi_p, alt._parent)
dat_text(np, '- Công ty TNHH Vật tư chuyên dùng xăng dầu An Khang;')
d.save(str(p))
ghi_expect(p, ['R06 FAIL'], 'Chèn tên doanh nghiệp làm dòng ĐẦU của khối Nơi nhận (Bạn chốt 07/9/2026).')

# ── R07: dòng Lưu sai ký hiệu ────────────────────────────────────────
p = sao('sct/bao-cao-ccn-gui-bct-ban-chuan-nguoi-dung.docx', 'r07-dong-luu-sai-ky-hieu.docx')
d = Document(str(p))
alt = dau_tien(d, lambda t: re.match(r'^-?\s*Lưu\s*:', t.strip()))
dat_text(alt, '- Lưu: VT, QLCN(Trung)')
d.save(str(p))
ghi_expect(p, ['R07 FAIL'], 'Đổi "CN" thành "QLCN" và bỏ dấu chấm cuối dòng Lưu.')

# ── R09: thuật ngữ cấm ───────────────────────────────────────────────
p = sao('sct/bao-cao-tinh-hinh-trien-khai-ccn.docx', 'r09-thuat-ngu-cam.docx')
d = Document(str(p))
alt = dau_tien(d, lambda t: len(t.strip()) > 80)
dat_text(alt, 'Trong kỳ đã xảy ra các vụ mất cắp tại kho. ' + alt.text)
d.save(str(p))
ghi_expect(p, ['R09 FAIL'], 'Chèn "các vụ mất cắp" (Nhóm K5 — phải viết "mất, thất thoát").')

# ── R10: giọng giải thích ────────────────────────────────────────────
p = sao('sct/cong-van-don-doc-tien-do-ha-tang-ccn-bao-cao-hang-tuan.docx', 'r10-giong-giai-thich.docx')
d = Document(str(p))
alt = dau_tien(d, lambda t: len(t.strip()) > 80)
dat_text(alt, 'Đây là luồng đầy đủ nhất, doanh nghiệp cần nắm rõ. ' + alt.text)
d.save(str(p))
ghi_expect(p, ['R10 WARN'], 'Chèn 2 mẫu câu Nhóm J đã mắc thật.')

# ── R11: địa danh mất nghiêng + chức danh mất đậm ────────────────────
p = sao('sct/cong-van-moi-hop-sct.docx', 'r11-dia-danh-mat-nghieng.docx')
d = Document(str(p))
for t in d.tables:
    for row in t.rows:
        for c in row.cells:
            for pp in c.paragraphs:
                if re.match(r'^[A-ZĐÀ-Ỹ][^,]{1,24},\s*ngày', pp.text.strip()):
                    for r in pp.runs: r.italic = False
                if pp.text.strip() in ('KT. GIÁM ĐỐC', 'PHÓ GIÁM ĐỐC'):
                    for r in pp.runs: r.bold = False
d.save(str(p))
ghi_expect(p, ['R11 FAIL'], 'Bỏ nghiêng dòng địa danh/ngày và bỏ đậm dòng chức danh.')

# ── R12: lề trang phi lý ─────────────────────────────────────────────
p = sao('sct/cong-van-moi-hop-sct.docx', 'r12-le-trang-phi-ly.docx')
d = Document(str(p))
d.sections[0].left_margin = Cm(0.2)
d.save(str(p))
ghi_expect(p, ['R12 FAIL'], 'Đặt lề trái 0,2 cm (trị số phi lý — dấu hiệu file hỏng).')

# ── R14: dấu vết lần sửa trước ───────────────────────────────────────
p = sao('sct/bao-cao-thang-phong-qlcn.docx', 'r14-dau-vet-lan-sua.docx')
d = Document(str(p))
alt = dau_tien(d, lambda t: len(t.strip()) > 80)
dat_text(alt, '(Bản điều chỉnh, sửa lần 2) ' + alt.text)
d.save(str(p))
ghi_expect(p, ['R14 FAIL'], 'Chèn "(Bản điều chỉnh, sửa lần 2)" vào thân văn bản.')

# ── R05: viện dẫn văn bản CHƯA có hiệu lực tại ngày ký ───────────────
# Dựng lại vụ thật 11/9/2026: NQ 66.25/2026/NQ-CP hiệu lực 15/9/2026 lọt vào văn bản
# ký ngày 11/9/2026. Số hiệu và ngày lấy từ registry/trang-thai.csv, không bịa.
p = sao('sct/cong-van-xin-y-kien-du-thao-vbqppl-bo-nganh.docx', 'r05-vien-dan-chua-co-hieu-luc.docx')
d = Document(str(p))
DIADANH = re.compile(r'^[A-ZĐÀ-Ỹ][^,]{1,24},\s*ngày')
xong = False
for t in d.tables:
    for row in t.rows:
        for c in row.cells:
            for pp in c.paragraphs:
                if not xong and DIADANH.match(pp.text.strip()):
                    dat_text(pp, 'Lào Cai, ngày 11 tháng 9 năm 2026')
                    xong = True
if not xong: sys.exit('R05: không tìm được dòng địa danh')
alt = dau_tien(d, lambda t: len(t.strip()) > 80)
dat_text(alt, 'Căn cứ Nghị quyết số 66.25/2026/NQ-CP ngày 04 tháng 9 năm 2026 của Chính phủ. '
              + alt.text)
d.save(str(p))
ghi_expect(p, ['R05 FAIL'],
           'Đặt ngày ký 11/9/2026 và chèn viện dẫn NQ 66.25/2026/NQ-CP (hiệu lực 15/9/2026).')

# ── Bốn file lỗi cho các HÀM KIỂM CŨ của qa_all.py (tag SZ13, SIGSPACE, HDR-BR, LINES) ──
# Thêm 17/9/2026 khi hiệu chỉnh các hàm này theo mẫu thật: mức FAIL thu hẹp lại, nên phải có
# file lỗi chứng minh chúng vẫn bắt được lỗi thật. .expect ghi "TAG FAIL" — run_regression.py
# thấy mã không bắt đầu bằng R thì chạy qa_all.py để lấy tag.
from docx.shared import Pt
from docx.oxml.ns import qn as _qn
from docx.oxml import OxmlElement

# SZ13: dòng Số đặt cỡ chữ tường minh SAI HẲN (20 = 10pt) — mẫu thật chỉ có trống/26/27/28.
p = sao('sct/cong-van-moi-hop-sct.docx', 'sz13-dong-so-sai-co-chu.docx')
d = Document(str(p))
xong = False
for row in d.tables[0].rows:
    for c in row.cells:
        for pp in c.paragraphs:
            if not xong and re.search(r'Số\s*:', pp.text):
                for r in pp.runs:
                    if r.text.strip(): r.font.size = Pt(10)
                xong = True
if not xong: sys.exit('SZ13: không tìm được dòng Số')
d.save(str(p))
ghi_expect(p, ['SZ13 FAIL'], 'Đặt cỡ chữ dòng "Số:" thành 10pt tường minh (sz=20).')

# SIGSPACE: ô ký chỉ còn 1 dòng trống giữa chức danh và tên (mẫu thật tối thiểu 3).
p = sao('sct/cong-van-moi-hop-sct.docx', 'sigspace-o-ky-thieu-dong-trong.docx')
d = Document(str(p))
right = d.tables[-1].rows[0].cells[-1]
rp = right.paragraphs
ne = [i for i, q in enumerate(rp) if q.text.strip()]
title_i, name_i = ne[-2], ne[-1]
trong = [rp[i] for i in range(title_i + 1, name_i) if not rp[i].text.strip()]
for q in trong[:-1]:
    q._p.getparent().remove(q._p)
d.save(str(p))
ghi_expect(p, ['SIGSPACE FAIL'], 'Xóa bớt dòng trống trong ô ký, chỉ còn 1 dòng giữa chức danh và tên người ký.')

# HDR-BR: chèn <w:br/> vào ô V/v của bảng header thật.
p = sao('sct/cong-van-moi-hop-sct.docx', 'hdrbr-ngat-dong-cung-trong-header.docx')
d = Document(str(p))
xong = False
for row in d.tables[0].rows:
    for c in row.cells:
        for pp in c.paragraphs:
            if not xong and pp.text.strip().startswith('V/v'):
                r = [x for x in pp.runs if x.text.strip()][0]
                br = OxmlElement('w:br'); r._r.append(br)
                xong = True
if not xong: sys.exit('HDR-BR: không tìm được dòng V/v')
d.save(str(p))
ghi_expect(p, ['HDR-BR FAIL'], 'Chèn một thẻ <w:br/> vào dòng V/v trong bảng header (Quy tắc 10).')

# LINES: xóa hết shape Line trong header; .expect có dòng goc: để qa_all so với mẫu gốc.
p = sao('sct/cong-van-moi-hop-sct.docx', 'lines-mat-duong-ke-header.docx')
d = Document(str(p))
n = 0
for el in list(d.element.body.iter(_qn('w:pict'))) + list(d.element.body.iter(_qn('w:drawing'))):
    el.getparent().remove(el); n += 1
if n == 0: sys.exit('LINES: mẫu không có shape')
d.save(str(p))
ghi_expect(p, ['LINES FAIL'], f'Xóa {n} shape Line/drawing khỏi file — so với mẫu gốc qua --goc thì FAIL (Quy tắc 11).')

print('Đã sinh', len(list(OUT.glob('*.docx'))), 'file lỗi')
