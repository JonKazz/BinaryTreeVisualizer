import pygame
import sys
from constants import *
from nodes.node_operations import setup_nodes
from ui.UI_manager import UIManager

class Visualizer:
    def __init__(self, root_node):
        self.root_node = root_node

        pygame.init()
        self.font = pygame.font.SysFont('arial', FONT_SIZE)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Binary Tree Visualizer")
        self.running = True
        
        self.ui_manager = UIManager(self.screen, self.font, self.root_node)
            

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_application()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.ui_manager.handle_click(mouse_pos)           
            
             
    def quit_application(self):
        self.running = False
        pygame.quit()
        sys.exit()


    def run(self):
        while self.running:
            self.handle_events()
            self.screen.fill(BACKGROUND_COLOR)
            self.ui_manager.draw_objects()
            pygame.display.flip()


def main():
    root_node = setup_nodes()
    visualizer = Visualizer(root_node)
    visualizer.run()

if __name__ == "__main__":
    main()
