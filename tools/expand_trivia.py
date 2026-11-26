import sys
content = open(r'e:\WORK\my page\trivia.html', encoding='utf-8').read()

old_ending = '</li>\n    </ul>\n\n    <hr>\n\n    <p class="last-updated">Last updated: 04/18/94</p>'

new_items = '''
      <li><i>Nevermind</i> knocked Michael Jackson&#8217;s <i>Dangerous</i> from #1 on January 11, 1992. The same week, Garth Brooks was at #3. The chart was different the following week.</li>
      <li>Butch Vig produced <i>Nevermind</i> in just seven weeks at Sound City Studios in Van Nuys, California &#8212; the same studio where Fleetwood Mac recorded <i>Rumours</i>.</li>
      <li>Kurt wore a Daniel Johnston &#8220;Hi, How Are You&#8221; t-shirt to the 1992 MTV VMAs. Johnston&#8217;s mail-order cassette distribution tripled overnight.</li>
      <li>The MTV Unplugged taping on November 18, 1993 was the last public performance Nirvana ever gave. The last song they played: &#8220;Where Did You Sleep Last Night.&#8221;</li>
      <li>Nirvana&#8217;s tour van in 1989 was a Dodge cargo van with no heat. The band and crew slept in it in January, in the Pacific Northwest.</li>
      <li>Steve Albini recorded <i>In Utero</i> in 14 days in February 1993. He charged a flat fee of $24,000. He accepted no royalties.</li>
      <li>The word &#8220;nirvana&#8221; in Sanskrit means &#8220;blowing out&#8221; &#8212; the extinction of desire and suffering. Kurt liked that definition. He said it was close to his definition of punk rock.</li>
      <li>Lollapalooza 1992 offered Nirvana the headlining slot. Kurt turned it down. Pearl Jam headlined instead.</li>
      <li>The Cobain Journals were published in 2002 by Riverhead Books, photocopied directly from Kurt&#8217;s handwritten notebooks. They include diary entries, song drafts, shopping lists, and 20 pages of drawings.</li>
      <li>At the 1992 Reading Festival, Kurt arrived onstage in a wheelchair pushed by Krist, wearing a hospital gown and blond wig. He stood up and played for two hours.</li>
      <li>Kurt&#8217;s K Records tattoo &#8212; on his left forearm &#8212; referred to Calvin Johnson&#8217;s Olympia, Washington label, home of Beat Happening and the lo-fi DIY scene he loved before grunge.</li>
      <li>The original price of Nirvana&#8217;s first Sub Pop single &#8220;Love Buzz&#8221; / &#8220;Big Cheese&#8221; (1988) was $3.00 from the Sub Pop Singles Club.</li>
      <li>Shonen Knife, the Japanese pop-punk band Kurt called &#8220;the greatest band in the world,&#8221; toured as Nirvana&#8217;s support act in Europe in 1991 and in the US in 1993.</li>
      <li>At the last show Nirvana ever played &#8212; Munich, March 1, 1994 &#8212; Kurt said nothing to the audience between songs. He walked offstage after the encore and did not come back.</li>'''

# find the closing </ul> near the end of the list
marker = 'In the Pines."</li>\n    </ul>'
if marker in content:
    content = content.replace(marker, 'In the Pines."</li>' + new_items + '\n    </ul>', 1)
    open(r'e:\WORK\my page\trivia.html', 'w', encoding='utf-8').write(content)
    print('trivia: OK, new length', len(content))
else:
    # debug
    idx = content.rfind('"In the Pines.')
    print('NOT FOUND, context:', repr(content[idx:idx+100]))
    sys.exit(1)
