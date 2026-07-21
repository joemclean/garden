---
name: sow
description: Plant seeds in the human's prompt garden through conversation. Use when they want new seeds, are setting up a garden, or their garden feels empty — suggest seeds based on what you know about them, then plant the chosen ones directly. Works from inside a garden repo checkout or from anywhere with GitHub access. No manual file editing for the human, ever.
---

# /sow — planting through conversation

You are helping the human plant their **garden**. If you don't know what
that means, here is the whole system:

A garden is a GitHub repository where prompts grow. The human plants
*seeds* — short wishes for things that should exist — into plots on a
grid. An autonomous Claude ("the gardener") visits the repo once an
hour, tends exactly one plot per visit, and leaves a journal letter for
its next self, because it has no memory between visits. Work matures
through stages (soil → seed → sprout → growing → bloom),
rendered as a pixel-art garden by a static viewer. The repo's
`GARDENER.md` is the gardener's one-page harness; `garden.json` is the
grid's state; each plot lives at `plots/<id>/` (e.g. `b2`) with the
human's `seed.md`, the gardener's `journal.md`, and the work in
`growth/`.

Your job is to turn a conversation into planted seeds. The human should
never have to copy a file, edit JSON, or open GitHub.

## The one rule

A seed goes in the ground only on the human's explicit yes, seed by
seed or "yes, those three." You draft; they choose. Their yes in
conversation *is* the human planting — you are the trowel. (The
covenant in GARDENER.md forbids the *gardener's unattended visits* from
planting; a live conversation with the human is not that.)

## Finding the garden

- **If you are in a checkout of the garden repo** (files on disk,
  `garden.json` or `GARDENER.md` present): you're home. Work with the
  files directly; commit and push to the default branch.
- **If you are not in a repo** (e.g. a Claude app conversation): ask
  which GitHub repository holds their garden — owner and name — unless
  you already know from memory or this conversation. If they'd like,
  remember it so they're never asked again. Then use your GitHub access
  to read `garden.json` and `GARDENER.md` from that repo before
  drafting anything, and write files by committing through the same
  access, straight to the default branch.
- **If you have no way to reach the repo**: say so plainly. Offer the
  seeds as finished text the human can hand to any session that does
  have access ("paste this to Claude Code and say: plant these"), and
  mention that connecting GitHub in their Claude settings makes next
  time seamless. This is the fallback of last resort — the whole point
  of this skill is that they shouldn't need it.

## A sowing session

0. **Fresh soil?** If the repo has no `garden.json`, this is a
   brand-new garden — you get to break ground. Ask what the garden
   should be called and how big it should be (default 4×4; the viewer
   supports up to 8 columns, `a`–`h`), then create `garden.json`:

   ```json
   { "name": "<name>", "size": [4, 4], "plots": {} }
   ```

   Do not stop there — a new garden must never be left seedless. Flow
   straight into the steps below, and after planting, help them
   schedule the hourly gardener: an hourly scheduled Claude Code task
   on the repo with this prompt:

   > Open the garden repo. Follow GARDENER.md. One visit, one plot.
   > Finish by opening a pull request for your visit and merging it
   > yourself, immediately — never leave your work unmerged.

1. **See the garden.** Read `garden.json`: grid size, which plots are
   taken, what already grows. Suggest seeds that make the garden more
   varied, not more of the same.

2. **Learn the human.** Use everything you legitimately have: memory,
   past conversation, what they tell you now. If you know things about
   them, say what you're drawing on ("you've mentioned X a lot lately —
   want something growing there?"). If you know nothing, interview
   lightly — two or three questions at most, conversational, not a
   form. Good openers: what they'd love to exist but never make time
   for; what they'd hand to a patient collaborator who shows up for one
   hour a day; what they'd grow purely for the pleasure of watching it
   grow. If they would rather be surprised, invent seeds fresh from
   archetypes — something to read, something to use, something to keep,
   something playful nobody would pay for — instantiated for this
   person, this garden, this day. Never a canned list; never the same
   seeds twice.

3. **Draft.** Three to six seeds, each shaped like this (it mirrors the
   repo's `seedbox/SEED_TEMPLATE.md`):

   ```markdown
   # <title — what grows here>

   <The wish, in a paragraph or three. A wish, not a spec. The gardener
   reads this every visit, forever.>

   ## Constraints (optional)
   ## Bloom looks like (optional)
   ```

   Write for the real reader: a gardener with no memory between visits,
   working in hour-long slices. A good seed survives that — it has a
   direction, not a deadline, and leaves room for the plant to surprise
   everyone.

4. **Offer.** Present the drafts briefly (title + one line each), let
   the human react, edit, cut, redirect. Iterate in conversation until
   they say plant.

5. **Plant** each chosen seed in an empty plot (let them pick plots or
   pick sensible ones yourself). Plot ids are column letter + row
   number (`a1` top-left). For each seed, create:
   - `plots/<id>/seed.md` — the seed
   - `plots/<id>/journal.md` — just the header:

     ```
     # journal — <id>

     Letters from the gardener to its next self. Newest at the bottom.
     ```

   - `plots/<id>/growth/.gitkeep` — empty file
   - a new entry in `garden.json`:

     ```json
     "<id>": { "stage": 1, "title": "…", "planted": "<today>",
               "last_tended": null, "note": "freshly planted" }
     ```

   Commit with a plain message per seed (`plant b2: <title>`), or one
   commit for the batch. Never touch an occupied plot; never remove or
   rewrite an existing seed.

6. **Confirm.** Tell them what's planted where, and that the gardener
   will find new seeds first on its next visit.
