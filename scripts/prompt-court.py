#!/usr/bin/env python3
"""Tire de chaque bloc long un prompt court de ~300 mots, dans l'ordre documente.

Pourquoi : Higgsfield recommande 150-300 mots ; au-dela de ~280 le modele lache des
instructions, et l'attention se dilue (debut et fin pesent, le milieu est enterre).
Nos blocs font 5 200 mots de mediane. Le bloc long reste le DOCUMENT DE REFERENCE
(geometrie GEO, raccords, verrous) ; c'est cette version courte qu'on colle.

Ordre des sections, celui que donnent les sources :
  SHOT · CONTINUITY · OPENING FRAME · ACTION · PERFORMANCE · CAMERA · LIGHT · SOUND
  · ENDING FRAME · CONSTRAINTS
"""
import re, glob, os, textwrap

def sect(b, start, stop=r'\n\n'):
    """Les sections du bloc long sont separees par une ligne vide : c'est la seule
    borne fiable (un intertitre en capitales peut ouvrir le corps d'une section)."""
    m = re.search(start + r'.*?(?=' + stop + r')', b, re.S)
    return re.sub(r'\s+', ' ', m.group(0)).strip() if m else ''

def phrases(txt, n):
    """Les n premieres phrases, sans couper au milieu d'une decimale ([0.0s])."""
    out, cur = [], ''
    for part in re.split(r'(?<=[.!?])\s+(?=[A-Z@\[])', txt):
        cur = part
        out.append(cur)
        if len(out) >= n: break
    return ' '.join(out)

def clip(txt, mots):
    w = txt.split()
    return ' '.join(w[:mots]) + ('…' if len(w) > mots else '')

def court(b, nom):
    L = []
    scene = sect(b, r'SCENE CONTEXT\n')
    L.append('SHOT — ' + clip(phrases(scene.replace('SCENE CONTEXT', '').strip(), 1), 26))

    m = re.search(r'^CONTINUITY REFERENCE[^\n]*\n(.*?)(?=\n\n)', b, re.S | re.M)
    cont = re.sub(r'\s+', ' ', m.group(1)).strip() if m else ''
    prev = re.search(r'precedes this one \(([^)]+)\)|same continuous shot \(([^)]+)\)|same film \(([^)]+)\)', cont)
    prev = next((g for g in prev.groups() if g), '') if prev else ''
    if 'live-action footage that opens the film' in cont:
        L.append('CONTINUITY — VIDEO 1 is the live-action footage that opens the film, shot on a real camera. '
                 'TAKE from it the light level, the grain, the colour of the room and the state the scene is in, and '
                 'match them. DO NOT TAKE its frames or its framing: the framing is the one written below.')
    elif 'No video is attached' in cont:
        L.append('CONTINUITY — no video attached. This is the head of its chain: it sets the light, grain and skin '
                 'rendering the following shots match. THE ATTACHED IMAGE IS THE FIRST FRAME — it fixes the opening '
                 'composition, every body position and pose, every prop state and the camera direction; take nothing '
                 'else from it, no border, no backdrop, no empty-room staging.')
    elif 'IN A DIFFERENT PLACE' in cont:
        L.append('CONTINUITY — VIDEO 1 is an earlier shot of the same film (%s), IN A DIFFERENT PLACE: rendering '
                 'reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight '
                 'roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.' % prev)
    elif 'CAMERA IS ALREADY MOVING' in cont:
        L.append('CONTINUITY — VIDEO 1 is the previous segment of this same continuous shot (%s) and THE CAMERA IS '
                 'ALREADY MOVING at its last frame. ALIGN THE BOUNDARY FIRST: start on that motion already underway, '
                 'same speed, same line, no ease-in, no restart, then carry it on. One single move across both clips.' % prev)
    elif cont and prev:
        L.append('CONTINUITY — VIDEO 1 is the shot immediately before this one (%s). ITS LAST FRAME IS THIS '
                 'GENERATION\'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the inherited '
                 'state below, already true, nothing replayed, then move on. It must CONNECT NATURALLY, NOT '
                 'IDENTICALLY. TAKE its light, grain, skin rendering and camera behaviour. DO NOT TAKE its framing.' % prev)
    inh = sect(b, r'HANDOFF — THE EXACT STATE THIS SHOT INHERITS')
    hand = re.search(r'WHERE THIS SHOT LEAVES EACH BODY.*', inh) if inh else None
    if hand:
        pos = hand.group(0).split('other bodies: ')[-1]
        L.append('INHERITED STATE, ALREADY TRUE AT FRAME ONE — ' + clip(pos, 26))

    anc = re.search(r'\|\s*\*\*`start_image`\*\*\s*\|([^\n|]*)', b)
    if anc and 'aucun' not in anc.group(1).lower():
        L.append("ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position "
                 "and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else "
                 "from it: no border, no backdrop, no empty-room staging, no reference layout.")
    ff = sect(b, r'FIRST FRAME AND SPATIAL BLOCKING')
    L.append('OPENING FRAME — ' + clip(ff.replace('FIRST FRAME AND SPATIAL BLOCKING', '')
             .replace('The generation opens on this exact frame:', '').strip(), 28))

    fm = re.search(r'FRAME MAP & CHOREOGRAPHY[^\n]*\n(.*?)(?=\nSUBJECT LOCK|\nCROSS-FRAME|\nLAST FRAME)', b, re.S)
    if fm:
        segs = re.findall(r'^\[([\d.]+)[^\]]*\]\s*([^\n]+)', fm.group(1), re.M)
        if segs:
            # La doc recommande 3-4 ETAPES, chacune avec UN changement d'etat et une fin
            # explicite — pas douze micro-segments, que le modele lit comme une liste.
            fin = float(segs[-1][0]) or 1.0
            beats, n = [], 3 if len(segs) <= 6 else 4
            for i in range(n):
                lo, hi = fin * i / n, fin * (i + 1) / n
                pris = [s for s in segs if lo <= float(s[0]) < hi] or ([segs[i]] if i < len(segs) else [])
                if not pris: continue
                # dans l'etape, la phrase qui porte le changement d'etat (ecrite en capitales)
                def poids(s):
                    caps = len(re.findall(r'\b[A-Z]{3,}\b', s[1]))
                    return caps * 12 + min(len(s[1]), 260) / 10
                pris = sorted(pris, key=poids, reverse=True)[:2]
                pris.sort(key=lambda s: float(s[0]))
                tetes = [re.split(r'(?<=[.;])\s', s[1])[0] for s in pris]
                tetes = [x for x in tetes if len(x.split()) > 3] or tetes[:1]
                beats.append("[%.1f-%.1fs] %s" % (lo, hi, clip(' '.join(tetes), 24)))
            L.append('ACTION in ' + str(len(beats)) + ' stages, timings are budgets not edit points, '
                     'each stage ends on the state the next one starts from — ' + ' '.join(beats))
    perf = sect(b, r'CHARACTER PERFORMANCE\n')
    L.append('PERFORMANCE — ' + clip(phrases(perf.replace('CHARACTER PERFORMANCE', '').strip(), 2), 22))

    cam = sect(b, r'\nCAMERA\n') or sect(b, r'OPTICS\n')
    L.append('CAMERA — ' + clip(cam.replace('CAMERA', '').replace('OPTICS', '').strip(), 16))

    lig = sect(b, r'\nLIGHT ')
    L.append('LIGHT — ' + clip(phrases(re.sub(r'^LIGHT[\s\W]*', '', lig), 1), 18))

    dia = re.search(r'^DIALOGUE ([^\n]+)', b, re.M)
    aud = sect(b, r'\nAUDIO\n')
    son = (dia.group(1) if dia else '') + ' ' + clip(phrases(aud.replace('AUDIO', '').strip(), 1), 25)
    L.append('SOUND — ' + clip(son.strip(), 28))

    emis = sect(b, r'LAST FRAME — THE EXACT STATE THIS SHOT HANDS OVER')
    lf = re.search(r'WHAT IS IN THE FRAME AT THE LAST INSTANT: (.*?)(?= WHERE THIS SHOT LEAVES|$)', emis) if emis else None
    if lf: L.append('ENDING FRAME, the state this shot hands over — ' + clip(lf.group(1), 26))

    av = sect(b, r'\nAVOID\n')
    items = [x.strip() for x in re.sub(r'^AVOID\s*', '', av).split(',') if x.strip()][:10]
    L.append('AVOID — ' + ', '.join(items) + '.')
    return '\n'.join(L)

d = 'docs/generations/videos'
tot, tailles = 0, []
for f in sorted(glob.glob(os.path.join(d, 'PRET-SEQ-*.md'))):
    seq = re.search(r'SEQ-(\d\d)', f).group(1)
    out = [f"# PROMPTS COURTS — SÉQUENCE {seq}", '',
           "> ~300 mots par plan, l'ordre recommandé par Higgsfield et ByteDance.",
           f"> Le détail complet reste dans `PRET-SEQ-{seq}.md` : géométrie GEO, verrous, raccords numérotés.",
           "> **C'est CETTE version qu'on colle dans Higgsfield.** L'autre est le document de tournage.", '']
    for b in re.split(r'\n(?=#{2,3} VIDÉO )', open(f, encoding='utf-8').read()):
        m = re.match(r'#{2,3} VIDÉO (\S+) —([^\n]*)', b)
        if not m: continue
        c = court(b, m.group(1)); tot += 1; tailles.append(len(c.split()))
        reg = re.search(r'\*\*RÉGLAGES[^\n]*\n\n(\|.*?)(?=\n\n)', b, re.S)
        out += [f"## {m.group(1)} —{m.group(2)}", '']
        if reg:
            out += ['**RÉGLAGES — à saisir dans l\'interface AVANT de coller le texte**', '', reg.group(1), '',
                    "> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en "
                    "référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.", '']
        out += ["> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.", '',
                '```', c, '```', '']
    open(os.path.join(d, f'PROMPT-COURT-SEQ-{seq}.md'), 'w', encoding='utf-8').write('\n'.join(out))
tailles.sort()
print(tot, "prompts · mots : min", tailles[0], "· médiane", tailles[len(tailles)//2], "· max", tailles[-1])
