# PROMPTS COURTS — SÉQUENCE 06

> ~300 mots par plan, l'ordre recommandé par Higgsfield et ByteDance.
> Le détail complet reste dans `PRET-SEQ-06.md` : géométrie GEO, verrous, raccords numérotés.
> **C'est CETTE version qu'on colle dans Higgsfield.** L'autre est le document de tournage.

## 6A — plan 6.1 « Le forum » *(12 s de rushes → 7 s au montage · Elements : @Nora + @NoraBedroom · start frame : LIEU-08 IMAGE 3)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 12 s |
| **Éléments** | @Nora + @NoraBedroom |
| **`start_image`** | LIEU-08 IMAGE 3 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — Alone at night in a dark bedroom, @Nora reads a page on her laptop, scrolls once, stops on something, and lifts her eyes off the screen toward the black window.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (5D), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition, framing, or ANY OF ITS AUDIO — not its dialogue, not its voices, not one line spoken in it.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Sam: centre of frame, SEATED, x=56%, filling 42% of frame height. @Milo: centre of frame, SEATED, x=38%, filling 26% of frame height. @Nora: centre of frame, SEATED, x=50%, filling 70% of frame height. Nothing in this list may be re-placed, re-lit or improved.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Medium from three-quarter behind her left shoulder, seated eye level, camera about 120 cm high and one metre behind the chair, static, locked off — exactly the axis of the reference angle, the desk filling the lower right half of frame, the window a black rectangle screen-right.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.8s] Starting positions, held until described otherwise: @Nora SEATED at x=55%, three-quarter back to camera, filling 58% of frame height, her face in lost profile toward the screen; [2.8-5.6s] Absolutely nothing moves in the frame except her breathing at the lower left corner and the faint flicker of the panel's own light. [5.6-8.4s] ONE SINGLE SCROLL, and one only: the whole field of pale grey blocks slides upward once, smoothly, about a third of the screen height, and settles. [8.4-11.2s] Starting positions: her face fills the frame at x=50%, 78% of frame height, lit cold blue-white from just below front;
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 85 mm f/2 equivalent.
LIGHT — motivated sources only, never more than two lit at once, and the two temperatures never mix.
SOUND — NOBODY SPEAKS IN THIS ENTIRE GENERATION: not one line, not one word, not one murmur, and NO LINE IS CARRIED OVER FROM THE ATTACHED VIDEO. SFX only.
ENDING FRAME, the state this shot hands over — Her face front-on filling the frame, lit cold blue from below, eyes lifted just past the unseen screen toward the dark window, the sodium rim in her hair, everything behind her blue-black.
AVOID — readable text on the screen, legible letters, words, digits or interface on the screen, characters of any alphabet on the screen, a cursor, an icon, a photograph, a map, a drawing or an image on the screen.
```

## 6A-bis — SECOURS de 6A *(6 s · à ne lancer QUE si le shot 2 de 6A sort avec des caractères à l'écran, une icône, un curseur ou une fenêtre de navigateur — c'est-à-dire dès qu'il est incalable en POST · Elements : @NoraBedroom · start frame : LIEU-08 IMAGE 3)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 6 s |
| **Éléments** | @NoraBedroom |
| **`start_image`** | LIEU-08 IMAGE 3 |
| **`video_references`** | *aucune — c'est une tête de chaîne* |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — A laptop screen alone in a dark empty bedroom, holding a page that is only light and blocks.
CONTINUITY — no video attached. This is the head of its chain: it sets the light, grain and skin rendering the following shots match. THE ATTACHED IMAGE IS THE FIRST FRAME — it fixes the opening composition, every body position and pose, every prop state and the camera direction; take nothing else from it, no border, no backdrop, no empty-room staging.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Static, camera about 105 cm high and 45 cm from the laptop, the screen square to the lens and IN FOCUS, locked off, absolutely no drift.
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.0s] Nothing moves at all except the panel's own faint light and the grain of the image. [1.0-2.0s] Nothing moves at all except the panel's own faint light and the grain of the image. [2.0-3.0s] ONE SINGLE SCROLL, and one only: the whole field of pale grey blocks slides upward once, smoothly, about a third of the screen height, and settles.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 85 mm f/2 equivalent.
LIGHT — motivated sources only, never more than two lit at once, and the two temperatures never mix.
SOUND — NOBODY SPEAKS IN THIS ENTIRE GENERATION: not one line, not one word, not one murmur, and NO LINE IS CARRIED OVER FROM THE ATTACHED VIDEO. SFX only.
ENDING FRAME, the state this shot hands over — The laptop screen square to the lens, filling the frame, an even cold blue-white field with its motionless pale grey blocks and not one character on it;
AVOID — readable text on the screen, legible letters, words, digits or interface on the screen, characters of any alphabet on the screen, a cursor, an icon, a photograph, a map, a drawing or an image on the screen.
```

## 6B — plan 6.2 « Le cri » *(12 s de rushes → 9 s au montage · Elements : @Nora + @BackGallery · start frame : LIEU-09 IMAGE 2 ; l'IMAGE 3 est l'axe du shot 2)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 12 s |
| **Éléments** | @Nora + @BackGallery |
| **`start_image`** | LIEU-09 IMAGE 2 ; l'IMAGE 3 est l'axe du shot 2 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — At midnight @Nora comes out onto the rear gallery of her building, takes hold of the rail, hesitates, and throws one question out loud at the rooftops.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (6A), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition, framing, or ANY OF ITS AUDIO — not its dialogue, not its voices, not one line spoken in it.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Nora: centre of frame, SEATED, x=55%, filling 58% of frame height. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY: whatever brought the bodies and the props here has already happened in the attached video and must NOT be performed again.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Wide along the gallery, eye level, camera about 160 cm high on the gallery itself looking down its length, static, locked off — exactly the axis of the reference angle: the empty walkway running away from camera, the rail screen-left, the ajar door in the wall screen-right at x=78%, the cold blue sky, the rooftops and the far harbour cranes beyond, the warm rectangle low across the boards at the bottom frame edge.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.6s] Frame contents, nothing moving through them yet: the gallery exactly as the reference, empty, nobody in it. [2.6-5.2s] Both hands close on the rail. [5.2-7.8s] THE LINE, out loud, thrown at the rooftops, louder than she meant it, the voice cracking on the last word: "Why did my mother die?" Her chin comes up on the line; [7.8-10.4s] Stillness.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — One geometry by night and one by day, never mixed.
SOUND — EXACTLY 1 SPOKEN LINE IN THIS ENTIRE GENERATION, written out here and nothing else. Any other speech, any line carried over from the attached video, any murmur or half-word is an ERROR. FROM [0.0s] TO [6.6s] NOBODY SPEAKS AT ALL: no line, no word, no murmur, no breath shaped like speech. [6.6-8.4s] @Nora, out loud to the night, thrown at the rooftops, louder than she meant it, the voice cracking on the last word: "Why did my mother die?" SFX only.
ENDING FRAME, the state this shot hands over — Her back at the gallery rail, already turning away toward the ajar door, both hands off the rail and at her sides, the empty washing line sagging above, the rooftops and the harbour cranes beyond, the warm rectangle unchanged and unremarked at the lower frame edge — nothing in the world has answered.
AVOID — a second person, a man, any figure or silhouette in any window, doorway or yard, a lit kitchen window framed directly, an insert of a window, a window lighting up or going dark, a curtain moving, a door opening, camera movement.
```

## 6B-bis — SECOURS de 6B *(6 s · à ne lancer QUE si le shot 2 de 6B rate : une fenêtre allumée ou une silhouette entre au cadre, une lumière change pendant la réplique, ou la voix sort avec de l'écho · Elements : @Nora + @BackGallery · start frame : LIEU-09 IMAGE 3, au rail)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 6 s |
| **Éléments** | @Nora + @BackGallery |
| **`start_image`** | LIEU-09 IMAGE 3, au rail |
| **`video_references`** | *aucune — c'est une tête de chaîne* |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — At midnight, at the rail of a rear gallery, @Nora hesitates and throws one question out loud at the rooftops.
CONTINUITY — no video attached. This is the head of its chain: it sets the light, grain and skin rendering the following shots match. THE ATTACHED IMAGE IS THE FIRST FRAME — it fixes the opening composition, every body position and pose, every prop state and the camera direction; take nothing else from it, no border, no backdrop, no empty-room staging.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Medium close along the rail, three-quarter left profile, eye level, camera about 160 cm high and 1.2 m from her, static, locked off, one size tighter than the main version so the frame is filled by her, the rail and the night alone.
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.8s] Starting positions, held until described otherwise: @Nora at x=45%, filling 82% of frame height, in three-quarter left profile facing the dark rooftops screen-left, both hands on the rail, weight forward, head slightly bowed. [1.8-3.6s] Stillness. [3.6-5.4s] Held to the end, no further movement: her hands still on the rail, her eyes open again on the rooftops, her breath clouding once more.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 85 mm f/2 equivalent.
LIGHT — One geometry by night and one by day, never mixed.
SOUND — EXACTLY 1 SPOKEN LINE IN THIS ENTIRE GENERATION, written out here and nothing else. Any other speech, any line carried over from the attached video, any murmur or half-word is an ERROR. FROM [0.0s] TO [1.6s] NOBODY SPEAKS AT ALL: no line, no word, no murmur, no breath shaped like speech. [1.6-3.4s] @Nora, out loud to the night, thrown at the rooftops, louder than she meant it, the voice cracking on the last word: "Why did my mother die?" SFX only.
ENDING FRAME, the state this shot hands over — Her three-quarter left profile at the rail, both hands still on the worn bare-wood top, her eyes open again on the dark rooftops, one last cloud of breath in the sodium, the empty washing line sagging above, the night behind her unchanged — nothing has answered.
AVOID — a second person, a man, any figure or silhouette anywhere, a window in frame, a door in frame, a lit rectangle of light in frame, a window lighting up or going dark, a curtain moving, camera movement, camera tilt.
```

## 6C — plan 6.3 « L'escalier » *(8 s de rushes → 5 s au montage · Elements : @Nora + @Sam + @NoraBedroom · start frame : LIEU-08 IMAGE 4, le palier, porte entrouverte 10 cm)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 8 s |
| **Éléments** | @Nora + @Sam + @NoraBedroom |
| **`start_image`** | LIEU-08 IMAGE 4, le palier, porte entrouverte 10 cm |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — A father stands in the dark landing outside his daughter's door, just arrived at the top of the stairs, and asks one quiet question.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (6B), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition, framing, or ANY OF ITS AUDIO — not its dialogue, not its voices, not one line spoken in it.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Nora: centre of frame, STANDING, x=45%, filling 72% of frame height. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY: whatever brought the bodies and the props here has already happened in the attached video and must NOT be performed again.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Single fixed shot down the landing, eye level, camera about 160 cm high at the top of the stairs, static, locked off.
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.0s] Starting positions, held until described otherwise: @Sam a grey silhouette at x=32%, filling 74% of frame height, three-quarter back to camera, facing the lit door gap, arms at his sides, weight even on both feet, the heavy shoulders slightly slumped, the head a fraction forward. [2.0-3.9s] @Nora, flat, unhurried, through the gap, with a small pause after the first word: "Nothing. [3.9-5.9s] The door closes without slamming — a slow swing and one soft click of the latch. He does not move.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — motivated sources only, never more than two lit at once, and the two temperatures never mix.
SOUND — EXACTLY 2 SPOKEN LINES IN THIS ENTIRE GENERATION, written out here and nothing else. Any other speech, any line carried over from the attached video, any murmur or half-word is an ERROR. FROM [0.0s] TO [1.5s] NOBODY SPEAKS AT ALL: no line, no word, no murmur, no breath shaped like speech. [1.5-2.4s] @Sam, quiet, low, rusty from disuse, almost swallowed: "You okay?" [3.2-4.8s] @Nora, flat, unhurried, through the gap, with a small pause after the first word: "Nothing. I stepped on something." SFX only.
ENDING FRAME, the state this shot hands over — The near-black landing, the bedroom door shut, the blade of light gone, the father's silhouette motionless at x=32% facing the closed door, arms at his sides, barely separable from the dark, nothing lit anywhere in frame.
AVOID — the man's face visible, the man's eyes, the man's profile lit, any light on the man's face or body, a rim of light on his cheek, a readable expression on the man, the man stepping forward, the man reaching for the door, the man turning away, the man going down the stairs.
```
