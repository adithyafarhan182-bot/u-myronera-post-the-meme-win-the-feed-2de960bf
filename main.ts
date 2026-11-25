// Night Shift Agent — entry for make.fun's "Post the Meme, Win the Feed" bounty.
// The entry is the X post itself: a two-panel meme (meme.png) posted from @ma_dar3
// with @_myronera tagged and the play code in its text. This program only hands
// the post in: it copies POST.json from the repository root to /output/POST.json,
// where the gate reads it. A plain copy, no network, no clock, no files outside
// the repository — so the two runs of an entry write the same bytes.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR stand
// in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

const source = join(BOT_DIR, 'POST.json');
const target = join(OUTPUT_DIR, 'POST.json');

// The gate refuses a POST.json it cannot parse, so fail loudly here instead of
// copying a broken file through. It also refuses the starter placeholder, so
// refuse that here too: the submitted commit must name a real post.
const text = readFileSync(source, 'utf8');
const parsed = JSON.parse(text) as unknown;
if (typeof parsed !== 'object' || parsed === null || typeof (parsed as { url?: unknown }).url !== 'string') {
  console.error('POST.json must be a JSON object with a string "url" field');
  process.exit(1);
}
const url = (parsed as { url: string }).url;
if (!/^https:\/\/(www\.|mobile\.)?(x\.com|twitter\.com)\/[^/]+\/status\/\d+/.test(url)) {
  console.error('POST.json "url" must be a real X post address, https://x.com/<handle>/status/<id>');
  process.exit(1);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
copyFileSync(source, target);
