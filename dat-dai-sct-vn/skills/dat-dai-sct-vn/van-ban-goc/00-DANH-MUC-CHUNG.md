# Danh mục chung văn bản gốc — toàn bộ kho skill-sct

**Danh mục toàn bộ văn bản gốc trong mọi plugin của kho skill-sct. Trước khi kết luận văn bản nào chưa có, phải tra tệp này và chạy scripts/tim_van_ban.py** (ví dụ `python3 scripts/tim_van_ban.py "QCVN 01:2019"`).

- Tệp này do `scripts/build_so_cai_van_ban_goc.py` sinh ra, giống nhau ở mọi plugin — **không sửa tay**; sửa thì chạy lại script tại gốc kho.
- Đường dẫn ghi theo gốc kho `<plugin>/skills/<plugin>/van-ban-goc/…`. Trên claude.ai gói plugin nằm tại `/mnt/skills/plugins/<plugin>:<plugin>/van-ban-goc/…` (thay phần `<plugin>/skills/<plugin>/`).
- Mỗi tệp gốc có bản trích chữ **cùng tên, đuôi `.txt`** đặt cạnh (cột *.txt*). Bản gốc ≥ 3 MB bị export-ignore, không vào gói claude.ai — khi đó **mở bản `.txt`**, không được trả lời "không mở được toàn văn".
- Văn bản đã có ở đây thì **phải mở toàn văn để trích**; chỉ khi tra danh mục và chạy `tim_van_ban.py` đều không thấy mới được nói "chưa có bản gốc trong kho" và hướng dẫn Bạn nạp qua Hộp thư `_inbox/` trên GitHub.

Thống kê: 324 văn bản gốc (324 có bản .txt) ở 18 plugin; 30 văn bản có số hiệu trong `vi-du-thuc-te/`. Sắp theo ngày ban hành giảm dần; không rõ ngày xếp cuối.

## Văn bản gốc (van-ban-goc/)

| Số hiệu | Ngày | Tên | Plugin chủ | Đường dẫn | .txt |
|---|---|---|---|---|---|
| 63/2026/TT-BCT | 30/09/2026 | Thông tư quy định về cơ sở dữ liệu thực phẩm thuộc phạm vi quản lý của Bộ Công Thương | attp-sct-vn | `attp-sct-vn/skills/attp-sct-vn/van-ban-goc/2026.09.30 63.2026.TT.BCT Thông tư quy định về cơ sở dữ liệu thực phẩm thuộc phạm vi quản lý của Bộ Công Thương.docx` | có |
| 3556/QĐ-UBND | 30/09/2026 | ban hanh Quy che du lieu TNMT | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/tinh/QD-3556-QD-UBND-30-9-2026-ban-hanh-Quy-che-du-lieu-TNMT.pdf` | có |
| — | 30/09/2026 | Quy che kem QD 3556 QD UBND 30 9 2026 du lieu TNMT | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/tinh/Quy-che-kem-QD-3556-QD-UBND-30-9-2026-du-lieu-TNMT.pdf` | có |
| 9387/UBND-KT | 15/09/2026 | UBND tinh trien khai CTr 104 giao So NNMT | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/dang/CV-9387-UBND-KT-15-9-2026-UBND-tinh-trien-khai-CTr-104-giao-So-NNMT.pdf` | có |
| 257/QĐ-BQLCKCN | 10/09/2026 | dieu chinh CTDT lan 3 Mundus TEXT | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/QD-257-QD-BQLCKCN-10-9-2026-dieu-chinh-CTDT-lan-3-Mundus-TEXT.txt` | có |
| 347/2026/NĐ-CP | 08/09/2026 | sua doi ND 105 2025 | pccc-sct-vn | `pccc-sct-vn/skills/pccc-sct-vn/van-ban-goc/ND-347-2026-ND-CP-08-9-2026-sua-doi-ND-105-2025.docx` | có |
| 347/2026/NĐ-CP | 08/09/2026 | sua doi ND 105 2025 | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/ND-347-2026-ND-CP-08-9-2026-sua-doi-ND-105-2025.docx` | có |
| 2449-CV/ĐU | 07/09/2026 | Dang uy UBND tinh trien khai CTr 104 | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/dang/CV-2449-CV-DU-07-9-2026-Dang-uy-UBND-tinh-trien-khai-CTr-104.pdf` | có |
| 66.25/2026/NQ-CP | 04/09/2026 | 04 9 2026 chuyen QLNN dia chat khoang san KCN ve Cong Thuong | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/NQ-66.25-2026-NQ-CP-04-9-2026-chuyen-QLNN-dia-chat-khoang-san-KCN-ve-Cong-Thuong.pdf` | có (OCR) |
| 104-CTr/TU | 30/08/2026 | Tinh uy Lao Cai thuc hien KL 75 CTr 31 | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/dang/CTr-104-CTr-TU-30-8-2026-Tinh-uy-Lao-Cai-thuc-hien-KL-75-CTr-31.pdf` | có |
| 892/BC-SNNMT | 28/08/2026 | PHU LUC nhu cau kinh phi 2027 2029 | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/BC-892-BC-SNNMT-28-8-2026-PHU-LUC-nhu-cau-kinh-phi-2027-2029.pdf` | có |
| 892/BC-SNNMT | 28/08/2026 | kinh phi SNMT 2025 2026 KH 2027 2029 | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/BC-892-BC-SNNMT-28-8-2026-kinh-phi-SNMT-2025-2026-KH-2027-2029.pdf` | có |
| 904/BC-SNNMT | 28/08/2026 | ket qua kiem tra xac minh Dai Dong Tien | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/BC-904-BC-SNNMT-28-8-2026-ket-qua-kiem-tra-xac-minh-Dai-Dong-Tien.pdf` | có |
| QĐ 2978/2026 | 21/08/2026 | dieu chinh CTDT KCN Phu Xuan 1 | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/QD-2978-2026-dieu-chinh-CTDT-KCN-Phu-Xuan-1.pdf` | có |
| — | 21/08/2026 | BB kiem tra thuc dia 21 8 2026 ranh gioi mo Dai Dong Tien Thanh Huong Nghia Lo | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/BB-kiem-tra-thuc-dia-21-8-2026-ranh-gioi-mo-Dai-Dong-Tien-Thanh-Huong-Nghia-Lo.pdf` | có (OCR) |
| 5116/QĐ-SCT | 20/08/2026 | giao nhiem vu lap bien ban VPHC khoang san ban ky so | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/khoang-san/2026.08.20-5116.QD.SCT-giao-nhiem-vu-lap-bien-ban-VPHC-khoang-san_ban-ky-so.pdf` | có |
| 5085/SCT-VP | 19/08/2026 | Trien khai nhiem vu uy quyen VLNCN ban ky | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/2026.08.19-5085.SCT.VP-Trien-khai-nhiem-vu-uy-quyen-VLNCN_ban-ky.pdf` | có |
| 2867/QĐ-UBND | 17/08/2026 | Phu luc danh muc uy quyen ban trinh | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/2026.08.17-2867.QD.UBND-Phu-luc-danh-muc-uy-quyen_ban-trinh.docx` | có |
| 2867/QĐ-UBND | 17/08/2026 | Uy quyen GD SCT linh vuc VLNCN ban ky | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/2026.08.17-2867.QD.UBND-Uy-quyen-GD-SCT-linh-vuc-VLNCN_ban-ky.pdf` | có |
| 235/NQ-CP | 14/08/2026 | thoa thuan Dieu 6 VN Singapore | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/NQ-235-NQ-CP-14-8-2026-thoa-thuan-Dieu-6-VN-Singapore.txt` | có |
| 2848/QĐ-UBND | 14/08/2026 | sua doi bo sung QD 1696 | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/04-uy-quyen-quy-trinh/QD-2848-QD-UBND-14-8-2026-sua-doi-bo-sung-QD-1696.pdf` | có |
| 226/QĐ-BQLCKCN | 14/08/2026 | dieu chinh bo sung HDTD quy hoach KCN | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/QD-226-QD-BQLCKCN-14-8-2026-dieu-chinh-bo-sung-HDTD-quy-hoach-KCN.pdf` | có |
| 42/2026/QĐ-TTg | 10/08/2026 | danh muc co so kiem ke KNK | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/QD-42-2026-QD-TTg-10-8-2026-danh-muc-co-so-kiem-ke-KNK.txt` | có |
| 8129/UBND-KT | 10/08/2026 | giao kiem tra xac minh kien nghi Dai Dong Tien | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/CV-8129-UBND-KT-10-8-2026-giao-kiem-tra-xac-minh-kien-nghi-Dai-Dong-Tien.pdf` | có |
| 129/QĐ-BQL | 06/08/2026 | DCCB QHPK KCN Phu Xuan | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/QD-129-QD-BQL-06-8-2026-DCCB-QHPK-KCN-Phu-Xuan.pdf` | có |
| 130/QĐ-BQL | 06/08/2026 | DCCB QHPK KCN Phu Xuan 1 | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/QD-130-QD-BQL-06-8-2026-DCCB-QHPK-KCN-Phu-Xuan-1.pdf` | có |
| QĐ 2736/2026 | 06/08/2026 | HD lua chon CDT CCN Mong Son | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/QD-2736-2026-HD-lua-chon-CDT-CCN-Mong-Son.pdf` | có |
| 831/2026/TB-UBND | 06/08/2026 | Cam Duong tiep nhan ho so CCN Cam Duong 1 | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/TB-831-2026-UBND-Cam-Duong-tiep-nhan-ho-so-CCN-Cam-Duong-1.pdf` | có |
| 311/2026/NĐ-CP | 06/08/2026 | sua doi ND 189 2025 | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/chung/ND-311-2026-NDCP-sua-doi-ND-189-2025.docx` | có |
| 28/CV-ĐĐT | 04/08/2026 | kien nghi lan chiem ranh gioi mo Dai Dong Tien | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/CV-28-CV-DDT-04-8-2026-kien-nghi-lan-chiem-ranh-gioi-mo-Dai-Dong-Tien.pdf` | có (OCR) |
| 31-CTr/TW | 28/07/2026 | Bo Chinh tri thuc hien KL 75 | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/dang/CTr-31-CTr-TW-28-7-2026-Bo-Chinh-tri-thuc-hien-KL-75.pdf` | có (OCR) |
| 75-KL/TW | 28/07/2026 | BVMT BDKH thoi ky moi | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/dang/KL-75-KL-TW-28-7-2026-BVMT-BDKH-thoi-ky-moi.pdf` | có (OCR) |
| 6987/SNNMT-KS | 23/07/2026 | nghia vu sau cap phep mo dat hiem Ben Den KhanhAn | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/CV-6987-SNNMT-KS-23-7-2026-nghia-vu-sau-cap-phep-mo-dat-hiem-Ben-Den-KhanhAn.txt` | có |
| 7432/UBND-XD | 21/07/2026 | trien khai QD 1074 | pccc-sct-vn | `pccc-sct-vn/skills/pccc-sct-vn/van-ban-goc/CV-7432-UBND-XD-21-7-2026-trien-khai-QD-1074.pdf` | có |
| 288/2026/NĐ-CP | 21/07/2026 | sua doi ND 122 2021 | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/dau-tu/ND-288-2026-NDCP-sua-doi-ND-122-2021.docx` | có |
| 6791/SNNMT | 17/07/2026 | y kien tham dinh CCN Bao Dap | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/CV-6791-SNNMT-17-7-2026-y-kien-tham-dinh-CCN-Bao-Dap.pdf` | có |
| 6795/SNNMT-KS | 17/07/2026 | nghia vu sau cap phep mo Quy Xa | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/CV-6795-SNNMT-KS-17-7-2026-nghia-vu-sau-cap-phep-mo-Quy-Xa.txt` | có |
| QĐ 2463/2026 | 16/07/2026 | CTDT KCN Vo Lao | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/QD-2463-2026-CTDT-KCN-Vo-Lao.pdf` | có |
| 283/2026/NĐ-CP | 15/07/2026 | xu phat lao dong BHXH NLD di lam viec nuoc ngoai | atvsld-sct-vn | `atvsld-sct-vn/skills/atvsld-sct-vn/van-ban-goc/ND-283-2026-NDCP-xu-phat-lao-dong-BHXH-NLD-di-lam-viec-nuoc-ngoai.docx` | có |
| 283/2026/NĐ-CP | 15/07/2026 | xu phat lao dong | atvsld-sct-vn | `atvsld-sct-vn/skills/atvsld-sct-vn/van-ban-goc/ND-283-2026-NDCP-xu-phat-lao-dong.txt` | có |
| 31/2026/TT-BNNMT | 15/07/2026 | dinh gia rung chi tra cac bon | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/TT-31-2026-TT-BNNMT-15-7-2026-dinh-gia-rung-chi-tra-cac-bon.txt` | có |
| 283/2026/NĐ-CP | 15/07/2026 | xu phat lao dong BHXH | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/lao-dong/ND-283-2026-NDCP-xu-phat-lao-dong-BHXH.docx` | có |
| 281/2026/NĐ-CP | 13/07/2026 | sua doi ND 123 2024 | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/dat-dai/ND-281-2026-NDCP-sua-doi-ND-123-2024.docx` | có |
| 7103/UBND-TH | 10/07/2026 | trien khai ND178 | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/CV-7103-UBND-TH-10-7-2026-trien-khai-ND178.pdf` | có |
| QĐ 2390/2026 | 09/07/2026 | KH dau tu cong trung han 2026 2030 | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/QD-2390-2026-KH-dau-tu-cong-trung-han-2026-2030.pdf` | có |
| 275/2026/NĐ-CP | 08/07/2026 | xu phat VPHC hoa chat VLNCN | xp-hc-vlncn-sct-vn | `xp-hc-vlncn-sct-vn/skills/xp-hc-vlncn-sct-vn/van-ban-goc/ND-275-2026-NDCP-xu-phat-VPHC-hoa-chat-VLNCN.docx` | có |
| 275/2026/NĐ-CP | 08/07/2026 | xu phat VPHC hoa chat VLNCN | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/ND-275-2026-NDCP-xu-phat-VPHC-hoa-chat-VLNCN.docx` | có |
| 49/2026/QĐ-UBND | 30/06/2026 | chi tiet Luat Dat dai Lao Cai | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/tinh/QD-49-2026-QD-UBND-chi-tiet-Luat-Dat-dai-Lao-Cai.docx` | có |
| — | 30/06/2026 | GCN DKDT KCN Ban Qua 30 6 2026 | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/GCN-DKDT-KCN-Ban-Qua-30-6-2026.pdf` | có |
| 1074/QĐ-BXD | 29/06/2026 |  | pccc-sct-vn | `pccc-sct-vn/skills/pccc-sct-vn/van-ban-goc/QD-1074-QD-BXD-29-6-2026.pdf` | có |
| — | 29/06/2026 | Tai lieu giai phap nang cao PCCC kem QD 1074 | pccc-sct-vn | `pccc-sct-vn/skills/pccc-sct-vn/van-ban-goc/Tai-lieu-giai-phap-nang-cao-PCCC-kem-QD-1074.pdf` | có |
| 2272/QĐ-UBND | 29/06/2026 | Co quan tiep nhan ho so GCN san xuat tien chat thuoc no ban du thao | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/2026.06.29-2272.QD.UBND-Co-quan-tiep-nhan-ho-so-GCN-san-xuat-tien-chat-thuoc-no_ban-du-thao.docx` | có |
| 2272/QĐ-UBND | 29/06/2026 | Co quan tiep nhan ho so GCN san xuat tien chat thuoc no ban ky | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/2026.06.29-2272.QD.UBND-Co-quan-tiep-nhan-ho-so-GCN-san-xuat-tien-chat-thuoc-no_ban-ky.pdf` | có |
| 47/2026/QĐ-UBND | 28/06/2026 | trinh tu thu tuc dat dai | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/tinh/QD-47-2026-QD-UBND-trinh-tu-thu-tuc-dat-dai.docx` | có |
| 36/2026/TT-BXD | 26/06/2026 | chi phi dau tu xay dung | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/TT-36-2026-TT-BXD-chi-phi-dau-tu-xay-dung.docx` | có |
| 39/2026/TT-BXD | 26/06/2026 | CSDL quoc gia HDXD | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/TT-39-2026-TT-BXD-CSDL-quoc-gia-HDXD.docx` | có |
| — | 25/06/2026 | Huong dan lien nganh 24 N2O | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/van-ban-goc/06-danh-muc-cong-van/Huong-dan-lien-nganh-24-N2O.pdf` | có |
| 34/2026/TT-BXD | 25/06/2026 | cap cong trinh | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/TT-34-2026-TT-BXD-cap-cong-trinh.docx` | có |
| QĐ 2170/2026 | 23/06/2026 | CTDT KCN Ban Qua | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/QD-2170-2026-CTDT-KCN-Ban-Qua.pdf` | có |
| 8388/BTC-QLCS | 19/06/2026 | trien khai ND178 | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/CV-8388-BTC-QLCS-19-6-2026-trien-khai-ND178.pdf` | có (OCR) |
| 217/2026/NĐ-CP | 19/06/2026 | quan ly hoat dong xay dung | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/ND-217-2026-quan-ly-hoat-dong-xay-dung.pdf` | có (OCR) |
| 212/2026/NĐ-CP | 17/06/2026 | dieu kien nang luc HDXD CSDL quoc gia | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/ND-212-2026-dieu-kien-nang-luc-HDXD-CSDL-quoc-gia.docx` | có |
| 43/2026/QĐ-UBND | 16/06/2026 | nghiem thu san pham dat dai | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/tinh/QD-43-2026-QD-UBND-nghiem-thu-san-pham-dat-dai.docx` | có |
| 207/2026/NĐ-CP | 15/06/2026 | QLCL thi cong bao tri | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/ND-207-2026-QLCL-thi-cong-bao-tri.docx` | có |
| 5973/UBND-KT | 11/06/2026 | tang cuong thanh kiem tra KS | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/CV-5973-UBND-KT-11-6-2026-tang-cuong-thanh-kiem-tra-KS.txt` | có |
| 2200/QĐ-BNNMT | 10/06/2026 | ke hoach trien khai ND 180 | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/QD-2200-QD-BNNMT-10-6-2026-ke-hoach-trien-khai-ND-180.txt` | có |
| 47/QĐ-HĐTV | 05/06/2026 | HDTV VNX quy che giao dich | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/QD-47-QD-HDTV-05-6-2026-VNX-quy-che-giao-dich.txt` | có |
| 40/2026/QĐ-UBND | 31/05/2026 | phan cap tham quyen dat dai | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/tinh/QD-40-2026-QD-UBND-phan-cap-tham-quyen-dat-dai.docx` | có |
| 39/QĐ-HĐTV | 28/05/2026 | HDTV VNX quy che CNTT ket noi | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/QD-39-QD-HDTV-28-5-2026-VNX-quy-che-CNTT-ket-noi.txt` | có |
| 40/QĐ-HĐTV | 28/05/2026 | HDTV VNX quy che thanh vien giao dich | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/QD-40-QD-HDTV-28-5-2026-VNX-quy-che-thanh-vien-giao-dich.txt` | có |
| 4390/UBND-NLN | 27/05/2026 | trien khai ND 180 | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/CV-4390-UBND-NLN-27-5-2026-trien-khai-ND-180.txt` | có |
| 180/2026/NĐ-CP | 21/05/2026 | dich vu hap thu cac bon rung | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/ND-180-2026-ND-CP-21-5-2026-dich-vu-hap-thu-cac-bon-rung.txt` | có |
| 26/2026/TT-BCT | 20/05/2026 | text | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/03-thong-tu/TT-26-2026-BCT-text.doc` | có |
| 178/2026/NĐ-CP | 20/05/2026 | tai san ket cau ha tang | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/ND-178-2026-tai-san-ket-cau-ha-tang.docx` | có |
| 26/2026/TT-BCT | 20/05/2026 | phan cap cat giam TTHC BCT | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/TT-26-2026-TT-BCT-phan-cap-cat-giam-TTHC-BCT.docx` | có |
| 66.18/2026/NQ-CP | 18/05/2026 |  | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/02-nghi-dinh/NQ-66-18-2026-NQ-CP.docx` | có |
| 66.19/2026/NQ-CP | 18/05/2026 | toan van | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/NQ-66.19-2026-NQ-CP-toan-van.docx` | có |
| 66.19/2026/NQ-CP | 18/05/2026 | Phu luc VIII phan quyen TTHC DCKS | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/NQ-66.19-2026-Phu-luc-VIII-phan-quyen-TTHC-DCKS.docx` | có |
| 66.18/2026/NQ-CP | 18/05/2026 | phan quyen cat giam TTHC | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/NQ-18-2026-NQ-CP-phan-quyen-cat-giam-TTHC.docx` | có |
| 66.18/2026/NQ-CP | 18/05/2026 | phan quyen cat giam TTHC DKKD | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/NQ-66.18-2026-NQ-CP-phan-quyen-cat-giam-TTHC-DKKD.docx` | có |
| 1696/QĐ-UBND | 15/05/2026 | uy quyen | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/04-uy-quyen-quy-trinh/QD-1696-QD-UBND-uy-quyen-15-5-2026.pdf` | có |
| 48/2026/TT-BTC | 12/05/2026 | giam sat giao dich san | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/TT-48-2026-TT-BTC-12-5-2026-giam-sat-giao-dich-san.txt` | có |
| 3686/UBND-XD | 11/05/2026 | kien nghi BXD PCCC VLNCN | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/04-uy-quyen-quy-trinh/CV-3686-UBND-XD-kien-nghi-BXD-PCCC-VLNCN.pdf` | có |
| 13A/BB-DTT72 | 10/05/2026 | thanh tra khai thac KS Mong Son | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/BB-13A-BB-DTT72-10-5-2026-thanh-tra-khai-thac-KS-Mong-Son.pdf` | có (OCR) |
| 17/QĐ-HĐTV | 29/04/2026 | HDTV VSDC quy che luu ky thanh toan | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/QD-17-QD-HDTV-29-4-2026-VSDC-quy-che-luu-ky-thanh-toan.txt` | có |
| 19/2026/NQ-CP | 29/04/2026 |  | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/02-nghi-dinh/NQ-19-2026-NQ-CP.pdf` | có (OCR) |
| 24/2026//NQ-CP | 29/04/2026 | cat giam TTHC XD | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/NQ-24-2026-NQ-CP-cat-giam-TTHC-XD.docx` | có |
| 3320/SNNMT-CCMT | 23/04/2026 | chuyen VBHN 48 49 | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/CV-3320-SNNMT-CCMT-23-4-2026-chuyen-VBHN-48-49.txt` | có |
| 15/2026/NQ-CP | 06/04/2026 | Nghị quyết tạm ngưng NĐ 46.2026 và NQ 66.13.2026 | attp-sct-vn | `attp-sct-vn/skills/attp-sct-vn/van-ban-goc/2026.04.06 15.2026.NQ.CP Nghị quyết tạm ngưng NĐ 46.2026 và NQ 66.13.2026.docx` | có |
| — | 06/04/2026 | VB giao tham gia phoi hop | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/04-uy-quyen-quy-trinh/VB-giao-tham-gia-phoi-hop.pdf` | có |
| 133/2026/NĐ-CP | 06/04/2026 | xu phat dien luc | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/dien-luc/ND-133-2026-NDCP-xu-phat-dien-luc.docx` | có |
| 112/2026/NĐ-CP | 01/04/2026 | trao doi quoc te tin chi | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/ND-112-2026-ND-CP-01-4-2026-trao-doi-quoc-te-tin-chi.txt` | có |
| 425/QĐ-BXD | 30/03/2026 | suat von dau tu | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/QD-425-QD-BXD-30-3-2026-suat-von-dau-tu.docx` | có |
| 597/HC-QLHC | 27/03/2026 | CucHoaChat | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/van-ban-goc/06-danh-muc-cong-van/CV-597-HC-QLHC-CucHoaChat.docx` | có |
| 78/VBHN-VPQH | 26/03/2026 | Luat Quan ly su dung vu khi VLN va CCHT HOP NHAT | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/van-ban-goc/2026.03.26-78.VBHN.VPQH-Luat-Quan-ly-su-dung-vu-khi-VLN-va-CCHT-HOP-NHAT.docx` | có |
| 134/KH-UBND | 26/03/2026 |  | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/KH-134-KH-UBND-26-3-2026.pdf` | có |
| 78/VBHN-VPQH | 26/03/2026 | Luat Quan ly su dung vu khi VLN va CCHT HOP NHAT | kho-vlncn-sct-vn | `kho-vlncn-sct-vn/skills/kho-vlncn-sct-vn/van-ban-goc/2026.03.26-78.VBHN.VPQH-Luat-Quan-ly-su-dung-vu-khi-VLN-va-CCHT-HOP-NHAT.docx` | có |
| 78/VBHN-VPQH | 26/03/2026 | Luat Quan ly su dung vu khi VLN va CCHT HOP NHAT | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/2026.03.26-78.VBHN.VPQH-Luat-Quan-ly-su-dung-vu-khi-VLN-va-CCHT-HOP-NHAT.docx` | có |
| 78/VBHN-VPQH | 26/03/2026 | Luat Quan ly su dung vu khi VLN va CCHT HOP NHAT | xp-hc-vlncn-sct-vn | `xp-hc-vlncn-sct-vn/skills/xp-hc-vlncn-sct-vn/van-ban-goc/2026.03.26-78.VBHN.VPQH-Luat-Quan-ly-su-dung-vu-khi-VLN-va-CCHT-HOP-NHAT.docx` | có |
| 78/VBHN-VPQH | 26/03/2026 | Luat Quan ly su dung vu khi VLN va CCHT HOP NHAT | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/2026.03.26-78.VBHN.VPQH-Luat-Quan-ly-su-dung-vu-khi-VLN-va-CCHT-HOP-NHAT.docx` | có |
| 15/2026/TT-BCT | 25/03/2026 | text | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/03-thong-tu/TT-15-2026-BCT-text.doc` | có |
| 2265/BCT-ATMT | 25/03/2026 | trien khai | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/04-uy-quyen-quy-trinh/CV-2265-BCT-ATMT-trien-khai.pdf` | có (OCR) |
| — | 25/03/2026 | Huong dan thu tuc cap GP loai 1 2 3 4 9 SCT | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/04-uy-quyen-quy-trinh/Huong-dan-thu-tuc-cap-GP-loai-1-2-3-4-9-SCT.docx` | có |
| 83/2026/NĐ-CP | 23/03/2026 | sua ND 06 o don | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/ND-83-2026-ND-CP-23-3-2026-sua-ND-06-o-don.txt` | có |
| CV 813 | 16/03/2026 | CucHoaChat | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/van-ban-goc/06-danh-muc-cong-van/CV-813-CucHoaChat.pdf` | có (OCR) |
| 699/QĐ-BNNMT | 27/02/2026 | thi diem phan bo han ngach 2025 2026 | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/QD-699-QD-BNNMT-27-02-2026-thi-diem-phan-bo-han-ngach-2025-2026.txt` | có |
| 452/BC-TTCP | 26/02/2026 | thanh tra chuyen de mo VLXD | tkm-sct-vn | `tkm-sct-vn/skills/tkm-sct-vn/van-ban-goc/BC-452-BC-TTCP-26-02-2026-thanh-tra-chuyen-de-mo-VLXD.pdf` | có (OCR) |
| 16/2026/QĐ-UBND | 25/02/2026 | Quy che CCN Lao Cai | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/QD-16-2026-QD-UBND-Quy-che-CCN-Lao-Cai.pdf` | có |
| QĐ 16/2026 | 25/02/2026 | Quy che CCN Lao Cai OCR | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/QD-16-2026-Quy-che-CCN-Lao-Cai-OCR.txt` | có |
| 11/2026/TT-BNNMT | 13/02/2026 | he thong dang ky quoc gia | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/TT-11-2026-TT-BNNMT-13-02-2026-he-thong-dang-ky-quoc-gia.txt` | có |
| 13/2026/TT-BQP | 12/02/2026 |  | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/van-ban-goc/03-thong-tu/TT-13-2026-BQP.docx` | có |
| 1153/BNNMT-QLĐĐ | 03/02/2026 | trien khai ND 49 | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/trung-uong/CV-1153-BNNMT-QLDD-03-02-2026-trien-khai-ND-49.docx` | có |
| 49/2026/NĐ-CP | 31/01/2026 | chi tiet NQ 254 | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/trung-uong/ND-49-2026-ND-CP-chi-tiet-NQ-254.docx` | có |
| 50/2026/NĐ-CP | 31/01/2026 | tien su dung dat tien thue dat | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/trung-uong/ND-50-2026-ND-CP-tien-su-dung-dat-tien-thue-dat.docx` | có |
| 216/ATMT-ATĐ | 30/01/2026 | huong dan nao vet ket hop thu hoi KS long ho thuy dien | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/CV-216-ATMT-ATD-30-01-2026-huong-dan-nao-vet-ket-hop-thu-hoi-KS-long-ho-thuy-dien.pdf` | có |
| 11/2026/QĐ-UBND | 29/01/2026 | Lao Cai quan ly dau tu xay dung | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/QD-11-2026-QD-UBND-Lao-Cai-quan-ly-dau-tu-xay-dung.pdf` | có (OCR) |
| 09/2026/TT-BQP | 22/01/2026 | Sua doi bo sung TT 98 2024 TT BQP | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/van-ban-goc/2026.01.22-09.2026.TT.BQP-Sua-doi-bo-sung-TT-98-2024-TT-BQP.docx` | có |
| 09/2026/TT-BQP | 22/01/2026 | Sua doi bo sung TT 98 2024 TT BQP | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/2026.01.22-09.2026.TT.BQP-Sua-doi-bo-sung-TT-98-2024-TT-BQP.docx` | có |
| 683/BTC-CST | 19/01/2026 | thue GTGT tin chi VERs | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/CV-683-BTC-CST-19-01-2026-thue-GTGT-tin-chi-VERs.txt` | có |
| 29/2026/NĐ-CP | 19/01/2026 | san giao dich cac bon | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/ND-29-2026-ND-CP-19-01-2026-san-giao-dich-cac-bon.txt` | có |
| 24/2026/NĐ-CP | 17/01/2026 | danh muc hoa chat | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/van-ban-goc/02-nghi-dinh/ND-24-2026-danh-muc-hoa-chat.docx` | có |
| 25/2026/NĐ-CP | 17/01/2026 | phat trien antoan anninh | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/van-ban-goc/02-nghi-dinh/ND-25-2026-phat-trien-antoan-anninh.docx` | có |
| 26/2026/NĐ-CP | 17/01/2026 | quan ly hoat dong hoa chat | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/van-ban-goc/02-nghi-dinh/ND-26-2026-quan-ly-hoat-dong-hoa-chat.docx` | có |
| 01/2026/TT-BCT | 17/01/2026 | huong dan ND26 bieu mau | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/van-ban-goc/03-thong-tu/TT-01-2026-BCT-huong-dan-ND26-bieu-mau.docx` | có |
| 02/2026/TT-BCT | 17/01/2026 | bien phap thi hanh ND25 | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/van-ban-goc/03-thong-tu/TT-02-2026-BCT-bien-phap-thi-hanh-ND25.docx` | có |
| 21/2026/NĐ-CP | 16/01/2026 | sua ND 193 2025 | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/ND-21-2026-ND-CP-sua-ND-193-2025.docx` | có |
| 04/2026/TT-BNNMT | 16/01/2026 | sua cac TT dia chat khoang san | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/TT-04-2026-TT-BNNMT-sua-cac-TT-dia-chat-khoang-san.docx` | có |
| 7/QĐ-BQLCKCN | 15/01/2026 | thanh lap HDTD quy hoach KCN | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/QD-7-QD-BQLCKCN-15-01-2026-thanh-lap-HDTD-quy-hoach-KCN.pdf` | có |
| 14/2026/NĐ-CP | 13/01/2026 | cat giam TTHC SXKD | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/ND-14-2026-cat-giam-TTHC-SXKD.docx` | có |
| 66.11/2026/NQ-CP | 06/01/2026 | dau gia quyen su dung dat | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/trung-uong/NQ-66.11-2026-NQ-CP-dau-gia-quyen-su-dung-dat.docx` | có |
| 67/2025/TT-BCT | 31/12/2025 | sua doi TT 43 2025 | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/TT-67-2025-TT-BCT-sua-doi-TT-43-2025.docx` | có |
| 5141/SNNMT-KS | 29/12/2025 | thong ke ke khai bao cao san luong | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/CV-5141-SNNMT-KS-29-12-2025-thong-ke-ke-khai-bao-cao-san-luong.txt` | có |
| 34-NQ/TU | 27/12/2025 |  | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/NQ-34-NQ-TU-27-12-2025.pdf` | có (OCR) |
| 146/2025/QH15 | 11/12/2025 | sua doi 15 luat nong nghiep moi truong | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/trung-uong/Luat-146-2025-QH15-sua-doi-15-luat-nong-nghiep-moi-truong.docx` | có |
| 254/2025/QH15 | 11/12/2025 | thao go vuong mac Luat Dat dai | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/trung-uong/NQ-254-2025-QH15-thao-go-vuong-mac-Luat-Dat-dai.docx` | có |
| 147/2025/QH15 | 11/12/2025 | sua Luat DCKS TOAN VAN | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/Luat-147-2025-QH15-sua-Luat-DCKS-TOAN-VAN.docx` | có |
| 147/2025/QH15 | 11/12/2025 | sua Luat DCKS | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/Luat-147-2025-QH15-sua-Luat-DCKS.docx` | có |
| 118/2025/QH15 | 10/12/2025 | Sua doi 10 luat lien quan an ninh trat tu | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/van-ban-goc/2025.12.10-118.2025.QH15-Sua-doi-10-luat-lien-quan-an-ninh-trat-tu.docx` | có |
| 118/2025/QH15 | 10/12/2025 | Sua doi 10 luat lien quan an ninh trat tu | kho-vlncn-sct-vn | `kho-vlncn-sct-vn/skills/kho-vlncn-sct-vn/van-ban-goc/2025.12.10-118.2025.QH15-Sua-doi-10-luat-lien-quan-an-ninh-trat-tu.docx` | có |
| 118/2025/QH15 | 10/12/2025 | Sua doi 10 luat lien quan an ninh trat tu | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/2025.12.10-118.2025.QH15-Sua-doi-10-luat-lien-quan-an-ninh-trat-tu.docx` | có |
| 135/2025/QH15 | 10/12/2025 | Luat Xay dung 135 2025 QH15 | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/Luat-Xay-dung-135-2025-QH15.docx` | có |
| 19/2025/NQ-HĐND | 09/12/2025 | bang gia dat Lao Cai | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/tinh/NQ-19-2025-NQ-HDND-bang-gia-dat-Lao-Cai.docx` | có |
| 26-NQ/TU | 05/12/2025 |  | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/NQ-26-NQ-TU-05-12-2025.pdf` | có (OCR) |
| 56/2025/TT-BCT | 28/11/2025 | quy trinh kiem tra chuyen nganh Cong Thuong | xp-hc-vlncn-sct-vn | `xp-hc-vlncn-sct-vn/skills/xp-hc-vlncn-sct-vn/van-ban-goc/TT-56-2025-TT-BCT-quy-trinh-kiem-tra-chuyen-nganh-Cong-Thuong.docx` | có |
| 56/2025/TT-BCT | 28/11/2025 | quy trinh kiem tra chuyen nganh Cong Thuong | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/TT-56-2025-TT-BCT-quy-trinh-kiem-tra-chuyen-nganh-Cong-Thuong.docx` | có |
| 2581/QĐ-TTg | 24/11/2025 | dieu chinh QD 866 Nui Phao Ta Phoi Tho Son Thong Nhat | quy-hoach-ct-vn | `quy-hoach-ct-vn/skills/quy-hoach-ct-vn/van-ban-goc/QD-2581-QD-TTg-24-11-2025-dieu-chinh-QD-866-Nui-Phao-Ta-Phoi-Tho-Son-Thong-Nhat.docx` | có |
| 9389/BNNMT-BĐKH | 20/11/2025 | giao viec cap tinh KNK | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/CV-9389-BNNMT-BDKH-20-11-2025-giao-viec-cap-tinh-KNK.txt` | có |
| 303/2025/NĐ-CP | 19/11/2025 | chuc nang nhiem vu co cau to chuc bo co quan ngang bo | sct-laocai-org-vn | `sct-laocai-org-vn/skills/sct-laocai-org-vn/van-ban-goc/ND-303-2025-chuc-nang-nhiem-vu-co-cau-to-chuc-bo-co-quan-ngang-bo.docx` | có |
| 28/2025/QĐ-UBND | 10/11/2025 | phan cap quan ly ATTP Lao Cai | attp-sct-vn | `attp-sct-vn/skills/attp-sct-vn/van-ban-goc/2025.11.10 QD 28-2025-QD-UBND phan cap quan ly ATTP Lao Cai.txt` | có |
| 1883/QĐ-UBND | 06/11/2025 | Phu luc danh muc uy quyen ban ky | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/van-ban-goc/2025.11.06-1883.QD.UBND-Phu-luc-danh-muc-uy-quyen_ban-ky.pdf` | có |
| 1883/QĐ-UBND | 06/11/2025 | Uy quyen GD SCT linh vuc VLNCN ban ky | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/van-ban-goc/2025.11.06-1883.QD.UBND-Uy-quyen-GD-SCT-linh-vuc-VLNCN_ban-ky.pdf` | có |
| — | 06/11/2025 | QD uy quyen VLNCN du thao trinh TTr 2205 ban hanh QD 1883 UBND 6.11.2025 | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/van-ban-goc/QD-uy-quyen-VLNCN_du-thao-trinh-TTr-2205_ban-hanh-QD-1883-UBND-6.11.2025.docx` | có |
| 282/2025/NĐ-CP | 30/10/2025 | Xu phat VPHC an ninh trat tu ATXH | xp-hc-vlncn-sct-vn | `xp-hc-vlncn-sct-vn/skills/xp-hc-vlncn-sct-vn/van-ban-goc/2025.10.30-282.2025.ND.CP-Xu-phat-VPHC-an-ninh-trat-tu-ATXH.docx` | có |
| 282/2025/NĐ-CP | 30/10/2025 | Xu phat VPHC an ninh trat tu ATXH | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/2025.10.30-282.2025.ND.CP-Xu-phat-VPHC-an-ninh-trat-tu-ATXH.docx` | có |
| 2419/ĐCKS-PCKS | 19/09/2025 | tra loi 42 vuong mac dia chat khoang san | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/CV-2419-DCKS-PCKS-19-9-2025-tra-loi-42-vuong-mac-dia-chat-khoang-san.pdf` | có |
| 66.3/2025/NQ-CP | 15/09/2025 | thao go quy hoach su dung dat | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/trung-uong/NQ-66.3-2025-NQ-CP-thao-go-quy-hoach-su-dung-dat.docx` | có |
| — | 15/09/2025 | CV UBND KT giao SCT tham muu uy quyen truoc 15.9.2025 | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/van-ban-goc/CV-UBND-KT_giao-SCT-tham-muu-uy-quyen_truoc-15.9.2025.docx` | có |
| 243/2025/NĐ-CP | 11/09/2025 | PPP | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/ND-243-2025-PPP.docx` | có |
| 21/2025/QĐ-UBND | 10/09/2025 | boi thuong nha cong trinh | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/tinh/QD-21-2025-QD-UBND-boi-thuong-nha-cong-trinh.docx` | có |
| 20/2025/QĐ-UBND | 29/08/2025 | boi thuong cay trong vat nuoi | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/tinh/QD-20-2025-QD-UBND-boi-thuong-cay-trong-vat-nuoi.docx` | có |
| 904/QĐ-UBND | 26/08/2025 | uy quyen lap Doan tham dinh ATTP | attp-sct-vn | `attp-sct-vn/skills/attp-sct-vn/van-ban-goc/2025.08.26 QD 904-QD-UBND uy quyen lap Doan tham dinh ATTP.txt` | có |
| 18/2025/QĐ-UBND | 15/08/2025 | boi thuong ho tro tai dinh cu | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/tinh/QD-18-2025-QD-UBND-boi-thuong-ho-tro-tai-dinh-cu.docx` | có |
| 226/2025/NĐ-CP | 15/08/2025 | sua doi cac nghi dinh dat dai | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/trung-uong/ND-226-2025-ND-CP-sua-doi-cac-nghi-dinh-dat-dai.docx` | có |
| 217/2025/NĐ-CP | 05/08/2025 | kiem tra chuyen nganh | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/06-kiem-tra/ND-217-2025-kiem-tra-chuyen-nganh.docx` | có |
| 1198/ATMT-ATKV | 21/07/2025 | Huong dan quan ly su dung VLNCN tra loi SCT Lai Chau trich luc | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/van-ban-goc/2025.07.21-1198.ATMT.ATKV-Huong-dan-quan-ly-su-dung-VLNCN_tra-loi-SCT-Lai-Chau_trich-luc.md` | có |
| 1178/DCK-CTT | 09/07/2025 | huong dan CCN dia gioi moi | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/1178-DCK-CTT-huong-dan-CCN-dia-gioi-moi.pdf` | có |
| 43/2025/TT-BCT | 04/07/2025 | ky thuat an toan khai thac KS | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/TT-43-2025-TT-BCT-ky-thuat-an-toan-khai-thac-KS.docx` | có |
| 193/2025/NĐ-CP | 02/07/2025 | trich quan trong | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/ND-193-2025-ND-CP-trich-quan-trong.docx` | có |
| 36/2025/TT-BNNMT | 02/07/2025 | PHU LUC I den IV | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/TT-36-2025-TT-BNNMT-PHU-LUC-I-den-IV.doc` | có |
| 36/2025/TT-BNNMT | 02/07/2025 | TOAN VAN dieu khoan | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/TT-36-2025-TT-BNNMT-TOAN-VAN-dieu-khoan.docx` | có |
| 36/2025/TT-BNNMT | 02/07/2025 | khai thac tan thu thu hoi | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/TT-36-2025-TT-BNNMT-khai-thac-tan-thu-thu-hoi.docx` | có |
| 178/2025/NĐ-CP | 01/07/2025 | quy hoach do thi nong thon | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/ND-178-2025-quy-hoach-do-thi-nong-thon.docx` | có |
| 189/2025/NĐ-CP | 01/07/2025 | tham quyen xu phat | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/chung/ND-189-2025-NDCP-tham-quyen-xu-phat.docx` | có |
| 84/2025/QH15 | 25/06/2025 | Luat Thanh tra 84 2025 | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/06-kiem-tra/Luat-Thanh-tra-84-2025.docx` | có |
| 88/2025/QH15 | 25/06/2025 | sua doi Luat XLVPHC | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/chung/Luat-88-2025-QH15-sua-doi-Luat-XLVPHC.docx` | có |
| 38/2025/TT-BCT | 19/06/2025 | Sua doi quy dinh phan cap thuc hien TTHC cua BCT | kho-vlncn-sct-vn | `kho-vlncn-sct-vn/skills/kho-vlncn-sct-vn/van-ban-goc/2025.06.19-38.2025.TT.BCT-Sua-doi-quy-dinh-phan-cap-thuc-hien-TTHC-cua-BCT.doc` | có |
| 38/2025/TT-BCT | 19/06/2025 |  | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/TT-38-2025-BCT.doc` | có |
| 08/2025/TT-BNNMT | 17/06/2025 | sua TT 01 2022 BDKH | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/TT-08-2025-TT-BNNMT-17-6-2025-sua-TT-01-2022-BDKH.txt` | có |
| 69/2025/QH15 | 14/06/2025 | Luat Hoa chat 69 2025 QH15 | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/van-ban-goc/01-luat/Luat-Hoa-chat-69-2025-QH15.docx` | có |
| 151/2025/NĐ-CP | 12/06/2025 | phan dinh tham quyen dat dai | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/trung-uong/ND-151-2025-ND-CP-phan-dinh-tham-quyen-dat-dai.docx` | có |
| 146/2025/NĐ-CP | 12/06/2025 | phan quyen phan cap | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/van-ban-goc/02-nghi-dinh/ND-146-2025-phan-quyen-phan-cap.docx` | có |
| 139/2025/NĐ-CP | 12/06/2025 | phan dinh tham quyen 2 cap BCT | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/ND-139-2025-phan-dinh-tham-quyen-2-cap-BCT.docx` | có |
| 146/2025/NĐ-CP | 12/06/2025 | Phan quyen phan cap linh vuc cong nghiep thuong mai | kho-vlncn-sct-vn | `kho-vlncn-sct-vn/skills/kho-vlncn-sct-vn/van-ban-goc/2025.06.12-146.2025.ND.CP-Phan-quyen-phan-cap-linh-vuc-cong-nghiep-thuong-mai.doc` | có |
| 146/2025/NĐ-CP | 12/06/2025 |  | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/ND-146-2025.doc` | có |
| 140/2025/NĐ-CP | 12/06/2025 | phan dinh tham quyen 2 cap XD | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/ND-140-2025-phan-dinh-tham-quyen-2-cap-XD.docx` | có |
| 144/2025/NĐ-CP | 12/06/2025 | phan quyen phan cap BXD | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/ND-144-2025-phan-quyen-phan-cap-BXD.docx` | có |
| 119/2025/NĐ-CP | 09/06/2025 | sua ND 06 | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/ND-119-2025-ND-CP-09-6-2025-sua-ND-06.txt` | có |
| 31/2025/TT-BCT | 16/05/2025 | toan van unicode | tkm-sct-vn | `tkm-sct-vn/skills/tkm-sct-vn/van-ban-goc/TT-31-2025-TT-BCT-toan-van-unicode.docx` | có |
| 105/2025/NĐ-CP | 15/05/2025 | PCCC CNCH | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/02-nghi-dinh/ND-105-2025-PCCC-CNCH.pdf` | có (OCR) |
| 106/2025/NĐ-CP | 15/05/2025 | xu phat VPHC PCCC CNCH | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/pccc/ND-106-2025-NDCP-xu-phat-VPHC-PCCC-CNCH.docx` | có |
| 24/2025/TT-BCT | 13/05/2025 | ke hoach quan ly rui ro | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/TT-24-2025-TT-BCT-ke-hoach-quan-ly-rui-ro.docx` | có |
| 02/2025/TT-BXD | 31/03/2025 | sua doi TT 06 2021 | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/TT-02-2025-TT-BXD-sua-doi-TT-06-2021.docx` | có |
| 24/2025/NĐ-CP | 21/02/2025 | sua doi ND 98 2020 | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/thuong-mai/ND-24-2025-NDCP-sua-doi-ND-98-2020.docx` | có |
| 334/QĐ-BCT | 06/02/2025 | dinh chinh TT 38 | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/QD-334-QD-BCT-06-02-2025-dinh-chinh-TT-38.txt` | có |
| 232/QĐ-TTg | 24/01/2025 | de an thi truong cac bon | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/QD-232-QD-TTg-24-01-2025-de-an-thi-truong-cac-bon.txt` | có |
| 181/2024/NĐ-CP | 31/12/2024 |  | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/van-ban-goc/ND-181-2024.docx` | có |
| 181/2024/NĐ-CP | 31/12/2024 | Quy dinh chi tiet ve VLNCN va tien chat thuoc no | kho-vlncn-sct-vn | `kho-vlncn-sct-vn/skills/kho-vlncn-sct-vn/van-ban-goc/2024.12.31-181.2024.ND.CP-Quy-dinh-chi-tiet-ve-VLNCN-va-tien-chat-thuoc-no.docx` | có |
| 181/2024/NĐ-CP | 31/12/2024 |  | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/ND-181-2024.docx` | có |
| 175/2024/NĐ-CP | 30/12/2024 | quan ly hoat dong xay dung CU | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/ND-175-2024-quan-ly-hoat-dong-xay-dung-CU.docx` | có |
| 168/2024/NĐ-CP | 26/12/2024 | xu phat TTATGT duong bo | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/giao-thong/ND-168-2024-NDCP-xu-phat-TTATGT-duong-bo.docx` | có |
| 158/2024/NĐ-CP | 18/12/2024 | van tai duong bo | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/02-nghi-dinh/ND-158-2024-van-tai-duong-bo.docx` | có |
| 161/2024/NĐ-CP | 18/12/2024 | HHNH text | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/02-nghi-dinh/ND-161-2024-HHNH-text.doc` | có |
| — | 18/12/2024 | PL1 danh muc HHNH | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/05-phu-luc-bieu-mau/PL1-danh-muc-HHNH.docx` | có |
| — | 18/12/2024 | PL3 bieu trung nguy hiem | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/05-phu-luc-bieu-mau/PL3-bieu-trung-nguy-hiem.pdf` | có (OCR) |
| — | 18/12/2024 | PL4 giay de nghi cap moi | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/05-phu-luc-bieu-mau/PL4-giay-de-nghi-cap-moi.pdf` | có (OCR) |
| — | 18/12/2024 | PL4b giay de nghi dieu chinh | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/05-phu-luc-bieu-mau/PL4b-giay-de-nghi-dieu-chinh.pdf` | có (OCR) |
| 54/2024/QH15 | 29/11/2024 | Dia chat va khoang san TOAN VAN | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/Luat-54-2024-QH15-Dia-chat-va-khoang-san-TOAN-VAN.docx` | có |
| 54/2024/QH15 | 29/11/2024 | tom tat dieu chinh | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/Luat-54-2024-QH15-tom-tat-dieu-chinh.docx` | có |
| 1422/QĐ-TTg | 19/11/2024 | ke hoach thich ung BDKH | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/QD-1422-QD-TTg-19-11-2024-ke-hoach-thich-ung-BDKH.txt` | có |
| 149/2024/NĐ-CP | 15/11/2024 | Quy dinh chi tiet Luat Quan ly vu khi VLN va CCHT | kho-vlncn-sct-vn | `kho-vlncn-sct-vn/skills/kho-vlncn-sct-vn/van-ban-goc/2024.11.15-149.2024.ND.CP-Quy-dinh-chi-tiet-Luat-Quan-ly-vu-khi-VLN-va-CCHT.pdf` | có (OCR) |
| 149/2024/NĐ-CP | 15/11/2024 | Quy dinh chi tiet Luat 42 2024 phan Bo Cong an | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/2024.11.15-149.2024.ND.CP-Quy-dinh-chi-tiet-Luat-42-2024-phan-Bo-Cong-an.docx` | có |
| 75/2024/TT-BCA | 15/11/2024 | Tham quyen cap giay phep van chuyen VLNCN | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/2024.11.15-75.2024.TT.BCA-Tham-quyen-cap-giay-phep-van-chuyen-VLNCN.docx` | có |
| 98/2024/TT-BQP | 15/11/2024 | VLNCN TCTN thuoc Bo Quoc phong | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/2024.11.15-98.2024.TT.BQP-VLNCN-TCTN-thuoc-Bo-Quoc-phong.docx` | có |
| 23/2024/TT-BCT | 07/11/2024 | Quan ly su dung VLNCN tien chat thuoc no thuoc BCT | kho-vlncn-sct-vn | `kho-vlncn-sct-vn/skills/kho-vlncn-sct-vn/van-ban-goc/2024.11.07-23.2024.TT.BCT-Quan-ly-su-dung-VLNCN-tien-chat-thuoc-no-thuoc-BCT.docx` | có |
| 23/2024/TT-BCT | 07/11/2024 |  | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/TT-23-2024-BCT.docx` | có |
| 467/TB-VPCP | 14/10/2024 | ket luan de an thi truong cac bon | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/TB-467-TB-VPCP-14-10-2024-ket-luan-de-an-thi-truong-cac-bon.txt` | có |
| 19/2024/TT-BCT | 10/10/2024 | sua QCVN05A | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/van-ban-goc/03-thong-tu/TT-19-2024-BCT-sua-QCVN05A.docx` | có |
| QCVN 05A:2020/BCT-SD1 | 10/10/2024 | 2024 | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/van-ban-goc/04-qcvn-tcvn/QCVN-05A-2020-BCT-SD1-2024.docx` | có |
| 123/2024/NĐ-CP | 04/10/2024 | xu phat dat dai | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/dat-dai/ND-123-2024-NDCP-xu-phat-dat-dai.docx` | có |
| 14/2024/TT-BCT | 15/08/2024 | che do bao cao mau van ban CCN | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/TT-14-2024-che-do-bao-cao-mau-van-ban-CCN.docx` | có |
| 09/KH-BTNMT | 06/08/2024 | trien khai CT 13 | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/KH-09-KH-BTNMT-06-8-2024-trien-khai-CT-13.txt` | có |
| 102/2024/NĐ-CP | 30/07/2024 | chi tiet Luat Dat dai | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/trung-uong/ND-102-2024-ND-CP-chi-tiet-Luat-Dat-dai.docx` | có |
| 101/2024/NĐ-CP | 29/07/2024 | dieu tra dang ky cap giay chung nhan | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/trung-uong/ND-101-2024-ND-CP-dieu-tra-dang-ky-cap-giay-chung-nhan.docx` | có |
| 88/2024/NĐ-CP | 15/07/2024 | boi thuong ho tro tai dinh cu | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/trung-uong/ND-88-2024-ND-CP-boi-thuong-ho-tro-tai-dinh-cu.docx` | có |
| 43/2024/QH15 | 29/06/2024 | sua doi Luat Dat dai | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/trung-uong/Luat-43-2024-QH15-sua-doi-Luat-Dat-dai.docx` | có |
| 23/2024/TT-BCT | 29/06/2024 | tienchat | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/03-thong-tu/TT-23-2024-BCT-tienchat.pdf` | có (OCR) |
| 42/2024/QH15 | 29/06/2024 | Luat Quan ly su dung vu khi vat lieu no va CCHT | kho-vlncn-sct-vn | `kho-vlncn-sct-vn/skills/kho-vlncn-sct-vn/van-ban-goc/2024.06.29-42.2024.QH15-Luat-Quan-ly-su-dung-vu-khi-vat-lieu-no-va-CCHT.docx` | có |
| 42/2024/QH15 | 29/06/2024 |  | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/Luat-42-2024-QH15.docx` | có |
| 71/2024/NĐ-CP | 27/06/2024 | gia dat | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/trung-uong/ND-71-2024-ND-CP-gia-dat.docx` | có |
| 35/2024/QH15 | 27/06/2024 | Luat Duong bo 35 2024 text | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/01-luat/Luat-Duong-bo-35-2024-text.docx` | có |
| 13/CT-TTg | 02/05/2024 | quan ly tin chi cac bon | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/CT-13-CT-TTg-02-5-2024-quan-ly-tin-chi-cac-bon.txt` | có |
| 34/2024/NĐ-CP | 31/03/2024 | CWC vukhihoahoc | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/van-ban-goc/02-nghi-dinh/ND-34-2024-CWC-vukhihoahoc.docx` | có |
| 32/2024/NĐ-CP | 15/03/2024 | quan ly phat trien CCN | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/ND-32-2024-quan-ly-phat-trien-CCN.docx` | có |
| 31/2024/QH15 | 18/01/2024 | Luat Dat dai 31 2024 QH15 | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/trung-uong/Luat-Dat-dai-31-2024-QH15.docx` | có |
| 28/2023/TT-BTNMT | 29/12/2023 | dinh muc MRV linh vuc chat thai | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/TT-28-2023-TT-BTNMT-29-12-2023-dinh-muc-MRV-linh-vuc-chat-thai.txt` | có |
| 43/2023/TT-BCT | 28/12/2023 | Sửa đổi TT 57.2018 về kinh doanh thuốc lá | attp-sct-vn | `attp-sct-vn/skills/attp-sct-vn/van-ban-goc/2023.12.28 43.2023.TT.BCT Sửa đổi TT 57.2018 về kinh doanh thuốc lá.pdf` | có (OCR) |
| 38/2023/TT-BCT | 27/12/2023 | MRV KNK nganh Cong Thuong | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/TT-38-2023-TT-BCT-27-12-2023-MRV-KNK-nganh-Cong-Thuong.txt` | có |
| 37/TT-BGTVT | 13/12/2023 |  | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/03-thong-tu/TT-37-BGTVT.pdf` | có |
| 9416/VPCP-QHQT | 30/11/2023 | thoa thuan VN Singapore | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/CV-9416-VPCP-QHQT-30-11-2023-thoa-thuan-VN-Singapore.txt` | có |
| 35/2023/NĐ-CP | 20/06/2023 | sua cac ND BXD | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/ND-35-2023-sua-cac-ND-BXD.docx` | có |
| 334/QĐ-TTg | 01/04/2023 | chien luoc dia chat khoang san cong nghiep khai khoang 2030 2045 | quy-hoach-ct-vn | `quy-hoach-ct-vn/skills/quy-hoach-ct-vn/van-ban-goc/QD-334-QD-TTg-01-4-2023-chien-luoc-dia-chat-khoang-san-cong-nghiep-khai-khoang-2030-2045.docx` | có |
| 896/QĐ-TTg | 26/07/2022 | chien luoc BDKH 2050 | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/QD-896-QD-TTg-26-7-2022-chien-luoc-BDKH-2050.txt` | có |
| 88/NQ-CP | 22/07/2022 | chuong trinh hanh dong thuc hien NQ 10 NQ TW | quy-hoach-ct-vn | `quy-hoach-ct-vn/skills/quy-hoach-ct-vn/van-ban-goc/NQ-88-NQ-CP-22-7-2022-chuong-trinh-hanh-dong-thuc-hien-NQ-10-NQ-TW.docx` | có |
| 45/2022/NĐ-CP | 07/07/2022 | xu phat bao ve moi truong | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/moi-truong/ND-45-2022-NDCP-xu-phat-bao-ve-moi-truong.docx` | có |
| 10-NQ/TW | 10/02/2022 | dinh huong chien luoc dia chat khoang san cong nghiep khai khoang | quy-hoach-ct-vn | `quy-hoach-ct-vn/skills/quy-hoach-ct-vn/van-ban-goc/NQ-10-NQ-TW-10-02-2022-dinh-huong-chien-luoc-dia-chat-khoang-san-cong-nghiep-khai-khoang.docx` | có |
| 17/2022/NĐ-CP | 31/01/2022 | Sua doi cac nghi dinh xu phat VPHC linh vuc cong thuong | kho-vlncn-sct-vn | `kho-vlncn-sct-vn/skills/kho-vlncn-sct-vn/van-ban-goc/2022.01.31-17.2022.ND.CP-Sua-doi-cac-nghi-dinh-xu-phat-VPHC-linh-vuc-cong-thuong.pdf` | có (OCR) |
| 17/2022/NĐ-CP | 31/01/2022 | sua doi ND 71 2019 134 2013 98 2020 99 2020 | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/chung/ND-17-2022-NDCP-sua-doi-ND-71-2019-134-2013-98-2020-99-2020.docx` | có |
| 154/QĐ-TTg | 29/01/2022 | keo dai ky quy hoach khoang san VLXD xi mang | quy-hoach-ct-vn | `quy-hoach-ct-vn/skills/quy-hoach-ct-vn/van-ban-goc/QD-154-QD-TTg-29-01-2022-keo-dai-ky-quy-hoach-khoang-san-VLXD-xi-mang.docx` | có |
| 16/2022/NĐ-CP | 28/01/2022 | xu phat xay dung | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/xay-dung/ND-16-2022-NDCP-xu-phat-xay-dung.docx` | có |
| 648/VPCP-NN | 26/01/2022 | de an thi truong cac bon | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/CV-648-VPCP-NN-26-01-2022-de-an-thi-truong-cac-bon.txt` | có |
| 06/2022/NĐ-CP | 07/01/2022 | giam nhe KNK o don | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/ND-06-2022-ND-CP-07-01-2022-giam-nhe-KNK-o-don.txt` | có |
| 04/2022/NĐ-CP | 06/01/2022 | sua doi ND 36 2020 va ND 91 2019 dat dai | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/khoang-san/ND-04-2022-NDCP-sua-doi-ND-36-2020-va-ND-91-2019-dat-dai.docx` | có |
| 8520/BCT-KHCN | 30/12/2021 | Cong van huong dan thuc hien quy dinh linh vuc an toan thuc pham | attp-sct-vn | `attp-sct-vn/skills/attp-sct-vn/van-ban-goc/2021.12.30 8520.BCT.KHCN Cong van huong dan thuc hien quy dinh linh vuc an toan thuc pham.pdf` | có (OCR) |
| 25/2026/VBHN-NĐ | 30/12/2021 | xu phat SHCN ban sao y UBND tinh | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/so-huu-cong-nghiep/VBHN-25-2026-ND-xu-phat-SHCN_ban-sao-y-UBND-tinh.pdf` | có (OCR) |
| 124/2021/NĐ-CP | 28/12/2021 | sua doi ND 115 2018 va ND 117 2020 | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/attp/ND-124-2021-NDCP-sua-doi-ND-115-2018-va-ND-117-2020.docx` | có |
| 122/2021/NĐ-CP | 28/12/2021 | xu phat ke hoach dau tu | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/dau-tu/ND-122-2021-NDCP-xu-phat-ke-hoach-dau-tu.docx` | có |
| 118/2021/NĐ-CP | 23/12/2021 | Phu luc bieu mau MQD01 42 MBB01 30 | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/chung/ND-118-2021-NDCP-Phu-luc-bieu-mau-MQD01-42-MBB01-30.docx` | có |
| 118/2021/NĐ-CP | 23/12/2021 | quy dinh chi tiet Luat XLVPHC ban goc chua hop nhat 68 190 2025 | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/chung/ND-118-2021-NDCP-quy-dinh-chi-tiet-Luat-XLVPHC_ban-goc-chua-hop-nhat-68-190-2025.docx` | có |
| 06/2021/TT-BXD | 30/06/2021 | phan cap cong trinh CU | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/TT-06-2021-TT-BXD-phan-cap-cong-trinh-CU.docx` | có |
| 3479/VPCP-NN | 26/05/2021 | thi diem tin chi rung Quang Nam | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/CV-3479-VPCP-NN-26-5-2021-thi-diem-tin-chi-rung-Quang-Nam.txt` | có |
| — | 27/04/2021 | VD BoCT cap GP Cty TQ | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/07-tham-khao/VD-BoCT-cap-GP-Cty-TQ.pdf` | có (OCR) |
| 06/2021/NĐ-CP | 26/01/2021 | QLCL thi cong bao tri CU | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/van-ban-goc/ND-06-2021-QLCL-thi-cong-bao-tri-CU.docx` | có |
| 47/2020/TT-BCT | 21/12/2020 | QCVN 04 2020 BCT Chat luong tien chat thuoc no | kho-vlncn-sct-vn | `kho-vlncn-sct-vn/skills/kho-vlncn-sct-vn/van-ban-goc/2020.12.21-47.2020.TT.BCT-QCVN-04-2020-BCT-Chat-luong-tien-chat-thuoc-no.docx` | có |
| 37/2020/TT-BCT | 30/11/2020 | taphuan | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/03-thong-tu/TT-37-2020-BCT-taphuan.docx` | có |
| 98/2020/NĐ-CP | 26/08/2020 | xu phat thuong mai hang gia ban goc chua hop nhat 17 2022 | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/thuong-mai/ND-98-2020-NDCP-xu-phat-thuong-mai-hang-gia-ban-goc-chua-hop-nhat-17-2022.docx` | có |
| 99/2020/NĐ-CP | 26/08/2020 | xu phat dau khi xang dau khi ban goc chua hop nhat 17 2022 | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/xang-dau-khi/ND-99-2020-NDCP-xu-phat-dau-khi-xang-dau-khi-ban-goc-chua-hop-nhat-17-2022.docx` | có |
| 36/2020/NĐ-CP | 24/03/2020 | xu phat tai nguyen nuoc khoang san ban goc chua hop nhat 04 2022 | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/khoang-san/ND-36-2020-NDCP-xu-phat-tai-nguyen-nuoc-khoang-san-ban-goc-chua-hop-nhat-04-2022.docx` | có |
| 32/2019/TT-BCT | 21/11/2019 | QCVN 01 2019 | kho-vlncn-sct-vn | `kho-vlncn-sct-vn/skills/kho-vlncn-sct-vn/van-ban-goc/TT-32-2019-BCT_QCVN-01-2019.doc` | có |
| 836/QĐ-BXD | 14/10/2019 | ke hoach lap quy hoach khoang san lam VLXD 2021 2030 | quy-hoach-ct-vn | `quy-hoach-ct-vn/skills/quy-hoach-ct-vn/van-ban-goc/QD-836-QD-BXD-14-10-2019-ke-hoach-lap-quy-hoach-khoang-san-lam-VLXD-2021-2030.docx` | có |
| 71/2019/NĐ-CP | 30/08/2019 | xu phat VPHC hoachat VLNCN | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/van-ban-goc/05-xu-phat-kiem-tra/ND-71-2019-xu-phat-VPHC-hoachat-VLNCN.docx` | có |
| 71/2019/NĐ-CP | 30/08/2019 | Xu phat VPHC linh vuc hoa chat va VLNCN | kho-vlncn-sct-vn | `kho-vlncn-sct-vn/skills/kho-vlncn-sct-vn/van-ban-goc/2019.08.30-71.2019.ND.CP-Xu-phat-VPHC-linh-vuc-hoa-chat-va-VLNCN.pdf` | có (OCR) |
| 71/2019/NĐ-CP | 30/08/2019 | xu phat | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/ND-71-2019-xu-phat.docx` | có |
| 57/2018/TT-BCT | 26/12/2018 | Quy định chi tiết các NĐ về kinh doanh thuốc lá | attp-sct-vn | `attp-sct-vn/skills/attp-sct-vn/van-ban-goc/2018.12.26 57.2018.TT.BCT Quy định chi tiết các NĐ về kinh doanh thuốc lá.pdf` | có (OCR) |
| 43/2018/TT-BCT | 15/11/2018 | Thông tư quản lý ATTP thuộc trách nhiệm Bộ Công Thương | attp-sct-vn | `attp-sct-vn/skills/attp-sct-vn/van-ban-goc/2018.11.15 43.2018.TT.BCT Thông tư quản lý ATTP thuộc trách nhiệm Bộ Công Thương.pdf` | có (OCR) |
| 115/2018/NĐ-CP | 04/09/2018 | xu phat ATTP ban goc chua hop nhat 124 2021 | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/attp/ND-115-2018-NDCP-xu-phat-ATTP-ban-goc-chua-hop-nhat-124-2021.docx` | có |
| 16/2018/TT-BCA | 15/05/2018 | tienchat | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/03-thong-tu/TT-16-2018-BCA-tienchat.doc` | có |
| 3109/BCT-KHCN | 20/04/2018 | Cong van huong dan thuc hien cong tac quan ly an toan thuc pham | attp-sct-vn | `attp-sct-vn/skills/attp-sct-vn/van-ban-goc/2018.04.20 3109.BCT.KHCN Cong van huong dan thuc hien cong tac quan ly an toan thuc pham.pdf` | có (OCR) |
| 15/2018/NĐ-CP | 02/02/2018 | Nghị định quy định chi tiết Luật ATTP (bản text trích được) | attp-sct-vn | `attp-sct-vn/skills/attp-sct-vn/van-ban-goc/2018.02.02 15.2018.NĐ.CP Nghị định quy định chi tiết Luật ATTP (bản text trích được).txt` | có |
| 15/2018/NĐ-CP | 02/02/2018 | Nghị định quy định chi tiết thi hành một số điều của Luật An toàn thực phẩm | attp-sct-vn | `attp-sct-vn/skills/attp-sct-vn/van-ban-goc/2018.02.02 15.2018.NĐ.CP Nghị định quy định chi tiết thi hành một số điều của Luật An toàn thực phẩm.doc` | có |
| 16/2017/QH14 | 15/11/2017 | Luat Lam nghiep 16 2017 QH14 15 11 2017 | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/Luat-Lam-nghiep-16-2017-QH14-15-11-2017.txt` | có |
| 419/QĐ-TTg | 05/04/2017 | chuong trinh REDD plus | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/QD-419-QD-TTg-05-4-2017-chuong-trinh-REDD-plus.txt` | có |
| 1803/QĐ-TTg | 22/10/2015 | an PMR WB | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/QD-1803-QD-TTg-22-10-2015-du-an-PMR-WB.txt` | có |
| 84/2015/QH13 | 25/06/2015 | An toan ve sinh lao dong | atvsld-sct-vn | `atvsld-sct-vn/skills/atvsld-sct-vn/van-ban-goc/Luat-84-2015-QH13-An-toan-ve-sinh-lao-dong.docx` | có |
| 1215/QĐ-BNN-TCCB | 02/06/2014 | quy che BCD REDD | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/QD-1215-QD-BNN-TCCB-02-6-2014-quy-che-BCD-REDD.txt` | có |
| 1775/QĐ-TTg | 21/11/2012 | de an quan ly phat thai tin chi | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/QD-1775-QD-TTg-21-11-2012-de-an-quan-ly-phat-thai-tin-chi.txt` | có |
| 07/CT-TTg | 02/03/2012 | chan chinh KKT KCN CCN | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/CT-07-2012-TTg-chan-chinh-KKT-KCN-CCN.docx` | có |
| — | 22/11/1994 | Nghi dinh thu Viet Trung | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/02-nghi-dinh/Nghi-dinh-thu-Viet-Trung.pdf` | có |
| — | — | DU THAO 2024 Phu luc I QD 13 2024 linh vuc THAM KHAO | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/DU-THAO-2024-Phu-luc-I-QD-13-2024-linh-vuc-THAM-KHAO.txt` | có |
| — | — | DU THAO 2024 Phu luc II QD 13 2024 nganh cong thuong THAM KHAO | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/DU-THAO-2024-Phu-luc-II-QD-13-2024-nganh-cong-thuong-THAM-KHAO.txt` | có |
| — | — | DU THAO 2024 Phu luc III QD 13 2024 GTVT THAM KHAO | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/DU-THAO-2024-Phu-luc-III-QD-13-2024-GTVT-THAM-KHAO.txt` | có |
| — | — | DU THAO 2024 Phu luc IV QD 13 2024 xay dung THAM KHAO | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/DU-THAO-2024-Phu-luc-IV-QD-13-2024-xay-dung-THAM-KHAO.txt` | có |
| — | — | Du thao De an 13 Tinh uy ban UBND tinh KHONG TRICH SO | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/Du-thao-De-an-13-Tinh-uy-ban-UBND-tinh-KHONG-TRICH-SO.txt` | có |
| — | — | Ghi chu chuc nang QLNN BVMT cua So Cong Thuong | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/Ghi-chu-chuc-nang-QLNN-BVMT-cua-So-Cong-Thuong.txt` | có |
| — | — | UNFCCC Cong uoc khung LHQ ve BDKH ban dich | bvmt-sct-vn | `bvmt-sct-vn/skills/bvmt-sct-vn/van-ban-goc/knk-bdkh/UNFCCC-Cong-uoc-khung-LHQ-ve-BDKH-ban-dich.txt` | có |
| — | — | So tay BTHTTDC SNNMT Lao Cai 7 2026 | dat-dai-sct-vn | `dat-dai-sct-vn/skills/dat-dai-sct-vn/van-ban-goc/So-tay-BTHTTDC-SNNMT-Lao-Cai-7-2026.pdf` | có (OCR) |
| TCVN 5507:2002 | — |  | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/van-ban-goc/04-qcvn-tcvn/TCVN-5507-2002.doc` | có |
| 06/2007/QH12 | — | Danh muc VBQPPL hoa chat | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/van-ban-goc/06-danh-muc-cong-van/Danh-muc-VBQPPL-hoa-chat.docx` | có |
| — | — | Phu luc danh muc uy quyen VLNCN TTHC 2.000229 2.000210 | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/van-ban-goc/Phu-luc-danh-muc-uy-quyen-VLNCN_TTHC-2.000229-2.000210.docx` | có |
| — | — | Hiep dinh van tai VN TQ | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/04-uy-quyen-quy-trinh/Hiep-dinh-van-tai-VN-TQ.pdf` | có |
| — | — | Quy trinh noi bo TTHC HHNH | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/04-uy-quyen-quy-trinh/Quy-trinh-noi-bo-TTHC-HHNH.docx` | có |
| — | — | Dieu 15 thanh phan ho so | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/05-phu-luc-bieu-mau/Dieu-15-thanh-phan-ho-so.docx` | có |
| — | — | Dieu 6 bao bi thung chua | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/05-phu-luc-bieu-mau/Dieu-6-bao-bi-thung-chua.docx` | có |
| — | — | Mau phuong an VC tham khao | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/05-phu-luc-bieu-mau/Mau-phuong-an-VC-tham-khao.docx` | có |
| — | — | PL1 danh muc HHNH mausac | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/05-phu-luc-bieu-mau/PL1-danh-muc-HHNH-mausac.xlsx` | có |
| — | — | PL2 so hieu nguy hiem | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/05-phu-luc-bieu-mau/PL2-so-hieu-nguy-hiem.pdf` | có (OCR) |
| — | — | PL5 phuong an to chuc | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/05-phu-luc-bieu-mau/PL5-phuong-an-to-chuc.pdf` | có (OCR) |
| — | — | PL8 mau giay phep | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/05-phu-luc-bieu-mau/PL8-mau-giay-phep.pdf` | có (OCR) |
| ĐLVN 05:2017 | — | kiem dinh xi tec | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/07-tham-khao/DLVN-05-2017-kiem-dinh-xi-tec.pdf` | có |
| — | — | Danh sach UN numbers | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/07-tham-khao/Danh-sach-UN-numbers.pdf` | có |
| — | — | VD BoKHCN cap GP Cty TQ | hnh-sct-vn | `hnh-sct-vn/skills/hnh-sct-vn/van-ban-goc/07-tham-khao/VD-BoKHCN-cap-GP-Cty-TQ.pdf` | có (OCR) |
| QĐ 2336/2026 | — | CTDT KCN Phu Xuan | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/QD-2336-2026-CTDT-KCN-Phu-Xuan.pdf` | có (OCR) |
| QĐ 2338/2026 | — | CTDT KCN Phu Xuan 1 | kccn-sct-vn | `kccn-sct-vn/skills/kccn-sct-vn/van-ban-goc/QD-2338-2026-CTDT-KCN-Phu-Xuan-1.pdf` | có (OCR) |
| — | — | BC UBND QLNN khoang san nam 2025 | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/BC-UBND-QLNN-khoang-san-nam-2025.docx` | có |
| — | — | BC tinh ket qua Chi thi 38 TTg | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/BC-tinh-ket-qua-Chi-thi-38-TTg.docx` | có |
| — | — | CV SNNMT 8 2025 huong dan DN thuc hien Luat DCKS | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/CV-SNNMT-8-2025-huong-dan-DN-thuc-hien-Luat-DCKS.docx` | có |
| — | — | CV UBND bao ve khoang san chua khai thac | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/CV-UBND-bao-ve-khoang-san-chua-khai-thac.docx` | có |
| — | — | Danh muc VBPL khoang san | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/Danh-muc-VBPL-khoang-san.docx` | có |
| — | — | KH UBND trien khai Chi thi 11 CT TU QLNN khoang san | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/van-ban-goc/KH-UBND-trien-khai-Chi-thi-11-CT-TU-QLNN-khoang-san.docx` | có |
| — | — | Ghi chu nghiep vu trong qua trinh su dung VLNCN | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/Ghi-chu-nghiep-vu-trong-qua-trinh-su-dung-VLNCN.docx` | có |
| 17/2022/NĐ-CP | — | sua doi xu phat | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/van-ban-goc/ND-17-2022-sua-doi-xu-phat.pdf` | có (OCR) |
| 31/2025/TT-BCT | — | 10 phu luc toan van | tkm-sct-vn | `tkm-sct-vn/skills/tkm-sct-vn/van-ban-goc/TT-31-2025-TT-BCT-10-phu-luc-toan-van.doc` | có |
| TT 31/2025 | — | than 6 dieu | tkm-sct-vn | `tkm-sct-vn/skills/tkm-sct-vn/van-ban-goc/TT-31-2025-than-6-dieu.md` | có |
| 88/2025/QH15 | — | sua doi Luat XLVPHC ban scan co dau | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/chung/Luat-88-2025-QH15-sua-doi-Luat-XLVPHC_ban-scan-co-dau.pdf` | có (OCR) |
| — | — | Phieu sao y UBND tinh VBHN 25 2026 | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/van-ban-goc/so-huu-cong-nghiep/Phieu-sao-y-UBND-tinh_VBHN-25-2026.docx` | có |

## Văn bản có số hiệu trong vi-du-thuc-te/ (văn bản đi, đến đã dùng làm ví dụ)

| Số hiệu | Ngày | Tên | Plugin | Đường dẫn |
|---|---|---|---|---|
| 7962/UBND-NC | 06/08/2026 | chi dao thuc hien KL48 | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/vi-du-thuc-te/bo-ho-so-kiem-tra-HCM-TayBac/CV-7962-UBND-NC-06.8.2026-chi-dao-thuc-hien-KL48.pdf` |
| 45/KL-TT | 05/07/2026 | Thanh tra tinh Viglacera | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/vi-du-thuc-te/KL-45-Viglacera-thanh-tra-tinh/KL-45-KL-TT-05.7.2026-Thanh-tra-tinh-Viglacera.pdf` |
| KH 3957 | 03/07/2026 | Kiem tra cap GCN 19 don vi | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/vi-du-thuc-te/KH-3957_3.7.2026_Kiem-tra-cap-GCN-19-don-vi.docx` |
| TB 3915 | 01/07/2026 | Huan luyen nguoi quan ly | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/vi-du-thuc-te/TB-3915_1.7.2026_Huan-luyen-nguoi-quan-ly.docx` |
| KH 3898 | 30/06/2026 | Huan luyen nguoi quan ly | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/vi-du-thuc-te/KH-3898_30.6.2026_Huan-luyen-nguoi-quan-ly.docx` |
| QĐ 3770 | 25/06/2026 | Cong nhan KQ XD Mien Bac | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/vi-du-thuc-te/QD-3770_25.6.2026_Cong-nhan-KQ-XD-Mien-Bac.docx` |
| QĐ 3728 | 24/06/2026 | Cong nhan KQ Xi mang Yen Binh | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/vi-du-thuc-te/QD-3728_24.6.2026_Cong-nhan-KQ-Xi-mang-Yen-Binh.docx` |
| BĐK 72 | 19/06/2026 | CV VS thu hoi da op lat di kem Viet Son Tang Loong | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/vi-du-thuc-te/BDK-72-CV-VS-19-6-2026-thu-hoi-da-op-lat-di-kem-Viet-Son-Tang-Loong.pdf` |
| CV 3155 | 02/06/2026 | Tu choi nguoi quan ly sai nganh Van Thinh | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/vi-du-thuc-te/CV-3155_2.6.2026_Tu-choi-nguoi-quan-ly-sai-nganh_Van-Thinh.docx` |
| TB 3059 | 29/05/2026 | Kiem tra Sin Quyen 2 dot | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/vi-du-thuc-te/TB-3059_29.5.2026_Kiem-tra-Sin-Quyen-2-dot.docx` |
| 10/BĐK-DK-PLNC | 28/05/2026 | thu hoi KS di kem che bien cao lanh Son Man | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/vi-du-thuc-te/BDK-10-DK-PLNC-28-5-2026-thu-hoi-KS-di-kem-che-bien-cao-lanh-Son-Man.pdf` |
| KH 3024 | 27/05/2026 | Ky rieng Sin Quyen | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/vi-du-thuc-te/KH-3024_27.5.2026_Ky-rieng-Sin-Quyen.docx` |
| KH 2242 | 23/04/2026 | Kiem tra cap GCN 28 don vi | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/vi-du-thuc-te/KH-2242_23.4.2026_Kiem-tra-cap-GCN-28-don-vi.docx` |
| TB 2245 | 23/04/2026 | To chuc kiem tra ky chung | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/vi-du-thuc-te/TB-2245_23.4.2026_To-chuc-kiem-tra-ky-chung.docx` |
| — | 13/04/2026 | TB 13.4.2026 Kiem tra tai tru so Hoa chat mo Tay Bac | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/vi-du-thuc-te/TB_13.4.2026_Kiem-tra-tai-tru-so-Hoa-chat-mo-Tay-Bac.docx` |
| TB 1894 | 09/04/2026 | Ket qua sau kiem tra chap hanh | hl-vlncn-sct-vn | `hl-vlncn-sct-vn/skills/hl-vlncn-sct-vn/vi-du-thuc-te/TB-1894_9.4.2026_Ket-qua-sau-kiem-tra-chap-hanh.docx` |
| TB 1894 | 09/04/2026 | ket qua sau kiem tra VLNCN ban ky | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/vi-du-thuc-te/TB-1894-ket-qua-sau-kiem-tra-VLNCN-ban-ky.pdf` |
| 1105/KH-ĐKT | 10/03/2026 | ke hoach kiem tra | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/vi-du-thuc-te/KH-1105-DKT-ke-hoach-kiem-tra.pdf` |
| QĐ 1050 | 06/03/2026 | kiem tra VLNCN 2026 | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/vi-du-thuc-te/QD-1050-kiem-tra-VLNCN-2026.pdf` |
| 1080/SNNMT-KS | 11/02/2026 | xin y kien thu hoi KS mo da hoa Lang Lanh II Chan Thien My | qlks-sct-vn | `qlks-sct-vn/skills/qlks-sct-vn/vi-du-thuc-te/CV-1080-SNNMT-KS-11-02-2026-xin-y-kien-thu-hoi-KS-mo-da-hoa-Lang-Lanh-II-Chan-Thien-My.pdf` |
| 26/QĐ-XPVPHC | — | 2026 Cuc Hoa chat xu phat TNHH TM Hai Dang | hc-sct-vn | `hc-sct-vn/skills/hc-sct-vn/vi-du-thuc-te/xu-phat/QD-26-QD-XPVPHC-2026-Cuc-Hoa-chat-xu-phat-TNHH-TM-Hai-Dang.pdf` |
| 2373/UBND | — | chi dao tu huong dan dich vu no min 2025 | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/vi-du-thuc-te/CV-2373-UBND-chi-dao-tu-huong-dan-dich-vu-no-min-2025.pdf` |
| CV 4280 | — | tra ho so Thanh Huong 2026 | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/vi-du-thuc-te/CV-4280-tra-ho-so-Thanh-Huong-2026.pdf` |
| CV 4378 | — | tra ho so Mong Son 2026 | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/vi-du-thuc-te/CV-4378-tra-ho-so-Mong-Son-2026.pdf` |
| 473/VPUBND | — | tra ho so Dong Khe 2025 | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/vi-du-thuc-te/CV-473-VPUBND-tra-ho-so-Dong-Khe-2025.pdf` |
| 565/VPUBND | — | tra ho so QL4D Muong Khuong 2025 | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/vi-du-thuc-te/CV-565-VPUBND-tra-ho-so-QL4D-Muong-Khuong-2025.pdf` |
| TB 1894 | — | ket qua sau kiem tra VLNCN | sd-vlncn-sct-vn | `sd-vlncn-sct-vn/skills/sd-vlncn-sct-vn/vi-du-thuc-te/TB-1894-ket-qua-sau-kiem-tra-VLNCN.docx` |
| CV 573 | — | Âu Lâu | xd-sct-vn | `xd-sct-vn/skills/xd-sct-vn/vi-du-thuc-te/au-lau-110kv-tham-dinh-BCNCKT/ho-so/CV 573 Âu Lâu.pdf` |
| TB 2948 | — | thong bao don vi Dieu 7 TT56 | xp-hc-vlncn-sct-vn | `xp-hc-vlncn-sct-vn/skills/xp-hc-vlncn-sct-vn/vi-du-thuc-te/bo-ho-so-xu-phat-Khi-cong-nghiep-mau-that/TB-2948-thong-bao-don-vi-Dieu-7-TT56.pdf` |
| TB 2948 | — | thong bao don vi Dieu 7 TT56 | xp-sct-vn | `xp-sct-vn/skills/xp-sct-vn/vi-du-thuc-te/bo-ho-so-xu-phat-Khi-cong-nghiep-mau-that/TB-2948-thong-bao-don-vi-Dieu-7-TT56.pdf` |

## Cùng số hiệu ở nhiều plugin (chờ Bạn chốt plugin chủ; chưa xóa)

- 09/2026/TT-BQP — hl-vlncn-sct-vn, sd-vlncn-sct-vn
- 118/2025/QH15 — hl-vlncn-sct-vn, kho-vlncn-sct-vn, sd-vlncn-sct-vn
- 146/2025/NĐ-CP — hc-sct-vn, kho-vlncn-sct-vn, sd-vlncn-sct-vn
- 149/2024/NĐ-CP — kho-vlncn-sct-vn, sd-vlncn-sct-vn
- 17/2022/NĐ-CP — kho-vlncn-sct-vn, sd-vlncn-sct-vn, xp-sct-vn
- 181/2024/NĐ-CP — hl-vlncn-sct-vn, kho-vlncn-sct-vn, sd-vlncn-sct-vn
- 23/2024/TT-BCT — hnh-sct-vn, kho-vlncn-sct-vn, sd-vlncn-sct-vn
- 26/2026/TT-BCT — hnh-sct-vn, qlks-sct-vn
- 275/2026/NĐ-CP — xp-hc-vlncn-sct-vn, xp-sct-vn
- 282/2025/NĐ-CP — xp-hc-vlncn-sct-vn, xp-sct-vn
- 283/2026/NĐ-CP — atvsld-sct-vn, xp-sct-vn
- 347/2026/NĐ-CP — pccc-sct-vn, xd-sct-vn
- 38/2025/TT-BCT — kho-vlncn-sct-vn, sd-vlncn-sct-vn
- 42/2024/QH15 — kho-vlncn-sct-vn, sd-vlncn-sct-vn
- 56/2025/TT-BCT — xp-hc-vlncn-sct-vn, xp-sct-vn
- 66.18/2026/NQ-CP — hnh-sct-vn, xd-sct-vn
- 71/2019/NĐ-CP — hc-sct-vn, kho-vlncn-sct-vn, sd-vlncn-sct-vn
- 78/VBHN-VPQH — hl-vlncn-sct-vn, kho-vlncn-sct-vn, sd-vlncn-sct-vn, xp-hc-vlncn-sct-vn, xp-sct-vn

## Tệp đặt tên chưa theo quy ước YYYY.MM.DD-SỐ.KÝ.HIỆU-Tên: 282

Số hiệu, ngày của các tệp này đọc từ phần đầu bản .txt hoặc đoán từ tên tệp — đối chiếu bản gốc trước khi trích dẫn số/ngày.

