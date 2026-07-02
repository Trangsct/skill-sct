# Cấu trúc cụ thể từng template (01–09)

### 01-cong-van.docx (Công văn)
- **Table 0** (header):
  - Cell trái P0=`UBND TỈNH LÀO CAI`, P1=`SỞ CÔNG THƯƠNG`, P2=`Số: .../SCT-CN`, P3=`V/v ...`
  - Cell phải P0=`CỘNG HÒA...`, P1=`Độc lập...`, P2=`Lào Cai, ngày...`
- **Paragraphs**: P2=`Kính gửi: ...`, P4 đến P15=nội dung body
- **Table 1** (footer):
  - Cell trái: `Nơi nhận:`, `- Như trên;`, `- ...`, `- Lưu: VT, CN.`
  - Cell phải: `KT. GIÁM ĐỐC` / `PHÓ GIÁM ĐỐC` / chữ ký / `Nguyễn Đình Chiến`

### 02-to-trinh.docx (Tờ trình)
- **Table 0** header: tương tự CV nhưng `Số: .../TTr-SCT`, KHÔNG có "V/v..."
- **Paragraphs**: P3=`TỜ TRÌNH`, P4-P5=`Về việc...` (2 dòng), P7=`Kính gửi:...`, P9-P31=nội dung
- **Table 1** footer: `GIÁM ĐỐC` (không có KT.) → `Hoàng Chí Hiền`

### 03-bao-cao.docx (Báo cáo)
- **Table 0** header: `Số: .../BC-SCT`
- **Paragraphs**: P1=`BÁO CÁO`, P2=`Về việc...`, P4=`Kính gửi:...`, P6 trở đi=nội dung
- Cấu trúc đề mục: I, II, III, IV (đậm) → 1, 2, 3 (đậm) → **a), b), c) (in nghiêng)**; mục **1.1, 1.2** (đậm nghiêng)
- **Table 1** footer **3 cột** (cell giữa trống): cell trái=Nơi nhận, cell phải=`KT. GIÁM ĐỐC PHÓ GIÁM ĐỐC` → `Nguyễn Đình Chiến`

### 04-ke-hoach.docx (Kế hoạch)
- **Table 0** header: `Số: .../KH-SCT`
- **Paragraphs**: P2=`KẾ HOẠCH`, P3-P4=tên kế hoạch, P7 trở đi=nội dung
- KHÔNG có "Kính gửi"
- Phần III thường là `TỔ CHỨC THỰC HIỆN` chia theo từng phòng

### 05-quyet-dinh.docx (Quyết định cá biệt)
- **Table 0** header: `Số: .../QĐ-SCT` (lưu ý có khoảng trắng quanh dấu `-`)
- **Paragraphs**:
  - P1=`QUYẾT ĐỊNH`
  - P2-P3=`Về việc...` (2 dòng)
  - P5=`GIÁM ĐỐC SỞ CÔNG THƯƠNG` (BẮT BUỘC, đậm)
  - P7-P16=`Căn cứ...` (italic)
  - P17=`Theo đề nghị của Trưởng phòng Quản lý công nghiệp,` (italic)
  - P18=`QUYẾT ĐỊNH:` (đậm)
  - **P19=`Điều 1:`** (bold) + nội dung — DÙNG `replace_keeping_first_run(19, 'nội dung mới')`
  - P20-P22=danh sách thành viên
  - **P23=`Điều 2:`** + nội dung
  - **P25=`Điều 3:`** + hiệu lực
  - P26=danh sách người chịu trách nhiệm thi hành
- **Table 1** footer: cell trái Nơi nhận, cell phải `KT. GIÁM ĐỐC PHÓ GIÁM ĐỐC` → `Nguyễn Đình Chiến`

### 06-giay-phep.docx (Giấy phép)
- **Table 0** header: `Số: .../GP-SCT`
- **Paragraphs**:
  - P1=`GIẤY PHÉP {LOẠI}` (vd `GIẤY PHÉP SẢN XUẤT RƯỢU CÔNG NGHIỆP`)
  - P2=`---------------` (đường gạch nối, GIỮ NGUYÊN)
  - P4=`GIÁM ĐỐC SỞ CÔNG THƯƠNG`
  - P6-P9=`Căn cứ...` (italic)
  - P10=`Xét đơn đề nghị...` (italic)
  - P11=`Theo đề nghị của...` (italic)
  - P12=`QUYẾT ĐỊNH:`
  - **P13=`Điều 1.`** + tiêu đề điều — `replace_keeping_first_run(13, '...', separator='. ')`
  - P14-P23=thông tin doanh nghiệp + sản phẩm
  - **P24=`Điều 2.`** + trách nhiệm
  - **P26=`Điều 3.`** + thời hạn

### 07-giay-chung-nhan-attp.docx (Giấy chứng nhận ATTP)
- **KHÔNG có Table header** — Quốc hiệu là paragraph trực tiếp căn giữa
- **Paragraphs đầu**: P0=`CỘNG HOÀ...`, P1=`Độc lập...`, P3=`GIẤY CHỨNG NHẬN`, P4=`CƠ SỞ ĐỦ ĐIỀU KIỆN ATTP`, P6=`SỞ CÔNG THƯƠNG TỈNH LÀO CAI`, P7=`CHỨNG NHẬN`
- Tiếp theo: thông tin cơ sở (tên, loại hình, chủ, địa chỉ, điện thoại)
- `ĐỦ ĐIỀU KIỆN AN TOÀN THỰC PHẨM THEO QUY ĐỊNH`
- Bảng chữ ký (cell trái trống, cell phải có `Lào Cai, ngày...` + `KT. GĐ - PGĐ`)
- `Số cấp: .../{năm}/GCNATTP-SCTLC` + `Hiệu lực đến ngày: .../...../{năm+3}`
- Phụ lục: I. DANH MỤC + II. NỘI DUNG (có pageBreak)

### 08-cong-van-noi-bo-phong.docx (Công văn nội bộ Phòng - tham gia ý kiến)
Văn bản **nội bộ giữa các phòng** trong Sở (vd Phòng QLCN gửi Phòng Kế hoạch - Tổng hợp để tham gia ý kiến hồ sơ KCN, dự án đầu tư...). **KHÁC với công văn SCT phát hành ra ngoài** (template 01): đây là văn bản cấp phòng, do Trưởng phòng ký.
- **Đặc trưng nhận diện** (KHÔNG nhầm với template 01):
  - Header **không có dòng `UBND TỈNH LÀO CAI`** và **không có dòng số ký hiệu `Số: .../SCT-CN`** — chỉ gồm `SỞ CÔNG THƯƠNG` (thường) + `PHÒNG QLCN` (đậm, có gạch chân). Đây là văn bản nội bộ nên không cấp số văn thư.
  - **Người ký là TRƯỞNG PHÒNG** (mặc định: Nguyễn Hữu Long - Trưởng phòng QLCN), KHÔNG phải Lãnh đạo Sở. Đây là **ngoại lệ** so với Quy tắc 6.
  - Dòng lưu ghi `- Lưu: CN (<Mã người soạn>).` (vd `Lưu: CN (Trung).`) — chỉ `CN`, không có `VT`.
- **Table 0** (header):
  - Cell trái P0=`SỞ CÔNG THƯƠNG` (thường), P1=`PHÒNG QLCN` (đậm), P2=`V/v ...`
  - Cell phải P0=`CỘNG HÒA...`, P1=`Độc lập...`, P2=`Lào Cai, ngày      tháng      năm 20...`
- **Paragraphs** (body, sau header table):
  - P(Kính gửi)=`Kính gửi: ...` (đậm, căn giữa) → tên phòng nhận
  - P=đoạn mở đầu `Phòng Quản lý công nghiệp nhận được Văn bản số ... về việc ...`
  - P=`Sau khi nghiên cứu hồ sơ, Phòng Quản lý công nghiệp có ý kiến tham gia như sau:`
  - Hệ đề mục: **1, 2, 3 (đậm đứng)** → **a), b), c) (in nghiêng nhãn + tiêu đề; nội dung diễn giải để đứng)** - đúng Quy tắc 9
  - Mục cuối thường là `3. Kết luận` rồi đoạn `Phòng Quản lý công nghiệp ...; đề nghị ... ./.`
- **Table 1** (footer): cell trái=`Nơi nhận:` / `- Như trên;` / `- Ban Giám đốc Sở;` / `- Lưu: CN (...).`; cell phải=`TRƯỞNG PHÒNG` + (để trống ký) + `Nguyễn Hữu Long`
- Body sửa bằng cách **rebuild các paragraph ở cấp XML** (như Chế độ B) để giữ đúng cặp run nghiêng/đứng cho nhãn a), b), c); hoặc dùng `TemplateDoc.replace_in_paragraph` cho từng đoạn.

### 09-bien-ban.docx (Biên bản làm việc/kiểm tra)
Tạo từ mẫu thật `examples/sct/bien-ban-lam-viec-lien-nganh-ccn.docx` (đã genericize). **KHÔNG cấp số.**
- **KHÔNG có Table header** — Quốc hiệu là paragraph căn giữa trực tiếp; **đường gạch chân dưới Tiêu ngữ là ĐỐI TƯỢNG LINE (VML shape)**, không phải border/underscore (giữ nguyên khi sửa, đừng xóa run chứa `<w:pict>`).
- **Paragraphs**: Quốc hiệu + Tiêu ngữ (căn giữa) → `BIÊN BẢN LÀM VIỆC` (đậm, giữa) → `Căn cứ …;` → `Hôm nay, hồi … giờ … ngày …, tại …, … Cụ thể như sau:` → `I. Thành phần tham gia` (đậm) với các cụm `1. <cơ quan>` (đậm) + dòng `Ông/Bà: …\t- …;` (căn trái) → `II. Nội dung làm việc` (đậm): `1. Tóm tắt nội dung chính`, `2. Ý kiến của các cơ quan tham dự` → `III. Các ý kiến thống nhất` (đậm): `Một là,…`, `Hai là,…` → đoạn kết `Biên bản kết thúc vào hồi … giờ … phút …, được lập thành … bản …/.`.
- **Table chữ ký** (cuối): các ô `Đại diện / <cơ quan>` + chừa trống ký + `<họ tên>`. Genericize sẵn bằng dấu `…`.
- Sửa nội dung: vì các đề mục I/II/III và 1./2. ở dạng đậm, dùng `replace_keeping_first_run`/giữ run đầu để không mất đậm; dòng `Ông/Bà:` để **căn trái** (justify làm banh dòng có dấu chấm dẫn). Thêm/bớt thành phần hoặc ý kiến: chèn paragraph mới theo đúng cặp định dạng.
