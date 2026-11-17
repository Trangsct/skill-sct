# CHANGELOG bvmt-sct-vn

## 1.8.2 — 17/11/2026 — Bản gốc Nghị định 48/2026/NĐ-CP

- Lưu bản gốc Nghị định số 48/2026/NĐ-CP ngày 29/01/2026 (PDF bản quét 62 trang + bản trích chữ OCR `.txt`): `van-ban-goc/2026.01.29-48.2026.ND.CP-Sua-doi-ND-08-2022-bao-ve-moi-truong.pdf`; ghi vào INDEX. Chưa có bản Word.
- Ref 03: thay ghi chú tạm bằng nguyên văn STT 4 Phụ lục II đã đối chiếu bản gốc (danh sách công đoạn loại trừ đối với phân bón hóa học); sửa dòng STT 4 trong bảng cho đủ danh sách.

## 1.8.1 — 17/11/2026 — Bản gốc phụ lục Nghị định 08/2022 (bản 2022)

- Lưu bản gốc Phụ lục I–XXXIV kèm Nghị định số 08/2022/NĐ-CP (bản năm 2022, Bạn cung cấp 17/11/2026): `van-ban-goc/2022.01.10-08.2022.ND.CP-Phu-luc-kem-theo-Nghi-dinh-ban-2022.doc` + bản trích chữ `.txt`; ghi vào INDEX văn bản gốc. Bản này chưa gồm sửa đổi của NĐ 05/2025/NĐ-CP, NĐ 48/2026/NĐ-CP.
- Ref 03: thêm ghi chú đối chiếu STT 4 Phụ lục II (phân bón hóa học) — nguyên văn bản 2022 "trừ phối trộn, sang chiết, đóng gói"; cách viết nhận xét khi chưa có bản gốc phụ lục NĐ 48/2026.

## 1.8.0 — 16/11/2026 — Phong cách phiếu nhận xét hội đồng thẩm định (ref 13)

- Thêm `references/13-phong-cach-phieu-nhan-xet-hoi-dong.md`: phong cách phiếu nhận xét của thành viên Hội đồng thẩm định (GPMT, ĐTM, quy chuẩn kỹ thuật) — đúng mẫu, ngắn gọn (mỗi mục 2–3 gạch đầu dòng, cả phiếu khoảng 3 trang), xứng tầm (bỏ góp ý vụn về chính tả, phông, ký hiệu); góp ý chi tiết đủ ba phần "hồ sơ ghi gì - thiếu gì - đề nghị sửa thế nào"; kiểm chứng file gốc trước khi kết luận sai; chuẩn căn lề A4, khối ký.
- SKILL.md (nhóm việc 9, bảng reference) và ref 08 mục 4 dẫn sang ref 13.
- Nguồn: Bạn chốt 16/11/2026 "ghi nhớ phong cách làm việc này vào plugin để tôi nhận xét GPMT hoặc ĐTM cho hay như vậy", rút từ phiếu nhận xét hồ sơ dự thảo QCĐP nước sạch 10/11/2026 ("tham gia đúng mẫu, ngắn gọn, xứng tầm"; "chỗ góp ý chi tiết nên rõ hơn cho ai cũng hiểu được").
- `plugin.json` 1.7.3 → 1.8.0. Chi tiết: `CHANGELOG-v2026.11.16-b.md`.

## 1.7.1 — 18/10/2026 — Căn cứ chức năng Sở: QĐ 3628/QĐ-UBND ngày 02/10/2026 thay QĐ 05/2025/QĐ-UBND (chuyển từ PR 112/115)

- Thay dẫn QĐ 05/2025/QĐ-UBND → **QĐ 3628/QĐ-UBND ngày 02/10/2026** (Quy định CNNV, quyền hạn, cơ cấu tổ chức Sở Công Thương — 06 phòng, có Phòng Quản lý khoáng sản; không có khu công nghiệp) trong mẫu văn bản, reference: `references/11-kl75-ctr31-ctr104-tu-trien-khai-sct.md`. Dòng nói về văn bản đã ký trước 02/10/2026 giữ nguyên dẫn cũ, ghi "lịch sử". Nguồn: `sct-laocai-org-vn` ref 04; bản gốc + `.txt`: `sct-laocai-org-vn/skills/sct-laocai-org-vn/van-ban-goc/2026.10.02-QD-3628-QD-UBND.pdf`. Máy kiểm: rule `qd-05-2025-da-thay-bang-qd-3628` trong `scripts/check_facts.py`.
- `plugin.json` 1.7.0 → 1.7.1.

## 1.7.0 — 17/10/2026 — Sửa tim_van_ban.py không tìm được số hiệu có chữ Đ

- `scripts/tim_van_ban.py` (bản chép từ gốc kho, đồng bộ bằng `build_so_cai_van_ban_goc.py`): sửa lỗi biểu thức tìm — chữ "đ" bị thay hai lần thành `[đ[dđ]]` nên MỌI số hiệu có chữ Đ (NĐ-CP, QĐ-UBND, QĐ-TTg) không bao giờ khớp và script kết luận sai "chưa có trong kho" (phát hiện 17/10/2026 khi kiểm thử GATE 0). Sau khi sửa: "181/2024/NĐ-CP" khớp 3 mục danh mục.
- `plugin.json` → 1.7.0. Chi tiết: `CHANGELOG-v2026.10.17.md`.

