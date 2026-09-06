# PROMPTS COURTS — SÉQUENCE 03

> ~300 mots par plan, l'ordre recommandé par Higgsfield et ByteDance.
> Le détail complet reste dans `PRET-SEQ-03.md` : géométrie GEO, verrous, raccords numérotés.
> **C'est CETTE version qu'on colle dans Higgsfield.** L'autre est le document de tournage.

## 3A — plan 3.1 « La tasse » *(10 s de rushes → 5 s au montage — LE seul ralenti du film · Elements : @Maeve + @Kitchen · Lens Anamorphic 40 mm f/2.8 · start frame : aucune)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @Maeve + @Kitchen |
| **`start_image`** | aucune |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — A few weeks later, the same kitchen, a paler morning.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (2D), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @SamBefore: left third of frame, SEATED, x=30%. @Maeve: centre of frame, SEATED, x=54%, filling 45% of frame height. @MiloBefore: centre of frame, x=62%. @NoraBefore: right third…
OPENING FRAME — Insert at counter height, eye level, held, operated, no longer following. No face in frame. Starting positions, held until described otherwise: the white porcelain cup of milk sits…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.4s] Starting positions, held until described otherwise: the white porcelain cup of milk sits on the counter at x=50%, mid-frame, filling 30% of frame height;… [2.4-4.7s] Real time. [4.7-7.1s] Still inside the slow motion: the last shard glides to a stop; Starting positions: @Maeve's face and right shoulder, right of centre at x=58%,… [7.1-9.4s] The fingers of the raised hand close slowly into a loose fist… and open again. The fingers close and open a second time, slower.
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 40 mm f/2.8 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — one source only, in every shot without exception: the single window directly above THE GAS RANGE on the…
SOUND — None. She says nothing to anyone, in either shot. SFX only.
ENDING FRAME, the state this shot hands over — Her face right of centre in three-quarter, flat and closed, eyes down on her own raised right hand, the hand half open at chest height, the…
AVOID — visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, subjects looking at camera, morphing objects.
```

## 3B — plan 3.2 « La conversation muette » *(10 s de rushes → 6 s au montage · ⚠ CADRE À VERROUILLER — rejoué au pixel en 4.3b · Elements : @SamBefore + @NoraBefore + @HospitalCorridor · Lens Anamorphic 85 mm f/2 · start frame : LIEU-05 IMAGE 2)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @SamBefore + @NoraBefore + @HospitalCorridor |
| **`start_image`** | LIEU-05 IMAGE 2 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — A hospital corridor, day.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (3A), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Maeve: centre of frame, STANDING, x=58%, filling 70% of frame height. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE,…
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — Medium-long shot compressed by the long lens, eye level, held, operated, no longer following. The framing and the focus split (foreground soft, mid-frame sharp) never change. Starting positions,…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.1s] Starting positions, held until described otherwise: extreme foreground at the left edge, x=12%, filling 55% of frame height: the back of @NoraBefore's head and… [2.1-4.3s] The doctor stops speaking. Sam's head goes down, slowly — the chin sinking toward the chest in one single continuous arc, nothing else moving,… [4.3-6.4s] The doctor stops speaking. [6.4-8.6s] The doctor's eyes drop to the floor. The doctor's right hand rises, unhurried, and settles on Sam's left shoulder.
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 85 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — DAY STATE: the tube run is directly overhead, above and slightly behind the camera: top light, faintly green,…
SOUND — None reaches the microphone at any point. The doctor's lips move at ten metres; his voice is never audible. No voices anywhere in this generation. SFX only.
ENDING FRAME, the state this shot hands over — The doctor's hand resting on Sam's shoulder, Sam's head down, the doctor's eyes on the floor, both compressed sharp in mid-frame against the blown-out window; Nora's…
AVOID — visible camera rigs, cartoonish colors, blurred focus on the two men, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, subjects looking at camera, slow motion.
```

## 3C — plan 3.3 « Tu m'écrases » *(8 s de rushes → 5 s au montage · Elements : @MaeveIll + @MiloBefore + @HospitalRoom · Lens Anamorphic 50 mm f/2 · start frame : LIEU-04 IMAGE 2)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 8 s |
| **Éléments** | @MaeveIll + @MiloBefore + @HospitalRoom |
| **`start_image`** | LIEU-04 IMAGE 2 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — A gravely ill mother holds her small son on a hospital bed.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (3B), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @SamBefore: centre of frame, x=57%. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY: whatever…
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — Medium close-up from the right side of the bed, camera at eye level about 140 cm high, roughly 1.5 m from the bed, held, operated, no longer following.…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.6s] Starting positions, held until described otherwise: @MaeveIll propped up in the bed, head and shoulders right of centre at x=58%, filling 70% of frame… [1.6-3.3s] A beat. [3.3-4.9s] Small voice, a real @MiloBefore's apology: "Sorry." [4.9-6.6s] Warm, slow, and completely serious under the warmth: "Don't be sorry.
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — inside the room: cold daylight from THE VOILED NORTH WINDOW, diffused twice by the sky and by the…
SOUND — [1.4-3.1s] @MaeveIll, dry amusement over a weak voice, unhurried: "Milo. You're squashing me." [3.9-4.7s] @MiloBefore, small voice: "Sorry." [5.3-6.6s] @MaeveIll, warm, slow, serious underneath: "Don't be sorry. Squash…
ENDING FRAME, the state this shot hands over — The mother propped up in the bed, the crimson scarf across her shoulders, her eyes closed, her nose lowered into @MiloBefore's hair — and @MiloBefore clamped…
AVOID — visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, subjects looking at camera, slow motion.
```

## 3D — plan 3.4 « La bague » *(10 s de rushes → 6 s au montage · ⚠ PLAN NEUF — REFONTE DU 31/08 · Elements : @MaeveIll + @NoraBefore + @MotherRing + @HospitalRoom · Lens Anamorphic 50 mm f/2 · start frame : LIEU-04 IMAGE 2 — shots 2 et 3 après hard cut interne, sans start frame)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @MaeveIll + @NoraBefore + @MotherRing + @HospitalRoom |
| **`start_image`** | LIEU-04 IMAGE 2 — shots 2 et 3 après hard cut interne, sans start frame |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — @NoraBefore comes to her dying mother's bedside and does not know where to put her hands.
CONTINUITY — VIDEO 1 is the shot immediately before this one (3C). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the inherited state below, already true, nothing replayed, then move on. It must CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin rendering and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @MaeveIll: centre of frame, x=58%, filling 70% of frame height. @MiloBefore: centre of frame, x=42%. Nothing in this list may be re-placed, re-lit or improved. THIS…
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — Medium two-shot from the right side of the bed, camera at eye level about 140 cm high, roughly 1.8 m from the bed, held, operated, no longer following…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.4s] Starting positions, held until described otherwise: @MaeveIll propped up in the bed at x=64%, filling 62% of frame height, in three-quarter view facing camera-left,… [2.4-4.7s] Starting positions: the white sheet fills the frame. The closed right fist comes over the open palm, opens against it, and the thin gold… [4.7-7.1s] Both the mother's hands close @NoraBefore's fingers over the ring, one finger at a time, and then hold the closed fist inside them, pressing,… [7.1-9.4s] Starting positions: @MaeveIll's face at x=62%, filling 55% of frame height, turned up toward her daughter;
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — inside the room: cold daylight from THE VOILED NORTH WINDOW, diffused twice by the sky and by the…
SOUND — None. Nobody speaks in this generation, in any shot. The mother's mouth opens at [8.1s] and NO sound is produced — not a word, not a whisper, not…
ENDING FRAME, the state this shot hands over — The tight two-shot at the bed rail: the mother's face turned up, her mouth just closed on nothing, her eyes open on her daughter — and…
AVOID — visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, subjects looking at camera, slow motion.
```

## 3E — plan 3.5 « La vitre » — **LA PLAQUE** *(10 s de rushes → 3 s dans 3.5 ET 8 s dans 10.10 · Elements : @MaeveIll + @SamBefore + @HospitalCorridor + @HospitalRoom au-delà de la vitre · Lens Anamorphic 50 mm f/2 · start frame : LIEU-05 IMAGE 3)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @MaeveIll + @SamBefore + @HospitalCorridor + @HospitalRoom |
| **`start_image`** | LIEU-05 IMAGE 3 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — Through the glass of a closed hospital room door, mute: a dying woman takes her husband's face in both her hands and speaks to him at…
CONTINUITY — VIDEO 1 is an earlier shot of the same film (3D), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @MaeveIll: centre of frame, x=62%, filling 55% of frame height. @NoraBefore: left third of frame, STANDING, x=32%, filling 58% of frame height. Nothing in this list…
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — Medium shot through the wired-glass door window, eye level from the corridor, held, operated, no longer following. The framing, the camera height and the off-centre crop never change…
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-0.6s] Starting positions, held until described otherwise, all of it seen through the glass: @MaeveIll sitting up in the bed, in three-quarter view facing camera-left,… [0.6-1.2s] Her two hands rise slowly from the sheet — the cannula line following the left one — and settle on his cheeks, one on… [1.2-1.8s] Her two hands rise slowly from the sheet — the cannula line following the left one — and settle on his cheeks, one on…
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — inside the room: cold daylight from THE VOILED NORTH WINDOW, diffused twice by the sky and by the…
SOUND — None audible. Her lips move continuously behind the reflections for eight seconds; not one sound of the room crosses the glass. (In 10.10 this same file receives her…
ENDING FRAME, the state this shot hands over — ⚠ ABSOLUTE REFERENCE FRAME — the exact frame that returns in 10.10: through the wired glass, her two hands holding his face, thumbs on his cheekbones,…
AVOID — visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, subjects looking at camera, slow motion.
```

## 3F — plans 3.5 (contrechamp) + 3.6 « Elle détourne les yeux · le rouge sort » *(10 s de rushes → 3 s dans 3.5 + 3 s en 3.6 · Elements : @NoraBefore + @SamBefore (main seule, seg. 2) + @HospitalCorridor · Lens Anamorphic 85 mm f/2 · start frame : LIEU-05 IMAGE 4 pour le shot 1 — shot 2 après hard cut interne, sans start frame)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @NoraBefore + @SamBefore + @HospitalCorridor |
| **`start_image`** | LIEU-05 IMAGE 4 pour le shot 1 — shot 2 après hard cut interne, sans start frame |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — @NoraBefore has just come out of a hospital room.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (3E), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @MaeveIll: centre of frame, x=54%. @SamBefore: centre of frame, SEATED, x=62%. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE,…
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — Medium shot across the corridor, compressed by the long lens, eye level, held, operated, no longer following. Starting positions, held until described otherwise: @NoraBefore left of centre at…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.3s] Starting positions, held until described otherwise: @NoraBefore left of centre at x=42%, chest-up, filling 68% of frame height, seen in three-quarter BACK — she… [2.3-4.7s] Her eyes drop from the pane to the floor. [4.7-7.0s] She turns away from the door — the head first, then the shoulders, then the feet — and walks out of frame screen-left, unhurried,… [7.0-9.3s] A man's right hand and forearm (@SamBefore — large, clean, NO ink anywhere, the thin worn steel wedding band, the grey marl cuff) enter…
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 85 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — DAY STATE: the tube run is directly overhead, above and slightly behind the camera: top light, faintly green,…
SOUND — None, in either segment. Not a voice anywhere in this generation. SFX only.
ENDING FRAME, the state this shot hands over — The empty plastic chair, centred, in the dim green-grey corridor — no scarf, no red, no one. The film's world without red begins on this frame.
AVOID — visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, subjects looking at camera, slow motion.
```
