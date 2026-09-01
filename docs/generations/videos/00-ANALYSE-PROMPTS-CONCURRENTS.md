# ANALYSE DES PROMPTS CONCURRENTS — et le gabarit qu'on en tire

> Six prompts fournis par David, de deux auteurs différents. Ce document dit **ce qu'ils font**,
> **ce qu'ils ont en commun**, **ce qui nous manquait**, et donne **le gabarit appliqué aux 62 blocs**.

---

## 1. Les deux familles

### 🅰 Famille PROSE — 3 prompts *(la bataille dans la neige)*

Écriture en paragraphes, pas de titres de section sauf trois à la fin.

```
CONTINUITY REFERENCE          ← prose : « ça continue du plan d'avant, @executioner vient de… »
[phrase de caméra]            ← « Handheld camera, alive and moving, jostling and urgent… »
[l'action, en prose]          ← ce qui se passe, dans l'ordre
[le tempo, en prose]          ← « Everything in fast real-time motion… No slow motion. »
Cinematography:               ← un paragraphe
Film emulation:               ← ★ UNE PELLICULE NOMMÉE
Photographic realism.         ← une liste de matières
Avoid:                        ← la liste des interdits
```

### 🅱 Famille STRUCTURÉE — 3 prompts *(le couloir)*

Titres en capitales, mesures en centimètres, secondes chronométrées.

```
SCENE CONTEXT                        FIRST FRAME AND SPATIAL BLOCKING
ACTIVE REFERENCES                    FORMAT MODE
LOCATION MAP                         OPTICS
CAMERA                               CHARACTER PERFORMANCE
PHYSICS                              LIGHTING
AUDIO                                POSITIVE CONSTRAINTS
```

---

## 2. Les onze points communs aux SIX prompts

| # | Ce qu'ils font tous | Pourquoi ça marche |
|---|---|---|
| **1** | **Le contexte AVANT l'action** | Le modèle sait d'où il part avant de savoir quoi faire. |
| **2** | **Une pellicule NOMMÉE** — *Fujifilm Superia 400 color negative* | ★ Le point le plus fort. « Film look » ne veut rien dire ; un négatif nommé porte une science des couleurs entière. |
| **3** | **La caméra est un opérateur, pas un point de vue** | « handheld, alive and moving, jostling » / « operator walking backward, not stabilized ». Une caméra tenue par un corps. |
| **4** | **Sous-exposer est demandé explicitement** | « Deliberately underexposed, protecting the shadows, rich retained shadow detail. » Ils demandent le manque de lumière. |
| **5** | **Les hautes lumières sont bridées** | « Restrained highlights, never blown out, holding texture. » |
| **6** | **Chaque référence est décrite ET verrouillée** | `@char_dad: Elderly Japanese male… **100% matches the reference.**` La phrase de verrouillage revient à chaque fois. |
| **7** | **Les distances sont en unités réelles** | « approximately 80cm–1 meter from his face », « 10–15cm above tile ». Jamais « close-up ». |
| **8** | **La première image est décrite en mots** | `FIRST FRAME AND SPATIAL BLOCKING` — ils ne comptent pas sur l'image de départ pour dire le cadre. |
| **9** | **Le jeu est un comportement, jamais un adjectif** | ★ « He does **not** perform fear. He is past it. » puis : **deux ruptures involontaires, et seulement deux** — une déglutition à 0:02, une mâchoire qui lâche à 0:04. |
| **10** | **La physique est une section** | « His torso sways passively with their stride rhythm — an oscillation he does not generate. » |
| **11** | **Le son est nommé, et la musique interdite** | « SFX only. No music. No background music of any kind. » |

---

## 3. Ce qu'ils font mieux que nous — et ce qu'on avait déjà

| | Eux | Nous, avant |
|---|---|---|
| Pellicule nommée | ✅ | ❌ « 35 mm film » — creux |
| Physique du mouvement | ✅ section entière | ❌ retiré au nettoyage |
| Jeu = comportement | ✅ « il ne joue pas la peur, il est passé de l'autre côté » | 🟡 des gestes, jamais la disposition |
| Carte du lieu en cm | ✅ | 🟡 dans la ligne CAM, mélangé au reste |
| Première image décrite | ✅ | ❌ on comptait sur l'image de départ |
| Contraintes en positif à la fin | ✅ | ❌ on finissait sur les interdits |
| Son : musique interdite | ✅ | 🟡 dans le negative prompt seulement |
| **Chorégraphie seconde par seconde** | 🟡 par blocs de temps | ✅ **on est plus précis qu'eux** |
| **Verrous de récit** *(règle zéro, le rouge, l'illisible)* | ❌ pas leur sujet | ✅ **on a ce qu'ils n'ont pas** |

**Conclusion : on garde notre chorégraphie et nos verrous, on prend leur grammaire.**

---

## 4. LE GABARIT — l'ordre appliqué aux 62 blocs

```
 1  SCENE CONTEXT                     ce qui se passe, en deux phrases, et la durée
 2  CONTINUITY REFERENCE              d'où l'on vient — @Video 1 ou tête de chaîne
 3  ACTIVE REFERENCES                 chaque @Element décrit + « 100% matches the reference »
 4  LOCATION MAP                      qui est où, en centimètres et en pourcentages de cadre
 5  FIRST FRAME AND SPATIAL BLOCKING  la toute première image, décrite en mots
 6  FORMAT MODE                       durée, nombre de cadrages, nombre de coupes
 7  OPTICS                            focale, ouverture, profondeur de champ, point
 8  CAMERA & CHOREOGRAPHY             notre chorégraphie seconde par seconde — inchangée
 9  CHARACTER PERFORMANCE             qui joue, et comment — comportement, jamais adjectif
10  PHYSICS                           poids, inertie, contact
11  CINEMATOGRAPHY                    source unique, sous-exposition, hautes lumières bridées
12  FILM EMULATION                    ★ Kodak Vision3 500T 5219
13  PHOTOGRAPHIC REALISM              la liste des matières
14  AUDIO                             SFX only. No music.
15  POSITIVE CONSTRAINTS              les règles reformulées en positif, en dernier
16  AVOID                             les interdits
```

**Pourquoi cet ordre** : le contexte et les références d'abord *(le modèle sait qui et où)*, la
chorégraphie au milieu *(le cœur)*, le rendu ensuite *(comment ça doit avoir l'air)*, et les
contraintes en dernier — **c'est la position que le modèle pondère le plus fort.**

---

## 5. Le choix de la pellicule — et pourquoi celle-là

Les concurrents prennent **Fujifilm Superia 400** : négatif froid, biais vert-cyan dans les ombres.
Bon pour leur neige grise de plein jour. **Mauvais pour toi** : ton film est de nuit.

**THE MENDER prend Kodak Vision3 500T 5219.**

| | |
|---|---|
| **500 ISO tungstène** | le négatif des intérieurs nuit à l'ampoule — exactement chez Anna, dans le bus, à l'abribus |
| **Il tient les ombres** | ta séquence 10 est noire à 80 % : c'est lui qui empêche la bouillie |
| **Il fait la halation** | l'anneau lumineux autour de la fenêtre chaude, de la lampe sodium, du poêle |
| **Le grain grossit dans le sous-exposé** | ton monde gris respire au lieu d'être plat |
| **Les scènes de jour ?** | **même négatif, filtre 85.** C'est ce que fait un vrai tournage. Un seul œil, du premier plan au dernier. |

⚠ **Ne jamais changer de pellicule en cours de film.** C'est ce qui donne l'impression d'une seule
équipe, d'un seul labo — et c'est ce qu'un chef opérateur voit en dix secondes. *(Rappel : Phedon
Papamichael est au jury.)*

---

## 6. Le point qu'ils font le mieux, et qu'il faut copier mot pour mot

> **« @char_son does not perform fear. He is past it. »**
> **« Exactly two involuntary physical breaks in 6 seconds: one swallow around 0:02, one jaw
> release under one second around 0:04–0:05. Nothing else. »**
> **« No head shaking. No twisting. No wide eyes. No open-mouthed terror. The fear is legible
> precisely because it has nowhere to go. »**

**Ils ne demandent jamais une émotion. Ils comptent les gestes qui la trahissent.**

C'est exactement ce qu'il faut pour **10.6** — le visage de Nora, la larme, le sourire.
Ne jamais écrire « elle est bouleversée ». Écrire : *cinq saccades des yeux, la mâchoire qui
descend de deux centimètres et ne remonte pas, UNE larme de l'œil droit, puis les coins de la
bouche qui montent contre la mâchoire ouverte.* **C'est déjà ce que dit ton bloc.**

---

*Gabarit appliqué par `scripts/build-blocs-prets.py` — les `PRET-SEQ-*.md` sont régénérables.*
