from constants import *
from nodes.node_operations import find_clicked_node

from ui.mode_manager import ModeManager
from object_visuals import Node_Edit_Button, NodeVisualization, EdgeVisualization
from object_visuals.buttons import *

class ObjectsVisualization:
    def __init__(self, screen, font, root_node):
        self.screen = screen
        self.font = font
        self.root_node = root_node
        self.mode = ModeManager()
        
        self.traverse_button = Traversal_Button() 
        self.preorder_button = Preorder_Button()
        self.postorder_button = Postorder_Button()
        self.inorder_button = Inorder_Button()
        
        self.edit_button = Edit_Button(self.font) 
        self.fill_tree_button = Fill_Button()
        self.node_edit_button = None
    
    
    def draw_objects(self):
        self.outline_color = DARK_GREY if self.mode == "frozen" else GREEN if self.mode == "edit" else BLACK
        self.draw_nodes(self.root_node)
        self.draw_buttons()
    
    
    def draw_buttons(self):
        self.update_buttons()
        self.edit_button.draw(self.screen, self.outline_color)
        if self.mode == "view" or self.mode == "traversal": self.traverse_button.draw(self.screen, self.outline_color)
        if self.mode == "traversal_pick": 
            self.preorder_button.draw(self.screen, self.outline_color)
            self.postorder_button.draw(self.screen, self.outline_color)
            self.inorder_button.draw(self.screen, self.outline_color)
        if self.mode == "edit": self.fill_tree_button.draw(self.screen, self.outline_color)
        if self.mode == "frozen": self.node_edit_button.draw(self.screen)
    
    
    def update_buttons(self):
        self.traverse_button.mode.set_mode(self.mode)
        self.edit_button.mode.set_mode(self.mode)
        self.fill_tree_button.mode.set_mode(self.mode)
    
    
    def create_node_edit_box(self, node):
        self.node_edit_button = Node_Edit_Button(node, self.font)

    def draw_nodes(self, node):
        node_vis = NodeVisualization(node, self.font, self.outline_color, self.mode)
        left_edge_vis = EdgeVisualization(node, node.left, self.mode)
        right_edge_vis = EdgeVisualization(node, node.right, self.mode)
        
        left_edge_vis.draw(self.screen)
        right_edge_vis.draw(self.screen)
        node_vis.draw(self.screen)
        
        if node.left:
            self.draw_nodes(node.left)
        if node.right:
            self.draw_nodes(node.right)
                
    
    def find_clicked_object(self, mouse_pos):
        if self.mode == "frozen" and self.node_edit_button.is_hovered(mouse_pos):
            return self.node_edit_button
        
        if self.mode == "edit" and self.fill_tree_button.is_hovered(mouse_pos):
            return self.fill_tree_button
        
        if self.edit_button.is_hovered(mouse_pos):
            return self.edit_button
        
        if (self.mode == "view" or self.mode == "traversal") and self.traverse_button.is_hovered(mouse_pos):
            self.traverse_button.mode.toggle_mode("traversal")               
            return self.traverse_button
        
        if self.mode == "traversal_pick":
            if self.postorder_button.is_hovered(mouse_pos):
                return self.postorder_button
            if self.preorder_button.is_hovered(mouse_pos):
                return self.preorder_button
            if self.inorder_button.is_hovered(mouse_pos):
                return self.inorder_button
             
        return find_clicked_node(self.root_node, mouse_pos)