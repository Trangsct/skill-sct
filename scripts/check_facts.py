#!/usr/bin/env python3
"""Quét dữ kiện lỗi thời / quy ước cũ còn sót trong toàn bộ plugin.

Mỗi khi Bạn chốt một quy ước mới hoặc một dữ kiện đổi (ủy quyền mới, đổi chuyên viên,
đổi nơi nộp hồ sơ...), thêm MỘT mục vào danh sách RULES bên dưới; CI (validate-plugins.yml)
sẽ đỏ ở bất kỳ plugin nào còn dùng cách cũ.

    python3 scripts/check_facts.py            # quét, in vi phạm, exit 1 nếu có FAIL
    python3 scripts/check_facts.py --warn     # in cả WARN (không làm CI đỏ)
    python3 scripts/check_facts.py --list     # liệt kê các quy tắc đang áp dụng

Phạm vi quét: mọi file .md trong <plugin>/skills/<plugin>/ (SKILL.md, references, mau-van-ban,
checklists, INDEX), TRỪ CHANGELOG*, van-ban-goc/*.md (văn bản gốc), vi-du-thuc-te/ (lịch sử thật)
và các dòng chứa từ khóa lịch sử/ngoại lệ (xem ALLOW_LINE).

Cách viết một rule:
  {
    "id": "gp-ubnd-2867",           # mã ngắn, duy nhất
    "pattern": r"...",              # regex (Python, IGNORECASE), so khớp trên từng dòng (NFC)
    "why": "...",                   # vì sao sai, và cách ghi đúng
    "since": "2026-08-20",          # mốc dữ kiện đổi
    "level": "FAIL" | "WARN",
    "only": ["sd-vlncn-sct-vn"],    # (tùy chọn) chỉ quét các plugin này
    "skip": ["vbhc-vn"],            # (tùy chọn) bỏ qua các plugin này
  }
"""
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Dòng có các cụm này được coi là đang nói về LỊCH SỬ / ngoại lệ có chủ ý → không báo
ALLOW_LINE = re.compile(
    r"(đến 19/8/2026|trước 20/8/2026|đến hết 19/8|trước đây|lịch sử|cũ\)|\(cũ\)|đã bãi bỏ|"
    r"không sửa lại|giữ nguyên lịch sử|không dùng|KHÔNG ghi|không ghi|cấm|CẤM|sai:|SAI|"
    r"→ đúng|-> đúng|thay vì|đã sửa|đã thay|từng ghi|trước 10/7/2026|đến 14/7/2026|"
    r"quy ước cố định|check_facts|ghi nhầm|trích luật|nguyên văn\)|theo luật|nguồn ghi|cách gọi|NQ 34 \(12/2025\)|"
    r"không \"giai đoạn|vụ (QĐ )?5116|bị bác|bôi đỏ|KHÔNG viết|Không cài|không cài)",
    re.I,
)

RULES = [
    {
        "id": "ubnd-viet-tat-trong-mau",
        # Bạn chốt 04/10/2026: mọi VBHC viết "UBND tỉnh"; chữ đầy đủ chỉ ở tên cơ quan ban hành đầu trang
        # và khối ký "TM. ỦY BAN NHÂN DÂN" (viết hoa, không bị bắt). Chỉ quét mẫu văn bản (mau-van-ban/) và
        # chỉ nhắc (WARN) vì mẫu lấy từ văn bản đã ban hành; mẫu sửa dần, văn bản mới phải sạch (vbhc-vn R19).
        "pattern": r"^(?!.*(?:(?-i:ỦY BAN NHÂN DÂN)|lịch sử)).*(?-i:Ủy ban nhân dân tỉnh)",
        "why": "Từ 04/10/2026 viết 'UBND tỉnh' trong căn cứ, Kính gửi, thân, nơi nhận, phụ lục; chữ đầy đủ chỉ ở đầu trang và khối ký (vbhc-vn R19, Nhóm P9).",
        "since": "2026-10-04",
        "level": "WARN",
    },
    {
        "id": "kcn-cam-duong-chua-khoi-cong",
        # Bạn chốt 04/10/2026: KCN Cam Đường chưa khởi công; mốc "khởi công tháng 9/2026" là kế hoạch cũ.
        "pattern": r"^(?!.*(?:chưa khởi công|lịch sử|kế hoạch|ref 43|Cam Đường 1)).*KCN Cam Đường[^\n]{0,80}khởi công[^\n]{0,30}9/2026",
        "why": "KCN Cam Đường chưa khởi công (Bạn chốt 04/10/2026) — viết 'đang thực hiện GPMB', không ghi mốc khởi công tháng 9/2026 (kccn-sct-vn ref 43 mục A, ref 31 mục 13).",
        "since": "2026-10-04",
        "level": "FAIL",
        "only": ["kccn-sct-vn", "dacn-sct-vn", "bpb-sct-vn"],
    },
    {
        "id": "ccn-mong-son-tmdt-496-651",
        # File Excel của Phòng 02/10/2026 ghi nhầm 596,651 tỷ ở dòng chi tiết; QĐ 3426/QĐ-UBND ngày 23/9/2026: 496,651 tỷ.
        "pattern": r"^(?!.*(?:496,651|lịch sử)).*Mông Sơn[^\n]{0,80}596,651",
        "why": "Tổng mức đầu tư CCN Mông Sơn là 496,651 tỷ đồng (QĐ 3426/QĐ-UBND ngày 23/9/2026) — kccn-sct-vn ref 43 mục D, ref 41 mục A.",
        "since": "2026-10-04",
        "level": "FAIL",
        "only": ["kccn-sct-vn", "dacn-sct-vn", "bpb-sct-vn"],
    },
    {
        "id": "ccn-yen-the-lap-day-59-5",
        # Bạn chốt 01/10/2026: lấy số liệu theo xã (mới hơn) — BC 590/BC-UBND ngày 29/9/2026 của UBND xã Lục Yên:
        # 05 DN được giao/cho thuê 23,78/39,97 ha = 59,5%. Số 40,24% (Excel Phòng 28/9/2026) chỉ còn là lịch sử.
        "pattern": r"^(?!.*(?:59,5|lịch sử|ref 42|trước 01/10/2026)).*Yên Thế[^\n]{0,60}40,24",
        "why": "Lấp đầy CCN Yên Thế từ 01/10/2026 là 59,5% (23,78/39,97 ha, BC 590/BC-UBND ngày 29/9/2026 của UBND xã Lục Yên) — kccn-sct-vn ref 42 mục C.1, ref 31 mục 12.",
        "since": "2026-10-01",
        "level": "FAIL",
        "only": ["kccn-sct-vn", "dacn-sct-vn", "bpb-sct-vn"],
    },
    {
        "id": "ccn-hung-khanh-lap-day-32-75",
        # Bạn chốt 01/10/2026: BC 388/BC-UBND ngày 29/9/2026 của UBND xã Hưng Khánh — 6,55/20 ha = 32,75% (thay 29% và 49,3%).
        "pattern": r"^(?!.*(?:32,75|lịch sử|ref 42|trước 01/10/2026)).*Hưng Khánh[^\n]{0,40}(?:\b29(?:,0)? ?%|\b29;|49,3)",
        "why": "Lấp đầy CCN Hưng Khánh từ 01/10/2026 là 32,75% (6,55/20 ha, BC 388/BC-UBND ngày 29/9/2026 của UBND xã Hưng Khánh) — kccn-sct-vn ref 42 mục C.5.",
        "since": "2026-10-01",
        "level": "FAIL",
        "only": ["kccn-sct-vn", "dacn-sct-vn", "bpb-sct-vn"],
    },
    {
        "id": "ccn-phu-thinh-2-chua-co-qd-thue-dat",
        # Chốt 01/10/2026 theo BC 30/BC-THDA ngày 29/9/2026 của Công ty TNHH Lâm nghiệp 888 Yên Bái: "37 ha" là diện tích
        # đơn xin thuê đất GĐ1 (373.782,8 m², nộp 25/11/2025), CHƯA có quyết định cho thuê đất (hạn CĐT tự đặt 15/11/2026).
        "pattern": r"^(?!.*(?:đơn xin|chưa có QĐ|chưa có quyết định|ref 42|lịch sử)).*Phú Thịnh 2[^\n]{0,120}thuê đất \d{2}(?:[,.]\d+)? ha",
        "why": "CCN Phú Thịnh 2 chưa có quyết định cho thuê đất; 37,38 ha là diện tích đơn xin thuê đất giai đoạn 1 (25/11/2025) — viết 'đã nộp đơn xin thuê đất GĐ1 37,38 ha, chưa có QĐ cho thuê' (kccn-sct-vn ref 42 mục B.1, C.8).",
        "since": "2026-09-29",
        "level": "FAIL",
        "only": ["kccn-sct-vn", "dacn-sct-vn", "bpb-sct-vn"],
    },
    {
        "id": "ccn-y-can-khoi-cong-11-2026",
        # 01/10/2026: BC 37/2026/TB-BC ngày 29/9/2026 của Công ty CP Luyện kim hóa chất Tây Bắc — giao đất 10/2026, dự kiến
        # khởi công 11/2026 Bạn chốt 01/10/2026 lấy theo CĐT (thông tin mới hơn) → FAIL.
        "pattern": r"^(?!.*(?:11/2026|ref 42|lịch sử)).*Y Can[^\n]{0,120}khởi công[^\n]{0,30}10/2026",
        "why": "Chủ đầu tư CCN Y Can báo cáo 29/9/2026: làm thủ tục giao đất trong 10/2026, dự kiến khởi công 11/2026 — ghi kèm mốc này (kccn-sct-vn ref 42 mục B.2, C.11).",
        "since": "2026-09-29",
        "level": "FAIL",
        "only": ["kccn-sct-vn", "dacn-sct-vn", "bpb-sct-vn"],
    },
    {
        "id": "qd-44-2021-ubnd-du-lieu-tnmt-bai-bo",
        # Chốt 01/10/2026: QĐ 3556/QĐ-UBND ngày 30/9/2026 ban hành Quy chế dữ liệu TNMT tỉnh Lào Cai, bãi bỏ
        # QĐ 44/2021/QĐ-UBND (Lào Cai cũ) và QĐ 23/2011/QĐ-UBND (Yên Bái cũ). Dòng dẫn văn bản cũ phải nhắc 3556 hoặc "bãi bỏ".
        "pattern": r"^(?!.*(?:3556|bãi bỏ|BÃI BỎ|lịch sử|trước 30/9/2026)).*(?:QĐ|Quyết định)(?: số)? (?:44/2021|23/2011)/QĐ-UBND",
        "why": "QĐ 44/2021/QĐ-UBND (Lào Cai) và QĐ 23/2011/QĐ-UBND (Yên Bái) về quy chế dữ liệu tài nguyên và môi trường đã bị bãi bỏ từ 30/9/2026 — dẫn Quy chế ban hành kèm QĐ 3556/QĐ-UBND ngày 30/9/2026 (bvmt-sct-vn ref 12).",
        "since": "2026-09-30",
        "level": "FAIL",
    },
    {
        "id": "duong-4e-da-phe-duyet-du-an",
        # Chốt 28/9/2026: QĐ 3480/QĐ-UBND ngày 27/9/2026 phê duyệt dự án Đường kết nối từ Quốc lộ 4E đến CCN Thống Nhất 1
        # (CTĐT 1693/QĐ-UBND ngày 15/5/2026). Câu "chưa được phê duyệt chủ trương đầu tư" chỉ còn là lịch sử (báo cáo 6-7/2026).
        "pattern": r"^(?!.*(?:3480|1693|lịch sử|trước 15/5/2026|đến 14/5/2026|KHÔNG viết|không viết|Không còn|không còn)).*(?:đường|tuyến)[^\n]{0,40}4E[^\n]{0,120}chưa (?:được )?(?:phê duyệt|có) chủ trương",
        "why": "Tuyến đường từ Quốc lộ 4E đến CCN Thống Nhất 1 đã có chủ trương đầu tư (QĐ 1693/QĐ-UBND ngày 15/5/2026) và phê duyệt dự án (QĐ 3480/QĐ-UBND ngày 27/9/2026, 130 tỷ, 1,2 km, 2026–2028) — kccn-sct-vn ref 41 mục A, ref 22 mục B.",
        "since": "2026-09-27",
        "level": "FAIL",
        "only": ["kccn-sct-vn", "dacn-sct-vn", "bpb-sct-vn", "vbhc-vn", "quy-hoach-ct-vn"],
    },
    {
        "id": "ccn-mong-son-yen-hop-2-da-thanh-lap",
        # Chốt 24/9/2026: QĐ 3426 (Mông Sơn) và 3427/QĐ-UBND (Yên Hợp 2) cùng ngày 23/9/2026. Không còn "chờ/dự kiến ban hành QĐ thành lập".
        "pattern": r"^(?!.*(?:3426|3427|lịch sử|đã thành lập|ĐÃ THÀNH LẬP|trước 23/9/2026|KHÔNG viết|không viết)).*(?:CCN|[Cc]ụm công nghiệp) (?:Mông Sơn|Yên Hợp 2)[^\n]{0,160}(?:chờ|dự kiến|đang trình)[^\n]{0,40}(?:ban hành )?(?:Quyết định|QĐ) thành lập",
        "why": "CCN Mông Sơn (QĐ 3426/QĐ-UBND) và CCN Yên Hợp 2 (QĐ 3427/QĐ-UBND) đã được thành lập ngày 23/9/2026 — bậc 10 ref 39; viết theo trạng thái sau thành lập (kế hoạch, đường găng, QHCT, GPMB đợt 1) — kccn-sct-vn ref 41, ref 31 mục 9.",
        "since": "2026-09-23",
        "level": "FAIL",
        "only": ["kccn-sct-vn", "dacn-sct-vn", "bpb-sct-vn", "quy-hoach-ct-vn"],
    },
    {
        "id": "pccc-nghiem-thu-nd347",
        # Chốt 24/9/2026 (NĐ 347/2026/NĐ-CP ngày 08/9/2026, hiệu lực 15/9/2026 + CV 6501/CAT-PCCC ngày 23/9/2026):
        # bãi bỏ k5 Đ6, Đ10 NĐ 105/2025 và Mẫu PC15-PC17 → CĐT tự nghiệm thu PCCC; không đòi văn bản chấp thuận của Công an.
        "pattern": r"^(?!.*(?:347|66\.18|bãi bỏ|(?:không|còn) (?:yêu cầu|đòi|còn)|KHÔNG (?:đòi|yêu cầu)|hoặc văn bản chấp thuận|nghiệm thu PCCC/|trước 15/9/2026|lịch sử|đã (?:được )?cấp)).*(?:Mẫu (?:số )?PC1[567]\b|văn bản chấp thuận (?:kết quả )?(?:kiểm tra )?nghiệm thu (?:về )?(?:PCCC|phòng cháy))",
        "why": "Từ 15/9/2026 NĐ 347/2026/NĐ-CP bãi bỏ khoản 5 Điều 6, Điều 10 NĐ 105/2025 và Mẫu PC15, PC16, PC17: chủ đầu tư tự nghiệm thu PCCC (điểm đ k1 Đ12 mới), hồ sơ là biên bản nghiệm thu PCCC của chủ đầu tư; không yêu cầu văn bản chấp thuận kết quả nghiệm thu PCCC của Công an (CV 6501/CAT-PCCC ngày 23/9/2026) — pccc-sct-vn ref 16.",
        "since": "2026-09-15",
        "level": "FAIL",
        "only": ["pccc-sct-vn", "kho-vlncn-sct-vn", "xd-sct-vn", "xp-sct-vn", "sd-vlncn-sct-vn", "dacn-sct-vn", "kccn-sct-vn", "hc-sct-vn", "tkm-sct-vn", "attp-sct-vn"],
    },
    {
        "id": "kcn-3-khu-626-24-ha",
        # Chốt 22/9/2026 (BC 294/BC-BQLCKCN 18/9/2026): 03 KCN Phía Nam 400 + Minh Quân 107,89 + Âu Lâu 118,35 = 626,24 ha.
        # 627,89 chỉ còn trong bảng lịch sử tháng 7/2026 (ref 17, dòng dẫn BC 225).
        "pattern": r"^(?!.*(?:lịch sử|tháng 7|BC 225|225/BC|thay 627,89|thay bằng 626,24|trước ngày)).*627,89",
        "why": "Diện tích 03 KCN Phía Nam, Minh Quân, Âu Lâu dùng 626,24 ha theo BC 294/BC-BQLCKCN ngày 18/9/2026 (400 + 107,89 + 118,35) — kccn-sct-vn ref 40 mục B.",
        "since": "2026-09-22",
        "level": "FAIL",
    },
    {
        "id": "vlncn-cap-dieu-chinh-la-giay-phep",
        # Chốt 22/9/2026 (PTP Trang, bộ GTYB Đồng Tâm): cấp điều chỉnh GP sử dụng VLNCN → kết quả là GIẤY PHÉP /GP-SCT
        # có dòng "(Cấp điều chỉnh)", không còn dùng "Quyết định điều chỉnh (nội dung) Giấy phép" (anti-error 36, mẫu 04).
        "pattern": r"^(?!.*(?:lịch sử|cách cũ|cách làm cũ|anti-error 36|không dùng|KHÔNG dùng|chỉ còn|trước đây|Hỏm Dưới|thay bằng|thay toàn bộ|THAY toàn bộ)).*(?:QĐ|Quyết định) điều chỉnh (?:nội dung )?(?:Giấy phép|GP)\b",
        "why": "Từ 22/9/2026 cấp điều chỉnh Giấy phép sử dụng VLNCN ra kết quả là Giấy phép /GP-SCT có dòng \"(Cấp điều chỉnh)\" (anti-error 36 sd-vlncn-sct-vn, mẫu 04); không dùng hình thức Quyết định điều chỉnh nữa.",
        "since": "2026-09-22",
        "level": "FAIL",
        "only": ["sd-vlncn-sct-vn"],
    },
    {
        "id": "qcvn-40-nuoc-thai-cong-nghiep",
        # QCVN 40:2025/BTNMT (TT 06/2025/TT-BTNMT ngày 28/02/2025, hiệu lực 01/9/2025) thay QCVN 40:2011/BTNMT.
        # "QCVN 40:2021/BTNMT" là ký hiệu KHÔNG TỒN TẠI - lỗi có thật trong QĐ phê duyệt QHPK KCN Minh Quân 18/9/2026.
        "pattern": r"^(?!.*(?:40:2025|thay thế|đã hết hiệu lực|không tồn tại|ký hiệu sai|lịch sử|trước ngày|nguyên văn|bản gốc)).*QCVN\s*40:\s*20(?:11|21)/BTNMT",
        "why": "Quy chuẩn nước thải công nghiệp đang hiệu lực là QCVN 40:2025/BTNMT (Thông tư 06/2025/TT-BTNMT ngày 28/02/2025, hiệu lực 01/9/2025) thay QCVN 40:2011/BTNMT; ký hiệu QCVN 40:2021/BTNMT KHÔNG tồn tại (lỗi trong QĐ phê duyệt QHPK KCN Minh Quân ngày 18/9/2026) - xem kccn-sct-vn ref 34 mục H.1.",
        "since": "2026-09-21",
        "level": "FAIL",
    },
    {
        "id": "duong-ic18-tmdt-260-ty",
        # QĐ 3382/QĐ-UBND ngày 18/9/2026 phê duyệt dự án đường IC18 - CCN Thống Nhất 1: TMĐT 260.000 triệu đồng.
        # 210.000 chỉ còn đúng khi nói về CHỦ TRƯƠNG đầu tư (QĐ 1955) hoặc KẾ HOẠCH đầu tư công trung hạn (QĐ 2390).
        "pattern": r"^(?!.*(?:3382|260\.000|chủ trương|kế hoạch|trung hạn|2390|1955|lịch sử|trước ngày)).*IC18[^\n]{0,160}210\.000",
        "why": "Tổng mức đầu tư dự án Đường kết nối từ nút giao IC18 đến CCN Thống Nhất 1 là 260.000 triệu đồng theo QĐ 3382/QĐ-UBND ngày 18/9/2026; 210.000 chỉ dùng khi nói về chủ trương đầu tư (QĐ 1955/QĐ-UBND ngày 19/6/2025) hoặc phân bổ kế hoạch đầu tư công trung hạn (QĐ 2390) — kccn-sct-vn ref 23 mục D.3, ref 22 mục B.",
        "since": "2026-09-18",
        "level": "FAIL",
    },
    {
        "id": "ccn-chau-que-to-trinh-196",
        # Bản gốc lấy từ Data360X 12/9/2026: UBND xã Châu Quế trình Tờ trình 196/TTr-UBND ngày 11/9/2026,
        # chính nó ghi thay thế Tờ trình 68/TTr-UBND ngày 11/5/2026 (bản 75 ha). Số 187 là của xã Tân Hợp.
        "pattern": r"^(?!.*196/TTr-UBND)(?:.*Châu Quế[^\n]{0,120}Tờ trình số 187|.*Tờ trình số 187[^\n]{0,120}Châu Quế)",
        "why": "Hồ sơ thành lập CCN Châu Quế hiện hành là Tờ trình 196/TTr-UBND ngày 11/9/2026 của UBND xã Châu Quế (thay thế Tờ trình 68/TTr-UBND ngày 11/5/2026); Tờ trình số 187 ngày 04/9/2026 là của UBND xã Tân Hợp — xem kccn-sct-vn ref 37 mục B.",
        "since": "2026-09-11",
        "level": "FAIL",
    },
    {
        "id": "ccn-chau-que-31-ha",
        # Quy mô chốt tại Tờ trình 196: 31 ha tại thôn Khe Pháo (giảm từ 75 ha do vướng hầm, tuyến đường sắt)
        "pattern": r"^(?!.*(?:thay thế|quy mô cũ|giảm|68/TTr-UBND|31 ha)).*(?:CCN|[Cc]ụm công nghiệp) Châu Quế[^\n]{0,60}\b75\s*ha",
        "why": "CCN Châu Quế chốt 31 ha tại thôn Khe Pháo theo Tờ trình 196/TTr-UBND ngày 11/9/2026; 75 ha là quy mô cũ đã bị thay thế (kccn-sct-vn ref 37 mục B).",
        "since": "2026-09-11",
        "level": "FAIL",
    },
    {
        "id": "ctr-104-khong-phai-du-thao",
        # CTr 104-CTr/TU ngày 30/8/2026 của Tỉnh ủy đã ban hành (ký Hoàng Giang, có dấu); lớp text PDF để trống số/ngày nên dễ bị ghi nhầm "dự thảo" — GATE ảnh 11/9/2026
        "pattern": r"(dự thảo|chưa ban hành|chưa ký|chưa điền số|chưa có số)[^\n]{0,80}(104-CTr/TU|Chương trình hành động[^\n]{0,40}Tỉnh ủy[^\n]{0,60}(75-KL/TW|31-CTr/TW))|(104-CTr/TU)[^\n]{0,80}(dự thảo|chưa ban hành|chưa ký|chưa điền số|chưa có số)",
        "why": "Chương trình hành động số 104-CTr/TU ngày 30/8/2026 của Tỉnh ủy Lào Cai ĐÃ BAN HÀNH (Hoàng Giang ký, có dấu) — số/ngày chỉ có trên ảnh trang 1, lớp text trống; không kết luận dự thảo từ context (bvmt-sct-vn ref 11 mục 0).",
        "since": "2026-08-30",
        "level": "FAIL",
    },
    {
        "id": "kl-75-ngay-28-7-2026",
        # KL 75-KL/TW và CTr 31-CTr/TW đều ngày 28/7/2026; CTr 104-CTr/TU ngày 30/8/2026 — bắt ngày sai đi kèm số văn bản
        "pattern": r"(75-KL/TW|31-CTr/TW)[^\n]{0,12}ngày (?!28/7/2026)\d{1,2}/\d{1,2}/\d{4}|104-CTr/TU[^\n]{0,12}ngày (?!30/8/2026)\d{1,2}/\d{1,2}/\d{4}",
        "why": "Ngày đúng: KL 75-KL/TW và CTr 31-CTr/TW ngày 28/7/2026; CTr 104-CTr/TU ngày 30/8/2026 (bản có dấu tại bvmt-sct-vn/van-ban-goc/dang/).",
        "since": "2026-07-28",
        "level": "FAIL",
    },
    {
        "id": "kl-75-cua-bch-tw",
        # KL 75-KL/TW do Ban Chấp hành Trung ương (Hội nghị TW 3 khóa XIV) ban hành; CTr 31-CTr/TW mới là của Bộ Chính trị
        "pattern": r"(Kết luận|KL)[^\n]{0,8}75-KL/TW[^\n]{0,40}của Bộ Chính trị|31-CTr/TW[^\n]{0,40}của Ban Chấp hành Trung ương",
        "why": "KL 75-KL/TW là của Ban Chấp hành Trung ương Đảng khóa XIV (Tổng Bí thư Tô Lâm ký); Chương trình hành động 31-CTr/TW là của Bộ Chính trị (Trần Cẩm Tú ký) — bvmt-sct-vn ref 11 anti-error 1.",
        "since": "2026-07-28",
        "level": "FAIL",
    },
    {
        "id": "qua-thoi-han-mac-nhien",
        # Bạn chốt 10/9/2026: công văn xin ý kiến không dùng câu áp đặt "quá thời hạn không có ý kiến được hiểu là thống nhất"
        "pattern": r"quá thời hạn[^\n]{0,40}(không có ý kiến|không trả lời)[^\n]{0,40}(được hiểu|coi như|xem như) (là )?thống nhất",
        "why": "Quy tắc 23 vbhc-vn: giọng đề nghị, không ra lệnh — bỏ câu này, thay bằng hạn gửi kèm lý do mềm.",
        "since": "2026-09-10",
        "level": "WARN",
    },
    {
        "id": "ubnd-chi-dao-khong-cai-dieu-kien-cap-phep",
        # Văn bản chỉ đạo của UBND tỉnh không được đặt điều kiện tiên quyết vào thủ tục cấp phép của ngành khác (Lãnh đạo Sở bác 06/9/2026 — Nhóm K vbhc-vn)
        "pattern": r"chỉ cấp (Giấy phép|GP|Mệnh lệnh) vận chuyển[^\n]{0,120}(phối hợp|kiểm tra thực tế)",
        "why": "Điều kiện 'sau khi phối hợp Sở kiểm tra thực tế' bị Lãnh đạo bác 06/9/2026 (mơ hồ, không sản phẩm). Dạng chốt: 'chỉ thực hiện cấp phép khi được Sở Công Thương (cơ quan quản lý về phương án nổ mìn trên địa bàn tỉnh) xác nhận khu vực nổ mìn đảm bảo khoảng cách an toàn…' — vai trò giao trước ở mục 1đ (vbhc-vn Nhóm K1; sd-vlncn mẫu 23 B2).",
        "since": "2026-09-06",
        "level": "FAIL",
    },
    {
        "id": "qd-1131-thay-the-qd-21-2026",
        # QĐ 1131/QĐ-TTg (danh mục công nghệ chiến lược) bị thay thế bởi QĐ 21/2026/QĐ-TTg từ 01/7/2026 — dòng dẫn 1131 mà không nhắc 21/2026
        "pattern": r"^(?!.*(21/2026/QĐ-TTg|thay thế|lịch sử)).*1131/QĐ-TTg",
        "why": "QĐ 1131/QĐ-TTg đã bị thay thế bởi QĐ 21/2026/QĐ-TTg (hiệu lực 01/7/2026) — dẫn QĐ 21/2026 (dacn-sct-vn ref 11); chỉ nhắc 1131 kèm chữ 'thay thế'/'lịch sử'.",
        "since": "2026-07-01",
        "level": "FAIL",
    },
    {
        "id": "snnmt-cap-phep-sau-nq-66-25",
        # Từ 15/9/2026, cơ quan tham mưu cấp phép khoáng sản cấp tỉnh là Sở Công Thương (NQ 66.25/2026/NQ-CP); cảnh báo dòng còn viết SNNMT chủ trì tham mưu cấp phép mà không nhắc NQ 66.25/mốc 15/9/2026
        "pattern": r"^(?!.*(66\.25|15/9/2026|14/9/2026)).*(Sở Nông nghiệp và Môi trường|SNNMT|Sở NN&MT)[^\n]{0,40}(chủ trì|tham mưu)[^\n]{0,60}(cấp|gia hạn|thu hồi)[^\n]{0,30}(giấy phép|GP) (thăm dò|khai thác)",
        "why": "Từ 15/9/2026 Sở Công Thương tham mưu QLNN về địa chất, khoáng sản (NQ 66.25/2026/NQ-CP, hiệu lực đến 28/02/2027) — viết theo thời kỳ; câu về SNNMT phải kèm mốc 15/9/2026 hoặc chữ 'lịch sử'/'trước ngày'.",
        "since": "2026-09-15",
        "level": "WARN",
    },
    {
        "id": "mau-03-giay-de-nghi-su-dung",
        # Giấy đề nghị cấp GP SỬ DỤNG VLNCN là Mẫu số 04 PL III TT 23/2024; Mẫu số 03 là XNK. Vụ Thịnh Đạt 03/9/2026.
        "pattern": r"(Giấy đề nghị[^\n]{0,60}(sử dụng VLNCN|sử dụng vật liệu nổ)[^\n]{0,40}Mẫu số 03|Mẫu số 03[^\n]{0,40}Giấy đề nghị[^\n]{0,40}sử dụng (VLNCN|vật liệu nổ))",
        "why": "Giấy đề nghị cấp/cấp lại/cấp điều chỉnh GP sử dụng VLNCN là Mẫu số 04 Phụ lục III TT 23/2024 (Mẫu số 03 là xuất khẩu, nhập khẩu; Mẫu 04 không bị TT 26/2026 sửa) — chốt 03/9/2026.",
        "since": "2026-09-03",
        "level": "FAIL",
    },
    {
        "id": "gp-ubnd-sau-2867",
        # "dự thảo Giấy phép (GP-UBND)", "ký GP-UBND", "trình Chủ tịch UBND tỉnh ký GP" — sau 20/8/2026 GP sử dụng VLNCN là /GP-SCT
        "pattern": r"(dự thảo giấy phép \(GP-UBND\)|Chủ tịch UBND tỉnh ký GP-UBND|GP sử dụng vẫn do Chủ tịch|ký hiệu dự kiến `/GP-SCT`)",
        "why": "Từ 20/8/2026 GP sử dụng VLNCN do Sở cấp theo QĐ 2867/QĐ-UBND, ký hiệu /GP-SCT, KT. GĐ – PGĐ Hoàng Văn Thuân ký (thu hồi GP, phê duyệt PANM vẫn UBND tỉnh).",
        "since": "2026-08-20",
        "level": "FAIL",
    },
    {
        "id": "noi-nop-pvhcc",
        "pattern": r"(đầu mối (tiếp nhận|nộp hồ sơ)[^.\n]{0,40}Trung tâm Phục vụ hành chính công|nộp (trực tiếp )?tại Trung tâm Phục vụ hành chính công|qua Trung tâm Phục vụ hành chính công tỉnh\) để được xem xét)",
        "why": "Nơi nộp TTHC ghi Cổng dịch vụ công một cửa Bộ Công Thương https://motcua-tthc.moit.gov.vn/ (quy ước 02/8/2026); Trung tâm PVHCC chỉ nêu là kênh phụ.",
        "since": "2026-08-02",
        "level": "FAIL",
    },
    {
        "id": "noi-nop-kenh-phu",
        "pattern": r"(kênh phụ[^\n]{0,30}Trung tâm Phục vụ|hoặc qua Trung tâm Phục vụ|Trung tâm Phục vụ [Hh]ành chính công[^\n]{0,20}(kênh phụ|hoặc (trực tiếp|Hệ thống))|nộp (hồ sơ )?(tại|qua) Trung tâm Phục vụ|(qua|tại) Trung tâm Phục vụ hành chính công tỉnh\))",
        "why": "Nơi nộp TTHC DUY NHẤT là https://motcua-tthc.moit.gov.vn/ (Bạn chốt lại 02/9/2026, đăng nhập VNeID) — không ghi Trung tâm PVHCC kể cả dạng 'kênh phụ'/'hoặc qua'.",
        "since": "2026-09-02",
        "level": "FAIL",
    },
    {
        "id": "noi-nop-dvcqg",
        "pattern": r"(nộp (hồ sơ )?(trên|qua|tại) Cổng (Dịch vụ công [Qq]uốc gia|DVC( quốc gia)?\b)|Nơi nộp[^\n]{0,40}(Hệ thống (thông tin giải quyết|TTGQ)|bưu chính))",
        "why": "Không hướng dẫn DN nộp qua Cổng DVCQG; ghi https://motcua-tthc.moit.gov.vn/ (trích dẫn nguyên văn luật thì thêm chữ 'theo luật' hoặc để trong ngoặc kép).",
        "since": "2026-08-02",
        "level": "FAIL",
    },
    {
        "id": "cong-hoa",
        "pattern": r"CỘNG HOÀ",
        "why": "Quốc hiệu viết 'CỘNG HÒA' (không 'HOÀ').",
        "since": "2026-06-01",
        "level": "FAIL",
    },
    {
        "id": "tieu-ngu-gach-noi",
        "pattern": r"Độc lập - Tự do - Hạnh phúc",
        "why": "Tiêu ngữ dùng en dash: 'Độc lập – Tự do – Hạnh phúc'.",
        "since": "2026-06-01",
        "level": "WARN",
    },
    {
        "id": "luu-khong-ghi-ten-chuyen-vien",
        # Chốt 01/10/2026: dòng Lưu cuối văn bản không ghi tên chuyên viên soạn thảo — "Lưu: VT, CN."
        # (nội bộ Phòng "Lưu: CN."). Thay quy ước cũ "Lưu: VT, CN(tên)" và rule cn-m-cuong-vlncn.
        "pattern": r"(?:Lưu[^\n]{0,30}\b(?:Q?L?CN)\s?\((?!\s*\d)[^)\n]{1,25}\)|\bCN\s?\((?:tên|Tên)\))",
        "why": "Từ 01/10/2026 dòng Lưu không ghi tên chuyên viên: viết 'Lưu: VT, CN.' (công văn nội bộ Phòng 'Lưu: CN.'). Dòng trích văn bản đã ban hành trước ngày này thì thêm chữ 'lịch sử'.",
        "since": "2026-10-01",
        "level": "FAIL",
    },
    {
        "id": "yen-hop-giai-doan",
        "pattern": r"Yên Hợp[^|\n]{0,25}giai đoạn (I|II|1|2)\b",
        "why": "CCN Yên Hợp (12 ha) và CCN Yên Hợp 1 (63 ha) là 2 dự án độc lập; không dùng 'giai đoạn I/II' (nếu chép nguyên văn nguồn phải chú thích).",
        "since": "2026-07-01",
        "level": "WARN",
    },
    {
        "id": "so-tnmt-hien-hanh",
        "pattern": r"(chuyển|gửi|hỏi|lấy ý kiến|phối hợp với) Sở (Tài nguyên và Môi trường|TN&MT)\b",
        "why": "Sở TN&MT đã hợp nhất thành Sở Nông nghiệp và Môi trường (SNNMT) từ 01/3/2025; nếu trích nguyên văn nghị định cũ thì giữ nhưng chú thích '(nay là SNNMT)'.",
        "since": "2025-03-01",
        "level": "WARN",
    },
    {
        "id": "xp-hc-vlncn-cu",
        "pattern": r"→ plugin `xp-hc-vlncn-sct-vn`|dùng plugin xp-hc-vlncn-sct-vn",
        "why": "xp-hc-vlncn-sct-vn đã được xp-sct-vn kế thừa (02/9/2026); trỏ sang xp-sct-vn.",
        "since": "2026-09-02",
        "level": "WARN",
        "skip": ["xp-hc-vlncn-sct-vn"],
    },
    {
        "id": "ban-du-thao-pdf",
        "pattern": r"bản dự thảo chưa điền số|chưa điền số/ngày|PDF là bản dự thảo",
        "why": "Không kết luận PDF là 'bản dự thảo/chưa điền số' khi chưa chạy extract_metadata.py (vụ QĐ 5116/QĐ-SCT 02/9/2026).",
        "since": "2026-09-02",
        "level": "FAIL",
    },
    {
        "id": "mundus-ctdt-lan-3-da-ban-hanh",
        # Dự án Mundus Stones (KCN Âu Lâu): QĐ chấp thuận điều chỉnh CTĐT lần 3 ĐÃ ban hành
        # là QĐ 257/QĐ-BQLCKCN ngày 10/9/2026 — không còn dòng nào được ghi "chưa có/chưa ban hành".
        "pattern": r"(Quyết định|QĐ)[^\n]{0,80}điều chỉnh (CTĐT|chủ trương đầu tư)[^\n]{0,80}lần (thứ )?0?3[^\n]{0,80}(chưa có|chưa ban hành|chờ ban hành)",
        "why": "Điều chỉnh CTĐT lần 3 dự án Mundus Stones (KCN Âu Lâu) đã ban hành tại QĐ 257/QĐ-BQLCKCN ngày 10/9/2026 (kccn-sct-vn ref 33 mục H) — cập nhật số/ngày, chỉ còn GCN đăng ký đầu tư điều chỉnh lần 3 là chưa có.",
        "since": "2026-09-10",
        "level": "FAIL",
        "only": ["kccn-sct-vn"],
    },
    {
        "id": "mundus-tien-do-quy-3-2026",
        # Tiến độ hoàn thành dự án Mundus Stones nay là quý IV/2027 (QĐ 257); quý III/2026 là mốc CŨ theo QĐ 140
        "pattern": r"^(?!.*(QĐ 140|quyết định số 140|140/QĐ-BQLCKCN|IV/2027|257|cũ|lịch sử|đối chiếu)).*Mundus[^\n]{0,160}(quý|Quý) III/2026",
        "why": "Tiến độ hoàn thành dự án Mundus Stones sau điều chỉnh lần 3 là quý IV/2027 (QĐ 257/QĐ-BQLCKCN 10/9/2026); mốc quý III/2026 chỉ được nhắc kèm QĐ 140 hoặc chữ 'cũ'/'lịch sử' (kccn-sct-vn ref 33 mục B.5).",
        "since": "2026-09-10",
        "level": "FAIL",
        "only": ["kccn-sct-vn"],
    },
    {
        "id": "qd334-khong-phai-qd333",
        # QĐ 334/QĐ-TTg 01/4/2023 = CHIẾN LƯỢC địa chất, khoáng sản, công nghiệp khai khoáng.
        # QĐ 333/QĐ-TTg 23/4/2024 = Kế hoạch thực hiện Quy hoạch khoáng sản (QĐ 866). Hai văn bản hay bị gõ lẫn.
        "pattern": r"^(?!.*334).*(QĐ|Quyết định số) ?333[^\n]{0,60}Chiến lược|^(?!.*333).*(QĐ|Quyết định số) ?334[^\n]{0,60}Kế hoạch thực hiện Quy hoạch khoáng sản",
        "why": "QĐ 334/QĐ-TTg ngày 01/4/2023 = Chiến lược địa chất, khoáng sản và công nghiệp khai khoáng đến 2030, tầm nhìn 2045; QĐ 333/QĐ-TTg ngày 23/4/2024 = Kế hoạch thực hiện Quy hoạch khoáng sản (QĐ 866). Đừng gán nội dung chéo (quy-hoach-ct-vn ref 10 mục VI; qlks-sct-vn ref 24 mục V).",
        "since": "2026-09-13",
        "level": "FAIL",
    },
    {
        "id": "qd154-het-vai-tro",
        # QĐ 154/QĐ-TTg 29/01/2022 chỉ kéo dài kỳ QH KS làm VLXD, xi măng ĐẾN KHI QĐ 1626/QĐ-TTg 15/12/2023 ban hành.
        "pattern": r"^(?!.*(1626|lịch sử|hết vai trò|hết hiệu lực|hồ sơ cũ|trước 15/12/2023|giải trình|thanh tra|kéo dài|không dẫn|Trích yếu)).*(QĐ|Quyết định số) ?154/QĐ-TTg",
        "why": "QĐ 154/QĐ-TTg ngày 29/01/2022 (kéo dài kỳ quy hoạch KS làm VLXD, xi măng) đã hết vai trò khi QĐ 1626/QĐ-TTg ngày 15/12/2023 được phê duyệt. Việc hiện nay dẫn QĐ 1626; chỉ nhắc QĐ 154 kèm chữ 'lịch sử'/'hồ sơ cũ' hoặc kèm QĐ 1626 (quy-hoach-ct-vn ref 10 mục V; qlks-sct-vn ref 24 mục IV).",
        "since": "2026-09-13",
        "level": "FAIL",
    },
    {
        "id": "ta-phoi-cong-suat-thap-phan",
        # QĐ 2581 in "967.434"/"8.473"; phải đọc là 967,434 và 8,473 ×10³ tấn/năm (ref 07 mục A.1).
        "pattern": r"967\.434 ?(nghìn tấn|×?\s?10³ tấn|103 tấn)|8\.473 ?(nghìn tấn|×?\s?10³ tấn|103 tấn)",
        "why": "Công suất khai thác mỏ Tả Phời theo QĐ 2581/QĐ-TTg phải ghi 967,434 ×10³ tấn quặng/năm (≈ 967.434 tấn/năm) và 8,473 ×10³ tấn tinh quặng/năm — không ghi '967.434 nghìn tấn/năm' (sẽ thành 967 triệu tấn/năm). Xem quy-hoach-ct-vn ref 07 mục A.1.",
        "since": "2026-09-13",
        "level": "FAIL",
    },
    {
        "id": "qd2581-ba-tinh",
        "pattern": r"QĐ 2581[^\n]{0,40}(chỉ|duy nhất)[^\n]{0,30}(Tả Phời|Lào Cai)",
        "why": "QĐ 2581/QĐ-TTg 24/11/2025 điều chỉnh QĐ 866 tại 03 khu vực của 03 tỉnh: vonfram Núi Pháo (Thái Nguyên, Phụ lục I), mỏ đồng Tả Phời (Lào Cai, Phụ lục II), bôxit Thọ Sơn - Thống Nhất (Đồng Nai, Phụ lục III). Phần Lào Cai là Phụ lục II (quy-hoach-ct-vn ref 07 mục A).",
        "since": "2026-09-13",
        "level": "WARN",
    },
    {
        "id": "qd836-khong-phai-quy-hoach",
        # QĐ 836/QĐ-BXD 14/10/2019 là KẾ HOẠCH TỔ CHỨC LẬP quy hoạch KS làm VLXD, không phải quy hoạch.
        # Quy hoạch thật là QĐ 1626/QĐ-TTg 15/12/2023.
        "pattern": r"(theo|căn cứ|tại) [^\n]{0,40}836/QĐ-BXD[^\n]{0,60}(quy hoạch khoáng sản|danh mục mỏ|trữ lượng)|Quy hoạch[^\n]{0,50}(ban hành|phê duyệt)[^\n]{0,30}(QĐ|Quyết định số) ?836/QĐ-BXD",
        "why": "QĐ 836/QĐ-BXD ngày 14/10/2019 là KẾ HOẠCH tổ chức lập quy hoạch KS làm VLXD (nội bộ Bộ Xây dựng), không có danh mục mỏ/trữ lượng. Quy hoạch KS làm VLXD là QĐ 1626/QĐ-TTg ngày 15/12/2023; từ 15/9/2026 đầu mối là Bộ Công Thương. Xem quy-hoach-ct-vn ref 10 mục V.2 và ref 01 mục 5.",
        "since": "2026-09-14",
        "level": "FAIL",
    },
    {
        "id": "kim-thanh-tham-tra-2021-88-bctt",
        # Chốt 30/9/2026: thiết kế BVTC 2021 mỏ chì - kẽm Cao Phạ (Cty CP Kim Thành) do Cty TNHH tư vấn và đầu tư
        # Sơn Thái lập, thẩm tra tại Báo cáo 88/BCTT-AH ngày 06/5/2021, Sở Công Thương Yên Bái thông báo thẩm định
        # tại VB 897/SCT-KTATMT ngày 18/5/2021. Số "28/BCTT-AH" là đọc nhầm.
        "pattern": r"^(?!.*(88/BCTT|lịch sử|sai|nhầm)).*\b28/BCTT-AH",
        "why": "Thẩm tra thiết kế 2021 mỏ chì - kẽm Cao Phạ (Kim Thành) là Báo cáo 88/BCTT-AH ngày 06/5/2021, không phải 28/BCTT-AH; khi viện dẫn nên dẫn thẳng VB 897/SCT-KTATMT ngày 18/5/2021 của Sở Công Thương Yên Bái (sd-vlncn-sct-vn anti-error 37e).",
        "since": "2026-09-30",
        "level": "FAIL",
        "only": ["sd-vlncn-sct-vn"],
    },
]

EXCLUDE_PARTS = ("van-ban-goc", "vi-du-thuc-te", "examples", "templates")
EXCLUDE_NAME = ("nd30-phu-luc",)  # bản chép nguyên văn VBQPPL — không sửa theo quy ước nội bộ


def iter_files():
    for pj in sorted(REPO.glob("*/.claude-plugin/plugin.json")):
        plugin = pj.parent.parent.name
        skill_dir = REPO / plugin / "skills" / plugin
        if not skill_dir.exists():
            continue
        for f in sorted(skill_dir.rglob("*.md")):
            rel = f.relative_to(skill_dir).as_posix()
            if rel.startswith("CHANGELOG") or any(p in rel.split("/") for p in EXCLUDE_PARTS) \
                    or any(x in f.name for x in EXCLUDE_NAME):
                continue
            yield plugin, f, rel


def main():
    args = sys.argv[1:]
    if "--list" in args:
        for r in RULES:
            print(f"[{r['level']}] {r['id']} (từ {r['since']}): {r['why']}")
        return 0
    show_warn = "--warn" in args
    compiled = [(r, re.compile(r["pattern"], re.I)) for r in RULES]
    fails, warns = [], []
    for plugin, f, rel in iter_files():
        try:
            lines = f.read_text(encoding="utf-8").split("\n")
        except UnicodeDecodeError:
            lines = f.read_text(encoding="utf-8", errors="ignore").split("\n")
        for n, raw in enumerate(lines, 1):
            line = unicodedata.normalize("NFC", raw)
            if ALLOW_LINE.search(line):
                continue
            for r, rx in compiled:
                if r.get("only") and plugin not in r["only"]:
                    continue
                if plugin in r.get("skip", []):
                    continue
                m = rx.search(line)
                if m:
                    item = (r["id"], f"{plugin}/{rel}:{n}", m.group(0)[:60], r["why"])
                    (fails if r["level"] == "FAIL" else warns).append(item)
    for lv, items in (("FAIL", fails), ("WARN", warns if show_warn else [])):
        for rid, loc, hit, why in items:
            print(f"[{lv} {rid}] {loc}: «{hit}»\n    → {why}")
    print(f"\ncheck_facts: {len(fails)} FAIL, {len(warns)} WARN "
          f"({'hiện' if show_warn else 'ẩn — dùng --warn để xem'})")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
