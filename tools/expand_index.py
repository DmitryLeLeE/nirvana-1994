content = open(r'e:\WORK\my page\index.html', encoding='utf-8').read()

# Insert a "What else was happening in 1994" section right before the visitor counter
marker = '    <p>\n      You are visitor number'
insert = '''    <h3>What else was happening in 1994</h3>
    <p class="small">the world the music lived inside</p>

    <table class="content">
      <tr><th>Happening</th><th>Notes</th></tr>
      <tr><td>OJ Simpson arrested</td><td>June 17, 1994 &#8212; 95 million people watched the Bronco chase live on TV</td></tr>
      <tr><td><i>Pulp Fiction</i> released</td><td>Cannes Palme d&#8217;Or winner; Tarantino; changed what a movie could look like</td></tr>
      <tr><td><i>Friends</i> premieres</td><td>September 22, NBC &#8212; &#8220;The One Where Monica Gets a Roommate&#8221;</td></tr>
      <tr><td>Nelson Mandela elected</td><td>South Africa&#8217;s first democratic election, April 27, 1994</td></tr>
      <tr><td>Cobain dies</td><td>April 5, 1994 &#8212; Seattle</td></tr>
      <tr><td>Green Day releases <i>Dookie</i></td><td>February 1994; punk finds the suburbs; MTV again</td></tr>
      <tr><td>Kurt Vonnegut still alive</td><td>writing, smoking, being right about things</td></tr>
      <tr><td>Oasis releases <i>Definitely Maybe</i></td><td>August 1994; Liam says Nirvana are &#8220;depressing&#8221;</td></tr>
      <tr><td>Rwandan genocide</td><td>April&#8211;July 1994; 800,000 dead; the world largely ignored it</td></tr>
      <tr><td><i>Forrest Gump</i> in theaters</td><td>Tom Hanks; $678 million worldwide; &#8220;life is like a box of chocolates&#8221;</td></tr>
    </table>

    <p class="small">
      <a href="culture90s.html">&#8594; more about the world of 1991&#8211;1994</a>
    </p>

    <hr>

'''

if marker in content:
    content = content.replace(marker, insert + marker, 1)
    open(r'e:\WORK\my page\index.html', 'w', encoding='utf-8').write(content)
    print('index: OK, new length', len(content))
else:
    print('NOT FOUND')
    idx = content.find('visitor number')
    print(repr(content[max(0,idx-100):idx+200]))
