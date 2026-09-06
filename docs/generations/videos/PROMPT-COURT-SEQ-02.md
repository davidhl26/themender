# PROMPTS COURTS — SÉQUENCE 02

> ~300 mots par plan, l'ordre recommandé par Higgsfield et ByteDance.
> Le détail complet reste dans `PRET-SEQ-02.md` : géométrie GEO, verrous, raccords numérotés.
> **C'est CETTE version qu'on colle dans Higgsfield.** L'autre est le document de tournage.

## 2A — plan 2.1 « Le quai, et le gobelet » *(12 s de rushes → 4 s au montage · Elements : @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @Quay · start frame : LIEU-02 IMAGE 1)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 12 s |
| **Éléments** | @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @Quay |
| **`start_image`** | LIEU-02 IMAGE 1 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — A family of four walks a quay toward dinner at sunset; an old man sits on the ground against a wall with a cardboard cup and…
CONTINUITY — VIDEO 1 is an earlier shot of the same film (1D), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — CAMERA: wide, eye level about 160 cm, operated and breathing, carried rather than nailed down, looking along the quay into the low sun — exactly the axis of…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.6s] Frame contents, nobody moving through it yet: the quay in low golden sunset, stacked traps lower right, the brick wall along the left, masts… [2.6-5.3s] MOVEMENT: the family enters at the left frame edge and walks screen-left to screen-right, unhurried, mid-ground, filling 45% of frame height — @SamBefore first,… [5.3-7.9s] Starting positions, held until described otherwise: THE SEATED MAN screen-left at x=30%, SEATED, back against the brick, filling 45% of frame height, blanket over… [7.9-10.6s] Her mouth goes up at one corner first and the smile reaches her eyes, the way it does for someone already known.
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 40 mm f/2.8 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — one source only: the low sun of the end of a clear day, a hand's width above the…
SOUND — None. Nobody speaks in this generation — @MiloBefore's babble stays indistinct, with no intelligible word in it. SFX only.
ENDING FRAME, the state this shot hands over — @Maeve standing straight over the seated man, her smile landing on his upturned, fully lit face, the coins and the folded bill in the beige cup,…
AVOID — any red other than the crimson wool scarf on @Maeve, red buoys, red hulls, red traps, a beard on the seated man, a broad or heavy build on the seated man, his face hidden or in shadow, the seated man standing, begging, reaching or speaking.
```

## 2B — plan 2.2 « Donne, et tu recevras » *(14 s de rushes → 6 s au montage · Elements : @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @Quay · start frame : LIEU-02 IMAGE 3)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 14 s |
| **Éléments** | @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @Quay |
| **`start_image`** | LIEU-02 IMAGE 3 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — Walking on toward dinner, a challenges her mother for giving money to a stranger; the mother answers in four unhurried words.
CONTINUITY — VIDEO 1 is the shot immediately before this one (2A). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the inherited state below, already true, nothing replayed, then move on. It must CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin rendering and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @SamBefore: centre of frame, x=60%. @Maeve: centre of frame, x=55%. @NoraBefore: right third of frame, x=80%. Nothing in this list may be re-placed, re-lit or improved.…
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — CAMERA: medium-close two-shot, eye level about 155 cm, operated and breathing, carried rather than nailed down, placed ahead of them on the walkway with the low sun directly…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-3.0s] Starting positions, held until described otherwise: @Maeve at x=44% and @NoraBefore at x=58%, chest-up, filling 45% of frame height, mid-ground, side by side, WALKING… [3.0-6.1s] She turns back to her mother and speaks, flat, half a challenge: "You don't even know him." Her answer, without turning her head, worn… [6.1-9.1s] A beat — the longest of the scene. [9.1-12.2s] Frame contents: the sunset gone, sky and wet concrete settled into an even luminous blue; MOVEMENT: the shopfront window flickers and comes alight —…
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 40 mm f/2.8 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — one source only: the low sun of the end of a clear day, a hand's width above the…
SOUND — [3.4-4.6s] @NoraBefore, flat, half a challenge: "You don't even know him." [5.2-6.6s] @Maeve, not turning her head, worn smooth by habit: "Give and you shall receive." [7.3-8.2s] @NoraBefore,…
ENDING FRAME, the state this shot hands over — The lit shopfront amber in the luminous blue dusk, the family small and almost at the door with their backs three-quarter to camera, @MiloBefore up on…
AVOID — any red other than the crimson wool scarf on @Maeve, red buoys, red hulls, a red shopfront, a readable sign, letters on the shopfront, readable signage, on-screen text, subtitles, captions.
```

## 2C — plan 2.3 « Les quatre assiettes » *(8 s de rushes → 4 s au montage · Elements : @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @Mei + @Restaurant + @GreenBandPlate · start frame : LIEU-07 IMAGE 2)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 8 s |
| **Éléments** | @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @Mei + @Restaurant + @GreenBandPlate |
| **`start_image`** | LIEU-07 IMAGE 2 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — The owner of a small harbour restaurant carries four plates to a family's table and sets them down one to each person, without being asked and…
CONTINUITY — VIDEO 1 is an earlier shot of the same film (2B), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Maeve: centre of frame, x=44%. @NoraBefore: centre of frame, x=58%, filling 45% of frame height. Nothing in this list may be re-placed, re-lit or improved. THIS…
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — CAMERA: medium on the table from the back of the room, eye level about 150 cm, operated and breathing, carried rather than nailed down, exactly the axis of…
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.4s] Starting positions, held until described otherwise: the table by the half-fogged window, the blue night behind the glass across the upper half of frame.… [2.4-4.8s] @Mei smiles at the family and trades two silent words with @Maeve — lips moving, nothing audible — then straightens, one hand flat on… [4.8-7.2s] MOVEMENT: she withdraws screen-left toward the beaded curtain, unhurried, and passes out of frame at x=8%.
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — amber-and-brass paper lanterns hung low over the tables are the key: they hang above the window table and…
SOUND — None. Nobody speaks in this generation. The two words @Mei trades with @Maeve are silent — lips moving, nothing audible. SFX only.
ENDING FRAME, the state this shot hands over — The family table from the back of the room: the four seated, the FOUR green-rimmed plates set one in front of each of them on the…
AVOID — three plates, five plates, duplicated plates, a plate moved after it is set, anyone reaching for a plate, anyone eating, food on the plates, a menu, a readable menu, readable signage.
```

## 2D — plan 2.4 « Le dragon au thé » *(14 s de rushes → 7 s au montage · Elements : @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @Restaurant + @GreenBandPlate · start frame : LIEU-07 IMAGE 2, état « later »)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 14 s |
| **Éléments** | @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @Restaurant + @GreenBandPlate |
| **`start_image`** | LIEU-07 IMAGE 2, état « later » |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — Much later in the evening, the little @MiloBefore has fallen asleep against his mother; the father dips a wooden chopstick in his tea and draws on…
CONTINUITY — VIDEO 1 is the shot immediately before this one (2C). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the inherited state below, already true, nothing replayed, then move on. It must CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin rendering and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @SamBefore: left third of frame, SEATED, x=26%, filling 50% of frame height. @Maeve: centre of frame, SEATED, x=44%. @MiloBefore: centre of frame, SEATED, x=60%. @NoraBefore: right…
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — CAMERA: one single continuous take, no cut. A medium three-quarter across the table, lens about 60 cm above the tabletop and 1.2 m back from the paper, on…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-3.4s] Starting positions, held until described otherwise: the white paper top crosses the lower third of frame. MOVEMENT: he draws on the white paper top… [3.4-6.7s] MOVEMENT: the tip goes back to the cup, takes its ink of tea, and returns to the paper. @NoraBefore speaks to her mother without… [6.7-10.1s] Her look leaves her daughter, travels to her husband's bent back and hand, and stays there a beat longer than a look needs to… [10.1-13.4s] MOVEMENT: the tip goes back to the cup, takes its ink of tea, and returns to the paper.
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — amber-and-brass paper lanterns hung low over the tables are the key: they hang above the window table and…
SOUND — [6.2-7.9s] @NoraBefore, to her mother, without taking her eyes off her father's hand, quiet and matter-of-fact: "I love Daddy's stories." That is the only line in this generation.…
ENDING FRAME, the state this shot hands over — The wider frame after the camera has stopped: the four of them at the table in the lantern amber — @SamBefore screen-left bent over the paper,…
AVOID — a recognizable dragon, a readable drawing, a legible picture on the paper, a finished illustration, letters, legible handwriting, ink, an inkwell, a pen, a pencil.
```
