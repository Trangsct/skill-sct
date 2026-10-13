#!/usr/bin/env python3
"""Xuất bộ plugin sang gói tri thức cho Gemini (Gem) và NotebookLM — tài khoản dự phòng.

Gemini không cài được plugin Claude, nên mỗi plugin được gộp thành MỘT tệp Markdown
(SKILL.md + references + checklists + mau-van-ban + vi-du-thuc-te; bỏ CHANGELOG, scripts,
tests, văn bản gốc). Plugin xếp thành 6 nhóm, mỗi nhóm là một Gem; mỗi nhóm có tệp
HUONG-DAN-GEM.txt để dán vào ô "Hướng dẫn" của Gem. Bản .txt toàn văn trong van-ban-goc/
chép riêng sang notebooklm/<nhóm>/ để nạp làm nguồn NotebookLM.

Chạy tại gốc kho:  python3 scripts/xuat_gemini.py [thư-mục-ra]   (mặc định ../gemini-export)
Kết quả: <thư-mục-ra>/ và <thư-mục-ra>.zip. Không ghi gì vào kho.
"""
import pathlib
import shutil
import sys
import unicodedata
from datetime import date

GOC = pathlib.Path(__file__).resolve().parent.parent

NHOM = {
    "1-VLNCN": ("Vật liệu nổ công nghiệp",
                ["sd-vlncn-sct-vn", "kho-vlncn-sct-vn", "hl-vlncn-sct-vn", "xp-hc-vlncn-sct-vn"]),
    "2-HOA-CHAT-HHNH-PCCC": ("Hóa chất, hàng hóa nguy hiểm, PCCC, an toàn lao động",
                             ["hc-sct-vn", "hnh-sct-vn", "pccc-sct-vn", "atvsld-sct-vn"]),
    "3-KCN-CCN-QUY-HOACH": ("Khu, cụm công nghiệp, quy hoạch, đất đai, dự án công nghiệp",
                            ["kccn-sct-vn", "quy-hoach-ct-vn", "dat-dai-sct-vn", "dacn-sct-vn"]),
    "4-KHOANG-SAN-MOI-TRUONG-XAY-DUNG": ("Khoáng sản, thiết kế mỏ, môi trường, xây dựng",
                                          ["qlks-sct-vn", "tkm-sct-vn", "bvmt-sct-vn", "xd-sct-vn"]),
    "5-VAN-BAN-TO-CHUC-XU-PHAT": ("Soạn văn bản hành chính, tổ chức Sở, xử phạt, bài phát biểu, ATTP",
                                  ["vbhc-vn", "vbhc-pdf-reader-vn", "sct-laocai-org-vn", "xp-sct-vn",
                                   "bpb-sct-vn", "attp-sct-vn"]),
    "6-CA-NHAN": ("Sức khỏe cá nhân", ["skcn-vn"]),
}
# data360x-sct-vn chỉ điều khiển bot trên GitHub — Gemini không dùng được, không xuất.

THU_MUC_LAY = ["references", "checklists", "mau-van-ban", "vi-du-thuc-te"]

LUU_Y = """> **Lưu ý khi dùng trên Gemini:** đây là bản xuất từ plugin Claude `{p}` (phiên bản {v}).
> Các bước "chạy script" (`tim_van_ban.py`, `extract_metadata.py`, `qa_*.py`…) KHÔNG chạy được trên
> Gemini — bỏ qua, tra trực tiếp trong nội dung tệp này. Văn bản gốc toàn văn nằm ở NotebookLM
> (nếu đã nạp) hoặc trên GitHub `Trangsct/skill-sct`, thư mục `{p}/skills/{p}/van-ban-goc/`.
"""

HUONG_DAN = """Bạn là trợ lý chuyên môn của chuyên viên Phòng Quản lý Công nghiệp, Sở Công Thương tỉnh Lào Cai, nhóm lĩnh vực: {ten}.

Tri thức nghiệp vụ nằm trong các tệp đính kèm của Gem này ({ds}). Mỗi tệp là một bộ quy tắc hoàn chỉnh: phần đầu (SKILL) là quy trình và quy tắc bắt buộc, các phần sau là tài liệu tham chiếu, mẫu văn bản, ví dụ thực tế.

Quy tắc làm việc:
1. Trước khi trả lời, xác định câu hỏi thuộc tệp nào và đọc phần SKILL của tệp đó; làm đúng quy trình, cổng kiểm tra (GATE) và quy ước ghi trong đó.
2. Không bịa số hiệu, ngày ban hành, tên người, số liệu. Chỉ dẫn những gì có trong tệp; không có thì nói rõ là tệp không ghi.
3. Bỏ qua mọi bước yêu cầu chạy script (Gemini không chạy được); thay bằng tra trong nội dung tệp.
4. Văn bản hành chính soạn theo thể thức Nghị định 30/2020/NĐ-CP và các quy ước riêng của Sở trong tệp.
5. Trả lời bằng tiếng Việt, xưng "tôi", gọi người dùng là "Bạn".
6. Đây là tài khoản DỰ PHÒNG: tri thức chốt đến ngày {ngay}; quy định mới hơn có thể chưa có — nhắc Bạn đối chiếu khi gặp văn bản sau ngày này.
"""


def doc(f):
    return unicodedata.normalize("NFC", f.read_text(encoding="utf-8", errors="replace"))


def phien_ban(p):
    import json
    try:
        return json.loads((GOC / p / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))["version"]
    except Exception:
        return "?"


def gop_plugin(p):
    sk = GOC / p / "skills" / p
    phan = [f"# Plugin {p}\n", LUU_Y.format(p=p, v=phien_ban(p)), "\n---\n\n## SKILL.md\n\n", doc(sk / "SKILL.md")]
    for tm in THU_MUC_LAY:
        d = sk / tm
        if not d.is_dir():
            continue
        for f in sorted(d.rglob("*.md")):
            rel = f.relative_to(sk).as_posix()
            phan += [f"\n\n---\n\n## {rel}\n\n", doc(f)]
    return "".join(phan)


def main():
    ra = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else GOC.parent / "gemini-export"
    if ra.exists():
        shutil.rmtree(ra)
    ngay = date.today().strftime("%d/%m/%Y")
    tong = []
    for ma, (ten, ds) in NHOM.items():
        gem = ra / "gem" / ma
        gem.mkdir(parents=True)
        for p in ds:
            (gem / f"{p}.md").write_text(gop_plugin(p), encoding="utf-8")
        (gem / "HUONG-DAN-GEM.txt").write_text(
            HUONG_DAN.format(ten=ten, ds=", ".join(f"{p}.md" for p in ds), ngay=ngay), encoding="utf-8")
        so_txt = 0
        for p in ds:
            vbg = GOC / p / "skills" / p / "van-ban-goc"
            for f in sorted(vbg.rglob("*.txt")) if vbg.is_dir() else []:
                dich = ra / "notebooklm" / ma / p / f.relative_to(vbg)
                dich.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(f, dich)
                so_txt += 1
        kb = sum(f.stat().st_size for f in gem.glob("*.md")) // 1024
        tong.append(f"| {ma} | {ten} | {len(ds)} | {kb} KB | {so_txt} |")
    (ra / "DOC-TRUOC.md").write_text(
        f"# Gói tri thức cho Gemini — xuất ngày {ngay}\n\n"
        "| Gem | Lĩnh vực | Số plugin | Tri thức | Văn bản gốc (.txt, cho NotebookLM) |\n|---|---|---|---|---|\n"
        + "\n".join(tong) + "\n\nCách nạp: xem hướng dẫn Claude gửi kèm.\n", encoding="utf-8")
    shutil.make_archive(str(ra), "zip", ra)
    print("\n".join(tong))
    print(f"Đã xuất: {ra}  và  {ra}.zip")


if __name__ == "__main__":
    main()
