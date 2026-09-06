# PROMPTS COURTS — SÉQUENCE 01

> ~300 mots par plan, l'ordre recommandé par Higgsfield et ByteDance.
> Le détail complet reste dans `PRET-SEQ-01.md` : géométrie GEO, verrous, raccords numérotés.
> **C'est CETTE version qu'on colle dans Higgsfield.** L'autre est le document de tournage.

## 1A — plan 1.2 « Je crois que j'ai brûlé les toasts » *(10 s de rushes → 9 s au montage · Elements : @SamBefore + @Maeve + @Kitchen · start frame : LIEU-01 IMAGE 2 `abf2d210`, ou la dernière frame de la vidéo des toasts)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @SamBefore + @Maeve + @Kitchen |
| **`start_image`** | LIEU-01 IMAGE 2 `abf2d210`, ou la dernière frame de la vidéo des toasts |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — A wife has just burned the toast in the golden light of the window above the stove.
CONTINUITY — VIDEO 1 is the live-action footage that opens the film, shot on a real camera. TAKE from it the light level, the grain, the colour of the room and the state the scene is in, and match them. DO NOT TAKE its frames or its framing: the framing is the one written under OPENING FRAME.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — One single shot, no cut. Wide across the room, camera on the west side at eye level, about 145 cm high, operated and breathing, carried rather than nailed down.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.4s] Her right hand reaches down to the front-left knob and TURNS THE GAS OFF — the blue flame shrinks and dies, the sizzle sinks to a whisper. [2.4-4.7s] Her eyes on his, half a confession and half a laugh: "I think I burned the toast." A beat of silence. [4.7-7.1s] Her, relaxed, matter-of-fact, the amusement rising on the last word, a small pause inside the line: "It's broken." — pause — "We're saving money." [7.1-9.4s] A WARM SMILING SILENCE.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 40 mm f/2.8 equivalent.
LIGHT — one source only, in every shot without exception: the single window directly above THE GAS RANGE on the east wall.
SOUND — [2.6-4.0s] @Maeve, smiling, half confession half laugh: "I think I burned the toast." [4.7-6.1s] @SamBefore, gentle, deadpan, no edge: "Why don't you use the toaster?" [6.8-8.6s] @Maeve, relaxed, matter-of-fact, amused on the last word, a small pause between the two sentences: "It's broken." "We're saving money." Nobody else speaks.
ENDING FRAME, the state this shot hands over — The wide of the kitchen from the west side, eye level 145 cm, static and settled: @SamBefore SEATED at the table screen-left, both palms flat on the table edge and the spoon set down beside his bowl, smiling up at her;
AVOID — a toaster, any toaster visible anywhere, the man standing up, the man rising from his chair, the woman walking away from the range, a knife or spatula or any utensil in her hands, the toast leaving the pan, toast or bread or a plate on the table, food being served, a third person in the kitchen.
```

## 1B — plans 1.3 et 1.4 « Il traverse, il l'enlace · front contre front » *(14 s de rushes → 13 s au montage · Elements : @SamBefore + @Maeve + @Kitchen · start frame : LA DERNIÈRE FRAME DE 1A — pas l'IMAGE 3)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 14 s |
| **Éléments** | @SamBefore + @Maeve + @Kitchen |
| **`start_image`** | **LA DERNIÈRE FRAME DU CLIP 1A**, extraite du rush. 1B ouvre sur le cadre exact où 1A s'arrête — même axe ouest, même hauteur 145 cm, Sam encore assis, les deux paumes à plat. **PAS l'IMAGE 3** : l'IMAGE 3 est le cadre d'ARRIVÉE de 1B, pas son premier frame ; la donner en `start_image` fait ouvrir la génération sur le two-shot frontal et tue le raccord avec 1A. |
| **`image_references`** | LIEU-01 IMAGE 3 `e9dc3786`, ANGLE H — **référence de composition seulement** : c'est le cadre que la caméra doit atteindre à la fin de son déplacement (two-shot frontal, hauteur de poitrine 150 cm, gazinière et fenêtre plein axe). |
| **`video_references`** | le clip 1A — pour le grain, la lumière, la peau et la façon dont la caméra respire. |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — A husband gets up from his kitchen table, crosses the room and plants himself in front of his wife;
CONTINUITY — VIDEO 1 is the shot immediately before this one (1A). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the INHERITED STATE line below, already true, nothing replayed, then move on. CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @SamBefore: left third of frame, SEATED at the table, both palms flat on its edge, x=30%, filling 48% of frame height. @Maeve: right third of frame, STANDING at the range with her back against it and facing the room, x=68%, filling 62% of frame height.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — The generation opens on this exact frame, and it is the frame the attached video ends on: a medium two-shot across the kitchen from the west side, eye level 145 cm.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-3.4s] HE RISES, AND THE WHOLE RISE IS SEEN. [3.4-6.8s] A HELD BEAT, FACE TO FACE — and it is the whole point of the shot. [6.8-10.2s] HIS ARMS GO AROUND HER, and the movement is seen whole. A TRUE SILENCE, nearly two full seconds, foreheads resting against each other. [10.2-13.6s] Him, LOWER than she was, certain, just as quietly: "Love you more."
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — one source only, in every shot without exception: the single window directly above THE GAS RANGE on the east wall.
SOUND — [11.6-12.4s] @Maeve, whispered, forehead to forehead, eyes closed: "Love you." [12.9-13.6s] @SamBefore, lower, certain, just as quietly: "Love you more." Nobody else speaks.
ENDING FRAME, the state this shot hands over — The two of them chest-up and half-silhouetted in the window's gold, forehead resting against forehead, both pairs of eyes closed, her two hands flat on his chest one slightly higher than the other, his arms wrapped around her waist with the wool of her sweater gathered under his palms, one last thin thread of smoke rising from the cooling pan beside them under the window.
AVOID — a kiss, kissing, mouths touching, an open-mouthed kiss, the embrace played long or theatrical, tears, crying, sadness, a toaster, any toaster visible anywhere.
```

## 1C — plan 1.5 « Les enfants arrivent » *(8 s de rushes → 4 s au montage · Elements : @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @Kitchen · start frame : LIEU-01 IMAGE 1 `a3f6c078`, le master)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 8 s |
| **Éléments** | @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @Kitchen |
| **`start_image`** | LIEU-01 IMAGE 1 `a3f6c078`, le master |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — A minute after the embrace, @NoraBefore and @MiloBefore arrive and the family folds together without a word being said: @MiloBefore runs in and throws his arms around his mother's legs;
CONTINUITY — VIDEO 1 is the shot immediately before this one (1B). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the INHERITED STATE line below, already true, nothing replayed, then move on. CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @SamBefore: centre-left of frame, STANDING, on his feet and across the room — he rose and crossed during this shot — chest to chest with @Maeve in front of the gas range, his arms wrapped around her waist, x=44%, filling 72% of frame height.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — One single shot, no cut. Wide across the room, camera on the west side at eye level, about 145 cm high, operated and breathing, carried rather than nailed down.
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.0s] Starting positions, held until described otherwise: @SamBefore at x=60%, filling 62% of frame height, and @Maeve at x=70%, filling 56% of frame height, both STANDING in front of the range, just separating from each other, three-quarter toward camera, both still carrying the end of the same smile. [2.0-4.0s] @SamBefore turns his head to the doorway. She crosses in three unhurried steps and folds into his side under the open arm; [4.0-6.0s] The four of them in one frame.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 40 mm f/2.8 equivalent.
LIGHT — one source only, in every shot without exception: the single window directly above THE GAS RANGE on the east wall.
SOUND — None. NOBODY SPEAKS IN THIS GENERATION — not the father, not the mother, not @NoraBefore, not @MiloBefore. No line is added, no name is called, no greeting is exchanged.
ENDING FRAME, the state this shot hands over — The four of them together in front of the gold window at the range side of the room — the small @MiloBefore's arms around his mother's legs and her hand on the crown of his head, @NoraBefore folded into her father's side under his closed arm with his chin resting on the top of her head — the breakfast table laid for four crossing the lower third untouched, the toast smoking thinly on its plate at the centre of it, the dark hallway doorway empty at the right frame edge.
AVOID — anyone speaking, a spoken line, moving lips, a name being called, a toaster, any toaster visible anywhere, anyone sitting down, a chair being pulled out, anyone touching the table, anyone eating.
```

## 1D — plan 1.6 « Quatre bols » *(5 s de rushes → 2 s au montage · Elements : @Kitchen seul · start frame : LIEU-01 IMAGE 5 `9ff73e9b`, ANGLE G)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 5 s |
| **Éléments** | @Kitchen |
| **`start_image`** | LIEU-01 IMAGE 5 `9ff73e9b`, ANGLE G |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — One overhead insert, no people at all: the breakfast table laid for four, intact and untouched, the burned toast smoking gently on its plate at the centre, while a family is heard alive in the room off screen.
CONTINUITY — VIDEO 1 is the shot immediately before this one (1C). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the INHERITED STATE line below, already true, nothing replayed, then move on. CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @SamBefore: centre of frame, x=60%, filling 62% of frame height. @Maeve: right third of frame, x=70%, filling 56% of frame height. @NoraBefore: right third of frame, x=86%, filling 48% of frame height. Nothing in this list may be re-placed, re-lit or improved.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — One single shot, no cut. Straight down onto the table from directly above, camera 190 cm over the tabletop, level, static, locked off, no movement of any kind.
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.2s] Frame contents, fixed for the whole shot: the laid table filling the frame, the plate with the two blackened slices at the centre at x=50% and 50% of frame height, the marmalade jar just beside it, the four bowls at the four places — one at x=22%, one at x=50% near the top edge, one at x=78%, one at x=50% near the bottom edge — the two cups and the two milk glasses at their places, the hard bar of warm light crossing the wood diagonally from the upper right to the lower left. [1.2-2.4s] Still nothing moves on the table. [2.4-3.6s] Still nothing moves on the table.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 40 mm f/2.8 equivalent.
LIGHT — one source only, in every shot without exception: the single window directly above THE GAS RANGE on the east wall.
SOUND — None. Nobody speaks. The family is heard off screen as noise, never as words: not one line, not one intelligible sentence, no name called. SFX only.
ENDING FRAME, the state this shot hands over — The breakfast table straight from above, laid for four and untouched — four bowls one at each place, the open jar of orange marmalade with its standing teaspoon at the centre, the butter dish, two faintly steaming coffees, two glasses of milk, and the plate with the two blackened slices at the middle of the table with one thin thread of smoke rising straight up through the hard bar of warm window light crossing the wood.
AVOID — any person in frame, a hand entering frame, an arm reaching in, a head at the frame edge, a shadow of a person across the table, a reflection of a person, chairs moving, objects moving, the marmalade jar moving, the plate moving.
```
