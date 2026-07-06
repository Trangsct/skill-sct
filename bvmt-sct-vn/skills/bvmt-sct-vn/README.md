# Skill bvmt-sct-vn — Hướng dẫn sử dụng

## Giới thiệu

Đây là skill chuyên môn về **quản lý nhà nước lĩnh vực Bảo vệ môi trường (BVMT) ngành Công Thương**, dành cho công chức Sở Công Thương tỉnh Lào Cai. Skill giúp Claude xác định **đúng vai trò** của Sở Công Thương trong công tác BVMT (chủ yếu là **phối hợp**, không chủ trì), tham chiếu đúng văn bản pháp luật còn hiệu lực, tránh các lỗi nghiệp vụ phổ biến, và soạn văn bản chuyên ngành chuẩn thể thức.

## Vấn đề cốt lõi skill giải quyết

Đây là điểm **dễ sai nhất** và là lý do skill tồn tại:

> **Sở Công Thương KHÔNG phải cơ quan chủ trì BVMT.** Cơ quan chủ trì là **Sở Nông nghiệp và Môi trường** (sau hợp nhất 2025). Sở Công Thương **không** phê duyệt ĐTM, **không** cấp Giấy phép môi trường, **không** tiếp nhận đăng ký môi trường. Sở Công Thương **phối hợp/tham gia ý kiến** theo điểm a khoản 2 Điều 160 Luật BVMT 2020, và **chủ trì** một số mảng ngành: công nghiệp môi trường – kinh tế tuần hoàn, kiểm kê/giảm nhẹ phát thải khí nhà kính (KNK) ngành Công Thương, an toàn hóa chất.

Lỗi thường gặp nếu thiếu skill: gán cho Sở Công Thương thẩm quyền phê duyệt/cấp phép môi trường; viện dẫn **Thông tư 35/2015/TT-BCT** như đang còn hiệu lực (thực tế **đã hết hiệu lực, chưa có văn bản thay thế**).

## Phạm vi nội dung

### Khung pháp lý được tích hợp (đã xác minh số/ngày)

- **Luật Bảo vệ môi trường số 72/2020/QH14** — đặc biệt Điều 160 (trách nhiệm Bộ Công Thương);
- **NĐ 08/2022/NĐ-CP**, **NĐ 05/2025/NĐ-CP** (sửa NĐ 08), **NĐ 48/2026/NĐ-CP** — hướng dẫn Luật BVMT;
- **NĐ 45/2022/NĐ-CP** — xử phạt VPHC lĩnh vực môi trường (hiện hành; đang có dự thảo sửa đổi, chưa ban hành);
- **NĐ 06/2022/NĐ-CP** và **NĐ 119/2025/NĐ-CP** — giảm nhẹ phát thải KNK, bảo vệ tầng ô-dôn;
- **TT 38/2023/TT-BCT** — MRV khí nhà kính ngành Công Thương (Sở Công Thương chủ trì phần ngành);
- **QĐ 11/2025/QĐ-TTg** — Quy chế ứng phó sự cố chất thải;
- Các văn bản CTR, BĐKH, cải cách TTHC (NQ 66.19/2026)...

### Dữ liệu/bối cảnh thực tiễn Lào Cai được tích hợp

- **Chỉ thị 26-CT/TU ngày 12/5/2026** của BTV Tỉnh ủy (đã xác minh số/ngày) — BVMT khai khoáng và dự án lớn trong KCN/CCN;
- **Đề án số 13** ban hành kèm **NQ 35-NQ/TU ngày 29/12/2025** (xác minh qua Chỉ thị 26) — tài nguyên, môi trường, phát triển bền vững 2026–2030;
- **Bãi thải gyps** và **rủi ro sự cố hóa chất** tại KCN Tằng Loỏng;
- Hệ thống xử lý nước thải tập trung KCN phía Nam, Âu Lâu, Minh Quân;
- Bộ mẫu câu/đoạn văn thực tế và FAQ cho công việc hằng ngày.

## Cấu trúc skill

```
bvmt-sct-vn/
├── SKILL.md                          (router chính — đọc trước)
├── README.md                         (file này)
└── references/
    ├── 01-vai-tro-sct-bvmt.md        (Ranh giới vai trò SCT ↔ Sở NN&MT; Điều 160; 8 nhóm nhiệm vụ; ai soạn/ký) — ĐỌC ĐẦU TIÊN
    ├── 02-khung-phap-ly.md           (Toàn bộ số/ngày văn bản đã xác minh + bảng hiệu lực/dự thảo)
    ├── 03-dtm-gpmt.md                (Tra cứu đầy đủ ĐTM/GPMT/đăng ký MT đến NĐ 48/2026: phân loại nhóm I-IV, bảng quyết định, ngưỡng, trình tự - thời điểm, thẩm quyền, bảng tra dự án Lào Cai, checklist phản biện)
    ├── 04-bvmt-kcn-ccn-mo.md         (BVMT khu/cụm công nghiệp + đóng cửa mỏ, cải tạo phục hồi môi trường)
    ├── 05-knk-carbon-bdkh.md         (Kiểm kê/giảm nhẹ KNK, MRV, thị trường các-bon, BĐKH ngành CT)
    ├── 06-su-co-xu-phat-cai-cach.md  (Ứng phó sự cố chất thải/hóa chất; xử phạt VPHC; cải cách TTHC)
    └── 07-boi-canh-lao-cai.md        (Chỉ thị 26-CT/TU; Đề án 13/NQ 35; gyps Tằng Loỏng; bộ mẫu công việc + FAQ)
```

## Nguyên tắc bất biến (anti-error)

1. Ngôn ngữ **"phối hợp"** cho phần BVMT chung; chỉ dùng "chủ trì" cho 3 mảng đúng vai (công nghiệp môi trường, KNK, an toàn hóa chất).
2. Cơ quan chủ trì BVMT = **Sở Nông nghiệp và Môi trường**; bộ chủ quản = **Bộ Nông nghiệp và Môi trường**.
3. **Không bịa số/ngày** văn bản pháp luật — chỉ dùng số đã xác minh ở `references/02-khung-phap-ly.md`; thiếu thì ghi "[đề nghị Bạn xác minh]".
4. **TT 35/2015/TT-BCT đã hết hiệu lực** — không viện dẫn như còn hiệu lực; kiến nghị Bộ Công Thương ban hành VBQPPL thay thế.
5. Tổ chức Lào Cai mới (từ 01/7/2025, không còn cấp huyện); địa danh Yên Bái cũ ghi "tỉnh Lào Cai".

## Tổ chức & người ký (mặc định)

- **Chuyên viên tham mưu:** CN(M.Long) — Lê Minh Long (môi trường/KNK/các-bon/công nghiệp môi trường). Dòng lưu: **Lưu: VT, CN(M.Long)**.
- **Người ký:** KT.GĐ – PGĐ **Hoàng Văn Thuân** (môi trường, khoáng sản, hóa chất); văn bản cấp tỉnh: GĐ **Hoàng Chí Hiền**.
- **Ký hiệu:** SCT-CN.

## Cách cài đặt

1. Đóng gói skill thành file `.skill` (đã thực hiện kèm theo).
2. Tải lên qua giao diện quản lý skills của Claude (Settings → Capabilities → Skills), hoặc giải nén vào thư mục skills của môi trường đang dùng.
3. Skill tự kích hoạt khi câu hỏi liên quan BVMT ngành Công Thương (tham gia ý kiến ĐTM, đóng cửa mỏ, gyps, KNK, sự cố hóa chất, Chỉ thị 26-CT/TU...).

## Lưu ý cập nhật

- Khi **Nghị định sửa đổi NĐ 45/2022** được ban hành chính thức → cập nhật `references/02` và `06`.
- Khi **Bộ Công Thương ban hành VBQPPL thay thế TT 35/2015** → cập nhật `references/01`, `02` và SKILL.md.
- Số/ngày các văn bản dự thảo phải xác minh lại trước khi viện dẫn vào văn bản chính thức.
