# CHANGELOG — bvmt-sct-vn v1.6.0 (01/10/2026)

Bổ sung **Quyết định số 3556/QĐ-UBND ngày 30/9/2026** của UBND tỉnh Lào Cai (KT.CT — PCT Nguyễn Thành Sinh ký; hiệu lực từ ngày ký) ban hành **Quy chế thu thập, quản lý, sử dụng, cập nhật và khai thác, chia sẻ thông tin, dữ liệu tài nguyên và môi trường tỉnh Lào Cai** — Bạn cung cấp 01/10/2026. Số/ngày đã đối chiếu ảnh trang 1 và `extract_metadata.py` (tên tệp gốc ghi 25/9, 28/9 — ngày đúng 30/9/2026).

Thay đổi:

- `references/12-quy-che-du-lieu-tnmt-qd-3556.md` (MỚI): thẻ văn bản (căn cứ NĐ 73/2017, NĐ 165/2025, NĐ 278/2025, TT 03/2022/TT-BTNMT, TT 02/2025/TT-BNNMT; bãi bỏ QĐ 44/2021/QĐ-UBND, QĐ 23/2011/QĐ-UBND Yên Bái, k16 Đ3 QĐ 59/2025/QĐ-UBND); định vị vai (Sở NN&MT chủ quản CSDL, VPĐK đất đai lưu trữ, Sở Công Thương chịu trách nhiệm dữ liệu của mình); bảng nghĩa vụ của Sở theo từng điều — giao nộp ≤ 30 ngày sau nghiệm thu (01 bộ điện tử + 01 bộ giấy, biên bản BM.01 PL V TT 03/2022), 01 năm với dữ liệu thường xuyên, 03–04 tháng với hồ sơ XDCB, giữ lại ≤ 02 năm, metadata, Mẫu 01 NĐ 73, **báo cáo Mẫu 05 trước 15/12 hằng năm**; bảng dữ liệu TNMT đang ở Sở (KNK 18 cơ sở, XLNT CCN, ranh giới CCN, khoáng sản); **điểm vênh: Quy chế vẫn giao lĩnh vực địa chất - khoáng sản cho Sở NN&MT trong khi NQ 66.25/2026/NQ-CP đã chuyển về Sở Công Thương từ 15/9/2026**; lịch việc đề xuất (phân công đầu mối 10/2026, báo cáo kỳ đầu 15/12/2026); 6 anti-error.
- `references/02-khung-phap-ly.md`: mục H thêm số 40; bảng theo dõi hiệu lực thêm 2 dòng (QĐ 44/2021 và QĐ 23/2011 bị bãi bỏ; QĐ 3556 hiệu lực).
- `references/01-vai-tro-sct-bvmt.md`: bảng phân vai thêm dòng "Dữ liệu TNMT do Sở tạo lập/đang giữ".
- `SKILL.md`: description, mục I, III (nhóm 10), IV, VII (ref 12), IX.
- `van-ban-goc/tinh/` (MỚI): PDF Quyết định + PDF Quy chế + bản trích chữ; cập nhật `van-ban-goc/INDEX.md`.
- Toàn kho: `scripts/check_facts.py` thêm rule `qd-44-2021-ubnd-du-lieu-tnmt-bai-bo`; `registry/trang-thai.csv` thêm QĐ 3556/QĐ-UBND và QĐ 44/2021/QĐ-UBND (bị bãi bỏ).
- `plugin.json` → 1.6.0.
