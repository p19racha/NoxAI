import os
import webbrowser
import subprocess
import datetime
import pyautogui

def run_command(action_json: dict):
    try:
        action = action_json.get("action")

        if action == "launch_app":
            os.system(f"start {action_json['app']}")
            return f"Launching {action_json['app']}."

        elif action == "open_url":
            webbrowser.open(action_json["url"])
            return f"Opening {action_json['url']}."

        elif action == "get_time":
            return "The time is " + datetime.datetime.now().strftime("%I:%M %p")

        elif action == "screenshot":
            filepath = os.path.expanduser("~/Desktop/nox_screenshot.png")
            screenshot = pyautogui.screenshot()
            screenshot.save(filepath)
            return "Screenshot saved to Desktop."

        elif action == "shutdown":
            os.system("shutdown /s /t 1")
            return "Shutting down the system."

        elif action == "restart":
            os.system("shutdown /r /t 1")
            return "Restarting the system."

        elif action == "sleep":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            return "Putting the system to sleep."

        else:
            return None

    except Exception as e:
        return f"⚠️ Error running system command: {e}"
