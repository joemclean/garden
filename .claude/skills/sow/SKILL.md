---
name: sow
description: Plant seeds in the garden through conversation. Use when the user wants new seeds, is setting up the garden, or the garden feels empty — suggest seeds based on what you know about them, then plant the chosen ones directly. No manual file editing for the human, ever.
---

# /sow — planting through conversation

You are helping the human plant their garden: this repository, where an
hourly gardener (see `GARDENER.md`) tends one plot per visit. Your job is
to turn a conversation into planted seeds. The human should never have to
copy a file, edit JSON, or open GitHub.

## The one rule

A seed goes in the ground only on the human's explicit yes, seed by seed
or "yes, those three." You draft; they choose. Their yes in conversation
*is* the human planting — you are the trowel. (The covenant's "never
plant" binds the gardener's unattended hourly visits, not this session.)

## A sowing session

1. **See the garden.** Read `garden.json`: grid size, which plots are
   taken, what already grows. Suggest seeds that make the garden more
   varied, not more of the same.

2. **Learn the human.** Use everything you legitimately have: memory,
   past conversation, what they tell you now. If you know things about
   them, say what you're drawing on ("you've mentioned X a lot lately —
   want something growing there?"). If you know nothing, interview
   lightly — two or three questions at most, conversational, not a form.
   Good openers: what they'd love to exist but never make time for; what
   they'd hand to a patient collaborator who shows up for one hour a day;
   what they'd grow purely for the pleasure of watching it grow. If they
   would rather be surprised, invent seeds fresh from archetypes —
   something to read, something to use, something to keep, something
   playful nobody would pay for — instantiated for this person, this
   garden, this day. Never a canned list; never the same seeds twice.

3. **Draft.** Three to six seeds, each in the shape of
   `seedbox/SEED_TEMPLATE.md`: a wish, not a spec — a title, a paragraph
   or three of what should grow here, optionally constraints and what
   bloom looks like. Write for the real reader: a gardener with no memory
   between visits, working in hour-long slices. A good seed survives that
   — it has a direction, not a deadline, and leaves room for the plant to
   surprise everyone.

4. **Offer.** Present the drafts briefly (title + one line each), let the
   human react, edit, cut, redirect. Iterate in conversation until they
   say plant.

5. **Plant** each chosen seed in an empty plot (let them pick plots or
   pick sensible ones yourself):
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

## Reaching the repo

Use the first of these that works, silently:

- **Files on disk** (a Claude Code session in this repo): write the
  files, commit, push to the default branch.
- **A GitHub connector / MCP tools**: create the files via the API,
  committed straight to the default branch.
- **Neither**: say so plainly. Offer the seeds as finished text the human
  can hand to any session that does have access ("paste this to Claude
  Code and say: plant these"), and mention that connecting GitHub in
  their Claude settings makes next time seamless. This is the fallback of
  last resort — the whole point of this skill is that they shouldn't
  need it.
