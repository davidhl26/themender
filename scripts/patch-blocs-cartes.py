# -*- coding: utf-8 -*-
"""Intègre les cartes de 00-CARTES-A-COLLER.md DANS chaque bloc PRET-SEQ,
et pose le registre caméra en trois actes.

But : un bloc = tout. David copie UN bloc, il colle dans Higgsfield, il génère.
Plus aucun document à ouvrir à côté.

Idempotent : relançable sans doubler.
"""
import io, re, sys, pathlib

D = pathlib.Path('/home/user/site-web-callbot.ai/docs/generations/videos')

# ─────────────────────────── les cartes tempérament ───────────────────────────
src = (D/'00-CARTES-A-COLLER.md').read_text(encoding='utf-8')
sec = src[src.index('# 3. LES CARTES TEMPÉRAMENT'):src.index('# 4. LA CHAÎNE')]
TEMPER = dict(re.findall(r'^## @(\w+)[^\n]*\n\n```\n(.*?)\n```', sec, re.M | re.S))

# ─────────────────────────── la carte anti-dérive ─────────────────────────────
ANTIDRIFT = re.search(r'# 5\. LA CARTE ANTI-DÉRIVE.*?```\n(.*?)\n```', src, re.S).group(1)

# ───────────────────── le registre caméra, en trois actes ─────────────────────
# La courbe suit celle que le scénario impose déjà à la lumière :
# CLAIR avant la mort · la clarté se retire en séq. 3 · SOMBRE ensuite.
REGISTER = {
'ALIVE': """CAMERA REGISTER — ALIVE
The camera is carried by a body, not mounted on one. It breathes with whoever holds it, drifts a centimetre or two and corrects, and reframes by small amounts as people move instead of waiting for them to arrive. It follows them. Never a shake, never a jolt, never a whip pan: this is the movement of somebody standing in the room with this family, watching them, close enough to be one of them. THE FRAME SETTLES AND COMES FULLY TO REST BEFORE THE LAST SECOND, so the final frame is clean and carries no motion blur.""",
'HOLDING': """CAMERA REGISTER — HOLDING ITS BREATH
The camera is still carried by a body, but it has stopped following. It holds its frame and lets people leave it rather than going after them. The only movement left is the residual weight of a human holding a camera — a drift of a few millimetres, one small correction, nothing more. It never reframes to chase anybody, and it never pans to find a face. This is the register between the two: no longer free, not yet dead.""",
'LOCKED': """CAMERA REGISTER — LOCKED
The camera is placed, and it stays. Nobody is followed, nothing is reframed, and when a body leaves the frame the frame does not go after it. The only life left in the image is the residual weight of the head itself, under one millimetre. This stillness is not neutrality and must never read as a surveillance camera: it is what the film lost when it lost her, and it should feel like a breath being held.""",
'RETURNING': """CAMERA REGISTER — MOVING AGAIN
For the first time since the hospital the camera moves of its own accord, and that movement is the point. Long, slow, unbroken, at one constant speed, with no ease-in and no ease-out. It does not hurry and it does not stop. After six sequences nailed to the floor, the simple fact that the frame travels at all is the emotional event of the scene — so the move must be smooth, deliberate and completely confident: never handheld, never nervous, never fast.""",
}
ACT = {'01':'ALIVE','02':'ALIVE','03':'HOLDING','04':'LOCKED','05':'LOCKED',
       '06':'LOCKED','07':'LOCKED','08':'LOCKED','09':'LOCKED','10':'RETURNING'}
# le souvenir russe vit dans la séq. 4 : il garde le registre verrouillé
MEM = {'4E','4F','4G','4H','4I'}

# ───────── les formules de plan, réécrites par acte (l'acte I ne se verrouille plus) ─────────
SHOTFIX = {
 'ALIVE':   [(r'static, locked off', 'operated and breathing, carried rather than nailed down'),
             (r'\block(ed)? off\b',  'operated and breathing')],
 'HOLDING': [(r'static, locked off', 'held, operated, no longer following'),
             (r'\block(ed)? off\b',  'held, operated, no longer following')],
}

def characters(title, body):
    """Les personnages RÉELLEMENT au cadre. Une carte de trop fait entrer quelqu'un."""
    tags = re.findall(r'@([A-Za-z][A-Za-z0-9]*)', title)
    return [t for t in dict.fromkeys(tags) if t in TEMPER]

def patch(n):
    p = D/f'PRET-SEQ-{n}.md'
    s = p.read_text(encoding='utf-8')
    parts = re.split(r'(?m)^(#{2,3} VIDÉO .*)$', s)
    out = [parts[0]]
    done = 0
    for i in range(1, len(parts), 2):
        title, body = parts[i], parts[i+1]
        code = re.match(r'#{2,3} VIDÉO ([0-9A-Za-z-]+)', title).group(1)
        f = re.search(r'```\n(.*?)\n```', body, re.S)
        if not f:
            out.append(title + body); continue
        blk = f.group(1)

        # 1 ─ registre caméra, inséré juste avant CAMERA — OPERATED
        reg = 'LOCKED' if code in MEM else ACT[n]
        if 'CAMERA REGISTER' not in blk:
            blk = blk.replace('CAMERA — OPERATED, NOT SIMULATED',
                              REGISTER[reg] + '\n\nCAMERA — OPERATED, NOT SIMULATED', 1)

        # 2 ─ les formules de plan suivent le registre
        for pat, rep in SHOTFIX.get(reg, []):
            blk = re.sub(pat, rep, blk)

        # 3 ─ cartes tempérament, juste après ACTIVE REFERENCES
        chars = characters(title, body)
        if chars and 'TEMPERAMENT,' not in blk:
            card = "\n".join(TEMPER[c] for c in chars)
            if 'LOCATION MAP' in blk:
                blk = blk.replace('LOCATION MAP', card + '\n\nLOCATION MAP', 1)
            else:
                blk = blk.replace('FORMAT MODE', card + '\n\nFORMAT MODE', 1)

        # 4 ─ carte anti-dérive, juste avant les contraintes positives
        if 'CONTINUITY — WHAT MUST NOT DRIFT' not in blk:
            blk = blk.replace('POSITIVE CONSTRAINTS',
                              ANTIDRIFT + '\n\nPOSITIVE CONSTRAINTS', 1)

        out.append(title + "\n\n```\n" + blk + "\n```\n" + body[f.end():])
        done += 1
    p.write_text("".join(out) if out[0].endswith('\n') else "\n".join(out), encoding='utf-8')
    return done

tot = 0
for n in ['01','02','03','04','05','06','07','08','09','10']:
    c = patch(n); tot += c
    print(f"  PRET-SEQ-{n}.md : {c} blocs · registre {ACT[n]}")
print(f"TOTAL {tot} blocs")
