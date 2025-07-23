import pyautogui
import time

pyautogui.size()

time.sleep(5)

pyautogui.position()

pyautogui.onScreen(1500, 800)

pyautogui.PAUSE = 2.5

pyautogui.FAILSAFE = True

pyautogui.moveTo(200, 200, duration=2)

pyautogui.dragTo(x=400, y=400, duration=2)

pyautogui.dragRel(100, 100, duration=2)

pyautogui.click(x=300, y=300, clicks=2, interval=0.25, button='left')
pyautogui.rightClick(x=200, y=200)
pyautogui.middleClick(x=250, y=250)
pyautogui.doubleClick(x=200, y=200)
pyautogui.tripleClick(x=200, y=200)

pyautogui.scroll(500, x=200, y=200)
pyautogui.mouseDown(x=200, y=200, button='left')
pyautogui.mouseUp(x=200, y=200, button='left')

pyautogui.typewrite('Hello world!\n', interval=0.5)

pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=0.2)

pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')
pyautogui.keyDown('shift')
pyautogui.keyUp('shift')

pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=0.2)

pyautogui.alert('This displays some text with an OK button.')
pyautogui.confirm('This displays text and has an OK and Cancel button.')
pyautogui.prompt('This lets the user type in a string and press OK.')

resposta = pyautogui.confirm('Para tirar um print da tela clique  OK ou Cancele.')

if resposta == "OK":
    pyautogui.screenshot('exemplo.png')
