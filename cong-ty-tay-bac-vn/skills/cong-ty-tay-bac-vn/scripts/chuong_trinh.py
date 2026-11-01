import sys, glob, os
from docx import Document
src, out = sys.argv[1], sys.argv[2]
d = Document(src)
def st(cell_or_p, text):
    ps = cell_or_p.paragraphs if hasattr(cell_or_p, 'paragraphs') else [cell_or_p]
    p = ps[0]; p.runs[0].text = text
    for r in p.runs[1:]: r._r.getparent().remove(r._r)
t = d.tables[1]
for i in (2, 3, 4, 5): st(t.rows[i].cells[2], '3')
st(t.rows[1].cells[0], 'Phần thứ nhất. Nội dung chung (12 giờ, học chung toàn lớp)')
st(t.rows[4].cells[3], 'Lý thuyết 2 giờ, thực hành 1 giờ')
st(t.rows[5].cells[3], 'Lý thuyết 2 giờ, thực hành 1 giờ')
st(t.rows[6].cells[0], 'Phần thứ hai. Nội dung riêng (04 giờ, học theo loại, nhóm hàng)')
st(t.rows[7].cells[2], '3'); st(t.rows[7].cells[3], 'Lý thuyết 2 giờ, thực hành, diễn tập 1 giờ')
st(t.rows[8].cells[1], 'Kiểm tra cuối khóa'); st(t.rows[8].cells[2], '1'); st(t.rows[8].cells[3], 'Kiểm tra trắc nghiệm')
ps = d.paragraphs
for p in ps:
    if p.text.startswith('- Lớp tập huấn tổ chức chung cho người lái xe'):
        st(p, '- Lớp tập huấn tổ chức chung cho người lái xe, người áp tải các loại, nhóm hàng: Phần thứ nhất (12 giờ) học chung toàn lớp, được tính vào thời lượng của từng loại, nhóm hàng; Phần thứ hai (04 giờ, gồm kiểm tra) học riêng theo loại, nhóm hàng ghi trong Giấy phép vận chuyển hàng hóa nguy hiểm của đơn vị.')
    elif p.text.startswith('- Hình thức: lý thuyết kết hợp thực hành'):
        st(p, '- Hình thức: học trực tuyến (online) vào buổi tối, từ 19 giờ 00 đến 23 giờ 00, mỗi buổi 04 giờ; lý thuyết kết hợp thực hành, diễn tập tình huống qua hình ảnh, video và thao tác mẫu; kiểm tra trắc nghiệm cuối mỗi loại, nhóm hàng.')
d.save(os.path.join(out, os.path.basename(src)))
print('ok')
