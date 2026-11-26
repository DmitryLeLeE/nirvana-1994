import json
import re
import subprocess
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent.parent


def load_js_globals(files):
    js_code = "const window = {};\n"
    for f in files:
        js_code += (ROOT / f).read_text(encoding="utf-8") + "\n"
    js_code += "console.log(JSON.stringify(window));"
    res = subprocess.run(["node"], input=js_code, capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        raise RuntimeError(f"Node error: {res.stderr}")
    return json.loads(res.stdout)


def extract_html_ids(html_path):
    txt = html_path.read_text(encoding="utf-8")
    return set(re.findall(r'\bid=["\']([^"\']+)["\']', txt))


data = load_js_globals([
    "data/concerts_data.js",
    "data/sessions_data.js",
    "data/releases_data.js",
    "data/photos_data.js",
    "data/artifacts_data.js",
    "data/scene_influences_data.js",
    "data/listening_data.js",
    "data/map_data.js",
])

errors = []
warnings = []
unverified = []
passed = []

concerts = data.get("NIRVANA_CONCERTS", [])
studios_list = data.get("NIRVANA_STUDIOS", [])
sessions = data.get("NIRVANA_SESSIONS", [])
releases = data.get("NIRVANA_PHYSICAL_RELEASES", [])
photos = data.get("NIRVANA_PHOTOS", [])
artifacts = data.get("NIRVANA_ARTIFACTS", [])
scene = data.get("NIRVANA_SCENE_ENTITIES", [])
inf = data.get("NIRVANA_INFLUENCE_LINKS", [])
songs = data.get("NIRVANA_SONGS", [])
map_places = data.get("NIRVANA_MAP_PLACES", [])

# Unique ID checks
def check_unique_ids(items, label):
    seen = set()
    for it in items:
        iid = it.get("id")
        if not iid:
            errors.append(f"{label}: item missing id")
        elif iid in seen:
            errors.append(f"{label}: duplicate id '{iid}'")
        seen.add(iid)
    return {it["id"]: it for it in items if it.get("id")}


concerts_by_id = check_unique_ids(concerts, "concerts")
studios_by_id = check_unique_ids(studios_list, "studios")
sessions_by_id = check_unique_ids(sessions, "sessions")
releases_by_id = check_unique_ids(releases, "releases")
photos_by_id = check_unique_ids(photos, "photos")
artifacts_by_id = check_unique_ids(artifacts, "artifacts")
scene_by_id = check_unique_ids(scene, "scene")
inf_by_id = check_unique_ids(inf, "influences")
songs_by_id = check_unique_ids(songs, "songs")
places_by_id = check_unique_ids(map_places, "map_places")

# Dynamic IDs rendered into specific HTML pages
dynamic_ids_by_page = {
    "concerts.html": set(concerts_by_id),
    "listening.html": set(studios_by_id) | set(sessions_by_id),
    "discography.html": set(releases_by_id),
    "artifacts.html": set(artifacts_by_id),
    "grunge.html": set(scene_by_id),
    "influences.html": set(inf_by_id),
}

html_ids_cache = {}

def validate_internal_href(href, context):
    if not href or href.startswith("http://") or href.startswith("https://") or href.startswith("mailto:"):
        return
    if href.startswith("/"):
        errors.append(f"{context}: absolute leading slash internal href '{href}'")
        return
    parsed = urlparse(href)
    page = parsed.path
    if not page:
        return
    target_path = ROOT / page
    if not target_path.exists():
        errors.append(f"{context}: target HTML does not exist '{href}'")
        return
    if parsed.fragment:
        if page not in html_ids_cache:
            html_ids_cache[page] = extract_html_ids(target_path) | dynamic_ids_by_page.get(page, set())
        if parsed.fragment not in html_ids_cache[page]:
            errors.append(f"{context}: anchor '#{parsed.fragment}' not found in '{page}'")
    qs = parse_qs(parsed.query)
    if page == "map.html" and "place" in qs:
        for pid in qs["place"]:
            if pid not in places_by_id:
                errors.append(f"{context}: map.html?place={pid} does not match any NIRVANA_MAP_PLACES id")
    if page == "listening.html" and "song" in qs:
        for sid in qs["song"]:
            if sid not in songs_by_id:
                errors.append(f"{context}: listening.html?song={sid} does not match any NIRVANA_SONGS id")
    if page == "artifacts.html" and "id" in qs:
        for aid in qs["id"]:
            if aid not in artifacts_by_id:
                errors.append(f"{context}: artifacts.html?id={aid} does not match any NIRVANA_ARTIFACTS id")
    if page == "concerts.html" and "concert" in qs:
        for cid in qs["concert"]:
            if cid not in concerts_by_id:
                errors.append(f"{context}: concerts.html?concert={cid} does not match any NIRVANA_CONCERTS id")


# 7.1 & 7.2 Map ID validation + coordinates + internal links
for pid, pl in places_by_id.items():
    lat, lng = pl.get("lat"), pl.get("lng")
    if not isinstance(lat, (int, float)) or not isinstance(lng, (int, float)):
        errors.append(f"Map place {pid}: invalid coordinates ({lat}, {lng})")
    elif not (-90 <= lat <= 90 and -180 <= lng <= 180):
        errors.append(f"Map place {pid}: out-of-range coordinates ({lat}, {lng})")
    for lnk in pl.get("links") or []:
        validate_internal_href(lnk.get("href"), f"map_places[{pid}]")
passed.append(f"Map places validated ({len(places_by_id)} unique IDs with valid coordinates)")

# 7.3 Gallery metadata validation
gallery_html = (ROOT / "gallery.html").read_text(encoding="utf-8")
if "classifyCell" in gallery_html:
    errors.append("gallery.html still contains heuristic classifyCell()")
if "sources.html" in gallery_html:
    errors.append("gallery.html still references non-existent sources.html")

valid_licenses = {
    "CC0", "CC BY", "CC BY-SA", "Public Domain",
    "Rights Reserved", "Fair Use / Editorial Reference", "Unknown / Unverified"
}
valid_precisions = {"EXACT", "MONTH", "YEAR", "APPROXIMATE", "UNKNOWN"}
known_authorship = 0
unknown_authorship = 0

for p in photos:
    pid = p.get("id", "?")
    for req in ("id", "src", "capture_date", "capture_date_precision", "publication_date", "photographer", "attribution", "location", "license", "license_url", "source_url", "related_href"):
        if not p.get(req):
            errors.append(f"Photo {pid} missing required field '{req}'")
    if p.get("capture_date_precision") not in valid_precisions:
        errors.append(f"Photo {pid} invalid capture_date_precision: {p.get('capture_date_precision')}")
    if p.get("license") not in valid_licenses:
        errors.append(f"Photo {pid} invalid license: {p.get('license')}")
    if p.get("license") == "Public Domain" and not p.get("license_jurisdiction"):
        errors.append(f"Photo {pid} Public Domain missing license_jurisdiction")
    if p.get("related_release_id") and p["related_release_id"] not in releases_by_id:
        errors.append(f"Photo {pid} references missing related_release_id '{p['related_release_id']}'")
    if p.get("artifact_id") and p["artifact_id"] not in artifacts_by_id:
        errors.append(f"Photo {pid} references missing artifact_id '{p['artifact_id']}'")
    validate_internal_href(p.get("related_href"), f"photos[{pid}].related_href")
    validate_internal_href(p.get("source_url"), f"photos[{pid}].source_url")

    photog = (p.get("photographer") or "").lower()
    if photog.startswith("unknown"):
        unknown_authorship += 1
        unverified.append(f"Photo {pid}: photographer unknown ({p.get('photographer')})")
    else:
        known_authorship += 1
    if p.get("capture_date_precision") in ("UNKNOWN", "APPROXIMATE"):
        unverified.append(f"Photo {pid}: capture_date precision is {p.get('capture_date_precision')} ({p.get('capture_date')})")

passed.append(f"Gallery metadata validated ({len(photos)} photos; known authorship={known_authorship}, unknown={unknown_authorship})")

# Artifacts links
for aid, art in artifacts_by_id.items():
    for lnk in art.get("links") or []:
        validate_internal_href(lnk.get("href"), f"artifacts[{aid}]")
passed.append(f"Artifacts internal links validated ({len(artifacts_by_id)} items)")

# 7.4 Concert setlist validation
valid_setlist = {"COMPLETE", "PARTIAL", "INCOMPLETE", "UNKNOWN"}
setlist_counts = {k: 0 for k in valid_setlist}
song_titles_lower = {s["title"].lower(): s["id"] for s in songs}
for c in concerts:
    cid = c.get("id", "?")
    st = c.get("setlist_status")
    sl = c.get("setlist") or []
    if st not in valid_setlist:
        errors.append(f"Concert {cid} invalid setlist_status: {st}")
    else:
        setlist_counts[st] += 1
    if st == "UNKNOWN" and len(sl) > 0:
        errors.append(f"Concert {cid} marked UNKNOWN but has non-empty setlist ({len(sl)})")
    if st in ("COMPLETE", "PARTIAL", "INCOMPLETE") and len(sl) == 0:
        errors.append(f"Concert {cid} marked {st} but has empty setlist")
    if not c.get("setlist_sources"):
        errors.append(f"Concert {cid} missing setlist_sources")
    vid = c.get("venue_id")
    if vid and vid not in places_by_id:
        errors.append(f"Concert {cid} references missing map venue_id '{vid}'")
    if st in ("PARTIAL", "INCOMPLETE", "UNKNOWN"):
        unverified.append(f"Concert {cid}: setlist_status={st} ({len(sl)} tracks)")
passed.append(f"Concerts validated ({len(concerts)} shows; setlist_counts={setlist_counts})")

# 7.5 Releases, Sessions, Scene, Songs
for r in releases:
    rid = r.get("id", "?")
    for req in ("id", "catalog_no", "category_type", "variant_description", "tracklist_summary", "source_url"):
        if not r.get(req):
            errors.append(f"Release {rid} missing {req}")
    validate_internal_href(r.get("source_url"), f"releases[{rid}].source_url")
passed.append(f"Physical releases validated ({len(releases)} items)")

valid_comp = {"COMPLETE RECORDING LIST", "SELECTED TRACKS", "PARTIAL DOCUMENTATION", "UNKNOWN"}
for st in studios_list:
    if not st.get("source_url", "").startswith("https://"):
        errors.append(f"Studio {st.get('id')} missing https source_url")
    if st.get("map_id") and st["map_id"] not in places_by_id:
        errors.append(f"Studio {st.get('id')} references missing map_id '{st['map_id']}'")

for ses in sessions:
    sid = ses.get("id", "?")
    if ses.get("completeness_status") not in valid_comp:
        errors.append(f"Session {sid} invalid completeness_status: {ses.get('completeness_status')}")
    if not ses.get("session_date") or not ses.get("first_release_date"):
        errors.append(f"Session {sid} missing separated session_date/first_release_date")
    if ses.get("studio_id") and ses["studio_id"] not in studios_by_id:
        errors.append(f"Session {sid} references missing studio_id '{ses['studio_id']}'")
    if not ses.get("source_url", "").startswith("https://"):
        errors.append(f"Session {sid} missing https source_url")
    if ses.get("completeness_status") in ("PARTIAL DOCUMENTATION", "UNKNOWN"):
        unverified.append(f"Session {sid}: completeness_status={ses.get('completeness_status')}")
passed.append(f"Studios ({len(studios_list)}) & Sessions ({len(sessions)}) validated")

for item in scene + inf:
    srcs = item.get("sources") or []
    if not srcs or not all(s.get("source_url", "").startswith("https://") for s in srcs):
        errors.append(f"Scene/Inf {item.get('id')} missing valid https sources")
passed.append(f"Scene ({len(scene)}) & Influences ({len(inf)}) validated")

for sg in songs:
    for lnk in sg.get("links") or []:
        validate_internal_href(lnk.get("href"), f"songs[{sg.get('id')}]")
passed.append(f"Songs internal links validated ({len(songs)} songs)")

report = {
    "concerts_count": len(concerts),
    "setlist_counts": setlist_counts,
    "photos_count": len(photos),
    "known_authorship_photos": known_authorship,
    "unknown_authorship_photos": unknown_authorship,
    "artifacts_count": len(artifacts),
    "scene_entities_count": len(scene),
    "influence_links_count": len(inf),
    "releases_count": len(releases),
    "studios_count": len(studios_list),
    "sessions_count": len(sessions),
    "songs_count": len(songs),
    "map_places_count": len(places_by_id),
    "errors": errors,
    "warnings": warnings,
    "unverified": unverified,
    "passed": passed,
}

(ROOT / "stage37_integrity_report.json").write_text(
    json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
)
print(json.dumps({
    "errors_count": len(errors),
    "warnings_count": len(warnings),
    "unverified_count": len(unverified),
    "passed_count": len(passed),
    "errors": errors,
    "warnings": warnings,
    "setlist_counts": setlist_counts,
    "known_authorship_photos": known_authorship,
    "unknown_authorship_photos": unknown_authorship,
}, indent=2, ensure_ascii=False))

if errors:
    raise SystemExit(1)
