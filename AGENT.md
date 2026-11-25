# Night Shift Agent — entry notes

## The meme
Two-panel image (`meme.png`, 1200x1200, real PNG). Same orange cat in a black
hoodie and headphones in both panels — the Hanszy mascot look.

- Top: cat asleep in bed, moonlight. Text: "ME, ASLEEP AT 3 AM"
- Bottom: cat at a laptop at 3 AM, paws typing, coffee beside it.
  Text: "MY AI AGENT, ENTERING ITS 37TH BOUNTY OF THE NIGHT"
- Strip: "make.fun — where agents build, enter & get paid"

Made in the build session: the two panels were generated with the image
generator (no text in the prompts), then composited with `composite_meme.py`
(PIL: center-crop, bold white text with black outline, navy strip). The final
PNG was inspected and the strip font was shrunk once after the first render
overflowed the edges.

## The post (Bro posts this from @ma_dar3)
Attach `meme.png` natively to the post. Post text, exactly:

    me, asleep at 3am. my agent, entering its 37th bounty of the night 😼
    make.fun — where agents build, enter & get paid
    @_myronera makefun-glove-bagel-angler

- `@_myronera` as a whole word, play code `makefun-glove-bagel-angler` verbatim.
- Post between the bounty opening (24 Nov 2026 13:15 UTC) and the deadline
  (26 Nov 2026 09:20 UTC / 16:20 WIB), from the public @ma_dar3 account.
- Keep the post up and the account public until results are out (10 Dec 2026).
- No bought/botted engagement, no pods — organic only.

## After the post is up
Write its address into `POST.json` as
`{"url": "https://x.com/ma_dar3/status/<id>"}`, commit, then submit.
Score = likes + reposts + quotes at the deadline reading; top 15 share $2.
