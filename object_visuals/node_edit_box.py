from constants import *
import pygame

class Node_Edit_Button:
    def __init__(self, node, node_font): 
        self.node = node       
        self.full_box = self.create_full_box()
        self.exit_box = self.create_exit_box()
        self.save_box = self.create_save_box()
        self.increment_box = self.create_increment_box()
        self.decrement_box = self.create_decrement_box()
        self.button_border_width = 3
        
        self.button_font = self.font = pygame.font.SysFont('gisha', FONT_SIZE-5)
        self.node_font = node_font


    def create_full_box(self):
        x_pos = self.node.coordinate[0] - NODE_SIZE * 2.5
        y_pos = self.node.coordinate[1] - NODE_SIZE * 1.5
        width = NODE_SIZE * 5
        height = NODE_SIZE * 3
        return pygame.Rect(x_pos, y_pos, width, height)

    def draw_full_box(self):
        pygame.draw.rect(self.screen, SHADED_GREEN, self.full_box)
        pygame.draw.rect(self.screen, GREEN, self.full_box, self.button_border_width)       
       
       
    def create_exit_box(self):
        x_pos = self.node.coordinate[0] - NODE_SIZE * 2.2
        y_pos = self.node.coordinate[1] + NODE_SIZE * 0.2
        width = NODE_SIZE
        height = NODE_SIZE
        return pygame.Rect(x_pos, y_pos, width, height)
    
    def draw_exit_box(self):
        pygame.draw.rect(self.screen, LIGHT_RED, self.exit_box)
        pygame.draw.rect(self.screen, GREEN, self.exit_box, self.button_border_width)
        text_surface = self.button_font.render("X", True, BLACK)
        text_rect = text_surface.get_rect(center=self.exit_box.center)
        self.screen.blit(text_surface, text_rect) 
    
    
    def create_save_box(self):
        x_pos = self.node.coordinate[0] - NODE_SIZE * 2.2
        y_pos = self.node.coordinate[1] - NODE_SIZE * 1.2
        width = NODE_SIZE
        height = NODE_SIZE
        return pygame.Rect(x_pos, y_pos, width, height)
    
    def draw_save_box(self):
        pygame.draw.rect(self.screen, LIGHT_GREEN, self.save_box)
        pygame.draw.rect(self.screen, GREEN, self.save_box, self.button_border_width)
        text_surface = self.button_font.render("R", True, BLACK)
        text_rect = text_surface.get_rect(center=self.save_box.center)
        self.screen.blit(text_surface, text_rect)


    def create_increment_box(self):
        node_x, node_y = self.node.coordinate[0], self.node.coordinate[1]
        topx, topy = node_x + NODE_SIZE * 1.7, node_y - NODE_SIZE * 1.15
        leftx, lefty = node_x + NODE_SIZE * 1.3, node_y - NODE_SIZE * 0.2
        rightx, righty = node_x + NODE_SIZE * 2.1, node_y - NODE_SIZE * 0.2
        return [(topx, topy), (leftx, lefty), (rightx, righty)]
    
    def draw_increment_box(self):
        pygame.draw.polygon(self.screen, LIGHT_GREEN, self.increment_box)
        pygame.draw.polygon(self.screen, GREEN, self.increment_box, self.button_border_width)
        
        
    def create_decrement_box(self):
        node_x, node_y = self.node.coordinate[0], self.node.coordinate[1]
        topx, topy = node_x + NODE_SIZE * 1.7, node_y + NODE_SIZE * 1.15
        leftx, lefty = node_x + NODE_SIZE * 1.3, node_y + NODE_SIZE * 0.2
        rightx, righty = node_x + NODE_SIZE * 2.1, node_y + NODE_SIZE * 0.2
        return [(topx, topy), (leftx, lefty), (rightx, righty)]
    
    def draw_decrement_box(self):
        pygame.draw.polygon(self.screen, LIGHT_GREEN, self.decrement_box)
        pygame.draw.polygon(self.screen, GREEN, self.decrement_box, self.button_border_width)

    
    def draw_node(self):
        pygame.draw.circle(self.screen, LIGHT_GREEN, self.node.coordinate, NODE_SIZE)
        pygame.draw.circle(self.screen, GREEN, self.node.coordinate, NODE_SIZE, NODE_BORDER_WIDTH)
        text_surface = self.node_font.render(str(self.node.val), True, BLACK)
        text_rect = text_surface.get_rect(center=self.node.coordinate)
        self.screen.blit(text_surface, text_rect)
        
        
    def draw(self, screen):
        self.screen = screen
        self.draw_full_box()
        self.draw_exit_box()
        self.draw_save_box()
        self.draw_increment_box()
        self.draw_decrement_box()
        self.draw_node()
    
    
    
    
    def is_hovered(self, mouse_pos):
        if self.save_box.collidepoint(mouse_pos):
            self.node.editing = False
            return True
        if self.exit_box.collidepoint(mouse_pos):
            self.node.clear()
            return True
        if self.triangle_is_hovered(mouse_pos, self.increment_box):
            if self.node.val < 99:
                self.node.val += 1
        if self.triangle_is_hovered(mouse_pos, self.decrement_box):
            if self.node.val > 0:
                self.node.val -= 1
    
    def triangle_is_hovered(self, mouse_pos, triangle):
        def area(x1, y1, x2, y2, x3, y3):
            return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)
        
        px, py = mouse_pos
        (x1, y1), (x2, y2), (x3, y3) = triangle

        total_area = area(x1, y1, x2, y2, x3, y3)
        area1 = area(px, py, x2, y2, x3, y3)
        area2 = area(x1, y1, px, py, x3, y3)
        area3 = area(x1, y1, x2, y2, px, py)
        
        return total_area == area1 + area2 + area3
        
    
            