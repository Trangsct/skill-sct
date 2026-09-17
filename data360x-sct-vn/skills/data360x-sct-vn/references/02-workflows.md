# Reference 02 — Bốn workflow là bốn nút bấm (kho `Trangsct/vlncn-laocai`)

Tất cả chạy trên runner tự cài ở máy cơ quan (`runs-on: [self-hosted, windows, laocai]`, tên runner
`may-so-cong-thuong`), trừ *De xuat VBPL* chạy trên GitHub. Máy tắt → lệnh nằm chờ tối đa 24 giờ rồi bị
hủy (`conclusion: cancelled`).

| Tệp workflow | Tên hiện trên GitHub | Inputs | Kết quả về | Thời gian |
|---|---|---|---|---|
| `lay-van-ban.yml` | Lay van ban theo yeu cau (may co quan) | `tim` (bắt buộc), `ngay` (60), `ten` | `theo-doi/yeu-cau/<ten>/README.md` + tệp | 3–15 phút |
| `quet-tren-may.yml` | Quet Data360X (may co quan) | `ngay` (30) | `inbox/`, `theo-doi/<năm>/`, `theo-doi/bao-cao/<ngày>.md` | 5–15 phút; lịch 11h30 thứ Tư |
| `tim-van-ban.yml` | Tim van ban vien dan (may co quan) | `ho_so` (tên thư mục trong `du-thao/`) | `du-thao/<ho_so>/kem-theo/` | 3–10 phút |
| `giu-phien.yml` | Giu phien Data360X (may co quan) | — | không có tệp; log báo phiên còn/hết | 20 giây; lịch 08h00 thứ Hai–Bảy |
| `de-xuat-vbpl.yml` | De xuat VBPL tu Data360X | — | `theo-doi/de-xuat-vbpl.csv` | 1 phút; 13h30 thứ Tư |

Tất cả `ref` = `main`.

## Cách gọi

**MCP GitHub (phiên Claude Code có kết nối GitHub)**
```
actions_run_trigger(method="run_workflow", owner="Trangsct", repo="vlncn-laocai",
                    workflow_id="lay-van-ban.yml", ref="main",
                    inputs={"tim": "5511/SCT-CN; tiêu chí lựa chọn chủ đầu tư", "ngay": "60", "ten": "xuan-ai"})
actions_list(method="list_workflow_runs", owner="Trangsct", repo="vlncn-laocai",
             resource_id="lay-van-ban.yml", perPage=1)          # xem run mới nhất: status, conclusion, id
actions_list(method="list_workflow_jobs", ..., resource_id=<run id>)   # từng bước
get_job_logs(owner=..., repo=..., run_id=<run id>, failed_only=true, return_content=true)   # khi failure
get_file_contents(owner="Trangsct", repo="vlncn-laocai", path="theo-doi/yeu-cau/xuan-ai/README.md")
```

**gh CLI**
```
gh workflow run lay-van-ban.yml -R Trangsct/vlncn-laocai -f tim="..." -f ngay=60 -f ten="xuan-ai"
gh run list -R Trangsct/vlncn-laocai -w lay-van-ban.yml -L 1
gh run watch <run id> -R Trangsct/vlncn-laocai
```

**Script trong plugin** (cần `GITHUB_TOKEN`/`GH_TOKEN`/`BOT_GITHUB_TOKEN` có quyền Actions: write trên kho)
```
python3 scripts/goi_bot.py lay  --tim "..." --ngay 60 --ten xuan-ai     # gửi lệnh, chờ, in README kết quả
python3 scripts/goi_bot.py quet --ngay 30
python3 scripts/goi_bot.py tim  --ho-so "2026.09.03. To trinh ... Phu Thinh 6"
python3 scripts/goi_bot.py giu-phien
python3 scripts/goi_bot.py trang-thai      # nhịp tim máy + run gần nhất của từng workflow
```

**Trang web** (khi phiên không có công cụ nào): đưa người dùng đường dẫn
`https://github.com/Trangsct/vlncn-laocai/actions/workflows/lay-van-ban.yml` → *Run workflow* → dán đúng
chuỗi `tim` Claude đã soạn. Bấm từ điện thoại cũng được.

## Chờ kết quả

1. Sau khi gửi, đợi ~3 phút rồi xem run mới nhất; `status` đi `queued → in_progress → completed`.
2. `queued` quá 10 phút = máy cơ quan đang tắt hoặc chưa đăng nhập Windows → báo người dùng, không chờ vô hạn.
3. `completed` + `conclusion: success` → đọc kết quả. `failure` → đọc log job (mục dưới).
4. Không gửi lệnh thứ hai của cùng workflow khi lệnh trước chưa `completed` (runner chỉ chạy một việc một lúc,
   lệnh sau xếp hàng).

## Đọc log khi `failure`

| Dòng trong log | Nghĩa | Làm |
|---|---|---|
| `Chờ đăng nhập, lần 1/6` rồi `TargetClosedError` / `Hết thời gian chờ đăng nhập` | phiên Data360X hết hạn, người dùng chưa đăng nhập lại | Báo: "trên máy cơ quan mở `dang-nhap-lan-dau.bat`, đăng nhập, rồi tôi gọi lại" |
| `Chưa có github_token trong config.json` | máy chưa cấu hình | Người dùng chạy `cai-dat.bat` |
| `Không nhận ra cột bảng` | Data360X đổi giao diện | Chạy `chay-thu.bat` (chế độ soi) và gửi `logs/soi` cho Claude sửa selector |
| `Yêu cầu rỗng` | `tim` trống hoặc chỉ có dấu `;` | Gửi lại |
| `refusing to allow ... workflow` khi đẩy | token bot không có scope workflow | Không liên quan tệp kết quả; chỉ xảy ra khi bot đụng `.github/` — báo Claude |

Mã thoát của bot: `0` xong; `1` lỗi chung; `2` thiếu cấu hình; `3` phiên hết hạn / không đăng nhập được;
`4` (chế độ online) chưa có phiên xuất.
