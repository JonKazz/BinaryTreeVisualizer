import pygame
import sys
from edit_button import Edit_Button
from node import *
from constants import *
from tree_operations import *


class Visualizer:
    def __init__(self, root):
        self.root = root
        self.height = tree_height(root)
        self.node_size = NODE_SIZE
        self.outline_width = NODE_BORDER_WIDTH
        self.outline_color = BLACK
        self.font_size = FONT_SIZE
        self.edit_mode = False

        # Initialize Pygame and setup screen and font
        pygame.init()
        self.font = pygame.font.SysFont('monaco', self.font_size)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Binary Tree Visualizer")
        self.running = True
        
        self.edit_button = Edit_Button(SCREEN_WIDTH - PADDING - 150, PADDING, 150, 80, "EDIT", self.font)


    def draw_vertices(self, node):
        coordinate = node.coordinate
        if node.left and node.left.val:
            child_coordinate = node.left.coordinate
            pygame.draw.line(self.screen, self.outline_color, child_coordinate, coordinate, self.outline_width)
            self.draw_vertices(node.left)
        if node.right and node.right.val:
            child_coordinate = node.right.coordinate
            pygame.draw.line(self.screen, self.outline_color, child_coordinate, coordinate, self.outline_width)
            self.draw_vertices(node.right)
 

    def draw_nodes(self, node):
        if node:
            node_visualizer = NodeVisualizer(node, self.font, self.node_size, self.outline_width, self.outline_color, self.edit_mode)
            node_visualizer.draw(self.screen)
            self.draw_nodes(node.left)
            self.draw_nodes(node.right)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            
            if self.edit_button.is_clicked(event):
                self.edit_mode = not self.edit_mode
            
                self.outline_color = GREEN if self.edit_mode else BLACK
    


    def run(self):
        """ Main loop to run the visualization """
        while self.running:
            self.handle_events()
                        
            self.screen.fill(BACKGROUND_COLOR)

            self.edit_button.draw(self.screen, self.outline_color)
            self.draw_vertices(self.root)
            self.draw_nodes(self.root)

            pygame.display.flip()

def main():
    root = setup_nodes()

    generate_coordinates(root)

    visualizer = Visualizer(root)
    visualizer.run()

if __name__ == "__main__":
    main()
