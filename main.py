import webview
import pyautogui
from pynput import mouse 

class Api():
    def ExecuteActions(self, actions):
        pyautogui.alert("Running Macro", "BloxxMacro")
        for item in actions:
            if item.startswith("("):
                try:
                    coords = item.replace("(", "").replace(")", "").split(",")
                    loc1 = int(coords[0].strip())
                    loc2 = int(coords[1].strip())
                    pyautogui.moveTo(loc1, loc2, 1, pyautogui.easeOutQuad)
                    pyautogui.click(loc1, loc2)
                except Exception as e:
                    print(f"Error parsing coordinates: {e}")
            else:
                pyautogui.press(item)

    def GetClickLocation(self):
        clicked_coords = []
        
        def on_click(x, y, button, pressed):
            if pressed:
                clicked_coords.append((int(x), int(y)))
                return False

        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
            
        if clicked_coords:
            return f"({clicked_coords[0][0]},{clicked_coords[0][1]})"
        return None

webview.create_window("BloxxMacro", "index.html", js_api=Api(), width=600, height=500)
webview.start()