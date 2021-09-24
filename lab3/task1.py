import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
rect(screen, (200, 200, 200), (0, 0, 600, 600))

circle(screen, (255, 255, 0), (300, 300), 100)
circle(screen, (0, 0, 0), (300, 300), 100, 2) #face

circle(screen, (255, 0, 0), (260, 260), 17)
circle(screen, (0, 0, 0), (260, 260), 17, 2) #eye 1 red

circle(screen, (255, 0, 0), (340, 260), 24)
circle(screen, (0, 0, 0), (340, 260), 24, 2) #eye 2 red

circle(screen, (0, 0, 0), (340, 260), 12)
circle(screen, (0, 0, 0), (260, 260), 7) #eyes black

rect(screen, (0, 0, 0), (265, 357, 90, 15)) #mouth

polygon(screen, (0, 0, 0), [(280, 240), (290, 230), (180, 180), (170, 190)]) #brow 1
polygon(screen, (0, 0, 0), [(300, 240), (320, 250), (400, 190), (380, 180)]) #brow 2

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
