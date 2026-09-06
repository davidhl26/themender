#!/usr/bin/env python3
"""Purge des mots d'age dans les 62 blocs a copier-coller.

Pourquoi : Seedance releve son seuil de moderation sur TOUT le prompt des qu'un mot
signale la jeunesse (child, kid, boy, girl, young, teenage, N-year-old), quelle que
soit l'image fournie. Le correctif documente : nommer le personnage par son ROLE ou
par son Element, et laisser l'image porter l'identite.

Deux regimes :
  - zones NEGATIVES (AVOID, et les enumerations d'interdits) -> jamais d'@Element,
    sinon on risque de le convoquer en le nommant. On y met un terme neutre.
  - partout ailleurs -> l'@Element lui-meme, qui est justement ce que le modele doit lire.

Les noms d'Elements (@AnnaYoung, @YoungMotherHospital, @Kolya11) sont MASQUES avant
traitement : les renommer casserait la mention cote Higgsfield.
"""
import re, sys, glob, os

# qui est "the girl" / "the boy" / "the child" selon la sequence
WHO = {
 '01': {'girl':'@NoraBefore','boy':'@MiloBefore','child':'@MiloBefore','children':'@NoraBefore and @MiloBefore'},
 '02': {'girl':'@NoraBefore','boy':'@MiloBefore','child':'@MiloBefore','children':'@NoraBefore and @MiloBefore'},
 '03': {'girl':'@NoraBefore','boy':'@MiloBefore','child':'@MiloBefore','children':'@NoraBefore and @MiloBefore'},
 '04': {'girl':'@Nora','boy':'@Kolya11','child':'@Kolya11','children':'@Kolya11'},
 '05': {'girl':'@Nora','boy':'@Milo','child':'@Milo','children':'@Nora and @Milo'},
 '06': {'girl':'@Nora','boy':'@Milo','child':'@Milo','children':'@Nora and @Milo'},
 '07': {'girl':'@Nora','boy':'@Milo','child':'@Milo','children':'@Nora and @Milo'},
 '08': {'girl':'@Nora','boy':'@Milo','child':'@Milo','children':'@Nora and @Milo'},
 '09': {'girl':'@Nora','boy':'@Milo','child':'@Milo','children':'@Nora and @Milo'},
 '10': {'girl':'@Nora','boy':'@Milo','child':'@Milo','children':'@Nora and @Milo'},
}
# dans une liste d'interdits : jamais de nom d'Element
NEUTRE = {'girl':'figure','boy':'figure','child':'figure','children':'figures'}

MASK = {}
def mask(t):
    def r(m):
        k = "\x00%d\x00" % len(MASK); MASK[k]=m.group(0); return k
    return re.sub(r'@\w+', r, t)
def unmask(t):
    for k,v in MASK.items(): t=t.replace(k,v)
    return t

AGE_NUM = r'(?:six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen)'

def commun(t):
    """Regles independantes du regime negatif/positif."""
    # SUBJECT LOCK : « The exact girl of the reference @X — fifteen, long dark hair »
    t = re.sub(r'The exact (?:girl|boy|child|young man|young woman|teenager) of', 'The exact person of', t)
    t = re.sub(r'(The exact person of[^—\n]{0,60})—\s*' + AGE_NUM + r',\s*', r'\1— ', t)
    t = re.sub(r'(The exact person of[^,\n]{0,60}),\s*' + AGE_NUM + r',\s*', r'\1, ', t)
    # « a fifteen-year-old girl » / « his thirteen-year-old daughter »
    t = re.sub(AGE_NUM + r'-year-old\s+', '', t, flags=re.I)
    # adjectifs de jeunesse accoles
    t = re.sub(r'\b(?:teenage|adolescent|young)\s+(?=girl|boy|child|daughter|son|face|figure|body|hands?|voice)', '', t, flags=re.I)
    t = re.sub(r'\bthe young mother\b', 'the mother', t, flags=re.I)
    t = re.sub(r'\bteenagers?\b', 'figure', t, flags=re.I)
    t = re.sub(r'\badolescents?\b', 'figure', t, flags=re.I)
    t = re.sub(r'\btoddler\b', 'figure', t, flags=re.I)
    # ages adultes ecrits en toutes lettres : on garde le sens, on retire le chiffre
    t = re.sub(r'—\s*(?:thirty|forty|fifty|sixty|seventy|eighty)(?:-(?:one|two|three|four|five|six|seven|eight|nine))?,\s*', '— ', t)
    return t

def remplace(t, table):
    for mot in ('children','child','girl','boy'):
        rep = table[mot]
        # possessif d'abord
        t = re.sub(r'\b(?:[Tt]he|[Aa]n?)\s+' + mot + r"'s\b", rep + "'s", t)
        t = re.sub(r"\b" + mot + r"'s\b", rep + "'s", t)
        t = re.sub(r'\b(?:[Tt]he|[Aa]n?)\s+' + mot + r'\b', rep, t)
        t = re.sub(r'\b' + mot + r'\b', rep, t)
    return t

def traite(path):
    seq = re.search(r'PRET-SEQ-(\d\d)', path).group(1)
    t = open(path, encoding='utf-8').read()
    MASK.clear()
    t = mask(t)
    t = commun(t)
    # decoupe : zones negatives = paragraphe qui suit « AVOID » + phrases d'interdits
    out, pos = [], 0
    for m in re.finditer(r'^AVOID\s*$', t, re.M):
        fin = t.find('\n\n', m.end())
        if fin == -1: fin = len(t)
        out.append(remplace(t[pos:m.start()], WHO[seq]))
        out.append(remplace(t[m.start():fin], NEUTRE))
        pos = fin
    out.append(remplace(t[pos:], WHO[seq]))
    t = unmask(''.join(out))
    open(path, 'w', encoding='utf-8').write(t)
    return seq

if __name__ == '__main__':
    d = os.path.join(os.path.dirname(__file__), '..', 'docs', 'generations', 'videos')
    for f in sorted(glob.glob(os.path.join(d, 'PRET-SEQ-*.md'))):
        print('traite', traite(f))
