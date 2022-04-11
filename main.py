from smile import *
from chukcha import *
from chukcha2 import *

pygame.init()
FPS = 30
def main_cycle():
    print('Выберите номер задания:')
    task = int(input())
    if task == 1:
        smile()
    elif task == 2:
        chukcha()
    elif task == 3:
        print('Введите кол-во иглу, чукч и котов через пробел')
        screen = background(800, 800, (206, 206, 206))
        rect(screen, 'white', (0, 400, 800, 800))
        a = input_many()
        iglu, chukchas, cats = a[0], a[1], a[2]
        for i in range(1, iglu + 1):
            print('Введите координаты и размер (стандарт - 10) иглу №', i)
            b = input_many()
            draw_iglu(b[0], b[1], b[2], screen)
        for i in range(1, chukchas + 1):
            print('Введите координаты и размер (стандарт - 10) чукчи №', i)
            b = input_many()
            draw_chukcha(b[0], b[1], b[2], screen)
        for i in range(1, cats + 1):
            print('Введите координаты и размер (стандарт - 10) кота №', i)
            b = input_many()
            draw_cat(b[0], b[1], b[2], screen)
    else:
        print('Такого задания не существует!')

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

    pygame.quit()

print('Данная программа позволяет выводить на экран изображения, сделанные с помощью библиотеки PyGame', '\n')
z = 1
while z == 1:
    main_cycle()
    print('Хотите продолжить?', '\n',
          '1 - да', '\n',
          '2 - нет')
    z = int(input())