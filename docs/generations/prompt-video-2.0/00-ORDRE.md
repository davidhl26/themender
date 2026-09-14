# PROMPT VIDÉO 2.0 — les 32 générations, dans l'ordre

> **Un décor = une prise, jusqu'à 30 s.** Là où l'ancien découpage coupait, c'est la caméra qui
> marche. Une coupe ne survit que si elle est le sens de la scène, et elle est alors **déclarée**
> (grammaire FRAMINGS). 30 s est un plafond, pas un remplissage : un plan seul dans son décor
> garde sa durée. 64 prompts → 32 générations (2 déjà faites).
>
> **Structure identique pour tous** (validée sur les vidéos 1 et 2) : MATERIALS → ROLES → DIALOGUE
> verrouillé → STYLE → AUDIO DESIGN → CHARACTERS → LE LIEU → SCREEN DIRECTION → LIGHT → STAGE 1…n
> avec TRANSITION → ENDING FRAME → AVOID. Chaque fichier passe `scripts/check-prompt-25.py`.
>
> **Réglages communs** : Seedance 2.5 · References · 21:9 · 1080p · bitrate high · son ON.
> Après collage, remonter aux deux premières lignes et **re-sélectionner chaque `@`** dans le
> sélecteur (un `@` collé en texte brut ne se lie à rien). Ne jamais écrire `@Video 1` avec un espace.

## Ce que le compte n'a pas encore — à créer AVANT de lancer les générations marquées 🔴

| Élément | bloque |
|---|---|
| `@maeveill` | G07, G08 (→ G31) |
| `@samsdf` | G21, G28, G32 |
| `@annayoung` `@warddoctor` `@kolya` `@youngmother` `@russianhospitalward` | G22, G23, G24 |

## Les 32 générations

Colonne « chaîne » : ce qu'on attache en `@video1`. **Valider chaque clip avant de générer le suivant.**

### 🟥 La fin du film — S4 + S5 + S6 + S7 · à générer en premier

| # | plans | fichier | durée | coupes | chaîne | statut |
|---|---|---|---|---|---|---|
| G25 | 10A | `G25-10A-la-maison-rouge.md` | 10 s | 0 | tête | ✅ écrit |
| G26 | 10B+10C | `G26-10B-10C-des-ecritures-partout-puis-clic.md` | 24 s | 0 | G25 | ✅ écrit |
| G27 | 10D+10E+10F-1 | `G27-10D-10E-10F1-le-noir-s-allume-son-visage.md` | 25 s | 1 déclarée | G26 | ✅ écrit |
| G28 | 10F-2→10H | `G28-10F2-10F3-10F4-10H-le-grand-recul-jusqu-aux-yeux.md` | 27 s | 0 | G27 **en mouvement** (`@image1` = sa dernière image) | ✅ écrit 🔴 |
| G29 | 10I | `G29-10I-sa-propre-maison.md` | 16 s | 3 déclarées | G28 (pellicule seule) | ✅ écrit |
| G30 | 10J | `G30-10J-dehors.md` | 24 s | 4 déclarées | G29 (pellicule seule) | ✅ écrit |
| G31 | 10K | `G31-10K-l-hopital-enfin-sonore.md` | — | — | **= les 8 premières secondes de G08**, piste chambre ouverte | ✅ (pas de génération) 🔴 |
| G32 | 10L | `G32-10L-il-leve-les-yeux-et-il-sourit.md` | 10 s | 0 | **G28**, pas G31 | ✅ écrit 🔴 |

Décisions prises pour la prise unique : caisson lumineux de l'abribus **éteint** dans tout G28 ; la
coupe de G27 (dos → visage) est la seule de la fin, c'est l'écart déclaré du script.

### 🌤 L'ouverture — S1

| # | plans | fichier | durée | coupes | chaîne | statut |
|---|---|---|---|---|---|---|
| G01 | 1A+1B | `G01-1A-1B-les-toasts.md` | 30 s | 0 | tête (ta vidéo des toasts) | ✅ généré |
| G02 | 1C+1D | `G02-1C-1D-les-enfants.md` | 24 s | 1 déclarée | G01 | ✅ généré |
| G03 | 2A+2B | `G03-2A-2B-le-quai.md` — la caméra tourne autour de Maeve, du contre-jour au soleil dans le dos | 30 s | 0 | G02 (pellicule seule) | ✅ écrit |
| G04 | 2C+2D | `G04-2C-2D-le-restaurant.md` — les quatre assiettes ‖ le dragon au thé | 24 s | 1 déclarée (l'ellipse) | G03 | ✅ écrit |
| G05 | 3A | `G05-3A-la-tasse.md` — le seul ralenti, la caméra se relève avec le temps | 12 s | 0 | **G02** (la même cuisine, pas sa lumière) | ✅ écrit |
| G06 | 3B | `G06-3B-la-conversation-muette.md` — cadre verrouillé au pixel, rejoué en G22 | 10 s | 0 | G05 **pellicule seule, jamais sa lumière** | ✅ écrit |
| G07 | 3C+3D | `G07-3C-3D-tu-m-ecrases-la-bague.md` — Milo puis Nora au chevet, la caméra descend aux mains | 24 s | 0 | G06 | ✅ écrit 🔴 |
| G08 | 3E+3F | `G08-3E-3F-la-vitre-puis-nora.md` — LA PLAQUE 8 s (= G31, répliques générées) ‖ Nora ‖ l'écharpe sort | 24 s | 1 déclarée (jours plus tard) | G07 | ✅ écrit 🔴 |

### ⬛ La traversée grise — S2

| # | plans | fichier | durée | coupes | chaîne | statut |
|---|---|---|---|---|---|---|
| G09 | 4A | le cadre du père (sa dernière image = `@image1` de G29) | 10 s | 0 | tête | ⏳ |
| G10 | 4B+4C | l'accueil, l'entrée dans le dessin, Kolya et la raison | 30 s | 0 | G09 | ⏳ |
| G11 | 4D | He hears you, trente ans en une image | 15 s | 0 | G10 | ⏳ |
| G12 | 5A+5B | les quatre tasses puis trois, jusqu'à « More tea? » | 30 s | 0 | G11 | ⏳ |
| G13 | 5C+5D | le père qui coupe — la caméra descend sur ses mains | 18 s | 0 | G12 | ⏳ |
| G14 | 6A | le forum | 12 s | 0 | G13 | ⏳ |
| G15 | 6B | le cri | 12 s | 0 | G14 | ⏳ |
| G16 | 6C | l'escalier | 8 s | 0 | G15 | ⏳ |
| G17 | 7A+7B | les cinq attentes déçues | 24 s | **4 déclarées** | G16 | ⏳ |
| G18 | 8A | la bibliothèque | 10 s | 0 | G17 | ⏳ |
| G19 | 8B+8C+8D | couloir → miroir → bague, une prise à travers la maison (repli 20 + 8) | 28 s | 0 | G18 | ⏳ |
| G20 | 8E | le bus de nuit | 12 s | 0 | G19 | ⏳ |
| G21 | 9A+9B+9C | l'abribus : elle traverse, « Got anything to eat? », « quand tu verras du rouge » | 30 s | 0 | G20 | ⏳ 🔴 |

### 🕯 Le souvenir lavé — S3 (parallèle à S2, jamais relié)

| # | plans | fichier | durée | coupes | chaîne | statut |
|---|---|---|---|---|---|---|
| G22 | 4E+4F+4G | l'hôpital côté Anna, le brancard, le rejeu | 26 s | 1 déclarée | tête | ⏳ 🔴 |
| G23 | 4H | les trois coups, le feu | 8 s | 0 | G22 | ⏳ 🔴 |
| G24 | 4I | la cour, le prénom | 10 s | 0 | G23 | ⏳ 🔴 |

## Les ruptures — rappel

| entre | quoi |
|---|---|
| G05 → G06 | pellicule seule, **jamais la lumière** — la clarté se retire ici |
| G08 → G09 | ✂ aucune chaîne — clair → gris, deux ans |
| S2 ↔ S3 | ✂ deux chaînes parallèles |
| G21 → G25 | ✂ LA rupture du film — le premier rouge plein cadre |
| G26 → G27 | le noir de G26 se soude au noir d'ouverture de G27 |
| G30 → G31 → G32 | ✂ des deux côtés de l'hôpital ; G32 se chaîne sur G28 |
