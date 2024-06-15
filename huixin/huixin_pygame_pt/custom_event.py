import pygame
pygame.init()

canvas = pygame.display.set_mode((800, 600))

timer = pygame.time.Clock()
pygame.display.set_caption('custom event')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

bg_active_color = WHITE
canvas.fill(bg_active_color)

CHANGE_COLOR = pygame.USEREVENT + 1
ON_BOX = pygame.USEREVENT + 2

box = pygame.Rect(100, 100, 100, 100)
grow = True

pygame.time.set_timer(CHANGE_COLOR, 500)

exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == CHANGE_COLOR:
            bg_active_color = RED if bg_active_color == WHITE else WHITE
            canvas.fill(bg_active_color)
        if event.type == ON_BOX:
            if grow:
                box.width += 1
                box.height += 1
                if box.width == 200:
                    grow = False
            else:
                box.width -= 1
                box.height -= 1
                if box.width == 100:
                    grow = True

    
    if box.collidepoint(pygame.mouse.get_pos()): 
        pygame.event.post(pygame.event.Event(ON_BOX)) 

    pygame.draw.rect(canvas, GREEN, box)
    pygame.display.flip()
    timer.tick(60)