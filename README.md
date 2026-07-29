# skills-sct — Kho quản lý phiên bản bộ plugin Claude của Sở Công Thương Lào Cai

Kho lưu trữ và theo dõi lịch sử thay đổi bộ plugin dùng cho công việc tham mưu tại Phòng Quản lý Công nghiệp.

> **Từ 25/7/2026 (tối): gộp trở lại MỘT marketplace duy nhất — `marketplace.json` v4.0.0 đủ 18 plugin.** Phương án tách đôi (skill-sct 12 + skill-sct-2 6) bị hủy vì hai đầu mối gây rối khi quản lý. Repo `skill-sct-2` ngừng sử dụng và sẽ xóa; từ nay **mọi cập nhật của cả 18 plugin CHỈ làm tại repo này**.
>
> ⚠️ **Vì marketplace đã cài trên claude.ai không nạp entry mới**, sau khi gộp phải **Remove → Add lại** marketplace `skill-sct` trên claude.ai thì 6 plugin `bpb-sct-vn`, `dacn-sct-vn`, `pccc-sct-vn`, `quy-hoach-ct-vn`, `sct-laocai-org-vn`, `vbhc-pdf-reader-vn` mới hiện ra. Nếu Add lại vẫn không đủ 18, giữ nguyên hiện trạng và cài 6 plugin đó bằng Local uploads (zip từng thư mục plugin) cho tới khi claude.ai sửa lỗi.

> **Từ 25/7/2026: toàn bộ 18 plugin đều theo chuẩn plugin** — mỗi thư mục có `.claude-plugin/plugin.json` ở gốc và nội dung skill nằm tại `skills/<tên>/`. Không còn thư mục nào để `SKILL.md` ở gốc. Thư mục `kcn-ccn-vn` (bản cũ) đã xoá ngày 25/7/2026, khôi phục từ commit `07dd33e` nếu cần.

| Plugin | Nội dung |
|---|---|
| `vbhc-vn` | Soạn thảo văn bản hành chính + 7 nhóm anti-error + đọc PDF metadata |
| `kccn-sct-vn` | Quản lý nhà nước về KCN/CCN theo NĐ 32/2024, NĐ 139/2025, NĐ 178/2026 (thay thế `kcn-ccn-vn` cũ) |
| `hnh-sct-vn` | Cấp phép vận chuyển hàng hóa nguy hiểm |
| `pccc-sct-vn` | PCCC 8 lĩnh vực ngành Công Thương, giải pháp kỹ thuật công trình hiện hữu (QĐ 1074/QĐ-BXD, QĐ 1609/QĐ-BCT) |
| `bpb-sct-vn` | Bài phát biểu, tham luận, diễn văn cho lãnh đạo Sở; 11 bài mẫu gốc + script dựng docx 15pt |
| `bvmt-sct-vn` | Bảo vệ môi trường ngành Công Thương, KNK, carbon |
| `quy-hoach-ct-vn` | Quy hoạch khoáng sản, điện, KCN, CCN |
| `sct-laocai-org-vn` | Cơ cấu tổ chức, phân công BGĐ và chuyên viên |
| `vbhc-pdf-reader-vn` | Trích metadata PDF văn bản hành chính |
| `tkm-sct-vn` | Thẩm định thiết kế mỏ khoáng sản 20 năm (2006–2026), toàn văn TT 31/2025, BC 452/BC-TTCP, liên kết trọn vòng đời dự án mỏ |
| `dacn-sct-vn` | Quản lý danh mục dự án công nghiệp và điều hành chỉ tiêu tăng trưởng theo NQ 169/NQ-CP: 09 chỉ tiêu Sở chủ trì, danh mục dự án động lực, phân tích sản xuất công nghiệp hằng tháng, cảnh báo sớm, 7 nhóm điểm nghẽn, báo cáo trước ngày 20, kịch bản tăng trưởng; kèm 2 script phân tích |
| `qlks-sct-vn` | QLNN về khoáng sản: phân vai liên ngành, KH quản lý rủi ro, GCN KTAT hầm lò, chế biến - nguồn gốc, đối chiếu VLNCN - sản lượng, rà chồng lấn khi thẩm định CCN, thống kê - kê khai - báo cáo định kỳ sản lượng (CV 5141), dữ liệu 178 GP + báo cáo năm 2025 |
| `attp-sct-vn` | An toàn thực phẩm và công nghiệp tiêu dùng - thực phẩm: GCN đủ điều kiện ATTP, tự công bố, hậu kiểm, thuốc lá, rượu; hướng dẫn UBND cấp xã quản lý hộ kinh doanh nhỏ lẻ; GATE hiệu lực NĐ 46/2026 tạm ngưng theo NQ 15/2026 |
| `xp-hc-vlncn-sct-vn` | Xử phạt VPHC hóa chất + VLNCN theo NĐ 275/2026/NĐ-CP (hiệu lực 25/8/2026, thay NĐ 71/2019 + Điều 1 NĐ 17/2022): bảng hành vi - mức phạt Đ7-61, thẩm quyền Đ62-73, chuyển tiếp Đ74, đối chiếu điều cũ→mới — plugin chế tài DÙNG CHUNG cho `sd-vlncn-sct-vn`, `hl-vlncn-sct-vn`, `kho-vlncn-sct-vn`, `hc-sct-vn` |

## Quy tắc validate BẮT BUỘC trước khi đóng gói plugin (tránh lỗi upload lặp lại)

Trình upload plugin của Claude từ chối gói nếu vi phạm. Trước khi zip, LUÔN kiểm:

0. **`description` trong `.claude-plugin/plugin.json` ≤ 500 ký tự** — nay đã có script kiểm tự động `scripts/check_descriptions.py`, CI chặn nếu vượt (giới hạn RIÊNG của plugin.json, chặt hơn SKILL.md — lỗi thật 14/7/2026 khi upload tkm-sct-vn 870 ký tự: "Plugin description must be at most 500 characters").
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
5. **`plugin.json` phải nằm tại `<tên>/.claude-plugin/plugin.json`** — KHÔNG để ở gốc thư mục skill (lỗi thật ở `bpb-sct-vn`, phát hiện 25/7/2026).
6. **Khi đồng bộ hai chiều: đối chiếu trước, ghi đè sau.** Bản trên repo có thể MỚI HƠN bản đang cài trên Claude (lỗi thật 25/7/2026: bản cài `pccc-sct-vn` ngày 14/5/2026 thiếu reference 15 và QĐ 1074/QĐ-BCT so với repo). Luôn `diff -rq` và so checksum trước khi copy đè.

Lệnh kiểm nhanh cả hai giới hạn description toàn repo:

```bash
python3 -c "
import json,glob,re,yaml,os
for pj in sorted(glob.glob('*/.claude-plugin/plugin.json')):
    d=pj.split('/')[0]; o=json.load(open(pj,encoding='utf-8')); pl=len(o['description'])
    sk=f'{d}/skills/{d}/SKILL.md'
    m=re.match(r'^---\n(.*?)\n---\n',open(sk,encoding='utf-8').read(),re.S)
    sl=len(yaml.safe_load(m.group(1)).get('description',''))
    print(('BAD ' if pl>500 or sl>1024 else 'ok  '),f'{d:22} plugin.json={pl:4} SKILL.md={sl:5}')"
```

## Quy trình cập nhật (mỗi khi Claude sửa skill)

1. Cuối phiên làm việc có sửa skill, yêu cầu Claude: **"đóng gói skill đã sửa thành zip"**.
2. Tải zip về máy, **giải nén**.
3. Trên GitHub, mở repo này → vào đúng thư mục skill (vd `vbhc-vn/`) → **Add file → Upload files** → kéo thả các file/thư mục vừa giải nén (file trùng đường dẫn sẽ tự ghi đè).
4. Ô commit message ghi: `YYYY.MM.DD — nội dung sửa` (vd `2026.07.02 — thêm Nhóm F, G; file hiện trạng ref 18`).
5. Bấm **Commit changes**.
6. Ghi thêm 1 dòng vào `CHANGELOG.md`.
7. **Nâng `version` trong `plugin.json` của skill vừa sửa** rồi chạy `python3 scripts/sync_marketplace.py` để `marketplace.json` khớp lại, và nâng `metadata.version`. Bỏ bước này thì bản mới KHÔNG về máy người dùng (xem mục dưới).
8. Đồng thời upload zip skill đó lên Claude (Settings → Skills → xóa bản cũ → Upload) để Claude dùng bản mới.

## Vì sao plugin đã sửa mà máy vẫn dùng bản cũ

Ba nút thắt, phải thông cả ba:

1. **`version` là khoá mở cập nhật.** Claude Code lấy version theo thứ tự: `version` trong `plugin.json` → `version` trong entry `marketplace.json` → commit SHA. Nếu version phân giải ra vẫn bằng bản đang cài thì mọi lệnh update đều **bỏ qua** plugin đó, dù nội dung đã đổi. Sửa nội dung mà quên nâng `plugin.json` = người dùng không nhận được gì.
2. **Hai file phải khớp.** Repo này đặt `version` ở cả `plugin.json` lẫn entry marketplace. `plugin.json` luôn thắng, nên entry marketplace lệch sẽ không chặn cập nhật nhưng làm catalog hiển thị sai version và mô tả cũ. `scripts/sync_marketplace.py` giữ hai file khớp; CI `.github/workflows/marketplace-sync.yml` chặn nếu lệch.
3. **Marketplace bên thứ ba mặc định TẮT auto-update.** Chỉ marketplace chính thức của Anthropic mới bật sẵn. Với `skill-sct` phải tự bật hoặc làm mới thủ công:

   ```
   /plugin marketplace update skill-sct   # kéo catalog mới
   /plugin update                          # cập nhật plugin đã cài
   /reload-plugins                         # nạp vào phiên đang chạy
   ```

   Bật một lần cho đỡ phải nhớ: `/plugin` → tab **Marketplaces** → chọn `skill-sct` → **Enable auto-update**. Sau khi bật, Claude Code kiểm tra sau lúc khởi động phiên với độ trễ ngẫu nhiên tới 10 phút, và phiên đang chạy vẫn dùng bản cũ cho tới khi `/reload-plugins`.

   Trên claude.ai: Settings → Plugins → mở marketplace `skill-sct` và bấm làm mới; nếu vẫn không đổi thì gỡ marketplace rồi Add lại (gỡ marketplace sẽ gỡ theo các plugin đã cài từ nó).

## Xem lại lịch sử / so sánh

- Tab **Commits** (hoặc nút đồng hồ ⏱ trên trang repo): danh sách mọi lần thay đổi theo ngày.
- Bấm vào một commit: GitHub hiển thị **đỏ (xóa) / xanh (thêm)** từng dòng — biết chính xác lần đó sửa gì.
- Muốn quay về bản cũ của một file: mở file → **History** → chọn phiên bản → copy nội dung.

## Lưu ý quan trọng

- Repo để **Private** (nội dung có thông tin nội bộ cơ quan: phân công nhân sự, quy trình, hồ sơ). Vì là private nên Claude KHÔNG tự đọc được repo này trong chat — khi cần đối chiếu, tải file từ repo và gửi vào chat.
- Nguồn sự thật là repo này; bản trên Claude Settings chỉ là "bản cài đặt". Mất bản nào cũng khôi phục được từ đây.

## Tự động cập nhật marketplace (từ 29/7/2026)

Trước đây phải nhớ chạy tay `scripts/sync_marketplace.py` rồi tự sửa `metadata.version`. Nay CI làm thay:

| Ngữ cảnh | CI làm gì |
|---|---|
| Push lên `main` | Kiểm giới hạn description → đồng bộ `marketplace.json` từ 19 `plugin.json` → **tự nâng `metadata.version` một bậc patch** → commit ngược lại với thông điệp `[skip ci]` |
| Push nhánh khác, pull request | Chỉ kiểm tra (`--check` và `check_descriptions.py`), lệch thì báo đỏ, không tự sửa |

Nghĩa là **chỉ cần sửa `version` trong `plugin.json` của plugin rồi push** — phần còn lại tự chạy.

Hai script:

- `scripts/sync_marketplace.py` — `--check` (kiểm), không tham số (ghi lại), `--bump` (ghi lại và nâng `metadata.version`).
- `scripts/check_descriptions.py` — kiểm `plugin.json` ≤ 500 và `SKILL.md` ≤ 1024 ký tự cho cả 19 plugin.

Điều kiện: repo bật **Settings → Actions → General → Workflow permissions → Read and write permissions** thì bước commit ngược mới chạy được.

Lưu ý vẫn còn: marketplace đã cài trên claude.ai không tự nạp **entry plugin mới**. Nâng version của plugin đã có thì cập nhật được; thêm plugin mới vào catalog thì vẫn phải Remove → Add lại marketplace.
