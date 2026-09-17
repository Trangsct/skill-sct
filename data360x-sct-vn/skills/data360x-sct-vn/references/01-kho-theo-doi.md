# Reference 01 — Kho `theo-doi/` (kho GitHub riêng tư `Trangsct/vlncn-laocai`)

Do bot ghi sau mỗi lượt quét (từ 12/9/2026). Mọi thứ ở đây là **văn bản nội bộ của Sở** — chỉ đọc, trích
nội dung để làm việc; không chép sang kho công khai (`skill-sct`, `ccn-laocai`).

## 1. Cây thư mục

| Đường dẫn | Ai ghi | Nội dung |
|---|---|---|
| `theo-doi/danh-muc-<năm>.json` | bot, mỗi lượt quét | **Mục lục MỌI văn bản đi + đến** quét được (kể cả loại chỉ ghi mục lục). Mảng các bản ghi, mới nhất ở cuối |
| `theo-doi/<năm>/<số>_<ký hiệu>.md` | bot | Chữ trong văn bản **mang quy định**, phần đầu là số, ngày, đơn vị, người ký, lĩnh vực, URL bản gốc |
| `theo-doi/<năm>/<số>_<ký hiệu>.pdf` | bot | Chỉ với **bản scan** không có lớp chữ |
| `theo-doi/bao-cao/<ngày>.md` | bot | **Bản tin** một lượt quét: văn bản mới xếp theo plugin; mục "Chưa xếp được vào plugin nào" |
| `theo-doi/yeu-cau/<ten>/` | bot, khi Claude ra lệnh | Kết quả động tác "Lay van ban theo yeu cau": `README.md` (thấy gì, thiếu gì), `<số>.md`/`.pdf`, `<số>.json`, `_ket-qua.json` |
| `theo-doi/_da-gom.json` | bot | `"<số>|<ngày>": "<ngày gom>"` — chống ghi lại |
| `theo-doi/de-xuat-vbpl.csv` | workflow *De xuat VBPL* (13h30 thứ Tư) | Văn bản pháp luật **công khai** (NĐ, TT, QĐ-TTg, QĐ-UBND…) lọc từ danh mục, để nạp vào `registry/trang-thai.csv` của `skill-sct` |
| `theo-doi/README.md` | người | Giải thích thư mục |
| `trang-thai/bot-chay.json` | bot | Nhịp tim: `lan_cuoi`, `may`, `quet`, `day`, `loi` |
| `inbox/` | bot | **Giấy phép cá biệt** (`/GP-`, `/GCN-`…) — dây chuyền riêng, máy đọc vào cơ sở dữ liệu giấy phép; không phải nơi tra văn bản |

## 2. Một bản ghi trong `danh-muc-<năm>.json`

```json
{
  "so_ky_hieu": "5563/SCT-CN",
  "ngay_ban_hanh": "10/09/2026",
  "trich_yeu": "Về việc đôn đốc tiến độ đầu tư xây dựng hạ tầng kỹ thuật cụm công nghiệp",
  "don_vi": "Phòng Công nghiệp",
  "nguoi_ky": "Nguyễn Đình Chiến",
  "loai": "Công văn",
  "nguon": "di",
  "url_chi_tiet": "https://csdlvb.laocai.gov.vn/van-ban-di/detail/?id=2971635",
  "linh_vuc": ["kccn-sct-vn"],
  "gom_luc": "2026-09-12",
  "tep": "theo-doi/2026/5563_SCT-CN.md"
}
```

- `nguon`: `den` = văn bản đến (Sở nhận), `di` = văn bản đi (Sở phát hành).
- `linh_vuc`: mã plugin trong `skill-sct` mà văn bản liên quan (có thể nhiều, có thể rỗng) — do bảng
  `LINH_VUC` trong `bot-data360x.py` xếp bằng từ khóa trong trích yếu. **Chỉ là gợi ý**, không phải phân loại
  pháp lý.
- `tep`: có → đã có chữ (hoặc bản scan) để đọc. Không có → chỉ mục lục; cần bản gốc thì mở `url_chi_tiet`
  (chỉ máy trong nước đã đăng nhập mở được) hoặc sai bot (SKILL.md động tác 2).
- `so_ky_hieu` có thể **rỗng** (bản cam kết, phụ lục doanh nghiệp gửi lên) — tệp khi đó tên `vb-<id>`.
- `nguoi_ky` thường rỗng ở văn bản đến; **không suy ra người ký từ chức danh**.

## 3. Bản tin `bao-cao/<ngày>.md`

Cấu trúc: dòng tổng (quét từ ngày nào, bao nhiêu văn bản, bao nhiêu mới, tải bao nhiêu tệp) → từng mục
`## <mã plugin> - <tên lĩnh vực> (N văn bản)` với từng dòng `[đến|đi] **số** ngày - trích yếu -> tệp` →
mục `## Chưa xếp được vào plugin nào` (25 dòng mới nhất) → `## Chỗ máy chưa lấy được`.

Mỗi lĩnh vực chỉ liệt kê 40 dòng mới nhất; đủ thì tra `danh-muc-<năm>.json`.

## 4. Lĩnh vực ↔ plugin (bảng `LINH_VUC`, bản 12/9/2026)

kccn-sct-vn (khu, cụm công nghiệp) · sd-vlncn-sct-vn (sử dụng VLNCN, nổ mìn) · kho-vlncn-sct-vn · hl-vlncn-sct-vn
(huấn luyện) · hnh-sct-vn (hàng hóa nguy hiểm) · hc-sct-vn (hóa chất) · attp-sct-vn · atvsld-sct-vn · pccc-sct-vn ·
bvmt-sct-vn · qlks-sct-vn (khoáng sản, apatit, quặng) · tkm-sct-vn (thiết kế mỏ) · xd-sct-vn (xây dựng) ·
dacn-sct-vn (dự án, IIP, chủ trương đầu tư, khuyến công) · quy-hoach-ct-vn (quy hoạch, điện, năng lượng) ·
xp-sct-vn (xử phạt, thanh tra, khiếu nại) · vbhc-vn (thể thức, văn thư) · sct-laocai-org-vn (tổ chức, phân công) ·
bpb-sct-vn (bài phát biểu).

Thêm plugin mới → thêm một mục vào `LINH_VUC` trong `ccn-laocai/scripts/bot-data360x.py` (PR kho ccn-laocai).

## 5. Bot tải PDF của văn bản nào?

Chỉ văn bản **mang quy định**: số ký hiệu `NĐ-CP, TT-, QĐ-TTg, QĐ-UBND, QĐ-BCT, CT-, NQ-, KH-, HD-, QC-, TB-`
hoặc trích yếu có *dự thảo, quy định, hướng dẫn, tiêu chí, quy chế, đề án, chương trình, kế hoạch, tổng kết,
sơ kết, sửa đổi, thay thế*. Không bao giờ tải giấy mời, hồ sơ mời thầu, lịch công tác, giấy phép cá biệt.
Trần 30 tệp/lượt, bỏ qua PDF trên 12 MB. Vì thế **công văn trao đổi từng việc thường chỉ có mục lục** — cần
bản gốc thì sai bot lấy đích danh.

## 6. Giới hạn cần nhớ

- Kho bắt đầu từ **20/8/2026**; văn bản cũ hơn phải sai bot với `ngay` lớn (Data360X có từ 2025).
- Lớp chữ `.md` là text-layer của PDF: **số, ngày ở trường ký số thường trống trong phần chữ** → lấy ở
  phần đầu tệp. Phụ lục bảng biểu có thể vỡ cột; con số quan trọng thì đối chiếu bản gốc/ảnh trang.
- `linh_vuc` xếp bằng từ khóa: có thể thiếu hoặc thừa. Tra kho nên dùng cả từ khóa lẫn `--linh-vuc`.
- Mục lục chỉ có văn bản mà tài khoản của người dùng nhìn thấy trên Data360X (Phòng Quản lý công nghiệp).
