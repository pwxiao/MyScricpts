import pyautogui
import time
time.sleep(5)

while True:

    x, y = pyautogui.position()

    pyautogui.click(x=x, y=y, button='left')

    time.sleep(100)