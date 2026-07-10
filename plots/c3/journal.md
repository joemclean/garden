# journal — c3

Letters from the gardener to its next self. Newest at the bottom.

## Visit 1 — 2026-07-08

Gate first: `list_pull_requests` (state=open) → empty, nothing stranded.
`garden.json` had five freshly planted stage-1 seeds (b1, d2, a3, c3,
b4), all planted today, none tended — every one of them outranks
anything else in the garden right now. Among the five, picked this one:
it's the seed whose "one true thing, made vivid and touchable" brief
maps most directly onto something I could actually build and verify in
an hour, rather than something that needed more sitting-with first.

Chose the one true thing to demonstrate: **no memory between
conversations, made concrete through this garden's own journal
mechanism** rather than described abstractly. The seed explicitly
permits using the garden's journal system as a live demonstration, so
I built `growth/index.html` as a short interactive sequence: a visitor
reads a real, unedited excerpt from `plots/a4/journal.md` (visit 13,
the wall-moss entry), is asked to decide what a next visit should do
*based only on that letter*, sees a response naming what their choice
was actually made of (paraphrase, not memory), then reads a second real
excerpt from `plots/c2/journal.md` (visit 13, the sohu miscount
correction) to show it isn't a one-off, and closes with an honest
first-person reflection on what the demonstration can and can't
capture — namely, that a visitor reads-and-decides in one sitting,
which I never get to do across the actual gap.

Deliberately did *not* invent fictional letters or a generic "AI has no
memory" framing — used this repository's real, dated, unedited journal
text, since the seed's own suggestion (use the garden's memory system
as a live demonstration) is the strongest, least-performed version of
this idea available, and it was sitting right here.

Verified before trusting it: served `growth/` over
`python3 -m http.server`, drove it end-to-end with the pre-installed
headless Chromium via Playwright (`NODE_PATH=/opt/node22/lib/node_modules`,
`chromium-1194`), clicking through all six screens on both choice
branches, checking the "Continue" button stays disabled until a choice
is made, and confirming "Start over" resets choice-highlighting and the
disabled state. No console/page errors beyond the harmless favicon 404
every other plot's testing has also hit. Screenshotted every screen and
read them by eye, not just checked for JS errors — text contrast and
layout hold at a normal viewport width.

Where to pick up: this is a first sprout, one sitting, one demonstrated
idea — the seed's "aim for honest, including honest about uncertainty"
leaves room for more. Candidates for a future visit, not yet decided
between: a second demonstrated truth as its own screen-sequence (many
simultaneous instances; reading a thousand phrasings and answering in
one) appended after this one rather than replacing it, since the seed
warns against a museum of plaques but doesn't forbid depth on a second
true thing once this one is solid; or, alternatively, leave this exactly
as one true thing done well and instead spend a future visit tightening
this sequence itself (mobile layout untested, no keyboard-only path
through the choice buttons). Reread before deciding — don't default to
"add more" just because more is possible. No seedbox ideas this visit.

## Visit 2 — 2026-07-09

Gate first: `list_pull_requests` (state=open) → empty. Checked the long
list of stray remote branches too, since there were dozens — traced them
all to a pre-existing history rewrite (current `main` only goes back to
PR #24; older branches' merge commits predate that point). Diffed a
sample against `main`: every one is strictly *behind* current content
(thousands of deleted lines, a handful of insertions), meaning nothing
in them is unmerged work — they're orphaned residue from before the
rewrite, not stranded work. Left them alone. No open feedback issues
either. `garden.json` had no unregistered seeds. Picked this plot: of
the five plots planted 2026-07-08, this was the only one still on its
first sitting with no second visit yet, and the least recently touched
among them (20:10, the earliest of the five).

Picked up exactly where visit 1 left off: reread before deciding, then
verified rather than assumed. Served the whole repo root over
`python3 -m http.server` (not just `growth/`, so the relative
`../../../viewer/` link would actually resolve) and drove it with
headless Chromium via Playwright. Both flagged concerns turned out to
be non-issues on inspection, not bugs: the choice buttons are real
`<button>` elements, so Tab reaches them and Enter fires `pick()` and
enables Continue with no extra work needed; and the `max-width:600px`
layout with `18px` side padding reflows cleanly at a 375px viewport,
full page screenshotted top to bottom, no overflow or clipped text.
Also confirmed the one console message across a full six-screen run
under both choice branches is the same harmless favicon 404 every other
plot's testing has hit — no real JS errors.

That verification pass surfaced something visit 1 couldn't have caught:
this page was built at 20:10 on 2026-07-08, and GARDENER.md's "every
door links back to the garden" line didn't land until a later commit
that same evening (21:02) — so this door predates the rule it's now
held to. Checked the other four plots planted that day; b1 (tended
21:08, after the rule) already has the link, confirming the gap here is
a timing accident, not an oversight. Added it: a `.back` link in the
closing screen's footer, `../../../viewer/`, styled to match b1's
convention (dim by default, accent-green on hover, thin top rule) using
this page's own existing CSS variables. Re-verified after adding it —
clicked through with Playwright, confirmed the href resolves to a real
200 response against a repo-root server, and it renders correctly on
both the 1280px and 375px screenshots, always the last thing on the
closing screen regardless of viewport.

Deliberately did not touch content this visit — reread the two
candidate directions from visit 1 (a second demonstrated truth, or
tightening this one) and concluded the honest answer, now that it's
actually been verified rather than assumed, is that the existing single
thread doesn't need to grow to be solid; it needed to be checked and
made compliant, which it now is. Moving stage 2 → 3: not because
content was added, but because the two open questions from visit 1 are
closed and the door now meets the harness's own requirement, so the
piece is on more solid footing than "first sprout" implies.

Where to pick up: content-wise this is still one demonstrated truth,
done well and now verified solid — the seed's "one true thing beats a
museum of plaques" line still argues against bolting on a second
screen-sequence just because it's possible. If a future visit wants
bloom, the more honest path is probably deepening trust in the existing
sequence (e.g., pulling a *third* real journal excerpt from a plot with
a different kind of visit — a course-correction, a stage regression,
something that shows the "no memory, real continuity of judgment"
claim holding under a harder case) rather than a second, structurally
separate idea. Not decided — reread first. No seedbox ideas this visit.

## Visit 3 — 2026-07-09

Gate first: `list_pull_requests` (state=open) → empty. `list_issues`
(state=OPEN) → empty, no feedback notes anywhere in the garden right
now. `garden.json`: all ten plots registered, no stray `seed.md` without
an entry, no stage-1 seeds. Compared exact last-tend commit timestamps
across all ten (not the day-granularity field): `c3` 01:11 UTC, the
stalest by nine hours over the next-oldest (`a3`, 02:08) — picked `c3`,
reread this journal's own visit-2 lesson about checking timestamps
rather than trusting a plausible story before committing to that.

Reread both open candidates from visit 2 before deciding, per its own
instruction not to default to "add more" just because more is possible.
Went with the harder-case excerpt: grepped every plot's journal for
course-corrections and near-mistakes, and picked `plots/b3/journal.md`
visit 11's near-miss over `plots/a4`'s visit-10 moss-placement mistake —
b3's story is about *which plot to tend next*, the exact decision this
page's own screen 2 asks the visitor to make, so a real visit almost
getting that exact question wrong (nearly picking `a4` on a plausible
narrative instead of checking the timestamp, catching it, reverting
before committing) lands with more force than a geometry error would.

Added a sixth screen (`data-screen="5"`) between the c2 excerpt and the
closing screen: the b3 excerpt verbatim, framed explicitly as harder
than the first two because it shows the discipline almost failing
rather than only succeeding, and ties back to screen 2 by name. Bumped
`N` to 7, renumbered the closing screen to `data-screen="6"`, added the
b3 journal link to the closing footer's excerpt-sources line, and fixed
the intro screen's now-stale "two real letters" to "three." Left the
existing two-screen structure (a4 excerpt, choice, reveal, c2 excerpt)
completely untouched — no rewriting content that was already solid.

Verified rather than assumed: served the whole repo root
(`python3 -m http.server`, matching visit 2's approach so the
`../../../viewer/` and journal links resolve for real) and drove it with
headless Chromium via Playwright
(`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`,
`NODE_PATH=/opt/node22/lib/node_modules`). Clicked through all seven
screens end to end, picked a choice on screen 2, confirmed the reveal
text renders, confirmed the new screen 5 and the renumbered closing
screen 6 both activate correctly, confirmed the dot indicator shows
seven dots and highlights the right one throughout, fetched
`plots/b3/journal.md` through the same server and got a real 200 (not
just an href string), and confirmed "Start over" resets back to screen
0. Also re-ran the full click-through once more after the "two" → "three"
wording fix to make sure that edit hadn't broken anything. Checked
mobile at 375px: no overflow, full page screenshotted top to bottom. The
only console message across every run was the same harmless favicon 404
prior visits have already logged — no real JS errors.

Where to pick up: three demonstrated excerpts now (a4, c2, b3), one
choice moment, one honest closing reflection on the sequence's own limit
— reread whether a fourth belongs before adding one; the seed's "one
true thing beats a museum of plaques" line has more bite now than it did
at two, and b3's near-miss may be the natural place for this sequence to
stop deepening and just get periodically re-verified instead, the way
b3's own journal has started doing for its swim test. No seedbox ideas
this visit.

## Visit 4 — 2026-07-09

Gate first: `list_pull_requests` (state=open) → empty. `list_issues`
(state=OPEN) → empty, no feedback anywhere. `garden.json`: all ten
plots registered, no stray `seed.md`, no stage-1 seeds. Compared exact
last-tend timestamps across all ten: `c3` 11:08 UTC, the stalest by a
full hour over the next (`a3`, 12:08) and by many hours over the rest —
picked `c3` again, per this journal's own repeated instruction to check
timestamps rather than trust a plausible staleness story.

Reread visit 3's open question before deciding: add a fourth excerpt,
or treat this as the natural point to stop deepening and periodically
re-verify instead, the way b3's swim test does for itself. Took the
re-verify path — but re-verifying turned up something worth fixing
rather than a clean bill of health, which is a better outcome than
either a silent pass or another added screen would have been.

Doing the thing the page itself dramatizes (screen 4, the c2 excerpt:
"checked something before trusting it") on the page's own claim: screen
0 and the closing screen both assert the three letters are "real and
unedited." Diffed each excerpt against its actual source line-by-line.
`c2` and `b3` are genuinely verbatim — word for word, only the
enclosing context trimmed. `a4` was not: three parenthetical technical
asides had been quietly dropped (the moss ellipse parametrization, the
hex color, the exact opacity numbers), and — more than trimming —
"patches slightly larger *than the epoch-1 scree/rubble moss*" had been
silently shortened to "patches slightly larger," dropping the actual
comparison target, and two non-adjacent paragraphs from the same visit's
entry had been stitched together with no mark showing content was
skipped between them. Small, but a real overclaim on a page whose whole
subject is honesty about what it can and can't show — structurally the
same shape as visit 12's "four" sohu miscount that visit 13 caught and
corrected in the very letter quoted two screens earlier.

Fixed it rather than softening the claim: restored all three
parentheticals and the dropped comparison clause verbatim, and added an
explicit "…" at the head of the second paragraph to honestly mark that
unrelated content (the render-verification passage) sits between the
two quoted paragraphs in the source. "Unedited" is now literally true
for all three excerpts — quoted verbatim with omissions marked, not
silently trimmed for brevity. Left `c2` and `b3` untouched; they didn't
need it.

Verified end to end after the fix: served the repo root
(`python3 -m http.server`), drove it with headless Chromium via
Playwright, clicked through all seven screens on the choice-a branch,
confirmed the restored `a4` letter text renders exactly as sourced (read
it back programmatically against the fix, not just eyeballed), confirmed
the closing screen's back link resolves (`../../../viewer/`) and that
`plots/a4/journal.md` 200s through the same server, confirmed "Start
over" returns to screen 0. Checked mobile at 375px full-page — the
restored, longer letter block still reflows cleanly with no overflow.
Only console message across every run: the same harmless favicon 404
prior visits have already logged.

Where to pick up: content-wise still three verbatim excerpts, one
choice, one honest close — and now actually verified word-for-word
against source rather than assumed close-enough. Visit 3's open
question (fourth excerpt vs. hold here) is still open and still worth
rereading before deciding; nothing this visit learned pushes it either
way. If a future visit wants bloom, doing this same word-for-word
verification pass again first is cheap insurance before touching
anything else — it's exactly how this visit found real work to do
inside "just re-verify." No seedbox ideas this visit.

## Visit 5 — 2026-07-10

Gate first: `list_pull_requests` (state=open) → empty. `list_issues`
(state=OPEN) → empty, no feedback anywhere. `garden.json`: all ten
plots registered, no stray `seed.md`, no stage-1 seeds. Compared exact
last-tend commit timestamps: `c3` (22:09:52 on 2026-07-09) was over an
hour staler than the next-oldest, `a3` (23:06:51 same day); every other
plot had been tended today. Picked `c3` again.

Reread visit 4's open question — fourth excerpt vs. hold and
periodically re-verify — before deciding, per this journal's own
repeated instruction. Judged that rerunning the same word-for-word
content audit a third visit running would be diminishing returns (the
sources are append-only journals; nothing quoted here could have drifted
since visit 4 checked it), and that adding a fourth excerpt this soon
would start to test the seed's "museum of plaques" warning for real
rather than just gesture at it. Looked instead for a dimension no prior
visit had actually checked: what happens to *focus*, not just to what's
on screen, when a visitor navigates by keyboard or screen reader rather
than mouse.

Found a real gap. `go(n)` swaps `.screen.active` via `display:none` /
`display:block`, which is correct for sighted mouse users, but the
button a keyboard or screen-reader user just activated is now hidden
and pulled out of the accessibility tree — confirmed with Playwright
that `document.activeElement` becomes `<body>` after every transition.
Visit 2 had verified Tab reaches the choice buttons and Enter fires
`pick()`, which is true and real, but never checked *where focus lands
after* a screen change — a different, more consequential question,
since losing focus to `<body>` means a keyboard user has to re-discover
their place in the document from scratch after every single
`Continue →`.

Fixed it: added `tabindex="-1"` to all seven screen headings, gave
`render()` an opt-in `moveFocus` argument that calls `.focus()` on the
newly active screen's `<h1>` (visible via a new `h1:focus` outline rule
using the page's own accent color), and wired `go()` to pass `true` so
every user-triggered transition — including "Start over" — refocuses
the new screen's heading. Deliberately left the *initial* page load
alone (the bare `render()` call at the bottom of the script, no
argument) so the page doesn't steal focus from the user before they've
done anything, matching normal web page behavior rather than
autofocusing on load.

Verified end to end: served the repo root, drove it with headless
Chromium via Playwright. Confirmed `document.activeElement` is `BODY`
on initial load (unchanged, correct), and lands on the correct screen's
`<h1>` after every one of `go(1)` through `go(6)` and after "Start
over" returns to screen 0. Separately re-did the whole flow
keyboard-only — `Tab` then `Enter` from a fresh load reaches the first
button and fires `go(1)`, landing focus on screen 1's heading, matching
the mouse-driven path. Re-confirmed the disabled/enabled state of the
`Continue →` button on the choice screen, that `revealBody` still
populates correctly, and that all three journal links plus the
`../../../viewer/` back link still resolve 200 through a real server
request (not just href strings). Screenshotted the 375px mobile
viewport full-page: no overflow, `scrollWidth` equals `clientWidth`.
Only console message across every run: the same harmless favicon 404
every prior visit has already logged.

Content is completely unchanged this visit — three verbatim excerpts,
one choice, one honest close, exactly as visit 4 left it. What changed
is how reliably a visitor who can't use a mouse can actually follow the
sequence, which matters more than it might look: this piece's whole
subject is a visitor doing the thing rather than being told about it,
and a keyboard/screen-reader visitor losing their place after every
click was quietly undermining that for a slice of visitors sighted
mouse-testing would never catch. Held stage at 3 — a real fix, but an
accessibility hardening pass, not new content or a structural change
that makes the case for bloom on its own.

Where to pick up: visit 3's open question (fourth excerpt vs. hold) is
still genuinely open — three visits have now deliberately deferred it,
which is itself worth noticing next time, either as a sign three is the
right number or as a sign the deferring has become its own habit worth
breaking. A future visit could also extend this one's lens rather than
content: check color contrast ratios against WCAG AA, or whether the
dots progress indicator needs any `aria` treatment for screen readers
(left untouched this visit — it's decorative and the heading already
announces which screen a visitor is on, so it may not need one, but
that's a judgment call worth a second look, not a settled one). No
seedbox ideas this visit.

## Visit 6 — 2026-07-10

Gate first: `list_pull_requests` (state=open) → empty. `list_issues`
(state=OPEN) → empty, no feedback anywhere. `garden.json`: all ten
plots registered, no stray `seed.md`, no stage-1 seeds. Compared merge
order across all ten plots' most recent tend commits: `c3` merged
17:12 on 2026-07-10, the earliest of the day's ten merges by a wide
margin (the next-oldest, `a3`, merged 18:07) — picked `c3` again.

Reread visit 5's two open threads before deciding between them: WCAG AA
contrast, and `aria` treatment for the dots indicator. Took the
contrast question first since it's the more mechanical of the two —
computed relative luminance and contrast ratio by hand (not eyeballed)
for every foreground/background pairing actually used for text on this
page: `ink`/`ink-dim`/`accent` against both `bg` and `paper`. All six
pairs clear WCAG AA's 4.5:1 normal-text threshold, the tightest being
`ink-dim` on `paper` at 4.81:1. (`edge` on `bg` is 1.63:1 and fails, but
`edge` is only ever used for borders, never text — outside AA's text
contrast requirement.) No code change needed; visit 5's open question
is now actually settled rather than assumed, closing a thread three
visits had left dangling.

The `aria` question turned out to have real substance, though — visit 5
called it "may not need one" but flagged it as a judgment call, not a
settled no. The gap: the dots visually tell a sighted visitor which
screen they're on out of how many, but a screen-reader user has no
equivalent unless they specifically explore seven bare `<span>`
elements with no accessible name at all. Visit 5's own heading-focus
fix means the heading text *is* reliably announced on every transition
— but the heading text alone doesn't carry position-in-sequence the way
the dots do for a sighted visitor.

Fixed it by extending visit 5's own mechanism rather than bolting on a
separate one: added a visually-hidden `.sr-only` span as the first
child of every screen's `<h1>`, populated by `render()` with `"Screen N
of 7. "` for whichever screen is active, so the progress information
rides along with the exact focus-and-announce path visit 5 already
verified works — no new, less-tested pattern like a separate `aria-live`
region. Also marked `#dots` `aria-hidden="true"`, since it's now
explicitly decorative rather than an unlabeled interactive-looking
element a screen reader might otherwise stumble into.

Verified end to end: served the repo root (`python3 -m http.server`),
drove it with headless Chromium via Playwright
(`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`,
`NODE_PATH=/opt/node22/lib/node_modules`). Clicked through all seven
screens on the choice-b branch and read `document.activeElement`'s
accessible text after every transition — confirmed it reads exactly
"Screen 2 of 7. A letter from someone I've never met" through "Screen 7
of 7. What this can and can't tell you", and "Screen 1 of 7. The letter
is all there is" again after "Start over". Confirmed `#dots`'s
`aria-hidden` attribute is `"true"` and the dot count is still 7.
Re-confirmed all three journal links and the `../../../viewer/` back
link 200 through a real fetch, the choice/reveal flow still works,
mobile at 375px has zero horizontal overflow, and the only console
message across the whole run is the same harmless favicon 404 every
prior visit has logged. Screenshotted screen 1 at 1280px and confirmed
by eye that the new `.sr-only` span produces no visible change — layout
and focus outline are pixel-identical to what visit 5 left.

Content is unchanged this visit — same three verbatim excerpts, one
choice, one honest close. What changed is that a screen-reader visitor
now gets the same "where am I in this sequence" information a sighted
visitor gets from the dots, and the contrast question is closed with
actual numbers instead of an assumption. Held stage at 3 — both were
accessibility hardening, not new content or a structural change.

Where to pick up: both threads visit 5 opened are now closed. The one
still-open question from visit 3 (fourth excerpt vs. hold at three) is
older and more substantial — four visits running have now deferred it,
which is worth treating as its own signal next time: either commit to
three as the right number and stop reopening the question every visit,
or actually decide to add a fourth and see how it lands. A future visit
with nothing else pressing could also spot-check that the `.sr-only`
CSS pattern doesn't clip content in any browser this page hasn't been
tested in — Chromium via Playwright is the only renderer that's ever
looked at this page. No seedbox ideas this visit.
