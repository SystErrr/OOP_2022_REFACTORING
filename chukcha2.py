import math

import pygame
from pygame.draw import *

gray = (220, 220, 220)
white = (255, 255, 255)


def input_many():
    """
    Ввод нескольких числе с клавиатуры и перевод их в тип int, возвращает массив
    """
    m_numbers = []
    m_numbers = list(map(int, input().split()))
    return m_numbers


def background(width, height, color):
    """
    Задание экрана, возвращает screen
    width, height - ширина и высота окна
    color - цвет фона, заданный в формате, подходящем для pygame.Color
    """
    screen = pygame.display.set_mode((width, height))
    screen.fill(color)
    return screen


def equation(x, y, x0, y0, scale):
    """
    Уравнение для смены координат и изменения размера фигур
    x0, y0 - координаты начальной точки фигуры
    x, y - задаваемые координаты начала рисовки
    """
    scale = scale / 10
    x1 = - x0 * scale + x
    y1 = - y0 * scale + y
    return x1, y1, scale

def draw_ellipse_angle(surface, color, rect, angle, width=0):
    """
    Функция для рисования повернутого эллипса
    screen - screen - объект pygame.Surface
    color - цвет фона, заданный в формате, подходящем для pygame.Color
    rect - прямоугольник, описывающий эллипс, список / массив типа (x, y, ширина, высота)
    angle - угол поворота эллипса
    width - ширина линии (0 - заливка)
    """
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center=target_rect.center))


def draw_iglu(x, y, scale, screen):
    """
    Функция для рисования иглу
    screen - screen - объект pygame.Surface
    x, y - задаваемые координаты
    scale - задаваемый размер
    """
    x1, y1, scale = equation(x, y, 150, 500, scale)
    circle(screen, gray, (x1 + 300 * scale, y1 + 500 * scale), 150 * scale, draw_top_left=True, draw_top_right=True)
    circle(screen, (0, 0, 0), (x1 + 300 * scale, y1 + 500 * scale), 150 * scale, 2, draw_top_left=True,
           draw_top_right=True)
    arc(screen, (0, 0, 0), (x1 + 225 * scale, y1 + 350 * scale, 150 * scale, 40 * scale), math.pi, 0)
    arc(screen, (0, 0, 0), (x1 + 175 * scale, y1 + 400 * scale, 250 * scale, 40 * scale), math.pi, 0)
    arc(screen, (0, 0, 0), (x1 + 155 * scale, y1 + 450 * scale, 290 * scale, 40 * scale), math.pi, 0)
    line(screen, (0, 0, 0), (x1 + 250 * scale, y1 + 385 * scale), (x1 + 230 * scale, y1 + 435 * scale))
    line(screen, (0, 0, 0), (x1 + 300 * scale, y1 + 350 * scale), (x1 + 300 * scale, y1 + 390 * scale))
    line(screen, (0, 0, 0), (x1 + 350 * scale, y1 + 385 * scale), (x1 + 380 * scale, y1 + 435 * scale))
    line(screen, (0, 0, 0), (x1 + 265 * scale, y1 + 440 * scale), (x1 + 250 * scale, y1 + 487 * scale))
    line(screen, (0, 0, 0), (x1 + 205 * scale, y1 + 432 * scale), (x1 + 185 * scale, y1 + 480 * scale))
    line(screen, (0, 0, 0), (x1 + 400 * scale, y1 + 432 * scale), (x1 + 420 * scale, y1 + 480 * scale))
    line(screen, (0, 0, 0), (x1 + 335 * scale, y1 + 440 * scale), (x1 + 350 * scale, y1 + 487 * scale))
    line(screen, (0, 0, 0), (x1 + 150 * scale, y1 + 500 * scale), (x1 + 450 * scale, y1 + 500 * scale))


def draw_cat(x, y, scale, screen):
    """
    Функция для рисования кота с рыбой в зубах
    screen - screen - объект pygame.Surface
    x, y - задаваемые координаты
    scale - задаваемый размер
    """
    x1, y1, scale = equation(x, y, 180, 590, scale)
    ellipse(screen, gray, (x1 + 200 * scale, y1 + 600 * scale, 200 * scale, 50 * scale))
    # fish
    draw_ellipse_angle(screen, (142, 190, 179), (x1 + 170 * scale, y1 + 610 * scale, 50 * scale, 10 * scale), -20)
    circle(screen, "black", (x1 + 180 * scale, y1 + 610 * scale), 1)
    polygon(screen, (142, 190, 179),
            [(x1 + 220 * scale, y1 + 623 * scale), (x1 + 230 * scale, y1 + 618 * scale),
             (x1 + 225 * scale, y1 + 630 * scale)])
    # cat
    ellipse(screen, gray, (x1 + 178 * scale, y1 + 575 * scale, 50 * scale, 40 * scale))
    polygon(screen, white, [(x1 + 185 * scale, y1 + 607 * scale), (x1 + 190 * scale, y1 + 607 * scale),
                            (x1 + 187 * scale, y1 + 612 * scale)])
    polygon(screen, white, [(x1 + 200 * scale, y1 + 610 * scale), (x1 + 205 * scale, y1 + 610 * scale),
                            (x1 + 202 * scale, y1 + 615 * scale)])

    draw_ellipse_angle(screen, gray, (x1 + 380 * scale, y1 + 580 * scale, 100 * scale, 25 * scale), 45)
    draw_ellipse_angle(screen, gray, (x1 + 200 * scale, y1 + 610 * scale, 25 * scale, 100 * scale), 135)
    draw_ellipse_angle(screen, gray, (x1 + 235 * scale, y1 + 610 * scale, 25 * scale, 100 * scale), 135)
    draw_ellipse_angle(screen, gray, (x1 + 335 * scale, y1 + 610 * scale, 25 * scale, 100 * scale), 225)
    draw_ellipse_angle(screen, gray, (x1 + 370 * scale, y1 + 610 * scale, 25 * scale, 100 * scale), 225)
    polygon(screen, gray, [(x1 + 220 * scale, y1 + 590 * scale), (x1 + 215 * scale, y1 + 580 * scale),
                           (x1 + 225 * scale, y1 + 570 * scale)])
    polygon(screen, gray, [(x1 + 190 * scale, y1 + 590 * scale), (x1 + 180 * scale, y1 + 590 * scale),
                           (x1 + 175 * scale, y1 + 570 * scale)])
    circle(screen, white, (x1 + 190 * scale, y1 + 590 * scale), 5 * scale)
    circle(screen, white, (x1 + 210 * scale, y1 + 590 * scale), 5 * scale)
    circle(screen, (0, 0, 0), (x1 + 212 * scale, y1 + 590 * scale), 2 * scale)
    circle(screen, (0, 0, 0), (x1 + 192 * scale, y1 + 590 * scale), 2 * scale)
    circle(screen, (0, 0, 0), (x1 + 192 * scale, y1 + 600 * scale), 2 * scale)


def draw_chukcha(x, y, scale, screen):
    """
    Функция для рисования чукчи
    screen - screen - объект pygame.Surface
    x, y - задаваемые координаты
    scale - задаваемый размер
    """
    x1, y1, scale = equation(x, y, 530, 450, scale)
    brown = (165, 126, 103)
    dbrown = (93, 71, 57)
    # капюшон
    ellipse(screen, gray, (x1 + 530 * scale, y1 + 450 * scale, 140 * scale, 70 * scale))
    # тело
    circle(screen, brown, (x1 + 600 * scale, y1 + 600 * scale), 100 * scale, draw_top_left=True, draw_top_right=True)
    ellipse(screen, brown, (x1 + 540 * scale, y1 + 600 * scale, 40 * scale, 50 * scale))
    ellipse(screen, brown, (x1 + 620 * scale, y1 + 600 * scale, 40 * scale, 50 * scale))
    ellipse(screen, brown, (x1 + 520 * scale, y1 + 630 * scale, 50 * scale, 25 * scale))
    ellipse(screen, brown, (x1 + 630 * scale, y1 + 630 * scale, 50 * scale, 25 * scale))
    rect(screen, dbrown, (x1 + 500 * scale, y1 + 600 * scale, 200 * scale, 25 * scale))
    rect(screen, dbrown, (x1 + 575 * scale, y1 + 500 * scale, 50 * scale, 100 * scale))
    # голова
    ellipse(screen, brown, (x1 + 550 * scale, y1 + 455 * scale, 100 * scale, 55 * scale))
    ellipse(screen, gray, (x1 + 560 * scale, y1 + 460 * scale, 80 * scale, 45 * scale))
    line(screen, 'black', (x1 + 570 * scale, y1 + 475 * scale), (x1 + 580 * scale, y1 + 480 * scale))
    line(screen, 'black', (x1 + 630 * scale, y1 + 475 * scale), (x1 + 620 * scale, y1 + 480 * scale))
    arc(screen, 'black', (x1 + 575 * scale, y1 + 485 * scale, 50 * scale, 10 * scale), 0, math.pi)
    # руки
    ellipse(screen, brown, (x1 + 470 * scale, y1 + 520 * scale, 80 * scale, 25 * scale))
    draw_ellipse_angle(screen, brown, (x1 + 650 * scale, y1 + 520 * scale, 80 * scale, 25 * scale), 30)
    # копье
    line(screen, 'black', (x1 + 480 * scale, y1 + 450 * scale), (x1 + 490 * scale, y1 + 650 * scale))





