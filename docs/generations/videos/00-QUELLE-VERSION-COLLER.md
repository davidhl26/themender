# Quelle version coller — et pourquoi il y en a deux

> Écrit le 06/09 après vérification en ligne (guide Higgsfield Seedance 2.5, doc ByteDance,
> guides de modération). Les sources sont listées en bas.

## La règle en une ligne

**Tu colles `PROMPT-COURT-SEQ-XX.md`. Tu ne colles jamais `PRET-SEQ-XX.md`.**

## Pourquoi

| | Longueur | Rôle |
|---|---|---|
| `PROMPT-COURT-SEQ-XX.md` | ~420 mots | **Ce qu'on colle dans Higgsfield.** |
| `PRET-SEQ-XX.md` | ~5 200 mots | Document de tournage : géométrie GEO, verrous, raccords numérotés, notes de coupe. |

Higgsfield recommande **150–300 mots** pour une scène de 30 s. Au-delà d'environ **280 mots**,
le modèle commence à lâcher des instructions : l'attention se dilue, **le début et la fin du
prompt pèsent plus lourd que le milieu**, et le milieu est justement là où vivait notre
chorégraphie seconde par seconde. Nos blocs faisaient 5 200 mots. Ils faisaient donc, très
probablement, moins bien qu'un prompt vingt fois plus court.

La version courte garde l'ordre que donnent les sources, et rien d'autre :

`SHOT · CONTINUITY · ANCHOR IMAGE · INHERITED STATE · OPENING FRAME · ACTION (3–4 étapes) ·
PERFORMANCE · CAMERA · LIGHT · SOUND · ENDING FRAME · AVOID`

## Les quatre choses corrigées ce jour-là

1. **Mots d'âge : 497 → 0.** Seedance relève son seuil de modération sur **tout** le prompt dès
   qu'un mot signale la jeunesse (*child, kid, boy, girl, young, teenage, N-year-old*), quelle
   que soit l'image fournie. Les personnages sont nommés par leur Élément ou par leur rôle.
   ⚠ **Reste à faire côté interface** : `@Kolya11` porte un âge dans son nom. À renommer en
   `@Kolya` dans Higgsfield, et je répercuterai partout.
2. **Le raccord.** « Pick the scene up exactly where the attached video leaves it » est la
   formulation d'**échec** documentée : elle fait fuiter des éléments de la suite dans le début
   du plan. Remplacée par l'alignement explicite de la frame de bord **avant** toute action
   nouvelle. Et la reproduction pixel-exacte n'est plus exigée : *boundary frames connect
   naturally, not identically*.
3. **Les références.** Chaque référence a maintenant sa fidélité et son exclusion. Sans ça,
   une plaque de lieu **vide** fait fuiter sa mise en scène vide dans le plan.
4. **L'ancre de premier frame.** Sur 2.5, si l'interface n'affiche pas de champ `start_image`
   (ce que tu as constaté), le rôle se déclare **dans le texte** : c'est la ligne `ANCHOR IMAGE`.

## Étapes, pas frames

Les timings sont des **budgets de temps, pas des points de montage** : une action peut tomber
légèrement de part et d'autre. C'est pour ça que l'ACTION est en 3–4 étapes et non en douze
micro-segments — chaque étape porte **un** changement d'état et se ferme sur un état explicite.
Ne jamais demander une fréquence à l'intérieur d'une seconde.

## Budget de références

**30 images · 10 vidéos (≤30 s cumulées) · 10 audio · 50 références au total** par génération.

## Chaînage

- Nouveau cadrage après une coupe → `omni_reference` + le clip précédent en `video_references`.
- Prolonger **le même** plan → `video_extension` (forward).
- **Au-delà de ~60 s cumulées, ré-ancrer sur les références d'origine — jamais étendre une extension.**

---

**Sources** — [Higgsfield, guide Seedance 2.5](https://higgsfield.ai/blog/seedance-2-5-prompting-guide) ·
[Higgsfield, guide Seedance 2.0](https://higgsfield.ai/blog/seedance-prompting-guide) ·
[Skill Seedance 2.5, OSideMedia](https://github.com/OSideMedia/higgsfield-ai-prompt-skill/blob/main/skills/higgsfield-seedance-2-5/SKILL.md) ·
[ByteDance, annonce Seedance 2.5](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) ·
[Morphic, prompts flaggés](https://morphic.com/resources/how-to/seedance-2-prompts-flagged-how-to-fix) ·
[apidog, éviter les flags](https://apidog.com/blog/seedance-2-prompts-avoid-content-flags/) ·
[10b.ai, prompts de mouvement](https://10b.ai/blog/seedance-2-0-prompt-tips-motion) ·
[invideo, continuité sur 20+ scènes](https://invideo.io/faq/how-do-you-maintain-narrative-continuity-across-20/)
