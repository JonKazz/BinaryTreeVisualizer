import pygame
from constants import *

class EdgeVisualization():
    def __init__(self, parent, child, mode):
        self.mode = mode
        self.parent_coord = parent.coordinate
        self.child_coord = self.generate_child_coordinate(child)
        self.highlighted = False
    
    def generate_child_coordinate(self, node):
        if not node:
            return None
        if not node.is_empty or (self.mode == "edit" and node.is_empty):
            return node.coordinate
    
    def get_color(self):
        if self.mode == "edit":
            return GREEN
        return BLACK
    
    def draw(self, screen):
        if self.child_coord:
            color = self.get_color()
            pygame.draw.line(screen, color, self.parent_coord, self.child_coord, NODE_BORDER_WIDTH)