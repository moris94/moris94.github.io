"""GeoAlbum — facts: docs/website/app-information.md (App Store 1.1.0, checked 2026-11-06)."""

POLICY = "https://bottlenose-network-d4d.notion.site/GeoAlbum-3dd661a42a4a80a4940ffe0ed93721e0"
MAIL = "shunmemo.support@gmail.com"

RINGS = """<svg class="rings" viewBox="0 0 400 400" aria-hidden="true" focusable="false">
<circle cx="200" cy="200" r="190"/><circle cx="200" cy="200" r="135"/><circle cx="200" cy="200" r="80"/>
</svg>"""

APP = {
    "slug": "geoalbum",
    "theme": "geoalbum",
    "theme_color": "#F6F8FB",
    "store_id": "6813050203",
    "version": "1.1.0",
    "min_ios": "18.0",
    "checked": "2026-11-06",
    "langs": ("en", "ja"),
    "primary_lang": "en",
    "ui_languages": ["en", "ja"],
    "schema_category": "MultimediaApplication",
    "store_url": {
        "ja": "https://apps.apple.com/jp/app/id6813050203",
        "en": "https://apps.apple.com/us/app/id6813050203",
    },
    "offers": {
        "ja": [("GeoAlbum", "0", "JPY", "場所ルール1つまで無料"),
               ("GeoAlbum Pro", "1100", "JPY", "買い切りのApp内課金。複数の場所ルールとまとめてスキャン")],
        "en": [("GeoAlbum", "0", "USD", "Free with one location rule"),
               ("GeoAlbum Pro", "6.99", "USD", "One-time in-app purchase: multiple location rules and scanning them together")],
    },
    "t": {},
}

APP["t"]["ja"] = {
    "name": "GeoAlbum",
    "store_name": "GeoAlbum",
    "title": "GeoAlbum：撮影場所で写真をApple「写真」のアルバムへ整理するiPhoneアプリ",
    "description": "GeoAlbumは、保存した場所ルールで撮影位置が一致する写真を見つけ、確認した写真をApple「写真」のアルバムへまとめて追加するiPhoneアプリです。照合は端末内。1ルールは無料、Proは買い切り。",
    "og_alt": "GeoAlbumのアイコンと、場所ルールで見つかった写真の確認画面",
    "hub_line_ja": "同じ場所で撮った写真を、いつもの「写真」アルバムへまとめて追加。",
    "hub_line_en": "Add photos taken at the same place to your usual Apple Photos album in one go.",
    "headline": "場所を登録。写真を確認。<br>いつものアルバムへ。",
    "lead": "GeoAlbumは、保存した「場所ルール」に撮影位置が一致する写真を見つけ、あなたが確認した写真をApple「写真」のアルバムへまとめて追加するiPhoneアプリです。写真の原本を移動・削除・複製することはありません。",
    "price_note": "無料（場所ルール1つ）。GeoAlbum Proは買い切り¥1,100。iOS 18.0以降。",
    "hero_art": RINGS,
    "hero_shot": "album",
    "hero_alt": "場所ルール「いつものカフェ」の候補写真12枚がチェックされ、「12枚をアルバムに追加」ボタンが表示された画面",
    "summary": "GeoAlbumは、店舗、作業場所、施設、趣味の場所など、同じ場所で繰り返し撮る写真の整理を短くするユーティリティです。写真はApple「写真」に残したまま、決まったアルバムへの追加だけを手伝います。撮影位置と場所ルールの照合は端末内で行い、写真や撮影位置をGeoAlbum独自のサーバーへ送りません。",
    "facts": [
        ("正式名", "GeoAlbum"),
        ("できること", "場所と範囲を保存し、撮影位置が一致する写真を見つけて、確認した写真をApple「写真」のアルバムへ追加"),
        ("料金", "無料（場所ルール1つ）。GeoAlbum Pro（買い切り）¥1,100で複数の場所ルールとまとめてスキャン"),
        ("対応環境", "iPhone（iOS 18.0以降）。App Storeの互換性表示では、Apple M1以降のMac（macOS 15.0以降）とApple Vision Pro（visionOS 2.0以降）にも対応"),
        ("言語", "日本語、英語"),
        ("対象の写真", "撮影位置が記録された写真とLive Photos。動画、非表示の写真、撮影位置のない写真は対象外"),
        ("プライバシー", "照合は端末内。アカウント登録、広告、行動追跡なし"),
        ("カテゴリ", "写真/ビデオ、ユーティリティ"),
        ("バージョン", "1.1.0（2026年10月1日公開）"),
        ("開発・提供", "Ryo Morishita"),
    ],
    "features_h": "GeoAlbumでできること",
    "features": [
        {
            "id": "rules", "h": "場所ルールを一度保存して、何度でも使う", "shot": "rules",
            "alt": "場所ルールの一覧。「工房」のルールと保存先アルバム「工房の記録」、前回の追加日時が表示されている",
            "body": "<p>場所と範囲（半径）、追加先のアルバムを「場所ルール」として保存します。一度作ったルールは、その場所で新しく撮った写真を整理するたびに使えます。</p>"
                    "<p>毎週同じ店舗で撮る商品の写真、継続して通う現場の記録、同じ施設での趣味の写真など、写真が増え続ける場所に向いています。</p>",
        },
        {
            "id": "place", "h": "地図、住所・施設名、写真から場所を指定", "shot": "place",
            "alt": "場所を指定する地図画面。中央のピンの周りに範囲を示す円が描かれ、「この場所を使う」ボタンがある",
            "body": "<p>場所は地図、住所・施設名の検索、またはその場所で撮影した写真の撮影位置から指定できます。「現在地へ」を押すと、地図を現在地付近から始められます。位置情報の許可を求めるのはこのボタンを押したときだけで、最初のピンを置くためだけに使います。</p>",
        },
        {
            "id": "review", "h": "追加する前に、自分で確認", "shot": "review",
            "alt": "候補写真の一覧の上に「アルバムに追加しますか？」という確認と「10枚を追加」ボタンが表示された画面",
            "body": "<p>見つかった写真は候補として表示され、追加する写真をあなたが選んでから、アルバムへまとめて追加します。確認なしに自動で追加することはありません。</p>"
                    "<p>同じアルバムに追加済みの写真はスキップします。ルールを変更・削除しても、写真とアルバムはそのまま残ります。</p>",
        },
        {
            "id": "pro", "h": "複数の場所をまとめて整理（GeoAlbum Pro）", "shot": "multi",
            "alt": "「工房」「店舗」「テニスコート」の3つの場所ルールが並び、それぞれ確認待ちの写真の枚数が表示されている",
            "body": "<p>無料で使える場所ルールは1つです。GeoAlbum Pro（買い切りのApp内課金）を購入すると、複数の場所ルールを作り、まとめてスキャンできます。サブスクリプションではありません。</p>",
        },
        {
            "id": "privacy", "h": "照合は端末の中だけで", "shot": "privacy",
            "alt": "GeoAlbumのプライバシー画面。端末内で分類すること、保存する情報、Appleのサービス、診断情報の説明",
            "body": "<p>写真の撮影位置と場所ルールの照合は端末内で行います。GeoAlbum独自のサーバーへ写真や撮影位置を送ることはなく、アカウント登録、広告、行動追跡もありません。</p>",
        },
    ],
    "steps": {
        "h": "GeoAlbumの使い方",
        "items": [
            ("場所と範囲を登録する", "地図、検索、または写真の撮影位置から場所を選び、範囲を決めます。"),
            ("追加先のアルバムを選ぶ", "Apple「写真」の既存のアルバムを選ぶか、新しく作ります。"),
            ("見つかった写真を確認して追加する", "候補の中から追加する写真を確かめ、まとめてアルバムへ追加します。"),
        ],
    },
    "gallery_h": "アプリの画面",
    "gallery": [
        ("album", "場所ルールで見つかった候補写真"),
        ("rules", "場所ルールの一覧"),
        ("review", "アルバムへの追加の確認"),
        ("place", "地図で場所と範囲を指定"),
        ("multi", "複数の場所ルール（Pro）"),
        ("privacy", "プライバシーの説明画面"),
    ],
    "fit": [
        "同じ店舗、現場、施設などで繰り返し写真を撮る人",
        "撮った写真を、決まったアルバムへ手作業でまとめている人",
        "iPhone標準のカメラとApple「写真」を使い続けたい人",
        "写真をほかのサービスへアップロードせずに整理したい人",
    ],
    "limits": [
        "撮影位置が記録されていない写真は見つけられません。撮影場所を推定することもしません",
        "動画と非表示の写真は対象外です",
        "写真の内容（写っているもの）で分類する機能はありません",
        "写真へのアクセスを「選択した写真のみ」にしている場合、許可していない写真は検索の対象になりません",
        "地図の表示、住所・施設名の検索、iCloud写真の読み込み、購入には通信が必要な場合があります",
    ],
    "faq": [
        ("what", "GeoAlbumはどんなアプリですか？",
         "<p>撮影場所をもとに写真を見つけ、確認した写真をApple「写真」のアルバムへまとめて追加するiPhoneアプリです。場所ルールを一度保存すれば、同じ場所で撮った写真の整理を何度でも繰り返せます。</p>"),
        ("price", "無料で使えますか？",
         "<p>場所ルール1つまで無料で使えます。複数の場所ルールとまとめてスキャンは、GeoAlbum Pro（買い切り、日本のApp Storeで¥1,100）で利用できます。価格は国や地域によって異なります。</p>"),
        ("original", "写真の原本は変更されますか？",
         "<p>いいえ。GeoAlbumは写真の原本を移動・削除・複製しません。写真はApple「写真」のライブラリに残ったまま、指定したアルバムに追加されるだけです。</p>"),
        ("auto", "撮影するたびに自動でアルバムへ追加されますか？",
         "<p>いいえ。GeoAlbumが候補を見つけ、追加する写真はあなたが確認して決めます。確認なしに自動で追加することはありません。</p>"),
        ("nolocation", "位置情報がない写真も整理できますか？",
         "<p>できません。GeoAlbumは写真に記録された撮影位置を使います。撮影位置がない写真の場所を推定する機能はありません。</p>"),
        ("offline", "インターネット接続は必要ですか？",
         "<p>撮影位置と場所ルールの照合は端末内で行います。地図の表示、住所・施設名の検索、iCloudに保存された写真の読み込み、購入には通信が必要な場合があります。</p>"),
        ("data", "写真や位置情報はどこに送られますか？",
         "<p>GeoAlbum独自のサーバーへ写真や撮影位置を送ることはありません。地図や検索、購入にはAppleのサービスを使います。詳しくは<a href=\"/geoalbum/ja/privacy/\">プライバシー</a>をご覧ください。</p>"),
        ("vs", "Apple「写真」の検索や「マップ」表示と何が違いますか？",
         "<p>「写真」アプリでも場所で写真を探せますが、見つけた写真を毎回選んでアルバムへ追加する作業は手作業です。GeoAlbumは場所と追加先を「場所ルール」として保存し、その作業を繰り返し短くすることに絞ったアプリです。</p>"),
    ],
    "closing_h": "まずは1つの場所から",
    "closing": "よく写真を撮る場所をひとつ登録して、いつものアルバムへの追加を試してみてください。",
    "privacy": {
        "title": "プライバシー｜GeoAlbum",
        "description": "GeoAlbumが扱う写真・撮影位置・場所ルールの概要。照合は端末内で、独自サーバーへの送信はありません。",
        "h1": "GeoAlbumのプライバシー",
        "body": f"""<p>GeoAlbumが扱う情報の概要です。App Storeに登録している正式なポリシーは<a href="{POLICY}">こちら</a>です。</p>
<h2>写真ライブラリ</h2>
<p>撮影位置の確認、場所ルールに一致する候補写真の検索とサムネイル表示、確認した写真のアルバムへの追加、保存先アルバムの表示と作成、追加済みの判定のために、Apple「写真」のライブラリへアクセスします。アクセス範囲はiOSの「設定」からいつでも変更できます。</p>
<h2>撮影位置と現在地</h2>
<p>写真に記録された緯度・経度を、保存した場所ルールと照合します。照合は端末内で行います。「現在地へ」を押したときだけ位置情報（使用中のみ）の許可を求め、地図の最初のピンを現在地に置くためだけに使います。</p>
<h2>端末内に保存する情報</h2>
<p>場所ルール（場所と範囲、保存先アルバムの参照）、候補写真の参照、選択・除外の状態、前回の整理結果、購入の状態を端末内に保存します。写真のコピーは保存しません。</p>
<h2>外部との通信</h2>
<p>GeoAlbumは、写真、撮影位置、場所ルール、アルバム名をGeoAlbum独自のサーバーへ送りません。地図の表示、住所・施設名の検索、iCloud写真の読み込み、App内課金と復元では、Appleのサービスと通信する場合があります。</p>
<h2>アカウント、広告、トラッキング</h2>
<p>アカウント登録、第三者広告、アプリやWebサイトをまたいだ追跡はありません。</p>
<h2>診断情報</h2>
<p>お問い合わせのときに、診断情報を自分で確認して共有できます。自動では送信されず、写真、撮影位置、場所ルールの名前、アルバム名は含みません。</p>
<h2>お問い合わせ</h2>
<p><a href="mailto:{MAIL}">{MAIL}</a></p>""",
    },
    "support": {
        "title": "サポート｜GeoAlbum",
        "description": "GeoAlbumで写真が見つからない、アルバムが表示されないときの確認項目と、お問い合わせ先。",
        "h1": "GeoAlbumのサポート",
        "body": f"""<h2>写真が見つからない</h2>
<ul>
<li>写真に撮影位置が記録されているか</li>
<li>GeoAlbumに写真へのアクセスが許可されているか（「選択した写真のみ」の場合、許可していない写真は対象外）</li>
<li>登録した場所と範囲が、写真の撮影位置を含んでいるか</li>
<li>写真が非表示になっていないか、動画ではないか</li>
<li>iCloudの写真を端末へ読み込める状態か</li>
<li>すでに保存先のアルバムへ追加済みではないか</li>
</ul>
<h2>アルバムが表示されない</h2>
<p>iPhoneの「設定」でGeoAlbumの写真アクセスを確認してください。既存のアルバムをすべて使うには、写真へのフルアクセスが必要な場合があります。保存先のアルバムを「写真」で削除した場合は、GeoAlbumで保存先を選び直してください。</p>
<h2>GeoAlbum Proが使えない</h2>
<p>アプリ内の「購入を復元」をお試しください。購入、支払い、返金はAppleの仕組みで処理されます。</p>
<h2>お問い合わせ</h2>
<p>解決しない場合は、<a href="mailto:{MAIL}">{MAIL}</a> までご連絡ください。GeoAlbumとiOSのバージョン、iPhoneの機種、起きたこと、直前の操作、表示されたメッセージを書いていただくと確認が早くなります。写真や具体的な住所を添付する必要はありません。</p>""",
    },
}

APP["t"]["en"] = {
    "name": "GeoAlbum",
    "store_name": "GeoAlbum: Sort Photos by Place",
    "title": "GeoAlbum: Sort Photos by Place into Apple Photos Albums",
    "description": "GeoAlbum finds photos taken at places you save and adds the ones you confirm to an Apple Photos album. On-device matching. One rule free; Pro is one-time.",
    "og_alt": "The GeoAlbum icon and the screen for reviewing photos found by a location rule",
    "hub_line_ja": "同じ場所で撮った写真を、いつもの「写真」アルバムへまとめて追加。",
    "hub_line_en": "Add photos taken at the same place to your usual Apple Photos album in one go.",
    "headline": "Save a place.<br>Review the photos.<br>Add them to your album.",
    "lead": "GeoAlbum is an iPhone app that finds photos whose recorded location matches a saved location rule, then adds the photos you confirm to an album in Apple Photos. It never moves, deletes or copies your originals.",
    "price_note": "Free with one location rule. GeoAlbum Pro is a one-time $6.99 purchase. Requires iOS 18.0 or later.",
    "hero_art": RINGS,
    "hero_shot": "album",
    "hero_alt": "Twelve matching photos for the location rule Favorite Cafe, all checked, with an Add 12 Photos to Album button",
    "summary": "GeoAlbum shortens a repetitive job: sorting photos you keep taking at the same shops, worksites, facilities or hobby spots into the same album. Your photos stay in Apple Photos; GeoAlbum only helps add them to the album you choose. Locations are matched against your rules on your device, and photos and their locations are never sent to GeoAlbum's own servers.",
    "facts": [
        ("Full name", "GeoAlbum: Sort Photos by Place"),
        ("What it does", "Save a place and radius, find photos taken there, review them and add the ones you choose to an Apple Photos album"),
        ("Price", "Free with one location rule. GeoAlbum Pro, a one-time $6.99 purchase in the US, adds multiple rules and scanning them together"),
        ("Requirements", "iPhone with iOS 18.0 or later. The App Store also lists Macs with Apple M1 or later (macOS 15.0 or later) and Apple Vision Pro (visionOS 2.0 or later)"),
        ("Languages", "English, Japanese"),
        ("Supported photos", "Photos and Live Photos with a recorded location. Videos, hidden photos and photos without location data are excluded"),
        ("Privacy", "Matching happens on your device. No account, ads or behavioral tracking"),
        ("Category", "Photo &amp; Video, Utilities"),
        ("Version", "1.1.0 (released October 1, 2026)"),
        ("Developer", "Ryo Morishita"),
    ],
    "features_h": "What you can do with GeoAlbum",
    "features": [
        {
            "id": "rules", "h": "Save a location rule once, reuse it", "shot": "rules",
            "alt": "List of location rules showing the Workshop rule, its destination album and when photos were last added",
            "body": "<p>A location rule is a place, a radius and a destination album. Once it's saved, reuse it whenever you've taken new photos there.</p>"
                    "<p>It suits places where photos keep piling up: product photos at the same shop each week, records of a worksite you visit regularly, or a club you go to.</p>",
        },
        {
            "id": "place", "h": "Choose a place on the map, by search, or from a photo", "shot": "place",
            "alt": "Map screen for choosing a place, with a circle showing the radius around the pin and a Use This Place button",
            "body": "<p>Pick a place on the map, search by address or place name, or use the location recorded in a photo taken there. Tap Use Current Location to start the map near you; location permission is requested only when you tap it, and only to place the first pin.</p>",
        },
        {
            "id": "review", "h": "You review before anything is added", "shot": "review",
            "alt": "Matching photos with a confirmation asking Add to Album? and an Add 10 Photos button",
            "body": "<p>Matches appear as candidates. You choose which ones to keep, then add them to the album in one step. Nothing is added without your confirmation.</p>"
                    "<p>Photos already in the destination album are skipped, and changing or deleting a rule leaves your photos and albums untouched.</p>",
        },
        {
            "id": "pro", "h": "Sort several places at once with GeoAlbum Pro", "shot": "multi",
            "alt": "Three location rules, Workshop, Shop and Tennis Court, each showing how many photos are waiting for review",
            "body": "<p>The free version includes one location rule. GeoAlbum Pro, a one-time in-app purchase, unlocks multiple rules and scanning them together. It is not a subscription.</p>",
        },
        {
            "id": "privacy", "h": "Matching stays on your device", "shot": "privacy",
            "alt": "GeoAlbum's privacy screen explaining on-device sorting, stored data, Apple services and diagnostics",
            "body": "<p>Photo locations are matched against your rules on your device. GeoAlbum doesn't send photos or their locations to its own servers, and there are no accounts, ads or behavioral tracking.</p>",
        },
    ],
    "steps": {
        "h": "How GeoAlbum works",
        "items": [
            ("Save a place and radius", "Choose a place on the map, by search, or from a photo's location, and set the radius."),
            ("Choose a destination album", "Pick an existing album in Apple Photos or create a new one."),
            ("Review the matches and add them", "Check the candidates and add the photos you choose to the album in one go."),
        ],
    },
    "gallery_h": "Screens from the app",
    "gallery": [
        ("album", "Matching photos for a location rule"),
        ("rules", "Location rules"),
        ("review", "Confirming before adding to the album"),
        ("place", "Choosing a place and radius on the map"),
        ("multi", "Several location rules with Pro"),
        ("privacy", "Privacy screen"),
    ],
    "fit": [
        "People who keep taking photos at the same shops, sites or facilities",
        "Anyone who sorts those photos into the same album by hand",
        "People who want to keep using the iPhone Camera and Apple Photos",
        "Anyone who wants to organize photos without uploading them to another service",
    ],
    "limits": [
        "Photos without a recorded location can't be found, and GeoAlbum doesn't guess where they were taken",
        "Videos and hidden photos are excluded",
        "It doesn't sort photos by what's in them",
        "With Limited Access to Photos, photos you haven't shared with GeoAlbum aren't searched",
        "Maps, address and place search, iCloud photo downloads and purchases may need an internet connection",
    ],
    "faq": [
        ("what", "What does GeoAlbum do?",
         "<p>GeoAlbum finds photos by where they were taken and adds the ones you confirm to an album in Apple Photos. Save a location rule once and repeat the same sorting whenever you take more photos there.</p>"),
        ("price", "Is GeoAlbum free?",
         "<p>You can use one location rule for free. Multiple rules and scanning them together come with GeoAlbum Pro, a one-time purchase ($6.99 on the US App Store). Prices vary by country or region.</p>"),
        ("original", "Does GeoAlbum change my original photos?",
         "<p>No. GeoAlbum never moves, deletes or copies originals. Your photos stay in your Apple Photos library and are simply added to the album you choose.</p>"),
        ("auto", "Are photos added automatically every time I take one?",
         "<p>No. GeoAlbum finds candidates and you decide which photos to add. Nothing is added without your confirmation.</p>"),
        ("nolocation", "Can it sort photos that have no location data?",
         "<p>No. GeoAlbum relies on the location recorded in each photo and doesn't estimate where other photos were taken.</p>"),
        ("offline", "Does GeoAlbum need an internet connection?",
         "<p>Matching photo locations against your rules happens on your device. Showing maps, searching for addresses or places, downloading photos stored in iCloud, and purchases may need a connection.</p>"),
        ("data", "Where are my photos and locations sent?",
         "<p>GeoAlbum doesn't send photos or their locations to its own servers. Maps, search and purchases use Apple services. See <a href=\"/geoalbum/en/privacy/\">Privacy</a> for details.</p>"),
        ("vs", "How is this different from searching by place in Apple Photos?",
         "<p>Apple Photos can show photos by place, but adding them to an album means selecting them by hand each time. GeoAlbum saves the place and the destination album as a rule, focusing on making that repeated step quick.</p>"),
    ],
    "closing_h": "Start with one place",
    "closing": "Save a place where you often take photos and try adding them to your usual album.",
    "privacy": {
        "title": "Privacy | GeoAlbum",
        "description": "How GeoAlbum handles photos, photo locations and location rules: matching on device, nothing sent to its own servers.",
        "h1": "GeoAlbum privacy",
        "body": f"""<p>A summary of the information GeoAlbum handles. The policy registered on the App Store is available <a href="{POLICY}">here</a> (in Japanese).</p>
<h2>Photo library</h2>
<p>GeoAlbum accesses your Apple Photos library to read recorded locations, find and show matching candidates, add the photos you confirm to an album, show and create destination albums, and check which photos are already in an album. You can change its access at any time in iOS Settings.</p>
<h2>Photo locations and current location</h2>
<p>The latitude and longitude recorded in photos are matched against your saved rules on your device. Location permission (While Using) is requested only when you tap Use Current Location, and is used only to place the first pin on the map.</p>
<h2>Stored on your device</h2>
<p>Location rules (place, radius and a reference to the destination album), references to candidate photos, selection and exclusion state, the last sorting result and purchase state. GeoAlbum doesn't keep its own copies of photos.</p>
<h2>Network</h2>
<p>GeoAlbum doesn't upload photos, photo locations, rule names or album names to its own servers. Maps, address and place search, iCloud photo downloads, and in-app purchases and restores may communicate with Apple services.</p>
<h2>Accounts, ads and tracking</h2>
<p>There are no accounts, no third-party ads and no tracking across apps or websites.</p>
<h2>Diagnostics</h2>
<p>When contacting support, you can review diagnostics and choose to share them yourself. They're never sent automatically and don't include photos, photo locations, rule names or album names.</p>
<h2>Contact</h2>
<p><a href="mailto:{MAIL}">{MAIL}</a></p>""",
    },
    "support": {
        "title": "Support | GeoAlbum",
        "description": "What to check when GeoAlbum doesn't find photos or show albums, and how to contact the developer.",
        "h1": "GeoAlbum support",
        "body": f"""<h2>Photos aren't found</h2>
<ul>
<li>Does the photo have a recorded location?</li>
<li>Is GeoAlbum allowed to access your photos? With Limited Access, photos you haven't shared aren't searched</li>
<li>Does the place and radius include where the photo was taken?</li>
<li>Is the photo hidden, or is it a video?</li>
<li>Can the photo be downloaded from iCloud to the device?</li>
<li>Is it already in the destination album?</li>
</ul>
<h2>Albums don't appear</h2>
<p>Check GeoAlbum's photo access in your iPhone's Settings. Using all existing albums may require full photo access. If you deleted the destination album in Photos, choose a new one in GeoAlbum.</p>
<h2>GeoAlbum Pro isn't available</h2>
<p>Try Restore Purchases in the app. Purchases, payments and refunds are handled by Apple.</p>
<h2>Contact</h2>
<p>If you still need help, email <a href="mailto:{MAIL}">{MAIL}</a> with your GeoAlbum and iOS versions, iPhone model, what happened, what you did just before and any message shown. You don't need to attach photos or exact addresses.</p>""",
    },
}
