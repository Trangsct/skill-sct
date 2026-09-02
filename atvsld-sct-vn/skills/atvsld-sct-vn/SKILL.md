---
name: atvsld-sct-vn
description: "AN TOÀN, VỆ SINH LAO ĐỘNG (ATVSLĐ) phần ngành Công Thương, Sở Công Thương Lào Cai. Kích hoạt: an toàn lao động, vệ sinh lao động, ATVSLĐ, ATLĐ, máy thiết bị vật tư chất có yêu cầu nghiêm ngặt, thiết bị áp lực, nồi hơi, bình chịu áp lực, thiết bị nâng đặc thù công nghiệp, kiểm định kỹ thuật an toàn lao động, khai báo sử dụng máy thiết bị, huấn luyện ATVSLĐ nhóm 1-6, thẻ an toàn, tai nạn lao động, sự cố kỹ thuật gây mất an toàn, điều tra tai nạn, Hội đồng ATVSLĐ tỉnh, Tháng hành động ATVSLĐ, Luật 84/2015, NĐ 283/2026 (hiệu lực 10/9/2026, thay NĐ 12/2022), NĐ 39/2016, NĐ 44/2016, Sở Nội vụ. 6 nghiệp vụ: (1) xác định máy/thiết bị/chất thuộc trách nhiệm Bộ Công Thương (điểm d k1 Đ33 Luật) và ranh giới Sở CT - Sở Nội vụ - Sở Y tế - xã; (2) hướng dẫn DN khai báo, kiểm định, hồ sơ kỹ thuật, huấn luyện; (3) tai nạn lao động, sự cố kỹ thuật trong mỏ, VLNCN, hóa chất, điện: tham gia điều tra, báo cáo; (4) kiểm tra ATVSLĐ lồng ghép kiểm tra chuyên ngành; (5) xử phạt: NĐ 283/2026 Sở CT CHUYỂN Sở Nội vụ; hành vi KTAT mỏ, VLNCN, hóa chất Sở XỬ theo NĐ 36/2020, 275/2026; (6) báo cáo, Tháng hành động, Hội đồng. Từ khóa thêm: QCVN, PTBVCN, quan trắc môi trường lao động, bệnh nghề nghiệp, CN(Linh), PGĐ Thuân."
---

# atvsld-sct-vn — ATVSLĐ phần ngành Công Thương, Sở Công Thương Lào Cai

> **GATE PDF (áp dụng mọi plugin nghiệp vụ):** nhận PDF văn bản nhà nước → chạy `python3 "/mnt/skills/plugins/vbhc-vn:vbhc-vn/scripts/extract_metadata.py" "<file.pdf>"` TRƯỚC khi dẫn số/ngày/người ký. Context trống "Số: /…", "ngày … tháng …" là PDF ký số, KHÔNG phải bản dự thảo (vụ QĐ 5116/QĐ-SCT 02/9/2026). Chi tiết: plugin `vbhc-pdf-reader-vn`.

## I. KHI NÀO DÙNG — và khi nào KHÔNG

**Dùng** khi câu hỏi về ATVSLĐ liên quan đến cơ sở công nghiệp, thương mại thuộc quản lý của Sở Công Thương (mỏ, nhà máy hóa chất, kho VLNCN, nhà máy luyện kim, thủy điện, xăng dầu – khí, CCN…) hoặc về máy, thiết bị, vật tư, chất có yêu cầu nghiêm ngặt về ATVSLĐ thuộc trách nhiệm Bộ Công Thương.

**Không dùng / chuyển plugin khác:**
- Huấn luyện, cấp GCN kỹ thuật an toàn **VLNCN, tiền chất thuốc nổ** → `hl-vlncn-sct-vn`; huấn luyện an toàn **hóa chất** → `hc-sct-vn`.
- Kiểm tra thiết kế – nghiệm thu **kho VLNCN** → `kho-vlncn-sct-vn`; thiết kế mỏ, KTAT khai thác mỏ (Đ55–62 NĐ 36/2020) → `tkm-sct-vn`, `qlks-sct-vn`, `xp-sct-vn`.
- Xử phạt VPHC (biên bản, quyết định, thẩm quyền chi tiết, thời hạn) → `xp-sct-vn` (ref 07 mục ATVSLĐ đã liên kết về đây).
- Quan hệ lao động, tiền lương, BHXH, người lao động nước ngoài: **không thuộc Sở Công Thương** (Sở Nội vụ) — chỉ trả lời ranh giới, không tham mưu nội dung.

## II. RANH GIỚI THẨM QUYỀN — đọc trước khi trả lời bất kỳ câu nào (bản gốc: `references/01`)

| Việc | Cơ quan | Căn cứ nguyên văn |
|---|---|---|
| QLNN chung về ATVSLĐ tại địa phương; **thanh tra, kiểm tra, xử lý vi phạm** ATVSLĐ | UBND tỉnh; cơ quan QLNN về lao động cấp tỉnh = **Sở Nội vụ** (từ 01/3/2025 nhận nhiệm vụ Sở LĐTBXH) | Đ86, Đ89 Luật 84/2015; Đ54 k2, Đ61 k1, Đ63 k8 NĐ 283/2026 |
| QLNN đối với **máy, thiết bị, vật tư, chất có yêu cầu nghiêm ngặt** liên quan **thiết bị áp lực, thiết bị nâng đặc thù chuyên ngành công nghiệp, hóa chất, VLNCN, trang thiết bị khai thác mỏ, dầu khí** (trừ thiết bị thăm dò, khai thác trên biển) | **Bộ Công Thương** → tại tỉnh: **Sở Công Thương** (cơ quan chuyên môn tương ứng) | **điểm d k1 Đ33** Luật 84/2015; k2 Đ30 (khai báo với cơ quan chuyên môn cấp tỉnh "theo thẩm quyền quy định tại khoản 1 và khoản 2 Điều 33") |
| Máy, thiết bị trong **thi công xây dựng** | Bộ/Sở Xây dựng | điểm đ k1 Đ33 |
| Danh mục máy, thiết bị nghiêm ngặt; danh mục công việc nghiêm ngặt | Bộ trưởng LĐTBXH (nay Bộ Nội vụ) ban hành trên cơ sở đề nghị các bộ | k2 Đ28; k6 Đ14 |
| Khai báo tai nạn chết người / ≥2 người bị thương nặng | NSDLĐ khai báo **cơ quan QLNN về lao động cấp tỉnh** (+ Công an); sự cố trong **dầu khí, phóng xạ, vận tải, LLVT** theo luật chuyên ngành | điểm b, c k1 Đ34 |
| Điều tra TNLĐ cấp tỉnh | Trưởng đoàn = thanh tra chuyên ngành ATVSLĐ cấp tỉnh; thành viên Sở Y tế, LĐLĐ và "một số thành viên khác" → **Sở Công Thương tham gia** khi tai nạn trong mỏ, VLNCN, hóa chất, điện (theo mời) | k2 Đ35 |
| Thanh tra ATVSLĐ trong **dầu khí, phóng xạ, vận tải, LLVT** | cơ quan QLNN lĩnh vực đó, phối hợp thanh tra ATVSLĐ | k2 Đ89 |
| **Xử phạt** ATVSLĐ (Đ31–38 NĐ 283/2026) | Chủ tịch UBND xã 37,5 tr / tỉnh 75 tr; **Giám đốc Sở Nội vụ 60 tr**; Công an một số điểm; **Sở Công Thương: KHÔNG có tên** ở Đ54 (lập biên bản) lẫn Đ55–62 (xử phạt) | Đ54, 55, 61, 63 NĐ 283/2026 |

⚠️ **Khai báo máy, thiết bị nghiêm ngặt — mâu thuẫn văn bản, hỏi Bạn thực tiễn Lào Cai trước khi hướng dẫn DN:** k2 Đ30 Luật nói khai báo với cơ quan chuyên môn cấp tỉnh **theo thẩm quyền Đ33** (thiết bị nhóm Công Thương → Sở Công Thương), nhưng **k1 Đ35 NĐ 283/2026** phạt hành vi "không khai báo với **Sở Nội vụ** tại địa phương trong 30 ngày kể từ ngày đưa vào sử dụng". NĐ 44/2016 (chưa có bản gốc) quy định thủ tục cụ thể. Khi trả lời: nêu cả hai căn cứ, đề nghị DN khai báo với Sở Nội vụ **và** gửi Sở Công Thương biết đối với thiết bị nhóm Công Thương — không kết luận một chiều.

## III. SÁU NGHIỆP VỤ

1. **Xác định thiết bị/chất thuộc nhóm Công Thương và ranh giới** — `references/02`. Trả lời theo cặp (thiết bị → điểm d k1 Đ33 → có/không thuộc Sở CT); danh mục cụ thể theo TT của Bộ (chưa có bản gốc → GATE, không tự liệt kê mã thiết bị).
2. **Hướng dẫn doanh nghiệp**: khai báo (k2 Đ30), kiểm định trước khi đưa vào sử dụng và định kỳ bởi tổ chức kiểm định (k1 Đ31), hồ sơ kỹ thuật an toàn (k3 Đ30), huấn luyện 6 nhóm và thẻ an toàn (Đ14), phương án bảo đảm ATVSLĐ khi xây mới/mở rộng (Đ29) — `references/02`, `05`. Nơi nộp TTHC (nếu là thủ tục của Sở): https://motcua-tthc.moit.gov.vn/ (duy nhất, đăng nhập VNeID).
3. **Tai nạn lao động, sự cố kỹ thuật** trong cơ sở ngành Công Thương: khai báo (Đ34), điều tra (Đ35), thống kê – báo cáo (Đ36); quan hệ với sự cố hóa chất (`hc-sct-vn`), sự cố VLNCN (`sd-vlncn-sct-vn`), sự cố mỏ (`qlks-sct-vn`) — `references/03`.
4. **Kiểm tra ATVSLĐ lồng ghép** vào kiểm tra chuyên ngành của Sở (NĐ 217/2025, TT 56/2025): nội dung kiểm tra máy thiết bị, huấn luyện, PTBVCN, quy chuẩn; phát hiện vi phạm Đ31–38 NĐ 283 → **biên bản làm việc + chuyển Sở Nội vụ** — `references/04`.
5. **Xử phạt**: Sở Công Thương **CHUYỂN** mọi hành vi NĐ 283/2026 (kể cả không kiểm định thiết bị nhóm Công Thương — Đ35) sang Sở Nội vụ/Chủ tịch UBND; hành vi **KTAT khai thác mỏ (Đ55–62 NĐ 36/2020), VLNCN, hóa chất (NĐ 275/2026)** Sở **XỬ** — ranh giới tại `references/04`; thủ tục tại `xp-sct-vn`.
6. **Báo cáo, Tháng hành động ATVSLĐ, Hội đồng ATVSLĐ tỉnh**: Sở CT báo cáo phần ngành theo yêu cầu Sở Nội vụ/UBND tỉnh (Đ86) — `references/06` (mẫu, kỳ hạn: hỏi Bạn vì chưa có văn bản của tỉnh trong plugin).

## IV. KHUNG PHÁP LÝ — chỉ 2 văn bản có bản gốc; còn lại là GATE

| Văn bản | Bản gốc | Dùng vào |
|---|---|---|
| **Luật ATVSLĐ 84/2015/QH13** ngày 25/6/2015 (hiệu lực 01/7/2016) | ✅ `van-ban-goc/` (.docx + .txt) | Đ14, 28–36, 82–89 — `references/01`, `02`, `03` |
| **NĐ 283/2026/NĐ-CP** ngày 15/7/2026 — xử phạt lao động, BHXH, NLĐ đi làm việc ở nước ngoài; **hiệu lực 10/9/2026**; thay NĐ 12/2022 (k4 Đ66); chuyển tiếp Đ67 | ✅ `van-ban-goc/` | Đ3 thời hiệu 01 năm; Đ7 mức cá nhân, tổ chức ×2; Đ31–38; Đ54–63 — `references/04` |
| NĐ 39/2016/NĐ-CP (chi tiết Luật ATVSLĐ: điều tra TNLĐ, khai báo, thống kê), NĐ 44/2016/NĐ-CP (kiểm định, huấn luyện, quan trắc; sđ NĐ 140/2018), TT 36/2019/TT-BLĐTBXH (danh mục máy thiết bị nghiêm ngặt), TT 06/2020/TT-BLĐTBXH (danh mục công việc nghiêm ngặt), TT 09/2017/TT-BCT (kiểm định KTAT thuộc Bộ Công Thương), QCVN thiết bị áp lực – thiết bị nâng của BCT/BLĐTBXH | ❌ **chưa có** | **GATE: chỉ nêu tên văn bản, KHÔNG dẫn điều khoản, mức, mã thiết bị cho đến khi Bạn cung cấp bản gốc** |

Sau sắp xếp bộ máy 2025: "Bộ Lao động – Thương binh và Xã hội" trong Luật 84/2015 → Bộ Nội vụ; "Sở LĐTBXH" → **Sở Nội vụ** (NĐ 283/2026 đã dùng tên mới). Khi trích Luật giữ nguyên văn và chú thích "(nay là …)".

## V. QUY TẮC BẤT BIẾN

1. **Không tự liệt kê danh mục thiết bị/mã kiểm định** khi chưa có bản gốc TT 36/2019, TT 09/2017 — nói "thuộc nhóm thiết bị áp lực/nâng đặc thù công nghiệp theo điểm d k1 Đ33" là đủ, phần danh mục ghi GATE.
2. **Sở Công Thương không lập biên bản VPHC, không ra QĐ xử phạt theo NĐ 283/2026** — kết luận này lấy từ nguyên văn Đ54, Đ61, Đ63; muốn khác phải có văn bản giao (như QĐ 5116/QĐ-SCT cho khoáng sản) mà NĐ 283 cũng không có "cửa" cho công chức Sở CT như Đ69 NĐ 36 → không đề xuất soạn QĐ giao cho ATVSLĐ.
3. Người ký: **KT. GIÁM ĐỐC – PHÓ GIÁM ĐỐC Hoàng Văn Thuân** (an toàn ngành, ATVSLĐ, máy – thiết bị nghiêm ngặt); chuyên viên **CN(Linh)**; PTP kiểm duyệt **Trang** → TP Long (theo `sct-laocai-org-vn`). Báo cáo trọng yếu gửi UBND tỉnh: GIÁM ĐỐC Hoàng Chí Hiền.
4. Thời hiệu ATVSLĐ **01 năm** (điểm a k4 Đ3 NĐ 283) — khác khoáng sản/môi trường 02 năm; hành vi "không kiểm định", "không khai báo" là hành vi đang thực hiện cho đến khi chấm dứt (k5 Đ3 dẫn k1 Đ8 NĐ 118).
5. Mức phạt NĐ 283 là **mức cá nhân, tổ chức ×2** (k1 Đ7), trừ các khoản liệt kê tại k1 Đ7 là mức tổ chức (gồm k2, 4 Đ36; k1 Đ37; k1, 5–8 Đ38 — tổ chức huấn luyện, tổ chức kiểm định, quan trắc).
6. Thể thức văn bản theo `vbhc-vn` (Quốc hiệu "CỘNG HÒA", tiêu ngữ en dash, Số/ngày 13pt, 2 Line, Kính gửi không đậm); nơi nộp TTHC duy nhất https://motcua-tthc.moit.gov.vn/.
7. Mọi số/ngày văn bản của tỉnh (Hội đồng ATVSLĐ, kế hoạch Tháng hành động, phân công điều tra TNLĐ) — **hỏi Bạn**, không bịa.

## VI. CẤU TRÚC PLUGIN

```
atvsld-sct-vn/
├── .claude-plugin/plugin.json
└── skills/atvsld-sct-vn/
    ├── SKILL.md
    ├── CHANGELOG.md
    ├── references/
    │   ├── 01-khung-phap-ly-ranh-gioi.md       ← Luật 84/2015 nguyên văn Đ28–36, 82–89; NĐ 283 Đ54–63; ranh giới 4 cơ quan
    │   ├── 02-may-thiet-bi-nghiem-ngat-bct.md  ← điểm d k1 Đ33; khai báo, kiểm định, hồ sơ kỹ thuật; mâu thuẫn k2 Đ30 ↔ k1 Đ35 NĐ 283
    │   ├── 03-tai-nan-lao-dong-su-co.md        ← Đ34–36; vai trò Sở CT; liên hệ sự cố hóa chất/VLNCN/mỏ
    │   ├── 04-xu-phat-nd-283-2026.md           ← thời hiệu, mức, Đ31–38 bảng hành vi, thẩm quyền, XỬ/CHUYỂN
    │   ├── 05-huan-luyen-atvsld.md             ← Đ14 Luật; 6 nhóm; ranh giới với huấn luyện KTAT VLNCN/hóa chất
    │   └── 06-bao-cao-thang-hanh-dong-hoi-dong.md ← Đ86; báo cáo phần ngành; Hội đồng; Tháng hành động (GATE thực tiễn)
    └── van-ban-goc/
        ├── INDEX.md
        ├── Luat-84-2015-QH13-An-toan-ve-sinh-lao-dong.docx (+ .txt)
        └── ND-283-2026-NDCP-xu-phat-lao-dong-BHXH-NLD-di-lam-viec-nuoc-ngoai.docx (+ .txt)
```
