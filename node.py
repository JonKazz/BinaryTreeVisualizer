import pygame
import math
from constants import *


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.coordinate = None
        self.is_empty = False if val else True


class NodeVisualizer:
    def __init__(self, node, font, size, border_width, border_color, edit_mode):
        self.node = node
        self.size = size
        self.font = font
        self.default_color = WHITE
        self.hover_color = LIGHT_GRAY
        self.border_color = border_color
        self.border_width = border_width
        self.edit_mode = edit_mode
        

    def is_mouse_over_node(self, mouse_pos):
        distance = math.sqrt((mouse_pos[0] - self.node.coordinate[0]) ** 2 + (mouse_pos[1] - self.node.coordinate[1]) ** 2)
        return distance <= self.size


    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.edit_mode and self.is_mouse_over_node(mouse_pos):
            node_color = self.hover_color
            text = "?"
        else:
            node_color = self.default_color
            text = str(self.node.val)
        
        
        if not self.node.is_empty:
            self.draw_node(screen, node_color, text)
    
    
    def draw_node(self, screen, node_color, text):
        pygame.draw.circle(screen, node_color, self.node.coordinate, self.size)
        pygame.draw.circle(screen, self.border_color, self.node.coordinate, self.size, self.border_width)

        text_surface = self.font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.node.coordinate)
        screen.blit(text_surface, text_rect)
