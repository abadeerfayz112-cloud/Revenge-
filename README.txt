# REVENGE — Android Build Package

## الطريقة 1: PWA (أسهل — 5 دقائق)
1. انقل المجلد لـ server (أو GitHub Pages)
2. افتح الرابط في Chrome على Android
3. ⋮ → "Add to Home screen"
4. هتشتغل Full-Screen زي التطبيقات

## الطريقة 2: APK بـ Buildozer (يحتاج Linux)
1. ثبّت Buildozer:
   pip install buildozer
   buildozer init
2. انسخ buildozer.spec للمجلد
3. انسخ main.py للمجلد
4. شغّل:
   buildozer android debug
5. APK هيطلع في: bin/revenge-0.9.2-arm64-v8a_armeabi-v7a-debug.apk

## الطريقة 3: Android Studio (WebView APK)
1. افتح Android Studio → New Project → Empty Activity
2. في activity_main.xml ضع WebView
3. في MainActivity.kt:
   webView.loadUrl("file:///android_asset/index.html")
4. ضع index.html في app/src/main/assets/
5. Build → Build APK
