# Quy tắc làm việc với repo skill-sct

## Quy trình giao nộp (Bạn chốt 15/8/2026 - áp dụng vĩnh viễn)

- **Sau khi hoàn thành việc nâng cấp/cập nhật skill hoặc plugin** (sửa SKILL.md, references, văn bản gốc, plugin.json...): commit, push lên nhánh làm việc, **LUÔN mở Pull Request gộp nhánh đó vào `main` VÀ MERGE NGAY, KHÔNG cần hỏi lại**. Ghi rõ trong PR: plugin nào, phiên bản mới, nội dung thay đổi chính.
- Lý do Bạn chốt: cần hiệu quả công việc, đã có nhiều bản sao lưu nên ưu tiên nhanh, không lo sai lệch dữ liệu.
- Quy tắc merge-ngay này áp dụng cho việc nâng cấp skill/plugin; việc khác ngoài phạm vi đó thì vẫn hỏi trước khi merge.

## Quy tắc nghiệp vụ chung

- Mỗi lần nâng cấp plugin: tăng version trong `.claude-plugin/plugin.json`, thêm CHANGELOG theo mẫu `CHANGELOG-vYYYY.MM.DD.md` trong thư mục skill, và thêm mục mới lên ĐẦU `CHANGELOG.md` ở gốc repo.
- **KHÔNG sửa `.claude-plugin/marketplace.json` thủ công** (kể cả sync version/mô tả hay nâng `metadata.version`): sau khi merge vào `main`, bot trong `marketplace-sync.yml` tự đồng bộ từ các `plugin.json`, tự nâng `metadata.version` (có so với catalog của commit trước nên PR sync sẵn cũng không làm bot bỏ sót) và tự commit lại. CI trên PR chỉ nhắc chứ không báo đỏ khi lệch version/mô tả.
- Văn bản pháp luật mới đưa vào plugin: lưu bản gốc vào thư mục `van-ban-goc/` tương ứng và cập nhật reference mục lục; tuyệt đối không bịa số/ngày văn bản.
- **Đọc PDF ký số** (số/ngày điền qua trường ký số): lớp text hiển thị số/ngày rời rạc - phải render trang thành ảnh để đọc chính xác, không kết luận "để trống" chỉ từ text layer.
