# Reference 03 — Bot, máy cơ quan và phiên đăng nhập

## 1. Bot là gì

`ccn-laocai/scripts/bot-data360x.py` (Python + Playwright, Chrome thật có giao diện), cài tại `D:\du-an\bot`
(máy không có ổ D: `C:\du-an\bot`) bằng `cai-dat.bat`; hồ sơ Chrome + `config.json` + log tại
`D:\du-an\bot-profile`. Mỗi lần chạy, workflow tải bản mới nhất của script từ kho `ccn-laocai` (qua
`api.github.com`, không qua CDN) nên sửa script xong là máy dùng ngay.

Chế độ dòng lệnh:

| Lệnh | Việc |
|---|---|
| `--ngay N` (mặc định) | quét đi + đến N ngày: giấy phép → `inbox/`; gom tri thức → `theo-doi/` |
| `--lay "a; b; c" --ngay N --luu DIR` | lấy văn bản theo yêu cầu (số ký hiệu / từ khóa) |
| `--tim trich-dan.json --luu DIR` | tìm văn bản viện dẫn của dự thảo |
| `--giu-phien` | mở trang chủ rồi đóng, giữ phiên SSO |
| `--dang-nhap` | mở Chrome để người dùng đăng nhập lần đầu (`dang-nhap-lan-dau.bat`) |
| `--soi` | chế độ soi giao diện, không đẩy gì (`chay-thu.bat`) |
| `--khong-gom`, `--gom-toi-da N` | tắt / đổi trần bước gom tri thức |
| `--online` | chạy trên GitHub bằng phiên đã xuất — dự phòng, cổng hay từ chối máy chủ nước ngoài |

## 2. Bot KHÔNG làm gì (ràng buộc của người dùng, không đổi)

- **Không đăng nhập hộ, không giải captcha dưới bất kỳ hình thức nào.** Phiên hết → bot mở cửa sổ Chrome,
  báo Windows + Telegram, chờ tối đa 6 × 15 phút cho người dùng tự đăng nhập; Chrome bị đóng thì mở lại.
- **Chỉ lấy dữ liệu từ Data360X** (csdlvb.laocai.gov.vn). Cổng vOffice cũ bỏ hẳn.
- Không bịa: không đọc được PDF thì ghi "không tải được PDF", để trống.
- Không đưa văn bản nội bộ sang kho công khai.

## 3. Máy cơ quan và runner

- Runner GitHub Actions tên `may-so-cong-thuong`, nhãn `self-hosted, windows, laocai`, cài bằng
  `cai-runner.bat` (kho `ccn-laocai/bot/`), chạy **ẩn trong phiên đăng nhập Windows của người dùng** (không phải
  dịch vụ) — vì bot cần Chrome thật và cookie phiên mã hóa theo tài khoản.
- Tự bật lại mỗi lần đăng nhập Windows; cứ 30 phút Task Scheduler kiểm tra một lần.
- Kiểm tra máy còn nối GitHub: `https://github.com/Trangsct/vlncn-laocai/settings/actions/runners` phải xanh
  **Idle**; hoặc `trang-thai/bot-chay.json` (`lan_cuoi` là lần bot chạy gần nhất, `may` là tên máy).
- Máy tắt/ngủ: lệnh nằm chờ (`queued`) tối đa 24 giờ. Đừng hứa "vài phút" khi `bot-chay.json` cho thấy máy đã
  im nhiều ngày — hỏi người dùng máy có bật không.

## 4. Phiên đăng nhập Data360X

- Đăng nhập qua `login.yenbai.gov.vn` (SSO, có captcha) — chỉ người dùng làm, trong Chrome hồ sơ của bot.
- Phiên sống vài ngày. Từ 17/9/2026 workflow `giu-phien.yml` mở trang chủ **08h00 thứ Hai–Bảy** để phiên
  không hết giữa hai lượt quét (vụ 16/9/2026: phiên hết, lượt quét thứ Tư đổ). Phiên hết thì bot báo ngay hôm
  đó; người dùng chạy `dang-nhap-lan-dau.bat` lúc rảnh.
- Khi Claude gọi bot mà log báo chờ đăng nhập: **dừng, báo người dùng**, không gọi lại liên tục.

## 5. Khi bot hỏng — thứ tự kiểm tra

1. Run `cancelled` sau 24 giờ `queued` → máy tắt. 2. `failure` với "Chờ đăng nhập" → phiên hết hạn.
3. `failure` với `Không nhận ra cột bảng` / `không tìm thấy PDF` hàng loạt → Data360X đổi giao diện: cần
   `chay-thu.bat` gửi `logs/soi` để sửa selector trong `bot-data360x.py`. 4. `0 dòng` ở trang đầu → cổng từ chối
   phiên/máy (thường ở chế độ online). 5. Lỗi khác → đọc `D:\du-an\bot-profile\logs\<ngày>.log` trên máy.

Sửa bot = sửa `scripts/bot-data360x.py` ở kho `ccn-laocai` (công khai — không ghi khóa, không ghi tên
người vào code), mở PR, merge; máy tự lấy bản mới ở lượt sau.
