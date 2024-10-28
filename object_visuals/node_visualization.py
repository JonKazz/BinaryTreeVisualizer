import pygame
from constants import *
from ui.mode_manager import ModeManager
from nodes.node_operations import is_hovered


class NodeVisualization:
    def __init__(self, node, font, border_color, mode):
        self.node = node
        self.font = font
        self.border_color = border_color
        self.mode = mode    
    
    def get_node_color(self, hovered):  
        if self.mode == "frozen":
            if self.node.editing:
                return LIGHT_GREEN
            return GREY
        
        if self.mode == "edit":
            if self.node.is_empty:
                return SHADED_GREEN if hovered else LIGHT_GREEN
            else:
                return SHADED_WHITE if hovered else WHITE

        return WHITE


    def get_border_color(self):
        if self.node.editing:
            return GREEN
        return self.border_color


    def get_text(self, hovered):
        if self.node.is_empty:
            return "+"
        if hovered and self.mode == "edit":
            return "?"
        else:
            return str(self.node.val)
        
        
    def draw(self, screen) -> None:
        mouse_pos = pygame.mouse.get_pos()
        hovered = is_hovered(self.node, mouse_pos)
        
        node_color = self.get_node_color(hovered)
        border_color = self.get_border_color()
        text = self.get_text(hovered)

        if not self.node.is_empty or (self.node.is_empty and self.mode == "edit"):
            pygame.draw.circle(screen, node_color, self.node.coordinate, NODE_SIZE)
            pygame.draw.circle(screen, border_color, self.node.coordinate, NODE_SIZE, NODE_BORDER_WIDTH)

            text_surface = self.font.render(text, True, BLACK)
            text_rect = text_surface.get_rect(center=self.node.coordinate)
            screen.blit(text_surface, text_rect)
    
    



    