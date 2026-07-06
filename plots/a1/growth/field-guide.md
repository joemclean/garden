# Field guide to this garden

*Written from the gardener's point of view, across its first four visits.*

## What this is

A garden is a repository that plants live in instead of a backlog. Where an
issue tracker asks "is this done," a plot asks "what does this want to
become." The human plants a seed — a wish, not a spec — in `plots/<id>/seed.md`.
Once an hour, a gardener with no memory of any previous visit arrives and
checks the gate: this repo's open pull requests and any stray branches. Two
different things can happen here, and they're not the same shape. Real
trouble — garden work stranded off `main`, an unanswered comment, a failing
check — *is* the whole visit: fix it, or merge it, or leave a comment, then
leave, no plot tending after. A PR that's already clean (checks passing, no
open threads, no conflicts) is lighter: merge it and carry on into the usual
plot-tending visit, don't leave it sitting for the human. Either way, once
the gate is clear, read `GARDENER.md` and `garden.json` to pick the one plot
that most needs attention. Spend a focused hour making that plot a little
more real, write a letter to the gardener who comes next, and leave.

There is exactly one piece of shared state: `garden.json`. It holds a stage
number and a one-line note per plot. Everything else — the seed, the journal,
the actual work in `growth/` — is discovered fresh, on the page, every visit.
Nothing is assumed to be remembered.

## How a visit feels

It feels like waking up in a room with a note taped to the door. Among the
plots — most of which, on any given day, are just soil — a freshly planted
seed outranks everything: it's a human's newest wish, untouched, and it
always gets read first. Otherwise you're weighing which existing plot most
needs you, on judgment, not a formula.

Then you go to that plot's `seed.md` and read it as if for the first time,
because for you it is. You read `journal.md` next — the accumulated letters
from every prior visit, in order, newest last. That journal is the only
memory this project has. If a past self left a vague or lazy entry, the
next self inherits confusion instead of context. Writing the journal well
*is* the job, as much as the work itself.

Then: one hour, one plot, whatever's in `growth/`. No wandering into other
plots. No editing `viewer/` or `GARDENER.md` itself — those belong to the
human, not the gardener.

## What makes a good seed

A good seed reads like a wish a friend made, not a ticket a manager filed.
The qualities that seem to matter:

- **It says what bloom looks like**, even loosely. "A stranger could read
  this in five minutes" is a bloom condition. Without one, a gardener has no
  way to know if progress is real or just motion.
- **It leaves room to be surprised.** A spec would over-determine the
  outcome and rob a slow, iterative process of the thing that makes it
  interesting — many small independent passes, each free to notice
  something the last one didn't.
- **It's honest about pace.** This seed says "grow it slowly across
  visits" — permission not to rush to bloom in one sitting, which matters
  because rushing here means guessing at intent instead of tending it.
- **It survives being read cold.** Since every gardener meets it fresh,
  a seed that depends on context outside itself (a conversation, an
  assumption, a half-explained abbreviation) will drift or stall. The seed
  has to be the whole brief.

## What hour-long slices with no memory actually do to the work

The constraint that stands out most: continuity is entirely textual. There
is no felt sense of "last time I was leaning toward X" — there is only
whatever got written down. Three visits have now tested that against real
handoffs rather than guessed at it:

- **Terseness in the journal is a real cost, not a style choice.** The prior
  entry named exactly what to do next ("reread with distance... consider
  trimming before adding") and that's what made this visit's starting point
  clear instead of a guess. A vaguer entry would have cost real time.
- **Half-finished thoughts don't survive a visit boundary.** Untested still,
  since the first visit happened to close at a stable, finished point. Worth
  watching for the visit where an hour runs out mid-thought.
- **Stage is a compression of history.** `garden.json`'s note said "needs a
  second visit's distance to trim and test" — a one-line summary that was
  enough, on its own, to know what this visit was for.
- **Small steps compound oddly.** Two data points now, and they point the
  same direction: this guide keeps being edited by a different hand than the
  one that wrote it, on no more information than what got written down, and
  it keeps holding together anyway.
- **The guide can go stale even when the journal is honest.** Visit 3 found
  the first real inaccuracy: "How a visit feels" still described the gate as
  just "open pull requests," but `GARDENER.md` had since been hardened to
  also cover stray branches and self-merging green PRs — changes landed by
  a *different* plot's work, invisible from inside this one. No journal
  entry was wrong; the ground the guide was standing on moved. Worth
  remembering: staleness isn't only a risk from a lazy handoff, it's a risk
  from the harness itself evolving between visits.
- **The gate had never had real content until visit 4 — and the guide's
  confident description of it turned out half-aspirational.** A green,
  mergeable PR was waiting. Merging it worked exactly as described. Deleting
  its now-merged head branch did not: the gardener's git push was rejected
  (403) and there is no GitHub tool available to delete a branch directly.
  Three visits had described "merge it, delete the branch" as one clean
  motion without ever having done it — it reads differently once tried.
  Some of what a seed-writer (or an earlier gardener) asserts about the
  harness is untested prediction wearing the voice of fact, and the only
  way to tell the difference is to hit the real case.

## Status of this guide

Four visits in: a first draft, a trim-and-test pass, a drift-and-correct
pass, and now the first visit where the gate actually had real work in it —
a green PR, merged clean, with a branch-deletion step that turned out not
to be doable with the tools on hand. The core shape has held across all
four passes without needing a rewrite, each time absorbing a real,
previously-untested claim rather than just adding more prose. Still open:
what a stalled plot looks like, what a bloom looks like, and a visit that
runs out of time mid-thought. Revise freely; nothing above is sacred —
the gate description in particular has now been wrong twice in different
ways, and will likely be wrong again the next time the harness or its
tools change underneath it.
