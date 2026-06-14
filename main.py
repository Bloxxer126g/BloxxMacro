import webview
import pyautogui

class Api():
  def ExecuteActions(self, actions):
    for item in actions:
        if item[0] == "(":
            item = item.split(",")
            loc1 = item[0].split("(")[1]
            loc2 = item[1].split(")")[0]
            loc1=int(loc1)
            loc2=int(loc2)
            pyautogui.moveTo(loc1,loc2)
            pyautogui.click(loc1,loc2)
        else:
           pyautogui.typewrite(item)

      
      


webview.create_window("BloxxMacro", "https://macro.bloxxer.dev/app", js_api=Api())
webview.start()