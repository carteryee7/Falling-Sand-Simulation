from models.cell import Cell
from grid import Grid
import random

class SteamCell(Cell):
    def __init__(self, x, y):
        """Initialize a steam cell with light gray color.
        
        Args:
            x: The x-coordinate in the grid
            y: The y-coordinate in the grid
        """
        color = (211, 211, 211)
        super().__init__(color, x, y)
    
    def check_rules(self, grid: Grid):
        """Apply steam physics: rise upward and move diagonally upward.
        
        Args:
            grid: The grid containing this cell
        """
        if grid.grid[self.x][self.y - 1] is None:
            grid.set_cell_pos(self, self.x, self.y - 1)
            
        elif grid.grid[self.x - 1][self.y - 1] is None and grid.grid[self.x + 1][self.y - 1] is None:
            if random.choice([True, False]):
                grid.set_cell_pos(self, self.x - 1, self.y - 1)
            else:
                grid.set_cell_pos(self, self.x + 1, self.y - 1)

        elif grid.grid[self.x - 1][self.y - 1] is None:
            grid.set_cell_pos(self, self.x - 1, self.y - 1)

        elif grid.grid[self.x + 1][self.y - 1] is None:
            grid.set_cell_pos(self, self.x + 1, self.y - 1)

        #behavior for water-like steam
        """elif grid.grid[self.x + 1][self.y] is None:
            grid.set_cell_pos(self, self.x + 1, self.y)

        elif grid.grid[self.x - 1][self.y] is None:
            grid.set_cell_pos(self, self.x - 1, self.y)"""