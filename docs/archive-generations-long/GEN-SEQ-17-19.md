# THE MENDER — Générations · SÉQUENCES 18 à 19

> Source de vérité : `docs/SCRIPT-THE-MENDER.md` (préambule + séq. 18-19 + notes de production),
> matière première : `docs/plans/PLANS-SEQ-17-19.md` (49 plans), gabarits et @tags :
> `docs/PROMPT-PACK-THE-MENDER.md`. Méthode : niveau 4 du pack *5 Levels of AI Video Prompting*
> (SCENE / FRAME MAP / SUBJECT LOCK / CROSS-FRAME RULES / LOCATION / LIGHT / MOVEMENT avec
> HARD CUT / DIALOGUE timecodé / CAMERA par segment / LAST FRAME / AUDIO / NEGATIVE), enrichi
> niveau 5 (@tags sauvegardés en Éléments + réglages Cinema Studio réels).
> **UNE génération = PLUSIEURS plans avec HARD CUT timecodés**, sauf les segments chaînés
> (orbite, retrait) qui sont chacun UNE prise continue sans coupe interne.

## En-tête de production

**23 blocs de génération · 126 s d'écran couverts (séq. 18 = 35 s · séq. 19 = 56 s · séq. 20 = 35 s)**
dont **117,5 s générées** par les 23 blocs et **8,5 s hors blocs** (20.3 reprise du fichier 7.7a : 2,5 s ·
20.12 noir : 2 s · 20.13 carton titre [POST] : 4 s).

**Réglages** (pack §3, conventions du découpage) : séq. 18 = Genre **Drama**, Anamorphic **28mm f/1.4** ;
séq. 19-19 = Genre **Noir**, Anamorphic **50mm f/2** (85mm sur les blocs de gros plans — un seul objectif
par génération : les dérogations locales sont notées dans le bloc). Partout : Style Manual · Camera
**Fine Film** · 21:9 · 1080p · sound on.

**Négatif commun** (à recopier en tête de chaque NEGATIVE PROMPT) : *visible camera rigs, cartoonish
colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in
frame, modern branding, readable signage.*

**Marquages** : **[POST]** = composé au montage, jamais généré · **[REPRISE DE FICHIER]** = aucune
génération, réutilisation d'un fichier existant · **[INVERSÉ AU MONTAGE]** = généré à l'endroit,
joué à l'envers · **[ÉDITION D'IMAGE]** = plate unique déclinée par édition puis animée.

### Table bloc → plans

| Bloc | Plans couverts | Durée | Cuts internes | Notes |
|---|---|---|---|---|
| **G1** | 18.1 · 18.2 · 18.3+18.4 · 18.5 · 18.6 | 13 s | 4 HARD CUT (18.3→18.4 continu, volet noir du chambranle) | approche + entrée + murs |
| **G2** | 18.7 · 18.8 · 18.9 · 18.10 · 18.11 | 11 s | 4 HARD CUT | arrêt du faisceau ([POST] artwork) + chute |
| **G3** | 18.12 | 3 s | aucun — orbite 1/4 | gabarit pack §4 tel quel |
| **G4** | 18.13 | 3 s | aucun — orbite 2/4 | idem |
| **G5** | 18.14 | 3 s | aucun — orbite 3/4 | idem |
| **G6** | 18.15 | 2 s | aucun — orbite 4/4 | idem |
| **G7** | 19.1 | 3 s | aucun — retrait 1/5 | départ sur la dernière image de G6 |
| **G8** | 19.2 | 2 s | aucun — retrait 2/5 | volet noir du chambranle |
| **G9** | 19.3 | 3 s | aucun — retrait 3/5 | lampadaire en bord cadre |
| **G10** | 19.4 | 3,5 s | aucun — retrait 4/5 | **[INVERSÉ AU MONTAGE]** — aucune pluie |
| **G11** | 19.5 | 2,5 s | aucun — retrait 5/5 | **[INVERSÉ AU MONTAGE]** — aucune pluie |
| **G12** | 19.6 → 19.12 | 14,5 s | 6 HARD CUT | le démasquage ; 12 images de 17.6 [REPRISE DE FICHIER] en tête |
| **G13** | 19.a + 19.h | 4 s | 1 HARD CUT | même décor @Shed ; broderie [POST] hors bloc |
| **G14** | 19.b | 2,5 s | aucun | @AnnaKitchen plein jour |
| **G15** | 19.c | 3,5 s | 1 HARD CUT | @Restaurant ; dialogue timecodé |
| **G16** | 19.d | 5 s | 4 HARD CUT (5×1 s) | @LibraryCorridor ; RÈGLE D verrouillée |
| **G17** | 19.e | 2,5 s | aucun | @Bathroom plein jour |
| **G18** | 19.f | 2,5 s | aucun | bureau nuit ; écran forum [POST] hors bloc |
| **G19** | 19.g | 4,5 s | 5 états [ÉDITION D'IMAGE] + 1 gén. finale | plate unique ; artwork [POST] hors bloc |
| **G20** | 19.i | 3 s | aucun | POV capuche ; vignette [POST] hors bloc |
| **G21** | 20.1 + 20.2 + 20.9 + 20.10 | 11,5 s | 3 HARD CUT | même décor @BusShelter — monté en deux temps |
| **G22** | 20.4 → 20.8 | 13 s | 4 HARD CUT | l'hôpital ENFIN SONORE ; dialogue timecodé (RÈGLE A) |
| **G23** | 20.11 | 2 s | aucun | image-à-vidéo sur le cadre référent 4.1 |

**Hors blocs (aucune génération)** : 20.3 (fichier 7.7a tel quel, fondu d'entrée 12 images [POST]) ·
20.12 (noir pur) · 20.13 (carton THE MENDER [POST]). **Incrustations [POST] rattachées aux blocs** :
artwork loup/montagne/oiseau (G2 sur 18.8, G19 sur 19.g — l'artwork unique de 4.3/4.4/4.5) · broderie
GIVE AND YOU SHALL RECEIVE (G13 sur 19.a) · contenu d'écran du forum (G18 sur 19.f) · vignette de
capuche (G20 sur 19.i) · 12 images du fichier 17.6 en tête de G12.

**Rappels opposables sur tout le fichier** : RÈGLE B (séq. 18 = premier et seul rouge plein cadre du
film ; en 18-19 aucun rouge hors manteau/fil) · RÈGLE D (jamais le visage du Mender ; manteau et
visage de Sam jamais dans le même cadre) · RÈGLE F0 (la barbe du SDF est la VRAIE barbe de @Sam —
aucun postiche, elle ne s'enlève pas) · RÈGLE H (aucun surnaturel) · RÈGLE I (capitales bâtonnées au
pochoir, jamais lisibles) · RÈGLE A (le mot *stories* n'existe qu'en 20.6, bloc G22).

---

## SÉQUENCE 18 — LA MAISON ROUGE *(35 s · 6 blocs : G1, G2, G3-G6)*
*Premier et seul rouge plein cadre du film. La torche de Nora est la source unique à partir de 18.2.*

### G1 — L'APPROCHE ET L'ENTRÉE *(plans 18.1 → 18.6 · 13 s · 5 segments, 4 hard cuts)*

**Elements:** @Nora + @RedHouseExterior + @RedHouseInterior
**Settings:** Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic 28mm f/1.4 · 21:9 · 1080p · 13s · sound on
**Style prompt (EN):** One sodium lamp far behind the camera, then a phone torch as the single source of everything; where the beam lands, saturated barn red is born out of brown-black night; deep crushed shadows, extremely shallow depth of field.

**SCENE**
A girl reaches a boarded red cottage at night, brings the only light, pushes the door and enters a room covered in writing. Five shots along one continuous approach, hard cuts (the cut into the interior is hidden by the door jamb wiping the lens black).

**FRAME MAP**
[0-3s] The cottage at x=50%, filling 60% of frame height, very wide shot, low angle. Front door open ten centimetres. No light inside. Nobody in frame. The façade reads brown-black — its red not yet revealed.
[3-5s] @Nora three-quarter rear at x=30%, filling 45% of frame height, raises her phone; the torch beam lands on the clapboard and **inside the beam the boards ignite into deep saturated barn red**; everything outside the beam stays brown-black.
[5-8.5s] Medium shot from directly behind @Nora, waist-up, the red door filling the frame ahead. She pushes it, it gives heavy on its hinges; the camera pushes with her, **the dark door jamb sweeps the lens as a full black wipe (~6.5s)**, then the interior opens from the threshold: bare wooden floor, a single chair, a table with an unlit paraffin lamp, walls dimly sensed under layered paper — nothing readable, everything at the edge of darkness. Her shoulder and raised torch at frame edge.
[8.5-11s] Torch-POV, wide including the ceiling: the narrow beam sweeps walls, staircase, ceiling beams — every surface covered edge to edge in dense hand-stencilled block capitals in ivory paint and ink, layered over years, on plaster and hundreds of overlapping pinned sheets. **The sweep is fast — up to 90 degrees per second — with true motion blur: no line is ever legible, the writing reads only as streaks and texture.**
[11-13s] Extreme close-up of the written wall: the torch held ten centimetres from the surface **overexposes the paper — the stencilled capitals bloom and burn into shapeless blotches of light and ink**; the focal plane drifts and never resolves. Paper fibres, pin heads, layered sheet edges in relief.

**SUBJECT LOCK, @NORA**
Fifteen, the exact face and wardrobe of her reference: charcoal hoodie, navy parka, off-white canvas sneakers, no red anywhere on her. Phone held up as a torch. Seen from behind or three-quarter rear only — her face never visible in this block.

**CROSS-FRAME RULES**
The same cottage and the same street in every shot. From [3s] on, the torch is the single light source of every frame. The only red anywhere is what the torch beam lights. No light ever comes from inside the house on its own. The stencilled writing is never legible in any frame of any shot. Nobody but @Nora appears.

**LOCATION**
Shots one to three: the dead end of a rough climbing street between two grey warehouse walls — @RedHouseExterior, an old boarded fisherman's net store, clapboard painted with red-lead primer thirty years ago, peeling, sagging picket fence, weeds at the kerb, cracked asphalt, ground mist. Shots three (after the wipe) to five: @RedHouseInterior, the single downstairs room.

**LIGHT**
[0-3s] one sodium street lamp fifty metres behind the camera — it only cuts the mist; the façade reads brown-black. [3-13s] the phone torch, single source: saturated barn red inside the beam, hard black outside; at ten centimetres it burns the paper to white.

**MOVEMENT**
[0-3s] Slow forward dolly at eye level, constant, perfectly steady, toward the cottage. The door stands ajar.
HARD CUT
[3-5s] Camera locked off. @Nora raises the phone; the beam trembles very slightly with her hand — **the red is born in the frame.**
HARD CUT
[5-8.5s] One continuous push: she pushes the swollen door, the jamb wipes the lens black, the interior opens from the threshold as she steps in.
HARD CUT
[8.5-11s] Handheld torch-POV sweep across walls, staircase and ceiling — too fast to read.
HARD CUT
[11-13s] Handheld float at the wall, focus hunting and never landing, the beam burning the paper.

**DIALOGUE** — (aucun)

**CAMERA**
[0-3s] Very wide, low angle, slow forward dolly, eye level, no shake. [3-5s] Wide, locked off. [5-8.5s] Medium from behind, forward dolly through the doorway. [8.5-11s] Handheld POV pan, ≤90°/s, real motion blur — one of the film's three handheld moments. [11-13s] Extreme close-up, handheld drift, f/1.4 razor-thin focus.

**LAST FRAME**
The overexposed written wall filling the frame: blooming blotches of light and ink on red, nothing legible, black at the edges.

**AUDIO**
[0-3s] The wind drops dead — an abnormal total hush — then the low sustained sub-bass drone fades in and holds. [3-5s] The drone rises a step; her breath, close. [5-8.5s] Swollen wood scraping the frame, the hinges, the larger echo of the empty room. [8.5-11s] Her breathing accelerating, very close. [11-13s] Paper crackling faintly, her breath. No music anywhere in the block.

**NEGATIVE PROMPT**
visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, legible handwriting, readable words, letters that form real words, cursive writing, Nora's face visible, any light inside the house other than the torch, any second light source, rain, red visible outside the torch beam, a locked-in sharp focus on the text.

*⚠ Notes FR : le rouge NE NAÎT PAS en 18.1 — il naît au segment 2 avec la torche (« c'est elle qui
apporte la lumière qui révèle les raisons »). RÈGLE I : l'illisibilité est un fait optique (vitesse,
surexposition, f/1.4), pas une consigne à l'image. 18.3→18.4 n'est pas un hard cut : c'est le même
mouvement, coupe masquée par le noir du chambranle — le prompt le décrit comme UNE poussée continue.*

---

### G2 — LES TROIS FIGURES ET LA CHUTE *(plans 18.7 → 18.11 · 11 s · 5 segments, 4 hard cuts)*

**Elements:** @Nora + @RedHouseInterior *(+ artwork loup/montagne/oiseau [POST])*
**Settings:** Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic 28mm f/1.4 · 21:9 · 1080p · 11s · sound on
**Style prompt (EN):** Torch-only light inside a room written edge to edge; raking beam, ink faintly gleaming, then the beam at rest; finally the fallen torch firing the ceiling so the whole room bathes in indirect red.

**SCENE**
The sweeping beam steadies on one patch of wall; the girl's face takes the red for the first time; her legs give and she lies on her back under a written ceiling. Five shots, hard cuts.

**FRAME MAP**
[0-1.5s] Two fast insert sweeps across other blocks of stencilled writing: the torch rakes almost parallel to the wall, ink lines catching a faint wet gleam, embossed paper layers throwing long micro-shadows — streaks, never words.
[1.5-5.5s] Medium-close on the wall: the beam glides across the streaking capitals, slows, and **stops** on a clear patch of plaster at x=50%, trembling minutely with the wrist, then makes three small deliberate pauses left to right across the patch, as if resting on three marks in turn. The writing around the patch stays soft and unreadable; the patch itself is evenly lit, in focus, visually calm.
[2-5.5s → cadre] *(même segment)* the patch centred, the surrounding wall dissolving at f/1.4.
[5.5-7.5s] Close-up on @Nora, off-frame gaze at the wall: **the rebound of her torch off the red wall washes her face in soft red light — the first red ever to touch her skin.** Her eyes go from scanning to still; a small involuntary smile arrives without her permission; then her gaze releases and slides past.
[7.5-9s] Wide shot, gentle high angle: in the middle of the bare floor her legs give — **not a collapse: a letting-go** — she folds down slowly through her knees onto the boards, phone in hand, her whole figure small at x=50%. The camera eases down with her.
[9-11s] Wide high angle, locked off: she lies on her back, arms loose, the phone fallen beside her at x=60%, **its beam pointing up at the writing-covered ceiling — the entire room bathes in warm indirect red**, the stencilled walls dissolving into out-of-focus red-and-ivory texture.

**SUBJECT LOCK, @NORA**
Exact reference face: fifteen, chapped lips, shadowed hollows under large grey-green eyes. Charcoal hoodie, navy parka. No tears in this block; no knowing expression — something moves in her that she does not understand.

**CROSS-FRAME RULES**
The same written room in all five shots; the torch is the only source in every frame. The writing is never legible in any frame. The clear patch of shot two is left EMPTY at generation — no drawing, no figure ever generated on it. The only red on her skin is bounced red light.

**LOCATION**
@RedHouseInterior, the single downstairs room, floor to ceiling in stencilled block capitals on plaster and layered pinned paper.

**LIGHT**
The phone torch only: raking and grazing in shot one; stable and even on the patch in shot two; bounced soft red off the wall onto her face in shot three; a swinging pool during the fall; then the fallen torch firing the ceiling — indirect red bathing the whole room.

**MOVEMENT**
[0-1.5s] Two whip lateral sweeps, handheld.
HARD CUT
[1.5-5.5s] The pan slows, settles, stops; the wrist trembles; three small pauses left to right.
HARD CUT
[5.5-7.5s] Camera locked off on her face; only her eyes and mouth move.
HARD CUT
[7.5-9s] Gentle descent with her as she folds down.
HARD CUT
[9-11s] Locked-off high angle; only her breathing moves.

**DIALOGUE** — (aucun)

**CAMERA**
[0-1.5s] Inserts, handheld, fast lateral. [1.5-5.5s] Medium-close, handheld settling to stillness. [5.5-7.5s] Close-up, locked off. [7.5-9s] Wide, gentle high angle, smooth descent. [9-11s] Wide, high angle, locked off.

**LAST FRAME**
@Nora full figure on her back on bare boards, phone beside her, beam up at the ceiling, the whole room in warm indirect red — the saturated heart of the film's only red sequence.

**AUDIO**
[0-1.5s] A loose shutter banging outside, once, twice; the drone holds. [1.5-5.5s] **The low drone stops dead. Silence.** Room tone and one held breath. [5.5-7.5s] Nothing. One single breath. [7.5-9s] The floorboards taking her weight, cloth, the phone knocking wood. [9-11s] Her breath, unsteady. No music anywhere in the block.

**NEGATIVE PROMPT**
visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, legible handwriting, readable words, letters that form real words, any generated animal drawing, any generated figure on the wall, tears, a knowing expression, a violent fall, sharp background, any second light source.

*⚠ Notes FR : [POST] — LES TROIS FIGURES (UN LOUP, UNE MONTAGNE, UN OISEAU) sont l'artwork unique du
film (le même que 4.3/4.4/4.5 et 19.g), incrusté en post sur la zone calme du segment 2, calé sur les
trois pauses du faisceau. Ne JAMAIS laisser le modèle les dessiner. Segment 3 : le spectateur, lui, a
reconnu la séquence 4 — elle, non. RÈGLE B : premier rouge sur sa peau, uniquement en lumière rebondie.*

---

### G3 → G6 — L'ORBITE *(plans 18.12 → 18.15 · 3+3+3+2 = 11 s · 4 segments chaînés SANS coupe interne)*

*Gabarit du pack §4 (« SÉQ 18 — LA MAISON ROUGE, l'orbite ») repris tel quel, un bloc par segment,
durées du découpage. Mouvement continu 9°/s, objectif à 6 cm du sol, même formulation d'orbite,
même ouverture dans les quatre prompts. **La dernière image de chaque segment est la première du
suivant** (image-à-vidéo). Raccords masqués par : le faisceau qui traverse l'objectif (1→2), un
battement de paupières — yeux fermés = images identiques (2→3), un souffle qui déplace une mèche
(3→4). Doctrine : une prise n'a pas de couture.*

#### G3 — Orbite, segment 1/4 *(plan 18.12 · 3 s)*
```
Elements @Nora + @RedHouseInterior. 21:9, 1080p, 3s, sound on.
Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 28mm, f/1.4.
Style prompt: one torch lying on the floor is the only source, deep saturated warm red filling
the whole frame, extremely shallow depth of field, the written walls dissolving into streaks of
ink, camera at floor level, slow and continuous.

@Nora lies on the floor of @RedHouseInterior, laughing, relieved. Close-up at floor level around
her head, left profile turning toward three-quarter.
Slow orbit around her, 9 degrees per second, lens 6 cm above the floor, one continuous move.
@Nora stays sharp, the written walls behind her stay far out of focus and read only as streaks.
The writing is never legible in any frame. The torch on the floor rakes her with warm red-amber
from below.
Segment 1 of 4. The last frame of this segment is the first frame of the next; identical move,
identical speed, identical aperture. At the very end of the segment the torch beam crosses the
lens and flares it.
LAST FRAME: her head in three-quarter, the lens flared by the beam crossing it.
AUDIO: her breath breaking into laughter, the warm room tone, nothing else. The evenings theme
returns — solo piano, very far away.
NEGATIVE PROMPT: legible handwriting, readable words, on-screen text, any face other than hers,
sharp background, handheld shake, cuts inside the segment, visible camera rigs, cartoonish
colors, subject looking at camera, slow motion, morphing objects, extra people in frame
```

#### G4 — Orbite, segment 2/4 *(plan 18.13 · 3 s)*
```
Elements @Nora + @RedHouseInterior. 21:9, 1080p, 3s, sound on.
Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 28mm, f/1.4.
Style prompt: same single floor-level torch glow, the red of the floorboards climbing onto her
face from below, whole frame saturated red, razor-thin focus.

Continuation, starting on the exact last frame of segment 1 (the lens flare of the beam
clearing). Three-quarter turning to full face.
Slow orbit around her, 9 degrees per second, lens 6 cm above the floor, one continuous move.
Her laugh breaks into a sob mid-segment; her chest hitches. The torch on the floor lights her
from below and the red of the floorboards rises onto her face — it will not leave her again
until the cut to black. Walls remain pure out-of-focus streaks of ink.
Segment 2 of 4. The last frame of this segment is the first frame of the next; identical move,
identical speed, identical aperture. At the very end her eyes close in a blink.
LAST FRAME: full face, eyes closed mid-blink.
AUDIO: the sob surfacing through the laugh. The solo piano theme, very far. Nothing else.
NEGATIVE PROMPT: legible handwriting, readable words, on-screen text, any face other than hers,
sharp background, handheld shake, cuts inside the segment, visible camera rigs, cartoonish
colors, subject looking at camera, slow motion, morphing objects, extra people in frame
```

#### G5 — Orbite, segment 3/4 *(plan 18.14 · 3 s)*
```
Elements @Nora + @RedHouseInterior. 21:9, 1080p, 3s, sound on.
Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 28mm, f/1.4.
Style prompt: same source, same red bath from below, the orbit unbroken, her face carrying
laughter and tears in the same breath.

Continuation, starting on the exact closed-eyes frame that ended segment 2; her eyes reopen.
Full face turning to three-quarter right.
Slow orbit around her, 9 degrees per second, lens 6 cm above the floor, one continuous move.
She is crying and laughing at once — tears running back toward her ears while the corners of
her mouth lift: relief, not grief. The red floor-bounce holds on her skin. Background:
continuous streaks of ivory on red, nothing legible.
Segment 3 of 4. The last frame of this segment is the first frame of the next; identical move,
identical speed, identical aperture. At the very end a breath of air moves a strand of hair
across her eye.
LAST FRAME: three-quarter right, the strand of hair across her eye.
AUDIO: the solo piano alone. Her breath between laugh and cry.
NEGATIVE PROMPT: legible handwriting, readable words, on-screen text, any face other than hers,
sharp background, handheld shake, cuts inside the segment, visible camera rigs, cartoonish
colors, subject looking at camera, slow motion, morphing objects, extra people in frame
```

#### G6 — Orbite, segment 4/4 *(plan 18.15 · 2 s)*
```
Elements @Nora + @RedHouseInterior. 21:9, 1080p, 2s, sound on.
Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 28mm, f/1.4.
Style prompt: same floor-level torch light; the orbit decelerates and comes to rest — the
stillness that seeds the pull-back of 19.1.

Continuation, starting on the exact last frame of segment 3 (the strand of hair settling).
Three-quarter right easing back toward profile — and the orbit decelerates smoothly and stops
completely, holding on her profile at rest. Her breathing settles into one long exhale.
Slow orbit around her, 9 degrees per second, lens 6 cm above the floor, decelerating to a full
stop. She stays sharp; the red walls stay streaks.
Segment 4 of 4. The final motionless frame must be clean and stable: it is the launch frame of
the reverse travelling of 19.1 (bloc G7).
LAST FRAME: her profile at rest, camera motionless — the exact start frame of G7.
AUDIO: one long exhale. The solo piano theme continues underneath, very far.
NEGATIVE PROMPT: legible handwriting, readable words, on-screen text, any face other than hers,
sharp background, handheld shake, cuts inside the segment, camera drift after the stop, visible
camera rigs, cartoonish colors, subject looking at camera, slow motion, morphing objects, extra
people in frame
```

*⚠ « C'est le seul endroit du film où la salle a le droit de craquer — avant le twist, et sans rien
savoir. »*

---

## SÉQUENCE 19 — LE RETRAIT ET LA RÉVÉLATION *(56 s · 14 blocs : G7-G11 retrait, G12 démasquage, G13-G20 montage)*

### G7 → G11 — LE RETRAIT-REMBOBINAGE *(plans 19.1 → 19.5 · 3+2+3+3,5+2,5 = 14 s · 5 segments chaînés SANS coupe interne)*

*Vitesse de recul verrouillée : **1,2 m/s constante, sans accélération, dans les cinq prompts.**
Raccords masqués : volet noir du chambranle (G7→G8), lampadaires en bord cadre (G9→G10, G10→G11).
**G10 et G11 sont générés À L'ENDROIT (caméra qui avance) puis INVERSÉS au montage** : lampadaires
qui s'éteignent dans le mauvais sens, phares à reculons, feuille qui remonte, Nora à reculons —
tout vient gratuitement. **Aucune pluie dans ces deux segments — brume au sol uniquement** (une
pluie inversée monterait et détruirait l'effet). Côté son, n'inverser que la corne de brume et le
grésillement ; le thème se redresse sans passer par l'inversion — le son suit la manipulation du
temps, comme la rampe du pack (« Car, a time ramp with the sound following it »).*

#### G7 — Retrait, segment 1/5 *(plan 19.1 · 3 s)*

**Elements:** @Nora + @RedHouseInterior · **Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** The floor torch receding, warm red shrinking to a pool in a growing darkness, a perfectly constant backward dolly with zero acceleration.

**SCENE / MOVEMENT** — one continuous shot, no cut. *(Image-à-vidéo : démarrer sur la dernière image de G6.)* Interior night. From floor level beside @Nora's face, **the camera pulls straight back at a locked constant 1.2 metres per second, no acceleration, no easing** — from close-up to wide. It leaves her and crosses @RedHouseInterior in reverse: her lit figure and the fallen torch shrink into a warm red island; the streaked written walls slide past out of focus; the darkness widens around the frame. She does not move; her quiet laughter stays behind with her.
**LOCATION / LIGHT** — @RedHouseInterior; the fallen torch, only source, receding.
**DIALOGUE** — (aucun)
**CAMERA** — backward dolly, floor level rising gently to eye level, locked speed, no shake.
**LAST FRAME** — wide: her small lit figure a red island in darkness, the doorway edge entering the frame.
**AUDIO** — the piano theme continues; her laughter recedes with the distance.
**NEGATIVE PROMPT** — visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, legible handwriting, readable words, speed changes, camera shake, any cut inside the segment.

#### G8 — Retrait, segment 2/5 *(plan 19.2 · 2 s)*

**Elements:** @Nora + @RedHouseInterior · **Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · 2s · sound on
**Style prompt (EN):** The door jamb sweeps the lens as a black wipe on a constant backward dolly, interior red giving way to exterior night.

**SCENE / MOVEMENT** — one continuous shot, no cut. Continuation of the pull-back, same locked 1.2 m/s. The camera reverses through the doorway — **the dark door jamb wipes across the lens as a full black shutter** — and comes out onto the night porch. Inside, deep in the frame, the tiny warm red pool with @Nora on the floor; around it the door frame, then the peeling red clapboard catching the last spill of torchlight. Ground mist, no rain.
**LOCATION / LIGHT** — threshold of @RedHouseInterior → porch of @RedHouseExterior; torch spill inside, night outside.
**DIALOGUE** — (aucun)
**CAMERA** — backward dolly through the doorway, locked speed.
**LAST FRAME** — the porch and doorway centred, the red pool deep inside, night around.
**AUDIO** — the wind returns as the door plane is crossed; the piano theme still under, thinning.
**NEGATIVE PROMPT** — visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, legible handwriting, readable words, rain, speed changes, camera shake.
*⚠ La coupe G7→G8 est masquée par le volet noir du chambranle.*

#### G9 — Retrait, segment 3/5 *(plan 19.3 · 3 s)*

**Elements:** @RedHouseExterior · **Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** Sodium takes back the night as the red house shrinks; constant backward dolly down the empty street, mist at the ground, crushed blacks.

**SCENE / MOVEMENT** — one continuous shot, no cut. The pull-back continues at the same locked 1.2 m/s down the rough street: **@RedHouseExterior shrinks in the frame**, its lit doorway a fading warm point between the grey warehouse walls. The sodium lamp far down the street takes over; the red drains back toward brown-black with distance. Cracked asphalt, ground mist only, no rain, nobody in frame. **A street lamp passes at the very edge of frame near the end of the segment.**
**LOCATION / LIGHT** — the climbing street; sodium dominant, the house a fading warm point.
**DIALOGUE** — (aucun)
**CAMERA** — backward dolly, eye level, locked speed.
**LAST FRAME** — the house small up the street, a street lamp entering the frame edge (masque du raccord vers G10).
**AUDIO** — **the theme dies here. No more music until 19.g (bloc G19).** Wind, the far foghorn, the receding house.
**NEGATIVE PROMPT** — visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, rain, people, red anywhere except the shrinking house, speed changes, camera shake.

#### G10 — Retrait, segment 4/5 *(plan 19.4 · 3,5 s · [INVERSÉ AU MONTAGE])*

**Elements:** @Nora + @RedHouseExterior (la rue) · **Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · 3.5s · sound on
**Style prompt (EN):** Sodium night street, ground mist only, constant-speed dolly, ordinary physical events staged cleanly so that reverse playback reads as time flowing backwards.

**SCENE / MOVEMENT** — one continuous shot, no cut. *(À GÉNÉRER À L'ENDROIT — le prompt décrit la prise avant inversion.)* Night, wide shot. The camera dollies **forward** up the climbing street toward the red house at a locked constant 1.2 m/s, eye level, perfectly steady. As it advances: **the sodium street lamps come on one after another as it passes them; a car's headlights cross a side street in normal forward motion; a single leaf detaches from a branch and falls to the ground.** Midway, @Nora enters past the camera from behind it and walks normally away down the street, shrinking, exiting the frame mid-street. **Ground mist only — absolutely no rain, no falling drops, no drips.** Exact face and wardrobe of her reference.
**LOCATION / LIGHT** — the street between the warehouses; sodium lamps, density staged for inversion.
**DIALOGUE** — (aucun)
**CAMERA** — forward dolly, eye level, locked 1.2 m/s (reads as the same backward speed once reversed).
**LAST FRAME** *(généré, avant inversion)* — the camera high up the street, lamps lit behind it; **une fois inversé, c'est la PREMIÈRE image à l'écran — elle doit raccorder au bord-cadre lampadaire de G9.**
**AUDIO** *(après inversion)* — the foghorn and the neon buzz played in reverse, very low. No music. No footstep sync required — the street swallows detail.
**NEGATIVE PROMPT** — visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, **rain, falling rain, dripping water**, red anywhere, speed changes, camera shake.
*⚠ [INVERSÉ AU MONTAGE] — à l'envers : lampadaires qui s'éteignent dans le mauvais sens, phares à
reculons, feuille qui remonte vers la branche, et NORA qui entre à reculons, monte la rue à l'envers
et sort derrière la caméra. « C'est le seul repère qui dise, sans un mot, que le temps recule. »*

#### G11 — Retrait, segment 5/5 *(plan 19.5 · 2,5 s · [INVERSÉ AU MONTAGE])*

**Elements:** @BusShelter (la rue, la camionnette) · **Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · 2.5s · sound on
**Style prompt (EN):** Same sodium night, ground mist only, the dolly starting gently from rest so its reversed self decelerates into the shelter.

**SCENE / MOVEMENT** — one continuous shot, no cut. *(À GÉNÉRER À L'ENDROIT.)* Night, wide shot near @BusShelter at the foot of the street. The camera starts from rest, eases up to the constant 1.2 m/s forward dolly up the street. As it moves off, **a battered old flatbed van parked at the kerb pulls out and drives away forward down the street**, its headlights sweeping once. Ground mist only, no rain, nobody in frame, the shelter's blank white light box at frame edge.
**LOCATION / LIGHT** — the foot of the street at @BusShelter; sodium, the shelter tube at frame edge.
**DIALOGUE** — (aucun)
**CAMERA** — forward dolly from rest (reversed: the backward travelling decelerates into the shelter).
**LAST FRAME** *(généré, avant inversion)* — mid-street, the van gone; **inversé, la fin à l'écran est l'arrêt du travelling devant l'abribus — l'amorce de 19.6 (G12).**
**AUDIO** *(après inversion)* — the engine sound reversed, righting itself to forward at the very end of the shot. No music. *(N'inverser que corne de brume et grésillement — notes de production §2.3.)*
**NEGATIVE PROMPT** — visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, **rain, falling rain**, red anywhere, lettering on the light box, traffic light, hydrant, camera shake.
*⚠ [INVERSÉ AU MONTAGE] — à l'envers : la camionnette remonte la rue à reculons et se range ; le
travelling arrière ralentit à l'approche de l'abribus.*

---

### G12 — LE DÉMASQUAGE *(plans 19.6 → 19.12 · 14,5 s · 7 segments, 6 hard cuts — le pivot du film)*

**Elements:** @Nora + @SamSDF + @Sam + @BusShelter *(+ 12 images du fichier 17.6 [REPRISE DE FICHIER] en tête, au montage)*
**Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic 85mm f/2 · 21:9 · 1080p · 14.5s · sound on
*(Dérogation locale : 19.6 et 19.7 étaient prévus au 50mm — le bloc entier passe au 85 pour l'unité
de la génération ; la caméra recule d'autant sur le plan large, compression assumée.)*
**Style prompt (EN):** The hard orange sodium cone of the shelter tube, wet asphalt holding the reflection, deep crushed blacks all around, camera completely still in every shot; a face the light does not forgive.

**SCENE**
A homeless man watches nothing as the girl walks away; behind the shelter, the still-warm van; then he takes the disguise off piece by piece — beanie, grime, mittens — and the frame finally rises to the face. Seven shots, hard cuts. No music at any point.

**FRAME MAP**
[0-1.5s] Wide from across the road: @BusShelter under its buzzing tube, @SamSDF seated on the bench inside at x=55%, motionless, **cropped by the frame at mouth height so his eyes are never visible**, the half-eaten sandwich in his hands. @Nora already walking away up the road, back to camera, small at x=70%, dissolving into the ground mist at the edge of the sodium cone. The blank light box unlit and empty. He does not watch her go. *(Au montage, les 12 premières images sont remplacées par la reprise exacte du cadre de 17.6 — les mains, le sandwich tendu — depuis le fichier existant.)*
[1.5-3s] Static insert, the alley behind the shelter: **the old flatbed van from the quay parked nose against the wall**, twenty metres away, off the road @Nora took. Sodium grazes its dented bonnet; faint heat shimmer. Nothing moves. No readable plates.
[3-5s] Medium close-up, three-quarter rear: **two hands rise and pull the stretched grey wool beanie off.** Beneath it the matted grey-brown curls are plastered flat, **soaked with sweat despite the cold** — faint steam lifts off the scalp into the backlight. The face stays turned away, never shown. The beanie drops to his knee.
[5-7.5s] Extreme close-up, the jawline in pure silhouette against the tube's hard backlight: **a grey cloth wipes the grime away, temple to cheek, stroke after stroke; clean skin reappears in bands beneath the grey film. The full unkempt grey beard stays exactly where it is — it is his own beard, real, rooted; nothing lifts, nothing peels.** The hand works low in the frame; the face itself remains out of frame above.
[7.5-10s] Extreme close-up on the hands, the tube light full on them: the hands lay the cloth on the knees, **pull off the fingerless wool mittens.** A thumb-back wipes across the blanket: **the grease comes off the backs of the hands — but on the index and middle fingers the dark blue-black ink stays, worked into the skin down to the second knuckle and under the nails.** Large, cracked, calloused hands — the exact hands of the @Sam reference macro.
[10-12s] Close-up on hands and mouth, the frame still cut below the eyes: the ink-stained hands pick the half-eaten sandwich up from the knee, part the paper with the fingertips. He bites. He chews, slow, the real grey beard moving with the jaw. **Then the chewing stops — mid-motion, held.** The paper trembles once, barely.
[12-14.5s] One slow vertical pan, rising from the ink-stained hands holding the sandwich, up the layered filthy clothes, to the face. **IT IS @Sam — the father.** The real grey beard, the swollen hooded pale grey-blue eyes, the heavy slack cheeks, bands of clean skin where the cloth passed, grime still at the hairline. He does not cry. **He allows himself nothing.** The tube above flickers once. His gaze is on the road where she disappeared, off-frame.

**SUBJECT LOCK, @SamSDF → @Sam**
One and the same man on the same bench for the whole runtime — the disguised @SamSDF of the reference becoming the bare @Sam of the reference as beanie, grime and mittens come off. **The beard NEVER moves, never lifts, never peels: it is his real beard (RÈGLE F0).** The eyes and the full face are never visible before the final segment. The face in the final segment must match the master reference derived from shot 8.3 exactly — no reinvention.

**SUBJECT LOCK, @NORA**
Appears ONLY in shot one, back to camera, small, walking away — exact wardrobe of her reference; her face never visible.

**CROSS-FRAME RULES**
@BusShelter is the same shelter in every shot: same bench, same tube, same blank light box. The hands in shots three to seven are the same hands. No coat anywhere in any frame. No red anywhere. Nobody but @SamSDF/@Sam and, in shot one only, @Nora. The frame stays below the eyes in every shot until the final pan.

**LOCATION**
@BusShelter at the far edge of the port town, night; the alley behind it for shot two.

**LIGHT**
The buzzing sodium tube of the shelter: hard orange cone from above, backlight for the silhouettes, full frontal on the hands; everything outside the cone near-black; wet asphalt reflections; ground mist.

**MOVEMENT**
[0-1.5s] Camera locked off across the road; only @Nora moves, receding.
HARD CUT
[1.5-3s] Static insert; nothing moves but heat shimmer.
HARD CUT
[3-5s] Locked off; the beanie comes off.
HARD CUT
[5-7.5s] Locked off; the cloth works, stroke after stroke.
HARD CUT
[7.5-10s] Locked off; mittens off, thumb-wipe, the ink stays.
HARD CUT
[10-12s] Locked off; bite, chew, stop.
HARD CUT
[12-14.5s] Slow vertical pan, hands → face. Nothing else moves.

**DIALOGUE** — (aucun)

**CAMERA**
[0-1.5s] Wide (long-lens, from across the road), locked off. [1.5-3s] Insert, locked off. [3-5s] Medium close-up, three-quarter rear, locked off. [5-7.5s] Extreme close-up in silhouette, locked off. [7.5-10s] Extreme close-up macro on hands, locked off. [10-12s] Close-up hands and mouth, locked off. [12-14.5s] Slow vertical pan up to the face.

**LAST FRAME**
@Sam's face frontal under the flickering tube — first frontal frame of him since sequence 11 — eyes on the dark road off-frame, dry, bands of clean skin in the grime, the real grey beard. No tears.

**AUDIO**
[0-1.5s] **The sound snaps back to forward motion with one audible breath of air.** The sandwich paper. The tube buzzing. [1.5-3s] The bonnet metal ticks as it cools. Twice. Wind. [3-5s] The wool dragging over hair; his breathing changes register — deeper, freed. [5-7.5s] The dry cloth on skin, repeated — **this sound carries the shot.** [7.5-10s] **Nothing. Total silence under the shot.** [10-12s] The paper, the chewing, then the chewing stopping — a small silence with the tube buzz behind it. [12-14.5s] The tube buzz alone. **The music does not enter.** No music anywhere in the block.

**NEGATIVE PROMPT**
visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, **a fake beard, a beard lifting or peeling away, any adhesive edge, the beard coming off**, his eyes visible before the final vertical pan, the coat anywhere in frame, any red, rain, readable number plate, lettering on the light box, tears, a new face differing from the reference, the beanie back on, clean fingertips, ink wiping away.

*⚠ Notes FR : « Le spectateur est reposé au même instant, pas à un autre » (19.6) — d'où les 12
images de 17.6 en tête, au montage. « Il a doublé le bus » (19.7) — information entièrement
visuelle. « Le spectateur comprend une demi-seconde avant de voir le visage » (19.10) — les doigts
tachés AVANT le visage, l'ordre est le twist. RÈGLE F0 : le bloc modèle « SÉQ 19 » du pack §4,
antérieur à la règle, montrait la barbe qui se détache — il est caduc sur ce point, le script fait
foi. Le manteau et le visage de Sam ne cohabitent JAMAIS (RÈGLE D) : le manteau n'existe pas dans ce
bloc. 19.12 : visage généré depuis la référence issue de 8.3, jamais créé à ce moment-là.*

---

### LE MONTAGE 19.a → 19.i *(27,5 s · 8 blocs G13-G20, groupés par décor · ordre du film rétabli au montage · AUCUNE MUSIQUE JUSQU'À 19.g)*

### G13 — LE HANGAR : L'AIGUILLE ET LE DÉGUISEMENT *(plans 19.a + 19.h · 4 s · 2 segments, 1 hard cut — même décor @Shed)*

**Elements:** @Mender (le manteau) + @Sam (mains, barbe) + @Shed *(+ broderie [POST] hors bloc)*
**Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic 85mm f/2 · 21:9 · 1080p · 4s · sound on
**Style prompt (EN):** One articulated bench lamp and one hanging inspection lamp over a dockside workbench, hard pools and black edges, macro shallow focus, thread and grime made legible as texture.

**SCENE**
On the same workbench: the coat being sewn, and the disguise being built. Two shots, hard cut. *(Deux fragments non contigus du film — 19.a ouvre le montage, 19.h le referme presque ; l'ordre est rétabli au montage.)*

**FRAME MAP**
[0-2.5s] Extreme macro on the bench: **a mender's needle pierces up through heavy red oilskin canvas from below**, draws ivory thread through, again, again — the exact hand, point and rhythm of the net-mending of sequences 3 and 7. Then a slight pan along the inside of the coat's collar: a line of dense stitching in **red thread on the red inner face**, freshly worked, the raking lamp making the thread relief legible as texture only. The stitching is abstract at generation — no readable letters.
[2.5-4s] Static insert on the bench under the hanging inspection lamp. Laid out: **the stretched grey beanie, a grey cloth, the moth-eaten fingerless wool mittens.** Two large hands dirty themselves deliberately — **grease worked onto the BACKS of the hands, never onto the fingertips, where the blue-black ink stays clean-edged.** Then one hand roughs up its own grey beard in a shard of mirror propped against a tin — **the shard shows jaw and beard only, never the whole face.**

**SUBJECT LOCK**
The hands are the exact hands of the @Sam reference macro: large, cracked, calloused, index and middle fingers ink-stained to the second knuckle. No face anywhere in the block — the mirror shard frames jaw and beard only.

**CROSS-FRAME RULES**
The same workbench, the same shed in both shots. The coat appears ONLY in shot one; no coat in shot two. No face in any frame (RÈGLE D). The beard in the shard is the real beard of the reference.

**LOCATION** — @Shed, the cluttered dockside repair shed at night.

**LIGHT** — [0-2.5s] the articulated bench lamp, raking, so the embroidered relief catches. [2.5-4s] the single hanging inspection lamp, hard pools, black edges.

**MOVEMENT**
[0-2.5s] Fixed macro, then a slight pan along the collar.
HARD CUT
[2.5-4s] Static insert; only the hands work.

**DIALOGUE** — (aucun)

**CAMERA** — [0-2.5s] extreme macro, shallow. [2.5-4s] insert, locked off.

**LAST FRAME** — the mirror shard with jaw and roughed beard, the disguise laid out on the bench around it.

**AUDIO** — [0-2.5s] the thread pulled through waxed canvas — **the same sound as the net on the quay, sequence 7** — the tin roof faint in the wind ; *au mixage : fragment 19.a SANS musique (avant 19.g)*. [2.5-4s] the wind in the tin roof ; *au mixage : fragment 19.h porte le thème, au loin (après 19.g)*.

**NEGATIVE PROMPT**
visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, legible letters at generation, cursive writing, any face, the coat and a face in the same frame, the coat in the second shot, a fake beard on the bench, a wig, grease on the fingertips, the full face in the mirror shard, any red outside the coat.

*⚠ [POST] hors bloc : la phrase cousue au fil rouge dans le col — GIVE AND YOU SHALL RECEIVE — est
incrustée en post (aucun texte généré). Seul le spectateur la verra. RÈGLE B : le manteau est l'un
des quatre porteurs du rouge. 19.h : on salit le dos des mains, jamais les pulpes — l'encre doit
rester lisible en 19.10 (bloc G12).*

---

### G14 — LA CUISINE D'ANNA : LE PACTE *(plan 19.b · 2,5 s · 1 prise)*

**Elements:** @Anna + @Sam + @AnnaKitchen (variante plein jour)
**Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · 2.5s · sound on
**Style prompt (EN):** Flat grey daylight from the lace window plus the low stove glow, a locked medium shot where a pact is sealed with a nod.

**SCENE / MOVEMENT** — one shot, locked off. Interior day. @Anna and @Sam sit either side of the small oilcloth table of @AnnaKitchen, grey daylight through the lace curtain, the stove low. **A single sheet of paper lies between them** — what she will have to say about the visitor, nothing else. Anna sets her finger on one line, lifts her eyes to him, and nods once. **On the dresser behind them, a framed photograph of an eleven-year-old boy** — a generated child, no real person, softly readable.
**SUBJECT LOCK** — both have the exact faces of their references (@Anna : 78 ans, chignon, robe d'intérieur sauge ; @Sam : l'homme du présent, barbe grise mi-longue, doigts tachés). No coat anywhere.
**LOCATION / LIGHT** — @AnnaKitchen en plein jour : fenêtre à dentelle + poêle bas, ambre tenu.
**DIALOGUE** — (aucun)
**CAMERA** — medium shot, locked off.
**LAST FRAME** — Anna mid-nod, her finger on the line, Sam across the table, the boy's photograph behind them.
**AUDIO** — muffled voices, unintelligible; the clock; the stove ticking. No music.
**NEGATIVE PROMPT** — visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, readable words on the sheet, any red, saturated embers, full flame in frame, the coat in frame.
*⚠ « Le chagrin d'Anna est réel. Seul le visiteur est inventé. » La photo encadrée contredit
localement la plate (« photos tournées ») : c'est voulu, uniquement dans ce plan.*

---

### G15 — LE RESTAURANT : LA RÉPÉTITION *(plan 19.c · 3,5 s · 2 segments, 1 hard cut · dialogue timecodé)*

**Elements:** @Mei + @Asha + @Fatiha + @Sam + @Restaurant
**Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · 3.5s · sound on
**Style prompt (EN):** All the ugly service fluorescents on in the closed restaurant, chairs up on tables, rehearsal warmth inside a cold light.

**SCENE**
The closed restaurant, the three women rehearsing, the author correcting a name he invented. Two shots, hard cut.

**FRAME MAP**
[0-1.5s] Wide shot of @Restaurant closed: chairs upturned on the tables, the fish tank dark, **every service fluorescent on, flat and ugly**. At a cleared table, @Mei, @Asha and @Fatiha seen three-quarter from behind, **rehearsing** — one of them stumbles on a word, all three burst out laughing, and they start again.
[1.5-3.5s] Medium close-up by the register: @Sam, a handwritten list in his ink-stained hand (paper angled so nothing reads), **correcting the pronunciation of a name he invented**, under his breath.

**SUBJECT LOCK** — the women's exact reference faces where visible; @Sam exact reference, ink-stained fingers on the list.
**CROSS-FRAME RULES** — same closed room, same fluorescents in both shots; no customers; no red anywhere in the room.
**LOCATION / LIGHT** — @Restaurant fermé, néons de service, laids, tous allumés.

**MOVEMENT**
[0-1.5s] Fixed wide; the women rehearse, laugh, restart.
HARD CUT
[1.5-3.5s] Slight lateral travel toward him at the register.

**DIALOGUE**
[2-3s] @Sam, under his breath, almost inaudible: "Msi-mu-li-zi."

**CAMERA** — [0-1.5s] wide, locked off. [1.5-3.5s] medium close-up, light lateral travel.
**LAST FRAME** — @Sam at the register, list in hand, lips just closing on the last syllable.
**AUDIO** — their laughter across the room; his voice, barely voiced — **the author pronounces, once, the word he built.** No music.
**NEGATIVE PROMPT** — visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, readable words on the list, red lanterns, red tablecloths, red menus, red packaging, the coat in frame, customers.
*⚠ RÈGLE F : le « mot isolé » de Sam au présent — l'une de ses deux seules prises de parole hors
capuche. Même comédien, même timbre que l'acte I, aucun traitement.*

---

### G16 — LA BIBLIOTHÈQUE : CINQ COUPES *(plan 19.d · 5 s · 5 segments de 1 s, 4 hard cuts)*

**Elements:** @Librarian + @Mender + @Sam + @LibraryCorridor
**Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · 5s · sound on
**Style prompt (EN):** Every-other shelf fluorescent, a lightless closet, the skylight over one empty table — five hard cuts, one second each, nothing explained twice.

**SCENE**
How the library delivery was done. Five shots of one second each, hard cuts, all inside @LibraryCorridor and its service spaces.

**FRAME MAP / MOVEMENT**
[0-1s] Medium close: **@Librarian** (same woman as 14.1) nods once and unlocks a service door with a key ring.
HARD CUT
[1-2s] The broom closet, no light source, a blade of light under the door: **a man pulls the long red coat on in the dark — pure shape, no face, no skin readable.**
HARD CUT
[2-3s] Wide down the shelf corridor: the writing-covered red back crosses between the stacks and is gone — the reference back of @Mender, hood up.
HARD CUT
[3-4s] **Close-up framed on closed eyes only:** @Sam crouched on the far side of a stack, hand flat on his sternum, counting his own breath — **the rolled coat pressed against his belly stays entirely below frame, never visible in this shot.**
HARD CUT
[4-5s] Insert: a man's hand in a grey wool sleeve — **no coat on him any more** — lays a paper folded in four on the open textbook of an empty study table without breaking stride.

**SUBJECT LOCK** — @Librarian : identité n°11 des notes de production, même figure que 14.1 (tag à créer si absent). @Mender : le dos de la référence, capuche relevée, jamais de visage. @Sam : les yeux fermés seuls (coupe 4), la main et la manche grise (coupe 5).
**CROSS-FRAME RULES** — same library in all five shots. **The coat and Sam's face NEVER cohabit in any frame (RÈGLE D)** : coupe 2 = forme pure sans peau ; coupe 3 = dos seul ; coupe 4 = yeux fermés cadrés seuls, manteau roulé SOUS le cadre ; coupe 5 = main sans manteau. Red exists only on the coat.
**LOCATION / LIGHT** — @LibraryCorridor : néons un sur deux ; le placard n'a aucune source ; verrière sur la table vide.
**DIALOGUE** — (aucun)
**CAMERA** — fixe · fixe · panoramique d'accompagnement · fixe · latéral.
**LAST FRAME** — the folded paper on the open textbook, the grey sleeve leaving frame.
**AUDIO** — the key ring; the ample page-turning rustle of the coat; his held breath — **then his daughter's running steps on the far side of the stack, passing, fading. Then the breath released.** No music.
**NEGATIVE PROMPT** — visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, **the coat and Sam's face in the same frame**, the Mender's face, any skin in the coat shots, readable book titles, readable words on the paper, red exit signs, red anywhere except the coat.

---

### G17 — LA SALLE DE BAIN : LE SAVON *(plan 19.e · 2,5 s · 1 prise)*

**Elements:** @Sam (main et épaule seulement) + @Bathroom
**Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · 2.5s · sound on
**Style prompt (EN):** White daylight from the frosted window on a bone-dry mirror, the writing invisible, patience made visible instead.

**SCENE / MOVEMENT** — one shot, locked off. Interior, **full daylight, the same morning** — tight shot of the mirror of @Bathroom alone. The mirror is **dry**; the room behind it empty and still (the house is empty, no school bag by the door). @Sam's hand and shoulder enter frame — face never in shot — **writing on the glass with a stub of soap, in ruler-guided stencilled block capitals. The strokes are invisible on the glass.** He steps back out of frame, checks at an angle (his shadow shifts), leans back in, rubs one patch out with his thumb, starts that patch again.
**SUBJECT LOCK** — la main de la référence @Sam (doigts tachés) ; le visage n'entre JAMAIS dans le cadre ni dans le miroir.
**LOCATION / LIGHT** — @Bathroom, jour blanc de la fenêtre dépolie.
**DIALOGUE** — (aucun)
**CAMERA** — tight on the mirror, locked off.
**LAST FRAME** — the dry mirror, apparently blank, the hand finishing a stroke at its edge.
**AUDIO** — the soap squeaking on glass, precise and slow. The empty house. No music.
**NEGATIVE PROMPT** — visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, visible letters on the mirror, readable words, his face in frame or in the mirror, steam, night lighting, any red.
*⚠ RÈGLE H : c'est ce film de savon déposé LE MATIN MÊME que la buée révélera d'un bloc en 15.2 —
rien de surnaturel. EN PLEIN JOUR, impérativement. RÈGLE I : capitales à la règle, jamais lisibles.*

---

### G18 — LE BUREAU À 3 H : LE FORUM *(plan 19.f · 2,5 s · 1 prise · écran [POST] hors bloc)*

**Elements:** @Sam (mains) + un coin de bureau, nuit *(écran [POST])*
**Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · 2.5s · sound on
**Style prompt (EN):** Screen glow plus one desk lamp in a dark room at 3 a.m., a slow pan from the machinery of the myth to its drying artwork.

**SCENE / MOVEMENT** — one shot: a slow pan from desk to radiator. On the desk: a laptop whose screen shows only a soft blue-white glow (**content blank at generation**), and beside the keyboard **a school ruler, a letter stencil, and a spiral notebook where a column of entries is ticked off one by one** — marks only, nothing legible. @Sam's ink-stained hands type, very slow, two fingers. The pan lands on the radiator: **nine tea-aged drawings drying, curled and buckled** — each sheet showing only an abstract dark figure-shape from behind, indistinct at this size, in visibly different media.
**SUBJECT LOCK** — les mains de la référence @Sam seules ; jamais le visage.
**LOCATION / LIGHT** — un coin de bureau, nuit ; une lampe de bureau + la lueur de l'écran, seules sources.
**DIALOGUE** — (aucun)
**CAMERA** — medium, slow pan desk → radiator.
**LAST FRAME** — the radiator with the nine buckled drawings, the desk lamp glow at frame edge.
**AUDIO** — the keyboard, very slow, two fingers. The radiator knocking. No music.
**NEGATIVE PROMPT** — visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, readable screen content, readable usernames, readable words in the notebook, his face, any red, daylight.
*⚠ [POST] hors bloc : TOUT le contenu écran (neuf onglets, neuf pseudos, la carte dans un dixième)
est composé en post, comme toute la séquence 11. Les neuf dessins définitifs sont l'artwork
existant, incrusté si le rendu généré ne suffit pas.*

---

### G19 — LA MAISON ROUGE, NUIT APRÈS NUIT *(plan 19.g · 4,5 s · plate unique, 5 états [ÉDITION D'IMAGE] + 1 génération finale · artwork [POST] hors bloc)*

**Elements:** @Sam (main) + @RedHouseInterior *(plate unique)*
**Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · sound on
**Style prompt (EN):** One rigorously fixed frame across months, a different real light source in each state — the light itself telling the time.

**PRODUCTION** — *Ce bloc n'est PAS une génération vidéo unique : UNE SEULE PLATE de
@RedHouseInterior (cadre large fixe), déclinée par édition d'image en CINQ ÉTATS, chacun animé
~0,7 s (micro-animations image-à-vidéo, cadre rigoureusement identique), coupes franches entre
états ; PUIS une génération finale en gros plan (~1 s). Total à l'écran : 4,5 s.*

**FRAME MAP (les cinq états, même cadre verrouillé)**
(1) bare walls, one written sentence, lit by a hand torch ;
(2) one full panel of writing, lit by a work light hung from the ceiling ;
(3) one whole wall covered, lit by a battery lamp on the floor ;
(4) walls and staircase covered, grey dawn through the doorway ;
(5) walls AND ceiling covered edge to edge, the paraffin lamp burning on the table.
The writing everywhere is stencilled block capitals, never legible.
**[3.5-4.5s] Génération finale, gros plan :** the night after the scream — the cloth-bound evenings notebook open flat beside a pot of ink, and **@Sam's ink-stained hand copying with a pen**, stroke by stroke, onto the wall paper.

**CROSS-FRAME RULES** — the five states share ONE identical locked frame: zero camera movement, zero framing drift between states; only the writing coverage and the light source change. The hand of the final close-up is the exact @Sam reference hand.
**LOCATION / LIGHT** — @RedHouseInterior ; une source réelle différente par état (torche, baladeuse, lampe à piles, aube grise, lampe à pétrole) — c'est la lumière qui raconte le temps.
**DIALOGUE** — (aucun)
**CAMERA** — plate : fixe absolue. Gros plan final : fixe.
**LAST FRAME** — the hand mid-stroke over the notebook and the wall paper, ink pot beside.
**AUDIO** — a pen nib scratching on wood and paper, looped and time-compressed across the five states. **LA MUSIQUE ENTRE ICI — exactement sur la main qui trace le loup.**
**NEGATIVE PROMPT** — visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, legible handwriting, readable words, camera movement between states, framing drift, his face, generated wolf or mountain or bird drawings.
*⚠ [POST] hors bloc : le loup, la montagne et l'oiseau sous la main sont le MÊME artwork unique que
4.3/4.4/4.5 et 18.8, incrusté en post sous le geste. « Des mois — bien avant le cri. La maison
attendait. »*

---

### G20 — SOUS LA CAPUCHE *(plan 19.i · 3 s · 1 prise · vignette [POST] hors bloc)*

**Elements:** @Nora + @BusShelter *(vignette de capuche [POST])*
**Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** Subjective from inside the hood, frame pointed at the ground, the flickering tube on wet asphalt, micro head movements — the third and last handheld moment of the film.

**SCENE / MOVEMENT** — one shot, subjective POV from inside the hood, the frame angled **down at the asphalt** in front of the bench, with very slight head-borne micro-movements. In the flickering tube light on the wet ground: **two soaked off-white canvas sneakers cross the asphalt and stop** a metre away. A girl's hand enters from the top of frame holding a paper-wrapped packet. **The gaze does not rise.** It rises only for half a second, at the very end, when she has already turned: **a dark parka back walking away into the ground mist**, sodium far beyond. The upper and lateral frame edges stay soft and dark (matte refined in post).
**SUBJECT LOCK** — @Nora : baskets et parka de la référence ; **son visage n'apparaît jamais.** Les mains du porteur de la capuche n'entrent jamais dans le cadre.
**LOCATION / LIGHT** — @BusShelter ; le tube qui clignote sur l'asphalte mouillé, sodium au fond.
**DIALOGUE** — (aucun)
**CAMERA** — handheld subjective POV (caméra portée autorisée : troisième et dernière occurrence, avec 14.4 et 18.5-18.6).
**LAST FRAME** — her dark parka back small in the mist, seen low, the frame still hood-darkened at its edges.
**AUDIO** — the tube buzzing; **his own breathing, enormous, trapped under the hood.** The theme fades out by the end of the fragment.
**NEGATIVE PROMPT** — visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, her face, his hands in frame, any red, rain, a raised steady gaze, lettering on the light box.
*⚠ [POST] hors bloc : la vignette de capuche (bord de tissu flou qui cerne le cadre) est composée en
post.*

---

## SÉQUENCE 20 — LA FIN *(35 s · 3 blocs G21-G23 + 8,5 s hors blocs)*
*L'hôpital ENFIN SONORE. On ne revoit jamais Nora après l'abribus.*

### G21 — L'ABRIBUS, AVANT ET APRÈS L'HÔPITAL *(plans 20.1 + 20.2 + 20.9 + 20.10 · 11,5 s · 4 segments, 3 hard cuts — même décor, générés d'un tenant, montés en deux temps)*

**Elements:** @Sam + @BusShelter
**Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic 85mm f/2 · 21:9 · 1080p · 11.5s · sound on
*(Dérogation locale : 20.10 était prévu au 50mm — le bloc passe entier au 85 ; le plan poitrine
recule d'autant, compression assumée.)*
**Style prompt (EN):** The bare tube overhead, hard and unflattering, orbits in shadow; then at last the face is allowed to break — relief and grief arriving in the same second.

**SCENE**
The same man on the same bench: before the memory (he stops chewing, he lifts his eyes) and after it (the nod lands, the tear comes, he eats the last bite and watches the empty road). Four shots, hard cuts. *(Au montage : segments 1-2 = plans 20.1 et 20.2, AVANT le bloc hôpital G22 ; segments 3-4 = plans 20.9 et 20.10, APRÈS. Le raccord 20.8→20.9 est un match-cut sur le hochement.)*

**FRAME MAP**
[0-2.5s] Close-up, locked off: @Sam's face at the shelter, the disguise gone, the real grey beard, bands of clean skin. He has stopped chewing. His eyes are down, **on the half-eaten sandwich in his ink-stained hands.** He does not move. The tube's hard top light puts his eye sockets half in shadow.
[2.5-4.5s] Very tight close-up on his eyes and brow: one event — **he lifts his eyes**, from the sandwich, up, to the middle distance ahead, off-frame. The hooded pale grey-blue eyes, swollen lids, muted catchlights. Nothing else moves.
[4.5-8s] Close-up under the flickering tube: **the shot opens mid-nod — the exact same head movement as 20.8 (bloc G22), to be match-cut on the motion.** He is answering his wife; never his daughter. And only now it comes: **his eyes are already wet at the head of the shot, one single tear detaches and runs into the beard — the tears and the relief happen at the same time.** He does not quite smile; the mouth softens, the shoulders drop once. He held.
[8-11.5s] Chest-up: he lowers his eyes to the sandwich his daughter made. **He takes another bite — the last bite of the film.** He chews, unhurried. He looks down the empty road, in the direction she went, into the dark. The camera pulls back very slowly — barely one metre over the whole shot. The blank light box, the wet kerb, the mist behind.

**SUBJECT LOCK, @SAM**
Exact face of the 8.3-derived master reference: real mid-length grey beard, swollen hooded pale grey-blue eyes, heavy slack cheeks, bands of clean skin in remaining grime, ink-stained index and middle fingers. Same layered clothes, no beanie, in all four shots.

**CROSS-FRAME RULES**
The same man, the same bench, the same shelter, the same buzzing tube in all four shots. The sandwich is the same half-eaten paper-wrapped sandwich throughout. Nobody else ever appears; the road stays empty. No red anywhere. Tears exist ONLY in shot three — dry eyes in shots one and two, wet but settled in shot four.

**LOCATION** — @BusShelter, night, ground mist, wet asphalt, blank unlit light box.

**LIGHT** — the flickering sodium tube overhead, hard, unflattering; everything beyond the cone near-black.

**MOVEMENT**
[0-2.5s] Locked off; nothing moves but his breathing.
HARD CUT
[2.5-4.5s] Locked off; only the eyes come up.
HARD CUT
[4.5-8s] Locked off; opens mid-nod, the tear detaches, the shoulders drop once.
HARD CUT
[8-11.5s] Very slow pull-back, barely one metre; he bites, chews, watches the road.

**DIALOGUE** — (aucun)

**CAMERA**
[0-2.5s] Close-up, locked off. [2.5-4.5s] Very tight close-up, locked off. [4.5-8s] Close-up, locked off. [8-11.5s] Chest-up, very slow pull-back.

**LAST FRAME**
@Sam chest-up on the bench, chewing stopped into stillness, eyes on the dark empty road off-frame, the shelter and the mist behind — dernier plan de son visage dans le film.

**AUDIO**
[0-2.5s] The tube buzz; the foghorn, very far. No music. [2.5-4.5s] **The tube buzz disappears from the mix** — an emptying, not a cut to silence. No music. [4.5-8s] **The evenings theme — one single line, naked.** The tube under it, faint. [8-11.5s] The chewing. Rain beginning on the tin roof of the shelter — heard, not seen. The theme has gone.

**NEGATIVE PROMPT**
visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red, the coat, the beanie, sobbing, a full smile, more than one tear falling, tears before the third shot, a second nod, anyone on the road, visible falling rain, lettering on the light box.

*⚠ Notes FR : 20.2 « IL LÈVE LES YEUX » — un seul événement dans le cadre. 20.9 : « il répond à sa
femme, jamais à sa fille » ; raccord au montage sur le mouvement exact du hochement de 20.8 (G22).
20.10 : « Le film s'ouvre et se ferme sur de la nourriture donnée par amour. »*

---

### G22 — L'HÔPITAL ENFIN SONORE *(plans 20.4 → 20.8 · 13 s · 5 segments, 4 hard cuts · dialogue timecodé — RÈGLE A)*

**Elements:** @Sam + @MaeveIll + @HospitalRoom + @HospitalCorridor *(image-à-vidéo : démarrer sur la DERNIÈRE IMAGE du fichier 7.7a)*
**Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · 13s · sound on
*(Les gros plans 20.5/20.6/20.8 étaient prévus au 85mm — le bloc passe entier au 50 : le travelling
à travers la vitre impose la focale ; les gros plans se serrent au cadre, pas à l'objectif.)*
**Style prompt (EN):** Corridor neon reflections sliding off the lens as the warm white bed lamp takes over — the only warmth left in the world; whites gone grey, sea-green monitor traces far behind.

**SCENE**
The camera crosses the glass we were kept behind, and the film finally lets us hear: her two sentences, the empty corridor where the girl stood, and his single nod. Five shots, hard cuts. *(En amont, au montage : 20.3 = le fichier 7.7a réutilisé TEL QUEL, fondu d'entrée 12 images [POST] — voir « Hors blocs ». Ce bloc démarre en image-à-vidéo sur la dernière image de ce fichier.)*

**FRAME MAP**
[0-2s] From the exact framing of 7.7a — through the wired-glass window of the corridor door, off-centre, @MaeveIll's hands holding @Sam's face — the camera engages a **very slow forward dolly, crosses the wired-glass pane and enters the room.** The corridor neon reflections slide off and leave the frame; the white bed lamp takes over. He is seated close against the bed, back three-quarter to us. Monitor traces pale sea-green.
[2-5.5s] In axis, chest-up: **@MaeveIll framed alone and lit — gaunt, hollowed, the grey-green eyes enormous now — with the back of @Sam's head as a dark out-of-focus mass at the near foreground edge.** Her two hands never release his face; her thumbs move once against his cheekbones. She speaks to him with everything she has left.
[5.5-9s] Close-up on @MaeveIll. **She is crying** — silent tears, no sobbing, her eyes holding his off-frame. She gives the instruction like a bequest, each word placed. Her hands stay raised, holding a face we do not see.
[9-11s] Static shot of the empty @HospitalCorridor — **the exact spot where the girl stood watching through the glass.** On the polished linoleum, **two damp sole prints, already drying at the edges.** Nobody in frame, the corridor receding into shadow. Exit signage green, dim.
[11-13s] Close-up on @Sam by the bed, the north window light flat on him. He holds her gaze off-frame — and **nods. Once. A promise, not a consolation.** The movement is small, vertical, deliberate, clean and isolated: **this exact head movement is the match-cut hinge to 20.9 (bloc G21).** His eyes are wet but nothing falls.

**SUBJECT LOCK, @MAEVEILL**
Exact reference face, gravely ill: sharpened cheekbones, grey pallor, cracked lips, thinned dull auburn hair, grey-green eyes enormous. Plain pale-blue hospital gown — **no scarf, no red in any frame: the scarf was never in this framing.**

**SUBJECT LOCK, @SAM**
The husband at the bed: back three-quarter, then a dark foreground mass, then the close-up of the reference face — eyes wet, nothing falling, one single nod.

**CROSS-FRAME RULES**
The same room, the same bed lamp, the same monitor in shots one to three and five; shot four is the corridor outside the same door. Her hands hold his face continuously through shots one to three. His face is never lit in her shots; her face never in his. No red anywhere. Only these two people exist; the corridor is empty.

**LOCATION** — @HospitalRoom (nuit, lampe de lit blanche, tracés vert d'eau) et @HospitalCorridor (néons verts, linoléum) — the film's one hospital.

**LIGHT** — corridor neon reflections giving way to the white bed lamp, the only warmth left; flat north-window grey on him; green-tinged fluorescents in the corridor.

**MOVEMENT**
[0-2s] Very slow forward dolly through the glass — **coupe invisible dans le reflet du néon au moment du franchissement.**
HARD CUT
[2-5.5s] Locked off; her thumbs move once.
HARD CUT
[5.5-9s] Locked off; the tears run, the words land.
HARD CUT
[9-11s] Locked off; the only event is evaporation.
HARD CUT
[11-13s] Locked off; one nod.

**DIALOGUE**
[3-5s] @MaeveIll, weak, very close to the microphone: "Don't let her go dark."
[6-8.5s] @MaeveIll, crying, barely voiced: "Tell them stories."

**CAMERA**
[0-2s] Medium, slow forward dolly. [2-5.5s] Chest-up, in axis, locked off. [5.5-9s] Close-up, locked off. [9-11s] Static corridor frame. [11-13s] Close-up, locked off.

**LAST FRAME**
@Sam's face in flat grey light at the end of the nod, eyes wet, nothing fallen — the exact motion frame that G21's third segment opens on.

**AUDIO**
[0-2s] **The sound blockade lifts** — the 50 Hz drone thins, and for the first time in the film the sound of the room rises through it: her breathing, a voice below words; the monitor underneath. [2-5.5s] Her voice, faint, intimate — the closest sound of the film; the monitor far under. [5.5-9s] Her voice, the monitor. [9-11s] The 50 Hz drone, alone. [11-13s] The monitor, far. No music anywhere in the block.

**NEGATIVE PROMPT**
visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red, a red scarf, fire extinguisher, name badges, wristbands, readable charts, red exit signs, his face and her face lit in the same shot, blood, IV drama, machine alarms, a second nod, a smile, sobbing, camera shake.

*⚠ Notes FR — RÈGLE A : « Tell them stories. » (segment 3, timecodé [6-8.5s]) est LA SEULE
OCCURRENCE DU MOT « stories » DE TOUT LE FILM. Ce sont les dernières paroles, et elles appartiennent
à la morte. Sous-titre français verrouillé : « Raconte-leur des histoires. » — 20.5 vérifié au
script : « Don't let her go dark. », pas « go out ». 20.7 : « Elle est partie une phrase trop tôt »
— la seule personne à qui ces mots serviraient est celle que le film laisse dehors pour toujours.
Payoff du triptyque 6.5 · 7.7 · 19 : l'hôpital enfin sonore.*

---

### G23 — LA MAIN QUI NE FAIT PLUS DE LUMIÈRE *(plan 20.11 · 2 s · 1 prise · image-à-vidéo sur le cadre référent 4.1)*

**Elements:** @Sam (main — cadre référent 4.1) + @BusShelter *(image-à-vidéo : composer la génération sur le fichier de 4.1, décliné par édition d'image en monde nocturne — même cadre au pixel près, monde noir au lieu d'ambre)*
**Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic 85mm f/2 · 21:9 · 1080p · 2s · sound on
**Style prompt (EN):** The tube's cold spill instead of a lamp's warmth, the same framing as the first bedtime — and the thumb with nothing left to switch on.

**SCENE / MOVEMENT** — one shot, locked off. Night, extreme close-up. **The framing replicates the referent frame 4.1 rigorously — same composition, same scale, same angle on the same man's hand:** the thumb short-nailed, in position — but there is no lamp switch. **The index and middle fingers are stained blue-black with ink. The hand holds the half-eaten sandwich. It no longer makes light.** Cold tube spill from above; mist behind; nothing else in frame.
**SUBJECT LOCK** — la main exacte de la référence @Sam ; le pouce de 4.1.
**LOCATION / LIGHT** — @BusShelter ; le tube froid au-dessus, la brume derrière.
**DIALOGUE** — (aucun)
**CAMERA** — extreme close-up, locked off.
**LAST FRAME** — the hand holding the half-eaten sandwich, motionless in the cold spill — dernier photogramme avant le NOIR (20.12).
**AUDIO** — rain on the tin roof; the foghorn, one last time.
**NEGATIVE PROMPT** — visible camera rigs, cartoonish colors, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red, a lamp, a switch, warm amber light, a face, clean fingertips.
*⚠ CADRE RÉFÉRENT 4.1 → 20.11 : en 4.1 ce pouce allumait la lampe des histoires du soir ; ici il ne
fait plus de lumière — la rime finale. Et le cadre répond au premier plan du film (1.1, la main de
Maeve et le pain) : « le film s'ouvre et se ferme sur de la nourriture donnée par amour ».*

---

## HORS BLOCS — aucune génération

### 20.3 — LA VITRE, LE MÊME CADRE *(2,5 s · [REPRISE DE FICHIER])*
Transition depuis G21/20.2 : **fondu de 12 images à travers le reflet du néon dans la vitre de
l'abribus [POST]** — et l'on retrouve **EXACTEMENT le cadre référent de 7.7a : la même image,
décentrée pareil, reflets pareils, LE FICHIER LUI-MÊME, réutilisé tel quel.** Maeve prend le visage
de Sam dans ses deux mains. Aucune écharpe, aucune chaise dans ce cadre : elles n'y ont jamais été.
**Et la coupure sonore se lève** : d'abord le bourdon 50 Hz du couloir seul, puis — pour la première
fois du film — le son de la chambre monte à travers : la respiration, une voix. Aucun re-rendu,
aucun recadrage du fichier. *(Puis G22 démarre en image-à-vidéo sur la dernière image de ce
fichier.)*

### 20.12 — NOIR *(2 s · [POST])*
Coupe franche au noir pur, tenue deux secondes. Rien à l'écran. **Son :** une corne de brume tenue,
qui s'éteint. Puis silence total.

### 20.13 — LE CARTON *(4 s · [POST])*
Sur le noir, lettrage ivoire, fin, centré, en capitales bâtonnées cohérentes avec la règle
d'écriture du film : **THE MENDER**. Tenu quatre secondes, coupe franche. **Son :** le thème des
soirs, quatre notes au violoncelle. Puis la coupe.
*⚠ RÈGLE A : le titre n'apparaît qu'ici, au tout dernier carton. FIN. « On ne la revoit jamais après
l'abribus. Le dernier plan d'elle est une main qui tend un sandwich. Elle ne saura jamais. Le
spectateur est le seul témoin. »*
