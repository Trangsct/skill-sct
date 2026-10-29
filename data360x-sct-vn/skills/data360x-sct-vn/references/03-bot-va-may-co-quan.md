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
| `--lay "a; b; c" --luu DIR` (hoặc `--lay @tệp.txt`) | lấy văn bản theo yêu cầu: gõ từng mục vào **ô tìm kiếm** của cổng, đọc bảng kết quả; `--ngay N` chỉ dùng khi ô tìm không hoạt động (lật trang) |
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

## 6. Cách bot tải đính kèm trên Data360X (từ 17/9/2026)

- Cổng là SPA (PrimeReact); backend `csdlvb-backend.laocai.gov.vn` **thiếu chứng thư trung gian** và giữ token
  đăng nhập ở localStorage (không ở cookie). Vì thế request riêng chỉ mang cookie bị 401, `ctx.request` lỗi
  chứng thư, fetch trong trang bị CORS, bấm hàng .pdf từng làm Chrome sập.
- Bot bắt hai thứ từ chính Chrome khi mở trang chi tiết: header `Authorization` gửi tới backend, và **URL đầy đủ
  Chrome dùng để tải tệp đầu** (`…/get-attach-by-id/<tên tệp>?attachId=…&token=…&isOld=…`). Danh sách tệp lấy
  từ JSON `get-attachs-by-id` (`attacH_ID`, `attacH_NAME`). Tệp còn lại tải bằng cách thay tên + attachId vào
  khuôn URL đó, qua request context `ignore_https_errors`. Kết quả lượt 23:31 17/9/2026: 3/3 tệp.
- Trong log run, `token=` bị che (`token=…`). Log có các dòng để soi: `API backend đã thấy`, `URL tải tệp Chrome
  đã dùng`, `JSON đính kèm (đầu)`, `<tên>: tải theo khuôn URL của Chrome (N bytes)`; trượt thì `KHÔNG tải được`
  kèm HTTP status. `chưa bắt được Authorization của backend` → trang chi tiết chưa gọi backend (phiên hết hạn
  hoặc cổng đổi) — xem mục 5.
- Đường dự phòng vẫn giữ trong `tai_dinh_kem`: URL trần từ JSON (hiện 400), URL có sẵn trong HTML, quét lân cận
  attachId ±24 theo tên trong content-disposition.

## 7. Chuyển sang EGOV (từ 10/10/2026, Bạn báo 21/10/2026)

- **Nguồn mới:** nền tảng chính quyền số EGOV của tỉnh, `https://egov1.laocai.gov.vn/home/default/1`. Data360X
  (`csdlvb.laocai.gov.vn`) dừng ở lượt quét 10/10/2026 (738 văn bản đi + đến từ 28/9); giữ lại làm nơi tra văn bản cũ.
- **Claude không vào được egov1** từ máy chủ nước ngoài (cổng chặn, giống Data360X) → mọi thao tác trên EGOV đi qua máy ở
  Lào Cai, với phiên Bạn tự đăng nhập. Không tự đăng nhập, không giải mã xác thực, không bấm nút thao tác hồ sơ.
- **Bước 1 — soi (đã có từ 21/10/2026):** `scripts/egov_soi.py` + `bot/soi-egov.bat` (kho `ccn-laocai`, PR #113). Bạn chạy
  một lần (dòng PowerShell ở đầu `bot/HUONG-DAN-CAI-BOT.md`): bot tự đi theo liên kết menu Văn bản đến/đi, mở thử văn bản đầu
  bảng, rồi Bạn tự bấm 10 phút (mở văn bản, xem đính kèm, mục Chờ xử lý, ô tìm kiếm). Kết quả ở kho riêng tư
  `vlncn-laocai/theo-doi/egov/soi/<ngày-giờ>/`: `README.md` (trang đã qua, khuôn API), `trang.json` (menu, bảng, ô nhập),
  `api.jsonl` (từng yêu cầu, mẫu phản hồi cắt ngắn), `trang/*.html`, `anh/*.jpg`. Mã phiên, mật khẩu, cookie đã che.
- **Bước 2 — bot EGOV (xong 29/10/2026, ccn-laocai PR #114):** `bot-data360x.py` thêm bộ đọc egov1 (hàm `_egov_*`) và lấy
  egov1 làm cổng mặc định (`"he_thong": "data360x"` trong `config.json` để quay lại). Dựng từ ảnh chụp danh sách Văn bản đến
  `/document/xem-den-index?type=all` (cột STT, Cấp độ, Trích yếu, Số ký hiệu, Ngày Ban Hành, Ngày Nhận, Trạng thái, Cơ quan ban
  hành, Người Ký, Độ mật, Nguồn văn bản) — phần chưa thấy tận mắt bot tự dò: vào Văn bản đi bằng cách bấm menu, 100 dòng/trang,
  tải tệp qua Chrome (link, khung xem PDF, bấm tên tệp). Đầu ra giữ nguyên (`danh-muc-<năm>.json`, `bao-cao/<ngày>.md`,
  `inbox/`, `yeu-cau/<ten>/`), `url_chi_tiet` trỏ về egov1; mới: `theo-doi/viec-cho-xu-ly/<ngày>/`. Văn bản Độ mật khác "Thường"
  bị bỏ hẳn. Lượt chạy đầu tự **khảo sát** cổng lên `theo-doi/egov/soi/<ngày-giờ>-bot/` (HTML, ảnh, cột nhận ra, API đã che mã)
  — có thư mục này mà bản tin vẫn trống/lỗi thì đọc nó và sửa `_egov_*`.
- **Lịch TAY 0.2.0** (máy ở Lào Cai, cài bằng `cai-tay.bat`): giữ phiên mỗi giờ 07–17h thứ Hai–Bảy; **07:30 thứ Hai–Sáu** việc
  chờ xử lý; **16:30 thứ Hai–Sáu** quét 7 ngày (thứ Tư 11:30 quét 30 ngày). Bấm tay: `quet-lai-ngay.bat`, `viec-cho-xu-ly.bat`,
  `khao-sat-egov.bat`; phiên hết thì `dang-nhap-lan-dau.bat` (Bạn tự nhập mã xác thực).
- Mở trang chi tiết trên egov1 có thể đổi văn bản từ "chưa đọc" sang "đã đọc" trên giao diện của Bạn (chưa kiểm trên cổng thật).
  Bot không bấm Chuyển, Ký, Hoàn thành hay nút thao tác hồ sơ nào.
