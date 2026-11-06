# 公式サイトの運用

## サイト構成

公開URL: `https://moris94.github.io/`（GitHubのユーザーサイト。独自ドメインなし）

| URL | 内容 | インデックス |
|---|---|---|
| `/`、`/ja/` | 開発者トップ（英語・日本語） | する |
| `/{app}/en/`、`/{app}/ja/` | アプリのトップ（概要、機能、使い方、画面、向いている人とできないこと、FAQ） | する |
| `/{app}/{lang}/privacy/` | プライバシーの概要と、App Store登録済みポリシーへのリンク | する |
| `/{app}/{lang}/support/` | よくある問題とお問い合わせ先 | する |
| `/{app}/` | 言語の選択（`noindex, follow`） | しない |
| `/404.html` | 見つからないページ（`noindex`） | しない |
| `/app-ads.txt` | 既存のAdSense設定（移設前と同じ内容） | 対象外 |

`{app}` は `taskbit`、`geoalbum`、`studyfocus`、`kaeroute`。
x-default は TaskBit・GeoAlbum・StudyFocus が英語、カエルートは日本語（アプリが日本語・繁体字中国語のみのため）。

### リポジトリ構成

```
site/build.py          静的HTMLを dist/ に生成（Python標準ライブラリのみ）
site/validate.py       生成物の検証（同上）
site/content/*.py      アプリごとの本文（日英）。事実は docs/website/app-information.md と一致させる
site/static/css/       共通CSS（アプリごとのテーマを含む）
site/static/img/       最適化済み画像（tools/prepare_assets.py で生成してコミット）
site/public/           そのまま公開ルートへ置くファイル（app-ads.txt）
tools/prepare_assets.py  アプリのリポジトリから画像を作る（ローカル専用）
tests/                 ブラウザテスト（ローカル専用、Playwright + axe-core）
.github/workflows/pages.yml  ビルド・検証・デプロイ
```

### 技術選定の理由

ページは26枚で、内容はアプリごとの本文だけが違う。Astroなどを入れるほどの規模ではなく、依存パッケージがないほうが長く保守しやすいので、Pythonの標準ライブラリだけで書いた小さなジェネレーターにした。出力は静的HTML・CSS・画像だけで、JavaScriptはない（JavaScriptを無効にしても全内容を読める）。

## 更新方法

1. アプリを更新したら、先に `docs/website/app-information.md` の事実（バージョン、価格、機能、データの扱い）を更新する。情報源は公開中のApp Store（iTunes Lookup API、App Storeのページ）を正とする。未公開の機能は載せない
2. `site/content/{app}.py` の該当箇所と `checked`（確認日）、`version` を更新する
3. スクリーンショットが変わったら `python3 tools/prepare_assets.py --products ~/Desktop/products`
4. `python3 site/build.py && python3 site/validate.py`
5. ローカル表示とブラウザテスト（下記）
6. `main` にpushすると GitHub Actions が検証してデプロイする

## テスト方法

```sh
python3 site/build.py
python3 site/validate.py              # SEO・リンクの静的検証
python3 site/validate.py --external   # 外部リンク（App Store、ポリシー）も確認
python3 -m http.server 8765 --bind 127.0.0.1 --directory dist &
cd tests && npm install && BASE=http://127.0.0.1:8765 npm test
```

`validate.py` が確認すること: lang、title・descriptionの有無と重複、canonicalがファイルのURLと一致、hreflangの自己参照・相互参照・x-default、OGP、JSON-LDのパースと必須項目（評価・レビューを含めていないこと、installUrlが本文にリンクされていること）、h1が1つで見出しの飛びがないこと、画像のalt・width・height、内部リンクとページ内リンク、sitemap.xmlとインデックス対象ページの一致、robots.txt、404、app-ads.txt。

`tests/browser-test.mjs` が確認すること（幅360pxと1280px）: HTTP 200、横方向のはみ出し、画像の読み込み、App Storeリンクの形式、言語切り替え、最初のTabでスキップリンク、コンソールエラー、axe-core（WCAG 2.2 AA）。スクリーンショットを `tests/screenshots/` に保存する。

## SEO施策

- ページごとに固有の title・description、自己参照の canonical、`lang` 属性、viewport、favicon、apple-touch-icon
- 日英で別URL。hreflang（ja、en、x-default）を全ページで相互参照。言語切り替えリンク
- Open Graph と Twitter Card（1200×630のOGP画像をアプリごとに用意）
- 構造化データ（JSON-LD）: アプリのトップに `MobileApplication`（name、alternateName、description、applicationCategory、operatingSystem、softwareVersion、image、screenshot、installUrl、offers、author/publisher）、`WebPage`、`WebSite`、`Person`（開発者）。サブページは `WebPage` と `BreadcrumbList`
  - Googleのソフトウェアアプリのリッチリザルトは `aggregateRating` か `review` が必須。4アプリとも評価がないため、**リッチリザルトの対象にはならない**。評価を作らず、エンティティの説明として使う
  - `applicationCategory` は、Googleが挙げる値のうちApp Storeのカテゴリと矛盾しないものを選んだ（TaskBit: LifestyleApplication、GeoAlbum: MultimediaApplication、StudyFocus: EducationalApplication、カエルート: UtilitiesApplication）
  - FAQPage は使っていない（Googleは2023年以降、FAQのリッチリザルトを一部の公的サイトに限っている）。FAQは通常のHTMLとして載せている
- `robots.txt` はすべてのクローラーを許可し、サイトマップを示す。ユーザーサイトなので robots.txt がホストのルートにあり、全ページに効く
- `sitemap.xml` は絶対URLと xhtml:link の言語代替を含む
- iOS Safari の Smart App Banner（`apple-itunes-app`）
- 画像はWebP（幅360/720、srcset）、width/height指定、ヒーロー以外は遅延読み込み。Webフォントなし、JavaScriptなし

## GEO（AI検索）施策

確認した公式資料（2026-11-06）:

- Google: [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) — AI OverviewsとAI Modeに追加の要件や特別な最適化、AI用のテキストファイル、特別な構造化データは不要。通常の検索でインデックスされ、スニペットを表示できることが条件。成果はSearch Consoleの検索パフォーマンス（ウェブ）に含まれる
- OpenAI: [Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots) — ChatGPT検索への掲載は `OAI-SearchBot` で決まる。`GPTBot` は学習用で別に制御できる。`ChatGPT-User` はユーザーの操作による訪問
- Bing Webmaster Tools の AI Performance レポート（2026年2月から公開プレビュー）: Copilot と Bing のAI要約での引用を、ページ別・グラウンディングクエリ別に表示。クリック数は含まれない

実装したこと（いずれも通常の読みやすさと両立するもの）:

- 各トップの冒頭に「〇〇は、△△のためのiPhoneアプリです」と1文で言い切るリード文と、`概要` の要約・事実表（正式名、できること、料金、対応環境、言語、データの保存先、バージョン、開発者、確認日）
- 「何をするか」「誰に向いているか」「無料か」「インターネットは必要か」「データはどこに保存されるか」「一般的な方法と何が違うか」にFAQで直接答える。仕様が確認できない質問は作っていない
- 「できないこと・注意点」を明記（AIに過大な説明をされないため）
- 名称・価格・機能の表記をApp Storeと一致させ、構造化データの値を本文に表示している内容と一致させた
- 重要な情報は画像の中だけに置かず、すべてHTMLのテキストで書いた

導入しなかったこと:

- `llms.txt`: Googleは AI機能のために新しい機械可読ファイルやAI用テキストファイルは不要と明言している。OpenAI・Bingの公式資料にも、検索掲載に使うという記載は見当たらない。効果の根拠がないため入れない
- AIクローラーの個別ブロック: robots.txt はすべて許可。学習用クローラー（GPTBot、Google-Extended など）を拒否するかはオーナーの方針として未決定。拒否する場合は `site/build.py` の robots.txt に `User-agent: GPTBot` / `Disallow: /` などを追加する（検索用の OAI-SearchBot や Googlebot は止めない）

期待する効果と不確実性: 上記はAI検索がアプリを正しく理解し、引用できる状態を作るためのもので、特定のAI検索での掲載・推薦を保証しない。新しいサイトはインデックスされるまで時間がかかり、外部からのリンクも現時点ではApp Storeの登録URLを変えない限りほとんどない。

## Search Console と Bing Webmaster Tools

### 登録状況（2026-11-06）

| 項目 | 状態 |
| --- | --- |
| Search Console プロパティ（URLプレフィックス `https://moris94.github.io/`） | 追加済み・所有権確認済み（HTMLタグ） |
| 確認用メタタグ | `site/verification.json` の `google-site-verification` に設定済み。トップ（`/`）に出力。**削除すると確認が外れる** |
| Search Console サイトマップ | 送信済み。送信直後のステータスは「取得できませんでした」（URLは200で正常に返る）。数日後に「成功」になったか要確認 |
| Search Console インデックス登録リクエスト | 8ページ送信済み：`/taskbit/en/` `/taskbit/ja/` `/geoalbum/en/` `/geoalbum/ja/` `/studyfocus/en/` `/studyfocus/ja/` `/kaeroute/ja/` `/kaeroute/en/` |
| Bing Webmaster Tools | Search Console からインポートで追加済み（`msvalidate.01` は未使用で空のまま） |
| Bing サイトマップ | インポートで登録済み（Success、26 URL）。さらに手動で再送信済み（送信直後は Processing） |
| Bing「AI Performance」 | 未確認 |

手順は以下（再登録や別サイトのときの参考）。

### Google Search Console

1. https://search.google.com/search-console を開き、「プロパティを追加」で **URLプレフィックス** に `https://moris94.github.io/` を入力する（`github.io` のドメインプロパティはDNSを管理できないので使えない）
2. 確認方法で「HTMLタグ」を選び、表示された `google-site-verification` の content の値を控える
3. 控えた値を `site/verification.json` の `google-site-verification` に入れ、`python3 site/build.py && python3 site/validate.py` を通してpushする（トップ `/` の head にだけメタタグが出る）
4. デプロイ後に「確認」を押す
5. 「サイトマップ」で `https://moris94.github.io/sitemap.xml` を送信する
6. 「URL検査」で各アプリのトップ（日英）のインデックス登録をリクエストする

### Bing Webmaster Tools

1. https://www.bing.com/webmasters を開き、「Google Search Consoleからインポート」を選ぶ（Search Consoleの確認後が簡単）。Search Console の所有者の Google アカウントを選んで閲覧権限を許可する（許可直後に Bing がエラー画面を出すことがあるが、もう一度インポートすれば通る）。または `https://moris94.github.io/` を追加して、`msvalidate.01` の値を `site/verification.json` に入れてpushする
2. サイトマップを送信する
3. 「AI Performance」でCopilotでの引用を確認する

## 成果の測定

| 対象 | 取得できる指標 | 取得できないこと |
|---|---|---|
| Google検索（AI Overviews・AI Modeを含む） | Search Consoleの表示回数、クリック数、掲載順位、クエリ、ページ、インデックス状況 | AI機能での表示だけを分けた数値（ウェブ検索に合算される） |
| Bing・Copilot | 検索の表示回数・クリック数、AI Performance（引用数、引用されたページ、グラウンディングクエリ） | AI回答からのクリック数 |
| ChatGPT検索 | 公式の管理画面は確認できなかった。アクセス解析を入れれば、参照元（chatgpt.com）からの流入として見える可能性がある（OpenAIの公式資料では未確認） | 表示回数、引用回数 |
| App Storeリンクのクリック | 現在は測定していない | — |
| App Store側 | App Store Connectの「App分析」で、Webからの参照元（App Store Connectで確認できる範囲） | サイト訪問とインストールを同じ人として結びつけること |

初期段階ではアクセス解析を入れていない（プライバシーと運用負荷を優先）。必要になったら、Cookieを使わない無料の解析（例: Cloudflare Web Analytics）を検討し、プライバシーの説明を更新してから入れる。App Storeリンクには、Appleの「キャンペーンリンク」（`ct` パラメータ）を付けるとApp Store Connectで流入元を確認できる。

AI検索の定点観測: 新しい会話で、指名質問（「TaskBitとは」）と一般質問（「ToDoが続かない人向けのiPhoneアプリ」「撮影場所で写真をアルバムに整理するiPhoneアプリ」「休憩中だけSNSを使える勉強タイマー」「徒歩の帰宅ルートをオフラインで保存できるアプリ」）を、サービス・モード・日時・言及の有無・引用URL・誤りの有無とあわせて記録する。少数の質問の結果を一般化しない。

## 既知の制約

- GitHub Pagesでは HTTPヘッダー（キャッシュ期間、CSP など）を設定できない。CSSは内容のハッシュを `?v=` に付けて、更新時に読み直させている
- 独自ドメインがないため、`github.io` 全体の評価に依存する。独自ドメインに移す場合は、CNAME設定と全URLのリダイレクトが必要（GitHub Pagesはユーザーサイトの独自ドメイン設定時に旧URLから自動転送する）
- アプリのリポジトリは非公開のため、画像の生成（`tools/prepare_assets.py`）はローカルでのみ行う
- App Store Connectでしか見られない項目（提供国一覧など）は未確認
- App Storeに登録されているプライバシー・サポートURLはNotionのまま。サイトのページへ切り替えるかはオーナーが決める（切り替える場合は App Store Connect で各アプリのURLを更新する）

## 公開前・公開後に人が確認すること

- 手元の `docs/website/internal-notes.md`（コミットしない）に記録した要確認事項
