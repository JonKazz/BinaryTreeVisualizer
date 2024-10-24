from constants import *
from ui.mode_manager import ModeManager
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
        self.mode = ModeManager()


    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


    def draw(self, screen, outline_color):
        mouse_pos = pygame.mouse.get_pos()
        button_color = GREY if self.mode == "frozen" or self.mode == "traversal" else SHADED_WHITE if self.is_hovered(mouse_pos) else WHITE

        pygame.draw.rect(screen, button_color, self.rect)
        pygame.draw.rect(screen, outline_color, self.rect, 3)
        
        text_surface = self.font.render(self.text, True, outline_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    
            