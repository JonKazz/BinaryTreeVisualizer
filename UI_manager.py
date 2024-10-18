from constants import *
from ui.edit_button import Edit_Button
from nodes.node_operations import *

class UIManager:
    def __init__(self, font):
        self.font = font
        self.edit_button = Edit_Button(self.font)

    def handle_click(self, mouse_pos, vis):
        if vis.currently_editing_node:
            self.draw_node_edit_box
        
        if self.edit_button.is_hovered(mouse_pos):
            vis.edit_mode = not vis.edit_mode
            vis.outline_color = GREEN if vis.edit_mode else BLACK

        elif vis.edit_mode:
            clicked_node = find_clicked_node(vis.root, mouse_pos)
            if clicked_node is not None:
                if clicked_node.is_empty:
                    clicked_node.fill(1)
                    generate_coordinates(clicked_node)   
                else:
                    vis.currently_editing_node = True      


    def draw_objects(self, screen, root, edit_mode):
        outline_color = GREEN if edit_mode else BLACK
        self.draw_edges(screen, root, edit_mode, outline_color)
        self.draw_nodes(screen, root, edit_mode, outline_color)
        self.edit_button.draw(screen, outline_color)
    
    
    def draw_edges(self, screen, node, edit_mode, outline_color):
        def _draw_edge(child):
            if child is not None and (not child.is_empty or edit_mode):
                pygame.draw.line(screen, outline_color, child.coordinate, node.coordinate, NODE_BORDER_WIDTH)
                self.draw_edges(screen, child, edit_mode, outline_color)
        _draw_edge(node.left)
        _draw_edge(node.right)
    
    
    def draw_nodes(self, screen, node, edit_mode, border_color) -> None:
        mouse_pos = pygame.mouse.get_pos()
        hovered = is_hovered(node, mouse_pos)
        
        if not node.is_empty or (node.is_empty and edit_mode):
            if node.is_empty:
                node_color = SHADED_GREEN if edit_mode and hovered else LIGHT_GREEN
                text = "+"
            else:
                node_color = SHADED_WHITE if edit_mode and hovered else WHITE
                text = "?" if edit_mode and hovered else str(node.val)

            pygame.draw.circle(screen, node_color, node.coordinate, NODE_SIZE)
            pygame.draw.circle(screen, border_color, node.coordinate, NODE_SIZE, NODE_BORDER_WIDTH)

            text_surface = self.font.render(text, True, BLACK)
            text_rect = text_surface.get_rect(center=node.coordinate)
            screen.blit(text_surface, text_rect)
        
        if node.left:
            self.draw_nodes(screen, node.left, edit_mode, border_color)
        if node.right:
            self.draw_nodes(screen, node.right, edit_mode, border_color)
            