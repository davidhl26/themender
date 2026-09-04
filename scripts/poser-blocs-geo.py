# -*- coding: utf-8 -*-
"""Pose le bloc GEO et la direction d'ecran, VERBATIM, dans tous les plans de chaque scene.

Methode confirmee par la recherche du 04/09 (source : le bloc GEO SPATIAL LAYOUT) :
\"Ecrire un bloc GEO par SCENE, pas par plan -- et le coller VERBATIM, sans une seule
modification, dans 100 % des plans de cette scene.\"

Mesure qui a motive l'operation : la chambre de Nora etait decrite de SEPT facons
differentes dans ses sept plans, la cuisine de CINQ facons dans six plans. Le modele
recevait sept chambres et en fabriquait sept.

Le GEO est pose JUSTE AVANT la section LOCATION du bloc, avec une clause de preseance :
il fait autorite sur la geometrie, la section LOCATION garde le detail propre au plan.
"""
import json, re, pathlib

D = pathlib.Path('/home/user/site-web-callbot.ai/docs/generations/videos')
SC = json.load(open('/tmp/claude-0/-home-user-site-web-callbot-ai/e3b5435b-90c4-51b2-85de-7bf079329855/scratchpad/geo.json'))

PRE = ("THE GEO BLOCK BELOW IS THE CANONICAL GEOMETRY OF THIS PLACE. It is pasted word for word into every "
       "shot of this scene and it OVERRIDES any later description that contradicts it: where a landmark "
       "stands, which side of frame it holds, how far it is from another landmark, and where the light "
       "comes from are settled here and nowhere else. Later sections add what belongs to THIS shot only — "
       "props in their state, bodies, action — and may not move the room.\n\n")

par_plan = {}
for s in SC:
    bloc = PRE + s['geo'].strip() + "\n\n" + s['screen'].strip()
    for c in s['plans']:
        par_plan[c] = bloc

n = 0; sans_ancre = []
for p in sorted(D.glob('PRET-SEQ-*.md')):
    src = p.read_text(encoding='utf-8'); out = []; last = 0
    for m in re.finditer(r'(#{2,3} VIDÉO ([0-9A-Za-z-]+)[^\n]*\n.*?\n```\n)(.*?)(\n```)', src, re.S):
        code, blk = m.group(2), m.group(3)
        if code in par_plan and 'THE GEO BLOCK BELOW IS THE CANONICAL GEOMETRY' not in blk:
            g = par_plan[code]
            for anchor in ('\nLOCATION @', '\nLOCATION MAP', '\nFIRST FRAME AND SPATIAL BLOCKING'):
                if anchor in blk:
                    blk = blk.replace(anchor, '\n' + g + anchor, 1); n += 1; break
            else:
                sans_ancre.append(code)
        out.append(src[last:m.start(3)]); out.append(blk); last = m.end(3)
    out.append(src[last:]); p.write_text("".join(out), encoding='utf-8')

print(f"bloc GEO pose sur {n} plans")
if sans_ancre: print("ancre introuvable :", sans_ancre)
