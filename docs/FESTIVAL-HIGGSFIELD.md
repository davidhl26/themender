# Higgsfield Global Film Festival — Règles assimilées

> Référence pour toutes les sessions de la semaine. Branche : `claude/higgsfield-film-festival-qf7jtp`.
> Sources : blog officiel Higgsfield + annonces X (@higgsfield_ai) via recherche web du 19/08/2026 —
> higgsfield.ai est **bloqué en accès direct depuis cet environnement** (proxy egress), donc la page
> `?tab=rules` n'a pas pu être lue mot à mot. David : vérifier dans le navigateur qu'aucune clause
> fine (droits, territoire, taxes) ne contredit ce résumé avant de soumettre.

---

## L'essentiel en une ligne

**Un court-métrage ≥ 3 minutes, 100 % généré dans le projet festival de Cinema Studio, soumis avant
le 3 septembre 23h59 PT, avec un post public sur YouTube/X/Instagram/Reddit. $1M de prix, 14 gagnants.**

---

## Calendrier officiel

> ⚠️ **DEADLINE REPOUSSÉE — vérifié le 01/09/2026.** Higgsfield a prolongé de 11 jours :
> **3 septembre → 14 septembre.** Et **le fuseau a changé avec** : c'était 23h59 **PT**,
> c'est désormais 23h59 **UTC**.
> **→ En heure de Miami : le 14 septembre à 19h59.** Compter en PT ferait arriver 7 h trop tard.
> ⚠ Source : deux recherches web concordantes du 01/09. **higgsfield.ai reste bloqué depuis
> l'environnement de dev — David doit confirmer dans son navigateur.**

| Étape | Date |
|---|---|
| Ouverture de la compétition | 10 août 2026 |
| ~~Deadline initiale~~ | ~~3 septembre 2026, 23h59 PT~~ |
| **Deadline de soumission** | **14 septembre 2026, 23h59 UTC** = **14/09 19h59 Miami** |
| Shortlist | 24 septembre |
| Délibération du jury | 25 septembre → 1er octobre |
| Annonce des gagnants | première semaine d'octobre |

⚠ **Les dates d'aval n'ont PAS bougé** dans les annonces trouvées (shortlist toujours au 24) :
le jury a donc dix jours de moins, pas nous.

⚠ **CONSÉQUENCE SUR LES PACKS ILLIMITÉS.** Les packs Higgsfield sont à durée limitée (7 jours).
**Ne pas les acheter avant de commencer réellement à générer** : un pack pris le 01/09 expire
le 08/09, six jours avant le rendu.

## Prix — $1,000,000, 14 gagnants

| Place | Montant |
|---|---|
| 1er | $500,000 |
| 2e | $200,000 |
| 3e | $100,000 |
| Audience Choice (prix du public, séparé du jury) | $100,000 |
| 10 mentions honorables | $10,000 chacune |

Un participant/équipe ne peut gagner **qu'un seul prix** au total.

## Règles du film

- **Durée : minimum 3 minutes.** Pas de maximum annoncé.
- **Genre et style : libres.** Toute langue (réelle ou fictive) **avec sous-titres OU voix-off en anglais**.
- **Format : MP4 ou MOV, jusqu'à 4K.**
- **Solo ou équipe de 4 max.** Tout utilisateur Higgsfield enregistré « in good standing » ;
  abonnement payant non requis pour soumettre.
- **Soumissions illimitées**, mais chaque entrée doit être un film autonome (interdit de découper
  une histoire en chapitres pour multiplier les entrées).

## Règles de création (les plus contraignantes)

1. **Tout doit être généré de zéro dans le projet festival de Cinema Studio** — le projet de
   soumission vit là « de la première génération au montage final ». Des générations antérieures
   peuvent servir de **références** uniquement.
2. **Aucun visage ni aucune voix de personne réelle en entrée — pas même les siens.**
   ⚠ Conséquence directe : la voix ElevenLabs clonée de David est **interdite** dans le film.
   Voix et musique passent par les outils audio de Higgsfield.
3. La fenêtre de génération = la période du concours (ouverte depuis le 10 août).

## Soumission minimale valable (« Minimal Viable Submission »)

Une entrée ne compte que si elle réunit **les deux** :
1. La vidéo finale **avec le watermark Higgsfield et le packshot** (appliqués par la plateforme à l'export).
2. **Un post public de cette même vidéo** sur Instagram, YouTube, X ou Reddit — le post doit rester
   public et visible **sans connexion** (compte privé/verrouillé = disqualification).

**Comment soumettre :** bouton « Create festival project » sur la page du festival, ou section
« Film Festival Contest » dans Cinema Studio → projet dédié où l'on génère les plans puis soumet
le film avec tous ses assets.

## Jugement

Critères : **réalisation (directing), qualité visuelle, son, originalité** — explicitement PAS le
nombre de followers. Jury annoncé : un quintuple oscarisé, l'ex-président de Walt Disney Animation
Studios (producteur exécutif de Toy Story), un lauréat du prix Turing, et Phedon Papamichael
(chef opérateur de Ford v Ferrari, The Pursuit of Happyness, The Trial of the Chicago 7).
Higgsfield a aussi open-sourcé les prompts de ses meilleurs films (Hell Grind, Zephyr, Mork) avec
breakdowns complets — à étudier comme référence de niveau attendu.

---

## Contraintes opérationnelles pour Claude Code (vérifiées le 19/08)

- **Crédits disponibles : ~1 116, plan Max** (`balance` MCP). À surveiller : un film de 3 min
  = ~30-36 clips de 5-6 s + itérations ; budgéter les regénérations.
- ⚠ **L'outil MCP `participate_in_contest` ne sert PAS au festival** — il inscrit un *site web*
  au concours d'apps Higgsfield. La soumission du film passe par Cinema Studio sur le site.
- ⚠ **À vérifier par David dans l'UI** (point décisif, non résolu par les sources) : est-ce que les
  générations lancées via le MCP Claude atterrissent dans le projet festival Cinema Studio, ou
  faut-il générer depuis l'UI du projet ? Dans le doute, la voie sûre est : créer le projet festival
  dans l'UI, et vérifier que chaque asset y apparaît. Le montage final doit se faire **dans**
  Cinema Studio (pas de ffmpeg local pour la version soumise).
- Aucun workflow « film festival » dans le catalogue MCP (vérifié) ; le skill local
  `scroll-film-studio` (sites web) ne s'applique pas ici — seule son expertise Seedance
  (image-clé → vidéo, cohérence de monde) est réutilisable.

## Plan de la semaine (à affiner avec David)

| Jour | Livrable |
|---|---|
| J1 (19/08) | Règles ✓ · concept : 2-3 pitchs, choix du film, script + découpage séquencier |
| J2 (20/08) | Monde visuel : direction artistique, images-clés des décors/personnages (références) |
| J3-J4 (21-22/08) | Génération des plans dans le projet festival (par actes, valider chaque acte) |
| J5 (23/08) | Son : voix-off/dialogues générés, musique, sound design |
| J6 (24/08) | Montage final dans Cinema Studio, sous-titres anglais, export watermark+packshot |
| J7 (25-26/08) | Post public (YouTube/X/Instagram/Reddit), soumission, campagne Audience Choice |

**Prochaine action (≤ 2 min) :** David crée le projet festival (« Create festival project » sur
higgsfield.ai) et confirme si les générations MCP y apparaissent — tout le pipeline de la semaine
en dépend.
