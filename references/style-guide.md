# Kawaii Bead Pin Photo Style Guide

This reference defines the target look for the bead safety-pin photo workflow. The approved anchor lives in this folder: `shiny-sample.png` — a **clean white square-rhinestone stud sample (user-confirmed in THIS conversation)**: silver safety pin across the top, one independent small jump ring per column hooked to the pin, a completely flat panel of PURE WHITE square-cut rhinestone studs in a regular grid — no pattern, no face, no eyes, no expression, no colored beads — with a single NEUTRAL round clear-cut diamond ornament on the pin bar center (position/texture display ONLY — never copy its shape) and dreamy sky-blue layered background (back layer sky/clouds, mid layer pin+panel, front layer bokeh glows, blurred toy silhouette at bottom right) and generic pearl/drop/tassel charms at the right end. NO subject, NO animal, NO face, NO black eyes, NO transparent orb, NO beach/sand/flower/toy as foreground subject, NO watermark — so it cannot contaminate a new subject. The anchor locks texture, bead shape/size/count/placement (the panel grid density is copied from this anchor), the layered background composition, and the fixed framework; all subject color comes only from the user's photo mosaic, and scene elements are specified by prompt only. **The pin ornament in the anchor is a NEUTRAL placeholder — its shape/color is never copied; the real pin ornament is always extracted from the CURRENT subject by prompt.**

## Fixed Bead-Grid Spec (approved pre-processing parameters)

- Mosaic pre-processing: **contain** mode is the ONLY allowed mode (keep the WHOLE image — subject AND its background; never crop the subject away; `cover`/`center` is FORBIDDEN — it center-crops the subject and destroys the silhouette/edges, this failed in a fresh install), background fill sampled from the photo's own background color (fallback `#DDF8FF`), grid **22–28** (simple → 22, detailed → 28; dolphin = 28), colors **10–12** (Median Cut quantization).
- **Full-image color fidelity (user-confirmed)**: the mosaic reproduces the ENTIRE picture's colors — the subject and its background colors stay (pink fabric background → pink base in the panel). The panel keeps that background color as its base/frame. Never let the final panel wash out to a single flat color (e.g. all-white) when the mosaic has a colored base.
- 28×28 keeps the dolphin's big silhouette (curved body, dorsal fin, tail, belly white) and the high-contrast dark eye; 12 colors merge blue-white gradients into clean bead blocks.
- **Grid 22–28 / colors 10–12 are HARD-LOCKED** (user-confirmed). Never raise grid or colors to chase detail; abstract mosaics are accepted and used as the anchor as-is.
- The pattern plate is the ONLY structural anchor; the image model must not re-interpret the original photo's structure.

## Pipeline

1. **Pre-clean (only if needed)** — readable text / numbers / watermarks / signatures removed by inpainting (area blends into surrounding background); noisy backgrounds (e.g. stripes) get a larger subject crop.
2. **Mosaic pass (approved parameters)** — run `prepare_bead_pattern.py` on the reference photo: contain mode, light background, 22–28 grid, 10–12 colors.
3. **Mosaic validation (single validation point)** — check ONLY whether the subject shape is recognizable at mosaic resolution. Abstract is accepted and used as-is; at most ONE re-run with a larger subject crop at the SAME locked grid/colors (never raise grid or colors).
4. **Bead generation (one shot)** — after validation passes, the mosaic is the only reference for subject shape; the original photo is not used for further validation. Generation passes BOTH references: `bead_pattern.png` (structure) + `shiny-sample.png` (texture + grid).

## Core Visual Formula

Three layers:

1. A reference subject quantized into a mosaic (subject AND background colors), then translated into bead art — the mosaic is the only detail source.
2. A flat square-cut rhinestone-studded panel hanging from a real-looking metal safety pin, one independent hook/ring per column.
3. A dreamy kawaii product-photo setting whose BACKGROUND SCENE follows the subject's natural context, with subject-colored charms.

The result should feel like a collectible handmade accessory photographed in a dreamy studio set themed to the subject.

## Mosaic-First Principle (highest priority)

- The mosaic (pixel plate) is the only detail source. Do NOT re-create fine details — eyes, flowers, ornaments, facial features — with beads. Whatever survives quantization as color blocks is beaded; whatever disappears stays gone.
- Never prompt for "draw eyes / keep the flower / emphasize landmarks" on the panel.
- Raise grid size or color count in the script for more fidelity — never prompt-level detail.

## Flat-Mosaic Principle (mandatory)

- The panel is a **completely flat** regular bead grid; the subject AND its background colors appear ONLY through bead colors, like pixel art. All beads on one plane.
- **COMPLETELY FLAT, NOTHING RAISED (user-confirmed)**: every square stud is a FLAT pasted tile on the same plane as the panel — NO raised/domed beads, NO 3D bumps, NO embossed relief, NO pop-out studs, NO depth illusion. Only bead-surface shine varies.
- NEVER sculpt a 3D/raised subject on top of the beads (no volumetric character/pet/doll, no relief, no embossed figure, no depth illusion inside the panel).
- Prompt additions: "flat mosaic, colors only, all beads on one plane, no 3D relief, no raised pattern, no volumetric figure".

## Bead Panel

- Hanging grid follows the approved pre-processing: 22–28 columns square grid (dolphin = 28), 10–12 colors, contain fit with background fill sampled from the photo's own background; **the panel reproduces the FULL image colors — subject plus its background color as base/frame**.
- **Beads are SQUARE CUT RHINESTONE-STUDDED, STRONG SPARKLE, DISTINCT (final output standard, user-approved)**: every bead is a **square** rhinestone/crystal stud — square-cut flat crystal tiles in a regular square grid, like square mosaic tiles. NEVER round, oval, or hexagonal beads. **The panel's bead size / row-column count / grid placement MUST match `shiny-sample.png` exactly** — the anchor is the clean white square-rhinestone stud sample whose bead density IS the approved density; never fewer, never denser, never a different row/column count.** **Every bead is clearly SEPARATED from its neighbors with visible small gaps/grout lines between them, like individual rhinestones pasted on a base with backing visible between beads — NEVER fused into a continuous sheet, NEVER a seamless glued-tile surface.** **Every stud is a FLAT tile on the same plane — NO raised/domed beads, NO 3D bumps, NO relief, NO depth.** Each bead: bright mirror highlight AND facet-like star glints, saturated luminous color, whole panel glitters like a diamond-studded mosaic, brighter and more luminous. **EVERY bead sparkles — no matte bead allowed (user-confirmed, panda v2)**: EACH AND EVERY bead must carry a bright mirror highlight AND a cross-cut facet star glint, refracting light like a cut diamond — the whole panel is brilliant and glittering, NO bead may look matte, dull, dim, or flat (not a single unsparkling bead anywhere in the panel). **Bead size / count / grid placement MUST match `shiny-sample.png` exactly** — the anchor is the clean white square-rhinestone stud sample (silver pin, per-column rings, pure-white bead grid, layered dreamy sky-blue background, generic pearl/drop/tassel charms, no animal/face/expression/colored beads), so it locks texture, shape, and grid spec WITHOUT contaminating the new subject's identity; all subject color comes only from the user's photo mosaic. Reference: `shiny-sample.png`.
- Shine is bead-surface glitter on a completely flat panel; never 3D relief, never raised subject.
- Rows and columns regular with slight natural sag.
- The photo's background color stays as the panel base/frame (pink fabric → pink base; sky → blue frame).

## Hardware

- Silver or chrome safety pin across the top.
- **Per-column hooks (strict)**: EVERY column of top-row beads has its own small metal jump ring or hook attached directly to the pin — one ring per column, a full row of rings with small gaps. Never two-corner hanging, never a shared chain.
- **No bead strings on the pin**: the pin bar carries NO string of beads. It carries exactly ONE small themed ornament **extracted from the CURRENT subject** — e.g. a tiny horse bead/charm for a horse subject, a small drop for a dolphin, a mini cake bead for a cake, a small strawberry bead for a strawberry-kitty — in subject colors.
- **Anchor placeholder rule (user-confirmed)**: the ornament shown in the texture anchor (`shiny-sample.png`) is a NEUTRAL round clear-cut diamond used ONLY to display position and texture — its shape/color is NEVER copied into outputs; every real pin ornament must be extracted from the CURRENT subject and specified by prompt (horse → tiny horse bead, rabbit → tiny rabbit bead, kitty → tiny kitty/strawberry bead).
- **Anti-contamination (user-confirmed)**: the pin ornament must NOT be a transparent round ball containing an animal, and must NOT carry over the reference sample's old subject (e.g. do not put the texture anchor's dolphin onto a non-dolphin output).

## Charms and Decorations (free variation)

- Charms and pin ornament vary around the subject; the mood stays dreamy kawaii, and the background scene follows the subject's natural context.
- Suggested directions: one larger themed charm **derived from the subject** near the right end of the pin; small accents (stars, water drops, pearl drops, bows, hearts, keys, glass beads, transparent petals); one metal filigree or bead-string tassel beside the panel. The right-end charm and the pin ornament both derive from the subject; small accents are generic.
- **Theme elements from the subject (user-confirmed, panda v2)**: the charm cluster AND the background scene must BOTH clearly derive from the subject's own identity and habitat — e.g. panda → panda-face pendant + tiny bamboo-stick charm + bamboo-leaf charms + pearls + drops + silver filigree tassel, background with blurred bamboo grove and floating bamboo leaves; kitty → kitty-face pendant + strawberry/ribbon charms; dolphin → dolphin/drop pendant + shell accents, ocean background. Generic accents (stars, drops, pearls, bows) stay small; the hero charm and scene elements must read as themed to the subject.
- All accent colors extracted from the subject palette.
- Charms hang from the pin or its right end; they never replace or mimic subject details on the panel.

## Background

- **Scene follows the subject's natural context** (user-confirmed): dolphin / sea creature → ocean / beach in blue tones; flowers / plants → forest / garden in green tones; cake / dessert → pastel dessert-shop or summer-cafe setting; strawberry / kitty → pink dreamy strawberry girlish scene; horse → meadow / pasture; panda → light-blue sky with blurred bamboo-grove silhouette and drifting bamboo leaves; pet → cozy home garden. **The background must carry the subject's own habitat elements (user-confirmed, panda v2)** — bamboo grove for panda, strawberries/flowers for kitty, waves/shells for dolphin — so the scene reads as themed to the subject, not generic. Scene colors harmonize with the subject palette.
- **Composition framework is FIXED for every output**: dreamy kawaii style, soft focus, bright and cute, gentle bokeh sparkles, shallow depth of field, square centered framing, optional blurred cute toy silhouette at bottom right.
- Avoid dark palettes, gritty texture, realistic clutter, readable text, brand marks.

## Composition

- Square, centered product framing; pin in the top third; panel in the center.
- The final should read instantly as a small handmade accessory, not a flat illustration.

## Judgment (avoid over-iteration)

- The mood, hardware structure, subject readability, square bead shape, and preserved panel base color are the acceptance criteria, not pixel-perfect read-back descriptions.
- Do not keep regenerating because a read-back description differs in minor ways; when the overall kawaii mood + structure + readability are achieved, deliver.
- **Pixel-art / flat-block failure diagnosis**: if the final image reads as flat pixel squares / plain matte blocks with no sparkle, the texture anchor (`shiny-sample.png`) was not passed or the sparkle wording was dropped — re-run with BOTH references (`bead_pattern.png` + `shiny-sample.png`) and the full prompt additions below. Never deliver a pixel-art-looking final image.

## Suggested Image Prompt Additions

- "macro product photography, handmade kawaii craft accessory"
- "[one sentence describing the mosaic subject from its color blocks — e.g. white round kitty face, two ears, strawberries on top, black dot eyes, yellow nose, whiskers, pink background — strictly reproduce this subject's color blocks from the mosaic plate, no added details]"
- "faithfully reproduce the mosaic pixel plate — full image colors including its background, no added details"
- "FLAT mosaic like pixel art, nothing protrudes, subject exists only as colored beads on one flat surface"
- "SQUARE rhinestone-studded mosaic: the panel's bead size / row-column count / grid placement match the style reference's bead grid exactly (same density as the reference sample — never fewer, never denser) — square, straight-edged, checkerboard-like regular grid (NOT round/oval/hexagonal, not a single bead round) — every bead a DISTINCT separate FLAT tile on one plane (NO raised/domed beads, NO 3D bumps, NO relief, NO depth) with visible small gaps between beads — never fused into a continuous sheet, never seamless glued tiles — bright mirror highlight AND facet-like star glints, diamond-studded glitter look, brighter and more luminous, bead grid size/count/placement matching the style reference"
- "panel base/frame color kept from the mosaic background, never washed out to all-white"
- "silver safety pin hardware, one independent jump ring per column"
- "no bead strings on the pin, only one small themed ornament extracted from the CURRENT subject in subject colors; no transparent ball with an animal, no carried-over subject from the reference"
- "background scene follows the subject's natural context (sea for dolphin, forest for flowers, dessert shop for cake, pink strawberry girlish scene for strawberry/kitty), dreamy kawaii mood"
- "charm colors extracted from the subject palette"

Negative constraints:

- "no printed poster, no flat pixel art, no embroidery, no fabric panel"
- "no beads forming eyes/flowers/details absent from the mosaic"
- "no round/oval/hexagonal beads, panel washed out to all-white"
- "no fused beads (beads merged into one continuous sheet or seamless tile surface — every bead must stay distinct with visible gaps)"
- "no bead strings on the pin, no single-point or two-corner hanging, no shared-chain hanging, no missing per-column rings"
- "no transparent ball with an animal on the pin, no carried-over subject from the reference"
- "no watermark, no logo, no readable typography"
