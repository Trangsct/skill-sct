# Sổ lỗi tự ghi — hnh-sct-vn

Lỗi Bạn chỉ ra trong phiên, Claude ghi ngay theo CLAUDE.md mục "Tự ghi lỗi" (Bạn chốt 17/10/2026). Đọc tệp này trước khi
soạn văn bản thuộc lĩnh vực của plugin. Định dạng mỗi mục và cách kiểm: `scripts/check_anti_error_format.py` ở gốc kho.
Lỗi kiểm được bằng máy thì kèm quy tắc trong `qa_rules.py` (vbhc-vn) hoặc `check_facts.py` và ghi mã ở dòng "Máy kiểm".
Yêu cầu riêng cho MỘT văn bản không ghi ở đây mà ghi vào `trang-thai/<hồ sơ>.md` mục "Yêu cầu riêng một lần".

### L001 — 02/11/2026 — Kết luận Sở không có thẩm quyền với tiền chất thuốc nổ loại 5.1
- Lỗi: thẩm định hồ sơ vận chuyển amoni nitrat và 05 muối clorat, perclorat, nitrat (loại 5.1), kết luận hàng là tiền chất thuốc nổ nên ngoài thủ tục HHNH, dự thảo công văn từ chối. Nguyên nhân: plugin ghi "trừ VLNCN, tiền chất thuốc nổ" như loại trừ chung. Bạn chỉ ra hai Giấy phép amoni nitrat Bộ, Cục đã cấp trước đó.
- Cách đúng: phần "trừ vật liệu nổ công nghiệp, tiền chất thuốc nổ" chỉ áp trong loại 1. Tiền chất loại 5.1 thụ lý như loại 5 (khoản 1 Điều 8), cấp Giấy phép HHNH kèm câu "không thay thế giấy phép vận chuyển, giấy phép nhập khẩu tiền chất thuốc nổ"; giấy phép của Công an cấp song song. Nguyên tắc 30.
- Ví dụ: tiền lệ 516/GP-BCT (6/2025), 112/GP-HC (11/2025), 5869/GP-SCT ngày 21/9/2026.
- Máy kiểm: check_facts `hnh-tien-chat-loai-5-van-cap-phep`

### L002 — 05/11/2026 — Đề nghị làm rõ "sơ mi rơ moóc container" chỉ dựa vào tên loại xe trên bản dịch
- Lỗi: công văn hoàn thiện hồ sơ 06 tiền chất loại 5.1 (bản 02/11) nêu 04 sơ mi rơ moóc là "loại chở container" theo bản dịch Giấy chứng nhận đăng ký xe Trung Quốc, đề nghị nêu hàng trong công-ten-nơ hay xếp trực tiếp. Chủ doanh nghiệp phản hồi đó là mooc sàn vẫn chở hàng bao bình thường; ảnh xe trên đăng ký là sàn phẳng, cùng nhãn hiệu, kích thước với rơ moóc ghi "thùng".
- Cách đúng: tên loại xe trên bản dịch đăng ký xe Trung Quốc không đủ để bắt lỗi dạng chứa hàng. Xem ảnh phương tiện, nhãn hiệu, kích thước, chiều cao sàn; chỉ nêu khi phương tiện thực tế không chở được dạng hàng đề nghị. Bản 05/11 bỏ ý này, giữ yêu cầu quy cách bao bì, nhãn.
- Ví dụ: sơ mi rơ moóc nhãn hiệu La Hưởng LXC9400TWYE, 12.450 x 2.550 x 1.600 mm, một xe bản dịch ghi "container", xe khác ghi "thùng".
- Máy kiểm: không (nội dung nghiệp vụ, loại N)

### L003 — 10/11/2026 — Thêm bảng danh sách người lái xe, người áp tải vào Danh mục kèm Giấy phép
- Lỗi: dự thảo Giấy phép vận chuyển xăng, dầu diesel loại 3 (01 tổ hợp đầu kéo - sơ mi rơ moóc xi téc, xe biển Việt Nam) thêm bảng thứ ba "Danh sách người lái xe và người áp tải" vào phần Danh mục kèm theo, theo ghi chú ngày 06/11/2026. Bạn chỉ ra không đúng quy định, yêu cầu bỏ.
- Cách đúng: mẫu Giấy phép tại Phụ lục VII, Phụ lục VIII Nghị định số 161/2024/NĐ-CP chỉ ghi tổ chức, giấy chứng nhận đăng ký, địa chỉ, người đại diện, loại hàng được phép vận chuyển và thời hạn; không có nội dung người lái xe, người áp tải. Danh sách người lái xe và người áp tải là thành phần hồ sơ (điểm c khoản 1, khoản 2 Điều 15), chỉ đối chiếu trong Biên bản thẩm định. Danh mục kèm Giấy phép chỉ gồm bảng hàng hóa và bảng phương tiện (phương tiện, thiết bị chứa hàng). Ghi chú 06/11/2026 về việc bổ sung danh sách này không còn áp dụng. Nguyên tắc 34.
- Ví dụ: Giấy phép xăng, dầu diesel loại 3 dự thảo ngày 10/11/2026, bản sửa chỉ còn bảng hàng hóa và bảng "Danh sách phương tiện vận chuyển".
- Máy kiểm: không (nội dung nghiệp vụ, loại N)
