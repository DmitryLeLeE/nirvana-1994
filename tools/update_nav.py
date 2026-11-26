"""
Adds the three new nav links (The 90s, Bootlegs, Influences) to ALL html files
that don't already have them.
"""
import os, glob

NAV_MARKER = '<a href="webmaster.html">Webmaster</a>'
NEW_LINKS = (
    '\n      <a href="culture90s.html">The 90s</a> |\n'
    '      <a href="bootlegs.html">Bootlegs</a> |\n'
    '      <a href="influences.html">Influences</a> |\n      '
)

base = r'e:\WORK\my page'
files = glob.glob(os.path.join(base, '*.html'))
updated = []
skipped = []

for fp in files:
    content = open(fp, encoding='utf-8').read()
    if 'culture90s.html' in content:
        skipped.append(os.path.basename(fp))
        continue
    if NAV_MARKER not in content:
        skipped.append(os.path.basename(fp) + ' [no marker]')
        continue
    content = content.replace(NAV_MARKER, NEW_LINKS + NAV_MARKER, 1)
    open(fp, 'w', encoding='utf-8').write(content)
    updated.append(os.path.basename(fp))

print('Updated:', updated)
print('Skipped:', skipped)
