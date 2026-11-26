content = open(r'e:\WORK\my page\index.html', encoding='utf-8').read()
old = '      <a href="webmaster.html">Webmaster</a>'
new = ('      <a href="culture90s.html">The 90s</a> |\n'
       '      <a href="bootlegs.html">Bootlegs</a> |\n'
       '      <a href="influences.html">Influences</a> |\n'
       '      <a href="webmaster.html">Webmaster</a>')
if old in content:
    content = content.replace(old, new, 1)
    open(r'e:\WORK\my page\index.html', 'w', encoding='utf-8').write(content)
    print('index nav OK, length', len(content))
else:
    print('NOT FOUND')
