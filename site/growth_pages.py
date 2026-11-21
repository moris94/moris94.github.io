"""Useful, indexable resources based on verified current product facts."""

DATE = '2026-11-20'
CLIP_URL = 'https://apps.apple.com/jp/app/id6796595506'
POLICY = 'https://bottlenose-network-d4d.notion.site/ClipNote-3ae661a42a4a806fade9ee22b9bdb6fb'

def add_page(b, path, title, description, body, slug='kaeroute', *,
             modified=DATE, application=None):
    icon = slug if slug in b.apps else 'clipnote'
    url = b.abs(path)
    page = {
        '@type': 'WebPage', 'url': url, 'name': title, 'description': description,
        'inLanguage': 'ja', 'dateModified': modified,
        'author': {'@type': 'Person', 'name': 'Ryo Morishita'},
    }
    jsonld = {'@context': 'https://schema.org', **page}
    if application is not None:
        app_id = f'{url}#app'
        page['about'] = {'@id': app_id}
        jsonld = {
            '@context': 'https://schema.org',
            '@graph': [page, {'@type': 'MobileApplication', '@id': app_id, 'url': url, **application}],
        }
    head = b.head(lang='ja',title=title,description=description,path=path,
        alternates={'ja':path},x_default=path,icon_dir=f'/static/img/{icon}',
        og_image=f'/static/img/{slug}/og.jpg' if slug in b.apps else '/static/img/hub-og.jpg',
        og_alt=title,jsonld=jsonld,
        extra='<script defer src="/static/js/resources.js?v=20261120"></script>')
    nav = b.app_header(b.apps[slug],'ja',None) if slug in b.apps else '<header class="site-header"><div class="wrap header-row"><a class="brand" href="/clipnote/ja/"><img src="/static/img/clipnote/favicon.png" width="36" height="36" alt=""><span>ClipNote</span></a><a href="/ja/">アプリ一覧</a></div></header>'
    year, month, day = map(int, modified.split('-'))
    b.write(path, head+f'<body class="t-{slug if slug in b.apps else "geoalbum"}">'+('<a class="skip" href="#main">本文へ移動</a>' if slug not in b.apps else '')+nav+f'<main id="main" class="guide wrap"><h1>{title}</h1>'+body+f'<p class="note">開発・提供：Ryo Morishita · 更新：<time datetime="{modified}">{year}年{month}月{day}日</time></p></main><footer class="wrap"><p><a href="/ja/">アプリ一覧へ</a></p></footer></body></html>')
    b.pages.append({'path':path,'alts':{'ja':path},'xdef':path,'lastmod':modified})

def build_resources(b):
    items=[
      ('目的地と連絡先','職場・学校から向かう場所と、連絡の取り方を平常時に確認した'),
      ('ルートの準備','距離、概算所要時間、曲がり角を確認した'),
      ('保存状態','必要な地図と主経路の保存が完了していることを確認した'),
      ('通信なしの参照','自分の端末で通信を切り、必要な保存情報を参照できるか確かめた'),
      ('端末以外の参照手段','必要なら紙など別の参照手段を用意した'),
      ('見直し','準備した計画を次に見直す日を決めた')]
    checks=''.join(f'<li><label><input type="checkbox"> <strong>{h}</strong><span>{text}</span></label></li>' for h,text in items)
    body=f'''<p class="lead">徒歩で帰る道を、平常時に準備するための確認表です。アプリの購入なしで使い、印刷できます。</p>
<p class="notice">この表は道路の安全性や帰宅開始の可否を判断するものではありません。災害時は身の安全を確保し、行政・勤務先・学校の指示を優先してください。</p>
<section><h2>準備した項目にチェック</h2><ul class="prep-checks">{checks}</ul>
<p>準備日：＿＿＿＿＿＿＿＿　見直す日：＿＿＿＿＿＿＿＿</p>
<button type="button" class="resource-action" data-print>チェックリストを印刷する</button><p class="note">チェック内容をサーバーへ送信しません。</p></section>
<section class="no-print"><h2>地図と経路も残したいとき</h2><p>この表で印刷できるのは準備項目だけです。カエルートでは1件の計画と主経路・必要な地図の保存を無料で試せます。地図を含むA4のPDF出力・印刷には買い切りのProが必要です。</p>
<p><a href="/kaeroute/ja/guides/prepare-walking-route/">保存・PDF出力の手順を見る</a></p>{b.store_button(b.apps['kaeroute'],'ja',placement='checklist')}<p>{b.apps['kaeroute']['t']['ja']['price_note']}</p></section>'''
    add_page(b,'/kaeroute/ja/checklist/','徒歩帰宅の準備チェックリスト（印刷用）','平常時に確認する徒歩帰宅の準備項目。ルート、地図保存、通信なしの参照、紙の備えと見直し日をチェックして印刷できます。',body)
    examples=[('問い合わせへの一次返信','お問い合わせありがとうございます。\n【用件】について確認のうえ、【返信予定日】までにご連絡します。\n【署名】'),('日程の確認','【宛名】様\n【用件】のお打ち合わせについて、【候補日時】のご都合はいかがでしょうか。\nよろしくお願いいたします。\n【署名】'),('AIへの依頼メモ','目的：【目的】\n対象読者：【対象読者】\n入力情報：【入力情報】\n出力形式：【出力形式】\n不明な点は推測で補わず、確認事項として示してください。')]
    cards=''.join('<section><h3>'+h+'</h3><pre>'+text+'</pre><button type="button" class="resource-action" data-copy>この例文をコピー</button></section>' for h,text in examples)
    body=f'''<p class="lead">毎回少しだけ違う返信文を、最初から書き直していませんか。ClipNoteは、定型文を保存し、コピー前に必要な変数を入力して使えるiPhoneアプリです。</p>
<p><a href="{CLIP_URL}" class="store-btn" data-link-placement="hero">App Storeで見る</a></p><p>App Storeでの表示名は「ClipNote Snippets」。無料ダウンロード・App内課金あり。iOS 17.0以降、日本語・英語対応。</p>
<section><h2>iPhoneのユーザ辞書とClipNoteの使い分け</h2><p>「確認しました」など、毎回同じ短いフレーズを入力するには、iPhone標準のユーザ辞書に読みを登録すると手軽です。宛名・日程・用件が毎回変わる返信は、ClipNoteにテンプレートとして保存し、コピー前に変わる箇所だけ入力できます。複数の返信を用途ごとにまとめたいときは、フォルダで整理できます。</p></section>
<section><h2>よく使う文章を、差し替える箇所と分ける</h2><p>下の例文をコピーし、自分の用途に直して使えます。【 】は説明用の差し替え目印です。ClipNote内の変数記法を表すものではありません。実際の登録はアプリの画面に従ってください。</p>{cards}<p role="status" data-copy-status aria-live="polite"></p></section>
<section><h2>ClipNoteで使う流れ</h2><ol><li>繰り返し使う文章をテンプレートとして保存する。</li><li>毎回変わる箇所を変数として設定する。</li><li>コピー前に変数を入力し、宛名や日程を確認してから、使いたいアプリへ貼り付ける。</li></ol></section>
<section><h2>無料で試すこと・Proを検討する場面</h2><p>まず定型文の保存とコピーが用途に合うか確認してください。ClipNote Proは、iCloud同期を含む機能を使うための買い切りのApp内課金です。Proの現在の価格と提供範囲は、アプリの購入画面で確認してください。</p><p>単に1つの文章をコピーするだけなら、手元のメモからのコピーでも対応できます。変数を入れて繰り返し使いたい、同期が必要、といった用途に合わせて検討してください。</p></section>
<section><h2>よくある質問</h2><h3>例文を使うのに購入は必要ですか？</h3><p>このページの例文は購入なしでコピーできます。文章を編集して送る前に、差し替え箇所と内容を確認してください。</p><h3>Proはサブスクリプションですか？</h3><p>確認済みの商品は非消費型の買い切りです。価格は購入画面で確認してください。</p><h3>このページのコピー機能は文章を送信しますか？</h3><p>例文はブラウザでコピーします。コピーする本文をアクセス解析に送信しません。サイトのアクセス解析は設定から選べます。</p></section>
<p><a href="{CLIP_URL}" class="store-btn" data-link-placement="closing">ClipNoteをApp Storeで見る</a></p><p><a href="{POLICY}">アプリのサポート・ポリシー</a> · <a href="mailto:shunmemo.support@gmail.com">お問い合わせ</a></p>'''
    application = {
        'name': 'ClipNote Snippets',
        'alternateName': 'ClipNote',
        'operatingSystem': 'iOS 17.0 or later',
        'applicationCategory': 'UtilitiesApplication',
        'installUrl': CLIP_URL,
        'offers': [{'@type': 'Offer', 'price': '0', 'priceCurrency': 'JPY',
                    'description': '無料ダウンロード・App内課金あり'}],
    }
    add_page(b,'/clipnote/ja/','iPhoneの定型文・返信テンプレートを保存して使う｜ClipNote','ClipNoteの定型文保存・変数入力・コピーの使い方と、無料で使える返信文・AI依頼文の例。ProのiCloud同期と買い切り課金について説明します。',body,'clipnote',
             modified='2026-11-22', application=application)
