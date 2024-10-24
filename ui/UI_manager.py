import time
from constants import *
from nodes.node_operations import *
from ui.UI_draw_objects import ObjectsVisualization
from ui.UI_traversal_visualizer import TraversalVisualizer
from object_visuals.edit_button import Edit_Button
from object_visuals.node_edit_box import Node_Edit_Button
from object_visuals.fill_tree_button import Fill_Button
from object_visuals.traversal_button import Traversal_Button

class UIManager:
    def __init__(self, screen, font, root_node):
        self.screen = screen
        self.font = font
        self.root_node = root_node
        self.edit_mode = False
        self.frozen_mode = False
        self.traversal_mode = False
        
        self.object_visualizer = ObjectsVisualization(screen, font, root_node)
        self.traversal_visualizer = TraversalVisualizer(root_node)


    def handle_click(self, mouse_pos):
        clicked_object = self.object_visualizer.find_clicked_object(mouse_pos)
        
        if self.frozen_mode:
            if isinstance(clicked_object, Node_Edit_Button):
                self.frozen_mode = False
        
        elif self.traversal_mode:
            if isinstance(clicked_object, Traversal_Button):
                self.traversal_visualizer.clear_traversal()
                self.traversal_mode = False
        
                
        elif isinstance(clicked_object, Traversal_Button):
            self.traversal_visualizer.create_nodes()
            self.traversal_mode = True
        
        elif isinstance(clicked_object, Edit_Button):
            self.edit_mode = not self.edit_mode
            
            
        elif self.edit_mode:
            if isinstance(clicked_object, Node):
                if clicked_object.is_empty:
                    clicked_object.fill(1)
                    generate_coordinates(clicked_object)   
                else:
                    self.object_visualizer.create_node_edit_box(clicked_object)
                    clicked_object.editing = True
                    self.frozen_mode = True 
                    
            if isinstance(clicked_object, Fill_Button):
                fill_tree(self.root_node)       
    
        self.update_object_visualizer()
    
    
    def update_object_visualizer(self):
        self.object_visualizer.edit_mode = self.edit_mode
        self.object_visualizer.frozen_mode = self.frozen_mode
        self.object_visualizer.traversal_mode = self.traversal_mode
        
    def draw_objects(self):
        self.object_visualizer.draw_objects()
        self.traversal_visualizer.traverse_cycle()
    

    