import pygame
import math
from constants import *
from nodes.node import Node
from nodes.node_operations import is_hovered


class NodeVisualizer:
    def __init__(self, node, font, border_width, border_color, edit_mode):
        self.node = node
        self.size = NODE_SIZE
        self.font = font
        self.default_color = WHITE
        self.hover_color = SHADED_WHITE
        self.border_color = border_color
        self.border_width = border_width
        self.edit_mode = edit_mode
    
        
    def draw(self, screen) -> None:
        mouse_pos = pygame.mouse.get_pos()
        hovered = is_hovered(self.node, mouse_pos)
        
        if not self.node.is_empty or (self.node.is_empty and self.edit_mode):
            if self.node.is_empty:
                node_color = SHADED_GREEN if self.edit_mode and hovered else LIGHT_GREEN
                text = "+"
            else:
                node_color = SHADED_WHITE if self.edit_mode and hovered else WHITE
                text = "?" if self.edit_mode and hovered else str(self.node.val)

            pygame.draw.circle(screen, node_color, self.node.coordinate, self.size)
            pygame.draw.circle(screen, self.border_color, self.node.coordinate, self.size, self.border_width)

            text_surface = self.font.render(text, True, BLACK)
            text_rect = text_surface.get_rect(center=self.node.coordinate)
            screen.blit(text_surface, text_rect)


    