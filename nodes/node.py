class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.coordinate = None
        self.is_empty = True if val is None else False
        self.editing = False
        
    def fill(self, val):
        self.val = val
        self.is_empty = False
        
        tree_level = (self.coordinate[1] - 80) // 160 + 1
        if tree_level < 5:
            self.left = Node(None)
            self.right = Node(None)

