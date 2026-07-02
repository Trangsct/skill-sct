#!/usr/bin/env python3
"""demo_to_trinh.py — Tạo Tờ trình mới từ mẫu thật."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fill_template import TemplateDoc

def main():
    doc = TemplateDoc('templates/02-to-trinh.docx')

    # Header (Table 0)
    doc.replace_in_cell(0, 0, 0, 'Số:            /TTr-SCT', 'Số:    65/TTr-SCT')
    doc.replace_in_cell(0, 0, 1, 'ngày       tháng       năm 2026', 'ngày 18 tháng 5 năm 2026')

    # Tiêu đề "Về việc..." (P4-P5)
    doc.set_paragraph_text(4, 'Về việc phê duyệt nhiệm vụ Quy hoạch chi tiết')
    doc.set_paragraph_text(5, 'Cụm công nghiệp Y Can, tỉnh Lào Cai tỉ lệ 1/500')

    # Kính gửi (P7) - giữ nguyên "Ủy ban nhân dân tỉnh Lào Cai"

    # Phần đầu: căn cứ + thực hiện (P9, P10, P11, P12)
    doc.set_paragraph_text(9, 'Căn cứ Luật Quy hoạch đô thị ngày 17/6/2009; Nghị định số 32/2024/NĐ-CP ngày 15/3/2024 của Chính phủ về quản lý, phát triển cụm công nghiệp.')
    doc.set_paragraph_text(10, 'Thực hiện Quyết định số 949/QĐ-UBND ngày 06/5/2025 của UBND tỉnh Yên Bái (cũ) về việc thành lập Cụm công nghiệp Y Can; Tờ trình số 30/TTr-UBND ngày 02/02/2026 của UBND xã Quy Mông, tỉnh Lào Cai.')
    doc.set_paragraph_text(11, 'Trên cơ sở hồ sơ đề xuất của Chủ đầu tư và ý kiến tham gia của các sở, ngành liên quan, Sở Công Thương đã hoàn thiện hồ sơ trình UBND tỉnh xem xét, phê duyệt.')
    doc.set_paragraph_text(12, 'Sở Công Thương kính trình Ủy ban nhân dân tỉnh Lào Cai phê duyệt nhiệm vụ Quy hoạch chi tiết Cụm công nghiệp Y Can với các nội dung như sau:')

    # Các đề mục I, II, III, IV, V (P13, P16, P19, P20, P28) — giữ nguyên cấu trúc

    # Sửa nội dung mục con (1, 2, 3) - đôi khi cần điều chỉnh tên cho phù hợp
    # Ở demo này giữ nguyên các đề mục, chỉ thay câu kết
    doc.set_paragraph_text(31, 'Trên đây là Tờ trình về phê duyệt nhiệm vụ Quy hoạch chi tiết Cụm công nghiệp Y Can, Sở Công Thương kính trình Uỷ ban nhân dân tỉnh xem xét, phê duyệt./.')

    # Lưu VT - đổi tên người soạn nếu cần (giữ nguyên Trung)
    # Người ký: GIÁM ĐỐC Hoàng Chí Hiền (giữ nguyên)

    doc.save('output/to-trinh-y-can.docx')

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    main()
