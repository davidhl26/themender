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

## Éléments — tous sur le compte depuis le 14/09

Les trois derniers ont été générés/créés le 14/09 (GPT Image 2 · 4K · high · 16:9, la fiche de base en référence) :
`@samsdf-1` (**c'est ce nom-là qu'il faut sélectionner** : version capuche, visage caché — job `7696c5ab-6874-4168-8d58-c9cd3b7e86c4`, réf. `@samafter` ; l'ancienne fiche à visage découvert reste sur le compte sous le nom `samsdf` (job `6e4fb30e-eb6e-408f-937c-4d9e312dd29f`) : à supprimer dans l'interface pour ne pas la sélectionner par erreur ; G28 et G32 chargent `@samafter` en plus pour le visage du démasquage) · `@maeveill` (job `56415cca-5183-4064-9ad7-3d94d93c7d13`, réf. `@maeva`) ·
`@russianhospitalward` (créé depuis LIEU-17 IMAGE 4, job `45171598-cf11-4165-8bfb-6c151b5ad13e`). **À valider à l'œil avant de lancer G07/G08 et G21** :
rien au-dessus de la lèvre dans la capuche, la barbe de `@samafter`, l'encre aux bouts des doigts ; le visage de `@maeva` amaigri, l'écharpe seul rouge.
⚠ Doublons sur le compte : `warddoctor` ×2, `youngmother` ×2 (même image — n'importe lequel).

## Les 32 générations

Colonne « chaîne » : ce qu'on attache en `@video1`. **Valider chaque clip avant de générer le suivant.**

### 🟥 La fin du film — S4 + S5 + S6 + S7 · à générer en premier

| # | plans | fichier | durée | coupes | chaîne | statut |
|---|---|---|---|---|---|---|
| G25 | 10A | `G25-10A-la-maison-rouge.md` | 10 s | 0 | tête | ✅ écrit |
| G26 | 10B+10C | `G26-10B-10C-des-ecritures-partout-puis-clic.md` | 24 s | 0 | G25 | ✅ écrit |
| G27 | 10D+10E+10F-1 | `G27-10D-10E-10F1-le-noir-s-allume-son-visage.md` | 25 s | 1 déclarée | G26 | ✅ écrit |
| G28 | 10F-2→10H | `G28-10F2-10F3-10F4-10H-le-grand-recul-jusqu-aux-yeux.md` | 27 s | 0 | G27 **en mouvement** (`@image1` = sa dernière image) | ✅ écrit |
| G29 | 10I | `G29-10I-sa-propre-maison.md` | 16 s | 3 déclarées | G28 (pellicule seule) | ✅ écrit |
| G30 | 10J | `G30-10J-dehors.md` | 24 s | 4 déclarées | G29 (pellicule seule) | ✅ écrit |
| G31 | 10K | `G31-10K-l-hopital-enfin-sonore.md` | — | — | **= les 8 premières secondes de G08**, piste chambre ouverte | ✅ (pas de génération) |
| G32 | 10L | `G32-10L-il-leve-les-yeux-et-il-sourit.md` | 10 s | 0 | **G28**, pas G31 | ✅ écrit |

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
| G07 | 3C+3D | `G07-3C-3D-tu-m-ecrases-la-bague.md` — Milo puis Nora au chevet, la caméra descend aux mains | 24 s | 0 | G06 | ✅ écrit |
| G08 | 3E+3F | `G08-3E-3F-la-vitre-puis-nora.md` — LA PLAQUE 8 s (= G31, répliques générées) ‖ Nora ‖ l'écharpe sort | 24 s | 1 déclarée (jours plus tard) | G07 | ✅ écrit |

### ⬛ La traversée grise — S2

| # | plans | fichier | durée | coupes | chaîne | statut |
|---|---|---|---|---|---|---|
| G09 | 4A | `G09-4A-le-cadre-du-pere.md` — le cadre du père, « Why? » (sa dernière image = `@image1` de G29) | 10 s | 0 | tête | ✅ écrit |
| G10 | 4B+4C | `G10-4B-4C-anna-le-dessin-kolya.md` — l'accueil ‖ la caméra plonge dans le dessin (souvenir G22–G24 inséré en post à 0:16,5) et en ressort, Kolya et la raison | 30 s | 1 déclarée (le large → la table) | G09 | ✅ écrit |
| G11 | 4D | `G11-4D-he-hears-you.md` — He hears you, la caméra suit Nora au montant, trente ans en une image | 16 s | 0 | G10 | ✅ écrit |
| G12 | 5A+5B | `G12-5A-5B-les-quatre-tasses-puis-trois-la-table-des-femmes.md` — les quatre tasses puis trois, la caméra suit Mei à la table des femmes, jusqu'à « More tea? » | 30 s | 0 | G11 | ✅ écrit |
| G13 | 5C+5D | `G13-5C-5D-les-mains-du-pere-le-trajet-du-regard.md` — les mains du père, la caméra se relève au large ‖ Nora serrée, le regard sur la chaise vide | 18 s | 1 déclarée (le contrechamp) | G12 | ✅ écrit |
| G14 | 6A | `G14-6A-le-forum.md` — la caméra contourne la chaise jusqu'à LA PLAQUE (POST : la page) ‖ serré de face | 13 s | 1 déclarée | G09 (même chambre) | ✅ écrit |
| G15 | 6B | `G15-6B-le-cri.md` — la caméra marche jusqu'au rail, « Why did my mother die? », rien ne répond | 13 s | 0 | G14 | ✅ écrit |
| G16 | 6C | `G16-6C-l-escalier.md` — plan fixe, « You okay? » / « Nothing. I stepped on something. » (⚠ archiver le son : référence de voix pour G21) | 8 s | 0 | G14 | ✅ écrit |
| G17 | 7A+7B | `G17-7A-7B-les-cinq-attentes-decues.md` — cinq jours, cinq cadres fixes ; la boîte aux lettres vit dans la même prise | 24 s | **4 déclarées** (sauts de jour) | G15 | ✅ écrit |
| G18 | 8A | `G18-8A-la-bibliotheque.md` — la caméra se lève sur l'axe du couloir, le dos écrit déjà en marche ‖ l'allée vide | 12 s | 1 déclarée | G17 | ✅ écrit |
| G19 | 8B+8C+8D | `G19-8B-8C-8D-le-couloir-le-miroir-la-bague.md` — couloir (suivi jusqu'au coin) ‖ miroir (PLAQUE puis recul) ‖ bague (macro → poitrine) — repli 20 + 8 | 28 s | 2 déclarées (sauts de temps) | G18 | ✅ écrit |
| G20 | 8E | `G20-8E-le-bus-de-nuit.md` — trois fois le même cadre (jump cuts voulus), la caméra recule aux portes | 12 s | 2 déclarées (même axe) | G19 | ✅ écrit |
| G21 | 9A+9B+9C | `G21-9A-9B-9C-l-abribus.md` — elle traverse (suivi) ‖ les valeurs serrées voyagent sous la lèvre, 3 répliques ‖ le large du haut de la rue | 30 s | 2 déclarées | G20 | ✅ écrit |

### 🕯 Le souvenir lavé — S3 (parallèle à S2, jamais relié)

| # | plans | fichier | durée | coupes | chaîne | statut |
|---|---|---|---|---|---|---|
| G22 | 4E+4F+4G | `G22-4E-4F-4G-l-hopital-russe.md` — la chambre ‖ le cadre de G06 au pixel, la caméra avance, la glissade, le cri ‖ le brancard de profil ‖ la caméra couchée sur le matelas : le rejeu, la dérive, le plafond, le rail | 27 s | **3 déclarées** (ellipse, autre femme, rejeu) | tête (`@video1` = G06, composition seule) | ✅ écrit |
| G23 | 4H | `G23-4H-les-trois-coups-et-le-feu.md` — trois coups, le dos coupé aux épaules, la caméra suit au poêle, la flamme (⚠ archiver le son des coups : dernier plan du film) | 10 s | 0 | G22 | ✅ écrit |
| G24 | 4I | `G24-4I-la-cour-et-le-prenom.md` — le dos montre le porche, la caméra suit Anna au porche, la contourne jusqu'au visage, la main sur la bouche | 14 s | 0 | G23 | ✅ écrit |

## Les ruptures — rappel

| entre | quoi |
|---|---|
| G05 → G06 | pellicule seule, **jamais la lumière** — la clarté se retire ici |
| G08 → G09 | ✂ aucune chaîne — clair → gris, deux ans |
| S2 ↔ S3 | ✂ deux chaînes parallèles |
| G21 → G25 | ✂ LA rupture du film — le premier rouge plein cadre |
| G26 → G27 | le noir de G26 se soude au noir d'ouverture de G27 |
| G30 → G31 → G32 | ✂ des deux côtés de l'hôpital ; G32 se chaîne sur G28 |
