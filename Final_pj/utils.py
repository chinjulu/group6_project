import json
import pygame
import settings_general as settings

menu_font = pygame.font.Font(settings.font_path, settings.menu_font_size)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

def draw_progress_bar(screen, x, y, width, height, color, percentage):
    pygame.draw.rect(screen, BLACK, (x, y, width+1, height+1))
    pygame.draw.rect(screen, color, (x, y, width * percentage / 100, height))


def draw_chart(screen, data):
    if not data:
        return
    
    chart_rect = pygame.Rect(50, 100, 700, 400)
    pygame.draw.rect(screen, WHITE, chart_rect, 2)

    max_hour = max(record['hour'] for record in data)
    
    # 绘制纵坐标和刻度线
    num_ticks = 10
    tick_interval = max_hour / num_ticks
    for i in range(num_ticks + 1):
        y = chart_rect.y + chart_rect.height - (i * chart_rect.height // num_ticks)
        hour_value = i * tick_interval
        tick_text = menu_font.render(f'{hour_value:.1f}', True, WHITE)
        screen.blit(tick_text, (chart_rect.x - 50, y - 10))
        pygame.draw.line(screen, WHITE, (chart_rect.x - 5, y), (chart_rect.x, y), 2)

    for i, record in enumerate(data):
        x = chart_rect.x + (i * chart_rect.width // len(data))
        hour_height = chart_rect.height * record['hour'] // max_hour

        pygame.draw.rect(screen, (0, 0, 255), (x, chart_rect.y + chart_rect.height - hour_height, 20, hour_height))

    
    
def save_record(record, file_path='leaderboard.json'):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(record)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
