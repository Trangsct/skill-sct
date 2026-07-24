---
name: xp-hc-vlncn-sct-vn
description: "Chuyên gia XỬ PHẠT VI PHẠM HÀNH CHÍNH lĩnh vực HÓA CHẤT và VẬT LIỆU NỔ CÔNG NGHIỆP (VLNCN) của Sở Công Thương Lào Cai theo Nghị định 275/2026/NĐ-CP ngày 08/7/2026 (hiệu lực 25/8/2026, THAY THẾ NĐ 71/2019 + Điều 1 NĐ 17/2022). Dùng khi: (1) tra cứu hành vi - mức phạt - hình thức bổ sung - biện pháp khắc phục (hóa chất Đ7-52; VLNCN Đ53-61: trách nhiệm, nhân lực - huấn luyện, giấy phép, sản xuất, bảo quản kho, vận chuyển, kinh doanh, sử dụng - hộ chiếu nổ mìn - dịch vụ nổ mìn, tiêu hủy); (2) xác định thẩm quyền xử phạt Đ62-73 (Chủ tịch UBND xã/tỉnh, Giám đốc SCT phạt đến 40/80 triệu, thanh tra, công an, QLTT); (3) chọn nghị định đúng theo thời điểm hành vi (chuyển tiếp Đ74 - mốc 25/8/2026); (4) đối chiếu điều khoản NĐ 71/2019 cũ sang NĐ 275/2026; (5) soạn biên bản VPHC, QĐ xử phạt. Từ khóa: xử phạt VPHC, NĐ 275/2026, mức phạt, tước giấy phép, đình chỉ hoạt động, biên bản VPHC, QĐ-XPHC, thẩm quyền xử phạt, chuyển hồ sơ hình sự, Điều 305 BLHS, để mất VLNCN, nổ mìn không phép, kho không đạt QCVN."
---

# xp-hc-vlncn-sct-vn — Xử phạt VPHC hóa chất & VLNCN theo NĐ 275/2026/NĐ-CP (Sở Công Thương Lào Cai)

## I. KHI NÀO DÙNG SKILL NÀY

Kích hoạt khi xử lý bất kỳ việc nào sau:

- **Tra cứu hành vi – mức phạt** để lập biên bản VPHC, soạn QĐ xử phạt, trả lời doanh nghiệp, đưa "số liệu răn đe" vào công văn đôn đốc:
  - Hóa chất (Đ7–52) → reference `03`;
  - VLNCN, tiền chất thuốc nổ (Đ53–61) → reference `02`.
- **Xác định thẩm quyền**: ai được phạt đến bao nhiêu, ai được tước GP/đình chỉ, trong thẩm quyền Sở hay phải trình Chủ tịch UBND tỉnh → reference `04`.
- **Chọn đúng nghị định theo thời điểm hành vi** (trước/sau mốc hiệu lực 25/8/2026; điều khoản chuyển tiếp Đ74) → mục IV dưới đây + reference `01`.
- **Đối chiếu điều khoản cũ → mới** khi hồ sơ, biên bản, kế hoạch kiểm tra trước đây viện dẫn NĐ 71/2019/NĐ-CP → reference `05`.
- **Soạn văn bản xử phạt** của Sở: biên bản VPHC, QĐ xử phạt /QĐ-XPHC, tờ trình + dự thảo QĐ trình Chủ tịch UBND tỉnh khi vượt thẩm quyền → mục VI + tiền lệ trong `sd-vlncn-sct-vn`.

**Ranh giới, liên kết với plugin khác:**
- Nghiệp vụ chuyên ngành (điều kiện, giấy phép, quy trình, kiểm tra chuyên ngành NĐ 217/2025): giấy phép sử dụng VLNCN + PANM → `sd-vlncn-sct-vn`; kho VLNCN → `kho-vlncn-sct-vn`; huấn luyện KTAT → `hl-vlncn-sct-vn`; quản lý hóa chất → `hc-sct-vn`. Plugin này CHỈ lo phần chế tài.
- Vận chuyển VLNCN: Công an cấp phép và chủ trì xử lý phần lớn (Đ58, Đ65); Sở nắm để phối hợp.
- Soạn văn bản: `vbhc-vn` (thể thức NĐ 30/2020), `sct-laocai-org-vn` (người ký, dòng Lưu), `vbhc-pdf-reader-vn`/GATE khi đọc PDF đến.

## II. VĂN BẢN LÕI (đã đối chiếu bản gốc trong `van-ban-goc/`)

TUYỆT ĐỐI không tự thay số/ngày khác.

1. **Nghị định số 275/2026/NĐ-CP ngày 08/7/2026** của Chính phủ quy định xử phạt vi phạm hành chính trong lĩnh vực hóa chất và vật liệu nổ công nghiệp — **hiệu lực từ 25/8/2026** (Đ75). Từ ngày này, **NĐ 71/2019/NĐ-CP và Điều 1 NĐ 17/2022/NĐ-CP hết hiệu lực**. Căn cứ ban hành gồm: Luật Tổ chức Chính phủ 63/2025; Luật Tổ chức CQĐP 72/2025; Luật XLVPHC 15/2012 (sđ Luật 67/2020, Luật 88/2025); **Luật Hóa chất 69/2025**; Luật Phòng, chống ma túy 120/2025; **Luật 42/2024** (vũ khí, VLN, CCHT). Người ký: KT. Thủ tướng, Phó Thủ tướng Phạm Gia Túc.
2. **NĐ 71/2019/NĐ-CP (sđ NĐ 17/2022)** — chỉ còn dùng cho hành vi xảy ra và kết thúc **trước 25/8/2026** (k1 Đ74 NĐ 275/2026) và giải quyết khiếu nại QĐ đã ban hành (k4 Đ74). Bản gốc: `sd-vlncn-sct-vn/van-ban-goc/` và `hc-sct-vn/van-ban-goc/05-xu-phat-kiem-tra/`.
3. **Nền thủ tục:** Luật XLVPHC (thời hiệu, thời hạn ra QĐ, cưỡng chế; bản sửa đổi 2025 hiệu lực 01/7/2025); NĐ 118/2021/NĐ-CP (sđ NĐ 68/2025, NĐ 190/2025 — xử phạt trên môi trường điện tử, k5 Đ5 NĐ 275/2026); NĐ 189/2025 (thẩm quyền xử phạt); kiểm tra chuyên ngành theo NĐ 217/2025 + TT 56/2025/TT-BCT (quy trình → `hc-sct-vn` ref 10, `sd-vlncn-sct-vn` ref 05 mục F).

## III. CẤU TRÚC NĐ 275/2026 — BẢN ĐỒ TRA CỨU NHANH

| Phần | Điều | Nội dung |
|---|---|---|
| Chương I | 1–6 | Phạm vi; đối tượng; hình thức phạt + khắc phục hậu quả (Đ3); **mức phạt cá nhân/tổ chức (Đ4)**; vi phạm nhiều lần, môi trường điện tử (Đ5); ranh giới hình sự (Đ6) |
| Ch. II Mục 1–6 | 7–52 | HÓA CHẤT: phát triển CN hóa chất (7–14); quản lý hoạt động (15–28); hóa chất nguy hiểm trong sản phẩm (29–30); an toàn (31–37, **Đ34 huấn luyện**); hóa chất Bảng (38–41); chế phẩm diệt côn trùng, diệt khuẩn (42–52) |
| Ch. II Mục 7 | 53–61 | VLNCN + TCTN: **53** trách nhiệm; **54** nhân lực; **55** quản lý GP/GCN; **56** nghiên cứu, thử nghiệm, sản xuất; **57** bảo quản (kho); **58** vận chuyển; **59** kinh doanh; **60** sử dụng + dịch vụ nổ mìn; **61** kiểm tra, thử, tiêu hủy |
| Chương III | 62–73 | Thẩm quyền: Chủ tịch UBND các cấp (62); **thủ trưởng chuyên ngành — GĐ SCT (63)**; thanh tra (64); Công an (65); Hải quan (66); Kiểm ngư (67); Kiểm lâm (68); QLTT (69); Biên phòng (70); Cảnh sát biển (71); **phân định (72)**; lập biên bản (73) |
| Chương IV | 74–76 | **Chuyển tiếp (74)**; hiệu lực 25/8/2026 (75); trách nhiệm thi hành (76) |

**Mức phạt (Đ4) — quy tắc nền của mọi tra cứu:**
- Mức tối đa/hành vi với CÁ NHÂN: hóa chất **50 triệu đ**; VLNCN **100 triệu đ**.
- Mức ghi tại Chương II là mức **CÁ NHÂN** (trừ Đ9, Đ11, Đ13); **TỔ CHỨC ×2**.
- Mức theo thẩm quyền Chương III cũng là mức cá nhân; với tổ chức ×2 (xác định thẩm quyền phải tính theo mức ĐÃ ×2 của tổ chức).

## IV. CHỌN NGHỊ ĐỊNH THEO THỜI ĐIỂM HÀNH VI (Đ74 — mốc 25/8/2026)

```
Hành vi xảy ra VÀ kết thúc TRƯỚC 25/8/2026
  (kể cả phát hiện sau, đang xem xét)          → NĐ 71/2019 (sđ NĐ 17/2022)
Hành vi bắt đầu trước, VẪN ĐANG DIỄN RA
  khi NĐ 275/2026 đã có hiệu lực               → NĐ 275/2026 (trừ k2 Đ74 - nhóm hóa chất đặc thù)
Hành vi xảy ra TỪ 25/8/2026                    → NĐ 275/2026
QĐ xử phạt đã ban hành/thi hành xong
  trước 25/8/2026 mà còn khiếu nại             → áp dụng quy định tại thời điểm ban hành QĐ (k4 Đ74)
```

- Xác định "đã kết thúc"/"đang thực hiện" theo pháp luật XLVPHC (k2 Đ5 NĐ 275/2026). Hành vi dạng "không thực hiện nghĩa vụ" (không báo cáo, không lưu hồ sơ, kho không đạt chuẩn đang tiếp diễn) thường là hành vi đang thực hiện → dễ rơi vào NĐ 275/2026 sau 25/8/2026.
- k2, k3 Đ74: một số hành vi HÓA CHẤT theo điều khoản cũ (Đ16, Đ17, Đ18, Đ31, điểm b k2 Đ37, điểm c k2 Đ40, điểm c k3 Đ46 NĐ 71/2019) xảy ra sau hiệu lực mà NĐ mới không quy định → áp dụng điều khoản tương ứng NĐ 275/2026 như bảng dẫn chiếu tại reference `01`.
- **Câu viện dẫn chuẩn trong QĐ xử phạt từ 25/8/2026:** *"Nghị định số 275/2026/NĐ-CP ngày 08 tháng 7 năm 2026 của Chính phủ quy định xử phạt vi phạm hành chính trong lĩnh vực hóa chất và vật liệu nổ công nghiệp"* — hành vi ghi nguyên văn theo đúng điểm-khoản-điều.

## V. THẨM QUYỀN — PHÂN ĐỊNH NHANH (chi tiết reference `04`)

| Chức danh | Hóa chất (cá nhân) | VLNCN (cá nhân) | Bổ sung |
|---|---|---|---|
| Chủ tịch UBND cấp xã (Đ62 k1) | đến 25 tr | đến 50 tr | tịch thu; đình chỉ/tước quyền có thời hạn; khắc phục hậu quả |
| Chủ tịch UBND cấp tỉnh (Đ62 k2) | đến 50 tr (kịch khung) | đến 100 tr (kịch khung) | đủ mọi hình thức |
| **Giám đốc Sở Công Thương (Đ63 k1)** | **đến 40 tr** | **đến 80 tr** | tịch thu; đình chỉ/tước quyền theo lĩnh vực phụ trách; khắc phục hậu quả |
| Cục trưởng Cục Hóa chất / Cục KTAT&MTCN (Đ63 k2) | đến 50 tr | đến 100 tr | đủ mọi hình thức |
| Công an, QLTT, Hải quan, Biên phòng, CSB, thanh tra | theo Đ64–71 | theo Đ64–71 | phân định hành vi tại Đ72 |

**Điểm mới quan trọng cho Sở:** NĐ 275/2026 quy định **đích danh Giám đốc Sở Công Thương** có thẩm quyền xử phạt (Đ63 k1, phân định tại điểm a k2 Đ72) — hết vướng mắc chức danh sau khi bỏ Thanh tra Sở (Luật Thanh tra 84/2025). Với tổ chức, GĐ SCT phạt được đến 80 tr (hóa chất) / 160 tr (VLNCN) tính theo mức ×2; vượt mức hoặc cần hình thức ngoài phạm vi → trình Chủ tịch UBND tỉnh.

## VI. QUY TRÌNH XỬ PHẠT CỦA SỞ (khi phát hiện vi phạm qua kiểm tra)

```
1. Lập BIÊN BẢN VPHC ngay khi phát hiện (Đ73: thành viên đoàn kiểm tra, công chức
   đang thi hành nhiệm vụ) — mô tả hành vi đúng cấu thành điểm-khoản-điều NĐ 275/2026;
   chứng cứ kèm theo (hộ chiếu nổ mìn, sổ sách, ảnh, kết quả đo)
2. Kiểm tra thời điểm hành vi → chọn nghị định theo mục IV (Đ74)
3. Xác minh tình tiết; tính thời hạn ra QĐ theo Luật XLVPHC (sđ 2025)
4. Xác định thẩm quyền theo TỔNG mức phạt của tổ chức (×2) + hình thức bổ sung:
   - Trong thẩm quyền GĐ Sở (Đ63 k1) → QĐ /QĐ-XPHC của Sở
   - Vượt/thuộc lực lượng khác → tờ trình + dự thảo QĐ trình Chủ tịch UBND tỉnh,
     hoặc chuyển hồ sơ đúng lực lượng (Đ72; hành vi có dấu hiệu tội phạm → Đ6)
5. QĐ xử phạt: mức tiền từng hành vi; hình thức bổ sung (tước GP/đình chỉ — ghi rõ
   số GP, thời hạn); biện pháp khắc phục; thời hạn, nơi nộp phạt; có thể thực hiện
   trên môi trường điện tử (k5 Đ5)
6. Theo dõi thi hành; giám sát trong thời gian tước GP/đình chỉ; cưỡng chế nếu không
   chấp hành; cập nhật CSDL; tổng hợp vào báo cáo định kỳ
```

**Ranh giới hình sự (Đ6):** phát hiện hành vi tại k3, k4 Đ55; k6 Đ58; k4, k5 Đ59; k5, điểm b, d k6 Đ60 → **chuyển hồ sơ cơ quan tố tụng** trước; chỉ xử phạt hành chính khi có quyết định không khởi tố/đình chỉ mà vẫn có dấu hiệu VPHC. Sử dụng, mua bán, tàng trữ, vận chuyển trái phép VLNCN → đối chiếu Điều 305 BLHS, không "hành chính hóa".

## VII. QUY TẮC LÀM VIỆC

1. Trả lời/soạn thảo tiếng Việt, văn phong hành chính; docx theo `vbhc-vn`, render kiểm tra trước khi giao.
2. Mức phạt luôn nêu kèm chú thích "cá nhân/tổ chức"; khi tư vấn cho DN mặc định nêu mức TỔ CHỨC (×2).
3. Trước khi viện dẫn: xác định thời điểm hành vi (mục IV). Văn bản soạn trước 25/8/2026 về hành vi đang diễn ra cần câu điều kiện chuyển tiếp.
4. Không tự điền số/ngày văn bản chưa ban hành; số QĐ để trống "Số:      /QĐ-XPHC".
5. Số liệu vụ việc, tiền lệ của Sở: lấy từ plugin nghiệp vụ tương ứng (`sd-`, `hl-`, `kho-`, `hc-`), không bịa.

## VIII. CẤU TRÚC PLUGIN

```
xp-hc-vlncn-sct-vn/
├── SKILL.md                              ← file này
├── CHANGELOG.md
├── references/
│   ├── 01-quy-dinh-chung-chuyen-tiep.md  ← phạm vi, hình thức phạt Đ3, mức phạt Đ4,
│   │                                        nhiều lần Đ5, hình sự Đ6, chuyển tiếp Đ74
│   ├── 02-hanh-vi-vlncn.md               ← bảng hành vi - mức phạt Đ53-61 (đầy đủ)
│   ├── 03-hanh-vi-hoa-chat.md            ← bản đồ Đ7-52 + chi tiết các điều Sở hay dùng
│   ├── 04-tham-quyen.md                  ← Đ62-73 + phân định Đ72 + ví dụ tính thẩm quyền
│   └── 05-doi-chieu-nd71-2019.md         ← bảng đối chiếu điều khoản cũ → mới
└── van-ban-goc/
    ├── ND-275-2026-NDCP-xu-phat-VPHC-hoa-chat-VLNCN.docx  ← toàn văn (bản Word)
    └── INDEX.md
```
