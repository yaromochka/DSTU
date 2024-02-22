import pygame as pg
import numpy as np
import Neural_Network as net
pg.font.init()

Hight, Size = 780, 600
display = pg.display.set_mode((Hight, Size))
font = pg.font.Font(None, 34)
font1 = pg.font.Font(None, 36)
array = np.zeros(10)
grid = np.zeros((28, 28))


# Отрисовка сетки
def draw_grid():
    for x in range(29):
        for y in range(29):
            pg.draw.line(display, 'black', (x * 20 + 10, 20), (x * 20 + 10, 560 + 20), 1)
            pg.draw.line(display, 'black', (10, y * 20 + 20), (570, y * 20 + 20), 1)

    pg.draw.rect(display, 'black', ((610, 420),(150, 50)))
    pg.draw.rect(display, 'black', ((610, 500), (150, 50)))

    text = font1.render('Очистить', True, 'white')
    display.blit(text, (627, 435))

    text = font1.render('Распознать', True, 'white')
    display.blit(text, (615, 515))

# Отрисовка поля
def draw_data():
    for x in range(28):
        for y in range(28):
            rect = pg.Rect((x * 20 + 10, y * 20 + 20), (20, 20))
            if grid[x][y] == 1:
                pg.draw.rect(display, 'black', rect, 10)

# Отрисовка
def draw_object():
    for x in range(10):
        rect = pg.Rect((630, x * 35 + 30), (140, 20))
        pg.draw.rect(display, 'black', rect, 1)

        text = font.render(f'{x}', True, 'black')
        display.blit(text, (600, x * 35 + 30))

# три=
def draw_progress():
    for i in range(len(array)):
        rect = pg.Rect((631, i * 35 + 31), (array[i] * 145, 18))
        if array[i]>0.6:
            pg.draw.rect(display, 'green', rect, 20)
        else:
            pg.draw.rect(display, 'black', rect, 20)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                if 610 < x < 760 and 420 < y < 470:
                    grid = np.zeros((28, 28), dtype=np.int8)

                if 610 < x < 760 and 500 < y < 550:
                    array = net.n_net.result(net.n_net, grid)[0]

    clock = pg.time.Clock()
    pg.display.set_caption(str(clock.get_fps()))

    display.fill('white')
    draw_grid()
    draw_object()
    draw_progress()
    draw_data()
    # array = net.n_net.result(net.n_net, grid)[0]
    pressed = pg.mouse.get_pressed()
    pos = pg.mouse.get_pos()
    if pressed[0]:
        x, y = pos
        x1, y1 = (pos[0] - 10) // 20, (pos[1] - 20) // 20
        if x1 < 28 and y1 < 28:
            grid[x1][y1] = 1
        #array = net.n_net.result(net.n_net, grid)[0]
        pg.display.update()



    if pressed[2]:
        x1, y1 = (pos[0] - 10) // 20, (pos[1] - 20) // 20
        if x1 < 28 and y1 < 28:
            grid[x1][y1] = 0
        pg.display.update()

    pg.display.flip()
