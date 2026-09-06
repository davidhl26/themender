# PROMPTS COURTS — SÉQUENCE 10

> ~300 mots par plan, l'ordre recommandé par Higgsfield et ByteDance.
> Le détail complet reste dans `PRET-SEQ-10.md` : géométrie GEO, verrous, raccords numérotés.
> **C'est CETTE version qu'on colle dans Higgsfield.** L'autre est le document de tournage.

## 10A — plan 10.1 « La maison rouge, et la porte » *(8 s → 4 s · @Nora + @RedHouseExterior · start frames LIEU-15 IMAGE 1 puis IMAGE 2 · 40 mm f/2.8)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 8 s |
| **Éléments** | @Nora + @RedHouseExterior |
| **`start_image`** | LIEU-15 IMAGE 1 puis IMAGE 2 |
| **`video_references`** | *aucune — c'est une tête de chaîne* |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — @Nora walks the last metres of a grey street toward the only red house in the world, stops, lays her hand flat on the door —…
CONTINUITY — no video attached. This is the head of its chain: it sets the light, grain and skin rendering the following shots match. THE ATTACHED IMAGE IS THE FIRST FRAME — it fixes the opening composition, every body position and pose, every prop state and the camera direction; take nothing else from it, no border, no backdrop, no empty-room staging.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — very wide straight down the street, eye level 160 cm, locked off, ref axis; the red house centred x=50%, 55% h at the far end. START: @Nora enters…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.8s] START: @Nora enters bottom of frame at x=48%, from directly behind, 22% h, walking away down the middle of the road; Six unhurried steps… [1.8-3.6s] She stops before the house, back to camera, shoulders lifting once on a breath. [3.6-5.4s] She stands 3/4 back, looking at the door. [5.4-7.2s] Her right hand rises and lays flat on the board at chest height, fingers spread. The door gives and swings inward 40 cm on…
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 40 mm f/2.8 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — STATE A · THE WINDOW LIT, THE DOOR SHUT (the arrival).
SOUND — None. Nobody speaks in this generation. SFX only.
ENDING FRAME, the state this shot hands over — The door 40 cm open, warm light widening across her cheek and the porch boards, her hand still flat on the board, the street black behind…
AVOID — a paraffin flame, a flickering flame, candlelight, knocking, a doorbell, a second person, any red outside the house, red on figure, the door opening before her hand touches it, readable words.
```

## 10B — plan 10.2 « Des écritures partout » *(12 s → 7 s · @Nora + @RedHouseInterior v2 · start frame IMAGE A v2 · 28 mm f/1.4)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 12 s |
| **Éléments** | @Nora + @RedHouseInterior |
| **`start_image`** | IMAGE A v2 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — @Nora steps into a room written on for months and turns once on herself, far too slowly for a look. 12 seconds, one continuous framing, no…
CONTINUITY — VIDEO 1 is an earlier shot of the same film (10A), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Nora: left third of frame, STANDING, x=32%. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO…
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — wide from just inside the doorway, eye level 160 cm, locked off, ref axis; the bulb at the top of frame, the pots sharp along the lower frame…
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-3.7s] START: the written room, the bulb burning, the pots, brushes, ladder and mattress all in frame. Her head goes up the left wall and… [3.7-7.3s] She turns once on herself — ONE single full revolution taking four and a half seconds, far too slow for a look; [7.3-11.0s] She comes to rest facing the far wall again, 3/4 back, both arms hanging.
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 28 mm f/1.4 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — TWO STATES, NOTHING IN BETWEEN.
SOUND — None. Nobody speaks in this generation. SFX only.
ENDING FRAME, the state this shot hands over — @Nora 3/4 back to camera in the middle of the written room, arms hanging, the bulb burning above her, the pots and brushes sharp along the…
AVOID — paint pots absent, brushes absent, ladder absent, mattress absent, a clean room, a paraffin lamp, candles, writing above a man's height, writing on the ceiling, glowing walls.
```

## 10C — plans 10.3 + 10.4 « Le dragon, puis CLIC » *(10 s → 7 s · @Nora + @RedHouseInterior v2 · start frame shot 1 : IMAGE B v2 ; shot 2 : aucun · 28 mm f/1.4)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @Nora + @RedHouseInterior |
| **`start_image`** | shot 1 : IMAGE B v2 ; shot 2 : aucun |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — @Nora stops dead before one clear empty patch of plaster in the middle of the writing, smiles without knowing why, and walks on; at the door…
CONTINUITY — VIDEO 1 is the shot immediately before this one (10B). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the inherited state below, already true, nothing replayed, then move on. It must CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin rendering and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Nora: left third of frame, STANDING, x=30%. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO…
OPENING FRAME — medium-close on the written wall, eye level, straight on, locked off, ref axis; the empty plaster patch centred x=50%, its top at 62% h. START: the written wall…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.2s] START: the written wall and the empty patch, the bulb's cone raking the strokes. [2.2-4.5s] The corners of her mouth go up into a small unexplained smile, and she is already moving again — one step left, out of… [4.5-6.8s] Her right hand comes up and finds the switch without looking at it — the ordinary reflex of turning off other people's lights. [6.8-9.0s] Her fingers turn it.
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 28 mm f/1.4 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — TWO STATES, NOTHING IN BETWEEN.
SOUND — None. Nobody speaks in this generation. SFX only.
ENDING FRAME, the state this shot hands over — Pure black — no image, no glow, no silhouette, nothing.
AVOID — a drawing on the plaster, a dragon, an animal, a creature, any figure on the wall, marks on the clear patch, figure touching the wall, a frown, recognition, the bulb lit after the click.
```

## 10D-1 — plan 10.5, segment 1/2 « Le noir s'allume » *(8 s · @Nora + @RedHouseInterior v2 · start frame : AUCUN, le bloc s'ouvre sur du noir plein · 28 mm f/1.4)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 8 s |
| **Éléments** | @Nora + @RedHouseInterior |
| **`start_image`** | AUCUN, le bloc s'ouvre sur du noir plein |
| **`video_references`** | *aucune — c'est une tête de chaîne* |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — One full second of pure black, then the black lights up: the strokes she has just walked past rise slowly until the room is readable, and…
CONTINUITY — no video attached. This is the head of its chain: it sets the light, grain and skin rendering the following shots match. THE ATTACHED IMAGE IS THE FIRST FRAME — it fixes the opening composition, every body position and pose, every prop state and the camera direction; take nothing else from it, no border, no backdrop, no empty-room staging.
OPENING FRAME — wide, eye level 160 cm, middle of the room looking back toward the front door, locked off, the axis of reference IMAGE C. PURE BLACK. Nothing visible at…
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.2s] The strokes begin to come up, very low, ember red under ash, first on the two side walls she walked past; [2.2-4.3s] The whole written band of both walls is up; [4.3-6.5s] The whole written band of both walls is up;
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 28 mm f/1.4 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — TWO STATES, NOTHING IN BETWEEN.
SOUND — None. Nobody speaks in this generation. SFX only.
ENDING FRAME, the state this shot hands over — The room at mid-glow, both written walls alive in dim ember red, the ceiling still dark, @Nora a dark unmoving shape at x=50%, hand raised on…
AVOID — letters appearing one by one, writing that draws itself, strokes crawling, a light source in frame, a lamp, a torch, moonlight, the bulb relighting, bright red, neon red.
```

## 10D-2 — plan 10.5, segment 2/2 « Le plafond entier » *(8 s · @Nora + @RedHouseInterior v2 · start frame : la LAST FRAME de 10D-1 · 28 mm f/1.4)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 8 s |
| **Éléments** | @Nora + @RedHouseInterior |
| **mode** | `video_extension` · `extension_mode: forward` |
| **vidéo à prolonger** | le segment précédent |
| ⚠ | **Un seul mouvement découpé — le raccord doit être invisible.** À défaut de `video_extension` : `start_image` = la dernière frame exacte du segment précédent. |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — The camera tilts up off the standing @Nora and finds the ceiling: written corner to corner, brightest directly above the mattress, where a man lay for…
CONTINUITY — VIDEO 1 is the previous segment of this same continuous shot (10D-1) and THE CAMERA IS ALREADY MOVING at its last frame. ALIGN THE BOUNDARY FIRST: start on that motion already underway, same speed, same line, no ease-in, no restart, then carry it on. One single move across both clips.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Nora: centre of frame, STANDING, x=50%. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY:…
OPENING FRAME — wide, eye level 160 cm, middle of the room looking back toward the front door, the exact frame that ends 10D-1; one single slow tilt up, no dolly,…
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.2s] The start frame held exactly: both written walls glowing, @Nora a dark shape at x=50%, 55% h, hand raised at x=62%. The camera tilts… [2.2-4.4s] The camera tilts up 35 degrees over four seconds and a fifth, evenly, never accelerating: the tops of the walls pass, then the ceiling… [4.4-6.6s] The tilt stops on the ceiling;
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 28 mm f/1.4 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — TWO STATES, NOTHING IN BETWEEN.
SOUND — None. Nobody speaks in this generation. SFX only.
ENDING FRAME, the state this shot hands over — The written ceiling filling the frame corner to corner in dim ember red, brightest above the mattress, the stair risers and the inside of the door…
AVOID — letters appearing one by one, writing that draws itself, strokes crawling, a light source in frame, a lamp, a torch, moonlight, the bulb relighting, bright red, neon red.
```

## 10E — plan 10.6 « Son visage » *(6 s → 5 s · @Nora + @RedHouseInterior v2 · start frame : AUCUN, écart déclaré · 50 mm f/1.4)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 6 s |
| **Éléments** | @Nora + @RedHouseInterior |
| **`start_image`** | AUCUN, écart déclaré |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — The face of a who has just seen the inside of a whole house light up. 6 seconds, one continuous framing, no cut.
CONTINUITY — VIDEO 1 is the shot immediately before this one (10D-2). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the inherited state below, already true, nothing replayed, then move on. It must CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin rendering and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Nora: centre of frame, STANDING, x=50%. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY:…
OPENING FRAME — close, 90 cm from her, eye level, three-quarter, static, locked off; her face at x=48%, 78% h, the room behind her at razor-thin focus. Held as found: mouth…
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.8s] Held as found: mouth closed, eyes wide, the dim red laying a thread of highlight along one cheekbone and the lower lip, everything else… [1.8-3.6s] Her jaw drops open two centimetres and stays open. ONE tear leaves the outer corner of the right eye and runs the whole cheek… [3.6-5.4s] The corners of her mouth go up — a real smile arriving late and against the open jaw, the eyes creasing with it, one…
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 50 mm f/1.4 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — TWO STATES, NOTHING IN BETWEEN.
SOUND — None. Nobody speaks in this generation. SFX only.
ENDING FRAME, the state this shot hands over — Her face, close, in dim ember red — jaw open, one wet track down the right cheek, smiling, eyes creased, not moving. This exact frame is…
AVOID — letters appearing one by one, writing that draws itself, strokes crawling, a light source in frame, a lamp, a torch, moonlight, the bulb relighting, bright red, neon red.
```

## 10F-1 — plan 10.7, segment 1/4 « La caméra la quitte » *(5 s · @Nora + @RedHouseInterior v2 · start frame : la LAST FRAME de 10E · 28 mm f/1.4)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 5 s |
| **Éléments** | @Nora + @RedHouseInterior |
| **mode** | `video_extension` · `extension_mode: forward` |
| **vidéo à prolonger** | le segment précédent |
| ⚠ | **Un seul mouvement découpé — le raccord doit être invisible.** À défaut de `video_extension` : `start_image` = la dernière frame exacte du segment précédent. |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — The camera leaves her face, draws back across the glowing room and out through the open door, and she stays where she is — smiling, getting…
CONTINUITY — VIDEO 1 is the previous segment of this same continuous shot (10E) and THE CAMERA IS ALREADY MOVING at its last frame. ALIGN THE BOUNDARY FIRST: start on that motion already underway, same speed, same line, no ease-in, no restart, then carry it on. One single move across both clips.
OPENING FRAME — begins on the exact last frame of the previous generation, her face at x=48%, 78% h, then draws straight back at a constant 1.2 metres per second, eye…
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.5s] Her face recedes to 55% h; At [2.6s] she is 34% h at x=50%, the whole written room around her, the ceiling alight above,… [1.5-2.9s] She holds at 24% h; [2.9-4.4s] The dark door jamb sweeps in from both edges and takes 30% of frame width on each side;
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 28 mm f/1.4 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — TWO STATES, NOTHING IN BETWEEN.
SOUND — None. Nobody speaks in this generation. SFX only.
ENDING FRAME, the state this shot hands over — The open doorway seen from the porch boards, a dim red rectangle in a grey-black street, @Nora a small unmoving shape inside it, the red stopping…
AVOID — letters appearing one by one, writing that draws itself, strokes crawling, a light source in frame, a lamp, a torch, moonlight, the bulb relighting, bright red, neon red.
```

## 10F-2 — plan 10.7, segment 2/4 « La rue grise » *(5 s · @RedHouseExterior · start frame : la LAST FRAME de 10F-1 · 24 mm f/2.8)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 5 s |
| **Éléments** | @RedHouseExterior |
| **mode** | `video_extension` · `extension_mode: forward` |
| **vidéo à prolonger** | le segment précédent |
| ⚠ | **Un seul mouvement découpé — le raccord doit être invisible.** À défaut de `video_extension` : `start_image` = la dernière frame exacte du segment précédent. |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — The camera keeps going: back down the grey street @Nora climbed, the red doorway shrinking to a warm point, and the ground begins to fall away.…
CONTINUITY — VIDEO 1 is the previous segment of this same continuous shot (10F-1) and THE CAMERA IS ALREADY MOVING at its last frame. ALIGN THE BOUNDARY FIRST: start on that motion already underway, same speed, same line, no ease-in, no restart, then carry it on. One single move across both clips.
OPENING FRAME — begins on the exact last frame of the previous generation, the open red doorway at x=50%, and draws straight back down the middle of the road at a…
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.3s] The doorway shrinks to 20% h; A sodium lamp passes overhead at [2.0s]; [1.3-2.7s] The camera is level with the first-floor windows; [2.7-4.0s] The camera is level with the first-floor windows;
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 24 mm f/2.8 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — STATE A · THE WINDOW LIT, THE DOOR SHUT (the arrival).
SOUND — None. Nobody speaks in this generation. SFX only.
ENDING FRAME, the state this shot hands over — Roof slates and chimney stacks across the lower half of frame, the black channel of the street between them, the red doorway a dim point far…
AVOID — people in the street, figure, a man, a car moving, red on the road, red on the walls, the camera stopping or accelerating, drone propeller sound, readable words, legible handwriting.
```

## 10F-3 — plan 10.7, segment 3/4 « La verticale » *(5 s · aucun personnage · start frame : la LAST FRAME de 10F-2 · 24 mm f/2.8)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 5 s |
| **Éléments** | aucun — ce plan ne charge aucun Élément |
| **mode** | `video_extension` · `extension_mode: forward` |
| **vidéo à prolonger** | le segment précédent |
| ⚠ | **Un seul mouvement découpé — le raccord doit être invisible.** À défaut de `video_extension` : `start_image` = la dernière frame exacte du segment précédent. |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — The camera leaves the street behind and rises straight up until the town is nothing but a scatter of orange grains in a black landscape. 5…
CONTINUITY — VIDEO 1 is the previous segment of this same continuous shot (10F-2) and THE CAMERA IS ALREADY MOVING at its last frame. ALIGN THE BOUNDARY FIRST: start on that motion already underway, same speed, same line, no ease-in, no restart, then carry it on. One single move across both clips.
OPENING FRAME — begins on the exact last frame of the previous generation and climbs straight up at a constant 9 m/s, tilting down 20 degrees evenly across the segment so…
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.3s] Roofs, chimney stacks and the black channel of the street directly below, filling the frame. The roofs fall away; [1.3-2.7s] Very high: the town is a grid of orange grains in a black landscape, the horizon entering the top of frame. [2.7-4.0s] Very high: the town is a grid of orange grains in a black landscape, the horizon entering the top of frame.
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 24 mm f/2.8 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — Available light only: sodium lamps below, going from lights to grains as the camera rises, and a lighter…
SOUND — None. Nobody speaks in this generation. SFX only.
ENDING FRAME, the state this shot hands over — The town small and even and very far below: slate roofs, black streets, sodium grains, the sky a lighter black with no stars.
AVOID — red anywhere, a red roof, a red light, city lights bright enough to read, a lit sign, moon, stars, drone propeller sound, the camera rolling, the camera hovering.
```

## 10F-4 — plan 10.7, segment 4/4 « La redescente sur l'abribus » *(5 s · @SamSDF + @BusShelter · start frame : AUCUN ; cible visuelle : LIEU-14 IMAGE 3 · 24 mm f/2.8)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 5 s |
| **Éléments** | @SamSDF + @BusShelter |
| **mode** | `video_extension` · `extension_mode: forward` |
| **vidéo à prolonger** | le segment précédent |
| ⚠ | **Un seul mouvement découpé — le raccord doit être invisible.** À défaut de `video_extension` : `start_image` = la dernière frame exacte du segment précédent. |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — Kilometres away from the red house, the camera comes down out of the air and settles on a bus shelter, where a man sits alone on…
CONTINUITY — VIDEO 1 is the previous segment of this same continuous shot (10F-3) and THE CAMERA IS ALREADY MOVING at its last frame. ALIGN THE BOUNDARY FIRST: start on that motion already underway, same speed, same line, no ease-in, no restart, then carry it on. One single move across both clips.
OPENING FRAME — high above the town, descending on one straight line at a constant 11 m/s, tilting up 15 degrees evenly to level out, coming to rest at 12 m;…
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.4s] The high town, orange grains on black, one grain isolating itself near frame centre. Descending: the grains resolve into lamps; [1.4-2.8s] Descending: the grains resolve into lamps; [2.8-4.2s] Down onto it: a bus shelter under one sodium lamp, its light box blank and lit, and a man seated on the bench, small,…
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 24 mm f/2.8 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — one source only: a single sodium street lamp on a column above the shelter, the column out of…
SOUND — None. Nobody speaks in this generation. SFX only.
ENDING FRAME, the state this shot hands over — The shelter at rest in its sodium cone, the seated man a dark shape on the bench with his head down, the blank light box lit…
AVOID — the man's face, his eyes, the man looking up, the man standing, a readable face at distance, red anywhere, tail lights, a traffic light, lettering on the light box, a bus.
```

## 10H — plan 10.8 « Les doigts, et les yeux » *(10 s → 6 s au montage · @SamSDF + @Sam + @BusShelter (LIEU-14) · Genre Drama · Camera Fine Film · 21:9 · 1080p · sound on · 85 mm f/2 · pas de start frame)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @SamSDF + @Sam + @BusShelter |
| **`start_image`** | aucune — ce plan démarre sans image de départ |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — A homeless man alone under sodium puts down a half-eaten sandwich, pushes his beanie back, wipes one cheek; his hands fill the frame half a second…
CONTINUITY — VIDEO 1 is the shot immediately before this one (10F-4). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the inherited state below, already true, nothing replayed, then move on. It must CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin rendering and camera behaviour. DO NOT TAKE its framing.
OPENING FRAME — Medium close, three-quarter from his left, camera 105 cm high, 1.6 m away, static, locked off. He fills 70% of frame height at x=44%, clouded glass behind, sodium…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.9s] Held until described otherwise: seated, head down toward his knees, hood up and pulled far forward, beanie low under it, the packet in his… [1.9-3.8s] His right hand WIPES ONE CHEEK with the rag, once, slowly, cheekbone down into the beard — the grime lifting in a band, the… [3.8-5.7s] Both hands lie open on his knees, palms down, motionless but living — fingers settling a millimetre, a thumb pressing and releasing. Head down… [5.7-7.6s] THE HEAD LIFTS — slowly, evenly, one unbroken movement, the chin coming up off the chest — and THE EYES COME INTO THE SODIUM…
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 85 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — one source only: a single sodium street lamp on a column above the shelter, the column out of…
SOUND — None. Nobody speaks in this generation. He does not speak, does not sigh theatrically, does not sob. SFX only.
ENDING FRAME, the state this shot hands over — The bearded man alone on the bench under the sodium cone, head fully lifted, pale grey-blue eyes wide open in the orange light, looking up the…
AVOID — a false beard, a glued-on beard, a prosthetic beard, a beard being pulled off, a wig, a disguise being removed, any other person in frame, figure, a vehicle, headlights.
```

## 10I — montage 10.9, micro-plans **a + b + f + h** « SA PROPRE MAISON » *(14 s de rushes → 7,5 s au montage · @Sam + @Nora + @Mender + @NoraBedroom + @Kitchen + @Bathroom · 50 mm f/2 · start frame du shot 1 : **LA LAST FRAME DE LA GÉNÉRATION 4A** — LIEU-08 IMAGE 2, « LE CADRE DU PÈRE »)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 14 s |
| **Éléments** | @Sam + @Nora + @Mender + @NoraBedroom + @Kitchen + @Bathroom |
| **`start_image`** | du shot 1 : **LA LAST FRAME DE LA GÉNÉRATION 4A** — LIEU-08 IMAGE 2, « LE CADRE DU PÈRE » |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — Four moments in one house, cut hard together.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (10H), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — The locked frame of the reference start image: a near-black hallway at night, camera 160 cm high, 2.8 m from the door, axis 10 degrees off the wall.…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-3.0s] EXACTLY the reference frame, no movement of any kind: inside the warm band at x=39%, @Nora curled on her side 2.5 m beyond the… [3.0-6.0s] HIS RIGHT HAND LIFTS toward the door — the back of the hand catching the light, THE FINGERS COMPLETELY CLEAN, no ink, no stain… [6.0-9.0s] THE PEN RUNS: one unbroken stroke drawn slowly across the weave left to right, the ivory ink laying down wet and catching the lamp,… [9.0-12.0s] THE COATED BACK IS ALREADY IN FRAME AND ALREADY MOVING, large — no entrance, no start-up: at x=52%, filling 76% of frame height, seen…
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — Shot 1: one source, the warm sodium-orange band escaping the door gap; it dies within a metre and…
SOUND — None. Nobody speaks in this generation, at any moment, in any shot. No whisper, no call, no name. SFX only.
ENDING FRAME, the state this shot hands over — The empty near-black hallway seen from the bedroom end, the far corner at x=24% with one thin thread of sodium orange on the wall, the unseen…
AVOID — the father's face, his face lit, light on his eyes, his eyes, his eyebrows, any part of his face above the upper lip, a second light source in the hallway, figure turning toward the door, figure sitting up, figure seeing anyone.
```

## 10J — montage 10.9, micro-plans **c + d + e + g** « DEHORS » *(19 s de rushes → 9,5 s au montage · @Sam + @Anna + @Mei + @Fatiha + @Asha + @Mender + @RedHouseInterior v2 + @AnnaKitchen + @Restaurant + @LibraryCorridor · 28 mm f/1.4 sh.1-2, 50 mm f/2 sh.3-5 · start frames : **IMAGE E v2** (sh.1) · **IMAGE A v2** (sh.2) · LIEU-06 IMAGE 5 (sh.3) · LIEU-07 IMAGE 5 (sh.4) · LIEU-11 IMAGE 3 (sh.5))*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 19 s |
| **Éléments** | @Sam + @Anna + @Mei + @Fatiha + @Asha + @Mender + @RedHouseInterior + @AnnaKitchen + @Restaurant + @LibraryCorridor |
| **`start_image`** | **IMAGE E v2** (sh.1 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — A man lays the first stroke of dark red on a bare wall and steps back to measure what it will cost.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (10I), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Sam: centre of frame, STANDING, x=58%, filling 74% of frame height. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE,…
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — Wide, camera at eye level 155 cm, 3 m back from the wall, static, locked off, the whole height of the room in frame. @Sam at x=40%, filling…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-4.3s] He stands facing the bare wall, hands empty; The brush comes off, his arm lowers, HE TAKES ONE STEP BACKWARDS and stops; [4.3-8.6s] The last white disappears under the red; ONE FULL BEAT OF DARK, only his breathing and the doorway's weak grey behind him. [8.6-12.9s] BROAD DAYLIGHT, the stove unlit. SHE LISTENS TO THE END, then NODS — once slowly, and again smaller — her eyes steady on him,… [12.9-17.2s] THE COAT IS ALREADY IN FRAME AND ALREADY MOVING — no entrance, no start-up: a tall figure seen from DIRECTLY BEHIND at x=48%, filling…
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 28 mm f/1.4 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — TWO STATES, NOTHING IN BETWEEN.
SOUND — None audible. Sam's jaw works in shots 3 and 4 and the women answer only with their heads; NOT ONE SOUND OF SPEECH IS GENERATED — no voice,…
ENDING FRAME, the state this shot hands over — The library service corridor, the grey window at its far end: a tired heavy man in a plain grey jacket, three-quarter back to camera, walking away…
AVOID — the man's face, his profile, his eyes, him turning toward camera, a face above the coat's collar, the coat pausing or turning back, readable handwriting, legible letters on the walls, readable words anywhere, readable menus.
```

## 10K — plan 10.10 « L'hôpital, enfin sonore » *(8 s · CADRE RÉFÉRENT ABSOLU · @MaeveIll + @SamBefore + @HospitalCorridor (LIEU-05) + @HospitalRoom (LIEU-04) · 50 mm f/2 · start frame : LIEU-05 IMAGE 3)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 8 s |
| **Éléments** | @MaeveIll + @SamBefore + @HospitalCorridor + @HospitalRoom |
| **`start_image`** | LIEU-05 IMAGE 3 |
| **`video_references`** | *aucune — c'est une tête de chaîne* |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — Through the glass of a hospital room door: a dying woman takes her husband's face in both her hands, will not let go of it, and…
CONTINUITY — no video attached. This is the head of its chain: it sets the light, grain and skin rendering the following shots match. THE ATTACHED IMAGE IS THE FIRST FRAME — it fixes the opening composition, every body position and pose, every prop state and the camera direction; take nothing else from it, no border, no backdrop, no empty-room staging.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — Medium shot through the wired-glass door window, eye level from the corridor, static, locked off. The framing, camera height and off-centre crop never change by a single pixel.…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.9s] Starting positions, held until described otherwise, all seen through the glass: @MaeveIll sitting up, three-quarter facing camera-left at x=54% inside the pane, filling 46%… [1.9-3.9s] Nobody moves. [3.9-5.8s] His shoulders go once — a single shake — and the light catches wet on his cheek. SHE GRIPS HARDER, the fingers pressing into… [5.8-7.7s] HIS MOUTH OPENS — the jaw comes down, the lips part on a word — AND NOTHING COMES OUT. He nods, slowly, inside her…
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — Corridor side: cold green fluorescent tubes overhead behind the camera, even and shadowless, their reflections lying across the…
SOUND — Two lines, spoken by @MaeveIll only, in English, exactly as written, nothing added, nothing paraphrased: SFX only.
ENDING FRAME, the state this shot hands over — ⚠ ABSOLUTE REFERENCE FRAME — through the wired glass, her two hands holding his face with the thumbs on his cheekbones, her eyes on his, his…
AVOID — the man speaking, any male voice, a whisper from him, him wiping his face, his hands rising to hers, her hands leaving his face or coming down, more than two nods, him standing, him turning toward the door, a chair in frame.
```

## 10L — plan 10.11 **LE DERNIER PLAN DU FILM** « Il lève les yeux, et il sourit » *(8 s de rushes → 6 s au montage · @SamSDF + @Sam + @BusShelter · UNE SEULE PRISE, caméra fixe · 85 mm f/2 · pas de start frame)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 8 s |
| **Éléments** | @SamSDF + @Sam + @BusShelter |
| **`start_image`** | aucune — ce plan démarre sans image de départ |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — A heavy homeless man alone on a bus shelter bench under sodium, his face already wiped in lighter streaks.
CONTINUITY — VIDEO 1 is the shot immediately before this one (10H). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the inherited state below, already true, nothing replayed, then move on. It must CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin rendering and camera behaviour. DO NOT TAKE its framing.
OPENING FRAME — Close, straight on, camera 110 cm high, 1.1 m away, locked off, ONE TAKE WITH NO CUT AND NO REFRAMING. His head at x=48%, filling 64% of frame…
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.9s] Start positions, held until described otherwise: SEATED, bare-headed, hood back off his head, the beanie shut in his left fist on his knee, his… [1.9-3.9s] A LONG BEAT, and nothing else happens: he holds the sky, breathing, two slow blinks, the jaw loose. [3.9-5.8s] THE CORNERS OF THE MOUTH GO UP AND DO NOT COME DOWN AGAIN — a small, uneven, involuntary smile that stays.
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 85 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — one source only: a single sodium street lamp on a column above the shelter, the column out of…
SOUND — None. Nobody speaks; he does not sob aloud, does not whisper, does not say a name. SFX only.
ENDING FRAME, the state this shot hands over — The bearded man alone on the bench under the sodium cone, bare-headed, the beanie shut in his left fist on his knee, his face wiped in…
AVOID — a false beard, a glued-on beard, a prosthetic beard, a beard being pulled off, a mask, a wig, a disguise being removed, anything peeling from the face, a glue line, the beanie thrown away or left on the bench.
```
