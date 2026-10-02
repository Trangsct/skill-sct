---
name: dat-dai-sct-vn
description: "ĐẤT ĐAI phục vụ dự án công nghiệp, Sở Công Thương Lào Cai: THU HỒI ĐẤT, BỒI THƯỜNG, HỖ TRỢ, TÁI ĐỊNH CƯ, giải phóng mặt bằng (GPMB). Kích hoạt: thu hồi đất, bồi thường, hỗ trợ, tái định cư, GPMB, mặt bằng sạch, kế hoạch thu hồi đất, thông báo thu hồi đất, kiểm đếm bắt buộc, phương án bồi thường, niêm yết, chi trả, cưỡng chế thu hồi đất, thưởng bàn giao mặt bằng trước thời hạn, trích đo địa chính, chỉnh lý hồ sơ địa chính, Hội đồng bồi thường, đơn vị tổ chức thực hiện nhiệm vụ bồi thường, UBND cấp xã. Nguồn: Sổ tay hướng dẫn trình tự, thủ tục bồi thường, hỗ trợ, tái định cư của Sở Nông nghiệp và Môi trường tỉnh Lào Cai (7/2026): quy trình 12 bước, thẩm quyền cấp xã, bảng mốc thời hạn, 10 tình huống phát sinh, 39 biểu mẫu. Dùng khi: đọc báo cáo GPMB KCN, CCN của xã và chủ đầu tư; xác định hồ sơ đang ở bước nào; viết phần vướng mắc GPMB trong báo cáo, tờ trình; trả lời doanh nghiệp. Từ khóa thêm: Luật Đất đai 31/2024/QH15, NĐ 88/2024, NĐ 102/2024, NĐ 151/2025, NĐ 49/2026, NQ 254/2025/QH15, QĐ 40/2026/QĐ-UBND."
---

# dat-dai-sct-vn — Đất đai phục vụ dự án công nghiệp (Sở Công Thương Lào Cai)

## I. KHI NÀO DÙNG PLUGIN NÀY

Sở Công Thương KHÔNG phải cơ quan quản lý đất đai và KHÔNG thực hiện thu hồi đất, bồi thường. Plugin này phục vụ ba việc của Phòng Quản lý công nghiệp:

1. **Đọc hiểu báo cáo GPMB** của UBND cấp xã, chủ đầu tư hạ tầng KCN, CCN, Ban Quản lý: xác định dự án đang ở bước nào trong 12 bước, còn bao nhiêu bước, mốc thời hạn tối thiểu còn lại → reference `03`, `04`, checklist `checklist-doc-bao-cao-gpmb.md`.
2. **Viết đúng thuật ngữ, đúng chủ thể** phần GPMB trong báo cáo, tờ trình, thông báo kết luận họp, công văn đôn đốc về KCN, CCN, dự án công nghiệp → reference `02`, `09`.
3. **Trả lời doanh nghiệp, chủ đầu tư** về trình tự, ai làm gì, hồ sơ chủ đầu tư phải cung cấp → reference `03` mục Bước 1, reference `09`.

Không dùng plugin này để: tính tiền bồi thường, áp giá đất, xác định loại đất, nguồn gốc đất của trường hợp cụ thể (thuộc UBND cấp xã, đơn vị tổ chức thực hiện nhiệm vụ bồi thường, Sở Nông nghiệp và Môi trường).

## II. NGUỒN VÀ MỨC ĐỘ TIN CẬY — ĐỌC TRƯỚC

Toàn bộ nội dung lấy từ **Sổ tay hướng dẫn trình tự, thủ tục bồi thường, hỗ trợ, tái định cư khi Nhà nước thu hồi đất** của Sở Nông nghiệp và Môi trường tỉnh Lào Cai (bìa ghi Ủy ban nhân dân tỉnh Lào Cai - Sở Nông nghiệp và Môi trường; file PDF tạo ngày 27/7/2026; 119 trang in, 61 trang PDF dạng trang đôi).

- Sổ tay là **tài liệu hướng dẫn, tuyên truyền**: không có số, ký hiệu, ngày ban hành, người ký. **CẤM viện dẫn Sổ tay làm căn cứ pháp lý** trong văn bản của Sở; chỉ viện dẫn luật, nghị định, nghị quyết, quyết định mà Sổ tay dẫn tới.
- Ngày 02/10/2026 đã đối chiếu các điều khoản Sổ tay dẫn với **bản gốc** Luật Đất đai, NQ 254/2025/QH15, NQ 66.3/2025/NQ-CP, NĐ 88/2024, NĐ 102/2024, NĐ 151/2025, NĐ 49/2026, Văn bản 1153/BNNMT-QLĐĐ (bản Word trong `van-ban-goc/trung-uong/`). Phần lớn khớp; 07 điểm Sổ tay dẫn chưa đúng hoặc chưa đủ và 11 quy định Sổ tay chưa nêu ghi ở reference `11` — **đọc reference `11` trước khi viện dẫn điều khoản**.
- Chưa có bản gốc: QĐ 40/2026/QĐ-UBND (phân cấp cho Chủ tịch UBND cấp xã), quy định trình tự, thủ tục của tỉnh, QĐ 18/2025/QĐ-UBND, QĐ 43/2026/QĐ-UBND, NĐ 101/2024. Nội dung dựa vào các văn bản này vẫn là "theo Sổ tay"; chưa đối chiếu thì viết "theo quy định của pháp luật về đất đai", không dẫn điều khoản.
- Các mốc 02 ngày, 03 ngày làm việc, 05 ngày làm việc trong quy trình chỉ có trong Sổ tay, không có trong luật, nghị định.
- Sổ tay có 18 điểm chưa thống nhất hoặc dẫn chưa đúng (số biểu mẫu, thời hạn niêm yết ghi trong mẫu, tên phòng chuyên môn, mẫu NĐ 151 đã hết hiệu lực, Điều 39 NĐ 102) → reference `10`. Gặp các điểm này lấy theo phần thân quy trình và điều luật được dẫn.
- Bản gốc Sổ tay: `van-ban-goc/So-tay-BTHTTDC-SNNMT-Lao-Cai-7-2026.pdf` (13,4 MB, chỉ có trên GitHub); bản trích chữ bằng máy: `van-ban-goc/So-tay-BTHTTDC-SNNMT-Lao-Cai-7-2026-OCR.txt` (có lỗi nhận dạng, chỉ dùng để tìm kiếm).

## III. TÓM TẮT CỐT LÕI

**Chủ thể** (reference `02`): Chủ tịch UBND cấp xã ban hành thông báo thu hồi đất, quyết định kiểm đếm bắt buộc, quyết định phê duyệt phương án bồi thường, hỗ trợ, tái định cư, quyết định thu hồi đất, quyết định cưỡng chế; quyết định thành lập Hội đồng bồi thường, hỗ trợ, tái định cư theo từng dự án. Đơn vị, tổ chức thực hiện nhiệm vụ bồi thường, hỗ trợ, tái định cư lập kế hoạch, kiểm đếm, lập phương án, chi trả. Phòng Kinh tế (xã) hoặc Phòng Kinh tế, Hạ tầng và Đô thị (phường) hoặc Phòng Nông nghiệp và Môi trường thẩm định, trình. Chủ đầu tư có văn bản đề nghị kèm hồ sơ dự án, cung cấp bản vẽ ranh giới, bảo đảm kinh phí.

**12 bước** (reference `03`): (1) xây dựng kế hoạch thu hồi đất, điều tra, khảo sát, đo đạc, kiểm đếm; (2) họp với người có đất trong khu vực thu hồi; (3) thông báo thu hồi đất; (4) điều tra, khảo sát, đo đạc, kiểm đếm, xác định nguồn gốc đất; (5) lập phương án; (6) niêm yết, lấy ý kiến; (7) thẩm định, phê duyệt phương án; (8) niêm yết, gửi phương án đã phê duyệt; (9) chi trả; (10) quyết định thu hồi đất; (11) vận động bàn giao mặt bằng; (12) quản lý quỹ đất đã thu hồi.

**Mốc thời hạn hay dùng** (đủ bảng tại reference `04`):

| Việc | Thời hạn theo Sổ tay |
|---|---|
| Xây dựng kế hoạch thu hồi đất | 10 ngày kể từ ngày nhận văn bản đề nghị của chủ đầu tư kèm hồ sơ dự án (k1 Đ28 NĐ 102/2024) |
| Gửi thông báo thu hồi đất trước khi ban hành quyết định thu hồi đất | chậm nhất 60 ngày với đất nông nghiệp, 120 ngày với đất phi nông nghiệp (điểm a k9 Đ3 NQ 254/2025/QH15); không áp dụng khi người có đất đồng ý thu hồi trước thời hạn hoặc khi thông báo được ban hành lại |
| Hiệu lực thông báo thu hồi đất | 12 tháng kể từ ngày ban hành |
| Niêm yết công khai phương án | 10 ngày (điểm b k9 Đ3 NQ 254/2025/QH15) |
| Đối thoại với trường hợp còn ý kiến không đồng ý | trong 30 ngày kể từ ngày tổ chức lấy ý kiến |
| Thẩm định phương án | không quá 30 ngày kể từ ngày nhận đủ hồ sơ (k3 Đ3 NĐ 88/2024; Sổ tay ghi 30 ngày làm việc) |
| Phê duyệt phương án | không quá 05 ngày làm việc (theo Sổ tay) |
| Chi trả tiền bồi thường, hỗ trợ | 30 ngày kể từ ngày quyết định phê duyệt phương án có hiệu lực |
| Ban hành quyết định thu hồi đất | 10 ngày kể từ ngày đủ một trong 07 điều kiện (reference `03` Bước 10) |

## IV. QUY TẮC HÀNH VĂN KHI SỞ VIẾT VỀ GPMB

1. Hiện trạng GPMB do UBND cấp xã, chủ đầu tư quản lý: số liệu diện tích đã thu hồi, đã chi trả, số hộ còn vướng lấy từ báo cáo của xã, chủ đầu tư (kỳ cập nhật mới nhất trong `kccn-sct-vn`); không tự suy ra từ mốc thời hạn.
2. Giao việc đúng chủ thể: việc ban hành thông báo, quyết định, tổ chức kiểm đếm, cưỡng chế ghi "đề nghị UBND xã (phường)…"; việc hướng dẫn nghiệp vụ đất đai, kiểm tra, ký duyệt bản đồ địa chính ghi "đề nghị Sở Nông nghiệp và Môi trường…"; không giao cho Sở Công Thương.
3. Dùng đúng tên gọi: "thông báo thu hồi đất", "quyết định kiểm đếm bắt buộc", "quyết định cưỡng chế thực hiện quyết định kiểm đếm bắt buộc", "phương án bồi thường, hỗ trợ, tái định cư", "quyết định thu hồi đất", "quyết định cưỡng chế thực hiện quyết định thu hồi đất", "đơn vị, tổ chức thực hiện nhiệm vụ bồi thường, hỗ trợ, tái định cư".
4. Khi ước tiến độ: cộng các mốc tối thiểu ở reference `04` mục B, ghi rõ là thời gian tối thiểu theo trình tự, chưa kể thời gian vận động, kiểm đếm bắt buộc, cưỡng chế.
5. Không chép số biểu mẫu trong phần thân Sổ tay (mẫu số 01 đến 17) sang văn bản; số biểu mẫu đúng theo danh mục 39 mẫu ở Phụ lục → reference `08`.
6. Không dẫn Điều 5 và các mẫu số 45 đến 48 NĐ 151/2025/NĐ-CP (hết hiệu lực từ 31/01/2026 theo NĐ 49/2026/NĐ-CP); không dẫn Điều 39 NĐ 102/2024/NĐ-CP cho cưỡng chế thu hồi đất thực hiện dự án.
7. Giá đất, đơn giá bồi thường, diện tích tối thiểu tách thửa chỉ lấy từ văn bản của tỉnh ở reference `12`; khu, cụm công nghiệp chưa có trong Phụ lục IV Bảng giá đất thì không tự suy giá.

## V. CÁC REFERENCE FILES

| File | Nội dung |
|---|---|
| `references/01-nguon-va-van-ban-vien-dan.md` | Mô tả Sổ tay, mục lục theo trang in; danh mục văn bản pháp luật Sổ tay viện dẫn và điều khoản được dẫn; cảnh báo chưa đối chiếu bản gốc |
| `references/02-tham-quyen-cap-xa-va-hoi-dong.md` | Thẩm quyền, nhiệm vụ của UBND cấp xã, Chủ tịch UBND cấp xã; Hội đồng bồi thường, hỗ trợ, tái định cư; Tổ giúp việc kiểm đếm; vai trò chủ đầu tư |
| `references/03-quy-trinh-12-buoc.md` | Trình tự 12 bước: ai làm, hồ sơ, thời hạn, biểu mẫu từng bước |
| `references/04-bang-moc-thoi-han.md` | Bảng toàn bộ mốc thời hạn; cách cộng thời gian tối thiểu của một dự án |
| `references/05-kiem-dem-bat-buoc-va-cuong-che.md` | Kiểm đếm bắt buộc, cưỡng chế kiểm đếm bắt buộc, cưỡng chế thu hồi đất, xử lý tài sản khi cưỡng chế (có nội dung vật liệu nổ công nghiệp) |
| `references/06-thuong-khieu-nai-dia-chinh.md` | Thưởng bàn giao mặt bằng trước thời hạn; giải quyết khiếu nại; chỉnh lý hồ sơ địa chính; kiểm tra, nghiệm thu bản đồ địa chính, trích đo |
| `references/07-muoi-truong-hop-phat-sinh.md` | 10 tình huống phát sinh và cách xử lý |
| `references/08-danh-muc-39-bieu-mau.md` | Danh mục 39 biểu mẫu Phụ lục, trang in, cơ quan ký; bảng quy đổi số mẫu giữa phần thân và Phụ lục |
| `references/09-ap-dung-cho-so-cong-thuong.md` | Cách dùng cho KCN, CCN, dự án công nghiệp: đọc báo cáo xã, câu hỏi cần hỏi, mẫu câu |
| `references/10-diem-chua-thong-nhat-trong-so-tay.md` | Các điểm chưa thống nhất, lỗi in trong Sổ tay và cách xử lý |
| `references/11-doi-chieu-ban-goc-va-bo-sung.md` | Kết quả đối chiếu Sổ tay với bản gốc; 07 điểm dẫn chưa đúng; 11 quy định Sổ tay chưa nêu (ngoại lệ 75%, thu hồi trước khi phê duyệt phương án, thời gian không cưỡng chế, di dời cơ sở sản xuất…); bảng ngày ban hành, hiệu lực; văn bản còn thiếu |
| `references/12-van-ban-tinh-lao-cai-gia-dat-don-gia-tach-thua.md` | NQ 19/2025/NQ-HĐND Bảng giá đất (giá đất nông nghiệp, giá đất từng KCN, CCN); QĐ 21/2025/QĐ-UBND bồi thường nhà, công trình, di chuyển máy móc; QĐ 49/2026/QĐ-UBND diện tích tối thiểu tách thửa |
| `checklists/checklist-doc-bao-cao-gpmb.md` | Bảng kiểm khi đọc báo cáo GPMB của xã, chủ đầu tư |
| `van-ban-goc/00-MUC-LUC.md` | Mục lục văn bản gốc |

## VI. LIÊN KẾT PLUGIN

| Plugin | Khi nào chuyển sang |
|---|---|
| `kccn-sct-vn` | Hiện trạng GPMB từng KCN, CCN (kỳ cập nhật mới nhất), điều kiện khởi công, tiến độ NQ 34-NQ/TU |
| `dacn-sct-vn` | Điểm nghẽn GPMB của dự án động lực, báo cáo tăng trưởng |
| `xp-sct-vn` | Xử phạt vi phạm hành chính về đất đai trong CCN |
| `xd-sct-vn` | Điều kiện khởi công, giấy phép xây dựng sau khi có mặt bằng |
| `qlks-sct-vn` | Thu hồi khoáng sản, đất đá thải trong phạm vi dự án |
| `sd-vlncn-sct-vn`, `kho-vlncn-sct-vn` | Vật liệu nổ công nghiệp trên đất bị cưỡng chế thu hồi; nổ mìn phục vụ san gạt mặt bằng |
| `vbhc-vn`, `sct-laocai-org-vn` | Thể thức văn bản, người ký |
