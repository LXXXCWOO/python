import pyautogui
import pyperclip

pyautogui.write("Hello World!!!", interval=0.25)
pyautogui.press('enter')
pyautogui.write("***Hello World***", interval=0.25)
pyautogui.press('enter')
pyperclip.copy("안녕하세요!")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

pyautogui.keyDown('Ctrl')
pyautogui.press('z')
pyautogui.keyUp('Ctrl')

# pyautogui.press(['left', 'left', 'left'])
pyautogui.press('left', presses=5, interval=1)
# pyautogui.press('enter', presses=5, interval=3)
pyautogui.press('enter', interval=1)
pyautogui.press('right')
pyautogui.press('enter', interval=1)
pyautogui.press('right')
pyautogui.press('enter', interval=1)
pyautogui.press('right')
pyautogui.press('enter', interval=1)
pyautogui.press('right')
pyautogui.press('enter', interval=1)

pyautogui.hotkey('ctrl', 'a')
