# PROMPTS COURTS — SÉQUENCE 05

> ~300 mots par plan, l'ordre recommandé par Higgsfield et ByteDance.
> Le détail complet reste dans `PRET-SEQ-05.md` : géométrie GEO, verrous, raccords numérotés.
> **C'est CETTE version qu'on colle dans Higgsfield.** L'autre est le document de tournage.

## 5A — plan 5.1 « Les quatre tasses, puis trois » *(12 s de rushes → 5 s au montage · Elements : @Sam + @Nora + @Milo + @Mei + @Restaurant · start frame : LIEU-07 IMAGE 2)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 12 s |
| **Éléments** | @Sam + @Nora + @Milo + @Mei + @Restaurant |
| **`start_image`** | LIEU-07 IMAGE 2 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — The owner brings tea to a family of three she has known for years and, out of old habit, sets FOUR cups — freezes — and…
CONTINUITY — VIDEO 1 is an earlier shot of the same film (4D), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Anna: left third of frame, SEATED, x=26%, filling 66% of frame height. @Nora: centre of frame, STANDING, x=40%, filling 82% of frame height. Nothing in this…
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — Medium, eye level, static, locked off, from the middle of the room toward the family table, the window behind it at screen-left, the lacquered counter running away deep…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.8s] Starting positions, held until described otherwise: @Sam SEATED at x=58%, three-quarter view facing camera, filling 45% of frame height — his bulk low in… [2.8-5.5s] Frame contents: the dark green cloth fills the frame. Cup one, set at Sam's place, top of frame — one small porcelain tap on… [5.5-8.3s] Cup two, at Milo's place, upper-left. Cup four travels toward the BARE place at the bottom of frame — and the hand slows through… [8.3-11.1s] THE HAND DOES NOT LET GO. @Mei STANDING at x=52%, bent slightly over the table, her right hand still closed on the fourth cup…
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — the weak amber paper lanterns above each table, each pool barely a metre wide, dying into shadow between…
SOUND — None. Nobody speaks in this generation — the service happens without one word. SFX only.
ENDING FRAME, the state this shot hands over — The family table with exactly THREE cups steaming, the metal teapot at centre, the bare place bare, the empty chair pushed in; @Sam mid-cut over @Milo's…
AVOID — visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, readable menus, readable signage.
```

## 5B-1 — plan 5.2, première moitié *(10 s de rushes → 7,2 s au montage · Elements : @Nora + @Mei + @Asha + @Fatiha + @Restaurant · start frame : LIEU-07 IMAGE 4 — L'AXE UNIQUE DE 5.2)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @Nora + @Mei + @Asha + @Fatiha + @Restaurant |
| **`start_image`** | LIEU-07 IMAGE 4 — L'AXE UNIQUE DE 5.2 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — At the next table over, three women who have known each other for years are talking fast across each other about somebody everybody knows — not…
CONTINUITY — VIDEO 1 is the shot immediately before this one (5A). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the inherited state below, already true, nothing replayed, then move on. It must CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin rendering and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Sam: centre of frame, SEATED, x=58%, filling 45% of frame height. @Milo: centre of frame, SEATED, x=38%, filling 30% of frame height. @Nora: left third of…
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — THE AXIS. Medium three-shot of the round table, eye level, static, locked off, no camera movement of any kind for the whole generation. No cut. Starting positions, held…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.8s] Starting positions, held until described otherwise: extreme near foreground SCREEN-LEFT at x=9%, LARGE and SOFT, out of focus, the back three-quarter of @Nora's head… [1.8-3.5s] @MEI CUTS ACROSS HER LAST WORD, flat, amused, without lifting her eyes from her own cup: "Everyone's grandmother saw him." Only her jaw and… [3.5-5.3s] @ASHA, level, one word, chopsticks still in her hand, eyes on the plates: "Msimulizi." @MEI laughs — one short breath of a laugh, the… [5.3-7.0s] @MEI, still on that breath: "I thought he was ours." Half a second where nobody speaks.
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — the weak amber paper lanterns above each table, each pool barely a metre wide, dying into shadow between…
SOUND — Four voices' worth of talk in one table's worth of time, quick and overlapping at the joins, each line landing on the tail of the one before, about…
ENDING FRAME, the state this shot hands over — The women's round table under the green tank glow, mid-meal and mid-conversation: @Fatiha drawing breath, her hands above the cloth; @Asha's eyes on Fatiha, chopsticks in…
AVOID — visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, readable menus, readable signage.
```

## 5B-2 — plan 5.2, seconde moitié, jusqu'à « More tea? » *(8 s de rushes → 5,8 s au montage · Elements : @Nora + @Mei + @Asha + @Fatiha + @Restaurant · start frame : LE DERNIER FRAME DE 5B-1 — repli : LIEU-07 IMAGE 4)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 8 s |
| **Éléments** | @Nora + @Mei + @Asha + @Fatiha + @Restaurant |
| **`start_image`** | LE DERNIER FRAME DE 5B-1 — repli : LIEU-07 IMAGE 4 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — The same three women at the same table, still talking across each other about the same man — and then they run out of it.
CONTINUITY — VIDEO 1 is the shot immediately before this one (5B-1). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the inherited state below, already true, nothing replayed, then move on. It must CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin rendering and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Asha: left third of frame, SEATED, x=27%. @Mei: centre of frame, SEATED, x=48%, filling 50% of frame height. @Fatiha: right third of frame, SEATED, x=73%, filling…
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — THE SAME AXIS, THE SAME FRAMING, NO CUT. Medium three-shot of the round table, eye level, static, locked off, no camera movement of any kind for the whole…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.6s] Starting positions, exactly the positions the previous shot ended on: @Asha SEATED at x=27%, three-quarter to camera, upright, filling 55% of frame height, chopsticks… [1.6-3.2s] @MEI CUTS IN, flat, finishing it for her, without lifting her eyes from her cup: "Never a big one." [3.2-4.8s] @ASHA lays her chopsticks down FLAT ACROSS HER OWN PLATE, one small wooden sound, and leaves her hand beside them. @ASHA, level, unhurried, the… [4.8-6.3s] @FATIHA, already elsewhere, to @Mei, ordinary: "More tea?" — and on the second word her right hand goes out and closes around the dented…
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — the weak amber paper lanterns above each table, each pool barely a metre wide, dying into shadow between…
SOUND — Quick, overlapping at the joins, about four words a second, nobody projecting, nobody performing. [0.20-0.95s] @Asha, level: "He's everybody's." — [0.85-2.65s] @Fatiha, over the tail of that: "He…
ENDING FRAME, the state this shot hands over — The women's round table under the green tank glow, already onto something else: @Fatiha's right hand closed on the dented metal teapot's handle, the pot still…
AVOID — visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, readable menus, readable signage.
```

## 5C — l'insert des mains de Sam *(6 s de rushes → 0,7 s au montage · Elements : @Sam + @Restaurant · aucune start frame — l'insert est décrit au prompt)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 6 s |
| **Éléments** | @Sam + @Restaurant |
| **`start_image`** | — l'insert est décrit au prompt |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — Two large workman's hands cut @Milo's food, slowly and evenly, the way they have all evening.
CONTINUITY — VIDEO 1 is the shot immediately before this one (5B-2). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the inherited state below, already true, nothing replayed, then move on. It must CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin rendering and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Asha: left third of frame, SEATED, x=27%, filling 55% of frame height. @Mei: centre of frame, SEATED, x=48%, filling 50% of frame height. @Fatiha: right third…
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — Tight insert, high angle, static, locked off, straight down onto the plate. Shallow focus: the plate and the hands sharp, the cloth falling off soft toward the frame…
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.4s] Frame contents, held until described otherwise: @SAM'S TWO HANDS ONLY — large, the skin cracked across the knuckles, the nails short and rimmed, the… [1.4-2.9s] The rhythm continues, unchanged. [2.9-4.3s] THE HANDS STOP DEAD, on the word "face", mid-cut. The hands start again — exactly the same rhythm as before, exactly the same grip,…
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 85 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — the weak amber paper lanterns above each table, each pool barely a metre wide, dying into shadow between…
SOUND — No line is spoken on screen; nobody in frame has a mouth in frame. OFF SCREEN ONLY, from another table across the room, a woman's level unhurried voice,…
ENDING FRAME, the state this shot hands over — Straight down on the plate of flat noodles on the dark green cloth: the worn-handled knife in the right hand and the fork in the left,…
AVOID — a face, any face, a head, shoulders, a neck, a chin, eyes, hair, a profile, a reflection of a face in the cup.
```

## 5D — plan 5.3 « Le père qui coupe, et le trajet du regard » *(12 s de rushes → 6 s au montage · Elements : @Sam + @Nora + @Milo + @Mei + @Asha + @Fatiha + @Restaurant · start frame : LIEU-07 IMAGE 2)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 12 s |
| **Éléments** | @Sam + @Nora + @Milo + @Mei + @Asha + @Fatiha + @Restaurant |
| **`start_image`** | LIEU-07 IMAGE 2 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — First, the family table, wide and silent: a heavy unshaven father cutting his son's food, eyes down, cutting, cutting — on screen, a busy father and…
CONTINUITY — VIDEO 1 is the shot immediately before this one (5C). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the inherited state below, already true, nothing replayed, then move on. It must CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin rendering and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Milo: centre of frame, x=48%. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY: whatever…
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — Wide, eye level, static, locked off, from the middle of the room onto the family table, seen from BEHIND @Nora, the window behind the table at screen-left. SILENT.…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.0s] Frame contents, held until described otherwise: the whole family table in frame. Nothing happens except this: @Sam's knife and fork work over @Milo's plate,… [2.0-4.1s] Nothing happens except this: @Sam's knife and fork work over @Milo's plate, slow, even, unbroken — he cuts, and he cuts, and he cuts. [4.1-6.1s] Frame contents: @Nora centred at x=50%, chest-up, filling 70% of frame height, SEATED, three-quarter to camera; HER EYES MOVE, ONCE, AND ONLY ONCE: they… [6.1-8.2s] The fork comes down slowly, without her having eaten, and settles on the plate rim with one small click.
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — the weak amber paper lanterns above each table, each pool barely a metre wide, dying into shadow between…
SOUND — No lines. Nobody speaks anywhere in this generation, on screen or off — the conversation across the room is over and the family table has not said a…
ENDING FRAME, the state this shot hands over — @Nora's face in close-up, still; her fork down on the plate rim, the mouthful never taken; her eyes low and to the LEFT, resting where the…
AVOID — visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, readable menus, readable signage.
```

## 5D-bis — SECOURS du shot 2 de 5D *(6 s · à ne lancer QUE si le serré manque de longueur de focale, ou si le regard part vers la droite · Elements : @Nora + @Restaurant · start frame : aucune — cadre décrit au prompt · Lens Anamorphic **85 mm f/2**)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 6 s |
| **Éléments** | @Nora + @Restaurant |
| **`start_image`** | aucune — cadre décrit au prompt |
| **`video_references`** | *aucune — c'est une tête de chaîne* |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — @Nora alone in the frame at a restaurant table, her fork stopped in the air, the mouthful never taken.
CONTINUITY — no video attached. This is the head of its chain: it sets the light, grain and skin rendering the following shots match. THE ATTACHED IMAGE IS THE FIRST FRAME — it fixes the opening composition, every body position and pose, every prop state and the camera direction; take nothing else from it, no border, no backdrop, no empty-room staging.
OPENING FRAME — Close on @Nora, facing her, eye level, static, locked off, shallow depth of field, 85 mm. Frame contents: @Nora centred at x=50%, chest-up, filling 72% of frame height,…
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.2s] Frame contents: @Nora centred at x=50%, chest-up, filling 72% of frame height, SEATED, three-quarter to camera; HER EYES MOVE, ONCE, AND ONLY ONCE: they… [1.2-2.5s] Held on that. [2.5-3.7s] The fork comes down slowly, without her having eaten, and settles on the plate rim with one small click. Held to the end, no…
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 85 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — the weak amber paper lanterns above each table, each pool barely a metre wide, dying into shadow between…
SOUND — None. Nobody speaks in this generation, on screen or off. SFX only.
ENDING FRAME, the state this shot hands over — @Nora's face in close-up, still; her fork down on the plate rim, the mouthful never taken; her eyes low and to the LEFT, resting where the…
AVOID — visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, readable menus, readable signage.
```
