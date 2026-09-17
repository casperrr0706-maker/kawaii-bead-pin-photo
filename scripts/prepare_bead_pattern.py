#!/usr/bin/env python3
"""Prepare a deterministic bead-mosaic pattern plate from a reference image."""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path
from typing import Iterable, Tuple

from PIL import Image, ImageDraw


RGB = Tuple[int, int, int]


def parse_hex_color(value: str) -> RGB:
    value = value.strip().lstrip("#")
    if len(value) != 6:
        raise argparse.ArgumentTypeError("Expected a 6-digit hex color, such as #9ddff2.")
    try:
        return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]
    except ValueError as exc:
        raise argparse.ArgumentTypeError("Expected a valid hex color.") from exc


def fit_rect(image: Image.Image, width: int, height: int, mode: str, background: RGB) -> Image.Image:
    image = image.convert("RGBA")
    if mode == "cover":
        scale = max(width / image.width, height / image.height)
        new_size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
        fitted = image.resize(new_size, Image.Resampling.LANCZOS)
        left = (new_size[0] - width) // 2
        top = (new_size[1] - height) // 2
        return fitted.crop((left, top, left + width, top + height)).convert("RGBA")

    canvas = Image.new("RGBA", (width, height), (*background, 255))
    scale = min(width / image.width, height / image.height)
    new_size = (max(1, round(image.width * scale)), max(1, round(image.height * scale)))
    fitted = image.resize(new_size, Image.Resampling.LANCZOS)
    x = (width - new_size[0]) // 2
    y = (height - new_size[1]) // 2
    canvas.alpha_composite(fitted, (x, y))
    return canvas


def quantize(image: Image.Image, colors: int) -> Image.Image:
    rgb = image.convert("RGB")
    palette_source = rgb.quantize(colors=colors, method=Image.Quantize.MEDIANCUT)
    return palette_source.convert("RGB")


def luminance(color: RGB) -> float:
    r, g, b = color
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def blend(a: RGB, b: RGB, t: float) -> RGB:
    return tuple(round(a[i] * (1 - t) + b[i] * t) for i in range(3))  # type: ignore[return-value]


def draw_bead(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], color: RGB) -> None:
    x0, y0, x1, y1 = box
    radius = max(3, (x1 - x0) // 5)
    shadow = blend(color, (0, 0, 0), 0.22)
    mid = color
    highlight = blend(color, (255, 255, 255), 0.55)
    rim = blend(color, (255, 255, 255), 0.18)

    draw.rounded_rectangle((x0 + 2, y0 + 3, x1 + 2, y1 + 4), radius=radius, fill=(*shadow, 80))
    draw.rounded_rectangle((x0, y0, x1, y1), radius=radius, fill=mid, outline=rim, width=2)

    inset = max(2, (x1 - x0) // 8)
    draw.rounded_rectangle(
        (x0 + inset, y0 + inset, x1 - inset, y0 + (y1 - y0) // 2),
        radius=max(2, radius // 2),
        fill=(*highlight, 72),
    )
    spot = max(2, (x1 - x0) // 7)
    draw.ellipse((x0 + inset, y0 + inset, x0 + inset + spot, y0 + inset + spot), fill=(255, 255, 255, 170))


def make_pixel_plate(grid_img: Image.Image, cell: int) -> Image.Image:
    return grid_img.resize((grid_img.width * cell, grid_img.height * cell), Image.Resampling.NEAREST)


def make_bead_preview(grid_img: Image.Image, cell: int, gap: int, background: RGB) -> Image.Image:
    width, height = grid_img.size
    margin = max(10, cell // 2)
    out_w = width * cell + (width - 1) * gap + margin * 2
    out_h = height * cell + (height - 1) * gap + margin * 2
    canvas = Image.new("RGBA", (out_w, out_h), (*background, 255))
    draw = ImageDraw.Draw(canvas, "RGBA")

    for y in range(height):
        for x in range(width):
            color = grid_img.getpixel((x, y))
            x0 = margin + x * (cell + gap)
            y0 = margin + y * (cell + gap)
            draw_bead(draw, (x0, y0, x0 + cell - 1, y0 + cell - 1), color)

    return canvas


def make_palette(colors: Iterable[tuple[RGB, int]], swatch: int = 72) -> Image.Image:
    colors = list(colors)
    cols = min(6, max(1, len(colors)))
    rows = math.ceil(len(colors) / cols)
    canvas = Image.new("RGB", (cols * swatch, rows * swatch), (250, 250, 250))
    draw = ImageDraw.Draw(canvas)

    for idx, (color, _) in enumerate(colors):
        x = (idx % cols) * swatch
        y = (idx // cols) * swatch
        draw.rectangle((x, y, x + swatch, y + swatch), fill=color)
        border = blend(color, (0, 0, 0), 0.35) if luminance(color) > 180 else blend(color, (255, 255, 255), 0.35)
        draw.rectangle((x, y, x + swatch - 1, y + swatch - 1), outline=border, width=2)

    return canvas


def count_colors(image: Image.Image) -> list[tuple[RGB, int]]:
    pixel_data = image.get_flattened_data() if hasattr(image, "get_flattened_data") else image.getdata()
    counts: Counter[RGB] = Counter(pixel_data)
    return counts.most_common()


def main() -> None:
    parser = argparse.ArgumentParser(description="Create bead mosaic pattern assets from an image.")
    parser.add_argument("image", type=Path, help="Reference image path.")
    parser.add_argument("--out-dir", type=Path, default=Path("bead-pattern-output"), help="Output directory.")
    parser.add_argument("--grid", type=int, default=48, help="Bead grid columns (fixed spec: 48).")
    parser.add_argument("--grid-h", type=int, default=0, help="Bead grid rows; defaults to --grid (square). Fixed spec: 40.")
    parser.add_argument("--colors", type=int, default=12, help="Maximum palette colors.")
    parser.add_argument("--cell", type=int, default=44, help="Preview cell size in pixels.")
    parser.add_argument("--gap", type=int, default=3, help="Preview gap between beads in pixels.")
    parser.add_argument("--mode", choices=("contain", "cover"), default="contain", help="Fit image into square or center-crop it.")
    parser.add_argument("--background", type=parse_hex_color, default=parse_hex_color("#9DDEF4"), help="Contain-mode background color.")
    args = parser.parse_args()

    if args.grid < 8 or args.grid > 64:
        raise SystemExit("--grid must be between 8 and 64.")
    grid_h = args.grid_h if args.grid_h > 0 else args.grid
    if grid_h < 8 or grid_h > 64:
        raise SystemExit("--grid-h must be between 8 and 64.")
    if args.colors < 2 or args.colors > 32:
        raise SystemExit("--colors must be between 2 and 32.")

    args.out_dir.mkdir(parents=True, exist_ok=True)

    original = Image.open(args.image)
    square = fit_rect(original, args.grid, grid_h, args.mode, args.background)
    grid_img = quantize(square, args.colors)

    pixel_plate = make_pixel_plate(grid_img, args.cell)
    bead_preview = make_bead_preview(grid_img, args.cell, args.gap, args.background)
    colors = count_colors(grid_img)
    palette = make_palette(colors)

    pixel_path = args.out_dir / "pixel_plate.png"
    bead_path = args.out_dir / "bead_pattern.png"
    palette_path = args.out_dir / "palette.png"
    manifest_path = args.out_dir / "manifest.json"

    pixel_plate.save(pixel_path)
    bead_preview.save(bead_path)
    palette.save(palette_path)

    manifest = {
        "source": str(args.image),
        "grid": args.grid,
        "colors_requested": args.colors,
        "mode": args.mode,
        "background": "#{:02X}{:02X}{:02X}".format(*args.background),
        "outputs": {
            "pixel_plate": str(pixel_path),
            "bead_pattern": str(bead_path),
            "palette": str(palette_path),
        },
        "palette": [
            {"hex": "#{:02X}{:02X}{:02X}".format(*color), "count": count}
            for color, count in colors
        ],
    }
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(json.dumps(manifest["outputs"], indent=2))


if __name__ == "__main__":
    main()
