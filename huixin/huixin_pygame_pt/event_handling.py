import pygame
pygame.init()

color = (255,0,0)
position = (0, 0)


canvas = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Event handling!")

image = pygame.image.load(".\OneDrive\git_repo\group6_project\huixin_pygame_pt\image.JPG")
optimized_image =image.convert()

# clock = pygame.time.Clock()
# clock.tick(60)

exit = False



while not exit:
    canvas.fill(color)
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d: 
                position = (position[0] + 10, position[1])
                print("You have pressed right arrow key") 
            elif event.key == pygame.K_LEFT: 
                print("You have pressed left arrow key") 
                position = (position[0] - 10, position[1])

    canvas.blit(optimized_image, dest = position)
        
    pygame.display.update()
    pygame.time.delay(1000)