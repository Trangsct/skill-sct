# Chế độ cập nhật định kỳ tiến độ KCN/CCN và quy tắc dùng skill làm nguồn hiện trạng

Chuyển từ bộ ghi nhớ cá nhân của người dùng sang skill ngày 08/9/2026. Đọc ref này trước khi trả lời bất kỳ câu hỏi nào về hiện trạng (tỷ lệ lấp đầy, nhà đầu tư, tiến độ, mốc khởi công, số doanh nghiệp) của KCN, CCN.

---

## 1. Nhịp cập nhật: 02 kỳ mỗi tuần, khác nhau về cách làm

- Nhiệm vụ định kỳ do Giám đốc Sở Hoàng Chí Hiền giao ngày 06/9/2026 (nhóm Zalo "NHÓM CCN LCI NEW"): Phòng QLCN cập nhật bộ sản phẩm tiến độ KCN, CCN và báo cáo Lãnh đạo Sở hằng tuần.
- Người dùng làm rõ ngày 08/9/2026, plugin được làm mới 02 lần mỗi tuần:

| Kỳ | Ai làm | Nguồn | Sản phẩm |
|---|---|---|---|
| THỨ 4 | Dây chuyền TỰ ĐỘNG Data360X (bot Playwright trên máy cơ quan kết xuất sổ văn bản đến/đi từ https://csdlvb.laocai.gov.vn → GitHub Actions gọi Claude API bóc trường → cập nhật trang congnghieplaocai.vn và file tham chiếu plugin; trường hợp chưa chắc thì mở PR chờ người dùng duyệt) | Sổ văn bản Data360X | Diễn biến tuần được ghi vào reference kỳ cập nhật và dữ liệu web; KHÔNG làm bộ 04 file Excel, KHÔNG gửi Zalo |
| THỨ 6 | Người dùng + Claude trong phiên làm việc (thủ công, có kiểm tra) | Sổ văn bản Data360X từ ngày chốt kỳ trước + hồ sơ nhà đầu tư + xác nhận của người dùng | Bộ 04 file Excel + tin Zalo báo cáo Giám đốc; ghi reference kỳ mới; push repo |

- Vì kỳ thứ 4 là máy tự chạy: khi đọc reference do kỳ thứ 4 tạo ra, kiểm tra có PR nào của bot còn treo (chưa merge) hay không trước khi coi là hiện trạng; diễn biến nằm trong PR treo chưa được tính.
- Mỗi kỳ ghi thành một reference mới đánh số tiếp theo (33, 34...) với tên `NN-ky-cap-nhat-DD-M-YYYY.md`, theo đúng khung mục A-I của ref 30; file sản phẩm (kỳ thứ 6) lưu vào `vi-du-thuc-te/`; cập nhật CHANGELOG, plugin.json và push repo ngay trong phiên.

## 2. Bộ 04 sản phẩm mỗi kỳ (chi tiết mẫu và quy tắc: ref 30 mục E, F, G, H)

1. Biểu tiến độ dự kiến các dự án KCN, CCN thành lập, khởi công, hoàn thành năm 2026: Mông Sơn dòng đầu; CCN chia 4 nhóm; 11 cột; không ô trống; không ghi chú nội bộ; A3 ngang.
2. Danh mục thu hút đầu tư các CCN đến năm 2030 (theo QĐ 1382): mỗi kỳ thêm sheet ngày mới đặt lên đầu, giữ các sheet cũ.
3. Danh mục thu hút đầu tư KCN giai đoạn 2026-2030 (theo QĐ 1382): cùng cách làm.
4. Bảng tiến độ thành lập và triển khai đầu tư hạ tầng kỹ thuật CCN Mông Sơn (đến khi có QĐ thành lập thì chuyển trọng tâm sang QHCT 1/500, đất đai, GPMT).

Kèm tin Zalo 5 mục gửi Giám đốc, viết không markdown (mẫu ref 30 mục F).

Quy tắc file Excel áp dụng cho cả 4 sản phẩm: không tô màu nền, không freeze panes, chữ đủ lớn, lề A4 hoặc A3 theo biểu, recalc 0 lỗi, render soi trang trước khi giao.

## 3. Quy tắc dùng skill làm nguồn hiện trạng (thay quy tắc cũ "hiện trạng phải hỏi người dùng")

Vì plugin được cập nhật 02 lần mỗi tuần, số liệu ở REFERENCE KỲ CẬP NHẬT MỚI NHẤT được coi là hiện trạng đủ tin cậy để soạn văn bản, trả lời, tổng hợp. Cách làm:

1. Tìm reference kỳ cập nhật có ngày mới nhất (bảng reference trong SKILL.md, dòng đánh dấu "MỚI NHẤT" hoặc số thứ tự lớn nhất có tên `ky-cap-nhat`). Chỉ dùng kỳ đó; các kỳ cũ hơn (ref 17, 25, 26, 30...) là lịch sử.
2. Khi dùng số liệu, ghi rõ ngày chốt của kỳ ("cập nhật đến 06/9/2026") trong sản phẩm hoặc trong câu trả lời để người đọc biết độ mới.
3. Nếu ngày hiện tại cách ngày chốt kỳ mới nhất QUÁ 04 NGÀY (tức đã bỏ lỡ một kỳ thứ 4 hoặc thứ 6), hoặc câu hỏi liên quan đến việc có văn bản mới sau ngày chốt (Quyết định thành lập, kết quả họp Hội đồng, khởi công), thì nêu rõ số liệu đang dùng là của kỳ nào và hỏi người dùng có diễn biến mới không trước khi đưa vào văn bản trình ký.
4. Dữ kiện cứng (tên, địa điểm xã, diện tích quy hoạch, quyết định đã ban hành) lấy ở ref 12, 13, 14, 31; không lấy từ kỳ cập nhật vì kỳ cập nhật chỉ ghi diễn biến.
5. Tuyệt đối không cộng dồn, ước tính hay nội suy số liệu giữa hai kỳ; không tự "cập nhật thêm" tiến độ theo suy đoán thời gian.

## 4. Liên kết

- Dây chuyền tự động Data360X: mô tả kiến trúc 3 khâu ở sct-laocai-org-vn mục "Công cụ số và dây chuyền dữ liệu"; bản giao việc "2026.09.02. Bản giao việc Claude Code - Tự động cập nhật văn bản lên 2 trang web và skill.md".
- Ref 30: khung nội dung một kỳ cập nhật, mẫu tin Zalo, quy tắc trình bày, quy trình 5 bước.
- Ref 31: sổ chốt dữ kiện cứng.
- sct-laocai-org-vn: người ký (PGĐ Nguyễn Đình Chiến), chuyên viên CN(Trung), Trưởng phòng Nguyễn Hữu Long trực tiếp chỉ đạo CCN.
- vbhc-vn: thể thức file Word nếu cần chuyển thể báo cáo.
