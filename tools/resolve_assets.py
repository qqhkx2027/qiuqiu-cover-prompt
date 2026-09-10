#!/usr/bin/env python3
"""Resolve and validate bundled image assets for qiuqiu-wechat-cover.

This script never downloads external assets.
It only reads files bundled inside this installed Skill.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]

ASSETS = {
    "identity": {
        "relative_path": "references/assets/qiuqiu-face-reference.jpg",
        "mime_type": "image/jpeg",
        "magic": b"\xff\xd8\xff",
        "description": "QIUQIU identity reference",
    },
    "style": {
        "relative_path": "references/assets/qiuqiu-style-reference.png",
        "mime_type": "image/png",
        "magic": b"\x89PNG\r\n\x1a\n",
        "description": "QIUQIU WeChat cover style reference",
    },
}


class AssetError(RuntimeError):
    pass


def resolve_asset(name, include_data_uri=False):
    spec = ASSETS[name]
    path = SKILL_ROOT / spec["relative_path"]

    if not path.is_file():
        raise AssetError(f"Bundled asset is missing: {spec['relative_path']}")

    data = path.read_bytes()

    if not data:
        raise AssetError(f"Bundled asset is empty: {spec['relative_path']}")

    if not data.startswith(spec["magic"]):
        raise AssetError(
            f"Bundled asset has invalid file signature: {spec['relative_path']}"
        )

    result = {
        "role": name,
        "description": spec["description"],
        "relative_path": spec["relative_path"],
        "absolute_path": str(path.resolve()),
        "mime_type": spec["mime_type"],
        "size_bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }

    if include_data_uri:
        encoded = base64.b64encode(data).decode("ascii")
        result["data_uri"] = f"data:{spec['mime_type']};base64,{encoded}"

    return result


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Resolve bundled qiuqiu-wechat-cover assets."
    )
    parser.add_argument(
        "--data-uri",
        action="store_true",
        help="Include base64 data URI for runtimes that cannot read local paths.",
    )
    parser.add_argument(
        "--asset",
        choices=["identity", "style", "all"],
        default="all",
    )

    args = parser.parse_args()

    names = list(ASSETS.keys()) if args.asset == "all" else [args.asset]

    try:
        assets = {name: resolve_asset(name, args.data_uri) for name in names}
    except AssetError as exc:
        print(
            json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False, indent=2)
        )
        return 1

    print(
        json.dumps(
            {
                "ok": True,
                "skill_root": str(SKILL_ROOT),
                "assets": assets,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

