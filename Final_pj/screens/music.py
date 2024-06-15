import pygame
import sys

# 初始化 Pygame
pygame.init()
background_music_path = "Assets/Bgm/bl cut.mp3"

def play_background_music(background_music_path):
    pygame.mixer.init()
    pygame.mixer.music.load(background_music_path)
    pygame.mixer.music.play(-1)  # 循环播放背景音乐

def play_sound_effect(sound_effect_path = None):
    if sound_effect_path is None:
        return
    else:
        
        sound_effect = pygame.mixer.Sound(sound_effect_path)
        sound_effect.play()
    # while pygame.mixer.get_busy():
    #     pygame.time.wait(100)  # 等待音效播放完毕

def sound_effects(play, sound_effect_path = None):
    # play_background_music(background_music_path)
    while True:
        if play:
            play_sound_effect(sound_effect_path)
            # pygame.mixer.music.unpause()  # 继续播放背景音乐
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()