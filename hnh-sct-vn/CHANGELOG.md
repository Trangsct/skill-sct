# CHANGELOG — hnh-sct-vn

## [1.11.0] - 04/9/2026
- **Ví dụ thực tế mới** `vi-du-thuc-te/soi-phuong-nam-canxi-hypoclorit-loai5-092026/`: **bộ hồ sơ mẫu chuẩn đầu tiên của nhóm LOẠI 5** và là **mẫu riêng của Chi nhánh số 1 - Công ty cổ phần Xuất nhập khẩu Sợi Phương Nam** (đơn vị nộp hồ sơ thường xuyên, vụ thứ ba trong năm 2026 sau Argon lỏng và NH3 khan). Gồm 04 tệp doanh nghiệp (Giấy đề nghị, Bảng kê phương tiện, Bảng kê người lái xe và người áp tải, Phương án tổ chức vận chuyển) cho canxi hypoclorit khô UN 1748 và canxi hypoclorit ngậm nước UN 2880 (loại 5, nhóm 5.1, số hiệu nguy hiểm 50), hàng đóng thùng nhựa 50 lít xếp trong công-ten-nơ 40 feet trên tổ hợp đầu kéo Ngạc J0H466 - sơ mi rơ moóc Ngạc J6657 biển Trung Quốc thuê theo Hợp đồng và Giấy ủy quyền cùng số 2026-001 ngày 01/8/2026; tuyến trong phạm vi 500 m khu vực cửa khẩu quốc tế đường bộ số II Kim Thành. Kèm **công văn hoàn thiện, bổ sung hồ sơ** của Sở và README nêu 09 lỗi đã sửa.
- **Reference 16 mục 10 mới:** nhận dạng vụ việc loại 5; **các lỗi lặp lại của Chi nhánh số 1 Sợi Phương Nam** (hợp đồng song ngữ còn nguyên nội dung bộ hồ sơ trước - vụ 9/2026 phần tiếng Trung vẫn ghi amoniac khan và tuyến Tằng Loỏng; khối lượng ghi tổng số tấn không rõ mốc tính; Phương án sao chép bộ cũ; số điện thoại không thống nhất); 03 điểm nghiệp vụ mới (đọc riêng "tổng trọng lượng kéo theo" của đầu kéo và "trọng tải theo quy định" của sơ mi rơ moóc trên giấy tờ xe Trung Quốc; đối chiếu phạm vi kinh doanh trên Chứng nhận vận tải đường bộ Trung Quốc với loại hàng đề nghị, làm căn cứ thực tế cho Điều 13 Nghị định thư Việt - Trung; phần chữa cháy riêng cho chất oxy hóa 5.1 - dùng nhiều nước, cấm bột khô, CO2, bọt gốc hữu cơ và chất chứa amoni); **quy tắc bôi đỏ** bản hồ sơ Sở dựng giúp trước khi giao doanh nghiệp tự hoàn thiện.
- Cập nhật SKILL.md mục IV-a (mô tả thư mục ví dụ mới) và mô tả reference 16 tại mục IV.
- Nâng version plugin lên 1.11.0; bổ sung bộ hồ sơ mẫu loại 5 vào mô tả plugin.

## [1.6.0] - 26/7/2026
- **Nguyên tắc 18 (SKILL.md) + reference 16 mục 8.1 + reference 11 lỗi 13:** cột "Khối lượng vận chuyển" của Danh mục kèm Giấy phép phải chọn theo DẠNG CHỨA HÀNG. Câu "Theo thiết kế của phương tiện" chỉ đúng với xi téc/bồn gắn cố định; hàng bao gói (chai, bình, phuy, can) trên xe tải, xe có mui thì không có "thiết kế" để dẫn chiếu. **Cách ghi chốt cho MỌI Giấy phép từ nay: "Theo giấy tờ của phương tiện"** (Bạn quyết 26/7/2026). Bắt buộc đọc mục "Thông tin về phương tiện" của Phương án trước khi điền cột này.
- **Nguyên tắc 19 + reference 16 mục 8.2 + reference 11 lỗi 14:** doanh nghiệp nộp nhiều bộ hồ sơ cùng đợt phải soát chéo 04 tiêu chí giữa các Giấy phép (cột khối lượng; cỡ chữ dòng "(Kèm theo Giấy phép... Số: .../GP - SCT...)" kế thừa 14pt, không để cứng 13pt; cấu trúc cột Ghi chú; thời hạn) và render soi hai bản cạnh nhau. Kiểm GCN tập huấn của lái xe, người áp tải có phủ đủ tất cả loại hàng của các bộ không.
- **Reference 16 mục 8.3 + reference 11 lỗi 15:** đọc NIÊN HẠN SỬ DỤNG từ đủ 03 nguồn (Giấy đề nghị; Chứng nhận đăng ký xe dòng "Giá trị đến ngày"; GCN kiểm định dòng "Niên hạn sử dụng" chỉ ghi năm) - thường lệch nhau; khi phải khống chế thời hạn thì lấy mốc sớm nhất từ giấy tờ gốc.
- **Reference 16 mục 8.4:** nhóm sai lệch nhỏ chỉ ghi Biên bản, không là căn cứ từ chối và không nêu trong công văn gửi doanh nghiệp (số điện thoại lệch giữa GCN ĐKDN và Đơn; GCN tập huấn ghi sai nghề nghiệp/tên đơn vị; kiểm định hết hạn sớm hơn thời hạn Giấy phép).
- **Reference 16 mục 8.5 + reference 10 + reference 11 lỗi 16:** cột (4) "Loại, nhóm hàng" của Phụ lục I ghi số LOẠI ("2"), con số "2.1" là cột (5) nhãn hiệu, biểu trưng - không bê "Loại 2, nhóm 2.1" từ Giấy đề nghị của DN vào Giấy phép.
- **Ví dụ thực tế mới** `vi-du-thuc-te/tien-anh-lpg-xangdau-072026/`: 02 Giấy phép bản chốt của Công ty TNHH MTV thương mại Tiến Anh (LPG loại 2 dạng chai chứa; xăng + dầu diesel loại 3 trên tổ hợp xi téc) kèm README bài học. Bổ sung tiền lệ vào bảng reference 16 mục 1 và mô tả thư mục vào SKILL.md mục IV-a.
- Cập nhật mục 2 reference 16: cách ghi cột khối lượng hiện hành là "Theo giấy tờ của phương tiện"; các bản đã phát hành trước đó giữ nguyên trong hồ sơ lịch sử, không dùng lại cho Giấy phép mới.

## [1.5.1] - 24/7/2026
- Bổ sung **Mẫu 6 - Biên bản thẩm định hồ sơ cấp Giấy phép (nội bộ Sở)** vào `mau-ho-so/`: bản chuẩn văn phong 24/7/2026 từ vụ NH3 khan (Công ty CP thương mại vận tải và tư vấn kỹ thuật, 05 tổ hợp xe biển Việt Nam), đã lược các phát hiện tồn tại riêng của vụ việc để dùng làm mẫu chung. Cập nhật danh mục biểu mẫu trong `00-huong-dan-lap-ho-so.md` và mô tả `mau-ho-so/` trong SKILL.md (mục IV).
- Ghi chú sử dụng: khi dùng cho vụ mới (Chế độ B) thay toàn bộ thông tin doanh nghiệp/phương tiện/nhân sự, cập nhật tên thành viên Đoàn theo phân công hiện hành; tồn tại phát hiện ghi vào điểm a-đ tương ứng và tổng hợp tại mục nhận xét, kiến nghị.

## [1.4.0] - 23/7/2026
- Bản chốt GP Argon 2 xe (Chi nhánh số 1 Sợi Phương Nam) thay vào vi-du-thuc-te/soi-phuong-nam-argon-nh3-072026/GP-SoiPhuongNam-Argon-loai2-2xe.docx.
- Nguyên tắc 14 mới + reference 16 mục 6.6: cột trọng tải bảng phương tiện khi số liệu DN kê không khớp giấy tờ gốc → tiêu đề "Trọng tải được phép chở", từng dòng "Theo giấy tờ của phương tiện"; bài học đầu kéo 25.000 kg (tổng trọng lượng) ≠ khối lượng kéo theo (40.000 kg) ≠ trọng tải chở (= 0).
- Tinh chỉnh nguyên tắc 11 + reference 16 mục 6.4: mệnh đề "nhưng không vượt quá ngày [niên hạn]" CHỈ viết khi niên hạn rơi TRONG thời hạn GP tính từ ngày ký dự kiến; vụ Argon ký 7/2026 + 24 tháng < niên hạn 23/8/2028 nên bỏ mệnh đề, chốt "24 tháng kể từ ngày ký./."; không viết "kể từ ngày ký ban hành".
- Ghi nhận lỗi soát bản DN nộp lại: viết hoa sai giữa câu; mâu thuẫn thời hạn kiểm định Vân A4488 (08/2026 vs 06/2027, bồn 06/5/2027) - ghi Biên bản thẩm định, không đưa vào GP.

## [1.3.0] - 22/7/2026
- Vụ 02 bộ hồ sơ Chi nhánh số 1 Sợi Phương Nam (Argon lỏng UN 1951 + NH3, xe biển Trung Quốc): mẫu Biên bản thẩm định chuẩn mới (địa điểm tại trụ sở DN, bảng ký ĐẠI DIỆN đơn vị + TRƯỞNG ĐOÀN, cột niên hạn sử dụng, bỏ "tối thiểu" ở nhận xét phương án) — nguyên tắc 12 SKILL.md, reference 16 mục 6.1.
- Kiểm định BỒN chứa tách riêng kiểm định XE với tổ hợp bồn biển TQ; không ghi thông số hồ sơ đang mâu thuẫn vào văn bản của Sở — nguyên tắc 13, reference 16 mục 6.2, reference 11 lỗi 10-12.
- Hàng mới Argon chất lỏng làm lạnh (UN 1951, nhóm 2.2, SHNH 22) — reference 16 mục 6.3.
- Cách viết thời hạn GP có chốt niên hạn: "24 tháng kể từ ngày ký nhưng không vượt quá ngày [niên hạn]./." — reference 16 mục 6.4.
- CV hướng dẫn hoàn thiện CHUNG cho nhiều bộ hồ sơ; ranh giới không yêu cầu vượt Điều 15 — reference 16 mục 6.5.
- 6 ví dụ thực tế mới tại vi-du-thuc-te/soi-phuong-nam-argon-nh3-072026/.

## [1.1.2] - 15/7/2026
- Bạn chốt: **toàn bộ HHNH → CN(Linh)** từ 15/7/2026 (cả thụ lý cấp GP vận chuyển lẫn an toàn/tập huấn); giai đoạn 6/7–14/7/2026 giữ CN(Khôi) đúng lịch sử.

## [1.1.1] - 14/7/2026
- Bổ sung ghi chú theo Thông báo phân công nội bộ Phòng QLCN 10/7/2026: an toàn - kiểm tra - tập huấn HHNH thuộc CV Vũ Việt Linh; thụ lý cấp GP vận chuyển HHNH thực tiễn CN(Khôi), kiểm duyệt nội bộ PTP Trần Trọng Trang; điểm mở cần xác nhận với Bạn.
