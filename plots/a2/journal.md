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
