from constants import *
from nodes import *
from ui.UI_draw_objects import ObjectsVisualization
from ui.UI_traversal_visualizer import TraversalVisualizer
from ui.mode_manager import ModeManager
from object_visuals import Node_Edit_Button
from object_visuals.buttons import *

class UIManager:
    def __init__(self, screen, font, root_node):
        self.screen = screen
        self.font = font
        self.root_node = root_node
        self.mode = ModeManager()
        
        self.object_visualizer = ObjectsVisualization(screen, font, root_node)
        self.traversal_visualizer = TraversalVisualizer(screen, font, root_node)


    def handle_click(self, mouse_pos):
        clicked_object = self.object_visualizer.find_clicked_object(mouse_pos)
        
        if self.mode == "frozen":
            if isinstance(clicked_object, Node_Edit_Button):
                self.mode.set_mode("edit")
        
        elif self.mode == "traversal_pick":
            if isinstance(clicked_object, Postorder_Button):
                self.traversal_visualizer.create_nodes("postorder")
                self.mode.set_mode("traversal")
            elif isinstance(clicked_object, Preorder_Button):
                self.traversal_visualizer.create_nodes("preorder")
                self.mode.set_mode("traversal")
            elif isinstance(clicked_object, Inorder_Button):
                self.traversal_visualizer.create_nodes("inorder")
                self.mode.set_mode("traversal")
                
        elif self.mode == "traversal":
            if isinstance(clicked_object, Traversal_Button):
                self.traversal_visualizer.clear_traversal()
                self.mode.set_mode("view")
        
        elif self.mode == "view" and isinstance(clicked_object, Traversal_Button):
            self.mode.set_mode("traversal_pick")
        
        elif isinstance(clicked_object, Edit_Button):
            self.mode.toggle_mode("edit")
            
        elif self.mode == "edit":
            if isinstance(clicked_object, Node):
                if clicked_object.is_empty:
                    clicked_object.fill(1)
                    generate_coordinates(clicked_object)   
                else:
                    self.object_visualizer.create_node_edit_box(clicked_object)
                    clicked_object.editing = True
                    self.mode.set_mode("frozen")
                    
            if isinstance(clicked_object, Fill_Button):
                fill_tree(self.root_node)       
    
        self.update_object_visualizer()
    
    
    def update_object_visualizer(self):
        self.object_visualizer.mode.set_mode(self.mode)
        
    def draw_objects(self):
        self.object_visualizer.draw_objects()
        self.traversal_visualizer.traverse_cycle()
    

    