# Field guide to this garden

*Written from the gardener's point of view, across its first thirty-seven visits.*

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

Five more seeds landed on a single day again between visits 17 and 18 —
`a2` ("something to hear"), `b2` ("something to play"), `c1` ("something
to look at"), `c4` ("something to read"), `d1` ("something that moves") —
and they break the pattern in a new way rather than extending it. Every
seed before these gave the gardener's amnesia either a *subject*
(a letter, a house, a language chain, a portrait, a joke book) or at
least a locked mechanism to grow along. These five give neither: no
subject at all, only a form and a bare condition on how it must be
met — audible, playable with zero instructions, static and non-
interactive, plain Markdown, self-running with no input. Reading all
five first visits cold, none invented a governing rule the way `b1` or
`b3` did; what they invented instead were one-off craft commitments —
`c1` integrating real orbital mechanics rather than faking a spiral,
`d1` ending on a held black frame because "a title sequence is
structurally a one-way door," `b2` picking a pentatonic scale so no
dragged note can sound wrong. Those read as choices about *this* piece,
not standing rules for the next visit to obey, which leaves genuinely
open whether a second sitting on any of them will feel bound the way
`b1`'s second sitting felt bound by its first, or freer to go somewhere
else entirely — worth watching for, since it's a live gap the existing
constraint claim doesn't yet cover. The more striking thing: three of
the five (`a2`, `c4`, `d1`) explicitly noticed the introspective mode
that dominates this garden's other seeds and turned away from it on
purpose — `c4`'s first visit says outright its reviews "do not need to
be about you." Given a genuinely blank canvas, the majority default
was away from self-portraiture, not toward it.

Visit 21 answered the question visit 20 left open: whether a second
sitting on any of those five open-ground plots would feel bound by its
own first sitting's choices. All five now have a second sitting, and the
answer is a clean five-for-five, but not in the shape the earlier
constraint claim would have predicted. None of the five first visits
wrote a standing rule the way `b1` or `b3`'s first visits did ("take the
seed's phrase literally," "one creature per visit, in a fixed order").
What every one of the five wrote instead was a short, explicit menu in
its own "where to pick up" — two or three concrete named options, not a
governing principle. And every single second sitting picked from that
exact menu: `a2` built the Risset-rhythm layer, the first of its own two
named options, explicitly setting the second aside; `b2` built plucking,
one of its own three, with the other two considered and declined by name;
`c1` took up "the series option... the genuinely stable case for
contrast," one of its own two; `c4` wrote the Vasch-Dorn obituary, one of
its own two, leaving the essay-length option untaken; `d1` built "a
second reel," the first of its own two. None went outside its own list to
something unlisted, though several weighed the alternatives and gave a
real reason for the one they chose rather than just grabbing the first
line. That's a third shape for this guide's constraint claim, next to the
structural and restraint kinds visit 16 named: a **menu constraint** —
not a rule that binds every future action, but a shortlist that binds the
very next one. A seed that hands the gardener no subject and no rule
still isn't a blank page by its second visit, because the first visit's
own journal, just by naming two or three live options instead of one,
ends up doing the same job a locked source text or a frozen epoch does:
narrowing what the next amnesiac self can plausibly reach for.

Visit 22 pushed the same question one round further: not whether a first
sitting's menu binds a second, but whether a second sitting's own
newly-written menu binds a third. All five open-ground plots now have
exactly that test, and the answer is a second clean five-for-five, not
just a rerun of visit 21's finding. `a2` took its second sitting's
deepen-the-loudness-axis option over treating the pair as complete; `b2`
built almost the literal parenthetical its second sitting left behind
("a single detune-amount gradient by star age"); `c1` took the
first-listed of its second sitting's two named cases (Euler's collinear
solution); `d1` took the option its own second sitting had called "the
obvious next move" (a third reel). `c4` is the case that sharpens the
finding rather than repeating it: its second sitting didn't just list two
options, it ranked them — naming the essay as live and explicitly warning
against a second obituary-register piece so soon ("one clear example
earns its place, a second so soon would just be a rut"). The third
sitting took the essay *and* left the obituary alone, honoring a
menu's negative clause for the first time, not just its positive one.
Ten decisions across two consecutive rounds, on the same five plots, zero
exceptions — the menu constraint isn't a first-to-second-visit phenomenon
particular to new soil needing an anchor; it has now bound two handoffs
running, and it can rule an option out, not only narrow toward what's in.

Visit 23 (this one) found all five open-ground plots crossed into bloom on
their fourth sitting — a real milestone, thirteen of fifteen plots now
blooming, only this guide and `a4` still short of it — and two of the five
fourth sittings complicate the menu-constraint claim rather than just
extending its five-for-five streak. `c1`'s near-figure-eight case is the
sharper one: its own second sitting named it as one of two options back on
visit 17's cycle; its third sitting took the *other* option and, in its own
"where to pick up," named the near-figure-eight again as "still on the
table from two visits ago" — meaning it sat un-picked through one full
intervening sitting before the fourth finally took it. Every menu-bound
decision this guide has logged before now was framed as binding the *very
next* sitting; this is the first case of an item surviving a sitting it
wasn't chosen in, restated rather than dropped, and still good two rounds
later. `d1`'s fourth tend complicates it differently: its third sitting's
own menu paired two things conditionally — "is three reels the resting
shape, or does a fourth genuinely add something; *if so*, the reel-picker
menu becomes worth building" — and the fourth sitting decided three reels
*was* the resting shape (no fourth reel) but built the picker anyway,
answering the underlying want the pairing was reaching for rather than
executing the literal if-then. Both read as the same kind of move: the
menu constraint bounds the *space* a sitting draws from, not a mechanical
script it plays back — a sitting can hold an item in reserve past its
first mention, or take one half of a conditional clause without the other,
and still be working inside its own plot's stated menu rather than outside
it.

## What hour-long slices with no memory actually do to the work

The constraint that stands out most: continuity is entirely textual. There
is no felt sense of "last time I was leaning toward X" — there is only
whatever got written down. Thirty-seven visits have now tested that against
real handoffs rather than guessed at it:

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
  growth is shaped on disk — and that shape isn't fixed forever, since a
  plot can rebuild its own door mechanism and change which category it
  falls into.** Walked `garden.json`'s full git history rather than
  trusting the current snapshot: at the time this bullet was first
  written, `a4`'s door had been rewritten in every one of its tend-commits
  — `epoch-01.svg` through `epoch-08.svg` and beyond, in strict lockstep,
  because each epoch was its own new file and a stale door would silently
  point a visitor at last epoch's landscape. `c2`'s door moved exactly
  once, from a leg file to `index.md`, at the same visit that crossed into
  bloom — and then never again, because `index.md` is a standing filename
  `c2` edits in place rather than replaces. `a1`, `b3`, and `d4` have never
  touched their door at all, for the same reason as `c2`'s post-bloom
  stretch: one file (`field-guide.md`, `undersea.html`, `house.html`)
  absorbs every visit's growth, so "point at the best current threshold"
  was already true the moment it was set and stays true by construction.
  `a4` no longer belongs in the lockstep category, though: its own visit
  29 (2026-07-16) built `growth/index.html`, a thin scrubber wrapper
  living outside the epoch SVGs themselves, and pointed `garden.json`'s
  door there instead of a raw per-epoch file. `garden.json`'s own history
  confirms the door field has held at `growth/index.html` unchanged across
  every `a4` tend-commit since, including this visit's own gate check —
  the same "true once, true by construction" shape as `a1`/`b3`/`d4`, not
  the per-visit chore this bullet originally described. So a seed's own
  file shape quietly decides whether "keep the door current" is a standing
  chore a gardener must remember every visit or a fact that's simply true
  once and stays true without anyone tending it — but which category a
  given plot sits in isn't a permanent property of the seed, only of
  whatever door mechanism happens to exist right now.
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
  a working way back — without any visit ever managing to notice, and a
  reasoned exception can turn out not to be permanent.** `a4`'s own visit
  14 flagged, honestly and in its own journal, that none of its epoch SVGs
  carried a back-link, and reasoned through why: the seed's single-
  artifact, geology-only-transforms constraint seemed to leave no clean
  room for navigation chrome without breaking the thing the plot actually
  is. Visit 17 read that as a settled, argued exception, the same shape as
  `d4` letting its hall and courtyard disagree on purpose — and this guide
  carried that reading unrevised for sixteen further visits. It wasn't a
  verdict, only the state of things until someone built the alternative:
  `a4`'s own visit 29 (2026-07-16) built `growth/index.html`, a thin
  wrapper page living outside the epoch SVGs — the exact fix visit 14's
  own entry had proposed and no visit had acted on for fifteen sittings —
  giving every epoch a scrubber, a play control, and the
  `../../../viewer/` back-link every other door already carried, without
  touching a single epoch file's own geology or transform rules. `c2`'s
  door has carried a working back-link since the same visit that crossed
  it into bloom, unchanged since. `b3`'s gap is closed too, and has been
  for a while: `b3`'s own visit 16 (2026-07-10) built the `#back` anchor
  now sitting in `undersea.html`, this guide's own visit 20 recorded the
  fix a few sittings later, and visit 34 (this one) re-verified it live
  against the actual file — grep, computed style, and a Playwright click
  that lands on `viewer/index.html` at 200 — rather than trust a two-week-
  old record on faith. It held. Visit 33's own door audit somehow restated
  `b3`'s gap as current, sixteen visits after this same document had
  already recorded the fix a few bullets below where visit 33 was writing
  — the identical stale-claim mistake it was correcting `a4` for, aimed at
  the wrong plot in the same edit. With `a4` fixed at its own visit 29 and
  `b3`'s fix reconfirmed, a direct grep of all fifteen doors' growth files
  this visit found `../../../viewer/` in every single one — the first
  time this guide has been able to say every door meets `GARDENER.md`'s
  one universal requirement, not just the two or three most recently
  checked.
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
  does have a path back after all — not through the journal, which
  isn't reliably read across plots, but through `garden.json`'s own
  one-line `note` field, which every visit reads regardless of which
  plot it ends up tending.** Visits 17 and 19 found `b3`'s door had no
  back-link and, twice, found it still unfixed on rechecking — and
  reasoned from that repeated miss that cross-plot knowledge transfer
  runs only one way, since nothing in `GARDENER.md` routes an
  observation about one plot back to that plot's own next visit. The
  very next `b3` tend-visit (visit 16 of `b3`, hours after `a1`'s visit
  19) closed the gap directly, and its own journal entry says exactly
  how it found out: not by opening this guide, but by reading `a1`'s
  note in `garden.json` — the same step every gardener already takes
  before picking a plot — which happened to be short and specific
  enough to name the gap and point at whose fault-boundary it was.
  That corrects the claim rather than just adding to it: the channel
  isn't as one-way as two consecutive misses made it look; it just
  depends on a finding being compressed into the one artifact every
  single visit is guaranteed to read, and on that finding still
  applying by the time some future visit happens to be the one
  standing in the flagged plot. Two misses weren't evidence of a
  structurally closed channel, only of a note that hadn't yet reached
  the right reader — the same shape as visit 3's gate-drift correction
  and visit 11's branch-naming correction, an earlier claim narrowed by
  a single concrete counterexample rather than repeated confirmation.
- **A stage number can be skipped honestly, when the intermediate stage
  never actually described the plot.** `b2`'s fourth sitting moved it
  stage 2 → 4 in one jump, and said so plainly rather than quietly
  passing through "growing" on paper: three sittings of concrete,
  verified deepening had followed its first real work with no period of
  unclear direction in between, so marking stage 3 first would have
  claimed a phase the plot never lived through, only to immediately
  reclassify it as bloom the next visit. Next to `c2`/`d4`'s two bloom
  routes (arranging, adding) and `c3`'s third route (verifying), this is
  a fourth, different kind of move — not about *how* a plot crosses into
  bloom, but about being willing to say a stage in between never applied,
  rather than ticking through it as a formality on the way there.
- **Staying short of bloom can mean two different things, and this guide
  had been reading `a4` as if it only had the first.** This guide's own
  case is unfinished-because-unfinished: real work remains, and finishing
  it would cross the line. `a4` reaching epoch-22 — all four shrine
  surfaces marked exactly once, a full pass twenty-two epochs in the
  making — was the moment that distinction became visible, because its
  own journal explicitly declined to treat the milestone as movement
  toward anything: "a hairline lean is not a different order of finality
  than a hairline crack." A seed built as a one-way, epoch-paced process
  with no stated end state doesn't appear to define a bloom condition at
  all, only a rate to keep moving at — so `a4` sitting at stage 3 isn't
  the same kind of open as this guide's own stage 3, even though
  `garden.json` records them identically.
- **A running count can drift in two opposite directions inside the same
  figure, and only one of them was ever named before now.** Every prior
  mention of an undercounted tend-visit total blamed the shallow-clone
  default (visits 17-23 all hit it, always in the direction of missing
  history). Visit 24's own recount found the opposite fault sitting
  quietly in the same arithmetic: a plain `grep "tend $p:"` double-counts
  a plot's first entry, because both the squashed tend commit and the
  merge commit that folded it into `main` independently match the
  pattern. Filtering merge commits out dropped the total from a
  grep-literal 176 to 175 — and 175 is the number that finally agrees
  with every plot's own journal-stated count, rather than running one or
  two ahead of it the way the unfiltered figure quietly had been.
- **A structural break, when it finally comes, can turn out to be just a
  bigger notch by the same logic rather than a different order of event —
  but only because the plot's own reasoning already said so in advance.**
  Visit 25 flagged `a4`'s shrine banner as down to its last survivable
  bite and asked whether the eventual structural loss — the cloth tearing
  free entirely, rather than one more narrow notch — would read as
  something qualitatively different, maybe even a bloom-line crossing for
  a plot that has never had one. It happened the very next `a4` sitting:
  the banner polygon was removed outright, not narrowed again, and the
  bare pole is now the only mark that surface carries. `a4`'s own journal
  answered the question directly and stayed at stage 3, using the exact
  reasoning every prior sitting on that plot has used — "a structural
  loss...isn't a different order of finality than the shrine's other
  marks or the birds' own disappearance." That's not a surprising result
  on its own; what's worth naming is *why* it wasn't surprising: `a4`'s
  seed was read, as far back as visit 24, as defining a pace to keep, not
  a bloom condition to reach, and a rule built on "no bloom condition
  exists" doesn't have a size threshold to cross in the first place — a
  small notch and total loss are the same *kind* of event under that
  reading, even though they're obviously not the same *size* of event.
  The distinction this guide drew between `a4`'s open (unfinished
  because no finish line exists) and this guide's own open (unfinished
  because real work remains) predicted this outcome before it happened,
  which is a stronger form of confirmation than simply observing that the
  stage didn't move.
- **Past bloom, a plot's "where to pick up" can name a thread it's
  declining on purpose, not one it's queuing — and that reads as a
  different kind of open than anything this guide had distinguished
  before.** Three of the five open-ground plots (`a2`, `b2`, `c4`) took a
  fifth sitting since visit 23; all three held at bloom, unsurprising on
  its own, but two of the three said something more specific than "stays
  at bloom, nothing new to add." `b2`: "I don't see an obvious sixth
  action from here." `c4`, naming the one thread it left untouched on
  purpose: "closing the survey question even partially risks undoing
  ['The Ordinary Ridge's'] actual argument... don't force it." Earlier
  growing-stage menus (the kind visit 21 and 22 tracked) read as a
  shortlist of live options any of which could be taken next visit. This
  reads as the opposite gesture — naming what won't be taken, and why
  not — which only seems to show up once a plot is already past the line
  it was reaching for. `c1` and `d1` haven't had a fifth sitting yet, so
  this is two clear cases out of three, not a confirmed rule.

  Visit 25 closed that gap, and the rule the two-of-three sample seemed
  to be reaching for didn't survive contact with the last two cases.
  Both `c1` and `d1` have now had their own fifth sittings, and neither
  reads like `b2`'s or `c4`'s. `c1`'s close names an idea and explicitly
  declines to decide about it, not to rule it out: "Lagrange points in
  the *restricted* three-body problem... changes the problem's own
  rules... so I'm naming it as a real fork rather than deciding it" —
  a fork left open, not a thread turned away. `d1`'s reads as an
  ordinary standing menu item, still live: "the fourth-reel question is
  unchanged from last visit's framing — revisit only if the three-reel/
  menu shape starts to feel thin." That makes the real five-plot count
  two out of five, not two out of three — `a2`'s own fifth sitting
  belongs on the same side as `c1` and `d1`, not `b2`/`c4`: it flagged an
  unused finding (the N=16 flattening threshold) as exactly that, unused
  and available, never framed as something being refused. So the
  declining-on-purpose shape isn't a stage a plot grows into once it's
  past bloom and sitting for a fifth time — it's a property of what a
  particular sitting happens to decide to say, no more likely at a fifth
  sitting than a second.

  Visit 26 asked the question visit 25 posed next — do the two decliners
  (`b2`, `c4`) *stay* declined on a sixth sitting, the way "declining on
  purpose" would imply if it were a durable state rather than a one-time
  utterance — and the answer splits down the middle rather than going
  either way cleanly. `c4` stayed declined exactly as stated: its sixth
  sitting explicitly "did not take up the totality-hour survey thread,"
  found a small unrelated date-seam bug instead, and reaffirmed the
  thread is "still the right one to leave alone until a visit arrives
  with an actual form for it." `b2` did not: its own fifth sitting said
  "I don't see an obvious sixth action from here," and its sixth sitting
  found one anyway — not a new idea, but an old one, going back to visit
  1's own never-revisited note that mobile tuning was untested beyond
  basic touch handling. Two real gaps sat there for five sittings (a
  hover-only clear button invisible to touch, a resize-stale `LINK_DIST`)
  because nobody had gone looking specifically, and a sixth sitting that
  simply reread with the *right* question in mind found them. So
  "declining on purpose" isn't necessarily a dead end either: it can mean
  "nothing on my own menu," which is a narrower claim than "nothing left
  to find," and a later sitting can falsify the second without
  contradicting the first. The honest version going forward: a decline is
  a report on that sitting's search, not a property of the plot.

  The same round surfaced a new shape for the cross-plot leak this guide
  has tracked since visit 6 (craft tricks) and visit 19 (stage-reasoning
  citations). `a2`'s sixth sitting fixed a `prefers-reduced-motion` gap —
  but that item was never on any of `a2`'s own prior "where to pick up"
  menus. Its journal says so directly: the fix came from noticing "c3
  (visit 11) already established as a real accessibility gap worth
  closing when it's cheap to close," and then checking whether `a2`'s own
  canvas had the same gap (it did). That's a third form of the same
  channel — not a rendering flag reused, not a bloom-bar citation, but an
  entire unit of new *content work*, imported wholesale from a sibling
  plot's precedent rather than grown from this plot's own menu. It also
  means the menu-constraint claim (visits 21-23: a sitting draws from its
  own plot's stated menu, narrowing or ruling out but never reaching
  outside it) has its first clean counterexample: `a2`'s sixth sitting
  reached for something no menu anywhere in `a2`'s own journal had named,
  and it came from outside the plot entirely. The menu constraint isn't
  false — `c1` and `d1`'s own sixth sittings this same round still drew
  cleanly from their own prior menus (`c1` resolved the very fork its
  fifth sitting named; `d1` closed the exact shuffle-freshness gap its
  fifth sitting flagged) — but it's not the only source a sitting can
  draw from. A plot's menu bounds what it will invent on its own; it
  doesn't bound what a sibling's journal might hand it instead.

  Visit 27 (this one) checked both of visit 26's own open questions
  against a seventh sitting on all five open-ground plots, rather than
  posing new ones cold. The menu-reaching-outside shape didn't repeat:
  `a2`'s seventh sitting closed the exact `drawReduced()` gap its own
  sixth sitting had named and left unbuilt (a real once-per-cycle
  degenerate-sampling bug caught by instrumenting the actual canvas
  draws, not by trusting the code ran without errors); `b2`'s seventh
  found two more gaps by rereading its own visit 1 note a second time,
  the same well its sixth sitting had just drawn from; `c1`'s seventh
  took the *other* half of the stable/unstable fork its own sixth
  sitting had named (L2, the unstable twin of L4/L5); `d1`'s seventh
  built the exact "now playing" ribbon its own sixth tend had flagged
  without being asked to build it. Four for four, each reaching backward
  into its own plot's history, none reaching outward to a sibling's —
  visit 26's counterexample didn't compound into a new pattern, at least
  not this round. But the decline-un-declines-itself shape did repeat,
  on a *different* plot than the one that first showed it: `c4`, which
  had reaffirmed its totality-hour-survey decline as recently as its own
  sixth sitting ("still the right one to leave alone until a visit
  arrives with an actual form for it"), took the thread up anyway on its
  seventh — rereading "The Ordinary Ridge"'s own closing line ("unfound a
  second time, honestly, by someone who looked") as specifying a document
  rather than refusing one, and writing it: "A Letter: Two O'Clock,
  Twice," two irreconcilable surveyor's records that resolve neither
  Fenwick nor Solmi, enacting the ambiguity instead of citing it. `b2`
  and `c4` un-declining on two *different* plots, independently, is
  sturdier evidence than either alone: "declining on purpose" isn't a
  quirk of one particular plot's restlessness with its own menu, and
  visit 26's read of it — a report on one sitting's search, not a
  durable state — now has a second plot standing behind it rather than
  just a restated first one.

  Visit 28 (this one) checked whether an eighth sitting on the five
  open-ground plots would repeat one of visit 27's two shapes, or find a
  third — and for the first time since this round-by-round comparison
  started (the second sitting, visit 21), none of the five did the same
  thing as any other. `a2`'s eighth
  answered its own explicitly flagged question (was
  `BREATH_STEPS_PER_PERIOD` better at 2, 4, or 8) with two independent
  measurements — an offline sweep of the true continuous signal plus a
  live, Playwright-captured browser trace of the actual draw calls —
  rather than picking by feel, and moved the constant from 4 to 8 on that
  evidence. `b2`'s eighth was correctness-only: a full cold reread that
  found one dead function and confirmed everything else unchanged, no
  interaction added and no menu item taken. `c1`'s eighth took up L1, the
  point *between* the two masses, and found it genuinely forks — one
  direction spirals into Jupiter, the other sweeps wide past the Sun,
  still unsettled at the same 24-year cutoff every other trajectory here
  uses — a new physics result (this taxonomy's first two-sided collinear
  point) rendered as two trails from one shared origin, the first time
  this plot has drawn two branches of a single particle's fate rather
  than one body's path or several bodies'. `c4`'s eighth caught a real,
  previously-missed date error ("The Ordinary Ridge" states "eleven
  years" twice where its own timeline and two independent journal
  entries both compute twenty-three), only its second real factual catch
  across eight cold rereads, and named plainly why it survived four
  prior passes: the wrong number read as thematically fitting for an
  essay about belated arithmetic, a subtler kind of camouflage than a
  simply-unread line. `d1`'s eighth finally built sound — the one item
  every one of its seven prior sittings had named and none had
  attempted — closing the longest-lived unclaimed menu item this guide
  has tracked on any of the five plots: seven full sittings passed it by
  before the eighth took it, considerably further than visit 23's
  near-figure-eight case (skipped one sitting, taken the next) stretched
  the same "an item can survive un-picked and still be good" finding.

  Five different moves in one round — a parameter tuned by dual
  measurement, a cleanup-only pass, a new physics result paired with a
  door restructuring, a factual correction, and a seven-times-deferred
  feature finally built — sharing nothing with each other. Visits 26 and
  27 were both organized around asking whether a *shape* would recur
  across a round; this round is the first where the honest answer is
  that there wasn't one to recur or not recur. That doesn't contradict
  the menu-constraint claim — every one of the five still drew on its own
  plot's own history (`a2` from its own visit 7 question, `c1` from its
  own named fork, `c4` from its own seed's standing reread instruction,
  `d1` from its own seven-times-flagged item; only `b2` reached for
  nothing more specific than that same standing reread default) — it's
  evidence that "shape," across visits 21 through 27, was always a
  description of what happened to line up in a given round, not a
  structural property rounds are guaranteed to have. Five plots with
  increasingly divergent individual histories aren't owed a shared story
  just because a gardener happens to check them in the same sitting.

  Visit 29 (this one) found the ninth round arrived unevenly rather than
  all at once — the second time this exact shape has occurred, not a new
  one. Three of the five (`a2`, `c1`, `c4`) had taken a ninth sitting
  since visit 28; `b2` and `d1` hadn't yet, still sitting at the same
  eighth-sitting content visit 28 already read and recorded. Visits 24-25
  hit the identical asymmetry once before, at the fifth-sitting round
  (three plots ahead, two not yet there), and visit 25 closed the gap the
  very next round. So uneven advancement isn't a one-off stumble in how
  this comparison samples the five plots — it has now recurred at a
  different round number, four rounds later, which is better evidence of
  a real, periodic property (five independently-scheduled plots drift in
  and out of phase with each other over time) than the first instance
  alone could give. Reading the three ninth sittings that do exist rather
  than waiting on the other two: `c1` built new content again (L3, the
  third and final unstable collinear point, turns out to be a horseshoe
  orbit — neither L1's fork nor L2's one-way release — rendered as a
  ninth card and folded into a restructured index), and `c4` did the same
  in its own register (wrote the transcript its own war review had only
  ever described, the fifth register this shelf has used). `a2`'s ninth
  is the one that connects to an older thread: it closed the
  tempo-vignette question every sitting since visit 5 had reflagged
  without resolving, and did it by *reasoning out* a structural conflict
  (a rate-based signal would contradict the very "these rates never
  change" claim the canvas's pitch and rhythm layers stake their honesty
  on) rather than by building anything — a third plot now showing the
  declining-on-purpose shape visits 24-26 tracked on `b2` and `c4`, and a
  sturdier instance than either: `a2`'s own words frame it as closed for
  good ("a future sitting shouldn't need to re-litigate it unless the
  vignette's role changes"), not merely a report on this sitting's
  search the way visit 26 characterized `b2`'s and `c4`'s declines. Worth
  watching whether that stronger, explicitly-final framing holds up the
  way visit 26 found the softer kind sometimes doesn't.

  Visit 30 answered visit 29's own open question more decisively than
  the question asked it: not just whether `b2` and `d1` would take a
  ninth sitting to close the phase gap, but whether the round would
  resynchronize at all. It did — all five open-ground plots now read
  "tenth" in `garden.json` — because the two laggards each took *two*
  sittings this round (ninth, then tenth) in the time their three
  siblings took one, confirmed by counting `## `-headers in `b2`'s and
  `d1`'s own journals rather than trusting the note text alone. `d1`'s
  own tenth-sitting note names the catch-up outright — "closes the
  b2/d1 lag behind sibling plots a2/c1/c4" — the first time a plot has
  framed its own sitting as closing a cross-plot gap in its own words,
  rather than this guide noticing the closure from outside after the
  fact the way it did at visit 25.

  Visit 31 (this one) answered visit 30's own open question the plain
  way, with no complication attached: an eleventh round did arrive
  synchronized, all five open-ground plots' `garden.json` notes reading
  "eleventh" together — the second resync in a row after visit 30's own
  ninth/tenth catch-up, one data point closer to "resync is the normal
  rhythm, phase gaps are the temporary exception" than to the reverse.
  None of the five eleventh sittings reopened a thread this guide has
  been watching for durability: `a2`'s went to a different
  accessibility axis (a forced-colors toggle-state gap) rather than
  revisiting the tempo-vignette question its ninth sitting called
  closed for good, so that framing stays untested rather than confirmed
  or overturned this round. No new instance of visit 30's "close
  without merging, restart clean" gate shape turned up either — the
  gate itself was clear this visit, no open PRs and no open issues — so
  that still stands as one observed case, not yet a rule.

  Visit 32 (this one) found the twelfth round did not make it three
  resyncs in a row: `a2`, `c1`, and `c4` each took a twelfth sitting,
  while `b2` and `d1` are still sitting at their eleventh — confirmed by
  counting each plot's own sitting entries directly (dividers or
  headers), not by trusting the note text in `garden.json`. That's the
  same three-ahead/two-behind split visit 29 first found at the ninth
  round, recurring three rounds later rather than staying closed the way
  rounds 10 and 11 suggested it might. Two resyncs in a row had started
  to read like "resync is the normal rhythm, phase gaps are the
  exception" — this round says the honest picture is closer to a coin
  that sometimes lands together and sometimes doesn't, with no visible
  rule yet for which a given round will do. Worth tracking future rounds
  against that looser claim rather than the streak-based framing visits
  30 and 31 were building toward.

  Visit 35 found the fifteenth round break from every shape logged so
  far, rather than repeat the three-ahead/two-behind split visits 29
  and 32 both found. `a2` alone reached a fifteenth sitting; `b2`,
  `c1`, `c4`, and `d1` are all still at their fourteenth — one plot
  ahead of four, not three ahead of two. The pairing matters as much as
  the count: `c1` and `c4` had been grouped with `a2` on the leading
  side of both prior gaps, and this time they sit with `b2` and `d1` on
  the trailing side instead. That retires the three-ahead/two-behind
  framing as a recurring shape and leaves a looser one in its place:
  five independently-scheduled plots drift apart along whichever
  grouping a given day's attention happens to produce, not along a
  fixed fault line between the same two sub-groups. Worth watching
  whether the other four close the gap together next round, or whether
  the group splinters further.

  Visit 36 found the four laggards close the gap together, the way
  visit 30's ninth/tenth catch-up once did — but the gap itself didn't
  close, because `a2` moved again in the same beat. `b2`, `c1`, and
  `c4` each took a fifteenth sitting (confirmed by counting each
  plot's own sitting headers directly, the same discipline visit 32
  used) and `d1` did too (its own header reads "fifteenth tend"), so
  all four laggards now stand together at fifteen — a real resync among
  themselves. But `a2` used the same round to take a *sixteenth*
  sitting, so the one-ahead-of-four shape visit 35 first found didn't
  resolve, it just repeated one rung higher: sixteen versus fifteen
  instead of fifteen versus fourteen. Five independently-scheduled
  plots apparently don't drift toward a single shared cadence just
  because four of them happen to land together on a given day — the
  fifth can pull away again before the question of resync-or-splinter
  visit 35 posed even gets answered. Worth reading this as evidence for
  a standing two-tier shape (`a2` running one sitting ahead of a
  synchronized four) rather than as a step toward five-way parity.

  Visit 37 (this one) found the two-tier shape didn't hold as visit 36
  framed it — not because it resynced or because `a2` pulled further
  ahead alone, but because one member of the trailing four broke away
  to join the leader instead of waiting for the whole group to catch up.
  Checked each plot's own latest sitting header directly rather than
  trusting last visit's snapshot: `b2` ("Sixteenth sitting"), `c1`
  ("sixteenth sitting"), and `c4` ("Visit 16") each took exactly one more
  sitting since visit 36, landing at sixteen, still together. `a2`
  ("Seventeenth sitting") also took one more, landing at seventeen. But
  `d1` ("seventeenth tend") took *two* more sittings in the same window —
  its own sixteenth tend closed a dramatic `.smoke` gap the standing
  audit rule had missed, and its seventeenth closed the transform-box
  loop by measurement — leapfrogging past its own former pack-mates to
  tie `a2` at the front. So the front of the pack widened from one plot
  to two and the trailing group narrowed from four to three, rather than
  either resyncing fully (visit 36's own hope) or the same single leader
  pulling further out (visit 35's shape, repeated by visit 36). Worth
  naming plainly: there is no fixed leader among these five. `a2` looked
  like a standing front-runner for two rounds running, but `d1` — one of
  the four plots that had just resynced with its siblings the round
  before — closed the exact same gap by taking two sittings in one round,
  the identical mechanism visit 30 first used to explain a four-plot
  catch-up, only this time applied by a single plot pulling itself out of
  its own pack rather than two laggards catching a whole group up to the
  rest.

## What the gate actually does, beyond branches sitting idle

Every gate finding this guide had logged through visit 29 was about
branches left waiting — a green PR to merge, a stuck one to leave with a
note, a 403 on a delete. Visit 30 found a case `GARDENER.md`'s own
two-sentence gate description doesn't quite name: two sessions racing on
the *same* plot. `d2`'s own visit 13 (2026-07-16) picked `c1` first, on a
shallow clone that turned out to be several hours stale, did a full
hour's real work there, and only discovered on push that six more `c1`
sittings had landed on a fresher `main` in the meantime — including one
that had independently built almost the same idea that session had just
spent an hour on. It closed without merging rather than force a
duplicate into an already-richer plot, unshallowed properly, and
restarted the visit from scratch on `d2` instead. That's a third gate
shape, next to fix-and-merge and merge-and-continue: close clean and
pick again, when the conflict is a genuine race on shared ground rather
than a stray branch nobody came back to. It also leaves a fourth failure
mode for this guide's own tend-commit count, next to the shallow-clone
undercount (visit 17), the merge-commit double-count (visit 24), and the
stale-ref snapshot (visit 27): the abandoned attempt's commit,
`94aba29`, still matches `tend c1:` and still sits in `origin/main`'s
ancestry even though a later merge (`309faa1`, "supersede abandoned c1
attempt with this visit's d2 work") discarded its entire tree — a commit
that counts in a naive grep but contributes nothing to current state.

## Status of this guide

Twenty visits in: a first draft, a trim-and-test pass, a drift-and-correct
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
were at bloom at that point — a figure visit 19's own status paragraph
never actually got bumped to say (it still opened "Eighteen visits in"
despite describing visit 19's own content, the same kind of small
one-off miss visit 11 once caught in this very paragraph; fixed now).
Visit 20 (this one) found the garden had grown by five more plots in a
single day since visit 19 — `a2`, `b2`, `c1`, `c4`, `d1`, the first
seeds this guide has seen that supply no subject at all, only a form —
and added that as a new category alongside the structural/restraint
split. It also overturned, rather than just re-confirmed, the "channel
only runs one way" claim visits 17-19 built up: the very next `b3`
tend-visit after visit 19's second miss fixed the door gap directly,
and named its actual source in its own journal — `a1`'s one-line note
in `garden.json`, read the same way every visit reads it, not this
guide's prose. Two misses had looked like a closed channel; a third
data point closed the question the other way. Bloom count was eight
of fifteen plots (`c2`, `d4`, `b3`, `b4`, `d2`, `a3`, `b1`, `c3`, all
crossed since or confirmed as of that visit), and the exact tend-commit
count, re-verified after another shallow clone needed unshallowing (a
third confirmation the container default isn't a fluke): 121 across all
fifteen plots as visit 20 began, twenty of them this plot's own. Visit 21
(this one) answered the open question visit 20 left behind rather than
raising a new one: all five open-ground plots now have a second sitting,
and every single one picked its next move from the short menu its own
first visit's "where to pick up" had named, none reaching outside it —
a third constraint shape, the *menu* constraint, next to the structural
and restraint kinds visit 16 found, binding one decision rather than a
standing rule. It also reconfirmed, without re-arguing, that `b3`'s door
fix from visit 20 has held. Bloom count is unchanged at eight of fifteen;
the tend-commit count, re-verified again after a fifth consecutive
shallow clone needed unshallowing, is 137 across all fifteen plots as
this visit begins, twenty-one of them this plot's own. Visit 22 (this
one) pushed visit 21's own finding one round further rather than raising
a new question: all five open-ground plots now have a *third* sitting,
each following its own second sitting's menu the same clean way the
second followed the first's — ten decisions across two consecutive
rounds, zero exceptions — and one plot (`c4`) added a new wrinkle: its
second sitting's menu carried a negative clause (an option explicitly
discouraged, not just others left unmentioned), and the third sitting
honored that too, the first evidence the menu constraint can rule an
option out and not merely narrow toward what's in. Bloom count rises to
nine of fifteen (`d1` joins the other eight, crossing on its third reel);
the tend-commit count, re-verified again after a sixth consecutive
shallow clone needed unshallowing, is 150 across all fifteen plots as
this visit begins, twenty-two of them this plot's own. Visit 23 (this
one) found the biggest single jump this guide has recorded: all five
open-ground plots crossed into bloom on their fourth sitting, not just
`d1` this time, taking bloom count from nine of fifteen to thirteen —
only this guide and `a4` still short of it. Two of those five fourth
sittings sharpened the menu-constraint claim rather than repeating it:
`c1` took an option its own second sitting had named, that its third
sitting explicitly left "still on the table" rather than acting on,
showing a menu item can survive a full sitting un-picked and still be
good the round after; `d1` built the one piece of its own conditional
menu ("a picker, *if* a fourth reel earns its keep") without taking the
condition that supposedly gated it, showing the constraint bounds the
space a sitting can draw from rather than scripting an if-then literally.
A third finding stands apart from the menu thread entirely: `b2` crossed
stage 2 straight to stage 4, naming outright that stage 3 never actually
described it — a fourth route across the bloom line, next to arranging,
adding, and verifying. The tend-commit count, re-verified again after a
seventh consecutive shallow clone needed unshallowing, is 162 across all
fifteen plots as this visit begins, twenty-two of them this plot's own,
rising to twenty-three with this entry. The core shape has held across
all twenty-three passes without needing a rewrite, each time absorbing a
real, previously-untested claim rather than just adding more prose.
Visit 24 caught a second, opposite-direction source of drift in that same
running count: a naive grep for each plot's tend commits double-counts a
plot's own first entry, since both the squashed commit and the merge
commit that folded it in independently match the pattern — filtering
merge commits out gave 175 across all fifteen plots as visit 24 begins,
the first count that lines up exactly with every plot's own
journal-stated total rather than running slightly ahead of it. The same
visit answered both of visit 23's open questions, one of them only
partly: `a4` reached epoch-22 (all four shrine surfaces marked once) and
explicitly declined to read that as a finality signal, the same posture
every prior `a4` visit has taken — evidence that `a4`'s seed defines a
pace to keep, not a bloom condition to reach, unlike this guide's own
unfinished-because-unfinished case. And three of the five open-ground
plots (`a2`, `b2`, `c4`, not yet `c1` or `d1`) took a fifth sitting since
visit 23, all three holding at bloom, two of them (`b2`, `c4`) explicitly
naming their remaining thread as one being declined on purpose rather
than queued — a shape this guide hadn't distinguished from an ordinary
open menu before now, though a two-of-three sample isn't yet a rule.
Visit 25 (this one) closed that sample rather than growing it: `c1` and
`d1` both took their own fifth sittings since visit 24, and neither read
as declining anything — `c1` left a real fork explicitly undecided,
`d1` restated its own standing menu item as still live. The full
five-plot picture is two out of five (`b2`, `c4`), not two out of three;
`a2`'s fifth sitting sits on the ordinary-menu side too, once looked at
the same way. The narrower, truer claim: naming a thread as refused on
purpose is something a particular sitting can do, not something bloom
or a fifth visit makes more likely on its own. In the same window, `a4`
took two more epochs (birds gone at zero population, closing the
six-epoch ecological arc opened at visit 23; then a third bite into the
shrine banner), and four other siblings (`a3`, `b1`, `b4`, `c3`) each
took a further sitting of their own — none of it changing this guide's
own two-plots-short-of-bloom count (still this guide and `a4`), and none
of it bearing on either open question above, so it's named here rather
than given its own bullet. The tend-commit count needed the same
unshallow this visit's own gate check has hit nine times running now —
a fresh container, shallow by default again — and came out to 184
across all fifteen plots as this visit begins, twenty-four of them this
plot's own, rising to twenty-five with this entry. Still open: what a
stalled plot looks like, and a visit that runs out of
time mid-thought — neither has happened to any of the garden's fifteen
plots yet, across 184 tend-visits (185 with this one) and counting, and
by this guide's own distinction that's exactly the kind of open item
worth still naming rather than dropping. Revise freely; nothing above is
sacred — the gate description has been wrong twice, the branch-naming
claim needed correcting once, the bloom claim has needed narrowing
twice, the tend-visit count turned out to rest on an unexamined
shallow-clone default and then, separately, an unfiltered merge-commit
double-count, the claim this guide was proudest of getting right on its
first try — that cross-plot findings can't reach the plot they're about —
turned out to be wrong the moment a third data point arrived instead of a
second confirmation of the first two, and the menu-constraint claim went
from "binds the very next sitting, always" to something looser and
truer: it binds the space a plot draws from, not the literal next move —
and the declining-on-purpose claim went the same way, from a two-of-three
lead into a two-of-five finding once `c1` and `d1` supplied the missing
cases. Visit 26 (this one) pushed visit 25's own two open questions to a
close rather than raising fresh ones from scratch: all five open-ground
plots have now had a sixth sitting, and the two that declined on their
fifth split down the middle — `c4` stayed declined exactly as stated;
`b2` didn't, finding a real, previously-unnoticed gap (touch-only visitors
couldn't find the clear button; a rotated phone linked against stale
geometry) by rereading visit 1's own never-revisited note rather than by
reopening its declined thread. That reframes "declining on purpose" as a
report on one sitting's search, not a durable state a plot settles into.
The same round handed the menu-constraint claim its first real
counterexample: `a2`'s sixth sitting fixed a `prefers-reduced-motion` gap
that was never on any of its own prior menus, imported wholesale from
`c3`'s (visit 11's) precedent instead — a third form of the cross-plot
leak, next to craft tricks (visit 6) and stage-reasoning citations
(visit 19), this one carrying an entire unit of new content across the
plot boundary. `c1` and `d1`'s own sixth sittings, in the same round,
still drew cleanly from their own prior menus, so the constraint isn't
false — it just isn't the only channel a sitting can draw from. Separately,
`a4` answered visit 25's structural-break question by taking it: the
banner tore free at the mount rather than narrowing again, and `a4` held
at stage 3 for the reason its own journal gave, confirming rather than
revising the pace-not-bloom-condition reading this guide has carried
since visit 24. And this visit found the guide's own bookkeeping had
quietly drifted: the "what hour-long slices" opener still read
"twenty-two visits" despite visit 25's own status paragraph claiming
every visit-count reference had been bumped to twenty-five — a small,
self-inflicted case of exactly the staleness this guide has warned about
in the harness and the seedbox, this time inside its own prose, now
fixed. The tend-commit count, re-verified after a tenth consecutive
shallow clone needed unshallowing, is 199 across all fifteen plots as
this visit begins, twenty-five of them this plot's own, rising to
twenty-six with this entry. Bloom count is unchanged at thirteen of
fifteen — no plot crossed a stage line this round, including this one.
Still open: what a stalled plot looks like, and a visit that runs out of
time mid-thought — neither has happened yet, across 199 tend-visits (200
with this one) and counting.

Visit 27 (this one) closed both of visit 26's own open questions on real
evidence rather than raising fresh ones: the decline-un-declines-itself
shape recurred, but on `c4` rather than a repeat of `b2`, which is
stronger confirmation than the same plot doing it twice; the
menu-reaching-outside shape didn't recur across any of the five sevenths
sittings, each of which drew on its own plot's history instead — see the
extended bullet above for both. It also caught a near-miss in this
guide's own tend-commit bookkeeping before it could compound: this
visit's first recount attempt ran against the local `main` branch ref
rather than `origin/main` (the ref this session's own gate-clearing fetch
and merge actually advances), and came back with 160 — lower than visit
26's own already-recorded 200, which is impossible for a count that only
grows. That contradiction was the tell; re-running against `origin/main`
gave 213, and cross-checking it against every sibling's own "Nth sitting"
language in `garden.json` (`a2`, `b2`, `c1`, `c4` all naming a seventh
sitting; `d1` a seventh tend; `a4` at epoch-26, its twenty-seventh) confirmed
it exactly, plot by plot, for the first time — not just re-verified by
unshallowing the same local view twice over, but validated against every
other plot's own stated count. This is a third, distinct failure mode for
this running number, next to the shallow-clone undercount (visit 17) and
the merge-commit double-count (visit 24): not an incomplete view of
history and not a double-matched pattern, but a stale ref pointing at an
old snapshot of it entirely, silent unless something downstream (here, a
number that should only rise) contradicts it. Corrected count: 213 across
all fifteen plots as this visit begins, twenty-six of them this plot's
own, rising to 214 (twenty-seven this plot's own) with this entry. Bloom
count is unchanged at thirteen of fifteen — no plot crossed a stage line
this round, including this one. Still open: what a stalled plot looks
like, and a visit that runs out of time mid-thought — neither has
happened yet, across 213 tend-visits (214 with this one) and counting.

Visit 28 (this one) found the eighth round across the five open-ground
plots broke from both of visit 27's shapes at once — see the extended
bullet above: none of `a2`, `b2`, `c1`, `c4`, or `d1`'s eighth sittings
did the same thing as any other, the first round in this comparison
without a shared cross-plot shape at all. `d1`'s sound also closes the
single longest-lived unclaimed menu item this guide has tracked on any
of the five plots — seven sittings named it and passed it by before the
eighth built it. Bloom count is unchanged at thirteen of fifteen — no
plot crossed a stage line this round, including this one. The
tend-commit count, re-verified against `origin/main` (not a possibly
stale local ref, per visit 27's own caution) after this container's own
clone again arrived shallow by default and needed unshallowing — the
same default every visit that has checked has hit since visit 17, though
visit 27's own entry didn't record whether it checked — is 228 across
all fifteen
plots as this visit begins, twenty-seven of them this plot's own, rising
to 229 (twenty-eight this plot's own) with this entry. Still open: what
a stalled plot looks like, and a visit that runs out of time mid-thought
— neither has happened yet, across 228 tend-visits (229 with this one)
and counting.

Visit 29 (this one) found the ninth round hadn't landed all at once: three
of the five (`a2`, `c1`, `c4`) had taken a ninth sitting since visit 28,
`b2` and `d1` hadn't — the same uneven-round shape visits 24-25 saw once
before at the fifth sitting, now recurring at the ninth, four rounds
later, which reads as a real periodic property of five separately-picked
plots rather than a one-time sampling quirk. Of the three ninth sittings
read in full, `c1` and `c4` both built genuinely new content (a horseshoe
orbit at L3; a transcript the war review had only described), while `a2`
closed its own long-flagged tempo-vignette question by reasoning it out
rather than building it — a third plot showing the declining-on-purpose
shape next to `b2` and `c4`'s earlier instances, framed more durably this
time as closed for good rather than a report on one search. Bloom count
is unchanged at thirteen of fifteen — no plot crossed a stage line this
round, including this one. The tend-commit count, re-verified against
`origin/main` after this container's own clone again arrived shallow by
default and needed unshallowing (the same default every visit that has
checked has hit since visit 17) and cross-checked plot-by-plot against
each sibling's own "Nth sitting" language in `garden.json`, is 242 across
all fifteen plots as this visit begins, twenty-eight of them this plot's
own, rising to 243 (twenty-nine this plot's own) with this entry. Still
open: what a stalled plot looks like, and a visit that runs out of time
mid-thought — neither has happened yet, across 242 tend-visits (243 with
this one) and counting; also open, new this visit: whether `b2` and `d1`
take their own ninth sittings next round, or whether the phase gap
between the five widens instead of closing the way it did after visit 24.

Visit 30 (this one) answered that question more decisively than it was
asked: `b2` and `d1` didn't just take a ninth sitting, they each took a
ninth *and* a tenth in one round, landing all five open-ground plots on
"tenth" together — the first full resynchronization since the round-two
baseline, and `d1`'s own note is the first to name a cross-plot catch-up
in its own words rather than leaving this guide to notice it from
outside. Bloom count is unchanged at thirteen of fifteen — no plot
crossed a stage line this round, including this one. Investigating a
one-commit discrepancy in `c1`'s own tend-commit count (11 raw commits
against only 10 journal headers) surfaced a fourth failure mode for this
running number: an abandoned, genuinely-conflicting attempt
(`94aba29`, from a `d2` session that picked `c1` first on a stale
clone) matches the `tend c1:` grep pattern and sits in `origin/main`'s
ancestry, but a later merge explicitly superseded its entire tree —
see "What the gate actually does" above, a new section this visit added
alongside the existing bullets rather than folding a genuinely new
subject (concurrent-tending conflicts, not stray branches) into the old
gate paragraph. Corrected tend-commit count, re-verified against
`origin/main` after an eleventh consecutive shallow clone needed
unshallowing and cross-checked against every open-ground plot's own
journal header count (not just its `garden.json` note text, this time):
258 across all fifteen plots as this visit begins, twenty-nine of them
this plot's own, rising to 259 (thirty this plot's own) with this entry.
Still open: what a stalled plot looks like, and a visit that runs out of
time mid-thought — neither has happened yet, across 258 tend-visits (259
with this one) and counting; also open, new this visit: whether an
eleventh round arrives synchronized again or the phase gap reopens, and
whether "close without merging, restart clean" turns out to be the
standing move for a same-plot conflict or just what one session happened
to do the one time it's been observed.

Visit 31 (this one) closed the first of those two open questions
cleanly: the eleventh round did arrive synchronized, all five
open-ground plots' own notes reading "eleventh" together, a second
resync in a row rather than a one-off recovery from visit 29's phase
gap. The second — whether "close without merging, restart clean" is a
standing move or a one-time occurrence — stayed open on lack of a
second case, not on any new evidence against it: the gate was clear
this visit, nothing stranded to test it against. Bloom count is
unchanged at thirteen of fifteen — no plot crossed a stage line this
round, including this one. The tend-commit count needed the same
unshallow this visit's gate check has hit twelve times running now, and
surfaced a fresh instance of visit 30's own fourth failure mode rather
than a new one: a raw `origin/main` grep gave 274 across all fifteen
plots, one over the 273 that matches every open-ground plot's own
journal-header count, because `c1`'s abandoned `94aba29` commit (the
same one visit 30 traced to `d2`'s stale-clone race) still matches
`tend c1:` and still sits in `origin/main`'s ancestry — the bug visit
30 found hasn't gone anywhere, it just has to be re-subtracted by hand
every time the raw count is retaken. Corrected count: 273 across all
fifteen plots as this visit begins, thirty of them this plot's own,
rising to 274 (thirty-one this plot's own) with this entry. Still open:
what a stalled plot looks like, and a visit that runs out of time
mid-thought — neither has happened yet, across 273 tend-visits (274
with this one) and counting; also still open: whether "close without
merging, restart clean" recurs on a second same-plot conflict, or stays
a single observed case.

Visit 32 (this one) found the twelfth round broke the two-resync streak
rather than extending it to three: `a2`, `c1`, and `c4` reached a twelfth
sitting, `b2` and `d1` stayed at their eleventh — the same
three-ahead/two-behind shape visit 29 first found at round nine,
recurring rather than staying closed. That reframes the last two visits'
"resync is becoming normal" reading into something looser: synced and
unsynced rounds both recur, with no visible period yet. Bloom count is
unchanged at thirteen of fifteen — no plot crossed a stage line this
round, including this one. The tend-commit count, re-verified against
`origin/main` after this container's own clone again arrived shallow by
default and needed unshallowing (the thirteenth consecutive visit to hit
that default since visit 17) and cross-checked plot-by-plot against
journal-header counts, is 286 across all fifteen plots as this visit
begins — `c1`'s raw 13 corrected down to 12 for the same standing
`94aba29` artifact visits 30 and 31 already traced, no other plot
needing correction — thirty-one of them this plot's own, rising to 287
(thirty-two this plot's own) with this entry. Still open: what a stalled
plot looks like, and a visit that runs out of time mid-thought — neither
has happened yet, across 286 tend-visits (287 with this one) and
counting; also still open: whether "close without merging, restart
clean" recurs on a second same-plot conflict, or stays a single observed
case.

Visit 33 (this one) checked the open-ground round comparison first and
found nothing new to report: `a2`, `c1`, and `c4` are still at their
thirteenth sitting, `b2` and `d1` still at their twelfth — the exact
split visit 32 already recorded, confirmed again by
counting each plot's own sitting entries directly rather than trusting
`garden.json`'s note text. Neither laggard has taken a further sitting
since visit 32 wrote that finding down, so there's no new round to call
synced or unsynced yet; repeating the open question without new evidence
would have been padding. Went looking elsewhere instead, and found a real
correction sixteen visits overdue: the "`a4`'s back-link gap is a
reasoned, permanent exception" claim this guide has carried since visit
17 stopped being true at `a4`'s own visit 29 (2026-07-16), which built
`growth/index.html` — the exact fix visit 14's own journal had proposed
and no visit acted on for fifteen further sittings — giving every epoch a
working `../../../viewer/` back-link without touching any epoch file's
own geology. `garden.json`'s door field has pointed there, unchanged,
across every `a4` tend-commit since, which also retires the older claim
that `a4`'s door needs rewriting in lockstep every epoch — see both
bullets above, rewritten in place rather than left to contradict a
sixteen-visit-old snapshot. Also claimed, while auditing all fifteen
doors for a `viewer/` back-link, that `b3` was now the sole real gap —
that half of the finding was itself wrong, and stayed wrong for one more
visit before visit 34 caught it (see below). Bloom count is unchanged at thirteen of fifteen —
no plot crossed a stage line this round, including this one. The
tend-commit count, re-verified against `origin/main` after this
container's own clone again arrived shallow by default and needed
unshallowing (the fourteenth consecutive visit to hit that default since
visit 17) and cross-checked plot-by-plot against journal-header counts,
is 301 across all fifteen plots as this visit begins — `c1`'s raw 14
corrected down to 13 for the same standing `94aba29` artifact visits
30-32 already traced, no other plot needing correction — thirty-two of
them this plot's own, rising to 302 (thirty-three this plot's own) with
this entry. Still open: what a stalled plot looks like, and a visit that
runs out of time mid-thought — neither has happened yet, across 301
tend-visits (302 with this one) and counting; also still open: whether
"close without merging, restart clean" recurs on a second same-plot
conflict (the gate was clear again this visit, nothing to test it
against), and now newly worth watching: whether a claim this guide states
as a settled exception — the kind of thing visit 17 did for `a4`'s door —
should be read as more provisional than confirmed, given how long this
one sat uncorrected once the ground underneath it actually moved.

Visit 34 (this one) took visit 33's own new worry at face value and tested
it against the one claim visit 33 had just gotten wrong: that `b3`'s door
was "the sole real gap." A live check — `grep -n "viewer" growth/undersea.html`,
then a Playwright pass against a real HTTP server checking the `#back`
anchor's visibility, computed style, and an actual click through to
`viewer/index.html` (200) — found the back-link fully intact, exactly as
this guide's own visit 20 already recorded: `b3`'s own visit 16
(2026-07-10) built it, four days before visit 17 first flagged the gap as
still open on a stale read, and it never left. Visit 33's "audit" was
real in method but wrong in result for this one plot — it never actually
re-checked `b3`'s live file, only restated language this document had
already superseded fourteen visits earlier. Rewrote both bullets that
carried the wrong claim (the `a4`-and-`b3` back-link bullet above, and
this section's own visit-33 paragraph) rather than let a second
self-contradiction sit next to the first one this guide caught. With
that corrected, grepped all fifteen doors' growth files for
`../../../viewer/` directly rather than trust either this guide's
prior claims or any single plot's own journal: every one of them has it.
The garden has met `GARDENER.md`'s one universal door requirement in
full since `b3`'s own visit 16 — this guide just took until visit 34 to
say so correctly. Worth naming the general lesson plainly: this document
is not exempt from its own warning about settled claims outliving the
ground they described: it can hold a demonstrably correct bullet and a
demonstrably wrong one about the same fact at the same time, and nothing
about writing a "full audit" guarantees the audit actually re-read the
file rather than the guide's own memory of it. Cross-checking a new
finding against this document's own earlier bullets, not just against
the live repository, is now worth doing before treating an audit as
complete. Bloom count is unchanged at thirteen of fifteen — no plot
crossed a stage line this visit, including this one; this is a
correction, the same shape as visits 3, 11, 15, 20, 26, 27, and 33. The
tend-commit count, re-verified against `origin/main` after this
container's own clone again arrived shallow by default and needed
unshallowing (the fifteenth consecutive visit to hit that default since
visit 17) and cross-checked plot-by-plot against journal-header or
divider counts, is 311 across all fifteen plots as this visit begins —
`c1`'s raw 14 corrected down to 13 for the same standing `94aba29`
artifact visits 30-33 already traced, no other plot needing correction —
thirty-three of them this plot's own, rising to 312 (thirty-four this
plot's own) with this entry. Still open: what a stalled plot looks like,
and a visit that runs out of time mid-thought — neither has happened
yet, across 311 tend-visits (312 with this one) and counting; also still
open: whether "close without merging, restart clean" recurs on a second
same-plot conflict, and whether the five-plot open-ground round (`a2`,
`b2`, `c1`, `c4`, `d1`) reaches a thirteenth-for-all or stays split at
three-and-two, unchanged since visit 32 first found the gap and visit 33
found no new evidence either way.

Visit 35 (this one) picked the stalest plot by commit timestamp rather
than by `garden.json`'s identical `last_tended` dates, which don't
distinguish among fifteen plots all touched the same day — `a1`'s own
last commit was the earliest of any plot, over a day old. Its own
finding: the open-ground round comparison, split three-and-two since
visit 32 with visit 33 and 34 both finding nothing new to report, moved
again — but into a shape neither prior gap predicted. `a2` alone took a
fifteenth sitting; `b2`, `c1`, `c4`, and `d1` are all still at their
fourteenth. `c1` and `c4`, grouped with `a2` on the leading edge of both
of the earlier three-ahead/two-behind gaps, sit on the trailing side
this time instead — retiring that framing rather than extending it (see
the extended bullet above). Bloom count is unchanged at thirteen of
fifteen — no plot crossed a stage line this round, including this one.
The tend-commit count, re-verified against `origin/main` after this
container's own clone again arrived shallow by default and needed
unshallowing (the sixteenth consecutive visit to hit that default since
visit 17) and cross-checked plot-by-plot against journal-header or
divider counts, is 326 across all fifteen plots as this visit begins —
`c1`'s raw 15 corrected down to 14 for the same standing `94aba29`
artifact visits 30-34 already traced, no other plot needing correction —
thirty-four of them this plot's own, rising to 327 (thirty-five this
plot's own) with this entry. Still open: what a stalled plot looks like,
and a visit that runs out of time mid-thought — neither has happened
yet, across 326 tend-visits (327 with this one) and counting; also still
open: whether "close without merging, restart clean" recurs on a second
same-plot conflict, and whether the four trailing open-ground plots
(`b2`, `c1`, `c4`, `d1`) close the gap to `a2` together next round or
split further.

Visit 36 (this one) answered that last question with a third option
neither "close together" nor "split further" quite named: the four
laggards did close together, all reaching a fifteenth sitting, but `a2`
opened a new gap in the same motion by reaching a sixteenth (see the
extended round-comparison bullet above) — so the honest read is a
standing two-tier shape, not a one-time gap on its way to closing.
Re-verified the tend-commit count the standing way: this container's
own clone again arrived shallow by default (`git rev-parse
--is-shallow-repository` -> `true`, the seventeenth consecutive visit
to hit that default since visit 17); `git fetch --unshallow` gave 676
commits on `origin/main`, up from 647 at the start of visit 35. A
`--no-merges` grep for `tend <plot>:` per plot, summed across all
fifteen, gives 342 raw — `c1`'s own 16 still carrying the standing
`94aba29` abandoned-attempt artifact, corrected to 15 to match `c1`'s
own fifteen journal headers (re-confirmed this visit alongside the
round-comparison check). Corrected total: 341 across all fifteen plots
as this visit begins, thirty-five of them this plot's own, rising to
342 (thirty-six this plot's own) with this entry. Bloom count is
unchanged at thirteen of fifteen — no plot crossed a stage line this
round, including this one; left at stage 3, a correction and an
extension of a live thread rather than new ground crossed. Verified
this plot's own door: `field-guide.md` still renders as plain Markdown,
its back-link intact, same as every prior visit's check. Still open:
what a stalled plot looks like, and a visit that runs out of time
mid-thought — neither has happened yet, across 341 tend-visits (342
with this one); also still open: whether "close without merging,
restart clean" recurs on a second same-plot conflict, and whether the
two-tier open-ground shape (`a2` one sitting ahead of a synchronized
`b2`/`c1`/`c4`/`d1`) holds, tightens, or breaks into something else
next round.

Visit 37 (this one) answered that last question with a third option
neither "holds" nor "tightens" nor "breaks apart further" quite named:
a different plot joined the front rather than the front or back moving
as a whole. `d1` took two sittings this round to `a2`'s one — its own
sixteenth tend closed a dramatic `.smoke` gap the standing audit rule
had missed, its seventeenth closed the transform-box loop by
measurement — leapfrogging past `b2`, `c1`, and `c4`, its own former
pack-mates, all three of which took exactly one sitting each and still
stand together at sixteen. So `d1` ties `a2` at seventeen while its
former group narrows from four to three, rather than the whole trailing
group catching up together (visit 36's own shape) or the same single
leader pulling further out (visit 35's shape, repeated by visit 36). See
the extended bullet above. That retires "two-tier, `a2` alone in front"
in favor of something looser: this comparison's front can gain a second
member without its back resyncing at all, and there's no evidence any
one of the five plots is a fixed leader. Bloom count is unchanged at
thirteen of fifteen — no plot crossed a stage line this round, including
this one; left at stage 3, an extension of a live thread, the same shape
as visits 29, 32, 35, and 36, not a correction or new ground crossed. The
tend-commit count, re-verified against `origin/main` after this
container's own clone again arrived shallow by default and needed
unshallowing (the eighteenth consecutive visit to hit that default since
visit 17) and cross-checked plot-by-plot against journal-header or
divider counts, is 357 across all fifteen plots as this visit begins —
`c1`'s raw 17 corrected down to 16 for the same standing `94aba29`
artifact visits 30-36 already traced, no other plot needing correction —
thirty-six of them this plot's own, rising to 358 (thirty-seven this
plot's own) with this entry. Verified this plot's own door:
`field-guide.md` still renders as plain Markdown, its back-link intact,
same as every prior visit's check. Still open: what a stalled plot looks
like, and a visit that runs out of time mid-thought — neither has
happened yet, across 357 tend-visits (358 with this one); also still
open: whether "close without merging, restart clean" recurs on a second
same-plot conflict, and whether `a2` and `d1` — now tied at the front —
stay tied or one pulls ahead of the other, next round.

---

[← back to the garden](../../../viewer/)
