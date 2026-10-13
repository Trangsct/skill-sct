# CHANGELOG — vbhc-vn v2.30.0 (13/10/2026)

Bạn chốt 13/10/2026 (vụ 3 công văn hoàn thiện hồ sơ vận chuyển HHNH Toàn Phát TQ, An Bình, Tân Phúc Hưng trình trên hệ thống quản lý văn bản mới, PGĐ ký số báo lỗi): văn bản giải quyết thủ tục hành chính **không gửi Ban Giám đốc Sở**, chỉ gửi trực tiếp các đơn vị theo đúng quy định; các dòng Nơi nhận cỡ 11; khối Nơi nhận - ký cách thân đúng 1 dòng; toàn bộ file phông Times New Roman. Máy kiểm và công cụ sửa ở vbhc-vn 2.30.0 (R19–R22, `scripts/chuan_hoa_xuat_ban.py`).

- `scripts/chuan_hoa_xuat_ban.py` (mới): chuẩn hóa trước khi xuất — (1) quét toàn bộ phông về Times New Roman (thân, kiểu Normal/Header/Footer, số trang, dấu cuối đoạn, docDefaults, theme, bảng phông; giữ Symbol, Wingdings); (2) các dòng Nơi nhận cỡ 11, bỏ chỉ số dưới/trên lạc; (3) đúng 1 dòng trống cỡ 14 trước bảng Nơi nhận - ký (thay đoạn đệm 1–7 pt); (4) `--tthc` bỏ dòng "Ban Giám đốc Sở". `TemplateDoc.save()` và `build_vb.py` tự gọi sau khi lưu.
- `scripts/qa_rules.py`: thêm R19 (phông), R20 (Nơi nhận cỡ 11), R21 (1 dòng trước khối ký, đoạn đệm nhỏ không tính) — WARN, thành FAIL khi `--final`; R22 (văn bản thủ tục hành chính gửi Ban Giám đốc Sở) — FAIL. Gợi ý của R06 bỏ "TT Phục vụ HCC" (trái Quy tắc 8).
- `tests/fail/`: 4 file lỗi mới r19–r22 (sinh bằng `tests/tao_file_loi.py`); r07b bỏ dòng Ban Giám đốc Sở theo mẫu gốc; `baseline-warn.json` cập nhật có chủ đích (WARN R19–R21 trên mẫu thật cũ — phông ẩn, cỡ 12, đoạn đệm).
- Mẫu thật `examples/sct/cong-van-de-nghi-bo-sung-ho-so.docx`, `giay-phep-van-chuyen-hhnh.docx`: bỏ dòng "- Ban Giám đốc Sở;" theo chốt mới (chỉ sửa đúng dòng này).
- SKILL.md Quy tắc bất biến 11, bảng QA, Nhóm G; `reference/phong-tranh-sai-lam.md` thứ tự Nơi nhận (bỏ TT Phục vụ HCC, ngoại lệ thủ tục hành chính); `tests/rule-inventory.md`.
- Ghi nhận khi trình trên hệ thống quản lý văn bản mới: mục Dự thảo chỉ để tệp công văn, không để tệp nén .rar bộ hồ sơ (tệp .rar được tích làm tệp ký → lãnh đạo không ký số được).

- `plugin.json` → 2.30.0.
