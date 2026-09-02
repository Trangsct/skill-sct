# CHANGELOG — hl-vlncn-sct-vn

## [1.4.1] - 02/9/2026 — rà soát tổng thể
- Mẫu 12: số GP sử dụng VLNCN ghi `…/GP-SCT` (từ 20/8/2026; GP cũ `…/GP-UBND`).
- Mẫu 01: dòng Lưu mặc định CN(Khôi) từ 10/7/2026 thay ghi chú CN(M.Cường) cũ.
- Ref 04 bước 2 (nơi nộp hồ sơ): thống nhất quy ước cố định — Cổng dịch vụ công một cửa Bộ Công Thương https://motcua-tthc.moit.gov.vn/, không ghi chung "Cổng DVCQG"/"Hệ thống TTGQ TTHC tỉnh".
- plugin.json 1.4.0 → **1.4.1**.

## [1.4.0] - 29/8/2026 (CV 1198/ATMT-ATKV — hướng dẫn nghiệp vụ Cục ATMT)
- Bạn cung cấp ảnh chụp **CV 1198/ATMT-ATKV ngày 21/7/2025** của Cục Kỹ thuật an toàn và Môi trường công nghiệp (Cục trưởng Phạm Tuấn Anh ký) trả lời SCT Lai Châu — GATE metadata từ ảnh. 3 nội dung: (1) GCN huấn luyện **thuộc quản lý của DN đề nghị cấp** (k2 Đ8 NĐ 181/2024); (2) NLĐ ký **nhiều HĐLĐ bán thời gian → từng DN phải tự huấn luyện + đề nghị cấp GCN riêng** (Đ19 BLLĐ), không dùng chung GCN giữa các DN; (3) thông báo sử dụng VLNCN với UBND tỉnh/xã — luật **không buộc UBND tỉnh kiểm tra điều kiện** đối với nội dung thông báo.
- Lưu `van-ban-goc/` (trích lục .md + ảnh .jpg), cập nhật INDEX; thêm ref `01` mục **C-quater**; FAQ 11 (ref `04`); khung pháp lý mục 11 + **anti-error 13** (phân biệt "giá trị toàn quốc" k5 Đ9 với việc dùng chung GCN giữa các DN) tại SKILL.md; bổ sung từ khóa description; plugin.json → 1.4.0.
- Ghi chú: nguồn hiện là ảnh bản giấy — khi viện dẫn trong văn bản chính thức, xin bản điện tử/sao y đối chiếu lại.

## [1.3.2] - 21/8/2026 (CV 5085/SCT-VP — triển khai nội bộ hai QĐ ủy quyền)
- Bạn cung cấp bản ký **CV 5085/SCT-VP ngày 19/8/2026** (GĐ Hoàng Chí Hiền ký; lưu tại `sd-vlncn-sct-vn/van-ban-goc/`): triển khai nội bộ QĐ 1883 + QĐ 2867 — **PGĐ Hoàng Văn Thuân trực tiếp chỉ đạo**, **Phòng QLCN chủ trì** tham mưu Lãnh đạo Sở; nhóm huấn luyện viện dẫn đúng cụm "k1 Đ6, Đ9, điểm b k1 Đ18 NĐ 181/2024" của Phụ lục QĐ 1883 → xác nhận nội bộ chính thức GCN huấn luyện tiếp tục theo QĐ 1883; **không đổi tiền lệ người ký** (QĐ công nhận + GCN vẫn GĐ ký trực tiếp — CV là phân công chỉ đạo, không phải giao ký thay).
- Thêm ref `01` mục **C-ter**; cập nhật INDEX văn bản gốc + SKILL.md (mục nhiệm vụ báo cáo/ủy quyền); plugin.json → 1.3.2.

## [1.3.1] - 19/8/2026 (bổ sung — Phụ lục QĐ 2867)
- Bạn cung cấp Phụ lục danh mục QĐ 2867 (bản trình) → **CHỐT: QĐ 2867 chỉ ủy quyền GP SỬ DỤNG VLNCN, KHÔNG bao gồm GCN huấn luyện** → nhiệm vụ huấn luyện tiếp tục viện dẫn QĐ 1883/QĐ-UBND như cũ, không đổi căn cứ; gỡ "quy tắc tạm thời" tại ref 01 C-bis, cập nhật INDEX + SKILL.md. Hai QĐ song song cùng hết hạn 28/02/2027 — khi tham mưu ủy quyền giai đoạn sau, đề xuất gộp một QĐ.

## [1.3.0] - 19/8/2026
- Ghi nhận **QĐ 2867/QĐ-UBND ngày 17/8/2026** — QĐ ủy quyền MỚI cùng lĩnh vực VLNCN (hiệu lực 20/8/2026 → hết 28/02/2027; PCT Nguyễn Thành Sinh ký; cùng gốc TTr 2205/TTr-SCT; báo cáo 06 tháng/01 năm). Bản ký lưu tại `sd-vlncn-sct-vn/van-ban-goc/`; ⚠ **chưa có Phụ lục danh mục** nên chưa xác định có bao trùm nhiệm vụ GCN huấn luyện hay không; chính văn không thay thế/bãi bỏ QĐ 1883. Thêm ref `01` mục **C-bis** (quy tắc tạm thời chọn căn cứ ủy quyền theo mốc 20/8/2026), cập nhật INDEX văn bản gốc + SKILL.md. **Chờ Bạn cung cấp Phụ lục QĐ 2867 để chốt.**

## [1.1.0] - 24/7/2026
- Cập nhật khung xử phạt theo **NĐ 275/2026/NĐ-CP ngày 08/7/2026** (hiệu lực 25/8/2026, thay NĐ 71/2019 + Điều 1 NĐ 17/2022): hành vi nhân lực chuyển **Đ50 cũ → Đ54 mới** (sử dụng người chưa huấn luyện 15–30 tr cá nhân + đình chỉ 3–6 tháng; không tổ chức huấn luyện 5–15 tr). Sửa SKILL.md (mục I, khung pháp lý 9, bảng thẩm quyền), ref 01, ref 06 §2 (kèm quy tắc chuyển tiếp Đ74), mẫu 12, INDEX văn bản gốc. Chi tiết chế tài chuyển về plugin dùng chung mới **`xp-hc-vlncn-sct-vn`** (bảng Đ53–61, thẩm quyền Đ62–73, đối chiếu cũ→mới, toàn văn NĐ 275/2026).

## [1.0.1] - 14/7/2026
- Đồng bộ Thông báo phân công nội bộ Phòng QLCN 10/7/2026: mặc định dòng Lưu hồ sơ huấn luyện KTAT VLNCN = **CN(Khôi)**; ví dụ thực tế trước 6/7/2026 giữ CN(Linh) đúng lịch sử.

## v1.0.0 — 04/7/2026
- Phát hành lần đầu. Phạm vi: huấn luyện, kiểm tra, cấp/cấp lại GCN huấn luyện KTAT VLNCN & TCTN (Sở Công Thương Lào Cai, ủy quyền QĐ 1883/QĐ-UBND ngày 06/11/2025).
- SKILL.md: 5 nghiệp vụ; thẩm quyền; 2 quy trình lõi (người quản lý / đối tượng khác); 12 anti-error đúc kết từ hồ sơ thật 2025–2026.
- 7 references: pháp lý (trích Đ4–20 NĐ 181, Đ24 NĐ 146, QĐ 1883); quy trình A/B/C/D; hướng dẫn DN + FAQ; nội dung huấn luyện Đ7/Đ12 + định hướng ra đề; kiểm tra – xử phạt – báo cáo; index ví dụ thực tế (metadata đã GATE).
- 14 mẫu văn bản: KH, TB (2 chế độ), QĐ công nhận, BC Tổ kiểm tra, GCN Mẫu 03, QĐ Tổ kiểm tra, CV trả hồ sơ (Văn Thịnh)/không cấp (Duy Hiếu), chuỗi đoàn kiểm tra chấp hành, BC UBND tỉnh, Mẫu 01+02 NĐ 181.
- vi-du-thuc-te: 13 file .docx thật đã ban hành 2026; van-ban-goc: NĐ 181/2024 toàn văn + hồ sơ QĐ ủy quyền.
- Liên kết plugin: sd-vlncn-sct-vn (GP sử dụng, PANM, xử phạt NĐ 71 dùng chung ref 05), kho-vlncn-sct-vn (kho, thủ kho), hnh-sct-vn (ranh giới vận chuyển), vbhc-vn, sct-laocai-org-vn.
