# CHANGELOG — vbhc-vn v2.33.0 (18/10/2026)

Đợt "tự động nâng cấp tiếp" sau bản giao việc 17/10/2026 (đề xuất 1, 7).

- **CI kiểm được trang khi render (đề xuất 1).** `qa_all.py` trước ghi cứng PDF vào `/home/claude/work/qa` — trên GitHub
  Actions không tạo được thư mục đó nên render thất bại im lặng (WARN RENDER) và WIDOW, SIGSPLIT chưa từng chạy trên CI.
  Nay: biến môi trường `VBHC_QA_DIR` → `/home/claude/work/qa` → thư mục tạm hệ thống; `kiem_tra_truoc_khi_giao.py`,
  `ra_soat_doc_lap.py` dùng cùng thư mục. `run_regression.py --voi-qa-all` coi WARN RENDER trên mẫu thật là đỏ.
- **WIDOW hạ WARN**: 6/26 mẫu thật đã ban hành có một từ cuối đoạn (số hiệu văn bản, "hiện./."), mẫu thật là chuẩn; vẫn
  in để cân nhắc rút câu. Dòng kẻ `_____` không tính.
- **SIGSPLIT**: khối ký gãy trong CÙNG một ô bảng ký (LibreOffice ngắt hàng; Word có thể khác — mẫu thật
  thong-bao-ket-luan-ubnd) → WARN kèm cách chữa `cantSplit` (H13); gãy giữa các đoạn/hàng vẫn FAIL.
- **`data/vbpl.json`** (đề xuất 7): 12 văn bản được điền ngày ban hành, hiệu lực từ bản gốc bằng `scripts/trich_hieu_luc.py`
  ở gốc kho (NĐ 71/2019, 146/2025, 106/2025, 161/2024, 168/2024, 133/2026, QĐ 2848, TT 56/2025, NQ 15/2026…) — R05 kiểm
  được thêm các văn bản này.
- `plugin.json` → 2.33.0.
