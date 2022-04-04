import pygame
from pygame.draw import *


def smile():
    screen = pygame.display.set_mode((400, 400))
    screen.fill((206, 206, 206))
    x1 = 100
    y1 = 250
    x2 = 300
    y2 = 300
    # face
    circle(screen, (255, 199, 30), (200, 200), 150)
    # eyes
    circle(screen, (255, 0, 0), (125, 150), 30)
    circle(screen, (0, 0, 0), (125, 150), 15)

    circle(screen, (255, 0, 0), (275, 150), 20, )
    circle(screen, (0, 0, 0), (275, 150), 15)
    # mouth
    rect(screen, (0, 0, 0), (x1, y1, x2 - x1, y2 - y1))
    # brows
    polygon(screen, (0, 0, 0), [(40, 45), (30, 70), (170, 145), (180, 125)])
    polygon(screen, (0, 0, 0), [(360, 55), (370, 80), (230, 155), (220, 135)])
