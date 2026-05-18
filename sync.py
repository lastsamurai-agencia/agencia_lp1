"""
project/index.html を index.html に同期するスクリプト。
- 画像パスを project/images/ に変換
- 広告計測タグ（GA4・Google広告・Yahoo!広告）を自動挿入
- IDが確定したら下記 CONFIG の値を書き換えるだけでOK
"""

# ============================================================
# 広告ID設定（確定したらここを書き換える）
# ============================================================
CONFIG = {
    "GA4_MEASUREMENT_ID":   "GA4_MEASUREMENT_ID",    # 例: G-XXXXXXXXXX
    "GADS_CONVERSION_ID":   "GADS_CONVERSION_ID",    # 例: AW-1234567890
    "GADS_FORM_LABEL":      "GADS_FORM_LABEL",       # Google広告フォームラベル
    "GADS_PHONE_LABEL":     "GADS_PHONE_LABEL",      # Google広告電話ラベル
    "YAHOO_CONVERSION_ID":  "YAHOO_CONVERSION_ID",   # 例: 1000012345
    "YAHOO_FORM_LABEL":     "YAHOO_FORM_LABEL",      # Yahoo!広告フォームラベル
    "YAHOO_PHONE_LABEL":    "YAHOO_PHONE_LABEL",     # Yahoo!広告電話ラベル
}

HEAD_TAGS = """\
<!-- ============================================================
     計測タグ（GA4 / Google広告 / Yahoo!広告）
     IDが確定したら sync.py の CONFIG セクションを書き換えてください
     ============================================================ -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_MEASUREMENT_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA4_MEASUREMENT_ID}');
  gtag('config', '{GADS_CONVERSION_ID}');
</script>
<!-- Yahoo!広告 サイトジェネラルタグ -->
<script>
  window.yjDataLayer = window.yjDataLayer || [];
  function ytag(){{yjDataLayer.push(arguments);}}
  ytag('config', {{ 'ycid': '{YAHOO_CONVERSION_ID}' }});
</script>
<script async src="https://s.yimg.jp/images/listing/tool/cv/ytag.js"></script>
""".format(**CONFIG)

FORM_SCRIPT = """\
<!-- フォーム送信・電話クリック計測 -->
<script>
  document.getElementById('contactForm').addEventListener('submit', function(e){{
    e.preventDefault();
    const msg = document.getElementById('successMsg');
    msg.classList.add('show');
    this.reset();
    const y = msg.getBoundingClientRect().top + window.scrollY - 120;
    window.scrollTo({{ top: y, behavior: 'smooth' }});

    if (typeof gtag !== 'undefined') {{
      gtag('event', 'generate_lead', {{ event_category: 'form', event_label: 'contact_form' }});
      gtag('event', 'conversion', {{ send_to: '{GADS_CONVERSION_ID}/{GADS_FORM_LABEL}' }});
    }}
    if (typeof ytag !== 'undefined') {{
      ytag('event', 'yss_conversion', {{ 'ycid': '{YAHOO_CONVERSION_ID}', 'label': '{YAHOO_FORM_LABEL}' }});
    }}
  }});

  document.querySelectorAll('a[href="tel:0365551607"]').forEach(function(el) {{
    el.addEventListener('click', function() {{
      if (typeof gtag !== 'undefined') {{
        gtag('event', 'call_click', {{ event_category: 'phone', event_label: '0365551607' }});
        gtag('event', 'conversion', {{ send_to: '{GADS_CONVERSION_ID}/{GADS_PHONE_LABEL}' }});
      }}
      if (typeof ytag !== 'undefined') {{
        ytag('event', 'yss_conversion', {{ 'ycid': '{YAHOO_CONVERSION_ID}', 'label': '{YAHOO_PHONE_LABEL}' }});
      }}
    }});
  }});
</script>
""".format(**CONFIG)

# ============================================================

import re

with open("project/index.html", encoding="utf-8") as f:
    html = f.read()

# 1. パス変換
html = html.replace('data-img="images/', 'data-img="project/images/')
html = html.replace('data-bg="images/', 'data-bg="project/images/')
html = html.replace('src="tweaks-panel.jsx"', 'src="project/tweaks-panel.jsx"')
# ロゴのフォールバック（カンマ区切り2番目）
html = html.replace(
    'project/images/logo.svg,images/logo.png',
    'project/images/logo.svg,project/images/logo.png'
)

# 2. headタグ挿入（フォント読み込みの直前）
html = html.replace(
    '<link rel="preconnect" href="https://fonts.googleapis.com">',
    HEAD_TAGS + '<link rel="preconnect" href="https://fonts.googleapis.com">'
)

# 3. フォームスクリプト挿入＆既存のシンプルハンドラを置換
simple_handler = re.search(
    r'<!-- Simple form handler -->.*?</script>',
    html, re.DOTALL
)
if simple_handler:
    html = html[:simple_handler.start()] + FORM_SCRIPT + html[simple_handler.end():]
else:
    # Simple form handler が見つからない場合は </body> 直前に挿入
    html = html.replace('</body>', FORM_SCRIPT + '</body>')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
