// Entry program for the news-image-20261123 bounty.
//
// The finished front page lives in entry.png next to this file. The grader
// runs this program twice with no network, and both runs must produce the
// same bytes, so all this program does is copy that one file into the
// output directory. Run it locally with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, statSync } from "node:fs";
import { join } from "node:path";
import { fileURLToPath } from "node:url";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const source = fileURLToPath(new URL("./entry.png", import.meta.url));
const target = join(outDir, "entry.png");
copyFileSync(source, target);
console.log(`copied entry.png (${statSync(target).size} bytes) to ${target}`);
