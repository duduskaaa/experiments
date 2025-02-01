import pyautogui as pg
from time import sleep

pg.press("win")
pg.write("cmd", interval=0.4)
pg.press('Enter')
sleep(3)

pg.write('python')
pg.press('Enter')

pg.write("from functools import reduce", interval=0.03)
pg.press('Enter')

pg.write("array = [i for i in range(1, 10)]", interval=0.03)
pg.press('Enter')

pg.write("fact = reduce(lambda x, y: x*y, array)", interval=0.03)
pg.press('Enter')

pg.write("fact", interval=0.03)
pg.press('Enter')

pg.write("We found factorial of 9. Nahuya? Idi nahui", interval=1)
pg.press('Enter')

