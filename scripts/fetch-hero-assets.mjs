// Récupère les médias du fond de héros (boucle JARVIS générée via Higgsfield,
// skill scroll-film-studio) au moment du build Netlify — l'environnement de
// build a l'accès Internet complet, contrairement au dépôt (pas de binaires
// en git). Échec ⇒ on continue sans vidéo : le héros garde son fond statique.
import { mkdirSync, writeFileSync, existsSync, statSync } from 'node:fs';

const ASSETS = [
  {
    url: 'https://d8j0ntlcm91z4.cloudfront.net/user_3EySMZUzUbGakFLyLPoFHW1KflJ/hf_20260814_152513_1b034177-514d-49d9-b6f6-d3cde0c409d4.mp4',
    dest: 'public/hero-film.mp4',
  },
  {
    url: 'https://d8j0ntlcm91z4.cloudfront.net/user_3EySMZUzUbGakFLyLPoFHW1KflJ/hf_20260814_152427_6e92c465-ba87-4714-b5a6-ff6bcaf7caf8.png',
    dest: 'public/hero-poster.png',
  },
  // L'orbe JARVIS (bouton d'enclenchement du dock) : boucle 1:1 Seedance.
  {
    url: 'https://d8j0ntlcm91z4.cloudfront.net/user_3EySMZUzUbGakFLyLPoFHW1KflJ/hf_20260814_185714_b378504f-f952-4c10-a84b-72b4f33d543c.mp4',
    dest: 'public/jarvis-orb.mp4',
  },
  {
    url: 'https://d8j0ntlcm91z4.cloudfront.net/user_3EySMZUzUbGakFLyLPoFHW1KflJ/hf_20260814_185553_872a2b4c-5404-4520-b90e-46d0b884d8c5.png',
    dest: 'public/jarvis-orb.png',
  },
];

mkdirSync('public', { recursive: true });

for (const { url, dest } of ASSETS) {
  if (!url.startsWith('http')) continue;
  if (existsSync(dest) && statSync(dest).size > 10_000) {
    console.log(`[hero-assets] ${dest} déjà présent, on garde.`);
    continue;
  }
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const buf = Buffer.from(await res.arrayBuffer());
    writeFileSync(dest, buf);
    console.log(`[hero-assets] ${dest} téléchargé (${Math.round(buf.length / 1024)} Ko).`);
  } catch (e) {
    console.warn(`[hero-assets] ${dest} indisponible (${e.message}) — le site build sans.`);
  }
}
