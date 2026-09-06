# PROMPTS COURTS — SÉQUENCE 04

> ~300 mots par plan, l'ordre recommandé par Higgsfield et ByteDance.
> Le détail complet reste dans `PRET-SEQ-04.md` : géométrie GEO, verrous, raccords numérotés.
> **C'est CETTE version qu'on colle dans Higgsfield.** L'autre est le document de tournage.

## 4A — plan 4.1 « Le cadre du père » *(10 s de rushes → 8 s au montage · Elements : @Nora + @NoraBedroom · start frame : LIEU-08 IMAGE 2, composition VERROUILLÉE)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @Nora + @NoraBedroom |
| **`start_image`** | LIEU-08 IMAGE 2, composition VERROUILLÉE |
| **`video_references`** | *aucune — c'est une tête de chaîne* |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — Night.
CONTINUITY — no video attached. This is the head of its chain: it sets the light, grain and skin rendering the following shots match. THE ATTACHED IMAGE IS THE FIRST FRAME — it fixes the opening composition, every body position and pose, every prop state and the camera direction; take nothing else from it, no border, no backdrop, no empty-room staging.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — One single locked shot.
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.7s] Starting position, held until described otherwise: @Nora LYING inside the band at x=39%, curled on her side on the bed roughly 2.5 m beyond the door, filling 24% of frame height, seen three-quarter from behind and above the shoulder line, her face half buried in the pillow and unreadable, both hands drawn up near it. [2.7-5.5s] THE WORD. [5.5-8.2s] Nothing answers.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — motivated sources only, never more than two lit at once, and the two temperatures never mix.
SOUND — [4.4-5.6s] @Nora, into the pillow, barely voiced, broken, on an exhale, not addressed to anyone in the house: "Why?" — Nobody answers.
ENDING FRAME, the state this shot hands over — The identical locked composition: the near-black hallway, the left jamb, the narrow warm sodium band through the half-open door with the curled @Nora inside it, the dark face of the door, and the black wall running to the right frame edge about 60 cm past the jamb — nobody in the hallway, nothing added, nothing moved.
AVOID — a second person, a man in the hallway, a silhouette, a shadow crossing the light band, a hand at the frame edge, a sleeve, a shoulder, a watcher, anyone entering, anyone leaving.
```

## 4B — plans 4.2 + 4.3 « L'accueil, et l'entrée dans le dessin » *(15 s de rushes → 10 s au montage · Elements : @Nora + @Anna + @AnnaKitchen + @AnnaDrawing · start frame : LIEU-06 IMAGE 2)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 15 s |
| **Éléments** | @Nora + @Anna + @AnnaKitchen + @AnnaDrawing |
| **`start_image`** | LIEU-06 IMAGE 2 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — Another night.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (4A), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Nora: centre of frame, LYING, x=39%. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY: whatever brought the bodies and the props here has already happened in the attached video and must NOT be performed again.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Medium wide from inside the kitchen, standing eye level about 160 cm, static, locked off, facing the room's doorway: the doorway left of centre with its frame worn to bare wood at hand height, opened on darkness beyond;
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-3.2s] Starting positions, held until described otherwise: the doorway empty and black at x=34%. [3.2-6.5s] Starting positions: @Anna SEATED in profile at x=26%, filling 66% of frame height, facing screen-right. @Anna does not look up. [6.5-9.8s] @Nora sits down, the chair taking her weight with a small dry sound; [9.8-13.0s] Starting positions: the drawing flat and unfolded at frame centre, its two fold lines standing very slightly proud.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — two practical sources only, both very low, in the drained grey-blue AFTER world about two thirds of a stop under normal, no red anywhere, flames included: the bulb over THE OILCLOTH TABLE lays a small gold pool on the cloth and models from above with hard shadow in the eye sockets, and where the frame comes down onto the table it rakes the surface at an angle rather than flattening it, so grain and fibre stand up;
SOUND — [12.2-13.0s] @Anna, from above the frame line, low and worn with a faint Russian accent, about two and a half words a second, flat, no lift on either sentence, a real pause between them: "I had a son.
ENDING FRAME, the state this shot hands over — The pencil hatching filling the frame edge to edge — no paper edge, no table, no cup, no hand, nobody: only rows of grey graphite strokes lying across the fibre of yellowed paper, the fibre itself risen through them, the strokes soft-focused at their tips and never resolving into a readable letter.
AVOID — anyone pouring tea, a kettle being lifted, a cup being filled or carried in, the stove being lit, a match, a lighter, an open flame in frame, saturated embers, red, bright red.
```

## 4C — plans 4.4 + 4.5 « Kolya, et la raison » *(15 s de rushes → 15 s au montage · Elements : @Nora + @Anna + @AnnaKitchen + @AnnaDrawing · start frame : la DERNIÈRE IMAGE DE LA GÉNÉRATION 4B — les hachures pleine image — réexportée et rechargée telle quelle)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 15 s |
| **Éléments** | @Nora + @Anna + @AnnaKitchen + @AnnaDrawing |
| **`start_image`** | la DERNIÈRE IMAGE DE LA GÉNÉRATION 4B — les hachures pleine image — réexportée et rechargée telle quelle |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — The camera comes back up out of a pencil drawing onto the table it lies on.
CONTINUITY — VIDEO 1 is the shot immediately before this one (4B). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the INHERITED STATE line below, already true, nothing replayed, then move on. CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Anna: centre of frame, SEATED, x=48%, filling 66% of frame height. @Nora: right third of frame, STANDING, x=72%, filling 74% of frame height. Nothing in this list may be re-placed, re-lit or improved.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Macro plumb down over the table, camera directly above the drawing, opening at the exact magnification of the incoming frame — grey pencil hatching filling the frame edge to edge — then a slow straight pull-back, plumb, no pan, no tilt, no rotation, coming to rest at about 60 cm above the sheet and locking there.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-3.5s] The pull-back: the strokes shrink and gather, the two fold lines come in from the sides, the sheet's foxed edge appears, then the worn oilcloth around it, then at the top of frame @Anna's two swollen hands closed around her cup, the thin worn gold band on one finger — her right thumb still resting on the paper, but stopped now. [3.5-7.1s] Starting position: @Anna SEATED, both hands closed around her cup on the table in front of her, eyes down on the drawing out of frame below, not on @Nora. [7.1-10.6s] Starting positions: @Nora's cup stopped in mid-air, ten centimetres below her mouth, held there. [10.6-14.2s] A held beat: nobody moves, @Nora's cup still up, the steam long gone from it.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 85 mm f/2 equivalent.
LIGHT — two practical sources only, both very low, in the drained grey-blue AFTER world about two thirds of a stop under normal, no red anywhere, flames included: the bulb over THE OILCLOTH TABLE lays a small gold pool on the cloth and models from above with hard shadow in the eye sockets, and where the frame comes down onto the table it rakes the surface at an angle rather than flattening it, so grain and fibre stand up;
SOUND — [3.1-4.0s] @Anna, from above the frame line, low and worn with a faint Russian accent, the breath going out from under the word so it comes half unvoiced: "Kolya." [6.1-7.1s] @Anna, on camera, quiet, plain, closing something, about two words a second: "She heard me." [8.6-11.0s] @Anna, on camera, flat, no lift, a real stop between the sentences, about two and a half words a second: "He explained nothing.
ENDING FRAME, the state this shot hands over — Across the table at seated eye level: @Anna sharp at x=62%, both hands around her cup, eyes down on the drawing, the tears still standing on her lids and never wiped;
AVOID — flashback imagery, memory superimposition, figure, a hospital, a corridor, a coat, ghostly figures, dream haze, white flash transition, spiral transition.
```

## 4D — plans 4.6 + 4.7 « He hears you, et trente ans en une image » *(15 s de rushes → 13 s au montage · Elements : @Nora + @Anna + @AnnaKitchen · start frame : LIEU-06 IMAGE 5)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 15 s |
| **Éléments** | @Nora + @Anna + @AnnaKitchen |
| **`start_image`** | LIEU-06 IMAGE 5 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — @Nora asks an old woman where to find someone, and gets an answer that is not an address.
CONTINUITY — VIDEO 1 is the shot immediately before this one (4C). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the INHERITED STATE line below, already true, nothing replayed, then move on. CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Anna: centre of frame, SEATED, x=62%, filling 58% of frame height. @Nora: left third of frame, SEATED, x=22%. Nothing in this list may be re-placed, re-lit or improved.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Two-shot square to the table's long side, seated eye level about 115 cm, static, locked off: the two mismatched chairs facing each other in profile at the left and the right of frame, the small table between them, the stove's amber grate a soft glow in the background at screen-right, the dresser soft behind the table, the bulb dropping its small gold pool onto the centre of the oilcloth.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-3.4s] Starting positions, held until described otherwise: @Anna SEATED in profile at x=26%, filling 66% of frame height, facing screen-right, both hands around her cup on the cloth. [3.4-6.8s] THE ANSWER, in two parts with a real stop between them; Neither of them adds anything. [6.8-10.2s] Her right hand comes up and takes the near upright of the door frame — the fingers closing across the pencil marks without seeing them — she steps through, and THE HAND LEAVES THE WOOD and goes out of frame with her. [10.2-13.6s] THE ONLY FOCUS MOVE OF THE SHOT: the focus travels slowly off the upright and back to the far wall, the pencil marks softening away — and the line above the stove comes up sharp: eight small odd mittens hanging in the amber, swaying a millimetre or two in the stove's rising heat, not one of them matching another.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 85 mm f/2 equivalent.
LIGHT — two practical sources only, both very low, in the drained grey-blue AFTER world about two thirds of a stop under normal, no red anywhere, flames included: the bulb over THE OILCLOTH TABLE lays a small gold pool on the cloth and models from above with hard shadow in the eye sockets, and where the frame comes down onto the table it rakes the surface at an angle rather than flattening it, so grain and fibre stand up;
SOUND — [1.3-2.6s] @Nora, plain, quiet, no hope in it, about two and a half words a second: "Where do I find him?" [3.9-5.6s] @Anna, low and worn with a faint Russian accent, in two parts with a real stop between them, the second part simply stated with no lift and no emphasis: "You don't find him." then "He hears you." — Nobody else speaks.
ENDING FRAME, the state this shot hands over — The kitchen with nobody in it: the near upright of the door frame at frame left gone soft, the black doorway beside it, and sharp at frame right the taut line above the cast-iron stove with its eight small odd mittens hanging in the amber, no two alike, swaying a millimetre in the rising heat — the grate glowing low behind them, the corners of the room lost in deep warm shadow.
AVOID — names beside the pencil marks, words on the door frame, letters, digits, dates, height chart numbers, a written name, legible handwriting, readable words anywhere, a monogram on a mitten.
```

## 4E — micro-plans **4.3a + 4.3b + 4.3c** « L'hôpital, du côté d'Anna » *(10 s de rushes → 7 s au montage · Elements : @AnnaYoung + @Kolya11 + @WardDoctor + @RussianHospitalWard + @RussianHospitalCorridor · **Lens Anamorphic 85 mm f/2 — PAS 50 mm, voir la note « LE RACCORD AU PIXEL »** · start frame : LIEU-17 IMAGE 4 ; l'IMAGE 2, ANGLE A, est l'axe des shots 2 et 3)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @AnnaYoung + @Kolya11 + @WardDoctor + @RussianHospitalWard + @RussianHospitalCorridor |
| **`start_image`** | LIEU-17 IMAGE 4 ; l'IMAGE 2, ANGLE A, est l'axe des shots 2 et 3 |
| **`video_references`** | *aucune — c'est une tête de chaîne* |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — A woman sits by her son's hospital bed and his fingers loosen out of her hand one by one;
CONTINUITY — no video attached. This is the head of its chain: it sets the light, grain and skin rendering the following shots match. THE ATTACHED IMAGE IS THE FIRST FRAME — it fixes the opening composition, every body position and pose, every prop state and the camera direction; take nothing else from it, no border, no backdrop, no empty-room staging.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Tight medium from the open doorway of @Kolya11's room, compressed flat by the long lens, standing eye level, camera about 155 cm high, static, locked off.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.3s] Starting positions, held until described otherwise: @Kolya11 LYING at x=52%, his head on the dented pillow at x=44%, his face filling 34% of frame height, three-quarter to camera, mouth slightly open, one thin strand of hair stuck flat to his forehead; [2.3-4.5s] Her hand closes on nothing. [4.5-6.8s] Ten metres away, mid-frame, the LAST room door on SCREEN LEFT opens inward and @WardDoctor steps out into the corridor at x=46%, sharp, compressed flat by the lens, filling 55% of frame height, and stops one step clear of the door frame. [6.8-9.1s] SHE SCREAMS ONE NAME.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 85 mm f/2 equivalent.
LIGHT — the run of bare fluorescent tubes in their shallow enamel troughs is the only source inside the corridor: cold, even, and so pallid it drains the tile of its colour, falling vertically from directly overhead onto the top of everything in frame, never from the side, and from just above and slightly behind the lens wherever the lens rides low near the floor;
SOUND — None. Nobody speaks in this generation. The only human sound in it is one screamed name, without words. SFX only.
ENDING FRAME, the state this shot hands over — The glazed eau-de-nil tiled wall filling most of the frame, and down it the wide smeared track of breath-damp left by a dragged flat hand — and low at the bottom edge, from behind and close, the top of @AnnaYoung's back and her low flat grey-streaked bun where she has come to rest kneeling against the tiles, still moving with what is left of her breath;
AVOID — bright red, saturated red, red cross, red crescent, fire extinguisher, red blanket, red-brown stain on the floor, red-brown stain on the walls, rust streaks reading as blood, warning colour.
```

## 4F — micro-plans **4.3d + 4.3f + 4.3g** « Le brancard » *(10 s de rushes → 7,5 s au montage · Elements : @YoungMotherHospital + @WardDoctor + @RussianHospitalCorridor · start frame : LIEU-17 IMAGE 1, le master ; l'IMAGE 5, ANGLE D, est l'axe du shot 2)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @YoungMotherHospital + @WardDoctor + @RussianHospitalCorridor |
| **`start_image`** | LIEU-17 IMAGE 1, le master ; l'IMAGE 5, ANGLE D, est l'axe du shot 2 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — The same night, in the same corridor.
CONTINUITY — VIDEO 1 is the shot immediately before this one (4E). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the INHERITED STATE line below, already true, nothing replayed, then move on. CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Kolya11: centre of frame, LYING, x=52%, filling 34% of frame height. @AnnaYoung: centre of frame, STANDING, x=44%. @WardDoctor: centre of frame, STANDING, x=46%, filling 55% of frame height. Nothing in this list may be re-placed, re-lit or improved.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Close three-quarter riding alongside the gurney at mattress height, camera about 90 cm from the floor and one metre from her shoulder, moving exactly with the gurney so she is steady in frame and the tiled wall streams past behind her, no other depth legible.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.2s] Starting positions, held until described otherwise: @YoungMotherHospital LYING at x=42%, her head on the flat pillow at x=30% and her face filling 34% of frame height, her belly high and full under the folded grey blanket at x=62%, BOTH HANDS FLAT ON THE BELLY, one above the other. [2.2-4.4s] HER HEELS PRESS DOWN INTO THE MATTRESS — the oilcloth denting under them, the tendons standing in her ankles, her whole body pushing back against nothing. [4.4-6.6s] HER FACE ENTERS LOW IN THE FRAME from the bottom edge, upside down to camera, at x=46%, filling 30% of frame height — only the chin, mouth, nose and the wet-stuck hair at the temples, her eyes travelling UP the ceiling, from the near trough to the furthest one, and stopping there. [6.6-8.8s] IT LETS GO ALL AT ONCE.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — the run of bare fluorescent tubes in their shallow enamel troughs is the only source inside the corridor: cold, even, and so pallid it drains the tile of its colour, falling vertically from directly overhead onto the top of everything in frame, never from the side, and from just above and slightly behind the lens wherever the lens rides low near the floor;
SOUND — None. Nobody speaks audibly in this generation. In shot 1 the doctor's mouth moves at her ear and NOTHING is heard;
ENDING FRAME, the state this shot hands over — The gurney's chrome side rail streaming along, and her right hand fallen open on the taped edge of the mattress beside it, palm up, the fingers slack and still rocking with the wheels, the eau-de-nil tiles sliding past soft behind them.
AVOID — audible speech, spoken words, whispered dialogue, lip-synced speech, a scream, crying out, bright red, saturated red, red cross, red crescent.
```

## 4G — micro-plan **4.3e** SEUL « Le rejeu — le même couloir, la même seconde, depuis le brancard » *(6 s de rushes → 3,5 s au montage · Elements : @AnnaYoung + @WardDoctor + @RussianHospitalCorridor — **@YoungMotherHospital N'EST PAS CHARGÉE : la caméra EST son regard** · Lens Anamorphic 40 mm f/2 · start frame : LIEU-17 IMAGE 3, ANGLE B)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 6 s |
| **Éléments** | @AnnaYoung + @WardDoctor + @RussianHospitalCorridor + @YoungMotherHospital |
| **`start_image`** | LIEU-17 IMAGE 3, ANGLE B |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — A hospital corridor at night, seen from a gurney that is rolling toward a pair of heavy double doors.
CONTINUITY — VIDEO 1 is the shot immediately before this one (4F). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the INHERITED STATE line below, already true, nothing replayed, then move on. CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @YoungMotherHospital: centre of frame, LYING, x=42%, filling 34% of frame height. @WardDoctor: centre of frame, x=52%. Nothing in this list may be re-placed, re-lit or improved.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Low counter-look along the corridor from the rolling gurney, camera about 60 cm from the floor, deep focus, rolling steadily toward the double doors, no other movement.
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.6s] Starting positions, held until described otherwise: the padded out-of-focus mattress edge across the bottom 18% of frame. The corridor comes on. [1.6-3.2s] The corridor again, uninterrupted: the doors bigger, the standing man still not moving, the kneeling shape still not moving, the tubes still crossing. [3.2-4.8s] A NAME IS SCREAMED SOMEWHERE AHEAD, torn and short.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 40 mm f/2 equivalent.
LIGHT — the run of bare fluorescent tubes in their shallow enamel troughs is the only source inside the corridor: cold, even, and so pallid it drains the tile of its colour, falling vertically from directly overhead onto the top of everything in frame, never from the side, and from just above and slightly behind the lens wherever the lens rides low near the floor;
SOUND — None. Nobody speaks in this generation, in any language. One name is screamed off screen, ahead of camera, and no other human sound exists. SFX only.
ENDING FRAME, the state this shot hands over — The corridor from sixty centimetres, the double doors slightly off centre with their two dark portholes, the ceiling troughs still crossing above — and on screen right, small in the depth, the standing man with his cap held against his chest, and lower down against the tiles the dark kneeling shape of a woman with her back turned, neither of them moving.
AVOID — the kneeling woman standing up, the kneeling woman turning, her face, her profile, the doctor walking forward, the doctor replacing his cap, the doctor's readable face, the doctor leaning in over the top edge, a white cloth cap over the top edge, a white coat near the lens.
```

## 4H — micro-plans **4.3h + 4.3i** « Les trois coups, et le feu » *(8 s de rushes → 5,5 s au montage · Elements : @AnnaYoung + @Mender + @AnnaKitchenPast · start frame : LIEU-18 IMAGE 2, ANGLE A porte fermée ; l'IMAGE 4, ANGLE B, est l'axe du shot 2)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 8 s |
| **Éléments** | @AnnaYoung + @Mender + @AnnaKitchenPast |
| **`start_image`** | LIEU-18 IMAGE 2, ANGLE A porte fermée ; l'IMAGE 4, ANGLE B, est l'axe du shot 2 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — Two years later, at night.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (4G), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @WardDoctor: centre of frame, STANDING, x=64%. @AnnaYoung: centre of frame, KNEELING, x=57%. Nothing in this list may be re-placed, re-lit or improved.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Medium wide on the closed door of the room, standing eye level, camera about 150 cm high and three metres back, slightly to one side so the door swings toward camera, static, locked off.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.6s] Starting positions, held until described otherwise: the closed plank door at x=58%, filling 74% of frame height, its paint worn through at the handle; [1.6-3.3s] @Mender IS ALREADY THERE, motionless, filling the opening: a BACK, seen from DIRECTLY BEHIND, standing on a black landing, filling 88% of frame height and CUT BY THE TOP OF THE FRAME AT THE SHOULDERS so no head, no hood and no neck are ever in the picture. [3.3-4.9s] HER HANDS BREAK KINDLING — the swollen knuckles going pale as they press, one stick snapping short, a second bending before it gives, the pieces going into the ash. [4.9-6.6s] A match is struck along the box and FAILS: a spit, a fizz, nothing. THE SECOND MATCH TAKES.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — The colour is drained out of the LIGHT ITSELF, not out of the surfaces, and it is drained inside the camera, not afterwards.
SOUND — None. Nobody speaks in this generation, in any language. SFX only.
ENDING FRAME, the state this shot hands over — The open stove door close in frame, the small pale amber flame standing alone in the packed grey ash inside it, the cast-iron edge lit from within for the first time in two winters — and the room around it dark, her hands and the carried splinter already gone out of frame.
AVOID — the coated figure's face, any profile of the coated figure, any front view, his head, his hood, his neck, the figure turning round, the figure looking back, the figure entering the room, the figure speaking.
```

## 4I — micro-plans **4.3j + 4.3k + 4.3l** « La cour, et le prénom » *(10 s de rushes → 6,5 s au montage · Elements : @AnnaYoung + @Mender + @YoungMother + @Kolya2 + @RussianCourtyard · start frame : LIEU-20 IMAGE 2, ANGLE A ; l'IMAGE 3 donne la valeur des shots 2 et 3)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @AnnaYoung + @Mender + @YoungMother + @Kolya2 + @RussianCourtyard |
| **`start_image`** | LIEU-20 IMAGE 2, ANGLE A ; l'IMAGE 3 donne la valeur des shots 2 et 3 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — The same night, three streets away.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (4H), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @AnnaYoung: left third of frame, STANDING, x=24%, filling 70% of frame height. Nothing in this list may be re-placed, re-lit or improved.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Wide across the courtyard, standing eye level, camera about 155 cm high, static, locked off, the mercury lamp high at x=12% throwing its cone down across the frame, the porch mouth small in the depth at x=76%, the bench at the far side.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.4s] The arm drops and HE WALKS OUT OF FRAME BY THE LEFT EDGE in two strides, without once turning round. [2.4-4.7s] Starting positions: @YoungMother STANDING at x=46%, front on, filling 78% of frame height, her hands at her sides, her face flat and tired; [4.7-7.1s] THE OLD WOMAN'S MOUTH ASKS SOMETHING in the near out-of-focus foreground, only the edge of her jaw moving at the frame's left edge — heard as nothing; [7.1-9.4s] SOMETHING GOES THROUGH THE FACE WITHOUT CHANGING IT: the breath stops between two exhalations, the throat moves once, the outer corners of the eyes tighten by a millimetre.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — The colour is drained out of the LIGHT ITSELF, not out of the surfaces, and it is drained inside the camera, not afterwards.
SOUND — None. Nobody is heard in this generation, in any language.
ENDING FRAME, the state this shot hands over — The old woman close in frame under the mercury lamp, her scarf knotted under her chin, her broad reddened hand flat across her own mouth with the thumb under the jaw, her eyes wide open and dry, one breath going out around her fingers and standing white in the cold — the porch and its caged bulb a soft blur behind her shoulder, and nobody in it.
AVOID — the coated figure's face, any profile, any front view, the figure turning round, the figure looking back, the figure speaking, a readable build, a readable age, the figure in shot 2, the figure in shot 3.
```
