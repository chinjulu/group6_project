# main_menu.py

import pygame
import sys
from button import Button
import settings_general as settings
from screens.egg_hatching_screen import egg_hatching_screen
from screens.show_leaderboard import show_leaderboard
from screens.music import sound_effects

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
text_color = (255, 255, 255)
outline_color = (0, 0, 0)
outline_thickness = 2

def main_menu(screen):
    menu_background_image = pygame.image.load(settings.menu_background_image_path)
    menu_background_image = pygame.transform.scale(menu_background_image, settings.screen_size)
    menu_font = pygame.font.Font(settings.font_path, settings.menu_font_size)
    heading_font = pygame.font.Font(settings.font_path, 55)

    heading_text = render_text_with_outline(u'寵物蛋遊戲', heading_font, text_color, outline_color, outline_thickness)
    
    start_button = Button(u'開始遊戲', (300, 200), menu_font, screen, GRAY, u'開始遊戲')
    exit_button = Button(u'結束遊戲', (300, 300), menu_font, screen, GRAY, u'結束遊戲')
    leaderboard_button = Button(u'查看排行榜', (300, 400), menu_font, screen, GRAY, u'查看排行榜')
    # sound_effects(False, None)
    music_path = "Assets/Bgm/bl cut.mp3"
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play(-1)  # Play the music in a loop
    # if screen is None:
    #     print("Error: Screen is None!!")
    # else:
    #     print(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
                

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.click(event):
                    egg_hatching_screen(screen)
                    start_button.release(event)
                if exit_button.click(event):
                    pygame.quit()
                    sys.exit()
                if leaderboard_button.click(event):
                    leaderboard_button.release(event)
                    show_leaderboard(screen)
                    
            # elif event.type == pygame.MOUSEBUTTONUP:
            #     start_button.release(event)
            #     exit_button.release(event)
            #     leaderboard_button.release(event)
        
        screen.blit(menu_background_image, (0, 0))
        screen.blit(heading_text, (250, 100))
        start_button.show()
        exit_button.show()
        leaderboard_button.show()
        pygame.display.update()


def render_text_with_outline(text, font, text_color, outline_color, outline_thickness):
    # Render the outline text
    outline_surface = font.render(text, True, outline_color)
    text_surface = font.render(text, True, text_color)

    width = text_surface.get_width() + outline_thickness * 2
    height = text_surface.get_height() + outline_thickness * 2

    # Create a new surface with the desired dimensions
    surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    surface = surface.convert_alpha()

    # Draw the outline text in all 8 directions around the original text
    for dx in range(-outline_thickness, outline_thickness + 1):
        for dy in range(-outline_thickness, outline_thickness + 1):
            if dx != 0 or dy != 0:
                surface.blit(outline_surface, (dx + outline_thickness, dy + outline_thickness))

    # Draw the original text on top of the outlines
    surface.blit(text_surface, (outline_thickness, outline_thickness))

    return surface