# CHANGELOG — sd-vlncn-sct-vn

## v1.0 — 04/7/2026
Phát hành lần đầu. Plugin cấp Giấy phép sử dụng VLNCN + phê duyệt Phương án nổ mìn (PANM), Sở Công Thương tỉnh Lào Cai — tiếp nối plugin kho-vlncn-sct-vn.

- **SKILL.md**: 5 nghiệp vụ (thẩm định cấp/điều chỉnh/cấp lại/thu hồi GP; thẩm định PANM trình Chủ tịch UBND tỉnh; hướng dẫn DN; kiểm tra - xử phạt; báo cáo); bảng thẩm quyền sau TT 38/2025 (UBND cấp tỉnh cấp GP, thực tiễn Chủ tịch ký KT. PCT Nguyễn Thành Sinh /GP-UBND); quy trình lõi A (cấp GP 7 bước) + B (PANM 5 bước); 10 anti-error.
- **references/** 7 file: 01 pháp lý (Luật 42/2024 Đ38-40, Luật 118/2025, NĐ 181/2024, NĐ 146/2025, TT 23/2024 + TT 38/2025, QCVN 01:2019/BCT, NĐ 71/2019 + 17/2022); 02 quy trình cấp GP + checklist thẩm định + cấp lại/điều chỉnh/thu hồi; 03 PANM (cây quyết định 2 chế độ, công thức Rc/rs/Rđv, quy trình 8 bước, hộ chiếu nổ mìn); 04 hướng dẫn DN A→Z + FAQ; 05 kiểm tra - xử phạt (bảng Đ56 và các điều liên quan, thẩm quyền, quy trình); 06 chế độ báo cáo (18/6-18/12, 30/6-30/12, đột xuất 24h/48h, cấu trúc Mẫu 03); 07 index ví dụ + bài học vụ việc.
- **mau-van-ban/** 15 mẫu: GP mỏ + GP công trình; tờ trình cấp GP; QĐ điều chỉnh; QĐ thu hồi; phiếu trình; tờ trình PANM; CV lấy ý kiến; biên bản kiểm tra hiện trường; QĐ PANM (thuần + kèm chấp thuận); CV hoàn thiện hồ sơ; CV đôn đốc; VB báo cáo không thuộc diện; báo cáo định kỳ năm.
- **vi-du-thuc-te/** 23 văn bản thật Lào Cai 2025–2026 (đã dedup, tên chuẩn hóa ASCII): 6 GP + 1 QĐ điều chỉnh; 5 QĐ/dự thảo PANM; 3 tờ trình PANM; CV Vạn Thắng, Yên Thành, Đồng Khê, lấy ý kiến SXD, đôn đốc; báo cáo năm 2025; QĐ ủy quyền + phụ lục.

## v1.1 — 04/7/2026
Bổ sung theo yêu cầu "đầy đủ tài liệu sẵn sàng cho công việc":
- **van-ban-goc/** (8 file + INDEX.md): Luật 42/2024, NĐ 181/2024, TT 23/2024, TT 38/2025, NĐ 146/2025, NĐ 71/2019, NĐ 17/2022 (scan), ghi chú nghiệp vụ.
- **vi-du-thuc-te/** thêm 6 PDF ký thật: 2 Phiếu trình, Biên bản kiểm tra hiện trường Yên Thành 8/6/2026, PANM đầy đủ của DN (Duy Hiếu - Xuân Hòa), CV SCT tham gia ý kiến PANM, CV SXD phúc đáp.
- Chuyển sang đóng gói PLUGIN (.claude-plugin/plugin.json + skills/), bỏ định dạng .skill.

## v1.2 — 04/7/2026
Bổ sung bộ hồ sơ KIỂM TRA CHUYÊN NGÀNH sau cấp phép (đợt kiểm tra thật 3/2026, 3 đơn vị/5 công trình):
- vi-du-thuc-te/: QĐ 1050/QĐ-SCT thành lập đoàn (pdf+txt), KH 1105/KH-ĐKT (pdf+txt), BC 1883/ĐKT-SCT (docx), TB 1894/TB-SCT (docx + pdf bản ký).
- mau-van-ban/: 4 mẫu mới 16-19 (QĐ kiểm tra chuyên ngành NĐ 217/2025; Kế hoạch của Đoàn; Báo cáo kết quả; Thông báo kết quả sau kiểm tra).
- references/05: thêm mục F — chuỗi kiểm tra 6 bước thực tế (QĐ → KH → QĐ phê duyệt KH → kiểm tra ≤10 ngày → BC → TB) + điểm nghiệp vụ (thời hiệu từ GP/Thông báo nổ mìn; đối chiếu 3 lớp Qmax GP↔PANM↔hộ chiếu; ký hiệu ĐKT-SCT/KH-ĐKT).
