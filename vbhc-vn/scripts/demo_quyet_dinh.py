#!/usr/bin/env python3
"""
demo_quyet_dinh.py — Tạo Quyết định cá biệt mới từ mẫu thật.

Đây là loại văn bản KHÓ nhất vì có:
  - Phần "GIÁM ĐỐC SỞ CÔNG THƯƠNG" (P5)
  - Nhiều "Căn cứ..." (P7-P16) - italic
  - "Theo đề nghị của..." (P17) - italic
  - "QUYẾT ĐỊNH:" (P18)
  - Điều 1, 2, 3 (P19, P23, P25) - "Điều X" BOLD + nội dung không bold

Ví dụ: thành lập Đoàn thẩm định ATTP cho công ty mới.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fill_template import TemplateDoc

def main():
    doc = TemplateDoc('templates/05-quyet-dinh.docx')

    # ==========================================================
    # Header (Table 0)
    # ==========================================================
    doc.replace_in_cell(0, 0, 0, 'Số:          /QĐ - SCT', 'Số:    127/QĐ-SCT')
    doc.replace_in_cell(0, 0, 1, 'ngày        tháng  3  năm 2026',
                        'ngày 20 tháng 5 năm 2026')

    # ==========================================================
    # Tiêu đề "Về việc..." (P2, P3)
    # ==========================================================
    doc.set_paragraph_text(2, 'Về việc thành lập Đoàn thẩm định cấp Giấy chứng nhận cơ sở')
    doc.set_paragraph_text(3, 'đủ điều kiện an toàn thực phẩm')

    # ==========================================================
    # Căn cứ — giữ nguyên các căn cứ pháp luật (P7-P15)
    # CHỈ thay căn cứ về hồ sơ cụ thể (P16)
    # ==========================================================
    doc.set_paragraph_text(16,
        'Căn cứ hồ sơ đơn đề nghị cấp Giấy chứng nhận đủ điều kiện an toàn thực phẩm '
        'của Công ty TNHH Sản xuất - Thương mại Hùng Sơn nộp trực tuyến qua Cổng dịch '
        'vụ công Quốc gia, ngày 18 tháng 5 năm 2026, mã hồ sơ H38.2-260518-0200015;'
    )

    # P17 "Theo đề nghị của Trưởng phòng Quản lý công nghiệp," — giữ nguyên

    # P18 "QUYẾT ĐỊNH:" — giữ nguyên

    # ==========================================================
    # ĐIỀU 1 (P19) — "Điều 1:" BOLD + nội dung
    # Dùng replace_keeping_first_run để giữ "Điều 1:" bold
    # ==========================================================
    doc.replace_keeping_first_run(19,
        'Thành lập Đoàn thẩm định điều kiện an toàn thực phẩm để cấp Giấy chứng nhận '
        'cơ sở đủ điều kiện an toàn thực phẩm đối với Công ty TNHH Sản xuất - Thương mại '
        'Hùng Sơn tại địa điểm sản xuất, kinh doanh: Lô A12, Cụm công nghiệp Đông Phố Mới, '
        'phường Lào Cai, tỉnh Lào Cai, gồm các ông, bà có tên sau:'
    )

    # Danh sách thành viên đoàn (P20, P21, P22)
    doc.set_paragraph_text(20,
        '1. Ông: Trần Trọng Trang - Phó Trưởng phòng Quản lý công nghiệp, Sở Công Thương - Trưởng đoàn;')
    doc.set_paragraph_text(21,
        '2. Ông: Nguyễn Văn B - Chuyên viên phòng Quản lý công nghiệp, Sở Công Thương - Thành viên;')
    doc.set_paragraph_text(22,
        '3. Bà: Trần Thị C - Chuyên viên phòng Quản lý công nghiệp, Sở Công Thương - Thành viên; thư ký.')

    # ==========================================================
    # ĐIỀU 2 (P23) — giữ nguyên (nội dung chuẩn về trách nhiệm đoàn)
    # P24 "Đoàn thẩm định tự giải thể..." — giữ nguyên
    # ==========================================================

    # ==========================================================
    # ĐIỀU 3 (P25) — "Điều 3:" BOLD
    # P26: danh sách người chịu trách nhiệm thi hành — sửa cho phù hợp
    # ==========================================================
    # P25 "Điều 3:  Quyết định này có hiệu lực từ ngày ký." — giữ nguyên

    doc.set_paragraph_text(26,
        'Chánh văn phòng Sở, Trưởng phòng Quản lý công nghiệp, Giám đốc Công ty TNHH '
        'Sản xuất - Thương mại Hùng Sơn; các tổ chức, cá nhân liên quan và các ông, bà có '
        'tên tại Điều 1 chịu trách nhiệm thi hành Quyết định này./.'
    )

    # ==========================================================
    # Lưu VT — đổi tên người soạn (mẫu là Trang - T.Dương, đổi thành Trung)
    # ==========================================================
    doc.replace_in_cell(1, 0, 0, '- Lưu VT, CN(Trang - T.Dương).',
                        '- Lưu: VT, CN(Trung).')

    # Người ký giữ nguyên (KT. GĐ - PGĐ Nguyễn Đình Chiến)

    doc.save('output/quyet-dinh-hung-son.docx')

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    main()
