# CHANGELOG — attp-sct-vn v1.6.0 (07/10/2026)

Nạp **Thông tư số 63/2026/TT-BCT ngày 30/9/2026** của Bộ Công Thương quy định về cơ sở dữ liệu thực phẩm thuộc phạm vi quản lý của Bộ Công Thương (KT. Bộ trưởng - Thứ trưởng Trương Thanh Hoài ký; hiệu lực 15/11/2026; thay thế TT 11/2026/TT-BCT ngày 27/02/2026 về truy xuất nguồn gốc thực phẩm). Bạn gửi bản .docx.

- **references/12 mới** `12-csdl-thuc-pham-truy-xuat-nguon-goc-tt63-2026.md`: thẻ văn bản, mốc áp dụng trước/sau 15/11/2026, khối căn cứ; 8 nhóm dữ liệu (Điều 6), đầu mối Bộ (Cục Công nghiệp, Cục KHCN&CĐS); việc của Sở tham mưu UBND tỉnh theo Điều 15 (số hóa GCN còn hiệu lực, hồ sơ công bố, hậu kiểm, báo cáo; ưu tiên hồ sơ trước khi CSDL vận hành); nghĩa vụ truy xuất của cơ sở (Điều 9-11, 17: hồ sơ phải lưu, lưu 12 tháng sau hạn dùng/60 tháng từ ngày sản xuất, cung cấp trong 24 giờ, các bước truy xuất, Mẫu báo cáo Phụ lục, hàng rủi ro cao); việc của cơ quan nhà nước (Điều 12-13) và khung công văn yêu cầu cơ sở truy xuất.
- references/08: thêm mốc TT 63/2026 vào bảng diễn biến; TT 63 vẫn dẫn NĐ 15/2018 + NQ 15/2026 làm căn cứ — bằng chứng củng cố mới nhất; mục 5 ghi TT 11/2026/TT-BCT bị thay từ 15/11/2026.
- references/05 mục 4: dẫn trình tự truy xuất theo TT 63/2026 (từ 15/11/2026), trỏ ref 12.
- van-ban-goc: bản gốc TT 63/2026 (.docx) + bản text; README.
- SKILL.md: nghiệp vụ (5), bản đồ references, mục van-ban-goc. plugin.json: description thêm TT 63/2026.
- `scripts/check_facts.py`: rule `tt-11-2026-bct-thay-boi-tt-63` (FAIL) — dòng nhắc TT 11/2026/TT-BCT phải kèm TT 63/2026. `registry/trang-thai.csv`: dòng TT 63/2026.
