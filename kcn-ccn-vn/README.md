# Skill kcn-ccn-vn - Hướng dẫn sử dụng

## Giới thiệu

Đây là skill chuyên môn về quản lý nhà nước Khu công nghiệp (KCN) và Cụm công nghiệp (CCN) tỉnh Lào Cai, dành riêng cho công chức Sở Công Thương. Skill giúp Claude trả lời chính xác hơn các câu hỏi nghiệp vụ, tham chiếu đúng văn bản pháp luật, áp dụng đúng quy trình thẩm định và soạn văn bản chuyên ngành.

## Phạm vi nội dung

Skill tập trung vào **CCN** (do Sở Công Thương trực tiếp tham mưu); **KCN** chỉ tóm lược các nội dung cần thiết để phối hợp với Ban Quản lý Khu kinh tế.

### Khung pháp lý được tích hợp

- Nghị định số 32/2024/NĐ-CP về CCN (trích nguyên văn các điều then chốt: Đ.2, Đ.8, Đ.9, Đ.10, Đ.13, Đ.23, Đ.36-37);
- Nghị định số 35/2022/NĐ-CP về KCN, KKT (tóm lược);
- Nghị định số 139/2025/NĐ-CP về phân quyền 02 cấp Bộ Công Thương;
- Quyết định số 16/2026/QĐ-UBND - Quy chế quản lý CCN tỉnh Lào Cai;
- Nghị quyết số 34-NQ/TU và Kế hoạch số 134/KH-UBND của tỉnh;
- Quyết định số 525/QĐ-UBND - Điều chỉnh Quy hoạch tỉnh 2021-2030;
- Quyết định số 425/QĐ-BXD - Suất vốn đầu tư năm 2025.

### Dữ liệu thực tiễn được tích hợp

- 07 KCN và 23 CCN đã thành lập trên địa bàn (tổng 3.042,67 ha);
- Quy hoạch đến 2030: 20 KCN (5.797 ha) + 54 CCN (2.928 ha);
- Tầm nhìn 2050: 22 KCN (8.078 ha) + 62 CCN (3.779 ha);
- Danh mục 14 KCN + 35 CCN trong danh mục thu hút đầu tư 2026-2030 (~45.300 tỷ đồng);
- Case studies thực tế: CCN Bảo Minh, An Thịnh, Bản Phung, Y Can, Thống Nhất 1, Đông An.

## Cấu trúc skill

```
kcn-ccn-vn/
├── SKILL.md                                    (router chính)
├── references/
│   ├── 01-luat-ccn-nd32.md                     (NĐ 32/2024 các điều trọng yếu)
│   ├── 02-luat-kcn-nd35.md                     (NĐ 35/2022 tóm lược)
│   ├── 03-quy-trinh-thanh-lap-ccn.md           (Quy trình 4 bước)
│   ├── 04-cham-diem-chu-dau-tu.md              (Hội đồng đánh giá thang 100)
│   ├── 05-mau-bao-cao-dau-tu.md                (Cấu trúc Báo cáo đầu tư 9 phần)
│   ├── 06-mo-hinh-2-cap-lao-cai.md             (Áp dụng NĐ 139/2025)
│   ├── 07-fdi-chu-dau-tu-ccn.md                (Vướng mắc FDI làm chủ đầu tư CCN)
│   ├── 08-xu-ly-ccn-truoc-2009.md              (Đ.36-37 NĐ 32, hạn 31/12/2026)
│   ├── 09-dieu-kien-khoi-cong.md               (Đ.107 Luật XD; miễn GPXD CCN)
│   ├── 10-quy-che-ccn-lao-cai.md               (QĐ 16/2026/QĐ-UBND)
│   ├── 11-nq34-kh134.md                        (NQ 34 và KH 134)
│   ├── 12-danh-muc-kcn-ccn-lao-cai.md          (Khung quy hoạch tổng thể theo QĐ 525)
│   ├── 13-suat-von-dau-tu.md                   (QĐ 425/QĐ-BXD)
│   ├── 14-nq26-nhiem-vu-2026.md                (NQ 26-NQ/TU nhiệm vụ 2026)
│   ├── 15-hien-trang-ccn-bao-cao-18-6-2026.md  (Hiện trạng 23 CCN - nguồn mới nhất)
│   └── 16-qd1382-danh-muc-thu-hut.md           (Danh mục thu hút đầu tư QĐ 1382)
└── checklists/
    ├── checklist-tham-dinh-ho-so-ccn.md        (11 mục rà soát hồ sơ)
    ├── checklist-cham-diem-cdt.md              (Chuẩn bị Hội đồng chấm điểm)
    └── checklist-khoi-cong.md                  (06 điều kiện Đ.107 Luật XD)
```

## Cách cài đặt

### Cách 1: Cài qua Claude.ai (sau khi Anthropic ra mắt tính năng public skills)

Hiện tại Anthropic đang triển khai tính năng skill cho Claude.ai. Khi có sẵn:
1. Vào Settings → Skills;
2. Upload file kcn-ccn-vn.zip;
3. Skill sẽ tự động kích hoạt khi gặp các từ khoá liên quan.

### Cách 2: Cài qua Claude API (developers)

Skill tuân theo định dạng của hệ thống skill Anthropic. Có thể tích hợp vào ứng dụng tự xây dựng qua Claude API.

### Cách 3: Sử dụng tham chiếu thủ công (hiện tại)

Trong khi chờ tính năng skill chính thức, có thể:
1. Lưu thư mục skill này vào máy;
2. Khi cần chuyên môn, paste nội dung file SKILL.md vào đầu cuộc trò chuyện;
3. Khi cần đào sâu, paste thêm reference cụ thể.

## Cách sử dụng

Khi Claude đã được cài đặt skill, chỉ cần đặt câu hỏi/yêu cầu bình thường. Skill sẽ tự động kích hoạt khi gặp các từ khoá:

- "cụm công nghiệp", "khu công nghiệp", "CCN", "KCN";
- "Nghị định 32/2024", "Nghị định 35/2022";
- "thẩm định", "chấm điểm chủ đầu tư", "Hội đồng đánh giá";
- "Bảo Minh", "An Thịnh", "Bản Phung", "Tằng Loỏng", "Bản Qua"...;
- "Quy chế CCN Lào Cai", "Nghị quyết 34", "Kế hoạch 134";
- "khởi công", "GPMB", "lấp đầy", "suất vốn đầu tư";
- "thành lập CCN", "mở rộng CCN", "điều chỉnh CCN";
- ...

### Ví dụ câu hỏi/yêu cầu Claude xử lý tốt:

1. "Thẩm định hồ sơ thành lập CCN Tân Nguyên 60 ha, nhà đầu tư là [...]"
2. "Soạn Tờ trình UBND tỉnh thành lập Hội đồng đánh giá lựa chọn chủ đầu tư CCN Bảo Hưng 2"
3. "CCN Đông An đã có quy hoạch chi tiết 2010 nhưng chưa có QĐ thành lập, xử lý ra sao?"
4. "Phân tích các điều kiện khởi công công trình hạ tầng CCN Y Can"
5. "Soạn báo cáo gửi UBND tỉnh về tình hình triển khai NQ 34 Quý II/2026"
6. "Tính khái toán suất vốn cho KCN [...] quy mô 250 ha"
7. "Hướng dẫn UBND xã [...] về 8 nhóm nhiệm vụ trong Quy chế CCN Lào Cai"

## Phối hợp với skill vbhc-vn

Skill này tập trung vào nội dung CHUYÊN MÔN. Khi cần tạo file Word (.docx) văn bản hành chính (công văn, tờ trình, báo cáo, kế hoạch), Claude sẽ phối hợp tự động với skill `vbhc-vn`:

- **Skill kcn-ccn-vn**: Cung cấp nội dung chuyên môn (căn cứ pháp lý, số liệu, cấu trúc Báo cáo);
- **Skill vbhc-vn**: Tạo file .docx theo đúng mẫu Sở Công Thương (header, font Times New Roman 14pt, lề 30/20mm, ký hiệu SCT-CN, người ký mặc định...).

## Lưu ý quan trọng

1. **Số liệu cập nhật đến tháng 5/2026**. Các số liệu về tỷ lệ lấp đầy, tiến độ GPMB, kết quả Quý gần nhất có thể đã thay đổi. Khi cần độ chính xác cao, đề nghị kiểm tra lại với Phòng Quản lý Công nghiệp.

2. **Văn bản pháp luật có thể được sửa đổi**. Đặc biệt:
   - NĐ 32/2024 đang được Bộ Công Thương dự thảo sửa đổi;
   - NĐ 35/2022 đang được Bộ Tài chính dự thảo nghị định thay thế;
   - Luật Đầu tư 2020 sẽ được thay thế bởi Luật Đầu tư 2025;
   - Quy định chuyển tiếp 02 cấp theo NĐ 139/2025 hết hiệu lực 28/02/2027.
   
   Trước khi áp dụng vào văn bản hành chính, đối chiếu với hiệu lực hiện hành.

3. **Dữ liệu địa giới hành chính** áp dụng từ 01/7/2025 theo NQ 202/2025/QH15 sáp nhập tỉnh Lào Cai và Yên Bái.

4. **Phân biệt giữa "Quy chế CCN tỉnh" và "NĐ 32/2024"**. Quy chế tỉnh có thể có nội dung chi tiết hơn hoặc khác với NĐ 32. Khi áp dụng cho CCN trên địa bàn Lào Cai, ưu tiên Quy chế tỉnh; khi không có quy định trong Quy chế tỉnh, áp dụng NĐ 32.

## Liên hệ và phản hồi

Skill được xây dựng nội bộ cho Sở Công Thương tỉnh Lào Cai. Khi phát hiện thông tin chưa chính xác, cần cập nhật, hoặc muốn bổ sung nội dung mới, có thể yêu cầu Claude chỉnh sửa skill trực tiếp.

---

*Phiên bản 1.0 - Tháng 5/2026*

*Tác giả: Sở Công Thương tỉnh Lào Cai (xây dựng cùng Claude AI)*
