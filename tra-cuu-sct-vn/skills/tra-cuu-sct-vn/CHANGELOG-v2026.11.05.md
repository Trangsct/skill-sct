# CHANGELOG — tra-cuu-sct-vn v1.0.0 (05/11/2026)

- Plugin mới: `.mcp.json` khai báo máy chủ `sct-tra-cuu` kiểu http (url `${SCT_MCP_URL}`, header `Authorization: Bearer ${SCT_MCP_TOKEN}`).
- `SKILL.md`: nguyên tắc gọi máy chủ trước, dự phòng script khi mất kết nối, không coi kết quả rỗng là "không có văn bản"; quy trình bắt buộc khi soạn văn bản (goi_boi_canh_soan_thao → nguoi_ky_va_luong_trinh → viết → kiem_tra_du_kien → vbhc-vn), khi thẩm định (checklist_tham_dinh → doi_chieu_ho_so), khi báo cáo (so_lieu_bao_cao), khi hỏi việc (viec_cho_xu_ly).
- `README.md`: khai báo biến trên máy (Windows `setx`), kiểm tra bằng `/mcp`, đổi khóa.
