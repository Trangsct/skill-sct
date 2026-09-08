# 17 — Sở tham gia Hội đồng thẩm định Kế hoạch phòng ngừa, ứng phó sự cố hóa chất do Cục Hóa chất chủ trì (Phiếu Mẫu 03c)

Đúc kết từ phiên thẩm định 08/9/2026: Kế hoạch điều chỉnh của Công ty Cổ phần DAP số 2 - Vinachem (KCN Tằng Loỏng). Chuyên viên Nguyễn Thị Loan là thành viên Hội đồng thẩm định do Cục Hóa chất mời; PTP Trần Trọng Trang rà soát hồ sơ, dựng Phiếu nhận xét. Reference này bổ sung cho ref 06 (thẩm định KH do UBND tỉnh chủ trì) một nghiệp vụ khác: **Sở là thành viên Hội đồng của Cục** đối với cơ sở thuộc điểm a khoản 2 Điều 33 NĐ 25/2026.

## 1. Khi nào Sở là thành viên chứ không phải cơ quan thẩm định

| Đối tượng (khoản 2 Điều 33 NĐ 25/2026) | Cơ quan thẩm định, phê duyệt | Vai trò Sở |
|---|---|---|
| Điểm a — có ≥ 01 chất Bảng A / hỗn hợp Bảng B Phụ lục IV NĐ 24/2026 đạt ngưỡng riêng lẻ | **Bộ Công Thương — Cục Hóa chất** (điểm c khoản 6 Điều 34 NĐ 25; khoản 3 Điều 4 TT 02/2026) | Thành viên Hội đồng theo mời của Cục; lập **Phiếu nhận xét, đánh giá Mẫu 03c** Phụ lục III TT 02/2026; tham gia kiểm tra thực tế (Mẫu 03đ) |
| Điểm b — tổng tỉ lệ q/Q ≥ 1, không chất nào đạt ngưỡng riêng lẻ | **UBND cấp tỉnh** (Sở tham mưu, ref 06) | Cơ quan thẩm định |

Cách xác định nhanh: mở Bảng 1.6 (bản kê khai hóa chất) của Kế hoạch, đối chiếu từng chất với Bảng A Phụ lục IV NĐ 24/2026. Ví dụ DAP số 2: NH3 khan 5.700 tấn so với ngưỡng 50.000 kg (số thứ tự 7 Bảng A) → điểm a → Cục. **Lưu ý Bảng A KHÔNG có H2SO4 (chỉ có oleum), H3PO4, H2SiF6, NaOH, lưu huỳnh rắn** — cơ sở axit lớn chỉ thuộc đối tượng KH khi có chất khác (thường là NH3) hoặc qua tổng tỉ lệ.

## 2. Phiếu Mẫu 03c — cấu trúc và cách điền

Bố cục theo TT 02/2026: (1) Tên cơ quan phê duyệt = **BỘ CÔNG THƯƠNG** / HỘI ĐỒNG THẨM ĐỊNH; (2) địa danh = **Hà Nội** (nơi cơ quan phê duyệt đặt trụ sở); (3) tên dự án/cơ sở; (4) tổ chức chủ quản; mục 1 thông tin kế hoạch; mục 2 người nhận xét (họ tên, chức vụ, cơ quan); mục 3 ba ô lựa chọn — **để trống, thành viên tự ký vào ô đã chọn**, không tự đánh X (quy tắc vbhc-vn Nhóm G); mục 4.1 nội dung đạt yêu cầu; mục 4.2 nội dung cần chỉnh sửa, bổ sung; ký tên.

Quy ước trình bày đã chốt (08/9/2026): dựng trên chính file Mẫu 03c (Chế độ B), khổ A4 lề 2-2-3-2, header 13pt có **2 đường Line shape** (dưới HỘI ĐỒNG THẨM ĐỊNH và dưới tiêu ngữ), thân 14pt lùi 1 cm căn đều, công thức hóa học chỉ số dưới, m2/m3 số mũ, đề mục 4.2 đánh số 4.2.1 … 4.2.n in đậm, khối ký ghi sẵn tên người nhận xét. Script dựng sẵn: `vi-du-thuc-te/ke-hoach-su-co/build_phieu_03c.py` (đọc `Mau-03c-goc.docx` + `line_runs.txt` trong cùng thư mục, sửa hai danh sách `DAT`/`SUA` rồi chạy; render soi từng trang trước khi giao). Bản mẫu đã hoàn thiện: `2026.09.08. Phieu-nhan-xet-Mau-03c-KH-su-co-DAP-so-2.docx`.

Ngày tháng để trống (điền ngày họp); dòng Chức vụ ghi chức vụ chuyên môn, chỉ thêm vai trò trong Hội đồng (ủy viên/ủy viên phản biện) khi có QĐ thành lập Hội đồng của Cục.

## 3. Checklist thẩm định nội dung Kế hoạch (đối chiếu Phụ lục II TT 02/2026 + khoản 3 Điều 33 NĐ 25/2026)

1. **Hồ sơ:** văn bản đề nghị Mẫu 03a + 09 bản KH (khoản 1 Điều 34); thông tin pháp lý trong văn bản đề nghị phải khớp tài liệu kèm (lần đăng ký thay đổi, ngày cấp GCN ĐKDN).
2. **Đối tượng, thẩm quyền:** KH phải có bảng đối chiếu từng hóa chất với ngưỡng Phụ lục IV; khối lượng là hóa chất thực (không quy đổi P2O5, không quy đổi 100%), thống nhất giữa phần Mở đầu, Bảng 1.6 và Bảng 1.7; kiểm tra chéo dung tích bồn × tỷ trọng.
3. **Căn cứ pháp lý:** khung 2026 (Luật 69/2025; NĐ 24/25/26/2026; TT 01/02-2026; QCVN 05A SĐ1:2024); rà ký hiệu văn bản khác (môi trường, ATVSLĐ, PCCC) — nhiều KH sao chép bản cũ.
4. **KH điều chỉnh** (khoản 3, 4 Điều 36): mọi hạng mục mới phải xuất hiện đủ ở **cả 4 chỗ**: Bảng 1.2 hạng mục công trình → Bảng 2.1 điểm nguy cơ (kèm điều kiện công nghệ, số người) → Bảng 2.2 tình huống + mô phỏng → mục 4.3 biện pháp theo khu vực + kịch bản diễn tập Chương 3. Lỗi điển hình DAP số 2: trạm xuất chỉ có ở Bảng 1.2 và Bảng 2.2, vắng ở Bảng 2.1 và mục 4.3.
5. **Mô phỏng ALOHA:** số liệu vùng AEGL trong bảng tổng hợp phải khớp mục mô phỏng; ngưỡng AEGL phải là bộ giá trị 60 phút (NH3: AEGL-1/2/3 ≈ 30/160/1.100 ppm) — DAP số 2 ghi 1.100/2.700/5.000 ppm là sai bộ ngưỡng; yêu cầu thuyết minh thông số khí tượng, cấp ổn định khí quyển, điều kiện nguồn (pha lỏng/khí, nhiệt độ, áp suất). Axit ăn mòn không bay hơi: không được chỉ ghi "cách ly 50 m", phải tính lượng tràn lớn nhất và khả năng thu gom.
6. **Bố cục bắt buộc thường thiếu:** phần Kiến nghị và cam kết của chủ đầu tư; Phụ lục bản vẽ A3 in màu (vị trí, tổng mặt bằng, vị trí lưu trữ + trạng thái bảo quản, thoát hiểm, mặt bằng thiết bị + khối lượng hóa chất tại thiết bị chính).
7. **Phối hợp ngoài hàng rào:** với cơ sở trong KCN Tằng Loỏng — đánh giá sự cố dây chuyền sang cơ sở liền kề, cảnh báo ra ngoài hàng rào, quy chế phối hợp bằng văn bản với DN liền kề + BQL Khu kinh tế + UBND xã + Cảnh sát PCCC&CNCH; danh bạ khẩn cấp có Sở Công Thương, UBND xã, Sở NN&MT.
8. **Nghĩa vụ sau phê duyệt:** cập nhật CSDL quốc gia trong 30 ngày (điểm c khoản 5 Điều 34); diễn tập hằng năm + báo cáo Mẫu 04 Phụ lục IV TT 02 (khoản 2 Điều 36); hạng mục thay đổi chỉ vận hành sau khi phê duyệt (khoản 8 Điều 36).

## 4. Điều kiện an toàn trạm xuất, đường ống — nội dung Sở yêu cầu bổ sung (dùng lại cho cơ sở tương tự)

**Trạm xuất NH3 lỏng (bồn cầu 0-10°C, ~0,5-0,6 MPa):** sơ đồ công nghệ trạm xuất (bơm/máy nén, đường xuất lỏng, đường hồi hơi cân bằng áp); van chặn khẩn cấp đóng nhanh đầu ống xuất + trên tuyến, kích hoạt từ DCS và tại chỗ; van an toàn xả áp cho đoạn ống lỏng có thể bị cô lập giữa hai van (giãn nở nhiệt); khớp nối chống bung / ống mềm có van tự đóng; chèn bánh + khóa liên động không cho xe nổ máy khi đang nạp; đo mức/cân/lưu lượng kế liên động ngắt quá đầy; nối đất, chống tĩnh điện; đầu dò NH3 liên động dừng bơm, đóng van; giàn phun mưa phủ kín khu xuất; thiết bị điện phòng nổ; PPE (mặt nạ, bình khí thở) đặt ngược gió; phiếu kiểm tra trước-trong-sau khi bơm, người giám sát thường trực; kiểm định thiết bị áp lực và đo chiều dày ăn mòn tuyến ống mới định kỳ.

**Trạm xuất axit (H2SO4 98%, H3PO4, H2SiF6) và NaOH:** hệ thống thu gom ≥ 110% dung tích phương tiện chứa lớn nhất (điểm 9.1.1, 10.1.7, 11.2 QCVN 05A SĐ1:2024) — tính theo xe bồn lớn nhất được phép nhận hàng, nêu số xe đồng thời; rửa mắt + tắm khẩn cấp ≤ 17 m (điểm 5.9); vật liệu: H2SO4 98% thép cacbon, H3PO4/H2SiF6 thép không gỉ, nhựa, thép lót cao su, **không dùng thủy tinh/gốm silicat với H2SiF6**; vôi bột/soda trung hòa, vật liệu thấm hút tại chỗ; hình đồ cảnh báo Phụ lục A QCVN 05A SĐ1:2024; **không phun nước trực tiếp vào vũng H2SO4 đặc**.

**Kịch bản diễn tập cần có tại trạm xuất:** rò rỉ tại khớp nối ống mềm; đứt ống mềm khi xe di chuyển; quá đầy xe bồn. DAP số 2 có 09 kịch bản nhưng không có kịch bản nào tại trạm xuất NH3 (chỉ có nhập).

## 5. Câu hỏi thường gặp: điều chỉnh KH có liên quan gì đến đầu tư, xây dựng, PCCC, môi trường?

Bốn nhóm thủ tục độc lập, không thay thế nhau; thẩm định KH không miễn trừ thủ tục nào. Khi cơ sở bổ sung trạm xuất để **bán hóa chất ra ngoài**:
- **Đầu tư:** bổ sung sản phẩm/hoạt động kinh doanh hóa chất so với mục tiêu "sản xuất DAP" → rà điều chỉnh chủ trương đầu tư/GCN ĐKĐT (cơ quan: BQL Khu kinh tế tỉnh với KCN vùng Lào Cai cũ); quy hoạch chi tiết 1/500 (DAP số 2 đã có QĐ 111/QĐ-BQL 09/7/2026).
- **Xây dựng:** thẩm định thiết kế, GPXD/miễn, nghiệm thu, KTCTNT theo NĐ 207/2026 (plugin xd-sct-vn).
- **PCCC:** thẩm duyệt + nghiệm thu bổ sung cho trạm xuất, tuyến ống (NĐ 105/2025; plugin pccc-sct-vn). Hồ sơ DAP số 2 chỉ có tài liệu 2015/2019/2024 — thiếu.
- **Môi trường:** GPMT số 454/GPMT-BNNMT 24/10/2025 cấp trước khi bổ sung hạng mục → rà điều chỉnh GPMT (plugin bvmt-sct-vn).
- **Hóa chất (việc của Sở):** NH3, H3PO4, H2SiF6, NaOH, S thuộc **Phụ lục II** → GCN đủ điều kiện kinh doanh hóa chất có điều kiện (UBND tỉnh); **H2SO4 thuộc nhóm 2 Phụ lục III** (tiền chất công nghiệp) → **Giấy phép kinh doanh hóa chất cần kiểm soát đặc biệt** do UBND cấp tỉnh cấp (điểm a khoản 1 Điều 3 TT 01/2026) + phiếu kiểm soát mua bán trong 10 ngày (khoản 1 Điều 8 TT 01/2026) — ref 04.
- **Vận chuyển:** Giấy phép vận chuyển HHNH (NĐ 161/2024; plugin hnh-sct-vn) + Biện pháp phòng ngừa trong vận chuyển (khoản 3 Điều 35 NĐ 25) mang theo xe.
- **Điều kiện tiên quyết:** khoản 8 Điều 36 NĐ 25 — hạng mục thay đổi chỉ được đưa vào hoạt động sau khi KH được phê duyệt; nếu đã vận hành trước → ghi nhận vi phạm, chuyển plugin xp-sct-vn.

## 6. Hồ sơ vụ DAP số 2 (08/9/2026) — dữ kiện đã xác minh từ tài liệu

- Văn bản đề nghị số **1648/DAP2-KTh** (tháng 8/2026, ngày viết tay chưa rõ), Tổng Giám đốc Vũ Việt Tiến ký, gửi Cục Hóa chất; ghi GCN ĐKDN "thay đổi lần 12 ngày 07/7/2025" nhưng bản kèm là **lần 13 ngày 03/8/2026** (Phòng Doanh nghiệp, Sở Tài chính tỉnh Lào Cai) → yêu cầu chỉnh.
- KH cũ được Bộ Công Thương phê duyệt tại QĐ 2054/QĐ-BCT ngày 09/3/2015 (theo KH nêu, chưa đối chiếu bản gốc).
- Lý do điều chỉnh: bổ sung hệ thống đường ống và trạm xuất NH3, H3PO4, H2SO4, H2SiF6; căn cứ điểm a khoản 3 Điều 36 NĐ 25/2026 — đúng.
- Khối lượng tồn trữ lớn nhất kê khai: S 16.000 t; NH3 5.700 t (2 bồn cầu 5.000 m3, vận hành 4.590 m3/bồn); H2SO4 10.000 t (2 bồn 3.010 m3 → ~11.000 t, lệch); H3PO4 2.900 t (ghi quy đổi P2O5 — sai cách kê); H2SiF6 290 t; NaOH 13 t; Na2SO4 745, Na2CO3 5, Na2SiF6 750 (thiếu đơn vị).
- Mô phỏng: rò bồn 1,5 cm → AEGL-3 340 m / AEGL-2 960 m / AEGL-1 2.270 m; vỡ ống 6 cm → 2,2 km / 6,1 km / 10 km; nổ bồn → 1.246 / 1.609 / 2.574 m; xuất nhập xe bồn (isotank 20 m3, lỗ 1,5 cm) → 190 / 550 / 1.310 m. Bảng 2.1, 2.2 ghi 121/170/277 m và 288 m — mâu thuẫn.
- Kết luận Sở đề xuất: **Đồng ý thông qua nhưng yêu cầu chỉnh sửa, bổ sung** (10 nhóm nội dung tại Phiếu 03c mẫu).
- Ranh giới phối hợp: DAP số 2 giáp Chi nhánh Luyện đồng Lào Cai, Nhà máy Tuyển Tằng Loỏng; khu xử lý Gyps giáp thôn Hà Hợp; danh bạ KH đã có Công an xã Tằng Loỏng, BQL Khu kinh tế, BVĐK số 2.

## 7. Liên kết

ref 06 (KH do tỉnh thẩm định), ref 04 (nhóm 2, phiếu kiểm soát), ref 12 (danh mục), ref 16 (thực tiễn); plugin `vbhc-vn` (thể thức, không tự đánh X), `hnh-sct-vn`, `pccc-sct-vn`, `bvmt-sct-vn`, `xd-sct-vn`, `kccn-sct-vn`, `xp-sct-vn`.
