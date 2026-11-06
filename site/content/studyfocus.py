"""StudyFocus (勉強集中 / Study Focus) — facts: docs/website/app-information.md (App Store 1.0, checked 2026-11-06)."""

TERMS = "https://bottlenose-network-d4d.notion.site/StudyFocus-3ba661a42a4a80c8a72dce3a4a054361"
MAIL = "shunmemo.support@gmail.com"


def rhythm(focus: str, brk: str, blocked: str, free: str, label: str) -> str:
    return f"""<ol class="rhythm" aria-label="{label}">
<li class="r-focus"><span class="r-name">{focus}</span><span class="r-state">{blocked}</span></li>
<li class="r-break"><span class="r-name">{brk}</span><span class="r-state">{free}</span></li>
<li class="r-focus r-next"><span class="r-name">{focus}</span><span class="r-state">{blocked}</span></li>
</ol>"""


APP = {
    "slug": "studyfocus",
    "theme": "studyfocus",
    "theme_color": "#F7F8F6",
    "store_id": "6800586592",
    "version": "1.0",
    "min_ios": "17.0",
    "checked": "2026-11-06",
    "langs": ("en", "ja"),
    "primary_lang": "en",
    "ui_languages": ["en", "ja"],
    "schema_category": "EducationalApplication",
    "store_url": {
        "ja": "https://apps.apple.com/jp/app/id6800586592",
        "en": "https://apps.apple.com/us/app/id6800586592",
    },
    "offers": {
        "ja": [("勉強集中", "0", "JPY", "無料版: 1日5回までの集中、個別アプリ3個まで、直近7日の記録"),
               ("勉強集中 Pro", "300", "JPY", "月額の自動更新サブスクリプション")],
        "en": [("Study Focus", "0", "USD", "Free: up to 5 focus sessions a day, up to 3 apps, last 7 days of history"),
               ("Study Focus Pro", "2.99", "USD", "Monthly auto-renewing subscription")],
    },
    "t": {},
}

APP["t"]["ja"] = {
    "name": "勉強集中",
    "store_name": "勉強集中 - SNS ブロッカー",
    "title": "勉強集中（Study Focus）：休憩中だけSNSが使える集中タイマー｜iPhoneアプリ",
    "description": "勉強集中は、集中時間は選んだSNSなどのアプリを自動でブロックし、休憩時間だけ使えるようにするiPhoneの集中タイマーです。休憩が終わると自動で再ブロック。無料で使え、Proは月額300円。",
    "og_alt": "勉強集中のアイコンと、集中中と休憩中のタイマー画面",
    "hub_line_ja": "集中中はSNSをブロックし、休憩中だけ使えるようにする勉強用タイマー。",
    "hub_line_en": "A study timer that blocks social apps while you focus and lets you use them on breaks.",
    "hub_note_en": "Called 勉強集中 in Japan and Study Focus in English.",
    "headline": "休憩はSNSで。<br>終われば、勉強へ。",
    "lead": "勉強集中（Study Focus）は、集中時間のあいだ選んだSNSなどのアプリを自動でブロックし、休憩時間になると使えるようにするiPhoneの集中タイマーです。休憩が終わると対象のアプリは自動で再びブロックされるので、「少しだけのつもり」が長引きません。",
    "price_note": "無料（制限あり）。Proは月額300円の自動更新サブスクリプション。iOS 17.0以降。",
    "hero_art": rhythm("集中", "休憩", "ブロック中", "使える", "集中と休憩のくり返し"),
    "hero_shot": "focus",
    "hero_alt": "集中中のタイマー画面。円形のリングの中に残り時間24分38秒、下に「あと25分で休憩」",
    "summary": "勉強集中は、SNSを我慢させるアプリではなく、集中と休憩のメリハリをつくるアプリです。ポモドーロタイマーは時間を計るだけで、休憩の終わりにSNSから戻れるかは本人次第です。勉強集中はAppleのスクリーンタイムの仕組みを使い、休憩が終わった時点で選んだアプリを自動で再びブロックします。",
    "facts": [
        ("正式名", "勉強集中 - SNS ブロッカー（英語名: Study Focus - Social Blocker）"),
        ("できること", "集中・休憩タイマー、集中中に選んだアプリを自動ブロック、休憩中は自動で解除、集中時間とセッション数の記録"),
        ("料金", "無料（1日5回までの集中、ブロック対象は個別アプリ3個まで、直近7日の記録）。勉強集中 Pro は月額300円の自動更新サブスクリプション（日本のApp Store）"),
        ("対応環境", "iPhone（iOS 17.0以降）。アプリのブロックにはスクリーンタイムへのアクセス許可が必要"),
        ("言語", "日本語、英語"),
        ("データの保存先", "タイマー設定、ブロック対象、記録は端末内。サーバーへの同期と外部の分析サービスは使いません"),
        ("カテゴリ", "教育、仕事効率化"),
        ("バージョン", "1.0（2026年8月15日公開）"),
        ("開発・提供", "Ryo Morishita"),
    ],
    "features_h": "勉強集中でできること",
    "features": [
        {
            "id": "timer", "h": "自分のリズムで、集中と休憩のタイマー", "shot": "settings",
            "alt": "設定画面。集中時間25分、休憩時間5分をプラスとマイナスで変更でき、スクリーンタイムの対象アプリとStudyFocus Proの項目がある",
            "body": "<p>集中時間と休憩時間をそれぞれ設定して、自分に合ったリズムで勉強できます。タイマーは一時停止や、その時間のスキップもできます。設定の変更は次の時間から反映されます。</p>",
        },
        {
            "id": "block", "h": "集中中は、選んだアプリを自動でブロック", "shot": "blocked",
            "alt": "集中中にSNSアプリを開いたときの画面。「集中時間です」「あと24分で休憩」と表示され、閉じるボタンがある",
            "body": "<p>SNSなど、集中を妨げるアプリを自分で選びます。集中時間が始まると、選んだアプリは自動で使えなくなり、開くと「集中時間です」と休憩までの残り時間が表示されます。</p>"
                    "<p>選択にはAppleのスクリーンタイムの仕組みを使います。無料版では個別のアプリを3個まで、Proではアプリ・カテゴリ・Webサイトを制限なく選べます。</p>",
        },
        {
            "id": "break", "h": "休憩になったら、自動で使える", "shot": "break",
            "alt": "休憩中のタイマー画面。緑のリングの中に残り4分21秒、下に「自由に休憩できます」",
            "body": "<p>休憩が始まると、ブロックは自動で解除されます。設定を切り替える必要はありません。休憩の終わりはローカル通知で知らせ、ロック画面のLive Activityで残り時間を確認できます。</p>",
        },
        {
            "id": "back", "h": "休憩が終わったら、自動で再ブロック", "shot": "ready",
            "alt": "休憩が終わった後の画面。「次の集中を始められます」と「次の集中を始める」ボタン",
            "body": "<p>休憩が終わると、選んだアプリは自動で再びブロックされます。アプリを閉じていても、画面をロックしていても同じです。次の集中は「次の集中を始める」をタップして始めます。</p>",
        },
        {
            "id": "stats", "h": "今日どれだけ集中したかを記録", "shot": "stats",
            "alt": "記録画面。今日の集中時間2時間35分、完了セッション5回、直近7日間の棒グラフと日ごとの記録",
            "body": "<p>今日の集中時間と完了したセッション数、直近7日間の推移を確認できます。Proでは、端末に保存されている過去の記録をすべて表示できます。</p>",
        },
    ],
    "steps": {
        "h": "勉強集中の使い方",
        "items": [
            ("スクリーンタイムを許可して、アプリを選ぶ", "最初の設定で、スクリーンタイムへのアクセスを許可し、集中中にブロックしたいアプリを選びます。"),
            ("集中時間と休憩時間を決める", "例えば集中25分・休憩5分のように、自分に合った長さにします。"),
            ("集中を始める", "集中中は選んだアプリがブロックされ、休憩になると使えます。休憩が終わると自動で再びブロックされます。"),
        ],
    },
    "gallery_h": "アプリの画面",
    "gallery": [
        ("focus", "集中中のタイマー"),
        ("blocked", "集中中にブロックしたアプリを開いたとき"),
        ("break", "休憩中のタイマー"),
        ("ready", "休憩の後、次の集中を待つ画面"),
        ("stats", "集中時間の記録"),
        ("settings", "タイマーとブロック対象の設定"),
    ],
    "fit": [
        "休憩中にSNSを見始めると、勉強に戻れなくなる人",
        "受験勉強、資格試験、大学の課題などで長時間勉強する人",
        "アプリを一日中ブロックするのではなく、休憩にはSNSを使いたい人",
        "ポモドーロのような集中と休憩のリズムで勉強したい人",
    ],
    "limits": [
        "アプリのブロックには、Appleのスクリーンタイムへのアクセス許可が必要です",
        "休憩の後、次の集中は自動では始まりません。ボタンを押して始めます",
        "無料版は1日5回までの集中、個別アプリ3個まで、直近7日の記録です。カテゴリやWebサイトの選択はProの機能です",
        "iOSの仕様、端末の再起動、時刻の変更、スクリーンタイムの許可の解除などにより、ブロックが予定どおりに動かない場合があります",
        "記録は端末内だけに保存され、ほかの端末とは同期しません",
    ],
    "faq": [
        ("what", "勉強集中はどんなアプリですか？",
         "<p>集中時間は選んだSNSなどのアプリをブロックし、休憩時間だけ使えるようにするiPhoneの集中タイマーです。休憩が終わると自動で再びブロックするので、休憩から勉強へ戻りやすくなります。</p>"),
        ("price", "無料で使えますか？",
         "<p>はい。無料版では1日5回まで集中を完了でき、ブロック対象として個別のアプリを3個まで選べ、直近7日の記録を見られます。勉強集中 Pro（日本のApp Storeで月額300円の自動更新サブスクリプション）では、回数・ブロック対象・記録の期間の制限がなくなります。</p>"),
        ("cancel", "Proの解約はどうすればいいですか？",
         "<p>iPhoneの「設定」で自分の名前を選び、「サブスクリプション」から勉強集中を選んで解約します。アプリを削除しただけでは解約されません。</p>"),
        ("permission", "スクリーンタイムの許可は必要ですか？",
         "<p>アプリをブロックするために必要です。勉強集中はAppleのFamilyControlsなどの仕組みを使い、選んだアプリをAppleが用意した識別情報として扱います。選んだアプリの中で何を見たか、何を投稿したかは取得しません。</p>"),
        ("vs", "普通のポモドーロタイマーやアプリブロッカーと何が違いますか？",
         "<p>ポモドーロタイマーは時間を計るだけなので、休憩の終わりにSNSを閉じるかは本人次第です。勉強集中はブロックをタイマーと連動させ、集中中だけブロックし、休憩中は使えるようにし、休憩が終わったら自動で再びブロックします。手動で切り替える必要はありません。</p>"),
        ("offline", "インターネット接続は必要ですか？",
         "<p>タイマー、ブロック、記録は端末内で動きます。Proの購入と購入状態の確認にはApp Storeとの通信が必要です。</p>"),
        ("data", "データはどこに保存されますか？",
         "<p>タイマーの設定、ブロック対象、集中の記録は端末内に保存されます。運営者のサーバーへの同期やiCloud同期はなく、外部の分析サービスにもデータを送りません。詳しくは<a href=\"/studyfocus/ja/privacy/\">プライバシー</a>をご覧ください。</p>"),
    ],
    "closing_h": "休憩は、ちゃんと休む",
    "closing": "集中するときは集中して、休憩はSNSで気分転換。終わったら、また勉強へ。",
    "privacy": {
        "title": "プライバシー｜勉強集中（Study Focus）",
        "description": "勉強集中が扱うスクリーンタイムの選択情報、タイマー、記録の概要。データは端末内に保存されます。",
        "h1": "勉強集中のプライバシー",
        "body": f"""<p>勉強集中（StudyFocus）が扱う情報の概要です。App Storeに登録している利用規約とプライバシーポリシーの全文は<a href="{TERMS}">こちら</a>です。</p>
<h2>スクリーンタイムの選択情報</h2>
<p>ブロック対象として選んだアプリ、カテゴリ、Webドメインを、AppleのFamilyControlsが提供する識別情報（トークン）として扱います。選んだアプリの中での閲覧内容、投稿、メッセージ、操作の内容は取得しません。</p>
<h2>端末内に保存する情報</h2>
<p>集中時間と休憩時間の設定、タイマーの状態と終了予定時刻、ブロック対象、日ごとの集中時間と完了セッション数を端末内に保存します。運営者のサーバーへの同期、バックアップ、iCloud同期は行いません。</p>
<h2>収集しない情報</h2>
<p>氏名、住所、電話番号、連絡先、写真、正確な位置情報、広告ID、閲覧履歴を収集しません。外部の分析SDKや広告は使いません。</p>
<h2>購入</h2>
<p>勉強集中 Pro の購入と購入状態の確認には、AppleのStoreKitとApp Storeを使います。カード番号などの決済情報はAppleが管理し、アプリと運営者は取得しません。</p>
<h2>お問い合わせ</h2>
<p><a href="mailto:{MAIL}">{MAIL}</a></p>""",
    },
    "support": {
        "title": "サポート｜勉強集中（Study Focus）",
        "description": "勉強集中でアプリがブロックされない、Proを解約したいときの確認方法と、お問い合わせ先。",
        "h1": "勉強集中のサポート",
        "body": f"""<h2>集中中にアプリがブロックされない</h2>
<p>iPhoneの「設定」で、勉強集中のスクリーンタイムへのアクセスが許可されているか確認してください。設定画面の「対象アプリを変更」で、ブロックしたいアプリが選ばれているかも確認してください。端末の再起動や時刻の変更の後は、アプリを一度開いてください。</p>
<h2>休憩の後、次の集中が始まらない</h2>
<p>休憩が終わると選んだアプリは自動で再びブロックされますが、次の集中は自動では始まりません。「次の集中を始める」をタップしてください。</p>
<h2>Proの購入の復元と解約</h2>
<p>設定画面の「購入を復元」で、以前購入したProを復元できます。解約は、iPhoneの「設定」で自分の名前を選び、「サブスクリプション」から行います。アプリを削除しただけでは解約されません。返金はAppleの手続きで申請してください。</p>
<h2>お問い合わせ</h2>
<p>解決しない場合は、<a href="mailto:{MAIL}">{MAIL}</a> までご連絡ください。アプリとiOSのバージョン、iPhoneの機種、起きたことと直前の操作を書いていただくと確認が早くなります。</p>""",
    },
}

APP["t"]["en"] = {
    "name": "Study Focus",
    "store_name": "Study Focus - Social Blocker",
    "title": "Study Focus: A Study Timer That Unblocks Social Apps Only on Breaks",
    "description": "Study Focus is an iPhone study timer that blocks the social apps you choose while you focus, unblocks them on breaks and blocks them again when the break ends.",
    "og_alt": "The Study Focus icon and the focus and break timer screens",
    "hub_line_ja": "集中中はSNSをブロックし、休憩中だけ使えるようにする勉強用タイマー。",
    "hub_line_en": "A study timer that blocks social apps while you focus and lets you use them on breaks.",
    "hub_note_ja": "日本のApp Storeでは「勉強集中」という名前です。",
    "headline": "Take your social media break. Then get back to studying.",
    "lead": "Study Focus is an iPhone focus timer that automatically blocks the apps you choose, such as social media, during focus sessions and makes them available when your break starts. When the break ends, those apps are blocked again automatically, so a quick look doesn't turn into half an hour.",
    "price_note": "Free with limits. Pro is a $2.99/month auto-renewing subscription in the US. Requires iOS 17.0 or later.",
    "hero_art": rhythm("Focus", "Break", "Blocked", "Available", "Alternating focus and break periods"),
    "hero_shot": "focus",
    "hero_alt": "Focus timer screen: a ring with 24:38 remaining and Break in 25 min below",
    "summary": "Study Focus isn't about giving up social media; it creates a clear rhythm between focus and rest. A Pomodoro timer only keeps time, so getting back from a break is up to your willpower. Study Focus uses Apple's Screen Time framework to block your chosen apps again the moment a break ends.",
    "facts": [
        ("Full name", "Study Focus - Social Blocker (<span lang=\"ja\">勉強集中</span> in Japan)"),
        ("What it does", "Focus and break timer, automatic blocking of chosen apps during focus, automatic unblocking on breaks, focus time and session history"),
        ("Price", "Free with up to 5 focus sessions a day, up to 3 individual apps and the last 7 days of history. Study Focus Pro is an auto-renewing monthly subscription ($2.99/month on the US App Store)"),
        ("Requirements", "iPhone with iOS 17.0 or later. App blocking requires Screen Time permission"),
        ("Languages", "English, Japanese"),
        ("Where data is stored", "Timer settings, blocked apps and history stay on your device. No server sync and no third-party analytics"),
        ("Category", "Education, Productivity"),
        ("Version", "1.0 (released August 14, 2026, US time)"),
        ("Developer", "Ryo Morishita"),
    ],
    "features_h": "What you can do with Study Focus",
    "features": [
        {
            "id": "timer", "h": "A focus and break timer on your terms", "shot": "settings",
            "alt": "Settings screen with Focus Duration 25 min and Break Duration 5 min steppers, Screen Time app selection and Study Focus Pro",
            "body": "<p>Set your own focus and break lengths. You can pause the timer or skip the current period, and changes to the durations apply from the next period.</p>",
        },
        {
            "id": "block", "h": "Distracting apps are blocked while you focus", "shot": "blocked",
            "alt": "Screen shown when opening a blocked social app during focus: It's time to focus, Break in 24 minutes, and a Close button",
            "body": "<p>Choose the social media and other apps that distract you. When a focus session starts, they're restricted automatically; open one and you'll see that it's time to focus and how long until your break.</p>"
                    "<p>Apps are chosen through Apple's Screen Time framework. The free version allows up to 3 individual apps; Pro allows unlimited apps, categories and websites.</p>",
        },
        {
            "id": "break", "h": "Apps become available on your break", "shot": "break",
            "alt": "Break timer screen: a green ring with 04:21 remaining and Enjoy your break freely",
            "body": "<p>When the break starts, blocking is lifted automatically, with no settings to switch. A local notification tells you when the period ends, and a Live Activity shows the time left on your Lock Screen.</p>",
        },
        {
            "id": "back", "h": "Blocked again when the break ends", "shot": "ready",
            "alt": "Screen after a break ends: Ready for your next Focus and a Start Next Focus button",
            "body": "<p>When your break ends, your chosen apps are blocked again automatically, even if Study Focus is closed or your phone is locked. Start the next focus session by tapping Start Next Focus.</p>",
        },
        {
            "id": "stats", "h": "See how much you focused today", "shot": "stats",
            "alt": "History screen: 2 hr 35 min focused today, 5 completed sessions, a bar chart of the last 7 days and daily history",
            "body": "<p>See today's focus time, completed sessions and the last 7 days. With Pro, you can view all the history stored on your device.</p>",
        },
    ],
    "steps": {
        "h": "How Study Focus works",
        "items": [
            ("Allow Screen Time and choose apps", "During setup, allow Screen Time access and choose the apps to block while you focus."),
            ("Set focus and break lengths", "For example, 25 minutes of focus and a 5-minute break, or whatever suits you."),
            ("Start focusing", "Chosen apps are blocked during focus and available on breaks, then blocked again automatically when the break ends."),
        ],
    },
    "gallery_h": "Screens from the app",
    "gallery": [
        ("focus", "Focus timer"),
        ("blocked", "Opening a blocked app during focus"),
        ("break", "Break timer"),
        ("ready", "Waiting for the next focus session"),
        ("stats", "Focus history"),
        ("settings", "Timer and blocked app settings"),
    ],
    "fit": [
        "Students who open social media on a break and can't get back to studying",
        "Anyone studying for long hours for entrance exams, certifications or coursework",
        "People who want social media on breaks rather than blocked all day",
        "Anyone who likes a Pomodoro-style rhythm of focus and rest",
    ],
    "limits": [
        "App blocking requires Screen Time permission from Apple's framework",
        "After a break, the next focus session doesn't start on its own; tap the button to begin",
        "The free version allows 5 focus sessions a day, 3 individual apps and the last 7 days of history; choosing categories or websites requires Pro",
        "iOS limitations, restarting the device, changing the time or revoking Screen Time permission can stop blocking from working as scheduled",
        "History is stored only on your device and isn't synced to other devices",
    ],
    "faq": [
        ("what", "What is Study Focus?",
         "<p>Study Focus is an iPhone focus timer that blocks the apps you choose, such as social media, during focus sessions and lets you use them during breaks. When a break ends, the apps are blocked again automatically, which makes it easier to get back to studying.</p>"),
        ("price", "Is Study Focus free?",
         "<p>Yes. The free version lets you complete up to 5 focus sessions a day, block up to 3 individual apps and view the last 7 days of history. Study Focus Pro, an auto-renewing monthly subscription ($2.99/month on the US App Store; prices vary by region), removes those limits.</p>"),
        ("cancel", "How do I cancel Pro?",
         "<p>Open Settings on your iPhone, tap your name, then Subscriptions, and choose Study Focus. Deleting the app doesn't cancel the subscription.</p>"),
        ("permission", "Why does it need Screen Time permission?",
         "<p>It's required to block apps. Study Focus uses Apple's FamilyControls framework, which represents the apps you choose as opaque tokens. It doesn't see what you view or post inside those apps.</p>"),
        ("vs", "How is it different from a Pomodoro timer or an app blocker?",
         "<p>A Pomodoro timer only keeps time, so closing social media after a break is up to you. Study Focus ties blocking to the timer: apps are blocked only during focus, available on breaks, and blocked again automatically when each break ends, so you don't have to switch anything by hand.</p>"),
        ("offline", "Does Study Focus need an internet connection?",
         "<p>The timer, blocking and history work on your device. Buying Pro and checking your subscription status need a connection to the App Store.</p>"),
        ("data", "Where is my data stored?",
         "<p>Timer settings, blocked apps and focus history are stored on your device. There's no server or iCloud sync, and no data is sent to third-party analytics. See <a href=\"/studyfocus/en/privacy/\">Privacy</a> for details.</p>"),
    ],
    "closing_h": "Rest properly on your breaks",
    "closing": "Focus when it's time to focus, scroll on your break, then get back to work.",
    "privacy": {
        "title": "Privacy | Study Focus",
        "description": "How Study Focus handles Screen Time selections, timer settings and history. Data stays on your device.",
        "h1": "Study Focus privacy",
        "body": f"""<p>A summary of the information Study Focus (StudyFocus) handles. The full terms of use and privacy policy registered on the App Store are available <a href="{TERMS}">here</a> (in Japanese).</p>
<h2>Screen Time selections</h2>
<p>The apps, categories and web domains you choose to block are handled as tokens provided by Apple's FamilyControls framework. Study Focus doesn't access what you view, post, message or do inside those apps.</p>
<h2>Stored on your device</h2>
<p>Focus and break durations, timer state and end times, your blocked selection, and daily focus time and completed sessions are stored on your device. There's no sync or backup to the developer's servers and no iCloud sync.</p>
<h2>Not collected</h2>
<p>Names, addresses, phone numbers, contacts, photos, precise location, advertising identifiers and browsing history are not collected. No third-party analytics SDKs or ads are used.</p>
<h2>Purchases</h2>
<p>Buying Study Focus Pro and checking its status use Apple's StoreKit and the App Store. Payment details such as card numbers are handled by Apple and never received by the app or the developer.</p>
<h2>Contact</h2>
<p><a href="mailto:{MAIL}">{MAIL}</a></p>""",
    },
    "support": {
        "title": "Support | Study Focus",
        "description": "What to check when apps aren't blocked, how to restore or cancel Pro, and how to contact the developer.",
        "h1": "Study Focus support",
        "body": f"""<h2>Apps aren't blocked during focus</h2>
<p>Check that Screen Time access is allowed for Study Focus in your iPhone's Settings, and that the apps you want to block are selected under Change Selected Apps in the app's settings. After restarting your phone or changing the time, open the app once.</p>
<h2>The next focus session doesn't start after a break</h2>
<p>When a break ends, your chosen apps are blocked again automatically, but the next focus session doesn't start on its own. Tap Start Next Focus.</p>
<h2>Restoring or canceling Pro</h2>
<p>Use Restore Purchases in the app's settings to restore Pro. To cancel, open Settings on your iPhone, tap your name, then Subscriptions. Deleting the app doesn't cancel the subscription. Refunds are requested through Apple.</p>
<h2>Contact</h2>
<p>If you still need help, email <a href="mailto:{MAIL}">{MAIL}</a> with your app and iOS versions, iPhone model, what happened and what you did just before.</p>""",
    },
}
