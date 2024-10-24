import time
import pyautogui as pg
pg.FAILSAFE = True
time.sleep(5)
for i in range(1000):
    pg.write('Sorry ')
    pg.press('enter')