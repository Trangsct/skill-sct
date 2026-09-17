# vbhc-vn 2.24.0 — 16–17/9/2026

Chuyển quy tắc soạn thảo từ văn xuôi sang kiểm tra bằng máy, và dựng bộ kiểm thử hồi quy.

Nguồn: Bản giao việc ngày 16/9/2026 của Trần Trọng Trang, Phó Trưởng phòng Quản lý công nghiệp.

Số phiên bản: đợt này bắt đầu là 2.23.0, nhưng trong lúc làm, hai phiên khác đã phát hành 2.22.1
(Nhóm M), 2.23.0 (Quy tắc 28, `fit_pages.py`) và 2.23.1 (Nhóm N, `normalize_body.py`) lên `main`.
Khi gộp, Quy tắc 28 được đưa vào `reference/quy-tac-bat-bien.md`, Nhóm M và N thành hai dòng
trong bảng A–N của SKILL.md, hai script mới vào bảng QA và bảng định tuyến. Bản gộp lấy số 2.24.0.

## Vì sao làm

SKILL.md đã 62 KB với 27 quy tắc bất biến và 12 nhóm sai lầm A–L, phần lớn chỉ là lời dặn,
máy không kiểm. Hệ quả kép: soạn thì chậm vì phải nạp hết, và quy tắc càng nhiều thì càng dễ
bỏ sót. Thêm nữa, mỗi lần nâng cấp plugin không có gì bảo đảm chỗ khác không hỏng theo —
bản 2.18.2 đã phải sửa lỗi trang trắng do keepNext sinh ra từ một lần nâng cấp trước.

## Thêm

- **scripts/qa_rules.py** — 15 quy tắc máy kiểm R01–R15. Mỗi hàm có docstring ghi mã quy tắc,
  nội dung bằng tiếng Việt, nguồn (số quy tắc trong SKILL.md hoặc nhóm A–L, ngày Bạn chốt) và
  mức FAIL/WARN. Chạy lẻ: `python3 scripts/qa_rules.py file.docx [--only R03] [--final] [--json]`.
  Bảng đăng ký `RULES` để `qa_all.py` duyệt qua.
- **scripts/qa_all.py mục 1b** — gọi bộ quy tắc trên, in cùng định dạng PASS/FAIL. Thêm cờ
  `--final` cho bản Bạn yêu cầu "hoàn thiện để xuất bản" (nâng WARN nhóm hoàn thiện thành FAIL).
- **data/** — bổ sung quy tắc mà không phải sửa code: `thuat-ngu-cam.txt` (R09 mức FAIL),
  `thuat-ngu-canh-bao.txt` (R09 mức WARN), `giong-giai-thich.txt` (R10, lấy đúng Nhóm J),
  `vbpl.json` (kho dữ kiện văn bản pháp luật cho R05 — đợt này tạo cấu trúc rỗng).
- **tests/run_regression.py** — hồi quy lớp 1, tất định, chạy trên CI. Kiểm hai chiều:
  26 mẫu thật không được có FAIL nào và không được phát sinh WARN mới (`baseline-warn.json`);
  11 file lỗi phải bị bắt đúng mã ghi trong `.expect` và không bắt thừa.
- **tests/fail/** — 11 file lỗi nhân tạo, mỗi file là bản sao một mẫu thật được sửa có chủ đích,
  kèm `.expect` ghi mã bắt buộc FAIL/WARN và dòng `nguon:` trỏ về mẫu gốc. Số hiệu văn bản trong
  file lỗi lấy nguyên từ mẫu thật — không bịa số, ngày mới.
- **tests/run_cases.sh + tests/cham_case.py + tests/cases/** — kiểm thử lớp 2 (có gọi mô hình),
  12 case đề bài thật kèm `tieu-chi.txt` (require/forbid/rule-pass/trang). NHÁP chờ Bạn duyệt.
- **tests/rule-inventory.md** — kiểm kê toàn bộ quy tắc đang tồn tại, phân loại M (máy kiểm được)
  / N (không), và 4 chỗ quy tắc văn xuôi LỆCH với mẫu thật cần Bạn chốt.
- **CI**: job `qa-evals` trong `.github/workflows/validate-plugins.yml` — cài LibreOffice,
  poppler-utils, python-docx, Pillow rồi chạy hồi quy lớp 1.

## Sửa

- SKILL.md: 62.085 → 59.363 byte. Các quy tắc đã có hàm kiểm chạy đúng được rút thành dòng
  dẫn chiếu mã: Quy tắc 10 (`HDR-BR`), 20 (`[F]`), 22 (`SIGSPACE`), 25 (**R02**), 27 (**R03**,
  **R04**, **R13**); mục thể thức lề và lùi đầu dòng (**R12**, **R13**); dòng Lưu (**R07**);
  Nhóm A (**R01**), C (**R08**), D (**R05**), G (**R06**, **R07**), J (**R10**).
- Hiệu chỉnh theo nguyên tắc "mẫu thật là chuẩn" — ba quy tắc khi đưa vào máy đã bắt chính mẫu
  thật, nên quy tắc được sửa chứ không sửa mẫu:
  - **R01** thu về vùng căn cứ (FAIL) và hạ xuống WARN ở thân văn bản; miễn trừ Luật, Nghị quyết
    Quốc hội (dẫn theo số/năm, không kèm ngày).
  - **R04** hạ phần "thẳng cột" xuống WARN — mẫu thật `cong-van-ubnd-tinh-chi-dao.docx` căn khối
    Kính gửi bằng khoảng trắng dẫn đầu chứ không bằng indent.
  - **R12** hạ lệch chuẩn lề xuống WARN — 4/26 mẫu thật lệch có chủ đích (phôi GCN 2,54 cm…).

## Chưa đạt, đã ghi lại để Bạn quyết

- ~~Tiêu chí "SKILL.md giảm ≥ 20%" mới đạt 4,4%~~ — **đã đạt 71%** sau khi Bạn cho làm tiếp
  Việc 4 (tinh gọn theo mô hình lõi và định tuyến). Ghi chép ban đầu giữ lại để thấy vì sao: Nguyên tắc IV.3 của bản giao việc chỉ cho
  phép xóa văn xuôi khi hàm kiểm tương ứng PASS trên toàn bộ examples/; các quy tắc 11–14
  (LINES, SZ13, WIDOW, SIGSPLIT) chưa PASS nên văn xuôi phải giữ. Phần còn lại là loại N hoặc
  thuộc việc tái cấu trúc SKILL.md mà mục III đã hoãn sang đợt sau.
- **`qa_all.py` đang FAIL 24/26 mẫu thật** — nợ kỹ thuật có sẵn từ trước 2.23.0 (SIGSPACE 13 file,
  SZ13 12, LINES 5, HDR-BR 1). Bộ quy tắc mới đóng góp 0 FAIL. Đã chốt hiện trạng vào
  `tests/baseline-qa-all.json` để nâng cấp sau không làm tệ thêm. Chi tiết: mục D.4 của
  `tests/rule-inventory.md`.

## Làm thêm ngoài bản giao việc (Bạn giao tiếp 16/9/2026)

- **Kho dữ kiện văn bản pháp luật có kiểm chứng.** `scripts/build_vbpl.py` ở gốc kho sinh
  `data/vbpl.json` từ `registry/trang-thai.csv` — một nguồn duy nhất, không lập kho thứ hai.
  Hiện 62 văn bản, 35 có ngày ban hành, 37 có ngày hiệu lực. `scripts/cite_check.py` quét mọi
  số hiệu trong bản thảo và chia ba nhóm KHỚP / LỆCH / CHƯA CÓ; cờ `--to-tim` bôi tím chỗ cần
  tra. Script không tự kết luận là bịa và không tự sửa số hiệu.
- **Trình biên dịch nội dung sang .docx.** `scripts/build_vb.py` dựng 8 loại văn bản từ một file
  nội dung dạng thẻ trên mẫu thật, tự tách run chỉ số dưới cho công thức hóa học và chỉ số trên
  cho m2, m3, tự lùi đầu dòng đồng đều. Bộ hồi quy mục 4 dựng thử cả 8 loại mỗi lần chạy.
- **Tinh gọn SKILL.md theo mô hình lõi và định tuyến.** 62.085 → 17.771 byte (giảm 71%). Ba khối
  lớn chuyển sang reference, KHÔNG xóa: `reference/quy-tac-bat-bien.md` (đủ 27 quy tắc),
  `reference/the-thuc-van-phong.md`, `reference/quy-trinh-hai-che-do.md`. SKILL.md nay gồm:
  nguyên tắc lõi, **bảng định tuyến loại văn bản → mẫu → `--loai` → reference cần đọc**, 10 quy
  tắc phải nhớ không tra, bảng lệnh QA, bảng 12 nhóm A–L mỗi nhóm một dòng kèm mã máy kiểm.
  Đã đối chiếu máy: đủ 27 quy tắc, đủ 12 nhóm A–L, mọi file reference và script còn được nhắc,
  các `--loai` và đường dẫn mẫu trong bảng định tuyến đều tồn tại thật.

## Bổ sung 17/9/2026 — tự động hóa tối đa theo yêu cầu của Bạn

- **`qa_all.py` PASS 26/26 mẫu thật** (trước: 2/26). Hiệu chỉnh 4 hàm kiểm cũ theo mẫu thật:
  SZ13 (trống/27/28 → WARN, cỡ lạ hoặc mất nghiêng → FAIL), SIGSPACE (chỉ điều kiện ô ký ≥3 dòng
  trống giữ FAIL), LINES (đếm cả `w:drawing`; FAIL chỉ khi `--goc` cho thấy mất shape so với mẫu gốc),
  HDR-BR (chỉ xét khi bảng 0 là header). Thêm 4 file lỗi tương ứng; bộ hồi quy nay 16 file lỗi và
  yêu cầu mẫu thật PASS hoàn toàn `qa_all.py`, không còn "không tệ hơn baseline".
- **Kho VBPL nạp từ Data360X**: `vlncn-laocai/scripts/de-xuat-vbpl.py` lọc văn bản của cơ quan
  ban hành công khai (NĐ-CP, TT-B*, QĐ-TTg, QĐ-B*, NQ-CP, QĐ-UBND…) từ danh mục csdlvb.laocai.gov.vn;
  `scripts/nap_vbpl_data360x.py` ở gốc kho nạp vào `registry/trang-thai.csv` (không ghi đè dòng
  người duy trì; hiệu lực để trống) rồi sinh lại `vbpl.json`. Kho từ 62 → **105 văn bản**.
- **Lớp 2 chạy được bằng `claude` CLI**: `run_cases.sh` thêm `--allowedTools` (cờ bypass bị từ chối
  với tài khoản root) và lời dẫn "trường hợp thử cấu trúc — không bịa số liệu, không hỏi lại".
- 4 điểm chờ chốt ở mục D `rule-inventory.md` đã xử lý theo "mẫu thật là chuẩn"; quy tắc header
  viết đầy đủ xếp vào lịch sử.

## Quy trình từ nay khi phát hiện lỗi mới

Không thêm văn xuôi vào SKILL.md nữa — xem mục "Quy trình khi phát hiện lỗi mới" trong
`HUONG_DAN_CAP_NHAT.md`.
