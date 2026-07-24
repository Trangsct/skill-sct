# skills-sct — Kho quản lý phiên bản bộ skill Claude của Sở Công Thương Lào Cai

Kho lưu trữ và theo dõi lịch sử thay đổi của 8 skill dùng cho công việc tham mưu tại Phòng Quản lý Công nghiệp:

| Skill | Nội dung |
|---|---|
| `vbhc-vn` | Soạn thảo văn bản hành chính + 7 nhóm anti-error + đọc PDF metadata |
| `kcn-ccn-vn` | Quản lý nhà nước về KCN/CCN (kèm file hiện trạng động ref 18) |
| `hnh-sct-vn` | Cấp phép vận chuyển hàng hóa nguy hiểm |
| `pccc-sct-vn` | PCCC 8 lĩnh vực ngành Công Thương |
| `bvmt-sct-vn` | Bảo vệ môi trường ngành Công Thương, KNK, carbon |
| `quy-hoach-ct-vn` | Quy hoạch khoáng sản, điện, KCN, CCN |
| `sct-laocai-org-vn` | Cơ cấu tổ chức, phân công BGĐ và chuyên viên |
| `vbhc-pdf-reader-vn` | Trích metadata PDF văn bản hành chính |
| `tkm-sct-vn` | Thẩm định thiết kế mỏ khoáng sản 20 năm (2006–2026), toàn văn TT 31/2025, BC 452/BC-TTCP, liên kết trọn vòng đời dự án mỏ |
| `dacn-sct-vn` | Quản lý danh mục dự án công nghiệp và điều hành chỉ tiêu tăng trưởng theo NQ 169/NQ-CP: 09 chỉ tiêu Sở chủ trì, danh mục dự án động lực, phân tích sản xuất công nghiệp hằng tháng, cảnh báo sớm, 7 nhóm điểm nghẽn, báo cáo trước ngày 20, kịch bản tăng trưởng; kèm 2 script phân tích |
| `qlks-sct-vn` | QLNN về khoáng sản: phân vai liên ngành, KH quản lý rủi ro, GCN KTAT hầm lò, chế biến - nguồn gốc, đối chiếu VLNCN - sản lượng, rà chồng lấn khi thẩm định CCN, thống kê - kê khai - báo cáo định kỳ sản lượng (CV 5141), dữ liệu 178 GP + báo cáo năm 2025 |

## Quy tắc validate BẮT BUỘC trước khi đóng gói plugin (tránh lỗi upload lặp lại)

Trình upload plugin của Claude từ chối gói nếu vi phạm. Trước khi zip, LUÔN kiểm:

0. **`description` trong `.claude-plugin/plugin.json` ≤ 500 ký tự** (giới hạn RIÊNG của plugin.json, chặt hơn SKILL.md — lỗi thật 14/7/2026 khi upload tkm-sct-vn 870 ký tự: "Plugin description must be at most 500 characters").
1. **`description` trong frontmatter SKILL.md ≤ 1024 ký tự** (đếm theo ký tự, tiếng Việt có dấu tính 1 ký tự/chữ). Đây là lỗi hay gặp nhất. Lệnh kiểm nhanh toàn repo:
   ```bash
   python3 -c "
   import re,glob
   for f in sorted(glob.glob('**/SKILL.md',recursive=True)):
       m=re.search(r'description:\s*\"(.*?)\"',open(f,encoding='utf-8').read(),re.S)
       n=len(m.group(1)) if m else -1
       print(('VUOT!' if n>1024 else 'ok   '),n,f)"
   ```
2. Cấu trúc gói: `.claude-plugin/plugin.json` ở gốc zip + nội dung tại `skills/<tên>/...` (zip từ BÊN TRONG thư mục plugin: `cd <tên> && zip -r ../x.zip .claude-plugin skills`).
3. `plugin.json` có đủ `name` (trùng tên thư mục skill), `version`, `description`.
4. Không kèm `__pycache__`, file tạm, file ẩn hệ điều hành.

## Quy trình cập nhật (mỗi khi Claude sửa skill)

1. Cuối phiên làm việc có sửa skill, yêu cầu Claude: **"đóng gói skill đã sửa thành zip"**.
2. Tải zip về máy, **giải nén**.
3. Trên GitHub, mở repo này → vào đúng thư mục skill (vd `vbhc-vn/`) → **Add file → Upload files** → kéo thả các file/thư mục vừa giải nén (file trùng đường dẫn sẽ tự ghi đè).
4. Ô commit message ghi: `YYYY.MM.DD — nội dung sửa` (vd `2026.07.02 — thêm Nhóm F, G; file hiện trạng ref 18`).
5. Bấm **Commit changes**.
6. Ghi thêm 1 dòng vào `CHANGELOG.md`.
7. Đồng thời upload zip skill đó lên Claude (Settings → Skills → xóa bản cũ → Upload) để Claude dùng bản mới.

## Xem lại lịch sử / so sánh

- Tab **Commits** (hoặc nút đồng hồ ⏱ trên trang repo): danh sách mọi lần thay đổi theo ngày.
- Bấm vào một commit: GitHub hiển thị **đỏ (xóa) / xanh (thêm)** từng dòng — biết chính xác lần đó sửa gì.
- Muốn quay về bản cũ của một file: mở file → **History** → chọn phiên bản → copy nội dung.

## Lưu ý quan trọng

- Repo để **Private** (nội dung có thông tin nội bộ cơ quan: phân công nhân sự, quy trình, hồ sơ). Vì là private nên Claude KHÔNG tự đọc được repo này trong chat — khi cần đối chiếu, tải file từ repo và gửi vào chat.
- Nguồn sự thật là repo này; bản trên Claude Settings chỉ là "bản cài đặt". Mất bản nào cũng khôi phục được từ đây.
