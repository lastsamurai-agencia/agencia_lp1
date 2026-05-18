# オフィス清掃LP

_Started 2026-05-18 06:36 UTC_

---

## User

オフィスやビルの清掃を行っている会社を運用している
google広告用にLPを作成したい

## Assistant

_[tool: questions_v2]_

## User

Questions answered:
- company_name: 株式会社AGENCIA
- service_area: 東京都
- target_customer: オフィスビル管理会社, 中小企業のオフィス, 店舗・商業施設, 病院・クリニック, 学校・公共施設, マンション管理組合
- service_types: 日常清掃（定期）, 定期清掃（月1回など）, トイレ清掃, 原状回復, ガラス清掃, スポット清掃, カーペット清掃, 排水管洗浄
- key_strengths: 対応の早さ・スピード, 見積り無料, 有資格者在籍, 柔軟な対応・カスタマイズ
- main_cta: 無料見積り依頼
- tone: 清潔感重視（白・水色・爽やか）
- hero_style: 大きな写真＋キャッチコピー＋CTA（王道）
- price_display: 目安料金のみ
- sections_wanted: 強み・選ばれる理由, サービス内容, 料金プラン, お客様の声, ビフォーアフター, 会社概要, よくある質問, お問い合わせフォーム
- variations: 1案でしっかり作る
- tweaks_interest: CTAの文言, フォント
- extra_info: 03-6555-1607がお問い合わせ電話番号
弊社のコーポレートサイトはhttps://languid-cleaning.jp/
LPの構成などの参考はこのサイトを参考にして https://sentakuki-toritsuke.com/tokyo/

## Assistant

_[tool: update_todos]_

_[tool: web_fetch]_

_[tool: web_fetch]_

参考サイトの内容と御社のコーポレートサイトを確認しました。会社情報・有資格者・保有資格番号なども把握できたので、Google広告向けにコンバージョン重視の縦長LPを構築します。

**デザイン方針:**
- 清潔感のあるホワイト × スカイブルー、CTAにコーラル系で訴求力アップ
- 王道のヒーロー → お悩み → 選ばれる理由 → サービス → 料金 → BeforeAfter → お客様の声 → 流れ → FAQ → 会社概要 → フォームの長尺LP構成
- 全セクションから到達しやすい固定の電話・CTAバー（モバイル）
- フォント: Noto Sans JP（Tweaksで切替可）
- 写真は実写プレースホルダー（後で差し替え可能）

_[tool: copy_starter_component]_

_[tool: read_file]_

_[tool: write_file]_

_[tool: grep]_

_[tool: str_replace_edit]_

_[tool: update_todos]_

_[tool: done]_

_[tool: fork_verifier_agent]_

株式会社AGENCIA様のGoogle広告用LPを作成しました。

**主な構成（縦長LP・王道構成）:**
1. ヒーロー（キャッチ＋特徴バッジ＋無料見積りCTA＋電話）
2. お悩み6つ → SOLUTION
3. 選ばれる理由 4つ（対応の早さ／無料見積り／有資格者／柔軟対応）
4. サービス内容 8種
5. 目安料金プラン（参考サイトの料金感に合わせて）
6. 中間CTAバナー
7. ビフォーアフター 4事例
8. お客様の声 3件
9. ご依頼の流れ 5ステップ
10. FAQ アコーディオン
11. 会社概要＋保有資格／登録番号
12. お問い合わせフォーム
13. フッター
14. モバイル用 固定CTAバー（電話 / 見積り）

**色・タイポ:** 白＋スカイブルー基調、CTAはコーラルでクリック誘導。Noto Sans JP デフォルト。

**Tweaks（右下パネル）:**
- CTAボタンの文言（全箇所一括変更）
- フォント（Noto Sans JP / Zen Kaku Gothic New / M PLUS 1p / Klee One から選択）

**次のステップとしておすすめ:**
- ヒーロー・サービス・ビフォーアフターの写真を実画像に差し替え（プレースホルダーで配置済み）
- フォーム送信先（メール / お問い合わせシステム）の接続
- Google広告のコンバージョンタグ設置

## User

電話ボタンで携帯の電話アプリが立ち上げれるようにしてもらえるかな？
またスマートフォンへのレスポンシブ対応はされている？

あとは画像を入れたいので、そのファイルを教えてください

## Assistant

_[tool: view_image]_

_[tool: str_replace_edit]_

ご質問にお答えします。

1. **電話ボタンのタップ発信** — すでに全ての電話ボタンに `tel:0365551607` リンクを実装済みなので、モバイルでタップすると電話アプリが起動します。念のため全箇所動作するか確認します。

2. **レスポンシブ対応** — 960px以下のブレイクポイントは実装済みですが、スマホ実機向けに小さめ画面（〜375px）の調整も追加します。

3. **画像ファイル** — `images/` フォルダを作成し、必要なファイル名一覧を `images/README.txt` に明記します。また写真がアップロードされたら自動で表示される仕組みに変更します。

_[tool: str_replace_edit]_

_[tool: str_replace_edit]_

_[tool: grep]_

「Languid Cleaning Service」を全箇所から削除します（ヘッダー・フッター）。

_[tool: grep]_

_[tool: str_replace_edit]_

_[tool: grep]_

_[tool: grep]_

「Languid Cleaning Service」を全箇所削除しました（ヘッダー・フッター・会社概要の商号欄）。代わりに「東京のオフィス・ビル清掃」という説明文に置き換えています。

引き続き、画像読み込みの仕組みと、レスポンシブ強化、画像ファイル一覧を準備します。

_[tool: str_replace_edit]_

_[tool: str_replace_edit]_

_[tool: write_file]_

_[tool: done]_

_[tool: run_script]_

画像ファイルが404を返さないよう、JS側で実ファイル存在チェックを行ってから挿入する方式に変更します。

_[tool: grep]_

_[tool: done]_

完了です。ご質問への対応をまとめます。

**1. 電話タップ発信** ✓
全ての電話番号に `tel:0365551607` リンクを実装済み。スマホ・タブレットでタップすると電話アプリが起動します（ヘッダー / ヒーロー / 中間バナー / 会社概要 / フッター / モバイル固定バー の計5箇所）。

**2. レスポンシブ対応** ✓
- 〜960px（タブレット）：グリッド1〜2列に再構成、モバイル用固定CTAバーを表示
- 〜480px（スマホ実機）：フォントサイズ・余白・CTA幅100%化など細かく最適化
- ヒーロー、価格表、フォーム、FAQ、ビフォーアフター、流れ など全セクションが画面幅に応じて自動調整されます

**3. 画像ファイルの配置場所** — `images/` フォルダに以下のファイル名で配置してください（合計17枚）：

| ファイル名 | 内容 | 推奨サイズ |
|---|---|---|
| `hero.jpg` | ヒーロー（メインビジュアル） | 1200×1500（縦長） |
| `service-01.jpg` 〜 `service-08.jpg` | 8つのサービス画像 | 1200×900 |
| `before-01.jpg` 〜 `before-04.jpg` | ビフォー4枚 | 1200×900 |
| `after-01.jpg` 〜 `after-04.jpg` | アフター4枚 | 1200×900 |

詳細は `images/README.txt` に記載しています。

**仕組み:** JSが起動時に各ファイルの存在を確認し、アップロード済みの画像だけを自動的に表示します。未アップロードの箇所はストライプのプレースホルダーのまま残ります（順次差し替え可能）。

## User

Apply comment

## Assistant

_[tool: str_replace_edit]_

ロゴ画像を `images/logo.svg` または `images/logo.png` に置けば自動でAマークと差し替わるよう実装します。

_[tool: str_replace_edit]_

_[tool: str_replace_edit]_

_[tool: str_replace_edit]_

_[tool: done]_

対応完了しました。

**ロゴ画像の配置方法:**
`images/` フォルダに `logo.svg`（推奨）または `logo.png` を配置してください。ヘッダー左上とフッターの「A」マークと自動で差し替わります。

- 推奨サイズ：正方形（128×128px〜）／透過PNG または SVG
- SVGが存在すれば優先、なければ PNG を読み込みます
- どちらもなければ現在の青いグラデーション＋「A」マークがそのまま表示されます

`images/README.txt` にもロゴの項目を追記しました（合計18ファイル）。

## User

<attached_files>
- images/logo.png
</attached_files>

## Assistant

_[tool: image_metadata]_

_[tool: show_html]_

_[tool: show_html]_

_[tool: save_screenshot]_

_[tool: view_image]_

_[tool: eval_js]_

_[tool: eval_js]_

_[tool: eval_js]_

_[tool: list_files]_

_[tool: eval_js]_

_[tool: eval_js]_

_[tool: eval_js]_

_[tool: eval_js]_

_[tool: grep]_

_[tool: read_file]_

_[tool: get_webview_logs]_

_[tool: eval_js]_

_[tool: sleep]_

_[tool: eval_js]_

_[tool: save_screenshot]_

_[tool: view_image]_

_[tool: done]_

ロゴが正常に反映されました。ヘッダー左上に黄・黒・オレンジのドットロゴが表示されています（フッターも同様）。ロゴが正常に表示されています。`images/logo.png` を自動で検出してヘッダーとフッターの「A」マークと差し替えました。

他の画像（hero / service / before-after）も同じく `images/` フォルダにファイルを置けば順次自動反映されます。

## User

Apply comment

## Assistant

_[tool: str_replace_edit]_

ヒーロー全体の背景に画像を設置できるようにします。`images/hero-bg.jpg` を配置すれば自動で背景になり、上に半透明オーバーレイを重ねて文字の可読性を確保します。

_[tool: str_replace_edit]_

_[tool: str_replace_edit]_

_[tool: done]_

ヒーローセクションに背景画像を設置する仕組みを追加しました。

**設置方法:**
`images/hero-bg.jpg` をアップロードすると、ヒーロー全体の背景に自動表示されます。
- 推奨サイズ：1920×1200px（横長16:10）
- 文字の可読性のため**白系の半透明オーバーレイ**が上に自動で重なります
- ファイルがない場合は現在の淡い水色グラデーションのまま

仕上がり調整は実際の画像で見ながら、オーバーレイの濃さや位置をご相談ください。

## User

Apply comment

## Assistant

_[tool: str_replace_edit]_

_[tool: str_replace_edit]_

ビフォーアフター事例03を「業務用エアコンの分解洗浄」に変更しました。`images/README.txt` も更新しています。

## User

<attached_files>
- images/images:hero-bg.jpg
</attached_files>

## User

フッターにコーポレートサイトへのリンクを追加してください

## Assistant

_[tool: list_files]_

_[tool: str_replace_edit]_

_[tool: done]_

フッターのお問い合わせ欄に「コーポレートサイト」リンク（https://languid-cleaning.jp/ ）を追加しました。外部リンクアイコン付きで、新しいタブで開きます。

## User

Apply comment

## Assistant

_[tool: str_replace_edit]_

_[tool: done]_

_[tool: web_fetch]_

料金表に下記のエアコン関連メニューを追加しました。

| メニュー | 目安料金 |
|---|---|
| 業務用エアコン分解洗浄（2.5馬力まで） | ¥25,000〜/台 |
| 業務用エアコン取り付け（2.5馬力まで） | ¥38,500〜/台 |
| 換気扇・レンジフード分解クリーニング | ¥15,000〜/台 |

**ご確認のお願い:**
- 「業務用エアコン取り付け」はコーポレートサイトの掲載値（38,500円／2.5馬力まで）をそのまま使用しています
- **「エアコン分解洗浄」「換気扇クリーニング」の金額はコーポレートサイトに記載がなかったため、業界相場を仮で入れています**。正確な料金がお決まりでしたら、お知らせいただければ差し替えます

## User

ありがとう。メインビジュアルだけども、携帯の表示だと画像やサイズなどが、小さく訴求力がなくなってしまう。https://miraisetsubi.com/を参考に全体的なサイズ感を訴求力高めに調整してほしい

## Assistant

_[tool: read_file]_

_[tool: grep]_

_[tool: web_fetch]_

参考サイトには直接アクセスできなかったので、訴求力の高いLPのモバイル定番パターン（大画像トップ＋大胆な見出し＋オーバーレイCTA）でリビルドします。

_[tool: str_replace_edit]_

_[tool: str_replace_edit]_

_[tool: save_screenshot]_

_[tool: view_image]_

_[tool: image_metadata]_

_[tool: web_fetch]_

参考サイトを確認しました。モバイルではヒーロー画像が画面いっぱいの大判ビジュアルで強く訴求している作りですね。同様にhero-bg.jpgを大胆に活かしたモバイル専用のヒーローに作り直します。

_[tool: str_replace_edit]_

_[tool: save_screenshot]_

_[tool: view_image]_

参考サイトの特徴：モバイルでは大判ヒーロービジュアルが画面いっぱいに広がり、シンプルでインパクトのある縦長レイアウト。同じ構造で組み直します。

_[tool: show_html]_

_[tool: sleep]_

_[tool: save_screenshot]_

_[tool: view_image]_

_[tool: save_screenshot]_

_[tool: view_image]_

_[tool: eval_js]_

_[tool: done]_

モバイルのヒーローを参考サイト風に大胆に変更しました。

**変更内容:**

1. **画像を全画面化** — モバイル時はヒーロー背景画像（`hero-bg.jpg`）が画面の88%まで広がり、画像主体のレイアウトに
2. **大きな見出し** — H1 を 42px に拡大、白文字＋影で背景画像の上でも視認性確保
3. **大きなCTAボタン** — 横幅100%、padding 20px、文字17px に拡大、強い影で立体感
4. **電話CTAも大判化** — 半透明白ガラス調のカード内に大きな番号を配置（30px）
5. **トラスト帯を強化** — ヒーロー直下にブランド色フルブリードで実績数値を表示
6. **右サイドの写真カードは非表示** — モバイルでは背景画像が主役なので削除

**重要なお願い 🔔**

現在の `hero-bg.jpg` は **360×240px** と小さく、モバイル全画面で表示するとぼやけます。
できれば **1600×1200px 以上**の高解像度版に差し替えていただけると、訴求力が大きく向上します。

実機（iPhone/Android）でご確認ください。プレビューパネルでは正確に再現できません。

## User

Apply comment

## Assistant

_[tool: str_replace_edit]_

「100% 有資格者プラン設計」を「**3資格 / 国家・公的資格を保有**」に変更しました。

具体的な数字＋公的資格という客観的事実で、信頼性と訴求力が強くなります（保有資格3つ：ビルクリーニング技能士／清掃作業監督者／建築物清掃管理資格者に対応）。

別の数字に置き換えたい場合（例：「創業○年」「顧客継続率○%」「対応実績○件」など）、実数があればお知らせください。

## User

事例04：店舗フロアを閉店後にスピード仕上げ
この部分をマンション共有部の床洗浄に変えてください

## Assistant

_[tool: str_replace_edit]_

_[tool: str_replace_edit]_

事例04を「マンション共用部の床洗浄＋WAX」に変更しました。

- 見出し：マンション共用部の床洗浄＋WAX
- 説明：エントランス・廊下・エレベーターホールなど、住人が毎日歩く共用部の床面を剥離洗浄＋WAXでリフレッシュ
- タグ：マンション / 定期清掃

`images/README.txt` も合わせて更新しています。

## User

WAXはなしでOK

## Assistant

_[tool: str_replace_edit]_

_[tool: str_replace_edit]_

_[tool: grep]_

_[tool: read_file]_

_[tool: str_replace_edit]_

事例04を「マンション共用部の床洗浄」に修正しました（WAX表記を削除、誤字も修正）。

## User

<attached_files>
- images/after-01.jpg
- images/after-02.jpg
- images/after-03.jpg
- images/after-04.jpg
- images/before-01.jpg
- images/before-02.jpg
- images/before-03.jpg
- images/before-04.jpg
- images/service-01.jpg
- images/service-02.jpg
- images/service-03.jpg
- images/service-04.jpg
- images/service-05.jpg
- images/service-06.jpg
- images/service-07.jpg
- images/service-08.jpg
</attached_files>

## Assistant

_[tool: show_html]_

_[tool: sleep]_

_[tool: save_screenshot]_

_[tool: view_image]_

すべての画像（16枚）を受け取りました。`images/` フォルダに配置済みなので、LPに自動で表示されます。

_[tool: done]_

16枚の画像（サービス8枚＋ビフォーアフター8枚）すべてLPに自動反映されました。

**画像の自動マッピング:**
- サービス：日常清掃→ポリッシャー→トイレ→ガラス→カーペット→排水管→原状回復→エアコンの順
- ビフォーアフター：床洗浄／縞模様タイル／業務用エアコン分解／マンション共用部（玄関前）

**気になった点（任意調整）:**
- 1枚目のサービス画像が「業務用エアコン清掃」になっていますが、見出しは「日常清掃（定期）」です。日常清掃のイメージとしては合っていない可能性があるので、もしお手元に**掃除機がけ／拭き掃除のような日常風景の写真**があれば、`service-01.jpg` として上書きすると整合性が取れます（現状のままでも問題ありません）
- ヒーロー右の縦長カード `hero.jpg`（任意）は未アップですが、モバイル時は非表示なので問題ありません。PCでヒーローを写真化したい場合のみ追加してください

実機でモバイル表示もご確認いただけると安心です。

## User

<attached_files>
- images/hero.jpg
</attached_files>

## Assistant

ヒーロー画像（AGENCIAロゴ入りスタッフ写真）を受け取りました。`images/hero.jpg` に配置済みなので、PCのヒーロー右側に自動で表示されます。

笑顔のスタッフ写真は、清掃業の「人」の信頼感を訴求するのにとても効果的です。

**現在のヒーロー画像のオーバーレイ:**
- 左上：「No.1 東京の柔軟対応 清掃パートナー」バッジ
- 右下：「建築物清掃業登録済 ★★★★★」カード

写真にスタッフが映っているので、オーバーレイがお顔にかからないか実機でご確認ください。もしバッジを非表示にしたい・位置を変えたい・人物に合わせた文言（お名前やご挨拶など）に変えたい場合は、お知らせください。

## User

Apply comment

## Assistant

_[tool: str_replace_edit]_

「柔軟なカスタマイズ」を「**柔軟対応可能**」に変更しました。これで4つすべて6文字に揃いました。

- お見積り無料（6文字）
- 最短即日対応（6文字）
- 有資格者在籍（6文字）
- 柔軟対応可能（6文字）

## User

Apply comment

## Assistant

_[tool: grep]_

_[tool: str_replace_edit]_

ファイル名表示を一括で非表示にします（ビフォーアフター・サービス画像・ヒーロー画像すべて）。全画像のファイル名ラベルを非表示にしました：
- ビフォーアフターの「before-XX.jpg / after-XX.jpg」
- サービスカードの「SVC_XX / service-XX.jpg」
- ヒーローの「HERO_IMAGE / images/hero.jpg」

画像が読み込まれていない場合は引き続きストライプのプレースホルダーが表示されます（テキストのみ消えた状態）。

## User

Apply comment

## Assistant

_[tool: grep]_

_[tool: str_replace_edit]_

ヘッダー・フッター両方のロゴ下のサブテキストを「**清掃のことならお任せ下さい！**」に変更しました。

Google広告のSEO観点では「東京」というキーワードも残しておいた方が有利な場合があります。下記タグはそのままにしてあります（必要であれば変更します）:
- ブラウザタブのタイトル：`東京のオフィス・ビル清掃 | 株式会社AGENCIA - 無料お見積り`
- description（検索結果に出る文）：`東京のオフィス・ビル清掃ならAGENCIA...`

こちらも訴求文に変更しますか？

## User

いいアイデアだね、それでいいと思うけど、どう？

## Assistant

_[tool: str_replace_edit]_

はい、SEO観点では「東京」「オフィス・ビル清掃」は重要キーワードなので、タイトル・descriptionに残すのは賢明だと思います。

現在のままでも問題ありませんが、せっかくなのでロゴの新タグライン「清掃のことならお任せ下さい！」のニュアンスも反映させて、より訴求力のあるdescriptionに磨きをかけました：

_[tool: read_file]_

_[tool: str_replace_edit]_

descriptionを更新しました。

**Before:** 東京のオフィス・ビル清掃ならAGENCIA。最短即日対応・有資格者在籍・無料お見積り。日常清掃から定期清掃、原状回復まで柔軟に対応します。

**After:** 東京のオフィス・ビル清掃なら株式会社AGENCIAにお任せください。日常清掃・定期清掃・原状回復・エアコン洗浄まで、有資格者チームがワンストップで対応。最短即日のお見積りは無料です。

「お任せください」のニュアンスと、新サービスの「エアコン洗浄」を追加しました。SEOキーワード（東京・オフィス・ビル清掃）はそのまま残してあります。

## User

Apply comment

## Assistant

_[tool: image_metadata]_

_[tool: view_image]_

_[tool: str_replace_edit]_

写真の顔位置を確認しました。顔は上部20%あたりにあるので、レスポンシブで縦横比が変わっても顔が常に見える位置に固定します。写真の表示位置を「中央上寄り（22%）」に固定しました。

これで画面幅に応じてヒーローカードの縦横比が変化しても（PC：縦長 4:5 / タブレット：横長 5:4）、顔が見切れずに常に表示されるようになります。`object-fit: cover` で自動拡大しつつ、表示の基準点を顔の高さに合わせる仕組みです。

別の写真に差し替えた際、顔の位置が大きく変わる場合は数値（現在22%）を調整できます。

## User

Apply comment

## Assistant

_[tool: copy_starter_component]_

_[tool: write_file]_

_[tool: show_html]_

_[tool: sleep]_

_[tool: save_screenshot]_

_[tool: view_image]_

_[tool: view_image]_

_[tool: view_image]_

_[tool: view_image]_

_[tool: view_image]_

_[tool: view_image]_

_[tool: view_image]_

_[tool: view_image]_

スマホ表示で全セクションの余白を細かく見直します。まず現状を確認します。

_[tool: grep]_

_[tool: grep]_

_[tool: read_file]_

直接CSSを精査して、モバイルでの余白のズレを修正します。

_[tool: str_replace_edit]_

_[tool: str_replace_edit]_

_[tool: str_replace_edit]_

主な問題点を発見しました。順に整理します：

**問題1：`pain-arrow` の上下余白アンバランス**
- 矢印の上：pain-grid の `margin-bottom: 42px` + arrow の `margin-top: 6px` = **48px**
- 矢印の下：arrow の `margin-bottom: 20px` = **20px**
→ 上下が28pxもズレている

**問題2：モバイルで矢印が大きすぎる（42px）**

**問題3：flow-step の縦並び時、矢印が消えて区切りが弱い**

**問題4：sec-title 周辺の余白**

これらを一気に整理します：

_[tool: str_replace_edit]_

_[tool: str_replace_edit]_

_[tool: grep]_

_[tool: read_file]_

_[tool: run_script]_

_[tool: done]_

スマホ表示の余白ズレを全体的に整理しました。

**主な修正点:**

1. **▼矢印（pain-arrow）の上下余白を対称化**
   - 修正前：上48px / 下20px（28pxズレ）
   - 修正後：上下とも28px / モバイルでは24px の対称配置
   - モバイルで矢印サイズも 42px → 26px に調整

2. **モバイル時の「ご依頼の流れ」セクション**
   - 縦並びになった際に各ステップ間に下向き矢印（▼）を追加
   - PCの右向き矢印（▶）を縦並びで再現することで、フローの流れが視覚的に分かりやすく

3. **SOLUTION バナーの行間調整**
   - モバイル時に「そのお悩み、AGENCIAが解決します」が読みやすい行間に

4. **その他**
   - お悩みカードのgapとmargin-bottomを統一
   - flow-grid のカード間gapを 14px → 24px に拡張

参考サイトのように、各セクションの上下リズムが揃った状態になります。実機でモバイル表示をご確認ください。

## User

Apply comment

## Assistant

_[tool: str_replace_edit]_

_[tool: str_replace_edit]_

お悩みカードの強制改行（`<br>`）を全6枚から削除しました。

**変更内容:**
- 各カードの不要な改行を削除し、テキストが自然に折り返すように
- `text-wrap: pretty` を適用して、改行時のバランスを自動最適化
- カードの幅に応じて1行や2行に綺麗に収まる

スマホ・PC両方で、右側の余白が出ない自然なレイアウトになります。

## User

選ばれる４つの理由のところ
カードの内容がとても良いので、スマホ画面で詳細説明が消えてしまうのが勿体無い。

デザイン的に損なわないように文章も表示してもらウェルかな

## Assistant

_[tool: grep]_

_[tool: str_replace_edit]_

_[tool: str_replace_edit]_

「選ばれる4つの理由」のモバイル時レイアウトを再構成して、説明文をしっかり読ませるデザインに変更します。「選ばれる4つの理由」のモバイル・タブレット表示を改善しました。

**変更内容:**

- **横並び（数字｜本文）→ 縦並びレイアウトに変更**
  - 数字スペースが固定幅で本文を圧迫していた問題を解消
  - 本文が画面幅いっぱい使えるようになり、説明文がしっかり読める

- **REASON番号を上部にコンパクトに配置**
  - 「REASON」ラベルをブランド色のピル型バッジ風に
  - 数字（01〜04）を横に並べた1行のヘッダー形式に整理

- **本文サイズを拡大**
  - スマホ：13.5px → **14.5px**（説明文）／17px → **18px**（見出し）
  - タブレット：14.5px / 19px（説明文 / 見出し）

これで折角の説明文がしっかり訴求できる形になります。

