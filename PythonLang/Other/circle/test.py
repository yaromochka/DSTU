import pyautogui as pa
import math


pa.PAUSE = 0.000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
# 1336, 667 682, 384 682 382
def draw_circle(x, y, radius):
    i = 0
    sectors = 11000
    i = i + math.pi / sectors
    xm = x + math.sin(i) * radius
    ym = y + math.cos(i) * radius
    pa.moveTo(xm, ym)
    pa.mouseDown(button='left')
    for j in range(0, 28000):
        i = i + math.pi / sectors
        xm = x + math.sin(i) * radius
        ym = y + math.cos(i) * radius
        pa.moveTo(xm, ym, _pause=False)


cx, cy = 1365/2, 771/2
pa.moveTo(cx, cy)
draw_circle(cx, cy, 307)