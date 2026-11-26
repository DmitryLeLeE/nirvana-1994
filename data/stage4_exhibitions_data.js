// Stage 4.5 — DIGITAL ARCHIVE EXHIBITIONS (5 Curated Exhibitions)
// Explicitly classifies items as ORIGINAL ARTIFACT, ARCHIVAL PHOTO, ILLUSTRATIVE RECONSTRUCTION, or MODERN RESEARCH MATERIAL.
window.NIRVANA_EXHIBITIONS = [
  {
    id: "exh-subpop",
    number: "EXHIBITION 01",
    title: "THE SUB POP YEARS (1987–1990)",
    intro: "From Aberdeen police records and Olympia dorm flyers to the $606.17 Bleach LP and 1989 European passport stamps, these items document Nirvana's independent Pacific Northwest period.",
    photo_ids: ["pho-14", "pho-15", "pho-17", "pho-16", "pho-01"],
    artifact_ids: ["art-mugshot-1986", "art-lovebuzz-cover", "art-bern-passport"],
    concert_ids: ["con-1987-04-18-tacoma", "con-1989-06-23-rhino"],
    album_links: [{ label: "Album Dossier: Bleach", href: "albums.html?album=bleach" }],
    sources: [
      { label: "LiveNirvana — 1987–1989", href: "https://www.livenirvana.com/concerts/87/87-04-18.php" },
      { label: "Wikipedia — Bleach", href: "https://en.wikipedia.org/wiki/Bleach_(Nirvana_album)" }
    ]
  },
  {
    id: "exh-nevermind",
    number: "EXHIBITION 02",
    title: "THE NEVERMIND PHENOMENON (1991–1992)",
    intro: "Visual evidence of Nirvana's transition from the April 1991 OK Hotel benefit to the 1992 MTV Video Music Awards, Rolling Stone covers, and global chart dominance.",
    photo_ids: ["pho-02", "pho-06", "pho-10", "pho-20"],
    artifact_ids: ["art-mustang-slts", "art-nirvana-1992-trio", "art-flyer-okhotel", "art-mag-rollingstone"],
    concert_ids: ["con-1991-04-17-okhotel", "con-1991-10-31-paramount", "con-1992-01-11-snl"],
    album_links: [{ label: "Album Dossier: Nevermind", href: "albums.html?album=nevermind" }],
    sources: [
      { label: "LiveNirvana — OK Hotel 1991", href: "https://www.livenirvana.com/concerts/91/91-04-17.php" },
      { label: "Wikipedia — Nevermind", href: "https://en.wikipedia.org/wiki/Nevermind" }
    ]
  },
  {
    id: "exh-inutero",
    number: "EXHIBITION 03",
    title: "IN UTERO (1992–1993)",
    intro: "Anatomical imagery, Kurt Cobain's Incesticide painting, and the November 1993 Sony Music Studios acoustic taping that closed the band's American touring era.",
    photo_ids: ["pho-03", "pho-04"],
    artifact_ids: ["art-inutero-angel", "art-backstage-unplugged"],
    concert_ids: ["con-1993-10-23-aragon", "con-1993-11-18-unplugged", "con-1993-12-13-liveandloud"],
    album_links: [
      { label: "Album Dossier: In Utero", href: "albums.html?album=in-utero" },
      { label: "Album Dossier: Incesticide", href: "albums.html?album=incesticide" }
    ],
    sources: [
      { label: "Wikipedia — In Utero", href: "https://en.wikipedia.org/wiki/In_Utero" },
      { label: "LiveNirvana — Unplugged", href: "https://www.livenirvana.com/concerts/93/93-11-18.php" }
    ]
  },
  {
    id: "exh-road",
    number: "EXHIBITION 04",
    title: "ON THE ROAD (STAGE & ZINES)",
    intro: "Stage performance photography, destroyed instruments preserved at MoPOP, festival passes, and the 1990s DIY punk zine network that carried tape-trading classifieds.",
    photo_ids: ["pho-07", "pho-08", "pho-19"],
    artifact_ids: ["art-smashed-guitar", "art-ticket-reading92", "art-zine-subpop"],
    concert_ids: ["con-1991-11-25-paradiso", "con-1992-02-01-melbourne", "con-1992-08-30-reading"],
    album_links: [{ label: "Tour Journeys", href: "concerts.html#journeys" }],
    sources: [
      { label: "LiveNirvana — Reading 1992", href: "https://www.livenirvana.com/concerts/92/92-08-30.php" },
      { label: "Fan Zine Archive", href: "zines.html" }
    ]
  },
  {
    id: "exh-lastdays",
    number: "EXHIBITION 05",
    title: "THE LAST DAYS OF NIRVANA (1994 & AFTER)",
    intro: "Documentation of the final Munich concert (March 1, 1994), April 1994 dispatches, posthumous MTV Unplugged release, and modern Aberdeen/Seattle memorial landmarks.",
    photo_ids: ["pho-05", "pho-18", "pho-21", "pho-22", "pho-23"],
    artifact_ids: ["art-setlist-munich", "art-news-apr94", "art-note-boddah"],
    concert_ids: ["con-1994-02-22-rome", "con-1994-03-01-munich"],
    album_links: [{ label: "Album Dossier: MTV Unplugged", href: "albums.html?album=unplugged" }],
    sources: [
      { label: "LiveNirvana — Munich 1994", href: "https://www.livenirvana.com/concerts/94/94-03-01.php" },
      { label: "Death & Legacy Transcript", href: "death.html" }
    ]
  }
];
