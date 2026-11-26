window.NIRVANA_RELEASES = [
  { id: "bleach", title: "Bleach", kind: "Studio Album", date: "June 15, 1989", label: "Sub Pop (SP34)", producer: "Jack Endino", studio: "Reciprocal Recording, Seattle", spotifyUrl: "https://open.spotify.com/album/4vE2n8x6j2q9k8k8x6j2q9", notes: "Recorded in ~30 hours for $606.17 (paid by Jason Everman). Features Chad Channing on drums and Dale Crover on three earlier tracks." },
  { id: "nevermind", title: "Nevermind", kind: "Studio Album", date: "September 24, 1991", label: "DGC (DGCD-24425)", producer: "Butch Vig", studio: "Sound City Studios, Van Nuys, CA", spotifyUrl: "https://open.spotify.com/album/2guirTSEqLizK7j9i1MTTZ", notes: "Reached #1 on Billboard 200 on Jan 11, 1992. Early CD pressings include hidden track 'Endless, Nameless' after ~10 minutes of silence." },
  { id: "incesticide", title: "Incesticide", kind: "Compilation", date: "December 15, 1992", label: "DGC / Sub Pop", producer: "Jack Endino, Steve Fisk, Butch Vig, Dale Griffin", studio: "Various (1988-1991)", spotifyUrl: "https://open.spotify.com/album/6I5B8i1Z9W4wK7l6B0d0Q8", notes: "B-sides, BBC Peel/Goodier sessions, and early demos. Cover painting by Kurt Cobain." },
  { id: "inutero", title: "In Utero", kind: "Studio Album", date: "September 21, 1993", label: "DGC (DGCD-24607)", producer: "Steve Albini (Scott Litt remixed 2 singles)", studio: "Pachyderm Studio, Cannon Falls, MN", spotifyUrl: "https://open.spotify.com/album/7wOOA7l306K8HfBKfPoafr", notes: "Recorded in 14 days in February 1993. Studio rental $24,000; Albini flat fee $100,000 with zero royalties." },
  { id: "unplugged", title: "MTV Unplugged in New York", kind: "Live / Acoustic", date: "November 1, 1994", label: "DGC", producer: "Nirvana & Scott Litt", studio: "Sony Music Studios, NYC (taped Nov 18, 1993)", spotifyUrl: "https://open.spotify.com/album/1To7kv722A8SpZF789MZy7", notes: "Acoustic set featuring Pat Smear, Lori Goldston (cello), and Cris & Curt Kirkwood of Meat Puppets. Won 1996 Grammy." },
  { id: "slts-single", title: "Smells Like Teen Spirit (Single)", kind: "Single", date: "September 10, 1991", label: "DGC", producer: "Butch Vig", studio: "Sound City / Smart Studios", spotifyUrl: "https://open.spotify.com/artist/6olE6TJLqED3rqDCT0FyPh", notes: "Peaked at #6 on Billboard Hot 100. B-sides: 'Even in His Youth' and 'Aneurysm'." },
  { id: "lovebuzz-single", title: "Love Buzz / Big Cheese", kind: "Single", date: "November 1988", label: "Sub Pop Singles Club #1 (SP23)", producer: "Jack Endino", studio: "Reciprocal Recording, Seattle", spotifyUrl: "https://open.spotify.com/artist/6olE6TJLqED3rqDCT0FyPh", notes: "Hand-numbered edition of 1,000 copies on 7-inch vinyl. Nirvana's debut single." },
  { id: "peel-sessions", title: "BBC Peel Sessions (1989-1991)", kind: "Demo / Radio Session", date: "1989 / 1990 / 1991", label: "BBC Radio 1", producer: "Dale Griffin / Miti Adhikari", studio: "Maida Vale Studios, London", spotifyUrl: "https://open.spotify.com/artist/6olE6TJLqED3rqDCT0FyPh", notes: "Three documented BBC sessions (Oct 26, 1989; Oct 21, 1990; Sept 3, 1991) verified via LiveNirvana." }
];

window.NIRVANA_SONGS = [
  {
    id: "drain-you",
    title: "Drain You",
    album: "Nevermind",
    year: 1991,
    duration: "3:43",
    category: "album",
    youtubeId: "d17254e6528", // fallback to official search/playlist when no single MV
    officialVideoId: "",
    spotifyQuery: "Nirvana Drain You",
    writers: "Kurt Cobain (music: Cobain/Grohl/Novoselic)",
    session: "May-June 1991, Sound City Studios, Van Nuys, CA (Butch Vig)",
    personnel: "Kurt Cobain (vocals, guitar), Krist Novoselic (bass), Dave Grohl (drums, backing vocals)",
    story: "Cobain called 'Drain You' one of his proudest compositions, describing it as a love song about two babies in the same hospital bed. The chaotic middle eight features squeaky rubber duck toys recorded in the studio.",
    versions: [
      { type: "Studio", label: "Nevermind LP (1991)", duration: "3:43", detail: "Multi-tracked guitars layered by Butch Vig; rubber-duck noise breakdown." },
      { type: "Radio Session", label: "BBC Peel Session #3 (Sept 3, 1991)", duration: "3:36", detail: "Rawer, faster BBC studio take recorded just weeks before Nevermind dropped." },
      { type: "Live", label: "Live and Loud, Pier 48 (Dec 13, 1993)", duration: "3:45", detail: "Two-guitar assault with Pat Smear; Kurt breaks a guitar string mid-song and switches instruments." },
      { type: "Demo", label: "Smart Studios / Boombox Demo (1990-91)", duration: "3:30", detail: "Early arrangement showing the quiet/loud bridge taking shape." }
    ],
    links: [
      { label: "Lyrics", href: "lyrics.html" },
      { label: "Concerts (Live & Loud)", href: "concerts.html" },
      { label: "Gears & Pedals", href: "gear.html" },
      { label: "Gallery (1992)", href: "gallery.html" }
    ]
  },
  {
    id: "slts",
    title: "Smells Like Teen Spirit",
    album: "Nevermind",
    year: 1991,
    duration: "5:01",
    category: "single",
    officialVideoId: "hTWKbfoikeg",
    writers: "Kurt Cobain, Krist Novoselic, Dave Grohl",
    session: "May-June 1991, Sound City Studios, Van Nuys, CA (Butch Vig)",
    personnel: "Kurt Cobain (vocals, guitar), Krist Novoselic (bass), Dave Grohl (drums)",
    story: "Written in early 1991 while Cobain was trying to write 'the ultimate pop song' inspired by the Pixies' quiet-loud dynamics. Kathleen Hanna spray-painted 'Kurt Smells Like Teen Spirit' on his wall, referring to Tobi Vail's deodorant. Premiered live at OK Hotel in Seattle on April 17, 1991.",
    versions: [
      { type: "Studio", label: "Nevermind LP (1991)", duration: "5:01", detail: "Fender Mustang/Jaguar + Boss DS-1, mixed by Andy Wallace." },
      { type: "Live", label: "OK Hotel, Seattle (Apr 17, 1991)", duration: "4:45", detail: "First known live performance, featuring different early lyrics." },
      { type: "Live", label: "Saturday Night Live (Jan 11, 1992)", duration: "4:50", detail: "Broadcast the day Nevermind hit #1 on Billboard 200." },
      { type: "Demo", label: "Boombox Rehearsal (Mar 1991)", duration: "4:32", detail: "Raw garage rehearsal recorded on cassette before Sound City." }
    ],
    links: [
      { label: "ASCII Guitar Tab", href: "tabs.html#slts" },
      { label: "Video Breakdown", href: "videos.html" },
      { label: "OK Hotel on Map", href: "map.html" },
      { label: "Lyrics", href: "lyrics.html" }
    ]
  },
  {
    id: "come-as-you-are",
    title: "Come As You Are",
    album: "Nevermind",
    year: 1991,
    duration: "3:39",
    category: "single",
    officialVideoId: "vabnZ9-ex7o",
    writers: "Kurt Cobain",
    session: "May-June 1991, Sound City Studios, Van Nuys, CA (Butch Vig)",
    personnel: "Kurt Cobain (vocals, guitar), Krist Novoselic (bass), Dave Grohl (drums)",
    story: "Built on a hypnotic D-standard riff processed through an Electro-Harmonix Small Clone chorus pedal. Released as the second single from Nevermind in March 1992, reaching #32 on the Hot 100.",
    versions: [
      { type: "Studio", label: "Nevermind LP (1991)", duration: "3:39", detail: "Tuned down one full step (D standard); iconic Small Clone chorus tone." },
      { type: "Acoustic", label: "MTV Unplugged in New York (Nov 18, 1993)", duration: "4:13", detail: "Acoustic guitar + cello arrangement; calmer and more melancholic." },
      { type: "Live", label: "Terminal Eins, Munich (Mar 1, 1994)", duration: "3:50", detail: "Interrupted by a brief venue power outage during the first verse and restarted." }
    ],
    links: [
      { label: "ASCII Guitar Tab", href: "tabs.html#caya" },
      { label: "Gear (Small Clone)", href: "gear.html" },
      { label: "Concerts (Munich)", href: "concerts.html" }
    ]
  },
  {
    id: "about-a-girl",
    title: "About a Girl",
    album: "Bleach",
    year: 1989,
    duration: "2:48",
    category: "album",
    officialVideoId: "AhcttcXcRYY",
    writers: "Kurt Cobain",
    session: "December 1988 / January 1989, Reciprocal Recording, Seattle (Jack Endino)",
    personnel: "Kurt Cobain (vocals, guitar), Krist Novoselic (bass), Chad Channing (drums)",
    story: "Written after Cobain spent an afternoon listening repeatedly to 'Meet the Beatles!'. He hesitated to put such a melodic song on Bleach, fearing it would alienate Sub Pop's grunge audience. Later became the opener and lead single of MTV Unplugged.",
    versions: [
      { type: "Studio", label: "Bleach LP (1989)", duration: "2:48", detail: "Fast, jangly electric take with Chad Channing on drums." },
      { type: "Radio Session", label: "BBC Peel Session #1 (Oct 26, 1989)", duration: "2:44", detail: "Maida Vale Studio 4 live-in-studio broadcast." },
      { type: "Acoustic", label: "MTV Unplugged in New York (Nov 18, 1993)", duration: "3:37", detail: "Opened the Unplugged set; released as a promotional single in Oct 1994." }
    ],
    links: [
      { label: "ASCII Guitar Tab", href: "tabs.html#aboutagirl" },
      { label: "Peel Sessions", href: "bootlegs.html" },
      { label: "The Beatles Influence", href: "influences.html" }
    ]
  },
  {
    id: "heart-shaped-box",
    title: "Heart-Shaped Box",
    album: "In Utero",
    year: 1993,
    duration: "4:41",
    category: "single",
    officialVideoId: "n6P0SitRwy8",
    writers: "Kurt Cobain",
    session: "February 1993, Pachyderm Studio, MN (Steve Albini); remixed by Scott Litt",
    personnel: "Kurt Cobain (vocals, guitar), Krist Novoselic (bass), Dave Grohl (drums)",
    story: "Lead single from In Utero, written in Drop Db tuning. One of two tracks remixed by Scott Litt after DGC felt Albini's original mix buried the vocals. Also the very last song Nirvana ever performed live (Munich, March 1, 1994).",
    versions: [
      { type: "Studio", label: "In Utero LP (Scott Litt remix, 1993)", duration: "4:41", detail: "Boosted vocals and added acoustic guitar/backing harmonies in chorus." },
      { type: "Demo / Alt Mix", label: "Steve Albini Original Mix (1993)", duration: "4:41", detail: "Drier, heavier bass and rawer vocal balance before Litt's remix." },
      { type: "Live", label: "Terminal Eins, Munich (Mar 1, 1994)", duration: "4:55", detail: "The final song Nirvana ever played onstage." }
    ],
    links: [
      { label: "ASCII Guitar Tab", href: "tabs.html#hsb" },
      { label: "Video Breakdown (Corbijn)", href: "videos.html" },
      { label: "Munich Final Show", href: "concerts.html" }
    ]
  },
  {
    id: "lithium",
    title: "Lithium",
    album: "Nevermind",
    year: 1991,
    duration: "4:17",
    category: "single",
    officialVideoId: "pkcJEvMcnEg",
    writers: "Kurt Cobain",
    session: "May-June 1991, Sound City Studios (Butch Vig)",
    personnel: "Kurt Cobain (vocals, guitar), Krist Novoselic (bass), Dave Grohl (drums)",
    story: "Named after the mood-stabilizing drug. Cobain said it was partly about a fictional man turning to religion after his girlfriend dies, and partly about his own mood swings.",
    versions: [
      { type: "Studio", label: "Nevermind LP (1991)", duration: "4:17", detail: "Clean D-standard verse exploding into distorted chorus; Dave Grohl backing vocals." },
      { type: "Demo", label: "Smart Studios Demo (Apr 1990)", duration: "4:20", detail: "Early version with Chad Channing on drums." },
      { type: "Live", label: "1992 MTV VMAs (Sept 9, 1992)", duration: "4:25", detail: "Preceded by a 4-second tease of 'Rape Me' against MTV's wishes." }
    ],
    links: [
      { label: "ASCII Guitar Tab", href: "tabs.html#lithium" },
      { label: "Smart Studios Demos", href: "bootlegs.html" },
      { label: "MTV VMAs 1992", href: "culture90s.html" }
    ]
  },
  {
    id: "polly",
    title: "Polly",
    album: "Nevermind",
    year: 1991,
    duration: "2:57",
    category: "acoustic",
    officialVideoId: "",
    writers: "Kurt Cobain",
    session: "April 1990, Smart Studios, Madison, WI (Butch Vig) — kept from 1990 demo!",
    personnel: "Kurt Cobain (vocals, Stella acoustic), Krist Novoselic (bass), Chad Channing (cymbals)",
    story: "Unlike the rest of Nevermind, the album version of 'Polly' comes from the April 1990 Smart Studios session with Chad Channing. Written after Cobain read a 1987 Tacoma newspaper article about a kidnapping.",
    versions: [
      { type: "Studio", label: "Nevermind LP (1990 Smart Studios take)", duration: "2:57", detail: "Recorded on a cheap Stella 12-string with 5 nylon strings; Chad Channing on cymbals." },
      { type: "Radio Session", label: "BBC Peel Session #1 (Oct 26, 1989)", duration: "2:50", detail: "Solo acoustic/sparse band take from London." },
      { type: "Live", label: "(New Wave) Polly — Incesticide (1992)", duration: "1:47", detail: "Up-tempo punk electric version recorded for BBC in Nov 1991." },
      { type: "Acoustic", label: "MTV Unplugged (Nov 18, 1993)", duration: "3:16", detail: "Gentle acoustic performance with Dave Grohl on brushes." }
    ],
    links: [
      { label: "ASCII Guitar Tab", href: "tabs.html#polly" },
      { label: "Peel Sessions", href: "bootlegs.html" }
    ]
  },
  {
    id: "all-apologies",
    title: "All Apologies",
    album: "In Utero",
    year: 1993,
    duration: "3:51",
    category: "single",
    officialVideoId: "aWmkuH1k7uA",
    writers: "Kurt Cobain",
    session: "February 1993, Pachyderm Studio (Albini); remixed by Scott Litt",
    personnel: "Kurt Cobain (vocals, guitar), Krist Novoselic (bass), Dave Grohl (drums), Kera Schaley (cello)",
    story: "Dedicated to Courtney Love and Frances Bean. Combines a hypnotic Drop D riff with Kera Schaley's cello and a mantra-like coda ('All in all is all we are').",
    versions: [
      { type: "Studio", label: "In Utero LP (Scott Litt remix, 1993)", duration: "3:51", detail: "Features Kera Schaley on cello and warm bass tone." },
      { type: "Acoustic", label: "MTV Unplugged in New York (Nov 18, 1993)", duration: "4:23", detail: "Performed with Lori Goldston on cello and Pat Smear on second guitar." },
      { type: "Demo", label: "Music Source Studio Demo (Jan 1991)", duration: "3:40", detail: "Early acoustic/folk-punk arrangement." }
    ],
    links: [
      { label: "Family", href: "family.html" },
      { label: "Lyrics", href: "lyrics.html" }
    ]
  },
  {
    id: "where-did-you-sleep",
    title: "Where Did You Sleep Last Night",
    album: "MTV Unplugged in New York",
    year: 1994,
    duration: "5:08",
    category: "acoustic",
    officialVideoId: "hEMm7gxBYSc",
    writers: "Traditional / Lead Belly arrangement",
    session: "November 18, 1993, Sony Music Studios, NYC",
    personnel: "Kurt Cobain (vocals, acoustic), Krist Novoselic (acoustic bass), Dave Grohl (drums), Pat Smear (guitar), Lori Goldston (cello)",
    story: "Traditional Appalachian folk song popularized by Lead Belly in the 1940s. Cobain chose it to close MTV Unplugged and refused an encore afterward, telling the producer nothing could top that final screamed verse.",
    versions: [
      { type: "Acoustic", label: "MTV Unplugged in New York (1993/1994)", duration: "5:08", detail: "Iconic final live acoustic performance; held the last note until his voice broke." },
      { type: "Bootleg / Side Project", label: "The Jury (1989 studio session)", duration: "4:55", detail: "Kurt and Krist recorded Lead Belly covers with Mark Lanegan (Screaming Trees)." }
    ],
    links: [
      { label: "Lead Belly Influence", href: "influences.html" },
      { label: "Unplugged Tracklist", href: "bootlegs.html" }
    ]
  },
  {
    id: "ykyr",
    title: "You Know You're Right",
    album: "Nirvana (2002)",
    year: 1994,
    duration: "3:38",
    category: "demo",
    officialVideoId: "qv96yJYhk3M",
    writers: "Kurt Cobain",
    session: "January 30, 1994, Robert Lang Studios, North Seattle (Adam Kasper)",
    personnel: "Kurt Cobain (vocals, guitar), Krist Novoselic (bass), Dave Grohl (drums)",
    story: "Logged as 'Kurt's Tune #1' on the final day of Nirvana's January 28-30, 1994 session at Robert Lang Studios — their last studio recording. Stayed unreleased until 2002 after legal settlement.",
    versions: [
      { type: "Studio", label: "Robert Lang Studios Master (Jan 30, 1994)", duration: "3:38", detail: "Official 2002 release; haunting harmonics and raw screamed chorus." },
      { type: "Live / Bootleg", label: "Aragon Ballroom, Chicago (Oct 23, 1993)", duration: "3:50", detail: "Only documented live performance (titled 'Autopilot' or 'On the Mountain' by tape traders)." }
    ],
    links: [
      { label: "Bootlegs & Rarities", href: "bootlegs.html" },
      { label: "Robert Lang on Map", href: "map.html" },
      { label: "Timeline 1994", href: "timeline.html" }
    ]
  },
  {
    id: "love-buzz",
    title: "Love Buzz",
    album: "Bleach",
    year: 1988,
    duration: "3:35",
    category: "single",
    officialVideoId: "",
    writers: "Robbie van Leeuwen (Shocking Blue cover)",
    session: "June-September 1988, Reciprocal Recording, Seattle (Jack Endino)",
    personnel: "Kurt Cobain (vocals, guitar), Krist Novoselic (bass), Chad Channing (drums)",
    story: "Nirvana's debut single (Sub Pop SP23, Nov 1988), limited to 1,000 hand-numbered copies. Krist Novoselic suggested covering the 1969 Dutch psych-rock track by Shocking Blue.",
    versions: [
      { type: "Studio", label: "Sub Pop Single / Bleach LP (1988-89)", duration: "3:35", detail: "Includes Kurt's sound-collage intro (trimmed slightly on Bleach LP)." },
      { type: "Radio Session", label: "BBC Peel Session #1 (Oct 26, 1989)", duration: "3:22", detail: "Tight live-in-studio radio take." }
    ],
    links: [
      { label: "Sub Pop History", href: "grunge.html" },
      { label: "Gallery (Love Buzz cover)", href: "gallery.html" }
    ]
  },
  {
    id: "do-re-mi",
    title: "Do Re Mi",
    album: "With the Lights Out (2004)",
    year: 1994,
    duration: "4:24",
    category: "demo",
    officialVideoId: "",
    writers: "Kurt Cobain",
    session: "Early 1994, home 4-track cassette recording, Seattle",
    personnel: "Kurt Cobain (vocals, acoustic guitar)",
    story: "One of Kurt Cobain's final home recordings, taped alone in his Seattle bedroom. Reflects his stated desire in early 1994 to pivot toward quieter, melodic acoustic songwriting.",
    versions: [
      { type: "Demo", label: "Home 4-Track Cassette (1994)", duration: "4:24", detail: "Solo acoustic voice and guitar; released in 2004 box set." }
    ],
    links: [
      { label: "Kurt's Final Plans", href: "kurt.html" },
      { label: "Discography Rarities", href: "discography.html" }
    ]
  }
];
