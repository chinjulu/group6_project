import pygame
import sys
from button import Button
from pet import Pet
import settings_general
from settings_gs import Pet_img
from time import time
import random
from utils import draw_progress_bar, draw_chart, save_record
import json
from screens.shop_screen import open_shop
from screens.setting_screen import setting_screen
from speech_recog import recognize_speech
# from screens.update import animate_images
from screens.music import play_sound_effect
from screens.achievement import achievement
from time import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)


text_color = (255, 255, 255)
outline_color = (0, 0, 0)
outline_thickness = 2
shadow_color = (0, 0, 0)
shadow_offset = (2, 2)


pet = Pet()
game_screen_font = pygame.font.Font(settings_general.font_path, settings_general.game_screen_font_size)

def draw_pet_location(screen, pet, pet_image_path):
    pet.image = pygame.image.load(pet_image_path)
    pet.rect = pet.image.get_rect(topleft=(pet.x, pet.y))
    img_width, img_height = pet.image.get_size()
    screen.blit(pet.image, pet.rect.topleft)
    return img_width, img_height

def draw_pet_attributes(screen,pet, food_button, water_button, achieve_button, speech_recognition_button):
    hungry_text = render_text_with_outline(f'飢餓度', game_screen_font, text_color, outline_color, outline_thickness)
    screen.blit(hungry_text, (25, 0))

    # draw_progress_bar
    draw_progress_bar(screen, 100, 10, 200, 18, (255, 0, 0), pet.hungry_level)

    happy_text = render_text_with_outline(f'快樂度', game_screen_font, text_color, outline_color, outline_thickness)
    screen.blit(happy_text, (25, 25))
    draw_progress_bar(screen, 100, 35, 200, 18, (255, 255, 0), pet.happy_level)

    healthy_text = render_text_with_outline(f'健康度', game_screen_font, text_color, outline_color, outline_thickness)
    screen.blit(healthy_text, (25, 50))
    draw_progress_bar(screen, 100, 60, 200, 18, (0, 255, 0), pet.healthy_level)

    speech_recognition_button.show()
    food_button.show()
    water_button.show()
    achieve_button.show()

def draw_player_info(screen,pet, shop_button, settings_button, play_game_earn_money_button):
    state_text = render_text_with_outline(f'成長階段: {pet.state}', game_screen_font, text_color, outline_color, outline_thickness)
    screen.blit(state_text, (550, 0))

    money_text = render_text_with_outline(f'阿堵物: {pet.money}', game_screen_font, text_color, outline_color, outline_thickness)
    screen.blit(money_text, (550, 25))

    hour_text = render_text_with_outline(f'壽命(hr): {pet.hour}', game_screen_font, text_color, outline_color, outline_thickness)
    screen.blit(hour_text, (550, 50))

    status_text = render_text_with_outline(f'狀態: {pet.status}', game_screen_font, text_color, outline_color, outline_thickness)
    screen.blit(status_text, (550, 75))

    settings_button.show()
    shop_button.show()
    play_game_earn_money_button.show()

def change_direction(pet):
    pet.speed_x = random.choice([-1, 0, 1])
    # pet.speed_y = random.choice([-1, 0, 1])
    pet.update_position()  # Update position after changing direction


def game_screen(screen, pet):
    
    clock = pygame.time.Clock()
    last_update_time = time()
    direction_change_time = time()
    
    food_button = Button(f'食物:{pet.food_amount}', (25, 80), game_screen_font, screen, GRAY, f'食物{pet.food_amount}')
    water_button = Button(f'水:{pet.water_amount}', (25, 110), game_screen_font, screen, GRAY, f'水:{pet.water_amount}')
    achieve_button = Button(u'成就', (25, 140), game_screen_font, screen, GRAY, u'成就')
    
    settings_button = Button(u'設定', (550, 105), game_screen_font, screen, GRAY, u'設定')
    speech_recognition_button = Button(u'說些什麼吧...', (550, 135), game_screen_font, screen, GRAY, u'說些什麼吧...')
    shop_button = Button(u'商店', (550, 165), game_screen_font, screen, GRAY, u'商店')
    play_game_earn_money_button = Button(u'賺錢', (550, 195), game_screen_font, screen, GRAY, u'賺錢')

    pet_image_path = Pet_img.load_images(pet, pet.state)
    happy_pet_image_path = Pet_img.load_images(pet, 'happy')
    sad_pet_image_path = Pet_img.load_images(pet, 'sad')
    listen_to_speech_pet_path = settings_general.listen_to_speech_pet_path
    pet_happy_start_time = 0
    pet_is_happy = False
    pet_sad_start_time = 0
    pet_is_sad = False
    pet_speech_start_time = 0
    pet_is_speeching = False

    change_direction(pet)

    while True:
        import settings_general as settings
        game_background_image = pygame.image.load(settings.game_background_image_path)
        game_background_image = pygame.transform.scale(game_background_image, settings.screen_size)
        screen.blit(game_background_image, (0, 0))

        current_time = time()
        if pet.status == 'dead' or pet.happy_level <= 0 or pet.hungry_level <= 0 or pet.healthy_level <= 0:
            game_over_screen(screen, pet)
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if shop_button.click(event):
                    open_shop(screen, pet)
                    food_button = Button(f'食物:{pet.food_amount}', (25, 80), game_screen_font, screen, GRAY, f'食物{pet.food_amount}')
                    water_button = Button(f'水:{pet.water_amount}', (25, 110), game_screen_font, screen, GRAY, f'水:{pet.water_amount}')
                    achieve_button = Button(u'成就', (25, 140), game_screen_font, screen, GRAY, u'成就')
                    
                    game_background_image = pygame.image.load(settings.game_background_image_path)
                    game_background_image = pygame.transform.scale(game_background_image, settings.screen_size)
                    screen.blit(game_background_image, (0, 0))
                    pygame.display.update()
                    continue
                if food_button.click(event):
                    return_val = pet.feed()
                    eat1_image = pygame.image.load(Pet_img.load_images(pet, 'eat1'))
                    eat2_image = pygame.image.load(Pet_img.load_images(pet, 'eat2'))
                    music_path = "Assets/Bgm/eat.mp3"

                    if return_val != 'no food':
                        play_sound_effect(music_path)
                        animate_images(screen, pet, eat1_image, eat2_image, duration=2, switch_interval=0.2, x=pet.x, y=pet.y)
                        pygame.mixer.music.unpause()

                    food_button = Button(f'食物:{pet.food_amount}', (25, 80), game_screen_font, screen, GRAY, f'食物{pet.food_amount}')
                if water_button.click(event):
                    return_val = pet.drink()
                    drink1_image = pygame.image.load(Pet_img.load_images(pet, 'drink1'))
                    drink2_image = pygame.image.load(Pet_img.load_images(pet, 'drink2'))
                    music_path = "Assets/Bgm/drink.mp3"

                    if return_val != 'no water':
                        play_sound_effect(music_path)
                        animate_images(screen,pet, drink1_image, drink2_image, duration=2, switch_interval=0.2, x=pet.x, y=pet.y)
                        pygame.mixer.music.unpause()

                    water_button = Button(f'水:{pet.water_amount}', (25, 110), game_screen_font, screen, GRAY, f'水:{pet.water_amount}')
                if settings_button.click(event):
                    setting_screen(screen, pet)
                if pet.rect.collidepoint(event.pos):
                    pet.touch_pet()
                    pet_image_path = Pet_img.load_images(pet, 'touch')
                    pet_happy_start_time = current_time
                    pet_is_happy = True
                    music_path = "Assets/Bgm/happy.mp3"
                    play_sound_effect(music_path)
                if speech_recognition_button.click(event):
                    pet_image_path = listen_to_speech_pet_path
                    draw_pet_location(screen,pet, listen_to_speech_pet_path)
                    draw_pet_attributes(screen,pet, food_button, water_button, achieve_button, speech_recognition_button)
                    draw_player_info(screen, pet,shop_button, settings_button, play_game_earn_money_button)
                    pygame.display.update()
                    sentiment, text = recognize_speech()
                    pet_speech_start_time = current_time
                    pet_is_speeching = True
                    if sentiment == 'positive (stars 4 and 5)':
                        pet_is_happy = True
                        pet_happy_start_time = current_time
                        pet_image_path = happy_pet_image_path
                        if "麥當勞" in text:
                            pet.happy_level += 15
                        else:
                            pet.happy_level += 10
                        music_path = "Assets/Bgm/happy.mp3"
                        play_sound_effect(music_path)
                    elif sentiment == 'negative (stars 1, 2 and 3)':
                        if "去讀書" in text:
                            pet.status = 'dead'
                            pet.happy_level = 0
                        
                        pet.happy_level -= 10
                        pet_is_sad = True
                        pet_sad_start_time = current_time
                        pet_image_path = sad_pet_image_path
                        music_path = "Assets/Bgm/cry.mp3"
                        play_sound_effect(music_path)

                    continue
                if achieve_button.click(event):
                    achievement()
                if play_game_earn_money_button.click(event):
                    play_game(screen, pet)
                    play_game_earn_money_button = Button(u'賺錢', (550, 195), game_screen_font, screen, GRAY, u'賺錢')
            elif event.type == pygame.MOUSEBUTTONUP:
                speech_recognition_button.release(event)
                shop_button.release(event)
                food_button.release(event)
                water_button.release(event)

        draw_pet_location(screen,pet, pet_image_path)
        draw_pet_attributes(screen, pet,food_button, water_button, achieve_button, speech_recognition_button)
        draw_player_info(screen,pet, shop_button, settings_button, play_game_earn_money_button)
        current_time = time()
        #if pet is happy
        if pet_is_happy and current_time - pet_happy_start_time >= 3:
            # music_path = "Assets/Bgm/happy.mp3"
            # play_sound_effect(music_path)
            pet_image_path = Pet_img.load_images(pet, pet.state)
            pygame.mixer.music.unpause()
            pet_is_happy = False
        #if pet is sad
        if pet_is_sad and current_time - pet_sad_start_time >= 3:
            # music_path = "Assets/Bgm/cry.mp3"
            # play_sound_effect(music_path)
            pet_image_path = Pet_img.load_images(pet, pet.state)
            pygame.mixer.music.unpause()
            pet_is_sad = False
        if pet_is_speeching and current_time - pet_speech_start_time >= 3:
            pet_image_path = Pet_img.load_images(pet, pet.state)
            pet_is_speeching = False
        if current_time - direction_change_time >= 2:
            change_direction(pet)
            direction_change_time = current_time
        if current_time - last_update_time >= 1:
            # print(1)
            pet.update_hour()
            # print(pet.hour)
            # print(pet.hungry_level)
            last_update_time = current_time

        if current_time - last_update_time >= 0.5 and current_time - last_update_time <= 0.55 or \
           current_time - last_update_time >= 0.95 and current_time - last_update_time <= 1:
            pet.x += pet.speed_x
            pet.y += pet.speed_y
            # print(pet.speed_x, pet.speed_y)
            pet.update_position()
            # change_direction(pet)

        #check if pet is out of screen
        if pet.x < 0:
            pet.x = 0
            change_direction(pet)
        elif pet.x > game_background_image.get_width() - pet.rect.width:
            pet.x = game_background_image.get_width() - pet.rect.width
            change_direction(pet)

        if pet.y < 0:
            pet.y = 0
            change_direction(pet)
        elif pet.y > game_background_image.get_height() - pet.rect.height:
            pet.y = game_background_image.get_height() - pet.rect.height
            change_direction(pet)


        # pet.move()
        # pet.x = max(0, min(pet.x, settings.screen_size[0] - pet.rect.width))
        # pet.y = max(0, min(pet.y, settings.screen_size[1] - pet.rect.height))
        pet.update_position()
        pygame.display.update()
        # clock.tick(60)

def game_over_screen(screen):
    import settings_general as settings
    font = pygame.font.Font(settings.font_path, 100)
    text_surface = font.render("Game Over", True, (255, 0, 0))
    screen.blit(text_surface, (200, 200))
    pygame.display.flip()
    pygame.time.wait(3000)
    sys.exit()
    
def show_leaderboard_with_chart(screen, pet):
    try:
        with open('leaderboard.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    screen.fill(BLACK)
    title_text = game_screen_font.render('Leaderboard', True, WHITE)
    screen.blit(title_text, (300, 50))

    if data:
        draw_chart(screen, data)
    else:
        no_data_text = game_screen_font.render('No data available', True, WHITE)
        screen.blit(no_data_text, (300, 200))

    return_button = Button('Return', (300, 500), game_screen_font, screen, GRAY, 'Return')
    return_button.show()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.click(event):
                    game_over_screen(screen,pet)
                    return
            elif event.type == pygame.MOUSEBUTTONUP:
                return_button.release(event)

def game_over_screen(screen,pet):
    import settings_general as settings
    from screens.main_menu import main_menu

    game_over_text = render_text_with_outline(f'{pet.name}死亡...！', game_screen_font, text_color, outline_color, outline_thickness)
    screen.fill(BLACK)
    screen.blit(game_over_text, (300, 200))
    record_text = game_screen_font.render(f'{pet.name} 壽命: {pet.hour}', True, WHITE)
    screen.blit(record_text, (300, 250))
    play_again_button = Button(u'再玩一次', (300, 300), game_screen_font, screen, GRAY, u'再玩一次')
    leaderboard_button = Button(u'排行榜', (300, 350), game_screen_font, screen, GRAY, u'排行榜')
    play_again_button.show()
    leaderboard_button.show()
    pygame.display.update()

    save_record(pet.get_summary())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.click(event):
                    pet.reset()
                    screen.fill(BLACK)
                    main_menu(screen)
                if leaderboard_button.click(event):
                    show_leaderboard_with_chart(screen,pet)
            elif event.type == pygame.MOUSEBUTTONUP:
                play_again_button.release(event)
                leaderboard_button.release(event)


def play_game(screen, pet):
    # if pet.gender == 'male':
    #     import Final_pj.settings_gs as settings
    # else:
    #     import settings_female as settings
    import settings_general as settings
    paddle_image = pygame.image.load(settings.paddle_image_path)
    paddle_image = pygame.transform.scale(paddle_image, (100, 100))
    paddle_rect = paddle_image.get_rect()
    paddle_rect.topleft = (screen.get_width() // 2 - paddle_rect.width // 2, screen.get_height() - paddle_rect.height - 10)

    ball_radius = 10

    ball = pygame.Rect(screen.get_width() // 2, screen.get_height() // 2, ball_radius * 2, ball_radius * 2)
    font = pygame.font.SysFont(None, 36)
    last_score_time = time()
    # def ball_game_main():
        # global ball_speed_x, ball_speed_y, score
    ball_speed_x = 5
    ball_speed_y = -5
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            paddle_rect.x -= 10
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            paddle_rect.x += 10
        # if keys[pygame.K_UP] or keys[pygame.K_w]:
        #     paddle_rect.y -= 10
        # if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        #     paddle_rect.y += 10

        # 防止球拍移出屏幕
        if paddle_rect.left < 0:
            paddle_rect.left = 0
        if paddle_rect.right > screen.get_width():
            paddle_rect.right = screen.get_width()
        if paddle_rect.top < 0:
            paddle_rect.top = 0
        if paddle_rect.bottom > screen.get_height():
            paddle_rect.bottom = screen.get_height()

        # 球移动
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # 碰到左右墙壁
        if ball.left <= 0 or ball.right >= screen.get_width():
            ball_speed_x = -ball_speed_x

        # 碰到顶部墙壁
        if ball.top <= 0:
            ball_speed_y = -ball_speed_y

        if (ball.colliderect(paddle_rect) and
            ball.bottom >= paddle_rect.top and
            ball.bottom <= paddle_rect.top + 5 and  # Ensure it's hitting near the top edge
            ball_speed_y > 0):  # Ensure the ball is moving downwards

            ball_speed_y = -ball_speed_y

            # Score cooldown to prevent rapid scoring
            current_time = time()
            if current_time - last_score_time > 0.1:  # 0.1 seconds cooldown
                pet.money += 1
                last_score_time = current_time

        # Ball falls to the bottom
        if ball.top >= screen.get_height():
            running = False
            ball_game_over_screen(screen, pet, font)

        ball_draw_objects(screen, paddle_image, paddle_rect, ball, font, pet)
        clock.tick(60)
def ball_draw_objects(screen, paddle_image, paddle_rect, ball, font, pet):
    import settings_general as settings
    game_background_image = pygame.image.load(settings.game_background_image_path)
    game_background_image = pygame.transform.scale(game_background_image, settings.screen_size)
    screen.blit(game_background_image, (0, 0))    
    screen.blit(paddle_image, paddle_rect.topleft)
    pygame.draw.ellipse(screen, (0,0,255), ball)
    score_text = render_text_with_outline(f"money: {pet.money}", game_screen_font, text_color, outline_color, outline_thickness)

    screen.blit(score_text, (10, 10))
    pygame.display.flip()

def ball_game_over_screen(screen, pet, font):
    # game_over_text = font.render(u'Game Over', True, WHITE)
    game_over_text = render_text_with_outline(f'Game Over', game_screen_font, text_color, outline_color, outline_thickness)
    screen.fill(BLACK)
    screen.blit(game_over_text, (300, 200))
    record_text = render_text_with_outline(f'錢錢: {pet.money}', game_screen_font, text_color, outline_color, outline_thickness)
    screen.blit(record_text, (300, 250))
    play_again_button = Button(u'再玩一次', (300, 300), game_screen_font, screen, GRAY, u'再玩一次')
    return_button = Button(u'回上頁', (300, 350), game_screen_font, screen, GRAY, u'回上頁')
    # leaderboard_button = Button(u'Leaderboard', (300, 400), font, screen, GRAY, u'Leaderboard')
    return_button.show()
    play_again_button.show()
    pygame.display.update()

    # save_record(pet.get_summary())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.click(event):
                    # pet.reset()
                    screen.fill(BLACK)
                    play_game(screen, pet)
                    # main()
                # if leaderboard_button.click(event):
                #     show_leaderboard_with_chart(screen)
                if return_button.click(event):
                    game_screen(screen, pet)

            elif event.type == pygame.MOUSEBUTTONUP:
                play_again_button.release(event)
                # leaderboard_button.release(event)


def animate_images(screen,pet, img1, img2, duration=2, switch_interval=0.2, x = pet.x, y = pet.y):
    start_time = time()
    last_switch_time = start_time
    current_image = img1
    food_button = Button(f'食物:{pet.food_amount}', (25, 80), game_screen_font, screen, GRAY, f'食物{pet.food_amount}')
    water_button = Button(f'水:{pet.water_amount}', (25, 110), game_screen_font, screen, GRAY, f'水:{pet.water_amount}')
    achieve_button = Button(u'成就', (25, 140), game_screen_font, screen, GRAY, u'成就')
    
    settings_button = Button(u'設定', (550, 105), game_screen_font, screen, GRAY, u'設定')
    speech_recognition_button = Button(u'說些什麼吧...', (550, 135), game_screen_font, screen, GRAY, u'說些什麼吧...')
    shop_button = Button(u'商店', (550, 165), game_screen_font, screen, GRAY, u'商店')
    play_game_earn_money_button = Button(u'賺錢', (550, 195), game_screen_font, screen, GRAY, u'賺錢')
    draw_pet_attributes(screen, pet, food_button, water_button, achieve_button, speech_recognition_button)
    draw_player_info(screen, pet, shop_button, settings_button, play_game_earn_money_button)
    
    while True:
        current_time = time()
        
        # 检查是否需要停止动画
        if current_time - start_time > duration:
            # pygame.mixer.music.unpause()
            break
        
        # 检查是否需要切换图片
        if current_time - last_switch_time >= switch_interval:
            last_switch_time = current_time
            current_image = img2 if current_image == img1 else img1
        
        
        screen.blit(current_image, (x, y))
        
        # 更新显示
        pygame.display.flip()
        

        # 检查退出事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


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

def render_text_with_shadow(text, font, text_color, shadow_color, shadow_offset):
    # Render the shadow text
    shadow_surface = font.render(text, True, shadow_color)
    text_surface = font.render(text, True, text_color)

    width = text_surface.get_width() + abs(shadow_offset[0])
    height = text_surface.get_height() + abs(shadow_offset[1])

    # Create a new surface with the desired dimensions
    surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
    surface = surface.convert_alpha()

    # Draw the shadow text
    surface.blit(shadow_surface, shadow_offset)

    # Draw the original text on top of the shadow
    surface.blit(text_surface, (0, 0))

    return surface
    #function call
    #text_surface = render_text_with_shadow(text, font, text_color, shadow_color, shadow_offset)