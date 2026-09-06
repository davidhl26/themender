#!/usr/bin/env python3
"""Reecrit CONTINUITY REFERENCE + HANDOFF selon la doc Seedance.

Trois regles documentees, appliquees ici :
  1. « Align the boundary frame BEFORE describing new content. » La formulation
     « then connect to the source video » (et ses equivalents : « pick the scene up
     exactly where the attached video leaves it ») est la formulation d'ECHEC
     documentee : elle fait fuiter des elements de la suite dans le debut du plan.
  2. « Boundary frames connect naturally, not identically. » Exiger une reproduction
     pixel a pixel n'est pas tenu par le modele ; on demande l'ETAT, pas l'image.
  3. Une phrase de ROLE par media, jamais fusionnee : ce que la reference definit,
     et ce qu'il ne faut PAS en prendre.

⚠ Pas de « @ » devant VIDEO 1 / IMAGE 1 : l'editeur Higgsfield parse tout « @… »
comme une mention d'Element et l'avale (constate en vrai sur le prompt de David).
"""
import re, glob, os

BOUNDARY = (
 "THE ATTACHED VIDEO (VIDEO 1) is the source clip: the shot that immediately precedes this one ({prev}){same}. "
 "ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: this clip opens "
 "on the state written under HANDOFF below — already true, nothing replayed — and only then moves on to the action the "
 "FRAME MAP gives. The boundary is meant to CONNECT NATURALLY, NOT IDENTICALLY: what must match is the state of the bodies "
 "and props, the light and the camera — not a pixel-identical image. "
 "WHAT TO TAKE FROM VIDEO 1: its light level and direction, its grain, its skin rendering, and the way its camera behaves — "
 "the same height, the same kind of movement, the same speed, the same breathing weight in the frame. "
 "WHAT NOT TO TAKE FROM VIDEO 1: its framing. The framing of this shot is the one the FRAME MAP gives below. "
 "Do not reset the room, do not relight it, do not change operator.")

MIDMOVE = (
 "THE ATTACHED VIDEO (VIDEO 1) is the previous segment of this same continuous shot ({prev}). "
 "ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME, AND THE CAMERA IS ALREADY MOVING ON IT. ALIGN THE BOUNDARY FIRST: "
 "read from VIDEO 1 the camera's exact speed, direction and height at the instant it hands over, start on that motion "
 "already underway, and only then carry the move on — same constant speed, same line, no ease-in, no ease-out, no restart. "
 "WHAT TO TAKE FROM VIDEO 1: the motion vector at the boundary, the light level, the grain, the skin rendering. "
 "WHAT NOT TO TAKE FROM VIDEO 1: any new framing of its own — the move continues into the FRAME MAP below. "
 "The join must read as one single move across the two clips.")

ELSEWHERE = (
 "THE ATTACHED VIDEO (VIDEO 1) is an earlier shot from the same film ({prev}), IN A DIFFERENT PLACE. It is a rendering "
 "reference only. WHAT TO TAKE FROM VIDEO 1: the film stock, the grain structure, the way skin and fabric resolve, the "
 "focus behaviour, the highlight roll-off. WHAT NOT TO TAKE FROM VIDEO 1: its light, its palette, its exposure level, its "
 "composition, its framing, and anything that was in its frame. This shot's light comes from its own LOCATION and LIGHT "
 "paragraphs below, its framing from its own FRAME MAP. Everything else is built new, at full quality.")

HEAD = (
 "No video is attached to this generation. This is the first shot of its chain: it sets the light, the grain and the skin "
 "rendering every following shot will be matched to. THE ATTACHED START IMAGE (IMAGE 1) IS THE FIRST FRAME: it defines the "
 "opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. "
 "WHAT NOT TO TAKE FROM IMAGE 1: nothing of its staging beyond that first frame — no empty-room look once bodies move, no "
 "reference border, no backdrop, no multi-view layout. Build every frame new from the references below, at full quality.")

def prev_of(par):
    m = re.search(r'\(([\dA-Za-z.\-]+)\)', par)
    return m.group(1) if m else 'the previous shot'

def rewrite(path):
    t = open(path, encoding='utf-8').read(); hits = 0
    def repl(m):
        nonlocal hits
        head, par = m.group(1), m.group(2)
        prev = prev_of(par)
        if 'MID-MOVEMENT' in head:            new = MIDMOVE.format(prev=prev)
        elif 'DIFFERENT PLACE' in head:       new = ELSEWHERE.format(prev=prev)
        elif 'NO VIDEO IS ATTACHED' in head:  new = HEAD
        elif 'OPENING FOOTAGE' in head:       return m.group(0)      # cas unique, deja correct
        else:
            same = ', in the same place and the same minute' if 'same minute' in par else (
                   ', in the same place' if 'same place' in par else '')
            extra = ''
            if 're-laid' in par:
                extra = (" THE PROPS ARE THE ONE EXCEPTION: the table has been re-laid in the minute between the two shots, "
                         "so do NOT carry the prop positions over — the PROP LAYOUT below is the only truth about them.")
            new = BOUNDARY.format(prev=prev, same=same) + extra
        hits += 1
        return head + '\n' + new
    t = re.sub(r'^(CONTINUITY REFERENCE[^\n]*)\n([^\n]+)', repl, t, flags=re.M)
    # la reproduction pixel-exacte n'est pas tenue par le modele
    t = t.replace("and the first frame of this generation must reproduce it exactly before anything moves.",
                  "and this generation opens with that state already true. It must CONNECT NATURALLY, NOT IDENTICALLY: "
                  "match the state, the light and the camera, never chase a pixel-identical copy.")
    open(path, 'w', encoding='utf-8').write(t)
    return hits

if __name__ == '__main__':
    d = os.path.join(os.path.dirname(__file__), '..', 'docs', 'generations', 'videos')
    tot = sum(rewrite(f) for f in sorted(glob.glob(os.path.join(d, 'PRET-SEQ-*.md'))))
    print(tot, "paragraphes CONTINUITY REFERENCE reecrits")
