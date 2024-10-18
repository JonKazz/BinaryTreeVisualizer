from constants import *
import pygame

class Node_Edit_Button:
    def __init__(self, font, node):        
        self.increment_box = self.create_increment_box(node)
        # self.exit_box = pygame.Rect(node.coordinate[0], node.coordinate[1], )
        self.font = font
        self.default_color = WHITE
        self.hover_color = SHADED_WHITE


    def create_increment_box(self, node):
        x_pos = node.coordinate[0]
        y_pos = node.coordinate[1]
        width = NODE_SIZE
        height = NODE_SIZE * 2
        
        return pygame.Rect(x_pos, y_pos, width, height)


    def is_hovered(self, mouse_pos, rect):
        return rect.collidepoint(mouse_pos)


    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.increment_box)
        pygame.draw.rect(screen, BLACK, self.increment_box, 3)

    
            