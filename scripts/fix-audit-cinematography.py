# -*- coding: utf-8 -*-
"""Audit du 02/09, constats 10, 14, 16, 17, 24, 81 : le paragraphe CINEMATOGRAPHY
de la cuisine du matin ("morning sun through domestic glass") etait colle a
l'identique dans 14 blocs -- dont le quai au couchant, le restaurant aux
lanternes et TOUT l'hopital. Quatre lumieres ecrasees par une seule.

Chaque paragraphe est desormais derive de ce que le bloc dit lui-meme de sa
lumiere, et la courbe du scenario est respectee : CLAIR avant la mort, la
clarte se retire en sequence 3.
"""
import re, pathlib

D = pathlib.Path('/home/user/site-web-callbot.ai/docs/generations/videos')

OLD_HEAD = 'Naturalistic available-light cinematography. One motivated source only — morning sun through domestic glass'

CINE = {
'KITCHEN': """CINEMATOGRAPHY
Naturalistic available-light cinematography. One motivated source only — morning sun through domestic glass — bounced warm off walls and skin, shadows open and full of colour. Exposed normally, never underexposed here: this is the one place in the film where nothing is missing. Highlights restrained and holding texture in the window and the crockery, never blown. Gentle contrast. True-to-life warm colour, never pushed, never graded.""",

'QUAY': """CINEMATOGRAPHY
Naturalistic available-light cinematography. One motivated source only — the low sun at the end of the day, coming down the quay almost level with the lens — raking across worn timber and wet stone, throwing long soft shadows and lighting faces from the side and from behind so hair and shoulders carry a warm rim. Exposed for the faces and letting the water behind them go bright: this is still the warm half of the film and nothing here is missing. Highlights restrained on the water, holding texture, never blown to white. Gentle contrast, deep golden warmth in the light itself and never in a grade.""",

'RESTAURANT': """CINEMATOGRAPHY
Naturalistic available-light cinematography. The motivated sources are practical and inside the room — amber paper lanterns hung low over the tables, and the cold green glow of a fish tank in the depth of the room. Warm pools on the tablecloths and on the faces, the corners of the room falling away into soft brown dark. Exposed for the amber, letting the shadows sit low but never go black; the green of the tank is the only cool note and it stays in the background. Highlights restrained on the lanterns and the glasses, holding texture. Gentle contrast, warm true-to-life colour, never pushed.""",

'KITCHEN_PALE': """CINEMATOGRAPHY
Naturalistic available-light cinematography. The same room and the same source as the first morning of the film — sun through domestic glass — but the light has thinned: the sun is behind high cloud, the bounce off the walls is weaker, the shadows have closed a little and lost some of their colour. Still exposed normally, still not a grey world; simply less of everything than before. Highlights restrained and holding texture, never blown. Gentle contrast. This is the first frame of the film where the warmth is measurably leaving, and it must read as weather, never as a grade.""",

'HOSPITAL': """CINEMATOGRAPHY
Naturalistic available-light cinematography. Two motivated sources, both cold and both institutional — flat overcast daylight through a large window, and the continuous tube light overhead — laid evenly across sea-green tiling and pale bedding with almost no direction and almost no shadow. Exposed normally but with the colour drained out of the light itself: what little warmth survives is in skin alone, and it is losing. Highlights restrained on the tiling, the glass and the bedding, holding texture, never blown. Flat gentle contrast, no modelling, nothing flattering. This is where the clarity of the first act withdraws — it drains, it does not switch off.""",
}

MAP = {'1A':'KITCHEN','1B':'KITCHEN','1C':'KITCHEN','1D':'KITCHEN',
       '2A':'QUAY','2B':'QUAY','2C':'RESTAURANT','2D':'RESTAURANT',
       '3A':'KITCHEN_PALE','3B':'HOSPITAL','3C':'HOSPITAL','3D':'HOSPITAL',
       '3E':'HOSPITAL','3F':'HOSPITAL'}

n = 0
for f in ['PRET-SEQ-01.md','PRET-SEQ-02.md','PRET-SEQ-03.md']:
    p = D/f
    s = p.read_text(encoding='utf-8')
    parts = re.split(r'(?m)^(#{2,3} VIDÉO .*)$', s)
    out = [parts[0]]
    for i in range(1, len(parts), 2):
        title, body = parts[i], parts[i+1]
        code = re.match(r'#{2,3} VIDÉO ([0-9A-Za-z-]+)', title).group(1)
        fen = re.search(r'```\n(.*?)\n```', body, re.S)
        if not fen or code not in MAP:
            out.append(title + body); continue
        blk = fen.group(1)
        if OLD_HEAD in blk:
            blk = re.sub(r'(?ms)^CINEMATOGRAPHY\n.*?(?=\n\n)', CINE[MAP[code]], blk, count=1)
            n += 1
        out.append(title + "\n\n```\n" + blk + "\n```\n" + body[fen.end():])
    p.write_text("".join(out), encoding='utf-8')

print(f"{n} paragraphes CINEMATOGRAPHY rendus a leur lumiere")
