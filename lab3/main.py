from smile import *
from chukcha import *
from chukcha2 import *

pygame.init()
FPS = 30

funcs = [smile, chukcha, chukcha2]

for i in range(3):
    funcs[i]()
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

pygame.quit()
