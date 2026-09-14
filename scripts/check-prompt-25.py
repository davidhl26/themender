#!/usr/bin/env python3
"""Liste de controle des prompts Seedance 2.5 (dossier prompt-video-2.0).

Verifie, pour chaque fichier passe en argument, le bloc entre triples backticks :
  1. guillemets droits : uniquement autour du dialogue (chaque phrase 2 fois : DIALOGUE + STAGE)
  2. aucun guillemet typographique
  3. non-ASCII : seul le tiret cadratin est tolere
  4. zero mot d'age
  5. les sections dans l'ordre de la video 1
  6. les regles qui ont repare la video 1 (langue, guillemets, vie continue, overlap...)
  7. timings : codes temps croissants, HARD CUT declare si >1 framing
  8. pas d'instruction de gel ("WITHOUT MOVING", "NOTHING MOVES" sur un corps, ...)
Sortie : OK ou la liste des manques. Code retour 1 si un manque.
"""
import re, sys, unicodedata

ORDRE = ['MATERIALS', 'ROLES', 'DIALOGUE', 'STYLE', 'AUDIO DESIGN', 'CHARACTERS',
         'SCREEN DIRECTION', 'LIGHT', 'STAGE 1', 'ENDING FRAME', 'AVOID']
REGLES = {
    'langue declaree': 'THE SPOKEN LANGUAGE IS ENGLISH THROUGHOUT',
    'regle des guillemets': 'QUOTATION MARKS IN THIS PROMPT APPEAR ONLY',
    'vie continue': 'EVER STILL, NOT FOR ONE FRAME',
    'settle': 'Movements SETTLE',
    'reaction sur l evenement': 'LANDS ON THE',
    'overlap': 'OVERLAP',
    'expo sur la peau': 'EXPOSURE IS SET ON THE SKIN',
    'pas de silhouette': 'SILHOUETTE',
    'pas de decor colle': 'no border, no backdrop',
}
AGE = ['girl', 'boy', 'child', 'children', 'kid', 'kids', 'year-old', 'years old', 'teen',
       'teenager', 'toddler', 'baby', 'infant', 'minor', 'schoolgirl', 'schoolboy', 'pupil']
GEL = [r'WITHOUT MOVING', r'NOTHING MOVES for', r'NOBODY MOVES(?! TOWARD)', r'DOES NOT MOVE',
       r'perfectly still', r'completely still', r'motionless(?! body| BODY)', r'stands frozen', r'freezes']

def check(path):
    t = open(path, encoding='utf-8').read()
    parts = t.split('```')
    if len(parts) < 3:
        return ['pas de bloc ``` trouve']
    b = parts[1]
    pb = []
    # 1. guillemets
    q = re.findall(r'"([^"]*)"', b)
    from collections import Counter
    c = Counter(q)
    for s, n in c.items():
        if n != 2:
            pb.append(f'guillemet x{n} (attendu 2 = DIALOGUE + STAGE) : "{s}"')
        if len(s.split()) == 1 and not s.endswith(('.', '?', '!')):
            pb.append(f'mot seul entre guillemets (indication de jeu ?) : "{s}"')
    no_dialogue = 'THERE IS NONE' in b or 'NOBODY SPEAKS IN THIS ENTIRE' in b
    if no_dialogue and q:
        pb.append(f'prompt muet mais {len(q)} guillemets')
    # 2. guillemets typographiques
    for ch in '“”«»‘’':
        if ch in b:
            pb.append(f'guillemet typographique {ch!r} x{b.count(ch)}')
    # 3. non-ascii
    # tolere : tiret cadratin, et les diacritiques des noms propres du dialogue (Mòyīrén)
    bad = sorted({ch for ch in b if ord(ch) > 127 and ch not in '—òīé'})
    for ch in bad:
        pb.append(f'non-ASCII {ch!r} U+{ord(ch):04X} {unicodedata.name(ch, "?")} x{b.count(ch)}')
    # 4. age
    for w in AGE:
        n = len(re.findall(r'\b' + re.escape(w) + r'\b', b, re.I))
        if n:
            pb.append(f'mot d age "{w}" x{n}')
    # 5. ordre des sections
    pos = []
    for s in ORDRE:
        m = re.search(r'(?m)^' + re.escape(s) + r'\b', b)
        if not m:
            pb.append(f'section absente : {s}')
        else:
            pos.append((m.start(), s))
    if [s for _, s in sorted(pos)] != [s for _, s in pos]:
        pb.append('sections dans le desordre : ' + ' > '.join(s for _, s in sorted(pos)))
    # 6. regles (un prompt muet declare l'absence de guillemets et de langue autrement)
    muet = 'DIALOGUE — THERE IS NONE' in b
    for k, v in REGLES.items():
        if muet and k in ('langue declaree', 'regle des guillemets'):
            continue
        if v not in b:
            pb.append(f'regle absente : {k} ({v})')
    if muet:
        if 'NOBODY SPEAKS' not in b:
            pb.append('prompt muet sans NOBODY SPEAKS')
        if 'NO QUOTATION MARK' not in b:
            pb.append('prompt muet sans la declaration NO QUOTATION MARK')
    # 7. timings
    codes = re.findall(r'\((\d):(\d\d(?:,\d)?)-(\d):(\d\d(?:,\d)?)\)', b)
    prev = -1
    for a, bb, cc, dd in codes:
        s0 = int(a) * 60 + float(bb.replace(',', '.')); s1 = int(cc) * 60 + float(dd.replace(',', '.'))
        if s0 != prev and prev != -1:
            pb.append(f'trou ou chevauchement de STAGE a {a}:{bb} (precedent finit a {prev} s)')
        if s1 <= s0:
            pb.append(f'STAGE a l envers ({a}:{bb}-{cc}:{dd})')
        prev = s1
    if prev > 30 * 1 and prev != -1 and prev > 30:
        pb.append(f'duree {prev} s > 30 s')
    nfr = len(re.findall(r'FRAMING [A-Z] \[', b))
    ncut = len(re.findall(r'HARD CUT AT', b))
    if nfr > 1 and ncut != nfr - 1:
        pb.append(f'{nfr} framings mais {ncut} HARD CUT declares')
    if nfr <= 1 and 'THERE IS NO EDITING' not in b and 'one single unbroken take' not in b:
        pb.append('une seule prise mais la grammaire de montage n est pas declaree (THERE IS NO EDITING / one single unbroken take)')
    # 8. gel : hors AVOID, hors negation ("not one of them is", "nobody is", "never")
    corps = b.split('\nAVOID')[0]
    for g in GEL:
        for m in re.finditer(g, corps):
            avant = corps[max(0, m.start() - 60):m.start()].lower()
            if re.search(r'(not one of them is|nobody is|never|no one is|none of them is|is not|are not)\s*$', avant):
                continue
            pb.append(f'instruction de gel : ...{corps[max(0, m.start() - 40):m.end() + 40].strip()}...')
    return pb

rc = 0
for p in sys.argv[1:]:
    pb = check(p)
    t = open(p, encoding='utf-8').read()
    b = t.split('```')[1] if '```' in t else ''
    print(f'{p}  ({len(b.split())} mots, {len(b)} car.)')
    if pb:
        rc = 1
        for x in pb:
            print('   -', x)
    else:
        print('   OK')
sys.exit(rc)
