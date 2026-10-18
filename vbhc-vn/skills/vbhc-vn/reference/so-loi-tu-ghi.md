# Sổ lỗi tự ghi — vbhc-vn

Lỗi Bạn chỉ ra trong phiên, Claude ghi ngay theo CLAUDE.md mục "Tự ghi lỗi" (Bạn chốt 17/10/2026). Đọc tệp này trước khi
soạn văn bản thuộc lĩnh vực của plugin. Định dạng mỗi mục và cách kiểm: `scripts/check_anti_error_format.py` ở gốc kho.
Lỗi kiểm được bằng máy thì kèm quy tắc trong `qa_rules.py` (vbhc-vn) hoặc `check_facts.py` và ghi mã ở dòng "Máy kiểm".
Yêu cầu riêng cho MỘT văn bản không ghi ở đây mà ghi vào `trang-thai/<hồ sơ>.md` mục "Yêu cầu riêng một lần".

### L001 — 17/10/2026 — Khoảng cách sau "Kính gửi" và ô ký tên
- Lỗi: thân văn bản bắt đầu ngay sát dưới khối "Kính gửi" (không có dòng trống); ô ký tên hẹp, thấp hơn hẳn khối Nơi nhận nên lãnh đạo không đủ chỗ ký.
- Cách đúng: sau dòng "Kính gửi" (cả khối nhiều nơi nhận) cách đúng 1 dòng trống rồi mới vào thân văn bản; ô ký tên rộng rãi, chiều cao tương ứng các dòng của khối Nơi nhận (≥ 3 dòng trống giữa chức danh và tên người ký — H13).
- Ví dụ: "Kính gửi: Ủy ban nhân dân tỉnh Lào Cai" → (1 dòng trống) → "Thực hiện …".
- Máy kiểm: `ra_soat_doc_lap.py` mục [3]; tự sửa dòng trống sau Kính gửi: `kiem_tra_truoc_khi_giao.py --tu-sua`; checklist_ra_soat.txt dòng 4, 5.

### L002 — 18/10/2026 — Doanh nghiệp chung dòng với cơ quan nhà nước ở Nơi nhận
- Lỗi: Nơi nhận ghép doanh nghiệp vào cùng dòng với cơ quan nhà nước ("Chi cục Hải quan khu vực VII; Công ty Điện lực Lào Cai") và xếp doanh nghiệp xen giữa các cơ quan. Bạn bác ngày 04/10/2026 khi rà Kế hoạch Bài toán lớn số 2 (PR 116); ghi sổ khi chuyển lên bản 2.34.0.
- Cách đúng: Nơi nhận xếp theo vị thế: cấp trên (b/c) → sở, ban, ngành → cơ quan ngành dọc → UBND xã, phường → doanh nghiệp đứng RIÊNG dòng, sau cùng → Văn phòng → Lưu.
- Ví dụ: "- UBND các xã, phường có cụm công nghiệp;" → "- Công ty Điện lực Lào Cai;" → "- CVP, PCVP UBND tỉnh;" → "- Lưu: VT, KT."
- Máy kiểm: R25 (FAIL khi chung dòng; WARN khi cơ quan nhà nước đứng sau doanh nghiệp); R06, R22.

### L003 — 18/10/2026 — "Ủy ban nhân dân" viết đủ chữ ở Nơi nhận và bảng phụ lục
- Lỗi: dòng Nơi nhận và ô bảng phụ lục của Kế hoạch viết "Ủy ban nhân dân tỉnh" thay vì "UBND tỉnh" (Bạn chốt 04/10/2026, PR 116). Thân văn bản vẫn viết đầy đủ theo checklist rà soát dòng 12 (17/10/2026); phần căn cứ chờ Bạn chốt phạm vi.
- Cách đúng: Nơi nhận "- UBND tỉnh (b/c);", "- UBND các xã, phường …;"; ô bảng phụ lục "UBND xã …"; đầu trang và khối ký "TM. ỦY BAN NHÂN DÂN" giữ đủ chữ.
- Ví dụ: "- Ủy ban nhân dân tỉnh (để b/c);" → "- UBND tỉnh (để b/c);".
- Máy kiểm: R24 (WARN).
