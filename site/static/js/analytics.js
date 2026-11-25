/* First-party UI; Google Analytics loads only after affirmative consent. */
(() => {
  'use strict';
  const measurement = document.querySelector('meta[name="moris-analytics-id"]')?.content;
  if (!/^G-[A-Z0-9]+$/.test(measurement || '')) return;
  const key = 'moris-site-analytics-choice';
  const appIds = {'6786552954':'taskbit','6813050203':'geoalbum','6800586592':'studyfocus','6811297451':'kaeroute','6796595506':'clipnote'};
  const panel = document.querySelector('[data-analytics-panel]');
  const settings = document.querySelector('[data-analytics-settings]');
  const testParam = new URLSearchParams(location.search).get('analytics_test');
  // Keep QA events separate while following links in the same tab.
  function testSession() {
    try {
      if (testParam === '1') sessionStorage.setItem('moris-analytics-test', '1');
      if (testParam === '0') sessionStorage.removeItem('moris-analytics-test');
      return sessionStorage.getItem('moris-analytics-test') === '1';
    } catch { return testParam === '1'; }
  }
  let enabled = false;
  let loaded = false;
  let viewed = false;
  const lang = document.documentElement.lang === 'ja' ? 'ja' : 'en';
  const cleanPage = () => location.origin + location.pathname;
  const sourceHost = () => { try { return new URL(document.referrer).hostname; } catch { return ''; } };
  function remember(value) { try { localStorage.setItem(key, value); } catch { /* Optional persistence. */ } }
  function choice() { try { return localStorage.getItem(key); } catch { return null; } }
  function send(name, values = {}) {
    if (!enabled) return;
    const test = testSession();
    window.gtag('event', test ? 'qa_' + name : name, {
      send_to: measurement, page_location: cleanPage(), page_referrer: sourceHost() ? `https://${sourceHost()}/` : '',
      page_title: document.title, page_language: lang,
      app_slug: location.pathname.split('/')[1] in {'taskbit':1,'geoalbum':1,'studyfocus':1,'kaeroute':1,'clipnote':1} ? location.pathname.split('/')[1] : 'portfolio',
      traffic_type: test ? 'developer_test' : 'website',
      ...(test ? {debug_mode:true} : {}), transport_type:'beacon', ...values
    });
  }
  function allow() {
    enabled = true;
    if (!loaded) {
      loaded = true;
      window.dataLayer = window.dataLayer || [];
      window.gtag = function () { window.dataLayer.push(arguments); };
      window.gtag('consent', 'default', {analytics_storage:'granted',ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied'});
      window.gtag('js', new Date());
      window.gtag('config', measurement, {send_page_view:false,allow_google_signals:false,allow_ad_personalization_signals:false,
        page_location:cleanPage(),page_referrer:sourceHost() ? `https://${sourceHost()}/` : '',cookie_flags:'SameSite=Lax;Secure'});
      const script = document.createElement('script'); script.async = true;
      script.src = `https://www.googletagmanager.com/gtag/js?id=${measurement}`;
      script.referrerPolicy = 'origin'; document.head.append(script);
    } else {
      window.gtag('consent','update',{analytics_storage:'granted'});
    }
    if (!viewed) { viewed = true; send('page_view'); }
  }
  function deny() {
    enabled = false;
    if (loaded) window.gtag('consent','update',{analytics_storage:'denied'});
    // Clear cookies created by this site's optional GA stream after withdrawal.
    document.cookie.split(';').forEach(part => {
      const name = part.trim().split('=')[0];
      if (name === '_ga' || name === `_ga_${measurement.slice(2).replace(/-/g,'_')}`) {
        for (const domain of ['', `;domain=${location.hostname}`])
          document.cookie = `${name}=;Max-Age=0;path=/${domain};SameSite=Lax;Secure`;
      }
    });
  }
  panel?.querySelectorAll('[data-analytics-choice]').forEach(button => button.addEventListener('click', () => {
    const value = button.dataset.analyticsChoice;
    remember(value); value === 'allow' ? allow() : deny();
    panel.hidden = true; settings?.focus();
  }));
  settings?.addEventListener('click', () => {
    panel.hidden = false; panel.querySelector('button')?.focus();
  });
  function track(event) {
    if (!enabled || (event.type === 'click' && event.button !== 0) || (event.type === 'auxclick' && event.button !== 1)) return;
    const anchor = event.target.closest?.('a[href]'); if (!anchor) return;
    let target; try { target = new URL(anchor.href); } catch { return; }
    if (target.protocol !== 'https:' || target.hostname !== 'apps.apple.com') return;
    const id = target.pathname.match(/\/id(\d+)(?:\/|$)/)?.[1]; if (!appIds[id]) return;
    let timer;
    const follow = () => { if (timer) { clearTimeout(timer); timer = null; location.assign(anchor.href); } };
    const wait = event.type === 'click' && !event.defaultPrevented && !event.metaKey && !event.ctrlKey && !event.shiftKey && !event.altKey && (!anchor.target || anchor.target === '_self') && !anchor.hasAttribute('download');
    if (wait) { event.preventDefault(); timer = setTimeout(follow, 400); }
    try {
      send('app_store_click', {app_slug:appIds[id],app_store_id:id,
        link_placement:anchor.dataset.linkPlacement || 'content',destination_country:target.pathname.split('/')[1],
        link_url:target.origin + target.pathname, event_callback:follow,event_timeout:400});
    } catch { follow(); }
  }
  document.addEventListener('click',track);
  document.addEventListener('auxclick',track);
  if (choice() === 'allow') allow();
  else if (choice() !== 'deny' && panel) panel.hidden = false;
})();
