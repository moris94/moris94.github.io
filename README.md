# moris94.github.io

Official sites for iPhone apps by Ryo Morishita, published with GitHub Pages at https://moris94.github.io/.

- TaskBit — `/taskbit/en/`, `/taskbit/ja/`
- GeoAlbum — `/geoalbum/en/`, `/geoalbum/ja/`
- Study Focus (勉強集中) — `/studyfocus/en/`, `/studyfocus/ja/`
- Kaeroute (カエルート) — `/kaeroute/ja/`, `/kaeroute/en/`

```sh
python3 site/build.py      # writes dist/
python3 site/validate.py   # SEO and link checks
```

Pushing to `main` builds, validates and deploys with GitHub Actions (`.github/workflows/pages.yml`).
Docs: `docs/website/` (app facts and sources, design concept, operations).
