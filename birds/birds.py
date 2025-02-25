import pyautogui as pg
from time import sleep

pg.press("win")
pg.write("cmd", interval=0.4)
pg.press('Enter')
sleep(3)

pg.write('chrome')
pg.press('Enter')

sleep(3)
pg.write("cats", interval=0.03)
pg.press('Enter')



with open("", "a") as file:
    file.write(f"{input('Отзыв: ')}")
