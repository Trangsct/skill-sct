---
name: vbhc-vn
description: "SOẠN THẢO, RÀ SOÁT VĂN BẢN HÀNH CHÍNH (.docx) Sở Công Thương Lào Cai: công văn, tờ trình, báo cáo, kế hoạch, quyết định, biên bản, giấy phép (kể cả HHNH), GCN ATTP, công văn nội bộ phòng; ký hiệu SCT-CN, TTr-SCT, BC-SCT, KH-SCT, QĐ-SCT, GP-SCT, GCNATTP-SCTLC; thể thức NĐ 30/2020, trình ký. Cả văn bản cấp UBND tỉnh/VP do Sở dự thảo (giấy mời, chỉ đạo, thông báo kết luận, phiếu trình). Dùng khi: soạn/rà soát/sửa/tham mưu/thẩm định/góp ý/triển khai VBHC; chuyển thể văn bản giữa các cấp ban hành; sửa lỗi trình bày file Word (khoảng trống bất thường, mất đường kẻ header, sai đậm/nghiêng, khối ký gãy trang); nhận PDF văn bản đến (chạy scripts/extract_metadata.py đọc số/ngày/người ký từ đĩa, không tin context); soạn bài phát biểu, VBQPPL (thể thức riêng). Trigger thêm: tên file chứa CV/QĐ/TTr/BC/KH/NQ/NĐ/TT/UBND/SCT/HĐND; cụm 'công văn đến'. Nội dung quy tắc ở thân skill + reference, không ở đây."
---


# vbhc-vn — Soạn văn bản hành chính từ mẫu thật của Sở Công Thương Lào Cai

Nguyên tắc lõi: **giữ nguyên 100% định dạng gốc** (header, gạch chân, bảng chữ ký, font), chỉ thay nội dung — không sinh văn bản từ đầu bằng code khi đã có mẫu/file gốc. *Vì sao:* dựng lại bằng code thường không tái tạo đúng khung, đường gạch chân, layout chữ ký → dễ sai thể thức và mất thời gian; mẫu thật đã được kiểm chứng.

Skill có **2 chế độ làm việc** (xem mục "Hai chế độ làm việc" bên dưới để chọn đúng):
- **Chế độ A — Tạo mới từ template**: dùng 09 mẫu trắng trong `templates/` + `TemplateDoc`. Áp dụng khi soạn một văn bản mới (công văn, tờ trình, quyết định, biên bản…).
- **Chế độ B — Sửa file người dùng tải lên**: dùng workflow `unpack → sửa `word/document.xml` → pack`. Áp dụng khi rà soát/chỉnh sửa file .docx có sẵn (báo cáo, phụ lục, biểu, kịch bản điều hành, bài phát biểu, kết luận…). **Đây là loại việc thường gặp nhất** và phải giữ nguyên định dạng file gốc, KHÔNG dựng lại bằng template.

**Thư viện mẫu sẵn có trong skill**: `templates/` = mẫu TRẮNG (Chế độ A, điền bằng `TemplateDoc`, đánh số 01-09); `examples/` = văn bản THẬT đã ban hành (Chế độ B - mở mẫu, copy ra chỗ làm việc, thay nội dung, giữ định dạng), gồm `examples/sct/` và `examples/ubnd/`. Xem mục "Thư viện mẫu thật đã ban hành (`examples/`)".

## Khi nào dùng

Khi người dùng yêu cầu tạo/soạn **hoặc rà soát/sửa/chỉnh** các văn bản:
- Công văn (CV), Tờ trình (TTr), Báo cáo (BC), Kế hoạch (KH)
- Quyết định cá biệt (QĐ-SCT), Giấy phép (GP), Giấy chứng nhận ATTP
- Phụ lục, biểu tổng hợp (khổ ngang), kịch bản điều hành, bài phát biểu, kết luận hội nghị, phiếu nhận xét/thẩm định hồ sơ
- Công văn nội bộ giữa các phòng (vd Phòng QLCN tham gia ý kiến gửi Phòng Kế hoạch - Tổng hợp), do Trưởng phòng ký
- **Văn bản cấp UBND tỉnh / Văn phòng UBND tỉnh** mà Sở dự thảo: giấy mời họp, công văn chỉ đạo/đề nghị, thông báo kết luận, phiếu trình, báo cáo của VP UBND (xem mục riêng phía dưới)
- Giấy phép vận chuyển hàng hóa nguy hiểm (GP-SCT), giấy mời dự họp cấp Sở (SCT-CN), tờ trình ban hành VBQPPL - có mẫu thật trong `examples/sct/`

Hoặc nhắc tới các ký hiệu: `SCT-CN`, `TTr-SCT`, `BC-SCT`, `KH-SCT`, `QĐ-SCT`, `GP-SCT`, `GCNATTP-SCTLC`.

**Luôn áp dụng bảng "Phòng tránh 14 nhóm sai lầm tham mưu A–N" bên dưới** (đã hợp nhất từ `anti-error-sct-vn`) và mục "Đọc PDF văn bản đến" (hợp nhất từ `vbhc-pdf-reader-vn`). Đối chiếu nội dung chuyên môn với `kccn-sct-vn` / `hnh-sct-vn`.

## Định tuyến — soạn loại nào thì đọc file nào

| Loại văn bản | Mẫu thật (Chế độ B) | `--loai` cho build_vb.py | Đọc thêm |
|---|---|---|---|
| Công văn | `examples/sct/cong-van-*.docx` | `cong-van` | `reference/the-thuc-van-phong.md`; Nhóm I, L nếu gửi doanh nghiệp |
| Công văn nội bộ Phòng | `examples/sct/cong-van-noi-bo-phong-*.docx` | `cong-van-noi-bo` | `reference/the-thuc-van-phong.md` mục "loại có quy ước riêng" |
| Tờ trình | `examples/sct/to-trinh-vbqppl-tien-chat-thuoc-no.docx` | `to-trinh` | `reference/quy-tac-bat-bien.md` QT 6 (người ký) |
| Báo cáo | `examples/sct/bao-cao-*.docx` | `bao-cao` | `reference/thu-vien-mau-that.md` |
| Báo cáo định kỳ của Phòng | `examples/sct/bao-cao-thang-phong-qlcn.docx` | `bao-cao-phong` | `reference/bao-cao-dinh-ky-phong-qlcn.md` |
| Kế hoạch | `examples/sct/ke-hoach-thuc-hien-de-an-08.docx` | `ke-hoach` | QT 24 (căn lề ô bảng phụ lục) |
| Quyết định cá biệt | `templates/05-quyet-dinh.docx` | — (Chế độ A) | `reference/templates-chi-tiet.md` |
| Giấy phép | `examples/sct/giay-phep-van-chuyen-hhnh.docx` | `giay-phep` | Nhóm G (thứ tự Nơi nhận gửi doanh nghiệp) |
| GCN ATTP | `examples/sct/giay-chung-nhan-attp-winmart.docx` | — (Chế độ A) | `reference/templates-chi-tiet.md` |
| Biên bản | `examples/sct/bien-ban-*.docx` | `bien-ban` | `reference/the-thuc-van-phong.md` |
| Văn bản cấp UBND tỉnh / VP UBND | `examples/ubnd/*.docx` | — (Chế độ B) | **Nhóm K** trong `reference/phong-tranh-sai-lam.md` |
| Văn bản thể thức Đảng | — | — | `reference/van-ban-dang-ca-nhan.md` |
| VBQPPL (QĐ UBND, NQ HĐND) | — | — | `reference/the-thuc-van-phong.md` mục VBQPPL |
| Phụ lục, biểu khổ ngang | `examples/sct/phu-bieu-*.docx` | — | `reference/cong-thuc-thuc-chien.md` |
| Hợp đồng, phụ lục hợp đồng, văn bản dài | file người dùng gửi (Chế độ B) | — | Quy tắc 28 trong `reference/quy-tac-bat-bien.md`; `scripts/fit_pages.py` |
| File .docx do xã / doanh nghiệp gửi đến để sửa | file người dùng gửi (Chế độ B) | — | **Nhóm N** trong `reference/phong-tranh-sai-lam.md`; `scripts/normalize_body.py` |

## Quy tắc bất biến — bản rút gọn

Đủ 28 quy tắc kèm lý do và vụ thật: **`reference/quy-tac-bat-bien.md`** — đọc file đó khi soạn
văn bản mới hoặc khi QA báo lỗi chưa rõ quy tắc gốc. Dưới đây là phần phải nhớ mà không tra:

1. **Không sinh văn bản từ đầu bằng code khi đã có mẫu/file gốc.** Chế độ A mở `templates/`;
   Chế độ B sửa trực tiếp file người dùng tải lên (Nhóm F — rebuild là xóa mất chỉnh sửa tay).
2. **Không đụng bảng header, bảng chữ ký, đường Line**; không xóa/thêm paragraph trong ô bảng.
3. **Không chèn ngắt dòng cứng** `\n`/`<w:br/>` trong một paragraph — tách thành paragraph riêng.
4. **Không giao PDF** cho người dùng; sản phẩm cuối chỉ là .docx.
5. **Người ký theo lĩnh vực**: KCN, CCN, ATTP → PGĐ Nguyễn Đình Chiến; HHNH, hóa chất, VLNCN,
   khoáng sản, môi trường, PCCC, ATVSLĐ, năng lượng, thương mại → PGĐ Hoàng Văn Thuân; TTr UBND
   tỉnh và KH/QĐ/BC quan trọng → Giám đốc Hoàng Chí Hiền; công văn nội bộ Phòng → Trưởng phòng.
6. **Người soạn trong dòng Lưu = chuyên viên phụ trách lĩnh vực**, không mặc định CN (Trang);
   tra bảng trong `sct-laocai-org-vn`. Không rõ thì hỏi, không đoán.
7. **PDF văn bản đến: chạy `scripts/extract_metadata.py` TRƯỚC khi dẫn số/ngày.** Ô số/ngày
   trống trong context là tín hiệu ĐỌC ĐĨA, không phải bằng chứng "chưa cấp số" hay "bản dự thảo".
8. **Nơi nộp hồ sơ TTHC = Cổng dịch vụ công một cửa Bộ Công Thương**
   `https://motcua-tthc.moit.gov.vn/` — nơi nộp DUY NHẤT, không ghi Trung tâm Phục vụ hành chính
   công dưới bất kỳ hình thức nào.
9. **Mọi lệnh replace là bắt buộc khớp, thất bại phải nổ to** — không bọc try/except nuốt lỗi.
10. **Tên file**: `YYYY.MM.DD. Tên văn bản đầy đủ tiếng Việt có dấu.docx`.

## QA — chạy gì, khi nào

| Việc | Lệnh |
|---|---|
| QA một phát (thể thức + nội dung + ảnh render) | `python3 scripts/qa_all.py <file>.docx` |
| Bản Bạn yêu cầu hoàn thiện để xuất bản | `python3 scripts/qa_all.py <file>.docx --final` |
| Kiểm nội dung bắt buộc có / cấm có | `... --forbid "<cụm cũ>" --require "<cụm mới>"` |
| Chỉ bộ quy tắc R01–R15, không render | `python3 scripts/qa_rules.py <file>.docx` |
| Đối chiếu số hiệu văn bản với kho đã kiểm chứng | `python3 scripts/cite_check.py <file>.docx` |
| Dựng .docx từ nội dung dạng thẻ | `python3 scripts/build_vb.py noi-dung.txt ra.docx --loai <loại>` |
| Đọc số/ngày/người ký từ PDF văn bản đến | `python3 scripts/extract_metadata.py <file>.pdf` |
| File .docx cơ quan khác gửi đến — gỡ định dạng ẩn (Nhóm N) | `python3 scripts/normalize_body.py <file>.docx --check` rồi `... <file>.docx` |
| Hợp đồng, phụ lục hợp đồng, văn bản dài — căn trang (Quy tắc 28) | `python3 scripts/fit_pages.py sweep <file>.docx` rồi `apply <pt>` |

`qa_all.py` đã gộp bộ quy tắc máy kiểm R01–R15 thành mục 1b, nên chạy một lệnh là đủ. Ý nghĩa
từng mã quy tắc: `tests/rule-inventory.md`. Quy trình khi phát hiện lỗi mới (thêm hàm kiểm và
trường hợp thử, KHÔNG thêm văn xuôi): `HUONG_DAN_CAP_NHAT.md`.

## Phòng tránh 14 nhóm sai lầm tham mưu A–N (luôn áp dụng)

Áp dụng cho mọi việc soạn / rà soát / góp ý / tham mưu, không chỉ khi tạo .docx.
**Chi tiết từng nhóm, vụ thật và checklist: `reference/phong-tranh-sai-lam.md`** — đọc file đó
trước khi trình ký. Mỗi nhóm một dòng để nhớ:

| Nhóm | Điều phải nhớ | Máy kiểm |
|---|---|---|
| **A** Pháp lý | Không điền số/ngày/điều khoản từ trí nhớ; không ghép 2 dữ kiện trong reference thành kết luận mới về vụ việc | R01, `cite_check.py` |
| **B** Nhiệm vụ | Quy tắc 1-1-1: mỗi nhiệm vụ đề xuất Sở làm phải truy về 1 câu chỉ đạo / 1 điều khoản / 1 chức năng của Sở | — (loại N) |
| **C** Từ ngữ | Bản trình ký chỉ có 3 trạng thái: khẳng định có căn cứ, đề nghị nêu căn cứ, bảo lưu. Không từ suy đoán | R08 |
| **D** Hiệu lực | VBPL viện dẫn phải còn hiệu lực **và ĐÃ có hiệu lực tại ngày ký** | R05 |
| **E** PDF | Nguồn là PDF thì chạy `extract_metadata.py`, không tin context (layout 2 cột) | — (quy trình) |
| **F** Không rebuild | File người dùng tải lên thì sửa trực tiếp file đó; chưa diff toàn văn thì mặc định coi là ĐÃ có sửa tay | R14 |
| **G** Thể thức từ sửa tay | Ngày để trống ngày, điền sẵn tháng/năm; `Lưu: VT, CN (Tên).`; Kính gửi ↔ Nơi nhận "Như trên" nhất quán; **doanh nghiệp xếp gần cuối Nơi nhận, ngay trên dòng Lưu**; biên bản có ô Đạt/Không đạt thì giữ nguyên, không tự điền | R04, R06, R07 |
| **H** Toàn vẹn trình bày | Không gán `run.text` cho run neo shape Line; Số/Ngày 13pt tường minh, ngày nghiêng; không widow word; khối ký không gãy trang; **keepNext chỉ cho đề mục**; cấm `trHeight` bảng nội dung | LINES, SZ13, WIDOW, SIGSPLIT, SIGSPACE, [F] |
| **I** Gửi doanh nghiệp | Không nêu mốc hiệu lực giấy tờ mà DN chưa vi phạm; không viết "đề nghị liên hệ Phòng … để được hướng dẫn" trong công văn hoàn thiện hồ sơ TTHC | R10 (một phần) |
| **J** Giọng giải thích | Mỗi câu phải nêu QUY ĐỊNH, YÊU CẦU hoặc SỰ VIỆC. Câu đánh giá mức độ, so sánh dễ - khó, dẫn dắt tâm lý → bỏ | R10 |
| **K** Văn bản chỉ đạo UBND tỉnh | **Gần như không viện dẫn điều khoản**; giao cơ quan khác viết tổng quát trong thẩm quyền thật của họ; điều kiện đặt lên cơ quan khác chỉ hợp lệ khi Sở đã được giao vai trò + có sản phẩm cụ thể; không tính từ đánh giá; thuật ngữ theo luật | R09, R15 |
| **L** Cho ý kiến, gia hạn, hướng dẫn hồ sơ | Phải ghi rõ **nhất trí / không nhất trí** kèm lý do — cấm "căn cứ theo quy định của pháp luật để thực hiện"; gia hạn không quá 01 lần, không quá 10 ngày, có mốc ngày cụ thể; hướng dẫn bổ sung hồ sơ đủ trong MỘT lần | R10 (một phần) |
| **M** Trạng thái hồ sơ vụ việc (17/9/2026) | Trước khi soạn văn bản gắn một vụ việc/cụm cụ thể phải xác định vụ việc đang ở **BƯỚC nào**, văn bản gần nhất số mấy; **đã có Quyết định thì không soạn văn bản của bước trước đó**; mẫu mượn được, trạng thái không mượn được; CCN/KCN chạy `kccn-sct-vn/scripts/trang_thai_cum.py` trước | — (loại N); `--forbid "để có cơ sở tham mưu"` |
| **N** Định dạng ẩn trong file cơ quan khác gửi (17/9/2026) | File .docx của xã/doanh nghiệp gửi đến: `w:numPr` sinh "- -", `w:ind` lẫn lộn, `w:tab` đầu đoạn, đoạn trống thừa — trích xuất text KHÔNG thấy, chỉ lộ trên ảnh render. **Chạy `normalize_body.py --check` trước và `normalize_body.py` sau khi sửa**, rồi `fix_quoc_hieu.py`, rồi `qa_all.py` | `normalize_body.py` |

## Đọc PDF văn bản đến — trích metadata chính xác

> ### CẢNH BÁO CỨNG — làm trước mọi việc khác
> Nhận file PDF có dấu hiệu là văn bản nhà nước VN (tên file CV/QĐ/TTr/BC/KH/NQ/NĐ/TT/UBND/SCT…; dòng đầu "ỦY BAN NHÂN DÂN/BỘ/SỞ/HĐND/CHÍNH PHỦ"; hoặc bối cảnh "công văn đến") → **DỪNG mọi thao tác khác** và chạy ngay:
> ```bash
> python3 "/mnt/skills/plugins/vbhc-vn:vbhc-vn/scripts/extract_metadata.py" "<đường dẫn file>" # nếu cài dạng user skill thì thay bằng /mnt/skills/user/vbhc-vn/scripts/
> ```
> *Vì sao:* PDF VBHC có layout 2 cột; số/ngày/người ký là text-box độc lập, khi nạp vào context thường bị bỏ trống hoặc nối sai thứ tự → **context KHÔNG đáng tin**. Ô "Số: /…" hay "ngày … tháng …" trống là **tín hiệu phải đọc đĩa**, không phải kết luận "nháp chưa cấp số" (hai thứ hiển thị y hệt nhau). Bỏ qua đã gây ≥2 vụ dẫn chiếu sai (CV 3861/UBND-NC; CV 3954/UBND-VX). Chi phí ~2 giây.

Cờ kích hoạt, OCR fallback (`ocrmypdf`), 11 trường output JSON, chức vụ ký (KT./TM./TUQ./TL.), khi nào chạy lại — chi tiết: **`reference/doc-pdf-metadata.md`**.

## Thư viện mẫu thật đã ban hành (`examples/`)
26 mẫu thật (`examples/sct/` 20 + `examples/ubnd/` 6) để soạn bằng Chế độ B: bảng "mẫu thật ↔ loại văn bản", người ký/ký hiệu, cấu trúc từng mẫu UBND/VP, lưu ý số liệu — đọc khi chọn mẫu hoặc soạn văn bản cấp UBND/VP: **`reference/thu-vien-mau-that.md`**.
Cốt lõi: ưu tiên mẫu thật trong `examples/` hơn template trắng (Chế độ B); KHÔNG dùng `TemplateDoc` cho file `examples/` (đã điền sẵn, không theo chỉ số paragraph); KHÔNG bê nguyên nội dung vụ việc cũ sang văn bản mới — chỉ kế thừa khung, thể thức, văn phong.

## Công thức & checklist thực chiến
Công thức căn bảng/biểu khổ ngang "vuông vắn" (A4 ngang 9071 DXA, lặp dòng tiêu đề, nền trắng), đồng bộ chéo Báo cáo↔Phụ lục↔VP UBND, toàn vẹn số liệu/metadata, mã người soạn dòng "Lưu" — đọc khi dựng biểu hoặc đồng bộ nhiều file: **`reference/cong-thuc-thuc-chien.md`**.

## Tài liệu tham chiếu (`reference/`) — đọc khi cần

SKILL.md chỉ giữ phần lõi và bảng định tuyến; chi tiết nằm ở các file dưới.

| File | Đọc khi |
|---|---|
| `quy-tac-bat-bien.md` | Soạn văn bản mới, hoặc QA báo lỗi chưa rõ quy tắc gốc — đủ 27 quy tắc kèm lý do và vụ thật |
| `the-thuc-van-phong.md` | Băn khoăn quy cách thể thức, ký hiệu, tên file; loại có quy ước riêng; VBQPPL |
| `quy-trinh-hai-che-do.md` | Chọn Chế độ A hay B; cú pháp `TemplateDoc`; quy trình unpack-sửa-pack; quy tắc tốc độ |
| `phong-tranh-sai-lam.md` | Trước khi trình ký — chi tiết 14 nhóm A–N, checklist, vụ thật |
| `thu-vien-mau-that.md` | Chọn mẫu thật cho Chế độ B — bảng mẫu ↔ loại VB ↔ người ký |
| `templates-chi-tiet.md` | Chế độ A — cấu trúc paragraph/table từng template 01–09 |
| `bao-cao-dinh-ky-phong-qlcn.md` | Báo cáo tháng/quý/9 tháng của Phòng, phụ biểu giao ban, bài phát biểu Trưởng phòng |
| `van-ban-dang-ca-nhan.md` | Văn bản thể thức Đảng, bộ 4 văn bản cá nhân đảng viên sau giám sát |
| `cong-cu-ky-thuat.md` | **Trước** khi xử lý file nén, PDF scan, sửa docx đa run — công thức đã kiểm chứng, không mò lại |
| `doc-pdf-metadata.md` | Đọc PDF công văn đến — cờ kích hoạt, OCR, 11 trường |
| `cong-thuc-thuc-chien.md` | Căn bảng/biểu khổ ngang, đồng bộ chéo nhiều file |
| `the-thuc-code.md` | Phải sinh .docx bằng code khi KHÔNG có mẫu — hàm định dạng đoạn + XML đường Line |
| `nd-79-2025-tom-tat.md` | Rà soát VBQPPL hết hiệu lực (Nhóm D) |
| `nd30-phu-luc-1-the-thuc.md` | Văn bản gốc Phụ lục I NĐ 30/2020 — căn cứ pháp lý của một quy tắc trình bày |
| `nd30-phu-luc-2-viet-hoa.md` | Gặp trường hợp viết hoa không chắc chắn — KHÔNG đoán |
| `nd30-phu-luc-3-viet-tat-mau.md` | Cần ký hiệu chuẩn cho loại văn bản chưa có trong `templates/` |

Script: `qa_all.py` (QA một phát) · `qa_rules.py` (R01–R15) · `cite_check.py` (đối chiếu số hiệu)
· `build_vb.py` (dựng từ nội dung dạng thẻ) · `build_bao_cao_phong.py` · `fill_template.py`
· `extract_metadata.py` (đọc PDF) · `normalize_body.py` (định dạng ẩn, Nhóm N) · `fit_pages.py` (căn trang hợp đồng, Quy tắc 28) · `fix_quoc_hieu.py` · `qa_pdf_check.py` · `check_document.py`.

## Demo có sẵn

Trong `scripts/`:
- `demo_cong_van.py` — Tạo công văn báo cáo tiến độ thẩm định CCN An Thịnh
- `demo_to_trinh.py` — Tạo Tờ trình phê duyệt Quy hoạch CCN Y Can
- `demo_quyet_dinh.py` — Tạo QĐ thành lập Đoàn thẩm định ATTP cho Cty Hùng Sơn

Đọc các demo này khi cần ví dụ cụ thể về cách sửa từng loại văn bản.
