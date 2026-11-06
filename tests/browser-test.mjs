// Browser checks for the built site. Serve dist/ first, e.g.:
//   python3 -m http.server 8765 --bind 127.0.0.1 --directory dist
//   cd tests && npm install && BASE=http://127.0.0.1:8765 npm test
// Uses the installed Google Chrome (channel "chrome"). Screenshots go to tests/screenshots/.
import { chromium } from "playwright";
import AxeBuilder from "@axe-core/playwright";
import fs from "node:fs";
import path from "node:path";

const BASE = process.env.BASE || "http://127.0.0.1:8765";
const OUT = path.join(path.dirname(new URL(import.meta.url).pathname), "screenshots");
fs.mkdirSync(OUT, { recursive: true });

const apps = ["taskbit", "geoalbum", "studyfocus", "kaeroute"];
const pages = ["/", "/ja/"];
for (const a of apps) for (const l of ["ja", "en"]) for (const s of ["", "privacy/", "support/"]) pages.push(`/${a}/${l}/${s}`);
pages.push(...apps.map((a) => `/${a}/`), "/404.html");

const viewports = [
  { name: "mobile", width: 360, height: 780 },
  { name: "desktop", width: 1280, height: 900 },
];

const failures = [];
const fail = (m) => { failures.push(m); console.log("FAIL", m); };

const browser = await chromium.launch({ channel: process.env.PW_CHANNEL || "chrome" });
for (const vp of viewports) {
  const ctx = await browser.newContext({ viewport: { width: vp.width, height: vp.height } });
  for (const p of pages) {
    const page = await ctx.newPage();
    const consoleErrors = [];
    page.on("console", (m) => m.type() === "error" && consoleErrors.push(m.text()));
    page.on("pageerror", (e) => consoleErrors.push(String(e)));
    const res = await page.goto(BASE + p, { waitUntil: "networkidle" });
    if (!res || res.status() !== 200) fail(`${p} status ${res && res.status()}`);
    // scroll to load lazy images
    const h = await page.evaluate(() => document.body.scrollHeight);
    for (let y = 0; y < h; y += 600) { await page.evaluate((v) => window.scrollTo(0, v), y); await page.waitForTimeout(40); }
    await page.waitForLoadState("networkidle");
    const r = await page.evaluate(() => {
      const imgs = [...document.images].map((i) => ({ src: i.currentSrc || i.src, ok: i.complete && i.naturalWidth > 0 }));
      const overflow = document.documentElement.scrollWidth - window.innerWidth;
      const wide = [...document.querySelectorAll("body *")].filter((e) => {
        const b = e.getBoundingClientRect();
        return b.width > 0 && b.right > window.innerWidth + 1 && getComputedStyle(e).position !== "absolute" && !e.closest(".hero-art");
      }).slice(0, 3).map((e) => e.tagName + "." + e.className);
      const store = [...document.querySelectorAll("a.store-btn")].map((a) => a.href);
      const small = [...document.querySelectorAll("a, button")].filter((e) => {
        const b = e.getBoundingClientRect();
        return b.width > 0 && b.height < 24 && !e.closest("p, dd, li.qa, .prose li");
      }).length;
      return { imgs, overflow, wide, store, small, lang: document.documentElement.lang };
    });
    for (const i of r.imgs) if (!i.ok) fail(`${p} [${vp.name}] image not loaded ${i.src}`);
    if (r.overflow > 0) fail(`${p} [${vp.name}] horizontal overflow ${r.overflow}px ${r.wide.join(",")}`);
    for (const s of r.store) if (!/^https:\/\/apps\.apple\.com\/(jp|us)\/app\/id\d+$/.test(s)) fail(`${p} bad store link ${s}`);
    if (/^\/(taskbit|geoalbum|studyfocus|kaeroute)\/(ja|en)\/$/.test(p) && r.store.length < 2) fail(`${p} expected App Store links in hero and closing`);
    if (r.small) fail(`${p} [${vp.name}] ${r.small} standalone links smaller than 24px`);
    if (consoleErrors.length) fail(`${p} console errors: ${consoleErrors.join(" | ")}`);

    if (vp.name === "desktop" || p.endsWith("/ja/") || p.endsWith("/en/") || p === "/") {
      const axe = await new AxeBuilder({ page }).withTags(["wcag2a", "wcag2aa", "wcag21aa", "wcag22aa"]).analyze();
      for (const v of axe.violations) fail(`${p} [${vp.name}] axe ${v.id} (${v.impact}): ${v.nodes.slice(0, 2).map((n) => n.target.join(" ")).join(", ")}`);
    }
    // keyboard: first Tab focuses the skip link on pages that have one
    if (await page.$(".skip")) {
      await page.evaluate(() => window.scrollTo(0, 0));
      await page.keyboard.press("Tab");
      const focused = await page.evaluate(() => document.activeElement && document.activeElement.className);
      if (focused !== "skip") fail(`${p} first Tab focuses "${focused}", expected skip link`);
    }

    // language switch goes to the same page in the other language
    const sw = await page.$("a.lang");
    if (sw) {
      const href = await sw.getAttribute("href");
      const other = await ctx.newPage();
      const rr = await other.goto(BASE + href);
      const lang = await other.evaluate(() => document.documentElement.lang);
      if (rr.status() !== 200 || lang === r.lang) fail(`${p} language switch to ${href} -> ${rr.status()} lang=${lang}`);
      await other.close();
    }

    if (/^\/(taskbit|geoalbum|studyfocus|kaeroute)\/(ja|en)\/$|^\/$/.test(p)) {
      await page.evaluate(() => window.scrollTo(0, 0));
      await page.waitForTimeout(3200);
      await page.screenshot({ path: path.join(OUT, `${vp.name}${p.replace(/\//g, "_")}.png`), fullPage: true });
    }
    await page.close();
  }
  await ctx.close();
}
await browser.close();
console.log(failures.length ? `\n${failures.length} failures` : `\nall browser checks passed (${pages.length} pages x ${viewports.length} viewports)`);
process.exit(failures.length ? 1 : 0);
