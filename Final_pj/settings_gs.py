import pygame
# from pet import Pet

pygame.init()

# 延遲導入 繼承Pet
class Pet_img():
    def __init__(self):
        from pet import Pet
        self.pet = Pet()
        self.images = self.load_images()

    def load_images(self, index):
        # 加載圖片
        img_Paths =f"Assets/img/pet/{self.gender}/{self.state}/{index}.png"
        return img_Paths


# # import pygame
# # from pet import Pet
# # pygame.font.init()

# # menu_background_image_path = "Assets/img/background/Resized/bamboo background.jpg"
# # screen_size = (800, 600)
# # font_path = "Assets\_font\HanyiSentyPagoda Regular.ttf"
# # menu_font_size = 36
# # game_background_image_path = "Assets\img/background\game bkg.jpg"
# # shop_background_image_path = "Assets\img/background/shop bkg.jpg"
# # leaderboard_json_path = "leaderboard.json"

# # baby_male_pet_image_path = "Assets\img\pet re.png"
# # baby_female_pet_image_path = "Assets\img\pet re.png"

# # baby_male_eat1_image_path = "Assets/img/pet/boy eat1.png"
# # baby_female_eat2_image_path = "Assets/img/pet/boy eat2.png"

# # teen_male_pet_image_path = "Assets\img\Resized\menu_background.jpg"
# # teen_female_pet_image_path = "Assets\img\Resized\menu_background.jpg"

# # adult_male_pet_image_path = "Assets\img\Resized\menu_background.jpg"
# # adult_female_pet_image_path = "Assets\img\Resized\menu_background.jpg"

# # happy_male_pet_image_path = "Assets\img\Resized\Male.jpg"
# # happy_female_pet_image_path = "Assets\img\Resized\Male.jpg"

# # sad_male_pet_image_path = "Assets\img\Resized\Female.jpg"
# # sad_female_pet_image_path = "Assets\img\Resized\Female.jpg"

# # listen_to_speech_pet_path = "Assets\img\Resized\menu_background.jpg"
# # paddle_image_path = "Assets\img\playing.png"

# import pygame
# pygame.font.init()
# menu_background_image_path = "Assets/img/background/Resized/bamboo background.jpg"
# screen_size = (800, 600)
# font_path = "Assets\_font\HanyiSentyPagoda Regular.ttf"
# menu_font_size = 36
# game_background_image_path = "Assets\img/background\game bkg.jpg"
# shop_background_image_path = "Assets\img/background/shop bkg.jpg"
# baby_pet_image_path = "Assets\img\pet re.png"
# baby_eat1_image_path = "Assets/img/pet/boy eat1.png"
# baby_eat2_image_path = "Assets/img/pet/boy eat2.png"
# teen_pet_image_path = "Assets\img\Resized\menu_background.jpg"
# adult_pet_image_path = "Assets\img\Resized\menu_background.jpg"
# happy_pet_image_path = "Assets\img\Resized\Male.jpg"
# sad_pet_image_path = "Assets\img\Resized\Female.jpg"
# leaderboard_json_path = "leaderboard.json"
# listen_to_speech_pet_path = "Assets\img\Resized\menu_background.jpg"
# paddle_image_path = "Assets\img\playing.png"