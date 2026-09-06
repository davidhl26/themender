# CE QUI BLOQUE — relevé sur ton compte Higgsfield le 06/09

> Les 62 prompts sont refaits au gabarit Seedance 2.0 / 1080p (`PROMPT-SEQ-01..10.md`).
> Mais **trois choses empêchent de lancer la totalité**, et deux sont de ton côté.

---

## 🔴 1. Quinze Éléments cités par les prompts n'existent pas sur ton compte

**18 plans sur 62** — presque un tiers du film — nomment un Élément que je ne trouve pas.
Sans lui, le modèle invente le visage à chaque plan : **aucune continuité d'identité**.

| Élément manquant | Plans concernés | Ce que c'est |
|---|---|---|
| `@SamSDF` | **9A · 9B · 9C · 10F-4 · 10H · 10L** | Sam à la rue, bloc 3 — six plans |
| `@AnnaYoung` | **4E · 4G · 4H · 4I** | Anna il y a trente ans |
| `@MaeveIll` | **3C · 3D · 3E · 10K** | Maeve à l'hôpital — dont le CADRE RÉFÉRENT ABSOLU de 10K |
| `@WardDoctor` | 4E · 4F · 4G | Le médecin du couloir russe |
| `@YoungMotherHospital` | 4F · 4G | La mère à l'hôpital |
| `@YoungMother` | 4I | La mère, trente ans plus tôt |
| `@Kolya11` | 4E | L'enfant malade |
| `@Kolya2` | 4I | Kolya tout petit |
| `@AnnaDrawing` | 4B · 4C | Le dessin au crayon |
| `@RussianHospitalWard` | 4E | La chambre de l'enfant |
| `@MotherRing` | 3D · 8D | La bague |
| `@Mailbox` `@CounterBowl` `@FoldedNote` `@GreenBandPlate` | divers | Accessoires |

**Ce que j'en fais en attendant** : dans les prompts, ces noms sont écrits **en clair** (SAM SDF,
ANNA YOUNG…) au lieu d'une mention `@`. Le modèle les construira depuis la description — donc
ça génère, mais l'identité **dérivera d'un plan à l'autre**. Pour six plans de Sam à la rue,
c'est rédhibitoire.

**Ce qu'il faut faire** : créer au minimum les **quatre personnages récurrents** —
`@SamSDF`, `@AnnaYoung`, `@MaeveIll`, `@WardDoctor`. Les autres n'apparaissent qu'une ou deux
fois et peuvent rester décrits au prompt. Les quatre accessoires n'ont pas besoin d'Élément :
une bague et une boîte aux lettres se décrivent très bien en trois lignes.

Dis-moi quand ils sont créés et je remets les mentions `@` partout en une passe.

---

## 🟠 2. Des doublons d'Éléments, et un piège sur la cuisine

Le compte contient beaucoup de doublons — souvent une version CamelCase (celle que j'ai
décrite, avec sa notice) et une version minuscule créée automatiquement ensuite.

**Le piège** : il existe **trois « kitchen »**. Le master de la cuisine familiale, celui qui
porte la notice, s'appelle **`Kitchen-1`**. Les deux `kitchen` en minuscules ne sont **pas le
master** — l'un d'eux est l'image d'ANGLE H. C'est celui-là que tu as attaché sur 1A et 1B.
Ça a marché, mais ce n'était pas le bon.

À garder / à supprimer : `Kitchen-1` *(garder)* contre `kitchen` ×2 et `kitchen-2` ·
`Restaurant` contre `restaurant` ×2 · `Quay` en double · `NightBus`/`nightbus` ·
`BackGallery`/`backgallery` · `LibraryCorridor`/`librarycorridor` · `Bathroom`/`bathroom` ·
`HospitalRoom`/`hospitalroom` · `HospitalCorridor`/`hospitalcorridor` · `NoraBedroom`/`norabedroom` ·
`AnnaKitchen`/`annakitchen` · `BusShelter`/`busshelter` · `RedHouseExterior`/`redhouseexterior` ·
`AnnaKitchenPast`/`annakitchenpast` · `RussianHospitalCorridor`/`russianhospitalcorridor` ·
`RussianNightStreet`/`russiannightstreet` · `RussianCourtyard`/`russiancourtyard` ·
`redhouseinterior`/`redhouseinterior2` · `Asha`/`asha` · `Fatiha`/`fatiha` ·
`sambefore`/`sambefore-2` · `milo` ×2 · `milobefore` ×2.
Et trois à jeter : `loc_xxx`, `xxx`, `My-Element`.

Les tableaux de réglages nomment déjà **la version à choisir** pour chaque plan.

---

## 🟠 3. Un plan dépasse le plafond de Seedance 2.0

**Seedance 2.0 plafonne à 15 s** (contre 30 s en 2.5). Un seul plan dépasse : **10J, 19 s** —
c'est le montage « DEHORS », cinq micro-plans dans cinq lieux différents.

Il faut le couper en trois générations, ce qui est de toute façon plus sûr que de demander
cinq lieux à une seule génération :

| | Contenu | Lieu | Durée |
|---|---|---|---|
| **10J-1** | shots 1 + 2 — il pose la première ligne, puis la pièce entière est écrite | maison rouge | 9 s |
| **10J-2** | shots 3 + 4 — il parle à Anna, puis aux trois femmes | cuisine d'Anna, restaurant | 6 s |
| **10J-3** | shot 5 — le manteau quitté derrière le chariot | couloir de la bibliothèque | 4 s |

Le montage garde les mêmes 9,5 s. Ça fait passer le film de 62 à **64 générations**.

---

## Ce que ça coûte, maintenant qu'on a un prix réel

1A a coûté **91 crédits** pour 10 s en 720p — soit **~9,1 crédits/seconde**. Le film fait
**591 s de rushes**. En 1080p le tarif est plus élevé qu'en 720p : compte **au moins
5 400 crédits**, probablement davantage. C'est la contrainte n°1 des jours qui restent.

**Mesure le vrai prix sur un plan avant de lancer la suite** : génère 1C en 1080p et regarde
ce qu'il retire. À partir de là on saura si le film entier tient dans ton budget, ou s'il faut
descendre certains plans en 720p.
