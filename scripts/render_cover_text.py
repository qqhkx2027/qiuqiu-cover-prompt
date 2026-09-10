#!/usr/bin/env python3
"""Render confirmed cover copy on a clean cover background.

The script deliberately requires an explicit output path and refuses paths
inside the skill repository, so generated media stays outside the package.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent.parent
TARGET_SIZE = (1880, 800)
FONT_CANDIDATES = (
    "/System/Library/Fonts/PingFang.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/STHeiti Light.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
)


def font_path(explicit: str | None) -> Path:
    candidates = ([explicit] if explicit else []) + list(FONT_CANDIDATES)
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return Path(candidate)
    raise SystemExit("找不到中文字体，请用 --font 指定本机字体文件。")


def load_copy(args: argparse.Namespace) -> dict[str, str]:
    values = {"hook": args.hook or "", "title": args.title or "", "subtitle": args.subtitle or ""}
    if args.copy_json:
        values.update(json.loads(Path(args.copy_json).read_text(encoding="utf-8")))
    if not values["title"]:
        raise SystemExit("必须提供主标题：--title 或 --copy-json。")
    return values


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="无字或少字的封面底图")
    parser.add_argument("--output", type=Path, required=True, help="项目目录之外的输出路径")
    parser.add_argument("--copy-json", type=Path, help="包含 hook/title/subtitle 的 JSON 文件")
    parser.add_argument("--hook")
    parser.add_argument("--title")
    parser.add_argument("--subtitle")
    parser.add_argument("--font", help="本机中文字体路径")
    parser.add_argument("--font-size", type=int, default=92)
    args = parser.parse_args()

    source = args.input.resolve()
    output = args.output.resolve()
    if not source.is_file():
        raise SystemExit(f"找不到底图：{source}")
    try:
        output.relative_to(ROOT)
    except ValueError:
        pass
    else:
        raise SystemExit(f"输出必须位于项目目录之外：{ROOT}")

    image = Image.open(source).convert("RGBA")
    width, height = image.size
    ratio = width / height
    if abs(ratio - 2.35) > 0.10:
        raise SystemExit(f"底图比例为 {ratio:.3f}，无法安全裁切到 2.35:1。")
    target_ratio = TARGET_SIZE[0] / TARGET_SIZE[1]
    if abs(ratio - target_ratio) > 0.001 or image.size != TARGET_SIZE:
        if ratio > target_ratio:
            crop_width = round(height * target_ratio)
            left_crop = (width - crop_width) // 2
            image = image.crop((left_crop, 0, left_crop + crop_width, height))
        else:
            crop_height = round(width / target_ratio)
            top_crop = (height - crop_height) // 2
            image = image.crop((0, top_crop, width, top_crop + crop_height))
        image = image.resize(TARGET_SIZE, Image.Resampling.LANCZOS)
        width, height = image.size

    copy = load_copy(args)
    font = font_path(args.font)
    draw = ImageDraw.Draw(image)
    title_font = ImageFont.truetype(str(font), args.font_size)
    hook_font = ImageFont.truetype(str(font), max(28, args.font_size // 2))
    subtitle_font = ImageFont.truetype(str(font), max(24, args.font_size // 3))

    left = int(width * 0.06)
    max_text_width = int(width * 0.48)
    y = int(height * 0.17)
    shadow = (49, 22, 58, 230)
    cream = (255, 235, 166, 255)
    pink = (255, 153, 194, 255)

    def draw_line(text: str, used_font: ImageFont.FreeTypeFont, fill: tuple[int, ...], y_pos: int) -> int:
        if not text:
            return y_pos
        box = draw.textbbox((0, 0), text, font=used_font, stroke_width=3)
        if box[2] - box[0] > max_text_width:
            raise SystemExit(f"文字超出左侧安全区，请缩短：{text}")
        draw.text((left + 5, y_pos + 6), text, font=used_font, fill=shadow, stroke_width=6, stroke_fill=shadow)
        draw.text((left, y_pos), text, font=used_font, fill=fill, stroke_width=3, stroke_fill=shadow)
        return y_pos + box[3] - box[1] + 18

    y = draw_line(copy["hook"], hook_font, pink, y)
    y = draw_line(copy["title"], title_font, cream, y)
    draw_line(copy["subtitle"], subtitle_font, cream, y + 4)

    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output)
    print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
