import pygame


pygame.init()

FPS = 300
clock = pygame.time.Clock()



W = 800
H = 600
sc = pygame.display.set_mode((W, H))
sc.fill((255, 255, 255))

P = 200
n = 1.5
scale = P / n
n_iter = 100

for y in range(-P, P):
    for x in range(-P, P):
        a = x / scale
        b = y / scale
        c = complex(a, b)
        z = complex(0)
        for n in range(n_iter):
            z = z**2 + c
            if abs(z) > 2:
                break
        else:
            pygame.draw.circle(sc, (0, 0, 0), (x + P, y + P), 2)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()
    clock.tick(FPS)

