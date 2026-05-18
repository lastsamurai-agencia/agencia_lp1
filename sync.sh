#!/bin/bash
# project/index.html → index.html 同期スクリプト
# 広告タグ（GA4・Google広告・Yahoo!広告）を毎回自動で再挿入します
set -e
python3 sync.py && echo "✅ 同期完了: project/index.html → index.html（広告タグ再挿入済み）"
