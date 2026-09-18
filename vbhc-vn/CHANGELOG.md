## [2.25.1] - 17/9/2026 — normalize_body.py: ba vùng bảo vệ (đoạn trống kề bảng, đoạn chứa shape/ngắt trang, khối Kính gửi)

- **Nguồn:** chạy lại script Nhóm N trên hai văn bản đã giao (công văn hướng dẫn 08 CCN có phụ lục mẫu Thông báo; Thông báo CCN Đông An) thì script đòi xóa nhầm: 2 đoạn trống kẹp khối Nơi nhận - chữ ký và bảng phụ lục; đoạn rỗng chứa **đường kẻ dưới trích yếu** (v:line) của mẫu Thông báo; và đòi ép lùi đầu dòng khối **Kính gửi** (left=1134, firstLine=0) về mức chung.
- **scripts/normalize_body.py**: (1) giữ mọi đoạn trống có anh chị em liền kề là `w:tbl`; (2) "đoạn rỗng" định nghĩa lại = không chữ VÀ không chứa `w:pict`, `w:drawing`, `w:br`, `w:object`, `mc:AlternateContent`; (3) hàm `khoi_kinh_gui()` bỏ qua đoạn "Kính gửi", các dòng tiếp theo còn lề trái riêng và dòng trống ngay dưới khối. Kiểm lại: hai văn bản đã chuẩn → 0/0/0/0; file gốc của UBND xã vẫn bắt 3 numPr, 36 ind lệch, 24 tab, 6 đoạn trống thừa.
- **reference/phong-tranh-sai-lam.md — Nhóm N**: thêm đoạn "Ba vùng script KHÔNG được đụng vào".
- `plugin.json` → 2.25.1.

## [2.25.0] - 18/9/2026 — R16 khối Kính gửi + build_vb.py dựng đúng khoảng cách khối

- **Nguồn:** vụ thật 18/9/2026 — bản công văn góp ý dự thảo QCVN 03:2026/BCA xuất ra cho Bạn bị lỗi trình bày: chỉ gửi một cơ quan (Công an tỉnh) nhưng "Kính gửi:" và tên cơ quan nằm hai dòng lệch nhau (giữ lại bảng 2 ô của mẫu gửi nhiều cơ quan), lại không cách một dòng với khối trích yếu phía trên và khối thân phía dưới; khối ký cũng không cách thân đúng một dòng. Bạn chỉ ra trực tiếp trên bản Word.
- **qa_rules.py — R16 (mới, FAIL)**: khối Kính gửi — gửi MỘT cơ quan thì "Kính gửi: <tên>." trên cùng một dòng; gửi nhiều cơ quan mới tách "Kính gửi:" lên trên, danh sách "- A;" … "- Z." xuống dưới; không để khối trống không có nơi nhận. Nhận được cả ba cách trình bày của mẫu thật (paragraph căn giữa, bảng 2 ô, danh sách trong cùng ô). Điều kiện bắt lỗi dựa vào dấu gạch đầu dòng nên 26/26 mẫu thật sạch.
- **build_vb.py**: dòng `[K]` không đi vào thân nữa mà dựng khối Kính gửi riêng theo SỐ nơi nhận — một nơi nhận thì xóa bảng của mẫu, thay bằng một dòng căn giữa, giữ đúng một dòng trống trên/dưới; nhiều nơi nhận thì điền danh sách vào ô phải của bảng. Thêm chuẩn hóa khối ký cách thân đúng một dòng trống. Thân văn bản không ghi lên dòng trống ngăn cách nữa.
- **normalize_body.py**: giữ 1 đoạn trống dưới trích yếu + **1** đoạn trống trước khối ký (trước đây 2).
- **tests/fail/r16-kinh-gui-tach-dong-mot-noi-nhan.docx** (file lỗi THẬT, không phải nhân tạo) + `.expect`; `run_regression.py` xanh: 26 mẫu thật 0 FAIL, 17 file lỗi bắt đúng mã.


## [2.23.1] - 17/9/2026 — Nhóm N: định dạng ẩn trong file .docx do cơ quan khác gửi đến + scripts/normalize_body.py

- **Nguồn:** vụ thật 17/9/2026 — rà soát, sửa Thông báo tiếp nhận hồ sơ đề nghị làm chủ đầu tư CCN Đông An do UBND xã Đông Cuông gửi. Sửa xong nội dung, bản render vẫn lỗi trình bày vì định dạng ẩn của file gốc; người dùng phải chỉ lại hai lượt ("- -" hai dấu gạch, thụt lề lệch, khoảng trắng trên mục 5).
- **reference/phong-tranh-sai-lam.md — Nhóm N (mới)**: N1 `w:numPr` danh sách tự động làm Word sinh thêm dấu gạch, hiển thị "- -" (trích xuất text KHÔNG thấy); N2 `w:ind` lẫn lộn giữa các nhóm đoạn (left=720 / left=0 / không có) gây thụt lề bậc thang; N3 `w:tab` đầu đoạn chồng lên firstLine; N4 đoạn trống thừa giữa thân đẩy đề mục xuống, tạo mảng trắng. Kèm quy trình bắt buộc 4 bước khi nhận file cơ quan khác gửi và 3 câu tự nhủ bắt lỗi sớm. Tiêu đề file → "14 nhóm sai lầm A–N".
- **scripts/normalize_body.py (mới)**: gỡ `w:numPr`; xóa `w:ind` rồi đặt lại left=0, right=0, firstLine đồng nhất; gỡ `w:tab` đầu run; xóa đoạn trống thừa (giữ 1 đoạn dưới trích yếu + 2 đoạn trước khối ký). Có `--check` (chỉ đếm) và `--indent` (567 hoặc 720). Không dùng `run.text=` nên không làm mất shape `v:line` ở header (bài học vụ Thành Hương 29/7/2026). Chạy thử trên chính file của UBND xã: bắt 3 numPr, 36 ind lệch, 24 tab, 8 đoạn trống thừa; sau chuẩn hóa về 0.
- **SKILL.md**: thêm `scripts/normalize_body.py` vào danh mục tham chiếu; tóm tắt Nhóm N vào đoạn "Luôn áp dụng…"; đổi A–M → A–N.
- `plugin.json` → 2.23.1.

## [2.22.0] - 16/9/2026 — Quy tắc 26, 27: văn bản thể thức Đảng, bộ văn bản cá nhân đảng viên sau giám sát; Kính gửi cân giữa; bản xuất bản không chỗ trống

- **reference/van-ban-dang-ca-nhan.md (MỚI)**: thể thức Đảng (tiêu đề ĐẢNG CỘNG SẢN VIỆT NAM + gạch dưới cân, không Quốc hiệu, không số, khối ký NGƯỜI BÁO CÁO); khối Kính gửi thẳng cột bằng tab + hanging indent và cân giữa trang; trích yếu viết hoa chữ đầu, chia dòng cân; mọi đoạn thân lùi 1,27 cm đồng đều; cấm chỗ trống "……" trong bản xuất bản; kết cấu đã duyệt của 4 văn bản (ý kiến phát biểu, báo cáo giải trình tiếp thu, kế hoạch khắc phục bảng 5 cột, báo cáo kết quả khắc phục). Nguồn: Bạn duyệt 4 lượt bộ văn bản sau giám sát của BTV Đảng ủy UBND tỉnh ngày 16/9/2026.
- **scripts/build_vb_dang.js (MỚI)**: dựng 3 văn bản bằng docx-js với hàm `header`, `kg`, `sign`, `P/C/H1`; nội dung ví dụ đã thay tên thật bằng biến NGUOI/CHI_BO/CHUC_VU/PHONG (repo công khai, không chép văn bản nội bộ).
- SKILL.md: Quy tắc 26 (thể thức Đảng, bộ 4 văn bản), Quy tắc 27 (Kính gửi nhiều nơi cân giữa; lùi đầu dòng đồng đều; bản xuất bản không chỗ trống, không chữ tím); bảng tham chiếu thêm dòng reference mới. `plugin.json` → 2.22.0, description đồng bộ.

# CHANGELOG — plugin vbhc-vn

## [2.14.0] - 06/9/2026 — Nhóm K viết lại theo BẢN CUỐI Bạn chốt (K1–K10)
- Diff bản cuối của Bạn với bản Claude giao cho thấy 2 quy ước trái với 2.13.x: **K1** điều kiện đặt lên cơ quan khác vẫn được dùng — nhưng chỉ khi Sở đã được giao vai trò ở mục trước và có sản phẩm cụ thể (câu chốt "chỉ thực hiện… khi được Sở Công Thương (cơ quan quản lý về phương án nổ mìn) xác nhận khu vực nổ mìn đảm bảo khoảng cách an toàn…", lặp nguyên văn 3 chỗ); **K6** văn bản chỉ đạo UBND tỉnh gần như không viện dẫn — bản sửa lần 1 dẫn đúng và đủ vẫn bị bác ("đúng không đồng nghĩa với cần ghi").
- Thêm K9 (công văn Sở trình kèm không nêu thiếu sót của cấp trên; không sửa thể thức riêng của Sở như "(Khôi)." subscript), K10 (thể thức nhỏ: "(Dự thảo)", "(B/c)"; SZ13 do Word ghi lại không sửa file cuối). K2, K3, K4, K7, K8 chỉnh cho khớp bản cuối; checklist + tự bắt lỗi thêm K1/K6; lệnh QA `--forbid` mới + đếm viện dẫn ≤ 4–5.
- Khung: `sd-vlncn-sct-vn/vi-du-thuc-te/*-ban-cuoi-6.9.2026.docx` (mẫu 23, plugin 2026.9.6.5).

## [2.13.1] - 06/9/2026 — Nhóm K8: mức chi tiết theo chủ thể
- reference/phong-tranh-sai-lam.md: K8 — phần Sở mình dẫn điều khoản, phần Công an/Bộ CHQS/sở khác viết tổng quát "theo thẩm quyền" (Bạn chốt lần 2 sau khi bản 2.13.0 dẫn quá chi tiết cho ngành dọc khác); "kiểm tra hồ sơ" không tách khỏi "thẩm định"; giao vai trò bằng câu xác lập. SKILL.md đồng bộ.

## [2.13.0] - 06/9/2026 — Nhóm K: văn bản chỉ đạo của UBND tỉnh do Sở dự thảo — giao việc cho cơ quan khác

### Thêm
- **reference/phong-tranh-sai-lam.md — Nhóm K MỚI** (K1–K7). Nguồn: dự thảo Công văn UBND tỉnh tăng cường quản lý VLNCN (bản 03/9/2026) bị Lãnh đạo Sở đọc nửa đầu và bôi đỏ 5 đoạn (1đ, 2a, 2b, 2c, 2d): *dùng từ vượt khỏi phong cách hành chính* + *trích dẫn điều khoản chưa chính xác*; rà tiếp nửa sau phát hiện mục 3 (Bộ CHQS tỉnh) sai thẩm quyền.
  - K1 không cài điều kiện tiên quyết vào thủ tục của cơ quan khác ("chỉ cấp GP vận chuyển sau khi…" ↔ Điều 41 Luật 42/2024 chốt cứng 03 ngày làm việc) → cơ chế phối hợp, đối chiếu.
  - K2 mỗi việc giao cơ quan X phải có điều khoản thẩm quyền của chính X (Bộ CHQS tỉnh không cấp Mệnh lệnh vận chuyển — Đ6 TT 98/2024/TT-BQP; Công an chỉ thẩm định 2 nội dung PCCC — Đ9 NĐ 105/2025; kiểm tra nghiệm thu PCCC dừng từ 01/7/2026 — NQ 66.18/2026); bảng 3 cột trước khi viết mục "Giao".
  - K3 bỏ tính từ đánh giá sau động từ thủ tục; K4 không ngoặc đơn giải thích trong câu giao việc; K5 thuật ngữ theo luật; K6 gọi tắt Luật một lần, điều khoản bị sửa ghi kèm văn bản sửa, không lặp ngày ở lần dẫn sau; K7 quy trình khi Lãnh đạo bôi đỏ một phần (sửa toàn văn, xóa đỏ ở paragraph mark, báo cáo 2 danh sách).
  - Lệnh QA nhanh `qa_all.py --forbid` cho các cụm đã bị bôi đỏ; checklist thêm ô [K]; mục "Khi tự phát hiện sắp mắc lỗi" thêm 3 dòng K2–K4.
- Khung đã sửa theo ý kiến Lãnh đạo lưu tại `sd-vlncn-sct-vn/vi-du-thuc-te/Du-thao-CV-UBND-tinh-chi-dao-tang-cuong-quan-ly-VLNCN-ban-sua-6.9.2026.docx` (mẫu 23 plugin đó, phiên bản 2026.9.6.1).

### Sửa
- SKILL.md: "10 nhóm A–J" → **"11 nhóm A–K"** tại 3 vị trí; tóm tắt Nhóm K trong mục "Luôn áp dụng" và danh sách nhóm; plugin.json description đồng bộ.

## [2.11.0] - 31/8/2026 — Nhóm J: giọng giải thích lọt vào thân văn bản

### Thêm
- **reference/phong-tranh-sai-lam.md — Nhóm J MỚI**. Bạn phát hiện lỗi tái phát qua câu *"Doanh nghiệp lưu ý điểm này để không nhầm rằng kho nhỏ thì được miễn thủ tục"* trong công văn hướng dẫn kho VLNCN. Cơ chế phát sinh: vừa soạn văn bản vừa viết phần giải thích cho người dùng trong cùng một mạch nên register bị rò. `check_document.py` không bắt được vì không sai thể thức, không sai căn cứ — phải tự soi thủ công.
  - **Tiêu chí một câu**: mỗi câu trong thân VBHC phải nêu quy định, nêu yêu cầu hoặc nêu sự việc.
  - **J1**: bảng 10 mẫu câu đã mắc thật kèm cách viết lại ("Đây là luồng đầy đủ nhất", "cần nắm rõ", "không đồng nghĩa với", "đáng kể", "công cụ pháp lý đúng là", "Điểm cần đặc biệt lưu ý"...).
  - **J2**: đề mục không dùng dạng hỏi đáp; chuyển "Câu hỏi 1: … ?" thành "1. Xác định … hay không".
  - **J3**: cấm từ định lượng cảm tính không kèm số.
  - **J4**: cấm câu meta về chính văn bản.
  - **J5**: ranh giới ngoại lệ — nêu bối cảnh, nguyên nhân khách quan ở đoạn mở đầu công văn vẫn hợp lệ.
  - Cách QA: `qa_all.py --forbid` cho các cụm hay tái phát, rồi đọc lại một lượt riêng chỉ soi register.

### Sửa
- Tiêu đề file: 8 nhóm → **10 nhóm A–J**; SKILL.md đổi "9 nhóm A–I" thành "10 nhóm A–J" tại 3 vị trí và bổ sung tóm tắt Nhóm J vào mục "Luôn áp dụng".

