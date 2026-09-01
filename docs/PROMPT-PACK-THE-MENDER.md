# THE MENDER — Prompt Pack (méthode 5 niveaux, niveau 5)

> Adapté du *Prompt Pack — 5 Levels of AI Video Prompting* de Youri van Hofwegen.
> **On travaille directement au niveau 5** : on ne décrit pas un type de personnage, on donne au
> modèle **une instance**, la même personne dans chaque plan, via des Éléments sauvegardés.
> Ce fichier **remplace** `PERSONNAGES-PROMPTS.md` (format split-screen sur blanc, abandonné).

## Ce que le pack change chez nous — cinq points

**① Fiche à trois panneaux sur gris moyen, pas split-screen sur blanc.** Et surtout : **le panneau de
face est SANS TÊTE**, volontairement. Le col tient sa forme et s'ouvre sur un creux sombre, comme
porté par un invisible. Raison : **le modèle n'a alors qu'UN seul visage à copier** — celui du
panneau de droite — au lieu d'en moyenner deux. C'est le geste qui fait tenir l'identité.

**② Les garde-robes sont des fiches séparées, dérivées de la fiche de base.** Un visage → plusieurs
`@tags`. Chez nous c'est décisif : **Sam donne quatre tags** — l'homme d'avant, l'homme d'après,
le SDF, le Mender. Un seul visage verrouillé, quatre apparences.

**③ Les décors sont des Éléments générés VIDES.** « completely empty, no people, no figures, no
subject. » On y fait entrer les personnages ensuite. Fini les décors qui changent entre deux plans.

**④ En Cinema Studio, genre / style / caméra / objectif / focale / diaphragme sont de VRAIS
réglages que le modèle doit obéir** — pas une prière dans le prompt. C'est là que le niveau 3
échouait : « le premier truc que le modèle laisse tomber, c'est l'objectif. »

**⑤ Le bloc de plan a huit sections obligatoires** : FRAME MAP (positions en x=% et en % de hauteur
d'image), SUBJECT LOCK, CROSS-FRAME RULES, LOCATION, LIGHT, MOVEMENT avec HARD CUT, CAMERA,
LAST FRAME, AUDIO, NEGATIVE PROMPT. Et une règle d'or reprise telle quelle : **ne jamais écrire une
émotion, écrire ce qu'elle fait au corps.** « Le modèle ne sait pas rendre le mot *tendu*. »

---

# 1. LES FICHES PERSONNAGES
*GPT Image 2, 4K. Générer, puis **sauvegarder chaque fiche en Élément** sous son tag.*

## Gabarit à trois panneaux (invariant, recopié mot pour mot)

> A three-panel character reference sheet, evenly spaced left to right, separated by thin vertical dividers, on a plain mid-grey seamless studio background.
> **Panel one, left:** a headless full-body front view. The body stands straight, arms relaxed at the sides, feet shoulder width apart. There is no head and no neck, **{LE COL}** holds its own shape and the opening reads as an empty dark hollow looking down into the garment, as if an invisible person is wearing it. The collar edge is crisp and complete. No fade, no blur, no ghosting, no stump, no wound.
> **Panel two, centre:** the same body full length seen from directly behind, standing straight, arms relaxed at the sides. Head and hair present, **{CHEVEUX}**, facing away from camera.
> **Panel three, right:** the same person chest-up, front on, looking directly forward, neutral expression, mouth closed.
> **{LA PERSONNE}** · **Wardrobe, identical in all three panels: {GARDE-ROBE}**
> Flat even studio lighting, shadowless, no cast shadows on the background, identical lighting across all three panels. Photographic, shot on a real camera, sharp focus, visible skin pores and fabric weave, no CGI.

**Queue commune à toutes les fiches :** *no red anywhere in the wardrobe* (sauf @Maeve et @Mender) ·
*original character, not resembling any real person* · *no text, no watermark, no logos.*

---

## @SamBefore — **fiche de base** (l'homme d'avant, séq. 1-4)
*C'est désormais la fiche pivot : le visage propre que le modèle copie. Toutes les variantes en dérivent.*

A three-panel character reference sheet, evenly spaced left to right, separated by thin vertical dividers, on a plain mid-grey seamless studio background.
Panel one, left: a headless full-body front view. The body stands straight, arms relaxed at the sides, feet shoulder width apart. There is no head and no neck, the soft grey marl sweatshirt's collar holds its own round shape and the opening reads as an empty dark hollow looking down into the shirt, as if an invisible person is wearing it. The collar edge is crisp and complete. No fade, no blur, no ghosting, no stump, no wound.
Panel two, centre: the same body full length seen from directly behind, standing straight, arms relaxed at the sides. Head and hair present, short neatly-kept dark brown hair with the first grey at the temples, facing away from camera.
Panel three, right: the same man chest-up, front on, looking directly forward, neutral expression, mouth closed.
The man: forty-eight, of Scots-Irish New England fishing stock, tall and solidly built with broad shoulders and a strong chest, carrying himself upright and easy. Weathered ruddy-tan skin from years of sea wind. A broad rectangular face with a heavy defined jaw and a strong chin, full cheeks with deep smile lines, a broad straight nose, a wide mouth with thin lips quick to a half-smile. Mature adult bone structure. Pale grey-blue eyes, striking against the weathered skin, with warm creases at the corners, naturally muted catchlights, no oversized specular glare in the iris, eye colour muted rather than glowing. Thick dark brown eyebrows. A short neat salt-and-pepper beard, more pepper than salt, trimmed close to the jaw. Large strong hands, clean, no ink.
Wardrobe, identical in all three panels: a soft grey marl sweatshirt with the sleeves pushed to the forearm, dark blue jeans worn at the knee, thick oatmeal wool socks, no shoes, a thin worn steel wedding band on the left ring finger.
Flat even studio lighting, shadowless, no cast shadows on the background, identical lighting across all three panels. Photographic, shot on a real camera, sharp focus, visible skin pores and fabric weave, no CGI. No red anywhere in the wardrobe. Original character, not resembling any real person or any celebrity. No text, no watermark, no logos.

## @Sam — deux ans après (le présent, séq. 5-19) ⟵ *(fiche @SamBefore en référence)*

A three-panel character reference sheet of the exact same man as the reference image — same face, same bone structure, same pale grey-blue eyes, same hair colour — changed only as follows, two years after losing his wife: a beard left untrimmed for about a month, scruffy and uneven, salt-and-pepper, clearly neglected but still short; about ten kilograms heavier, a little fuller in the face and around the waist, the jaw softened but still visible; light shadows under the eyes, subtle, not dramatic; and above all a quiet sadness in the whole bearing — the shoulders slightly slumped, the gaze low, the corners of the mouth fallen, a tired beaten air. Nothing else about him changes. Same three panels as the reference: headless full-body front view (the charcoal thermal shirt's collar holding its own round shape, an empty dark hollow, crisp edge, no fade, no blur, no ghosting, no stump, no wound), full rear view with the hair present, chest-up front portrait with neutral expression and mouth closed. Same plain mid-grey seamless studio background, same thin vertical dividers.
The hands: the same hands, now with cracked skin and the fingertips and nail beds of both hands stained dark blue-black with ink.
Wardrobe, identical in all three panels: a faded charcoal waffle-knit thermal shirt under an unlined olive-drab canvas work jacket with a torn left cuff and salt-bleached shoulders, dark navy work trousers worn shiny at the knees, a scuffed brown leather belt, oil-stained tan leather work boots, the same thin worn steel wedding band.
Flat even studio lighting, shadowless, no cast shadows on the background, identical lighting across all three panels. Photographic, shot on a real camera, sharp focus, visible skin pores and fabric weave, no CGI. No red anywhere in the wardrobe. Original character, not resembling any real person or any celebrity. No text, no watermark, no logos.

## @SamSDF — le déguisement ⟵ *(fiche @Sam en référence — AUCUNE barbe postiche)*
*Le SDF porte la vraie barbe de Sam, salie et hérissée. Le déguisement n'est que bonnet, capuche, crasse, couches et posture.*

A three-panel character reference sheet of the same heavy grey-bearded man from the reference image, keeping his exact face, his month-old scruffy salt-and-pepper beard, his weight and his pale grey-blue eyes — now living rough: the same beard dirtied, matted and made to read fuller and older, a grey film of grime worked into the temples, the neck and the hairline, wind-cracked lips, broken capillaries across the cheekbones, and a stretched dark grey wool beanie pulled low to the eyebrows. Evenly spaced left to right, separated by thin vertical dividers, on a plain mid-grey seamless studio background.
Panel one, left: a headless full-body front view. The body stands straight, arms relaxed at the sides, feet shoulder width apart. There is no head and no neck, the layered flannel collars hold their own shape and the opening reads as an empty dark hollow looking down into the shirts, as if an invisible person is wearing it. The collar edge is crisp and complete. No fade, no blur, no ghosting, no stump, no wound.
Panel two, centre: the same body full length seen from directly behind, standing straight, arms relaxed at the sides, the beanie on, matted grey curls escaping at the nape, facing away from camera.
Panel three, right: the same man chest-up, front on, looking directly forward, neutral expression, mouth closed, the beanie low, the grime and the matted beard doing the rest.
The hands: fingerless grey wool gloves worn through at the tips, grease dirt on the backs of the hands — never on the fingertips, where the dark blue-black ink stains of the reference remain visible.
Wardrobe, identical in all three panels: a filthy oatmeal thermal shirt under two open flannel shirts in faded brown and washed-out blue check, over them a torn olive parka with the stuffing showing at the left shoulder and no zip, baggy stained dark trousers held with a length of rope, mismatched boots, one taped at the toe.
Flat even studio lighting, shadowless, no cast shadows on the background, identical lighting across all three panels. Photographic, shot on a real camera, sharp focus, visible skin pores and fabric weave, no CGI. No red anywhere in the wardrobe. No text, no watermark, no logos.

## @Mender — variante garde-robe, **sans aucun visage** *(fiche @Sam en référence)*
> **RÉGÉNÉRÉE LE 01/09 — job `9b668d28-9509-4ab7-80a5-5ebb08927b76`** *(GPT Image 2 · 4K · high · 16:9 ·
> référence = la fiche @Sam)*. **Motif : l'écriture du dos sortait en gribouillages** — le prompt disait
> *« dense but abstract »*. Corrigé : de l'écriture (lignes, mots, alphabet inventé dont les caractères
> reviennent), illisible parce que l'alphabet est inconnu. **⚠ Élément `mender` à remplacer par cette image.**
*Le seul tag dont les trois panneaux sont sans visage — c'est la loi du film.*

A three-panel costume reference sheet of the same tall broad-shouldered man from the reference image, entirely enveloped so that **no part of his face is visible in any panel**. Evenly spaced left to right, separated by thin vertical dividers, on a plain mid-grey seamless studio background.
Panel one, left: a headless full-body front view. The body stands straight, arms relaxed at the sides, feet shoulder width apart. There is no head and no neck, the high stiff standing collar of the coat holds its own shape and the opening reads as an empty dark hollow looking down into the coat, as if an invisible person is wearing it. The collar edge is crisp and complete. No fade, no blur, no ghosting, no stump, no wound.
Panel two, centre: **the money panel** — the same body full length seen from directly behind, standing straight, arms relaxed at the sides, the deep oilskin hood drawn up so the head is completely lost in shadow, the whole back of the coat filling the panel.
Panel three, right: the same figure from behind at three-quarter rear angle, chest-up crop, hood up, **the face never visible, not even in profile.**
The coat, identical in all three panels: a long mid-calf oilskin sea coat in deep dried-blood red, heavy weather-beaten waxed canvas with a dull waxen sheen and salt bloom at the hem. The whole back is densely covered from collar to hem in thousands of lines of handwritten script in ivory, some lines matte ink and some raised in embroidered ivory thread that catches the light so the back seems to ripple. IT IS REAL HANDWRITING AND MUST READ AS SUCH: straight horizontal lines running the full width of the back, one beneath another from collar to hem, evenly spaced, the strokes gathering into word-shaped clusters clearly separated by spaces and running on into sentences — written in an invented cursive alphabet whose characters recur again and again the way a real alphabet's do. Unmistakably a script, but no script that exists on earth, and not one word readable in any language. Never random scribble, never a scrawl, never abstract mark-making, never decorative squiggles: every stroke belongs to a character, every character to a word, every word sits on its line. Patches of other cloth are sewn in over the years — a triangle of grey sailcloth at the shoulder blade, a strip of woven textile at the flank, a square of mended fishing net at the elbow — with visible hand stitching in mismatched thread throughout. Dark heavy deck boots below. No visible hands in the reference sheet.
**⚠ Exception plan 13.3 (bibliothèque)** : une main nue pend le long du manteau — sale, les doigts tachés d'encre noire jusqu'à la deuxième phalange. Générée d'après le plan macro des mains de @Sam. C'est le plant que presque personne ne verra au premier visionnage : le père a les mains sales, le Mender aussi.
Flat even studio lighting, shadowless, no cast shadows on the background, identical lighting across all three panels, raking very slightly from the left so the embroidered lines catch. Photographic, shot on a real camera, sharp focus, visible fabric weave, wax cracking, wear and repair, no CGI.
**No face, no front view of a face, no profile showing the face, no eyes, no skin visible anywhere. No legible text, no readable words, no letters that form real words.** No text overlay, no watermark, no logos.

## @Maeve — la mère *(37 ans, acte I)*
A three-panel character reference sheet, evenly spaced left to right, separated by thin vertical dividers, on a plain mid-grey seamless studio background.
Panel one, left: a headless full-body front view. The body stands straight, arms relaxed at the sides, feet shoulder width apart. There is no head and no neck, the oatmeal cable-knit sweater's collar holds its own round shape and the opening reads as an empty dark hollow looking down into the sweater, as if an invisible person is wearing it. The collar edge is crisp and complete. No fade, no blur, no ghosting, no stump, no wound.
Panel two, centre: the same body full length seen from directly behind, standing straight, arms relaxed at the sides. Head and hair present, shoulder-length dark auburn hair with a natural loose wave, facing away from camera.
Panel three, right: the same woman chest-up, front on, looking directly forward, neutral expression, mouth closed.
The woman: thirty-seven, of Irish American descent, slim, medium height, narrow shoulders. Fair skin that freckles rather than tans, with scattered faint freckles across the nose and cheekbones and uneven natural tone along the jaw. An oval face with a softly defined jaw, wide cheekbones, a small straight nose, a wide mouth with a thin upper lip and a fuller lower lip. Grey-green eyes with a slight downward outer tilt and fine laugh lines at the corners. Soft mid-brown eyebrows. No makeup beyond a faint natural flush.
Wardrobe, identical in all three panels: a soft oatmeal cable-knit sweater with the sleeves pushed to the elbow, a plain dark grey long skirt, thick grey wool socks, **a deep crimson-red long wool scarf loosely wound over the shoulders**, a thin gold wedding band. Barefoot.
Flat even studio lighting, shadowless, no cast shadows on the background, identical lighting across all three panels. Photographic, shot on a real camera, sharp focus, visible skin pores and fabric weave, no CGI. Original character, not resembling any real person. No text, no watermark, no logos.

## @MaeveIll — variante *(hôpital, 40 ans — fiche @Maeve en référence)*
A three-panel character reference sheet of the same woman from the reference image, keeping her exact face, the grey-green eyes, the freckles across the nose and the dark auburn hair — **now three years later and gravely ill: gaunt hollowed cheeks, sharpened cheekbones and temples, a grey-tinged pallor, dry cracked lips, hair thinned and dull.** Same three panels, same headless front view, same rear view, same chest-up portrait, same mid-grey seamless background, same thin dividers.
Wardrobe, identical in all three panels: a plain pale-blue hospital gown, **the same deep crimson-red wool scarf draped over the shoulders**, an IV cannula taped to the back of the left hand.
Flat even studio lighting, shadowless, no cast shadows, identical across all three panels. Photographic, sharp focus, visible skin pores, no CGI. No text, no watermark, no logos.

## @Nora — 15 ans *(⟵ générer avec DEUX images de référence : la fiche @SamBefore ET la fiche @Maeve)*
A three-panel character reference sheet of an original fifteen year old girl who is unmistakably THE DAUGHTER OF THE TWO PEOPLE IN THE REFERENCE IMAGES — the man and the woman are her father and mother, and her face blends both: her father's straight nose and slightly squared jaw, her mother's wide mouth with the thin upper lip and fuller lower lip, and her mother's grey-green eyes with the slight downward outer tilt, under her father's thick dark eyebrows. Long dark brown hair with a coarse natural wave, unwashed, pushed back behind the ears or half-tied with a plain black elastic, no product, matte finish. She is a distinct original person, not a copy of either parent. Evenly spaced panels left to right, separated by thin vertical dividers, on a plain mid-grey seamless studio background.
Panel one, left: a headless full-body front view. The body stands straight, arms relaxed at the sides, feet shoulder width apart. There is no head and no neck, the oversized hooded sweatshirt's collar holds its own round shape and the opening reads as an empty dark hollow looking down into it, as if an invisible person is wearing it. The collar edge is crisp and complete. No fade, no blur, no ghosting, no stump, no wound.
Panel two, centre: the same body full length seen from directly behind, standing straight, arms relaxed at the sides, the long dark wavy hair present, facing away from camera.
Panel three, right: the same girl chest-up, front on, looking directly forward, neutral expression, mouth closed.
Her state: pale olive skin that has lost its colour, adolescent bone structure not yet fully set, chapped bitten lips with no colour, heavy lids with grey shadowed hollows beneath, a flat unfocused gaze, a scatter of small blemishes along the jaw and forehead, faint freckles across the nose like her mother's, dry patches at the nostrils, no makeup. Thin adolescent build, slightly too thin, shoulders rounded inward.
Wardrobe, identical in all three panels: an oversized faded charcoal-grey hooded sweatshirt with worn cuffs, a dark navy nylon parka with a broken zip pull, straight-leg dark indigo jeans frayed at the hem, grey wool socks, scuffed off-white canvas sneakers. No jewellery.
Flat even studio lighting, shadowless, no cast shadows on the background, identical lighting across all three panels. Photographic, shot on a real camera, sharp focus, visible skin pores and fabric weave, no CGI. No red anywhere in the wardrobe. No glamorous styling. Original character, not resembling any real person. No text, no watermark, no logos.

## @NoraBefore — variante *(acte I, 13 ans — fiche @Nora en référence)*
A three-panel character reference sheet of the same girl from the reference image, keeping her exact face — the grey-green eyes with the slight downward tilt, her father's straight nose and slightly squared jaw, her mother's wide mouth, the thick dark eyebrows, the faint freckles — **but two years younger, thirteen, and visibly, radiantly happy: clear healthy skin with colour in the cheeks, bright open eyes with no shadows beneath, lips soft and unbitten with natural colour, hair shorter to the shoulders, washed and shiny, loose, the shoulders open and easy, a smile always half-arrived at the corner of the mouth.** She is the same person as the reference, before anything happened to her. Same three panels: headless full-body front view (the collar holding its own round shape, an empty dark hollow, crisp edge, no fade, no blur, no ghosting, no stump, no wound), full rear view with the hair present, chest-up front portrait, neutral-warm expression, mouth closed. Same mid-grey seamless background, same thin dividers.
Wardrobe, identical in all three panels: a soft mustard-and-cream striped long-sleeve top, a denim skirt over navy leggings, white socks, the same scuffed off-white canvas sneakers newer and cleaner. No jewellery.
Flat even studio lighting, shadowless, identical across all three panels. Photographic, shot on a real camera, sharp focus, visible skin pores and fabric weave, no CGI. No red anywhere. No glamorous styling. No text, no watermark, no logos.


## @Milo — le petit frère, 8 ans *(⟵ générer avec DEUX images de référence : la fiche @SamBefore ET la fiche @Maeve — puis la fiche @Nora en troisième référence si l'outil l'accepte, pour verrouiller la fratrie)*
A three-panel character reference sheet of an original eight year old boy who is unmistakably THE SON OF THE TWO PEOPLE IN THE REFERENCE IMAGES — the man and the woman are his father and mother, and his face blends both: HIS FATHER'S PALE GREY-BLUE EYES with long lashes, his mother's small straight nose and the shape of her smile, full childhood cheeks with soft down, faint freckles across the nose like his mother's. Thick dark brown hair cut short with a cowlick standing up at the crown. He is also clearly the younger brother of a dark-haired teenage girl. A distinct original child, not a copy of either parent. Evenly spaced panels left to right, separated by thin vertical dividers, on a plain mid-grey seamless studio background.
Panel one, left: a headless full-body front view. The body stands straight, arms relaxed at the sides, feet shoulder width apart. There is no head and no neck, the ribbed long-sleeve top's collar holds its own round shape under the dungaree bib and the opening reads as an empty dark hollow looking down into it, as if an invisible person is wearing it. The collar edge is crisp and complete. No fade, no blur, no ghosting, no stump, no wound.
Panel two, centre: the same body full length seen from directly behind, standing straight, arms relaxed at the sides, the short dark hair with its cowlick present, facing away from camera.
Panel three, right: the same child chest-up, front on, looking directly forward, neutral expression, mouth closed, a serious watchful expression in the pale grey-blue eyes.
His build: small and slight, slightly knock-kneed, fair olive skin with colour in the cheeks, a small healed scab on one knee.
Wardrobe, identical in all three panels: a mustard-yellow ribbed long-sleeve top, grey-blue corduroy dungarees with one strap twisted, thick cream socks, small navy velcro trainers. No jewellery.
Flat even studio lighting, shadowless, no cast shadows on the background, identical lighting across all three panels. Photographic, shot on a real camera, sharp focus, visible skin pores and fabric weave, no CGI. No red anywhere in the wardrobe. Original character, not resembling any real person. No text, no watermark, no logos.

## @MiloBefore — variante *(acte I, 6 ans — fiche @Milo en référence)*
A three-panel character reference sheet of the same child from the reference image, keeping his exact face and his father's pale grey-blue eyes — **now two years younger, six years old: a rounder face, finer shorter hair with the same cowlick, one lower front tooth missing, pure delight always close to the surface.** Same three panels, same headless front view, same rear view, same chest-up portrait, same mid-grey background, same dividers.
Wardrobe, identical in all three panels: a green-and-navy striped long-sleeve top, grey corduroy trousers, small navy velcro trainers. No jewellery.
Flat even studio lighting, shadowless, identical across all three panels. Photographic, sharp focus, no CGI. No red anywhere. No text, no watermark, no logos.


## @Anna — la voisine russe, 78 ans
A three-panel character reference sheet, evenly spaced left to right, separated by thin vertical dividers, on a plain mid-grey seamless studio background.
Panel one, left: a headless full-body front view. The body stands straight, arms relaxed at the sides, feet shoulder width apart. There is no head and no neck, the floral housecoat's buttoned collar holds its own shape and the opening reads as an empty dark hollow looking down into it, as if an invisible person is wearing it. The collar edge is crisp and complete. No fade, no blur, no ghosting, no stump, no wound.
Panel two, centre: the same body full length seen from directly behind, standing straight, arms relaxed at the sides. Head and hair present, thin white hair pinned up in a low flat bun with steel pins, facing away from camera.
Panel three, right: the same woman chest-up, front on, looking directly forward, neutral expression, mouth closed.
The woman: seventy-eight, of Russian descent long settled in New England, short and heavy-set, thick at the waist, weight resting on one hip, swollen knuckles. Pale skin thinned and spotted by age, translucent and papery over prominent veins on the backs of the hands. A broad square face with heavy jowls and a strong wide jaw, high wide Slavic cheekbones, a short broad nose, thin lips set in a straight line. Small pale grey-blue eyes deeply hooded by heavy lids, watery, with dark pouches beneath. Sparse faded eyebrows. Deep vertical lines around the mouth and between the brows, age spots on the temples.
Wardrobe, identical in all three panels: a pale sage-green floral housecoat buttoned to the throat, a thick brown hand-knitted cardigan with darned elbows, a grey wool skirt to mid-calf, thick opaque brown stockings, flat brown felt house slippers with trodden-down heels, a thin worn gold wedding band, a small enamel brooch at the collar.
Flat even studio lighting, shadowless, no cast shadows on the background, identical lighting across all three panels. Photographic, shot on a real camera, sharp focus, visible skin pores and fabric weave, no CGI. No red anywhere in the wardrobe. Original character, not resembling any real person. No text, no watermark, no logos.

## @Mei — la patronne du restaurant, 58 ans
A three-panel character reference sheet, evenly spaced left to right, separated by thin vertical dividers, on a plain mid-grey seamless studio background.
Panel one, left: a headless full-body front view. The body stands straight, arms relaxed at the sides, feet shoulder width apart. There is no head and no neck, the white cotton shirt's collar holds its own shape above the apron bib and the opening reads as an empty dark hollow looking down into it, as if an invisible person is wearing it. The collar edge is crisp and complete. No fade, no blur, no ghosting, no stump, no wound.
Panel two, centre: the same body full length seen from directly behind, standing straight, arms relaxed at the sides, the apron ties knotted twice at the back. Head and hair present, long black hair going grey at the roots and temples, worn twisted up in a low bun at the nape and held with a single lacquered wooden hairpin, loose strands escaping at the temples and down the neck, facing away from camera.
Panel three, right: the same woman chest-up, front on, looking directly forward, neutral expression, mouth closed.
The woman: fifty-eight, Chinese American of Fujianese descent, short and sturdy with strong forearms, standing squarely. Warm ivory skin dulled by decades of kitchen heat, enlarged pores across the nose, deep laugh lines, a small burn scar on the inside of the right forearm. A round-square face with a soft but clearly defined jaw, flat wide cheekbones, a short broad nose, a small mouth with a thin upper lip. Dark brown almond eyes with a marked epicanthic fold and fine lines fanning from the corners, a quick direct gaze. Sparse straight dark eyebrows. Long black hair going grey at the roots and temples, worn twisted up in a low practical bun at the nape, held with a single lacquered wooden hairpin, loose strands escaping at the temples.
Wardrobe, identical in all three panels: a plain white short-sleeved cotton shirt, a long dark green cotton apron tied twice around the waist and stained at the hip where she wipes her hands, loose black trousers, flat black canvas shoes with the backs trodden flat, a thin jade bangle on the left wrist, a folded order pad in the apron pocket.
Flat even studio lighting, shadowless, no cast shadows on the background, identical lighting across all three panels. Photographic, shot on a real camera, sharp focus, visible skin pores and fabric weave, no CGI. No red anywhere in the wardrobe. Original character, not resembling any real person. No text, no watermark, no logos.

## @Asha — l'Est-Africaine, 52 ans
A three-panel character reference sheet, evenly spaced left to right, separated by thin vertical dividers, on a plain mid-grey seamless studio background.
Panel one, left: a headless full-body front view. The body stands straight, arms relaxed at the sides, feet shoulder width apart. There is no head and no neck, the cream cotton polo-neck's collar holds its own round shape under the open coat and the opening reads as an empty dark hollow looking down into it, as if an invisible person is wearing it. The collar edge is crisp and complete. No fade, no blur, no ghosting, no stump, no wound.
Panel two, centre: the same body full length seen from directly behind, standing straight, arms relaxed at the sides. Head and hair present, short neat black locs gathered back at the nape with a plain wooden pin, facing away from camera.
Panel three, right: the same woman chest-up, front on, looking directly forward, neutral expression, mouth closed.
The woman: fifty-two, Kenyan American, tall and slim and upright with a long neck and squared shoulders. Deep rich dark brown skin with warm undertones, faint hyperpigmentation along the cheekbones, fine lines at the mouth. A long oval face with high sharply defined cheekbones and a strong clean jawline, a broad nose with a rounded tip, full lips with a defined cupid's bow in a natural deep berry-brown tone with a soft matte finish. Large dark brown almond eyes set wide apart with a calm steady gaze and fine lines at the outer corners. Full arched dark eyebrows lightly shaped. Lightly worn makeup with slightly uneven blending rather than flawless coverage. A few strands greying at the temple.
Wardrobe, identical in all three panels: a fine-gauge cream cotton polo-neck, a long olive-and-indigo patterned open coat in soft woven cloth, straight dark charcoal trousers, flat dark brown leather ankle boots, small gold hoop earrings, a single thin gold bangle.
Flat even studio lighting, shadowless, no cast shadows on the background, identical lighting across all three panels. Photographic, shot on a real camera, sharp focus, visible skin pores and fabric weave, no CGI. No red anywhere in the wardrobe. Original character, not resembling any real person. No text, no watermark, no logos.

## @Fatiha — la Marocaine, 66 ans
A three-panel character reference sheet, evenly spaced left to right, separated by thin vertical dividers, on a plain mid-grey seamless studio background.
Panel one, left: a headless full-body front view. The body stands straight, arms relaxed at the sides, feet shoulder width apart. There is no head and no neck, the patterned tunic's neckline holds its own shape under the open cardigan and the opening reads as an empty dark hollow looking down into it, as if an invisible person is wearing it. The neckline edge is crisp and complete. No fade, no blur, no ghosting, no stump, no wound.
Panel two, centre: the same body full length seen from directly behind, standing straight, arms relaxed at the sides. Head present, a soft patterned ochre and dusty-blue headscarf tied at the nape with dark grey hair gathered loosely under it, facing away from camera.
Panel three, right: the same woman chest-up, front on, looking directly forward, neutral expression, mouth closed.
The woman: sixty-six, Moroccan American of Amazigh heritage, short and rounded with soft shoulders and expressive hands. Warm golden-olive skin with sun spots at the temples and on the hands. A heart-shaped face with a softened but still defined jaw, high broad cheekbones, a long straight nose, a wide mouth with a thin upper lip in a natural brown-rose tone, deep nasolabial folds and deep lines around the mouth from talking and laughing. Dark hazel-brown eyes with heavy hooded lids, a lively animated gaze and deep crow's feet. Strong dark eyebrows greying at the outer ends. Small faded traditional dots tattooed on the chin. White hair at the front, a few strands escaping at the temples.
Wardrobe, identical in all three panels: a long charcoal wool cardigan over a mustard and cream patterned tunic, a long grey pleated skirt to the ankle, dark brown leather flat sandals over thick socks, small gold hoop earrings, several thin gold rings.
Flat even studio lighting, shadowless, no cast shadows on the background, identical lighting across all three panels. Photographic, shot on a real camera, sharp focus, visible skin pores and fabric weave, no CGI. No red anywhere in the wardrobe. Original character, not resembling any real person. No text, no watermark, no logos.


---

### LE SOUVENIR RUSSE — six fiches ajoutées le 30/08 *(flashback de la séq. 4)*
*⚠ Aucun de ces six personnages ne PARLE : le souvenir est muet sous la voix off d'Anna — zéro
lip-sync russe à générer. ⚠ Ils n'existent que dans le bloc 4.3, jamais ailleurs dans le film.*

*Les fiches du **flashback russe** (séq. 4, 30 s, il y a trente ans) — à insérer dans la section 1 **juste après @Anna**, dont la première descend. **Aucun de ces personnages n'existe au présent du film.** Le souvenir se joue sur deux dates : **l'hôpital, il y a ~30 ans** (@RussianHospitalCorridor), puis **deux ans plus tard, il y a ~28 ans**, les trois coups, la rue et la cour (@AnnaKitchenPast · @RussianNightStreet · @RussianCourtyard).*

**⚠ QUEUE COMMUNE — à recopier mot pour mot à la fin de CHAQUE prompt de cette section, sans jamais l'abréger.** Elle porte trois règles d'un coup et elle est alignée sur le document des lieux russes écrit le même jour :

> *Flat even studio lighting, shadowless, no cast shadows on the background, identical lighting across all three panels. Photographic, shot on a real camera, sharp focus, visible skin pores and fabric weave, no CGI, no beauty retouching, no skin smoothing. **No red anywhere in the image** — no red garment, no red trim, no red scarf and above all no red pioneer neckerchief, no red badge, no red star, no red prop, nothing red in the background. **No religious object of any kind** — no cross, no icon, no pendant, no medal, no amulet. **No badge, no emblem, no insignia, no crest, no pin.** **No lettering anywhere and no Cyrillic characters of any kind** — no writing on any garment, no numerals, no label, no tag. Original character, not resembling any real person. No text, no watermark, no logos.*

## @AnnaYoung — Anna trente ans plus tôt, en Russie *(48 ans — flashback séq. 4)* ⟵ *(fiche @Anna en référence — OBLIGATOIRE)*
> **GÉNÉRÉE LE 30/08 — job `cf30ae6c-483b-4279-a0ee-4dbef01c3e71`** *(GPT Image 2 · 4K · high · 16:9 · référence = la fiche @Anna, job `fcd3c452-58fd-45dd-b053-e88a3371d6a1`)*.
> ⚠ **À VALIDER À L'ŒIL AVANT TOUT LE RESTE DE LA SÉQ. 4** : si on ne reconnaît pas la vieille voisine dans cette femme, tout le souvenir russe s'effondre. Sauvegarder ensuite comme Élément `@AnnaYoung`.
*Ce n'est pas une nouvelle personne, c'est une variante d'âge : le spectateur doit reconnaître la vieille voisine dans la femme du flashback **sans qu'on le lui dise jamais**. Générée sans la fiche @Anna en image de référence, elle ne vaut rien.*

A three-panel character reference sheet of the same woman as the reference image, thirty years earlier — keeping her exact bone structure: the broad square face with the strong wide jaw, the high wide Slavic cheekbones, the short broad nose, the thin lips set in a straight line, and the small pale grey-blue eyes deeply hooded by heavy lids — **now forty-eight years old and not yet old**: the flesh still firm along the jaw with no jowls, the cheeks full and solid, the skin thick and weather-worn rather than thinned and papery, cold-mottled across the cheekbones and the bridge of the nose from years of outdoor winters, coarse open pores, no age spots at the temples, no translucency and no standing veins on the backs of the hands. Deep lines only between the brows and at the outer corners of the eyes, the vertical lines around the mouth barely started. The eyes clear and dry rather than watery, the pouches beneath them shallow. Eyebrows fuller and mid-brown, not yet faded. The hair thick, dark chestnut brown heavily streaked with grey at the temples and along the parting, pinned into the same low flat bun with the same steel pins — the identical habit, thirty years earlier. Her build: already short and heavy-set and thick at the waist, but **the back straight**, the shoulders squared and level, the weight carried evenly on both feet, the hands broad, reddened and work-hardened with short blunt nails and knuckles enlarged by work but not yet swollen by age. Same plain mid-grey seamless studio background, same thin vertical dividers, evenly spaced left to right.
Panel one, left: a headless full-body front view. The body stands straight, arms relaxed at the sides, feet shoulder width apart. There is no head and no neck, the heavy overcoat's collar holds its own shape and the opening reads as an empty dark hollow looking down into the coat, as if an invisible person is wearing it. The collar edge is crisp and complete. No fade, no blur, no ghosting, no stump, no wound.
Panel two, centre: the same body full length seen from directly behind, standing straight, arms relaxed at the sides. Head present, the dark charcoal wool headscarf covering the hair and knotted under the chin so the knot is hidden at this angle, the back edge of the scarf sitting low on the nape with a few thick greying strands of the bun escaping beneath it, facing away from camera.
Panel three, right: the same woman chest-up, front on, looking directly forward, neutral expression, mouth closed, the headscarf framing the face and tied under the chin.
Wardrobe, identical in all three panels: period-correct everyday winter clothing of a poor household thirty years ago, worn and mended, nothing that reads as costume design — a dark charcoal wool overcoat two sizes too big, the shoulder seams dropping past her own shoulders, the cuffs turned back once, the hem to mid-calf, the wool rubbed shiny at the elbows and balded at the seat, one horn button replaced long ago with a mismatched grey one, the pocket corners hand-darned in thread that does not match; under it a heavy oatmeal hand-knitted cardigan and a dark grey-green wool dress washed thin at the collar; thick brown stockings; scuffed black leather winter boots, the heels worn down on the outer edge, salt tide-lines dried white across the toes; a plain dark charcoal wool headscarf knotted under the chin; the same thin worn gold wedding band as the reference. No other jewellery.
*(+ QUEUE COMMUNE)*

⚠ **Arithmétique — corrigée.** @Anna a **78 ans** au présent. L'hôpital est **trente ans** en arrière : elle a **48 ans**, son fils onze. Les trois coups, la rue et la cour se jouent **deux ans plus tard** (il y a ~28 ans) : elle a **50 ans**. **Une seule fiche couvre les deux dates** — à cet âge deux ans ne se voient pas dans la chair — mais il ne faut pas générer une seconde @AnnaYoung pour la cour. *(⚠ Le script porte « Le visage d'Anna (48) » au plan 4.3l, qui se joue deux ans après l'hôpital : lire 50.)*
⚠ **Le foulard** est noué sous le menton dans toute la partie « deux ans plus tard » (porte, rue, cour). **À l'hôpital il est repoussé sur les épaules et le chignon apparaît** — et c'est précisément là que sa nuque est à l'image (4.3b, premier plan flou ; 4.3c, elle de dos, les genoux qui lâchent). **Cet état-là est verrouillé par un tirage à part, ci-dessous** : ne pas le laisser à l'improvisation d'un prompt de plan.
⚠ **Ce qui doit rester générique** : elle n'a aucune expression à porter dans la fiche. Le chagrin se joue au plan, dans la main qui se referme sur du vide (4.3a) et dans le corps qui descend le long de la faïence (4.3c) — jamais dans un visage de fiche.

**Tirage à générer EN PLUS de la fiche — la nuque, foulard repoussé** *(hors Éléments · fiche @AnnaYoung en référence)*
> **GÉNÉRÉ LE 30/08 — job `9890c939-e6b6-42be-a522-b06b881a1b24`** *(GPT Image 2 · 4K · high · 3:2 · référence = @AnnaYoung, job `cf30ae6c-483b-4279-a0ee-4dbef01c3e71`)*.

A single reference image of the same forty-eight year old woman from the reference image, standing full length on the same plain mid-grey seamless studio background, seen from directly behind, arms at her sides — **the dark charcoal headscarf pushed back off the head and lying across the shoulders, still knotted loosely at the throat, so the low flat bun is fully visible**: thick dark chestnut hair heavily streaked with grey, pinned with the same steel pins, a few coarse strands pulled loose at the nape and standing away from the head, the parting showing grey. Same heavy overcoat, same shoulder seams dropping past her own shoulders, wardrobe otherwise identical to the reference sheet in every detail. The nape and the set of the shoulders clearly readable. Flat even studio lighting, shadowless.
*(+ QUEUE COMMUNE, en retirant « identical lighting across all three panels »)*

⚠ **Pourquoi ce tirage existe** : le couloir de l'hôpital est le seul endroit du film où Anna est filmée de dos, et c'est le plan charnière de la séquence. Sans référence verrouillée, la nuque de 4.3b et la nuque de 4.3c ne seront pas la même femme.

## @Kolya11 — le fils d'Anna, 11 ans, à l'hôpital *(sa seule apparition du film : 4.3a, le lit)* ⟵ *(fiche @AnnaYoung en référence)*
> **GÉNÉRÉE LE 30/08 — job `b968601b-a4dd-462d-9323-89847835d336`** *(GPT Image 2 · 4K · high · 3:2 · référence = la fiche @AnnaYoung, job `cf30ae6c-483b-4279-a0ee-4dbef01c3e71`)*.
> ⚠ **LE GABARIT À TROIS PANNEAUX A ÉTÉ REFUSÉ PAR LA MODÉRATION HIGGSFIELD** (statut `nsfw`) : le panneau
> « corps de face SANS TÊTE », appliqué à un enfant gravement malade en chemise d'hôpital, déclenche le
> filtre. **Fiche refaite en DEUX panneaux, tous deux avec la tête** (buste de face · buste de dos), et
> l'état de santé écrit en « enfant en convalescence, ordinaire, fatigué » plutôt qu'en termes cliniques.
> **Règle à retenir pour toute future fiche d'enfant : jamais de panneau sans tête.** L'identité tient
> quand même : un seul visage à copier, celui du panneau de gauche.
*Il porte le prénom que la jeune mère donnera à son enfant. **On ne le voit qu'une fois, et il est en train de mourir** : la fiche est écrite dans cet état-là, il n'existe aucun plan de lui en bonne santé. Ne pas générer de variante « avant » : ce serait un Élément que rien n'utilise, à quatre jours de la deadline.*

A three-panel character reference sheet of an original eleven year old boy who is unmistakably THE SON OF THE WOMAN IN THE REFERENCE IMAGE — her broad square face in a child's version, her high wide Slavic cheekbones, her short broad nose, her thin straight mouth, and above all her small pale grey-blue eyes deeply hooded by heavy lids, under sparse fair eyebrows. He is a distinct original child, not a copy of the woman. **He is gravely ill and has been for a long time**: the face wasted so the cheekbones and the jaw stand out under the skin, the temples hollowed, dark grey-brown hollows under the eyes, the skin a dull yellow-grey with no colour anywhere in it, the lips dry, cracked and drained to the colour of the skin, a fine sweat along the hairline and the upper lip with a few strands of hair stuck flat to the forehead. His hair thin and lifeless, mid-brown, grown out unevenly and cut short at home months ago, the scalp showing at the crown. His body: far too thin for his height, the shoulders narrow and dropped, the collarbones and the wrist bones standing out, the neck too long for the head, the hands very thin with pale nail beds, a small dark bruise inside one elbow. **Nothing angelic, nothing sentimental, no beauty retouching, no glow, no saintly light** — a real, ordinary, seriously ill child. Evenly spaced panels left to right, separated by thin vertical dividers, on a plain mid-grey seamless studio background.
Panel one, left: a headless full-body front view. The body stands straight, arms relaxed at the sides, feet shoulder width apart. There is no head and no neck, the hospital gown's neckline holds its own shape and the opening reads as an empty dark hollow looking down into it, as if an invisible person is wearing it. The neckline edge is crisp and complete. No fade, no blur, no ghosting, no stump, no wound.
Panel two, centre: the same body full length seen from directly behind, standing straight, arms relaxed at the sides, the thin mid-brown hair present with the scalp showing at the crown, the gown's back ties visible, the nape very thin, facing away from camera.
Panel three, right: the same child chest-up, front on, looking directly forward, neutral expression, mouth closed, the eyes open and dull.
Wardrobe, identical in all three panels: a washed-thin pale grey-green cotton hospital gown of the period, the printed pattern worn away to a ghost, the seams softened by a hundred boil washes, one shoulder tie broken and re-knotted, tied loose at the back; thick grey hand-knitted socks brought from home, one sagging at the ankle; no shoes; **a plain narrow blank fabric band on one wrist with no lettering and no marking of any kind**. No jewellery.
*(+ QUEUE COMMUNE)*

⚠ **Le plan qu'il joue** *(4.3a — 2,5 s)* : il est **allongé**, trop petit pour un lit de fer d'adulte, la bouche entrouverte, une mèche collée au front, **sa main dans celle d'Anna — et les doigts se desserrent un par un.** La fiche est debout et neutre parce que c'est un gabarit de personnage ; **la maladie doit être dans la CHAIR de la fiche, pas dans une pose**, sinon le plan la perdra.
⚠ **Aucune tache de naissance.** La version corrigée du 30/08 relie les deux femmes par **le prénom hurlé dans le couloir**, pas par une marque sur un visage. Si une marque était réintroduite quelque part, elle devrait apparaître à l'identique sur @Kolya11 **et** sur @Kolya2 — deux fiches à refaire.
⚠ **Aucune photographie encadrée de lui n'existe dans le film.** Ne pas fabriquer d'insert : @AnnaKitchen est un lieu verrouillé, et sa fiche impose *« framed photographs turned so their faces are not readable »* — tous les cadres restent de dos, y compris chez Anna aujourd'hui. Son fils, on ne le voit qu'à l'hôpital, il y a trente ans.

## @WardDoctor — le médecin de service *(jamais nommé — 4.3b, 4.3d, 4.3e)* ⟵ *(fiche de base, aucune référence croisée)*
> **GÉNÉRÉE LE 30/08 — job `b7340dca-eb18-4567-a894-fbedb466381c`** *(GPT Image 2 · 4K · high · 16:9 · sans référence)*.
*Sans lui, le raccord entre 4.3b (le couloir vu d'Anna) et 4.3e (le même couloir vu du brancard) ne tient pas : ce sera deux hommes différents, et la séquence perd son pivot. **Il ne parle jamais.** Son seul geste : il retire sa casquette de toile et n'avance pas.*

A three-panel character reference sheet, evenly spaced left to right, separated by thin vertical dividers, on a plain mid-grey seamless studio background.
Panel one, left: a headless full-body front view. The body stands straight, arms relaxed at the sides, feet shoulder width apart. There is no head and no neck, the white coat's stand collar holds its own shape and the opening reads as an empty dark hollow looking down into the coat, as if an invisible person is wearing it. The collar edge is crisp and complete. No fade, no blur, no ghosting, no stump, no wound.
Panel two, centre: the same body full length seen from directly behind, standing straight, arms relaxed at the sides. Head present, thinning grey hair cut short and flattened by the cap, the soft cloth cap on, the coat's belt tied at the small of the back, facing away from camera.
Panel three, right: the same man chest-up, front on, looking directly forward, neutral expression, mouth closed, the cloth cap on.
The man: **fifty-five, Russian, ordinary and tired** — average height, a heavy chest going soft, a short thick neck, a squarish face with a broad forehead and a blunt nose, deep lines from the nose to the corners of the mouth, grey stubble showing along the jaw by the end of a double shift, pouched lower lids, small brown eyes, a grey moustache trimmed square. Thinning grey hair. **The hands are the character**: broad, scrubbed raw and dry, the knuckles chapped and split, the nails cut to the quick. **Nothing distinguished, nothing heroic, no bedside manner in the face** — a state employee at the end of a shift.
Wardrobe, identical in all three panels: period-correct hospital clothing of thirty years ago — a white cotton coat gone bone-grey with boiling, buttoned to the throat with a stand collar, belted at the back, the cuffs frayed and turned back once, a rusty spot at one pocket corner where a pen has bled through, the shoulder seam mended in slightly whiter thread; **a soft white cloth cap, the kind that is taken off in a corridor** — it must read as removable and hold its shape in the hand; a grey-green shirt collar showing at the neck; dark grey trousers gone shiny at the knee; scuffed brown leather shoes with worn heels. No stethoscope, no instrument, no clipboard, no armband. No jewellery except a plain thin steel wedding band.
*(+ QUEUE COMMUNE — et en plus, explicitement : **no red cross anywhere on the coat, on the cap, on the pocket, or on any object**.)*

⚠ **La croix rouge est le piège nº 1 de cette fiche** : blouse blanche + hôpital = le modèle la pose de lui-même, sur la poche ou sur la casquette. Le refus est déjà dans la queue commune, **le répéter dans chaque prompt de plan qui le cite** (règle B).
⚠ **Il joue aussi le médecin penché à l'oreille de la jeune femme (4.3d).** Un seul homme pour les trois plans : c'est plus vrai (un hôpital de nuit n'a qu'un médecin de garde) et c'est une génération de moins.

## @YoungMother — la jeune mère, dans la cour *(25 ans — il y a ~28 ans · **fiche de base**)*
> **GÉNÉRÉE LE 30/08 — job `f0200a53-86ce-4b0f-950b-954b81e89d47`** *(GPT Image 2 · 4K · high · 16:9 · sans référence)*. C'est la fiche de base : les deux suivantes en descendent.
*Générée **sans référence croisée** : elle ne descend de personne. Un visage ordinaire, fatigué, que personne ne remarquerait — c'est capital pour le réalisme, et c'est ce qui rend le prénom bouleversant plutôt que joli.*

A three-panel character reference sheet, evenly spaced left to right, separated by thin vertical dividers, on a plain mid-grey seamless studio background.
Panel one, left: a headless full-body front view. The body stands straight, arms relaxed at the sides, feet shoulder width apart. There is no head and no neck, the winter coat's collar holds its own shape and the opening reads as an empty dark hollow looking down into the coat, as if an invisible person is wearing it. The collar edge is crisp and complete. No fade, no blur, no ghosting, no stump, no wound.
Panel two, centre: the same body full length seen from directly behind, standing straight, arms relaxed at the sides. Head and hair present, fine sandy-brown hair pulled back into a thin low ponytail with a stretched elastic, the ends dry and uneven where they were cut at home, a soft grey knitted hat pushed back off the crown, facing away from camera.
Panel three, right: the same woman chest-up, front on, looking directly forward, neutral expression, mouth closed.
The woman: twenty-five, Russian, small and thin-boned and slightly stooped, narrow sloping shoulders, a short neck, a body that has not got its strength back. A narrow oval face with a small receding chin and a soft undefined jaw, a long straight nose set a little off-true at the bridge, close-set light hazel-brown eyes with pale sparse lashes and a flat tired gaze, heavy grey hollows beneath them. Fine sandy-brown hair, thin at the temples. Pale skin blotched and uneven in tone, cold-mottled across the nose and cheeks, dry and flaking at the nostrils and along the eyebrows, a small cluster of old blemish marks on the chin. Chapped lips split at the centre, a colourless mouth, one upper front tooth slightly chipped and turned. Unshaped brows, no makeup at all. Hands rough and cracked across the knuckles, nails bitten short, one cuticle torn. **An ordinary plain face, tired, entirely unremarkable — not a model, no glamour styling, no beauty retouching, no skin smoothing, no flattering angle.**
Wardrobe, identical in all three panels: period-correct everyday winter clothing of a poor household thirty years ago — a shapeless dark green-brown wool coat cut for someone larger, belted at the waist with the coat's own frayed belt, a thin synthetic fur collar rubbed bald in patches, two buttons matching and one not, the hem let down and showing the old crease; a soft grey hand-knitted hat; a dark mustard scarf wound twice at the throat, the wool pilled; thick dark stockings; grey felt winter boots with black rubber galoshes pulled over them, the galoshes scuffed grey at the toes. No jewellery except a plain thin steel wedding band.
*(+ QUEUE COMMUNE)*

⚠ **Elle ne doit ressembler à personne de la famille d'Anna** — ossature étroite contre ossature carrée, yeux clairs mais rapprochés contre petits yeux encapuchonnés. Si les deux femmes se ressemblent, le lien du prénom devient une ressemblance, et le récit s'effondre.
⚠ **Le lieu de la rencontre est la cour** (@RussianCourtyard), au banc — c'est là que le prénom est demandé et donné. Elle n'a aucune réplique à l'image : la voix d'Anna couvre tout, **aucun lip-sync russe à générer.**

## @YoungMotherHospital — variante *(l'hôpital, deux ans plus tôt — 23 ans, enceinte)* ⟵ *(fiche @YoungMother en référence)*
> **GÉNÉRÉE LE 30/08 — job `28f272da-e8db-4229-983a-43564754a04a`** *(GPT Image 2 · 4K · high · 3:2 · référence = @YoungMother, job `f0200a53-86ce-4b0f-950b-954b81e89d47`)*.
A three-panel character reference sheet of the same woman from the reference image, keeping her exact face — the narrow oval face, the long straight nose off-true at the bridge, the close-set light hazel-brown eyes with their pale lashes, the chipped upper front tooth — **now two years younger, twenty-three, and heavily pregnant at around eight months**: the face fuller and water-swollen, the eyelids and the upper lip puffy, the jawline lost, blotchy uneven pigmentation across the cheekbones and the forehead, the skin shining with sweat, the hair stuck flat to the temples and the forehead in dark wet strands with the rest scraped back and escaping a snapped elastic, the lips colourless and dry with a fresh split, the lower lids swollen and the whites of the eyes reddened from crying, the eyes open too wide and not focused on anything. The belly high and full, the body heavy and off-balance, one hand resting low under the bump, the ankles swollen over the socks. Same three panels as the reference: headless full-body front view (the hospital gown's neckline holding its own shape, an empty dark hollow, crisp edge, no fade, no blur, no ghosting, no stump, no wound), full rear view with the hair present and the gown's back ties visible, chest-up front portrait with neutral expression and mouth closed. Same plain mid-grey seamless studio background, same thin vertical dividers.
Wardrobe, identical in all three panels: a washed-thin pale grey-green cotton hospital gown of the period, the printed pattern worn away to a ghost, the seams softened by a hundred boil washes, one shoulder tie broken and re-knotted, tied loose at the back; a stretched dark grey hand-knitted cardigan hanging off the shoulders; thick hand-knitted oatmeal socks; no shoes; **a plain narrow blank fabric band on the left wrist with no lettering and no marking of any kind**. No jewellery except the plain thin steel wedding band.
*(+ QUEUE COMMUNE)*

⚠ **Ne PAS écrire d'émotion dans le prompt** (« la pire heure de sa vie », « désespérée », « terrifiée ») : le modèle ne sait pas la rendre, il rend du pathos. Tout est déjà dans le corps ci-dessus — les paupières gonflées, la lèvre fendue, les cheveux collés, le regard qui ne se pose sur rien. **C'est la règle du film : on écrit ce que ça fait au corps.**
⚠ **Le geste du récit** — elle lève les yeux — se joue **vers un plafond d'hôpital écaillé** (4.3f), jamais vers un ciel, jamais vers un objet de culte, jamais avec les mains jointes (règle E). Ce qu'on filme, c'est la nuque qui bascule et la gorge qui se tend, pas une prière.
⚠ Le modèle embellit spontanément une jeune femme enceinte (peau lissée, cheveux coiffés, lumière flatteuse) : les mentions anti-retouche de la queue commune sont **structurantes**, ne pas les couper pour raccourcir le prompt.
⚠ **C'est la seule variante du pack qui remonte le temps** au lieu de le descendre : 23 ans à l'hôpital, 25 dans la cour deux ans plus tard.

## @Kolya2 — le petit garçon de la cour, 2 ans *(il y a ~28 ans)* ⟵ *(fiche @YoungMother en référence)*
> **GÉNÉRÉE LE 30/08 — job `436b224b-b82f-4c44-a9dc-373fa7ebca4a`** *(GPT Image 2 · 4K · high · 3:2 · référence = @YoungMother, job `f0200a53-86ce-4b0f-950b-954b81e89d47`)*. Deux panneaux avec la tête, même raison que @Kolya11.
*Il porte le prénom du fils mort. **Il ne fait rien d'autre qu'être là** : accroché à la jambe de sa mère, il regarde par en dessous une vieille femme qu'il ne connaît pas. Le prénom, ce sont les deux femmes qui se le disent — lui ne réagit pas, ne se retourne pas, n'entend rien de particulier. **C'est ce qui rend la scène insoutenable : l'enfant ne sait pas ce qu'il porte.***

A three-panel character reference sheet of an original two year old boy who is unmistakably THE SON OF THE WOMAN IN THE REFERENCE IMAGE — her long straight nose in miniature, her close-set light hazel-brown eyes with the same pale sparse lashes, her fine sandy-brown hair, here soft and flyaway with a deep whorl at the crown and a cut fringe. He is a distinct original child, not a copy of the woman. Toddler proportions observed honestly: a large head on a short neck, a rounded belly, short legs slightly bowed, small fat hands with dimples where the knuckles will be, no waist. Evenly spaced panels left to right, separated by thin vertical dividers, on a plain mid-grey seamless studio background.
Panel one, left: a headless full-body front view. The body stands straight, arms relaxed at the sides, feet planted apart. There is no head and no neck, the padded snowsuit's stand-up collar holds its own round shape and the opening reads as an empty dark hollow looking down into the suit, as if an invisible person is wearing it. The collar edge is crisp and complete. No fade, no blur, no ghosting, no stump, no wound.
Panel two, centre: the same body full length seen from directly behind, standing straight, arms relaxed at the sides, the knitted pompom hat on with the chin tie hanging loose, fine hair escaping at the nape, the mitten cord slung across the back of the suit between the two cuffs, facing away from camera.
Panel three, right: the same child chest-up, front on, looking directly forward, neutral expression, mouth closed.
His state: fair skin cold-mottled high on both cheeks, a permanent damp shine at the chin, a dry crust under the nose, four small teeth showing when the mouth opens, a faint milk-crust patch at the hairline. Nothing precious, nothing advertising-cute — a solid, slightly dishevelled small child dressed against real cold.
Wardrobe, identical in all three panels: period-correct winter clothing of thirty years ago — a padded one-piece quilted snowsuit in dull petrol blue with a mustard-yellow yoke, the quilting flattened at the knees and the seat, a neat square mend at one cuff, the zip pull replaced with a loop of cord; a hand-knitted oatmeal wool hat with a pompom on top and a chin tie; hand-knitted mustard mittens joined by a long twisted wool cord threaded through both sleeves and hanging out at the cuffs; thick grey wool tights; small grey felt boots with black rubber galoshes.
*(+ QUEUE COMMUNE)*

⚠ **Son seul cadre** *(4.3k)* : **accroché à la jambe de sa mère, il regarde Anna par en dessous** — donc en légère contre-plongée, à hauteur d'adulte, la tête renversée en arrière. Il ne parle pas, il ne sourit pas, il ne joue pas. **Aucun plan du film ne le montre en train de se retourner** : ne pas générer de tirage de « position de retournement », il n'existe pas de plan pour l'accueillir.
⚠ **Il ne doit PAS ressembler à @Kolya11.** Les deux enfants ne sont liés que par le prénom, et c'est toute la force de la scène. Cheveux blond-roux fins contre cheveux mi-bruns, ossature étroite contre ossature large, yeux noisette rapprochés contre yeux gris-bleu encapuchonnés. **Consigne à répéter dans le prompt de plan, pas seulement dans la fiche** — et de toute façon les deux ne sont jamais dans la même image.
⚠ **Le costume d'époque tire spontanément vers le rouge** (foulard de pionnier, drapeau, étoile) : la queue commune le refuse, **la recopier entière dans chaque prompt de plan**, sinon la règle B tombe dès la première image.

---

## Ordre de génération conseillé

1. **@Anna** — existe déjà, c'est l'ancre. Rien ne se génère avant elle.
2. **@AnnaYoung** ⟵ @Anna *(référence obligatoire)* · puis **le tirage « nuque, foulard repoussé »** ⟵ @AnnaYoung *(hors Éléments)*
3. **@Kolya11** ⟵ @AnnaYoung
4. **@YoungMother** ⟵ **aucune référence** — visage indépendant, à générer en premier de sa branche
5. **@YoungMotherHospital** ⟵ @YoungMother
6. **@Kolya2** ⟵ @YoungMother
7. **@WardDoctor** ⟵ **aucune référence** — il n'appartient à aucune des deux branches

**Deux branches, jamais mélangées.** La branche Anna se ressemble de mère à fils ; la branche de la jeune mère se ressemble de mère à fils ; **les deux branches ne se ressemblent pas entre elles.** Le seul pont entre elles est un prénom entendu dans un couloir. Le médecin n'appartient à personne.

**À reporter au §5 ORDRE DE PRODUCTION** : l'étape 5 (personnages secondaires) passe de 4 à **10 fiches** (+@AnnaYoung, @Kolya11, @WardDoctor, @YoungMother, @YoungMotherHospital, @Kolya2 = **6 nouveaux Éléments**) ; l'étape 7 (plans hors Éléments) passe de 3 à **4 tirages** (+ la nuque d'Anna, foulard repoussé). **Rappel** : l'étape 6 passe de 17 à **21 lieux** avec le bloc des lieux russes → **total avant le premier plan du film : 34 → 45 Éléments.**

**Durée ajoutée au film : 0 s.** Ce bloc ne crée aucun plan — six fiches et un tirage de position. Le flashback qu'elles servent reste à **30 s exactement**, et la séq. 4 à 78 s.

---

# 2. LES LIEUX

*⚠ **Les quatre lieux russes du flashback (LIEU-17 à LIEU-20) ne sont PAS repris ici** :
ils ont leurs propres documents, plus détaillés, dans `docs/generations/lieux/`. Ils suivent les mêmes
règles et portent la même queue commune. Tags : `@RussianHospitalCorridor`, `@RussianHospitalWard`,
`@AnnaKitchenPast`, `@RussianNightStreet`, `@RussianCourtyard`.*
*GPT Image 2, 4K. **Générés VIDES de toute figure.** Sauvegarder chacun en Élément.*
**Queue commune à tous les lieux (RÉALISME MAX — demande David 25/08, à recopier en entier) :** *The location is completely empty, no people anywhere, no figures, no subject. No readable text, no lettering, no signage with words, no logos, no brand names, no place names. Hyper-realistic documentary photograph, indistinguishable from a real location photo: shot on a full-frame digital cinema camera, natural light only, true-to-life colour, real-world imperfections everywhere — fingerprints and grease marks on handles and surfaces, chipped and repainted edges, uneven plaster, scuffed floor, water stains, dust in the corners, worn varnish, slightly crooked shelves — subtle sensor grain, gentle natural vignetting, nothing staged or styled. NOT CGI, NOT a 3D render, NOT an illustration, no concept-art look, no video-game lighting, no HDR glow, no over-saturation, no perfect symmetry, no showroom cleanliness. Shot like a real photograph, not a render: full-frame camera with a fixed prime lens, natural depth of field with gentle focus falloff, soft halation blooming around the brightest window or lamp, subtle chromatic aberration and natural vignetting at the frame edges, faint ISO noise in the deepest shadows, highlights rolling off softly like film, white balance a touch imperfect as on a real location, the composition half a degree off-true as if framed by a human hand. The image should look like an unremarkable frame from a location scout's camera roll — believable, ordinary, real. No oversharpening, no waxy or plastic surfaces, no teal-and-orange colour grade, no tilt-shift miniature effect, no impossible depth of field, no dreamlike haze, no fantasy atmosphere, no AI artifacts.*

**@Kitchen** *(révisé 24/08 — la fenêtre JUSTE AU-DESSUS de la poêle, demande David · densifié 25/08)* — A small working-class kitchen in a New England triple-decker, seen at eye level from the west side of the room. The working wall is the far east wall, and THE SINGLE WINDOW IS DIRECTLY ABOVE THE GAS RANGE — its sill just above the back burners, no cabinet over the range, a cast-iron pan on the front-left burner right under the glass. The window is an old double-hung sash painted off-white, the paint blistered and browned along the bottom rail by years of pan heat, the glazing putty cracked and crumbling at one corner, a fine film of cooking grease and dust on the lower panes softening everything seen through them; the sill carries old knife marks and a fossilised drip of candle wax. The pan is decades-old cast iron, its seasoning built up black and glossy, the handle worn grey. Along that wall: an enamel sink worn through to dark metal around the drain, limescale crusted white at the base of the crosshead taps, the chrome rubbed to brass on the handles; a cluttered counter whose varnish is scrubbed away in a pale cloud around the chopping area, marked with knife scars and one black ring burned by a hot pot, holding a small ageing radio with a dented speaker grille, a yellowed dial with its markings worn to nothing, and a bent wire antenna; then the gas range under the window, its white enamel chipped to black steel on one corner, the burner grates seasoned black, a soft amber varnish of old grease around the control knobs; a thin striped cotton tea towel, hem fraying, over the oven rail. Open shelves with cream and blue crockery on the left north wall — stacked mixing bowls, mismatched plates, the cream-and-blue butter dish, cups hanging from dull brass hooks — the shelf edges chipped through the faded sage to an older cream paint, the boards bowing slightly under the weight; a doorway to a dark hallway in the right south wall near the corner, its frame worn to bare wood at hand height. A worn wooden table with four mismatched wooden chairs stands in the middle of the room, the tabletop scrubbed pale and silky with the ghosts of old water rings, one chair repainted long ago and chipping, all four seats polished by use. Painted tongue-and-groove walls in faded sage, scuffed at chair-back height and darkened to ochre behind the range; old ceramic floor tiles in faded buff and grey, their glaze worn matte along the path from sink to table, one tile cracked in front of the range, the grout gone dark. Low morning light pours through the window above the range, falls straight onto the pan — which throws a soft warm gleam back up onto the ceiling — edges the enamel of the range in gold, and lies in a hard bar across the table, dust visible in it; the pale walls bounce the gold back so the whole room reads bright, generous and warm, nothing murky, nothing underexposed. Warm ambers and worn wood, deep shadows in the corners that stay warm and readable, never crushed to black. No red anywhere. *(+ queue commune)*

**@Quay** — A working fishing quay on the North Atlantic coast, seen at eye level from the walkway, looking along it. Stacked grey and blue lobster traps, their vinyl-coated wire bleached chalky by salt, runners worn white, broken corners mended with zip ties and twists of monofilament; coiled rope stiff with salt, some hanks tarred black, laid on the concrete beside a low warehouse wall in weathered brick — the faces spalled and flaking, the mortar repointed in mismatched patches, a green tide-line of algae along the base and white salt bloom higher up. Cast-iron bollards with generations of paint chipped away to laminar rust, their crowns rubbed bright by hawsers; a rusted chain slumped between them, flakes of rust staining the concrete orange beneath each link; gull droppings dried white on the bollard tops. Trawler masts and cranes beyond, their cables black with old grease, and flat grey water lying still against the pilings. Wet concrete underfoot, worn and pitted, standing water in the hollows, a faint diesel sheen at the drain, fish scales dried silver in the cracks. It is the end of a clear day: the sun hangs low over the water and pours warm gold straight down the quay, raking long soft shadows from the bollards and the trap stacks, firing the wet concrete with amber glare, filling every puddle with the colour of the sky and warming the brick to ochre — full, generous evening light, clear and high, nothing underexposed; the muted greys, greens and blues of the gear all warmed through with gold. No red anywhere, no buoys, no red hulls. *(+ queue commune)*

**@LivingRoom** — A small living room at night in a New England triple-decker, seen at eye level. A worn armchair, its wool upholstery gone shiny and threadbare along the front of both arms, the seat cushion permanently hollowed, a knitted throw in oatmeal and brown squares folded over one arm; a low side table in dark-varnished wood, its top ringed with the pale ghosts of years of hot mugs, one drawer with a loose tarnished brass pull, and on it a single lamp with a woven ecru shade — the inside of the shade scorched faintly brown at the top rim, the braided cord running down to a floor socket with a strip of aged tape holding it along the skirting. A threadbare rug, its pattern trodden to shadow along the walking line, one corner curled and refusing to lie flat; a bookshelf of sagging boards packed with cloth-bound spines faded to blankness, more books stacked flat on top, dust thick at the shelf ends; a dark window with the reflection of the room in it, the old glass slightly wavy, dust felted on the meeting rail, the night beyond pure black. Bare floorboards dark with age around the rug, their gaps holding decades of dust. The lamp is the only light source, warm and low: it lays one amber pool across the rug and the arm of the chair, prints the basket-weave of its shade faintly up the wall, catches the varnish rings on the table — and everything beyond its throw falls to near-black, a soft gentle underexposure with deep true shadows and no fill from anywhere. Deep shadows, warm pool of light on the rug. No red anywhere. *(+ queue commune)*

**@KidsBedroom** — A small shared children's bedroom at night, seen at eye level from the foot of the bed, shared by a teenage girl and a small boy. A double bed against a papered wall — the wallpaper an old faded pattern of small yellow flowers on grey-blue, its seams lifting near the ceiling, rubbed and scuffed at mattress height where the bed has knocked it for years — with an amber quilted blanket, hand-stitched, the quilting puckered with washing, one corner patched in a near-matching cloth; a bedside lamp with a woven shade, its switch a worn thumb-wheel on the cord; a painted chest of drawers chipped to an earlier colour around the knobs, the top drawer not quite closing flush, its top crowded with small worn toys and a hairbrush; children's drawings pinned to the wall — pencil and crayon, no letters anywhere, corners curled, small rust halos around the older pins; an open doorway to a dark hallway on one side, its frame nicked and scuffed at child height. Painted floorboards with a small rag rug beside the bed, dust gathered along the skirting. Large clear wall surface above the bed. The bedside lamp is the only light source, warm amber, low and raking across the papered wall so every seam and blister of the paper stands out in relief and a shadow cast on it would be huge and sharp; the ceiling and the far corners fall into soft warm darkness, gently underexposed, the doorway a pure black rectangle. Deep warm shadows. No red anywhere. *(+ queue commune)*

**@HospitalRoom** — A single hospital room in daylight, seen at eye level from the foot of the bed. An adjustable bed with white sheets still creased along their fold lines, a cellular blanket tucked flat, the side rails in dulled chrome with grey plastic latches worn smooth by hands; a bedside monitor with pale sea-green traces, its screen carrying a thin film of dust, its casing slightly yellowed with age, the cables gathered with a strip of tape; an IV stand in chrome, chipped at the weighted base, its castors scuffed grey; a moulded plastic visitor chair in pale grey-green, the front edge of the seat polished by use, a hairline crack starting at one corner; a north-facing window with a thin voile blind greyed along the hem, condensation beaded along the bottom of the aluminium frame, the sealant gone grey; pale green-grey walls scarred at trolley height where the wall bumper rail is scratched and gouged, the paint touched up in rectangles that almost match; a hard welded-vinyl floor hazed with mop swirls, black heel scuffs multiplying near the door, the coving at the skirting yellowed. Flat cold light from the north window — shadowless and even, the voile diffusing it to a grey sheet that lies without warmth on the bed linen — doubled by the overhead fluorescent behind its prismatic diffuser, a few dead insects shadowed inside it; no contrast anywhere, nothing warm anywhere. Whites, sea-greens, cold greys. **Exit signage green. No red anywhere, no fire extinguisher in frame.** *(+ queue commune)*

**@HospitalCorridor** — A hospital corridor at night, seen at eye level along its length. A row of plastic chairs ganged on a steel beam against one wall, their seats gone shiny, one cracked through at the corner, the beam's paint chipped at the bolt heads; a door with a wired-glass window — the diamond mesh dark inside the glass, the pane smudged with hand grease at push height, the aluminium kick plate dull with scratches; a handrail running the wall, its vinyl worn grey along the top, the screw heads painted over; a linen trolley parked against the wall, its canvas bags sagging, one castor turned out; closed doors receding into the distance, each with its own dark wired pane. Two-tone green-grey walls scarred by decades of trolley strikes, the scars touched up in paint that no longer matches; a polished vinyl floor hazed with mop swirls, carrying the long smeared reflections of the ceiling lights all the way down. Overhead fluorescent tubes, greener than the rooms, one of them aged dimmer and greener than its neighbours, reflecting on the polished floor and on the glass of the door; the light is cold, even and faintly sickly, and it gives out before the end of the corridor, which sinks into gently underexposed darkness. Cold green-greys, deep shadow at the far end. **Exit signage green. No red anywhere.** *(+ queue commune)*

**@AnnaKitchen** — An elderly Russian widow's kitchen in New England, seen at eye level from a chair at the table. A small oilcloth-covered table, the oilcloth's flower pattern faded to a ghost of itself, worn white along the near edge where forearms have rested for forty years, one crescent-shaped burn scar where a pot was set down too soon; two mismatched chairs, their seats hollowed and their varnish gone matte; a cast-iron stove with a low flame behind its grate, the blacking rubbed thin on the proud edges, the chrome trim pitted, a battered kettle sitting off to one side of the top plate; a dresser crowded with mismatched china — gilt rims rubbed away by washing, glaze crazed into fine brown nets, one teapot mended long ago with a visible seam of glue — with framed photographs turned so their faces are not readable; lace at the window, yellowed, darned in two places with slightly whiter thread, browned along its fold lines; faded floral wallpaper darkened to amber above the stove, seams lifting, one patch replaced from a different roll that almost matches. Worn painted floorboards with a path scrubbed pale from door to stove, the paint gone entirely at the stove's feet. The stove and a single overhead bulb — low-wattage, under a shallow enamel shade, its cord ambered with age — are the only sources, amber and gold, very low: the grate lays a soft warm flicker across the floorboards, the bulb pools on the oilcloth, and the corners of the room dissolve into deep warm shadow, gently underexposed, nothing else lit. Deep warm shadows. **The stove is held in amber and gold, flame low, never a saturated ember, never a full flame in frame. No red anywhere.** *(+ queue commune)*

**@Restaurant** — A small old family-run Chinese restaurant in a New England port town at night, seen at eye level from the back of the room. Six formica tables with dark green cloths washed to a soft sheen and still showing their pressed fold lines, the formica edges chipped where the cloth corners lift; wooden chairs, mismatched across decades, their lacquer worn through on the backrest where hands pull them out; a lacquered service counter, the lacquer crazed into fine cracks and rubbed to bare wood on the corner everyone rounds, a worn abacus and a covered toothpick jar on top; a green-lit fish tank with a white tide-line of limescale at the waterline, algae creeping in the corners, its pump trailing a line of small bubbles, its glow laying a faint rippling green on the ceiling above it; a beaded curtain to the kitchen, the strands uneven with age, several restrung on fishing line, one gap where a strand is missing; paper lanterns in amber and brass, their paper sun-faded, one panel patched with almost-matching paper, the tassels furred with dust; a window onto a wet street with a roller blind half down, its pull-cord frayed, the lower glass fogged with condensation at the edges, the street beyond cold and blue with sodium reflections sliding on the wet asphalt. Dark linoleum floor worn to a grey path from the door to the counter. Warm low light from the lanterns and the counter — small tungsten pools on each green cloth — the fish tank throwing green, the street cold and blue beyond the glass. **No red anywhere: no red lanterns, no red tablecloths, no red menus, no red packaging.** *(+ queue commune)* *(⚠ Sert DEUX fois — séq. 2 heureuse, séq. 5 grise : ce prompt de lieu reste neutre-chaud ; la version grise se joue dans le style prompt vidéo, pas ici.)*

**@NoraBedroom** — A fifteen-year-old girl's small bedroom at night, seen at eye level from the doorway. A single bed with a rumpled dark quilt half pulled off the mattress, the fitted sheet escaping at one corner, the pillow dented and doubled over; a cluttered desk with a laptop closed, its lid clouded with fingerprints and the ghost outlines of peeled-off stickers, its charging cable kinked and mended with a turn of tape; school books in a leaning pile, dog-eared, their covers scuffed to blankness, a cold mug of tea ringed onto the topmost one; loose paper, a single earbud, a dead pen without its cap; a chair with clothes slung over the back — a hoodie, jeans inside-out — and more clothes dropped on the floor beside it; a window onto a back gallery and rooftops, condensation beaded along the bottom pane, dust felted on the sill, the catch painted stuck; a door to the hallway. Unmade, uncared for: dust along the skirting, a crumpled tissue by the bed, nothing put away. The only light is the cold blue-white of the closed laptop lid's glow — a thin seam of it rimming the desk edge and the nearest books — and the sodium orange of a street lamp through the window, lying in one skewed rectangle across the floorboards and the foot of the bed; the two temperatures never mix, and everything outside them falls into deep blue-black shadow, gently underexposed, the corners gone entirely. Deep blue-black shadows. No red anywhere. *(+ queue commune)*

**@BackGallery** — The rear wooden gallery of a New England triple-decker at night, seen from the gallery itself looking out. A painted wooden rail — grey over green over an older white, the layers flaking to bare silvered wood along the top where hands have rubbed it smooth — on turned balusters, two of them replaced with plain sticks; peeling deck boards with the grain raised, the nailheads standing proud and rusted, each one bleeding a small dark streak, gaps between the boards opening onto darkness; a washing line of grey-green cord sagging between two hooks, a few wooden pegs left clipped to it, one split; the galleries of the flats below and above visible as receding rails, the underside of the one above stained by years of drips; back yards and rooftops beyond — asphalt shingles, leaning fences, a shed with a tarpaulin roof — and harbour cranes far off against the sky. The boards still hold a thin sheen from earlier rain. Sodium street lamps from below and behind push a dull orange up-light that catches the underside of the gallery above and the flaking edges of the rail; the sky is a cold deep blue, nearly black at the zenith; and the kitchen window of the flat below throws one warm rectangle onto the boards, the only warm thing in frame. Everything outside these few sources falls to near-black, gently underexposed. No red anywhere. *(+ queue commune)*

**@Bathroom** — A small tiled family bathroom, seen at eye level facing the mirror above the basin. A plain rectangular mirror, its silvering blooming into small black spots along the bottom edge and one corner, a faint constellation of dried toothpaste specks near the basin; a basin with a chipped enamel edge — the chip showing dark metal — limescale trails running grey-white from both taps to the drain, the chrome of the crosshead taps worn to brass on the handles, a hard grey sliver of soap fused to the dish; a shower curtain pushed back, its folds greyed along the hem, one ring replaced with a twist of wire; white square tiles with grey grout, the grout darkened in the lines nearest the floor, one tile cracked corner to corner and left in place; a radiator with towels over it — the radiator's paint yellowed and blistered with rust at the valve, a rust drip-stain on the floor tile beneath, the towels thin, stiff and line-dried; a small frosted window, condensation gathered into slow drops at the bottom of the pane, the sealant greyed and pulling away, the sill's paint peeling in one clean arc. The floor tiles are dulled to matte along the path from door to basin. Flat cool light from the frosted window — soft, shadowless, grey — plus a single wall light above the mirror whose cooler glow flattens everything it touches; the room is even, cold and slightly dim, gently underexposed in the corners, nothing warm anywhere. Whites and cold greys. No red anywhere. *(+ queue commune)*

**@LibraryCorridor** — A corridor between tall wooden bookshelves in an old school library, seen at eye level down its length, the shelves running away on both sides and closing in. The shelves are dark varnished oak, their outer edges rounded and paled by a century of hands, the shelf lips worn to raw wood where books are dragged out, one high shelf visibly bowed under its load; the books themselves are only texture — cloth and cracked leather spines faded to blankness, some leaning into the gaps, some lying flat on top of the rows, all of it under a fine even dust. Worn parquet floor, the herringbone blocks rubbed matte grey along the exact centre line of the corridor, a few blocks lifted slightly proud, one replaced long ago in a lighter wood, old wax built up yellow against the shelf bases; brass rail lights along the shelf tops switched off, their brass tarnished brown, their small shades dusty; a study table with a chair at the near end, the table's edge worn round, its top marked with old ink blots gone pale and the fine scratches of decades, the chair's seat polished dark. A window at the far end throwing flat afternoon light straight down the corridor — a grey-white shaft with dust hanging almost motionless in it, laying a long dull gleam up the centre of the parquet and a bright rectangle on the floor at the end; the light gives out quickly to either side, so the shelf aisles hold deep soft shadow and the near end of the corridor sits gently underexposed. Deep shelf shadows, a bright rectangle at the end. **Exit signage green. No red anywhere. No readable book titles.** *(+ queue commune)*

**@Classroom** — ✂️ **SUPPRIMÉ le 26/08** (le plan 7.5 « école » n'existe plus ; ne pas générer).

**@NightBus** — The interior of a city bus at night, seen at eye level from a seat in the middle looking forward down the aisle. Worn moulded seats in grey-blue, the fabric pilled and rubbed shiny along the aisle edges, one seatback split and mended with a strip of grey tape, the plastic seat shells scratched and dulled; chrome poles worn cloudy at hand height, each carrying the ghost rings of stickers long peeled away; a ribbed rubber floor worn smooth and pale along the centre of the aisle, grit and dried footprints in the ribs, a flattened bottle cap trodden into it; condensation on the windows — beads running in slow trails, wiped arcs at shoulder height gone blurry again, drips gathering along the black rubber seals; the driver's area a dark silhouette far ahead behind a scratched perspex partition, black night beyond the glass with occasional street lamps sliding past as long smeared streaks of orange. Cold white ceiling strip lighting inside — one diffuser panel yellowed with age, dead moths shadowed inside another — flattening everything it touches, while the sodium orange washes through the fogged windows in slow passes, sliding along the poles and across the seat backs and dying between lamps, so the bus keeps sinking back into a gently underexposed gloom between each pass. **No red anywhere: no stop button lights, no red handrails.** *(+ queue commune)*

**@BusShelter** — A bus shelter at the far edge of a port town at night, seen at eye level from across the road. A steel and glass shelter, its powder-coated frame chipped to rust at every bolt head, the glass panels clouded with fine scratches and grime along their bottom edges — one panel cracked from a corner and left that way — with one bench of worn timber slats, the paint flaked to bare grey wood, the screw heads rusted proud; a blank white advertising light box with **no image and no lettering**, switched off, its acrylic face dusty, a thin drift of dead insects settled along the inside of its bottom edge, catching only the sodium; a leaning timetable pole, its display frame empty and fogged, its concrete footing cracked and tilted; a wet empty road, the asphalt patched in darker rectangles, holding one long gloss of rain; a chain-link fence sagging between leaning posts with a shred of plastic caught in it, and a dark warehouse behind, corrugated, with paler rectangles where signs were long since taken down; weeds gone to seed at the kerb, wet and bent. One sodium street lamp above throws a hard orange cone: it carves the shelter out of the dark, doubles itself in the shelter glass and again in the wet asphalt, rims the bench slats and the top of the fence — and everything outside it falls to near-black, deep and gently underexposed, the warehouse a mass, the road ending in nothing. Wet asphalt holding the reflection. **No red anywhere, no traffic light, no hydrant.** *(+ queue commune)*

**@RedHouseExterior** — A small old wooden fisherman's cottage at the dead end of a rough street at the edge of a port town at night, seen at eye level from up the street. **The cottage is painted deep barn red**, the clapboard weathered and peeling — paint lifting in stiff curls along the board edges, bare silvered cedar showing beneath, a rust streak bleeding down from every nailhead, one patch repainted long ago in a red that no longer quite matches; a low porch with checked and cracked posts, its two steps sagging and worn hollow in the middle; one window on the ground floor with a warm lamp burning behind it, the old glass faintly wavy, a thin curtain half drawn, the light ambering the peeling paint of the window surround; a sagging picket fence, pickets missing like teeth, one length held up with twisted wire, the gate hanging open on its lower hinge. The street either side is grey warehouse wall and cracked asphalt with no other colour anywhere — frost-heaved cracks with dead weeds in them, shallow puddles, the corrugated walls blank and dark. The lit window and one distant street lamp are the only sources: the window lays a warm patch across the porch boards and the fence pickets and reaches a little way into the street; the far sodium lamp puts one cold-orange edge on the wet asphalt behind; everything else falls to near-black, deep and gently underexposed. **The red of the cottage is the only red in the frame and it is fully saturated.** *(+ queue commune)*

**@RedHouseInterior** — The single downstairs room of a small old wooden cottage, seen at eye level from the doorway. **Every surface — walls, ceiling, the staircase, the inside of the door — is covered edge to edge in dense handwritten lines, in ivory paint and ink, layered over years**, some on the plaster directly, some on hundreds of sheets of paper pinned and pasted and overlapping. The layers show their ages: the oldest lines browned and sunk into the plaster, newer ones sitting proud in raised ivory paint, ink lines feathering where the plaster drank them; the papers are of every weight and yellowed unevenly, edges curled and lifting, some pinned with tacks rusting a halo into the sheet, some pasted flat and bubbled with the glue, overlapping like fish scales up the walls and across the ceiling boards; beneath it all the plaster is cracked and patched, and the writing runs straight over every crack and repair without stopping, up the staircase stringer, across each riser, over the door's panels and its old iron rim lock. A bare wooden floor of wide old boards, a ghost line of ancient paint at the edges, worn pale along the path from the door to the table, spotted here and there with small dried drips of ivory and ink; a single plain wooden chair, its seat polished dark, one stretcher mended with wire; a table scarred and stained with wax and ink, with a paraffin lamp burning on it — the brass gone amber, the chimney sooted at the lip, the flame trimmed low. **The writing is real handwriting in straight horizontal lines of word-shaped clusters, in an invented alphabet whose characters recur; unmistakably a script, but no script that exists and not one word readable in any language — never a scribble.** The lamp is the only source, warm, low, throwing the writing into raking relief — every raised line casting its own hair-thin shadow, the curled paper edges glowing at their rims — while the ceiling and the corners of the room fall away into deep warm darkness, gently underexposed. Warm reds and ambers. *(+ queue commune)*

**@Shed** — A cluttered dockside repair shed at night, seen at eye level from the doorway. A long workbench under an articulated lamp, nets hanging from hooks, spools of twine, tins, a vice, a wooden tool box, a paraffin heater, a small window black with night, plans and papers pinned across one wall. A single articulated bench lamp is the only light, hard and low, everything beyond falling to near-black. No red anywhere. *(+ queue commune)*

**@Docks** — A working fishing port at dawn in late November, seen at eye level from the quayside. Trawlers moored in a row, cranes and gantries, stacked crates and nets, bollards and chain, an ice house with its shutter half up, low mist on the flat water. Cold blue pre-dawn light with the first warm break at the horizon, sodium lamps still burning on the quay. **Feux de position éteints, no buoys, no red hulls, no red gloves. No red anywhere.** *(+ queue commune)*

---

# 3. LE GABARIT D'ANIMATION
*Cinema Studio 3.5 — genre, style, caméra, objectif, focale et diaphragme sont des **réglages**, pas du texte.*

```
Elements @Personnage(s) + @Lieu. 21:9, 1080p, {durée}s, sound on.
Genre {…} · Style Manual · Camera {…} · Lens {…}, {focale}mm, f/{diaph}.
Style prompt: {la lumière du film, en une phrase — sources motivées, contraste, tenue de la caméra}.

{Action, en nommant les @tags à chaque plan}. {N} shots, hard cuts.
[0-Xs] {plan 1}
HARD CUT
[X-Ys] {plan 2}
HARD CUT
[Y-Zs] {plan 3}
DIALOGUE [t1-t2s] @Tag, {ton} : "{réplique}"
{CROSS-FRAME RULES : « le seul … est @Tag », « chaque plan montre @Tag avec le visage exact
de la référence », « @Lieu est le même … dans les trois plans », « il marche dans une seule
direction pendant toute la durée »}.
AUDIO: {sources réelles, puis la musique ou son absence}.
```

**Réglages maison, valables pour tout le film**
| | Acte I (séq. 1-4) | Le monde gris (séq. 5-16, 18-19) | La maison rouge (séq. 17) |
|---|---|---|---|
| Genre | Drama | Noir | Drama |
| Camera | Fine Film | Fine Film | Fine Film |
| Lens | Anamorphic | Anamorphic | Anamorphic |
| Focale | 40 mm | 50 mm (85 mm sur les gros plans) | 28 mm |
| Diaph | f/2.8 | f/2 | f/1.4 |
| Style prompt | lumière d'or d'une seule fenêtre ou d'une seule lampe, chaude, matières vivantes, caméra posée | tout gris-bleu désaturé, sources sodium et néon uniquement, noirs profonds, caméra posée, aucun tremblement | rouge saturé plein cadre, une seule lampe à pétrole, très faible profondeur de champ |

**Négatif commun à tous les plans**
> visible camera rigs, cartoonish colors, blurred focus, on-screen text, subject looking at camera, slow motion, morphing objects, extra people in frame, modern branding, readable signage

---

# 4. LES SÉQUENCES — blocs prêts à coller

## SÉQ 1 — LE MATIN *(26 s, 4 plans)*
```
Elements @SamBefore + @Maeve + @NoraBefore + @MiloBefore + @Kitchen. 21:9, 1080p, 10s, sound on.
Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 40mm, f/2.8.
Style prompt: one low east window is the only source, warm gold, a hard bar of light across the
table with dust in it, deep shadow in the corners, camera locked off, no handheld shake.

A family morning in @Kitchen. Four shots, hard cuts.
[0-3s] Extreme close-up, high angle over a gas range. Two slices of bread blacken in a cast-iron
pan, smoke rising straight. A woman's hand turns them too late, snatches back. Her laugh, off.
HARD CUT
[3-6s] Medium shot. @Maeve barefoot at the sink, scraping the burnt toast, humming off-key.
@SamBefore enters behind her from the hall, coat open, salt on the shoulders, and lays both cold
hands on the back of her neck. She shrieks, elbows him, they both laugh. He takes the knife from
her and finishes the job.
DIALOGUE [4.5-6s] @Maeve, laughing: "You're a monster." @SamBefore, flat: "I know."
HARD CUT
[6-8s] Medium shot. @MiloBefore runs in in pyjamas and jumps onto the back of @SamBefore. He does not
turn around; he holds her with one hand out of pure habit and keeps scraping with the other.
@NoraBefore comes in, sits, watches the circus, rolls her eyes, smiles anyway.
HARD CUT
[8-10s] Insert on hands, then widening. @SamBefore pours @Maeve's coffee, stops three centimetres
from the rim, adds exactly half a sugar, stirs twice, sets the cup in front of her. He asks her
nothing. She does not look up — she puts out her hand and the cup is there.
The only four people in @Kitchen are @SamBefore, @Maeve, @NoraBefore and @MiloBefore, each with the exact
face of their reference. @Kitchen is the same kitchen in all four shots, same table, same four
mismatched chairs, same window direction. Nobody looks at the lens.
AUDIO: the pan, a short laugh, a radio low in the room, bare feet on tile, the knife, the coffee,
the spoon twice, the cup set down on wood, four voices overlapping. No music.
```
*Puis, en plan séparé (2 s) :* `Elements @Kitchen. High angle on the table, FOUR bowls and FOUR
chairs, the bar of window light across it, nobody in frame.` **⚠ Fichier à conserver : il sera
décliné en trois bols et une chaise vide pour la séq. 7.**

## SÉQ 16 — L'ABRIBUS *(27,5 s — le test du sandwich)*
```
Elements @Nora + @SamSDF + @BusShelter. 21:9, 1080p, 12s, sound on.
Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 50mm, f/2.
Style prompt: one sodium street lamp above the shelter is the only source, a hard orange cone,
everything outside it near-black, wet asphalt holding the reflection, camera locked off.

@Nora crosses to @SamSDF at @BusShelter and gives him her sandwich. Three shots, hard cuts.
[0-4s] Wide, eye level from across the road. @Nora small, x=30%, filling 25% of frame height,
stands at the edge of the sodium cone. @SamSDF seated on the bench inside the shelter, x=65%,
motionless, cropped by the frame at mouth height so no eyes are visible. She crosses the road
toward him — the first step is hers.
HARD CUT
[4-8s] Medium close-up, low angle, @SamSDF from the chest up, the frame cutting him at mouth
height so his eyes are never visible. He speaks. @Nora's hand enters frame holding a wrapped
sandwich. He takes it slowly and begins to eat.
DIALOGUE [4.5-6s] @SamSDF, a broken voice, rough with cold: "Got anything to eat?"
DIALOGUE [7-8s] @SamSDF, chewing, quiet: "Most people say no."
HARD CUT
[8-12s] Medium shot. @SamSDF raises one arm and points straight up the dark road. @Nora follows
the arm with her eyes, then walks out of the sodium cone into the black.
DIALOGUE [8.5-10.5s] @SamSDF: "Straight ahead. When you see red, you're there."
The only two people at @BusShelter are @Nora and @SamSDF. @SamSDF is cropped at mouth height in
every single frame he appears in, his eyes are never visible, not once. @Nora has the exact face
of her reference. @BusShelter is the same shelter in all three shots. The advertising light box
stays blank and unlit.
AUDIO: wind across the shelter glass, wet road, the paper unwrapping, chewing, a far-off foghorn.
No music.
NEGATIVE PROMPT: the man's eyes visible, the man's full face in frame, any red in frame, on-screen
text, lettering on the light box, other people, subject looking at camera, slow motion
```

## SÉQ 18 — LE DÉMASQUAGE *(le pivot du film)*
```
Elements @SamSDF + @Sam + @BusShelter. 21:9, 1080p, 12s, sound on.
Genre Noir · Style Manual · Camera Fine Film · Lens Anamorphic, 85mm, f/2.
Style prompt: the same single sodium lamp above the shelter, hard orange from above, deep crushed
blacks all around, wet asphalt, camera completely still.

A man takes off a disguise at @BusShelter. Three shots, hard cuts. No music at any point.
[0-4s] Extreme close-up, static. A hand enters frame and pulls the grey wool beanie off. Matted
hair beneath. The hand is large and calloused and the fingertips and nail beds are stained dark
blue-black with ink. The frame stays below the eyes throughout.
HARD CUT
[4-8s] Extreme close-up, static, the frame still cut at mouth height. The hand works under the
lower edge of the frame; the coarse grey beard comes away in one piece. The point where it lifts
from the skin is never in frame.
HARD CUT
[8-12s] Slow vertical pan upward, from the hands to the face. @Sam, the disguise gone, unwraps the
sandwich and eats. His shoulders go once. He is crying and he keeps eating.The hands in shots one and two are the
same hands. @BusShelter is the same shelter as the previous scene, same bench, same lamp, same
blank light box. No coat and no face in the same frame at any point.
AUDIO: the sodium lamp buzzing, wind, the beanie, the beard's adhesive giving way, paper, one
breath that catches. Silence otherwise. No music.
NEGATIVE PROMPT: the beard's edge lifting from the skin in frame, any red in frame, visible camera
rigs, on-screen text, other people, subject looking at camera, music
```

## SÉQ 17 — LA MAISON ROUGE *(l'orbite — 4 segments chaînés)*
```
Elements @Nora + @RedHouseInterior. 21:9, 1080p, 8s, sound on. ×4 segments.
Genre Drama · Style Manual · Camera Fine Film · Lens Anamorphic, 28mm, f/1.4.
Style prompt: one paraffin lamp is the only source, deep saturated warm red filling the whole
frame, extremely shallow depth of field, the written walls dissolving into streaks of ink,
camera at floor level, slow and continuous.

@Nora lies on the floor of @RedHouseInterior, laughing and crying at once, relieved.
Slow orbit around her, 9 degrees per second, lens 6 cm above the floor, one continuous move.
@Nora stays sharp, the written walls behind her stay far out of focus and read only as streaks.
The writing is never legible in any frame.
Segment 1 of 4, 0-8s. The last frame of this segment is the first frame of the next; identical
move, identical speed, identical aperture.
AUDIO: her breath breaking into laughter, then into crying, the lamp, nothing else.
The theme returns on solo piano, very far away.
NEGATIVE PROMPT: legible handwriting, readable words, on-screen text, any face other than hers,
sharp background, handheld shake, cuts inside the segment
```
*Raccords des 4 segments masqués par : le faisceau qui traverse l'objectif, **un battement de
paupières** (yeux fermés = images identiques), un souffle qui déplace une mèche.*

---

# 5. ORDRE DE PRODUCTION

| Étape | Quoi | Combien |
|---|---|---|
| 1 | Fiche **@SamBefore** (le visage pivot du film — l'homme propre) | 1 |
| 2 | Variantes en cascade : **@Sam** (⟵ @SamBefore), puis **@SamSDF** et **@Mender** (⟵ @Sam) | 3 |
| 3 | **@Maeve** puis **@MaeveIll** | 2 |
| 4 | **@Nora** puis **@NoraBefore** · **@Milo** puis **@MiloBefore** | 4 |
| 5 | **@Anna · @Mei · @Asha · @Fatiha** *(en parallèle)* | 4 |
| 6 | **Les 17 lieux, vides** *(en parallèle)* | 17 |
| 7 | Plans macro hors Éléments : les mains tachées d'encre · le col au fil rouge · la table à 4 bols | 3 |
| | **Total avant le premier plan du film** | **34 Éléments** |

**Puis** : les blocs d'animation séquence par séquence, chacun ne citant que des `@tags` déjà
sauvegardés. Comme le dit le pack : *« le même visage tient à travers les trois mondes depuis un
seul tag, sans chaîne de continuité à maintenir. C'est le saut d'un bon plan isolé à un vrai film. »*

⚠ **Les quatre séquences ci-dessus sont les modèles.** Les quinze autres suivent exactement le même
gabarit — à écrire une fois les 34 Éléments générés et validés, pour que chaque bloc cite des tags
qui existent vraiment.
