"""
Ensures every main page has the full archive navigation links and verifies:
1. Zero broken internal href/src paths.
2. Zero leading-slash absolute paths that break under /nirvana-1994/.
3. Zero missing alt attributes on <img> tags.
"""
import glob, os, re

base = r'e:\WORK\my page'
NEW_CORE = (
    '<a href="discography.html">Discography</a> |\n'
    '      <a href="listening.html">Listening Room</a> |\n'
    '      <a href="map.html">Map</a> |\n'
    '      <a href="artifacts.html">Artifacts</a> |\n'
    '      <a href="search.html">Search</a> |'
)
NEW_P3 = (
    '<a href="quiz.html">Quiz</a> |\n'
    '      <a href="pc1994.html">Virtual PC</a> |\n'
    '      <a href="mixtape.html">Mixtape</a> |\n'
    '      <a href="zines.html">Zines</a> |\n'
    '      <a href="usenet.html">Usenet</a> |'
)

updated = 0
for fp in sorted(glob.glob(os.path.join(base, '*.html'))):
    fn = os.path.basename(fp)
    if fn in ('secret.html', 'webring-dead.html'):
        continue
    txt = open(fp, encoding='utf-8').read()
    changed = False
    if 'listening.html' not in txt and '<a href="discography.html">Discography</a> |' in txt:
        txt = txt.replace('<a href="discography.html">Discography</a> |', NEW_CORE, 1)
        changed = True
    if 'pc1994.html' not in txt and '<a href="quiz.html">Quiz</a> |' in txt:
        txt = txt.replace('<a href="quiz.html">Quiz</a> |', NEW_P3, 1)
        changed = True
    if changed:
        open(fp, 'w', encoding='utf-8').write(txt)
        updated += 1

print('Updated nav on files:', updated)

# Verification pass
broken = []
abs_paths = []
missing_alt = []
htmls = sorted(glob.glob(os.path.join(base, '*.html')))
for fp in htmls:
    fn = os.path.basename(fp)
    txt = open(fp, encoding='utf-8').read()
    for m in re.findall(r'(?:href|src)="([^"]+)"', txt):
        if m.startswith(('http', 'mailto:', '#', 'javascript:')):
            continue
        if m.startswith('/'):
            abs_paths.append((fn, m))
        path_only = m.split('#', 1)[0].split('?', 1)[0]
        if path_only and not os.path.exists(os.path.join(base, path_only)):
            broken.append((fn, m))
    for img_tag in re.findall(r'<img\b[^>]*>', txt):
        if 'alt=' not in img_tag:
            missing_alt.append((fn, img_tag))

print(f'Total HTML files: {len(htmls)}')
print('Broken internal paths:', broken)
print('Absolute leading-slash paths:', abs_paths)
print('Images missing alt:', missing_alt)
assert not broken and not abs_paths and not missing_alt
