from cell import Cell
from grid import Grid
import random

class WaterCell(Cell):
    def __init__(self, x, y):
        super().__init__((0, 0, 255), x, y)
    
    def check_rules(self, grid: Grid):
        if grid.grid[self.x][self.y + 1] is None:
            grid.set_cell_pos(self, self.x, self.y + 1)
        elif grid.grid[self.x - 1][self.y + 1] is None and grid.grid[self.x + 1][self.y + 1] is None:
            if random.choice([True, False]):
                grid.set_cell_pos(self, self.x - 1, self.y + 1)
            else:
                grid.set_cell_pos(self, self.x + 1, self.y + 1)
        elif grid.grid[self.x - 1][self.y + 1] is None:
            grid.set_cell_pos(self, self.x - 1, self.y + 1)
        elif grid.grid[self.x + 1][self.y + 1] is None:
            grid.set_cell_pos(self, self.x + 1, self.y + 1)