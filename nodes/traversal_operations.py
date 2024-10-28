from nodes.node import Node


def unhighlight_nodes(node: Node) -> None:
    if node:
        node.highlighted = False
        if node.left:
            unhighlight_nodes(node.left)
        if node.right:
            unhighlight_nodes(node.right)



def preorder_traversal(root: Node):
    result = []
    def traverse(node):
        result.append(node)
        
        if node.left and not node.left.is_empty:
            result.append((node, node.left))
            traverse(node.left)
        
        if node.right and not node.right.is_empty:
            result.append((node, node.right))
            traverse(node.right)
    
    traverse(root)
    return result


def postorder_traversal(root: Node):
    result = []
    def traverse(node):
        if node.left and not node.left.is_empty:
            result.append((node, node.left))
            traverse(node.left)
        
        if node.right and not node.right.is_empty:
            result.append((node, node.right))
            traverse(node.right)
        
        result.append(node)
    
    traverse(root)
    return result


def inorder_traversal(root: Node) -> list:
    result = []
    
    def traverse(node: Node) -> None:
        if node.left and not node.left.is_empty:
            result.append((node, node.left))
            traverse(node.left)
            
        result.append(node)
        
        if node.right and not node.right.is_empty:
            result.append((node, node.right))
            traverse(node.right)
    
    traverse(root)
    return result



    
    
    





