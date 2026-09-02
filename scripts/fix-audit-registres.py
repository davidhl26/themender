# -*- coding: utf-8 -*-
"""Corrige le registre camera BLOC PAR BLOC, et l'AVOID qui le contredisait.

Audit du 02/09, constats 2, 12, 32, 76-80 : la liste AVOID interdisait
"camera movement, dolly, pan, zoom" dans des blocs dont le registre exige un
mouvement. Ma faute : j'avais pose le registre par SEQUENCE sans toucher aux
AVOID, et sans regarder ce que chaque plan demande vraiment.

Deux corrections :
1. Le registre suit desormais le BLOC, pas la sequence. Mesure : en sequence 10
   seuls 5 blocs bougent (le recul hors de la maison rouge et la verticale
   au-dessus de la ville) ; les 10 autres sont fixes, coda d'hopital comprise.
   Et 1D est un plomb vertical sur la table, sans personnage, qui dit lui-meme
   "no movement of any kind" : il repasse en LOCKED.
2. Dans les blocs qui bougent, l'AVOID perd l'interdit generique de mouvement et
   garde les interdits utiles (deuxieme mouvement, zoom, tremblement).
   Formulation reprise de PRET-SEQ-02, ou elle etait deja correcte.
"""
import re, pathlib

D = pathlib.Path('/home/user/site-web-callbot.ai/docs/generations/videos')

REGISTER = {}
for k, t in [
 ('ALIVE', """CAMERA REGISTER — ALIVE
The camera is carried by a body, not mounted on one. It breathes with whoever holds it, drifts a centimetre or two and corrects, and reframes by small amounts as people move instead of waiting for them to arrive. It follows them. Never a shake, never a jolt, never a whip pan: this is the movement of somebody standing in the room with this family, watching them, close enough to be one of them. THE FRAME SETTLES AND COMES FULLY TO REST BEFORE THE LAST SECOND, so the final frame is clean and carries no motion blur."""),
 ('HOLDING ITS BREATH', """CAMERA REGISTER — HOLDING ITS BREATH
The camera is still carried by a body, but it has stopped following. It holds its frame and lets people leave it rather than going after them. The only movement left is the residual weight of a human holding a camera — a drift of a few millimetres, one small correction, nothing more. It never reframes to chase anybody, and it never pans to find a face. This is the register between the two: no longer free, not yet dead."""),
 ('LOCKED', """CAMERA REGISTER — LOCKED
The camera is placed, and it stays. Nobody is followed, nothing is reframed, and when a body leaves the frame the frame does not go after it. The only life left in the image is the residual weight of the head itself, well under one millimetre. This stillness is not neutrality and must never read as a surveillance camera: it is what the film lost when it lost her, and it should feel like a breath being held."""),
 ('MOVING AGAIN', """CAMERA REGISTER — MOVING AGAIN
For the first time since the hospital the camera moves of its own accord, and that movement is the point. Long, slow, unbroken, at one constant speed, with no ease-in and no ease-out. It does not hurry and it does not stop. After six sequences nailed to the floor, the simple fact that the frame travels at all is the emotional event of the scene — so the move must be smooth, deliberate and completely confident: never handheld, never nervous, never fast."""),
]:
    REGISTER[k] = t

# le registre appartient au BLOC. Defaut par acte, exceptions mesurees.
ACT = {'01':'ALIVE','02':'ALIVE','03':'HOLDING ITS BREATH','04':'LOCKED','05':'LOCKED',
       'coup':'LOCKED','06':'LOCKED','07':'LOCKED','08':'LOCKED','09':'LOCKED','10':'LOCKED'}
MEM = {'4E','4F','4G','4H','4I'}          # le souvenir russe vit dans la seq. 4
MOVERS = {'10D-2','10F-1','10F-2','10F-3','10F-4'}   # les 5 seuls plans qui bougent
STILL_INSERT = {'1D'}                      # plomb vertical, sans personnage

AVOID_OLD = 'visible camera rigs, camera movement, dolly, pan, zoom, handheld shake'
AVOID_NEW = ('visible camera rigs, a second camera move, a whip pan, a zoom or crash zoom, '
             'the camera pushing in, handheld shake')

changed_reg = changed_avoid = 0
for p in sorted(D.glob('PRET-SEQ-*.md')):
    n = p.name[9:11]
    s = p.read_text(encoding='utf-8')
    parts = re.split(r'(?m)^(#{2,3} VIDÉO .*)$', s)
    out = [parts[0]]
    for i in range(1, len(parts), 2):
        title, body = parts[i], parts[i+1]
        code = re.match(r'#{2,3} VIDÉO ([0-9A-Za-z-]+)', title).group(1)
        f = re.search(r'```\n(.*?)\n```', body, re.S)
        if not f:
            out.append(title + body); continue
        blk = f.group(1)

        want = ('LOCKED' if code in MEM or code in STILL_INSERT
                else ('MOVING AGAIN' if code in MOVERS
                      else ('LOCKED' if n == '10' else ACT[n])))

        cur = re.search(r'CAMERA REGISTER — ([A-Z][A-Z ]*)', blk)
        if cur and cur.group(1).strip() != want:
            blk = re.sub(r'CAMERA REGISTER — [A-Z][A-Z ]*\n.*?(?=\n\n)', REGISTER[want], blk, flags=re.S)
            changed_reg += 1
            # 1D redevient un plomb immobile : sa ligne de plan repasse en fixe
            if code in STILL_INSERT:
                blk = blk.replace('operated and breathing, carried rather than nailed down', 'static, locked off')

        # l'AVOID ne doit interdire le mouvement que la ou le registre l'interdit
        if want in ('ALIVE', 'MOVING AGAIN') and AVOID_OLD in blk:
            blk = blk.replace(AVOID_OLD, AVOID_NEW); changed_avoid += 1

        out.append(title + "\n\n```\n" + blk + "\n```\n" + body[f.end():])
    p.write_text("".join(out), encoding='utf-8')

print(f"registres corriges : {changed_reg} blocs")
print(f"AVOID corriges     : {changed_avoid} blocs")
