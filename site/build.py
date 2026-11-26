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
from guides import GUIDES, GUIDES_EN, GUIDES_ZH_TW
from growth_pages import build_resources

SITE = pathlib.Path(__file__).resolve().parent
ROOT = SITE.parent
APP_ORDER = ("taskbit", "geoalbum", "studyfocus", "kaeroute")
DEVELOPER = "Ryo Morishita"
SUPPORT_EMAIL = "shunmemo.support@gmail.com"
GUIDE_UPDATED = "2026-11-26"
GUIDE_CONTENT = {"ja": GUIDES, "en": GUIDES_EN, "zh-TW": GUIDES_ZH_TW}
GUIDE_LABELS = {
    "ja": {
        "title": "使い方ガイド", "author": "アプリ開発者",
        "published": "公開", "updated": "更新",
        "screens": "画面は掲載例です。最新の提供内容・価格はApp Storeをご確認ください。",
        "caption": "既存の掲載画面例", "before": "始める前に", "decision": "無料で試す範囲と、その次",
        "overview": "機能・料金・よくある質問を詳しく見る",
    },
    "en": {
        "title": "How-to guides", "author": "app developer",
        "published": "Published", "updated": "Updated",
        "screens": "Screenshots illustrate the steps. Check the App Store for current availability and pricing.",
        "caption": "App screenshot", "before": "Before you start", "decision": "What you can try for free",
        "overview": "See features, pricing, and frequently asked questions",
    },
    "zh-TW": {
        "author": "App 開發者", "published": "發布", "updated": "更新",
        "screens": "畫面取自繁體中文版 App 的操作示例。",
        "caption": "Kaeroute 操作畫面", "before": "開始前", "decision": "免費版與 Pro",
        "overview": "查看 App 介紹（日文）",
    },
}

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
    "zh-TW": {
        "skip": "跳至主要內容", "limits": "使用限制",
        "support": "支援（日文）", "privacy": "隱私權（日文）",
        "store": "在台灣 App Store 下載",
        "other_apps": "Ryo Morishita 的 App", "developer": "開發者",
        "locale": "zh_TW", "date_fmt": lambda d: f"{int(d[:4])}年{int(d[5:7])}月{int(d[8:10])}日",
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
        self.analytics = json.loads((SITE / "analytics.json").read_text())
        script = (SITE / "static/js/analytics.js").read_bytes()
        self.analytics_href = "/static/js/analytics.js?v=" + hashlib.sha256(script).hexdigest()[:10]
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
        if "</body>" in content:
            lang = next((locale for locale in UI if f'<html lang="{locale}">' in content), "en")
            content = content.replace("</body>", self.analytics_ui(lang) + "\n</body>")
        target.write_text(content, encoding="utf-8")

    def analytics_ui(self, lang: str) -> str:
        if lang == "ja":
            title = "サイトのアクセス解析"
            text = "許可すると、Google Analyticsでページ閲覧とApp Storeへのクリックを計測します。拒否してもサイトとダウンロードは利用できます。設定はいつでも変更できます。"
            yes, no, settings = "許可する", "拒否する", "アクセス解析の設定"
            privacy = "Googleのプライバシーポリシー"
        elif lang == "zh-TW":
            title = "網站流量分析"
            text = "經你同意後，本網站會使用 Google Analytics 統計網頁瀏覽及 App Store 連結的點擊。拒絕後仍可使用網站及下載 App。你可以隨時變更設定。"
            yes, no, settings = "允許", "拒絕", "流量分析設定"
            privacy = "Google 隱私權政策"
        else:
            title = "Website analytics"
            text = "With your permission, Google Analytics measures page views and clicks to the App Store. You can decline and still use the site and download apps. You can change your choice anytime."
            yes, no, settings = "Allow", "Decline", "Analytics settings"
            privacy = "Google Privacy Policy"
        return f'''<div class="analytics-settings"><button type="button" data-analytics-settings>{settings}</button></div>
<aside class="analytics-panel" data-analytics-panel aria-labelledby="analytics-title" hidden>
  <h2 id="analytics-title">{title}</h2><p>{text}</p>
  <p><a href="https://policies.google.com/privacy">{privacy}</a></p>
  <div><button type="button" data-analytics-choice="deny">{no}</button><button type="button" data-analytics-choice="allow">{yes}</button></div>
</aside>'''

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
        for locale in alternates or {}:
            if locale != lang:
                parts.append(f'<meta property="og:locale:alternate" content="{UI[locale]["locale"]}">')
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
        parts.append(f'<meta name="moris-analytics-id" content="{esc(self.analytics["measurement_id"])}">')
        parts.append(f'<script defer src="{self.analytics_href}"></script>')
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
            app_locale = lang if lang in a["langs"] else a["primary_lang"]
            extra = (f'<p class="foot-links"><a href="/{current}/{app_locale}/privacy/">{u["privacy"]}</a>'
                     f'<a href="/{current}/{app_locale}/support/">{u["support"]}</a></p>')
        footer_note = {
            "ja": f"{DEVELOPER}。掲載しているのはApp Storeで公開中の機能です。",
            "en": f"{DEVELOPER}. This site describes features available in the current App Store version.",
            "zh-TW": f"{DEVELOPER}。本網站介紹 App Store 版本提供的功能。",
        }[lang]
        return f"""<footer class="site-footer">
  <div class="wrap">
    {extra}
    <p class="foot-title"><a href="{hub}">{u['other_apps']}</a></p>
    <ul class="foot-apps">{''.join(items)}</ul>
    <p class="foot-note">{u['developer']}: {footer_note}</p>
  </div>
</footer>"""

    def store_button(self, app: dict, lang: str, label_key: str = "store", placement: str = "hero") -> str:
        return (f'<a class="store-btn" href="{app["store_url"][lang]}" data-link-placement="{esc(placement)}">'
                f'{UI[lang][label_key]}</a>')

    # ---------- JSON-LD
    def graph_common(self) -> list[dict]:
        return [
            {"@type": "Person", "@id": self.abs("/#developer"), "name": DEVELOPER, "url": self.abs("/")},
            {"@type": "WebSite", "@id": self.abs("/#website"), "url": self.abs("/"), "name": "Ryo Morishita Apps",
             "publisher": {"@id": self.abs("/#developer")}, "inLanguage": ["en", "ja", "zh-TW"]},
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
        modified = GUIDE_UPDATED if slug in GUIDE_CONTENT[lang] else t.get("modified", app["checked"])
        page = {"@type": "WebPage", "@id": self.abs(path), "url": self.abs(path), "name": t["title"],
                "description": t["description"], "inLanguage": lang, "about": {"@id": self.abs(f"/{slug}/{lang}/#app")},
                "isPartOf": {"@id": self.abs("/#website")}, "dateModified": modified}
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
                         og_alt=app["t"].get(lang, app["t"][app["primary_lang"]])["og_alt"],
                         jsonld=jsonld, extra=extra, theme_color=app["theme_color"])

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
      <div class="cta">{self.store_button(app, lang, placement="closing")}<p class="price-note">{t['price_note']}</p></div>
    </div>
  </section>
</main>
{self.footer(lang, slug)}
</body>
</html>
"""
        if slug in GUIDE_CONTENT[lang]:
            g = GUIDE_CONTENT[lang][slug]
            guide_path = f'/{slug}/{lang}/guides/{GUIDES[slug]["slug"]}/'
            taiwan_link = ""
            if slug in GUIDES_ZH_TW:
                taiwan_path = f'/{slug}/zh-TW/guides/{GUIDES[slug]["slug"]}/'
                taiwan_title = esc(GUIDES_ZH_TW[slug]["title"])
                taiwan_link = f'<p><a href="{taiwan_path}" lang="zh-TW" hreflang="zh-TW">{taiwan_title}</a></p>'
            guide_link = (f'<section class="wrap guide-promo"><h2>{GUIDE_LABELS[lang]["title"]}</h2>'
                          f'<p><a href="{guide_path}">{esc(g["title"])}</a></p><p>{esc(g["description"])}</p>'
                          f'{taiwan_link}</section>')
            body = body.replace('<section class="facts-section"', guide_link + '<section class="facts-section"', 1)
        self.write(path, head + "\n" + body)
        lastmod = GUIDE_UPDATED if slug in GUIDE_CONTENT[lang] else t.get("modified", app["checked"])
        self.pages.append({"path": path, "alts": alts, "xdef": xdef, "lastmod": lastmod})

    def guide_evidence(self, evidence: dict) -> str:
        parts = [f'<section><h2>{esc(evidence["title"])}</h2><p>{esc(evidence["intro"])}</p>']
        if columns := evidence.get("columns"):
            headings = "".join(f'<th scope="col">{esc(label)}</th>' for label in columns)
            rows = "".join(f'<tr><th scope="row">{esc(label)}</th><td>{esc(result)}</td></tr>'
                           for label, result in evidence["rows"])
            parts.append(f'<table class="guide-table"><thead><tr>{headings}</tr></thead><tbody>{rows}</tbody></table>')
        if download := evidence.get("download"):
            path, label = download
            parts.append(f'<p><a href="{esc(path)}" download>{esc(label)}</a></p>')
        if video := evidence.get("video"):
            path, caption = video
            parts.append(f'<figure class="guide-video"><video controls playsinline preload="none" width="400" height="868" aria-describedby="guide-video-caption">'
                         f'<source src="{esc(path)}" type="video/mp4"></video>'
                         f'<figcaption id="guide-video-caption">{esc(caption)} <a href="{esc(path)}">Download the video</a>.</figcaption></figure>')
        return "".join(parts) + "</section>"

    def guide(self, app: dict, lang: str) -> None:
        slug = app["slug"]
        g, labels, ui = GUIDE_CONTENT[lang][slug], GUIDE_LABELS[lang], UI[lang]
        alts = {locale: f"/{slug}/{locale}/guides/{GUIDES[slug]['slug']}/"
                for locale in GUIDE_CONTENT if slug in GUIDE_CONTENT[locale]}
        path, x_default = alts[lang], alts[app["primary_lang"]]
        app_locale = lang if lang in app["langs"] else app["primary_lang"]
        app_path = f"/{slug}/{app_locale}/"
        app_text = app["t"][app_locale]
        product_name = g.get("product_name", app_text["name"])
        published = "2026-11-18" if lang == "ja" else GUIDE_UPDATED
        graph = {"@context":"https://schema.org", "@graph":[*self.graph_common(), {
            "@type":"Article", "@id":self.abs(path), "url":self.abs(path),
            "headline":g["title"], "description":g["description"], "inLanguage":lang,
            "datePublished":published, "dateModified":GUIDE_UPDATED,
            "author":{"@type":"Person","name":DEVELOPER},
            "about":{"@id":self.abs(app_path + "#app")}}]}
        head = self.common_head(app, lang, g["title"] + " | " + product_name,
                                g["description"], path, alts, x_default, graph)
        shot_alts = g.get("shot_alts", {})
        steps = "".join(
            f'<section class="guide-step"><div><h2>{i}. {esc(h)}</h2><p>{esc(body)}</p></div>'
            f'<figure>{self.img(slug, shot, lang, shot_alts.get(shot, h))}<figcaption>{labels["caption"]}</figcaption></figure></section>'
            for i, (h, body, shot) in enumerate(g["steps"], 1)
        )
        example = ""
        if case := g.get("example"):
            visits = "".join(
                f"<li><strong>{esc(label)}</strong> {esc(detail)}</li>"
                for label, detail in case["visits"]
            )
            example = f"""
<section class="guide-step">
<div><h2>{esc(case['title'])}</h2><p>{esc(case['intro'])}</p><ol>{visits}</ol></div>
<figure>{self.img(slug, case['shot'], lang, case['alt'])}<figcaption>{esc(case['caption'])}</figcaption></figure>
</section>"""
        if preview := g.get("preview"):
            heading, detail, shot, alt = preview
            example = f'<section class="guide-step"><div><h2>{esc(heading)}</h2><p>{esc(detail)}</p></div><figure>{self.img(slug, shot, lang, alt)}</figure></section>'
        checklist = ""
        if slug == "kaeroute" and lang == "ja":
            checklist = '<p class="resource-callout">持ち物や連絡先だけを紙で確認したい方は、<a href="/kaeroute/ja/checklist/">無料の徒歩帰宅準備チェックリストを開いて印刷</a>できます。</p>'
        dates = f'{labels["published"]} <time datetime="{published}">{ui["date_fmt"](published)}</time>'
        if published != GUIDE_UPDATED:
            dates += f' · {labels["updated"]} <time datetime="{GUIDE_UPDATED}">{ui["date_fmt"](GUIDE_UPDATED)}</time>'
        if lang == "zh-TW":
            header = f'''<a class="skip" href="#main">{ui['skip']}</a>
<header class="site-header"><div class="wrap header-row">
<a class="brand" href="{path}" aria-current="page"><img src="/static/img/{slug}/icon-96.webp" width="36" height="36" alt=""><span>{esc(product_name)}</span></a>
</div></header>'''
            language_links = (f'<p><a href="{alts["ja"]}" lang="ja" hreflang="ja">日本語</a> · '
                              f'<a href="{alts["en"]}" lang="en" hreflang="en">English</a></p>')
        else:
            header = self.app_header(app, lang, alts.get(OTHER[lang]))
            language_links = (f'<p><a href="{alts["zh-TW"]}" lang="zh-TW" hreflang="zh-TW">繁體中文（台灣）</a></p>'
                              if "zh-TW" in alts else "")
        price_note = g.get("price_note", app_text["price_note"])
        body = f"""<body class="t-{app['theme']}">{header}
<main id="main" class="guide wrap"><article>
<h1>{esc(g['title'])}</h1>
<p class="lead">{esc(g['lead'])}</p>
{language_links}
<p class="note">{DEVELOPER} ({labels['author']}) · {dates}</p>
<p class="note">{labels['screens']}</p>
{checklist}{example}
<div class="cta">{self.store_button(app,lang,placement='guide_example')}</div>
<section><h2>{labels['before']}</h2><p>{esc(g['before'])}</p></section>
{steps}
{self.guide_evidence(g['evidence']) if 'evidence' in g else ''}
<section class="notice"><h2>{ui['limits']}</h2><p>{esc(g['limits'])}</p></section>
<section><h2>{labels['decision']}</h2><p>{esc(g['decision'])}</p>
<div class="cta">{self.store_button(app,lang,placement='guide')}<p class="price-note">{price_note}</p></div></section>
<p><a href="{app_path}">{labels['overview']}</a> · <a href="{app_path}privacy/">{ui['privacy']}</a> · <a href="{app_path}support/">{ui['support']}</a></p>
</article></main>{self.footer(lang,slug)}</body></html>"""
        self.write(path, head + body)
        self.pages.append({"path": path, "alts": alts, "xdef": x_default, "lastmod": GUIDE_UPDATED})

    def app_sub(self, app: dict, lang: str, kind: str, alts: dict, xdef: str) -> None:
        u, t, slug = UI[lang], app["t"][lang], app["slug"]
        page = t[kind]
        analytics_note = ""
        if kind == "privacy":
            analytics_note = ('<h2>このWebサイトのアクセス解析</h2><p>アプリのデータ取り扱いとは別に、このサイトでは許可した方のページ閲覧とApp StoreリンクのクリックをGoogle Analyticsで計測します。Googleはブラウザー・端末・通信に関する情報とCookieを扱います。広告向けのシグナルは無効です。送信するページURLから検索パラメータを除き、参照元はホスト名だけにします。サイト下部の「アクセス解析の設定」で拒否・変更できます。拒否しても利用に影響しません。</p>' if lang == "ja" else '<h2>Analytics on this website</h2><p>Separate from how the app handles data, this website uses Google Analytics to measure page views and App Store link clicks only with your permission. Google processes browser, device and connection information and analytics cookies. Advertising signals are disabled. Page URL query parameters are removed and referrers are reduced to the hostname. Use Analytics settings at the bottom of the page to decline or change your choice. Declining does not affect access.</p>')
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
    {analytics_note}
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
        guide_links = "".join(
            f'<li><a href="/{slug}/{lang}/guides/{GUIDES[slug]["slug"]}/">{esc(g["title"])}</a></li>'
            for slug, g in GUIDE_CONTENT[lang].items()
        )
        body = f"""<body class="t-hub">
<a class="skip" href="#main">{UI[lang]['skip']}</a>
<header class="site-header"><div class="wrap header-row"><a class="brand" href="{path}"><span>Ryo Morishita</span></a>
<a class="lang" href="{alts[o]}" hreflang="{o}" lang="{o}">{LANG_SWITCH[lang]}</a></div></header>
<main id="main">
  <div class="wrap">
    <h1>{copy[2]}</h1>
    <p class="lead">{copy[3]}</p>
    <ul class="hub-list">{''.join(rows)}</ul>
    <section class="guide-promo"><h2>{GUIDE_LABELS[lang]['title']}</h2><ul>{guide_links}</ul></section>
    {('<section><h2>定型文の再利用</h2><p><a href="/clipnote/ja/">ClipNote：返信文とAI依頼文のテンプレート例</a></p><p><a href="/kaeroute/ja/checklist/">徒歩帰宅の準備チェックリストを印刷する</a></p></section>') if lang == 'ja' else ''}
    <p class="hub-contact">{UI[lang]['contact']}: <a href="mailto:{SUPPORT_EMAIL}">{SUPPORT_EMAIL}</a></p>
  </div>
</main>
</body>
</html>
"""
        self.write(path, head + "\n" + body)
        self.pages.append({"path": path, "alts": alts, "xdef": "/", "lastmod": GUIDE_UPDATED})

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
        (self.out / "sitemap.txt").write_text("\n".join(self.abs(p["path"]) for p in self.pages) + "\n", encoding="utf-8")
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
        for lang, guides in GUIDE_CONTENT.items():
            for slug in guides:
                self.guide(self.apps[slug], lang)
        build_resources(self)
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
