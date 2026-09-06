# PROMPTS COURTS — SÉQUENCE 09

> ~300 mots par plan, l'ordre recommandé par Higgsfield et ByteDance.
> Le détail complet reste dans `PRET-SEQ-09.md` : géométrie GEO, verrous, raccords numérotés.
> **C'est CETTE version qu'on colle dans Higgsfield.** L'autre est le document de tournage.

## 9A — plan 9.1 « C'est elle qui traverse » *(10 s générées → 4,8 s au montage · Elements : @Nora + @SamSDF + @BusShelter · start frame : LIEU-14 IMAGE 2, telle quelle)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @Nora + @SamSDF + @BusShelter |
| **`start_image`** | LIEU-14 IMAGE 2, telle quelle |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — A deserted bus stop at the far edge of a port town at night.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (8E), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME. It fixes the opening composition, the position and pose of every body, the state of every prop, the scene and the camera direction. Take nothing else from it: no border, no backdrop, no empty-room staging, no reference layout.
OPENING FRAME — Wide, eye level at 160 cm, from the near kerb directly across the road from the shelter, static, locked off. The exact framing of the reference: the shelter…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.4s] Starting positions, held until described otherwise: @SamSDF SEATED inside the shelter at x=62%, filling 30% of frame height, motionless, a banked dark mass under… [2.4-4.7s] Her weight shifts onto her left foot — the first movement of the sequence is hers. She steps off the near kerb and starts… [4.7-7.1s] Starting positions: @Nora STANDING mid-road at x=45%, filling 60% of frame height, three-quarter back to camera, WALKING toward the shelter, hands in pockets, her… [7.1-9.4s] She slows over two steps and stops, TWO PACES from the bench, at the inner edge of the cone.
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — one sodium street lamp on the shelter roofline is the only source in the world: a hard orange…
SOUND — No lines in this generation. Nobody speaks. SFX only.
ENDING FRAME, the state this shot hands over — @Nora from three-quarter rear at x=45%, stopped two paces from the bench inside the cone's edge, hands in her pockets, breath steaming; the camera dead behind…
AVOID — visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, subjects looking at camera, slow motion.
```

## 9B — plan 9.2 « Got anything to eat? » *(14 s générées → 8,2 s au montage · Elements : @Nora + @SamSDF + @BusShelter · pas de start frame lieu — cadres serrés)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 14 s |
| **Éléments** | @Nora + @SamSDF + @BusShelter |
| **`start_image`** | aucune — ce plan démarre sans image de départ |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — He asks for food without lifting his head.
CONTINUITY — VIDEO 1 is the shot immediately before this one (9A). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the inherited state below, already true, nothing replayed, then move on. It must CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin rendering and camera behaviour. DO NOT TAKE its framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @SamSDF: centre of frame, SEATED, x=62%, filling 30% of frame height. @Nora: centre of frame, STANDING, x=45%, filling 60% of frame height. Nothing in this list…
OPENING FRAME — Frame contents, nothing else in the world: the top edge of frame across his upper lip; the front of the hood, the matted grey beard beaded with mist…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-3.3s] Frame contents, nothing else in the world: the top edge of frame across his upper lip; He speaks first, without lifting his head —… [3.3-6.6s] Frame contents: the right side of her parka fills the frame at x=50% and 80% of frame height, the worn cuff and her bare… [6.6-9.9s] The paper is torn back in one movement — pulled, not unwrapped, no ceremony — and the bread is open in his lap, THE… [9.9-13.2s] THE JAW STOPS DEAD in the middle of the mouthful. Both hands come up into the bottom of frame and fold the crumpled paper…
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 85 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — one sodium street lamp on the shelter roofline is the only source in the world: a hard orange…
SOUND — (the vagrant's voice: the same actor as @Sam, pitched a third lower, broken by the cold — slowed delivery, no processing that alters the grain of the voice)…
ENDING FRAME, the state this shot hands over — The close-up cropped across his upper lip: the front of the hood, the matted beard with a crumb caught in it, the lips just closed after…
AVOID — visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, subjects looking at camera, slow motion.
```

## 9C — plan 9.3 « Quand tu verras du rouge » *(10 s générées → 7,0 s au montage · Elements : @Nora + @SamSDF + @BusShelter · pas de start frame lieu ; LIEU-14 IMAGE 3 telle quelle en seconde référence — cible exacte du shot 8)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @Nora + @SamSDF + @BusShelter |
| **`start_image`** | aucune — ce plan démarre sans image de départ |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — Still holding the folded half of the sandwich shut in his left fist, he raises his other arm and points up the black road; he gives…
CONTINUITY — VIDEO 1 is the shot immediately before this one (9B). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the inherited state below, already true, nothing replayed, then move on. It must CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin rendering and camera behaviour. DO NOT TAKE its framing.
OPENING FRAME — Starting positions: @SamSDF SEATED on the bench at x=45%, filling 75% of frame height, head bowed toward the road at his feet, the top edge of frame across…
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.3s] Starting positions: @SamSDF SEATED on the bench at x=45%, filling 75% of frame height, head bowed toward the road at his feet, the top… [2.3-4.6s] His RIGHT arm rises off the blanket and crosses the whole frame in one line, at chest height, well below the top edge —… [4.6-6.9s] Starting positions: the shelter A LONE NEON ISLAND IN TOTAL BLACK at the centre-distance, x=55%, filling 30% of frame height, its sodium cone wearing… [6.9-9.2s] His chin lifts a few degrees, no higher — the upper lip stays exactly at the frame's top edge — toward the black road…
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through…
CAMERA — Anamorphic 85 mm f/2 equivalent. Depth of field wide open at that stop: the plane described…
LIGHT — one sodium street lamp on the shelter roofline is the only source in the world: a hard orange…
SOUND — (the vagrant's voice: the same actor as @Sam, pitched a third lower, broken by the cold — slowed delivery, no processing that alters the grain of the voice)…
ENDING FRAME, the state this shot hands over — The shelter a lone neon island in total black: @SamSDF small and bowed under the tube, his hooded head a dark thumbnail with no face in…
AVOID — visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, subjects looking at camera, slow motion.
```
