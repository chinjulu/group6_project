# import required libraries
import pygame
import random

# initialize pygame objects
pygame.init()

# define the colours
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# set the Dimensions
width = 650
height = 700

# size of a block
pixel = 64

# set Screen
screen = pygame.display.set_mode((width, 
								height))

# set caption
pygame.display.set_caption("CORONA SCARPER")

# load the image
# gameIcon = pygame.image.load("rectangleBlock.png")

# set icon
# pygame.display.set_icon(gameIcon)

# load the image
backgroundImg = pygame.image.load("wallBackground.jpg")
# load the image


# set the position
playerXPosition = (width/2) - (pixel/2)

# So that the player will be 
# at height of 20 above the base
playerYPosition = height - pixel - 10	

# set initially 0
playerXPositionChange = 0

# define a function for setting
# the image at particular
# coordinates
def player(x, y):
# paste image on screen object
    # screen.blit(playerImage, (x, y))
    pygame.draw.rect(screen, (0, 0, 255), (x, y, pixel, pixel))
    # pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) 

# load the image
blockImage = pygame.image.load("rectangleBlock.png")

# set the random position
blockXPosition = random.randint(0,
								(width - pixel))

blockYPosition = 0 - pixel

# set the speed of
# the block
blockXPositionChange = 0
blockYPositionChange = 2

# define a function for setting
# the image at particular
# coordinates
def block(x, y):
# paste image on screen object
    # screen.blit(blockImage,(x, y))
    pygame.draw.rect(screen, (170, 170, 170), (x, y, pixel, pixel))
