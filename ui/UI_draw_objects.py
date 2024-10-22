import pygame
from constants import *
from object_visuals.edit_button import Edit_Button
from object_visuals.node_edit_box import Node_Edit_Button
from object_visuals.node_visualization import NodeVisualization
from nodes.node_operations import find_clicked_node

class ObjectsVisualization:
    def __init__(self, screen, font, root_node, edit_mode, frozen_mode):
        self.screen = screen
        self.font = font
        self.root_node = root_node
        
        self.edit_mode = edit_mode
        self.frozen_mode = frozen_mode  
        self.edit_button = Edit_Button(self.font) 
        self.node_edit_button = None
    
    def draw_objects(self):
        self.outline_color = DARK_GREY if self.frozen_mode else GREEN if self.edit_mode else BLACK
        self.draw_edges(self.root_node)
        self.draw_nodes(self.root_node)
        self.draw_edit_button()
        if self.frozen_mode: self.draw_node_edit_box()
    
    
    def create_node_edit_box(self, node):
        self.node_edit_button = Node_Edit_Button(node, self.font)
    
    def draw_node_edit_box(self):
        self.node_edit_button.draw(self.screen)
    
    def draw_edit_button(self):
        self.edit_button.frozen_mode = self.frozen_mode
        self.edit_button.draw(self.screen, self.outline_color)
        
    def draw_edges(self, node):
        def _draw_edge(child):
            if child and (not child.is_empty or self.edit_mode):
                pygame.draw.line(self.screen, self.outline_color, child.coordinate, node.coordinate, NODE_BORDER_WIDTH)
                self.draw_edges(child)
        _draw_edge(node.left)
        _draw_edge(node.right)
        

    def draw_nodes(self, node):
        drawn_node = NodeVisualization(node, self.font, self.outline_color, self.edit_mode, self.frozen_mode)
        drawn_node.draw(self.screen)
        
        if node.left:
            self.draw_nodes(node.left)
        if node.right:
            self.draw_nodes(node.right)
                
    
    def find_clicked_object(self, mouse_pos):
        if self.frozen_mode and self.node_edit_button.is_hovered(mouse_pos):
            return self.node_edit_button
        
        if self.edit_button.is_hovered(mouse_pos):
            return self.edit_button

        return find_clicked_node(self.root_node, mouse_pos)
    
        