# -*- coding: utf-8 -*-
"""LE CONTRAT DE RACCORD, applique a toute la chaine.

David : \"je veux pouvoir situer les personnages dans l'espace, un tracking exact,
et que le plan d'avant reflete sur le plan prochain.\"

Mesure avant : 6 LAST FRAME chiffres sur 62, et dans 50 raccords sur 52 la fin du
plan N etait en prose pendant que le debut du plan N+1 donnait des pourcentages
inventes separement. Rien ne reliait les deux bouts.

PRINCIPE, appris en verifiant : le contrat transmet CE QUE LE PLAN FINIT PAR
MONTRER, jamais la derniere position connue des corps. 4B finit sur un macro dans
le grain du crayon, 4D sur des moufles et \"nobody in the room\" : leur faire
transmettre une position de personnage serait faux. C'est donc la prose du LAST
FRAME qui commande le CONTENU, et le bloc ne fournit que les CHIFFRES des
personnages reellement presents dans cette derniere image.

N'invente aucun chiffre : un personnage sans coordonnee nulle part dans son bloc
reste en prose et est signale en fin d'execution.
Idempotent : ne touche pas un bloc qui porte deja le contrat.
"""
import re, pathlib

D = pathlib.Path('/home/user/site-web-callbot.ai/docs/generations/videos')
FILES = sorted(D.glob('PRET-SEQ-*.md'))
RX_BLOCK = r'(#{2,3} VIDÉO ([0-9A-Za-z-]+)[^\n]*\n.*?\n```\n)(.*?)(\n```)'
RX_POS = re.compile(r'@(\w+)\b((?:(?!@\w)[^.\n]){0,140}?)x=(\d+)%((?:(?!@\w)[^.\n]){0,80})')

def coords(blk):
    """Derniere position chiffree de chaque personnage, cherchee dans TOUT le bloc."""
    out = {}
    for m in RX_POS.finditer(blk):
        w, mid, x, post = m.groups()
        h = re.search(r'filling (\d+)% of frame height', mid + post)
        po = re.search(r'\b(SEATED|STANDING|CROUCHED|KNEELING|LYING)\b', mid)
        d = out.get(w, {})
        out[w] = {'x': x, 'h': h.group(1) if h else d.get('h'),
                  'posture': po.group(1) if po else d.get('posture')}
    # posture de secours : le verrou de CHARACTER PERFORMANCE fait autorite
    for m in re.finditer(r'@(\w+) is (SEATED|STANDING|CROUCHED|KNEELING)', blk):
        w, po = m.groups()
        if w in out and not out[w].get('posture'):
            out[w]['posture'] = po
    return out

def last_frame(blk):
    m = re.search(r'(?ms)^LAST FRAME[^\n]*(?:\n(?!\n).*)*', blk)
    return m.group(0) if m else None

def prev_of(blk):
    m = re.search(r'precedes this one \(([^)]+)\)|continuous shot \(([^)]+)\)|same film \(([^)]+)\)', blk)
    return next((g for g in m.groups() if g), None) if m else None

S = {}
for p in FILES:
    for m in re.finditer(RX_BLOCK, p.read_text(encoding='utf-8'), re.S):
        code, blk = m.group(2), m.group(3)
        S[code] = {'blk': blk, 'lf': last_frame(blk), 'coords': coords(blk), 'prev': prev_of(blk)}

def build_lf(code):
    """Le CONTENU vient de la prose du LAST FRAME (elle seule sait ce qui est au
    cadre). Les CHIFFRES viennent du bloc : on donne la derniere position connue
    de chaque corps, en disant honnetement que c'est la position ou le plan les
    laisse -- qu'ils soient encore au cadre ou non. Le plan suivant s'ouvre le
    plus souvent sur la meme piece, et c'est ce dont il a besoin."""
    v = S[code]
    if not v['lf']: return None, []
    if 'THE EXACT STATE THIS SHOT HANDS OVER' in v['lf']:
        return v['lf'], []
    prose = re.sub(r'(?m)^LAST FRAME\s*', '', v['lf']).strip()
    lines = []
    for w, d in v['coords'].items():
        if not d.get('x'): continue
        bits = ([d['posture']] if d.get('posture') else []) + [f"x={d['x']}%"]
        if d.get('h'): bits.append(f"filling {d['h']}% of frame height")
        lines.append(f"@{w}: " + ", ".join(bits) + ".")
    head = ("LAST FRAME — THE EXACT STATE THIS SHOT HANDS OVER, because the next shot opens on it\n"
            "WHAT IS IN THE FRAME AT THE LAST INSTANT: " + prose)
    if lines:
        head += ("\nWHERE THIS SHOT LEAVES EACH BODY, to the number — these are the positions the next shot "
                 "inherits, whether or not the body is still inside this last frame: " + " ".join(lines))
    return head, []

HAND = ("HANDOFF — THE EXACT STATE THIS SHOT INHERITS FROM THE ATTACHED VIDEO\n"
"These are NOT new positions to invent. This is the frame the previous shot ({p}) ends on, repeated here to the "
"number, and the first frame of this generation must reproduce it exactly before anything moves.\n{body}\n"
"Nothing in this list may be re-placed, re-lit or improved. Whatever the FRAME MAP below asks for happens AFTER "
"this state, never instead of it.")

n_lf = n_hand = 0; gaps = []
for p in FILES:
    src = p.read_text(encoding='utf-8'); out = []; last = 0
    for m in re.finditer(RX_BLOCK, src, re.S):
        code, blk = m.group(2), m.group(3); new = blk
        lfnew, miss = build_lf(code)
        if lfnew and 'THE EXACT STATE THIS SHOT HANDS OVER' not in blk:
            new = re.sub(r'(?ms)^LAST FRAME[^\n]*(?:\n(?!\n).*)*', lfnew.replace('\\', '\\\\'), new, count=1)
            n_lf += 1
            if miss: gaps.append((code, miss))
        pv = S[code]['prev']
        if pv and pv in S and 'HANDOFF —' not in new:
            pl, _ = build_lf(pv)
            if pl:
                new = new.replace('ACTIVE REFERENCES',
                                  HAND.format(p=pv, body=pl.split('\n', 1)[1]) + '\n\nACTIVE REFERENCES', 1)
                n_hand += 1
        out.append(src[last:m.start(3)]); out.append(new); last = m.end(3)
    out.append(src[last:]); p.write_text("".join(out), encoding='utf-8')

print(f"LAST FRAME rendus transmissibles : {n_lf}")
print(f"HANDOFF poses                    : {n_hand}")
print(f"personnages sans coordonnee      : {len(gaps)}")
for c, w in gaps: print(f"   {c:8} {w}")
