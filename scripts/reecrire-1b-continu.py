# -*- coding: utf-8 -*-
import re, pathlib
D = pathlib.Path('/home/user/site-web-callbot.ai/docs/generations/videos')

LOCMAP = """LOCATION MAP
ONE SINGLE FRAMING THAT TRAVELS — there is no cut anywhere in this generation. The camera begins as a medium two-shot across the kitchen from the west side, chest height about 150 cm, holding the table with @SamBefore seated at screen-left and @Maeve standing at the range at screen-right, the window burning gold above her. From [1.0s] the camera begins to drift right and forward WITH him as he rises and crosses — an operator walking, not a dolly on rails — and by [6.0s] it has arrived at a tighter two-shot of the two of them chest-up and half-silhouetted against the window, where it settles and stays for the rest of the take, breathing.
Every distance, height and frame position given below is literal and is held exactly; nothing drifts toward a more flattering angle."""

FIRST = """FIRST FRAME AND SPATIAL BLOCKING The generation opens on this exact frame, and it is the frame the attached video ends on: a medium two-shot across the kitchen from the west side, chest height about 150 cm. @SamBefore SEATED at the table screen-left at x=24%, filling 44% of frame height, three-quarter to camera and turned toward her, BOTH PALMS FLAT ON THE TABLE EDGE, the spoon lying on the wood beside his bowl where he has just set it down. @Maeve STANDING at the range screen-right at x=70%, filling 62% of frame height, her back against the range, facing the room, hands resting on the range edge either side of her hips, half-silhouetted against the gold window directly above the pan. Both cups steaming in the bar of light between them. The pan smokes very thinly. This is the frame the first video frame must already be, before anything moves: nothing is settling into place, nothing fades up, nothing is mid-transition."""

FORMAT = """FORMAT MODE
ONE SINGLE CONTINUOUS UNCUT TAKE, 14 seconds long, at real-time speed. NO CUT ANYWHERE, no montage, no dissolve, no speed ramp, no slow motion. Everything that happens in this generation is seen: nothing is skipped, nothing happens off-screen, no movement is elided between one position and the next. If a body goes from sitting to standing, the whole rise is on screen."""

CHOREO = """FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND

ONE SHOT [0.0-14.0s] — One single continuous take, no cut. The camera begins as a medium two-shot across the kitchen from the west side, chest height about 150 cm, operated and breathing, carried rather than nailed down; from [1.0s] it drifts right and forward WITH him — an operator walking with the man, arriving a fraction late on every change of direction — and settles at [6.0s] into a tighter two-shot against the window, where it stays, breathing, to the end.

[0.0s] Starting positions, exactly as the attached video leaves them: @SamBefore SEATED at x=24%, filling 44% of frame height, three-quarter to camera, both palms flat on the table edge, the spoon on the wood beside his bowl. @Maeve STANDING at the range at x=70%, filling 62% of frame height, back against the range, facing the room, hands on the range edge either side of her hips, half-silhouetted in the gold. Both cups steaming between them.

[0.0-1.0s] Nothing moves but the room: the thin smoke off the pan, the steam of the two cups turning in the bar of light, her chest lifting once and settling. He is still looking at her, still half-smiling. One slow blink.

[1.0-3.2s] HE RISES, AND THE WHOLE RISE IS SEEN. The weight goes into his palms first — the fingers flatten and go a shade paler against the wood, the tendons standing on the backs of his hands. His shoulders come forward over the table and his chin drops four or five centimetres as the body loads. Then he pushes up. THE CHAIR TAKES HIS WEIGHT LEAVING and rocks back about a centimetre on the tile with one short dry scrape. He comes up in a single unhurried movement — not athletic, a man of forty-eight getting out of a kitchen chair: the hips lead, the knees straighten a beat behind them, the torso arrives last. At full height his balance settles with ONE small sway forward and back, and his shoulders drop a centimetre as they let go of the effort. The pushed-up sleeves of his sweatshirt slide half a centimetre down his forearms as his arms come down to his sides. HIS EYES DO NOT LEAVE HER AT ANY POINT OF THE RISE.

[3.2-6.0s] HE CROSSES, three unhurried steps on the tile, and the camera goes with him — drifting right and forward at his pace, a beat behind him, the way a person following would. His weight rolls heel to ball on each step; his wool socks make almost no sound on the tile, only a soft drag on the third step. His hands stay open and empty at his sides, the fingers slightly curled, moving with his walk and not held. As he passes through the bar of window light at [4.6s] it crosses his face and shoulder once, left to right, and is gone. He arrives and STOPS PLANTED directly in front of her, at x=42%, filling 74% of frame height, close, three-quarter back to camera — and the stop is a real stop, his weight settling onto both feet with one small forward-back correction, not a freeze. Neither of them has said anything.

[6.0-7.6s] A HELD BEAT, FACE TO FACE — and it is the whole point of the shot. Her chin tips up about two centimetres to keep his eyes. His head tilts one degree to the left. She breathes in through her nose and it lifts her shoulders a centimetre and lets them down. HER SMILE DOES NOT GROW HERE; it is already there and it simply stays, which is harder and truer. The pan's thin smoke crosses the gold between their heads. Nothing else in the frame moves.

[7.6-10.0s] HIS ARMS GO AROUND HER, and the movement is seen whole. His right arm goes first and low, sliding around her waist at the small of her back; the left follows a beat later and higher. His hands come flat, the fingers spread, and the wool of her sweater gathers into soft folds under each palm. He draws her in slowly — she comes off the range edge and her weight transfers onto her front foot as she arrives against him. HER HANDS COME UP BETWEEN THEM and settle flat on his chest, one slightly higher than the other. Her eyes close as she is drawn in — the lids come down unhurried, not squeezed. The camera has already settled by now and only breathes.

[10.0-11.6s] A TRUE SILENCE, nearly two full seconds, foreheads resting against each other. NOBODY SPEAKS AND NOBODY MOVES except their breathing, and THE TWO BREATHS DO NOT FALL INTO STEP — his is slower and deeper, hers shallower and quicker, and they cross rather than match. The pan ticks once as it cools. One strand of her hair lifts in the window's warmth and settles back against her temple.

[11.6-12.4s] Her, almost a whisper, without opening her eyes and without moving her head: "Love you." Her lips are the only thing in her face that moves.

[12.4-12.9s] A breath. HIS CHEST LIFTS ONCE UNDER HER TWO HANDS and her hands ride it up and down. His jaw moves a millimetre.

[12.9-13.6s] Him, LOWER than she was, certain, just as quietly: "Love you more."

[13.6-14.0s] Held to the end, no further movement beyond their living micro-life: forehead against forehead in the gold, wrapped in each other, her hands flat on his chest, one last thin thread of smoke rising from the cooling pan beside them under the window. His eyes stay closed."""

LASTF = """LAST FRAME The two of them chest-up and half-silhouetted in the window's gold, forehead resting against forehead, both pairs of eyes closed, her two hands flat on his chest one slightly higher than the other, his arms wrapped around her waist with the wool of her sweater gathered under his palms, one last thin thread of smoke rising from the cooling pan beside them under the window. The frame is at rest and carries no motion blur."""

AUDIO = """AUDIO
SFX only. No music. No background music of any kind, no score, no drone, no ambient pad. The room first — the thin crackle of the cooling pan, a small radio too quiet to make out two metres away, a gull far off outside. Then the chair: the short dry scrape of its legs rocking back on the tile as his weight leaves it, and the small creak of the wood. His three steps in wool socks on tile, almost silent, one soft drag on the third. The rustle of wool as the embrace closes. Then a true silence with two sets of breathing in it that do not fall into step, the pan ticking as it cools, and the two low lines inside it. No music."""

p = D/'PRET-SEQ-01.md'
s = p.read_text(encoding='utf-8')
m = re.search(r'(#{2,3} VIDÉO 1B .*?\n```\n)(.*?)(\n```)', s, re.S)
blk = m.group(2)

blk = re.sub(r'(?ms)^LOCATION MAP\n.*?(?=\n\nFIRST FRAME)', LOCMAP, blk, count=1)
blk = re.sub(r'(?ms)^FIRST FRAME AND SPATIAL BLOCKING.*?(?=\n\nFORMAT MODE)', FIRST, blk, count=1)
blk = re.sub(r'(?ms)^FORMAT MODE\n.*?(?=\n\nOPTICS)', FORMAT, blk, count=1)
blk = re.sub(r'(?ms)^FRAME MAP & CHOREOGRAPHY.*?(?=\n\nSUBJECT LOCK, MAEVE)', CHOREO, blk, count=1)
blk = re.sub(r'(?ms)^LAST FRAME .*?(?=\n\n)', LASTF, blk, count=1)
blk = re.sub(r'(?ms)^AUDIO\n.*?(?=\n\nPOSITIVE CONSTRAINTS)', AUDIO, blk, count=1)

# la duree et la description de scene suivent
blk = blk.replace('Two shots, one hard cut.', 'ONE SINGLE CONTINUOUS TAKE, no cut anywhere — the rise, the crossing, the embrace and the two lines all happen inside one unbroken shot, and the camera travels with him instead of cutting.')
blk = blk.replace('10 seconds, in 2 framings joined by 1 hard cut.', '14 seconds, one single continuous framing that travels. No cut.')
blk = blk.replace('A husband crosses his kitchen', 'A husband gets up from his kitchen table, crosses the room')
# les deux personnages debout : ce n'est plus vrai, il commence assis
blk = blk.replace('Both characters are STANDING for the entire generation — nobody sits, nobody crouches, nobody leaves the frame.',
 '@SamBefore is SEATED at the table at [0.0s] and RISES ON SCREEN between [1.0s] and [3.2s]; the change of posture happens entirely in frame, never across a cut and never off-screen. From [3.2s] he is standing for the rest of the take. Nobody else sits, nobody crouches, nobody leaves the frame.')
blk = blk.replace('@SamBefore enters walking at [0.0s] and, from [1.8s] onward, stands in front of her and does not step again.',
 '@SamBefore rises from his chair between [1.0s] and [3.2s], crosses in three steps, and from [6.0s] stands in front of her and does not step again.')
blk = blk.replace('| **durée** | 10 s |', '| **durée** | 14 s |')
# l'AVOID ne doit plus interdire le mouvement de camera qui porte le plan
blk = blk.replace('a second camera move, a whip pan, a zoom or crash zoom, the camera pushing in, handheld shake',
 'a whip pan, a zoom or crash zoom, a crash-in, handheld shake, a cut of any kind, a camera move the FRAME MAP does not describe')
blk = blk.replace('anyone sitting down, ', '')

s = s[:m.start(2)] + blk + s[m.end(2):]
s = s.replace('| **durée** | 10 s |\n| **Éléments** | @SamBefore + @Maeve + @Kitchen |\n| **`start_image`** | LIEU-01 IMAGE 3',
              '| **durée** | 14 s |\n| **Éléments** | @SamBefore + @Maeve + @Kitchen |\n| **`start_image`** | LIEU-01 IMAGE 3')
p.write_text(s, encoding='utf-8')
print("1B reecrit ·", len(blk), "caracteres")
print("  HARD CUT restants :", blk.count('HARD CUT'))
print("  duree :", re.search(r'(\d+) seconds long', blk).group(1), "s")
