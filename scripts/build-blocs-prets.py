# -*- coding: utf-8 -*-
import io,re,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from blocs_references import REFDESC

D='/home/user/site-web-callbot.ai/docs/generations/videos'

FILM = """FILM EMULATION — THE SAME STOCK FROM THE FIRST FRAME TO THE LAST
Shot on Kodak Vision3 500T 5219 tungsten colour negative, one stock, one lab, for the entire film, rated at box speed and printed flat. Cool naturalistic colour science; shadows falling slightly blue-green and holding real separation and texture inside them; skin tones understated, never warmed up, never rosy. Gentle contrast, soft highlight roll-off, highlights restrained and never blown, a faint halation ring blooming around every practical source. Moderate fine grain that grows in the underexposed areas and breathes with the exposure. Not glossy, not digital, not warm. Daylight scenes are the same stock corrected with an 85 filter, never a different look.

CAMERA — OPERATED, NOT SIMULATED
One anamorphic lens set throughout: slight barrel distortion at the frame edges, oval out-of-focus highlights, mild edge softness, faint vignetting, vintage lens character. Focus is pulled by a human hand — it arrives a few frames late, occasionally overshoots by a hair and settles back, and breathes with the operator's pace. Every held frame keeps a residual human weight in it, a drift of a few millimetres: never a locked robotic stillness, never a shake. No digital sharpening, no edge halos, no noise-reduction smear, no beauty retouching, no plastic skin, no CGI gloss.

PHOTOGRAPHIC REALISM
True skin texture with visible pores and fine hairs, real fabric weave, seams and wrinkles that crease with movement, worn surfaces with real wear, natural asymmetry, natural motion blur in every movement. Deliberately underexposed where the scene calls for it, protecting the shadows and retaining detail inside them: no banding, no posterisation, no crushed flat blacks, no smeared low-light noise, no digital mush."""

WORLD = {
'01':"""WORLD — BEFORE
Morning gold through domestic glass. High key, open shadows, warm bounce off walls and skin. Nothing is underexposed, nothing is grey, nothing is cold. There is blood under the skin. This is the light the whole rest of the film will lose, so it has to be genuinely warm here and not merely bright.""",
'04':"""WORLD — AFTER
A grey-blue world, gently underexposed, roughly two thirds of a stop below normal. Sparse motivated sources only — one bulb, one window, one sodium lamp — and deep quiet blacks between them. Colour is drained but not absent: what survives is amber from a flame, sodium orange from a street, sea-green from tile. Never a saturated hue. No red anywhere, flames included.""",
'MEM':"""WORLD — THE WASHED MEMORY
The colour is bleached out of the light itself, never in the grade. Heavy silver grain, highlights blown and bleeding, contrast flat and tired. One single hue survives: the sea-green tiling of a hospital. No red anywhere, flames included. Not one legible letter, digit, sign or Cyrillic character anywhere in frame — the country is carried by architecture, materials and light alone.""",
'RED':"""WORLD — THE RED HOUSE
The only place in the film where red is allowed, and here it is the whole place. Outside: a red door in a grey street. Inside, once the bulb is out, there is no light source at all — the room is lit by nothing but its own writing, every stroke glowing faintly from within, low and even, the colour of embers under ash, far too dim and too soft for any stroke to be read. Never bright red, never neon, never a magic glow.""",
}
WORLD['02']=WORLD['03']=WORLD['01']
for k in ['05','06','07','08','09']: WORLD[k]=WORLD['04']

SEGS=[["1A","1B","1C","1D","2A","2B","2C","2D","3A","3B","3C","3D","3E","3F"],
      ["4A","4B","4C","4D","5A","5B-1","5B-2","5C","5D","6A","6B","6C","7A","7B","8A","8B","8C","8D","8E","9A","9B","9C"],
      ["4E","4F","4G","4H","4I"],["10A","10B","10C"],
      ["10D-1","10D-2","10E","10F-1","10F-2","10F-3","10F-4","10H","10I","10J"],["10K"],["10L"]]
PREV={}
for seg in SEGS:
    for i,c in enumerate(seg):
        PREV[c]=seg[i-1] if i else None
PREV["10L"]="10H"
MOVEMENT={"10D-2","10F-1","10F-2","10F-3","10F-4"}

def chain(code, loc_now, loc_prev, first_of_film):
    p=PREV.get(code)
    if p is None:
        return ("CONTINUITY REFERENCE\nNo previous shot is attached to this generation. This is the first shot of its chain: it sets the light, the grain and the skin rendering that every following shot will be matched to. Build every frame new from the references below, at full quality."
                if not first_of_film else
                "CONTINUITY REFERENCE\n@Video 1: the live-action footage that opens the film, shot on a real camera. Use it ONLY to read the light level, the grain, the colour of the room and the state the scene is in. Do NOT reuse, copy or extend any of its frames: every frame here is built new from the references below, at full quality, and the framing comes solely from the FRAME MAP below.")
    if code in MOVEMENT:
        return f"CONTINUITY REFERENCE\n@Video 1: the previous segment of this same continuous shot ({p}). Use it ONLY to read where the movement stands — light level, grain, skin rendering, and above all the camera's exact speed and direction at the moment it hands over. Do NOT reuse, copy or extend any of its frames: every frame here is built new from the references below, at full quality. The framing comes solely from the FRAME MAP below, and the movement continues at exactly the same constant speed, with no ease-in and no ease-out."
    if loc_now and loc_now==loc_prev:
        return f"CONTINUITY REFERENCE\n@Video 1: the shot that immediately precedes this one ({p}), in the same place and the same minute. Use it ONLY to read where the scene stands — the exact light level and direction, the grain, the skin rendering, the state the bodies and the props are left in, and the camera's speed. Do NOT reuse, copy or extend any of its frames: every frame here is built new from the references below, at full quality. The framing comes solely from the FRAME MAP below and owes nothing to the previous shot's composition."
    return f"CONTINUITY REFERENCE\n@Video 1: an earlier shot from the same film ({p}), in a different place. Use it ONLY to match the physical rendering — the film stock, the grain structure, the way skin and fabric resolve, the focus behaviour, the highlight roll-off. Do NOT take its light, its palette, its exposure level, its composition or any of its frames: this shot's light comes from its own LOCATION and LIGHT paragraphs below, and its framing from its own FRAME MAP. Everything is built new, at full quality."

POS = """POSITIVE CONSTRAINTS — CHECK EVERY FRAME AGAINST THESE
Every named reference above is matched 100%: same face, same build, same wardrobe, same wear. Nobody is better groomed, better lit, better dressed or better rested than the shot before; wardrobe, hair, dirt, damage and wear do not improve or clean themselves up. Props stay exactly where the prop layout puts them. The light level, the weather and the time of day do not move inside this generation.
The choreography written in the FRAME MAP is the whole performance: no gesture, step, head turn, prop interaction or expression beyond it. Between described movements every body holds its last position naturally, breathing and blinking, never frozen and never fidgeting.
Nobody looks at the lens at any point. Nobody speaks except where DIALOGUE says so.
Every stroke of handwriting anywhere in frame is a The writing is real handwriting laid out in straight horizontal lines — word-shaped clusters separated by spaces, gathered into sentences and paragraphs — in an invented cursive alphabet whose characters recur again and again the way a real alphabet's do. Unmistakably a script, but no script that exists on earth, and not one word readable in any language: it reads as writing from across the room and as nothing at all up close. Never random scribble, never a scrawl, never abstract mark-making, never decorative squiggles. No signage, no label, no digit, no subtitle, no caption is readable anywhere.
One continuous uncut take at real-time speed, for the exact duration requested. No slow motion, no speed ramp, no added cut."""

def build(n):
    src=io.open(f'{D}/VIDEO-SEQ-{n}.md',encoding='utf-8').read()
    parts=re.split(r'(?m)^(#{2,3} VIDÉO .*)$', src)
    out=[]
    head=parts[0]
    m=re.search(r'^# (.*)$',head,re.M)
    out.append(f"# {m.group(1) if m else 'SÉQUENCE '+n}\n" if m else f"# SÉQUENCE {n}\n")
    out.append("> **BLOCS PRÊTS À COLLER.** Tout est dedans : chaîne, pellicule, monde, références, contraintes.\n"
               "> **Tu copies UN bloc entier, tu le colles, tu génères. Rien à ajouter.**\n"
               "> Modèle **Seedance 2.5** · 21:9 · 1080p · bitrate **high** · sound off.\n"
               f"> Source des blocs : `VIDEO-SEQ-{n}.md` — ce document en est la version assemblée.\n")
    prev_loc=None
    for i in range(1,len(parts),2):
        title, body = parts[i], parts[i+1]
        code=re.match(r'#{2,3} VIDÉO ([0-9A-Za-z-]+)', title).group(1)
        tags=list(dict.fromkeys(re.findall(r'@([A-Za-z][A-Za-z0-9]*)', title)))
        tags=[t for t in tags if t in REFDESC]
        locs=[t for t in tags if t in ('Kitchen','Quay','KidsBedroom','HospitalRoom','HospitalCorridor','AnnaKitchen','AnnaKitchenPast','Restaurant','NoraBedroom','BackGallery','Bathroom','LibraryCorridor','NightBus','BusShelter','RedHouseExterior','RedHouseInterior','RussianHospitalCorridor','RussianHospitalWard','RussianNightStreet','RussianCourtyard')]
        loc_now=','.join(sorted(locs))
        fence=re.search(r'```\n(.*?)\n```', body, re.S)
        if not fence:
            out.append(title+body); prev_loc=loc_now or prev_loc; continue
        inner=fence.group(1)
        sp=re.match(r'(Style prompt:.*?)(\n\n)(.*)', inner, re.S)
        style, rest = (sp.group(1), sp.group(3)) if sp else ("", inner)
        world = WORLD['MEM'] if code in ("4E","4F","4G","4H","4I") else (WORLD['RED'] if n=='10' else WORLD[n])
        refs = "ACTIVE REFERENCES\n" + "\n".join(f"@{t}: {REFDESC[t]}" for t in tags) if tags else ""
        rest = re.sub(r'\nNEGATIVE PROMPT ', '\n'+POS+'\n\nNEGATIVE PROMPT ', rest, count=1)
        blocks=[chain(code, loc_now, prev_loc, code=='1A'), style, FILM, world, refs, rest]
        new="\n\n".join(b for b in blocks if b)
        out.append(title+"\n\n```\n"+new+"\n```\n"+body[fence.end():])
        prev_loc=loc_now or prev_loc
    io.open(f'{D}/PRET-SEQ-{n}.md','w',encoding='utf-8').write("\n".join(out))
    return len(range(1,len(parts),2))

tot=0
for n in ['01','02','03','04','05','06','07','08','09','10']:
    c=build(n); tot+=c; print(f"  PRET-SEQ-{n}.md : {c} blocs")
print(f"TOTAL {tot} blocs prêts à coller")
