# PROMPTS COURTS — SÉQUENCE 07

> ~300 mots par plan, l'ordre recommandé par Higgsfield et ByteDance.
> Le détail complet reste dans `PRET-SEQ-07.md` : géométrie GEO, verrous, raccords numérotés.
> **C'est CETTE version qu'on colle dans Higgsfield.** L'autre est le document de tournage.

## 7A — plans 7.1 + 7.2 + 7.3 « Elle cherche encore » *(12 s générées · 7,5 s au montage — trois plans, deux hard cuts, 3 s → 2,5 s → 2 s · Elements : @Nora + @BackGallery + @Kitchen — la boîte aux lettres est décrite dans le bloc, sans Élément · start frame : aucune)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 12 s |
| **Éléments** | @Nora + @BackGallery + @Kitchen |
| **`start_image`** | aucune |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — Three short shots on three different days.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (6C), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Sam: left third of frame, STANDING, x=32%, filling 74% of frame height. @Nora: right third of frame, STANDING, x=68%. Nothing in this list may be re-placed, re-lit or improved.
OPENING FRAME — Medium shot on the gallery, eye level, camera standing on the gallery about 1.5 m back from the rail and three-quarter to it, static, locked off. FLAT GREY OVERCAST MORNING.
ACTION in 4 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-2.5s] Starting positions, held until described otherwise: the painted rail crosses the frame from the lower left foreground toward mid-frame, its top rubbed to bare grey wood at x=45%; [2.5-5.0s] Starting positions, held until described otherwise: the mailbox centred at x=48%, filling 40% of frame height, its little door hanging open and down, the dark empty inside of it turned toward camera, the weather-checked grey post below it; [5.0-7.5s] She looks along the street far below in one direction, then turns her head and looks along it the other way. [7.5-10.0s] Starting positions, held until described otherwise: @Nora SEATED alone at the middle table at x=45%, three-quarter to camera, filling 60% of frame height, charcoal hoodie, hood down, the chipped off-white plate in front of her with a little food left on it, the steel fork in her right hand.
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — One geometry by night and one by day, never mixed.
SOUND — None. Not a word anywhere in this generation. Nobody speaks and nobody mouths words. SFX only.
ENDING FRAME, the state this shot hands over — @Nora at the kitchen table, alone, eyes back down on the plate, the fork in the food, the window above the cold range a flat white rectangle behind her, the three empty chairs pushed in.
AVOID — visible camera rigs, cartoonish colors, blurred focus on her, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, readable lettering, a name plate on the mailbox.
```

## 7B — plans 7.4 + 7.5 « Elle ne regarde plus » *(10 s générées · 3,5 s au montage — deux plans, un hard cut, 1,5 s → 2 s · Elements : @Nora + @BackGallery + @NoraBedroom — la boîte aux lettres est décrite dans le bloc, sans Élément · start frame : aucune)*

**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**

| | |
|---|---|
| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |
| **durée** | 10 s |
| **Éléments** | @Nora + @BackGallery + @NoraBedroom |
| **`start_image`** | aucune |
| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. **Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |

> Si l'interface Seedance 2.5 n'affiche **pas** de champ `start_image` : joins l'image en référence ordinaire — la ligne ANCHOR IMAGE du prompt lui donne déjà son rôle de premier frame.

> ⛔ Tu ne copies QUE le texte entre les triples backticks. Ni le titre, ni le tableau.

```
SHOT — @Nora comes home along her back gallery in the evening and walks straight past the mailbox without seeing it.
CONTINUITY — VIDEO 1 is an earlier shot of the same film (7A), IN A DIFFERENT PLACE: rendering reference only. TAKE its film stock, grain, skin and fabric rendering, focus behaviour, highlight roll-off. DO NOT TAKE its light, palette, exposure, composition or framing.
INHERITED STATE, ALREADY TRUE AT FRAME ONE — @Nora: centre of frame, SEATED, x=45%, filling 60% of frame height. Nothing in this list may be re-placed, re-lit or improved. THIS IS AN ACQUIRED STATE, NOT AN ACTION TO PLAY: whatever brought the bodies and the props here has already happened in the attached video and must NOT be performed again.
OPENING FRAME — Wide shot along the gallery walkway, eye level, camera standing on the gallery looking along it, static, locked off. SODIUM EVENING.
ACTION in 3 stages, timings are budgets not edit points, each stage ends on the state the next one starts from — [0.0-1.3s] Frame contents, with the walk already under way: the empty walkway runs across and away from camera, the flaking painted rail SCREEN-LEFT, the receding rails of the flats above and below, the empty washing line overhead, the shut door back into the flat in the wall SCREEN-RIGHT at x=78%, the cold near-black sky beyond the rail. [1.3-2.7s] Nobody speaks. [2.7-4.0s] She keeps walking screen-right at the same pace and reaches the shut door of the flat at x=78%, her back to camera;
PERFORMANCE — Nobody performs an emotion here.
CAMERA — Anamorphic 50 mm f/2 equivalent.
LIGHT — One geometry by night and one by day, never mixed.
SOUND — None. Not a word anywhere in this generation. Nobody speaks and nobody mouths words. SFX only.
ENDING FRAME, the state this shot hands over — The back of her head and her nape above the dark quilt, absolutely still but breathing, her face away from camera, the skewed sodium rectangle out of focus behind her, the room black around it.
AVOID — visible camera rigs, cartoonish colors, blurred focus, on-screen text, subtitles, captions, burned-in text, karaoke lyrics, readable lettering, a name plate on the mailbox.
```
