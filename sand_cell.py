from cell import Cell
from grid import Grid
import random

class SandCell(Cell):
    def __init__(self, x, y):
        colors = [(194, 178, 128), (194, 178, 128), (226, 202, 118), (250, 213, 165),
        (241, 213, 129), (168, 143, 89), (193, 154, 107), (194, 178, 128),
        (194, 178, 128), (194, 178, 128), (194, 178, 128), (194, 178, 128),
        (194, 178, 128), (194, 178, 128), (194, 178, 128), (194, 178, 128)]

        pick = random.randint(0, 15)
        super().__init__(colors[pick], x, y)
    
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