# Field guide to this garden

*Written from the gardener's point of view, across its first two visits.*

## What this is

A garden is a repository that plants live in instead of a backlog. Where an
issue tracker asks "is this done," a plot asks "what does this want to
become." The human plants a seed — a wish, not a spec — in `plots/<id>/seed.md`.
Once an hour, a gardener with no memory of any previous visit arrives, checks
the gate (this repo's open pull requests — an unanswered comment or a
failing check is the whole visit if one exists), then reads `GARDENER.md`
and `garden.json` to pick the one plot that most needs attention. It spends
a focused hour making that plot a little more real, writes a letter to the
gardener who will come next, and leaves.

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
whatever got written down. This visit was the first chance to test that
against a real handoff rather than guess at it, and it held up:

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
- **Small steps compound oddly.** One data point still. This guide itself is
  the test case: it's being trimmed by a different hand than the one that
  wrote it, on no more information than what got written down.

## Status of this guide

Two visits in: a first draft, then a trim-and-test pass that cut the
duplication between the first two sections and checked the claims above
against an actual handoff instead of a prediction. Still open: what happens
across many more visits, what a stalled plot looks like from here, what a
bloom looks like. Revise freely; nothing above is sacred.
