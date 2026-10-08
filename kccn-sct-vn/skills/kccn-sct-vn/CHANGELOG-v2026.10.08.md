# CHANGELOG — kccn-sct-vn v1.50.0 (08/10/2026)

Địa bàn ưu đãi đầu tư cấp xã (QĐ 2167/QĐ-UBND) và hướng trả lời doanh nghiệp hỏi miễn tiền thuê đất.

- **references/46 (mới)**: QĐ 2167/QĐ-UBND ngày 23/6/2026 công bố địa bàn ưu đãi đầu tư cấp xã (87 xã, phường đặc biệt khó khăn, 08 khó khăn; căn cứ NĐ 96/2026/NĐ-CP, QĐ 2752/QĐ-UBND) thay thế QĐ 1894/QĐ-UBND ngày 07/11/2025 (61 + 34); danh mục nguyên văn; 04 phường Văn Phú, Yên Bái, Nam Cường, Âu Lâu không có tên; bảng đối chiếu nơi đặt từng KCN, CCN; QĐ 2752/QĐ-UBND ngày 31/12/2025 (thôn, xã vùng DTTS và miền núi 2026-2030; Gia Phú khu vực II); vụ Văn bản 232/CV-LCIDI-HT ngày 08/10/2026 (CCN Thống Nhất 1 hỏi miễn tiền thuê đất toàn bộ thời gian thuê) — hướng trả lời trọng tâm thẩm quyền: Sở chỉ tham gia ý kiến (điểm a khoản 2 Điều 33 NĐ 32/2024), việc xác định miễn, giảm thuộc Sở NN&MT, Thuế tỉnh.
- **van-ban-goc**: PDF QĐ 2167 + Phụ lục + bản trích chữ; PDF QĐ 1894 + bản trích chữ; QĐ 2752 bản scan nén 120 dpi + OCR 63 trang; Phụ lục II QĐ 2752 + OCR. QĐ 1894 và QĐ 2752 ≥ 3 MB — export-ignore, claude.ai đọc bản trích chữ.
- **references/16**: sửa căn cứ của QĐ 2167 (NĐ 96/2026/NĐ-CP, QĐ 2752 — không phải NĐ 31/2021); trỏ sang ref 46; thêm nguyên tắc Sở không xác định miễn, giảm tiền thuê đất.
- **SKILL.md**: mục I.17 và dòng ref 46 trong bảng reference.
- `scripts/check_facts.py` gốc kho: rule `qd-1894-dia-ban-uu-dai-thay-boi-qd-2167` (FAIL). `registry/trang-thai.csv`: QĐ 2167, QĐ 1894 (bị thay thế), QĐ 2752.
- `plugin.json` → 1.50.0.

# CHANGELOG — kccn-sct-vn v1.49.1 (08/10/2026)

Bạn chốt 08/10/2026: văn bản quy phạm pháp luật Bạn gửi phải lưu bản Word vào `van-ban-goc/` (quy tắc chung ở `CLAUDE.md` gốc kho).

- **references/24**: ghi rõ Nghị định 303/2026/NĐ-CP **thiếu bản gốc** (file Bạn gửi 04/8/2026 không được lưu); thêm mục A-bis — bảng đối chiếu khoản của Điều 1 Nghị định 303/2026 với điều của Nghị định 32/2024 (khoản 3 ↔ Điều 8 và khoản 5 ↔ khoản 1 Điều 10 theo nguồn thứ cấp; khoản 18 ↔ Điều 35 đã đọc bản gốc; khoản sửa khoản 1 Điều 2 chưa rõ); cảnh báo bẫy trùng số 303/2025/NĐ-CP ≠ 303/2026/NĐ-CP.
- Việc còn lại: Bạn gửi bản Word Nghị định 303/2026/NĐ-CP để lưu và điền đủ bảng.
