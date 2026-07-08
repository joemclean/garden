# Plants — customizing a plot's sprite

Every plot is drawn with a plant sprite that matures through the six
stages. The default is the classic flower, but it's a starting point,
not a rule.

## Picking a built-in variant

Set `"plant"` on the plot's entry in `garden.json`:

```json
"b3": { "stage": 3, "plant": "kelp", ... }
```

Built-ins: `classic` (flower), `kelp`, `vine`, `fungus`, `crystal` —
the last one is there to prove the "plant" needn't be botanical at all.

## Drawing your own

Put a `plant.json` in the plot (e.g. `plots/b3/plant.json`) and point
`"plant"` at its repo-relative path:

```json
"b3": { "stage": 3, "plant": "plots/b3/plant.json", ... }
```

The file:

```json
{
  "palette": { "x": "#4f8fb0", "X": "#8fd0e8" },
  "stages": [
    ["................", "... 16 rows of 16 chars, stage 0: soil ..."],
    ["... stage 1: seed ..."],
    ["... stage 2: sprout ..."],
    ["... stage 3: growing ..."],
    ["... stage 4: bloom ..."],
    ["... stage 5: gone to seed ..."]
  ]
}
```

- Six sprites, one per stage, each 16 rows of 16 characters.
- `.` is transparent; other characters index into `palette`, which is
  merged over the built-in palette (so `m` mound-brown, `k` speck,
  `s`/`g`/`G`/`L` greens etc. are already available).
- Stage 0 is usually the shared tilled-soil rows — copy them from any
  built-in.
- Rows above row 9 shift 1px on alternate frames (the sway); the
  viewer fades all colors toward a dry tan when a plot goes untended
  for 3+ days. Both come free.
- A missing or malformed file falls back to the classic flower — the
  grid never goes blank.

The one design rule: the six stages should read as **one thing
maturing**. Anyone glancing at the grid should still see, instantly,
how far along each plot is — that's what the garden view is for.
