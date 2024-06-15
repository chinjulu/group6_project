import pygame
from pygame.locals import *

pygame.init()
canvas = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Draw with mouse!")
canvas.fill((255, 255, 255))

circle_position = []
circle_radius = 10
circle_color = (255, 150, 0)

exit = False

while not exit:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit = True
        if event.type == MOUSEBUTTONDOWN:
            circle_position.append(event.pos)
        if event.type == MOUSEBUTTONUP:
            circle_position.append(event.pos)
            # pygame.draw.circle(canvas, circle_color, circle_position[0], circle_radius, 0)
            # circle_position = []
            for i in circle_position:
                pygame.draw.circle(canvas, circle_color, i, circle_radius, 0)
                circle_color = (circle_color[0]-1 , circle_color[1] +1, circle_color[2] +1)
    pygame.display.update()