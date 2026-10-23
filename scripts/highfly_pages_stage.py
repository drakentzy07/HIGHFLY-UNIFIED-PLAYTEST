#!/usr/bin/env python3
"""Stage the standalone UNIFIED playtest without changing the game's source tree or any other Pages release."""
import json, re, sys
from pathlib import Path

if len(sys.argv)!=3:
    raise SystemExit("usage: highfly_pages_stage.py GAME_DIST SOURCE_SHA")
dist=Path(sys.argv[1]); source_sha=sys.argv[2]
assert re.fullmatch(r"[a-f0-9]{40}",source_sha), "SOURCE_SHA_INVALID"
assert (dist/"index.html").is_file(), "BUILD_INDEX_MISSING"
assert (dist/"assets").is_dir(), "BUILD_ASSETS_MISSING"
assert (dist/"highfly-origin.webmanifest").is_file(), "BUILD_MANIFEST_MISSING"
base="/HIGHFLY-UNIFIED-PLAYTEST/"
index=(dist/"index.html").read_text()
assert base+"assets/" in index, "VITE_BASE_WRONG"
# Vite rewrites imported files. Static donor URLs in scripts/style/HTML,
# particularly /cobalt-hollow-lab/{ui,audio}, must be project-scoped too.
fixed=0
prefixes=("ui","audio","basis","media","assets","fonts","claudium",
          "guide-stills","highfly","map_art","map_bg","data")
roots=(dist/"assets",)
files=[p for root in roots for p in root.rglob("*") if p.is_file()]
files.extend(p for p in dist.glob("*.html"))
for p in files:
    if p.suffix not in (".js",".css",".html",".json",".webmanifest"):
        continue
    try:
        old=p.read_text()
    except (UnicodeDecodeError,OSError):
        continue
    s=old.replace("/cobalt-hollow-lab/","/HIGHFLY-UNIFIED-PLAYTEST/")
    # Only resource URLs: never change route definitions, comments or storage keys.
    for prefix in prefixes:
        for lead in ('"', "'", "`", 'url(', 'url("', "url('"):
            s=s.replace(lead+"/"+prefix+"/",lead+base+prefix+"/")
    for static in ("home-bg.png","home-bg.mp4","icon-192.png","icon-512.png",
                   "highfly-origin-icon-512.png","highfly-origin-icon-192.png"):
        for lead in ('"', "'", "`", 'url(', 'url("', "url('"):
            s=s.replace(lead+"/"+static,lead+base+static)
    if s!=old:
        p.write_text(s)
        fixed+=1

# Standalone manifest belongs only to this repo; SW is deliberately disabled
# in source for this playtest to avoid shared-domain CacheStorage interference.
manifest=dist/"highfly-origin.webmanifest"
config=json.loads(manifest.read_text())
config.update({"name":"HIGHFLY — Cazador Universal (Prueba S23)",
               "short_name":"HIGHFLY LAB","id":base,"start_url":base,
               "scope":base,"display":"standalone","orientation":"landscape"})
manifest.write_text(json.dumps(config,ensure_ascii=False,indent=2)+"\n")
# Avoid indexing disposable lab, but preserve original title and architecture.
page=dist/"index.html"
html=page.read_text()
html=html.replace("<title>HIGHFLY —","<title>HIGHFLY UNIFIED PLAYTEST —")
if '<meta name="robots"' not in html:
    html=html.replace("</head>",'<meta name="robots" content="noindex, nofollow" /></head>')
page.write_text(html)
assert base+"assets/" in html,"FINAL_HTML_BASE_WRONG"
for rel in re.findall(r"""(?:src|href)=["'](/HIGHFLY-UNIFIED-PLAYTEST/assets/[^"']+)""",html):
    f=dist/rel.removeprefix(base)
    assert f.is_file(), "MISSING_VERSIONED_ASSET_"+rel
assert (dist/"highfly-origin-icon-512.png").is_file(), "PWA_ICON_MISSING"
assert (dist/"highfly-origin-icon-192.png").is_file(), "PWA_ICON_MISSING"
assets=list((dist/"media").rglob("*.glb")) if (dist/"media").is_dir() else []
assert len(assets)>100,"MISSING_WORLD_MODELS"
size=sum(p.stat().st_size for p in dist.rglob("*") if p.is_file())
assert size<1_055_000_000,"PAGES_ARTIFACT_OVERSIZE_"+str(size)
data={"edition":"HIGHFLY UNIFIED PLAYTEST — Universal Hunter Recovery",
      "sourceCommit":source_sha,"isolatedSaves":True,
      "storageNamespace":"highfly-unified-playtest-*",
      "level1PaidSkills":True,"nativeWorld":True,
      "productionRepoUntouched":True,"physicalS23":"PENDING HUMAN TEST",
      "base":base,"filesFixed":fixed,"glbCount":len(assets),"uncompressedBytes":size}
(dist/"highfly-playtest-qa.json").write_text(json.dumps(data,indent=2)+"\n")
(dist/".nojekyll").touch()
print("HIGHFLY_STANDALONE_PAGES_STAGE_GREEN=1",json.dumps(data),flush=True)
