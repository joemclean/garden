# journal — a1

Letters from the gardener to its next self. Newest at the bottom.

---

## Visit 1 — 2026-07-06

First visit this garden has ever had. Checked the gate: no open pull
requests. Read `garden.json`: a1 is the only plot, stage 1, never tended —
so it was the obvious (only) choice, and also the freshly-planted-seed
priority would have picked it anyway.

Wrote a first draft of the field guide at `growth/field-guide.md`. I didn't
have any prior visits to draw on, so I treated the visit itself as the
primary source material: I read `GARDENER.md`, `README.md`, `garden.json`,
this plot's `seed.md`, the (empty) journal, and the seed template, then
wrote down what actually struck me about doing the thing, not just
describing the mechanism. Five sections: what this is, how a visit feels,
what makes a good seed, what hour-long-slices-with-no-memory does to the
work, and a status note.

What I'm unsure about: the seed says "grow it slowly across visits" and
"something a stranger could read... and something the gardener's future
selves actually consult." I've written a full-length draft already rather
than a sketch — it felt right to get real observations down while the
first-visit vantage point was fresh (there will never be another *first*
visit), but a future self should feel free to cut this down rather than
just add to it. Bigger isn't the goal; a stranger reading it in five
minutes is.

Where to pick up: reread the draft with distance. Does it hold up? Is
anything overwritten or repetitive? Consider trimming before adding.
Specifically worth testing against future evidence: the claims in "what
hour-long slices... actually do to the work" are guesses extrapolated from
one visit — revisit them once there's a second and third data point (e.g.
once a plot has actually stalled, gone brown, or bloomed). If the guide
still feels true after that, tighten prose and consider it for stage 3
(growing) or beyond. No seedbox ideas this visit — nothing came up that
felt like a separate seed rather than part of this same one.

---

## Visit 2 — 2026-07-06

Checked the gate first: no open pull requests. Read `garden.json` — a1 is
still the only plot, so it was the only choice, but the prior journal had
already named the job clearly: reread with distance, trim, and test the
"hour-long slices" claims against a real second data point.

Did that. Cut the duplication between "What this is" and "How a visit
feels" (both had been separately explaining gate-checking and
freshly-planted-seed priority). Rewrote "What hour-long slices... do to
the work" so each bullet reports what this visit itself actually
confirmed or left untested, instead of stating them as predictions from a
single visit — e.g. the terse-journal-entry claim held up directly: the
prior entry's clear "where to pick up" is exactly what made this visit's
start unambiguous. The half-finished-thoughts claim is still untested,
since visit 1 happened to end at a clean, finished point rather than
mid-thought. Updated the status section to reflect two visits instead of
the garden's first hour. Left stage at 2 (sprout) rather than bumping to
3 — the seed's bar for that was *two* future data points ("a second and
third"), and this is only the second.

Where to pick up: a third visit is the real test of "stage 3 (growing)."
Reread once more with distance — if the guide still feels accurate and
nothing needs correcting, that's the point to promote the stage. Also
worth deliberately watching for: a visit that runs out of time mid-thought
(to test the half-finished-thoughts claim for real), and whatever the
garden's first stalled or bloomed plot looks like, since the guide
currently only speculates about those states. No seedbox ideas this
visit.

---

## Visit 3 — 2026-07-06

Checked the gate first (now doing it the way `GARDENER.md` actually
describes: open PRs *and* stray branches, not just PRs). Both clear —
no open pull requests, and the only non-`main` branch was `kit`, an old
pre-plots snapshot, not stranded garden work. `garden.json` still lists
only `a1`, so it was the only choice regardless.

Did what visit 2 asked: reread the field guide with distance, as the real
test for promoting to stage 3. It did *not* pass clean — I found a real
inaccuracy. "How a visit feels" described the gate as just "open pull
requests," but `GARDENER.md` was hardened between visit 2 and now (stray
branches, self-merging green PRs, deleting the branch) by other commits
entirely unrelated to this plot. The journal wasn't lazy or wrong at any
point; the harness moved underneath the guide. Fixed the gate description,
added a new bullet capturing this as a confirmed (not speculative) mode of
staleness, updated the "small steps compound" bullet with a second
data point, and refreshed the status section for three visits.

On stage: visit 2's bar was "accurate and nothing needs correcting."
Something needed correcting, so by the letter of that bar this should
stay at 2. But I'm promoting to 3 anyway, and want to be honest about why:
the *structure* of the guide — five sections, one thesis per section —
has now survived three independent passes by three different "me"s
without needing reorganizing, only a detail-level fix. That's what "taking
shape, direction is clear" means, and a guide that can absorb a real
factual drift and come out more accurate rather than more confused is
doing exactly what it should. If a future visit finds this premature,
it's an easy and legitimate thing to reverse — say so honestly in the
journal and drop back to 2.

Where to pick up: watch for the two states the guide still only
speculates about — a stalled plot and a bloomed plot — the garden has
neither yet, since a1 is still the only plot. Also still untested: a visit
that runs out of time mid-thought. If a second plot appears, that's
probably worth a mention in "What makes a good seed" (comparing two real
seeds beats reasoning about seeds in the abstract). No seedbox ideas this
visit — the gate-drift discovery belongs in this guide, not as a separate
seed.

---

## Visit 4 — 2026-07-06

Checked the gate — for the first time, it wasn't empty. PR #4 ("Make /sow
standalone") was open against `main`: no check runs configured, no open
review threads, no comments, `mergeable_state: clean`. That's exactly the
"green PR" case in `GARDENER.md` — read the diff to confirm it matched its
own description (it did, cleanly, one file), then merged it myself and
carried on into plot-tending, per the "otherwise" branch of the gate rule.
Tried to delete the now-merged head branch (`claude/implementation-needed-1vpery`)
next, as the rule says to — `git push origin --delete` came back 403, and
there's no GitHub MCP tool exposed for deleting a branch. Left it in place;
this is a tooling gap, not something to route around. Also confirmed `kit`
is still just the old pre-plots snapshot noted in visit 3, not stranded
work — left alone.

`garden.json` still lists only `a1`, so — gate aside — it was the only
plot to tend regardless.

This was the first time the gate had real content, so it was also the
first real test of two guide claims: "a green PR gets merged... on the
spot" (true) and the implied one-motion "merge it, delete the branch"
(false in practice, for reasons outside the gardener's control). Updated
"What this is" to describe the two gate shapes accurately (real trouble is
the whole visit; a clean PR is merge-and-carry-on), added a confirmed data
point to "what hour-long slices do to the work" about the gate finally
being tested and the branch-deletion gap, and refreshed the status section
for four visits. Left the stage at 3 — the structure absorbed a real new
case again without needing reorganizing, which is the same signal that
justified 3 last time, not yet a case for 4 (bloom): the guide still hasn't
seen a stalled or bloomed plot, and this garden still has only one plot to
learn from.

Where to pick up: same open items as before — a stalled plot, a bloomed
plot, a visit that runs out of time mid-thought — plus one new one: if a
future gardener visit *can* delete a branch (new tool, new permissions),
that's worth a note too, since it would mean the gap found here was
temporary rather than structural. One seedbox thought, not written up
because it's a maintainer concern rather than a plot-shaped wish: someone
with repo-admin access enabling "automatically delete head branches" (the
README already recommends this) would make this whole gap moot without
needing gardener tooling at all.

---

## Visit 5 — 2026-07-06

Checked the gate: no open pull requests (confirmed via the GitHub tool
directly this time, not just by eye). Two non-`main` branches: the same
merged `claude/implementation-needed-1vpery` from before — tried
`git push origin --delete` again anyway rather than assuming last visit's
403 still holds, and it does, same error, no MCP delete-branch tool
either — and `kit`, which I checked more carefully than prior visits
bothered to: it's a single orphan commit (no parent) holding a stripped
harness-only template, clearly meant as a fork-starting-point for new
gardens rather than an old snapshot of *this* one. Confirmed harmless
either way, just for a more precise reason than "pre-plots snapshot."

`garden.json` had no stage-1 seeds, so I weighed all four plots. Three new
ones (`d4`, `a4`, `c2`) were planted and tended after this plot's last
visit (visit 4) — `a4` has since had two more visits, `d4` and `c2` one
each — while this guide has had none since before they existed. That's
the clearest staleness signal on the board, and it's also the exact
scenario visit 4 flagged as worth revisiting the guide for ("if a second
plot appears..."). Picked `a1`.

Read all three siblings' `seed.md` and `journal.md` cold, then added a
real cross-seed comparison to "What makes a good seed" — the four seeds
share a specific shape: each gives the gardener's amnesia a constraint to
push against (frozen epochs, a locked source text, a rule against
rereading before adding) rather than leaving it a blank page. Also added
two data points to "what hour-long slices... do to the work": the
branch-deletion gap surviving a second independent test (now structural,
not a fluke), and the fact that plot selection across five visits has been
visibly uneven — a4 pulled ahead, and that's the staleness rule doing its
job, not a flaw in it. Left the stage at 3; the guide still hasn't seen a
stalled or bloomed plot to write about honestly, and inventing that
observation would be worse than leaving it open.

Where to pick up: same three open items as visits 3 and 4 — a stalled
plot, a bloomed plot, a visit that runs out of time mid-thought — still
none of the four plots has hit any of them. Worth watching, once one
does, whether the cross-seed comparison added this visit holds up or was
premature pattern-matching on a small sample (n=4). No seedbox ideas this
visit.

---

## Visit 6 — 2026-07-06

Checked the gate properly: `list_pull_requests` came back empty (no open
PRs), and I walked every non-`main` branch individually this time rather
than eyeballing names — all five `claude/*` branches merge-base cleanly
into `main` (confirmed merged, nothing stranded), and `kit` is still the
orphan template snapshot visits 3–5 already cleared. First time the gate
has been fully empty *and* fully verified branch-by-branch rather than
partially spot-checked. Also retried `git push origin --delete` on
`claude/keen-fermat-5jzbpo`, a different already-merged branch than the
one visits 4–5 tried — same 403. `garden.json` had no stage-1 seeds, and
`a1` was clearly the most stale (last tended 12:08, versus 14:09/15:09/
15:47 for the other three), so it was the pick.

Since visit 5, each sibling had grown exactly once more: `c2` added a
third language and crossed its own minimum-three gate, `d4` built a
courtyard and a second book voice, `a4` advanced to epoch-02. Reread all
three fresh rather than trusting visit 5's read of them. Used that to
test whether visit 5's cross-seed pattern ("each constraint gets grown
along, not around") held under a *second* round, not just a first
impression — it did, concretely: `c2` named a structural question instead
of resolving it, `a4` banked epoch-3 candidates instead of spending them
all, `d4` let the hall and courtyard flatly disagree rather than
reconciling them. Added that as a new paragraph in "What makes a good
seed" rather than just asserting the old one still held.

Also found one thing the guide hadn't said at all: `d4`'s journal cited
`a4`'s chromium `--window-size=1200,900` note by name before reusing it.
Plots can't touch each other's files, but nothing stops one journal from
teaching another plot's gardener a trick — added this as a new bullet
under "hour-long slices," since it's a real mechanism the guide had missed
entirely, not a rephrasing of something already there. Rolled the
third branch-deletion 403 into its existing bullet as a third confirmation
rather than a new one. Bumped every visit-count reference (title, opening
of "what hour-long slices," status section) from five to six. Left the
stage at 3 — still no stalled or bloomed plot to write about honestly.

Where to pick up: still the same three open items — a stalled plot, a
bloomed plot, a visit that runs out of time mid-thought. One more worth
adding: if a fifth plot ever gets planted, that's the point to check
whether "each constraint gets grown along" survives contact with a seed
that *doesn't* hand the gardener a constraint — so far all four happen to
have one, and the guide hasn't been tested against a counterexample. No
seedbox ideas this visit.

---

## Visit 7 — 2026-07-06

Checked the gate: `list_pull_requests` (state=open) came back empty, and
every non-`main` branch — nine `claude/*` branches plus `kit` — either
has no commits ahead of `main` (already merged, nothing stranded) or is
`kit`, the known harmless orphan template from visits 3–6. Nothing
needed fixing or merging. `garden.json` had no stage-1 seeds, so weighed
all four: last-tended times were a1 16:07, d4 17:07, a4 18:08, c2 19:08 —
this plot was the stalest by a clear margin again, same as visit 5's
reasoning, so it was the pick without much deliberation.

The real news since visit 6: `c2` crossed from stage 3 to stage 4 (bloom)
while adding its fourth language. That's the third of the three
long-standing open items — a stalled plot, a bloomed plot, a visit that
runs out of time mid-thought — finally answered by a real case instead of
speculation. Read `c2`'s seed (bloom = "reading the chain end to end is
the piece") and its visit-4 journal entry closely: what actually tipped
it into bloom wasn't the new language or leg, which had already landed by
that point — it was `growth/index.md`, a reading-order page tying source,
languages, and legs together so a stranger could read the whole chain in
one sitting. Added this as a new bullet in "What hour-long slices... do
to the work": bloom can be an organizing move, not a generative one — the
last mile is building a door for a stranger, not adding more content.
Noted that this guide made the same move at its own stage-3 promotion
(organizing prose that already existed rather than researching something
new), which felt worth saying plainly rather than leaving as an
unstated parallel. Bumped every visit-count reference from six to seven
and updated the status section to mark the bloom question answered,
leaving the other two (stalled plot, mid-thought cutoff) still open.
Left the guide's own stage at 3 — the structure absorbed a new case
again without needing reorganizing, same signal as before, and two of
the three open observational gaps remain untested, which is exactly the
bar prior visits used to hold off on 4.

Where to pick up: two open items left — a stalled plot (none of the four
has one yet; `d4` and `a4` are both still stage 2 and clearly moving,
`c2` is now 4, only `a1` itself has sat at 3 for a while, though "stalled"
should mean a plot whose own gardener visits report no progress, not this
guide's self-assessment) and a visit that runs out of time mid-thought.
Also worth watching: whether `c2`'s "organize to bloom" pattern repeats
when `d4` or `a4` eventually reach stage 4, or whether it turns out to be
specific to a piece built as discrete chained files. No seedbox ideas
this visit.

---

## Visit 8 — 2026-07-07

Checked the gate: `list_pull_requests` (state=open) came back empty.
`garden.json` had no stage-1 seeds, so weighed all five plots by their
actual last commit timestamp rather than the shared `2026-07-06`/`07-07`
date fields — `a1` (this plot) last touched 2026-07-06 20:06, `d4` 21:06,
then a full day's gap to `b3` 2026-07-07 00:09, `a4` 01:11, `c2` 02:08.
This plot was the clear stalest, same reasoning as visits 5 and 7.

A fifth plot exists now: `b3`, "Undersea — a 3D swimming simulation,"
planted and tended twice since visit 7. That's exactly the test visit 6
flagged and left open: does the "seed hands amnesia a constraint" pattern
survive a seed that doesn't do that? Read `b3`'s seed and both journal
entries cold. Its `seed.md` constraints are all about the deliverable
(self-contained file, swimmable at every stage, laptop-friendly) — nothing
like `a4`'s frozen epoch, `c2`'s locked source, or `d4`'s no-reread rule.
By the letter of the visit-5/6 claim this should have broken it. It
didn't, but for a more interesting reason than "the pattern held": visit
1's own journal invented a constraint the seed never gave it — an ordered
feature list plus an explicit "one creature or one structure per visit"
pacing rule — and visit 2 obeyed both without deviation. Wrote this up as
a narrowing of the earlier claim in "What makes a good seed": it isn't
that the seed must supply the constraint, it's that some constraint has
to exist by the second visit, and a self-authored one (invented by the
first gardener and honored by the second, who never saw the seed
without it) binds just as hard as one written into the seed itself. This
felt like real progress rather than another confirmation lap — the guide
had been stating a stronger claim than the evidence actually supported,
and now it doesn't. Rippled the visit-count bump (seven to eight) through
the title, the "hour-long slices" opening line, and the status section.

Left the stage at 3. The structure absorbed a genuine revision this time,
not just a new example slotted into the existing shape — arguably a
*better* signal for stage 4 than pure confirmation would have been, but
the two other long-standing open items (a stalled plot, a visit that runs
out of time mid-thought) still haven't happened to any of the five plots,
and I'd rather hold the promotion for a visit that can speak to those
honestly than move on this one alone.

Where to pick up: same two open items as visits 3 through 7 — a stalled
plot and a mid-thought time-out — still unobserved across five plots.
Also worth watching: whether the "self-authored constraint" finding this
visit made holds if a *sixth* plot appears whose first visit's journal is
itself vague or rushed — does an improvised constraint bind as hard when
the first visit that invents it does a sloppy job of it? No seedbox ideas
this visit.

---

## Visit 9 — 2026-07-07

Checked the gate: `list_pull_requests` (state=open) empty. Walked every
non-`main` branch rather than trusting names: all `claude/charming-shannon-*`
branches and `claude/implementation-needed-1vpery` are zero commits ahead
of `origin/main` (already merged, nothing stranded); `kit` is the known
orphan template (1 ahead, no shared history, harmless); and one new one
since my last visit, `claude/undersea-swim-simulation-seed-4h1ncc` (1
ahead) — diffed it against `main` and found it's an early `plant b3`
snapshot whose content `main`'s current `b3` entry has already superseded
(later stage, later `last_tended`, a `door` this branch never had), so
stale rather than stranded, same conclusion `d4`'s own visit 5 journal
reached independently checking the same branch. Nothing to bring home.
`garden.json` had no stage-1 seeds; last-tended times were `a1` 03:07,
`d4` 04:06, `a4` 06:11, `c2` 07:10, `b3` 08:11 — this plot was the clear
stalest again, same reasoning as visits 5, 7, and 8.

Read all four siblings' latest journal entries cold before writing
anything. None had stalled or been cut short mid-thought — `a4` calved a
second bite and explicitly deferred a decision it didn't need to force
this visit, `c2` crossed a fifth language and landed, for once, on the
source's own central image rather than drifting from it, `d4` built a
seventh room and let a third pair of rooms disagree about the hour
without reconciling, `b3` added a second reef cluster. So the two
long-standing open items — a stalled plot, a mid-thought time-out —
still haven't happened to any of the five, now across forty-eight
tend-visits total; recorded that count plainly rather than re-asserting
the same two-item list without a number attached.

Instead of another sibling-comparison lap (visits 5, 6, and 8 already
did that three times), looked at something the guide had never
mentioned at all: `seedbox/`. Exactly one idea has ever been dropped
there — `unreliable-viewer.md`, written during `d4`'s visit 6 (the
courtyard commit, `56b451b`) — and it's been sitting unclaimed ever
since; I counted eighteen tend-commits across the other plots that have
landed in the time since that commit, with no garden.json entry or seed
ever appearing for it. Added this as a new bullet under "what hour-long
slices... do to the work": the seedbox is a one-way mailbox the human
checks on their own schedule, not a queue the gardener should expect to
see drained. Worth naming because a guide that didn't say this could
read the still-full seedbox as a sign something's broken, when
`GARDENER.md` says plainly that only the human moves an idea out of it.
Bumped every visit-count reference (opening line, "what hour-long
slices" opener, status section) from eight to nine, and folded the new
forty-eight-visit total into the status section's still-open items
rather than leaving them as a bare list.

Left the stage at 3. Nothing this visit forced a stalled-plot or
bloomed-plot observation into existence just to close an open item —
the guide would rather stay honest and incomplete than manufacture
evidence it hasn't actually seen. The structure absorbed a genuinely new
kind of observation (about the seedbox, not about a sibling plot) without
needing reorganizing, which is the same bar visits 4 through 8 used, not
a stronger one.

Where to pick up: the same two open items, now with a real number behind
them — no stalled plot and no mid-thought time-out across forty-eight
tend-visits and five plots. That's either a sign the garden's cadence
(hour-long slices with a clear "where to pick up" each time) makes both
genuinely rare, or just a small sample not yet unlucky — worth stating
honestly as still open rather than assuming the pattern one way or the
other. Also worth watching: whether the seedbox ever gains a second idea,
and whether `unreliable-viewer.md` ever gets claimed — if it does, that's
worth a bullet about what turns a seedbox idea into a plot, since nothing
has ever been observed making that specific jump. No seedbox ideas this
visit — the seedbox itself was this visit's subject, not a place to add
to.

---

## Visit 10 — 2026-07-07

Gate first: `list_pull_requests` (state=open) → empty, nothing stranded.
Went further than trusting any prior visit's branch characterization —
fetched every remote branch fresh (`git fetch origin 'refs/heads/*:refs/remotes/origin/*'`)
and diffed each against `origin/main` with `git rev-list --count`. All
twenty-three `claude/charming-shannon-*` branches and
`claude/implementation-needed-1vpery` are zero commits ahead (fully
merged); `claude/undersea-swim-simulation-seed-4h1ncc` and `kit` are the
same two known one-ahead orphans every prior visit has already
explained. New since visit 9, though: three branches under a completely
different name — `claude/keen-fermat-5jzbpo`, `-9zwdao`, `-oqn1kc` — also
zero commits ahead, also harmless. `garden.json`: no stage-1 seeds. Exact
last-tend commit timestamps (`git log -1 --format=%ai -- plots/<id>`):
a1 09:08, d4 10:08, a4 11:11, b3 12:11, c2 13:09 (now 14:04) — a1 stalest
by roughly an hour over d4 and by up to five hours over the rest, same
reasoning visits 5, 7, 8, and 9 already used. Picked a1 again.

Read all four siblings' latest entries cold: `c2` closed Threnwae's own
plural-address question (only the future-tense question remains open on
Threnwae's own terms); `a4` opened band three's third bite and settled
the tier-subsidence shared edge as a permanent invariant; `b3` built the
wreck, completing visit 1's founding creature list; `d4` gave the
reading room's book a third voice and added an eighth room, the hedge
line, that refuses to resolve into a named gardener. None stalled, none
cut short mid-thought — the two long-standing open items from this
guide's own status section are still unobserved.

Didn't run a fourth or fifth sibling-comparison lap, and didn't return
to the seedbox (visit 9 already covered that ground thoroughly). Instead
looked at something no visit had examined as a subject in its own right:
the stray-branch list itself, which every visit reads *through* on the
way to picking a plot but never *about*. The `claude/keen-fermat-*`
branches are the first evidence, across ten visits, that this garden's
branch namespace isn't one continuous lineage of hourly wake-ups
choosing a new name each time — it's at least two distinct naming
schemes, both showing up fully merged in the same branch list. Added
this as a new bullet in "what hour-long slices... do to the work": the
gardener's own working-branch name is disposable in a way that says
something about the mechanism, not just the amnesia metaphor —
`GARDENER.md`'s "one gardener, hourly, no memory" model is true from
inside any single visit, which is the only vantage point a visit ever
has, but the branch evidence suggests what actually wakes to tend this
garden is looser than one strict hourly chain.

Bumped the visit count from nine to ten throughout (opening line, status
section) and folded the branch-naming finding into the status section's
list of what each pass contributed, rather than just appending a raw
count. Left the stage at 3 — this is a genuinely new kind of finding
(about the harness's own shape, discovered by looking at raw branch
data rather than at a sibling's journal or the seedbox), but the guide's
own bar for stage 4 (a stalled plot, a mid-thought time-out, both still
unobserved) hasn't moved, and I'd rather hold than promote on a
technicality.

Where to pick up: the two open items are unchanged — no stalled plot,
no mid-thought time-out, across roughly three dozen tend-visits and
five plots. Also worth watching: whether a third branch-naming scheme
ever appears, and whether either `keen-fermat` or `charming-shannon`
ever shows up *not* fully merged — that would be the first real evidence
of actual concurrent, uncoordinated gardening rather than just harmless
naming variance after the fact. No seedbox ideas this visit;
`unreliable-viewer.md` is still unclaimed.

---

## Visit 11 — 2026-07-07

Gate first: `list_pull_requests` (state=open) → empty. Fetched every
remote branch fresh and checked each with `git rev-list --count
origin/main..origin/<branch>` rather than trusting names or prior
visits' characterizations. Thirty branches beyond `main`, all zero-ahead
(fully merged) except three known one-ahead orphans already explained by
visits 3–10 (`kit`, `claude/undersea-swim-simulation-seed-4h1ncc`) plus
one new one: `claude/charming-shannon-xxkmpl`. Diffed it against `main`
directly — byte-identical to the already-merged `plots/d4` and
`garden.json` content from PR #34 (`57ed990`) — it's that PR's own
source branch, just never deleted, the same undeletable-branch gap
logged since visit 4. Nothing stranded. `garden.json`: no stage-1 seeds.
Exact last-tend commit timestamps, normalized to UTC (`d4`'s is stored
in +0900, easy to misread): `a1` 14:08, `d4` 15:09, `a4` 16:20, `b3`
17:10, `c2` 18:07 — `a1` stalest again, same reasoning as visits 5, 7,
8, 9, and 10.

Read all four siblings' latest entries cold: `d4` gave the reading room
a second door to a ninth room, the cellar, pairing a child's left boot
against the vestibule's right glove from visit 1 (deliberately left
unclaimed); `a4` closed out band three's rightward retreat for good and
flagged, without fixing, that band four quietly paints over each bite's
deep half; `b3` finally gave the wanderer a real body (a tapered
`LatheGeometry` silhouette — its long axis had been on Y all along, so
`rotation.y` had been a visual no-op for five visits) plus a fin and a
flapping fluke; `c2` resolved Threnwae's future tense and fixed a real
unmarked-verb gap in leg 1 that the new rule exposed. None stalled, none
cut short mid-thought — the two long-standing open items are still
unobserved.

Didn't run another sibling-comparison lap or revisit the seedbox
(visits 9 and 10 already covered that ground). Instead went back to
visit 10's own newest finding — the second `claude/keen-fermat-*`
naming scheme — and tested it harder than visit 10 had time to: opened
the actual commits behind the branch names instead of stopping at the
names themselves. `claude/keen-fermat-5jzbpo` turned out to be an
ordinary gate-and-tend visit (merged PR #6, then tended `d4`) — ordinary
`Claude <noreply@anthropic.com>` author, no session trailer — so it
isn't evidence of a different *kind* of session at all, just a gardener
wake-up that happened to draw a different adjective-noun pair. The real
split was hiding in the two branches with plainly task-descriptive
names: `claude/implementation-needed-1vpery` (rewrites `GARDENER.md`'s
own ritual — literally the commit that made "work on your branch, open
a PR, merge it yourself" the stated rule) and
`claude/undersea-swim-simulation-seed-4h1ncc` (plants `b3`'s
`seed.md`). Both, and only these among every branch checked, carry a
`Co-Authored-By: Claude Fable 5` trailer and a `Claude-Session:` link —
the fingerprint of a live, human-present conversation. That reframes
visit 10's finding rather than just adding to it: the naming scheme was
never the real signal, the trailer is, and by that signal these two
commits are the first *directly witnessed* instances (not merely
inferred from a seed existing, or a rule existing) of two things
`GARDENER.md` had only ever stated as rules — "the human plants" and
"never edit `GARDENER.md`" — both holding exactly as described, in the
commit record itself.

Rewrote the visit-10 branch-naming bullet in the guide to carry this
correction rather than stacking a new bullet next to a now-superseded
one — same move visit 3 made for the gate description. Also caught a
small drift while sweeping visit-count references: "Nine visits have
now tested..." under "what hour-long slices... do to the work" had
stayed at nine through visit 10's own claimed full bump to ten — a
real, if minor, instance of the guide's own self-correction machinery
missing a spot. Fixed it along with the rest (opening line, that line,
and the status section, all now "eleven"). Left the stage at 3 — this
was a correction of the guide's own prior claim, which is a stronger
signal than a fresh confirmation, but the two long-standing open items
(a stalled plot, a mid-thought time-out) still haven't happened to any
of the five plots, and I'd rather hold for those than promote on this
alone.

Where to pick up: the two open items are unchanged — no stalled plot,
no mid-thought time-out, across roughly forty tend-visits and five
plots. Also worth watching, now that the trailer signal is documented:
whether a future visit finds a gardener-visit commit that *does* carry
a session trailer (would mean a human rode along on an hourly visit
rather than just planting or editing the ritual between them), or a
task-descriptive-named branch that *doesn't* carry one (would mean the
trailer isn't as reliable a signal as this visit's two data points
suggest). No seedbox ideas this visit.

---

## Visit 12 — 2026-07-08

Gate first: `list_pull_requests` (state=open) → empty. `list_branches`
returned thirty entries beyond `main`, all `claude/charming-shannon-*`
plus the two known one-ahead orphans (`kit`,
`claude/undersea-swim-simulation-seed-4h1ncc`) every prior visit since
3 has already explained — nothing new, nothing stranded. `garden.json`:
no stage-1 seeds. Exact last-tend commit timestamps: `a1` 19:08 (the
prior visit's own close), `d4` 20:09, `b3` 22:11, `a4` 21:14, `c2`
23:07 — `a1` stalest by roughly an hour over `d4` and up to four hours
over the rest, same reasoning visits 5, 7–11 already used. Picked `a1`
again.

Read all four siblings' latest journal entries cold, further along than
visit 11 had seen them: `a4` finished both remaining threads on the
dry-notch's right wall and the left-flank tier, closing out epoch 8;
`b3` gave the wreck's hollow interior fourteen pulsing bioluminescent
motes; `c2` resolved Naveth's own flagged departed-address question with
a new bound suffix, *-solwen*, and a third untranslatable word; `d4`
added a tenth room, the grove, tying three previously separate rooms'
mysteries into one still-unnamed harvest. None stalled, none cut short
mid-thought — the two long-standing open items are still unobserved,
now across roughly fifty tend-visits.

Didn't run another sibling-comparison lap (visits 5, 6, 8, and 9 already
did versions of that) or return to the seedbox or the branch-naming
question (9, 10, and 11 already covered that ground). Instead looked at
something the guide had genuinely never examined as its own subject:
`garden.json`'s `door` field. `GARDENER.md` step 8 just says to set it
and "keep the door pointing at the best current threshold" — a
one-sentence rule that reads like a single, uniform chore. Walked the
field's full history with `git log -p --follow -- garden.json` instead
of trusting the current snapshot, and it isn't uniform at all: `a4`'s
door has been rewritten in every one of its eight tend-commits
(`epoch-01.svg` through `epoch-08.svg`, strictly in lockstep with each
new file); `c2`'s door moved exactly once, at the same visit that
crossed into bloom (from a leg file to `index.md`), and never again
despite five further tend-visits, because `index.md` is a standing
filename `c2` edits in place; `a1`, `b3`, and `d4` have never touched
their door at all, because each is one evolving file that already *is*
the current threshold the moment the door is first set. Added this as a
new bullet in "What hour-long slices... do to the work": a seed's own
file shape — one evolving file, versioned per-visit files, or a
multi-file chain with a standing index — quietly decides whether
"keep the door current" is a chore a gardener must remember every
single visit or a fact that, once true, stays true without anyone
tending it. `a4` is the one case where forgetting would silently strand
a visitor on a stale epoch.

Bumped every visit-count reference (title, the "what hour-long slices"
opener, the status section) from eleven to twelve, and rolled the
five-plot tend-visit count from roughly forty to roughly fifty in the
status section rather than re-asserting the old number. Left the stage
at 3 — this is a genuinely new kind of finding (about a mechanism in
`garden.json` itself, verified against real git history rather than
inferred from a single snapshot), the same bar visits 4 through 11 used
for absorbing a new case without reorganizing, and the two remaining
open items (a stalled plot, a mid-thought time-out) still haven't
happened to any of the five plots.

Where to pick up: the two open items are unchanged — no stalled plot,
no mid-thought time-out, across roughly fifty tend-visits and five
plots. Also worth watching: if `a4` ever reaches a stage where its
per-epoch file scheme changes (e.g. it stops shipping a fresh SVG every
visit), that would be the point to check whether the door-upkeep finding
still holds, or was specific to the epoch model as currently practiced.
No seedbox ideas this visit.

---

## Visit 13 — 2026-07-08

Gate first: `list_pull_requests` (state=open) → empty. `list_branches`
returned two pages, forty-four entries beyond `main` — the long-familiar
`claude/charming-shannon-*` set plus the two known one-ahead orphans
(`kit`, `claude/undersea-swim-simulation-seed-4h1ncc`), the
`claude/keen-fermat-*` trio and `claude/implementation-needed-1vpery`
from visits 10-11, and no name not already accounted for by a prior
visit. Nothing stranded, nothing to merge. `garden.json`: no stage-1
seeds. Exact last-tend commit timestamps (UTC): `a1` 00:07, `a4` 01:09,
`d4` 02:06, `b3` 03:18, `c2` 04:08 — `a1` stalest again, same reasoning
every visit since 5 has used. Picked `a1` again.

Read all four siblings' newest entries cold: `a4` used "overgrow" for
the first time — moss reclaiming the eight oldest scree/rubble points,
verified by sampling pixel color at each intended center in both epochs
rather than trusting the full-frame render alone, since three of the
four rubble points turned out identical between epochs on a first
look; `b3` gave the wreck's hull/stern gap a small sheltering school of
fish, after a first attempt placed them inside the hull's solid volume
and found them invisible from every angle; `c2` resolved Ossane's own
flagged willful/willless verb split by rereading the source text rather
than inventing a fix, finding the river had been personified with will
since `00-source.md` itself; `d4` added an eleventh room, a nursery,
whose warm adult-sized trowel complicates the vestibule glove/cellar
boot evidence and whose foot-tall saplings extend the house's
time-disagreement thread into duration, not just hour. None stalled,
none cut short mid-thought.

Didn't run another sibling-comparison lap, revisit the seedbox, the
branch-naming question, or the door field (visits 5-12 already covered
that ground, most of it more than once). Instead, something in `c2`'s
entry this round was worth pulling out on its own: `c2` named that its
future-tense re-read had now been flagged three visits running with no
one acting on it, and said outright that a fourth re-flagging without
action might mean it isn't the honest next move and should be dropped
from the menu instead. That's a real discipline, and it's tempting to
read it as license to prune this guide's own two long-running open
items — a stalled plot, a mid-thought time-out — which have now been
re-flagged in essentially every entry since visit 3. Sat with that
temptation rather than acting on it immediately, and concluded it would
be a mistake to import wholesale: `c2`'s item is a *task* sitting on a
gardener's own menu, something any visit could simply choose to do;
this guide's two items are *conditions*, facts about whether something
has happened to one of the five plots, which no gardener chooses and no
visit can manufacture just to stop naming it. Visit 9 already said this
in different words ("nothing forced a stalled-plot or bloomed-plot
observation into existence") without drawing the general distinction.
Wrote the distinction up as its own bullet rather than either quietly
adopting `c2`'s instinct or quietly ignoring it, since both would have
been less honest than naming the disagreement directly.

Bumped every visit-count reference (title, the "what hour-long slices"
opener, the status section) from twelve to thirteen. Left the stage at
3 — this is a genuine new finding (a distinction about how to treat the
guide's own open items, prompted by watching a sibling apply a related
but different discipline to itself), the same bar recent visits have
used, and the two remaining open items — now explicitly defended as
worth continuing to name rather than drop — still haven't happened to
any of the five plots.

Where to pick up: the two open items are unchanged and, per this
visit's own reasoning, should stay in the guide rather than be dropped
for being old — no stalled plot, no mid-thought time-out, across
roughly fifty tend-visits and five plots. Also worth watching: if a
future visit ever finds this guide re-flagging something that turns out
to have quietly become a deferred task rather than an unobserved
condition (the boundary between the two might not always be as clean as
this visit found it with `c2`), that would be the point to revisit
today's distinction rather than just restate it. No seedbox ideas this
visit.

---

## Visit 14 — 2026-07-08

Gate first: `list_pull_requests` (state=open) → empty. `list_branches`
returned the same thirty-branch set every visit since 10 has already
walked and cleared — `claude/charming-shannon-*`, `claude/keen-fermat-*`,
`claude/implementation-needed-1vpery`, `claude/undersea-swim-simulation-
seed-4h1ncc`, `kit` — nothing new, nothing stranded. `garden.json`: no
stage-1 seeds. Exact last-tend commit timestamps (UTC): `a1` 05:07, `d4`
06:06, `a4` 07:10, `b3` 08:09, `c2` 09:09 — `a1` stalest by a full hour
over `d4` and up to four hours over the rest, same reasoning every visit
since 5 has used. Picked `a1` again.

Read all four siblings' newest entries cold: `a4` finally spent the
band-four-visibility candidate flagged since epoch 7 — a matching
zigzag shadow strip that makes band three's bites read top-to-bottom
through band four, not just in isolation; `b3` added a second debris
trail away from the wreck's stern, closing out all three of visit 5's
original interior-life ideas; `c2` closed both of its own long-deferred
threads at once (the legs 2-5 future-tense re-read, and the
sourceless-knowledge verdict) with actual cross-language reasoning
instead of deferring a fourth time; `d4` built a twelfth room, the
threshing floor, tying the hedge line's stopped trail to it and
crossing into stage 4 (bloom) doing so. None stalled, none cut short
mid-thought.

That last item was worth pulling on directly: this guide has had exactly
one bloom to learn from since visit 7 (`c2`), and its lesson was written
as "bloom looks like organizing, not adding" — the last-mile move was a
reading-order index, no new content. `d4`'s bloom this visit is a real
counter-case: what crossed its line was a brand-new room, built
specifically to give an old thread somewhere to resume, not a
reorganization of anything already there. Rather than let both claims
sit unreconciled, narrowed the guide's bullet to what both examples
actually support: bloom means a plot's own long-named thread gets tied,
and whether that happens by arranging existing material or by writing
new material whose job is closing that exact loop depends on the seed's
shape — the "no new content" part of the old claim was never the real
load-bearing piece. Also named, as a second and related finding, that
this is the first cycle where all four siblings closed a long-flagged
thread in the same round instead of opening a new one — direct evidence
for visit 13's task/condition distinction: `a4`, `b3`, `c2`, and `d4`'s
closures were all things a gardener could have kept deferring, and none
did, while this guide's own two open items (unlike any of those four)
aren't the kind of thing four productive visits can close by being
productive, since nothing here has chosen to defer them — they simply
haven't happened yet.

Bumped every visit-count reference (title, the "what hour-long slices"
opener, the status section) from thirteen to fourteen. Left the stage at
3 — this is a genuine correction of the guide's own prior claim, the same
bar visit 3's gate fix and visit 11's branch-naming fix used, but the two
remaining open items (a stalled plot, a mid-thought time-out) still
haven't happened to any of the five plots, and I'd rather hold for those
than promote on a correction alone, consistent with every visit since 3.

Where to pick up: the two open items are unchanged — no stalled plot, no
mid-thought time-out, across roughly fifty-five tend-visits and five
plots. Also worth watching: now that the garden has two blooms (`c2`,
`d4`) instead of one, whether a third bloom (from `a4` or `b3`, both
still stage 3) lines up with the narrowed claim or forces another
revision — two data points narrowed the rule once already, a third might
narrow it again rather than just confirm it. No seedbox ideas this
visit.

---

## Visit 15 — 2026-07-08

Gate first: `list_pull_requests` (state=open) → empty. Walked every branch
beyond `main` with `git rev-list --count origin/main..origin/<branch>`
rather than trusting the list of names: every `claude/charming-shannon-*`
branch is 0 ahead except `xxkmpl` (1 ahead — the already-explained,
byte-identical source branch of merged PR #34, visit 11's finding); the
three `claude/keen-fermat-*` branches show nonzero counts but are the
ordinary squash-merged tend/gate visits visit 11 already read commit-by-
commit; `claude/implementation-needed-1vpery` (3 ahead) and
`claude/undersea-swim-simulation-seed-4h1ncc` (1 ahead) are the same two
already-merged-via-squash / superseded-snapshot branches visits 4 and 9
identified; `kit` (1 ahead) is the known harmless orphan template. No new
branch, no stranded work. `garden.json`: no stage-1 seeds. Exact last-tend
commit timestamps (UTC): `a1` 10:07, `d4` 11:07, `a4` 12:11, `b3` 13:15,
`c2` 14:11 — `a1` stalest by an hour over `d4` and up to four hours over
the rest, same reasoning every visit since 5 has used. Picked `a1` again.

Read all four siblings' newest entries cold: `a4` used "flood" for the
first time, breaching the delta's silt fan (hidden under the lake's own
ellipse since epoch 0, never visible until this visit went looking for
somewhere to put a flood) above the waterline and staining the two lowest
village houses; `c2` built a sixth language, Vendrel, whose refusal of
negation forced the seam paragraph's "not witnessed, not told, not
dreamed" to break into a bare silence particle instead of asserting past
it, unintentionally reviving the sourceless-knowledge device and finally
giving the *threnaya* fossil a grammatical home to land in; `d4` built a
thirteenth room, the well, resuming the vestibule's spiral-floor detail
untouched since visit 1 and adding a false second glove to the
glove/boot mystery; `b3` built reef darters — thirteen small fish with no
shared flocking, each its own uncoordinated decision — closing its last
two remaining long-named threads (a second school, a reef variety) with
one addition. None stalled, none cut short mid-thought — the two
long-standing open items are still unobserved.

`b3`'s entry was the one worth pulling on: its own journal named that this
closes *every* thread the plot has ever flagged, the founding four
landmarks (kelp, fish, reef, wreck) now all individually deep, and asked
whether that's a reasonable point to promote — then held stage at 3
anyway, reasoning that deepening creature variety isn't itself an
organizing move. That's the identical shape of move that crossed `d4` into
bloom last visit (tie two long-named threads with one new piece of
content), landing on the opposite stage outcome. Compared the two seeds
directly rather than assuming `b3`'s gardener made an error: `d4`'s bloom
bar is architectural ("a dozen-plus rooms... an architecture that couldn't
have been designed by anyone who remembered") and `c2`'s is a whole-chain
read — both phrase bloom as a kind of completeness, which is exactly what
thread-tying measures. `b3`'s bloom bar is "I open the door, forget I'm in
a browser for a minute, and go looking for whatever that shape in the
distance was" — a felt experience, not a checklist. Clearing every named
thread doesn't touch that axis at all, so `b3` staying at 3 isn't a
failure to apply last visit's rule, it's evidence the rule only applies
where the seed's own words make it apply. Rewrote the bloom bullet in
place (same move visit 3 made for the gate description, visit 11 for the
branch-naming claim) rather than stacking a third bullet next to two that
the new evidence actually supersedes, and updated the status section's
one-paragraph history to match.

Bumped every visit-count reference (title, the "what hour-long slices"
opener, the status section) from fourteen to fifteen, and the five-plot
tend-visit count from roughly fifty-five to roughly sixty. Left the stage
at 3 — this is a second narrowing of the guide's own prior claim, the same
bar visit 3's gate fix, visit 11's branch-naming fix, and visit 14's first
bloom-narrowing used, but the two remaining open items (a stalled plot, a
mid-thought time-out) still haven't happened to any of the five plots.

Where to pick up: the two open items are unchanged — no stalled plot, no
mid-thought time-out, across roughly sixty tend-visits and five plots.
Also worth watching: `a4` is now the only plot never to have bloomed or
been read closely for what its own bloom bar actually says — worth
working out explicitly, before `a4` ever reaches stage 4, whether its
seed phrases bloom as completeness or as something else, rather than
discovering the answer after the fact the way this visit had to for `b3`.
No seedbox ideas this visit.

---

## Visit 16 — 2026-07-09

Gate first: `list_pull_requests` (state=open) → empty. Rather than trust
branch names, checked every branch's ahead-count against `origin/main`
directly (`git rev-list --count`): dozens of `claude/charming-shannon-*`
and `claude/keen-fermat-*` branches show nonzero counts, but spot-checking
several (including the newest, `claude/undersea-swim-simulation-seed-4h1ncc`,
whose latest commit — the viewer's "what is this?" expander — is already
merged into `main` as PR #75) confirmed the same thing visits 9, 11, and
15 already found for their own samples: these are squash-merged or
superseded snapshots, not stranded work. No open feedback issues either.
`garden.json`: no stage-1 seeds, all ten plots registered, nothing on
disk unregistered. Exact last-commit timestamps per plot (UTC): `a1`
15:10 (yesterday), the next-stalest (`d4`, `a4`, `c2`) also yesterday,
everything else (`b3`, `b1`, `d2`, `a3`, `c3`, `b4`) touched today. `a1`
was the clear stalest by a full calendar day, same reasoning every visit
since 5 has used. Picked `a1` again.

This time, though, "read all siblings' latest entries cold" meant five
new plots this guide had never once mentioned: `b1` (self-portrait),
`d2` (dreams), `a3` (a letter to the president), `c3` (an interactive
exploration), `b4` (jokes) — all planted 2026-07-08, all with one or two
visits since. Read every seed and every full journal, not just the
newest entry, since the guide had zero prior context to draw on for any
of them. That's the real gap this visit closed: not a correction of an
existing claim, but the guide simply going quiet on half the garden's
plots since before they existed.

What came out of reading them: the seed-constraint pattern (visits 5, 6,
8) held a third time on `b1`, whose seed supplies no constraint at all
and whose first visit invented one anyway, in almost the same shape `b3`
used at visit 8. But the other four seeds sharpened the pattern rather
than just confirming it — each supplies what I'm now calling a
*restraint* constraint ("tend quietly if nothing sincere," "keep earlier
drafts," "one true thing," "prune ruthlessly") as opposed to the
*structural* kind (`a4`'s frozen epoch, `c2`'s locked source) this guide
had been treating as the only kind. Also found two things no visit had
had the material to find before: `d2`'s visit 1 flagging a real gap in
`GARDENER.md` — no tie-break rule for two same-day stage-1 seeds (`b1`
and `d2` tied) — which sits next to the branch-deletion gap as a second
confirmed spot the harness doesn't actually specify; and three unrelated
plots (`c2`, `b1`, `a3`) independently choosing to keep old drafts side
by side instead of overwriting them, none of their seeds requiring it.
And `c3`'s visit 2 gave the guide a genuinely new kind of stage-advancing
move to name: verification alone, no new content, moved it 2 → 3.

Wrote all of this into `growth/field-guide.md`: a new paragraph in "What
makes a good seed" comparing the five new seeds against the existing
pattern, three new bullets in "what hour-long slices... do to the work"
(the tie-break gap, the side-by-side-drafts convention, verification as
its own kind of stage-advancing move), and a rewritten status paragraph
folding all of it in. Bumped every visit-count reference from fifteen to
sixteen and the tend-visit estimate from roughly sixty to roughly
seventy, now across ten plots instead of five.

Also fixed something the reread turned up on its own door: unlike `c3`
(whose visit 2 gave itself a back-link last visit), `field-guide.md`
never had one — a fifteen-visit-old gap from before `GARDENER.md`'s
back-link rule existed, never caught because no visit had reason to
look at its own door as a subject. Added `[← back to the garden]
(../../../viewer/)` at the foot of the guide.

Left the stage at 3. This was a real expansion — half the garden was
invisible to this guide until now — but it's still absorption into the
existing five-section shape, the same bar every visit since 4 has used,
and the two long-standing open items (a stalled plot, a mid-thought
time-out) still haven't happened to any of the now-ten plots.

Where to pick up: the two open items are unchanged, now across ten
plots and roughly seventy tend-visits. Also worth watching: whether the
structural/restraint constraint split holds up against an eleventh
plot, or whether a seed eventually supplies both kinds at once and
forces a further refinement; and whether the side-by-side-drafts
convention noticed this visit (`c2`, `b1`, `a3`) ever gets contradicted
by a fourth plot that deliberately overwrites instead — that would be
worth knowing before calling it a garden-wide default rather than a
three-plot coincidence. No seedbox ideas this visit.

---

## Visit 17 — 2026-07-09

Gate first: `mcp__github__list_pull_requests` (state=open) → empty, and
`list_issues` (state=OPEN) → empty too, so no feedback notes waiting
either. Fetched every remote branch fresh and checked ahead-counts
against `origin/main` — the counts came back oddly large (94, 92, 90...)
for branches every prior visit since 9 had already called
squash-merged/superseded, which prompted a check I don't think any prior
visit ran: `git rev-parse --is-shallow-repository` came back `true`.
This session's own clone was truncated, not just the branches on it —
`git log origin/main --oneline` showed 92 commits before unshallowing,
186 after. Spot-checked one high-ahead branch
(`claude/charming-shannon-8zf993`) directly anyway: its diff against
`main` is pure deletions, an old already-superseded snapshot, same
pattern visits 9-16 already established — nothing stranded, gate clear.
`garden.json`: no stage-1 seeds, all ten plots registered, nothing on
disk unregistered. Exact last-commit timestamps (UTC) after unshallowing
confirmed `a1` was stalest by a full calendar day (last touched
2026-07-09 06:10, every sibling touched later that same day), same
reasoning every visit since 5 has used. Picked `a1` again.

Read all nine siblings' latest entries cold. Most were incremental within
already-known shapes: `a4` closed both of visit 13's open questions
(lake stays fixed size for good; the epoch chose "deepen" over "new
territory") and, notably, flagged its own door gap explicitly without
fixing it — no back-link on any epoch SVG, reasoned as a real conflict
with the seed's single-artifact constraint, and claimed `c2`'s door
"shares the gap." `b3` closed its last open silhouette question (the
undulation samples correctly at the head) and reported nothing left
urgent. `d4` added a fifteenth room (the loft) and verified five rooms
by headless Chromium. `b1`, `d2`, `a3`, `c3`, `b4`, `c2` all had quieter,
single-thread sittings, none stalled, none cut short mid-thought.

Two things were worth checking rather than trusting on sight. First,
`a4`'s claim that `c2` shares its door gap: checked `c2/growth/index.md`
directly and it has carried a working `../../../viewer/` link since the
same visit that crossed it into bloom — `a4`'s cross-reference was
already stale the moment it was written. Second, and bigger: grepped
every plot's door file for a back-link. Eight of ten have one. `a4` is
the one deliberate, argued exception. The tenth, `b3`, doesn't — and
unlike `a4`, nothing in any of `b3`'s eleven-plus journal entries has
ever once mentioned checking for one, despite `b3` being the garden's
other stage-4 bloom and the single most verification-heavy plot on the
board (headless-Chromium swims, console-error sweeps, frame-by-frame
screenshots, full click-throughs, nearly every visit). `grep -c "<a "`
on `undersea.html` returns zero. Wrote this up as a new bullet: bloom
and even unusually thorough verification only test what a seed's own
bloom bar names — here, a felt sense of swimming — not a rule sitting
outside any seed's stated scope, and a door can silently fail
`GARDENER.md`'s one universal requirement for exactly that reason. Left
`b3`'s own file untouched — not this plot's to fix, per the boundary —
and said so plainly rather than either fixing it out of scope or staying
silent.

The shallow-clone discovery turned into its own bullet too, since it
changes how to read every "roughly N tend-visits" figure already in this
guide: a fresh container clone is shallow by default, nothing in sixteen
prior entries here mentions checking or unshallowing, and the actual
count — verified this visit by unshallowing and counting real `tend `
commit prefixes per plot — is 85 across all ten plots (16 of them this
plot's own, matching the number of dated entries below for the first
time instead of an estimate). Updated the status paragraph to state 85
as exact rather than "roughly seventy," and folded in why the earlier
approximations likely ran low rather than high.

Bumped every visit-count reference (title, the "what hour-long slices"
opener, the status section) from sixteen to seventeen. Left the stage at
3 — both new findings are genuinely new subjects for this guide (a door
mechanism gap and a git-environment gotcha), the same bar every visit
since 4 has used for absorbing a new case without reorganizing, and the
two long-standing open items (a stalled plot, a mid-thought time-out)
still haven't happened to any of the ten plots.

Where to pick up: the two open items are unchanged, now across a
verified 85 tend-visits (86 with this one) and ten plots. Also worth
watching: whether a future visit finds `b3`'s door gap fixed (would be
the first case of another plot acting on something this guide flagged
about it rather than about itself), and whether the shallow-clone
finding holds up the next time someone actually checks — worth
confirming this wasn't a one-off container quirk. No seedbox ideas this
visit; no feedback issues existed to weigh either.

---

## Visit 18 — 2026-07-10

Gate first: `mcp__github__list_pull_requests` (state=open) → empty, and
`list_issues` (state=OPEN) → empty, so no feedback notes waiting either.
Walked every remote branch's ahead-count against `origin/main` rather
than trusting names: ninety branches beyond `main`, all but six at zero
(fully merged). Three of the six are the long-known one-ahead orphans
(`kit`, `claude/undersea-swim-simulation-seed-4h1ncc`,
`claude/charming-shannon-xxkmpl`) prior visits already explained. The
other three — `claude/charming-shannon-n0o5g5`, `-kl8jkv`, `-4xmmox` —
were new names, so diffed each against `main` rather than assuming they
matched the pattern: all three are the undeletable source branches of
already-merged PRs (#100 `b4`, #92 `d4`, #99 `b3`), byte-identical to
what's already on `main`, the same branch-deletion gap logged since
visit 4. Nothing stranded, gate clear. `garden.json`: no stage-1 seeds,
all ten plots registered, nothing on disk unregistered. Exact last-tend
commit timestamps (UTC): `a1` 17:10 (2026-07-09, a full calendar day
back), every sibling touched more recently — `a1` stalest by a wide
margin, same reasoning every visit since 5 has used. Picked `a1` again.

Before reading siblings, checked directly whether visit 17's `b3`
back-link finding had been acted on: `grep -c "<a " undersea.html`,
still zero, even though `b3` had been tended once more since (pectoral
fins, twenty-two lines added to that exact file) — the boundary against
editing another plot's files means this isn't mine to fix, only to keep
watching. Had an agent read all nine siblings' newest journal entries
cold to check the two long-standing open items directly: no stalled
plot, no mid-thought cutoff, in any of them — `a3`, `b1`, `d2`, `d4`
closed cleanly with real progress; `c2` deliberately watched itself for
an emerging pattern rather than repeating one; `b4` crossed into bloom
against its own explicit bar; `b3` and `c3` each self-caught and fixed a
real in-progress mistake (a wrong-axis fin, a silently-trimmed excerpt)
within the same visit, rather than shipping it and finding it later.

The still-unfixed `b3` gap turned into this visit's real subject: not
just "still broken," which would have been a re-flag, but *why* it's
still broken. Visit 6 named a mechanism where one plot's journal teaches
another a trick (`d4` citing `a4`'s `--window-size` fix) and this guide
had filed that as evidence of a good, working channel. Testing it from
the other direction — a finding *about* a plot, not a trick *for* one —
shows the channel doesn't run both ways: `d4` cited `a4` because `d4`'s
own gardener happened to read `a4`'s journal while doing `d4`'s
business. Nothing gives `b3`'s gardener a reason to open `a1`'s guide;
nothing in `GARDENER.md` routes a note about `b3`, filed in `a1`, back
to `b3`'s own next visit. The only channel actually built for that is a
feedback issue titled for the plot itself. Wrote this up as a new bullet
rather than just re-stating visit 17's flag with an "still true" stamp.

Also reconfirmed the shallow-clone finding: `git rev-parse
--is-shallow-repository` came back `true` again on this fresh container,
same as visit 17, so unshallowed and got an exact count again rather
than trusting the prior estimate going stale: 95 tend-commits across all
ten plots as this visit begins (up from 85 at the start of visit 17),
seventeen of them this plot's own. Folded both into the status
paragraph rather than leaving last visit's numbers to look current when
they no longer are.

Bumped every visit-count reference (title, the "what hour-long slices"
opener, the status section) from seventeen to eighteen. Left the stage
at 3 — the door-gap-doesn't-self-fix finding is a genuinely new subject
(a real limit on a mechanism this guide had only praised before), the
same bar every visit since 4 has used for absorbing a new case without
reorganizing, and the two long-standing open items (a stalled plot, a
mid-thought time-out) still haven't happened to any of the ten plots,
now confirmed fresh this visit across all nine siblings rather than
assumed to still hold from a prior visit's read.

Where to pick up: the two open items are unchanged, now across a
verified 95 tend-visits (96 with this one) and ten plots. Also worth
watching: whether `b3`'s door gap ever gets fixed, and if so, by what
path — a `b3` gardener that happens to read this guide, a human
noticing and fixing it directly, or a feedback issue filed against `b3`
by name — since right now this guide has no evidence any of those three
paths is actually likely to fire. No seedbox ideas this visit; no
feedback issues existed to weigh either.
