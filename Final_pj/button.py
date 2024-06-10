import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

class Button:
    def __init__(self, text, pos, font, bg=GRAY, feedback=''):
        self.x, self.y = pos
        self.font = font
        self.screen = pygame.display.get_surface()  # Get the screen surface
        if feedback == '':
            self.feedback = text
        else:
            self.feedback = feedback
        self.original_text = text  # 保存原始文本
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
            self.change_text(self.original_text, GRAY)
            return True
        return False
