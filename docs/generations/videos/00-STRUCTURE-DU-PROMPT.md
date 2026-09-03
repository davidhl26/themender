# LA STRUCTURE DU PROMPT DE GÉNÉRATION VIDÉO

> Le squelette réel des 62 blocs de THE MENDER, relevé sur le bloc 4B.
> Chaque en-tête est en CAPITALES, seul sur sa ligne, suivi de son contenu.
> Ordre imposé : le modèle pondère le début et surtout **la fin**.

```
SCENE CONTEXT
Ce qui se passe, en deux ou trois phrases. La durée. Le nombre de cadrages et de coupes.
Se termine toujours par : « Every second is choreographed below; nothing beyond it may be invented. »

CONTINUITY REFERENCE — <THIS SHOT CONTINUES THE ATTACHED VIDEO | SAME FILM, DIFFERENT PLACE | NO VIDEO IS ATTACHED>
THE VIDEO ATTACHED TO THIS GENERATION is <le plan précédent, nommé>. Ce qu'il faut en reprendre,
et ce qu'il ne faut PAS en reprendre. ⚠ Jamais écrire « @Video » : l'éditeur Higgsfield l'avale.

HANDOFF — THE EXACT STATE THIS SHOT INHERITS FROM THE ATTACHED VIDEO
L'image sur laquelle le plan précédent se termine, recopiée au chiffre près.
« These are NOT new positions to invent… the first frame must reproduce it exactly before anything moves. »

ACTIVE REFERENCES
@Element : sa description en une phrase + « 100% matches the reference. » Un par ligne.

TEMPERAMENT, <PERSONNAGE>
Quel genre de personne fait le geste. Une carte par personnage RÉELLEMENT au cadre — jamais un de plus.

LOCATION MAP
Qui est où, cadrage par cadrage, en pourcentages de cadre et en centimètres. Jamais « close-up ».

FIRST FRAME AND SPATIAL BLOCKING
La toute première image, décrite en mots — on ne compte pas sur l'image de départ pour dire le cadre.
« This is the frame the first video frame must already be, before anything moves. »

FORMAT MODE
Durée exacte. Une prise continue, ou N cadrages joints par N-1 coupes franches. Rien d'autre.

OPTICS
Focale, ouverture, profondeur de champ, comportement du point.

CONTINUITY LOCK
Ce qui ne peut ni apparaître, ni disparaître, ni bouger. Les postures, verrouillées.

PROP LAYOUT — FIXED
Chaque accessoire : sa place, son état, son usure. Ce qui n'est pas listé n'existe pas.

FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND
    SHOT n [x.x-y.ys] — le cadrage, en toutes lettres
    [x.xs] Positions de départ, tenues jusqu'à mention contraire
    [x.x-y.ys] Un événement physique par intervalle. Jamais une émotion : les gestes qui la trahissent.
    HARD CUT
Le cœur du bloc. C'est ici qu'on est plus précis que tout le monde.

SUBJECT LOCK, <PERSONNAGE>
Le corps exact et la garde-robe exacte. « He never looks at the lens. »

CROSS-FRAME RULES
Ce qui doit tenir d'un cadrage à l'autre. NO INVENTED ACTION : ce qui n'est pas décrit ne bouge pas.

CONTINUITY — WHAT MUST NOT DRIFT
Personne n'est mieux coiffé, mieux habillé ni mieux reposé qu'au plan d'avant.

LOCATION
La géométrie canonique du lieu, jamais variée.

LIGHT
LA source. Une seule, motivée. Ce qu'elle fait à chaque surface.

DIALOGUE
Les répliques avec leur horodatage et leur ton. « Nobody else speaks. No other line is added. »

LAST FRAME — THE EXACT STATE THIS SHOT HANDS OVER, because the next shot opens on it
WHAT IS IN THE FRAME AT THE LAST INSTANT : ce que le plan montre vraiment à la dernière image.
WHERE THIS SHOT LEAVES EACH BODY, to the number : @X: POSTURE, x=NN%, filling NN% of frame height.
C'est ce bloc que le HANDOFF du plan suivant recopie.

CHARACTER PERFORMANCE
« Nobody performs an emotion here. » Les postures de chacun, du premier au dernier frame.

PHYSICS — WEIGHT, INERTIA, CONTACT
Tout a une masse et lui obéit. Le vêtement traîne, le cheveu suit d'un temps, rien ne traverse rien.

WORLD — <BEFORE | AFTER | THE WASHED MEMORY | THE RED HOUSE>
Où ce plan se situe dans l'arc du film. « This is the light the rest of the film will lose. »

CINEMATOGRAPHY
La lumière DE CE PLAN. Combien de sources, exposition, hautes lumières bridées.

FILM EMULATION — THE SAME STOCK FROM THE FIRST FRAME TO THE LAST
Kodak Vision3 500T 5219. Une pellicule, un labo, du premier plan au dernier. Jamais changer.

CAMERA REGISTER — <ALIVE | HOLDING ITS BREATH | LOCKED | MOVING AGAIN>
La caméra en trois actes : vivante avant la mort, suspendue en séq. 3, verrouillée ensuite,
mobile à nouveau dans la maison rouge.

CAMERA — OPERATED, NOT SIMULATED
Un corps tient l'appareil. Le point arrive quelques images en retard. Jamais d'immobilité robotique.

PHOTOGRAPHIC REALISM
Pores, tissage, usure réelle, flou de bougé naturel. Sous-exposé où la scène le demande.

AUDIO
SFX only. No music. Chaque son nommé, avec son instant.

POSITIVE CONSTRAINTS — CHECK EVERY FRAME AGAINST THESE
Les règles reformulées en POSITIF. C'est la position que le modèle pondère le plus fort.

AVOID
Les interdits, en liste. Tout ce qui ne doit jamais entrer au cadre.
```

---

## Les trois blocs qui n'existent nulle part ailleurs

Le PDF **« 5 Levels of AI Video Prompting »** donne le squelette *(SCENE, FRAME MAP, SUBJECT LOCK,
CROSS-FRAME RULES, LOCATION, LIGHT, CAMERA, LAST FRAME, AUDIO, NEGATIVE PROMPT)*.
Les **six prompts concurrents** ajoutent la grammaire *(SCENE CONTEXT, ACTIVE REFERENCES, FIRST FRAME,
FORMAT MODE, OPTICS, PHYSICS, FILM EMULATION, POSITIVE CONSTRAINTS)*.

Trois sections ne viennent ni de l'un ni des autres :

| | Pourquoi elle existe |
|---|---|
| **`HANDOFF`** | Le PDF dit lui-même : *« it has no field for frame position, cross-shot continuity, so add those back yourself »*. Les Elements tiennent le visage et le décor, pas la position dans l'espace. |
| **`LAST FRAME` chiffré** | L'autre bout du même contrat. Sans lui, le HANDOFF n'aurait rien à recopier. |
| **`CAMERA REGISTER`** | Fait varier la caméra selon l'acte, au lieu d'un réglage unique pour tout le film. |

## Deux règles de forme

**Tout en anglais à l'intérieur du bloc.** Le français vit autour, jamais dedans.

**Jamais de `@` devant autre chose qu'un Element.** L'éditeur Higgsfield parse toute mention `@…`
comme une référence et l'avale — c'est ce qui a fait disparaître `@Video 1` d'un prompt entier.
