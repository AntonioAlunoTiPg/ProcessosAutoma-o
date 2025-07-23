import pyautogui
from time import sleep

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

sleep(5)

with open('alunos.txt', 'r', encoding='utf-8') as file:
    for line in file:
        aluno, email = line.strip().split(',')
        # Clica e preenche o campo Name (1417, 714)
        pyautogui.click(299, 369, duration=1)
        sleep(1)
        pyautogui.write(aluno)

        # Clica e preenche o campo Email (1423, 770)
        pyautogui.click(299, 412, duration=1)
        sleep(1)
        pyautogui.write(email)
        # Clica no botão Add (415, 452)
        pyautogui.click(362, 433, duration=0.5)
        # Tira screenshot para auditoria
        pyautogui.screenshot(f'aluno_{aluno}.png')
        sleep(1)