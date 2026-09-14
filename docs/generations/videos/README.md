# THE MENDER — les vidéos

Onze fichiers utiles, et rien d'autre.

| Fichier | Ce que c'est |
|---|---|
| **`PROMPT-SEQ-01..10.md`** | **Ce qu'on colle dans Higgsfield.** 64 prompts, gabarit validé en vrai sur 1B, réglés Seedance 2.0 · 1080p · son ON. Chacun porte son tableau de réglages. |
| `PRET-SEQ-01..10.md` | Le document de tournage : géométrie GEO, verrous de continuité, raccords numérotés, notes de coupe. **Jamais collé** — c'est la source dont `scripts/prompt-seedance20.py` tire les prompts. |
| `00-ORDRE-DE-GENERATION.md` | Dans quel ordre générer, et quel clip attacher à quel plan. |
| `00-CE-QUI-BLOQUE-LA-GENERATION.md` | Les Éléments manquants sur le compte, les doublons à nettoyer, le budget. |
| `00-CONFLITS-DE-GEOMETRIE.md` | Les 110 conflits de géométrie relevés, et les dix qui demandent une décision de David. |

## Comment coller

1. Ouvre le `PROMPT-SEQ` de la séquence, règle l'interface d'après le tableau du plan.
2. Colle le texte entre les triples backticks, **rien d'autre**.
3. Remonte aux **deux premières lignes** (`MATERIALS`, `ROLES`) et **re-sélectionne chaque `@` dans le sélecteur** : un `@` collé en texte brut ne se lie à rien.

## Régénérer les prompts

```
python3 scripts/prompt-seedance20.py
```

Lit les `PRET-SEQ`, écrit les `PROMPT-SEQ`. La carte des noms d'Éléments réels vit dans
`scripts/elements-reels.py` — c'est là qu'on met à jour un nom renommé dans Higgsfield.
