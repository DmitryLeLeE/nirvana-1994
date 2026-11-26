import glob, json, os, re
from collections import Counter

base = r'e:\WORK\my page'

COMPACT_NAV = '''<p class="nav">
      <a href="index.html">Home</a> |
      <a href="about.html">The Band</a> |
      <a href="discography.html">Discography</a> |
      <a href="songs.html">Songs</a> |
      <a href="listening.html">Listening Room</a> |
      <a href="concerts.html">Concerts</a> |
      <a href="timeline.html">Timeline</a> |
      <a href="gallery.html">Gallery</a> |
      <a href="media.html">Media</a> |
      <a href="sitemap.html">Archive</a> |
      <a href="search.html">Search</a> |
      <a href="links.html">Sources</a>
    </p>'''

updated = 0
for fp in sorted(glob.glob(os.path.join(base, '*.html'))):
    fn = os.path.basename(fp)
    if fn in ('secret.html', 'webring-dead.html'):
        continue
    txt = open(fp, encoding='utf-8').read()
    new_txt, n = re.subn(r'<p class="nav">.*?</p>', COMPACT_NAV, txt, count=1, flags=re.S)
    if n == 1 and new_txt != txt:
        open(fp, 'w', encoding='utf-8').write(new_txt)
        updated += 1

# Static QA checks
htmls = sorted(glob.glob(os.path.join(base, '*.html')))
main_pages = [os.path.basename(f) for f in htmls if os.path.basename(f) not in ('secret.html', 'webring-dead.html')]
nav_counts = set()
dup_ids = []
broken_links = []
broken_imgs = []
missing_alt = []
abs_paths = []
linked_pages = set(['index.html', 'sitemap.html'])

for fp in htmls:
    fn = os.path.basename(fp)
    txt = open(fp, encoding='utf-8').read()
    ids = re.findall(r'\bid="([^"]+)"', txt)
    dups = [k for k, v in Counter(ids).items() if v > 1]
    if dups:
        dup_ids.append((fn, dups))
    for m in re.findall(r'href="([^"]+)"', txt):
        if m.startswith(('http', 'mailto:', '#', 'javascript:')):
            continue
        if m.startswith('/'):
            abs_paths.append((fn, m))
        path_only = m.split('#', 1)[0].split('?', 1)[0]
        if path_only:
            linked_pages.add(path_only)
            if not os.path.exists(os.path.join(base, path_only)):
                broken_links.append((fn, m))
    for m in re.findall(r'src="([^"]+)"', txt):
        if m.startswith('http'):
            continue
        if m.startswith('/'):
            abs_paths.append((fn, m))
        path_only = m.split('#', 1)[0].split('?', 1)[0]
        if path_only and not os.path.exists(os.path.join(base, path_only)):
            broken_imgs.append((fn, m))
    for img_tag in re.findall(r'<img\b[^>]*>', txt):
        if 'alt=' not in img_tag:
            missing_alt.append((fn, img_tag))
    if fn in main_pages:
        nav_m = re.search(r'<p class="nav">(.*?)</p>', txt, re.S)
        nav_counts.add(len(re.findall(r'href="([^"]+)"', nav_m.group(1))) if nav_m else 0)

# Sitemap route count
sm_txt = open(os.path.join(base, 'sitemap.html'), encoding='utf-8').read()
sm_tables = sm_txt.split('<h3>Neighbors in the webring</h3>')[0]
sm_routes = sorted(set(re.findall(r'href="([^"]+\.html)"', sm_tables)))

# Timeline integrity
tl_txt = open(os.path.join(base, 'timeline.html'), encoding='utf-8').read()
tl_ids = re.findall(r'id:\s*"([^"]+)"', tl_txt)
tl_statuses = re.findall(r'status:\s*"([^"]+)"', tl_txt)
tl_counts = dict(Counter(tl_statuses))

unlinked = sorted(set(os.path.basename(f) for f in htmls) - linked_pages - {'webring-dead.html'})

report = {
    "nav_updated_files": updated,
    "total_html_files": len(htmls),
    "main_pages_count": len(main_pages),
    "nav_link_counts": list(nav_counts),
    "sitemap_archive_routes_count": len(sm_routes),
    "duplicate_ids": dup_ids,
    "broken_internal_links": broken_links,
    "broken_local_images": broken_imgs,
    "missing_alt": missing_alt,
    "absolute_leading_slash_paths": abs_paths,
    "unused_routes": unlinked,
    "timeline": {
        "total_events": len(tl_ids),
        "unique_ids": len(set(tl_ids)),
        "status_counts": tl_counts,
        "sum_matches": sum(tl_counts.values()) == len(tl_ids)
    }
}
print(json.dumps(report, indent=2))
assert not dup_ids and not broken_links and not broken_imgs and not missing_alt and not abs_paths
assert nav_counts == {12} and report["timeline"]["sum_matches"]
