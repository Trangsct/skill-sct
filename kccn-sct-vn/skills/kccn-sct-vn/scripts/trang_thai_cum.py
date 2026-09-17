#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GATE TRẠNG THÁI HỒ SƠ — tra bậc thủ tục hiện tại của một CCN/KCN trước khi soạn văn bản.

Dùng:
    python3 scripts/trang_thai_cum.py "Châu Quế"
    python3 scripts/trang_thai_cum.py "Mông Sơn" --all      # in mọi dòng, kể cả dòng không có số văn bản

Script quét references/, vi-du-thuc-te/, checklists/, mau-van-ban/ của plugin kccn-sct-vn, lọc các dòng
nhắc tên cụm, gắn mỗi dòng vào một bậc thủ tục (bảng bậc ở references/39-gate-trang-thai-ho-so-cum.md)
và kết luận bậc cao nhất đã đạt. Kết quả là CĂN CỨ ĐỂ HỎI LẠI người dùng, không phải kết luận cuối cùng:
plugin chỉ ghi đến kỳ cập nhật gần nhất.
"""

import argparse
import datetime
import os
import re
import sys
import unicodedata

THU_MUC_QUET = ['references', 'vi-du-thuc-te', 'checklists', 'mau-van-ban']

# (bậc, tên bậc, các mẫu nhận dạng trong câu chữ)
BAC = [
    (1, 'Quy hoạch, danh mục thu hút đầu tư',
     [r'qđ\s*525', r'qđ\s*1382', r'phụ lục iii']),
    (2, 'Xã thông báo công khai tiếp nhận hồ sơ',
     [r'tb\s*\d+/tb-ubnd', r'thông báo (công khai )?tiếp nhận', r'thông báo kêu gọi']),
    (3, 'Nhà đầu tư nộp hồ sơ; xã trình Sở',
     [r'ttr-ubnd', r'xã trình', r'phường trình', r'báo cáo đầu tư']),
    (4, 'Sở lấy ý kiến sở, ngành',
     [r'lấy ý kiến sở', r'xin ý kiến sở', r'ý kiến thẩm định']),
    (5, 'Cử cán bộ, trình thành lập Hội đồng',
     [r'cử cán bộ', r'trình (thành )?lập hội đồng', r'trình thành lập hội đồng']),
    (6, 'ĐÃ CÓ Quyết định thành lập Hội đồng, Tổ giúp việc',
     [r'thành lập hội đồng[^\n]{0,60}(qđ|quyết định)', r'(qđ|quyết định)[^\n]{0,60}thành lập hội đồng',
      r'có hội đồng', r'tổ giúp việc[^\n]{0,40}qđ']),
    (7, 'Tiêu chí chấm điểm (QĐ của Chủ tịch Hội đồng)',
     [r'qđ-hđ', r'tiêu chí (đánh giá|chấm điểm)', r'bộ tiêu chí']),
    (8, 'Họp Hội đồng chấm điểm, báo cáo kết quả',
     [r'gm-hđ', r'họp (hội đồng|chấm điểm)', r'phiên chấm điểm', r'kết quả chấm điểm']),
    (9, 'Sở thẩm định, trình UBND tỉnh thành lập cụm',
     [r'trình (ubnd tỉnh )?thành lập(?! hội đồng)', r'bc-sct[^\n]{0,40}thành lập']),
    (10, 'ĐÃ CÓ Quyết định thành lập CCN',
     [r'quyết định thành lập (ccn|cụm)', r'qđ thành lập (ccn|cụm)', r'đã thành lập cụm']),
    (11, 'Sau thành lập: quy hoạch 1/500, đất đai, môi trường, khởi công',
     [r'1/500', r'khởi công', r'gpmt', r'giao đất', r'cho thuê đất']),
]

MAU_SO_VB = re.compile(
    r'\b\d{1,5}\s*/\s*(?:[A-ZĐ]{2,10}-)?(?:QĐ|TTr|BC|CV|TB|GM|SCT|UBND|HĐ|BQL)[A-ZĐ\-]*',
    re.IGNORECASE)
MAU_NGAY = re.compile(r'\b\d{1,2}/\d{1,2}/20\d{2}\b')
MAU_GIAI_THE = re.compile(r'giải thể', re.IGNORECASE)
MAU_TEN_CUM = re.compile(r'\b(?:CCN|KCN)\s+([A-ZĐÂÊÔƯÁÀÃ][^\s,;|)(]*(?:\s+[A-ZĐÂÊÔƯÁÀÃ0-9][^\s,;|)(]*){0,2})')
MAU_LAM_LAI = re.compile(r'thay thế|điều chỉnh vị trí|chuyển vị trí|làm lại hồ sơ', re.IGNORECASE)
CUA_SO = 90  # so ky tu lay hai ben ten cum khi doan qua dai


def bo_dau(s):
    s = unicodedata.normalize('NFD', s)
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return s.replace('đ', 'd').replace('Đ', 'D').lower()


def goc_plugin():
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(here)


def quet(ten_cum, in_het=False):
    goc = goc_plugin()
    khoa = bo_dau(ten_cum)
    ket_qua = []
    for thu_muc in THU_MUC_QUET:
        duong_dan = os.path.join(goc, thu_muc)
        if not os.path.isdir(duong_dan):
            continue
        for root, _, files in os.walk(duong_dan):
            for ten_file in sorted(files):
                if not ten_file.endswith(('.md', '.txt')):
                    continue
                full = os.path.join(root, ten_file)
                try:
                    with open(full, encoding='utf-8') as f:
                        dong_list = f.readlines()
                except (OSError, UnicodeDecodeError):
                    continue
                for i, dong in enumerate(dong_list, 1):
                    if khoa not in bo_dau(dong):
                        continue
                    co_so_vb = bool(MAU_SO_VB.search(dong))
                    if not co_so_vb and not in_het:
                        continue
                    cua_so = doan_chua_ten(dong, khoa)
                    ten_khac = {t.strip() for t in MAU_TEN_CUM.findall(cua_so)
                                if bo_dau(t).strip() != khoa}
                    ket_qua.append({
                        'file': os.path.relpath(full, goc),
                        'dong': i,
                        'text': dong.strip(),
                        'bac': doan_bac(cua_so),
                        'ngay': MAU_NGAY.findall(dong),
                        'nhieu_cum': len(ten_khac) > 0,
                        'lam_lai': bool(MAU_LAM_LAI.search(cua_so)),
                    })
    return ket_qua


def doan_chua_ten(dong, khoa):
    """Lấy đoạn hẹp nhất còn chứa tên cụm. Dòng liệt kê nhiều cụm thường ngăn bằng dấu ';';
    dòng bảng giữ nguyên cả hàng vì tên cụm nằm ở ô đầu, nội dung ở ô sau."""
    manh = re.split(r';', dong)
    ung_vien = [m for m in manh if khoa in bo_dau(m)]
    doan = min(ung_vien, key=len) if ung_vien else dong
    if len(doan) > 320:
        vitri = bo_dau(doan).find(khoa)
        doan = doan[max(0, vitri - CUA_SO): vitri + len(khoa) + CUA_SO]
    return doan


def doan_bac(dong):
    d = bo_dau(dong)
    bac_tim = []
    for so, _, mau_list in BAC:
        for mau in mau_list:
            if re.search(bo_dau(mau), d):
                bac_tim.append(so)
                break
    return max(bac_tim) if bac_tim else None


def ngay_moi_nhat(ket_qua):
    ngay_list = []
    for k in ket_qua:
        for n in k['ngay']:
            try:
                d, m, y = [int(x) for x in n.split('/')]
                ngay_list.append(datetime.date(y, m, d))
            except ValueError:
                continue
    return max(ngay_list) if ngay_list else None


def ten_bac(so):
    for b, ten, _ in BAC:
        if b == so:
            return ten
    return '?'


def main():
    ap = argparse.ArgumentParser(description='Tra bậc thủ tục hiện tại của một CCN/KCN')
    ap.add_argument('ten_cum', help='Tên cụm hoặc khu, vd "Châu Quế"')
    ap.add_argument('--all', action='store_true', dest='in_het',
                    help='In mọi dòng nhắc tên cụm, kể cả dòng không có số văn bản')
    args = ap.parse_args()

    ket_qua = quet(args.ten_cum, args.in_het)

    print('=' * 72)
    print('GATE TRẠNG THÁI HỒ SƠ — {}'.format(args.ten_cum))
    print('=' * 72)

    if not ket_qua:
        print('KHÔNG tìm thấy dòng nào về cụm này trong plugin.')
        print('→ DỪNG soạn thảo. Hỏi người dùng cụm đang ở bước nào '
              '(mẫu câu: references/39-gate-trang-thai-ho-so-cum.md mục E).')
        return 2

    rieng = [k for k in ket_qua if not k['nhieu_cum']]
    liet_ke = [k for k in ket_qua if k['nhieu_cum']]
    cao_nhat = max([k['bac'] for k in rieng if k['bac']], default=None)

    def in_dong(k):
        nhan = 'bậc {}'.format(k['bac']) if k['bac'] else 'chưa xếp bậc'
        print('[{}] {}:{}'.format(nhan, k['file'], k['dong']))
        text = k['text']
        print('    ' + (text[:300] + '…' if len(text) > 300 else text))
        if MAU_GIAI_THE.search(text):
            print('    ⚠ dòng nhắc GIẢI THỂ — kiểm tra Hội đồng còn hoạt động không')
        if k['lam_lai']:
            print('    ⚠ dòng nhắc THAY THẾ / ĐỔI VỊ TRÍ — hồ sơ có thể đang làm lại, '
                  'bậc cũ và bậc mới chạy song song, bắt buộc hỏi người dùng')

    print('--- Dòng nói riêng về cụm này (dùng để xếp bậc) ---')
    if rieng:
        for k in sorted(rieng, key=lambda x: (x['bac'] or 0, x['file'], x['dong'])):
            in_dong(k)
    else:
        print('(không có)')

    if liet_ke:
        print('--- Dòng liệt kê nhiều cụm (tham khảo, KHÔNG dùng xếp bậc) ---')
        for k in sorted(liet_ke, key=lambda x: (x['file'], x['dong'])):
            in_dong(k)

    print('-' * 72)
    if cao_nhat:
        print('BẬC CAO NHẤT ghi nhận trong plugin: {} — {}'.format(cao_nhat, ten_bac(cao_nhat)))
        print('Chỉ được soạn văn bản của bậc {} hoặc bậc {}.'.format(cao_nhat, cao_nhat + 1))
        if cao_nhat == 5:
            print('⚠ Đã có Tờ trình trình UBND tỉnh thành lập Hội đồng. TRƯỚC KHI soạn lại công văn '
                  'cử cán bộ, phải xác nhận UBND tỉnh đã ban hành Quyết định thành lập Hội đồng chưa '
                  '(đúng vụ Châu Quế 17/9/2026, ref 39 mục A).')
        if cao_nhat >= 6:
            print('⚠ Cụm đã có Hội đồng: CẤM công văn đề nghị cử cán bộ "để có cơ sở tham mưu '
                  'UBND tỉnh thành lập Hội đồng" (bảng cấm ngược, ref 39 mục D).')
        if cao_nhat >= 10:
            print('⚠ Cụm đã có Quyết định thành lập: CẤM tờ trình đề nghị thành lập cụm.')
    else:
        print('Có dòng nhắc tên cụm nhưng chưa xếp được bậc riêng cho cụm này.')
        print('→ DỪNG soạn thảo, hỏi người dùng (ref 39 mục E).')
    moi_nhat = ngay_moi_nhat(ket_qua)
    if moi_nhat:
        cach = (datetime.date.today() - moi_nhat).days
        print('Dòng có ngày mới nhất: {} (cách hôm nay {} ngày).'.format(
            moi_nhat.strftime('%d/%m/%Y'), cach))
        if cach > 7:
            print('⚠ Quá 07 ngày — bậc kế tiếp có thể đã xong mà plugin chưa ghi. HỎI người dùng '
                  'trước khi soạn (ref 39 mục E).')
    print('LƯU Ý: plugin chỉ ghi đến kỳ cập nhật gần nhất (ref 32). Trước khi trình ký, '
          'xác nhận lại với người dùng nếu dòng mới nhất đã cũ hoặc bậc kế tiếp có thể đã xong.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
