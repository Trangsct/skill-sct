---
name: quy-hoach-ct-vn
description: "Cẩm nang quy hoạch 04 ngành Công Thương tỉnh Lào Cai: KHOÁNG SẢN, ĐIỆN/NĂNG LƯỢNG, KHU CÔNG NGHIỆP (KCN), CỤM CÔNG NGHIỆP (CCN). Dùng khi: xác định một dự án nguồn điện/lưới điện/mỏ khoáng sản/KCN/CCN có trong quy hoạch không và thuộc quyết định nào; tra danh mục thủy điện, điện sinh khối/gió/mặt trời/rác, trạm biến áp - đường dây 500-220-110kV; tra khu vực thăm dò - khai thác - chế biến khoáng sản nhóm I/II/III/IV (apatit, đồng, sắt, đất hiếm, graphit, VLXDTT); tham gia ý kiến, rà soát, soạn báo cáo/công văn/tờ trình về điều chỉnh quy hoạch tỉnh, quy hoạch điện, quy hoạch khoáng sản, KCN/CCN; xác định quan hệ giữa Quy hoạch điện VIII và Quy hoạch khoáng sản quốc gia với Quy hoạch tỉnh. Tra: QĐ 525/QĐ-UBND 25/02/2026, QĐ 768/QĐ-TTg 15/4/2025 (Quy hoạch điện VIII), QĐ 866/QĐ-TTg 18/7/2023, QĐ 1626/QĐ-TTg 15/12/2023. Từ khoá: quy hoạch điện VIII, QĐ 768, nguồn điện, thủy điện, TBA, đường dây, đấu nối, công suất MW; QĐ 866, apatit, đồng, đất hiếm, graphit, VLXDTT; Phụ lục II III QĐ 525, Tằng Loỏng, Bát Xát."
---

# quy-hoach-ct-vn — Cẩm nang quy hoạch ngành Công Thương tỉnh Lào Cai

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

### 2. Quy hoạch ngành quốc gia (cấp trên, ràng buộc tỉnh)

| Văn bản | Lĩnh vực | Tình trạng |
|---|---|---|
| **QĐ 768/QĐ-TTg ngày 15/4/2025** | **Điều chỉnh Quy hoạch điện VIII** (phát triển điện lực quốc gia 2021-2030, tầm nhìn 2050) | Hiệu lực kể từ ngày ký; thay thế QĐ 500/QĐ-TTg ngày 15/5/2023. Ký: KT. Thủ tướng - PTT Bùi Thanh Sơn. **Xem ref 02** |
| **QĐ 866/QĐ-TTg ngày 18/7/2023** | Quy hoạch thăm dò, khai thác, chế biến, sử dụng các loại **khoáng sản** (nhóm I; trừ dầu khí, than, phóng xạ, VLXD, phân tán nhỏ lẻ) | Hiệu lực kể từ ngày ký; PTT Trần Hồng Hà ký. Đang rà soát điều chỉnh (KH thực hiện QĐ 333/QĐ-TTg 23/4/2024). **Xem ref 04** |
| **QĐ 1626/QĐ-TTg ngày 15/12/2023** | Quy hoạch thăm dò, khai thác, chế biến, sử dụng khoáng sản **làm vật liệu xây dựng** (nhóm II) | **Xem ref 04** |
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
| `references/01-he-thong-quy-hoach.md` | Khi giải thích hệ thống quy hoạch, mối quan hệ quốc gia–vùng–tỉnh–ngành; vai trò Sở Công Thương trong lập/điều chỉnh quy hoạch; nguyên tắc tích hợp |
| `references/02-qh-dien-viii-qd768.md` | Khi cần quan điểm, mục tiêu, cơ cấu nguồn điện quốc gia, lưới truyền tải theo QĐ 768; các chỉ tiêu công suất, điện thương phẩm, tỷ lệ NLTT toàn quốc |
| `references/03-dien-lao-cai.md` | NGUỒN CHI TIẾT về điện Lào Cai: hiện trạng nguồn/lưới + **danh mục phương án** nguồn điện (thủy điện, sinh khối, gió, mặt trời, rác), TBA & đường dây 500/220/110kV theo Báo cáo QHT (Bảng 32-43). Dùng khi tra một dự án cụ thể, lập danh mục, đối chiếu đấu nối |
| `references/04-khoang-san.md` | NGUỒN CHI TIẾT về khoáng sản: phân nhóm I-IV, thẩm quyền quy hoạch; khu vực thăm dò–khai thác Lào Cai (apatit, đồng, sắt, đất hiếm, graphit, đá hoa trắng, kaolin); VLXDTT; QĐ 866, 1626, Luật ĐCKS 2024 |
| `references/05-kcn-ccn-quy-hoach.md` | Khi tra danh mục, vị trí xã, diện tích KCN (Phụ lục II) và CCN (Phụ lục III) theo QĐ 525. **Trỏ sang `kcn-ccn-vn`** cho thành lập, cấp phép, chấm điểm chủ đầu tư |
| `references/06-cau-truc-bao-cao-qht.md` | Khi soạn/rà soát/góp ý báo cáo thuyết minh quy hoạch tỉnh hoặc phương án phát triển ngành; cấu trúc chuẩn của Báo cáo điều chỉnh QHT |
| `references/07-dieu-chinh-qd866-lao-cai.md` | Khi cần **danh mục mỏ nhóm I cụ thể trên địa bàn Lào Cai** (đồng Sin Quyền/Tả Phời/Vi Kẽm/Khe Cam, sắt Quý Xa/Kíp Tước, đất hiếm Yên Phú, graphit Bảo Hà/Nậm Thi); QĐ 2581/QĐ-TTg (Tả Phời, đã ký) và dự thảo điều chỉnh QĐ 866 (3/2026, chưa ký) |
| `references/08-toa-do-tham-do-che-bien-lao-cai.md` | Khi cần **tọa độ khép góc**, danh mục **thăm dò (Phụ lục II)**, **chế biến (Phụ lục IV)** các mỏ Lào Cai; hướng dẫn tra file nguồn gốc cho số liệu chính xác |

## IV. FILE NGUỒN GỐC ĐỂ TRA CỨU CHÍNH XÁC (`sources/`)

Thư mục **`sources/`** chứa **toàn văn các văn bản gốc** (text trích từ PDF/DOCX) để tra cứu đầy đủ, chính xác — không chỉ dựa vào reference tóm tắt. Xem mục lục `sources/00-MUC-LUC-NGUON.md`.

**Khi nào mở file nguồn:** bất kỳ lúc nào cần số liệu/danh mục/tọa độ CHÍNH XÁC để đưa vào văn bản (ví dụ: tọa độ khép góc một mỏ, công suất một dự án điện, trữ lượng một khoáng sản). Reference (ref 02-08) cho khung và phần Lào Cai trích sẵn; file nguồn cho chi tiết toàn văn.

**Cách tra:** grep theo **TÊN MỎ + TÊN XÃ** hoặc **tên dự án điện** (KHÔNG theo số phụ lục — chỉ số không nhất quán), rồi đọc khối xung quanh. Ví dụ:
```bash
grep -n -i "quý xa\|tả phời" sources/qd866-dieuchinh-2026-phuluc.txt
```
File hiện có: `qd866-dieuchinh-2026-thuyetminh.txt` và `...phuluc.txt` (DỰ THẢO 3/2026), `qd768-quyhoach-dien-viii-toanvan.txt` (ĐÃ KÝ), `qht-laocai-2026-baocao-thuyetminh.txt` và `...phuluc.txt` (bản thao tác QHT Lào Cai 7/6/2026, tích hợp cả 04 ngành). Có thể bổ sung file nguồn mới theo hướng dẫn trong mục lục.

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

8. **Nguyên tắc trích dẫn.** Trong văn bản hành chính ghi đầy đủ "Quyết định số 768/QĐ-TTg ngày 15 tháng 4 năm 2025 của Thủ tướng Chính phủ phê duyệt Điều chỉnh Quy hoạch phát triển điện lực quốc gia thời kỳ 2021-2030, tầm nhìn đến năm 2050". Tránh viết tắt "QH điện VIII", "QĐ 866" trong văn bản chính thức (chỉ dùng nội bộ).

## VI. NGƯỜI KÝ MẶC ĐỊNH CHO VĂN BẢN VỀ QUY HOẠCH NGÀNH

(Phối hợp skill `sct-laocai-org-vn` và `vbhc-vn`)

| Loại văn bản | Người ký mặc định |
|---|---|
| Báo cáo/Tờ trình tổng thể quy hoạch ngành gửi UBND tỉnh, Tỉnh uỷ | Giám đốc Hoàng Chí Hiền |
| Công văn tham gia ý kiến quy hoạch điện, lưới điện, năng lượng | KT. Giám đốc - PGĐ Hoàng Văn Thuân (phụ trách năng lượng) |
| Công văn tham gia ý kiến quy hoạch khoáng sản, VLNCN | KT. Giám đốc - PGĐ Hoàng Văn Thuân (phụ trách khoáng sản) |
| Công văn tham gia ý kiến quy hoạch KCN, CCN | KT. Giám đốc - PGĐ Nguyễn Đình Chiến (phụ trách KCN, CCN) |
| Phiếu góp ý nội bộ, công văn nghiệp vụ Phòng QLCN | Theo lĩnh vực: PGĐ phụ trách tương ứng |

Dòng "Lưu: VT, CN(...)": tra bảng phân công chuyên viên Phòng QLCN trong skill `sct-laocai-org-vn`. Lĩnh vực KCN/CCN và tham gia ý kiến dự án công nghiệp → **CN(Trung)**; lĩnh vực điện/khoáng sản → theo chuyên viên phụ trách.
