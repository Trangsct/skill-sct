#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ghi_nhat_ky.py — ghi nhật ký cuối phiên vào tệp trạng thái hồ sơ bằng MỘT lệnh (Bạn chốt 17/10/2026, mục 6).

Ghi nhật ký phiên (mặc định ngày hôm nay):
    python3 scripts/ghi_nhat_ky.py "Phú Thịnh 1" \
        --viec "Soạn công văn đôn đốc tiến độ GPMB" \
        --van-ban "2026.10.17. Công văn đôn đốc GPMB CCN Phú Thịnh 1.docx (bản 2)" \
        --quyet-dinh "Không nêu tờ trình khi đã có Quyết định" \
        --xong "Gửi công văn đôn đốc tiến độ" --tiep-theo "Chờ xã báo cáo trước 25/10/2026" \
        --viec-do "Bổ sung số liệu diện tích đã GPMB" --cau-hoi "Xã đã chi trả đợt 2 chưa?"

Tạo hồ sơ mới từ trang-thai/MAU.md:
    python3 scripts/ghi_nhat_ky.py --tao-moi "Thành lập Cụm công nghiệp X" --bi-danh "CCN X; cụm X" \
        --plugin kccn-sct-vn

Nạp nhật ký tạm (phiên trước kết thúc khi chưa kịp ghi — xem CLAUDE.md mục "Kết thúc phiên"):
    python3 scripts/ghi_nhat_ky.py --nap-tam nhat-ky-tam.json

Đối số đầu là slug tệp, tên hoặc bí danh hồ sơ (tra bằng tim_ho_so.py). Các tham số lặp được nhiều lần.
Script tự: chèn mục "### dd/mm/yyyy" vào Nhật ký phiên (cùng ngày thì gộp vào mục đã có); thêm --xong vào
"Bước đã xong" (đánh số tiếp, kèm ngày); thay "Bước tiếp theo" bằng --tiep-theo (nếu có); thêm --vuong-mac và
--cau-hoi vào "Vướng mắc, câu hỏi còn mở", --giai-quyet xóa dòng vướng mắc chứa cụm đó; thêm --quyet-dinh vào
"Quyết định của Bạn"; --mot-lan vào "Yêu cầu riêng một lần"; --phat-hanh "số|ngày|cơ quan|trích yếu|tệp" thêm
dòng bảng "Văn bản đã phát hành". Nhật ký quá 10 mục thì gộp các mục cũ (giữ 5 mục mới nhất) thành
"### Tóm tắt đến ngày …".

Từ chối ghi (mã 3) khi nội dung có số điện thoại, tài khoản, người đại diện, thông tin đăng ký doanh nghiệp,
sức khỏe, đời tư — kho skill-sct công khai (mục 6.2). --tam ghi vào nhat-ky-tam.json ở thư mục hiện hành thay
vì sửa kho (phiên không có quyền ghi kho).
"""
from __future__ import annotations

import argparse
import json
import re
import sys

sys.dont_write_bytecode = True  # nhập trang_thai_lib cạnh script: không sinh __pycache__ trong kho (CI chặn)
from pathlib import Path

from tim_ho_so import cham
from trang_thai_lib import (DE_NHAT_KY, MUC, THU_MUC, TRONG, HoSo, hom_nay, kiem_rieng_tu,
                            ngay_khoa, slug)

GIU_MOI = 5
TOI_DA = 10
TAM = "nhat-ky-tam.json"


def tao_moi(ten: str, bi_danh: str, plugins: list[str]) -> Path:
    p = THU_MUC / f"{slug(ten)}.md"
    if p.exists():
        raise SystemExit(f"Đã có {p} — ghi nhật ký vào tệp đó, không tạo trùng.")
    dong = [f"# {ten}", "", f"Bí danh: {bi_danh or ten}", f"Plugin liên quan: {', '.join(plugins)}", ""]
    for m in MUC:
        dong += [f"## {m}", ""]
        if m == "Văn bản đã phát hành":
            dong += ["| Số ký hiệu | Ngày | Cơ quan | Trích yếu ngắn | Tệp trong kho |", "|---|---|---|---|---|", ""]
        elif m == "Nhật ký phiên":
            dong += [f"### {hom_nay()}", "- Việc đã làm: tạo tệp trạng thái từ mẫu.", ""]
        else:
            dong += [f"- {TRONG}", ""]
    p.write_text("\n".join(dong).rstrip() + "\n", encoding="utf-8")
    return p


def gop_cu(hs: HoSo) -> bool:
    """Mục 6.3: nhật ký quá 10 mục thì gộp các mục cũ thành 'Tóm tắt đến ngày …'."""
    nk = hs.muc_nhat_ky()
    if len(nk) <= TOI_DA:
        return False
    cu, moi = nk[:-GIU_MOI], nk[-GIU_MOI:]
    tom: list[str] = []
    ngay_cuoi = ""
    for de, noi in cu:
        m = DE_NHAT_KY.match(de)
        ngay = m.group(1) if m else ""
        if de.startswith("### Tóm tắt"):
            tom += [ln for ln in noi if ln.strip()]
        else:
            viec = next((ln.split(":", 1)[1].strip() for ln in noi if ln.startswith("- Việc đã làm:")),
                        " ".join(ln.strip("- ") for ln in noi if ln.strip())[:200])
            tom.append(f"- {ngay}: {viec}")
        if ngay and ngay_khoa(ngay) > ngay_khoa(ngay_cuoi):
            ngay_cuoi = ngay
    dong = [f"### Tóm tắt đến ngày {ngay_cuoi}", *tom, ""]
    for de, noi in moi:
        dong += [de, *[ln for ln in noi if ln.strip()], ""]
    hs.dat("Nhật ký phiên", dong)
    return True


def ghi(hs: HoSo, a) -> None:
    ngay = a.ngay
    # 1. Nhật ký phiên
    nk = hs.muc_nhat_ky()
    moi = []
    for nhan, ds in (("Việc đã làm", a.viec), ("Văn bản đã xuất", a.van_ban),
                     ("Quyết định của Bạn", a.quyet_dinh), ("Việc còn dở", a.viec_do),
                     ("Câu hỏi chưa được trả lời", a.cau_hoi)):
        if ds:
            moi.append(f"- {nhan}: " + "; ".join(ds))
    if not moi:
        raise SystemExit("Không có nội dung nhật ký (--viec/--van-ban/--quyet-dinh/--viec-do/--cau-hoi).")
    dong: list[str] = []
    da_gop = False
    for de, noi in nk:
        noi = [ln for ln in noi if ln.strip()]
        if de.strip() == f"### {ngay}" and not da_gop:
            for dong_moi in moi:  # cùng nhãn thì nối vào dòng đã có, không lặp nhãn
                nhan = dong_moi.split(":", 1)[0] + ":"
                i = next((k for k, ln in enumerate(noi) if ln.startswith(nhan)), None)
                if i is None:
                    noi.append(dong_moi)
                else:
                    noi[i] = noi[i].rstrip(". ") + "; " + dong_moi.split(":", 1)[1].strip()
            da_gop = True
        dong += [de, *noi, ""]
    if not da_gop:
        dong += [f"### {ngay}", *moi, ""]
    hs.dat("Nhật ký phiên", dong)
    gop_cu(hs)
    # 2. Bước đã xong — đánh số tiếp
    if a.xong:
        cu = [ln for ln in hs.dong("Bước đã xong") if TRONG not in ln]
        n = max([int(m.group(1)) for m in (re.match(r"\s*(\d+)\.", ln) for ln in cu) if m] or [0])
        hs.dat("Bước đã xong", cu + [f"{n + i + 1}. ({ngay}) {x}" for i, x in enumerate(a.xong)])
    # 3. Bước tiếp theo — thay hẳn (bước cũ đã xong hoặc đã đổi)
    if a.tiep_theo:
        hs.dat("Bước tiếp theo", [f"- {x}" for x in a.tiep_theo])
    # 4. Vướng mắc
    if a.giai_quyet:
        con = [ln for ln in hs.dong("Vướng mắc, câu hỏi còn mở")
               if not any(g.lower() in ln.lower() for g in a.giai_quyet)]
        hs.dat("Vướng mắc, câu hỏi còn mở", con or [f"- {TRONG}"])
    if a.vuong_mac or a.cau_hoi:
        hs.them("Vướng mắc, câu hỏi còn mở", [f"- ({ngay}) {x}" for x in a.vuong_mac + a.cau_hoi])
    # 5. Quyết định, yêu cầu một lần
    if a.quyet_dinh:
        hs.them("Quyết định của Bạn", [f"- ({ngay}) {x}" for x in a.quyet_dinh])
    if a.mot_lan:
        hs.them("Yêu cầu riêng một lần", [f"- ({ngay}) {x}" for x in a.mot_lan])
    # 6. Văn bản đã phát hành
    for x in a.phat_hanh:
        cot = [c.strip() for c in x.split("|")]
        if len(cot) != 5:
            raise SystemExit(f"--phat-hanh cần 5 cột 'số|ngày|cơ quan|trích yếu|tệp': {x}")
        bang = hs.dong("Văn bản đã phát hành")
        if not any(ln.startswith("|---") for ln in bang):
            bang = ["| Số ký hiệu | Ngày | Cơ quan | Trích yếu ngắn | Tệp trong kho |", "|---|---|---|---|---|"]
        bang = [ln for ln in bang if TRONG not in ln]
        hs.dat("Văn bản đã phát hành", bang + ["| " + " | ".join(c or "—" for c in cot) + " |"])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ho_so", nargs="?", help="slug tệp, tên hoặc bí danh hồ sơ")
    ap.add_argument("--ngay", default=hom_nay(), help="dd/mm/yyyy, mặc định hôm nay")
    for k in ("viec", "van-ban", "quyet-dinh", "viec-do", "cau-hoi", "xong", "tiep-theo", "vuong-mac",
              "giai-quyet", "mot-lan", "phat-hanh"):
        ap.add_argument(f"--{k}", action="append", default=[])
    ap.add_argument("--tao-moi", metavar="TEN", help="tạo tệp mới từ mẫu với tên hồ sơ này")
    ap.add_argument("--bi-danh", default="")
    ap.add_argument("--plugin", action="append", default=[])
    ap.add_argument("--tam", action="store_true", help=f"ghi vào ./{TAM} thay vì sửa kho")
    ap.add_argument("--nap-tam", metavar="TEP", help="nạp các mục từ tệp nhật ký tạm vào kho")
    a = ap.parse_args()

    if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", a.ngay):
        raise SystemExit("--ngay phải dạng dd/mm/yyyy, ví dụ 17/10/2026")
    noi_dung = " ".join(sum((getattr(a, k) for k in ("viec", "van_ban", "quyet_dinh", "viec_do", "cau_hoi",
                                                      "xong", "tiep_theo", "vuong_mac", "mot_lan", "phat_hanh")),
                            [])) + " " + (a.tao_moi or "") + " " + a.bi_danh
    lo = kiem_rieng_tu(noi_dung)
    if lo:
        print("TỪ CHỐI GHI — kho skill-sct công khai, nội dung có: " + "; ".join(lo), file=sys.stderr)
        return 3

    if a.nap_tam:
        tep = Path(a.nap_tam)
        so = 0
        for muc in json.loads(tep.read_text(encoding="utf-8")):
            args = [muc["ho_so"], "--ngay", muc["ngay"]]
            if muc.get("tao_moi") and not (THU_MUC / f"{slug(muc['tao_moi'])}.md").exists():
                args = ["--tao-moi", muc["tao_moi"], "--bi-danh", muc.get("bi_danh", ""), "--ngay", muc["ngay"]]
            for k, v in muc.items():
                if k in ("tao_moi", "bi_danh"):
                    continue
                if k not in ("ho_so", "ngay"):
                    for x in v:
                        args += [f"--{k.replace('_', '-')}", x]
            sys.argv = [sys.argv[0], *args]
            if main() != 0:
                return 1
            so += 1
        print(f"Đã nạp {so} mục từ {tep}; xóa tệp tạm sau khi commit.")
        return 0

    if a.tam:
        if a.ho_so and not (THU_MUC / f"{a.ho_so}.md").exists():
            ds_hs = cham(a.ho_so)
            if ds_hs:
                a.ho_so = ds_hs[0][1].path.stem  # ghi slug, phiên sau nạp không phải tra lại bí danh
            elif not a.tao_moi:
                raise SystemExit(f"Chưa có hồ sơ '{a.ho_so}' — thêm --tao-moi \"<Tên>\" --plugin … để phiên sau tạo tệp.")
        tep = Path.cwd() / TAM
        ds = json.loads(tep.read_text(encoding="utf-8")) if tep.exists() else []
        muc = {"ho_so": a.ho_so or slug(a.tao_moi), "ngay": a.ngay}
        if a.tao_moi:
            muc.update(tao_moi=a.tao_moi, bi_danh=a.bi_danh, plugin=a.plugin)
        muc.update({k: getattr(a, k) for k in ("viec", "van_ban", "quyet_dinh", "viec_do", "cau_hoi", "xong",
                                               "tiep_theo", "vuong_mac", "giai_quyet", "mot_lan", "phat_hanh")
                    if getattr(a, k)})
        ds.append(muc)
        tep.write_text(json.dumps(ds, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Đã ghi nhật ký tạm vào {tep} — phiên sau chạy: python3 scripts/ghi_nhat_ky.py --nap-tam {tep}")
        return 0

    if a.tao_moi:
        if not a.plugin:
            raise SystemExit("--tao-moi cần ít nhất một --plugin")
        p = tao_moi(a.tao_moi, a.bi_danh, a.plugin)
        print(f"Đã tạo {p}")
        if not any(getattr(a, k) for k in ("viec", "van_ban", "quyet_dinh", "viec_do", "cau_hoi", "xong",
                                           "tiep_theo", "vuong_mac", "mot_lan", "phat_hanh")):
            return 0
        a.ho_so = p.stem

    if not a.ho_so:
        ap.error("thiếu tên hồ sơ")

    p = THU_MUC / f"{a.ho_so}.md"
    if not p.exists():
        ds = cham(a.ho_so)
        if not ds:
            raise SystemExit(f"Không tìm thấy hồ sơ '{a.ho_so}'. Tạo mới bằng --tao-moi.")
        p = ds[0][1].path
    hs = HoSo(p)
    ghi(hs, a)
    hs.luu()
    print(f"Đã ghi nhật ký {a.ngay} vào {p.relative_to(THU_MUC.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
