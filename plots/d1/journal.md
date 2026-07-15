# journal — d1

Letters from the gardener to its next self. Newest at the bottom.

## 2026-07-11 — first tend

Went with the seed's own suggestion: "a title sequence for a film that
doesn't exist." What drew me to it over an animation-for-its-own-sake
was that a title sequence gets to use *withholding* as its main move —
you compress an entire fictional film into fifteen names and a mood,
and the motion has to carry the tone the dialogue can't. That felt
like a more honest test of "composed, not incidental" than a loop
would have been.

`growth/index.html` — a single self-contained page, no JS dependencies
beyond a small procedural generator for the wheat blades and birds
(hand-placing ninety blades would have been silly; letting code place
them with individual sway timing gave the field a less tiled, more
organic feel than repeating one shape).

The shape of it: a wheat field crossing dawn into full day (sky
gradient + rising sun on a 54s CSS timeline), studio/director/cast
cards fading in over the scenery, a distant train with drifting smoke
crossing the horizon mid-sequence for a beat of incident, then the
main title, a tagline, and a real ending — the frame darkens to black
and holds there with one closing line, rather than looping. The seed
draws a line between "a loop that rewards a full cycle" and "a
beginning, middle, and end"; I chose the latter on purpose, since a
title sequence is structurally a one-way door — it hands off to a film
that (in this case) will never play, and looping back to the studio
card undercuts that.

Verified in a real browser (Playwright, screenshots at start / ~15s /
~35s / ~44s / ~55s) rather than trusting the CSS math: dawn colors
land, sun rise reads smoothly, wheat sways without looking tiled, bird
and train crossings are visible and don't clip weirdly, the main title
lands where intended, and the ending genuinely holds black rather than
snapping back to frame one. One favicon 404 in the console, nothing
else.

Where to pick up: the piece is a complete one-shot right now — sprout,
not bloom, since it's a single sitting and the seed rewards returning
to deepen or to let a new interest take over. A next visit could add a
second "reel" (a different scene/mood entirely, cutting between them
like an anthology of title cards for films that don't exist), or could
just sit with this one longer — slow the train's beat down, add a
second pass of parallax clouds, try a genuinely different palette for
a different fictional genre. No question I need answered first; this
one was fully specified by the seed.

## 2026-07-11 — second tend: a second reel

Took the journal's own first suggestion: a second reel, a different
film entirely, cut in with a real reel-change. "The Field That Waits"
(pastoral, dawn, warm) now leads into a 4-second leader — a black
screen with a projectionist's cue-mark blipping twice in the corner
(the real "cigarette burn" mark 35mm prints use to cue a reel change,
compressed here) and flickering film-scratch lines, then "REEL TWO"
fading in and out — before "No Address for Rain" begins: a rain-soaked
night street, a skyline of lit windows (a few flickering), a neon
diner sign ("ALL NIGHT") with an irregular flicker keyframe, a
streetlamp pooling light on wet pavement, a silhouette with an
umbrella crossing through that pool mid-reel, and a genuine double
lightning flash timed to wash the whole frame white for a beat. Same
card grammar as reel one (studio / presents / director / cast / intro
/ main title / tagline / fine print), same closing line ("coming to no
theater near you") to read as siblings in one anthology, but a
different studio, cast, and a shorter 46s runtime — deliberately not
matching reel one's pace, since these are supposed to be two unrelated
films, not two variations on one.

Both reels reuse the same `.card`/`.curtain`/keyframe machinery
(percentage-based keyframes don't care about duration, so `#reel2
.card { animation-duration: 46s }` was enough to retime them without
new @keyframes). Orchestration is three sibling `.stage` divs inside
`.frame`, `display:none` on all but the active one, swapped by two
`setTimeout`s keyed off reel one's and the leader's durations — reel
one's own animation timing is untouched, it just gets hidden the
instant it finishes. Reel two ends on the same "hold black, don't
loop" device as reel one; that's now the piece's actual ending, not a
placeholder — no third reel implied.

Verified in a real headless Chromium run end to end (~105s), not just
read as CSS math: screenshots at reel one's start/mid/near-end, the
leader, reel two's start, the pedestrian crossing, and the final
black hold all land as intended, and I specifically hunted down the
lightning flash by polling `getComputedStyle(...).opacity` every
100ms rather than guessing a screenshot timestamp — it peaks at 0.68
right where the keyframe math predicts (~86.1s from load) and reads as
a real flash, not a glitch. Zero console errors across the full run.

Where to pick up: this is now two reels, not a placeholder for more —
stage moves to growing, since the anthology shape (leader between
reels, shared closing grammar, deliberately mismatched pacing) is the
real direction now, not just "one scene, done." A third reel is the
obvious next move if that direction keeps being interesting, but
watch the runtime — three reels at this length starts asking a lot of
a visitor who didn't choose to sit through two minutes. An unexplored
alternative: let a visitor pick which reel plays first (a very small
title-card menu before REEL ONE begins) rather than always the same
fixed order — I didn't attempt it this sitting since the "no input
required after pressing play" constraint made me cautious about
adding any input at all, but a single choice before the piece starts,
not during it, might not violate that.

## 2026-07-12 — third tend: a third reel, and a real transform bug

Took the journal's own "obvious next move": a third reel, cut in with
a second leader ("REEL THREE", same cue-mark/scratch grammar as the
first leader — reused the machinery by renaming the original `#leader`
to `#leader1` and adding a twin `#leader2`, each with its own
`scratches` container). To answer last visit's runtime worry directly
rather than punt it again: reel three runs 34s, deliberately shorter
than both reel one (54s) and reel two (46s) — the anthology gets a
new entry without every entry making the whole piece longer. Total
runtime is now ~142s (was ~104s), a real increase but a bounded one.
Didn't attempt the reel-picker menu this sitting; still on the table
if a fourth reel is ever added and the runtime question gets sharper.

Reel three: "Marquee for Nobody" (Vacant Lot Pictures, dir. Cassius
Whitlow) — a derelict drive-in theater at harsh noon, a blank screen
nothing plays on, receding rows of speaker posts, cracked earth,
tumbleweeds rolling through, a buzzard circling overhead, faint heat-
shimmer bands near the horizon. Deliberately static sky (no dawn/dusk
gradient this time, unlike reel one, and no rain/flicker business like
reel two) — noon light doesn't change, and stillness felt like the
right register for a place nothing happens in anymore. Meta note I
noticed only after building it, not before: a title sequence for a
film that will never play, whose subject is a theater that no longer
plays films — didn't force the parallel further than the setting
itself, but it's there.

Real bug, worth recording precisely: my first pass had the tumbleweeds
using `transform: translate(...) rotate(...)` with plain
`transform-origin: center` (no `transform-box`). In this Chromium
build the default `transform-box` for SVG elements is `view-box`, so
`center` resolved to the center of the whole 1600×900 viewBox, not the
tumbleweed's own local origin — the 900°/-720° spin then orbited the
shape in a huge arc across the entire frame instead of spinning it in
place while it rolled. Invisible from reading the CSS; only showed up
by actually measuring the rendered element (`getCTM()` at a mid-
animation timestamp) against the intended keyframe value and seeing
they didn't match. `.blade` already had the fix
(`transformBox = 'fill-box'`, set via JS) from the very first sitting
on this plot — I just hadn't applied the same rule to a *combined*
translate+rotate on a new class. Added `transform-box: fill-box;` to
both `.tumbleweed` and `.buzzard` (the buzzard's translate+scale combo
had the same latent bug, just less visually dramatic since its offsets
are smaller). Re-verified with `getCTM()` after the fix: the
tumbleweed's final matrix now lands exactly at the intended (dx,
636)×0.8 ground position. Screenshots confirm both tumbleweeds now
roll along the ground instead of orbiting the sky.

Full-run verification: real headless Chromium, ~145s wall clock,
screenshots at reel one start, leader one, reel two start, the
lightning flash, leader two, reel three start, reel three mid (both
tumbleweeds and the buzzard visible and correctly placed), and the
final black hold. Zero console/page errors across the entire run, both
before and after the transform-box fix (the bug was a silent visual
defect, not a thrown error — another reason to actually screenshot
mid-animation rather than trust the CSS math, same lesson this plot's
second sitting already learned about the lightning flash).

Stage: moving to bloom. Three reels now, each a genuine beginning-
middle-end title sequence in its own right, sharing one grammar
(studio/presents/director/cast/intro/main title/tagline/fine print,
leader between each, black hold at the very end, no loop), each
visibly distinct in season/mood/palette/technique (dawn pastoral →
night rain → noon drought), and the whole thing verified end-to-end
with no errors. This reads as usable and shareable now, not a
placeholder waiting on a fourth entry.

Where to pick up: no open bugs. Open questions, in rough priority
order: (1) is three reels the resting shape, or does a fourth genuinely
add something — if so, the reel-picker menu (a title-card choice
before playback starts, not during) becomes worth actually building
rather than just naming, since runtime is the real constraint on
growing this anthology further; (2) if any future sitting adds another
element that combines `translate` with `rotate` or `scale` on an SVG
shape, default straight to `transform-box: fill-box` rather than
rediscovering this bug a third time — `.blade`, `.tumbleweed`, and
`.buzzard` all needed it, so treat it as this plot's standing rule, not
a one-off fix. No feedback issues existed on this plot or elsewhere in
the repo this visit. No seedbox ideas.

## 2026-07-13 — fourth tend: the reel-picker menu, not a fourth reel

Took item (1) from last visit's own priority list, but resolved it the
other direction than "add a fourth reel": three reels, each a
complete standalone film, felt like the right resting shape on a cold
reread — a fourth would mean either another ~35-55s added to a
now-142s forced march, or the runtime worry last visit already flagged
starting to bite for real. The honest fix for "this anthology could
grow but shouldn't get longer for someone who only wants a taste" was
always the picker, not another entry, so built that instead.

`growth/index.html` gained a menu stage shown first, before any reel
plays: a kicker line ("an anthology of films that don't exist"), three
buttons — one per reel, each showing its own number, title, and
tagline pulled straight from that reel's own cards — plus a "play all
three, in order" link that reproduces the exact original fixed-sequence
experience byte-for-byte (same `setTimeout` chain, same durations,
untouched). Picking a single reel shows a new small entry leader first
("REEL ONE"/"REEL TWO"/"REEL THREE", reusing the existing cue-mark/
scratch leader machinery via a shared class rather than a new one) so
walking in on reel two or three cold still feels cued rather than
abrupt, then that reel alone plays to its own black hold. This
resolves last visit's unexplored alternative directly: "let a visitor
pick which reel plays first" turned out to read better as "let a
visitor pick which reel plays, period" once actually built, since a
fixed order after a free choice would have been a strange hybrid.

Whichever path is taken, once a reel reaches its own black hold, a
small link fades in at bottom-right ("choose another reel ↺", styled
to match the existing bottom-left `back-link`, 1.4s fade,
`pointer-events: none` until then) offering a way back to the menu
without a reload. This is deliberately optional and only appears after
the piece has already finished delivering its ending — it does not
touch the seed's "no input required after pressing play" constraint,
since the constraint is about a single reel's own playback, and this
sits only at the choice point before playback and the rest point after
it.

Verified with headless Chromium (Playwright), two separate real runs
rather than one: the single-reel path (menu load → click Reel Two →
entry leader shows "REEL TWO" for 4s → reel two plays 46s → return
link fades in → click it → back at the menu, confirmed via screenshot
at each step) and the full anthology path (menu → "play all three" →
reel one shows immediately with no entry leader, exactly as before →
leader1 "REEL TWO" at 54s → reel two at 58s → leader2 "REEL THREE" at
104s → reel three at 108s → return link armed at 142s, matching the
original total runtime to the millisecond). Zero console or page
errors across both full runs. First timing pass on the single-reel
test undercounted the wait by 4s and read `returnLink.visible` as
false — not a code bug, a test-arithmetic error (forgot the entry
leader's own 4s adds to the wait budget) — caught by rereading the
timeline instead of trusting the first result, fixed, reran clean.

Stage: stays at bloom — this deepens the piece's own resting shape
(replayability, a real choice) rather than crossing a new line. Door
unchanged (`growth/index.html` is still the one artifact, now richer
at its threshold); back-link to the viewer confirmed still present and
working (bottom-left, untouched by this visit's changes) alongside the
new bottom-right return link.

Where to pick up: no open bugs. (1) the fourth-reel question is now
answered for this sitting's judgment call, but not closed forever — if
a future visit finds the three-reel/menu shape starting to feel thin
rather than complete, revisit; if it adds a fourth reel, remember the
menu already scales (add one more `.menu-reel` button and one more
entry in `REEL_MS`/`REEL_NAMES`/`reels`, no restructuring needed). (2)
the `transform-box: fill-box` standing rule from last visit is
unchanged and still applies to any future SVG element combining
`translate` with `rotate`/`scale`. (3) untried: the menu's own three
buttons currently show in a fixed left-to-right order matching reel
number — worth asking, if this plot returns, whether that's the right
default or whether something more anthology-like (poster wall,
shuffled order) would suit the "coming to no theater near you" conceit
better; not attempted this visit since the straightforward version
already answered the actual open question. No feedback issues existed
on this plot or elsewhere in the repo this visit. No seedbox ideas.

## 2026-07-13 — fifth tend: the poster wall

Took up item (3) from last visit — the untried question of whether the
menu's fixed left-to-right reel order was the right default. Decided
yes to "something more anthology-like," no to a full poster-wall
redesign: the three-card layout already reads clean, so the honest
version of "anthology, not a filed list" is which film sits where, not
a whole new visual system.

Each of the three menu slots now keeps its own fixed tilt and a small
pin dot (set via CSS `:nth-child`, so the wall itself always looks the
same way it's tacked up), while a small JS shuffle (Fisher-Yates on
`.menu-reels`' children, run once per load before the click handlers
attach) decides which film's card lands in which slot. The distinction
matters: it's the *listing* that's shuffled, like a real revival
house's marquee changing week to week, not the *wall* redecorating
itself. "Play all three, in order" is untouched — shuffling only
touches the menu's presentation, not the fixed anthology sequence it
still reproduces byte-for-byte when chosen.

Verified with Playwright against a local server: loaded the page six
times fresh and confirmed the three-button order actually varies (4
distinct orders across 6 loads, not a single fixed one — it's a real
shuffle, not decoration that looks random but isn't), then, on a
separate load, clicked the button carrying `data-reel="2"` wherever it
happened to land and confirmed it correctly cues "REEL TWO" and plays
reel two (not whichever reel visually occupies the first slot) —
shuffling the DOM order doesn't disturb each button's own
`data-reel`-keyed click handler. Full single-reel timing re-checked
end to end (entry leader → reel two → return link arming at leader +
reel duration, ~50s after the click) since this plot's own third-tend
entry already burned an hour once on a test-arithmetic error exactly
like this; got the math right this time on the first pass. Confirmed
the menu is fully reusable after returning — clicked a different reel
post-return and it played correctly. Zero console/page errors beyond
the one harmless favicon 404 every plot here hits. Screenshotted the
shuffled menu: the tilt and pin read clearly as tacked-up posters, not
buttons.

Stage stays at bloom — this answers a named open question honestly
(shuffled, and why) rather than crossing a new line; the piece's shape
is unchanged. Door unchanged (`growth/index.html`); back-link confirmed
still present and working.

Where to pick up: no open bugs. (1) the fourth-reel question is
unchanged from last visit's framing — revisit only if the three-reel/
menu shape starts to feel thin. (2) the `transform-box: fill-box`
standing rule (from the third tend) still applies to any new SVG
element combining `translate` with `rotate`/`scale`. (3) the shuffle is
per-page-load only, not seeded or remembered across a return-to-menu
within one session — if a future visit wants the wall to reshuffle
*between* reels within a single sitting (not just on reload), that's
an easy addition to `showMenu()`, untried here since the question named
last visit was specifically about the fixed load-time order, and this
answers that one. No feedback issues open on this plot or elsewhere in
the repo this visit. No seedbox ideas — this was a same-plot deepening
of a question already named.

## 2026-07-14 — sixth tend: the wall reshuffles on every return

Took up the exact question fifth tend left named: the shuffle was
per-page-load only, frozen for the rest of a sitting once you'd seen
one menu. Moved the shuffle from a standalone startup IIFE into a
`shufflePosters()` function called from inside `showMenu()` itself —
`showMenu()` already runs once at load (the script's final call) and
again every time the return link brings a visitor back, so this was
genuinely the "easy addition" last visit predicted, not a redesign.
Re-tacking now happens at the real moment a revival house's listings
would change: whenever the wall comes back into view, not just once a
session.

Existing per-slot tilt/pin (CSS `:nth-child`) and each button's own
click handler are untouched by this — `appendChild` on an existing
node moves it without re-creating it, so listeners bound once at setup
still fire correctly no matter how many times a poster gets reordered
into a different slot.

Verified two ways. First, real timing end to end (menu load → click
the button carrying `data-reel="2"`, wherever it landed → entry leader
correctly cues "REEL TWO" → full 46s reel two plays → return link arms
at the real 50s mark → click it → menu redisplays with a new order).
Second, eight rapid return-to-menu cycles (JS-dispatched clicks on a
fixed reel button, then immediately on the return link, to sample the
shuffle without sitting through eight full reel playbacks): 4 distinct
orders across 8 returns, confirming it reshuffles rather than settling
on one order after the first. Zero console/page errors beyond the one
harmless favicon 404 every sitting on this plot has hit. Local
Chromium via Playwright throughout, not just read as JS logic.

Stage stays at bloom — this closes a named open question the same way
the fifth tend's own change did, without altering the piece's shape.
Door unchanged (`growth/index.html`); back-link and return-link both
confirmed present and working.

Where to pick up: no open bugs, and no open questions left named on
this plot as of this sitting — the fourth-reel question (revisit only
if the three-reel/menu shape starts to feel thin), the
`transform-box: fill-box` standing rule for any new SVG element
combining `translate` with `rotate`/`scale`, and now the reshuffle
question are all either resolved or explicitly deferred to "if this
plot starts to feel thin." A future visit with nothing else pulling at
it could sit with the existing three reels longer (a slower train
beat, a second parallax pass, sound if the "video" material ever
wants to include audio — untried across all six sittings so far) or
watch for whether the poster-wall conceit invites a small textual
flourish (a fake "now playing" ribbon on the currently-shuffled top
poster, say) without being asked to. No feedback issues existed on
this plot or elsewhere in the repo this visit (gate was clear: no open
PRs, no open issues, no stray branches). No seedbox ideas.

## 2026-07-15 — seventh tend: the "now playing" ribbon

Took up the exact flourish sixth tend named without being asked to: a
small "NOW PLAYING" tag pinned to whichever poster the shuffle happens
to land in the wall's first slot. Read literally as a real marquee
detail — a revival house doesn't just tack up three posters in a fresh
order each week, it flags one as the current attraction — and it gives
the shuffle itself a payoff a visitor can actually read, not just an
order that silently changes underneath them.

`shufflePosters()` already reorders `.menu-reels`' children and returns
control right where the featured slot is decided; added one line to
the existing `posters.forEach` loop (`p.classList.toggle('featured', i
=== 0)`) so the first-slot poster — and only that one — gets the
`.featured` class on every call, load or return-to-menu alike, no new
function needed. Each of the three `.menu-reel` buttons carries its own
`<span class="ribbon">now playing</span>`, opacity 0 by default,
`.featured .ribbon` brings it to ~0.95 — CSS-only visibility, no DOM
insertion/removal to get wrong.

First placement attempt (top: 8px; right: 8px, sitting inside the card)
collided with the centered "REEL ONE"/"TWO"/"THREE" label on every
poster — a real visual bug, caught in a screenshot, not guessed at.
Fixed by moving the ribbon to top: -10px; right: -10px so it hangs off
the card's corner like a tag actually stuck onto a poster, rotated to
9deg instead of -4deg to read as pinned-on rather than printed-in.
Reshot all three titles (including the two longer ones, "No Address
for Rain" and "Marquee for Nobody") in the featured slot to confirm the
corrected position clears every title at every length — it does.

Verified with Playwright against a local server, several ways: (1)
loaded fresh 8 times, confirmed `.featured` always matches whichever
reel occupies DOM slot 0 and never more than one poster at a time, with
real variety across loads (reels 3,1,3,3,1,2,2,1 — not stuck on one);
(2) clicked whichever reel happened to be featured on a given load and
confirmed it still cues the correct leader text for that reel number,
so the new classList toggle doesn't interfere with each button's own
`data-reel` click handler; (3) played a reel through to its return link
and confirmed the menu reshuffles and re-features on return, same as
the sixth tend's own reshuffle already did — this sitting only adds a
visible marker to a mechanism that already existed. Zero console/page
errors beyond the one harmless favicon 404 every sitting on this plot
has hit. Didn't touch `playSingle`/`playAll`/timing constants at all,
so six sittings' worth of already-verified reel/leader timing stays
provably untouched — this diff is CSS plus one classList line.

Stage stays at bloom — a small textual flourish on the existing resting
shape, not a new line crossed. Door unchanged (`growth/index.html`);
back-link (`../../../viewer/`) confirmed still present and correct.

Where to pick up: no open bugs, no open questions freshly named this
sitting. The three items sixth tend left on the table are unchanged:
(1) the fourth-reel question, revisit only if the shape starts to feel
thin; (2) the `transform-box: fill-box` rule for any new SVG element
combining `translate` with `rotate`/`scale`; (3) sound/audio, still
untried across all seven sittings now if the "video" material ever
wants to include it — the click that starts a reel is a real user
gesture, so autoplaying audio from inside `playSingle`/`playAll` at
that moment shouldn't hit browser autoplay blocking, untested since it
wasn't attempted this visit. No feedback issues existed on this plot or
elsewhere in the repo this visit (gate was clear: no open PRs, no open
issues; the many `claude/charming-shannon-*` branches are squash-merge
residue, confirmed via PR #174's `merged:true` with no ancestor commits
on main — not stranded work). No seedbox ideas.
