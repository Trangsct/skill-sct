# CHANGELOG — sct-laocai-org-vn v2.10.0 (22/10/2026)

Bạn gửi bản PDF ký số ba văn bản ngày 22/10/2026; số, ngày, người ký đọc bằng `vbhc-vn/skills/vbhc-vn/scripts/extract_metadata.py`.

- **QĐ 6320/QĐ-SCT ngày 06/10/2026** (GĐ Hoàng Chí Hiền ký) là Quyết định phân công nhiệm vụ GĐ, PGĐ, thay QĐ 766/QĐ-SCT; căn cứ QĐ 6286/QĐ-SCT ngày 05/10/2026 ban hành Quy chế làm việc. Chốt vướng mắc ở ref 03 mục A: SKILL.md và mọi plugin đổi số dẫn từ "QĐ 6286/QĐ-SCT ngày 05/10/2026" sang "QĐ 6320/QĐ-SCT ngày 06/10/2026"; nội dung phân công không đổi.
- **QĐ 6226/QĐ-SCT ngày 02/10/2026** (GĐ Hoàng Chí Hiền ký) ban hành Quy định chức năng, nhiệm vụ Văn phòng và 5 phòng (Điều 3–8; Phòng Quản lý khoáng sản Điều 6), thay QĐ 59/QĐ-SCT. `references/01-chuc-nang-nhiem-vu-cac-phong-qd59.md` → `references/01-chuc-nang-nhiem-vu-cac-phong-qd6226.md`, viết lại toàn bộ theo QĐ 6226 (giữ số điều, khoản, mục, điểm để viện dẫn) kèm bảng thay đổi so với QĐ 59 (lịch sử). Bỏ phần nhiệm vụ QLNL, QLTM theo QĐ 59 chép trùng trong SKILL.md.
- SKILL.md: căn cứ pháp lý (QĐ 6226, QĐ 6286 Quy chế làm việc, QĐ 6320); tóm tắt 6 đơn vị theo QĐ 6226; lưu ý lĩnh vực của PGĐ Thuân nằm ở Phòng QLCN (dầu khí, luyện kim, BVMT - CN môi trường, ATVSLĐ — điểm b, c mục 2.12); bảng routing tách khai thác, chế biến khoáng sản (Phòng QLKS) và luyện kim, dầu khí (Phòng QLCN); ký hiệu Phòng QLKS `/SCT-KS`; dẫn điều khoản trong mục "Sai lầm thường gặp" theo QĐ 6226.
- QĐ 3628/QĐ-UBND Bạn gửi kèm trùng khớp từng byte với `van-ban-goc/2026.10.02-QD-3628-QD-UBND.pdf` đã có — không thêm.
- Bản gốc QĐ 6226, QĐ 6320 là văn bản nội bộ của Sở: không lưu vào kho công khai (CLAUDE.md gốc kho), chỉ viết lại nội dung.
- `scripts/check_facts.py`: rule `qd-phan-cong-bgd-la-6320`, `qd-59-sct-da-thay-bang-6226` (FAIL). `registry/trang-thai.csv`: thêm QĐ 59, 6226, 766, 6320, 6286/QĐ-SCT.
- `plugin.json` 2.9.0 → 2.10.0.
