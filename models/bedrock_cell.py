from models.cell import Cell
from grid import Grid

class  BedrockCell(Cell):
    def __init__(self, x, y):
        """Initialize a bedrock cell with black color.
        
        Args:
            x: The x-coordinate in the grid
            y: The y-coordinate in the grid
        """
        color = (0, 0, 0)
        super().__init__(color, x, y)
    
    def check_rules(self, grid: Grid):
        """Apply bedrock physics: remains stationary (no movement).
        
        Args:
            grid: The grid containing this cell
        """
        pass