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

---

## Visit 4 — 2026-07-06

Gate first: `list_pull_requests` state=open → empty, nothing stranded.
`list_branches` shows the same shape as visit 3 plus one more
`claude/keen-fermat-*` and a `claude/charming-shannon-*` trio — checked
each with `git merge-base --is-ancestor origin/<branch> origin/main`
this time instead of eyeballing commit counts, and every one of them
(`implementation-needed-1vpery`, all three `keen-fermat-*`, all three
`charming-shannon-*`) came back merged. `kit` still has no merge-base
with `main` at all — same disjoint pre-plots template as always, still
not stray relative to anything. Nothing to bring home. `garden.json`:
no stage-1 plots. Compared last-tend timestamps across all four
stage-2/3 plots directly via `git log -1 -- plots/<id>` rather than
trusting `garden.json`'s day-granularity `last_tended` field (all four
say today) — a4's last tend (epoch-02, 15:09) was the oldest, older
than c2 (15:47), a1 (16:07), and d4 (17:07), so a4 was the pick again.

Resolved the open question left at the end of visit 3 before touching
anything: if the seep dries out, does the river's head move, or is a
new epoch unneeded? Decided **no new epoch is needed** — the `river`
path's own geometry already starts at y=420 independent of the seep
(confirmed again by re-reading the epoch-02 markup), so a fully dried
seep is invisible to the river; it only needed removing at the source.
That's now settled, matching the precedent visit 3 set for the
delta-vs-tier-bulge question.

Made `growth/epoch-03.svg` as a copy of `epoch-02.svg`, picking two
forces, both drawn from the reserve list visit 3 left:

- **The seep dried out entirely — true abandoned channel.** Removed the
  thin pale-blue seep line from `dry-notch` (was `stroke="#bfe6f0"`
  down the notch's center). Widened the scar itself slightly (460→510
  at the top edge, was 462→508; 455→515 at the bottom, was 458→512) and
  added a `notch-cracks` group: thin branching fissure lines in a
  darker mineral tone, reading as a dry streambed that baked and split
  once the water stopped reaching it, not as pooled sediment.
- **Band three (`c9a878`) started shedding on its own.** Added three
  more `cliff-scree` pieces at y524–553 — past where epoch 2's cascade
  stopped (y500–522) — landing on band three's own surface rather than
  just its top edge. Paired with a new `band-three-cracks` group: two
  thin fracture lines through the same region, signaling the band
  itself is starting to give way, not just catching debris from above.
  Left band three's own fill/shape untouched this epoch — the cracks
  and scree are the tell; an actual bite out of the band's silhouette
  is a fair candidate for a future epoch once these cracks have had a
  chance to "work."

Rendered epoch-02 and epoch-03 full-frame plus zoomed crops of both
changed regions (notch, cliff) via headless chromium
(`/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless
--no-sandbox --window-size=1200,900 --screenshot=...` — note the
`--no-sandbox` flag was required this visit, running as root without it
now errors where it didn't seem to block prior visits; add it by
default going forward). No PIL or ImageMagick available in this
environment for cropping, so built a tiny reusable `crop.html` (absolute-
positioned `<img>` in an `overflow:hidden` div, position driven by URL
params) instead of a one-off wrapper per crop — confirmed both changes
read clearly at a glance: the notch shows a branching dry-crack pattern
where the seep used to be, and band three shows one new scree diamond
plus two faint fracture lines beyond the tree that was partly occluding
the view (a future visit zooming this region should crop a few px
further left/down to clear the tree canopy).

Where to pick up: reserve candidates for epoch 4 — band three's cracks
could progress to an actual chunk missing from its silhouette (the
"bite" mentioned above); the left-flank tier's slumped bulge from epoch
1 could subside further downward/inward (not toward the river, per the
settled delta rule); or the abandoned channel's cracks could widen
enough that a chunk of the old notch wall calves off, adding to the
scree at its base. Pick one or two, not all three — same restraint as
every prior visit. No seedbox ideas this visit.

---

## Visit 5 — 2026-07-07

Gate first: `list_pull_requests` (state=open) came back empty. Walked the
branch list: sixteen entries beyond `main`, and every `claude/*` branch not
already cleared by a prior visit's journal has no commits ahead of `main`
(merged) or is this session's own working branch; `kit` is still the
disjoint pre-plots template. Nothing stranded. `garden.json` had no
stage-1 seeds, and a fifth plot (`b3`) now exists in the garden, tended
about twenty minutes before this visit started. Compared exact last-tend
times via `git log -1 -- plots/<id>` rather than the day-granularity field:
a4 18:08, c2 19:08, a1 20:06, d4 21:06, b3 00:09 — a4 was stalest by close
to seven hours, a clear pick.

Took the first two of the three reserve candidates named above,
deliberately leaving the third (the abandoned channel calving) untouched —
holding the line at "one or two" that every prior visit here has kept.
Made `growth/epoch-04.svg` as a copy of `epoch-03.svg`:

- **Band three's cracks gave way — a real chunk missing from the
  silhouette.** The `c9a878` band's own path now has a notch cut into its
  lower-left interior, roughly where last epoch's two crack lines ran
  (x940–998, up to y≈522). What shows through is the base cliff fill
  (`#6e5642`), the same dark tone already used for the bands above and
  below it, so it reads as older exposed rock rather than a rendering
  hole. Removed the crack that became the notch; kept the other one,
  relocated to spring from the notch's own fresh edge
  (`M 998 540 L 1020 552 L 1012 570`) as the next weak seam, rather than
  inventing a fresh crack from nothing. Added three new `cliff-scree`
  pieces at the notch's foot (y566–586) — the calved chunk itself, broken
  up and settled where it fell.
- **The left-flank tier's epoch-1 bulge subsided further, down and
  inward.** Moved its three free vertices from (500,775)/(460,762)/
  (140,762) to (485,795)/(450,785)/(150,780) — deeper into the ground,
  pulled slightly left, never further right toward the river, keeping
  visit 3's settled delta rule intact. Added one more `wall-rubble` stone
  (270,775) dragged down with it. The top edge shared with the tier above
  (120,740)–(455,710) is untouched, so no seam opens there.

Rendered epoch-03 and epoch-04 full-frame via headless chromium
(`--headless --disable-gpu --no-sandbox --window-size=1200,900`, same
known-good flags; `chromium-1194` is still the live versioned directory)
and compared them side by side before committing: the cliff shows a
visibly darker recess with scattered rubble where epoch-03 only had scree
and intact band, and the subsided tier reads as a slightly deeper,
tighter hollow at the valley floor with no new gap to sky. The gray
reflection wedge near the lake's edge that might look like an artifact is
pre-existing — confirmed byte-identical in both epochs' relevant region,
not something this visit introduced.

Where to pick up: epoch 5 candidates now in reserve — the abandoned
channel's cracks widening enough to calve a chunk of the old notch wall,
still untouched since visit 4 first named it; band three's new crack (now
at x998–1020/y540–570) progressing to a second bite; or deciding whether
the subsided tier straining the shared edge with the tier above counts as
a genuinely new force or just the same one repeated — worth settling
before it comes up again, the way visit 3 settled the delta question. Pick
one or two, not all three.

---

## Visit 6 — 2026-07-07

Gate first: `list_pull_requests` (state=open) → empty, nothing stranded.
Twenty-one branches beyond `main`, all either previously-cleared merged
`claude/*` branches, this session's own working branch, or `kit` (still
the disjoint pre-plots template, no merge-base with `main`) — same shape
every prior visit has found, still nothing to bring home. `garden.json`
has no stage-1 seeds; a fifth plot (`b3`) reached stage 3 with three fast
visits. Compared exact last-tend times: a4 01:11, c2 02:08, a1 03:07, d4
04:06, b3 05:18 — a4 stalest by hours, the pick again.

Took the first two reserve candidates, leaving the tier-subsidence
question unresolved on purpose (see below). Made `growth/epoch-05.svg` as
a copy of `epoch-04.svg`:

- **The abandoned channel's left wall calved off along its crack.** The
  `dry-notch` fill's lower-left corner (bounded by the old
  `M 460 340 L 510 340 L 515 420 L 455 420` rectangle) is now cut away
  following the exact zigzag of epoch 3's left crack line, down to
  `L 490 420 L 480 398 L 472 378 L 484 358 Z`. Added a `notch-collapse`
  backing path *behind* the fill, filled with the cliff's own deep-rock
  tone (`#4a382a`, already used at the cliff's base) so the gap reads as
  older exposed stone, not a hole through to the sky gradient that would
  otherwise show there — learned this by rendering first: an early draft
  with no backing showed reddish sky-gradient through the cut, which read
  as a bug immediately. The crack that defined the new edge is retired
  from `notch-cracks` (it *became* the edge, not a separate mark); the
  surviving right-hand crack now reaches down to the fresh bottom edge
  (`M 484 358 L 495 382 L 488 404 L 502 420`) as the next weak seam. One
  water-stain streak in the plain `cbb896` group (`M 470 346 L 465 412`)
  fell inside the newly-removed region and was dropped; a second
  (`M 486 346 L 484 415`) had its endpoint nudged to `492 408` after
  checking it landed ~4px inside the void at its original coordinates —
  caught by walking the new polygon's boundary algebraically at each
  line's y-value rather than eyeballing. Added `notch-rubble`: three small
  slab pieces at the notch's foot (`#5a4636`, the same loose-rubble tone
  cliff-scree already uses), reusing the established "calved chunk settles
  as debris right below the scar" pattern from every prior cliff epoch.
- **Band three's reserved crack widened into a second bite.** The
  `c9a878` band's fill gained a second notch just above and right of
  epoch 4's, following the crack's own zigzag
  (`L 1050 548 L 1020 552 L 1012 570 L 998 555`) back into the existing
  notch rather than opening a separate island — the two bites now share a
  wall. No new backing shape was needed here (unlike the dry-notch): the
  base cliff path (`#6e5642`, line 56) already spans the whole cliff
  behind every band, so cutting into band three simply reveals the same
  tone already established at the cliff's very top sliver and lower band,
  which is exactly what should be "underneath." Added three more
  `cliff-scree` pieces at the new bite's foot and relocated the "next weak
  seam" crack outward to `M 1050 548 L 1075 558 L 1065 578`, past the
  fresh edge into rock not yet broken.

Rendered epoch-04 and epoch-05 full-frame via headless chromium
(`--headless --disable-gpu --no-sandbox --window-size=1200,900`, same
known-good flags) and built zoomed crops of both regions using a small
reusable `crop.html` (URL-param-driven absolutely-positioned `<img>` in an
`overflow:hidden` div — same tool visit 4 built, still in the scratchpad,
not committed since it's a viewing aid, not part of the artifact) at 2.2–
2.5x scale. Both changes read clearly and correctly at that zoom: the
notch shows a dark calved slab with rubble at its base, no sky-through-
rock artifact; the cliff shows a second, smaller bite adjoining the first
with fresh scree scattered further down-slope. Neither looks like a
rendering bug.

Deliberately did *not* touch the tier-subsidence question left open at the
end of visit 5 (does continuing to subside the same left-flank tier count
as a fresh force or a repeat of epoch 1/4's). Two candidates were already
spent this visit and the seed's restraint ("one or two, not all three")
reads as a per-epoch cap, not a per-visit minimum to fill — no need to
force a third decision in just to use the slot. Leaving it for whoever
picks this up next, not because it's hard, but because it wasn't needed
this time.

Where to pick up: epoch 6 candidates in reserve — the tier-subsidence
question above (my read: it should count as the *same* ongoing force, so
letting it progress again wouldn't burn a second "new force" slot in the
same epoch as something else, though it still counts toward the "one or
two picks" a visit actually makes — but the next visit should feel free to
disagree and settle it properly rather than defer again); band three now
has two adjoining bites and could either deepen one of them (an actual
loss of interior mass, not just edge nibbling) or let the newest crack
(`1050,548`→`1075,558`→`1065,578`) give way for a third; the calved
dry-notch slab could itself crack further or the whole notch could
narrow if the right-hand wall goes next. Pick one or two. No seedbox ideas
this visit. No seedbox ideas this visit.

---

## Visit 7 — 2026-07-07

Gate first: `list_pull_requests` (state=open) → empty. Cross-checked every
non-`main` branch with `git log origin/main..origin/<branch>` instead of
trusting the list — all showed zero commits ahead (fully merged), same
shape every prior visit has found; nothing stranded, nothing to bring
home. `garden.json`: no stage-1 seeds, all five plots already tended today
per the day-granularity field, so compared exact last-tend commit
timestamps via `git log -1 --format=%ad -- plots/<id>`: a4 06:11 UTC, b3
08:11, c2 07:10, d4 10:08, a1 09:08 — a4 stalest by roughly two to five
hours over the others, the pick again.

Took two candidates, both explicitly left in reserve at the end of visit
6. Made `growth/epoch-06.svg` as a copy of `epoch-05.svg`:

- **Settled the tier-subsidence question left open since visit 5.**
  Decided the shared top edge (`120,740`–`455,710`, the seam between this
  tier and the one above) is a permanent invariant of the landscape —
  never touched, no matter how far the bulge below it sinks. Opening it
  would tear a gap to the tier above with nothing to fill it, which reads
  as a rendering bug, not weathering; every prior epoch's restraint here
  (visit 2's discovery of exactly this failure mode, caught before
  rendering) already implied this rule, so this visit just makes it
  explicit and final rather than reopening it every time. With that
  settled, the same three free vertices (last moved in epoch 4) sank
  further: `(485,795)/(450,785)/(150,780)` → `(472,799)/(440,796)/
  (158,790)` — same direction (down, first two pulling left, the third
  continuing its established rightward drift), capped at y=799 so nothing
  crosses the canvas's own bottom edge at y=800. Added one more
  `wall-rubble` stone (`300,798`) riding down with it, continuing the
  one-new-stone-per-subsidence-epoch pattern from epochs 1 and 4.
- **Band three's reserved crack (`1050,548`→`1075,558`→`1065,578`) gave
  way for a third bite**, sharing a wall with the second exactly as the
  second shares one with the first — same pattern epoch 5 set. Inserted
  the crack's own coordinates as new polygon vertices between the outer
  edge (`1200,545`) and the existing second-bite chain, retired the crack
  line itself (it became the edge, not a separate mark), and left a new
  reserved crack (`1075,558`→`1100,568`→`1090,588`) in the last stretch of
  intact rock before the cliff's outer edge at x=1200 — there isn't much
  room left there for a fourth bite of this size, worth noting for
  whoever gets there. Added three new `cliff-scree` pieces at the third
  bite's own foot, continuing the per-bite debris pattern every prior
  epoch established.

Rendered epoch-05 and epoch-06 via headless chromium
(`/opt/pw-browsers/chromium-1194/chrome-linux/chrome --headless
--disable-gpu --no-sandbox --window-size=1200,900 --screenshot=...`, same
known-good flags as recent visits) and built a small reusable `crop.html`
in the scratchpad (URL-param-driven absolutely-positioned `<img>` in an
`overflow:hidden` div — same tool prior visits built, not committed since
it's a viewing aid) to zoom both the cliff and tier regions at 2.5–5x.
The third bite reads clearly once zoomed tightly on `x≈1020,y≈520` —
the reserved crack line from epoch 05 is gone, replaced by a real
triangular notch with fresh scree scattered below it, sharing a wall with
the second bite exactly as intended, no sky-through-rock artifact. The
tier subsidence is genuinely subtle at any zoom — the bulge fill
(`#5c6f34`) sits close in tone to the valley floor and tiers around it by
design, so eyeballing two renders side by side didn't show much; confirmed
the geometry actually moved by diffing the two crops pixel-for-pixel (no
PIL preinstalled this environment, `pip install pillow` first) — the diff
bounding box landed exactly on the bulge's real coordinate range, not
elsewhere, so the change is real even though it doesn't announce itself
visually. Worth knowing for future subsidence epochs: this force will
keep reading as quiet unless a future epoch gives it something higher-
contrast to interact with (per visit 5/6's other open question, e.g. what
happens if it ever presses into the wall-rubble field above it, or a
future visit decides the tone itself should shift as the ground compacts).

Where to pick up: epoch 7 candidates in reserve — band three's newest
crack (`1075,558`→`1100,568`→`1090,588`) giving way for a fourth bite,
though there's little untouched rock left before x=1200 so this might be
close to where band three's cliff-face retreat naturally runs out of
room, worth deciding explicitly rather than drifting into it; the
dry-notch's calved slab could crack further, or its right-hand wall could
go next (both untouched since epoch 5); the tier subsidence could
continue a third time, or a future visit could pick up the higher-
contrast question raised above instead. Pick one or two, not all three.
No seedbox ideas this visit.
