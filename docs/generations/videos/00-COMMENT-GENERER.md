# COMMENT GÉNÉRER — la marche à suivre, écran par écran

> Écrit le 02/09 après le test réel de David : *« j'insère la dernière vidéo dans Seedance 2.0,
> il y a pas de suivi, c'est pas le même mouvement de caméra. »*
> **La cause : il y a TROIS façons d'attacher une vidéo, et la plus faible était utilisée.**

---

## 1. Les trois façons d'attacher — et ce que chacune fait vraiment

Les deux Seedance acceptent les mêmes rôles de média. Ils ne font pas du tout la même chose.

| Rôle | Ce que ça fait | Continuité obtenue |
|---|---|---|
| **`start_image`** | La **première image** de la nouvelle vidéo **EST** cette image | **Au pixel.** C'est le raccord le plus fort |
| **`video_references`** | Le modèle *regarde* la vidéo pour le style, l'identité, le rendu | **Aucune continuité de cadre.** ⚠ **C'est ce que tu faisais** |
| **`video_extension`** *(Seedance 2.5 seulement)* | **Prolonge** réellement la vidéo, en avant ou en arrière | **Le plan continue.** Le raccord est invisible |

**C'est là qu'était le problème.** `video_references` ne continue jamais un plan — il ne fait qu'inspirer
le rendu. Le modèle n'a jamais reçu l'ordre de reprendre le mouvement, parce que ce rôle ne le porte pas.

---

## 2. Mais attention : 1A et 1B ne sont PAS un plan continu

C'est le point qui explique ta déception, et il n'est pas dans le modèle — il est dans le découpage.

**1A** est un plan large depuis l'ouest, en 40 mm. **1B** est un plan moyen face au fourneau, en 50 mm.
**Il y a une coupe entre les deux au montage.** Deux positions de caméra différentes, comme sur
n'importe quel tournage.

Donc entre 1A et 1B, ce qui doit se raccorder n'est **pas** le mouvement de caméra — c'est :
la même pièce, la même lumière, les mêmes vêtements, la même usure, et **la même *manière* de tenir
la caméra**. Pas le même cadre.

**Un vrai raccord invisible n'existe que dans 5 plans du film** — les segments du grand recul de la
séquence 10 (`10D-2`, `10F-1` à `10F-4`). Là, c'est un seul mouvement découpé en morceaux.

---

## 3. Les trois cas, et quoi faire dans chacun

### 🅐 CAS NORMAL — nouveau cadrage après une coupe *(la grande majorité des 62 plans)*

C'est 1A → 1B, 4B → 4C, et presque tout le film.

1. Modèle **Seedance 2.5**, 21:9, 1080p, bitrate **high**, **sound off**
2. **`start_image`** = **l'image de lieu que le titre du bloc nomme** *(pour 1B : `LIEU-01 IMAGE 3`,
   job `e9dc3786`)* — **jamais** la dernière frame du plan précédent : le cadrage n'est pas le même
3. **`video_references`** = le clip précédent — il sert au grain, à la lumière et à la peau
4. **Éléments** = ceux que le titre du bloc liste, et rien d'autre
5. **Prompt** = le bloc entier, collé tel quel
6. Durée = celle du `FORMAT MODE` du bloc

### 🅑 UN SEUL MOUVEMENT DÉCOUPÉ — `10D-2`, `10F-1`, `10F-2`, `10F-3`, `10F-4`

Là, et seulement là, le raccord doit être **invisible**.

1. Modèle **Seedance 2.5**, mode **`video_extension`**, `extension_mode` = **`forward`**
2. La vidéo à prolonger = le segment précédent
3. Prompt = le bloc entier
4. *(À défaut : `start_image` = la dernière frame exacte du segment précédent, exportée en image.)*

### 🅒 TÊTE DE CHAÎNE — `1A`, `4A`, `4E`, `10A`… *(11 plans)*

Aucune vidéo à attacher. `start_image` = l'image de lieu nommée par le titre. C'est tout.

---

## 4. La vérification à faire À CHAQUE collage — 20 secondes

- [ ] **La ligne de chaîne commence bien par `THE VIDEO ATTACHED TO THIS GENERATION`**
      *(si elle commence par un deux-points seul, l'éditeur a mangé quelque chose — recolle)*
- [ ] **Regarde quel Élément l'éditeur a accroché.** Il substitue tout seul : `@Kitchen` devient
      `@[kitchen](840a3190…)`, qui est le **vieux kitchen bâti sur un ANGLE**, pas le master.
      Deux plans qui n'appellent pas le même Élément ne sont pas dans le même décor.
- [ ] **`sound off`** — le son est écrit dans les blocs pour le montage, pas pour la génération
- [ ] Durée = celle du `FORMAT MODE`

---

## 5. Ce qui change entre les deux modèles

| | Seedance 2.0 | Seedance 2.5 |
|---|---|---|
| Durée max | 15 s | **30 s** |
| Résolution max | **4K** | 1080p |
| `video_extension` | ❌ | **✅** |
| Abonnement illimité | ✅ | ✅ |

**Pour ce film : 2.5.** Le `video_extension` est indispensable aux 5 segments de la séquence 10, et
le 4K de la 2.0 ne sert à rien puisqu'on livre en 1080p.
