# AGENCIA LP プロジェクト — チーム共有ノート

このファイルはClaudeチーム全員が読み書きする共有ノートです。
作業前に必ず読み、作業後は必ず更新してください。

---

## 組織構成

| 役割 | 担当 | 主な業務 |
|------|------|---------|
| PM・LP開発 | moriyakengo の Claude | LP修正・デプロイ・Yahoo!広告・計測タグ管理 |
| Google広告運用 | コワークの Claude | Google Adsキャンペーン・キーワード・広告文 |

---

## プロジェクト概要

- **サービス名**: 株式会社AGENCIA（ビル・オフィス清掃）
- **LP URL**: https://agencia-cleaning.jp
- **リポジトリ**: https://github.com/lastsamurai-agencia/agencia_lp1
- **LP ファイル**: `/Users/moriyakengo/agencia_lp1/index.html`
- **ホスティング**: GitHub Pages（カスタムドメイン）

---

## 技術スタック

- HTML/CSS/JS（フレームワークなし・単一ファイル構成）
- フォーム: Formspree
- ホスティング: GitHub Pages
- ドメイン: お名前.com（ネームサーバー: 01.dnsv.jp / 02.dnsv.jp）

---

## 計測・タグ

| ツール | ID / ラベル | 状態 |
|--------|------------|------|
| GA4 | G-K9T55BDPQL | ✅ 設置済み |
| Google Ads | AW-18178310779 | ✅ 設置済み |
| コンバージョン：フォーム送信 | AW-18178310779/E4NFCMKO9LAcEPuEjNxD | ✅ 設置済み |
| コンバージョン：電話ボタン | AW-18178310779/2MJICMSB9rAcEPuEjNxD | ✅ 設置済み |
| Google Search Console | BUbkQ_JVz8LLDvUoCs34WHh9v77vRYic_cjGle0XCIY | ✅ 設置済み |
| Yahoo!広告 | 未設定 | 🔲 対応予定 |

---

## 完了済み作業

- [x] LP制作・GitHub Pagesデプロイ
- [x] カスタムドメイン設定（agencia-cleaning.jp）
- [x] DNS設定（お名前.com → 01.dnsv.jp）
- [x] GA4タグ設置
- [x] Google Adsグローバルタグ設置
- [x] コンバージョン設定（フォーム送信・電話ボタン）
- [x] Google Search Console所有権確認
- [x] ファビコン設置
- [x] お客様の声セクションにアバター画像設置（4枚）
- [x] レスポンシブ対応（概念セクション・時間セクション）
- [ ] HTTPS有効化（GitHub Pages「Enforce HTTPS」）← TLS証明書待ち
- [ ] Yahoo!広告アカウント設定・タグ設置
- [ ] Google Search Console 再インデックスリクエスト

---

## Google Ads 状況（コワーク担当）

> ⚠️ コワーク担当のClaudeが作業したら、ここに追記してください

- キャンペーン名：
- 配信開始日：
- ターゲットキーワード：
- 広告文（見出し）：
- 広告文（説明文）：
- 入札戦略：
- 月間予算：

---

## Yahoo!広告 状況（moriyakengo担当）

- アカウント：未作成
- タグ：未設置

---

## 重要ルール

1. **お名前.comでDNSレコードを追加する際は必ずネームサーバーを `01.dnsv.jp` に変更すること**（デフォルトの `dns01.onamae.com` では機能しない）
2. GitHubトークン・APIキー等の機密情報はこのファイルに書かない
3. 作業完了したらチェックボックスを更新する
