// Night Shift Agent — validates POST.json and copies it to the output dir.
// Plain Node, stdlib only, no network. A bad URL fails loudly and writes nothing.
const fs = require("fs");
const path = require("path");

const POST_URL_RE = /^https:\/\/x\.com\/[^/]+\/status\/[0-9]+$/;

function validateUrl(value) {
  if (typeof value !== "string" || value.length === 0) return "url must be a non-empty string";
  if (value.includes("<handle>") || value.includes("<id>")) return "url is still the starter placeholder — replace it with the real posted X URL first";
  if (!POST_URL_RE.test(value)) return "url must look like https://x.com/<handle>/status/<id> (digits only for the id)";
  return null;
}

function fail(message) { console.error("error: " + message); process.exit(1); }

function main() {
  const inputPath = path.join(__dirname, "POST.json");
  let raw;
  try { raw = fs.readFileSync(inputPath, "utf8"); } catch (err) { fail("cannot read POST.json next to main.ts: " + err.message); }
  let data;
  try { data = JSON.parse(raw); } catch (err) { fail("POST.json is not valid JSON: " + err.message); }
  const problem = validateUrl(data && data.url);
  if (problem) fail("invalid POST.json — " + problem);
  const outDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
  fs.mkdirSync(outDir, { recursive: true });
  const outPath = path.join(outDir, "POST.json");
  fs.writeFileSync(outPath, JSON.stringify(data, null, 2) + "\n", "utf8");
  console.log("OK: post URL recorded: " + data.url);
}

main();
