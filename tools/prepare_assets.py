#!/usr/bin/env python3
"""Prepare optimized site images from the app repositories (run locally).

The app repositories are private and are not available to GitHub Actions,
so this script is run by hand on the developer's Mac and its output
(site/static/img/**) is committed. It only reads the source images.

Sources
- App icons: the published App Store artwork (iTunes Lookup artworkUrl512).
- Screenshots: raw simulator captures in each app repository whose file
  names match the screenshots currently published on the App Store.

Usage: python3 tools/prepare_assets.py --products ~/Desktop/products
"""
from __future__ import annotations

import argparse
import io
import json
import pathlib
import urllib.request

from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "site" / "static" / "img"
WIDTHS = (360, 720)

APPS = {
    "taskbit": {
        "bundle": "com.moris94.taskbit",
        "bg": "#FBF7EE",
        "shots": {
            "home": ("taskbit/AppStoreScreenshots/raw/ja/01_home.png", "taskbit/AppStoreScreenshots/raw/en-US/01_home.png"),
            "create": ("taskbit/AppStoreScreenshots/raw/ja/04_create.png", "taskbit/AppStoreScreenshots/raw/en-US/04_create.png"),
            "schedule": ("taskbit/AppStoreScreenshots/raw/ja/02_schedule.png", "taskbit/AppStoreScreenshots/raw/en-US/02_schedule.png"),
            "arrange": ("taskbit/AppStoreScreenshots/raw/ja/03_arrange.png", "taskbit/AppStoreScreenshots/raw/en-US/03_arrange.png"),
            "room": ("taskbit/AppStoreScreenshots/raw/ja/05_room.png", "taskbit/AppStoreScreenshots/raw/en-US/05_room.png"),
        },
        "og": ("home", "room"),
    },
    "geoalbum": {
        "bundle": "com.moris94.geoalbum",
        "bg": "#EEF3FA",
        "shots": {
            k: (f"geoalbum/artifacts/appstore/raw/ja/GeoAlbum Store Screenshots-{n}.png",
                f"geoalbum/artifacts/appstore/raw/en-US/GeoAlbum Store Screenshots-{n}.png")
            for k, n in {
                "album": "01-place-to-album", "rules": "02-reuse-place", "review": "03-review-and-add",
                "place": "04-photo-location", "multi": "05-work-and-hobbies", "privacy": "06-on-device",
            }.items()
        },
        "og": ("album", "place"),
    },
    "studyfocus": {
        "bundle": "com.moris94.studyfocus",
        "bg": "#F7F8F6",
        "shots": {
            k: (f"studyfocus/fastlane/screenshots/raw/ja-JP/iPhone 17 Pro Max-{n}.png",
                f"studyfocus/fastlane/screenshots/raw_en/en-US/iPhone 17 Pro Max-{n}.png")
            for k, n in {
                "focus": "01_focus", "break": "02_break", "ready": "03_ready",
                "blocked": "04_blocked", "stats": "04_statistics", "settings": "05_settings",
            }.items()
        },
        "og": ("focus", "break"),
    },
    "kaeroute": {
        "bundle": "com.moris94.kaeroute",
        "bg": "#F2F1EC",
        # The app has no English UI: the English page shows the Japanese screens.
        "shots": {
            k: (f"route/artifacts/screenshots/raw/ja/Route Screenshots-{n}.png", None)
            for k, n in {
                "route": "01-route", "offline": "02-offline", "pdf": "03-pdf",
                "create": "04-create", "alternative": "05-alternative", "settings": "06-privacy",
            }.items()
        },
        "og": ("route", "pdf"),
    },
}


def save_webp(img: Image.Image, path: pathlib.Path, width: int) -> None:
    h = round(img.height * width / img.width)
    img.resize((width, h), Image.LANCZOS).save(path, "WEBP", quality=80, method=6)


def fetch_icon(bundle: str) -> Image.Image:
    with urllib.request.urlopen(f"https://itunes.apple.com/lookup?bundleId={bundle}&country=jp", timeout=30) as r:
        url = json.load(r)["results"][0]["artworkUrl512"]
    with urllib.request.urlopen(url, timeout=30) as r:
        return Image.open(io.BytesIO(r.read())).convert("RGB")


def rounded(img: Image.Image, radius: int) -> Image.Image:
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, *img.size), radius, fill=255)
    out = img.convert("RGBA")
    out.putalpha(mask)
    return out


def og_image(app: str, cfg: dict, icon: Image.Image, shots: dict[str, Image.Image]) -> None:
    canvas = Image.new("RGB", (1200, 630), cfg["bg"])
    ic = rounded(icon.resize((220, 220), Image.LANCZOS), 50)
    canvas.paste(ic, (120, 205), ic)
    x = 560
    for key in cfg["og"]:
        s = shots[key]
        w = 270
        h = round(s.height * w / s.width)
        s = rounded(s.resize((w, h), Image.LANCZOS), 36)
        canvas.paste(s.crop((0, 0, w, 560)), (x, 70), s.crop((0, 0, w, 560)))
        x += w + 40
    canvas.save(OUT / app / "og.jpg", "JPEG", quality=84, optimize=True, progressive=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--products", required=True, type=pathlib.Path)
    args = ap.parse_args()
    for app, cfg in APPS.items():
        d = OUT / app
        d.mkdir(parents=True, exist_ok=True)
        icon = fetch_icon(cfg["bundle"])
        for size in (512, 192):
            icon.resize((size, size), Image.LANCZOS).save(d / f"icon-{size}.png", optimize=True)
        icon.resize((180, 180), Image.LANCZOS).save(d / "apple-touch-icon.png", optimize=True)
        icon.resize((96, 96), Image.LANCZOS).save(d / "icon-96.webp", "WEBP", quality=85)
        icon.resize((144, 144), Image.LANCZOS).save(d / "icon-144.webp", "WEBP", quality=85)
        rounded(icon.resize((64, 64), Image.LANCZOS), 14).save(d / "favicon.png", optimize=True)
        firsts = {}
        for key, (ja, en) in cfg["shots"].items():
            for lang, rel in (("ja", ja), ("en", en)):
                if rel is None:
                    continue
                img = Image.open(args.products / rel).convert("RGB")
                firsts.setdefault(key, img)
                for w in WIDTHS:
                    save_webp(img, d / f"{key}-{lang}-{w}.webp", w)
        og_image(app, cfg, icon, firsts)
        print("prepared", app)
    hub_images()


def hub_images() -> None:
    canvas = Image.new("RGB", (1200, 630), "#FFFFFF")
    for i, app in enumerate(APPS):
        ic = Image.open(OUT / app / "icon-512.png").convert("RGB").resize((200, 200), Image.LANCZOS)
        ic = rounded(ic, 46)
        canvas.paste(ic, (130 + i * 250, 215), ic)
    canvas.save(OUT / "hub-og.jpg", "JPEG", quality=88, optimize=True)
    fav = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
    d = ImageDraw.Draw(fav)
    d.rounded_rectangle((0, 0, 63, 63), 14, fill="#222326")
    for i, (x, y) in enumerate(((14, 14), (36, 14), (14, 36), (36, 36))):
        d.rounded_rectangle((x, y, x + 14, y + 14), 4, fill=["#98B58F", "#3478F6", "#4F5D95", "#E8590C"][i])
    fav.save(OUT / "hub-favicon.png", optimize=True)


if __name__ == "__main__":
    main()
