from constants import *
from ui.mode_manager import ModeManager
import pygame

class Preorder_Button:
    def __init__(self):
        x_pos = SCREEN_WIDTH - PADDING - 115
        y_pos = PADDING + 90
        height = 40
        width = 115
        
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        self.font = self.font = pygame.font.SysFont('arial', FONT_SIZE-21)
        self.mode = ModeManager()


    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def draw(self, screen, outline_color):
        mouse_pos = pygame.mouse.get_pos()
        button_color = GREY if self.mode == "frozen" else SHADED_WHITE if self.is_hovered(mouse_pos) else WHITE

        pygame.draw.rect(screen, button_color, self.rect)
        pygame.draw.rect(screen, outline_color, self.rect, 3)
        
        text_surface = self.font.render("PREORDER", True, outline_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    
            