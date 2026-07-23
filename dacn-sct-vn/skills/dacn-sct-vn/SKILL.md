---
name: dacn-sct-vn
description: "Điều hành DANH MỤC DỰ ÁN CÔNG NGHIỆP phục vụ MỤC TIÊU TĂNG TRƯỞNG tỉnh Lào Cai theo NQ 169/NQ-CP ngày 27/6/2026 và Công văn triển khai của UBND tỉnh (17/7/2026). 6 nghiệp vụ: (1) tra 09 chỉ tiêu Sở Công Thương chủ trì + chỉ tiêu phối hợp, mục tiêu 2026 và 2026-2030; (2) lập, cập nhật, xếp hạng danh mục dự án động lực (KCN, CCN, khoáng sản, luyện kim, hóa chất, điện, chế biến, thương mại); (3) phân tích sản xuất công nghiệp hằng tháng, tính % kế hoạch, so cùng kỳ, cảnh báo sản phẩm hụt chỉ tiêu; (4) nhận diện điểm nghẽn (GPMB, quy hoạch, đất đai, GPXD, môi trường, PCCC) và phương án tháo gỡ; (5) báo cáo định kỳ trước ngày 20 gửi Sở Tài chính, lồng ghép NQ 01/NQ-CP; (6) kịch bản tăng trưởng, dự báo hoàn thành. Từ khóa: NQ 169/NQ-CP, KL 18-KL/TW, NQ 25/2026/QH16, NQ 109/NQ-CP, tăng trưởng, IIP, chỉ số sản xuất công nghiệp, chế biến chế tạo, GRDP, điện thương phẩm, kim ngạch xuất nhập khẩu, tổng mức bán lẻ, tiết kiệm năng lượng, dự án động lực, điểm nghẽn, báo cáo trước ngày 20."
---

# dacn-sct-vn — Quản lý dự án công nghiệp phục vụ mục tiêu tăng trưởng (Sở Công Thương Lào Cai)

Plugin giúp Phòng Quản lý Công nghiệp tham mưu Giám đốc Sở **điều hành theo chỉ tiêu**: gắn từng dự án công nghiệp trên địa bàn với chỉ tiêu tăng trưởng được giao, theo dõi tiến độ, cảnh báo sớm và soạn văn bản tham mưu.

Khác biệt với các plugin khác trong hệ sinh thái: `kccn-sct-vn` quản lý **thủ tục** thành lập KCN/CCN; `qlks-sct-vn`, `hc-sct-vn`, `tkm-sct-vn`... quản lý **chuyên ngành**. Plugin này quản lý **kết quả đầu ra và đóng góp tăng trưởng** của toàn bộ dự án công nghiệp, bất kể dự án thuộc lĩnh vực nào.

---

## I. KHI NÀO DÙNG PLUGIN NÀY

Kích hoạt khi xử lý bất kỳ việc nào sau đây:

1. **Tra chỉ tiêu tăng trưởng được giao**: chỉ tiêu nào Sở Công Thương chủ trì, chỉ tiêu nào phối hợp, mục tiêu năm 2026, mục tiêu giai đoạn 2026-2030, cơ quan phối hợp → reference `02`.
2. **Lập/cập nhật danh mục dự án động lực tăng trưởng**, xếp nhóm ưu tiên, gắn dự án với chỉ tiêu, ước tính đóng góp → reference `03` + `du-lieu/schema-du-an.json` + script `theo_doi_du_an.py`.
3. **Phân tích số liệu sản xuất công nghiệp hằng tháng** (file theo dõi 42 nhóm sản phẩm chủ yếu): tính % kế hoạch năm, so tháng trước, so cùng kỳ, lũy kế, lọc sản phẩm hụt tiến độ → reference `04` + script `phan_tich_thang.py`.
4. **Nhận diện điểm nghẽn và đề xuất tháo gỡ** cho dự án chậm tiến độ: GPMB, quy hoạch, chủ trương đầu tư, đất đai, GPXD, môi trường, PCCC, nghĩa vụ tài chính → reference `06` + checklist `checklist-ra-soat-diem-nghen.md`.
5. **Soạn báo cáo định kỳ NQ 169** gửi Sở Tài chính trước ngày 20 của kỳ báo cáo, lồng ghép báo cáo NQ 01/NQ-CP → `mau-van-ban/01` + `05`.
6. **Xây dựng kịch bản tăng trưởng, dự báo khả năng hoàn thành**, giải trình chỉ tiêu có nguy cơ không đạt → reference `07`.
7. **Trả lời chất vấn, giải trình chênh lệch số liệu** giữa số liệu chuyên ngành của Sở và số liệu Thống kê tỉnh → reference `04` mục V + `05` mục IV.

**KHÔNG dùng plugin này** để: làm thủ tục thành lập CCN (dùng `kccn-sct-vn`), cấp phép chuyên ngành (dùng plugin lĩnh vực tương ứng), soạn định dạng file .docx (dùng `vbhc-vn`).

---

## II. QUY TRÌNH CHUẨN (bắt buộc)

- **Bước 1 — GATE SỐ LIỆU.** Chỉ tiêu **mục tiêu** (giao tại NQ 169 và Phụ lục Công văn UBND tỉnh) là số **TĨNH, đã chốt** → tra reference `02`, dùng trực tiếp.
  Số liệu **thực hiện** (sản lượng, IIP, kim ngạch, tiến độ dự án, lấp đầy, GPMB) là số **ĐỘNG** → **TUYỆT ĐỐI KHÔNG lấy từ trí nhớ và không lấy từ reference cũ**. Phải: (a) Bạn cung cấp file kỳ mới nhất, hoặc (b) đọc từ file gốc trên đĩa bằng script, hoặc (c) dừng lại và hỏi Bạn.
- **Bước 2 — Xác minh chuyên môn** tại reference tương ứng: đúng chỉ tiêu, đúng cơ quan chủ trì/phối hợp, đúng phương pháp tính, đúng kỳ báo cáo.
- **Bước 3 — Đối chiếu chéo** với plugin lĩnh vực (`kccn-sct-vn`, `qlks-sct-vn`, `quy-hoach-ct-vn`...) nếu nội dung chạm tới thủ tục hoặc quy hoạch.
- **Bước 4 — Soạn file .docx** bằng plugin `vbhc-vn` (thể thức NĐ 30/2020; ký hiệu SCT-CN; Lưu VT, CN(tên) theo lĩnh vực). Nếu có PDF văn bản đến → chạy GATE `vbhc-pdf-reader-vn` trước.
- **Bước 5 — GATE xuất file**: render soi ảnh từng trang trước khi giao.

### Bảng phân vai hệ sinh thái

| Plugin | Khi nào chuyển sang / phối hợp |
|---|---|
| `vbhc-vn` | Soạn MỌI file .docx — plugin này chỉ cấp nội dung |
| `vbhc-pdf-reader-vn` | Nhận PDF văn bản đến → đọc số/ngày/người ký từ file gốc |
| `kccn-sct-vn` | Thủ tục thành lập/mở rộng CCN, chấp thuận CTĐT KCN, tỷ lệ lấp đầy, tiến độ NQ 34-NQ/TU |
| `quy-hoach-ct-vn` | Đối chiếu dự án nguồn điện/lưới điện/mỏ với quy hoạch (QĐ 768, QĐ 866, QĐ 525) |
| `qlks-sct-vn` / `tkm-sct-vn` | Dự án khai thác, chế biến khoáng sản: sản lượng, thiết kế mỏ, đình chỉ |
| `hc-sct-vn` | Dự án hóa chất (phốt pho vàng, axit, phân bón, DAP/MAP) |
| `bvmt-sct-vn` | Chỉ tiêu 29, 30, 31 (XLNT KCN, tái sử dụng nước thải, cơ sở đạt quy chuẩn) |
| `xd-sct-vn` / `pccc-sct-vn` | Điểm nghẽn GPXD, nghiệm thu, PCCC của dự án trong KCN |
| `bpb-sct-vn` | Bài phát biểu của Lãnh đạo Sở về tăng trưởng công nghiệp |
| `sct-laocai-org-vn` | Xác định người ký, chuyên viên tham mưu, dòng Lưu VT |

---

## III. KHUNG PHÁP LÝ CỐT LÕI

Trục xương sống của công tác điều hành tăng trưởng (chi tiết reference `01`):

1. **Kết luận số 18-KL/TW của Trung ương** — định hướng mục tiêu tăng trưởng.
2. **Nghị quyết số 25/2026/QH16 của Quốc hội** — chỉ tiêu kinh tế - xã hội.
3. **Nghị quyết số 109/NQ-CP của Chính phủ**.
4. **Nghị quyết số 169/NQ-CP ngày 27/6/2026 của Chính phủ** — mục tiêu tăng trưởng của các địa phương năm 2026 và giai đoạn 2026-2030. **Đây là văn bản giao chỉ tiêu gốc.**
5. **Công văn số 7323/UBND-TH ngày 17/7/2026 của UBND tỉnh Lào Cai** — triển khai NQ 169 trên địa bàn; kèm Phụ lục phân công cơ quan chủ trì theo dõi, tổng hợp, đánh giá và báo cáo 32 chỉ tiêu. Người ký: Chủ tịch UBND tỉnh Nguyễn Tuấn Anh.
   > ✅ Số văn bản **7323** đã được đối chiếu bản gốc và xác nhận ngày 23/7/2026. (Con số 7325 xuất hiện trên trang Phụ lục của bản scan là lệch dấu đóng số, không dùng.)
6. **Nghị quyết số 01/NQ-CP** hằng năm — báo cáo NQ 169 được **lồng ghép** vào báo cáo NQ 01.
7. **Nghị quyết số 34-NQ/TU của Tỉnh ủy Lào Cai** — phát triển hạ tầng KCN/CCN, GPMB (theo dõi tại `kccn-sct-vn`).
8. **Quyết định 525/QĐ-UBND ngày 25/02/2026** — Quy hoạch tỉnh; **Quyết định 1382/QĐ-UBND ngày 23/4/2026** — Danh mục dự án thu hút đầu tư 2026-2030 (nguồn gốc của danh mục dự án tiềm năng).

---

## IV. CHỈ TIÊU SỞ CÔNG THƯƠNG CHỦ TRÌ — TRA NHANH

Bảng đầy đủ, kể cả chỉ tiêu phối hợp và các lưu ý về sai lệch giữa bản dự thảo và bản ký, xem reference `02`.

| TT | Chỉ tiêu | ĐVT | Giai đoạn 2026-2030 | Mục tiêu 2026 |
|---|---|---|---|---|
| 3 | Tốc độ tăng chỉ số sản xuất công nghiệp bình quân hằng năm (IIP) | % | >12 | 13 |
| 4 | Tỷ trọng công nghiệp chế biến, chế tạo trong GRDP | % | 13,8 | 11,8 |
| 5 | Giá trị tăng thêm ngành chế biến, chế tạo bình quân đầu người | USD | 685 | 415 |
| 6 | Tăng trưởng bình quân tổng mức bán lẻ hàng hoá và doanh thu dịch vụ tiêu dùng | % | 11,8 | 12,9 |
| 7 | Tăng trưởng giá trị kim ngạch xuất khẩu hàng hoá | % | 23 | 93,5 |
| 7c | — Nhóm nhiên liệu, khoáng sản | % | 20,11 | 18,18 |
| 8 | Tăng trưởng giá trị kim ngạch nhập khẩu hàng hoá | % | 27 | 108,3 |
| 15 | Tăng trưởng điện thương phẩm bình quân | % | >11 | 12,10 |
| 32 | Tỷ lệ doanh nghiệp công nghiệp áp dụng giải pháp sử dụng năng lượng tiết kiệm, hiệu quả | % | 62 | 50 |

**Chỉ tiêu Sở Công Thương phối hợp (không chủ trì nhưng chịu trách nhiệm cung cấp số liệu và giải pháp):** 1.2 khu vực công nghiệp và xây dựng; 9 công nghiệp văn hoá; 11 tổng vốn đầu tư toàn xã hội; 29 tỷ lệ KCN có hệ thống XLNT tập trung đạt chuẩn; 30 xử lý, tái sử dụng nước thải; 31 cơ sở SXKD đạt quy chuẩn môi trường.

---

## V. CÁC REFERENCE FILES

| File | Nội dung |
|---|---|
| `references/01-khung-phap-ly-tang-truong.md` | Chuỗi văn bản KL 18 → NQ 25/2026/QH16 → NQ 109 → NQ 169 → CV UBND tỉnh; trách nhiệm chung của sở chủ trì và sở phối hợp |
| `references/02-chi-tieu-nq169-sct.md` | **Bảng đầy đủ 32 chỉ tiêu**, tách rõ chủ trì/phối hợp; kết quả Quý I/2026 làm mốc; các sai lệch giữa bản dự thảo Excel và bản ký |
| `references/03-danh-muc-du-an-dong-luc.md` | Khung phân nhóm dự án động lực, tiêu chí xếp hạng, trường dữ liệu bắt buộc, quy tắc gắn dự án ↔ chỉ tiêu |
| `references/04-phuong-phap-tinh-va-nguon-so-lieu.md` | Cách tính IIP, giá trị sản xuất giá so sánh 2010, điện thương phẩm, kim ngạch; nguồn số liệu và cơ chế đối chiếu với Thống kê tỉnh |
| `references/05-che-do-bao-cao.md` | Kỳ báo cáo, hạn trước ngày 20, đầu mối Sở Tài chính, cấu trúc nội dung bắt buộc, cách lồng ghép NQ 01/NQ-CP |
| `references/06-diem-nghen-va-thao-go.md` | 07 nhóm điểm nghẽn điển hình của dự án công nghiệp và hướng xử lý theo thẩm quyền |
| `references/07-kich-ban-tang-truong.md` | Phương pháp dựng kịch bản tháng/quý/năm, ngưỡng cảnh báo, mẫu giải trình chỉ tiêu có nguy cơ không đạt |

## VI. CÔNG CỤ (scripts)

| Script | Công dụng |
|---|---|
| `scripts/phan_tich_thang.py` | Đọc file Excel theo dõi sản xuất công nghiệp hằng tháng (sheet `T1`..`T12`), tính % kế hoạch năm, so tháng trước, so cùng kỳ, lũy kế; xuất bảng cảnh báo sản phẩm hụt tiến độ |
| `scripts/theo_doi_du_an.py` | Quản lý sổ danh mục dự án động lực (JSON): thêm, cập nhật, lọc theo nhóm/chỉ tiêu/trạng thái, chấm điểm ưu tiên, xuất bảng đưa vào báo cáo |
| `du-lieu/schema-du-an.json` | Lược đồ trường dữ liệu chuẩn của một dự án động lực |
| `du-lieu/danh-muc-du-an.json` | Sổ dữ liệu (khởi tạo rỗng — **Bạn nạp dữ liệu thật**, plugin không tự sinh) |

## VII. BIỂU MẪU VÀ CHECKLIST

| File | Nội dung |
|---|---|
| `mau-van-ban/01-bao-cao-dinh-ky-nq169.md` | Khung báo cáo tháng/quý/năm gửi Sở Tài chính |
| `mau-van-ban/02-cong-van-don-doc-du-an.md` | Công văn đôn đốc chủ đầu tư/UBND xã đẩy nhanh tiến độ dự án |
| `mau-van-ban/03-bao-cao-giai-trinh-chi-tieu.md` | Báo cáo giải trình chỉ tiêu có nguy cơ không hoàn thành |
| `checklists/checklist-so-lieu-ky-bao-cao.md` | 12 mục kiểm tra trước khi phát hành số liệu |
| `checklists/checklist-ra-soat-diem-nghen.md` | Rà soát dự án chậm tiến độ theo 07 nhóm điểm nghẽn |

---

## VIII. NGUYÊN TẮC BẤT BIẾN CỦA PLUGIN

1. **Không bịa số liệu thực hiện.** Mọi con số về sản lượng, IIP, kim ngạch, tiến độ, lấp đầy đều phải có nguồn là file/kỳ báo cáo cụ thể do Bạn cung cấp. Không có nguồn → ghi `[chờ số liệu]` và báo Bạn.
2. **Không bịa số/ngày văn bản.** Số văn bản đóng dấu trên bản scan phải được Bạn xác nhận.
3. **Phân biệt rõ mục tiêu ↔ thực hiện ↔ dự báo.** Trong mọi bảng, ba loại số này phải nằm ở ba cột riêng, có nhãn rõ.
4. **Phân biệt rõ chủ trì ↔ phối hợp.** Sở Công Thương không tự nhận trách nhiệm chỉ tiêu do cơ quan khác chủ trì, cũng không đẩy chỉ tiêu mình chủ trì sang cơ quan phối hợp.
5. **Số liệu chuyên ngành phải khớp số liệu Thống kê tỉnh.** Có chênh lệch → phối hợp rà soát, giải trình, thống nhất **trước khi** báo cáo UBND tỉnh (khoản 5 mục II Công văn triển khai).
6. **Không dùng ký hiệu markdown** trong nội dung Bạn sẽ gửi đi/sao chép.
