# THE MENDER — PLANS DE GÉNÉRATION · SÉQUENCES 1 → 5

> Blocs Higgsfield Cinema Studio, un par plan numéroté du script (1.1 → 6.6 — le script fait foi).
> Titres et notes en français ; tout le contenu générable en anglais.

## Rappel des réglages du bloc

| | Séq. 1–4 (Acte I) | Séq. 6 (la bascule) |
|---|---|---|
| Genre | **Drama** | **Noir** |
| Camera | Fine Film | Fine Film |
| Lens | Anamorphic | Anamorphic |
| Focale | 40 mm | 50 mm (85 mm sur les inserts et gros plans) |
| Diaph | f/2.8 | f/2 |
| Format | 21:9 · 1080p · sound on | 21:9 · 1080p · sound on |
| Lumière | or d'une seule fenêtre ou d'une seule lampe, chaude, matières vivantes, caméra posée | mêmes décors, la saturation se retire plan après plan ; néons verts au couloir ; caméra posée |

## Éléments requis (générés et validés AVANT toute animation)

- **Personnages :** `@SamBefore` (séq. 1–4) · `@Sam` (6.4 uniquement — RÈGLE F0) · `@Maeve` (séq. 1–5) · `@NoraBefore` (séq. 1, 2, 4) · `@MiloBefore` (séq. 1, 4)
- **Lieux :** `@Kitchen` (séq. 1 et 6.1–6.3) · `@Quay` (séq. 2) · `@LivingRoom` (séq. 5) · `@KidsBedroom` (séq. 4) · `@HospitalCorridor` (6.4)
- **Hors Éléments :** l'homme au gobelet (2.2 — figurant unique décrit au prompt, **N'EST PAS SAM**) · l'artwork unique loup/montagne/oiseau (composé en post sur 4.3/4.4/4.5, réutilisé tel quel en 18.8 et 19.g) · le décor de 6.5 (insert serré décrit, aucun Élément lieu n'existe pour la chambre des parents).

## Rappels opposables sur ces cinq séquences

- **Police du rouge (RÈGLE B).** Le rouge n'existe **nulle part** avant 4.7 — l'écharpe entre sur l'épaule de Maeve en 4.7 et reste le **seul** porteur de rouge jusqu'à 6.5. La fiche `@Maeve` comporte l'écharpe : chaque plan antérieur à 4.7 la **retire explicitement** (prompt + négatif). Neutralisations décor par décor reprises dans chaque NEGATIVE.
- **Jamais de regard caméra. Aucun texte lisible nulle part.** (Le seul mot lisible du film, MENDER en 8.4, n'est pas dans ces séquences.)
- **Jamais un mot d'émotion nu** : le corps montre.
- **Caméra posée partout** (fixe ou dolly régulière) — la caméra portée n'existe qu'en 14.4, 18.5–18.6 et 19.i.
- **Musique : un seul thème (« le thème des soirs »), toujours posé au mix, jamais généré.** Chaque bloc porte `generated music` au négatif ; les entrées du thème sont signalées plan par plan.
- **Cadres référents de ce lot :** 1.8 (fichier conservé, décliné par édition en 8.5) et 4.1 (composition consignée, refaite à l'identique en 20.11).
- Le script donne les fiches en référence d'identité ; quand la scène exige une autre tenue que celle de la fiche (séq. 2 en extérieur), le prompt la décrit — **le visage reste celui de la référence.**

---

## SÉQUENCE 1 — LE MATIN *(26 s, int. jour, @Kitchen — couleurs pleines, chaudes)*

> ⚠ **SÉQUENCE 1 RÉÉCRITE (v3, dialogue des toasts brûlés)** — le découpage fin ci-dessous est
> l'ancienne version muette. La version qui fait foi : `SCRIPT-THE-MENDER.md` (séq. 1) et
> `docs/generations/GEN-SEQ-01-05.md` (GEN-01 «Les toasts brûlés», GEN-02 «Les câlins»).

### Plan 1.1 — 3 s
**Elements:** @Maeve (la main seule) + @Kitchen · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** One low east window is the only source, warm gold morning light with the blue gas flame beneath the pan, deep warm shadows, camera locked off.
**PROMPT (EN):** Extreme close-up, high angle over the gas range of @Kitchen, locked-off camera. A cast-iron pan sits on the blue gas ring; two slices of bread blacken in it, a thin line of smoke rising perfectly straight in the still air. A woman's hand — @Maeve's hand, fair freckled skin, thin gold wedding band — enters frame, flips the slices too late, brushes the hot pan and snatches back in one sharp jerk, shakes itself out and hovers, unrepentant. Her laugh lands just off frame, close and bright. Low golden sun from the east kitchen window rakes across the range while the gas flame gives the pan a blue underlight; the anamorphic lens holds the smoke in soft oval bokeh behind the razor-sharp pan edge. The only person present is @Maeve, framed at the hand and forearm only; no face in frame. @Kitchen is the kitchen of the reference Element, same range, same window direction. Nobody looks at the lens.
**AUDIO:** the sizzle of the pan, one short bright laugh just off mic, a radio playing very low somewhere in the room. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, red fruit or vegetables, red crockery, red tea towel, red jam, saturated red flame + a face in frame, a red scarf, generated music.
*Note : PREMIER PLAN DU FILM — il répond au dernier (20.10 : une main d'homme, seule dans le froid, tient le sandwich de sa fille). Le film s'ouvre et se ferme sur de la nourriture donnée par amour.*

### Plan 1.2 — 4 s
**Elements:** @Maeve + @Kitchen · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 4s · sound on
**Style prompt (EN):** The east window in soft backlight, dust visible in the gold bar of light, deep warm shadows, one smooth slow lateral dolly, no handheld shake.
**PROMPT (EN):** Medium-full shot, slight lateral dolly at a walking-eye pace. @Maeve, barefoot on the cold tile of @Kitchen, stands at the enamel sink scraping the burnt toast with a table knife — with disproportionate, ceremonial care, black crumbs raining into the basin — while she hums along with the radio, landing beside every note and not caring. She wears the oatmeal cable-knit sweater and long dark grey skirt of her reference, sleeves pushed to the elbow, **no scarf** — nothing red exists in this world yet. The window behind her puts her in soft counter-light, dust hanging in the gold bar across the room. The only person in frame is @Maeve, with the exact face of the reference. @Kitchen is the same kitchen as the previous shot, same window direction. Nobody looks at the lens.
**AUDIO:** the knife rasping on charred bread, her humming just off the note, the radio low. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, red fruit or vegetables, red crockery, red tea towel, red jam + a red scarf on her shoulders, shoes on her feet, generated music.

### Plan 1.3 — 3 s
**Elements:** @SamBefore + @Maeve + @Kitchen · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** Two colour temperatures in one frame — cold blue daylight through the open door against the gold of the kitchen — camera locked off.
**PROMPT (EN):** Medium shot, locked off, from inside @Kitchen toward the entrance door. The door opens and @SamBefore comes home off a night shift: navy peacoat hanging open, dried salt crusted white on the shoulders, cheeks reddened raw by cold wind. He sets his canvas bag down by the door and blows into his cupped hands, shoulders still carrying the outside. Through the open door the day reads cold and blue; inside, the east window keeps the kitchen gold — the two temperatures meet across the frame. In the background @Maeve stays at the sink, back turned, still scraping. The only people in frame are @SamBefore and @Maeve, each with the exact face of their reference; no scarf anywhere. @Kitchen is the same kitchen as the previous shot. Nobody looks at the lens.
**AUDIO:** the door, one second of wind, the door clapping shut. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, red fruit or vegetables, red crockery, red tea towel + a red scarf, generated music.

### Plan 1.4 — 4 s
**Elements:** @SamBefore + @Maeve + @Kitchen · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 4s · sound on
**Style prompt (EN):** The east window as the only source, warm gold on the two of them, camera locked off — one single frame, no coverage.
**PROMPT (EN):** Waist-level two-shot, locked off, both of them in the frame the whole time — no cutting inside the shot. @SamBefore crosses @Kitchen without a sound and lays both ice-cold hands flat on the back of @Maeve's neck. She shrieks, her whole back arching, and drives an elbow into his ribs; the two laughs collide and tangle. He kisses the top of her hair, takes the knife out of her hand and finishes scraping the toast himself, already at work as she rubs her neck. The window light holds them both in the same gold. The only two people in frame are @SamBefore and @Maeve, each with the exact face of their reference; she wears no scarf. @Kitchen is the same kitchen as the previous shot. Nobody looks at the lens.
**DIALOGUE:** [1.5-2.7s] @Maeve, laughing through the last of the shriek: "You're a monster." · [3.0-3.8s] @SamBefore, flat, deadpan, already scraping: "I know."
**AUDIO:** the shriek, two laughs colliding, the knife taking up the scraping again, the radio low underneath. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, red fruit or vegetables, red crockery, red tea towel + a red scarf, a cut inside the shot, generated music.
*Note : plan taille, les deux dans le cadre, aucun découpage — le script l'exige.*

### Plan 1.5 — 3 s
**Elements:** @SamBefore + @MiloBefore + @Kitchen · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** The east window gold on the action, deep warm corners, a small smooth dolly back, no shake.
**PROMPT (EN):** Medium shot with a small steady dolly back. @MiloBefore, in his cream pyjamas, bare feet slapping the tile, barrels into @Kitchen and leaps onto @SamBefore's back at the sink. @SamBefore does not even turn around: one arm hooks under the boy and holds him there out of pure habit, and the other hand keeps scraping the toast without missing a stroke. @MiloBefore's laugh shows the gap of his missing lower front tooth as he hangs on. The only people in frame are @SamBefore and @MiloBefore, each with the exact face of their reference. @Kitchen is the same kitchen as the previous shot, same window direction, warm gold morning light. Nobody looks at the lens.
**AUDIO:** bare feet on tile, the boy's high laugh, the knife still scraping. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, red fruit or vegetables, red crockery, red tea towel + the man dropping the child, generated music.

### Plan 1.6 — 3 s
**Elements:** @NoraBefore + @Kitchen · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** The east window in lateral gold on her face, the room's bustle kept off frame, camera locked off.
**PROMPT (EN):** Close medium shot, locked off, lateral window light. @NoraBefore comes into @Kitchen with her hair across her face, in her pale-blue star-print pyjamas, drops onto a wooden chair at the table and watches the commotion somewhere off frame. Her eyes go up to the ceiling — the full twelve-year-old eye-roll — and then the corner of her mouth gives her away: the smile arrives anyway and she lets it stay. The only person in frame is @NoraBefore, with the exact face of the reference; the rest of the family stays off frame. @Kitchen is the same kitchen as the previous shot. Nobody looks at the lens.
**AUDIO:** the chair scraping the tile, the happy chaos of the kitchen behind her, the radio low. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, red fruit or vegetables, red crockery, red tea towel + generated music.

### Plan 1.7 — 4 s
**Elements:** @SamBefore + @Maeve + @Kitchen · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 4s · sound on
**Style prompt (EN):** The east window gold across the table, steam catching in the light, one very slight continuous dolly back, no shake.
**PROMPT (EN):** Insert on hands widening to a waist-level two-shot in one very slight continuous dolly back. @SamBefore pours coffee into @Maeve's cup at the table of @Kitchen: he stops the pour exactly three centimetres below the rim, drops in precisely half a sugar cube, stirs twice — two turns, no more — and sets the cup down on the wood in front of her. He has asked her nothing. @Maeve never looks up: her attention is off frame on the room where the little boy is heard, and her hand simply opens on the table — and the cup is there, meeting it. Their two wedding bands catch the window light. The only people in frame are @SamBefore and @Maeve, each with the exact face of their reference; she wears no scarf. @Kitchen is the same kitchen as the previous shot. Nobody looks at the lens.
**AUDIO:** the coffee pouring, the spoon exactly twice against porcelain, the cup set down on wood, the household warm and indistinct behind. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, red crockery, red fruit or vegetables + a red scarf, a cut inside the shot, generated music.
*Note : ⚠ Ce plan dit tout du couple sans une réplique. Ne jamais le couper.*

### Plan 1.8 — 2 s
**Elements:** @Kitchen (seul — personne dans le cadre) · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 2s · sound on
**Style prompt (EN):** The hard bar of low east sun lying diagonally across the table, warm gold on worn wood, camera locked off directly overhead.
**PROMPT (EN):** Top-down plongée, locked off, directly over the kitchen table of @Kitchen. **FOUR bowls, FOUR mismatched wooden chairs**, steam rising from the bowls, the hard bar of window light lying diagonally across the worn wood, dust in the beam. Nobody is in frame — no hands, no bodies, only the set table and the light; the four overlapping voices live entirely in the sound. @Kitchen is the same kitchen as the whole sequence, same table, same four chairs, same window direction. Everything holds still except the steam.
**AUDIO:** four voices overlapping just off frame, indistinct and bright, spoons against bowls, a chair creak, the radio far under. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, red crockery, red fruit or vegetables, readable labels + any person, any hand, any body part in frame, generated music.
**⚠ RÉFÉRENT:** CADRE RÉFÉRENT — généré **une seule fois** ; le fichier est conservé et **décliné par édition d'image en 8.5** (même cadre : trois bols, une chaise vide, lumière grise, rai de soleil disparu). Jamais regénéré. Consigner l'axe, la hauteur et la position exacte des quatre bols.

---

## SÉQUENCE 2 — CE QU'ELLE DONNE *(18 s, ext. jour, @Quay)*

### Plan 2.1 — 3 s
**Elements:** @Maeve + @NoraBefore + @Quay · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** Soft overcast late-morning daylight, shadowless, wet concrete carrying a dull sheen, one smooth lateral tracking dolly at walking pace.
**PROMPT (EN):** Wide shot, lateral tracking dolly accompanying them at their walking pace. @Maeve and @NoraBefore walk the concrete walkway of @Quay along the stacked grey and blue lobster traps, an ecru canvas tote carried between them, one handle each, their strides settled into the same rhythm. @Maeve wears her oatmeal cable-knit sweater under an open grey wool coat, long dark grey skirt, leather boots, **no scarf**; @NoraBefore — the exact face of her reference — wears a navy duffle coat over a grey jumper, dark jeans and off-white canvas sneakers, hair loose in the sea wind, colour in her cheeks. Trawler masts and cranes stand beyond the traps against a flat pale sky; the water is grey and still. The only people in frame are @Maeve and @NoraBefore. @Quay is the quay of the reference Element. Nobody looks at the lens.
**AUDIO:** gulls, halyards slapping the masts, a diesel idling far off, their steps on wet concrete. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, red buoys, red hulls, red gloves, red traps + a red scarf, generated music.

### Plan 2.2 — 4 s
**Elements:** @Maeve + @NoraBefore + @Quay (+ figurant unique décrit — sans Élément) · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 4s · sound on
**Style prompt (EN):** The same soft overcast daylight, open and even on every face, the dolly easing to a stop exactly when she stops.
**PROMPT (EN):** Medium shot; the lateral dolly slows and stops with her. Against the weathered brick warehouse wall of @Quay a man sits on the ground, a grey blanket over his legs, holding out a beige cardboard cup — he asks nothing, says nothing, his face calm and fully visible in the flat open daylight: **a stranger in his seventies, slight and narrow-shouldered, gaunt, clean-shaven**, nothing about him like the broad bearded fisherman of this family. @Maeve stops mid-stride. She does not search long: she turns her coat pocket out into the cup — coins, one folded bill — and smiles down at him the way one smiles at someone already known, her head slightly tilted. @NoraBefore hangs back a step, weight on one hip, watching. The only people in frame are @Maeve, @NoraBefore and the seated stranger; @Maeve and @NoraBefore have the exact faces of their references; the seated man is seen full-face, in full light, and resembles neither of them nor any other character. @Quay is the same quay as the previous shot. No scarf, no red. Nobody looks at the lens.
**AUDIO:** the coins dropping into cardboard, one by one, the folded bill's paper, gulls above. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, red buoys, red hulls, red cup + a beard on the seated man, a broad heavy build on the seated man, the seated man's face hidden or in shadow, a red scarf, generated music.
*Note : ⚠ CET HOMME N'EST PAS SAM. Silhouette, âge et carrure franchement différents, vu de face, en pleine lumière — le film ne triche jamais ici.*

### Plan 2.3 — 3 s
**Elements:** @Maeve + @NoraBefore + @Quay · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** Overcast flat daylight, no shadows, a steady tracking dolly holding them mid-frame as they walk.
**PROMPT (EN):** Close medium shot in motion, tracking dolly accompanying them. @Maeve and @NoraBefore have taken up their walk again along @Quay, the ecru tote swinging between them. @NoraBefore twists at the waist to look back over her shoulder toward the seated man, now small and out of focus far behind them, then turns to her mother as she speaks. Both have the exact faces of their references; @Maeve wears no scarf. The only people in frame are @Maeve and @NoraBefore, with the stranger far behind in soft anamorphic bokeh. @Quay is the same quay as the previous shot. Nobody looks at the lens.
**DIALOGUE:** [1.2-2.6s] @NoraBefore, over her shoulder, flat, half a challenge: "You don't even know him."
**AUDIO:** their footsteps on the wet concrete, gulls farther off, rigging. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, red buoys, red hulls + a red scarf, generated music.

### Plan 2.4 — 8 s
**Elements:** @Maeve + @NoraBefore + @Quay · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 8s · sound on
**Style prompt (EN):** Soft overcast daylight full on their faces as they walk toward the lens, a steady backwards dolly locked to their pace, no shake.
**PROMPT (EN):** Close two-shot, they walk toward camera, steady backwards tracking dolly at their exact pace for the full duration. @Maeve answers first with her body: one shoulder lifts and drops, the answer self-evident. She delivers the phrase without slowing down. @NoraBefore, beside her, frowns into it — brows knotting, mouth working on the logic. Then @Maeve looks over at her daughter and takes her time, the corner of her mouth going up before she gives her the last two words. The tote swings between them; the port slides by out of focus behind. The only people in frame are @Maeve and @NoraBefore, each with the exact face of their reference; @Maeve wears no scarf; they walk in one single direction the whole shot. @Quay is the same quay as the previous shot. Nobody looks at the lens.
**DIALOGUE:** [0.8-2.6s] @Maeve, easy, worn smooth by habit: "Give and you shall receive." · [3.2-4.6s] @NoraBefore, brow knotted: "Receive what?" · [5.8-7.4s] @Maeve, unhurried, a smile in the voice: "You'll see."
**AUDIO:** the port behind them — gulls, rigging, water against the pilings, their steps. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, red buoys, red hulls + a red scarf, a cut inside the shot, generated music.
*Note : ⚠ LA PHRASE DU FILM. Elle appartient à Maeve, elle est dite dans un vrai moment, et elle paie en 17.6 — le sandwich.*

---

## SÉQUENCE 5 — EUX DEUX *(20 s, int. nuit, @LivingRoom — une seule lampe)*

### Plan 5.1 — 3 s
**Elements:** @Maeve + @LivingRoom · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** A single low lamp with a woven ecru shade is the only source, one warm pool of light, everything beyond it falling to near-black, camera locked off.
**PROMPT (EN):** Medium shot, locked off. @LivingRoom at night: the lamp with the woven ecru shade, posed low on the side table, is the only light in the room. @Maeve is folded into the worn armchair inside its pool, bare feet tucked under her, a midnight-blue clothbound book open in her hands, the knitted throw pushed to one side; her eyes travel the page. Beyond the lamp's throw the room falls away to near-black, the dark window holding a faint reflection of the lit chair. The only person in frame is @Maeve, with the exact face of the reference; she wears no scarf. @LivingRoom is the living room of the reference Element. Nobody looks at the lens.
**AUDIO:** the house at night — the fridge compressor cycling, a foghorn very far off, a page. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, a red lampshade, a red book cover, a red net, a red throw + a red scarf, readable book title, generated music.

### Plan 5.2 — 4 s
**Elements:** @SamBefore + @Maeve + @LivingRoom · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 4s · sound on
**Style prompt (EN):** The single ecru lamp raking warm across working hands, deep black beyond the pool, one very slow continuous dolly back, no shake.
**PROMPT (EN):** Close shot on hands, then one very slow continuous dolly back that widens the frame. @SamBefore sits on the rug of @LivingRoom, his back against @Maeve's armchair, a verdigris fishing net spread across his knees. He mends without looking down: the wooden netting needle passes, loops, knots, pulls tight — the same regular cycle again and again, his hands knowing the work by themselves while his face rests easy in the half-dark. As the frame widens, @Maeve's knees and the edge of her midnight-blue book appear above him in the chair; a page turns over his head. The lamp is the only source, catching the twine and the backs of his clean hands. The only people in frame are @SamBefore and @Maeve, each with the exact face of their reference. @LivingRoom is the same room as the previous shot, same lamp. Nobody looks at the lens.
**AUDIO:** the twine hissing through the mesh, the wooden needle, one page turned above him, the house underneath. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, a red net, a red lampshade, a red book cover + ink stains on his fingers, a cut inside the shot, generated music.
*Note : ⚠ C'EST LE GESTE DU MANTEAU. Même main, même point, même rythme — rappel exact en 19.a. Mains propres : l'encre appartient à l'homme d'après.*

### Plan 5.3 — 5 s
**Elements:** @SamBefore + @Maeve + @LivingRoom · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 5s · sound on
**Style prompt (EN):** One warm lamp pool holding the two of them, near-black all around, camera locked off, nothing moves but their hands.
**PROMPT (EN):** Wide two-shot, locked off, both of them inside the lamp's pool in @LivingRoom. Without breaking the mending rhythm, @SamBefore reaches up from the net, catches @Maeve's two bare feet where they hang at the edge of the armchair, and slides them under his sweater, flat against the warmth of his stomach — one continuous, practised movement. Neither of them looks at the other. Neither says a word. She turns a page; his hands return to the net and the cycle resumes exactly. The lamp is the only source; the rest of the room stays near-black. The only people in frame are @SamBefore and @Maeve, each with the exact face of their reference. @LivingRoom is the same room, same lamp, same armchair as the previous shot. Nobody looks at the lens.
**AUDIO:** the page, the net, nothing else. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, a red net, a red lampshade + either of them speaking, either of them looking at the other, a cut inside the shot, generated music.
*Note : ⚠ PLANT — ce geste revient à l'hôpital en 7.5. C'est le sien, il n'appartient qu'à eux.*

### Plan 5.4 — 5 s
**Elements:** @SamBefore + @Maeve + @LivingRoom · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 5s · sound on
**Style prompt (EN):** The single lamp warm on one side of each face, deep black behind, two locked-off close values only, hard cuts between them.
**PROMPT (EN):** Tight shot–reverse-shot, exactly two camera values, both locked off, hard cuts. Three shots. [0-2s] Close on @SamBefore from beside the lamp: his hands go still on the net; his eyes come up to @Maeve above him and stay there — long, past politeness, unblinking, the lamp warm on one side of his face. HARD CUT [2-3.4s] Reverse close on @Maeve in the armchair: she feels the look land, and lowers the midnight-blue book to her chin, one eyebrow up, and speaks. HARD CUT [3.4-5s] Back on @SamBefore, identical framing to the first shot: he answers and does not look away, the look holding through the end of the shot. The only people are @SamBefore and @Maeve, each with the exact face of their reference in every shot; @LivingRoom, the lamp and the chair are identical across all three shots. Nobody looks at the lens.
**DIALOGUE:** [2.4-2.9s] @Maeve, book at her chin, one eyebrow up: "What?" · [3.7-4.3s] @SamBefore, quiet, holding the look: "Nothing."
**AUDIO:** the house — a clock somewhere, the fridge; their two voices low and close. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, a red lampshade, a red book cover + a third camera value, generated music.
*Note : la remontée du livre devant sa figure glisse sur l'entrée de 5.5.*

### Plan 5.5 — 3 s
**Elements:** @Maeve + @LivingRoom · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** The lamp's warm side-light on the upper half of her face, the book's dark cover closing the bottom of the frame, camera locked off.
**PROMPT (EN):** Close-up, locked off. @Maeve's face behind the raised midnight-blue book in the armchair of @LivingRoom: the cover settles into place across the lower frame, and above its edge she is smiling to herself — the smile pushing at her cheeks and narrowing her eyes while they hold the page far too steadily to be reading. The lamp gives her one warm side; the room behind is black. The only person in frame is @Maeve, with the exact face of the reference; no scarf. @LivingRoom is the same room and lamp as the previous shot. Nobody looks at the lens.
**AUDIO:** the house, faint. Music: rien à générer — au mix, **le thème des soirs entre ici au piano, très bas, pour la première fois du film.**
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, a red book cover, a red lampshade + a red scarf, readable book title, generated music.

---

## SÉQUENCE 4 — LES SOIRS *(34 s, int. nuit, @KidsBedroom — le visage et la voix de Sam ; le rouge entre en 4.7)*

### Plan 4.1 — 2 s
**Elements:** @SamBefore (le pouce seul) + @KidsBedroom · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 2s · sound on
**Style prompt (EN):** The bedside lamp itself is the entire source, saturated warm amber blooming up from black as the filament climbs, camera locked off.
**PROMPT (EN):** Extreme close-up, locked off. A man's thumb — @SamBefore's, short clean nail, **no ink anywhere on the fingers** — pushes the toggle switch of the bedside lamp with the woven shade in @KidsBedroom. One dry click; the filament climbs from dull orange to full warm amber and the woven shade prints its texture onto the light as the frame fills. Nothing else in frame: the thumb, the switch, the base of the lamp, the amber bloom. The only person present is @SamBefore, framed at the thumb and hand only. Nobody looks at the lens.
**AUDIO:** the dry click, then the small held silence of a room with two children in it. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, a red lampshade + ink stains on the fingers, a face in frame, generated music.
**⚠ RÉFÉRENT:** CADRE RÉFÉRENT — composition à consigner au pixel (échelle, angle, position de la main et de la lampe) et **à réutiliser à l'identique en 20.11** : la même main, le même pouce — mais index et majeur tachés d'encre, tenant le sandwich à demi mangé, et « elle ne fait plus de lumière ».

### Plan 4.2 — 6 s
**Elements:** @SamBefore + @NoraBefore + @MiloBefore + @KidsBedroom · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 6s · sound on
**Style prompt (EN):** The bedside lamp takes him three-quarters, warm and frank, the room falling to warm dark behind, camera locked off.
**PROMPT (EN):** Close medium shot on @SamBefore, locked off, the children as soft out-of-focus foreground. On the edge of the bed in @KidsBedroom, **face on, in full lamp light**: @SamBefore. @NoraBefore and @MiloBefore lie under the amber quilt pulled to their chins, their heads soft shapes at the bottom of frame. He is in the middle of telling it — leaning in, doing the voices, hands beginning to shape something in the air, with the total seriousness of a man doing the most important work of his day. When the boy interrupts, @SamBefore answers without breaking register, grave as a judge, and the children's laughter tumbles over it. The only people in frame are @SamBefore, @NoraBefore and @MiloBefore, each with the exact face of their reference; his hands are clean, no ink. @KidsBedroom is the bedroom of the reference Element, the lamp its only source. Nobody looks at the lens.
**DIALOGUE:** [0-3.0s] @SamBefore, a low storyteller's rumble, dead serious: "…and the wolf had been walking so long his paws had gone soft. Soft like bread." · [3.4-4.4s] @MiloBefore, delighted, through the gap of a missing tooth: "That's disgusting." · [4.5-6s] @SamBefore, grave, not missing a beat: "It's extremely disgusting. Don't interrupt."
**AUDIO:** his full voice, two children's laughter tumbling over it, the quilt shifting. Music: rien à générer — le thème des soirs court très bas au mix.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, red drawings on the wall, a red quilt + ink stains on his fingers, generated music.

### Plan 4.3 — 3 s
**[POST]** *On génère : le mur papier peint + la lampe rasante + les mains nouées de @SamBefore en amorce, le mur laissé net de toute figure. On composite : l'ombre du LOUP — l'artwork vectoriel unique (le même jeu loup/montagne/oiseau que 18.8 et 19.g), animé en ombre portée.*
**Elements:** @SamBefore (mains en amorce) + @KidsBedroom + artwork loup (post) · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** The bedside lamp rakes the wall from low and close so any cast shadow reads huge and knife-edged, saturated amber, camera locked off.
**PROMPT (EN):** Wide shot of the papered bedroom wall of @KidsBedroom, locked off, @SamBefore's knotted hands as a dark out-of-focus shape at the frame edge in front of the bedside lamp. The lamp rakes the wall from low and close; the wall itself stays an open field of warm amber light and paper grain, **kept clear of any distinct shadow figure** — the wolf shadow is composited in post from the master artwork. His growl lands — a domestic growl with no menace in it, twice, badly — and off frame two children shriek with laughter. The only person present is @SamBefore, framed at the hands only; the children stay off frame. @KidsBedroom is the same room and lamp as the previous shot. Nobody looks at the lens.
**AUDIO:** the failed growl, twice, and two children howling with laughter. Music: rien à générer — le thème court au mix.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, red drawings on the wall + a wolf, any animal-shaped shadow, any recognizable shadow figure on the wall (composited in post), a face in frame, generated music.

### Plan 4.4 — 3 s
**[POST]** *On génère : même dispositif que 4.3 — le mur nu sous la lampe rasante, les deux mains à plat en amorce, arête tenue. On composite : la silhouette de la MONTAGNE depuis l'artwork unique.*
**Elements:** @SamBefore (mains en amorce) + @KidsBedroom + artwork montagne (post) · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** The same raking amber lamp light across the bare wall, deep warm shadow at the edges, camera locked off, absolute stillness.
**PROMPT (EN):** Wide shot of the same papered wall of @KidsBedroom, locked off, identical set-up to the previous shot. @SamBefore's two hands come flat together in the foreground amorce, edge against edge, one clean ridge line — and hold absolutely still. The wall stays an open field of raking amber light, **clear of any distinct shadow figure** — the mountain silhouette is composited in post. Off frame, the little boy's laughter stops at once: the cut of that sound is the event of the shot. The only person present is @SamBefore, framed at the hands only. @KidsBedroom is the same room and lamp as the previous shot. Nobody looks at the lens.
**DIALOGUE:** [0.3-2.2s] @SamBefore (off, at frame edge), the voice dropping lower and slower: "And then, right in front of him — a mountain."
**AUDIO:** his voice; the laughter stopping dead; the room's small silence. Music: rien à générer — au mix, **le piano se creuse d'un ton.**
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, red drawings on the wall + a mountain shadow, any recognizable shadow figure on the wall (composited in post), a face in frame, generated music.

### Plan 4.5 — 5 s
**[POST]** *On génère : la plaque de panoramique — le mur balayé par un pano de 15° vers l'embrasure, lampe rasante, pouces croisés en amorce. On composite : l'OISEAU de l'artwork unique, animé battant des ailes le long du pano jusqu'à l'embrasure.*
**Elements:** @SamBefore (mains en amorce) + @KidsBedroom + artwork oiseau (post) · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 5s · sound on
**Style prompt (EN):** The raking amber lamp light travelling the wall as a single slow 15-degree pan drifts toward the doorway, camera on a fluid head, no shake.
**PROMPT (EN):** Wide shot of the papered wall of @KidsBedroom; one single slow 15-degree pan, left to right, ending toward the dark doorway edge. @SamBefore's crossed thumbs and spread fingers rise into the foreground amorce in front of the lamp and hold their bird shape as the pan travels the raking amber light along the wall toward the door — the wall itself **kept clear of any distinct shadow figure**: the bird shadow that beats its wings across the whole wall is animated and composited in post along this camera path. His voice places each word like a stone. The only person present is @SamBefore, framed at the hands only; the children stay off frame; the pan moves in one direction only, once. @KidsBedroom is the same room and lamp as the previous shot. Nobody looks at the lens.
**DIALOGUE:** [0.3-3.2s] @SamBefore, the low register, each word placed: "And the bird said: I'll carry you over. But you have to give me something first."
**AUDIO:** his voice; then only the room. Music: rien à générer — au mix, **le piano tient une note.**
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, red drawings on the wall + a bird, any bird-shaped shadow, any recognizable shadow figure on the wall (composited in post), a second pan direction, a face in frame, generated music.
*Note : ⚠ LA PIÈCE MAÎTRESSE DU FILM. La loi du Mender — il demande une petite chose d'abord — est prononcée ici, trois ans avant que le mythe n'existe. Personne ne le relève. C'est dans ce qu'il raconte le soir que Sam ira la prendre.*

### Plan 4.6 — 3 s
**Elements:** @NoraBefore + @KidsBedroom · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** The bedside lamp warm and low across her face on the pillow, the rest of the room in warm dark, camera locked off.
**PROMPT (EN):** Close-up, locked off. @NoraBefore on the pillow in @KidsBedroom, the amber quilt at her chin, the lamp warm on her face. She is completely inside it: lips parted, eyes wide and locked on the wall off frame, the quilt edge forgotten in her fists — she does not blink once in the whole shot. She is twelve, and every muscle in her face says she believes it. Her father's voice continues off frame, low, an indistinct narration murmur with no distinct words. The only person in frame is @NoraBefore, with the exact face of the reference. @KidsBedroom is the same room and lamp as the previous shot. Nobody looks at the lens.
**AUDIO:** her father's voice off, low and indistinct, no intelligible words; the quilt; the lamp's silence. Music: rien à générer — le thème court au mix.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, a red quilt + intelligible generated dialogue, a blink, generated music.

### Plan 4.7 — 4 s
**Elements:** @Maeve + @KidsBedroom · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 4s · sound on
**Style prompt (EN):** The bedroom lamp reaching her at a raking angle across the doorway, the hallway behind her pure black, only the red catching, camera locked off.
**PROMPT (EN):** Chest-up close shot, locked off, on the doorway of @KidsBedroom. @Maeve stands with her shoulder against the doorframe, arms loosely folded, **the deep crimson wool scarf of her reference wound over her shoulders — the first red of the film, and the only red in the frame.** She is not watching her children: her eyes are aimed off frame at the man telling it by the lamp — on him — steady and unhurried, the stance of someone with nowhere else she would rather be standing. The bedroom lamp reaches her at a raking angle; the hallway behind her is black; only the red catches the light. The man's voice continues off frame; the camera never rejoins him. The only person in frame is @Maeve, with the exact face of the reference; her gaze goes off frame toward the bed, never at the lens.
**AUDIO:** Sam's voice off, low, indistinct; the room. Music: rien à générer — au mix, **la voix passe dessous le piano.**
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red other than the scarf, red drawings, a red lampshade + her looking into the room's children, a lit hallway, generated music.
*Note : ⚠ LE ROUGE ENTRE DANS LE FILM ICI, sur l'épaule de Maeve. Il le quittera en 7.9, sur un geste. Elle ne regarde pas ses enfants — elle le regarde, lui.*

### Plan 4.8 — 3 s
**Elements:** @SamBefore + @KidsBedroom · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** The bedside lamp full and warm on him, deep warm dark behind, camera locked off.
**PROMPT (EN):** Close medium shot, locked off. @SamBefore in full play at the edge of the bed in @KidsBedroom, one hand still raised in the air holding half a shape, the laugh sitting openly in his face, shoulders loose, leaning into the lamp light — a man in the middle of the best part of his day, with no idea that he is being watched from the doorway. The children's laughter rises around his voice from the bottom of frame. The only people in frame are @SamBefore and, as soft shapes under the quilt, @NoraBefore and @MiloBefore, each with the exact face of their reference; his hands are clean, no ink; the doorway stays out of this frame. @KidsBedroom is the same room and lamp as the previous shot. Nobody looks at the lens.
**AUDIO:** his voice, the children's laughter. Music: rien à générer — le thème court au mix.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, a red quilt + ink stains on his fingers, the doorway or the woman in frame, generated music.

### Plan 4.9 — 3 s
**Elements:** @Maeve + @NoraBefore (voix off) + @KidsBedroom · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** The lamp's raking warmth across her at the doorframe, the hallway black behind, only the scarf's red catching, camera locked off.
**PROMPT (EN):** Close shot on @Maeve at the doorway of @KidsBedroom, locked off, same raking light as before — the crimson scarf still the only red in frame. She says the evening phrase the way one says goodnight: without thinking about it, already half-turned to go, the words worn round from use. From the bed, off frame, her daughter's answer comes back without a head lifting from the pillow. The only person in frame is @Maeve, with the exact face of the reference; the hallway behind her stays black; her eyes rest on the room, never on the lens.
**DIALOGUE:** [0.5-2.0s] @Maeve, offhand, warm, no weight on it: "Give and you shall receive." · [2.2-3.0s] @NoraBefore (off, without lifting her head), automatic, sing-song: "We know, Mom."
**AUDIO:** their two voices, the quilt shifting off frame. Music: rien à générer — au mix, **le piano baisse d'un cran pour elle, et pour elle seule.**
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red other than the scarf + a lit hallway, generated music.

### Plan 4.10 — 2 s
**Elements:** @SamBefore + @Maeve (silhouette à l'embrasure) + @KidsBedroom · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 2s · sound on
**Style prompt (EN):** The bedside lamp as the last light in the world, then black — a slight steady dolly back, no shake.
**PROMPT (EN):** Waist-level shot with a slight steady dolly back. @SamBefore turns from the bed toward the doorway of @KidsBedroom and smiles at the woman standing there — @Maeve, a dark shape at the doorframe, the crimson scarf a last ember of red — and she returns the smile as the hallway light behind her dies. He is already turning back to the children, picking up exactly where he stopped, when the bedside lamp goes out on his voice and the frame drops to black. The only people in frame are @SamBefore, @Maeve at the doorway, and the two children as soft shapes under the quilt, each with the exact face of their reference. @KidsBedroom is the same room and lamp as the whole sequence. Nobody looks at the lens.
**AUDIO:** his voice continuing in the dark for two full seconds after the light dies — then a hard cut. Music: rien à générer — au mix, le thème s'efface avec la lampe.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red other than the scarf + the voice stopping with the light, generated music.

---

## SÉQUENCE 6 — LA BASCULE *(12 s — un an plus tard ; la saturation se retire plan après plan)*

### Plan 6.1 — 2 s
**Elements:** @Maeve (la main seule) + @Kitchen · **Settings:** Genre Noir · Camera Fine Film · Lens Anamorphic 85mm f/2 · 21:9 · 1080p · 2s · sound on
**Style prompt (EN):** The same east kitchen window, but the sky is white and the light lies flat — the gold is gone, colour just starting to drain, camera locked off.
**PROMPT (EN):** Insert, locked off, at counter height in @Kitchen — the same kitchen, the same east window as the first morning, but full daylight under a white sky: the light is flat, the hard gold bar has disappeared. A white porcelain cup slips out of a woman's hand — @Maeve's hand, the thin gold band — and bursts on the tile, shards skating outward. The hand stays where the cup left it, half open. The radio keeps playing, unchanged, indifferent. The only person present is @Maeve, framed at the hand and forearm only; no face in frame. @Kitchen is the kitchen of the reference Element, same window direction as sequence 1. Nobody looks at the lens.
**AUDIO:** the porcelain, very loud and close; the radio carrying on under it, unchanged. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, a red cup, red crockery, any blood + warm golden light, a face in frame, generated music.
*Note : la désaturation s'installe — même fenêtre qu'en 1.1, ciel blanc, plus de rai d'or. Tasse blanche imposée (police du rouge, séq. 6). Aucun sang, nulle part.*

### Plan 6.2 — 3 s
**Elements:** @Maeve + @Kitchen · **Settings:** Genre Noir · Camera Fine Film · Lens Anamorphic 85mm f/2 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** Flat white window light with no modelling, the colour thinning further, two locked-off close values, hard cut.
**PROMPT (EN):** Two shots, hard cut, both locked off. [0-1.6s] Extreme close-up on @Maeve's hand held up in front of her in the flat window light of @Kitchen: the fingers open, then close, then open again — each time a half-beat late on her intent, the thumb not quite meeting the fingertips. Twice. HARD CUT [1.6-3s] Close-up on her face: @Maeve, the exact face of the reference, her eyes down on the hand, held very still, the swallow visible in her throat; then her mouth closes into a flat line and she looks toward the window instead of the door. **She tells no one.** The only person in frame is @Maeve; no scarf, no red. @Kitchen is the same kitchen as the previous shot, the light flat and toneless. Nobody looks at the lens.
**AUDIO:** the radio; the house behind her — two children's voices arguing somewhere far off in the flat. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, any blood + a red scarf, warm golden light, her speaking, generated music.

### Plan 6.3 — 3 s
**Elements:** @Maeve + @Kitchen · **Settings:** Genre Noir · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** Flat white daylight over the whole room, saturation almost gone, deep focus only on her, camera locked off.
**PROMPT (EN):** Wide shot, locked off. @Maeve kneels small in the lower part of the frame on the tile of @Kitchen, gathering the porcelain shards into her open palm one by one, unhurried, precise, her head bowed to the work. Far behind her, past the anamorphic lens's shallow field, the blurred warmth of the household keeps moving — a small out-of-focus silhouette crosses the hallway, unaware, unrecognizable. The white window light lies flat over everything; the room's colours have thinned. The only sharp person in frame is @Maeve, with the exact face of the reference; any background figure stays severely out of focus and unidentifiable; no scarf, no red. @Kitchen is the same kitchen as the previous shot. Nobody looks at the lens.
**AUDIO:** the porcelain clicking piece by piece into her palm; the household muffled behind; the radio faint. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus on her, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, any blood + a sharp face in the background, warm golden light, generated music.

### Plan 6.4 — 2 s
**Elements:** @Sam + @HospitalCorridor · **Settings:** Genre Noir · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · 2s · sound on
**Style prompt (EN):** Overhead fluorescent tubes, green and pitiless, reflecting off the polished floor, deep shadow at the corridor's far end, camera locked off.
**PROMPT (EN):** Wide shot, locked off, down the length of @HospitalCorridor at night. @Sam sits alone on one of the plastic chairs against the wall, leaning far forward, elbows on knees, both hands joined and pressed against his mouth. He does not move for the entire shot — the stillness is the event; only his breath moves the joined hands a fraction. The green fluorescent tubes overhead are the only light, doubling in the polished floor; the far end of the corridor falls to shadow; every exit sign that appears is green. The only person in frame is @Sam, with the exact face of the reference — the bearded, weary man. @HospitalCorridor is the corridor of the reference Element. Nobody looks at the lens.
**AUDIO:** the 50 Hz mains hum. Nothing else. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red anywhere, red exit signage, a fire extinguisher in frame, any blood + name badges, wristbands, readable notice boards, him moving or standing, generated music.
*Note : fiche @Sam imposée par la RÈGLE F0 (deux états, deux fiches, jamais mélangés — présent = séq. 6 à 19). Aucun toponyme, aucun badge, aucun tableau nominatif (règle TEXTE À L'ÉCRAN).*

### Plan 6.5 — 7 s
**Elements:** @Sam + @Nora + @HospitalCorridor · **Settings:** Genre Noir · Camera Fine Film · Lens Anamorphic 85mm f/2 · 21:9 · 1080p · 7s · sound on
**Style prompt (EN):** Flat green overhead fluorescents doubling in the polished floor, the window at the far end of the corridor blown out to white, long-lens compression, camera locked off, no handheld shake.
**PROMPT (EN):** Long-lens shot down the length of @HospitalCorridor in daylight, locked off. In the extreme foreground, soft and out of focus, the back of a teenage girl's head and shoulder (@Nora) at the frame's left edge — we watch from behind her, from her place. Ten metres away, compressed by the long lens, two men stand in the middle of the corridor: a hospital doctor in his sixties, short grey hair, rimless glasses, a white coat over a grey shirt, a closed folder held against his thigh — and @Sam, the bearded, weary man of the reference, in his olive canvas work jacket. The doctor speaks quietly; no words carry. He stops speaking. @Sam's head goes down, slowly, in one continuous movement. Then the doctor lowers his own eyes, and places one hand on @Sam's shoulder. The hand stays. Neither man moves again for the rest of the shot. @Nora does not move at all. Every exit sign is green. Nobody looks at the lens.
**DIALOGUE:** Aucun — la conversation est VISIBLE mais jamais audible.
**AUDIO:** the 50 Hz mains hum of the corridor, a trolley far off, a phone ringing once in a closed office. No voices. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, on-screen text, subjects looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, audible dialogue, lip movements readable as words, any red anywhere, red exit signage, a fire extinguisher in frame, name badges, wristbands, readable notice boards, generated music.
*Note : premier volet du triptyque des conversations muettes (6.5 → 7.7 → 19). Le MÉDECIN apparaît une seule fois — généré au plan, pas d'Élément. @Sam en fiche présent (RÈGLE F0).*

### Plan 6.6 — 2 s
**Elements:** @Maeve (les mains seules) — aucun Élément lieu : insert serré décrit (chambre adulte, dessus de lit neutre, lampe de chevet) · **Settings:** Genre Noir · Camera Fine Film · Lens Anamorphic 85mm f/2 · 21:9 · 1080p · 2s · sound on
**Style prompt (EN):** A single bedside lamp, warm but muted, every colour in the frame drained except one, camera locked off.
**PROMPT (EN):** Insert, locked off, on the corner of a bed in a dim adult bedroom — a small soft travel bag lies open on a plain grey-beige quilt, half packed with folded pale clothing. @Maeve's hands — fair freckled skin, the thin gold band — lower in, last of all, **the deep crimson wool scarf, folded with care**, smooth it once flat with the palm, and draw the zip closed across it. The scarf's red is the only saturated colour in the frame; everything else has gone toneless under the single bedside lamp. The only person present is @Maeve, framed at the hands and forearms only; no face in frame. Nobody looks at the lens. The shot ends clean on the closed bag.
**AUDIO:** the bag's hinge of fabric, the zip — full and close — then a hard dry cut. No music.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage + any red other than the folded scarf, any blood + a face in frame, hospital equipment, generated music.
*Note : l'écharpe traverse la séq. 6 ici seulement ; elle repart avec Maeve vers l'hôpital (séq. 7) et le rouge quittera le film en 7.9, sur un geste. Coupe sèche.*

---

*Fin des séquences 1 → 5 — 32 blocs. Suite : séquence 7 (l'hôpital — blanc froid, vert d'eau, cadre référent absolu 7.7a) dans le lot suivant.*
