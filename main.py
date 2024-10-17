import pygame
import sys
from edit_button import Edit_Button
from node import *
from constants import *
from tree_operations import *


class Visualizer:
    def __init__(self, root):
        self.root = root
        self.outline_width = NODE_BORDER_WIDTH
        self.outline_color = BLACK
        self.edit_mode = False

        pygame.init()
        self.font = pygame.font.SysFont('arial', FONT_SIZE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Binary Tree Visualizer")
        self.running = True
        
        self.edit_button = Edit_Button(self.font)


    def draw_edges(self, parent):
        def draw_single_edge(child):
            if child and (self.edit_mode or not child.is_empty):
                pygame.draw.line(self.screen, self.outline_color, child.coordinate, parent.coordinate, self.outline_width)
                self.draw_edges(child)
        draw_single_edge(parent.left)
        draw_single_edge(parent.right)
        

    def draw_nodes(self, node):
        drawn_node = NodeVisualizer(node, self.font, self.outline_width, self.outline_color, self.edit_mode)
        drawn_node.draw(self.screen)
        
        if node.left:
            self.draw_nodes(node.left)
        if node.right:    
            self.draw_nodes(node.right)
            

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.edit_button.is_hovered(mouse_pos):
                    self.edit_mode = not self.edit_mode
                    self.outline_color = GREEN if self.edit_mode else BLACK
                
                clicked_node = NodeVisualizer(self.root, self.font, self.outline_width, self.outline_color, self.edit_mode).find_clicked_node(mouse_pos)
                if clicked_node is not None:
                    clicked_node.fill(1)
                    generate_coordinates(clicked_node)                
            
             
    


    def run(self):
        while self.running:
            self.handle_events()
                        
            self.screen.fill(BACKGROUND_COLOR)

            self.edit_button.draw(self.screen, self.outline_color)
            self.draw_edges(self.root)
            self.draw_nodes(self.root)

            pygame.display.flip()

def main():
    root = setup_nodes()

    visualizer = Visualizer(root)
    visualizer.run()

if __name__ == "__main__":
    main()
