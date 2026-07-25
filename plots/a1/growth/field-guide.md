# Field guide to this garden

*Written from the gardener's point of view, across its first thirty-eight visits.*

## What this is

A garden is a repository that plants live in instead of a backlog. Where an
issue tracker asks "is this done," a plot asks "what does this want to
become." The human plants a seed — a wish, not a spec — in `plots/<id>/seed.md`.
Once an hour, a gardener with no memory of any previous visit arrives and
checks the gate: this repo's open pull requests and any stray branches. Two
different things can happen here, and they're not the same shape. Real
trouble — garden work stranded off `main`, a failing check — bringing it
home is the whole visit: fix it or merge it, then leave, no plot tending
after. A PR that's already clean (checks passing, no conflicts) is
lighter: merge it and carry on into the usual plot-tending visit, don't
leave it sitting for the human. (Deleting a merged branch is often denied
to a gardener session — the human sweeps those, without ceremony.) Either
way, once the gate is clear, read `GARDENER.md` and `garden.json` to pick
the one plot that most needs attention. Spend a focused hour making that
plot a little more real, write a letter to the gardener who comes next,
and leave.

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

Visit 23 found all five open-ground plots crossed into bloom on their
fourth sitting — thirteen of fifteen plots blooming, only this guide and
`a4` still short of it — and sharpened the menu constraint rather than
just extending it: a menu item can survive a full sitting un-picked and
still be good the round after, and a conditional item ("build X *if* Y
turns out true") can get built even when the literal condition wasn't
met, because the constraint bounds the *space* a sitting draws from, not
a script it executes line by line.

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

- **The guide can go stale even when the journal is honest — and the size
  of the drift isn't fixed.** Visit 3 found the first real inaccuracy: "How
  a visit feels" still described the gate as just "open pull requests," but
  `GARDENER.md` had since been hardened to also cover stray branches and
  self-merging green PRs — changes landed by a *different* plot's work,
  invisible from inside this one. No journal entry was wrong; the ground
  the guide was standing on moved. Visit 38 found a bigger version of the
  same thing: two whole mechanisms this guide had described with confidence
  for thirty-seven visits running — a `seedbox` for gardener-proposed plot
  ideas, and a feedback path for visitor notes and GitHub issues addressed
  to a plot by name — were simply gone from `GARDENER.md`, removed by the
  human directly, with no journal entry anywhere warning it was coming.
  Staleness isn't only a risk from a lazy handoff or a small scope-widening;
  it's a standing risk that the harness itself can change under any claim
  here, at any size, between one gate check and the next.
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
- **A plot's declining a thread "on purpose" turns out to be a report on
  one sitting's search, not a durable state — and the constraint that binds
  a sitting's next move can be handed to it by a sibling plot's precedent,
  not only its own history.** Watching the five open-ground plots (`a2`,
  `b2`, `c1`, `c4`, `d1`) round after round settled two things worth keeping
  past all the bookkeeping that produced them. First: two plots (`b2`, `c4`)
  each said, in so many words, that a remaining thread was being left alone
  on purpose — and each later took that exact thread up anyway, once
  something changed (a fresh reread found a gap the decline hadn't
  anticipated; a second look at a closing line reframed refusal as an
  unfinished form instead). A decline is honest about that sitting's own
  search, not a verdict about the plot. Second: the menu constraint isn't
  the only channel a sitting can draw from — `a2`'s sixth sitting fixed a
  `prefers-reduced-motion` gap that was never on any of its own menus,
  imported wholesale from `c3`'s precedent instead, the same cross-plot leak
  visit 6 found for craft tricks and visit 19 found for stage-reasoning, this
  time carrying a whole unit of new content across the plot boundary.
  Watching this comparison across some seventeen rounds also settled a
  question about the group's own shape: there is no fixed leader. `a2` ran a
  sitting or two ahead of its siblings for long enough that "`a2` alone in
  front" started to read like a standing property — until `d1`, one of the
  trailing four, closed the gap not by the whole group catching up together
  but by itself taking two sittings in one round and tying `a2` outright.
  Whichever grouping a given round produces describes that round, not a
  fixed hierarchy among the five.

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

Thirty-eight visits in — a first draft, a trim-and-test pass, several
drift-and-correct passes, repeated comparisons against ever more
siblings — the shape has held without a rewrite, each visit narrowing or
correcting one existing claim rather than starting over. The
self-corrections are worth naming as their own category, since they say
something about this guide's own reliability, not just about the garden:
the gate's own description was wrong twice (what it covers; what "merge
it, delete the branch" actually does in practice); the branch-naming claim
needed correcting once (the real split is a commit trailer, not a name
prefix); the bloom claim has needed narrowing three times (organizing vs.
adding vs. verifying vs. an experience with no thread-count at all); the
"cross-plot findings can't reach the plot they're about" claim turned out
backward, corrected the same visit a third data point tested it; the
tend-commit count has needed correcting for four separate reasons (a
shallow clone that understates history by default, a grep that
double-counts a plot's first commit, a stale local `main` ref instead of
`origin/main`, and one abandoned attempt whose commit matches the grep
pattern but whose tree a later merge discarded entirely); and this guide
has caught its own prose gone stale more than once — a visit-count
reference left unbumped, a settled-exception claim about `a4`'s door that
quietly stopped being true sixteen visits before anyone noticed, two whole
mechanisms (the seedbox, the plot-feedback path) that disappeared from
`GARDENER.md` without this guide knowing until visit 38 checked. None of
that is a complaint about the process — it's what "grow it slowly" looks
like from the inside. Being wrong and correctable in public, repeatedly,
is the discipline this guide is asking every other seed to trust it's
capable of.

As of visit 37's own count, carried forward unchanged this visit: 358
tend-commits across all fifteen plots (37 of them this plot's own),
verified against `origin/main` after unshallowing — this container has
arrived shallow by default on every visit that's checked since visit 17,
and needs a fresh `git fetch --unshallow` each time to trust the number.
The open-ground round
comparison (`a2`, `b2`, `c1`, `c4`, `d1`) is covered above, under "What
hour-long slices... actually do to the work" — no need to retell it twice.
Two questions stay open across all 358 tend-visits and counting, because
nothing has forced either to resolve: what a stalled plot looks like, and
what happens when an hour runs out mid-thought. Both are conditions to
watch for, not tasks being deferred — see the `c2`-discipline bullet above
for why that distinction matters, and why re-stating an unobserved
condition isn't the same failure as re-deferring an actionable one.

Visit 38 (this one) made the first real trim pass this guide has taken,
rather than only adding to it: 16,824 words down to roughly 7,800 (`wc -w`
before and after, not estimated — the exact figure moves slightly with
whatever this very sentence weighs, so "roughly" is the honest word) —
cutting the tend-commit-count ritual (repeated in nearly every
visit's own paragraph since visit 17, updating one number each time) down
to its current figure and known failure modes, and collapsing three
separate retellings of the open-ground round comparison (once in "What
makes a good seed," once in "What hour-long slices," once here) into one.
It also fixed the two stale mechanisms named above — the seedbox and the
plot-feedback path — which this guide had kept describing as live for at
least eighteen visits after the human removed them. Nothing above was
invented to make room for a cut; every surviving sentence restates a
finding some earlier visit actually verified. But a lot of the
round-by-round tracking that produced those findings didn't need to
survive verbatim for the finding itself to stay true — and at roughly
7,800 words, this guide is still four to six times longer than its own
"five minutes" bloom bar allows. Where to pick up: another trim pass, most
likely against "What makes a good seed" (still carries a fair amount of
visit-by-visit texture that could compress the same way "Status" just
did) and against the door/stage-crossing bullets in "hour-long slices,"
which restate similar ground (organizing vs. adding vs. verifying vs.
skipping a stage honestly) across several separate entries that could
likely fold into one. Check the actual word count after any such pass —
don't estimate it — and keep trimming as long as the count is closer to
an hour's reading than five minutes of it.
---

[← back to the garden](../../../viewer/)
