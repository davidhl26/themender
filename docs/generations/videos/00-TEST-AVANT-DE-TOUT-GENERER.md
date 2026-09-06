# LE TEST — deux générations, avant de lancer les 62

> Objectif : savoir si le raccord tient **sur ton film**, pas en théorie.
> On génère 1A, puis 1B en lui attachant 1A. Si Sam se lève et traverse sans que la cuisine
> change de forme, la méthode tient. Sinon on le saura pour ~2 générations au lieu de 62.

---

## AVANT DE COMMENCER

| | |
|---|---|
| Crédits | **39,76.** Un plan 5 s en 1080p en coûte ~45. **Passe en 480p** et lis le coût que l'interface affiche AVANT de confirmer. |
| Éléments requis | `@SamBefore` · `@Maeve` · `@Kitchen` — ils existent déjà |
| Image d'ancrage | LIEU-01 **IMAGE 2** `abf2d210` pour 1A · LIEU-01 **IMAGE 3** `e9dc3786` (ANGLE H) pour 1B |

---

## ÉTAPE 1 — générer 1A

1. Higgsfield → **Seedance 2.5**, mode **omni_reference**.
2. Réglages : **21:9 · 480p · durée 10 s · sound off**.
3. Joins les Éléments **@SamBefore + @Maeve + @Kitchen**.
4. Joins **LIEU-01 IMAGE 2** (`abf2d210`). S'il y a un champ `start_image`, mets-la dedans ;
   s'il n'y en a pas, joins-la en référence ordinaire — la ligne ANCHOR IMAGE lui donne son rôle.
5. **Aucune vidéo attachée.** 1A est la tête de chaîne.
6. Colle le texte ci-dessous, **rien d'autre**.

```
SHOT — A wife has just burned the toast in the golden light of the window above the stove. Her husband is at the table behind her, and neither of them is in any hurry.
CONTINUITY — No video is attached. This is the head of its chain: it sets the light, the grain and the skin rendering every following shot will be matched to.
ANCHOR IMAGE — THE ATTACHED IMAGE IS THE FIRST FRAME: opening composition, every body's position and pose, every prop's state, the scene, the camera direction. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — One single shot, no cut. Wide across the room, camera on the west side at eye level, about 145 cm high, operated and breathing, carried rather than nailed down. @Maeve stands at the gas range screen-right at x=68%, half-silhouetted in the window's gold directly above the range. @SamBefore is SEATED at the table screen-left at x=30%, three-quarter to camera, turned toward her.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.4s] Her right hand reaches down to the front-left knob and TURNS THE GAS OFF — the blue flame shrinks and dies, the sizzle sinks to a whisper. [2.4-4.7s] SHE TURNS HER BACK TO THE RANGE AND FACES THE ROOM, both hands coming to rest on the range edge either side of her hips, her eyes finding his: "I think I burned the toast." [4.7-7.1s] He answers from the table without moving. She answers back, amused on the last word: "It's broken." — pause — "We're saving money." [7.1-9.4s] A WARM SMILING SILENCE, both of them still, looking at each other across the room, the steam of the two cups crossing the bar of light between them.
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the ACTION stages above: no added expression, no widened eyes, no trembling lip, no theatrical breath.
CAMERA — Anamorphic 40 mm f/2.8 equivalent, wide open, handheld but settled, breathing rather than drifting. No push in, no zoom, no rack focus.
LIGHT — One source only: the single window directly above THE GAS RANGE on the east wall, warm gold morning light toward camera. No lamp, no practical, no fill, no second source. Nothing underexposed, no grey, no cold cast.
SOUND — [2.6-4.0s] @Maeve, smiling, half confession half laugh: "I think I burned the toast." [4.7-6.1s] @SamBefore, gentle, deadpan, no edge: "Why don't you use the toaster?" [6.8-8.6s] @Maeve, relaxed, matter-of-fact, amused on the last word: "It's broken." "We're saving money." Nobody else speaks.
ENDING FRAME, the state this shot hands over — The wide of the kitchen from the west side, static and settled: @SamBefore SEATED at the table screen-left, both palms flat on the table edge, the spoon set down beside his bowl, smiling up at her; @Maeve STANDING at the range screen-right, her back against it and facing the room, both hands on the range edge either side of her hips; both cups steaming, the pan smoking very thinly under the window, the gas off.
AVOID — a toaster, any toaster visible anywhere, the man standing up, the man rising from his chair, the woman walking away from the range, a knife or spatula or any utensil in her hands, the toast leaving the pan, toast or bread or a plate on the table, food being served, a third person in the kitchen.
```

**Ce que tu regardes en sortie de 1A**
- La cuisine ressemble-t-elle à `@Kitchen` ? Fenêtre **au-dessus de la gazinière**, à droite ?
- Sam reste-t-il **assis** tout du long ? (le prompt l'interdit de se lever)
- Y a-t-il un grille-pain ? (il est interdit — c'est le test de l'AVOID)

Si 1A rate déjà, **arrête-toi là et envoie-moi le résultat.** Inutile de payer 1B.

---

## ÉTAPE 2 — générer 1B, en lui attachant 1A

1. Même modèle, **Seedance 2.5 · omni_reference · 21:9 · 480p · durée 14 s · sound off**.
2. Mêmes Éléments : **@SamBefore + @Maeve + @Kitchen**.
3. **Attache le clip 1A que tu viens de générer** en `video_references`. ← c'est tout le test.
4. Image d'ancrage : **LIEU-01 IMAGE 3** `e9dc3786` (ANGLE H) — c'est le cadre d'arrivée.
5. Colle le texte ci-dessous.

```
SHOT — A husband gets up from his kitchen table, crosses the room and plants himself in front of his wife. They hold one smiling beat face to face in the window's gold, and he puts his arms around her and draws her in.
CONTINUITY — VIDEO 1 is the shot immediately before this one, in the same room, the same minute. ITS LAST FRAME IS THIS GENERATION'S BOUNDARY FRAME. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: open on the INHERITED STATE line below, already true, nothing replayed, then move on. CONNECT NATURALLY, NOT IDENTICALLY. TAKE from VIDEO 1 its light level and direction, its grain, its skin rendering, and the way its camera behaves. DO NOT TAKE its framing beyond the first instant.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @SamBefore: left third of frame, SEATED at the table, both palms flat on its edge, the spoon beside his bowl, x=30%, filling 48% of frame height. @Maeve: right third of frame, STANDING at the range with her back against it and facing the room, x=68%, filling 62% of frame height. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY.
ANCHOR IMAGE — the attached image is the framing this shot ARRIVES AT in its second half: a straight-on two-shot of the two of them in front of the gas range, chest height. It is a composition reference, not the first frame. Take nothing else from it — no border, no backdrop, no empty-room staging.
OPENING FRAME — ONE SINGLE CONTINUOUS UNCUT TAKE, 14 seconds, real time, NO CUT ANYWHERE. It opens on the wide from the west side at eye level 145 cm — the frame VIDEO 1 ends on — and the camera travels with him as he crosses, settling into the straight-on two-shot at the range.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-3.4s] HE RISES, AND THE WHOLE RISE IS SEEN: the weight goes into his palms first, the tendons standing on the backs of his hands, his shoulders coming forward over the table, then he is up. Nothing is skipped and nothing happens off-screen. [3.4-6.8s] HE CROSSES, three unhurried steps on the tile, and the camera goes with him, drifting right and forward at his pace, a beat behind him, the way a person following would. He stops face to face with her and they hold one smiling beat. [6.8-10.2s] HIS ARMS GO AROUND HER AND THE MOVEMENT IS SEEN WHOLE: the right arm first and low around the small of her back, the left following a beat later and higher, her two hands coming flat on his chest, foreheads settling together. [10.2-14.0s] A TRUE SILENCE, then the two lines, then held to the end — forehead against forehead, both pairs of eyes closed, only their breathing moving, and the two breaths DO NOT fall into step.
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the ACTION stages above: no added expression, no widened eyes, no trembling lip, no theatrical breath. He is SEATED at [0.0s] and standing from [3.4s]; the change of posture happens entirely in frame, never across a cut and never off-screen.
CAMERA — Anamorphic 50 mm f/2 equivalent, wide open, handheld and operated, carried rather than nailed down. One continuous move that follows him and settles; no cut, no zoom, no speed ramp, no slow motion.
LIGHT — One source only: the single window directly above THE GAS RANGE on the east wall, warm gold morning light toward camera, the two of them half-silhouetted in it by the end. No lamp, no practical, no fill, no second source.
SOUND — [11.6-12.4s] @Maeve, whispered, forehead to forehead, eyes closed: "Love you." [12.9-13.6s] @SamBefore, lower, certain, just as quietly: "Love you more." Nobody else speaks. Neither line is repeated.
ENDING FRAME, the state this shot hands over — The two of them chest-up and half-silhouetted in the window's gold, forehead resting against forehead, both pairs of eyes closed, her two hands flat on his chest one slightly higher than the other, his arms wrapped around her waist, one last thin thread of smoke rising from the cooling pan under the window.
AVOID — a kiss, kissing, mouths touching, an open-mouthed kiss, the embrace played long or theatrical, tears, crying, sadness, a cut of any kind, a jump in his position, him standing up off-screen, a toaster, any toaster visible anywhere.
```

---

## ÉTAPE 3 — la seule chose à regarder

Mets 1A et 1B bout à bout et réponds à **cinq questions**. C'est tout le test.

| # | Question | Ce que ça prouve |
|---|---|---|
| 1 | Au premier frame de 1B, Sam est-il **assis**, à gauche, les paumes à plat ? | Le raccord d'état tient |
| 2 | La cuisine est-elle **la même pièce** — fenêtre au-dessus de la gazinière, à droite ? | La géométrie tient |
| 3 | La lumière et le grain sont-ils **les mêmes** entre les deux clips ? | `video_references` fait son travail |
| 4 | **Le voit-on se lever et traverser**, sans coupe, sans saut ? | Les 4 étapes sont lues |
| 5 | Est-ce qu'il rate quelque chose que l'AVOID interdit (baiser, grille-pain, coupe) ? | La liste d'interdits est lue |

**Envoie-moi les deux clips et tes réponses.** Selon ce qui casse, je sais quoi corriger :

- **1 casse** → le raccord doit passer par la dernière frame de 1A en image, pas par `video_references` seul.
- **2 casse** → il faut réinjecter le bloc GEO, même court.
- **3 casse** → `video_references` n'est pas lu comme on croit ; on passe à `video_extension`.
- **4 casse** → le prompt est encore trop long, ou les étapes trop chargées ; on descend à 3 étapes.
- **5 casse** → l'AVOID est trop bas dans le prompt (le milieu est enterré) ; on le remonte.

---

## SI TU VEUX LA RÉPONSE À L'AUTRE QUESTION (optionnel, 1 génération de plus)

Refais **exactement l'étape 2**, mêmes réglages, mêmes pièces jointes, mais en collant cette fois
le bloc **long** de 1B (`PRET-SEQ-01.md`, ~5 200 mots). Compare les deux 1B.
C'est la seule façon de savoir si le court fait mieux que le long **sur ton film**.
Ne la fais que s'il te reste des crédits après les deux premières.
