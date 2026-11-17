# Sổ lỗi tự ghi — bvmt-sct-vn

Lỗi Bạn chỉ ra trong phiên, Claude ghi ngay theo CLAUDE.md mục "Tự ghi lỗi" (Bạn chốt 17/10/2026). Đọc tệp này trước khi
soạn văn bản thuộc lĩnh vực của plugin. Định dạng mỗi mục và cách kiểm: `scripts/check_anti_error_format.py` ở gốc kho.
Lỗi kiểm được bằng máy thì kèm quy tắc trong `qa_rules.py` (vbhc-vn) hoặc `check_facts.py` và ghi mã ở dòng "Máy kiểm".
Yêu cầu riêng cho MỘT văn bản không ghi ở đây mà ghi vào `trang-thai/<hồ sơ>.md` mục "Yêu cầu riêng một lần".

### L001 — 17/11/2026 — Chê báo cáo đề xuất GPMT nhóm III thiếu đánh giá, dự báo tác động
- Lỗi: Bản nhận xét GPMT một nhà máy phân bón trong khu công nghiệp đánh giá "Không đạt yêu cầu" vì Chương IV không có phần đánh giá, dự báo nguồn thải, và ghi "Không áp dụng" cho hiện trạng môi trường mà không dẫn căn cứ. Nguyên nhân: viết theo trí nhớ về mẫu cũ, chưa đọc Mẫu số 22c và Điều 18a.
- Cách đúng: trước khi nhận xét, xác định nhóm dự án rồi đọc Mẫu số 22c (`van-ban-goc/2026.01.29-09.2026.TT.BNNMT-Sua-doi-TT-02-2022-bao-ve-moi-truong.txt`). Dự án nhóm III KHÔNG phải thực hiện: Mục 1 Chương IV (đánh giá, dự báo tác động môi trường); điểm b, c Mục 1.1, điểm b Mục 1.2, điểm a Mục 2.1, Mục 2.3, 2.4, 3.2 Chương III; Chương V. Dự án trong khu sản xuất, kinh doanh, dịch vụ tập trung, cụm công nghiệp không phải đánh giá (nhóm II) hoặc mô tả (nhóm III) hiện trạng môi trường — điểm c khoản 2 Điều 18a Thông tư 02/2022/TT-BTNMT, bổ sung tại Điều 9 Thông tư 09/2026/TT-BNNMT. Với nhóm III, các dòng 4, 4.1, 4.2 của Mẫu 30 ghi "Không áp dụng" kèm căn cứ; tồn tại về nguồn thải đưa sang dòng 7 (công trình, biện pháp), 9, 10 (khối lượng chất thải), 11 (nội dung cấp phép). Nếu nghi ngờ phân loại nhóm, nêu thành câu hỏi phân loại, không chê thiếu đánh giá.
- Ví dụ: "Báo cáo lập theo nhóm III; Mẫu số 22c không yêu cầu dự án nhóm III đánh giá, dự báo tác động môi trường (Mục 1 Chương IV)."
- Máy kiểm: không (nội dung pháp lý, phải đọc mẫu).

### L002 — 17/11/2026 — Thiếu văn bản gốc mà không báo Bạn tải bổ sung
- Lỗi: Khi soạn Bản nhận xét, kho chưa có Nghị định 48/2026/NĐ-CP và Thông tư 09/2026/TT-BNNMT; trợ lý tự tra mạng không ra rồi viết theo tóm tắt, chỉ ghi chú "chưa đối chiếu được" ở cuối câu trả lời, không đề nghị Bạn gửi tệp. Hệ quả: phải sửa Bản nhận xét ba lần ngay trong buổi họp Hội đồng.
- Cách đúng: nguyên tắc Bạn chốt 17/11/2026 — thiếu tài liệu (văn bản quy phạm, mẫu biểu, hồ sơ) thì báo Bạn tải bổ sung NGAY ở câu đầu, nêu đích danh số, tên văn bản cần, trước khi viết nội dung dựa vào văn bản đó. Trình tự: tra kho (`tim_van_ban.py`) → tra sổ văn bản → không có thì dừng và xin tệp; không thay bằng tóm tắt hay nguồn thứ cấp.
- Ví dụ: "Kho chưa có Thông tư 09/2026/TT-BNNMT (Mẫu số 22c, Mẫu số 30). Bạn tải giúp bản Word hoặc PDF để tôi đối chiếu trước khi viết mục 4 và mục 7."
- Máy kiểm: không.
