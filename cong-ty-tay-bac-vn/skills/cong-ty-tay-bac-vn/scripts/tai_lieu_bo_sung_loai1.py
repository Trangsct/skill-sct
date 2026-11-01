"""Tài liệu tập huấn bổ sung: loại 1 - tín hiệu báo nguy tàu biển (pháo hiệu hàng hải)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vb import *
from docx.shared import Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'
IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'mau', 'bieu-trung') + os.sep
DATE = '2026.11.01'

# Ngân hàng câu hỏi bộ C12 (dùng chung với kiemtra.py)
C12 = [
    ('Tín hiệu báo nguy tàu biển (pháo hiệu hàng hải) thuộc loại hàng hóa nguy hiểm nào?',
     ['Loại 1: Chất nổ và vật phẩm dễ nổ', 'Nhóm 4.1: Chất rắn dễ cháy', 'Loại 9: Chất và vật phẩm nguy hiểm khác', 'Nhóm 2.1: Khí dễ cháy'], 'A'),
    ('Biểu trưng nguy hiểm của loại 1 có màu nền:',
     ['Đỏ', 'Vàng', 'Xanh lá cây', 'Da cam'], 'D'),
    ('Pháo hiệu hàng hải và amoni nitrat cùng giao cho một chuyến hàng, người lái xe, người áp tải phải:',
     ['Xếp chung, chằng buộc chắc chắn', 'Không xếp chung trên cùng một phương tiện', 'Xếp chung nếu đi ban ngày', 'Xếp amoni nitrat lên trên pháo hiệu'], 'B'),
    ('Lửa từ lốp xe đã bén vào thùng hàng chở pháo hiệu, người lái xe, người áp tải phải:',
     ['Leo lên thùng xe dỡ hàng ra', 'Dùng bình chữa cháy dập lửa trong thùng hàng', 'Không chữa cháy hàng hóa, rời xa xe, cách ly khu vực, báo 114', 'Lái xe tiếp đến cửa hàng xăng dầu gần nhất'], 'C'),
    ('Xe chở pháo hiệu nhóm 1.4 bị cháy, phạm vi cách ly theo Sổ tay ERG 2024 là:',
     ['500 m mọi hướng', '50 m', '10 m', 'Không cần cách ly'], 'A'),
    ('Xe chở tín hiệu báo nguy tàu biển không được đi qua công trình hầm có chiều dài:',
     ['Từ 500 m trở lên', 'Từ 100 m trở lên', 'Từ 1.000 m trở lên', 'Bất kỳ, nếu đi ban đêm'], 'B'),
    ('Kiện pháo hiệu bị vỡ, sản phẩm rơi ra mặt đường, việc làm đúng là:',
     ['Để người dân tự nhặt', 'Đốt bỏ tại chỗ', 'Kích hoạt thử để kiểm tra', 'Thu gom sản phẩm còn nguyên vào thùng riêng, không để người khác nhặt, báo người thuê vận tải'], 'D'),
    ('Khi xếp, dỡ kiện pháo hiệu, yêu cầu đúng là:',
     ['Thao tác nhẹ nhàng, không quăng ném, không mở kiện, không hút thuốc', 'Dùng móc sắt kéo kiện cho nhanh', 'Mở kiện để kiểm đếm từng quả', 'Quăng ném kiện từ trên xe xuống'], 'A'),
]

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    d = new_doc()
    p = P(d, 'CÔNG TY TNHH NĂNG LƯỢNG VÀ ĐIỆN LỰC TÂY BẮC', size=13, bold=True, align='center', before=0)
    add_line(p, 80, (9072 / 20 - 80) / 2, 19)
    P(d, '', size=10, before=0)
    P(d, 'TÀI LIỆU TẬP HUẤN BỔ SUNG', bold=True, align='center', before=12)
    P(d, 'AN TOÀN HÀNG HÓA NGUY HIỂM LOẠI 1', bold=True, align='center', before=0)
    p = P(d, 'Tín hiệu báo nguy tàu biển (pháo hiệu hàng hải)', bold=True, align='center', before=0)
    add_line(p, 110, (9072 / 20 - 110) / 2, 22)
    P(d, '', before=0)
    P(d, '«Tài liệu này bổ sung nội dung riêng của loại 1 vào Chuyên đề 5 của Tài liệu tập huấn an toàn hàng hóa nguy hiểm '
         'dùng chung cho người lái xe, người áp tải. Chuyên đề 1, 2, 3, 4 học theo tài liệu dùng chung; câu hỏi kiểm tra '
         'tại mục 20 của tài liệu này.»', before=6)

    def H(t):
        return P(d, t, bold=True, before=10, keep=True)

    def B(t, **k):
        return P(d, t, before=3, **k)

    H('XII. LOẠI 1: CHẤT NỔ VÀ VẬT PHẨM DỄ NỔ')
    H('1. Định nghĩa loại hàng, phạm vi áp dụng')
    B('Loại 1 gồm chất nổ và vật phẩm dễ nổ (điểm a khoản 1 Điều 4 Nghị định số 161/2024/NĐ-CP). Vật phẩm dễ nổ là sản phẩm có chứa '
      'chất nổ hoặc hỗn hợp pháo hoa, khi bị kích thích (va đập, ma sát, nhiệt, lửa, tia lửa điện) có thể cháy mạnh, phát sáng, '
      'phát khói, phóng đi hoặc nổ.')
    B('Tài liệu này áp dụng cho các vật phẩm tín hiệu cấp cứu dùng trên tàu biển, thường gọi là pháo hiệu hàng hải, có tên trong '
      'Danh mục hàng hóa nguy hiểm tại Phụ lục I Nghị định số 161/2024/NĐ-CP. Việc vận chuyển vật liệu nổ công nghiệp, tiền chất '
      'thuốc nổ, pháo thực hiện theo pháp luật về vũ khí, vật liệu nổ, công cụ hỗ trợ, tiền chất thuốc nổ và pháo (khoản 3 Điều 1 '
      'Nghị định số 161/2024/NĐ-CP), không thuộc phạm vi tài liệu này.')
    B('Theo hệ thống phân loại của Liên hợp quốc, loại 1 chia thành 06 nhóm theo mức độ nguy hiểm: nhóm 1.1 có nguy cơ nổ khối; '
      'nhóm 1.2 có nguy cơ văng bắn; nhóm 1.3 có nguy cơ cháy kèm nổ nhỏ hoặc văng bắn nhỏ; nhóm 1.4 không có nguy cơ đáng kể, '
      'hậu quả chủ yếu giới hạn trong kiện hàng; nhóm 1.5, 1.6 là chất, vật phẩm rất kém nhạy. Chữ cái đi kèm (nhóm tương thích) '
      'cho biết loại vật phẩm, ví dụ chữ G là vật phẩm chứa hỗn hợp pháo hoa, chữ S là vật phẩm có tác động giới hạn trong kiện hàng.')

    H('2. Các mặt hàng thường gặp')
    TABLE(d, [1100, 3200, 900, 1300, 1300, 1272], [
        ['TT trong Danh mục', 'Tên gọi và mô tả', 'Số UN', 'Loại, nhóm hàng', 'Biểu trưng', 'Hướng dẫn ERG'],
        ['109', 'Tín hiệu, báo nguy, tàu biển', '0195', '1', '1', '112'],
        ['375', 'Tín hiệu, báo nguy, tàu biển', '0505', '1', '1.4', '114'],
        ['376', 'Tín hiệu, báo nguy, tàu biển', '0506', '1', '1.4', '114'],
        ['377', 'Tín hiệu, khói', '0507', '1', '1.4', '114'],
        ['105', 'Thiết bị tín hiệu, cầm tay', '0191', '1', '1.4', '114'],
    ], ['center', 'left', 'center', 'center', 'center', 'center'], size=12)
    B('Trên thực tế, một bộ pháo hiệu hàng hải thường gồm: pháo hiệu dù (phóng lên cao, thả dù treo ngọn sáng đỏ), đuốc cầm tay '
      '(cháy sáng đỏ), tín hiệu khói nổi (tạo khói màu da cam trên mặt nước). Số UN, nhóm hàng của từng sản phẩm ghi trên kiện hàng '
      'và trong hồ sơ vận chuyển do người thuê vận tải cung cấp.')

    H('3. Số hiệu nguy hiểm')
    B('Danh mục hàng hóa nguy hiểm không quy định số hiệu nguy hiểm đối với các mặt hàng nêu trên (cột số hiệu nguy hiểm để trống). '
      'Báo hiệu nguy hiểm trên phương tiện thực hiện theo Phụ lục II Nghị định số 161/2024/NĐ-CP và chỉ dẫn trong Giấy phép vận '
      'chuyển hàng hóa nguy hiểm.')

    H('4. Biểu trưng, báo hiệu nguy hiểm')
    B('Biểu trưng loại 1 (mô tả theo Phụ lục III): nhóm 1.1, 1.2, 1.3 có biểu tượng quả bom nổ màu đen, nền màu da cam, số "1" ở '
      'góc đáy; nhóm 1.4, 1.5, 1.6 có chữ số "1.4", "1.5", "1.6" màu đen, nền màu da cam, số "1" ở góc đáy; dưới chữ số ghi chữ cái '
      'nhóm tương thích. Biểu trưng dán ở hai bên, phía trước và phía sau phương tiện; sau khi dỡ hết hàng và không tiếp tục chở loại '
      'hàng đó thì làm sạch và bóc hoặc xóa biểu trưng.')
    p = P(d, '', align='center', indent=False, before=6, keep=True)
    r = p.add_run(); r.add_picture(IMG + 'bt-1.png', width=Cm(4.2))
    r = p.add_run('          ')
    r = p.add_run(); r.add_picture(IMG + 'bt-14.png', width=Cm(4.2))
    P(d, 'Hình 1. Biểu trưng loại 1, nhóm 1.1, 1.2, 1.3 (trái) và nhóm 1.4, nhóm tương thích G (phải)', size=13, italic=True,
      align='center', before=3)

    H('5. Tính chất lý, hóa')
    for t in ['- Pháo hiệu chứa hỗn hợp pháo hoa gồm chất ôxi hóa (như kali perclorat, stronti nitrat), nhiên liệu kim loại (như magie) '
              'và chất kết dính; pháo hiệu dù có thêm liều phóng bằng thuốc đen.',
              '- Hỗn hợp pháo hoa tự chứa chất ôxi hóa nên cháy được cả khi không có không khí, kể cả dưới nước; ngọn lửa có nhiệt độ rất '
              'cao, khó dập tắt.',
              '- Sản phẩm có hạn sử dụng ghi trên vỏ; sản phẩm quá hạn, bị ẩm, bị móp méo, nứt vỏ dễ mất ổn định, dễ tự kích hoạt.']:
        B(t)

    H('6. Nguy cơ cháy, nổ')
    for t in ['- Va đập mạnh, rơi kiện, ma sát, nhiệt độ cao, ngọn lửa, tia lửa điện có thể kích hoạt sản phẩm.',
              '- Pháo hiệu dù bị kích hoạt có thể phóng đi như tên lửa theo hướng bất kỳ; đuốc cháy làm bén lửa sang kiện hàng bên cạnh.',
              '- Khi cả xe hàng bị cháy, sản phẩm lần lượt bị kích hoạt, gây cháy lan, văng bắn; hàng nhóm 1.1, 1.2, 1.3 có thể nổ.']:
        B(t)

    H('7. Nguy cơ đối với sức khỏe con người')
    for t in ['- Bỏng nặng do ngọn lửa, xỉ kim loại nóng chảy; chấn thương do sản phẩm văng bắn.',
              '- Ánh sáng cường độ cao gây tổn thương mắt khi nhìn trực tiếp ở cự ly gần.',
              '- Khói gây kích ứng mắt, đường hô hấp.']:
        B(t)

    H('8. Nguy cơ đối với môi trường')
    B('- Tro, xỉ, sản phẩm cháy dở chứa perclorat, nitrat, hợp chất kim loại gây ô nhiễm đất, nguồn nước nếu không được thu gom.')

    H('9. Dạng bao bì, thùng chứa, phương tiện thường dùng')
    B('Sản phẩm đóng trong hộp, thùng các-tông hoặc hòm gỗ đạt yêu cầu, có nhãn loại 1, ghi số UN và tên hàng; vận chuyển bằng xe '
      'tải thùng kín hoặc thùng có mui bạt che kín, khóa được.')

    H('10. Các nguy cơ gây mất an toàn trong bảo quản, xếp dỡ, vận chuyển')
    TABLE(d, [2200, 6872], [
        ['Công đoạn', 'Nguy cơ, nguyên nhân thường gặp'],
        ['Chuẩn bị xe', 'Sàn thùng xe có đinh, vật sắc nhọn, dầu mỡ; hệ thống điện chập chờn; thiếu bình chữa cháy'],
        ['Xếp dỡ', 'Quăng ném, kéo lê, làm rơi kiện; dùng móc sắt; hút thuốc, dùng lửa gần nơi xếp dỡ; nhận kiện đã rách, ướt'],
        ['Vận chuyển', 'Xếp chung với chất ôxi hóa, chất dễ cháy; chằng buộc lỏng, phanh gấp làm xô kiện; đỗ lâu dưới nắng nóng'],
        ['Sự cố', 'Cháy lốp, cháy cabin lan vào thùng hàng; tai nạn làm vỡ kiện, sản phẩm rơi ra đường, người dân nhặt'],
    ], ['center', 'left'], size=12)

    H('11. Nguyên tắc xếp chung hàng hóa')
    for t in ['- Không xếp chung các loại hàng hóa có thể tác động lẫn nhau làm tăng mức độ nguy hiểm trong cùng một phương tiện '
              '(khoản 2 Điều 10 Nghị định số 161/2024/NĐ-CP).',
              '- Không xếp chung pháo hiệu với chất ôxi hóa (nhóm 5.1, như amoni nitrat), perôxít hữu cơ (nhóm 5.2), chất lỏng dễ cháy '
              '(loại 3), khí (loại 2), chất rắn dễ cháy (loại 4), chất ăn mòn (loại 8).',
              '- Người lái xe, người áp tải của đơn vị vừa vận chuyển amoni nitrat vừa vận chuyển pháo hiệu phải bố trí hai loại hàng '
              'trên các phương tiện, chuyến hàng riêng; làm sạch thùng xe trước khi chuyển sang chở loại hàng kia.']:
        B(t)

    H('12. Yêu cầu riêng khi kiểm tra phương tiện, xếp dỡ, vận chuyển, giao hàng')
    B('«(Áp dụng cho người lái xe và người áp tải, bổ sung cho quy trình chung tại Chuyên đề 3)»')
    B('a) Kiểm tra phương tiện, giấy tờ trước khi nhận hàng')
    for t in ['- Giấy phép vận chuyển hàng hóa nguy hiểm còn hiệu lực, đúng tên hàng, số UN, phương tiện, người lái xe, người áp tải; '
              'hồ sơ vận chuyển do người thuê vận tải cung cấp.',
              '- Thùng xe sạch, khô, không có đinh, vật sắc nhọn nhô ra, không dính dầu mỡ; mui bạt, cửa thùng kín, khóa được.',
              '- Hệ thống điện, phanh, lốp hoạt động tốt; bình chữa cháy theo phương án vận chuyển; biểu trưng, báo hiệu nguy hiểm đúng quy định.']:
        B(t)
    B('b) Nhận hàng, xếp hàng lên phương tiện')
    for t in ['- Chỉ nhận kiện nguyên vẹn, khô, có nhãn; không nhận kiện rách, ướt, móp méo, có mùi khét.',
              '- Thao tác nhẹ nhàng, không quăng ném, không kéo lê, không dùng móc sắt; không mở kiện.',
              '- Không hút thuốc, không dùng lửa tại nơi xếp dỡ; tắt máy xe khi xếp dỡ.',
              '- Xếp chặt, chèn kín, chằng buộc chắc chắn, không xếp cao quá thành thùng; xếp xa ống xả, nguồn nhiệt.']:
        B(t)
    B('c) Trong quá trình vận chuyển')
    for t in ['- Không chở người không có nhiệm vụ; không chở hàng khác trái nguyên tắc xếp chung.',
              '- Chạy với tốc độ phù hợp, tránh phanh gấp; kiểm tra chằng buộc sau quãng đường đầu và mỗi lần dừng nghỉ.',
              '- Không dừng, đỗ ở nơi đông người, gần cửa hàng xăng dầu, khu vực hàn cắt, nơi đốt rác; khi dừng, đỗ phải có người trông coi xe.',
              '- Không đi qua công trình hầm có chiều dài từ 100 m trở lên (khoản 1 Điều 11 Nghị định số 161/2024/NĐ-CP); khi đi phà '
              'tuân thủ khoản 2 Điều 11.']:
        B(t)
    B('d) Giao hàng, dỡ hàng và sau khi dỡ hàng')
    for t in ['- Giao đủ số kiện, đối chiếu với hồ sơ vận chuyển; kiện bị hư hỏng trong quá trình vận chuyển lập biên bản, để riêng.',
              '- Kiểm tra thùng xe không còn sót sản phẩm; làm sạch, bóc hoặc xóa biểu trưng khi không tiếp tục chở loại hàng này.']:
        B(t)

    H('13. Trang thiết bị an toàn, phương tiện bảo vệ cá nhân')
    for t in ['- Bình chữa cháy theo phương án vận chuyển để dập cháy lốp, cháy động cơ, cabin khi lửa chưa lan tới hàng.',
              '- Găng tay chịu nhiệt, kính bảo hộ; quần áo bảo hộ bằng vải bông, không dùng vật liệu tổng hợp dễ chảy.',
              '- Biển cảnh báo, cọc tiêu, dây cảnh giới; đèn pin; thùng riêng có nắp để thu gom sản phẩm rơi vãi.']:
        B(t)

    H('14. Xử lý sự cố cháy')
    for t in ['- Lửa ở lốp, động cơ, cabin chưa lan tới hàng: dùng bình chữa cháy, nước dập ngay; đồng thời báo 114.',
              '- Lửa đã bén vào thùng hàng: không chữa cháy hàng hóa; mọi người rời xa xe, cách ly khu vực, ngăn người và phương tiện '
              'đi vào; báo 114, 113, người vận tải, người thuê vận tải, Ủy ban nhân dân cấp xã nơi gần nhất.',
              '- Chỉ lực lượng chữa cháy chuyên nghiệp quyết định việc chữa cháy từ xa.']:
        B(t)

    H('15. Xử lý rơi vãi, vỡ kiện')
    for t in ['- Dừng xe ở nơi an toàn, đặt biển cảnh báo; không để người dân nhặt sản phẩm.',
              '- Không kích hoạt thử, không đốt bỏ, không tháo rời sản phẩm.',
              '- Sản phẩm còn nguyên vẹn: nhặt nhẹ nhàng, cho vào thùng riêng có nắp, đánh dấu; sản phẩm ướt, móp méo, đã cháy dở: để '
              'riêng, khoanh vùng, báo người thuê vận tải và cơ quan chức năng xử lý.']:
        B(t)

    H('16. Khoảng cách cách ly, sơ tán ban đầu')
    B('Khoảng cách tham khảo theo Hướng dẫn số 112 (nhóm 1.1, 1.2, 1.3) và số 114 (nhóm 1.4) của Sổ tay ERG 2024. Lực lượng chức năng '
      'có thẩm quyền quyết định phạm vi cách ly, sơ tán cụ thể.')
    TABLE(d, [3600, 2736, 2736], [
        ['Tình huống', 'Nhóm 1.4 (UN 0191, 0505, 0506, 0507)', 'Nhóm 1.1, 1.2, 1.3 (UN 0195)'],
        ['Vỡ kiện, rơi vãi (biện pháp phòng ngừa ban đầu)', 'Cách ly tối thiểu 100 m mọi hướng', 'Cách ly tối thiểu 500 m mọi hướng'],
        ['Xe hàng bị cháy', 'Cách ly 500 m mọi hướng, xem xét sơ tán 500 m', 'Cách ly 1.600 m mọi hướng, sơ tán 1.600 m'],
    ], ['left', 'center', 'center'], size=12)

    H('17. Sơ cứu đặc thù')
    for t in ['- Bỏng: làm mát vùng bỏng bằng nước sạch ít nhất 20 phút; không bóc phần quần áo dính vào da; che phủ bằng gạc sạch; gọi 115.',
              '- Mắt bị lóa, bị dị vật: không dụi mắt; rửa bằng nước sạch; chuyển cơ sở y tế.',
              '- Hít phải khói: đưa nạn nhân ra nơi thoáng khí; theo dõi hô hấp.',
              '- Chấn thương do văng bắn: cầm máu, cố định, chuyển cấp cứu.']:
        B(t)

    H('18. Ngăn chặn ô nhiễm, thu gom, khắc phục môi trường')
    for t in ['- Không xối nước cuốn tro, xỉ, sản phẩm cháy dở xuống cống, rãnh, khe suối.',
              '- Sau khi lực lượng chức năng xác nhận an toàn, thu gom tro, xỉ, sản phẩm hư hỏng vào thùng có nắp, ghi nhãn; bàn giao cho '
              'người thuê vận tải hoặc đơn vị có chức năng xử lý chất thải nguy hại.']:
        B(t)

    H('19. Tình huống giả định')
    B('Tình huống 1: Xe chở pháo hiệu hàng hải xuống đèo bị bó phanh, cháy lốp sau; khói bốc lên sát thùng hàng.')
    B('Xử lý: dừng xe ở nơi xa khu dân cư nếu còn điều khiển được; tắt máy; dùng bình chữa cháy dập lửa lốp khi lửa chưa lan tới hàng; '
      'khi lửa đã bén vào hàng: rời xe, không chữa cháy hàng hóa; báo ngay 114, 113, người vận tải, người thuê vận tải, Ủy ban nhân dân '
      'cấp xã nơi gần nhất; ngăn người, phương tiện trong phạm vi 500 m.')
    B('Tình huống 2: Tại kho, chủ hàng đề nghị ghép 20 thùng pháo hiệu lên xe đang chở bao amoni nitrat cho kịp chuyến.')
    B('Xử lý: người áp tải, người lái xe từ chối xếp chung vì chất ôxi hóa làm tăng mức độ nguy hiểm của vật phẩm dễ nổ (khoản 2 '
      'Điều 10 Nghị định số 161/2024/NĐ-CP); báo người vận tải bố trí xe, chuyến hàng riêng.')

    H('20. Câu hỏi kiểm tra (dùng cho Phần B bài kiểm tra, câu 13 đến câu 20)')
    for i, (q, opts, a) in enumerate(C12, 13):
        P(d, '⟪Câu %d.⟫ %s' % (i, q), before=4, keep=True)
        for k, (L, o) in enumerate(zip('ABCD', opts)):
            P(d, '%s. %s' % (L, o), before=0, keep=(k < 3))
    P(d, 'Đáp án (dùng cho người chấm): ' + '; '.join('câu %d: %s' % (i, a) for i, (_, _, a) in enumerate(C12, 13)) + '.',
      italic=True, before=8)
    path = os.path.join(OUT, '%s. Tài liệu tập huấn bổ sung an toàn hàng hóa nguy hiểm loại 1 - tín hiệu báo nguy tàu biển.docx' % DATE)
    d.save(path)
    print('saved', path)
