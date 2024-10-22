from constants import *
import pygame

class Node_Edit_Button:
    def __init__(self, node, node_font): 
        self.node = node       
        self.total_box = self.create_total_box()
        self.exit_box = self.create_exit_box()
        self.save_box = self.create_save_box()
        self.button_font = self.font = pygame.font.SysFont('gisha', FONT_SIZE-5)
        self.node_font = node_font
        self.default_color = WHITE
        self.hover_color = SHADED_WHITE

    def create_total_box(self):
        x_pos = self.node.coordinate[0] - NODE_SIZE * 2.5
        y_pos = self.node.coordinate[1] - NODE_SIZE * 1.5
        width = NODE_SIZE * 5
        height = NODE_SIZE * 3
        return pygame.Rect(x_pos, y_pos, width, height)
    
    def create_exit_box(self):
        x_pos = self.node.coordinate[0] - NODE_SIZE * 2.2
        y_pos = self.node.coordinate[1] + NODE_SIZE * 0.2
        width = NODE_SIZE
        height = NODE_SIZE
        return pygame.Rect(x_pos, y_pos, width, height)
    
    def create_save_box(self):
        x_pos = self.node.coordinate[0] - NODE_SIZE * 2.2
        y_pos = self.node.coordinate[1] - NODE_SIZE * 1.2
        width = NODE_SIZE
        height = NODE_SIZE
        return pygame.Rect(x_pos, y_pos, width, height)


    def is_hovered(self, mouse_pos):
        if self.save_box.collidepoint(mouse_pos):
            self.node.editing = False
            return True
        if self.exit_box.collidepoint(mouse_pos):
            self.node.clear()
            return True


    def draw(self, screen):
        pygame.draw.rect(screen, SHADED_GREEN, self.total_box)
        pygame.draw.rect(screen, GREEN, self.total_box, 3)
        
        pygame.draw.rect(screen, LIGHT_RED, self.exit_box)
        pygame.draw.rect(screen, GREEN, self.exit_box, 3)
        text_surface = self.button_font.render("X", True, BLACK)
        text_rect = text_surface.get_rect(center=self.exit_box.center)
        screen.blit(text_surface, text_rect)
        
        pygame.draw.rect(screen, LIGHT_BLUE, self.save_box)
        pygame.draw.rect(screen, GREEN, self.save_box, 3)
        text_surface = self.button_font.render("R", True, BLACK)
        text_rect = text_surface.get_rect(center=self.save_box.center)
        screen.blit(text_surface, text_rect)
        
        pygame.draw.circle(screen, LIGHT_GREEN, self.node.coordinate, NODE_SIZE)
        pygame.draw.circle(screen, GREEN, self.node.coordinate, NODE_SIZE, NODE_BORDER_WIDTH)
        text_surface = self.node_font.render(str(self.node.val), True, BLACK)
        text_rect = text_surface.get_rect(center=self.node.coordinate)
        screen.blit(text_surface, text_rect)
    
            