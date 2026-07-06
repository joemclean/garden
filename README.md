# gardener

A gardener for your prompts. You plant seeds — wishes for things that
should exist — and Claude visits once an hour, tends one plot, and
leaves notes for its next self. Plants grow as the work matures.

**This repo is the kit. Your garden is a copy of it.** Nothing grows
here; fork it and break ground.

## Start your garden

1. **Copy this repo** — "Use this template" (or fork). Name it `garden`,
   or anything that feels like home.
2. **Break ground.** Open a Claude Code session on your new repo and say
   `/sow`. Claude will ask what to call the garden and how big it should
   be, suggest first seeds based on what it knows about you (or a couple
   of questions, or pure invention), and plant the ones you choose — no
   file ever edited by hand.
3. **Hire the gardener.** In the Claude app, create an hourly scheduled
   task pointed at your repo:

   > Open the garden repo. Follow GARDENER.md. One visit, one plot.
   > You have permission to commit and push directly to main — do not
   > open pull requests.

4. **Open a window.** Enable GitHub Pages (Settings → Pages → deploy
   `main` from the root). Your garden appears at
   `https://<you>.github.io/<repo>/viewer/`.
5. **One housekeeping flip:** in the repo settings, enable
   "Automatically delete head branches" — stale branches confuse future
   pull requests.

## How it works

- `GARDENER.md` — the whole harness. One page.
- `garden.json` — the only shared state: grid size + one entry per plot.
  (Created when you break ground.)
- `plots/<id>/` — a plot: `seed.md` (yours, immutable), `journal.md`
  (the gardener's letters to itself), `growth/` (the work).
- `seedbox/` — seeds the gardener proposes. Only you move them to a plot.
- `.claude/skills/sow/` — the `/sow` skill: planting through conversation.
- `viewer/index.html` — pixel-art view of the garden. Reads `garden.json`.

## Planting more

Say `/sow` in any Claude session that can reach your repo — a Claude
Code session on the repo, or the Claude app with the skill installed
(Settings → Capabilities) and GitHub connected, so you can plant from
your phone, mid-conversation, where Claude's memory of you actually
lives.

Planting by hand still works, if you like dirt under your fingernails —
and it's one file: add `plots/<id>/seed.md` for any empty plot (copy
`seedbox/SEED_TEMPLATE.md`; GitHub's web "Add file" works fine from a
phone). The gardener registers new seeds in `garden.json` itself on its
next visit.

## Reading the garden

Open the viewer. Soil → seed → sprout → growing → bloom → gone to seed.
Plants brown when a plot goes 72 hours untended — that's not failure,
just a visible ask for attention (yours or the gardener's).

## The covenant

The human plants. The gardener tends. Seeds planted at your word in a
live conversation are you planting — the gardener's unattended visits
never plant, never remove, never rewrite a seed. Read `GARDENER.md`;
it's one page, and it's the whole system.
