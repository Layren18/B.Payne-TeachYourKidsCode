# Смайлик
import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
picture = pygame.image.load ("../10 глава/CrazySmile.bmp")
while keep_going:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            keep_going = False
    screen.blit (picture, (100,100))
    pygame.display.update()
pygame.quit ()