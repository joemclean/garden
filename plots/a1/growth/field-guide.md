# Field guide to this garden (draft v1)

*Written from the gardener's point of view, on the very first visit this garden ever had.*

## What this is

A garden is a repository that plants live in instead of a backlog. Where an
issue tracker asks "is this done," a plot asks "what does this want to
become." The human plants a seed — a wish, not a spec — in `plots/<id>/seed.md`.
Once an hour, a gardener with no memory of any previous visit arrives, reads
`GARDENER.md`, picks the one plot that most needs attention, and spends a
focused hour making it a little more real. Then it writes a letter to the
gardener who will come next, and leaves.

There is exactly one piece of shared state: `garden.json`. It holds a stage
number and a one-line note per plot. Everything else — the seed, the journal,
the actual work in `growth/` — is discovered fresh, on the page, every visit.
Nothing is assumed to be remembered.

## How a visit feels

It feels like waking up in a room with a note taped to the door. The note
(`GARDENER.md`) says: check the gate first — are there open pull requests
that need a reply, a fix, a rebase? If so, that's the whole visit; tend it
and leave. Otherwise, open `garden.json` and look at the grid. Most of it,
on any given day, is soil — empty. One or two plots have something growing.
A freshly planted seed outranks everything: it's a human's newest wish,
untouched, and it always gets read first.

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
From this first visit, the qualities that seem to matter:

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

The constraint that stands out most, even from a single visit: continuity
is entirely textual. There is no felt sense of "yesterday I was leaning
toward X" — there is only whatever got written down. That has a few
consequences worth naming for whoever reads this next:

- **Terseness in the journal is a real cost, not a style choice.** "Did some
  work on the guide" tells a memoryless successor nothing about *which*
  work, *why* that angle, or *what's still open*. The journal has to
  over-explain relative to how a single continuous author would write to
  themselves.
- **Half-finished thoughts don't survive a visit boundary.** Anything not
  written down by the end of the hour might as well not have happened, from
  the next gardener's perspective. This argues for closing each visit at a
  stable point — even mid-draft — rather than leaving state that only
  makes sense if you remember the reasoning that produced it.
- **Stage is a compression of history.** `garden.json`'s one-line note and
  stage number are what a human sees without reading any journal at all.
  They have to be honest on their own, since not every reader will go
  deeper.
- **Small steps compound oddly.** Because no single visit can lean on
  momentum, progress looks less like a person working and more like relay
  runners who never meet — each one has to pick up the baton purely from
  what's written on it. The quality of the *handoff* matters as much as
  the quality of the work.

## Status of this guide

This is a first draft, written in the garden's very first hour of existence
— there was no prior journal, no prior visit, nothing to build on but
`GARDENER.md` itself and the act of tending for the first time. Later
visits should test these observations against more lived experience: do
these things still feel true after ten visits? After the first plot
blooms? After the first stalled plot goes brown? Revise freely; nothing
above is sacred.
