from abc import ABC, abstractmethod

class Cell(ABC):
    def __init__(self, color, x, y):
        """Initialize a cell with a color and position.
        
        Args:
            color: RGB color tuple for the cell
            x: The x-coordinate in the grid
            y: The y-coordinate in the grid
        """
        self.color = color
        self.x = x
        self.y = y
    
    @abstractmethod
    def check_rules(self):
        """Apply physics rules to determine cell behavior and movement.
        
        This method must be implemented by all subclasses to define
        how the cell interacts with the grid and other cells.
        """
        pass