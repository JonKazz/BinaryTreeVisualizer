from constants import *
from object_visuals.edit_button import Edit_Button
from object_visuals.node_edit_box import Node_Edit_Button
from object_visuals.node_visualization import NodeVisualization
from object_visuals.traversal_button import Traversal_Button
from object_visuals.fill_tree_button import Fill_Button
from nodes.node_operations import find_clicked_node

class ObjectsVisualization:
    def __init__(self, screen, font, root_node):
        self.screen = screen
        self.font = font
        self.root_node = root_node
        
        self.edit_mode = False
        self.frozen_mode = False 
        self.traversal_mode = False
        
        self.traverse_button = Traversal_Button() 
        self.edit_button = Edit_Button(self.font) 
        self.fill_tree_button = Fill_Button()
        self.node_edit_button = None
    
    def draw_objects(self):
        self.outline_color = DARK_GREY if self.frozen_mode else GREEN if self.edit_mode else BLACK
        self.draw_nodes(self.root_node)
        self.draw_buttons()
    
    
    def draw_buttons(self):
        self.update_buttons()
        self.edit_button.draw(self.screen, self.outline_color)
        if not self.edit_mode: self.traverse_button.draw(self.screen, self.outline_color)
        if self.edit_mode: self.fill_tree_button.draw(self.screen, self.outline_color)
        if self.frozen_mode: self.node_edit_button.draw(self.screen)
    
    def update_buttons(self):
        self.traverse_button.frozen_mode = self.frozen_mode
        self.edit_button.frozen_mode = self.frozen_mode
        self.edit_button.traversal_mode = self.traversal_mode
        self.fill_tree_button.frozen_mode = self.frozen_mode
    
    
    def create_node_edit_box(self, node):
        self.node_edit_button = Node_Edit_Button(node, self.font)

    def draw_nodes(self, node):
        drawn_node = NodeVisualization(node, self.font, self.outline_color, self.edit_mode, self.frozen_mode)
        drawn_node.draw_left_edge(self.screen)
        drawn_node.draw_right_edge(self.screen)
        drawn_node.draw_node(self.screen)
        
        if node.left:
            self.draw_nodes(node.left)
        if node.right:
            self.draw_nodes(node.right)
                
    
    def find_clicked_object(self, mouse_pos):
        if self.frozen_mode and self.node_edit_button.is_hovered(mouse_pos):
            return self.node_edit_button
        
        if self.edit_button.is_hovered(mouse_pos):
            return self.edit_button

        if self.fill_tree_button.is_hovered(mouse_pos) and self.edit_mode:
            return self.fill_tree_button
        
        if self.traverse_button.is_hovered(mouse_pos):
            self.traverse_button.traversal_mode = not self.traverse_button.traversal_mode
            return self.traverse_button
        
        return find_clicked_node(self.root_node, mouse_pos)