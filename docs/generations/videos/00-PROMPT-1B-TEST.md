# 1B — le prompt du test

> **Toutes les mentions `@` sont regroupées sur les deux premières lignes.**
> Raison : dans l'éditeur Higgsfield, un `@` collé en texte brut n'est qu'un mot — il ne se lie à
> rien. Chaque mention doit être **choisie dans le sélecteur** qui s'ouvre quand tu tapes `@`.
> Les rassembler en haut, c'est cinq sélections au même endroit au lieu d'une chasse dans le corps
> du texte. Une fois liés, les noms peuvent être repris en clair plus bas — la liaison est faite.

## Réglages

| | |
|---|---|
| **modèle** | Seedance 2.5 |
| **mode** | **References** *(= `omni_reference`. Sequel = prolonger le même plan, Prequel = idem en arrière, Edit video = retoucher)* |
| **format** | 21:9 · **720p** · bitrate high |
| **durée** | **14 s** · **son ON** |
| **`@video1`** | le clip **1A** |
| **`@image1`** | **la dernière frame de 1A** — le premier frame de 1B |
| **Éléments** | `@sambefore` · `@maeva` · `@kitchen` |

## Comment coller, en trois gestes

1. Colle tout le texte ci-dessous d'un bloc.
2. Remonte aux **deux premières lignes** : efface chaque `@…` et retape `@`, puis **choisis
   l'entrée dans le sélecteur**. Cinq fois — `@video1`, `@image1`, `@sambefore`, `@maeva`, `@kitchen`.
3. Vérifie qu'elles sont devenues des pastilles cliquables et non du texte gris. Lance.

⚠ Si un nom d'Élément diffère chez toi, prends celui du sélecteur — c'est lui qui fait foi.

## Le prompt

```
MATERIALS — @video1 is the shot immediately before this one, same room, same minute. @image1 is the last frame of that shot and IT IS THE FIRST FRAME OF THIS GENERATION. @sambefore is SAM, the husband. @maeva is MAEVE, the wife. @kitchen is the room.
ROLES — From the attached video take the light level and direction, the grain, the skin rendering and the way the camera behaves; take no framing from it beyond the first instant. From the first-frame image take the opening composition and the exact position, pose and prop state of everything in it; take nothing else from it, no border, no backdrop, no empty-room staging. From SAM, MAEVE and the room reference take identity, wardrobe, architecture and materials exactly; take none of their pose, framing, lighting or staging.
SHOT — A husband gets up from his kitchen table, crosses the room and plants himself in front of his wife. They hold one smiling beat face to face in the window's gold, and he puts his arms around her and draws her in.
CONTINUITY — ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: this clip opens on the first-frame image exactly, everything in it already true and nothing replayed, and only then does the action begin.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — SAM: left third of frame, SEATED at the table, both palms flat on its edge, the spoon beside his bowl, x=30%, filling 48% of frame height. MAEVE: right third of frame, STANDING at the range with her back against it and facing the room, both hands on the range edge either side of her hips, x=68%, filling 62% of frame height. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY.
OPENING FRAME — ONE SINGLE CONTINUOUS UNCUT TAKE, 14 seconds, real time, NO CUT ANYWHERE. It opens on the first-frame image — the wide of the kitchen from the west side, eye level 145 cm, the single window above the gas range behind them — and the camera travels with him as he crosses, settling into a straight-on chest-height two-shot of the two of them in front of the range.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-3.4s] HE RISES, AND THE WHOLE RISE IS SEEN: the weight goes into his palms first, the tendons standing on the backs of his hands, his shoulders coming forward over the table, then he is up. Nothing is skipped and nothing happens off-screen. [3.4-6.8s] HE CROSSES, three unhurried steps on the tile, and the camera goes with him, drifting right and forward at his pace, a beat behind him, the way a person following would. He stops face to face with her and they hold one smiling beat. [6.8-10.2s] HIS ARMS GO AROUND HER AND THE MOVEMENT IS SEEN WHOLE: the right arm first and low around the small of her back, the left following a beat later and higher, her two hands coming flat on his chest, foreheads settling together. [10.2-14.0s] A TRUE SILENCE, then the two lines, then held to the end — forehead against forehead, both pairs of eyes closed, only their breathing moving, and the two breaths DO NOT fall into step.
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the ACTION stages above: no added expression, no widened eyes, no trembling lip, no theatrical breath. SAM is SEATED at [0.0s] and standing from [3.4s]; the change of posture happens entirely in frame, never across a cut and never off-screen.
CAMERA — Anamorphic 50 mm f/2 equivalent, wide open, handheld and operated, carried rather than nailed down. One continuous move that follows him and settles; no cut, no zoom, no speed ramp, no slow motion.
LIGHT — One source only: the single window directly above THE GAS RANGE on the east wall, warm gold morning light toward camera, the two of them half-silhouetted in it by the end. No lamp, no practical, no fill, no second source. Nothing underexposed, no grey, no cold cast.
SOUND — Spoken dialogue, two lines and no more. [11.6-12.4s] MAEVE, whispered, forehead to forehead, eyes closed, barely voiced: "Love you." [12.9-13.6s] SAM, lower in pitch than she was, certain, just as quietly: "Love you more." Nobody else speaks, neither line is repeated, and no other word is added. Under them, room tone only: two breaths out of step, the faint tick of the cooling pan, wool moving against wool. NO MUSIC of any kind, no score, no drone, no ambient pad.
ENDING FRAME, the state this shot hands over — The two of them chest-up and half-silhouetted in the window's gold, forehead resting against forehead, both pairs of eyes closed, her two hands flat on his chest one slightly higher than the other, his arms wrapped around her waist, one last thin thread of smoke rising from the cooling pan under the window.
AVOID — a kiss, kissing, mouths touching, an open-mouthed kiss, the embrace played long or theatrical, tears, crying, sadness, music, a score, a cut of any kind, a jump in his position, him standing up off-screen, a toaster, any toaster visible anywhere.
```

## Les six questions, une fois sorti

| # | Question | Ce que ça prouve | Si ça casse |
|---|---|---|---|
| 1 | Au premier frame, Sam est-il **assis** à gauche, paumes à plat ? | le raccord d'état tient | passer par **Sequel** |
| 2 | **Même cuisine** — fenêtre au-dessus de la gazinière, à droite ? | la géométrie tient | réinjecter le bloc GEO |
| 3 | Lumière, grain, peau **identiques** à 1A ? | `@video1` fait son travail | `@video1` n'est pas lu comme on croit |
| 4 | **Le voit-on se lever et traverser**, sans coupe ni saut ? | les 4 étapes sont lues | descendre à 3 étapes |
| 5 | Un baiser, un grille-pain, une musique, une coupe ? | l'AVOID est lu | remonter l'AVOID plus haut |
| 6 | **La bouche forme-t-elle les deux répliques** ? | les lignes SOUND pilotent le jeu | écrire les répliques dans l'ACTION |
