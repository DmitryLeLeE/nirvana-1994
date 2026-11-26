import glob, os

MARKER = '<a href="quiz.html">Quiz</a>'
ADD = '<a href="wall.html">Kurt Wall</a> |\n      '
base = r'e:\WORK\my page'
updated = []
for fp in sorted(glob.glob(os.path.join(base, '*.html'))):
    fn = os.path.basename(fp)
    txt = open(fp, encoding='utf-8').read()
    if 'wall.html' in txt:
        continue
    if MARKER in txt:
        txt = txt.replace(MARKER, ADD + MARKER, 1)
        open(fp, 'w', encoding='utf-8').write(txt)
        updated.append(fn)
print('Kurt Wall added to nav on:', len(updated), updated)
