class ModeManager():
    def __init__(self):
        self.view_mode = True
        self.edit_mode = False
        self.frozen_mode = False
        self.traversal_mode = False
        self.traversal_pick_mode = False
    
    
    def get_mode(self) -> str:
        if self.view_mode:
            return "view"
        elif self.edit_mode:
            return "edit"
        elif self.frozen_mode:
            return "frozen"
        elif self.traversal_mode:
            return "traversal"
        elif self.traversal_pick_mode:
            return "traversal_pick"
        else:
            raise ValueError("No mode detected.")
        
        
    def set_mode(self, mode_name: str) -> None:
        self.view_mode = False
        self.edit_mode = False
        self.frozen_mode = False
        self.traversal_mode = False
        self.traversal_pick_mode = False
        
        if mode_name == "view":
            self.view_mode = True
        elif mode_name == "edit":
            self.edit_mode = True
        elif mode_name == "frozen":
            self.frozen_mode = True
        elif mode_name == "traversal":
            self.traversal_mode = True
        elif mode_name == "traversal_pick":
            self.traversal_pick_mode = True
        else:
            raise ValueError(f"Unknown mode: {mode_name}")


    def toggle_mode(self, mode_name: str) -> None:
        if mode_name == "edit":
            if self.edit_mode:
                self.edit_mode = False
                self.view_mode = True
            else:
                self.edit_mode = True
                self.view_mode = False
        if mode_name == "traversal":
            if self.traversal_mode:
                self.traversal_mode = False
                self.view_mode = True
            else:
                self.traversal_mode = True
                self.view_mode = False

    def __eq__(self, other):
        return isinstance(other, str) and other == self.get_mode()
    
    
    def __str__(self):
        if self.edit_mode:
            return "edit"
        elif self.frozen_mode:
            return "frozen"
        elif self.traversal_mode:
            return "traversal"
        elif self.view_mode:
            return "view"
        elif self.traversal_pick_mode:
            return "traversal_pick"