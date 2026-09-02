# CHANGELOG — qlks-sct-vn

## [1.9.1] - 02/9/2026 — sửa theo scripts/check_facts.py (CI dữ kiện lỗi thời)
- Sửa các vi phạm do scripts/check_facts.py quét: nơi nộp hồ sơ → motcua-tthc.moit.gov.vn; tiêu ngữ en dash trong mẫu; trỏ xp-hc-vlncn-sct-vn → xp-sct-vn; CN(M.Cường) trong mẫu → CN(Khôi), trong ví dụ lịch sử chú thích "lịch sử"; ký hiệu /GP-SCT bỏ chữ "dự kiến". Không đổi nghiệp vụ.

## v1.9.0 — 29/8/2026: nghiệp vụ 12 — xác minh kiến nghị lấn chiếm ranh giới mỏ giáp ranh (mẫu chuẩn vụ Đại Đồng Tiến)

**Nguồn:** Bạn cung cấp trọn bộ 4 văn bản của vụ việc điển hình được đánh giá giải quyết rất tốt: (1) **CV 28/CV-ĐĐT ngày 04/8/2026** của Công ty TNHH Đại Đồng Tiến (GĐ Trần Thành Công ký, scan 61 trang kèm phụ lục chứng cứ) kiến nghị DNTN Thành Hương Nghĩa Lộ lấn chiếm, khai thác trái phép sang ranh giới mỏ đá xã Văn Chấn; (2) **CV 8129/UBND-KT ngày 10/8/2026** (PCT Nguyễn Thành Sinh ký) giao SNNMT chủ trì, phối hợp SXD, SCT, UBND xã Văn Chấn xác minh, báo cáo trước 30/8/2026; (3) **Biên bản kiểm tra thực địa ngày 21/8/2026** ký đủ 6 bên (3 sở + xã + 2 doanh nghiệp); (4) **BC 904/BC-SNNMT ngày 28/8/2026** (PGĐ Phạm Năng Chung ký) — hoàn thành trước hạn 2 ngày. Kết luận: đo GPS hệ VN2000 tại 2 vị trí bên kiến nghị chỉ → cả 2 nằm TRONG ranh giới GP 2596/GP-UBND của bên bị kiến nghị (cách ranh 11m/14m, cao độ +384/+386m > mức sâu cho phép +380m) — **chưa lấn chiếm**; cả hai doanh nghiệp ký thống nhất.

### Nội dung mới

- **`references/22-xac-minh-kien-nghi-lan-chiem-ranh-gioi-mo-giap-ranh.md` (MỚI)**: dòng thời gian 18 ngày từ chỉ đạo đến báo cáo; bảng đối chiếu 2 giấy phép (412/GP-UBND 2012 và 2596/GP-UBND 2014 của UBND tỉnh Yên Bái cũ); **7 kỹ thuật xác minh** làm nên chất lượng vụ này (mời cả hai doanh nghiệp cùng ra thực địa và ký; đo GPS đúng hệ tọa độ giấy phép VN2000 KTT 104°45' múi 3° tại đúng vị trí bên kiến nghị chỉ, đo cả cao độ chân tầng; đối chiếu 3 lớp ranh GP - mức sâu - hồ sơ thuê đất; tách vụ cũ 270m² năm 2022 khỏi kiến nghị mới; kết luận dứt khoát trên số liệu; câu giới hạn phạm vi kiểm tra; ý kiến từng cơ quan thành mục riêng); câu mẫu ý kiến của SCT trong đoàn (mục 4.3 biên bản thật); khuôn cấu trúc báo cáo kết quả 3 phần với **kiến nghị phòng ngừa kể cả khi không có vi phạm** (ranh 2 mỏ cách nhau 01-03m, có nơi <01m + nổ mìn → 6 nhóm kiến nghị với doanh nghiệp + 1 nhóm với cơ quan); quy trình chuẩn B1-B7 tái sử dụng; 7 bài học đối chiếu nhanh.
- **`van-ban-goc/`**: 4 file PDF gốc của vụ việc (CV 28 scan không lớp text; CV 8129 + BC 904 ký số — số/ngày phải render ảnh để đọc; biên bản thực địa scan ký tươi).
- **`references/08`** mục I: con trỏ sang reference 22 cho tình huống kiến nghị lấn chiếm ranh giới mỏ giáp ranh.
- `SKILL.md`: mục V đổi thành **12 nghiệp vụ**, thêm nghiệp vụ 12; bước B4 quy trình thêm nhánh "kiến nghị lấn chiếm ranh giới mỏ giáp ranh"; cây thư mục thêm reference `22` + cập nhật van-ban-goc 26 văn bản; description thêm từ khóa (xác minh kiến nghị lấn chiếm, tranh chấp ranh giới mỏ giáp ranh). `plugin.json` → 1.9.0.

### Bài học nghiệp vụ đáng giá nhất

1. **Thực địa + thiết bị đo thắng mọi tranh luận giấy tờ** — không hòa giải chay: đo tọa độ và cao độ bằng GPS theo đúng hệ quy chiếu của giấy phép, để con số kết luận; bên kiến nghị tự chỉ vị trí đo nên không thể phản bác kết quả.
2. **Kiến nghị của doanh nghiệp không đồng nghĩa có vi phạm** — kết luận "chưa lấn chiếm" dứt khoát, có số liệu, cả bên kiến nghị cũng ký thống nhất; văn bản không quy chụp bên nào.
3. **Không có vi phạm vẫn xử lý gốc rễ rủi ro** — giá trị lớn nhất của BC 904 là phần kiến nghị phòng ngừa từ đặc điểm "2 mỏ giáp ranh quá gần + dùng VLNCN": duy trì mốc giới, khai thác đúng phép - đúng thiết kế, không dùng VLNCN vượt ranh giới bề mặt/độ sâu, chủ động dừng khi có nguy cơ, giám sát thường xuyên.
4. **Câu giới hạn phạm vi** trong cả biên bản lẫn báo cáo ("chỉ kiểm tra xác minh đối với các vị trí do bên kiến nghị đề nghị, không kiểm tra các nội dung khác") — bảo vệ pháp lý đoàn kiểm tra.
5. **Sáp nhập tỉnh không làm đứt hồ sơ**: giấy phép và biên bản thời Yên Bái viện dẫn nguyên trạng, chua "(nay thuộc xã Văn Chấn, tỉnh Lào Cai)".

## v1.8.0 — 25/8/2026: nghiệp vụ 11 — ủy viên Hội đồng thẩm định Đề án thăm dò khoáng sản (QĐ 777/QĐ-UBND)

**Nguồn:** 04 hồ sơ xin ý kiến của Sở Nông nghiệp và Môi trường và 04 Phiếu đánh giá, nhận xét do PGĐ Hoàng Văn Thuân ký: cát sỏi suối Ngòi Thia (xã Xuân Ái, 29/7/2026); cát sỏi sông Chảy khu vực Bản Mủng - Bản Chuân (xã Xuân Hòa, 06/7/2026); cát sỏi suối Nhù thôn Ngầu 3 (xã Võ Lao — CV 7637/SNNMT-KS ngày 10/8/2026, QĐ trúng đấu giá 2084/QĐ-UBND ngày 16/6/2026); đá hoa trắng Làng Lạnh III (xã Lục Yên — QĐ trúng đấu giá 2806/QĐ-UBND ngày 11/8/2026).

### Nội dung mới

- **`references/21-hoi-dong-tham-dinh-de-an-tham-do-777.md` (MỚI)**: vị trí của SCT trong quy trình (ủy viên Hội đồng, trả lời trong 12 ngày làm việc theo điểm b khoản 3 Điều 42 NĐ 193/2025 sửa bởi NĐ 21/2026); bảng phân vai 10 cơ quan/cá nhân trong Hội đồng và ranh giới không lấn sang ủy viên phản biện, Phòng QLXDCT-TL&PCTT; **4 trục nội dung bắt buộc** của Phiếu SCT; **6 lỗi kỹ thuật lặp lại** trong các đề án đã thẩm định; bảng **4 vụ thực tế**; kỹ thuật xử lý hồ sơ đến (giải nén RAR tên tiếng Việt bằng `unar`, OCR tiếng Việt, xác minh bảng tọa độ bằng mắt, tính diện tích bằng shapely, chồng ranh giới với quy hoạch).
- **`mau-van-ban/09-phieu-nhan-xet-uy-vien-hoi-dong-tham-dinh-de-an-tham-do.md` (MỚI)**: khung biểu mẫu; khung nội dung mục I.1 (6 gạch đầu dòng), I.2 (7 nhãn), I.3 (10 kiến nghị chuẩn); 5 đoạn câu chữ mẫu đã dùng thực tế.
- `SKILL.md`: mục V đổi thành **11 nghiệp vụ**, thêm nghiệp vụ 11; bước B4 quy trình thêm nhánh "xin ý kiến đề án thăm dò"; cây thư mục thêm reference `21` và mẫu `09`; description thêm từ khóa kích hoạt (hội đồng thẩm định đề án thăm dò, phiếu đánh giá nhận xét ủy viên hội đồng, QĐ 777/QĐ-UBND, Điều 42 Luật ĐC&KS, Mẫu số 01 Phụ lục VI TT 40/2025, đá hoa trắng, Làng Lạnh, suối Nhù, Ngòi Thia). `plugin.json` → 1.8.0.

### Bài học nghiệp vụ đáng giá nhất

1. **VLNCN trong giai đoạn thăm dò là khoảng trống hầu như không ai kiểm.** Đề án Làng Lạnh III (284,04 ha, dự toán 77,1 tỷ đồng) xác định phải nổ mìn phá đá để mở 3,5 km đường vận chuyển chính (mặt đường 6-7 m), 8 km đường đến nền khoan và 52 nền khoan, nhưng chỉ viết một câu "tuân thủ theo quy định hiện hành về quản lý vật liệu nổ"; dự toán không có một khoản VLNCN nào (chỉ 35 triệu + 40 triệu cho 11,5 km đường); chương bảo vệ môi trường không dự báo chấn động, sóng không khí, đá văng. Đây là phần việc **chỉ SCT phát hiện được** trong Hội đồng.
2. **Phải tự kiểm chứng tọa độ và diện tích, không tin thuyết minh.** Vụ suối Nhù: 10 điểm khép góc trùng khớp tuyệt đối với QĐ 2084/QĐ-UBND nhưng diện tích tính lại là 7,5714 ha trong khi cả Đề án và Quyết định đều ghi 7,5 ha. Vụ Làng Lạnh III: 28 điểm cho 284,037 ha, khớp 284,04 ha.
3. **Lỗi sao chép địa danh giữa các đề án.** Đề án mỏ tại xã Lục Yên viết "khu vực thăm dò nằm gần Sông Lô"; báo cáo khảo sát mỏ suối Nhù viết "mỏ cát sỏi trên suối Ngòi Thia". Đây là căn cứ xác định nguồn nước và công trình cần bảo vệ.
4. **Mâu thuẫn nội tại về hiện trạng lưới điện** giữa mục "vị trí địa lý" ("không có đường truyền dẫn điện") và mục "mạng lưới giao thông" ("mạng lưới điện Quốc gia đã được kéo đến các thôn xóm") — xuất hiện ở cả 2 đề án của cùng một đơn vị tư vấn.
5. **Không khẳng định "không chồng lấn KCN/CCN" khi chưa có tọa độ ranh giới để chồng lớp** — chuyển thành yêu cầu chủ đầu tư bổ sung và tự khẳng định.
6. **Thể thức biểu mẫu của Hội đồng có 02 lỗi sẵn** (`<w:br/>` trong header, khối ký đặt tên trước chức vụ) — giữ nguyên, không tự sửa; `qa_all.py` báo FAIL HDR-BR là lỗi của biểu mẫu.

### Ghi vấn còn mở

- Đề án Làng Lạnh III viết khu mỏ "đã được quy hoạch tại QH số 866 và QH số 1626". Đá hoa trắng thuộc nhóm II, đã được đưa ra khỏi quy hoạch khoáng sản nhóm I — cần đối chiếu bản QĐ 866 điều chỉnh đã ký để khẳng định dứt điểm.
- Chưa có tọa độ ranh giới KCN Võ Lao (QĐ 2463/QĐ-UBND) và KCN Lục Yên, CCN Yên Thế, CCN Tân Lĩnh để chồng lớp trực tiếp — đề nghị Bạn bổ sung phụ lục tọa độ từ BQL Khu kinh tế tỉnh.

## v1.7.0 — 20/8/2026: kinh nghiệm biên bản thanh tra/kiểm tra từ mẫu thật BB 13A/BB-ĐTT72 (Thanh tra tỉnh — vụ Mông Sơn)

**Nguồn:** Bạn cung cấp bản scan **Biên bản làm việc số 13A/BB-ĐTT72 ngày 10/5/2026** của Đoàn thanh tra số 72-2026 (QĐ 72/QĐ-TT ngày 13/3/2026 của Chánh Thanh tra tỉnh Lào Cai) — thống nhất kết quả thanh tra chấp hành pháp luật trong khai thác khoáng sản đối với Công ty CP Mông Sơn, mỏ đá hoa trắng Làng Cạn, xã Mông Sơn (vùng Yên Bái cũ). Bản scan không có lớp text — đã render ảnh từng trang để đọc (11 trang scan = 10 trang biên bản, trang 3 scan trùng).

### Nội dung mới

- **`references/20-bien-ban-thanh-tra-kiem-tra-mau-thuc-te.md` (MỚI)**: bối cảnh tổ chức (thanh tra DN ngành Công Thương nay thuộc Thanh tra tỉnh — Phòng lĩnh vực Công Thương và KHCN; SCT chỉ kiểm tra chuyên ngành); khuôn 5 phần của biên bản làm việc chốt kết quả thanh tra; **10 kinh nghiệm** lập biên bản (bảng số liệu nhiều năm sản lượng + VLNCN đặt cạnh nhau, chuỗi định danh hồ sơ + chú thích chân trang, tồn tại viết kiểu đối chiếu có số liệu — ĐTM/bãi thải 2, khám sức khỏe thiếu đích danh từng năm, bán hàng cho 23 đơn vị ngoài mục tiêu GCN đầu tư; mục lịch sử xử phạt ghi đến đồng; mục "Ý kiến khác nhau của thành viên đoàn"; lập 03 bản + ký nháy từng trang; xử lý chuyển tiếp sáp nhập tỉnh trong viện dẫn; lỗi trình bày cần tránh; biên bản không kèm chế tài); **checklist "đón thanh tra tỉnh"** 6 trục cho doanh nghiệp mỏ.
- **`mau-van-ban/02` mục C (MỚI)**: khung biên bản làm việc chốt kết quả cuối đợt kiểm tra của SCT, chuyển thể từ khuôn BB 13A về đúng phạm vi chức năng SCT.
- **`references/08`**: bổ sung đầu mối Thanh tra tỉnh + bước lập biên bản làm việc chốt kết quả trong quy trình B3.
- **`checklists/checklist-kiem-tra-mo.md` mục A7 (MỚI)**: 5 phép đối chiếu kiểu thanh tra (khám sức khỏe từng năm; mục tiêu GCN đầu tư; hạng mục ĐTM; VLNCN - sản lượng; nộp phạt/khắc phục các QĐ xử phạt cũ).
- `van-ban-goc/BB-13A-BB-DTT72-10-5-2026-thanh-tra-khai-thac-KS-Mong-Son.pdf`: bản gốc scan.
- `SKILL.md`: nghiệp vụ 6 mở rộng + cây thư mục + description thêm từ khóa "biên bản kiểm tra". `plugin.json` → 1.7.0.

### Ghi vấn còn mở

- Biên bản ghi "đăng ký thay đổi lần thứ 9 ngày 07/9/2026" — sau ngày lập biên bản (10/5/2026), nghi là 07/9/2016; khi cần trích dẫn phải kiểm chứng GCN ĐKDN.
- Trang bìa có dấu tiếp nhận iOffice (Số 381, ký số 19/8/2026) — không phải ngày lập biên bản.

## v1.6.0 — 01/8/2026: bổ sung TOÀN VĂN QPPL gốc; đính chính 4 điểm pháp lý quan trọng

**Nguồn:** Bạn cung cấp toàn văn 5 văn bản QPPL ngày 01/8/2026, theo yêu cầu "văn bản QPPL nên đẩy lên GitHub để thường xuyên sử dụng". Nhờ đó đã đối chiếu được nguyên văn thay vì trích gián tiếp qua công văn hướng dẫn của SNNMT — và phát hiện **4 điểm ở v1.5.0 chưa chính xác hoặc đã lạc hậu**.

### File QPPL mới trong `van-ban-goc/`

| File | Nội dung |
|---|---|
| `Luat-54-2024-QH15-Dia-chat-va-khoang-san-TOAN-VAN.docx` | Toàn văn Luật ĐC&KS (trước chỉ có bản tóm tắt điều chỉnh) |
| `Luat-147-2025-QH15-sua-Luat-DCKS-TOAN-VAN.docx` | Toàn văn Luật sửa đổi |
| `TT-36-2025-TT-BNNMT-TOAN-VAN-dieu-khoan.docx` | Toàn văn điều khoản |
| `TT-36-2025-TT-BNNMT-PHU-LUC-I-den-IV.doc` + `.txt` | **Toàn văn Phụ lục I–IV** — bản trước không có phụ lục mẫu |
| `TT-04-2026-TT-BNNMT-sua-cac-TT-dia-chat-khoang-san.docx` | Sửa TT 36/2025 và các TT khác lĩnh vực địa chất - khoáng sản |

### Bốn đính chính

**1. Khoản 5 Điều 75 đã bị Luật 147/2025 sửa — v1.5.0 dùng bản cũ.**
Bản 54/2024: miễn đăng ký cho *"điểm a khoản 1 **và** điểm a khoản 4"*. Bản sửa bởi **khoản 23 Điều 1 Luật 147/2025** (từ 01/01/2026): *"…trừ trường hợp quy định tại **điểm a khoản 4** Điều này."*
→ **Từ 01/01/2026 chỉ còn MỘT trường hợp miễn đăng ký**: khoáng sản dùng cho chính công trình/hạng mục của dự án đó. Trường hợp thu hồi trong dự án đầu tư khai thác khoáng sản (điểm a khoản 1) **không còn được miễn**.

**2. Nhà thầu thi công được cấp giấy xác nhận — CV 2419 đã lạc hậu.**
Khoản 23 Điều 1 Luật 147/2025 bổ sung vào điểm b và điểm c khoản 1 Điều 75: *"Trường hợp chủ đầu tư, nhà đầu tư không có nhu cầu thu hồi khoáng sản thì giấy xác nhận đăng ký thu hồi khoáng sản được cấp cho **nhà thầu thi công** trên cơ sở chấp thuận của chủ đầu tư, nhà đầu tư."*
→ Chủ đập thuỷ điện **không cần tự đứng tên**; đơn vị thi công nạo vét được cấp thẳng. Điều này **thay thế** câu trả lời của Cục ĐCKS tại CV 2419/ĐCKS-PCKS ngày 19/9/2025 ("chỉ cấp cho chủ đầu tư hoặc nhà đầu tư; uỷ quyền theo pháp luật khác"). Điểm b, c cũng được nới: dự án chỉ cần *"được quyết định, phê duyệt hoặc chấp thuận theo quy định của pháp luật"*.

**3. Nghĩa vụ "báo cáo hằng tháng" KHÔNG phải quy định của khoản 2 Điều 76.**
Nguyên văn điểm c khoản 2 Điều 76: *"Báo cáo kết quả hoạt động thu hồi khoáng sản cho cơ quan quản lý nhà nước có thẩm quyền **theo quy định của Bộ trưởng**…"* — tức mẫu 08 Phụ lục IV, nộp trước 15/02. Yêu cầu **hằng tháng** là điều kiện riêng SNNMT Lào Cai đưa vào văn bản hướng dẫn và Giấy xác nhận. Reference 16 nay tách rõ hai tầng, tránh viện dẫn sai căn cứ.

**4. Hồ sơ luồng Điều 97 cần 05 bản vẽ, không phải 1.**
Điều 97 khoản 2 chỉ nêu "bản đồ hiện trạng", nhưng **Phụ lục của mẫu 04** yêu cầu đủ: bản đồ vị trí · bản đồ/sơ đồ địa chất khoáng sản khu mỏ · bản đồ hiện trạng · bản đồ kết thúc thu hồi · bản đồ tổng mặt bằng chung toàn mỏ.

### Bổ sung khác

- **Reference mới `19-phu-luc-III-mau-ho-so-thu-hoi-toan-van.md`** — toàn văn **7 mẫu** Phụ lục III bản đang có hiệu lực (TT 36/2025 sửa bởi khoản 4 Điều 9 TT 04/2026): mẫu 01 · 02 · 03 · **03a (mới)** · 04 · 05 · 06, kèm chú thích 89–93 của mẫu và bảng đối chiếu với văn bản thật.
- **Mẫu 03a mới** (TT 04/2026) — *Văn bản đề nghị được sử dụng khoáng sản* cho khối lượng **đã tập kết tại bãi thải, bãi chứa**, người đề nghị có thể là **nhà đầu tư hoặc nhà thầu thi công**. Đây là mẫu đúng cho kịch bản "đá thải mỏ apatit đã đổ ở bãi, muốn bán ra ngoài".
- **Ba trường hợp miễn tiền cấp quyền** (khoản 3 Điều 98 Luật) nay chép đủ a, b, c — v1.5.0 chỉ nêu điểm a.
- **Nguyên tắc khoản 2 Điều 75**: không áp dụng với nước khoáng, nước nóng thiên nhiên; chỉ được thu hồi khi **bắt buộc** phải san gạt, đào đắp, nạo vét theo đúng thiết kế.
- **Gốc của điểm a khoản 1 Điều 75**: dẫn chiếu **điểm d khoản 1 Điều 59** và **điểm c khoản 1 Điều 70** — nay chép nguyên văn vào reference 18, kèm phân biệt với quyền *sử dụng đất, đá thải mỏ* tại điểm i khoản 1 Điều 59.
- **Giấy xác nhận (mẫu 05)**: thời gian thu hồi ghi bằng **số tháng kể từ ngày có hiệu lực** (không phải khoảng ngày); mục "Mức sâu" chỉ bắt buộc với trường hợp nạo vét lòng sông, lòng hồ; Nơi nhận phải có **Cục ĐCKS VN (bản sao)**.
- `references/01` mục IV-bis bổ sung khoản 23 Điều 1 Luật 147/2025 và TT 04/2026.
- Cập nhật `mau-van-ban/07`, `08`, `checklists/checklist-ho-so-thu-hoi-khoang-san.md`, `SKILL.md`.

### Còn thiếu

Bốn tệp `.rar` (bản vẽ khổ lớn, hồ sơ pháp lý dự án) và số, ngày phát hành chính thức của hai công văn dự thảo hướng dẫn Phúc Long, Tu Trên.

## v1.5.0 — 01/8/2026: nghiệp vụ 10 — THU HỒI KHOÁNG SẢN (nạo vét lòng hồ thuỷ điện + đất đá thải mỏ)

**Nguồn:** 20 tài liệu thật do Bạn cung cấp ngày 01/8/2026 (thư mục `Khoáng sản/Thu hồi tận thu`), gồm 2 văn bản gốc của Bộ và 10 văn bản, hồ sơ thực tế của Lào Cai.

**Mục tiêu Bạn đặt ra:** plugin phải hoàn thiện được trọn bộ hồ sơ cho hai kịch bản — (A) **khai thác cát tại lòng hồ thuỷ điện**, (B) **tận thu đá làm VLXD tại bãi thải mỏ apatit**.

### Hai câu trả lời chốt được rút ra từ tài liệu

1. **Không có thủ tục "cấp phép khai thác cát lòng hồ thuỷ điện".** Con đường hợp pháp duy nhất là *nạo vét bồi lắng lòng hồ kết hợp thu hồi cát, sỏi* — hai giai đoạn tách bạch: (i) dự án/kế hoạch nạo vét do **chủ sở hữu công trình thuỷ điện quyết định chủ trương đầu tư**, **không phải xin giấy phép** trong phạm vi bảo vệ đập (Điều 42 NĐ 62/2025 + QĐ 628/QĐ-BCT bãi bỏ TTHC; Điều 14 NĐ 67/2018 sửa bởi khoản 6 Điều 1 NĐ 40/2023); (ii) đăng ký thu hồi cát sỏi để Chủ tịch UBND tỉnh cấp **Giấy xác nhận đăng ký thu hồi khoáng sản** (điểm c khoản 1 Điều 75 Luật ĐC&KS, Điều 98 NĐ 193/2025, mẫu 02 Phụ lục III TT 36/2025). Pháp luật ĐC&KS **không** quy định việc lập, thẩm định, phê duyệt dự án nạo vét — CV 2419/ĐCKS-PCKS ngày 19/9/2025 mục 11.
2. **Đá thải mỏ, quặng đuôi đi luồng Điều 97 NĐ 193/2025**, không phải Điều 98: hồ sơ 3 tài liệu (VB đề nghị mẫu 01 · Báo cáo vị trí - khối lượng - chủng loại - thời gian mẫu 04 · Bản đồ hiện trạng ghi khối lượng **từng vị trí**). Khối lượng đã trót khai thác đang nằm ở kho, bãi chứa mà chưa được cho phép thu hồi → có lối ra tại **khoản 9 Điều 4 Luật 147/2025/QH15**.

**Gate phân luồng mới, hỏi trước mọi việc:** khoáng sản thu hồi **dùng cho chính dự án** (không phải đăng ký, chỉ cập nhật báo cáo định kỳ và thống kê - kiểm kê trữ lượng — khoản 4 Điều 97) hay **cung cấp cho công trình, dự án khác** (phải đăng ký, phải có Giấy xác nhận)? Trả lời sai câu này thì sai cả bộ hồ sơ.

### File mới

| File | Nội dung |
|---|---|
| `references/16-thu-hoi-khoang-san-tong-quan.md` | Trục chung: phân biệt khai thác / tận thu / thu hồi; 5 trường hợp khoản 1 Điều 75 + thẩm quyền; khi nào phải đăng ký; hai luồng hồ sơ Điều 97 - Điều 98; trình tự và 5 mốc thời hạn; nghĩa vụ khoản 2 Điều 76; bộ 6 mẫu Phụ lục III; 4 đầu việc của SCT; 7 bẫy |
| `references/17-nao-vet-long-ho-thuy-dien-thu-hoi-cat-soi.md` | Gỡ nút thắt "ai phê duyệt dự án nạo vét"; sơ đồ 2 giai đoạn; 7 ràng buộc bắt buộc đưa vào văn bản hướng dẫn DN; phần an toàn đập theo CV 216/ATMT-ATĐ (khoản 1 Điều 49 NĐ 62/2025); checklist 8 câu |
| `references/18-thu-hoi-dat-da-thai-quang-duoi-ks-di-kem-trong-mo.md` | Hai trường hợp Điều 97; khoản 9 Điều 4 Luật 147/2025; hồ sơ 3 tài liệu; khung Báo cáo mẫu 04 và 3 câu "lý do đề xuất thu hồi" mạnh nhất; lấy ý kiến ngành (SCT bị hỏi gì); tiền cấp quyền và trường hợp miễn; nghĩa vụ sau khi có GXN |
| `mau-van-ban/07-bo-ho-so-thu-hoi-cat-soi-long-ho-thuy-dien.md` | CV SCT hướng dẫn chủ đập (3 mục, đủ căn cứ); Bản đăng ký mẫu 02; CV trả hồ sơ - chỉ dẫn đúng cơ quan; QA 6 điểm |
| `mau-van-ban/08-bo-ho-so-thu-hoi-dat-da-thai-mo.md` | VB đề nghị mẫu 01; khung Báo cáo mẫu 04; yêu cầu bản đồ hiện trạng mẫu 35; **VB SCT tham gia ý kiến theo đề nghị SNNMT** (4 mục); CV hướng dẫn DN có đá thải ở bãi; QA 7 điểm |
| `checklists/checklist-ho-so-thu-hoi-khoang-san.md` | 7 khối A–G: phân luồng · dự án gốc · thành phần hồ sơ 2 luồng · 8 điểm soi chéo nội dung · 8 cam kết · 7 việc của SCT · bảng thời hạn |
| `vi-du-thuc-te/` (mới) | 10 văn bản thật + `00-MUC-LUC.md` |
| `van-ban-goc/CV-216-ATMT-ATD-30-01-2026-...pdf` | Cục KTAT&MTCN hướng dẫn SCT Lào Cai (trả lời CV 472/SCT-NL ngày 28/01/2026) |
| `van-ban-goc/CV-2419-DCKS-PCKS-19-9-2025-...pdf` | Cục ĐCKS trả lời 42 kiến nghị của 7 tỉnh |

### File sửa

- `SKILL.md`: description → **10 nghiệp vụ** + bộ từ khoá thu hồi khoáng sản; thêm mục nghiệp vụ **10** ở phần V; GATE B4 thêm bước phân luồng Điều 97/98; cây thư mục mục X cập nhật.
- `references/01-khung-phap-ly-gate-thoi-ky.md`: thêm mục **IV-bis** — 12 văn bản khung riêng cho chế định thu hồi (gồm NĐ 62/2025, QĐ 628/QĐ-BCT, NĐ 67/2018 + NĐ 40/2023, khoản 6 Điều 78 Luật Điện lực, NĐ 67/2019, QĐ 3339/QĐ-BNNMT).

### Ví dụ thật đưa vào

Thuỷ điện **Phúc Long** (xã Phúc Khánh) · thuỷ điện **Tu Trên** — Cty TNHH Xây lắp Cương Lĩnh (xã Nậm Xé) · mỏ cao lanh **Sơn Mãn** — Cty CP Khoáng sản Sông Hồng Lào Cai (bản đăng ký 10/ĐK-PLNC ngày 28/5/2026, 4.062 m², 43.500 tấn/năm) · KCN **Tằng Loỏng** — Cty CP DV xử lý môi trường xanh Việt Sơn (bản đăng ký 72/CV-VS ngày 19/6/2026, 4,43 ha, 334.894 m³, đá ốp lát 21,6%) · mỏ đá hoa **Làng Lạnh II** xã Lục Yên — Cty TNHH SX và TM Chân Thiện Mỹ (CV 1080/SNNMT-KS ngày 11/02/2026 xin ý kiến các ngành) · KĐT **Mường Hoa** Sa Pa (Giấy xác nhận của Chủ tịch UBND tỉnh, 33.642,77 m², 150.000 m³).

### Còn thiếu — cần Bạn bổ sung

1. **Toàn văn Phụ lục III TT 36/2025/TT-BNNMT** (6 mẫu 01–06). Bản TT trong `van-ban-goc/` chỉ có phần điều khoản, chưa có phụ lục mẫu. Hiện các mẫu trong `mau-van-ban/07`, `08` dựng lại từ hồ sơ thật đã được chấp nhận — đủ dùng nhưng nên đối chiếu bản gốc.
2. **Toàn văn Điều 75, Điều 76 Luật ĐC&KS 54/2024** (bản trong `van-ban-goc/` là bản tóm tắt điều chỉnh). Nội dung hiện trích theo nguyên văn các công văn hướng dẫn của SNNMT — chính xác nhưng không phải bản luật.
3. Bốn tệp nén chưa đưa vào repo: `Hồ sơ đăng ký.rar`, `hs đk thu hồi trong dự án cao lanh sơn mãn.rar`, `Pháp lý dự án.rar`, `THU HOI KS SCAN.rar` (chủ yếu bản vẽ khổ lớn và hồ sơ pháp lý dự án).
4. Hai tệp `.doc` (định dạng Word 97) chưa đọc được trong môi trường hiện tại — đề nghị lưu lại dạng `.docx` hoặc PDF: `1. BẢN ĐĂNG KÝ THU HỒI ĐÁ KHỐI LÀM ĐÁ ỐP LÁT.doc`, `GM kiểm tra (Việt Sơn).docx`.
5. **Số và ngày phát hành chính thức** của hai công văn hướng dẫn Phúc Long và Tu Trên (bản trong repo là dự thảo chưa điền số, ngày).

## v1.4.0 — 26/7/2026: reference 15 — nguồn thu đóng góp khai thác khoáng sản trong đầu tư công trung hạn 2026-2030

Bổ sung `references/15-nguon-thu-dong-gop-ks-dtc-2026-2030.md` từ **Quyết định số 2390/QĐ-UBND ngày 09/7/2026** của UBND tỉnh Lào Cai về kế hoạch đầu tư công trung hạn giai đoạn 2026-2030 nguồn vốn ngân sách địa phương (Chủ tịch Nguyễn Tuấn Anh ký; căn cứ NQ 25/NQ-HĐND ngày 29/6/2026; Tờ trình 536/TTr-STC ngày 19/6/2026). **Biểu số 04** của quyết định là biểu riêng cho nguồn thu này.

### Số liệu chốt

| Chỉ tiêu | Triệu đồng |
|---|---|
| Tổng nguồn thu đóng góp khai thác khoáng sản giai đoạn 2026-2030 | **1.594.379** |
| Đã phân bổ chi tiết (03 dự án) | **257.448** |
| Còn lại chưa phân bổ | **1.336.931** |

03 dự án đã bố trí: nâng cấp, mở rộng đường **T2 trong KCN Tằng Loỏng** 20.000; sửa chữa, nâng cấp, mở rộng đường **T12, T19 trong KCN Tằng Loỏng** 50.000 (cả hai theo QĐ 1217/QĐ-UBND 21/4/2025, CTĐT 1902 ngày 16/6/2025, QĐ dự án 2573 ngày 26/12/2025 cho T2); đường dọc sông Hồng kết nối cửa khẩu Bản Vược đến Y Tý 187.448 (QĐ 2805/QĐ-UBND 01/11/2024, lồng ghép 50 tỷ nguồn tiền sử dụng đất).

### Vì sao đáng lưu vào plugin khoáng sản

70.000 triệu (27% phần đã phân bổ) là đường nội bộ KCN Tằng Loỏng — địa bàn chế biến khoáng sản, luyện kim, hóa chất của tỉnh. Tỉnh đã xác lập **tiền lệ** dùng nguồn thu đóng góp khai thác khoáng sản để đầu tư hạ tầng phục vụ chính khu vực có hoạt động khoáng sản. Với 1.336.931 còn chưa phân bổ, ref 15 nêu 04 hướng đề xuất có căn cứ: đường nội bộ còn lại KCN Tằng Loỏng; hạ tầng - XLNT - bãi thải khu chế biến (bãi thải gyps → `bvmt-sct-vn`); hạ tầng CCN gắn chế biến khoáng sản (Mông Sơn, Tân Nguyên — xã Bảo Ái); khắc phục hư hỏng đường do xe vận chuyển khoáng sản.

### Quy tắc viện dẫn đã ghi

- Gọi **đúng tên nguồn theo quyết định**: "nguồn thu đóng góp từ các tổ chức, cá nhân khai thác khoáng sản". KHÔNG gọi tắt thành "phí khoáng sản", "thuế tài nguyên", "tiền cấp quyền khai thác" — khác nhau về bản chất pháp lý và cơ quan thu.
- Không viết "đã được cấp vốn" mà "đã được bố trí trong kế hoạch đầu tư công trung hạn giai đoạn 2026-2030…".
- Kế hoạch có thể điều chỉnh giữa kỳ từ phần chưa phân bổ → kiểm tra quyết định điều chỉnh sau 09/7/2026, hỏi Bạn.
- Phân định: reference 15 chỉ nói phần **chi đầu tư công**; nghĩa vụ **thu** (tiền cấp quyền, thuế tài nguyên, phí BVMT, đóng góp hỗ trợ địa phương) thuộc Sở Tài chính, Thuế, Sở Nông nghiệp và Môi trường.
- Bẫy đọc file: bản .doc lưu hành nội bộ là dự thảo trình ký, ô số/ngày TRỐNG; chỉ bản PDF đã ký có số 2390 và ngày 09/7/2026.

### Thay đổi SKILL.md

Thêm nghiệp vụ số 9 "Nguồn thu đóng góp từ tổ chức, cá nhân khai thác khoáng sản trong đầu tư công" trỏ reference `15`; bổ sung từ khoá "QĐ 2390/2026 nguồn thu đóng góp KS" vào `description` (rút gọn vài cụm để giữ 1016/1024 ký tự).

Liên kết: phần KCN/CCN của cùng quyết định → `kccn-sct-vn` ref 22; cấp điện nông thôn do SCT làm chủ đầu tư → `quy-hoach-ct-vn` ref 09. PDF gốc lưu tại `kccn-sct-vn/.../van-ban-goc/QD-2390-2026-KH-dau-tu-cong-trung-han-2026-2030.pdf`.


## v1.0.0 (17/7/2026)
- Phát hành lần đầu: plugin quản lý nhà nước về khoáng sản của Sở Công Thương tỉnh Lào Cai.
- Khung pháp lý: Luật ĐC&KS 54/2024 (sửa bởi Luật 147/2025), NĐ 193/2025 (sửa bởi NĐ 21/2026), NQ 66.19/2026 Phụ lục VIII, TT 24/43/67/2025 + TT 26/2026/TT-BCT, TT 37/2025/TT-BCT, chùm TT BNNMT 2025, Chỉ thị 11-CT/TU + 26-CT/TU, CV 5973/UBND-KT.
- 11 references, 5 mẫu văn bản, 2 checklist, 3 file dữ liệu CSV (208 GP khai thác 31/10/2025; 43 GP thăm dò Yên Bái 6/2025; theo dõi pháp lý 209 mỏ 4/2026), 17 văn bản gốc.
- 6 nghiệp vụ: phân vai liên ngành; KH quản lý rủi ro; huấn luyện - GCN KTAT khai thác KS hầm lò; chế biến - nguồn gốc; đối chiếu VLNCN - sản lượng; kiểm tra - xử phạt - báo cáo.

## v1.1.0 (20/7/2026)
- Thêm reference 12 (khoáng sản trong thẩm định dự án, thành lập CCN — quy trình rà 4 lớp chồng lấn QĐ 866/1626/525/1277, case CCN Báo Đáp chồng mỏ Caolanh - felspat theo CV 6791/SNNMT-KHTC ngày 17/7/2026) và reference 13 (cấu trúc chuẩn báo cáo năm theo đề cương Bộ NNMT + số liệu nền chính thức 2025: 178 GP khai thác còn hiệu lực, đấu giá, tiền cấp quyền, 4 kết luận thanh tra, vướng mắc đã kiến nghị).
- Thêm mẫu 06 (ý kiến khoáng sản trong thẩm định + công văn yêu cầu chủ đầu tư điều chỉnh ranh giới chồng lấn).
- Bổ sung GATE NĐ 136/2025/NĐ-CP Điều 34 (từ 12/6/2025 nhóm II về Chủ tịch UBND tỉnh) vào references 01, 03; thẩm quyền khoanh định khu vực cấm theo Luật 147/2025; QĐ 1277/QĐ-TTg khu dự trữ; NĐ 23/2020 cát sỏi; các CV chỉ đạo mới (4115, 4330/UBND-KT, 196/UBND-KT, 10699/BNNMT-ĐCKS).
- Nghiệp vụ mở rộng 6 → 7; văn bản gốc 17 → 19 file.

## v1.2.0 (24/7/2026)
- **Nghiệp vụ mở rộng 7 → 8**: thêm nghiệp vụ "Thống kê, kê khai, kiểm soát sản lượng và báo cáo định kỳ hoạt động khoáng sản".
- Thêm reference **14** (chắt lọc CV 5141/SNNMT-KS ngày 29/12/2025 của Sở Nông nghiệp và Môi trường): bảng phân luồng nơi nhận báo cáo định kỳ theo nhóm khoáng sản (SCT nhận nhóm I và nước nóng - nước khoáng thiên nhiên tỉnh cấp; nhóm II/III/IV đi luồng Sở Xây dựng); kỳ báo cáo và hạn nộp 15/02; mẫu 05/06/07/08 Phụ lục IV TT 36/2025/TT-BNNMT; hai lớp thống kê trữ lượng và thứ tự ưu tiên căn cứ xác định (K3 Đ59 NĐ 193/2025); vị trí và loại thiết bị cân - đo (có chế biến phải 02 điểm; thiết bị đo đạc chỉ dùng cho nước khoáng - nước nóng, đá ốp lát, cát sỏi lòng sông - lòng hồ - biển, KS ghi công suất theo thể tích); bốn loại sổ sách - chứng từ với tần suất ghi chép hàng ngày/hàng tháng; **ngưỡng chênh lệch 10%** buộc doanh nghiệp giải trình; chế độ lưu giữ bản gốc và bản sao tại văn phòng mỏ; bản đồ - mặt cắt hiện trạng 01 năm 01 lần chốt 31/12; yêu cầu với UBND cấp xã.
- Reference **07**: bổ sung mục VI về công văn nghĩa vụ sau cấp phép của SNNMT (mẫu chuẩn CV 6795/SNNMT-KS ngày 17/7/2026, mỏ sắt Quý Xa) kèm 5 đầu việc SCT phải mở hồ sơ theo dõi khi nhận được; bổ sung 3 dòng nghĩa vụ mới trong quá trình khai thác (sử dụng đất theo K2 Đ205 Luật Đất đai 2024; sử dụng nước - xả thải Đ36; BVMT Đ79-80 Luật ĐC&KS) và làm rõ căn cứ KH quản lý rủi ro, báo cáo định kỳ.
- Reference **02**: bổ sung nhiệm vụ số 8 của SCT (nơi nhận báo cáo định kỳ nhóm I) và vai trò tương ứng của Sở Xây dựng.
- Reference **09**: bổ sung 4 văn bản của SNNMT (CV 1085 ngày 19/8/2025, CV 1297 ngày 25/8/2025, CV 4611 ngày 12/12/2025, CV 5141 ngày 29/12/2025, CV 6795 ngày 17/7/2026) và nhịp theo dõi chiều NHẬN báo cáo trước 15/02 hằng năm.
- Reference **10**: thêm mục I-b ghi nhận giấy phép mới ngoài mốc chốt CSV — **GP 199/GP-BNNMT ngày 14/7/2026** cấp cho Công ty cổ phần Khai thác và Chế biến kim loại Thủ Đô khai thác quặng sắt mỏ Quý Xa, xã Văn Bàn.
- Checklist hồ sơ pháp lý mỏ: thêm nhóm 5b (thống kê - kê khai - báo cáo sản lượng, 10 điểm rà) và 3 cờ đỏ mới.
- Văn bản gốc 19 → 21 file (bổ sung toàn văn CV 5141 và CV 6795).

## v1.3.0 (24/7/2026)
- Chắt lọc **CV 6987/SNNMT-KS ngày 23/7/2026** (PGĐ Phạm Năng Chung ký) — công văn nghĩa vụ sau cấp phép gửi Công ty Cổ phần Công nghiệp Khánh An, mỏ **đất hiếm** khu vực Bến Đền, xã Gia Phú và xã Bảo Thắng (GP 197/GP-BNNMT ngày 13/7/2026 của Bộ trưởng Bộ NNMT, khai thác tổng oxit đất hiếm TR2O3 không bao gồm CeO2).
- Reference **07** mục VI: nay có 2 tiền lệ cùng khuôn (CV 6795 + CV 6987, cách nhau 6 ngày) — xác nhận quy trình lặp ổn định của SNNMT (ban hành trong ~10 ngày sau ngày cấp GP); bổ sung lưu ý trích dẫn giấy phép cấp theo thành phần có ích kèm loại trừ (không rút gọn "khai thác đất hiếm").
- Reference **10** mục I-b: thêm dòng GP 197/GP-BNNMT — mỏ đất hiếm thứ 2 trên bảng theo dõi toàn tỉnh; mỏ nằm trên 2 xã; doanh nghiệp trụ sở Hà Nội (lưu bản sao sổ sách tại văn phòng mỏ).
- Reference **09**: thêm CV 6987 vào danh mục văn bản SNNMT.
- Văn bản gốc 21 → 22 file (toàn văn CV 6987).
