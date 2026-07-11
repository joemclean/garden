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
