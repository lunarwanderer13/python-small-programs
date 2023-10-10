import pyautogui as pag
import random
import time

while True:
    x = random.randint(300,700)
    y = random.randint(200,800)
    pag.moveTo(x,y,0.5)
    print(f'Moved mouse cursor to {x} - {y}')
    time.sleep(10)