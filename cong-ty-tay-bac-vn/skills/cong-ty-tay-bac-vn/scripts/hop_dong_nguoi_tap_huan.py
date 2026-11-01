"""Hợp đồng nguyên tắc thuê người tập huấn 05 năm: Công ty Tây Bắc - người tập huấn (điền thông tin người tập huấn)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vb import *

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
ND161 = ('Nghị định số 161/2024/NĐ-CP ngày 18 tháng 12 năm 2024 của Chính phủ quy định Danh mục hàng hóa nguy hiểm, '
         'vận chuyển hàng hóa nguy hiểm và trình tự, thủ tục cấp giấy phép, cấp giấy chứng nhận hoàn thành chương trình '
         'tập huấn cho người lái xe hoặc người áp tải vận chuyển hàng hóa nguy hiểm trên đường bộ')

d = new_doc()
quoc_hieu_center(d)
P(d, 'HỢP ĐỒNG THUÊ NGƯỜI TẬP HUẤN', bold=True, align='center', before=12)
P(d, 'An toàn hàng hóa nguy hiểm', bold=True, align='center', before=0)
P(d, 'Số: 16.10/2026/HĐGV', align='center', before=0, after=6)
for t in ['«Căn cứ Bộ luật Dân sự số 91/2015/QH13 ngày 24 tháng 11 năm 2015;»', '«Căn cứ %s,»' % ND161]:
    P(d, t)
P(d, 'Hôm nay, ngày 16 tháng 10 năm 2026, tại trụ sở Công ty TNHH Năng lượng và Điện lực Tây Bắc, chúng tôi gồm:')
P(d, '⟪BÊN THUÊ (Bên A): CÔNG TY TNHH NĂNG LƯỢNG VÀ ĐIỆN LỰC TÂY BẮC⟫')
for t in ['- Đại diện: Ông Trần Trọng Đài; Chức vụ: Giám đốc',
          '- Địa chỉ: Số nhà 16, ngõ 119 đường Nguyễn Phúc, phường Yên Bái, tỉnh Lào Cai; Mã số doanh nghiệp: 5200966576; Điện thoại: ⟦…⟧',
          '- Số tài khoản: ⟦…⟧ tại Ngân hàng TMCP Đầu tư và Phát triển Việt Nam (BIDV) - Chi nhánh Yên Bái.']:
    P(d, t, before=3)
P(d, '⟪BÊN ĐƯỢC THUÊ (Bên B): ⟦HỌ VÀ TÊN NGƯỜI TẬP HUẤN⟧⟫')
for t in ['- Ngày sinh: ⟦…⟧; Số định danh cá nhân: ⟦…⟧; Địa chỉ: ⟦…⟧; Điện thoại: ⟦…⟧; Số tài khoản: ⟦…⟧ tại ⟦…⟧',
          '- Trình độ: ⟦Trình độ, văn bằng (số hiệu, ngày, trường); kinh nghiệm quản lý hóa chất tối thiểu 05 năm⟧',
          ]:
    P(d, t, before=3)
P(d, 'Hai bên thống nhất ký kết Hợp đồng với các điều khoản sau:')
P(d, '⟪Điều 1. Nội dung công việc⟫', keep=True)
P(d, 'Bên B làm người tập huấn các lớp tập huấn an toàn hàng hóa nguy hiểm cho người lái xe, người áp tải do Bên A tổ chức '
     'hoặc phối hợp tổ chức với người thuê vận tải, người vận tải. Loại, nhóm hàng, thời gian, địa điểm, danh sách học viên của '
     'từng lớp do Bên A thông báo cho Bên B bằng văn bản hoặc tin nhắn trước ngày khai giảng ít nhất 05 ngày.')
P(d, '⟪Điều 2. Thù lao và thanh toán⟫', keep=True)
P(d, '1. Thù lao: 150.000 đồng/lớp tập huấn (Bằng chữ: Một trăm năm mươi nghìn đồng một lớp tập huấn), đã bao gồm chi phí đi lại, '
     'ăn ở và thuế thu nhập cá nhân (nếu có). Mỗi lớp tập huấn tính theo một đợt tập huấn Bên A thông báo cho Bên B, '
     'không phụ thuộc số loại, nhóm hàng và số học viên.')
P(d, '2. Bên A thanh toán bằng tiền mặt hoặc chuyển khoản trong 05 ngày làm việc kể từ ngày Bên B ký Biên bản bàn giao hồ sơ '
     'tập huấn của lớp đó.')
P(d, '⟪Điều 3. Trách nhiệm của Bên A⟫', keep=True)
P(d, 'Thông báo lịch tập huấn theo Điều 1; cung cấp tài liệu tập huấn, danh sách học viên; bố trí địa điểm, '
     'trang thiết bị thực hành; thanh toán đúng hạn.')
P(d, '⟪Điều 4. Trách nhiệm của Bên B⟫', keep=True)
for t in ['1. Bảo đảm điều kiện của người tập huấn theo khoản 4 Điều 8 Nghị định số 161/2024/NĐ-CP trong suốt thời hạn hợp đồng; '
          'cung cấp bản sao văn bằng, tài liệu chứng minh kinh nghiệm công tác và chịu trách nhiệm về tính trung thực của các tài liệu này; báo ngay cho Bên A khi không thể nhận lớp hoặc không còn đủ điều kiện.',
          '2. Chịu trách nhiệm toàn bộ về chuyên môn của từng lớp tập huấn trước Bên A và trước đơn vị có người lao động tham gia '
          'tập huấn: giảng dạy đúng chương trình, đủ thời lượng; theo dõi, xác nhận việc tham gia của học viên; ra đề, coi, chấm '
          'kiểm tra khách quan, giữ bí mật đề kiểm tra và đáp án; tính chính xác, trung thực của kết quả kiểm tra do Bên B đề nghị công nhận.',
          '3. Lập, ký hồ sơ lớp tập huấn; ký Biên bản bàn giao hồ sơ tập huấn với đơn vị có người lao động tham gia tập huấn.',
          '4. Trường hợp Bên A hoặc đơn vị có người lao động tham gia tập huấn bị cơ quan có thẩm quyền xử lý vi phạm, phải tổ chức '
          'tập huấn lại hoặc phải bồi thường cho bên thứ ba do Bên B không bảo đảm điều kiện người tập huấn, không giảng dạy đủ '
          'chương trình, thời lượng hoặc kết quả kiểm tra không trung thực thì Bên B hoàn trả thù lao của lớp đó và bồi thường '
          'toàn bộ thiệt hại.']:
    P(d, t)
P(d, '⟪Điều 5. Chấm dứt hợp đồng⟫', keep=True)
P(d, 'Hợp đồng chấm dứt khi hết thời hạn hoặc hai bên thỏa thuận chấm dứt; mỗi bên được đơn phương chấm dứt hợp đồng nhưng '
     'phải báo cho bên kia trước 30 ngày. Bên A được chấm dứt hợp đồng ngay khi Bên B không còn đủ điều kiện người tập huấn '
     'hoặc vi phạm khoản 2 Điều 4.')
P(d, '⟪Điều 6. Thời hạn và điều khoản chung⟫', keep=True)
P(d, 'Hợp đồng có thời hạn 05 năm kể từ ngày ký. Tranh chấp được giải quyết bằng thương lượng, không thương lượng được thì đưa ra '
     'Tòa án có thẩm quyền. Hợp đồng lập thành 02 bản, mỗi bên giữ 01 bản./.')
two_sign(d, ['ĐẠI DIỆN BÊN A', 'GIÁM ĐỐC'], ['BÊN B', ''], blank=3, names=('Trần Trọng Đài', '⟦Họ và tên⟧'))
path = os.path.join(OUT, '2026.11.01. Hợp đồng thuê người tập huấn an toàn hàng hóa nguy hiểm - người tập huấn (05 năm).docx')
d.save(path)
print('saved', path)
