import pygame
import sys
from constants import *
from nodes.node_operations import setup_nodes
from ui.UI_manager import UIManager

class Visualizer:
    def __init__(self, root):
        self.root = root
        self.edit_mode = False
        self.currently_editing_node = False

        pygame.init()
        self.font = pygame.font.SysFont('arial', FONT_SIZE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Binary Tree Visualizer")
        self.running = True
        
        self.ui_manager = UIManager(self.font)
            

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_application()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.ui_manager.handle_click(mouse_pos, self)           
            
             
    def quit_application(self):
        self.running = False
        pygame.quit()
        sys.exit()


    def run(self):
        while self.running:
            self.handle_events()
            self.screen.fill(BACKGROUND_COLOR)
            self.ui_manager.draw_objects(self.screen, self.root, self.edit_mode, self.currently_editing_node)
            pygame.display.flip()


def main():
    root = setup_nodes()
    visualizer = Visualizer(root)
    visualizer.run()

if __name__ == "__main__":
    main()
