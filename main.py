import webview

class Api():
  def ExecuteActions(self, actions):
    for item in actions:
      print(item)
      


webview.create_window("BloxxMacro", "https://macro.bloxxer.dev/app", js_api=Api())
webview.start()