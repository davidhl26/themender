# THE MENDER — GÉNÉRATIONS GROUPÉES · SÉQUENCES 1 → 5

> **⚠ REMPLACÉ (20/08) — ce lot est intégralement remplacé par `GEN-SEQ-01-07.md`** (Bloc I restructuré : acte I = une seule soirée — séq. 1 au soleil du soir + 1.7bis « Or… we eat out tonight » + 1.8 table dressée intacte, nouvelles séq. 2 LA ROUTE (famille entière, écharpe rouge dès 2.1) et séq. 3 LE RESTAURANT HEUREUX, plan 4.11 ajouté).
> Aucun bloc de ce fichier ne doit plus être généré tel quel : les toasts, le quai, eux deux, les soirs et la bascule y sont repris adaptés/renumérotés (GEN-01→12), les [POST] 4.3-4.5 recopiés.
> Conservé pour archive et comparaison uniquement.

> Regroupement du découpage fin (`docs/plans/PLANS-SEQ-01-05.md`) en **le moins de générations
> possible**, au format niveau 4 du pack *5 Levels of AI Video Prompting* (shot list : SCENE /
> FRAME MAP / SUBJECT LOCK / CROSS-FRAME RULES / LOCATION / LIGHT / MOVEMENT + HARD CUT /
> DIALOGUE / CAMERA / LAST FRAME / AUDIO / NEGATIVE PROMPT), enrichi niveau 5 (@Éléments +
> réglages Cinema Studio). Le script (`docs/SCRIPT-THE-MENDER.md`) fait foi.
> Titres et notes en français ; **tout le contenu générable en anglais**.

**10 blocs de génération · 109 s générées en blocs · + 11 s en [POST] (4.3, 4.4, 4.5) = 117 s
du script couvertes** (séq. 1 : 30 s · séq. 2 : 18 s · séq. 5 : 20 s · séq. 4 : 34 s · séq. 6 : 19 s).
C'est le minimum : chaque séquence dépasse 15 s (ou change de lieu), donc aucun regroupement
supplémentaire n'est possible sans franchir une séquence ou le plafond de durée.

## Table de correspondance bloc → plans du script

| Bloc | Titre | Durée | Plans couverts | Lieu | Élément(s) lieu |
|---|---|---|---|---|---|
| GEN-01 | «Les toasts brûlés» | 15 s | 1.1 → 1.4 | cuisine | @Kitchen |
| GEN-02 | «Les câlins» | 12 s | 1.5 → 1.8 | cuisine | @Kitchen |
| GEN-03 | «Le quai» | 10 s | 2.1 → 2.3 | quai | @Quay |
| GEN-04 | «Donne, et tu recevras» | 8 s | 2.4 | quai | @Quay |
| GEN-05 | «Eux deux» | 12 s | 5.1 → 5.3 | salon | @LivingRoom |
| GEN-06 | «Le regard tenu» | 8 s | 5.4 → 5.5 | salon | @LivingRoom |
| GEN-07 | «La lampe des soirs» | 8 s | 4.1 → 4.2 | chambre des enfants | @KidsBedroom |
| GEN-08 | «Le rouge entre» | 15 s | 4.6 → 4.10 | chambre des enfants | @KidsBedroom |
| GEN-09 | «La tasse» | 8 s | 6.1 → 6.3 | cuisine | @Kitchen |
| GEN-10 | «Le couloir, deux fois» | 11 s | 6.4 → 6.6 | couloir d'hôpital + insert chambre | @HospitalCorridor (6.6 décrit, sans Élément) |
| [POST] | loup / montagne / oiseau | 11 s | 4.3 · 4.4 · 4.5 | chambre des enfants | @KidsBedroom |

**Décisions de groupage à connaître**
- **GEN-04 (2.4 seul).** Le script interdit tout découpage intérieur de 2.4 (« aucun découpage »),
  et la séquence 2 dépasse 15 s : le plan reste une prise unique de 8 s — dérogation assumée à la
  règle « 2 à 6 plans par bloc ».
- **GEN-10 (6.4 + 6.5 + 6.6).** Le raccord nuit/jour n'interdit PAS le groupage : c'est un saut de
  temps **écrit au script**, traité comme le changement tunnel→arène du « Boxer » du pack — chaque
  segment porte son propre bloc LIGHT et rien ne doit se raccorder à travers la coupe. 6.6 (2 s)
  ne peut pas tenir seul (règle 8–15 s) ; il rejoint le bloc sur sa coupe sèche scriptée.
- **Cadres référents dans les blocs.** 1.8 est le **dernier** segment de GEN-02 (son fichier — et
  sa dernière image — est extrait et conservé pour la déclinaison 8.5) ; 4.1 est le **premier**
  segment de GEN-07 (composition consignée au pixel pour 20.11). Doctrine « une seule prise n'a
  pas de couture » : le LAST FRAME de chaque bloc est décrit précisément et sert de raccord.
- **Police du rouge.** Aucun rouge nulle part avant 4.7. L'écharpe de @Maeve n'existe qu'en
  GEN-08 (segments où elle apparaît) et au segment final de GEN-10 ; partout ailleurs le négatif
  l'exclut explicitement. Le mot proscrit (RÈGLE A) n'apparaît dans aucun prompt.
- **Musique.** Un seul thème (« le thème des soirs »), toujours posé AU MIX, jamais généré —
  chaque bloc porte `generated music` au négatif ; les entrées du thème sont signalées en note.

---

## GEN-01 — «Les toasts brûlés» (15 s) — couvre les plans 1.1 → 1.4 du script

**Elements:** @SamBefore + @Maeve + @Kitchen · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 15s · sound on
**Style prompt (EN):** One low east window is the only source, warm gold morning light, a hard bar of light across the table with dust visible in it, the blue of the gas flame under the pan, deep soft shadow in the corners, camera locked off, no handheld shake.

SCENE
A husband and wife tease each other over burned toast in their small kitchen in the morning. Four shots, hard cuts. Warm, alive, unposed.

FRAME MAP
[0-3s] Extreme close-up, high angle over the gas range. A cast-iron pan centred, two slices of bread blackening, smoke rising straight. A woman's hand enters from the right and touches one slice with a fingertip, snatches back.
[3-7s] Medium two-shot. @Maeve at the range screen-right, x=65%, barefoot, still laughing. @SamBefore seated at the table screen-left, x=30%, a bowl in front of him, looking up at her.
[7-12s] Medium close two-shot at the table. @Maeve slides the blackened toast onto a plate and sets it in front of @SamBefore with mock ceremony, then points a finger at him, mock-stern. He looks down at the plate, then up at her.
[12-15s] Waist-level two-shot, one framing, no coverage. @SamBefore stands, catches @Maeve by the waist and kisses her neck. She protests for form's sake, laughing, and keeps laughing. He keeps his face in her neck one second too long.

SUBJECT LOCK, MAEVE
The exact woman of the reference — dark auburn wavy hair, grey-green eyes, freckles, oatmeal cable-knit sweater with pushed-up sleeves, dark grey long skirt, barefoot, thin gold wedding band. Laughing easily through the whole block. She never looks at the lens.

SUBJECT LOCK, SAM
The exact man of the reference @SamBefore — upright, solid, short neat dark brown hair, short trimmed salt-and-pepper beard, pale grey-blue eyes, clean hands, grey marl sweatshirt. Dry deadpan humour breaking into a smile. He never looks at the lens.

CROSS-FRAME RULES
The same two people in all four shots, exact faces of their references, same wardrobe throughout. @Kitchen is the same kitchen in all four shots: same table, same four mismatched chairs, same window direction, same crockery. The light comes from the same low east window in every shot. The pan and the burned toast persist across the cuts.

LOCATION
@Kitchen — the worn wooden table under the window, gas range with the cast-iron pan, cream and blue crockery, cluttered counter, small radio playing low.

LIGHT
Warm gold morning sun through the single east window, dust in the beam, blue gas flame under the pan, no other source.

MOVEMENT
[0-3s] Her fingertip touches the blackened toast, snatches back. Off-screen her voice, then a real laugh.
HARD CUT
[3-7s] She scrapes at the toast, laughing; he watches her over his bowl and speaks; she answers without turning around, then turns, wooden spatula in hand.
HARD CUT
[7-12s] She sets the plate of charcoal toast in front of him like a prize, points a mock-stern finger; he looks at the plate, looks up, delivers his line flat; she delivers hers holding back laughter.
HARD CUT
[12-15s] He stands, catches her waist, kisses her neck; she laughs and swats at him without meaning it.

DIALOGUE
[1-3s] @Maeve, off-screen then laughing, warm: "Oh no… I think I burned the toast."
[4-5.5s] @SamBefore, deadpan: "Why don't you use the toaster?"
[5.5-7s] @Maeve, shrugging, not turning: "It's broken. And we're saving money."
[8-9.5s] @SamBefore, looking at the plate, flat: "Yeah… but this is charcoal."
[9.5-12s] @Maeve, finger pointed, mock-stern, fighting a smile: "You've got no choice. You'll eat it, you horrible man."

CAMERA
[0-3s] Extreme close-up, high angle, static.
[3-7s] Medium two-shot, eye level, static, wide lens.
[7-12s] Medium close two-shot across the table, eye level, static.
[12-15s] Waist-level two-shot, eye level, static — one framing, no coverage.

LAST FRAME
The two of them in one frame at the table, his face in her neck, her head tipped back laughing, the plate of burned toast in the lower third, the bar of window light across the table.

AUDIO
The pan sizzling, her fingertip on the toast, a real laugh, the radio low in the room, the plate set on wood, their two voices warm and quick, her laughter under the kiss. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subjects looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, red fruit, red kettle, red crockery, red packaging, posed smiles, sitcom lighting, generated music.

*Note : premier plan du film (1.1) — la main qui touche la nourriture ratée par amour répond au dernier plan (20.10, la main qui tient le sandwich). Grille-pain absent du décor @Kitchen : ne pas en faire apparaître un.*

---

## GEN-02 — «Les câlins» (12 s) — couvre les plans 1.5 → 1.8 du script

**Elements:** @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @Kitchen · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 12s · sound on
**Style prompt (EN):** Same single east window, warm gold, dust in the beam, camera locked off, no handheld shake — the same morning continuing.

SCENE
The children arrive and the family folds into each other. Four shots, hard cuts. The last happy tableau of the film.

FRAME MAP
[0-3s] Medium shot. @Maeve at the range screen-right, x=60%. @MiloBefore bursts in from the doorway screen-left in cream pyjamas and throws himself into her legs, arms around her, a full-weight hug. Her hand lands on his head.
[3-8s] Medium close on @SamBefore turning toward the doorway, then widening: @NoraBefore in the doorway, x=20%, hair in her face, already smiling as she watches her mother and brother — genuinely happy. @SamBefore opens one arm; she crosses the kitchen and he wraps her in, his chin resting on the top of her head. Both facing the room, not the lens.
[8-10s] Wide ensemble. The whole family alive in one frame: @Maeve and @MiloBefore tangled together screen-right, @SamBefore and @NoraBefore in an embrace screen-left, the plate of charcoal toast smoking gently at the centre of the table. Everyone talking at once, indistinct.
[10-12s] Top-down plate shot of the table: FOUR bowls, FOUR chairs, the bar of window light lying across the wood, the plate of blackened toast at the centre. Nobody in frame.

SUBJECT LOCK, MILO
The exact five-year-old boy of the reference @MiloBefore — cream cotton pyjamas, one lower front tooth missing, dark brown hair. He hugs his mother and does not let go.

SUBJECT LOCK, NORA
The exact twelve-year-old girl of the reference @NoraBefore — pale-blue star-print pyjamas, shoulder-length dark hair, clear healthy skin, bright alert eyes, colour in her cheeks. Smiling before anyone sees her. Visibly, simply happy.

CROSS-FRAME RULES
The same four people, exact faces of their references, same wardrobe throughout. @Kitchen identical to GEN-01: same table, same four chairs, same window direction, same plate of burned toast. The hug in shot two is warm, ordinary and unposed — a father and daughter who do this every day.

LOCATION
@Kitchen, continuing directly from GEN-01.

LIGHT
Same warm gold morning window, no other source.

MOVEMENT
[0-3s] @MiloBefore runs in and slams a hug into @Maeve's legs; she laughs, hand on his head, still holding the spatula.
HARD CUT
[3-8s] @SamBefore turns, sees @NoraBefore in the doorway already smiling; he opens an arm; she crosses; he folds her in, chin on her head; her eyes close for a moment.
HARD CUT
[8-10s] The whole family in one wide frame, everyone talking over everyone, nothing staged, the toast smoking at the centre of the table.
HARD CUT
[10-12s] The empty top-down table: four bowls, four chairs, the light bar, the blackened toast.

DIALOGUE
Aucun — voix indistinctes et chevauchées (brouhaha heureux), aucune parole intelligible.

CAMERA
[0-3s] Medium shot, eye level, static. [3-8s] Medium close then widening, eye level, static. [8-10s] Wide ensemble, eye level, static. [10-12s] Top-down plongée, static.

LAST FRAME
The top-down table: four bowls, four chairs, the bar of light, the blackened toast at centre.
**⚠ CADRE RÉFÉRENT — ce dernier segment (10-12s) est LE cadre décliné en 8.5 (trois bols, une chaise vide, lumière grise) : en extraire une image fixe propre et la conserver.**

AUDIO
Bare feet on tile, the boy's high voice indistinct, overlapping happy voices, the radio, the pan ticking as it cools. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subjects looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, red fruit, red crockery, red packaging, posed family portrait, sitcom lighting, a fifth chair or fifth bowl, generated music.

*Note : le câlin de 3-8s est LE DERNIER câlin du film entre Sam et Nora — après la mort de Maeve il ne la touchera plus jamais. Le jouer simple et quotidien, jamais souligné.*


## GEN-03 — «Le quai» (10 s) — couvre les plans 2.1 → 2.3 du script

**Elements:** @Maeve + @NoraBefore + @Quay (+ figurant unique décrit — sans Élément) · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 10s · sound on
**Style prompt (EN):** Soft overcast late-morning daylight, shadowless and even on every face, wet concrete carrying a dull sheen, smooth tracking dolly moves only, no handheld shake.

**SCENE**
Mother and daughter walk the quay; the mother empties her pocket into a stranger's cup and smiles at him like someone she knows. Three shots, hard cuts.

**FRAME MAP**
[0-3s] @Maeve x=45% and @NoraBefore x=58%, walking, mid-ground, filling 45% of frame height; the ecru tote swinging between them at x=51%; stacked grey and blue lobster traps along the upper half of frame; trawler masts and cranes beyond against a flat pale sky.
[3-7s] The seated stranger screen-left, x=25%, on the ground against the weathered brick warehouse wall, filling 40% of frame height; @Maeve stopped over him at x=52%; @NoraBefore hanging back a step at x=75%.
[7-10s] @Maeve x=40% and @NoraBefore x=62%, chest-up, filling 65% of frame height, walking; the stranger far behind at x=15%, small and soft in anamorphic bokeh.

**SUBJECT LOCK, @MAEVE**
Exact face of the reference. Oatmeal cable-knit sweater under an open grey wool coat, long dark grey skirt, leather boots, thin gold band. **No scarf, nothing red.**

**SUBJECT LOCK, @NORA12**
Exact face of the reference. Navy duffle coat over a grey jumper, dark jeans, off-white canvas sneakers, hair loose in the sea wind, colour in her cheeks.

**SUBJECT LOCK, THE SEATED STRANGER** *(sans Élément — une seule apparition)*
A stranger in his seventies, slight and narrow-shouldered, gaunt, clean-shaven, his calm face fully visible in the flat open daylight; a grey blanket over his legs, a beige cardboard cup held out. He asks nothing, says nothing. Nothing about him resembles a broad bearded fisherman or any other character of the film.

**CROSS-FRAME RULES**
@Quay is the same quay of the reference Element in all three segments — same stacked traps, same brick wall, same flat grey water, same overcast shadowless light. The walk moves in one single direction along the quay for the whole block. The only three people ever in frame are @Maeve, @NoraBefore and the seated stranger; @Maeve and @NoraBefore carry the exact faces of their references in every segment; the stranger is seen full-face, in full light, and appears only in segments 2 and 3. Nobody looks at the lens.

**LOCATION**
@Quay — the working North Atlantic fishing quay of the reference Element: concrete walkway, stacked grey and blue lobster traps, weathered brick warehouse wall, bollards, trawler masts and cranes, flat grey water.

**LIGHT**
Overcast late-morning daylight, soft and shadowless, identical in all three segments; wet concrete underfoot holding a dull sheen.

**MOVEMENT**
[0-3s] @Maeve and @NoraBefore walk the concrete walkway along the traps, one tote handle each, their strides settled into the same rhythm.
HARD CUT
[3-7s] @Maeve stops mid-stride at the seated man. She does not search long: she turns her coat pocket out into his cup — coins, one folded bill — and smiles down at him the way one smiles at someone already known, her head slightly tilted. @NoraBefore hangs back a step, weight on one hip, watching.
HARD CUT
[7-10s] They have taken up their walk again, the tote swinging between them. @NoraBefore twists at the waist to look back over her shoulder toward the man, now small and out of focus far behind, then turns to her mother as she speaks.

**DIALOGUE**
[8.2-9.6s] @NoraBefore, over her shoulder, flat, half a challenge: "You don't even know him."

**CAMERA**
[0-3s] Wide shot, lateral tracking dolly accompanying them at their walking pace.
[3-7s] Medium shot; the dolly eases to a stop exactly when she stops.
[7-10s] Close medium shot in motion, tracking dolly accompanying them.

**LAST FRAME**
The two of them mid-stride, chest-up, @NoraBefore just turned to her mother with the line closing on her mouth, the quay soft behind them.

**AUDIO**
Gulls, halyards slapping the masts, a diesel idling far off, their steps on wet concrete, the coins dropping into cardboard one by one, the folded bill's paper. No music.

**NEGATIVE PROMPT**
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, red buoys, red hulls, red gloves, red traps, a red cup, a red scarf, a beard on the seated man, a broad heavy build on the seated man, the seated man's face hidden or in shadow, generated music

*Note : ⚠ CET HOMME N'EST PAS SAM — silhouette, âge et carrure franchement différents, vu de face, en pleine lumière : le film ne triche jamais ici. GEN-04 reprend la marche de face — le raccord se fait dans le mouvement (mêmes tenues, même lieu, même lumière).*

---

## GEN-04 — «Donne, et tu recevras» (8 s) — couvre le plan 2.4 du script

**Elements:** @Maeve + @NoraBefore + @Quay · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 8s · sound on
**Style prompt (EN):** Soft overcast daylight full on their faces as they walk toward the lens, a steady backwards dolly locked to their pace, no handheld shake.

**SCENE**
The phrase of the film, given in a real moment, walking. One single continuous take — no cut anywhere.

**FRAME MAP**
[0-8s] @Maeve x=45% and @NoraBefore x=58%, chest-up two-shot filling 65% of frame height, walking toward camera for the full duration; the ecru tote swinging between them at the bottom of frame; the port sliding by out of focus behind them.

**SUBJECT LOCK, @MAEVE**
Exact face of the reference. Oatmeal cable-knit sweater under the open grey wool coat, long dark grey skirt, leather boots, thin gold band. **No scarf, nothing red.**

**SUBJECT LOCK, @NORA12**
Exact face of the reference. Navy duffle coat over a grey jumper, dark jeans, off-white canvas sneakers, hair loose in the sea wind.

**CROSS-FRAME RULES**
One single continuous take: no cut, no change of framing. They walk in one single direction the whole shot, at one constant pace. @Quay is the same quay, the same wardrobe and the same overcast light as the previous block. The only people in frame are @Maeve and @NoraBefore, each with the exact face of their reference. Nobody looks at the lens.

**LOCATION**
@Quay — the same working fishing quay of the reference Element, walked along its length.

**LIGHT**
Overcast daylight, soft and shadowless, full on their faces.

**MOVEMENT**
[0-8s] @Maeve answers first with her body — one shoulder lifts and drops, the answer self-evident — and delivers the phrase without slowing down. @NoraBefore, beside her, frowns into it: brows knotting, mouth working on the logic. Then @Maeve looks over at her daughter and takes her time, the corner of her mouth going up before she gives her the last two words. The tote swings between them. No cut anywhere in the take.

**DIALOGUE**
[0.8-2.6s] @Maeve, easy, worn smooth by habit: "Give and you shall receive."
[3.2-4.6s] @NoraBefore, brow knotted: "Receive what?"
[5.8-7.4s] @Maeve, unhurried, a smile in the voice: "You'll see."

**CAMERA**
[0-8s] Close two-shot, steady backwards tracking dolly locked to their exact pace, no shake.

**LAST FRAME**
@Maeve's half-smile landing on her daughter, @NoraBefore still frowning at the answer, both mid-stride, the port soft behind.

**AUDIO**
The port behind them — gulls, rigging, water against the pilings, their steps on wet concrete. No music.

**NEGATIVE PROMPT**
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, red buoys, red hulls, a red scarf, a cut inside the shot, generated music

*Notes : ⚠ LA PHRASE DU FILM — elle appartient à Maeve, elle est dite dans un vrai moment, et elle paie en 17.6 (le sandwich). Un seul plan dans ce bloc : le script interdit tout découpage intérieur de 2.4, et la séquence dépasse 15 s — dérogation assumée à la règle « 2 à 6 plans ».*

---

## GEN-05 — «Eux deux» (12 s) — couvre les plans 5.1 → 5.3 du script

**Elements:** @SamBefore + @Maeve + @LivingRoom · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 12s · sound on
**Style prompt (EN):** A single low lamp with a woven ecru shade is the only source, one warm pool of light, everything beyond its throw falling to near-black, camera locked off or on one very slow continuous dolly, no handheld shake.

**SCENE**
Night. She reads; he mends a net at her feet; he warms her feet under his sweater without a word. Three shots, hard cuts.

**FRAME MAP**
[0-3s] @Maeve in the worn armchair, x=55%, filling 55% of frame height inside the lamp's pool; the lamp screen-left at x=28%, posed low; the dark window upper right holding a faint reflection of the lit chair.
[3-7s] Opens close on @SamBefore's hands centred at x=50% over the verdigris net in the foreground; the slow dolly back ends with @SamBefore seated on the rug, back against the armchair, filling the lower 50% of frame, @Maeve's knees and the edge of her midnight-blue book above him at x=58%.
[7-12s] Wide two-shot: @SamBefore on the rug at x=50% in the lower half, @Maeve above him in the chair at x=56%, the lamp at x=25%; the pool of light holds them both; near-black all around.

**SUBJECT LOCK, @SAMBEFORE**
Exact face of the reference. Grey marl sweatshirt, dark blue jeans, oatmeal wool socks — the reference wardrobe. **Hands clean, no ink anywhere.** The mending cycle is his: wooden netting needle passes, loops, knots, pulls tight — regular, without looking down, his face easy in the half-dark.

**SUBJECT LOCK, @MAEVE**
Exact face of the reference. Reference wardrobe **without the scarf**; barefoot, feet tucked under her then extended to the chair's edge; a midnight-blue clothbound book open in her hands.

**CROSS-FRAME RULES**
@LivingRoom is the same room of the reference Element in all three segments — same single lamp, same armchair, same rug. The lamp is the only source in every frame. The mending cycle keeps the exact same rhythm in segments 2 and 3. In segment 3 neither of them looks at the other and neither says a word. The only people in frame are @SamBefore and @Maeve, each with the exact face of their reference. Nobody looks at the lens.

**LOCATION**
@LivingRoom — the small New England living room at night of the reference Element: worn armchair with a knitted throw, low side table with the single woven-ecru-shade lamp, threadbare rug, bookshelf, dark window reflecting the room.

**LIGHT**
The single lamp, warm and low, is the only source; one warm pool on the chair and the rug; everything beyond falls to near-black.

**MOVEMENT**
[0-3s] @Maeve reads in the armchair, bare feet tucked under her, her eyes travelling the page.
HARD CUT
[3-7s] @SamBefore mends the net without looking down: the needle passes, loops, knots, pulls tight — the same regular cycle again and again, his hands knowing the work by themselves. A page turns over his head as the frame widens.
HARD CUT
[7-12s] Without breaking the mending rhythm, @SamBefore reaches up from the net, catches @Maeve's two bare feet where they hang at the edge of the armchair, and slides them under his sweater, flat against the warmth of his stomach — one continuous, practised movement. Neither looks at the other. Neither says a word. She turns a page; his hands return to the net and the cycle resumes exactly.

**DIALOGUE**
Aucun.

**CAMERA**
[0-3s] Medium shot, locked off.
[3-7s] Close shot on hands, one very slow continuous dolly back widening the frame.
[7-12s] Wide two-shot, locked off.

**LAST FRAME**
The two of them inside the lamp's pool — her feet under his sweater, his hands back on the net mid-knot, her book up; near-black beyond.

**AUDIO**
The house at night — the fridge compressor cycling, a foghorn very far off, the twine hissing through the mesh, the wooden needle, pages turning. No music.

**NEGATIVE PROMPT**
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, a red net, a red lampshade, a red book cover, a red throw, a red scarf, readable book title, ink stains on his fingers, either of them speaking, generated music

*Notes : ⚠ le segment [3-7 s] (5.2) est LE GESTE DU MANTEAU — même main, même point, même rythme, rappel exact en 19.a ; mains propres, l'encre appartient à l'homme d'après. ⚠ Le segment [7-12 s] (5.3) est le PLANT du geste des pieds — payoff en 7.5. LAST FRAME = raccord : GEN-06 reprend ce dispositif en valeurs serrées.*

---

## GEN-06 — «Le regard tenu» (8 s) — couvre les plans 5.4 → 5.5 du script

**Elements:** @SamBefore + @Maeve + @LivingRoom · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 8s · sound on
**Style prompt (EN):** The single lamp warm on one side of each face, deep black behind, locked-off close values only, no handheld shake.

**SCENE**
He looks at her too long; she catches him; the film's quiet declaration. Four shots, hard cuts — segments 1 and 3 share one identical camera set-up.

**FRAME MAP**
[0-2s] Close on @SamBefore from beside the lamp, x=50%, filling 70% of frame height, the net still across his lap at the bottom of frame; warm lamp side-light on the left of his face.
[2-3.4s] Reverse close on @Maeve in the armchair, x=50%, filling 70% of frame height, the midnight-blue book lowering to her chin.
[3.4-5s] Identical framing to segment 1: @SamBefore x=50%, same scale, same angle, same lamp side.
[5-8s] Close-up: @Maeve behind the raised book, the dark cover closing the lower 40% of frame, her eyes and brow above its edge at x=50%.

**SUBJECT LOCK, @SAMBEFORE**
Exact face of the reference. Grey marl sweatshirt, the net across his lap, clean hands, no ink. His eyes come up and stay — long, past politeness, unblinking.

**SUBJECT LOCK, @MAEVE**
Exact face of the reference. Reference wardrobe without the scarf; the midnight-blue clothbound book. In segment 4 her eyes hold the page far too steadily to be reading.

**CROSS-FRAME RULES**
Segments 1 and 3 are the same camera set-up to the pixel — same axis, same scale, same lamp side; only two camera values exist across segments 1 to 3. The book that rises at the end of segment 2 is the same book already in place in segment 4. @LivingRoom, the lamp and the armchair are identical in all four segments. The only people are @SamBefore and @Maeve, each with the exact face of their reference in every segment. Nobody looks at the lens.

**LOCATION**
@LivingRoom — the same room, lamp and armchair as the previous block.

**LIGHT**
The single lamp, warm on one side of each face; the room behind falls to black.

**MOVEMENT**
[0-2s] @SamBefore's hands go still on the net; his eyes come up to @Maeve above him and stay there — long, past politeness, unblinking.
HARD CUT
[2-3.4s] @Maeve feels the look land, lowers the book to her chin, one eyebrow up, and speaks.
HARD CUT
[3.4-5s] @SamBefore answers and does not look away; the look holds through the end of the segment.
HARD CUT
[5-8s] @Maeve behind the raised book: above its edge she is smiling to herself — the smile pushing at her cheeks and narrowing her eyes while they hold the page far too steadily to be reading.

**DIALOGUE**
[2.4-2.9s] @Maeve, book at her chin, one eyebrow up: "What?"
[3.7-4.3s] @SamBefore, quiet, holding the look: "Nothing."

**CAMERA**
[0-2s] Close shot, locked off, from beside the lamp.
[2-3.4s] Reverse close shot, locked off.
[3.4-5s] Close shot, locked off — identical set-up to segment 1.
[5-8s] Close-up, locked off.

**LAST FRAME**
Her eyes above the book's edge, the private smile held, the lamp warm on one side, black behind.

**AUDIO**
The house — a clock somewhere, the fridge; their two voices low and close; a page. No music.

**NEGATIVE PROMPT**
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, a red lampshade, a red book cover, a red scarf, readable book title, a third camera value in the first three segments, generated music

*Note : au mix, **le thème des soirs entre sur le segment final au piano, très bas, pour la première fois du film** — jamais généré.*

---

## GEN-07 — «La lampe des soirs» (8 s) — couvre les plans 4.1 → 4.2 du script

**Elements:** @SamBefore + @NoraBefore + @MiloBefore + @KidsBedroom · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 8s · sound on
**Style prompt (EN):** The bedside lamp itself is the entire source, saturated warm amber blooming up from black as the filament climbs, then taking him three-quarters, warm and frank, the room falling to warm dark behind, camera locked off.

**SCENE**
The lamp clicks on; the father tells it to his children, face on, in full light. Two shots, hard cut.

**FRAME MAP**
[0-2s] Extreme close-up: the bedside lamp's toggle switch centred at x=50%; @SamBefore's thumb entering from frame-right at x=62%; the woven shade filling the upper frame; nothing else in frame.
[2-8s] @SamBefore at the edge of the bed, x=55%, chest-up, filling 65% of frame height, face on, in full lamp light; @NoraBefore and @MiloBefore as soft out-of-focus head shapes under the amber quilt across the lower 25% of frame; the lamp screen-left at x=20%.

**SUBJECT LOCK, @SAMBEFORE**
Exact face of the reference. Grey marl sweatshirt of the reference. **Hands clean, short clean nails, no ink anywhere.** The total seriousness of a man doing the most important work of his day; when the boy interrupts, he answers without breaking register, grave as a judge.

**SUBJECT LOCK, @NORA12 / @MILO5**
Exact faces of their references where visible; under the amber quilt pulled to their chins, soft foreground shapes. @MiloBefore's missing lower front tooth shows when he speaks.

**CROSS-FRAME RULES**
The thumb in segment 1 belongs to the same man as segment 2 — the same clean hand, short clean nail. Same lamp, same woven shade, same amber light in both segments; the lamp is the only source. Segment 1 shows nothing but the thumb, the switch and the lamp — no face. The only people in frame are @SamBefore, @NoraBefore and @MiloBefore. @KidsBedroom is the bedroom of the reference Element. Nobody looks at the lens.

**LOCATION**
@KidsBedroom — the shared children's bedroom of the reference Element: double bed against the papered wall, amber quilt, the bedside lamp with the woven shade, the dark doorway to the hallway.

**LIGHT**
The bedside lamp is the only source: in segment 1 the filament climbs from dull orange to full warm amber and the woven shade prints its texture onto the light; in segment 2 it takes him three-quarters, warm and frank, the room falling to warm dark.

**MOVEMENT**
[0-2s] The thumb pushes the toggle. One dry click; the filament climbs; the amber blooms up from black and fills the frame.
HARD CUT
[2-8s] @SamBefore is in the middle of telling it — leaning in, doing the voices, hands beginning to shape something in the air. The boy interrupts, delighted; @SamBefore answers grave as a judge, not missing a beat, and the children's laughter tumbles over it.

**DIALOGUE**
[2.3-5.0s] @SamBefore, a low telling rumble, dead serious: "…and the wolf had been walking so long his paws had gone soft. Soft like bread."
[5.3-6.3s] @MiloBefore, delighted, through the gap of the missing tooth: "That's disgusting."
[6.4-8.0s] @SamBefore, grave, not missing a beat: "It's extremely disgusting. Don't interrupt."

**CAMERA**
[0-2s] Extreme close-up, locked off.
[2-8s] Close medium shot, locked off, the children as soft out-of-focus foreground.

**LAST FRAME**
@SamBefore leaning into the lamp light, both hands rising toward the lamp, fingers starting to knot into a shape.

**AUDIO**
The dry click, then the small held silence of a room with two children in it; his full voice, two children's laughter tumbling over it, the quilt shifting. No music.

**NEGATIVE PROMPT**
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, red drawings on the wall, a red quilt, a red lampshade, ink stains on the fingers, generated music

*Notes : ⚠ CADRE RÉFÉRENT (4.1) — consigner la composition du segment [0-2 s] au pixel (échelle, angle, position de la main et de la lampe) : **à réutiliser à l'identique en 20.11** (même main, index et majeur tachés d'encre, le sandwich à demi mangé, la lampe éteinte). LAST FRAME = raccord direct vers 4.3 [POST] (les mains nouées devant la lampe). Les plans [POST] 4.3 → 4.5 s'insèrent AU MONTAGE entre ce bloc et GEN-08. Le thème des soirs court très bas au mix.*

---

## GEN-08 — «Le rouge entre» (15 s) — couvre les plans 4.6 → 4.10 du script

**Elements:** @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @KidsBedroom · **Settings:** Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 15s · sound on
**Style prompt (EN):** The bedside lamp is the only source, saturated warm amber, raking; the hallway beyond the doorway near-black; deep warm shadows; camera locked off except one slight steady dolly back on the final segment.

**SCENE**
The girl believes it; the mother watches the man, not the children; the phrase is said like goodnight; the lamp goes out on his voice. Five shots, hard cuts — segments 2 and 4 share one identical doorway set-up.

**FRAME MAP**
[0-3s] @NoraBefore on the pillow, x=48%, her face filling 55% of frame height; the amber quilt at her chin across the lower frame; lamp warmth from screen-left.
[3-7s] The doorway: @Maeve chest-up at the doorframe, x=50%, filling 70% of frame height; **the deep crimson wool scarf over her shoulders — the only red in frame**; the hallway black behind her.
[7-10s] @SamBefore at the bed's edge, x=52%, filling 65% of frame height, one hand raised holding half a shape; the two children as soft shapes under the quilt across the lower 25%; the doorway NOT in this frame.
[10-13s] @Maeve at the doorway, x=50% — the same set-up as segment 2.
[13-15s] Waist-level: @SamBefore at x=45% turning from the bed toward the doorway; @Maeve a dark shape at the doorframe at x=78%, the scarf a last ember of red; the frame ends on black.

**SUBJECT LOCK, @NORA12**
Exact face of the reference. On the pillow, quilt at her chin, completely inside it: lips parted, eyes wide and locked on the wall off frame, the quilt edge forgotten in her fists. **She does not blink once in her segment.**

**SUBJECT LOCK, @MAEVE**
Exact face of the reference. Reference wardrobe **with the deep crimson wool scarf wound over her shoulders — the first red of the film**. Shoulder against the doorframe, arms loosely folded. **Her eyes are on the man by the lamp — on him — never on the children, never on the lens.** The stance of someone with nowhere else she would rather be standing.

**SUBJECT LOCK, @SAMBEFORE**
Exact face of the reference. Grey marl sweatshirt, clean hands, no ink. A man in the middle of the best part of his day, with no idea he is being watched from the doorway.

**SUBJECT LOCK, @MILO5**
A soft shape under the quilt, exact face of the reference where visible.

**CROSS-FRAME RULES**
@KidsBedroom is the same room and the same lamp in all five segments; the lamp is the only source until it dies at the very end. Segments 2 and 4 are the same doorway set-up — same axis, same scale, same raking light. **The crimson scarf is the ONLY red in any frame of this block and appears only in the segments where @Maeve appears; segments 1 and 3 contain no red at all.** The man's voice runs off frame under segments 1 and 2 and the camera never rejoins him during them. Each character carries the exact face of their reference in every segment. Nobody looks at the lens.

**LOCATION**
@KidsBedroom — the same shared bedroom of the reference Element: the bed, the amber quilt, the bedside lamp with the woven shade, the papered wall, the doorway to the dark hallway.

**LIGHT**
The bedside lamp, saturated warm amber: warm and low across @NoraBefore's face on the pillow; reaching @Maeve at a raking angle across the doorway, the hallway behind her black, only the red catching; full and warm on @SamBefore. In the final segment the faint hallway glow dies behind her, then the bedside lamp goes out and the frame drops to black.

**MOVEMENT**
[0-3s] @NoraBefore on the pillow, completely inside it, eyes wide and locked on the wall off frame; she does not blink. Her father's voice continues off frame, low, an indistinct murmur with no distinct words.
HARD CUT
[3-7s] @Maeve stands shoulder-to-doorframe, arms loosely folded, watching the man telling it by the lamp — steady, unhurried. His voice continues off; the camera never rejoins him.
HARD CUT
[7-10s] @SamBefore in full play, one hand still raised holding half a shape, the laugh sitting openly in his face, shoulders loose, leaning into the lamp light; the children's laughter rises from the bottom of frame.
HARD CUT
[10-13s] @Maeve says the evening phrase the way one says goodnight — without thinking about it, already half-turned to go, the words worn round from use. From the bed, off frame, her daughter's answer comes back without a head lifting from the pillow.
HARD CUT
[13-15s] @SamBefore turns from the bed toward the doorway and smiles at her; she returns the smile as the faint hallway glow behind her dies. He is already turning back to the children, picking up exactly where he stopped, when the bedside lamp goes out on his voice and the frame drops to black.

**DIALOGUE**
[10.5-12.0s] @Maeve, offhand, warm, no weight on it: "Give and you shall receive."
[12.2-13.0s] @NoraBefore (off, without lifting her head), automatic, sing-song: "We know, Mom."

**CAMERA**
[0-3s] Close-up, locked off.
[3-7s] Chest-up close shot on the doorway, locked off.
[7-10s] Close medium shot, locked off.
[10-13s] Close shot on the doorway, locked off — identical set-up to segment 2.
[13-15s] Waist-level shot, slight steady dolly back, ending on black.

**LAST FRAME**
Full black — no image; his voice alone carrying into the dark.

**AUDIO**
His voice off, low and indistinct, no intelligible words, under segments 1 and 2; his voice and the children's laughter in segment 3; the two spoken lines in segment 4; the quilt shifting; then his voice continuing in the dark for two full seconds after the light dies. No music.

**NEGATIVE PROMPT**
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red other than the crimson scarf on the woman, red drawings on the wall, a red quilt, a red lampshade, ink stains on his fingers, a lit hallway in segments 2 and 4, the woman looking at the children, a blink from the girl in the first segment, the voice stopping with the light, generated music

*Notes : ⚠ LE ROUGE ENTRE DANS LE FILM au segment [3-7 s] (4.7), sur l'épaule de Maeve — il le quittera en 7.9, sur un geste. Elle ne regarde pas ses enfants : elle le regarde, lui. Fin de bloc = fin de la séquence 4 : la voix continue deux pleines secondes dans le noir, puis coupe franche. Au mix : le piano baisse d'un cran pour elle (segment 4, et pour elle seule), puis le thème s'efface avec la lampe.*

---

## GEN-09 — «La tasse» (8 s) — couvre les plans 6.1 → 6.3 du script

**Elements:** @Maeve + @Kitchen · **Settings:** Genre Noir · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · 8s · sound on
**Style prompt (EN):** The same east kitchen window as the first morning, but under a white sky — the light lies flat and toneless, the hard gold bar gone, colour draining shot by shot, camera locked off throughout.

**SCENE**
A cup slips; a hand stops obeying; she tells no one. Four shots, hard cuts (the middle two are the scripted internal cut of 6.2).

**FRAME MAP**
[0-2s] Insert at counter height: the white porcelain cup and @Maeve's hand centred at x=50%; the tile floor across the lower frame; flat white window light from screen-left.
[2-3.6s] Extreme close-up: @Maeve's raised hand centred at x=50%, filling 60% of frame height, palm toward her.
[3.6-5s] Close-up: @Maeve's face at x=50%, filling 65% of frame height, her eyes down toward the hand below frame.
[5-8s] Wide: @Maeve kneeling small in the lower third at x=45%, filling 35% of frame height; the room's blurred warmth far behind; a small out-of-focus silhouette crossing the hallway at x=80%, unrecognizable.

**SUBJECT LOCK, @MAEVE**
Exact face of the reference wherever her face shows. Fair freckled skin, thin gold band, the reference wardrobe. **No scarf, nothing red, no blood anywhere.** In segment 3 her mouth closes into a flat line and she looks toward the window instead of the door — she tells no one.

**CROSS-FRAME RULES**
@Kitchen is the same kitchen as Act I — same east window direction, same range, same sink — but the light is flat and white and no gold exists anywhere. The hand in segments 1 and 2 is the same hand as the woman in segments 3 and 4. The shards in segment 4 are the same cup from segment 1. The only sharp person in any frame is @Maeve; any background figure stays severely out of focus and unidentifiable. Nobody looks at the lens.

**LOCATION**
@Kitchen — the kitchen of the reference Element, in full flat daylight under a white sky.

**LIGHT**
Flat white window light with no modelling in every segment; the hard gold bar of Act I has disappeared; saturation thinning segment by segment.

**MOVEMENT**
[0-2s] The white cup slips out of her hand and bursts on the tile, shards skating outward. The hand stays where the cup left it, half open. The radio keeps playing, unchanged, indifferent.
HARD CUT
[2-3.6s] The fingers open, then close, then open again — each time a half-beat late on her intent, the thumb not quite meeting the fingertips. Twice.
HARD CUT
[3.6-5s] Her face: eyes down on the hand, held very still, the swallow visible in her throat; then the mouth closes into a flat line and she looks toward the window instead of the door.
HARD CUT
[5-8s] She kneels and gathers the porcelain shards into her open palm one by one, unhurried, precise, her head bowed to the work; far behind her the blurred warmth of the household keeps moving, unaware.

**DIALOGUE**
Aucun — elle ne dit rien à personne.

**CAMERA**
[0-2s] Insert, locked off, at counter height.
[2-3.6s] Extreme close-up, locked off.
[3.6-5s] Close-up, locked off.
[5-8s] Wide shot, locked off, deep focus held only on her.

**LAST FRAME**
@Maeve small and kneeling, the shards gathered in her palm, the household a blur of warmth behind her, the light flat and white.

**AUDIO**
The porcelain bursting, very loud and close; the radio carrying on under it, unchanged; two children's voices arguing somewhere far off; the shards clicking piece by piece into her palm. No music.

**NEGATIVE PROMPT**
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, a red cup, red crockery, any blood, warm golden light, a red scarf, her speaking, a sharp face in the background, generated music

*Note : objectif unique du bloc — 50 mm (le découpage donnait 85 mm sur 6.1/6.2 : un seul réglage par génération ; le 50 tient les inserts ET le plan large de la petite cuisine). La désaturation s'installe : même fenêtre qu'en 1.1, ciel blanc, plus de rai d'or.*

---

## GEN-10 — «Le couloir, deux fois» (11 s) — couvre les plans 6.4 → 6.6 du script

**Elements:** @Sam + @Nora + @Maeve (mains seules) + @HospitalCorridor (+ le médecin décrit au prompt — sans Élément ; la chambre du segment final décrite — sans Élément) · **Settings:** Genre Noir · Camera Fine Film · Lens Anamorphic 85mm f/2 · 21:9 · 1080p · 11s · sound on
**Style prompt (EN):** Green overhead fluorescent tubes doubling in the polished floor, long-lens compression down the corridor, deep desaturated grey-greens, camera locked off, absolute stillness, no handheld shake.

**SCENE**
The same hospital corridor twice — night, then day — then a two-second insert on a packed bag. Three shots, hard cuts; each cut is a scripted time jump.

**FRAME MAP**
[0-2s] Night. @Sam alone on a plastic chair against the wall, x=40%, mid-ground, filling 45% of frame height, leaning far forward; the corridor running away to deep shadow at frame centre; the green tubes doubling in the floor.
[2-9s] Day. Extreme foreground at the left edge, x=12%: the back of @Nora's head and shoulder, soft, out of focus. Ten metres away, compressed by the long lens mid-frame: the doctor at x=46% and @Sam at x=57%, both filling 55% of frame height; the window at the far end of the corridor blown out to white behind them.
[9-11s] Insert on the corner of a bed in a dim adult bedroom: an open soft travel bag centred at x=50% on a plain grey-beige quilt, half packed with folded pale clothing; @Maeve's hands entering from the top of frame; the scarf's crimson the only saturated colour.

**SUBJECT LOCK, @SAM** *(RÈGLE F0 — fiche du présent)*
The bearded, weary man of the reference, exact face: a month-old scruffy salt-and-pepper beard, a fuller face, light shadows under the eyes, slumped shoulders, head carried low. Olive canvas work jacket of the reference. He does not speak at any point.

**SUBJECT LOCK, @NORA**
Back of head and shoulder only, soft and out of focus at the frame edge — dark wavy hair; her face never resolves. **She does not move at all** in her segment.

**SUBJECT LOCK, THE DOCTOR** *(sans Élément — une seule apparition dans le film)*
In his sixties, short grey hair, rimless glasses, a white coat over a grey shirt, a closed folder held against his thigh. He speaks quietly; **no words carry and his lip movements are never readable as words.**

**SUBJECT LOCK, @MAEVE** *(mains seules)*
Fair freckled skin, the thin gold wedding band; framed at the hands and forearms only — her face never in frame.

**CROSS-FRAME RULES**
Segments 1 and 2 are the same corridor of the reference Element — same plastic chairs, same doors, same polished floor — first at night, then in daylight: the cut between them is a scripted time jump and each segment obeys only its own LIGHT block; nothing needs to match across the cut. @Sam is the same man in segments 1 and 2 — same face, same beard, same olive jacket. Segment 3 is a different room, entered on a scripted hard cut; nothing of the corridor appears in it. Every exit sign in the corridor is green. **The scarf's crimson appears ONLY in the final segment and is the only red of the whole block.** Nobody looks at the lens.

**LOCATION**
Segments 1–2: @HospitalCorridor — the corridor of the reference Element: a row of plastic chairs against one wall, closed doors receding, a polished floor, a window at the far end.
Segment 3: a dim adult bedroom — the corner of a bed, a plain grey-beige quilt, a single bedside lamp; no hospital equipment anywhere.

**LIGHT**
[0-2s] Night: the green fluorescent tubes overhead are the only light, doubling in the polished floor; the far end of the corridor falls to shadow.
[2-9s] Day: the same green tubes, flat and pitiless, plus the window at the far end of the corridor blown out to white.
[9-11s] A single bedside lamp, warm but muted; every colour in the frame drained except the scarf's red.

**MOVEMENT**
[0-2s] @Sam sits alone, leaning far forward, elbows on knees, both hands joined and pressed against his mouth. He does not move for the entire segment — the stillness is the event; only his breath moves the joined hands a fraction.
HARD CUT
[2-9s] The doctor speaks quietly to @Sam; no words carry. He stops speaking. @Sam's head goes down, slowly, in one continuous movement. Then the doctor lowers his own eyes, and places one hand on @Sam's shoulder. The hand stays. Neither man moves again for the rest of the segment. @Nora does not move at all.
HARD CUT
[9-11s] @Maeve's hands lower in, last of all, the deep crimson wool scarf, folded with care, smooth it once flat with the palm, and draw the zip closed across it. The shot ends clean on the closed bag.

**DIALOGUE**
Aucun — la conversation du segment [2-9 s] est **visible mais jamais audible**.

**CAMERA**
[0-2s] Wide shot down the corridor's length, locked off.
[2-9s] Long-lens shot from @Nora's position, locked off, absolute stillness; the two men compressed mid-corridor, @Nora soft in the extreme foreground.
[9-11s] Insert, locked off.

**LAST FRAME**
The closed bag on the quilt, the zip drawn shut over the folded red, the hands at rest beside it.

**AUDIO**
The 50 Hz mains hum through both corridor segments; a trolley far off; a phone ringing once in a closed office; **no voices anywhere**; then the bag's hinge of fabric and the zip, full and close. No music.

**NEGATIVE PROMPT**
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subjects looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, audible dialogue, lip movements readable as words, any red anywhere except the folded crimson scarf in the final segment, red exit signage, a fire extinguisher in frame, any blood, name badges, wristbands, readable notice boards, hospital equipment in the bedroom, a face in the final segment, generated music

*Notes : décision de groupage — 6.4 + 6.5 groupés malgré le raccord nuit/jour : saut de temps écrit au script, traité comme le tunnel→arène du « Boxer » du pack (un bloc LIGHT par segment, rien à raccorder à travers la coupe) ; 6.6 (2 s) rejoint sur sa coupe sèche scriptée. Objectif unique 85 mm (le découpage donnait 50 mm sur 6.4) : dérogation assumée pour tenir la compression longue focale de 6.5, le plan maître du bloc — le large de 6.4 devient un large compressé dans l'axe du couloir. ⚠ 6.5 = premier volet du triptyque des conversations muettes (6.5 → 7.7 → 19). Chronologie : Nora a 13 ans ici — de dos, hors foyer, l'écart se joue à la silhouette, pas à une autre fiche. Coupe sèche finale : la séquence 7 reprend le rouge sur les épaules de Maeve.*

---

# [POST] — plans hors blocs (contenu inchangé du découpage fin)

> Les trois plans ci-dessous (11 s) ne sont **pas** regroupés : le mur est généré net de toute
> figure, l'ombre (loup / montagne / oiseau) est **compositée en post depuis l'artwork unique**
> (le même jeu que 18.8 et 19.g). Ils s'insèrent au montage entre GEN-07 et GEN-08.
> Contenu recopié tel quel depuis `docs/plans/PLANS-SEQ-01-05.md`.

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

---

*Fin des séquences 1 → 5 en 10 générations (106 s) + 3 plans [POST] (11 s). Suite : séquence 7 (l'hôpital — blanc froid, vert d'eau, cadre référent absolu 7.7a) dans le lot suivant.*
