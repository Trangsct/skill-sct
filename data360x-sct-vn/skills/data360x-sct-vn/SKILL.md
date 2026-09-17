---
name: data360x-sct-vn
description: "CÁNH TAY CỦA CLAUDE VÀO DATA360X (csdlvb.laocai.gov.vn - hệ thống văn bản đi/đến của Sở Công Thương Lào Cai). Kích hoạt khi: cần một văn bản đi/đến của Sở, văn bản của UBND tỉnh/Bộ gửi đến, hồ sơ một CCN/KCN/doanh nghiệp, 'lấy văn bản', 'tìm trên Data360X', 'văn bản mới tuần này', 'có công văn nào về…', 'sai bot', 'gọi bot', 'quét lại', soát dự thảo cần văn bản viện dẫn, cập nhật plugin theo bản tin theo-doi, hoặc bất kỳ việc nào đang thiếu dữ liệu gốc mà Data360X có. 4 động tác: (1) TRA KHO đã gom theo-doi/ ở kho riêng tư vlncn-laocai (danh-muc-<năm>.json, bao-cao/, tệp .md/.pdf); (2) SAI BOT LẤY đúng văn bản theo số ký hiệu/từ khóa (workflow 'Lay van ban theo yeu cau'); (3) QUÉT MỚI cả đi + đến (workflow 'Quet Data360X'); (4) TÌM VĂN BẢN VIỆN DẪN của dự thảo. Chờ kết quả rồi đọc tiếp trong cùng phiên; số/ngày lấy ở đầu tệp, không đọc trong lớp chữ; kho công khai không chép văn bản nội bộ."
---

# data360x-sct-vn — Data360X là cánh tay, chuột và bàn phím của Claude

> Bạn chốt 17/9/2026: *"khi làm việc bên chat, Claude biết cách kết hợp sử dụng kho dữ liệu của Data360X
> hoặc giao Data360X tự vào trang cơ sở dữ liệu để tải các tài liệu liên quan đến công việc, từ đó công
> việc được hoàn thành đầy đủ, tự động."* Skill này là bản hướng dẫn thao tác đó. Đọc hiểu, thẩm định,
> chốt câu chữ vẫn là của Claude; bot chỉ làm phần cơ học: vào cổng, tải, đọc chữ.

## I. Bức tranh 30 giây

```
 Claude (phiên làm việc)                    Máy cơ quan (runner "may-so-cong-thuong")
 ───────────────────────                    ──────────────────────────────────────────
 1. tra KHO theo-doi/  ──── có rồi ──►  đọc, làm việc
        │ chưa có
        ▼
 2. ra lệnh GitHub Actions ──────────────►  bot mở Chrome đã đăng nhập Data360X
    (Lay van ban theo yeu cau)               tải PDF → trích chữ → đẩy về kho
        │                                              │
        ◄───────── chờ 3-15 phút, đọc theo-doi/yeu-cau/<ten>/README.md
 3. làm tiếp việc đang dở với văn bản gốc trong tay
```

- **Kho** = thư mục `theo-doi/` trong kho GitHub **riêng tư** `Trangsct/vlncn-laocai` (ref 01).
- **Bot** = `scripts/bot-data360x.py` (kho `ccn-laocai`), chạy trên máy cơ quan qua GitHub Actions, dùng hồ sơ
  Chrome đã đăng nhập của người dùng. **Không đăng nhập hộ, không giải captcha** — phiên hết hạn thì bot báo
  và chờ người dùng đăng nhập (ref 03).
- Bốn workflow trong kho `vlncn-laocai` là bốn "nút bấm" (ref 02). Gọi bằng công cụ GitHub có trong phiên
  (MCP `actions_run_trigger`, `gh workflow run`, hoặc `scripts/goi_bot.py`).

## II. QUY TẮC LÀM VIỆC (đọc trước khi làm bất cứ gì)

1. **Tra kho trước, sai bot sau.** Kho đã có mục lục MỌI văn bản đi + đến từ 20/8/2026 (khoảng 500 văn bản
   mỗi tháng) và chữ của văn bản mang quy định. Chạy `scripts/tim_trong_kho.py` trước; chỉ gọi bot khi kho
   không có bản gốc hoặc cần văn bản mới hơn lượt quét gần nhất.
2. **Sai bot là hành động có thật trên máy cơ quan**: Chrome mở lên, tải tệp, đẩy commit. Gộp mọi thứ cần
   vào MỘT lệnh (nhiều số ký hiệu và từ khóa cách nhau bằng `;`) thay vì gọi nhiều lần. Không gọi lại khi lệnh
   trước còn đang chạy.
3. **Số và ngày văn bản lấy ở phần đầu tệp `.md`** (bot chép từ bảng danh mục Data360X) — **không** đọc trong
   phần chữ, vì trường ký số không nằm trong lớp text (đầu văn bản thường thấy `Số: /TTr-SCT`, `ngày tháng 8
   năm 2026` trống). Bản scan `.pdf` không có chữ: phải mở ảnh trang để đọc.
4. **Không bịa.** Kho không có, bot không thấy → nói rõ "không thấy trên Data360X trong N ngày quét", đề nghị
   mở rộng khoảng ngày hoặc hỏi người dùng. Không suy ra số, ngày, tên từ trí nhớ.
5. **Kho công khai — riêng tư.** `vlncn-laocai` riêng tư: văn bản nội bộ chỉ nằm đó. `skill-sct` và
   `ccn-laocai` công khai: khi cập nhật plugin hay web, viết lại nội dung, dẫn số hiệu và ngày, **không chép
   bản gốc** sang.
6. **Không sửa lịch, không tạo workflow mới, không đổi nhãn runner** nếu người dùng không yêu cầu. Cần thêm
   khả năng cho bot thì sửa `bot-data360x.py` ở kho `ccn-laocai` theo quy trình PR.
7. Bot cần **máy cơ quan đang bật và đã đăng nhập Windows**.
8. **Từ khóa NGẮN** (Bạn chốt 17/9/2026): số văn bản chỉ ghi phần số hoặc số/ký hiệu (`3226/QĐ-UBND`), không
   kèm mã đuôi; tra về một dự án, doanh nghiệp, địa danh thì **chỉ tên riêng** — `Xuân Ái`, `PH Group`, `Châu Quế`
   — không viết "cụm công nghiệp Xuân Ái" vì cổng khớp chuỗi đúng từng chữ, còn văn bản viết CCN/Cụm CN/KCN mỗi
   nơi một kiểu. Bot cũng tự bỏ các chữ chung ở đầu và chỉ gõ phần số, nhưng đừng trông vào đó.
9. **Một hồ sơ có nhiều tệp.** Trang chi tiết có PDF chính và tab *File đính kèm* (dự thảo .docx, bảng so sánh,
   báo cáo…). Bot tải đủ: tệp gốc `<số>__dkN-<tên>` + bản chữ `.md` cho .docx/.pdf; mục *Tệp đính kèm* ở
   cuối phần đầu tệp `.md` chính. Khi đọc một văn bản xin ý kiến dự thảo, **đọc cả đính kèm** — nội dung
   thật nằm ở đó, công văn chính thường chỉ vài dòng. **PDF chính bot lưu có thể là tệp đính kèm đầu tiên**
   (khung xem của Data360X mở tệp đầu — vụ 9425/UBND-NC 17/9/2026: `9425_UBND-NC.pdf` thực ra là công văn
   4865/BCA của Bộ, còn công văn 9425 của tỉnh nằm ở `__dk3-…`): đối chiếu số ký hiệu ở đầu từng tệp `.md`
   trước khi trích dẫn. Trong `_ket-qua.json`, mỗi đính kèm có `tai_duoc: true/false`; false → xem log
   run (ref 03 mục 6), không tự kết luận nội dung.
10. **Tài liệu sau mã QR.** Công văn của Bộ, ngành hay chỉ in mã QR *"Đề nghị quét QR để tải tài liệu"*. Bot
    quét QR trong PDF chính và PDF đính kèm, tải tài liệu ở đường dẫn đó (Google Drive tệp/thư mục, trang web,
    tệp trực tiếp) thành đính kèm `<số>__qrN-<tên>`, ghi rõ URL trong mục *Tệp đính kèm*. Bot không tải được
    (thư mục Drive không công khai, trang cần đăng nhập) → mục đó ghi URL trong tệp `qr-khong-tai-duoc.txt`:
    đưa URL cho người dùng mở bằng tay, **không** đoán nội dung dự thảo.
11. **Từ khóa rộng bị chặn trần 12 văn bản** — bản tin kết quả ghi "Từ khóa quá rộng, bỏ qua N". Gặp dòng đó
    thì thu hẹp từ khóa hoặc dùng số ký hiệu, không kết luận "không có".
12b. **Đọc luồng xử lý trước khi chọn loại văn bản** (Bạn chốt 17/9/2026). Mỗi hồ sơ bot lấy có mục *Luồng xử lý*
    (từ tab *Thông tin gửi, nhận* trên Data360X): ai gửi ai, hành động *Xử lý chính / Phối hợp / Nhận để biết*,
    hạn xử lý. Bot đã suy sẵn vai trò của Phòng Công nghiệp:
    - **Chủ trì** (Trưởng phòng nhận *Xử lý chính*) → soạn **văn bản của Sở** (công văn, tờ trình… Lãnh đạo Sở ký);
      người xử lý chính trong luồng là **người soạn** — ghi vào dòng `Lưu: VT, CN(Tên)`.
    - **Phối hợp** → chuyên viên soạn **công văn nội bộ của Phòng** gửi phòng chủ trì (mẫu vbhc-vn template 08).
    - **Nhận để biết** → không soạn, chỉ theo dõi. Phòng không có trong luồng → hỏi người dùng.
    Hạn xử lý trong luồng là hạn **của Sở**; hạn ghi trong công văn của Bộ/tỉnh là hạn gửi đi — lấy hạn sớm hơn.
12. **Chrome trên máy cơ quan bị đóng giữa lượt** (người dùng đóng nhầm, máy khóa): bot tự mở lại và làm tiếp;
    `README.md` luôn được ghi kể cả khi lỗi, mục *Lượt lấy bị lỗi giữa chừng* cho biết phải gọi lại phần nào. Lệnh gửi lúc máy tắt nằm chờ tối đa 24 giờ rồi
   bị hủy. Xem `trang-thai/bot-chay.json` (nhịp tim) để biết máy im bao lâu trước khi hứa với người dùng.

## III. BỐN ĐỘNG TÁC

### 1. Tra kho đã gom

```bash
# tại thư mục chứa bản clone vlncn-laocai (hoặc đặt VLNCN_DIR), tìm theo từ khóa / số / lĩnh vực / ngày
python3 scripts/tim_trong_kho.py "tiêu chí lựa chọn chủ đầu tư" --linh-vuc kccn-sct-vn --tu 01/09/2026
python3 scripts/tim_trong_kho.py 5511/SCT-CN
python3 scripts/tim_trong_kho.py --ban-tin            # in bản tin mới nhất
```

Kết quả: từng dòng `số | ngày | đi/đến | lĩnh vực | trích yếu | tệp` — có `tệp` là đã có chữ để đọc ngay
(`theo-doi/2026/<số>.md`). Không có bản clone: script tự đọc qua GitHub API nếu có `GITHUB_TOKEN`
(hoặc `GH_TOKEN`, `BOT_GITHUB_TOKEN`) trong môi trường; trong phiên có MCP GitHub thì dùng
`get_file_contents` với `Trangsct/vlncn-laocai`, đường dẫn `theo-doi/danh-muc-2026.json`.

Tra xong mà tệp là `.pdf` (bản scan) → dựng ảnh trang bằng pymupdf rồi đọc bằng mắt (ref 04 mục 3).

### 2. Sai bot lấy đúng văn bản (cánh tay)

Workflow **`lay-van-ban.yml`** — *Lay van ban theo yeu cau (may co quan)*, kho `Trangsct/vlncn-laocai`,
`ref: main`. Inputs:

| input | ý nghĩa | ví dụ |
|---|---|---|
| `tim` | các mục cách nhau bằng `;` — mục có `/` là **số ký hiệu** (khớp đúng), còn lại là **từ khóa ngắn** trong trích yếu (không phân biệt dấu; tên riêng, không kèm chữ chung) | `5511/SCT-CN; 3226/QĐ-UBND; Xuân Ái; PH Group` |
| `ngay` | chỉ dùng khi ô tìm kiếm của cổng không hoạt động (bot phải lật trang): quét bao nhiêu ngày gần nhất, mặc định 60 | `90` |
| `ten` | tên thư mục kết quả (chữ không dấu, `-`); trống = ngày giờ | `ccn-xuan-ai-cham-diem` |

Gọi (chọn một):
```
MCP:   actions_run_trigger(method="run_workflow", owner="Trangsct", repo="vlncn-laocai",
                           workflow_id="lay-van-ban.yml", ref="main", inputs={"tim": "...", "ngay": "60", "ten": "..."})
gh:    gh workflow run lay-van-ban.yml -R Trangsct/vlncn-laocai -f tim="..." -f ngay=60 -f ten="..."
script: python3 scripts/goi_bot.py lay --tim "..." --ngay 60 --ten "..."   # tự chờ và in README kết quả
```

Bot **gõ từng mục vào ô tìm kiếm của Data360X** (Bạn chốt 17/9/2026) rồi đọc bảng kết quả — không lật từng
trang — nên văn bản cũ mấy năm cũng tìm được, không bị giới hạn bởi `ngay`.

Rồi **chờ**: xem run mới nhất của workflow (MCP `actions_list` `list_workflow_runs`, resource `lay-van-ban.yml`)
đến khi `status = completed`. Thời gian: 2–5 phút cho vài mục (mỗi mục là một lần tìm trên hai bảng đến/đi). Không chờ bằng vòng
lặp dày; kiểm tra sau 3 phút rồi mỗi 2 phút. Xong thì đọc
`theo-doi/yeu-cau/<ten>/README.md` (thấy gì, thiếu gì) và từng tệp `.md`/`.pdf` trong đó.

`conclusion = failure` → xem log job (ref 03 mục "khi bot hỏng"): phổ biến nhất là **phiên đăng nhập hết
hạn** (log có "Chờ đăng nhập") → báo người dùng đăng nhập lại trên máy cơ quan, sau đó gọi lại.

### 3. Quét mới cả văn bản đi + đến

Workflow **`quet-tren-may.yml`** — *Quet Data360X (may co quan)*, input `ngay` (mặc định 30). Tự chạy
**11h30 thứ Tư**; gọi tay khi người dùng nói "lấy văn bản tuần này", "quét lại", hoặc bản tin gần nhất cũ
hơn 4 ngày. Kết quả: giấy phép → `inbox/` (máy đọc vào cơ sở dữ liệu); văn bản mang quy định → `theo-doi/<năm>/`;
bản tin `theo-doi/bao-cao/<ngày>.md`. Sau khi xong, đọc bản tin và làm theo mục IV.

### 4. Tìm văn bản viện dẫn của một dự thảo

Workflow **`tim-van-ban.yml`** — *Tim van ban vien dan (may co quan)*, input `ho_so` = tên thư mục trong
`du-thao/` đã có `trich-dan.json` (do workflow *Soat du thao* sinh). Kết quả về `du-thao/<ho_so>/kem-theo/`.
Với danh sách số ký hiệu rời (không phải từ dự thảo) thì dùng động tác 2.

## IV. KHI NÀO TỰ ĐỘNG DÙNG (không chờ người dùng bảo)

| Tình huống trong phiên | Làm |
|---|---|
| Soạn tờ trình/báo cáo/công văn mà căn cứ là văn bản Sở nhận hoặc gửi gần đây | Động tác 1; thiếu → 2 |
| Người dùng nhắc một số ký hiệu (`5563/SCT-CN`, `3226/QĐ-UBND`…) mà phiên không có bản gốc | 1 → 2 |
| Cập nhật plugin (skill-sct) theo quy trình đầu phiên | Đọc bản tin mới nhất (1); cũ hơn 4 ngày → 3 |
| Soát dự thảo có viện dẫn | 4 |
| Thẩm định hồ sơ CCN/KCN/giấy phép cần công văn góp ý của các sở | 2 với từ khóa tên dự án + `ngay` 90 |
| Người dùng hỏi "tuần này có gì mới về X" | 1 với `--tu` 7 ngày; không đủ → 3 |

Trước khi trả lời người dùng, luôn ghi rõ **nguồn**: `số ký hiệu, ngày, tệp trong theo-doi/` hoặc
"bot quét N ngày không thấy".

## V. CÁC REFERENCE

| Tệp | Nội dung |
|---|---|
| `references/01-kho-theo-doi.md` | Cấu trúc `theo-doi/`: danh mục JSON (từng trường), bản tin, tệp `.md`/`.pdf`, `_da-gom`, `yeu-cau/`, `de-xuat-vbpl.csv`; bảng lĩnh vực ↔ plugin; giới hạn của kho |
| `references/02-workflows.md` | 4 workflow: tên tệp, inputs, thời gian, nơi trả kết quả, cách gọi bằng MCP / gh / script, cách đọc log lỗi |
| `references/03-bot-va-may-co-quan.md` | Bot làm gì, không làm gì; runner; phiên đăng nhập; giữ phiên hằng ngày; nhịp tim; các mã thoát; khi bot hỏng thì làm gì |
| `references/04-kich-ban-mau.md` | 5 kịch bản có thật, từng bước lệnh và câu trả lời mẫu cho người dùng |

## VI. LIÊN KẾT VỚI PLUGIN KHÁC

- `vbhc-pdf-reader-vn`: đọc số/ngày trên PDF ký số — dùng khi bot trả về `.pdf` (bản scan).
- `vbhc-vn`: sổ đăng ký VBPL công khai được nạp từ `theo-doi/de-xuat-vbpl.csv` (script
  `skill-sct/scripts/nap_vbpl_data360x.py`) — cùng nguồn Data360X, khác mục đích.
- `kccn-sct-vn` ref 32 và 37: quy trình cập nhật định kỳ từ dây chuyền này.
