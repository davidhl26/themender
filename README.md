# THE MENDER

Court métrage — **Higgsfield Global Film Festival**
Dépôt de production : script, personnages, lieux, blocs de génération.

> **Rendu : 3 septembre, 23 h 59 PT.**
> Tout doit être généré à l'intérieur du projet Cinema Studio du festival.

---

## Le film en trois phrases

Après la mort de Maeve, Sam devient muet de chagrin.
Il fabrique un mythe — **le Rapiéceur** : un homme en manteau couvert d'écritures qui demande une petite chose, puis donne une raison de vivre — uniquement pour que sa fille Nora, 15 ans, en ait une.

**Elle ne le saura jamais.**

**3 blocs · 10 séquences · 66 plans · 5 min 31.**

---

## Par où commencer

| # | Ouvrir | Pourquoi |
|---|---|---|
| 1 | **[docs/RESUME-DES-PLANS.md](docs/RESUME-DES-PLANS.md)** | Les 66 plans en une lecture, avec l'intérêt de chaque scène entre parenthèses. **Commence ici.** |
| 2 | **[docs/SCRIPT-THE-MENDER.md](docs/SCRIPT-THE-MENDER.md)** | Le script. **C'est la vérité** — en cas de contradiction, il gagne. |
| 3 | **[docs/generations/videos/](docs/generations/videos/)** | Les 56 blocs vidéo à copier-coller dans Higgsfield, séquence par séquence. |
| 4 | **[docs/PROMPT-PACK-THE-MENDER.md](docs/PROMPT-PACK-THE-MENDER.md)** | Les fiches personnages (`@Sam`, `@Nora`, `@Anna`…) et leurs identifiants. |
| 5 | **[docs/generations/lieux/](docs/generations/lieux/)** | Les 19 lieux : image maîtresse + angles dérivés. |
| 6 | **[docs/FESTIVAL-HIGGSFIELD.md](docs/FESTIVAL-HIGGSFIELD.md)** | Les règles du festival. |

---

## Comment générer

**Les lieux d'abord, les personnages ensuite, les vidéos en dernier.**

1. **Un lieu = une image maîtresse, puis les angles dérivés** avec la maîtresse en référence et le paragraphe GEOMETRY recopié mot pour mot. Sans ça, le décor change entre deux plans.
2. **Un personnage = une planche** (gabarit trois panneaux). ⚠ Un panneau sans tête appliqué à un enfant déclenche le filtre NSFW de Higgsfield — deux panneaux, tous les deux avec la tête.
3. **Une vidéo = un bloc copié tel quel**, sans rien réécrire. Chaque bloc porte sa `start frame`, sa `LAST FRAME` et sa coupe (`⚠ COUPE`). Les coupes sont calculées : les respecter, sinon les raccords bégaient.

Les blocs sont en anglais **volontairement** — c'est la langue du moteur. Le français dans un corps de bloc est un défaut.

---

## Les règles qui ne se négocient pas

**RÈGLE ZÉRO — NORA N'APPREND JAMAIS QUE LE MENDER EST SON PÈRE.**
Elle ne le sait pas, ne le soupçonne pas, ne le devine pas. Aucune scène de soupçon, aucune question posée à Sam, aucune ambiguïté finale. Les frôlements — elle passe à côté de la preuve sans la voir — sont souhaitables ; la suspicion, jamais.
**Nous sommes les seuls témoins. C'est le film.**

| | Règle | En une ligne |
|---|---|---|
| **A** | Le mot | *story/stories* vit dans l'acte I, meurt avec Maeve, et revient **une seule fois** — dans sa bouche, plan 10.10. Ni synonyme (*tale, legend, myth*) entre les deux. |
| **B** | Le rouge | Quatre porteurs : l'écharpe de Maeve, le manteau, la maison rouge, ses écritures. **Rien de rouge sur Nora, jamais.** |
| **C** | La raison | Jamais formulée — **sauf une fois, chez Anna (4.5)** : « He gave me a reason to be alive without him. » |
| **D** | Le Mender | Jamais de visage. Le SDF est coupé à hauteur de bouche dans **chaque** image de la séquence 9. **À partir du plan 10.8, ses yeux sont visibles et le restent jusqu'au noir** — Nora est absente de toute la fin. |
| **E** | Universel | Aucune religion, aucun dieu, aucun lieu de culte. Des pays seulement. La ville n'est jamais nommée. |
| **F** | Les corps | @SamBefore/@Sam, @NoraBefore/@Nora, @MiloBefore/@Milo, @Maeve/@MaeveIll — **jamais mélangés.** Sam parle et rit dans l'acte I, puis se tait deux ans. |
| **G** | Concours | Aucun visage ni voix réels en entrée. Tout texte lisible (forum, miroir, carton) **composé en post, jamais généré.** L'écriture est une texture. |
| **H** | Aucun surnaturel | Trois mécanismes, trois explications matérielles montrées à l'image : le savon déposé à sec sur le miroir · la coïncidence chez Anna · **la peinture** des murs, chargée par l'ampoule que Nora éteint elle-même. |

## Ce qui reste ouvert

- [ ] Valider **@AnnaYoung** visuellement — tout le flashback russe en dépend.
- [ ] Trancher : rétablir ou non **le baiser du plan 1.3** (coupé au resserrage).
- [ ] Trancher : utiliser ou non **la dernière image de la vidéo du toast** comme image de départ du 1A.

---

## Notes de dossier

- `docs/generations/videos/VIDEO-SEQ-11.md` est **retiré** — la séquence 11 a fusionné dans la 10.
- Les `docs/generations/GEN-SEQ-*.md` des séquences 5, 7, 8, 9 et 10 sont **périmés** : ils portent une bannière 🗄 qui renvoie vers le document VIDEO-SEQ correspondant.
- `docs/archive-*` : versions longues antérieures. Conservées pour mémoire, plus à jour.
- `docs/FILM-SCRIPT-V1.md` : la toute première version. Historique.
