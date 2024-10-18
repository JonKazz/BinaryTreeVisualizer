# from ui.node_visualization import NodeVisualizer
# from constants import *
# from nodes.node_operations import *

# class NodeManager:
#     def __init__(self, root, font):
#         self.root = root
#         self.font = font

#     def handle_node_click(self, mouse_pos, visualizer):
#         if visualizer.edit_mode:
#             clicked_node = find_clicked_node(self.root, mouse_pos)
#             if clicked_node is None:
#                 return

#             if clicked_node.is_empty:
#                 clicked_node.fill(1)
#                 generate_coordinates(clicked_node)
#             else:
#                 visualizer.editing_node_value = True
#                 visualizer.edit_mode = False
#                 self.draw_edit_node(visualizer, clicked_node)

#     def draw_edit_node(self, visualizer, node):
#         editing = True
#         while editing:
#             visualizer.handle_events()
#             visualizer.draw_objects()
#             edited_node = NodeVisualizer(node, self.font, NODE_BORDER_WIDTH, BLACK, visualizer.edit_mode)
#             editing = not edited_node.draw_edit_screen(node.coordinate[0], node.coordinate[1], visualizer.screen)
#             pygame.display.flip()
#         visualizer.editing_node_value = False

#     def draw_nodes(self, screen):
#         self._draw_edges(self.root, screen)
#         self._draw_nodes(self.root, screen)


#     def _draw_edges(self, parent, screen):
#         def draw_single_edge(child):
#             if child and not child.is_empty:
#                 pygame.draw.line(screen, BLACK, child.coordinate, parent.coordinate, NODE_BORDER_WIDTH)
#                 self._draw_edges(child, screen)
#         draw_single_edge(parent.left)
#         draw_single_edge(parent.right)


#     def _draw_nodes(self, node, screen):
#         drawn_node = NodeVisualizer(node, self.font, NODE_BORDER_WIDTH, BLACK, False)
#         drawn_node.draw_node(screen)

#         if node.left:
#             self._draw_nodes(node.left, screen)
#         if node.right:
#             self._draw_nodes(node.right, screen)
