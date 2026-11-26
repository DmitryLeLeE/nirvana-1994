import urllib.request, hashlib

base_url = 'https://dmitrylelee.github.io/nirvana-1994/'
files = [
    'index.html', 'links.html', 'timeline.html', 'bootlegs.html', 'sitemap.html', 'search.html',
    'listening.html', 'style.css', 'data/listening_data.js',
    'concerts.html', 'data/concerts_data.js',
    'gallery.html', 'data/photos_data.js', 'data/artifacts_data.js',
    'grunge.html', 'influences.html', 'data/scene_influences_data.js',
    'discography.html', 'data/releases_data.js', 'data/sessions_data.js'
]
markers = {
    'index.html': 'NEW ARCHIVE TOOLS',
    'links.html': '1. SOURCES AVAILABLE IN 1994',
    'timeline.html': 'Archive Stats (auto-calculated):',
    'bootlegs.html': 'The Boombox Rehearsal (c. Summer 1987)',
    'sitemap.html': 'Archive &amp; Site Map',
    'search.html': 'href="sitemap.html">Archive</a>',
    'listening.html': 'completeness_status',
    'concerts.html': 'setlist_status',
    'gallery.html': 'data/photos_data.js',
    'grunge.html': 'renderSources',
    'influences.html': 'renderSources',
    'discography.html': 'category_type'
}
for f in files:
    local = open(f, encoding='utf-8').read().replace('\r\n', '\n')
    req = urllib.request.Request(base_url + f + '?cb=stage37', headers={'User-Agent': 'Nirvana1994DeployCheck/1.0', 'Cache-Control': 'no-cache'})
    remote = urllib.request.urlopen(req, timeout=10).read().decode('utf-8').replace('\r\n', '\n')
    h_loc = hashlib.sha256(local.encode('utf-8')).hexdigest()[:12]
    h_rem = hashlib.sha256(remote.encode('utf-8')).hexdigest()[:12]
    m_ok = (markers[f] in remote) if f in markers else True
    print(f'{f:24s} | match={local == remote} | sha_loc={h_loc} sha_rem={h_rem} | marker={m_ok}')
