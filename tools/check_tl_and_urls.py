import re, urllib.request
from collections import Counter

txt = open(r'e:\WORK\my page\timeline.html', encoding='utf-8').read()
statuses = re.findall(r'status:\s*"([^"]+)"', txt)
ids = re.findall(r'id:\s*"([^"]+)"', txt)
print('TL_EVENTS count:', len(statuses), 'Unique IDs:', len(set(ids)), dict(Counter(statuses)))

candidates = [
    "https://www.livenirvana.com/concerts/87/87-04-18.php",
    "https://www.livenirvana.com/concerts/91/91-04-17.php",
    "https://www.livenirvana.com/concerts/92/92-08-30.php",
    "https://www.livenirvana.com/concerts/93/93-11-18.php",
    "https://www.livenirvana.com/concerts/94/94-03-01.php",
    "https://www.livenirvana.com/sessions/radio/october-1989.php",
    "https://www.livenirvana.com/sessions/studio/may-1991.php",
    "https://www.livenirvana.com/sessions/studio/feb-1993.php",
    "https://www.livenirvana.com/sessions/studio/january-1994.php",
    "https://www.livenirvana.com/sessions/home/summer-1987.php",
    "https://www.discogs.com/master/13814-Nirvana-Nevermind",
    "https://www.discogs.com/master/22439-Nirvana-Bleach",
    "https://www.discogs.com/master/13859-Nirvana-In-Utero",
    "https://www.discogs.com/master/42473-Nirvana-MTV-Unplugged-In-New-York"
]
for u in candidates:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=6) as r:
            print(f'[{r.status}] {u}')
    except Exception as e:
        print(f'[ERR] {u} -> {e}')
