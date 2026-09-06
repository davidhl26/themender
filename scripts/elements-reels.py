#!/usr/bin/env python3
"""Inventaire reel des Elements du compte, et la carte corpus -> compte.

Releve le 06/09 via show_reference_elements. Deux problemes en sortent :
  - des DOUBLONS (kitchen x3, restaurant x3, quay x2, et une serie CamelCase/minuscule)
  - des Elements CITES par les blocs qui n'existent pas du tout sur le compte
"""

# nom dans le corpus -> nom exact sur le compte (None = n'existe pas encore)
CARTE = {
    # personnages
    'Sam': 'sam', 'SamBefore': 'sambefore', 'SamAfter': 'samafter',
    'Maeve': 'maeva',
    'Nora': 'nora', 'NoraBefore': 'norabefore',
    'Milo': 'milo', 'MiloBefore': 'milobefore',
    'Mender': 'mender', 'Anna': 'anna', 'Mei': 'mei', 'Fatiha': 'fatiha', 'Asha': 'asha',
    # personnages MANQUANTS
    'MaeveIll': None, 'SamSDF': None, 'AnnaYoung': None, 'Kolya11': None, 'Kolya2': None,
    'WardDoctor': None, 'YoungMother': None, 'YoungMotherHospital': None,
    # lieux
    'Kitchen': 'Kitchen-1', 'Quay': 'Quay', 'Restaurant': 'Restaurant',
    'HospitalRoom': 'HospitalRoom', 'HospitalCorridor': 'HospitalCorridor',
    'AnnaKitchen': 'AnnaKitchen', 'NoraBedroom': 'NoraBedroom', 'BackGallery': 'BackGallery',
    'Bathroom': 'Bathroom', 'LibraryCorridor': 'LibraryCorridor', 'NightBus': 'NightBus',
    'BusShelter': 'BusShelter', 'RedHouseExterior': 'RedHouseExterior',
    'RedHouseInterior': 'redhouseinterior', 'AnnaKitchenPast': 'AnnaKitchenPast',
    'RussianHospitalCorridor': 'RussianHospitalCorridor', 'RussianNightStreet': 'RussianNightStreet',
    'RussianCourtyard': 'RussianCourtyard',
    'RussianHospitalWard': None,
    # accessoires : jamais des Elements, on les decrit au prompt
    'MotherRing': None, 'Mailbox': None, 'CounterBowl': None, 'FoldedNote': None,
    'GreenBandPlate': None, 'AnnaDrawing': None,
}

# nom affiche dans le corps du prompt, une fois la mention liee en tete
NOM = {
    'sam': 'SAM', 'sambefore': 'SAM', 'samafter': 'SAM',
    'maeva': 'MAEVE', 'nora': 'NORA', 'norabefore': 'NORA',
    'milo': 'MILO', 'milobefore': 'MILO', 'mender': 'THE MENDER',
    'anna': 'ANNA', 'mei': 'MEI', 'fatiha': 'FATIHA', 'asha': 'ASHA',
}

# doublons a nettoyer dans l'interface : (a garder, a supprimer)
DOUBLONS = [
    ('Kitchen-1', 'kitchen (x2, ce sont des ANGLES, pas le master), kitchen-2'),
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
