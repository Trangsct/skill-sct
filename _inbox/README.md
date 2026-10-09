# Hộp thư nạp kho (`_inbox/`) — kéo thả văn bản, máy tự xếp vào plugin

Bạn chốt 09/10/2026. Mục tiêu: văn bản quy phạm pháp luật gửi MỘT LẦN là nằm trong kho, có toàn văn
`.txt` tra được bằng máy, mọi phiên về sau đều tìm thấy (xem `00-DANH-MUC-CHUNG.md` trong `van-ban-goc/`
của từng plugin và `scripts/tim_van_ban.py`).

## Cách dùng (6 bước)

1. Mở `github.com/Trangsct/skill-sct`, vào thư mục `_inbox`.
2. Bấm **Add file** → **Upload files**.
3. Kéo thả tệp văn bản (`.docx`, `.doc`, `.pdf`, `.xlsx`; mỗi lần một hoặc nhiều tệp).
4. Ở phần **Commit changes** ghi `nạp [số hiệu]`, chọn **Commit directly to the main branch**
   (nếu nhánh `main` đang chặn commit trực tiếp thì chọn *Create a new branch* — workflow vẫn chạy trên nhánh đó).
5. Chờ 2–5 phút (có LibreOffice/OCR có thể tới 8 phút), vào mục **Pull requests** sẽ thấy PR **"Nạp kho: [số hiệu] [tên]"**.
6. Đọc mô tả PR (số, ngày, cơ quan, plugin chủ, kết quả kiểm tra bản `.txt`, cảnh báo dung lượng) rồi bấm **Merge**.

## Máy làm gì (workflow `.github/workflows/nap-kho.yml` → `scripts/nap_kho.py`)

- Bóc chữ bằng `scripts/trich_chu_van_ban_goc.py` (Word, LibreOffice cho `.doc`, pdftotext, OCR tiếng Việt cho bản quét),
  đọc **số hiệu, ngày, cơ quan, người ký** bằng script — không đoán.
- Đoán **plugin chủ** theo bảng từ khóa (VLNCN, nổ mìn → `sd-vlncn-sct-vn`; kho VLNCN → `kho-vlncn-sct-vn`; hóa chất →
  `hc-sct-vn`; hàng hóa nguy hiểm → `hnh-sct-vn`; cụm, khu công nghiệp → `kccn-sct-vn`; khoáng sản → `qlks-sct-vn`;
  thực phẩm → `attp-sct-vn`; môi trường → `bvmt-sct-vn`; phòng cháy → `pccc-sct-vn`; đất đai → `dat-dai-sct-vn`;
  xử phạt → `xp-sct-vn`; xây dựng → `xd-sct-vn`; tổ chức bộ máy Sở → `sct-laocai-org-vn`…). Không đoán được →
  `vbhc-vn/skills/vbhc-vn/van-ban-goc/chua-phan-loai/` và ghi rõ trong PR.
- Đổi tên chuẩn `YYYY.MM.DD-SỐ.KÝ.HIỆU-Tên-trích-yếu-ngắn`, giữ nguyên định dạng gốc; chuyển vào `van-ban-goc/` của
  plugin chủ; sinh `.txt` cùng tên; dựng lại `DANH-MUC-VAN-BAN-GOC.csv` và `00-DANH-MUC-CHUNG.md` ở mọi plugin;
  chạy `export_ignore.py`; xóa tệp khỏi `_inbox/`; mở PR.
- Cảnh báo trong PR khi tệp > 3 MB (bản gốc không vào gói claude.ai, chỉ còn trên GitHub; bản `.txt` vẫn vào gói)
  và khi tổng kho vượt 480 MB (trần claude.ai 512 MB).

## Lưu ý

- Thiết lập một lần: Settings → Actions → General → Workflow permissions → *Read and write permissions* và
  *Allow GitHub Actions to create and approve pull requests* (nếu không, bước mở PR báo lỗi 403).
- Sau khi merge, phiên Claude kế tiếp cập nhật reference tóm tắt của plugin chủ, CHANGELOG, version (mục 4.1 `CLAUDE.md`).
- Thư mục này chỉ là nơi tạm; không để tệp nằm lâu. Tệp không bóc được chữ sẽ vẫn ở đây và PR ghi rõ lỗi.
