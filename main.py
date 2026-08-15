from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from jnius import autoclass
import os

class RevengeApp(App):
    def build(self):
        Window.clearcolor = (0.03, 0.03, 0.05, 1)
        layout = BoxLayout()
        # Load local HTML
        webview = autoclass('android.webkit.WebView')
        activity = autoclass('org.kivy.android.PythonActivity').mActivity
        wv = webview(activity)
        wv.getSettings().setJavaScriptEnabled(True)
        wv.getSettings().setDomStorageEnabled(True)
        wv.setBackgroundColor(0x08080d)
        # Load from assets
        wv.loadUrl('file:///android_asset/www/index.html')
        layout.add_widget(wv)
        return layout

if __name__ == '__main__':
    RevengeApp().run()
