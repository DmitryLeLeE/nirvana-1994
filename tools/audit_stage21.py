import glob, re
from collections import Counter

htmls = sorted(glob.glob('*.html'))
print(f'Total HTML files: {len(htmls)}')
for fn in htmls:
    txt = open(fn, encoding='utf-8').read()
    ids = re.findall(r'\bid="([^"]+)"', txt)
    dups = [k for k, v in Counter(ids).items() if v > 1]
    nav_m = re.search(r'<p class="nav">(.*?)</p>', txt, re.S)
    nav_links = re.findall(r'href="([^"]+)"', nav_m.group(1)) if nav_m else []
    if dups or len(nav_links) != 38:
        print(f'{fn:18s} | nav_links:{len(nav_links):2d} | dup_ids:{dups}')
    if 'boombox' in txt.lower() or 'butterworth' in txt.lower():
        for i, l in enumerate(txt.splitlines(), 1):
            if 'boombox' in l.lower() or 'butterworth' in l.lower():
                print(f'  [BOOMBOX] {fn}:{i}: {l.strip()[:100]}')
