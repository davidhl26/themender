# PROMPTS COURTS — SÉQUENCE 08

> ~300 mots par plan, l'ordre recommandé par Higgsfield et ByteDance.
> Le détail complet reste dans `PRET-SEQ-08.md` : géométrie GEO, verrous, raccords numérotés.
> **C'est CETTE version qu'on colle dans Higgsfield.** L'autre est le document de tournage.

## 8A — plan 8.1 « La bibliothèque » *(10 s de rushes → 5 s au montage · Elements : @Nora + @Mender + @LibraryCorridor · start frame : LIEU-11 IMAGE 2)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @Nora + @Mender + @LibraryCorridor |
| **`start_image`** | LIEU-11 IMAGE 2 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — @Nora alone in an emptied school library hears pages turning with no reader, lifts her eyes from a book she was not reading, and far down the corridor a long written coat — a back, never a face — is already crossing between two shelf ranges and turns the corner.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (7B), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Nora: centre of frame, LYING, x=52%, filling 60% of frame height. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY: whatever brought the bodies and the props here has already happened in the attached video and must NOT be performed again.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Medium across the study table, seated eye level, camera about 115 cm high and 1.5 m from the table at a slight three-quarter angle, static, locked off.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.4s] Starting positions, held until described otherwise: @Nora SEATED at x=46%, three-quarter toward camera, filling 55% of frame height, head down over the open textbook, both forearms on the table either side of it, the pencil untouched. [2.4-4.8s] THE COAT IS ALREADY IN THE FRAME AND ALREADY MOVING, large and unmistakable — no entrance, no start-up: at x=52%, filling 62% of frame height, a tall figure seen from DIRECTLY BEHIND, mid-stride, crossing the gap between two shelf ranges from screen-left to screen-right, hard against the window's backlight. [4.8-7.3s] OFF SCREEN, behind camera: a chair goes over backwards and cracks on the parquet, then fast running steps. [7.3-9.7s] @Nora swings into the near frame edge from screen-left, SEEN FROM BEHIND AND THREE-QUARTER BACK, her left hand catching the shelf upright, and stops dead — no face to camera.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — One source only: the window at the far end of the corridor, throwing flat cold late-afternoon light straight down its length — a grey-white shaft with dust hanging almost motionless in it, the beam's edges feathered, laying a long dull gleam up the centre of the parquet and a bright rectangle on the floor at the end.
SOUND — None. Nobody speaks in this generation. The riffle of pages is the only voice this scene has. SFX only.
ENDING FRAME, the state this shot hands over — The empty side aisle beyond the corner, running away between two tall shelf faces, dust settling in the weak grey spill — and at the near frame edge, from behind, @Nora swung in around the shelf upright, her left hand gripping it, shoulders heaving, looking down the emptiness at nothing.
AVOID — the coated figure's face, any profile of the coated figure, any front view of the coated figure, the figure turning around, the figure looking back, the figure's eyes, the figure pausing, bright red, saturated red, the coat reading as red.
```

## 8A-bis — SECOURS de 8A *(5 s · à ne lancer QUE si le shot 2 de 8A rate : manteau trop petit, trop sombre, ou lu comme un simple passant · Elements : @Mender + @LibraryCorridor · start frame : LIEU-11 IMAGE 1, le master)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 5 s |
| **Éléments** | @Mender + @LibraryCorridor |
| **`start_image`** | LIEU-11 IMAGE 1, le master |
| **`video_references`** | *aucune — c'est une tête de chaîne* |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — A tall figure in a long written coat — a back, never a face — is already crossing the corridor of an emptied school library from one shelf range to the next, and turns the corner without ever looking back.
CONTINUITY — no video attached. This is the head of its chain: it sets the light, grain and skin rendering the following shots match. THE ATTACHED IMAGE IS THE FIRST FRAME — it fixes the opening composition, every body position and pose, every prop state and the camera direction; take nothing else from it, no border, no backdrop, no empty-room staging.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Wide straight down the corridor of shelves, eye level about 155 cm, deep focus, static, locked off, one stop wider than the main version — the shelves closing in toward the bright window rectangle at the far end, exactly the axis of the reference master, the whole height of a standing figure held inside the frame with air above the hood.
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.1s] THE COAT IS ALREADY IN THE FRAME AND ALREADY MOVING, large and unmistakable — no entrance, no start-up: at x=44%, filling 78% of frame height, a tall figure seen from DIRECTLY BEHIND, mid-stride, crossing the gap between two shelf ranges from screen-left to screen-right, hard against the window's backlight. [1.1-2.3s] Three unhurried strides — the ivory lines rippling across the whole back, the hem swinging heavily, the bare hand swinging with them — and he passes behind the last shelf upright at x=74% and turns the corner screen-right, without once turning his head. [2.3-3.4s] The corridor holds, empty, the dust turning slowly in the light.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 40 mm f/2 equivalent, one stop wider than 8A.
LIGHT — One source only: the window at the far end of the corridor, throwing flat cold late-afternoon light straight down its length — a grey-white shaft with dust hanging almost motionless in it, the beam's edges feathered, laying a long dull gleam up the centre of the parquet and a bright rectangle on the floor at the end.
SOUND — None. Nobody speaks in this generation. SFX only.
ENDING FRAME, the state this shot hands over — The empty corridor of shelves seen straight down its length, the bright grey-white window rectangle at its far end, dust turning slowly in the shaft, the parquet holding one long dull gleam up its centre — nobody in it, nothing moving, nothing left anywhere.
AVOID — the coated figure's face, any profile of the coated figure, any front view of the coated figure, the figure turning around, the figure looking back, the figure's eyes, the figure pausing, the figure returning into frame, bright red, saturated red.
```

## 8B — plan 8.2 « Le couloir de la maison » *(10 s de rushes → 4 s au montage · Elements : @Nora + @Mender + @NoraBedroom · start frame : LIEU-08 IMAGE 4, le palier, porte entrouverte 10 cm)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @Nora + @Mender + @NoraBedroom |
| **`start_image`** | LIEU-08 IMAGE 4, le palier, porte entrouverte 10 cm |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — Night.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (8A), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Nora: hard against the NEAR LEFT frame edge, STANDING — she got up and ran during this shot — swung in around the shelf upright at the mouth of the side aisle, seen from behind and three-quarter back, her left hand gripping the upright, x=16%, filling 80% of frame height.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Static, camera at 160 cm on the landing, looking down the full length of the dark hallway, exactly the axis of the reference angle: her bedroom door screen-right at x=68%, ajar ten centimetres, the blade of cold light from the gap lying across the boards toward camera;
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-3.0s] The bedroom door swings quietly inward and widens; [3.0-6.0s] Her left hand comes off the handle and drops to her side. [6.0-9.0s] She crosses the last two metres in two slow barefoot steps, the glass hanging at her side, and stops at the corner, her free hand coming to rest on the rail post.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — motivated sources only, never more than two lit at once, and the two temperatures never mix.
SOUND — None. Nobody speaks. Her breathing and the house are the only voices. SFX only.
ENDING FRAME, the state this shot hands over — @Nora alone at the dark corner of the landing, seen from behind, chest-up, looking down into the black stairwell, the empty glass hanging at her side, one hand on the rail post, the thread of sodium grazing her shoulder;
AVOID — the figure's face, the figure's profile, the figure's head, the figure's shoulders, the figure's hands, the figure's eyes, the coat above hip height, the coat pausing or turning or coming back, the coat visible longer than one second, the coat hanging on a hook.
```

## 8B-bis — SECOURS de 8B *(4 s · à ne lancer QUE si le manteau ne se lit pas au fond du couloir noir : rien de visible, ou une ombre informe · Elements : @Mender + @NoraBedroom · start frame : aucun — cadre décrit au prompt, à 2 m du coin)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 4 s |
| **Éléments** | @Mender + @NoraBedroom |
| **`start_image`** | aucun — cadre décrit au prompt, à 2 m du coin |
| **`video_references`** | *aucune — c'est une tête de chaîne* |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — At the far corner of a dark upstairs landing, the hem and lower back of a long written coat slide once past the corner toward the unseen stairs and are gone.
CONTINUITY — no video attached. This is the head of its chain: it sets the light, grain and skin rendering the following shots match. THE ATTACHED IMAGE IS THE FIRST FRAME — it fixes the opening composition, every body position and pose, every prop state and the camera direction; take nothing else from it, no border, no backdrop, no empty-room staging.
OPENING FRAME — Static, camera at 160 cm, two metres from the corner of the landing and square to the corner wall, locked off: the corner and the stair rail's top post filling the right half of frame, the wall running away to the left, the black drop of the unseen stairwell opening beyond the post, near-black everywhere except where the sodium thread grazes the wall.
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-0.9s] Frame contents, nothing moving through them yet: the corner, the rail post, the thin thread of sodium orange lying along the wall, the boards catching it in one dull line, the blacks fully crushed. [0.9-1.7s] The corner holds, empty, the sodium thread lying exactly where it was, nothing moving. [1.7-2.6s] The corner holds, empty, the sodium thread lying exactly where it was, nothing moving.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — motivated sources only, never more than two lit at once, and the two temperatures never mix.
SOUND — None. Nobody speaks in this generation. SFX only.
ENDING FRAME, the state this shot hands over — The empty far corner of the dark landing, the stair rail's top post catching one dull edge of sodium, the black drop of the unseen stairwell opening away beyond it, the thread of sodium lying along the wall — nothing in the frame, nothing moving.
AVOID — the figure's face, the figure's profile, the figure's head, the figure's shoulders, the figure's hands, the figure's eyes, the coat above hip height, the coat pausing or turning or coming back, the coat visible longer than one second, the coat hanging on a hook.
```

## 8C — plan 8.3 « Le miroir » *(10 s de rushes → 5 s au montage · Elements : @Nora + @Bathroom · start frame : LIEU-10 IMAGE 2)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @Nora + @Bathroom |
| **`start_image`** | LIEU-10 IMAGE 2 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — @Nora steps out of the shower, the towel half-raised, and lifts her eyes to the mirror out of habit — and the gesture stops there.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (8B), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Nora: centre of frame, STANDING, x=62%, filling 62% of frame height. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY: whatever brought the bodies and the props here has already happened in the attached video and must NOT be performed again.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Medium chest-up from the doorway, angled toward the mirror and basin, eye level, static, locked off — exactly the axis of the reference angle: the mirror screen-right at x=65%, the basin below it, the shower curtain and the towel radiator at the frame edges.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.3s] Frame contents: the steam-filled room, the mirror at x=65% fogged across its LOWER THIRD only, clear glass above it; [2.3-4.6s] Starting positions: the fog now covers the LOWER HALF of the glass; [4.6-6.9s] The fog is now complete, edge to edge, and the three clear bands stand in it, whole, sharp and still, held wide and steady for the rest of the shot — no change of shape, no growth, no drift, no drop crossing them. [6.9-9.2s] She takes one step backwards, off balance, and her shoulder blades hit the door — a flat dull knock;
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 85 mm f/2 equivalent.
LIGHT — one practical: the single wall light above THE MIRROR, diffused by the vapour, the bulb wearing a soft halo in the steam, its throw dying within a metre, laying whites and cold greys on the tiles.
SOUND — None. Nobody speaks in this generation. Her breath is the only voice. SFX only.
ENDING FRAME, the state this shot hands over — The steam-filled bathroom: the fogged mirror screen-left with the three clear abstract soap bands standing whole in the fog, @Nora screen-right chest-up with her shoulder blades against the door, her right arm out and two fingertips resting on the glass a hand's width beside the bands, the two beads just beginning to run at the far tip of the lower band, steam drifting through the wall light.
AVOID — legible letters, readable words, letterforms in the fog, any writing that reads as text, letters appearing one by one, a stroke that draws itself, a line advancing on its own, a fade-in of marks, marks changing shape between shots, a hand wiping the mirror.
```

## 8C-bis — SECOURS de 8C *(5 s · à ne lancer QUE si le miroir refuse d'accueillir des bandes horizontales nettes avec Nora dans le cadre · Elements : @Bathroom · start frame : LIEU-10 IMAGE 2)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 5 s |
| **Éléments** | @Bathroom |
| **`start_image`** | LIEU-10 IMAGE 2 |
| **`video_references`** | *aucune — c'est une tête de chaîne* |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — A macro insert on a fogged bathroom mirror, alone: three clear bands of abstract soap streaks stand in the fog, whole, sharp and unmoving, while the steam drifts and two beads begin to run at the far end of the lowest band.
CONTINUITY — no video attached. This is the head of its chain: it sets the light, grain and skin rendering the following shots match. THE ATTACHED IMAGE IS THE FIRST FRAME — it fixes the opening composition, every body position and pose, every prop state and the camera direction; take nothing else from it, no border, no backdrop, no empty-room staging.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Macro insert on the mirror alone, 85 mm, camera square to the glass at about 60 cm, static, locked off: the fogged mirror filling the frame, its chipped enamel edge entering the left and right frame edges, the chipped top of the basin crossing the bottom of frame.
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.5s] Frame contents, unmoving: the glass fogged edge to edge; [1.5-2.9s] Nothing on the mirror changes for one frame: the three bands hold their shapes, lengths and positions absolutely, the fog holds its opacity, no stroke extends, no mark is added, nothing writes itself. [2.9-4.4s] Two beads gather at the OUTER END of the lower band, at its far right tip, and begin to run — slowly, a few millimetres, blurring that far tip only.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 85 mm f/2 equivalent.
LIGHT — one practical: the single wall light above THE MIRROR, diffused by the vapour, the bulb wearing a soft halo in the steam, its throw dying within a metre, laying whites and cold greys on the tiles.
SOUND — None. Nobody speaks in this generation. Nobody is in it. SFX only.
ENDING FRAME, the state this shot hands over — The fogged mirror filling the frame, the three clear abstract soap bands standing whole and sharp in the fog in its central third, the two beads stalled halfway down at the far tip of the lower band, steam drifting slowly across the glass in the wall light — no person, no reflection, nothing else.
AVOID — legible letters, readable words, letterforms in the fog, any writing that reads as text, letters appearing one by one, a stroke that draws itself, a line advancing on its own, a fade-in of marks, marks changing shape, a hand wiping the mirror.
```

## 8D — plan 8.4 « La bague » *(8 s de rushes → 3 s au montage · Elements : @Nora + @NoraBedroom + @MotherRing · start frame : LIEU-08 IMAGE 3)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 8 s |
| **Éléments** | @Nora + @NoraBedroom + @MotherRing |
| **`start_image`** | LIEU-08 IMAGE 3 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — Dressed to leave, @Nora opens a small worn box, looks once at her mother's ring, closes her fist on it until the knuckles whiten, and puts it into the right-hand pocket of her coat without looking at it.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (8C), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Nora: centre of frame, STANDING, x=62%. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY: whatever brought the bodies and the props here has already happened in the attached video and must NOT be performed again.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Macro on her hands and the box, high angle over the desk, camera about 50 cm above the wood, tilted down at roughly 60 degrees, static, locked off, very shallow focus.
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.4s] Her hands come into frame from the lower edge without hurry; [2.4-4.8s] The closed fist lowers out of the bottom of frame and does not come back. [4.8-7.2s] Her left hand reaches to the clip lamp and clicks the switch.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 85 mm f/2 equivalent.
LIGHT — motivated sources only, never more than two lit at once, and the two temperatures never mix.
SOUND — None. Nobody speaks in this generation. The hands say it. SFX only.
ENDING FRAME, the state this shot hands over — The desk in sodium orange only, the clip lamp dark, the small worn velvet box open and empty with its velvet bed dented where the ring sat, the closed laptop a dull shape at the far edge, @Nora a dark unmoving mass at the frame edge with one breath lifting her shoulders.
AVOID — the ring visible after the first shot, the ring visible inside the pocket, the ring worn on a finger, the box reopening, a second look at the ring, jewellery in the final frame, a sandwich, food on the desk, greaseproof paper, kitchen string.
```

## 8E — plan 8.5 « Le bus de nuit » *(12 s de rushes → 6 s au montage · Elements : @Nora + @NightBus · start frame : LIEU-13 IMAGE 2 ; l'IMAGE 3 est l'axe du shot 4)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 12 s |
| **Éléments** | @Nora + @NightBus |
| **`start_image`** | LIEU-13 IMAGE 2 ; l'IMAGE 3 est l'axe du shot 4 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — @Nora rides a night bus alone, forehead against the glass, a whole untouched sandwich lying in crumpled paper on her lap under her hand — and she never once looks at it.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (8D), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Nora: centre of frame, STANDING, x=52%, filling 66% of frame height. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY: whatever brought the bodies and the props here has already happened in the attached video and must NOT be performed again.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Close-up, right profile, seated eye level about 110 cm, camera locked to the bus a metre from her, static framing, the fogged window filling the frame behind her.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.8s] Starting positions, held until described otherwise: her face in right profile at x=44%, filling 66% of frame height, forehead resting against the glass in the one clear wiped patch, eyes half open on the dark going past; [2.8-5.5s] Starting positions, held until described otherwise: her face in right profile at x=44%, filling 66% of frame height, forehead resting against the glass in the one clear wiped patch, eyes half open; [5.5-8.2s] Starting positions, held until described otherwise: her face in right profile at x=44%, filling 66% of frame height, forehead resting against the glass in the one clear wiped patch; [8.2-11.0s] She stands in ONE movement, without hurry and without hesitation — and in the same movement the crumpled packet is lifted off her lap and pushed down into the parka's RIGHT side pocket, where it settles and bulges.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — Cold white ceiling strip light inside, one diffuser panel yellowed and fractionally dimmer than the rest, pooling flat and shadowless on the seat backs and the tops of the poles.
SOUND — None. Nobody speaks in this generation. The chime counts for her. SFX only.
ENDING FRAME, the state this shot hands over — @Nora standing at the closed doors, three-quarter back to camera, her right hand on the cloudy chrome pole, the crumpled paper packet pushed into her parka's right side pocket and bulging there, her reflection doubled in the dark door glass, the empty aisle and seats behind her, the bus still slowing, the night outside absolute.
AVOID — any red anywhere, red brake lights, red traffic lights, red stop-button lights, red handrails, red signage through the windows, a readable destination display, readable signage, legible numerals, on-screen text.
```
