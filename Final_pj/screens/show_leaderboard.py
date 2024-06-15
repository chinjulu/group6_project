import pygame
import sys
from button import Button
import json
import settings_general as settings

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)
menu_font = pygame.font.Font(settings.font_path, settings.menu_font_size)

def show_leaderboard(screen):
    scroll_offset = 0  # 用于记录滚动偏移量
    scroll_speed = 20  # 滚动速度

    screen.fill(BLACK)
    title_text = menu_font.render('Leaderboard', True, WHITE)
    screen.blit(title_text, (300, 50))
    return_button = Button('Return', (300, 500), menu_font, screen, GRAY, 'Return')
    return_button.show()
    pygame.display.update()

    while True:
        try:
            with open(settings.leaderboard_json_path, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        screen.fill(BLACK)  # 清空屏幕
        screen.blit(title_text, (300, 50))  # 重新绘制标题

        # 计算内容高度
        content_height = 100 + len(data) * 50

        y_offset = 100 - scroll_offset  # 基于滚动偏移量调整起始y位置

        for record in data:
            # 仅显示在可见区域内的记录
            if 100 <= y_offset <= 450:  # 确保文字在标题下方并在Return按钮上方显示
                record_text = menu_font.render(f"Hour: {record['hour']}, Hungry: {record['hungry_level']}, Happy: {record['happy_level']}, Healthy: {record['healthy_level']}", True, WHITE)
                screen.blit(record_text, (50, y_offset))
            y_offset += 50
        return_button.show()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.click(event):
                    screen.fill(BLACK)
                    return
            elif event.type == pygame.MOUSEBUTTONUP:
                return_button.release(event)
            elif event.type == pygame.MOUSEWHEEL:  # 捕获鼠标滚轮事件
                scroll_offset += event.y * scroll_speed  # 调整滚动偏移量，乘以20以增加滚动速度
                max_scroll_offset = min(0, 500 - content_height)  # 限制最大滚动偏移量
                scroll_offset = max(max_scroll_offset, scroll_offset)  # 限制滚动范围
                if(scroll_offset < 0):
                    scroll_offset = 0

        pygame.display.update()
