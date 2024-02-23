import webbrowser, pyautogui
from time import sleep

webbrowser.open('https://www.tiktok.com/')
sleep(10)

pyautogui.click(1746,171,duration=2)
sleep(5)
pyautogui.click(983,579,duration=2)
sleep(5)
pyautogui.click(865,768,duration=2)
sleep(5)
pyautogui.click(1272,945,duration=2)
sleep(5)
pyautogui.click(1106,778,duration=2)
sleep(5)
pyautogui.click(1106,894,duration=2)

webbrowser.open('https://www.tiktok.com/@alesapellegrino')
pyautogui.click(478,788,duration=2)
sleep(5)

for video in range(6):
    imagem = pyautogui.locateOnScreen('curtida.png')
if imagem:
    pyautogui.press('down')
    sleep(5)
else:
    sleep(5)
    pyautogui.click(1294,409,duration=2)
    pyautogui.press('down')
