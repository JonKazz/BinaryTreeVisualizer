from constants import *
import pygame

class Traversal_Button:
    def __init__(self):
        x_pos = SCREEN_WIDTH - PADDING - 150
        y_pos = PADDING + 90
        height = 80
        width = 150
        
        self.rect = pygame.Rect(x_pos, y_pos, width, height)
        
        self.font = self.font = pygame.font.SysFont('arial', FONT_SIZE-10)
        self.frozen_mode = False
        self.traversal_mode = False


    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def get_text(self):
        if self.traversal_mode:
            return "CLEAR"
        else:
            return "TRAVERSE"

    def draw(self, screen, outline_color):
        text = self.get_text()
        mouse_pos = pygame.mouse.get_pos()
        button_color = GREY if self.frozen_mode else SHADED_WHITE if self.is_hovered(mouse_pos) else WHITE

        pygame.draw.rect(screen, button_color, self.rect)
        pygame.draw.rect(screen, outline_color, self.rect, 3)
        
        text_surface = self.font.render(text, True, outline_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    
            