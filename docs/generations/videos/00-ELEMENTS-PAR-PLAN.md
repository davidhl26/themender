# LES ELEMENTS À CHARGER — plan par plan

> **Avant de coller un bloc**, charge dans Higgsfield les Elements listés sur sa ligne.
> Le bloc les nomme déjà par leur `@` dans sa section `ACTIVE REFERENCES` : si l'Element
> n'est pas chargé, le modèle invente le personnage ou le décor.

> 🎭 personnage · 🏠 lieu · 📦 objet · ⛓ = ajoute AUSSI le clip précédent en **référence vidéo**


## Séquence 1

| Bloc | 🎭 Personnages | 🏠 Lieu | 📦 Objet | ⛓ Vidéo préc. |
|---|---|---|---|---|
| **1A** | `@SamBefore` · `@Maeve` | `@Kitchen` | — | — *(tête)* |
| **1B** | `@SamBefore` · `@Maeve` | `@Kitchen` | — | `1A` |
| **1C** | `@SamBefore` · `@Maeve` · `@NoraBefore` · `@MiloBefore` | `@Kitchen` | — | `1B` |
| **1D** | — | `@Kitchen` | — | `1C` |

## Séquence 2

| Bloc | 🎭 Personnages | 🏠 Lieu | 📦 Objet | ⛓ Vidéo préc. |
|---|---|---|---|---|
| **2A** | `@SamBefore` · `@Maeve` · `@NoraBefore` · `@MiloBefore` | `@Quay` | — | `1D` |
| **2B** | `@SamBefore` · `@Maeve` · `@NoraBefore` · `@MiloBefore` | `@Quay` | — | `2A` |
| **2C** | `@SamBefore` · `@Maeve` · `@NoraBefore` · `@MiloBefore` · `@Mei` | `@Restaurant` | — | `2B` |
| **2D** | `@SamBefore` · `@Maeve` · `@NoraBefore` · `@MiloBefore` | `@Restaurant` | — | `2C` |

## Séquence 3

| Bloc | 🎭 Personnages | 🏠 Lieu | 📦 Objet | ⛓ Vidéo préc. |
|---|---|---|---|---|
| **3A** | `@Maeve` | `@Kitchen` | — | `2D` |
| **3B** | `@SamBefore` · `@NoraBefore` | `@HospitalCorridor` | — | `3A` |
| **3C** | `@MaeveIll` · `@MiloBefore` | `@HospitalRoom` | — | `3B` |
| **3D** | `@MaeveIll` · `@NoraBefore` | `@HospitalRoom` | `@MotherRing` | `3C` |
| **3E** | `@MaeveIll` · `@SamBefore` | `@HospitalCorridor` · `@HospitalRoom` | — | `3D` |
| **3F** | `@NoraBefore` · `@SamBefore` | `@HospitalCorridor` | — | `3E` |

## Séquence 4

| Bloc | 🎭 Personnages | 🏠 Lieu | 📦 Objet | ⛓ Vidéo préc. |
|---|---|---|---|---|
| **4A** | `@Nora` | `@NoraBedroom` | — | — *(tête)* |
| **4B** | `@Nora` · `@Anna` | `@AnnaKitchen` | `@AnnaDrawing` | `4A` |
| **4C** | `@Nora` · `@Anna` | `@AnnaKitchen` | `@AnnaDrawing` | `4B` |
| **4D** | `@Nora` · `@Anna` | `@AnnaKitchen` | — | `4C` |
| **4E** | `@AnnaYoung` · `@Kolya11` · `@WardDoctor` | `@RussianHospitalWard` · `@RussianHospitalCorridor` | — | — *(tête)* |
| **4F** | `@YoungMotherHospital` · `@WardDoctor` | `@RussianHospitalCorridor` | — | `4E` |
| **4G** | `@AnnaYoung` · `@WardDoctor` · `@YoungMotherHospital` | `@RussianHospitalCorridor` | — | `4F` |
| **4H** | `@AnnaYoung` · `@Mender` | `@AnnaKitchenPast` | — | `4G` |
| **4I** | `@AnnaYoung` · `@Mender` · `@YoungMother` · `@Kolya2` | `@RussianCourtyard` | — | `4H` |

## Séquence 5

| Bloc | 🎭 Personnages | 🏠 Lieu | 📦 Objet | ⛓ Vidéo préc. |
|---|---|---|---|---|
| **5A** | `@Sam` · `@Nora` · `@Milo` · `@Mei` | `@Restaurant` | — | `4D` |
| **5B-1** | `@Nora` · `@Mei` · `@Asha` · `@Fatiha` | `@Restaurant` | — | `5A` |
| **5B-2** | `@Nora` · `@Mei` · `@Asha` · `@Fatiha` | `@Restaurant` | — | `5B-1` |
| **5C** | `@Sam` | `@Restaurant` | — | `5B-2` |
| **5D** | `@Sam` · `@Nora` · `@Milo` · `@Mei` · `@Asha` · `@Fatiha` | `@Restaurant` | — | `5C` |
| **5D-bis** | `@Nora` | `@Restaurant` | — | `—` |

## Séquence 6

| Bloc | 🎭 Personnages | 🏠 Lieu | 📦 Objet | ⛓ Vidéo préc. |
|---|---|---|---|---|
| **6A** | `@Nora` | `@NoraBedroom` | — | `5D` |
| **6A-bis** | — | `@NoraBedroom` | — | `—` |
| **6B** | `@Nora` | `@BackGallery` | — | `6A` |
| **6B-bis** | `@Nora` | `@BackGallery` | — | `—` |
| **6C** | `@Nora` · `@Sam` | `@NoraBedroom` | — | `6B` |

## Séquence 7

| Bloc | 🎭 Personnages | 🏠 Lieu | 📦 Objet | ⛓ Vidéo préc. |
|---|---|---|---|---|
| **7A** | `@Nora` | `@BackGallery` · `@Kitchen` | — | `6C` |
| **7B** | `@Nora` | `@BackGallery` · `@NoraBedroom` | — | `7A` |

## Séquence 8

| Bloc | 🎭 Personnages | 🏠 Lieu | 📦 Objet | ⛓ Vidéo préc. |
|---|---|---|---|---|
| **8A** | `@Nora` · `@Mender` | `@LibraryCorridor` | — | `7B` |
| **8A-bis** | `@Mender` | `@LibraryCorridor` | — | `—` |
| **8B** | `@Nora` · `@Mender` | `@NoraBedroom` | — | `8A` |
| **8B-bis** | `@Mender` | `@NoraBedroom` | — | `—` |
| **8C** | `@Nora` | `@Bathroom` | — | `8B` |
| **8C-bis** | — | `@Bathroom` | — | `—` |
| **8D** | `@Nora` | `@NoraBedroom` | `@MotherRing` | `8C` |
| **8E** | `@Nora` | `@NightBus` | — | `8D` |

## Séquence 9

| Bloc | 🎭 Personnages | 🏠 Lieu | 📦 Objet | ⛓ Vidéo préc. |
|---|---|---|---|---|
| **9A** | `@Nora` · `@SamSDF` | `@BusShelter` | — | `8E` |
| **9B** | `@Nora` · `@SamSDF` | `@BusShelter` | — | `9A` |
| **9C** | `@Nora` · `@SamSDF` | `@BusShelter` | — | `9B` |

## Séquence 10

| Bloc | 🎭 Personnages | 🏠 Lieu | 📦 Objet | ⛓ Vidéo préc. |
|---|---|---|---|---|
| **10A** | `@Nora` | `@RedHouseExterior` | — | — *(tête)* |
| **10B** | `@Nora` | `@RedHouseInterior` | — | `10A` |
| **10C** | `@Nora` | `@RedHouseInterior` | — | `10B` |
| **10D-1** | `@Nora` | `@RedHouseInterior` | — | — *(tête)* |
| **10D-2** | `@Nora` | `@RedHouseInterior` | — | `10D-1` |
| **10E** | `@Nora` | `@RedHouseInterior` | — | `10D-2` |
| **10F-1** | `@Nora` | `@RedHouseInterior` | — | `10E` |
| **10F-2** | — | `@RedHouseExterior` | — | `10F-1` |
| **10F-3** | — | — | — | `10F-2` |
| **10F-4** | `@SamSDF` | `@BusShelter` | — | `10F-3` |
| **10H** | `@SamSDF` · `@Sam` | `@BusShelter` | — | `10F-4` |
| **10I** | `@Sam` · `@Nora` · `@Mender` | `@NoraBedroom` · `@Kitchen` · `@Bathroom` | — | `10H` |
| **10J** | `@Sam` · `@Anna` · `@Mei` · `@Fatiha` · `@Asha` · `@Mender` | `@RedHouseInterior` · `@AnnaKitchen` · `@Restaurant` · `@LibraryCorridor` | — | `10I` |
| **10K** | `@MaeveIll` · `@SamBefore` | `@HospitalCorridor` · `@HospitalRoom` | — | — *(tête)* |
| **10L** | `@SamSDF` · `@Sam` | `@BusShelter` | — | `10H` |

---

## Toutes les fiches à créer une fois pour toutes

| `@Element` | Ce que c'est |
|---|---|
| `@Anna` | 🎭 personnage |
| `@AnnaDrawing` | 📦 objet |
| `@AnnaKitchen` | 🏠 lieu |
| `@AnnaKitchenPast` | 🏠 lieu |
| `@AnnaYoung` | 🎭 personnage |
| `@Asha` | 🎭 personnage |
| `@BackGallery` | 🏠 lieu |
| `@Bathroom` | 🏠 lieu |
| `@BusShelter` | 🏠 lieu |
| `@Fatiha` | 🎭 personnage |
| `@HospitalCorridor` | 🏠 lieu |
| `@HospitalRoom` | 🏠 lieu |
| `@KidsBedroom` | 🏠 lieu |
| `@Kitchen` | 🏠 lieu |
| `@Kolya11` | 🎭 personnage |
| `@Kolya2` | 🎭 personnage |
| `@LibraryCorridor` | 🏠 lieu |
| `@Maeve` | 🎭 personnage |
| `@MaeveIll` | 🎭 personnage |
| `@Mei` | 🎭 personnage |
| `@Mender` | 🎭 personnage |
| `@Milo` | 🎭 personnage |
| `@MiloBefore` | 🎭 personnage |
| `@MotherRing` | 📦 objet |
| `@NightBus` | 🏠 lieu |
| `@Nora` | 🎭 personnage |
| `@NoraBedroom` | 🏠 lieu |
| `@NoraBefore` | 🎭 personnage |
| `@Quay` | 🏠 lieu |
| `@RedHouseExterior` | 🏠 lieu |
| `@RedHouseInterior` | 🏠 lieu |
| `@Restaurant` | 🏠 lieu |
| `@RussianCourtyard` | 🏠 lieu |
| `@RussianHospitalCorridor` | 🏠 lieu |
| `@RussianHospitalWard` | 🏠 lieu |
| `@RussianNightStreet` | 🏠 lieu |
| `@Sam` | 🎭 personnage |
| `@SamBefore` | 🎭 personnage |
| `@SamSDF` | 🎭 personnage |
| `@WardDoctor` | 🎭 personnage |
| `@YoungMother` | 🎭 personnage |
| `@YoungMotherHospital` | 🎭 personnage |

---

## ✅ LES ELEMENTS DE LIEUX EXISTENT — créés le 01/09

Les 17 lieux du film sont maintenant enregistrés comme Elements dans Higgsfield, chacun **sur son
image MASTER** et nommé comme dans les documents. Il n'y a plus rien à créer : tu les charges, c'est tout.

| `@Element` | id | Doc | Note |
|---|---|---|---|
| `@Kitchen-1` | `efb7e486-7d41-4ec4-865e-fb7819d4aca5` | LIEU-01 | ⚠ le nom `Kitchen` était pris |
| `@Quay` | `1995747d-a3fa-4f1c-b961-2447df509713` | LIEU-02 |  |
| `@HospitalRoom` | `00091ff6-c8a3-4c7e-9f14-c3b8806cbcde` | LIEU-04 |  |
| `@HospitalCorridor` | `039e0c17-5dba-49a0-9dfe-da2d897bb14d` | LIEU-05 |  |
| `@AnnaKitchen` | `1f52688d-eb2d-4d22-8dc8-fc0fe0767c80` | LIEU-06 |  |
| `@Restaurant` | `4c45eb46-6391-4f9d-aa7a-90ef92edd9db` | LIEU-07 |  |
| `@NoraBedroom` | `0bf65b3a-34df-4562-be24-0f7624c66e6a` | LIEU-08 |  |
| `@BackGallery` | `8bf5cd08-b418-4689-9133-2d7f7aa85979` | LIEU-09 |  |
| `@Bathroom` | `c80c273b-a960-482b-beaf-45527dcff4e9` | LIEU-10 |  |
| `@LibraryCorridor` | `016f6c5b-c26c-436c-98e2-2e78afa55441` | LIEU-11 |  |
| `@NightBus` | `1ebc89e2-22e8-43cf-8d2e-3c04d0a7a87a` | LIEU-13 |  |
| `@BusShelter` | `17adad6f-6137-4e3b-b077-4c74f841a7e5` | LIEU-14 |  |
| `@RedHouseExterior` | `94d4c41e-65e3-47a4-b439-c4da10c4f06d` | LIEU-15 |  |
| `@RussianHospitalCorridor` | `68b57993-3631-4e60-ad55-a64ddd3c680e` | LIEU-17 |  |
| `@AnnaKitchenPast` | `1b2dd5fd-f718-4117-9f0b-45c46b61d28a` | LIEU-18 |  |
| `@RussianNightStreet` | `eefb91c7-75b6-4129-a423-64b5d3d90d83` | LIEU-19 |  |
| `@RussianCourtyard` | `ee53660d-1112-4f1e-ab18-7bbed83c9362` | LIEU-20 |  |

### ⚠ Deux choses à savoir

**1. `@Kitchen` s'appelle `@Kitchen-1`.** Un Element `kitchen` existait déjà — construit sur l'ANGLE H,
pas sur le master — et Higgsfield a refusé le doublon. **Supprime l'ancien `kitchen` dans l'interface**,
puis renomme `Kitchen-1` en `Kitchen`. Sans ça, les blocs qui disent `@Kitchen` ne trouveront rien.

**2. `@RedHouseInterior` n'existe pas, et c'est voulu.** Ses images sont celles du 27/08, marquées
PÉRIMÉES : écritures ivoire et lampe à pétrole au lieu de l'ampoule électrique. **Génère d'abord les
quatre images v2** (prompt prêt dans `LIEU-16 §v2`), puis sauvegarde la v2 A comme Element.
En attendant, toute la séquence 10 intérieure est bloquée.

*(Les personnages étaient déjà tous enregistrés : nora, sam, sambefore, samafter, milo, milobefore,
norabefore, maeva, anna, mei, asha, fatiha, mender.)*
