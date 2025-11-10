import pyautogui
import time

file_path = "source.txt"

delay = 7

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

print(f"Typing will start in {delay} seconds... Move your cursor where needed.")
time.sleep(delay)

pyautogui.typewrite(content, interval=0.01)
