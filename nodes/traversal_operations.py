from nodes.node import Node


def unhighlight_nodes(node: Node) -> None:
    if node:
        node.highlighted = False
        if node.left:
            unhighlight_nodes(node.left)
        if node.right:
            unhighlight_nodes(node.right)


def preorder_traversal(root: Node) -> list:
    result = []
    stack = [(root, None)]
    
    while stack:
        node, parent = stack.pop()
        
        if node and not node.is_empty:
            if parent:
                result.append((parent, node))
            result.append(node)
            
            if node.right and not node.right.is_empty:
                stack.append((node.right, node))
            if node.left and not node.left.is_empty:
                stack.append((node.left, node))
    
    return result



def postorder_traversal(root: Node):
    result = []
    def traverse(node):
        if node and not node.is_empty:
            traverse(node.left)
            traverse(node.right)
            
            if node.left and not node.left.is_empty and node.right and not node.right.is_empty:
                result.append(((node.left, node), (node.right, node)))
            elif node.left and not node.left.is_empty:
                result.append((node.left, node))
            elif node.right and not node.right.is_empty:
                result.append((node.right, node))
                
            result.append(node)
    
    traverse(root)
    return result



    
    
    





