# quy-hoach-ct-vn

Cẩm nang **quy hoạch 04 ngành Công Thương** trên địa bàn tỉnh Lào Cai: **khoáng sản, điện/năng lượng, KCN, CCN**. Trọng tâm là *lớp quy hoạch* — tra cứu danh mục, vị trí, quy mô, giai đoạn của dự án/mỏ/công trình theo các quyết định quy hoạch.

## Phạm vi & ranh giới với skill khác

- **Skill này:** quy hoạch tích hợp 04 ngành; danh mục nguồn/lưới điện, mỏ khoáng sản; tham gia ý kiến/rà soát quy hoạch.
- **`kcn-ccn-vn`:** thành lập, cấp phép, chấm điểm chủ đầu tư, điều kiện khởi công KCN/CCN.
- **`hnh-sct-vn`, `pccc-sct-vn`:** cấp phép, an toàn HHNH/hóa chất, PCCC.
- **`vbhc-vn`:** tạo file văn bản .docx đúng thể thức (bước cuối).
- **`sct-laocai-org-vn`:** phân công lãnh đạo, người ký, người soạn.

## Cấu trúc

```
quy-hoach-ct-vn/
├── SKILL.md                          # khung pháp lý + định tuyến + nguyên tắc
└── references/
    ├── 01-he-thong-quy-hoach.md      # hệ thống QH, vai trò Sở CT, tích hợp
    ├── 02-qh-dien-viii-qd768.md      # Quy hoạch điện VIII (QĐ 768) quốc gia
    ├── 03-dien-lao-cai.md            # danh mục nguồn/lưới điện Lào Cai (Bảng 32-43)
    ├── 04-khoang-san.md              # QĐ 866/1626, nhóm I-IV, khoáng sản Lào Cai
    ├── 05-kcn-ccn-quy-hoach.md       # lớp quy hoạch KCN/CCN (trỏ kcn-ccn-vn)
    ├── 06-cau-truc-bao-cao-qht.md    # cấu trúc Báo cáo QHT + checklist góp ý
    ├── 07-dieu-chinh-qd866-lao-cai.md # QĐ 2581 (Tả Phời — toàn văn, tọa độ 4 khu) + dự thảo điều chỉnh QĐ 866; danh mục mỏ Lào Cai
    ├── 08-toa-do-tham-do-che-bien-lao-cai.md # tọa độ khép góc, thăm dò, chế biến mỏ Lào Cai
    ├── 09-von-dtc-cap-dien-2026-2030.md # vốn đầu tư công cấp điện nông thôn (QĐ 2390/QĐ-UBND)
    └── 10-chu-truong-chien-luoc-khoang-san.md # NQ 10-NQ/TW, NQ 88/NQ-CP, QĐ 334 (Chiến lược), QĐ 154 (lịch sử)
sources/                              # TOÀN VĂN FILE GỐC để tra cứu chính xác
    ├── 00-MUC-LUC-NGUON.md           # mục lục + cách tra
    ├── qd866-dieuchinh-2026-thuyetminh.txt   # dự thảo điều chỉnh QĐ 866 (thuyết minh, 219tr)
    ├── qd866-dieuchinh-2026-phuluc.txt       # dự thảo điều chỉnh QĐ 866 (phụ lục, 449tr)
    ├── qd768-quyhoach-dien-viii-toanvan.txt  # QĐ 768 toàn văn (đã ký)
    ├── qd2581-dieuchinh-qd866-toanvan.txt    # QĐ 2581 toàn văn + PL I, II, III (đã ký)
    ├── qd334-chien-luoc-dckscnkk-toanvan.txt # QĐ 334 Chiến lược ĐC, KS, CN khai khoáng (đã ký)
    ├── nq10-nqtw-2022-toanvan.txt            # NQ 10-NQ/TW Bộ Chính trị (đã ban hành)
    ├── nq88-nqcp-2022-toanvan.txt            # NQ 88/NQ-CP + danh mục 18 nhiệm vụ (đã ký)
    ├── qd154-keodai-ky-qh-vlxd-ximang-toanvan.txt # QĐ 154 kéo dài kỳ QH VLXD, xi măng (lịch sử)
    ├── qht-laocai-2026-baocao-thuyetminh.txt # Báo cáo QHT Lào Cai 7/6/2026 (4 ngành tích hợp)
    └── qht-laocai-2026-phuluc.txt            # Phụ lục Báo cáo QHT Lào Cai 7/6/2026
van-ban-goc/                          # BẢN GỐC DOCX 05 văn bản trung ương về khoáng sản
    └── 00-MUC-LUC.md                 # mục lục + cách mở đọc
```

Cơ chế: `references/` cho khung + phần Lào Cai trích sẵn (tra nhanh); `sources/` cho toàn văn gốc (tra chính xác, đầy đủ khi đưa số vào văn bản). Có thể bổ sung file nguồn mới vào `sources/` theo hướng dẫn trong mục lục.

## Văn bản gốc tham chiếu

- QĐ 525/QĐ-UBND 25/02/2026 — Quy hoạch tỉnh Lào Cai.
- QĐ 768/QĐ-TTg 15/4/2025 — Điều chỉnh Quy hoạch điện VIII.
- QĐ 866/QĐ-TTg 18/7/2023 — khoáng sản nhóm I; điều chỉnh bởi QĐ 2581/QĐ-TTg 24/11/2025 (mỏ đồng Tả Phời).
- QĐ 1626/QĐ-TTg 15/12/2023 — khoáng sản VLXD (khép lại thời kỳ kéo dài theo QĐ 154/QĐ-TTg 29/01/2022).
- NQ 10-NQ/TW 10/02/2022 (Bộ Chính trị) → NQ 88/NQ-CP 22/7/2022 → QĐ 334/QĐ-TTg 01/4/2023 — chủ trương, chương trình hành động và Chiến lược địa chất, khoáng sản, công nghiệp khai khoáng đến 2030, tầm nhìn 2045.
- Luật Quy hoạch 2017; Luật Điện lực 2024; Luật Địa chất và Khoáng sản 54/2024 (sửa 147/2025).

## Lưu ý dữ liệu

Số liệu công suất (MW), trữ lượng, diện tích, vị trí có thể thay đổi qua các lần điều chỉnh quy hoạch. Bản thuyết minh QHT 07/6/2026 ghi nhầm QĐ 866 ngày "17/8/2023" — ngày đúng là **18/7/2023**.
