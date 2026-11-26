import glob, re

for fn in sorted(glob.glob('*.html')):
    txt = open(fn, encoding='utf-8').read()
    lu = re.search(r'class="last-updated"[^>]*>(.*?)<', txt)
    ext_imgs = len(re.findall(r'<img[^>]+src="http', txt))
    h3s = re.findall(r'<h3[^>]*>(.*?)</h3>', txt)
    clean = re.sub(r'<[^>]+>', ' ', txt)
    words = len(clean.split())
    vp = 'viewport' in txt
    lu_s = lu.group(1) if lu else '-'
    print(f'{fn:18s} | words:{words:4d} | ext_img:{ext_imgs:2d} | vp:{vp} | {lu_s:24s} | h3:{len(h3s)}')
