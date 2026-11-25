# sct-laocai-org-vn 2.17.0 — 25/11/2026 — Bạn chốt 25/11/2026: vận chuyển hàng hóa nguy hiểm, PCCC chuyển sang PGĐ Hoàng Văn Thuân

- SKILL.md (lưu ý cốt lõi, bảng routing, khối người ký, hướng dẫn mục 5, sai lầm thường gặp, bảng liên kết plugin), reference 07 mục E, F, `data/phan-cong-ky.json` (HHNH, PCCC → Hoàng Văn Thuân): vận chuyển hàng hóa nguy hiểm và PCCC ngành Công Thương do **PGĐ Hoàng Văn Thuân** ký — Bạn chốt 25/11/2026 (QĐ 7750/QĐ-SCT không ghi đích danh hai lĩnh vực này). Giấy phép vận chuyển 07/10–16/11/2026 do PGĐ Nguyễn Đình Chiến ký là lịch sử.
- Còn giữ "dự kiến PGĐ Chiến", chờ Bạn xác nhận: khu công nghiệp, an toàn ngành khác (xăng dầu, khí), chất lượng sản phẩm hàng hóa, KHCN lĩnh vực công nghiệp.
- Máy kiểm `check_facts.py` rule `pgd-thuan-ky-hoa-chat-vlncn-tu-17-11` áp thêm cho hnh-sct-vn, pccc-sct-vn.
- `plugin.json` 2.16.0 → 2.17.0.

# sct-laocai-org-vn 2.16.0 — 25/11/2026 — QĐ 7750/QĐ-SCT ngày 17/11/2026 phân công Ban Giám đốc (thay QĐ 6320/QĐ-SCT)

- Bạn gửi bản PDF ký số ngày 25/11/2026; số, ngày, người ký đọc bằng `extract_metadata.py`: **7750/QĐ-SCT ngày 17/11/2026**, Giám đốc Hoàng Chí Hiền ký, hiệu lực từ ngày ký, thay QĐ 6320/QĐ-SCT ngày 06/10/2026. Văn bản nội bộ — bản gốc lưu ở kho riêng tư, không lưu ở kho công khai.
- Reference 07 (mới): thể thức, căn cứ; Điều 1 (7 khoản); bảng phân công Điều 2 chép sát bản gốc; bảng đối chiếu QĐ 6320 ↔ QĐ 7750; hệ quả người ký với Phòng QLCN; việc còn mở.
- SKILL.md: viết lại mục "Phân công nhiệm vụ trong Lãnh đạo Sở"; bảng routing, khối người ký, hướng dẫn mục 5, sai lầm thường gặp, mục NQ 66.25, bảng liên kết plugin. Thay đổi làm đổi người ký: **hóa chất, VLNCN** và **xây dựng chuyên ngành Công Thương** (trừ dự án năng lượng) về PGĐ Hoàng Văn Thuân; **Phòng Quản lý Khoáng sản** về PGĐ Phạm Năng Chung; PGĐ Nguyễn Đình Chiến vẫn phụ trách Phòng QLCN. HHNH, PCCC, KCN: QĐ 7750 không ghi đích danh — giữ "dự kiến PGĐ Chiến", chờ Bạn xác nhận lại. Xã, phường theo dõi: 99/99.
- `data/phan-cong-ky.json`: thêm giai đoạn từ 17/11/2026 (thêm lĩnh vực "xây dựng"), đóng giai đoạn QĐ 6320 ở 16/11/2026.
- Reference 03, 04: ghi chú QĐ 6320 đã được thay.
- Máy kiểm `scripts/check_facts.py`: bỏ rule `pgd-chien-ky-hoa-chat-vlncn-hhnh`; thêm `pgd-thuan-ky-hoa-chat-vlncn-tu-17-11`, `qd-6320-da-thay-bang-7750`.
- `plugin.json` 2.15.0 → 2.16.0.
