import math

import pygame
from pygame.draw import *


def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center=target_rect.center))


def draw_iglu(x, y, scale):
    x *= scale
    y *= scale
    circle(screen, gray, (x + 300 * scale, y + 500 * scale), 150 * scale, draw_top_left=True, draw_top_right=True)
    circle(screen, (0, 0, 0), (x + 300 * scale, y + 500 * scale), 150 * scale, 2, draw_top_left=True,
           draw_top_right=True)
    arc(screen, (0, 0, 0), (x + 225 * scale, y + 350 * scale, 150 * scale, 40 * scale), math.pi, 0)
    arc(screen, (0, 0, 0), (x + 175 * scale, y + 400 * scale, 250 * scale, 40 * scale), math.pi, 0)
    arc(screen, (0, 0, 0), (x + 155 * scale, y + 450 * scale, 290 * scale, 40 * scale), math.pi, 0)
    line(screen, (0, 0, 0), (x + 250 * scale, y + 385 * scale), (x + 230 * scale, y + 435 * scale))
    line(screen, (0, 0, 0), (x + 300 * scale, y + 350 * scale), (x + 300 * scale, y + 390 * scale))
    line(screen, (0, 0, 0), (x + 350 * scale, y + 385 * scale), (x + 380 * scale, y + 435 * scale))
    line(screen, (0, 0, 0), (x + 265 * scale, y + 440 * scale), (x + 250 * scale, y + 487 * scale))
    line(screen, (0, 0, 0), (x + 205 * scale, y + 432 * scale), (x + 185 * scale, y + 480 * scale))
    line(screen, (0, 0, 0), (x + 400 * scale, y + 432 * scale), (x + 420 * scale, y + 480 * scale))
    line(screen, (0, 0, 0), (x + 335 * scale, y + 440 * scale), (x + 350 * scale, y + 487 * scale))
    line(screen, (0, 0, 0), (x + 150 * scale, y + 500 * scale), (x + 450 * scale, y + 500 * scale))


def draw_cat(x, y, scale):
    x *= scale
    y *= scale
    ellipse(screen, gray, (x + 200 * scale, y + 600 * scale, 200 * scale, 50 * scale))
    # fish
    draw_ellipse_angle(screen, (142, 190, 179), (x + 170 * scale, y + 610 * scale, 50 * scale, 10 * scale), -20)
    circle(screen, "black", (x + 180 * scale, y + 610 * scale), 1)
    polygon(screen, (142, 190, 179),
            [(x + 220 * scale, y + 623 * scale), (x + 230 * scale, y + 618 * scale),
             (x + 225 * scale, y + 630 * scale)])
    # cat
    ellipse(screen, gray, (x + 178 * scale, y + 575 * scale, 50 * scale, 40 * scale))
    polygon(screen, white, [(x + 185 * scale, y + 607 * scale), (x + 190 * scale, y + 607 * scale),
                            (x + 187 * scale, y + 612 * scale)])
    polygon(screen, white, [(x + 200 * scale, y + 610 * scale), (x + 205 * scale, y + 610 * scale),
                            (x + 202 * scale, y + 615 * scale)])

    draw_ellipse_angle(screen, gray, (x + 380 * scale, y + 580 * scale, 100 * scale, 25 * scale), 45)
    draw_ellipse_angle(screen, gray, (x + 200 * scale, y + 610 * scale, 25 * scale, 100 * scale), 135)
    draw_ellipse_angle(screen, gray, (x + 235 * scale, y + 610 * scale, 25 * scale, 100 * scale), 135)
    draw_ellipse_angle(screen, gray, (x + 335 * scale, y + 610 * scale, 25 * scale, 100 * scale), 225)
    draw_ellipse_angle(screen, gray, (x + 370 * scale, y + 610 * scale, 25 * scale, 100 * scale), 225)
    polygon(screen, gray, [(x + 220 * scale, y + 590 * scale), (x + 215 * scale, y + 580 * scale),
                           (x + 225 * scale, y + 570 * scale)])
    polygon(screen, gray, [(x + 190 * scale, y + 590 * scale), (x + 180 * scale, y + 590 * scale),
                           (x + 175 * scale, y + 570 * scale)])
    circle(screen, white, (x + 190 * scale, y + 590 * scale), 5 * scale)
    circle(screen, white, (x + 210 * scale, y + 590 * scale), 5 * scale)
    circle(screen, (0, 0, 0), (x + 212 * scale, y + 590 * scale), 2 * scale)
    circle(screen, (0, 0, 0), (x + 192 * scale, y + 590 * scale), 2 * scale)
    circle(screen, (0, 0, 0), (x + 192 * scale, y + 600 * scale), 2 * scale)


def draw_chukcha(x, y, scale):
    x *= scale
    y *= scale
    brown = (165, 126, 103)
    dbrown = (93, 71, 57)
    ellipse(screen, gray, (x + 530 * scale, y + 450 * scale, 140 * scale, 70 * scale))
    circle(screen, brown, (x + 600 * scale, y + 600 * scale), 100 * scale, draw_top_left=True, draw_top_right=True)
    ellipse(screen, brown, (x + 540 * scale, y + 600 * scale, 40 * scale, 50 * scale))
    ellipse(screen, brown, (x + 620 * scale, y + 600 * scale, 40 * scale, 50 * scale))
    ellipse(screen, brown, (x + 520 * scale, y + 630 * scale, 50 * scale, 25 * scale))
    ellipse(screen, brown, (x + 630 * scale, y + 630 * scale, 50 * scale, 25 * scale))
    rect(screen, dbrown, (x + 500 * scale, y + 600 * scale, 200 * scale, 25 * scale))
    rect(screen, dbrown, (x + 575 * scale, y + 500 * scale, 50 * scale, 100 * scale))
    ellipse(screen, brown, (x + 550 * scale, y + 455 * scale, 100 * scale, 55 * scale))
    ellipse(screen, gray, (x + 560 * scale, y + 460 * scale, 80 * scale, 45 * scale))
    line(screen, 'black', (x + 570 * scale, y + 475 * scale), (x + 580 * scale, y + 480 * scale))
    line(screen, 'black', (x + 630 * scale, y + 475 * scale), (x + 620 * scale, y + 480 * scale))
    arc(screen, 'black', (x + 575 * scale, y + 485 * scale, 50 * scale, 10 * scale), 0, math.pi)
    ellipse(screen, brown, (x + 470 * scale, y + 520 * scale, 80 * scale, 25 * scale))
    draw_ellipse_angle(screen, brown, (x + 650 * scale, y + 520 * scale, 80 * scale, 25 * scale), 30)
    line(screen, 'black', (x + 480 * scale, y + 450 * scale), (x + 490 * scale, y + 650 * scale))


pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))
screen.fill((206, 206, 206))

# ground
white = (255, 255, 255)
rect(screen, white, (0, 400, 800, 800))

# iglu
gray = (220, 220, 220)
draw_iglu(400, 200, 0.7)
draw_iglu(0, 0, 1)
draw_iglu(100, 550, 0.5)
draw_iglu(300, 600, 0.5)


draw_chukcha(700, 300, 0.5)
draw_chukcha(650, 350, 0.5)
draw_chukcha(450, 400, 0.5)
draw_chukcha(0, 0, 1)

draw_cat(-50, 0, 1)
draw_cat(50, 100, 1)
draw_cat(-80, 400, 0.5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
