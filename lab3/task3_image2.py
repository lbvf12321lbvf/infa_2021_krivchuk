import pygame
from pygame.draw import *
import numpy as np

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 800))


def cloud_circle(x, y, size):
    """
    рисует круг для облака
    :param x: x координата
    :param y: y координата
    :param size: коэф размера
    :return: none
    """
    circle(screen, (255, 255, 255), (x, y), 30 * size)
    circle(screen, (0, 0, 0), (x, y), 30 * size, 2)


def tree_circle(x, y, size):
    """
    рисует круг для дерева
    :param x: x координата
    :param y: y координата
    :param size: коэф размера
    :return: none
    """
    circle(screen, (0, 123, 31), (x, y), 30 * size)
    circle(screen, (0, 0, 0), (x, y), 30 * size, 2)


def cloud(x, y, size):
    """
    рисует облако из кругов при помощи tree_circle()
    :param x: x левого нижнего элемента
    :param y: н левого нижнего элемента
    :param size: коэф размера
    :return: none
    """
    cloud_circle(x, y, size)
    cloud_circle(x + 30 * size, y, size)
    cloud_circle(x + 60 * size, y, size)
    cloud_circle(x + 90 * size, y, size)
    cloud_circle(x + 60 * size, y - 30 * size, size)
    cloud_circle(x + 30 * size, y - 30 * size, size)


def tree(x, y, size):
    """
    рисуется дерево при помощи tree_circle и rect
    :param x: x координата низа ствола
    :param y: y координта низа ствола
    :param size: коэф размера
    :return: none
    """
    rect(screen, (0, 0, 0), (x - 10 * size, y, 20 * size, 100 * size))  # tree trunk
    tree_circle(x, y - 75 * size, size)
    tree_circle(x + 30 * size, y - 55 * size, size)
    tree_circle(x - 30 * size, y - 55 * size, size)
    tree_circle(x, y - 40 * size, size)
    tree_circle(x + 23 * size, y - 10 * size, size)
    tree_circle(x - 30 * size, y - 10 * size, size)


def sun(n, radius, position):
    """
    рисует солнце на полигоне, путём рисования множества трекгольников
    :param n: количество кругов
    :param radius: радиус
    :param position: (x, y) координаты
    :return: none
    """
    n, r = n, radius
    x, y = position
    rmin = r * 0.9
    pts = []
    for i in range(n):
        pts.append([x + r * np.cos(2 * np.pi * i / n), y + r * np.sin(2 * np.pi * i / n)])
        pts.append([x + rmin * np.cos(2 * np.pi * i / n + np.pi / n), y + rmin * np.sin(2 * np.pi * i / n + np.pi / n)])
    polygon(screen, 'yellow', pts)


def house_roof(x, y, size):
    """
    рисует крышу дому
    :param x: x координата нижнего левого края
    :param y: н координата нижнего левого края
    :param size: коэф размера
    :return: none
    """
    polygon(screen, (200, 0, 0), [(x, y), (x + 300 * size, y), ((2 * x + 300 * size) / 2, y - 110 * size)])
    polygon(screen, (0, 0, 0), [(x, y), (x + 300 * size, y), ((2 * x + 300 * size) / 2, y - 110 * size)], 3)


def house_window(x, y, a, b):
    """
    рисует окно
    :param x: левая верхняя координата x
    :param y: левая верхняя координата y
    :param a: ширина в px
    :param b: высота в px
    :return: none
    """
    rect(screen, (0, 200, 200), (x, y, a, b))
    rect(screen, (0, 0, 0), (x, y, a, b), 3)


def house_basement(x, y, size):
    """
    рисует тело дома
    :param x: верхняя левая координата x
    :param y: верхняя левая координата y
    :param size: коэф размера
    :return: none
    """
    rect(screen, (99, 65, 30), (x, y, 300 * size, 200 * size))
    rect(screen, (0, 0, 0), (x, y, 300 * size, 200 * size), 3)


def house(x, y, size):
    """
    рисует дом при помощи house_basement(),house_roof(),house_window()
    :param x:координата x левого верхнего угла
    :param y:координата н левого верхнего угла
    :param size:коэф размера
    :return:none
    """
    house_basement(x, y, size)
    house_roof(x, y, size)
    house_window(x + 100 * size, y + 70 * size, 100 * size, 60 * size)


def background(color1, color2):
    """
    рисует задний план
    :param color1: цвет неба
    :param color2: цвет земли
    :return: none
    """
    rect(screen, color1, (0, 0, 1200, 400))
    rect(screen, color2, (0, 400, 1200, 400))


background('blue', 'green')
sun(20, 50, (70, 70))
cloud(250, 100, 1)
cloud(600, 190, 0.8)
cloud(900, 170, 1.2)
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
