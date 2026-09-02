# SÉQUENCE 6 — LE FORUM ET LE CRI · VIDÉOS À COPIER-COLLER *(monde gris · 3 générations obligatoires + 2 secours · 32 s de rushes → 21 s au montage)*

> **UN BLOC = TOUT.** Tu copies **un seul bloc**, tu le colles dans Higgsfield, tu génères.
> **Rien à ouvrir à côté, rien à ajouter.** Les cartes de `00-CARTES-A-COLLER.md` sont
> désormais *dans* chaque bloc : chaîne, monde, tempérament des personnages au cadre,
> pellicule, registre caméra, anti-dérive, contraintes.
>
> Registre caméra de cette séquence : **LOCKED**.
> Modèle **Seedance 2.5** · 21:9 · 1080p · bitrate **high** · sound off.
> Source : `VIDEO-SEQ-06.md`.
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


## VIDÉO 6A — plan 6.1 « Le forum » *(12 s de rushes → 7 s au montage · Elements : @Nora + @NoraBedroom · start frame : LIEU-08 IMAGE 3)*
**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 12 s |
| **Éléments** | @Nora + @NoraBedroom |
| **`start_image`** | LIEU-08 IMAGE 3 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> ⛔ **NE COLLE PAS CE TABLEAU.** Il est pour toi, pas pour le modèle : c'est ce que tu règles
> dans l'interface avant de coller. **Tu ne copies QUE le texte entre les triples backticks
> ci-dessous**, et rien d'autre — pas le titre, pas ce tableau, pas cette ligne.


```
SCENE CONTEXT
Alone at night in a dark bedroom, a girl reads a page on her laptop, scrolls once, stops on something, and lifts her eyes off the screen toward the black window. Three shots, two hard cuts. Nothing on the screen is ever a word: the page exists as light and blocks only. Every second is choreographed below; nothing beyond it may be invented. 12 seconds, in 3 framings joined by 2 hard cuts.

CONTINUITY REFERENCE — SAME FILM, DIFFERENT PLACE
THE VIDEO ATTACHED TO THIS GENERATION is an earlier shot from the same film (5D), in a different place. Use it ONLY to match the physical rendering — the film stock, the grain structure, the way skin and fabric resolve, the focus behaviour, the highlight roll-off. Do NOT take its light, its palette, its exposure level or its composition: this shot's light comes from its own LOCATION and LIGHT paragraphs below, and its framing from its own FRAME MAP. Everything else is built new, at full quality.

HANDOFF — THE EXACT STATE THIS SHOT INHERITS FROM THE ATTACHED VIDEO
These are NOT new positions to invent. This is the frame the previous shot (5D) ends on, repeated here to the number, and the first frame of this generation must reproduce it exactly before anything moves.
WHAT IS IN THE FRAME AT THE LAST INSTANT: @Nora's face in close-up, still; her fork down on the plate rim, the mouthful never taken; her eyes low and to the LEFT, resting where the empty chair at her own table stands soft at the frame's left edge; the amber of the room and the green of the tank soft and out of focus behind her; her lips closed.
WHERE THIS SHOT LEAVES EACH BODY, to the number — these are the positions the next shot inherits, whether or not the body is still inside this last frame: @Sam: SEATED, x=56%, filling 42% of frame height. @Milo: SEATED, x=38%, filling 26% of frame height. @Nora: SEATED, x=50%, filling 70% of frame height.
Nothing in this list may be re-placed, re-lit or improved. Whatever the FRAME MAP below asks for happens AFTER this state, never instead of it.

ACTIVE REFERENCES
@Nora: Nora, fifteen, long dark brown unwashed hair, grey-green eyes, pale olive skin gone colourless, bitten lips, heavy lids over grey hollows, thin build. Running on empty: grief has made her polite and absent — she answers, she says thank you, and none of it reaches her face. She goes very still before anything shows. NOTHING RED ON HER. 100% matches the reference.
@NoraBedroom: Nora's bedroom and the landing outside it, grey and underexposed, one narrow sodium band under the door. 100% matches the reference.

TEMPERAMENT, NORA A fifteen-year-old running on empty. Grief has made her polite and absent: she answers, she carries the dish back, she says thank you, and none of it reaches her face. Her body is tired before the day starts. She does not cry in front of people — the swollen eyelids come from somewhere else, earlier. When something does move her, she goes very still first, and only then does it show.

LOCATION MAP
Framing 1 [0.0-4.0s] — camera: Medium from three-quarter behind her left shoulder, seated eye level, camera about 120 cm high and one metre behind the chair, static, locked off — exactly the axis of the reference angle, the desk filling the lower right half of frame, the window a black rectangle screen-right.
Framing 2 [4.0-9.0s] — camera: THE PLATE. Over her right shoulder, straight onto the laptop screen, camera about 130 cm high and 70 cm behind her, the screen square to the lens and IN FOCUS, static, locked off, no drift of any kind. The screen fills the middle of frame from x=22% to x=78% and 46% of frame height; the dark mass of her right shoulder and the back of her head cuts the lower left corner as an out-of-focus silhouette; the dark room around the screen is near-black.
Framing 3 [9.0-12.0s] — camera: Close-up front-on, eye level a few degrees below hers, camera in the place of the wall beside the screen, the laptop itself out of frame below the lower edge, static, locked off.
Every distance, height and frame position given above is literal and is held exactly; nothing drifts toward a more flattering angle.

FIRST FRAME AND SPATIAL BLOCKING The generation opens on this exact frame: Medium from three-quarter behind her left shoulder, seated eye level, camera about 120 cm high and one metre behind the chair, static, locked off — exactly the axis of the reference angle, the desk filling the lower right half of frame, the window a black rectangle screen-right. Starting positions, held until described otherwise: @Nora SEATED at x=55%, three-quarter back to camera, filling 58% of frame height, her face in lost profile toward the screen; the open laptop screen-left at x=25%, its screen a soft blue-white glow angled away from camera, its content unreadable from here and containing no characters. Left forearm flat on the desk, right hand at the trackpad. Her cheek and the edge of her nose carry the cold blue; the sodium rims her hair from screen-right. Expression: slack with attention, lips closed. This is the frame the first video frame must already be, before anything moves: nothing is settling into place, nothing fades up, nothing is mid-transition.

FORMAT MODE
One take of 12 seconds at real-time speed, containing exactly 3 successive framings joined by 2 hard cuts, placed at the moments the FRAME MAP gives and nowhere else. Each framing is held completely still between its cuts. No other cut, no montage, no dissolve, no speed ramp, no slow motion.

OPTICS
Anamorphic 85 mm f/2 equivalent. Depth of field wide open at that stop: the plane described in the FRAME MAP is tack sharp and everything behind it falls off progressively. Focus holds on that plane and breathes naturally with the camera's movement — no deliberate rack focus unless the FRAME MAP calls for one.

CONTINUITY LOCK Every prop named in the layout appears in EVERY shot where its surface is visible, in the same position and state — nothing appears, disappears, multiplies or moves unless the choreography says so. Each character's posture (SEATED or STANDING) is stated at the top of every shot and never changes off-screen. A character holds exactly the object the choreography puts in their hand — no other utensil or object may materialise. THE SCREEN'S CONTENT IS A LOCKED PROP: the same blue field and the same pale grey blocks in every frame of every shot, changing exactly once, at the single scroll, and never otherwise — no window opening, no popup, no notification, no cursor, no image, no photograph, no map, no drawing, no icon, no character of any alphabet at any time.

PROP LAYOUT — FIXED The cluttered desk against the wall, the window screen-right of it. At its centre the laptop, OPEN for this whole generation, its screen angled toward @Nora and away from camera in shot 1. Screen-left of the laptop: the leaning pile of dog-eared school books, spines away from camera, their covers scuffed to blankness. Screen-right of it: a cold mug of tea, untouched, ringed onto the topmost book. Behind her: the chair back with clothes slung over it, the unmade bed a dark mass at the frame edge. Nothing on the desk moves, nothing is added to it, nothing is picked up. Matter and wear, precise: the desk varnish is worn through to bare wood along the front edge and marked with old water rings; the laptop lid is clouded with fingerprints and carries the ghost outlines of peeled-off stickers, its charging cable kinked and mended with a turn of tape; the books' covers are soft and cupped, their corners rounded; the mug's glaze is crazed and its inside stained brown; the window sill's paint is flaking and old condensation stains sit in the corners of the panes.

FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND

SHOT 1 [0.0-4.0s] — Medium from three-quarter behind her left shoulder, seated eye level, camera about 120 cm high and one metre behind the chair, static, locked off — exactly the axis of the reference angle, the desk filling the lower right half of frame, the window a black rectangle screen-right.
[0.0s] Starting positions, held until described otherwise: @Nora SEATED at x=55%, three-quarter back to camera, filling 58% of frame height, her face in lost profile toward the screen; the open laptop screen-left at x=25%, its screen a soft blue-white glow angled away from camera, its content unreadable from here and containing no characters. Left forearm flat on the desk, right hand at the trackpad. Her cheek and the edge of her nose carry the cold blue; the sodium rims her hair from screen-right. Expression: slack with attention, lips closed.
[0.0-2.2s] Only her eyes move — small lateral travels along unseen lines, the blue reflection trembling faintly on her cheek. Nothing else in the room moves.
[2.2-3.2s] She leans in three centimetres — the shoulders follow, nothing else. Her lips part a millimetre.
[3.2-4.0s] Held, motionless but breathing, her eyes still working. Held to the cut.

HARD CUT

SHOT 2 [4.0-9.0s] — THE PLATE. Over her right shoulder, straight onto the laptop screen, camera about 130 cm high and 70 cm behind her, the screen square to the lens and IN FOCUS, static, locked off, no drift of any kind. The screen fills the middle of frame from x=22% to x=78% and 46% of frame height; the dark mass of her right shoulder and the back of her head cuts the lower left corner as an out-of-focus silhouette; the dark room around the screen is near-black.
[4.0s] The screen: a plain soft blue-white field with a scatter of pale grey blocks laid across it in horizontal bands — bands of flat pale grey with NO characters in them, not one letter, not one digit, not one punctuation mark, in any language, at any size. The blocks are motionless. Nothing else is on the screen: no cursor, no icon, no image, no photograph, no map, no drawing, no window frame, no menu bar.
[4.0-5.8s] Absolutely nothing moves in the frame except her breathing at the lower left corner and the faint flicker of the panel's own light. The screen holds. HOLD THIS EXACTLY: this window is a plate.
[5.8-6.4s] ONE SINGLE SCROLL, and one only: the whole field of pale grey blocks slides upward once, smoothly, about a third of the screen height, and settles. The block pattern that arrives is different from the one that left, and is equally characterless.
[6.4-9.0s] Nothing moves again. The screen holds the new arrangement, motionless, in focus, to the end of the shot. HOLD THIS EXACTLY: this window is a plate. No second scroll, no drift, no reframe, no change of brightness.

HARD CUT

SHOT 3 [9.0-12.0s] — Close-up front-on, eye level a few degrees below hers, camera in the place of the wall beside the screen, the laptop itself out of frame below the lower edge, static, locked off.
[9.0s] Starting positions: her face fills the frame at x=50%, 78% of frame height, lit cold blue-white from just below front; the sodium rim on her hair screen-right; behind her only the blue-black of the room. Eyes down toward the unseen screen, tracking left to right. Expression flat, tired, absorbed.
[9.0-10.2s] Reading. The eyes travel, a slow blink, one swallow at [9.8s].
[10.2-11.2s] Her eyes stop moving. They widen a fraction — not fear, arithmetic. Her lips part and close again without a sound. The blue light on her face is perfectly still.
[11.2-12.0s] Her gaze lifts an inch, off the screen, past it — toward the dark window and the night outside. Held to the end, no other movement, no expression added.

SUBJECT LOCK, NORA The exact girl of the reference @Nora — fifteen, long dark brown hair with a coarse natural wave, unwashed, pushed back behind the ears; grey-green eyes with the slight downward outer tilt under thick dark eyebrows; her father's straight nose and slightly squared jaw, her mother's wide mouth; pale olive skin that has lost its colour, chapped bitten lips with no colour, heavy lids with grey shadowed hollows beneath, faint freckles across the nose, bitten nails; thin adolescent build, shoulders rounded inward. The oversized faded charcoal-grey hooded sweatshirt with worn cuffs, hood down. No parka in this generation. No jewellery. Resting expression: flat, tired, closed. She never looks at the lens.

CROSS-FRAME RULES @NoraBedroom is the same room in all three shots: same desk with its worn varnish and water rings, same open laptop in the same place, same leaning pile of books, same mug, same window direction, same unmade bed in shadow, same two sources. The same girl throughout, exact face and wardrobe of her reference, in the same chair, in the same posture. The screen is open and lit in every shot and carries no legible character in any frame of any shot — not sharp, not blurred, not reflected in her eyes, not reflected in the window glass. She is the only human being in this generation: no second figure, no silhouette, no shadow of anyone else, in the room, in the doorway, in the window or in any reflection. Nothing red exists anywhere. Nobody looks at the lens. NO INVENTED ACTION: If a body part is not described as moving, it does not move. No gesture, step, head turn, prop interaction or expression change beyond the choreography written above; between described movements every body holds its last described position naturally (breathing, blinking, micro-sway only). CONTINUITY LOCK above and the POSITIVE CONSTRAINTS below apply in full.

CONTINUITY — WHAT MUST NOT DRIFT
Wardrobe, hair, dirt, damage and wear are exactly as the references define them and do not improve, clean themselves up or change between shots. Nobody is better groomed, better lit, better dressed or better rested than in the shot before. Props stay where the prop layout puts them. Weather, time of day and light level do not move inside a sequence. Nobody looks at the lens at any point.

LOCATION @NoraBedroom — the small bedroom of a fifteen-year-old at night: the cluttered desk against the wall, its varnish worn through at the front edge and marked with old water rings; the laptop, open, its lid clouded with fingerprints and the ghost outlines of peeled-off stickers, its charging cable kinked and mended with a turn of tape; the leaning pile of dog-eared school books, covers scuffed to blankness, a cold mug of tea ringed onto the topmost one; loose paper, a single earbud, a dead pen without its cap; the chair with clothes slung over the back and more clothes dropped on the floor beside it; the single bed with its rumpled dark quilt half pulled off the mattress, the fitted sheet escaping at one corner, the pillow dented and doubled over, deep in shadow; the window onto the back gallery and rooftops, condensation beaded along the bottom pane, dust felted on the sill, the catch painted stuck; dust along the skirting, a crumpled tissue by the bed, nothing put away. Unmade, uncared for. No red anywhere. No readable text, no lettering, no signage with words, no logos.

LIGHT Two sources only. The cold blue-white of the open laptop screen as the key — brightest on her face and on the desk edge and the nearest books, dying fast with distance, dead before it reaches the far wall, and shifting faintly once as the page moves; and the sodium orange of the street lamp through the window as a thin warm rim on her hair and along the sill, raking slightly upward because the lamp stands below the window. The two temperatures never mix. Deep blue-black shadow everywhere else, the whole frame gently underexposed, the corners of the room gone entirely, blacks truly black. In shot 2 the screen is the brightest thing in frame by a wide margin and holds an even, flat, unclipped brightness across its whole surface — no hot spot, no bloom that eats its edges, no flicker band. No other source, no fill, no bounce the room itself would not give.

DIALOGUE None. Nobody speaks in this generation. She reads.

LAST FRAME — THE EXACT STATE THIS SHOT HANDS OVER, because the next shot opens on it
WHAT IS IN THE FRAME AT THE LAST INSTANT: Her face front-on filling the frame, lit cold blue from below, eyes lifted just past the unseen screen toward the dark window, the sodium rim in her hair, everything behind her blue-black.
WHERE THIS SHOT LEAVES EACH BODY, to the number — these are the positions the next shot inherits, whether or not the body is still inside this last frame: @Nora: SEATED, x=55%, filling 58% of frame height.



CHARACTER PERFORMANCE
Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through nothing else: no added expression, no widened eyes, no trembling lip, no theatrical breath. What is not written does not happen. Between the written events every body simply holds its last position, breathing, blinking and drifting a few millimetres, never frozen and never fidgeting.
@Nora is SEATED at the desk for the entire generation and never stands, never leaves the chair, never turns away from the desk. Shoulders rounded inward, hood down, hair pushed behind the ears. Her hands: left forearm flat on the desk edge and staying there; right hand resting at the trackpad, the index finger moving only for the single scroll written in the FRAME MAP above. She wears the oversized faded charcoal-grey hoodie — no parka in this generation. She never types, never speaks, never touches her face.

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
SFX only. No music. No background music of any kind, no score, no drone, no ambient pad. The faint whirr of the laptop fan, her slow breathing, one swallow at [9.8s], one soft dry tap of the trackpad at [5.8s] and no other, a single car passing far below at [7.2s] — and beneath everything the low hum of the sleeping city, one gust pressing briefly on the window glass, the building's pipes ticking once as they cool. No typing. No keyboard. No voices. No notification sound. No music.

POSITIVE CONSTRAINTS — CHECK EVERY FRAME AGAINST THESE
Every named reference above is matched 100%: same face, same build, same wardrobe, same wear. Nobody is better groomed, better lit, better dressed or better rested than the shot before; wardrobe, hair, dirt, damage and wear do not improve or clean themselves up. Props stay exactly where the prop layout puts them. The light level, the weather and the time of day do not move inside this generation.
The choreography written in the FRAME MAP is the whole performance: no gesture, step, head turn, prop interaction or expression beyond it. Between described movements every body holds its last position naturally, breathing and blinking, never frozen and never fidgeting.
Nobody looks at the lens at any point. Nobody speaks except where DIALOGUE says so.
Every stroke of handwriting anywhere in frame is real handwriting laid out in straight horizontal lines — word-shaped clusters separated by spaces, gathered into sentences and paragraphs — in an invented cursive alphabet whose characters recur again and again the way a real alphabet's do. Unmistakably a script, but no script that exists on earth, and not one word readable in any language: it reads as writing from across the room and as nothing at all up close. Never random scribble, never a scrawl, never abstract mark-making, never decorative squiggles. No signage, no label, no digit, no subtitle, no caption is readable anywhere.
One continuous take at real-time speed for the exact duration requested, containing ONLY the framings and the hard cuts that FORMAT MODE declares above, at the moments the FRAME MAP gives and nowhere else. No dissolve, no fade, no montage, no extra cut. No slow motion, no speed ramp.

AVOID
readable text on the screen, legible letters, words, digits or interface on the screen, characters of any alphabet on the screen, a cursor, an icon, a photograph, a map, a drawing or an image on the screen, a browser window or menu bar, a notification popup, screen content reflected legibly in her eyes or in the window glass, a second scroll, the screen drifting or reframing, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, a second person, a silhouette in the doorway, a figure in the window, a reflection of anyone else, a long written coat, any coated figure, subjects looking at camera, visible camera rigs, camera movement, dolly, pan, zoom, handheld shake, slow motion, morphing objects, extra people in frame, extra gestures, improvised actions, wandering hands, typing on a keyboard, repositioned props, appearing or disappearing objects, warm lamps, tidy room, any red anywhere, a red charging LED, glamorous styling, posed expression, theatrical acting, overacting, rushed movements, uncanny smoothness, plastic skin, beauty filter, CGI look, video-game lighting, frozen characters, statue-like stillness, mannequin pose, freeze-frame stillness, generated music.
```








*⚠ **POINT DE COUPE — le plan fait 7 s au montage, la génération en fait 12.** Garder :
① **1,2 s** du shot 1, de `[2.6s]` à `[3.8s]` — elle penchée, les yeux qui travaillent : juste assez pour poser
le visage bleui et la nuit autour ; ② **4,0 s** du shot 2, de `[4.6s]` à `[8.6s]` — **c'est la plaque**, et
elle porte tout le plan : 1,2 s d'ÉTAT A, le scroll dedans, puis **2,2 s d'ÉTAT B plein** ; ③ **1,8 s** du
shot 3, de `[9.8s]` à `[11.6s]` — les yeux qui s'arrêtent, et le regard qui se lève vers la fenêtre.
**Ne jamais démarrer ② après `[4.6s]`** : l'ÉTAT A doit avoir le temps d'exister avant le scroll, sinon le
rituel arrive sans que rien ne l'ait précédé. **Ne jamais finir ② avant `[8.6s]`** : le script exige que le
rituel tienne pleinement à l'écran, et 2,2 s est le plancher.
**RÉSERVE, hors montage nominal** : `[11.6-12.0s]` du shot 3 — la tenue du regard levé. Elle n'entre que si le
cut vers 6B paraît trop sec, et on rogne alors sur ①, jamais sur la plaque.*

*⚠ **[POST] — LA PAGE.** Composer sur la plaque du shot 2, calé image par image sur le scroll de `[5.8-6.4s]` :
**ÉTAT A** les deux brèves d'une ligne (*« He asked my father for a chair. My father hadn't stood up in a
year. »* · *« He asked me for salt. »*) et la carte aux huit épingles, huit vignettes au trait du même dos ;
**ÉTAT B** le rituel en gras, seul, grand : *« If you carry a why too heavy: at midnight, cry it out to the
night, out loud. »* Curseur cyan. **AUCUN bloc de loi** — elle a été retirée du forum le 31/08, les trois
femmes viennent de la dire. **Aucune de ces lignes ne contient story / tale / legend / myth** (règle A).
Les huit vignettes sont dessinées en post : **jamais un manteau généré à l'image** (règle D).
⚠ Si le rush du shot 2 contient ne serait-ce qu'un caractère à l'écran, la prise est inutilisable telle quelle
(règle G) et le POST ne pourra pas s'y caler — lancer **6A-bis**.*

---


### VIDÉO 6A-bis — SECOURS de 6A *(6 s · à ne lancer QUE si le shot 2 de 6A sort avec des caractères à l'écran, une icône, un curseur ou une fenêtre de navigateur — c'est-à-dire dès qu'il est incalable en POST · Elements : @NoraBedroom · start frame : LIEU-08 IMAGE 3)*
**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 6 s |
| **Éléments** | @NoraBedroom |
| **`start_image`** | LIEU-08 IMAGE 3 |
| **`video_references`** | *aucune — c'est une tête de chaîne* |

> ⛔ **NE COLLE PAS CE TABLEAU.** Il est pour toi, pas pour le modèle : c'est ce que tu règles
> dans l'interface avant de coller. **Tu ne copies QUE le texte entre les triples backticks
> ci-dessous**, et rien d'autre — pas le titre, pas ce tableau, pas cette ligne.


```
SCENE CONTEXT
A laptop screen alone in a dark empty bedroom, holding a page that is only light and blocks. It sits still, scrolls once, and sits still again. One single shot, no cut, closer than the main version and without anyone in frame, so the surface is clean enough to be composed on. Nobody appears at any point. Every second is choreographed below; nothing beyond it may be invented. 6 seconds, one continuous framing, no cut.

CONTINUITY REFERENCE — NO VIDEO IS ATTACHED
No previous clip is attached to this generation. This is the first shot of its chain: it sets the light, the grain and the skin rendering that every following shot will be matched to. Build every frame new from the references below, at full quality.

ACTIVE REFERENCES
@NoraBedroom: Nora's bedroom and the landing outside it, grey and underexposed, one narrow sodium band under the door. 100% matches the reference.

LOCATION MAP
Framing 1 [0.0-6.0s] — camera: Static, camera about 105 cm high and 45 cm from the laptop, the screen square to the lens and IN FOCUS, locked off, absolutely no drift. The screen fills the frame from x=14% to x=86% and 62% of frame height; the worn keyboard along the bottom edge; near-black on all four sides.
Every distance, height and frame position given above is literal and is held exactly; nothing drifts toward a more flattering angle.

FIRST FRAME AND SPATIAL BLOCKING The generation opens on this exact frame: Static, camera about 105 cm high and 45 cm from the laptop, the screen square to the lens and IN FOCUS, locked off, absolutely no drift. The screen fills the frame from x=14% to x=86% and 62% of frame height; the worn keyboard along the bottom edge; near-black on all four sides. The screen: a plain soft blue-white field with a scatter of pale grey blocks laid across it in horizontal bands — bands of flat pale grey with NO characters in them, not one letter, not one digit, not one punctuation mark, in any language, at any size. The blocks are motionless. Nothing else is on the screen: no cursor, no icon, no image, no photograph, no map, no drawing, no window frame, no menu bar. This is the frame the first video frame must already be, before anything moves: nothing is settling into place, nothing fades up, nothing is mid-transition.

FORMAT MODE
One single continuous uncut take, 6 seconds long, at real-time speed. No cut, no montage, no dissolve, no speed ramp, no slow motion.

OPTICS
Anamorphic 85 mm f/2 equivalent. Depth of field wide open at that stop: the plane described in the FRAME MAP is tack sharp and everything behind it falls off progressively. Focus holds on that plane and breathes naturally with the camera's movement — no deliberate rack focus unless the FRAME MAP calls for one.

CONTINUITY LOCK Every prop named in the layout appears in the frame where its surface is visible, in the same position and state — nothing appears, disappears, multiplies or moves unless the choreography says so. THE SCREEN'S CONTENT IS A LOCKED PROP: the same blue field and the same pale grey blocks in every frame, changing exactly once, at the single scroll, and never otherwise — no window opening, no popup, no notification, no cursor, no icon, no image, no photograph, no map, no drawing, no character of any alphabet at any time. NOBODY ENTERS: no hand, no shoulder, no reflection of a person, at any point.

PROP LAYOUT — FIXED The open laptop on the worn desk, its screen square to the lens and filling most of the frame; below its lower edge, the top of the keyboard in raking light, the keycaps worn shiny at their centres, the letters on them rubbed away to blankness. Around the screen the room is near-black. Nothing else is in frame and nothing is added. Matter and wear, precise: the screen bezel carries a fine film of dust and two thumb smears at its lower corners; the panel's surface holds the faintest grid of its own coating and a shallow scratch across the lower third; the desk varnish beyond the laptop is worn through to bare wood and marked with old water rings.

FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND

SHOT 1 [0.0-6.0s] — Static, camera about 105 cm high and 45 cm from the laptop, the screen square to the lens and IN FOCUS, locked off, absolutely no drift. The screen fills the frame from x=14% to x=86% and 62% of frame height; the worn keyboard along the bottom edge; near-black on all four sides.
[0.0s] The screen: a plain soft blue-white field with a scatter of pale grey blocks laid across it in horizontal bands — bands of flat pale grey with NO characters in them, not one letter, not one digit, not one punctuation mark, in any language, at any size. The blocks are motionless. Nothing else is on the screen: no cursor, no icon, no image, no photograph, no map, no drawing, no window frame, no menu bar.
[0.0-2.4s] Nothing moves at all except the panel's own faint light and the grain of the image. HOLD THIS EXACTLY: this window is a plate.
[2.4-3.0s] ONE SINGLE SCROLL, and one only: the whole field of pale grey blocks slides upward once, smoothly, about a third of the screen height, and settles. The block pattern that arrives is different from the one that left, and is equally characterless.
[3.0-6.0s] Nothing moves again. The screen holds the new arrangement, motionless, in focus, to the end. HOLD THIS EXACTLY: this window is a plate. No second scroll, no drift, no reframe, no change of brightness, nothing entering frame.

SUBJECT LOCK, NORA Not present. @Nora does not appear in this generation, in any frame, in any reflection, in any shadow. No person of any kind is in frame.

CROSS-FRAME RULES One continuous shot — no cut, no reframe, no camera movement of any kind. @NoraBedroom is the same room as its reference Element: same worn desk with its water rings, same laptop with its fingerprinted lid and taped cable, same near-black room around it, same two sources. The screen carries no legible character in any frame — not sharp, not blurred, not reflected in the bezel, not reflected in anything. Nothing red exists anywhere. NO INVENTED ACTION: If a body part is not described as moving, it does not move. No gesture, step, head turn, prop interaction or expression change beyond the choreography written above; between described movements every body holds its last described position naturally (breathing, blinking, micro-sway only). CONTINUITY LOCK above and the POSITIVE CONSTRAINTS below apply in full.

CONTINUITY — WHAT MUST NOT DRIFT
Wardrobe, hair, dirt, damage and wear are exactly as the references define them and do not improve, clean themselves up or change between shots. Nobody is better groomed, better lit, better dressed or better rested than in the shot before. Props stay where the prop layout puts them. Weather, time of day and light level do not move inside a sequence. Nobody looks at the lens at any point.

LOCATION @NoraBedroom — the cluttered desk of a fifteen-year-old's bedroom at night, seen close: the desk varnish worn through to bare wood along the front edge and marked with old water rings; the open laptop, its lid clouded with fingerprints and the ghost outlines of peeled-off stickers, its charging cable kinked and mended with a turn of tape, the keycaps worn shiny at their centres with their letters rubbed away to blankness; beyond the pool of screen light, the leaning pile of dog-eared school books and the cold ringed mug lost in shadow, the unmade bed and the window only as darkness. Unmade, uncared for. No red anywhere. No readable text, no lettering, no signage with words, no logos.

LIGHT One source only: the screen itself, cold blue-white, even and flat and unclipped across its whole surface — no hot spot, no bloom eating its edges, no flicker band, no scan line. It rakes across the keyboard at the bottom edge and dies within thirty centimetres; everything beyond that is near-black, gently underexposed, the corners gone entirely, blacks truly black. A trace of sodium orange survives far behind, at the very edge of the frame, as a single warm thread on the sill — nothing more. No other source, no fill.

DIALOGUE None. Nobody speaks in this generation. The room is empty.

LAST FRAME — THE EXACT STATE THIS SHOT HANDS OVER, because the next shot opens on it
WHAT IS IN THE FRAME AT THE LAST INSTANT: The laptop screen square to the lens, filling the frame, an even cold blue-white field with its motionless pale grey blocks and not one character on it; the worn keyboard raking along the bottom edge; near-black on all four sides.



CHARACTER PERFORMANCE
Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through nothing else: no added expression, no widened eyes, no trembling lip, no theatrical breath. What is not written does not happen. Between the written events every body simply holds its last position, breathing, blinking and drifting a few millimetres, never frozen and never fidgeting.
Nobody is in this generation. No person, no body, no hand, no shoulder, no reflected figure, in any frame.

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
SFX only. No music. No background music of any kind, no score, no drone, no ambient pad. The faint whirr of the laptop fan, the low hum of the sleeping city under it, one gust pressing briefly on the window glass far behind, the building's pipes ticking once as they cool. One soft dry tap of a trackpad at [2.4s], off screen, and no other. No breathing. No typing. No voices. No notification sound. No music.

POSITIVE CONSTRAINTS — CHECK EVERY FRAME AGAINST THESE
Every named reference above is matched 100%: same face, same build, same wardrobe, same wear. Nobody is better groomed, better lit, better dressed or better rested than the shot before; wardrobe, hair, dirt, damage and wear do not improve or clean themselves up. Props stay exactly where the prop layout puts them. The light level, the weather and the time of day do not move inside this generation.
The choreography written in the FRAME MAP is the whole performance: no gesture, step, head turn, prop interaction or expression beyond it. Between described movements every body holds its last position naturally, breathing and blinking, never frozen and never fidgeting.
Nobody looks at the lens at any point. Nobody speaks except where DIALOGUE says so.
Every stroke of handwriting anywhere in frame is real handwriting laid out in straight horizontal lines — word-shaped clusters separated by spaces, gathered into sentences and paragraphs — in an invented cursive alphabet whose characters recur again and again the way a real alphabet's do. Unmistakably a script, but no script that exists on earth, and not one word readable in any language: it reads as writing from across the room and as nothing at all up close. Never random scribble, never a scrawl, never abstract mark-making, never decorative squiggles. No signage, no label, no digit, no subtitle, no caption is readable anywhere.
One continuous uncut take at real-time speed, for the exact duration requested. No slow motion, no speed ramp, no added cut.

AVOID
readable text on the screen, legible letters, words, digits or interface on the screen, characters of any alphabet on the screen, a cursor, an icon, a photograph, a map, a drawing or an image on the screen, a browser window or menu bar, a notification popup, a second scroll, the screen drifting or reframing, screen flicker bands, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, a person, a hand, a shoulder, a reflection of anyone, a long written coat, any coated figure, subjects looking at camera, visible camera rigs, camera movement, dolly, pan, zoom, handheld shake, slow motion, morphing objects, extra people in frame, extra gestures, improvised actions, repositioned props, appearing or disappearing objects, warm lamps, any red anywhere, a red charging LED, uncanny smoothness, plastic skin, beauty filter, CGI look, video-game lighting, frozen characters, statue-like stillness, mannequin pose, freeze-frame stillness, generated music.
```








*⚠ **Réglage de 6A-bis** : Lens Anamorphic **85 mm f/2**, 6 s.
**Comment se monte 6A-bis** : garder `[0.6-4.6s]` — **4,0 s**, soit 1,8 s d'ÉTAT A, le scroll de `[2.4-3.0s]`
dedans, puis 1,6 s d'ÉTAT B… **et c'est le piège** : l'ÉTAT B doit tenir 2,2 s. Garder donc `[0.4-4.8s]` =
**4,4 s**, avec 2,0 s d'ÉTAT A et **2,4 s d'ÉTAT B**, et rogner alors 0,4 s sur le fragment ① de 6A (le shot 1
passe à 0,8 s). Le fragment remplace tel quel les 4,0 s de plaque de 6A ; ① et ③ de 6A restent valables et se
recollent autour sans retouche — **le raccord est invisible parce que la plaque est déjà un plan sans elle** :
on passe de son épaule à l'écran seul, ce que le montage fait de toute façon.*

---


## VIDÉO 6B — plan 6.2 « Le cri » *(12 s de rushes → 9 s au montage · Elements : @Nora + @BackGallery · start frame : LIEU-09 IMAGE 2 ; l'IMAGE 3 est l'axe du shot 2)*
**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 12 s |
| **Éléments** | @Nora + @BackGallery |
| **`start_image`** | LIEU-09 IMAGE 2 ; l'IMAGE 3 est l'axe du shot 2 |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> ⛔ **NE COLLE PAS CE TABLEAU.** Il est pour toi, pas pour le modèle : c'est ce que tu règles
> dans l'interface avant de coller. **Tu ne copies QUE le texte entre les triples backticks
> ci-dessous**, et rien d'autre — pas le titre, pas ce tableau, pas cette ligne.


```
SCENE CONTEXT
At midnight a girl comes out onto the rear gallery of her building, takes hold of the rail, hesitates, and throws one question out loud at the rooftops. Nothing answers. A dog barks twice, very far away. She lets go and goes back in. Two shots, one hard cut. She is the only living being on screen and nothing in the world responds to her. Every second is choreographed below; nothing beyond it may be invented. 12 seconds, in 2 framings joined by 1 hard cut.

CONTINUITY REFERENCE — SAME FILM, DIFFERENT PLACE
THE VIDEO ATTACHED TO THIS GENERATION is an earlier shot from the same film (6A), in a different place. Use it ONLY to match the physical rendering — the film stock, the grain structure, the way skin and fabric resolve, the focus behaviour, the highlight roll-off. Do NOT take its light, its palette, its exposure level or its composition: this shot's light comes from its own LOCATION and LIGHT paragraphs below, and its framing from its own FRAME MAP. Everything else is built new, at full quality.

HANDOFF — THE EXACT STATE THIS SHOT INHERITS FROM THE ATTACHED VIDEO
These are NOT new positions to invent. This is the frame the previous shot (6A) ends on, repeated here to the number, and the first frame of this generation must reproduce it exactly before anything moves.
WHAT IS IN THE FRAME AT THE LAST INSTANT: Her face front-on filling the frame, lit cold blue from below, eyes lifted just past the unseen screen toward the dark window, the sodium rim in her hair, everything behind her blue-black.
WHERE THIS SHOT LEAVES EACH BODY, to the number — these are the positions the next shot inherits, whether or not the body is still inside this last frame: @Nora: SEATED, x=55%, filling 58% of frame height.
Nothing in this list may be re-placed, re-lit or improved. Whatever the FRAME MAP below asks for happens AFTER this state, never instead of it.

ACTIVE REFERENCES
@Nora: Nora, fifteen, long dark brown unwashed hair, grey-green eyes, pale olive skin gone colourless, bitten lips, heavy lids over grey hollows, thin build. Running on empty: grief has made her polite and absent — she answers, she says thank you, and none of it reaches her face. She goes very still before anything shows. NOTHING RED ON HER. 100% matches the reference.
@BackGallery: The back gallery at night under sodium — a painted wooden rail, grey over green over an older white, the paint flaking to bare silvered wood along the top; peeling deck boards with the grain raised and the nailheads standing proud and rusted. 100% matches the reference.

TEMPERAMENT, NORA A fifteen-year-old running on empty. Grief has made her polite and absent: she answers, she carries the dish back, she says thank you, and none of it reaches her face. Her body is tired before the day starts. She does not cry in front of people — the swollen eyelids come from somewhere else, earlier. When something does move her, she goes very still first, and only then does it show.

LOCATION MAP
Framing 1 [0.0-5.0s] — camera: Wide along the gallery, eye level, camera about 160 cm high on the gallery itself looking down its length, static, locked off — exactly the axis of the reference angle: the empty walkway running away from camera, the rail screen-left, the ajar door in the wall screen-right at x=78%, the cold blue sky, the rooftops and the far harbour cranes beyond, the warm rectangle low across the boards at the bottom frame edge.
Framing 2 [5.0-12.0s] — camera: Medium close along the rail, three-quarter left profile, eye level, camera about 160 cm high and 1.5 m from the rail, static, locked off — the axis of the second reference angle: the rail crossing from the lower left foreground toward mid-frame, its top rubbed to bare grey wood where her hands rest, the dark rooftops and back yards soft beyond it screen-left, the receding rails of the flats above and below soft screen-right, the empty washing line sagging through the upper frame, the cold deep blue sky above. The warm rectangle is out of this frame entirely.
Every distance, height and frame position given above is literal and is held exactly; nothing drifts toward a more flattering angle.

FIRST FRAME AND SPATIAL BLOCKING The generation opens on this exact frame: Wide along the gallery, eye level, camera about 160 cm high on the gallery itself looking down its length, static, locked off — exactly the axis of the reference angle: the empty walkway running away from camera, the rail screen-left, the ajar door in the wall screen-right at x=78%, the cold blue sky, the rooftops and the far harbour cranes beyond, the warm rectangle low across the boards at the bottom frame edge. Frame contents, nothing moving through them yet: the gallery exactly as the reference, empty, nobody in it. The warm rectangle lies low, unremarked. The washing line sags empty overhead. This is the frame the first video frame must already be, before anything moves: nothing is settling into place, nothing fades up, nothing is mid-transition.

FORMAT MODE
One take of 12 seconds at real-time speed, containing exactly 2 successive framings joined by 1 hard cut, placed at the moments the FRAME MAP gives and nowhere else. Each framing is held completely still between its cuts. No other cut, no montage, no dissolve, no speed ramp, no slow motion.

OPTICS
Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described in the FRAME MAP is tack sharp and everything behind it falls off progressively. Focus holds on that plane and breathes naturally with the camera's movement — no deliberate rack focus unless the FRAME MAP calls for one.

CONTINUITY LOCK Every prop named in the layout appears in EVERY shot where its surface is visible, in the same position and state — nothing appears, disappears, multiplies or moves unless the choreography says so. Each character's posture (SEATED or STANDING) is stated at the top of every shot and never changes off-screen. A character holds exactly the object the choreography puts in their hand — no other utensil or object may materialise; her hands are empty for the whole generation. THE WORLD DOES NOT ANSWER: no light anywhere changes brightness, no window lights up or goes dark, no curtain moves, no door opens, no shape appears at any point, before, during or after the line.

PROP LAYOUT — FIXED The gallery boards bare and peeling. The painted wooden rail runs across frame on its turned balusters, two of them replaced with plain sticks. The washing line sags overhead, EMPTY — no laundry, not one garment, ever. The door back into the flat stands ajar at the screen-right edge of the wide shot, dark inside. The warm rectangle of light from the flat below lies across the boards near the lower frame edge in the wide shot only, unremarked, cut by the rail's shadow, and is out of frame entirely in the close shot. Every window of the flats below and above stays dark or unframed — no lit window is ever framed directly, no figure and no silhouette appears in any window, doorway or yard. Nothing moves in this generation except @Nora. Matter and wear, precise: the rail is grey over green over an older white, the layers curling and flaking, rubbed to bare silvered wood along the top where hands have rested for decades; the deck boards have the grain raised and split at the ends, rusted nailheads standing proud, each bleeding a small dark streak, grit and dead leaves caught in the gaps; the washing line is grey-green cord, slackened and frayed, its fibres fuzzed along the sag, a few wooden pegs left clipped to it, one split; rust streaks bleed from the rail brackets down the posts; the boards still hold a thin sheen from earlier rain.

FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND

SHOT 1 [0.0-5.0s] — Wide along the gallery, eye level, camera about 160 cm high on the gallery itself looking down its length, static, locked off — exactly the axis of the reference angle: the empty walkway running away from camera, the rail screen-left, the ajar door in the wall screen-right at x=78%, the cold blue sky, the rooftops and the far harbour cranes beyond, the warm rectangle low across the boards at the bottom frame edge.
[0.0s] Frame contents, nothing moving through them yet: the gallery exactly as the reference, empty, nobody in it. The warm rectangle lies low, unremarked. The washing line sags empty overhead.
[0.0-1.2s] The empty gallery breathes: the night, a far-off car, the cord of the line stirring a few millimetres in the wind. Nothing else.
[1.2-2.6s] @Nora steps out through the ajar door without hurry — three slow steps, arms held close to her body against the cold, her breath visible — and stops at the rail at x=45%, filling 54% of frame height, facing the night, her back three-quarter to camera. She does not close the door behind her.
[2.6-5.0s] Both hands close on the rail. Her weight settles forward onto them, head slightly bowed. She stands. Her breath clouds twice. Held to the cut, no other movement.

HARD CUT

SHOT 2 [5.0-12.0s] — Medium close along the rail, three-quarter left profile, eye level, camera about 160 cm high and 1.5 m from the rail, static, locked off — the axis of the second reference angle: the rail crossing from the lower left foreground toward mid-frame, its top rubbed to bare grey wood where her hands rest, the dark rooftops and back yards soft beyond it screen-left, the receding rails of the flats above and below soft screen-right, the empty washing line sagging through the upper frame, the cold deep blue sky above. The warm rectangle is out of this frame entirely.
[5.0s] Starting positions, held until described otherwise: @Nora at x=45%, filling 72% of frame height, in three-quarter left profile facing the dark rooftops screen-left, both hands on the rail, the knuckles pale with grip, weight forward. Her breath fast and shallow, visible. Expression: a tired face with two things fighting on it, neither of them named.
[5.0-6.6s] She hesitates — the mouth opens and closes again without a sound; the grip tightens; one breath drawn deeper than the others and held half a second.
[6.6-8.4s] THE LINE, out loud, thrown at the rooftops, louder than she meant it, the voice cracking on the last word: "Why did my mother die?" Her chin comes up on the line; nothing else in her body moves; her hands stay exactly where they are.
[8.4-10.4s] Stillness. Her breath clouds, fast then slower. NOTHING ANSWERS — no voice, no echo, no light changing anywhere in frame, no shape appearing. At [9.4s], very far away, a dog barks twice. Her eyes stay on the rooftops, then close for one full second and open again.
[10.4-12.0s] She lets go of the rail, straightens, and turns without hurry back toward the door — two slow steps, her back to camera. Held on her back to the end.

SUBJECT LOCK, NORA The exact girl of the reference @Nora — fifteen, long dark brown hair with a coarse natural wave, unwashed, pushed back behind the ears; grey-green eyes with the slight downward outer tilt under thick dark eyebrows; her father's straight nose and slightly squared jaw, her mother's wide mouth; pale olive skin that has lost its colour, chapped bitten lips, heavy lids with grey shadowed hollows beneath, faint freckles across the nose, bitten nails; thin adolescent build, shoulders rounded inward. The dark navy nylon parka with the broken zip pull over the oversized faded charcoal-grey hooded sweatshirt, hood down, straight-leg dark indigo jeans frayed at the hem, scuffed off-white canvas sneakers. No jewellery. Resting expression: flat, exhausted, closed. She never looks at the lens.

CROSS-FRAME RULES @BackGallery is the same gallery in both shots: same painted rail flaking to bare silvered wood, same peeling boards with their proud rusted nailheads, same empty sagging washing line, same receding rails of the flats below and above, same rooftops and far harbour cranes, same sodium direction from below and behind. The same girl in both shots, exact face and wardrobe of her reference, the same parka over the same hoodie, her hands empty throughout. The camera never moves in either shot — no pan, no tilt, no push, no drift — and never frames any lit window directly; the warm rectangle stays at the lower frame edge of the wide shot only, is never approached, never favoured, never inserted, and is simply absent from the close shot. She is the only human being in the entire generation: no figure, no silhouette and no shadow of anyone else exists anywhere, in any window, doorway, yard or reflection. The washing line is empty in every frame. Nothing red exists anywhere. Nobody looks at the lens. NO INVENTED ACTION: If a body part is not described as moving, it does not move. No gesture, step, head turn, prop interaction or expression change beyond the choreography written above; between described movements every body holds its last described position naturally (breathing, blinking, micro-sway only). CONTINUITY LOCK above and the POSITIVE CONSTRAINTS below apply in full.

CONTINUITY — WHAT MUST NOT DRIFT
Wardrobe, hair, dirt, damage and wear are exactly as the references define them and do not improve, clean themselves up or change between shots. Nobody is better groomed, better lit, better dressed or better rested than in the shot before. Props stay where the prop layout puts them. Weather, time of day and light level do not move inside a sequence. Nobody looks at the lens at any point.

LOCATION @BackGallery — the rear wooden gallery of a triple-decker at night: a painted wooden rail, grey over green over an older white, the layers flaking to bare silvered wood along the top where hands have rubbed it smooth, on turned balusters, two of them replaced with plain sticks; peeling deck boards with the grain raised, the nailheads standing proud and rusted, each bleeding a small dark streak, gaps between the boards opening onto darkness, grit and dead leaves caught in them; a washing line of grey-green cord sagging between two hooks, a few wooden pegs left clipped to it, one split, no laundry on it; the galleries of the flats below and above visible as receding rails, the underside of the one above stained by years of drips; rust streaks bleeding from the rail brackets down the posts; back yards and rooftops beyond — asphalt shingles, leaning fences, a shed with a tarpaulin roof — and harbour cranes far off against the sky; the door back into the flat, its paint chipped around the latch. The boards still hold a thin sheen from earlier rain. No red anywhere. No readable text, no lettering, no signage with words, no logos.

LIGHT Two sources only. Sodium street lamps from below and behind, raking their dull orange upward — catching the underside of the rail, the curled paint flakes, the proud rusted nailheads and the bare-wood patches along the top, edging her jaw and shoulder from behind, and lighting her breath into brief clouds. And the cold deep blue of the night sky as a weak top fill on her shoulders and on the boards. Her face stays in cold half-light, gently underexposed, and the blacks between the sources are truly black. The warm rectangle from the flat below lies on the boards at the bottom frame edge of the wide shot as one texture among others, never brightening, never dimming, never approached, never lit differently from one shot to the next; it is out of frame in the close shot. NO LIGHT ANYWHERE CHANGES AT ANY POINT IN THIS GENERATION. No other source, no fill.

DIALOGUE [6.6-8.4s] @Nora, out loud to the night, thrown at the rooftops, louder than she meant it, the voice cracking on the last word: "Why did my mother die?"

LAST FRAME — THE EXACT STATE THIS SHOT HANDS OVER, because the next shot opens on it
WHAT IS IN THE FRAME AT THE LAST INSTANT: Her back at the gallery rail, already turning away toward the ajar door, both hands off the rail and at her sides, the empty washing line sagging above, the rooftops and the harbour cranes beyond, the warm rectangle unchanged and unremarked at the lower frame edge — nothing in the world has answered.
WHERE THIS SHOT LEAVES EACH BODY, to the number — these are the positions the next shot inherits, whether or not the body is still inside this last frame: @Nora: STANDING, x=45%, filling 72% of frame height.



CHARACTER PERFORMANCE
Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through nothing else: no added expression, no widened eyes, no trembling lip, no theatrical breath. What is not written does not happen. Between the written events every body simply holds its last position, breathing, blinking and drifting a few millimetres, never frozen and never fidgeting.
@Nora is STANDING for the entire generation — she never sits, never crouches, never leans over the rail, never climbs anything. She wears the dark navy nylon parka with the broken zip pull over the charcoal hoodie, hood down. Her hands are empty throughout: at her sides from [0.0s] to [2.6s], BOTH ON THE RAIL from [2.6s] to [10.4s], at her sides again after. She holds no object at any point.

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
SFX only. No music. No background music of any kind, no score, no drone, no ambient pad. Night wind, the boards creaking under her steps, the low tide-hum of the port beneath everything, a loose halyard clinking far off against a mast, a single car crossing the town below at [4.2s], her breathing audible and quick; then the line — one voice alone in the night, dry and unamplified, no reverb, no echo, no space added to it — and after it a long true silence with nothing in it but the wind, broken at [9.4s] by a dog barking twice, very far away. No reply of any kind. No door, no window, no voice. No music.

POSITIVE CONSTRAINTS — CHECK EVERY FRAME AGAINST THESE
Every named reference above is matched 100%: same face, same build, same wardrobe, same wear. Nobody is better groomed, better lit, better dressed or better rested than the shot before; wardrobe, hair, dirt, damage and wear do not improve or clean themselves up. Props stay exactly where the prop layout puts them. The light level, the weather and the time of day do not move inside this generation.
The choreography written in the FRAME MAP is the whole performance: no gesture, step, head turn, prop interaction or expression beyond it. Between described movements every body holds its last position naturally, breathing and blinking, never frozen and never fidgeting.
Nobody looks at the lens at any point. Nobody speaks except where DIALOGUE says so.
Every stroke of handwriting anywhere in frame is real handwriting laid out in straight horizontal lines — word-shaped clusters separated by spaces, gathered into sentences and paragraphs — in an invented cursive alphabet whose characters recur again and again the way a real alphabet's do. Unmistakably a script, but no script that exists on earth, and not one word readable in any language: it reads as writing from across the room and as nothing at all up close. Never random scribble, never a scrawl, never abstract mark-making, never decorative squiggles. No signage, no label, no digit, no subtitle, no caption is readable anywhere.
One continuous take at real-time speed for the exact duration requested, containing ONLY the framings and the hard cuts that FORMAT MODE declares above, at the moments the FRAME MAP gives and nowhere else. No dissolve, no fade, no montage, no extra cut. No slow motion, no speed ramp.

AVOID
a second person, a man, any figure or silhouette in any window, doorway or yard, a lit kitchen window framed directly, an insert of a window, a window lighting up or going dark, a curtain moving, a door opening, camera movement, camera tilt, camera pan, push-in toward any window, drift, any red anywhere, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, subjects looking at camera, visible camera rigs, slow motion, rain, thunder, an answering voice, reverb or echo on the voice, an amplified or processed voice, extra people in frame, extra gestures, improvised actions, wandering hands, laundry on the line, warm light on her face, a long written coat, any coated figure, theatrical acting, overacting, screaming, sobbing, rushed movements, uncanny smoothness, plastic skin, beauty filter, CGI look, video-game lighting, frozen characters, statue-like stillness, mannequin pose, freeze-frame stillness, generated music.
```








*⚠ **POINT DE COUPE — le plan fait 9 s au montage, la génération en fait 12.** Garder :
① **3,4 s** du shot 1, de `[1.0s]` à `[4.4s]` — la fin de la galerie vide, sa sortie, sa marche, ses deux mains
qui se ferment sur le rail ; ② **5,6 s** du shot 2, de `[6.0s]` à `[11.6s]` — la fin de l'hésitation, la
réplique entière, le silence, le chien, les yeux qui se ferment, et **les deux premiers pas du retour**.
**Ne jamais couper avant `[10.4s]`** dans ② : le script écrit « elle reste un instant, **puis rentre** » — sans
ces deux pas, le plan finit sur une fille qui attend encore, et 6.3 arrive de nulle part.
**RÉSERVE** : `[0.0-1.0s]` du shot 1, la galerie vide, si l'entrée dans la séquence a besoin d'air.*

*⚠ **CONTRÔLE À FAIRE SUR LE RUSH — trois choses, dans cet ordre.** ① **Aucune fenêtre allumée cadrée, aucune
silhouette nulle part** : c'est la seule chose qui ferait exister quelqu'un d'autre dans ce plan, et tout le
film tient sur le fait qu'on croit que personne n'a entendu. ② **Aucune lumière ne change**, avant, pendant ni
après la réplique — un carreau qui s'allume, et le monde a répondu. ③ **Aucun écho, aucune réverbération** sur
la voix : le cri doit tomber à plat dans la nuit. Si l'un des trois lâche, la prise est à refaire.*

---


### VIDÉO 6B-bis — SECOURS de 6B *(6 s · à ne lancer QUE si le shot 2 de 6B rate : une fenêtre allumée ou une silhouette entre au cadre, une lumière change pendant la réplique, ou la voix sort avec de l'écho · Elements : @Nora + @BackGallery · start frame : LIEU-09 IMAGE 3, au rail)*
**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 6 s |
| **Éléments** | @Nora + @BackGallery |
| **`start_image`** | LIEU-09 IMAGE 3, au rail |
| **`video_references`** | *aucune — c'est une tête de chaîne* |

> ⛔ **NE COLLE PAS CE TABLEAU.** Il est pour toi, pas pour le modèle : c'est ce que tu règles
> dans l'interface avant de coller. **Tu ne copies QUE le texte entre les triples backticks
> ci-dessous**, et rien d'autre — pas le titre, pas ce tableau, pas cette ligne.


```
SCENE CONTEXT
At midnight, at the rail of a rear gallery, a girl hesitates and throws one question out loud at the rooftops. Nothing answers. A dog barks twice, very far away. One single shot, no cut, tighter than the main version so that nothing in the world can enter the frame to answer her. She is the only living being on screen. Every second is choreographed below; nothing beyond it may be invented. 6 seconds, one continuous framing, no cut.

CONTINUITY REFERENCE — NO VIDEO IS ATTACHED
No previous clip is attached to this generation. This is the first shot of its chain: it sets the light, the grain and the skin rendering that every following shot will be matched to. Build every frame new from the references below, at full quality.

ACTIVE REFERENCES
@Nora: Nora, fifteen, long dark brown unwashed hair, grey-green eyes, pale olive skin gone colourless, bitten lips, heavy lids over grey hollows, thin build. Running on empty: grief has made her polite and absent — she answers, she says thank you, and none of it reaches her face. She goes very still before anything shows. NOTHING RED ON HER. 100% matches the reference.
@BackGallery: The back gallery at night under sodium — a painted wooden rail, grey over green over an older white, the paint flaking to bare silvered wood along the top; peeling deck boards with the grain raised and the nailheads standing proud and rusted. 100% matches the reference.

TEMPERAMENT, NORA A fifteen-year-old running on empty. Grief has made her polite and absent: she answers, she carries the dish back, she says thank you, and none of it reaches her face. Her body is tired before the day starts. She does not cry in front of people — the swollen eyelids come from somewhere else, earlier. When something does move her, she goes very still first, and only then does it show.

LOCATION MAP
Framing 1 [0.0-6.0s] — camera: Medium close along the rail, three-quarter left profile, eye level, camera about 160 cm high and 1.2 m from her, static, locked off, one size tighter than the main version so the frame is filled by her, the rail and the night alone.
Every distance, height and frame position given above is literal and is held exactly; nothing drifts toward a more flattering angle.

FIRST FRAME AND SPATIAL BLOCKING The generation opens on this exact frame: Medium close along the rail, three-quarter left profile, eye level, camera about 160 cm high and 1.2 m from her, static, locked off, one size tighter than the main version so the frame is filled by her, the rail and the night alone. Starting positions, held until described otherwise: @Nora at x=45%, filling 82% of frame height, in three-quarter left profile facing the dark rooftops screen-left, both hands on the rail, weight forward, head slightly bowed. Her breath fast and shallow, visible in the cold. Expression: a tired face with two things fighting on it, neither of them named. This is the frame the first video frame must already be, before anything moves: nothing is settling into place, nothing fades up, nothing is mid-transition.

FORMAT MODE
One single continuous uncut take, 6 seconds long, at real-time speed. No cut, no montage, no dissolve, no speed ramp, no slow motion.

OPTICS
Anamorphic 85 mm f/2 equivalent. Depth of field wide open at that stop: the plane described in the FRAME MAP is tack sharp and everything behind it falls off progressively. Focus holds on that plane and breathes naturally with the camera's movement — no deliberate rack focus unless the FRAME MAP calls for one.

CONTINUITY LOCK Every prop named in the layout appears in the frame where its surface is visible, in the same position and state — nothing appears, disappears, multiplies or moves unless the choreography says so. Her posture (STANDING) is stated below and never changes; her hands are empty and stay on the rail. THE WORLD DOES NOT ANSWER: no light anywhere changes brightness, no window lights up or goes dark, no curtain moves, no door opens, no shape appears at any point, before, during or after the line. NO WINDOW, NO DOOR AND NO WALKWAY IS IN THIS FRAME AT ALL.

PROP LAYOUT — FIXED The painted rail crossing the frame from the lower left foreground toward mid-frame, its turned balusters and rust-streaked brackets below it. The empty washing line sagging through the upper frame — no laundry, not one garment, ever. Beyond the rail, soft and far, dark rooftops and back yards; screen-right, soft, the receding rails of the flats above and below. Nothing else is in frame; no door, no window, no lit rectangle, no threshold. Matter and wear, precise: the rail is grey over green over an older white, the layers curling and flaking, rubbed to bare silvered wood along the top at x=45% where hands have rested for decades; the balusters are chipped at their turnings, two of them replaced with plain sticks; rust bleeds from the brackets down the posts; the cord of the line is grey-green, slackened and frayed, its fibres fuzzed along the sag, a few wooden pegs left clipped to it, one split.

FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND

SHOT 1 [0.0-6.0s] — Medium close along the rail, three-quarter left profile, eye level, camera about 160 cm high and 1.2 m from her, static, locked off, one size tighter than the main version so the frame is filled by her, the rail and the night alone.
[0.0s] Starting positions, held until described otherwise: @Nora at x=45%, filling 82% of frame height, in three-quarter left profile facing the dark rooftops screen-left, both hands on the rail, weight forward, head slightly bowed. Her breath fast and shallow, visible in the cold. Expression: a tired face with two things fighting on it, neither of them named.
[0.0-1.6s] She hesitates — the mouth opens and closes again without a sound; the grip tightens; one breath drawn deeper than the others and held half a second.
[1.6-3.4s] THE LINE, out loud, thrown at the rooftops, louder than she meant it, the voice cracking on the last word: "Why did my mother die?" Her chin comes up on the line; nothing else in her body moves; her hands stay exactly where they are.
[3.4-5.4s] Stillness. Her breath clouds, fast then slower. NOTHING ANSWERS — no voice, no echo, no light changing anywhere in frame, no shape appearing. At [4.4s], very far away, a dog barks twice. Her eyes stay on the rooftops, then close for one full second and open again.
[5.4-6.0s] Held to the end, no further movement: her hands still on the rail, her eyes open again on the rooftops, her breath clouding once more.

SUBJECT LOCK, NORA The exact girl of the reference @Nora — fifteen, long dark brown hair with a coarse natural wave, unwashed, pushed back behind the ears; grey-green eyes with the slight downward outer tilt under thick dark eyebrows; her father's straight nose and slightly squared jaw, her mother's wide mouth; pale olive skin that has lost its colour, chapped bitten lips, heavy lids with grey shadowed hollows beneath, faint freckles across the nose, bitten nails; thin adolescent build, shoulders rounded inward. The dark navy nylon parka with the broken zip pull over the oversized faded charcoal-grey hooded sweatshirt, hood down. No jewellery. Resting expression: flat, exhausted, closed. She never looks at the lens.

CROSS-FRAME RULES One continuous shot — no cut, no reframe, no camera movement of any kind. @BackGallery is the same gallery as its reference Element: same painted rail flaking to bare silvered wood, same rust-streaked brackets, same empty sagging washing line, same rooftops and back yards, same sodium direction from below and behind. The same girl as her reference, exact face and wardrobe, in the same parka over the same hoodie, her hands empty and on the rail throughout. She is the only human being in this generation: no figure, no silhouette and no shadow of anyone else exists anywhere, in any reflection or at any edge of frame. No window, no door and no lit rectangle is in frame at any moment. The washing line is empty in every frame. Nothing red exists anywhere. Nobody looks at the lens. NO INVENTED ACTION: If a body part is not described as moving, it does not move. No gesture, step, head turn, prop interaction or expression change beyond the choreography written above; between described movements every body holds its last described position naturally (breathing, blinking, micro-sway only). CONTINUITY LOCK above and the POSITIVE CONSTRAINTS below apply in full.

CONTINUITY — WHAT MUST NOT DRIFT
Wardrobe, hair, dirt, damage and wear are exactly as the references define them and do not improve, clean themselves up or change between shots. Nobody is better groomed, better lit, better dressed or better rested than in the shot before. Props stay where the prop layout puts them. Weather, time of day and light level do not move inside a sequence. Nobody looks at the lens at any point.

LOCATION @BackGallery — a close section of the rear wooden gallery of a triple-decker at night: the painted wooden rail, grey over green over an older white, the layers flaking to bare silvered wood along the top where hands have rubbed it smooth, on turned balusters, two of them replaced with plain sticks; rust streaks bleeding from the rail brackets down the posts; peeling deck boards below with the grain raised and the nailheads standing proud and rusted; a washing line of grey-green cord sagging through the upper frame, a few wooden pegs left clipped to it, one split, no laundry on it; beyond the rail, soft, the dark back yards and rooftops — asphalt shingles, leaning fences — and the receding rails of the flats above and below screen-right; the cold deep blue sky above, nearly black at the zenith. No red anywhere. No readable text, no lettering, no signage with words, no logos.

LIGHT Two sources only. Sodium street lamps from below and behind, raking their dull orange upward — catching the underside of the rail, the curled paint flakes, the proud rusted nailheads and the bare-wood patches along the top, edging her jaw and shoulder from behind, and lighting her breath into brief clouds. And the cold deep blue of the night sky as a weak top fill on her shoulders. Her face stays in cold half-light, gently underexposed, and the blacks between the sources are truly black. The warm rectangle from the flat below is out of this frame entirely. NO LIGHT ANYWHERE CHANGES AT ANY POINT IN THIS GENERATION. No other source, no fill.

DIALOGUE [1.6-3.4s] @Nora, out loud to the night, thrown at the rooftops, louder than she meant it, the voice cracking on the last word: "Why did my mother die?"

LAST FRAME — THE EXACT STATE THIS SHOT HANDS OVER, because the next shot opens on it
WHAT IS IN THE FRAME AT THE LAST INSTANT: Her three-quarter left profile at the rail, both hands still on the worn bare-wood top, her eyes open again on the dark rooftops, one last cloud of breath in the sodium, the empty washing line sagging above, the night behind her unchanged — nothing has answered.
WHERE THIS SHOT LEAVES EACH BODY, to the number — these are the positions the next shot inherits, whether or not the body is still inside this last frame: @Nora: STANDING, x=45%, filling 82% of frame height.



CHARACTER PERFORMANCE
Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through nothing else: no added expression, no widened eyes, no trembling lip, no theatrical breath. What is not written does not happen. Between the written events every body simply holds its last position, breathing, blinking and drifting a few millimetres, never frozen and never fidgeting.
@Nora is STANDING for the entire generation — she never sits, never crouches, never leans over the rail, never steps away, never turns her back to camera. She wears the dark navy nylon parka with the broken zip pull over the charcoal hoodie, hood down. Both hands are on the rail from [0.0s] to the end, knuckles pale with grip; she holds no object at any point.

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
SFX only. No music. No background music of any kind, no score, no drone, no ambient pad. Night wind, the low tide-hum of the port beneath everything, a loose halyard clinking far off against a mast, her breathing audible and quick; then the line — one voice alone in the night, dry and unamplified, no reverb, no echo, no space added to it — and after it a long true silence with nothing in it but the wind, broken at [4.4s] by a dog barking twice, very far away. No reply of any kind. No door, no window, no voice. No music.

POSITIVE CONSTRAINTS — CHECK EVERY FRAME AGAINST THESE
Every named reference above is matched 100%: same face, same build, same wardrobe, same wear. Nobody is better groomed, better lit, better dressed or better rested than the shot before; wardrobe, hair, dirt, damage and wear do not improve or clean themselves up. Props stay exactly where the prop layout puts them. The light level, the weather and the time of day do not move inside this generation.
The choreography written in the FRAME MAP is the whole performance: no gesture, step, head turn, prop interaction or expression beyond it. Between described movements every body holds its last position naturally, breathing and blinking, never frozen and never fidgeting.
Nobody looks at the lens at any point. Nobody speaks except where DIALOGUE says so.
Every stroke of handwriting anywhere in frame is real handwriting laid out in straight horizontal lines — word-shaped clusters separated by spaces, gathered into sentences and paragraphs — in an invented cursive alphabet whose characters recur again and again the way a real alphabet's do. Unmistakably a script, but no script that exists on earth, and not one word readable in any language: it reads as writing from across the room and as nothing at all up close. Never random scribble, never a scrawl, never abstract mark-making, never decorative squiggles. No signage, no label, no digit, no subtitle, no caption is readable anywhere.
One continuous uncut take at real-time speed, for the exact duration requested. No slow motion, no speed ramp, no added cut.

AVOID
a second person, a man, any figure or silhouette anywhere, a window in frame, a door in frame, a lit rectangle of light in frame, a window lighting up or going dark, a curtain moving, camera movement, camera tilt, camera pan, drift, any red anywhere, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, subjects looking at camera, visible camera rigs, slow motion, rain, thunder, an answering voice, reverb or echo on the voice, an amplified or processed voice, extra people in frame, extra gestures, improvised actions, wandering hands, laundry on the line, warm light on her face, a long written coat, any coated figure, theatrical acting, overacting, screaming, sobbing, rushed movements, uncanny smoothness, plastic skin, beauty filter, CGI look, video-game lighting, frozen characters, statue-like stillness, mannequin pose, freeze-frame stillness, generated music.
```








*⚠ **Réglage de 6B-bis** : Lens Anamorphic **85 mm f/2** (un cran plus serré que 6B), 6 s.
**Comment se monte 6B-bis** : garder `[0.6-6.0s]` — **5,4 s**, qui remplacent tel quel les 5,6 s du fragment ②
de 6B. On perd les deux pas du retour : **rattraper les 0,2 s manquantes sur le fragment ① de 6B** (démarrer à
`[0.8s]` au lieu de `[1.0s]`), et **enchaîner directement sur 6C** — le cut se fait alors sur elle immobile au
rail, ce qui est plus sec mais tient : l'ellipse de l'escalier était déjà dans le cut. ⚠ Si le retour manque
vraiment, reprendre les deux pas dans le shot 1 de 6B, qui les contient déjà à l'envers, et les monter à
l'endroit — c'est le même axe, la même lumière, le même costume.*

---


## VIDÉO 6C — plan 6.3 « L'escalier » *(8 s de rushes → 5 s au montage · Elements : @Nora + @Sam + @NoraBedroom · start frame : LIEU-08 IMAGE 4, le palier, porte entrouverte 10 cm)*
**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 8 s |
| **Éléments** | @Nora + @Sam + @NoraBedroom |
| **`start_image`** | LIEU-08 IMAGE 4, le palier, porte entrouverte 10 cm |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> ⛔ **NE COLLE PAS CE TABLEAU.** Il est pour toi, pas pour le modèle : c'est ce que tu règles
> dans l'interface avant de coller. **Tu ne copies QUE le texte entre les triples backticks
> ci-dessous**, et rien d'autre — pas le titre, pas ce tableau, pas cette ligne.


```
SCENE CONTEXT
A father stands in the dark landing outside his daughter's door, just arrived at the top of the stairs, and asks one quiet question. She answers through the gap without opening it. The door closes. He stays where he is. One single static shot, no cut. Whether he heard anything tonight is never answered — his face is never lit, his expression never readable, and she never asks him anything. Every second is choreographed below; nothing beyond it may be invented. 8 seconds, one continuous framing, no cut.

CONTINUITY REFERENCE — SAME FILM, DIFFERENT PLACE
THE VIDEO ATTACHED TO THIS GENERATION is an earlier shot from the same film (6B), in a different place. Use it ONLY to match the physical rendering — the film stock, the grain structure, the way skin and fabric resolve, the focus behaviour, the highlight roll-off. Do NOT take its light, its palette, its exposure level or its composition: this shot's light comes from its own LOCATION and LIGHT paragraphs below, and its framing from its own FRAME MAP. Everything else is built new, at full quality.

HANDOFF — THE EXACT STATE THIS SHOT INHERITS FROM THE ATTACHED VIDEO
These are NOT new positions to invent. This is the frame the previous shot (6B) ends on, repeated here to the number, and the first frame of this generation must reproduce it exactly before anything moves.
WHAT IS IN THE FRAME AT THE LAST INSTANT: Her back at the gallery rail, already turning away toward the ajar door, both hands off the rail and at her sides, the empty washing line sagging above, the rooftops and the harbour cranes beyond, the warm rectangle unchanged and unremarked at the lower frame edge — nothing in the world has answered.
WHERE THIS SHOT LEAVES EACH BODY, to the number — these are the positions the next shot inherits, whether or not the body is still inside this last frame: @Nora: STANDING, x=45%, filling 72% of frame height.
Nothing in this list may be re-placed, re-lit or improved. Whatever the FRAME MAP below asks for happens AFTER this state, never instead of it.

ACTIVE REFERENCES
@Nora: Nora, fifteen, long dark brown unwashed hair, grey-green eyes, pale olive skin gone colourless, bitten lips, heavy lids over grey hollows, thin build. Running on empty: grief has made her polite and absent — she answers, she says thank you, and none of it reaches her face. She goes very still before anything shows. NOTHING RED ON HER. 100% matches the reference.
@Sam: Sam two years later, a month of badly trimmed beard, ten kilos heavier, grey under the eyes. Two years without speaking — not sullen, emptied. He moves through his own house like a guest, shoulders forward, eyes down and to the side. Every gesture is finished; none is explained. 100% matches the reference.
@NoraBedroom: Nora's bedroom and the landing outside it, grey and underexposed, one narrow sodium band under the door. 100% matches the reference.

TEMPERAMENT, NORA A fifteen-year-old running on empty. Grief has made her polite and absent: she answers, she carries the dish back, she says thank you, and none of it reaches her face. Her body is tired before the day starts. She does not cry in front of people — the swollen eyelids come from somewhere else, earlier. When something does move her, she goes very still first, and only then does it show.
TEMPERAMENT, SAM AFTER Two years without speaking. Not sullen — emptied. He moves through his own house like a guest: slower, heavier, shoulders carried forward, eyes down and to the side. He still does things for his daughter, but wordlessly and out of her sight. Every gesture is finished; none is ever explained. When he is alone his face does what it wants; the moment she is in the room it does nothing at all.

LOCATION MAP
Framing 1 [0.0-8.0s] — camera: Single fixed shot down the landing, eye level, camera about 160 cm high at the top of the stairs, static, locked off. No cut, no reframe, no drift — exactly the axis of the reference angle: the bedroom door screen-right at x=68% ajar ten centimetres, the blade of light lying across the boards toward camera, the stair rail's top post screen-left at x=15%, near-black everywhere else.
Every distance, height and frame position given above is literal and is held exactly; nothing drifts toward a more flattering angle.

FIRST FRAME AND SPATIAL BLOCKING The generation opens on this exact frame: Single fixed shot down the landing, eye level, camera about 160 cm high at the top of the stairs, static, locked off. No cut, no reframe, no drift — exactly the axis of the reference angle: the bedroom door screen-right at x=68% ajar ten centimetres, the blade of light lying across the boards toward camera, the stair rail's top post screen-left at x=15%, near-black everywhere else. Starting positions, held until described otherwise: @Sam a grey silhouette at x=32%, filling 74% of frame height, three-quarter back to camera, facing the lit door gap, arms at his sides, weight even on both feet, the heavy shoulders slightly slumped, the head a fraction forward. The blade of light on the boards does not touch him and never will. In the gap at x=68%: the sliver of @Nora — one eye, part of a pale cheek, dark hair, the navy edge of her collar — her face half turned away. This is the frame the first video frame must already be, before anything moves: nothing is settling into place, nothing fades up, nothing is mid-transition.

FORMAT MODE
One single continuous uncut take, 8 seconds long, at real-time speed. No cut, no montage, no dissolve, no speed ramp, no slow motion.

OPTICS
Anamorphic 50 mm f/2 equivalent. Depth of field wide open at that stop: the plane described in the FRAME MAP is tack sharp and everything behind it falls off progressively. Focus holds on that plane and breathes naturally with the camera's movement — no deliberate rack focus unless the FRAME MAP calls for one.

CONTINUITY LOCK Every prop named in the layout appears in EVERY frame where its surface is visible, in the same position and state — nothing appears, disappears, multiplies or moves unless the choreography says so. Each character's posture (SEATED or STANDING) is stated at the top of the shot and never changes off-screen. Neither character holds any object at any point, and no object may materialise in anyone's hand. THE ONLY THING THAT MOVES IN THIS GENERATION IS THE DOOR, and only when the choreography says so. NO GARMENT IS EVER AN OBJECT IN THIS HOUSE: nothing hangs on any hook, nothing is folded, nothing is laid down, and no long written coat exists anywhere in this generation, in any frame, in any corner.

PROP LAYOUT — FIXED The dark landing at the top of the stairs. @Nora's bedroom door screen-right at x=68%, ajar ten centimetres; through the gap, a vertical sliver of @NoraBedroom — cold blue-white and sodium orange — and the blade of that light across the bare floorboards toward camera. The stair rail's top post screen-left at x=15%, barely separable from the dark. Nothing else is readable in the black: no hook, no coat, no bag, no shoes, no mirror, no glass, no picture, no furniture. Matter and wear, precise: the boards are cupped and gappy where the blade grazes them, worn pale along the walk-line, their nail heads dark and slightly proud; the skirting's paint is bruised at ankle height; the door's paint is thickened by old repaints and chipped around the latch, the latch plate scratched bright around the tongue, the handle tarnished and slightly loose; the rail post's varnish is rubbed dull and slightly sticky from decades of hands.

FRAME MAP & CHOREOGRAPHY — SECOND BY SECOND

SHOT 1 [0.0-8.0s] — Single fixed shot down the landing, eye level, camera about 160 cm high at the top of the stairs, static, locked off. No cut, no reframe, no drift — exactly the axis of the reference angle: the bedroom door screen-right at x=68% ajar ten centimetres, the blade of light lying across the boards toward camera, the stair rail's top post screen-left at x=15%, near-black everywhere else.
[0.0s] Starting positions, held until described otherwise: @Sam a grey silhouette at x=32%, filling 74% of frame height, three-quarter back to camera, facing the lit door gap, arms at his sides, weight even on both feet, the heavy shoulders slightly slumped, the head a fraction forward. The blade of light on the boards does not touch him and never will. In the gap at x=68%: the sliver of @Nora — one eye, part of a pale cheek, dark hair, the navy edge of her collar — her face half turned away.
[0.0-1.5s] Nothing moves. The house settles once, below — a single click of wood. His breathing, slow, lifting the shoulders a few millimetres. Her breath in the gap is a little quicker than his, and nothing in the frame remarks on it.
[1.5-2.4s] @Sam, quiet, low, rusty from disuse, almost swallowed: "You okay?" Only his head lifts one centimetre on the line; the silhouette otherwise holds exactly.
[2.4-3.2s] A beat. In the gap, her eye drops to the boards; her lips part before the answer.
[3.2-4.8s] @Nora, flat, unhurried, through the gap, with a small pause after the first word: "Nothing. I stepped on something." Her face does not come into the gap; her eye does not search his silhouette; nothing on her asks anything.
[4.8-5.4s] A beat. Neither of them moves. The blade of light holds steady on the boards.
[5.4-5.9s] The door closes without slamming — a slow swing and one soft click of the latch. The blade of light narrows, thins, and dies with the click. The landing falls to near-black; his silhouette is now barely separable from the dark.
[5.9-8.0s] He does not move. He does not turn away. He does not go down. Held to the end, no further movement — only his breathing, and the house.

SUBJECT LOCK, SAM The man of the reference @Sam — mid-forties, heavy-set, about ten kilograms past his own frame, the shoulders slumped, the head carried a fraction forward, a month-old untrimmed salt-and-pepper beard, the faded charcoal waffle-knit thermal shirt under the unlined olive-drab canvas work jacket with its torn left cuff, dark navy work trousers worn shiny at the knees, oil-stained tan leather work boots — but rendered ONLY as an unlit grey silhouette for the entire generation: outline, mass and posture, never features. HIS FACE IS NEVER VISIBLE, NEVER LIT, NEVER READABLE, in any frame: no eyes, no cheek, no mouth, no skin, no glint, no rim of light on his profile. He never looks at the lens. He wears no coat of any kind and there is no coat anywhere in this generation.

SUBJECT LOCK, NORA The exact girl of the reference @Nora — fifteen, long dark brown hair with a coarse natural wave, unwashed; grey-green eyes with the slight downward outer tilt under thick dark eyebrows; pale olive skin without colour, chapped bitten lips, heavy lids with grey shadowed hollows beneath — visible ONLY as a vertical sliver in the ten-centimetre gap: one eye, part of a pale cheek, strands of hair, and the dark navy edge of her parka collar, nothing more. She never opens the door wider, never leans out, never fully appears. She asks nothing, says no name, does not repeat herself, does not hesitate over her answer, and her face never carries a question, a doubt or a suspicion of any kind — only the flat closed tiredness of someone ending a conversation. She never looks at the lens.

CROSS-FRAME RULES One continuous shot — no cut, no reframe, no camera movement of any kind. The two people are the exact people of their references. Nothing enters or leaves the frame; nobody else exists on screen — no third figure, no silhouette on the stairs, no shape at the bottom of the stairwell, no shadow of anyone, no reflection of anyone. No second light source ever appears, and no light on any surface changes except the blade of light narrowing and dying with the door. No expression of the father's is ever readable, because no light ever reaches his face — the ambiguity is the point and must survive every single frame. No long written coat and no coated figure exists anywhere in this generation. Nothing red exists anywhere. NO INVENTED ACTION: If a body part is not described as moving, it does not move. No gesture, step, head turn, prop interaction or expression change beyond the choreography written above; between described movements every body holds its last described position naturally (breathing, blinking, micro-sway only). CONTINUITY LOCK above and the POSITIVE CONSTRAINTS below apply in full.

CONTINUITY — WHAT MUST NOT DRIFT
Wardrobe, hair, dirt, damage and wear are exactly as the references define them and do not improve, clean themselves up or change between shots. Nobody is better groomed, better lit, better dressed or better rested than in the shot before. Props stay where the prop layout puts them. Weather, time of day and light level do not move inside a sequence. Nobody looks at the lens at any point.

LOCATION @NoraBedroom, the dark upstairs landing at the top of the stairs — bare floorboards cupped and gappy, worn pale along the walk-line where the blade of light grazes them, their nail heads dark and slightly proud; a chipped scuffed skirting bruised at ankle height; the stair rail's top post screen-left, its varnish rubbed dull and slightly sticky from decades of hands, barely separable from the dark; the bedroom door screen-right, its paint thickened by old repaints and chipped around the latch, the latch plate scratched bright around the tongue, the handle tarnished; through the ten-centimetre gap, a vertical sliver of the bedroom beyond — cold blue-white glow and sodium orange, the cluttered dark room unreadable behind it. Every one of these textures exists only where the blade touches it; everything else stays swallowed in black. Nothing hangs anywhere. No red anywhere. No readable text, no lettering, no signage with words, no logos.

LIGHT One source only: the blade of cold blue and sodium light through the ajar door — hard-edged at the gap, widening and softening as it crosses the boards toward camera, a little dust hanging in it. It never touches the man: it falls between him and the door and dies before it reaches him, so his whole body reads as an unlit grey mass against deeper black. The whole frame is gently underexposed with the blacks truly crushed and the corners gone entirely. When the door closes, the blade narrows in real time with the swing and dies on the click, leaving only the faintest spill under the door and nothing else. No other source, no warm lamp, no moonlight, no fill, no bounce.

DIALOGUE [1.5-2.4s] @Sam, quiet, low, rusty from disuse, almost swallowed: "You okay?" [3.2-4.8s] @Nora, flat, unhurried, through the gap, with a small pause after the first word: "Nothing. I stepped on something."

LAST FRAME — THE EXACT STATE THIS SHOT HANDS OVER, because the next shot opens on it
WHAT IS IN THE FRAME AT THE LAST INSTANT: The near-black landing, the bedroom door shut, the blade of light gone, the father's silhouette motionless at x=32% facing the closed door, arms at his sides, barely separable from the dark, nothing lit anywhere in frame.
WHERE THIS SHOT LEAVES EACH BODY, to the number — these are the positions the next shot inherits, whether or not the body is still inside this last frame: @Sam: STANDING, x=32%, filling 74% of frame height. @Nora: STANDING, x=68%.



CHARACTER PERFORMANCE
Nobody performs an emotion here. The feeling is legible only through the exact physical events written in the choreography above, and through nothing else: no added expression, no widened eyes, no trembling lip, no theatrical breath. What is not written does not happen. Between the written events every body simply holds its last position, breathing, blinking and drifting a few millimetres, never frozen and never fidgeting.
@Sam is STANDING for the entire generation, hands empty at his sides, and never moves from where he stands — he never steps forward, never steps back, never turns away, never reaches for the door, never touches anything. He is rendered ONLY as an unlit grey silhouette: outline and posture, never features, never skin, never eyes. @Nora is STANDING behind the door for the entire generation, visible only as a vertical sliver in the ten-centimetre gap: one eye, part of a cheek, strands of dark hair, and the dark navy edge of her parka collar. She never opens the door wider, never steps into the gap, never leans out.

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
SFX only. No music. No background music of any kind, no score, no drone, no ambient pad. The house settling, one click of wood below at [0.7s], a water pipe ticking somewhere as it cools, the muffled night of the street barely reaching through the walls; his breathing, slow; hers behind the door, a little quicker; the two lines quiet and unhurried with a real silence between them; the slow swing of the door and one soft click of the latch at [5.9s]; then only his breathing and the house. No footsteps. No stairs. No music.

POSITIVE CONSTRAINTS — CHECK EVERY FRAME AGAINST THESE
Every named reference above is matched 100%: same face, same build, same wardrobe, same wear. Nobody is better groomed, better lit, better dressed or better rested than the shot before; wardrobe, hair, dirt, damage and wear do not improve or clean themselves up. Props stay exactly where the prop layout puts them. The light level, the weather and the time of day do not move inside this generation.
The choreography written in the FRAME MAP is the whole performance: no gesture, step, head turn, prop interaction or expression beyond it. Between described movements every body holds its last position naturally, breathing and blinking, never frozen and never fidgeting.
Nobody looks at the lens at any point. Nobody speaks except where DIALOGUE says so.
Every stroke of handwriting anywhere in frame is real handwriting laid out in straight horizontal lines — word-shaped clusters separated by spaces, gathered into sentences and paragraphs — in an invented cursive alphabet whose characters recur again and again the way a real alphabet's do. Unmistakably a script, but no script that exists on earth, and not one word readable in any language: it reads as writing from across the room and as nothing at all up close. Never random scribble, never a scrawl, never abstract mark-making, never decorative squiggles. No signage, no label, no digit, no subtitle, no caption is readable anywhere.
One continuous uncut take at real-time speed, for the exact duration requested. No slow motion, no speed ramp, no added cut.

AVOID
the man's face visible, the man's eyes, the man's profile lit, any light on the man's face or body, a rim of light on his cheek, a readable expression on the man, the man stepping forward, the man reaching for the door, the man turning away, the man going down the stairs, the door slamming, the door reopening, the girl opening the door wider, the girl leaning out, the girl fully visible, the girl asking a question, the girl saying a name, the girl frowning, a doubtful or suspicious look, a third person, a silhouette on the stairs, a shape at the bottom of the stairwell, a long written coat, any coated figure, a coat on a hook, any red anywhere, a second light source, a lamp switching on, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, subjects looking at camera, visible camera rigs, camera movement, dolly, pan, zoom, handheld shake, slow motion, morphing objects, extra people in frame, extra gestures, improvised actions, wandering hands, repositioned props, appearing or disappearing objects, footsteps walking away, hurried dialogue, characters answering instantly, theatrical acting, overacting, warm lamps, uncanny smoothness, plastic skin, beauty filter, CGI look, video-game lighting, frozen characters, statue-like stillness, mannequin pose, freeze-frame stillness, generated music.
```








*⚠ **POINT DE COUPE — le plan fait 5 s au montage, la génération en fait 8.** Garder **`[1.2s]` → `[6.2s]`** :
0,3 s de silence avant la question, les deux répliques avec leur vrai temps entre elles, le battement d'après,
la porte qui se referme, et **0,3 s de presque-noir avec lui dedans**. C'est tout le plan.
**RÉSERVE** : `[6.2-8.0s]` — il reste seul dans le noir. Elle n'entre que si l'attaque de la séquence 7 paraît
trop brutale ; le script veut au contraire un enchaînement sec.
⚠ **Ne pas garder au-delà de `[7.0s]`** : plus le plan dure sur lui, plus le spectateur cherche une réponse à
« a-t-il entendu ? » — et le film ne la donne pas ici.*

*⚠ **LE VERROU DE VOIX — la raison pour laquelle ce plan ne se coupe pas.** « You okay? » est **la seule
réplique de Sam dans tout le présent du film** : il ne parle ni en séq. 5, ni en 7, ni en 8, et en séq. 10 c'est
Maeve qu'on entend. **C'est donc le seul échantillon dont l'oreille dispose pour reconnaître la voix du SDF en
9.2** (règle F : la voix du SDF est celle de Sam, une tierce plus bas, cassée par le froid). La prise doit
sortir **basse, râpeuse, rouillée par le silence** — pas chuchotée, pas douce : une voix qui ne sert plus.
Archiver le fichier son de cette réplique : c'est la référence de tonalité à donner au prompt de 9.2.*

*⚠ **RÈGLE ZÉRO, contrôle à faire sur le rush avant de valider** : dans la fenêtre `[3.2-5.4s]`, son œil dans
l'entrebâillement ne doit **jamais chercher le visage de son père**, ne jamais s'attarder, ne jamais se plisser.
Elle répond et elle referme. S'il existe un seul frame où elle regarde la silhouette autrement que pour ne pas
la regarder, la prise est à jeter — c'est ce frame-là qui casserait le film.*

*⚠ **LE DÉTAIL QUI NE SE SOULIGNE JAMAIS** : le col de sa parka dans l'entrebâillement, et son souffle un peu
court. Elle rentre du dehors, elle vient de crier dans la nuit — **et personne dans le cadre ne le remarque.**
Aucun insert, aucun temps d'arrêt, aucune inflexion. Le spectateur ne doit pas le voir la première fois.*

---

## RÉCAPITULATIF DE GÉNÉRATION

| Bloc | Plan | Lieu / start frame | Objectif | Rushes | Montage |
|---|---|---|---|---|---|
| **6A** | 6.1 — le forum | @NoraBedroom · LIEU-08 IMAGE 3 | **la plaque du rituel**, et le regard qui se lève | 12 s | 7 s |
| **6B** | 6.2 — le cri | @BackGallery · LIEU-09 IMAGE 2 (+ IMAGE 3) | la question posée à la nuit, et rien qui répond | 12 s | 9 s |
| **6C** | 6.3 — l'escalier | @NoraBedroom · LIEU-08 IMAGE 4 | il était là, réveillé, à minuit — **et on n'en saura pas plus** | 8 s | 5 s |
| *(6A-bis)* | *secours 6.1* | *@NoraBedroom · LIEU-08 IMAGE 3* | *l'écran seul, sans elle : une plaque propre pour le POST* | *6 s* | *remplace ② de 6A* |
| *(6B-bis)* | *secours 6.2* | *@BackGallery · LIEU-09 IMAGE 3* | *le cri, serré, aucune fenêtre ne peut entrer au cadre* | *6 s* | *remplace ② de 6B* |

**Total : 3 générations obligatoires · 32 s de rushes → 21 s au montage.** Les deux blocs de secours ne se
lancent que sur panne constatée ; ils sont écrits en entier ci-dessus, prêts à copier-coller, **jamais par
renvoi** — aucun n'oblige à reconstruire quoi que ce soit à la main.

**Ordre de génération conseillé** : **6A d'abord** (c'est le seul plan du film qui a une dépendance POST sur
cette séquence, et le seul dont l'échec bloque le montage — s'il faut basculer sur 6A-bis, autant le savoir
tôt), puis **6C** (la réplique de Sam est un plant sonore pour la séquence 9 : il faut le fichier son avant de
prompter 9.2), puis 6B (le plus sûr des trois : une fille seule, caméra fixe, une réplique).

**[POST] de la séquence** : un seul élément — la page du forum, en **deux états** composés sur la plaque du
shot 2 de 6A, calés sur le scroll de `[5.8-6.4s]`. Textes verbatim en tête de document. **Aucun autre texte,
nulle part, dans aucun des cinq blocs.**

---

## ⚠ CE QUI PEUT RATER

**6A — des caractères sur l'écran *(le risque n°1 de la séquence)*.**
Le modèle veut écrire. Dès qu'il pose une lettre, un chiffre, une icône, un curseur ou une barre de menu sur la
plaque, **la prise est inutilisable telle quelle** (règle G) et le POST ne peut plus se caler dessus : on ne
compose pas un rituel par-dessus des mots générés. **Plan B** : la génération **6A-bis**, écrite en entier
après le bloc — l'écran seul, sans elle, plus près, sans le moindre corps dans le cadre. Si même là il écrit,
**troisième recours** : sortir l'écran du plan et **monter la page en insert graphique pur**, plein cadre,
composé de bout en bout en post ; on perd le raccord physique à la chambre, on garde le rituel — mais c'est le
dernier recours, parce qu'un insert sans la pièce autour casse le monde gris pendant 4 s.

**6A — l'écran net *(un écart, pas une erreur)*.** Le document du lieu et l'ancienne version de ce bloc
demandaient un écran **flou**. Ici il est **net et vierge**, exprès. Ne pas « corriger » ce point en croyant
rétablir la continuité : du texte composé sur un flou ne tient pas à 2,2 s, et ce plan porte le rituel.
Le flou reste la règle partout ailleurs dans le film (7A plan 3).

**6A — la durée du rituel.** L'ÉTAT B doit tenir **au moins 2,2 s pleines à l'écran**. Toute fenêtre de montage
qui démarre après `[6.4s]` ou finit avant `[8.6s]` vole du rituel — et le rituel est la seule raison d'être du
plan depuis l'épure du 31/08. Si le rush ne donne pas 2,2 s stables après le scroll, régénérer : c'est moins
cher qu'un spectateur qui n'a pas lu la phrase qui déclenche 6.2.

**6A — le scroll multiple.** Le modèle a tendance à faire défiler en continu. **Un seul scroll, et il est le
raccord des deux états.** Deux scrolls, et le POST n'a plus de point de calage ; un scroll continu, et il n'en
a plus du tout. Contrôler image par image `[4.0-9.0s]` avant de valider.

**6B — quelque chose répond.** C'est le seul risque qui touche au sens. Une fenêtre qui s'allume, un carreau
cadré de face, une silhouette au fond d'une cour, un écho sur la voix : **le monde a répondu, et le film n'a
plus d'histoire.** Contrôler les trois points de la note de coupe avant toute chose. **Plan B** : la génération
**6B-bis**, écrite en entier après le bloc — cadre serré au rail, où **aucune fenêtre, aucune porte et aucun
lit rectangle de lumière ne peut physiquement entrer**. C'est le repli le plus sûr du document.

**6B — le cri sur-joué.** Le piège est un hurlement, des sanglots, un menton qui tremble. Le script écrit
« elle serre la rambarde, hésite, puis », pas une crise. La voix casse **sur le dernier mot seulement**, et le
corps ne bouge pas. Si le rush est théâtral, régénérer sans rien changer d'autre que la SUBJECT LOCK —
*flat, exhausted, closed*.

**6B — l'écho.** Un modèle « aide » volontiers un cri lancé dehors en lui ajoutant de la réverbération. Ici
c'est interdit : le cri doit tomber à plat, sec, dans une nuit qui ne renvoie rien. Le NEGATIVE PROMPT le porte
deux fois ; si le rush revient réverbéré, la piste voix est à refaire — ne pas essayer de la désreverbérer.

**6C — le visage de Sam éclairé.** La lame de lumière est censée mourir avant lui. Le modèle peut la faire
courir jusqu'à ses pieds, poser un liseré sur sa joue, ou simplement le déboucher. **Un seul frame où son
expression se lit et le plan perd son sujet** — l'ambiguïté est tout ce qu'il a. **Plan B sans nouvelle
génération** : relancer 6C en remplaçant les trois lignes de cadre par celles-ci, ce qui met la caméra de
**l'autre côté de la porte**, dans la chambre, d'où il est structurellement impossible d'éclairer son visage :
> `SHOT 1 [0.0-8.0s]` — Single fixed shot from INSIDE the bedroom, eye level, camera about 150 cm high, one metre back from the door, static, locked off, looking out through the ten-centimetre gap: @Nora's shoulder and the back of her head cutting the near left frame edge as a dark mass at x=22%, the door's inner face and its tarnished handle at x=40%, and beyond the gap at x=58% a vertical slice of the near-black landing with, in it, nothing but a grey unlit mass where the man stands.
> `[0.0s]` Starting positions, held until described otherwise: the room's cold blue-white glow and its sodium orange fall on her shoulder and on the door's inner face and go no further; through the gap, the landing is a vertical band of near-black, and @Sam is an unlit grey mass filling 60% of that band's height, three-quarter to the gap, arms at his sides, no feature of any kind resolving.
> `[5.4-5.9s]` Her hand comes into frame at x=34% and pushes the door shut without slamming — a slow swing and one soft click. The vertical band of landing narrows, thins, and is gone with the click. The room's own light stays exactly as it was.
> *(⚠ Dans cette variante, `[5.9-8.0s]` tient sur la face intérieure de la porte fermée et sur son épaule immobile ; la réserve de montage devient `[6.2-7.4s]`. Adapter LAST FRAME en conséquence : « The inner face of the closed bedroom door, its tarnished handle, @Nora's shoulder and the back of her head motionless at the near frame edge, the room's cold light unchanged on both. » **Le reste du bloc se copie sans une modification** — les verrous, la règle ZÉRO et les deux répliques sont identiques.)*

**6C — RÈGLE ZÉRO.** Le vrai danger n'est pas technique. Si le rush contient **un seul frame** où son œil dans
l'entrebâillement cherche le visage de son père, s'attarde, se plisse, ou si elle ouvre la bouche pour ajouter
quelque chose, **la prise est à jeter** : ce frame-là fabrique un soupçon, et le film entier repose sur le fait
qu'il n'y en a aucun. Contrôler image par image la fenêtre `[3.2-5.4s]` avant de valider.

**6C — la voix de Sam.** Trop douce, trop claire, trop « papa », et 9.2 n'a plus de référence à quoi répondre.
Elle doit sortir **basse, râpeuse, rouillée** — une voix qui ne sert plus depuis deux ans. C'est le seul
échantillon du film. Si elle est jolie, la prise est à refaire même si tout le reste est bon.

**6C — la porte qui claque.** Un claquement transforme la réponse en refus, et le plan raconte alors une
dispute que le film n'a pas. Battant lent, **un seul déclic doux**, et la lame qui meurt avec.

**Toute la séquence — le rouge.** Trois pièges concrets : une diode de chargeur sous le bureau (6A), un feu
arrière ou une enseigne au fond des toits (6B), un voyant quelconque sur le palier (6C). Nous sommes à quatre
séquences de la maison rouge, qui doit être **le premier rouge plein cadre du film** : vérifier chaque passe
image par image, et au moindre doute désaturer en post plutôt que de garder un rush douteux.

---

## ⚠ DÉPENDANCES À CORRIGER AILLEURS *(à faire avant de composer le POST, sinon on compose l'ancienne version)*

1. **Le contenu du forum.** `docs/generations/GEN-SEQ-06.md` §[POST] porte encore **trois brèves** (la troisième
   est *« He asked my sister to sing. »*) et **la loi en gras** (*« He asks before he gives. Whatever he asks
   for, give it. »*). **Les deux sont supprimés par l'épure du 31/08** : deux brèves, pas de loi, le rituel.
   Tant que ces deux lignes n'ont pas sauté, quiconque compose le POST à partir de ce fichier remet la loi à
   l'écran deux plans après que les trois femmes viennent de la dire.
2. **La durée.** Le même fichier annonce la séquence en trois générations de 12 + 12 + 8 s pour **~32 s de
   film** ; elle en fait désormais **21** (7 + 9 + 5). Les rushes, eux, ne changent pas — ce sont les points de
   coupe de ce document qui font foi.
3. **Le renvoi de 6.2.** `docs/SCRIPT-THE-MENDER.md` plan 6.2 dit encore « la vérité est en **11.3b** », et
   `LIEU-09-BackGallery.md` parle d'un « contrechamp caché **11.1b** » où Sam entend le cri depuis la cuisine
   du dessous. **Ces deux renvois pointent la numérotation à 11 séquences, qui n'existe plus.** Dans le film
   épuré, le montage muet est **10.9**, et **aucun de ses huit plans ne montre Sam entendant le cri** : la
   révélation de 6.2 est portée par **10.9a** (le contrechamp du cadre de 4.1 — « il a tout entendu, depuis le
   début »). ⚠ **À trancher par David** : corriger les deux renvois vers 10.9a, ou réintroduire le contrechamp
   cuisine dans le montage muet. **Quoi qu'il décide, la discipline de 6B ne change pas** — rectangle chaud
   jamais souligné, aucune silhouette dans aucune fenêtre : elle ne coûte rien et c'est elle qui laisse les
   deux options ouvertes.
4. **L'écran net.** `LIEU-08-NoraBedroom.md` note que « 6A et 7A plan 3 [veulent le laptop] OUVERT (écart
   délibéré déclaré dans leurs prompts, **écran toujours flou**) ». À amender pour 6A seulement : **le shot 2
   veut l'écran NET et vierge de caractères**, c'est la plaque du POST. 7A plan 3 garde le flou.
5. **Le fichier son de « You okay? »** (6C). À archiver et à nommer explicitement dans `VIDEO-SEQ-09.md` comme
   référence de tonalité de la voix du SDF (règle F). Sans lui, 9.2 se prompte à l'aveugle.

--- FIN ---
