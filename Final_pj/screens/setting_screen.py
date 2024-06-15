from button import Button
import pygame
import settings_general as settings
import sys
from pet import Pet

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)


menu_font = pygame.font.Font(settings.font_path, settings.menu_font_size)

def setting_screen(screen, pet): #volumn, resume, return to main menu
    from screens.main_menu import main_menu
    vol_up_button = Button(u'Volume Up', (300, 200), menu_font, screen, GRAY, u'Volume Up')
    vol_down_button = Button(u'Volume Down', (300, 300), menu_font, screen, GRAY, u'Volume Down')
    resume_button = Button(u'Resume', (300, 400), menu_font, screen, GRAY, u'Resume')
    return_to_main_menu_button = Button(u'Return to Main Menu', (300, 500), menu_font, screen, GRAY, u'Return to Main Menu')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if vol_up_button.click(event):
                    # pass
                    pygame.mixer.music.set_volume(min(1, pygame.mixer.music.get_volume() + 10))
                if vol_down_button.click(event):
                    # pass
                    pygame.mixer.music.set_volume(max(0, pygame.mixer.music.get_volume() - 10))
                if resume_button.click(event):
                    # game_screen(screen)
                    return
                if return_to_main_menu_button.click(event):
                    pet.reset()
                    screen.fill(BLACK)
                    main_menu(screen)
            elif event.type == pygame.MOUSEBUTTONUP:
                vol_up_button.release(event)
                vol_down_button.release(event)
                resume_button.release(event)
                return_to_main_menu_button.release(event)
        screen.fill(BLACK)
        vol_up_button.show()
        vol_down_button.show()
        resume_button.show()
        return_to_main_menu_button.show()
        pygame.display.update()