from nodes.node_operations import preorder_traversal, unhighlight_nodes
from object_visuals.node_visualization import NodeVisualization
from constants import *

class TraversalVisualizer():
    def __init__(self, root_node):
        self.nodes = None
        self.cycle = TRAVERSAL_CYCLE
        self.root_node = root_node
        
    def create_nodes(self):
        self.nodes = preorder_traversal(self.root_node)
    
    def clear_traversal(self):
        self.nodes = None
        unhighlight_nodes(self.root_node)

    def traverse_cycle(self):
        if not self.nodes:
            return
        if self.cycle == 0:
            self.nodes[0].highlighted = True
            self.nodes.pop(0)
            self.cycle = TRAVERSAL_CYCLE
        else:
            self.cycle -= 1
        