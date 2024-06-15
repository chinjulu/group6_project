# from time import time
import pygame
import sys
# import settings
from time import time
from button import Button

class Pet:
    def __init__(self):
        self.hour = 0  # 寵物活了幾小時
        self.status = 'hungry'  # 寵物狀態（hungry, full）
        self.hungry_level = 50  # 飢餓程度（0-100%）
        self.happy_level = 100  # 快樂程度（0-100%）
        self.healthy_level = 50  # 健康程度（0-100%）
        self.state = 'baby'  # 寵物狀態（baby, teens, adult）
        self.food_amount = 2  # 玩家擁有的食物數量
        self.water_amount = 2  # 玩家擁有的水數量
        self.money = 100  # 玩家擁有的金錢數量
        self.time_since_last_hour = 0  # 距离上次小时的时间
        self.x = 200
        self.y = 400
        self.speed_x = 1
        self.speed_y = 0
        self.name = ''
        self.gender = None
        # if self.gender == 'male':
        #     import settings_male as settings
        # else:
        #     import settings_female as settings
        # Assuming an initial size for the pet's image
        # self.image = pygame.image.load(settings.baby_pet_image_path)

        from settings_gs import Pet_img
        self.image = pygame.image.load(Pet_img.load_images(self, 'baby'))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update_position(self):
        self.rect.topleft = (self.x, self.y)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        print(self.x, self.y)
        self.update_position()


    def update_hour(self):
        self.time_since_last_hour += 1
        if self.time_since_last_hour <= 9:  # 每3秒钟更新一次hour
            self.hour += 1
            if self.time_since_last_hour == 3 or self.time_since_last_hour == 6 or self.time_since_last_hour == 9:
                # self.hungry_level -= 10
                if self.state == 'baby':
                    self.hungry_level -= 5
                elif self.state == 'teen':
                    self.hungry_level -= 10
                else:
                    self.hungry_level -= 15
            if self.time_since_last_hour == 5 or self.time_since_last_hour == 0:
                self.happy_level -= 5
            if self.time_since_last_hour == 7:
                self.healthy_level -= 5
                
        else:
            self.time_since_last_hour = 0

        # 根据hour更改state
        if self.hour < 50:
            self.state = 'baby'
        elif self.hour < 150:
            self.state = 'teen'
        else:
            self.state = 'adult'

        # 更新status
        if self.hungry_level <= 0:
            self.status = 'dead'
        elif self.hungry_level <= 10:
            self.status = 'starving'
        elif self.hungry_level <= 20:
            self.status = 'hungry'
        else:
            self.status = 'full'


    def feed(self):
        if self.food_amount > 0:
            self.food_amount -= 1
            if self.hungry_level < 100:
                if (self.hungry_level + 10) > 100:
                    self.hungry_level = 100
                else:
                    self.hungry_level += 10
            else:
                self.hungry_level = 100

            if self.happy_level < 100:
                if (self.happy_level + 5) > 100:
                    self.happy_level = 100
                else:
                    self.happy_level += 5
            else:
                self.happy_level = 100

            if self.healthy_level < 100:
                if (self.healthy_level + 5) > 100:
                    self.healthy_level = 100
                else:
                    self.healthy_level += 5
            else:
                self.healthy_level = 100
            return "success"
        else:
            return "no food"
    def drink(self):
        if self.water_amount > 0:
            self.water_amount -= 1
                
            if self.happy_level < 100:
                if (self.happy_level + 5) > 100:
                    self.happy_level = 100
                else:
                    self.happy_level += 5
            else:
                self.happy_level = 100

            if self.healthy_level < 100:
                if (self.healthy_level + 10) > 100:
                    self.healthy_level = 100
                else:
                    self.healthy_level += 10
            else:
                self.healthy_level = 100
            return "success"
        else:
            return "no water"
    def buy_food(self):
        if self.money >= 3:
            self.money -= 3
            self.food_amount += 1

    def buy_water(self):
        if self.money >= 1:
            self.money -= 1
            self.water_amount += 1
    
    def touch_pet(self):
        if self.happy_level < 100:
            if (self.happy_level + 5) > 100:
                self.happy_level = 100
            else:
                self.happy_level += 5
        else:
            self.happy_level = 100
    
    def reset(self):
        self.hour = 0  # 寵物活了幾小時
        self.status = 'hungry'  # 寵物狀態（hungry, full）
        self.hungry_level = 50  # 飢餓程度（0-100%）
        self.happy_level = 100  # 快樂程度（0-100%）
        self.healthy_level = 50  # 健康程度（0-100%）
        self.state = 'baby'  # 寵物狀態（baby, teens, adult）
        self.food_amount = 2  # 玩家擁有的食物數量
        self.water_amount = 2  # 玩家擁有的水數量
        self.money = 100  # 玩家擁有的金錢數量
        self.time_since_last_hour = 0  # 距离上次小时的时间
        self.x = 200
        self.y = 400
        self.speed_x = 1
        self.speed_y = 0
        self.name = ''
        self.gender = ''
    def get_summary(self):
        return {
            'hour': self.hour,
            'hungry_level': self.hungry_level,
            'happy_level': self.happy_level,
            'healthy_level': self.healthy_level,
        }