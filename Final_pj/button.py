import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

class Button:
    def __init__(self, text, pos, font,screen, bg=GRAY, feedback=''):
        self.x, self.y = pos
        self.font = font
        self.screen = screen
        if screen is None:
            print("Error: Screen is None!!", text)
        else:
            pass
            # print(screen , " is not None", text)

        if self.screen is None:
            print("Error: Screen is None!")
        if feedback == '':
            self.feedback = text
        else:
            self.feedback = feedback
        self.original_text = text  # 保存原始文本
        self.original_bg = bg
        self.change_text(text, bg)


    def change_text(self, text, bg=GRAY):
        self.rendered_text = self.font.render(text, True, WHITE)
        self.size = self.rendered_text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.rendered_text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.bg = bg

    def show(self):
        self.screen.blit(self.surface, (self.x, self.y))  # Blit the button surface onto the screen

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.change_text(self.feedback, BLACK)
                return True
        return False

    def release(self, event):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            self.change_text(self.original_text, self.original_bg)
            return True
        return False

class img_Button:
    def __init__(self, text, pos, font, screen, bg_image_path=None, feedback=''):
        self.x, self.y = pos
        self.font = font
        self.screen = screen
        self.bg_image_path = bg_image_path
        self.bg_image = pygame.image.load(bg_image_path) if bg_image_path else None
        pygame.transform.scale(self.bg_image, (200, 200))
        self.original_text = text
        self.feedback = feedback if feedback else text
        self.change_text(text)
        # self.size = (200, 200)
        # if self.bg_image_path:
        #     self.bg_image = pygame.image.load(bg_image_path)
        #     self.bg_image = pygame.transform.scale(self.bg_image, self.size)  # 缩放背景图片
        # else:
        #     self.bg_image = None

    def change_text(self, text):
        self.rendered_text = self.font.render(text, True, WHITE)
        self.size = self.rendered_text.get_size()
        # self.text_rect = self.rendered_text.get_rect(center=(self.size[0] // 2, self.size[1] // 2))
        if self.bg_image:
            self.surface = pygame.transform.scale(self.bg_image, self.size)
        else:
            self.surface = pygame.Surface(self.size)
            self.surface.fill(GRAY)
        self.surface.blit(self.rendered_text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def show(self):
        self.screen.blit(self.surface, (self.x, self.y))

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.change_text(self.feedback)
                return True
        return False

    def release(self, event):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            self.change_text(self.original_text)
            return True
        return False
