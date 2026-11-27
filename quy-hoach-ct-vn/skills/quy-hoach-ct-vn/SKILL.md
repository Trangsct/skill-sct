---
name: quy-hoach-ct-vn
description: "QUY HOẠCH 04 ngành Công Thương Lào Cai: KHOÁNG SẢN, ĐIỆN/NĂNG LƯỢNG, KCN, CCN. Kích hoạt: quy hoạch điện VIII (QĐ 768/QĐ-TTg), quy hoạch khoáng sản QĐ 866 - 1626 - 2581/QĐ-TTg, quy hoạch tỉnh QĐ 525/QĐ-UBND, thủy điện, TBA, đường dây 500-220-110kV, đấu nối, apatit, đồng, đất hiếm, graphit, tọa độ khép góc mỏ. Dùng khi: xác định dự án nguồn điện/lưới điện/mỏ/KCN/CCN có trong quy hoạch không, thuộc quyết định nào; tra thăm dò - khai thác - chế biến khoáng sản nhóm I-IV; tham gia ý kiến, soạn báo cáo/công văn/tờ trình điều chỉnh quy hoạch; viết phần Căn cứ theo chuỗi chủ trương - chiến lược NQ 10-NQ/TW, NQ 88/NQ-CP, QĐ 334/QĐ-TTg; vốn cấp điện nông thôn (QĐ 2390/QĐ-UBND). Tra: QĐ 525 25/02/2026, QĐ 768 15/4/2025, QĐ 866 18/7/2023, QĐ 1626 15/12/2023, QĐ 2581 24/11/2025 (Tả Phời). Từ 15/9/2026 quy hoạch khoáng sản về Bộ Công Thương (NQ 66.25/2026). Điều chỉnh QH điện VIII bước 1 (VB 8151/BCT-ĐL, hạn 12/10/2026) và Đề án CN ứng dụng năng lượng nguyên tử (VB 7832/BCT-CLCS): ref 11."
---

# quy-hoach-ct-vn — Cẩm nang quy hoạch ngành Công Thương tỉnh Lào Cai

> **Tra văn bản gốc (Bạn chốt 09/10/2026, áp dụng mọi plugin):** đọc `van-ban-goc/00-DANH-MUC-CHUNG.md` và chạy `python3 scripts/tim_van_ban.py "<số hiệu hoặc cụm từ>"` TRƯỚC khi kết luận văn bản nào chưa có trong kho. Văn bản đã có trong danh mục thì phải mở toàn văn `.txt` cùng tên đặt cạnh bản gốc để trích; cấm trả lời "không có tài liệu", "chưa có trong gói", "không mở được toàn văn", "tra mạng khi cần nguyên văn". Khi Bạn gửi văn bản quy phạm pháp luật trong phiên: (a) đọc số, ngày, cơ quan, người ký bằng script (GATE), không đọc bằng mắt; (b) đặt tên `YYYY.MM.DD-SỐ.KÝ.HIỆU-Tên-trích-yếu-ngắn`, giữ nguyên định dạng gốc; (c) lưu vào `van-ban-goc/` của plugin chủ theo lĩnh vực, không nhân bản sang plugin khác; (d) sinh `.txt` bằng `scripts/trich_chu_van_ban_goc.py`; (e) chạy `scripts/build_so_cai_van_ban_goc.py` ở gốc kho để cập nhật danh mục; (f) cập nhật reference tóm tắt + CHANGELOG; (g) push, mở PR. Phiên không có quyền ghi kho thì nói ngay ở câu đầu và hướng dẫn Bạn dùng Hộp thư nạp kho `_inbox/` trên GitHub (`_inbox/README.md`, 6 bước), không được chỉ tóm tắt rồi bỏ qua tệp.

> **Lấy toàn văn văn bản quy phạm pháp luật từ thuvienphapluat.vn — TỰ ĐỘNG, không chờ Bạn nhắc (Bạn chốt 27/11/2026; quy trình đã chạy được 26/11/2026; áp dụng mọi plugin):** cần toàn văn một luật, nghị định, thông tư, quyết định… mà MCP `sct-tra-cuu` (`tra_phap_luat`, `tra_van_ban`, `tra_reference`) và `scripts/tim_van_ban.py` đều không có (thường là văn bản ngoài lĩnh vực công thương, vd Nghị định 335/2025/NĐ-CP về đánh giá công chức) thì tự lấy qua trình duyệt trên máy Bạn, không hỏi lại: (1) WebSearch chỉ dùng để tìm đường dẫn trang văn bản trên thuvienphapluat.vn (bản tóm tắt của báo không thay được toàn văn); WebFetch bị chặn ở thuvienphapluat.vn, luatnguyen, congbao.chinhphu.vn — không thử lại, không vòng qua bằng curl; (2) nạp công cụ Claude in Chrome trong MỘT lần ToolSearch (`list_connected_browsers`, `select_browser`, `tabs_context_mcp`, `tabs_create_mcp`, `navigate`, `get_page_text`, `javascript_tool`, `computer`, `tabs_close_mcp`); máy có 2 Chrome kết nối thì `select_browser` trước, Bạn không chỉ định thì chọn Browser 1; Chrome không kết nối thì làm y các bước bằng trình duyệt tích hợp của ứng dụng Claude; (3) mở tab mới (`tabs_context_mcp` createIfEmpty) → `navigate` tới trang văn bản → `get_page_text`; (4) `get_page_text` cắt ở 50.000 ký tự nên thường mất Phụ lục, mẫu biểu ở cuối — đây là giới hạn công cụ, KHÔNG phải trang chặn, không vội kết luận phải đăng nhập; lấy phần còn thiếu bằng `javascript_tool`: đọc `document.body.innerText`, cắt từ mốc (vd `lastIndexOf('PHỤ LỤC II')`), chuẩn hóa bớt xuống dòng và chuỗi dấu chấm, gán vào biến `window.__vb` rồi trả từng khúc khoảng 1.000–1.600 ký tự, ghép đủ đến hết văn bản; (5) trang đòi đăng nhập: tài khoản cơ quan đã lưu sẵn trong Chrome, chỉ bấm nút Đăng nhập, KHÔNG BAO GIỜ gõ mật khẩu; tài khoản dùng chung tối đa 5 người — hiện cảnh báo "có 1 người khác bị Đăng xuất" thì DỪNG, hỏi Bạn trước khi bấm Đồng ý (sẽ đẩy một đồng nghiệp ra); (6) lấy xong đóng tab (`tabs_close_mcp`); (7) đối chiếu số, ngày, cơ quan ban hành, trích yếu trên trang với văn bản cần tìm (số trùng khác năm là văn bản khác: 303/2025 ≠ 303/2026); (8) lưu vào kho để lần sau không phải lấy lại: tệp `.txt` toàn văn đặt tên `YYYY.MM.DD-SỐ.KÝ.HIỆU-Tên-trích-yếu-ngắn.txt`, dòng đầu ghi "Nguồn: thuvienphapluat.vn, lấy ngày dd/mm/yyyy", vào `van-ban-goc/` của plugin chủ theo lĩnh vực (ngoài mọi lĩnh vực → `vbhc-vn`), chạy `scripts/build_so_cai_van_ban_goc.py`, push, mở PR và merge; phiên không có quyền ghi kho thì vẫn giao tệp và hướng dẫn Bạn nạp qua Hộp thư `_inbox/`; (9) Bạn cần file thì dựng Word: Times New Roman 13, lề trên, dưới 2 cm, trái 3 cm, phải 2 cm; Chương, Mục, tiêu đề in đậm căn giữa; "Điều n." in đậm; soi bản PDF kiểm tra trang trắng rồi mới giao. Chỉ khi cả Chrome lẫn trình duyệt tích hợp không kết nối được, hoặc trang không có văn bản, mới báo Bạn tải bổ sung.

> **GATE PDF (áp dụng mọi plugin nghiệp vụ):** nhận PDF văn bản nhà nước → chạy `python3 "/mnt/skills/plugins/vbhc-vn:vbhc-vn/scripts/extract_metadata.py" "<file.pdf>"` TRƯỚC khi dẫn số/ngày/người ký. Context trống "Số: /…", "ngày … tháng …" là PDF ký số, KHÔNG phải bản dự thảo (vụ QĐ 5116/QĐ-SCT 02/9/2026). Chi tiết: plugin `vbhc-pdf-reader-vn`.


Skill này tổng hợp khung pháp lý và dữ liệu quy hoạch của **04 ngành thuộc phạm vi quản lý của ngành Công Thương** được tích hợp trong Quy hoạch tỉnh Lào Cai: **khoáng sản, điện/năng lượng, khu công nghiệp (KCN), cụm công nghiệp (CCN)**.

Trọng tâm là **lớp quy hoạch** — tức trả lời các câu hỏi: *dự án/mỏ/công trình này có trong quy hoạch không, thuộc quyết định nào, ở giai đoạn nào, quy mô bao nhiêu, vị trí xã nào.* Phần thủ tục thành lập, cấp phép, chấm điểm chủ đầu tư KCN/CCN do skill `kcn-ccn-vn` đảm nhiệm; phần cấp phép, kiểm tra HHNH/hóa chất do `hnh-sct-vn` đảm nhiệm — skill này KHÔNG thay thế các skill đó.

## I. KHI NÀO DÙNG SKILL NÀY

Tham chiếu skill này khi:

1. Tra cứu một dự án **nguồn điện** (thủy điện, sinh khối, gió, mặt trời, rác), **lưới điện** (TBA, đường dây 500/220/110kV) có trong Quy hoạch điện VIII điều chỉnh / Quy hoạch tỉnh Lào Cai hay không; quy mô, vị trí, phương án đấu nối, giai đoạn.
2. Tra cứu khu vực **thăm dò, khai thác, chế biến khoáng sản** nhóm I/II/III/IV trên địa bàn; phân định thẩm quyền quy hoạch khoáng sản (quốc gia vs tỉnh).
3. Tra cứu danh mục, vị trí, diện tích **KCN/CCN theo quy hoạch tỉnh** (Phụ lục II, III QĐ 525) — để lập danh mục, đối chiếu quy hoạch.
4. Tham gia ý kiến, rà soát, góp ý dự thảo **điều chỉnh quy hoạch tỉnh**, quy hoạch điện, quy hoạch khoáng sản, phương án phát triển công nghiệp.
5. Soạn báo cáo, công văn, tờ trình, phiếu góp ý về quy hoạch ngành; xác định **mối quan hệ tích hợp** giữa quy hoạch ngành quốc gia (điện VIII, khoáng sản 866) và quy hoạch tỉnh.
6. Giải thích **hệ thống quy hoạch** theo Luật Quy hoạch 2017 (quốc gia → vùng → tỉnh → có tính chất kỹ thuật chuyên ngành).
7. Viết phần **"Căn cứ…"** hoặc phần mở đầu báo cáo/tờ trình về khoáng sản cần dẫn đúng **chuỗi chủ trương → chiến lược → quy hoạch** (NQ 10-NQ/TW → NQ 88/NQ-CP → QĐ 334/QĐ-TTg → QĐ 866/QĐ 1626); tra **định hướng chiến lược** của một loại khoáng sản (đồng, sắt, đất hiếm, apatit, đá hoa trắng) — phần này ở QĐ 334, KHÔNG ở QĐ 866. **Xem ref 10**.

Quy trình chuẩn khi cần TẠO FILE văn bản:
- **Bước 1:** Tham chiếu skill này (và `kcn-ccn-vn` nếu là KCN/CCN) để xác định đúng căn cứ, số liệu, danh mục quy hoạch.
- **Bước 2:** Dùng skill `vbhc-vn` để tạo file .docx đúng thể thức Sở Công Thương.

## II. KHUNG PHÁP LÝ QUY HOẠCH (cập nhật tháng 6/2026)

### 1. Luật, nghị định nền tảng về quy hoạch

| Văn bản | Nội dung | Ghi chú |
|---|---|---|
| Luật Quy hoạch số 21/2017/QH14 | Hệ thống quy hoạch quốc gia; tích hợp đa ngành vào quy hoạch tỉnh | Hiệu lực 01/01/2019 |
| Luật số 35/2018/QH14; Luật số 61/2020/QH14; Luật sửa đổi ngày 29/11/2024 | Sửa đổi, bổ sung các luật có liên quan đến quy hoạch | Luật 29/11/2024 sửa Luật QH, Luật ĐT, Luật PPP, Luật Đấu thầu |
| Nghị định số 37/2019/NĐ-CP | Quy định chi tiết Luật Quy hoạch | Sửa bởi NĐ 58/2023/NĐ-CP (12/8/2023) và NĐ 22/2025/NĐ-CP (11/02/2025) |
| **Luật Quy hoạch số 112/2025/QH15 ngày 10/12/2025**; **NĐ 70/2026/NĐ-CP ngày 09/3/2026** (chi tiết Luật Quy hoạch) | Luật 112/2025 là căn cứ của QĐ 525 (25/02/2026); NĐ 70/2026: Điều 26 nội dung quy hoạch tỉnh, Điều 55 đánh giá thực hiện quy hoạch; nhiệm vụ quy hoạch khoáng sản tại Phụ lục I chuyển Bộ Công Thương thực hiện theo NQ 66.25/2026 (plugin qlks-sct-vn ref 23) | Dẫn hai văn bản này khi viện dẫn khung quy hoạch sau 2025; hai dòng trên (Luật 21/2017, NĐ 37/2019) để tra lịch sử — đối chiếu bản gốc trước khi kết luận văn bản nào bị thay thế. Dự thảo Bộ tiêu chí đánh giá thực hiện quy hoạch tỉnh (Bộ Tài chính 11/2026): **ref 13 mục G** |

### 2. Quy hoạch ngành quốc gia (cấp trên, ràng buộc tỉnh)

| Văn bản | Lĩnh vực | Tình trạng |
|---|---|---|
| **NQ 10-NQ/TW ngày 10/02/2022** (Bộ Chính trị) | Định hướng **chiến lược** địa chất, khoáng sản và công nghiệp khai khoáng đến 2030, tầm nhìn 2045 | Chủ trương gốc; thay NQ 02-NQ/TW 2011. Lào Cai triển khai bằng CTr 39-CTr/TU 29/01/2026, KH 200/KH-UBND 05/5/2026. **Xem ref 10** |
| **NQ 88/NQ-CP ngày 22/7/2022** | Chương trình hành động của Chính phủ thực hiện NQ 10-NQ/TW; danh mục **18 nhiệm vụ** | Nhiệm vụ 7 → QĐ 866 (**Bộ Công Thương chủ trì lập**), 8 → QĐ 1626, 9 → QH năng lượng quốc gia, 11 → Quy hoạch tỉnh có phương án bảo vệ, sử dụng KS. **Xem ref 10** |
| **QĐ 334/QĐ-TTg ngày 01/4/2023** | **Chiến lược** địa chất, khoáng sản và công nghiệp khai khoáng đến 2030, tầm nhìn 2045 | PTT Trần Hồng Hà ký; hiệu lực từ ngày ký. Chứa **định hướng từng loại khoáng sản** + mục tiêu 2025/2030/2045 + phân công Bộ Công Thương, UBND tỉnh. **Xem ref 10** |
| **QĐ 768/QĐ-TTg ngày 15/4/2025** | **Điều chỉnh Quy hoạch điện VIII** (phát triển điện lực quốc gia 2021-2030, tầm nhìn 2050) | Hiệu lực kể từ ngày ký; thay thế QĐ 500/QĐ-TTg ngày 15/5/2023. Ký: KT. Thủ tướng - PTT Bùi Thanh Sơn. **Xem ref 02** |
| **QĐ 866/QĐ-TTg ngày 18/7/2023** | Quy hoạch thăm dò, khai thác, chế biến, sử dụng các loại **khoáng sản** (nhóm I; trừ dầu khí, than, phóng xạ, VLXD, phân tán nhỏ lẻ) | Hiệu lực kể từ ngày ký; PTT Trần Hồng Hà ký. Đang rà soát điều chỉnh (KH thực hiện QĐ 333/QĐ-TTg 23/4/2024). **Xem ref 04** |
| **QĐ 1626/QĐ-TTg ngày 15/12/2023** | Quy hoạch thăm dò, khai thác, chế biến, sử dụng khoáng sản **làm vật liệu xây dựng** (nhóm II) | **Xem ref 04** |
| **QĐ 154/QĐ-TTg ngày 29/01/2022** | Kéo dài kỳ quy hoạch KS làm **VLXD** và KS làm **xi măng** (QĐ 152/2008, QĐ 45/2012; QĐ 105/2008, QĐ 1065/2010) cho tới khi QH VLXD 2021-2030 được phê duyệt | **LỊCH SỬ — hết vai trò từ 15/12/2023** (khi QĐ 1626 ban hành). Chỉ dùng giải trình hồ sơ 29/01/2022 → 15/12/2023. **Xem ref 10 mục V** |
| **QĐ 995/QĐ-TTg 09/8/2018** · **QĐ 836/QĐ-BXD 14/10/2019** | Giao các bộ lập quy hoạch ngành quốc gia 2021-2030; kế hoạch tổ chức lập quy hoạch KS làm VLXD của Bộ Xây dựng | **LỊCH SỬ — quy trình, không có danh mục mỏ.** Quy trình 3 giai đoạn: **ref 01 mục 5**; đối chiếu tiến độ: **ref 10 mục V.2** |
| **QĐ 2581/QĐ-TTg ngày 24/11/2025** | Điều chỉnh QĐ 866 — bổ sung/điều chỉnh **mỏ đồng Tả Phời** (xã Hợp Thành, Lào Cai); Phụ lục III.10 (khai thác) và VI.10 (tọa độ) | ĐÃ KÝ. **Xem ref 07** |
| Dự thảo Điều chỉnh QH khoáng sản nhóm I (Cục ĐC&KS - Bộ NN&MT, 3/2026) | Rà soát toàn diện QĐ 866; danh mục mỏ nhóm I Lào Cai (đồng, sắt, đất hiếm, graphit) | **CHƯA KÝ** — chỉ tham khảo/góp ý. **Xem ref 07** |
| Luật Điện lực số 61/2024/QH15 ngày 30/11/2024 | Quy hoạch phát triển điện lực, đầu tư xây dựng | Hiệu lực 01/02/2025; NĐ 56/2025/NĐ-CP (03/3/2025) hướng dẫn về quy hoạch điện lực, phương án phát triển mạng lưới cấp điện |
| Luật Địa chất và Khoáng sản số 54/2024/QH15 | Địa chất, khoáng sản; phân nhóm I-IV; thẩm quyền tỉnh điều tra cơ bản nhóm III, IV | Hiệu lực 01/7/2025; sửa bởi Luật số 147/2025/QH15 (hiệu lực 01/01/2026) |

### 3. Quy hoạch tỉnh Lào Cai (tích hợp cả 04 ngành)

| Văn bản | Nội dung | Ngày |
|---|---|---|
| **QĐ 525/QĐ-UBND** của Chủ tịch UBND tỉnh | Phê duyệt **điều chỉnh Quy hoạch tỉnh Lào Cai 2021-2030, tầm nhìn 2050** (sau sáp nhập, căn cứ NQ 05/NQ-HĐND 09/02/2026). Tích hợp phương án phát triển điện, khoáng sản, KCN, CCN. Phụ lục II (KCN), Phụ lục III (CCN). **Xem ref 05, 06** | 25/02/2026 |
| Báo cáo điều chỉnh Quy hoạch tỉnh (thuyết minh) | Tài liệu thuyết minh tích hợp đầy đủ hiện trạng + phương án 04 ngành; nguồn của các danh mục chi tiết. **Xem ref 03, 04, 06** | bản 18/4 và 07/6/2026 |

> ⚠️ **Cảnh báo lỗi nguồn:** Bản thuyết minh Báo cáo điều chỉnh QHT (07/6/2026) ghi nhầm "QĐ 866/QĐ-TTg ngày **17/8/2023**". Ngày đúng đã xác minh là **18/7/2023**. Khi trích dẫn trong văn bản chính thức, dùng **18/7/2023**.

## III. CÁC REFERENCE FILES (đọc khi cần đào sâu)

| Reference | Khi cần dùng |
|---|---|
| `references/01-he-thong-quy-hoach.md` | Khi giải thích hệ thống quy hoạch, mối quan hệ quốc gia–vùng–tỉnh–ngành; vai trò Sở Công Thương trong lập/điều chỉnh quy hoạch; nguyên tắc tích hợp. **Mục 5: quy trình 3 giai đoạn lập một quy hoạch ngành quốc gia** (QĐ 995/QĐ-TTg 09/8/2018 giao nhiệm vụ; ví dụ mẫu QĐ 836/QĐ-BXD) và **2 lần địa phương được lấy ý kiến** — góp nhiệm vụ vs góp danh mục mỏ |
| `references/02-qh-dien-viii-qd768.md` | Khi cần quan điểm, mục tiêu, cơ cấu nguồn điện quốc gia, lưới truyền tải theo QĐ 768; các chỉ tiêu công suất, điện thương phẩm, tỷ lệ NLTT toàn quốc |
| `references/03-dien-lao-cai.md` | NGUỒN CHI TIẾT về điện Lào Cai: hiện trạng nguồn/lưới + **danh mục phương án** nguồn điện (thủy điện, sinh khối, gió, mặt trời, rác), TBA & đường dây 500/220/110kV theo Báo cáo QHT (Bảng 32-43). Dùng khi tra một dự án cụ thể, lập danh mục, đối chiếu đấu nối |
| `references/04-khoang-san.md` | NGUỒN CHI TIẾT về khoáng sản: phân nhóm I-IV, thẩm quyền quy hoạch; khu vực thăm dò–khai thác Lào Cai (apatit, đồng, sắt, đất hiếm, graphit, đá hoa trắng, kaolin); VLXDTT; QĐ 866, 1626, Luật ĐCKS 2024 |
| `references/05-kcn-ccn-quy-hoach.md` | Khi tra danh mục, vị trí xã, diện tích KCN (Phụ lục II) và CCN (Phụ lục III) theo QĐ 525. **Trỏ sang `kcn-ccn-vn`** cho thành lập, cấp phép, chấm điểm chủ đầu tư |
| `references/06-cau-truc-bao-cao-qht.md` | Khi soạn/rà soát/góp ý báo cáo thuyết minh quy hoạch tỉnh hoặc phương án phát triển ngành; cấu trúc chuẩn của Báo cáo điều chỉnh QHT |
| `references/07-dieu-chinh-qd866-lao-cai.md` | Khi cần **danh mục mỏ nhóm I cụ thể trên địa bàn Lào Cai** (đồng Sin Quyền/Tả Phời/Vi Kẽm/Khe Cam, sắt Quý Xa/Kíp Tước, đất hiếm Yên Phú, graphit Bảo Hà/Nậm Thi); QĐ 2581/QĐ-TTg (Tả Phời, đã ký) và dự thảo điều chỉnh QĐ 866 (3/2026, chưa ký) |
| `references/08-toa-do-tham-do-che-bien-lao-cai.md` | Khi cần **tọa độ khép góc**, danh mục **thăm dò (Phụ lục II)**, **chế biến (Phụ lục IV)** các mỏ Lào Cai; hướng dẫn tra file nguồn gốc cho số liệu chính xác |
| `references/09-von-dtc-cap-dien-2026-2030.md` | Khi cần **vốn đầu tư công trung hạn 2026-2030 cho các dự án cấp điện do Sở Công Thương làm chủ đầu tư** (QĐ 2390/QĐ-UBND ngày 09/7/2026): 07 dự án / 130.447 triệu đồng, toàn bộ từ nguồn thu tiền sử dụng đất — 04 chuyển tiếp (cấp điện nông thôn Yên Bái 2014-2025, khắc phục thiên tai 2024, Sín Chải, Lếch Mông) + 03 khởi công mới theo QĐ 1411-1413/QĐ-UBND 28/4/2026 (Sơn Lương, Đề Chơ - Phình Hồ, Khao Mang - Mù Cang Chải - Lao Chải); lưu ý 03 dự án mới xếp ở lĩnh vực Nông nghiệp-PTNT chứ không phải công nghiệp; cách viết đúng khi viện dẫn |
| `references/10-chu-truong-chien-luoc-khoang-san.md` | Khi cần **chuỗi chủ trương → chiến lược → quy hoạch** khoáng sản: **NQ 10-NQ/TW 10/02/2022** (quan điểm, mục tiêu 2025/2030/2045, câu về mỏ sắt Quý Xa), **NQ 88/NQ-CP 22/7/2022** (danh mục 18 nhiệm vụ, ai chủ trì QĐ 866/1626, nghĩa vụ bố trí kinh phí bảo vệ KS chưa khai thác + báo cáo 31/12 hằng năm), **QĐ 334/QĐ-TTg 01/4/2023** (Chiến lược — **định hướng thăm dò/khai thác/chế biến từng loại khoáng sản**, danh mục dự trữ KS quốc gia, phân công Bộ Công Thương và UBND tỉnh), **QĐ 154/QĐ-TTg 29/01/2022** và **QĐ 836/QĐ-BXD 14/10/2019** (kéo dài kỳ QH VLXD + kế hoạch lập QH VLXD — lịch sử, mạch QĐ 836 → QĐ 154 → QĐ 1626 giải trình vì sao chậm 26 tháng); 9 anti-error khi viện dẫn |
| `references/11-dieu-chinh-qh-dien-viii-buoc-1-va-de-an-nang-luong-nguyen-tu-10-2026.md` | **(MỚI 10/10/2026) Hai đề án trung ương lấy ý kiến tháng 10/2026:** **(A) Điều chỉnh Quy hoạch điện VIII (bước 1)** — VB 8151/BCT-ĐL 07/10/2026; UBND tỉnh giao Sở chủ trì (10251/UBND-KT 08/10), **báo cáo trước 12/10/2026**; CV 6415/SCT-NL 09/10 (PGĐ Giang) lấy ý kiến sở, ngành, xã, PC Lào Cai hạn 11h 12/10; Phòng QLKS, QLCN, KH-TH góp ý theo lĩnh vực gửi Phòng QLNL; việc của phòng khi góp ý (đối chiếu danh mục nguồn, lưới QĐ 768; phụ tải KCN/CCN, mỏ; dự án chậm/bổ sung); **(B) Đề án phát triển công nghiệp ứng dụng năng lượng nguyên tử** — VB 7832/BCT-CLCS 29/9/2026 (hồ sơ 3 phần), Sở lấy ý kiến CV 6220/SCT-CN 02/10; bảng 14 ý kiến đã nhận đến 09/10 (13 nhất trí; **xã Bản Liền 741/UBND-KT đề nghị bổ sung 4 nội dung**: chiếu xạ bảo quản nông sản, phân bố trung tâm dịch vụ, an toàn bức xạ – phối hợp 3 cấp, cơ chế hỗ trợ địa phương); khuôn văn bản tổng hợp ý kiến; 4 anti-error |
| `references/12-ctdt-nguon-dien-va-chinh-sach-dmt-mai-nha-ho-gia-dinh-11-2026.md` | **(MỚI 03/11/2026) Chủ trương đầu tư nguồn điện và chính sách điện mặt trời mái nhà hộ gia đình:** QĐ 3938/QĐ-UBND 22/10/2026 chấp thuận CTĐT **thủy điện Tung Chung** 9,2 MW (khởi công Quý I/2027, phát điện Quý I/2029); TB 793/TB-STC 02/11 **Nậm Lành** chưa đủ cơ sở (vốn chủ sở hữu); TB 765/TB-STC 28/10 **ĐMT Nậm Đông IV** — Sở NN&MT chưa nhất trí (đất Trạm Tấu còn 9,03/33,7 ha), ý kiến Sở 6830/SCT-NL (tọa độ VN-2000 hành lang 35 kV); khuôn ý kiến Sở khi phối hợp thẩm định CTĐT nguồn điện; **TTr 1659/TTr-UBND 03/11/2026** đăng ký xây dựng **NQ HĐND hỗ trợ hộ gia đình lắp ĐMT mái nhà và lưu trữ điện 2027–2030** (theo TTr 7097/TTr-SCT 29/10, VB 10790/VPCP-CN hạn tháng 12/2026); TT 70/2026/TT-BCT định mức kiểm toán năng lượng; 3 anti-error |
| `references/13-ky-cap-nhat-17-11-2026-dmt-mai-nha-an-toan-dap-gp-dien-luc.md` | **(MỚI 17/11/2026)** (A) **NQ HĐND hỗ trợ hộ gia đình lắp ĐMT mái nhà 2027–2030**: NQ 264/NQ-TT 12/11/2026 chấp thuận, **thủ tục thông thường**; CV 11687/UBND-KT giao Sở chủ trì; QĐ 7634/QĐ-SCT Tổ soạn thảo; CV 7642/SCT-NL xin ý kiến hạn 19/11, kỳ họp HĐND 08–09/12/2026; dự thảo 9 điều, **≤ 50 triệu đồng/hộ**, 540 hộ không thể cấp điện lưới → 27 tỷ; bảng ý kiến đã nhận; 4 điểm Sở Tư pháp 2449/STP; (B) Chỉ thị 09, 10/CT-TTg, VB 10790/VPCP-CN, **KH 268/KH-UBND** (ĐMT mái nhà > 500 MW đến 2030), **KH 147/KH-UBND** (NQ 70: nguồn ~4.622 MW; báo cáo trước 15/11 hằng năm); (C) **NĐ 407/2026/NĐ-CP** (EVN, hiệu lực 28/12/2026); (D) chuyển giao công trình điện theo NĐ 02/2024 (7649/SCT-NL hỏi Cục Điện lực); (E) rà soát **GP hoạt động điện lực** (7401/SCT-NL; GP-SCT do Sở cấp); (F) **phương án bảo vệ đập, ứng phó khẩn cấp thủy điện do UBND xã phê duyệt** theo QĐ 66/2026/QĐ-UBND (Nậm Hô: QĐ 1192, 1197/QĐ-UBND xã Dền Sáng); (G) dự thảo **Bộ tiêu chí giám sát, đánh giá thực hiện quy hoạch tỉnh** (Bộ Tài chính, NĐ 70/2026 Điều 26, 55); 6 anti-error |
| `references/14-ky-cap-nhat-24-11-2026-gop-y-nq-dmt-kiem-tra-du-an-dien-qh-nghia-lo.md` | **(MỚI 24/11/2026)** (A) **Tổng hợp ý kiến góp ý dự thảo NQ HĐND hỗ trợ hộ gia đình lắp ĐMT mái nhà 2027–2030** (CV 7642/SCT-NL): 14 đơn vị nhất trí, 5 đơn vị có ý kiến nội dung — **Sở Tài chính 9307/STC-TĐ** (viết lại Điều 1; thống nhất Điều 2 – Điều 6; tiêu chí "không thể cấp điện lưới" có điện lực + UBND xã xác nhận; mỗi hộ một lần, không trùng; hỗ trợ **bằng hiện vật**; dự toán chi tiết làm cơ sở mức 50 triệu; phân kỳ 2027–2030; câu sửa Điều 3), xã Mường Khương, phường Sa Pa, xã Pha Long, **PC Lào Cai 5029/PCLK-KD** (2 phương án song song, 1 triệu đồng/kWp tối đa 3 triệu); xã Lâm Thượng gửi nhầm văn bản; 2714/STP-XDVBQPPL, 1610/MTTQ-BTT chưa có toàn văn; (B) **kiểm tra dự án thủy điện đang vận hành của Sở Tài chính** theo khoản 2 Điều 65 NĐ 19/2026/NĐ-CP, TT 44/2026/TT-BTC (Nậm Khánh 12 MW — TB 857/TB-STC; Yên Hà — TB 870/TB-STC) và việc Sở cho ý kiến khi điều chỉnh GCN đầu tư; (C) giấy phép hoạt động điện lực thủy điện Minh Lương (94/GP-ĐL Cục Điện lực, hạn 26/3/2028), đường dây đấu nối do đơn vị khác có giấy phép quản lý; (D) **QĐ 7643/QĐ-SCT** kiểm tra an toàn điện, hợp đồng mua bán điện (Đoàn ký TB-ĐKT); (E) **QĐ 4355/QĐ-UBND 20/11/2026 quy hoạch chung đô thị liên phường Nghĩa Lộ – Trung Tâm – Cầu Thia – Liên Sơn**: cấp điện khớp QĐ 768/QĐ 525 (TBA 220 kV Nghĩa Lộ 2×250 MVA; 110 kV Nghĩa Lộ, Ba Khe), hạ ngầm lưới, đất KS – VLXD 72,10 → 199,16 ha; 6 anti-error (7642/**SCT**-NL; 8859/BCT-ĐL ngày **16/10/2026**; 272 MW chỉ là dự kiến) |
| `references/15-ranh-gioi-so-hoa-9-so-do-khoang-san-nhom-I-lao-cai.md` | **(MỚI 25/11/2026) Ranh giới số hóa 09 sơ đồ quy hoạch khoáng sản nhóm I tỉnh Lào Cai** (bản vẽ 3.3, 3.4 chì kẽm; 4.6 sắt; 8.4, 8.5 đồng; 9.3 vàng; 11.2, 11.3 đất hiếm; 12 apatit): 123 khu vực, 1.129 điểm góc, VN-2000 KTT 105° múi 6° + WGS84; tệp trong `du-lieu/` (KMZ gốc Bạn gửi, CSV, bảng Word); `scripts/tra_toa_do_quy_hoach.py` tra điểm nằm trong khu vực nào, tra theo tên; kết quả đối chiếu Phụ lục VI dự thảo điều chỉnh QĐ 866 (113/123 khớp, 10 khu vực lệch phải đối chiếu); các khu chồng lấn nhau; cảnh báo hệ tọa độ khác hồ sơ cấp phép của tỉnh (KTT 104°45' múi 3°). Dùng khi rà dự án, CCN, KCN có chồng lấn quy hoạch khoáng sản không |

## IV. FILE NGUỒN GỐC ĐỂ TRA CỨU CHÍNH XÁC (`sources/`)

Thư mục **`sources/`** chứa **toàn văn các văn bản gốc** (text trích từ PDF/DOCX) để tra cứu đầy đủ, chính xác — không chỉ dựa vào reference tóm tắt. Xem mục lục `sources/00-MUC-LUC-NGUON.md`.

**Khi nào mở file nguồn:** bất kỳ lúc nào cần số liệu/danh mục/tọa độ CHÍNH XÁC để đưa vào văn bản (ví dụ: tọa độ khép góc một mỏ, công suất một dự án điện, trữ lượng một khoáng sản). Reference (ref 02-08) cho khung và phần Lào Cai trích sẵn; file nguồn cho chi tiết toàn văn.

**Cách tra:** grep theo **TÊN MỎ + TÊN XÃ** hoặc **tên dự án điện** (KHÔNG theo số phụ lục — chỉ số không nhất quán), rồi đọc khối xung quanh. Ví dụ:
```bash
grep -n -i "quý xa\|tả phời" sources/qd866-dieuchinh-2026-phuluc.txt
```
File hiện có: `qd866-dieuchinh-2026-thuyetminh.txt` và `...phuluc.txt` (DỰ THẢO 3/2026), `qd768-quyhoach-dien-viii-toanvan.txt` (ĐÃ KÝ), `qht-laocai-2026-baocao-thuyetminh.txt` và `...phuluc.txt` (bản thao tác QHT Lào Cai 7/6/2026, tích hợp cả 04 ngành), và 05 văn bản trung ương về khoáng sản ĐÃ KÝ: `qd2581-dieuchinh-qd866-toanvan.txt`, `qd334-chien-luoc-dckscnkk-toanvan.txt`, `nq10-nqtw-2022-toanvan.txt`, `nq88-nqcp-2022-toanvan.txt`, `qd154-keodai-ky-qh-vlxd-ximang-toanvan.txt`, `qd836-bxd-ke-hoach-lap-qh-vlxd-toanvan.txt`. Có thể bổ sung file nguồn mới theo hướng dẫn trong mục lục.

Thư mục **`du-lieu/`** (từ 25/11/2026): file KMZ gốc ranh giới 09 sơ đồ quy hoạch khoáng sản nhóm I Lào Cai, CSV tọa độ 1.129 điểm, bảng Word — xem ref 15.

Thư mục **`van-ban-goc/`** giữ **bản gốc DOCX** của 06 văn bản trung ương nêu trên (mục lục `van-ban-goc/00-MUC-LUC.md`) — dùng khi cần mở đọc nguyên văn, đối chiếu thể thức hoặc gửi kèm.

> **Phân biệt pháp lý khi trích nguồn:** số liệu từ file *dự thảo* (qd866-dieuchinh-2026-*) chỉ để tham khảo/góp ý; viện dẫn chính thức phải căn cứ văn bản **ĐÃ KÝ** (QĐ 866 18/7/2023, QĐ 2581 24/11/2025, QĐ 768 15/4/2025, QĐ 525 25/02/2026).

## V. NGUYÊN TẮC BẤT BIẾN

1. **Không bịa số/ngày văn bản quy hoạch.** Khi không chắc, ghi "[XX]/QĐ-... ngày .../.../...." và đề nghị xác minh; báo người dùng. Đặc biệt cẩn trọng với số liệu công suất (MW), trữ lượng, diện tích — đây là dữ liệu thay đổi theo từng lần điều chỉnh quy hoạch.

2. **Phân biệt rõ 03 cấp quy hoạch điện/khoáng sản:**
   - **Quy hoạch ngành quốc gia** (điện VIII - QĐ 768; khoáng sản - QĐ 866, 1626): xác định tổng thể, định hướng, danh mục dự án trọng điểm. Tỉnh KHÔNG được mâu thuẫn.
   - **Quy hoạch tỉnh** (QĐ 525): tích hợp phương án phát triển ngành trên địa bàn, cụ thể hóa cho từng xã/khu vực.
   - **Kế hoạch thực hiện** và các quyết định chấp thuận/cấp phép từng dự án: bước triển khai.
   Khi tra "dự án X có trong quy hoạch không", phải nói rõ trong quy hoạch **nào**.

3. **Tuân thủ địa giới hành chính mới sau 01/7/2025 (NQ 202/2025/QH15; mô hình 02 cấp).** Tỉnh Lào Cai mới gồm cả địa bàn Yên Bái cũ; 99 xã/phường, không có cấp huyện. Danh mục nguồn điện/mỏ trong Báo cáo QHT 07/6/2026 đã dùng **tên xã mới** (ví dụ: Xã Hạnh Phúc, Đông Cuông, Phong Dụ Hạ, Khao Mang...). Khi viện dẫn vị trí, dùng tên xã/phường mới; nếu tài liệu cũ còn ghi huyện/xã cũ (Văn Yên, Trấn Yên, Văn Chấn, Lục Yên...) thì quy đổi và ghi chú.

4. **Khoáng sản — phân định thẩm quyền quy hoạch (Luật ĐCKS 54/2024):**
   - Nhóm I (kim loại, năng lượng, hóa chất giá trị cao): theo QĐ 866 quốc gia.
   - Nhóm II (khoáng chất công nghiệp, VLXD cao cấp): theo QĐ 1626 quốc gia.
   - Nhóm III, IV (VLXD thông thường, phân tán nhỏ lẻ): **UBND tỉnh** được tổ chức điều tra cơ bản, khoanh định, đưa vào quy hoạch tỉnh (Điều 14, Điều 20 Luật 54/2024). Đây là điểm mới so với Luật Khoáng sản 2010.

5. **Điện — không nhầm "nguồn điện" với "lưới điện".** Danh mục nguồn (Bảng 32-36 QHT) và danh mục lưới (Bảng 37-43) là hai nhóm khác nhau. Khi tra dự án thủy điện phải xem cả phương án đấu nối (lưới) đi kèm.

6. **KCN/CCN — chỉ dùng skill này cho lớp quy hoạch.** Mọi nội dung thành lập, mở rộng, điều chỉnh, chấm điểm chủ đầu tư, điều kiện khởi công → chuyển sang `kcn-ccn-vn`. Số liệu hiện trạng/lấp đầy CCN mới nhất cũng ở `kcn-ccn-vn` (Báo cáo 18/6/2026).

7. **Số liệu thay đổi nhanh & quy hoạch đang được điều chỉnh.** Cả QĐ 866 (đang rà soát điều chỉnh) và NĐ 35/2022 đều có thể thay đổi. Khi người dùng hỏi số liệu mới nhất, báo rõ mốc thời gian của dữ liệu trong skill và đề nghị cập nhật từ cơ quan đầu mối.

8. **Phân biệt 3 lớp khi trả lời về khoáng sản:** *định hướng chiến lược* (NQ 10-NQ/TW, QĐ 334) ≠ *danh mục quy hoạch* (QĐ 866, QĐ 1626 + các quyết định điều chỉnh như QĐ 2581) ≠ *dự án đã được chấp thuận chủ trương đầu tư/cấp phép*. Câu kiểu "đầu tư mở rộng cơ sở chế biến đồng kim loại tại Lào Cai" (QĐ 334) là định hướng quốc gia, KHÔNG phải dự án đã có chủ trương. Khi dẫn nguyên văn NQ 10/NQ 88/QĐ 334 thì giữ tên cơ quan trong bản gốc ("Bộ Tài nguyên và Môi trường") và **ghi chú trong ngoặc** tên cơ quan hiện nay (Bộ Nông nghiệp và Môi trường; mảng địa chất, khoáng sản từ 15/9/2026 là Bộ Công Thương). Chi tiết: ref 10 mục VI.

9. **Nguyên tắc trích dẫn.** Trong văn bản hành chính ghi đầy đủ "Quyết định số 768/QĐ-TTg ngày 15 tháng 4 năm 2025 của Thủ tướng Chính phủ phê duyệt Điều chỉnh Quy hoạch phát triển điện lực quốc gia thời kỳ 2021-2030, tầm nhìn đến năm 2050". Tránh viết tắt "QH điện VIII", "QĐ 866" trong văn bản chính thức (chỉ dùng nội bộ).

## VI. NGƯỜI KÝ MẶC ĐỊNH CHO VĂN BẢN VỀ QUY HOẠCH NGÀNH

(Phối hợp skill `sct-laocai-org-vn` và `vbhc-vn`)

| Loại văn bản | Người ký mặc định |
|---|---|
| Báo cáo/Tờ trình tổng thể quy hoạch ngành gửi UBND tỉnh, Tỉnh uỷ | Giám đốc Hoàng Chí Hiền |
| Công văn tham gia ý kiến quy hoạch điện, lưới điện, năng lượng | KT. Giám đốc - PGĐ Nguyễn Trường Giang (phụ trách năng lượng, Phòng QLNL — QĐ 7750/QĐ-SCT ngày 17/11/2026, thay QĐ 6320/QĐ-SCT ngày 06/10/2026) |
| Công văn tham gia ý kiến quy hoạch khoáng sản | KT. Giám đốc - PGĐ Hoàng Văn Thuân (công nghiệp khai thác mỏ và chế biến khoáng sản) hoặc PGĐ Phạm Năng Chung (địa chất và phần khoáng sản còn lại; phụ trách Phòng Quản lý Khoáng sản) — QĐ 7750/QĐ-SCT ngày 17/11/2026 (thay QĐ 6320/QĐ-SCT ngày 06/10/2026); QĐ 7750 không liệt kê từng đầu việc, ý kiến gồm cả hai phần thì hỏi Bạn |
| Công văn tham gia ý kiến về VLNCN | KT. Giám đốc - PGĐ Hoàng Văn Thuân (từ 17/11/2026, QĐ 7750/QĐ-SCT; 05/10–16/11/2026 PGĐ Nguyễn Đình Chiến theo QĐ 6320/QĐ-SCT — lịch sử) |
| Công văn tham gia ý kiến quy hoạch KCN, CCN | KT. Giám đốc - PGĐ Nguyễn Đình Chiến (phụ trách KCN, CCN) |
| Phiếu góp ý nội bộ, công văn nghiệp vụ Phòng QLCN | Theo lĩnh vực: PGĐ phụ trách tương ứng |

Dòng Lưu ghi `Lưu: VT, CN(Tên).` — tên chuyên viên soạn thảo, Nơi nhận có Ban Giám đốc Sở (Bạn chốt 16/11/2026). Chuyên viên tham mưu tra bảng phân công Phòng QLCN trong skill `sct-laocai-org-vn`: KCN/CCN và tham gia ý kiến dự án công nghiệp → **CV Trung**; điện/khoáng sản → theo chuyên viên phụ trách.
