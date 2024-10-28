import pygame
from constants import *
from nodes import *

class TraversalVisualizer():
    def __init__(self, screen, font, root_node):
        self.traversal_order = []  
        self.current_index = 0  
        self.cycle = TRAVERSAL_CYCLE
        self.root_node = root_node
        self.font = font
        self.screen = screen
        self.line_progress = {}
        
    def create_nodes(self, traversal_type):
        if traversal_type == "postorder":
            self.traversal_order = postorder_traversal(self.root_node)
        elif traversal_type == "preorder":
            self.traversal_order = preorder_traversal(self.root_node)
        elif traversal_type == "inorder":
            self.traversal_order = inorder_traversal(self.root_node)
        
        self.current_index = 0
        self.line_progress.clear()
    
    def clear_traversal(self):
        self.traversal_order = []
        self.current_index = 0
        self.line_progress.clear()
        unhighlight_nodes(self.root_node)


    def traverse_cycle(self):        
        if not self.traversal_order:
            return
        self.draw_traversal()
        if self.current_index >= len(self.traversal_order):
            return

        if self.cycle == 0:
            self.current_index += 1
            self.cycle = TRAVERSAL_CYCLE
        else:
            self.cycle -= 1


    def draw_traversal(self):
        for i in range(self.current_index):
            element = self.traversal_order[i]
            
            if isinstance(element, tuple):
                self.draw_line(element)
        
        for i in range(self.current_index):
            element = self.traversal_order[i]
            
            if isinstance(element, Node):
                self.draw_node(element)


    def calculate_coordinates(self, p_coord, c_coord):
        x1, y1 = p_coord
        x2, y2 = c_coord
        dx, dy = x2 - x1, y2 - y1
        length = (dx**2 + dy**2)**0.5
        unit_dx, unit_dy = dx / length, dy / length
    
        start = (x1 + unit_dx * NODE_SIZE, y1 + unit_dy * NODE_SIZE)
        end = (x2 - unit_dx * NODE_SIZE, y2 - unit_dy * NODE_SIZE)
        return (start, end)


    def draw_line(self, element):
        if isinstance(element[0], tuple):
            for parent, child in element:
                parent_coord, child_coord = self.calculate_coordinates(parent.coordinate, child.coordinate)
                
                self.draw_growing_line(parent_coord, child_coord, speed=1)
        
        else:
            parent, child = element
            parent_coord, child_coord = self.calculate_coordinates(parent.coordinate, child.coordinate)
            self.draw_growing_line(parent_coord, child_coord, speed=1)


    def draw_node(self, element):
        pygame.draw.circle(self.screen, LIGHT_RED, element.coordinate, NODE_SIZE)
        pygame.draw.circle(self.screen, RED, element.coordinate, NODE_SIZE, NODE_BORDER_WIDTH+1)
        text_surface = self.font.render(str(element.val), True, BLACK)
        text_rect = text_surface.get_rect(center=element.coordinate)
        self.screen.blit(text_surface, text_rect)



    def draw_growing_line(self, start, end, speed=0.5):
        key = (start, end)
        
        if key not in self.line_progress:
            self.line_progress[key] = 0 
        
        progress = self.line_progress[key]
        if progress < 1:
            progress += speed / TRAVERSAL_CYCLE
            self.line_progress[key] = min(progress, 1)
        
        current_x = start[0] + (end[0] - start[0]) * progress
        current_y = start[1] + (end[1] - start[1]) * progress
        current_endpoint = (int(current_x), int(current_y))
        
        pygame.draw.line(self.screen, RED, start, current_endpoint, NODE_BORDER_WIDTH+1)
