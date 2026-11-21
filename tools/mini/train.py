#!/usr/bin/env python3
"""Trainiert die Mini-KI (Absichtserkennung) für jede App und exportiert die Gewichte als JS.
Aufruf: python3 mini/train.py [id|en|de|all]
Daten: mini/templates.py (Satzmuster DE/EN), mini/data_<app>.json (Lerndaten der App)."""
import json, re, random, unicodedata, base64, sys, math, pathlib
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.linear_model import LogisticRegression
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from templates import T, FILLERS_DE, FILLERS_EN, GRAMMAR, OFFTOPIC, LANGNAMES, PRE, POST, CONCEPTS
CON = {w: k for k, ws in CONCEPTS.items() for w in ws}

H = 2048
D = pathlib.Path(__file__).parent

def norm(s):
    s = s.lower().replace("ß", "ss")
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def fnv(s):
    h = 2166136261
    for ch in s:
        h ^= ord(ch)
        h = (h * 16777619) & 0xFFFFFFFF
    return h

def feats(text):
    toks = norm(text).split()
    f = {}
    def add(k):
        i = fnv(k) % H
        f[i] = f.get(i, 0) + 1
    for t in toks:
        add("w:" + t)
        if t in CON: add("k:" + CON[t])
        w = "<" + t + ">"
        for n in (2, 3, 4):
            for i in range(len(w) - n + 1):
                add("c:" + w[i:i + n])
    for a, b in zip(toks, toks[1:]):
        add("b:" + a + "_" + b)
    return f

def vec(rows):
    data, ind, ptr = [], [], [0]
    for text in rows:
        f = feats(text)
        nrm = math.sqrt(sum((1 + math.log(v)) ** 2 for v in f.values())) or 1
        for i, v in f.items():
            ind.append(i); data.append((1 + math.log(v)) / nrm)
        ptr.append(len(ind))
    return csr_matrix((data, ind, ptr), shape=(len(rows), H))

# ---------- Rauschen: Tippfehler, fehlende Umlaute, Füllwörter, Wortauslassung ----------
NEIGH = {c: n for c, n in zip("qwertzuiopasdfghjklyxcvbnm", ["w", "qe", "wr", "et", "rz", "tu", "zi", "uo", "ip", "o", "sq", "adw", "sfe", "dgr", "fht", "gjz", "hku", "jli", "kzo", "lpi", "xs", "yc", "xv", "cb", "vn", "bm"])}
def typo(w, rng):
    if len(w) < 4: return w
    k = rng.random()
    i = rng.randrange(1, len(w) - 1)
    if k < .25: return w[:i] + w[i + 1] + w[i] + w[i + 2:] if i + 2 <= len(w) else w
    if k < .5: return w[:i] + w[i + 1:]
    if k < .65: return w[:i] + w[i] + w[i:]
    if k < .85 and w[i] in NEIGH: return w[:i] + rng.choice(NEIGH[w[i]]) + w[i + 1:]
    return w[:i] + w[i + 1:]

def noisy(text, rng, fillers, strength=1.0, keep=()):
    ws = text.split()
    out = []
    for w in ws:
        if w in keep or rng.random() > .75 * strength + .25:
            out.append(w); continue
        r = rng.random()
        if r < .55 * strength: out.append(typo(w, rng))
        elif r < .8: out.append(w)
        else: out.append(w)
    ws = out
    if len(ws) > 3 and rng.random() < .2 * strength:
        del ws[rng.randrange(len(ws))]
    if len(ws) > 2 and rng.random() < .15 * strength:
        i = rng.randrange(len(ws) - 1); ws[i], ws[i + 1] = ws[i + 1], ws[i]
    s = " ".join(ws)
    if rng.random() < .35: s = rng.choice(fillers) + " " + s
    if rng.random() < .2: s = s + " " + rng.choice(fillers)
    if rng.random() < .5: s = s.lower()
    if rng.random() < .5: s = s.replace("?", "").replace("!", "").replace(".", "")
    if rng.random() < .3: s = s.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    return s

def clean_gloss(g):
    g = re.sub(r"\(.*?\)", "", g)
    g = g.split("/")[0].split(";")[0].split(",")[0].strip()
    return g

def build_dataset(app, templates_by_intent, rng, per_intent, target_n, off_n):
    data = json.load(open(D / f"data_{app}.json", encoding="utf-8"))
    targets = [v[0] for v in data["vocab"]] + [v[0] for v in data["sent"]] + [v[0] for v in data["lines"]]
    glosses = [clean_gloss(v[1]) for v in data["vocab"]] + [clean_gloss(v[1]) for v in data["sent"][:200]]
    tnorm = set(norm(t) for t in targets)
    words = [w for w in targets if len(w.split()) <= 3] + glosses
    native = "de" if app in ("id", "en") else "en"
    lang_t = LANGNAMES[app]
    X, Y = [], []
    for intent, tmpls in templates_by_intent.items():
        for _ in range(per_intent):
            lang = native if rng.random() < .8 else ("en" if native == "de" else "de")
            tl = tmpls.get(lang) or tmpls.get("en") or []
            if not tl: continue
            tpl = rng.choice(tl)
            w = rng.choice(words)
            n = rng.choice(glosses)
            g = rng.choice(GRAMMAR[lang])
            L = rng.choice(lang_t[lang])
            if intent not in ("target", "unknown") and rng.random() < .45:
                tpl = rng.choice(PRE[lang]) + " " + tpl
            if intent not in ("target", "unknown") and rng.random() < .25:
                tpl = tpl + " " + rng.choice(POST[lang])
            s = tpl.replace("{w}", w).replace("{n}", n).replace("{g}", g).replace("{l}", L)
            s = noisy(s, rng, FILLERS_DE if lang == "de" else FILLERS_EN, strength=rng.choice([0, .5, 1, 1]))
            if norm(s) in tnorm: continue   # Kollision mit Zielsprache vermeiden
            X.append(s); Y.append(intent)
    for _ in range(target_n):
        t = rng.choice(targets)
        X.append(noisy(t, rng, [""], strength=rng.choice([0, .5, 1]))); Y.append("target")
    for _ in range(off_n):
        lang = native if rng.random() < .8 else ("en" if native == "de" else "de")
        s = rng.choice(OFFTOPIC[lang])
        s = noisy(s, rng, FILLERS_DE if lang == "de" else FILLERS_EN, strength=rng.choice([0, .5, 1]))
        if norm(s) in tnorm: continue
        X.append(s); Y.append("unknown")
    # Zufallsrauschen
    for _ in range(off_n // 4):
        X.append("".join(rng.choice("abcdefghijklmnopqrstuvwxyz ") for _ in range(rng.randrange(4, 22)))); Y.append("unknown")
    return X, Y, native

def split_templates(rng, frac=.25):
    train, test = {}, {}
    for intent, d in T.items():
        train[intent], test[intent] = {}, {}
        for lang, lst in d.items():
            lst = lst[:]; rng.shuffle(lst)
            k = max(1, int(len(lst) * frac))
            test[intent][lang] = lst[:k]; train[intent][lang] = lst[k:] or lst
    return train, test

def export(app, clf, classes):
    W = clf.coef_.astype(np.float32)          # C x H
    b = clf.intercept_.astype(np.float32)
    scale = float(np.abs(W).max() / 127.0)
    q = np.clip(np.round(W / scale), -127, 127).astype(np.int8)
    trig = set()
    for intent, d in T.items():
        if intent in ("target", "unknown"): continue
        for lang, lst in d.items():
            for tpl in lst:
                for tok in norm(tpl.replace("{w}", " ").replace("{n}", " ").replace("{g}", " ").replace("{l}", " ")).split(): trig.add(tok)
    trig.update(CON.keys())
    for lst in (FILLERS_DE, FILLERS_EN, PRE["de"], PRE["en"], POST["de"], POST["en"]):
        for f in lst:
            for tok in norm(f).split(): trig.add(tok)
    model = {"H": H, "classes": list(classes), "scale": scale, "b": [round(float(x), 3) for x in b],
             "W": base64.b64encode(q.tobytes()).decode(), "trig": sorted(trig), "con": CON}
    js = "/* Automatisch erzeugt von mini/train.py – nicht von Hand ändern */\nconst MINI_MODEL=" + json.dumps(model, ensure_ascii=False, separators=(",", ":")) + ";\n"
    (D.parent / f"mini_model_{app}.js").write_text(js, encoding="utf-8")
    return len(js)

def run(app):
    rng = random.Random(7)
    tr_t, te_t = split_templates(random.Random(3))
    Xtr, Ytr, _ = build_dataset(app, tr_t, rng, 700, 2500, 900)
    Xte, Yte, _ = build_dataset(app, te_t, random.Random(99), 150, 500, 200)
    clf = LogisticRegression(max_iter=400, C=8.0)
    clf.fit(vec(Xtr), Ytr)
    pred = clf.predict(vec(Xte))
    acc = float(np.mean(pred == np.array(Yte)))
    # Konfidenz-Schwelle 0.5
    proba = clf.predict_proba(vec(Xte)); conf = proba.max(1)
    print(f"[{app}] Testgenauigkeit (unbekannte Satzmuster + anderes Rauschen): {acc*100:.1f}% auf {len(Xte)} Beispielen")
    per = {}
    for p, y in zip(pred, Yte): per.setdefault(y, []).append(p == y)
    print("   pro Absicht:", {k: round(100 * sum(v) / len(v)) for k, v in sorted(per.items())})
    # endgültiges Modell auf allen Mustern
    Xall, Yall, _ = build_dataset(app, T, random.Random(11), 900, 3000, 1100)
    clf2 = LogisticRegression(max_iter=500, C=8.0)
    clf2.fit(vec(Xall), Yall)
    ht = json.load(open(D / "handtest.json", encoding="utf-8"))
    bad = []; tot = 0; ok = 0
    for lang in ("de", "en"):
        rows = ht[lang]
        P = clf2.predict(vec([r[0] for r in rows]))
        for r, p in zip(rows, P):
            tot += 1
            if p == r[1]: ok += 1
            else: bad.append((lang, r[0], r[1], p))
    print(f"   Handgeschriebene, frei formulierte Testfragen: {ok}/{tot} = {100*ok/tot:.0f}%")
    for b in bad[:14]: print("     ✗", b)
    h2 = json.load(open(D / "handtest2.json", encoding="utf-8"))
    nat = "de" if app in ("id", "en") else "en"
    rows = h2[nat]; P = clf2.predict(vec([r[0] for r in rows])); pr = clf2.predict_proba(vec([r[0] for r in rows])).max(1)
    ok = sum(p == r[1] for p, r in zip(P, rows))
    ok7 = sum(p == r[1] for p, r, c in zip(P, rows, pr) if c >= .5)
    print(f"   NEUE, ungesehene Testfragen ({nat}): {ok}/{len(rows)} = {100*ok/len(rows):.0f}%")
    for p, r, c in zip(P, rows, pr):
        if p != r[1]: print(f"     ✗ {r[0]!r} -> {p} (soll {r[1]}, conf {c:.2f})")
    size = export(app, clf2, clf2.classes_)
    print(f"   exportiert: mini_model_{app}.js ({size//1024} KB), Beispiele gesamt: {len(Xall)}")
    # Trainingsdaten zum Nachlesen
    with open(D / f"train_{app}.jsonl", "w", encoding="utf-8") as f:
        for x, y in list(zip(Xall, Yall))[:4000]: f.write(json.dumps({"text": x, "intent": y}, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    apps = ["id", "en", "de"] if len(sys.argv) < 2 or sys.argv[1] == "all" else [sys.argv[1]]
    for a in apps: run(a)
