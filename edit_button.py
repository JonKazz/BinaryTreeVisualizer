from constants import *
import pygame

class Edit_Button:
    def __init__(self, x_pos, y_pos, width, height, text, font):
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.text = text
        self.font = font
        self.default_color = WHITE
        self.hover_color = LIGHT_GRAY



    def draw(self, screen, outline_color):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            button_color = self.hover_color
        else:
            button_color = self.default_color

        pygame.draw.rect(screen, button_color, self.rect)
        pygame.draw.rect(screen, outline_color, self.rect, 3)
        
        text_surface = self.font.render(self.text, True, outline_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                return True
        return False