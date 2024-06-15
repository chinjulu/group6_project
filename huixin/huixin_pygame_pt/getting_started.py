import pygame

pygame.init()
color = (255,0,0)
position = (0, 0)
rect_color = (0, 255, 0)


canvas = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Show image!")

image = pygame.image.load(".\OneDrive\git_repo\group6_project\huixin_pygame_pt\image.JPG")
optimized_image =image.convert()
optimized_image.set_colorkey((255,255,255))

clock = pygame.time.Clock()
clock.tick(60)

exit = False

show_image = True

while not exit:
    canvas.fill(color)
    # canvas.blit(optimized_image, dest = position)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    if show_image:
        canvas.blit(optimized_image, dest = position)
        show_image = False
    else:
        pygame.draw.rect(canvas, rect_color, [30,30,60,60])
        pygame.draw.circle(canvas, rect_color,[400,400], 50,0)
        pygame.draw.polygon(canvas, 'blue', [[0,0],[50,50],[250,250],[150,20]])
        pygame.draw.line(canvas, 'blue', [0,0], [400,400], 5)
        show_image = True
    pygame.display.update()
    pygame.time.delay(1000)