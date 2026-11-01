"""Ghép trang PDF thành ảnh: strip.py <pdf> <ảnh ra> <trang đầu> <trang cuối> [dpi]"""
import sys, subprocess, glob, os, tempfile
from PIL import Image

pdf, out, a, b = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
dpi = sys.argv[5] if len(sys.argv) > 5 else '45'
tmp = tempfile.mkdtemp()
subprocess.run(['pdftoppm', '-r', dpi, '-png', '-f', str(a), '-l', str(b), pdf, os.path.join(tmp, 'p')], check=True)
ims = [Image.open(x) for x in sorted(glob.glob(os.path.join(tmp, 'p-*.png')))]
w = sum(i.width for i in ims)
c = Image.new('RGB', (w, max(i.height for i in ims)), 'white')
x = 0
for i in ims:
    c.paste(i, (x, 0)); x += i.width
c.save(out)
print(out)
