# LES CARTES À COLLER — continuité et réalisme

> **À quoi ça sert.** Tes 56 blocs sont déjà écrits, vérifiés, et je n'y touche pas. Ce document
> ajoute **des cartes courtes que tu colles dans chaque génération**, en plus du bloc. Elles font
> deux choses que le bloc ne peut pas faire tout seul :
> **① tenir le même œil et la même pellicule d'un plan à l'autre** (continuité)
> **② dire au modèle QUI joue, pas seulement ce qu'il fait** (réalisme).
>
> ⚠ **Les cartes sont en anglais. C'est volontaire — c'est la langue du moteur.**
> Tu les colles telles quelles, sans traduire, sans reformuler.

---

## MODE D'EMPLOI — où coller, dans quel ordre

Tu construis ta génération comme ça, de haut en bas :

| Ordre | Quoi | Quand |
|---|---|---|
| 1 | **CARTE VIDÉO PRÉCÉDENTE** | ⚠ blocs chaînés **seulement** (liste plus bas) |
| 2 | `Style prompt:` … | ligne existante du bloc |
| 3 | **CARTE CAMÉRA** | **TOUJOURS.** Tous les blocs, sans exception. |
| 4 | **CARTE MONDE** | **TOUJOURS.** Celle de l'acte où tu es. |
| 5 | `SCENE` … jusqu'à `POSTURE LOCK` | bloc existant, inchangé |
| 6 | **CARTES TEMPÉRAMENT** | une par personnage nommé présent au cadre |
| 7 | `FRAME MAP` … jusqu'à `AUDIO` | bloc existant, inchangé |
| 8 | **CARTE ANTI-DÉRIVE** | **TOUJOURS.** |
| 9 | `NEGATIVE PROMPT` … | dernière ligne du bloc, inchangée |

**Rien d'autre ne change.** Tu ne retires jamais une ligne du bloc.

---

# 1. LA CARTE CAMÉRA — dans les 56 blocs

**C'est la carte la plus importante du document.** Elle est identique du premier plan au dernier :
c'est elle qui fait que le film a l'air tourné par une seule équipe, avec une seule caméra.

```
CAMERA & STOCK — IDENTICAL IN EVERY SHOT OF THIS FILM
Shot on one anamorphic lens set on 35 mm film, one stock, one lab, from the first frame to the last. Slight barrel distortion at the frame edges and oval out-of-focus highlights. Focus is pulled by a human hand: it arrives a few frames late, occasionally overshoots by a hair and settles back. Highlights roll off softly and carry a faint halation ring around any practical source; blacks are dense but never crushed and hold a fine grain that breathes with the exposure. Colour is muted and true to life, never graded toward teal and orange. The camera is operated, not simulated: every held frame keeps a residual human weight in it, a drift of a few millimetres — never a locked robotic stillness, never a shake. No digital sharpening, no edge halos, no noise-reduction smear, no beauty retouching, no plastic skin, no CGI gloss.
```

---

# 2. LES CARTES MONDE — une par acte

## 🌤 MONDE CLAIR — séquences 1, 2, 3

```
WORLD — BEFORE
Morning gold through domestic glass. High key, open shadows, warm bounce off walls and skin. Nothing is underexposed, nothing is grey, nothing is cold. There is blood under the skin. This is the light the rest of the film will lose, so it must be genuinely warm here and not merely bright.
```

## ⬛ MONDE GRIS — séquences 4 à 9

```
WORLD — AFTER
A grey-blue world, gently underexposed, roughly two thirds of a stop below normal. Sparse motivated sources only — one bulb, one window, one sodium lamp — and deep quiet blacks between them. Colour is drained but not absent: what survives is amber from a flame, sodium orange from a street, sea-green from tile. Never a saturated hue. No red anywhere, flames included.
```

## 🕯 SOUVENIR LAVÉ — le flashback russe, à l'intérieur de la séquence 4

```
WORLD — THE WASHED MEMORY
The colour is bleached out of the light itself, never in the grade. Heavy silver grain, highlights blown and bleeding, contrast flat and tired. One single hue survives: the sea-green tiling of a hospital. No red anywhere, flames included. Not one legible letter, digit, sign or Cyrillic character anywhere in frame — the country is carried by architecture, materials and light alone.
```

## 🟥 LA MAISON ROUGE — séquence 10

```
WORLD — THE RED HOUSE
The only place in the film where red is allowed, and here it is the whole place. Outside: a red door in a grey street. Inside, once the bulb is out, there is no light source at all — the room is lit by nothing but its own writing, every stroke glowing faintly from within, low and even, the colour of embers under ash, far too dim and too soft for any stroke to be read. Never bright red, never neon, never a magic glow. The strokes are a dense abstract texture forming no characters, in no language, nowhere legible.
```

---

# 3. LES CARTES TEMPÉRAMENT — une par personnage au cadre

> **Pourquoi ça manquait.** Tes blocs décrivent les *gestes* seconde par seconde — c'est excellent,
> et ça reste la vérité. Mais un modèle joue mieux quand il sait **quel genre de personne** fait le
> geste. Ces cartes ne changent aucune action : elles disent la disposition.
>
> ⚠ **Ne colle que les personnages présents à l'image.** Coller Anna dans un plan où elle n'est pas
> la fait entrer dans le cadre.

## @SamBefore — l'acte I

```
TEMPERAMENT, SAM BEFORE A man who talks. He performs small things for his family — burns the toast and turns it into a story, narrates his own failures while they are happening. Loose in the shoulders, quick to laugh at himself, hands always doing something. He touches people as he passes them. Nothing about him is guarded. This is the man his two years of silence will be measured against, so the ease has to be real here.
```

## @Sam — le présent

```
TEMPERAMENT, SAM AFTER Two years without speaking. Not sullen — emptied. He moves through his own house like a guest: slower, heavier, shoulders carried forward, eyes down and to the side. He still does things for his daughter, but wordlessly and out of her sight. Every gesture is finished; none is ever explained. When he is alone his face does what it wants; the moment she is in the room it does nothing at all.
```

## @SamSDF — le déguisement

```
TEMPERAMENT, THE VAGRANT A man playing someone else, and playing him well. Slower, stiller, older in the joints; the cold has genuinely got into him. He does not perform kindness — he asks for something small, receives it, gives back more than he took, and states it flatly, the way a man states a fact. He never lingers and never watches anyone walk away while they can still see him. His voice sits a third lower than his own and is broken by the cold.
```

## @Nora — 15 ans

```
TEMPERAMENT, NORA A fifteen-year-old running on empty. Grief has made her polite and absent: she answers, she carries the dish back, she says thank you, and none of it reaches her face. Her body is tired before the day starts. She does not cry in front of people — the swollen eyelids come from somewhere else, earlier. When something does move her, she goes very still first, and only then does it show.
```

## @NoraBefore — 13 ans

```
TEMPERAMENT, NORA BEFORE Thirteen and entirely unguarded. She interrupts, she leans on people, she laughs at her father's jokes before he has finished them. Her happiness is loud, physical, and costs her nothing.
```

## @Anna

```
TEMPERAMENT, ANNA A woman who has buried people and keeps the stove lit. Warm without softness, quick and practical in the hands, slow and careful in the eyes. She does not comfort — she pours the tea and waits. Grief lives in her as patience, never as weakness: she will cry in the middle of a sentence and go on speaking in the same steady voice, and she will never once wipe her face. Nothing about her is fragile.
```

## @AnnaYoung — 48 ans, le souvenir

```
TEMPERAMENT, ANNA YOUNG The same woman, thirty years earlier: practical hands, straight back, no drama offered to anybody. Everything that breaks in her breaks inward and without sound — until the one moment it does not. She is never a victim in any frame; she is someone doing the next necessary thing until there is no next thing left.
```

## @Maeve

```
TEMPERAMENT, MAEVE Dry, fast, affectionate and entirely unsentimental — even dying. She does not soften her voice for anyone. What she wants she asks for plainly, and once. Her tenderness arrives as instruction, never as comfort.
```

## @MaeveIll

```
TEMPERAMENT, MAEVE ILL The illness has taken her body and left the voice and the impatience intact. She spends what she has left on being understood, not on being reassuring. She is not frightened, and she is not brave about it either — she is simply out of time and aware of it.
```

## @Milo — 8 ans, le présent

```
TEMPERAMENT, MILO Eight years old and the only one in the house who still says things out loud. He has not learned to be careful around grief yet, so he asks, and he keeps asking. Watchful pale grey-blue eyes that go to his sister's face before they go to anything else. He fidgets, he leans, he is always slightly too close to whoever he is talking to.
```

## @MiloBefore — 6 ans, l'acte I

```
TEMPERAMENT, MILO BEFORE Six, and made of momentum. He arrives at speed, collides with legs, is picked up, and is off again. He does not listen to whole sentences. Everything about him is noise and warmth.
```

## @Asha — 52 ans

```
TEMPERAMENT, ASHA Upright, deliberate, economical. She listens longer than most people are comfortable with before she says anything, and when she does speak it is short and settled — a woman used to being believed without raising her voice. Her hands are still when she talks. Warmth in her comes out as attention, not as smiling.
```

## @Fatiha — 66 ans

```
TEMPERAMENT, FATIHA Sixty-six, and everything she says goes through her hands first. Quick, warm, interrupting, laughing at the edge of serious things. She touches the arm of whoever she is talking to. She tells you a thing that broke her the way you would mention the weather, and moves on before you can be sorry about it.
```

## @Mei

```
TEMPERAMENT, MEI Brisk, busy, entirely unmystified. She runs a restaurant and she is still running it while this is happening. What she passes on, she passes on the way she would pass on a phone number: practical, low, half over her shoulder, already moving to the next thing.
```

---

# 4. LA CARTE VIDÉO PRÉCÉDENTE — blocs chaînés seulement

⚠ **NE LA COLLE QUE SUR CES CINQ BLOCS.** *(quatre chaînés par l'image + 10F-4, cas particulier.)* Ce sont les seuls où un même mouvement est découpé en
segments. Partout ailleurs il y a un **cut** — et donner le plan précédent en référence sur un cut
fait hériter son cadre : le cut ne se lit plus comme un cut, et ton montage tombe.

| Bloc | Ce qu'il continue | Image de départ |
|---|---|---|
| **10D-2** | la montée des braises, segment 2/2 | ✅ dernière image de 10D-1 |
| **10F-1** | le grand travelling arrière, segment 1/4 | ✅ dernière image de 10E |
| **10F-2** | segment 2/4 | ✅ dernière image de 10F-1 |
| **10F-3** | segment 3/4 | ✅ dernière image de 10F-2 |
| **10F-4** | segment 4/4 — l'arrivée sur l'abribus | ❌ **AUCUNE** — voir ci-dessous |

### ⚠ Le cas 10F-4 — c'est là que la carte sert le plus

**10F-4 est le segment 4/4 d'un mouvement continu, et pourtant il n'a aucune image de départ.**
C'est un écart assumé dans le document : la caméra redescend sur l'abribus, un décor que la dernière
image de 10F-3 ne contient pas.

Résultat : **le plan le plus important du film — celui où on voit enfin les yeux du père — repart
de zéro au milieu d'un mouvement.** C'est ton plus gros risque de raccord.

👉 **Sur 10F-4, colle la carte MAIS ne mets PAS d'image de départ.** Passe 10F-3 en référence vidéo
seulement. La carte transmettra la vitesse, le grain et le niveau de lumière — pas le cadre.
C'est exactement ce pour quoi elle est faite.

Tu passes le clip précédent en **référence vidéo**, et tu colles ceci **tout en haut**, avant
`Style prompt:` :

```
@Video 1: the shot that immediately precedes this one. Use it ONLY to read where the scene stands — light level, grain, skin rendering, camera speed and direction, and the exact state the movement is in. Do NOT reuse, copy or extend any of its frames: every frame here is generated new from the start frame and the references below, at full quality. The framing of this shot is defined solely by the FRAME MAP below, and the movement continues at exactly the same speed, without easing in or out.
```

---

# 5. LA CARTE ANTI-DÉRIVE — dans les 56 blocs

C'est celle qui empêche les personnages de « s'améliorer » d'un plan à l'autre — le défaut le plus
courant et le plus destructeur en génération de film.

```
CONTINUITY — WHAT MUST NOT DRIFT
Wardrobe, hair, dirt, damage and wear are exactly as the references define them and do not improve, clean themselves up or change between shots. Nobody is better groomed, better lit, better dressed or better rested than in the shot before. Props stay where the prop layout puts them. Weather, time of day and light level do not move inside a sequence. Nobody looks at the lens at any point.
```

---

# 6. TABLEAU DE COLLAGE — séquence par séquence

*(Vérifié en lisant les 10 documents — pas de mémoire.)*

| Séq. | Carte MONDE | Cartes TEMPÉRAMENT à coller |
|---|---|---|
| 1 | CLAIR | @SamBefore · @Maeve · @NoraBefore · @MiloBefore |
| 2 | CLAIR | @SamBefore · @Maeve · @NoraBefore · @MiloBefore · @Mei |
| 3 | CLAIR qui se retire | @SamBefore · @MaeveIll · @NoraBefore · @MiloBefore |
| 4 | GRIS · **+ SOUVENIR LAVÉ dans le flashback** | @Nora · @Anna — puis, dans le souvenir : @AnnaYoung *(aucune carte pour Kolya, le médecin et la jeune mère : ils ne parlent pas et ne jouent qu'un geste)* |
| 5 | GRIS | @Nora · @Milo · @Mei · @Asha · @Fatiha |
| 6 | GRIS | @Nora · @Sam |
| 7 | GRIS | @Nora |
| 8 | GRIS | @Nora *(@Mender = le manteau, jamais un visage — pas de carte)* |
| 9 | GRIS | @Nora · **@SamSDF** |
| 10 | **LA MAISON ROUGE** | @Nora *(jusqu'à 10F-1)* · **@SamSDF** *(à partir de 10F-4)* · @MaeveIll *(le flashback)* · dans le montage muet : @Anna · @Mei · @Asha · @Fatiha |

⚠ **Séquence 4** : le flashback russe change de carte MONDE **à l'intérieur du même document**.
Les blocs du présent prennent GRIS, les micro-plans du souvenir prennent SOUVENIR LAVÉ. Ne mélange
jamais les deux dans une même génération.

---

# 7. TROIS CHOSES QUE J'AJOUTE, EN PLUS

## ⚠ A — Un changement de genre entre la séq. 9 et la séq. 10

Tes réglages disent **Genre Noir** pour les séquences 4 à 9, et **Genre Drama** pour la 10.
Ces deux séquences se suivent directement au montage. Un changement de genre change l'étalonnage
du modèle : **tu risques un saut de ton visible au raccord**, juste avant la fin du film.

**Deux options — c'est ta décision, pas la mienne :**
- **Garder Noir jusqu'au bout** (la maison rouge éclate d'autant plus dans un monde qui n'a pas bougé)
- **Assumer le changement** (le film respire enfin, c'est le sujet de la scène)

Je penche pour **garder Noir**, et laisser le rouge faire le travail tout seul. Mais teste les deux
sur le plan 10A : c'est 2 générations.

## ✅ B — Génère TROIS plans d'abord, pas cinquante-six

Ne lance pas la séquence entière. Prends **10A** (la maison rouge, extérieur), **9B** (le SDF coupé
à la bouche), **1C** (la table à quatre, monde clair). Trois mondes, trois difficultés.

Regarde-les côte à côte. Si les trois tiennent ensemble, ton système est bon et tu peux dérouler.
Si l'un décroche, tu l'as appris pour le prix de 3 clips, pas de 56.

## ✅ C — Le multi-cam se fait en deux générations, pas en une

Seedance 2.0 **n'a aucun paramètre multi-plans**. Tes 30 blocs qui portent un `SHOT 2` demandent
poliment au modèle de couper — il le fera ou non.

**Pour les plans où la coupe compte vraiment** : génère le large, génère le serré depuis la même
image de départ, et coupe au montage. C'est fiable à 100 %, et c'est toi qui choisis l'image de
coupe. Avec un pack illimité, ça ne coûte rien de plus.

---

## Rappel des trois choses qui ne se négocient jamais

1. **RÈGLE ZÉRO** — Nora n'apprend jamais que le Mender est son père. Aucun regard qui doute.
2. **Aucune écriture lisible** nulle part — l'écriture est une texture, dans aucune langue.
3. **Le rouge n'appartient qu'à la maison rouge** — et à l'écharpe de Maeve dans l'acte I.
