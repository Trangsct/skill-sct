# 00 — MỤC LỤC VĂN BẢN GỐC (`van-ban-goc/`)

Bản gốc (DOCX toàn văn) các văn bản **công khai cấp trung ương** mà plugin viện dẫn. Khác với `sources/`
(text trích từ PDF/DOCX, dùng để `grep`), thư mục này giữ **bản gốc để mở đọc và đối chiếu nguyên văn**.

> ⚠️ Chỉ đặt vào đây **văn bản quy phạm, văn bản chỉ đạo đã công bố** (gồm quyết định phê duyệt quy hoạch và hồ sơ quy hoạch đã công bố như QĐ 525). Dự thảo nội bộ, hồ sơ chưa ban hành,
> văn bản đi/đến của Sở → để ở kho riêng tư `vlncn-laocai`, KHÔNG đưa vào kho này (kho công khai).

| File | Văn bản | Người ký | Hiệu lực | Reference dùng |
|---|---|---|---|---|
| `NQ-10-NQ-TW-10-02-2022-...docx` | **NQ 10-NQ/TW ngày 10/02/2022** của Bộ Chính trị — định hướng chiến lược địa chất, khoáng sản và công nghiệp khai khoáng đến 2030, tầm nhìn 2045 | TBT Nguyễn Phú Trọng (T/M Bộ Chính trị) | từ ngày ban hành | ref **10** mục II |
| `NQ-88-NQ-CP-22-7-2022-...docx` | **NQ 88/NQ-CP ngày 22/7/2022** của Chính phủ — Chương trình hành động thực hiện NQ 10-NQ/TW (kèm danh mục 18 nhiệm vụ) | KT. TTg — PTT Lê Văn Thành | từ ngày ký | ref **10** mục III |
| `QD-334-QD-TTg-01-4-2023-...docx` | **QĐ 334/QĐ-TTg ngày 01/4/2023** — phê duyệt Chiến lược địa chất, khoáng sản và công nghiệp khai khoáng đến 2030, tầm nhìn 2045 | KT. TTg — PTT Trần Hồng Hà | từ ngày ký | ref **10** mục IV |
| `QD-154-QD-TTg-29-01-2022-...docx` | **QĐ 154/QĐ-TTg ngày 29/01/2022** — điều chỉnh kéo dài kỳ quy hoạch khoáng sản làm VLXD, khoáng sản làm xi măng | KT. TTg — PTT Lê Văn Thành | từ ngày ký; **đã hết vai trò** khi QĐ 1626/QĐ-TTg 15/12/2023 được phê duyệt | ref **10** mục V |
| `QD-2581-QD-TTg-24-11-2025-...docx` | **QĐ 2581/QĐ-TTg ngày 24/11/2025** — điều chỉnh QĐ 866 tại 3 khu vực: vonfram Núi Pháo (Thái Nguyên), **mỏ đồng Tả Phời (Lào Cai)**, bôxit Thọ Sơn + Thống Nhất (Đồng Nai). Kèm Phụ lục I, II, III | KT. TTg — PTT Trần Hồng Hà | từ ngày ký | ref **07** mục A, ref **08** |
| `QD-836-QD-BXD-14-10-2019-...docx` | **QĐ 836/QĐ-BXD ngày 14/10/2019** — Kế hoạch lập Quy hoạch thăm dò, khai thác, chế biến và sử dụng các loại khoáng sản làm VLXD thời kỳ 2021-2030, tầm nhìn 2050 (kèm biểu nội dung chi tiết) | Bộ trưởng Bộ Xây dựng Phạm Hồng Hà | từ ngày ký; **LỊCH SỬ** — quy hoạch tương ứng là QĐ 1626/QĐ-TTg 15/12/2023 | ref **10** mục V.2; ref **01** mục 5 |
| `2026.02.25-525.QD.UBND-Phe-duyet-dieu-chinh-Quy-hoach-tinh-Lao-Cai-2021-2030.pdf` (+`.txt` OCR) | **QĐ 525/QĐ-UBND ngày 25/02/2026** của Chủ tịch UBND tỉnh Lào Cai — phê duyệt điều chỉnh Quy hoạch tỉnh Lào Cai thời kỳ 2021-2030, tầm nhìn 2050; bản ký 119 trang kèm phụ lục (Phụ lục II KCN, III CCN). PDF nén 13 MB — chỉ trên GitHub, tra bằng `.txt` | Chủ tịch UBND tỉnh | từ ngày ký | ref **05**, **06**; `kccn-sct-vn` ref 13 |
| `2026.02.25-525.QD.UBND-Bao-cao-tong-hop-Quy-hoach-tinh-ban-hoan-thien-09.10.2026.pdf` (+`.txt`) | Báo cáo tổng hợp Quy hoạch tỉnh (điều chỉnh), bản hoàn thiện 09/10/2026, 1.011 trang — hồ sơ kèm QĐ 525 (Sở Tài chính phát hành theo BC 1156/BC-STC 30/9/2026). PDF 13 MB — chỉ trên GitHub; `.txt` 4 MB | — | theo QĐ 525 | ref **05** mục 5, ref **06** |
| `2026.02.25-525.QD.UBND-Bao-cao-tom-tat-Quy-hoach-tinh-ban-hoan-thien-09.10.2026.pdf` (+`.txt`) | Báo cáo tóm tắt Quy hoạch tỉnh (điều chỉnh), bản hoàn thiện 09/10/2026, 87 trang | — | theo QĐ 525 | ref **05**, **06** |

## Cách dùng

```bash
# đọc toàn văn một văn bản (DOCX → text)
python3 -c "
import zipfile
from xml.etree import ElementTree as ET
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
r=ET.fromstring(zipfile.ZipFile('QD-334-QD-TTg-01-4-2023-chien-luoc-dia-chat-khoang-san-cong-nghiep-khai-khoang-2030-2045.docx').read('word/document.xml'))
print('\n'.join(''.join(t.text or '' for t in p.iter(W+'t')) for p in r.iter(W+'p')))
"
```

Hoặc `grep` trên bản text đã trích sẵn trong `sources/` (xem `sources/00-MUC-LUC-NGUON.md`).
