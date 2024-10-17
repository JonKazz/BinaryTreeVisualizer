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



def generate_coordinates(node: Node) -> None:
    if node:
        parent_wc, parent_hc = node.coordinate
        height = [80.0, 240.0, 400.0, 560.0, 720.0].index(parent_hc)
        if height == 4:
            return None
        if node.left:
            child_hc = parent_hc + 160
            child_wc = parent_wc - (300 / 2 ** height)
            node.left.coordinate = (child_wc, child_hc)
            generate_coordinates(node.left)
        if node.right:
            child_hc = parent_hc + 160
            child_wc = parent_wc + (300 / 2 ** height)
            node.right.coordinate = (child_wc, child_hc)
            generate_coordinates(node.right)
        


def count_nodes(node: Node) -> int:
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)  
            
    
def setup_nodes() -> Node:
    root = Node(1)
    root.coordinate = (600, 80)
    
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