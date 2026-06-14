import webview
import pyautogui

class Api():
  def ExecuteActions(self, actions):
    for item in actions:
        if item[0] == "(":
            item = item.split(",")
            print(item)
        else:
           pyautogui.typewrite(item)

      
      


webview.create_window("BloxxMacro", "https://macro.bloxxer.dev/app", js_api=Api())
webview.start()