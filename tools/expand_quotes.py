content = open(r'e:\WORK\my page\quotes.html', encoding='utf-8').read()

# Find the last existing quote block before the coffee photo
# Insert after the last <p class="quote"> block

new_quotes = '''
    <p class="quote">
      &#8220;I think of myself as a frustrated, angry, bored, sad little boy.&#8221;<br>
      <span class="small">&#8212; Journals, 2002</span>
    </p>

    <p class="quote">
      &#8220;If you ever need anything, please don&#8217;t hesitate to ask someone else first.&#8221;<br>
      <span class="small">&#8212; Kurt Cobain, Journals &#8212; from a note he kept in his wallet</span>
    </p>

    <p class="quote">
      &#8220;Nobody dies a virgin &#8212; life f***s us all.&#8221;<br>
      <span class="small">&#8212; Journals, 2002</span>
    </p>

    <p class="quote">
      &#8220;The duty of youth is to challenge corruption.&#8221;<br>
      <span class="small">&#8212; Kurt Cobain</span>
    </p>

    <p class="quote">
      &#8220;The sun is gone, but I have a light.&#8221;<br>
      <span class="small">&#8212; &#8220;Dumb,&#8221; <i>In Utero</i>, 1993</span>
    </p>

    <p class="quote">
      &#8220;I never went to school. I never knew what was going on. I failed eighth grade
      three times. I was completely lost. All I could do was write songs.&#8221;<br>
      <span class="small">&#8212; interview, 1993</span>
    </p>

    <p class="quote">
      &#8220;A friend is nothing but a known enemy.&#8221;<br>
      <span class="small">&#8212; Journals, 2002</span>
    </p>

    <p class="quote">
      &#8220;No one is afraid of heights. They are afraid of falling.&#8221;<br>
      <span class="small">&#8212; attributed to Kurt</span>
    </p>

    <p class="quote">
      &#8220;I am a walking contradiction and my parents are both alive.&#8221;<br>
      <span class="small">&#8212; Journals, 2002</span>
    </p>

    <p class="quote">
      &#8220;Ground control to Davy Crocket: we have a boredom problem.&#8221;<br>
      <span class="small">&#8212; Journals, 2002</span>
    </p>

'''

marker = '    <p><img class="photo" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/45/A_small_cup_of_coffee'
if marker in content:
    content = content.replace(marker, new_quotes + marker, 1)
    open(r'e:\WORK\my page\quotes.html', 'w', encoding='utf-8').write(content)
    print('quotes: OK, new length', len(content))
else:
    print('NOT FOUND')
    idx = content.find('coffee')
    print(repr(content[max(0,idx-200):idx+100]))
