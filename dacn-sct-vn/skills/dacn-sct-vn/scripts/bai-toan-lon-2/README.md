# Bộ script dựng hồ sơ Bài toán lớn số 2 (bản 10/9/2026)

Chạy trong sandbox Claude (Ubuntu, python-docx, LibreOffice). Copy cả thư mục về `/home/claude/work/`, rồi:

```
cd /home/claude/work
MODE=body python3 build_kh_bt2.py      # → output/kh_bt2.docx (thân Kế hoạch, 23 trang)
MODE=pl   python3 build_kh_bt2.py      # → output/kh_bt2_phuluc.docx (Phụ lục I-III, khổ ngang)
python3 build_ttr_bt2.py               # → output/ttr_bt2.docx (Tờ trình Sở, template 02 vbhc-vn)
python3 build_cv_bt2.py                # → output/cv_xin_y_kien_bt2.docx (CV gửi sở ngành + trang 2 danh sách viện/trường/DN)
python3 build_cv_noi_bo_bt2.py         # → output/cv_noi_bo_bt2.docx (CV nội bộ Lãnh đạo Sở + phòng, mẫu Văn phòng)
python3 "/mnt/skills/plugins/bpb-sct-vn:bpb-sct-vn/scripts/build_bpb.py" bpb_bt2.txt output/bpb_bt2.docx
python3 "/mnt/skills/plugins/vbhc-vn:vbhc-vn/scripts/qa_all.py" output/<file>.docx --require ... --forbid ...
```

- Nội dung Kế hoạch nằm ở `noi_dung_bt2.py` (CAN_CU, THAN, NOI_NHAN) và `phu_luc_bt2.py` (PL1/PL2/PL3); sửa chữ ở đó rồi build lại, không sửa tay docx.
- Kinh phí: 365.000 triệu (65.000 sự nghiệp + 300.000 đầu tư công nguồn đóng góp khai thác khoáng sản QĐ 2390/QĐ-UBND); tổng Phụ lục I phải khớp mục VIII.
- Quy tắc thể thức đã chốt: vbhc-vn Quy tắc 14, 22, 23 (khối ký; giọng đề nghị; cấm câu "quá thời hạn không có ý kiến…").
- Các script dùng đường dẫn `/mnt/skills/plugins/vbhc-vn:vbhc-vn/...` và `/home/claude/work/output/`; nếu chạy ở nơi khác thì sửa hằng số đường dẫn đầu file.
