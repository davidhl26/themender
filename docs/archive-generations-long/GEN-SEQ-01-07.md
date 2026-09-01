# THE MENDER — GÉNÉRATIONS GROUPÉES · BLOC I — SÉQUENCES 1 → 7

> Blocs de génération du **BLOC I entier** (script v2 : `docs/SCRIPT-THE-MENDER.md`, acte I
> restructuré en **UNE SEULE SOIRÉE**), au format niveau 4 du pack *5 Levels of AI Video
> Prompting* (shot list : SCENE / FRAME MAP / SUBJECT LOCK / CROSS-FRAME RULES / LOCATION /
> LIGHT / MOVEMENT + HARD CUT / DIALOGUE / CAMERA / LAST FRAME / AUDIO / NEGATIVE PROMPT),
> enrichi niveau 5 (@Éléments + réglages Cinema Studio, `docs/PROMPT-PACK-THE-MENDER.md`).
> Le script fait foi. Titres et notes en français ; **tout le contenu générable en anglais**.
>
> **Ce fichier remplace** : `GEN-SEQ-01-05.md` en totalité, et les blocs GEN-01 → GEN-04
> (séquence 7, l'hôpital) de `GEN-SEQ-06-08.md` — repris ici renumérotés GEN-13 → GEN-16.
> `GEN-SEQ-06-08.md` reste la référence pour les séquences 8 (monde gris) et 9 (Anna).

**16 blocs de génération · 173 s générées · ~175 s de script en blocs (séq. 1 légèrement
compressée) · + 11 s en [POST] (4.3, 4.4, 4.5) = ~186 s du BLOC I couvertes**
(sommes plan à plan — séq. 1 : 34 s · séq. 2 : 20 s · séq. 3 : 22 s · séq. 4 : 37 s ·
séq. 5 : 20 s · séq. 6 : 19 s · séq. 7 : 34 s).

## Table de correspondance bloc → plans du script

| Bloc | Titre | Durée gen | Plans couverts | Lieu | Élément(s) |
|---|---|---|---|---|---|
| GEN-01 | «Les toasts brûlés» | 15 s | 1.1 → 1.4 | cuisine, fin de journée | @Kitchen |
| GEN-02 | «Les câlins, et la sortie» | 15 s | 1.5 → 1.8 (incl. 1.7bis) | cuisine, fin de journée | @Kitchen |
| GEN-03 | «La route au couchant» | 8 s | 2.1 → 2.2 | quai, couchant | @Quay (+ mendiant décrit) |
| GEN-04 | «Donne, et tu recevras» | 12 s | 2.3 → 2.5 | quai, crépuscule | @Quay (+ devanture décrite) |
| GEN-05 | «Les quatre assiettes» | 12 s | 3.1 → 3.2 | restaurant | @Restaurant + @Mei |
| GEN-06 | «I love Papa's stories» | 10 s | 3.3 → 3.4 | restaurant | @Restaurant |
| GEN-07 | «La lampe des soirs, et la porte» | 11 s | 4.1 · 4.2 · 4.11 | chambre des enfants | @KidsBedroom |
| GEN-08 | «Le rouge au chambranle» | 15 s | 4.6 → 4.10 | chambre des enfants | @KidsBedroom |
| GEN-09 | «Eux deux» | 12 s | 5.1 → 5.3 | salon | @LivingRoom |
| GEN-10 | «Le regard tenu» | 8 s | 5.4 → 5.5 | salon | @LivingRoom |
| GEN-11 | «La tasse» | 8 s | 6.1 → 6.3 | cuisine, jour blanc | @Kitchen |
| GEN-12 | «Le couloir, deux fois» | 11 s | 6.4 → 6.6 | couloir d'hôpital + insert chambre | @HospitalCorridor |
| GEN-13 | «La chambre : la main, et Milo» | 9 s | 7.1 → 7.2 | chambre d'hôpital | @HospitalRoom |
| GEN-14 | «La chambre : la phrase, le mur, les pieds» | 11 s | 7.3 → 7.5 | chambre d'hôpital | @HospitalRoom |
| GEN-15 ⚠ | «La vitre» | 8 s (→ 2 × 3 s) | 7.7a + 7.7b | couloir, à travers la vitre | @HospitalCorridor + @HospitalRoom |
| GEN-16 | «Le couloir : la porte, Nora, l'écharpe» | 8 s | 7.6 · 7.8 · 7.9 | couloir d'hôpital | @HospitalCorridor |
| [POST] | loup / montagne / oiseau | 11 s | 4.3 · 4.4 · 4.5 | chambre des enfants | @KidsBedroom |

**Ordres de montage à connaître**
- **Séquence 4** : GEN-07 seg. 1-2 (4.1-4.2) → [POST] 4.3-4.5 → GEN-08 (4.6-4.10) →
  GEN-07 seg. 3 (4.11). GEN-07 se génère d'un tenant et s'insère coupé.
- **Séquence 7** : GEN-13 → GEN-14 → GEN-16 seg. 1 (7.6) → **GEN-15** (7.7a/b) →
  GEN-16 seg. 2-3 (7.8, 7.9). GEN-16 se génère d'un tenant et s'insère coupé autour de GEN-15.

**Décisions de groupage à connaître**
- **Séq. 1 (34 s de script) en 2 × 15 s.** 1.5/1.6/1.7 compressés d'environ une seconde chacun ;
  aucune 3e génération possible sans créer un bloc < 8 s.
- **GEN-04 (2.3 + 2.4 + 2.5).** L'échange mère-fille entier (« You don't even know him » →
  « You'll see ») tient dans UNE génération : voix et visages continus. 2.4 reste une prise
  de 7 s sans coupe intérieure ; 2.5 (2 s) rejoint sur sa fin de séquence.
- **GEN-05 : 3.2 porte sa coupe intérieure écrite au script** (« plan rapproché Sam puis
  contrechamp sur les deux enfants ») → deux segments dans le bloc.
- **GEN-07 : 4.11 (3 s) ne peut tenir seul** (règle 8-15 s) ; il rejoint 4.1-4.2 — même chambre,
  même porte — et s'insère au montage après GEN-08 (précédent : GEN-15/GEN-16).
- **GEN-15 : bloc dédié, ne JAMAIS grouper** — cadre référent absolu 7.7a, réutilisé tel quel
  en 20.3.
- **Police du rouge (RÈGLE B).** Le rouge ENTRE en 2.1 (GEN-03, l'écharpe sur Maeve, dehors,
  heureuse) et QUITTE le film en 7.9 (GEN-16 seg. 3). Aucun rouge en séq. 1 (avant l'écharpe),
  ni au restaurant (écharpe et manteaux hors champ — lanternes ambre/laiton, nappes vertes,
  aquarium vert, enseigne = halo ambre jamais lisible), ni en séq. 5. L'écharpe est « encore
  sur les épaules » en 4.7 (GEN-08), pliée dans le sac en 6.6 (GEN-12), sur Maeve à l'hôpital
  (GEN-13/14). Partout ailleurs le négatif l'exclut explicitement.
- **RÈGLE A v2.** *Story/stories* VIT dans l'acte I : la réplique 3.3 de Nora est générée telle
  quelle (GEN-06). Le mot n'apparaît dans aucun autre prompt du lot.
- **Casting (RÈGLE F0 + chronologie figée).** Séq. 1-5 (une seule soirée) : @SamBefore ·
  @Maeve · @NoraBefore (13 ans) · @MiloBefore (6 ans). Séq. 6-7 : **@Sam** (fiche du présent),
  @Maeve (6.1-6.3) puis **@MaeveIll** ; Nora 13 / Milo 6 y sont **joués sur les fiches du
  présent** (costume + coiffure, jamais une nouvelle identité — convention du lot hôpital
  conservée : l'état de la séq. 7 est à l'opposé de la fiche « heureuse » @NoraBefore).
  Le script écrit « 12 ans » en 4.6 par survivance : la chronologie figée dit **13** — on suit 13.
- **Lumière d'une seule soirée.** Or du soir par la fenêtre ouest (séq. 1), couchant doré puis
  bleu du crépuscule (séq. 2), lanternes ambre (séq. 3), lampes chaudes (séq. 4-5). La
  saturation se retire en séq. 6 ; blanc froid / vert d'eau en séq. 7. L'ancienne version
  « matin » des toasts est caduque.
- **Musique.** Un seul thème (« le thème des soirs »), toujours posé AU MIX, jamais généré —
  chaque bloc porte `generated music` au négatif ; les entrées du thème sont signalées en note.

---

## GEN-01 — «Les toasts brûlés» (15 s) — couvre les plans 1.1 → 1.4 du script

**Elements:** @SamBefore + @Maeve + @Kitchen · **Settings:** Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 40mm, f/2.8 · 21:9 · 1080p · 15s · sound on
**Style prompt (EN):** One low west window is the only source, end-of-day sun, warm gold light, a hard bar of light across the table with dust visible in it, the blue of the gas flame under the pan, deep soft shadow in the corners, camera locked off, no handheld shake.

SCENE
A husband and wife tease each other over burned toast in their small kitchen at the end of the day, the sun low and gold in the single window. Four shots, hard cuts. Warm, alive, unposed.

FRAME MAP
[0-3s] Extreme close-up, high angle over the gas range. A cast-iron pan centred, two slices of bread blackening, smoke rising straight. A woman's hand enters from the right and touches one slice with a fingertip, snatches back.
[3-7s] Medium two-shot. @Maeve at the range screen-right, x=65%, barefoot, still laughing. @SamBefore seated at the table screen-left, x=30%, a bowl in front of him, looking up at her.
[7-12s] Medium close two-shot at the table. @Maeve slides the blackened toast onto a plate and sets it in front of @SamBefore with mock ceremony, then points a finger at him, mock-stern. He looks down at the plate, then up at her.
[12-15s] Waist-level two-shot, one framing, no coverage. @SamBefore stands, catches @Maeve by the waist and kisses her neck. She protests for form's sake, laughing, and keeps laughing. He keeps his face in her neck one second too long.

SUBJECT LOCK, @MAEVE
The exact woman of the reference — dark auburn wavy hair, grey-green eyes, freckles, oatmeal cable-knit sweater with pushed-up sleeves, dark grey long skirt, barefoot, thin gold wedding band. **No scarf in this block, nothing red.** Laughing easily through the whole block. She never looks at the lens.

SUBJECT LOCK, @SAMBEFORE
The exact man of the reference — upright, solid, short neat dark brown hair, short trimmed salt-and-pepper beard, pale grey-blue eyes, clean hands, grey marl sweatshirt. Dry deadpan humour breaking into a smile. He never looks at the lens.

CROSS-FRAME RULES
The same two people in all four shots, exact faces of their references, same wardrobe throughout. @Kitchen is the same kitchen in all four shots: same table, same four mismatched chairs, same window direction, same crockery. The light comes from the same low west window in every shot — low, gold, end of day. The pan and the burned toast persist across the cuts.

LOCATION
@Kitchen — the worn wooden table under the window, gas range with the cast-iron pan, cream and blue crockery, cluttered counter, small radio playing low.

LIGHT
Warm gold late-day sun through the single window, low and raking, dust in the beam, blue gas flame under the pan, no other source.

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
The two of them in one frame at the table, his face in her neck, her head tipped back laughing, the plate of burned toast in the lower third, the low gold bar of window light across the table.

AUDIO
The pan sizzling, her fingertip on the toast, a real laugh, the radio low in the room, the plate set on wood, their two voices warm and quick, her laughter under the kiss. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subjects looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, red fruit, red kettle, red crockery, red packaging, posed smiles, sitcom lighting, morning light, cold daylight, generated music.

*Note : ⚠ PREMIER PLAN DU FILM (1.1) — la main qui touche la nourriture ratée par amour répond au dernier plan (20.10, la main qui tient le sandwich). Acte I = une seule soirée : soleil bas plein ouest — l'ancienne version « matin » est caduque. Grille-pain absent du décor @Kitchen : ne pas en faire apparaître un.*

---

## GEN-02 — «Les câlins, et la sortie» (15 s) — couvre les plans 1.5 → 1.8 du script (incl. 1.7bis)

**Elements:** @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @Kitchen · **Settings:** Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 40mm, f/2.8 · 21:9 · 1080p · 15s · sound on
**Style prompt (EN):** Same single west window, warm gold end-of-day sun, dust in the beam, camera locked off, no handheld shake — the same evening continuing.

SCENE
The children arrive, the family folds into each other, the father proposes eating out, and the laid table stays behind, untouched. Six shots, hard cuts. The last happy tableau of the film.

FRAME MAP
[0-3s] Medium shot. @Maeve at the range screen-right, x=60%. @MiloBefore bursts in from the doorway screen-left in cream pyjamas and throws himself into her legs, arms around her, a full-weight hug. Her hand lands on his head.
[3-7.5s] Medium close on @SamBefore turning toward the doorway, then widening: @NoraBefore in the doorway, x=20%, hair in her face, already smiling as she watches her mother and brother — genuinely happy. @SamBefore opens one arm; she crosses the kitchen and he wraps her in, his chin resting on the top of her head. Both facing the room, not the lens.
[7.5-9.5s] Wide ensemble. The whole family alive in one frame: @Maeve and @MiloBefore tangled together screen-right, @SamBefore and @NoraBefore in an embrace screen-left, the plate of charcoal toast smoking gently at the centre of the table. Everyone talking at once, indistinct.
[9.5-11.5s] Close on @SamBefore, x=50%. He looks at the charred toast, then at his wife, then at the children — and proposes.
[11.5-13s] Wide family shot. The children erupt with joy — @MiloBefore throws both arms straight up; @NoraBefore lights up; @Maeve laughs and throws the tea towel across @SamBefore's shoulder.
[13-15s] Top-down shot of the table: FOUR bowls, FOUR chairs, the table laid and untouched, the plate of blackened toast smoking at the centre, the low gold bar of window light across the wood. Nobody in frame.

SUBJECT LOCK, @MILOBEFORE
The exact six-year-old boy of the reference — cream cotton pyjamas, one lower front tooth missing, dark brown hair with its cowlick. He hugs his mother and does not let go; in shot five both his arms shoot straight up.

SUBJECT LOCK, @NORABEFORE
The exact thirteen-year-old girl of the reference — pale-blue star-print pyjamas, shoulder-length dark hair, clear healthy skin, bright alert eyes, colour in her cheeks. Smiling before anyone sees her. Visibly, simply happy.

CROSS-FRAME RULES
The same four people, exact faces of their references, same wardrobe throughout. @Kitchen identical to GEN-01: same table, same four chairs, same window direction, same plate of burned toast, same low gold light. The hug in shot two is warm, ordinary and unposed — a father and daughter who do this every day. The laid table in shot six is the same table seen in every other shot, untouched.

LOCATION
@Kitchen, continuing directly from GEN-01.

LIGHT
Same warm gold end-of-day window, low and raking, no other source.

MOVEMENT
[0-3s] @MiloBefore runs in and slams a hug into @Maeve's legs; she laughs, hand on his head, still holding the spatula.
HARD CUT
[3-7.5s] @SamBefore turns, sees @NoraBefore in the doorway already smiling; he opens an arm; she crosses; he folds her in, chin on her head; her eyes close for a moment.
HARD CUT
[7.5-9.5s] The whole family in one wide frame, everyone talking over everyone, nothing staged, the toast smoking at the centre of the table.
HARD CUT
[9.5-11.5s] @SamBefore looks at the charred toast, then at his wife, then at his children, and delivers the proposal — flat, then breaking into a smile.
HARD CUT
[11.5-13s] The two children erupt at once — @MiloBefore's arms shoot up; @Maeve laughs and flings the tea towel onto @SamBefore's shoulder; the room turns toward the door.
HARD CUT
[13-15s] The empty top-down table: four bowls, four chairs, laid and untouched, the toast smoking, the light bar. The happy hubbub recedes off frame; a door.

DIALOGUE
[9.9-11.3s] @SamBefore, looking from the toast to his wife to the kids, flat then warming: "Or… we eat out tonight."

CAMERA
[0-3s] Medium shot, eye level, static. [3-7.5s] Medium close then widening, eye level, static. [7.5-9.5s] Wide ensemble, eye level, static. [9.5-11.5s] Close shot, eye level, static. [11.5-13s] Wide shot, eye level, static. [13-15s] Top-down plongée, static.

LAST FRAME
The top-down laid table: four bowls, four chairs, the low gold bar of light, the blackened toast smoking at centre — untouched, nobody in frame.

AUDIO
Bare feet on tile, the boy's high voice indistinct, overlapping happy voices, the radio, his line, two children shrieking with joy at once, @Maeve's laugh, the towel landing on cloth; then the hubbub receding, a door closing, the pan ticking as it cools. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subjects looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, red fruit, red crockery, red packaging, posed family portrait, sitcom lighting, a fifth chair or fifth bowl, anyone eating at the table, generated music.

*Notes : ⚠ le câlin de [3-7.5 s] est LE DERNIER câlin du film entre Sam et Nora — après la mort de Maeve il ne la touchera plus jamais ; le jouer simple et quotidien, jamais souligné. ⚠ CADRE RÉFÉRENT 1.8 — segment final [13-15 s] : LA TABLE DRESSÉE, INTACTE — personne n'y mangera ce soir. En extraire une image fixe propre et la conserver : elle est déclinée par édition d'image en 8.5 (trois bols, une chaise vide, ciel blanc, rai disparu — jamais regénérée).*

---

## GEN-03 — «La route au couchant» (8 s) — couvre les plans 2.1 → 2.2 du script

**Elements:** @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @Quay (+ le mendiant décrit — sans Élément) · **Settings:** Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 40mm, f/2.8 · 21:9 · 1080p · 8s · sound on
**Style prompt (EN):** Low golden sunset along the quay, masts and rigging in backlight against the warm sky, long warm shadows across the concrete, faces catching the last of the sun, a smooth lateral tracking dolly that stops when she stops, no handheld shake.

SCENE
The whole family walks the quay toward dinner at sunset; the mother empties her pocket into a stranger's cup and smiles at him like someone she knows. Two shots, hard cut.

FRAME MAP
[0-4s] Wide lateral tracking shot: the family mid-ground, filling 45% of frame height, walking screen-left to screen-right — @SamBefore x=32% with @MiloBefore riding on his shoulders (their stacked silhouette breaking the skyline), @Maeve x=52% with **the deep crimson wool scarf over her shoulders — the only red in frame**, @NoraBefore x=64% in step beside her mother; stacked grey and blue lobster traps across the lower right; trawler masts and cranes in backlight against the golden sky in the upper half.
[4-8s] Medium shot: the seated stranger screen-left, x=25%, on the ground against the weathered brick warehouse wall, filling 40% of frame height, his face to camera in full warm light; @Maeve stopped over him at x=55%; @SamBefore with @MiloBefore and @NoraBefore walking on, soft in the background at x=80%.

SUBJECT LOCK, @MAEVE
Exact face of the reference. Oatmeal cable-knit sweater under an open grey wool coat, long dark grey skirt, leather boots, thin gold band — and **the deep crimson wool scarf loosely wound over her shoulders: the first red of the film, and the only red in any frame of this block.** Happy, unhurried, outdoors.

SUBJECT LOCK, @SAMBEFORE
Exact face of the reference. A dark navy wool peacoat open over the grey marl sweatshirt, dark jeans. @MiloBefore rides on his shoulders; @SamBefore's hands stay locked around the boy's shins for every frame they appear in.

SUBJECT LOCK, @NORABEFORE
Exact face of the reference, thirteen, radiant. A navy duffle coat open over the mustard-and-cream striped top, hair loose in the sea wind, colour in her cheeks.

SUBJECT LOCK, @MILOBEFORE
Exact face of the reference, six, the missing lower front tooth. A small navy wool coat over the green-and-navy striped top. On his father's shoulders, fists in his father's hair, babbling non-stop, delighted.

SUBJECT LOCK, THE SEATED STRANGER *(sans Élément — une seule apparition)*
A stranger in his seventies, slight and narrow-shouldered, gaunt, clean-shaven, his calm face **fully visible, facing the camera, in the full warm sunset light**; a grey blanket over his legs, a beige cardboard cup set on the ground before him. He asks nothing, says nothing. Nothing about him resembles a broad bearded fisherman or any other character of the film.

CROSS-FRAME RULES
@Quay is the same quay of the reference Element in both shots — same stacked traps, same brick wall, same masts — under the same low sunset light. The walk moves in one single direction along the quay. The only five people ever in frame are the four family members and the seated stranger, each family face exact to its reference; the stranger is seen full-face, in full light, and appears only in shot two. The crimson scarf on @Maeve is the only red in any frame. Nobody looks at the lens.

LOCATION
@Quay — the working North Atlantic fishing quay of the reference Element: concrete walkway, stacked grey and blue lobster traps, weathered brick warehouse wall, bollards, trawler masts and cranes, flat water holding the sunset.

LIGHT
Low golden sunset, warm and raking, masts in backlight, long shadows; the stranger's face taken full and warm by the low sun.

MOVEMENT
[0-4s] The family walks the quay into the low sun. @MiloBefore rides his father's shoulders, fists in his hair, babbling; @NoraBefore falls into step with her mother; the scarf lifts in the sea wind.
HARD CUT
[4-8s] @Maeve slows and stops at the seated man. She does not search long: she turns her coat pocket out into his cup — coins, one folded bill — and smiles down at him the way one smiles at someone already known, her head slightly tilted. He looks up at her into the low sun. The others drift on a few steps, soft behind; @NoraBefore hangs back, watching.

DIALOGUE
Aucun — le babil de Milo reste indistinct, aucune parole intelligible.

CAMERA
[0-4s] Wide shot, lateral tracking dolly accompanying them at their walking pace, eye level.
[4-8s] Medium shot; the dolly eases to a stop exactly when she stops.

LAST FRAME
@Maeve bent slightly toward the cup, her smile landing on the man's upturned, fully lit face, the crimson scarf the one line of red in the gold, the family soft beyond her shoulder.

AUDIO
Gulls, halyards slapping the masts, their steps on the concrete, Milo's high babble, the coins dropping into cardboard one by one, the folded bill's paper. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red other than the crimson scarf on the mother, red buoys, red hulls, red traps, red gloves, a red cup, a beard on the seated man, a broad heavy build on the seated man, the seated man's face hidden or in shadow, overcast flat light, generated music.

*Notes : ⚠ LE ROUGE ENTRE DANS LE FILM (2.1) — l'écharpe sur les épaules de Maeve, dehors, en mouvement, heureuse ; il ne quittera le film qu'en 7.9 (GEN-16). ⚠ CET HOMME N'EST PAS SAM — silhouette, âge et carrure franchement différents, vu de face, en pleine lumière : le film ne triche jamais ici.*

---

## GEN-04 — «Donne, et tu recevras» (12 s) — couvre les plans 2.3 → 2.5 du script

**Elements:** @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @Quay (+ la devanture du restaurant décrite — sans Élément) · **Settings:** Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 40mm, f/2.8 · 21:9 · 1080p · 12s · sound on
**Style prompt (EN):** The last of the sunset dying into blue dusk along the quay, warm low light full on their faces in the first two segments, the lit shopfront's amber halo the warmest thing in the final wide, steady dolly moves locked to their pace, no handheld shake.

SCENE
The daughter challenges the gift; the mother answers with the phrase of the film, walking; at the quay's end the restaurant window lights up and the family goes in. Three shots, hard cuts — the whole mother-daughter exchange lives inside this one generation.

FRAME MAP
[0-3s] Walking close shot: @Maeve x=40% and @NoraBefore x=55%, chest-up, filling 60% of frame height, walking; @NoraBefore twisting at the waist to look back over her shoulder; the seated man tiny and soft far behind at x=15%; @SamBefore and @MiloBefore ahead, soft at the frame edge x=85%.
[3-10s] Close two-shot walking toward camera: @Maeve x=45% and @NoraBefore x=58%, chest-up, filling 65% of frame height, walking toward the lens for the full segment; behind and between them, soft in anamorphic bokeh at x=75%, @SamBefore with @MiloBefore on his shoulders.
[10-12s] Wide static shot: the quay's end in blue dusk; the small restaurant shopfront screen-right, x=68%, its window coming alight — an amber halo, no readable sign; the family small at x=55%, crossing to it; the crimson scarf one small line of red at the door.

SUBJECT LOCK, @MAEVE
Exact face of the reference. Grey wool coat open over the oatmeal sweater, **the deep crimson scarf over her shoulders — the only red in any frame**. She answers first with her body: one shoulder lifts and drops, the answer self-evident.

SUBJECT LOCK, @NORABEFORE
Exact face of the reference, thirteen. Navy duffle coat, hair loose in the sea wind. She frowns into the answer: brows knotting, mouth working on the logic — a challenge, not a sulk.

SUBJECT LOCK, @SAMBEFORE / @MILOBEFORE
Exact faces of their references where they resolve; mostly soft background shapes — the father pretending to drop the boy from his shoulders and catching him, the boy howling with laughter.

CROSS-FRAME RULES
@Quay is the same quay, the same wardrobe and the same dying sunset as the previous block; by segment three the sun is gone and the dusk is blue. They walk in one single direction the whole block. The only five people in frame are the four family members and, in segment one only, the distant seated man. The crimson scarf on @Maeve is the only red in any frame. Segment two is one continuous take with no cut inside it. Nobody looks at the lens.

LOCATION
@Quay — the same working fishing quay, walked to its end; at the end, a small old family-run Chinese restaurant shopfront: wood-framed window, a roller blind half up, warm amber light coming on inside, a hanging sign reduced to a soft amber halo, never readable.

LIGHT
Segments one and two: the last warm sunset light full on their faces as they walk toward it. Segment three: blue dusk, the sun gone; the shopfront's amber glow is the warmest source in the frame.

MOVEMENT
[0-3s] They have taken up the walk again. @NoraBefore twists to look back toward the man far behind, then turns to her mother with the line.
HARD CUT
[3-10s] @Maeve gives the phrase without slowing down. @NoraBefore frowns into it and pushes back. @Maeve looks over at her daughter and takes her time, the corner of her mouth going up before she gives her the last two words. Behind them, soft, @SamBefore pretends to drop @MiloBefore and catches him; the boy howls with laughter. No cut anywhere in the segment.
HARD CUT
[10-12s] At the quay's end the restaurant window flickers alight — an amber halo in the blue. The family crosses to it and the door takes them in one by one; the doorbell rings once.

DIALOGUE
[0.8-2.2s] @NoraBefore, over her shoulder, flat, half a challenge: "You don't even know him."
[3.6-5.2s] @Maeve, easy, worn smooth by habit: "Give and you shall receive."
[5.8-6.8s] @NoraBefore, brow knotted: "Receive what?"
[8.0-9.4s] @Maeve, unhurried, a smile in the voice: "You'll see."

CAMERA
[0-3s] Close shot in motion, lateral tracking dolly at their pace.
[3-10s] Close two-shot, steady backwards tracking dolly locked to their exact pace, no shake.
[10-12s] Wide shot, locked off.

LAST FRAME
The lit shopfront amber in the blue dusk, the door just closed on the family, the quay empty, masts black against the last of the light.

AUDIO
The port behind them — gulls settling, rigging, water against the pilings, their steps; Milo's laughter behind the lines; then the doorbell and a wash of warm room sound as the door opens and shuts. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red other than the crimson scarf on the mother, red buoys, red hulls, a red sign, a red lantern in the window, readable lettering on the shopfront, a cut inside segment two, generated music.

*Notes : ⚠ LA PHRASE DU FILM (2.4) — elle appartient à Maeve, dite dans un vrai moment, en marchant ; elle paie en 17.6, le sandwich. L'échange entier tient dans UNE génération pour la continuité des voix et des visages. L'enseigne n'est jamais lisible : un halo ambre (RÈGLE « TEXTE À L'ÉCRAN »).*

---

## GEN-05 — «Les quatre assiettes» (12 s) — couvre les plans 3.1 → 3.2 du script

**Elements:** @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @Mei + @Restaurant · **Settings:** Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 40mm, f/2.8 · 21:9 · 1080p · 12s · sound on
**Style prompt (EN):** Amber paper lanterns and brass are the sources, warm low light pooling on the faces, the fish tank throwing green at the frame edge, the street cold and blue beyond the half-fogged window, camera locked off.

SCENE
The owner sets four plates without being asked — she knows them; the father performs the dragon story and the children detonate. Three shots, hard cuts (the second cut is the scripted internal cut of 3.2).

FRAME MAP
[0-4s] Medium shot on the table from the room: the green-clothed table; @Mei leaning in from the left foreground amorce, x=15%, setting FOUR plates one by one; @SamBefore nearest camera in three-quarter back amorce screen-left, x=30%; @Maeve at the table's end, x=50%; @NoraBefore x=62% and @MiloBefore x=76% side by side facing camera; amber lanterns above; the green-lit fish tank at the right edge, x=92%.
[4-9s] Close on @SamBefore from the children's side, x=50%, filling 70% of frame height: both hands raised as a dragon's jaws, two wooden chopsticks held as moustaches under his nose, lantern light warm on his face.
[9-12s] Countershot on the two children: @MiloBefore x=40% and @NoraBefore x=64%, chest-up, filling 65% of frame height; the table edge and the four plates across the lower frame.

SUBJECT LOCK, @MEI
The exact woman of the reference — white cotton shirt, long dark green apron, jade bangle, the lacquered wooden hairpin in the low bun. She sets four plates, one to each person, in one sure unbroken rhythm — the gesture of someone who has done it for years and knows this family. She smiles at them, exchanges two silent words with @Maeve (lips moving, nothing audible), and goes. She never looks at the lens.

SUBJECT LOCK, @SAMBEFORE
Exact face of the reference; grey marl sweatshirt, the peacoat off and out of frame. Total commitment to the performance: hands as jaws, chopstick moustaches, a ridiculous domestic growl — a very bad dragon voice delivered dead serious.

SUBJECT LOCK, @MAEVE
Exact face of the reference; oatmeal sweater. **Coat and scarf off and out of frame — nothing red anywhere in this block.**

SUBJECT LOCK, @NORABEFORE / @MILOBEFORE
Exact faces of their references, coats off. @MiloBefore, six, the missing tooth showing: pure delight, both hands ready to bang the table. @NoraBefore, thirteen: laughing a real child's laugh, head thrown back.

CROSS-FRAME RULES
@Restaurant is the same room in all three shots: same green tablecloths, same amber-and-brass paper lanterns, same green fish tank, same half-fogged window onto the blue night. The four plates set in shot one sit on the table in shots two and three. The only five people ever in frame are the four family members and @Mei; the rest of the room stays soft and unpeopled. Every family face exact to its reference. Nobody looks at the lens.

LOCATION
@Restaurant — the small old family-run Chinese restaurant of the reference Element: formica tables with dark green cloths, lacquered counter, the green-lit fish tank, the beaded curtain to the kitchen, paper lanterns in amber and brass, the window onto the wet street with its half-drawn blind.

LIGHT
Warm low amber from the lanterns and the counter on every face; the fish tank throwing green at the frame edge; the street beyond the fogged glass cold and blue. No red light anywhere.

MOVEMENT
[0-4s] @Mei leans in and sets the four plates one-two-three-four, one per person, a settled habit; she smiles at the family, trades two silent words with @Maeve, and withdraws. The family is already leaning in, mid-conversation.
HARD CUT
[4-9s] @SamBefore builds the story with his whole body: the hands rise into a dragon's jaws, the chopsticks become moustaches, he growls — badly, twice — and lands the line at full volume.
HARD CUT
[9-12s] @MiloBefore erupts, banging the table with both hands, shouting his confession; @NoraBefore laughs with her head thrown back; the plates jump.

DIALOGUE
[5.5-8.5s] @SamBefore, a terrible dragon voice, loud, dead serious: "…and the dragon said: WHO ATE MY NOODLES?"
[9.3-11.4s] @MiloBefore, howling with joy, banging the table: "ME! IT WAS ME!"

CAMERA
[0-4s] Medium shot, eye level, locked off.
[4-9s] Close shot, eye level, locked off.
[9-12s] Countershot close two-shot, eye level, locked off.

LAST FRAME
The two children mid-laughter — Milo's arms up off the banged table, Nora's head thrown back — warm lantern light full on both faces, the four plates in the lower frame.

AUDIO
The room low — chopsticks, crockery, the kitchen far off behind the beaded curtain; the four plates set down one by one; his dragon voice; then the two children's laughter over everything — the loudest table in the restaurant. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, red lanterns, red tablecloths, red menus, red chopsticks, red packaging, a red scarf, red aquarium decor, other diners in frame, generated music.

*Note : ⚠ CADRE RÉFÉRENT ÉMOTIONNEL (3.1) — les QUATRE assiettes posées d'office, une par personne : c'est ce geste que Mei retiendra en 10.2 (quatre tasses par habitude… et elle en retire une). Conserver une image nette du geste des quatre assiettes.*

---

## GEN-06 — «I love Papa's stories» (10 s) — couvre les plans 3.3 → 3.4 du script

**Elements:** @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @Restaurant · **Settings:** Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 40mm, f/2.8 · 21:9 · 1080p · 10s · sound on
**Style prompt (EN):** The same amber lanterns warm on the faces, the half-fogged window holding the blue harbour night behind the table, camera locked off except one very slow continuous forward dolly in the final segment.

SCENE
The daughter tells her mother she loves her father's stories; the mother files the moment away; the whole table dissolves into the happiest laughter of the film. Two shots, hard cut.

FRAME MAP
[0-5s] Close two-shot: @NoraBefore x=42% leaning toward @Maeve x=62% at the table's end, both chest-up, filling 70% of frame height; beyond them, soft in anamorphic bokeh at x=85%, @SamBefore mid-dragon, hands still up.
[5-10s] Ensemble of the table: all four in frame — @SamBefore x=30%, @Maeve x=48%, @NoraBefore x=62%, @MiloBefore x=78% — filling the middle band of the frame; behind and above them the half-fogged window holds the blue night of the port across the upper half.

SUBJECT LOCK, @NORABEFORE
Exact face of the reference, thirteen. She leans toward her mother and speaks **without taking her eyes off her father** — warm, simple, no solemnity.

SUBJECT LOCK, @MAEVE
Exact face of the reference, nothing red on her. **MAEVE SMILES:** she looks at her daughter, then at her husband in full performance, and says nothing — the look of someone putting the moment away somewhere safe.

SUBJECT LOCK, @SAMBEFORE / @MILOBEFORE
Exact faces of their references. @SamBefore keeps the dragon going soft in the background of shot one, then lets it die in shot two into open laughter; @MiloBefore laughs himself breathless.

CROSS-FRAME RULES
@Restaurant, the table, the green cloth and the four plates are identical to the previous block; the lanterns are the same sources. Coats and the scarf stay out of frame — no red anywhere. The only four people in frame are the family. In shot one @SamBefore stays soft and out of focus; the camera moves only in shot two, one very slow forward dolly, nothing else. Nobody looks at the lens.

LOCATION
@Restaurant — the same table by the half-fogged window onto the blue night of the port.

LIGHT
Warm amber lantern light on the four faces; the fogged pane behind them holding the cold blue night; the fish tank's green kept to the frame edge.

MOVEMENT
[0-5s] @NoraBefore leans to her mother and says it, eyes still on her father. @Maeve smiles — at her daughter, then across at the man mid-performance — and says nothing. She just keeps it.
HARD CUT
[5-10s] The whole table, four faces in the warm light, the dragon dying into a shared fit of laughter — Milo breathless, Nora wiping her eyes, Sam surrendering, Maeve laughing with them. The camera eases forward, very slowly, toward the table. Behind the fogged glass, the blue night of the port.

DIALOGUE
[1.2-3.0s] @NoraBefore, leaning to her mother, eyes on her father, warm and simple: "I love Papa's stories."

CAMERA
[0-5s] Close two-shot, eye level, locked off.
[5-10s] Ensemble of the table, eye level, one very slow continuous forward dolly — the only camera movement of the block.

LAST FRAME
The four of them mid-laugh inside the amber light, the fogged pane behind holding the blue harbour night — the happiest frame of the film.

AUDIO
His dragon voice soft at a distance under shot one; the laughter of all four filling shot two — the happiest sound of the film; the room low, the far kitchen, a chopstick set down. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, red lanterns, red tablecloths, red menus, a red scarf, other diners in frame, a camera move in the first segment, generated music.

*Notes : ⚠ RÈGLE A (version 2) — « stories » VIT dans l'acte I : cette réplique est générée telle quelle. C'est le plant : elle a dit à sa mère qu'elle aimait les histoires de son père — le Mender lui en écrira mille. Le mot meurt avec Maeve (séq. 8 à 19) et ne revient qu'en 20. ⚠ 3.4 = LE plan que le spectateur reverra mentalement en 10.1, quand ils seront trois derrière la même vitre — conserver le cadre.*

---

## GEN-07 — «La lampe des soirs, et la porte» (11 s) — couvre les plans 4.1 · 4.2 · 4.11 du script

**⚠ Montage : les plans [POST] 4.3 → 4.5 puis GEN-08 (4.6 → 4.10) s'insèrent ENTRE les
segments 2 et 3 de ce bloc. GEN-07 se génère d'un tenant et s'insère coupé.**

**Elements:** @SamBefore + @NoraBefore + @MiloBefore + @KidsBedroom · **Settings:** Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 40mm, f/2.8 · 21:9 · 1080p · 11s · sound on
**Style prompt (EN):** The bedside lamp itself is the entire source, saturated warm amber blooming up from black as the filament climbs, then taking him three-quarters, warm and frank, the room falling to warm dark behind; in the final segment the room is dark and the only light is a thin warm ray from the hallway under the door; camera locked off.

SCENE
The lamp clicks on; the father tells it to his children, face on, in full light; and much later, the story over, he slips out and closes the door. Three shots, hard cuts.

FRAME MAP
[0-2s] Extreme close-up: the bedside lamp's toggle switch centred at x=50%; @SamBefore's thumb entering from frame-right at x=62%; the woven shade filling the upper frame; nothing else in frame.
[2-8s] @SamBefore at the edge of the bed, x=55%, chest-up, filling 65% of frame height, face on, in full lamp light; @NoraBefore and @MiloBefore as soft out-of-focus head shapes under the amber quilt across the lower 25% of frame; the lamp screen-left at x=20%.
[8-11s] The closed side of the bedroom door seen from inside the dark room, centred, x=50%, filling most of the frame; a thin warm line of hallway light under it across the lower frame.

SUBJECT LOCK, @SAMBEFORE
Exact face of the reference. Grey marl sweatshirt of the reference. **Hands clean, short clean nails, no ink anywhere.** The total seriousness of a man doing the most important work of his day; when the boy interrupts, he answers without breaking register, grave as a judge. In segment three he is a dark shape only, no face readable.

SUBJECT LOCK, @NORABEFORE / @MILOBEFORE
Exact faces of their references where visible; under the amber quilt pulled to their chins, soft foreground shapes. @MiloBefore's missing lower front tooth shows when he speaks.

CROSS-FRAME RULES
The thumb in segment 1 belongs to the same man as segments 2 and 3 — the same clean hand, short clean nail. Same lamp, same woven shade, same room in all three segments; the lamp is the only source in segments 1 and 2 and is off in segment 3. Segment 1 shows nothing but the thumb, the switch and the lamp — no face. The only people in frame are @SamBefore, @NoraBefore and @MiloBefore. @KidsBedroom is the bedroom of the reference Element; the door in segment 3 is the doorway of that same room. Nobody looks at the lens.

LOCATION
@KidsBedroom — the shared children's bedroom of the reference Element: double bed against the papered wall, amber quilt, the bedside lamp with the woven shade, the doorway to the hallway.

LIGHT
Segments 1-2: the bedside lamp is the only source — the filament climbs from dull orange to full warm amber, the woven shade prints its texture onto the light; it takes him three-quarters, warm and frank, the room falling to warm dark. Segment 3: the room is dark; the only light is the thin warm ray of the hallway under the door, and briefly the soft rectangle of the dim hallway as the door opens and closes.

MOVEMENT
[0-2s] The thumb pushes the toggle. One dry click; the filament climbs; the amber blooms up from black and fills the frame.
HARD CUT
[2-8s] @SamBefore is in the middle of telling it — leaning in, doing the voices, hands beginning to shape something in the air. The boy interrupts, delighted; @SamBefore answers grave as a judge, not missing a beat, and the children's laughter tumbles over it.
HARD CUT
[8-11s] The story is over; the room is dark, the children asleep. Off frame, one soft click — the last amber dies. His dark shape crosses the frame without a sound, opens the door onto the dim hallway, slips through, and closes it to a soft click of the latch. The frame stays on the closed door and the thin ray beneath it, one second too long.

DIALOGUE
[2.3-5.0s] @SamBefore, a low telling rumble, dead serious: "…and the wolf had been walking so long his paws had gone soft. Soft like bread."
[5.3-6.3s] @MiloBefore, delighted, through the gap of the missing tooth: "That's disgusting."
[6.4-8.0s] @SamBefore, grave, not missing a beat: "It's extremely disgusting. Don't interrupt."

CAMERA
[0-2s] Extreme close-up, locked off.
[2-8s] Close medium shot, locked off, the children as soft out-of-focus foreground.
[8-11s] Medium shot on the door from inside the dark room, locked off.

LAST FRAME
The closed door in the dark, the warm ray of hallway light under it — nothing else, nobody in frame.

AUDIO
The dry click, then the small held silence of a room with two children in it; his full voice, two children's laughter tumbling over it, the quilt shifting; then, in the dark: the soft click of the lamp, bare careful steps, the hinge, the latch, and the house settling. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, red drawings on the wall, a red quilt, a red lampshade, ink stains on the fingers, a readable face in the final segment, a knock on the door, generated music.

*Notes : ⚠ CADRE RÉFÉRENT (4.1) — consigner la composition du segment [0-2 s] au pixel (échelle, angle, position de la main et de la lampe) : à réutiliser à l'identique en 20.11 (même main, index et majeur tachés d'encre, le sandwich à demi mangé, la lampe éteinte). ⚠ PLANT (4.11) — c'est cette même porte devant laquelle, en 8.6, sa main levée n'osera plus frapper ; le plan tient une seconde de trop, comme 8.6. LAST FRAME du segment 2 = raccord direct vers 4.3 [POST] (les mains nouées devant la lampe). Le thème des soirs court très bas au mix.*

---

## GEN-08 — «Le rouge au chambranle» (15 s) — couvre les plans 4.6 → 4.10 du script

**Elements:** @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @KidsBedroom · **Settings:** Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 40mm, f/2.8 · 21:9 · 1080p · 15s · sound on
**Style prompt (EN):** The bedside lamp is the only source, saturated warm amber, raking; the hallway beyond the doorway near-black; deep warm shadows; camera locked off except one slight steady dolly back on the final segment.

SCENE
The girl believes it; the mother watches the man, not the children; the phrase is said like goodnight; the lamp goes out on his voice. Five shots, hard cuts — segments 2 and 4 share one identical doorway set-up.

FRAME MAP
[0-3s] @NoraBefore on the pillow, x=48%, her face filling 55% of frame height; the amber quilt at her chin across the lower frame; lamp warmth from screen-left.
[3-7s] The doorway: @Maeve chest-up at the doorframe, x=50%, filling 70% of frame height; **the deep crimson wool scarf still over her shoulders — the only red in frame**; the hallway black behind her.
[7-10s] @SamBefore at the bed's edge, x=52%, filling 65% of frame height, one hand raised holding half a shape; the two children as soft shapes under the quilt across the lower 25%; the doorway NOT in this frame.
[10-13s] @Maeve at the doorway, x=50% — the same set-up as segment 2.
[13-15s] Waist-level: @SamBefore at x=45% turning from the bed toward the doorway; @Maeve a dark shape at the doorframe at x=78%, the scarf a last ember of red; the frame ends on black.

SUBJECT LOCK, @NORABEFORE
Exact face of the reference, thirteen. On the pillow, quilt at her chin, completely inside it: lips parted, eyes wide and locked on the wall off frame, the quilt edge forgotten in her fists. She is thirteen and she believes it. **She does not blink once in her segment.**

SUBJECT LOCK, @MAEVE
Exact face of the reference. Reference wardrobe **with the deep crimson wool scarf still wound over her shoulders from the walk home — the only red of the block**. Shoulder against the doorframe, arms loosely folded. **Her eyes are on the man by the lamp — on him — never on the children, never on the lens.** The stance of someone with nowhere else she would rather be standing.

SUBJECT LOCK, @SAMBEFORE
Exact face of the reference. Grey marl sweatshirt, clean hands, no ink. A man in the middle of the best part of his day, with no idea he is being watched from the doorway.

SUBJECT LOCK, @MILOBEFORE
A soft shape under the quilt, exact face of the reference where visible.

CROSS-FRAME RULES
@KidsBedroom is the same room and the same lamp in all five segments; the lamp is the only source until it dies at the very end. Segments 2 and 4 are the same doorway set-up — same axis, same scale, same raking light. **The crimson scarf is the ONLY red in any frame of this block and appears only in the segments where @Maeve appears; segments 1 and 3 contain no red at all.** The man's voice runs off frame under segments 1 and 2 and the camera never rejoins him during them. Each character carries the exact face of their reference in every segment. Nobody looks at the lens.

LOCATION
@KidsBedroom — the same shared bedroom of the reference Element: the bed, the amber quilt, the bedside lamp with the woven shade, the papered wall, the doorway to the dark hallway.

LIGHT
The bedside lamp, saturated warm amber: warm and low across @NoraBefore's face on the pillow; reaching @Maeve at a raking angle across the doorway, the hallway behind her black, only the red catching; full and warm on @SamBefore. In the final segment the faint hallway glow dies behind her, then the bedside lamp goes out and the frame drops to black.

MOVEMENT
[0-3s] @NoraBefore on the pillow, completely inside it, eyes wide and locked on the wall off frame; she does not blink. Her father's voice continues off frame, low, an indistinct murmur with no distinct words.
HARD CUT
[3-7s] @Maeve stands shoulder-to-doorframe, arms loosely folded, watching the man telling it by the lamp — steady, unhurried. His voice continues off; the camera never rejoins him.
HARD CUT
[7-10s] @SamBefore in full play, one hand still raised holding half a shape, the laugh sitting openly in his face, shoulders loose, leaning into the lamp light; the children's laughter rises from the bottom of frame.
HARD CUT
[10-13s] @Maeve says the evening phrase the way one says goodnight — without thinking about it, already half-turned to go, the words worn round from use. From the bed, off frame, her daughter's answer comes back without a head lifting from the pillow.
HARD CUT
[13-15s] @SamBefore turns from the bed toward the doorway and smiles at her; she returns the smile as the faint hallway glow behind her dies. He is already turning back to the children, picking up exactly where he stopped, when the bedside lamp goes out on his voice and the frame drops to black.

DIALOGUE
[10.5-12.0s] @Maeve, offhand, warm, no weight on it: "Give and you shall receive."
[12.2-13.0s] @NoraBefore (off, without lifting her head), automatic, sing-song: "We know, Mom."

CAMERA
[0-3s] Close-up, locked off.
[3-7s] Chest-up close shot on the doorway, locked off.
[7-10s] Close medium shot, locked off.
[10-13s] Close shot on the doorway, locked off — identical set-up to segment 2.
[13-15s] Waist-level shot, slight steady dolly back, ending on black.

LAST FRAME
Full black — no image; his voice alone carrying into the dark.

AUDIO
His voice off, low and indistinct, no intelligible words, under segments 1 and 2; his voice and the children's laughter in segment 3; the two spoken lines in segment 4; the quilt shifting; then his voice continuing in the dark for two full seconds after the light dies. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red other than the crimson scarf on the woman, red drawings on the wall, a red quilt, a red lampshade, ink stains on his fingers, a lit hallway in segments 2 and 4, the woman looking at the children, a blink from the girl in the first segment, the voice stopping with the light, generated music.

*Notes : ⚠ Le rouge est entré en 2.1 (GEN-03) — ici l'écharpe est « ENCORE sur les épaules » (4.7), rapportée de la promenade : elle brûle doucement au chambranle et ne quittera le film qu'en 7.9. Elle ne regarde pas ses enfants : elle le regarde, lui. Fin de bloc = fin de la partie contée de la séquence 4 : la voix continue deux pleines secondes dans le noir, puis coupe franche (4.11 = GEN-07 seg. 3). Au mix : le piano baisse d'un cran pour elle (segment 4, et pour elle seule), puis le thème s'efface avec la lampe.*

---

## GEN-09 — «Eux deux» (12 s) — couvre les plans 5.1 → 5.3 du script

**Elements:** @SamBefore + @Maeve + @LivingRoom · **Settings:** Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 40mm, f/2.8 · 21:9 · 1080p · 12s · sound on
**Style prompt (EN):** A single low lamp with a woven ecru shade is the only source, one warm pool of light, everything beyond its throw falling to near-black, camera locked off or on one very slow continuous dolly, no handheld shake.

SCENE
Late night, the same evening. She reads; he mends a net at her feet; he warms her feet under his sweater without a word. Three shots, hard cuts.

FRAME MAP
[0-3s] @Maeve in the worn armchair, x=55%, filling 55% of frame height inside the lamp's pool; the lamp screen-left at x=28%, posed low; the dark window upper right holding a faint reflection of the lit chair.
[3-7s] Opens close on @SamBefore's hands centred at x=50% over the verdigris net in the foreground; the slow dolly back ends with @SamBefore seated on the rug, back against the armchair, filling the lower 50% of frame, @Maeve's knees and the edge of her midnight-blue book above him at x=58%.
[7-12s] Wide two-shot: @SamBefore on the rug at x=50% in the lower half, @Maeve above him in the chair at x=56%, the lamp at x=25%; the pool of light holds them both; near-black all around.

SUBJECT LOCK, @SAMBEFORE
Exact face of the reference. Grey marl sweatshirt, dark blue jeans, oatmeal wool socks — the reference wardrobe. **Hands clean, no ink anywhere.** The mending cycle is his: wooden netting needle passes, loops, knots, pulls tight — regular, without looking down, his face easy in the half-dark.

SUBJECT LOCK, @MAEVE
Exact face of the reference. Reference wardrobe **without the scarf — nothing red anywhere**; barefoot, feet tucked under her then extended to the chair's edge; a midnight-blue clothbound book open in her hands.

CROSS-FRAME RULES
@LivingRoom is the same room of the reference Element in all three segments — same single lamp, same armchair, same rug. The lamp is the only source in every frame. The mending cycle keeps the exact same rhythm in segments 2 and 3. In segment 3 neither of them looks at the other and neither says a word. The only people in frame are @SamBefore and @Maeve, each with the exact face of their reference. Nobody looks at the lens.

LOCATION
@LivingRoom — the small New England living room at night of the reference Element: worn armchair with a knitted throw, low side table with the single woven-ecru-shade lamp, threadbare rug, bookshelf, dark window reflecting the room.

LIGHT
The single lamp, warm and low, is the only source; one warm pool on the chair and the rug; everything beyond falls to near-black.

MOVEMENT
[0-3s] @Maeve reads in the armchair, bare feet tucked under her, her eyes travelling the page.
HARD CUT
[3-7s] @SamBefore mends the net without looking down: the needle passes, loops, knots, pulls tight — the same regular cycle again and again, his hands knowing the work by themselves. A page turns over his head as the frame widens.
HARD CUT
[7-12s] Without breaking the mending rhythm, @SamBefore reaches up from the net, catches @Maeve's two bare feet where they hang at the edge of the armchair, and slides them under his sweater, flat against the warmth of his stomach — one continuous, practised movement. Neither looks at the other. Neither says a word. She turns a page; his hands return to the net and the cycle resumes exactly.

DIALOGUE
Aucun.

CAMERA
[0-3s] Medium shot, locked off.
[3-7s] Close shot on hands, one very slow continuous dolly back widening the frame.
[7-12s] Wide two-shot, locked off.

LAST FRAME
The two of them inside the lamp's pool — her feet under his sweater, his hands back on the net mid-knot, her book up; near-black beyond.

AUDIO
The house at night — the fridge compressor cycling, a foghorn very far off, the twine hissing through the mesh, the wooden needle, pages turning. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, a red net, a red lampshade, a red book cover, a red throw, a red scarf, readable book title, ink stains on his fingers, either of them speaking, generated music.

*Notes : ⚠ le segment [3-7 s] (5.2) est LE GESTE DU MANTEAU — même main, même point, même rythme, rappel exact en 19.a ; mains propres, l'encre appartient à l'homme d'après. ⚠ Le segment [7-12 s] (5.3) est le PLANT du geste des pieds — payoff en 7.5 (GEN-14). LAST FRAME = raccord : GEN-10 reprend ce dispositif en valeurs serrées.*

---

## GEN-10 — «Le regard tenu» (8 s) — couvre les plans 5.4 → 5.5 du script

**Elements:** @SamBefore + @Maeve + @LivingRoom · **Settings:** Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 40mm, f/2.8 · 21:9 · 1080p · 8s · sound on
**Style prompt (EN):** The single lamp warm on one side of each face, deep black behind, locked-off close values only, no handheld shake.

SCENE
He looks at her too long; she catches him; the film's quiet declaration. Four shots, hard cuts — segments 1 and 3 share one identical camera set-up.

FRAME MAP
[0-2s] Close on @SamBefore from beside the lamp, x=50%, filling 70% of frame height, the net still across his lap at the bottom of frame; warm lamp side-light on the left of his face.
[2-3.4s] Reverse close on @Maeve in the armchair, x=50%, filling 70% of frame height, the midnight-blue book lowering to her chin.
[3.4-5s] Identical framing to segment 1: @SamBefore x=50%, same scale, same angle, same lamp side.
[5-8s] Close-up: @Maeve behind the raised book, the dark cover closing the lower 40% of frame, her eyes and brow above its edge at x=50%.

SUBJECT LOCK, @SAMBEFORE
Exact face of the reference. Grey marl sweatshirt, the net across his lap, clean hands, no ink. His eyes come up and stay — long, past politeness, unblinking.

SUBJECT LOCK, @MAEVE
Exact face of the reference. Reference wardrobe without the scarf; the midnight-blue clothbound book. In segment 4 her eyes hold the page far too steadily to be reading.

CROSS-FRAME RULES
Segments 1 and 3 are the same camera set-up to the pixel — same axis, same scale, same lamp side; only two camera values exist across segments 1 to 3. The book that rises at the end of segment 2 is the same book already in place in segment 4. @LivingRoom, the lamp and the armchair are identical in all four segments. The only people are @SamBefore and @Maeve, each with the exact face of their reference in every segment. Nobody looks at the lens.

LOCATION
@LivingRoom — the same room, lamp and armchair as the previous block.

LIGHT
The single lamp, warm on one side of each face; the room behind falls to black.

MOVEMENT
[0-2s] @SamBefore's hands go still on the net; his eyes come up to @Maeve above him and stay there — long, past politeness, unblinking.
HARD CUT
[2-3.4s] @Maeve feels the look land, lowers the book to her chin, one eyebrow up, and speaks.
HARD CUT
[3.4-5s] @SamBefore answers and does not look away; the look holds through the end of the segment.
HARD CUT
[5-8s] @Maeve behind the raised book: above its edge she is smiling to herself — the smile pushing at her cheeks and narrowing her eyes while they hold the page far too steadily to be reading.

DIALOGUE
[2.4-2.9s] @Maeve, book at her chin, one eyebrow up: "What?"
[3.7-4.3s] @SamBefore, quiet, holding the look: "Nothing."

CAMERA
[0-2s] Close shot, locked off, from beside the lamp.
[2-3.4s] Reverse close shot, locked off.
[3.4-5s] Close shot, locked off — identical set-up to segment 1.
[5-8s] Close-up, locked off.

LAST FRAME
Her eyes above the book's edge, the private smile held, the lamp warm on one side, black behind.

AUDIO
The house — a clock somewhere, the fridge; their two voices low and close; a page. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, a red lampshade, a red book cover, a red scarf, readable book title, a third camera value in the first three segments, generated music.

*Note : au mix, **le thème des soirs entre sur le segment final au piano, très bas, pour la première fois du film** — jamais généré. Fin de l'acte I-soirée : la séquence 6 (GEN-11) casse la lumière.*

---

## GEN-11 — «La tasse» (8 s) — couvre les plans 6.1 → 6.3 du script

**Elements:** @Maeve + @Kitchen · **Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 50mm, f/2 · 21:9 · 1080p · 8s · sound on
**Style prompt (EN):** The same single kitchen window as Act I, now in flat daylight under a white sky — the warm gold of the evening gone, the light flat and toneless, colour draining shot by shot, camera locked off throughout.

SCENE
Weeks later. A cup slips; a hand stops obeying; she tells no one. Four shots, hard cuts (the middle two are the scripted internal cut of 6.2).

FRAME MAP
[0-2s] Insert at counter height: the white porcelain cup and @Maeve's hand centred at x=50%; the tile floor across the lower frame; flat white window light from screen-left.
[2-3.6s] Extreme close-up: @Maeve's raised hand centred at x=50%, filling 60% of frame height, palm toward her.
[3.6-5s] Close-up: @Maeve's face at x=50%, filling 65% of frame height, her eyes down toward the hand below frame.
[5-8s] Wide: @Maeve kneeling small in the lower third at x=45%, filling 35% of frame height; the room's blurred warmth far behind; a small out-of-focus silhouette crossing the hallway at x=80%, unrecognizable.

SUBJECT LOCK, @MAEVE
Exact face of the reference wherever her face shows. Fair freckled skin, thin gold band, the reference wardrobe. **No scarf, nothing red, no blood anywhere.** In segment 3 her mouth closes into a flat line and she looks toward the window instead of the door — she tells no one.

CROSS-FRAME RULES
@Kitchen is the same kitchen as Act I — same window direction, same range, same sink — but the light is flat and white and no gold exists anywhere. The hand in segments 1 and 2 is the same hand as the woman in segments 3 and 4. The shards in segment 4 are the same cup from segment 1. The only sharp person in any frame is @Maeve; any background figure stays severely out of focus and unidentifiable. Nobody looks at the lens.

LOCATION
@Kitchen — the kitchen of the reference Element, in full flat daylight under a white sky.

LIGHT
Flat white window light with no modelling in every segment; the hard gold bar of the first evening has disappeared; saturation thinning segment by segment.

MOVEMENT
[0-2s] The white cup slips out of her hand and bursts on the tile, shards skating outward. The hand stays where the cup left it, half open. The radio keeps playing, unchanged, indifferent.
HARD CUT
[2-3.6s] The fingers open, then close, then open again — each time a half-beat late on her intent, the thumb not quite meeting the fingertips. Twice.
HARD CUT
[3.6-5s] Her face: eyes down on the hand, held very still, the swallow visible in her throat; then the mouth closes into a flat line and she looks toward the window instead of the door.
HARD CUT
[5-8s] She kneels and gathers the porcelain shards into her open palm one by one, unhurried, precise, her head bowed to the work; far behind her the blurred warmth of the household keeps moving, unaware.

DIALOGUE
Aucun — elle ne dit rien à personne.

CAMERA
[0-2s] Insert, locked off, at counter height.
[2-3.6s] Extreme close-up, locked off.
[3.6-5s] Close-up, locked off.
[5-8s] Wide shot, locked off, deep focus held only on her.

LAST FRAME
@Maeve small and kneeling, the shards gathered in her palm, the household a blur of warmth behind her, the light flat and white.

AUDIO
The porcelain bursting, very loud and close; the radio carrying on under it, unchanged; two children's voices arguing somewhere far off; the shards clicking piece by piece into her palm. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, a red cup, red crockery, any blood, warm golden light, a red scarf, her speaking, a sharp face in the background, generated music.

*Note : objectif unique du bloc — 50 mm (un seul réglage par génération ; le 50 tient les inserts ET le plan large de la petite cuisine). La désaturation s'installe : même fenêtre qu'en 1.1, ciel blanc, plus d'or du soir.*

---

## GEN-12 — «Le couloir, deux fois» (11 s) — couvre les plans 6.4 → 6.6 du script

**Elements:** @Sam + @Nora + @Maeve (mains seules) + @HospitalCorridor (+ le médecin décrit au prompt — sans Élément ; la chambre du segment final décrite — sans Élément) · **Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 85mm, f/2 · 21:9 · 1080p · 11s · sound on
**Style prompt (EN):** Green overhead fluorescent tubes doubling in the polished floor, long-lens compression down the corridor, deep desaturated grey-greens, camera locked off, absolute stillness, no handheld shake.

SCENE
The same hospital corridor twice — night, then day — then a two-second insert on a packed bag. Three shots, hard cuts; each cut is a scripted time jump.

FRAME MAP
[0-2s] Night. @Sam alone on a plastic chair against the wall, x=40%, mid-ground, filling 45% of frame height, leaning far forward; the corridor running away to deep shadow at frame centre; the green tubes doubling in the floor.
[2-9s] Day. Extreme foreground at the left edge, x=12%: the back of @Nora's head and shoulder, soft, out of focus. Ten metres away, compressed by the long lens mid-frame: the doctor at x=46% and @Sam at x=57%, both filling 55% of frame height; the window at the far end of the corridor blown out to white behind them.
[9-11s] Insert on the corner of a bed in a dim adult bedroom: an open soft travel bag centred at x=50% on a plain grey-beige quilt, half packed with folded pale clothing; @Maeve's hands entering from the top of frame; the scarf's crimson the only saturated colour.

SUBJECT LOCK, @SAM *(RÈGLE F0 — fiche du présent)*
The bearded, weary man of the reference, exact face: a month-old scruffy salt-and-pepper beard, a fuller face, light shadows under the eyes, slumped shoulders, head carried low. Olive canvas work jacket of the reference. He does not speak at any point.

SUBJECT LOCK, @NORA
Back of head and shoulder only, soft and out of focus at the frame edge — dark wavy hair; her face never resolves. **She does not move at all** in her segment.

SUBJECT LOCK, THE DOCTOR *(sans Élément — une seule apparition dans le film)*
In his sixties, short grey hair, rimless glasses, a white coat over a grey shirt, a closed folder held against his thigh. He speaks quietly; **no words carry and his lip movements are never readable as words.**

SUBJECT LOCK, @MAEVE *(mains seules)*
Fair freckled skin, the thin gold wedding band; framed at the hands and forearms only — her face never in frame.

CROSS-FRAME RULES
Segments 1 and 2 are the same corridor of the reference Element — same plastic chairs, same doors, same polished floor — first at night, then in daylight: the cut between them is a scripted time jump and each segment obeys only its own LIGHT block; nothing needs to match across the cut. @Sam is the same man in segments 1 and 2 — same face, same beard, same olive jacket. Segment 3 is a different room, entered on a scripted hard cut; nothing of the corridor appears in it. Every exit sign in the corridor is green. **The scarf's crimson appears ONLY in the final segment and is the only red of the whole block.** Nobody looks at the lens.

LOCATION
Segments 1-2: @HospitalCorridor — the corridor of the reference Element: a row of plastic chairs against one wall, closed doors receding, a polished floor, a window at the far end.
Segment 3: a dim adult bedroom — the corner of a bed, a plain grey-beige quilt, a single bedside lamp; no hospital equipment anywhere.

LIGHT
[0-2s] Night: the green fluorescent tubes overhead are the only light, doubling in the polished floor; the far end of the corridor falls to shadow.
[2-9s] Day: the same green tubes, flat and pitiless, plus the window at the far end of the corridor blown out to white.
[9-11s] A single bedside lamp, warm but muted; every colour in the frame drained except the scarf's red.

MOVEMENT
[0-2s] @Sam sits alone, leaning far forward, elbows on knees, both hands joined and pressed against his mouth. He does not move for the entire segment — the stillness is the event; only his breath moves the joined hands a fraction.
HARD CUT
[2-9s] The doctor speaks quietly to @Sam; no words carry. He stops speaking. @Sam's head goes down, slowly, in one continuous movement. Then the doctor lowers his own eyes, and places one hand on @Sam's shoulder. The hand stays. Neither man moves again for the rest of the segment. @Nora does not move at all.
HARD CUT
[9-11s] @Maeve's hands lower in, last of all, the deep crimson wool scarf, folded with care, smooth it once flat with the palm, and draw the zip closed across it. The shot ends clean on the closed bag.

DIALOGUE
Aucun — la conversation du segment [2-9 s] est **visible mais jamais audible**.

CAMERA
[0-2s] Wide shot down the corridor's length, locked off.
[2-9s] Long-lens shot from @Nora's position, locked off, absolute stillness; the two men compressed mid-corridor, @Nora soft in the extreme foreground.
[9-11s] Insert, locked off.

LAST FRAME
The closed bag on the quilt, the zip drawn shut over the folded red, the hands at rest beside it.

AUDIO
The 50 Hz mains hum through both corridor segments; a trolley far off; a phone ringing once in a closed office; **no voices anywhere**; then the bag's hinge of fabric and the zip, full and close. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subjects looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, audible dialogue, lip movements readable as words, any red anywhere except the folded crimson scarf in the final segment, red exit signage, a fire extinguisher in frame, any blood, name badges, wristbands, readable notice boards, hospital equipment in the bedroom, a face in the final segment, generated music.

*Notes : décision de groupage — 6.4 + 6.5 groupés malgré le raccord nuit/jour : saut de temps écrit au script, traité comme le tunnel→arène du « Boxer » du pack (un bloc LIGHT par segment, rien à raccorder à travers la coupe) ; 6.6 (2 s) rejoint sur sa coupe sèche scriptée. Objectif unique 85 mm : dérogation assumée pour tenir la compression longue focale de 6.5, le plan maître du bloc. ⚠ 6.5 = premier volet du triptyque des conversations qu'on ne nous donne pas (6.5 → 7.7 → 19). Chronologie : Nora a 13 ans ici — de dos, hors foyer, l'écart se joue à la silhouette, pas à une autre fiche. Coupe sèche finale : la séquence 7 reprend le rouge sur les épaules de Maeve.*

---

## GEN-13 — «La chambre : la main, et Milo» (9 s) — couvre les plans 7.1 → 7.2 du script

**Elements:** @MaeveIll + @Milo + @HospitalRoom · **Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 50mm, f/2 · 21:9 · 1080p · 9s · sound on
**Style prompt (EN):** Flat cold hospital daylight — a voiled north window plus overhead fluorescent, no contrast anywhere; the only warmth is a small white bed lamp on two faces; camera locked off, no handheld shake.
*Note FR : « ON DOIT AIMER SA VOIX AVANT DE LA PERDRE » — le segment 2 ne se coupe pas au montage.*

SCENE
Two shots in the same hospital room, hard cut. A gaunt hand on a white sheet; then the mother and her small son on the bed.

FRAME MAP
[0-3s] The hand of @MaeveIll centred, x=50%, foreground, filling 45% of frame height, lying on a smooth white sheet; the room beyond a soft cold blur. No face in frame, no scarf in frame.
[3-9s] @MaeveIll propped up in the bed, head and shoulders right of centre, x=58%, filling 70% of frame height; @Milo climbed onto the bed against her, x=42%, his cheek pressed to her shoulder. The deep crimson-red scarf across her shoulders. The bedside monitor with pale sea-green traces soft at the far left edge, x=8%.

SUBJECT LOCK, @MAEVEILL
The exact gaunt face and hand of her reference: hollowed cheeks, sharpened temples, grey-tinged papery skin over sharp tendons, dry cracked lips, thinned dull auburn hair. Pale-blue hospital gown. The thin gold wedding band far too loose on her finger. In shot two only: the deep crimson-red wool scarf draped over her shoulders. Her breath is short but her timing is intact. She never looks at the lens.

SUBJECT LOCK, @MILO
The exact face of his reference, played six years old here: finer, shorter hair, smaller in every way, a small knitted jumper over grey-blue corduroy dungarees. He never looks at the lens.

CROSS-FRAME RULES
The hand in shot one is the same hand as @MaeveIll's in shot two — same papery skin, same too-loose gold band. @HospitalRoom is the same room in both shots: same bed, same monitor with pale sea-green traces, same voiled north window. The scarf exists ONLY in shot two, on her shoulders — the only red in the whole block. Light identical across both shots.

LOCATION
@HospitalRoom — single room in daylight: white sheets, bedside monitor (pale sea-green traces), IV stand, plastic visitor chair, north-facing window with thin voile, pale green-grey walls.

LIGHT
Shadowless: north window through voile plus ceiling fluorescent, no contrast. In shot two a small white bed lamp is the only warmth, on the two faces.

MOVEMENT
[0-3s] Locked-off insert. The hand lies still on the sheet; one finger stirs and the thin gold wedding band slides a half turn around it, far too loose for the finger it once fitted. The hand settles again and does not move.
HARD CUT
[3-9s] Locked off. @Milo presses his cheek into her shoulder. She speaks — a smile inside the voice; he flinches back an inch; she pulls him closer; he squeezes harder. She closes her eyes, smiles, and breathes into his hair, her nose in it, holding still.

DIALOGUE
[3.8-4.8s] @MaeveIll, low, a smile inside the voice, breath short: "Milo. You're squashing me."
[5.2-5.8s] @Milo, small, pulling back: "Sorry."
[6.2-7.6s] @MaeveIll, softer, pulling him in: "Don't be sorry. Squash me."

CAMERA
[0-3s] Extreme close-up insert, eye level, shallow depth of field on the knuckles, locked off.
[3-9s] Medium close two-shot, eye level, locked off.

LAST FRAME
@MaeveIll's eyes closed, her nose in @Milo's hair, both perfectly still; the scarf one line of crimson across her shoulders; the monitor's pale sea-green traces soft at the left edge.

AUDIO
A heart monitor far off down the hall, a trolley in the corridor, the sheet moving, their two voices close, corridor murmur through the door. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage · no red anywhere except the crimson scarf in shot two, no red LEDs, monitor traces pale sea-green only, no fire extinguisher, exit signage green only · no patient wristband, no name badge, no tears, no visible IV bag label · generated music.

---

## GEN-14 — «La chambre : la phrase, le mur, les pieds» (11 s) — couvre les plans 7.3 → 7.5 du script

**Elements:** @MaeveIll + @Milo + @Nora + @Sam + @HospitalRoom · **Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 50mm, f/2 · 21:9 · 1080p · 11s · sound on
**Style prompt (EN):** One small white bed lamp modelling faces against a cold flat room — voiled north window plus fluorescent, no contrast — camera locked off, no handheld shake.
*Note FR : segment 3 = payoff exact de 5.3 (GEN-09) — même geste, monde changé. Deux mains autour des deux pieds, rien d'autre : ne jamais « améliorer » le geste.*

SCENE
Three shots in the same hospital room, hard cuts. The phrase passed to the smallest; the daughter who will not give her gaze; the husband warming her feet.

FRAME MAP
[0-4s] @Milo close-up, centred, x=50%, filling 75% of frame height; his mother's jaw and ear soft at the right frame edge, x=88%, out of focus. No scarf in this frame.
[4-7s] @Nora close-up, centred, x=50%, filling 80% of frame height, standing at the foot of the bed; in the blurred lower edge of frame, her mother's head on the pillow. No scarf in this frame.
[7-11s] Wide shot of the whole bed: @MaeveIll in the bed left of centre, x=40%, the crimson scarf on her shoulders; @Sam seated at the foot of the bed, x=70%, her feet in his hands. The voiled north window behind.

SUBJECT LOCK, @MAEVEILL
Exact gaunt face of her reference, pale-blue hospital gown, hair thinned and dull, dry lips; in shot three the deep crimson-red wool scarf over her shoulders — the only red in the block. She whispers like a secret; she never looks at the lens.

SUBJECT LOCK, @MILO
Exact face of his reference, played six: finer shorter hair, large pale grey-blue eyes with muted catchlights, small knitted jumper over corduroy dungarees. He listens with his whole face and repeats the words carefully, articulating, like a lesson he refuses to get wrong.

SUBJECT LOCK, @NORA
Exact face of her reference, played thirteen here: hair brushed and tied back, colour still in her cheeks, a plain dark school coat. She does not cry. Her jaw is still, her mouth closed, her arms straight at her sides. Her eyes stay fixed on the wall behind her mother's head and do not move.

SUBJECT LOCK, @SAM
The exact heavy figure and face of his reference: mid-length unkempt greying beard, loose grey-brown curls, hooded swollen pale grey-blue eyes, slumped shoulders, head carried low, corners of the mouth fallen; olive canvas work jacket; large cracked hands, fingertips faintly stained dark blue-black with ink.

CROSS-FRAME RULES
All three shots are the same @HospitalRoom: same bed, same monitor with pale sea-green traces, same voiled north window, same flat light. The mother in the frame edges of shots one and two is the same @MaeveIll as in shot three. The scarf exists ONLY in shot three, on her shoulders. Every face is exact to its reference. Nobody looks at the lens in any shot.

LOCATION
@HospitalRoom — single room in daylight: white sheets, bedside monitor (pale sea-green traces), IV stand, voiled north window, pale green-grey walls.

LIGHT
Shot one: the white bed lamp is the key on the child's face, the room falling to cold grey. Shot two: overhead fluorescent, dead flat on her face, no modelling, no warmth. Shot three: flat cold north-window daylight across the whole bed, no contrast.

MOVEMENT
[0-4s] She whispers to him like a secret, her lips barely moving at the frame's edge. He listens, then repeats it back, careful, articulating every word, his eyes on hers.
HARD CUT
[4-7s] @Nora stands at the foot of the bed and does not cry. In the blurred lower edge her mother's head turns on the pillow toward her, searching; Nora's gaze stays on the wall. She does not give it.
HARD CUT
[7-11s] @Sam lifts the edge of the sheet and takes both of @MaeveIll's feet in his two large hands, enclosing them completely to warm them — the gesture of a man who has done it a thousand evenings. Neither says a word about it. She closes her eyes. His thumbs move once, slowly, and stop.

DIALOGUE
[0.4-1.6s] @MaeveIll, a whisper at his ear, half off-frame: "Give and you shall receive."
[2.0-3.6s] @Milo, applied, articulating each word: "Give and you shall receive."

CAMERA
[0-4s] Close-up, eye level, locked off, shallow focus on the child.
[4-7s] Close-up, eye level, locked off, flat fluorescent.
[7-11s] Wide shot of the whole bed, eye level, locked off, both in frame the entire segment.

LAST FRAME
The wide of the bed: her eyes closed, his two hands enclosing her feet, the scarf on her shoulders, the flat white window behind — nobody moving.

AUDIO
His small voice alone in shot one; the monitor beep and a trolley in shot two; the sheet and the far-off beep in shot three. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage · no red anywhere except the crimson scarf in shot three, monitor traces pale sea-green only, no fire extinguisher, exit signage green only · no tears, no trembling chin, no patient wristband, no name badge, no dialogue in shots two and three · generated music.

---

## GEN-15 ⚠ — «La vitre» (8 s → 2 × 3 s au montage) — couvre les plans 7.7a + 7.7b du script

**⚠ CADRE RÉFÉRENT ABSOLU — bloc dédié, ne JAMAIS grouper avec autre chose. Une seule génération,
cadre rigoureusement fixe de bout en bout, AUCUN hard cut : le raccord 7.7a→7.7b du script est
masqué par le reflet de néon qui balaie le verre à t≈4 s. Au montage : [0-3 s] devient LE fichier
7.7a, réutilisé TEL QUEL en 20.3 (on ne le régénère jamais) ; [4.4-7.4 s] devient 7.7b.
MUET côté chambre. Aucune écharpe, aucune chaise dans ce cadre.**

**Elements:** @Sam + @MaeveIll + @HospitalCorridor + @HospitalRoom (au-delà de la vitre) · **Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 50mm, f/2 · 21:9 · 1080p · 8s · sound on
**Style prompt (EN):** Corridor neon reflected on wired glass in the foreground, the room beyond a shade warmer — the only warmth left — camera locked off at shoulder height, the frame never changes.

SCENE
One single locked-off shot, eight seconds, through the wired-glass window of the closed room door, from the corridor. No cut of any kind; a neon reflection sweeps the glass at the four-second mark.

FRAME MAP
[0-8s] The wired-glass window of the door fills the frame, deliberately off-centre, cropped wrong on purpose, as if we are not allowed to be here. Beyond the glass: @MaeveIll at x=55% and @Sam at x=40%, chest-up, facing each other; the contact of her hands on his face sits in the lower third of the frame. Corridor fluorescent reflections lie across the foreground glass.

SUBJECT LOCK, @MAEVEILL
Exact gaunt face of her reference, pale-blue hospital gown, **no scarf anywhere in this frame**. She holds the face of @Sam in both her hands and speaks at length without letting go; her thumbs stay on his cheekbones.

SUBJECT LOCK, @SAM
Exact bearded, weary face of his reference. He is crying; he nods; he keeps nodding; his shoulders drop once late in the shot. He never wipes his face, never pulls back.

CROSS-FRAME RULES
One continuous take: the framing, camera height and off-centre crop never change by a single pixel. The glass, its wire mesh, the faint condensation and the moving reflections stay between us and them for the full eight seconds. **No chair and no scarf anywhere in the frame at any moment.** Both faces exact to their references. Nobody looks at the lens.

LOCATION
@HospitalCorridor side of a closed hospital room door with a wired-glass window; @HospitalRoom beyond the glass.

LIGHT
Corridor fluorescents in reflection on the glass in the foreground, green-grey; the room behind the glass a shade warmer — the only warmth left in the sequence.

MOVEMENT
[0-3.8s] Beyond the glass, @MaeveIll takes the face of @Sam in both her hands and holds it, and speaks to him at length without letting go. He cries. He nods. He nods again. The condensation on the glass breaks the fine detail of her fingers.
[3.8-4.4s] **REFLECTION SWEEP (raccord du script, pas un cut) :** a bright neon reflection slides across the glass left to right as an unseen trolley passes in the corridor, momentarily washing the image. The frame itself does not move.
[4.4-8s] She still holds his face in both hands, in the lower third of frame, and keeps talking without releasing him. He nods again; his shoulders drop once; she does not let go.

DIALOGUE
Aucun — ses lèvres bougent, rien ne passe la vitre.

CAMERA
[0-8s] Medium shot through the wired glass, shoulder height, locked off, one continuous take, no reframing, no movement.

LAST FRAME
Identical framing to the first frame: her two hands still on his face in the lower third, his head mid-nod, the reflections lying still across the glass, the room's warmth behind.

AUDIO
**Nothing from the room.** Only the 50 Hz fluorescent drone of the corridor and a telephone ringing unanswered in an office somewhere off; the ring stops mid-ring near the end. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage · no red anywhere, no scarf, no chair in frame, exit signage green only, no fire extinguisher · no audible voices, no lip-sync emphasis, no centred composition, no camera move, no cut · generated music.

*Note : ⚠ deuxième volet du triptyque des conversations qu'on ne nous donne pas (6.5 → 7.7 → 19). C'est désormais la SEULE chose que le film nous refuse — et on vient de passer quatre minutes à aimer ces deux-là.*

---

## GEN-16 — «Le couloir : la porte, Nora, l'écharpe» (8 s) — couvre les plans 7.6 · 7.8 · 7.9 du script

**⚠ Montage : GEN-15 (7.7a/b) s'insère ENTRE les segments 1 et 2 de ce bloc.
LE ROUGE QUITTE LE FILM sur le segment 3 — il ne reviendra qu'au manteau.**

**Elements:** @Nora + @Milo (jambes seules) + @HospitalCorridor (+ la main de @Sam en amorce, seg. 3) · **Settings:** Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 50mm, f/2 · 21:9 · 1080p · 8s · sound on
**Style prompt (EN):** Corridor fluorescents greener than the room behind, polished floor holding the tube reflections, deep shadow at the far end, camera locked off.

SCENE
Three shots in the same hospital corridor, hard cuts. The children leave the room; the daughter watches the glass and walks away; a hand takes the folded scarf off a chair.

FRAME MAP
[0-2s] Knee-height frame: the two door leaves centred, x=50%, the polished floor across the lower half. Legs only — no face, no head, ever.
[2-5s] @Nora in profile, left of centre, x=35%, chest-up, filling 65% of frame height; ten metres down the corridor the small lit wired-glass window of the door, x=78%, in soft focus.
[5-8s] Insert: a plastic visitor chair centred, x=50%; on it the deep crimson-red scarf, folded flat, filling 25% of frame height — the only colour in a green-grey frame.

SUBJECT LOCK, @NORA
Exact face of her reference, played thirteen: hair tied back, dark school coat, scuffed sneakers. She does not cry. In shot one only her legs and coat hem appear.

SUBJECT LOCK, LA MAIN DE @SAM (seg. 3)
A man's hand only: large, weathered, thick-knuckled, the fingertips faintly stained dark blue-black with old ink — the exact hand of @Sam's reference. No face, no body beyond the arm.

CROSS-FRAME RULES
All three shots are the same @HospitalCorridor: same plastic chairs, same handrail, same polished floor, same green-grey fluorescents, same door with its wired-glass window. The legs in shot one belong to @Nora (thirteen) and @Milo (six: corduroy dungarees, small velcro trainers). The scarf in shot three is the same deep crimson scarf as on @MaeveIll's shoulders — folded flat with care — and it is the ONLY red in the block. Nobody looks at the lens; in shots one and three no face ever enters the frame.

LOCATION
@HospitalCorridor — plastic chairs against the wall, handrail, closed doors receding, a door with a wired-glass window, polished floor.

LIGHT
Overhead fluorescent tubes, greener than the room disappearing behind the door; hard and green-grey on the plastic chair in shot three; deep shadow at the far end.

MOVEMENT
[0-2s] The door opens: the legs of @Nora and the small legs of @Milo come out into the corridor and pass close by the lens. Behind them, a pair of heavy work boots stays where it is, beside the bed. The door swings shut on its closer, slowly, and clicks.
HARD CUT
[2-5s] @Nora, ten metres from the door, looks at the lit wired-glass window. She sees; she hears nothing. She holds three seconds. Then she turns her eyes away first, then her head, and walks out of the frame; her steps recede. The camera does not follow. Focus eases to the distant door and the frame holds on the empty corridor.
HARD CUT
[5-8s] The folded crimson scarf on the plastic chair. The man's ink-stained hand enters the frame, takes the folded scarf without hurry, and carries it out of the frame. The chair stays, empty, under the fluorescent. Hold on the empty chair.

DIALOGUE
Aucun.

CAMERA
[0-2s] Low wide shot, knee height, locked off.
[2-5s] Medium close shot, eye level, locked off; the frame empties itself.
[5-8s] Insert, eye level, locked off.

LAST FRAME
The empty plastic chair under the green-grey fluorescent, no scarf, no hand, nothing red left anywhere in the frame.

AUDIO
The door hinge and small footsteps in shot one; the 50 Hz drone, her receding steps and a distant telephone that stops ringing in shot two; the wool sliding on plastic then a hard dry cut in shot three. No music.

NEGATIVE PROMPT
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage · the only red in the whole block is the folded scarf in shot three — no other red anywhere, exit signage green only, no fire extinguisher · no faces in shots one and three, no tears, no camera move, no one else in the corridor, no unfolding of the scarf · generated music.

*Notes : ⚠ 7.8 — elle part une phrase trop tôt : elle n'entendra jamais. ⚠ 7.9 — LE ROUGE QUITTE LE FILM sur un geste ; la séquence 8 (GEN-SEQ-06-08.md, GEN-05) s'ouvre sans aucun rouge nulle part.*

---

# [POST] — plans hors blocs (séquence 4 : loup / montagne / oiseau)

> Les trois plans ci-dessous (11 s) ne sont **pas** regroupés : le mur est généré net de toute
> figure, l'ombre (loup / montagne / oiseau) est **compositée en post depuis l'artwork unique**
> (le même jeu que 18.8 et 19.g). Ils s'insèrent au montage entre les segments 2 et 3 de GEN-07,
> avant GEN-08.

### Plan 4.3 — 3 s — LE LOUP
**[POST]** *On génère : le mur papier peint + la lampe rasante + les mains nouées de @SamBefore en amorce, le mur laissé net de toute figure. On composite : l'ombre du LOUP — l'artwork vectoriel unique (le même jeu loup/montagne/oiseau que 18.8 et 19.g), animé en ombre portée.*
**Elements:** @SamBefore (mains en amorce) + @KidsBedroom + artwork loup (post) · **Settings:** Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 40mm, f/2.8 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** The bedside lamp rakes the wall from low and close so any cast shadow reads huge and knife-edged, saturated amber, camera locked off.
**PROMPT (EN):** Wide shot of the papered bedroom wall of @KidsBedroom, locked off, @SamBefore's knotted hands as a dark out-of-focus shape at the frame edge in front of the bedside lamp. The lamp rakes the wall from low and close; the wall itself stays an open field of warm amber light and paper grain, **kept clear of any distinct shadow figure** — the wolf shadow is composited in post from the master artwork. His growl lands — a domestic growl with no menace in it, twice, badly — and off frame two children shriek with laughter. The only person present is @SamBefore, framed at the hands only; the children stay off frame. @KidsBedroom is the same room and lamp as the previous shot. Nobody looks at the lens.
**LAST FRAME:** the knotted hands still held in front of the lamp at the frame edge, the raked wall an open amber field awaiting the composited shadow.
**AUDIO:** the failed growl, twice, and two children howling with laughter. Music: rien à générer — le thème court au mix.
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, red drawings on the wall, a wolf, any animal-shaped shadow, any recognizable shadow figure on the wall (composited in post), a face in frame, generated music.

### Plan 4.4 — 3 s — LA MONTAGNE
**[POST]** *On génère : même dispositif que 4.3 — le mur nu sous la lampe rasante, les deux mains à plat en amorce, arête tenue. On composite : la silhouette de la MONTAGNE depuis l'artwork unique.*
**Elements:** @SamBefore (mains en amorce) + @KidsBedroom + artwork montagne (post) · **Settings:** Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 40mm, f/2.8 · 21:9 · 1080p · 3s · sound on
**Style prompt (EN):** The same raking amber lamp light across the bare wall, deep warm shadow at the edges, camera locked off, absolute stillness.
**PROMPT (EN):** Wide shot of the same papered wall of @KidsBedroom, locked off, identical set-up to the previous shot. @SamBefore's two hands come flat together in the foreground amorce, edge against edge, one clean ridge line — and hold absolutely still. The wall stays an open field of raking amber light, **clear of any distinct shadow figure** — the mountain silhouette is composited in post. Off frame, the little boy's laughter stops at once: the cut of that sound is the event of the shot. The only person present is @SamBefore, framed at the hands only. @KidsBedroom is the same room and lamp as the previous shot. Nobody looks at the lens.
**DIALOGUE:** [0.3-2.2s] @SamBefore (off, at frame edge), the voice dropping lower and slower: "And then, right in front of him — a mountain."
**LAST FRAME:** the two hands held flat edge to edge, absolutely still, the ridge line clean against the raked amber wall.
**AUDIO:** his voice; the laughter stopping dead; the room's small silence. Music: rien à générer — au mix, **le piano se creuse d'un ton.**
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, red drawings on the wall, a mountain shadow, any recognizable shadow figure on the wall (composited in post), a face in frame, generated music.

### Plan 4.5 — 5 s — L'OISEAU
**[POST]** *On génère : la plaque de panoramique — le mur balayé par un pano de 15° vers l'embrasure, lampe rasante, pouces croisés en amorce. On composite : l'OISEAU de l'artwork unique, animé battant des ailes le long du pano jusqu'à l'embrasure.*
**Elements:** @SamBefore (mains en amorce) + @KidsBedroom + artwork oiseau (post) · **Settings:** Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 40mm, f/2.8 · 21:9 · 1080p · 5s · sound on
**Style prompt (EN):** The raking amber lamp light travelling the wall as a single slow 15-degree pan drifts toward the doorway, camera on a fluid head, no shake.
**PROMPT (EN):** Wide shot of the papered wall of @KidsBedroom; one single slow 15-degree pan, left to right, ending toward the dark doorway edge. @SamBefore's crossed thumbs and spread fingers rise into the foreground amorce in front of the lamp and hold their bird shape as the pan travels the raking amber light along the wall toward the door — the wall itself **kept clear of any distinct shadow figure**: the bird shadow that beats its wings across the whole wall is animated and composited in post along this camera path. His voice places each word like a stone. The only person present is @SamBefore, framed at the hands only; the children stay off frame; the pan moves in one direction only, once. @KidsBedroom is the same room and lamp as the previous shot. Nobody looks at the lens.
**DIALOGUE:** [0.3-3.2s] @SamBefore, the low register, each word placed: "And the bird said: I'll carry you over. But you have to give me something first."
**LAST FRAME:** the pan at rest on the dark doorway edge, the raked amber wall behind — the frame into which 4.7 (GEN-08, Maeve au chambranle) répond au montage.
**AUDIO:** his voice; then only the room. Music: rien à générer — au mix, **le piano tient une note.**
**NEGATIVE:** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage, any red anywhere, red drawings on the wall, a bird, any bird-shaped shadow, any recognizable shadow figure on the wall (composited in post), a second pan direction, a face in frame, generated music.
*Note : ⚠ LA PIÈCE MAÎTRESSE DU FILM. La loi du Mender — il demande une petite chose d'abord — est prononcée ici, deux ans avant que Nora ne parte le chercher. Personne ne le relève. C'est dans sa propre histoire du soir que Sam ira la prendre.*

---

*Fin du BLOC I : 16 blocs (173 s générées) + 3 plans [POST] (11 s) = ~186 s couvertes,
séquences 1 → 7 complètes. Suite : séquences 8 (le monde gris) et 9 (Anna) dans
`GEN-SEQ-06-08.md` (blocs GEN-05 → GEN-12 + [POST] 8.4/8.5, toujours valables).*




