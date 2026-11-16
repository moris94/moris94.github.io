import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
const code=readFileSync(new URL('../site/static/js/analytics.js',import.meta.url),'utf8');
function browser(stored=null) {
 const listeners={},choices={},scripts=[],moves=[],timers=[];
 const panel={hidden:true,querySelector:()=>({focus(){}}),querySelectorAll:()=>['allow','deny'].map(value=>({dataset:{analyticsChoice:value},addEventListener:(type,fn)=>choices[value]=fn}))};
 const settings={addEventListener:(type,fn)=>listeners.settings=fn,focus(){}};
 const values=new Map(stored?[['moris-site-analytics-choice',stored]]:[]);
 const document={documentElement:{lang:'ja'},title:'Test',referrer:'https://www.google.com/search?q=private',cookie:'',
   querySelector:selector=>selector.startsWith('meta')?{content:'G-4JWYM0L799'}:selector.includes('panel')?panel:settings,
   createElement:()=>({}),head:{append:s=>scripts.push(s)},addEventListener:(type,fn)=>listeners[type]=fn};
 const location={origin:'https://moris94.github.io',hostname:'moris94.github.io',pathname:'/kaeroute/ja/',search:'?private=secret&analytics_test=1',assign:u=>moves.push(u)};
 const window={};vm.runInNewContext(code,{document,window,location,URL,URLSearchParams,localStorage:{getItem:k=>values.get(k),setItem:(k,v)=>values.set(k,v)},setTimeout:fn=>{timers.push(fn);return timers.length},clearTimeout(){}});
 const click=(url='https://apps.apple.com/jp/app/id6811297451',mod=false)=>{const anchor={href:url,dataset:{linkPlacement:'hero'},hasAttribute:()=>false};let prevented=false;listeners.click({type:'click',button:0,metaKey:mod,defaultPrevented:false,target:{closest:()=>anchor},preventDefault:()=>prevented=true});return prevented;};
 return {window,listeners,choices,scripts,moves,timers,panel,click,values};
}
test('no Google request before consent or after saved refusal',()=>{for(const stored of [null,'deny']){const b=browser(stored);assert.equal(b.scripts.length,0);assert.equal(b.click(),false);assert.equal(b.moves.length,0);}});
test('consent tracks one sanitized App Store click and preserves navigation fallback',()=>{
 const b=browser();b.choices.allow();assert.equal(b.scripts.length,1);assert.equal(b.click(),true);
 const events=b.window.dataLayer.map(x=>Array.from(x)).filter(x=>x[0]==='event');
 assert.equal(events.filter(x=>x[1]==='app_store_click').length,1);const params=events.find(x=>x[1]==='app_store_click')[2];
 assert.equal(params.app_slug,'kaeroute');assert.equal(params.link_placement,'hero');assert.equal(params.page_location,'https://moris94.github.io/kaeroute/ja/');assert.equal(params.page_referrer,'https://www.google.com/');assert.equal(params.traffic_type,'developer_test');
 b.timers[0]();assert.equal(b.moves[0],'https://apps.apple.com/jp/app/id6811297451');
 b.choices.deny();const length=b.window.dataLayer.length;assert.equal(b.click(),false);assert.equal(b.window.dataLayer.length,length);
});
test('modified links and unrelated destinations retain native browser behavior',()=>{const b=browser('allow');assert.equal(b.click(undefined,true),false);assert.equal(b.click('https://apps.apple.com.evil.test/jp/app/id6811297451'),false);assert.equal(b.click('https://apps.apple.com/jp/app/id0000000'),false);assert.equal(b.moves.length,0);});
