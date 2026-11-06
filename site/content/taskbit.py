"""TaskBit — facts: docs/website/app-information.md (App Store 1.4.0, checked 2026-11-06)."""

POLICY = "https://bottlenose-network-d4d.notion.site/TaskBit-391661a42a4a80b4ad01d490f9bede3f"
MAIL = "shunmemo.support@gmail.com"

APP = {
    "slug": "taskbit",
    "theme": "taskbit",
    "theme_color": "#FBF7EE",
    "store_id": "6786552954",
    "version": "1.4.0",
    "min_ios": "17.0",
    "checked": "2026-11-06",
    "langs": ("en", "ja"),
    "primary_lang": "en",
    "ui_languages": ["en", "ja"],
    "schema_category": "LifestyleApplication",
    "store_url": {
        "ja": "https://apps.apple.com/jp/app/id6786552954",
        "en": "https://apps.apple.com/us/app/id6786552954",
    },
    "offers": {
        "ja": [("TaskBit", "0", "JPY", None)],
        "en": [("TaskBit", "0", "USD", None)],
    },
    "t": {},
}

APP["t"]["ja"] = {
    "name": "TaskBit",
    "store_name": "TaskBit：育つToDo・タスク管理",
    "title": "TaskBit：タスクを終えると部屋が育つiPhoneのToDoアプリ",
    "description": "TaskBitは、タスクを完了するとコインが貯まり、小さな相棒が暮らす部屋に家具が増えていくiPhone向けToDoアプリです。繰り返し、リマインダー、カレンダーの完了履歴に対応。無料。",
    "og_alt": "TaskBitのアイコンと、部屋と今日のタスクが並ぶホーム画面",
    "hub_line_ja": "タスクを終えると、小さな相棒の部屋に家具が増えていくToDoアプリ。",
    "hub_line_en": "A to-do app where finished tasks add furniture to a little companion's room.",
    "headline": "今日のひとつで、<br>部屋が少し育つ。",
    "lead": "TaskBitは、やることをひとつ終えるたびにコインが貯まり、小さな相棒「TaskBit」の部屋に家具が増えていくiPhoneのToDoアプリです。連続記録や、できなかった日を責める表示はありません。",
    "price_note": "無料。iOS 17.0以降。",
    "hero_shot": "home",
    "hero_alt": "TaskBitのホーム画面。上に家具が置かれた部屋、下に今日のタスクの一覧と完了済みのタスク",
    "summary": "TaskBitは、タスク管理の基本機能（作成・繰り返し・リマインダー・カレンダー）に、完了で部屋が育つ仕組みを組み合わせたToDoアプリです。小さな達成を目に見える変化にして、勉強・読書・運動・家事などを自分のペースで続けたい人に向いています。",
    "facts": [
        ("正式名", "TaskBit：育つToDo・タスク管理"),
        ("できること", "タスク管理、毎日・毎週・毎月の繰り返し、時刻つきリマインダー、カレンダー、家具を集めて部屋を模様替え"),
        ("料金", "無料（App内課金なし）"),
        ("対応環境", "iPhone（iOS 17.0以降）。App Storeの互換性表示では、Apple M1以降のMac（macOS 14.0以降）とApple Vision Pro（visionOS 1.0以降）にも対応"),
        ("言語", "日本語、英語"),
        ("データの保存先", "タスク、完了履歴、コイン、家具は端末内。アカウント登録とクラウド同期はありません"),
        ("カテゴリ", "仕事効率化、ライフスタイル"),
        ("バージョン", "1.4.0（2026年11月1日公開）"),
        ("開発・提供", "Ryo Morishita"),
    ],
    "features_h": "TaskBitでできること",
    "features": [
        {
            "id": "tasks", "h": "タスクを作って、終えたらチェック",
            "alt": "タスク作成画面。タスク名、カテゴリ、日付、時刻の指定、繰り返しの項目が並ぶ",
            "body": "<p>タスク名と日付を入れて保存し、終わったらチェックするだけの、シンプルなToDoリストです。カテゴリと時刻も設定できます。</p>"
                    "<p>ホーム画面には部屋と今日のタスクが並び、完了したタスクは「完了済み」にまとまります。</p>",
        },
        {
            "id": "repeat", "h": "毎日・毎週・毎月の繰り返し",
            "body": "<p>読書や勉強、運動、家事など、決まって行うことは繰り返しを設定できます。毎日、指定した曜日、毎月の指定日や月末を選べます。31日のように存在しない日付を指定した場合、その日がない月には発生しません。</p>",
        },
        {
            "id": "reminders", "h": "時刻を指定したタスクのリマインダー",
            "body": "<p>タスクに時刻を設定すると、その時刻に通知でお知らせします。通知を使うにはiPhoneでTaskBitの通知を許可してください。通知はiPhoneの「設定」からいつでも変更できます。</p>",
        },
        {
            "id": "calendar", "h": "予定と完了履歴をカレンダーで", "shot": "schedule",
            "alt": "カレンダー画面。月のカレンダーの下に、選んだ日の予定のタスクが並ぶ",
            "body": "<p>これからの予定と、これまでに完了したタスクをカレンダーで見返せます。完了履歴からは、タイトルとカテゴリを引き継いで同じタスクをもう一度登録できます（バージョン1.4.0から）。内容を確認してから保存するまで、新しいタスクは登録されません。</p>",
        },
        {
            "id": "room", "h": "コインを貯めて、部屋に家具を増やす", "shot": "room",
            "alt": "家具が増えたTaskBitの部屋。窓、棚、時計、植物が置かれ、コインの残高が表示されている",
            "body": "<p>タスクを完了するとコインが貯まります。コインを使って家具や小物を手に入れると、相棒の部屋が少しずつ変わっていきます。毎日の行動が、目に見える積み重ねとして残ります。</p>"
                    "<p>相棒に空腹や体力のようなお世話の義務はなく、毎日開かなくても困ることはありません。</p>",
        },
        {
            "id": "arrange", "h": "家具の収納と模様替え", "shot": "arrange",
            "alt": "模様替え画面。持っている家具の一覧と、それぞれの「しまう」「移動」ボタン",
            "body": "<p>手に入れた家具は、しまったり、配置できる別の場所へ移したりできます。画面上の好きな位置に自由に置く方式ではなく、家具ごとに用意された場所から選びます。</p>",
        },
    ],
    "steps": {
        "h": "TaskBitの使い方",
        "items": [
            ("今日できそうなことを入れる", "タスク名と日付を入れます。続けたいことには繰り返し、忘れたくないことには時刻を設定します。"),
            ("終えたらチェックする", "タスクを完了するとコインが貯まります。できなかった日があっても、責める表示はありません。"),
            ("部屋を育てる", "貯めたコインで家具を増やし、しまったり移したりして、自分らしい部屋にしていきます。"),
        ],
    },
    "gallery_h": "アプリの画面",
    "gallery": [
        ("home", "ホーム画面。部屋と今日のタスク"),
        ("create", "タスク作成画面"),
        ("schedule", "カレンダー画面"),
        ("arrange", "模様替え画面"),
        ("room", "家具が増えた部屋"),
    ],
    "fit": [
        "ToDoリストを作っても、なかなか続かない人",
        "勉強、読書、運動、家事などの習慣を、プレッシャーなく続けたい人",
        "連続記録が途切れると、やる気がなくなってしまう人",
        "かわいい見た目で、繰り返しや通知もしっかり使いたい人",
    ],
    "limits": [
        "アカウントとクラウド同期はありません。データは使っている端末の中だけにあり、ほかの端末とは共有されません",
        "チームでのタスク共有や、ほかの人への割り当てはできません",
        "家具は、家具ごとに決まった配置場所から選んで置きます",
        "リマインダーを使うには、iPhoneでTaskBitの通知を許可する必要があります",
    ],
    "faq": [
        ("what", "TaskBitはどんなアプリですか？",
         "<p>iPhone向けのToDo・タスク管理アプリです。タスクを完了するとコインが貯まり、そのコインで小さな相棒が暮らす部屋に家具を増やしていけます。ペットのお世話をするアプリではなく、日々の小さな達成を楽しむためのアプリです。</p>"),
        ("price", "無料で使えますか？",
         "<p>はい。TaskBitは無料で、App内課金はありません（バージョン1.4.0時点）。最新の情報は<a href=\"https://apps.apple.com/jp/app/id6786552954\">App Storeのページ</a>でご確認ください。</p>"),
        ("habit", "勉強や読書などの習慣づくりに使えますか？",
         "<p>使えます。毎日、指定した曜日、毎月の指定日や月末に繰り返すタスクを設定できます。連続記録やペナルティで継続を強制する仕組みはないので、休んだ日があっても次の日から同じように続けられます。</p>"),
        ("streak", "連続記録が途切れたり、相棒が弱ったりしますか？",
         "<p>いいえ。連続記録の表示や、できなかった日を責める表示はありません。相棒に空腹などのお世話の義務もありません。</p>"),
        ("reminder", "リマインダー（通知）はありますか？",
         "<p>あります。タスクに時刻を設定すると、その時刻に通知でお知らせします。iPhoneでTaskBitの通知を許可してください。</p>"),
        ("history", "終わったタスクは見返せますか？",
         "<p>はい。カレンダーで予定と完了履歴を見返せます。完了履歴から同じタスクをもう一度登録することもできます。</p>"),
        ("offline", "インターネット接続は必要ですか？",
         "<p>タスクの作成・完了・カレンダー・部屋の模様替えは端末内のデータで動きます。オンラインのアカウントやクラウド同期はありません。</p>"),
        ("data", "データはどこに保存されますか？",
         "<p>タスク、完了履歴、コイン、家具は端末内に保存されます。アプリの改善のため、Google Analytics for Firebaseで機能の利用状況（画面の表示や機能の利用結果など）を送信しますが、タスク名や通知の本文は送信しません。分析はアプリ内の「プライバシー」画面で無効にできます。詳しくは<a href=\"/taskbit/ja/privacy/\">プライバシー</a>をご覧ください。</p>"),
        ("devices", "iPadや機種変更後の端末にデータを移せますか？",
         "<p>TaskBitにはアプリ独自のクラウド同期がないため、端末間でデータを自動で同期することはできません。</p>"),
    ],
    "closing_h": "まずは、今日できることをひとつ",
    "closing": "読書を10分、机を片づける、散歩に行く。小さなタスクを終えるたびに、部屋が少しずつ変わっていきます。",
    "privacy": {
        "title": "プライバシー｜TaskBit",
        "description": "TaskBitが保存・送信する情報の概要。タスクは端末内に保存され、利用状況の分析はアプリ内で無効にできます。",
        "h1": "TaskBitのプライバシー",
        "body": f"""<p>TaskBitが扱う情報の概要です。App Storeに登録している正式なポリシーは<a href="{POLICY}">こちら</a>です。</p>
<h2>端末内に保存する情報</h2>
<p>タスク（名前、カテゴリ、日付、時刻、繰り返しの設定）、完了履歴、コイン、家具とその配置を端末内に保存します。アカウント登録はなく、アプリ独自のクラウド同期はありません。アプリを削除すると、端末内のデータも削除されます。</p>
<h2>通知</h2>
<p>時刻を設定したタスクのリマインダーには、iOSのローカル通知を使います。通知の内容を外部へ送信することはありません。</p>
<h2>利用状況の分析</h2>
<p>TaskBitは、初回体験、タスクの作成・完了、報酬、リマインダーの改善のため、Google LLCが提供するGoogle Analytics for Firebaseを使用します。送信される可能性がある情報は、アプリのバージョン、端末・OS・言語などFirebase Analyticsが自動で収集する情報と、画面の表示や機能の利用結果、リマインダーの有無、繰り返しの種類など、あらかじめ決めた利用イベントです。</p>
<p>タスク名、通知の本文、タスクの具体的な日付・時刻、メールアドレス、氏名、電話番号、広告ID（IDFA）は送信しません。分析データを広告に使うことはありません。</p>
<p>分析は初期状態で有効です。アプリ内の「プライバシー」画面でいつでも無効にでき、無効にした後は新しい分析イベントを送信しません。</p>
<h2>お問い合わせ</h2>
<p><a href="mailto:{MAIL}">{MAIL}</a></p>""",
    },
    "support": {
        "title": "サポート｜TaskBit",
        "description": "TaskBitの使い方、よくある問題、お問い合わせ先。",
        "h1": "TaskBitのサポート",
        "body": f"""<h2>通知が届かない</h2>
<p>iPhoneの「設定」でTaskBitの通知が許可されているか確認してください。通知はタスクに時刻を設定した場合に届きます。集中モードがオンのときは、通知が表示されないことがあります。</p>
<h2>繰り返しのタスクが表示されない日がある</h2>
<p>毎月の指定日で、その月に存在しない日付（例: 31日）を選んだ場合、その月には発生しません。毎月の最終日に繰り返したいときは「月末」を選んでください。</p>
<h2>機種変更・アプリの再インストール</h2>
<p>TaskBitにはアプリ独自のクラウド同期がありません。アプリを削除すると、端末内のタスクや部屋のデータも削除されます。</p>
<h2>お問い合わせ</h2>
<p>解決しない場合は、<a href="mailto:{MAIL}">{MAIL}</a> までご連絡ください。TaskBitのバージョン、iOSのバージョン、iPhoneの機種、起きたことと直前の操作を書いていただくと確認が早くなります。</p>""",
    },
}

APP["t"]["en"] = {
    "name": "TaskBit",
    "store_name": "TaskBit: Gamified To-Do List",
    "title": "TaskBit: A Gamified To-Do List Where Your Room Grows",
    "description": "TaskBit is an iPhone to-do app where completing tasks earns coins that add furniture to a little companion's room. Repeating tasks, reminders and a calendar of completed tasks. Free.",
    "og_alt": "The TaskBit icon and the home screen with the room and today's tasks",
    "hub_line_ja": "タスクを終えると、小さな相棒の部屋に家具が増えていくToDoアプリ。",
    "hub_line_en": "A to-do app where finished tasks add furniture to a little companion's room.",
    "headline": "Finish one task.<br>Watch your room grow.",
    "lead": "TaskBit is an iPhone to-do list where every task you complete earns coins, and those coins add furniture to the room of your little companion, TaskBit. There are no streaks and nothing scolds you about missed days.",
    "price_note": "Free. Requires iOS 17.0 or later.",
    "hero_shot": "home",
    "hero_alt": "TaskBit home screen: a furnished room at the top and a list of today's tasks below",
    "summary": "TaskBit combines the basics of a to-do app (tasks, repeats, reminders and a calendar) with a room that grows as you complete tasks. It suits people who want to keep up with studying, reading, exercise or chores at their own pace by seeing small wins add up.",
    "facts": [
        ("Full name", "TaskBit: Gamified To-Do List"),
        ("What it does", "To-do list, daily, weekly and monthly repeats, timed reminders, calendar, collecting furniture and arranging a room"),
        ("Price", "Free, no in-app purchases"),
        ("Requirements", "iPhone with iOS 17.0 or later. The App Store also lists Macs with Apple M1 or later (macOS 14.0 or later) and Apple Vision Pro (visionOS 1.0 or later)"),
        ("Languages", "English, Japanese"),
        ("Where data is stored", "Tasks, history, coins and furniture stay on your device. No account and no cloud sync"),
        ("Category", "Productivity, Lifestyle"),
        ("Version", "1.4.0 (released October 31, 2026, US time)"),
        ("Developer", "Ryo Morishita"),
    ],
    "features_h": "What you can do with TaskBit",
    "features": [
        {
            "id": "tasks", "h": "Add a task, check it off",
            "alt": "New task screen with fields for the title, category, date, a time toggle and repeat",
            "body": "<p>Type a title and a date, save, and check the task off when it's done. You can also set a category and a time.</p>"
                    "<p>The home screen shows the room above today's tasks, and finished tasks move into a Completed group.</p>",
        },
        {
            "id": "repeat", "h": "Daily, weekly and monthly repeats",
            "body": "<p>Set repeats for things you do regularly, such as reading, studying, exercise or chores: every day, on chosen weekdays, on a day of the month, or at the end of the month. If you choose a date that a month doesn't have, such as the 31st, the task doesn't occur in that month.</p>",
        },
        {
            "id": "reminders", "h": "Reminders for timed tasks",
            "body": "<p>Give a task a time and TaskBit sends a notification at that time. Allow notifications for TaskBit on your iPhone to use reminders; you can change this any time in Settings.</p>",
        },
        {
            "id": "calendar", "h": "Plans and completed tasks on a calendar", "shot": "schedule",
            "alt": "Calendar screen: a month view with the tasks planned for the selected day listed below",
            "body": "<p>See upcoming plans and the tasks you've completed on a calendar. Since version 1.4.0 you can add a task again from your completion history: the title and category are prefilled, and nothing is saved until you review it and tap save.</p>",
        },
        {
            "id": "room", "h": "Earn coins, add furniture to the room", "shot": "room",
            "alt": "A more furnished TaskBit room with a window, shelves, a clock and plants, and the coin balance",
            "body": "<p>Completing tasks earns coins. Spend them on furniture and small items, and your companion's room changes little by little, so your everyday progress stays visible.</p>"
                    "<p>Your companion never gets hungry or needs care, and nothing goes wrong if you don't open the app for a while.</p>",
        },
        {
            "id": "arrange", "h": "Store and rearrange furniture", "shot": "arrange",
            "alt": "Arrange screen listing owned furniture, each with Store and Move buttons",
            "body": "<p>Put away furniture you've earned or move it to another spot it fits. Furniture isn't placed freely anywhere on screen; each item has its own set of available spots to choose from.</p>",
        },
    ],
    "steps": {
        "h": "How TaskBit works",
        "items": [
            ("Add something you can do today", "Enter a title and a date. Add a repeat for things you want to keep doing and a time for things you don't want to forget."),
            ("Check it off when you're done", "Completing a task earns coins. Missed a day? Nothing scolds you for it."),
            ("Grow the room", "Use your coins to add furniture, then store or move it to make the room your own."),
        ],
    },
    "gallery_h": "Screens from the app",
    "gallery": [
        ("home", "Home screen with the room and today's tasks"),
        ("create", "New task screen"),
        ("schedule", "Calendar screen"),
        ("arrange", "Arrange furniture screen"),
        ("room", "A room with more furniture"),
    ],
    "fit": [
        "People who make to-do lists but struggle to stick with them",
        "Anyone building a habit such as studying, reading, exercise or chores, without pressure",
        "People who lose motivation when a streak breaks",
        "Anyone who wants a cute to-do app that still has proper repeats and reminders",
    ],
    "limits": [
        "No account or cloud sync: your data lives only on the device you use and isn't shared with other devices",
        "No shared lists or assigning tasks to other people",
        "Furniture goes into the spots available for each item, not anywhere on screen",
        "Reminders need notification permission for TaskBit on your iPhone",
    ],
    "faq": [
        ("what", "What is TaskBit?",
         "<p>TaskBit is a to-do and task manager for iPhone. Completing tasks earns coins, which you use to add furniture to the room where a little companion lives. It isn't a virtual pet to look after; it's a way to enjoy small daily wins.</p>"),
        ("price", "Is TaskBit free?",
         "<p>Yes. TaskBit is free with no in-app purchases (as of version 1.4.0). Check the <a href=\"https://apps.apple.com/us/app/id6786552954\">App Store page</a> for the latest details.</p>"),
        ("habit", "Can I use it to build a study or reading habit?",
         "<p>Yes. Tasks can repeat every day, on chosen weekdays, on a day of the month, or at month end. There are no streaks or penalties, so after a day off you simply carry on.</p>"),
        ("streak", "Will I lose a streak or will my companion suffer if I skip a day?",
         "<p>No. TaskBit shows no streaks and doesn't scold you for missed days, and the companion has no hunger or care needs.</p>"),
        ("reminder", "Does TaskBit have reminders?",
         "<p>Yes. Give a task a time and TaskBit sends a notification at that time. Allow notifications for TaskBit on your iPhone.</p>"),
        ("history", "Can I look back at finished tasks?",
         "<p>Yes. The calendar shows upcoming plans and completed tasks, and you can add a task again from your history.</p>"),
        ("offline", "Does TaskBit need an internet connection?",
         "<p>Creating and completing tasks, the calendar and arranging the room work with data on your device. There is no online account or cloud sync.</p>"),
        ("data", "Where is my data stored?",
         "<p>Tasks, history, coins and furniture are stored on your device. To improve the app, TaskBit sends usage events (such as which screens were shown and whether features succeeded) with Google Analytics for Firebase; it does not send task titles or notification text. You can turn analytics off on the in-app Privacy screen. See <a href=\"/taskbit/en/privacy/\">Privacy</a> for details.</p>"),
        ("devices", "Can I move my data to another device?",
         "<p>TaskBit has no cloud sync of its own, so data isn't synced between devices automatically.</p>"),
    ],
    "closing_h": "Start with one thing you can do today",
    "closing": "Read for ten minutes, tidy your desk, go for a walk. Each small task you finish changes the room a little.",
    "privacy": {
        "title": "Privacy | TaskBit",
        "description": "What TaskBit stores and sends: tasks stay on your device, and usage analytics can be turned off in the app.",
        "h1": "TaskBit privacy",
        "body": f"""<p>A summary of the information TaskBit handles. The policy registered on the App Store is available <a href="{POLICY}">here</a> (in Japanese).</p>
<h2>Stored on your device</h2>
<p>Tasks (title, category, date, time and repeat settings), completion history, coins, and your furniture and its arrangement are stored on your device. There is no account and no cloud sync of TaskBit's own. Deleting the app deletes this data from the device.</p>
<h2>Notifications</h2>
<p>Reminders for timed tasks use iOS local notifications. Notification content is not sent anywhere.</p>
<h2>Usage analytics</h2>
<p>TaskBit uses Google Analytics for Firebase, provided by Google LLC, to improve onboarding, task creation and completion, rewards and reminders. Data that may be sent includes the app version; device, OS and language information collected automatically by Firebase Analytics; and predefined usage events such as screens shown, feature outcomes, whether a reminder is set and the repeat type.</p>
<p>TaskBit does not send task titles, notification text, exact task dates or times, email addresses, names, phone numbers or advertising identifiers (IDFA). Analytics data is not used for advertising.</p>
<p>Analytics is on by default. You can turn it off at any time on the in-app Privacy screen; after that, no new analytics events are sent.</p>
<h2>Contact</h2>
<p><a href="mailto:{MAIL}">{MAIL}</a></p>""",
    },
    "support": {
        "title": "Support | TaskBit",
        "description": "Help with TaskBit: common questions and how to contact the developer.",
        "h1": "TaskBit support",
        "body": f"""<h2>I don't get reminders</h2>
<p>Check that notifications are allowed for TaskBit in your iPhone's Settings. Reminders are sent only for tasks with a time. A Focus mode may hide notifications.</p>
<h2>A repeating task doesn't appear in some months</h2>
<p>If a monthly task is set to a date a month doesn't have (for example, the 31st), it doesn't occur that month. Choose "Last day" to repeat on the last day of every month.</p>
<h2>New phone or reinstalling the app</h2>
<p>TaskBit has no cloud sync of its own. Deleting the app deletes your tasks and room data from the device.</p>
<h2>Contact</h2>
<p>If you still need help, email <a href="mailto:{MAIL}">{MAIL}</a>. Including your TaskBit version, iOS version, iPhone model, what happened and what you did just before helps us look into it faster.</p>""",
    },
}
