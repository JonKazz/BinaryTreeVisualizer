from constants import *
import pygame

class Edit_Button:
    def __init__(self, font):
        x_pos = SCREEN_WIDTH - PADDING - 150
        y_pos = PADDING
        height = 80
        width = 150
        
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        
        self.text = "EDIT"
        self.font = font
        self.default_color = WHITE
        self.hover_color = SHADED_WHITE

    def draw(self, screen, outline_color):
        mouse_pos = pygame.mouse.get_pos()
        if self.is_hovered(mouse_pos):
            button_color = self.hover_color
        else:
            button_color = self.default_color

        pygame.draw.rect(screen, button_color, self.rect)
        pygame.draw.rect(screen, outline_color, self.rect, 3)
        
        text_surface = self.font.render(self.text, True, outline_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
    
            