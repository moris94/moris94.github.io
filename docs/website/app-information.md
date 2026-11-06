# アプリ情報（公式サイトの一次情報）

確認日: 2026-11-06（JST）。サイトの文面はこの表の「確認済み」の情報だけで書く。
アプリを更新したら、この表を先に更新してからサイトの文面を変える。

## 情報源と取得方法

| 記号 | 情報源 | 取得方法 | 備考 |
|---|---|---|---|
| L | iTunes Lookup API（Apple公式の公開API） | `https://itunes.apple.com/lookup?bundleId=…&country=jp/us/tw` | 正式名、説明文、バージョン、価格、最低OS、カテゴリ、言語、リリースノート、アイコン、スクリーンショット |
| W | 公開App Storeページ（apps.apple.com） | HTMLを取得して解析 | App内課金の商品名と価格、App Privacyラベル、互換性、プライバシーポリシーURL |
| R | 各アプリのリポジトリ（非公開） | 開発者の手元で読んだ | fastlaneメタデータ（サブタイトル・キーワード・プロモーションテキスト）、仕様書、公開タグのコード、実画面キャプチャ |
| N | 既存の公開ポリシー（Notion） | ブラウザで表示して読んだ | App Storeに登録済みのプライバシーポリシー・サポートURL |

### 未取得の項目

App Store Connect APIでしか取れない項目（提供国・地域の一覧、各国の価格表など）は未取得。公開中のApp Store（L・W）の値を正とし、リポジトリの値（R）は照合に使った。

## 共通

| 項目 | 値 | 源 |
|---|---|---|
| 開発者・販売元 | Ryo Morishita | L（sellerName / artistName） |
| サポート連絡先 | shunmemo.support@gmail.com | N（TaskBit、GeoAlbum、StudyFocus（規約の末尾は未取得）、カエルートのポリシー） |
| 評価・レビュー | 評価件数 0（全アプリ、2026-11-06）。サイトと構造化データに評価は載せない | L |
| 年齢区分 | 4+（全アプリ） | L |

## TaskBit

| 項目 | 値 | 源 |
|---|---|---|
| App Store ID | 6786552954 | L |
| 正式名（日本） | TaskBit：育つToDo・タスク管理 | L |
| 正式名（米国） | TaskBit: Gamified To-Do List | L |
| サブタイトル | 達成が部屋の成長に変わるやることリスト / Build Habits, Grow Your Room | R（aso-phase1） |
| Bundle ID | com.moris94.taskbit | L |
| 公開バージョン | 1.4.0（2026-11-01 JST公開） | L |
| 初回公開 | 2026-07-07 | L |
| 対応OS | iOS 17.0以降。互換性: Apple M1以降のMac（macOS 14.0以降）、Apple Vision Pro（visionOS 1.0以降） | L・W |
| カテゴリ | 仕事効率化（Productivity）、ライフスタイル | L |
| 言語 | 日本語、英語 | L |
| 価格 | 無料。App内課金の表示なし | L・W |
| 主な機能（1.4.0） | タスクの作成・編集・完了／日付・時刻・毎日・毎週・毎月の繰り返し／時刻を指定したタスクのリマインダー／カレンダーで予定と完了履歴／完了履歴から再登録（1.4.0の新機能）／完了でコインが貯まり、コインで家具を増やす／家具の収納と模様替え | L（説明文・リリースノート）、R（v1.4タグのコード） |
| 方針 | 連続記録やできなかった日を責める表示はない | L |
| データ保存 | タスク、完了履歴、コイン、家具は端末内。v1.4にアプリ内のクラウド同期はない | R |
| 分析 | v1.4のコードにGoogle Analytics for Firebaseが含まれる。アプリ内の「プライバシー」画面で無効にできる | R（v1.4タグ） |
| プライバシーURL | https://bottlenose-network-d4d.notion.site/TaskBit-391661a42a4a80b4ad01d490f9bede3f | W |
| スクリーンショット | `AppStoreScreenshots/raw/{ja,en-US}/01〜05`（2026-10-26撮影、公開中のスクリーンショットと同じ画面） | R |
| 開発中（掲載しない） | v1.5の有料の追加部屋（審査提出済み、未公開） | R |

## GeoAlbum

| 項目 | 値 | 源 |
|---|---|---|
| App Store ID | 6813050203 | L |
| 正式名 | GeoAlbum（日本）／GeoAlbum: Sort Photos by Place（米国） | L |
| サブタイトル | 撮影場所で写真をアルバム整理 / Sort Photos by Where Taken | R |
| Bundle ID | com.moris94.geoalbum | L |
| 公開バージョン | 1.1.0（2026-10-01公開）。初回公開 2026-09-24 | L |
| 対応OS | iOS 18.0以降。互換性: Mac（macOS 15.0以降、M1以降）、Apple Vision Pro（visionOS 2.0以降） | L・W |
| カテゴリ | 写真/ビデオ、ユーティリティ | L |
| 言語 | 日本語、英語 | L |
| 価格 | 無料。App内課金「GeoAlbum Pro」¥1,100 / $6.99（買い切り） | L・W |
| 無料版 | 場所ルール1つ | L |
| Pro | 複数の場所ルール、まとめてスキャン | L |
| 対象外 | 動画、非表示の写真、撮影位置がない写真。位置情報のない写真の撮影場所は推定しない | L・N |
| 写真の扱い | 原本を移動・削除・複製しない。追加前にユーザーが確認。追加済みはスキップ。ルール変更・削除で写真とアルバムは変わらない | L |
| 通信 | 地図、住所・施設名の検索、iCloud写真の読み込み、購入でAppleのサービスと通信する場合がある | L・N |
| 位置情報権限 | v1.1.0で「現在地へ」ボタンを追加。押したときだけ「使用中のみ」の許可を求め、最初のピンを現在地に置くためだけに使う | R（v1.1.0タグ） |
| プライバシーURL | https://bottlenose-network-d4d.notion.site/GeoAlbum-3dd661a42a4a80a4940ffe0ed93721e0 | W |
| スクリーンショット | `artifacts/appstore/raw/{ja,en-US}/01〜06`（ファイル名が公開中のものと一致） | R・L |

## StudyFocus（勉強集中 / Study Focus）

| 項目 | 値 | 源 |
|---|---|---|
| App Store ID | 6800586592 | L |
| 正式名 | 勉強集中 - SNS ブロッカー（日本）／Study Focus - Social Blocker（米国） | L |
| Bundle ID | com.moris94.studyfocus | L |
| 公開バージョン | 1.0（2026-08-15公開） | L |
| 対応OS | iOS 17.0以降（Screen Timeの許可が必要） | L |
| カテゴリ | 教育、仕事効率化 | L |
| 言語 | 日本語、英語 | L |
| 価格 | 無料。App内課金「勉強集中 Pro / Study Focus Pro」¥300 / $2.99 | W |
| Proの形態 | 月額の自動更新サブスクリプション（日本: 月額300円） | N（利用規約）、R |
| 無料版 | 1日5回までの集中セッション完了、ブロック対象は個別アプリ3個まで、直近7日の記録 | N・R |
| Pro | 集中回数、ブロック対象（アプリ・カテゴリ・Webサイト）、記録の表示期間が無制限 | N・R |
| データ | タイマー設定、ブロック対象、記録は端末内。サーバー同期・iCloud同期・外部分析なし | N |
| 利用規約・プライバシー | https://bottlenose-network-d4d.notion.site/StudyFocus-3ba661a42a4a80c8a72dce3a4a054361 | L・W |
| スクリーンショット | `fastlane/screenshots/raw/ja-JP`、`raw_en/en-US`（2026-08-12撮影） | R |

## カエルート（Kaeroute）

| 項目 | 値 | 源 |
|---|---|---|
| App Store ID | 6811297451 | L |
| 正式名 | カエルート - 防災・徒歩帰宅ルート（日本・台湾） | L |
| 繁体字名 | Kaeroute 返家路線・防災準備 | R |
| サブタイトル | オフライン地図で備える。帰り道をPDF・紙にも | R |
| Bundle ID | com.moris94.kaeroute | L |
| 公開バージョン | 1.0.0（2026-09-24 JST公開） | L |
| 対応OS | iOS 17.0以降 | L |
| カテゴリ | ナビゲーション、ユーティリティ | L |
| 言語 | 日本語、繁体字中国語（**英語UIはない**） | L・W |
| 配信 | 日本・台湾のストアで確認。米国・香港のストアでは見つからない | L |
| 価格 | 無料。App内課金「カエルート Pro」¥980（買い切り。サブスクリプションではない） | L・W |
| 無料 | 1件の計画、その主経路と必要な地図の保存、保存済み情報の参照 | L |
| Pro | 複数計画、代替経路を最大2件、注意地点とメモ、A4のPDF作成・共有・AirPrint印刷、見直し通知 | L |
| 通信 | 地点検索、新しいルートの作成、地図のダウンロードはインターネットが必要。地点検索はApple MapKit、経路はopenrouteservice/HeiGIT、地図ファイルはGitHubなどから取得 | L・N |
| データ | アカウント不要。アプリ独自のクラウド同期と常時の位置追跡はない。計画は設定から削除できる | L |
| 地図・経路データ | © OpenStreetMap contributors（ODbL）、openrouteservice / HeiGIT | R（アプリ内の表記） |
| 注意事項 | 災害後の道路状況・安全性・通行可能性を保証しない。帰宅開始のタイミングを判断しない | L |
| プライバシー・サポートURL | https://bottlenose-network-d4d.notion.site/3da661a42a4a800095aad0247a42414f | W・R |
| スクリーンショット | `artifacts/screenshots/raw/ja`（ファイル名が公開中のものと一致） | R・L |
| 開発中（掲載しない） | 地図カタログの拡張、オフラインダウンロードの変更（2026-11のコミット） | R |

## サイトに書いた細かな事実の根拠

上の表に加えて、サイトの本文で使った事実とその源。

| アプリ | 事実 | 源 |
|---|---|---|
| TaskBit | 分析で送らない情報（タスク名、通知本文、具体的な日時、連絡先、IDFA）、分析は初期状態で有効、広告に使わない、アプリ内で無効化できる | R（`docs/privacy/privacy-policy-v1.1.md`、v1.4タグの `PrivacyView.swift`・`FirebaseAnalyticsTracker.swift`） |
| TaskBit | アプリを削除すると端末内のデータも削除。個人を特定する情報を取得しない（アカウントなし） | N（2026-07-02版） |
| TaskBit | 相棒にお世話の義務はない、連続記録・責める表示はない | L（説明文）、R（プロダクト憲章） |
| TaskBit | コインで家具を手に入れる | R（v1.4 `FurniturePurchaseUseCase.swift`） |
| TaskBit | 繰り返し「月末 / Last day」の表記 | R（v1.4の文字列） |
| GeoAlbum | 照合は端末内、独自サーバーへ送らない、アカウント・広告・追跡なし、Live Photos対応、端末内に保存する情報、診断情報は手動共有 | L（説明文）、N（2026-09-16版） |
| StudyFocus | 一時停止・スキップ、集中・休憩の終了をローカル通知、ロック画面のLive Activity | R（公開直前のコミット 07483de のREADMEと文字列、LiveActivityターゲット） |
| カエルート | 保存状態と最終確認日の表示 | L（説明文） |
| カエルート | 現在地はボタン操作時だけ取得、移動履歴を残さない、地点検索はApple MapKit | N（2026-09-13版）、R（設定画面の表示） |
