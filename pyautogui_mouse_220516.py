import time
import pyautogui

# 화면 사이즈 표시
size = pyautogui.size()
print(size)

time.sleep(2)
print(pyautogui.position())

# XENICS STORMX VM3 아이콘 실행 후 Close
pyautogui.moveTo(960, 150)
pyautogui.moveTo(140, 500, duration=1.5)
pyautogui.doubleClick()

pyautogui.moveTo(1430, 1050, duration=2)
pyautogui.click()

pyautogui.moveTo(1320, 230, duration=2)
pyautogui.click()

pyautogui.moveTo(816, 81, 2)
pyautogui.dragTo(539, 80, 2)
