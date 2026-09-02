# -*- coding: utf-8 -*-
"""Audit du 02/09 — les defauts de CONTENU determinables sans arbitrage de David."""
import re, pathlib
D = pathlib.Path('/home/user/site-web-callbot.ai/docs/generations/videos')
def blocks(p):
    s = p.read_text(encoding='utf-8')
    return re.split(r'(?m)^(#{2,3} VIDÉO .*)$', s)
def save(p, parts):
    p.write_text("".join(parts), encoding='utf-8')
log = []

# ── 1 · la carte ecriture ne doit pas reclamer un script la ou les traces sont
#        volontairement abstraites (savon sur le miroir, the sur le papier).
CARVE = {
 '2D': "The wet tea strokes on the paper in this shot are NOT handwriting and the handwriting rule above does not reach them: they stay exactly as the choreography describes them — dark wet abstract lines, no letters, no words, nothing readable, nothing that resolves into a character.",
 '8C': "The soap streaks on the mirror in this shot are NOT handwriting and the handwriting rule above does not reach them: they stay exactly as the choreography describes them — clear abstract bands in the fog, no letters, no words, nothing readable. The message is composited in post, never generated.",
 '8C-bis': "The soap streaks on the mirror in this shot are NOT handwriting and the handwriting rule above does not reach them: they stay exactly as the choreography describes them — clear abstract bands in the fog, no letters, no words, nothing readable. The message is composited in post, never generated.",
 '10I': "The soap marks on the mirror in this shot are NOT handwriting and the handwriting rule above does not reach them: they stay exactly as the choreography describes them — abstract marks only, no letters, no words, nothing readable. The message is composited in post, never generated.",
}
# ── 2 · substitutions plates, appliquees partout ───────────────────────────────
FLAT = [
 # la rambarde : le lieu genere est en BOIS PEINT, pas en fer (LIEU-09)
 ('@BackGallery: The back gallery at night under sodium, wet concrete, iron rail.',
  '@BackGallery: The back gallery at night under sodium — a painted wooden rail, grey over green over an older white, the paint flaking to bare silvered wood along the top; peeling deck boards with the grain raised and the nailheads standing proud and rusted.'),
]
n_carve = n_flat = 0
for p in sorted(D.glob('PRET-SEQ-*.md')):
    parts = blocks(p)
    for i in range(1, len(parts), 2):
        code = re.match(r'#{2,3} VIDÉO ([0-9A-Za-z-]+)', parts[i]).group(1)
        f = re.search(r'```\n(.*?)\n```', parts[i+1], re.S)
        if not f: continue
        blk = f.group(1)
        if code in CARVE and CARVE[code] not in blk:
            blk = re.sub(r'(Never random scribble, never a scrawl, never abstract mark-making, never decorative squiggles\.)',
                         r'\1 ' + CARVE[code], blk, count=1); n_carve += 1
        for a, b in FLAT:
            if a in blk: blk = blk.replace(a, b); n_flat += 1
        parts[i+1] = "\n\n```\n" + blk + "\n```\n" + parts[i+1][f.end():]
    save(p, parts)
log.append(f"carte ecriture · {n_carve} blocs recoivent une exception explicite (savon, the)")
log.append(f"rambarde       · {n_flat} fiches @BackGallery rendues au bois peint du lieu genere")

# ── 3 · cartes de chaine fausses : 4F et 10L sont dans le MEME lieu que leur ────
#        plan precedent, pas dans un autre.
CHAIN_SAME = ("CONTINUITY REFERENCE\n@Video 1: the shot that immediately precedes this one ({p}), in the same "
 "place and the same minute. Use it ONLY to read where the scene stands — the exact light level and direction, "
 "the grain, the skin rendering, the state the bodies and the props are left in, and the camera's speed. Do NOT "
 "reuse, copy or extend any of its frames: every frame here is built new from the references below, at full "
 "quality. The framing comes solely from the FRAME MAP below and owes nothing to the previous shot's composition.")
FIXCHAIN = {'4F': '4E', '10L': '10H'}
n_chain = 0
for p in sorted(D.glob('PRET-SEQ-*.md')):
    parts = blocks(p)
    for i in range(1, len(parts), 2):
        code = re.match(r'#{2,3} VIDÉO ([0-9A-Za-z-]+)', parts[i]).group(1)
        if code not in FIXCHAIN: continue
        f = re.search(r'```\n(.*?)\n```', parts[i+1], re.S)
        if not f: continue
        blk = f.group(1)
        if 'in a different place' in blk:
            blk = re.sub(r'(?s)CONTINUITY REFERENCE\n@Video 1: an earlier shot from the same film[^\n]*',
                         CHAIN_SAME.format(p=FIXCHAIN[code]), blk, count=1); n_chain += 1
        parts[i+1] = "\n\n```\n" + blk + "\n```\n" + parts[i+1][f.end():]
    save(p, parts)
log.append(f"chaine         · {n_chain} blocs (4F, 10L) passes en chaine COMPLETE : meme lieu que leur precedent")

# ── 4 · registre LOCKED contre un mouvement declare dans le bloc lui-meme ──────
#        9A (travelling derriere Nora) et 4C (retrait depuis les hachures).
MOVED = ("CAMERA REGISTER — LOCKED, WITH THE ONE MOVE THE FRAME MAP DECLARES\n"
 "The camera is placed and it stays, except for the single move the FRAME MAP names explicitly — that move is "
 "part of the shot and must happen exactly as written. Outside it, nobody is followed, nothing is reframed, and "
 "when a body leaves the frame the frame does not go after it. No second move, no reframe, no pan to find a "
 "face. This stillness is not neutrality and must never read as a surveillance camera: it is what the film lost "
 "when it lost her.")
n_reg = 0
for name, codes in [('PRET-SEQ-09.md', {'9A'}), ('PRET-SEQ-04.md', {'4C'})]:
    p = D/name; parts = blocks(p)
    for i in range(1, len(parts), 2):
        code = re.match(r'#{2,3} VIDÉO ([0-9A-Za-z-]+)', parts[i]).group(1)
        if code not in codes: continue
        f = re.search(r'```\n(.*?)\n```', parts[i+1], re.S)
        if not f: continue
        blk = f.group(1)
        if 'CAMERA REGISTER — LOCKED\n' in blk:
            blk = re.sub(r'(?s)CAMERA REGISTER — LOCKED\n.*?(?=\n\n)', MOVED, blk, count=1); n_reg += 1
        blk = blk.replace('visible camera rigs, camera movement, dolly, pan, zoom, handheld shake',
                          'visible camera rigs, any camera move the FRAME MAP does not declare, a whip pan, a zoom or crash zoom, handheld shake')
        parts[i+1] = "\n\n```\n" + blk + "\n```\n" + parts[i+1][f.end():]
    save(p, parts)
log.append(f"registre       · {n_reg} blocs (9A, 4C) autorisent le mouvement que leur FRAME MAP declare")

# ── 5 · focale contradictoire dans 8C-bis : le cadre est en 85, l'OPTICS disait 50 ─
p = D/'PRET-SEQ-08.md'; s = p.read_text(encoding='utf-8')
m = re.search(r'(#{2,3} VIDÉO 8C-bis[^\n]*\n\n```\n)(.*?)(\n```)', s, re.S)
if m:
    blk = re.sub(r'(?m)^(Anamorphic )50( mm)', r'\g<1>85\g<2>', m.group(2))
    s = s[:m.start(2)] + blk + s[m.end(2):]
    p.write_text(s, encoding='utf-8')
    log.append("focale         · 8C-bis : OPTICS passe de 50 a 85 mm, pour raccorder avec 8C")

for l in log: print(l)
