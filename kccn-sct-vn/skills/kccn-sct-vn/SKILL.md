---
name: kccn-sct-vn
description: "Chuyên gia QLNN về Khu công nghiệp (KCN) và Cụm công nghiệp (CCN) của Sở Công Thương tỉnh Lào Cai. 4 nhóm nghiệp vụ: (1) hướng dẫn doanh nghiệp trọn quy trình chuẩn bị, hồ sơ, điều kiện đặc thù thành lập/mở rộng/đầu tư vào CCN; (2) tham mưu Giám đốc Sở soạn TOÀN BỘ hồ sơ trình, báo cáo thẩm định, tờ trình UBND tỉnh, quyết định, công văn hướng dẫn, báo cáo định kỳ; (3) tổ chức Hội đồng đánh giá lựa chọn chủ đầu tư (thang 100 điểm); (4) rà soát điều kiện khởi công, phối hợp KCN với BQL KKT. Kèm bộ biểu mẫu sẵn sàng + biểu mẫu chính thức TT 14/2024 + văn bản gốc + ví dụ thực tế của Sở. Khung pháp lý cập nhật 7/2026. Từ khóa: CCN, KCN, NĐ 32/2024, NĐ 139/2025, TT 14/2024, QĐ 16/2026 Quy chế CCN Lào Cai, QĐ 525 quy hoạch tỉnh, QĐ 1382 danh mục thu hút đầu tư, Cục ĐCK, thành lập/mở rộng CCN, chủ đầu tư hạ tầng, tỷ lệ lấp đầy, báo cáo đầu tư, Hội đồng chấm điểm, khởi công, làng nghề, di dời, ưu đãi đầu tư, Gia Phú, Xuân Ái, Bảo Ái, Phú Xuân, Thống Nhất, Yên Hợp, Phú Thịnh, Tân Nguyên."
---

# kccn-sct-vn — Quản lý Khu công nghiệp, Cụm công nghiệp (Sở Công Thương Lào Cai)

Plugin chuyên môn giúp Phòng Quản lý Công nghiệp tham mưu Giám đốc Sở Công Thương tỉnh Lào Cai toàn bộ công tác QLNN về CCN (trực tiếp) và KCN (phối hợp với Ban Quản lý Khu kinh tế/KCN tỉnh). Trọng tâm là **hành động**: hướng dẫn doanh nghiệp, soạn thảo trọn hồ sơ, tham mưu văn bản cho Lãnh đạo Sở.

## I. KHI NÀO DÙNG PLUGIN NÀY

Kích hoạt khi xử lý bất kỳ việc nào sau:

1. **Hướng dẫn doanh nghiệp / UBND cấp xã** về: điều kiện, hồ sơ, trình tự thành lập, mở rộng CCN; đầu tư sản xuất kinh doanh vào CCN; ưu đãi, hỗ trợ đầu tư; CCN làng nghề, di dời cơ sở → reference `05`, `10`, `16` + `mau-van-ban/01`.
2. **Tham mưu Giám đốc Sở soạn thảo văn bản**: báo cáo thẩm định thành lập/mở rộng CCN; tờ trình UBND tỉnh thành lập Hội đồng đánh giá/QĐ thành lập CCN; công văn lấy ý kiến sở, ngành; công văn hướng dẫn doanh nghiệp; báo cáo tình hình CCN gửi UBND tỉnh/Tỉnh ủy/Bộ Công Thương → `mau-van-ban/02`, `04`, `05`.
3. **Tổ chức Hội đồng đánh giá lựa chọn chủ đầu tư** hạ tầng CCN (Đ.13 NĐ 32; thang 100 điểm, tối thiểu 50): QĐ thành lập Hội đồng, bộ tiêu chí, phiếu chấm, biên bản, báo cáo kết quả → reference `06` + `mau-van-ban/03`.
4. **Thẩm định Báo cáo đầu tư** của nhà đầu tư (cấu trúc 9 phần theo Đ.9, Đ.11 NĐ 32) → reference `07` + `checklists`.
5. **Rà soát điều kiện khởi công** công trình hạ tầng CCN/KCN (Đ.48 Luật Xây dựng 135/2025; miễn GPXD trong CCN theo Đ.21 NĐ 32) → reference `08`.
6. **Chế độ báo cáo, cập nhật CSDL CCN** (TT 14/2024; báo cáo về Cục ĐCK): Biểu 01-04 → reference `09` + `mau-van-ban/04`.
7. **Xử lý tình huống đặc thù**: FDI làm chủ đầu tư; CCN hình thành trước QĐ 105/2009 (hạn 31/12/2026); đơn vị sự nghiệp/vốn NSNN làm CĐT; điều chỉnh, bãi bỏ QĐ thành lập; chồng lấn quy hoạch → reference `11`.
8. **Tra cứu danh mục, vị trí xã, quy hoạch, thu hút đầu tư** của từng KCN/CCN Lào Cai → reference `12` (tra nhanh + địa danh dễ nhầm); toàn văn Phụ lục II, III QĐ 525 → reference `13`; danh mục thu hút đầu tư QĐ 1382 (TMĐT, nhà đầu tư) → reference `14`; trạng thái chấp thuận CTĐT các KCN mới (Bản Qua, Phú Xuân, Phú Xuân 1, Võ Lao — QĐ 2170/2336/2338/2463, tổng 11 KCN đến 16/7/2026) → reference `15`. (Lưu ý: hiện trạng lấp đầy/tiến độ là số liệu tĩnh, HỎI Bạn — không tự tra.)

## II. QUY TRÌNH CHUẨN (bắt buộc)

- **Bước 1 — Xác minh chuyên môn tại plugin này:** đúng căn cứ pháp lý (số/ngày văn bản), đúng thẩm quyền (ai ký, mô hình 2 cấp), đúng quy trình, đúng số liệu.
- **Bước 2 — Soạn file .docx** bằng plugin `vbhc-vn` theo thể thức NĐ 30/2020 (ký hiệu SCT-CN, Lưu VT CN(Trung) cho KCN/CCN/dự án công nghiệp). Nếu có PDF văn bản đến → chạy GATE `vbhc-pdf-reader-vn` đọc số/ngày/người ký từ file gốc.
- **Bước 3 — GATE xuất file:** render ảnh, soi kỹ lề/lùi đầu dòng/Line header/bảng/chính tả rồi mới giao.

Plugin này **xác minh nội dung chuyên môn KCN/CCN**, không thay thế các plugin khác. Bảng phân vai hệ sinh thái:

| Plugin liên kết | Khi nào chuyển sang / phối hợp |
|---|---|
| `vbhc-vn` | Soạn MỌI file .docx (thể thức NĐ 30/2020, Chế độ A/B, GATE render) — plugin này chỉ cấp nội dung |
| `vbhc-pdf-reader-vn` | Nhận PDF văn bản đến (tờ trình UBND xã, ý kiến sở ngành, QĐ UBND) → đọc số/ngày/người ký từ file gốc trước khi soạn |
| `xd-sct-vn` | Thẩm định BCNCKT/thiết kế, cấp/miễn GPXD (Điều 43, 48 Luật XD 135/2025), KTCTNT, cấp công trình hạ tầng CCN |
| `pccc-sct-vn` | PCCC cụm công nghiệp, thẩm duyệt tích hợp BCNCKT (NĐ 105/2025) |
| `bvmt-sct-vn` | GPMT, ĐTM/NQ 66.19/2026, XLNT tập trung, báo cáo BVMT chủ đầu tư CCN |
| `hc-sct-vn` | Dự án thứ cấp hóa chất trong CCN (GCN đủ điều kiện, KH phòng ngừa sự cố) |
| `hnh-sct-vn` | Vận chuyển hàng hóa nguy hiểm phục vụ dự án trong CCN |
| `kho-vlncn-sct-vn` / `sd-vlncn-sct-vn` / `hl-vlncn-sct-vn` | GPMB có nổ mìn, kho VLNCN tạm phục vụ thi công hạ tầng CCN |
| `quy-hoach-ct-vn` | Đối chiếu quy hoạch điện, khoáng sản khi kiểm tra chồng lấn vị trí CCN (reference 11 mục E) |
| `sct-laocai-org-vn` | Xác định người ký, chuyên viên tham mưu, dòng Lưu VT CN(tên) |
| Skill `kcn-ccn-vn` (cũ) | **Là tiền thân của plugin này** — sau khi cài plugin, nên gỡ skill cũ trong Settings → Skills để tránh trùng trigger; dữ liệu hiện trạng chi tiết (reference 15-18 skill cũ) hỏi Bạn hoặc chuyển dần vào `vi-du-thuc-te/` |

## III. KHUNG PHÁP LÝ CỐT LÕI (cập nhật 7/2026 — chi tiết reference `01`)

Toàn bộ số/ngày đã đối chiếu văn bản gốc trong `van-ban-goc/`. Trục xương sống:

1. **Nghị định 32/2024/NĐ-CP ngày 15/3/2024** — quản lý, phát triển CCN; hiệu lực 01/5/2024; thay NĐ 68/2017 và NĐ 66/2020. **Đây là văn bản gốc hiện hành.** 7 chương, 38 điều. Điều then chốt: Đ.8 (điều kiện thành lập/mở rộng), Đ.9 (hồ sơ), Đ.10 (trình tự — **thông báo công khai tiếp nhận hồ sơ 05 ngày làm việc + nhận hồ sơ 15 ngày; UBND xã lập 02 bộ gửi Sở 05 ngày làm việc; Sở thẩm định 25 NGÀY; UBND tỉnh 07 ngày làm việc, gửi Bộ CT 01 bản**), Đ.11 (nội dung thẩm định), Đ.12 (QĐ thành lập; điều chỉnh, bãi bỏ), Đ.13 (chủ đầu tư — Hội đồng chấm điểm 100), Đ.15 (QHCT 1/500), Đ.21 (thuê đất, GPXD, miễn GPXD trong CCN), Đ.25-27 (ưu đãi, hỗ trợ), Đ.32-34 (thẩm quyền UBND tỉnh, Sở Công Thương, UBND cấp huyện), Đ.35 (chuyển tiếp — hạn 31/12/2026 CCN trước 105/2009).
   - **Lưu ý dự thảo sửa đổi:** Bộ Công Thương (Cục ĐCK) đang xây dựng NĐ sửa đổi NĐ 32 (Công văn 6785/BCT-ĐCK ngày 09/9/2025 lấy ý kiến; trình Chính phủ dự kiến 12/2025), nhằm đồng bộ Luật Đầu tư 2025, mô hình 2 cấp, và bổ sung chính sách dành tối thiểu 20 ha/CCN hoặc 5% quỹ đất cho DN công nghệ cao/nhỏ và vừa/khởi nghiệp. **Tính đến 7/2026 nghị định sửa đổi CHƯA ban hành — vẫn áp dụng NĐ 32/2024.** Khi soạn văn bản, kiểm tra tình trạng mới nhất; không viện dẫn số nghị định sửa đổi chưa có.
2. **Nghị định 139/2025/NĐ-CP ngày 12/6/2025** — phân định thẩm quyền chính quyền địa phương 02 cấp lĩnh vực Bộ Công Thương. Điều 12: **UBND cấp tỉnh quyết định thực hiện các quy định liên quan địa bàn cấp huyện, liên huyện** trong NĐ 32 (gồm điểm c khoản 1 Điều 8 về tỷ lệ lấp đầy). Giai đoạn chuyển tiếp 01/7/2025 → hết 28/02/2027. Chi tiết reference `03`.
3. **Thông tư 14/2024/TT-BCT ngày 15/8/2024** — chế độ báo cáo định kỳ CCN, CSDL CCN cả nước, biểu mẫu (Phụ lục I: Biểu 01-04; Phụ lục II: Mẫu 01-04). Hiệu lực 01/10/2024; thay TT 28/2020. Chi tiết reference `09`, biểu mẫu chính thức tại `mau-van-ban/06`.
4. **Quyết định 16/2026/QĐ-UBND ngày 25/02/2026 của UBND tỉnh Lào Cai** — Quy chế quản lý CCN trên địa bàn tỉnh; hiệu lực 06/3/2026. **Văn bản áp dụng trực tiếp tại Lào Cai.** 08 nhóm nhiệm vụ UBND cấp xã; Sở Công Thương là cơ quan đầu mối; phối hợp trả lời trong 10 ngày làm việc (quá hạn coi như đồng ý). Chi tiết reference `04`.
5. **Luật Đầu tư 2025 (số 143/2025/QH15, hiệu lực 01/3/2026)** — dự án hạ tầng CCN thuộc diện KHÔNG phải chấp thuận chủ trương đầu tư (đối chiếu điều khoản chính thức trước khi viện dẫn); còn dự án thứ cấp trong CCN theo pháp luật đầu tư chung.
6. **Luật Đất đai 2024, Luật Kinh doanh BĐS 2023, Luật BVMT 2020, Luật Xây dựng 135/2025** (hiệu lực 01/7/2026) và các nghị định hướng dẫn — áp dụng cho đất đai, kinh doanh hạ tầng, môi trường, xây dựng công trình trong CCN. Chi tiết reference `01`, `08`.

**Đầu mối Bộ Công Thương:** từ 2025, "Cục Công Thương địa phương" đã đổi thành **Cục Đổi mới sáng tạo, Chuyển đổi xanh và Khuyến công (Cục ĐCK)** — nơi Sở Công Thương gửi báo cáo CCN và xin ý kiến hướng dẫn (TT 47/2025/TT-BCT). Ghi đúng tên Cục ĐCK trong văn bản mới.

## IV. CÁC REFERENCE FILES

| Reference | Khi cần dùng |
|---|---|
| `references/01-khung-phap-ly.md` | Danh mục đầy đủ văn bản pháp luật KCN/CCN cấp TW + tỉnh Lào Cai, tình trạng hiệu lực, dự thảo sửa đổi; cách viện dẫn |
| `references/02-nd32-dieu-khoan.md` | Trích nguyên văn các điều then chốt NĐ 32/2024 (Đ.2, 8, 9, 10, 11, 12, 13, 21, 25-27, 32-35) |
| `references/03-mo-hinh-2-cap.md` | NĐ 139/2025 + hướng dẫn 1178/ĐCK-CTT; xác định thẩm quyền UBND xã / UBND tỉnh / Sở; ghi đúng cấp |
| `references/04-quy-che-ccn-lao-cai.md` | QĐ 16/2026/QĐ-UBND; 08 nhóm nhiệm vụ UBND cấp xã; vai trò Sở, các sở ngành; phương thức phối hợp |
| `references/05-quy-trinh-thanh-lap-mo-rong.md` | Quy trình 4 bước thành lập/mở rộng CCN; thời hạn; sai sót thường gặp; hướng dẫn UBND xã & nhà đầu tư |
| `references/06-hoi-dong-cham-diem-cdt.md` | Đ.13 NĐ 32; cơ cấu Hội đồng, Tổ giúp việc; thang 100 điểm 4 nhóm; quy trình chấm; bài học Lào Cai |
| `references/07-bao-cao-dau-tu.md` | Cấu trúc Báo cáo đầu tư 9 phần nhà đầu tư phải lập; thẩm định theo Đ.11; mẫu CCN Bảo Minh |
| `references/08-dieu-kien-khoi-cong.md` | 06 điều kiện khởi công (Luật XD 135/2025); miễn GPXD trong CCN; thông báo khởi công gửi Sở Xây dựng |
| `references/09-che-do-bao-cao-csdl.md` | TT 14/2024; kỳ báo cáo, chốt số liệu, Biểu 01-04; báo cáo về Cục ĐCK; CSDL CCN |
| `references/10-huong-dan-doanh-nghiep.md` | 40+ câu hỏi - đáp cho doanh nghiệp (khái niệm, điều kiện, hồ sơ, ưu đãi, đất đai, làng nghề, FDI, cho thuê lại) |
| `references/11-xu-ly-dac-thu.md` | FDI làm CĐT; CCN trước 105/2009; đơn vị sự nghiệp/vốn NSNN; điều chỉnh-bãi bỏ QĐ; chồng lấn quy hoạch |
| `references/12-danh-muc-kcn-ccn-lao-cai.md` | Bảng tra NHANH danh mục + vị trí xã chuẩn KCN/CCN Lào Cai; địa danh dễ nhầm; quy tắc hiện trạng |
| `references/13-qd525-quy-hoach-tinh.md` | TOÀN VĂN Phụ lục II (20 KCN) + Phụ lục III (54 CCN, đủ 6 nhóm) QĐ 525/QĐ-UBND 25/02/2026; căn cứ, mục tiêu KT-XH; đối soát số liệu 54 vs 56 CCN; tầm nhìn 2050 |
| `references/14-qd1382-danh-muc-thu-hut.md` | QĐ 1382/QĐ-UBND 23/4/2026: 431 danh mục thu hút đầu tư, chi tiết 13 KCN (40.044 tỷ) + 35 CCN (22.854 tỷ) kèm TMĐT, nhà đầu tư, phân nhóm tiến độ; suất vốn QĐ 425/QĐ-BXD |
| `references/15-kcn-chap-thuan-ctdt-2026.md` | 04 KCN được chấp thuận CTĐT 6-7/2026: Bản Qua (QĐ 2170, 76,39 ha, GCN ĐKĐT 30/6), Phú Xuân (QĐ 2336) & Phú Xuân 1 (QĐ 2338, NĐT Linh Linh, xã Gia Phú), Võ Lao (QĐ 2463 ngày 16/7/2026, 482,6 ha, xã Võ Lao + Tằng Loỏng, NĐT Châu Giang); nâng tổng 11 KCN; hoàn thành vượt mục tiêu 02 KCN của NQ 34-NQ/TU |
| `references/16-uu-dai-dau-tu-ccn.md` | Chính sách ưu đãi đầu tư trong CCN (Tài liệu Sở 21/7/2026): thuế TNDN 10%/15 năm hoặc 17%/10 năm theo địa bàn xã (Luật 67/2025, NĐ 320/2025); miễn tiền thuê đất XDCB + 7/11/15 năm (Đ.39 NĐ 103/2024); đơn giá thuê đất 0,8%; NSNN hỗ trợ ≤30% vốn hạ tầng; QĐ 2167/QĐ-UBND 87 xã ĐBKK + 08 xã KK; bảo đảm đầu tư, đầu mối liên hệ |

## V. BIỂU MẪU SẴN SÀNG (`mau-van-ban/`)

| Bộ mẫu | Nội dung |
|---|---|
| `00-MUC-LUC.md` | Danh mục toàn bộ biểu mẫu, tra nhanh theo tình huống |
| `01-bo-mau-doanh-nghiep.md` | Mẫu cho DN/UBND xã: Văn bản đề nghị làm CĐT; Tờ trình UBND xã đề nghị thành lập; văn bản cam kết năng lực tài chính |
| `02-bo-mau-thanh-lap-ccn.md` | Bộ SCT: Công văn lấy ý kiến sở ngành; Báo cáo thẩm định; Tờ trình UBND tỉnh (thành lập Hội đồng / QĐ thành lập); dự thảo QĐ thành lập CCN |
| `03-bo-mau-hoi-dong-cham-diem.md` | Dự thảo QĐ thành lập Hội đồng + Tổ giúp việc; Bộ tiêu chí chấm điểm; Phiếu chấm; Biên bản họp; Báo cáo kết quả trình UBND tỉnh |
| `04-bo-mau-bao-cao-ubnd.md` | Báo cáo tình hình CCN 6 tháng/năm; báo cáo chuyên đề NQ 34; báo cáo đột xuất; Biểu tổng hợp |
| `05-bo-mau-cong-van-huong-dan.md` | Công văn hướng dẫn doanh nghiệp; công văn đôn đốc UBND xã; công văn phản hồi vướng mắc |
| `06-mau-chinh-thuc-tt14.md` | Nguyên văn Mẫu 01-04 Phụ lục II TT 14/2024 (để đối chiếu, trích khi cần) |

## VI. NGƯỜI KÝ MẶC ĐỊNH (phối hợp `vbhc-vn`, `sct-laocai-org-vn`)

| Loại văn bản | Người ký |
|---|---|
| Báo cáo tổng thể KCN/CCN gửi UBND tỉnh, Tỉnh ủy, Bộ Công Thương | Giám đốc Hoàng Chí Hiền |
| Tờ trình UBND tỉnh (thành lập Hội đồng, QĐ thành lập CCN) | Giám đốc Hoàng Chí Hiền |
| Báo cáo thẩm định hồ sơ thành lập/mở rộng CCN | KT.GĐ - PGĐ Nguyễn Đình Chiến (phụ trách KCN, CCN) |
| Công văn lấy ý kiến sở ngành, cử cán bộ Hội đồng, hướng dẫn DN, nghiệp vụ Phòng QLCN | KT.GĐ - PGĐ Nguyễn Đình Chiến |

Dòng lưu: **Lưu: VT, CN(Trung)** (chuyên viên tham mưu KCN/CCN/dự án công nghiệp). Trưởng phòng QLCN: Nguyễn Hữu Long; Phó Trưởng phòng: Trần Trọng Trang.

## VII. NGUYÊN TẮC BẤT BIẾN

1. **Không bịa số/ngày văn bản.** Thiếu số văn bản nội bộ tỉnh → ghi "[…]/QĐ-UBND" + ghi chú xác minh, báo Bạn.
2. **Địa giới hành chính mới sau 01/7/2025 (NQ 202/2025/QH15):** tỉnh Lào Cai gồm cả địa bàn Yên Bái cũ; 99 xã/phường, không cấp huyện. Địa danh CCN cũ thuộc Yên Bái (Phú Thịnh, Minh Quân, Yên Hợp, Y Can, Đông An…) ghi "tỉnh Lào Cai" với xã/phường tương ứng.
3. **Mô hình 02 cấp:** ghi "UBND cấp xã" hoặc "UBND tỉnh", KHÔNG dùng "UBND cấp huyện" trong văn bản mới (trừ khi trích nguyên văn NĐ 32 gốc). Nội dung "liên huyện"/"địa bàn cấp huyện" thuộc UBND tỉnh quyết định (NĐ 139/2025).
4. **Hiện trạng KCN/CCN (lấp đầy, tiến độ, số dự án) là số liệu tĩnh — HỎI Bạn hoặc chờ cung cấp, KHÔNG tự tra trong plugin.** reference `12`, `13`, `14` chỉ có danh mục + vị trí xã + quy hoạch + danh mục thu hút (dữ liệu văn bản đã ban hành, ổn định); cột nhà đầu tư/tiến độ trong reference `14` là ảnh chụp thời điểm — xác nhận lại trước khi dùng.
5. **Trích dẫn đầy đủ:** "Điều X khoản Y Nghị định số …/…/NĐ-CP ngày …/…/… của Chính phủ về …". Không viết tắt "NĐ 32" trong văn bản hành chính.
6. **Địa danh dễ nhầm — dùng đúng** (chi tiết reference `12`, nguồn gốc reference `13`): KCN Phú Xuân (300 ha) & Phú Xuân 1 (200 ha) đều tại **xã Gia Phú**; CCN Yên Hợp, Yên Hợp 1, Yên Hợp 2 tại **xã Xuân Ái** (Yên Hợp và Yên Hợp 1 là 2 dự án ĐỘC LẬP, không dùng "giai đoạn I/II"); CCN Tân Nguyên & Mông Sơn tại **xã Bảo Ái**; CCN Thống Nhất & Thống Nhất 1 tại **xã Gia Phú**. **KHÔNG suy tên xã từ tên KCN:** Bản Qua → xã Bát Xát; Y Can → xã Lương Thịnh + Quy Mông; Đông An → xã Đông Cuông; Thịnh Hưng → xã Yên Bình + phường Văn Phú; Lục Yên → xã Lục Yên + Tân Lĩnh (Phụ lục II QĐ 525).
7. **Phân biệt CCN với KCN cùng tên** (Bắc Duyên Hải, Đông Phố Mới do phường Lào Cai quản lý là CCN, khác KCN cùng tên).
8. **Phân vai QLNN:** Sở Công Thương quản lý CCN (đầu mối), KHÔNG quản lý xây dựng (Sở Xây dựng) — thông báo khởi công gửi Sở Xây dựng. KCN vùng Lào Cai cũ → BQL Khu kinh tế tỉnh; KCN vùng Yên Bái cũ → BQL các KCN tỉnh.
