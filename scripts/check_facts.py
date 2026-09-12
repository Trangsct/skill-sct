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
        "id": "cn-m-cuong-vlncn",
        "pattern": r"CN\(M\.?\s?Cường\)",
        "why": "Từ 10/7/2026 chuyên viên VLNCN/PANM là CN(Khôi); Đỗ Mạnh Cường là PTP, không đứng dòng Lưu (văn bản cũ giữ nguyên lịch sử — thêm chữ 'lịch sử'/'trước 10/7/2026' vào dòng nếu là trích dẫn cũ).",
        "since": "2026-07-10",
        "level": "WARN",
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
