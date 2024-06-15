import pygame
import sys
from button import Button
from button import img_Button
import settings_general as settings

menu_font = pygame.font.Font(settings.font_path, settings.menu_font_size)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

def open_shop(screen, pet):
    shop_background_image = pygame.image.load(settings.shop_background_image_path)
    shop_background_image = pygame.transform.scale(shop_background_image, settings.screen_size)
    # buy_food_button = Button(u'Food: 3 dollar', (10, 400), menu_font, screen, GRAY, u'Food: 3 dollar')
    bmaboo_button_image_path = "Assets/img/bamboo.png"
    water_button_image_path = "Assets/img/bamboo.png"
    buy_food_button = img_Button(u'3 dollar', (30, 400), menu_font, screen, bmaboo_button_image_path, u'- 3兩')
    # buy_water_button = Button(u'Water: 1 dollar', (200, 400), menu_font, screen, GRAY, u'Water: 1 dollar')
    buy_water_button = img_Button(u'1 dollar', (200, 400), menu_font, screen, water_button_image_path, u'- 1兩')
    return_to_game_button = Button(u'Return', (400, 400), menu_font, screen, GRAY, u'Return')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if buy_food_button.click(event):
                    pet.buy_food()
                if buy_water_button.click(event):
                    pet.buy_water()
                if return_to_game_button.click(event):
                    return  # Simply return to go back to the game screen
            elif event.type == pygame.MOUSEBUTTONUP:
                buy_food_button.release(event)
                buy_water_button.release(event)

        screen.blit(shop_background_image, (0, 0))
        buy_food_button.show()
        buy_water_button.show()
        return_to_game_button.show()


        money_text = menu_font.render(f'Money: {pet.money}', True, WHITE)
        screen.blit(money_text, (500, 100))
        food_text = menu_font.render(f'Food: {pet.food_amount}', True, WHITE)
        screen.blit(food_text, (500, 150))
        water_text = menu_font.render(f'Water: {pet.water_amount}', True, WHITE)
        screen.blit(water_text, (500, 200))
        pygame.display.update()
