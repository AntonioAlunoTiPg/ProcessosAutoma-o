import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

while True:
    pyautogui.screenshot(f'print_{time.time()}.png') #Nome único com timestamp
    time.sleep(3) #Pausa de 3 segundos
    

