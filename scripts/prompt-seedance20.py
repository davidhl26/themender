#!/usr/bin/env python3
"""Les 62 prompts, au gabarit valide sur 1B, pour Seedance 2.0 en 1080p.

Ce gabarit est celui qui a marche en vrai le 06/09 :
  - toutes les mentions « @ » sur les DEUX PREMIERES LIGNES (MATERIALS puis ROLES),
    parce qu'un « @ » colle en texte brut ne se lie a rien : il faut le choisir dans
    le selecteur, et cinq selections au meme endroit valent mieux qu'une chasse ;
  - chaque materiau declare CE QU'IL FAUT EN PRENDRE et CE QU'IL NE FAUT PAS ;
  - l'AUDIO de la video attachee est explicitement exclu — sans ca @maeva rejouait
    « I think I burned the toast », la replique du plan precedent ;
  - les repliques sont COMPTEES et le silence qui les precede est DECLARE, sinon le
    modele comble le vide avec ce qu'il entend ;
  - l'action est en 3-4 ETAPES, chacune fermee sur un etat explicite.

Seedance 2.0 : duree 4-15 s (plafond dur), 1080p, pas de video_extension —
le chainage passe donc par start_image + video_references, jamais par une extension.
"""
import re, glob, os, importlib.util

spec = importlib.util.spec_from_file_location('er', os.path.join(os.path.dirname(__file__), 'elements-reels.py'))
er = importlib.util.module_from_spec(spec); spec.loader.exec_module(er)
CARTE = {k.lower(): v for k, v in er.CARTE.items()}
NOM = er.NOM

def reel(nom):
    """Nom exact sur le compte, ou None si l'Element n'existe pas encore.

    La carte fait autorite : elle a ete relevee sur le compte le 06/09. Un nom absent
    de la carte est un Element qui n'existe pas, pas un nom a supposer valide."""
    return CARTE.get(nom.lower())

def affiche(nom):
    r = reel(nom)
    if r and r.lower() in NOM:
        return NOM[r.lower()]
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', nom).upper()

def sect(b, start, stop=r'\n\n'):
    m = re.search(start + r'.*?(?=' + stop + r')', b, re.S | re.M)
    return re.sub(r'\s+', ' ', m.group(0)).strip() if m else ''

def phrases(txt, n):
    out = []
    for part in re.split(r'(?<=[.!?])\s+(?=[A-Z@\[])', txt):
        out.append(part)
        if len(out) >= n: break
    return ' '.join(out)

def clip(txt, mots):
    """Des phrases entieres jusqu'au budget : une instruction tronquee est lue de travers."""
    txt = txt.strip()
    if len(txt.split()) <= mots: return txt
    pris, n = [], 0
    for s in re.split(r'(?<=[.;!?])\s+', txt):
        k = len(s.split())
        if pris and n + k > mots * 1.15: break
        pris.append(s); n += k
        if n >= mots: break
    return ' '.join(pris).strip()

AUDIO_EXCL = ("TAKE NOTHING OF ITS AUDIO: not its dialogue, not its voices, not one line spoken in it. "
              "Every line heard in it belongs to the previous shot and MUST NEVER BE HEARD AGAIN HERE.")

# Seedance 2.0 plafonne a 15 s. 10J en fait 19 : c'est un montage de cinq micro-plans
# dans cinq lieux, on le coupe sur ses propres frontieres de SHOT plutot que dans une action.
# Les references de chaque morceau sont DECLAREES, pas devinees : un lieu se nomme en prose
# dans la choregraphie, jamais par une mention, donc aucune heuristique ne le retrouve.
SPLITS = {
    '10J': [('10J-1', (1, 2), 9.0, 'la maison rouge : il pose la premiere ligne, puis la piece entiere est ecrite',
             ['Sam', 'RedHouseInterior']),
            ('10J-2', (3, 4), 6.0, "la cuisine d'Anna puis le restaurant : il demande, on accepte",
             ['Sam', 'Anna', 'Mei', 'Fatiha', 'Asha', 'AnnaKitchen', 'Restaurant']),
            ('10J-3', (5, 5), 4.0, 'le couloir de la bibliotheque : le manteau quitte derriere le chariot',
             ['Sam', 'Mender', 'LibraryCorridor'])],
}

def refs_bruts(b):
    m = re.search(r'^ACTIVE REFERENCES\n(.*?)(?=\n\n)', b, re.S | re.M)
    return m.group(1) if m else ''


def couper(b, shots):
    """Ne garde du FRAME MAP que les SHOT demandes, et ramene leurs timings a zero."""
    m = re.search(r'(FRAME MAP & CHOREOGRAPHY[^\n]*\n)(.*?)(?=\nSUBJECT LOCK|\nCROSS-FRAME|\nLAST FRAME)', b, re.S)
    if not m: return b
    lo, hi = shots
    blocs = re.split(r'\n(?=SHOT \d+ \[)', m.group(2))
    gardes, t0 = [], None
    for bl in blocs:
        n = re.match(r'SHOT (\d+) \[', bl)
        if not n or not (lo <= int(n.group(1)) <= hi): continue
        if t0 is None:
            d = re.search(r'\[([\d.]+)-', bl)
            t0 = float(d.group(1)) if d else 0.0
        gardes.append(bl)
    if not gardes: return b
    txt = '\n'.join(gardes)
    def recale(x):
        a, z = float(x.group(1)) - t0, float(x.group(2)) - t0
        return '[%.1f-%.1fs]' % (max(a, 0), max(z, 0))
    txt = re.sub(r'\[([\d.]+)-([\d.]+)s\]', recale, txt)
    return b[:m.start(2)] + txt + b[m.end(2):]


def construire(b, nom_plan, restreint=None):
    L = []

    # ---- 1. MATERIALS : toutes les mentions, et rien qu'elles ------------------
    refs = sect(b, r'^ACTIVE REFERENCES\n', r'\n\n')
    elts, manquants = [], []
    for e in re.findall(r'@(\w+):', refs):
        # Sur un plan coupe, on ne joint QUE les references que le morceau utilise vraiment :
        # attacher un lieu qu'on ne filme pas, c'est l'inviter a fuir dans l'image.
        if restreint is not None and e.lower() not in restreint: continue
        r = reel(e)
        (elts if r else manquants).append((e, r))
    vu = set(); uniq = []
    for x in elts:
        if x[1] not in vu:
            vu.add(x[1]); uniq.append(x)
    elts = uniq

    cont_h = re.search(r'^CONTINUITY REFERENCE([^\n]*)\n(.*?)(?=\n\n)', b, re.S | re.M)
    entete, corps = (cont_h.group(1), re.sub(r'\s+', ' ', cont_h.group(2))) if cont_h else ('', '')
    prev = re.search(r'\(([\dA-Za-z.\-]+)\)', corps)
    prev = prev.group(1) if prev else ''
    tete_de_chaine = 'No video is attached' in corps or 'NO VIDEO IS ATTACHED' in entete

    mat = []
    if not tete_de_chaine:
        mat.append("@video1 is the shot immediately before this one (%s)." % (prev or 'the previous shot'))
        mat.append("@image1 is the last frame of that shot and IT IS THE FIRST FRAME OF THIS GENERATION.")
    else:
        mat.append("@image1 IS THE FIRST FRAME OF THIS GENERATION. No previous clip is attached: this shot is the "
                   "head of its chain and sets the light, the grain and the skin rendering the following shots match.")
    LIEUX = {'kitchen-1','quay','restaurant','hospitalroom','hospitalcorridor','annakitchen','norabedroom',
             'backgallery','bathroom','librarycorridor','nightbus','busshelter','redhouseexterior',
             'redhouseinterior','annakitchenpast','russianhospitalcorridor','russiannightstreet','russiancourtyard'}
    for e, r in elts:
        if r.lower() in LIEUX:
            mat.append("@%s is %s, one of the places this shot happens in." % (r, affiche(e))
                       if sum(1 for _, q in elts if q.lower() in LIEUX) > 1
                       else "@%s is THE PLACE THIS SHOT HAPPENS IN." % r)
        else:
            mat.append("@%s is %s." % (r, affiche(e)))
    L.append('MATERIALS — ' + ' '.join(mat))

    # ---- 2. ROLES : ce qu'on prend de chaque materiau, ce qu'on n'en prend pas --
    roles = []
    if not tete_de_chaine:
        if 'IN A DIFFERENT PLACE' in corps or 'different place' in corps:
            roles.append("From the attached video take ONLY the film stock, the grain structure, the way skin and "
                         "fabric resolve, the focus behaviour and the highlight roll-off. DO NOT TAKE its light, its "
                         "palette, its exposure, its composition or its framing, and " + AUDIO_EXCL)
        else:
            roles.append("From the attached video take the light level and direction, the grain, the skin rendering "
                         "and the way the camera behaves. TAKE NO FRAMING FROM IT beyond the first instant, and " + AUDIO_EXCL)
    roles.append("From the first-frame image take the opening composition and the exact position, pose and prop state "
                 "of everything in it; take nothing else from it — no border, no backdrop, no empty-room staging, "
                 "no reference layout.")
    if elts:
        noms = ', '.join(affiche(e) for e, r in elts if r.lower() not in LIEUX) or 'the references'
        noms += ' and the place reference'
        roles.append("From %s take identity, face, build, wardrobe, architecture and materials exactly as the "
                     "reference gives them; take none of their pose, framing, lighting or staging." % noms)
    L.append('ROLES — ' + ' '.join(roles))

    # ---- 3. le plan lui-meme ---------------------------------------------------
    scene = sect(b, r'^SCENE CONTEXT\n').replace('SCENE CONTEXT', '').strip()
    L.append('SHOT — ' + clip(phrases(scene, 1), 34))

    if not tete_de_chaine:
        herite = sect(b, r'HANDOFF — THE EXACT STATE THIS SHOT INHERITS')
        a_herite = 'WHERE THIS SHOT LEAVES' in herite
        if 'CAMERA IS ALREADY MOVING' in corps or 'MID-MOVEMENT' in entete:
            L.append('CONTINUITY — THE CAMERA IS ALREADY MOVING at the boundary. ALIGN THE BOUNDARY FIRST: start on '
                     'that motion already underway, same speed, same line, no ease-in and no restart, then carry it '
                     'on. One single move across both clips.')
        else:
            ou = 'the INHERITED STATE line below' if a_herite else 'the first-frame image'
            L.append('CONTINUITY — ALIGN THE BOUNDARY BEFORE ANYTHING NEW HAPPENS: this clip opens on %s exactly, '
                     'everything in it already true and nothing replayed, and only then does the action begin. '
                     'It must CONNECT NATURALLY, NOT IDENTICALLY.' % ou)
        if a_herite:
            pos = re.search(r'WHERE THIS SHOT LEAVES EACH BODY.*', herite).group(0).split('other bodies: ')[-1]
            L.append('INHERITED STATE, ALREADY TRUE AT FRAME ONE — ' + clip(pos, 40))

    ff = sect(b, r'FIRST FRAME AND SPATIAL BLOCKING')
    L.append('OPENING FRAME — ' + clip(ff.replace('FIRST FRAME AND SPATIAL BLOCKING', '')
             .replace('The generation opens on this exact frame:', '').strip(), 30))

    fm = re.search(r'FRAME MAP & CHOREOGRAPHY[^\n]*\n(.*?)(?=\nSUBJECT LOCK|\nCROSS-FRAME|\nLAST FRAME)', b, re.S)
    if fm:
        segs = re.findall(r'^\[([\d.]+)[^\]]*\]\s*([^\n]+)', fm.group(1), re.M)
        if segs:
            fin = float(segs[-1][0]) or 1.0
            beats, n = [], 3 if len(segs) <= 8 else 4
            for i in range(n):
                lo, hi = fin * i / n, fin * (i + 1) / n
                pris = [s for s in segs if lo <= float(s[0]) < hi] or ([segs[i]] if i < len(segs) else [])
                if not pris: continue
                pris = sorted(pris, key=lambda s: len(re.findall(r'\b[A-Z]{3,}\b', s[1])) * 12
                              + min(len(s[1]), 260) / 10, reverse=True)[:2]
                pris.sort(key=lambda s: float(s[0]))
                tetes = [re.split(r'(?<=[.;])\s', s[1])[0] for s in pris]
                tetes = [x for x in tetes if len(x.split()) > 3] or tetes[:1]
                beats.append("[%.1f-%.1fs] %s" % (lo, hi, clip(' '.join(tetes), 18)))
            L.append('ACTION in %d stages, timings are budgets not edit points, each stage ends on the state the next '
                     'one starts from — %s' % (len(beats), ' '.join(beats)))

    perf = sect(b, r'^CHARACTER PERFORMANCE\n').replace('CHARACTER PERFORMANCE', '').strip()
    L.append('PERFORMANCE — ' + clip(phrases(perf, 2), 34))
    cam = sect(b, r'\nCAMERA\n') or sect(b, r'^OPTICS\n')
    L.append('CAMERA — ' + clip(cam.replace('CAMERA', '').replace('OPTICS', '').strip(), 30))
    lig = sect(b, r'\nLIGHT ')
    L.append('LIGHT — ' + clip(phrases(re.sub(r'^LIGHT[\s\W]*', '', lig), 1), 18))

    dia = re.search(r'^DIALOGUE ([^\n]+)', b, re.M)
    aud = sect(b, r'\nAUDIO\n').replace('AUDIO', '').strip()
    ligne = dia.group(1) if dia else ''
    n_rep = len(re.findall(r'\[[\d.]+-[\d.]+s\]', ligne))
    if n_rep:
        garde = ('EXACTLY %d SPOKEN LINE%s IN THIS ENTIRE GENERATION, written out here and nothing else. Any other '
                 'speech, any line carried over from the attached video, any murmur or half-word is an ERROR. '
                 % (n_rep, 'S' if n_rep > 1 else ''))
        d0 = re.search(r'\[(\d+\.\d+)-', ligne)
        if d0 and float(d0.group(1)) > 0.4:
            garde += ('FROM [0.0s] TO [%ss] NOBODY SPEAKS AT ALL: no line, no word, no murmur, no breath shaped like '
                      'speech. ' % d0.group(1))
        son = garde + ligne
    else:
        son = ('NOBODY SPEAKS IN THIS ENTIRE GENERATION: not one line, not one word, not one murmur, and NO LINE IS '
               'CARRIED OVER FROM THE ATTACHED VIDEO.')
    L.append('SOUND — ' + son + ' ' + clip(phrases(aud, 1), 20))

    emis = sect(b, r'LAST FRAME — THE EXACT STATE THIS SHOT HANDS OVER')
    lf = re.search(r'WHAT IS IN THE FRAME AT THE LAST INSTANT: (.*?)(?= WHERE THIS SHOT LEAVES|$)', emis) if emis else None
    if lf: L.append('ENDING FRAME, the state this shot hands over — ' + clip(lf.group(1), 18))

    av = sect(b, r'\nAVOID\n').replace('AVOID', '').strip()
    L.append('AVOID — ' + ', '.join([x.strip() for x in av.split(',') if x.strip()][:10]) + '.')

    txt = '\n'.join(L)
    txt = txt.replace('the FRAME MAP', 'the ACTION stages').replace('FRAME MAP', 'ACTION stages')
    txt = txt.replace('the choreography above', 'the ACTION stages above')
    # dans le corps, les personnages portent leur nom en clair : la mention est deja liee en tete
    tete, reste = txt.split('\nSHOT —', 1)
    # Dans le CORPS, plus une seule mention : la liaison est faite en tete, et un « @ » colle
    # en texte brut plus bas ne se lie a rien — il ne ferait que semer de faux liens.
    # On balaie TOUTES les mentions, pas seulement celles de ce plan : le texte extrait du bloc
    # long en charrie d'autres (repliques, raccord herite, derniere frame).
    def en_clair(m):
        return affiche(m.group(1))
    reste = re.sub(r'(?<!\w)@(\w+)', en_clair, reste)
    for e, r in manquants:
        tete = re.sub(r'(?<!\w)@' + re.escape(e) + r'\b', affiche(e), tete)
    return tete + '\nSHOT —' + reste, elts, manquants

# ---------------------------------------------------------------------------
D = 'docs/generations/videos'
total, tailles, sans_elt, trop_long = 0, [], {}, []
for f in sorted(glob.glob(os.path.join(D, 'PRET-SEQ-*.md'))):
    seq = re.search(r'SEQ-(\d\d)', f).group(1)
    out = [f"# PROMPTS — SÉQUENCE {seq}  ·  Seedance 2.0 · 1080p", '',
           "> Gabarit validé en vrai sur 1B le 06/09. **C'est cette version qu'on colle.**",
           f"> Le détail complet reste dans `PRET-SEQ-{seq}.md` (géométrie GEO, verrous, raccords).", '',
           "> ⚠ **Toutes les mentions `@` sont sur les deux premières lignes.** Colle le texte, puis remonte",
           "> et **re-sélectionne chacune dans le sélecteur** : un `@` collé en texte brut ne se lie à rien.", '']
    for b in re.split(r'\n(?=#{2,3} VIDÉO )', open(f, encoding='utf-8').read()):
        m = re.match(r'#{2,3} VIDÉO (\S+) —([^\n]*)', b)
        if not m: continue
        plan0 = m.group(1)
        for plan, shots, duree_f, note, refs_p in SPLITS.get(plan0, [(plan0, None, None, None, None)]):
            b_p = couper(b, shots) if shots else b
            restreint = {x.lower() for x in refs_p} if refs_p else None
            c, elts, manquants = construire(b_p, plan, restreint)
            total += 1; tailles.append(len(c.split()))
            d = re.search(r'\*\*durée\*\* \| (\d+(?:[.,]\d+)?) s', b)
            duree = duree_f if duree_f else (float(d.group(1).replace(',', '.')) if d else 10.0)
            if duree > 15: trop_long.append((plan, duree)); duree = 15.0
            si = re.search(r'\|\s*\*\*`start_image`\*\*\s*\|([^\n|]*)', b)
            tete = 'No video is attached' in c or 'No previous clip is attached' in c
            if manquants: sans_elt[plan] = [x[0] for x in manquants]
            titre = m.group(2) if not note else (' morceau %s de %s — %s' % (plan.split('-')[-1], plan0, note))
            out += [f"## {plan} —{titre}", '',
                    '| | |', '|---|---|',
                    '| **modèle** | **Seedance 2.0** · mode `std` · genre `drama` |',
                    '| **format** | 21:9 · **1080p** · bitrate **high** |',
                    f'| **durée** | **{duree:g} s** · **son ON** |',
                    ('| **`@image1`** (start image) | ' + (si.group(1).strip() if si else '—') + ' |') if tete
                    else '| **`@image1`** (start image) | **la dernière frame du clip précédent** |',
                    ('| **`@video1`** | — aucune vidéo, tête de chaîne |') if tete
                    else '| **`@video1`** | le clip précédent |',
                    '| **Éléments** | ' + (' · '.join('`@' + r + '`' for _, r in elts) or '—') + ' |']
            if note:
                out += ['', '> ✂ **%s a été coupé en trois** : Seedance 2.0 plafonne à 15 s et le plan en fait 19. '
                        'Ce morceau couvre %s. Le montage garde les mêmes 9,5 s au total.' % (plan0, note)]
            if manquants:
                out += ['', '> 🔴 **Élément(s) inexistant(s) sur le compte : ' +
                        ', '.join('@' + x[0] for x in manquants) +
                        '.** Ils sont écrits en clair dans le prompt (le modèle les construira depuis la '
                        "description), mais l'identité ne sera pas verrouillée d'un plan à l'autre "
                        'tant qu\'ils ne sont pas créés.']
            out += ['', '```', c, '```', '']
    open(os.path.join(D, f'PROMPT-SEQ-{seq}.md'), 'w', encoding='utf-8').write('\n'.join(out))

tailles.sort()
print(total, "prompts · mots : min", tailles[0], "· médiane", tailles[len(tailles)//2], "· max", tailles[-1])
print("plans au-dessus du plafond 15 s de Seedance 2.0 :", trop_long or "aucun")
print("plans citant un Element inexistant :", len(sans_elt))
for k, v in sorted(sans_elt.items()): print("   ", k, "→", ', '.join('@'+x for x in v))
