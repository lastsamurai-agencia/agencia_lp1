# 株式会社AGENCIA Google・Yahoo広告 LP タスク管理

最終更新: 2026-05-21

---

## ⏭️ 明日やること（ここから再開）

### 【STEP 1】広告タグのID設定 ← 最優先
> 各広告アカウントを作成してIDを取得し、「タグIDを設定して」と依頼するだけでOK

- [ ] **GA4（Googleアナリティクス）**
  - [analytics.google.com](https://analytics.google.com) でプロパティ作成
  - 測定ID（`G-XXXXXXXXXX`）を取得 → Claude Codeに共有

- [ ] **Google広告**
  - [ads.google.com](https://ads.google.com) でアカウント作成
  - コンバージョン「フォーム送信」「電話クリック」を作成
  - コンバージョンID・ラベルを取得 → Claude Codeに共有

- [ ] **Yahoo!広告**
  - [marketing.yahoo.co.jp](https://marketing.yahoo.co.jp) でアカウント作成（法人番号が必要）
  - コンバージョンIDを取得 → Claude Codeに共有

- [ ] IDが揃ったら「タグIDを設定して」と依頼 → sync → push で完了

### 【STEP 2】カスタムドメインの設定
> agencia-cleaning.com でLPを公開する

- [ ] ドメイン `agencia-cleaning.com` を取得（お名前.com / ムームードメインなど、年2,000円前後）
- [ ] ドメイン会社のDNS設定にAレコードを4つ追加
  ```
  185.199.108.153
  185.199.109.153
  185.199.110.153
  185.199.111.153
  ```
- [ ] GitHubリポジトリ Settings → Pages → Custom domain に `agencia-cleaning.com` を入力
- [ ] 「CNAMEを戻してpushして」と依頼 → 完了

### 【STEP 3】広告キャンペーン作成
> タグとドメインが揃ったら出稿スタート

- [ ] Google検索広告キャンペーン作成（キーワード・広告文・予算設定）
- [ ] Yahoo!検索広告キャンペーン作成

---

## ✅ 完了済み

- [x] LP (index.html) 設計・実装・レスポンシブ対応
- [x] 画像20枚設置（ロゴ・ヒーロー・サービス・ビフォーアフター）
- [x] 電話タップ発信対応
- [x] お問い合わせフォーム実装
- [x] フォーム送信メールの日本語化（Formspree）
- [x] フォーム動作テスト済み（メール受信確認済み）
- [x] 広告タグのコード設置（GA4・Google広告・Yahoo!広告 ※IDは未設定）
- [x] GitHubリポジトリ作成・push済み
- [x] GitHub Pages で公開済み → https://lastsamurai-agencia.github.io/agencia_lp1/
- [x] sync.py / sync.sh：Claude Designとの同期スクリプト作成
- [x] Claude Designの修正を随時反映する仕組み構築

---

## 📝 次回Claude Codeを開いたら

「TASKS.md を確認して、次回やることから再開して」と言えばすぐ続きから始められます。

---

## ⏭️ 次回やること（ここから再開）

### 【次回 STEP 1】広告タグのID設定
> 広告アカウントを作成してIDを取得し、Claude Codeに貼り付けるだけでOK

1. **GA4（Googleアナリティクス）のアカウント作成**
   - [analytics.google.com](https://analytics.google.com) でプロパティ作成
   - 測定ID（`G-XXXXXXXXXX`）を取得 → Claude Codeに共有
   - ※ Googleアカウントがあればすぐ作れる

2. **Google広告のアカウント作成**
   - [ads.google.com](https://ads.google.com) でアカウント作成
   - コンバージョン「フォーム送信」「電話クリック」を設定
   - コンバージョンID・ラベルを取得 → Claude Codeに共有

3. **Yahoo!広告のアカウント作成**
   - [marketing.yahoo.co.jp](https://marketing.yahoo.co.jp) でアカウント作成（法人番号が必要）
   - コンバージョン設定 → IDを取得 → Claude Codeに共有

4. **IDが揃ったら Claude Code で「タグIDを設定して」と依頼**
   - sync.py に自動反映 → 「同期して」でindex.htmlに反映

### 【次回 STEP 2】フォームの送信先メールを設定
> 現状はフォーム送信しても実際にはどこにも届かない。公開前に必須。

- [formspree.io](https://formspree.io) で無料登録（月50件まで無料）
- 受け取りたいメールアドレスを登録 → フォームID（例：`xpzvgkqw`）を取得
- Claude Codeに「フォームのメール設定して、IDは〇〇」と依頼 → 即反映

### 【次回 STEP 3】GitHubにpush（ファイルをアップロード）
> pushとは：このリポジトリのファイルをGitHubのサーバーに送ること
> タグ・フォーム設定が終わってから実施する

- GitHubアカウントのPersonal Access Token（PAT）を発行
  - [github.com/settings/tokens/new](https://github.com/settings/tokens/new)
  - Scope: `repo` にチェック → トークンをClaude Codeに共有
- push先: `https://github.com/lastsamurai-agencia/agencia_lp1.git`

### 【次回 STEP 3】GitHub Pagesで公開
- リポジトリ設定 → Pages → Branch: main を選択
- Custom domain に `agencia-cleaning.com` を入力
- ドメイン会社のDNS設定（Aレコード4つを追加）
  ```
  185.199.108.153
  185.199.109.153
  185.199.110.153
  185.199.111.153
  ```
- `https://agencia-cleaning.com` で表示確認

---

## ✅ 完了

### LP制作
- [x] LP (index.html) 設計・実装
- [x] レスポンシブ対応（PC / タブレット / スマホ）
- [x] 電話番号タップ発信対応（`tel:` リンク）
- [x] ヒーロー背景画像 (`hero-bg.jpg`) 設置
- [x] ロゴ画像 (`logo.png`) 設置
- [x] スタッフ写真 (`hero.jpg`) 設置
- [x] サービス画像 8枚 (`service-01.jpg` 〜 `service-08.jpg`) 設置
- [x] ビフォーアフター画像 8枚 (`before/after-01〜04.jpg`) 設置
- [x] お問い合わせフォーム実装
- [x] フッターにコーポレートサイトリンク追加

### 広告タグ（コード実装済み・IDは未設定）
- [x] Google Analytics 4 (GA4) タグ設置（プレースホルダー）
- [x] Google広告 コンバージョンタグ設置（プレースホルダー）
- [x] Yahoo!広告 サイトジェネラルタグ設置（プレースホルダー）
- [x] フォーム送信コンバージョンイベント実装
- [x] 電話クリックコンバージョンイベント実装

### 環境整備
- [x] sync.sh / sync.py：Claude Designとの同期スクリプト作成
- [x] CNAME：カスタムドメイン `agencia-cleaning.com` 設定ファイル作成
- [x] GitHubリポジトリ作成済み（push前）

---

## 🔲 タグID確定後にやること

### 広告キャンペーン作成（STEP 4）
- [ ] Google検索広告キャンペーン作成
  - キーワード設定（「オフィス 清掃 東京」など）
  - 広告文作成（3〜5パターン）
  - 入札戦略：「クリック数の最大化」でスタート
  - 予算設定（目安：月3〜5万円から）
- [ ] Yahoo!検索広告キャンペーン作成
- [ ] フォーム送信先をメール or CRMに接続

### 運用開始後（STEP 5）
- [ ] 2〜4週間後：コンバージョンデータを確認
- [ ] CV数が10件以上たまったら入札戦略を「目標CPA」に変更
- [ ] 効果の低いキーワードを停止・調整
- [ ] 広告文のA/Bテスト実施

---

## 📝 メモ

### index.html 内の差し替え箇所まとめ
| プレースホルダー | 意味 | 行番号付近 |
|---|---|---|
| `GA4_MEASUREMENT_ID` | GA4 測定ID | head内（3箇所） |
| `GADS_CONVERSION_ID` | Google広告 コンバージョンID | head + フォーム・電話 |
| `GADS_FORM_LABEL` | Google広告 フォームラベル | フォーム送信イベント |
| `GADS_PHONE_LABEL` | Google広告 電話ラベル | 電話クリックイベント |
| `YAHOO_CONVERSION_ID` | Yahoo!広告 コンバージョンID | head + フォーム・電話 |
| `YAHOO_FORM_LABEL` | Yahoo!広告 フォームラベル | フォーム送信イベント |
| `YAHOO_PHONE_LABEL` | Yahoo!広告 電話ラベル | 電話クリックイベント |

### 差し替えコマンド（IDが確定したら実行）
```bash
# 例：GA4 IDを差し替える場合
sed -i 's/GA4_MEASUREMENT_ID/G-XXXXXXXXXX/g' index.html

# 例：Google広告IDを差し替える場合
sed -i 's/GADS_CONVERSION_ID/AW-1234567890/g' index.html
```
