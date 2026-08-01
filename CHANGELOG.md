# Nhật ký thay đổi bộ skill

## 2026-08-01 — `qlks-sct-vn` v1.5.0: nghiệp vụ 10 — THU HỒI KHOÁNG SẢN (nạo vét lòng hồ thủy điện + đất đá thải mỏ)

- Nguồn: 20 tài liệu thật do Bạn gửi ngày 01/8/2026 (thư mục `Khoáng sản/Thu hồi tận thu`): CV **216/ATMT-ATĐ** ngày 30/01/2026 của Cục Kỹ thuật an toàn và Môi trường công nghiệp - Bộ Công Thương; CV **2419/ĐCKS-PCKS** ngày 19/9/2025 của Cục Địa chất và Khoáng sản Việt Nam; 10 văn bản, hồ sơ thực tế của Lào Cai (thủy điện Phúc Long, Tu Trên; cao lanh Sơn Mãn; Việt Sơn - Tằng Loỏng; đá hoa Làng Lạnh II; KĐT Mường Hoa).
- Mục tiêu: plugin hoàn thiện được **trọn bộ hồ sơ** cho (A) khai thác cát tại lòng hồ thủy điện, (B) tận thu đá làm VLXD tại bãi thải mỏ apatit.
- **Hai kết luận pháp lý chốt**: (1) không có thủ tục "cấp phép khai thác cát lòng hồ" — chỉ có *nạo vét kết hợp thu hồi cát, sỏi*, hai giai đoạn: chủ sở hữu công trình quyết định chủ trương đầu tư dự án nạo vét (không phải xin giấy phép trong phạm vi bảo vệ đập — Điều 42 NĐ 62/2025, QĐ 628/QĐ-BCT, Điều 14 NĐ 67/2018 sửa bởi NĐ 40/2023) → Chủ tịch UBND tỉnh cấp Giấy xác nhận đăng ký thu hồi (Điều 75, Điều 98 NĐ 193/2025); pháp luật ĐC&KS **không** quy định lập, thẩm định, phê duyệt dự án nạo vét (CV 2419 mục 11). (2) Đất đá thải mỏ, quặng đuôi đi luồng **Điều 97 NĐ 193/2025** (3 tài liệu), khối lượng đã tập kết ở kho, bãi chứa có lối ra tại **khoản 9 Điều 4 Luật 147/2025**.
- Gate phân luồng mới: khoáng sản thu hồi **dùng cho chính dự án** (không phải đăng ký) hay **cung cấp cho dự án khác** (phải đăng ký).
- File mới: `references/16`, `17`, `18`; `mau-van-ban/07`, `08`; `checklists/checklist-ho-so-thu-hoi-khoang-san.md`; thư mục `vi-du-thuc-te/` (10 văn bản + mục lục); 2 văn bản gốc vào `van-ban-goc/`. File sửa: `SKILL.md` (10 nghiệp vụ, GATE B4, cây thư mục), `references/01` (mục IV-bis: 12 văn bản khung của chế định thu hồi).
- Còn thiếu, cần Bạn bổ sung: toàn văn **Phụ lục III TT 36/2025** (6 mẫu), toàn văn **Điều 75, 76 Luật 54/2024**, 4 tệp `.rar` bản vẽ - hồ sơ pháp lý, 2 tệp `.doc` Word 97, số và ngày phát hành chính thức của 2 công văn dự thảo. Chi tiết: `qlks-sct-vn/skills/qlks-sct-vn/CHANGELOG.md`.

## 2026-07-30 — `sd-vlncn-sct-vn` v2026.7.31 + `vbhc-vn` v2.7.1: vụ Thành Hương trọn 3 giai đoạn, bộ khung trình cấp GP, hai bẫy kỹ thuật docx

- Nguồn: hồ sơ **DNTN Thành Hương Nghĩa Lộ** — mỏ đá vôi VLXDTT thôn Bản Hốc, xã Văn Chấn (GP khai thác 2596/GP-UBND ngày 24/12/2014); nộp lại 28/7/2026 sau CV 4280/SCT-CN, bị trả lần 2 ngày 29/7/2026, bổ sung đủ → bộ trình cấp GP 29–30/7/2026.
- **ĐÍNH CHÍNH**: CV 4280/SCT-CN ký ngày **16/7/2026** (GATE bản PDF ký), không phải 22/7 như ghi chú cũ tại ref 07.
- `sd-vlncn-sct-vn` v2026.7.31: ref 07 mục I viết lại 3 giai đoạn (danh mục tồn tại lần 2; kết luận không thuộc diện điểm d k2 Đ38 theo BB thực địa 09/7; số liệu 3-khớp; quy tắc trình bày chốt 30/7); mẫu 01/03/06 trỏ khung mới; **3 khung docx thật bản chốt PTP Trang 30/7** đưa vào `vi-du-thuc-te/` theo chỉ đạo trực tiếp (dự thảo chưa ký/chưa đóng dấu, không chứa số định danh cá nhân): `TTr-cap-GP-Thanh-Huong-29.7.2026.docx`, `Phieu-trinh-cap-GP-Thanh-Huong-29.7.2026.docx`, `GP-du-thao-cap-moi-Thanh-Huong-29.7.2026.docx`.
- `vbhc-vn` v2.7.1: (1) quy tắc **số mũ m³/m² superscript thật** (tách run + vertAlign, rà regex `m[23](?!\d)` toàn văn); (2) mục mới "Sửa file SAU khi QA — hai bẫy đã trả giá": gán `run.text` xóa cả shape `v:line` trong run (vụ mất đường kẻ dưới Độc lập ở dự thảo GP), mọi sửa sau QA PASS phải QA lại; kỹ thuật đối chiếu thể thức bằng pixel với bản ký (GP 2507) và đo đậm/thường bằng tỉ lệ mực cùng dòng.

## 2026-07-30 — `sd-vlncn-sct-vn` v2026.7.30: nguyên tắc trị số nhỏ hơn khi PANM lệch thiết kế (vụ Miền Tây)

- Nguồn: hồ sơ **Công ty cổ phần Miền Tây** — mỏ đá vôi VLXDTT phường Trung Tâm (GP khai thác 121/GP-UBND ngày 21/01/2025), PANM số 01/PANM bản DN nộp lại 20/7/2026, Thuyết minh thiết kế mỏ 151 trang (Bảng 6.4 các thông số khoan nổ mìn) kèm QĐ 05/2025/QĐ-PD ngày 03/9/2025 phê duyệt BCKTKT điều chỉnh, QĐ 799/QĐ-UBND ngày 22/5/2023 chấp thuận chủ trương đầu tư.
- **Nguyên tắc mới (anti-error 20)**: PANM lệch thiết kế về **khối lượng** (thuốc nổ, kíp, dây nổ, thuốc nạp/lỗ) → chốt trị số **NHỎ HƠN**; lệch về **khoảng cách an toàn** (Rc, rs, đá văng) → chốt trị số **LỚN HƠN**. Ba bước rà bắt buộc: kiểm tra chéo tháng × 12 = quý × 4 = năm; tự tính lại công thức của cả PANM và thiết kế (thiết kế đã phê duyệt vẫn sai số học); ràng buộc nội tại cột thuốc × p = thuốc nạp/lỗ, cột bua = Lk − cột thuốc ≥ max(Wct; 20d).
- Trị số đã chốt cho Miền Tây: thuốc nổ 23.540 kg/năm, kíp nổ 3.246 cái/năm, dây nổ 6.818 m/năm, thuốc nạp 19 và 16,7 kg/lỗ, Wct 3,3 m, cột thuốc 2,2/2,0 m, cột bua 3,6/3,8 m, Rc 43,5 m, rs 154,9 m, đá văng 300/225 m.
- File: `skills/sd-vlncn-sct-vn/SKILL.md` (anti-error 20), `references/03-panm.md` (mục G lỗi 14, 15), `references/07-vi-du-thuc-te.md` (mục J + mục D nhận về bài học 12–14 đang lạc, thêm 15–17), CHANGELOG plugin. Bộ 4 văn bản thực tế của vụ việc **không đưa vào repo** (repo public, file chứa dữ liệu cá nhân và doanh nghiệp).

## 2026-07-29 — `bpb-sct-vn` v1.1.0: nạp kho số liệu KT-XH tháng 7/2026 (BC 229-BC/TU)

- Nguồn: **Báo cáo sơ bộ tháng 7/2026 số 229-BC/TU ngày 27/7/2026** của Tỉnh ủy Lào Cai (T/L Ban Thường vụ, Phó CVP Nguyễn Hữu Hải ký). GATE PDF: context hiển thị trống ô số/ngày, số thật đọc bằng `pdftotext -layout` từ file gốc trên đĩa.
- Thêm `references/so-lieu-ktxh-thang-7-2026.md` — kho dữ liệu nền cho bài phát biểu soạn tháng 8–9/2026, 5 khối: (1) **ngành Công Thương**: GTSXCN tháng 7 đạt 6.401 tỷ, lũy kế 40.417,7 tỷ = 51% KH +4,4% CK; khởi công **CCN Phú Thịnh 3** 75 ha >550 tỷ (03 NĐT thứ cấp thuê ~35 ha = 71%); bán lẻ lũy kế 52.550 tỷ = 54,7% KH +9,5%; XNK lũy kế 2.223 triệu USD = 36,2% KH +35,5%; nhiệm vụ tháng 8: bảo đảm nguyên liệu sản xuất, tiết kiệm tối thiểu 10% điện năng; (2) kinh tế chung: thu NSNN 12.989 tỷ = 110% kịch bản +16,8%, giải ngân ĐTC 30%/47,3%, FDI, Hội nghị XTĐT trao 24 dự án >24.160 tỷ; (3) sự kiện neo mở đầu: **Thông báo 381/TB-VPCP ngày 17/7/2026** kết luận của Thủ tướng Lê Minh Hưng, Kỳ họp thứ 3 HĐND (31 NQ), giám sát chuyên đề điện lực của Đoàn ĐBQH; (4) tồn tại: GPMB chậm tại Lao Chải, Chế Tạo, Yên Thành, **Châu Quế** (trùng địa bàn CCN Châu Quế đang thẩm định — cờ lưu ý khi phát biểu), Gia Hội; (5) quy tắc ưu tiên: số người dùng cung cấp luôn thắng số trong kho.
- Cờ dữ liệu: NQ 01/NQ-CP được báo cáo nguồn ghi 2 ngày khác nhau (06/01 và 08/01/2026) — skill yêu cầu kiểm tra lại trước khi dẫn, không tự chọn.
- SKILL.md: Bước 1 (thông số 4) và mục 8 trỏ đến kho số liệu, kèm nguyên tắc số liệu hiện trạng KCN/CCN vẫn phải hỏi Bạn.
- `plugin.json` 1.0.2 → **1.1.0**; `marketplace.json` đồng bộ, `metadata.version` 4.5.4 → **4.5.5**.

## 2026-07-28 (bổ sung) — `vbhc-vn` v2.7.0: thêm mẫu vàng công văn xin ý kiến dự thảo VBQPPL của bộ

- Vụ thật: Bộ Công Thương lấy ý kiến dự thảo Nghị định sửa đổi, bổ sung Nghị định số 181/2024/NĐ-CP (VLNCN, tiền chất thuốc nổ) tại **CV 5633/BCT-ATMT ngày 22/7/2026**; UBND tỉnh giao Sở Công Thương chủ trì tại **VB 7653/UBND-KT ngày 27/7/2026** (hạn gửi Cục Kỹ thuật an toàn và Môi trường công nghiệp trước 01/8/2026).
- Thêm `examples/sct/cong-van-xin-y-kien-du-thao-vbqppl-bo-nganh.docx` — bản Bạn đã chỉnh tay và duyệt: gọn **01 trang**, Kính gửi dạng bảng 2 cột, Nơi nhận rút gọn `- Như trên; - Lưu: VT, CN(tên).`, ký KT. GĐ - PGĐ Hoàng Văn Thuân.
- **Bài học nội dung (chốt 28/7/2026):** khi UBND tỉnh giao Sở chủ trì lấy ý kiến về dự thảo VBQPPL của bộ, phần yêu cầu phải **TỔNG QUÁT như văn bản giao của UBND tỉnh** — nghiên cứu, tham gia ý kiến theo yêu cầu của bộ và các nội dung thuộc phạm vi quản lý nhà nước của cơ quan mình; **KHÔNG liệt kê điều, khoản cụ thể** vì dễ bó hẹp phạm vi góp ý của cơ quan được hỏi.
- GATE PDF: cả 2 văn bản đến đều hiển thị trống ô số/ngày trong context; số thật đọc từ đĩa (`extract_metadata.py`, PDF scan phải OCR trang 1).
- `reference/thu-vien-mau-that.md` thêm dòng bảng mẫu ↔ loại văn bản; SKILL.md cập nhật 17 → **21 mẫu thật** (`examples/sct/` 15 + `examples/ubnd/` 6).
- `plugin.json` 2.6.0 → **2.7.0**; `marketplace.json` đồng bộ, `metadata.version` 4.5.2 → **4.5.3**.

## 2026-07-28 (bổ sung) — `kccn-sct-vn` v1.12.0: hồ sơ pháp lý gốc CCN Thống Nhất 1, sửa lỗi TMĐT 485 tỷ → 860 tỷ

- Nguồn: 04 PDF bản scan có dấu do Bạn cung cấp. GATE file gốc trên đĩa: 3/4 file không có lớp text, phải render ảnh soi từng trang để lấy số, ngày, người ký.
- **QĐ 298/QĐ-UBND ngày 20/02/2025** (Chủ tịch Trịnh Xuân Trường) thành lập CCN Thống Nhất 1, 74,95 ha, CĐT Công ty CP Đầu tư phát triển Công nghiệp Lào Cai, **TMĐT 860.008.000.000 đồng**.
- **QĐ 630/QĐ-UBND ngày 06/3/2025** chấp thuận CTĐT đồng thời chấp thuận nhà đầu tư — CCN sinh thái, hoạt động đến 01/11/2073, ràng buộc khu vực dự trữ khoáng sản quốc gia, 27 mốc tọa độ VN2000 (múi 3 và múi 6).
- **QĐ 1311/QĐ-UBND ngày 23/6/2025 của UBND thành phố Lào Cai** (Chủ tịch Nguyễn Quốc Huy) phê duyệt QHCT 1/500 — bảng sử dụng đất 749.504,1 m², XLNT 3.000 m³/ngđ, lao động 3.747 người.
- **QĐ 1955/QĐ-UBND ngày 19/6/2025** đường IC18 – CCN Thống Nhất 1 (2,6 km, 4 làn, nhóm B, 210.000 triệu) — **chốt dứt điểm ngày 19/6/2025**, đóng cờ đỏ nêu từ v1.9.0.
- **Sửa lỗi:** con số 485 tỷ đồng trong case study khởi công (reference 08) và ví dụ thực tế là SAI → thay bằng 860.008 triệu đồng. Chuẩn hoá cách dùng 74,95 ha (pháp lý) / 75 ha (quy hoạch) / 74,97 ha (GPMB).
- Thêm `references/23-ccn-thong-nhat-1-ho-so-goc.md`; SKILL.md thêm nghiệp vụ 11 và dòng bảng tra, description rút còn 984 ký tự.
- `plugin.json` 1.11.0 → **1.12.0**; `marketplace.json` đồng bộ, `metadata.version` 4.5.1 → **4.5.2**.

## 2026-07-28 (bổ sung) — `attp-sct-vn` v1.1.0: nạp bộ hồ sơ thực tế + văn bản của tỉnh

- Nguồn: 02 archive **ATTP** và **Thuốc lá** do Bạn cung cấp (56 + 20 file, gồm VBQPPL, văn bản của UBND tỉnh, biểu mẫu, hồ sơ đã xử lý).
- **QĐ 28/2025/QĐ-UBND ngày 10/11/2025** (hiệu lực 20/11/2025) phân cấp QLNN về ATTP tỉnh Lào Cai, thay QĐ 08/2021/QĐ-UBND (Yên Bái) và QĐ 45/2024/QĐ-UBND (Lào Cai) → reference 01 viết mới: 6 nguyên tắc phân cấp, Điều 6 (Sở Công Thương), Điều 7 (cấp xã — hộ kinh doanh thuộc xã, không thuộc Sở).
- Chuỗi thẩm quyền cấp GCN ATTP 3 tầng → reference 02 viết mới: NĐ 146/2025 khoản 5 Điều 37 + điểm ii Mục 3 Phần VII Phụ lục XI; TT 38/2025 khoản 2 Điều 16 sửa khoản 2 Điều 6 TT 43/2018; **QĐ 904/QĐ-UBND ngày 26/8/2025** ủy quyền GĐ Sở lập Đoàn thẩm định.
- **GATE mới:** QĐ 904/QĐ-UBND ủy quyền **chỉ đến hết 31/12/2025** → skill cấm viện dẫn như còn hiệu lực, bắt buộc hỏi Bạn về QĐ thay thế năm 2026 trước khi soạn Quyết định thành lập Đoàn thẩm định.
- reference 03, 04, 05, 07 viết mới (tự công bố, miễn cấp GCN và bản cam kết, hậu kiểm - xử phạt, rượu bia); reference 06 bổ sung TT 57/2018, TT 43/2023, mẫu QĐ Đoàn thẩm định, 3 lỗi hợp đồng ủy thác theo CV 2534/SCT-CN ngày 17/11/2025.
- Thêm 05 biểu mẫu thật, 02 bộ ví dụ thực tế (Siêu thị An Lạc — cấp GCN ATTP 9/2025; Kim Ngọc — thuốc lá 2025), 06 văn bản gốc.
- `plugin.json` 1.0.0 → **1.1.0**; `marketplace.json` entry đồng bộ, `metadata.version` 4.5.0 → **4.5.1**.

## 2026-07-28 — plugin mới `attp-sct-vn` v1.0.0 + marketplace v4.5.0

- Khởi tạo plugin thứ 19: **an toàn thực phẩm và công nghiệp tiêu dùng - thực phẩm** (GCN cơ sở đủ điều kiện ATTP, tự công bố sản phẩm, hậu kiểm; thuốc lá; rượu, bia, nước giải khát, sữa chế biến, dầu thực vật, bánh kẹo).
- **GATE HIỆU LỰC ATTP** (reference 08): NĐ 46/2026/NĐ-CP ngày 26/01/2026 đang **tạm ngưng hiệu lực** theo NQ 09/2026/NQ-CP ngày 04/02/2026, sau đó là **NQ 15/2026/NQ-CP ngày 06/4/2026**, cho đến khi Luật ATTP (sửa đổi) và nghị định hướng dẫn có hiệu lực; trong thời gian này **NĐ 15/2018/NĐ-CP tiếp tục áp dụng**. Skill mặc định dẫn NĐ 15/2018, cấm dẫn NĐ 46/2026.
- **Đính chính quan trọng** (reference 06): thẩm quyền cấp, cấp lại, cấp sửa đổi bổ sung, thu hồi **Giấy phép chế biến nguyên liệu thuốc lá** đã phân cấp từ Bộ Công Thương **về UBND cấp tỉnh** theo **khoản 5 Điều 18 NĐ 146/2025/NĐ-CP** (hiệu lực 01/7/2025, trình tự thủ tục tại Phụ lục V) — sửa nhận định sai trước đó cho rằng thẩm quyền vẫn thuộc Bộ. Bài học rà thẩm quyền: phải soát **đủ 03 nguồn** NĐ 146/2025 (và NĐ 139/2025), NQ 19/2026, NQ 66.18/2026, không dừng ở hai Nghị quyết.
- Điều kiện cấp Giấy phép chế biến nguyên liệu thuốc lá cắt giảm còn **02** theo Phụ lục II phần B NQ 19/2026; Giấy phép mua bán nguyên liệu thuốc lá và GCN đủ điều kiện đầu tư trồng cây thuốc lá đã bãi bỏ điều kiện.
- references 01, 02, 03, 04, 05, 07 dựng khung, chờ file mẫu, hồ sơ thực tế và Quyết định công bố TTHC để hoàn thiện ở v1.1.0.
- `marketplace.json`: thêm entry `attp-sct-vn` 1.0.0, `metadata.version` 4.4.0 → **4.5.0**, mô tả 18 → 19 plugin; `sync_marketplace.py --check` đã khớp.

## 2026-07-27 (bổ sung) — marketplace v4.4.0: đồng bộ lại entry lệch + chốt cơ chế cập nhật

- **Lỗi:** 04 entry trong `.claude-plugin/marketplace.json` bị bỏ quên khi nâng cấp plugin, nên catalog phát cho claude.ai vẫn là bản cũ: `dacn-sct-vn` 1.2.0→**1.3.0**, `kccn-sct-vn` 1.9.0→**1.11.0**, `qlks-sct-vn` 1.3.1→**1.4.0**, `quy-hoach-ct-vn` 1.0.2→**1.1.0** (cả `description` cũng lệch). Nguyên nhân: các commit ngày 26-27/7 chỉ sửa `plugin.json` mà không chạm `marketplace.json`.
- Thêm `scripts/sync_marketplace.py`: tái tạo mảng `plugins` từ 18 file `plugin.json` (giữ nguyên `source` và thứ tự), có cờ `--check` để chỉ kiểm tra.
- Thêm `.github/workflows/marketplace-sync.yml`: mỗi lần push/PR sẽ chạy `--check`, lệch là fail — không còn tái diễn lỗi quên đồng bộ.
- `metadata.version` 4.3.0 → **4.4.0**.
- Ghi chú vận hành: Claude Code phân giải version theo thứ tự `plugin.json` → entry marketplace → commit SHA; và marketplace bên thứ ba **mặc định TẮT auto-update**, phải bật hoặc refresh thủ công thì bản mới mới về máy.

## 2026-07-27 — sd-vlncn-sct-vn v2026.7.27.1

- Thêm bộ ví dụ thực tế trọn gói vụ Công ty CP Miền Tây (mỏ đá vôi lộ thiên phường Trung Tâm, nhà dân 230 m < Rđv 300 m): Phiếu trình thẩm định kèm Phụ lục bảng đánh giá 19 hàng, Tờ trình, dự thảo QĐ phê duyệt PANM + chấp thuận sử dụng VLNCN, PANM bản Sở hiệu chỉnh — bộ mẫu ưu tiên cho trường hợp mỏ lộ thiên (Si Ma Cai giữ vai trò mẫu nổ hầm).
- Bài học đã duyệt cập nhật vào ref 07 + mẫu 06/07/11: Tờ trình trình UBND tỉnh do GIÁM ĐỐC ký trực tiếp, nơi nhận "Ban GĐ Sở"; dự thảo QĐ ghi "Sở Công Thương" không kèm "tỉnh Lào Cai", header điền sẵn tháng/năm; quy tắc nhãn đậm - nội dung thường; cảnh báo lỗi gốc mẫu Si Ma Cai (ngày Luật 42, hai Điều 3 trùng).
- SKILL.md ghi rõ người ký Tờ trình; plugin.json cập nhật 30 ví dụ thực tế.

## 2026-07-27 — `hnh-sct-vn` v1.6.0: cột "Khối lượng vận chuyển" theo dạng chứa hàng + soát chéo nhiều Giấy phép cùng đợt

- Nguồn: vụ **Công ty TNHH MTV thương mại Tiến Anh** (MSDN 5300804272), 02 bộ hồ sơ cùng đợt 7/2026 — LPG loại 2 (UN 1075) đi ở **dạng chai chứa 12 kg và 48 kg** trên xe ô tô tải có mui 24C-055.24; xăng UN 1203 + dầu diesel UN 1202 loại 3 trên tổ hợp đầu kéo 24C-047.97 kéo sơ mi rơ moóc xi téc 24R-004.50. Toàn bộ số liệu đối chiếu từ hồ sơ gốc (Giấy đề nghị, Bảng kê phương tiện, Bảng kê lái xe - áp tải, Phương án, GCN ĐKDN, GCN kiểm định, Chứng nhận đăng ký xe, GPKDVT, 02 GCN tập huấn).
- **Nguyên tắc 18 mới:** cột "Khối lượng vận chuyển" của Danh mục kèm Giấy phép chọn theo DẠNG CHỨA HÀNG, không copy máy móc "Theo thiết kế của phương tiện" từ mẫu xi téc. Cách ghi chốt cho mọi Giấy phép: **"Theo giấy tờ của phương tiện"**.
- **Nguyên tắc 19 mới:** một doanh nghiệp nộp nhiều bộ hồ sơ thì soát chéo 04 tiêu chí giữa các Giấy phép (cột khối lượng; cỡ chữ dòng "(Kèm theo Giấy phép...)" kế thừa 14pt; cấu trúc cột Ghi chú; thời hạn) và render soi hai bản cạnh nhau.
- Reference 16 thêm **mục 8** (8.1 dạng chai chứa, 8.2 soát chéo cùng đợt, 8.3 đọc niên hạn từ 03 nguồn, 8.4 sai lệch nhỏ chỉ ghi Biên bản, 8.5 cột loại/nhóm hàng); reference 11 thêm **lỗi 13-16**; reference 10 thêm cảnh báo phân biệt cột (4) "Loại, nhóm hàng" với cột (5) "Nhãn hiệu, biểu trưng".
- Ví dụ thực tế mới `vi-du-thuc-te/tien-anh-lpg-xangdau-072026/` (02 Giấy phép bản chốt + README); bổ sung tiền lệ vào bảng reference 16 mục 1 và mô tả thư mục vào SKILL.md mục IV-a.
- `plugin.json` 1.5.2 → **1.6.0**; `marketplace.json` entry `hnh-sct-vn` → 1.6.0, `metadata.version` 4.1.0 → **4.2.0**.

## 2026-07-26 — `dacn-sct-vn` v1.2.0: nạp mảng KCN và Khu kinh tế cửa khẩu vùng Lào Cai cũ

- Nguồn: **Kế hoạch 72/KH-BQL ngày 08/7/2026** của Ban Quản lý Khu kinh tế tỉnh Lào Cai (Trưởng ban Vương Trinh Quốc) về Phát triển KTXH năm 2027, kèm biểu **Dự tính giá trị SXCN năm 2027**; ban hành theo Văn bản 6607/UBND-TH ngày 27/6/2026 của UBND tỉnh; nơi nhận có Sở Công Thương. Metadata trích từ PDF gốc bằng `extract_metadata.py`.
- Thêm reference `08-kcn-kkt-bql-khu-kinh-te.md` và dữ liệu `du-lieu/gtsxcn-kcn-kkt-2027.json` (**04 khu vực, 37 cơ sở, 85 dòng sản phẩm; tổng 26.301.347 triệu đồng**, đã đối chiếu khớp bản gốc, lệch 1 triệu do làm tròn Excel).
- Ghi rõ **05 mâu thuẫn số liệu trong chính Kế hoạch 72** để rà trước khi tổng hợp — quan trọng nhất: mục tiêu GTSXCN 2027 (26.000 tỷ) **thấp hơn ước thực hiện 2026 (28.000 tỷ)** khoảng 7,1%, có thể xung đột với chỉ tiêu IIP >12% của NQ 169.
- `SKILL.md`: thêm nghiệp vụ (7); thay ghi chú phạm vi bằng **bảng hai địa bàn - hai Ban** (Ban Quản lý Khu kinh tế tỉnh cho vùng Lào Cai cũ ≠ Ban Quản lý các Khu công nghiệp tỉnh cho vùng Yên Bái cũ), thêm nguyên tắc bất biến "không gộp nhầm hai Ban".
- `plugin.json` 1.1.2 → **1.2.0**; `marketplace.json` cập nhật entry `dacn-sct-vn` (tái tạo từ plugin.json, không sửa tay entry khác), `metadata.version` 4.0.0 → **4.1.0**.

## 2026-07-26 (bổ sung) — `sd-vlncn-sct-vn` v2026.7.26.1: sửa ranh giới trách nhiệm thẩm định

- Hồ sơ đầy đủ thì **Sở Công Thương tự thẩm định, tự kết luận** (k6 Đ39 Luật 42/2024), kể cả kết luận đủ/chưa đủ các bước thiết kế mỏ — không hỏi Sở Xây dựng. Thiếu bước → trả lại hồ sơ, chỉ địa chỉ cơ quan thẩm định để **doanh nghiệp** tự liên hệ, đúng nguyên văn CV 473/VPUBND-KT.
- Reference 09 thêm mục F (bảng ranh giới việc của Sở / DN / sở khác); SKILL.md thêm anti-error 19; sửa reference 02 (C3, D.3, D.11), reference 07 (D.1, D.11), mẫu 08 (khối phạm vi dùng mẫu).

## 2026-07-26 — `sd-vlncn-sct-vn` v2026.7.26: chống bị UBND tỉnh trả lại hồ sơ cấp phép VLNCN

- Nguồn: 3 văn bản trả hồ sơ quý III–IV/2025 do Bạn cung cấp, đã trích metadata từ PDF gốc: **2373/UBND-KT 23/9/2025**, **473/VPUBND-KT 07/10/2025**, **565/VPUBND-KT 23/10/2025**.
- Thêm reference `09-cong-gac-ubnd-tra-ho-so.md` (ba câu hỏi gác cổng, bảng tự kiểm 12 điểm, quy trình 5 bước sau khi bị trả) và mẫu `20-bang-tu-kiem-truoc-khi-trinh-ubnd.md`.
- Checklist thẩm định thêm nhóm **C2b — pháp lý đất đai, mặt bằng**; SKILL.md thêm anti-error 16–18; reference 02 thêm lỗi D.10–D.12; reference 07 thêm 3 ví dụ thực tế và bài học D.8–D.10; mẫu 06 thêm mục đất đai và mục tự kiểm.
- `plugin.json` 2026.7.24 → **2026.7.26**; `marketplace.json` cập nhật version + description entry `sd-vlncn-sct-vn` (tái tạo từ plugin.json, không sửa tay các entry khác).

## 2026-07-25 (tối) — Hủy phương án tách đôi, gộp về MỘT marketplace: `marketplace.json` v4.0.0 đủ 18 plugin

- **Lý do:** vận hành song song hai marketplace (`skill-sct` 12 plugin + `skill-sct-2` 6 plugin) gây rối khi quản lý — hai nơi cập nhật, dễ lệch phiên bản, đã phát sinh tình trạng plugin trùng tên giữa bản cài từ marketplace và bản upload tay. Quyết định quay về một đầu mối duy nhất.
- `marketplace.json` v4.0.0: tái tạo TỰ ĐỘNG toàn bộ mảng `plugins` từ 18 file `<thư mục>/.claude-plugin/plugin.json` (đúng quy tắc "không sửa tay entry"). 12 entry cũ giữ nguyên version, thêm lại 6 entry: `bpb-sct-vn` 1.0.2, `dacn-sct-vn` 1.1.2, `pccc-sct-vn` 1.1.2, `quy-hoach-ct-vn` 1.0.2, `sct-laocai-org-vn` 2.0.3, `vbhc-pdf-reader-vn` 2.0.2.
- Không phải copy file nào: 6 thư mục plugin vẫn nằm sẵn trong repo này từ lần tách và đã đối chiếu `diff -rq` với `skill-sct-2` — **giống hệt từng byte**, không có thay đổi nội dung ở repo kia cần mang về.
- Đã chạy `claude plugin validate --strict` cho marketplace và cả 18 plugin: pass toàn bộ.
- **Repo `skill-sct-2` ngừng sử dụng**, sẽ xóa trên GitHub; marketplace `skill-sct-2` trên claude.ai gỡ bỏ. Từ nay mọi cập nhật 18 plugin CHỈ làm tại repo này.
- **Bước bắt buộc trên claude.ai sau khi gộp:** Remove → Add lại marketplace `skill-sct` (marketplace đã cài không nạp entry mới). Nếu Add lại vẫn thiếu 6 plugin, dùng Local uploads cho 6 plugin đó — hạn chế đã biết của claude.ai, không phải lỗi repo.
- Quy tắc "mỗi marketplace giữ ≤ 12 plugin" đặt ra buổi chiều nay bị bãi bỏ theo quyết định gộp.

## 2026-07-25 (chiều) — Tách 2 marketplace: skill-sct v3.0.0 giữ 12 plugin đang chạy, skill-sct-2 nhận 6 plugin chưa vào được

- **Nguyên nhân chốt hạ sau chuỗi chẩn đoán:** marketplace đã cài trên claude.ai chỉ cập nhật nội dung các plugin có sẵn từ lần Add đầu tiên, KHÔNG nạp entry mới thêm vào sau. Bằng chứng: 12 plugin gốc (bvmt, hc, hl, hnh, kccn, kho, qlks, sd, tkm, vbhc, xd, xp) luôn hiện và nhận cập nhật nội dung; 6 plugin bổ sung sau (bpb, dacn, pccc, quy-hoach-ct, sct-laocai-org, vbhc-pdf-reader) không bao giờ xuất hiện dù đã: đủ 18 entry hợp lệ (v2.0.0), nâng version 2 nhịp (v2.0.1-2.0.2), đảo lên đầu danh sách (v2.0.3), gỡ skill tải tay trùng tên, Remove → Add lại marketplace. Các giả thuyết description >500, đường dẫn ngoài ASCII đã loại trừ bằng số liệu.
- `marketplace.json` v3.0.0: giữ đúng 12 plugin đang chạy. 6 plugin chưa vào được chuyển sang repo mới **`skill-sct-2`** (marketplace riêng, Add mới nạp trọn danh sách; nội dung nguyên trạng commit `db67f45`).
- Thư mục 6 plugin tạm GIỮ trong repo này (không còn trong marketplace.json nên không ảnh hưởng) — xóa bằng commit dọn dẹp sau khi skill-sct-2 xác nhận chạy ổn; từ đó mọi cập nhật 6 plugin này CHỈ làm ở skill-sct-2.
- Quy tắc mới: plugin MỚI thêm vào marketplace nào phải Remove → Add lại marketplace đó trên claude.ai; mỗi marketplace giữ ≤ 12 plugin.
## 2026-07-25 — marketplace.json v2.0.0: đồng bộ đủ 18 plugin, khớp version tuyệt đối

- **Nguyên nhân marketplace trên claude.ai thiếu plugin:** claude.ai chỉ đọc `.claude-plugin/marketplace.json`, không tự quét thư mục. File này mới liệt kê 12/18 plugin (thiếu `bpb-sct-vn`, `dacn-sct-vn`, `pccc-sct-vn`, `quy-hoach-ct-vn`, `sct-laocai-org-vn`, `vbhc-pdf-reader-vn`) và lệch version 5 entry (`hnh` 1.3.0≠1.5.2, `kccn` 1.6.0≠1.9.0, `qlks` 1.1.0≠1.3.1, `tkm` 1.2.0≠1.3.1, `vbhc` 2.2.0≠2.6.0).
- **Sửa:** tái tạo toàn bộ mảng `plugins` TỰ ĐỘNG từ `<thư mục>/.claude-plugin/plugin.json` của cả 18 plugin — name/source/description/version lấy nguyên gốc, không gõ tay. Đã validate: 18/18 plugin.json hợp lệ, description ≤ 500; 18/18 SKILL.md description ≤ 1024 (bpb dùng YAML gấp dòng `>-`, 1016 ký tự); name khớp tên thư mục.
- **Quy tắc mới (chống tái diễn):** mỗi lần nâng version một plugin phải chạy lại khối lệnh đồng bộ marketplace (xem mục validate trong README) hoặc yêu cầu Claude "đồng bộ marketplace.json" trước khi push; entry marketplace KHÔNG bao giờ sửa tay.

## 2026-07-25 (bổ sung 3) — kccn-sct-vn v1.9.0: ref 19 qua GATE, phát hiện 3 nội dung gán sai cho NQ 34

Bạn cung cấp bản gốc NQ 34-NQ/TU và KH 134/KH-UBND — ref 19 nay đã qua GATE, hoàn tất cả 3 reference merge hôm nay.

**Lỗi nặng nhất:** bản chưng cất cũ gán cho NQ 34 ba mục tiêu *"45,3% GRDP năm 2030"*, *"tăng trưởng GRDP 11%/năm"*, *"tỉnh phát triển khá vùng Trung du và Miền núi phía Bắc"*. Rà toàn văn 5 trang: **không có cụm nào trong số đó xuất hiện**. NQ 34 chỉ nói "tăng trưởng kinh tế trên 10% năm 2026". Nhiều khả năng thuộc Đề án 08 hoặc NQ Đại hội Đảng bộ tỉnh. Đã loại bỏ.

**Bẫy đọc file:** số và ngày của KH 134 hiển thị TRỐNG khi nạp PDF vào context, phải đọc từ đĩa mới ra "Số: 134/KH-UBND — ngày 26/3/2026". Đúng kịch bản `vbhc-pdf-reader-vn`. Tên file "trình ký ngày 24/3/2026" là ngày trình ký, không phải ngày ban hành.

**Cờ đỏ trong bản gốc:** KH 134 ban hành 26/3/2026 nhưng viện dẫn QĐ 1955/QĐ-UBND "ngày 19/6/2026" — sau 3 tháng, nghi lỗi đánh máy, không viện dẫn cho tới khi tra được bản gốc.

**Bổ sung:** 07 mục tiêu NQ 34 đầy đủ (bản cũ thiếu chỉ tiêu 06 KCN + 20 CCN đang hoạt động và tỷ lệ lấp đầy KCN >70%/CCN 60-70%); vốn KH 134 khái toán 7.080 tỷ (NSNN 1.280 + DN 5.800); 10 đầu mối, SCT là cơ quan thường trực; phân biệt 2 mốc báo cáo ngày 20 và ngày 25.

Người ký đã xác nhận: NQ 34 — PBT Thường trực **Hoàng Giang**; KH 134 — PCT **Nguyễn Thế Phước**.

## 2026-07-25 (bổ sung 2) — kccn-sct-vn v1.8.0: merge 03 reference tồn đọng, kiểm chứng bản gốc

Hoàn tất mục "cân nhắc merge đợt sau" tồn từ v1.0 của `kccn-sct-vn`. Ba reference cuối của skill `kcn-ccn-vn` (đã xoá sáng nay) nay vào plugin dưới dạng **references/19, 20, 21** — nhưng **đối chiếu bản gốc trước khi merge**, không bê nguyên.

**Kết quả kiểm chứng — 3 lỗi thật trong bản cũ:**

| Lỗi | Bản cũ | Bản gốc |
|---|---|---|
| NQ 26 — mục tiêu tăng trưởng | "từ **107%** trở lên" (lỗi OCR) | **"từ 10% trở lên"** |
| QĐ 425 — phạm vi chi phí | Gộp chung KCN và CCN | Khác nhau: trạm XLNT nằm trong chi phí xây dựng của KCN, KHÔNG của CCN |
| QĐ 425 — chi phí chưa tính | Liệt kê 4 khoản, có GPMB | Đúng **03 khoản**, KHÔNG có GPMB |

**Bổ sung mới:** phụ lục NQ 26 (thành lập mới 03 KCN Y Can, Đông An, Bản Qua hạn 12/2026 — bản cũ bỏ hoàn toàn); điều kiện dùng Bảng 51 theo NĐ 49/2026/NĐ-CP khi UBND tỉnh chưa công bố suất vốn riêng; mã hiệu 13300.01-08 và cơ cấu chi phí xây dựng/thiết bị.

**Phát hiện chéo:** chỉ tiêu KCN có XLNT tập trung — KH 134 đặt **100%**, NQ 26 đặt **41,7%**; đã ghi cảnh báo chéo ở cả 3 reference để không bị trộn khi soạn báo cáo.

**Còn treo:** ref 19 (NQ 34/KH 134) chưa qua GATE vì chưa có bản gốc trong `van-ban-goc/` — đã ghi banner cảnh báo đầu file.

Văn bản gốc bổ sung: NQ 26 bản scan nén 44 MB → 8,7 MB + bản OCR toàn văn; QĐ 425/QĐ-BXD.

## 2026-07-25 (bổ sung) — Xoá thư mục `kcn-ccn-vn` (bản cũ đã được thay bằng `kccn-sct-vn`)

Sau khi đối chiếu nội dung, xoá `kcn-ccn-vn/` khỏi nhánh main. Đây là thư mục duy nhất còn ở dạng skill cũ; **repo nay 100% là plugin (18 plugin)**.

**Căn cứ xoá:**
- `kccn-sct-vn` đã kế thừa và mở rộng toàn bộ nghiệp vụ: 18 reference (so với 18 bản cũ nhưng viết lại theo NĐ 32/2024 + NĐ 139/2025 + NĐ 178/2026), thêm 6 bộ mẫu văn bản, 13 văn bản gốc, thư mục ví dụ thực tế (21 MB so với 344 KB).
- **Bản cũ chứa dữ liệu đã lỗi thời, là bẫy trích dẫn sai:** bảng suất vốn (ref 13) lập theo QĐ 409/QĐ-BXD 2025 trong khi đã có **QĐ 425/QĐ-BXD ngày 30/3/2026** thay thế; `15-hien-trang-ccn-bao-cao-18-6-2026.md` và `18-hien-trang-cap-nhat.md` là số liệu hiện trạng — thuộc loại đã chốt nguyên tắc KHÔNG tra trong skill vì dễ lỗi thời.
- Trùng trigger với `kccn-sct-vn` nếu vô tình cài song song, vi phạm nguyên tắc single source of truth.
- Nhu cầu "tra lịch sử" đã được git phục vụ đầy đủ, không cần giữ thư mục sống.

**Khôi phục bất cứ lúc nào** — toàn bộ 23 file nằm tại commit `07dd33e` (02/7/2026):

```bash
git show 07dd33e --stat                                    # xem danh sách file
git show 07dd33e:kcn-ccn-vn/references/14-nq26-nhiem-vu-2026.md   # đọc 1 file
git checkout 07dd33e -- kcn-ccn-vn                         # phục hồi cả thư mục
```

Ba reference `kccn-sct-vn` từng hoãn merge (11 NQ 34/KH 134, 13 suất vốn chi tiết, 14 NQ 26) đã được ghi lệnh lấy lại kèm cảnh báo rà số liệu vào `kccn-sct-vn/skills/kccn-sct-vn/CHANGELOG.md`.

## 2026-07-25 — Chuyển 5 skill cuối cùng sang chuẩn plugin + sửa lỗi description > 500 ký tự

**Hoàn tất chuyển đổi:** từ nay 100% skill trong repo (18 plugin) đều theo chuẩn `.claude-plugin/plugin.json` + `skills/<tên>/`, không còn thư mục để SKILL.md ở gốc.

- **`bpb-sct-vn` v1.0.0 (MỚI trên repo)** — soạn bài phát biểu, tham luận, diễn văn cho lãnh đạo Sở; kèm 2 references, 11 bài mẫu gốc (`kho-bai-mau/`) và `scripts/build_bpb.py`. Bản đang cài đặt để `plugin.json` **sai vị trí** (ở gốc thư mục skill thay vì `.claude-plugin/`) — đã đặt lại đúng chỗ khi đóng gói.
- **`pccc-sct-vn` v1.1.0** — chuyển sang cấu trúc plugin. **Giữ nguyên bản trên repo** (mới hơn bản đang cài ngày 14/5/2026): đã có `references/15-giai-phap-ky-thuat-qd1074-bxd.md`, cập nhật QĐ 1074/QĐ-BXD 29/6/2026, QĐ 1609/QĐ-BCT 01/7/2026, CV 7432/UBND-XD 21/7/2026 và 3 văn bản gốc trong `van-ban-goc/`. **Không ghi đè ngược bằng bản cài cũ.**
- **`quy-hoach-ct-vn` v1.0.0**, **`sct-laocai-org-vn` v2.0.1**, **`vbhc-pdf-reader-vn` v2.0.0** — chuyển cấu trúc, nội dung giống hệt bản đang cài (đối chiếu checksum MD5 từng file, khớp 100%). Số hiệu phiên bản lấy theo phiên bản nội bộ khai báo trong SKILL.md.
- Toàn bộ chuyển đổi dùng `git mv` nên **giữ nguyên lịch sử commit** của từng file.

**Sửa lỗi hàng loạt — `description` trong `plugin.json` vượt 500 ký tự:** rà toàn repo phát hiện **8/18 plugin vi phạm** giới hạn riêng của `plugin.json` (xem quy tắc validate số 0 trong README, lỗi thật ngày 14/7/2026 khi upload tkm-sct-vn). Các plugin này sẽ bị Claude từ chối nếu upload lại. Đã rút gọn toàn bộ về 382-441 ký tự, giữ nguyên từ khoá nhận diện:

| Plugin | Trước | Sau | Phiên bản |
|---|---|---|---|
| `quy-hoach-ct-vn` | 743 | 414 | 1.0.0 |
| `pccc-sct-vn` | 738 | 409 | 1.1.0 |
| `qlks-sct-vn` | 733 | 441 | 1.3.0 → **1.3.1** |
| `sct-laocai-org-vn` | 717 | 401 | 2.0.1 |
| `vbhc-pdf-reader-vn` | 703 | 413 | 2.0.0 |
| `bpb-sct-vn` | 699 | 382 | 1.0.0 |
| `tkm-sct-vn` | 589 | 403 | 1.3.0 → **1.3.1** |
| `hnh-sct-vn` | 543 | 411 | 1.5.1 → **1.5.2** |

`description` trong frontmatter SKILL.md giữ nguyên (giới hạn 1024, cao nhất là kccn-sct-vn 1021 — vẫn hợp lệ).

**Còn lại:** thư mục `kcn-ccn-vn` vẫn ở dạng skill cũ — đây là bản **đã được nâng cấp thành `kccn-sct-vn`**, giữ lại chỉ để tra lịch sử, KHÔNG chuyển thành plugin và KHÔNG cài song song (trùng trigger với kccn-sct-vn).

## 2026-07-24 (bổ sung) — hnh-sct-vn v1.5.1: Mẫu 6 Biên bản thẩm định hồ sơ cấp Giấy phép

- Thêm **`mau-ho-so/Mau 6 - Bien ban tham dinh ho so cap Giay phep (noi bo So).docx`** — bản chuẩn văn phong 24/7/2026 dựng từ vụ NH3 khan (Công ty CP thương mại vận tải và tư vấn kỹ thuật, 05 tổ hợp xe biển Việt Nam), đã lược các phát hiện tồn tại riêng của vụ việc để dùng làm mẫu chung cho mọi vụ thẩm định HHNH.
- Cập nhật danh mục biểu mẫu (`00-huong-dan-lap-ho-so.md`), SKILL.md mục IV, CHANGELOG plugin, `plugin.json` v1.5.1.

## 2026-07-24 — Nâng cấp cụm VLNCN theo NĐ 275/2026/NĐ-CP + plugin xử phạt dùng chung mới

**Nguồn:** Nghị định **275/2026/NĐ-CP ngày 08/7/2026** quy định xử phạt VPHC lĩnh vực hóa chất và VLNCN — **hiệu lực 25/8/2026, thay thế NĐ 71/2019/NĐ-CP + Điều 1 NĐ 17/2022/NĐ-CP** (Đ75); chuyển tiếp Đ74 (hành vi kết thúc trước 25/8/2026 vẫn theo NĐ cũ).

- **`xp-hc-vlncn-sct-vn` v1.0.0 (MỚI)** — plugin chế tài dùng chung 2 lĩnh vực: SKILL.md (bản đồ nghị định, quy tắc mức phạt Đ4, chọn nghị định theo thời điểm, thẩm quyền nhanh, quy trình xử phạt, ranh giới hình sự Đ6); 5 references (quy định chung + chuyển tiếp; bảng VLNCN Đ53–61 đầy đủ; bản đồ hóa chất Đ7–52 + Đ25/Đ34; thẩm quyền Đ62–73 + ví dụ tính; đối chiếu NĐ 71/2019 → 275/2026 với quy luật +4); van-ban-goc kèm toàn văn NĐ 275/2026 (bản Word).
- **`sd-vlncn-sct-vn` [2026.7.24]** — ref 05 chuyển bảng sang Đ60 (thêm điểm mới 3d, 4b), thẩm quyền mới (**GĐ SCT đích danh k1 Đ63: 80 tr/cá nhân VLNCN**), câu viện dẫn 2 thời kỳ; SKILL.md mục 10 + anti-error 9 + ranh giới; ref 01/03, mẫu 13/18, INDEX.
- **`hl-vlncn-sct-vn` v1.1.0** — hành vi nhân lực Đ50 cũ → **Đ54 mới** (15–30 tr + đình chỉ 3–6 tháng); SKILL.md, ref 01/06, mẫu 12, INDEX.
- **`kho-vlncn-sct-vn` v1.5.0** — nhóm bảo quản kho Đ53 cũ → **Đ57 mới** (kho không đạt 50–70 tr + đình chỉ 6–12 tháng; để mất VLNCN 80–100 tr); làm rõ ranh giới PANM/GP sử dụng: `sd-vlncn-sct-vn` CHỦ TRÌ.
- **`hc-sct-vn` v1.2.0** — nhóm hóa chất viết lại theo Luật 69/2025 (Đ25 CSDL thay Đ29 cũ — không báo cáo năm 30–40 tr/tổ chức, tăng ~3 lần; Đ34 huấn luyện ATHC thay Đ11 cũ); cập nhật SKILL.md, ref 07/10/11/15/16.
- Quyết định kiến trúc: **GIỮ 3 plugin nghiệp vụ VLNCN riêng** (hl/kho/sd — trigger chính xác, tiết kiệm context), phần trùng lặp (chế tài xử phạt) hợp nhất vào plugin dùng chung; NĐ 71/2019 giữ trong van-ban-goc phục vụ vụ giao thời.

## 2026-07-24 (bổ sung) — vbhc-vn v2.4.0: Quy tắc 20 — cấm chiều cao dòng cố định `<w:trHeight>` trong bảng nội dung

- **Vụ thật:** Biên bản thẩm định hồ sơ cấp Giấy phép vận chuyển HHNH loại 2 (Công ty CP thương mại vận tải và tư vấn kỹ thuật, 24/7/2026) — trang 4 kết bằng đề mục `- Lái xe:` rồi bỏ trắng gần nửa trang, bảng lái xe nhảy nguyên khối sang trang 5. Không hề có paragraph trống: thủ phạm là `<w:trHeight>` gán cứng từng dòng (1623 và 2002 twip) cộng `<w:cantSplit/>` → cụm "dòng tiêu đề + dòng dữ liệu đầu" cao ~7 cm, vượt phần giấy còn lại.
- **Quy tắc 20 (mới):** Chế độ A không bao giờ ghi `<w:trHeight>`; Chế độ B phải gỡ sạch khi sửa mẫu thật hoặc file doanh nghiệp gửi. Ngoại lệ: bảng header (bảng 1) giữ nguyên theo mẫu thật; chừa chỗ ký/điền tay thì dùng paragraph trống trong ô. Còn hụt thì siết giãn dòng trong ô về `w:line="300"` exact (chữ 13pt) / `320` (14pt), giữ nguyên `<w:cantSplit/>`. Mốc an toàn: cụm "tiêu đề + dòng 1" ≤ 6 cm.
- **`check_document.py` nhóm [F] mới:** quét bảng cấp ngoài cùng, đếm `<w:trHeight>` theo từng bảng; bảng 1 báo INFO, bảng 2 trở đi báo LỖI và fail `--strict`.
- Cập nhật `reference/phong-tranh-sai-lam.md` (checklist + 2 dòng bắt lỗi sớm), frontmatter SKILL.md, `plugin.json` v2.4.0.

## 2026-07-24 — qlks-sct-vn v1.2.0: chế độ thống kê, kê khai, báo cáo sản lượng khoáng sản (CV 5141/SNNMT-KS)

- Chắt lọc **CV 5141/SNNMT-KS ngày 29/12/2025** của Sở Nông nghiệp và Môi trường thành reference 14 mới. Điểm cốt lõi với Sở Công Thương: **SCT là nơi nhận báo cáo định kỳ của mỏ nhóm I** (cả GP Bộ NNMT cấp và GP Chủ tịch UBND tỉnh cấp) và nước nóng - nước khoáng thiên nhiên tỉnh cấp; nhóm II/III/IV đi luồng Sở Xây dựng. Hạn nộp trước **15/02** hằng năm, Mẫu 05/06/07/08 Phụ lục IV TT 36/2025/TT-BNNMT, báo cáo định kỳ đã tích hợp báo cáo thống kê trữ lượng.
- Chốt các mốc nghiệp vụ dùng khi kiểm tra mỏ: dự án **có hạng mục chế biến phải có 02 điểm cân - đo** (trước khi vào chế biến và khi ra khỏi dự án); thiết bị đo đạc chỉ dùng cho nước khoáng - nước nóng, đá ốp lát, cát sỏi lòng sông - lòng hồ - biển, khoáng sản ghi công suất theo thể tích, còn lại dùng cân; sổ khối lượng ghi **hàng ngày**, sổ hàm lượng ghi **hàng tháng**; **chênh lệch quá 10%** so với sổ theo dõi thì doanh nghiệp phải giải trình; bản đồ - mặt cắt hiện trạng lập 01 năm 01 lần chốt đến 31/12; trụ sở khác địa chỉ mỏ phải lưu 01 bộ bản sao sổ sách tại văn phòng mỏ.
- Chắt lọc **CV 6795/SNNMT-KS ngày 17/7/2026** (nghĩa vụ sau cấp phép, mỏ sắt Quý Xa) thành reference 07 mục VI: nhận diện loại công văn SNNMT gửi doanh nghiệp mới được cấp phép và đồng gửi SCT, kèm 5 đầu việc SCT phải mở hồ sơ theo dõi (thiết kế mỏ nhóm I, KH quản lý rủi ro, huấn luyện - GCN KTAT, VLNCN, tiếp nhận báo cáo định kỳ).
- Ghi nhận giấy phép mới: **GP 199/GP-BNNMT ngày 14/7/2026** cấp cho Công ty cổ phần Khai thác và Chế biến kim loại Thủ Đô khai thác quặng sắt **mỏ Quý Xa, xã Văn Bàn** (reference 10 mục I-b).
- Nghiệp vụ 7 → 8; references 13 → 14; văn bản gốc 19 → 21; bổ sung 4 văn bản SNNMT vào reference 09 và nhóm 5b + 3 cờ đỏ mới vào checklist hồ sơ pháp lý mỏ.

## 2026-07-24 — hc-sct-vn v1.1.0: vụ Cục Hóa chất xử phạt DN trên địa bàn (QĐ 26/QĐ-XPVPHC 08/7/2026)

- Bổ sung hồ sơ vụ Cục Hóa chất phạt Công ty TNHH Thương mại Hải Đăng (phường Lào Cai) 16 triệu đồng: 4tr — không lưu đủ hồ sơ huấn luyện ATHC (điểm a khoản 3 Điều 11 NĐ 71/2019); 12tr — không nộp báo cáo tổng hợp năm 2025 qua chemicaldata.gov.vn (Điều 29 NĐ 71/2019 sửa khoản 15 Điều 1 NĐ 17/2022). Bản scan QĐ tại `vi-du-thuc-te/xu-phat/`.
- Chốt nghiệp vụ: NĐ 71/2019 + 17/2022 vẫn là khung xử phạt hiện hành đến 7/2026 dù khung quản lý đã theo Luật 69/2025; thẩm quyền Cục Hóa chất dẫn QĐ 464/QĐ-BCT 16/3/2026; quy trình khi Cục kiểm tra/xử phạt trực tiếp gửi Sở phối hợp (ref 10, 16); chế tài răn đe cho CV đôn đốc DN báo cáo năm (ref 11 mục 4a); 3 cấu phần bắt buộc hồ sơ huấn luyện (ref 07).

## 2026-07-23 (bổ sung 4) — hnh-sct-vn v1.4.0: bản chốt GP Argon 2 xe + thông lệ ghi cột trọng tải

- Thay bản chốt (23/7/2026) Giấy phép Argon 2 xe biển Trung Quốc vào `vi-du-thuc-te/soi-phuong-nam-argon-nh3-072026/GP-SoiPhuongNam-Argon-loai2-2xe.docx`.
- Nguyên tắc 14 mới + reference 16 mục 6.6: khi số liệu trọng tải DN kê không khớp giấy tờ gốc hoặc hồ sơ mâu thuẫn, tiêu đề cột rút gọn "Trọng tải được phép chở", từng dòng ghi "Theo giấy tờ của phương tiện"; bài học đầu kéo — 25.000 kg là tổng trọng lượng bản thân, khối lượng kéo theo 40.000 kg, trọng tải chở = 0.
- Tinh chỉnh nguyên tắc 11 + reference 16 mục 6.4: mệnh đề "nhưng không vượt quá ngày [niên hạn]" CHỈ viết khi niên hạn rơi TRONG thời hạn GP tính từ ngày ký dự kiến (vụ Argon: 7/2026 + 24 tháng < 23/8/2028 → bỏ mệnh đề); không viết "kể từ ngày ký ban hành".

## 2026-07-23 (bổ sung 3) — dacn-sct-vn v1.1.0: nạp dữ liệu thật 95 dự án trong 03 KCN

- **Sổ danh mục dự án từ rỗng → 95 dự án thứ cấp** trong 03 KCN do Ban Quản lý các Khu công nghiệp tỉnh quản lý. Nguồn: Phụ lục 01 và 02 kèm Báo cáo của Tổ rà soát (bản 12/5/2026) + Báo cáo đánh giá hiện trạng, tình hình triển khai các dự án đầu tư trong các KCN (số liệu chốt đến 16/4/2026).
- **Phân bố:** theo KCN — phía Nam 66, Minh Quân 17, Âu Lâu 12 (khớp tuyệt đối với Báo cáo); theo trạng thái — đã sản xuất kinh doanh 46, đang đầu tư xây dựng 13, chưa triển khai xây dựng 36; tổng vốn đăng ký 15.501,318 tỷ đồng.
- **Điểm nghẽn: 63/95 dự án đang vướng, 238 lượt** — xây dựng 96 (chưa có GPXD 44, xây sai GPXD 24, chưa nghiệm thu 28), môi trường và PCCC 45, chủ trương đầu tư 44, nghĩa vụ tài chính 34, đất đai 19. Có 01 dự án vướng 8/8 nhóm, 07 dự án vướng 7 nhóm, 32 dự án không vướng.
- **05 cảnh báo về dữ liệu gốc** ghi thẳng vào file, script in ra đầu tiên khi chạy `kiem-tra`: (1) 09 dự án nhóm A đã dừng hoạt động nhưng phụ lục không chỉ rõ dự án nào — phải xác định trước khi tính chỉ tiêu sản lượng; (2) chênh lệch tổng vốn 98 tỷ do tiểu tổng nhóm B thiếu mục 47 (Super Star); (3) chênh lệch cột nghĩa vụ tài chính 3 lượt ở nhóm B (STT 48, 50, 51, 58) giữa đánh dấu từng mục và tiểu tổng, 07 cột còn lại khớp tuyệt đối; (4) trường xã/phường để trống vì phụ lục không ghi địa giới sau 01/7/2025; (5) trường nhóm phân loại tự động theo từ khoá, cần rà soát — nhất là bột đá CaCO3 vì ranh giới CBCT ↔ KS ảnh hưởng chỉ tiêu 4. **Không tự sửa số liệu gốc ở chỗ nào.**
- **Cải tiến `theo_doi_du_an.py`:** lệnh `kiem-tra` in kỳ số liệu ở đầu, in khối cảnh báo dữ liệu gốc trước tiên, gom cảnh báo theo LOẠI kèm số lượt và ví dụ thay vì liệt kê từng dòng (238 dòng → 1 khối).
- **`SKILL.md` ghi rõ phạm vi còn thiếu của sổ:** chưa có dự án trong các KCN do Ban Quản lý Khu kinh tế tỉnh quản lý, dự án trong CCN, dự án ngoài khu/cụm, khoáng sản, thuỷ điện, hạ tầng KCN/CCN — để không báo cáo thiếu.

## 2026-07-23 (bổ sung 2) — dacn-sct-vn v1.0.1: xác nhận 03 điểm treo, gỡ toàn bộ GATE

Bạn đã đối chiếu bản gốc có dấu và xác nhận ngày 23/7/2026. Ba nội dung treo khi phát hành v1.0.0 nay đã chốt:

1. **Công văn triển khai NQ 169 của UBND tỉnh Lào Cai: số 7323/UBND-TH ngày 17/7/2026**, Chủ tịch Nguyễn Tuấn Anh ký. Con số 7325 trên trang Phụ lục của bản scan là lệch dấu đóng số — không dùng.
2. **Ba dòng phân nhóm hàng xuất khẩu CÓ trên bản ký** và dùng chính thức: 7a nông-lâm-thuỷ sản 87,5%; 7b công nghiệp chế biến, chế tạo 7,14%; 7c nhiên liệu, khoáng sản 18,18% (mục tiêu năm 2026). Việc 7a, 7b mờ/mất khi in và 7c bị đánh số nhầm thành TT 10 là lỗi in ấn của bản scan, không phải nội dung văn bản — khi lập bảng báo cáo đánh số lại theo trật tự 7a, 7b, 7c dưới chỉ tiêu 7.
3. **Chỉ tiêu 29 (tỷ lệ KCN đang hoạt động có hệ thống XLNT tập trung đạt chuẩn), mục tiêu năm 2026 = 42%** theo bản ký; 41,7% trong bản dự thảo Excel là số cũ — không dùng.

- Sửa: `SKILL.md` mục III.5, `references/01`, `references/02` (gỡ 02 cảnh báo + thêm hướng dẫn đánh số lại 7a/7b/7c), `mau-van-ban/01` (điền số vào đoạn mở đầu + sửa lưu ý 1), `mau-van-ban/02`, `mau-van-ban/03` (điền đủ số, ngày Công văn ở phần căn cứ), `plugin.json` v1.0.1.
- **Kết quả:** plugin không còn nội dung treo; toàn bộ căn cứ pháp lý đủ điều kiện viện dẫn trực tiếp vào văn bản phát hành.

## 2026-07-23 (lần 3 — chiều)
- **sd-vlncn-sct-vn [2026.7.23.2]**: vụ Mông Sơn giai đoạn 2 — PANM chỉnh sửa hoàn chỉnh theo CV 4378 (Công ty ký ngay, 35 trang, không ô chờ điền). Reference 07 mục H bổ sung 4 bài học chiến lược: (1) "dải thiết kế" — thiết kế tính theo d=105mm nhưng quy định dải 76-105mm (tr.58-59, Bảng 3-11), mỏ chỉ có máy 76/90mm → giữ 76/90 + mục 3.5 bảng đối chiếu 9 điểm chứng minh cùng công thức/an toàn hơn, không buộc điều chỉnh thiết kế; (2) tối ưu trần cho DN có địa chỉ: Qb(max)=683kg theo Bảng tổng hợp thiết kế tr.63 (Rc 61,6m, rs 261,4m, vi sai 3 hàng 228kg<403kg); (3) gộp chủng loại thuốc nổ "Thuốc nổ các loại (AD1; Anfo): 38.950kg" theo tiền lệ GP 2781/TTr ngày 20/7/2026 + ghi chú linh hoạt cơ cấu, kíp vẫn tách 2.184+3.408; (4) thể thức: lùi đầu dòng 78 đề mục (quy tắc vĩnh viễn kể cả Chế độ B), sửa đánh số trùng mục IV (hai lần 4.3, "4..3", mục "5." lạc) sau khi grep tham chiếu chéo. Reference 03 mục G thêm điểm 11-13; reference 08 thêm mục E case xác nhận Mông Sơn (lỗ con 4.4→300m phía thấp, lỗ lớn 4.5→200m, 500m > mọi giá trị → không thuộc điểm d k2 Đ38); SKILL.md anti-error 15. Ví dụ thực tế mới: PANM-Mong-Son-chinh-sua-2026.docx + CV-4378-tra-ho-so-Mong-Son-2026.pdf.

## 2026-07-23 — Thêm plugin dacn-sct-vn v1.0.0: quản lý dự án công nghiệp phục vụ mục tiêu tăng trưởng

- **Plugin mới**, cấu trúc chuẩn. Đáp ứng **Nghị quyết 169/NQ-CP ngày 27/6/2026** của Chính phủ về mục tiêu tăng trưởng của các địa phương năm 2026 và giai đoạn 2026-2030 (thực hiện KL 18-KL/TW, NQ 25/2026/QH16, NQ 109/NQ-CP) và **Công văn triển khai của UBND tỉnh Lào Cai ngày 17/7/2026** kèm Phụ lục phân công 32 chỉ tiêu. Sở Công Thương **chủ trì 09 chỉ tiêu**, phối hợp 06.
- **Vị trí trong hệ sinh thái:** `kccn-sct-vn` quản lý THỦ TỤC KCN/CCN; các plugin lĩnh vực quản lý CHUYÊN NGÀNH; `dacn-sct-vn` quản lý **KẾT QUẢ ĐẦU RA VÀ ĐÓNG GÓP TĂNG TRƯỞNG** của toàn bộ dự án công nghiệp, không phân biệt lĩnh vực.
- **7 references:** (01) chuỗi văn bản + trách nhiệm cơ quan chủ trì/phối hợp/người đứng đầu + bảng đầu mối cấp tỉnh; (02) **bảng đầy đủ 32 chỉ tiêu** với mục tiêu 2026 và giai đoạn 2026-2030, kết quả Quý I/2026 làm mốc; (03) 7 nhóm dự án động lực (HT-KCN, HT-CCN, KS, LK-HC, CBCT, NL, TM), 8 trạng thái vòng đời, thang chấm điểm ưu tiên 100 điểm, quy tắc gắn dự án ↔ chỉ tiêu; (04) phương pháp tính IIP, giá so sánh 2010, kim ngạch, chế biến chế tạo, tiết kiệm năng lượng + quy trình 5 bước xử lý chênh lệch với Thống kê tỉnh; (05) chế độ báo cáo trước ngày 20 gửi Sở Tài chính, lồng ghép NQ 01/NQ-CP, khung 7 mục, lịch công tác trong tháng; (06) 7 nhóm điểm nghẽn chưng cất từ thực tiễn rà soát dự án trong các KCN (QH, CTDT, GPMB, DD, XD, MT-PCCC, TC) + quy tắc 04 yếu tố bắt buộc; (07) 3 kịch bản tăng trưởng, ngoại suy 5 bước, xử lý riêng nhóm mùa vụ, 4 ngưỡng cảnh báo.
- **2 scripts đã kiểm thử trên dữ liệu thật:** `phan_tich_thang.py` đọc file Excel theo dõi sản xuất công nghiệp (sheet T1-T12), tính %KH năm, độ lệch so tiến độ chuẩn, so cùng kỳ, ước cả năm, tự gắn 4 mức cảnh báo AN-TOAN / CAN-CHU-Y / NGUY-CO / BAO-DONG, xuất CSV; `theo_doi_du_an.py` 7 lệnh quản lý sổ danh mục dự án, tự phát hiện bản ghi thiếu nguồn và bản ghi tính sản lượng sai trạng thái, chấm điểm ưu tiên tự động, xuất bảng không markdown để dán vào báo cáo.
- **3 mẫu văn bản** (báo cáo định kỳ NQ 169 kèm bảng 9 chỉ tiêu có sẵn mục tiêu; công văn đôn đốc dự án; báo cáo giải trình chỉ tiêu có nguy cơ không hoàn thành), **2 checklist** (12 mục kiểm tra số liệu; rà soát dự án theo 7 nhóm điểm nghẽn), **2 file dữ liệu** (`schema-du-an.json` lược đồ đầy đủ; `danh-muc-du-an.json` khởi tạo RỖNG — plugin không tự sinh dữ liệu).
- **6 anti-error nghiệp vụ** đưa thẳng vào script và checklist: không nhầm điện phát với điện thương phẩm (chỉ tiêu 15); không nhầm vốn đăng ký với vốn thực hiện (chỉ tiêu 11); không nhầm diện tích GPMB với mặt bằng sạch; chỉ trạng thái HD/MR mới được tính sản lượng; tốc độ tăng trưởng phải tính theo giá so sánh 2010; ba loại số mục tiêu/thực hiện/dự báo phải ở ba cột riêng.
- **2 điểm còn treo, đã đánh dấu GATE trong SKILL.md và reference 01, chờ Bạn xác nhận bản gốc:** (a) số Công văn triển khai của UBND tỉnh — bản scan đóng dấu số tự động, OCR không đọc được, trang 1 hiển thị 7323 còn Phụ lục hiển thị 7325; (b) hai dòng phân nhóm hàng xuất khẩu (nông lâm thuỷ sản 87,5%; công nghiệp chế biến chế tạo 7,14%) chỉ có trong bản dự thảo Excel, bản ký bị mất khi in và đánh số nhầm TT 7 → TT 10 → TT 8. Ngoài ra chỉ tiêu 29 lệch giữa bản ký (42%) và dự thảo (41,7%) — đã lấy số bản ký.
- Đã áp quy tắc validate: description plugin.json 496 ký tự (≤500), SKILL.md description 989 ký tự (≤1024), cấu trúc `.claude-plugin/plugin.json` + `skills/dacn-sct-vn/`, không kèm `__pycache__`.

## 2026-07-23 (bổ sung)
- **sd-vlncn-sct-vn [2026.7.23]**: vụ Thành Hương Nghĩa Lộ (mỏ đá vôi Bản Hốc, xã Văn Chấn — CV 4280/SCT-CN ngày 22/7/2026 trả hồ sơ). Thêm reference `08-khoang-cach-an-toan-da-vang.md` — chưng cất nguyên gốc QCVN 01:2019/BCT về đá văng: kiến trúc 2 tầng (Bảng 1 khoản 7 Điều 5 là SÀN + chú thích (2) chỉ đánh dấu 2 dòng; Phụ lục 7 mục 4.1/4.3/4.4/4.5 là cách XÁC ĐỊNH), toàn bộ dữ liệu Bảng 1/7.8/7.9, quy tắc 1,5 lần (kích hoạt dốc >30° HOẶC chênh >30m; chỉ "về phía thấp hơn"; gắn đích danh Bảng 7.8 — CẤM phép lai sàn Bảng 1 × 1,5), hai cách đọc cho nổ làm tơi n<1 và cách Sở đã CHỐT (lỗ lớn theo 4.5/Bảng 7.9 sàn 200m không nhân; lỗ nhỏ theo 4.4 → Bảng 7.8 cột n=1, w làm tròn tăng → ×1,5 = 300m phía thấp hơn), hệ quả biên sát nút → hiệu lực PANM dạng ĐIỀU KIỆN theo đo đạc hiện trường (điểm d k2 Đ38), yêu cầu nhất quán khi kết luận khác công văn Sở đã phát hành. Reference 03: mục C.3 dẫn sang ref 08 + mục G mới checklist 10 lỗi PANM điển hình (mâu thuẫn 2.4, vi sai Qb>Qmax, đơn vị kíp cái, 32/36mm, số học tháng=năm/12, căn cứ sống, QĐ phân công dẫn GP hết hiệu lực, kho cung ứng, che chắn bắt buộc + trạm gác QL, nghĩa vụ hậu kiểm mục V). Reference 07 mục I: tóm tắt vụ việc + 2 file ví dụ thực tế mới (`CV-4280-tra-ho-so-Thanh-Huong-2026.pdf`, `PANM-Thanh-Huong-chinh-sua-2026.docx` — PANM mẫu chuẩn 30 trang: bảng 1.000m, chia nhóm vi sai, che chắn B40 kèm sơ đồ Hình 4, trạm gác QL32, ô 【…】 bôi đỏ chờ số liệu). SKILL.md: anti-error 14 + cây thư mục.

## 2026-07-23
- **pccc-sct-vn v1.1.1**: PHÁT HIỆN QUAN TRỌNG qua theo dõi web — **Bộ Công Thương ĐÃ ban hành QĐ 1609/QĐ-BCT ngày 01/7/2026** (Thứ trưởng Trương Thanh Hoài ký, hiệu lực 01/7/2026, Công báo số 406 ngày 17/7/2026, ~32 trang) ban hành giải pháp kỹ thuật nâng cao an toàn PCCC cho cơ sở, công trình không bảo đảm PCCC thuộc thẩm quyền quản lý của BCT — văn bản áp dụng trực tiếp cho cửa hàng xăng dầu, gas, kho VLNCN, nhà máy điện, hóa chất. Sửa toàn bộ các chỗ ghi "BCT chưa ban hành" trong SKILL.md (bảng khung pháp lý + nguyên tắc 8), reference 14 (mốc 01/7/2026, mục V), reference 15 (mục II, VI). Đánh dấu: toàn văn chưa chưng cất — chờ tải bản gốc từ Công báo (link CDN chặn truy cập tự động), khi có sẽ GATE PDF và bổ sung reference chi tiết; tuyệt đối không suy diễn nội dung QĐ 1609 từ QĐ 1074.
- **kccn-sct-vn v1.7.0**: cập nhật Nghị định 178/2026/NĐ-CP ngày 20/5/2026 (hiệu lực 06/7/2026) — nghị định khung đầu tiên về quản lý, sử dụng, khai thác tài sản kết cấu hạ tầng CCN/KCN do Nhà nước đầu tư. Thêm reference `18-nd178-2026-tai-san-kcht-ccn.md` (phạm vi/loại trừ; hai chế độ song song khoản 3 Đ.1; SCT = cơ quan quản lý chuyên ngành hạ tầng cấp tỉnh; trình tự giao Đ.10 với Mẫu 01B; 4 phương thức khai thác; 9 hình thức xử lý; báo cáo 28/02 - 15/3; mốc 06/01/2027 danh mục BCT và 06/7/2028 hạn giao tài sản; lộ trình 6 bước cho Phòng QLCN) + toàn văn `van-ban-goc/ND-178-2026-tai-san-ket-cau-ha-tang.docx`. Cập nhật reference 01 (bảng D), SKILL.md (description, trigger 9, khung pháp lý điểm 7, bảng reference), plugin.json 1.7.0.
- **pccc-sct-vn v1.1.0**: cập nhật QĐ 1074/QĐ-BXD ngày 29/6/2026 (KT. Bộ trưởng — TTr Phạm Minh Hà) ban hành giải pháp kỹ thuật nâng cao an toàn PCCC cho cơ sở, công trình hiện hữu không bảo đảm PCCC thuộc thẩm quyền BXD, và CV 7432/UBND-XD ngày 21/7/2026 (KT. Chủ tịch — PCT Phan Trung Bá) triển khai tại Lào Cai (SXD chủ trì, hạn 01/7/2028). Thêm reference `15-giai-phap-ky-thuat-qd1074-bxd.md`: 3 điều kiện phạm vi đồng thời (danh sách UBND tỉnh + thẩm quyền BXD + Phụ lục I NĐ 105), 3 nhóm giải pháp (áp QCVN/TCVN hiện hành kể cả giảm quy mô; thiết kế theo tính năng 9 bước; giải pháp cụ thể cho tồn tại điển hình), yêu cầu tối thiểu mục 4.4, tóm tắt 6 Phụ lục A-F với các bẫy loại trừ hạng nguy hiểm cháy nổ A, B (Phụ lục F do C07 biên soạn theo CV 2257/BCA-VPB + 2147/C07-P4), phân công việc cho SCT/Phòng QLCN theo CV 7432. Cập nhật SKILL.md (khung pháp lý mục II, bảng reference, nguyên tắc bất biến 8, description) và reference 14 (mốc 01/7/2026: BXD đã hoàn thành; BCT CHƯA ban hành — quá hạn, cần theo dõi/tham mưu đề nghị Bộ). Thêm `van-ban-goc/` 3 file: QĐ 1074, Tài liệu V18 60 trang kèm QĐ, CV 7432.
## 2026-07-21
- **sd-vlncn-sct-vn [2026.7.21]**: cập nhật TT 26/2026/TT-BCT 20/5/2026 (thay Điều 4 TT 23/2024 về thẩm quyền, bãi bỏ k1–3 Đ1 TT 38/2025, mẫu GP mới) theo GP 2507/GP-UBND ngày 21/7/2026 — Cty CP Khai thác VLXD Miền Bắc, mỏ đá VLXDTT thôn Toòng Già xã Phong Hải, hiệu lực đến 05/7/2031; thêm bản ký + toàn văn vào vi-du-thuc-te; sửa SKILL.md (mục II, bảng thẩm quyền III), reference 01 (mục 5a + cụm căn cứ), reference 07 (bảng A), mẫu 01/05/10. Đồng bộ GP lên web vlncn-laocai (công ty + giấy phép + công trình mới) và file 2507_GP-UBND.pdf lên vlncn-laocai-files.
- **kccn-sct-vn v1.5.0**: thêm reference `16-uu-dai-dau-tu-ccn.md` — chính sách ưu đãi đầu tư trong CCN theo Tài liệu giới thiệu của Sở ngày 21/7/2026 (thuế TNDN 10%/15 năm hoặc 17%/10 năm theo địa bàn xã — Luật 67/2025 + NĐ 320/2025; miễn tiền thuê đất XDCB + 7/11/15 năm — Đ.39 NĐ 103/2024; đơn giá thuê đất 0,8%; NSNN hỗ trợ ≤30% vốn hạ tầng; QĐ 2167/QĐ-UBND 23/6/2026: 87 xã ĐBKK + 08 xã KK; lưu ý từ 01/10/2025 ưu đãi thuế theo xã/phường nơi đặt CCN). Cập nhật SKILL.md (bảng reference + nhiệm vụ 1), Q36 reference 10 trỏ sang 16. Đồng bộ với khối "Chính sách ưu đãi đầu tư" mới trên congnghieplaocai.vn.

## 2026-07-20
- **kccn-sct-vn v1.4.0**: KCN Võ Lao được chấp thuận CTĐT tại QĐ 2463/QĐ-UBND ngày 16/7/2026 (482,6 ha, xã Võ Lao + Tằng Loỏng, NĐT Công ty CP đầu tư hạ tầng Châu Giang); tổng 11 KCN có QĐ CTĐT/đã thành lập; hoàn thành vượt mục tiêu 02 KCN của NQ 34-NQ/TU. Cập nhật references 12, 14, 15, SKILL.md; thêm van-ban-goc/QD-2463-2026-CTDT-KCN-Vo-Lao.pdf.


## 20/7/2026 — hnh-sct-vn v1.2.1: bài học căn cứ thời hạn Giấy phép (niên hạn sử dụng, KHÔNG phải thời hạn kiểm định)

- **Lỗi thật vụ Toàn Phát TQ** (NH3 loại 2, 5 tổ hợp xe biển TQ, tuyến Hà Khẩu - Kim Thành): CV bổ sung hồ sơ viết "không vượt quá thời hạn kiểm định của từng phương tiện" — Bạn bắt sai. Căn cứ đúng: **khoản 3 Điều 13 NĐ 161/2024** = tối đa 24 tháng và **không quá NIÊN HẠN SỬ DỤNG của phương tiện** (đã đối chiếu văn bản gốc). Thời hạn kiểm định chỉ là điều kiện phương tiện; khống chế GP theo hạn kiểm định (tiền lệ Apatit, Sợi Phương Nam 23 tháng) là biện pháp nghiệp vụ ghi trong Phiếu trình, không viện dẫn Điều 13.3.
- Sửa: SKILL.md mục VII (nguyên tắc bất biến 11), reference 11 (lỗi thẩm định số 9), reference 16 mục 2 (LƯU Ý CĂN CỨ + xử lý riêng xe biển Trung Quốc); CHANGELOG-v2026.07.20.md.
- **Commit này đồng bộ luôn delta v1.2.0 (06/7/2026)** repo còn thiếu: mẫu Biên bản thẩm định chuẩn của Sở (Thái Thịnh loại 3) + cập nhật SKILL.md mục IV-a, references 15, 16.

## 20/7/2026 — Thêm plugin qlks-sct-vn v1.1.0: quản lý nhà nước về khoáng sản

- **Plugin mới** (v1.0.0 ngày 17/7 + nâng cấp v1.1.0 ngày 20/7), cấu trúc chuẩn. Lõi: (a) ma trận phân vai SCT - SNNMT - SXD - Thuế - Công an - xã theo TT 37/2025/TT-BCT + KH Chỉ thị 11-CT/TU + CV 5973/UBND-KT; (b) GATE 6 mốc: 01/7/2025 (Luật 54/2024) → **12/6/2025 NĐ 136/2025 Đ34 nhóm II về Chủ tịch tỉnh** → 01/01/2026 (Luật 147/2025) → 16/01/2026 (NĐ 21/2026) → 18/5/2026 (NQ 66.19 phân quyền 9 nhóm TTHC) + cấp đổi GP 36 tháng; (c) 7 nghiệp vụ: phân vai, KH quản lý rủi ro (TT 24/2025, hầm lò 7 ngày sau TT 26/2026), GCN KTAT khai thác hầm lò (TT 43/2025 — phân biệt GCN KTAT VLNCN của hl-vlncn), chế biến - nguồn gốc, đối chiếu VLNCN - sản lượng qua chỉ tiêu thuốc nổ đơn vị, kiểm tra - tham mưu đình chỉ (10 nhóm tồn tại phải dừng khai thác theo hướng dẫn SNNMT 8/2025), rà chồng lấn khoáng sản khi thẩm định dự án/CCN (4 lớp QĐ 866 - 1626 - 525 - 1277/QĐ-TTg; case CCN Báo Đáp chồng 2 ha mỏ Caolanh - felspat theo CV 6791/SNNMT-KHTC 17/7/2026).
- **13 references, 6 mẫu văn bản, 2 checklist**; `du-lieu/` 3 CSV (208 GP khai thác 31/10/2025, 43 GP thăm dò Yên Bái 6/2025, theo dõi pháp lý 209 mỏ 4/2026 với cột TKM/GĐĐH/trạm cân/GP VLN); `van-ban-goc/` 19 file (TT 24/43/67/2025, TT 26/2026, NQ 66.19 toàn văn + PL VIII, Luật 147, NĐ 21/2026, BC UBND tỉnh QLNN khoáng sản năm 2025 — nguồn số liệu chính thức 178 GP còn hiệu lực = 70 Bộ + 108 tỉnh, 4 kết luận thanh tra 2025, 6 nhóm vướng mắc đã kiến nghị Bộ).
- Reference 11 + 12: bản đồ liên kết 13 plugin, ranh giới tinh với tkm (thẩm định vs kiểm tra tuân thủ thiết kế), hl-vlncn (2 loại GCN KTAT), sd-vlncn (VLNCN phù hợp công suất), kccn (ý kiến khoáng sản trong thẩm định CCN 2 chiều).
- Đã áp quy tắc validate: description plugin.json 495 ký tự (≤500), SKILL.md description 1018 ký tự (≤1024).

## 15/7/2026 — Chốt 2 điểm mở phân công (xác nhận của Bạn)

- **sct-laocai-org-vn v2.0.1**: KCN → CN(Trung); **toàn bộ HHNH → CN(Linh)** từ 15/7/2026 (giai đoạn 6/7–14/7/2026 giữ CN(Khôi) đúng lịch sử).
- **hnh-sct-vn 1.1.2**: chuyên viên thụ lý GP vận chuyển HHNH = CN(Linh), kiểm duyệt PTP Trần Trọng Trang.

## 14/7/2026 — Đồng bộ Thông báo phân công nội bộ Phòng QLCN 10/7/2026

- **sct-laocai-org-vn v2.0**: viết lại mục "Cơ cấu nội bộ Phòng QLCN" — 1 TP + 3 PTP (Nguyễn Hồng Vân, Trần Trọng Trang, Đỗ Mạnh Cường) + 10 CV; VLNCN/CCN/KHCN-ĐMST CN → TP trực tiếp; VLNCN → CN(Khôi); ATTP → CN(Nam); chất lượng SPHH → CN(Dương); chế độ báo cáo nội bộ; bảng liên kết hệ sinh thái.
- **sd-vlncn-sct-vn 2026.7.14 / kho-vlncn-sct-vn 1.4.1 / hl-vlncn-sct-vn 1.0.1**: dòng Lưu VLNCN chuyển CN(Linh) → CN(Khôi).
- **xd-sct-vn 1.1.1**: kiểm duyệt thẩm định/KTCTNT = PTP Vân; kho VLNCN phối hợp CN(Khôi).
- **hnh-sct-vn 1.1.1**: ghi chú tách an toàn/tập huấn HHNH (CN Linh) và thụ lý cấp phép (CN Khôi, PTP Trang kiểm duyệt).

## 2026-07-14 — Thêm plugin tkm-sct-vn v1.2.0: chuyên viên cao cấp thẩm định thiết kế mỏ (2006–2026)
- **Plugin mới**, cấu trúc chuẩn `<tên>/.claude-plugin/plugin.json` + `<tên>/skills/<tên>/`. Lõi: (a) bảng dòng thời gian pháp lý 6 thời kỳ TT 03/2007/TT-BCN → 33/2012 → 26/2016 → 31/2025/TT-BCT đan với Luật XD 2003/50-2014/135-2025 và NĐ 16/2005→12/2009→59/2015→15/2021→175/2024→217/2026 (đã xác minh web đến từng ngày ban hành); (b) GATE GIAI ĐOẠN chống trộn căn cứ hai thời kỳ; (c) 3 phép thử thẩm quyền theo nhóm khoáng sản I–IV (NĐ 193/2025 + 21/2026, đá hoa trắng → SXD từ 02/7/2025); (d) chuyển tiếp kép: khoản 5 Điều 76 NĐ 217/2026 (chấm dứt - trả hồ sơ, mẫu thật đập 1 Sin Quyền 7/2026) và Điều 4 TT 31/2025 (trình trước 01/7/2025 chưa có TB KQ → theo TT 26/2016).
- **`van-ban-goc/`**: toàn văn TT 31/2025 bản Unicode (.docx, thân 6 điều + đủ 10 Phụ lục) + bản .doc gốc moit.gov.vn + BC 452/BC-TTCP 26/02/2026 (scan gốc, 10MB) — thanh tra chuyên đề mỏ VLXD toàn quốc, thời kỳ 01/01/2019–30/6/2024 (trang 2 bản gốc in nhầm "2029"), chưng cất tại reference 09 thành bản đồ rủi ro hậu kiểm + 24 kiến nghị chính sách.
- **`vi-du-thuc-te/`**: 12 văn bản thật của Sở 2019–2026 (TB thẩm định San Bang - Sin Quyền, NM tuyển apatit nghèo ~200,3 tỷ, cặp CV từ chối đá hoa trắng nhóm II, CV chấm dứt K5Đ76, CV Quang Đạt rút hồ sơ, tham luận 2019, báo cáo giải trình Thanh tra CP...) làm template Chế độ B; `mau-van-ban/` 2 khung CV từ chối/chấm dứt với đoạn ranh giới trách nhiệm 2 tầng chép nguyên văn.
- **Reference 10 + mục XI SKILL.md**: bản đồ liên kết 15 plugin theo vòng đời dự án mỏ (quy-hoach-ct → tkm → bvmt/pccc/xd → sd/kho/hl-vlncn → hc/hnh → kccn → vbhc/org/bpb), 4 kịch bản chuỗi, quy tắc chống giẫm chân; ranh giới tinh: thiết kế khoan nổ trong thiết kế mỏ = tkm, giấy phép VLNCN/PANM = sd-vlncn, kho = kho-vlncn, vận chuyển VLNCN do Công an cấp (không thuộc hnh).
- Tự test 5 kịch bản PASS (thẩm quyền sau 01/7/2026, K5Đ76, trích Phụ lục từ file gốc, bẫy lỗi in BC 452, ranh giới vận chuyển VLNCN).

## 2026-07-09 — vbhc-vn v2.1.0 → v2.2.0: vá 3 lỗi thật vụ CV Yên Hợp gửi Sở Tài chính (replace trượt im lặng)
- **Vụ thật 09/7/2026**: soạn CV tham gia ý kiến điều chỉnh tiến độ quy hoạch CCN Yên Hợp trên mẫu thật `cong-van-de-nghi-bo-sung-ho-so.docx` mắc 3 lỗi lọt ra bản trình: (1) V/v vẫn nguyên trích yếu vụ nổ mìn cũ — file mẫu lưu Unicode **NFD** (dấu tách rời) trong khi pattern là NFC nên `replace_in_cell` trượt **im lặng**, QA thể thức vẫn PASS; (2) không điền số/ngày công văn đến của UBND xã Xuân Ái (857/UBND-KT ngày 08/7/2026) do bỏ qua bước bắt buộc `extract_metadata.py` — context hiển thị ô số trống; (3) dòng Lưu ghi CN(Trang) thay vì CN(Trung) — CCN do chuyên viên Lê Quang Trung tham mưu theo bảng phân công `sct-laocai-org-vn`.
- **`scripts/fill_template.py`**: `_replace_text_in_paragraph` chuẩn hóa **Unicode NFC hai phía** trước khi so khớp (khớp được mẫu lưu NFD); `replace_in_cell`/`replace_in_paragraph` thêm tham số `required=True` mặc định — pattern không khớp là **raise ValueError kèm text thật** của ô/paragraph, chấm dứt thất bại im lặng (truyền `required=False` chỉ khi pattern tùy chọn có chủ đích).
- **`scripts/qa_all.py`**: thêm `--forbid "chuỗi1" "chuỗi2" ...` / `--require ...` — đối chiếu NỘI DUNG toàn văn bản (paragraph + mọi ô bảng, NFC hai phía): FAIL nếu còn chuỗi vụ cũ hoặc thiếu chuỗi vụ mới. Chốt chặn thứ hai độc lập với assertion trong build script; bắt buộc dùng với Chế độ B trên mẫu thật.
- **SKILL.md**: thêm Quy tắc bất biến 15-19: (15) NFC/NFD khi tự viết code so khớp; (16) replace bắt buộc khớp, không bọc try/except nuốt lỗi; (17) `--forbid`/`--require` bắt buộc với Chế độ B trên mẫu thật, kèm công thức lập danh sách; (18) người soạn dòng Lưu = **chuyên viên phụ trách lĩnh vực** tra bảng `sct-laocai-org-vn` (CCN→Trung...), `CN(Trang)` chỉ khi PTP nói rõ tự soạn, không rõ thì hỏi; (19) văn bản đến là PDF phải `extract_metadata.py` trước khi dẫn chiếu số/ngày — ô trống trong context là tín hiệu đọc đĩa, script không đọc được thì để trống và nói rõ. Quy tắc tốc độ mục 2 cập nhật lệnh chuẩn `build && qa_all --forbid ... --require ...`.
- Đã test 5 kịch bản: QA PASS/FAIL đúng, raise đúng lúc pattern trượt, pattern NFC khớp mẫu NFD, demo cũ chạy bình thường.

## 2026-07-06 (đợt 4) — bvmt-sct-vn v1.0 → v1.1.0: chuyên sâu ĐTM/GPMT đến NĐ 48/2026 + chuyển chuẩn plugin
- **Viết lại toàn bộ `references/03-dtm-gpmt.md`** (67 → ~250 dòng) thành tài liệu tra cứu đầy đủ: (a) khung phân loại nhóm I/II/III/IV theo Điều 28 Luật BVMT (sửa bởi Luật 146/2025) + Điều 25 NĐ 08 (sửa bởi Điều 5 NĐ 48/2026 — quy mô đất lượng hóa: lớn ≥300 ha, TB 50–<300, nhỏ <50 ha; bỏ tiêu chí lúa 2 vụ), tóm tắt Phụ lục II/III/IV/V bản mới (PL II thu hẹp 17 loại hình, bỏ kho xăng dầu; hạ tầng KCN nhóm I STT 6b PL III, hạ tầng CCN chuyển sang NHÓM II STT 4b PL IV); (b) bảng quyết định ĐTM → GPMT → đăng ký môi trường, kèm ngưỡng GPMT mới khoản 5 Điều 74 (NT sinh hoạt ≥50 m³/ngày, NT công nghiệp thuộc PL II mọi mức, ngoài PL II ≥10 m³/ngày, khí thải ≥5.000 m³/giờ, tính theo dự án tổng thể); đổi "miễn đăng ký" → "không phải đăng ký"; (c) trình tự - thời điểm (ĐTM đồng thời BCNCKT, phê duyệt trước quyết định đầu tư; GPMT trước vận hành thử nghiệm; VHTN ≤6+6 tháng, 2 trường hợp miễn VHTN; Điều 27a phân kỳ/dự án thành phần — tiêu chí theo dự án tổng thể; trường hợp điều chỉnh GPMT mới: chuyển giao/tiếp nhận/tái sử dụng nước thải; nộp trực tuyến toàn trình); (d) phân cấp thẩm quyền: Điều 26a mới (Chủ tịch UBND tỉnh nhận đầu tư công không QH/TTg, dự án chỉ tiêu chí chuyển MĐSDĐ nhạy cảm, THỦY ĐIỆN không QH/TTg, dầu khí), Điều 27b liên tỉnh; ghi rõ KHÔNG còn cấp xã cấp GPMT (Luật 146 Điều 41 mới + NĐ 48 bãi bỏ quy định NĐ 131/2025); (e) bảng tra nhanh 10 loại dự án Lào Cai (thủy điện, mỏ apatit/đồng/sắt/đá vôi trắng, tuyển khoáng, luyện kim Tằng Loỏng, DAP/gyps, hạ tầng KCN, hạ tầng CCN 50–75 ha kèm ngoại lệ khoản 7 Điều 48, dự án thứ cấp, kho xăng dầu, nhiệt điện) + mục anti-error 7 cạm bẫy. Toàn bộ số điều/khoản/ngưỡng trích từ văn bản gốc (file .docx NĐ 48/2026, Luật 146/2025, NĐ 08/2022, NĐ 05/2025, Luật 72/2020, TT 09/2026 do người dùng cung cấp).
- **Cập nhật `references/02-khung-phap-ly.md`**: chi tiết hóa mục Luật 146/2025 (ngày 11/12/2025, hiệu lực 01/01/2026, liệt kê các khoản sửa Luật BVMT) và NĐ 48/2026 (liệt kê nội dung từng Điều 5–39, gồm Điều 26a/27a/162/163 sửa đổi, Điều 35 thay phụ lục, Điều 38 chuyển tiếp, Điều 39 bãi bỏ NĐ 131/136); bổ sung TT 09/2026/TT-BNNMT (29/01/2026, bãi bỏ TT 07/2025/TT-BNNMT); ghi chú "ưu tiên văn bản hợp nhất NĐ 08 gộp đến NĐ 48, chưa có thì đọc song song 3 nghị định"; mở rộng bảng theo dõi hiệu lực (thêm 3 dòng: Luật hợp nhất, TT 07/2025/TT-BNNMT hết hiệu lực, NĐ 131/136 bị bãi bỏ một phần).
- **SKILL.md**: description bổ sung từ khóa phân loại nhóm I II III IV, Phụ lục III IV V, Điều 28/30/39/49, Điều 26a 27a, đối tượng ĐTM/GPMT, đăng ký môi trường, thời điểm cấp GPMT, vận hành thử nghiệm; mục IV cập nhật ngày/hiệu lực; mục VII viết lại mô tả ref 03.
- **Chuyển chuẩn plugin**: `bvmt-sct-vn/.claude-plugin/plugin.json` (v1.1.0) + `bvmt-sct-vn/skills/bvmt-sct-vn/…` (thống nhất kiểu gói của repo, zip là upload được ngay).
- Giữ nguyên tắc cốt lõi: SCT là cơ quan PHỐI HỢP, không phê duyệt ĐTM, không cấp GPMT; tên cơ quan mới Bộ/Sở Nông nghiệp và Môi trường, không còn cấp huyện.

## 2026-07-06 (đợt 3) — vbhc-vn v2.1.0 (QA một phát) + vbhc-pdf-reader-vn v2.0 (sentinel)
- **vbhc-vn v2.0.1 → v2.1.0**: thêm `scripts/qa_all.py` — QA MỘT PHÁT: một lệnh gộp kiểm XML (Line header, 13pt Số/Ngày, br header, body căn giữa/firstLine) + check_document + render PDF đúng 1 lần (profile soffice ấm; widow word, khối ký gãy trang) + ảnh ghép mọi trang trong 1 file để view 1 lượt. Đo: 1,3-3,0s/vòng thay vì ≥30-50s render đôi cũ. `qa_pdf_check.py` thêm `--pdf` khỏi render lại. SKILL.md: Bước 2 bỏ lượt inspect template, Bước 4 viết lại "build && qa_all", mục mới "Quy tắc tốc độ" (văn bản thường 3-4 lượt tool). Kèm vá v2.0.2: 2 file reference `*-goc.md` hết hardcode đường dẫn skill lẻ.
- **vbhc-pdf-reader-vn v1.0 → v2.0**: thu gọn thành SENTINEL 70 dòng (trigger mạnh + quy tắc cứng + script; chi tiết ủy quyền cho reference plugin vbhc-vn); bổ sung vụ sai thứ 3 (2861/SYT-NVY 19/6/2026); bỏ tham chiếu chết anti-error-sct-vn; lệnh fallback sang script trong plugin; script giữ nguyên (giống từng byte bản plugin — quy ước sửa là sửa cả 2 nơi).

## 2026-07-06 (đợt 2) — kccn-sct-vn v1.3.0: cập nhật 03 KCN được chấp thuận CTĐT
- Thêm `references/15-kcn-chap-thuan-ctdt-2026.md`: KCN Bản Qua (QĐ 2170/QĐ-UBND 23/6/2026, 76,39 ha, GCN ĐKĐT 30/6/2026); KCN Phú Xuân (QĐ 2336) và Phú Xuân 1 (QĐ 2338) cùng ngày 02/7/2026, NĐT Công ty CP công nghiệp Linh Linh, xã Gia Phú → tổng 10 KCN đã thành lập/có QĐ CTĐT.
- Cập nhật reference 12, 14 phản ánh trạng thái mới; bổ sung 4 văn bản gốc đã ký vào `van-ban-goc/`.

## 2026-07-06 — Thêm plugin kccn-sct-vn v1.2.0 (merge dữ liệu tra cứu từ skill kcn-ccn-vn)
- **Thêm mới lên repo**: plugin `kccn-sct-vn` v1.2.0 (trước đó v1.1.0 chỉ upload trực tiếp lên Claude, chưa có trên repo). Cấu trúc chuẩn gói `<tên>/.claude-plugin/plugin.json` + `<tên>/skills/<tên>/`.
- **Merge từ skill cũ kcn-ccn-vn**: reference 13 mới (toàn văn Phụ lục II — 20 KCN + Phụ lục III — 54 CCN đủ 6 nhóm của QĐ 525/QĐ-UBND 25/02/2026; đối soát 54/56/52 CCN; tầm nhìn 2050); reference 14 mới (QĐ 1382/QĐ-UBND 23/4/2026: 431 danh mục, chi tiết 13 KCN + 35 CCN kèm TMĐT, nhà đầu tư, suất vốn QĐ 425/QĐ-BXD).
- **Sửa lỗi nghiêm trọng reference 12**: vị trí xã 6 KCN sai do suy từ tên KCN (Bản Qua→xã Bát Xát; Y Can→Lương Thịnh+Quy Mông; Đông An→Đông Cuông; Thịnh Hưng→Yên Bình+phường Văn Phú; Lục Yên→Lục Yên+Tân Lĩnh; Cốc Mỳ-Trịnh Tường→Trịnh Tường); bổ sung KCN Việt Hồng 2 (200 ha) bị thiếu; chốt CCN Y Can (Quy Mông), Đông An (Đông Cuông), Bảo Hưng 2 (phường Âu Lâu). Thêm quy tắc "KHÔNG suy tên xã từ tên KCN".
- **Chủ đích không merge**: dữ liệu hiện trạng lấp đầy/tiến độ (ref 15, 18 skill cũ) — giữ nguyên tắc hỏi người dùng. Skill `kcn-ccn-vn` giữ lại trên repo làm nguồn lưu trữ; trên Claude nên tắt sau khi v1.2.0 chạy ổn.

## 2026-07-05 (đợt 2) — Đưa 6 plugin lên repo + chuẩn hóa kiểu lưu "gói trong thư mục"
- **Chuẩn hóa cấu trúc repo**: mỗi plugin nay lưu dạng `<tên>/.claude-plugin/plugin.json` + `<tên>/skills/<tên>/...` (zip lại từng thư mục là ra file upload được ngay, không phải bọc thủ công — tránh lỗi validation upload). Chuyển `vbhc-vn` và `hnh-sct-vn` từ kiểu phẳng cũ sang kiểu gói.
- **Thêm mới**: hc-sct-vn v1.0.1, xd-sct-vn v1.1.0, hl-vlncn-sct-vn v1.0.0, sd-vlncn-sct-vn v2026.7.4.2, kho-vlncn-sct-vn v1.4.0.
- **Cập nhật**: hnh-sct-vn → v1.1.0 (thẩm quyền loại 5+8 theo TT 26/2026); vbhc-vn giữ v2.0.1.
- Nắn lại 2 gói bị bọc lệch (hc-sct-vn, sd-vlncn-sct-vn) về đúng chuẩn; dọn __pycache__/.DS_Store.

## 2026-07-05 — vbhc-vn: nâng cấp v2.0.0 → v2.0.1 (chuẩn plugin + vá SZ13 tận gốc)
- **v2.0.0**: chuyển chuẩn plugin; 4 quy tắc bất biến mới (11: cấm gán run.text vào run neo shape Line; 12: dòng Số/Ngày 13pt tường minh, ngày in nghiêng; 13: cấm widow word; 14: khối ký không gãy trang); nâng 7 → 8 nhóm anti-error; thêm `scripts/qa_pdf_check.py` (QA tự động 4 kiểm tra); sửa CỘNG HOÀ→CỘNG HÒA + en dash tiêu ngữ 4 template; chèn Line thiếu vào template 07; check_document bổ sung 10 VBQPPL hết hiệu lực; đổi tên 2 file reference bỏ dấu cách; thêm CHANGELOG riêng của plugin.
- **v2.0.1**: `fill_template.py` gán text vào run chủ đạo (text dài nhất) giữ 13pt tường minh khi điền template; vá 7/9 template gốc thiếu `w:sz=26` ở dòng Số/Ngày (01,02,03,04,05,07,08); `qa_pdf_check.py` guard đầu vào .docx báo lỗi thân thiện khi truyền nhầm PDF; rút gọn demo công văn cho khối ký trọn trang 1. Kiểm chứng: 3 demo → 3/3 QA PASS, render soi ảnh đạt thể thức.

## 2026.07.02 — Khởi tạo kho + đợt cập nhật từ rà soát tuần 30/6–2/7
- **vbhc-vn**: nâng 5 → 7 nhóm sai lầm (thêm Nhóm F — không rebuild file người dùng tải lên; Nhóm G — thể thức chi tiết từ chỉnh sửa tay); thêm `reference/cong-cu-ky-thuat.md` (RAR/OCR/docx/QA); rút gọn description dưới 1024 ký tự.
- **kcn-ccn-vn**: thêm `references/18-hien-trang-cap-nhat.md` (file hiện trạng động có dấu thời gian + bảng mốc hạn); quy tắc 7 mới về sử dụng hiện trạng; nguyên tắc xử lý song song CCN chưa có QĐ thành lập (7b); ĐVSNCL làm chủ đầu tư hạ tầng (7c).
- **hnh-sct-vn**: cảnh báo PGĐ ký KT. GĐ theo ủy quyền đích danh QĐ 1696 + yêu cầu Điều 14 Luật 72/2025 (ref 01); tiền lệ Phương Nam xe biển Trung Quốc / giấy phép loại D NĐ 158/2024 (ref 07); checklist rà dự thảo Giấy phép mục 7b (ref 03).

## 2026-07-04 — vbhc-vn
- Bổ sung VĂN BẢN GỐC 3 Phụ lục Nghị định 30/2020/NĐ-CP vào `reference/`:
  - `nd30-phu-luc-1-the-thuc.md`: Phụ lục I — thể thức, kỹ thuật trình bày VBHC và bản sao (cỡ chữ, kiểu chữ, sơ đồ ô, bảng mẫu chữ Mục V).
  - `nd30-phu-luc-2-viet-hoa.md`: Phụ lục II — quy tắc viết hoa trong VBHC.
  - `nd30-phu-luc-3-viet-tat-mau.md`: Phụ lục III — bảng chữ viết tắt tên loại văn bản + mô tả mẫu trình bày.
- SKILL.md: thêm chỉ dẫn tra 3 file trên (khi nào đọc file nào), rút gọn description ≤1024 ký tự, bổ sung trigger về thể thức/viết hoa/viết tắt theo NĐ 30/2020.
- Không đưa Phụ lục IV–VI (quản lý văn bản, lập hồ sơ, tài liệu điện tử) — ngoài phạm vi soạn thảo.

## 24/7/2026
- **qlks-sct-vn v1.3.0**: chắt lọc CV 6987/SNNMT-KS ngày 23/7/2026 (nghĩa vụ sau cấp phép — mỏ đất hiếm khu vực Bến Đền, xã Gia Phú và xã Bảo Thắng, GP 197/GP-BNNMT ngày 13/7/2026 của Bộ trưởng Bộ NNMT, Công ty CP Công nghiệp Khánh An, tổng oxit đất hiếm TR2O3 không bao gồm CeO2): reference 07 mục VI nay có 2 tiền lệ cùng khuôn (CV 6795 + CV 6987) xác nhận quy trình lặp của SNNMT; reference 10 mục I-b thêm GP 197 (mỏ đất hiếm thứ 2 toàn tỉnh); reference 09 cập nhật danh mục; văn bản gốc 21 → 22 file.
- **tkm-sct-vn v1.3.0**: reference 03 thêm mục 6 "Mỏ nhóm I mới cấp phép — chủ động chuẩn bị tiếp nhận hồ sơ" (quặng sắt Quý Xa GP 199 + đất hiếm Bến Đền GP 197) kèm GATE sau 01/7/2026 (CQCM chỉ thẩm định BCNCKT theo NĐ 217/2026; thiết kế sau TKCS chủ đầu tư tự thẩm định, phê duyệt rồi gửi cơ quan QLNN theo K2, K3 Đ77 NĐ 193/2025 — SCT tiếp nhận, không thẩm định lại) và cảnh giới riêng mỏ đất hiếm chưa có tiền lệ tại SCT; tạo CHANGELOG.md riêng cho skill.
- **vbhc-vn v2.6.0**: thêm 2 mẫu vàng 24/7/2026 do người dùng ban hành: `cong-van-xin-y-kien-cac-co-quan-phuong-an-ccn-von-nsnn.docx` (xin ý kiến liên ngành: Kính gửi khối thụt lề nhóm theo loại cơ quan, deadline đậm, ghi chú gửi kèm nghiêng) và `cong-van-don-doc-tien-do-ha-tang-ccn-bao-cao-hang-tuan.docx` (đôn đốc nhiều DN: Kính gửi bảng "- Tên DN (tên CCN);", 3 mục đậm, chế tài Điều 12 NĐ 32/2024); làm rõ phạm vi Nhóm I: cấm câu "liên hệ Phòng..." chỉ với CV trả lời hồ sơ TTHC, còn CV quản lý ngành gửi nhiều đối tượng giữ câu đầu mối phản ánh qua Phòng.
- **vbhc-vn v2.5.0** (vụ thật Báo cáo CCN gửi BCT, người dùng sửa tay + soi Word): Nhóm H thêm **H5** — helper thay text dùng chung phải kiểm run chứa shape (xpath w:pict|w:drawing) và assert số pict file xuất == file gốc; bước "khử gen lỗi mẫu thật" bắt buộc trước khi giao (đánh lại o:spid duy nhất từng v:line, xóa hanging indent ô header, w:lang → vi-VN, bỏ trHeight cố định bảng ký). Nhóm G thêm 3 quy tắc: Kính gửi 1 nơi nhận = 1 dòng căn giữa, không bảng, không chấm cuối (nhiều nơi = khối thụt lề 1701/708 + 2268); báo cáo gửi Bộ thêm Cục chuyên môn chủ trì vào Nơi nhận và ghi "- Ban Giám đốc Sở;"; ô Nơi nhận bảng ký ≥ ~3260 dxa khi tên cơ quan dài.
- **hnh-sct-vn v1.5.0**: bổ sung nguyên tắc 15 (văn phong công văn gửi doanh nghiệp - 2 quy tắc bất biến), 16 (đối chiếu môi chất bồn chứa với hàng xin phép), 17 (xe biển Việt Nam, SMRM không quy định niên hạn); reference 16 thêm mục 7; thêm ví dụ thực tế `tu-van-ky-thuat-nh3-072026/` (biên bản thẩm định + CV bản chuẩn văn phong).
- **vbhc-vn v2.3.0**: thêm **Nhóm I** vào bộ anti-error (nay 9 nhóm) - văn phong công văn gửi doanh nghiệp: không nêu mốc hiệu lực giấy tờ DN chưa vi phạm; bỏ câu "đề nghị liên hệ Phòng ... để được hướng dẫn".
