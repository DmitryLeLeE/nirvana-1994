import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def load_js_globals(files):
    # Use node if available, else parse simple JSON-like JS? Let's check node first, or evaluate via python?
    # Actually node is super clean if installed, let's try node first.
    js_code = "const window = {};\n"
    for f in files:
        js_code += Path(ROOT / f).read_text(encoding="utf-8") + "\n"
    js_code += "console.log(JSON.stringify(window));"
    res = subprocess.run(["node"], input=js_code, capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        raise RuntimeError(f"Node error: {res.stderr}")
    return json.loads(res.stdout)

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

# 1. Concerts
concerts = data.get("NIRVANA_CONCERTS", [])
valid_setlist = {"COMPLETE", "PARTIAL", "INCOMPLETE", "UNKNOWN"}
setlist_counts = {k: 0 for k in valid_setlist}
for c in concerts:
    st = c.get("setlist_status")
    if st not in valid_setlist:
        errors.append(f"Concert {c.get('id')} invalid setlist_status: {st}")
    else:
        setlist_counts[st] += 1
    if not c.get("setlist_sources"):
        errors.append(f"Concert {c.get('id')} missing setlist_sources")

# 2. Photos
photos = data.get("NIRVANA_PHOTOS", [])
artifacts = {a["id"]: a for a in data.get("NIRVANA_ARTIFACTS", [])}
gallery_html = (ROOT / "gallery.html").read_text(encoding="utf-8")
if "classifyCell" in gallery_html:
    errors.append("gallery.html still contains heuristic classifyCell()")
for p in photos:
    for req in ("id", "src", "capture_date", "photographer", "location", "license", "source_url"):
        if not p.get(req):
            errors.append(f"Photo {p.get('id')} missing {req}")
    aid = p.get("artifact_id")
    if aid and aid not in artifacts:
        errors.append(f"Photo {p.get('id')} references missing artifact_id {aid}")

# 3. Scene & Influences
scene = data.get("NIRVANA_SCENE_ENTITIES", [])
inf = data.get("NIRVANA_INFLUENCE_LINKS", [])
for item in scene + inf:
    srcs = item.get("sources") or []
    if not srcs or not all(s.get("source_url", "").startswith("https://") for s in srcs):
        errors.append(f"Scene/Inf {item.get('id')} missing valid https sources")

# 4. Releases
releases = data.get("NIRVANA_PHYSICAL_RELEASES", [])
for r in releases:
    for req in ("id", "category_type", "variant_description", "tracklist_summary", "source_url"):
        if not r.get(req):
            errors.append(f"Release {r.get('id')} missing {req}")

# 5. Studios & Sessions
studios = {s["id"]: s for s in data.get("NIRVANA_STUDIOS", [])}
sessions = data.get("NIRVANA_SESSIONS", [])
valid_comp = {"COMPLETE RECORDING LIST", "SELECTED TRACKS", "PARTIAL DOCUMENTATION", "UNKNOWN"}
for st in studios.values():
    if not st.get("source_url", "").startswith("https://"):
        errors.append(f"Studio {st.get('id')} missing https source_url")
for ses in sessions:
    if ses.get("completeness_status") not in valid_comp:
        errors.append(f"Session {ses.get('id')} invalid completeness_status: {ses.get('completeness_status')}")
    if not ses.get("session_date") or not ses.get("first_release_date"):
        errors.append(f"Session {ses.get('id')} missing separated session_date/first_release_date")
    sid = ses.get("studio_id")
    if sid and sid not in studios:
        errors.append(f"Session {ses.get('id')} references missing studio_id {sid}")
    if not ses.get("source_url", "").startswith("https://"):
        errors.append(f"Session {ses.get('id')} missing https source_url")

report = {
    "concerts_count": len(concerts),
    "setlist_counts": setlist_counts,
    "photos_count": len(photos),
    "artifacts_count": len(artifacts),
    "scene_entities_count": len(scene),
    "influence_links_count": len(inf),
    "releases_count": len(releases),
    "studios_count": len(studios),
    "sessions_count": len(sessions),
    "songs_count": len(data.get("NIRVANA_SONGS", [])),
    "map_places_count": len(data.get("NIRVANA_MAP_PLACES", [])),
    "errors": errors,
}
print(json.dumps(report, indent=2, ensure_ascii=False))
if errors:
    raise SystemExit(1)
