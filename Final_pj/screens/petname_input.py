import pygame
import sys
from button import Button
import settings_general as settings
from pet import Pet
import time
import tkinter as tk

pet = Pet()
pygame.init()

pygame.display.set_caption("幫你的小寶貝取名字吧")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
LIGHTGRAY = (211, 211, 211)

font = pygame.font.Font(settings.font_path, settings.menu_font_size)

# 初始化输入框内容
user_text = ''
input_active = False

# 创建输入框和确认按钮
input_box = pygame.Rect(250, 200, 300, 50)
confirm_button = pygame.Rect(350, 300, 100, 50)
def handle_chinese_input(initial_text=''):
    def on_confirm():
        global user_text
        user_text = entry.get()
        root.destroy()  # 销毁 Tkinter 窗口

    root = tk.Tk()
    root.title("中文輸入")

    label = tk.Label(root, text="請輸入寵物名稱：", font=("Arial", 18))
    label.pack(pady=10)

    entry = tk.Entry(root, font=("Arial", 16))
    entry.insert(0, initial_text)  # 在输入框中插入初始文本
    entry.pack(pady=10)

    confirm_button = tk.Button(root, text="確定", font=("Arial", 16), command=on_confirm)
    confirm_button.pack(pady=10)

    root.mainloop()


def petname(screen, pet):
    last_blink_time = time.time()
    cursor_visible = True
    global user_text, input_active
    user_text = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    input_active = True
                    handle_chinese_input(user_text)  # 调用 Tkinter 处理中文输入，并传入当前已输入的文字
                    pet.name = user_text
                else:
                    input_active = False
                if confirm_button.collidepoint(event.pos):
                    print(f"愛寵名: {pet.name}")
                    return True
            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        print(f"愛寵名: {user_text}")
                        user_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode
        
        current_time = time.time()
        if current_time - last_blink_time >= 0.5:  # 光标每0.5秒闪烁一次
            cursor_visible = not cursor_visible
            last_blink_time = current_time

        # 绘制输入框和确认按钮
        pygame.draw.rect(screen, WHITE, (230, 180, 350, 200))
        pygame.draw.rect(screen, LIGHTGRAY if input_active else GRAY, input_box)
        pygame.draw.rect(screen, GRAY, confirm_button)
        
        # 绘制按钮文字
        confirm_text = font.render('確認', True, BLACK)
        screen.blit(confirm_text, (confirm_button.x + 20, confirm_button.y + 10))
        
        # 绘制输入框内容
        text_surface = font.render(user_text, True, BLACK)
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))
        
        # 绘制光标
        if cursor_visible and input_active:
            cursor_x = input_box.x + 10 + text_surface.get_width() + 2
            cursor_y = input_box.y + 10
            cursor_height = font.get_height()
            pygame.draw.line(screen, BLACK, (cursor_x, cursor_y), (cursor_x, cursor_y + cursor_height), 2)
        
        # 更新显示
        pygame.display.flip()