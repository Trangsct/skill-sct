# Quy tắc làm việc với repo skill-sct

## Quy trình giao nộp (Bạn chốt 15/8/2026 - áp dụng vĩnh viễn)

- **Sau khi hoàn thành việc nâng cấp/cập nhật skill hoặc plugin** (sửa SKILL.md, references, văn bản gốc, plugin.json...): commit, push lên nhánh làm việc, **LUÔN mở Pull Request gộp nhánh đó vào `main` VÀ MERGE NGAY, KHÔNG cần hỏi lại**. Ghi rõ trong PR: plugin nào, phiên bản mới, nội dung thay đổi chính.
- Lý do Bạn chốt: cần hiệu quả công việc, đã có nhiều bản sao lưu nên ưu tiên nhanh, không lo sai lệch dữ liệu.
- Quy tắc merge-ngay này áp dụng cho việc nâng cấp skill/plugin; việc khác ngoài phạm vi đó thì vẫn hỏi trước khi merge.

## Trần 512 MB archive của claude.ai — export-ignore (phát hiện 29/9/2026)

claude.ai đồng bộ marketplace bằng cách **tải archive (zip) của kho từ GitHub**, tự chạy mỗi khi có
push hoặc PR merge vào `main` (nút *Re-sync* trên marketplace để chạy tay). Giới hạn mặc định (docs
Cowork → Install plugins → Limits): **archive kho ≤ 512 MB, mỗi gói plugin ≤ 200 MB, ≤ 5.000 tệp/plugin**.
Vụ 11/9/2026: archive nén lên 512,8 MB (10/9 mới 503,6 MB) → claude.ai báo "Sync failed", **mọi plugin
trên claude.ai đứng ở bản 10/9 suốt 18 ngày** dù kho vẫn cập nhật đều và CI vẫn xanh.

Cách xử lý đã chốt: `.gitattributes` đánh `export-ignore` cho **mọi tệp ≥ 3 MB** — tệp vẫn nằm trong kho
(git clone, Claude Code, GitHub) nhưng **không đi vào gói claude.ai**; archive còn ~207 MB.

- `.gitattributes` là file **tự sinh** bởi `python3 scripts/export_ignore.py` — không sửa tay. Sau khi
  thêm/xóa tệp nặng: chạy script rồi commit `.gitattributes` cùng đợt. `check_descriptions.py` gọi
  `export_ignore.py --check` nên CI đỏ nếu quên, hoặc nếu archive dự tính vượt 400 MB (dư địa trước 512).
- Hệ quả: Claude trên claude.ai **không mở được PDF/DOCX ≥ 3 MB** của plugin. Văn bản gốc nặng phải có
  **bản trích chữ `.txt`/`.md` đặt cạnh** (pdftotext / `extract_metadata.py`) và reference dẫn bản trích đó;
  mục lục văn bản gốc ghi rõ tệp nào chỉ có trên GitHub.
- Muốn giữ nguyên PDF trong gói claude.ai thì phải chuyển bản gốc sang kho riêng — chưa làm, chờ Bạn chốt.

## Nguồn cập nhật plugin hằng tuần (Bạn chốt 12/9/2026)

Bot Data360X quét **cả văn bản đi lẫn văn bản đến** của Sở (11h30 thứ Tư hằng tuần, hoặc bấm tay ở Actions
kho `vlncn-laocai` → *Quet Data360X (may co quan)*), xếp theo lĩnh vực của từng plugin ở đây, tải bản gốc về
`theo-doi/` của kho **riêng tư** `vlncn-laocai` kèm bản tin `theo-doi/bao-cao/<ngày>.md`.

Cách tra kho và cách sai bot vào Data360X lấy đúng văn bản đang cần: plugin **`data360x-sct-vn`** (scripts `tim_trong_kho.py`, `goi_bot.py`; workflow `lay-van-ban.yml`). Tra kho trước, sai bot sau.

**Đầu mỗi phiên làm việc với bộ plugin: đọc bản tin mới nhất đó trước.** Cùng lúc nạp văn bản pháp luật công khai mà bot đã lọc:
`python3 scripts/nap_vbpl_data360x.py ../vlncn-laocai/theo-doi/de-xuat-vbpl.csv` (thêm dòng mới vào
`registry/trang-thai.csv`, không ghi đè dòng đã đối chiếu tay, hiệu lực để trống; sinh lại `vbpl.json`). Mỗi mục trong bản tin ghi rõ văn
bản thuộc plugin nào và đường dẫn PDF. Đọc PDF → có quy định/số liệu mới thì sửa plugin tương ứng theo quy
trình dưới đây; không có gì mới thì báo lại một dòng cho Bạn là đã rà.

Ba điều bắt buộc:

- **Không chép văn bản nội bộ sang kho này.** `skill-sct` công khai ra Internet; bản gốc văn bản đi/đến chỉ
  nằm ở kho riêng tư. Cập nhật plugin thì viết lại nội dung quy định, dẫn số hiệu và ngày, không đính kèm bản gốc.
- **Không bịa số, ngày, tên.** Đọc được gì trong PDF thì ghi nấy; PDF ký số phải chạy
  `vbhc-vn/skills/vbhc-vn/scripts/extract_metadata.py` trước khi ghi số/ngày (xem mục dưới).
- Mục *"Chưa xếp được vào plugin nào"* trong bản tin: chủ đề nào lặp lại nhiều lần là dấu hiệu cần **lập
  plugin mới** — đề xuất với Bạn.

## Dây chuyền quy tắc máy kiểm của vbhc-vn (Bạn chốt 16/9/2026)

Plugin `vbhc-vn` từ bản 2.23.0 **không nhận thêm quy tắc dưới dạng văn xuôi nữa**. Phát hiện lỗi
soạn thảo mới thì thêm một hàm kiểm và một trường hợp thử, theo 4 bước ghi trong
`vbhc-vn/skills/vbhc-vn/HUONG_DAN_CAP_NHAT.md` mục "Quy trình khi phát hiện lỗi mới":

1. Lưu file lỗi vào `vbhc-vn/skills/vbhc-vn/tests/fail/` kèm file `.expect` cùng tên (ghi mã quy
   tắc bắt buộc FAIL/WARN và dòng `nguon:` trỏ mẫu thật gốc).
2. Viết hàm `rule_Rnn(doc, ctx)` trong `vbhc-vn/skills/vbhc-vn/scripts/qa_rules.py`, đăng ký vào
   bảng `RULES`. Docstring bắt buộc ghi: mã, nội dung tiếng Việt, nguồn (số quy tắc trong SKILL.md
   hoặc nhóm A–L + ngày Bạn chốt), mức FAIL/WARN. Quy tắc chỉ là danh sách cụm từ thì thêm dòng
   vào `data/` chứ không sửa code.
3. Chạy `python3 tests/run_regression.py` tại thư mục plugin — phải xanh.
4. Tăng version, ghi CHANGELOG, chạy `sync_marketplace.py --bump` như thường lệ.

Ba điều bắt buộc khi làm việc với dây chuyền này:

- **Mẫu thật là chuẩn.** 26 file trong `examples/` phải PASS mọi quy tắc. Quy tắc nào làm mẫu thật
  FAIL thì quy tắc viết sai hoặc hiểu sai — **sửa quy tắc, tuyệt đối không sửa mẫu**. Đã có tiền lệ:
  R01, R04, R12 đều phải thu hẹp phạm vi vì bắt nhầm mẫu thật (xem `tests/rule-inventory.md` mục D).
- **Chỉ rút văn xuôi khỏi SKILL.md sau khi hàm kiểm đã bắt đúng lỗi trên ít nhất một file trong
  `tests/fail/` VÀ PASS trên toàn bộ `examples/`.** Chưa đủ hai điều kiện thì giữ nguyên văn xuôi.
- **Quy tắc máy không kiểm được** (nội dung pháp lý, suy diễn nhiệm vụ, giọng văn tổng thể) giữ
  nguyên văn xuôi và ghi là loại N trong `tests/rule-inventory.md` — không ép thành regex.

CI: job `qa-evals` trong `.github/workflows/validate-plugins.yml` chạy hồi quy lớp 1 mỗi lần có
thay đổi; job đỏ thì không merge.

## Quy tắc nghiệp vụ chung

- Mỗi lần nâng cấp plugin: tăng version trong `.claude-plugin/plugin.json`, thêm CHANGELOG theo mẫu `CHANGELOG-vYYYY.MM.DD.md` trong thư mục skill, và thêm mục mới lên ĐẦU `CHANGELOG.md` ở gốc repo.
- **TUYỆT ĐỐI KHÔNG sửa tay `.claude-plugin/marketplace.json`.** Chỉ sửa `plugin.json` của plugin, rồi chạy `python3 scripts/sync_marketplace.py --bump` để script tự đồng bộ description/version và **nâng `metadata.version`**. Lý do: script chỉ nâng `metadata.version` khi phát hiện lệch giữa hai file; nếu sửa tay marketplace.json cùng lúc thì không còn lệch, script bỏ qua, `metadata.version` đứng yên và **claude.ai không nhận ra catalog đã đổi** nên người dùng vẫn thấy bản cũ. Lỗi này đã xảy ra ngày 30/8/2026 (attp v1.4.0 và v1.5.0), phải nâng bù 2 bậc.
- Trước khi push: chạy `python3 scripts/sync_marketplace.py --check` và `python3 scripts/check_descriptions.py` (script này tự gọi tiếp `scripts/check_facts.py` — quét dữ kiện lỗi thời/quy ước cũ trên mọi plugin — và `scripts/export_ignore.py --check` — archive claude.ai dưới trần 512 MB; CI validate-plugins.yml vì thế cũng đỏ khi có vi phạm), cả hai phải trả về ok; và `find . -name __pycache__ -not -path "./.git/*"` phải rỗng (CI báo đỏ nếu còn — vụ 02/9/2026 sau khi chạy thử qa_all.py). **Mỗi khi Bạn chốt quy ước mới hoặc dữ kiện đổi, thêm một rule vào RULES của check_facts.py**; dòng nói về lịch sử thì kèm chữ "lịch sử"/"trước ngày…" để không bị báo. Lưu ý: PAT hiện dùng không có quyền `workflow`, không sửa được file trong .github/workflows/ — muốn sửa workflow phải dùng token có scope workflow.
- **Sổ đăng ký văn bản pháp luật** `registry/`: `van-ban-phap-luat.csv` + `README.md` do `python3 scripts/build_registry.py` tự sinh từ trích dẫn trong 20 plugin (không sửa tay); lớp trạng thái do người duy trì ghi ở `registry/trang-thai.csv` (ngày ban hành, hiệu lực, bị sửa đổi/thay thế bởi, dự thảo thay thế) — chỉ ghi khi đã đối chiếu bản gốc. Sau mỗi đợt nâng cấp plugin có thêm/bớt văn bản: chạy lại build_registry.py và commit cùng. Khi một nghị định bị thay thế: ghi vào trang-thai.csv → `--check` (chạy kèm check_descriptions.py trên CI, không chặn) liệt kê mọi dòng ở plugin còn dẫn văn bản cũ mà không nhắc văn bản mới. Cột `plugins` trong CSV cho biết phải rà plugin nào khi văn bản đổi.
- Văn bản pháp luật mới đưa vào plugin: lưu bản gốc vào thư mục `van-ban-goc/` tương ứng và cập nhật reference mục lục; tuyệt đối không bịa số/ngày văn bản.
- **Văn bản quy phạm pháp luật Bạn gửi: BẮT BUỘC lưu file Word (Bạn chốt 08/10/2026 — áp dụng cho MỌI plugin).** Luật, pháp lệnh, nghị quyết, nghị định, quyết định của Thủ tướng, thông tư, quyết định quy phạm của UBND tỉnh mà Bạn gửi trong phiên (kèm file hoặc dán nội dung) thì **ngay trong phiên đó** phải: (1) lưu **bản Word `.docx`** vào `van-ban-goc/` của plugin đúng lĩnh vực — Bạn gửi cả Word và PDF thì lưu cả hai; chỉ có PDF thì lưu PDF kèm bản trích chữ toàn văn `.txt`/`.md` cùng tên và báo Bạn là còn thiếu bản Word; (2) reference tóm tắt phải ghi **đường dẫn file gốc** và, với văn bản sửa đổi, bổ sung, **bảng đối chiếu "khoản … Điều … của văn bản sửa đổi ↔ điều, khoản của văn bản được sửa"** đọc từ file gốc; (3) không được kết thúc phiên khi mới chỉ có bản tóm tắt. Văn bản quy phạm pháp luật là văn bản công khai, **không thuộc diện "không chép văn bản nội bộ sang kho này"** (quy định đó chỉ áp dụng cho văn bản đi, đến của cơ quan). Trước khi lưu phải đọc số, ngày, trích yếu **từ chính file** và đối chiếu với văn bản Bạn gọi tên — số trùng khác năm là văn bản khác (303/2025/NĐ-CP ≠ 303/2026/NĐ-CP); lệch thì báo Bạn ngay. **PDF gốc đẩy lên GitHub là được, nhưng Claude phải NẮM TRỌN nội dung trong gói claude.ai (Bạn chốt 08/10/2026 lần 2):** mọi văn bản quy phạm chỉ có PDF trong `van-ban-goc/` bắt buộc có **bản trích chữ toàn văn `.txt` cùng tên** đặt cạnh (sinh bằng `python3 scripts/trich_chu_van_ban_goc.py` — pdftotext với PDF có lớp chữ, tesseract tiếng Việt với bản quét, đầu tệp ghi `[OCR]`); bản `.txt` nhỏ nên luôn vào gói claude.ai dù PDF bị export-ignore. Reference tóm tắt chỉ là lối vào; nội dung đầy đủ nằm ở bản Word hoặc bản `.txt`. Khi được hỏi về một văn bản đã có trong `van-ban-goc/` thì **mở bản Word/`.txt` ra đọc**, không được trả lời "chưa có thông tin" chỉ vì reference không ghi. `trich_chu_van_ban_goc.py --check` chạy kèm `check_descriptions.py` — còn PDF thiếu bản trích chữ thì CI đỏ. Rà tồn đọng: `python3 scripts/check_ban_word_vbqppl.py` (liệt kê văn bản quy phạm trong `van-ban-goc/` chưa có bản Word và reference ghi "Bạn cung cấp" mà không có file). Vụ 08/10/2026: Nghị định 303/2026/NĐ-CP Bạn gửi ngày 04/8/2026 chỉ được tóm tắt vào `kccn-sct-vn` reference 24, không lưu file; khi soạn công văn gấp phục vụ Đoàn đại biểu Quốc hội không tra được khoản nào của Điều 1 sửa Điều 8 Nghị định 32/2024/NĐ-CP, phải lấy từ nguồn thứ cấp.
- **Đọc PDF ký số** (số/ngày điền qua trường ký số): lớp text trong context bỏ rơi số/ngày - BẮT BUỘC chạy `vbhc-vn/skills/vbhc-vn/scripts/extract_metadata.py` (hoặc `pdftotext -layout`, hoặc render `pdftoppm` soi ảnh) TRƯỚC khi ghi số/ngày vào bất kỳ file nào của repo; không kết luận "để trống"/"bản dự thảo" chỉ từ context. Vụ 02/9/2026: QĐ 5116/QĐ-SCT ngày 20/8/2026 bị ghi nhầm "bản dự thảo chưa điền số" trong xp-sct-vn 1.3.1 vì bỏ bước này.
