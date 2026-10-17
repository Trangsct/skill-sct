---
name: vbhc-vn
description: "SOẠN THẢO, RÀ SOÁT VĂN BẢN HÀNH CHÍNH (.docx) Sở Công Thương Lào Cai: công văn, tờ trình, báo cáo, kế hoạch, quyết định, biên bản, giấy phép (kể cả HHNH), GCN ATTP, công văn nội bộ phòng; ký hiệu SCT-CN, TTr-SCT, BC-SCT, KH-SCT, QĐ-SCT, GP-SCT, GCNATTP-SCTLC; thể thức NĐ 30/2020, trình ký. Cả văn bản cấp UBND tỉnh/VP do Sở dự thảo (giấy mời, chỉ đạo, thông báo kết luận, phiếu trình). Dùng khi: soạn/rà soát/sửa/tham mưu/thẩm định/góp ý/triển khai VBHC; chuyển thể văn bản giữa các cấp ban hành; sửa lỗi trình bày file Word (khoảng trống bất thường, mất đường kẻ header, sai đậm/nghiêng, khối ký gãy trang); nhận PDF văn bản đến (chạy scripts/extract_metadata.py đọc số/ngày/người ký từ đĩa, không tin context); soạn bài phát biểu, VBQPPL (thể thức riêng). Trigger thêm: tên file chứa CV/QĐ/TTr/BC/KH/NQ/NĐ/TT/UBND/SCT/HĐND; cụm 'công văn đến'. Nội dung quy tắc ở thân skill + reference, không ở đây."
---


# vbhc-vn — Soạn văn bản hành chính từ mẫu thật của Sở Công Thương Lào Cai

> **Tra văn bản gốc (Bạn chốt 09/10/2026, áp dụng mọi plugin):** đọc `van-ban-goc/00-DANH-MUC-CHUNG.md` và chạy `python3 scripts/tim_van_ban.py "<số hiệu hoặc cụm từ>"` TRƯỚC khi kết luận văn bản nào chưa có trong kho. Văn bản đã có trong danh mục thì phải mở toàn văn `.txt` cùng tên đặt cạnh bản gốc để trích; cấm trả lời "không có tài liệu", "chưa có trong gói", "không mở được toàn văn", "tra mạng khi cần nguyên văn". Khi Bạn gửi văn bản quy phạm pháp luật trong phiên: (a) đọc số, ngày, cơ quan, người ký bằng script (GATE), không đọc bằng mắt; (b) đặt tên `YYYY.MM.DD-SỐ.KÝ.HIỆU-Tên-trích-yếu-ngắn`, giữ nguyên định dạng gốc; (c) lưu vào `van-ban-goc/` của plugin chủ theo lĩnh vực, không nhân bản sang plugin khác; (d) sinh `.txt` bằng `scripts/trich_chu_van_ban_goc.py`; (e) chạy `scripts/build_so_cai_van_ban_goc.py` ở gốc kho để cập nhật danh mục; (f) cập nhật reference tóm tắt + CHANGELOG; (g) push, mở PR. Phiên không có quyền ghi kho thì nói ngay ở câu đầu và hướng dẫn Bạn dùng Hộp thư nạp kho `_inbox/` trên GitHub (`_inbox/README.md`, 6 bước), không được chỉ tóm tắt rồi bỏ qua tệp.

Nguyên tắc lõi: **giữ nguyên 100% định dạng gốc** (header, gạch chân, bảng chữ ký, font), chỉ thay nội dung — không sinh văn bản từ đầu bằng code khi đã có mẫu/file gốc. *Vì sao:* dựng lại bằng code thường không tái tạo đúng khung, đường gạch chân, layout chữ ký → dễ sai thể thức và mất thời gian; mẫu thật đã được kiểm chứng.

Skill có **2 chế độ làm việc** (xem mục "Hai chế độ làm việc" bên dưới để chọn đúng):
- **Chế độ A — Tạo mới từ template**: dùng 09 mẫu trắng trong `templates/` + `TemplateDoc`. Áp dụng khi soạn một văn bản mới (công văn, tờ trình, quyết định, biên bản…).
- **Chế độ B — Sửa file người dùng tải lên**: dùng workflow `unpack → sửa `word/document.xml` → pack`. Áp dụng khi rà soát/chỉnh sửa file .docx có sẵn (báo cáo, phụ lục, biểu, kịch bản điều hành, bài phát biểu, kết luận…). **Đây là loại việc thường gặp nhất** và phải giữ nguyên định dạng file gốc, KHÔNG dựng lại bằng template.

**Thư viện mẫu sẵn có trong skill**: `templates/` = mẫu TRẮNG (Chế độ A, điền bằng `TemplateDoc`, đánh số 01-09); `examples/` = văn bản THẬT đã ban hành (Chế độ B - mở mẫu, copy ra chỗ làm việc, thay nội dung, giữ định dạng), gồm `examples/sct/` và `examples/ubnd/`. Xem mục "Thư viện mẫu thật đã ban hành (`examples/`)".

## GATE 0 — Kế hoạch soạn thảo (Bạn chốt 17/10/2026; chạy TRƯỚC mọi GATE khác, áp dụng mọi plugin soạn văn bản)

Trước khi viết dòng nào của thân văn bản, Claude tự lập kế hoạch và ghi vào `ke-hoach-soan.txt` trong thư mục làm việc
(việc nội bộ — KHÔNG gửi Bạn duyệt; tác tử rà soát ở GATE cuối dùng tệp này để đối chiếu):

a) Loại văn bản, cơ quan ban hành, người ký dự kiến (Quy tắc 5), ký hiệu dự kiến.
b) Nơi nhận dự kiến.
c) Toàn bộ căn cứ pháp lý sẽ viện dẫn, mỗi căn cứ ghi nguồn: đường dẫn tệp gốc trong kho, hoặc tên tệp Bạn vừa gửi,
   hoặc "chưa có nguồn - cần người dùng cung cấp". **Căn cứ không có nguồn thì không đưa vào văn bản.**
d) Toàn bộ số liệu sẽ dùng (diện tích, số dự án, kinh phí, tọa độ, khối lượng VLNCN…), mỗi số ghi nguồn như điểm c.
e) Những điểm còn thiếu hoặc chưa rõ.
f) Mỗi điểm thiếu: tự tìm trước trong kho — `scripts/tim_van_ban.py`, `van-ban-goc/00-DANH-MUC-CHUNG.md`, tệp
   `trang-thai/` của hồ sơ (`scripts/tim_ho_so.py` ở gốc kho), reference của plugin lĩnh vực, `sct-laocai-org-vn`. Thấy
   thì dùng, ghi nguồn. Không thấy thì **vẫn làm tiếp, bôi tím** chỗ thiếu trong file xuất ra. Chỉ dừng hỏi khi chỗ thiếu
   quyết định toàn bộ nội dung (không rõ loại văn bản, không rõ đối tượng, không rõ cấp phép hay từ chối) — tối đa MỘT
   lần hỏi mỗi phiên, gộp mọi câu, kèm phương án mặc định sẽ dùng nếu Bạn không trả lời.

Mẫu tệp (gõ thẳng, không markdown): `templates/ke-hoach-soan-mau.txt`. Số hiệu Bạn gửi trong phiên mà chưa có trong
kho thì ghi vào `can-cu-phien.txt` (mỗi dòng một số hiệu) cạnh file .docx để máy kiểm nhận.

- **Văn bản dưới một trang đủ dữ kiện trong yêu cầu hoặc tệp `trang-thai/` của hồ sơ** (giấy mời, công văn chuyển hồ sơ, phiếu trình ngắn): bỏ qua tệp
  kế hoạch, soạn ngay; vẫn chạy kiểm tra số hiệu (R23).
- **Máy kiểm R23** (`qa_rules.py`, chạy trong `qa_all.py` mục 1b): mọi số hiệu văn bản quy phạm (dạng số/năm/ký hiệu)
  trong file .docx phải khớp tệp gốc trong kho hoặc căn cứ của phiên; không khớp → WARN, in số hiệu để Bạn kiểm tra.
- **Khi giao file, báo Bạn tối đa 3 dòng**: nguồn căn cứ đã dùng; chỗ bôi tím cần Bạn bổ sung (nếu có); chỗ đã tự chọn
  phương án (nếu có).

## GATE 0b — Dàn ý (Bạn chốt 17/10/2026)

Áp dụng cho văn bản từ 3 trang trở lên hoặc thuộc loại: báo cáo, kế hoạch, đề án, phương án nổ mìn, báo cáo đánh giá
rủi ro, kế hoạch ứng cứu khẩn cấp, bài phát biểu, tờ trình kèm dự thảo.

a) Sau GATE 0, lập dàn ý theo **dàn ý mặc định** của loại văn bản (`reference/dan-y-mac-dinh.md` — mọi dàn ý lấy từ mẫu
   thật, văn bản gốc trong kho) hoặc theo văn bản mẫu gần nhất trong kho; ghi vào `ke-hoach-soan.txt` (mục g), KHÔNG
   gửi Bạn.
b) Dựng thân văn bản ngay theo dàn ý. Viết đủ, không ngắn hơn dàn ý — phương án nổ mìn phải đầy đủ và dài.
c) Chỉ gửi dàn ý xin ý kiến khi Bạn yêu cầu rõ "cho tôi xem dàn ý trước", hoặc loại văn bản chưa có dàn ý mặc định và
   chưa có mẫu nào trong kho: gửi gọn một màn hình điện thoại, gõ thẳng không markdown, kèm câu "Nếu không có ý kiến
   tôi sẽ viết theo dàn ý này".
d) Khi giao file báo một dòng: "Dàn ý theo mẫu [tên mẫu hoặc dàn ý mặc định]". Bạn muốn sửa bố cục thì sửa trên bản đã viết.

## GATE cuối — Rà soát độc lập (Bạn chốt 17/10/2026)

Sau khi file .docx đã dựng xong, TRƯỚC khi giao Bạn. Hai việc chạy SONG SONG, không nối tiếp:

1. **Claude** chạy MỘT lệnh: `python3 scripts/kiem_tra_truoc_khi_giao.py <file>.docx --tu-sua [--final]` — gộp `qa_all.py`
   (R01–R23), `cite_check.py`, `ra_soat_doc_lap.py`; tự sửa lỗi hình thức máy sửa được (phông, Nơi nhận cỡ 11, một dòng
   trước khối ký, một dòng sau Kính gửi, bảng nền trắng căn giữa dọc, dòng Lưu bỏ tên chuyên viên) rồi kiểm lại.
2. **Tác tử phụ chưa tham gia soạn** (công cụ Agent, chạy nền) nhận đúng lời giao sau, không kèm bối cảnh phiên:

   ```
   Rà soát độc lập file <đường dẫn .docx>. Chạy python3 <thư mục vbhc-vn>/scripts/ra_soat_doc_lap.py "<file>" và đọc
   toàn văn bằng script (python-docx hoặc pdftotext), KHÔNG dựa vào trí nhớ. Đối chiếu TỪNG dòng
   <thư mục vbhc-vn>/scripts/checklist_ra_soat.txt (và ke-hoach-soan.txt cạnh file nếu có). Không sửa file.
   Trả về danh sách: số thứ tự | vị trí (trang/đoạn) | nội dung lỗi | cách sửa đề xuất | loại HÌNH THỨC hoặc NỘI DUNG.
   Không lỗi thì trả đúng một dòng "Không phát hiện lỗi".
   ```

- Lỗi HÌNH THỨC tác tử tìm ra → Claude tự sửa bằng script (`kiem_tra_truoc_khi_giao.py --tu-sua`, `chuan_hoa_xuat_ban.py`,
  `normalize_body.py`…) rồi chạy lại rà soát, không hỏi Bạn. Lỗi NỘI DUNG, số liệu, viện dẫn → nêu gọn cho Bạn kèm hướng xử lý
  Claude đã chọn.
- Chu trình kiểm tra - sửa - kiểm lại **tối đa 2 vòng**; còn lỗi thì bôi tím chỗ đó và báo, không kéo dài.
- Phiên không có công cụ tác tử phụ: Claude tự đối chiếu checklist nhưng ghi rõ **"rà soát không độc lập"** trong báo cáo.
- Báo Bạn gọn: "Rà soát độc lập: không phát hiện lỗi" hoặc "Đã tự sửa [n] lỗi hình thức" + danh sách lỗi nội dung (nếu có),
  gộp vào tối đa 3 dòng báo khi giao file (GATE 0), dòng "Dàn ý theo mẫu …" (GATE 0b) và vế "đã ghi nhật ký".

## Khi nào dùng

Khi người dùng yêu cầu tạo/soạn **hoặc rà soát/sửa/chỉnh** các văn bản:
- Công văn (CV), Tờ trình (TTr), Báo cáo (BC), Kế hoạch (KH)
- Quyết định cá biệt (QĐ-SCT), Giấy phép (GP), Giấy chứng nhận ATTP
- Phụ lục, biểu tổng hợp (khổ ngang), kịch bản điều hành, bài phát biểu, kết luận hội nghị, phiếu nhận xét/thẩm định hồ sơ
- Công văn nội bộ giữa các phòng (vd Phòng QLCN tham gia ý kiến gửi Phòng Kế hoạch - Tổng hợp), do Trưởng phòng ký
- **Văn bản cấp UBND tỉnh / Văn phòng UBND tỉnh** mà Sở dự thảo: giấy mời họp, công văn chỉ đạo/đề nghị, thông báo kết luận, phiếu trình, báo cáo của VP UBND (xem mục riêng phía dưới)
- Giấy phép vận chuyển hàng hóa nguy hiểm (GP-SCT), giấy mời dự họp cấp Sở (SCT-CN), tờ trình ban hành VBQPPL - có mẫu thật trong `examples/sct/`

Hoặc nhắc tới các ký hiệu: `SCT-CN`, `TTr-SCT`, `BC-SCT`, `KH-SCT`, `QĐ-SCT`, `GP-SCT`, `GCNATTP-SCTLC`.

**Luôn áp dụng bảng "Phòng tránh 15 nhóm sai lầm tham mưu A–O" bên dưới** (đã hợp nhất từ `anti-error-sct-vn`) và mục "Đọc PDF văn bản đến" (hợp nhất từ `vbhc-pdf-reader-vn`). Đối chiếu nội dung chuyên môn với `kccn-sct-vn` / `hnh-sct-vn`.

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
5. **Người ký theo lĩnh vực** (QĐ 6286/QĐ-SCT ngày 05/10/2026): Phòng QLCN — KCN, CCN, ATTP, hóa chất,
   VLNCN, PCTT (dự kiến cả HHNH, PCCC) → PGĐ Nguyễn Đình Chiến; khai thác, chế biến khoáng sản, thiết kế mỏ,
   CN môi trường, ATVSLĐ → PGĐ Hoàng Văn Thuân; cấp phép, đấu giá khoáng sản → PGĐ Phạm Năng Chung;
   năng lượng → PGĐ Nguyễn Trường Giang; thương mại → PGĐ Trịnh Văn Thành / Nguyễn Huy Tưởng; TTr UBND
   tỉnh và KH/QĐ/BC quan trọng → Giám đốc Hoàng Chí Hiền; công văn nội bộ Phòng → Trưởng phòng.
6. **Dòng Lưu KHÔNG ghi tên chuyên viên** (Bạn chốt 01/10/2026): `Lưu: VT, CN.`; công văn nội bộ
   Phòng `Lưu: CN.`. `build_vb.py` và `TemplateDoc.save()` tự bỏ tên còn sót trong mẫu thật cũ; R07 WARN nếu còn tên.
7. **PDF văn bản đến: chạy `scripts/extract_metadata.py` TRƯỚC khi dẫn số/ngày.** Ô số/ngày
   trống trong context là tín hiệu ĐỌC ĐĨA, không phải bằng chứng "chưa cấp số" hay "bản dự thảo".
8. **Nơi nộp hồ sơ TTHC = Cổng dịch vụ công một cửa Bộ Công Thương**
   `https://motcua-tthc.moit.gov.vn/` — nơi nộp DUY NHẤT, không ghi Trung tâm Phục vụ hành chính
   công dưới bất kỳ hình thức nào.
9. **Mọi lệnh replace là bắt buộc khớp, thất bại phải nổ to** — không bọc try/except nuốt lỗi.
10. **Tên file**: `YYYY.MM.DD. Tên văn bản đầy đủ tiếng Việt có dấu.docx`.
11. **Trước khi xuất file chạy `python3 scripts/chuan_hoa_xuat_ban.py <file>.docx` (thêm `--tthc` với văn bản thủ tục hành chính)** rồi `qa_all.py --final` (Bạn chốt 13/10/2026): (a) quét TOÀN BỘ phông về Times New Roman, kể cả kiểu Normal, số trang, theme — mẫu thật cũ còn `.VnTime` ẩn, hệ thống quản lý văn bản mới chuyển PDF để ký số có thể lỗi; (b) các dòng Nơi nhận cỡ 11 ("Nơi nhận:" cỡ 12); (c) khối Nơi nhận - ký cách thân đúng 1 dòng trống cỡ 14; (d) văn bản thủ tục hành chính không gửi "Ban Giám đốc Sở". Máy kiểm R19–R22. `TemplateDoc.save()` và `build_vb.py` tự chạy bước này. Trình trên hệ thống: mục Dự thảo chỉ để tệp công văn (.docx/.pdf), không để tệp nén .rar/.zip bộ hồ sơ.

## QA — chạy gì, khi nào

| Việc | Lệnh |
|---|---|
| **Một lệnh trước khi giao** (qa_all + cite_check + số đo rà soát; `--tu-sua` sửa lỗi hình thức) | `python3 scripts/kiem_tra_truoc_khi_giao.py <file>.docx --tu-sua` |
| Số đo cho tác tử rà soát độc lập (đối chiếu `scripts/checklist_ra_soat.txt`) | `python3 scripts/ra_soat_doc_lap.py <file>.docx` |
| QA một phát (thể thức + nội dung + ảnh render) | `python3 scripts/qa_all.py <file>.docx` |
| Bản Bạn yêu cầu hoàn thiện để xuất bản | `python3 scripts/qa_all.py <file>.docx --final` |
| Kiểm nội dung bắt buộc có / cấm có | `... --forbid "<cụm cũ>" --require "<cụm mới>"` |
| Chỉ bộ quy tắc R01–R23, không render | `python3 scripts/qa_rules.py <file>.docx` |
| Chuẩn hóa trước khi xuất: phông, Nơi nhận cỡ 11, 1 dòng trước khối ký (Quy tắc 11) | `python3 scripts/chuan_hoa_xuat_ban.py <file>.docx [--tthc]` |
| Đối chiếu số hiệu văn bản với kho đã kiểm chứng | `python3 scripts/cite_check.py <file>.docx` |
| Dựng .docx từ nội dung dạng thẻ | `python3 scripts/build_vb.py noi-dung.txt ra.docx --loai <loại>` |
| Đọc số/ngày/người ký từ PDF văn bản đến | `python3 scripts/extract_metadata.py <file>.pdf` |
| File .docx cơ quan khác gửi đến — gỡ định dạng ẩn (Nhóm N) | `python3 scripts/normalize_body.py <file>.docx --check` rồi `... <file>.docx` |
| Hợp đồng, phụ lục hợp đồng, văn bản dài — căn trang (Quy tắc 28) | `python3 scripts/fit_pages.py sweep <file>.docx` rồi `apply <pt>` |

**Tự ghi lỗi (Bạn chốt 17/10/2026):** Bạn chỉ ra lỗi trong văn bản đã soạn → trong cùng phiên, không chờ nhắc: sửa văn
bản; ghi một mục vào `reference/so-loi-tu-ghi.md` (lỗi thể thức chung) hoặc sổ lỗi của plugin lĩnh vực; kiểm được bằng
máy thì thêm quy tắc R theo `HUONG_DAN_CAP_NHAT.md`; tăng bản plugin; báo một dòng "Đã ghi lỗi này vào [plugin] bản [số]".
Yêu cầu "chỉ lần này" không thành quy tắc — ghi vào tệp trạng thái hồ sơ.

`qa_all.py` đã gộp bộ quy tắc máy kiểm R01–R23 thành mục 1b, nên chạy một lệnh là đủ. Ý nghĩa
từng mã quy tắc: `tests/rule-inventory.md`. Quy trình khi phát hiện lỗi mới (thêm hàm kiểm và
trường hợp thử, KHÔNG thêm văn xuôi): `HUONG_DAN_CAP_NHAT.md`.

## Phòng tránh 15 nhóm sai lầm tham mưu A–O (luôn áp dụng)

Áp dụng cho mọi việc soạn / rà soát / góp ý / tham mưu, không chỉ khi tạo .docx.
**Chi tiết từng nhóm, vụ thật và checklist: `reference/phong-tranh-sai-lam.md`** — đọc file đó
trước khi trình ký. Mỗi nhóm một dòng để nhớ:

| Nhóm | Điều phải nhớ | Máy kiểm |
|---|---|---|
| **A** Pháp lý | Không điền số/ngày/điều khoản từ trí nhớ; không ghép 2 dữ kiện trong reference thành kết luận mới về vụ việc; căn cứ phải có nguồn (GATE 0) | R01, R23, `cite_check.py` |
| **B** Nhiệm vụ | Quy tắc 1-1-1: mỗi nhiệm vụ đề xuất Sở làm phải truy về 1 câu chỉ đạo / 1 điều khoản / 1 chức năng của Sở | — (loại N) |
| **C** Từ ngữ | Bản trình ký chỉ có 3 trạng thái: khẳng định có căn cứ, đề nghị nêu căn cứ, bảo lưu. Không từ suy đoán | R08 |
| **D** Hiệu lực | VBPL viện dẫn phải còn hiệu lực **và ĐÃ có hiệu lực tại ngày ký** | R05 |
| **E** PDF | Nguồn là PDF thì chạy `extract_metadata.py`, không tin context (layout 2 cột) | — (quy trình) |
| **F** Không rebuild | File người dùng tải lên thì sửa trực tiếp file đó; chưa diff toàn văn thì mặc định coi là ĐÃ có sửa tay | R14 |
| **G** Thể thức từ sửa tay | Ngày để trống ngày, điền sẵn tháng/năm; `Lưu: VT, CN.`; Kính gửi ↔ Nơi nhận "Như trên" nhất quán; **doanh nghiệp xếp gần cuối Nơi nhận, ngay trên dòng Lưu**; **văn bản thủ tục hành chính không gửi Ban Giám đốc Sở**; dòng Nơi nhận cỡ 11; khối ký cách thân 1 dòng; **sau Kính gửi cách 1 dòng, ô ký cao tương ứng khối Nơi nhận (17/10/2026)**; biên bản có ô Đạt/Không đạt thì giữ nguyên, không tự điền | R04, R06, R07, R20–R22 |
| **H** Toàn vẹn trình bày | Không gán `run.text` cho run neo shape Line; Số/Ngày 13pt tường minh, ngày nghiêng; không widow word; khối ký không gãy trang; **keepNext chỉ cho đề mục**; cấm `trHeight` bảng nội dung | LINES, SZ13, WIDOW, SIGSPLIT, SIGSPACE, [F] |
| **I** Gửi doanh nghiệp | Không nêu mốc hiệu lực giấy tờ mà DN chưa vi phạm; không viết "đề nghị liên hệ Phòng … để được hướng dẫn" trong công văn hoàn thiện hồ sơ TTHC | R10 (một phần) |
| **J** Giọng giải thích | Mỗi câu phải nêu QUY ĐỊNH, YÊU CẦU hoặc SỰ VIỆC. Câu đánh giá mức độ, so sánh dễ - khó, dẫn dắt tâm lý → bỏ | R10 |
| **K** Văn bản chỉ đạo UBND tỉnh | **Gần như không viện dẫn điều khoản**; giao cơ quan khác viết tổng quát trong thẩm quyền thật của họ; điều kiện đặt lên cơ quan khác chỉ hợp lệ khi Sở đã được giao vai trò + có sản phẩm cụ thể; không tính từ đánh giá; thuật ngữ theo luật | R09, R15 |
| **L** Cho ý kiến, gia hạn, hướng dẫn hồ sơ | Phải ghi rõ **nhất trí / không nhất trí** kèm lý do — cấm "căn cứ theo quy định của pháp luật để thực hiện"; gia hạn không quá 01 lần, không quá 10 ngày, có mốc ngày cụ thể; hướng dẫn bổ sung hồ sơ đủ trong MỘT lần | R10 (một phần) |
| **M** Trạng thái hồ sơ vụ việc (17/9/2026) | Trước khi soạn văn bản gắn một vụ việc/cụm cụ thể phải xác định vụ việc đang ở **BƯỚC nào**, văn bản gần nhất số mấy; **đã có Quyết định thì không soạn văn bản của bước trước đó**; mẫu mượn được, trạng thái không mượn được; CCN/KCN chạy `kccn-sct-vn/scripts/trang_thai_cum.py` trước | — (loại N); `--forbid "để có cơ sở tham mưu"` |
| **N** Định dạng ẩn trong file cơ quan khác gửi (17/9/2026) | File .docx của xã/doanh nghiệp gửi đến: `w:numPr` sinh "- -", `w:ind` lẫn lộn, `w:tab` đầu đoạn, đoạn trống thừa — trích xuất text KHÔNG thấy, chỉ lộ trên ảnh render. **Chạy `normalize_body.py --check` trước và `normalize_body.py` sau khi sửa**, rồi `fix_quoc_hieu.py`, rồi `qa_all.py` | `normalize_body.py` |
| **O** Tên doanh nghiệp (20/9/2026) | Luôn viết **"Công ty TNHH" / "Công ty TNHH MTV"**, không viết "Công ty trách nhiệm hữu hạn" — kể cả khi giấy đăng ký doanh nghiệp, giấy đề nghị của DN hay văn bản cơ quan khác viết đủ chữ; nhất quán trong cả bộ hồ sơ | — (loại N) |

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
| `dan-y-mac-dinh.md` | GATE 0b — dàn ý mặc định 14 loại văn bản dài (phương án nổ mìn, đánh giá rủi ro, ứng cứu khẩn cấp, bài phát biểu, báo cáo, kế hoạch, tờ trình, đề án), kèm nguồn |
| `so-loi-tu-ghi.md` | **Đọc trước khi soạn** — lỗi Bạn chỉ ra trong phiên, ghi ngay theo mục "Tự ghi lỗi" (từ 17/10/2026; định dạng L001…, kiểm bằng `scripts/check_anti_error_format.py` ở gốc kho) |
| `quy-tac-bat-bien.md` | Soạn văn bản mới, hoặc QA báo lỗi chưa rõ quy tắc gốc — đủ 27 quy tắc kèm lý do và vụ thật |
| `the-thuc-van-phong.md` | Băn khoăn quy cách thể thức, ký hiệu, tên file; loại có quy ước riêng; VBQPPL |
| `quy-trinh-hai-che-do.md` | Chọn Chế độ A hay B; cú pháp `TemplateDoc`; quy trình unpack-sửa-pack; quy tắc tốc độ |
| `phong-tranh-sai-lam.md` | Trước khi trình ký — chi tiết 15 nhóm A–O, checklist, vụ thật |
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

Script: `kiem_tra_truoc_khi_giao.py` (một lệnh trước khi giao) · `ra_soat_doc_lap.py` (số đo GATE cuối) · `qa_all.py` (QA một phát) · `qa_rules.py` (R01–R23) · `cite_check.py` (đối chiếu số hiệu)
· `build_vb.py` (dựng từ nội dung dạng thẻ) · `build_bao_cao_phong.py` · `fill_template.py`
· `extract_metadata.py` (đọc PDF) · `normalize_body.py` (định dạng ẩn, Nhóm N) · `fit_pages.py` (căn trang hợp đồng, Quy tắc 28) · `fix_quoc_hieu.py` · `qa_pdf_check.py` · `check_document.py`.

## Demo có sẵn

Trong `scripts/`:
- `demo_cong_van.py` — Tạo công văn báo cáo tiến độ thẩm định CCN An Thịnh
- `demo_to_trinh.py` — Tạo Tờ trình phê duyệt Quy hoạch CCN Y Can
- `demo_quyet_dinh.py` — Tạo QĐ thành lập Đoàn thẩm định ATTP cho Cty Hùng Sơn

Đọc các demo này khi cần ví dụ cụ thể về cách sửa từng loại văn bản.
