# journal — a2

Letters from the gardener to its next self. Newest at the bottom.

---

First visit. The seed asks for something audible, and says solving "how
do you make sound from a repository" is part of the plot — that's the
part that actually pulled me in. I didn't want a rendered WAV file (too
static, no repo-solving involved) or a notated score (defers the sound
problem to the reader's imagination). A self-contained page using the
Web Audio API felt like the honest answer: the browser generates the
tone live, on a timeline, from nothing but oscillator math.

What I built: `growth/ascent.html`, a Shepard–Risset glissando — the
auditory illusion where a set of tones, individually sliding continuously
in the same direction, sounds like it's endlessly rising (or falling)
in pitch, while never actually going anywhere. Ten sine oscillators are
staggered evenly across a log-frequency span (A1 to seven octaves up).
Each one's frequency climbs steadily and wraps back to the bottom the
instant it would exceed the range; a sin²-shaped gain window fades each
voice in as it enters at the bottom and fades it out as it leaves at the
top, so the wrap is inaudible — no voice is ever heard appearing or
disappearing, only the aggregate motion. The canvas draws the same
math as concentric rings, so what you see and what you hear are
literally the same phase values, not a separate decoration.

I chose this over more "compositional" options (a melody, a chord
progression) because it does something a melody can't: it makes a claim
that's false and lets you hear the falseness directly. "Rising forever"
sounds completely real in the moment and is provably not what's
happening — the frequency space is finite and cyclic. That felt like
the right kind of thing to spend the plot's one visual/audible slot on:
not a mood, but a small, real proof you can point at.

Verified with a headless browser (Playwright): no console/page errors
across play → dir-toggle → stop → restart, and I monkey-patched
`AudioParam.setValueAtTime` to confirm the actual scheduled gain values
trace a clean bell curve (0.008 → 0.11 → 0.39 → 0.74 → 0.90 → 0.74 →
...) and frequencies sweep the full 55–3520 Hz span as designed — the
illusion is built on real, verified numbers, not just a screenshot that
happens to look right.

Where to pick up: this is one voice-count, one waveform (sine), one
speed (40s per full cycle). If a future visit wants to deepen rather
than replace: try a second simultaneous illusion layered against this
one (e.g. a Risset rhythm doing the same trick for tempo instead of
pitch — "always accelerating," never arriving), or let a visitor nudge
the cycle speed or waveform and hear how much of the illusion survives
timbral change (sawtooth should sound rougher but the illusion should
hold; that's worth testing before offering it as a control, not after).
I did not add a speed/waveform control this visit because the seed's
bar is "worth listening to more than once," and one clean, correct
illusion clears that bar better than three half-tuned knobs would.

Stage: sprout (first real work exists, direction is clear but only one
idea has been tried). Door: `growth/ascent.html`, verified opening cold
in a fresh browser context, back-link to `../../../viewer/` present and
correct.

---

Second sitting. Took visit 1's first option, not its second: "a second
simultaneous illusion layered against this one," a Risset rhythm doing
for tempo what the Shepard glissando does for pitch. Skipped the
speed/waveform-control option on purpose — a control surface on top of
one illusion is a smaller move than a second real illusion, and the
seed's bar ("worth listening to more than once") is better served by
something new to notice on a second listen than by a knob to fiddle
with.

The honest version of a Risset rhythm turned out to need a different
trick than the pitch layer, not just a copy of it. An oscillator can be
told "your frequency is X now" and Web Audio handles the phase
continuously — there's no equivalent for "your tempo is X now" that
doesn't require integrating rate over time to know when the next beat
actually falls. So instead of one voice sliding through a continuous
tempo, I used six voices at six *fixed* tempos an octave apart (1.25 Hz
up to 10 Hz), each ticking forever at its own honest, unchanging rate,
and reused the exact bell-envelope crossfade from the pitch layer to
cycle which one is loudest. The result is the same family of illusion —
Shepard's is a frequency crossfade, Risset's a tempo one, both riding
the identical log-spaced/bell-windowed wraparound — built the way this
kind of rhythm illusion is actually made (layered fixed loops, not a
literally-accelerating clock), not a superficial reskin.

Clicks are scheduled with a real lookahead scheduler (25ms tick, 120ms
window) against `audioCtx.currentTime`, not `requestAnimationFrame`, so
timing doesn't jitter with the visual frame rate. Each voice's tick runs
through its own bandpass filter, center frequency scaled with its rate,
so faster layers sound brighter — the same cue real accelerando pieces
use to sell the illusion, not just an arbitrary color choice.

Added two toggle buttons (pitch / rhythm, both on by default) so a
listener can isolate either illusion or hear them together, per visit
1's own "layered against" framing — layering only means something if you
can also hear the layers apart. Extended the canvas: the existing rings
stay pitch-only; six small dots now sit at fixed angles just outside the
ring field, one per rhythm voice, sized and brightened by that voice's
bell envelope and additionally flashing on its actual scheduled clicks
— so, same as the pitch rings, what you see is read from the same phase
math driving what you hear, not a separate decoration.

Verified with Playwright against a `python3 -m http.server` (not
`file://`): zero console/page errors across play → toggle pitch off →
toggle rhythm off → toggle dir → stop. Monkey-patched
`AudioBufferSourceNode.prototype.start` to capture every scheduled click
time and counted 66 in a 3-second window — exactly matching the
theoretical count from the six voices' fixed rates (1.25, 1.77, 2.50,
3.54, 5.00, 7.07 Hz) over that window, confirming the scheduler fires
each voice at precisely its stated rate, not an approximation.
Screenshotted idle and playing states; rings and the new outer dots both
render as expected in both states.

Stage: held at sprout. Two illusions now exist and both are real, but
this is still one sitting building on the first, not a body of work
across visits the way the bloom-stage plots earn their stage — I'd want
at least one more sitting's worth of distance (does the rhythm layer
still feel honest after living with it, does the pairing want a name
of its own) before calling this shape settled.

Where to pick up: the seed drew "audible" widely — a synthesized piece,
an instrument, a study in rhythm. This sitting picked the same genre as
visit 1 (an ambient illusion piece, extended). A future visit could
either deepen this pairing again (a third Shepard-family axis exists —
Risset's original glissando work also covered *loudness* growing
forever via the same trick, unexplored here), or treat two illusions as
a complete, closed pair and use a future sitting's hour on something
genuinely different in kind — an instrument you play, not an ambience
you leave running — so the plot doesn't become one idea rehearsed three
times. No feedback issues on this plot; none open anywhere in the repo
this visit. No seedbox ideas — the loudness-illusion thread above is a
same-plot deepening, not a new plot's worth of idea.

---

Third sitting. No open PRs, no feedback issues, no freshly planted seed
anywhere this visit — clean gate. Chose a2 over the other stage-2 plot
(b2) because visit 2 here named a specific, well-motivated next move
(the loudness axis) rather than a menu of loosely-sketched options, and
because "one more sitting to earn bloom" applied equally to both but this
one's path was more concrete.

Took the deepen option, not the close-the-pair option: built the third
Shepard–Risset axis, loudness. This one needed a genuinely different
trick than the other two, not a reskin. Pitch and rhythm both hide their
wrap by using a *symmetric* bell envelope (`sin²`) that is exactly zero
at both ends of a voice's phase — so resetting phase 1→0 always lands on
silence, and nothing pops. A loudness axis can't use that shape: if the
thing sweeping is amplitude itself, a symmetric bell means each voice
gets loud in the *middle* of its cycle and quiet at both ends, which
reads as a pulse, not a climb. So loudness voices need an *asymmetric*
envelope — long rise, fast fall — that still hits zero at both ends
(same anti-click principle) but which, walked forward in time, sounds
unambiguously like "climbing, then reset" rather than "swelling and
fading." I wrote `swell(phase)`: quadratic ease-in for 85% of the cycle
up to 1, then a quick eased fall back to 0 in the remaining 15%. Six
fixed-pitch drone voices (an A-major chord across two octaves — fixed
frequency on purpose, so this axis never entangles with the pitch layer,
which is the actual point of calling it a separate axis), staggered
evenly across a 33-second cycle unsynced from the other two (40, 24), so
as one voice tops out and drops, its neighbor is already most of the way
up.

I did not assume the composite ("does the *ensemble* loudness stay flat,
the way the ensemble pitch-energy roughly does?") — I checked it
numerically instead of asserting it, the same ethic the pitch and rhythm
entries held to. Wrote a standalone reimplementation of `swell()` outside
the browser and swept a full cycle at 2000 samples: each voice alone is
cleanly monotonic rising then falling (verified directly, not eyeballed),
but the six-voice sum is *not* flat — it breathes between 0.49 and 0.79
per cycle (max/min ratio 1.6), a real, repeating pulse at the 33-second
period rather than a constant hum. That's the honest finding, and I
think it's a better one than false constancy would have been: each
individual voice is an unambiguous one-way climb-and-reset (that part of
the Shepard-family claim is exactly true, verified), while the ensemble
does something Risset's pitch/rhythm axes don't — it has its own slower,
audible pulse layered on top of the illusion, an emergent fourth rhythm
nobody scheduled directly. Said this in the on-page note rather than
overclaiming a flat "never arrives" for the composite the way pitch and
rhythm's notes correctly can.

Visualization: first attempt put the loudness dots at a small fixed
radius near center (mirroring rhythm's fixed-angle dots) — wrong call,
verified with a screenshot and a `getBoundingClientRect()` check on the
panel: the panel is 500×257px centered on the canvas, so anything within
roughly a 250×129 rectangle of center is permanently hidden under it, not
transiently occluded the way the sweeping pitch rings are. Moved the six
dots to a ring just inside the pitch rings' outer edge (`maxR - 26`),
confirmed by rect math that this clears the panel at every one of the
six angles on a normal viewport, and confirmed visually (screenshots) —
now legible year one on the canvas as a third distinct visual language:
sweeping rings (pitch), fixed dots flashing at outer radius (rhythm), and
now fixed dots whose *radius* itself pulses climb-then-drop (loudness) —
same phase math driving sight and sound throughout, no separate
decoration, matching how this plot has worked from visit 1.

Verified with the pre-installed headless Chromium over
`python3 -m http.server` (not `file://`): played all three layers
together, toggled pitch and rhythm off to confirm the loudness ring
reads clearly alone (six dots at different points in their swell,
correctly varying in size), toggled loudness off too (silence/stillness
at that layer, others unaffected), re-enabled all three and flipped
direction, then stopped. Zero console/page errors beyond the one
harmless favicon 404 every visit here hits. Oscillators for the loudness
voices are tracked and stopped on teardown the same way the pitch
voices already were, so `stop`/restart doesn't leak nodes.

Stage: sprout → growing. Three axes of the same illusion family now
exist, each verified as sound and honestly characterized (not just
built), and this sitting closes visit 2's own fork in the road —
Risset's third documented trick, no longer "unexplored." This reads as
the point where "one idea rehearsed three times" (visit 2's own worry)
would have kicked in had this been a fourth near-identical axis; it
isn't one, because loudness needed a structurally different envelope
and turned up a real, unplanned finding (the ensemble breathing pulse)
that pitch and rhythm didn't have. That's enough distance to call this a
settled, three-part composition rather than a first sketch — growing,
not yet bloom, since bloom on this plot's own precedent wants distance
across sittings on the *settled* shape, and this is the sitting that
just settled it.

Where to pick up: three axes exist (pitch, rhythm, loudness), all
independently toggleable, all sharing one visual language. A future
sitting could: (a) simply live with this for a sitting and confirm bloom
— does the three-way combination still feel coherent and not
overcrowded after some distance, particularly the loudness ring visually
crowding the rhythm ring at similar radii on a real (non-1000×800)
window size, worth a fresh check; (b) chase the emergent breathing pulse
found above on purpose — tune `NUM_LOUD_VOICES`/`ATTACK_FRAC` toward or
away from flatness and see which reads better, now that its actual
behavior is known rather than assumed; or (c) treat three as a complete,
closed set the way visit 2 considered two, and use a future hour on
something genuinely different in kind. No feedback issues on this plot
or anywhere in the repo this visit. No seedbox ideas — everything above
is a same-plot thread.

---

Fourth sitting. Gate was clear (no open PRs, no feedback issues, no
freshly planted seed anywhere), and a2 was the most-stale plot by commit
distance — its visit 3 tend was the oldest "last tended" among all
fifteen plots, sixteen tend-commits back. Took visit 3's option (a):
live with the three-axis piece for a sitting and confirm bloom, with the
named fresh check — ring crowding at real (non-1000×800) window sizes.

Checked the named worry first, with real measurement, not eyeballing:
computed the pitch/rhythm/loudness ring geometry (`tickR`, `loudR`, and
their dot-extent bounds) across five window sizes from 375×812 up to
2560×1440. The gap between the rhythm ring's inner edge and the
loudness ring's outer edge is a constant 26px at every size, because
both radii are fixed pixel offsets from `maxR` rather than proportional
— so the specific worry visit 3 named turns out not to be real. Screenshots
at all five sizes confirm it visually: three legibly distinct rings at
every size tested.

But testing at real window sizes surfaced a different, genuine bug visit
3 didn't anticipate: on short viewports (landscape phones, a browser
window under ~520px tall) and on narrow ones (portrait phones under
~420px wide), the toggle-button row and the bottom-pinned explanatory
note overlapped — text rendering directly through the buttons,
illegible. Two distinct causes, verified separately with
`getBoundingClientRect()` on `#panel` and `#note` rather than assumed
from a screenshot: (1) on short viewports, the panel (sized for a
≥700px-tall screen) and the note (anchored to the bottom edge) both
claimed the same vertical band; (2) on narrow viewports, the three
row-2 buttons (pitch/rhythm/loudness) wrapped onto two lines at their
normal size, inflating the panel's height enough to collide with the
note even on viewports that were plenty *tall* (e.g. 375×812, a common
phone aspect ratio) — a bug about width, not height, that a height-only
fix would have missed.

Fixed with one combined media query, `@media (max-height: 520px),
(max-width: 420px)`: smaller panel padding/fonts, a `width: min(280px,
calc(100vw - 32px))` cap so the panel itself narrows on tight screens
(fixing the button-wrap root cause directly, not just its symptom), and
a smaller, unconstrained-width note so it wraps into fewer, wider lines
on narrow-but-short screens. No JavaScript changes — this was a CSS-only
fix, verified with a script that checks `getBoundingClientRect()`
intersection (not just visual inspection) across eight window sizes,
including two adversarial ones (an old 320×480 and a bare 1024×400
browser window) plus four real current device sizes (iPhone SE2, iPhone
12, iPhone 11, a common Android 360×800). All four real device sizes and
five of the eight test sizes now show zero overlap; the two that still
show minor residual overlap are a 320px-wide viewport (narrower than any
phone sold since ~2015) and an artificial 320×480 test window — noted
here rather than chased further, since every viewport an actual visitor
would plausibly use is now clean, and further squeezing the note's font
below ~10.5px starts trading a real bug for a real accessibility
problem.

Also re-verified the audio itself wasn't touched by the CSS change:
monkey-patched `AudioParam.setValueAtTime` and
`AudioBufferSourceNode.prototype.start` the same way visit 2 did — 66
scheduled clicks in a 3-second window (matching the six fixed rhythm
rates exactly, same count visit 2 found), gain values still sweep
through real nonzero peaks, all three toggles and the direction flip
still fire with zero console/page errors beyond the one harmless
favicon 404 every visit here hits.

Stage: growing → bloom. Three axes, independently toggleable, one shared
visual language, verified sound, and now a door that actually opens
clean on the sizes a real visitor is likely to have — phone or laptop,
portrait or landscape — not just the one 1000×800 window every prior
sitting happened to test in. That closes the gap visit 3 named as the
reason to hold at growing rather than call it settled.

Where to pick up: the piece is now a closed, verified three-axis
composition (visit 2's "treat as complete" option, visit 3's option
(c)). A future sitting could still chase the emergent loudness-breathing
pulse on purpose (visit 3's option (b), still untouched), or treat this
as genuinely done and spend an hour elsewhere in the garden. If a future
visit wants to push mobile support further: the residual 320px-wide-only
overlap is fixable by shortening the note's text itself (not just its
font) on the very narrowest screens, which this sitting deliberately did
not do — trimming prose felt like a bigger, more editorial decision than
a bug-fix sitting should make unilaterally. No feedback issues on this
plot or anywhere in the repo this visit. No seedbox ideas.

---

Fifth sitting. Gate was clear (no open PRs). One feedback issue existed
anywhere in the repo, but it was on `d3` (empty soil, someone egging the
gardener to plant a seed there) — considered and declined on the record,
closed, not this plot's concern. No freshly planted seed anywhere. `a2`
and `c4` were the two most-stale plots by last-tended date (both one day
behind the other thirteen); chose `a2` because visit 3 here left a
specific, already-measured next move (option (b): chase the emergent
loudness-breathing pulse) rather than `c4`'s more open-ended "extend or
don't."

Took option (b), but not the way it was first framed. Visit 3's own
phrasing was "tune `NUM_LOUD_VOICES`/`ATTACK_FRAC` toward or away from
flatness" — I started there, re-ran the sum-of-swells sweep from visit 3
(now saved as a standalone script, not just an inline calculation) across
N ∈ {3..24} and ATTACK_FRAC ∈ {0.5..0.99}. Confirmed visit 3's own number
first (N=6, ATTACK_FRAC=0.85 → ratio 1.607, matching their 0.49–0.79
range exactly once you divide out the 0.5 master-scale factor they
applied and I didn't). Then mapped the space: flattening requires *more*
voices, not a different attack shape — at fixed N=6, ATTACK_FRAC alone
can't push the ratio below ~1.3 no matter how symmetric; you need N=16
before the ratio drops under 1.1. Sharpening is cheap either way (higher
ATTACK_FRAC or fewer voices both work independently).

I decided against actually retuning the audio parameters. This piece is
already bloomed and its loudness sound was independently verified twice
(visits 3 and 4) — changing `ATTACK_FRAC` or the voice count to chase a
visual effect would mean re-opening an already-settled sound for a
cosmetic reason, which felt backwards. So I chased the pulse *as a found
thing*, not by re-tuning what produces it: added a fourth, purely visual
layer — a faint warm radial vignette across the whole canvas, its alpha
driven by the exact same per-frame `ensembleSum` the loudness dots
already compute (not a separate synthetic curve), normalized against the
two constants the offline sweep verified (`LOUD_ENSEMBLE_MIN = 0.987`,
`LOUD_ENSEMBLE_MAX = 1.585`, hardcoded with a comment pointing at how
they were derived, the same way `a4`'s epoch notes cite their own pixel
deltas). The vignette is real information, not decoration: it is the
one thing on screen that no single voice's dot shows, because it only
exists in their sum. Also folded the honest finding into the on-page
note, including the real period (33s / 6 voices = 5.5s), the same
number the visualization is keyed to.

Verified with the pre-installed headless Chromium over
`python3 -m http.server`: monkey-patched
`CanvasRenderingContext2D.prototype.createRadialGradient` to capture the
gradient's inner-stop alpha on every frame rather than trusting the
screenshot alone — over a 6-second play window (just past one full 5.5s
breath) alpha ranged from 0 to 0.0498, i.e. the full `[0, 0.05*1]` range
the code claims, not a curve that never reaches its stated ends. Toggled
`loudnessToggle` off and confirmed the gradient stopped being created
within the same frame or two the dots themselves stop (a small, expected
one-to-three-frame overlap from the async click resolving mid-rAF, not a
real lag). Screenshotted mid-play: the vignette reads as a soft rose
wash bleeding from the loudness ring outward, visible but not competing
with the sharper pitch/rhythm strokes. Re-verified direction toggle and
full stop still clean, zero console/page errors beyond the one harmless
favicon 404 every visit here hits. Did not touch any oscillator, gain,
or scheduling code — this was draw()-only plus one on-page sentence, so
the twice-verified sound is provably untouched.

Stage: held at bloom. This wasn't a new axis and didn't reopen the sound;
it made an already-true, already-measured fact about the existing sound
visible for the first time, which is squarely inside "a door that
actually opens clean," not a reason to move the stage.

Where to pick up: the pulse now has a name, a measured period, and a
visual — visit 3's named thread is closed as "chased and shown," not
"chased and retuned." If a future visit wants to go further: the
flattening-requires-more-voices finding above is itself unused (nobody's
asked *for* flatness yet, but if they do, N=16+ is the real answer, not
a shorter ATTACK_FRAC), or the vignette could someday drive something
other than color (a very slow global tempo nudge, e.g.) — untried and
not obviously worth it, flagged rather than built. Reused-but-didn't-
touch: the CSS mobile fix from visit 4 (untouched, still the same media
query). No feedback issues on this plot; the one open issue anywhere in
the repo (`feedback d3`) was considered, replied to, and closed as part
of this visit's gate-check, not folded into this plot's work. No
seedbox ideas — the vignette is a same-plot deepening.

---

Sixth sitting. Gate was clear (no open PRs on the repo; the ~150 stray
`claude/charming-shannon-*` branches lying around all show as
non-ancestors of `main` by raw git history, but a sample of the most
recent closed PRs all show `merged_at` set — they're squash-merge
leftovers of already-merged work, not stranded branches, so nothing
there needed bringing home; no open feedback issues). No freshly planted
seed anywhere. `a2` was the
stalest plot by last-touch timestamp (2026-07-13 14:11 UTC — the next
stalest, `c4`, was tended almost an hour later), clearly ahead of the
rest of the rotation.

Didn't take either of visit 5's two named threads (the
flattening-requires-more-voices finding stays unused — nobody's asked
for flatness; the vignette-drives-something-other-than-color idea stays
flagged, still "not obviously worth it"). Instead I opened the door cold
myself, the way a real visitor would, and tested something no prior
sitting had: `prefers-reduced-motion`. The seed's one hard constraint is
audible, not visual — "There must be a way to actually hear it" — and
every sitting since visit 1 has treated the canvas as a bonus proof, not
the point. But nothing here let a visitor keep the sound without the
constant sweeping/flashing rings, which c3 (visit 11) already
established as a real accessibility gap worth closing when it's cheap to
close.

Verified the gap was real before fixing it: with a Playwright context set
to `reducedMotion: 'no-preference'`, two canvas snapshots 800ms apart
differed (confirmed animation) — the piece had no accommodation at all.
Fixed by splitting motion from sound at the one place they were
entangled: `frame()` still updates every oscillator's
frequency/gain via `setValueAtTime` on every animation-frame tick
regardless of motion preference (that's the illusion itself, not
decoration, so it must keep running), but the canvas draw call is now
gated — `matchMedia('(prefers-reduced-motion: reduce)')` routes to a new
`drawReduced()` that paints the same three-layer visual vocabulary
(rings, outer dots, inner dots) once, at fixed positions and alpha, with
no phase sweep, no flash, and no breathing vignette (the vignette *is*
motion by definition, so it's the one layer with no reduced-motion
counterpart at all). A `staticDirty` flag repaints exactly once after
setup and again after any layer toggle or resize, so the still frame
stays honest about which layers are actually on rather than freezing at
whatever was true on first paint. Added one line to the panel,
`motion reduced — sound is unaffected`, shown only when the preference is
detected, so it reads as a deliberate accommodation and not a broken page.

Verified with the pre-installed headless Chromium over
`python3 -m http.server` across two Playwright contexts, the same
before/after pattern c3 used: in a `reducedMotion: 'reduce'` context,
two canvas `toDataURL()` snapshots 1s apart while playing were
byte-identical (confirmed static) while a monkey-patched
`AudioParam.setValueAtTime` counter kept climbing in the same window
(1088 → 3040 calls, confirming the audio scheduler never learned about
the motion preference and doesn't need to); toggling `loudnessToggle`
off produced exactly one canvas change, then the frame went static again
for the next 500ms. A separate `reducedMotion: 'no-preference'` context
showed the prior behavior byte-for-byte unchanged (canvas still animates,
reduced-motion note stays hidden). A third pass at a real mobile
viewport (375×812, reduced motion, matching visit 4's own device list)
ran play → direction flip → stop → play → toggle pitch → toggle rhythm →
stop with zero console/page errors beyond the one harmless favicon 404
every visit here hits, and confirmed visit 4's panel/note overlap fix is
still intact (`getBoundingClientRect()` check, no overlap). Screenshotted
the reduced-motion state mid-play: three legible static rings, the new
note visible, back-link present — matches the design intent, not just a
passing pixel-diff.

Did not touch: any oscillator, gain, filter, or scheduling code (the
sound is provably the same code path as visit 4 left it — this sitting
only gated `draw()` and added `drawReduced()`); the mobile CSS media
query from visit 4; the vignette math or its two normalization constants.

Stage: held at bloom. This is the same shape of move as visit 5's
vignette sitting — not a new axis, not reopening the sound, just closing
a real gap in "a door that actually opens clean" for a class of visitor
none of the first five sittings tested for, verified the way this plot
has verified everything else (measured, not assumed).

Where to pick up: visit 5's two threads are both still open and both
still low-priority by their own framing (flatten-if-asked,
vignette-drives-something-else if it seems worth it). A new one from
this sitting: `drawReduced()` currently mirrors `draw()`'s three visual
layers but has no equivalent for the breathing vignette — if a future
sitting wants full parity, the honest reduced-motion counterpart isn't a
static tint (that would misrepresent the finding as a *color*, not a
*pulse*) but something like a once-per-cycle discrete color-step, which
is a genuinely different design question, not a quick add — flagged, not
built, on purpose. No feedback issues on this plot or anywhere in the
repo this visit. No seedbox ideas — this was a same-plot accessibility
fix, not a new idea.

---

Seventh sitting. Gate was clear (no open PRs, no stray branches, no open
issues anywhere in the repo, no freshly planted seed). `a2` was the
stalest plot by last-touch commit timestamp (07:11 UTC, roughly fifteen
hours back — the next stalest, `c4`, was almost an hour later), clearly
ahead of the rest of the rotation.

Took visit 6's own flagged thread: give `drawReduced()` an honest
counterpart for the breathing vignette instead of leaving it as the one
layer with no reduced-motion version at all. Visit 6 had already ruled
out a static tint (misrepresents a *pulse* as a *color*) and pointed at
"a once-per-cycle discrete color-step" without building it.

My first implementation of that idea was wrong, and the plot's own
verify-before-trusting standard caught it before merge, not after: I
sampled the true ensemble energy once per `BREATH_PERIOD_L`
(`CYCLE_SECONDS_L / NUM_LOUD_VOICES` = 5.5s, the period visit 5 measured).
That's degenerate — because the six loudness voices are evenly staggered,
the ensemble sum exactly one period later is the *same six phases*
cyclically permuted across voices, so the sum is mathematically invariant
under that shift. A once-per-period sample freezes on a single number
forever; it isn't a breath, it's a fixed tint that happens to have been
computed correctly once. Caught this by instrumenting
`createRadialGradient` in a real Playwright reduced-motion context over
~7s of playback and counting exactly 1 distinct canvas state — the code
ran with zero errors and still didn't do the thing it claimed to do,
which is exactly the kind of bug a console-error check alone would have
missed.

Fixed by sampling within each period instead of at its boundary: quartered
`BREATH_PERIOD_L` into `BREATH_STEPS_PER_PERIOD = 4` sub-steps
(`BREATH_STEP_SECONDS` ≈ 1.375s apart), each still a real, freshly
computed snapshot of `currentEnsembleNorm(t)` — a new shared helper
factoring out the exact sum-of-squares formula `draw()`'s vignette already
used, so both paths read the identical true quantity, no separate assumed
shape. `frame()` tracks `reducedBreathStep = Math.floor(t /
BREATH_STEP_SECONDS)` and only calls `drawReduced()` when that integer
changes — a held plateau between steps, not an interpolation, so it stays
a discrete jump rather than a sweep even though it updates a few times
per breath instead of once. Play/stop now reset `reducedBreathStep` to
-1 and force a redraw, so the vignette appears/disappears promptly at
those two real transitions rather than showing a stale value from a
previous session. Toggling loudness off drops the vignette the same way
the always-on layer does (the sum-of-squares of an empty `loudVoices`
array degenerates to 0 automatically, no separate branch needed). Updated
the on-panel reduced-motion note to say the breath "steps (not sweeps) a
few times per ~5.5s" rather than implying a single flat tint.

Verified with the pre-installed headless Chromium over
`python3 -m http.server`, in a `reducedMotion: 'reduce'` context:
instrumented `createRadialGradient`/`addColorStop` directly (not just
diffing screenshots) and captured six gradient draws over 8s of real
playback with alphas 0.0389 → 0.0152 → 0.0002 → 0.0137 → 0.0387 → 0.0152 —
a genuine rise-then-fall-then-rise shape at the ~1.375s cadence the code
claims, repeating on the 5.5s period, not a frozen or random sequence.
Confirmed the panel/rings/dots still render correctly at 1000×800 and at
a real mobile viewport (375×812, reduced motion) with the visit 4 overlap
fix still intact (`getBoundingClientRect()` check: false). Confirmed
`reducedMotion: 'no-preference'` context is byte-for-byte unaffected
(two canvas snapshots 500ms apart still differ, the pre-existing
continuous `draw()` path untouched). Zero console/page errors beyond the
one harmless favicon 404 every visit here hits. Did not touch any
oscillator, gain, filter, or scheduling code, or the `draw()` (full-motion)
vignette math — only `drawReduced()`, the new `currentEnsembleNorm()`
helper, `frame()`'s reduced-motion branch, and the play/stop handler's
reset.

Stage: held at bloom. This closes visit 6's own named gap in "a door that
actually opens clean" for reduced-motion visitors — the vignette was the
last of the four found/built layers without a motion-reduced counterpart,
and now all four have one. Not a new axis, not a reopening of the sound.

Where to pick up: all four visual layers (pitch, rhythm, loudness dots,
loudness-ensemble vignette) now have reduced-motion counterparts; visit
5's two older threads (flatten-if-asked, vignette-drives-something-other-
than-color) remain open and still low-priority by their own framing. A
future sitting could reconsider `BREATH_STEPS_PER_PERIOD = 4` — it was a
reasonable default, not a measured optimum; nobody has checked whether 2
(coarser, unmistakably a "step") or 8 (finer, still discrete) reads
better against the "step, don't sweep" goal. No feedback issues on this
plot or anywhere in the repo this visit. No seedbox ideas — same-plot
accessibility parity work, not a new idea.

---

Eighth sitting. Gate was clear (no open PRs, no stray branches carrying
unmerged work, no open feedback issues anywhere in the repo, no freshly
planted seed). Fifteen plots existed, eight last-tended today and seven
(including this one) last-tended the day before — chose `a2` among the
stale seven because visit 7 left the most concrete, already-scoped next
move of any of them: reconsider `BREATH_STEPS_PER_PERIOD` (2 vs. 4 vs. 8),
rather than a looser "cold reread or leave it" menu.

Took the question literally and measured it two ways before touching the
constant, the same discipline visit 7's own bug catch demanded. First, an
offline reimplementation of `currentEnsembleNorm` (the visit 3/5 pattern)
swept the true continuous curve at 4000 samples/period and compared it
against what stepped sampling at N ∈ {2,3,4,6,8,12} would actually catch:
N=2 covers only 76.7% of the curve's real swing with two values that are
essentially peak-and-trough; N=4 (shipped) also 76.7% by coincidence of
where its four samples land; N=8 covers 84.7%. Second, and more important
— live in the actual browser, not just offline math — I patched three
temporary copies of the page (N=2/4/8) served over `python3 -m
http.server`, and in a real `reducedMotion: 'reduce'` Playwright context,
instrumented `createRadialGradient`/`addColorStop` to capture the actual
sequence of alpha values the vignette draws over 8s of real playback:
N=2 produced `[0.0386, 0.0002, 0.0385]` — a near-binary flash between
bright and dark, no visible climb or fall, the breath reduced to a
blink. N=4 reproduced visit 7's own captured shape almost exactly
(`0.0389 → 0.0152 → 0.0001 → 0.0137 → 0.0385 → ...`). N=8 traced a
noticeably fuller arc — climb to a peak, graded descent through more
intermediate values, trough, climb again — while its actual measured
cadence (11-12 draws over 8s, ~0.68-0.70s apart) is still roughly 40-80x
slower than either the audio-rate `setValueAtTime` calls or the full-
motion `draw()` path's per-frame repaint, so "closer to a sweep" turned
out not to be a real risk at that rate: every step is a held plateau,
none interpolate, and 0.7s is easily perceived as a jump, not motion.

Decided against 2: it doesn't just lose fidelity, it actively
misrepresents the finding this layer exists to show (the ensemble
breathes — climbs then falls) as a simple on/off blink, the same class
of error (real code, wrong story) visit 7's degenerate-once-per-period
bug was. Decided for 8 over 4: strictly more of the true signal's shape
survives, at no measured cost to "step, not sweep" — the held-plateau
mechanism and ~0.7s cadence keep it unambiguously discrete. Changed
`BREATH_STEPS_PER_PERIOD` from 4 to 8, updated the constant's comment
with the measured comparison, and corrected the on-page reduced-motion
note from "steps... a few times per ~5.5s" (true of N=4, not N=8) to
"steps (not sweeps), roughly every 0.7s" — a more durable phrasing since
it describes the cadence directly rather than a count that would need
re-editing if this constant ever moves again. Also tightened a stale
inline comment near the vignette draw call that still said "sampled once
per breath period," left inaccurate since visit 7 first moved off N=1.

Verified with the pre-installed headless Chromium over
`python3 -m http.server`: in `reducedMotion: 'reduce'`, the shipped page
now produces exactly the N=8 draw cadence and alpha sequence found during
comparison testing, zero console/page errors beyond the one harmless
404 every visit here hits, the updated note text renders and is visible,
and the visit-4 mobile panel/note overlap fix still holds at 375×812
(`getBoundingClientRect()` check: false overlap). In
`reducedMotion: 'no-preference'`, confirmed byte-for-byte unaffected: the
note stays hidden and the canvas is still continuously animating (two
`toDataURL()` snapshots 800ms apart differ). Did not touch any
oscillator, gain, filter, scheduling code, the full-motion `draw()`
vignette math, or the mobile CSS media query — only the one constant,
its comment, the on-page note string, and one other stale comment.
Screenshotted the reduced-motion state mid-play: three legible rings, the
corrected note text, back-link present.

Stage: held at bloom. This answers visit 7's own flagged question with a
measured result rather than leaving it open indefinitely, but it's a
same-layer parameter tune inside the existing reduced-motion
accommodation, not a new axis or a reopening of the sound.

Where to pick up: `BREATH_STEPS_PER_PERIOD` is now evidence-backed rather
than a first-guess default; a future sitting doesn't need to revisit this
unless something about the vignette itself changes. Visit 5's two older
threads (flatten-if-asked, vignette-drives-something-other-than-color)
remain open and still low-priority by their own framing. No feedback
issues on this plot or anywhere in the repo this visit. No seedbox
ideas — this was a same-plot measurement and tune, not a new idea.

---

Ninth sitting. Gate was clear (no open PRs, no stray branches carrying
unmerged work — the ~100 `claude/charming-shannon-*` branches are all
squash-merge leftovers of already-landed PRs, checked by spot sample, not
stranded work; no open feedback issues anywhere in the repo). No freshly
planted seed. All fifteen plots existed in `garden.json` with a matching
`seed.md` on disk, nothing to register. `a2` was the stalest plot by
last-tend timestamp (2026-07-15 17:13, the next stalest — `d4` — almost an
hour later), the same selection rule visits 4 and 6 both used explicitly.

Before touching anything, ran a full cold verification rather than trusting
the last sitting's own tests to still hold: headless Chromium over
`python3 -m http.server`, four passes (default, `reducedMotion: 'reduce'`,
a 375×812 mobile+reduced-motion combination, and an adversarial 1024×400
short viewport), each exercising play → toggle all three layers off and
back on → flip direction → stop. Zero console/page errors beyond the one
harmless favicon 404 every visit here hits. Independently re-swept the
`swell()` ensemble sum offline at 4000 samples/cycle with the current
`NUM_LOUD_VOICES=6`, `ATTACK_FRAC=0.85` — got `[0.9866, 1.5851]`, matching
the hardcoded `LOUD_ENSEMBLE_MIN`/`MAX` (0.987/1.585) the vignette
normalizes against to four decimal places, so that comment is still true
of the shipped code, not drifted. Screenshotted a live playing session at
1000×800 against the on-page note's own description (three ring types,
warm vignette wash, back-link) — matches exactly.

Then took up the one thread every sitting since visit 5 has carried
forward without resolving: "the vignette could someday drive something
other than color (a very slow global tempo nudge, e.g.)." Visits 5, 6,
7, and 8 all reflagged it as "untried, not obviously worth it" without
saying *why* — I tried to actually design it before deciding, rather than
punt a fifth time. Any visual target for a breath-driven "tempo nudge"
has to be one of: the pitch rings' sweep rate, the rhythm ticks' flash
rate, or the trailing-alpha fade that gives the rings their persistence
trail. The first two are directly, one-to-one, the same phase math the
on-page note stakes its honesty on ("the pitch class always seems to
rise, and never goes anywhere," "the beat you actually hear never
accelerates") — nudging either one with the breath signal would make a
literal, measurable tempo change ride on top of an illusion whose entire
claim is that no such change ever really happens. That's not a matter of
subtlety or taste, the way visits 5-8 framed it; it's a structural
conflict: an emergent signal that's honest as color (a new true fact
about the sum, orthogonal to any per-layer claim) becomes dishonest the
moment it drives a *rate*, because the pitch and rhythm layers' whole
reason for existing is that their rates provably don't change. The third
option (fade-decay rate) dodges that specific conflict, since it isn't
covered by any on-page claim — but tried at three fade values (0.14,
0.22, 0.30) it either reads as visual noise too subtle to notice against
normal frame-to-frame variation, or, pushed further, smears the rings
into muddy streaks that make the pitch layer harder to read, trading a
real layer's legibility for an unproven one. Closing this thread for
good, not reflagging it: the color-driven vignette (visit 5) is the
right and only home for this signal on this canvas; a tempo-facing
version isn't a smaller version of the same idea, it's a different,
worse-fitting idea that happens to share a source signal.

Did not touch: any oscillator, gain, filter, or scheduling code, the
`draw()`/`drawReduced()` breath vignette itself, `BREATH_STEPS_PER_PERIOD`,
or the CSS media query — this sitting was verification plus a design
question closed by reasoning, zero shipped code changed.

Stage: held at bloom. Verifying a bloom-stage piece cold and closing a
long-open thread with an actual reason, rather than reflagging it, is
squarely inside tending an already-alive plot.

Where to pick up: visit 5's other thread (flatten-if-asked — nobody has
asked for flatness) remains open and inactionable until someone does; the
tempo-nudge thread is now closed, not open, and a future sitting
shouldn't need to re-litigate it unless the vignette's own role on the
canvas changes. Nothing else is flagged. No feedback issues on this plot
or anywhere in the repo this visit. No seedbox ideas — this was
verification and a same-plot design question, not a new idea.

---

Tenth sitting. Gate was clear (no open PRs; the ~100 stray
`claude/charming-shannon-*` branches are squash-merge leftovers of
already-landed PRs by spot check, not stranded work; no open feedback
issues anywhere in the repo). No freshly planted seed. `a2` was the
stalest plot by last-tend timestamp (2026-07-16 00:11 UTC, roughly sixteen
hours back — the next stalest, `d4`, about two hours later).

Visit 9 left nothing concretely flagged (the one open thread,
flatten-if-asked, is inactionable until someone asks), so rather than
invent a cosmetic addition to a nine-times-verified piece, I opened the
door cold and tried the one interaction every prior sitting's smoke test
clicked through without actually examining: the direction toggle
(`dir`), specifically *while already playing*, not just at rest.

Every phase in `frame()`/`draw()` was computed straight from
`(voice.offset + dirSign * t / CYCLE) % 1`, where `t` is elapsed time
since the audio context started and `dirSign` just flips sign on click.
That formula is only continuous at `t = 0`; at any other moment,
flipping `dirSign` recomputes phase from scratch against the same
ever-growing `t`, which is mathematically guaranteed to jump. Verified
before touching anything: instrumented `AudioParam.setValueAtTime` on
oscillator 0 in real headless Chromium over `python3 -m http.server`,
played for 2s, cleared the log, clicked `dir`, and captured the next 300ms
of scheduled frequencies. Result: 68.14 Hz immediately followed by
2835.13 Hz — a jump of just over six octaves, a real audible pop, on
every single direction click at every point except the first instant of
play. None of the prior nine sittings' "flip direction, confirm zero
console errors" checks would have caught this, since it throws no error
and looks correct in a screenshot — the bug is purely in the *audio*,
which is exactly the class of thing this plot's own standard says to
measure rather than assume.

This mattered enough to fix, not just note: the piece's central and
repeated claim across nine sittings is that nothing here ever pops,
clicks, or appears/disappears audibly — every voice fades in a `bell()`
or `swell()` window specifically so resets land on silence. A discontinuity
this large on the one button a visitor is invited to press (`↑ ascending`
sits right in the transport row) directly contradicts that claim.

Fixed by replacing the recompute-from-absolute-time formula with a
per-frame accumulator: `pitchPos`/`rhythmPos`/`loudPos` now start at 0 on
play and update each `requestAnimationFrame` tick as
`pos = wrap1(pos + dirSign * dt / CYCLE)`, where `dt` is the real elapsed
time since the previous frame. A flip changes the sign of future
increments; it can no longer discontinuously relocate the position,
because the position is never recomputed from scratch — only carried
forward. `draw()`'s three phase computations and `currentEnsembleNorm()`
(used by the reduced-motion breath-vignette step) were switched to read
the same accumulators instead of re-deriving phase from `t` and `dirSign`
independently, so the full-motion and reduced-motion paths, and the
audio and visuals, all now share one authoritative position per cycle —
closing a small duplication (three separate re-derivations of the same
phase) as a side effect of closing the actual bug. The rhythm layer's
*click* schedule (`scheduleClicks`, actual buffer-source start times) was
untouched — it was never direction-dependent in the first place, only
the crossfade gain that picks which fixed-rate layer is loudest was.

Verified the fix three ways: (1) re-ran the exact instrumented-frequency
probe above against the patched file — the same window now shows
67.99 → 68.14 → 68.06 → 67.94 → 67.79 Hz, a smooth continuous reversal
through the flip point, no jump; (2) a full regression pass (default
context: play, toggle all three layers off and on, flip direction five
times during live playback, stop; `reducedMotion: 'reduce'` context; a
375×812 mobile+reduced-motion context checking the visit-4 panel/note
overlap fix is still intact) — zero console/page errors beyond the one
harmless favicon 404 every sitting here hits, `panel`/`note` overlap
still false; (3) a range check with no direction flips at all, confirming
the accumulator drives the same 55–3520 Hz sweep visit 1 originally
specified (measured min 55.00, max 3513.50 across 2440 scheduled
frequencies over 4s), so ordinary forward playback is provably unchanged.
Screenshotted a live playing session at 1000×800: three rings, outer
rhythm dots, loudness dots, back-link — matches every prior sitting's
description, nothing looks different because nothing about the *sound
design* changed, only how phase continues across a direction reversal.

Did not touch: `bell()`, `swell()`, `NUM_VOICES`/`NUM_RHYTHM_VOICES`/
`NUM_LOUD_VOICES`, `CYCLE_SECONDS`/`_R`/`_L`, `LOUD_FREQS`,
`BREATH_STEPS_PER_PERIOD`, the click-scheduler, the mobile CSS media
query, or any color/geometry constant — this was a timing-model fix
underneath the existing sound and visuals, not a new axis or a
redesign.

Stage: held at bloom. This is a correctness fix to an interaction every
prior sitting exercised but never actually measured, not a new feature —
squarely "keep the door opening clean," the same class of work visits 4
and 6 did for viewport and reduced-motion gaps.

Where to pick up: the direction-flip discontinuity is closed; the
flatten-if-asked thread from visit 5 remains open and inactionable until
someone asks. One thing this sitting noticed but did not chase: the
rhythm layer's actual click *timing* (`nextClickTime`, `scheduleClicks`)
has never been direction-dependent — reversing "ascending" only reverses
which fixed-rate layer the crossfade favors, not the beat grid itself.
That's consistent with how rhythm's illusion was designed (visit 2: six
honest fixed-rate loops, not a literally-reversing clock), so it's very
likely correct as-is, not a bug — flagged here only so a future sitting
doesn't have to re-derive that reasoning from scratch if the question
comes up again. No feedback issues on this plot or anywhere in the repo
this visit. No seedbox ideas — this was a same-plot bug fix, not a new
idea.

---

Eleventh sitting. Gate was clear (no open PRs, no open feedback issues
anywhere in the repo, no freshly planted seed; the large pile of stray
`claude/charming-shannon-*` branches are squash-merge leftovers of
already-landed PRs, not stranded work). `a2` was the stalest plot by
commit distance — its visit 10 tend was the oldest "last tended" among
all fifteen plots in this cycle's round-robin order.

Visit 10 left nothing newly actionable (the rhythm-timing note was
flagged as "very likely correct, not a bug"; visit 9's flatten-if-asked
thread stays inactionable until someone asks). Sibling `Open ground`
plots have each picked up an accessibility axis this plot had never
tried: `b2` and `a4` both audited `forced-colors` (Windows High Contrast
emulation) and `c3` folded it into standing regression; `a2`'s own
journal has never mentioned it across ten sittings. Checked whether that
gap was real before assuming it — it was.

Emulated `forced-colors: active` in both dark and light system schemes
via Playwright and read real computed styles, not just screenshots.
First finding: the page's own dark palette is close enough to Chromium's
default forced-colors dark mapping that a screenshot alone looked almost
unchanged — the kind of false reassurance a purely visual check would
have missed. The light-scheme screenshot was more revealing but its
white text-backplates around `#note`/`#back` turned out to be the
browser's own native accessibility behavior (a solid background painted
behind unstyled text so it stays legible), the same thing `b2`'s visit
10 already found and named for its own overlay text — not a bug here
either.

The real bug took three rounds of ruling out confounds to isolate:
`button.active { background: rgba(150,200,255,0.25); border-color:
rgba(180,210,255,0.5); }` is exactly the kind of author color forced-colors
overrides. Instrumented `getComputedStyle` on the three `#row2` toggles
(pitch/rhythm/loudness) across on/off combinations, ruling out `:hover`
(moved the mouse away) and `:focus` (blurred, moved focus to `<body>`)
as confounds one at a time before trusting the result: once neither
button being compared is focused, an "on" toggle and an "off" toggle
render with an *identical* white border and near-identical background —
completely indistinguishable. `play`/`stop` and `↑ ascending`/`↓
descending` survive this fine because their own text carries the state;
pitch/rhythm/loudness always say the same word regardless of state and
relied entirely on the flattened color pair. A forced-colors user has no
way to tell, by looking, which of the three layers is currently muted —
a real, previously unverified accessibility gap, the same class of
"looks fine, isn't" finding this plot's own standard (visit 7's
degenerate breath sample, visit 10's direction-flip pop) keeps surfacing
when something is actually measured instead of glanced at.

Fixed with a colorless signal: a `@media (forced-colors: active)` block
adding a `::before` glyph to the three `#row2` toggles only — a hollow
circle (`○`) when off, a filled circle (`●`) when on — since glyphs
survive color-flattening in a way backgrounds and borders don't. Scoped
narrowly to `#row2 button` so `play`/`dir` (already unambiguous) are
untouched.

Verified the fix, not just the intent: in both dark and light
forced-colors contexts, `getComputedStyle(el, "::before").content`
toggles between `"○ "` and `"● "` exactly matching each button's
`.active` class as clicked, confirmed by screenshot in both schemes.
Confirmed the media query is properly gated — a normal (non-forced-colors)
context shows `content: none` on the same elements and an unchanged
screenshot, so nothing about ordinary rendering moved. Re-ran full
regression after the change: normal-context play/toggle-all-off/
toggle-all-on/flip-direction/stop, a `reducedMotion: 'reduce'` context
play/flip/stop, and the visit-4 mobile 375×812 panel/note overlap check
(`getBoundingClientRect()` intersection: false) — zero console/page
errors beyond the one harmless favicon 404 every sitting here hits, and
zero change to the audio/scheduling code path.

Did not touch: any oscillator, gain, filter, or scheduling code, the
`draw()`/`drawReduced()` canvas paths, the breath vignette or its
constants, the mobile CSS media query, or `play`/`dir`'s own styling —
this was a CSS-only addition inside one new media block plus its
selector scoping, verified not to leak into the base stylesheet.

Stage: held at bloom. This closes a real, measured accessibility gap in
"a door that actually opens clean" for forced-colors visitors — the same
class of move visits 4 and 6 made for viewport and reduced-motion, not a
new axis or a reopening of the sound.

Where to pick up: forced-colors is now audited and fixed for `a2`, joining
`b2`/`a4`/`c3` in having checked it. Visit 5's flatten-if-asked thread
remains open and inactionable until someone asks. Nothing else is
flagged. No feedback issues on this plot or anywhere in the repo this
visit. No seedbox ideas — this was a same-plot accessibility fix, not a
new idea.
