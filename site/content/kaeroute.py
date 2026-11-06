"""カエルート (Kaeroute) — facts: docs/website/app-information.md (App Store 1.0.0, checked 2026-11-06).

The app UI is Japanese and Traditional Chinese only and the app is not on the US App Store,
so the English page links to the Japan store and shows the Japanese screens.
"""

POLICY = "https://bottlenose-network-d4d.notion.site/3da661a42a4a800095aad0247a42414f"
MAIL = "shunmemo.support@gmail.com"
JP = "https://apps.apple.com/jp/app/id6811297451"
TW = "https://apps.apple.com/tw/app/id6811297451"

APP = {
    "slug": "kaeroute",
    "theme": "kaeroute",
    "theme_color": "#F2F1EC",
    "store_id": "6811297451",
    "version": "1.0.0",
    "min_ios": "17.0",
    "checked": "2026-11-06",
    "langs": ("ja", "en"),
    "primary_lang": "ja",
    "shot_langs": ("ja",),
    "ui_languages": ["ja", "zh-Hant"],
    "schema_category": "UtilitiesApplication",
    "store_url": {"ja": JP, "en": JP},
    "offers": {
        "ja": [("カエルート", "0", "JPY", "1件の帰宅計画と保存済み情報の参照は無料"),
               ("カエルート Pro", "980", "JPY", "買い切りのApp内課金（サブスクリプションではありません）")],
        "en": [("Kaeroute", "0", "JPY", "One plan and viewing saved information are free"),
               ("Kaeroute Pro", "980", "JPY", "One-time in-app purchase on the Japan App Store, not a subscription")],
    },
    "t": {},
}

APP["t"]["ja"] = {
    "name": "カエルート",
    "store_name": "カエルート - 防災・徒歩帰宅ルート",
    "title": "カエルート：災害時の徒歩帰宅ルートを平常時に準備・オフライン保存するiPhoneアプリ",
    "description": "カエルートは、災害や交通機関の停止に備えて、職場・学校から自宅や集合場所までの徒歩ルートを平常時に準備し、地図と一緒に端末へ保存するiPhoneアプリです。電波がなくても確認でき、ProならA4のPDFで紙にも残せます。",
    "og_alt": "カエルートのアイコンと、保存した徒歩ルートの画面、帰宅計画のPDF",
    "hub_line_ja": "災害に備えて、職場や学校からの徒歩帰宅ルートを先に準備・保存。",
    "hub_line_en": "Prepare and save a walking route home from work or school before a disaster.",
    "hub_note_en": "The app is in Japanese and Traditional Chinese.",
    "headline": "帰る道を、<br>スマホにも、紙にも。",
    "lead": "カエルートは、災害や交通機関の停止に備えて、職場・学校から自宅や集合場所までの徒歩ルートを<strong>平常時に</strong>準備するiPhoneアプリです。地図とルートを先に保存しておけば、通信できないときも確認できます。",
    "price_note": "無料（1件の計画）。カエルート Pro は買い切り¥980。iOS 17.0以降。",
    "hero_shot": "route",
    "hero_alt": "帰宅計画「職場から集合場所へ」の画面。オフライン保存済み、3.8 km、約0時間47分、主経路と代替経路の切り替え、地図上の徒歩ルート、曲がり角の一覧",
    "summary": "カエルートは、発災後にその場で最適な経路を案内する災害ナビではありません。普段のうちに帰り道を調べて保存し、通信障害やスマートフォンが使えない場面でも、端末と紙で参照できるようにしておくための準備ツールです。",
    "facts": [
        ("正式名", "カエルート - 防災・徒歩帰宅ルート"),
        ("できること", "徒歩の帰宅ルートの作成、経由地点、距離・概算所要時間・曲がり角の確認、地図とルートのオフライン保存、Proで複数計画・代替経路・A4のPDFと印刷"),
        ("料金", "無料（1件の計画と、その主経路・必要な地図の保存）。カエルート Pro は買い切り¥980（サブスクリプションではありません）"),
        ("対応環境", "iPhone（iOS 17.0以降）"),
        ("言語", "日本語、繁体字中国語"),
        ("データの保存先", "地点・計画・メモは端末内。アカウント登録、アプリのクラウド同期、常時の位置追跡はありません"),
        ("地図・経路データ", "© OpenStreetMap contributors、openrouteservice（HeiGIT）"),
        ("カテゴリ", "ナビゲーション、ユーティリティ"),
        ("バージョン", "1.0.0（2026年9月24日公開）"),
        ("開発・提供", "Ryo Morishita"),
    ],
    "features_h": "準備する、保存する、参照する",
    "features": [
        {
            "id": "plan", "h": "平常時に、徒歩の帰宅ルートをつくる", "shot": "create",
            "alt": "帰宅計画の作成画面。出発地「職場（東京駅周辺）」、目的地「集合場所（上野公園）」、経由地点の追加、徒歩ルートの候補と地図",
            "body": "<p>出発地と目的地を検索して、徒歩ルートを作成します。通りたい場所は経由地点に設定できます。作成したルートは、距離、概算所要時間、曲がり角で確認できます。</p>"
                    "<p>職場や学校から自宅へ、あるいは家族との集合場所へ。普段歩かない長い道のりを、時間のあるときに一度たどっておけます。</p>",
        },
        {
            "id": "save", "h": "電波がないときのために、先に保存", "shot": "offline",
            "alt": "「地図を保存」画面。保存した帰宅ルートと周辺地図は通信がなくても確認できるという説明、オフライン保存済みの表示と容量",
            "body": "<p>計画と、その主経路、必要な地図を端末に保存します。保存状態と最終確認日が表示されるので、出発前に準備ができているかを確かめられます。</p>"
                    "<p>オフラインで見られるのは、保存が完了した地図・ルート・曲がり角などの情報です。地点検索、新しいルートの作成、地図のダウンロードにはインターネット接続が必要です。</p>",
        },
        {
            "id": "pdf", "h": "Proなら、A4のPDFで紙にも残せる", "shot": "pdf",
            "alt": "帰宅計画PDFのプレビュー。全体図と区間別地図、距離と所要時間が載ったA4のページ",
            "body": "<p>カエルート Pro では、全体図、区間別地図、曲がり角を含むA4のPDFを作成できます。PDFは共有やファイルへの保存ができ、AirPrint対応のプリンターで印刷できます。スマートフォン自体が使えない場合の備えになります。</p>",
        },
        {
            "id": "pro", "h": "Proで、代替経路と複数の計画", "shot": "alternative",
            "alt": "主経路、代替経路1、代替経路2を切り替えるタブがある帰宅計画の画面",
            "body": "<p>Pro では、主経路に加えて、得られた候補から代替経路を最大2件保存できます（代替経路は必ず生成されるとは限りません）。複数の帰宅・移動計画、注意しておきたい地点やメモ、計画の見直し通知も使えます。</p>"
                    "<p>Proはアプリ内で購入する買い切りで、サブスクリプションではありません。</p>",
        },
        {
            "id": "refer", "h": "必要なときだけ、現在地を確認",
            "body": "<p>保存したルートは、地図と曲がり角の一覧でたどれます。現在地はボタンを押したときだけ確認し、移動の履歴は残しません。</p>",
        },
    ],
    "steps": {
        "h": "カエルートの使い方",
        "items": [
            ("出発地と目的地を決める", "職場や学校と、自宅や集合場所を検索して選びます。通りたい場所があれば経由地点にします。"),
            ("ルートを確かめて保存する", "距離、所要時間、曲がり角を確認し、計画と地図を端末に保存します。"),
            ("ときどき見直す", "保存状態と最終確認日を確かめます。Proなら見直しの通知や、紙に残すPDFも使えます。"),
        ],
    },
    "gallery_h": "アプリの画面",
    "gallery": [
        ("route", "保存した帰宅計画"),
        ("offline", "地図の保存"),
        ("pdf", "帰宅計画のPDF（Pro）"),
        ("create", "帰宅計画の作成"),
        ("alternative", "代替経路（Pro）"),
        ("settings", "設定とデータの扱い"),
    ],
    "fit": [
        "電車やバスで通勤・通学していて、止まったときの帰り道を知らない人",
        "家族との集合場所までの道を、前もって確かめておきたい人",
        "通信できないときやスマートフォンが使えないときの備えを持っておきたい人",
        "職場や学校が複数ある人（複数の計画はPro）",
    ],
    "limits": [
        "災害が起きた後の道路状況や、ルートの安全性・通行できるかを保証するものではありません",
        "帰宅を始めるタイミングは判断しません",
        "オフラインで見られるのは、事前に保存が完了した情報だけです",
        "地図・経路は、提供データのある対応エリアで利用できます。未収録のエリアでは地図の保存を完了できない場合があります",
        "アプリの表示は日本語と繁体字中国語です",
    ],
    "faq": [
        ("what", "カエルートはどんなアプリですか？",
         "<p>災害や交通機関の停止に備えて、職場・学校から自宅や集合場所までの徒歩ルートを平常時に準備し、地図と一緒に端末へ保存するiPhoneアプリです。保存した情報は通信できないときも確認でき、Proなら紙に印刷して持っておけます。</p>"),
        ("navi", "災害が起きたときに、安全な道を案内してくれますか？",
         "<p>いいえ。カエルートは平常時の準備と、保存した計画の参照のためのツールです。災害後の道路状況や安全性を判断したり、リアルタイムで案内したりはしません。まず身の安全を確保し、行政・勤務先・学校などの情報と指示を優先してください。</p>"),
        ("offline", "電波がなくても使えますか？",
         "<p>事前に保存が完了した地図・ルート・曲がり角などは、通信できないときも確認できます。地点検索、新しいルートの作成、地図のダウンロードにはインターネット接続が必要なので、普段のうちに保存しておいてください。</p>"),
        ("price", "無料で使えますか？",
         "<p>1件の計画と、その主経路・必要な地図の保存、保存済み情報の参照は無料です。PDFの作成・印刷、代替経路、複数の計画、メモなどには、カエルート Pro（買い切り¥980）の購入が必要です。サブスクリプションではありません。</p>"),
        ("print", "ルートを紙に印刷できますか？",
         "<p>Proで、全体図、区間別地図、曲がり角を含むA4のPDFを作成できます。AirPrint対応のプリンターで印刷したり、ファイルとして保存・共有したりできます。</p>"),
        ("data", "自宅や勤務先の情報はどこに保存されますか？",
         "<p>地点・計画・メモは端末内に保存されます。アカウント登録は不要で、アプリのクラウド同期や常時の位置追跡はありません。地点検索とルート作成のときは、検索内容や出発地・目的地・経由地の座標を外部の地図・経路サービスへ送信します。詳しくは<a href=\"/kaeroute/ja/privacy/\">プライバシー</a>をご覧ください。</p>"),
        ("vs", "普段の地図アプリと何が違いますか？",
         "<p>地図アプリは、その場で検索して案内することが中心です。カエルートは、徒歩の帰宅ルートを先に作って保存し、通信できないときやスマートフォンが使えないときにも、端末と紙で参照できる状態をつくることに絞っています。</p>"),
        ("area", "どの地域で使えますか？",
         "<p>地図・経路は、提供データのある対応エリアで利用できます。未収録のエリアでは、地図の保存を完了できない場合があります。</p>"),
    ],
    "closing_h": "その場で探さない。帰る道を、先に持っておく。",
    "closing": "時間のある今日のうちに、いつもの場所からの帰り道をひとつ保存しておきましょう。",
    "notice": ("ご利用にあたって", "<p>カエルートは、平常時の準備と保存済み計画の参照のためのツールです。災害発生後の道路状況やルートの安全性・通行可能性を保証するものではなく、帰宅を開始するタイミングも判断しません。</p><p>まず身の安全を確保し、発災直後にむやみに移動を開始せず、行政・勤務先・学校などの情報と指示を優先してください。実際の状況に応じて、待機・迂回・引き返しを判断してください。</p>"),
    "privacy": {
        "title": "プライバシー｜カエルート",
        "description": "カエルートが端末内に保存する情報と、地点検索・ルート作成で外部サービスへ送る情報の概要。",
        "h1": "カエルートのプライバシー",
        "body": f"""<p>カエルートが扱う情報の概要です。App Storeに登録している正式なプライバシーポリシーは<a href="{POLICY}">こちら</a>です。</p>
<h2>端末内に保存する情報</h2>
<p>地点、帰宅計画、経路、メモ、保存した地図は端末内に保存します。アカウント登録は不要で、アプリのクラウド同期は行いません。保存したデータは、設定の「保存データをすべて削除」から削除できます。</p>
<h2>現在地</h2>
<p>現在地は、ボタンを押して確認するときだけ取得します。常時の位置追跡はせず、移動の履歴も残しません。</p>
<h2>外部サービスへ送る情報</h2>
<p>必要な機能のために、次の外部サービスを利用します。通信先にはIPアドレスなどの通信に伴う情報が伝わります。</p>
<ul>
<li>地点検索: Appleの地図サービス（MapKit）。入力した検索語句や検索対象地域</li>
<li>徒歩ルートの作成: openrouteservice（HeiGIT）。出発地・目的地・経由地点の座標と検索条件</li>
<li>地図の取得・ダウンロード: GitHubなどの配信基盤。要求するファイルから地図の対象エリアが分かる場合があります</li>
<li>Proの購入・復元: Apple App Store（StoreKit）</li>
</ul>
<p>地図データは © OpenStreetMap contributors です。アプリには広告トラッキングや行動解析のためのSDKを組み込んでいません。</p>
<h2>PDF</h2>
<p>「ファイル」などへ書き出したPDFは、その保存先で管理されます。</p>
<h2>お問い合わせ</h2>
<p><a href="mailto:{MAIL}">{MAIL}</a></p>""",
    },
    "support": {
        "title": "サポート｜カエルート",
        "description": "カエルートの地図の保存、オフラインでの確認、Proの購入についての確認項目と、お問い合わせ先。",
        "h1": "カエルートのサポート",
        "body": f"""<h2>ご利用にあたって</h2>
<p>カエルートは、平常時の準備と保存済み計画の参照のためのツールです。災害発生後の道路状況やルートの安全性・通行可能性を保証するものではなく、帰宅を開始するタイミングも判断しません。まず身の安全を確保し、発災直後にむやみに移動を開始せず、行政・勤務先・学校などの情報と指示を優先してください。実際の状況に応じて、待機・迂回・引き返しを判断してください。</p>
<h2>オフラインで地図が表示されない</h2>
<p>計画の画面で「オフライン保存済み」と表示されているか確認してください。保存が完了していない地図は、通信できないときに表示できません。未収録のエリアでは地図の保存を完了できない場合があります。</p>
<h2>ルートが作成できない・検索できない</h2>
<p>地点検索と新しいルートの作成にはインターネット接続が必要です。通信できる場所でもう一度お試しください。</p>
<h2>Proが使えない</h2>
<p>設定の「購入を復元」をお試しください。購入、支払い、返金はAppleの仕組みで処理されます。</p>
<h2>お問い合わせ</h2>
<p>解決しない場合は、<a href="mailto:{MAIL}">{MAIL}</a> までご連絡ください（件名に「カエルート」とご記入ください）。この窓口は緊急通報・救助要請には対応していません。アプリとiOSのバージョン、iPhoneの機種、起きたことと直前の操作を書いていただくと確認が早くなります。自宅などの具体的な住所を書く必要はありません。</p>""",
    },
}

APP["t"]["en"] = {
    "name": "Kaeroute",
    "store_name": "カエルート - 防災・徒歩帰宅ルート",
    "title": "Kaeroute (カエルート): Plan and Save a Walking Route Home for Disasters",
    "description": "Kaeroute is an iPhone app for planning a walking route home before a disaster or transit shutdown. Saved maps work offline; Pro makes printable PDFs. Japanese UI.",
    "og_alt": "The Kaeroute icon, a saved walking route and a printable route plan PDF",
    "hub_line_ja": "災害に備えて、職場や学校からの徒歩帰宅ルートを先に準備・保存。",
    "hub_line_en": "Prepare and save a walking route home from work or school before a disaster.",
    "hub_note_en": "The app is in Japanese and Traditional Chinese.",
    "headline": "Your way home, on your phone and on paper.",
    "lead": "Kaeroute (<span lang=\"ja\">カエルート</span>) is an iPhone app for preparing a walking route from your workplace or school to home or a family meeting point <strong>before</strong> a disaster or transit shutdown. Save the maps and route in advance and you can check them even without a connection.",
    "price_note": "The app's interface is in Japanese and Traditional Chinese. Free with one plan; Kaeroute Pro is a one-time ¥980 purchase on the Japan App Store. Requires iOS 17.0 or later.",
    "hero_shot": "route",
    "hero_alt": "A saved route plan in the Japanese interface: saved for offline use, 3.8 km, about 47 minutes, tabs for the main and alternative routes, the walking route on a map and a list of turns",
    "shot_note": "The app has no English interface, so these screens are shown in Japanese.",
    "summary": "Kaeroute is not a disaster navigation app that finds the best route after something happens. It's a preparation tool: look up your way home ahead of time, save it, and keep it available on your phone and on paper for when networks are down or your phone can't be used.",
    "facts": [
        ("Full name", "<span lang=\"ja\">カエルート - 防災・徒歩帰宅ルート</span> (Traditional Chinese name: <span lang=\"zh-Hant\">Kaeroute 返家路線・防災準備</span>)"),
        ("What it does", "Create walking routes home, add waypoints, check distance, estimated time and turns, save maps and routes for offline use; Pro adds multiple plans, alternative routes and printable A4 PDFs"),
        ("Price", "Free with one plan and its main route and maps. Kaeroute Pro is a one-time ¥980 purchase, not a subscription"),
        ("App languages", "Japanese and Traditional Chinese (no English interface)"),
        ("Availability", "Listed on the App Store in Japan and Taiwan as of November 6, 2026; it was not found on the US App Store"),
        ("Requirements", "iPhone with iOS 17.0 or later"),
        ("Where data is stored", "Places, plans and notes stay on your device. No account, no cloud sync and no continuous location tracking"),
        ("Map and route data", "© OpenStreetMap contributors, openrouteservice (HeiGIT)"),
        ("Category", "Navigation, Utilities"),
        ("Version", "1.0.0 (released September 24, 2026, Japan time)"),
        ("Developer", "Ryo Morishita"),
    ],
    "features_h": "Plan, save, refer",
    "features": [
        {
            "id": "plan", "h": "Plan a walking route home in normal times", "shot": "create",
            "alt": "Creating a route plan in Japanese: start near Tokyo Station, destination Ueno Park meeting point, add a waypoint, and a walking route on the map",
            "body": "<p>Search for a start and a destination and Kaeroute creates a walking route. Add waypoints for places you want to pass through, then check the distance, estimated walking time and turns.</p>"
                    "<p>From work or school to home, or to a meeting point with your family: walk through a long, unfamiliar route once while you have time.</p>",
        },
        {
            "id": "save", "h": "Save it before you lose signal", "shot": "offline",
            "alt": "Save maps screen in Japanese explaining that saved routes and nearby maps can be viewed without a connection, with saved status and size",
            "body": "<p>Save the plan, its main route and the maps it needs to your device. The saved status and the date you last checked are shown, so you can confirm you're ready.</p>"
                    "<p>Only maps, routes and turns that finished saving are available offline. Searching for places, creating new routes and downloading maps need an internet connection.</p>",
        },
        {
            "id": "pdf", "h": "Print it on A4 paper with Pro", "shot": "pdf",
            "alt": "Preview of a route plan PDF: an A4 page with an overview map, section maps, distance and time",
            "body": "<p>Kaeroute Pro creates an A4 PDF with an overview map, section maps and turns. Share it, save it to Files or print it with an AirPrint printer, so you have a backup if your phone can't be used.</p>",
        },
        {
            "id": "pro", "h": "Alternative routes and multiple plans with Pro", "shot": "alternative",
            "alt": "Route plan screen in Japanese with tabs to switch between the main route and alternative routes 1 and 2",
            "body": "<p>With Pro, save up to two alternative routes from the candidates found, in addition to the main route (alternatives aren't always available). You can also keep multiple plans, mark points to watch out for, add notes and get reminders to review your plans.</p>"
                    "<p>Pro is a one-time in-app purchase, not a subscription.</p>",
        },
        {
            "id": "refer", "h": "Check your location only when you need to",
            "body": "<p>Follow the saved route with the map and the list of turns. Your current location is checked only when you tap the button, and no movement history is kept.</p>",
        },
    ],
    "steps": {
        "h": "How Kaeroute works",
        "items": [
            ("Choose a start and a destination", "Search for your workplace or school and your home or meeting point. Add waypoints if you want to pass through specific places."),
            ("Check the route and save it", "Review distance, time and turns, then save the plan and maps to your device."),
            ("Review it from time to time", "Check the saved status and last-checked date. With Pro, get review reminders and print a PDF."),
        ],
    },
    "gallery_h": "Screens from the app",
    "gallery": [
        ("route", "A saved route plan"),
        ("offline", "Saving maps"),
        ("pdf", "Route plan PDF (Pro)"),
        ("create", "Creating a route plan"),
        ("alternative", "Alternative routes (Pro)"),
        ("settings", "Settings and data handling"),
    ],
    "fit": [
        "Commuters and students in Japan who rely on trains or buses and don't know the way home on foot",
        "Families who want to check the way to a meeting point in advance",
        "Anyone who wants a backup for when networks are down or a phone can't be used",
        "People with more than one workplace or school (multiple plans need Pro)",
    ],
    "limits": [
        "It doesn't guarantee road conditions after a disaster, or that a route is safe or passable",
        "It doesn't decide when you should start walking home",
        "Only information that finished saving beforehand is available offline",
        "Maps and routes work in supported areas with available data; maps may not finish saving outside them",
        "The interface is in Japanese and Traditional Chinese only",
    ],
    "faq": [
        ("what", "What is Kaeroute?",
         "<p>Kaeroute is an iPhone app for preparing, in normal times, a walking route from work or school to home or a meeting point, and saving it on your device with the maps it needs. Saved information can be viewed without a connection, and with Pro you can print it.</p>"),
        ("english", "Is Kaeroute available in English?",
         "<p>No. The app's interface is in Japanese and Traditional Chinese. As of November 6, 2026, it is listed on the App Store in Japan and Taiwan, and it was not found on the US App Store.</p>"),
        ("navi", "Will it guide me along a safe route during a disaster?",
         "<p>No. Kaeroute is for preparing in advance and referring to saved plans. It doesn't assess road conditions or safety after a disaster or give real-time guidance. Stay safe first and follow information and instructions from authorities, your workplace or school.</p>"),
        ("offline", "Does it work without a signal?",
         "<p>Maps, routes and turns that finished saving beforehand can be viewed offline. Searching for places, creating new routes and downloading maps need an internet connection, so save them ahead of time.</p>"),
        ("price", "Is Kaeroute free?",
         "<p>One plan with its main route and maps, and viewing saved information, are free. PDF export and printing, alternative routes, multiple plans and notes require Kaeroute Pro, a one-time ¥980 purchase on the Japan App Store. It is not a subscription.</p>"),
        ("data", "Where are my home and workplace stored?",
         "<p>Places, plans and notes are stored on your device. No account is needed, and there is no cloud sync or continuous location tracking. When you search for places or create routes, the search text and the coordinates of the start, destination and waypoints are sent to external map and routing services. See <a href=\"/kaeroute/en/privacy/\">Privacy</a> for details.</p>"),
    ],
    "closing_h": "Don't search on the spot. Have your way home ready.",
    "closing": "While you have time today, save one route home from a place you go every day.",
    "notice": ("Before you rely on it", "<p>Kaeroute is for preparing in normal times and referring to saved plans. It doesn't guarantee road conditions, safety or whether a route is passable after a disaster, and it doesn't decide when to start walking home.</p><p>Stay safe first, don't start moving right after a disaster without need, and follow information and instructions from authorities, your workplace or school. Decide whether to wait, detour or turn back based on the actual situation.</p>"),
    "privacy": {
        "title": "Privacy | Kaeroute (カエルート)",
        "description": "What Kaeroute stores on your device and what it sends to map and routing services when you search or create routes.",
        "h1": "Kaeroute privacy",
        "body": f"""<p>A summary of the information Kaeroute handles. The privacy policy registered on the App Store is available <a href="{POLICY}">here</a> (in Japanese).</p>
<h2>Stored on your device</h2>
<p>Places, route plans, routes, notes and saved maps are stored on your device. No account is needed and there is no cloud sync of the app's own. You can delete all saved data from the app's settings.</p>
<h2>Current location</h2>
<p>Your current location is read only when you tap the button to check it. There's no continuous tracking and no movement history.</p>
<h2>Sent to external services</h2>
<p>Kaeroute uses these external services for the features that need them. Each service receives information that comes with any connection, such as your IP address.</p>
<ul>
<li>Place search: Apple's map service (MapKit), which receives your search text and search area</li>
<li>Walking routes: openrouteservice (HeiGIT), which receives the coordinates of the start, destination and waypoints and the search conditions</li>
<li>Map downloads: distribution services such as GitHub; the files requested may reveal which map area you need</li>
<li>Buying and restoring Pro: Apple App Store (StoreKit)</li>
</ul>
<p>Map data is © OpenStreetMap contributors. The app has no SDKs for ad tracking or behavioral analytics.</p>
<h2>PDFs</h2>
<p>PDFs exported to Files or elsewhere are managed by wherever you save them.</p>
<h2>Contact</h2>
<p><a href="mailto:{MAIL}">{MAIL}</a></p>""",
    },
    "support": {
        "title": "Support | Kaeroute (カエルート)",
        "description": "Notes on using Kaeroute, saving maps for offline use and Pro, and how to contact the developer.",
        "h1": "Kaeroute support",
        "body": f"""<h2>Before you rely on it</h2>
<p>Kaeroute is for preparing in normal times and referring to saved plans. It doesn't guarantee road conditions, safety or whether a route is passable after a disaster, and it doesn't decide when to start walking home. Stay safe first, don't start moving right after a disaster without need, and follow information and instructions from authorities, your workplace or school. Decide whether to wait, detour or turn back based on the actual situation.</p>
<h2>Maps don't appear offline</h2>
<p>Check that the plan shows it has been saved for offline use. Maps that didn't finish saving can't be shown without a connection, and maps may not finish saving outside supported areas.</p>
<h2>I can't search or create a route</h2>
<p>Searching for places and creating new routes need an internet connection. Try again where you have a connection.</p>
<h2>Pro isn't available</h2>
<p>Try Restore Purchases in the app's settings. Purchases, payments and refunds are handled by Apple.</p>
<h2>Contact</h2>
<p>Email <a href="mailto:{MAIL}">{MAIL}</a> with "Kaeroute" in the subject. This address cannot handle emergency calls or rescue requests. Include your app and iOS versions, iPhone model, what happened and what you did just before. You don't need to include your home address.</p>""",
    },
}
