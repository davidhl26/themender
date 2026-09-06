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
CONTINUITY — VIDEO 1 is an earlier shot of the same film (8E), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition, framing, or ANY OF ITS AUDIO — not its dialogue, not its voices, not one line spoken in it.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — Wide, eye level at 160 cm, from the near kerb directly across the road from the shelter, static, locked off.
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-3.1s] Starting positions, held until described otherwise: @SamSDF SEATED inside the shelter at x=62%, filling 30% of frame height, motionless, a banked dark mass under the flickering sodium, HIS HOOD PULLED FAR FORWARD AND HIS HEAD BOWED TO HIS KNEES so the inside of the hood is solid black — beard, cracked lips, chin, chest, blankets read; [3.1-6.3s] She steps off the near kerb and starts across the wet road toward him, walking diagonally away from the lens, pace even — not slow, not hurried: decided. [6.3-9.4s] She slows over two steps and stops, TWO PACES from the bench, at the inner edge of the cone.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — one sodium street lamp on the shelter roofline is the only source in the world: a hard orange cone with a buzzing flicker, one moth circling the lamp head and ticking against the glass.
SOUND — NOBODY SPEAKS IN THIS ENTIRE GENERATION: not one line, not one word, not one murmur, and NO LINE IS CARRIED OVER FROM THE ATTACHED VIDEO. SFX only.
ENDING FRAME, the state this shot hands over — @Nora from three-quarter rear at x=45%, stopped two paces from the bench inside the cone's edge, hands in her pockets, breath steaming;
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
CONTINUITY — VIDEO 1 is the shot immediately before this one (9A). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the INHERITED STATE line below, already true, nothing replayed, then move on. CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin and camera behaviour. DO NOT TAKE its framing, AND TAKE NOTHING OF ITS AUDIO — not its dialogue, not its voices, not one line spoken in it; every line heard in it belongs to the previous shot and must never be heard again here.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @SamSDF: centre of frame, SEATED, x=62%, filling 30% of frame height. @Nora: centre of frame, STANDING, x=45%, filling 60% of frame height. Nothing in this list may be re-placed, re-lit or improved.
OPENING FRAME — Frame contents, nothing else in the world: the top edge of frame across his upper lip;
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-3.3s] Frame contents, nothing else in the world: the top edge of frame across his upper lip; [3.3-6.6s] Frame contents: the right side of her parka fills the frame at x=50% and 80% of frame height, the worn cuff and her bare right hand already at the pocket mouth; [6.6-9.9s] The paper is torn back in one movement — pulled, not unwrapped, no ceremony — and the bread is open in his lap, THE PAPER STILL IN HIS LEFT HAND. [9.9-13.2s] THE JAW STOPS DEAD in the middle of the mouthful.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 85 mm f/2 equivalent.
LIGHT — one sodium street lamp on the shelter roofline is the only source in the world: a hard orange cone with a buzzing flicker, one moth circling the lamp head and ticking against the glass.
SOUND — NOBODY SPEAKS IN THIS ENTIRE GENERATION: not one line, not one word, not one murmur, and NO LINE IS CARRIED OVER FROM THE ATTACHED VIDEO. SFX only.
ENDING FRAME, the state this shot hands over — The close-up cropped across his upper lip: the front of the hood, the matted beard with a crumb caught in it, the lips just closed after the line, the jaw NOT working, and low in frame his closed LEFT fist gripping the crumpled paper folded over the half-eaten bread, resting on the blanket over his left knee, his right hand empty beside it;
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
SHOT — Still holding the folded half of the sandwich shut in his left fist, he raises his other arm and points up the black road; he gives her the direction flat, without looking at her.
CONTINUITY — VIDEO 1 is the shot immediately before this one (9B). ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the state VIDEO 1 ends on, already true, nothing replayed, then move on. CONNECT NATURALLY, NOT IDENTICALLY. TAKE its light, grain, skin and camera behaviour. DO NOT TAKE its framing, AND TAKE NOTHING OF ITS AUDIO — not its dialogue, not its voices, not one line spoken in it; every line heard in it belongs to the previous shot and must never be heard again here.
OPENING FRAME — Starting positions: @SamSDF SEATED on the bench at x=45%, filling 75% of frame height, head bowed toward the road at his feet, the top edge of frame across his upper lip — the front of the hood, the beard, the cracked lips, the chin, the chest, the blankets, the hands, and nothing above the upper lip: no nose, no eyes, no brow.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.3s] Starting positions: @SamSDF SEATED on the bench at x=45%, filling 75% of frame height, head bowed toward the road at his feet, the top edge of frame across his upper lip — the front of the hood, the beard, the cracked lips, the chin, the chest, the blankets, the hands, and nothing above the upper lip: no nose, no eyes, no brow. [2.3-4.6s] His RIGHT arm rises off the blanket and crosses the whole frame in one line, at chest height, well below the top edge — the frayed fingerless glove, the grease-black back of the hand, the finger held out toward the dark of the road at frame right — and STAYS there, extended. [4.6-6.9s] Starting positions: the shelter A LONE NEON ISLAND IN TOTAL BLACK at the centre-distance, x=55%, filling 30% of frame height, its sodium cone wearing a wide dim halo in the ground mist — @SamSDF small and bowed on the bench inside it, HIS HOOD PULLED FAR FORWARD AND HIS HEAD BOWED TO HIS KNEES, his head a dark hooded thumbnail with no face in it at this scale, the pale folded packet showing in his closed LEFT fist on his left knee, the dead milky light box a pale grey rectangle beside him. [6.9-9.2s] His chin lifts a few degrees, no higher — the upper lip stays exactly at the frame's top edge — toward the black road at frame right.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 85 mm f/2 equivalent.
LIGHT — one sodium street lamp on the shelter roofline is the only source in the world: a hard orange cone with a buzzing flicker, one moth circling the lamp head and ticking against the glass.
SOUND — NOBODY SPEAKS IN THIS ENTIRE GENERATION: not one line, not one word, not one murmur, and NO LINE IS CARRIED OVER FROM THE ATTACHED VIDEO. SFX only.
ENDING FRAME, the state this shot hands over — The shelter a lone neon island in total black: @SamSDF small and bowed under the tube, his hooded head a dark thumbnail with no face in it, the pale folded packet gripped in his closed LEFT fist on his left knee, the dead milky light box a pale grey rectangle beside him — only his reflection on the wet asphalt, @Nora gone into the black.
AVOID — visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, subjects looking at camera, slow motion.
```
