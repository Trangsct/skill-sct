# CHANGELOG — hc-sct-vn

## [1.3.0] - 08/9/2026 — Sở là thành viên Hội đồng thẩm định KH của Cục Hóa chất; Phiếu Mẫu 03c; vụ DAP số 2
- **ref 17 (mới)** `17-thanh-vien-hoi-dong-tham-dinh-kh-cuc-hoa-chat.md`: phân biệt vai trò Sở (cơ quan thẩm định với điểm b / thành viên Hội đồng của Cục với điểm a); cách điền Phiếu Mẫu 03c (không tự đánh X ô lựa chọn, ngày để trống, chức vụ chuyên môn); checklist 8 điểm thẩm định nội dung KH theo Phụ lục II TT 02/2026 (KH điều chỉnh phải khớp Bảng 1.2 → 2.1 → 2.2 → mục 4.3 + diễn tập; bộ ngưỡng AEGL 60 phút; axit không bay hơi phải tính lượng tràn); điều kiện an toàn trạm xuất NH3 lỏng và trạm xuất axit (110% dung tích xe bồn, 17 m, vật liệu, không phun nước vào H2SO4 đặc); quan hệ KH điều chỉnh với thủ tục đầu tư - xây dựng - PCCC - môi trường; bán H2SO4 ra ngoài → GP kinh doanh hóa chất kiểm soát đặc biệt nhóm 2 (tỉnh) + phiếu kiểm soát mua bán; dữ kiện vụ DAP số 2 đã xác minh.
- **vi-du-thuc-te/ke-hoach-su-co/**: `Mau-03c-goc.docx`; `2026.09.08. Phieu-nhan-xet-Mau-03c-KH-su-co-DAP-so-2.docx` (bản hoàn thiện cho CV Loan, 10 nhóm yêu cầu); `build_phieu_03c.py` + `line_runs.txt` (script dựng Phiếu 03c trên mẫu gốc: A4 lề 2-2-3-2, header 13pt 2 đường Line shape, thân 14pt lùi 1 cm, subscript công thức, m2/m3 số mũ, nén chữ tránh chữ lẻ); `VB-de-nghi-1648-DAP2-KTh-tham-dinh-KH.pdf`.
- SKILL.md (mục I, IV, V), ref 06 (mục 3, 12), ref 15 (mục lục), ref 16 (mục 5a) trỏ sang ref 17; description plugin/SKILL thêm từ khóa Mẫu 03c, trạm xuất NH3, DAP số 2.

## [1.2.3] - 02/9/2026 — nơi nộp TTHC duy nhất motcua-tthc.moit.gov.vn
- Nơi nộp hồ sơ TTHC: DUY NHẤT Cổng dịch vụ công một cửa Bộ Công Thương https://motcua-tthc.moit.gov.vn/ (đăng nhập VNeID) — Bạn chốt lại 02/9/2026. Bỏ mọi cách ghi "kênh phụ"/"hoặc qua" Trung tâm Phục vụ hành chính công, bưu chính, trực tiếp, "Cổng DVCQG", "Hệ thống TTGQ TTHC tỉnh" trong hướng dẫn DN; trích luật thì ghi rõ là trích luật.

## [1.2.2] - 02/9/2026 — sửa theo scripts/check_facts.py (CI dữ kiện lỗi thời)
- Sửa các vi phạm do script quét: nơi nộp hồ sơ → motcua-tthc.moit.gov.vn; tiêu ngữ en dash trong mẫu; trỏ xp-hc-vlncn-sct-vn → xp-sct-vn; CN(M.Cường) trong mẫu → CN(Khôi), trong ví dụ lịch sử chú thích "lịch sử"; ký hiệu /GP-SCT bỏ chữ "dự kiến". Không đổi nghiệp vụ.

Nhật ký thay đổi của plugin (Quản lý nhà nước về hóa chất). Lịch sử trước 02/9/2026 xem CHANGELOG.md ở gốc repo (tìm theo tên plugin) và `git log -- hc-sct-vn/`.

## [1.2.1] - 02/9/2026 — khởi tạo CHANGELOG trong thư mục skill
- Rà soát tổng thể 02/9/2026: plugin đúng cấu trúc, description trong ngưỡng, không phát hiện dữ kiện lỗi thời cần sửa. Phiên bản giữ nguyên 1.2.1.
- Từ nay mỗi lần nâng cấp ghi mục mới lên đầu file này (theo CLAUDE.md của repo).
