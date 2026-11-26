import glob, os, re
from collections import Counter

base = r'e:\WORK\my page'

CANONICAL_NAV = '''<p class="nav">
      <a href="index.html">Home</a> |
      <a href="about.html">The Band</a> |
      <a href="grunge.html">The Scene</a> |
      <a href="timeline.html">Timeline</a> |
      <a href="discography.html">Discography</a> |
      <a href="listening.html">Listening Room</a> |
      <a href="map.html">Map</a> |
      <a href="artifacts.html">Artifacts</a> |
      <a href="search.html">Search</a> |
      <a href="kurt.html">Kurt Cobain</a> |
      <a href="family.html">Family</a> |
      <a href="death.html">Death &amp; Legacy</a> |
      <a href="27club.html">27 Club</a> |
      <a href="songs.html">Songs</a> |
      <a href="quotes.html">Quotes</a> |
      <a href="lyrics.html">Lyrics</a> |
      <a href="faq.html">FAQ</a> |
      <a href="poll.html">Poll</a> |
      <a href="gear.html">Gear</a> |
      <a href="trivia.html">Trivia</a> |
      <a href="awards.html">Awards</a> |
      <a href="culture90s.html">The 90s</a> |
      <a href="bootlegs.html">Bootlegs</a> |
      <a href="influences.html">Influences</a> |
      <a href="tabs.html">Tabs</a> |
      <a href="concerts.html">Concerts</a> |
      <a href="venues.html">Venues</a> |
      <a href="videos.html">Videos</a> |
      <a href="wall.html">Kurt Wall</a> |
      <a href="quiz.html">Quiz</a> |
      <a href="pc1994.html">Virtual PC</a> |
      <a href="mixtape.html">Mixtape</a> |
      <a href="zines.html">Zines</a> |
      <a href="usenet.html">Usenet</a> |
      <a href="webmaster.html">Webmaster</a> |
      <a href="sitemap.html">Sitemap</a> |
      <a href="media.html">Media</a> |
      <a href="gallery.html">Gallery</a> |
      <a href="guestbook.html">Guestbook</a> |
      <a href="links.html">Sources</a>
    </p>'''

updated = 0
for fp in sorted(glob.glob(os.path.join(base, '*.html'))):
    fn = os.path.basename(fp)
    if fn in ('secret.html', 'webring-dead.html'):
        continue
    txt = open(fp, encoding='utf-8').read()
    new_txt, n = re.subn(r'<p class="nav">.*?</p>', CANONICAL_NAV, txt, count=1, flags=re.S)
    if n == 1 and new_txt != txt:
        open(fp, 'w', encoding='utf-8').write(new_txt)
        updated += 1

print('Unified nav updated on files:', updated)

# Static QA
broken = []
abs_paths = []
missing_alt = []
dup_ids_all = []
nav_counts = set()

htmls = sorted(glob.glob(os.path.join(base, '*.html')))
for fp in htmls:
    fn = os.path.basename(fp)
    txt = open(fp, encoding='utf-8').read()
    ids = re.findall(r'\bid="([^"]+)"', txt)
    dups = [k for k, v in Counter(ids).items() if v > 1]
    if dups:
        dup_ids_all.append((fn, dups))
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
    if fn not in ('secret.html', 'webring-dead.html'):
        nav_m = re.search(r'<p class="nav">(.*?)</p>', txt, re.S)
        nav_counts.add(len(re.findall(r'href="([^"]+)"', nav_m.group(1))) if nav_m else 0)

print(f'Total HTML files: {len(htmls)}')
print('Nav link counts across 40 main pages:', nav_counts)
print('Duplicate IDs:', dup_ids_all)
print('Broken internal paths:', broken)
print('Absolute leading-slash paths:', abs_paths)
print('Images missing alt:', missing_alt)
assert not broken and not abs_paths and not missing_alt and not dup_ids_all and nav_counts == {40}
