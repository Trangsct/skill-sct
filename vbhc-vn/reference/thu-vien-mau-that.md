# Thư viện mẫu thật đã ban hành (`examples/`) — Chế độ B

Bên cạnh `templates/` (mẫu TRẮNG để điền bằng `TemplateDoc` - Chế độ A), skill có thư mục `examples/` chứa **văn bản thật đã ban hành**, giữ nguyên 100% định dạng, dùng làm mẫu cho **Chế độ B**: mở file mẫu phù hợp trong `examples/`, **copy sang chỗ làm việc** rồi thay nội dung (unpack → sửa `word/document.xml` → pack), giữ nguyên layout.

Quy tắc bắt buộc với `examples/`:
- **KHÔNG dùng `TemplateDoc`** cho file trong `examples/` (đã điền sẵn, không phải mẫu trắng theo chỉ số paragraph).
- **KHÔNG bê nguyên nội dung vụ việc cũ** (tên cụm công nghiệp/doanh nghiệp/cán bộ, số liệu, vụ việc) sang văn bản mới — chỉ kế thừa khung, thể thức và văn phong.
- Vẫn áp dụng mục "Phòng tránh 7 nhóm sai lầm tham mưu" (cuối skill): không bịa số/ngày văn bản; không suy diễn nhiệm vụ ngoài chỉ đạo; không dùng từ suy đoán trong bản trình ký.

`examples/` chia 02 nhóm: `examples/sct/` (văn bản do Sở Công Thương ban hành) và `examples/ubnd/` (văn bản cấp UBND tỉnh/Văn phòng UBND tỉnh mà Sở dự thảo).

### A. examples/sct/ - văn bản do Sở Công Thương ban hành (mẫu thật)

Các loại này đều đã có **mẫu trắng** tương ứng trong `templates/`. **Ưu tiên dùng `examples/sct/`** (mẫu thật đã ban hành — đúng văn phong, bố cục bảng, thể thức người ký theo lĩnh vực) theo Quy tắc ưu tiên ở mục "Hai chế độ làm việc"; chỉ dùng `templates/` (dựng mới bằng `TemplateDoc`) khi không có mẫu thật phù hợp.

| Loại văn bản | File mẫu | Ký hiệu | Người ký (mẫu) | Ghi chú |
|---|---|---|---|---|
| Công văn đề nghị DN bổ sung hồ sơ | `examples/sct/cong-van-de-nghi-bo-sung-ho-so.docx` | `/SCT-CN` | KT. GĐ - PGĐ Hoàng Văn Thuân | CV nghiệp vụ; lĩnh vực VLNCN/dịch vụ nổ mìn do PGĐ Thuân ký; Lưu VT, CN(Linh) |
| Công văn mời dự họp (cấp Sở) | `examples/sct/cong-van-moi-hop-sct.docx` | `/SCT-CN`, V/v mời dự họp | KT. GĐ - PGĐ | Giấy mời cấp Sở; khối Kính gửi dạng bảng. Theo memory: SCT-GM là văn bản độc lập, không tham chiếu cuộc họp trước, thành phần bình đẳng |
| Tờ trình ban hành VBQPPL | `examples/sct/to-trinh-vbqppl-tien-chat-thuoc-no.docx` | `/TTr-SCT` | GIÁM ĐỐC Hoàng Chí Hiền | Trình UBND tỉnh ban hành Quyết định QPPL (tiền chất thuốc nổ); kèm hồ sơ dự thảo; Lưu VT, CN(TĐKhôi). VBQPPL theo NĐ 78/2025 + NĐ 187/2025 |
| Kế hoạch thực hiện đề án/chỉ đạo | `examples/sct/ke-hoach-thuc-hien-de-an-08.docx` | `/KH-SCT` | Lãnh đạo Sở | KH thực hiện Đề án 08; cấu trúc I. Mục đích, yêu cầu → II. Nội dung, nhiệm vụ → III. Tổ chức thực hiện; thường kèm phụ lục bảng phân công |
| Báo cáo chuyên đề | `examples/sct/bao-cao-ket-qua-thang-atvsld.docx` | `/BC-SCT` | KT. GĐ - PGĐ Hoàng Văn Thuân | Báo cáo kết quả Tháng hành động ATVSLĐ; Lưu VT, CN(Khôi) |
| Báo cáo tổng hợp khổ dài (có bảng) | `examples/sct/bao-cao-tinh-hinh-trien-khai-ccn.docx` | `/BC-SCT` | GIÁM ĐỐC Hoàng Chí Hiền | Báo cáo hiện trạng CCN toàn tỉnh phục vụ hội nghị; Lưu VT, CN(Trung); đối chiếu số liệu với `kcn-ccn-vn` ref 15 |
| Giấy phép vận chuyển HHNH | `examples/sct/giay-phep-van-chuyen-hhnh.docx` | `/GP-SCT` | KT. GĐ - PGĐ | GP vận chuyển hàng hóa nguy hiểm (xăng, dầu Diesel); có bảng HHNH (số UN, loại/nhóm, số hiệu nguy hiểm, phương tiện). Dùng kèm skill `hnh-sct-vn` |
| Giấy chứng nhận ATTP | `examples/sct/giay-chung-nhan-attp-winmart.docx` | `.../GCNATTP-SCTLC` | KT. GĐ - PGĐ | GCN cơ sở đủ điều kiện ATTP (chuỗi WinMart+); KHÔNG có bảng header, Quốc hiệu căn giữa trực tiếp; kèm phụ lục danh mục sản phẩm |
| Công văn nội bộ Phòng (tham gia ý kiến hồ sơ) | `examples/sct/cong-van-noi-bo-phong-tham-gia-y-kien-kcn.docx` | (nội bộ, KHÔNG cấp số) | Trưởng phòng QLCN | **Mẫu thật cho Chế độ B của loại "công văn nội bộ phòng" (template 08)**. Phòng QLCN gửi Phòng KH-TH tham gia ý kiến hồ sơ đề xuất đầu tư hạ tầng KCN (Phú Xuân); Kính gửi 1 phòng; mở đầu "Phòng QLCN nhận được Văn bản số .../BQL-QHXD..."; thân 1. Sự phù hợp quy hoạch, 2. Nội dung đề nghị làm rõ/bổ sung, 3. Kết luận; kết "đề nghị Phòng KH-TH nghiên cứu, tổng hợp"; Lưu: CN. Đối chiếu nội dung KCN với `kcn-ccn-vn` |
| Biên bản làm việc (liên ngành) | `examples/sct/bien-ban-lam-viec-lien-nganh-ccn.docx` | (KHÔNG cấp số) | các bên cùng ký | **Mẫu biên bản làm việc nhiều cơ quan** (về CCN Đầm Hồng/kiến nghị UBND phường). Mở đầu Quốc hiệu căn giữa (KHÔNG có bảng header cơ quan), "Căn cứ Văn bản số .../UBND-KT ngày .../ Hôm nay, ngày ... tại Sở Công Thương..."; I. Thành phần (liệt kê từng cơ quan + họ tên, chức vụ), II. Nội dung làm việc, III. Kết luận/Thống nhất; khối ký nhiều bên (đại diện các sở, UBND phường) |
| Biên bản kiểm tra thực tế (HHNH) | `examples/sct/bien-ban-kiem-tra-thuc-te-hhnh.docx` | (KHÔNG cấp số) | Đoàn kiểm tra + đơn vị được kiểm tra | **Mẫu biên bản kiểm tra thực tế phục vụ cấp GP vận chuyển HHNH** (loại 3, xăng dầu - Cty An Khang). Căn cứ NĐ 161/2024, Điều 44 NĐ 105/2025, khoản 2 Điều 8 TT 38/2025 (sửa đổi bởi TT 26/2026), QĐ ủy quyền của UBND tỉnh; "Hôm nay vào hồi ... giờ, ngày ..., Đoàn kiểm tra của Sở Công Thương tiến hành kiểm tra thực tế..."; I. Thành phần, II. Nội dung và kết quả kiểm tra (nhiều bảng: phương tiện, người điều khiển, người áp tải, biểu trưng/bao bì); III. Kết luận, kiến nghị. Dùng kèm `hnh-sct-vn` |

### B. examples/ubnd/ - văn bản cấp UBND tỉnh / Văn phòng UBND tỉnh (mẫu thật)

Nhóm này có header, ký hiệu, thể thức người ký KHÁC HẲN văn bản Sở. Sở chỉ **dự thảo**; người ký do UBND/VP quyết định.

| Loại văn bản | Cơ quan ban hành | Ký hiệu | File mẫu | Người ký (mẫu) |
|---|---|---|---|---|
| Giấy mời họp | UBND tỉnh | `/GM-UBND` (VP: `/GM-VPUBND`) | `examples/ubnd/giay-moi-hop-ubnd.docx` | TL. CHỦ TỊCH - KT. CHÁNH VĂN PHÒNG - PHÓ CHÁNH VĂN PHÒNG |
| Công văn chỉ đạo của UBND tỉnh | UBND tỉnh | `/UBND-KT` | `examples/ubnd/cong-van-ubnd-tinh-chi-dao.docx` | KT. CHỦ TỊCH - PHÓ CHỦ TỊCH (Ngô Hạnh Phúc) |
| Công văn VP UBND truyền đạt/đề nghị | VP UBND tỉnh (TL. Chủ tịch) | `/UBND-KT` | `examples/ubnd/cong-van-vp-ubnd-truyen-dat.docx` | TL. CHỦ TỊCH - KT. CHÁNH VĂN PHÒNG - PHÓ CHÁNH VĂN PHÒNG (Hoàng Ngọc Bích) |
| Thông báo Kết luận của Chủ tịch UBND tỉnh | VP UBND tỉnh | `/TB-VP` | `examples/ubnd/thong-bao-ket-luan-ubnd.docx` | CHÁNH VĂN PHÒNG (Lê Trí Hà) |
| Phiếu trình giải quyết công việc | VP UBND tỉnh (nội bộ) | (không cấp số) | `examples/ubnd/phieu-trinh-giai-quyet-cong-viec.docx` | Chuyên viên/Lãnh đạo VP trình |
| Báo cáo của VP UBND tỉnh | VP UBND tỉnh | `/BC-VP` | `examples/ubnd/bao-cao-vp-ubnd.docx` | CHÁNH VĂN PHÒNG |

#### Quy ước header (cơ quan ban hành)
- **UBND tỉnh trực tiếp ban hành** (công văn chỉ đạo, giấy mời, quyết định): dòng cơ quan là **`ỦY BAN NHÂN DÂN TỈNH LÀO CAI`** (đậm), KHÔNG có dòng cấp trên (khác văn bản Sở: Sở có 2 dòng `UBND TỈNH LÀO CAI` + `SỞ CÔNG THƯƠNG`).
- **Văn phòng UBND tỉnh ban hành** (thông báo, báo cáo, phiếu trình, một số công văn truyền đạt): 2 dòng `UBND TỈNH LÀO CAI` (thường) + **`VĂN PHÒNG`** (đậm).
- Quốc hiệu bên phải; bắt buộc gạch chân dưới tên cơ quan và dưới "Độc lập - Tự do - Hạnh phúc".

#### Quy ước ký hiệu (hậu tố theo khối/lĩnh vực của VP UBND)
- Công văn UBND tỉnh: `Số: .../UBND-<Khối>`. Khối Kinh tế = `KT` (CCN/KCN, công nghiệp, xây dựng, tài chính); khối khác đã gặp: `NLN` (nông lâm nghiệp - môi trường), `NC` (nội chính). Nội dung CCN/KCN dùng `UBND-KT`.
- Thông báo: `/TB-VP`; Báo cáo VP: `/BC-VP`; Giấy mời: `/GM-UBND` hoặc `/GM-VPUBND` (đã gặp cả hai - đối chiếu mẫu/đầu mối phát hành).
- Phiếu trình giải quyết công việc: văn bản nội bộ VP, KHÔNG cấp số.
- KHÔNG bịa số; để trống chờ Văn thư UBND/VP cấp số.

#### Quy ước người ký
- **PCT UBND tỉnh ký thay Chủ tịch** (công văn chỉ đạo, quyết định cá biệt): `KT. CHỦ TỊCH` / `PHÓ CHỦ TỊCH` / họ tên (vd Ngô Hạnh Phúc - PCT Thường trực).
- **VP ký thừa lệnh Chủ tịch** (giấy mời, công văn truyền đạt, đôn đốc): `TL. CHỦ TỊCH` / `KT. CHÁNH VĂN PHÒNG` / `PHÓ CHÁNH VĂN PHÒNG` / họ tên (vd Hoàng Ngọc Bích).
- **Thông báo Kết luận**: `CHÁNH VĂN PHÒNG` / họ tên (vd Lê Trí Hà); một số trường hợp `TL. CHỦ TỊCH` + Chánh VP.
- **Văn bản UBND tỉnh do Chủ tịch ký trực tiếp**: `TM. ỦY BAN NHÂN DÂN TỈNH` / `CHỦ TỊCH` / họ tên.

#### Quy ước "Nơi nhận" thường gặp
- Công văn chỉ đạo UBND tỉnh: `- Như trên;` / `- Chủ tịch UBND tỉnh (b/c);` / `- Chánh VP, Phó CVP (tên);` / `- Lưu: VT, KT(tên).`
- Thông báo Kết luận: `- Thường trực Tỉnh ủy (b/c);` / `- Thường trực HĐND tỉnh (b/c);` / `- Chủ tịch, các Phó Chủ tịch UBND tỉnh;` / `- Các Sở liên quan;` / ... / `- Lưu: VT, TH.`
- Giấy mời: `- Như kính gửi;` / `- Chủ tịch UBND tỉnh (b/c);` / `- Lưu: VT, KT(tên), HCQT(tên).`

#### Cấu trúc từng mẫu UBND/VP
- **giay-moi-hop-ubnd (GM-UBND)**: tiêu đề `GIẤY MỜI HỌP` + dòng "Về ..."; khối `Kính gửi:` dạng bảng liệt kê đại biểu; thân: `1. Thời gian, hình thức họp`, `2. Địa điểm, thành phần` (2.1, 2.2...; "Chủ trì cuộc họp", "Thành phần"), phần giao chuẩn bị; kết "Ủy ban nhân dân tỉnh kính mời ... nêu trên./.".
- **cong-van-ubnd-tinh-chi-dao (UBND-KT)**: mở đầu "Xét đề nghị của ... tại [văn bản số.../ngày...], Chủ tịch Ủy ban nhân dân tỉnh có ý kiến chỉ đạo như sau:"; thân đánh số `1, 2, 3...` mỗi mục "Giao [cơ quan] ..."; kết "Ủy ban nhân dân tỉnh yêu cầu ... khẩn trương triển khai thực hiện./."; ký KT. CHỦ TỊCH - PHÓ CHỦ TỊCH.
- **cong-van-vp-ubnd-truyen-dat (UBND-KT)**: mở đầu "Thực hiện ý kiến chỉ đạo của Lãnh đạo Ủy ban nhân dân tỉnh ..., Văn phòng Ủy ban nhân dân tỉnh đề nghị ...:"; thân đánh số theo từng cơ quan; nêu mốc thời gian gửi báo cáo; ký TL. CHỦ TỊCH - KT. CHÁNH VĂN PHÒNG - PHÓ CHÁNH VĂN PHÒNG.
- **thong-bao-ket-luan-ubnd (TB-VP)**: tiêu đề `THÔNG BÁO` + "Kết luận của đồng chí [Chủ tịch] ... tại cuộc họp ..."; mở đầu nêu bối cảnh, thành phần dự họp; `I. ĐÁNH GIÁ CHUNG`; `II. NHIỆM VỤ, GIẢI PHÁP TRỌNG TÂM VÀ PHÂN CÔNG TỔ CHỨC THỰC HIỆN` chia theo từng cơ quan (1. Sở Công Thương, 2. Sở Tài chính, ... 9. Văn phòng UBND tỉnh); kết "Trên đây là kết luận của đồng chí ...; Văn phòng Ủy ban nhân dân tỉnh thông báo ... thực hiện./."; ký CHÁNH VĂN PHÒNG.
- **phieu-trinh-giai-quyet-cong-viec (VP, nội bộ)**: tiêu đề `PHIẾU TRÌNH GIẢI QUYẾT CÔNG VIỆC`; "Kính gửi: Đồng chí [Phó] Chủ tịch Ủy ban nhân dân tỉnh."; `I. VỀ NỘI DUNG TRÌNH DUYỆT CỦA ĐƠN VỊ` (1. Cơ quan trình duyệt; 2. Vấn đề trình; 3. Hồ sơ, văn bản liên quan; 4. Nội dung trình); `II. TÓM TẮT QUÁ TRÌNH THẨM ĐỊNH VÀ Ý KIẾN THAM GIA CỦA CÁC NGÀNH`; tiếp theo là ý kiến, đề xuất của Văn phòng. Header có dòng `VĂN PHÒNG`, không cấp số.
- **bao-cao-vp-ubnd (BC-VP)**: cấu trúc như Báo cáo (template 03) nhưng header VP UBND, ký hiệu `/BC-VP` (`I. HIỆN TRẠNG CHUNG` → bảng chi tiết từng cụm). Mẫu báo cáo tổng hợp khổ dài kèm bảng nhiều dòng.

#### Lưu ý số liệu (đối chiếu trước khi dùng)
- Báo cáo VP UBND (`bao-cao-vp-ubnd`) nêu tổng 970,46 ha, lấp đầy trên 30%; trong khi Thông báo Kết luận, Báo cáo CCN của Sở (`examples/sct/bao-cao-tinh-hinh-trien-khai-ccn`) nêu 903,78 ha, lấp đầy 29,0% - số liệu giữa các bản CHƯA THỐNG NHẤT. Phải chốt số đúng theo nguồn mới nhất của Phòng QLCN trước khi trích (xem `kcn-ccn-vn` ref 15).
