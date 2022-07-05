# Точки по нажатию и линия по удержанию
import pygame
pygame.init()
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Кликай и/или удерживай чтобы рисовать")
keep_going = True
YELLOW = (255, 255, 0)  # Желтый цвет
radius = 15
mousedown = False
while keep_going:  # Игровой цикл
    for event in pygame.event.get():  # Обработка событий
        if event.type == pygame.QUIT:
            keep_going = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
    if mousedown:  # Рисование
        spot = pygame.mouse.get_pos()
        pygame.draw.circle(screen, YELLOW, spot, radius)
    pygame.display.update()
pygame.quit()