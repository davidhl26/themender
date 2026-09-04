# -*- coding: utf-8 -*-
"""Deux corrections que la recherche du 04/09 apporte a MON contrat de raccord.

CORRECTION 1 — les coordonnees seules ne sont pas honorees.
  Source confirmee : \"EN LANGAGE OBSERVABLE, JAMAIS EN COORDONNEES. Bannir 'x-position 38%' :
  le modele ne les honore pas.\" Et : \"ancre qualitative ET chiffre dans LA MEME phrase, jamais
  l'un sans l'autre.\"
  Mon LAST FRAME ne donnait que des chiffres. On garde le chiffre (il fixe la formulation d'un
  bloc a l'autre) mais on lui adjoint l'ancre qualitative -- tiers gauche / centre / tiers droit --
  et on dit explicitement au modele que c'est la RELATION qui prime, pas le pourcentage.

CORRECTION 2 — un HANDOFF recopie mot pour mot fait REJOUER l'action.
  Source confirmee : \"Le plan N+1 ne reprend pas la phrase End state du plan N telle quelle (cela
  ferait rejouer l'action). Il ouvre par ce qui PERSISTE, formule comme un acquis, pas comme un
  evenement.\"
  Mon HANDOFF disait \"repeated here to the number\" sans dire que c'est un acquis. On ajoute la
  clause qui l'interdit explicitement.
"""
import re, pathlib

D = pathlib.Path('/home/user/site-web-callbot.ai/docs/generations/videos')

def ancre(x):
    x = int(x)
    if x < 34: return "left third of frame"
    if x > 66: return "right third of frame"
    return "centre of frame"

n_pos = n_hand = 0
for p in sorted(D.glob('PRET-SEQ-*.md')):
    s = p.read_text(encoding='utf-8')

    # ── 1 · chaque position gagne son ancre qualitative ──────────────────────
    def enrich(m):
        global n_pos
        who, rest = m.group(1), m.group(2)
        if 'of frame,' in rest or 'third of frame' in rest: return m.group(0)
        mx = re.search(r'x=(\d+)%', rest)
        if not mx: return m.group(0)
        n_pos += 1
        return f"@{who}: {ancre(mx.group(1))}, {rest}"
    s = re.sub(r'@(\w+): ((?:SEATED|STANDING|CROUCHED|KNEELING|LYING)?,? ?x=\d+%[^.]*\.)', enrich, s)

    # ── 2 · la phrase qui dit que la relation prime sur le pourcentage ───────
    OLD = ("WHERE THIS SHOT LEAVES EACH BODY, to the number — these are the positions the next shot "
           "inherits, whether or not the body is still inside this last frame:")
    NEW = ("WHERE THIS SHOT LEAVES EACH BODY — these are the positions the next shot inherits, whether or "
           "not the body is still inside this last frame. READ THE SPATIAL RELATION FIRST AND THE "
           "PERCENTAGE SECOND: the percentage only fixes the wording from one shot to the next, what "
           "must actually be honoured is where each body stands in relation to the room and to the "
           "other bodies:")
    s = s.replace(OLD, NEW)

    # ── 3 · le handoff est un ACQUIS, pas une action a rejouer ───────────────
    OLDH = ("Nothing in this list may be re-placed, re-lit or improved. Whatever the FRAME MAP below asks "
            "for happens AFTER this state, never instead of it.")
    NEWH = ("Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN "
            "ACTION TO PLAY: whatever brought the bodies and the props here has already happened in the "
            "attached video and must NOT be performed again. This generation opens with it already true, "
            "and everything the FRAME MAP asks for happens AFTER it, never instead of it.")
    if OLDH in s:
        n_hand += s.count(OLDH); s = s.replace(OLDH, NEWH)

    p.write_text(s, encoding='utf-8')

print(f"positions enrichies d'une ancre qualitative : {n_pos}")
print(f"HANDOFF portant la clause d'acquis          : {n_hand}")
