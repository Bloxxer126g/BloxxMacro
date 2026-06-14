import webview

class Api():
  def log(self, value):
    print(value)

webview.create_window("BloxxMacro", "https://macro.bloxxer.dev/app", js_api=Api())
webview.start()