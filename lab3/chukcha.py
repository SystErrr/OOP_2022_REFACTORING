import math

import pygame
from pygame.draw import *


def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center=target_rect.center))


pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))
screen.fill((206, 206, 206))

# ground
white = (255, 255, 255)
rect(screen, white, (0, 400, 800, 800))

# iglu
gray = (220, 220, 220)
circle(screen, gray, (300, 500), 150, draw_top_left=True, draw_top_right=True)
circle(screen, (0, 0, 0), (300, 500), 150, 2, draw_top_left=True, draw_top_right=True)
arc(screen, (0, 0, 0), (225, 350, 150, 40), math.pi, 0)
arc(screen, (0, 0, 0), (175, 400, 250, 40), math.pi, 0)
arc(screen, (0, 0, 0), (155, 450, 290, 40), math.pi, 0)
line(screen, (0, 0, 0), (250, 385), (230, 435))
line(screen, (0, 0, 0), (300, 350), (300, 390))
line(screen, (0, 0, 0), (350, 385), (380, 435))
line(screen, (0, 0, 0), (265, 440), (250, 487))
line(screen, (0, 0, 0), (205, 432), (185, 480))
line(screen, (0, 0, 0), (400, 432), (420, 480))
line(screen, (0, 0, 0), (335, 440), (350, 487))
line(screen, (0, 0, 0), (150, 500), (450, 500))

x = 70
y = 510
# cat
ellipse(screen, gray, (200, 600, 200, 50))
# fish
draw_ellipse_angle(screen, (142, 190, 179), (x + 100, y + 100, 50, 10), -20)
circle(screen, "black", (x + 110, y + 100), 1)
polygon(screen, (142, 190, 179), [(x + 150, y+ 113), (x + 160, y + 108), (x+155, y+120)])
# cat
ellipse(screen, gray, (178, 575, 50, 40))
polygon(screen, white, [(x+115, y+97), (x+120, y+97), (x+117, y+102)])
polygon(screen, white, [(x+130, y+100), (x+135, y+100), (x+132, y+105)])

draw_ellipse_angle(screen, gray, (380, 580, 100, 25), 45)
draw_ellipse_angle(screen, gray, (200, 610, 25, 100), 135)
draw_ellipse_angle(screen, gray, (235, 610, 25, 100), 135)
draw_ellipse_angle(screen, gray, (335, 610, 25, 100), 225)
draw_ellipse_angle(screen, gray, (370, 610, 25, 100), 225)
polygon(screen, gray, [(220, 590), (215, 580), (225, 570)])
polygon(screen, gray, [(190, 590), (180, 590), (175, 570)])
circle(screen, white, (190, 590), 5)
circle(screen, white, (210, 590), 5)
circle(screen, (0, 0, 0), (212, 590), 2)
circle(screen, (0, 0, 0), (192, 590), 2)
circle(screen, (0, 0, 0), (192, 600), 2)


# chukcha
brown = (165, 126, 103)
dbrown = (93, 71, 57)
ellipse(screen, gray, (530, 450, 140, 70))
circle(screen, brown, (600, 600), 100, draw_top_left=True, draw_top_right=True)
ellipse(screen, brown, (540, 600, 40, 50))
ellipse(screen, brown, (620, 600, 40, 50))
ellipse(screen, brown, (520, 630, 50, 25))
ellipse(screen, brown, (630, 630, 50, 25))
rect(screen, dbrown, (500, 600, 200, 25))
rect(screen, dbrown, (575, 500, 50, 100))
ellipse(screen, brown, (550, 455, 100, 55))
ellipse(screen, gray, (560, 460, 80, 45))
line(screen, 'black', (570, 475), (580, 480))
line(screen, 'black', (630, 475), (620, 480))
arc(screen, 'black', (575, 485, 50, 10), 0, math.pi)
ellipse(screen, brown, (470, 520, 80, 25))
draw_ellipse_angle(screen, brown, (650, 520, 80, 25), 30)
line(screen, 'black', (480, 450), (490, 650))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
