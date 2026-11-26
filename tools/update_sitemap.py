content = open(r'e:\WORK\my page\sitemap.html', encoding='utf-8').read()

old = '      <tr><td><a href="secret.html">(a secret)</a></td><td>found it already, didn\'t you</td></tr>'
new = '''      <tr><td><a href="culture90s.html">The 90s</a></td><td>MTV, Lollapalooza, hair metal, flannel, what was happening in 1994</td></tr>
      <tr><td><a href="bootlegs.html">Bootlegs &amp; Rarities</a></td><td>Peel Sessions, Reading \'92, Unplugged extras, the last recording</td></tr>
      <tr><td><a href="influences.html">Influences</a></td><td>The Pixies, Lead Belly, Melvins, Sonic Youth, Neil Young, Daniel Johnston</td></tr>
      <tr><td><a href="secret.html">(a secret)</a></td><td>found it already, didn\'t you</td></tr>'''

if old in content:
    content = content.replace(old, new, 1)
    open(r'e:\WORK\my page\sitemap.html', 'w', encoding='utf-8').write(content)
    print('sitemap OK, length', len(content))
else:
    idx = content.find('secret.html')
    print('NOT FOUND context:', repr(content[max(0,idx-30):idx+80]))
