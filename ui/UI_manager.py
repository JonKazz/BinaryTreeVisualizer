import pygame
from constants import *
from ui.edit_button import Edit_Button
from ui.node_edit_box import Node_Edit_Button
from ui.node_visualization import NodeVisualizer
from nodes.node_operations import *

class UIManager:
    def __init__(self, font):
        self.font = font
        self.edit_button = Edit_Button(self.font)
        self.node_edit_box = None

    def handle_click(self, mouse_pos, vis):
        if vis.currently_editing_node:
            if self.node_edit_box.is_hovered(mouse_pos, self.node_edit_box.increment_box):
                vis.currently_editing_node = False
          
        elif self.edit_button.is_hovered(mouse_pos):
            vis.edit_mode = not vis.edit_mode

        elif vis.edit_mode:
            clicked_node = find_clicked_node(vis.root, mouse_pos)
            if clicked_node is not None:
                if clicked_node.is_empty:
                    clicked_node.fill(1)
                    generate_coordinates(clicked_node)   
                else:
                    clicked_node.editing = True
                    vis.currently_editing_node = True
                    self.node_edit_box = Node_Edit_Button(vis.font, clicked_node)  
    
    
    

    def draw_objects(self, screen, root, edit_mode, currently_editing_node):
        outline_color = DARK_GREY if currently_editing_node else GREEN if edit_mode else BLACK
        self.draw_edges(screen, root, edit_mode, outline_color)
        self.draw_nodes(screen, root, edit_mode, outline_color, currently_editing_node)
        self.edit_button.draw(screen, outline_color)
        
        if currently_editing_node:
            self.node_edit_box.draw(screen)
    
    
    def draw_edges(self, screen, node, edit_mode, outline_color):
        def _draw_edge(child):
            if child is not None and (not child.is_empty or edit_mode):
                pygame.draw.line(screen, outline_color, child.coordinate, node.coordinate, NODE_BORDER_WIDTH)
                self.draw_edges(screen, child, edit_mode, outline_color)
        _draw_edge(node.left)
        _draw_edge(node.right)
    
    
    def draw_nodes(self, screen, node, edit_mode, border_color, frozen) -> None:
        drawn_node = NodeVisualizer(node, self.font, border_color, edit_mode, frozen)
        drawn_node.draw(screen)
        if node.left:
            self.draw_nodes(screen, node.left, edit_mode, border_color, frozen)
        if node.right:
            self.draw_nodes(screen, node.right, edit_mode, border_color, frozen)
            