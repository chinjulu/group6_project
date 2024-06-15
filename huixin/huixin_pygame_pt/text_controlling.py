####### display 2 fonts on the screen #######
# import pygame
# pygame.init()
# pygame.font.init()

# # Set up the drawing window
# display_surface = pygame.display.set_mode([800, 600])
# pygame.display.set_caption("text control")

# font1 = pygame.font.Font(".\OneDrive\git_repo\group6_project\huixin_pygame_pt\_fonts\Magiesta.ttf", 50)
# font2 = pygame.font.Font("OneDrive\git_repo\group6_project\huixin_pygame_pt\_fonts\Manetains.otf", 40)

# text1 = font1.render('Magiesta', True, (0, 255, 0))
# text2 = font2.render('Manetains', True, (0, 255, 0))

# textRect1 = text1.get_rect()
# textRect2 = text2.get_rect()
 
# textRect1.center = (250, 250)

# textRect2.center = (250, 300)
 
# while True:
#     display_surface.fill((255, 0, 0))
 
#     display_surface.blit(text1, textRect1)
#     display_surface.blit(text2, textRect2)
 
#     for event in pygame.event.get():
 
#         if event.type == pygame.QUIT:

#             pygame.quit()
#             quit()
#         pygame.display.update()



####### cursor input on window #######
# import pygame
# import time
# pygame.init()
# pygame.font.init()
# display_screen = pygame.display.set_mode([800, 600])
# pygame.display.set_caption("cursor input on window")

# text = "hello world"
# font = pygame.font.Font(".\OneDrive\git_repo\group6_project\huixin_pygame_pt\_fonts\Magiesta.ttf", 50)
# img = font.render(text, True, (255, 255, 255))
# rect = img.get_rect()
# cursor = pygame.Rect(rect.right, rect.top, 3, rect.height)

# running = True
 
# while running:
     
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_BACKSPACE:
#                 if len(text) > 0:
#                     text = text[:-1]
#             else:
#                 text += event.unicode
#             img = font.render(text, True, (255, 255, 255))
#             rect.size = img.get_size()
#             cursor.topleft = rect.topright

#     display_screen.fill((0, 0, 0))
#     display_screen.blit(img, rect)

#     if time.time() % 1 > 0.5:
#         pygame.draw.rect(display_screen, (255, 255, 255), cursor)

#     pygame.display.update()
# pygame.quit()

####### scrolling text #######
# import pygame module in this program
# import pygame

# # activate the pygame library 
# # initiate pygame and give permission 
# # to use pygame's functionality. 
# pygame.init()


# # create the display surface object 
# # (x, y) is the height and width of pygame window
# win=pygame.display.set_mode((500, 500))

# # set the pygame window name 
# pygame.display.set_caption("Scrolling Text")

# # setting the pygame font style(1st parameter)
# # and size of font(2nd parameter)
# Font=pygame.font.SysFont('timesnewroman', 30)

# # define the RGB value for white, 
# # green, yellow, orange colour 
# white=(255, 255, 255)
# yellow=(255, 255, 0)
# green=(0, 255, 255)
# orange=(255, 100, 0)
# done=False

# # Split the text into letters 
# # 3rd parameter is font colour and 
# # 4th parameter is Font background
# letter1=Font.render("H", False, orange, yellow)
# letter2=Font.render("E", False, orange, green)
# letter3=Font.render("M", False, orange, yellow)
# letter4=Font.render("A", False, orange, green)
# letter5=Font.render("N", False, orange, yellow)
# letter6=Font.render("T", False, orange, green)
# letter7=Font.render("H", False, orange, yellow)

# # assigning values to
# # i and c variable 
# i=0
# c=1

# # infinite loop
# while not done:
# 	if(i>=820):
# 		i=0
# 		c+=1
# 		pygame.time.wait(50)
		
# 	# completely fill the surface object 
# 	# with white color 
# 	win.fill(white)
# 	if(c%6==0): 
# 		# Scrolling the text in diagonal
# 		# on right side of the Screen.
# 		# copying the text surface object 
# 		# to the display surface object 
# 		# at the center coordinate. 
# 		win.blit(letter1, (662-i, -162+i))
# 		win.blit(letter2, (639-i, -139+i))
# 		win.blit(letter3, (608-i, -108+i))
# 		win.blit(letter4, (579-i, -79+i))
# 		win.blit(letter5, (552-i, -52+i))
# 		win.blit(letter6, (529-i, -29+i))
# 		win.blit(letter7, (500 -i, 0 + i))
# 		i+=80
# 	if(c%6==5): 
# 		# Scrolling the text in diagonal on
# 		# left side of the Screen.
# 		win.blit(letter1, (-162+i, -162+i)) 
# 		win.blit(letter2, (-135+i, -135+i))
# 		win.blit(letter3, (-110+i, -110+i))
# 		win.blit(letter4, (-79+i, -79+i))
# 		win.blit(letter5, (-52+i, -52+i))
# 		win.blit(letter6, (-27+i, -27+i))
# 		win.blit(letter7, (0+i, 0+i))
		
# 		# Decides the speed of
# 		# the text on screen
# 		i+=80
# 	if(c%6==4): 
	
# 		# Scrolling the text in
# 		# right side of the Screen.
# 		win.blit(letter1, (480, -180+i))
# 		win.blit(letter2, (480, -150+i))
# 		win.blit(letter3, (480, -120+i))
# 		win.blit(letter4, (480, -90+i))
# 		win.blit(letter5, (480, -60+i))
# 		win.blit(letter6, (480, -30+i))
# 		win.blit(letter7, (480, 0+i))
		
# 		# Decides the speed of
# 		# the text on screen
# 		i +=80
# 	if(c%6==3): 
# 		# Scrolling the text in left
# 		# side of the Screen.
# 		win.blit(letter1, (0, -180+i))
# 		win.blit(letter2, (0, -150+i))
# 		win.blit(letter3, (0, -120+i))
# 		win.blit(letter4, (0, -90+i))
# 		win.blit(letter5, (0, -60+i))
# 		win.blit(letter6, (0, -30+i))
# 		win.blit(letter7, (0, 0+i))
		
# 		# Decides the speed of
# 		# the text on screen
# 		i+=80
# 	if(c%6==1):

# 		win.blit(letter1, (-124+i, 0))
# 		win.blit(letter2, (-102+i, 0))
# 		win.blit(letter3, (-82+i, 0))
# 		win.blit(letter4, (-58+i, 0))
# 		win.blit(letter5, (-40+i, 0))
# 		win.blit(letter6, (-19+i, 0))
# 		win.blit(letter7, (0+i, 0))
		
# 		# Decides the speed of
# 		# the text on screen
# 		i +=80
# 	if(c%6==2):
	
# 	# Scrolling the text in bottom of the Screen.
# 		win.blit(letter1, (-124+i, 470))
# 		win.blit(letter2, (-102+i, 470))
# 		win.blit(letter3, (-82+i, 470))
# 		win.blit(letter4, (-58+i, 470))
# 		win.blit(letter5, (-40+i, 470))
# 		win.blit(letter6, (-19+i, 470))
# 		win.blit(letter7, (0+i, 470))
		
# 		# Decides the speed
# 		# of the text on screen
# 		i+=80
	
# 	# Draws the surface object to the screen.
# 	pygame.display.update()
	
# 	# iterate over the list of Event objects 
# 	# that was returned by pygame.event.get() method
# 	for event in pygame.event.get():
# 		if(event.type==pygame.QUIT):
# 			done=True
# 	#Delay with 5ms
# 	pygame.time.wait(500)
# pygame.quit()


####### How to create a text input box with Pygame? #######
# import sys module 
import pygame 
import sys 


# pygame.init() will initialize all 
# imported module 
pygame.init() 

clock = pygame.time.Clock() 

# it will display on screen 
screen = pygame.display.set_mode([600, 500]) 

# basic font for user typed 
base_font = pygame.font.Font(None, 32) 
user_text = '' 

# create rectangle 
input_rect = pygame.Rect(200, 200, 140, 32) 

# color_active stores color(lightskyblue3) which 
# gets active when input box is clicked by user 
color_active = pygame.Color('lightskyblue3') 

# color_passive store color(chartreuse4) which is 
# color of input box. 
color_passive = pygame.Color('chartreuse4') 
color = color_passive 

active = False

while True: 
	for event in pygame.event.get(): 

	# if user types QUIT then the screen will close 
		if event.type == pygame.QUIT: 
			pygame.quit() 
			sys.exit() 

		if event.type == pygame.MOUSEBUTTONDOWN: 
			if input_rect.collidepoint(event.pos): 
				active = True
			else: 
				active = False

		if event.type == pygame.KEYDOWN: 

			# Check for backspace 
			if event.key == pygame.K_BACKSPACE: 

				# get text input from 0 to -1 i.e. end. 
				user_text = user_text[:-1] 

			# Unicode standard is used for string 
			# formation 
			else: 
				user_text += event.unicode
	
	# it will set background color of screen 
	screen.fill((255, 255, 255)) 

	if active: 
		color = color_active 
	else: 
		color = color_passive 
		
	# draw rectangle and argument passed which should 
	# be on screen 
	pygame.draw.rect(screen, color, input_rect) 

	text_surface = base_font.render(user_text, True, (255, 255, 255)) 
	
	# render at position stated in arguments 
	screen.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
	
	# set width of textfield so that text cannot get 
	# outside of user's text input 
	input_rect.w = max(100, text_surface.get_width()+10) 
	
	# display.flip() will update only a portion of the 
	# screen to updated, not full area 
	pygame.display.flip() 
	
	# clock.tick(60) means that for every second at most 
	# 60 frames should be passed. 
	clock.tick(60) 
