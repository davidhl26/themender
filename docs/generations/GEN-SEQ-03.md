# GEN-SEQ-03 — Séquence 3 : LA PERTE *(version courte · format CHORÉGRAPHIE TEMPS RÉEL)*

> **Plans 3.1 → 3.7 · CINQ générations (3A → 3E)** — ~53 s de rushes pour ~34-40 s au montage.
> **Format « chorégraphie temps réel » (David, 21/08)** : position, posture, mains, regard et
> expression définis à chaque instant + règles de jeu réalistes recopiées **dans chaque bloc**
> (chaque génération est collable seule dans Cinema Studio).
> ⚠ **Règle F** : en 3.2 et 3.5-3.7 c'est encore **@SamBefore** — l'homme d'avant, propre, barbe
> courte taillée, mains sans encre. La transformation en @Sam n'arrive que deux ans plus tard (séq. 4+).
> ⚠ **Règle B** : le SEUL rouge de la séquence est l'écharpe de Maeve — sur la chemise d'hôpital
> en 3.3-3.5 (3C, 3D), pliée sur la chaise en 3.7 (3E seg. 2). Cuisine sans rouge (3A), couloir
> sans rouge (3B, 3E seg. 1). Hôpital : signalétique VERTE, moniteurs vert d'eau.
> ⚠ **Règle A** : aucun mot interdit dans les prompts ni les dialogues de cette séquence.
> ⚠ **3A est LE SEUL slow motion du film** — gabarit « time ramp » du pack (l'exemple « Car ») :
> la rampe est écrite dans la chorégraphie ET dans l'AUDIO, et « slow motion » est **retiré du
> negative prompt de 3A uniquement**. Partout ailleurs il reste interdit.
> ⚠ **3D = CADRE RÉFÉRENT ABSOLU (3.5)** : génération dédiée, cadre verrouillé au pixel —
> **ce fichier est réutilisé TEL QUEL en 11.2, enfin sonore** (la voix de Maeve posée au mix).
> Conserver le master intact.
> ☀️ **LUMIÈRE (règle 25/08)** : dans cette séquence **la clarté SE RETIRE** — 3A encore chaude
> mais pâlie (l'or aminci en blanc paille), puis l'hôpital froid et blafard (3B-3E). Le vrai
> sombre n'arrive qu'après la mort (séq. 4+).
> 📷 **RÉALISME MAX (David 25/08)** : chaque Style prompt se termine par la queue réalisme
> (« Hyper-realistic live-action footage… ») + la lumière du monde du bloc ; chaque négatif porte
> « uncanny smoothness, plastic skin, beauty filter, CGI look, video-game lighting »
> (⚠ « slow motion » reste ABSENT du négatif de 3A, et de lui seul).
> **Montage** : 3A → 3B → 3C → 3D → 3E seg. 1 (3.6) → 3E seg. 2 (3.7, ellipse scénarisée).

---

## 1. ÉLÉMENTS À GÉNÉRER D'ABORD

### Lieux *(GPT Image 2, 4K — générés VIDES, sauvegardés en Élément. Prompts complets, queue commune incluse.)*

**@Kitchen** *(déjà généré pour la séq. 1 — même Élément, ne pas régénérer)*
> A small working-class kitchen in a New England triple-decker, seen at eye level from the doorway. A worn wooden table under a window, four mismatched wooden chairs, a gas range with a cast-iron pan, an enamel sink, open shelves with cream and blue crockery, a cluttered counter, a small radio, a tea towel over the oven rail. Painted tongue-and-groove walls in faded sage. Morning light comes low through the single east window and lies in a hard bar across the table, dust visible in it. Warm ambers and worn wood, deep shadows in the corners. No red anywhere. The location is completely empty, no people anywhere, no figures, no subject. No readable text, no lettering, no signage with words, no logos, no brand names, no place names. Photographic, shot on a real camera, sharp focus, no CGI.

**@HospitalRoom**
> A single hospital room in daylight, seen at eye level from the foot of the bed. An adjustable bed with white sheets, a bedside monitor with pale sea-green traces, an IV stand, a plastic visitor chair, a north-facing window with a thin voile blind, pale green-grey walls, a hard floor. Flat cold light from the north window plus overhead fluorescent, no contrast. Whites, sea-greens, cold greys. Exit signage green. No red anywhere, no fire extinguisher in frame. The location is completely empty, no people anywhere, no figures, no subject. No readable text, no lettering, no signage with words, no logos, no brand names, no place names. Photographic, shot on a real camera, sharp focus, no CGI.

**@HospitalCorridor**
> A hospital corridor at night, seen at eye level along its length. A row of plastic chairs against one wall, a door with a wired-glass window, a handrail, a linen trolley, closed doors receding. Overhead fluorescent tubes, greener than the rooms, reflecting on the polished floor and on the glass of the door. Cold green-greys, deep shadow at the far end. Exit signage green. No red anywhere. The location is completely empty, no people anywhere, no figures, no subject. No readable text, no lettering, no signage with words, no logos, no brand names, no place names. Photographic, shot on a real camera, sharp focus, no CGI.

### Objets *(set dressing — PAS d'Élément, rien en [POST] dans cette séquence)*

- **La tasse blanche (3A)** : décrite à l'identique partout où elle apparaît —
  *« a plain white glazed porcelain cup, unpatterned, no logo, filled with milk »*. Les éclats
  du segment slow motion sont LA MÊME tasse, jamais une autre. Aucun autre récipient en scène.
- **L'écharpe rouge** : ce n'est PAS un objet séparé — c'est la **garde-robe de la fiche
  @MaeveIll** (*« the same deep crimson-red wool scarf draped over the shoulders »*). En 3.7
  seulement, elle vit sans elle : *« the deep crimson-red wool scarf, folded flat »* sur la
  chaise. Formule à recopier dans chaque bloc où elle apparaît :
  **« the deep crimson-red wool scarf is the ONLY red allowed in frame »**.
- **[POST]** : rien. Aucun texte composé, aucun artwork inséré dans cette séquence.

### Personnages *(fiches §1 du pack, déjà sauvegardées en Élément)*

| Tag | Plans | Note d'emploi |
|---|---|---|
| **@Maeve** | 3.1 | Encore chez elle, avant l'hôpital. **Sans écharpe** (cuisine sans rouge, règle B) — le lock la décrit sans. |
| **@MaeveIll** | 3.3-3.5 | Chemise d'hôpital pâle-bleue, **écharpe rouge sur les épaules**, cathéter au dos de la main gauche, alliance or trop lâche. |
| **@SamBefore** | 3.2, 3.5-3.7 | ⚠ **Règle F : c'est encore l'homme d'avant** — barbe courte taillée, carrure droite, mains propres SANS encre, sweatshirt gris chiné. Pas de barbe d'un mois, pas de +10 kg : ça, c'est @Sam, deux ans plus tard. En 3.7, seule sa main entre au cadre. |
| **@NoraBefore** | 3.2, 3.4, 3.6 | 13 ans. Le visage de la fiche, mais l'éclat éteint pour toute la séquence : mâchoire serrée, yeux fixes — écrit dans le corps, jamais nommé. |
| **@MiloBefore** | 3.3-3.4 | 6 ans, dent du bas manquante, haut rayé vert et marine. |
| **LE MÉDECIN** | 3.2 | **Figurant one-off, décrit dans le prompt de 3B — pas d'Élément** (comme l'homme du quai en 2.1). Fin cinquantaine, cheveux gris courts, lunettes cerclées acier, blouse blanche SANS badge ni cordon, mains vides. |

---

## 2. GÉNÉRATIONS VIDÉO

## GÉNÉRATION 3A — plan 3.1 « La tasse » *(10 s — LE time ramp du film)*

**Elements** : @Maeve + @Kitchen · **Settings** : Genre Drama · Camera Fine Film · Lens Anamorphic 40mm f/2.8 · 21:9 · 1080p · 10s · sound on

**Style prompt (EN)** : The same single east window as before, but the gold has thinned — a pale straw-white morning, the bar of light across the counter weaker and milkier, colour beginning to drain from the room, the ambers cooler, deep soft shadow in the corners. Camera locked off, no handheld shake. Real-time pacing except for one written time ramp in the middle of the fall. Hyper-realistic live-action footage, indistinguishable from film shot on a real set with real actors: true skin texture with visible pores and fine hairs, real fabric weave, seams and wrinkles that crease with movement, natural motion blur, constant micro-life in every held position (breathing, blinking, weight shifts of a few millimetres), only motivated practical light, subtle film grain, true-to-life colour. NOT CGI, NOT animation, no uncanny smoothness, no plastic skin, no beauty retouching, no video-game look. World-light: the brightness is withdrawing — the room is still warm but paled, the gold thinned to straw-white, colour quietly draining; the last faintly warm morning of the film, subdued yet never murky, nothing crushed to black.

**SCENE** A few weeks later, the same kitchen, a paler morning. A white cup slips from the wife's hand — time ramps down in mid-fall, the cup turning, the milk pulling into a spiral — it bursts on the tile in slow motion — and time snaps back to real speed on her face as she looks at her own hand and opens and closes the fingers, twice. She tells no one. Two shots, one hard cut. Every second is choreographed below; nothing beyond it may be invented.

**PERFORMANCE PACING** Unhurried, naturalistic, lived-in performance throughout. Real-time pacing: every action takes the time it takes in real life, nothing is compressed or hurried. A character always finishes their action before they speak. Before every reply there is a beat of silence — the listener breathes, thinks, then answers. Dialogue at relaxed conversational speed with natural pauses inside the lines. Held looks are truly held. Documentary naturalism, warm and imperfect, never theatrical.

**CONTINUITY LOCK** Every prop named in the layout appears in EVERY shot where its surface is visible, in the same position and state — nothing appears, disappears, multiplies or moves unless the choreography says so. Each character's posture (SEATED or STANDING) is stated at the top of every shot and never changes off-screen. A character holds exactly the object the choreography puts in their hand — no other utensil or object may materialise.

**PROP LAYOUT — FIXED** The counter beside the enamel sink, under the east window. On it: ONE plain white glazed porcelain cup, unpatterned, no logo, filled with milk — the only cup and the only vessel in the scene. The small radio at the far end of the counter, switched on, playing low. The cast-iron pan hangs cold on the range, flame off. The table behind is bare. **No red anywhere, no scarf anywhere, no second cup.** The shards in shot one are this same cup and nothing else; nothing on the counter moves except the cup. Matter and wear, precise: the cup's white glaze carries a fine crazing, the milk filling it to two-thirds; the counter top is worn, its front edge chipped and rubbed pale; the enamel sink's rim is chipped to dark metal in two places; the radio is a small old set with a fabric grille and a worn tuning knob; the floor tiles are old, hairline-cracked here and there, their grout greyed; the cast-iron pan sits cold on the range, matte black with old seasoning.

**POSTURE LOCK** @Maeve is STANDING at the counter for the entire generation, barefoot, and never walks. In shot one only her right hand and the cup move. In shot two only her eyes and the fingers of her right hand move. She never speaks.

**FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND**

**SHOT 1 [0.0-6.3s] — Insert at counter height, eye level, static, locked off. No face in frame.**
[0.0s] Starting positions, held until described otherwise: the white porcelain cup of milk sits on the counter at x=50%, mid-frame, filling 30% of frame height; the tile floor falls away across the lower third; the pale bar of window light crosses the counter from screen-left; the radio soft and out of focus at the right edge, x=90%. @Maeve's right hand and forearm enter the left edge at x=20% — fair freckled skin, thin gold wedding band — palm open, unhurried, reaching for the cup. No other part of her is in frame.
[0.0-1.4s] Real time. Her hand closes around the cup and lifts it from the counter, an ordinary everyday gesture, nothing wrong yet.
[1.4-2.2s] Real time. Mid-lift, at chest height, her fingers simply stop obeying — they slacken all at once, no spasm, no drama — and the cup rolls out of her open hand.
[2.2-5.6s] **TIME RAMPS DOWN INTO SLOW MOTION as the cup clears her fingers**: the cup turns slowly on its own axis as it falls, the milk pulling out of it into one long slow spiral ribbon that hangs and twists in the pale bar of light, dust drifting; her open hand stays where the cup left it, half open, motionless; **the cup meets the tile and bursts in slow motion**, the white porcelain opening outward petal by petal, **the shards skating out across the tile** in long slow slides, the milk sheeting flat and wide.
[5.6-6.3s] Still inside the slow motion: the last shard glides to a stop; the milk spreads; her half-open hand has not moved from where the cup left it.

**HARD CUT — TIME SNAPS BACK TO REAL SPEED ON THE CUT**

**SHOT 2 [6.3-10.0s] — Close-up, eye level, static, locked off.**
[6.3s] Starting positions: @Maeve's face and right shoulder, right of centre at x=58%, filling 70% of frame height, in three-quarter view facing camera-left and DOWN — her eyes on her own right hand, which she holds raised at chest height at x=35%, lower third of frame, palm up, half open. The kitchen soft behind her, the pale window light on one side of her face. Her face is still — no fright played, no trembling: a flat, closed face over something held very tightly underneath.
[6.3-7.2s] Real time, dry and ordinary. She looks at the hand. Nothing moves but her breathing.
[7.2-8.0s] The fingers of the raised hand close slowly into a loose fist… and open again. Once. Her eyes never leave the hand.
[8.0-8.6s] A beat. Nothing moves.
[8.6-9.4s] The fingers close and open a second time, slower. That is all.
[9.4-10.0s] Held to the end, no further movement: her eyes on the open hand, her face flat, the radio playing on somewhere behind, unchanged, indifferent. She tells no one.

**SUBJECT LOCK, MAEVE** The exact woman of the reference — dark auburn wavy hair, grey-green eyes, freckles across the nose and cheekbones, oatmeal cable-knit sweater with pushed-up sleeves, dark grey long skirt, barefoot, thin gold wedding band. **No scarf.** Resting expression in this generation: the laughter of the earlier mornings is gone; her face is quiet, closed, inward — fear written only in stillness, never played. She never speaks. She never looks at the lens.

**CROSS-FRAME RULES** @Kitchen is the same kitchen as the earlier mornings — same counter, same sink, same window direction, same radio — but the light is paler and the gold has thinned. The hand in shot one is the same hand as the woman in shot two — same freckled skin, same gold band. The shards on the tile are the same white cup from shot one. She is the only person in either frame. The time ramp exists ONLY inside shot one between 2.2s and 6.3s; both shots begin and end at real speed. PERFORMANCE PACING and CONTINUITY LOCK apply as written above. **NO INVENTED ACTION** If a body part is not described as moving, it does not move. No gesture, step, head turn, prop interaction or expression change beyond the choreography written below; between described movements every body holds its last described position naturally (breathing, blinking, micro-sway only).

**LOCATION** @Kitchen — the same worn working-class kitchen as the earlier mornings: the counter and enamel sink under the east window; painted tongue-and-groove walls in faded sage, chipped and repainted along their edges; the open shelves of cream and blue crockery slightly crooked on their brackets; the tile floor scuffed, its grout greyed; the small radio playing low at the counter's end; the cold cast-iron pan on the range; the worn wooden table behind, bare, its varnish rubbed through at the four places where a family eats. No toaster exists in this kitchen. Nothing readable anywhere.

**LIGHT** One source: the single east window, its morning sun filtered through thin high cloud — the gold thinned to pale straw-white. The bar of light enters from screen-left, crosses the counter and just clips the cup, laying a soft white line along the porcelain's shoulder and a pale sheen on the milk; dust drifts visibly inside the bar; the rest of the room falls to deep soft shadow in the corners — still domestic, never murky. No flame under the pan, no lamp lit. The bar is weaker, milkier, cooler than the earlier mornings; the room a shade colder than it has ever been.

**DIALOGUE** None. She says nothing to anyone, in either shot.

**LAST FRAME** Her face right of centre in three-quarter, flat and closed, eyes down on her own raised right hand, the hand half open at chest height, the pale window light on one side of her face, the kitchen soft behind.

**AUDIO** The sound follows the time ramp exactly. [0.0-2.2s] Real time: the radio thin and low on the counter, the ordinary morning room tone, the small ceramic slide of the cup leaving the counter. [2.2-6.3s] As time slows, **the radio stretches and drops low, smearing out of shape**; the milk pours long and soft; **the burst of the cup arrives as a single deep low-frequency bloom**, and the shards skate with a drawn-out glassy hiss under it. [6.3s] **Time snaps back on the cut — the real room returns at once, dry and ordinary**: the radio playing on, unchanged, indifferent, her slow breathing, nothing else. Under both real-time sections, faint and constant: the morning outside — one car passing in the street below, a gull far off toward the harbour — and the house itself, a water pipe ticking somewhere in the wall. No music.

**NEGATIVE PROMPT** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subjects looking at camera, morphing objects, extra people in frame, extra gestures, improvised actions, wandering hands, repositioned props, appearing or disappearing objects, a second cup, red crockery, a red cup, a red scarf, any red anywhere, any blood, a cut on her hand, trembling played for drama, her speaking, a face in shot one, rich saturated golden light, rushed movements, theatrical acting, overacting, modern branding, readable signage, posed expressions, sitcom lighting, generated music, uncanny smoothness, plastic skin, beauty filter, CGI look, video-game lighting.
*(⚠ « slow motion » est volontairement ABSENT de ce négatif — uniquement dans cette génération.)*

---

## GÉNÉRATION 3B — plan 3.2 « La conversation muette » *(10 s)*

**Elements** : @SamBefore + @NoraBefore + @HospitalCorridor (+ le médecin décrit au prompt — sans Élément) · **Settings** : Genre Drama · Camera Fine Film · Lens Anamorphic 85mm f/2 · 21:9 · 1080p · 10s · sound on

**Style prompt (EN)** : Flat cold hospital daylight — greener overhead fluorescent tubes doubling in the polished floor, the window at the far end of the corridor blown out to white, long-lens compression flattening ten metres of corridor, deep desaturated grey-greens, camera locked off, absolute stillness, no handheld shake. Real-time pacing, nothing hurried. Hyper-realistic live-action footage, indistinguishable from film shot on a real set with real actors: true skin texture with visible pores and fine hairs, real fabric weave, seams and wrinkles that crease with movement, natural motion blur, constant micro-life in every held position (breathing, blinking, weight shifts of a few millimetres), only motivated practical light, subtle film grain, true-to-life colour. NOT CGI, NOT animation, no uncanny smoothness, no plastic skin, no beauty retouching, no video-game look. World-light: the brightness has left the world — cold, pallid, even hospital light, drained green-greys, bloodless and flat; no golden warmth exists anywhere here.

**SCENE** A hospital corridor, day. In the extreme foreground, out of focus: the back of a thirteen-year-old girl's head. Ten metres away, compressed by the lens, a doctor speaks to her father in a voice that never reaches us. The doctor stops. The father's head goes down, slowly. The doctor's hand settles on his shoulder — and stays. One single continuous shot, no cut. **Nothing said in this corridor is ever audible.** Every second is choreographed below; nothing beyond it may be invented.

**PERFORMANCE PACING** Unhurried, naturalistic, lived-in performance throughout. Real-time pacing: every action takes the time it takes in real life, nothing is compressed or hurried. A character always finishes their action before they speak. Before every reply there is a beat of silence — the listener breathes, thinks, then answers. Dialogue at relaxed conversational speed with natural pauses inside the lines. Held looks are truly held. Documentary naturalism, warm and imperfect, never theatrical.

**CONTINUITY LOCK** Every prop named in the layout appears in EVERY shot where its surface is visible, in the same position and state — nothing appears, disappears, multiplies or moves unless the choreography says so. Each character's posture (SEATED or STANDING) is stated at the top of every shot and never changes off-screen. A character holds exactly the object the choreography puts in their hand — no other utensil or object may materialise.

**PROP LAYOUT — FIXED** The row of plastic chairs against the screen-left wall, all empty. The linen trolley parked far down the corridor, motionless. Closed doors receding on both sides. The handrail along the wall. Every exit sign is a blank green pictogram with no words. Nobody's hands hold anything — the doctor's hands are empty for the whole shot, no clipboard, no folder, no papers. Nothing in the corridor moves except what the choreography says. Matter and wear, precise: the chairs are moulded polypropylene, their seats dulled and micro-scratched by years of cleaning, steel legs on scuffed grey rubber feet; the handrail carries a grey bumper strip scuffed dark at gurney height; the linen trolley's chromed frame is dulled, its canvas bags slack; the doors are laminate with scratched steel kick plates; the polished vinyl floor shows faint buffer swirls under the tubes.

**POSTURE LOCK** All three are STANDING for the entire generation; nobody sits, nobody walks, nobody enters or leaves the frame. @NoraBefore is the motionless foreground and never turns around. The doctor and @SamBefore hold their floor positions to the end — only heads, shoulders and the doctor's right arm move.

**FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND**

**ONE SHOT [0.0-10.0s] — Medium-long shot compressed by the long lens, eye level, static, locked off.**
[0.0s] Starting positions, held until described otherwise: extreme foreground at the left edge, x=12%, filling 55% of frame height: the back of @NoraBefore's head and her left shoulder, severely out of focus — dark wavy hair to the shoulders, absolutely still, facing away from camera toward the two men. Ten metres away, mid-frame, sharp, compressed flat by the lens: THE DOCTOR at x=46%, in right-profile facing camera-right toward Sam — late fifties, short grey hair, steel-rimmed glasses, a knee-length white coat over a grey shirt, no badge, no lanyard, hands loosely clasped in front of him, weight even on both feet. @SamBefore at x=57%, in three-quarter view facing camera-left toward the doctor, both filling 55% of frame height — arms hanging straight at his sides, weight square, chin level, his eyes fixed on the doctor's mouth, his face held very still. Behind them the corridor window blown out to white. The green tubes double in the polished floor.
[0.0-3.2s] The doctor speaks — his lips move, low and unhurried, with small pauses; **not one word reaches the microphone**. His head makes two small measured tilts as he speaks. His clasped hands do not move. Sam does not move at all: eyes on the doctor's mouth, arms hanging.
[3.2-4.0s] The doctor stops speaking. A beat. Nobody in the frame moves.
[4.0-6.5s] **Sam's head goes down, slowly** — the chin sinking toward the chest in one single continuous arc, nothing else moving, his arms staying dead at his sides; at the end of the arc his shoulders drop one centimetre and stay there.
[6.5-7.6s] The doctor's eyes drop to the floor. A beat. His hands unclasp slowly.
[7.6-8.6s] The doctor's right hand rises, unhurried, and **settles on Sam's left shoulder. The hand stays.**
[8.6-10.0s] Held to the end, no further movement anywhere in the frame: the hand on the shoulder, Sam's head down, the doctor's eyes on the floor, Nora's blurred nape motionless in the foreground. Nobody moves again.

**SUBJECT LOCK, SAM** The exact man of the reference @SamBefore — upright, solid, broad-shouldered, short neat dark brown hair, short trimmed salt-and-pepper beard, pale grey-blue eyes, clean hands with no ink, grey marl sweatshirt, dark blue jeans, thin worn steel wedding band. This is still the man from before — nothing of him has changed yet except what this corridor does to him in real time. He does not cry, he does not speak: the collapse is written only in the slow arc of the head and the one-centimetre drop of the shoulders. He never looks at the lens.

**SUBJECT LOCK, NORA** The exact girl of the reference @NoraBefore, thirteen — seen ONLY from behind, out of focus, for the whole shot: dark wavy shoulder-length hair, the mustard-and-cream striped top's shoulder line soft at the frame edge. She never turns, never moves, and her face is never visible.

**SUBJECT LOCK, DOCTOR** A one-off figure, described here only: late fifties, short grey hair, steel-rimmed glasses, a knee-length white coat over a plain grey shirt, no badge, no lanyard, no stethoscope, empty hands. His manner is quiet and practised — the bad news is in the smallness of his gestures. His voice is NEVER audible. He never looks at the lens.

**CROSS-FRAME RULES** One continuous take: the framing, the camera height and the focus split (foreground soft, mid-frame sharp) never change. The only three people in the corridor are @NoraBefore, the doctor and @SamBefore — no nurse, no patient, no passer-by, ever. Every exit sign is green. No red exists anywhere in the frame. PERFORMANCE PACING and CONTINUITY LOCK apply as written above. **NO INVENTED ACTION** If a body part is not described as moving, it does not move. No gesture, step, head turn, prop interaction or expression change beyond the choreography written below; between described movements every body holds its last described position naturally (breathing, blinking, micro-sway only).

**LOCATION** @HospitalCorridor — the corridor of the reference Element by day: the row of empty moulded plastic chairs against one wall, seats dulled by cleaning; closed laminate doors receding, kick plates scratched; the handrail with its scuffed grey bumper strip; the linen trolley far off, chrome dulled, canvas slack; the polished vinyl floor with faint buffer swirls; blank green exit pictograms with no words; the window at the far end. Nothing readable anywhere.

**LIGHT** Two sources: the run of overhead fluorescent tubes in their prismatic diffusers, slightly green, laying an even, shadowless wash down the corridor and doubling as long soft streaks in the buffed vinyl; and the far window, blown out to a flat white rectangle that backlights the two men and hazes their edges. The white coat takes the tubes' faint green cast; no shadow is deeper than a half-tone; the whole corridor is pallid, cold and even — drained, bloodless, no warmth anywhere.

**DIALOGUE** None reaches the microphone at any point. The doctor's lips move at ten metres; his voice is never audible. **No voices anywhere in this generation.**

**LAST FRAME** The doctor's hand resting on Sam's shoulder, Sam's head down, the doctor's eyes on the floor, both compressed sharp in mid-frame against the blown-out window; Nora's blurred nape motionless at the left edge. Nobody moving.

**AUDIO** Corridor ambience ONLY: the fluorescent hum, the building's air, a linen trolley rolling somewhere far off, one door closing in another wing, soft soles far away. Farther into the building, the hospital's life at a distance: a lift chiming on another floor, a phone ringing twice at an unseen desk and stopping, a cart's wheel ticking away down some other corridor. **No voices at any point, not even murmured.** No music.

**NEGATIVE PROMPT** visible camera rigs, cartoonish colors, blurred focus on the two men, on-screen text, subjects looking at camera, slow motion, morphing objects, extra people in frame, a nurse, a passing patient, extra gestures, improvised actions, wandering hands, repositioned props, appearing or disappearing objects, audible speech, murmured voices, subtitles, lip movements readable as words, the girl turning around, the girl's face, tears, a trembling chin, the man falling to his knees, a clipboard, papers, a stethoscope, name badges, lanyards, readable notice boards, any red anywhere, red exit signage, a fire extinguisher, any blood, rushed movements, theatrical acting, overacting, modern branding, readable signage, generated music, uncanny smoothness, plastic skin, beauty filter, CGI look, video-game lighting.

---

## GÉNÉRATION 3C — plans 3.3-3.4 « Écrase-moi, et la phrase » *(15 s)*

**Elements** : @MaeveIll + @MiloBefore + @NoraBefore + @HospitalRoom · **Settings** : Genre Drama · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · 15s · sound on

**Style prompt (EN)** : Flat cold hospital daylight — a voiled north window plus overhead fluorescent, no contrast anywhere, whites and sea-greens and cold greys; the only warmth in the room is the deep crimson of a wool scarf on the mother's shoulders. Camera locked off, no handheld shake. Unhurried, naturalistic, real-time pacing. Hyper-realistic live-action footage, indistinguishable from film shot on a real set with real actors: true skin texture with visible pores and fine hairs, real fabric weave, seams and wrinkles that crease with movement, natural motion blur, constant micro-life in every held position (breathing, blinking, weight shifts of a few millimetres), only motivated practical light, subtle film grain, true-to-life colour. NOT CGI, NOT animation, no uncanny smoothness, no plastic skin, no beauty retouching, no video-game look. World-light: the brightness has left the world — cold, pallid, even hospital light, drained whites and sea-greens, bloodless and flat; the scarf's crimson is the only warmth that survives.

**SCENE** The mother, gravely ill, holds her small son on the hospital bed and tells him not to be sorry — then passes him a phrase like a secret, and he repeats it. The daughter at the foot of the bed will not give her mother her eyes. Two shots, one hard cut. Every second is choreographed below; nothing beyond it may be invented.

**PERFORMANCE PACING** Unhurried, naturalistic, lived-in performance throughout. Real-time pacing: every action takes the time it takes in real life, nothing is compressed or hurried. A character always finishes their action before they speak. Before every reply there is a beat of silence — the listener breathes, thinks, then answers. Dialogue at relaxed conversational speed with natural pauses inside the lines. Held looks are truly held. Documentary naturalism, warm and imperfect, never theatrical.

**CONTINUITY LOCK** Every prop named in the layout appears in EVERY shot where its surface is visible, in the same position and state — nothing appears, disappears, multiplies or moves unless the choreography says so. Each character's posture (SEATED or STANDING) is stated at the top of every shot and never changes off-screen. A character holds exactly the object the choreography puts in their hand — no other utensil or object may materialise.

**PROP LAYOUT — FIXED** The adjustable bed, head raised, white sheets. The bedside monitor with pale sea-green traces at the screen-left side of the bed — soft, never sharp, never beeping loudly. The IV stand behind the headboard, its line running to the cannula taped to the back of her left hand. The plastic visitor chair against the wall under the window, empty, and it stays empty. The voile blind down over the north window. **The deep crimson-red wool scarf draped over her shoulders in BOTH shots — the ONLY red allowed in frame.** No flowers, no cards, no charts, nothing readable anywhere. Nothing in the room moves. Matter and wear, precise: the bed's steel rails carry chipped enamel paint rubbed to metal where hands grip; the sheets are laundered stiff, their white gone faintly grey with industrial washing; the monitor's plastic housing is slightly yellowed, its pale sea-green traces soft; the IV line is thin and clear, the cannula's tape wrinkled at one edge on the back of her hand; the visitor chair is moulded plastic dulled by cleaning; the voile hangs limp, greyed at the hem. The scarf is the one object from home — soft loose-spun wool, pilled, its fringe uneven with years of wear.

**POSTURE LOCK** @MaeveIll is IN THE BED, propped up on the raised head of the bed, for the entire generation — she never sits up further, never stands. @MiloBefore is ON THE BED against her right side for the entire generation — he never climbs down. @NoraBefore is STANDING at the foot of the bed for the entire generation (visible in shot two only) — she never sits, never steps closer, never leaves.

**FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND**

**SHOT 1 [0.0-8.5s] — Medium close-up from the right side of the bed, eye level, static, locked off.**
[0.0s] Starting positions, held until described otherwise: @MaeveIll propped up in the bed, head and shoulders right of centre at x=58%, filling 70% of frame height, in three-quarter view facing camera-left and down toward the boy — the deep crimson-red scarf across her shoulders over the pale-blue hospital gown, her thinned auburn hair loose, the gold band loose on her finger. @MiloBefore at x=42%, climbed onto the bed against her right side, his cheek pressed flat against her chest below her collarbone, both his arms wrapped hard around her ribs, squeezing — his face toward camera, eyes shut tight. Her right arm lies over his back; her left hand, cannula taped to its back, rests on the sheet. The monitor's pale sea-green traces soft at the far left edge, x=8%.
[0.0-1.5s] Nobody speaks. He squeezes; she breathes shallow under the squeeze; the room hums.
[1.5-3.2s] Without moving anything but her mouth and one eyebrow, dry amusement over a weak voice, unhurried: "Milo. You're squashing me."
[3.2-4.0s] A beat. His eyes open. His arms slacken and he starts to pull his head back off her chest, a few centimetres.
[4.0-4.8s] Small voice, a real child's apology: "Sorry."
[4.8-5.4s] A beat. Her eyes hold on him; the corner of her mouth lifts.
[5.4-7.2s] Warm, slow, and completely serious under the warmth: "Don't be sorry. Squash me."
[7.2-8.5s] He clamps back onto her harder than before, cheek flat on her chest. Her eyes close. She lowers her nose into his hair and breathes in, once, long. Held to the cut.

**HARD CUT**

**SHOT 2 [8.5-15.0s] — Wide shot from the window side, eye level, static, locked off — the whole bed and the foot of the bed in frame.**
[8.5s] Starting positions: the bed runs from screen-left, @MaeveIll propped up at x=35%, the crimson scarf on her shoulders, @MiloBefore still against her right side at x=28%, his head now resting below her shoulder, her right arm over him. At the foot of the bed, screen-right, STANDING: @NoraBefore at x=72%, filling 60% of frame height, arms straight down at her sides, weight even, chin level — her eyes fixed on the wall ABOVE and BEHIND her mother's head, not on her mother, and they stay there. The empty visitor chair against the wall at x=90%. The monitor soft at the far left edge.
[8.5-9.3s] A beat. Maeve turns her head down toward Milo's ear — only the head moves.
[9.3-11.0s] She whispers to him, slowly, shaping it like a secret, just loud enough for the microphone: "Give and you shall receive."
[11.0-11.8s] A beat. Milo's brow folds with concentration; his lips rehearse without sound.
[11.8-13.4s] He repeats it, over-articulating every word, small solemn voice: "Give and you shall receive."
[13.4-15.0s] Maeve's eyes leave Milo and travel up to Nora — and stay on her, open, asking, the whole rest of the shot. **Nora's eyes do not move from the wall. She does not give the look.** Nobody moves. Held to the end.

**SUBJECT LOCK, MAEVE** The exact gaunt woman of the reference @MaeveIll — hollowed cheeks, sharpened cheekbones and temples, grey-tinged pallor, dry cracked lips, thinned dull auburn hair, grey-green eyes; the pale-blue hospital gown, **the deep crimson-red wool scarf draped over the shoulders — the ONLY red allowed in frame**, the IV cannula taped to the back of the left hand, the thin gold wedding band loose on her finger. Her body is failing but her timing is intact — the dryness, the warmth, the patience are all still hers. She never looks at the lens.

**SUBJECT LOCK, MILO** The exact child of the reference @MiloBefore, six years old — round face, his father's pale grey-blue eyes, the cowlick at the crown, one lower front tooth missing, green-and-navy striped long-sleeve top, grey corduroy trousers. He squeezes with his whole body; his repeat of the phrase is solemn, not cute. He never looks at the lens.

**SUBJECT LOCK, NORA** The exact girl of the reference @NoraBefore, thirteen — grey-green eyes with the slight downward tilt, her father's straight nose, faint freckles, dark wavy shoulder-length hair, mustard-and-cream striped top, denim skirt over navy leggings. In this room her brightness is switched off: jaw set, mouth flat, eyes fixed on the wall behind her mother for every frame — the refusal is in the fixed eyes, never in a played sulk. She never looks at the lens.

**CROSS-FRAME RULES** Both shots are the same @HospitalRoom: same bed, same monitor with pale sea-green traces, same IV stand and line, same voiled north window, same empty visitor chair, same flat light. @MaeveIll and @MiloBefore hold the same positions on the bed across the cut, shifted only as the choreography says. The scarf is on her shoulders in both shots and is the only red in the block. Every face is exact to its reference. Nobody looks at the lens in any shot. PERFORMANCE PACING and CONTINUITY LOCK apply as written above. **NO INVENTED ACTION** If a body part is not described as moving, it does not move. No gesture, step, head turn, prop interaction or expression change beyond the choreography written below; between described movements every body holds its last described position naturally (breathing, blinking, micro-sway only).

**LOCATION** @HospitalRoom — the room of the reference Element: the adjustable bed with chipped enamel rails and white sheets laundered stiff; the bedside monitor with pale sea-green traces, its housing faintly yellowed; the chromed IV stand and its thin clear line; the plastic visitor chair dulled by cleaning; the voiled north window, the voile greyed at its hem; pale green-grey walls scuffed at bed height; a hard floor. Nothing readable anywhere — no charts, no labels.

**LIGHT** Two sources: the north window, its daylight diffused twice — by the sky and by the voile — into a broad, directionless pale wash across the bed; and the overhead fluorescent, filling what little shadow the window leaves. The sheets hold the highest values in the frame; the faces sit a half-tone below them, even and unmodelled; the monitor's traces add a faint sea-green glow at the left edge. No contrast, no lamp warmth anywhere — the crimson wool absorbs the cold light and stays deep: the only warm value in the frame.

**DIALOGUE** [1.5-3.2s] @MaeveIll, dry amusement over a weak voice, unhurried: "Milo. You're squashing me." [4.0-4.8s] @MiloBefore, small voice: "Sorry." [5.4-7.2s] @MaeveIll, warm, slow, serious underneath: "Don't be sorry. Squash me." [9.3-11.0s] @MaeveIll, whispered to his ear, shaped like a secret: "Give and you shall receive." [11.8-13.4s] @MiloBefore, over-articulating, small solemn voice: "Give and you shall receive."

**LAST FRAME** The wide of the whole bed: Milo tucked under his mother's arm, the crimson scarf across her shoulders, her eyes up and open on her daughter — and Nora at the foot of the bed, arms at her sides, eyes fixed on the wall above her mother's head, giving nothing. Nobody moving.

**AUDIO** The room's flat hum, the small regular tick of the monitor almost below hearing, cloth against cloth as Milo squeezes, her breath shortened by the squeeze, one long slow breath into his hair, five lines of dialogue with real silences between them — the whisper barely carrying. Beyond the door, the ward at a distance: a trolley passing once, a muffled two-tone chime with no words, a door sighing shut in another room. No music.

**NEGATIVE PROMPT** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subjects looking at camera, slow motion, morphing objects, extra people in frame, a nurse, a doctor, extra gestures, improvised actions, wandering hands, repositioned props, appearing or disappearing objects, any red anywhere except the deep crimson-red wool scarf on her shoulders, red LEDs, monitor traces any colour but pale sea-green, red exit signage, a fire extinguisher, any blood, tears, a trembling chin, a patient wristband, a name badge, readable charts, flowers, greeting cards, Nora looking at her mother, Nora sitting, Milo climbing off the bed, rushed movements, hurried dialogue, characters answering instantly, talking over each other, theatrical acting, overacting, modern branding, readable signage, generated music, uncanny smoothness, plastic skin, beauty filter, CGI look, video-game lighting.

---

## GÉNÉRATION 3D — plan 3.5 « La vitre » *(8 s — CADRE RÉFÉRENT ABSOLU, réutilisé tel quel en 11.2)*

> ⚠ **BLOC DÉDIÉ — NE JAMAIS GROUPER.** Cadre verrouillé au pixel, un seul plan continu, aucun
> mouvement de caméra, aucune coupe. **Ce fichier est réutilisé image pour image en 11.2, enfin
> sonore** : la voix de Maeve y sera posée au mix sur ces mêmes lèvres — garder son visage en
> trois-quarts derrière les reflets, le débit des lèvres doux, jamais lisible comme des mots.
> Conserver le master non réencodé.

**Elements** : @MaeveIll + @SamBefore + @HospitalCorridor + @HospitalRoom (au-delà de la vitre) · **Settings** : Genre Drama · Camera Fine Film · Lens Anamorphic 50mm f/2 · 21:9 · 1080p · 8s · sound on

**Style prompt (EN)** : Seen from the corridor through the wired-glass window of a closed hospital room door — cold green fluorescent reflections sliding faintly on the glass between us and them, faint condensation at the pane's edge, and beyond the glass the room warmer, a small bed lamp's amber on two faces. Deep desaturated green-greys on our side. Camera locked off, absolutely still, no handheld shake. **Not one sound of the room crosses the glass.** Hyper-realistic live-action footage, indistinguishable from film shot on a real set with real actors: true skin texture with visible pores and fine hairs, real fabric weave, seams and wrinkles that crease with movement, natural motion blur, constant micro-life in every held position (breathing, blinking, weight shifts of a few millimetres), only motivated practical light, subtle film grain, true-to-life colour. NOT CGI, NOT animation, no uncanny smoothness, no plastic skin, no beauty retouching, no video-game look. World-light: the brightness of the world has shrunk to one small place — cold, pallid green-grey on the corridor side of the glass, and beyond it only the small amber bed lamp, the last warmth of the act, held behind glass.

**SCENE** Through the glass of the door, mute: the dying wife takes her husband's face in both her hands and speaks to him at length. He cries. He nods. He nods again. We hear only the corridor. One single continuous shot, locked frame, no cut, no camera movement of any kind. Every second is choreographed below; nothing beyond it may be invented.

**PERFORMANCE PACING** Unhurried, naturalistic, lived-in performance throughout. Real-time pacing: every action takes the time it takes in real life, nothing is compressed or hurried. A character always finishes their action before they speak. Before every reply there is a beat of silence — the listener breathes, thinks, then answers. Dialogue at relaxed conversational speed with natural pauses inside the lines. Held looks are truly held. Documentary naturalism, warm and imperfect, never theatrical.

**CONTINUITY LOCK** Every prop named in the layout appears in EVERY shot where its surface is visible, in the same position and state — nothing appears, disappears, multiplies or moves unless the choreography says so. Each character's posture (SEATED or STANDING) is stated at the top of every shot and never changes off-screen. A character holds exactly the object the choreography puts in their hand — no other utensil or object may materialise.

**PROP LAYOUT — FIXED** The closed hospital room door filling the right of frame, its wired-glass window at x=58%, occupying 45% of frame height — wire mesh in the glass, faint condensation at the edges, the corridor's green tubes reflected in slow faint slides across it. The corridor wall soft at frame-left. **NO chair anywhere on the corridor side of the frame.** Beyond the glass: the raised bed, the small warm bed lamp, the voile blind — the monitor out of this angle. **The deep crimson-red wool scarf on her shoulders, muted by the glass — the ONLY red allowed in frame.** Nothing in the corridor moves for the whole shot. Matter and wear, precise: the door is a heavy laminate hospital door, paint chipped along its edge, a brushed-steel push plate dulled by hands, a scratched kick plate low; the wired glass carries its diamond mesh slightly imperfect, a faint film of cleaning smears, the condensation beading only at the pane's cold edges; the corridor wall at frame-left shows a scuffed grey bumper rail, soft with defocus.

**POSTURE LOCK** @MaeveIll is sitting up in the bed for the entire shot and never leaves it. @SamBefore is SEATED on the edge of the bed facing her, bent toward her, for the entire shot — he never stands, never turns toward the door. Nobody is in the corridor. Nobody enters or leaves.

**FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND**

**ONE SHOT [0.0-8.0s] — Medium shot through the wired-glass door window, eye level from the corridor, static, locked off. The framing, camera height and off-centre crop never change by a single pixel.**
[0.0s] Starting positions, held until described otherwise, all of it seen through the glass: @MaeveIll sitting up in the bed, in three-quarter view facing camera-left, at x=54% inside the pane, the crimson scarf on her shoulders over the pale-blue gown, her face turned up toward him. @SamBefore seated on the edge of the bed at x=62%, his back in three-quarter to us, bent toward her, forearms on his knees, head slightly lowered toward her face. The warm lamp behind them; the green tube reflections lying across the glass between us and them.
[0.0-1.2s] Nobody moves. The reflections slide faintly. The corridor hums on our side.
[1.2-2.0s] Her two hands rise slowly from the sheet — the cannula line following the left one — and settle on his cheeks, one on each side, her thumbs on his cheekbones.
[2.0-8.0s] She speaks to him continuously, at length, never letting go of his face — her lips moving softly behind the reflections, unhurried, with real pauses, **and not one syllable crosses the glass**. Inside this span, in order:
  [4.2-4.8s] His shoulders go once — a single shake — and the light catches wet on his cheek. He is crying. Her thumbs do not move from his cheekbones.
  [5.4-5.8s] He nods, slowly, inside her hands.
  [6.6-7.0s] He nods again — smaller, surer.
  [7.0-8.0s] She keeps speaking, holding his face; the reflections keep sliding; nothing else in either room moves. Held to the very last frame.

**SUBJECT LOCK, MAEVE** The exact gaunt woman of the reference @MaeveIll — hollowed cheeks, sharpened temples, grey pallor, dry lips, thinned dull auburn hair, grey-green eyes, pale-blue hospital gown, **the deep crimson-red wool scarf on her shoulders, muted through the glass — the ONLY red allowed in frame**, the cannula on the back of the left hand, the loose gold band. She holds his face for the whole shot and speaks without stopping — everything she has left is in the hands and the eyes. She never looks at the lens.

**SUBJECT LOCK, SAM** The exact man of the reference @SamBefore — short neat dark brown hair, short trimmed salt-and-pepper beard, grey marl sweatshirt, steel wedding band, clean hands with no ink — seen mostly from behind in three-quarter, his face only in lost profile inside her hands. He cries without wiping his face; his hands stay on his knees. He nods twice and only twice. He never looks at the lens.

**CROSS-FRAME RULES** One continuous take: the framing, the camera height and the off-centre crop never change by a single pixel; there is no cut and no camera movement of any kind. The glass, its wire mesh, the faint condensation and the moving reflections stay between us and them for the full eight seconds. **No chair and no other person anywhere in the frame at any moment.** Both faces exact to their references. Nobody looks at the lens. PERFORMANCE PACING and CONTINUITY LOCK apply as written above. **NO INVENTED ACTION** If a body part is not described as moving, it does not move. No gesture, step, head turn, prop interaction or expression change beyond the choreography written below; between described movements every body holds its last described position naturally (breathing, blinking, micro-sway only).

**LOCATION** The @HospitalCorridor side of a closed hospital room door with a wired-glass window — heavy laminate door, chipped paint edge, dulled steel push plate, scratched kick plate, the diamond wire mesh in the pane, cleaning smears and edge condensation on the glass, the scuffed corridor wall soft at frame-left; @HospitalRoom beyond the glass — the raised bed, the small warm bed lamp, the voile blind. Nothing readable anywhere.

**LIGHT** Corridor side: the cold green fluorescent tubes overhead behind the camera, even and shadowless, their long reflections lying across the wired glass and sliding faintly — a pallid green-grey wash on the door and wall. Room side, through the glass: the small bed lamp behind and to the left of the two figures throws a low amber that models her face from the side, catches the wet on his cheek and warms the muted crimson of the scarf's wool. The glass holds the two temperatures apart — the cold in front, the last warmth of the act behind it, out of reach.

**DIALOGUE** None audible. Her lips move continuously behind the reflections for six seconds; **not one sound of the room crosses the glass.** *(En 11.2, ce même fichier reçoit sa voix au mix — ne jamais générer la voix ici.)*

**LAST FRAME** ⚠ CADRE RÉFÉRENT ABSOLU — the exact frame that returns in 11.2: through the wired glass, her two hands holding his face, thumbs on his cheekbones, her lips mid-word, his cheek wet in the lamp's warmth, the crimson scarf muted on her shoulders, the green reflections lying across the pane. Nothing moving but her lips.

**AUDIO** The corridor side ONLY: the fluorescent hum above the camera, the building's air, a trolley far off in another wing, once. A lift chimes once, far below; soft soles cross some distant junction and fade. **From the room: absolute silence — no voice, no murmur, no cloth, nothing.** No music.

**NEGATIVE PROMPT** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subjects looking at camera, slow motion, morphing objects, extra people in frame, anyone in the corridor, extra gestures, improvised actions, wandering hands, repositioned props, appearing or disappearing objects, any camera movement, any cut, a centred composition, audible voices, murmured speech, subtitles, lip movements readable as words, lip-sync emphasis, a chair in frame, any red anywhere except the deep crimson-red wool scarf on her shoulders, red exit signage, a fire extinguisher, red LEDs, any blood, him standing, him turning toward the door, her letting go of his face, more than two nods, rushed movements, theatrical acting, overacting, modern branding, readable signage, generated music, uncanny smoothness, plastic skin, beauty filter, CGI look, video-game lighting.

---

## GÉNÉRATION 3E — plans 3.6-3.7 « Nora s'éloigne, le rouge sort » *(10 s)*

**Elements** : @NoraBefore + @SamBefore (main seule, seg. 2) + @HospitalCorridor · **Settings** : Genre Drama · Camera Fine Film · Lens Anamorphic 85mm f/2 · 21:9 · 1080p · 10s · sound on

**Style prompt (EN)** : Flat cold hospital light — the greener fluorescent tubes doubling in the polished floor, deep desaturated grey-greens, long-lens compression; in the second segment the corridor is later and dimmer, the tubes the only light. Camera locked off, absolute stillness, no handheld shake. Real-time pacing, nothing hurried. Hyper-realistic live-action footage, indistinguishable from film shot on a real set with real actors: true skin texture with visible pores and fine hairs, real fabric weave, seams and wrinkles that crease with movement, natural motion blur, constant micro-life in every held position (breathing, blinking, weight shifts of a few millimetres), only motivated practical light, subtle film grain, true-to-life colour. NOT CGI, NOT animation, no uncanny smoothness, no plastic skin, no beauty retouching, no video-game look. World-light: the brightness has left the world — cold, pallid, even hospital light, drained green-greys, bloodless and flat; in segment 2 dimmer still, and the folded scarf's crimson the only colour that survives.

**SCENE** The daughter watches the glass from ten metres — she sees, she hears nothing — and walks away one sentence too soon. Then, later: on a corridor chair, the folded red scarf; a man's hand takes it out of frame. The red leaves the film. Two shots, one hard cut; **the cut is a scripted time jump — days pass across it, each segment obeys only its own LIGHT block, nothing needs to match across the cut.** Every second is choreographed below; nothing beyond it may be invented.

**PERFORMANCE PACING** Unhurried, naturalistic, lived-in performance throughout. Real-time pacing: every action takes the time it takes in real life, nothing is compressed or hurried. A character always finishes their action before they speak. Before every reply there is a beat of silence — the listener breathes, thinks, then answers. Dialogue at relaxed conversational speed with natural pauses inside the lines. Held looks are truly held. Documentary naturalism, warm and imperfect, never theatrical.

**CONTINUITY LOCK** Every prop named in the layout appears in EVERY shot where its surface is visible, in the same position and state — nothing appears, disappears, multiplies or moves unless the choreography says so. Each character's posture (SEATED or STANDING) is stated at the top of every shot and never changes off-screen. A character holds exactly the object the choreography puts in their hand — no other utensil or object may materialise.

**PROP LAYOUT — FIXED** Segment 1: the corridor by day — the row of empty plastic chairs soft along the screen-left wall, closed doors receding, the door with the wired-glass window far down the corridor at frame-left, its pane a small warm rectangle, severely out of focus; **no red anywhere in this segment**. Segment 2: later — ONE plastic visitor chair of that same row, centred; on its seat **the deep crimson-red wool scarf, folded flat — the ONLY red allowed in frame, and the only colour in a green-grey world**; nothing else on or near the chair. Nothing moves in either segment except what the choreography says. Matter and wear, precise: the chair is moulded polypropylene, its seat dulled and micro-scratched grey-white by years of cleaning, steel legs on scuffed rubber feet; the folded scarf shows its real wool — soft loose spin, pilled surface, uneven fringe, one edge worn thin — folded flat with care, the fold lines sharp; the polished vinyl floor doubles the tubes in long soft streaks, faint buffer swirls readable.

**POSTURE LOCK** Segment 1: @NoraBefore is STANDING, then walks out of frame — the only walking in the block, written below. Segment 2: no person is ever in frame; only the right hand and forearm of @SamBefore enter and leave. Nobody else exists in either segment.

**FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND**

**SHOT 1 [0.0-6.0s] — Medium shot across the corridor, eye level, static, locked off. (Plays right after 3D in the edit.)**
[0.0s] Starting positions, held until described otherwise: @NoraBefore right of centre at x=60%, chest-up, filling 65% of frame height, in three-quarter view facing screen-left — arms hanging straight at her sides, weight even on both feet, chin level, mouth flat, **her eyes locked on the wired-glass window ten metres down the corridor**, visible at frame-left, x=10%, as a small warm out-of-focus rectangle. The row of chairs soft behind her. The green tubes double in the floor.
[0.0-2.8s] She watches, absolutely still. Behind the far glass, minute movement — unreadable at this distance. She sees. She hears nothing. Only her breathing moves.
[2.8-3.6s] Her eyes drop from the glass to the floor. A beat. Nothing else moves.
[3.6-5.6s] She turns away from the glass — the head first, then the shoulders, then the feet — and walks out of frame screen-right, unhurried, arms at her sides, without one look back.
[5.6-6.0s] The corridor holds without her: the chairs, the doubled tubes, the warm little rectangle of glass still lit far down at the left. **⚠ Elle part une phrase trop tôt. Elle n'entendra jamais.**

**HARD CUT — SCRIPTED TIME JUMP (days later, the corridor dimmer)**

**SHOT 2 [6.0-10.0s] — Insert, eye level at seat height, static, locked off.**
[6.0s] Starting positions: the plastic visitor chair centred at x=50%, filling 60% of frame height; on its seat the deep crimson-red wool scarf, folded flat, filling 22% of frame height — **the only colour in the frame**. The corridor behind is dim, emptier, the tubes' green doubling on the floor. Nobody in frame.
[6.0-7.4s] The chair and the folded scarf alone, perfectly still. The corridor hums.
[7.4-8.2s] A man's right hand and forearm (@SamBefore — large, clean, no ink, the thin worn steel wedding band, the grey marl cuff) enter from screen-left, unhurried, and **settle flat on the folded wool** — and rest there half a second, not gripping.
[8.2-9.3s] The fingers close slowly around the scarf and lift it — the wool sliding softly off the plastic — and carry it out of frame screen-left. **LE ROUGE QUITTE LE FILM.**
[9.3-10.0s] The empty chair, green-grey, and no red anywhere in the world of the film. Held to the end, nothing moving.

**SUBJECT LOCK, NORA** The exact girl of the reference @NoraBefore, thirteen — grey-green eyes, her father's straight nose, faint freckles, dark wavy shoulder-length hair, mustard-and-cream striped top, denim skirt over navy leggings, scuffed off-white sneakers. Her face is closed and dry — no tears, no trembling: the leaving is flat, which is worse. She never looks at the lens, and never looks back.

**SUBJECT LOCK, SAM (HAND ONLY)** In segment 2 only the right hand and forearm of @SamBefore exist in frame: a large strong clean hand, **no ink anywhere on the fingers**, the thin worn steel wedding band, the grey marl sweatshirt cuff. The face, the body, the rest of the man: never in frame. The gesture is slow, flat, emptied — grief written as the half-second the hand rests flat before it closes.

**CROSS-FRAME RULES** Both segments are the same @HospitalCorridor of the reference Element — same chairs, same doors, same polished floor — first by day, then later and dimmer: the cut between them is a scripted time jump and each segment obeys only its own LIGHT block; nothing needs to match across the cut. The chair in segment 2 is one of the chairs of segment 1. The scarf is the same deep crimson-red wool scarf worn by the mother in the previous blocks, now folded. **The scarf's crimson appears ONLY in segment 2 and is the only red of the whole block — and after it leaves the frame, no red exists anywhere.** Every exit sign is green. Nobody looks at the lens. PERFORMANCE PACING and CONTINUITY LOCK apply as written above. **NO INVENTED ACTION** If a body part is not described as moving, it does not move. No gesture, step, head turn, prop interaction or expression change beyond the choreography written below; between described movements every body holds its last described position naturally (breathing, blinking, micro-sway only).

**LOCATION** @HospitalCorridor — the corridor of the reference Element: the row of moulded plastic chairs against one wall, seats dulled by years of cleaning; the door with the wired-glass window far down its length; closed laminate doors receding, kick plates scratched; the handrail's scuffed grey bumper strip; the polished vinyl floor doubling the tubes; blank green exit pictograms with no words. Nothing readable anywhere.

**LIGHT** Segment 1: day — the run of overhead tubes lays an even, shadowless green-grey wash along the corridor and doubles in the buffed floor; the far pane's small warm rectangle is the only warm value, ten metres deep in the frame; her face is lit flat, pallid, without modelling. Segment 2: later — half the tubes off, the corridor dimmer and emptier, the remaining tubes the only source, their green deepened, the floor's reflections longer and darker; the crimson of the folded wool takes what little light there is and holds it — the only colour in the frame.

**DIALOGUE** None, in either segment. Not a voice anywhere.

**LAST FRAME** The empty plastic chair, centred, in the dim green-grey corridor — no scarf, no red, no one. The film's world without red begins on this frame.

**AUDIO** Segment 1: the corridor's flat hum, her soft unhurried steps leaving on the polished floor, fading out of frame; far off, the hospital's day — a lift chime, a cart, a door in another wing; no voices. Segment 2: near-silence — the hum, the soft slide of wool lifted off plastic, nothing else; far away, once, a door closes in another wing. No breath, no voice. No music.

**NEGATIVE PROMPT** visible camera rigs, cartoonish colors, blurred focus, on-screen text, subjects looking at camera, slow motion, morphing objects, extra people in frame, a nurse, a doctor, extra gestures, improvised actions, wandering hands, repositioned props, appearing or disappearing objects, tears, a trembling chin, her looking back, her running, a face in the second segment, any body beyond the hand and forearm in the second segment, ink stains on the fingers, any red anywhere except the folded crimson scarf in the second segment, red exit signage, a fire extinguisher, any blood, audible voices, name badges, readable notice boards, rushed movements, theatrical acting, overacting, modern branding, readable signage, generated music, uncanny smoothness, plastic skin, beauty filter, CGI look, video-game lighting.

---

**Note** : la séquence encaisse la perte sans jamais la montrer — pas de lit de mort, pas de larmes chez Nora : la mort tient toute dans une main qui reste sur une épaule (3B), un regard non donné (3C) et une écharpe pliée (3E). **3D est le plan le plus précieux du film** : le même fichier revient en 11.2 avec la voix de Maeve posée au mix — archiver le master, ne jamais le réencoder, et vérifier au premier visionnage que les lèvres restent illisibles derrière les reflets (règles A et G sauves). Le time ramp de 3A est l'unique entorse au « no slow motion » du film — si le modèle abuse de la rampe, resserrer [2.2-5.6s] et rallonger le réel autour. Au montage : couper 3A à ~9 s si le deuxième geste des doigts suffit ; insérer 3E seg. 1 immédiatement après 3D, l'ellipse vers 3E seg. 2 assume le saut de temps. Prochaine étape : GEN-SEQ-04 (la porte entrouverte, et Anna — le monde gris commence, 50mm f/2, aucun Sam au cadre).
