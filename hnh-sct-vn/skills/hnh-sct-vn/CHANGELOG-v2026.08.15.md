# CHANGELOG v2026.08.15 - Tích hợp QĐ 2848/QĐ-UBND ngày 14/8/2026 sửa đổi, bổ sung QĐ 1696/QĐ-UBND

Nguồn: bản PDF đã ký "Quyết định số **2848/QĐ-UBND ngày 14/8/2026** của UBND tỉnh Lào Cai sửa đổi, bổ sung một số nội dung của Quyết định số 1696/QĐ-UBND" (đã tiếp thu ý kiến Thành viên UBND tỉnh; theo Tờ trình 4173/TTr-SCT ngày 14/7/2026; TM. UBND - Chủ tịch Nguyễn Tuấn Anh ký, dấu đỏ), Bạn cung cấp 15/8/2026.

## Nội dung văn bản đã tích hợp

1. **Thay toàn bộ Mục I (Lĩnh vực vận chuyển HHNH) Phụ lục QĐ 1696** bằng Phụ lục mới - ủy quyền Giám đốc Sở Công Thương trọn gói cấp/cấp điều chỉnh/cấp lại/thu hồi Giấy phép:
   - **Loại 5, 8** (MỚI - giai đoạn 29/5-13/8/2026 chưa ủy quyền, Sở phải trình UBND tỉnh ký): căn cứ khoản 1 Điều 8 TT 38/2025 (sửa bởi Điều 25 TT 26/2026); mã TTHC **1.013340 / 1.013350 / 1.013351**.
   - Loại 1 (trừ VLNCN/TCTN), 2, 3, 4, 9: căn cứ khoản 2 Điều 8 (căn cứ được dẫn LẠI theo TT 26/2026, hết tình trạng Phụ lục cũ dẫn TT 15/2026); mã 1.014967/68/69.
2. **Thay Điều 2 QĐ 1696 (thời hạn ủy quyền):** HHNH đến hết **31/12/2030**; ATVSLĐ đến hết 28/02/2027; chấm dứt trước hạn khi văn bản căn cứ bị sửa đổi/thay thế làm thay đổi thẩm quyền/nội dung ủy quyền.
3. Hiệu lực từ ngày ký **14/8/2026**; nội dung khác của QĐ 1696 giữ nguyên.
4. Căn cứ mới ghi nhận: **QĐ 1213/QĐ-BCT ngày 22/5/2026** (công bố TTHC sửa đổi, bổ sung, bãi bỏ - bản công bố SAU TT 26/2026); QĐ 1522/QĐ-UBND ngày 04/5/2026 (Quy chế làm việc UBND tỉnh 2026-2031); QĐ 05/2025/QĐ-UBND.

## Hệ quả nghiệp vụ từ 14/8/2026

- Giám đốc Sở ký Giấy phép theo ủy quyền cho **cả 7 loại** (1 trừ VLNCN/TCTN, 2, 3, 4, 5, 8, 9) - loại 5, 8 KHÔNG còn trình UBND tỉnh. Hồ sơ loại 5, 8 tiếp nhận 29/5-13/8/2026 xử lý theo mô hình trình ký cũ.
- Căn cứ ủy quyền trong văn bản: "Quyết định số 1696/QĐ-UBND ngày 15/5/2026... (được sửa đổi, bổ sung tại Quyết định số 2848/QĐ-UBND ngày 14/8/2026...)". Hồ sơ loại 5, 8 dẫn **khoản 1** Điều 8 (không phải khoản 2).
- Mã TTHC 2 bộ riêng: loại 5,8 → 1.013340/50/51; loại 1,2,3,4,9 → 1.014967/68/69 - không dùng lẫn.

## Bài học kỹ thuật đọc PDF ký số (bổ sung nguyên tắc VII.10 SKILL.md)

Số/ngày văn bản điền qua **trường ký số** (widget) không hiện liền mạch trong lớp text của PDF - trích text thô sẽ thấy "2848", "14" rời rạc và dễ kết luận nhầm "số/ngày để trống". Phải **render trang thành ảnh** để đọc (đúng quy trình skill `vbhc-pdf-reader-vn`). Phiên 15/8/2026 đã mắc lỗi này ở lần đọc đầu, sửa ngay trong cùng phiên.

## Các file đã sửa

- **SKILL.md:** description; mục II thêm 13a (QĐ 1213/QĐ-BCT) và 15a (toàn văn QĐ 2848 + cách dẫn căn cứ); mục III (bảng thẩm quyền, "Ai ký", bộ mã TTHC 2 nhóm); mục V; mục VI câu gác cổng 1-3; mục VII nguyên tắc 10 (kèm bài học PDF ký số).
- **ref 01:** Bước 4 "2 nhịp ủy quyền" (QĐ 1696 + QĐ 2848); mục 2a; sơ đồ; mục 4 + thời hạn 31/12/2030; mục 5 bảng đủ 6 mã TTHC; mục 6.
- **ref 09:** tiêu đề; bảng hệ quả; mục **3a** (QĐ 1213 + bảng mã) và **3b** (toàn văn QĐ 2848: bảng Phụ lục mới, Điều 2 mới, căn cứ, hệ quả); mục 5.
- **ref 03, 04, 07, 08, 14, 16, 17:** đồng bộ trạng thái loại 5, 8 - Giám đốc Sở ký từ 14/8/2026; ref 16 thêm khối căn cứ Biên bản thẩm định/GP loại 5, 8.
- **ref 15:** dòng QĐ 1696; dòng mới `QD-2848-QD-UBND-14-8-2026-sua-doi-bo-sung-QD-1696.pdf`; lưu ý đọc PDF ký số.
- **van-ban-goc/04-uy-quyen-quy-trinh/:** thêm bản PDF đã ký QĐ 2848.
- **plugin.json:** 1.6.0 → 1.7.0.
