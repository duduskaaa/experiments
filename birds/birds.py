import pyautogui as pg
from time import sleep

pg.press("win+r")
pg.write("chrome", interval=0.4)
pg.press('Enter')
sleep(3)

pg.write('cats')
pg.press('Enter')

with open("logs.txt", "a") as file:
    file.write(f"{input('Отзыв: ')}")
