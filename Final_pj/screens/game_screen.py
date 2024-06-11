import pygame
import sys
from button import Button
from pet import Pet
import settings
from time import time
import random


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

pet = Pet()

menu_font = pygame.font.Font(settings.font_path, settings.menu_font_size)

def draw_pet_location(screen, pet_image_path):
    pet_image = pygame.image.load(pet_image_path)
    pet.rect = pet_image.get_rect()
    pet.rect.topleft = (pet.x, pet.y)
    img_width, img_height = pet_image.get_size()
    screen.blit(pet_image, pet.rect.topleft)
    return (img_width, img_height)

def draw_pet_attributes(screen, food_button, water_button):
    hungry_text = menu_font.render(f'Hungry Level: {pet.hungry_level}%', True, WHITE)
    screen.blit(hungry_text, (50, 50))

    happy_text = menu_font.render(f'Happy Level: {pet.happy_level}%', True, WHITE)
    screen.blit(happy_text, (50, 100))

    healthy_text = menu_font.render(f'Healthy Level: {pet.healthy_level}%', True, WHITE)
    screen.blit(healthy_text, (50, 150))

    food_button.show()
    water_button.show()

def draw_player_info(screen, shop_button):
    state_text = menu_font.render(f'State: {pet.state}', True, WHITE)
    screen.blit(state_text, (500, 50))

    money_text = menu_font.render(f'Money: {pet.money}', True, WHITE)
    screen.blit(money_text, (500, 100))

    hour_text = menu_font.render(f'Hour: {pet.hour}', True, WHITE)
    screen.blit(hour_text, (500, 200))

    status_text = menu_font.render(f'Status: {pet.status}', True, WHITE)
    screen.blit(status_text, (500, 250))

    shop_button.show()

def change_direction():
    pet.speed_x = random.choice([-1, 0, 1])
    pet.speed_y = random.choice([-1, 0, 1])

def game_screen(screen):
    last_update_time = time()
    direction_change_time = time()
    shop_button = Button(u'Shop', (500, 150), menu_font, screen, GRAY, u'Shop')
    food_button = Button(f'Food:{pet.food_amount}', (50, 200), menu_font, screen, GRAY, f'Food{pet.food_amount}')
    water_button = Button(f'Water:{pet.water_amount}', (50, 250), menu_font, screen, GRAY, f'Water:{pet.water_amount}')

    pet_image_path = settings.baby_pet_image_path if pet.state == 'baby' else (settings.teen_pet_image_path if pet.state == 'teen' else settings.adult_pet_image_path)
    happy_pet_image_path = settings.happy_pet_image_path  # 假设这是宠物开心状态的图片路径
    pet_happy_start_time = 0
    pet_is_happy = False

    change_direction()

    while True:
        current_time = time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if pet.status == 'dead':
                game_over_screen(screen)
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if shop_button.click(event):
                    open_shop(screen)
                if food_button.click(event):
                    pet.feed()
                    food_button = Button(f'Food:{pet.food_amount}', (50, 200), menu_font, screen, GRAY, f'Food{pet.food_amount}')
                if water_button.click(event):
                    pet.drink()
                    water_button = Button(f'Water:{pet.water_amount}', (50, 250), menu_font, screen, GRAY, f'Water:{pet.water_amount}')

                # 检查是否点击宠物
                if pet.rect.collidepoint(event.pos):
                    pet.touch_pet()
                    pet_image_path = happy_pet_image_path
                    pet_happy_start_time = current_time
                    pet_is_happy = True

            elif event.type == pygame.MOUSEBUTTONUP:
                shop_button.release(event)
                food_button.release(event)
                water_button.release(event)

        # 恢复宠物原始图片
        if pet_is_happy and current_time - pet_happy_start_time > 2:  # 2秒钟后恢复原始图片
            pet_image_path = settings.baby_pet_image_path if pet.state == 'baby' else (settings.teen_pet_image_path if pet.state == 'teen' else settings.adult_pet_image_path)
            pet_is_happy = False

        screen.fill(BLACK)
        draw_pet_attributes(screen, food_button, water_button)
        draw_player_info(screen, shop_button)
        img_width, img_height = draw_pet_location(screen, pet_image_path)

        if current_time - last_update_time >= 1:
            last_update_time = current_time
            pet.update_hour()

        if current_time - direction_change_time >= 1:  # 每1秒改变一次方向
            direction_change_time = current_time
            change_direction()

        if current_time - last_update_time >= 0.5 and current_time - last_update_time <= 0.55 or \
           current_time - last_update_time >= 0.95 and current_time - last_update_time <= 1:
            pet.x += pet.speed_x
            pet.y += pet.speed_y

        # 保持宠物在屏幕范围内，并在接近边界时改变方向
        if pet.x < 0:
            pet.x = 0
            change_direction()
        elif pet.x > screen.get_width() - img_width:
            pet.x = screen.get_width() - img_width
            change_direction()

        if pet.y < 0:
            pet.y = 0
            change_direction()
        elif pet.y > screen.get_height() - img_height:
            pet.y = screen.get_height() - img_height
            change_direction()

        pygame.display.update()

def open_shop(screen):
    buy_food_button = Button(u'Food: 3 dollar', (300, 200), menu_font, screen, GRAY, u'Food: 3 dollar')
    buy_water_button = Button(u'Water: 1 dollar', (300, 300), menu_font, screen, GRAY, u'Water: 1 dollar')
    return_to_game_button = Button(u'Return to Game', (300, 400), menu_font, screen, GRAY, u'Return to Game')
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
                    game_screen(screen)
            elif event.type == pygame.MOUSEBUTTONUP:
                buy_food_button.release(event)
                buy_water_button.release(event)
        screen.fill(BLACK)
        buy_food_button.show()
        buy_water_button.show()
        return_to_game_button.show()
        # 绘制宠物属性: food amount, water amount, money
        money_text = menu_font.render(f'Money: {pet.money}', True, WHITE)
        screen.blit(money_text, (500, 100))
        food_text = menu_font.render(f'Food: {pet.food_amount}', True, WHITE)
        screen.blit(food_text, (500, 150))
        water_text = menu_font.render(f'Water: {pet.water_amount}', True, WHITE)
        screen.blit(water_text, (500, 200))
        pygame.display.update()

def game_over_screen(screen):
    from screens.main_menu import main_menu
    game_over_text = menu_font.render(u'Game Over', True, WHITE)
    screen.fill(BLACK)
    screen.blit(game_over_text, (300, 200))
    record_text = menu_font.render(f'Your final hour: {pet.hour}', True, WHITE)
    screen.blit(record_text, (300, 250))
    play_again_button = Button(u'Play Again', (300, 300), menu_font, screen, GRAY, u'Play Again')
    play_again_button.show()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.click(event):
                    pet.reset()
                    screen.fill(BLACK)
                    main_menu(screen)  # 返回游戏主菜单
