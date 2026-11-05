# tra-cuu-sct-vn — gắn máy chủ tra cứu MCP vào bộ plugin

Plugin này khai báo máy chủ MCP `sct-tra-cuu` (kiểu `http`, Streamable HTTP) qua `.mcp.json`, dùng hai biến môi trường:

- `SCT_MCP_URL` — địa chỉ máy chủ, dạng `https://<địa chỉ Vercel>/mcp`
- `SCT_MCP_TOKEN` — khóa truy cập (do người quản trị khai báo trên Vercel, biến `SCT_MCP_TOKEN`)

Không ghi giá trị thật vào kho. `.mcp.json` chỉ chứa `${SCT_MCP_URL}` và `${SCT_MCP_TOKEN}`.

## Khai báo trên máy

Windows (PowerShell hoặc cmd, chạy một lần; mở lại ứng dụng để nhận biến):

```bat
setx SCT_MCP_URL "https://<địa chỉ>/mcp"
```

```bat
setx SCT_MCP_TOKEN "<khóa>"
```

macOS, Linux (thêm vào `~/.zshrc` hoặc `~/.bashrc`):

```bash
export SCT_MCP_URL="https://<địa chỉ>/mcp"
export SCT_MCP_TOKEN="<khóa>"
```

Sau `setx`: **tắt hẳn** Antigravity hoặc Claude Code rồi mở lại (biến môi trường chỉ nạp khi khởi động).

## Cài và kiểm tra

1. Cài plugin từ marketplace của kho: `/plugin install tra-cuu-sct-vn@skill-sct` (hoặc bật trong danh sách plugin).
2. Gõ `/mcp` → phải thấy máy chủ `sct-tra-cuu` trạng thái kết nối, 16 công cụ.
3. Hỏi thử: "CCN Xuân Ái đang ở bậc thủ tục nào" → Claude gọi `trang_thai_cum` và trả bậc kèm nguồn.

Không thấy máy chủ trong `/mcp`: kiểm tra biến đã có (`echo %SCT_MCP_URL%` trên cmd), đã mở lại ứng dụng chưa, và
`curl -i <SCT_MCP_URL>` phải trả 401 (máy chủ sống, đòi khóa). Thử nhanh không qua plugin:

```bash
claude mcp add --transport http sct-tra-cuu https://<địa chỉ>/mcp --header "Authorization: Bearer <khóa>"
```

## Đổi khóa

Đổi `SCT_MCP_TOKEN` trên Vercel (Redeploy), rồi chạy lại `setx SCT_MCP_TOKEN "<khóa mới>"` và mở lại ứng dụng.

## Hạn chế

claude.ai (hộp thoại *Add custom connector*) hiện chưa có mục Request headers nên chưa gắn được; dự kiến đợt 2 thêm đăng nhập OAuth.
Trên claude.ai vẫn dùng script và tài liệu trong các plugin như cũ.
