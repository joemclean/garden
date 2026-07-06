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
   > Finish by opening a pull request for your visit and merging it
   > yourself, immediately — never leave your work unmerged.

3. Host `viewer/` anywhere static (GitHub Pages works: serve the repo
   root so the viewer can fetch `../garden.json`).
4. In the repo settings, enable "Automatically delete head branches" —
   stale branches confuse future pull requests.

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

Still works, if you like dirt under your fingernails — and it's one
file: add `plots/<id>/seed.md` for any empty plot (copy
`seedbox/SEED_TEMPLATE.md`; GitHub's web "Add file" works fine from a
phone). The gardener registers new seeds in `garden.json` itself on its
next visit, and fresh seeds are always tended first.

## Reading the garden

Open the viewer. Soil → seed → sprout → growing → bloom → gone to seed.
Plants brown when a plot goes 72 hours untended — that's not failure,
just a visible ask for attention (yours or the gardener's).

Tap a plot to step inside: the card links to the plot's growth files,
journal, and seed — and when the gardener has set a `door` (the plot's
best artifact), straight to the live work itself, served by Pages.
