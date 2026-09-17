# Kawaii Bead Pin Photo Style Guide

This reference defines the target look for the bead safety-pin photo workflow. The approved mood sample lives in this folder (`approved-sample.png`) — a beach-side summer scene with a bead mosaic panel, small flower on the pin, and shell/flower/star charms.

## Fixed Bead-Grid Spec (approved pre-processing parameters)

- Mosaic pre-processing: **contain** mode (never crop the subject), light background fill (e.g. `#DDF8FF`), grid **22–28** (simple → 22, detailed → 28; dolphin = 28), colors **10–12** (Median Cut quantization).
- 28×28 keeps the dolphin's big silhouette (curved body, dorsal fin, tail, belly white) and the high-contrast dark eye; 12 colors merge blue-white gradients into clean bead blocks.
- **Grid 22–28 / colors 10–12 are HARD-LOCKED** (user-confirmed). Never raise grid or colors to chase detail; abstract mosaics are accepted and used as the anchor as-is.
- The pattern plate is the ONLY structural anchor; the image model must not re-interpret the original photo's structure.

## Pipeline

1. **Mosaic pass (approved parameters)** — run `prepare_bead_pattern.py` on the reference photo: contain mode, light background, 22–28 grid, 10–12 colors.
2. **Mosaic validation (single validation point)** — check ONLY whether the subject shape is recognizable at mosaic resolution. Abstract is accepted and used as-is; at most ONE re-run with a larger subject crop at the SAME locked grid/colors (never raise grid or colors).
3. **Bead generation** — after validation passes, the mosaic is the only reference for subject shape; the original photo is not used for further validation.

## Core Visual Formula

Three layers:

1. A reference subject quantized into a mosaic, then translated into bead art — the mosaic is the only detail source.
2. A physical bead panel hanging from a real-looking metal safety pin, one independent hook/ring per column.
3. A dreamy kawaii summer/beach product-photo setting with subject-colored charms.

The result should feel like a collectible handmade accessory photographed in a playful beach studio set.

## Mosaic-First Principle (highest priority)

- The mosaic (pixel plate) is the only detail source. Do NOT re-create fine details — eyes, flowers, ornaments, facial features — with beads. Whatever survives quantization as color blocks is beaded; whatever disappears stays gone.
- Never prompt for "draw eyes / keep the flower / emphasize landmarks" on the panel.
- Raise grid size or color count in the script for more fidelity — never prompt-level detail.

## Flat-Mosaic Principle (mandatory)

- The panel is a **completely flat** regular bead grid; the subject appears ONLY through bead colors, like pixel art. All beads on one plane.
- NEVER sculpt a 3D/raised subject on top of the beads (no volumetric character/pet/doll, no relief, no embossed figure, no depth illusion inside the panel).
- Reference files: `flat-style-A.png` ~ `flat-style-D.png` show the approved flat look.
- Prompt additions: "flat mosaic, colors only, all beads on one plane, no 3D relief, no raised pattern, no volumetric figure".

## Bead Panel

- Hanging grid follows the approved pre-processing: 22–28 columns square grid (dolphin = 28), 10–12 colors, contain fit with light background fill.
- **Beads are RHINESTONE-STUDDED, SQUARE CUT (final output standard, user-approved)**: every bead is a SQUARE rhinestone/crystal stud; the whole panel glitters like a diamond-studded mosaic. Each bead: bright mirror highlight, facet-like sparkle glints, saturated luminous color. **Bead size / count / grid placement must match `shiny-sample.png` exactly** (same rows & columns, same bead proportions, same panel position — the anchor now is the user-approved abstract color-block sample with square studs and NO subject, so it also locks the grid spec without contaminating the new subject). Reference: `shiny-sample.png` and `approved-sample.png`.
- Shine is bead-surface glitter on a completely flat panel; never 3D relief, never raised subject.
- Rows and columns regular with slight natural sag.
- Optional framing border color derived from the photo background (sea/sky → cyan/blue) as a mosaic-level block.

## Hardware

- Silver or chrome safety pin across the top.
- **Per-column hooks (strict)**: EVERY column of top-row beads has its own small metal jump ring or hook attached directly to the pin — one ring per column, a full row of rings with small gaps. Never two-corner hanging, never a shared chain.
- **No bead strings on the pin**: the pin bar carries NO string of beads. It may carry ONE small themed ornament drawn from the subject — e.g. a tiny horse bead/charm for a horse subject, a small drop for a dolphin — in subject colors.
- Tiny loops or bead-string endings along the panel's lower edge are fine.

## Charms and Decorations (free variation)

- Charms, pin ornament, and background may vary creatively around the subject; only the mood must match (dreamy kawaii summer/beach).
- Suggested directions: one larger themed charm **derived from the subject** near the right end of the pin; small accents (stars, water drops, pearl drops, bows, hearts, keys, glass beads, transparent petals); one metal filigree or bead-string tassel beside the panel. The right-end charm and the pin ornament both derive from the subject; small accents are generic.
- All accent colors extracted from the subject palette.
- Charms hang from the pin or its right end; they never replace or mimic subject details on the panel.

## Background

- Dreamy kawaii summer / tropical beach, decorative but secondary: bright blue sky, warm sand, flowers, palm leaves, blurred bokeh, sparkles, diffuse sunlight.
- Optional cute toy silhouettes (e.g. Hello Kitty, teddy bear) softly blurred in the background.
- Soft focus, shallow depth of field, pastel gradients.
- Avoid dark palettes, gritty texture, realistic clutter, readable text, brand marks.

## Composition

- Square, centered product framing; pin in the top third; panel in the center.
- The final should read instantly as a small handmade accessory, not a flat illustration.

## Judgment (avoid over-iteration)

- The mood, hardware structure, and subject readability are the acceptance criteria, not pixel-perfect read-back descriptions.
- Do not keep regenerating because a read-back description differs in minor ways; when the overall kawaii mood + structure + readability are achieved, deliver.

## Suggested Image Prompt Additions

- "macro product photography, handmade kawaii craft accessory"
- "faithfully reproduce the mosaic pixel plate, no added details"
- "shiny rhinestone-studded mosaic, SQUARE-cut crystal studs, bright mirror highlight per bead, facet-like glints, diamond-studded glitter look, bead grid size/count/placement matching the style reference"
- "silver safety pin hardware, one independent jump ring per column"
- "no bead strings on the pin, only one small themed ornament in subject colors"
- "freely vary charms and background around the subject, dreamy kawaii summer beach mood"
- "charm colors extracted from the subject palette"

Negative constraints:

- "no printed poster, no flat pixel art, no embroidery, no fabric panel"
- "no beads forming eyes/flowers/details absent from the mosaic"
- "no bead strings on the pin, no single-point or two-corner hanging, no shared-chain hanging, no missing per-column rings"
- "no watermark, no logo, no readable typography"
