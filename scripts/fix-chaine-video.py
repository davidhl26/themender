# -*- coding: utf-8 -*-
"""David, 02/09 : \"j'insere la derniere video dans Seedance 2.0, il y a pas de suivi,
c'est pas le meme mouvement de camera, pas de suivi de sequence\".

Trois causes dans MES fichiers (la quatrieme est cote interface) :

1. \"@Video 1\" etait AVALE par l'editeur Higgsfield, qui le parse comme une
   mention d'Element -- exactement comme il a transforme @sambefore en
   @[sambefore](06ed4385...). Dans le prompt colle par David, la ligne commence
   par un deux-points orphelin : le modele ne sait meme plus qu'une video est
   attachee. Plus aucun \"@\" devant : \"THE VIDEO ATTACHED TO THIS GENERATION\".

2. Le bloc INTERDISAIT la continuite qu'on lui demande : \"Do NOT reuse, copy or
   extend any of its frames [...] the framing owes nothing to the previous
   shot's composition\". Pour un plan qui suit dans le MEME lieu, c'est le
   contraire qu'il faut : reprendre la ou l'autre s'arrete, meme comportement de
   camera, meme vitesse. La consigne \"tout reconstruire\" reste pour les plans
   qui changent de lieu, ou elle est juste.

3. \"Each framing is held completely still between its cuts\" contredisait le
   registre ALIVE (camera portee qui respire et suit) dans 3 blocs.
"""
import re, pathlib
D = pathlib.Path('/home/user/site-web-callbot.ai/docs/generations/videos')

# ── 1+2 · les quatre variantes de chaine, reecrites ──────────────────────────
SAME = ("CONTINUITY REFERENCE — THIS SHOT CONTINUES THE ATTACHED VIDEO\n"
"THE VIDEO ATTACHED TO THIS GENERATION is the shot that immediately precedes this one ({p}), in the same "
"place and the same minute. THIS GENERATION IS ITS DIRECT CONTINUATION and must feel like the same take "
"filmed by the same operator seconds later: carry over its exact light level and direction, its grain, its "
"skin rendering, the state the bodies and the props are left in, AND ABOVE ALL THE WAY ITS CAMERA BEHAVES — "
"the same height, the same kind of movement, the same speed, the same breathing weight in the frame. Pick the "
"scene up exactly where the attached video leaves it. Do not restart it, do not reset the room, do not relight "
"it, do not change operator. The new framing is the one the FRAME MAP gives below, but it is reached by the "
"same camera, moving the same way.")

MOVE = ("CONTINUITY REFERENCE — THIS SHOT CONTINUES THE ATTACHED VIDEO, MID-MOVEMENT\n"
"THE VIDEO ATTACHED TO THIS GENERATION is the previous segment of this same continuous shot ({p}). THIS "
"GENERATION IS ITS DIRECT CONTINUATION: the camera is already moving when this clip begins and it does not "
"stop, restart, ease in or change speed. Read from the attached video the camera's exact speed, direction and "
"height at the moment it hands over, and carry the move on at that same constant speed, on the same line, with "
"no ease-in and no ease-out. Carry over its light level, its grain and its skin rendering unchanged. The join "
"must be invisible: one single move across the two clips.")

DIFF = ("CONTINUITY REFERENCE — SAME FILM, DIFFERENT PLACE\n"
"THE VIDEO ATTACHED TO THIS GENERATION is an earlier shot from the same film ({p}), in a different place. Use "
"it ONLY to match the physical rendering — the film stock, the grain structure, the way skin and fabric "
"resolve, the focus behaviour, the highlight roll-off. Do NOT take its light, its palette, its exposure level "
"or its composition: this shot's light comes from its own LOCATION and LIGHT paragraphs below, and its framing "
"from its own FRAME MAP. Everything else is built new, at full quality.")

HEAD = ("CONTINUITY REFERENCE — NO VIDEO IS ATTACHED\n"
"No previous clip is attached to this generation. This is the first shot of its chain: it sets the light, the "
"grain and the skin rendering that every following shot will be matched to. Build every frame new from the "
"references below, at full quality.")

OPEN = ("CONTINUITY REFERENCE — THE FILM'S OPENING FOOTAGE IS ATTACHED\n"
"THE VIDEO ATTACHED TO THIS GENERATION is the live-action footage that opens the film, shot on a real camera. "
"Use it to read the light level, the grain, the colour of the room and the state the scene is in, and match "
"them. Do NOT reuse or extend its frames: the framing comes from the FRAME MAP below.")

n = {'same':0,'move':0,'diff':0,'head':0,'open':0,'still':0}
for p in sorted(D.glob('PRET-SEQ-*.md')):
    s = p.read_text(encoding='utf-8')
    parts = re.split(r'(?m)^(#{2,3} VIDÉO .*)$', s)
    out = [parts[0]]
    for i in range(1, len(parts), 2):
        title, body = parts[i], parts[i+1]
        f = re.search(r'```\n(.*?)\n```', body, re.S)
        if not f: out.append(title + body); continue
        blk = f.group(1)
        prev = re.search(r'precedes this one \(([^)]+)\)|same continuous shot \(([^)]+)\)|same film \(([^)]+)\)', blk)
        pv = next((g for g in prev.groups() if g), '?') if prev else '?'
        old = re.search(r'(?s)^CONTINUITY REFERENCE\n.*?(?=\n\n)', blk, re.M)
        if old:
            t = old.group(0)
            if 'previous segment of this same continuous shot' in t:
                blk = blk.replace(t, MOVE.format(p=pv)); n['move'] += 1
            elif 'in the same place and the same minute' in t:
                blk = blk.replace(t, SAME.format(p=pv)); n['same'] += 1
            elif 'in a different place' in t:
                blk = blk.replace(t, DIFF.format(p=pv)); n['diff'] += 1
            elif 'live-action footage that opens the film' in t:
                blk = blk.replace(t, OPEN); n['open'] += 1
            elif 'No previous shot is attached' in t:
                blk = blk.replace(t, HEAD); n['head'] += 1
        # 3 · une camera portee ne tient pas un cadre "completement immobile"
        if 'REGISTER — ALIVE' in blk and 'held completely still between its cuts' in blk:
            blk = blk.replace('Each framing is held completely still between its cuts.',
                              'Each framing is held on the operator\'s own weight between its cuts — breathing, drifting a centimetre and correcting — never nailed down and never drifting into a new composition.')
            n['still'] += 1
        out.append(title + "\n\n```\n" + blk + "\n```\n" + body[f.end():])
    p.write_text("".join(out), encoding='utf-8')

print(f"chaine MEME LIEU (continuation reelle) : {n['same']}")
print(f"chaine MEME MOUVEMENT (segments)       : {n['move']}")
print(f"chaine AUTRE LIEU (pellicule seule)    : {n['diff']}")
print(f"tetes de chaine                        : {n['head']}")
print(f"ouverture du film                      : {n['open']}")
print(f"'held completely still' vs ALIVE       : {n['still']}")
