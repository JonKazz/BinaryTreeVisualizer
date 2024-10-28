class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.coordinate = None
        
        self.is_empty = True if val is None else False
        self.editing = False
        self.highlighted = False
    
    def fill(self, val: int) -> None:
        self.val = val
        self.is_empty = False
        
        tree_level = (self.coordinate[1] - 80) // 160 + 1
        if tree_level < 5:
            self.left = Node(None)
            self.right = Node(None)
    
    def clear(self) -> None:
        self.val = None
        self.left = None
        self.right = None
        self.is_empty = True
        self.editing = False
    
    def __repr__(self) -> str:
        return str(self.val)
