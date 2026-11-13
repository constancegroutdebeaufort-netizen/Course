"""Construit docs/index.html (version GitHub Pages) à partir de index.html (version artifact Claude)."""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
body = (root / "index.html").read_text(encoding="utf-8")
head = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#0A0E13">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Sub 50">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<link rel="icon" href="icon-192.png">
<link rel="manifest" href="manifest.webmanifest">
<style>*{box-sizing:border-box}:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;-webkit-text-size-adjust:100%}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
"""
(root / "docs" / "index.html").write_text(head + body + "\n</body>\n</html>\n", encoding="utf-8")
(root / "docs" / "manifest.webmanifest").write_text("""{
  "name": "Objectif 49'59",
  "short_name": "Sub 50",
  "lang": "fr",
  "start_url": "./",
  "scope": "./",
  "display": "standalone",
  "background_color": "#0A0E13",
  "theme_color": "#0A0E13",
  "icons": [
    {"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
    {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}
  ]
}
""", encoding="utf-8")
(root / "docs" / ".nojekyll").write_text("", encoding="utf-8")
print("docs/ à jour")
