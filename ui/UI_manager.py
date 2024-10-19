import pygame
from constants import *
from nodes.node_operations import *
from ui.UI_draw_objects import ObjectsVisualization
from object_visuals.edit_button import Edit_Button
from object_visuals.node_edit_box import Node_Edit_Button

class UIManager:
    def __init__(self, screen, font, root_node, edit_mode, frozen_mode):
        self.screen = screen
        self.font = font
        self.root_node = root_node
        self.edit_mode = edit_mode
        self.frozen_mode = frozen_mode
        
        self.object_visualizer = ObjectsVisualization(screen, font, root_node, edit_mode, frozen_mode)


    def handle_click(self, mouse_pos):
        clicked_object = self.object_visualizer.find_clicked_object(mouse_pos)
        
        if self.frozen_mode:
            if type(clicked_object) is Node_Edit_Button:
                clicked_object.node.editing = False
                self.frozen_mode = False
          
        elif type(clicked_object) is Edit_Button:
            self.edit_mode = not self.edit_mode

        elif type(clicked_object) is Node and self.edit_mode:
            if clicked_object.is_empty:
                clicked_object.fill(1)
                generate_coordinates(clicked_object)   
            else:
                self.object_visualizer.create_node_edit_box(clicked_object)
                clicked_object.editing = True
                self.frozen_mode = True        
        
        self.update_object_visualizer()
    
    
    def update_object_visualizer(self):
        self.object_visualizer.edit_mode = self.edit_mode
        self.object_visualizer.frozen_mode = self.frozen_mode
        
    def draw_objects(self):
        self.object_visualizer.draw_objects()
    

    