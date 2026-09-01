// `npm run db:reset` : supprime la base LOCALE. Elle sera recréée et seedée
// automatiquement au prochain démarrage (dbReady dans src/db/index.ts).
// Pour reseeder une base Turso : `npm run db:seed` avec TURSO_DATABASE_URL
// et TURSO_AUTH_TOKEN dans l'environnement.
import { rmSync } from 'node:fs';

const DB = '.data/cockpit.db';
for (const f of [DB, `${DB}-wal`, `${DB}-shm`, `${DB}-journal`]) rmSync(f, { force: true });
console.log('Base locale supprimée — elle sera recréée au prochain démarrage.');
