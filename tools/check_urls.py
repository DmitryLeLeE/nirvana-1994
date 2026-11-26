import re
import sys
import urllib.request

files = sys.argv[1:] or ["data/scene_influences_data.js"]
urls = set()
for fn in files:
    txt = open(fn, encoding="utf-8").read()
    for u in re.findall(r"https://[^\s\"']+", txt):
        urls.add(u)

ok = 0
bad = []
for u in sorted(urls):
    try:
        req = urllib.request.Request(u, method="HEAD", headers={"User-Agent": "Nirvana1994QA/1.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            if r.status == 200:
                ok += 1
            else:
                bad.append((u, r.status))
    except Exception as e:
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "Nirvana1994QA/1.0"})
            with urllib.request.urlopen(req, timeout=10) as r:
                if r.status == 200:
                    ok += 1
                else:
                    bad.append((u, r.status))
        except Exception as e2:
            bad.append((u, str(e2)))

print(f"Checked: {len(urls)}, OK: {ok}, Bad: {len(bad)}")
for b in bad:
    print("BAD:", b)
