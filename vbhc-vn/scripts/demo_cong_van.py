#!/usr/bin/env python3
"""
demo_cong_van.py — Demo: Sửa Công văn từ mẫu thật.

Mẫu gốc: templates/01-cong-van.docx (do Bạn cung cấp)
Đầu ra:  output/cong-van-moi.docx
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fill_template import TemplateDoc


def main():
    # Mở file mẫu
    doc = TemplateDoc('templates/01-cong-van.docx')

    # ==========================================================
    # 1. SỬA HEADER (Table 0): Số ký hiệu, V/v, Ngày tháng năm
    # ==========================================================
    # Cell trái có 4 paragraph: "UBND TỈNH LÀO CAI" / "SỞ CÔNG THƯƠNG" / "Số:..." / "V/v ..."
    # Cell phải có 3 paragraph: "CỘNG HÒA..." / "Độc lập..." / "Lào Cai, ngày..."

    # Số ký hiệu
    doc.replace_in_cell(0, 0, 0, 'Số:       /SCT-CN', 'Số:    458/SCT-CN')

    # V/v ...
    doc.replace_in_cell(0, 0, 0, 'V/v ……………….',
                        'V/v báo cáo tiến độ thẩm định CCN An Thịnh')

    # Ngày tháng năm (bên cell phải)
    doc.replace_in_cell(0, 0, 1, 'ngày      tháng      năm 2026',
                        'ngày 15 tháng 5 năm 2026')

    # ==========================================================
    # 2. SỬA "Kính gửi:" (Paragraph 2)
    # ==========================================================
    doc.replace_in_paragraph(2, '…………..', 'Ủy ban nhân dân tỉnh Lào Cai')

    # ==========================================================
    # 3. THAY NỘI DUNG CHÍNH (Paragraph 4 đến 15)
    # ==========================================================
    # Thay toàn bộ nội dung body bằng nội dung mới
    new_body = [
        {'text': 'Thực hiện Văn bản số 1234/UBND-KT ngày 10/5/2026 của Ủy ban nhân dân tỉnh Lào Cai về việc đẩy nhanh tiến độ thẩm định hồ sơ thành lập Cụm công nghiệp An Thịnh, Sở Công Thương báo cáo Ủy ban nhân dân tỉnh tiến độ thực hiện như sau:'},
        {'text': '1. Tình hình triển khai', 'bold': True},
        {'text': '- Đã tiếp nhận đầy đủ hồ sơ đề nghị thành lập CCN An Thịnh từ Công ty TNHH Đằng Phong - Kiến Phát ngày 02/5/2026.'},
        {'text': '- Đã tổ chức 02 cuộc họp Hội đồng thẩm định vào ngày 08/5/2026 và 12/5/2026 để xem xét hồ sơ.'},
        {'text': '- Đã lấy ý kiến tham gia của các sở, ngành liên quan, dự kiến nhận đầy đủ ý kiến trước ngày 20/5/2026.'},
        {'text': '2. Khó khăn, vướng mắc', 'bold': True},
        {'text': '- Chủ đầu tư cần cập nhật phương án giải phóng mặt bằng theo địa giới hành chính mới sau hợp nhất tỉnh.'},
        {'text': '3. Kế hoạch tiếp theo', 'bold': True},
        {'text': '- Hoàn thiện báo cáo thẩm định, trình Ủy ban nhân dân tỉnh xem xét, quyết định thành lập CCN trước ngày 15/6/2026.'},
        {'text': 'Trên đây là báo cáo của Sở Công Thương về tiến độ thẩm định CCN An Thịnh, kính trình Ủy ban nhân dân tỉnh xem xét./.'},
    ]
    doc.replace_body_paragraphs(start_idx=4, end_idx=16, new_paragraphs=new_body)

    # ==========================================================
    # 4. SỬA NƠI NHẬN (Table cuối, cell trái)
    # ==========================================================
    # Thay "Lưu: VT, CN." → "Lưu: VT, CN(Trung)."
    doc.replace_in_cell(1, 0, 0, 'Lưu: VT, CN.', 'Lưu: VT, CN(Trung).')

    # Người ký: giữ nguyên (Nguyễn Đình Chiến) trong mẫu

    # ==========================================================
    # 5. LƯU
    # ==========================================================
    doc.save('output/cong-van-an-thinh.docx')


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    main()
