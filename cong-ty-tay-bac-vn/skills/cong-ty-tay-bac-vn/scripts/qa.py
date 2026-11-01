"""Chuẩn hóa phông, chuyển PDF, ghép ảnh trang: qa.py <thư mục docx> <thư mục render> [mẫu tên]"""
import sys, os, glob, subprocess
from PIL import Image

src, out = sys.argv[1], sys.argv[2]
pat = sys.argv[3] if len(sys.argv) > 3 else ''
os.makedirs(out, exist_ok=True)
fix = subprocess.run('find / -path "*vbhc-vn*" -name chuan_hoa_xuat_ban.py 2>/dev/null | head -1', shell=True,
                     capture_output=True, text=True).stdout.strip()
for f in sorted(glob.glob(os.path.join(src, '*.docx'))):
    if pat and pat not in f:
        continue
    subprocess.run(['python3', fix, f, '--chi-phong'], capture_output=True, timeout=120)
    subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', out, f], capture_output=True, timeout=300)
    pdf = os.path.join(out, os.path.basename(f)[:-5] + '.pdf')
    n = int([l for l in subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout.splitlines()
             if l.startswith('Pages')][0].split()[1])
    print(n, 'trang:', os.path.basename(f))
