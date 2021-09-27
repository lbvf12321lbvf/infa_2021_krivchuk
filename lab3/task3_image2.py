import pygame
from pygame.draw import *
import numpy as np 
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 800))
#size - доля объекта от некоего стандартного размера (0.1, 0.2, ... 0.9, и т.д)
def cloud_circle(x,y, size):
    circle(screen, (255, 255, 255), (x, y), 30*size)
    circle(screen, (0, 0, 0), (x, y), 30*size, 2)
    
def tree_circle(x,y, size):
    circle(screen, (0, 123, 31), (x, y), 30*size)
    circle(screen, (0, 0, 0), (x, y), 30*size, 2)
    
def cloud(x,y, size):
    cloud_circle(x, y, size)
    cloud_circle(x+30*size, y, size)
    cloud_circle(x+60*size, y, size)
    cloud_circle(x+90*size, y, size)
    cloud_circle(x+60*size, y-30*size, size)
    cloud_circle(x+30*size, y-30*size, size) #x,y - координаты левого нижнего элемента
    
def tree(x,y, size):
    rect(screen, (0, 0, 0), (x-10*size, y, 20*size, 100*size)) #tree trunk
    tree_circle(x, y-75*size, size)
    tree_circle(x+30*size, y-55*size, size)
    tree_circle(x-30*size, y-55*size, size)
    tree_circle(x, y-40*size, size)
    tree_circle(x+23*size, y-10*size, size)
    tree_circle(x-30*size, y-10*size, size) #x,y - координаты начала ствола
    
def sun(n, radius, position):
    n, r = n, radius
    x, y = position
    rmin=r*0.9
    dx=np.pi/n
    pts = []
    for i in range(n):
        pts.append([x + r * np.cos(2 * np.pi * i / n), y + r * np.sin(2 * np.pi * i / n)])
        pts.append([x + rmin * np.cos(2 * np.pi * i / n + np.pi / n), y + rmin * np.sin(2 * np.pi * i / n +  np.pi / n)])
    polygon(screen, 'yellow', pts)
    
def house(x,y, size):
    rect(screen, (99, 65, 30), (x, y, 300*size, 200*size)) 
    rect(screen, (0, 0, 0), (x, y, 300*size, 200*size), 3) #house basement

    polygon(screen, (200, 0, 0), [(x, y), (x+300*size, y), ((2*x+300*size)/2, y-110*size)])
    polygon(screen, (0, 0, 0), [(x, y), (x+300*size, y), ((2*x+300*size)/2, y-110*size)], 3) #house roof

    rect(screen, (0, 200, 200), (x+100*size, y+70*size, 100*size, 60*size)) 
    rect(screen, (0, 0, 0), (x+100*size, y+70*size, 100*size, 60*size), 3) #house window   

#все функции готовы, начнём рисовать
rect(screen, (0, 255, 255), (0, 0, 1200, 400))
rect(screen, (0, 255, 0), (0, 400, 1200, 400)) #background
sun (20, 50, (70,70))
cloud (250, 100, 1)
cloud (600, 190, 0.8)
cloud (900, 170, 1.2)
house(150, 420, 0.8)
house(660, 420, 0.6)
tree(500, 420, 1.5)
tree(930, 420, 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
