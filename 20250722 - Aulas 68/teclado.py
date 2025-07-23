import pyautogui
from time import sleep
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.press('winleft') # Abre o menu Iniciar
sleep(1)
pyautogui.write('calculadora') # Digita "calculadora"
sleep(1)
pyautogui.press('enter') # Abre a calculadora