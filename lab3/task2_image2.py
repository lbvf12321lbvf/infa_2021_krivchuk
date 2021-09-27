import pygame
from pygame.draw import *
import numpy as np 
pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))

def cloud_circle(x,y):
    circle(screen, (255, 255, 255), (x, y), 30)
    circle(screen, (0, 0, 0), (x, y), 30, 2)
def tree_circle(x,y):
    circle(screen, (30, 255, 30), (x, y), 30)
    circle(screen, (0, 0, 0), (x, y), 30, 2)

def draw_regular_polygon(n, radius, position):
    n, r = n, radius
    x, y = position
    rmin=r*0.9
    dx=np.pi/n
    pts = []
    for i in range(n):
        pts.append([x + r * np.cos(2 * np.pi * i / n), y + r * np.sin(2 * np.pi * i / n)])
        pts.append([x + rmin * np.cos(2 * np.pi * i / n + np.pi / n), y + rmin * np.sin(2 * np.pi * i / n +  np.pi / n)])
    polygon(screen, 'yellow', pts)
#https://stackoverflow.com/questions/29064259/drawing-pentagon-hexagon-in-pygame
    
rect(screen, (0, 255, 255), (0, 0, 800, 400))
rect(screen, (0, 255, 0), (0, 400, 800, 400)) #background

cloud_circle(440, 100)
cloud_circle(470, 100)
cloud_circle(500, 100)
cloud_circle(530, 100)
cloud_circle(500, 70)
cloud_circle(470, 70) #cloud

rect(screen, (99, 65, 30), (130, 350, 300, 200)) 
rect(screen, (0, 0, 0), (130, 350, 300, 200), 3) #house basement

polygon(screen, (200, 0, 0), [(130, 350), (430, 350), (280, 260)])
polygon(screen, (0, 0, 0), [(130, 350), (430, 350), (280, 260)], 3) #house roof

rect(screen, (0, 200, 200), (230, 420, 100, 60)) 
rect(screen, (0, 0, 0), (230, 420, 100, 60), 3) #house window

rect(screen, (0, 0, 0), (610, 380, 20, 100)) #tree trunk
tree_circle(620, 280)
tree_circle(650, 310)
tree_circle(590, 310)
tree_circle(620, 340)
tree_circle(643, 370)
tree_circle(590, 370) #tree crown

draw_regular_polygon(20, 50, (700,100)) #sun

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
