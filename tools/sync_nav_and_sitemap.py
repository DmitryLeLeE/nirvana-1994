"""
Adds Tabs, Concerts, Quiz links to .nav across all HTML files and updates sitemap.html.
"""
import glob, os

NAV_MARKER = '<a href="webmaster.html">Webmaster</a>'
NEW_LINKS = (
    '<a href="tabs.html">Tabs</a> |\n'
    '      <a href="concerts.html">Concerts</a> |\n'
    '      <a href="quiz.html">Quiz</a> |\n      '
)

base = r'e:\WORK\my page'
updated = []
for fp in sorted(glob.glob(os.path.join(base, '*.html'))):
    fn = os.path.basename(fp)
    content = open(fp, encoding='utf-8').read()
    if 'tabs.html' in content:
        continue
    if NAV_MARKER in content:
        content = content.replace(NAV_MARKER, NEW_LINKS + NAV_MARKER, 1)
        open(fp, 'w', encoding='utf-8').write(content)
        updated.append(fn)

print('Nav updated:', len(updated), updated)

# Update sitemap.html
sm_path = os.path.join(base, 'sitemap.html')
sm = open(sm_path, encoding='utf-8').read()
sm_marker = '      <tr><td><a href="secret.html">(a secret)</a></td>'
sm_add = (
    '      <tr><td><a href="tabs.html">Tabs</a></td><td>ASCII guitar tabs in 1994 OLGA format</td></tr>\n'
    '      <tr><td><a href="concerts.html">Concerts</a></td><td>Paramount \'91, SNL, Reading \'92, Live and Loud, Munich \'94</td></tr>\n'
    '      <tr><td><a href="quiz.html">Quiz</a></td><td>10-question "How 1994 Are You?" fan test</td></tr>\n'
)
if 'tabs.html' in sm and 'ASCII guitar tabs' not in sm:
    sm = sm.replace(sm_marker, sm_add + sm_marker, 1)
    open(sm_path, 'w', encoding='utf-8').write(sm)
    print('Sitemap updated')
