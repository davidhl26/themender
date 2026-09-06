# 1B — le prompt du test, version définitive

> Corrigée sur trois points que David a relevés en manipulant l'interface :
> **les mentions d'Éléments sont en minuscules**, les pièces jointes se nomment
> **`@video1`** et **`@image1`** *sans espace* (avec l'espace, l'éditeur Higgsfield
> avale la mention — c'était le bug du prompt d'origine), et **le son est ON**.

## Réglages

| | |
|---|---|
| **modèle** | Seedance 2.5 |
| **le menu à quatre entrées** | choisis **References**. C'est le mode `omni_reference` : celui qui accepte à la fois les Éléments, une image et une vidéo. **Sequel** = `video_extension` forward (il prolonge littéralement le même plan), **Prequel** = la même chose en arrière, **Edit video** = retoucher une vidéo existante. |
| **format** | 21:9 · **720p** · bitrate high |
| **durée** | **14 s** |
| **son** | **ON** |
| **`@video1`** | le clip **1A** que tu viens de générer |
| **`@image1`** | **la dernière frame de 1A** — c'est le premier frame de 1B |
| **Éléments** | `@sambefore` + `@maeva` + `@kitchen` |

⚠ Les trois noms d'Éléments doivent correspondre **exactement** à ceux de ton interface.
Je les écris en minuscules comme tu me l'as dit pour `@maeva` ; si `@sambefore` ou `@kitchen`
s'écrivent autrement chez toi, corrige-les dans le texte avant de coller — une mention qui ne
résout pas est une référence perdue.

## Le prompt

```
SHOT — A husband gets up from his kitchen table, crosses the room and plants himself in front of his wife. They hold one smiling beat face to face in the window's gold, and he puts his arms around her and draws her in.
CONTINUITY — @video1 is the shot immediately before this one, same room, same minute. @image1 is its last frame and it IS THE FIRST FRAME OF THIS GENERATION. ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: this clip opens on @image1 exactly, everything in it already true and nothing replayed, and only then does the action begin. TAKE from @video1 its light level and direction, its grain, its skin rendering, and the way its camera behaves. DO NOT TAKE from @video1 any framing beyond that first instant — the camera moves on.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @sambefore: left third of frame, SEATED at the table, both palms flat on its edge, the spoon beside his bowl, x=30%, filling 48% of frame height. @maeva: right third of frame, STANDING at the range with her back against it and facing the room, both hands on the range edge either side of her hips, x=68%, filling 62% of frame height. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY.
OPENING FRAME — ONE SINGLE CONTINUOUS UNCUT TAKE, 14 seconds, real time, NO CUT ANYWHERE. It opens on @image1 — the wide of the kitchen from the west side, eye level 145 cm, the single window above the gas range behind them — and the camera travels with him as he crosses, settling into a straight-on chest-height two-shot of the two of them in front of the range.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-3.4s] HE RISES, AND THE WHOLE RISE IS SEEN: the weight goes into his palms first, the tendons standing on the backs of his hands, his shoulders coming forward over the table, then he is up. Nothing is skipped and nothing happens off-screen. [3.4-6.8s] HE CROSSES, three unhurried steps on the tile, and the camera goes with him, drifting right and forward at his pace, a beat behind him, the way a person following would. He stops face to face with her and they hold one smiling beat. [6.8-10.2s] HIS ARMS GO AROUND HER AND THE MOVEMENT IS SEEN WHOLE: the right arm first and low around the small of her back, the left following a beat later and higher, her two hands coming flat on his chest, foreheads settling together. [10.2-14.0s] A TRUE SILENCE, then the two lines, then held to the end — forehead against forehead, both pairs of eyes closed, only their breathing moving, and the two breaths DO NOT fall into step.
PERFORMANCE — Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the ACTION stages above: no added expression, no widened eyes, no trembling lip, no theatrical breath. @sambefore is SEATED at [0.0s] and standing from [3.4s]; the change of posture happens entirely in frame, never across a cut and never off-screen.
CAMERA — Anamorphic 50 mm f/2 equivalent, wide open, handheld and operated, carried rather than nailed down. One continuous move that follows him and settles; no cut, no zoom, no speed ramp, no slow motion.
LIGHT — One source only: the single window directly above THE GAS RANGE on the east wall, warm gold morning light toward camera, the two of them half-silhouetted in it by the end. No lamp, no practical, no fill, no second source. Nothing underexposed, no grey, no cold cast.
SOUND — Spoken dialogue, two lines and no more. [11.6-12.4s] @maeva, whispered, forehead to forehead, eyes closed, barely voiced: "Love you." [12.9-13.6s] @sambefore, lower in pitch than she was, certain, just as quietly: "Love you more." Nobody else speaks, neither line is repeated, and no other word is added. Under them, room tone only: two breaths out of step, the faint tick of the cooling pan, wool moving against wool. NO MUSIC of any kind, no score, no drone, no ambient pad.
ENDING FRAME, the state this shot hands over — The two of them chest-up and half-silhouetted in the window's gold, forehead resting against forehead, both pairs of eyes closed, her two hands flat on his chest one slightly higher than the other, his arms wrapped around her waist, one last thin thread of smoke rising from the cooling pan under the window.
AVOID — a kiss, kissing, mouths touching, an open-mouthed kiss, the embrace played long or theatrical, tears, crying, sadness, music, a score, a cut of any kind, a jump in his position, him standing up off-screen, a toaster, any toaster visible anywhere.
```

## Les six questions, une fois sorti

| # | Question | Ce que ça prouve |
|---|---|---|
| 1 | Au premier frame, @sambefore est-il **assis** à gauche, les paumes à plat ? | le raccord d'état tient |
| 2 | Est-ce **la même cuisine** — fenêtre au-dessus de la gazinière, à droite ? | la géométrie tient |
| 3 | Lumière, grain et peau **identiques** à 1A ? | `@video1` fait son travail |
| 4 | **Le voit-on se lever et traverser**, sans coupe ni saut ? | les 4 étapes sont lues |
| 5 | Un baiser, un grille-pain, une musique, une coupe ? | l'AVOID est lu |
| 6 | **La bouche forme-t-elle les deux répliques** ? | les lignes SOUND pilotent le jeu |

**Pourquoi References et pas Sequel** — Sequel prolonge *le même plan* et donnerait forcément un
raccord parfait : il prouverait quelque chose qu'on sait déjà, sur un cas qui ne représente qu'une
poignée des 62 liens. References est le mode qu'il faudra pour la cinquantaine de raccords où le
cadre change. C'est celui-là qu'il faut mettre à l'épreuve. **Si la question 1 casse**, alors on
bascule sur Sequel pour les liens qui s'y prêtent — et on le saura.

Selon ce qui casse : **1** → il faut passer le raccord par **Sequel** (`video_extension`). **2** → réinjecter le
bloc GEO. **3** → `@video1` n'est pas lu comme on croit. **4** → descendre à 3 étapes. **5** →
remonter l'AVOID plus haut dans le prompt. **6** → écrire les répliques dans l'ACTION, pas dans SOUND.
