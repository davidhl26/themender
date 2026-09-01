# PROMPT — Refonte visuelle & ergonomique : « Cockpit Sabari v2 »

> Rédigé le 17/08/2026 à la demande de David. À coller tel quel dans une session
> Claude Code sur ce repo pour lancer la refonte. Contexte complet dans CLAUDE.md.

## Rôle

Tu es directeur artistique ET ingénieur front. Tu refonds le **visuel** et
l'**ergonomie** du Cockpit Sabari — sans toucher au moteur, aux données ni au
backend JARVIS. Tu travailles par phases, avec **validation de David entre
chaque phase**. Consulte le skill `frontend-design` s'il existe, sinon
`dataviz` pour tout graphique.

## Contexte produit (non négociable)

- **Utilisateur unique** : David, TDAH, opérateur sous tension financière. Il
  consulte le matin en 30 secondes, souvent sur téléphone, entre
  Miami/Rabat/Paris/Tel Aviv.
- **Le produit a UN job** : afficher la date de rupture de trésorerie et
  comment chaque décision la déplace. Si l'écran d'accueil ne répond pas à
  « est-ce que je passe le mois ? » en 3 secondes, la refonte a échoué.
- **Stack existante** : Next.js 14 App Router, Tailwind (tokens
  `ink`/`hud`/`frost`/`signal` dans tailwind.config), Recharts,
  react-grid-layout v2, Zustand. **Interdits : nouvelle lib UI (pas de
  shadcn/MUI), lib d'animation lourde (pas de framer-motion), refonte du
  routing.**
- **Pages** : `/` (Bureau = canvas de modules), `/classique` (ancien dashboard
  complet), `/organisation` (tâches, routines, cartes mentales, chrono),
  `/saisie` (formulaires + connexions). Dock JARVIS 380 px à droite
  (`CopilotPanel`), orbe vidéo Higgsfield, arc reactor CSS.

## Lois du design (héritées, à respecter à la lettre)

1. **Le rouge (`#E5484D`) n'existe QUE pour la rupture de trésorerie.** Nulle
   part ailleurs — pas d'erreurs rouges, pas de baisse boursière rouge.
   L'ambre `signal` signale, le rouge condamne.
2. **Le héros, c'est la date de rupture + le verdict du mois.** Tout le reste
   lui est subordonné visuellement.
3. **Les montants négatifs et dates dépassées se signalent, ne s'atténuent
   jamais.**
4. **Chiffres en tabular figures** (IBM Plex Sans Condensed / JetBrains Mono
   selon la surface) — les colonnes de montants s'alignent.
5. **Jamais de total fusionné perso+entités affiché** (litige en cours —
   séparation des patrimoines visible).
6. **Pas de décor** : chaque élément structurel encode une information réelle.
7. **Mode Calme** (`.calme`) : zéro animation, zéro lueur — doit rester
   intégral après refonte. `prefers-reduced-motion` respecté partout.
8. **L'incertitude s'affiche** (IBKR ≈, HUD manquant) — jamais masquée.

## Diagnostic à traiter (l'état actuel a poussé par accrétion)

- **Deux dashboards** (`/` Bureau et `/classique`) se concurrencent : le
  verdict/rupture vit sur `/classique`, les tâches sur `/`. David doit choisir
  où regarder → décider d'UNE hiérarchie.
- **Trois esthétiques cohabitent** : instrument froid (classique), verre
  JARVIS (`.glass`, Bureau), formulaires bruts (Saisie). Unifier en UN système.
- **Saisie** est une page d'admin austère : longs formulaires, zéro
  hiérarchie, alors qu'elle contient des actions vitales (AutoPay, connexions,
  rappels).
- **Densité non maîtrisée** : le classique empile 10 sections à la même
  intensité visuelle ; l'œil TDAH ne sait pas où atterrir.
- **Mobile** : pile verticale correcte mais navigation 4 onglets + dock
  JARVIS = trop de niveaux ; le geste « je vérifie en 10 s dans l'ascenseur »
  n'est pas optimisé.

## La refonte

### Phase 1 — Système de design unifié (fondations)

- Formaliser les **tokens** dans tailwind.config : garder `ink` (noir-teal) +
  `hud` (cyan) + `signal` (ambre) + rouge-rupture ; ajouter une échelle
  d'élévation (3 niveaux de surface max), une échelle typo
  (display/num/body/label), des espacements 8pt.
- **Un seul langage de carte** : remplacer `.surface` ET `.glass` par un
  composant unique à 2 variantes (donnée froide / module interactif).
  Bordures, ombres, radius identiques partout.
- États systématiques : hover, focus visible (clavier), loading (skeleton
  discret, pas de spinner), erreur (ambre + texte, jamais rouge), vide (une
  ligne d'aide + une action).
- **Critère** : une capture de chaque page ne montre aucun style orphelin
  (audit des classes ad hoc) ; contraste AA vérifié sur les 6 paires de
  couleurs principales.

### Phase 2 — LA page unique (fusion Bureau + Classique)

- `/` devient l'unique dashboard : **bandeau-verdict fixe en tête** (hors
  grille, toujours visible) : « Je passe [mois] ? OUI/NON · Rupture le X ·
  J−n » + micro-courbe 13 semaines cliquable. Seul élément non déplaçable.
- Tout le reste du classique devient **modules du canvas** : courbe complète,
  disponibilités par patrimoine, dettes, échéances+agenda, décisions,
  inconnues §11 — ajoutés au registre react-grid-layout avec migration douce
  `softAdd` (motif existant, `PERSIST_VERSION`++).
- `/classique` disparaît (redirect 308) une fois la parité atteinte. Aucune
  info perdue : checklist de parité vérifiée section par section.
- Hiérarchie par défaut du canvas (ordre mobile aussi) : verdict →
  décisions/échéances → prochaine action → cash → tâches/chrono → bourse →
  mindmap → modules épinglés.
- **Critère** : depuis un téléphone, verdict + prochaine action + 1re échéance
  visibles sans scroller ; l'ancien contenu du classique accessible à 100 % ;
  C1–C6 de la Phase 1 du Bureau toujours verts (drag/figé/persistance/calme).

### Phase 3 — Saisie repensée en « Réglages & Données »

- Découper en onglets ou accordéons : **Comptes · Dettes · Flux · Burn ·
  Connexions · Rappels** — une section visible à la fois, ancre profonde par
  URL (`/saisie#dettes`).
- Chaque formulaire : valeurs actuelles affichées en clair AVANT le champ (je
  vois, puis je corrige), bouton d'enregistrement collant en bas de section,
  confirmation optimiste.
- Les actions critiques (AutoPay OFF, reconnexion Google expirée, rappels non
  testés) remontent en **bandeau d'état** en tête de page.
- **Critère** : mettre à jour un solde = 3 interactions max depuis n'importe
  où ; test Playwright du parcours.

### Phase 4 — Micro-interactions & voix

- Transitions d'entrée des modules ≤150 ms, uniquement translate/opacity
  (GPU), désactivées en Calme.
- Feedback JARVIS : pendant l'analyse, l'orbe pulse déjà — ajouter l'état dans
  le bandeau-verdict (point cyan discret) pour savoir qu'il travaille dock
  fermé.
- Toasts unifiés (une seule position, ambre/cyan), remplaçant les messages
  inline disparates.
- **Critère** : Lighthouse perf ≥ 90 mobile sur `/` ; aucune animation en
  `.calme` (audit automatisé existant à réutiliser).

### Ergonomie TDAH transverse (toutes phases)

- **Une action primaire par écran**, toujours au même endroit.
- Capture de tâche accessible en ≤ 2 interactions depuis toute page
  (raccourci N conservé, bouton visible sur mobile).
- Indices temporels ambiants conservés (WorldClock, J−n) ; les J−n ≤ 2
  passent en ambre plein.
- Ce qui n'est pas à l'écran n'existe pas : rien d'important à plus d'un
  scroll du verdict.

### Méthode & garde-fous

- Une PR de commits atomiques par phase ; **capture avant/après + court test
  Playwright par critère d'acceptation** ; David valide entre les phases — tu
  n'enchaînes JAMAIS deux phases sans son « validez ».
- Interdiction de casser : moteur (`engine.ts`), routes API, outils JARVIS,
  persistance du bureau, Basic Auth, mode Calme, formats monétaires
  (`fmtUSD`).
- Si un choix esthétique contredit une Loi du design, la Loi gagne — signale
  le conflit au lieu de trancher seul.
