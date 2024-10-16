from constants import *
from node import Node
import collections

def tree_height(root: Node) -> int:
    q = collections.deque([root])
    height = 0
    while q:
        height += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return height          


def generate_coordinates(root: Node) -> None:
    heights = [80.0, 240.0, 400.0, 560.0, 720.0]
    q = collections.deque()
    q.append(root)
    tree_level = 0 
    
    while q:
        tree_level += 1
        widths = [((2 * i - 1) * SCREEN_WIDTH) / 2 ** tree_level for i in range(1, 2**(tree_level-1) + 1)]
        
        for i in range(len(q)):
            node = q.popleft()
            
            height_coordinate = heights[tree_level-1]  
            width_coordinate = widths[i]
            node.coordinate = (width_coordinate, height_coordinate)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


def count_nodes(node: Node) -> int:
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)  
            
    
def setup_nodes() -> Node:
    root = Node(1)
    root.left = Node(None)
    root.right = Node(None)
    return root
   


def add_empty_nodes(node: Node) -> None:
    if node and not node.is_empty:
        if node.left:
            add_empty_nodes(node.left)
        else:
            node.left = Node(None)
        if node.right:
            add_empty_nodes(node.right)
        else:
            node.right = Node(None)