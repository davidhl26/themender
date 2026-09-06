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
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @SamBefore: left third of frame, SEATED, x=30%. @Maeve: centre of frame, SEATED, x=54%, filling 45% of frame height. @MiloBefore: centre of frame, x=62%. @NoraBefore: right third of frame, SEATED, x=78%. Nothing in this list may be re-placed, re-lit or improved.
OPENING FRAME — Insert at counter height, eye level, held, operated, no longer following. No face in frame.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.4s] Starting positions, held until described otherwise: the white porcelain cup of milk sits on the counter at x=50%, mid-frame, filling 30% of frame height; [2.4-4.7s] Real time. [4.7-7.1s] Still inside the slow motion: the last shard glides to a stop; [7.1-9.4s] The fingers of the raised hand close slowly into a loose fist… and open again.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 40 mm f/2.8 equivalent.
LIGHT — one source only, in every shot without exception: the single window directly above THE GAS RANGE on the east wall.
SOUND — None. She says nothing to anyone, in either shot. SFX only.
ENDING FRAME, the state this shot hands over — Her face right of centre in three-quarter, flat and closed, eyes down on her own raised right hand, the hand half open at chest height, the pale window light on one side of her face, the kitchen soft behind.
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
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Maeve: centre of frame, STANDING, x=58%, filling 70% of frame height. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY: whatever brought the bodies and the props here has already happened in the attached video and must NOT be performed again.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Medium-long shot compressed by the long lens, eye level, held, operated, no longer following. The framing and the focus split (foreground soft, mid-frame sharp) never change.
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.9s] Starting positions, held until described otherwise: extreme foreground at the left edge, x=12%, filling 55% of frame height: the back of @NoraBefore's head and her left shoulder, severely out of focus — dark wavy hair to the shoulders, absolutely still, facing away from camera toward the two men. [2.9-5.7s] The doctor stops speaking. [5.7-8.6s] The doctor's eyes drop to the floor. The doctor's right hand rises, unhurried, and settles on Sam's left shoulder.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 85 mm f/2 equivalent.
LIGHT — DAY STATE: the tube run is directly overhead, above and slightly behind the camera: top light, faintly green, even and shadowless, no shadow deeper than a half-tone, doubling as long soft streaks down the buffed vinyl and lying in slow faint reflections across any glazing.
SOUND — None reaches the microphone at any point. The doctor's lips move at ten metres; his voice is never audible. No voices anywhere in this generation. SFX only.
ENDING FRAME, the state this shot hands over — The doctor's hand resting on Sam's shoulder, Sam's head down, the doctor's eyes on the floor, both compressed sharp in mid-frame against the blown-out window;
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
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @SamBefore: centre of frame, x=57%. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY: whatever brought the bodies and the props here has already happened in the attached video and must NOT be performed again.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Medium close-up from the right side of the bed, camera at eye level about 140 cm high, roughly 1.5 m from the bed, held, operated, no longer following.
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.2s] Starting positions, held until described otherwise: @MaeveIll propped up in the bed, head and shoulders right of centre at x=58%, filling 70% of frame height, in three-quarter view facing camera-left and down toward @MiloBefore — the deep crimson-red scarf across her shoulders over the pale-blue hospital gown, her thinned auburn hair loose, the thin gold wedding band loose on her left hand. [2.2-4.4s] Small voice, a real @MiloBefore's apology: "Sorry." [4.4-6.6s] Warm, slow, and completely serious under the warmth: "Don't be sorry.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — inside the room: cold daylight from THE VOILED NORTH WINDOW, diffused twice by the sky and by the voile into a directionless grey wash across the bed, doubled by the overhead fluorescent behind its prismatic diffuser — shadowless, unmodelled, whites, sea-greens and cold greys, no warmth in frame.
SOUND — [1.4-3.1s] @MaeveIll, dry amusement over a weak voice, unhurried: "Milo. You're squashing me." [3.9-4.7s] @MiloBefore, small voice: "Sorry." [5.3-6.6s] @MaeveIll, warm, slow, serious underneath: "Don't be sorry.
ENDING FRAME, the state this shot hands over — The mother propped up in the bed, the crimson scarf across her shoulders, her eyes closed, her nose lowered into @MiloBefore's hair — and @MiloBefore clamped against her chest, both arms locked round her ribs, his eyes shut.
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
CONTINUITY — VIDEO 1 is the shot immediately before this one (3C). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the INHERITED STATE line below, already true, nothing replayed, then move on. CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @MaeveIll: centre of frame, x=58%, filling 70% of frame height. @MiloBefore: centre of frame, x=42%. Nothing in this list may be re-placed, re-lit or improved.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Medium two-shot from the right side of the bed, camera at eye level about 140 cm high, roughly 1.8 m from the bed, held, operated, no longer following — the raised head of the bed right of centre, the open floor beside it at screen-left.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.4s] Starting positions, held until described otherwise: @MaeveIll propped up in the bed at x=64%, filling 62% of frame height, in three-quarter view facing camera-left, the crimson scarf across her shoulders over the pale-blue gown, her right fist closed on the sheet at her hip, her left hand with the cannula flat beside it. [2.4-4.7s] Starting positions: the white sheet fills the frame. [4.7-7.1s] Both the mother's hands close @NoraBefore's fingers over the ring, one finger at a time, and then hold the closed fist inside them, pressing, not letting go. [7.1-9.4s] Starting positions: @MaeveIll's face at x=62%, filling 55% of frame height, turned up toward her daughter;
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — inside the room: cold daylight from THE VOILED NORTH WINDOW, diffused twice by the sky and by the voile into a directionless grey wash across the bed, doubled by the overhead fluorescent behind its prismatic diffuser — shadowless, unmodelled, whites, sea-greens and cold greys, no warmth in frame.
SOUND — None. Nobody speaks in this generation, in any shot.
ENDING FRAME, the state this shot hands over — The tight two-shot at the bed rail: the mother's face turned up, her mouth just closed on nothing, her eyes open on her daughter — and the daughter looking down at her, still, waiting, her closed right fist out of focus at the bottom of frame.
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
SHOT — Through the glass of a closed hospital room door, mute: a dying woman takes her husband's face in both her hands and speaks to him at length, without ever letting go.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (3D), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @MaeveIll: centre of frame, x=62%, filling 55% of frame height. @NoraBefore: left third of frame, STANDING, x=32%, filling 58% of frame height. Nothing in this list may be re-placed, re-lit or improved.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Medium shot through the wired-glass door window, eye level from the corridor, held, operated, no longer following.
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-0.6s] Starting positions, held until described otherwise, all of it seen through the glass: @MaeveIll sitting up in the bed, in three-quarter view facing camera-left, at x=54% inside the pane, the crimson scarf on her shoulders over the pale-blue gown, her face turned up toward him, her hands still on the sheet. [0.6-1.2s] Her two hands rise slowly from the sheet — the cannula line following the left one — and settle on his cheeks, one on each side, her thumbs on his cheekbones. [1.2-1.8s] Her two hands rise slowly from the sheet — the cannula line following the left one — and settle on his cheeks, one on each side, her thumbs on his cheekbones.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — inside the room: cold daylight from THE VOILED NORTH WINDOW, diffused twice by the sky and by the voile into a directionless grey wash across the bed, doubled by the overhead fluorescent behind its prismatic diffuser — shadowless, unmodelled, whites, sea-greens and cold greys, no warmth in frame.
SOUND — None audible. Her lips move continuously behind the reflections for eight seconds; not one sound of the room crosses the glass.
ENDING FRAME, the state this shot hands over — ⚠ ABSOLUTE REFERENCE FRAME — the exact frame that returns in 10.10: through the wired glass, her two hands holding his face, thumbs on his cheekbones, her lips mid-word, his cheek wet in the lamp's warmth, the crimson scarf muted on her shoulders, the cold green reflections lying across the pane.
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
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @MaeveIll: centre of frame, x=54%. @SamBefore: centre of frame, SEATED, x=62%. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY: whatever brought the bodies and the props here has already happened in the attached video and must NOT be performed again.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Medium shot across the corridor, compressed by the long lens, eye level, held, operated, no longer following.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.3s] Starting positions, held until described otherwise: @NoraBefore left of centre at x=42%, chest-up, filling 68% of frame height, seen in three-quarter BACK — she has stopped three paces beyond the door, facing away down the corridor, shoulders high, arms hanging, her RIGHT HAND A CLOSED FIST at her side. [2.3-4.7s] Her eyes drop from the pane to the floor. [4.7-7.0s] She turns away from the door — the head first, then the shoulders, then the feet — and walks out of frame screen-left, unhurried, arms at her sides, the fist still closed, without one look back. [7.0-9.3s] A man's right hand and forearm (@SamBefore — large, clean, NO ink anywhere, the thin worn steel wedding band, the grey marl cuff) enter from screen-left, unhurried, and settle flat on the folded wool — and rest there half a second, not gripping.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 85 mm f/2 equivalent.
LIGHT — DAY STATE: the tube run is directly overhead, above and slightly behind the camera: top light, faintly green, even and shadowless, no shadow deeper than a half-tone, doubling as long soft streaks down the buffed vinyl and lying in slow faint reflections across any glazing.
SOUND — None, in either segment. Not a voice anywhere in this generation. SFX only.
ENDING FRAME, the state this shot hands over — The empty plastic chair, centred, in the dim green-grey corridor — no scarf, no red, no one.
AVOID — visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, subjects looking at camera, slow motion.
```
