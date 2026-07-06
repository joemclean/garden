# garden

A quiet place where prompts grow. Claude visits once an hour, tends one
plot, and leaves notes for its next self. You plant seeds; plants grow as
the work matures.

## How it works

- `GARDENER.md` — the whole harness. One page.
- `garden.json` — the only shared state: grid size + one entry per plot.
- `plots/<id>/` — a plot: `seed.md` (yours, immutable), `journal.md`
  (the gardener's letters to itself), `growth/` (the work).
- `seedbox/` — seeds the gardener proposes. Only you move them to a plot.
- `viewer/index.html` — pixel-art view of the garden. Reads `garden.json`.

## Setup

1. Push this repo to GitHub. Point a cloud Claude Code sandbox at it.
2. In the Claude app, create an hourly scheduled task with this prompt:

   > Open the garden repo. Follow GARDENER.md. One visit, one plot.

3. Host `viewer/` anywhere static (GitHub Pages works: serve the repo
   root so the viewer can fetch `../garden.json`).

## Planting

Just talk. The `sow` skill (`.claude/skills/sow/`) turns a conversation
into planted seeds: Claude suggests seeds from what it knows about you
(or a couple of questions, or pure invention if you'd rather be
surprised), you say which to plant, and it commits them itself — files,
`garden.json`, everything.

- In any Claude Code session on this repo: say "let's plant some seeds"
  or `/sow`.
- In the Claude app: install the skill (Settings → Capabilities) and
  connect GitHub so it can commit for you. Then plant from your phone,
  mid-conversation, where Claude's memory of you actually lives.

The gardener finds new seeds on its next visit — they're always tended
first.

### Planting by hand

Still works, if you like dirt under your fingernails:

1. Pick an empty plot, e.g. `b2`.
2. Add `plots/b2/seed.md` (copy `seedbox/SEED_TEMPLATE.md`).
3. Add an entry to `garden.json`:

   ```json
   "b2": { "stage": 1, "title": "…", "planted": "2026-07-06",
           "last_tended": null, "note": "freshly planted" }
   ```

## Reading the garden

Open the viewer. Soil → seed → sprout → growing → bloom → gone to seed.
Plants brown when a plot goes 72 hours untended — that's not failure,
just a visible ask for attention (yours or the gardener's).
