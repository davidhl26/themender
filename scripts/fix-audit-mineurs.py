# -*- coding: utf-8 -*-
"""Audit du 02/09 — les 15 defauts MINEURS qui restaient reellement.
(13 des 28 signales etaient des doublons des systemiques, deja corriges.)
"""
import re, pathlib
D = pathlib.Path('/home/user/site-web-callbot.ai/docs/generations/videos')
log = []

def sub_all(pairs, glob='*SEQ-*.md', label=''):
    n = 0
    for p in sorted(D.glob(glob)):
        s = o = p.read_text(encoding='utf-8')
        for a, b in pairs:
            if a in s:
                n += s.count(a); s = s.replace(a, b)
        if s != o: p.write_text(s, encoding='utf-8')
    if label: log.append(f"{label} · {n}")
    return n

# 1 ─ le flottement residuel se contredisait entre les deux cartes camera :
#     LOCKED disait "well under one millimetre", CAMERA — OPERATED "a few millimetres".
sub_all([
 ('The only life left in the image is the residual weight of the head itself, well under one millimetre.',
  'The only life left in the image is the residual human weight the CAMERA paragraph below describes — the same drift of a few millimetres, never more, and never a reframe.'),
 ('The only life left in the image is the residual weight of the head itself, under one millimetre.',
  'The only life left in the image is the residual human weight the CAMERA paragraph below describes — the same drift of a few millimetres, never more, and never a reframe.'),
], label='flottement residuel reconcilie entre les deux cartes camera')

# 2 ─ 4B : le plat entre au cadre a [1.4s] dans les mains de Nora, pas a [3.2s].
#     Un objet qui apparait a [3.2s] est exactement la materialisation que le bloc interdit.
sub_all([('The white enamel casserole dish is NOT in the room at [0.0s]: it enters at [3.2s] in the girl\'s two hands',
          'The white enamel casserole dish is NOT in the room at [0.0s]: it enters at [1.4s] in the girl\'s two hands, carried in through the doorway, and is set down on the dresser at [3.2s]')],
        label='4B · le plat entre a [1.4s], pose a [3.2s]')

# 3 ─ un bloc colle seul n'a acces a aucune "previous generation" : il n'a que son Element.
sub_all([('the same one as the previous generations', 'the same one as its reference Element'),
         ('the same as the previous generations', 'the same as its reference Element')],
        label='renvoi aux "previous generations" remplace par l\'Element')

# 4 ─ "one stop" est une unite d'exposition, pas de cadrage (et le bloc l'emploie
#     deja dans son sens photographique).
sub_all([('one stop tighter than the main version', 'one size tighter than the main version')],
        label='6B-bis · "one stop" (exposition) devient "one size" (cadrage)')

# 5 ─ 8B : le palier est declare en parquet nu, le son y ajoutait une moquette.
sub_all([('The soft brush of the door on the carpet strip', 'The soft brush of the door edge over bare floorboards')],
        label='8B · la moquette du son disparait, le palier est en parquet nu')

# 6 ─ renvois morts : l'evenement est ecrit AU-DESSUS, pas en dessous.
sub_all([('the only walking in the block, written below', 'the only walking in the block, written in the FRAME MAP above'),
         ('the single scroll written below', 'the single scroll written in the FRAME MAP above'),
         ('written below', 'written in the FRAME MAP above')],
        label='renvois internes rediriges vers le FRAME MAP')

# 7 ─ 1D : duree de MONTAGE confondue avec duree de GENERATION.
sub_all([('This is a count, held two seconds: four bowls, four places, four people.',
          'This is a count: four bowls, four places, four people. It is generated at 5 seconds and cut to two in the edit — generate the full 5.')],
        label='1D · la duree de montage ne se confond plus avec celle de generation')

# 8 ─ 8C / 8D : les titres renvoyaient a une declaration qui vit dans un AUTRE document.
sub_all([(' — écart déclaré en tête de document', ''), (' — écarts déclarés en tête de document', '')],
        glob='PRET-SEQ-*.md', label='8C / 8D · renvoi a un autre document supprime du titre')

# ── les corrections qui visent UN bloc precis ────────────────────────────────
def in_block(fname, code, pairs, label):
    p = D/fname; s = p.read_text(encoding='utf-8')
    m = re.search(r'(#{2,3} VIDÉO ' + re.escape(code) + r'[^\n]*\n\n```\n)(.*?)(\n```)', s, re.S)
    if not m: log.append(f"{label} · BLOC {code} INTROUVABLE"); return
    blk = m.group(2); n = 0
    for a, b in pairs:
        if a in blk: blk = blk.replace(a, b); n += 1
    p.write_text(s[:m.start(2)] + blk + s[m.end(2):], encoding='utf-8')
    log.append(f"{label} · {n} substitution(s)")

# 1C · la chaine annonce "la meme minute, accessoires inchanges" alors que le bloc
#      declare une ellipse d'une minute avec la table re-dressee.
in_block('PRET-SEQ-01.md', '1C', [(
 'the shot that immediately precedes this one (1B), in the same place and the same minute',
 'the shot that immediately precedes this one (1B), in the same place but about a minute later — the table has been re-laid in that minute, so read its light, its grain and its skin rendering, NEVER the position of its props')],
 '1C · la chaine reconnait l\'ellipse d\'une minute')

# 1C · renvoi a un instant qui n'existe pas dans CE bloc (reste du bloc 1A).
in_block('PRET-SEQ-01.md', '1C', [('their feet not moving except for her half-step at [1.4s]',
                                   'their feet not moving except for her half-step written in the FRAME MAP above')],
         '1C · renvoi a [1.4s] (instant du bloc 1A) supprime')

# 1D · insert sans personne : le boilerplate decrivait des corps qui respirent au cadre.
in_block('PRET-SEQ-01.md', '1D', [(
 'Between the written events every body simply holds its last position, breathing, blinking and drifting a few millimetres',
 'NOBODY IS IN THIS SHOT. No body, no hand, no arm, no shoulder, no shadow of a person enters the frame at any point: it is the table alone')],
 '1D · le bloc cesse de decrire des corps dans un insert vide')

# 4H · le verrou de posture disait DEBOUT pour les deux plans, le shot 2 est accroupi.
in_block('PRET-SEQ-04.md', '4H', [(
 '@AnnaYoung is STANDING for both shots — walking to the door in shot 1, crouched on her heels at the stove and then rising in shot 2.',
 '@AnnaYoung is STANDING in shot 1, walking to the door. She is CROUCHED on her heels at the stove at the first frame of shot 2 and RISES to standing inside it. The change of posture happens across the hard cut between the two shots, and the rise happens on screen.')],
 '4H · le verrou de posture dit enfin ce que fait le shot 2')

# 4 · en-tete : 8 + 10 + 15 + 13 = 46, pas 48.
sub_all([('55 s de rushes → 48 s au montage', '55 s de rushes → 46 s au montage')],
        glob='*SEQ-04.md', label='seq. 4 · arithmetique de l\'en-tete corrigee (46 s)')

for l in log: print(l)
