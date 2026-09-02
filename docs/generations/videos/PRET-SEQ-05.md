# SÉQUENCE 5 — LE RESTAURANT GRIS · VIDÉOS À COPIER-COLLER *(monde gris · 5 générations obligatoires + 1 secours · 48 s de rushes → 24 s au montage)*

> **UN BLOC = TOUT.** Tu copies **un seul bloc**, tu le colles dans Higgsfield, tu génères.
> **Rien à ouvrir à côté, rien à ajouter.** Les cartes de `00-CARTES-A-COLLER.md` sont
> désormais *dans* chaque bloc : chaîne, monde, tempérament des personnages au cadre,
> pellicule, registre caméra, anti-dérive, contraintes.
>
> Registre caméra de cette séquence : **LOCKED**.
> Modèle **Seedance 2.5** · 21:9 · 1080p · bitrate **high** · sound off.
> Source : `VIDEO-SEQ-05.md`.
>
> ➜ **La marche à suivre écran par écran : ** — quel rôle de média
>    utiliser, et pourquoi attacher la vidéo en *référence* ne produit AUCUNE continuité de cadre.
> ➜ **La marche à suivre écran par écran : `00-COMMENT-GENERER.md`** — quel rôle de média
>    utiliser, et pourquoi attacher la vidéo en *référence* ne produit AUCUNE continuité de cadre.
> ⚠ **DEUX PIÈGES DE L'INTERFACE HIGGSFIELD** *(vérifiés le 02/09 sur un prompt réellement collé)* :
> 1. **Ne jamais écrire `@Video 1` dans un prompt.** L'éditeur le parse comme une mention d'Élément et
>    l'AVALE : la ligne se retrouve à commencer par un deux-points orphelin, et le modèle ne sait même
>    plus qu'une vidéo est attachée. Les blocs disent désormais **THE VIDEO ATTACHED TO THIS
>    GENERATION**, sans `@`. Si tu réécris un bloc à la main, garde cette formule.
> 2. **Vérifie quel Élément l'éditeur a accroché.** En collant, il réécrit `@Kitchen` en
>    `@[kitchen](840a3190…)` — et `840a3190` est le VIEUX kitchen bâti sur un ANGLE, pas sur le master.
>    Deux plans qui n'appellent pas le même Élément ne sont pas dans le même décor.


## VIDÉO 5A — plan 5.1 « Les quatre tasses, puis trois » *(12 s de rushes → 5 s au montage · Elements : @Sam + @Nora + @Milo + @Mei + @Restaurant · start frame : LIEU-07 IMAGE 2)*

```
SCENE CONTEXT
The owner brings tea to a family of three she has known for years and, out of old habit, sets FOUR cups — freezes — and takes one back. Nobody says a word about it; nobody says a word at all. At the table a heavy, unshaven father cuts his young son's food without ever lifting his eyes. Three shots, two hard cuts. Every second is choreographed below; nothing beyond it may be invented. 12 seconds, in 3 framings joined by 2 hard cuts.

CONTINUITY REFERENCE — SAME FILM, DIFFERENT PLACE
THE VIDEO ATTACHED TO THIS GENERATION is an earlier shot from the same film (4D), in a different place. Use it ONLY to match the physical rendering — the film stock, the grain structure, the way skin and fabric resolve, the focus behaviour, the highlight roll-off. Do NOT take its light, its palette, its exposure level or its composition: this shot's light comes from its own LOCATION and LIGHT paragraphs below, and its framing from its own FRAME MAP. Everything else is built new, at full quality.

ACTIVE REFERENCES
@Sam: Sam two years later, a month of badly trimmed beard, ten kilos heavier, grey under the eyes. Two years without speaking — not sullen, emptied. He moves through his own house like a guest, shoulders forward, eyes down and to the side. Every gesture is finished; none is explained. 100% matches the reference.
@Nora: Nora, fifteen, long dark brown unwashed hair, grey-green eyes, pale olive skin gone colourless, bitten lips, heavy lids over grey hollows, thin build. Running on empty: grief has made her polite and absent — she answers, she says thank you, and none of it reaches her face. She goes very still before anything shows. NOTHING RED ON HER. 100% matches the reference.
@Milo: Milo, eight, the only one in the house who still says things out loud. He has not learned to be careful around grief, so he asks, and keeps asking. Watchful pale grey-blue eyes that go to his sister's face first. 100% matches the reference.
@Mei: Mei, fifty-eight, who runs the restaurant — brisk, busy, entirely unmystified, and still running it while this happens. What she passes on she passes on the way she would pass on a phone number: practical, low, half over her shoulder, already moving. Dark green apron stained at the hip. 100% matches the reference.
@Restaurant: Mei's restaurant — amber lanterns, green tablecloths, a green fish tank. No red anywhere, no legible signage. 100% matches the reference.

TEMPERAMENT, SAM AFTER Two years without speaking. Not sullen — emptied. He moves through his own house like a guest: slower, heavier, shoulders carried forward, eyes down and to the side. He still does things for his daughter, but wordlessly and out of her sight. Every gesture is finished; none is ever explained. When he is alone his face does what it wants; the moment she is in the room it does nothing at all.
TEMPERAMENT, NORA A fifteen-year-old running on empty. Grief has made her polite and absent: she answers, she carries the dish back, she says thank you, and none of it reaches her face. Her body is tired before the day starts. She does not cry in front of people — the swollen eyelids come from somewhere else, earlier. When something does move her, she goes very still first, and only then does it show.
TEMPERAMENT, MILO Eight years old and the only one in the house who still says things out loud. He has not learned to be careful around grief yet, so he asks, and he keeps asking. Watchful pale grey-blue eyes that go to his sister's face before they go to anything else. He fidgets, he leans, he is always slightly too close to whoever he is talking to.
TEMPERAMENT, MEI Brisk, busy, entirely unmystified. She runs a restaurant and she is still running it while this is happening. What she passes on, she passes on the way she would pass on a phone number: practical, low, half over her shoulder, already moving to the next thing.

LOCATION MAP
Framing 1 [0.0-3.5s] — camera: Medium, eye level, static, locked off, from the middle of the room toward the family table, the window behind it at screen-left, the lacquered counter running away deep at the extreme screen-right.
Framing 2 [3.5-9.5s] — camera: Extreme close-up, high angle over the table's free corner, static, locked off, looking straight down at the cloth.
Framing 3 [9.5-12.0s] — camera: Medium, eye level, static, locked off — the exact framing of shot 1.
Every distance, height and frame position given above is literal and is held exactly; nothing drifts toward a more flattering angle.

FIRST FRAME AND SPATIAL BLOCKING The generation opens on this exact frame: Medium, eye level, static, locked off, from the middle of the room toward the family table, the window behind it at screen-left, the lacquered counter running away deep at the extreme screen-right. Starting positions, held until described otherwise: @Sam SEATED at x=58%, three-quarter view facing camera, filling 45% of frame height — his bulk low in the chair, shoulders slumped, the month-old beard uneven on the softened jaw, eyes DOWN on his hands; his knife and fork work slowly over Milo's plate, cutting flat noodles into small pieces, the wrist heavy, a constant unhurried rhythm. @Milo SEATED at x=38%, facing camera, filling 30% of frame height, chewing a small mouthful, eyes on his plate. @Nora SEATED foreground-left at x=20%, back three-quarter to camera, soft, filling 50% of frame height, motionless, her fork resting on her plate rim. The back of the EMPTY CHAIR cuts the lower-right foreground at x=80%, pushed in, bare cloth before it. Weak amber lantern pools; the green fish-tank glow far behind. Nobody speaks. This is the frame the first video frame must already be, before anything moves: nothing is settling into place, nothing fades up, nothing is mid-transition.

FORMAT MODE
One take of 12 seconds at real-time speed, containing exactly 3 successive framings joined by 2 hard cuts, placed at the moments the FRAME MAP gives and nowhere else. Each framing is held completely still between its cuts. No other cut, no montage, no dissolve, no speed ramp, no slow motion.

OPTICS
Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described in the FRAME MAP is tack sharp and everything behind it falls off progressively. Focus holds on that plane and breathes naturally with the camera's movement — no deliberate rack focus unless the FRAME MAP calls for one.

CONTINUITY LOCK Every prop named in the layout appears in EVERY shot where its surface is visible, in the same position and state — nothing appears, disappears, multiplies or moves unless the choreography says so. Each character's posture (SEATED or STANDING) is stated at the top of every shot and never changes off-screen. A character holds exactly the object the choreography puts in their hand — no other utensil or object may materialise.

GEOMETRY — LOCKED FOR THE WHOLE SEQUENCE The family table is the square formica table nearest the street window. The women's round table is THE NEXT TABLE OVER, about a metre and a half away, under the green glow of the fish tank at the end of the lacquered counter — in this generation it is empty, cleared, and nobody sits at it. Family table: @Sam faces into the room, @Milo sits at his right hand, @Nora sits opposite @Sam; the FOURTH CHAIR — on the side nearest the women's table — is EMPTY and pushed in, its place bare, and nobody ever sits in it. NOTHING STANDS AT THE COUNTER'S FAR END: no stool, no bowl, nothing on it, in any shot.

PROP LAYOUT — FIXED THE FAMILY TABLE: the square formica table, its edges chipped to black at the corners, under a dark green cloth washed soft and bobbled by years, fold-creases pressed in permanently. THREE place settings only. On the cloth: @Milo's plate of flat noodles and greens, steam thinning off it, directly in front of him; @Sam's own plate, barely touched, at his elbow; @Nora's plate of rice and greens, her fork resting on its rim — all thick white china, glaze worn grey at the edges by decades of stacking; a small dish of dark soy sauce off-centre. The FOURTH place is BARE: no plate, no cup, no cutlery, bare green cloth, for the whole generation. @Sam holds a worn-handled knife in his right hand and a fork in his left, working over MILO'S plate, never his own. MEI'S TRAY: a round black lacquered tray, its lacquer rubbed matte at the grip and finely scratched in circles by years of loads, carried flat on her left forearm — on it a dented metal teapot, dull with handling, its spout tea-stained at the lip, and FOUR small white porcelain cups, glaze finely crazed, no two rims worn quite alike. The fourth cup LEAVES on the tray at the end and the family table finishes the generation with exactly THREE cups. Nothing else moves.

FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND

SHOT 1 [0.0-3.5s] — Medium, eye level, static, locked off, from the middle of the room toward the family table, the window behind it at screen-left, the lacquered counter running away deep at the extreme screen-right.
[0.0s] Starting positions, held until described otherwise: @Sam SEATED at x=58%, three-quarter view facing camera, filling 45% of frame height — his bulk low in the chair, shoulders slumped, the month-old beard uneven on the softened jaw, eyes DOWN on his hands; his knife and fork work slowly over Milo's plate, cutting flat noodles into small pieces, the wrist heavy, a constant unhurried rhythm. @Milo SEATED at x=38%, facing camera, filling 30% of frame height, chewing a small mouthful, eyes on his plate. @Nora SEATED foreground-left at x=20%, back three-quarter to camera, soft, filling 50% of frame height, motionless, her fork resting on her plate rim. The back of the EMPTY CHAIR cuts the lower-right foreground at x=80%, pushed in, bare cloth before it. Weak amber lantern pools; the green fish-tank glow far behind. Nobody speaks.
[0.0-1.8s] Held. The only movement in frame is Sam's slow cutting and Milo's chewing. The room is nearly silent.
[1.8-3.5s] @Mei enters from the right edge, mid-ground, STANDING, filling 60% of frame height, the round black tray flat on her left forearm — the metal teapot and FOUR small white cups on it. She walks without hurry to the table's free corner beside the empty chair and stops. Nobody at the table looks up.

HARD CUT

SHOT 2 [3.5-9.5s] — Extreme close-up, high angle over the table's free corner, static, locked off, looking straight down at the cloth.
[3.5s] Frame contents: the dark green cloth fills the frame. Sam's place at the top of frame — his knife-and-fork rhythm just entering the top edge and continuing, slow, for the whole shot. Milo's plate upper-left. Nora's place at the right. The BARE place at the bottom of frame, in front of the empty chair. Mei's hands and the tray edge enter from the lower frame.
[3.7-4.6s] Her right hand sets the metal teapot at the table's centre, without a sound.
[4.8-5.6s] Cup one, set at Sam's place, top of frame — one small porcelain tap on the cloth.
[5.8-6.6s] Cup two, at Milo's place, upper-left. The same automatic rhythm, a gesture done ten thousand times.
[6.8-7.6s] Cup three, at Nora's place, right.
[7.8-8.6s] Cup four travels toward the BARE place at the bottom of frame — and the hand slows through the last centimetres. The cup touches the cloth.
[8.6-9.5s] THE HAND DOES NOT LET GO. It stays closed around the fourth cup, frozen, knuckles still. At the top of frame Sam's knife keeps its slow rhythm. Nothing else in the frame moves.

HARD CUT

SHOT 3 [9.5-12.0s] — Medium, eye level, static, locked off — the exact framing of shot 1.
[9.5-10.2s] @Mei STANDING at x=52%, bent slightly over the table, her right hand still closed on the fourth cup at the bare place — completely still, a full held moment. Nobody at the table looks at her. Sam cuts; Milo chews; Nora does not move.
[10.2-11.1s] The hand lifts the fourth cup back onto the tray, without a sound. She straightens.
[11.1-12.0s] She turns and walks out of frame right, the tray level, the cup riding on it. At the table nothing changes: three cups steaming, the bare place bare, Sam mid-cut, eyes down. Held to the end. Not one word has been spoken.

SUBJECT LOCK, SAM The exact man of the reference @Sam — the father, two years after: the same broad rectangular face, heavy jaw and pale grey-blue eyes as before, now about ten kilograms heavier, fuller in the face and around the waist; a month-old scruffy uneven salt-and-pepper beard, clearly neglected; light shadows under the eyes; the shoulders slumped, the gaze kept low, the corners of the mouth fallen — a tired, beaten quiet. Wardrobe: the faded charcoal waffle-knit thermal shirt under the olive-drab canvas work jacket with the torn left cuff, the thin worn steel wedding band. His hands: large, the skin cracked, the fingertips faintly stained dark blue-black — they read only as a workman's hands. HE NEVER SPEAKS, never smiles, never lifts his eyes from the plates, and never looks at the lens.

SUBJECT LOCK, NORA The exact girl of the reference @Nora — fifteen, long dark brown wavy hair, unwashed, half-tied back; grey-green eyes with a slight downward outer tilt, heavy lids with grey shadowed hollows beneath, faint freckles across the nose, chapped bitten lips, pale olive skin drained of colour, thin adolescent build, shoulders rounded inward. Wardrobe: the oversized faded charcoal-grey hooded sweatshirt with worn cuffs, dark indigo jeans, NO parka. Resting expression: flat, elsewhere. She never speaks in this sequence and never looks at the lens.

SUBJECT LOCK, MILO The exact child of the reference @Milo — eight, his father's pale grey-blue eyes with long lashes, his mother's small straight nose, full childhood cheeks, faint freckles, thick dark hair with the cowlick standing at the crown; small and slight. Wardrobe: the mustard-yellow ribbed long-sleeve top, the grey-blue corduroy dungarees with one strap twisted. He eats in silence, small mouthfuls, eyes mostly on his plate — a serious, watchful child. He never speaks and never looks at the lens.

SUBJECT LOCK, MEI The exact woman of the reference @Mei — fifty-eight, Chinese American, short and sturdy, warm ivory skin dulled by decades of kitchen heat, deep laugh lines, dark brown almond eyes with a quick direct gaze; the long black hair going grey twisted up in a low bun held with the single lacquered wooden hairpin, loose strands at the temples. Wardrobe: the plain white short-sleeved cotton shirt, the long dark green cotton apron stained at the hip, the thin jade bangle on the left wrist. In this generation her eyes never cross the family's faces: she serves looking at the table, not at the people, and she never looks at the girl. She never looks at the lens.

CROSS-FRAME RULES The same four people in all three shots, exact faces of their references, same wardrobe. @Restaurant is the same room throughout: same two tables in the same positions, same lantern positions, same fish tank on the same wall, same window. Sam's slow cutting rhythm continues across all three shots and never stops. The teapot and the three set cups persist in their exact positions once placed; the fourth cup exists only in Mei's hand, at the bare place during the freeze, and back on the tray — never anywhere else. The empty place stays bare and the empty chair stays pushed in in every frame. Nothing stands at the counter's far end in any frame. Nobody at the family table looks up at Mei; Mei never meets anyone's eyes; nobody speaks. Nobody looks at the lens. NO INVENTED ACTION: If a body part is not described as moving, it does not move. No gesture, step, head turn, prop interaction or expression change beyond the choreography written above; between described movements every body holds its last described position naturally (breathing, blinking, micro-sway only). CONTINUITY LOCK above and the POSITIVE CONSTRAINTS below apply in full.

CONTINUITY — WHAT MUST NOT DRIFT
Wardrobe, hair, dirt, damage and wear are exactly as the references define them and do not improve, clean themselves up or change between shots. Nobody is better groomed, better lit, better dressed or better rested than in the shot before. Props stay where the prop layout puts them. Weather, time of day and light level do not move inside a sequence. Nobody looks at the lens at any point.

LOCATION @Restaurant — the small old family-run Chinese restaurant of the act-one dinner, unchanged and older for it: six formica tables on tubular chrome legs dulled and pitted at the feet, each under a dark green cloth washed soft by years; wooden chairs, their varnish worn pale where hands pull them out, one with a re-glued back rail; the lacquered service counter, its lacquer finely crazed and rubbed to bare wood at the corner where trays slide; the green-lit fish tank, a faint limescale line at the waterline, a slow stream of bubbles, two dark carp barely moving; the beaded curtain to the kitchen, a few strands short; paper lanterns in amber and brass, their paper sun-faded, one panel neatly mended; the window onto the wet street, condensation creeping up the lower glass, the roller blind half down. Nothing stands at the counter's far end: no stool, no bowl, nothing on it. Only the family table is occupied; every other table is empty and cleared, chairs squared — a half-empty room on a slow night. No red anywhere. No readable menus, no lettering anywhere, no other diners, no staff besides Mei.

LIGHT The amber paper lanterns burning low — weak tungsten bulbs inside the paper, each throwing a soft pool barely a metre wide that dies into shadow between the tables, real falloff, the paper itself glowing unevenly where it has thinned; the green fluorescent glow of the fish tank the strongest colour in the room, rippling faintly on the counter lacquer; the counter light dim; cold blue night through the window glass, the wet street holding its reflections; a desaturated grey-blue cast over the whole room, gently underexposed, deep blacks under the empty tables and in the corners. No golden warmth, no cosy atmosphere, and the exposure is exactly the same in the last frame as in the first.

DIALOGUE None. Nobody speaks in this generation — the service happens without one word.

LAST FRAME The family table with exactly THREE cups steaming, the metal teapot at centre, the bare place bare, the empty chair pushed in; @Sam mid-cut over @Milo's plate, eyes down; @Milo chewing; @Nora's fork on her plate rim; @Mei's back leaving frame right with the tray and the fourth cup on it. Grey-blue room, the green tank glowing far behind, nothing at the counter's far end.



CHARACTER PERFORMANCE
Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through nothing else: no added expression, no widened eyes, no trembling lip, no theatrical breath. What is not written does not happen. Between the written events every body simply holds its last position, breathing, blinking and drifting a few millimetres, never frozen and never fidgeting.
@Sam, @Nora and @Milo are SEATED for the entire generation and never rise. @Mei is STANDING for the entire generation — she never sits, never kneels, and leaves frame only as choreographed. Nobody sits in the empty fourth chair. Sam's hands hold the knife and fork over Milo's plate throughout — no other object. Mei's hands hold only the tray, the teapot, and one cup at a time.

PHYSICS — WEIGHT, INERTIA, CONTACT
Everything in frame has mass and obeys it. A body starts and stops with its own weight: it settles into a position rather than snapping into it, and a limb leads while the torso follows a beat later. Feet take the ground with real contact and real friction — on wet stone a step is slightly damped, never sliding, never skating. Clothing lags behind the body that moves it, keeps its own folds and swings back late; hair moves a beat behind the head and comes to rest slowly.
Objects have the mass their material implies. A wooden door swings on its hinges at the speed its own weight allows: it starts slowly, gathers a little, and is slowed at the end by its own friction and the resistance of the hinge — it never floats, never snaps open, never accelerates on its own, and it never moves before something moves it. Hands deform what they touch: fingers flatten slightly against a hard surface, fabric compresses under a grip, a held object presses back. Nothing passes through anything. Nothing changes speed without a cause visible in the frame.

WORLD — AFTER
A grey-blue world, gently underexposed, roughly two thirds of a stop below normal. Sparse motivated sources only — one bulb, one window, one sodium lamp — and deep quiet blacks between them. Colour is drained but not absent: what survives is amber from a flame, sodium orange from a street, sea-green from tile. Never a saturated hue. No red anywhere, flames included.

CINEMATOGRAPHY
Naturalistic available-light cinematography in the raw realist tradition. One motivated source at a time and no fill — a single bulb, a single window, a distant sodium lamp — with deep quiet blacks between them. Deliberately underexposed, roughly two thirds of a stop below normal, protecting the shadows and keeping real separation and texture inside them. Highlights restrained, never blown, holding texture in the filament and the wet stone. Low gentle contrast. Muted desaturated true-to-life colour: what survives is amber from a flame, sodium orange from a street, sea-green from tile — never a saturated hue, and never red.

FILM EMULATION — THE SAME STOCK FROM THE FIRST FRAME TO THE LAST
Shot on Kodak Vision3 500T 5219 tungsten colour negative, one stock, one lab, for the entire film, rated at box speed and printed flat. Cool naturalistic colour science; shadows falling slightly blue-green and holding real separation and texture inside them; skin tones understated, never warmed up, never rosy. Gentle contrast, soft highlight roll-off, highlights restrained and never blown, a faint halation ring blooming around every practical source. Moderate fine grain that grows in the underexposed areas and breathes with the exposure. Not glossy, not digital, not warm. Daylight scenes are the same stock corrected with an 85 filter, never a different look.

CAMERA REGISTER — LOCKED
The camera is placed, and it stays. Nobody is followed, nothing is reframed, and when a body leaves the frame the frame does not go after it. The only life left in the image is the residual human weight the CAMERA paragraph below describes — the same drift of a few millimetres, never more, and never a reframe. This stillness is not neutrality and must never read as a surveillance camera: it is what the film lost when it lost her, and it should feel like a breath being held.

CAMERA — OPERATED, NOT SIMULATED
One anamorphic lens set throughout: slight barrel distortion at the frame edges, oval out-of-focus highlights, mild edge softness, faint vignetting, vintage lens character. Focus is pulled by a human hand — it arrives a few frames late, occasionally overshoots by a hair and settles back, and breathes with the operator's pace. Every held frame keeps a residual human weight in it, a drift of a few millimetres: never a locked robotic stillness, never a shake. No digital sharpening, no edge halos, no noise-reduction smear, no beauty retouching, no plastic skin, no CGI gloss.

PHOTOGRAPHIC REALISM
True skin texture with visible pores and fine hairs, real fabric weave, seams and wrinkles that crease with movement, worn surfaces with real wear, natural asymmetry, natural motion blur in every movement. Deliberately underexposed where the scene calls for it, protecting the shadows and retaining detail inside them: no banding, no posterisation, no crushed flat blacks, no smeared low-light noise, no digital mush.

AUDIO
SFX only. No music. No background music of any kind, no score, no drone, no ambient pad. The slow scrape of Sam's knife on china; four small porcelain sounds as the cups meet the cloth, then one as a cup is lifted away; the tray; the fish-tank pump and the soft burst of its bubbles at the surface; the low drone of the kitchen extractor behind the beaded curtain; the drinks cooler cycling on and off somewhere; wet tyres passing faint outside; the half-empty room's own quiet between all of it; not one voice at the family table. No music.

POSITIVE CONSTRAINTS — CHECK EVERY FRAME AGAINST THESE
Every named reference above is matched 100%: same face, same build, same wardrobe, same wear. Nobody is better groomed, better lit, better dressed or better rested than the shot before; wardrobe, hair, dirt, damage and wear do not improve or clean themselves up. Props stay exactly where the prop layout puts them. The light level, the weather and the time of day do not move inside this generation.
The choreography written in the FRAME MAP is the whole performance: no gesture, step, head turn, prop interaction or expression beyond it. Between described movements every body holds its last position naturally, breathing and blinking, never frozen and never fidgeting.
Nobody looks at the lens at any point. Nobody speaks except where DIALOGUE says so.
Every stroke of handwriting anywhere in frame is real handwriting laid out in straight horizontal lines — word-shaped clusters separated by spaces, gathered into sentences and paragraphs — in an invented cursive alphabet whose characters recur again and again the way a real alphabet's do. Unmistakably a script, but no script that exists on earth, and not one word readable in any language: it reads as writing from across the room and as nothing at all up close. Never random scribble, never a scrawl, never abstract mark-making, never decorative squiggles. No signage, no label, no digit, no subtitle, no caption is readable anywhere.
One continuous take at real-time speed for the exact duration requested, containing ONLY the framings and the hard cuts that FORMAT MODE declares above, at the moments the FRAME MAP gives and nowhere else. No dissolve, no fade, no montage, no extra cut. No slow motion, no speed ramp.

AVOID
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, readable menus, readable signage, readable lettering, subjects looking at camera, slow motion, morphing objects, extra people in frame, other diners, waiters, extra gestures, improvised actions, wandering hands, repositioned props, appearing or disappearing objects, more than four cups, a fifth cup, the fourth cup left on the table at the end, a place setting at the empty place, anyone sitting in the empty chair, anyone at the family table looking up at the waitress, the waitress meeting anyone's eyes, the waitress looking at the girl, the father lifting his eyes, spoken dialogue, characters swapping seats, a stool at the counter, a bowl on a stool, anything standing at the counter's far end, rushed movements, hurried service, theatrical acting, overacting, posed smiles, sitcom lighting, warm saturated grade, golden light, the room brightening, any red anywhere, red lanterns, red tablecloths, red menus, red packaging, a red bowl, generated music, uncanny smoothness, plastic skin, beauty filter, CGI look, video-game lighting, frozen characters, statue-like stillness, mannequin pose, freeze-frame stillness.
```








*⚠ **POINT DE COUPE — 5 s au montage sur 12 s de rushes.** Garder ① **1,6 s** du shot 1, de `[1.9s]` à `[3.5s]`
— l'entrée de Mei, rien avant ; ② **2,0 s** du shot 2, de `[7.6s]` à `[9.5s]` — la quatrième tasse qui ralentit,
qui touche la nappe, et la main qui ne lâche pas ; ③ **1,4 s** du shot 3, de `[9.5s]` à `[10.9s]` — le gel vu
de face et la tasse qui repart. **Ne JAMAIS tailler dans le gel `[8.6-10.2s]`** : c'est le payoff direct de
2.3 (quatre assiettes posées d'office, en souriant). Conserver 5A et le fichier de 2.3 côte à côte pour
vérifier le raccord de jeu de Mei — même geste, deux vies.*

---


## VIDÉO 5B-1 — plan 5.2, première moitié *(10 s de rushes → 7,2 s au montage · Elements : @Nora + @Mei + @Asha + @Fatiha + @Restaurant · start frame : LIEU-07 IMAGE 4 — L'AXE UNIQUE DE 5.2)*

```
SCENE CONTEXT
At the next table over, three women who have known each other for years are talking fast across each other about somebody everybody knows — not telling a story to anyone, just talking, cutting in, finishing each other's sentences. They are not performing and they are not addressing anybody outside their table. A metre and a half away, in the soft foreground, a teenage girl has stopped eating and is listening, and not one of them notices. ONE single continuous shot, no cut. Every second is choreographed below; nothing beyond it may be invented. 10 seconds, one continuous framing, no cut.

CONTINUITY REFERENCE — THIS SHOT CONTINUES THE ATTACHED VIDEO
THE VIDEO ATTACHED TO THIS GENERATION is the shot that immediately precedes this one (5A), in the same place and the same minute. THIS GENERATION IS ITS DIRECT CONTINUATION and must feel like the same take filmed by the same operator seconds later: carry over its exact light level and direction, its grain, its skin rendering, the state the bodies and the props are left in, AND ABOVE ALL THE WAY ITS CAMERA BEHAVES — the same height, the same kind of movement, the same speed, the same breathing weight in the frame. Pick the scene up exactly where the attached video leaves it. Do not restart it, do not reset the room, do not relight it, do not change operator. The new framing is the one the FRAME MAP gives below, but it is reached by the same camera, moving the same way.

ACTIVE REFERENCES
@Nora: Nora, fifteen, long dark brown unwashed hair, grey-green eyes, pale olive skin gone colourless, bitten lips, heavy lids over grey hollows, thin build. Running on empty: grief has made her polite and absent — she answers, she says thank you, and none of it reaches her face. She goes very still before anything shows. NOTHING RED ON HER. 100% matches the reference.
@Mei: Mei, fifty-eight, who runs the restaurant — brisk, busy, entirely unmystified, and still running it while this happens. What she passes on she passes on the way she would pass on a phone number: practical, low, half over her shoulder, already moving. Dark green apron stained at the hip. 100% matches the reference.
@Asha: Asha, fifty-two, upright, deliberate, economical. She listens longer than is comfortable before saying anything, and when she speaks it is short and settled. Her hands are still when she talks. Warmth in her comes out as attention, not as smiling. 100% matches the reference.
@Fatiha: Fatiha, sixty-six, and everything she says goes through her hands first. Quick, warm, interrupting, laughing at the edge of serious things. She touches the arm of whoever she talks to, mentions what broke her the way you mention the weather, and moves on. 100% matches the reference.
@Restaurant: Mei's restaurant — amber lanterns, green tablecloths, a green fish tank. No red anywhere, no legible signage. 100% matches the reference.

TEMPERAMENT, NORA A fifteen-year-old running on empty. Grief has made her polite and absent: she answers, she carries the dish back, she says thank you, and none of it reaches her face. Her body is tired before the day starts. She does not cry in front of people — the swollen eyelids come from somewhere else, earlier. When something does move her, she goes very still first, and only then does it show.
TEMPERAMENT, MEI Brisk, busy, entirely unmystified. She runs a restaurant and she is still running it while this is happening. What she passes on, she passes on the way she would pass on a phone number: practical, low, half over her shoulder, already moving to the next thing.
TEMPERAMENT, ASHA Upright, deliberate, economical. She listens longer than most people are comfortable with before she says anything, and when she does speak it is short and settled — a woman used to being believed without raising her voice. Her hands are still when she talks. Warmth in her comes out as attention, not as smiling.
TEMPERAMENT, FATIHA Sixty-six, and everything she says goes through her hands first. Quick, warm, interrupting, laughing at the edge of serious things. She touches the arm of whoever she is talking to. She tells you a thing that broke her the way you would mention the weather, and moves on before you can be sorry about it.

LOCATION MAP
Framing 1 [0.0-10.0s] — camera: THE AXIS. Medium three-shot of the round table, eye level, static, locked off, no camera movement of any kind for the whole generation. No cut.
Every distance, height and frame position given above is literal and is held exactly; nothing drifts toward a more flattering angle.

FIRST FRAME AND SPATIAL BLOCKING The generation opens on this exact frame: THE AXIS. Medium three-shot of the round table, eye level, static, locked off, no camera movement of any kind for the whole generation. No cut. Starting positions, held until described otherwise: extreme near foreground SCREEN-LEFT at x=9%, LARGE and SOFT, out of focus, the back three-quarter of @Nora's head and shoulder, filling 62% of frame height, SEATED, her raised right hand and the stopped fork just readable as a soft shape. At the extreme left edge, soft and dark, the top rail of the EMPTY CHAIR at her table. Mid-frame, SHARP: the women's round table. @Asha SEATED at x=27%, three-quarter to camera, upright, long neck, squared shoulders, filling 55% of frame height, her chopsticks in her right hand. @Mei SEATED at the back of the group at x=48%, filling 50% of frame height, her shoulders square to the counter at screen-right, her face in three-quarter from camera-left, her right hand around her cup on the cloth. @Fatiha SEATED at x=73%, three-quarter to camera, filling 55% of frame height, her hands free above the cloth. Behind them the fish tank's green field. A weak amber lantern hangs over the round table. This is the frame the first video frame must already be, before anything moves: nothing is settling into place, nothing fades up, nothing is mid-transition.

FORMAT MODE
One single continuous uncut take, 10 seconds long, at real-time speed. No cut, no montage, no dissolve, no speed ramp, no slow motion.

OPTICS
Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described in the FRAME MAP is tack sharp and everything behind it falls off progressively. Focus holds on that plane and breathes naturally with the camera's movement — no deliberate rack focus unless the FRAME MAP calls for one.

CONTINUITY LOCK Every prop named in the layout appears in EVERY frame where its surface is visible, in the same position and state — nothing appears, disappears, multiplies or moves unless the choreography says so. Each character's posture is SEATED and never changes. A character holds exactly the object the choreography puts in their hand — no other utensil or object may materialise.

GEOMETRY — LOCKED FOR THE WHOLE SEQUENCE The camera sits in the aisle just past the family table, at eye level, looking at the women's small round table with the green-lit fish tank filling the background behind it and the lacquered counter running away deep at SCREEN-RIGHT. The family table is the square formica table nearest the street window, just outside the frame's LEFT edge, ABOUT A METRE AND A HALF AWAY — this is the next table over, not a distant one. @Nora sits at it with her back three-quarter to camera, her head and shoulder in the extreme near foreground screen-left. At the women's round table, seen from this axis: @Asha on the LEFT of frame, @Mei at the BACK of the group with her shoulders square to the counter and her face turned toward screen-right, @Fatiha on the RIGHT of frame. @MEI SITS WITH HER BACK THREE-QUARTER TO THE FAMILY TABLE: it lies behind her LEFT shoulder, outside her field of view, and she never turns toward it — she would have to turn her head right round to see anyone at it. NOTHING STANDS AT THE COUNTER'S FAR END: no stool, no bowl, nothing on it.

PROP LAYOUT — FIXED, AND CARRIED UNCHANGED THROUGH 5B-2 THE WOMEN'S ROUND TABLE, under a dark green cloth washed soft by years: at the centre a dented metal teapot, dull with handling, its spout tea-stained at the lip. THREE small white cups of finely crazed porcelain, one before each woman — @Mei's about half full, @Asha's about one third full, @Fatiha's nearly empty with a dry tea ring inside. THREE small plain water glasses, each about two thirds full, one just to the right of each cup. NOBODY DRINKS AT ANY POINT AND NO LEVEL IN ANY CUP OR GLASS EVER CHANGES. TWO small plates of dumplings, their steam long gone, between them. @Fatiha's worn bamboo chopsticks rest across her plate; @Asha's chopsticks are in her right hand. @Mei's cup is IN HER RIGHT HAND, her fingers around it, its base resting on the cloth — she never lifts it to her mouth. THE FAMILY TABLE, at the frame's left edge and beyond it: exactly THREE small white cups, no longer steaming, the metal teapot at centre, the fourth place BARE and its chair EMPTY and pushed in — at the extreme left edge, soft and dark, only the top rail of that empty chair reads. @Nora's fork is IN HER RIGHT HAND, STOPPED in the air above her plate, a piece of food speared on it — it never travels to her mouth, in this generation or in any other of this sequence. Nothing on either table moves unless the choreography says so.

FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND

SHOT [0.0-10.0s] — THE AXIS. Medium three-shot of the round table, eye level, static, locked off, no camera movement of any kind for the whole generation. No cut.
[0.0s] Starting positions, held until described otherwise: extreme near foreground SCREEN-LEFT at x=9%, LARGE and SOFT, out of focus, the back three-quarter of @Nora's head and shoulder, filling 62% of frame height, SEATED, her raised right hand and the stopped fork just readable as a soft shape. At the extreme left edge, soft and dark, the top rail of the EMPTY CHAIR at her table. Mid-frame, SHARP: the women's round table. @Asha SEATED at x=27%, three-quarter to camera, upright, long neck, squared shoulders, filling 55% of frame height, her chopsticks in her right hand. @Mei SEATED at the back of the group at x=48%, filling 50% of frame height, her shoulders square to the counter at screen-right, her face in three-quarter from camera-left, her right hand around her cup on the cloth. @Fatiha SEATED at x=73%, three-quarter to camera, filling 55% of frame height, her hands free above the cloth. Behind them the fish tank's green field. A weak amber lantern hangs over the round table.
[0.0-0.6s] Held: we arrive on a conversation already running, mid-thought, nobody starting anything. In the soft foreground @Nora's chin turns a few degrees toward the women's table; the ear first, the eyes still down; the fork does not move.
[0.35-2.15s] @FATIHA speaks, quick and offhand, one open hand lifting a few centimetres off the cloth and dropping back on the last word: "…my grandmother swore she saw him. Twice."
[1.95-2.95s] @MEI CUTS ACROSS HER LAST WORD, flat, amused, without lifting her eyes from her own cup: "Everyone's grandmother saw him." Only her jaw and her eyes move; her hand stays around the cup.
[2.80-4.20s] @FATIHA, over the tail of that, not conceding anything: "Al-Maktoub. That's what we call him."
[4.05-4.60s] @ASHA, level, one word, chopsticks still in her hand, eyes on the plates: "Msimulizi."
[4.60-5.15s] @MEI, straight after her, the same flat register: "Mòyīrén."
[5.15-5.55s] @MEI laughs — one short breath of a laugh, the shoulders lifting once, nothing more. The light does not change.
[5.55-6.55s] @MEI, still on that breath: "I thought he was ours."
[6.55-7.05s] Half a second where nobody speaks. Nobody looks toward the family table. Nobody looks at the girl. @Asha's eyes go from Mei to Fatiha and stay there.
[7.05-10.0s] Held to the end, no further movement beyond micro-life: three women mid-meal waiting for the next thing one of them will say, @Fatiha drawing breath, @Mei's hand still around her cup, @Asha's chopsticks still in her right hand; in the soft foreground @Nora has not moved at all — the fork still up, the shoulder still, the chin still turned a few degrees toward them.

SUBJECT LOCK, FATIHA The exact woman of the reference @Fatiha — sixty-six, Moroccan American, short and rounded with soft shoulders and expressive hands; warm golden-olive skin with sun spots, dark hazel-brown eyes with heavy hooded lids and a lively animated gaze, deep lines around the mouth from talking and laughing, the small faded traditional dots tattooed on the chin; the soft patterned ochre and dusty-blue headscarf tied at the nape. Wardrobe: the long charcoal wool cardigan over the mustard and cream patterned tunic, small gold hoop earrings, several thin gold rings. Her register here: quick, offhand, talking to her two friends and to nobody else — this is gossip, not a story, and she never performs it. She never looks at the lens.

SUBJECT LOCK, ASHA The exact woman of the reference @Asha — fifty-two, Kenyan American, tall, slim and upright with a long neck and squared shoulders; deep rich dark brown skin, high sharply defined cheekbones, full lips in a natural deep berry-brown, large calm wide-set dark brown eyes with a steady gaze, short neat black locs gathered back with a plain wooden pin, a few grey strands at the temple. Wardrobe: the fine-gauge cream cotton polo-neck, the long olive-and-indigo patterned open coat, small gold hoop earrings, the single thin gold bangle. Her register here: calm, level, dropping one word into the others' talk and letting it lie. She never looks at the lens.

SUBJECT LOCK, MEI The exact woman of the reference @Mei — fifty-eight, Chinese American, short and sturdy, warm ivory skin dulled by decades of kitchen heat, deep laugh lines, dark brown almond eyes with a quick direct gaze; the long black hair going grey twisted up in a low bun held with the single lacquered wooden hairpin, loose strands at the temples. Wardrobe: the plain white short-sleeved cotton shirt, the long dark green cotton apron stained at the hip, the thin jade bangle on the left wrist. SHE SITS WITH HER BACK THREE-QUARTER TO THE FAMILY TABLE AND HER EYES NEVER LEAVE HER TWO FRIENDS AND HER OWN CUP: not one glance toward the family table, not one glance toward the girl, not once, not for a single frame. She never looks at the lens.

SUBJECT LOCK, NORA The exact girl of the reference @Nora — fifteen, long dark brown wavy hair, unwashed, half-tied back; grey-green eyes with a slight downward outer tilt, heavy lids with grey shadowed hollows beneath, faint freckles across the nose, chapped bitten lips, pale olive skin drained of colour, thin adolescent build, shoulders rounded inward. Wardrobe: the oversized faded charcoal-grey hooded sweatshirt with worn cuffs, dark indigo jeans, NO parka. In this generation she is SOFT and OUT OF FOCUS in the extreme foreground, back three-quarter to camera; her face is never readable, she never turns to the lens, she never speaks, and the only thing that moves in her is the chin turning a few degrees. Her fork stays stopped in the air.

CROSS-FRAME RULES ONE single continuous shot with no cut inside it and no camera movement whatsoever. @Restaurant is the same room as every other generation of this sequence: same two tables in the same positions, same lanterns, same fish tank, same window, and nothing at the counter's far end. The state of both tables is the state locked in the prop layout and it does not change: three cups and three water glasses at the women's table at their exact levels, three cups and the bare fourth place at the family table, nothing drunk, nothing eaten, nothing cleared. Everything the women mention stays OFF SCREEN AND OUT OF THE FILM: no flashback, no cutaway, no insert, no other place, no other time, no period costume — the whole generation happens at this table, tonight, in these clothes. None of the three ever names what she is talking about beyond the three proper names written in the dialogue, and none of those names is ever translated or explained. Mei's back stays three-quarter to the family table in every frame; her eyes never go past her two friends and her cup. None of the three women ever looks toward the family table, lowers her voice, or plays the line to anybody outside her own table. The girl never turns her face to camera and never speaks. Nobody looks at the lens. The light does not change on the laugh. NO INVENTED ACTION: If a body part is not described as moving, it does not move. No gesture, step, head turn, prop interaction or expression change beyond the choreography written above; between described movements every body holds its last described position naturally (breathing, blinking, micro-sway only). CONTINUITY LOCK above and the POSITIVE CONSTRAINTS below apply in full.

CONTINUITY — WHAT MUST NOT DRIFT
Wardrobe, hair, dirt, damage and wear are exactly as the references define them and do not improve, clean themselves up or change between shots. Nobody is better groomed, better lit, better dressed or better rested than in the shot before. Props stay where the prop layout puts them. Weather, time of day and light level do not move inside a sequence. Nobody looks at the lens at any point.

LOCATION @Restaurant — the small old family-run Chinese restaurant of the act-one dinner, unchanged and older for it: six formica tables on tubular chrome legs dulled and pitted at the feet, each under a dark green cloth washed soft by years; wooden chairs, their varnish worn pale where hands pull them out, one with a re-glued back rail; the lacquered service counter, its lacquer finely crazed and rubbed to bare wood at the corner where trays slide; the green-lit fish tank, a faint limescale line at the waterline, a slow stream of bubbles, two dark carp barely moving; the beaded curtain to the kitchen, a few strands short; paper lanterns in amber and brass, their paper sun-faded, one panel neatly mended; the window onto the wet street, condensation creeping up the lower glass, the roller blind half down. Nothing stands at the counter's far end: no stool, no bowl, nothing on it. Only the two tables described in the layout are occupied; every other table is empty and cleared, chairs squared — a half-empty room on a slow night. No red anywhere. No readable menus, no lettering anywhere, no other diners, no staff.

LIGHT The amber paper lanterns burning low — weak tungsten bulbs inside the paper, each throwing a soft pool barely a metre wide that dies into shadow between the tables, real falloff, the paper itself glowing unevenly where it has thinned; the green fluorescent glow of the fish tank behind the round table, the strongest colour in the room, rippling faintly on the counter lacquer; the counter light dim; cold blue night through the window glass; a desaturated grey-blue cast over the whole room, gently underexposed, deep blacks under the empty tables and in the corners. The exposure and the colour are exactly the same in the last frame as in the first — the talk does not light the room.

DIALOGUE Four voices' worth of talk in one table's worth of time, quick and overlapping at the joins, each line landing on the tail of the one before, about four words a second, nobody projecting, nobody performing. [0.35-2.15s] @Fatiha: "…my grandmother swore she saw him. Twice." — [1.95-2.95s] @Mei, cutting across her last word, flat and amused, eyes on her own cup: "Everyone's grandmother saw him." — [2.80-4.20s] @Fatiha, over the tail of that: "Al-Maktoub. That's what we call him." — [4.05-4.60s] @Asha, level, one word: "Msimulizi." — [4.60-5.15s] @Mei, straight after: "Mòyīrén." — a short breath of a laugh — [5.55-6.55s] @Mei: "I thought he was ours." — Nobody else speaks. Not one word is spoken at the family table. None of the three names is ever translated, explained or repeated in English.

LAST FRAME The women's round table under the green tank glow, mid-meal and mid-conversation: @Fatiha drawing breath, her hands above the cloth; @Asha's eyes on Fatiha, chopsticks in her right hand; @Mei's hand still around her cup on the cloth, her chest just settling from a short laugh; in the extreme soft left foreground the back of @Nora's head and shoulder, unmoved, her fork still stopped in the air; nothing at the counter's far end.



CHARACTER PERFORMANCE
Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through nothing else: no added expression, no widened eyes, no trembling lip, no theatrical breath. What is not written does not happen. Between the written events every body simply holds its last position, breathing, blinking and drifting a few millimetres, never frozen and never fidgeting.
All four characters in frame are SEATED for the entire generation; nobody rises, nobody changes seats, nobody leaves frame. @Mei never turns her head or body toward the family table. @Nora stays back three-quarter to camera and never turns her face to the lens. Her fork stays up.

PHYSICS — WEIGHT, INERTIA, CONTACT
Everything in frame has mass and obeys it. A body starts and stops with its own weight: it settles into a position rather than snapping into it, and a limb leads while the torso follows a beat later. Feet take the ground with real contact and real friction — on wet stone a step is slightly damped, never sliding, never skating. Clothing lags behind the body that moves it, keeps its own folds and swings back late; hair moves a beat behind the head and comes to rest slowly.
Objects have the mass their material implies. A wooden door swings on its hinges at the speed its own weight allows: it starts slowly, gathers a little, and is slowed at the end by its own friction and the resistance of the hinge — it never floats, never snaps open, never accelerates on its own, and it never moves before something moves it. Hands deform what they touch: fingers flatten slightly against a hard surface, fabric compresses under a grip, a held object presses back. Nothing passes through anything. Nothing changes speed without a cause visible in the frame.

WORLD — AFTER
A grey-blue world, gently underexposed, roughly two thirds of a stop below normal. Sparse motivated sources only — one bulb, one window, one sodium lamp — and deep quiet blacks between them. Colour is drained but not absent: what survives is amber from a flame, sodium orange from a street, sea-green from tile. Never a saturated hue. No red anywhere, flames included.

CINEMATOGRAPHY
Naturalistic available-light cinematography in the raw realist tradition. One motivated source at a time and no fill — a single bulb, a single window, a distant sodium lamp — with deep quiet blacks between them. Deliberately underexposed, roughly two thirds of a stop below normal, protecting the shadows and keeping real separation and texture inside them. Highlights restrained, never blown, holding texture in the filament and the wet stone. Low gentle contrast. Muted desaturated true-to-life colour: what survives is amber from a flame, sodium orange from a street, sea-green from tile — never a saturated hue, and never red.

FILM EMULATION — THE SAME STOCK FROM THE FIRST FRAME TO THE LAST
Shot on Kodak Vision3 500T 5219 tungsten colour negative, one stock, one lab, for the entire film, rated at box speed and printed flat. Cool naturalistic colour science; shadows falling slightly blue-green and holding real separation and texture inside them; skin tones understated, never warmed up, never rosy. Gentle contrast, soft highlight roll-off, highlights restrained and never blown, a faint halation ring blooming around every practical source. Moderate fine grain that grows in the underexposed areas and breathes with the exposure. Not glossy, not digital, not warm. Daylight scenes are the same stock corrected with an 85 filter, never a different look.

CAMERA REGISTER — LOCKED
The camera is placed, and it stays. Nobody is followed, nothing is reframed, and when a body leaves the frame the frame does not go after it. The only life left in the image is the residual human weight the CAMERA paragraph below describes — the same drift of a few millimetres, never more, and never a reframe. This stillness is not neutrality and must never read as a surveillance camera: it is what the film lost when it lost her, and it should feel like a breath being held.

CAMERA — OPERATED, NOT SIMULATED
One anamorphic lens set throughout: slight barrel distortion at the frame edges, oval out-of-focus highlights, mild edge softness, faint vignetting, vintage lens character. Focus is pulled by a human hand — it arrives a few frames late, occasionally overshoots by a hair and settles back, and breathes with the operator's pace. Every held frame keeps a residual human weight in it, a drift of a few millimetres: never a locked robotic stillness, never a shake. No digital sharpening, no edge halos, no noise-reduction smear, no beauty retouching, no plastic skin, no CGI gloss.

PHOTOGRAPHIC REALISM
True skin texture with visible pores and fine hairs, real fabric weave, seams and wrinkles that crease with movement, worn surfaces with real wear, natural asymmetry, natural motion blur in every movement. Deliberately underexposed where the scene calls for it, protecting the shadows and retaining detail inside them: no banding, no posterisation, no crushed flat blacks, no smeared low-light noise, no digital mush.

AUDIO
SFX only. No music. No background music of any kind, no score, no drone, no ambient pad. Two tables breathing differently: three quick alive voices at the round table, overlapping, and nothing at all at the family table but the slow scrape of a knife on china, faint, off frame left. Fatiha's rings against the cloth; one short breath of a laugh; the cups and glasses never touched. Underneath: the fish-tank pump and its bubbles, the kitchen extractor's low drone behind the beaded curtain, the drinks cooler cycling, wet tyres passing faint outside. No music.

POSITIVE CONSTRAINTS — CHECK EVERY FRAME AGAINST THESE
Every named reference above is matched 100%: same face, same build, same wardrobe, same wear. Nobody is better groomed, better lit, better dressed or better rested than the shot before; wardrobe, hair, dirt, damage and wear do not improve or clean themselves up. Props stay exactly where the prop layout puts them. The light level, the weather and the time of day do not move inside this generation.
The choreography written in the FRAME MAP is the whole performance: no gesture, step, head turn, prop interaction or expression beyond it. Between described movements every body holds its last position naturally, breathing and blinking, never frozen and never fidgeting.
Nobody looks at the lens at any point. Nobody speaks except where DIALOGUE says so.
Every stroke of handwriting anywhere in frame is real handwriting laid out in straight horizontal lines — word-shaped clusters separated by spaces, gathered into sentences and paragraphs — in an invented cursive alphabet whose characters recur again and again the way a real alphabet's do. Unmistakably a script, but no script that exists on earth, and not one word readable in any language: it reads as writing from across the room and as nothing at all up close. Never random scribble, never a scrawl, never abstract mark-making, never decorative squiggles. No signage, no label, no digit, no subtitle, no caption is readable anywhere.
One continuous uncut take at real-time speed, for the exact duration requested. No slow motion, no speed ramp, no added cut.

AVOID
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, readable menus, readable signage, readable lettering, subjects looking at camera, slow motion, morphing objects, extra people in frame, other diners, waiters, extra gestures, improvised actions, wandering hands, repositioned props, appearing or disappearing objects, a cut inside the shot, camera movement, dolly, pan, zoom, push in, handheld shake, a flashback, a cutaway, an insert, another place, another time, period costume, the women telling a story, storytelling performance, a speaker addressing the room, anyone looking toward the family table, Mei turning toward the family table, Mei looking at the girl, Mei making eye contact with the family table, anyone lowering their voice, the girl turning to camera, the girl's face readable, the girl speaking, anyone at the family table speaking, the father lifting his eyes, drinking, pouring, changing tea levels, a stool at the counter, a bowl on a stool, anything standing at the counter's far end, the room brightening on the laughter, warm saturated grade, golden light, sitcom lighting, rushed movements, theatrical acting, overacting, posed smiles, any red anywhere, red lanterns, red tablecloths, red menus, red packaging, generated music, uncanny smoothness, plastic skin, beauty filter, CGI look, video-game lighting, frozen characters, statue-like stillness, mannequin pose, freeze-frame stillness.
```








*⚠ **POINT DE COUPE — 7,2 s au montage sur 10 s de rushes.** Garder `[0.30s]` → `[7.50s]`. **Débit** : 25 mots
en 6,2 s ≈ **4 mots/s**, avec trois chevauchements de 0,15 à 0,20 s aux joints (Mei sur Fatiha, Fatiha sur Mei,
Mei sur Asha). Le demi-silence `[6.55-7.05s]` **fait partie du plan** : c'est lui qui rend le chaînage
invisible. **Sauvegarder le DERNIER FRAME de 5B-1 : il est la start frame de 5B-2.***

---


## VIDÉO 5B-2 — plan 5.2, seconde moitié, jusqu'à « More tea? » *(8 s de rushes → 5,8 s au montage · Elements : @Nora + @Mei + @Asha + @Fatiha + @Restaurant · start frame : LE DERNIER FRAME DE 5B-1 — repli : LIEU-07 IMAGE 4)*

```
SCENE CONTEXT
The same three women at the same table, still talking across each other about the same man — and then they run out of it. One of them lays her chopsticks down and says the last thing anybody has to say about him; the table goes quiet by itself for half a second; and then the oldest one asks about tea and it is over. Nothing has happened, for them. A metre and a half away, in the soft foreground, the teenage girl has not moved, and not one of them notices. ONE single continuous shot, no cut. Every second is choreographed below; nothing beyond it may be invented. 8 seconds, one continuous framing, no cut.

CONTINUITY REFERENCE — THIS SHOT CONTINUES THE ATTACHED VIDEO
THE VIDEO ATTACHED TO THIS GENERATION is the shot that immediately precedes this one (5B-1), in the same place and the same minute. THIS GENERATION IS ITS DIRECT CONTINUATION and must feel like the same take filmed by the same operator seconds later: carry over its exact light level and direction, its grain, its skin rendering, the state the bodies and the props are left in, AND ABOVE ALL THE WAY ITS CAMERA BEHAVES — the same height, the same kind of movement, the same speed, the same breathing weight in the frame. Pick the scene up exactly where the attached video leaves it. Do not restart it, do not reset the room, do not relight it, do not change operator. The new framing is the one the FRAME MAP gives below, but it is reached by the same camera, moving the same way.

ACTIVE REFERENCES
@Nora: Nora, fifteen, long dark brown unwashed hair, grey-green eyes, pale olive skin gone colourless, bitten lips, heavy lids over grey hollows, thin build. Running on empty: grief has made her polite and absent — she answers, she says thank you, and none of it reaches her face. She goes very still before anything shows. NOTHING RED ON HER. 100% matches the reference.
@Mei: Mei, fifty-eight, who runs the restaurant — brisk, busy, entirely unmystified, and still running it while this happens. What she passes on she passes on the way she would pass on a phone number: practical, low, half over her shoulder, already moving. Dark green apron stained at the hip. 100% matches the reference.
@Asha: Asha, fifty-two, upright, deliberate, economical. She listens longer than is comfortable before saying anything, and when she speaks it is short and settled. Her hands are still when she talks. Warmth in her comes out as attention, not as smiling. 100% matches the reference.
@Fatiha: Fatiha, sixty-six, and everything she says goes through her hands first. Quick, warm, interrupting, laughing at the edge of serious things. She touches the arm of whoever she talks to, mentions what broke her the way you mention the weather, and moves on. 100% matches the reference.
@Restaurant: Mei's restaurant — amber lanterns, green tablecloths, a green fish tank. No red anywhere, no legible signage. 100% matches the reference.

TEMPERAMENT, NORA A fifteen-year-old running on empty. Grief has made her polite and absent: she answers, she carries the dish back, she says thank you, and none of it reaches her face. Her body is tired before the day starts. She does not cry in front of people — the swollen eyelids come from somewhere else, earlier. When something does move her, she goes very still first, and only then does it show.
TEMPERAMENT, MEI Brisk, busy, entirely unmystified. She runs a restaurant and she is still running it while this is happening. What she passes on, she passes on the way she would pass on a phone number: practical, low, half over her shoulder, already moving to the next thing.
TEMPERAMENT, ASHA Upright, deliberate, economical. She listens longer than most people are comfortable with before she says anything, and when she does speak it is short and settled — a woman used to being believed without raising her voice. Her hands are still when she talks. Warmth in her comes out as attention, not as smiling.
TEMPERAMENT, FATIHA Sixty-six, and everything she says goes through her hands first. Quick, warm, interrupting, laughing at the edge of serious things. She touches the arm of whoever she is talking to. She tells you a thing that broke her the way you would mention the weather, and moves on before you can be sorry about it.

LOCATION MAP
Framing 1 [0.0-8.0s] — camera: THE SAME AXIS, THE SAME FRAMING, NO CUT. Medium three-shot of the round table, eye level, static, locked off, no camera movement of any kind for the whole generation.
Every distance, height and frame position given above is literal and is held exactly; nothing drifts toward a more flattering angle.

FIRST FRAME AND SPATIAL BLOCKING The generation opens on this exact frame: THE SAME AXIS, THE SAME FRAMING, NO CUT. Medium three-shot of the round table, eye level, static, locked off, no camera movement of any kind for the whole generation. Starting positions, exactly the positions the previous shot ended on: @Asha SEATED at x=27%, three-quarter to camera, upright, filling 55% of frame height, chopsticks in her right hand, her eyes on @Fatiha. @Mei SEATED at the back at x=48%, filling 50% of frame height, shoulders square to the counter at screen-right, face in three-quarter from camera-left, her right hand around her cup on the cloth. @Fatiha SEATED at x=73%, three-quarter to camera, filling 55% of frame height, drawing breath, her hands above the cloth. Extreme near foreground SCREEN-LEFT at x=9%, LARGE and SOFT, out of focus: the back three-quarter of @Nora's head and shoulder, filling 62% of frame height, her raised right hand and the stopped fork a soft shape. Behind them the fish tank's green field. This is the frame the first video frame must already be, before anything moves: nothing is settling into place, nothing fades up, nothing is mid-transition.

FORMAT MODE
One single continuous uncut take, 8 seconds long, at real-time speed. No cut, no montage, no dissolve, no speed ramp, no slow motion.

OPTICS
Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described in the FRAME MAP is tack sharp and everything behind it falls off progressively. Focus holds on that plane and breathes naturally with the camera's movement — no deliberate rack focus unless the FRAME MAP calls for one.

CONTINUITY LOCK Every prop named in the layout appears in EVERY frame where its surface is visible, in the same position and state — nothing appears, disappears, multiplies or moves unless the choreography says so. Each character's posture is SEATED and never changes. A character holds exactly the object the choreography puts in their hand — no other utensil or object may materialise.

GEOMETRY — IDENTICAL TO THE SHOT THIS ONE CONTINUES The camera sits in the aisle just past the family table, at eye level, looking at the women's small round table with the green-lit fish tank filling the background behind it and the lacquered counter running away deep at SCREEN-RIGHT. The family table is the square formica table nearest the street window, just outside the frame's LEFT edge, ABOUT A METRE AND A HALF AWAY. @Nora sits at it with her back three-quarter to camera, her head and shoulder in the extreme near foreground screen-left, LARGE and OUT OF FOCUS. At the round table: @Asha at x=27% on the LEFT, @Mei at the BACK at x=48% with her shoulders square to the counter, @Fatiha at x=73% on the RIGHT. @MEI SITS WITH HER BACK THREE-QUARTER TO THE FAMILY TABLE: it lies behind her LEFT shoulder, outside her field of view, and she never turns toward it. NOTHING STANDS AT THE COUNTER'S FAR END: no stool, no bowl, nothing on it.

PROP LAYOUT — FIXED, CARRIED UNCHANGED FROM THE PREVIOUS SHOT THE WOMEN'S ROUND TABLE, under a dark green cloth washed soft by years: at the centre a dented metal teapot, dull with handling, its spout tea-stained at the lip. THREE small white cups of finely crazed porcelain — @Mei's about half full and IN HER RIGHT HAND with its base resting on the cloth, @Asha's about one third full, @Fatiha's nearly empty with a dry tea ring inside. THREE small plain water glasses, each about two thirds full, one just to the right of each cup. NOBODY DRINKS AT ANY POINT AND NO LEVEL IN ANY CUP OR GLASS EVER CHANGES; the teapot is never lifted, never tipped, never poured. TWO small plates of dumplings, their steam long gone, between them. @Fatiha's worn bamboo chopsticks rest across her plate. @Asha's chopsticks are IN HER RIGHT HAND at the start and are laid FLAT ACROSS HER OWN PLATE at [3.45s], where they stay. THE FAMILY TABLE, at the frame's left edge and beyond it: exactly THREE small white cups, no longer steaming, the metal teapot at centre, the fourth place BARE and its chair EMPTY and pushed in — at the extreme left edge, soft and dark, only the top rail of that empty chair reads. @Nora's fork is IN HER RIGHT HAND, STOPPED in the air above her plate, a piece of food speared on it — it never travels to her mouth.

FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND

SHOT [0.0-8.0s] — THE SAME AXIS, THE SAME FRAMING, NO CUT. Medium three-shot of the round table, eye level, static, locked off, no camera movement of any kind for the whole generation.
[0.0s] Starting positions, exactly the positions the previous shot ended on: @Asha SEATED at x=27%, three-quarter to camera, upright, filling 55% of frame height, chopsticks in her right hand, her eyes on @Fatiha. @Mei SEATED at the back at x=48%, filling 50% of frame height, shoulders square to the counter at screen-right, face in three-quarter from camera-left, her right hand around her cup on the cloth. @Fatiha SEATED at x=73%, three-quarter to camera, filling 55% of frame height, drawing breath, her hands above the cloth. Extreme near foreground SCREEN-LEFT at x=9%, LARGE and SOFT, out of focus: the back three-quarter of @Nora's head and shoulder, filling 62% of frame height, her raised right hand and the stopped fork a soft shape. Behind them the fish tank's green field.
[0.0-0.20s] Held, nothing moving but breath.
[0.20-0.95s] @ASHA, level, dropping it in: "He's everybody's."
[0.85-2.65s] @FATIHA, coming in over the tail of that, quick, one hand turning palm-up on the cloth and settling again: "He asks for something first. Always something small."
[2.50-3.45s] @MEI CUTS IN, flat, finishing it for her, without lifting her eyes from her cup: "Never a big one."
[3.45-3.70s] @ASHA lays her chopsticks down FLAT ACROSS HER OWN PLATE, one small wooden sound, and leaves her hand beside them. Nothing else moves.
[3.70-5.30s] @ASHA, level, unhurried, the last thing anybody has to say: "And nobody has ever seen his face."
[5.30-5.85s] THE BEAT. The table goes quiet all by itself, the way a table goes quiet — no reaction, no glance exchanged, nobody looking at anybody, nobody looking toward the family table, nobody looking at the girl. @Fatiha's eyes drop to the teapot. @Mei blinks once. @Asha's hand stays beside her chopsticks. Half a second, no more.
[5.85-6.35s] @FATIHA, already elsewhere, to @Mei, ordinary: "More tea?" — and on the second word her right hand goes out and closes around the dented metal teapot's handle. She does not lift it.
[6.35-8.0s] Held to the end, no further movement beyond micro-life: @Fatiha's hand on the teapot handle, @Mei giving one small nod, @Asha's eyes coming back up to the two of them — the three of them already onto something else. The teapot is never lifted. In the soft foreground @Nora has not moved at all: the fork still up, the shoulder still, the chin still turned a few degrees toward them.

SUBJECT LOCK, FATIHA The exact woman of the reference @Fatiha — sixty-six, Moroccan American, short and rounded with soft shoulders and expressive hands; warm golden-olive skin with sun spots, dark hazel-brown eyes with heavy hooded lids and a lively animated gaze, deep lines around the mouth, the small faded traditional dots tattooed on the chin; the soft patterned ochre and dusty-blue headscarf tied at the nape; the long charcoal wool cardigan over the mustard and cream patterned tunic, small gold hoop earrings, several thin gold rings. Her last line is thrown away, warm and ordinary, as if the previous minute had never happened. She never looks at the lens.

SUBJECT LOCK, ASHA The exact woman of the reference @Asha — fifty-two, Kenyan American, tall, slim and upright with a long neck and squared shoulders; deep rich dark brown skin, high sharply defined cheekbones, full lips in a natural deep berry-brown, large calm wide-set dark brown eyes with a steady gaze, short neat black locs gathered back with a plain wooden pin, a few grey strands at the temple; the fine-gauge cream cotton polo-neck, the long olive-and-indigo patterned open coat, small gold hoop earrings, the single thin gold bangle. She says her last line flat and without weight — she is stating a known thing, not delivering anything. She never looks at the lens.

SUBJECT LOCK, MEI The exact woman of the reference @Mei — fifty-eight, Chinese American, short and sturdy, warm ivory skin dulled by decades of kitchen heat, deep laugh lines, dark brown almond eyes with a quick direct gaze; the long black hair going grey twisted up in a low bun held with the single lacquered wooden hairpin, loose strands at the temples; the plain white short-sleeved cotton shirt, the long dark green cotton apron stained at the hip, the thin jade bangle on the left wrist. SHE SITS WITH HER BACK THREE-QUARTER TO THE FAMILY TABLE AND HER EYES NEVER LEAVE HER TWO FRIENDS AND HER OWN CUP: not one glance toward the family table, not one glance toward the girl, not once, not for a single frame. She never looks at the lens.

SUBJECT LOCK, NORA The exact girl of the reference @Nora — fifteen, long dark brown wavy hair, unwashed, half-tied back; grey-green eyes with a slight downward outer tilt, heavy lids with grey shadowed hollows beneath, faint freckles, chapped bitten lips, pale olive skin drained of colour, thin adolescent build, shoulders rounded inward; the oversized faded charcoal-grey hooded sweatshirt with worn cuffs, dark indigo jeans, NO parka. In this generation she is SOFT and OUT OF FOCUS in the extreme foreground, back three-quarter to camera; her face is never readable, she never turns to the lens, she never speaks, and nothing in her moves at all. Her fork stays stopped in the air.

CROSS-FRAME RULES ONE single continuous shot with no cut inside it and no camera movement whatsoever, on exactly the axis and framing of the shot it continues — same three women in the same seats at the same sizes, same faces, same wardrobe, same tea levels, same green field behind them. @Restaurant is the same room as every other generation of this sequence, and nothing stands at the counter's far end. Nothing on either table changes except @Asha's chopsticks going down at [3.45s] and @Fatiha's hand arriving on the teapot handle at [6.0s]; nothing is drunk, nothing is poured, no level moves. None of the three ever names what she is talking about, and no proper name is ever translated or explained. None of them looks toward the family table, lowers her voice, or plays a line to anybody outside her own table; the last line and the silence after it are addressed to nobody. The girl never turns her face to camera and never speaks. Nobody looks at the lens. The light does not change at any point. NO INVENTED ACTION: If a body part is not described as moving, it does not move. No gesture, step, head turn, prop interaction or expression change beyond the choreography written above; between described movements every body holds its last described position naturally (breathing, blinking, micro-sway only). CONTINUITY LOCK above and the POSITIVE CONSTRAINTS below apply in full.

CONTINUITY — WHAT MUST NOT DRIFT
Wardrobe, hair, dirt, damage and wear are exactly as the references define them and do not improve, clean themselves up or change between shots. Nobody is better groomed, better lit, better dressed or better rested than in the shot before. Props stay where the prop layout puts them. Weather, time of day and light level do not move inside a sequence. Nobody looks at the lens at any point.

LOCATION @Restaurant — the small old family-run Chinese restaurant of the act-one dinner, unchanged and older for it: six formica tables on tubular chrome legs dulled and pitted at the feet, each under a dark green cloth washed soft by years; wooden chairs, their varnish worn pale where hands pull them out, one with a re-glued back rail; the lacquered service counter, its lacquer finely crazed and rubbed to bare wood at the corner where trays slide; the green-lit fish tank, a faint limescale line at the waterline, a slow stream of bubbles, two dark carp barely moving; the beaded curtain to the kitchen, a few strands short; paper lanterns in amber and brass, their paper sun-faded, one panel neatly mended; the window onto the wet street, condensation creeping up the lower glass, the roller blind half down. Nothing stands at the counter's far end: no stool, no bowl, nothing on it. Only the two tables described in the layout are occupied; every other table is empty and cleared, chairs squared — a half-empty room on a slow night. No red anywhere. No readable menus, no lettering anywhere, no other diners, no staff.

LIGHT The amber paper lanterns burning low — weak tungsten bulbs inside the paper, each throwing a soft pool barely a metre wide that dies into shadow between the tables, real falloff, the paper itself glowing unevenly where it has thinned; the green fluorescent glow of the fish tank behind the round table, the strongest colour in the room, rippling faintly on the counter lacquer; the counter light dim; cold blue night through the window glass; a desaturated grey-blue cast over the whole room, gently underexposed, deep blacks under the empty tables and in the corners. The exposure and the colour are exactly the same in the last frame as in the first, and exactly the same as in the shot this one continues.

DIALOGUE Quick, overlapping at the joins, about four words a second, nobody projecting, nobody performing. [0.20-0.95s] @Asha, level: "He's everybody's." — [0.85-2.65s] @Fatiha, over the tail of that: "He asks for something first. Always something small." — [2.50-3.45s] @Mei, cutting in flat, eyes on her own cup: "Never a big one." — [3.70-5.30s] @Asha, unhurried and without weight: "And nobody has ever seen his face." — HALF A SECOND OF SILENCE, [5.30-5.85s], nobody speaking, nobody reacting — [5.85-6.35s] @Fatiha, already elsewhere, to @Mei, completely ordinary: "More tea?" — Nobody else speaks. Not one word is spoken at the family table.

LAST FRAME The women's round table under the green tank glow, already onto something else: @Fatiha's right hand closed on the dented metal teapot's handle, the pot still on the cloth; @Mei mid-nod, her cup still in her right hand; @Asha's chopsticks lying flat across her plate, her eyes back on the two of them; in the extreme soft left foreground the back of @Nora's head and shoulder, unmoved, her fork still stopped in the air; nothing at the counter's far end.



CHARACTER PERFORMANCE
Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through nothing else: no added expression, no widened eyes, no trembling lip, no theatrical breath. What is not written does not happen. Between the written events every body simply holds its last position, breathing, blinking and drifting a few millimetres, never frozen and never fidgeting.
All four characters in frame are SEATED for the entire generation; nobody rises, nobody changes seats, nobody leaves frame. @Mei never turns her head or body toward the family table. @Nora stays back three-quarter to camera and never turns her face to the lens. Her fork stays up.

PHYSICS — WEIGHT, INERTIA, CONTACT
Everything in frame has mass and obeys it. A body starts and stops with its own weight: it settles into a position rather than snapping into it, and a limb leads while the torso follows a beat later. Feet take the ground with real contact and real friction — on wet stone a step is slightly damped, never sliding, never skating. Clothing lags behind the body that moves it, keeps its own folds and swings back late; hair moves a beat behind the head and comes to rest slowly.
Objects have the mass their material implies. A wooden door swings on its hinges at the speed its own weight allows: it starts slowly, gathers a little, and is slowed at the end by its own friction and the resistance of the hinge — it never floats, never snaps open, never accelerates on its own, and it never moves before something moves it. Hands deform what they touch: fingers flatten slightly against a hard surface, fabric compresses under a grip, a held object presses back. Nothing passes through anything. Nothing changes speed without a cause visible in the frame.

WORLD — AFTER
A grey-blue world, gently underexposed, roughly two thirds of a stop below normal. Sparse motivated sources only — one bulb, one window, one sodium lamp — and deep quiet blacks between them. Colour is drained but not absent: what survives is amber from a flame, sodium orange from a street, sea-green from tile. Never a saturated hue. No red anywhere, flames included.

CINEMATOGRAPHY
Naturalistic available-light cinematography in the raw realist tradition. One motivated source at a time and no fill — a single bulb, a single window, a distant sodium lamp — with deep quiet blacks between them. Deliberately underexposed, roughly two thirds of a stop below normal, protecting the shadows and keeping real separation and texture inside them. Highlights restrained, never blown, holding texture in the filament and the wet stone. Low gentle contrast. Muted desaturated true-to-life colour: what survives is amber from a flame, sodium orange from a street, sea-green from tile — never a saturated hue, and never red.

FILM EMULATION — THE SAME STOCK FROM THE FIRST FRAME TO THE LAST
Shot on Kodak Vision3 500T 5219 tungsten colour negative, one stock, one lab, for the entire film, rated at box speed and printed flat. Cool naturalistic colour science; shadows falling slightly blue-green and holding real separation and texture inside them; skin tones understated, never warmed up, never rosy. Gentle contrast, soft highlight roll-off, highlights restrained and never blown, a faint halation ring blooming around every practical source. Moderate fine grain that grows in the underexposed areas and breathes with the exposure. Not glossy, not digital, not warm. Daylight scenes are the same stock corrected with an 85 filter, never a different look.

CAMERA REGISTER — LOCKED
The camera is placed, and it stays. Nobody is followed, nothing is reframed, and when a body leaves the frame the frame does not go after it. The only life left in the image is the residual human weight the CAMERA paragraph below describes — the same drift of a few millimetres, never more, and never a reframe. This stillness is not neutrality and must never read as a surveillance camera: it is what the film lost when it lost her, and it should feel like a breath being held.

CAMERA — OPERATED, NOT SIMULATED
One anamorphic lens set throughout: slight barrel distortion at the frame edges, oval out-of-focus highlights, mild edge softness, faint vignetting, vintage lens character. Focus is pulled by a human hand — it arrives a few frames late, occasionally overshoots by a hair and settles back, and breathes with the operator's pace. Every held frame keeps a residual human weight in it, a drift of a few millimetres: never a locked robotic stillness, never a shake. No digital sharpening, no edge halos, no noise-reduction smear, no beauty retouching, no plastic skin, no CGI gloss.

PHOTOGRAPHIC REALISM
True skin texture with visible pores and fine hairs, real fabric weave, seams and wrinkles that crease with movement, worn surfaces with real wear, natural asymmetry, natural motion blur in every movement. Deliberately underexposed where the scene calls for it, protecting the shadows and retaining detail inside them: no banding, no posterisation, no crushed flat blacks, no smeared low-light noise, no digital mush.

AUDIO
SFX only. No music. No background music of any kind, no score, no drone, no ambient pad. Three quick voices at the round table, overlapping, then the small wooden sound of chopsticks laid on a plate, then one flat sentence, then half a second in which the room's own noise is suddenly audible — the fish-tank pump and its bubbles, the kitchen extractor's low drone behind the beaded curtain, the drinks cooler cycling, wet tyres passing outside — and then an ordinary question and a hand closing on a metal handle. At the family table, off frame left, nothing but the slow scrape of a knife on china, faint, unbroken, all the way through. No music.

POSITIVE CONSTRAINTS — CHECK EVERY FRAME AGAINST THESE
Every named reference above is matched 100%: same face, same build, same wardrobe, same wear. Nobody is better groomed, better lit, better dressed or better rested than the shot before; wardrobe, hair, dirt, damage and wear do not improve or clean themselves up. Props stay exactly where the prop layout puts them. The light level, the weather and the time of day do not move inside this generation.
The choreography written in the FRAME MAP is the whole performance: no gesture, step, head turn, prop interaction or expression beyond it. Between described movements every body holds its last position naturally, breathing and blinking, never frozen and never fidgeting.
Nobody looks at the lens at any point. Nobody speaks except where DIALOGUE says so.
Every stroke of handwriting anywhere in frame is real handwriting laid out in straight horizontal lines — word-shaped clusters separated by spaces, gathered into sentences and paragraphs — in an invented cursive alphabet whose characters recur again and again the way a real alphabet's do. Unmistakably a script, but no script that exists on earth, and not one word readable in any language: it reads as writing from across the room and as nothing at all up close. Never random scribble, never a scrawl, never abstract mark-making, never decorative squiggles. No signage, no label, no digit, no subtitle, no caption is readable anywhere.
One continuous uncut take at real-time speed, for the exact duration requested. No slow motion, no speed ramp, no added cut.

AVOID
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, readable menus, readable signage, readable lettering, subjects looking at camera, slow motion, morphing objects, extra people in frame, other diners, waiters, extra gestures, improvised actions, wandering hands, repositioned props, appearing or disappearing objects, a cut inside the shot, camera movement, dolly, pan, zoom, push in, handheld shake, a flashback, a cutaway, an insert, another place, another time, the women telling a story, storytelling performance, a speaker addressing the room, a dramatic pause, a meaningful glance exchanged, anyone looking toward the family table, Mei turning toward the family table, Mei looking at the girl, anyone looking at the girl, anyone lowering their voice, the girl turning to camera, the girl's face readable, the girl speaking, anyone at the family table speaking, the father lifting his eyes, lifting the teapot, pouring tea, drinking, changing tea levels, a stool at the counter, a bowl on a stool, anything standing at the counter's far end, the room brightening, warm saturated grade, golden light, sitcom lighting, rushed movements, theatrical acting, overacting, posed smiles, any red anywhere, red lanterns, red tablecloths, red menus, red packaging, generated music, uncanny smoothness, plastic skin, beauty filter, CGI look, video-game lighting, frozen characters, statue-like stillness, mannequin pose, freeze-frame stillness.
```








*⚠ **POINT DE COUPE — 5,8 s au montage sur 8 s de rushes.** Garder `[0.20s]` → `[6.50s]`, soit **6,3 s** dont
**0,5 s d'insert 5C recouvre l'image** (voir ci-dessous) : **5,8 s de cette génération à l'écran.**
5B-1 (7,2 s) + 5B-2 (5,8 s) = **13,0 s**, la durée exacte du script.*

*⚠ **OÙ TOMBE L'INSERT 5C — la seule coupe de tout le plan 5.2.** Il recouvre `[5.15s]` → `[5.85s]` de 5B-2,
soit **0,70 s** : on quitte les femmes 0,15 s avant la fin de la phrase d'Asha (elle continue au son), les mains
de Sam s'arrêtent net dessus, la demi-seconde de silence se joue sur elles, et on revient sur la table des
femmes juste à temps pour « More tea? ». **Aucune parole n'est perdue** — l'insert ne mange que du silence.
**Ne jamais le déplacer sur « More tea? »** : il rendrait la réplique lourde, et c'est sa légèreté qui coupe.*

---


## VIDÉO 5C — l'insert des mains de Sam *(6 s de rushes → 0,7 s au montage · Elements : @Sam + @Restaurant · aucune start frame — l'insert est décrit au prompt)*

```
SCENE CONTEXT
Two large workman's hands cut a child's food, slowly and evenly, the way they have all evening. A woman's voice says something across the room, off screen — and the hands stop dead, mid-cut, for half a second. Then they start again at exactly the same rhythm, as if nothing had happened. ONE single continuous shot, no cut. NOTHING ABOVE THE FOREARMS IS EVER IN FRAME: no face, no head, no shoulders, no chin, no eyes, no reflection of a face, at any point. Every second is choreographed below; nothing beyond it may be invented. 6 seconds, one continuous framing, no cut.

CONTINUITY REFERENCE — THIS SHOT CONTINUES THE ATTACHED VIDEO
THE VIDEO ATTACHED TO THIS GENERATION is the shot that immediately precedes this one (5B-2), in the same place and the same minute. THIS GENERATION IS ITS DIRECT CONTINUATION and must feel like the same take filmed by the same operator seconds later: carry over its exact light level and direction, its grain, its skin rendering, the state the bodies and the props are left in, AND ABOVE ALL THE WAY ITS CAMERA BEHAVES — the same height, the same kind of movement, the same speed, the same breathing weight in the frame. Pick the scene up exactly where the attached video leaves it. Do not restart it, do not reset the room, do not relight it, do not change operator. The new framing is the one the FRAME MAP gives below, but it is reached by the same camera, moving the same way.

ACTIVE REFERENCES
@Sam: Sam two years later, a month of badly trimmed beard, ten kilos heavier, grey under the eyes. Two years without speaking — not sullen, emptied. He moves through his own house like a guest, shoulders forward, eyes down and to the side. Every gesture is finished; none is explained. 100% matches the reference.
@Restaurant: Mei's restaurant — amber lanterns, green tablecloths, a green fish tank. No red anywhere, no legible signage. 100% matches the reference.

TEMPERAMENT, SAM AFTER Two years without speaking. Not sullen — emptied. He moves through his own house like a guest: slower, heavier, shoulders carried forward, eyes down and to the side. He still does things for his daughter, but wordlessly and out of her sight. Every gesture is finished; none is ever explained. When he is alone his face does what it wants; the moment she is in the room it does nothing at all.

LOCATION MAP
Framing 1 [0.0-6.0s] — camera: Tight insert, high angle, static, locked off, straight down onto the plate. Shallow focus: the plate and the hands sharp, the cloth falling off soft toward the frame edges.
Every distance, height and frame position given above is literal and is held exactly; nothing drifts toward a more flattering angle.

FIRST FRAME AND SPATIAL BLOCKING The generation opens on this exact frame: Tight insert, high angle, static, locked off, straight down onto the plate. Shallow focus: the plate and the hands sharp, the cloth falling off soft toward the frame edges. Frame contents, held until described otherwise: @SAM'S TWO HANDS ONLY — large, the skin cracked across the knuckles, the nails short and rimmed, the fingertips faintly stained dark blue-black; the worn-handled knife in the right at x=58%, the fork in the left at x=38%, both working over the plate. The forearms enter from the top of frame in the olive-drab canvas work-jacket sleeves, the LEFT cuff torn and frayed; the thin worn steel wedding band on the left hand. NO FACE, NO HEAD, NO SHOULDERS IN FRAME. This is the frame the first video frame must already be, before anything moves: nothing is settling into place, nothing fades up, nothing is mid-transition.

FORMAT MODE
One single continuous uncut take, 6 seconds long, at real-time speed. No cut, no montage, no dissolve, no speed ramp, no slow motion.

OPTICS
Anamorphic 85 mm f/2 equivalent. Depth of field wide open at that stop: the plane described in the FRAME MAP is tack sharp and everything behind it falls off progressively. Focus holds on that plane and breathes naturally with the camera's movement — no deliberate rack focus unless the FRAME MAP calls for one.

CONTINUITY LOCK Every prop named in the layout appears in EVERY frame where its surface is visible, in the same position and state — nothing appears, disappears, multiplies or moves unless the choreography says so. The hands hold exactly the knife and the fork the choreography puts in them — no other utensil or object may materialise, and neither is ever put down.

GEOMETRY The camera looks straight down at the family table's dark green cloth from about seventy centimetres above it, tight enough that the plate and two forearms fill the frame. The forearms enter from the TOP of frame. The table's far edge and the room beyond are OUT OF FRAME. The women's round table, the counter and every face in the restaurant are OUT OF FRAME and stay out of frame.

PROP LAYOUT — FIXED @Milo's plate of flat noodles and greens, thick white china with the glaze worn grey at the rim, centred at x=48% and filling about 45% of frame height, half the noodles already cut into small pieces, the last of the steam long gone. Under it the dark green cloth washed soft and bobbled by years, its pressed fold-crease running across the lower frame, one old pale stain near the near edge. At the top-right frame edge, soft: the rim and handle of a small white porcelain cup, glaze finely crazed, and the round shoulder of a dented metal teapot. At the top-left frame edge, soft and cut by the frame: the edge of a second plate, barely touched. IN THE HANDS: a worn-handled knife in the RIGHT hand, its wooden handle darkened and slightly loose at the tang; a plain fork in the LEFT. Nothing else is in frame at any point.

FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND

SHOT [0.0-6.0s] — Tight insert, high angle, static, locked off, straight down onto the plate. Shallow focus: the plate and the hands sharp, the cloth falling off soft toward the frame edges.
[0.0s] Frame contents, held until described otherwise: @SAM'S TWO HANDS ONLY — large, the skin cracked across the knuckles, the nails short and rimmed, the fingertips faintly stained dark blue-black; the worn-handled knife in the right at x=58%, the fork in the left at x=38%, both working over the plate. The forearms enter from the top of frame in the olive-drab canvas work-jacket sleeves, the LEFT cuff torn and frayed; the thin worn steel wedding band on the left hand. NO FACE, NO HEAD, NO SHOULDERS IN FRAME.
[0.0-1.6s] The knife and fork work, slow and even, cutting flat noodles into small pieces — the same unhurried rhythm as all evening, the wrist heavy, the fork holding the food down while the knife draws through. Nothing else moves. Off screen, faint and far, three women's voices at another table, unintelligible.
[1.6-3.2s] The rhythm continues, unchanged. OFF SCREEN, from across the room, a woman's level voice comes through the others, clearly: "And nobody has ever seen his face."
[3.2-3.7s] THE HANDS STOP DEAD, on the word "face", mid-cut. Absolutely still: the knife halfway through a piece, the fork holding the food down, the knuckles motionless, the forearms locked. Only the faintest breath moves the canvas sleeve, and one fingertip settles a millimetre on the knife handle. Half a second, no more. The room's own noise fills it.
[3.7-4.3s] The hands start again — exactly the same rhythm as before, exactly the same grip, as if nothing had happened. Not one finger has changed position. No face has entered frame.
[4.3-6.0s] Held to the end: the knife and fork working over the plate, slow and even, unbroken. Nothing else in the frame moves. Off screen the voices have moved on to something ordinary.

SUBJECT LOCK, SAM Only the forearms and hands of the exact man of the reference @Sam: large hands, the skin cracked across the knuckles and dry at the finger joints, short rimmed nails, the fingertips faintly stained dark blue-black — a workman's hands and nothing more; the thin worn steel wedding band on the left ring finger, dulled and slightly out of round; the olive-drab canvas work-jacket sleeves, the weave visible, the LEFT cuff torn and frayed, a faded stain low on the right forearm. HE IS NEVER SEEN ABOVE THE FOREARMS: no face, no profile, no chin, no cheek, no eyes, no hair, no shoulder, no neck, no reflection of a face in the cup or the teapot, in any frame, ever. He never speaks and there is no reverse angle on him anywhere in this generation.

CROSS-FRAME RULES ONE single continuous shot with no cut inside it and no camera movement whatsoever. The plate, the cloth, the cup rim and the teapot shoulder stay exactly where the prop layout puts them from the first frame to the last. The knife stays in the right hand and the fork in the left for the whole shot; neither is ever put down, swapped or set on the plate. The cutting rhythm before the stop and the cutting rhythm after the stop are identical. NOBODY ELSE EXISTS ON SCREEN: no second pair of hands, no child's hands, no waitress, no shape at the frame edge — the voices are all off screen and none of their owners is ever seen. No face of any kind appears in this generation. Nobody looks at the lens because no eyes exist in it. NO INVENTED ACTION: If a body part is not described as moving, it does not move. No gesture, step, head turn, prop interaction or expression change beyond the choreography written above; between described movements every body holds its last described position naturally (breathing, blinking, micro-sway only). CONTINUITY LOCK above and the POSITIVE CONSTRAINTS below apply in full.

CONTINUITY — WHAT MUST NOT DRIFT
Wardrobe, hair, dirt, damage and wear are exactly as the references define them and do not improve, clean themselves up or change between shots. Nobody is better groomed, better lit, better dressed or better rested than in the shot before. Props stay where the prop layout puts them. Weather, time of day and light level do not move inside a sequence. Nobody looks at the lens at any point.

LOCATION @Restaurant — the family table of the small old family-run Chinese restaurant, seen from directly above and only that: the dark green cloth washed soft and bobbled by years, its pressed fold-crease permanent, an old pale stain near the near edge, the chipped black corner of the formica just readable at the extreme lower frame edge; thick white china with the glaze worn grey by decades of stacking; a small white porcelain cup and a dented metal teapot soft at the top-right edge. The rest of the room — the counter, the fish tank, the window, the other tables — is entirely out of frame. Nothing stands at the counter's far end anywhere in this sequence. No red anywhere. No readable menus, no lettering anywhere, no logos.

LIGHT One weak amber lantern pool from directly above, falling on the plate and the hands and dying into shadow at the frame edges, real falloff, the paper of the lantern itself out of frame; a faint cool green spill from the fish tank reaching the far edge of the cloth; a desaturated grey-blue cast over everything, gently underexposed, deep blacks at the corners of frame. The exposure does not change at any point — the light is exactly the same before, during and after the stop. No golden warmth, no cosy atmosphere, no light change on the moment.

DIALOGUE No line is spoken on screen; nobody in frame has a mouth in frame. OFF SCREEN ONLY, from another table across the room, a woman's level unhurried voice, coming through the murmur of two others: [1.6-3.2s] "And nobody has ever seen his face." Nothing else is intelligible, before or after.

LAST FRAME Straight down on the plate of flat noodles on the dark green cloth: the worn-handled knife in the right hand and the fork in the left, mid-cut, the olive-drab canvas sleeves with the torn left cuff entering the top of frame, the thin worn steel wedding band catching a low amber gleam, the fingertips faintly stained dark blue-black. No face anywhere in frame.



CHARACTER PERFORMANCE
Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through nothing else: no added expression, no widened eyes, no trembling lip, no theatrical breath. What is not written does not happen. Between the written events every body simply holds its last position, breathing, blinking and drifting a few millimetres, never frozen and never fidgeting.
Only @Sam's two forearms and hands exist in this generation, entering from the top of frame, working over the plate for the whole shot. He is SEATED off frame and never rises. He never speaks. Nothing above the forearms is ever in frame.

PHYSICS — WEIGHT, INERTIA, CONTACT
Everything in frame has mass and obeys it. A body starts and stops with its own weight: it settles into a position rather than snapping into it, and a limb leads while the torso follows a beat later. Feet take the ground with real contact and real friction — on wet stone a step is slightly damped, never sliding, never skating. Clothing lags behind the body that moves it, keeps its own folds and swings back late; hair moves a beat behind the head and comes to rest slowly.
Objects have the mass their material implies. A wooden door swings on its hinges at the speed its own weight allows: it starts slowly, gathers a little, and is slowed at the end by its own friction and the resistance of the hinge — it never floats, never snaps open, never accelerates on its own, and it never moves before something moves it. Hands deform what they touch: fingers flatten slightly against a hard surface, fabric compresses under a grip, a held object presses back. Nothing passes through anything. Nothing changes speed without a cause visible in the frame.

WORLD — AFTER
A grey-blue world, gently underexposed, roughly two thirds of a stop below normal. Sparse motivated sources only — one bulb, one window, one sodium lamp — and deep quiet blacks between them. Colour is drained but not absent: what survives is amber from a flame, sodium orange from a street, sea-green from tile. Never a saturated hue. No red anywhere, flames included.

CINEMATOGRAPHY
Naturalistic available-light cinematography in the raw realist tradition. One motivated source at a time and no fill — a single bulb, a single window, a distant sodium lamp — with deep quiet blacks between them. Deliberately underexposed, roughly two thirds of a stop below normal, protecting the shadows and keeping real separation and texture inside them. Highlights restrained, never blown, holding texture in the filament and the wet stone. Low gentle contrast. Muted desaturated true-to-life colour: what survives is amber from a flame, sodium orange from a street, sea-green from tile — never a saturated hue, and never red.

FILM EMULATION — THE SAME STOCK FROM THE FIRST FRAME TO THE LAST
Shot on Kodak Vision3 500T 5219 tungsten colour negative, one stock, one lab, for the entire film, rated at box speed and printed flat. Cool naturalistic colour science; shadows falling slightly blue-green and holding real separation and texture inside them; skin tones understated, never warmed up, never rosy. Gentle contrast, soft highlight roll-off, highlights restrained and never blown, a faint halation ring blooming around every practical source. Moderate fine grain that grows in the underexposed areas and breathes with the exposure. Not glossy, not digital, not warm. Daylight scenes are the same stock corrected with an 85 filter, never a different look.

CAMERA REGISTER — LOCKED
The camera is placed, and it stays. Nobody is followed, nothing is reframed, and when a body leaves the frame the frame does not go after it. The only life left in the image is the residual human weight the CAMERA paragraph below describes — the same drift of a few millimetres, never more, and never a reframe. This stillness is not neutrality and must never read as a surveillance camera: it is what the film lost when it lost her, and it should feel like a breath being held.

CAMERA — OPERATED, NOT SIMULATED
One anamorphic lens set throughout: slight barrel distortion at the frame edges, oval out-of-focus highlights, mild edge softness, faint vignetting, vintage lens character. Focus is pulled by a human hand — it arrives a few frames late, occasionally overshoots by a hair and settles back, and breathes with the operator's pace. Every held frame keeps a residual human weight in it, a drift of a few millimetres: never a locked robotic stillness, never a shake. No digital sharpening, no edge halos, no noise-reduction smear, no beauty retouching, no plastic skin, no CGI gloss.

PHOTOGRAPHIC REALISM
True skin texture with visible pores and fine hairs, real fabric weave, seams and wrinkles that crease with movement, worn surfaces with real wear, natural asymmetry, natural motion blur in every movement. Deliberately underexposed where the scene calls for it, protecting the shadows and retaining detail inside them: no banding, no posterisation, no crushed flat blacks, no smeared low-light noise, no digital mush.

AUDIO
SFX only. No music. No background music of any kind, no score, no drone, no ambient pad. Close and dry, the slow scrape of the knife on china, over and over, the small give of noodles under the blade. Far off and unintelligible, three women's voices at another table — and one of them coming clear through the others for one sentence. Underneath: the fish-tank pump and its bubbles, the kitchen extractor's low drone behind the beaded curtain, the drinks cooler cycling, wet tyres passing outside. During the half-second stop the scraping stops with the hands and the room's own noise is suddenly, briefly audible on its own. No music.

POSITIVE CONSTRAINTS — CHECK EVERY FRAME AGAINST THESE
Every named reference above is matched 100%: same face, same build, same wardrobe, same wear. Nobody is better groomed, better lit, better dressed or better rested than the shot before; wardrobe, hair, dirt, damage and wear do not improve or clean themselves up. Props stay exactly where the prop layout puts them. The light level, the weather and the time of day do not move inside this generation.
The choreography written in the FRAME MAP is the whole performance: no gesture, step, head turn, prop interaction or expression beyond it. Between described movements every body holds its last position naturally, breathing and blinking, never frozen and never fidgeting.
Nobody looks at the lens at any point. Nobody speaks except where DIALOGUE says so.
Every stroke of handwriting anywhere in frame is real handwriting laid out in straight horizontal lines — word-shaped clusters separated by spaces, gathered into sentences and paragraphs — in an invented cursive alphabet whose characters recur again and again the way a real alphabet's do. Unmistakably a script, but no script that exists on earth, and not one word readable in any language: it reads as writing from across the room and as nothing at all up close. Never random scribble, never a scrawl, never abstract mark-making, never decorative squiggles. No signage, no label, no digit, no subtitle, no caption is readable anywhere.
One continuous uncut take at real-time speed, for the exact duration requested. No slow motion, no speed ramp, no added cut.

AVOID
a face, any face, a head, shoulders, a neck, a chin, eyes, hair, a profile, a reflection of a face in the cup, a reflection of a face in the teapot, a reverse angle, a second pair of hands, a child's hands, another person in frame, visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, readable menus, readable signage, readable lettering, subjects looking at camera, slow motion, morphing objects, extra people in frame, extra gestures, improvised actions, wandering hands, repositioned props, appearing or disappearing objects, the knife being put down, the fork being put down, the utensils swapping hands, a cut inside the shot, camera movement, dolly, pan, zoom, push in, focus pull, handheld shake, the hands trembling, the hands clenching, a dramatic gesture, the light changing on the moment, a warm glow, golden light, the room brightening, warm saturated grade, any red anywhere, red tablecloths, red packaging, a red bowl, theatrical acting, overacting, generated music, uncanny smoothness, plastic skin, beauty filter, CGI look, video-game lighting, frozen characters, statue-like stillness, mannequin pose, freeze-frame stillness.
```








*⚠ **POINT DE COUPE — 0,7 s au montage sur 6 s de rushes.** Garder `[3.05s]` → `[3.75s]` : 0,15 s de mains qui
coupent encore, l'arrêt net, la demi-seconde d'immobilité, et on repart. **Le raccord son est déjà écrit** :
la phrase d'Asha est la même dans 5B-2 et dans 5C — au montage on garde la voix de 5B-2 et on ne prend de 5C
que l'image.*

*⚠ **CE QUE CE PLAN NE DOIT PAS DIRE.** C'est un père qui se fige une demi-seconde, vu par personne. Il n'y a
ni contrechamp, ni visage, ni œil, ni musique dessus — **et c'est précisément parce qu'on ne voit pas sa tête
que le film tient jusqu'au bout.** Si le rush contient un seul frame de visage, de menton ou de reflet de
visage dans la tasse, **la prise est à jeter.***

---


## VIDÉO 5D — plan 5.3 « Le père qui coupe, et le trajet du regard » *(12 s de rushes → 6 s au montage · Elements : @Sam + @Nora + @Milo + @Mei + @Asha + @Fatiha + @Restaurant · start frame : LIEU-07 IMAGE 2)*

```
SCENE CONTEXT
First, the family table, wide and silent: a heavy unshaven father cutting his young son's food, eyes down, cutting, cutting — on screen, a busy father and nothing else. Then the camera crosses to the far side of the table and holds close on the teenage girl: her fork still stopped in the air, the mouthful never taken; her eyes come back from the women's table across the room and settle on the empty chair at her own table, and stop there. She puts the fork down without having eaten. She asks nobody anything. Two shots, one hard cut. Every second is choreographed below; nothing beyond it may be invented. 12 seconds, in 2 framings joined by 1 hard cut.

CONTINUITY REFERENCE — THIS SHOT CONTINUES THE ATTACHED VIDEO
THE VIDEO ATTACHED TO THIS GENERATION is the shot that immediately precedes this one (5C), in the same place and the same minute. THIS GENERATION IS ITS DIRECT CONTINUATION and must feel like the same take filmed by the same operator seconds later: carry over its exact light level and direction, its grain, its skin rendering, the state the bodies and the props are left in, AND ABOVE ALL THE WAY ITS CAMERA BEHAVES — the same height, the same kind of movement, the same speed, the same breathing weight in the frame. Pick the scene up exactly where the attached video leaves it. Do not restart it, do not reset the room, do not relight it, do not change operator. The new framing is the one the FRAME MAP gives below, but it is reached by the same camera, moving the same way.

ACTIVE REFERENCES
@Sam: Sam two years later, a month of badly trimmed beard, ten kilos heavier, grey under the eyes. Two years without speaking — not sullen, emptied. He moves through his own house like a guest, shoulders forward, eyes down and to the side. Every gesture is finished; none is explained. 100% matches the reference.
@Nora: Nora, fifteen, long dark brown unwashed hair, grey-green eyes, pale olive skin gone colourless, bitten lips, heavy lids over grey hollows, thin build. Running on empty: grief has made her polite and absent — she answers, she says thank you, and none of it reaches her face. She goes very still before anything shows. NOTHING RED ON HER. 100% matches the reference.
@Milo: Milo, eight, the only one in the house who still says things out loud. He has not learned to be careful around grief, so he asks, and keeps asking. Watchful pale grey-blue eyes that go to his sister's face first. 100% matches the reference.
@Mei: Mei, fifty-eight, who runs the restaurant — brisk, busy, entirely unmystified, and still running it while this happens. What she passes on she passes on the way she would pass on a phone number: practical, low, half over her shoulder, already moving. Dark green apron stained at the hip. 100% matches the reference.
@Asha: Asha, fifty-two, upright, deliberate, economical. She listens longer than is comfortable before saying anything, and when she speaks it is short and settled. Her hands are still when she talks. Warmth in her comes out as attention, not as smiling. 100% matches the reference.
@Fatiha: Fatiha, sixty-six, and everything she says goes through her hands first. Quick, warm, interrupting, laughing at the edge of serious things. She touches the arm of whoever she talks to, mentions what broke her the way you mention the weather, and moves on. 100% matches the reference.
@Restaurant: Mei's restaurant — amber lanterns, green tablecloths, a green fish tank. No red anywhere, no legible signage. 100% matches the reference.

TEMPERAMENT, SAM AFTER Two years without speaking. Not sullen — emptied. He moves through his own house like a guest: slower, heavier, shoulders carried forward, eyes down and to the side. He still does things for his daughter, but wordlessly and out of her sight. Every gesture is finished; none is ever explained. When he is alone his face does what it wants; the moment she is in the room it does nothing at all.
TEMPERAMENT, NORA A fifteen-year-old running on empty. Grief has made her polite and absent: she answers, she carries the dish back, she says thank you, and none of it reaches her face. Her body is tired before the day starts. She does not cry in front of people — the swollen eyelids come from somewhere else, earlier. When something does move her, she goes very still first, and only then does it show.
TEMPERAMENT, MILO Eight years old and the only one in the house who still says things out loud. He has not learned to be careful around grief yet, so he asks, and he keeps asking. Watchful pale grey-blue eyes that go to his sister's face before they go to anything else. He fidgets, he leans, he is always slightly too close to whoever he is talking to.
TEMPERAMENT, MEI Brisk, busy, entirely unmystified. She runs a restaurant and she is still running it while this is happening. What she passes on, she passes on the way she would pass on a phone number: practical, low, half over her shoulder, already moving to the next thing.
TEMPERAMENT, ASHA Upright, deliberate, economical. She listens longer than most people are comfortable with before she says anything, and when she does speak it is short and settled — a woman used to being believed without raising her voice. Her hands are still when she talks. Warmth in her comes out as attention, not as smiling.
TEMPERAMENT, FATIHA Sixty-six, and everything she says goes through her hands first. Quick, warm, interrupting, laughing at the edge of serious things. She touches the arm of whoever she is talking to. She tells you a thing that broke her the way you would mention the weather, and moves on before you can be sorry about it.

LOCATION MAP
Framing 1 [0.0-4.5s] — camera: Wide, eye level, static, locked off, from the middle of the room onto the family table, seen from BEHIND @Nora, the window behind the table at screen-left. SILENT.
Framing 2 [4.5-12.0s] — camera: Close on @Nora from the FAR SIDE of the family table, facing her, eye level, static, locked off, shallow depth of field. The camera stands on her father's side of the table but tight enough on her face that NEITHER @Sam NOR @Milo is ever in frame, and it is never a point-of-view shot. THE FRAME IS MIRRORED WITH RESPECT TO SHOT 1: the empty fourth chair and the women's table are now to the LEFT.
Every distance, height and frame position given above is literal and is held exactly; nothing drifts toward a more flattering angle.

FIRST FRAME AND SPATIAL BLOCKING The generation opens on this exact frame: Wide, eye level, static, locked off, from the middle of the room onto the family table, seen from BEHIND @Nora, the window behind the table at screen-left. SILENT. Frame contents, held until described otherwise: the whole family table in frame. @Sam SEATED at x=56%, three-quarter facing camera, filling 42% of frame height, his bulk low in the chair, shoulders slumped, the month-old beard uneven on the softened jaw, eyes DOWN on his hands. @Milo SEATED at x=38%, facing camera, filling 26% of frame height, chewing small mouthfuls, eyes on his plate. @Nora SEATED at x=20%, back three-quarter to camera, soft, filling 45% of frame height, her right hand raised, the fork stopped in the air. The EMPTY CHAIR at x=76%, pushed in, the bare green cloth in front of it — no plate, no cup. The three cups, the teapot. Deep in the background at x=88%, small, soft and unlit by any event: the women's round table, the three women sitting still, their conversation over. A weak amber lantern pool over the family table; the green tank glow far behind. This is the frame the first video frame must already be, before anything moves: nothing is settling into place, nothing fades up, nothing is mid-transition.

FORMAT MODE
One take of 12 seconds at real-time speed, containing exactly 2 successive framings joined by 1 hard cut, placed at the moments the FRAME MAP gives and nowhere else. Each framing is held completely still between its cuts. No other cut, no montage, no dissolve, no speed ramp, no slow motion.

OPTICS
Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described in the FRAME MAP is tack sharp and everything behind it falls off progressively. Focus holds on that plane and breathes naturally with the camera's movement — no deliberate rack focus unless the FRAME MAP calls for one.

CONTINUITY LOCK Every prop named in the layout appears in EVERY shot where its surface is visible, in the same position and state — nothing appears, disappears, multiplies or moves unless the choreography says so. Each character's posture (SEATED or STANDING) is stated at the top of every shot and never changes off-screen. A character holds exactly the object the choreography puts in their hand — no other utensil or object may materialise.

GEOMETRY — LOCKED FOR THE WHOLE SEQUENCE The family table is the square formica table nearest the street window. The women's round table is THE NEXT TABLE OVER, about a metre and a half away, under the green glow of the fish tank at the end of the lacquered counter — in this generation the three women sit at it, silent and soft in the background, and their conversation is over. Family table: @Sam faces into the room, @Milo sits at his right hand, @Nora sits opposite @Sam; the FOURTH CHAIR — on the side nearest the women's table — is EMPTY and pushed in, its place bare. NOTHING STANDS AT THE COUNTER'S FAR END: no stool, no bowl, nothing on it. FROM @NORA'S SEAT BOTH THINGS THAT MATTER ARE ON THE SAME SIDE, TO HER RIGHT, AND IN THIS ORDER: the women's round table FAR; and nearer, a metre from her hand, the EMPTY FOURTH CHAIR of her own table. That is the order her eyes travel in shot 2 — from the far thing to the near one, and it stops on the near one. SCREEN DIRECTION, AND IT REVERSES BETWEEN THE TWO SHOTS — THIS IS THE MOST IMPORTANT INSTRUCTION IN THIS GENERATION. Shot 1 is filmed from BEHIND @Nora, from the middle of the room, so everything on her right lies to the RIGHT of frame: the empty chair at x=76%, the women's table at x=88%. Shot 2 is filmed from THE OPPOSITE SIDE OF THE TABLE, facing her, so the same things now lie to the LEFT of frame: the empty chair is at the frame's LEFT edge, the women's table is further LEFT and off screen, and @Milo's side of the table is to the RIGHT of frame. IN SHOT 2 EVERY MOVEMENT OF HER EYES GOES TO THE LEFT OF FRAME AND NOWHERE ELSE.

PROP LAYOUT — FIXED THE FAMILY TABLE: the square formica table under a dark green cloth washed soft and bobbled by years. The dented metal teapot at the centre; exactly THREE small white cups of finely crazed porcelain, no longer steaming, one at each occupied place; the FOURTH place BARE — no plate, no cup, no cutlery, bare green cloth — its chair EMPTY and pushed in. @Milo's plate of flat noodles and greens in front of him; @Sam's own plate, barely touched, at his elbow; @Nora's plate of rice and greens, untouched; a small dish of dark soy sauce off-centre — all thick white china, glaze worn grey at the edges. @Sam holds a worn-handled knife in his right hand and a fork in his left, working over MILO'S plate, never his own, for the whole generation. @Nora's fork is IN HER RIGHT HAND, STOPPED in the air at chin height, a piece of food speared on it — it NEVER travels to her mouth, and it comes down onto her plate rim once, at [7.1-8.2s], and stays there. THE WOMEN'S TABLE in the background: the metal teapot with @Fatiha's hand no longer on it, three small white cups and three small water glasses at their levels, untouched, two small plates of dumplings with the steam long gone, wooden chopsticks laid flat across the plates — nothing drunk, nothing eaten, nothing cleared, and the three women sit still and say nothing.

FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND

SHOT 1 [0.0-4.5s] — Wide, eye level, static, locked off, from the middle of the room onto the family table, seen from BEHIND @Nora, the window behind the table at screen-left. SILENT.
[0.0s] Frame contents, held until described otherwise: the whole family table in frame. @Sam SEATED at x=56%, three-quarter facing camera, filling 42% of frame height, his bulk low in the chair, shoulders slumped, the month-old beard uneven on the softened jaw, eyes DOWN on his hands. @Milo SEATED at x=38%, facing camera, filling 26% of frame height, chewing small mouthfuls, eyes on his plate. @Nora SEATED at x=20%, back three-quarter to camera, soft, filling 45% of frame height, her right hand raised, the fork stopped in the air. The EMPTY CHAIR at x=76%, pushed in, the bare green cloth in front of it — no plate, no cup. The three cups, the teapot. Deep in the background at x=88%, small, soft and unlit by any event: the women's round table, the three women sitting still, their conversation over. A weak amber lantern pool over the family table; the green tank glow far behind.
[0.0-4.5s] Nothing happens except this: @Sam's knife and fork work over @Milo's plate, slow, even, unbroken — he cuts, and he cuts, and he cuts. His eyes never leave his hands. He does not speak, he does not look at his son, he does not look at his daughter, he does not look up at anything. @Milo chews. @Nora does not move, her fork still up. Nobody speaks anywhere in the room. On screen there is a father busy with his son's plate, and nothing else.

HARD CUT

SHOT 2 [4.5-12.0s] — Close on @Nora from the FAR SIDE of the family table, facing her, eye level, static, locked off, shallow depth of field. The camera stands on her father's side of the table but tight enough on her face that NEITHER @Sam NOR @Milo is ever in frame, and it is never a point-of-view shot. THE FRAME IS MIRRORED WITH RESPECT TO SHOT 1: the empty fourth chair and the women's table are now to the LEFT.
[4.5s] Frame contents: @Nora centred at x=50%, chest-up, filling 70% of frame height, SEATED, three-quarter to camera; her fork STOPPED in the air at chin height in her right hand, a piece of food on it, forgotten; her lips slightly parted, not chewing. Her eyes are held OFF SCREEN-LEFT, far, toward the women's table, fixed and open. At the frame's LEFT edge, soft and dark, the top rail and back of the EMPTY FOURTH CHAIR at her own table. Behind her, far out of focus, the depth of the room — two weak amber lantern pools, and low at the left of frame the green spill of the fish tank. NO WINDOW BEHIND HER: the street window is behind the camera, on the far side of the table.
[4.5-5.2s] Held. She breathes shallow. Nothing moves. The fork does not move.
[5.2-5.9s] HER EYES MOVE, ONCE, AND ONLY ONCE: they come back from the far left and DOWN — nearer, lower, ON THE SAME LEFT SIDE — and stop on the empty chair at her own table, a metre from her hand, soft at the frame's left edge. Nothing else in her body moves; her head does not turn.
[5.9-7.1s] Held on that. The eyes do not leave the chair. Her jaw is loose; she has forgotten she is holding anything. Something crosses her face and is put down again; her jaw sets a fraction. Her eyes never travel to the RIGHT of frame at any point, and they never come to the lens.
[7.1-8.2s] The fork comes down slowly, without her having eaten, and settles on the plate rim with one small click. Her hand stays on it a second.
[8.2-12.0s] Held to the end, no further movement: her face still, her eyes low and to the LEFT where the empty chair stands, her lips closed. She says nothing. She asks nobody anything.

SUBJECT LOCK, NORA The exact girl of the reference @Nora — fifteen, long dark brown wavy hair, unwashed, half-tied back; grey-green eyes with a slight downward outer tilt, heavy lids with grey shadowed hollows beneath, faint freckles across the nose, chapped bitten lips, pale olive skin drained of colour, thin adolescent build, shoulders rounded inward. Wardrobe: the oversized faded charcoal-grey hooded sweatshirt with worn cuffs, dark indigo jeans, NO parka. Resting expression: flat, elsewhere. In this generation her resting stillness is total — the whole performance lives in ONE small eye movement, to the LEFT of frame, and in the fork coming down; no other part of her body moves at any point. She does not cry, her lips do not tremble, her brow does not furrow into a question, she never speaks, and she never looks at the lens.

SUBJECT LOCK, SAM The exact man of the reference @Sam — the father, two years after: the same broad rectangular face, heavy jaw and pale grey-blue eyes as before, now about ten kilograms heavier, fuller in the face and around the waist; a month-old scruffy uneven salt-and-pepper beard, clearly neglected; light shadows under the eyes; the shoulders slumped, the gaze kept low, the corners of the mouth fallen — a tired, beaten quiet. Wardrobe: the faded charcoal waffle-knit thermal shirt under the olive-drab canvas work jacket with the torn left cuff, the thin worn steel wedding band. His hands: large, the skin cracked, the fingertips faintly stained dark blue-black — they read only as a workman's hands. HE NEVER SPEAKS, never smiles, NEVER LIFTS HIS EYES FROM THE PLATE, not once, and never looks at the lens. He exists only in shot 1: he is not in the second shot at all, not his face, not his shoulder, not his hands, not a blurred edge of him.

SUBJECT LOCK, MILO The exact child of the reference @Milo — eight, his father's pale grey-blue eyes with long lashes, his mother's small straight nose, full childhood cheeks, faint freckles, thick dark hair with the cowlick standing at the crown; small and slight. Wardrobe: the mustard-yellow ribbed long-sleeve top, the grey-blue corduroy dungarees with one strap twisted. He eats in silence, small mouthfuls, eyes mostly on his plate — a serious, watchful child. He exists only in shot 1. He never speaks and never looks at the lens.

SUBJECT LOCK, THE THREE WOMEN The exact women of the references @Mei, @Asha and @Fatiha, seated at their round table in the deep background of shot 1 only, small and soft and out of focus: @Mei in the plain white shirt and long dark green apron with her hair in the low bun and the lacquered wooden hairpin; @Asha upright with her short neat locs and her olive-and-indigo patterned open coat; @Fatiha rounded, in the ochre and dusty-blue headscarf and the long charcoal cardigan. Their conversation is over: they sit still, say nothing, and none of them looks toward the family table or toward the girl at any point. They are out of frame entirely in shot 2. None of them looks at the lens.

CROSS-FRAME RULES The same room in both shots — @Restaurant, same two tables in the same positions, same lanterns, same fish tank, same window, and nothing at the counter's far end. The state of both tables is the state locked in the PROP LAYOUT above and it does not change from the first frame to the last except for the fork coming down: three cups and the bare fourth place at the family table, the empty chair pushed in, and at the women's table nothing drunk, nothing eaten, nothing cleared. SHOT 1 COMES FIRST AND SHOT 2 SECOND, ALWAYS, IN THIS ORDER: the wide of the father is never placed after the close of the girl. THE CAMERA CROSSES TO THE OTHER SIDE OF THE TABLE BETWEEN THE TWO SHOTS, SO THE SCREEN DIRECTION REVERSES: what lies at the RIGHT of frame in shot 1 — the empty chair, the women's table — lies at the LEFT of frame in shot 2. In shot 2 the girl's eyes come from the FAR left of the room to the NEAR empty chair at the frame's left edge and stop there; they never travel to the right of frame, never across the table to her father, never into the lens, and there is no reverse angle on his face anywhere in this generation. Nobody speaks at any point, anywhere. Nobody looks at the lens. NO INVENTED ACTION: If a body part is not described as moving, it does not move. No gesture, step, head turn, prop interaction or expression change beyond the choreography written above; between described movements every body holds its last described position naturally (breathing, blinking, micro-sway only). CONTINUITY LOCK above and the POSITIVE CONSTRAINTS below apply in full.

CONTINUITY — WHAT MUST NOT DRIFT
Wardrobe, hair, dirt, damage and wear are exactly as the references define them and do not improve, clean themselves up or change between shots. Nobody is better groomed, better lit, better dressed or better rested than in the shot before. Props stay where the prop layout puts them. Weather, time of day and light level do not move inside a sequence. Nobody looks at the lens at any point.

LOCATION @Restaurant — the small old family-run Chinese restaurant of the act-one dinner, unchanged and older for it: six formica tables on tubular chrome legs dulled and pitted at the feet, each under a dark green cloth washed soft by years; wooden chairs, their varnish worn pale where hands pull them out, one with a re-glued back rail; the lacquered service counter, its lacquer finely crazed and rubbed to bare wood at the corner where trays slide; the green-lit fish tank, a faint limescale line at the waterline, a slow stream of bubbles, two dark carp barely moving; the beaded curtain to the kitchen, a few strands short; paper lanterns in amber and brass, their paper sun-faded, one panel neatly mended; the window onto the wet street, condensation creeping up the lower glass, the roller blind half down. Nothing stands at the counter's far end: no stool, no bowl, nothing on it. Only the two tables described in the layout are occupied; every other table is empty and cleared, chairs squared — a half-empty room on a slow night. No red anywhere. No readable menus, no lettering anywhere, no other diners, no staff.

LIGHT The amber paper lanterns burning low — weak tungsten bulbs inside the paper, each throwing a soft pool barely a metre wide that dies into shadow between the tables, real falloff, the paper itself glowing unevenly where it has thinned; the green fluorescent glow of the fish tank the strongest colour in the room, rippling faintly on the counter lacquer; the counter light dim; cold blue night through the window glass, the wet street holding its reflections; a desaturated grey-blue cast over the whole room, gently underexposed, deep blacks under the empty tables and in the corners. In shot 1 the window's cold blue sits behind the table at screen-left. In shot 2 the window is behind the camera and never seen: one weak lantern pool models the girl's face from above-front, leaving the eye sockets shadowed, and the room behind her dissolves into soft amber patches with the tank's green low at the left. No golden warmth, no cosy atmosphere.

DIALOGUE No lines. Nobody speaks anywhere in this generation, on screen or off — the conversation across the room is over and the family table has not said a word all evening.

LAST FRAME @Nora's face in close-up, still; her fork down on the plate rim, the mouthful never taken; her eyes low and to the LEFT, resting where the empty chair at her own table stands soft at the frame's left edge; the amber of the room and the green of the tank soft and out of focus behind her; her lips closed.



CHARACTER PERFORMANCE
Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through nothing else: no added expression, no widened eyes, no trembling lip, no theatrical breath. What is not written does not happen. Between the written events every body simply holds its last position, breathing, blinking and drifting a few millimetres, never frozen and never fidgeting.
@Sam, @Nora and @Milo are SEATED for the entire generation and never rise; the three women in the background are SEATED and never rise. Nobody sits in the empty fourth chair, nobody touches it. @Sam's hands hold the knife and fork over @Milo's plate for the whole generation and HE NEVER LIFTS HIS EYES, not once, not for a single frame.

PHYSICS — WEIGHT, INERTIA, CONTACT
Everything in frame has mass and obeys it. A body starts and stops with its own weight: it settles into a position rather than snapping into it, and a limb leads while the torso follows a beat later. Feet take the ground with real contact and real friction — on wet stone a step is slightly damped, never sliding, never skating. Clothing lags behind the body that moves it, keeps its own folds and swings back late; hair moves a beat behind the head and comes to rest slowly.
Objects have the mass their material implies. A wooden door swings on its hinges at the speed its own weight allows: it starts slowly, gathers a little, and is slowed at the end by its own friction and the resistance of the hinge — it never floats, never snaps open, never accelerates on its own, and it never moves before something moves it. Hands deform what they touch: fingers flatten slightly against a hard surface, fabric compresses under a grip, a held object presses back. Nothing passes through anything. Nothing changes speed without a cause visible in the frame.

WORLD — AFTER
A grey-blue world, gently underexposed, roughly two thirds of a stop below normal. Sparse motivated sources only — one bulb, one window, one sodium lamp — and deep quiet blacks between them. Colour is drained but not absent: what survives is amber from a flame, sodium orange from a street, sea-green from tile. Never a saturated hue. No red anywhere, flames included.

CINEMATOGRAPHY
Naturalistic available-light cinematography in the raw realist tradition. One motivated source at a time and no fill — a single bulb, a single window, a distant sodium lamp — with deep quiet blacks between them. Deliberately underexposed, roughly two thirds of a stop below normal, protecting the shadows and keeping real separation and texture inside them. Highlights restrained, never blown, holding texture in the filament and the wet stone. Low gentle contrast. Muted desaturated true-to-life colour: what survives is amber from a flame, sodium orange from a street, sea-green from tile — never a saturated hue, and never red.

FILM EMULATION — THE SAME STOCK FROM THE FIRST FRAME TO THE LAST
Shot on Kodak Vision3 500T 5219 tungsten colour negative, one stock, one lab, for the entire film, rated at box speed and printed flat. Cool naturalistic colour science; shadows falling slightly blue-green and holding real separation and texture inside them; skin tones understated, never warmed up, never rosy. Gentle contrast, soft highlight roll-off, highlights restrained and never blown, a faint halation ring blooming around every practical source. Moderate fine grain that grows in the underexposed areas and breathes with the exposure. Not glossy, not digital, not warm. Daylight scenes are the same stock corrected with an 85 filter, never a different look.

CAMERA REGISTER — LOCKED
The camera is placed, and it stays. Nobody is followed, nothing is reframed, and when a body leaves the frame the frame does not go after it. The only life left in the image is the residual human weight the CAMERA paragraph below describes — the same drift of a few millimetres, never more, and never a reframe. This stillness is not neutrality and must never read as a surveillance camera: it is what the film lost when it lost her, and it should feel like a breath being held.

CAMERA — OPERATED, NOT SIMULATED
One anamorphic lens set throughout: slight barrel distortion at the frame edges, oval out-of-focus highlights, mild edge softness, faint vignetting, vintage lens character. Focus is pulled by a human hand — it arrives a few frames late, occasionally overshoots by a hair and settles back, and breathes with the operator's pace. Every held frame keeps a residual human weight in it, a drift of a few millimetres: never a locked robotic stillness, never a shake. No digital sharpening, no edge halos, no noise-reduction smear, no beauty retouching, no plastic skin, no CGI gloss.

PHOTOGRAPHIC REALISM
True skin texture with visible pores and fine hairs, real fabric weave, seams and wrinkles that crease with movement, worn surfaces with real wear, natural asymmetry, natural motion blur in every movement. Deliberately underexposed where the scene calls for it, protecting the shadows and retaining detail inside them: no banding, no posterisation, no crushed flat blacks, no smeared low-light noise, no digital mush.

AUDIO
SFX only. No music. No background music of any kind, no score, no drone, no ambient pad. The room low and nearly empty: the fish-tank pump and the soft burst of its bubbles, the kitchen extractor's drone far off behind the beaded curtain, the drinks cooler cycling, wet tyres passing outside. In shot 1, close and dry, the slow scrape of a knife on china, over and over, unbroken. In shot 2 the same knife continues faint and off frame under everything, then the small click of the fork settling on the plate rim, and after it nothing. Not one voice in the room. No music.

POSITIVE CONSTRAINTS — CHECK EVERY FRAME AGAINST THESE
Every named reference above is matched 100%: same face, same build, same wardrobe, same wear. Nobody is better groomed, better lit, better dressed or better rested than the shot before; wardrobe, hair, dirt, damage and wear do not improve or clean themselves up. Props stay exactly where the prop layout puts them. The light level, the weather and the time of day do not move inside this generation.
The choreography written in the FRAME MAP is the whole performance: no gesture, step, head turn, prop interaction or expression beyond it. Between described movements every body holds its last position naturally, breathing and blinking, never frozen and never fidgeting.
Nobody looks at the lens at any point. Nobody speaks except where DIALOGUE says so.
Every stroke of handwriting anywhere in frame is real handwriting laid out in straight horizontal lines — word-shaped clusters separated by spaces, gathered into sentences and paragraphs — in an invented cursive alphabet whose characters recur again and again the way a real alphabet's do. Unmistakably a script, but no script that exists on earth, and not one word readable in any language: it reads as writing from across the room and as nothing at all up close. Never random scribble, never a scrawl, never abstract mark-making, never decorative squiggles. No signage, no label, no digit, no subtitle, no caption is readable anywhere.
One continuous take at real-time speed for the exact duration requested, containing ONLY the framings and the hard cuts that FORMAT MODE declares above, at the moments the FRAME MAP gives and nowhere else. No dissolve, no fade, no montage, no extra cut. No slow motion, no speed ramp.

AVOID
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, readable menus, readable signage, readable lettering, subjects looking at camera, slow motion, morphing objects, extra people in frame, other diners, waiters, extra gestures, improvised actions, wandering hands, repositioned props, appearing or disappearing objects, camera movement, dolly, pan, zoom, push in, focus pull, handheld shake, the girl looking toward the right of the frame, the girl's eyes travelling right, the girl looking toward the boy's side of the table, the girl looking across the table at her father, the girl looking at any person, the girl frowning, the girl's face carrying a question, a window behind the girl in the close shot, cold blue night behind the girl in the close shot, the father lifting his eyes, the father looking at his daughter, the father looking at his son, the father speaking, a close-up of the father's face, a reverse angle on the father, the father in the close shot, the boy in the close shot, the women looking toward the family table, the girl speaking, the girl crying, tears, trembling lips, the girl looking at camera, the girl eating, the fork reaching her mouth, a fourth cup at the family table, a place setting at the empty place, anyone sitting in the empty chair, anyone entering frame, anyone standing up, a stool at the counter, a bowl on a stool, anything standing at the counter's far end, rushed movements, theatrical acting, overacting, posed smiles, sitcom lighting, warm saturated grade, golden light, the room brightening, any red anywhere, red lanterns, red tablecloths, red menus, red packaging, generated music, uncanny smoothness, plastic skin, beauty filter, CGI look, video-game lighting, frozen characters, statue-like stillness, mannequin pose, freeze-frame stillness.
```








*⚠ **POINT DE COUPE — 6 s au montage sur 12 s de rushes.** Garder ① **2,2 s** du shot 1, de `[1.5s]` à `[3.7s]`
— le père qui coupe, rien d'autre ; ② **3,8 s** du shot 2, de `[4.65s]` à `[8.45s]` — l'attente, le trajet du
regard, la fourchette qui redescend. **Le trajet du regard et la fourchette ne se taillent pas : c'est le plan.***

*⚠ **RÈGLE ZÉRO — CONTRÔLE DE RACCORD, à faire sur le rush avant de valider.** Le regard part de la table des
femmes et **s'arrête sur la chaise vide**, jamais sur son père. **INTERDIT dans toute la séquence : couper des
yeux de Nora au visage de Sam.** Le plan large de Sam vient **AVANT**, jamais après — ce raccord-là, à lui seul,
fabriquerait un soupçon sans qu'un mot soit dit. Un frame où elle fronce les sourcils est à jeter.*

*⚠ **DIRECTION D'ÉCRAN.** Le plan 2 est un **contrechamp** : tout ce qui est à la DROITE de Nora se retrouve
**à GAUCHE du cadre**. Le regard doit partir vers la **GAUCHE** ; un frame où il part vers la droite tombe sur
Milo et le trajet du script ne se joue pas.*

---


### VIDÉO 5D-bis — SECOURS du shot 2 de 5D *(6 s · à ne lancer QUE si le serré manque de longueur de focale, ou si le regard part vers la droite · Elements : @Nora + @Restaurant · start frame : aucune — cadre décrit au prompt · Lens Anamorphic **85 mm f/2**)*

```
SCENE CONTEXT
A teenage girl alone in the frame at a restaurant table, her fork stopped in the air, the mouthful never taken. Her eyes come back from something far to her left and settle on something near, low and still to her left — a metre from her hand — and stop there. She puts the fork down without having eaten. She says nothing and she asks nobody anything. ONE single continuous shot, no cut, nobody else in frame at any point. Every second is choreographed below; nothing beyond it may be invented. 6 seconds, one continuous framing, no cut.

CONTINUITY REFERENCE — NO VIDEO IS ATTACHED
No previous clip is attached to this generation. This is the first shot of its chain: it sets the light, the grain and the skin rendering that every following shot will be matched to. Build every frame new from the references below, at full quality.

ACTIVE REFERENCES
@Nora: Nora, fifteen, long dark brown unwashed hair, grey-green eyes, pale olive skin gone colourless, bitten lips, heavy lids over grey hollows, thin build. Running on empty: grief has made her polite and absent — she answers, she says thank you, and none of it reaches her face. She goes very still before anything shows. NOTHING RED ON HER. 100% matches the reference.
@Restaurant: Mei's restaurant — amber lanterns, green tablecloths, a green fish tank. No red anywhere, no legible signage. 100% matches the reference.

TEMPERAMENT, NORA A fifteen-year-old running on empty. Grief has made her polite and absent: she answers, she carries the dish back, she says thank you, and none of it reaches her face. Her body is tired before the day starts. She does not cry in front of people — the swollen eyelids come from somewhere else, earlier. When something does move her, she goes very still first, and only then does it show.

LOCATION MAP
Framing 1 [0.0-6.0s] — camera: Close on @Nora, facing her, eye level, static, locked off, shallow depth of field, 85 mm.
Every distance, height and frame position given above is literal and is held exactly; nothing drifts toward a more flattering angle.

FIRST FRAME AND SPATIAL BLOCKING The generation opens on this exact frame: Close on @Nora, facing her, eye level, static, locked off, shallow depth of field, 85 mm. Frame contents: @Nora centred at x=50%, chest-up, filling 72% of frame height, SEATED, three-quarter to camera; her fork STOPPED in the air at chin height in her right hand, a piece of food on it, forgotten; her lips slightly parted, not chewing. Her eyes are held OFF SCREEN-LEFT, far, fixed and open. At the frame's LEFT edge, soft and dark, the top rail and back of the EMPTY FOURTH CHAIR. Behind her, far out of focus, the depth of the room — two weak amber lantern pools, and low at the left of frame a green spill. This is the frame the first video frame must already be, before anything moves: nothing is settling into place, nothing fades up, nothing is mid-transition.

FORMAT MODE
One single continuous uncut take, 6 seconds long, at real-time speed. No cut, no montage, no dissolve, no speed ramp, no slow motion.

OPTICS
Anamorphic 85 mm f/2 equivalent. Depth of field wide open at that stop: the plane described in the FRAME MAP is tack sharp and everything behind it falls off progressively. Focus holds on that plane and breathes naturally with the camera's movement — no deliberate rack focus unless the FRAME MAP calls for one.

CONTINUITY LOCK Every prop named in the layout appears in EVERY frame where its surface is visible, in the same position and state — nothing appears, disappears, multiplies or moves unless the choreography says so. Her posture is SEATED and never changes. She holds exactly the fork the choreography puts in her hand — no other utensil or object may materialise.

GEOMETRY The camera stands on the far side of the family table, facing her, at eye level, tight enough that no other person is ever in frame and it is never a point-of-view shot. EVERYTHING THAT MATTERS IS TO THE LEFT OF FRAME: the women's round table far off screen-left, and nearer, at the frame's LEFT edge, the top rail and back of the EMPTY FOURTH CHAIR at her own table. @Milo's side of the table is to the RIGHT of frame and out of shot. NO WINDOW BEHIND HER: the street window is behind the camera. Nothing stands at the counter's far end anywhere in this sequence.

PROP LAYOUT — FIXED @Nora's fork is IN HER RIGHT HAND, STOPPED in the air at chin height, a piece of food speared on it — it never travels to her mouth, and it comes down onto her plate rim once, at [2.6-3.7s], and stays there. Low in the frame, soft: the near edge of the dark green cloth, the rim of her untouched plate of rice and greens, and the rim of one small white porcelain cup with its glaze finely crazed. At the frame's LEFT edge, soft and dark, the top rail and back of the empty fourth chair, and before it bare green cloth — no plate, no cup, no cutlery. Nothing else is in frame.

FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND

SHOT [0.0-6.0s] — Close on @Nora, facing her, eye level, static, locked off, shallow depth of field, 85 mm.
[0.0s] Frame contents: @Nora centred at x=50%, chest-up, filling 72% of frame height, SEATED, three-quarter to camera; her fork STOPPED in the air at chin height in her right hand, a piece of food on it, forgotten; her lips slightly parted, not chewing. Her eyes are held OFF SCREEN-LEFT, far, fixed and open. At the frame's LEFT edge, soft and dark, the top rail and back of the EMPTY FOURTH CHAIR. Behind her, far out of focus, the depth of the room — two weak amber lantern pools, and low at the left of frame a green spill.
[0.0-0.7s] Held. She breathes shallow. Nothing moves. The fork does not move.
[0.7-1.4s] HER EYES MOVE, ONCE, AND ONLY ONCE: they come back from the far left and DOWN — nearer, lower, ON THE SAME LEFT SIDE — and stop on the empty chair at the frame's left edge. Nothing else in her body moves; her head does not turn.
[1.4-2.6s] Held on that. The eyes do not leave it. Her jaw is loose; she has forgotten she is holding anything. Something crosses her face and is put down again; her jaw sets a fraction. Her eyes never travel to the RIGHT of frame, and they never come to the lens.
[2.6-3.7s] The fork comes down slowly, without her having eaten, and settles on the plate rim with one small click. Her hand stays on it a second.
[3.7-6.0s] Held to the end, no further movement: her face still, her eyes low and to the LEFT, her lips closed. She says nothing. She asks nobody anything.

SUBJECT LOCK, NORA The exact girl of the reference @Nora — fifteen, long dark brown wavy hair, unwashed, half-tied back; grey-green eyes with a slight downward outer tilt, heavy lids with grey shadowed hollows beneath, faint freckles across the nose, chapped bitten lips, pale olive skin drained of colour, thin adolescent build, shoulders rounded inward. Wardrobe: the oversized faded charcoal-grey hooded sweatshirt with worn cuffs, dark indigo jeans, NO parka. Resting expression: flat, elsewhere. The whole performance lives in ONE small eye movement, to the LEFT of frame, and in the fork coming down; no other part of her body moves at any point. She does not cry, her lips do not tremble, her brow does not furrow into a question, she never speaks, and she never looks at the lens.

CROSS-FRAME RULES ONE single continuous shot with no cut inside it and no camera movement whatsoever. NOBODY ELSE EXISTS ON SCREEN at any point: no father, no boy, no waitress, no woman, no silhouette, no blurred edge of another body, no reverse angle on anyone. Her eyes go to the LEFT of frame and nowhere else; they never travel right, never across the table, never to the lens. The empty chair stays soft at the frame's left edge in every frame. Nothing red exists anywhere. Nobody looks at the lens. NO INVENTED ACTION: If a body part is not described as moving, it does not move. No gesture, step, head turn, prop interaction or expression change beyond the choreography written above; between described movements every body holds its last described position naturally (breathing, blinking, micro-sway only). CONTINUITY LOCK above and the POSITIVE CONSTRAINTS below apply in full.

CONTINUITY — WHAT MUST NOT DRIFT
Wardrobe, hair, dirt, damage and wear are exactly as the references define them and do not improve, clean themselves up or change between shots. Nobody is better groomed, better lit, better dressed or better rested than in the shot before. Props stay where the prop layout puts them. Weather, time of day and light level do not move inside a sequence. Nobody looks at the lens at any point.

LOCATION @Restaurant — the small old family-run Chinese restaurant of the act-one dinner, seen only as the soft depth behind a face: formica tables under dark green cloths washed soft by years, wooden chairs with their varnish worn pale, the lacquered service counter finely crazed, the green-lit fish tank throwing a low green spill at the left of frame, the beaded curtain to the kitchen, paper lanterns in amber and brass with their paper sun-faded — all of it far out of focus. Nothing stands at the counter's far end: no stool, no bowl, nothing on it. No red anywhere. No readable menus, no lettering anywhere, no logos, no other diners in focus or out of it.

LIGHT One weak amber lantern pool from above and slightly in front, modelling her face and leaving the eye sockets shadowed; behind her the room dissolves into two soft amber patches with the fish tank's green low at the left; a desaturated grey-blue cast over everything, gently underexposed, deep blacks at the frame edges. No window behind her, no cold blue night behind her, no golden warmth, no cosy atmosphere, and the exposure never changes.

DIALOGUE None. Nobody speaks in this generation, on screen or off.

LAST FRAME @Nora's face in close-up, still; her fork down on the plate rim, the mouthful never taken; her eyes low and to the LEFT, resting where the empty chair stands soft at the frame's left edge; the amber of the room and a low green spill soft and out of focus behind her; her lips closed.



CHARACTER PERFORMANCE
Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through nothing else: no added expression, no widened eyes, no trembling lip, no theatrical breath. What is not written does not happen. Between the written events every body simply holds its last position, breathing, blinking and drifting a few millimetres, never frozen and never fidgeting.
@Nora is SEATED for the entire generation and never rises, never turns her body, never leans. Nobody else exists in this generation at any point.

PHYSICS — WEIGHT, INERTIA, CONTACT
Everything in frame has mass and obeys it. A body starts and stops with its own weight: it settles into a position rather than snapping into it, and a limb leads while the torso follows a beat later. Feet take the ground with real contact and real friction — on wet stone a step is slightly damped, never sliding, never skating. Clothing lags behind the body that moves it, keeps its own folds and swings back late; hair moves a beat behind the head and comes to rest slowly.
Objects have the mass their material implies. A wooden door swings on its hinges at the speed its own weight allows: it starts slowly, gathers a little, and is slowed at the end by its own friction and the resistance of the hinge — it never floats, never snaps open, never accelerates on its own, and it never moves before something moves it. Hands deform what they touch: fingers flatten slightly against a hard surface, fabric compresses under a grip, a held object presses back. Nothing passes through anything. Nothing changes speed without a cause visible in the frame.

WORLD — AFTER
A grey-blue world, gently underexposed, roughly two thirds of a stop below normal. Sparse motivated sources only — one bulb, one window, one sodium lamp — and deep quiet blacks between them. Colour is drained but not absent: what survives is amber from a flame, sodium orange from a street, sea-green from tile. Never a saturated hue. No red anywhere, flames included.

CINEMATOGRAPHY
Naturalistic available-light cinematography in the raw realist tradition. One motivated source at a time and no fill — a single bulb, a single window, a distant sodium lamp — with deep quiet blacks between them. Deliberately underexposed, roughly two thirds of a stop below normal, protecting the shadows and keeping real separation and texture inside them. Highlights restrained, never blown, holding texture in the filament and the wet stone. Low gentle contrast. Muted desaturated true-to-life colour: what survives is amber from a flame, sodium orange from a street, sea-green from tile — never a saturated hue, and never red.

FILM EMULATION — THE SAME STOCK FROM THE FIRST FRAME TO THE LAST
Shot on Kodak Vision3 500T 5219 tungsten colour negative, one stock, one lab, for the entire film, rated at box speed and printed flat. Cool naturalistic colour science; shadows falling slightly blue-green and holding real separation and texture inside them; skin tones understated, never warmed up, never rosy. Gentle contrast, soft highlight roll-off, highlights restrained and never blown, a faint halation ring blooming around every practical source. Moderate fine grain that grows in the underexposed areas and breathes with the exposure. Not glossy, not digital, not warm. Daylight scenes are the same stock corrected with an 85 filter, never a different look.

CAMERA REGISTER — LOCKED
The camera is placed, and it stays. Nobody is followed, nothing is reframed, and when a body leaves the frame the frame does not go after it. The only life left in the image is the residual human weight the CAMERA paragraph below describes — the same drift of a few millimetres, never more, and never a reframe. This stillness is not neutrality and must never read as a surveillance camera: it is what the film lost when it lost her, and it should feel like a breath being held.

CAMERA — OPERATED, NOT SIMULATED
One anamorphic lens set throughout: slight barrel distortion at the frame edges, oval out-of-focus highlights, mild edge softness, faint vignetting, vintage lens character. Focus is pulled by a human hand — it arrives a few frames late, occasionally overshoots by a hair and settles back, and breathes with the operator's pace. Every held frame keeps a residual human weight in it, a drift of a few millimetres: never a locked robotic stillness, never a shake. No digital sharpening, no edge halos, no noise-reduction smear, no beauty retouching, no plastic skin, no CGI gloss.

PHOTOGRAPHIC REALISM
True skin texture with visible pores and fine hairs, real fabric weave, seams and wrinkles that crease with movement, worn surfaces with real wear, natural asymmetry, natural motion blur in every movement. Deliberately underexposed where the scene calls for it, protecting the shadows and retaining detail inside them: no banding, no posterisation, no crushed flat blacks, no smeared low-light noise, no digital mush.

AUDIO
SFX only. No music. No background music of any kind, no score, no drone, no ambient pad. The room low and nearly empty: the fish-tank pump and the soft burst of its bubbles, the kitchen extractor's drone far off behind the beaded curtain, the drinks cooler cycling, wet tyres passing outside. Under everything, faint and off frame, the slow scrape of a knife on china, unbroken. Then the small click of the fork settling on the plate rim, and after it nothing. Not one voice in the room. No music.

POSITIVE CONSTRAINTS — CHECK EVERY FRAME AGAINST THESE
Every named reference above is matched 100%: same face, same build, same wardrobe, same wear. Nobody is better groomed, better lit, better dressed or better rested than the shot before; wardrobe, hair, dirt, damage and wear do not improve or clean themselves up. Props stay exactly where the prop layout puts them. The light level, the weather and the time of day do not move inside this generation.
The choreography written in the FRAME MAP is the whole performance: no gesture, step, head turn, prop interaction or expression beyond it. Between described movements every body holds its last position naturally, breathing and blinking, never frozen and never fidgeting.
Nobody looks at the lens at any point. Nobody speaks except where DIALOGUE says so.
Every stroke of handwriting anywhere in frame is real handwriting laid out in straight horizontal lines — word-shaped clusters separated by spaces, gathered into sentences and paragraphs — in an invented cursive alphabet whose characters recur again and again the way a real alphabet's do. Unmistakably a script, but no script that exists on earth, and not one word readable in any language: it reads as writing from across the room and as nothing at all up close. Never random scribble, never a scrawl, never abstract mark-making, never decorative squiggles. No signage, no label, no digit, no subtitle, no caption is readable anywhere.
One continuous uncut take at real-time speed, for the exact duration requested. No slow motion, no speed ramp, no added cut.

AVOID
visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, readable menus, readable signage, readable lettering, subjects looking at camera, slow motion, morphing objects, extra people in frame, another person in frame, the father, the boy, a waitress, other diners, a reverse angle on anyone, extra gestures, improvised actions, wandering hands, repositioned props, appearing or disappearing objects, camera movement, dolly, pan, zoom, push in, focus pull, handheld shake, the girl looking toward the right of the frame, the girl's eyes travelling right, the girl looking at any person, the girl frowning, the girl's face carrying a question, a window behind the girl, cold blue night behind the girl, the girl speaking, the girl crying, tears, trembling lips, the girl looking at camera, the girl eating, the fork reaching her mouth, a place setting at the empty place, anyone sitting in the empty chair, a stool at the counter, a bowl on a stool, rushed movements, theatrical acting, overacting, posed smiles, sitcom lighting, warm saturated grade, golden light, the room brightening, any red anywhere, red lanterns, red tablecloths, red menus, red packaging, generated music, uncanny smoothness, plastic skin, beauty filter, CGI look, video-game lighting, frozen characters, statue-like stillness, mannequin pose, freeze-frame stillness.
```








*⚠ **Point de coupe de 5D-bis** : garder `[0.15s]` → `[3.95s]` — 3,8 s, exactement la fenêtre du shot 2 qu'il
remplace. Les 2,2 s de plan large du shot 1 de 5D restent valables et se recollent devant sans retouche.*

---

## RÉCAPITULATIF DE GÉNÉRATION

| Bloc | Plan | Lieu / start frame | Objectif | Rushes | Montage |
|---|---|---|---|---|---|
| **5A** | 5.1 — les quatre tasses | @Restaurant · LIEU-07 IMAGE 2 | le payoff de 2.3, et le père transformé | 12 s | 5 s |
| **5B-1** | 5.2 (1/2) | @Restaurant · LIEU-07 IMAGE 4 | elles se parlent, vite, en se coupant | 10 s | 7,2 s |
| **5B-2** | 5.2 (2/2) | **dernier frame de 5B-1** | le silence, puis « More tea? » | 8 s | 5,8 s |
| **5C** | insert dans 5.2 | *aucune — décrit au prompt* | la main qui s'arrête, **sans visage** | 6 s | 0,7 s* |
| **5D** | 5.3 — le trajet du regard | @Restaurant · LIEU-07 IMAGE 2 | elle décide, et ne demande rien | 12 s | 6 s |
| *(5D-bis)* | *secours shot 2 de 5.3* | *cadre décrit, 85 mm* | *le serré seul, regard à gauche* | *6 s* | *remplace ② de 5D* |

\* **l'insert 5C ne s'ajoute pas** : il recouvre 0,7 s de 5B-2. **Total à l'écran : 5 + 13 + 6 = 24 s**, la durée
exacte du script. **5 générations obligatoires (dont l'insert) · 48 s de rushes → 24 s au montage.**

**Ordre de génération conseillé** : **5B-1 d'abord** (l'axe unique, les trois visages, et le débit à trois voix —
le seul vrai risque du document), puis **5B-2** chaîné sur son dernier frame, puis **5C**, puis **5A**, puis **5D**.

**[POST] de la séquence : AUCUN.** Aucun texte, aucun artwork, aucune retouche. C'est la seule séquence du
film qui n'a rien en post.

---

## ⚠ CE QUI PEUT RATER

**5B-1 et 5B-2 — le débit à trois voix qui se coupent la parole *(le risque n°1 du document)*.** Trois
locuteurs nommés dans un plan fixe, avec des chevauchements de 0,15 s : le modèle a tendance à **séquencer**
(chacune attend son tour, on perd le naturel), à **avaler une réplique**, ou à **désynchroniser les lèvres** sur
les chevauchements. **Plan B, sans regénérer l'image** : garder le rush séquencé et **recréer les chevauchements
au mixage** — les lèvres bougent déjà, il suffit d'avancer de 0,15 s la piste de celle qui coupe. Le procédé est
déjà éprouvé sur la séquence. **Plan C, si une réplique manque à l'image** : la redistribuer à la voix off d'une
femme hors cadre est **interdit** — elles sont trois et elles sont toutes dans le plan. Régénérer le bloc.

**5B — la prononciation des trois noms.** *Al-Maktoub · Msimulizi · Mòyīrén* peuvent sortir déformés ou
anglicisés. Ils ne portent aucune information narrative : **ce qui compte est qu'ils soient trois et différents.**
Si l'un est massacré, garder la prise et **le corriger au mixage sur la seule syllabe fautive** — ne pas
régénérer 10 s pour un mot. ⚠ **Aucun des trois n'est jamais traduit** : leur traduction serait le mot interdit
(règle A).

**5B — MEI QUI REGARDE NORA.** Le danger n'est pas technique. Un seul frame où Mei jette un œil vers la table
famille, et la scène devient un message adressé — le contraire exact de ce que le script veut. **Contrôler image
par image sur les deux blocs.** Idem pour Fatiha et Asha : **aucune des trois ne regarde vers la gauche du cadre.**
Si le rush contient ce frame, **la prise est à jeter.**

**5B-2 — le battement de silence.** Le modèle voudra le remplir (un rire, un soupir, un regard échangé, une
respiration appuyée) ou le raccourcir. **Il doit durer une demi-seconde exactement et ne rien contenir** : c'est
lui qui fait que « More tea? » atterrit sur une table déjà passée à autre chose. S'il est joué comme une pause
dramatique — regards qui se croisent, gravité — **régénérer** : les négatifs *a dramatic pause, a meaningful
glance exchanged* sont là pour ça.

**5B-2 — « More tea? » sur-joué.** La réplique doit être **plate, ordinaire, déjà ailleurs.** Si elle est jouée
avec chaleur ou avec un regard vers Nora, tout le décalage tombe et la scène ne bascule plus.

**5B-2 — le chaînage.** Si les visages, les niveaux de thé ou la position de la caméra dérivent entre 5B-1 et
5B-2, la coupe se voit et 5.2 cesse d'être un seul plan. **Contrôle obligatoire sur trois points** : hauteur de
@Mei dans le cadre (50 %), position de sa main autour de la tasse, et niveau des trois verres d'eau. En cas de
dérive : repartir de **LIEU-07 IMAGE 4** et recopier le bloc GEOMETRY de 5B-1 en tête du prompt fautif.

**5C — un visage dans le cadre.** C'est la seule façon de rater ce plan, et elle est fatale : un menton, une
épaule, ou **un reflet de visage dans la tasse blanche ou sur la théière métallique** au bord haut du cadre.
Les négatifs les nomment tous les trois. **Contrôler image par image ; au moindre reflet, régénérer** — ou, en
dernier recours, resserrer le cadrage en post jusqu'à ne garder que les mains, quitte à perdre en définition.

**5C — l'arrêt qui ne se lit pas.** À 0,7 s de montage, un arrêt mou est invisible. Il doit être **net, à
l'image près, et suivi d'une reprise au rythme identique.** Si le rush freine progressivement ou repart plus
vite, **la prise est à refaire** : c'est tout le plan.

**5C — l'image morte.** On demande une immobilité d'une demi-seconde : le modèle peut rendre un vrai
freeze-frame. Le grain, la vapeur et le souffle dans la manche doivent continuer de vivre pendant l'arrêt. Les
négatifs anti-figé sont là pour ça — **si l'image est parfaitement morte, la prise est à refaire.**

**5D — RÈGLE ZÉRO.** Le vrai danger de la séquence. Si le regard de Nora part vers la DROITE, il tombe sur Milo
et le trajet ne se joue pas ; s'il traverse la table vers son père, ou si un seul frame lui met un doute sur le
visage, **le film entier tombe.** Contrôler image par image la fenêtre `[4.65-8.45s]`. **Plan B** : la
génération **5D-bis**, écrite en entier ci-dessus.

**5D — l'ordre des deux plans.** Le plan large de Sam vient **AVANT** le serré, jamais après. Inversé, il devient
un contrechamp du regard de sa fille — et fabrique le soupçon que la règle zéro interdit.

**5A — Mei qui sourit.** En 2.3 elle souriait en posant quatre assiettes ; ici le même geste ne doit plus porter
aucun sourire, et **elle ne croise le regard de personne.** Un sourire dans ce plan efface deux ans.

**5A — la quatrième tasse laissée sur la table.** Elle repart **toujours** sur le plateau. Si le rush la laisse
en place, la prise est inutilisable : la table doit finir à trois.

**Toute la séquence — la lumière qui se réchauffe.** Le petit rire de Mei, la conversation vivante : le modèle
voudra éclairer. **La chaleur est dans les voix, jamais dans l'image.** Si une vignette te paraît « jolie »,
c'est raté — le monde est gris de la séquence 4 à la séquence 9 (règle COULEUR opposable).

**Toute la séquence — le rouge.** Lanternes, emballages, bol : c'est un restaurant, le rouge s'invite tout seul,
et il ruinerait la règle B à cinq séquences de la maison rouge, qui doit être le **premier rouge plein cadre du
film.** Vérifier chaque passe image par image ; au moindre doute, désaturer en post plutôt que garder un rush
douteux.

---

## ⚠ DÉPENDANCES À CORRIGER AILLEURS *(à faire avant de générer les séquences 2 et 10, sinon la continuité est fausse)*

1. **`@CounterBowl` ne doit pas être créé.** L'ancienne version de ce document demandait de sauvegarder le
   dernier frame d'un insert de comptoir comme Élément `@CounterBowl`, et de le réutiliser dans tous les blocs
   de la séquence 5 **et dans le montage muet de la séquence 10**. Cet insert est supprimé avec le récit de Mei :
   **il n'y a plus ni tabouret ni bol nulle part dans le film.** Vérifier `VIDEO-SEQ-10.md` et `GEN-SEQ-05.md` /
   `GEN-SEQ-10.md` — toute ligne qui appelle `@CounterBowl`, « the stool », « the plain white bowl » ou
   « chopsticks laid flat across the rim » est **périmée**.
2. **`LIEU-07-Restaurant.md`** — la note « **IMAGE 4 → 5D plan 1** » et « zone nette du cadre profond (5B plan 1,
   5D plan 2) » suit l'ancienne nomenclature à huit blocs. **Nouvelle correspondance : IMAGE 2 → 5A et 5D ·
   IMAGE 4 → 5B-1 · 5B-2 = dernier frame de 5B-1 · 5C = aucune start frame.** La ligne « le plateau et les
   quatre tasses de Mei (5A) » reste juste ; la ligne « **le bol du comptoir** » est à supprimer du set dressing.
3. **`VIDEO-SEQ-02.md`** — la note « ⚠ CADRE RÉFÉRENT ÉMOTIONNEL → paie en 5.1 » du plan 2.3 reste valable **et
   devient le seul lien entre les deux restaurants** : les quatre assiettes posées d'office, en souriant, et les
   quatre tasses posées d'office, sans un sourire, avec une reprise. Garder les deux fichiers côte à côte au
   montage. ⚠ Le **numéro du dragon** ayant été supprimé de la séquence 2, vérifier que `VIDEO-SEQ-02.md` ne
   fasse plus aucun renvoi à « la loi du dragon » depuis la séquence 5 : **la loi est dite ici, par Fatiha et
   Mei** (« He asks for something first. Always something small. » / « Never a big one. »), et nulle part ailleurs.
4. **`VIDEO-SEQ-06.md`** — le script retire la loi du forum (6.1) parce que les trois femmes viennent de la
   dire ici. Vérifier que le bloc du forum ne porte plus que **le rituel**, et plus les trois pavés de texte.
5. **`VIDEO-SEQ-10.md`, plan 10.9e** — « Le restaurant vide, l'après-midi. Il parle aux trois femmes. Elles
   hochent la tête. » Ce plan **gagne à la refonte** : Sam pouvait faire répéter six répliques courtes à trois
   femmes sur une serviette ; il ne pouvait pas leur faire jouer trois récits de vie. **Le texte qu'il leur fait
   répéter est désormais exactement celui de 5B-1 et 5B-2** — le vérifier si le bloc de la séquence 10 montre un
   papier dans sa main (texture uniquement, règle G : rien de lisible).
