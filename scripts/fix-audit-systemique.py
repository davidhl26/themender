# -*- coding: utf-8 -*-
"""Corrige les 3 defauts SYSTEMIQUES remontes par l'audit du 02/09.

A · 32 blocs a coupe franche portaient encore "One continuous uncut take ... No added cut"
    en derniere ligne : deux ordres opposes dans le meme prompt.
C · 62 blocs : "Every stroke of handwriting anywhere in frame is a" + la carte ecriture,
    collee au milieu de la phrase. Predicat disparu, consigne inanalysable. (Ma faute.)
D · 62 blocs : la carte anti-derive inseree au milieu de "CONTINUITY LOCK above and the
    POSITIVE CONSTRAINTS below apply in full." (Ma faute, ce tour-ci.)
"""
import re, pathlib

D = pathlib.Path('/home/user/site-web-callbot.ai/docs/generations/videos')
CARD = None
n_a = n_c = n_d = 0

for p in sorted(D.glob('PRET-SEQ-*.md')):
    s = p.read_text(encoding='utf-8')

    # ── D · la carte anti-derive doit sortir du milieu de la phrase ────────────
    m = re.search(r'CONTINUITY LOCK above and the (CONTINUITY — WHAT MUST NOT DRIFT\n.*?)(?=\nPOSITIVE CONSTRAINTS|\n\n)', s, re.S)
    if m and CARD is None:
        CARD = m.group(1).rstrip()
    before = s
    s = re.sub(r'CONTINUITY LOCK above and the CONTINUITY — WHAT MUST NOT DRIFT\n.*?\n(?=POSITIVE CONSTRAINTS)',
               'CONTINUITY LOCK above and the POSITIVE CONSTRAINTS below apply in full.\n\n' + CARD + '\n\n',
               s, flags=re.S)
    n_d += len(re.findall(r'CONTINUITY LOCK above and the POSITIVE CONSTRAINTS below apply in full\.', s)) if s != before else 0

    # ── C · rendre la phrase de l'ecriture grammaticale ───────────────────────
    n_c += s.count('anywhere in frame is a The writing is real handwriting')
    s = s.replace('anywhere in frame is a The writing is real handwriting',
                  'anywhere in frame is real handwriting')

    p.write_text(s, encoding='utf-8')

# ── A · la derniere ligne doit suivre le FORMAT MODE du bloc ──────────────────
UNCUT = 'One continuous uncut take at real-time speed, for the exact duration requested. No slow motion, no speed ramp, no added cut.'
CUT   = ('One continuous take at real-time speed for the exact duration requested, containing ONLY the '
         'framings and the hard cuts that FORMAT MODE declares above, at the moments the FRAME MAP gives '
         'and nowhere else. No dissolve, no fade, no montage, no extra cut. No slow motion, no speed ramp.')
RAMP  = ('One continuous take for the exact duration requested, containing ONLY the framings, the hard cuts '
         'and the speed change that FORMAT MODE declares above, at the moments the FRAME MAP gives and '
         'nowhere else. No dissolve, no fade, no montage, no extra cut, and no speed change anywhere the '
         'FRAME MAP does not call for one.')

for p in sorted(D.glob('PRET-SEQ-*.md')):
    s = p.read_text(encoding='utf-8')
    parts = re.split(r'(?m)^(#{2,3} VIDÉO .*)$', s)
    out = [parts[0]]
    for i in range(1, len(parts), 2):
        title, body = parts[i], parts[i+1]
        f = re.search(r'```\n(.*?)\n```', body, re.S)
        if not f:
            out.append(title + body); continue
        blk = f.group(1)
        if UNCUT in blk:
            has_cut  = 'HARD CUT' in blk
            has_ramp = bool(re.search(r'slow motion|speed ramp|ralenti', blk, re.I)) and re.search(r'FORMAT MODE[^\n]*(?:ramp|slow)', blk, re.I)
            if has_ramp:
                blk = blk.replace(UNCUT, RAMP); n_a += 1
            elif has_cut:
                blk = blk.replace(UNCUT, CUT); n_a += 1
        out.append(title + "\n\n```\n" + blk + "\n```\n" + body[f.end():])
    p.write_text("".join(out), encoding='utf-8')

print(f"A · {n_a} blocs a coupe franche : derniere ligne alignee sur le FORMAT MODE")
print(f"C · {n_c} phrases d'ecriture rendues grammaticales")
print(f"D · carte anti-derive sortie du milieu de la phrase, phrase restauree")
