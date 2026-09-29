# Reference 05 — TAY và hàng đợi `yeu-cau/` (từ 30/9/2026)

**Vì sao có:** đêm 29/9/2026 bot ngừng 11 ngày vì máy bàn cơ quan tắt, việc đăng ký GitHub runner lên laptop
hỏng 3 lần, lượt quét online trên máy chủ GitHub bị cổng Data360X từ chối (timeout). Bạn chốt xây lại: máy ở
Lào Cai chỉ là **"tay"** chép văn bản; Claude là **"não"**. Tiến trình `TAY` (`ccn-laocai/tay/tay.py`, cài bằng
`bot/cai-tay.bat`, đã qua máy ảo Windows) chạy ẩn trên laptop/máy bàn, **tự kéo việc** từ hàng đợi thay vì chờ
GitHub sai qua runner. Không có gì để đăng ký, không "already configured".

## TAY tự làm gì (không cần ai ra lệnh)

| Việc | Khi nào |
|---|---|
| Giữ phiên Data360X (Chrome thu nhỏ ~20 giây) | mỗi giờ 07–17h, thứ Hai–Bảy |
| Quét 30 ngày (như lượt thứ Tư cũ) | thứ Tư từ 11:30, hoặc bất cứ lúc nào trong giờ làm việc nếu đã quá 7 ngày chưa quét |
| Tự cập nhật `tay.py`, `bot-data360x.py` từ `main` kho ccn-laocai | mỗi vòng 10 phút |
| Nhịp tim `trang-thai/tay.json` (kho vlncn-laocai) | mỗi giờ và ngay sau mỗi việc |

## Ra lệnh cho TAY: ghi một tệp JSON vào `vlncn-laocai/yeu-cau/`

```json
{"loai": "lay",  "yeu_cau": "5511/SCT-CN; tiêu chí lựa chọn chủ đầu tư", "ngay": 60,
 "ten": "xuan-ai", "luu": "theo-doi/yeu-cau/xuan-ai", "trang_thai": "cho"}
{"loai": "tim",  "ho_so": "2026.09.03. To trinh ... CCN Phu Thinh 6", "trang_thai": "cho"}
{"loai": "quet", "ngay": 30, "trang_thai": "cho"}
{"loai": "giu-phien", "trang_thai": "cho"}
```

Ba cách ghi, chọn một:

1. **MCP GitHub trong phiên** — nhanh nhất, không cần workflow:
   `create_or_update_file(owner="Trangsct", repo="vlncn-laocai", branch="main", path="yeu-cau/2026-09-30_0900-lay.json", content=<JSON trên>, message="Yeu cau TAY: lay ...")`
2. **Workflow `yeu-cau.yml`** (*Yeu cau TAY (ghi vao hang doi)*, chạy trên GitHub, bấm từ điện thoại được):
   `actions_run_trigger(method="run_workflow", owner="Trangsct", repo="vlncn-laocai", workflow_id="yeu-cau.yml", ref="main", inputs={"loai": "lay", "yeu_cau": "...", "ngay": "60", "ten": "xuan-ai"})`
3. **Script**: `python3 scripts/goi_bot.py lay --tim "..." --ngay 60 --ten xuan-ai --qua-tay` (ghi qua workflow rồi chờ).

Tên tệp: `<YYYY-MM-DD_HHMMSS>-<loai>.json` để sắp theo thời gian.

## Chờ và đọc kết quả

TAY kéo hàng đợi **mỗi 10 phút**; việc `lay` mất thêm 3–15 phút. Đọc lại chính tệp yêu cầu: `trang_thai`
đi `cho` → `dang` (kèm `may`, `luc`) → `xong` hoặc `loi` (kèm `tom_tat`, `xong_luc`). Kết quả:

| loai | Kết quả về |
|---|---|
| lay | `theo-doi/yeu-cau/<ten>/README.md` + `.md`/`.pdf` (như ref 02) |
| tim | `du-thao/<ho_so>/kem-theo/` |
| quet | `inbox/`, `theo-doi/<năm>/`, `theo-doi/bao-cao/<ngày>.md` |
| giu-phien | không có tệp; `tom_tat` ghi phiên còn hay hết |

`trang_thai` không đổi sau 30 phút → TAY không chạy trên máy nào: xem `trang-thai/tay.json` (`luc` cũ hơn 2 giờ
là máy tắt hoặc chưa cài), báo người dùng bật máy hoặc nháy đúp `cai-tay.bat`. **Không** ghi lại yêu cầu lần
hai khi tệp cũ còn `cho`/`dang`.

## Quan hệ với bốn workflow cũ (ref 02)

Bốn workflow trên runner (`lay-van-ban.yml`, `quet-tren-may.yml`, `tim-van-ban.yml`, `giu-phien.yml`) vẫn còn
cho tới khi TAY chạy song song ổn một tuần; chúng chỉ chạy khi có runner đăng ký và trực tuyến. Từ 30/9/2026
**ưu tiên hàng đợi TAY**; chỉ dùng workflow cũ khi `trang-thai/tay.json` không có mà runner lại đang Idle.
