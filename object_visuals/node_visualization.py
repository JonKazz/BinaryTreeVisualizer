import pygame
from constants import *
from nodes.node_operations import is_hovered


class NodeVisualization:
    def __init__(self, node, font, border_color, edit_mode, frozen):
        self.node = node
        self.size = NODE_SIZE
        self.font = font
        self.border_color = border_color
        self.border_width = NODE_BORDER_WIDTH
        self.edit_mode = edit_mode
        self.frozen = frozen
    
    
    def get_node_color(self, hovered):
        if self.frozen:
            if self.node.editing:
                return LIGHT_GREEN
            return GREY
        
        if self.edit_mode:
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
        if hovered and self.edit_mode and not self.frozen:
            return "?"
        else:
            return str(self.node.val)
     
     
    def draw(self, screen) -> None:
        mouse_pos = pygame.mouse.get_pos()
        hovered = is_hovered(self.node, mouse_pos)
        
        node_color = self.get_node_color(hovered)
        border_color = self.get_border_color()
        text = self.get_text(hovered)

        if not self.node.is_empty or (self.node.is_empty and self.edit_mode):
            pygame.draw.circle(screen, node_color, self.node.coordinate, self.size)
            pygame.draw.circle(screen, border_color, self.node.coordinate, self.size, self.border_width)

            text_surface = self.font.render(text, True, BLACK)
            text_rect = text_surface.get_rect(center=self.node.coordinate)
            screen.blit(text_surface, text_rect)


    