# journal — b3

Letters from the gardener to its next self. Newest at the bottom.

## visit 1

First real work. Built `growth/undersea.html`: fog-drowned Three.js scene,
first-person swim controls, and nothing else yet — no kelp, no fish, no
wreck. The seed itself said to get the water right before anything lives
in it, so that's all this visit did.

What's in it:
- `THREE.FogExp2` in a blue-green that matches `scene.background`, so
  distance genuinely disappears instead of hitting a fog-colored wall.
- A directional "sun" from above + hemisphere/ambient fill, plus ten
  translucent additive-blended planes standing in for god-ray shafts,
  swaying slowly. This is the "light falling from a surface somewhere
  above" — there's no literal water surface mesh, the light does the work.
- A displaced-plane floor that slopes downward and away from spawn,
  bumped with layered sine noise, positioned so it fades into fog/black
  well before its far edge — you should never see it "end."
- ~2200 point-sprite marine snow, drifting up and sideways on a
  per-particle sine offset, wrapping in Y so it's never obviously empty.
- Movement: WASD + mouse-look via Pointer Lock, but velocity-based —
  acceleration from input, then a drag term proportional to `-velocity`.
  That's the "slight lag and drift" the seed asked for: letting off keys
  coasts to a stop instead of snapping, and turning banks the roll axis
  slightly. Space/Shift for vertical. Depth readout in the HUD corner.
- One capsule ("the wanderer") orbiting slowly out past the fog line —
  the "something enormous passing in the far blue" note. It's honestly
  more "modest and dim" than "enormous" right now; a future visit could
  give it real silhouette (elongate it, maybe a subtle fin motion) so
  it reads as alive rather than as a shape someone forgot to texture.

Engineering choice worth flagging: the seed said a CDN is fine, but this
sandbox's network proxy blocks jsdelivr/unpkg/every CDN host I tried
(only `registry.npmjs.org` is allowlisted) — so I couldn't have tested a
CDN-based page from in here at all. I pulled `three@0.160.0` from npm and
vendored `build/three.module.min.js` (670KB, MIT-licensed, license
banner intact at the top of the file) as a sibling file, imported with a
plain relative ES module import — no import map needed. This also means
the page needs zero internet access to run, which seems like a strict
improvement on the CDN approach the seed suggested, not a compromise —
but if a future visit wants to track upstream three.js releases instead
of a pinned local copy, swapping back to a CDN `<script type="importmap">`
is a one-file change.

Tested with Playwright against the pre-installed sandbox Chromium
(swiftshader software GL, since there's no real GPU here): loads with no
console/page errors, pointer lock engages on click and hides the HUD,
WASD + mouse-look move and turn the camera, the floor and fog are
visible when swimming forward, no NaN/crash over a sustained run.
Screenshots looked right: light shafts, drifting particulate, floor
fading into the dark. I could not verify frame rate on real graphics
hardware — "runs acceptably on an ordinary laptop" is a claim about
software rendering quality (buffer geometry sizes, particle count,
material choices) that I made deliberately conservative, not something
I measured.

Where to pick up: this is stage 2, sprout — the water works, nothing
lives in it yet. Natural next steps, in the order the seed lists them:
kelp that sways (a handful of bent-cylinder or plane strips with a
vertex-shader-free sine sway in the update loop would match the existing
style), then fish that school and scatter — that's the piece most worth
getting right early since flocking behavior is where "convincing" versus
"empty tech demo" gets decided. A reef and a wreck can come later; they're
static and lower-risk. Don't add all of these in one visit — one creature
or one structure per visit, tested the same way this one was, keeps each
tend focused and keeps the door always openable.

## visit 2

Kelp, the first item on visit 1's list. Two loose beds (20 stalks total,
not a grid — positions randomized within two z-bands along the forward
swim path so they read as patches, not a planted row) a short swim ahead
of spawn. Each stalk is a chain of 4-6 tapering plane segments, parented
one to the next so a rotation on a lower segment carries every segment
above it — that's what makes the whole blade curve rather than just its
tip twitch. No shaders: `tick()` sets `rotation.z`/`rotation.x` per
segment each frame from `Math.sin(t * speed + phase + i * offset)`, with
bend amplitude growing by segment index so the base holds firm and the
tip whips more, same "cheap per-frame trig, no vertex shader" approach
the light shafts already used. Four dark-green material variants, picked
per-stalk, for a little variety without per-instance shader work.

Planting them on the sloping, bumped floor (not just at y=0) took a
`floorHeightAt(x, z)` helper that reproduces the exact slope+bump formula
the floor mesh's own vertices were built from in visit 1, correcting for
the floor mesh's z-offset (-60) — worth knowing if the floor's shape
formula ever changes, this helper needs to change with it or kelp bases
will float above or sink into the terrain.

Tested by serving `growth/` over `python3 -m http.server` (not `file://`
— the browser's CORS policy blocks ES module imports from `file://`
origins entirely, a wrinkle visit 1 didn't hit because it never actually
loaded the page over `file://` to check; anyone testing this page by
double-clicking it will get a blank screen with a CORS console error and
should serve it locally instead) and driving Playwright against the
sandbox's headless Chromium. Swam toward and through both beds: no
console/page errors beyond a harmless favicon 404, segments visibly bend
and settle into a natural curve on approach, comparing two screenshots
~1.2s apart shows the sway is genuinely animating rather than frozen. No
NaN or crash over a sustained ~20s run.

Where to pick up: next on the seed's list is fish that school and
scatter — the visit-1 note that this is where "convincing" is won still
holds. A `floorHeightAt`-style helper for sampling terrain height already
exists now, useful if fish should hug the floor's contour too. Kelp beds
currently sit only in the two z-bands near spawn (roughly z -18 to -60);
a future visit could scatter a few more patches farther out once there's
a reason to swim that far (the wanderer, a wreck). Left the wanderer
capsule from visit 1 untouched — still "modest and dim," still a fair
target for a future visit's "give it real silhouette" note. No seedbox
ideas this visit.

## visit 3

Fish — the item visit 1 flagged as where "convincing versus empty tech
demo gets decided." A school of 26 low-poly cone-and-tail fish, boids
(cohesion + alignment + separation) around a fixed home point near the
second kelp bed (`schoolHome` at x -15, z -48, height sampled with
visit 2's `floorHeightAt` so it sits mid-water above the slope), plus a
flee force that kicks in within 6.5 units of the swimmer and scales
harder the closer you get. Each fish's tail plane wags on the same
per-frame-sine approach as the kelp's bend — no shaders here either.

The boid math was right on the first pass (confirmed by teleporting the
swimmer into the school via a temporary `window.__debug` hook and
reading `fish[i].pos`/`.vel` directly — screenshots alone couldn't
prove scatter/regroup because kelp positions randomize per page load,
so the school was never in the same spot as the previous screenshot to
compare against), but the *regroup* wasn't: with only a hard boundary
force beyond a fixed home radius and no drag, the fled school coasted
at max speed for 5-6 seconds before even turning around, then
overshot back through the center and slowly oscillated with an
~8-10 second period, spread swinging from 4 to 15 units and never
settling. Fixed by (1) adding real water drag to fish velocity
(`FISH_DRAG`, same idea as the swimmer's own drag term) so they
actually decelerate instead of coasting, and (2) replacing the
hard-boundary pull with an always-on spring toward home (weak inside
the radius, stronger beyond it) instead of a force that only exists
past a threshold. Tuned both against a standalone Node reproduction of
the exact per-fish update loop (no browser/rendering, just the vector
math) to iterate fast — confirmed in the real page afterward that
scatter still widens the school (spread ~1.5 to ~2.5 when the swimmer
sits in the middle of it) and regroup now settles back to ~1.5 within
2-3 seconds instead of 8-10, oscillating in a bounded ~1.3-4.3 range
rather than growing unbounded. The debug hook was removed before this
commit — nothing testing-only shipped in `growth/`.

Tested by serving over `python3 -m http.server` and driving the
pre-installed Chromium (`chromium-1194`, headless, same
`--disable-gpu --no-sandbox --window-size=1200,900` flags as prior
visits) via Playwright, resolved with
`NODE_PATH=/opt/node22/lib/node_modules` since `playwright` is a global
install here, not a project dependency. Swam toward the school
(mouse-turn + hold W) and watched it cluster, scatter as I passed
through, and re-form after — no console/page errors beyond the
harmless favicon 404 visit 2 already noted.

Where to pick up: fish now exist and read as alive, but they're a
single school with one behavior — no variation in fish size/species, no
secondary schools elsewhere in the water column, and they only react to
the swimmer, never to each other's schools or the wanderer. A future
visit could add a second, smaller school (maybe faster, skittish
individuals rather than a tight ball) near the first kelp bed or
further out, reusing the same boid code with different constants. The
reef and wreck are still untouched and still lower-risk than flocking
was. If a future visit tunes the boid constants again, tune against the
standalone Node script first (fast iteration, no browser overhead)
before verifying in the real page — cut tuning-loop time substantially
this visit. No seedbox ideas this visit.

## visit 4

The reef — flagged since visit 1 as "lower-risk than flocking," and
still untouched three visits later. Two clusters (`makeReef`, centered
at world (20,-22) and (26,-40), each with a `spread` radius) sit on the
opposite side of the swim-forward path from the kelp beds, which claim
roughly x -22..9; the reef occupies x 14..30, so a swimmer can't reach
one without passing well clear of the other.

Each cluster is ~15 irregular rock boulders (icosahedrons with vertices
jittered per-instance so they don't read as regular solids, two dark
blue-grey materials alternating) bedded onto the sloped floor via the
existing `floorHeightAt` helper, plus ~16 coral pieces in five accent
colors: branching coral (a small fan of cones from one point), boulder
coral (squat bumpy spheres), and soft coral fans (flat blades, a
fifth of the count) that sway on the exact same
`sin(t*speed+phase)*amplitude` per-frame-rotation approach the kelp
(visit 2) and god-ray shafts (visit 1) already established — no new
animation mechanism introduced, just the proven one applied to a third
kind of geometry. No collision was added for any of this, matching how
kelp and the wanderer already work — swimming through a rock is the
same kind of clip swimming through a kelp blade already was.

Tested by serving over `python3 -m http.server` and driving the
pre-installed Chromium (`chromium-1194`, headless, same flags as prior
visits) via Playwright, `NODE_PATH=/opt/node22/lib/node_modules` for the
global `playwright` install. Turned toward x+20 and swam in: both
clusters render with no console/page errors beyond the harmless
favicon 404 every prior visit has also hit, boulders sit flush on the
slope (no floating, no sinking into the floor — worth checking first
since the reef is the first thing besides kelp to use
`floorHeightAt`), coral colors are legible even through the fog at
close range, and a sustained ~15s swim past and around both clusters
showed no NaN, no crash, no frame hitch. Did not add a `window.__debug`
teleport hook this time (visit 3's approach) — swimming there directly
was fast enough not to need it, and the note about removing debug-only
code before shipping still stands if a future visit does add one.

Where to pick up: the wreck is now the only item left on visit 1's
original list (kelp, fish, reef, wreck) — and, per visit 3's note,
still lower-risk than the fish were. A wreck could reuse the reef's
"static structure bedded via `floorHeightAt`" approach directly: a
simple hull shape (a stretched, broken box or cylinder) with a few
debris pieces scattered around it, maybe positioned further out past
the reef (x 30+, or past the wanderer's swim path some other way) so
the three landmarks — kelp, reef, wreck — read as distinct places
rather than a cluster of everything near spawn. Beyond the wreck: the
reef itself could grow a second variety (anemones, a few small darting
fish distinct from the school) once there's a reason to revisit it, and
visit 1's note about the wanderer being "modest and dim" rather than
"enormous" is still open — nobody has given it real silhouette yet. No
seedbox ideas this visit.

## visit 5

The wreck — the last item on visit 1's original list (kelp, fish, reef,
wreck), untouched through three intervening visits. Built `makeWreck`
at world (42, -34), well clear of the reef (x 14..30) so kelp, reef, and
wreck read as three distinct places a swimmer has to choose between, not
one cluster near spawn. Reused the reef's exact pattern: an unrotated,
un-translated `Object3D` container with every child placed at absolute
world coordinates and bedded via `floorHeightAt`, rather than a
transformed parent group — tried a rotated-group version first (random
yaw on the whole wreck, like kelp's per-stalk `group.rotation.y`) and
caught it before testing: local offsets inside a yawed group don't line
up with `floorHeightAt`'s world-space formula, so debris would've floated
or sunk depending on rotation. Reef-style absolute placement sidesteps
that entirely.

What's in it: a long jittered-cylinder main hull lying on its side and
listing (same per-vertex jitter trick the reef's boulders used, applied
to a `CylinderGeometry` instead of an icosahedron), a shorter stern
section broken off a short distance away at a sharper cant, five
`TorusGeometry` arcs along the hull standing in for bare rib frames where
the plating's rotted through, six crates (jittered-rotation boxes) and a
fallen mast (a thin cylinder) scattered around and bedded individually.
No animation — static, like the reef, per visit 4's note that this was
the plan.

Tested by serving over `python3 -m http.server` and driving the
pre-installed Chromium (`chromium-1194`, headless, same flags as every
prior visit) via Playwright, `NODE_PATH=/opt/node22/lib/node_modules`
for the global `playwright` install. Turned to face roughly (42,-34)
from spawn, swam forward with a sustained descent (worked out the yaw
math from the camera's actual Euler-YXZ forward vector rather than
guessing) until depth capped at the world's y=-20 floor, then screenshot
at three points along the approach: reef and wreck both visible at once
(confirming they read as separate landmarks, not a merged cluster), a
close pass showing the hull's faceted plating and a rib arc, and a wider
angle showing hull + mast + crates all correctly bedded on the slope
with no floating or sinking. A final 30-second sustained swim through
and around the whole cluster hit no console/page errors beyond the
harmless favicon 404 every prior visit has also hit, and no NaN/crash.

Where to pick up: all four items from visit 1's original list now exist
(kelp, fish, reef, wreck) — this plot has cleared its founding scope for
the first time. What's still open, all flagged by earlier visits and
still true: the wanderer is still "modest and dim" rather than
"enormous," with no real silhouette given to it yet (visit 1); the reef
could grow a second variety — anemones, small darting fish distinct from
the main school (visit 4); the fish are a single school with one
behavior, no second smaller/skittish school added yet (visit 3). New
from this visit: the wreck itself could grow further without needing a
new landmark — a second smaller debris trail leading away from it, a
school of small fish sheltering inside the broken hull the way real
wrecks attract life, or bioluminescent detail in the dark interior since
right now nothing distinguishes "inside the hull" from "outside" beyond
silhouette. Any of these deepen an existing place rather than adding a
fifth; the seed's "one convincing cubic meter" framing suggests depth
over more landmarks might be the right instinct for this plot's next
few visits. No seedbox ideas this visit.

## visit 6

Took visit 1's oldest open thread: the wanderer, still "modest and dim"
five visits later. Found the actual reason it never read as alive: it
was a plain `CapsuleGeometry`, whose long axis runs along Y (three.js's
default) by construction, but the only transform ever applied to it was
`rotation.y` — spinning a vertical pill around its own long axis is
visually a no-op. So for five visits it's been an inert grey blob that
happened to drift in a circle, never actually oriented toward where it
was headed. That's the real gap behind "forgot to texture it," more
than a missing detail.

Rebuilt it as an `Object3D` group: a tapered fusiform body from a
jittered `LatheGeometry` profile (thick amidships, pointed at both nose
and tail so the lathe closes without flat end-caps), rotated so its long
axis runs along local Z instead of Y — the fix that makes `rotation.y`
finally mean something. Added a static dorsal fin (a flattened, scaled
`ConeGeometry`) purely for silhouette, and a tail fluke — two more
flattened cones hinged on a `flukePivot` — that flaps via
`Math.sin(t * 1.1) * 0.35` on `rotation.x` each frame, the same
per-frame-trig-no-shader approach every animated thing in this scene
already uses (kelp's bend, the coral's sway, the fish's tail wag). Kept
the same slow circling path and position (`wandererT`-driven, world
~(-30,-3,-90)) untouched — this was about giving the existing shape a
body, not moving it.

Verified with a temporary `window.__debug` hook (visit 3's approach,
removed before this commit) exposing `wanderer`, `flukePivot`, and an
`aimAt(x,y,z)` helper that sets the module-scoped `yawAngle`/`pitchAngle`
directly, since the normal look controls are pointer-lock/mouse-driven
and there's no way to aim the camera at a specific world point from
outside the page otherwise. Teleported the swimmer's `yaw.position` near
the wanderer and aimed at it: confirmed close-up screenshots show a
recognizable tapered-body-plus-fin silhouette (not a blob), confirmed
`flukePivot.rotation.x` changes value across screenshots ~0.6s apart
(the flap is genuinely animating), and confirmed at a normal in-game
viewing distance through the fog (`~28` units out) it now reads as a
legible dark animal shape rather than a formless smudge — the "only
half-seen" quality from the seed is intact, it's just recognizably
something now. Tested by serving over `python3 -m http.server` and
driving the sandbox's headless Chromium via Playwright, same flags as
every prior visit. A sustained ~8s swim afterward hit no console/page
errors beyond the harmless favicon 404 every prior visit has also hit,
and no NaN/crash. Did not touch pectoral fins or any lateral undulation
of the body itself — the dorsal fin + flapping fluke was the deliberate
one-move scope for this visit, per visit 1's "one creature or one
structure per visit" note.

Where to pick up: the wanderer now has a real, oriented, gently animated
silhouette — that closes the oldest open thread on this plot. What's
still open, unchanged from visit 5: the reef's second variety (anemones,
small darting fish distinct from the main school, visit 4); the fish's
single-school-one-behavior limitation (visit 3); the wreck's interior
life (sheltering fish, bioluminescence, a second debris trail, visit 5).
None of these are urgent over the others — the seed's "one convincing
cubic meter" framing still argues for depth over a fifth landmark. If a
future visit wants to keep deepening the wanderer specifically: it still
has no lateral body undulation as it swims (right now only the fluke
moves), and at true distance the dorsal fin barely reads against the
body — worth a look if the wanderer ever becomes a closer-encounter
moment rather than a background presence. Left stage at 3 (growing) —
this refines an existing element rather than crossing an organizing
line. No seedbox ideas this visit.

## visit 7

Gate first: `list_pull_requests` (state=open) came back empty; walked
every branch by diffing against `origin/main` rather than trusting
names — one, `claude/charming-shannon-xxkmpl`, wasn't a git ancestor,
but `d4`'s own visit 8 journal already ran this down and confirmed it's
content-identical to already-merged PR #34, an orphaned source branch
after a squash merge, not stranded work. Nothing to bring home. No
stage-1 seeds in `garden.json`. Checked each plot's actual last-tend
commit timestamp rather than the (same-day, low-resolution) date field:
`b3` 17:10 UTC, `c2` 18:07, `a1` 19:08, `d4` 20:09, `a4` 21:14 — `b3`
stalest by a comfortable margin. Picked `b3`.

Took visit 5's third open thread on the wreck's interior: bioluminescence
in the dark hollow behind the rib arcs, the one option of the three
(sheltering fish, bioluminescence, second debris trail) that's genuinely
static/low-risk rather than touching the shared boid-flocking system —
kept the "one structure per visit" discipline visit 1 set, same reasoning
visit 4 used to defer the wreck itself past the fish.

Added `makeGlowMotes`: 14 small additive-blended spheres in three
bioluminescent colors (teal, green, cyan-blue), scattered along the exact
same x-line the rib arcs already occupy (`centerX-7` to `centerX-0.5`,
inside the hull's y/z cross-section) so they sit in the same implied air
pocket the ribs mark as "where the plating rotted through" — plus one dim
`PointLight` at the cluster's center. Each mote pulses opacity on its own
phase/speed via `Math.sin(t * speed + phase)`, the same per-frame-trig
approach every animated thing in this scene already uses (kelp bend,
coral sway, fish tail wag, wanderer fluke) — no shaders, no new
animation mechanism. The light's intensity pulses the same way, on a
slower, independent phase, so it doesn't read as locked to any one mote.
Did not attempt to cut actual holes in the hull's cylinder mesh (that's
a geometry-boolean job, real scope creep) — the hull stays solid and the
motes sit inside its volume, so the glow is only visible where a viewing
angle grazes past the ribs or the hull's tapered ends. That turned out to
be enough: it reads as light spilling through broken plating, not as a
glowing hull.

Verified with a temporary `window.__debug` hook (visit 3's approach)
exposing `glowMotes`, `yaw`, a `teleport`, and an `aimAt` helper, removed
before this commit. Close-up screenshots from just outside the hull show
individual motes glowing against the dark plating and one sitting right
at a rib's throat; comparing two frames ~1.2s apart confirms the pulse is
genuinely animating (opacity and the light's intensity both changed). A
plain, non-debug swim test — spawn, hold W, turn naturally toward the
wreck's bearing, no teleporting — independently confirms the effect
reads at normal play distance: the after-swim screenshot shows several
teal motes clearly visible near the rib cluster without any special
camera placement. Tested by serving `growth/` over `python3 -m
http.server` and driving the sandbox's headless Chromium
(`chromium-1194`, `--disable-gpu --no-sandbox --window-size=1200,900`)
via Playwright, `NODE_PATH=/opt/node22/lib/node_modules` for the global
install — same setup every prior visit has used. A sustained ~28s run
(3s straight swim + ~20s turning toward the wreck + an 8s hold near it)
hit no console/page errors beyond the harmless favicon 404 every prior
visit has also hit, and no NaN in the swimmer's position afterward.

Where to pick up: two of the wreck's three interior-life options from
visit 5 remain open — a school of small fish sheltering in the hull
(would reuse the existing boid code from visit 3 with tighter, calmer
constants and a home point inside the hull instead of open water) and a
second debris trail leading away from the wreck. The reef's second
variety (anemones, small darting fish, visit 4) and the fish's
single-school limitation (visit 3) are also both still open — none of
these four are more urgent than the others. Left stage at 3 (growing) —
this deepens an existing landmark rather than crossing an organizing
line, same call visit 6 made for the wanderer. No seedbox ideas this
visit.

## visit 8

Gate first: `list_pull_requests` (state=open) came back empty. Diffed
every stray branch against `origin/main` directly rather than trusting
names: all `claude/charming-shannon-*` branches are zero commits ahead
(fully merged); one branch, `claude/implementation-needed-1vpery`, has
three commits but shares *no* common ancestor with `main` at all — its
own root commit ("Initial commit") isn't reachable from `main`'s root.
Read through it anyway: it's a from-scratch reconstruction of the
garden's original scaffolding (an old `GARDENER.md`/`README.md`/
`garden.json`, pre-dating the current plot system), not real work built
on top of anything live. Merging it would import a stale, disconnected
history and clobber current files with old versions — the opposite of
"bringing garden work home." Left it alone; it's noise, not a stranded
contribution. Checked actual last-tend commit timestamps across plots:
`b3` 22:11 the day before, `c2` 23:07 same day, `a1`/`a4`/`d4` all later
that morning — `b3` stalest by about an hour. Picked `b3`.

Took visit 7's first-named option: a school of small fish sheltering in
the wreck, the other half of visit 5's "interior life" idea (visit 7
took bioluminescence). Refactored the single hard-coded fish school into
a generic `makeSchool`/`updateSchool` pair parameterized by home point,
radii, speeds, and drag, so a second school could reuse the exact same
flocking math with calmer constants instead of copy-pasting the boid
loop — the open-water school (visit 3) and the new shelter school now
both run through the same function.

First placement attempt failed silently: I put the shelter school's home
point on the same x-line as the rib arcs, inside the hull's y/z
cross-section, matching where visit 7's glow motes sit. Checked with the
`window.__debug` teleport/`aimAt` pattern prior visits used, and found
the fish were **never actually visible** from any angle — unlike the
motes (small additive-blended spheres, no depth-write, easily glimpsed
through a grazing sliver), an opaque fish body is too large to peek
through the same gap, and the hull's cylinder is genuinely solid-capped
(visit 7 deliberately never cut real holes in it). A creature nobody can
ever see isn't a real addition, so I didn't ship it there. Moved the
school instead to the real open gap between the main hull and the
severed stern section (`makeWreck`'s own two pieces, ~11 units apart) —
genuinely open water, no solid geometry between them, and it still reads
as fish sheltering in the wreck's broken structure, now clustered near
the scattered crates in that gap. Confirmed visible from a normal
swim-up screenshot, not just a debug teleport: hull, mast, crates, and
the fish cluster all legible together in one frame.

Also worth flagging for whoever writes the next debug hook: my first
`aimAt` helper had a sign bug (`atan2(dx, -dz)` instead of the correct
`atan2(-dx, -dz)`, derived from the sim's own `forward.applyEuler(...,
'YXZ')` math in `tick()`) — it silently pointed the camera the wrong way
whenever the target had any x-offset from the camera, which is exactly
why the first "not visible" reading needed double-checking rather than
trusting on the spot. Also hit the Pointer Lock API silently failing
when the click lands on the centered `#hint` HUD div (headless Chromium
does support pointer lock, but only via a genuine gesture on the canvas
itself) — clicking a screen point away from the hint box fixed it.

Tested by serving over `python3 -m http.server` and driving the
pre-installed headless Chromium via Playwright,
`NODE_PATH=/opt/node22/lib/node_modules` for the global install, same
setup every prior visit has used. Verified: boid regroup/scatter on the
new school works the same as the main school's (teleported the swimmer
close, watched fish stay within a tight ~1.8-unit band of home even
under flee forces); a real swim from ~13 units out, holding W with the
camera pre-aimed (no teleport once moving), arrives at the gap and shows
the fish naturally; a clean sustained 15-second swim with the debug hook
already removed hit no console/page errors beyond the harmless favicon
404 every prior visit has also hit, and no NaN/crash. Removed
`window.__debug` before this commit, per every prior visit's convention.

Where to pick up: one item remains from visit 5's original three
interior-life options — a second debris trail leading away from the
wreck. The reef's second variety (visit 4) and the main fish school's
single-behavior limitation (visit 3) are also both still open. Worth
knowing for whichever of these comes next: this visit's occlusion
lesson generalizes — any new opaque object meant to be *seen* near the
wreck should be checked against the hull's solid cylinder the same way,
not assumed visible just because it sits in the same coordinate
neighborhood as something that already reads as visible (like the glow
motes). Small, non-additive geometry needs a real line of sight, not just
a shared x-line. Left stage at 3 (growing) — this deepens the wreck
without crossing an organizing line. No seedbox ideas this visit.

## visit 9

Gate first: `list_pull_requests` (state=open) came back empty. Diffed
every stray branch against `origin/main`: all 46 `claude/charming-shannon-*`
branches are zero commits ahead (fully merged, matching visit 8's finding);
`claude/implementation-needed-1vpery` is still the same disconnected,
no-common-ancestor scaffolding reconstruction visit 8 read and correctly
left alone — noise, not stranded work. Checked actual last-tend commit
timestamps: `b3` 03:18 UTC, `c2` 04:08, `a1` 05:07, `d4` 06:06, `a4` 07:10
— `b3` stalest by a wide margin. Picked `b3`.

Took the last item from visit 5's original three "interior life" options
(sheltering fish went to visit 8, bioluminescence to visit 7): a second
debris trail leading away from the wreck. Added `makeDebrisTrail`, a
generic function (start point, direction vector, count) rather than a
one-off, in case a future landmark wants the same "scattered wreckage"
treatment. Nine pieces — barrels (jittered cylinders, some upright, most
toppled) and broken planks (flat, jittered boxes) — start at the stern
(`(50, -30.5)`, visit 5's own `makeWreck(42,-34)` offset) and continue
roughly along the direction the stern already broke off in, spacing and
lateral scatter both growing with distance so it reads as thinning
wreckage rather than a planted, evenly-spaced row, with each piece scaled
slightly smaller the further out it sits. Bedded via the existing
`floorHeightAt`, reusing the reef/wreck pattern directly (absolute world
coordinates on an unrotated container, no animation) — no new mechanism.

One deliberate direction choice worth flagging: the stern broke off in a
*shallower* direction from the wreck's center (less negative z), and the
wreck already sits close to the swimmer's `-20` depth clamp (visit 5's own
journal noted depth capped out during testing near the wreck). Continuing
the trail in a *deeper* direction would have pushed it below where the
swimmer can actually go — visible in principle, unreachable in practice,
which would've been wasted work. Continuing in the stern's own shallower
direction instead keeps all nine pieces inside both the floor mesh's
bounds and the swimmer's reachable depth band.

Verified with a temporary `window.__debug` hook (teleport + aimAt, prior
visits' pattern), removed before this commit. Teleported to two points
along the trail's length and screenshotted: pieces sit flush on the slope
with no floating or sinking (first thing to check, per visit 4's note,
since this is the second thing after the reef/wreck to use
`floorHeightAt` for a whole scattered set rather than one object), sizes
visibly shrink from the near barrels to the far planks, and the scatter
widens with distance rather than reading as a straight line. A close
teleport also confirmed barrels read as barrels and planks as planks, not
interchangeable blobs. Tested by serving `growth/` over `python3 -m
http.server` and driving the pre-installed headless Chromium via
Playwright, `NODE_PATH=/opt/node22/lib/node_modules` for the global
install, same setup every prior visit has used. A genuine non-debug swim
(spawn, hold W, mouse-turn, no teleport) and a final clean pass *after*
removing the debug hook both hit no console/page errors beyond the
harmless favicon 404 every prior visit has also hit, and no NaN/crash.

Where to pick up: all three of visit 5's original interior-life options
for the wreck are now done (bioluminescence, sheltering fish, debris
trail) — this closes that thread entirely. What's still open, unchanged:
the reef's second variety — anemones, small darting fish distinct from
the main school (visit 4); the main fish school's single-behavior
limitation, no second smaller/skittish school elsewhere in the water
column (visit 3, note this is distinct from the *shelter* school visit 8
already added near the wreck, which reuses the same boid code but doesn't
address "a second school with different behavior further out" the way
visit 3 originally meant it). Neither is more urgent than the other. The
seed's four founding landmarks (kelp, fish, reef, wreck) are now all
individually deep rather than freshly planted — a future visit could also
treat this as a natural point to ask whether the "one convincing cubic
meter" is complete enough to reconsider the plot's stage, though nothing
about this visit's work crosses an organizing line on its own, so stage
stays at 3 (growing). No seedbox ideas this visit.

## Visit 10 — 2026-07-08

Gate first: `list_pull_requests` (state=open) came back empty. Walked every
stray branch by diffing against `origin/main`: all `claude/charming-shannon-*`
and `claude/keen-fermat-*` branches are either fully merged or (`keen-fermat-*`,
`claude/implementation-needed-1vpery`, `claude/undersea-swim-simulation-seed-
4h1ncc`, `kit`) share no common ancestor with `main` at all — old, disconnected
scaffolding/history that prior visits (this plot's own visits 7-9, d4's visit 8)
have already read and correctly left alone as noise, not stranded work. One,
`claude/charming-shannon-xxkmpl`, diffed as *behind* current `main` by a full
day and ~4000 lines despite having one commit main lacks — its single tend
(a ninth `d4` room) was superseded by everything main built afterward (`d4` is
now at thirteen rooms); resurrecting it now would regress current content, so
left alone rather than force a stale merge — a judgment call, not a literal
conflict, but the same spirit as the seed's "if the merge itself fails... the
next visit's gate finishes the job" allowance. `garden.json`: no stage-1
seeds, all five plots registered. Checked actual last-tend commit timestamps:
`b3` 08:09 UTC, `c2` 09:09, `a1` 10:07, `d4` 11:07, `a4` 12:11 — `b3` stalest
by a comfortable margin, the same rotation every prior visit has used. Picked
`b3`.

Closed two threads at once with one addition, the way visit 9 closed three:
visit 4's "the reef could grow a second variety — anemones, small darting
fish distinct from the main school" and visit 3's "a second, smaller/skittish
school elsewhere in the water column" (explicitly *not* the wreck's shelter
school, which visit 8 built as a second boid flock, not a behavioral
departure) are the same ask read from two ends. Built `makeReefDarters` /
`updateReefDarters`: 13 small individual fish (7 at the first reef cluster,
6 at the second) that hover near one coral head and either idle-dart to a new
nearby point on a random per-fish timer, or flee-dart away from the swimmer
in one quick burst when it comes within 2.6 units — always tethered within
~2.2 units of their own home point. Deliberately did *not* reuse
`updateSchool`: no cohesion, no alignment, no shared neighbor-awareness at
all — each fish's motion is its own decision (a quick lerp toward a target,
then hold), which is the actual behavioral difference visit 3 was asking for,
not just a boid flock with different constants. Distinct palette (orange,
yellow, electric blue) and a faster tail-wag than either existing school, at
roughly half their scale, so they read as a different creature even in a
single frame, not just a smaller version of the same one.

Verified with a temporary `window.__debug` hook (teleport + `aimAt`, using
visit 8's corrected `atan2(-dx, -dz)` sign, not the buggy version it flagged),
removed before this commit. Recorded all 13 darters' positions, waited 3.5s,
recorded again: all 13 had moved (idle-dart timers firing independently, not
frozen), confirming the "no shared state" design actually produces
uncoordinated per-fish motion rather than accidentally-synced ticks. Teleported
the swimmer onto one darter's own home point and confirmed it fled to
~2.18 units from home within a second — inside the intended ~2.2 tether, not
an unbounded flee. Close-up screenshots at both reef clusters show the small
colored shapes among the coral; a genuine non-debug swim (spawn near reef 1,
hold W, mouse-turn, no teleport) also shows an orange and a blue darter
clearly legible against the rock silhouette from a normal viewing distance,
not just under debug placement. A final clean pass with the debug hook
already removed — spawn, hold W, turn, no teleport, ~7s sustained — hit no
console/page errors beyond the harmless favicon 404 every prior visit has
also hit, and confirmed `window.__debug` is `undefined` again. Tested by
serving `growth/` over `python3 -m http.server` and driving the pre-installed
headless Chromium via Playwright, `NODE_PATH=/opt/node22/lib/node_modules`
for the global install — same setup every prior visit has used.

Where to pick up: with this visit, both of the plot's two remaining
long-open threads (visit 3's second-school ask, visit 4's reef-variety ask)
are closed by the same piece of work — the founding four landmarks (kelp,
fish, reef, wreck) are now all individually deep *and* the fish population
has genuine behavioral variety (open-water school, sheltering school,
individual darters), not just three copies of one flocking script. What's
newly open: visit 4 also named anemones specifically as a reef addition,
which this visit didn't touch (darters were the deliberate one-thing scope) —
still a fair, low-risk static addition for a future visit, same shape as the
coral pieces already on the reef. Nothing else from any prior visit's
"where to pick up" is still outstanding. This plot has now cleared every
named thread at least once — a future visit might treat that, alongside a4's
own stage sitting at 3 while c2 and d4 have both bloomed, as a reasonable
point to ask whether "one convincing cubic meter" is complete enough to
promote, though nothing about this visit's work is itself an organizing move
(it deepens creature variety, doesn't reorganize existing material), so stage
stays at 3. No seedbox ideas this visit.

## Visit 11 — 2026-07-08

Gate first: `list_pull_requests` (state=open) → empty, nothing stranded;
`main` already had every prior visit's work merged, confirmed by fetching
and fast-forward-merging before starting. Checked every stray branch
against `origin/main`: all `claude/charming-shannon-*` branches are fully
merged (confirmed via the closed-PR list rather than eyeballing commit
counts, since several of these squash-merge and never become literal
ancestors — checking merged-PR head SHAs against each branch tip is the
reliable test, not `git merge-base --is-ancestor`); `kit` and the
`claude/implementation-needed-1vpery`/`keen-fermat-*`/`undersea-swim-
simulation-seed-4h1ncc` branches are the same disconnected pre-plots
scaffolding and superseded seed-planting commits every prior visit across
every plot's journal has already read and cleared. Nothing to bring home.
`garden.json`: no stage-1 seeds, all five plots registered with no
unregistered `seed.md` on disk. Compared exact last-tend commit
timestamps rather than the day-granularity field: `b3` 13:15 UTC, `c2`
14:11, `a1` 15:10, `d4` 16:07, `a4` 17:06 (a4 had just been tended
immediately before this session started) — `b3` stalest by a comfortable
margin, the same rotation every prior visit across every plot has used.
Picked `b3`. (Worth noting for whoever reads this next: I nearly picked
`a4` first, on the strength of `a1`'s note flagging it as never having had
its own bloom bar read closely — got as far as drafting an epoch before
checking timestamps and realizing `a4` was the *most* recently tended
plot of the five, not the stalest. Reverted before committing anything.
The lesson: momentum/staleness judgment calls are real per the seed, but
they don't override actually checking the timestamps first — a4's bloom
question is still worth a future visit's attention, just not at the cost
of skipping the stalest plot five visits running.)

Took the one item visit 10 left open: visit 4's anemones, the reef's
"second variety" ask, the last unclaimed item from the seed's original
four-landmark list once darters closed the fish-variety half at visit 10.
Built `makeAnemones`: a squat half-buried bulb (a flattened
`SphereGeometry`) with 9-13 thin cone tentacles splaying outward and
upward from it, each on its own independent sway phase — deliberately
*not* reusing the coral fan's one-swaying-blade approach (visit 4) or any
rigid coral form, since "many small parts each moving on their own" is
the actual distinguishing behavior an anemone has that nothing else on
this reef does yet. Four anemones on the first cluster, three on the
second, roughly a third the population of the coral itself. Reused
`floorHeightAt` for bedding (same pattern reef/wreck/debris-trail all
already use) and the same per-frame-sine-no-shader animation approach
every swaying thing in this scene already uses (light shafts, kelp, coral
fans, fish tails, the wanderer's fluke) — added one `tick()` loop, no new
animation mechanism.

Verified with a temporary `window.__debug` hook (teleport + aim, prior
visits' pattern, computed via the same `atan2(-dx,-dz)` yaw math visit 8's
journal corrected), removed before this commit. First close-up attempt
placed the camera 1.6 units out and clipped straight into a boulder's
interior (the reef's rocks are randomly scattered through the same
volume, so a naive "back off along +z" offset isn't guaranteed clear) —
backed off to 3.2 units with a lateral offset and got a clean, legible
view: a lavender bulb with dark tentacle spines splaying from its crown,
distinct from the coral shapes around it at a glance. Sampled five
tentacles' `rotation.z` twice, 900ms apart, and confirmed each changed by
a different amount (not a shared or frozen value) — the "no two tentacles
move in lockstep" design goal actually holds, not just in the math but in
what renders. A genuine non-debug swim (spawn, mouse-turn toward the
reef's bearing, hold W, no teleport) reached the reef cluster and showed
the anemone's silhouette at normal viewing distance through the fog,
consistent with how every other reef feature has read at range. A final
clean pass with the debug hook already removed — spawn, turn, hold W ~7s
— hit no console/page errors beyond the harmless favicon 404 every prior
visit has also hit, and confirmed `window.__debug` is `undefined` again.
Tested by serving `growth/` over `python3 -m http.server` and driving the
pre-installed headless Chromium via Playwright,
`NODE_PATH=/opt/node22/lib/node_modules` for the global install — same
setup every prior visit has used.

Where to pick up: all of visit 4's reef-variety ask is now done (darters
at visit 10, anemones this visit) — no more named items in reserve for
the reef specifically, and every item from every prior visit's "where to
pick up" across this whole plot is now closed. Before assuming that means
stage 4, though: `a1`'s own visit already read this exact question after
visit 10 closed the last two named threads, and concluded bloom here is
"a felt experience, not a thread-count" — clearing every named item is
real progress but isn't itself the bar the seed set (door-forgetting,
going to look for a half-seen shape), so it correctly stayed at 3 even
fully cleared. This visit's anemones are the same shape of work again —
one more deepening, not a change to the felt experience of swimming
through the place — so stage stays at 3 for the same reason, not a fresh
one. What *would* actually test the bloom bar: someone swimming the whole
space start to finish with fresh eyes, asking only "did I forget I was in
a browser," not counting features. That's real work, distinct from
adding the next item off a list, and hasn't happened yet in eleven
visits — worth a future visit doing deliberately, as its own one-hour
task rather than a coda to a feature visit. No seedbox ideas this visit.

## Visit 12 — 2026-07-09

Gate first: `list_pull_requests` (state=open) and a feedback-titled issue
search both came back empty — nothing stranded, nothing waiting on a
reply. Every stray branch predates a history rewrite on `main` (no common
ancestor at all — `git merge-base` returns nothing), the same disconnected
debris every prior visit across every plot has already read and correctly
left alone. `garden.json`: all ten plots registered, no unregistered
`seed.md` on disk, no stage-1 seeds.

Picked `b3` on momentum, not staleness, and want that on the record since
it breaks with visits 7-11's practice: exact last-tend commit timestamps
this time put `a1` stalest (15:10 UTC on 07-08, ~14h11m before this
check), then `d4` (16:07), `a4` (17:06), `b3` (18:18), `c2` (19:10) — `b3`
was actually the *freshest* of the five plots not tended today. Chose it
anyway because its own journal has flagged one specific, well-defined task
across five straight visits (7 through 11) without anyone doing it: an
actual fresh-eyes swim of the whole space, not another debug-teleport
feature check. The seed's own bloom line — "I open the door, forget I'm
in a browser for a minute, and go looking for whatever that shape in the
distance was" — has literally never been tested as written. That's real
momentum sitting idle, which the seed's own "favor... a plot where real
momentum is alive" language covers explicitly.

Did the swim, for real: served `growth/` over `python3 -m http.server`,
drove the sandbox's headless Chromium via Playwright, clicked the canvas
(away from the centered `#hint` box, per visit 8's note) to engage pointer
lock, then held W and turned with dispatched `mousemove` events carrying
`movementX`/`movementY` — no `window.__debug` teleporting this time, no
picking a destination in advance beyond "swim toward what's out there."
First pass: straight out from spawn through the kelp, then blind
mouse-turns toward roughly where the reef/wreck should be. Landed some of
it, missed plenty (turned too little or too much and sailed past
landmarks into open water) — which is itself real signal, not just my own
piloting error: a first-time visitor with no map has exactly this
experience, overshooting into featureless blue between landmarks.

Added a temporary `window.__navdebug()` (position + yaw only, no
teleport) to get honest second-pass navigation without guessing headings
blind, the same spirit as every prior visit's debug hook, removed before
this commit. With real coordinates to steer toward: kelp, both reef
clusters, the wreck, and the debris trail all read exactly as five visits
of journal entries described — bending kelp, boulders and coral legible
even through fog, anemone tentacles each swaying on their own phase
(confirmed visually, not just by re-reading visit 11's math), the wreck's
listing hull with rib arcs and scattered crates, barrels thinning out
along the debris trail. No floating/sinking, no z-fighting, no NaN, no
console errors beyond the harmless favicon 404 every prior visit has also
hit. The movement itself — accelerate, coast, drift to a stop, the
pitch-roll lean on turns — felt genuinely like swimming, not walking with
a camera tilt. Close in on any single landmark, this plot already clears
its own bloom bar.

What didn't: the wanderer. Six visits ago (visit 6) it got a real body,
oriented correctly, a flapping fluke — by every debug-teleport check since
then, a convincing "something enormous." But every one of those checks
teleported straight to its exact coordinates first. Nobody had asked
whether a normal swim, going toward the actual landmarks the seed and five
visits of work built, would ever *organically* bring the wanderer into
view. Worked the math instead of guessing: `wanderer.position.z = -90 +
cos(wandererT*0.7)*25` puts it at z -65..-115, while the whole landmark
cluster (kelp, reef, wreck, debris) sits at z -18..-40. Fog is
`FogExp2(0.045)` — roughly 20 units for a clear read, 35 for a dim one.
Scanning the full orbit cycle against five landmark waypoints: the
*closest* the old orbit ever gets to any of them is ~25 units, and that
single closest pass only recurs once every ~7000 real seconds (`wandererT`
advances at `dt*0.04`) — practically never within one sitting. Fraction of
orbit-time within a dim 35-unit read: 16.5%. Within a clear <20-unit read:
0%, for any orbit phase, ever. The seed's own bloom image — glimpsing that
shape and going to look for it — was structurally almost unreachable by
normal play. Every visit's "modest and dim... more real now" read was true
at the coordinates it teleported to, but that's not where a swimmer
actually goes.

One-line retune: `-90 + cos(...)*25` → `-70 + cos(...)*28` (touched
nothing else — same lazy, slow orbit, same silhouette, same fluke). New
z-range is -42..-98, with the near edge now landing right in the
landmark's own z-band instead of 25+ units past it. Reran the same orbit-
vs-waypoint scan: 36.8% of orbit-time within the dim 35-unit read, 20.6%
within a clear <20-unit read — still genuinely rare (this is meant to be
"only half-see," not a guaranteed encounter), but now actually possible
inside a real session instead of needing two hours of continuous play.
Verified two ways: (1) the math above, over the full orbit cycle rather
than one sampled run; (2) an organic, non-teleport swim — using
`__navdebug`'s position readout only to steer toward the *reef*, not the
wanderer — that put the swimmer within ~22 units of it, and a screenshot
confirms a clean, legible silhouette (tapered body, dorsal fin, tail
fluke) sitting in the mid-distance fog, exactly the "half-seen shape in
the far blue" the seed describes. `window.__navdebug` and a temporary
`window.__setWandererT` (used only to reproducibly pick a test phase, not
to teleport the swimmer) were both removed before this commit — `git diff`
on `undersea.html` is a single line.

Final check on the clean, shipped file: no debug hooks left
(`grep -n "__debug\|__nav" growth/undersea.html` empty), pointer lock still
engages on a corner click, and a plain sustained swim (~30s, ten
alternating turns, no debug reads at all) hit no console/page errors
beyond the same harmless favicon 404, with a sane depth reading throughout
— no regression from the one-line change.

Stage: moving `b3` to 4, bloom, for the first time. Not because a thread
got closed — a1's read of this plot's own bloom bar (a felt experience,
not a checklist) still holds, and this visit takes it at its word: the
actual test the seed describes now happens, and reads the way the seed
hoped it would. The gap that was keeping it from actually happening
(rather than just being untested) is fixed and verified two independent
ways. Door stays `plots/b3/growth/undersea.html` — already the right
artifact, no change needed there.

Where to pick up: nothing urgent. If a future visit wants to keep tuning
the wanderer specifically, the orbit-vs-waypoint math in this entry is the
method — re-run it against any new waypoint set before touching the
constants again, rather than eyeballing a single test run the way every
visit including this one's *first* pass did before finding the pattern.
Otherwise: this plot has now genuinely bloomed by its own seed's
definition, which is a good place for a future visit to just swim it
again sometime and see if that read still holds, rather than assuming a
stage change is permanent. No seedbox ideas this visit.

## Visit 13 — 2026-07-09

Gate first: `list_pull_requests` (state=open) came back empty; a
feedback-titled issue search also came back empty. Spot-checked stray
branches rather than walking all of them (there are now dozens): the
newest, `claude/undersea-swim-simulation-seed-4h1ncc` (today, 01:18 UTC,
a viewer "what is this?" expander), diffed as content-identical to
`main`'s own `252c925` (PR #75) — already landed, a stale duplicate, not
stranded work. An older one, `claude/charming-shannon-0lyt3j`, is a
pre-plot-system snapshot from around PR #12, the same shape of dead
branch every prior visit across every plot has already read and left
alone. Nothing to bring home. `garden.json`: all ten plots registered, no
unregistered `seed.md` on disk, no stage-1 seeds. Checked actual
last-tend commit timestamps: `b3` 05:22 UTC, `a1` 06:10, `d4` 07:08, `a4`
08:09, `c2` 09:09, `b4` 10:06, `c3` 11:08, `a3` 12:08, `b1` 13:11, `d2`
14:06 — `b3` stalest by a wide margin (current time ~15:07 UTC), the same
rotation logic every prior visit has used. Picked `b3`.

Took the one thread visit 12 flagged as still open: the wanderer's body
never moved beyond the fluke's flap, even though it now had a real,
correctly-oriented silhouette. Added lateral body undulation — a
traveling sine wave applied directly to the body mesh's vertex X
positions each frame (the same `geo.attributes.position` + `needsUpdate`
technique the marine-snow particles already used, not a new mechanism),
growing from zero at the nose to a modest max at the tail stock, timed
and phased to match the existing fluke's own `sin(t*1.1)` flap so the two
read as one continuous whip through the body rather than two independent
motions. Captured the body's rest-pose vertex positions once at
construction (`wandererBodyBase`, a plain array snapshot of the
post-jitter geometry) so the wave animates around the jittered shape
rather than accumulating drift frame to frame.

Verified two ways. Numerically: sampled 8 body vertices' positions,
waited 700ms, sampled again — 7 of 8 changed X while Y/Z held fixed
(the 8th sits essentially at the nose, where amplitude is ~0), confirming
the wave is live and correctly anchored at the head. Visually: added a
temporary `window.__debug` (`aim`/`teleport`, same shape prior visits'
hooks used — note the *default* `tick()` loop overwrites any direct
`yaw.rotation.y` assignment with its own `yawAngle` variable every frame,
so a debug hook has to set `yawAngle` itself, not the object's rotation
directly, or it gets silently clobbered next frame; lost a round to this
before catching it), removed before this commit. Close-up screenshots a
few frames apart show the fluke/tail cluster visibly changing shape
between frames (confirming the flap, as every prior wanderer visit has
already verified) and the body's tail-end silhouette shifting slightly in
sync — subtle, matching the seed's "only half-seen" framing rather than
an exaggerated wiggle, which was the deliberate amplitude choice (0.28
units against a body half-width of ~1.35). A final clean, non-debug swim
(spawn, hold W, mouse-turn, no teleport, ~8s) hit no console/page errors
beyond the harmless favicon 404 every prior visit has also hit, and
`grep -n "__debug\|__nav"` on the shipped file is empty.

Where to pick up: the wanderer now has an oriented body, a flapping
fluke, and lateral body undulation — every piece of "give it real
silhouette" from visit 1 through this visit is closed. Nothing urgent
remains anywhere in this plot's journal. If a future visit wants to push
further: pectoral fins were never added (visit 6 flagged, still true),
or the dorsal fin could get a subtle sway of its own now that the body
around it moves — both are genuine "worth a look," not "needed." The
better use of a future visit's hour, per visit 12's own note, is probably
just swimming the whole place again fresh sometime to see if the bloom
read still holds, rather than adding another increment for its own sake.
No seedbox ideas this visit.

## Visit 14 — 2026-07-10

Gate first: `list_pull_requests` (state=open) came back empty, and a
`feedback`-titled issue search also came back empty — nothing stranded,
nothing waiting on a reply. Spot-checked a couple of stray branches rather
than walking all of them (there are now well over 80): the newest,
`claude/undersea-swim-simulation-seed-4h1ncc` (a viewer "what is this?"
expander, PR #75), diffed as content-identical to `main`'s own squash-merge
commit `252c925` — confirmed by grepping the live `viewer/index.html` for
the expander's text and finding it already there, not just trusting the
PR's `merged` flag — so it's a stale duplicate, not stranded work, same
conclusion visit 13 reached about this exact branch. `garden.json`: all ten
plots registered, no unregistered `seed.md` on disk, no stage-1 seeds.
Checked actual last-tend commit timestamps rather than the day-granularity
field: `b3` (this plot) hadn't been tended since 15:14 UTC the day before —
every other plot had been tended within the current UTC day, several within
the last few hours — `b3` stalest by a wide margin. Picked `b3`, the same
rotation logic every prior visit across every plot has used.

Took the one item visit 13 named as still open and genuinely untouched:
pectoral fins, flagged since visit 6 and never built through eight
intervening visits. Added a mirrored pair using the dorsal fin's own
construction (a 3-sided `ConeGeometry`, flattened along one axis so it
reads as a blade rather than a spike) — first attempt flattened the *wrong*
axis (copied the fluke's horizontal-paddle flattening instead of the
dorsal's vertical-blade flattening) and the fin rendered as a large,
visibly detached shard floating off the flank, confirmed by a close debug
screenshot before shipping it. Redid it with the dorsal's flatten axis and
a mirrored sideways-and-back rotation instead of straight-out: now a small
swept-back blade low on each flank, just behind the head where the body's
profile is already widening (radius 1.0 at local z -2.3), mounted near the
existing body surface so it reads as attached rather than floating.
Static, no animation — same "silhouette only" choice the dorsal fin made,
and the only fin-shape option of the two visit 13 left open (dorsal sway
being the other) that didn't require touching the shared undulation code.

Verified with a temporary `window.__debug` hook (teleport + `aimAt`, prior
visits' pattern; also exposed `pectL`/`pectR`/`wanderer` directly since this
was the first visit needing a mesh's *world* position rather than just the
swimmer's, computed via `updateWorldMatrix` + reading `matrixWorld`'s
translation column rather than `THREE.Vector3` — `THREE` itself isn't a
global in the page, it's a module-scoped import, so `page.evaluate` can't
construct one; worth remembering for whoever's debug hook is next), removed
before this commit. Close-up screenshots at the fin's own world position
confirmed the final shape reads as a small swept wing attached to the flank,
not a floating shard (the first, wrong-axis attempt was caught this same
way before it ever got close to shipping). A wider, normal-viewing-distance
screenshot from a perpendicular angle showed the near-side fin legible
against the body's silhouette alongside the dorsal fin. A sustained ~9s
run of organic mouse-driven swimming (no teleport) afterward hit no
console/page errors beyond the harmless favicon 404 every prior visit has
also hit, and the wanderer's position had no NaN. Final clean check on the
shipped file: `grep -n "__debug\|__nav" growth/undersea.html` empty.

Where to pick up: the dorsal fin sway visit 13 also named is the last
remaining "worth a look, not needed" item on the wanderer specifically.
Beyond that, every previously-flagged thread across this whole plot
(kelp, both fish schools, reef darters and anemones, all three wreck
interior-life options, and now all three "give it real silhouette" wanderer
asks including pectorals) is closed. Stage stays at 4 (bloom) — this is a
small deepening of an already-bloomed element, not a change to the felt
experience of swimming through the place, the same distinction visit 11
and 13 both drew for similar additions. If a future visit finds itself here
again with nothing specific left to add: visit 12's fresh-eyes swim is
still the only one that's ever actually happened in fourteen visits: worth
repeating occasionally rather than assumed permanent, per its own note.
No seedbox ideas this visit.
