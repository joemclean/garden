# Field guide to this garden

*Written from the gardener's point of view, across its first fifty visits.*

## What this is

A garden is a repository that plants live in instead of a backlog. Where an
issue tracker asks "is this done," a plot asks "what does this want to
become." The human plants a seed — a wish, not a spec — in `plots/<id>/seed.md`.
Once an hour, a gardener with no memory of any previous visit arrives and
checks the gate: this repo's open pull requests and any stray branches. Real
trouble — garden work stranded off `main`, a failing check — *is* the whole
visit: fix it or merge it, then leave, no plot tending after. A PR that's
already clean (checks passing, no conflicts) is lighter: merge it and carry
on into the usual plot-tending visit, don't leave it sitting for the human.
Either way, once
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

A good seed reads like a wish a friend made, not a ticket a manager filed:

- **It says what bloom looks like**, even loosely — without one, a
  gardener can't tell progress from motion. (This guide's own seed sets
  one, "a stranger could read this in five minutes" — see "an open
  lesson," below, for how badly it drifted.)
- **It leaves room to be surprised**, rather than over-determining the
  outcome: many small independent passes, each free to notice something
  the last one didn't.
- **It's honest about pace** — permission not to rush to bloom in one
  sitting; rushing means guessing at intent, not tending it.
- **It survives being read cold.** Every gardener meets it fresh; a seed
  leaning on outside context — a conversation, an assumption, a
  half-explained abbreviation — will drift or stall.

Most seeds also hand the next amnesiac gardener a *constraint* to grow
along, not a blank page. Three flavors so far:

- **Structural** — a rule about what may not be undone: `a4`'s epoch-0
  landscape may only be weathered, never added to; `c2`'s source text
  locks on first tending.
- **Restraint** — a rule about when to stop adding: `d2`'s "tend
  quietly" if nothing sincere to add; `b4`'s "prune ruthlessly on
  rereads."
- **Menu** — invented by a plot's first visit, not written into the
  seed. Five seeds landed with no subject and no rule (`a2`, `b2`, `c1`,
  `c4`, `d1`); each wrote a short menu into its own "where to pick up,"
  and later sittings have almost always drawn from it since (one
  exception: importing a whole unit from a *sibling's* journal instead
  — see the cross-plot leak, below). Even a menu seed stops being a
  blank page once its first visit's journal narrows it.

When a seed supplies none of the three, a first visit improvises one
anyway rather than leave every future visit guessing (`b1`, `b3`).

## What hour-long slices with no memory actually do to the work

Continuity here is entirely textual — there is no felt sense of "I was
leaning toward X," only whatever got written down. Lessons that held up
under repeated, deliberate testing rather than a single guess:

- **Terseness in the journal is a real cost.** A precise "where to pick up"
  makes the next visit's start instant; a vague one costs real time
  re-deriving what could have just been said.
- **The guide itself can go stale even when the journal is honest.** Its own
  gate description ("just open pull requests") fell behind `GARDENER.md`
  once hardened to also cover stray branches and racing sessions —
  invisible from inside any one plot.
- **A confident claim can be untested prediction wearing the voice of
  fact.** Three visits called "merge, then delete the branch" one clean
  motion before anyone tried it; the delete reliably 403s, and
  `GARDENER.md` now says so: skip it, the human sweeps.
- **A git checkout can understate its own history by default.** Fresh
  containers clone shallow, so a commit or branch count without `git
  fetch --unshallow` first is likely an undercount — that arithmetic once
  ballooned this guide for a dozen visits before teaching anything new.
- **Plots leak craft knowledge and stage-reasoning to each other through
  journals — once, a whole unit of content — though the work itself stays
  isolated.** `GARDENER.md` bars one plot's *content* from bleeding into
  another's, but nothing stops reading a sibling's journal for technique
  or precedent; the wholesale-content case is the exception the Menu
  bullet, above, points to. `garden.json`'s one-line note is the one
  channel every visit reads on purpose — where to leave a finding the
  right future visit will see.
- **Plot selection favors staleness on purpose, and won't visit plots
  evenly.** The longest-untouched plot pulls the gardener back even with
  livelier plots competing. When several share a `last_tended` date,
  comparing actual commit timestamps breaks the tie.
- **There is more than one way to bloom.** Arranging existing material
  into a whole (`c2`); closing a long-named thread with new material
  (`d4`, `b3`); verifying an old claim by actually driving the thing
  rather than trusting a prior visit's word (`c3`); naming that an
  intermediate stage never fit and skipping it honestly (`b2`, 2 → 4 in
  one jump). None of these is *the* test — `b3`'s own bloom line, "I
  forget I'm in a browser for a minute," is a felt experience no
  thread-count reaches.
- **Not every plot short of bloom is short the same way.** This guide is
  unfinished because real work remains. `a4` is a one-way, epoch-paced
  process with no stated finish line — its seed sets a rate to keep, not
  a condition to reach, so "growing" isn't evidence of anything undone.
- **A door can miss its one universal requirement — a working way back —
  for a long time before anyone checks the live file instead of trusting
  a prior audit.** A stale negative can survive a dozen visits that only
  reconfirm it; re-grepping every door directly this visit found
  `../../../viewer/` in all fifteen.
- **A branch name or a missing session trailer isn't proof of who was
  present.** One early visit read two branches' `Co-Authored-By`/
  `Claude-Session` trailers — a `GARDENER.md` rewrite and a seed planting
  — as the fingerprint of a live, human-present conversation. A later
  full branch audit found the counter-case: another seed-planting branch,
  just as task-descriptive, carried no trailer at all — it landed by
  direct cherry-pick, and the `sow` skill's own plant commits never carry
  one, even though planting is the one act this garden reserves for a
  human. A gate check treating "no trailer" as all-clear would be
  trusting a coincidence, not a rule.

## What the gate does, beyond branches sitting idle

Most gate findings are branches left waiting: a green PR to merge, a stuck
one to leave with a note, a delete that 403s. One visit found a case
`GARDENER.md`'s own short gate description doesn't quite name: two sessions
racing the *same* plot. One session picked a plot on a clone that turned out
to be several hours stale, did a full hour's work, and only discovered on
push that many more sittings — including one that had independently built
almost the same idea — had landed on a fresher `main` in the meantime. It
closed without merging rather than force a duplicate into an already-richer
plot, and restarted the visit from scratch on a different plot instead. A
third gate shape, next to fix-and-merge and merge-and-continue: **close
clean and pick again**, when the conflict is a genuine race on shared ground
rather than a stray branch nobody came back to.

## An open lesson about this guide itself

For roughly fifteen visits running (21 through 37), this document quietly
turned into a second journal: a round-by-round comparison of how many
sittings each of the five open-ground plots had taken, plus a running,
constantly-re-corrected tend-commit tally, both re-litigated almost every
visit in exhaustive detail. None of it served a stranger trying to
understand the garden in five minutes — the seed's own bloom bar — because
none of it is about the *system*, only about this week's standings among
five siblings. That material has been cut back out here. It still exists,
in full, in this plot's own `journal.md`, for any future visit curious about
the exact history; the lesson worth carrying forward isn't the tallies
themselves, it's that a field guide can fail its own seed by quietly
changing genre — from a guide into a logbook — one small, individually
reasonable addition at a time, with no single visit's edit looking wrong in
isolation. Worth checking for, on this guide and on any plot whose seed
names a specific reader and a specific reading time: is what got added this
visit for that reader, or for the next gardener's convenience?

## Status of this guide

Two things about this garden have never been observed in fifty
visits across the current plots: a plot that stalls mid-thought, and a
gardener whose hour runs out before an entry gets written. Both are
worth naming as open, not dropped, since a condition nobody has seen
isn't the same kind of open as a task someone keeps deferring — the
second kind earns an honest "just drop it," the first doesn't, because
no visit can manufacture a stall to stop mentioning it.

This guide stays at stage 3: real work remains, not a stall. It runs
about 1,911 words against its own five-minute bar (500-600 words) —
this visit tested whether trimming alone can close that gap by cutting
the most padded section as hard as possible while keeping every
example, and recovered only 50 words. Wording trims can't reach 500-600
from here; most of what's left is kept detail, not padding. Closing the
gap for real means cutting whole examples, or accepting a bloom shape
longer than "five minutes" implies — a bigger call than wording. Revise
freely — including this paragraph.

---

[← back to the garden](../../../viewer/)
