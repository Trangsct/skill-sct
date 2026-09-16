# Hướng dẫn cài đặt / cập nhật plugin vbhc-vn

## Cài mới (khuyến nghị: xóa bản cũ, cài bản mới hoàn toàn)

1. Trong Claude.ai: Settings → Capabilities (hoặc mục quản lý Skills/Plugins) → gỡ skill/plugin `vbhc-vn` cũ (cả bản user skill lẫn bản plugin nếu có 2 bản — tránh trùng trigger).
2. Tải lên file `vbhc-vn-vX.Y.Z.zip` (bản mới nhất trong repo `Trangsct/skill-sct`).
3. Kiểm tra sau cài: hỏi Claude "kiểm tra plugin vbhc-vn" — Claude phải đọc được `SKILL.md` tại `/mnt/skills/plugins/vbhc-vn:vbhc-vn/SKILL.md`.

## Cấu trúc gói (chuẩn plugin từ 04/7/2026)

```
vbhc-vn-vX.Y.Z.zip
├── .claude-plugin/plugin.json     ← manifest (bắt buộc, ở gốc zip)
└── skills/vbhc-vn/
    ├── SKILL.md                   ← description ≤ 1024 bytes UTF-8
    ├── templates/  (09 mẫu trắng)
    ├── examples/   (17 mẫu thật: 11 sct + 6 ubnd)
    ├── reference/  (thể thức NĐ 30, 8 nhóm anti-error, công cụ kỹ thuật...)
    └── scripts/    (fill_template, extract_metadata, check_document, qa_pdf_check)
```

## Quy trình bắt buộc sau mỗi lần build/chỉnh/nâng cấp

1. Chạy validator đóng gói (kiểm description bytes, ASCII paths, cấu trúc zip) TRƯỚC khi xuất.
2. Cập nhật `CHANGELOG.md` (bắt buộc, không cần nhắc).
3. Push GitHub repo `Trangsct/skill-sct` — nếu phiên Claude.ai không có credentials thì tải zip về và push thủ công (hoặc dùng Claude Code có GitHub App).

## Ghi chú đường dẫn

Skill cài dạng **plugin** nằm tại `/mnt/skills/plugins/vbhc-vn:vbhc-vn/`; cài dạng **user skill** nằm tại `/mnt/skills/user/vbhc-vn/`. Các script trong tài liệu viết theo đường dẫn plugin — nếu dùng bản user skill thì thay tiền tố tương ứng.

## Quy trình khi phát hiện lỗi mới (từ bản 2.23.0, Bạn chốt 16/9/2026)

Từ nay khi phát hiện một lỗi soạn thảo mới thì không viết thêm một đoạn văn xuôi vào SKILL.md
nữa, mà thêm một hàm kiểm và một trường hợp thử. Bốn bước, làm tuần tự.

Bước một. Lưu file lỗi. Chép file .docx đang mắc lỗi vào thư mục tests/fail của plugin, đặt tên
theo dạng mã quy tắc và mô tả ngắn, ví dụ r16-thieu-dau-cham-cuoi.docx. Tạo cạnh nó một file
cùng tên nhưng đuôi .expect, trong đó ghi ba thứ: các dòng bắt đầu bằng dấu thăng là ghi chú
nói rõ đã sửa gì so với bản gốc; một dòng nguon: trỏ tới mẫu thật đã dùng làm bản gốc; và mỗi
dòng còn lại là một mã quy tắc kèm mức, ví dụ R16 FAIL. Nếu chưa có file lỗi thật thì chép một
mẫu thật trong examples ra rồi sửa có chủ đích đúng một chỗ, và ghi rõ trong phần ghi chú rằng
đây là file lỗi nhân tạo. Tuyệt đối không bịa số hiệu hay ngày tháng văn bản mới; số hiệu trong
file lỗi phải lấy nguyên từ chính mẫu thật.

Bước hai. Viết hàm kiểm. Mở scripts/qa_rules.py, viết một hàm mới tên rule_R kèm số thứ tự tiếp
theo, nhận vào doc và ctx, trả về danh sách phát hiện. Docstring của hàm bắt buộc ghi bốn thứ:
mã quy tắc, nội dung quy tắc bằng tiếng Việt, nguồn gồm số quy tắc trong SKILL.md hoặc tên nhóm
trong phong tranh sai lam kèm ngày chốt, và mức là FAIL hay WARN. Đăng ký hàm vào bảng RULES ở
cuối file. Nếu quy tắc chỉ là một danh sách cụm từ thì không viết vào code mà thêm dòng vào file
tương ứng trong thư mục data, như thuat-ngu-cam.txt hoặc giong-giai-thich.txt.

Bước ba. Chạy hồi quy. Gõ lệnh python3 tests/run_regression.py tại thư mục plugin. Lệnh này kiểm
hai chiều: toàn bộ mẫu thật trong examples không được có lỗi FAIL nào, và mỗi file trong tests
fail phải bị bắt đúng mã đã ghi. Nếu quy tắc mới làm một mẫu thật bị FAIL thì quy tắc viết sai
hoặc hiểu sai, phải sửa quy tắc chứ tuyệt đối không sửa mẫu thật. Nếu quy tắc mới chỉ làm phát
sinh cảnh báo WARN mới trên mẫu thật mà xét thấy cảnh báo đó là đúng thì chạy lại lệnh trên kèm
tham số hai gạch cap-nhat-baseline để chốt lại mốc.

Bước bốn. Tăng phiên bản và ghi nhật ký. Mở file plugin.json trong thư mục chấm claude-plugin,
tăng số phiên bản. Thêm một file CHANGELOG theo mẫu ngày tháng trong thư mục skill và thêm một
mục mới lên đầu file CHANGELOG ở gốc kho. Chạy python3 scripts/sync_marketplace.py với tham số
hai gạch bump tại gốc kho, không sửa tay marketplace.json.

Sau khi làm xong bốn bước, đẩy lên nhánh làm việc và mở pull request như thường lệ. Job qa-evals
trên GitHub sẽ tự chạy lại bước ba; job này đỏ thì không merge được.

## Cách tự chạy bộ kiểm thử

Chạy lớp một, tức phần tất định không gọi mô hình, bằng lệnh sau, gõ tại thư mục
vbhc-vn/skills/vbhc-vn của kho skill-sct:

    python3 tests/run_regression.py

Thêm tham số hai gạch chi-tiet để xem kết quả từng file. Thêm tham số hai gạch voi-qa-all để
chạy thêm qa_all.py trên toàn bộ mẫu thật; phần này cần cài LibreOffice nên chậm hơn, khoảng
một phút.

Chạy lớp hai, tức phần giao đề bài thật cho Claude Code rồi chấm sản phẩm, bằng lệnh:

    bash tests/run_cases.sh

Muốn chạy vài trường hợp thôi thì ghi thêm số thứ tự, ví dụ bash tests/run_cases.sh 01 05. Lệnh
này gọi Claude Code nên chỉ chạy khi cần, không chạy trên GitHub. Sản phẩm và nhật ký từng lần
chạy nằm trong tests/_ket-qua.

Muốn kiểm một file bất kỳ bằng riêng bộ quy tắc, không cần render ảnh, thì gõ:

    python3 scripts/qa_rules.py duong-dan-file.docx

Thêm hai gạch only kèm mã quy tắc để chạy một quy tắc, ví dụ hai gạch only R03. Thêm hai gạch
final khi đây là bản hoàn thiện để xuất bản, khi đó các cảnh báo về chỗ trống và chữ tím được
nâng thành lỗi chặn.
