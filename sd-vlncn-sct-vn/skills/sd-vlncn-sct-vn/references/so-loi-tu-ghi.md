# Sổ lỗi tự ghi — sd-vlncn-sct-vn

Lỗi Bạn chỉ ra trong phiên, Claude ghi ngay theo CLAUDE.md mục "Tự ghi lỗi" (Bạn chốt 17/10/2026). Đọc tệp này trước khi
soạn văn bản thuộc lĩnh vực của plugin. Định dạng mỗi mục và cách kiểm: `scripts/check_anti_error_format.py` ở gốc kho.
Lỗi kiểm được bằng máy thì kèm quy tắc trong `qa_rules.py` (vbhc-vn) hoặc `check_facts.py` và ghi mã ở dòng "Máy kiểm".
Yêu cầu riêng cho MỘT văn bản không ghi ở đây mà ghi vào `trang-thai/<hồ sơ>.md` mục "Yêu cầu riêng một lần".

### L001 — 30/10/2026 — Kết luận nhầm "không vướng an ninh, trật tự" khi công trình không có trong Giấy chứng nhận ANTT
- Lỗi: rà Thông báo thực hiện dịch vụ nổ mìn của một nhà thầu (thành viên liên danh, tự nổ mìn phần việc của mình tại một gói thầu giao thông), Claude bỏ lý do an ninh, trật tự vì Giấy chứng nhận ANTT của công ty có ngành "dịch vụ nổ mìn (trên địa bàn tỉnh)" và "kinh doanh ngành, nghề có sử dụng VLNCN". Bạn chỉ ra: công trình này chưa phù hợp với Giấy chứng nhận ANTT (hoặc chưa có GCN ANTT), yêu cầu tra rõ điều khoản.
- Cách đúng: với ngành, nghề có sử dụng VLNCN để thi công công trình, đối chiếu ĐỊA ĐIỂM trên Giấy chứng nhận ANTT với địa điểm sử dụng VLNCN — GCN chỉ ghi kho/mỏ ở xã khác thì công trình mới chưa được chứng nhận; tiền lệ cùng công ty: GCN ANTT riêng cho từng gói thầu, ghi phạm vi lý trình (ref 07 mục L). Căn cứ: điểm đ k1 Đ38, điểm a k1 Đ39 Luật 42/2024 (sđ Luật 118/2025); NĐ 96/2016/NĐ-CP (sđ NĐ 56/2023, NĐ 58/2026; từ 15/11/2026 thêm NĐ 392/2026): Điều 3 (ngành nghề có điều kiện), k1 Đ6 (cấm kinh doanh khi chưa có GCN), điểm a k2 Đ18 (kinh doanh không đúng ngành, nghề, địa điểm ghi trong GCN → thu hồi có thời hạn), k1 Đ21 và k11 Đ25 (thay đổi nội dung → đề nghị cấp đổi), Đ24 (thẩm quyền Công an). Yêu cầu công ty xin cấp/cấp đổi GCN ANTT cho địa điểm trước khi đề nghị cấp GP sử dụng; không nhận GCN của dịch vụ nổ mìn thay cho địa điểm thi công.
- Ví dụ: công văn Sở trả lời Thông báo dịch vụ nổ mìn của một công ty tại gói thầu đường giao thông xã Phong Dụ Thượng (30/10/2026), mục 4 "Về an ninh, trật tự". Cùng văn bản: tự nổ mìn phần việc của mình theo hợp đồng thi công không phải dịch vụ nổ mìn (điểm a k1 Đ40, k4 Đ39) → phải xin GP sử dụng VLNCN.
- Máy kiểm: thủ công — checklist thẩm định C1 (ref 02): đối chiếu địa điểm trên GCN ANTT với địa điểm nổ mìn trong Giấy đề nghị, PANM.
