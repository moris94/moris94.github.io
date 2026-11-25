"""Editorial guides grounded in existing published feature descriptions.
No claims of new device testing, performance gains, or independent reviews.
"""
GUIDES = {
 'kaeroute': {
  'slug':'prepare-walking-route',
  'title':'徒歩帰宅ルートの地図をオフライン保存し、PDFで印刷する方法',
  'description':'カエルートで職場から自宅までの徒歩帰宅ルートと地図を事前に保存し、通信なしで参照する準備と、ProでA4の経路図をPDF出力・印刷する手順。',
  'preview':('経路図を紙に残すなら','ProのPDFには全体図・区間別地図・曲がり角が入ります。まず無料の1計画で、職場から自宅までの経路を作成・保存できます。','pdf','カエルートのA4経路図の出力画面'),
  'lead':'カエルートは、職場や学校から自宅・集合場所への徒歩帰宅ルートを平常時に準備するiPhoneアプリです。保存が完了した地図・経路・曲がり角はオフラインで確認でき、ProではA4のPDFにして印刷できます。',
  'before':'徒歩経路と周辺のオフライン地図を確認するだけなら、iPhoneの「マップ」から始められます。職場から自宅までの経由地点や曲がり角を計画としてまとめ、端末と紙の両方に残したいときは、カエルートで保存し、ProのA4 PDF出力を使えます。災害時に帰宅を始めるかは、行政・勤務先・学校の指示を優先してください。',
  'steps':[
   ('出発地・目的地から計画をつくる','職場や学校、自宅や集合場所を検索して選び、必要なら経由地点を追加します。距離、概算所要時間、曲がり角を確認します。表示される所要時間は、災害時の実際の移動時間を保証するものではありません。','create'),
   ('必要な地図とルートを先に保存する','インターネットに接続できる間に、計画と主経路・必要な地図を保存します。保存状態と最終確認日を確認してください。未収録の地域では地図の保存を完了できない場合があります。','offline'),
   ('保存した計画を参照し、定期的に見直す','オフラインで参照できるのは保存が完了した情報だけです。準備時には通信を切った状態でも必要な画面を参照できるか、ご自身の端末で確認してください。地点検索や新しい経路作成には通信が必要です。','route'),
   ('紙にも残すならProでPDFを作成する','カエルート Proでは全体図・区間別地図・曲がり角を含むA4のPDFを作成できます。ファイルへ保存・共有でき、AirPrint対応プリンターで印刷できます。スマートフォン以外の参照手段として準備します。','pdf')],
  'limits':'発災後の道路状況、安全性・通行可能性を保証せず、帰宅を始めるタイミングも判断しません。まず身の安全を確保し、行政・勤務先・学校の情報や指示を優先してください。',
  'decision':'まず無料の1計画で保存までの手順を確かめ、複数計画・代替経路・紙への出力が必要ならProの内容を確認してください。アプリの画面言語は日本語・繁体字中国語です。'
 },
 'geoalbum': {
  'slug':'organize-photos-by-place',
  'title':'同じ場所で撮ったiPhone写真を既存のアルバムにまとめる方法',
  'description':'GeoAlbumで店舗や作業場所のルールを保存し、撮影場所で絞った写真を確認して、Apple「写真」の既存アルバムへ繰り返し追加する手順。',
  'lead':'GeoAlbumは、同じ店舗や作業場所で繰り返し撮った写真を、Apple「写真」の既存アルバムに追加するiPhoneアプリです。保存した場所と範囲から候補を探し、選んだ写真だけを追加します。原本は写真ライブラリに残ります。',
  'before':'撮影場所を地図で見たり、その場で数枚を選んでアルバムへ追加したりするなら、iPhone標準の「写真」から始められます。同じ店舗や現場で撮るたびに同じアルバムへまとめたいなら、GeoAlbumに場所・範囲と追加先を保存し、見つかった候補を確認してまとめて追加できます。',
  'steps':[
   ('場所と範囲をルールとして保存する','地図、住所・施設名、または写真から場所を指定します。探したい写真の撮影場所に合わせて範囲を設定します。近隣の写真も含まれる場合があるため、次の確認を省略しないでください。','place'),
   ('追加先のアルバムを選ぶ','Apple「写真」のどのアルバムにまとめたいかを決めます。1つの場所ルールで繰り返し整理するところから始められます。','rules'),
   ('見つかった写真を確認して追加する','候補の中から追加したい写真を自分で確認し、アルバムへまとめて追加します。撮影した瞬間に自動で振り分ける機能ではありません。写真の原本を移動・削除・複製することはありません。','album')],
  'example': {
   'title':'同じ店舗で2週続けて撮った商品写真をまとめる',
   'intro':'店舗で新商品の写真を毎週撮り、Apple「写真」の「店舗Aの商品写真」アルバムにまとめる場合を考えます。',
   'visits':[
    ('1週目','店舗の場所と範囲、追加先のアルバムを場所ルールに保存します。ルールで写真を探し、撮影位置が範囲内の商品写真3枚を確認して追加します。'),
    ('2週目','同じ場所ルールで再び写真を探します。前週に追加した3枚は追加対象から外れ、この週に同じ範囲内で撮った商品写真2枚が候補に出ます。その2枚を確認して追加すると、同じアルバムに2週分の5枚がそろいます。')],
   'shot':'review',
   'alt':'GeoAlbumが選択済みの候補写真をアルバムに追加する前に確認を求める画面',
   'caption':'候補を選んだあとの確認画面。画像は既存の掲載例です。',
  },
  'limits':'位置情報がない写真は場所で照合できません。撮影位置と場所ルールの照合は端末内で行います。写真や撮影位置をGeoAlbum独自のサーバーへ送りません。地図表示や場所検索などに必要な通信とは区別してください。',
  'decision':'まず無料の1ルールで候補が用途に合うか確認し、複数の場所ルールやまとめてスキャンする必要があればProを検討してください。整理にかかる時間や精度の改善率は、ここでは実測・保証していません。'
 }
}

GUIDES['studyfocus'] = {
 'slug':'sns-break-focus-timer',
 'title':'休憩中だけSNSを使い、終了後に再ブロックする集中タイマー',
 'description':'勉強集中でSNSなどのアプリを集中中にブロックし、休憩中に使うための設定手順。スクリーンタイムの許可、無料範囲、再ブロックの注意点を紹介します。',
 'preview':('25分勉強して、5分だけSNSを開く例','スクリーンタイムを許可して対象のSNSを選びます。集中の25分間はブロック、休憩の5分間は利用可能。休憩が終わると再びブロックされ、次の集中は自分で開始します。','break','勉強集中で休憩の残り時間を確認する画面'),
 'lead':'勉強集中（Study Focus）は、集中中に選んだSNSアプリをブロックし、休憩中に使えるようにするiPhoneの集中タイマーです。休憩が終わるとSNSを自動で再ブロックします。次の集中タイマーはボタンを押して始めます。',
 'before':'通知を静かにするならiPhoneの「集中モード」、SNSを使える時刻や1日の利用時間を決めるなら「スクリーンタイム」が使えます。勉強と休憩をタイマーで切り替え、選んだSNSを休憩中だけ使いたい場合は、勉強集中の集中・休憩タイマーを使えます。ブロックにはスクリーンタイムへのアクセス許可が必要です。',
 'steps':[
  ('集中時間と休憩時間を決める','自分の予定に合わせて集中と休憩の長さを決め、ブロック対象のアプリを選びます。無料版で選べる個別アプリは3個までです。','settings'),
  ('集中を始める','集中時間中は選んだアプリがブロックされます。勉強の成果や成績を保証する機能ではなく、アプリを開くきっかけを減らすための設定です。','blocked'),
  ('休憩に使い、終了後の状態を確認する','休憩時間は選んだアプリを使えます。休憩が終わると再ブロックしますが、次の集中タイマーは自動で始まりません。ボタンを押して開始してください。','break')],
 'limits':'端末の再起動、時刻変更、スクリーンタイム許可の解除など、iOSや設定の影響で予定どおりにブロックされない場合があります。記録は端末内に保存され、他端末とは同期しません。',
 'decision':'無料版は1日5回までの集中、個別アプリ3個まで、直近7日の記録です。カテゴリ・Webサイトの選択や制限解除が必要なら、自動更新サブスクリプションのProを確認してください。アプリの削除だけではサブスクリプションを解約できません。'
}
GUIDES['taskbit'] = {
 'slug':'tasks-grow-room',
 'title':'タスク完了で部屋を育てるToDoアプリの使い方',
 'description':'TaskBitで今日のタスクを登録し、完了してコインを貯め、相棒の部屋に家具を増やす流れを掲載画面で紹介します。',
 'preview':('「明日の持ち物をそろえる」を終えたら','今日のタスクを1つ登録して、終わったらチェック。貯めたコインを家具や小物に使うと、相棒の部屋に自分が選んだものが増えていきます。','room','TaskBitで家具と相棒のいる部屋を開いた画面'),
 'lead':'TaskBitは、ToDoを完了するたびにコインを貯め、家具や小物に使って相棒の部屋を育てられるiPhoneアプリです。家具は用意された配置先から選び、あとから収納や模様替えもできます。',
 'before':'やることを記録し、時刻を決めて思い出すなら、iPhone標準の「リマインダー」で始められます。小さなタスクの完了を楽しみにしたいなら、TaskBitではチェックするたびにコインが貯まり、相棒の部屋の家具や小物に使えます。まず今日できそうな作業を1つ入れて試せます。',
 'steps':[
  ('今日のタスクを入れる','タスク名と日付を設定します。続けたいことは繰り返し、忘れたくない予定には時刻を設定できます。通知を使うにはiPhone側の許可が必要です。','home'),
  ('終えたらチェックし、部屋を見る','タスクを完了するとコインが貯まります。コインで家具や小物を手に入れ、相棒の部屋に変化を加えられます。毎日開かなくても相棒が弱るようなお世話の義務はありません。','room'),
  ('家具をしまう・移す','手に入れた家具の収納や模様替えができます。画面上の好きな位置へ自由配置する方式ではなく、家具ごとに用意された配置先から選びます。','arrange')],
 'limits':'毎日の継続やタスク達成の効果は未検証です。',
 'decision':'無料で今日のタスクから試せます。繰り返しや完了履歴などの詳しい仕様はアプリ紹介ページで確認してください。'
}

GUIDES_EN = {
    "geoalbum": {
        "title": "Add iPhone Photos From the Same Place to an Existing Album",
        "description": "Use GeoAlbum to find photos from repeated visits and add selected matches to an existing Apple Photos album.",
        "lead": "GeoAlbum finds iPhone photos from repeated visits to a shop, workshop, or other location. Save an area and an existing Apple Photos album as a rule, then review and add the photos you choose. The originals stay in your library.",
        "example": {
            "title": "Organize product photos after two visits to a shop",
            "intro": "Suppose you photograph new products at the same shop each week and keep them in one Apple Photos album.",
            "visits": [
                ("First visit", "Save the shop's location, radius, and destination album. Find the matches and add the three product photos you select."),
                ("Second visit", "Run the same rule. GeoAlbum skips the three photos already in that album. Review the two new matches and add them to collect all five photos in the same album."),
            ],
            "shot": "review",
            "alt": "GeoAlbum asks for confirmation before adding the selected photos to an album",
            "caption": "The confirmation screen is an app screenshot.",
        },
        "before": "Use the map in Apple Photos to find photos from a one-off visit. A saved GeoAlbum rule is useful when you return to the same place and want to reuse the same destination album.",
        "steps": [
            ("Save a location and radius", "Choose a place from a map, search for it, or use a photo with location information. Set a radius that covers the area you photographed.", "place"),
            ("Choose the existing album", "Select the destination from your Apple Photos albums. Run the rule when you want to look for matching photos.", "rules"),
            ("Review matches and add your selection", "Check for photos taken nearby and leave out any you do not want. Tap Add to put the selected matches in the album.", "album"),
        ],
        "limits": "Location matching requires photos with recorded coordinates and runs on the device. The rule runs when you use it. Your originals stay in the Apple Photos library.",
        "decision": "Start with one free location rule. Pro adds multiple rules and lets you scan them together.",
    },
    "kaeroute": {
        "title": "Save an Offline Walking Route Home and Print a PDF Map",
        "description": "Prepare a walking route home in Kaeroute, save its map and turns for offline use, and print an A4 route PDF with Pro.",
        "lead": "Kaeroute is an iPhone app for preparing a walking route home from work or school before a transit disruption. Once saved, the map, route, and turns can be viewed offline. Kaeroute Pro exports a printable A4 PDF with an overview map, section maps, and turns.",
        "preview": ("Pack a printed route as a backup", "Create and save one plan for free. To carry a paper copy, use Pro to export the full route and its key turns as an A4 PDF.", "pdf", "Kaeroute's A4 route PDF preview in Japanese"),
        "before": "Choose a starting point, a destination, and any waypoints while you have internet access. The app interface is available in Japanese and Traditional Chinese. The App Store link on this page goes to the Japan storefront.",
        "steps": [
            ("Plan your main route", "Select the endpoints and add waypoints if needed. Review the distance, estimated walking time, and turns.", "create"),
            ("Save and check offline access", "Download the required map and save the route. Once saving is complete, disconnect from the internet and check that you can view both on your phone.", "offline"),
            ("Export an A4 PDF with Pro", "Save the PDF to Files, share it, or print it with an AirPrint printer. The paper copy can help you prepare in advance.", "pdf"),
        ],
        "limits": "Creating a route or downloading a map requires internet access. Emergencies can change road conditions. Follow instructions from local authorities and your workplace or school before deciding when to leave.",
        "decision": "The free app covers one plan and its saved main route and maps. Pro adds PDF export, multiple plans, and alternative routes.",
    },
    "taskbit": {
        "title": "Earn Furniture by Completing To-Dos on iPhone",
        "description": "Use TaskBit to earn coins for completing tasks and spend them on furniture and decorations for your companion's room.",
        "lead": "TaskBit is a gamified iPhone to-do list. Completing a task earns coins, which you can spend on furniture and decorations for your companion's room. You can rearrange the room as you collect more items.",
        "preview": ("Give today's task a small reward", "Add a task such as packing tomorrow's bag. When you finish, check it off. Use the coins you collect to choose an item for the room.", "room", "A companion in a furnished room in TaskBit"),
        "before": "iPhone Reminders can handle checklists and timed reminders. Use TaskBit when a visible reward for completing tasks would make that daily routine more appealing.",
        "steps": [
            ("Add one task for today", "Enter a short title and date. You can also set a time or repeat schedule.", "home"),
            ("Complete the task to earn coins", "Check off the task when you finish. Save up coins and spend them on furniture or decorations in the app.", "room"),
            ("Choose where the furniture goes", "Place a piece in one of its available spots. You can move or store it later.", "arrange"),
        ],
        "limits": "Furniture has predefined positions. The companion stays fine on days you skip. Notifications require permission in iOS.",
        "decision": "Start for free with a task you already plan to do today.",
    },
    "studyfocus": {
        "title": "Block Social Apps While Studying and Reblock Them After Breaks",
        "description": "Set up the Study Focus iPhone timer to block selected social apps while studying, allow them on breaks, and reblock them when the break ends.",
        "lead": "Study Focus is an iPhone study timer that blocks the social apps you select while you study and unblocks them on breaks. It automatically blocks those apps again when the break ends. Start the next focus timer yourself.",
        "preview": ("Study for 25 minutes and take a five-minute break", "Choose which apps to block and set your study and break lengths. Selected apps are blocked during the study period, available on the break, and blocked again when it ends.", "break", "The Study Focus app showing the time left in a break"),
        "before": "Allow Study Focus to use Screen Time before picking apps to block. iOS Focus can silence notifications when that is all you need.",
        "steps": [
            ("Set your timers and select apps", "Choose your focus and break lengths, then select the social apps you want to restrict. The free plan lets you choose up to three individual apps.", "settings"),
            ("Start a study session", "The selected apps are blocked while the focus timer runs.", "blocked"),
            ("Take a break and check the block", "Use the selected apps during the break. At the end of the break, they are blocked again. Tap to start the next focus session.", "break"),
        ],
        "limits": "Reboots, time changes, or loss of Screen Time permission can interfere with blocking. Check the behavior on your device before relying on it.",
        "decision": "The free plan includes up to five focus sessions per day, three individual apps, and seven days of history. Pro is a subscription and adds controls for categories and websites.",
    },
}
