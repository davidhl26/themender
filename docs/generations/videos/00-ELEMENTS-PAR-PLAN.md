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
