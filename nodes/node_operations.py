import math
from collections import deque
from constants import *
from nodes.node import Node

def setup_nodes() -> Node:
    root = Node(None)
    root.coordinate = (600, 80)
    root.fill(1)
    generate_coordinates(root)
    return root

def generate_coordinates(node: Node) -> None:
    if node:
        parent_wc, parent_hc = node.coordinate
        
        tree_level = int((parent_hc - 80) / 160)
        if tree_level == 4:
            return None
        
        if node.left:
            child_hc = parent_hc + 160
            child_wc = parent_wc - (300 / 2 ** tree_level)
            node.left.coordinate = (child_wc, child_hc)
            generate_coordinates(node.left)
            
        if node.right:
            child_hc = parent_hc + 160
            child_wc = parent_wc + (300 / 2 ** tree_level)
            node.right.coordinate = (child_wc, child_hc)
            generate_coordinates(node.right)


def fill_tree(root: Node) -> None:
    if root.is_empty: root.fill(1)
    value = root.val
    q = deque([root])
    
    while q:
        node = q.popleft()
        node.fill(value)
        generate_coordinates(node)
        value += 1
        
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


def is_hovered(node, mouse_pos) -> bool:
    distance = math.sqrt((mouse_pos[0] - node.coordinate[0]) ** 2 + (mouse_pos[1] - node.coordinate[1]) ** 2)
    return distance <= NODE_SIZE


def find_clicked_node(node, mouse_pos) -> Node:
    if is_hovered(node, mouse_pos):
        return node
    
    if node.left:
        checked_node = find_clicked_node(node.left, mouse_pos)
        if checked_node:
            return checked_node
    if node.right:
        checked_node = find_clicked_node(node.right, mouse_pos)
        if checked_node:
            return checked_node
        
    return None

def unhighlight_nodes(node) -> None:
    if node:
        node.highlighted = False
        if node.left:
            unhighlight_nodes(node.left)
        if node.right:
            unhighlight_nodes(node.right)
            
            
            
def preorder_traversal(root) -> list[Node]:
    nodes = []
    
    q = deque()
    q.append(root)
    while q:
        node = q.pop()
        nodes.append(node)
        if node.right and not node.right.is_empty:
            q.append(node.right)
        if node.left and not node.left.is_empty:
            q.append(node.left)
                
    return nodes



def preorder_traversal_test(root) -> list[Node]:
    nodes = []
    
    q = deque()
    q.append(root)
    while q:
        node = q.pop()
        nodes.append(node)
        if node.right and not node.right.is_empty:
            q.append(node.right)
        if node.left and not node.left.is_empty:
            q.append(node.left)
                
    return nodes





    

