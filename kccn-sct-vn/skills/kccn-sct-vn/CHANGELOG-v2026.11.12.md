# CHANGELOG — kccn-sct-vn v1.66.0 (12/11/2026)

Nguồn: Bạn gửi tệp nén `tai_lieu_nhiem_vu_17.zip` (Báo cáo GPMB dự án đường sắt Lào Cai - Hà Nội - Hải Phòng tuần 24–30/10/2026
kèm phụ lục), yêu cầu "cập nhật các thông tin mới nhất liên quan đến khu công nghiệp, cụm công nghiệp liên quan đến đường sắt".

- **ref 56 (mới)**: Báo cáo **727/BC-TGV ngày 02/11/2026** của Tổ Giúp việc Ban Chỉ đạo GPMB đường sắt (số đọc bằng
  `extract_metadata.py`, ngày đọc trên ảnh trang 1). Thông tin chung dự án đoạn qua tỉnh; phạm vi GPMB phường Lào Cai: 66 tổ chức
  (42 KCN Đông Phố Mới, 09 CCN Sơn Mãn, 02 CCN Đông Phố Mới, 07 khác); 04 dự án hạ tầng tiếp nhận cơ sở di dời do Ban QLDA ĐTXD
  tỉnh làm chủ đầu tư (SX1-SX2 đã xong; Khu Bản Qua ~70 %; Khu Thống Nhất QĐ 1841/QĐ-UBND 23,6 ha ~68 %; Khu Vạn Hòa không đầu tư),
  vốn 2026; Hội đồng thẩm định đơn giá QĐ 3285/QĐ-UBND 11/9/2026; mốc phê duyệt phương án trước 05/11/2026 (TB 153/TB-VPUBND).
  Tra thêm kho riêng tư: **QĐ 4093/QĐ-UBND ngày 02/11/2026** thành lập Tổ hỗ trợ doanh nghiệp KCN Đông Phố Mới (PCT Phan Trung Bá
  Tổ trưởng; Trưởng BQL KKT Tổ phó, cơ quan thường trực; PGĐ Sở Công Thương là thành viên); TB 279-TB/VPTU ngày 12/10/2026 mục 4.
  Ghi chú lệch nguồn: Khu Bản Qua 95 ha (ref 17) ≠ "khoảng 75 ha" (BC 727); TB 153 ≠ 158/TB-VPUBND; 279-TB/VPTU ≠ "279-TB/BCĐ".
- **ref 17 mục V**: ghi rõ số liệu tháng 7/2026 là lịch sử, trỏ sang ref 56. **ref 12**: dòng KCN Đông Phố Mới trỏ ref 56.
- **Sổ lỗi L002**: bỏ câu "chủ đầu tư chưa ghi trong kho"; chủ đầu tư là Ban QLDA ĐTXD tỉnh; sửa câu ví dụ giao việc.
- **check_facts**: thêm `tb-279-vptu-khong-phai-tb-bcd`, `ha-tang-khu-ban-qua-chu-dau-tu-ban-qlda-dtxd-tinh`.
- **SKILL.md**: thêm dòng ref 56 vào bảng reference.
- `trang-thai/di-doi-kcn-dong-pho-moi-duong-sat.md` (mới): tệp trạng thái hồ sơ.
- `plugin.json` 1.64.1 → **1.66.0** (bỏ qua 1.65.0 vì CHANGELOG mục 05/11/2026 đã dùng số này).
