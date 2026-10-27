# Sổ lỗi tự ghi — hl-vlncn-sct-vn

Lỗi Bạn chỉ ra trong phiên, Claude ghi ngay theo CLAUDE.md mục "Tự ghi lỗi" (Bạn chốt 17/10/2026). Đọc tệp này trước khi
soạn văn bản thuộc lĩnh vực của plugin. Định dạng mỗi mục và cách kiểm: `scripts/check_anti_error_format.py` ở gốc kho.
Lỗi kiểm được bằng máy thì kèm quy tắc trong `qa_rules.py` (vbhc-vn) hoặc `check_facts.py` và ghi mã ở dòng "Máy kiểm".
Yêu cầu riêng cho MỘT văn bản không ghi ở đây mà ghi vào `trang-thai/<hồ sơ>.md` mục "Yêu cầu riêng một lần".

### L001 — 26/10/2026 — Suy ra doanh nghiệp thuộc Bộ Quốc phòng chỉ từ hậu tố "BQP" trong tên

- Lỗi: Bôi tím, ghi chú "chưa xác định thẩm quyền (khoản 1, khoản 2 Điều 6 NĐ 181)" và nói đơn vị "thuộc Bộ Quốc phòng" chỉ vì tên Cty Yên Phú Đông Đô - BQP, trong khi hồ sơ cho thấy ngược lại.
- Cách đúng: Thẩm quyền xét theo cơ quan cấp GP sử dụng VLNCN và chứng cứ trong hồ sơ: GCN cũ do cơ quan nào cấp (Cục KTAT&MTCN → ngành Công Thương), đơn vị có gửi báo cáo VLNCN cho Sở không. Không có chứng cứ thì hỏi bản sao GP, không kết luận từ tên.
- Ví dụ: GCN 6671/GCN-ATMT ngày 30/10/2024 do Cục KTAT&MTCN cấp cho người quản lý của Cty → thuộc thẩm quyền Sở theo khoản 1 Điều 6.
- Máy kiểm: không (nhận định nghiệp vụ).

### L002 — 27/10/2026 — Công văn trả lời người không đủ điều kiện nêu việc đã tham dự huấn luyện, kiểm tra

- Lỗi: Công văn trả lời Cty R.K Việt Nam có câu "Ông … đã tham dự huấn luyện, kiểm tra trong các ngày 17, 18/10/2026."
- Cách đúng: Công văn trả lời hồ sơ không đủ điều kiện chỉ nêu hồ sơ ghi gì → quy định → lý do chưa đủ cơ sở → đề nghị; không nêu việc tham dự, không nêu kết quả kiểm tra của người không đủ điều kiện.
- Ví dụ: bỏ hẳn câu tham dự; đoạn đề nghị bắt đầu "Đề nghị Công ty bổ sung…".
- Máy kiểm: không.

### L003 — 27/10/2026 — Công văn trả lời doanh nghiệp gửi thêm Trung tâm Phục vụ hành chính công

- Lỗi: Dựng công văn trả lời từ khuôn QĐ công nhận nên Nơi nhận có dòng "Trung tâm Phục vụ hành chính công tỉnh".
- Cách đúng: Công văn trả lời doanh nghiệp (mẫu 09, 10): "- Như trên; - Lưu: VT, BP1C, CN." Dòng Trung tâm Phục vụ hành chính công chỉ dùng ở QĐ công nhận kết quả (mẫu 05 mục A).
- Ví dụ: CV R.K Việt Nam bản Bạn sửa 27/10/2026.
- Máy kiểm: không.

### L004 — 26/10/2026 — Đưa lỗi nhỏ của hồ sơ (thiếu ảnh 3x4) vào công văn trả lời

- Lỗi: Công văn trả lời Cty Định Nghĩa đề nghị bổ sung 02 ảnh 3x4 của học viên đã đạt.
- Cách đúng: Lỗi nhỏ (thiếu ảnh, chính tả…) bỏ qua, xử lý trực tiếp với đơn vị khi nhận GCN; công văn chỉ nêu nội dung không đủ điều kiện.
- Ví dụ: đoạn về học viên đạt chỉ ghi "Ông … đáp ứng điều kiện, đã được huấn luyện, kiểm tra trong các ngày … và đạt yêu cầu."
- Máy kiểm: không.
