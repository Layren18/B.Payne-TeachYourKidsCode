# Красная точка
import pygame
pygame.init()
screen = pygame.display.set_mode ([800, 600])
keep_going = True
RED = (200, 0, 0)
radius = 50
while keep_going:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            keep_going = False
    pygame.draw.circle (screen, RED, (200,350), radius)
    pygame.display.update()
pygame.quit()