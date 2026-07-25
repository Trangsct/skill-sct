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
    ├── 07-dieu-chinh-qd866-lao-cai.md # QĐ 2581 (Tả Phời) + dự thảo điều chỉnh QĐ 866; danh mục mỏ Lào Cai
    └── 08-toa-do-tham-do-che-bien-lao-cai.md # tọa độ khép góc, thăm dò, chế biến mỏ Lào Cai
sources/                              # TOÀN VĂN FILE GỐC để tra cứu chính xác
    ├── 00-MUC-LUC-NGUON.md           # mục lục + cách tra
    ├── qd866-dieuchinh-2026-thuyetminh.txt   # dự thảo điều chỉnh QĐ 866 (thuyết minh, 219tr)
    ├── qd866-dieuchinh-2026-phuluc.txt       # dự thảo điều chỉnh QĐ 866 (phụ lục, 449tr)
    ├── qd768-quyhoach-dien-viii-toanvan.txt  # QĐ 768 toàn văn (đã ký)
    ├── qht-laocai-2026-baocao-thuyetminh.txt # Báo cáo QHT Lào Cai 7/6/2026 (4 ngành tích hợp)
    └── qht-laocai-2026-phuluc.txt            # Phụ lục Báo cáo QHT Lào Cai 7/6/2026
```

Cơ chế: `references/` cho khung + phần Lào Cai trích sẵn (tra nhanh); `sources/` cho toàn văn gốc (tra chính xác, đầy đủ khi đưa số vào văn bản). Có thể bổ sung file nguồn mới vào `sources/` theo hướng dẫn trong mục lục.

## Văn bản gốc tham chiếu

- QĐ 525/QĐ-UBND 25/02/2026 — Quy hoạch tỉnh Lào Cai.
- QĐ 768/QĐ-TTg 15/4/2025 — Điều chỉnh Quy hoạch điện VIII.
- QĐ 866/QĐ-TTg 18/7/2023 — khoáng sản nhóm I.
- QĐ 1626/QĐ-TTg 15/12/2023 — khoáng sản VLXD.
- Luật Quy hoạch 2017; Luật Điện lực 2024; Luật Địa chất và Khoáng sản 54/2024 (sửa 147/2025).

## Lưu ý dữ liệu

Số liệu công suất (MW), trữ lượng, diện tích, vị trí có thể thay đổi qua các lần điều chỉnh quy hoạch. Bản thuyết minh QHT 07/6/2026 ghi nhầm QĐ 866 ngày "17/8/2023" — ngày đúng là **18/7/2023**.
