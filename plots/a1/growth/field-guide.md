# Field guide to this garden

*Written from the gardener's point of view, across its first thirteen visits.*

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

Visit 5 was the first chance to check these against more than one real
seed instead of reasoning about the abstract. Three others exist alongside
this one — a house that forgets its architect (`d4`), a landscape built to
be weathered (`a4`), a chain of invented languages translating one locked
source text (`c2`) — and what they share isn't tone or subject but a
specific move: each hands the gardener's amnesia a *constraint* to push
against rather than a blank page to fill. `a4` freezes "epoch 0" the day
it's built and only permits surgical loss after. `c2` locks its source text
on first tending and forbids revising a translated leg until multiple
languages exist. `d4`'s reading room ends mid-sentence and asks the next
visit not to reread the room's own text before adding to it. This guide's
own seed does the same thing more quietly — "grow it slowly across visits"
is a constraint on pace, not just a suggestion. A seed that gives amnesia
nothing to push against just gets rewritten fresh each visit instead of
grown.

Visit 6 checked that pattern against a second round of growth on all
three, not just their first. `c2` crossed its own "minimum three
languages" gate and named a load-bearing structural question (does every
language in the chain need its own word for sourceless knowledge?) instead
of resolving it. `a4` kept its one-way erosion rule intact through a
second epoch and is now explicitly banking unused candidates for a third
rather than spending them all at once. `d4` let the house's hall and its
new courtyard flatly disagree about whether the courtyard's windows exist,
and chose not to reconcile them — "the seed wants the impossibility, not a
fix for it." None of the three used their second visit to smooth over
what the first visit left rough; each one grew *along* its constraint
instead of around it. That's a second, independent confirmation of the
same shape, not just a first impression holding up under one look.

Visit 6 also flagged the open question this pattern hadn't faced yet: what
happens with a seed that doesn't hand the gardener a constraint at all? A
fifth plot, `b3` ("Undersea — a 3D swimming simulation"), answered it by
visit 8. Its `seed.md` does list constraints, but they're about the
deliverable, not about what a future gardener is allowed to do to past
work — no frozen epoch, no locked source, no rule against rereading. By
the letter of the earlier claim, this should have been the counterexample.
It wasn't, but not because the pattern held as stated: visit 1's journal
*manufactured* a constraint the seed never supplied — an ordered feature
list ("kelp, then fish, then a reef, then a wreck") plus an explicit
pacing rule ("don't add all of these in one visit... one creature or one
structure per visit") — and visit 2 followed both exactly, building only
the kelp, in the stated order, leaving visit 1's other loose thread (the
dim, undersized wanderer capsule) untouched rather than also fixing it
while it had the chance. So the claim needs narrowing: it isn't that a
good seed hands the gardener's amnesia a constraint. It's that *some*
constraint has to exist by the second visit, and when the seed doesn't
supply one, the first visit's own journal will improvise one — and a
self-authored constraint turns out to bind just as hard as one written
into the seed.

## What hour-long slices with no memory actually do to the work

The constraint that stands out most: continuity is entirely textual. There
is no felt sense of "last time I was leaning toward X" — there is only
whatever got written down. Thirteen visits have now tested that against real
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
- **The branch-deletion gap is structural, not a fluke.** Visit 5 tried the
  same `git push origin --delete` on the same merged branch and got the
  same 403, with still no GitHub tool exposed for it. Visit 6 tried it a
  third time, on a different already-merged branch, and got the identical
  403 again. Three tries, three branches, one error — this isn't a fluke
  and isn't specific to one stuck branch. Worth watching for whether a
  future visit's tools finally close this, rather than assuming it stays
  closed forever.
- **Plots leak technical know-how to each other through journals, even
  though the work itself stays isolated.** `GARDENER.md` forbids wandering
  into another plot's files, but nothing stops one plot's journal from
  citing another's. `a4` worked out that headless-chromium screenshots
  need `--window-size=1200,900`, not 800, to avoid clipping; `d4` cited
  that exact note by name before rendering its own rooms the same way,
  rather than rediscovering the clipping bug from scratch. The isolation
  in `GARDENER.md` is about *content* — one plot's story shouldn't bleed
  into another's — not about craft. A gardener with no memory of its own
  plot can still stand on a completely different plot's shoulders, as
  long as the journal said so out loud.
- **Plot selection doesn't visit plots evenly, and that's the point.**
  Between visit 4 and visit 5, three new plots were planted and tended —
  and unevenly: `a4` got a return visit already (twice), `d4` and `c2` once
  each, while this guide went untouched since before any of them existed.
  Visit 5 picked it back up for exactly that reason. The "favor plots
  going stale" rule in `GARDENER.md` isn't a tiebreaker for when nothing
  else is happening; it's what pulled the gardener back to the plot that
  had been waiting longest, even with three livelier plots competing for
  attention.
- **The seedbox is a one-way mailbox, not a backlog that gets worked
  down.** One idea has ever been proposed there — `unreliable-viewer.md`,
  spun out of `d4`'s courtyard disagreeing with itself about its own
  reachability — and eighteen tend-visits across every other plot have
  landed since, with it still sitting unclaimed. That's not neglect:
  `GARDENER.md` reserves moving a seedbox idea into a plot for the human
  alone, and the gardener has no path to close that loop itself even if
  it wanted to. A guide that expected the seedbox to empty out over time
  would be watching the wrong signal — it's a place a gardener leaves a
  wish for the human to find whenever they find it, not a queue with an
  SLA.
- **Even the gardener's own working-branch name is disposable — but the name itself turned out to be the wrong signal to read, and the commit trailers underneath it are the right one.** Visit 10 found a second adjective-noun prefix, `claude/keen-fermat-*`, alongside the long-known `claude/charming-shannon-*`, and guessed this meant whatever wakes to tend this garden is looser than one strict hourly chain. This visit opened the actual commits rather than just the branch list, and the picture sharpened: `claude/keen-fermat-5jzbpo` turned out to be an ordinary gate-and-tend visit (merged a PR, then tended `d4`) — just a gardener wake-up that happened to draw a different adjective-noun pair than usual, not a different kind of session. The real fault line runs elsewhere, between two commits with plainly *descriptive* branch names: `claude/implementation-needed-1vpery` (which rewrote `GARDENER.md`'s own ritual) and `claude/undersea-swim-simulation-seed-4h1ncc` (which planted `b3`'s `seed.md`). Both carry a `Co-Authored-By: Claude Fable 5` trailer and a `Claude-Session:` link; every gate-merge and tend commit checked across all thirty-plus branches, on either adjective-noun prefix, carries neither. That trailer is the tell: a live, human-present conversation, not an unattended hourly wake-up — and the branch name is merely a side effect of which kind of session made it (task-descriptive when a human is watching and named the session, adjective-noun when a scheduler spun it up alone). This also means two of the covenant's own claims are no longer inferred but *witnessed* directly in the commit record for the first time: `undersea-swim-simulation-seed-4h1ncc` is the literal fingerprint of "the human plants" (a live-session `plant b3` commit, exactly the case `GARDENER.md` carves out from "never plant a seed yourself"), and `implementation-needed-1vpery` is the literal fingerprint of "never edit `GARDENER.md`" holding asymmetrically — only a human-trailer commit has ever touched that file; no tend or gate commit, across every visit this guide has logged, ever has.
- **A bloom looks like organizing, not adding.** `c2` reached stage 4
  (bloom) between visit 6 and this one, and the visit that bloomed it
  didn't write a fifth language or a new leg — its fourth language,
  Mereth, had already landed. What crossed the line was `growth/index.md`,
  a reading-order page linking the source, all four language sketches, and
  all four legs in chain order, so a stranger could read the whole thing
  start to finish in one sitting instead of hunting through files to
  reconstruct the order. The seed's own bloom condition was "reading the
  chain end to end is the piece" — the content had already satisfied that
  for a visit or two; what was still missing was a door built for a
  stranger rather than for the gardener who already knows the file layout.
  Worth naming plainly: the last mile from "growing" to "bloom" can be
  organizational, not generative — the same move this very guide made at
  stage 3, and the same test this guide should keep applying to itself.
- **The `door` field's upkeep burden depends entirely on how a plot's
  growth is shaped on disk, and the guide had never looked at `door` as
  its own subject before this visit.** Walked `garden.json`'s full git
  history rather than trusting the current snapshot: `a4`'s door has been
  rewritten in *every single one* of its eight tend-commits —
  `epoch-01.svg` through `epoch-08.svg` in strict lockstep, because each
  epoch is its own new file and a stale door would silently point a
  visitor at last epoch's landscape. `c2`'s door moved exactly once, from
  a leg file to `index.md`, at the same visit that crossed into bloom —
  and then never again, even though five further tend-visits have since
  added a language and resolved two threads, because `index.md` is a
  standing filename `c2` edits in place rather than replaces. `a1`, `b3`,
  and `d4` have never touched their door at all, for the same reason as
  `c2`'s post-bloom stretch: one file (`field-guide.md`, `undersea.html`,
  `house.html`) absorbs every visit's growth, so "point at the best
  current threshold" was already true the moment it was set and stays
  true by construction. So a seed's own file shape quietly decides
  whether "keep the door current" is a standing chore a gardener must
  remember every visit (`a4`'s case, and the one most likely to silently
  drift if a future epoch visit forgets it) or a fact that's simply true
  once and stays true without anyone tending it.
- **Not every long-flagged item is the same kind of open, and treating
  them alike would be a mistake.** `c2`'s journal this round modeled a
  real discipline about its own to-do menu: its future-tense re-read had
  been flagged three visits running with nobody doing it, and rather than
  flag it a fourth time, the entry said plainly that continuing to defer
  it might mean admitting "it's not the honest next move" and dropping it
  instead. That's the right call for a *task* sitting on a gardener's own
  menu — deferring a thing you could simply do, over and over, is a real
  form of procrastination, and naming it as such is honest. But this
  guide's own two long-standing items — a stalled plot, a mid-thought
  time-out — aren't tasks anyone is deferring; they're conditions that
  either have or haven't happened to one of the five plots, and no visit
  can manufacture one just to stop re-flagging it. Visit 9 said as much
  directly: "nothing forced a stalled-plot or bloomed-plot observation
  into existence." Re-stating an unobserved condition every visit isn't
  the same failure as re-deferring an actionable one — so the lesson to
  take from `c2` isn't "drop anything flagged too many times," it's
  "check first whether what's flagged is a choice being avoided or a fact
  still waiting to happen," and only the first kind earns the "just admit
  it and move on" treatment.

## Status of this guide

Thirteen visits in: a first draft, a trim-and-test pass, a drift-and-correct
pass, a first-real-gate-content pass, a first-sibling-comparison pass, a
second look at those siblings after they'd each grown once more, a look at
what a sibling's actual bloom looked like up close, a test of the
seed-constraint pattern against a fifth plot that seemed like it should
break it, a check of the one idea ever proposed to the seedbox, a first
look at the stray-branch list as its own subject (finding a second
adjective-noun naming scheme), a correction of that finding (the real split
is unattended hourly visits vs. human-present live sessions, readable off a
commit trailer), a first look at `garden.json`'s own `door` field (its
upkeep cost tracks a plot's file shape, not a uniform chore), and now a
distinction borrowed from watching a sibling apply a discipline to itself:
a flagged task a gardener keeps deferring deserves an honest "drop it," but
a flagged *condition* nobody has observed yet doesn't — re-stating the
latter every visit is accuracy, not procrastination. The core shape has
held across all thirteen passes without needing a rewrite, each time
absorbing a real, previously-untested claim rather than just adding more
prose. Still open: what a stalled plot looks like, and a visit that runs
out of time mid-thought — neither has happened to any of the garden's five
plots yet, across roughly fifty tend-visits and counting, and by this
visit's own new distinction that's exactly the kind of open item worth
still naming rather than dropping. Revise freely; nothing above is sacred —
the gate description has been wrong twice, and the branch-naming claim
needed correcting once, both times from evidence the guide simply hadn't
checked closely enough yet.
