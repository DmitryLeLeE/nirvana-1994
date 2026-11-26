import glob, re, urllib.request, os

htmls = sorted(glob.glob('*.html'))
print(f'Total HTML files: {len(htmls)}')

img_urls = set()
broken_internal = []
post_1994_mentions = []

for fn in htmls:
    txt = open(fn, encoding='utf-8').read()
    for m in re.findall(r'href="([^"]+)"', txt):
        if m.startswith(('http', 'mailto:', '#', 'javascript:')):
            continue
        path_only = m.split('#', 1)[0].split('?', 1)[0]
        if path_only and not os.path.exists(path_only):
            broken_internal.append((fn, m))
    for m in re.findall(r'src="([^"]+)"', txt):
        if m.startswith('http'):
            img_urls.add(m)
        elif not os.path.exists(m):
            broken_internal.append((fn, 'IMG:' + m))
    clean = re.sub(r'<[^>]+>', ' ', txt)
    years = sorted(set(re.findall(r'\b(199[5-9]|20[0-2]\d)\b', clean)))
    if years:
        post_1994_mentions.append((fn, years))

print('Broken internal links/assets:', broken_internal)
print('Post-1994 years mentioned:', post_1994_mentions)
print(f'Unique external images ({len(img_urls)}):')
for u in sorted(img_urls):
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Nirvana1994Audit/1.0 (https://dmitrylelee.github.io/nirvana-1994/)'})
        with urllib.request.urlopen(req, timeout=8) as r:
            print(f'  [{r.status}] {u}')
    except Exception as e:
        print(f'  [ERR: {e}] {u}')
