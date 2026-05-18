# 株式会社AGENCIA Google・Yahoo広告 LP タスク管理

最終更新: 2026-05-18

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

### 広告タグ
- [x] Google Analytics 4 (GA4) タグ設置（プレースホルダー）
- [x] Google広告 コンバージョンタグ設置（プレースホルダー）
- [x] Yahoo!広告 サイトジェネラルタグ設置（プレースホルダー）
- [x] フォーム送信コンバージョンイベント実装
- [x] 電話クリックコンバージョンイベント実装

---

## 🔲 未完了

### STEP 1：LP公開（優先度：高）
- [ ] ホスティングサービスを選定・契約（Xserver / Netlify / さくら など）
- [ ] 独自ドメインを取得（例：`agencia-cleaning.jp`）
- [ ] `index.html` と `project/` フォルダをサーバーにアップロード
- [ ] ブラウザで表示・動作確認（PC・スマホ両方）
- [ ] フォーム送信先を接続（メール or お問い合わせシステム）

### STEP 2：GA4セットアップ（優先度：高）
- [ ] Google Analytics 4 のプロパティ作成
- [ ] 測定ID（`G-XXXXXXXXXX`）を取得
- [ ] `index.html` の `GA4_MEASUREMENT_ID` を実際のIDに差し替え（3箇所）
- [ ] GA4 リアルタイムレポートで計測確認

### STEP 3：Google広告セットアップ（優先度：高）
- [ ] Google広告アカウント作成（[ads.google.com](https://ads.google.com)）
- [ ] コンバージョン「フォーム送信」を作成 → ラベル取得
- [ ] コンバージョン「電話クリック」を作成 → ラベル取得
- [ ] `index.html` の以下を実際の値に差し替え
  - `GADS_CONVERSION_ID`（例：`AW-1234567890`）
  - `GADS_FORM_LABEL`
  - `GADS_PHONE_LABEL`
- [ ] 検索キャンペーン作成
  - キーワード設定（「オフィス 清掃 東京」など）
  - 広告文作成（3〜5パターン）
  - 入札戦略：「クリック数の最大化」でスタート
  - 予算設定（目安：月3〜5万円からスタート）
- [ ] コンバージョン計測が正常に動作するか確認

### STEP 4：Yahoo!広告セットアップ（優先度：中）
- [ ] Yahoo! JAPAN Business Centerでビジネスアカウント作成
- [ ] Yahoo!広告アカウント作成（[marketing.yahoo.co.jp](https://marketing.yahoo.co.jp)）
- [ ] コンバージョン「フォーム送信」「電話クリック」を作成
- [ ] `index.html` の以下を実際の値に差し替え
  - `YAHOO_CONVERSION_ID`
  - `YAHOO_FORM_LABEL`
  - `YAHOO_PHONE_LABEL`
- [ ] 検索キャンペーン作成
- [ ] コンバージョン計測が正常に動作するか確認

### STEP 5：運用開始後（優先度：低）
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
