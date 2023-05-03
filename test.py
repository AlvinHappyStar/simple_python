import pyautogui
import time

image_path_1 = "1.png"
image_path_2 = "2.png"
image_path_3 = "3.png"
image_path_4 = "4.png"
image_path_5 = "5.png"

for match in pyautogui.locateAllOnScreen(image_path_1):
    x, y = pyautogui.center(match)
    pyautogui.moveTo(x, y)
pyautogui.click(x,y)

time.sleep(3)


for match in pyautogui.locateAllOnScreen(image_path_2):
    x, y = pyautogui.center(match)
    pyautogui.moveTo(x, y)
pyautogui.click(x,y)

time.sleep(3)

for match in pyautogui.locateAllOnScreen(image_path_3):
    x, y = pyautogui.center(match)
    pyautogui.moveTo(x, y)
pyautogui.click(x,y)

time.sleep(3)

for match in pyautogui.locateAllOnScreen(image_path_3):
    x, y = pyautogui.center(match)
    pyautogui.moveTo(x, y)
pyautogui.click(x,y)

time.sleep(3)

for match in pyautogui.locateAllOnScreen(image_path_4):
    x, y = pyautogui.center(match)
    pyautogui.moveTo(x, y)
pyautogui.click(x,y)

time.sleep(3)

for match in pyautogui.locateAllOnScreen(image_path_5):
    x, y = pyautogui.center(match)
    pyautogui.moveTo(x, y)
pyautogui.click(x,y)

time.sleep(3)

