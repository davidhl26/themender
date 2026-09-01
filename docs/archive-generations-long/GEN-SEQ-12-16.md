# THE MENDER — Générations regroupées · SÉQUENCES 13 à 16

> Écrit d'après `docs/plans/PLANS-SEQ-12-16.md` (matière première), `docs/SCRIPT-THE-MENDER.md`
> (**le script fait foi**) et `docs/PROMPT-PACK-THE-MENDER.md` §3 (réglages Cinema Studio, @tags).
> Format : **niveau 4 complet** (SCENE · FRAME MAP timestampé + x=% · SUBJECT LOCK · CROSS-FRAME
> RULES · LOCATION · LIGHT · MOVEMENT avec HARD CUT · DIALOGUE timecodé · CAMERA par segment ·
> LAST FRAME · AUDIO · NEGATIVE) **enrichi niveau 5** (@tags Éléments + réglages réels).
> Objectif : **le moins de générations possible** — chaque bloc ci-dessous = UNE génération.

## Vue d'ensemble

**12 blocs · 82,5 s couverts · 36 plans du découpage (35 segments — 14.6+14.7 fusionnés en un
segment continu).**

| Bloc | Séq. | Plans couverts | Lieu (un seul par bloc) | Durée | Segments |
|---|---|---|---|---|---|
| 12-A | 12 | 13.1 → 13.5 | @Kitchen (la fenêtre) | 10,5 s | 5 |
| 12-B | 12 | 13.6 | @NoraBedroom | 2 s | 1 |
| 13 | 13 | 14.1 → 14.7 | @LibraryCorridor | 15 s | 6 |
| 14 | 14 | 15.1 → 15.3 | @Bathroom | 7,5 s | 3 |
| 15-A | 15 | 16.1 | chambre de Nora (macro, hors Élément) | 2,5 s | 1 |
| 15-B | 15 | 16.2 → 16.3 | @Kitchen (plan de travail) | 3 s | 2 |
| 15-C | 15 | 16.4 | @KidsBedroom (depuis le seuil) | 2 s | 1 |
| 15-D | 15 | 16.5 → 16.6 | l'entrée — les deux faces de la même porte | 5 s | 2 |
| 15-E | 15 | 16.7 | rue de nuit (hors Élément) | 3 s | 1 |
| 15-F | 15 | 16.8 → 16.9 | @NightBus | 4,5 s | 2 |
| 16-A | 16 | 17.1 → 17.6 | @BusShelter | 14 s | 6 |
| 16-B | 16 | 17.7 → 17.11 | @BusShelter | 13,5 s | 5 |

**Règles de groupage appliquées** : jamais deux séquences dans un bloc ; un bloc = un lieu ;
2 à 6 plans par bloc, 15 s maximum. Les blocs sous 8 s sont **imposés** par la règle du lieu
unique (séq. 16 change de décor presque à chaque plan) ou par la durée du script (séq. 15 :
7,5 s en tout ; 13.6 : plan solitaire dans son propre décor).

**Durées à la génération** : durée non entière ou sous le minimum du moteur → générer à la durée
acceptée immédiatement supérieure et **couper au montage** ; les timecodes des FRAME MAP restent
ceux du script.

**Réglages du monde gris (tous les blocs)** : Genre **Noir** · Style **Manual** · Camera
**Fine Film** · Lens **Anamorphic** · f/2 · 21:9 · 1080p · sound on. La focale est un réglage
unique par génération : **50 mm** par défaut, **85 mm** quand le bloc est dominé par des inserts
(15-A, 15-B) ; à l'intérieur d'un bloc, le caractère « long lens / wide » restant se demande dans
les lignes CAMERA. Caméra posée partout — **une seule exception : le segment 14.4 (caméra
portée, la première du film).**

**Rappels opposables** (recopiés en toutes lettres dans les NEGATIVE de chaque bloc concerné) —
**RÈGLE B** : aucun rouge nulle part, sauf le manteau en 14.3 **presque brun en contre-jour** ;
séq. 14 signalétique de sortie verte, aucun extincteur ; séq. 16 bus de trois quarts avant, feux
arrière et bandeaux hors champ, aucun feu de circulation, aucune bouche d'incendie ; séq. 17
caisson publicitaire **vide, blanc laiteux**. **RÈGLE D** : le SDF cadré **coupé à hauteur de
bouche dans chaque segment où il apparaît**, les yeux jamais visibles — et le NEGATIVE l'interdit
explicitement. **RÈGLE F0** : la barbe du SDF est la vraie barbe de @Sam. **RÈGLE H** : rien de
surnaturel — le miroir révèle d'un bloc un film de savon du matin. **RÈGLE I** : capitales
bâtonnées uniquement ; le papier de 14.6 est un dessin, **aucun mot**. Tout texte à l'écran est
**[POST]**, jamais généré (liste en fin de fichier).

---

## SÉQUENCE 13 — LE SILENCE *(12,5 s — cinq matins, puis un sixième — 2 blocs)*

> **Dérogation de méthode, assumée** : le script (CADRES RÉFÉRENTS) prévoyait une plate unique
> déclinée par édition d'image et animée 2 s par matin (6 générations). Le bloc 12-A remplace les
> cinq animations de la fenêtre par **UNE génération à cadre verrouillé** — la tenue du cadre est
> imposée par le FRAME MAP et les CROSS-FRAME RULES, et la **plate 13.0** du découpage sert
> d'image de départ. **Repli** : si le cadre dérive entre les coupes, revenir à la méthode du
> script (plate + éditions, plan par plan). 13.6 reste un bloc à part : autre lieu, et c'est
> l'arrêt de la série de cadres qui le signale.

### BLOC 12-A — 10,5 s — « Cinq matins à la fenêtre » *(plans 13.1 → 13.5)*

```
Elements @Nora + @Kitchen (plate 13.0 as start frame). 21:9, 1080p, 10.5s, sound on.
Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 50mm, f/2.
Style prompt: flat grey overcast daylight from the single window as the only source, no fill, low
contrast, camera locked off on one identical frame for the entire runtime, no handheld shake.

SCENE
Five mornings at the same kitchen window, one locked frame repeated. Every shot is the exact same
framing; only the stated details change between mornings. Five shots, hard cuts.

FRAME MAP
[0-2s] @Nora from behind, waist-up, centred x=50%, filling 70% of frame height, at the kitchen
window which fills the frame; a mug held in both hands close to her chest; the narrow back alley
below empty; thin rain streaking the glass.
[2-4s] The identical frame. The rain now slants across the glass in the opposite direction; the
light one step darker; the mug still in her hands; her shoulders one centimetre lower.
[4-6s] The identical frame. No mug: her arms crossed over her chest, her forehead resting against
the cold glass, a small patch of breath-fog on the pane swelling and shrinking with each exhale.
[6-8s] The identical frame. Her head bowed — she looks down at her own hands, turning them over
slowly, palms up, palms down; the window behind her a sheet of white; the rain stopped.
[8-10.5s] The identical frame WITHOUT her. The window alone for a full second; then deep in the
background, small and soft-focus, @Nora crosses the kitchen from one side to the other without
even glancing at the window, and exits the frame.

SUBJECT LOCK, NORA
Fifteen, thin, shoulders rounded inward, long dark brown wavy unwashed hair, oversized faded
charcoal-grey hoodie with worn cuffs. Seen from behind in every shot; her face is never visible,
not once.

CROSS-FRAME RULES
All five shots are the exact same locked-off camera and framing — same window, same walls, same
lens height, held to the pixel: the cuts read as different mornings, never as different places.
@Nora is the same girl in every shot, same hair, same hoodie. The alley below stays empty in all
five shots — no figure ever appears in it. The mug exists only in shots one and two. The light
sinks one step per morning through shot four.

LOCATION
@Kitchen — the single kitchen window over a narrow back alley, no practical lights on, worn wood
and faded sage walls falling to shadow at the frame edges. No red anywhere.

LIGHT
Flat grey overcast daylight through the window only, no fill: one step darker in shots two and
three, a blank white sheet in shot four, flat grey again in shot five.

MOVEMENT
[0-2s] First morning. She scans the alley below, her head moving in small slow increments, left,
then right. The alley is empty. She never turns around.
HARD CUT
[2-4s] Second morning. She still holds the mug, she still scans. The alley is still empty.
HARD CUT
[4-6s] Third morning. She no longer scans: she leans, forehead to the glass, her breath fogging
and clearing on the pane.
HARD CUT
[6-8s] Fourth morning. She has stopped watching the alley: she looks down at her own hands,
turning them over slowly. She does not check the window once.
HARD CUT
[8-10.5s] Fifth morning. Nobody at the window for a full second — the mark of a habit with no one
in it. Then, far back in the kitchen, she crosses the room without a glance at the glass and is
gone.

DIALOGUE: none.

CAMERA
[0-10.5s] All five shots: the same locked-off medium shot at eye level, wide enough to hold the
whole window, zero movement, zero reframing.

LAST FRAME
The empty window in flat grey light, nobody in the frame, the kitchen dim at the edges.

AUDIO
[0-2s] A foghorn, far off; light rain on the glass; room tone. [2-4s] A garbage truck working the
alley, off: hydraulic whine, a bin set down; no foghorn. [4-6s] A single buoy bell, slow, off the
water; her breath against the glass, close. [6-8s] Nothing at all — dead-quiet room tone.
[8-10.5s] Her footsteps crossing the room and fading. No music anywhere.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera,
slow motion, morphing objects, extra people in frame, modern branding, readable signage, no red
anywhere in frame, her face visible, camera movement, any reframing between shots, any figure in
the alley
```

### BLOC 12-B — 2 s — « Le dernier matin » *(plan 13.6 — bloc solo forcé : lieu propre)*

```
Elements @Nora + @NoraBedroom. 21:9, 1080p, 2s, sound on.
Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 50mm, f/2.
Style prompt: grey daylight from the bedroom window only, flat and colourless, deep soft shadow on
the near side of the bed, camera locked off.

SCENE
The sixth morning. She no longer goes to the window. One shot, no cut.

FRAME MAP
[0-2s] Medium close shot inside the bedroom: @Nora lying on the bed on her side at x=40%, back to
camera, facing the wall, filling 55% of frame height; deep in the background at x=75%, the window
stands empty — nobody at it, flat white day beyond.

SUBJECT LOCK, NORA
Fifteen, thin, long dark brown wavy unwashed hair, fully dressed in her oversized faded
charcoal-grey hoodie, knees drawn up on the rumpled dark quilt. Back to camera for the whole
shot; her face and her eyes are never visible.

CROSS-FRAME RULES
Single shot. She does not move: only her shoulder rises barely with her breathing, long
intervals, nothing else. Nobody appears at the window.

LOCATION
@NoraBedroom — single bed, rumpled dark quilt, cluttered desk, the window onto the back gallery.
No red anywhere.

LIGHT
Grey daylight from the bedroom window only, flat, colourless; the near side of the bed in deep
soft shadow.

MOVEMENT
[0-2s] Nothing moves but her breathing. The series of window frames has stopped, and the stopping
is the event.

DIALOGUE: none.

CAMERA
[0-2s] Medium close shot, eye level, locked off.

LAST FRAME
Her back and drawn-up knees on the bed, the empty window flat white in the background, unchanged
from the first frame.

AUDIO
No foghorn any more. Nothing. The silence is the shot — bare room tone only. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera,
slow motion, morphing objects, extra people in frame, modern branding, readable signage, no red
anywhere in frame, her face visible, her eyes visible, any movement of her body beyond breathing,
anyone at the window, camera movement
```

---

## SÉQUENCE 14 — LA BIBLIOTHÈQUE *(15 s — 1 bloc unique)*

> **Un seul bloc de 15 s, 6 segments** — 14.6 et 14.7 sont **fusionnés en un segment continu**
> (le script enchaîne déjà : l'insert du papier, puis « le cadre quitte le papier et monte à son
> visage »). Rien n'est perdu, une génération est gagnée.
> **Verrous** : le dos rouge de 14.3 **presque brun en contre-jour** (règle B) ; la main sale aux
> doigts tachés d'encre reste telle quelle — générée d'après le plan macro des mains de @Sam,
> jamais inventée ; le papier de 14.6 ne porte **aucun mot** — c'est un dessin, incrusté [POST]
> sur une feuille générée vierge (règle I). @Nora et @Mender ne partagent jamais un cadre.
> **Montage** : le panoramique de 14.3 est demandé « en retard » à la génération ; si la version
> générée ne rate pas assez le sujet, appliquer le retard de douze images au montage (script).

### BLOC 13 — 15 s — « L'apparition, la course, le papier » *(plans 14.1 → 14.7)*

```
Elements @Nora + @Mender + @LibraryCorridor. 21:9, 1080p, 15s, sound on.
Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 50mm, f/2.
Style prompt: white zenithal skylight over the tables and old fluorescent tubes over the stacks,
every other tube lit so the aisles alternate pools and shadow, cool and even, deep shelf shadows,
camera locked off except one handheld run.

SCENE
A municipal library, daytime. Nora hears the coat before she sees it, misses it by seconds, and
finds a folded drawing on her table. Six shots, hard cuts.

FRAME MAP
[0-3s] @Nora seated at the study table, right of centre x=60%, chest-up, filling 55% of frame
height; the reading room in depth behind her, empty tables; at the far counter x=85%, a librarian
seen only from behind, soft-focus, shelving books from a cart.
[3-5s] The stacks in deep enfilade, eye level, vanishing point dead centre x=50%, the bright
window at the far end; the aisle empty end to end.
[5-7.5s] The same enfilade. At the very far end, thirty metres away, tiny at x=78% and filling
barely 15% of frame height: the back of @Mender turning the corner of the last stack; one bare
hand hanging at the sleeve passes through the beam of the far tube for half a second.
[7.5-10s] @Nora from behind, waist-up, x=50%, running down the aisle, the tube lights strobing
across her shoulders; handheld.
[10-12s] The next corridor, wide, eye level, empty; at the far end x=50%, a plain grey service
door finishing its swing.
[12-15s] Extreme close-up, top-down and slightly raked: her hands and the open textbook centred,
a sheet of paper folded in four on it; then the frame climbs to a close-up of her face, centred,
filling most of frame height.

SUBJECT LOCK, NORA
Fifteen, thin, shoulders rounded inward, long dark brown wavy unwashed hair, oversized faded
charcoal-grey hoodie, dark navy parka, chapped bitten lips, large grey-green eyes with heavy lids
and grey shadowed hollows beneath. The exact face of her reference. Her face appears only in the
final shot.

SUBJECT LOCK, MENDER
A long mid-calf oilskin coat, hood up, seen strictly from behind, never any other way. In the
backlight the red of the coat is swallowed, reading almost brown, nearly black; only the ivory
lines of script catch the light and ripple as the cloth moves. One bare hand hangs at the end of
the sleeve — a large dirty hand, the fingers stained blue-black with ink to the second knuckle —
the same hand as the macro reference of @Sam's hands, never invented. No face, no profile, no
eyes, no other skin, ever.

CROSS-FRAME RULES
@Nora and @Mender never appear in the same shot: @Nora exists in shots one, four and six only;
@Mender exists in shot three only; the librarian exists in shot one only, distant, from behind.
The library is the same library in all six shots — same shelves, same worn parquet, same
skylight, same alternating tubes, green exit signage only. The coat's red never reads bright: it
stays nearly brown in backlight in its single shot. The page-rustle in shots one to three is one
continuous sound and its timbre never changes.

LOCATION
Municipal library — tall dark wooden stacks in enfilade, worn parquet, a study table with a chair
at the near end, a flat bright window at the far end, brass rail lights switched off, green exit
signage, no fire extinguisher anywhere. No readable book titles.

LIGHT
White zenithal skylight over the tables; every other fluorescent tube lit over the stacks,
alternating pools and shadow; shot three backlit by the single far tube; shot five lit by the far
tube only, the shelves between in shadow.

MOVEMENT
[0-3s] She sits over an open textbook she is not reading — her eyes are on the page but they do
not travel. Off-screen, a rustle of pages begins: regular, ample, unhurried, going on far too
long to be someone leafing through a book. Her chin lifts a few degrees; her eyes come up without
her head following. The tables around her are empty.
HARD CUT
[3-5s] The stacks in enfilade. Nothing moves — not a shadow, not a book. The rustle continues
over the stillness, then stops dead, mid-breath.
HARD CUT
[5-7.5s] At the far end of the enfilade, the back of @Mender turns the corner of the last stack
and disappears; for half a second, one bare ink-stained hand hangs in the beam of the far tube —
the only skin visible in the entire apparition. The camera pans right toward him too late — a
delayed pan that misses him, reaching the corner as it stands empty.
HARD CUT
[7.5-10s] @Nora runs. Her dark hoodie and parka pumping, hair swinging, the every-other tube
lights sweeping over her shoulders in alternating bands. Off-screen behind, a chair goes over —
sound only, never seen. She takes the corner at full speed, one hand slapping and gripping the
shelf upright to sling herself around it.
HARD CUT
[10-12s] The next corridor. Empty. The movement slams to a hard stop, then absolute stillness; at
the far end, the plain grey service door finishes its swing and closes without a sound, the last
ten centimetres of its arc, the latch never heard.
HARD CUT
[12-15s] Back at her table. Her fingers, chapped, bitten nails, take a sheet of paper folded in
four that was not there before and unfold it flat; the paper has weight and creases, the skylight
gives its folds relief; the face of the sheet is left clean — no letters, no drawing generated.
Then the frame climbs from the paper to her face, and the face changes as the frame arrives: the
flat unfocused gaze sharpens to a fixed point, her lips part a few millimetres, the held breath
lets go, and the muscles around her eyes lift for the first time in the film.

DIALOGUE: none.

CAMERA
[0-3s] Medium close-up, eye level, locked off.
[3-5s] Wide, eye level, down the enfilade, locked off.
[5-7.5s] Wide, eye level, a slow right pan that starts late and arrives after he is gone.
[7.5-10s] Waist shot from behind, HANDHELD tracking run — real shake, real breath, the frame
loose, the horizon breathing.
[10-12s] Wide, eye level; the tracking slams to a hard stop, then locked.
[12-15s] Extreme close-up, top-down on the hands, then a light ascending travel to a close-up of
her face.

LAST FRAME
@Nora's face in close-up, eyes down toward the sheet below the frame, the muscles around her eyes
lifted, white zenithal skylight even and cool on her.

AUDIO
[0-5s] The page-rustle — the exact timbre of a sheet of paper being unfolded, held a second too
long — steady and wide over library room tone, a trolley wheel far off; it cuts off clean
mid-breath at the end of shot two. [5-7.5s] The rustle of the coat receding — cloth that sounds
like pages being turned — then gone around the corner; tube hum; no footsteps audible.
[7.5-10s] Her soles hammering the carpeted parquet, her breath hard and close, the chair falling
off-screen. [10-12s] The ambience cuts off at the stop — only her ragged breathing just behind
the lens; the door makes no sound at all. [12-15s] The sheet unfolding — the same page-timbre,
held a second too long — then nothing. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera,
slow motion, morphing objects, extra people beyond the one distant librarian, modern branding,
readable signage, exit signage green only, no fire extinguisher in frame, no red anywhere in
frame except the coat read as near-brown, the coat's red reading bright, saturated or full, the
man's face, any profile, any eyes, any skin other than the one hanging hand, legible words on the
coat, the figure pausing or turning toward camera, any letters, words or drawing generated on the
paper, readable book titles, the chair falling in frame, her face visible before the final shot
```

---

## SÉQUENCE 15 — LA BUÉE *(7,5 s — 1 bloc)*

> **Règles H et I** : rien ne s'écrit en direct — le message est un film de savon déposé le matin
> même, révélé **d'un bloc** par la vapeur. Les plans miroir sont générés **vierges** ; le texte
> **TONIGHT. BUS 7. SEVENTH STOP.** est composé en post (capitales bâtonnées, cache piloté par la
> buée). Elle n'est **jamais** dans le même cadre que son reflet.

### BLOC 14 — 7,5 s — « Le miroir » *(plans 15.1 → 15.3 — [POST] texte)*

```
Elements @Nora + @Bathroom. 21:9, 1080p, 7.5s, sound on.
Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 50mm, f/2.
Style prompt: one hard halogen wall light above the mirror, its halo blooming in the shower
steam, cold tile shadows, camera locked off except one very slight push-in.

SCENE
A steamed bathroom at night. The fog reveals, in one block, a message laid in soap that morning —
the mirror is generated clean in every shot; the text exists only in post. Three shots, hard
cuts.

FRAME MAP
[0-2s] @Nora chest-up, right of centre x=60%, her back to the mirror which holds the left of
frame around x=30%, hazing at its edges — plain fog, nothing on it.
[2-5.5s] The mirror tight, filling the frame; @Nora a soft dark shape in the near foreground at
x=20%; the fog climbing the glass in a slow even tide from the bottom edge. NO letters, NO marks
generated.
[5.5-7.5s] The fogged mirror full frame — the reflection only, she is never in the same frame as
her reflection; centred x=50%, a rough wiped porthole the size of two hands; inside it, her eyes
alone.

SUBJECT LOCK, NORA
Fifteen, just out of the shower, a towel over her shoulders, hair stuck flat to her neck and
temples, movements small and automatic, eyes down. In the final shot only the reflected eyes —
@Nora's exact eyes from the reference, heavy lids, grey shadowed hollows, pupils large, not
blinking once.

CROSS-FRAME RULES
The same bathroom, the same mirror, the same single halogen in all three shots. The mirror is
generated clean in every shot — no letters, no marks: nothing writes itself, no stroke ever
appears after another. Her body and her reflection never share a frame. She never turns around.

LOCATION
@Bathroom — plain rectangular mirror above the basin, chipped enamel edge, white square tiles
with grey grout, thick shower steam. No red anywhere.

LIGHT
The single hard halogen above the mirror, white, its halo hanging in the vapour; everything
beyond falls to cold grey tile.

MOVEMENT
[0-2s] She reaches for her toothbrush on the basin edge without looking at the glass, eyes down.
Behind her the mirror begins to haze at its edges.
HARD CUT
[2-5.5s] The steam climbs the glass in a slow even tide, condensation beading and greying the
mirror; her blurred shape stays motionless in the foreground, unaware, toothbrush halted mid-air.
(In post, where the soap film was laid that morning, the message appears in one block, all at
once, at the moment the fog reaches it: TONIGHT. BUS 7. SEVENTH STOP. — stick capitals, ruled and
stencilled.)
HARD CUT
[5.5-7.5s] The reflection only: the rough porthole just wiped clear by her palm, water tracks
bleeding down from its lower edge; inside it her eyes, wide, fixed, not blinking once for the
entire shot. (The stick-capital letters stand around the porthole in the fog, composited in post,
out of focus at frame edge.)

DIALOGUE: none.

CAMERA
[0-2s] Medium close-up, eye level, locked off.
[2-5.5s] Tight on the mirror, a very slight push-in — a few centimetres over the whole shot.
[5.5-7.5s] Extreme close-up on the glass, locked off.

LAST FRAME
The fogged mirror full frame, the wiped porthole with her unblinking eyes at its centre, wet
streaks catching the hard halogen. (Les lettres [POST] autour du hublot.)

AUDIO
[0-2s] The extractor fan running, a tap dripping into the basin, steam-dulled room tone.
[2-5.5s] The low sustained drone — very low, continuous — rises under the fan; nothing else.
[5.5-7.5s] The extractor fan stops. Her breathing stops with it. Dead silence, one beat — cut to
black. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera,
slow motion, morphing objects, extra people in frame, modern branding, readable signage, no red
anywhere in frame, any letters or marks generated on the mirror, text appearing stroke by stroke,
a hand or finger writing, cursive writing, glowing or supernatural lettering, her turning around,
her body and her reflection in the same frame, a blink in the final shot
```

---

## SÉQUENCE 16 — LE DÉPART *(20 s — 6 blocs : le lieu change presque à chaque plan)*

> **Verrous** : la bague est vue **UNE fois (15-A), jamais de gros plan ensuite** — en 17.5 elle
> n'est que sentie à travers le tissu. Le sandwich est emballé avec soin : c'est son dîner — le
> même paquet reparaît en 16-A/16-B. Le bus **sans aucun rouge** : trois quarts avant, feux
> arrière et bandeaux hors champ, aucun feu de circulation, aucune bouche d'incendie ; le « 7 »
> de la girouette est **[POST]**. En 15-D, **Anna garde Milo** — au fond de la cuisine, éclairée
> chaud, elle ne lève pas les yeux ; le visage de @Sam reste perdu en contre-jour.

### BLOC 15-A — 2,5 s — « La bague » *(plan 16.1 — solo : chambre de Nora, macro)*

```
Elements @Nora (hands). 21:9, 1080p, 2.5s, sound on.
Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 85mm, f/2.
Style prompt: a single bedside lamp, low and warmthless in the grey world, a tight pool of light
on wood and velvet, everything else near-black, camera locked off.

SCENE
A keepsake box, a ring, a pocket. One shot, no cut.

FRAME MAP
[0-2.5s] Extreme close-up, macro, the small wooden box centred x=50% in the lamp's pool; her
hands entering from frame right; the right pocket of her navy parka at the lower frame edge.

SUBJECT LOCK, NORA (HANDS)
A fifteen-year-old's hands: bitten nails, chapped knuckles, the gestures small and certain, no
hesitation and no ceremony. The navy parka sleeve with its worn cuff.

CROSS-FRAME RULES
Single shot. The ring is on screen two seconds, no more, and will never be seen again in the
film. Her face never enters the frame.

LOCATION
Her bedroom at night — a small wooden keepsake box, worn velvet inside, dark wood beneath the
lamp pool. No red anywhere.

LIGHT
A single bedside lamp, the only source, low, its pool just covering the box; everything else
falls to near-black.

MOVEMENT
[0-2.5s] The box opens under her fingers; the hinge resists then gives. On the worn velvet: her
mother's ring, a thin gold band. Her hand takes it, closes over it into a fist, holds one beat —
then slips fist and ring together into the right pocket of the parka, and the flap falls.

DIALOGUE: none.

CAMERA
[0-2.5s] Extreme close-up, macro, locked off.

LAST FRAME
Her hand flat over the closed pocket flap, the open box at the edge of the lamp pool, the velvet
hollow empty.

AUDIO
The hinge of the box, the fabric of the pocket. Room tone. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera,
slow motion, morphing objects, extra people in frame, modern branding, readable signage, no red
anywhere in frame, lingering on the ring, the ring visible after it enters the pocket, her face
in frame, jewellery sparkle or glamour lighting
```

### BLOC 15-B — 3 s — « Le sandwich » *(plans 16.2 → 16.3 — @Kitchen, plan de travail)*

```
Elements @Nora (hands) + @Kitchen. 21:9, 1080p, 3s, sound on.
Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 85mm, f/2.
Style prompt: only the low lateral glow of the stove hood lamp, raking across the counter,
everything outside its throw falling to black, camera locked off.

SCENE
A sandwich made and wrapped in the dark kitchen. Two shots, hard cut.

FRAME MAP
[0-1.5s] Insert: her palm flat on a sandwich centred x=50% on the counter, the knife on the
cutting board beside it at x=70%; the hood lamp's rake from frame left.
[1.5-3s] Insert, same light: her hands folding the paper closed over the sandwich, centred
x=50%; the right pocket of the parka entering at the lower right of frame x=70%.

SUBJECT LOCK, NORA (HANDS)
The same hands as the ring shot: bitten nails, chapped knuckles, worn navy parka cuff. Careful,
deliberate, unhurried.

CROSS-FRAME RULES
Both shots are the same counter, the same hood lamp, the same hands. The ring is never visible —
only the pocket receiving the packet. The wrapping paper is plain, unprinted.

LOCATION
@Kitchen at night — the counter under the stove hood, cutting board, knife; the room beyond the
lamp's throw in darkness. No red anywhere.

LIGHT
The stove hood lamp, the only light on, very low and lateral, raking across the counter; one
warmthless pool.

MOVEMENT
[0-1.5s] Her palm presses down flat on the sandwich, compacting the bread with care, evenly,
corner to corner — the press of someone making it hold together for a journey, not someone in a
hurry.
HARD CUT
[1.5-3s] Her hands fold the paper closed over the sandwich — wrapped with care, the folds sharp
and deliberate, tucked like a parcel — then push it down into the right pocket of the parka,
against what is already there. It is her own dinner.

DIALOGUE: none.

CAMERA
[0-1.5s] Insert, close, locked off.
[1.5-3s] Insert, close, locked off.

LAST FRAME
The pocket receiving the wrapped packet, the paper catching the hood lamp's rake, the kitchen
black beyond.

AUDIO
[0-1.5s] The knife set down on the board, the soft give of the bread; the house silent around it.
[1.5-3s] The wrapping paper creasing and settling. Nothing else. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera,
slow motion, morphing objects, extra people in frame, modern branding, readable signage, no red
anywhere in frame, the ring visible, her face in frame, printed or branded wrapping paper,
overhead light on, sloppy or rushed gesture
```

### BLOC 15-C — 2 s — « Milo dort » *(plan 16.4 — solo : @KidsBedroom, depuis le seuil)*

```
Elements @Nora + @Milo + @KidsBedroom. 21:9, 1080p, 2s, sound on.
Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 50mm, f/2.
Style prompt: only the hallway sconce behind her, a warm-dulled wedge of light falling through
the door ajar onto the sleeping child, the room beyond in darkness, camera locked off.

SCENE
She stops one second at her brother's door. One shot, no cut.

FRAME MAP
[0-2s] Close shot from the threshold, the door ajar: @Milo asleep centred x=55%, small under the
amber quilt; the wedge of hallway light across him stopping halfway up the bed; @Nora's shoulder
and dark hair in silhouette at the near frame edge x=10%.

SUBJECT LOCK, MILO
Eight years old, small, thick dark hair with the cowlick standing up at the crown, mouth open,
one arm flung out. The exact face of his reference; his eyes are closed.

SUBJECT LOCK, NORA
Only her shoulder and dark hair in silhouette at frame edge; her face never visible.

CROSS-FRAME RULES
Single shot. The child never wakes or stirs beyond breathing. She does not enter the room: her
weight shifts once toward it, and back.

LOCATION
@KidsBedroom at night, seen through the door ajar — the amber quilted blanket, the room in
darkness beyond the wedge of light. No red anywhere.

LIGHT
The hallway sconce behind her, the only source: a warm-dulled wedge through the door, falling
across the bed and stopping halfway up it.

MOVEMENT
[0-2s] Nothing moves but the child's slow breathing and her single shift of weight — toward the
room, then back. She holds, one second, and does not go in.

DIALOGUE: none.

CAMERA
[0-2s] Close shot from the threshold, eye level, locked off.

LAST FRAME
The sleeping child under the wedge of light, her silhouette shoulder still at the frame edge.

AUDIO
The child's breathing, slow and even. A floorboard settles once under her weight. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera,
slow motion, morphing objects, extra people in frame, modern branding, readable signage, no red
anywhere in frame, the child waking or stirring, her entering the room, her face lit
```

### BLOC 15-D — 5 s — « La porte » *(plans 16.5 → 16.6 — un lieu : l'entrée, champ intérieur puis contre-champ extérieur de la même porte)*

```
Elements @Nora + @Sam + @Anna (entrance hall, no saved location Element). 21:9, 1080p, 5s,
sound on.
Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 50mm, f/2.
Style prompt: the entrance sconce burning BEHIND him so he stands in contre-jour with his face
lost, one warm bare-bulb glow far off from the open kitchen door, sodium seeping at the exterior
frame edges, camera locked off.

SCENE
He lets her pass; the door closes; his silhouette stays behind the frosted glass. Two shots, hard
cut — the same front door from inside, then from outside.

FRAME MAP
[0-3s] The entrance hall, night: @Nora a dark foreground shape at the frame edge x=15%, zipped
into her parka; @Sam leaning against the wall by the door at x=55%, in full contre-jour, filling
70% of frame height, his face lost; at the far end of the corridor x=85%, the kitchen door open —
@Anna small at the table, a glass of tea before her, lit warm by a single bare bulb.
[3-5s] Outside: the closed front door, the frosted pane filling most of the frame, centred
x=50%; behind the glass, his blurred silhouette — heavy shoulders, head slightly bowed.

SUBJECT LOCK, SAM
A heavy silhouette: the bulk of the olive canvas work jacket, the outline of the unkempt greying
beard, shoulders slumped, head carried low. His face is never readable, in either shot — a mass,
not a man.

SUBJECT LOCK, NORA
Fifteen, navy parka zipped, dark hair; a dark foreground shape, her face never lit.

SUBJECT LOCK, ANNA
Seventy-eight, short and heavy-set, thin white hair in a low bun, pale floral housecoat, thick
brown cardigan. She sits at the kitchen table far in the depth, and she does not look up, not
once. The exact figure of her reference.

CROSS-FRAME RULES
The silhouette behind the frosted glass in shot two is the same man from shot one — same heavy
shoulders, same bowed head, same jacket bulk. He asks nothing; she says nothing; nobody touches
anybody. He steps aside ten centimetres — exactly enough to let her pass — and no more. Anna
never looks up. Three people, three distances, in shot one only.

LOCATION
The entrance hall of the flat and the street side of its front door — a frosted-glass pane, a
narrow corridor to the open kitchen door at the far end. No red anywhere.

LIGHT
Shot one: the entrance sconce behind him (full contre-jour), the warm bare bulb of the kitchen
far off, everything between in shadow. Shot two: the sconce glowing through the frosted glass,
sodium orange from the street touching the doorframe at the frame edges.

MOVEMENT
[0-3s] He leans by the door as if he has been waiting a while. She comes to it. He steps aside
ten centimetres to let her pass. Deep in the background, Anna sits unmoving over her tea. Nothing
is said.
HARD CUT
[3-5s] The door is closed. Behind the frosted glass his silhouette stays exactly where it was,
motionless, one full beat too long. Then it thins, greys, and fades back into the depth of the
hall as he steps away, the sconce light closing over where he stood.

DIALOGUE: none.

CAMERA
[0-3s] Medium shot, eye level, locked off.
[3-5s] Tight shot on the door, eye level, locked off.

LAST FRAME
The frosted pane empty of him, the sconce a soft mass of light behind it, sodium orange at the
frame edges, rain flecking the glass.

AUDIO
[0-3s] The latch of the front door under her hand, their two breathings — his slower, hers
shallower; nothing said. [3-5s] The street side: rain on the porch roof, the sodium lamp's faint
buzz. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera,
slow motion, morphing objects, extra people in frame, modern branding, readable signage, no red
anywhere in frame, the man's face readable or lit, his features readable through the glass, Anna
looking up, any word spoken, an embrace or a touch, the door reopening, the silhouette waving or
pressing to the glass
```

### BLOC 15-E — 3 s — « Le bus traverse » *(plan 16.7 — solo : rue de nuit, [POST] girouette)*

```
Elements: night street set, no saved Element. 21:9, 1080p, 3s, sound on.
Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 50mm, f/2.
Style prompt: the bus's own yellow interior neons and one sodium lamp as the only sources, their
smears sliding across wet asphalt, a constant lateral tracking, no shake.

SCENE
An empty night bus crosses the frame. One shot, no cut.

FRAME MAP
[0-3s] Wide, the bus crossing the frame seen three-quarter FRONT, never from behind, filling 60%
of frame height, its lit windows a band of yellow; the wet empty street lower third; the
destination blind above the windscreen glowing blank.

SUBJECT LOCK, BUS
An empty city night bus, three-quarter front at all times: no tail lights ever in field, no red
strip or banner anywhere on it, every seat visible and empty, the driver a dark shape. The
destination blind blank and unreadable in generation — the number 7 is composited in post.

CROSS-FRAME RULES
Single shot. No other vehicle, no pedestrian, no lit shopfront. The camera speed is locked to the
bus.

LOCATION
A wet empty street in the port town at night — cracked asphalt holding the light in long smears,
fine rain through the sodium cone. No traffic light, no fire hydrant. No red anywhere.

LIGHT
The bus's yellow interior neons and one sodium street lamp, the only sources; their reflections
dragged long on the wet asphalt.

MOVEMENT
[0-3s] The bus crosses the frame at constant speed, wipers working, its light sliding under it on
the wet road; the camera tracks laterally with it, locked to its pace.

DIALOGUE: none.

CAMERA
[0-3s] Wide shot, eye level, constant lateral tracking at the bus's speed, no shake.

LAST FRAME
The bus exiting the frame edge, still three-quarter front, its yellow band smearing on the wet
asphalt, the blind blank.

AUDIO
The diesel, an axle squealing on the joint, the wipers' rubber beat. Rain. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera,
slow motion, morphing objects, extra people in frame, modern branding, readable signage, no red
anywhere in frame, no tail lights, no red banners or strips on the bus, no traffic light, no fire
hydrant, a readable route number or destination generated in-model, passengers visible, the bus
seen from the rear
```

### BLOC 15-F — 4,5 s — « Septième arrêt » *(plans 16.8 → 16.9 — @NightBus)*

```
Elements @Nora + @NightBus. 21:9, 1080p, 4.5s, sound on.
Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 50mm, f/2.
Style prompt: cold white ceiling strip light from above, sodium passing through the condensation
windows in slow washes, deep black beyond the glass, camera locked off inside the bus.

SCENE
She counts the stops on her fingers, then steps out into total black. Two shots, hard cut.

FRAME MAP
[0-2.5s] Insert, shallow focus: her hand flat on her jeans-clad thigh, centred x=50%; the bus's
destination/stop display band in soft-focus amorce at the top corner x=85%, an unreadable smear
of light.
[2.5-4.5s] Waist shot from behind: @Nora standing in the aisle at x=50%, one hand on the chrome
pole, facing the doors which fill the frame ahead — folding open onto total black: no lamp, no
building, no horizon.

SUBJECT LOCK, NORA
Fifteen, navy parka with the broken zip pull, worn sleeve cuff, bitten nails, long dark brown
hair. Her face never enters the frame.

CROSS-FRAME RULES
Both shots are the same bus: same cold ceiling strips, same condensation on the glass, same
grey-blue seats, no other passengers ever. The camera never leaves the bus. No red anywhere
inside: no stop-button lights, no red handrails.

LOCATION
@NightBus rolling — worn moulded seats, chrome poles, condensation on the windows, black night
beyond the glass. No red anywhere.

LIGHT
Cold white ceiling strips inside; sodium washes sliding through the windows as lamps pass;
nothing at all beyond the open doors.

MOVEMENT
[0-2.5s] Her hand lies flat on her thigh. One finger folds down. Then a second. Then the third —
counting stops, the knuckles whitening slightly at each fold.
HARD CUT
[2.5-4.5s] She is already standing, hand on the pole. The doors fold open onto pure black — a
hole. She steps down and out of the bus's light, swallowed to a silhouette in two steps. The
camera stays inside; the bus pulls away, carrying its light with it and leaving her out there.

DIALOGUE: none.

CAMERA
[0-2.5s] Insert, close, shallow focus, locked off.
[2.5-4.5s] Waist shot from behind, eye level, locked off inside the bus — the bus itself carries
the point of view away.

LAST FRAME
From inside the pulling-away bus: the doors folded shut on black glass, her silhouette already
lost outside, the cold ceiling strips reflected in the wet pane.

AUDIO
[0-2.5s] The stop-request chime — three times, each one closer — over the diesel drone and the
tyre hiss on wet road. [2.5-4.5s] The pneumatic doors, her step down onto gravel, then the engine
gathering and receding, taking its own sound and light with it. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera,
slow motion, morphing objects, extra people in frame, modern branding, readable signage, no red
anywhere in frame, no stop-button lights, no red handrails, the display band in focus or
readable, her face in frame, other passengers, any light source outside the doors, the camera
leaving the bus
```

---

## SÉQUENCE 17 — L'ABRIBUS *(27,5 s — 2 blocs, même lieu : @BusShelter)*

> **RÈGLE D, verrouillée trois fois par bloc** : dans **chaque segment** où @SamSDF apparaît, le
> FRAME MAP impose le cadre **coupé à hauteur de bouche**, les CROSS-FRAME RULES répètent que ses
> yeux ne sont **jamais** visibles, et le NEGATIVE l'interdit en toutes lettres (*the man's eyes
> visible, the man's full face in frame*). Dans les valeurs larges (17.1, 17.11), c'est la poutre
> du toit de l'abribus + le bord du cadre qui coupent. **Ses trois répliques sont timecodées à
> l'identique du découpage** (0,5–2 s dans 17.4 et 17.8 ; 0,5–3 s dans 17.10), reportées sur la
> timeline du bloc. Le caisson publicitaire reste **vide, blanc laiteux, sans image ni lettrage**.
> Voix : celle de @Sam baissée d'une tierce, rauque de froid — même comédien, aucun traitement.
> La bague n'est que **sentie** en 17.5 ; le sandwich est le paquet du bloc 15-B.

### BLOC 16-A — 14 s — « L'approche et le don » *(plans 17.1 → 17.6)*

```
Elements @Nora + @SamSDF + @BusShelter. 21:9, 1080p, 14s, sound on.
Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 50mm, f/2.
Style prompt: the shelter's tired fluorescent tube buzzing over the bench and the sodium cone
above holding the wet road, everything outside them near-black, wet asphalt carrying the
reflections, camera locked off except one lateral tracking.

SCENE
Nora crosses to the homeless man at the bus shelter and holds out her sandwich. Six shots, hard
cuts.

FRAME MAP
[0-3s] Wide, eye level from across the road: @SamSDF seated on the bench inside the shelter at
x=65%, motionless, CROPPED BY THE FRAME AND THE SHELTER'S ROOF BEAM AT MOUTH HEIGHT so no eyes
are ever visible; the blank milky-white advertising light box beside the bench at x=80%, carrying
no image and no lettering; @Nora at x=30%, filling 25% of frame height, a pure silhouette at the
edge of the dark.
[3-5.5s] Medium close-up on @Nora at x=50% at the dark edge of the road, her phone low, its glow
lighting her from below.
[5.5-8s] Waist shot, three-quarter rear, @Nora at x=45% crossing the wet road; the shelter and
the seated shape growing at the right frame edge, HIS HEAD ABOVE THE MOUTH NEVER ENTERING THE
FRAME.
[8-10.5s] Close-up on @SamSDF at x=50%, THE FRAME CUT HARD AT MOUTH HEIGHT — hood, matted grey
beard, chapped lips, and nothing else. His eyes are never visible.
[10.5-12s] Insert on the right pocket of @Nora's navy parka at x=55%, two metres from the bench.
[12-14s] Insert: the wrapped sandwich extended into the neon at the exact centre x=50%; beyond
it, soft-focus at frame edge, the dark banked shape of @SamSDF on the bench, NOTHING OF HIM ABOVE
THE MOUTH IN FRAME.

SUBJECT LOCK, SAMSDF
A heavy man living rough: stretched dark grey wool beanie pulled low, hood up over it, the full
matted grey beard — his real beard, dirtied and windblown, no false beard — wind-cracked lips,
layered flannels under a torn olive parka, blankets banked over his knees. Moth-eaten grey wool
fingerless mitts, the backs of the hands black with quay grease and dust, the nails rimmed with
grime. HE IS CROPPED AT MOUTH HEIGHT IN EVERY FRAME HE APPEARS IN; HIS EYES ARE NEVER VISIBLE,
NOT ONCE.

SUBJECT LOCK, NORA
Fifteen, thin, navy parka with the broken zip pull, oversized charcoal hoodie beneath, long dark
brown unwashed hair, chapped bitten lips, large grey-green eyes with heavy lids and shadowed
hollows. The exact face of her reference.

CROSS-FRAME RULES
The only two people at the shelter are @Nora and @SamSDF. @SamSDF is the same man in every shot
he appears in — same beanie, same hood, same beard, same blankets — and the frame never rises
above his mouth: his eyes are never visible in any shot. The shelter is the same shelter in all
six shots: same bench, same tube, same blank milky light box. In shot one there is light on him
and none on her. The ring is never visible — only its shape through the cloth, once, in shot
five. The sandwich in shot six is the carefully wrapped packet, its folds still sharp.

LOCATION
@BusShelter — a steel and glass shelter at the far edge of the port town at night, one bench, a
blank white advertising light box with no image and no lettering, a leaning timetable pole, a wet
empty road, chain-link fence and a dark warehouse behind, ground mist at ankle height. No traffic
light, no hydrant. No red anywhere.

LIGHT
The shelter's tired fluorescent tube on him and on the milky light box; the sodium cone above
holding the wet road; her phone's glow from below in shot two — the only source of that shot;
everything else near-black.

MOVEMENT
[0-3s] Nobody moves for the whole shot. He sits banked in his blankets under the flickering tube;
she stands stock-still at the edge of the dark. The distance between them is the subject of the
shot.
HARD CUT
[3-5.5s] She checks the count of stops on her phone, the screen angled away, its content never
readable — a plain rectangle of cold glow lighting her from below. Then she lifts her head toward
the man across the road, and the under-light drops off her eyes as she raises them into the dark.
Her breath fogs through the glow.
HARD CUT
[5.5-8s] SHE is the one who crosses; the first step is hers. She steps off the kerb, hands in her
parka pockets, her pace even — not slow, not hurried: decided. With each step the neon takes more
of her — the shoulder of the parka, the hair, the pale edge of her cheek — while the dark she
came from closes behind. Her reflection walks under her on the asphalt.
HARD CUT
[8-10.5s] He does not lift his head. He speaks first — the lips move inside the beard, unhurried,
his breath steaming through the neon on each word. The wool of the hood is beaded with mist.
HARD CUT
[10.5-12s] Her hand slides into the pocket — and stops. Under the fabric her fingers pass over
the ring; the small hard shape rolls once beneath them, printed for an instant against the nylon.
She feels it. She leaves it there. The hand shifts deeper, past it.
HARD CUT
[12-14s] The hand comes back out with the carefully wrapped sandwich — the folds still sharp —
and extends it across the space between them, into the neon, and holds it there, steady, at the
exact centre of frame. The packet is the brightest thing in the shot. Her hand does not waver.

DIALOGUE
[8.5-10s] @SamSDF, a broken voice, rough with cold — Sam's voice dropped a third, same actor, no
processing: "Got anything to eat, miss?"

CAMERA
[0-3s] Wide shot, eye level from across the road, locked off.
[3-5.5s] Medium close-up, eye level, locked off.
[5.5-8s] Waist shot, three-quarter rear, lateral tracking at her walking pace, no shake.
[8-10.5s] Close-up, eye level, locked off — the frame cut hard at mouth height.
[10.5-12s] Insert, close, locked off.
[12-14s] Insert, close, shallow focus, locked off.

LAST FRAME
The wrapped packet held steady at the exact centre of the neon, her sleeve beaded with mist, the
dark banked shape of the man beyond it — nothing of him above the mouth in frame.

AUDIO
[0-3s] The tube's buzz and flicker-tick, a foghorn far off, water dripping from the sheet-metal
roof onto asphalt. [3-5.5s] Her visible breath — slow in, held, out; the tube faint across the
road. [5.5-8s] Her steps, one landing flat in a puddle, the buzz rising as she nears. [8-10.5s]
His voice, low and rasped, the tube under it. [10.5-12s] Fabric — the nylon shifting, the small
roll of something hard inside it. [12-14s] The paper's single crease as her grip shifts; the
tube; the drip from the roof. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera,
slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red
in frame, no traffic light, no hydrant, the man's eyes visible, the man's full face in frame, any
part of his face above the mouth, the frame drifting upward on him, a false or glued-on beard
look, lettering or image on the light box, light on Nora in the first shot, a readable phone
screen or interface, the ring visible, printed or branded wrapping, her hand trembling
```

### BLOC 16-B — 13,5 s — « Le repas, la direction, le départ » *(plans 17.7 → 17.11)*

```
Elements @Nora + @SamSDF + @BusShelter. 21:9, 1080p, 13.5s, sound on.
Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 50mm, f/2.
Style prompt: the tube above and behind him so the neon touches only lips, chin, hands and the
pointing arm, deep blacks holding everything else, the street beyond pure black, camera locked
off.

SCENE
He eats slowly, says what people say, points up the hill, and does not watch her go. Five shots,
hard cuts.

FRAME MAP
[0-2.5s] Close-up: his hands and the paper fill the frame, THE MOUTH AT THE VERY TOP EDGE — never
higher; the wrapped paper open on the blanket over his knees.
[2.5-5s] Close-up on @SamSDF at x=50%, THE FRAME CUT AT MOUTH HEIGHT — the identical value and
crop as the "miss" shot: hood, beard, lips, nothing else; the blank milky light box at the frame
edge x=85%. His eyes are never visible.
[5-7s] Close-up on @Nora at x=50%, the neon full on her face for the first time; the black road
behind her.
[7-11s] Medium waist shot of @SamSDF on the bench at x=45% — EVEN HERE THE HEAD IS CUT BY THE
FRAME AT MOUTH HEIGHT; his arm rises and crosses the whole frame toward the dark hill at frame
right; the light box blank and milky beside him.
[11-13.5s] General shot on a very long focal from up the road, perspective compressed flat:
@Nora walking away at x=40%, diminishing into the ground mist; @SamSDF small and centred in his
cone of light at x=60%, CROPPED AT MOUTH HEIGHT BY THE SHELTER'S ROOF BEAM AND THE FRAME.

SUBJECT LOCK, SAMSDF
Same lock as the previous block: beanie, hood, the real matted grey beard, layered flannels, torn
olive parka, blankets; moth-eaten grey wool fingerless mitts, backs of the hands black with quay
grease, nails rimmed with grime — nothing legible in all that dirt, the dark fingertips reading
as more of it. HE IS CROPPED AT MOUTH HEIGHT IN EVERY FRAME HE APPEARS IN; HIS EYES ARE NEVER
VISIBLE, NOT ONCE.

SUBJECT LOCK, NORA
Fifteen, navy parka, charcoal hoodie, long dark unwashed hair, chapped bitten lips, mist beading
in her hair at the temples. The exact face of her reference.

CROSS-FRAME RULES
The only two people at the shelter are @Nora and @SamSDF. @SamSDF is the same man in every shot —
same beanie, same hood, same beard, same mitts, same blankets — and the frame never rises above
his mouth: his eyes are never visible in any shot. The shelter is the same shelter in all five
shots: same bench, same tube, same blank milky light box. He and she never share a frame except
the final wide. He never watches her go: the hooded head stays bowed toward the road at his feet.
The sandwich is the same wrapped packet throughout, half-eaten by the final shot.

LOCATION
@BusShelter — the same steel and glass shelter, bench, blank white advertising light box with no
image and no lettering, wet empty road, chain-link fence and dark warehouse behind, ground mist.
The road climbing away behind is pure black. No traffic light, no hydrant. No red anywhere.

LIGHT
The tube above and behind him: neon on the lower lip and chin, on the hands, on the raised arm —
and full on her face in her shot, hard and unflattering from above; everything else deep black.
No light ever appears up the hill.

MOVEMENT
[0-2.5s] He takes the sandwich, unwraps it without hurry, and eats slowly, without greed, the way
you make a thing last — small bites, long pauses, the jaw working under the beard at the top of
frame. The steam of his breath and of the bread crosses the neon beam with each exhale.
HARD CUT
[2.5-5s] He speaks around the food, quietly, not looking up — a half-swallowed observation, not a
complaint; the lips barely open, the words dropped rather than offered. A crumb sits in the
beard. The steam of the words crosses the neon.
HARD CUT
[5-7s] She waits for a question. He does not ask one. The waiting is in the body: her weight
rocks forward onto the balls of her feet a centimetre, her lips part to answer something — and
nothing comes to answer; the parted lips close again slowly. Her eyes stay down toward the bench,
off-frame.
HARD CUT
[7-11s] He lifts his chin toward the road that climbs away into the mist, and his arm comes up
and crosses the whole frame in one line — the frayed mitt, the grease-black back of the hand, the
finger held out toward the dark of the hill — and stays there, extended, while he speaks. When
the line is said, the arm comes down and he goes back to eating, the packet retrieved from his
knee, as if nothing had been given.
HARD CUT
[11-13.5s] She walks away from the shelter into the ground mist and diminishes — parka, then
hair, then a grey outline, sinking into the black up the hill. He stays on the bench, the
half-eaten sandwich resting on his knee, and he does not watch her go. The two reflections
separate on the wet asphalt until only his remains.

DIALOGUE
[3-4.5s] @SamSDF, chewing, quiet: "Most people say no."
[7.5-10s] @SamSDF, flat, certain: "Straight up the hill. When you see the red, you're there."

CAMERA
[0-2.5s] Close-up on the hands, eye level, locked off — the mouth at the very top edge of frame.
[2.5-5s] Close-up, eye level, locked off — the frame cut at mouth height.
[5-7s] Close-up, eye level, a very slight push-in — a few centimetres across the whole shot.
[7-11s] Medium waist shot, eye level, locked off — the head cut at mouth height even now.
[11-13.5s] General shot, very long lens character, compressed flat, locked off.

LAST FRAME
The shelter a neon island in total black: @SamSDF small and bowed under the tube, cropped at
mouth height by the roof beam, the half-eaten sandwich on his knee, the blank milky light box
glowing beside him — only his reflection left on the wet asphalt.

AUDIO
[0-2.5s] The paper, the slow chewing, the mist dripping from the shelter roof. [2.5-5s] His
voice, low; the foghorn answers from the water, one long note; the tube. [5-7s] Nothing — the
buzz and the drip have fallen away; near-silence, her held breath. [7-11s] His voice; then the
paper again and the slow chewing; the tube. [11-13.5s] Her steps decreasing up the hill until the
mist takes them; the tube's buzz remains — it is the last sound. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera,
slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red
in frame — the word "red" is spoken, never shown, the man's eyes visible, the man's full face in
frame, any face above the mouth, the frame drifting upward, clean hands, wolfing or hurried
eating, self-pity played in the voice direction, lettering or image on the light box, the man
turning his head to follow her, any light up the hill, her speaking, tears
```

---

## [POST] — hors blocs (composés au montage, jamais générés)

| Où | Quoi | Règle |
|---|---|---|
| Bloc 13, segment [12-15s] (plan 14.6) | Le dessin à l'encre sur le papier déplié : le même dos, le même manteau, **neuvième technique — AUCUN mot, aucune lettre**. Incrusté sur la feuille générée vierge. | I |
| Bloc 14, segments [2-5.5s] et [5.5-7.5s] (plans 15.2–15.3) | **TONIGHT. BUS 7. SEVENTH STOP.** en capitales bâtonnées tracées à la règle et au pochoir, apparition **d'un bloc** via un cache piloté par la buée ; autour du hublot en 15.3. Miroir généré vierge dans les deux segments. | H + I |
| Bloc 15-E (plan 16.7) | Le **« 7 »** de la girouette du bus — la girouette est générée vierge et illisible. | Texte à l'écran |

**Notes de montage** —
- Bloc 13, segment 14.3 : le retard du panoramique est demandé à la génération ; sinon,
  **retarder de douze images au montage** (script).
- Durées : couper chaque bloc à sa durée de script (blocs générés à la seconde supérieure ou au
  minimum du moteur — voir Vue d'ensemble).
- Son signature : le bruissement de pages (bloc 13) doit garder **exactement le timbre du papier
  déplié en 9.6** — caler au mixage si la génération s'en écarte.
- Voix du SDF (blocs 16-A/16-B) : dérivée de celle de @Sam — registre baissé d'une tierce,
  souffle rauque de froid, débit ralenti ; **même comédien, aucun traitement qui altère le
  grain** (règle F).
