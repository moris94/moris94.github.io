#!/usr/bin/env python3
"""Build the static official sites into dist/ (Python 3.10+, standard library only).

Usage: python3 site/build.py [--base-url https://moris94.github.io] [--out dist]
"""
from __future__ import annotations

import argparse
import hashlib
import html
import importlib.util
import json
import pathlib
import shutil
import struct

SITE = pathlib.Path(__file__).resolve().parent
ROOT = SITE.parent
APP_ORDER = ("taskbit", "geoalbum", "studyfocus", "kaeroute")
DEVELOPER = "Ryo Morishita"
SUPPORT_EMAIL = "shunmemo.support@gmail.com"

UI = {
    "ja": {
        "skip": "本文へ移動",
        "features": "機能",
        "howto": "使い方",
        "faq": "よくある質問",
        "support": "サポート",
        "privacy": "プライバシー",
        "store": "App Storeでダウンロード",
        "store_view": "App Storeで見る",
        "facts": "概要",
        "fit": "向いている人",
        "limits": "できないこと・注意点",
        "other_apps": "Ryo Morishitaのアプリ",
        "developer": "開発・提供",
        "checked": "掲載情報の確認日",
        "home": "トップ",
        "lang_name": "日本語",
        "lang_label": "言語",
        "nav_label": "サイト内",
        "official_policy": "App Storeに登録しているポリシー全文",
        "contact": "お問い合わせ",
        "back_to_app": "アプリの紹介へ戻る",
        "locale": "ja_JP",
        "date_fmt": lambda d: f"{int(d[:4])}年{int(d[5:7])}月{int(d[8:10])}日",
    },
    "en": {
        "skip": "Skip to content",
        "features": "Features",
        "howto": "How it works",
        "faq": "FAQ",
        "support": "Support",
        "privacy": "Privacy",
        "store": "Download on the App Store",
        "store_view": "View on the App Store",
        "facts": "At a glance",
        "fit": "Who it's for",
        "limits": "Limits and notes",
        "other_apps": "Apps by Ryo Morishita",
        "developer": "Developer",
        "checked": "Information checked on",
        "home": "Home",
        "lang_name": "English",
        "lang_label": "Language",
        "nav_label": "On this site",
        "official_policy": "Full policy registered on the App Store",
        "contact": "Contact",
        "back_to_app": "Back to the app overview",
        "locale": "en_US",
        "date_fmt": lambda d: (lambda x: f"{x:%B} {x.day}, {x.year}")(__import__("datetime").date.fromisoformat(d)),
    },
}
OTHER = {"ja": "en", "en": "ja"}
LANG_SWITCH = {"ja": "English", "en": "日本語"}


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def load_app(slug: str) -> dict:
    spec = importlib.util.spec_from_file_location(slug, SITE / "content" / f"{slug}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.APP


def webp_size(path: pathlib.Path) -> tuple[int, int]:
    b = path.read_bytes()[:30]
    kind = b[12:16]
    if kind == b"VP8 ":
        w, h = struct.unpack("<HH", b[26:30])
        return w & 0x3FFF, h & 0x3FFF
    if kind == b"VP8L":
        bits = int.from_bytes(b[21:25], "little")
        return (bits & 0x3FFF) + 1, ((bits >> 14) & 0x3FFF) + 1
    if kind == b"VP8X":
        return int.from_bytes(b[24:27], "little") + 1, int.from_bytes(b[27:30], "little") + 1
    raise ValueError(f"unknown webp: {path}")


class Builder:
    def __init__(self, base: str, out: pathlib.Path):
        self.base = base.rstrip("/")
        self.out = out
        self.apps = {s: load_app(s) for s in APP_ORDER}
        self.pages: list[dict] = []  # for sitemap
        css = (SITE / "static" / "css" / "site.css").read_bytes()
        self.css_href = "/static/css/site.css?v=" + hashlib.sha256(css).hexdigest()[:10]

    # ---------- helpers
    def abs(self, path: str) -> str:
        return self.base + path

    def img(self, slug: str, key: str, lang: str, alt: str, *, eager: bool = False, sizes: str = "(min-width: 900px) 320px, 72vw") -> str:
        app = self.apps[slug]
        shot_lang = lang if lang in app.get("shot_langs", ("ja", "en")) else app.get("shot_langs", ("ja",))[0]
        p360 = f"/static/img/{slug}/{key}-{shot_lang}-360.webp"
        p720 = f"/static/img/{slug}/{key}-{shot_lang}-720.webp"
        w, h = webp_size(SITE / p360.lstrip("/"))
        loading = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
        return (f'<img class="shot" src="{p720}" srcset="{p360} 360w, {p720} 720w" sizes="{sizes}" '
                f'width="{w}" height="{h}" alt="{esc(alt)}" {loading}>')

    def write(self, path: str, content: str) -> None:
        target = self.out / path.lstrip("/")
        if path.endswith("/"):
            target = target / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    # ---------- shared layout
    def head(self, *, lang: str, title: str, description: str, path: str, alternates: dict[str, str] | None,
             x_default: str | None, icon_dir: str, og_image: str, og_alt: str, jsonld: dict | None,
             noindex: bool = False, extra: str = "", theme_color: str = "#ffffff") -> str:
        u = UI[lang]
        parts = [
            "<!doctype html>",
            f'<html lang="{lang}">',
            "<head>",
            '<meta charset="utf-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1">',
            f"<title>{esc(title)}</title>",
            f'<meta name="description" content="{esc(description)}">',
        ]
        if noindex:
            parts.append('<meta name="robots" content="noindex, follow">')
        else:
            parts.append(f'<link rel="canonical" href="{self.abs(path)}">')
        if alternates and not noindex:
            for l, p in alternates.items():
                parts.append(f'<link rel="alternate" hreflang="{l}" href="{self.abs(p)}">')
            if x_default:
                parts.append(f'<link rel="alternate" hreflang="x-default" href="{self.abs(x_default)}">')
        parts += [
            f'<meta name="theme-color" content="{theme_color}">',
            f'<link rel="icon" href="{icon_dir}/favicon.png" type="image/png">',
            f'<link rel="apple-touch-icon" href="{icon_dir}/apple-touch-icon.png">',
            f'<link rel="stylesheet" href="{self.css_href}">',
            '<meta property="og:type" content="website">',
            f'<meta property="og:title" content="{esc(title)}">',
            f'<meta property="og:description" content="{esc(description)}">',
            f'<meta property="og:url" content="{self.abs(path)}">',
            f'<meta property="og:image" content="{self.abs(og_image)}">',
            '<meta property="og:image:width" content="1200">',
            '<meta property="og:image:height" content="630">',
            f'<meta property="og:image:alt" content="{esc(og_alt)}">',
            f'<meta property="og:locale" content="{u["locale"]}">',
        ]
        if alternates and OTHER[lang] in alternates:
            parts.append(f'<meta property="og:locale:alternate" content="{UI[OTHER[lang]]["locale"]}">')
        parts += [
            '<meta property="og:site_name" content="Ryo Morishita Apps">',
            '<meta name="twitter:card" content="summary_large_image">',
            f'<meta name="twitter:title" content="{esc(title)}">',
            f'<meta name="twitter:description" content="{esc(description)}">',
            f'<meta name="twitter:image" content="{self.abs(og_image)}">',
        ]
        if extra:
            parts.append(extra)
        if jsonld:
            data = json.dumps(jsonld, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
            parts.append(f'<script type="application/ld+json">{data}</script>')
        parts.append("</head>")
        return "\n".join(parts)

    def app_header(self, app: dict, lang: str, alt_path: str | None) -> str:
        u, t, slug = UI[lang], app["t"][lang], app["slug"]
        top = f"/{slug}/{lang}/"
        switch = ""
        if alt_path:
            o = OTHER[lang]
            switch = (f'<a class="lang" href="{alt_path}" hreflang="{o}" lang="{o}">{LANG_SWITCH[lang]}</a>')
        return f"""<a class="skip" href="#main">{u['skip']}</a>
<header class="site-header">
  <div class="wrap header-row">
    <a class="brand" href="{top}"><img src="/static/img/{slug}/icon-96.webp" width="36" height="36" alt=""><span>{esc(t['name'])}</span></a>
    <nav aria-label="{u['nav_label']}">
      <ul>
        <li><a href="{top}#features">{u['features']}</a></li>
        <li><a href="{top}#faq">{u['faq']}</a></li>
        <li><a href="/{slug}/{lang}/support/">{u['support']}</a></li>
      </ul>
    </nav>
    {switch}
  </div>
</header>"""

    def footer(self, lang: str, current: str | None = None) -> str:
        u = UI[lang]
        items = []
        for s in APP_ORDER:
            a = self.apps[s]
            l = lang if lang in a["langs"] else a["primary_lang"]
            cur = ' aria-current="true"' if s == current else ""
            items.append(f'<li><a href="/{s}/{l}/"{cur}>{esc(a["t"][l]["name"])}</a></li>')
        hub = "/" if lang == "en" else "/ja/"
        extra = ""
        if current:
            a = self.apps[current]
            extra = (f'<p class="foot-links"><a href="/{current}/{lang}/privacy/">{u["privacy"]}</a>'
                     f'<a href="/{current}/{lang}/support/">{u["support"]}</a></p>')
        return f"""<footer class="site-footer">
  <div class="wrap">
    {extra}
    <p class="foot-title"><a href="{hub}">{u['other_apps']}</a></p>
    <ul class="foot-apps">{''.join(items)}</ul>
    <p class="foot-note">{u['developer']}: {DEVELOPER}{'。' if lang == 'ja' else '. '}{'掲載しているのはApp Storeで公開中の機能です。' if lang == 'ja' else 'This site describes features available in the current App Store version.'}</p>
  </div>
</footer>"""

    def store_button(self, app: dict, lang: str, label_key: str = "store") -> str:
        return (f'<a class="store-btn" href="{app["store_url"][lang]}" >'
                f'{UI[lang][label_key]}</a>')

    # ---------- JSON-LD
    def graph_common(self) -> list[dict]:
        return [
            {"@type": "Person", "@id": self.abs("/#developer"), "name": DEVELOPER, "url": self.abs("/")},
            {"@type": "WebSite", "@id": self.abs("/#website"), "url": self.abs("/"), "name": "Ryo Morishita Apps",
             "publisher": {"@id": self.abs("/#developer")}, "inLanguage": ["en", "ja"]},
        ]

    def app_jsonld(self, app: dict, lang: str, path: str) -> dict:
        t, slug = app["t"][lang], app["slug"]
        offers = [{"@type": "Offer", "name": name, "price": price, "priceCurrency": cur,
                   **({"description": desc} if desc else {})}
                  for name, price, cur, desc in app["offers"][lang]]
        app_node = {
            "@type": "MobileApplication",
            "@id": self.abs(f"/{slug}/{lang}/#app"),
            "name": t["name"],
            **({"alternateName": t["store_name"]} if t["store_name"] != t["name"] else {}),
            "description": t["description"],
            "url": self.abs(path),
            "applicationCategory": app["schema_category"],
            "operatingSystem": f"iOS {app['min_ios']} or later",
            "softwareVersion": app["version"],
            "image": self.abs(f"/static/img/{slug}/icon-512.png"),
            "screenshot": [self.abs(f"/static/img/{slug}/{k}-{lang if lang in app.get('shot_langs', ('ja','en')) else app.get('shot_langs', ('ja',))[0]}-720.webp") for k, _ in t["gallery"][:3]],
            "installUrl": app["store_url"][lang],
            "downloadUrl": app["store_url"][lang],
            "offers": offers,
            "author": {"@id": self.abs("/#developer")},
            "publisher": {"@id": self.abs("/#developer")},
            "inLanguage": app["ui_languages"],
            "sameAs": sorted(set(app["store_url"].values())) + [self.abs(f"/{slug}/{o}/") for o in app["langs"] if o != lang],
        }
        page = {"@type": "WebPage", "@id": self.abs(path), "url": self.abs(path), "name": t["title"],
                "description": t["description"], "inLanguage": lang, "about": {"@id": self.abs(f"/{slug}/{lang}/#app")},
                "isPartOf": {"@id": self.abs("/#website")}, "dateModified": app["checked"]}
        return {"@context": "https://schema.org", "@graph": [app_node, page, *self.graph_common()]}

    def sub_jsonld(self, app: dict, lang: str, path: str, title: str, description: str) -> dict:
        slug = app["slug"]
        crumbs = {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": app["t"][lang]["name"], "item": self.abs(f"/{slug}/{lang}/")},
            {"@type": "ListItem", "position": 2, "name": title, "item": self.abs(path)},
        ]}
        page = {"@type": "WebPage", "@id": self.abs(path), "url": self.abs(path), "name": title,
                "description": description, "inLanguage": lang, "about": {"@id": self.abs(f"/{slug}/{lang}/#app")},
                "isPartOf": {"@id": self.abs("/#website")}, "dateModified": app["checked"]}
        return {"@context": "https://schema.org", "@graph": [page, crumbs, *self.graph_common()]}

    # ---------- pages
    def app_pages(self, app: dict) -> None:
        slug = app["slug"]
        langs = app["langs"]
        xdef = app["primary_lang"]
        for lang in langs:
            alts = {l: f"/{slug}/{l}/" for l in langs}
            self.app_index(app, lang, alts, f"/{slug}/{xdef}/")
            for kind in ("privacy", "support"):
                self.app_sub(app, lang, kind, {l: f"/{slug}/{l}/{kind}/" for l in langs}, f"/{slug}/{xdef}/{kind}/")
        self.app_chooser(app)

    def common_head(self, app, lang, title, description, path, alts, xdef, jsonld, extra=""):
        slug = app["slug"]
        return self.head(lang=lang, title=title, description=description, path=path, alternates=alts,
                         x_default=xdef, icon_dir=f"/static/img/{slug}", og_image=f"/static/img/{slug}/og.jpg",
                         og_alt=app["t"][lang]["og_alt"], jsonld=jsonld, extra=extra, theme_color=app["theme_color"])

    def app_index(self, app: dict, lang: str, alts: dict, xdef: str) -> None:
        u, t, slug = UI[lang], app["t"][lang], app["slug"]
        path = f"/{slug}/{lang}/"
        smart = f'<meta name="apple-itunes-app" content="app-id={app["store_id"]}">'
        head = self.common_head(app, lang, t["title"], t["description"], path, alts, xdef,
                                self.app_jsonld(app, lang, path), smart)
        alt_path = alts.get(OTHER[lang])

        facts = "".join(f"<div><dt>{esc(k)}</dt><dd>{v}</dd></div>" for k, v in t["facts"])
        facts += f'<div><dt>{u["checked"]}</dt><dd><time datetime="{app["checked"]}">{u["date_fmt"](app["checked"])}</time></dd></div>'

        feats = []
        for f in t["features"]:
            shot = f'<figure class="feature-shot">{self.img(slug, f["shot"], lang, f["alt"])}</figure>' if f.get("shot") else ""
            feats.append(f'<article class="feature" id="{f["id"]}">\n<div class="feature-text"><h3>{esc(f["h"])}</h3>{f["body"]}</div>{shot}</article>')

        steps = "".join(f"<li><h3>{esc(h)}</h3><p>{b}</p></li>" for h, b in t["steps"]["items"])
        fit = "".join(f"<li>{x}</li>" for x in t["fit"])
        limits = "".join(f"<li>{x}</li>" for x in t["limits"])
        faq = "".join(f'<div class="qa" id="{qid}"><h3>{esc(q)}</h3>{a}</div>' for qid, q, a in t["faq"])
        gallery = "".join(f"<li>{self.img(slug, k, lang, alt, sizes='(min-width: 900px) 220px, 60vw')}</li>" for k, alt in t["gallery"])
        shot_note = f'<p class="note">{t["shot_note"]}</p>' if t.get("shot_note") else ""
        notice = ""
        if t.get("notice"):
            nh, nb = t["notice"]
            notice = f'''<section class="notice-section" aria-labelledby="notice-h"><div class="wrap"><div class="notice"><h2 id="notice-h">{esc(nh)}</h2>{nb}</div></div></section>'''

        body = f"""<body class="t-{app['theme']}">
{self.app_header(app, lang, alt_path)}
<main id="main">
  <section class="hero">
    <div class="wrap hero-grid">
      <div class="hero-text">
        <p class="hero-app"{' lang="ja"' if lang == "en" and t["store_name"] != t["name"] and not t["store_name"].isascii() else ""}>{esc(t['store_name'])}</p>
        <h1>{t['headline']}</h1>
        <p class="lead">{t['lead']}</p>
        <div class="cta">{self.store_button(app, lang)}<p class="price-note">{t['price_note']}</p></div>
      </div>
      <div class="hero-art">{t.get('hero_art', '')}{self.img(slug, t['hero_shot'], lang, t['hero_alt'], eager=True, sizes='(min-width: 900px) 340px, 72vw')}</div>
    </div>
  </section>

  <section class="facts-section" aria-labelledby="facts-h">
    <div class="wrap">
      <h2 id="facts-h">{u['facts']}</h2>
      <p class="summary">{t['summary']}</p>
      <dl class="facts">{facts}</dl>
    </div>
  </section>

  {notice}
  <section class="features" id="features" aria-labelledby="features-h">
    <div class="wrap">
      <h2 id="features-h">{esc(t['features_h'])}</h2>
      {''.join(feats)}
    </div>
  </section>

  <section class="steps-section" id="howto" aria-labelledby="howto-h">
    <div class="wrap">
      <h2 id="howto-h">{esc(t['steps']['h'])}</h2>
      <ol class="steps">{steps}</ol>
    </div>
  </section>

  <section class="gallery-section" aria-labelledby="gallery-h">
    <div class="wrap">
      <h2 id="gallery-h">{esc(t['gallery_h'])}</h2>
      {shot_note}
      <ul class="gallery">{gallery}</ul>
    </div>
  </section>

  <section class="fit-section" aria-labelledby="fit-h">
    <div class="wrap two-col">
      <div><h2 id="fit-h">{u['fit']}</h2><ul class="ticks">{fit}</ul></div>
      <div><h2>{u['limits']}</h2><ul class="limits">{limits}</ul></div>
    </div>
  </section>

  <section class="faq" id="faq" aria-labelledby="faq-h">
    <div class="wrap">
      <h2 id="faq-h">{u['faq']}</h2>
      {faq}
    </div>
  </section>

  <section class="closing">
    <div class="wrap">
      <h2>{esc(t['closing_h'])}</h2>
      <p>{t['closing']}</p>
      <div class="cta">{self.store_button(app, lang)}<p class="price-note">{t['price_note']}</p></div>
    </div>
  </section>
</main>
{self.footer(lang, slug)}
</body>
</html>
"""
        self.write(path, head + "\n" + body)
        self.pages.append({"path": path, "alts": alts, "xdef": xdef, "lastmod": app["checked"]})

    def app_sub(self, app: dict, lang: str, kind: str, alts: dict, xdef: str) -> None:
        u, t, slug = UI[lang], app["t"][lang], app["slug"]
        page = t[kind]
        path = f"/{slug}/{lang}/{kind}/"
        head = self.common_head(app, lang, page["title"], page["description"], path, alts, xdef,
                                self.sub_jsonld(app, lang, path, page["h1"], page["description"]))
        alt_path = alts.get(OTHER[lang])
        body = f"""<body class="t-{app['theme']} sub">
{self.app_header(app, lang, alt_path)}
<main id="main">
  <div class="wrap prose">
    <p class="crumb"><a href="/{slug}/{lang}/">{esc(t['name'])}</a></p>
    <h1>{esc(page['h1'])}</h1>
    {page['body']}
    <p class="back"><a href="/{slug}/{lang}/">{u['back_to_app']}</a></p>
  </div>
</main>
{self.footer(lang, slug)}
</body>
</html>
"""
        self.write(path, head + "\n" + body)
        self.pages.append({"path": path, "alts": alts, "xdef": xdef, "lastmod": app["checked"]})

    def app_chooser(self, app: dict) -> None:
        slug = app["slug"]
        links = "".join(
            f'<li><a href="/{slug}/{l}/" hreflang="{l}" lang="{l}">{esc(app["t"][l]["name"])}: {UI[l]["lang_name"]}</a></li>'
            for l in app["langs"])
        pl = app["primary_lang"]
        head = self.head(lang=pl, title=f'{app["t"][pl]["name"]}', description=app["t"][pl]["description"],
                         path=f"/{slug}/", alternates=None, x_default=None, icon_dir=f"/static/img/{slug}",
                         og_image=f"/static/img/{slug}/og.jpg", og_alt=app["t"][pl]["og_alt"], jsonld=None,
                         noindex=True, theme_color=app["theme_color"])
        body = f"""<body class="t-{app['theme']} chooser">
<main id="main" class="wrap prose">
  <img src="/static/img/{slug}/icon-192.png" width="96" height="96" alt="">
  <h1>{esc(app['t'][pl]['name'])}</h1>
  <ul class="choose">{links}</ul>
</main>
</body>
</html>
"""
        self.write(f"/{slug}/", head + "\n" + body)

    def hub(self, lang: str) -> None:
        path = "/" if lang == "en" else "/ja/"
        alts = {"en": "/", "ja": "/ja/"}
        copy = {
            "en": ("Apps by Ryo Morishita", "Official pages for iPhone apps by Ryo Morishita: TaskBit, GeoAlbum, Study Focus and Kaeroute.",
                   "iPhone apps by Ryo Morishita", "Small apps that each solve one everyday problem. Every page describes what the current App Store version can do."),
            "ja": ("Ryo Morishitaのアプリ", "Ryo Morishitaが開発・提供するiPhoneアプリ（TaskBit、GeoAlbum、勉強集中、カエルート）の公式ページです。",
                   "Ryo MorishitaのiPhoneアプリ", "毎日のひとつの困りごとを解決する、小さなアプリを作っています。各ページでは、App Storeで公開中のバージョンでできることを説明しています。"),
        }[lang]
        rows = []
        for s in APP_ORDER:
            a = self.apps[s]
            l = lang if lang in a["langs"] else a["primary_lang"]
            t = a["t"][l]
            note = ""
            if l != lang:
                note = f'<p class="hub-note">{a["t"][l].get("hub_note_" + lang, "")}</p>'
            rows.append(f"""<li class="hub-app hub-{s}">
  <img src="/static/img/{s}/icon-144.webp" width="72" height="72" alt="" loading="lazy">
  <div>
    <h2><a href="/{s}/{l}/">{esc(t['name'])}</a></h2>
    <p>{t['hub_line_' + lang]}</p>
    {note}
  </div>
</li>""")
        jsonld = {"@context": "https://schema.org", "@graph": [
            *self.graph_common(),
            {"@type": "CollectionPage", "@id": self.abs(path), "url": self.abs(path), "name": copy[0], "inLanguage": lang,
             "isPartOf": {"@id": self.abs("/#website")},
             "hasPart": [{"@id": self.abs(f"/{s}/{lang if lang in self.apps[s]['langs'] else self.apps[s]['primary_lang']}/#app")} for s in APP_ORDER]},
        ]}
        verify = json.loads((SITE / "verification.json").read_text(encoding="utf-8"))
        verify_tags = "\n".join(f'<meta name="{esc(k)}" content="{esc(v)}">' for k, v in verify.items() if v) if lang == "en" else ""
        head = self.head(lang=lang, title=copy[0], description=copy[1], path=path, alternates=alts, x_default="/",
                         icon_dir="/static/img/taskbit", og_image="/static/img/hub-og.jpg",
                         og_alt=copy[0], jsonld=jsonld, extra=verify_tags)
        head = head.replace('href="/static/img/taskbit/favicon.png"', 'href="/static/img/hub-favicon.png"').replace(
            'href="/static/img/taskbit/apple-touch-icon.png"', 'href="/static/img/hub-favicon.png"')
        o = OTHER[lang]
        body = f"""<body class="t-hub">
<a class="skip" href="#main">{UI[lang]['skip']}</a>
<header class="site-header"><div class="wrap header-row"><a class="brand" href="{path}"><span>Ryo Morishita</span></a>
<a class="lang" href="{alts[o]}" hreflang="{o}" lang="{o}">{LANG_SWITCH[lang]}</a></div></header>
<main id="main">
  <div class="wrap">
    <h1>{copy[2]}</h1>
    <p class="lead">{copy[3]}</p>
    <ul class="hub-list">{''.join(rows)}</ul>
    <p class="hub-contact">{UI[lang]['contact']}: <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a></p>
  </div>
</main>
</body>
</html>
"""
        self.write(path, head + "\n" + body)
        self.pages.append({"path": path, "alts": alts, "xdef": "/", "lastmod": max(a["checked"] for a in self.apps.values())})

    def not_found(self) -> None:
        head = self.head(lang="ja", title="ページが見つかりません / Page not found", description="お探しのページは見つかりませんでした。",
                         path="/404.html", alternates=None, x_default=None, icon_dir="/static/img",
                         og_image="/static/img/hub-og.jpg", og_alt="Ryo Morishita Apps", jsonld=None, noindex=True)
        head = head.replace('/static/img/favicon.png', '/static/img/hub-favicon.png').replace('/static/img/apple-touch-icon.png', '/static/img/hub-favicon.png')
        links = "".join(f'<li><a href="/{s}/{self.apps[s]["primary_lang"]}/">{esc(self.apps[s]["t"][self.apps[s]["primary_lang"]]["name"])}</a></li>' for s in APP_ORDER)
        body = f"""<body class="t-hub">
<main id="main">
  <div class="wrap">
    <h1>ページが見つかりません</h1>
    <p class="lead">URLが変わったか、ページが削除された可能性があります。</p>
    <h2 lang="en">Page not found</h2>
    <p lang="en">The page may have moved or been removed.</p>
    <ul class="choose">{links}</ul>
    <p><a href="/ja/">アプリ一覧</a> / <a href="/" lang="en">All apps</a></p>
  </div>
</main>
</body>
</html>
"""
        (self.out / "404.html").write_text(head + "\n" + body, encoding="utf-8")

    def sitemap(self) -> None:
        rows = []
        for p in self.pages:
            alts = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{self.abs(a)}"/>' for l, a in p["alts"].items())
            alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{self.abs(p["xdef"])}"/>'
            rows.append(f'  <url>\n    <loc>{self.abs(p["path"])}</loc>\n    <lastmod>{p["lastmod"]}</lastmod>{alts}\n  </url>')
        xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
               + "\n".join(rows) + "\n</urlset>\n")
        (self.out / "sitemap.xml").write_text(xml, encoding="utf-8")
        (self.out / "robots.txt").write_text(
            "# Public pages may be crawled by search engines and AI search crawlers.\n"
            "User-agent: *\nAllow: /\n\n"
            f"Sitemap: {self.abs('/sitemap.xml')}\n", encoding="utf-8")

    def run(self) -> None:
        if self.out.exists():
            shutil.rmtree(self.out)
        self.out.mkdir(parents=True)
        shutil.copytree(SITE / "static", self.out / "static")
        for f in (SITE / "public").iterdir():
            shutil.copy2(f, self.out / f.name)
        (self.out / ".nojekyll").write_text("", encoding="utf-8")
        self.hub("en")
        self.hub("ja")
        for s in APP_ORDER:
            self.app_pages(self.apps[s])
        self.not_found()
        self.sitemap()
        print(f"built {len(self.pages)} indexable pages into {self.out}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", default="https://moris94.github.io")
    ap.add_argument("--out", default=str(ROOT / "dist"))
    args = ap.parse_args()
    Builder(args.base_url, pathlib.Path(args.out)).run()


if __name__ == "__main__":
    main()
