# dacn-sct-vn 1.13.0 — 03/11/2026

## Tính giá trị sản xuất, tăng trưởng kinh tế tỉnh (ref 17) — nạp 05 tệp Bạn gửi

- **Dữ liệu nhóm A** `du-lieu/sxkd-tang-truong/2026-10-26-stc-quy-iv.json`: Phụ lục 01–03 của Sở Tài chính rà soát SXKD, đầu tư, xây dựng quý IV và cả năm 2026 (theo VB 10210/UBND-TH 07/10/2026; chốt 26/10/2026; báo cáo chưa có số) — 940 đơn vị, 595 công trình, 46 trọng điểm, bảng tổng hợp; máy cộng khớp lời văn báo cáo (22.253,14 tỷ; công nghiệp 7.358,80 tỷ).
- **Dữ liệu nền 2025** `du-lieu/nen-2025/`: 18 bảng Yên Bái cũ (31/5/2025) + 5 bảng Lào Cai cũ (6/2025): GTSXCN giá SS 2010 2020–2025, năng lực sản xuất theo sản phẩm, KCN, CCN, FDI, dự án cấp mới, thủy điện, QHĐ VIII, mỏ, hạ tầng thương mại.
- **Scripts mới:** `tinh_tang_truong.py` (tong-hop, cong-nghiep, do-phu, uoc-nam, dong-gop, quy-doi, nen-2025); `nap_sxkd_stc.py` (nạp Excel Sở Tài chính kỳ sau); `xuat_bang_an_danh.py` (xuất bảng Excel đã ẩn danh).
- **Reference 17 mới:** GATE viện dẫn bản chưa số; 4 điều phải biết (không phải GTSXCN; độ phủ ≈ 33,6% GTSXCN 9 tháng; vắng 20/37 DN CV 10349; dữ liệu bất thường); công thức ước cả năm, QIV cần đạt, đóng góp GRDP, quy đổi; quy trình tháng; mục lục dữ liệu nền.
- **Ẩn danh (kho công khai):** 191 hộ kinh doanh, tổ đội; họ tên trong ghi chú, vướng mắc GPMB; số điện thoại, cột liên hệ/đại diện; danh sách 510 cửa hàng LPG chỉ giữ số đếm. Bạn xác nhận 03/11/2026 số điện thoại, họ tên là công khai, lãnh đạo đã duyệt → bản đầy đủ đặt ở plugin riêng tư `dong-nghiep-sct-vn` 1.3.0 (kho vlncn-laocai, ref 07).
- SKILL.md: nghiệp vụ 15, bảng reference, công cụ, phạm vi dữ liệu; check_facts thêm rule `stc-sxkd-quy-iv-khong-phai-gtsxcn`.
- `plugin.json` → 1.13.0.
