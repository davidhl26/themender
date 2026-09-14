#!/usr/bin/env python3
"""Inventaire reel des Elements du compte, et la carte corpus -> compte.

Releve le 06/09 via show_reference_elements. Deux problemes en sortent :
  - des DOUBLONS (kitchen x3, restaurant x3, quay x2, et une serie CamelCase/minuscule)
  - des Elements CITES par les blocs qui n'existent pas du tout sur le compte
"""

# nom dans le corpus -> nom exact sur le compte (None = n'existe pas encore)
# Releve sur les captures de l'interface, le 14/09 — apres le nettoyage des doublons.
# C'est le selecteur qui fait foi, pas l'API : elle listait encore des Elements supprimes.
# 19 lieux + 11 personnages. Tout est en minuscules SAUF @Quay.
CARTE = {
    # --- personnages presents ---
    'Sam': 'samafter', 'SamAfter': 'samafter', 'SamBefore': 'sambefore',
    'Maeve': 'maeva',
    'Nora': 'nora', 'NoraBefore': 'norabefore',
    'Milo': 'milo', 'MiloBefore': 'milobefore',
    'Mender': 'mender', 'Anna': 'anna', 'Fatiha': 'fatiha', 'Asha': 'asha',
    # @mei n'apparait pas sur les captures mais l'API le listait : la grille etait
    # peut-etre coupee. A confirmer dans le selecteur avant de generer la sequence 5.
    'Mei': 'mei',
    # --- personnages ABSENTS du selecteur ---
    'MaeveIll': None, 'SamSDF': None, 'AnnaYoung': None, 'Kolya11': None, 'Kolya2': None,
    'WardDoctor': None, 'YoungMother': None, 'YoungMotherHospital': None,
    # --- lieux presents ---
    'Kitchen': 'kitchen', 'Quay': 'Quay', 'Restaurant': 'restaurant',
    'HospitalRoom': 'hospitalroom', 'HospitalCorridor': 'hospitalcorridor',
    'AnnaKitchen': 'annakitchen', 'NoraBedroom': 'norabedroom', 'BackGallery': 'backgallery',
    'Bathroom': 'bathroom', 'LibraryCorridor': 'librarycorridor', 'NightBus': 'nightbus',
    'BusShelter': 'busshelter', 'RedHouseExterior': 'redhouseexterior',
    'RedHouseInterior': 'redhouseinterior', 'AnnaKitchenPast': 'annakitchenpast',
    'RussianHospitalCorridor': 'russianhospitalcorridor',
    'RussianNightStreet': 'russiannightstreet', 'RussianCourtyard': 'russiancourtyard',
    # --- lieux ABSENTS ---
    'RussianHospitalWard': None,
    # --- accessoires : jamais des Elements, on les decrit au prompt ---
    'MotherRing': None, 'Mailbox': None, 'CounterBowl': None, 'FoldedNote': None,
    'GreenBandPlate': None, 'AnnaDrawing': None,
}

# nom affiche dans le corps du prompt, une fois la mention liee en tete
NOM = {
    'samafter': 'SAM', 'sambefore': 'SAM',
    'maeva': 'MAEVE', 'nora': 'NORA', 'norabefore': 'NORA',
    'milo': 'MILO', 'milobefore': 'MILO', 'mender': 'THE MENDER',
    'anna': 'ANNA', 'mei': 'MEI', 'fatiha': 'FATIHA', 'asha': 'ASHA',
}

# doublons a nettoyer dans l'interface : (a garder, a supprimer)
DOUBLONS = [
    ('— nettoyage fait le 14/09 par David : 19 lieux + 11 personnages, plus de doublons', ''),
    ('Restaurant', 'restaurant (x2, auto)'),
    ('Quay', 'Quay en double'),
    ('NightBus', 'nightbus'), ('BackGallery', 'backgallery'),
    ('LibraryCorridor', 'librarycorridor'), ('Bathroom', 'bathroom'),
    ('HospitalRoom', 'hospitalroom'), ('HospitalCorridor', 'hospitalcorridor'),
    ('NoraBedroom', 'norabedroom'), ('AnnaKitchen', 'annakitchen'),
    ('BusShelter', 'busshelter'), ('RedHouseExterior', 'redhouseexterior'),
    ('AnnaKitchenPast', 'annakitchenpast'),
    ('RussianHospitalCorridor', 'russianhospitalcorridor'),
    ('RussianNightStreet', 'russiannightstreet'), ('RussianCourtyard', 'russiancourtyard'),
    ('redhouseinterior', 'redhouseinterior2'),
    ('Asha', 'asha en double'), ('Fatiha', 'fatiha en double'),
    ('sambefore', 'sambefore-2'), ('milobefore', 'milobefore en double'), ('milo', 'milo en double'),
    ('—', 'loc_xxx, xxx, My-Element : a supprimer'),
]
