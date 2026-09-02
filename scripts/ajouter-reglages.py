# -*- coding: utf-8 -*-
"""David, 02/09 : \"il y a pas start image sur ce prompt\".

Il avait raison. Le start frame, les Elements et la duree vivaient dans le TITRE
markdown, au-dessus de la fence -- donc perdus des qu'on copie le texte du bloc.
La promesse \"un bloc = tout\" etait fausse sur le seul point qui compte au
moment de cliquer.

Ce script pose un ENCADRE DE REGLAGES juste au-dessus de chaque fence :
- la duree, prise dans le FORMAT MODE du bloc (la source qui fait foi) ;
- les Elements et le start frame, pris dans le titre (trois formats de titre
  coexistent dans le corpus, les trois sont parses) ;
- le role de media a utiliser, qui n'est PAS le meme selon les trois cas.
Idempotent.
"""
import re, pathlib
D = pathlib.Path('/home/user/site-web-callbot.ai/docs/generations/videos')
MOVERS = {'10D-2','10F-1','10F-2','10F-3','10F-4'}

def duration(blk, title):
    m = re.search(r'One (?:single continuous uncut )?take,? (?:of )?(\d+(?:\.\d+)?) seconds', blk)
    if m: return m.group(1)
    m = re.search(r'\((\d+(?:,\d+)?)\s*s\b', title)
    return m.group(1) if m else None

def elements(title):
    """Tous les @ du titre, dans l'ordre. Robuste aux trois formats de titre du
    corpus et aux parentheses qui cassaient la lecture par prefixe."""
    seen = []
    for t in re.findall(r'@(\w+)', title):
        if t not in seen:
            seen.append(t)
    return ' + '.join('@' + t for t in seen) if seen else "aucun \u2014 ce plan ne charge aucun \u00c9l\u00e9ment"

def startframe(title):
    if re.search(r'pas de start frame', title, re.I):
        return "aucune \u2014 ce plan d\u00e9marre sans image de d\u00e9part"
    m = re.search(r'start frames?\s*:?\s*([^\u00b7)]+)', title)
    return m.group(1).strip().rstrip('\u00b7').strip() if m else None

n = 0
for p in sorted(D.glob('PRET-SEQ-*.md')):
    s = p.read_text(encoding='utf-8')
    # on retire un ancien encadre pour pouvoir relancer
    s = re.sub(r"\n\*\*RÉGLAGES —.*?\*Le texte à coller commence sous cette ligne\.\*\n", "", s, flags=re.S)
    parts = re.split(r'(?m)^(#{2,3} VIDÉO .*)$', s)
    out = [parts[0]]
    for i in range(1, len(parts), 2):
        title, body = parts[i], parts[i+1]
        code = re.match(r'#{2,3} VIDÉO ([0-9A-Za-z-]+)', title).group(1)
        fen = re.search(r'```\n(.*?)\n```', body, re.S)
        if not fen:
            out.append(title + body); continue
        blk = fen.group(1)
        dur, els, sf = duration(blk, title), elements(title), startframe(title)

        if code in MOVERS:
            media = ("| **mode** | `video_extension` · `extension_mode: forward` |\n"
                     "| **vidéo à prolonger** | le segment précédent |\n"
                     "| ⚠ | **Un seul mouvement découpé — le raccord doit être invisible.** "
                     "À défaut de `video_extension` : `start_image` = la dernière frame exacte du segment précédent. |")
        elif 'NO VIDEO IS ATTACHED' in blk:
            media = (f"| **`start_image`** | {sf or '—'} |\n"
                     "| **`video_references`** | *aucune — c'est une tête de chaîne* |")
        else:
            media = (f"| **`start_image`** | {sf or '—'} |\n"
                     "| **`video_references`** | le clip précédent — pour le grain, la lumière et la peau. "
                     "**Jamais sa dernière frame en `start_image`** : le cadrage n'est pas le même |")

        box = (f"\n**RÉGLAGES — à saisir dans l'interface AVANT de coller le texte**\n\n"
               f"| | |\n|---|---|\n"
               f"| **modèle** | Seedance 2.5 · 21:9 · 1080p · bitrate **high** · **sound off** |\n"
               f"| **durée** | {dur or '—'} s |\n"
               f"| **Éléments** | {els or '—'} |\n"
               f"{media}\n\n"
               f"*Le texte à coller commence sous cette ligne.*\n")
        out.append(title + box + body)
        n += 1
    p.write_text("".join(out), encoding='utf-8')
print(f"encadre pose sur {n} blocs")
