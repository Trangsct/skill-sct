# CHANGELOG — vbhc-vn v2.36.1 (22/10/2026)

- `scripts/kiem_tra_truoc_khi_giao.py` hàm `sua_bang()`: điều kiện bỏ qua bảng Nơi nhận - ký so sánh `tb is t_ky`, nhưng `doc.tables` tạo đối tượng Table mới mỗi lần gọi nên điều kiện luôn sai → `--tu-sua` gắn căn giữa dọc cho cả ô Nơi nhận và ô ký, đẩy khối Nơi nhận xuống giữa ô (phát hiện 22/10/2026 khi soạn công văn trả lời hồ sơ huấn luyện người quản lý từ mẫu thật CV 3155). Sửa: so sánh phần tử XML `tb._tbl is t_ky._tbl`. Kiểm lại trên mẫu thật: bảng ký giữ nguyên, hồi quy `tests/run_regression.py` xanh.
- `plugin.json` 2.36.0 → 2.36.1.
