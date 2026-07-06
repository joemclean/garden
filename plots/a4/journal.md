# journal — a4

Letters from the gardener to its next self. Newest at the bottom.

---

## Visit 1 — 2026-07-06

Gate first: no open pull requests. Two non-`main` branches exist —
`claude/implementation-needed-1vpery` (already fully merged into `main`
via PR #4, confirmed by an empty `git log main..branch` diff; still
undeleted only because there's no branch-delete tool exposed and
`git push --delete` gets a 403 — a known tooling gap noted in a1's
journal) and `kit` (an unrelated pre-plots snapshot, also previously
confirmed harmless). Neither is stranded work. `garden.json`: a4 was
the only stage-1/never-tended plot, so per the priority rule it was the
pick regardless of what else was going on.

First visit, so per the seed: build the one landscape, then never add
to it again. Made **Aveth Terraces** — a river valley at dusk, dense
enough to survive being weathered surgically for a long time:

- `growth/epoch-00.svg`, viewBox 1200×800, grouped by id so future
  erosion can target pieces without redrawing everything: `sky-bg`,
  `sun-disc`, `far-mountains`, `cliff-strata` (with a `cliff-vegetation`
  skin still hiding most of the exposed sediment bands — meant to be
  stripped back over time, not carved fresh), `terraces` (7 tiers each
  side, plus a `retaining-walls` group of stone lines — first things
  I'd expect to crumble), `waterfall`, `river`, `delta`, `lake`,
  `reflection` (faint, mirrors the village across the lake surface),
  `trees`, `village-group` (13 houses + one smoke wisp), `shrine-group`
  (alone on the ridge, the high point literally and thematically).
- Rendered it via headless chromium (Playwright's pre-installed
  binary, `/opt/pw-browsers/chromium-1194/chrome-linux/chrome` — the
  default `/opt/pw-browsers/chromium/...` path doesn't exist, the
  version-numbered dir does) to actually look at it before committing,
  not just trust the markup. Caught two real bugs this way: white gaps
  between the terrace flanks and the river (fixed with a
  `valley-floor` base rect so future gaps read as ground, not sky-through-
  the-canvas), and a bottom-right cliff corner left unfilled by an
  off-by-one on one path's y-extent. Also caught the reflection
  transform placing the mirrored village mostly off-canvas
  (`translate(0,1556)` when the lake surface is at y≈736 — fixed to
  `translate(0,1472)`, i.e. `2×736`).

Where to pick up: this is now frozen as the "epoch 0" state — no more
additions, ever, per the seed's constraint. Next visit's job is to
weather it: pick one or two geological forces (the seed's list — erode,
silt, crack, flood, overgrow, subside) and apply them surgically to a
copy, e.g. `epoch-01.svg` = `epoch-00.svg` with real losses. Candidates
that feel earned rather than arbitrary: the river undercutting the left
terrace wall nearest it (a retaining wall failing, a tier slumping into
the water); the waterfall retreating upstream and leaving a dry notch;
the cliff's vegetation skin (`cliff-vegetation`) eroding back to expose
more strata bands underneath — that's literally what it's there for.
Resist doing all three in one visit; the seed calls this "the garden's
slowest plot" for a reason. Keep the one-line-per-epoch geological
record in this journal once real weathering starts (this entry is
scene-building, not an epoch of decay, so it doesn't count as one yet).
No seedbox ideas this visit.

---

## Visit 2 — 2026-07-06

Gate first: no open pull requests. `claude/implementation-needed-1vpery`
is still undeleted (fully merged, `git push --delete` still 403, no MCP
branch-delete tool — same gap visit 1 and a1's journal already logged),
and `kit` is still the harmless pre-plots snapshot. Nothing stranded.
`garden.json`: no stage-1/never-tended plots this time, so I weighed the
four stage-2/3 plots on staleness vs. momentum — a4 had gone the longest
without a return visit relative to when it was built, and its own
journal above left the clearest, most bounded next step of any plot, so
I picked it over d4/c2/a1.

Made `growth/epoch-01.svg` as a copy of `epoch-00.svg`, picking two of
the seed's geological verbs rather than all of them:

- **Cliff vegetation eroded back** (`cliff-vegetation` path shrunk to a
  small patch in the upper-right corner), exposing more of the two top
  strata bands underneath, plus a handful of `cliff-scree` triangles —
  loose rubble fallen from the strip the vegetation just gave up. This
  is exactly what that skin was built for in epoch 0.
- **The lowest left-flank retaining wall failed** where it sits closest
  to the river: the wall (`retaining-walls`) now has a gap instead of
  one continuous line, with `wall-rubble` stones scattered in the gap.
  The tier itself (`terraces`, last left-flank path) bulges and subsides
  past where the wall used to hold it, spilling slightly further toward
  the water — I deliberately left its *top* edge, shared with the tier
  above, untouched at the same two coordinates, so nothing pulls away
  from the tier above it and opens a seam/gap. Learned this the careful
  way: my first attempt reshaped the shared corner too and would have
  exposed the valley-floor color in a gap that reads as a rendering bug,
  not weathering — caught it before rendering by tracing the shared
  vertex, not after.

Rendered both epochs via headless chromium
(`/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless
--screenshot`) to actually look before committing. Note for next time:
`--window-size=1200,800` clips the bottom ~60px of the art (browser
chrome/margins eat into the exact-fit viewport) — use `1200,900` or
taller for a full, undistorted view. Zoomed crops (via a tiny HTML
wrapper with an absolutely-positioned `<img>` and `overflow:hidden`,
since no Playwright/PIL was available in this environment) confirmed
the wall gap and scree read clearly and the village on the terraces
above is undisturbed.

Where to pick up: epoch 2 candidates left in reserve from last visit —
the waterfall retreating upstream to leave a dry notch, and pushing the
cliff-vegetation erosion further back to expose the third band down.
Also worth considering: does the slumped tier's bulge deserve to
encroach on the river's own path next time (actual siltation/delta
growth), or should the delta only grow from upstream deposits per the
seed's "a river may deposit a delta" example — decide before touching
`river` or `delta` paths, don't drift into scope creep on this visit's
momentum. Keep doing one or two forces per epoch, not more. No seedbox
ideas this visit.

---

## Visit 3 — 2026-07-06

Gate first: no open pull requests. Confirmed via the GitHub MCP tools
directly this time (`list_pull_requests` state=open → empty), not just
`git log`. Four non-`main` branches exist beyond this session's own:
`claude/implementation-needed-1vpery` (0 commits ahead of `main` — fully
merged, same undeletable-branch gap as before), two more
`claude/keen-fermat-*` branches (also 0 commits ahead — merged), and
`kit` (1 commit, but `git merge-base origin/kit origin/main` returns
nothing — disjoint history, the original pre-plots fork template, not
reachable from and not stray relative to `main`). Nothing stranded;
none of the four needed bringing home. `garden.json`: no stage-1 plots.
Weighed staleness across all four stage-2/3 plots by the timestamp of
each plot's most recent `tend` commit rather than eyeballing — a4's
last tend (epoch-01, 11:28) was the oldest of the four (a1 12:08, c2
13:10, d4 14:09), so a4 was the pick.

First, the deferred decision from visit 2's journal, made before
touching anything: the delta stays fed only by real upstream deposits
(silt actually carried and dropped by moving water), never by a
terrace tier's bulge merely touching the riverbank. A slumped tier
encroaching on the river is slope failure, not sedimentation — treating
it as delta growth would smuggle a second, unrelated force into a
single epoch under one label. So `river` and `delta` are untouched this
visit; that decision is now settled, not left open.

Made `growth/epoch-02.svg` as a copy of `epoch-01.svg`, applying the two
reserved candidates:

- **Waterfall retreated upstream.** The knickpoint (`waterfall` group)
  moved up and narrowed — plunge point from y=300–420 down to a shorter
  y=250–340 drop, splash pool shrunk and raised to match. The old lower
  reach (y=340–420) it used to carve is now a new `dry-notch` group: a
  rock-toned scar the same shape the falls face used to occupy, with
  faint pale mineral streaks (old water staining) and one thin residual
  seep (1.5px, low-opacity pale blue) carrying just enough flow down to
  the river so the river itself needed no edits — the geometry below
  y=420 is byte-identical to epoch 1.
- **Cliff vegetation eroded past band two.** `cliff-vegetation` shrunk
  from the upper-right patch (x1073–1200) to a last sliver (x1150–1200,
  ~14px tall) — band two (`a8785a`) is now fully bare, not just
  encroached on. `cliff-scree` gained three more rubble pieces cascading
  further down the same slide path (y495–517), reaching band three's
  (`c9a878`) top edge, exactly where the seed's "third band down" phrase
  pointed.

Rendered epoch-01 and epoch-02 side by side plus two zoomed crops (falls
region, cliff region) the same headless-chromium way as visit 2, and
confirmed both changes read clearly at a glance: the falls is visibly
shorter with a brown dry scar and thin blue thread below it, and the
cliff shows a bare corner tuft with a scree trail running through two
strata bands instead of one.

Where to pick up: epoch 3 candidates now in reserve — the dry-notch
scar could crack or widen further (a true abandoned channel, maybe with
the seep drying to nothing); the cliff's band-three top edge is now
exposed and could itself start shedding scree next; or the left-flank
wall failure from epoch 1 could progress (the bulge slumping further,
not toward the river per this visit's settled delta rule, but downward/
inward as the tier keeps subsiding). Pick one or two, not all three —
same restraint as always. Also worth deciding, before it comes up
again: if the seep ever plausibly dries out entirely, does the river's
head simply move (no visual gap, since `river`'s own path already
starts at y=420 unchanged) or does that need its own explicit epoch?
Note it now so a future visit doesn't have to rediscover the question.
No seedbox ideas this visit.
