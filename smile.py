import pygame
from pygame.draw import *


def background(width, height, color):
    """
    Задание экрана, возвращает screen
    width, height - ширина и высота окна
    color - цвет фона, заданный в формате, подходящем для pygame.Color
    """
    screen = pygame.display.set_mode((width, height))
    screen.fill(color)
    return screen


def face(screen):
    """
    Рисует лицо
    screen - объект pygame.Surface
    """
    circle(screen, (255, 199, 30), (200, 200), 150)


def eyes(screen):
    """
    Рисует глаза
    screen - объект pygame.Surface
    """
    circle(screen, (255, 0, 0), (125, 150), 30)
    circle(screen, (0, 0, 0), (125, 150), 15)
    circle(screen, (255, 0, 0), (275, 150), 20, 30)
    circle(screen, (0, 0, 0), (275, 150), 15)


def mouth(screen):
    """
    Рисует рот
    screen - объект pygame.Surface
    """
    rect(screen, (0, 0, 0), (100, 250, 200, 50))


def brows(screen):
    """
    Рисует брови
    screen - объект pygame.Surface
    """
    polygon(screen, (0, 0, 0), [(40, 45), (30, 70), (170, 145), (180, 125)])
    polygon(screen, (0, 0, 0), [(360, 55), (370, 80), (230, 155), (220, 135)])


def smile():
    """
    Рисует смайлик на экране
    screen - объект pygame.Surface
    """
    screen = background(400, 400, (180, 180, 180))
    face(screen)
    eyes(screen)
    mouth(screen)
    brows(screen)