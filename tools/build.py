#!/usr/bin/env python3
"""Baut die Apps (Indonesisch, Englisch, Deutsch) aus den Teildateien. Aufruf: build.py [id|en|de|all]"""
import pathlib, sys, json
d = pathlib.Path(__file__).parent
import datetime, zoneinfo
BUILD = datetime.datetime.now(zoneinfo.ZoneInfo("Europe/Berlin")).strftime("%d.%m.%Y %H:%M")
css = (d / "style.css").read_text(encoding="utf-8")
APPS = {
 "id": dict(files=["head.js","data_a1.js","data_a2.js","data_b1.js","data_b2.js","extra_id.js","lang_id.js","mini_model_id.js","main.js"], out="belajar-indonesisch-v2.html",
            lang="de", title="Belajar – Indonesisch lernen (A1–B2)", h1="🇮🇩 Belajar – Indonesisch", short="Belajar", xp="⭐ 0 XP", st="🔥 0 Tage", i18n=None),
 "en": dict(files=["head_plain.js"]+[f"data_en_{k}.js" for k in ("a1","a2","b1","b2")]+["extra_en.js","lang_en.js","mini_model_en.js","main.js"], out="english.html",
            lang="de", title="Englisch lernen (A1–B2)", h1="🇬🇧 Englisch lernen", short="Englisch", xp="⭐ 0 XP", st="🔥 0 Tage", i18n=None),
 "de": dict(files=["head_plain.js"]+[f"data_de_{k}.js" for k in ("a1","a2","b1","b2")]+["extra_de.js","lang_de.js","mini_model_de.js","main.js"], out="deutsch.html",
            lang="en", title="Learn German (A1–B2)", h1="🇩🇪 Learn German", short="Deutsch", xp="⭐ 0 XP", st="🔥 0 days", i18n="i18n_en.json"),
}
def build(k):
    a = APPS[k]
    parts = []
    for f in a["files"]:
        p = d / f
        if not p.exists():
            print("fehlt:", f); return
        txt = p.read_text(encoding="utf-8")
        if f == "main.js" and a["i18n"]:
            tr = json.loads((d / a["i18n"]).read_text(encoding="utf-8"))
            for de in sorted(tr, key=len, reverse=True):
                txt = txt.replace(de, tr[de])
        parts.append(txt)
    js = "\n".join(parts).replace("__BUILD__", BUILD)
    html = f"""<!DOCTYPE html>
<html lang="{a['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="{a['short']}">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="theme-color" content="#f2f2f7">
<meta name="referrer" content="no-referrer">
<title>{a['title']}</title>
<style>
{css}
</style>
</head>
<body>
<header>
  <h1>{a['h1']}</h1>
  <div class="stats"><span id="sXp">{a['xp']}</span><span id="sStreak">{a['st']}</span></div>
</header>
<nav id="tabs"></nav>
<main id="view"></main>
<script>
{js}
</script>
</body>
</html>
"""
    out = d / a["out"]
    out.write_text(html, encoding="utf-8")
    (d / f"bundle_{k}.js").write_text(js, encoding="utf-8")
    if k == "id": (d / "bundle.js").write_text(js, encoding="utf-8")
    print("OK", out, len(html)//1024, "KB")
for k in (sys.argv[1:] or ["id"]):
    if k == "all":
        for x in APPS: build(x)
    else: build(k)
