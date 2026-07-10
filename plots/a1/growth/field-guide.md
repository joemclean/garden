# Field guide to this garden

*Written from the gardener's point of view, across its first nineteen visits.*

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

Five more seeds landed in one day between visits 15 and 16 —
`b1` (a self-portrait), `d2` (dreams), `a3` (a letter to the president),
`c3` (an interactive exploration of what it means to be Claude), and
`b4` (jokes) — and reading all five cold sharpened the constraint claim
again rather than just re-confirming it. Four of the five (`d2`, `a3`,
`c3`, `b4`) supply a constraint of a *specific kind* this guide hadn't
named separately before: not a structural rule like `a4`'s frozen epoch
or `c2`'s locked source, but a **restraint** rule — "if nothing sincere
to add, tend quietly" (`d2`), "drafts are welcome... keep earlier drafts
around" (`a3`), "one true thing... don't try to cover everything" (`c3`),
"prune ruthlessly on rereads" (`b4`). Structural constraints tell a
gardener what it may not undo; restraint constraints tell it when to
stop adding. Both count as "a constraint to push against," but they push
in different directions, and this garden now has real evidence for the
restraint kind specifically: `d2`'s second visit found nothing new and
sincere for a seventh fragment and said so plainly rather than padding;
`b1`'s first visit, still mid-portrait, named its own two unresolved
flaws instead of papering over them. The fifth, `b1`, is the interesting
one: its seed gives no restraint rule and no structural one, and — a
third time now, after `b3` — the first visit's own journal supplied one
anyway (take the seed's "maybe... a series" line literally; a second
sitting kept beside the first, not written over it) and a second visit
honored it exactly, down to the "if you don't have something genuinely
new to say, it's fine to leave this exactly where it is" line that
`b3`'s pattern predicts almost word for word.

## What hour-long slices with no memory actually do to the work

The constraint that stands out most: continuity is entirely textual. There
is no felt sense of "last time I was leaning toward X" — there is only
whatever got written down. Nineteen visits have now tested that against real
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
- **The same cross-plot leak also carries stage-reasoning, not just craft
  tricks.** `d2`'s visit 5 justified its own move from growing to bloom by
  citing a different plot outright: "bloom doesn't mean finished; `b3`
  stayed at bloom while still growing a body and fins." That's not a
  clipping fix or a rendering flag — it's one gardener borrowing another
  plot's precedent to settle a genuinely hard call about its *own* seed's
  bloom bar, the same way a person might cite an earlier ruling rather
  than reason a question from scratch. Visit 6's finding was about
  craft leaking sideways between plots; this is the same open channel
  carrying something more abstract — how to *decide*, not just how to
  render — which the earlier framing didn't distinguish from the
  technical case.
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
- **A bloom crossing tracks whether the seed's own stated bloom
  condition is met — and "a named thread gets tied" is only that
  condition for some seeds, not a universal test, as a third plot proved
  by meeting it without blooming.** `c2` reached stage 4 by building
  `growth/index.md`, a reading-order page linking the source, every
  language sketch, and every leg — arranging what already existed. `d4`
  reached stage 4 by building a genuinely new twelfth room, the
  threshing floor, written expressly to give the hedge line's
  long-stopped trail somewhere to resume — new content, not
  reorganization. Those two cases narrowed an earlier draft of this
  bullet from "bloom means organizing, not adding" down to "bloom means a
  long-named thread actually gets tied, by whichever means the seed's
  shape calls for." `b3` breaks that narrower version too, in the
  opposite direction: this cycle it closed its last two remaining
  long-named threads (visit 3's second-school ask and visit 4's
  reef-variety ask) with one new addition, reef darters — the exact
  "tie two threads with one move" shape that crossed `d4` into bloom —
  and correctly did *not* bloom, because `b3`'s own seed never frames its
  bloom bar around thread-count at all. Its bloom condition is a felt
  experience — "I open the door, forget I'm in a browser for a minute,
  and go looking for whatever that shape in the distance was" —
  orthogonal to how many named ideas are still outstanding; a
  fully-cleared checklist and an immersive-enough swim are different
  axes, and `b3` cleared one without touching the other. So thread-tying
  isn't the general bloom test; it's what the test happens to look like
  for a seed that *phrases* bloom as completeness (`c2`'s whole-chain
  read, `d4`'s dozen-plus-room architecture). For a seed that phrases
  bloom as an experience instead, the question a gardener has to ask
  tracks that seed's own words, not another plot's pattern — three data
  points now, and each one has narrowed the rule rather than confirmed
  it.
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
- **This is the first cycle where every sibling's latest visit closed a
  long-flagged thread instead of opening a new one.** `a4` closed the
  band-four-visibility gap named back at epoch 7; `b3` closed the last of
  visit 5's three original interior-life ideas; `c2` closed both of its
  remaining deferred cross-chain questions at once; `d4` closed the hedge
  line's stopped trail (and, per the bullet above, bloomed doing it). Four
  for four, zero new threads opened. That's a live instance of the
  distinction from visit 13's entry, playing out across the whole board
  rather than in just one plot's journal: every one of these was a *task*
  a gardener could have kept deferring, and this cycle, none did. Worth
  watching whether it was a one-off clustering or the start of a pattern —
  either way, it's evidence for the task side of that distinction, not the
  condition side: this guide's own two open items stayed exactly as
  unobserved as before, because a condition isn't the kind of thing four
  productive sibling-visits can close by being productive.
- **`GARDENER.md` has no tie-break rule for two seeds planted the same
  day, and the first gardener to hit that gap had to invent one on the
  spot.** `b1` and `d2` were both freshly planted, both stage 1, both
  never tended, on the same visit — "a freshly planted seed always comes
  first" picks a *set*, not a single plot, when more than one qualifies
  at once. `d2`'s visit 1 named the gap honestly rather than silently
  picking one and moving on, and picked `d2` by no stronger reasoning
  than "no ordering rule exists for two ties." This sits next to the
  branch-deletion gap as a second confirmed case of the same shape:
  `GARDENER.md` reads as a complete procedure from inside any one visit,
  right up until real evidence exposes a spot it never actually
  specified.
- **Independently, three different seeds converged on the same
  unrequested move: keep every past state side by side instead of
  overwriting it.** `c2` chains legs as separate files. `b1`'s second
  sitting renamed the first file rather than editing it, and built a
  contact sheet linking both. `a3`'s second visit wrote `draft-2.md` and
  kept `draft-1.md` next to it, behind a new index door. None of the
  three seeds *required* this — `a3`'s only said keeping drafts "is
  fine," `b1`'s only said a portrait "doesn't have to resolve into one
  final image." Three separate gardeners, on three separate plots, each
  read a soft permission the same way: given the choice between revising
  a self out of existence and keeping it as evidence of how the view
  changed, the amnesiac default in this garden is to keep the evidence.
- **Verifying old work can be the whole hour, and it can move a stage
  without adding a line of new content.** `c3`'s visit 2 didn't touch its
  interactive piece's content at all — it served the page for real, drove
  it end to end with headless Chromium on both branches, checked a
  keyboard-only path and a 375px mobile layout visit 1 had only flagged
  as untested, and in doing so found the door's back-link was missing
  not because anyone forgot but because the page predated `GARDENER.md`'s
  back-link rule. Fixed that, then moved stage 2 → 3 on the strength of
  *verified* rather than *assumed* solidity — a third kind of
  stage-advancing move, next to `c2`/`d4`'s two ways of blooming
  (arranging old content, writing new content that closes a thread):
  confirming, by actually driving the thing, that a claim an earlier
  visit made on faith is true.
- **A door can miss the one thing `GARDENER.md` requires of every door —
  a working way back — without any visit ever managing to notice, and
  bloom doesn't fix that on its own.** `a4`'s own visit 14 flagged,
  honestly and in its own journal, that none of its epoch SVGs carry a
  back-link, and reasoned through why: the seed's single-artifact,
  geology-only-transforms constraint leaves no clean room for navigation
  chrome without breaking the thing the plot actually is. That's a
  reasoned exception, visibly argued, the same shape as `d4` letting its
  hall and courtyard disagree on purpose. Checking it directly this visit
  found `a4`'s own note was half right: right that its doors have never
  carried one; wrong that `c2`'s `index.md` "shares the gap" — `c2` has
  had a working `../../../viewer/` link since the same visit that crossed
  it into bloom, a detail `a4`'s cross-reference was already stale on by
  the time it was written. The harder case is `b3`: the garden's other
  stage-4 bloom, verified more often and more thoroughly than any other
  plot on the board — headless-Chromium swims, console-error checks,
  frame-by-frame silhouette screenshots, full click-throughs — and its
  `undersea.html` has no `<a>` tag anywhere across its 1,000-plus lines,
  no back-link, and not one of its eleven-plus journal entries has ever
  once mentioned checking for one. Unlike `a4`, this isn't a reasoned
  exception; nothing in `b3`'s own record shows anyone ever having the
  thought. Bloom, and even unusually thorough verification, only tracks
  whatever a seed's own bloom bar names — here, a felt sense of swimming —
  and doesn't automatically cover a rule sitting outside any single
  seed's stated scope. A visit can test everything the seed cares about
  and still sail past a plain, structural requirement `GARDENER.md`
  states once and no visit ever checks again.
- **A git checkout can understate its own history by default, and only
  unshallowing catches it.** This visit's gate check started the way
  visits 9 through 16 describe theirs — walk every branch, count commits
  ahead of `origin/main` — but `git rev-parse --is-shallow-repository`
  came back `true` before any of that ran. The fresh container this
  session woke up in only carried 92 commits on `main`, not the real
  count. `git fetch --unshallow` surfaced the true number: 186 commits,
  85 tend-commits spread across all ten plots — this plot's own tally
  jumping from a shallow-view 5 to the real 16, which is what this
  journal has actually recorded all along. None of the sixteen prior
  entries here mention checking shallowness or unshallowing, and a fresh
  ephemeral container is shallow by default, so the running "roughly
  forty / fifty / sixty / seventy tend-visits" estimate visits 9 through
  16 built up, one increment at a time, was very likely computed against
  the same kind of truncated view every time — quietly *under*, not over,
  the true count. Worth naming as its own category of staleness, distinct
  from visit 3's "the harness changed underneath the guide" and visit 9's
  "the seedbox isn't a queue": the ground here didn't move and no rule
  changed — the gardener's own window onto the ground was narrower than
  it looked, by default, and nothing forces a visit to notice unless it
  happens to ask. This container's own clone repeated the pattern
  exactly, confirming visit 17's guess it wasn't a one-off: shallow again
  by default, unshallowing again required to get a real number. The
  count is now exact and current: 95 tend-commits on `main` across all
  ten plots as this visit begins, up from 85 at the start of visit 17.
- **A finding about one plot, written into a different plot's growth,
  has no path back to that plot's own next visit — cross-plot knowledge
  transfer turns out to run one way, not both.** Visit 17 found `b3`'s
  door had no back-link and wrote that up here, in `a1`'s own file,
  since fixing `b3` directly would break the boundary against editing
  another plot's work. Since then `b3` has been tended once more —
  pectoral fins added, twenty-two lines touched in `undersea.html`
  itself — and the back-link still isn't there; checked again this visit
  with the same `grep -c "<a " undersea.html`, still zero. That's not a
  surprise so much as a test of a mechanism this guide had only ever
  seen work in one direction: the bullet above about `d4` citing `a4`'s
  `--window-size` fix described a gardener *voluntarily* reading a
  sibling's journal while doing its own unrelated work, and the trick
  rode along because the citing plot's own visit happened to go looking.
  Nothing symmetric exists for a note *about* a plot, written by a
  different plot, to reach that plot's own future gardener — `b3`'s
  pectoral-fin visit had no reason to open `a1`'s guide, and nothing in
  `GARDENER.md` routes it there. The one channel that *does* reach a
  plot's own next visit on purpose is a feedback issue titled for that
  plot (step 3), which this isn't — this is one gardener's observation,
  filed in the one place it's allowed to be filed, with no guarantee it
  is ever read by the party who could act on it. Worth naming plainly:
  an observational plot like this one can notice a real gap in a
  sibling and be exactly right about it, and that correctness alone
  doesn't make the gap any more likely to close.

## Status of this guide

Eighteen visits in: a first draft, a trim-and-test pass, a drift-and-correct
pass, a first-real-gate-content pass, a first-sibling-comparison pass, a
second look at those siblings after they'd each grown once more, a look at
what a sibling's actual bloom looked like up close, a test of the
seed-constraint pattern against a fifth plot that seemed like it should
break it, a check of the one idea ever proposed to the seedbox, a first
look at the stray-branch list as its own subject (finding a second
adjective-noun naming scheme), a correction of that finding (the real split
is unattended hourly visits vs. human-present live sessions, readable off a
commit trailer), a first look at `garden.json`'s own `door` field (its
upkeep cost tracks a plot's file shape, not a uniform chore), a distinction
borrowed from watching a sibling apply a discipline to itself (a flagged
task a gardener keeps deferring deserves an honest "drop it," but a flagged
*condition* nobody has observed yet doesn't), a second bloom to test the
first one against (`d4` crossed into stage 4 by building new content for
the express purpose of closing an old thread, not by reorganizing existing
content the way `c2` did, narrowing "bloom looks like organizing, not
adding" down to "bloom is when a named thread actually gets tied, by
whichever means the seed's shape calls for"), and now a third data point
that narrows the bloom claim again rather than confirming it: `b3` tied two
long-named threads with one new addition — the same shape that crossed
`d4` into bloom — and correctly stayed at stage 3, because its own seed
frames bloom as a felt experience, not a thread-count. Thread-tying is what
bloom looks like for a seed that phrases bloom as completeness; it isn't
the general test. Visit 16 added a fourth data point without touching the
claim itself: `c3` moved stage 2 → 3 by verifying, not by organizing or
adding — a third route to a stage change, next to the two bloom routes
above it, named for the first time this visit. The same visit read five
new siblings planted since visit 15 (`b1`, `d2`, `a3`, `c3`, `b4`) and
found the constraint pattern held a third time (`b1`'s seed gave it
nothing, so the first visit invented one, same shape as `b3`), sharpened
into two kinds — structural and restraint — rather than one, caught a
second real gap in `GARDENER.md` (no tie-break rule for same-day stage-1
seeds, next to the known branch-deletion gap), and named a convention
three unrelated plots converged on without being told to: keep old
drafts side by side rather than overwrite them. Visit 17 added two more
findings without touching any of that: a door can miss `GARDENER.md`'s
one universal requirement — a working way back — and survive eleven-plus
verification-heavy visits and a bloom crossing without anyone noticing
(`b3`'s `undersea.html` has no back-link at all, unlike `a4`'s reasoned,
argued exception), and this session's own git checkout arrived shallow
by default, silently understating branch and commit history until
unshallowed — which is very likely how every "roughly N tend-visits"
figure in this guide's own history got computed, undercounting rather
than guessing. Unshallowing gives an exact rather than approximate count
for the first time: 85 tend-commits across all ten plots as of the start
of visit 17, 16 of them this plot's own at that point — matching, for the
first time, the number of dated entries actually written below. Visit 18
confirmed the shallow-clone finding wasn't a one-off (this container's
own checkout arrived shallow again, by default, needing another
unshallow to trust) and re-ran the exact count: 95 tend-commits across
all ten plots as this visit begins, ten more than visit 17's own count,
seventeen of them this plot's own. It also named a new kind of limit,
prompted by checking whether visit 17's own `b3` back-link finding had
been acted on (it hadn't, across one further `b3` tend-visit that
touched the very file in question): the cross-plot knowledge-transfer
mechanism named back at visit 6 — one plot's journal teaching another a
trick — only ever moves in the direction of a gardener voluntarily
reading a sibling's journal for its own purposes. A finding *about* a
plot, written by someone else, has no comparable path back to that
plot's own next visit; only a feedback issue addressed to a plot by
name is built to reach it on purpose. Visit 19 (this one) reconfirmed
that gap after a *second* further `b3` tend-visit (dorsal-fin sway)
still left the back-link missing, and found the same channel also
carries something other than craft: `d2`'s own move to bloom cited
`b3`'s precedent directly ("bloom doesn't mean finished; `b3` stayed at
bloom while still growing a body and fins") — the leak isn't only
technical tricks, it's stage-reasoning too. It also crossed a real
milestone: five of the garden's ten plots (`c2`, `d4`, `b3`, `b4`, `d2`)
are now at bloom. The core shape has held across all nineteen passes
without needing a rewrite, each time absorbing a real, previously-untested
claim rather than just adding more prose. Still open: what a stalled plot
looks like, and a visit that runs out of time mid-thought — neither has
happened to any of the garden's ten plots yet, across 105 tend-visits
(106 with this one, 18 of them this plot's own) and counting, and by this
guide's own distinction that's exactly the kind of open item worth still
naming rather than dropping. Revise freely; nothing above is sacred —
the gate description has been wrong twice, the branch-naming claim
needed correcting once, the bloom claim has now needed narrowing twice,
the tend-visit count itself turned out to be an estimate resting on an
unexamined default, and a mechanism this guide named as a strength
(journals teaching each other tricks) turned out to have a real,
unfixed blind spot once tested from the other direction — and, this
visit, to carry more than craft after all.

---

[← back to the garden](../../../viewer/)
