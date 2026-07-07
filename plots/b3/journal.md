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
