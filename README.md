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
