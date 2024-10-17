import pygame
import math
from constants import *


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.coordinate = None
        self.is_empty = True if val is None else False
        
    def fill(self, val):
        self.val = val
        self.is_empty = False
        self.left = Node(None)
        self.right = Node(None)
    


class NodeVisualizer:
    def __init__(self, node, font, size, border_width, border_color, edit_mode):
        self.node = node
        self.size = size
        self.font = font
        self.default_color = WHITE
        self.hover_color = SHADED_WHITE
        self.border_color = border_color
        self.border_width = border_width
        self.edit_mode = edit_mode
        

    def is_mouse_over_node(self, mouse_pos):
        distance = math.sqrt((mouse_pos[0] - self.node.coordinate[0]) ** 2 + (mouse_pos[1] - self.node.coordinate[1]) ** 2)
        return distance <= self.size
    

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        if not self.node.is_empty or (self.node.is_empty and self.edit_mode):
            if self.node.is_empty:
                node_color = SHADED_GREEN if self.edit_mode and self.is_mouse_over_node(mouse_pos) else LIGHT_GREEN
                text = "+"
            else:
                node_color = SHADED_WHITE if self.edit_mode and self.is_mouse_over_node(mouse_pos) else WHITE
                text = "?" if self.edit_mode and self.is_mouse_over_node(mouse_pos) else str(self.node.val)

            self.draw_node(screen, node_color, text)


    def draw_node(self, screen, node_color, text):
        pygame.draw.circle(screen, node_color, self.node.coordinate, self.size)
        pygame.draw.circle(screen, self.border_color, self.node.coordinate, self.size, self.border_width)

        text_surface = self.font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.node.coordinate)
        screen.blit(text_surface, text_rect)


    