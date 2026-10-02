# 09 — Áp dụng cho Sở Công Thương: KCN, CCN, dự án công nghiệp

## A. Vị trí của Sở trong chuỗi thu hồi đất

Theo Sổ tay, các chủ thể thực hiện là: UBND cấp xã, Chủ tịch UBND cấp xã, phòng chuyên môn cấp xã, đơn vị bồi thường, Hội đồng bồi thường, chủ đầu tư, MTTQ, Công an cấp xã, Văn phòng Đăng ký đất đai, Sở Nông nghiệp và Môi trường (thẩm định thiết kế kỹ thuật đo đạc, ký duyệt bản đồ địa chính, kiểm tra nghiệm thu). **Sổ tay không giao nhiệm vụ nào cho Sở Công Thương.**

Sở Công Thương gặp nội dung này ở các việc:
- tổng hợp tiến độ, khó khăn GPMB các KCN, CCN trong báo cáo định kỳ, báo cáo NQ 34-NQ/TU, tài liệu họp UBND tỉnh (plugin `kccn-sct-vn`);
- rà điểm nghẽn GPMB của dự án công nghiệp động lực (plugin `dacn-sct-vn`);
- tham mưu thông báo kết luận, công văn đôn đốc, trong đó có nhiệm vụ GPMB giao cho UBND cấp xã, chủ đầu tư;
- trả lời chủ đầu tư hạ tầng CCN, nhà đầu tư thứ cấp hỏi về trình tự;
- hồ sơ có điều kiện về đất (quyết định thuê đất trong hồ sơ giấy phép sử dụng vật liệu nổ công nghiệp, điều kiện khởi công hạ tầng CCN).

## B. Đối chiếu chủ đầu tư hạ tầng KCN, CCN với Bước 1

| Chủ đầu tư phải có | Dùng để |
|---|---|
| Văn bản đề nghị thực hiện dự án gửi UBND cấp xã, kèm hồ sơ dự án (một trong các loại văn bản ở reference `02` mục E) | Mốc bắt đầu tính 10 ngày xây dựng kế hoạch thu hồi đất |
| Hợp đồng với đơn vị bồi thường | Xác định đơn vị lập kế hoạch, kiểm đếm, lập phương án |
| Bản vẽ vị trí, ranh giới, diện tích khu đất thu hồi | Hồ sơ thông báo thu hồi đất |
| Sản phẩm đo đạc, trích đo đã kiểm tra, nghiệm thu, ký duyệt | Hồ sơ thông báo thu hồi đất, hồ sơ thẩm định phương án |
| Kinh phí bồi thường, hỗ trợ, tái định cư | Chi trả trong 30 ngày kể từ ngày quyết định phê duyệt phương án có hiệu lực; chậm ứng thì chịu khoản chi trả chậm, tính vào chi phí đầu tư, không được khấu trừ vào tiền thuê đất |

Sổ tay không nêu riêng trường hợp quyết định thành lập cụm công nghiệp. Văn bản pháp lý của từng KCN, CCN cụ thể (quyết định thành lập, quyết định chấp thuận chủ trương đầu tư, giao chủ đầu tư): tra `kccn-sct-vn` (GATE trạng thái hồ sơ); việc văn bản đó có đủ làm căn cứ thu hồi đất hay không do UBND cấp xã, Sở Nông nghiệp và Môi trường xác định.

## C. Xác định "đang ở bước nào" từ một câu trong báo cáo

| Báo cáo ghi | Tương ứng | Việc kế tiếp và mốc |
|---|---|---|
| "đã ban hành kế hoạch thu hồi đất" | xong Bước 1 | họp dân, thông báo thu hồi đất (chuỗi 02 + 02 + 02 ngày) |
| "đã ban hành thông báo thu hồi đất" | xong Bước 3 | kiểm đếm; đồng hồ 60 ngày hoặc 120 ngày bắt đầu chạy từ ngày gửi; thông báo hết hiệu lực sau 12 tháng |
| "đang kiểm đếm", "đang kiểm kê", "đã kiểm đếm … ha" | Bước 4 | xác nhận nguồn gốc đất song song; lập phương án |
| "đang lập phương án", "đã lập phương án … hộ" | Bước 5 | niêm yết 10 ngày |
| "đang niêm yết, lấy ý kiến" | Bước 6 | đối thoại trong 30 ngày; trình thẩm định |
| "đang thẩm định phương án" | Bước 7 | không quá 30 ngày làm việc; phê duyệt không quá 05 ngày làm việc |
| "đã phê duyệt phương án … ha, … tỷ đồng" | xong Bước 7 | gửi quyết định (05 ngày làm việc); chi trả (30 ngày); quyết định thu hồi đất (10 ngày) |
| "đã chi trả … tỷ đồng cho … hộ" | Bước 9 | quyết định thu hồi đất, nhận bàn giao |
| "đã thu hồi … ha", "đã có quyết định thu hồi đất" | xong Bước 10 | vận động bàn giao (Bước 11) |
| "mặt bằng sạch … ha", "đã bàn giao … ha" | xong Bước 11 | quản lý quỹ đất; giao đất, cho thuê đất (ngoài phạm vi Sổ tay) |
| "còn … hộ chưa nhận tiền", "chưa bàn giao" | Bước 9 hoặc 11 | vận động 10 ngày; gửi tiền vào tài khoản; cưỡng chế nếu đủ điều kiện |

"Đã GPMB" là cách nói gộp, không phải một bước của quy trình: khi tổng hợp phải tách diện tích đã phê duyệt phương án, đã chi trả, đã có quyết định thu hồi đất, đã bàn giao (mặt bằng sạch). Số liệu nào xã, chủ đầu tư không tách thì ghi đúng như báo cáo, không tự quy đổi.

## D. Mẫu câu cho văn bản của Sở

- Giao việc: "Đề nghị Ủy ban nhân dân xã … đẩy nhanh việc thẩm định, phê duyệt phương án bồi thường, hỗ trợ, tái định cư đối với … ha còn lại của Cụm công nghiệp …; tổ chức vận động các hộ chưa nhận tiền bồi thường, chưa bàn giao mặt bằng."
- Với chủ đầu tư: "Đề nghị Công ty … bảo đảm kinh phí bồi thường, hỗ trợ, tái định cư theo phương án đã được phê duyệt; phối hợp với Ủy ban nhân dân xã …, đơn vị, tổ chức thực hiện nhiệm vụ bồi thường, hỗ trợ, tái định cư trong kiểm đếm, chi trả."
- Với Sở Nông nghiệp và Môi trường: "Đề nghị Sở Nông nghiệp và Môi trường hướng dẫn Ủy ban nhân dân xã … tháo gỡ vướng mắc về xác định nguồn gốc đất, …".
- Nêu vướng mắc: ghi số hộ, diện tích, lý do theo báo cáo của xã; không viết "do xã chậm" khi báo cáo không nêu.

Không viết: "Sở Công Thương chỉ đạo UBND xã thu hồi đất"; "đề nghị UBND tỉnh ban hành quyết định thu hồi đất" đối với trường hợp thẩm quyền đã thuộc Chủ tịch UBND cấp xã (reference `02` mục B); "theo Sổ tay của Sở Nông nghiệp và Môi trường" ở phần căn cứ.

## E. Câu hỏi nên đặt cho xã, chủ đầu tư khi số liệu chưa rõ

1. Thông báo thu hồi đất ban hành ngày nào, còn hiệu lực đến ngày nào?
2. Diện tích đã kiểm đếm, đã lập phương án, đã phê duyệt phương án, đã chi trả, đã có quyết định thu hồi đất, đã bàn giao — mỗi mốc bao nhiêu ha, bao nhiêu hộ, tổ chức?
3. Trong phần còn lại có đất ở (mốc 120 ngày), có bố trí tái định cư không; khu tái định cư đã có chưa?
4. Số hộ còn vướng thuộc tình huống nào (reference `07`): tranh chấp, thế chấp, thừa kế, vắng chủ, không đồng ý giá?
5. Đã ban hành quyết định kiểm đếm bắt buộc, quyết định cưỡng chế nào chưa?
6. Chủ đầu tư đã chuyển đủ kinh phí bồi thường theo phương án đã phê duyệt chưa?
